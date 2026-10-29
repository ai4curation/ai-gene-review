"""Report how much of each reference-protein domain is covered by other sequences in an MSA.

Domain ranges are supplied on the command line as NAME:START-END in reference coordinates.
Coverage = fraction of reference residues in the range aligned to a non-gap residue,
and identity = identical residues over those aligned pairs. Also reports the target
residue span that falls inside the range.
"""

import argparse
import json
from pathlib import Path

from Bio import SeqIO

p = argparse.ArgumentParser()
p.add_argument("alignment")
p.add_argument("--reference", required=True)
p.add_argument("--domains", nargs="+", required=True, help="NAME:START-END")
p.add_argument("--output", required=True)
args = p.parse_args()

seqs = {r.id: str(r.seq) for r in SeqIO.parse(args.alignment, "fasta")}
ref = seqs[args.reference]
ref_col = {}
n = 0
for c, a in enumerate(ref):
    if a != "-":
        n += 1
        ref_col[n] = c

out = {"alignment": args.alignment, "reference": args.reference, "domains": {}}
for spec in args.domains:
    name, rng = spec.split(":")
    start, end = (int(x) for x in rng.split("-"))
    cols = [ref_col[i] for i in range(start, end + 1)]
    entry = {"reference_range": [start, end], "targets": {}}
    for sid, s in seqs.items():
        if sid == args.reference:
            continue
        pos = {}
        k = 0
        for c, a in enumerate(s):
            if a != "-":
                k += 1
                pos[c] = k
        aligned = [c for c in cols if s[c] != "-"]
        ident = sum(ref[c] == s[c] for c in aligned)
        tpos = [pos[c] for c in aligned]
        entry["targets"][sid] = {
            "aligned_fraction": round(len(aligned) / len(cols), 3),
            "identity_over_aligned": round(ident / len(aligned), 3) if aligned else None,
            "target_span": [min(tpos), max(tpos)] if tpos else None,
        }
    out["domains"][name] = entry

Path(args.output).write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps(out, indent=2))
