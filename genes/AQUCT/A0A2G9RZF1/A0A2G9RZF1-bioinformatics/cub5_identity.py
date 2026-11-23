"""Percent identity of the A0A2G9RZF1 CUB ORF (residues 30-156) to the C-terminal
CUB5 domain of human TLL1, BMP1 and TLL2, from the phmmer domain alignments.

Reads PHMMER_OUT (produced by fetch_and_phmmer.sh); prints, for each target
domain alignment with bit score > 100, the number of identical aligned positions.
"""
import re
from pathlib import Path

import sys
fname = sys.argv[1] if len(sys.argv) > 1 else "phmmer_panel.out"
text = Path(__file__).with_name(fname).read_text()
blocks = re.split(r"\n>> ", text)
for block in blocks[1:]:
    target = block.split()[0]
    for dom in re.split(r"\n  == domain ", block)[1:]:
        m = re.match(r"(\d+)\s+score: ([\d.]+) bits", dom)
        if not m or float(m.group(2)) < 100:
            continue
        lines = [l for l in dom.splitlines()[1:] if l.strip()]
        q, t = "", ""
        # alignment comes in groups of 4 lines: query, match, target, PP
        i = 0
        while i + 3 < len(lines):
            ql, tl = lines[i].split(), lines[i + 2].split()
            if len(ql) >= 4 and len(tl) >= 4:
                q += ql[2]
                t += tl[2]
            i += 4
        pairs = [(a, b) for a, b in zip(q.upper(), t.upper()) if a != "-" and b != "-" and a != "." and b != "."]
        ident = sum(a == b for a, b in pairs)
        print(f"{target}\tdomain {m.group(1)}\t{m.group(2)} bits\tidentical={ident}/{len(pairs)}\t{100*ident/len(pairs):.1f}%")
