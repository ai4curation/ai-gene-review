"""List candidate gene annotations implied by modules.

A module that places a protein in a process is making a claim about that
protein. Where neither GOA nor the protein's own gene review carries the
process, the claim is a lead for a ``NEW`` annotation in the review. This
report lists those leads, one row per module, annoton, protein and process.

A lead is not an annotation and a module is not evidence for one: the module's
placement is this project's own claim, so each row still needs a publication
and has to pass the participation test in the curation guidelines (the gene
product must do some of the work of the process; being required for it, or
being a component shared by many pathways, is not enough). The report is sorted
so the rows most likely to survive that test come first:

1. the annoton names the process itself (``process_source: annoton``) instead
   of inheriting the concept of an enclosing node;
2. the annoton's function is a receptor or receptor-ligand activity, the
   participants that decide which pathway a module is;
3. GOA has experimental annotation of the protein under a sibling process.

Only proteins with a local gene folder are listed. Run it with
``just module-annotation-leads``.
"""

from __future__ import annotations

import csv
from pathlib import Path
from typing import Any, Callable

import typer
import yaml
from yaml import CSafeLoader

from ai_gene_review.module_process_conformance import (
    GoProcessGraph,
    module_process_conformance,
    oak_go_process_graph,
)
from ai_gene_review.module_qc import index_gene_reviews

LabelLookup = Callable[[str], str | None]

LEAD_STATUSES = frozenset({"PROCESS_NOT_ANNOTATED", "SIBLING_PROCESS_ONLY"})
LEAD_COLUMNS = (
    "module",
    "annoton",
    "gene",
    "gene_label",
    "gene_review",
    "process_id",
    "process_label",
    "process_source",
    "receptor_or_ligand",
    "goa_sibling_processes",
    "module_evidence",
)


def _rank(row: dict[str, Any]) -> tuple[Any, ...]:
    """Sort key: most direct module claim first, then stable by module and gene."""
    return (
        row["process_source"] != "annoton",
        row["receptor_or_ligand"] != "yes",
        not row["goa_sibling_processes"],
        row["module"],
        row["annoton"],
        row["gene"],
        row["process_id"],
    )


def collect_leads(
    modules_dir: Path,
    *,
    gene_index: dict[str, Path] | None = None,
    genes_dir: Path = Path("genes"),
    graph: GoProcessGraph | None = None,
    label: LabelLookup | None = None,
) -> list[dict[str, Any]]:
    """Collect every module-implied process that a gene's review does not carry.

    ``graph`` and ``label`` may be injected for tests; otherwise the local GO
    snapshot supplies both. A module whose check could not run raises, so a
    missing ontology is never reported as an empty lead list.
    """
    if gene_index is None:
        gene_index = index_gene_reviews(genes_dir)
    if graph is None:
        oak = oak_go_process_graph()
        graph, label = oak.graph, label or oak.label
    lookup: LabelLookup = label or (lambda curie: None)

    leads: list[dict[str, Any]] = []
    for path in sorted(modules_dir.glob("*.yaml")):
        data = yaml.load(path.read_text(encoding="utf-8"), Loader=CSafeLoader)
        if not isinstance(data, dict) or not isinstance(data.get("module"), dict):
            continue
        result = module_process_conformance(data, gene_index=gene_index, graph=graph)
        if result["failure"]:
            raise RuntimeError(f"{path}: {result['failure']}")
        for row in result["rows"]:
            if row["status"] not in LEAD_STATUSES:
                continue
            for process in row["expected_process_ids"]:
                leads.append(
                    {
                        "module": path.stem,
                        "annoton": row["annoton_id"],
                        "gene": row["participant_id"],
                        "gene_label": row["participant_label"] or "",
                        "gene_review": row["review_path"] or "",
                        "process_id": process,
                        "process_label": lookup(process) or "",
                        "process_source": row["process_source"],
                        "receptor_or_ligand": "yes"
                        if row["pathway_defining"]
                        else "no",
                        "goa_sibling_processes": "|".join(row["sibling_process_ids"]),
                        "module_evidence": "|".join(row["evidence_ids"]),
                    }
                )
    return sorted(leads, key=_rank)


def write_leads(leads: list[dict[str, Any]], output: Path) -> None:
    """Write leads as a tab-separated file with a header row."""
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle, fieldnames=LEAD_COLUMNS, delimiter="\t", lineterminator="\n"
        )
        writer.writeheader()
        writer.writerows(leads)


def main(
    modules_dir: Path = typer.Option(
        Path("modules"), help="Directory of module YAML files."
    ),
    genes_dir: Path = typer.Option(Path("genes"), help="Directory of gene reviews."),
    output: Path = typer.Option(
        Path("reports/module-annotation-leads.tsv"), help="Where to write the report."
    ),
) -> None:
    """Write the module-implied annotation leads report and print a summary."""
    leads = collect_leads(modules_dir, genes_dir=genes_dir)
    write_leads(leads, output)
    stated = sum(row["process_source"] == "annoton" for row in leads)
    receptors = sum(row["receptor_or_ligand"] == "yes" for row in leads)
    typer.echo(
        f"{len(leads)} leads in {len({row['module'] for row in leads})} modules "
        f"({stated} with the process stated on the annoton, {receptors} on a receptor "
        f"or ligand) -> {output}"
    )


if __name__ == "__main__":
    typer.run(main)
