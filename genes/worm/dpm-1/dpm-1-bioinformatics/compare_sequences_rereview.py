# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython", "requests"]
# ///
"""Independent re-review: map U4PF58 (dpm-1 isoform b) onto the canonical
Q9TYJ7 (isoform a) and onto human DPM1 (O60762) and yeast Dpm1 (P14020),
using sequences fetched live from UniProt REST (no local prediction files).

Run: uv run --script compare_sequences_rereview.py > RESULTS-rereview.md
"""
import requests
from Bio import Align
from Bio.Align import substitution_matrices

ACCS = {"U4PF58": "worm dpm-1 isoform b (benchmark)", "Q9TYJ7": "worm dpm-1 isoform a (canonical)",
        "O60762": "human DPM1", "P14020": "yeast DPM1"}


def fetch(acc: str) -> dict:
    return requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.json", timeout=60).json()


def seq(rec: dict) -> str:
    return rec["sequence"]["value"]


def aligner() -> Align.PairwiseAligner:
    a = Align.PairwiseAligner()
    a.substitution_matrix = substitution_matrices.load("BLOSUM62")
    a.open_gap_score = -10
    a.extend_gap_score = -0.5
    return a


def identity_over_aligned(aln) -> tuple[int, int]:
    ident = aligned = 0
    for (s1, e1), (s2, e2) in zip(*aln.aligned):
        for i, j in zip(range(s1, e1), range(s2, e2)):
            aligned += 1
            ident += aln.target[i] == aln.query[j]
    return ident, aligned


recs = {a: fetch(a) for a in ACCS}
print("# dpm-1 re-review: isoform mapping and ortholog comparison\n")
print("Sequences fetched live from UniProt REST by `compare_sequences_rereview.py`.\n")
print("| Accession | Description | Length | Reviewed | PANTHER |")
print("|---|---|---|---|---|")
for a, d in ACCS.items():
    r = recs[a]
    panther = ";".join(x["id"] for x in r.get("uniProtKBCrossReferences", []) if x["database"] == "PANTHER")
    print(f"| {a} | {d} | {len(seq(r))} | {r['entryType']} | {panther} |")

frag, canon = seq(recs["U4PF58"]), seq(recs["Q9TYJ7"])
pos = canon.find(frag)
print("\n## U4PF58 vs canonical Q9TYJ7\n")
if pos >= 0:
    print(f"U4PF58 is an exact substring of Q9TYJ7: canonical residues {pos + 1}-{pos + len(frag)} "
          f"of {len(canon)} ({len(frag)} residues, 100% identity).\n")
else:
    print("U4PF58 is NOT an exact substring of Q9TYJ7.\n")

print("Q9TYJ7 sequence features (from UniProt):\n")
print("| Type | Description | Start | End | Present in U4PF58 |")
print("|---|---|---|---|---|")
for f in recs["Q9TYJ7"].get("features", []):
    s, e = f["location"]["start"]["value"], f["location"]["end"]["value"]
    inside = pos >= 0 and s >= pos + 1 and e <= pos + len(frag)
    overlap = pos >= 0 and not (e < pos + 1 or s > pos + len(frag))
    print(f"| {f['type']} | {f.get('description', '')} | {s} | {e} | {'full' if inside else ('partial' if overlap else 'no')} |")

print("\n## Global alignments of canonical Q9TYJ7 with characterised orthologs\n")
print("BLOSUM62, gap open -10, extend -0.5. Identity over aligned (ungapped) columns.\n")
print("| Pair | Aligned columns | Identical | % identity |")
print("|---|---|---|---|")
al = aligner()
for other in ("O60762", "P14020"):
    aln = al.align(canon, seq(recs[other]))[0]
    i, n = identity_over_aligned(aln)
    print(f"| Q9TYJ7 vs {other} | {n} | {i} | {100 * i / n:.1f} |")

n_bind = sum(1 for f in recs["O60762"].get("features", []) if f["type"] == "Binding site")
print(f"\nHuman DPM1 carries {n_bind} annotated binding-site residues in total.")
print("\n## Where the U4PF58 segment falls in human DPM1\n")
aln = al.align(canon, seq(recs["O60762"]))[0]
mapped = []
for (s1, e1), (s2, e2) in zip(*aln.aligned):
    for i, j in zip(range(s1, e1), range(s2, e2)):
        if pos <= i < pos + len(frag):
            mapped.append(j + 1)
if mapped:
    print(f"Canonical residues {pos + 1}-{pos + len(frag)} align to human DPM1 residues "
          f"{min(mapped)}-{max(mapped)} ({len(mapped)} aligned columns).\n")
print("Human DPM1 (O60762) features overlapping that interval:\n")
print("| Type | Description / ligand | Start | End | By similarity to |")
print("|---|---|---|---|---|")
for f in recs["O60762"].get("features", []):
    s, e = f["location"]["start"]["value"], f["location"]["end"]["value"]
    if mapped and not (e < min(mapped) or s > max(mapped)) and f["type"] not in ("Chain",):
        desc = f.get("description", "") or f.get("ligand", {}).get("name", "")
        src = ",".join(x.get("id", "") for x in f.get("evidences", []) if x.get("source") == "UniProtKB")
        print(f"| {f['type']} | {desc} | {s} | {e} | {src} |")
