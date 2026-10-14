#!/usr/bin/env python3
"""
Notebook Manifest Validator for Lean-Hallucination-Guard

Validates:
- JSON structure of notebooks_manifest.json
- Required fields for each notebook entry
- Existence of corresponding .md scaffolds in /notebooks
- Non-empty interactive component lists
"""

import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "notebooks" / "notebooks_manifest.json"
NOTEBOOK_DIR = ROOT / "notebooks"

REQUIRED_FIELDS = [
    "file_name",
    "target_audience",
    "objective",
    "interactive_components"
]

def fail(msg):
    print(f"[FAIL] {msg}")
    sys.exit(1)

def ok(msg):
    print(f"[OK] {msg}")

def validate_manifest_exists():
    if not MANIFEST_PATH.exists():
        fail(f"Manifest not found: {MANIFEST_PATH}")
    ok("Manifest file exists.")

def load_manifest():
    try:
        with open(MANIFEST_PATH, "r") as f:
            data = json.load(f)
        ok("Manifest JSON loaded successfully.")
        return data
    except json.JSONDecodeError as e:
        fail(f"Invalid JSON in manifest: {e}")

def validate_notebook_entries(manifest):
    suite = manifest.get("demonstration_suite")
    if not isinstance(suite, list):
        fail("Manifest missing 'demonstration_suite' list.")
    ok("Notebook suite list found.")

    for entry in suite:
        for field in REQUIRED_FIELDS:
            if field not in entry:
                fail(f"Notebook entry missing required field: {field}")
        ok(f"Fields validated for: {entry['file_name']}")

        if not isinstance(entry["interactive_components"], list):
            fail(f"interactive_components must be a list for {entry['file_name']}")
        if len(entry["interactive_components"]) == 0:
            fail(f"interactive_components list is empty for {entry['file_name']}")
        ok(f"Interactive components valid for: {entry['file_name']}")

def validate_notebook_files(manifest):
    suite = manifest["demonstration_suite"]

    for entry in suite:
        md_name = entry["file_name"].replace(".ipynb", ".md")
        md_path = NOTEBOOK_DIR / md_name

        if not md_path.exists():
            fail(f"Missing scaffold file: {md_path}")
        ok(f"Scaffold exists: {md_name}")

def main():
    print("=== Validating Notebook Manifest ===")
    validate_manifest_exists()
    manifest = load_manifest()
    validate_notebook_entries(manifest)
    validate_notebook_files(manifest)
    print("\nAll checks passed successfully.")

if __name__ == "__main__":
    main()
