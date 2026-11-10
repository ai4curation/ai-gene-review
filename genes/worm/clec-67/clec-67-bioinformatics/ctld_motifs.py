"""Inspect the C-type lectin domain (CTLD) of clec-67 (Q8ITX4) for canonical
cysteines and carbohydrate-recognition motifs. Reads the cached UniProt flat file."""
import re
import sys
from pathlib import Path

path = Path(sys.argv[1] if len(sys.argv) > 1 else "../clec-67-uniprot.txt")
text = path.read_text()
seq = "".join(text.split("\nSQ   ")[1].split("\n", 1)[1].split()).rstrip("/")
m = re.search(r"FT   DOMAIN\s+(\d+)\.\.(\d+)\s*\nFT\s+/note=\"C-type lectin\"", text)
start, end = int(m.group(1)), int(m.group(2))
dom = seq[start - 1:end]
print(f"length={len(seq)} CTLD={start}..{end}")
print(f"CTLD sequence: {dom}")
cys = [start + i for i, c in enumerate(dom) if c == "C"]
print(f"CTLD cysteines ({len(cys)}): {cys}")
for motif in ["EPN", "QPD", "WND"]:
    print(f"motif {motif} in CTLD: {motif in dom}")
print(f"total cysteines in protein: {seq.count('C')}")
