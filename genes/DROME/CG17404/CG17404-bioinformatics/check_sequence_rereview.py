"""Sequence checks for Q9VGC0 (CG17404) from the cached UniProt flat file.

Reads ../CG17404-uniprot.txt, extracts the sequence and feature table, and
reports: the residues at the annotated ACT_SITE positions, the local motifs
around them, the residue at the chymotrypsin-numbering S1-pocket position 189
(located from the conserved G-D-S-G-G motif: 189 is six residues before the
catalytic Ser), the putative zymogen activation site (R/K immediately before
the mature-N-terminus motif [IV][IV]GG), and the length of the region between
the signal peptide and the S1 domain (where a clip domain would have to sit).
Usage: python3 check_sequence_rereview.py
"""
import json
import re
from pathlib import Path

here = Path(__file__).resolve().parent
text = (here.parent / "CG17404-uniprot.txt").read_text()

seq = "".join(
    re.sub(r"[^A-Z]", "", line)
    for line in text.split("\nSQ   ")[1].split("\n")[1:]
    if not line.startswith("//")
)

features = {}
for m in re.finditer(r"^FT   (\w+)\s+(\d+)(?:\.\.(\d+))?", text, re.M):
    features.setdefault(m.group(1), []).append(
        (int(m.group(2)), int(m.group(3) or m.group(2)))
    )

out = {"accession": "Q9VGC0", "length": len(seq)}
out["act_sites"] = {
    str(start): seq[start - 1] for start, _ in features.get("ACT_SITE", [])
}
out["act_site_context"] = {
    str(start): seq[max(0, start - 6) : start + 5]
    for start, _ in features.get("ACT_SITE", [])
}
gdsgg = [m.start() + 1 for m in re.finditer("GDSGG", seq)]
out["GDSGG_motif_starts"] = gdsgg
if gdsgg:
    cat_ser = gdsgg[0] + 2
    out["catalytic_ser_from_motif"] = cat_ser
    out["S1_pocket_189_position"] = cat_ser - 6
    out["S1_pocket_189_residue"] = seq[cat_ser - 7]
act = [(m.start() + 1, seq[m.start() : m.start() + 6]) for m in re.finditer(r"[RK][IV][IV]GG", seq)]
out["activation_site_candidates"] = [
    {"scissile_bond": f"{seq[p - 1]}{p}-{seq[p]}{p + 1}", "motif": motif}
    for p, motif in act
]
sig_end = features["SIGNAL"][0][1]
dom_start = features["DOMAIN"][0][0]
out["signal_peptide_end"] = sig_end
out["s1_domain_start"] = dom_start
out["prodomain_length_between_signal_and_s1_domain"] = dom_start - sig_end - 1
out["prodomain_sequence"] = seq[sig_end : dom_start - 1]
out["cysteines_in_prodomain"] = seq[sig_end : dom_start - 1].count("C")

print(json.dumps(out, indent=2))
