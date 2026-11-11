# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Scan the apl2 (O43079) sequence for clathrin-box motifs and report domain layout.

Reads the local UniProt flat file (apl2-uniprot.txt) and reports:
- sequence length
- InterPro/Pfam domain cross-references present in the record
- matches to the clathrin-box consensus L[LI][DEN][LF][DE] (Dell'Angelica 1998 type)
- whether any beta-adaptin appendage-domain signature (IPR015151 / IPR013037 /
  PF09066 / PF02883) is listed
"""
import re
import sys
from pathlib import Path

here = Path(__file__).resolve().parent
uniprot = here.parent / "apl2-uniprot.txt"
text = uniprot.read_text()

seq_block = text.split("\nSQ ")[1].split("\n", 1)[1].split("//")[0]
seq = re.sub(r"\s", "", seq_block)
print(f"length\t{len(seq)}")

dr = [ln for ln in text.splitlines() if ln.startswith(("DR   InterPro", "DR   Pfam", "DR   PANTHER", "DR   PIRSF"))]
for ln in dr:
    print("xref\t" + ln[5:])

appendage_ids = ["IPR015151", "IPR013037", "IPR012295", "PF09066", "PF02883"]
found = [a for a in appendage_ids if a in text]
print(f"appendage_signatures_in_record\t{found if found else 'none'}")

for m in re.finditer(r"L[LI][DEN][LF][DE]", seq):
    s = m.start()
    print(f"clathrin_box\t{s + 1}-{m.end()}\t{m.group()}\tcontext={seq[max(0, s - 10):m.end() + 10]}")

print(f"c_terminus_after_last_clathrin_box\t{seq[m.end():] if 'm' in dir() else 'NA'}")
sys.exit(0)
