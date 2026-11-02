# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython>=1.81", "requests"]
# ///
"""Independent re-review mapping of J3KS48 onto canonical NARF Q9UHQ1.

Fetches both sequences and Pfam domain coordinates live from UniProt and
InterPro (no frozen prediction inputs), aligns them globally, and reports
which reference residues, cysteines and Pfam domain residues the selected
product retains. Run: uv run --script compare_sequences_rereview.py
"""

import json

import requests
from Bio import Align
from Bio.Align import substitution_matrices

SELECTED = "J3KS48"
REFERENCE = "Q9UHQ1"


def fetch_seq(acc: str) -> str:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    return "".join(r.text.splitlines()[1:])


def fetch_pfam(acc: str) -> list[tuple[str, str, int, int]]:
    r = requests.get(
        f"https://www.ebi.ac.uk/interpro/api/entry/pfam/protein/uniprot/{acc}", timeout=60
    )
    r.raise_for_status()
    out = []
    for res in r.json()["results"]:
        for p in res["proteins"]:
            for loc in p["entry_protein_locations"]:
                for f in loc["fragments"]:
                    out.append(
                        (res["metadata"]["accession"], res["metadata"]["name"], f["start"], f["end"])
                    )
    return out


def main() -> None:
    sel, ref = fetch_seq(SELECTED), fetch_seq(REFERENCE)
    aligner = Align.PairwiseAligner()
    aligner.mode = "global"
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    aln = aligner.align(sel, ref)[0]
    pairs = [((int(a[0]), int(a[1])), (int(b[0]), int(b[1]))) for a, b in zip(*aln.aligned)]
    # map reference position (1-based) -> selected position for identical residues
    ref_to_sel: dict[int, int] = {}
    for (s0, s1), (r0, r1) in pairs:
        for i in range(s1 - s0):
            if sel[s0 + i] == ref[r0 + i]:
                ref_to_sel[r0 + i + 1] = s0 + i + 1
    blocks = []
    for (s0, s1), (r0, r1) in pairs:
        ident = sum(sel[s0 + i] == ref[r0 + i] for i in range(s1 - s0))
        blocks.append({"ref": [r0 + 1, r1], "sel": [s0 + 1, s1], "identical": ident})
    ref_cys = [i + 1 for i, c in enumerate(ref) if c == "C"]
    cys_retained = [c for c in ref_cys if c in ref_to_sel]
    domains = []
    for accn, name, start, end in fetch_pfam(REFERENCE):
        span = range(start, end + 1)
        kept = sum(1 for p in span if p in ref_to_sel)
        dom_cys = [c for c in ref_cys if start <= c <= end]
        domains.append(
            {
                "pfam": accn,
                "name": name,
                "ref_interval": [start, end],
                "length": len(span),
                "identical_residues_retained": kept,
                "cysteines": dom_cys,
                "cysteines_retained": [c for c in dom_cys if c in ref_to_sel],
            }
        )
    result = {
        "selected": SELECTED,
        "selected_length": len(sel),
        "reference": REFERENCE,
        "reference_length": len(ref),
        "identical_residues_total": len(ref_to_sel),
        "aligned_blocks": blocks,
        "reference_cysteines": ref_cys,
        "reference_cysteines_retained": cys_retained,
        "reference_pfam_domains": domains,
        "selected_pfam_domains": [
            {"pfam": a, "name": n, "interval": [s, e]} for a, n, s, e in fetch_pfam(SELECTED)
        ],
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
