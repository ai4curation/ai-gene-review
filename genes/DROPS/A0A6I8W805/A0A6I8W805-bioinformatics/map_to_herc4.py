# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython", "requests"]
# ///
"""Map LOC117183218 isoform X1 (A0A6I8W805) onto its closest relatives.

For each comparator (D. pseudoobscura Herc4, D. melanogaster Herc4, the
D. pseudoobscura RCC1-only paralog LOC6903915), fetch sequence, RCC1 repeat
and HECT domain features and PANTHER assignment from UniProt REST, local-align
X1 (BLOSUM62, gap -11/-1), and report identity and the region of the
comparator covered. Also reports AlphaFold DB mean pLDDT for X1.

Run: uv run map_to_herc4.py
"""
import requests
from Bio.Align import PairwiseAligner, substitution_matrices

API = "https://rest.uniprot.org/uniprotkb"
X1 = "A0A6I8W805"
COMPARATORS = {
    "A0A6I8W510": "D. pseudoobscura Herc4",
    "Q9W0H2": "D. melanogaster Herc4 (FBgn0035207)",
    "A0A6I8W7D9": "D. pseudoobscura LOC6903915",
}


def entry(acc: str) -> dict:
    r = requests.get(f"{API}/{acc}.json", timeout=120)
    r.raise_for_status()
    return r.json()


def features(e: dict, kind: str, note: str) -> list[tuple[int, int]]:
    out = []
    for f in e.get("features", []):
        if f["type"] == kind and note in f.get("description", ""):
            out.append((f["location"]["start"]["value"], f["location"]["end"]["value"]))
    return out


def panther(e: dict) -> str:
    return ";".join(x["id"] for x in e.get("uniProtKBCrossReferences", []) if x["database"] == "PANTHER")


al = PairwiseAligner(mode="local", substitution_matrix=substitution_matrices.load("BLOSUM62"),
                     open_gap_score=-11, extend_gap_score=-1)
x1e = entry(X1)
x1 = x1e["sequence"]["value"]
print(f"## {X1} (X1): {len(x1)} aa; PANTHER {panther(x1e)}")
print(f"RCC1 repeats: {features(x1e, 'Repeat', 'RCC1')}; HECT: {features(x1e, 'Domain', 'HECT')}")

print("\n## Alignments")
print("acc\tdescription\tlen\tPANTHER\tRCC1_repeats\tHECT\tidentity\tX1_range\tcomparator_range\tcomparator_repeats_covered")
for acc, desc in COMPARATORS.items():
    e = entry(acc)
    s = e["sequence"]["value"]
    reps = features(e, "Repeat", "RCC1")
    hect = features(e, "Domain", "HECT")
    aln = al.align(x1, s)[0]
    pairs = [(i, j) for i, j in zip(aln[0], aln[1]) if i != "-" and j != "-"]
    ident = sum(i == j for i, j in pairs)
    qs, qe = aln.coordinates[0][0] + 1, aln.coordinates[0][-1]
    ts, te = aln.coordinates[1][0] + 1, aln.coordinates[1][-1]
    covered = [r for r in reps if r[1] >= ts and r[0] <= te]
    print(f"{acc}\t{desc}\t{len(s)}\t{panther(e)}\t{len(reps)} {reps}\t{hect}\t"
          f"{ident}/{len(pairs)} ({100*ident/len(pairs):.0f}%)\t{qs}-{qe}\t{ts}-{te}\t{len(covered)}")

r = requests.get(f"https://alphafold.ebi.ac.uk/api/prediction/{X1}", timeout=120)
if r.ok and r.json():
    m = r.json()[0]
    print(f"\n## AlphaFold DB {X1}: globalMetricValue (mean pLDDT) = {m.get('globalMetricValue')}")
else:
    print(f"\n## AlphaFold DB {X1}: no model returned (HTTP {r.status_code})")
