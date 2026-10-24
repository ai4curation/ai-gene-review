# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython", "requests"]
# ///
"""Compare horse TNFRSF1A gene products (A0A5F5Q204 and the two sibling
Ensembl models from ENSECAG00000016330) with human P19438 and mouse P25118.

Reports length, global identity to human, coverage of human features
(signal peptide 1-21, CRD1-4 22-196 region cysteines, PLAD, TM 212-232,
death domain 356-441, by human UniProt coordinates), and the residues of the
horse sequence aligned before human Met1.
"""
import json
import requests
from Bio import Align
from Bio.Align import substitution_matrices

ACCS = {
    "A0A5F5Q204": "horse benchmark",
    "F6YIE3": "horse sibling model",
    "A0A5F5PQM0": "horse sibling model",
    "P19438": "human canonical",
    "P25118": "mouse canonical",
}


def fetch(acc: str) -> str:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    return "".join(r.text.splitlines()[1:])


def features(acc: str) -> list[dict]:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.json", timeout=60)
    r.raise_for_status()
    out = []
    for f in r.json().get("features", []):
        if f["type"] in ("Signal", "Chain", "Topological domain", "Transmembrane", "Domain", "Repeat", "Region"):
            out.append({"type": f["type"], "desc": f.get("description", ""),
                        "start": f["location"]["start"]["value"], "end": f["location"]["end"]["value"]})
    return out


seqs = {a: fetch(a) for a in ACCS}
human = seqs["P19438"]
hfeat = features("P19438")

aligner = Align.PairwiseAligner()
aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
aligner.open_gap_score = -10
aligner.extend_gap_score = -0.5
aligner.mode = "global"

results = {"human_features": hfeat, "comparisons": {}}
for acc, label in ACCS.items():
    if acc == "P19438":
        continue
    s = seqs[acc]
    aln = aligner.align(s, human)[0]
    # map human positions -> query positions
    h2q = {}
    ident = 0
    aligned = 0
    for (qs, qe), (hs, he) in zip(*aln.aligned):
        qs, qe, hs, he = int(qs), int(qe), int(hs), int(he)
        for i in range(qe - qs):
            h2q[hs + i + 1] = qs + i + 1
            aligned += 1
            if s[qs + i] == human[hs + i]:
                ident += 1
    first_h = min(h2q) if h2q else None
    q_before_h1 = h2q.get(1, None)
    cov = {}
    for f in hfeat:
        if f["type"] in ("Signal", "Transmembrane", "Domain", "Repeat", "Region"):
            span = range(f["start"], f["end"] + 1)
            covered = sum(1 for p in span if p in h2q)
            same = sum(1 for p in span if p in h2q and s[h2q[p] - 1] == human[p - 1])
            cov[f"{f['type']}:{f['desc']}:{f['start']}-{f['end']}"] = {
                "covered_frac": round(covered / len(span), 3),
                "identity_frac": round(same / len(span), 3),
            }
    # cysteines in human extracellular region 22-211 conserved?
    hcys = [p for p in range(22, 212) if human[p - 1] == "C"]
    cys_kept = sum(1 for p in hcys if p in h2q and s[h2q[p] - 1] == "C")
    results["comparisons"][acc] = {
        "label": label,
        "length": len(s),
        "identity_over_aligned_to_human": round(ident / aligned, 3),
        "aligned_positions": aligned,
        "query_residues_before_human_pos1": (q_before_h1 - 1) if q_before_h1 else None,
        "first_human_pos_aligned": first_h,
        "query_Nterm_30": s[:30],
        "human_ecd_cysteines": len(hcys),
        "human_ecd_cysteines_conserved": cys_kept,
        "feature_coverage": cov,
    }

print(json.dumps(results, indent=2))
