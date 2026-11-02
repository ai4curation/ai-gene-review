"""Re-review: compare the benchmark horse IRAK3 model (A0A3Q2HDT6) with the
Ensembl-canonical horse product (F6QZW8), the other horse model (A0A5F5PKF5),
human IRAK3 (Q9Y616) and mouse Irak3 (Q8K4B2).

Fetches sequences from UniProt REST and transcript structure from Ensembl REST,
computes global pairwise alignments, maps the human UniProt Death domain
(41-106), Protein kinase domain (165-452), Ser110 (IRAK1 site, PIN1 motif),
and the CGS291-293 / DFA311-313 pseudokinase motifs onto each horse model.

Run: uv run --with biopython --with requests python compare_gene_models_rereview.py
Writes results-rereview.json next to this script.
"""
import json
from pathlib import Path

import requests
from Bio import Align
from Bio.Align import substitution_matrices

ACCS = {
    "horse_benchmark": "A0A3Q2HDT6",
    "horse_canonical": "F6QZW8",
    "horse_other": "A0A5F5PKF5",
    "human": "Q9Y616",
    "mouse": "Q8K4B2",
}
HUMAN_FEATURES = {
    "death_domain": (41, 106),
    "kinase_domain": (165, 452),
    "Ser110": (110, 110),
    "CGS_motif": (291, 293),
    "DFA_motif": (311, 313),
    "N_terminus_1_40": (1, 40),
}


def fetch_seq(acc: str) -> str:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    return "".join(r.text.splitlines()[1:])


def aligner() -> Align.PairwiseAligner:
    a = Align.PairwiseAligner()
    a.mode = "global"
    a.substitution_matrix = substitution_matrices.load("BLOSUM62")
    a.open_gap_score = -10
    a.extend_gap_score = -0.5
    a.end_gap_score = 0
    return a


def pos_map(aln) -> dict[int, int]:
    """Map 1-based positions in target (seq A) to query (seq B)."""
    m = {}
    for (a0, a1), (b0, b1) in zip(*aln.aligned):
        for k in range(a1 - a0):
            m[int(a0) + k + 1] = int(b0) + k + 1
    return m


def stats(aln, a: str, b: str) -> dict:
    ident = paired = 0
    for (a0, a1), (b0, b1) in zip(*aln.aligned):
        for k in range(a1 - a0):
            paired += 1
            ident += int(a[a0 + k] == b[b0 + k])
    return {
        "paired": paired,
        "identical": ident,
        "identity_pct": round(100 * ident / paired, 1),
        "coverage_of_first_pct": round(100 * paired / len(a), 1),
        "coverage_of_second_pct": round(100 * paired / len(b), 1),
    }


def map_features(human: str, other: str, aln) -> dict:
    m = pos_map(aln)
    out = {}
    for name, (s, e) in HUMAN_FEATURES.items():
        mapped = [m.get(i) for i in range(s, e + 1)]
        present = [x for x in mapped if x is not None]
        out[name] = {
            "human_range": [s, e],
            "human_residues": human[s - 1 : e] if e - s < 10 else None,
            "mapped_count": len(present),
            "length": e - s + 1,
            "mapped_range": [present[0], present[-1]] if present else None,
            "other_residues": "".join(other[x - 1] for x in present) if e - s < 10 else None,
        }
    return out


def main() -> None:
    seqs = {k: fetch_seq(v) for k, v in ACCS.items()}
    al = aligner()
    res = {"accessions": ACCS, "lengths": {k: len(v) for k, v in seqs.items()}}
    # benchmark vs canonical horse product
    bc = al.align(seqs["horse_canonical"], seqs["horse_benchmark"])[0]
    m = pos_map(bc)
    first = min(m)  # first canonical residue paired
    res["benchmark_vs_canonical"] = stats(bc, seqs["horse_canonical"], seqs["horse_benchmark"])
    res["benchmark_vs_canonical"]["canonical_residues_unpaired_N_term"] = sorted(
        i for i in range(1, len(seqs["horse_canonical"]) + 1) if i not in m and i < 100
    )
    res["benchmark_vs_canonical"]["benchmark_N_term_8"] = seqs["horse_benchmark"][:8]
    res["benchmark_vs_canonical"]["canonical_45_60"] = seqs["horse_canonical"][44:60]
    # identity of benchmark residues 4..end vs canonical (suffix identity)
    suffix = seqs["horse_benchmark"][3:]
    res["benchmark_suffix_from_4_is_exact_substring_of_canonical"] = suffix in seqs["horse_canonical"]
    if suffix in seqs["horse_canonical"]:
        res["benchmark_suffix_start_in_canonical"] = seqs["horse_canonical"].index(suffix) + 1
    res["first_canonical_residue_paired"] = first
    # each horse model and mouse vs human, with feature mapping
    for k in ("horse_benchmark", "horse_canonical", "horse_other", "mouse"):
        a = al.align(seqs["human"], seqs[k])[0]
        res[f"human_vs_{k}"] = stats(a, seqs["human"], seqs[k])
        res[f"human_vs_{k}"]["features"] = map_features(seqs["human"], seqs[k], a)
    # Ensembl transcript structure
    r = requests.get(
        "https://rest.ensembl.org/lookup/id/ENSECAG00000026958?expand=1",
        headers={"Content-Type": "application/json"},
        timeout=60,
    )
    r.raise_for_status()
    g = r.json()
    res["ensembl_gene"] = {
        "id": g["id"],
        "display_name": g.get("display_name"),
        "canonical_transcript": g.get("canonical_transcript"),
        "transcripts": [
            {
                "id": t["id"],
                "is_canonical": t.get("is_canonical"),
                "protein": t.get("Translation", {}).get("id"),
                "protein_length": t.get("Translation", {}).get("length"),
                "n_exons": len(t["Exon"]),
                "first_exon": [t["Exon"][0]["start"], t["Exon"][0]["end"]],
                "strand": t["strand"],
            }
            for t in g["Transcript"]
        ],
    }
    out = Path(__file__).with_name("results-rereview.json")
    out.write_text(json.dumps(res, indent=2))
    print(json.dumps(res, indent=2))


if __name__ == "__main__":
    main()
