#!/usr/bin/env python3
"""Regenerate data.js from a competitions CSV.

Usage: python3 build.py [path/to/competitions.csv]
Defaults to competitions_full.csv in the current directory.
"""
import csv
import json
import sys

csv_path = sys.argv[1] if len(sys.argv) > 1 else "competitions_full.csv"

with open(csv_path, newline="", encoding="utf-8-sig") as f:
    records = list(csv.DictReader(f))

with open("data.js", "w", encoding="utf-8") as f:
    f.write("const DATA = " + json.dumps(records, ensure_ascii=False) + ";\n")

print(f"Wrote {len(records)} records to data.js")
