#!/usr/bin/env python3
"""Locate ASAP3 D484 relative to the ArfGAP zinc-finger motif.

PMID:23433073 writes "the position homologous to D47 in the other subfamilies
(D484 in ASAP3 structure)".  The `47` is a position in that paper's own consensus
numbering, not a protein residue number, so the offset has to be measured from the
one residue number the paper gives in a real sequence: ASAP3 D484.
"""

from __future__ import annotations

import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from common import uniprot_entry  # noqa: E402

MOTIF = re.compile(r"C.{2}C.{16}C.{2}C.{4}R")

for acc in ("Q8TDY4", "Q8N6T3", "O95081"):
    e = uniprot_entry(acc, "accession,id,sequence,ft_domain,ft_zn_fing")
    seq = e["sequence"]["value"]
    zf = dom = None
    for f in e.get("features", []):
        s, t = f["location"]["start"]["value"], f["location"]["end"]["value"]
        if f["type"] == "Zinc finger":
            zf = (s, t)
        if f["type"] == "Domain" and "Arf-GAP" in (f.get("description") or ""):
            dom = (s, t)
    m = MOTIF.search(seq)
    print(f"\n{acc} {e['uniProtkbId']} len={len(seq)} domain={dom} zf={zf}")
    if m:
        off = m.start()  # 0-based
        cys4 = off + 24  # 1-based position of 4th Cys
        arg = off + 29
        print(f"  motif at {off+1}..{off+len(m.group(0))}: {m.group(0)}")
        print(f"  4th Cys = {cys4}{seq[cys4-1]}   Arg = {arg}{seq[arg-1]}")
        for p in (484, 47, 466):
            if 1 <= p <= len(seq):
                print(f"  residue {p} = {seq[p-1]}  (offset from 4th Cys = {p-cys4}, "
                      f"from Arg = {p-arg})")
        # print the neighbourhood of the motif
        print(f"  seq[{off-5+1}..{off+40}] = {seq[max(0,off-5):off+40]}")
    if acc == "Q8TDY4":
        print(f"  window 470..500: {seq[469:500]}")
        for i, ch in enumerate(seq[469:500], start=470):
            if ch == "D":
                print(f"     Asp at {i}")
