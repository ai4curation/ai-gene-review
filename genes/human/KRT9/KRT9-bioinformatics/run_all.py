# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Run the whole KRT9 analysis in order. Usage: uv run run_all.py [--refresh]

--refresh refetches every input from the network (results then reflect the new snapshot);
without it the committed data/ snapshot is reused and only coordinate files are downloaded.
"""
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
STEPS = [
    ["00_fetch.py"] + (["--refresh"] if "--refresh" in sys.argv else []),
    ["01_architecture.py"],
    ["01_architecture.py", "--keratin-gene", "KRT14", "--tag", "control_KRT14"],  # control input
    ["02_variants.py"],
    ["03_statistics.py"],
    ["04_conservation.py"],
    ["05_structure.py"],
    ["06_report_tables.py"],
]
for step in STEPS:
    print(">>>", " ".join(step), flush=True)
    subprocess.run(["uv", "run", "--script", *step], cwd=HERE, check=True)
print("all steps finished")
