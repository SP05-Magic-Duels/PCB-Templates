#!/usr/bin/env sh

# Exit immediately if any command fails
set -e

echo "--- Running post-merge KiCad Library Sync Hook ---"

# Check for and run the Python interpreter
if command -v python >/dev/null 2>&1; then
    python scripts/update_pcb_imports.py
elif command -v python3 >/dev/null 2>&1; then
    python3 scripts/update_pcb_imports.py
else
    echo "Warning: Python interpreter not found. Skipping KiCad library sync."
fi

# The script does NOT exit 0 if it failed, relying on 'set -e' for clean exit.
