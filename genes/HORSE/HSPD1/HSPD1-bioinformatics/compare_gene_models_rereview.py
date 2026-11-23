"""Compare the horse HSPD1 gene models with human HSPD1 (re-review, 2026-10-20).

Inputs (all local, fetched once and committed alongside this script):
  - ../HSPD1-uniprot.txt                 horse F6Z587 (benchmark accession, 541 aa)
  - A0A9L0S8L8-rereview.fasta            horse A0A9L0S8L8 (Ensembl canonical ENSECAP00000072491)
  - A0A9L0TMN1-rereview.fasta            horse A0A9L0TMN1 (ENSECAP00000088410)
  - ensembl_gene_rereview.json           Ensembl REST lookup of ENSECAG00000008968 (expand=1)
  - ../../../human/HSPD1/HSPD1-uniprot.txt  human P10809 (573 aa)

Domain boundaries are an input parameter, taken from the human mHsp60 structure
paper PMID:32317635 (mature numbering; the precursor carries a 26-residue
transit peptide, UniProt P10809 TRANSIT 1-26). The script maps every horse
model gap onto those domains; it does not assert any functional consequence.

Run from repo root:
  uv run python genes/HORSE/HSPD1/HSPD1-bioinformatics/compare_gene_models_rereview.py
"""

import json
from pathlib import Path

from Bio import Align, SeqIO, SwissProt

HERE = Path(__file__).resolve().parent
GENE_DIR = HERE.parent
HUMAN = GENE_DIR.parents[1] / "human" / "HSPD1" / "HSPD1-uniprot.txt"
TRANSIT_LEN = 26
# PMID:32317635: "equatorial ATP-binding domain (residues 1-137, 411-526), an
# intermediate hinge domain (residues 138-191, 375-411), and an apical domain
# (residues 192-374)" -- mature numbering.
DOMAINS = [
    ("equatorial", 1, 137),
    ("intermediate", 138, 191),
    ("apical", 192, 374),
    ("intermediate", 375, 410),
    ("equatorial", 411, 526),
]


def domain_of(mature_pos: int) -> str:
    """Return the structural domain for a mature-numbered residue.

    >>> domain_of(150)
    'intermediate'
    >>> domain_of(-3)
    'transit_peptide'
    """
    if mature_pos < 1:
        return "transit_peptide"
    for name, start, end in DOMAINS:
        if start <= mature_pos <= end:
            return name
    return "C-terminal tail"


def aligner() -> Align.PairwiseAligner:
    a = Align.PairwiseAligner()
    a.mode = "global"
    a.match_score = 2
    a.mismatch_score = -1
    a.open_gap_score = -10
    a.extend_gap_score = -0.5
    a.end_gap_score = 0
    return a


def compare(human_seq: str, model_seq: str) -> dict:
    aln = aligner().align(human_seq, model_seq)[0]
    h, m = str(aln[0]), str(aln[1])
    hp = mp = 0
    ident = paired = 0
    human_missing: list[int] = []
    model_insert: list[int] = []
    for u, v in zip(h, m):
        if u != "-":
            hp += 1
        if v != "-":
            mp += 1
        if u != "-" and v != "-":
            paired += 1
            ident += u == v
        elif u != "-":
            human_missing.append(hp)
        else:
            model_insert.append(mp)

    def runs(pos: list[int]) -> list[list[int]]:
        out: list[list[int]] = []
        for p in pos:
            if out and p == out[-1][1] + 1:
                out[-1][1] = p
            else:
                out.append([p, p])
        return out

    gaps = []
    for s, e in runs(human_missing):
        doms = sorted({domain_of(p - TRANSIT_LEN) for p in range(s, e + 1)})
        gaps.append(
            {
                "human_precursor_range": [s, e],
                "mature_range": [s - TRANSIT_LEN, e - TRANSIT_LEN],
                "length": e - s + 1,
                "human_residues": human_seq[s - 1 : e],
                "domains": doms,
            }
        )
    return {
        "model_length": len(model_seq),
        "paired": paired,
        "identical": ident,
        "identity": round(ident / paired, 4),
        "human_residues_missing_in_model": gaps,
        "model_residues_not_in_human": [
            {"model_range": [s, e], "residues": model_seq[s - 1 : e]}
            for s, e in runs(model_insert)
        ],
        "alignment": str(aln),
    }


def exon_table(gene: dict) -> dict:
    strand = gene["strand"]
    out = {}
    for t in gene["Transcript"]:
        exons = sorted(
            t["Exon"], key=lambda e: e["start"], reverse=(strand == -1)
        )
        out[t["id"]] = {
            "is_canonical": bool(t.get("is_canonical")),
            "protein": t.get("Translation", {}).get("id"),
            "protein_length": t.get("Translation", {}).get("length"),
            "exons_5_to_3": [[e["start"], e["end"], e["end"] - e["start"] + 1] for e in exons],
        }
    all_exons = {tuple(x[:2]) for v in out.values() for x in v["exons_5_to_3"]}
    for tid, v in out.items():
        present = {tuple(x[:2]) for x in v["exons_5_to_3"]}
        v["exons_absent_vs_union"] = sorted(
            [list(x) + [x[1] - x[0] + 1] for x in all_exons - present],
            reverse=(strand == -1),
        )
    return out


def main() -> None:
    with HUMAN.open() as f:
        human = SwissProt.read(f)
    with (GENE_DIR / "HSPD1-uniprot.txt").open() as f:
        f6 = SwissProt.read(f)
    models = {"F6Z587": f6.sequence}
    for acc in ["A0A9L0S8L8", "A0A9L0TMN1"]:
        rec = next(SeqIO.parse(HERE / f"{acc}-rereview.fasta", "fasta"))
        models[acc] = str(rec.seq)
    gene = json.loads((HERE / "ensembl_gene_rereview.json").read_text())

    results = {
        "human_accession": human.accessions[0],
        "human_length": len(human.sequence),
        "domain_boundaries_source": "PMID:32317635 (mature numbering)",
        "models": {acc: compare(human.sequence, seq) for acc, seq in models.items()},
        "ensembl_transcripts": exon_table(gene),
    }
    alns = {acc: r.pop("alignment") for acc, r in results["models"].items()}
    (HERE / "results-rereview.json").write_text(json.dumps(results, indent=2) + "\n")
    (HERE / "alignments-rereview.txt").write_text(
        "\n".join(f"### human P10809 (target) vs {k} (query)\n{v}" for k, v in alns.items())
    )

    lines = [
        "# HSPD1 horse gene models vs human P10809 (re-review 2026-10-20)",
        "",
        "Generated by `compare_gene_models_rereview.py`; full data in `results-rereview.json`,",
        "alignments in `alignments-rereview.txt`. Domain boundaries (mature numbering) from PMID:32317635.",
        "",
        "## Protein models",
        "",
        "| Model | Length | Identity to human (paired) | Human residues absent | Extra residues |",
        "|---|---|---|---|---|",
    ]
    for acc, r in results["models"].items():
        gaps = "; ".join(
            f"{g['human_precursor_range'][0]}-{g['human_precursor_range'][1]} "
            f"({g['length']} aa, mature {g['mature_range'][0]}-{g['mature_range'][1]}, "
            f"{'/'.join(g['domains'])})"
            for g in r["human_residues_missing_in_model"]
        ) or "none"
        extra = "; ".join(
            f"{x['model_range'][0]}-{x['model_range'][1]} {x['residues']}"
            for x in r["model_residues_not_in_human"]
        ) or "none"
        lines.append(
            f"| {acc} | {r['model_length']} | {r['identical']}/{r['paired']} ({r['identity']:.1%}) | {gaps} | {extra} |"
        )
    lines += ["", "## Ensembl transcripts of ENSECAG00000008968", ""]
    lines += ["| Transcript | Canonical | Protein | Length | Exons | Exons absent vs union of all transcripts (includes alternative UTR exons) |", "|---|---|---|---|---|---|"]
    for tid, v in results["ensembl_transcripts"].items():
        absent = "; ".join(f"{s}-{e} ({n} bp)" for s, e, n in v["exons_absent_vs_union"]) or "none"
        lines.append(
            f"| {tid} | {v['is_canonical']} | {v['protein']} | {v['protein_length']} | {len(v['exons_5_to_3'])} | {absent} |"
        )
    (HERE / "RESULTS-rereview.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
