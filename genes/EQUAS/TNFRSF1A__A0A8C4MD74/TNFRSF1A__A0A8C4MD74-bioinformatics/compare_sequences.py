# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython", "requests"]
# ///
"""Compare donkey TNFRSF1A canonical product A0A8C4MD74 with human TNFR1
(P19438, reviewed), mouse Tnfrsf1a (P25118, reviewed) and the horse
full-length model A0A5F5Q204.

For each pair: global identity over aligned positions; and, by human UniProt
coordinates, coverage/identity of every human feature (signal, CRDs, TM,
death domain, regions), the number of the 24 human extracellular cysteines
(positions 22-211) conserved, and whether selected human functional residues
are conserved. Sequences and features are fetched live from UniProt REST.
"""
import json
import requests
from Bio import Align
from Bio.Align import substitution_matrices

TARGET = "A0A8C4MD74"
OTHERS = {"P25118": "mouse Tnfrsf1a (reviewed)", "A0A5F5Q204": "horse TNFRSF1A full-length model"}


def fetch(acc: str) -> str:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    return "".join(r.text.splitlines()[1:])


def features(acc: str) -> list[dict]:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.json", timeout=60)
    r.raise_for_status()
    keep = ("Signal", "Transmembrane", "Domain", "Repeat", "Region", "Motif")
    return [
        {"type": f["type"], "desc": f.get("description", ""),
         "start": f["location"]["start"]["value"], "end": f["location"]["end"]["value"]}
        for f in r.json().get("features", []) if f["type"] in keep
    ]


aligner = Align.PairwiseAligner()
aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
aligner.open_gap_score = -10
aligner.extend_gap_score = -0.5
aligner.mode = "global"


def compare(q: str, ref: str, ref_feats: list[dict] | None) -> dict:
    aln = aligner.align(q, ref)[0]
    r2q: dict[int, int] = {}
    ident = aligned = 0
    for (qs, qe), (rs, re_) in zip(*aln.aligned):
        for i in range(int(qe) - int(qs)):
            r2q[int(rs) + i + 1] = int(qs) + i + 1
            aligned += 1
            ident += q[int(qs) + i] == ref[int(rs) + i]
    out: dict = {
        "query_length": len(q), "ref_length": len(ref), "aligned_positions": aligned,
        "identity_over_aligned": round(ident / aligned, 3),
    }
    if ref_feats is not None:
        cov = {}
        for f in ref_feats:
            span = range(f["start"], f["end"] + 1)
            covered = sum(p in r2q for p in span)
            same = sum(p in r2q and q[r2q[p] - 1] == ref[p - 1] for p in span)
            q_pos = [r2q[p] for p in span if p in r2q]
            cov[f"{f['type']}:{f['desc']}:{f['start']}-{f['end']}"] = {
                "covered_frac": round(covered / len(span), 3),
                "identity_frac": round(same / len(span), 3),
                "query_span": [min(q_pos), max(q_pos)] if q_pos else None,
            }
        out["feature_coverage"] = cov
        hcys = [p for p in range(22, 212) if ref[p - 1] == "C"]
        out["ref_ecd_cysteines"] = len(hcys)
        out["ref_ecd_cysteines_conserved"] = sum(p in r2q and q[r2q[p] - 1] == "C" for p in hcys)
        out["formatted_alignment"] = str(aln)
    return out


q = fetch(TARGET)
human = fetch("P19438")
res = {"target": TARGET, "vs_human_P19438": compare(q, human, features("P19438")), "others": {}}
for acc, label in OTHERS.items():
    res["others"][acc] = {"label": label, **compare(q, fetch(acc), None)}
print(json.dumps(res, indent=2))
