"""Re-review: compare all horse DARS2 gene-model products (Ensembl ENSECAG00000004044)
with reviewed human DARS2 (Q6PI48) and map human UniProt binding/region features.

Run: uv run --with biopython python compare_models_rereview.py
Input: dars2_models-rereview.fasta (downloaded from rest.uniprot.org on 2026-10-20)
Output: results-rereview.json (and stdout)
"""
import json
from Bio import SeqIO
from Bio.Align import PairwiseAligner, substitution_matrices

HUMAN = "Q6PI48"
# Human Q6PI48 features (UniProt FT lines, ECO:0000250 / ECO:0000269 where stated)
FEATURES = {
    "transit_peptide_1-47": (1, 47),
    "aspartate_region_244-247": (244, 247),
    "ATP/Asp_binding_266-268": (266, 268),
    "ATP_binding_535": (535, 535),
    "Asp_binding_542": (542, 542),
    "ATP_binding_584-587": (584, 587),
    "N6-acetyllysine_K368": (368, 368),
    "N6-acetyllysine_K382": (382, 382),
}

recs = {r.id.split("|")[1]: str(r.seq) for r in SeqIO.parse("dars2_models-rereview.fasta", "fasta")}
human = recs[HUMAN]
al = PairwiseAligner()
al.substitution_matrix = substitution_matrices.load("BLOSUM62")
al.open_gap_score = -10
al.extend_gap_score = -0.5
al.mode = "global"

out = {}
for acc, seq in recs.items():
    if acc == HUMAN:
        continue
    a = al.align(human, seq)[0]
    # map human position -> horse residue (or None)
    hmap = {}
    for (hs, he), (ts, te) in zip(*a.aligned):
        for i in range(he - hs):
            hmap[hs + i + 1] = (ts + i + 1, seq[ts + i])
    paired = len(hmap)
    ident = sum(1 for hp, (tp, tr) in hmap.items() if human[hp - 1] == tr)
    missing = [p for p in range(1, len(human) + 1) if p not in hmap]
    # compress missing into ranges
    ranges = []
    for p in missing:
        if ranges and p == ranges[-1][1] + 1:
            ranges[-1][1] = p
        else:
            ranges.append([p, p])
    feats = {}
    for name, (s, e) in FEATURES.items():
        hres = human[s - 1:e]
        tres = "".join(hmap[p][1] if p in hmap else "-" for p in range(s, e + 1))
        feats[name] = {"human": hres, "horse": tres, "conserved": hres == tres}
    out[acc] = {
        "length": len(seq),
        "paired_with_human": paired,
        "identity_among_paired": round(ident / paired, 4),
        "human_ranges_absent": ranges,
        "horse_residues_unpaired": len(seq) - paired,
        "c_terminal_20": seq[-20:],
        "features": feats,
    }
out["_human_C_terminal_20"] = human[-20:]
json.dump(out, open("results-rereview.json", "w"), indent=2)
print(json.dumps(out, indent=2))
