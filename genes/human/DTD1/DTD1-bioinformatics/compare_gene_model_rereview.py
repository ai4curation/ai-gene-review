# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Re-review analysis: relate A0A2R8YCT7 to the canonical DTD1 product Q8TEA8.

Fetches both sequences from UniProt and both transcript models from Ensembl
REST, then reports: the shared N-terminal prefix, the point of divergence, the
divergent C-terminal tail, which canonical features lie beyond the divergence,
and the exon structures of the two transcripts (with biotype).

Run: uv run --script compare_gene_model_rereview.py > RESULTS-rereview.md
"""

import json
import urllib.request

TARGET = "A0A2R8YCT7"
CANONICAL = "Q8TEA8"
TARGET_TX = "ENST00000647441"
CANONICAL_TX = "ENST00000377452"

# Canonical features taken from the Q8TEA8 UniProt record (positions on Q8TEA8).
CANONICAL_FEATURES = [
    ("Mg(2+) binding (ECO:0000269 PubMed:17264083)", 4, 4),
    ("Mg(2+) binding (ECO:0000269 PubMed:17264083)", 6, 6),
    ("Mg(2+) binding (ECO:0000269 PubMed:17264083)", 28, 28),
    ("Beta strand 131-146 (PDB:2OKV)", 131, 146),
    ("Gly-cisPro motif (ECO:0000250 Q8IIS0)", 139, 140),
    ("Disordered C-terminal region (MobiDB-lite)", 142, 209),
    ("Phosphoserine 197", 197, 197),
]


def fetch(url: str) -> str:
    with urllib.request.urlopen(url) as fh:
        return fh.read().decode()


def uniprot_seq(acc: str) -> str:
    fasta = fetch(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta")
    return "".join(line.strip() for line in fasta.splitlines() if not line.startswith(">"))


def ensembl_tx(tx: str) -> dict:
    url = f"https://rest.ensembl.org/lookup/id/{tx}?content-type=application/json;expand=1"
    return json.loads(fetch(url))


def main() -> None:
    t = uniprot_seq(TARGET)
    c = uniprot_seq(CANONICAL)
    prefix = 0
    while prefix < min(len(t), len(c)) and t[prefix] == c[prefix]:
        prefix += 1
    print("# DTD1 re-review: gene-model analysis of A0A2R8YCT7 vs Q8TEA8\n")
    print(f"- {TARGET} length: {len(t)} aa")
    print(f"- {CANONICAL} length: {len(c)} aa")
    print(f"- Identical N-terminal prefix: residues 1-{prefix}")
    print(f"- {TARGET} tail after divergence: {t[prefix:]} (residues {prefix + 1}-{len(t)})")
    print(f"- {CANONICAL} sequence after divergence: {c[prefix:]} (residues {prefix + 1}-{len(c)})")
    print(f"- Canonical residues absent from {TARGET}: {len(c) - prefix} of {len(c)}\n")

    print("## Canonical features vs divergence point\n")
    print("| Feature | Q8TEA8 interval | Retained in A0A2R8YCT7 |")
    print("|---|---|---|")
    for name, s, e in CANONICAL_FEATURES:
        if e <= prefix:
            status = "yes (identical prefix)"
        elif s > prefix:
            status = "no (after divergence)"
        else:
            status = f"partial (only {s}-{prefix})"
        print(f"| {name} | {s}-{e} | {status} |")

    print("\n## Transcript models (Ensembl GRCh38)\n")
    for tx in (CANONICAL_TX, TARGET_TX):
        d = ensembl_tx(tx)
        tl = d.get("Translation", {})
        print(f"### {tx} ({d['biotype']}, Ensembl canonical={bool(d.get('is_canonical'))})\n")
        print(f"Translation {tl.get('id')} length {tl.get('length')}, CDS end {tl.get('end')}\n")
        print("| Exon | Start | End | Length (nt) |")
        print("|---|---|---|---|")
        for ex in d["Exon"]:
            print(f"| {ex['id']} | {ex['start']} | {ex['end']} | {ex['end'] - ex['start'] + 1} |")
        print()

    can_exons = {(e["start"], e["end"]) for e in ensembl_tx(CANONICAL_TX)["Exon"]}
    can_ends = {e for _, e in can_exons}
    extra = [
        e for e in ensembl_tx(TARGET_TX)["Exon"]
        if not any(s <= e["start"] <= en or s <= e["end"] <= en for s, en in can_exons)
    ]
    print("## Exons of the target model that do not overlap any canonical exon\n")
    for ex in extra:
        ln = ex["end"] - ex["start"] + 1
        print(f"- {ex['id']} {ex['start']}-{ex['end']} ({ln} nt; length mod 3 = {ln % 3})")
    print(f"\n(Canonical exon end coordinates checked: {len(can_ends)})")


if __name__ == "__main__":
    main()
