# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Locate endocytic-adaptor motifs and the AAK1 site in the donkey NUMB model.

Usage: uv run --script motifs_rereview.py ../NUMB-uniprot.txt human-P49757-uniprot.txt
Reports positions of DPF/NPF motifs, the residue at position 102 (human AAK1
site T102, PMID:18657069), and whether the PID domain feature is present.
"""
import re
import sys


def parse(path):
    seq, inseq, pid = [], False, None
    for line in open(path):
        if line.startswith("SQ"):
            inseq = True
            continue
        if line.startswith("//"):
            break
        if inseq:
            seq.append(line.replace(" ", "").strip())
        m = re.match(r"FT   DOMAIN\s+(\d+)\.\.(\d+)", line)
        if m and pid is None:
            pid = (int(m.group(1)), int(m.group(2)))
    return "".join(seq), pid


for label, path in zip(["donkey", "human"], sys.argv[1:3]):
    s, pid = parse(path)
    print(f"## {label} {path} length {len(s)}")
    print(f"first DOMAIN feature: {pid}")
    print(f"residue 102: {s[101]} (context {s[96:107]})")
    for motif in ["DPF", "NPF"]:
        hits = [m.start() + 1 for m in re.finditer(motif, s)]
        print(f"{motif} motif start positions: {hits}")
    print()
