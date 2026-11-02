# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython", "requests"]
# ///
"""Compare the Tango5 UniProt entries Q7KVQ7 and Q9W2S1, and each against human VMP1 (Q96GC9).

Fetches sequences, PANTHER family/subfamily (InterPro API) and transmembrane/domain
features (UniProt REST), then reports containment and global pairwise identity.
Run: uv run compare_isoforms.py
"""
import json

import requests
from Bio import Align
from Bio.Align import substitution_matrices

ACCS = ["Q7KVQ7", "Q9W2S1", "Q96GC9"]


def fasta(acc: str) -> str:
    txt = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60).text
    return "".join(line.strip() for line in txt.splitlines() if not line.startswith(">"))


def panther(acc: str) -> list[str]:
    url = f"https://www.ebi.ac.uk/interpro/api/entry/panther/protein/uniprot/{acc}?page_size=20"
    data = requests.get(url, timeout=60).json()
    out = []
    for r in data["results"]:
        for p in r.get("proteins", []):
            for loc in p.get("entry_protein_locations", []) or []:
                sf = loc.get("subfamily") or {}
                out.append(f"{r['metadata']['accession']} {sf.get('accession', '')} {sf.get('name', '')}")
    return sorted(set(out))


def features(acc: str) -> list[str]:
    data = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.json", timeout=60).json()
    return [
        f"{f['type']} {f['location']['start']['value']}-{f['location']['end']['value']} {f.get('description', '')}"
        for f in data.get("features", [])
        if f["type"] in ("Transmembrane", "Domain")
    ]


def identity(a: str, b: str) -> tuple[float, int]:
    aligner = Align.PairwiseAligner(mode="global")
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    aln = aligner.align(a, b)[0]
    ident = aligned = 0
    for (s1, e1), (s2, e2) in zip(*aln.aligned):
        for i, j in zip(range(s1, e1), range(s2, e2)):
            aligned += 1
            ident += a[i] == b[j]
    return ident / aligned, aligned


seqs = {a: fasta(a) for a in ACCS}
report = {"lengths": {a: len(s) for a, s in seqs.items()}}
short, long_ = seqs["Q7KVQ7"], seqs["Q9W2S1"]
pos = long_.find(short)
report["Q7KVQ7_exact_substring_of_Q9W2S1_start"] = pos + 1 if pos >= 0 else None
report["Q7KVQ7_is_C_terminal_suffix_of_Q9W2S1"] = long_.endswith(short)
report["panther"] = {a: panther(a) for a in ACCS}
report["features"] = {a: features(a) for a in ACCS}
for a in ("Q7KVQ7", "Q9W2S1"):
    frac, n = identity(seqs[a], seqs["Q96GC9"])
    report[f"identity_{a}_vs_Q96GC9"] = {"fraction_identical_over_aligned": round(frac, 3), "aligned_columns": n}
print(json.dumps(report, indent=2))
