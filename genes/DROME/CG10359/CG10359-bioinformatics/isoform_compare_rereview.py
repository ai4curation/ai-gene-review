# /// script
# requires-python = ">=3.10"
# dependencies = ["requests"]
# ///
"""Compare UniProt entries for FlyBase FBgn0035452 (CG10359) against B7Z0B2.

Run: uv run --script isoform_compare_rereview.py
Prints length and non-equal difflib opcodes (0-based, B7Z0B2 coordinates first).
"""
from difflib import SequenceMatcher

import requests

ACCS = ["B7Z0B2", "B7Z0B3", "Q9VZN7", "Q95S38"]


def seq(acc: str) -> str:
    fa = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60).text
    return "".join(fa.split("\n")[1:])


ref = seq("B7Z0B2")
print("B7Z0B2", len(ref))
for acc in ACCS[1:]:
    s = seq(acc)
    ops = [o for o in SequenceMatcher(None, ref, s, autojunk=False).get_opcodes() if o[0] != "equal"]
    print(acc, len(s), ops)
