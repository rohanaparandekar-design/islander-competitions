# Islander Competitions

Single-file static site (`index.html`) that reads all competition data from `competitions.json`.
No backend, no build step. Deployed via GitHub Pages at islandercompetitions.org.

## Weekly update: adding or editing a competition

Everything the site shows comes from **`competitions.json`** — edit that one file, commit, push.

Each entry in the `competitions` array needs:

| field | notes |
|---|---|
| `id` | unique kebab-case slug; also used in shareable links (`#c/<id>`) |
| `name` | display name |
| `interest` | exactly one of the 6 in `meta.interest_areas` |
| `difficulty` | `Beginner` \| `Intermediate` \| `Advanced` \| `Elite` (drives the quiz path order) |
| `structure` | `solo` \| `team` \| `either` |
| `teacher_required`, `free`, `advisor_required` | booleans |
| `cost_note` | short (e.g. `Free`, `$20 fee`); `cost_detail` = the long version for the detail page |
| `deadline` | ISO date `YYYY-MM-DD` **or `null`** if only a window is known |
| `deadline_note` | human timing, always filled (shown when `deadline` is null); `deadline_display` = long version |
| `grade` | range string: `"9-12"`, `"11"`, `"6-12"` — a single number means that grade only |
| `time_commitment` | `low` \| `medium` \| `high` (quiz filter); `time_commitment_detail` = free text for the detail page |
| `why_it_helps` | one sentence, student-facing — shown on quiz result cards |
| `what_it_is`, `what_you_need_to_do`, `full_timeline`, `notes` | detail-page prose (optional but recommended) |
| `url` | official site |

A `null` deadline is handled everywhere: it sorts last, never shows a negative or "NaN" countdown,
and still appears in quiz results and interest pages. Keep every interest stocked with at least one
competition per difficulty level so the Beginner→Elite path stays complete.

## Setting the two endpoints

Both are constants at the top of the `<script>` block in `index.html`:

```js
const FORM_ENDPOINT   = "https://REPLACE-ME.example.com/subscribe";
const SUBMIT_FORM_URL  = "https://forms.gle/n676c9ysFu3fn17L6";
```

- **`FORM_ENDPOINT`** — the email capture (email + grade + interest) POSTs here. It must return a
  `2xx` response on success (the form only shows "You're on the list ✓" on a real 2xx; anything else
  shows a retry message). Use a **Formspree** form (`https://formspree.io/f/xxxx`) or **Buttondown**
  API endpoint. A Google Form `formResponse` URL will **not** work — it returns an opaque response
  the page can't read. Until this is set, email submits will show the retry message.
- **`SUBMIT_FORM_URL`** — the "Missing a competition? Submit one →" link. Points to a Google Form.
  Owner reviews submissions and adds approved ones to `competitions.json` by hand.

## Local preview

`competitions.json` is loaded with `fetch()`, which browsers block on `file://`. Preview with a
local server: `python3 -m http.server` then open `http://localhost:8000`. The live site is fine.

## Data provenance

`competitions.json` was merged from a curated list (interest / difficulty / quiz fields) and
`competitions_full.csv` (detail-page prose). The CSV is kept for reference only — the site does not
read it. `data.js` is the retired pre-redesign data file, also unused.
