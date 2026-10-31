"""Report the PAINT losses (IRD/IKR) on a gene's lineage, for use while reviewing it.

An IRD produces no leaf annotation: it only stops an ancestral IBD from descending, so a
reviewer reading the gene's GOA file never sees it. A cached GOA file can even still carry
the IBA that a newer IRD has withdrawn. This module finds, for one gene review, every
PAINT loss whose node lies on the path from the PANTHER family root to the gene's leaf,
and lists the review's own rows on each blocked term, so the review can agree with the
loss or argue against it explicitly.

Data: PAINT ``IBD.gaf`` (cached under ``.cache/paint/``) and the family tree from the
PANTHER API (cached under ``.cache/panther_trees/``). Terms are matched exactly; a
review row on a descendant of the blocked term is not reported.

Usage:
    uv run python -m ai_gene_review.validation.gene_paint_losses human SLC52A1
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable

import yaml

from ai_gene_review.etl.panther_paint import (
    IBD_GAF_URL,
    IBDRecord,
    download_cached,
    open_text,
    parse_ibd_gaf,
    parse_ptn_nodes,
)
from ai_gene_review.etl.panther_trees import ancestors_of, leaf_nodes_for, leaves_below, load_family


@dataclass
class PaintLoss:
    """One PAINT loss on the gene's lineage, with the review rows it bears on."""

    node: str
    go_id: str
    evidence: str
    date: str
    ancestral_nodes: list[str]
    clade_size: int
    reannotated_below: bool
    review_rows: list[str] = field(default_factory=list)


def is_loss(rec: IBDRecord) -> bool:
    """True for a PAINT loss row: a NOT qualifier, or IRD/IKR evidence even without one.

    >>> is_loss(IBDRecord("PTN1", "GO:1", "F", "IKR", False))
    True
    >>> is_loss(IBDRecord("PTN1", "GO:1", "F", "IBD", False))
    False
    """
    return rec.negated or rec.evidence in ("IRD", "IKR")


def losses_on_lineage(
    tree: dict[str, Any], leaf: str, ibd_index: dict[str, list[IBDRecord]]
) -> list[PaintLoss]:
    """Return the PAINT losses whose node is an ancestor of (or is) ``leaf``.

    ``reannotated_below`` is true when PAINT puts a positive annotation for the same
    term on a node between the loss and the leaf, which lifts the block for this gene.

    >>> tree = {"leaves": {"PTN3": {"uniprot": "P1"}},
    ...         "under": {"PTN1": ["PTN3"], "PTN2": ["PTN3"]}}
    >>> gaf = ["PANTHER\\tPTN2\\tPTN2\\tNOT\\tGO:1\\tGO_REF:0000033\\tIRD\\tPANTHER:PTN1\\tF"
    ...        "\\t\\t\\tprotein\\ttaxon:9606\\t20260101\\tGO_Central\\t\\t"]
    >>> [(x.node, x.go_id, x.ancestral_nodes) for x in losses_on_lineage(tree, "PTN3", parse_ibd_gaf(gaf))]
    [('PTN2', 'GO:1', ['PTN1'])]
    """
    lineage = ancestors_of(tree, leaf)
    found: list[PaintLoss] = []
    for node in sorted(lineage):
        for rec in ibd_index.get(node, []):
            if not is_loss(rec):
                continue
            clade = set(leaves_below(tree, node))
            lifted = any(
                not is_loss(other) and other.go_id == rec.go_id
                for below in lineage
                if below != node and set(leaves_below(tree, below)) < clade
                for other in ibd_index.get(below, [])
            )
            found.append(
                PaintLoss(
                    node=node,
                    go_id=rec.go_id,
                    evidence=rec.evidence,
                    date=rec.date,
                    ancestral_nodes=parse_ptn_nodes("|".join(rec.seeds)),
                    clade_size=len(clade),
                    reannotated_below=lifted,
                )
            )
    return found


def review_rows(review: dict, go_id: str) -> list[str]:
    """Describe the review's existing annotations and core functions on ``go_id``.

    >>> review_rows({"existing_annotations": [{"term": {"id": "GO:1"}, "evidence_type": "IBA",
    ...              "review": {"action": "ACCEPT"}}]}, "GO:1")
    ['IBA:ACCEPT']
    """
    rows = []
    for a in review.get("existing_annotations") or []:
        if (a.get("term") or {}).get("id") == go_id:
            neg = "NOT " if a.get("negated") else ""
            rows.append(f"{neg}{a.get('evidence_type')}:{(a.get('review') or {}).get('action')}")
    for cf in review.get("core_functions") or []:
        ids = [(cf.get(slot) or {}).get("id") for slot in ("molecular_function", "contributes_to_molecular_function")]
        for slot in ("directly_involved_in", "locations", "in_complex"):
            value = cf.get(slot) or []
            ids += [x.get("id") for x in (value if isinstance(value, list) else [value])]
        if go_id in ids:
            rows.append("CORE_FUNCTION")
    return rows


def panther_families(uniprot_txt: str) -> list[str]:
    """Family-level PANTHER ids from a UniProt flat file's DR lines.

    >>> panther_families("DR   PANTHER; PTHR12929; X; 1.\\nDR   PANTHER; PTHR12929:SF20; Y; 1.\\n")
    ['PTHR12929']
    """
    return sorted(set(re.findall(r"^DR   PANTHER; (PTHR\d+);", uniprot_txt, re.M)))


def report(organism: str, gene: str, root: Path = Path(".")) -> tuple[str, list[PaintLoss]]:
    """Build the markdown report for one gene review."""
    folder = root / "genes" / organism / gene
    review = yaml.safe_load((folder / f"{gene}-ai-review.yaml").read_text()) or {}
    accession = str(review.get("id", ""))
    uniprot = folder / f"{gene}-uniprot.txt"
    families = panther_families(uniprot.read_text()) if uniprot.exists() else []
    with open_text(download_cached(IBD_GAF_URL, root / ".cache" / "paint")) as fh:
        ibd_index = parse_ibd_gaf(fh)

    lines = [f"# PAINT losses on the {gene} ({accession}) lineage", ""]
    losses: list[PaintLoss] = []
    for family in families:
        tree = load_family(family, root / ".cache" / "panther_trees")
        if tree is None:
            lines.append(f"- {family}: tree not available; losses not checked.")
            continue
        leaves = leaf_nodes_for(tree, accession)
        if not leaves:
            lines.append(f"- {family}: {accession} is not a leaf of this tree; losses not checked.")
            continue
        for leaf in leaves:
            for loss in losses_on_lineage(tree, leaf, ibd_index):
                loss.review_rows = review_rows(review, loss.go_id)
                losses.append(loss)
    if not families:
        lines.append(f"- No PANTHER family in {uniprot.name}; losses not checked.")
    if losses:
        lines += [
            "| Node | Term | Evidence | Date | Blocks IBD at | Clade | Re-annotated below | Review rows |",
            "|---|---|---|---|---|---|---|---|",
        ]
        for x in losses:
            lines.append(
                f"| {x.node} | {x.go_id} | {x.evidence} | {x.date} | {', '.join(x.ancestral_nodes)} | "
                f"{x.clade_size} | {'yes' if x.reannotated_below else 'no'} | {'; '.join(x.review_rows) or '-'} |"
            )
    elif families:
        lines.append("No IRD or IKR loss on this gene's lineage.")
    return "\n".join(lines), losses


def main(argv: Iterable[str] | None = None) -> int:
    """Print the report for ``ORGANISM GENE``."""
    import argparse

    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("organism")
    parser.add_argument("gene")
    args = parser.parse_args(list(argv) if argv is not None else None)
    text, _ = report(args.organism, args.gene)
    print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
