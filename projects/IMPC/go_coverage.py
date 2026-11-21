"""How do IMPC-phenotyped genes stand in GO, and how does GO encode knockout evidence?

Two questions:

1. For mouse genes IMPC has phenotyped, how many have an experimentally
   supported GO molecular function, and does IMPC reach a cellular level for
   the genes that lack one (the "dark" genes IMPC set out to illuminate)?
2. How does MGI's own knockout-derived GO curation (IMP, IGI) qualify its
   annotations: does it claim the gene product participates in the process
   (``involved_in``) or only that it acts upstream of it
   (``acts_upstream_of_or_within``)?

3. For the "dark" genes (no experimental mouse MF or BP), does the human
   ortholog have an experimental MF or BP in the human GO annotation file?
   Mouse genes are mapped to human through IMPC's own ``human_gene_symbol``
   field, matched to GAF column 3 (symbol). A gene counts as covered if any of
   its mapped human symbols carries an experimental annotation.

Inputs (git-ignored): ``.cache/impc/{genotype_phenotype,genes}.tsv``,
``.cache/impc/mgi.gaf.gz`` (http://current.geneontology.org/annotations/mgi.gaf.gz),
``.cache/impc/goa_human.gaf.gz`` (http://current.geneontology.org/annotations/goa_human.gaf.gz),
and ``projects/IMPC/results/mp_term_levels.tsv`` from ``mp_resolution.py``.

Output: ``projects/IMPC/results/go_coverage.yaml`` and ``GO_COVERAGE.md``.

    uv run python projects/IMPC/go_coverage.py
"""

from __future__ import annotations

import gzip
from collections import Counter, defaultdict
from pathlib import Path

import pandas as pd
import yaml

CACHE = Path(".cache/impc")
HERE = Path(__file__).parent
RESULTS = HERE / "results"

EXPERIMENTAL = {"EXP", "IDA", "IPI", "IMP", "IGI", "IEP", "HTP", "HDA", "HMP", "HGI", "HEP"}
PROTEIN_BINDING = "GO:0005515"
LEVELS = [
    "CELLULAR",
    "CIRCULATING_MOLECULE",
    "ORGAN_PROCESS",
    "ANATOMY",
    "BEHAVIOUR",
    "NO_LOGICAL_DEFINITION",
]


def gaf_date(path: Path) -> str:
    with gzip.open(path, "rt") as fh:
        for line in fh:
            if not line.startswith("!"):
                break
            if line.lower().startswith("!date-generated:") or line.lower().startswith("!date:"):
                return line.split(":", 1)[1].strip()
    return "unknown"


def experimental_sets(gaf: pd.DataFrame, key: str) -> tuple[set[str], set[str]]:
    """Genes (by ``key`` column) with a non-NOT experimental MF (bare protein binding excluded) / BP."""
    exp = gaf[gaf.evidence.isin(EXPERIMENTAL) & ~gaf.qualifier.str.startswith("NOT")]
    mf = set(exp[(exp.aspect == "F") & (exp.go != PROTEIN_BINDING)][key])
    bp = set(exp[exp.aspect == "P"][key])
    return mf, bp


def read_gaf(path: Path) -> pd.DataFrame:
    rows = []
    with gzip.open(path, "rt") as fh:
        for line in fh:
            if line.startswith("!"):
                continue
            f = line.rstrip("\n").split("\t")
            rows.append(
                {
                    "gene": f[1],
                    "symbol": f[2],
                    "qualifier": f[3],
                    "go": f[4],
                    "ref": f[5],
                    "evidence": f[6],
                    "aspect": f[8],
                }
            )
    return pd.DataFrame(rows)


def main() -> None:
    gaf = read_gaf(CACHE / "mgi.gaf.gz")
    gp = pd.read_csv(CACHE / "genotype_phenotype.tsv", sep="\t")
    genes = pd.read_csv(CACHE / "genes.tsv", sep="\t")
    levels = pd.read_csv(RESULTS / "mp_term_levels.tsv", sep="\t")
    gp["level"] = gp.mp_term_id.map(dict(zip(levels.mp_term_id, levels.level)))

    exp = gaf[gaf.evidence.isin(EXPERIMENTAL)]
    not_rows = exp.qualifier.str.startswith("NOT")
    exp = exp[~not_rows]
    exp_mf = exp[(exp.aspect == "F") & (exp.go != PROTEIN_BINDING)]
    exp_bp = exp[exp.aspect == "P"]
    has_mf = set(exp_mf.gene)
    has_bp = set(exp_bp.gene)
    has_bp_participates = set(exp_bp[exp_bp.qualifier == "involved_in"].gene)

    phenotyped = set(genes.loc[genes.phenotyping_data_available == True, "mgi_accession_id"])  # noqa: E712
    with_call = set(gp.marker_accession_id)

    def finest(acc_levels: pd.Series) -> str:
        s = set(acc_levels.dropna())
        for lv in LEVELS:
            if lv in s:
                return lv
        return "NO_LOGICAL_DEFINITION"

    gene_level = gp.groupby("marker_accession_id")["level"].agg(finest)
    dark = with_call - has_mf
    dark_bp = with_call - has_mf - has_bp

    # Human coverage of the dark genes, through IMPC's human_gene_symbol mapping.
    human_gaf_path = CACHE / "goa_human.gaf.gz"
    human = None
    if human_gaf_path.exists():
        hgaf = read_gaf(human_gaf_path)
        h_mf, h_bp = experimental_sets(hgaf, "symbol")
        to_human = {
            acc: [x for x in str(sym).split("|") if x and x != "nan"]
            for acc, sym in zip(genes.mgi_accession_id, genes.human_gene_symbol)
        }

        def covered(acc: str, sets: list[set[str]]) -> bool:
            return any(h in s for h in to_human.get(acc, []) for s in sets)

        no_ortholog = {g for g in dark_bp if not to_human.get(g)}
        mapped = dark_bp - no_ortholog
        hum_mf = {g for g in mapped if covered(g, [h_mf])}
        hum_bp = {g for g in mapped if covered(g, [h_bp])}
        hum_any = hum_mf | hum_bp
        still_dark = dark_bp - hum_any
        human = {
            "goa_human_date": gaf_date(human_gaf_path),
            "goa_human_rows": int(len(hgaf)),
            "dark_genes_mouse": len(dark_bp),
            "dark_genes_without_human_symbol": len(no_ortholog),
            "dark_genes_with_human_symbol": len(mapped),
            "dark_genes_with_experimental_human_mf": len(hum_mf),
            "dark_genes_with_experimental_human_bp": len(hum_bp),
            "dark_genes_with_experimental_human_mf_or_bp": len(hum_any),
            "dark_in_both_species": len(still_dark),
            "finest_impc_level_dark_in_both_species": {
                k: int(v) for k, v in gene_level[gene_level.index.isin(still_dark)].value_counts().items()
            },
        }
        # Same question for the wider "no experimental mouse MF" set.
        mapped_mf = {g for g in dark if to_human.get(g)}
        human["no_mouse_mf_genes"] = len(dark)
        human["no_mouse_mf_with_experimental_human_mf"] = len({g for g in mapped_mf if covered(g, [h_mf])})
        human["no_mf_in_either_species"] = len(dark) - human["no_mouse_mf_with_experimental_human_mf"]

    # How MGI qualifies knockout-derived (IMP) biological-process annotations.
    imp_bp = gaf[(gaf.evidence == "IMP") & (gaf.aspect == "P")]
    ida_bp = gaf[(gaf.evidence == "IDA") & (gaf.aspect == "P")]

    out = {
        "mgi_gaf_rows": int(len(gaf)),
        "impc_genes_phenotyped": len(phenotyped),
        "impc_genes_with_significant_call": len(with_call),
        "phenotyped_without_significant_call": len(phenotyped - with_call),
        "genes_with_call_and_experimental_mf": len(with_call & has_mf),
        "genes_with_call_no_experimental_mf": len(dark),
        "genes_with_call_no_experimental_mf_or_bp": len(dark_bp),
        "finest_impc_level_all_genes_with_call": {
            k: int(v) for k, v in gene_level.value_counts().items()
        },
        "finest_impc_level_genes_without_experimental_mf": {
            k: int(v) for k, v in gene_level[gene_level.index.isin(dark)].value_counts().items()
        },
        "finest_impc_level_genes_without_experimental_mf_or_bp": {
            k: int(v) for k, v in gene_level[gene_level.index.isin(dark_bp)].value_counts().items()
        },
        "mgi_imp_bp_qualifiers": {k: int(v) for k, v in imp_bp.qualifier.value_counts().items()},
        "mgi_ida_bp_qualifiers": {k: int(v) for k, v in ida_bp.qualifier.value_counts().items()},
        "mgi_gaf_references_naming_impc": int(gaf.ref.str.contains("IMPC|mousephenotype", case=False).sum()),
    }
    if human:
        out["human_coverage_of_dark_genes"] = human
    RESULTS.mkdir(exist_ok=True)
    (RESULTS / "go_coverage.yaml").write_text(yaml.safe_dump(out, sort_keys=False))

    def pct(a: int, b: int) -> str:
        return f"{a:,} ({100 * a / b:.0f}%)" if b else str(a)

    n = out["impc_genes_with_significant_call"]
    lines = [
        "# IMPC genes and GO (generated)",
        "",
        "Generated by `go_coverage.py`; do not edit by hand. Experimental evidence ="
        f" {', '.join(sorted(EXPERIMENTAL))}; bare protein binding ({PROTEIN_BINDING}) does not count as a molecular function.",
        "",
        f"- Genes IMPC reports as phenotyped: {out['impc_genes_phenotyped']:,}",
        f"- With at least one significant call: {n:,}",
        f"- ...of which have an experimental mouse MF annotation: {pct(out['genes_with_call_and_experimental_mf'], n)}",
        f"- ...with no experimental mouse MF: {pct(out['genes_with_call_no_experimental_mf'], n)}",
        f"- ...with no experimental mouse MF or BP: {pct(out['genes_with_call_no_experimental_mf_or_bp'], n)}",
        f"- MGI GO annotations whose reference names IMPC: {out['mgi_gaf_references_naming_impc']}",
        "",
        "## Finest level IMPC reaches for a gene",
        "",
        "| Finest level | All genes with a call | No experimental MF | No experimental MF or BP |",
        "|---|---:|---:|---:|",
    ]
    if human:
        d = human["dark_genes_mouse"]
        lines += [
            "",
            "## Human coverage of the dark genes",
            "",
            f"Dark genes = genes with a significant IMPC call and no experimental mouse MF or BP ({d:,})."
            f" Mapped to human through IMPC's `human_gene_symbol` field and matched to column 3 of"
            f" goa_human.gaf ({human['goa_human_date']}); same experimental code set, bare protein binding excluded.",
            "",
            f"- Dark genes with no human symbol in IMPC's gene table: {pct(human['dark_genes_without_human_symbol'], d)}",
            f"- With an experimental human MF: {pct(human['dark_genes_with_experimental_human_mf'], d)}",
            f"- With an experimental human BP: {pct(human['dark_genes_with_experimental_human_bp'], d)}",
            f"- With an experimental human MF or BP: {pct(human['dark_genes_with_experimental_human_mf_or_bp'], d)}",
            f"- **Dark in both species** (no experimental MF or BP in mouse or human): {pct(human['dark_in_both_species'], n)} of genes with a call",
            f"- Genes with a call and no experimental MF in either species: "
            f"{pct(human['no_mf_in_either_species'], n)} (mouse-only figure {human['no_mouse_mf_genes']:,};"
            f" {human['no_mouse_mf_with_experimental_human_mf']:,} recovered by a human MF)",
            "",
            "| Finest IMPC level, genes dark in both species | Genes |",
            "|---|---:|",
        ]
        for lv in LEVELS:
            lines.append(f"| {lv} | {human['finest_impc_level_dark_in_both_species'].get(lv, 0):,} |")
        lines.append("")
    a = out["finest_impc_level_all_genes_with_call"]
    b = out["finest_impc_level_genes_without_experimental_mf"]
    c = out["finest_impc_level_genes_without_experimental_mf_or_bp"]
    for lv in LEVELS:
        lines.append(f"| {lv} | {a.get(lv, 0):,} | {b.get(lv, 0):,} | {c.get(lv, 0):,} |")
    lines += [
        "",
        "## How MGI qualifies GO biological-process annotations",
        "",
        "| Qualifier | IMP (mutant phenotype) | IDA (direct assay) |",
        "|---|---:|---:|",
    ]
    quals = sorted(set(out["mgi_imp_bp_qualifiers"]) | set(out["mgi_ida_bp_qualifiers"]))
    ti, td = len(imp_bp), len(ida_bp)
    for q in quals:
        lines.append(
            f"| {q} | {pct(out['mgi_imp_bp_qualifiers'].get(q, 0), ti)} | "
            f"{pct(out['mgi_ida_bp_qualifiers'].get(q, 0), td)} |"
        )
    lines.append("")
    (RESULTS / "GO_COVERAGE.md").write_text("\n".join(lines))
    print("\n".join(lines))


if __name__ == "__main__":
    main()
