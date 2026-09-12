"""Cross-check curated family reviews against the gene reviews that inherit from them.

A family review and a gene review can contradict each other, and until now nothing could
see it. The family review says "this term is only safe for these subfamilies"; a gene
review in a different subfamily says "ACCEPT". Both files are individually valid, both
pass their own validators, and the disagreement is invisible.

That is exactly the PGRP case. PTHR11022's single PAINT node asserts amidase activity at
Bilateria, so every descendant inherits it -- including the PGRP-LC receptors that have
demonstrably lost the zinc site. The family review records that; a gene review that
accepted the amidase term anyway would be in direct conflict, and this module is what
notices.

Three checks, all deterministic joins over data already in the repo:

``check_scope_violations``
    A ``term_assessment`` scoped ``SUBFAMILY_ONLY`` names the subfamilies a term is safe
    for. A gene in some *other* subfamily of the same family that retains the term is a
    violation. ``NOT_APPLICABLE`` is the stronger form: no member may retain it.

``check_pruning_conflicts``
    A ``node_assessment`` of ``NEEDS_PRUNING`` / ``TOO_DEEP`` / ``WRONG_NODE`` names the
    subfamilies that wrongly inherit a term. A gene in one of those subfamilies that
    retains the term is a conflict.

``check_family_gene_disagreement``
    The converse direction, which is just as informative: the family says a term IS safe
    for this gene's subfamily, but the gene review removes it. One of the two is wrong and
    a human should decide which.

The join keys are already present: a gene's subfamily comes from its UniProt
``DR PANTHER`` cross-reference, and its actions come from its ``-ai-review.yaml``. Around
2,800 genes in this repo carry both a subfamily and a PANTHER-propagated annotation, so
the surface is real rather than theoretical.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from enum import Enum
from pathlib import Path

import yaml
from yaml import CSafeLoader as _Loader  # libyaml; ~10x faster over the gene corpus

PANTHER_SF_RE = re.compile(r"DR   PANTHER; (PTHR\d+:SF\d+);")
PANTHER_FAM_RE = re.compile(r"DR   PANTHER; (PTHR\d+);")
ACCESSION_RE = re.compile(r"^AC   (\S+?);", re.M)

#: Actions where the gene review keeps the annotation in place.
RETAINING_ACTIONS = {"ACCEPT", "KEEP_AS_NON_CORE"}
#: Actions where the gene review is already pushing back on the annotation.
FLAGGING_ACTIONS = {"REMOVE", "MARK_AS_OVER_ANNOTATED", "MODIFY"}


class Verdict(str, Enum):
    """Outcome of one cross-check."""

    OK = "OK"
    CONFLICT = "CONFLICT"
    UNRESOLVED = "UNRESOLVED"


@dataclass(frozen=True)
class GeneRef:
    """A gene review, with the identifiers needed to join it to a family review."""

    accession: str
    symbol: str
    family: str
    subfamily: str | None
    review_path: Path


@dataclass
class CrossCheck:
    """One family/gene comparison."""

    kind: str
    family: str
    gene: str
    subfamily: str | None
    term: str
    gene_action: str
    verdict: Verdict
    message: str

    def __str__(self) -> str:
        return (
            f"[{self.verdict.value}] {self.kind} {self.family} "
            f"{self.gene} ({self.subfamily or 'no SF'}) {self.term}: {self.message}"
        )


def index_genes_by_family(genes_dir: Path) -> dict[str, list[GeneRef]]:
    """Map PANTHER family CURIE -> gene reviews belonging to it.

    Built by scanning UniProt records line-wise rather than parsing the review YAMLs, so
    the index over the whole corpus is cheap; only genes in a family that actually has a
    review are loaded in full later.
    """
    index: dict[str, list[GeneRef]] = {}
    for uniprot_path in sorted(genes_dir.glob("*/*/*-uniprot.txt")):
        text = uniprot_path.read_text(errors="replace")
        acc_match = ACCESSION_RE.search(text)
        if not acc_match:
            continue
        fam_match = PANTHER_FAM_RE.search(text)
        if not fam_match:
            continue
        sf_match = PANTHER_SF_RE.search(text)
        stem = uniprot_path.name[: -len("-uniprot.txt")]
        review_path = uniprot_path.parent / f"{stem}-ai-review.yaml"
        if not review_path.exists():
            continue
        ref = GeneRef(
            accession=acc_match.group(1),
            symbol=stem,
            family=f"PANTHER:{fam_match.group(1)}",
            subfamily=f"PANTHER:{sf_match.group(1)}" if sf_match else None,
            review_path=review_path,
        )
        index.setdefault(ref.family, []).append(ref)
    return index


def gene_actions_for_term(review_path: Path) -> dict[str, set[str]]:
    """Map GO term id -> the set of review actions the gene records for it.

    A gene can carry several rows for one term (different evidence codes), so the value is
    a set. Negated rows are skipped: a ``NOT`` annotation asserting the gene lacks the
    function is agreement with a family review that says the term is unsafe, not conflict.
    """
    doc = yaml.load(review_path.read_text(), Loader=_Loader)
    actions: dict[str, set[str]] = {}
    for ann in (doc or {}).get("existing_annotations") or []:
        if ann.get("negated"):
            continue
        term = (ann.get("term") or {}).get("id")
        action = ((ann.get("review") or {}).get("action")) or ""
        if term:
            actions.setdefault(term, set()).add(action)
    return actions


def _term_ids(entries) -> list[tuple[str, str]]:
    """Extract (id, label) from a list of inlined Term objects."""
    out = []
    for e in entries or []:
        if isinstance(e, dict) and e.get("id"):
            out.append((e["id"], e.get("label", "")))
    return out


def check_scope_violations(
    review: dict, gene_index: dict[str, list[GeneRef]]
) -> list[CrossCheck]:
    """Genes retaining a term the family scoped away from their subfamily."""
    family = review.get("family_id", "?")
    results: list[CrossCheck] = []

    for assessment in review.get("term_assessments") or []:
        scope = assessment.get("scope")
        if scope not in ("SUBFAMILY_ONLY", "NOT_APPLICABLE"):
            continue
        term = (assessment.get("assessed_term") or {}).get("id", "?")
        allowed = {sf for sf, _ in _term_ids(assessment.get("applicable_subfamilies"))}

        for gene in gene_index.get(family, []):
            if scope == "SUBFAMILY_ONLY" and gene.subfamily in allowed:
                continue
            actions = gene_actions_for_term(gene.review_path).get(term)
            if not actions:
                continue
            if scope == "SUBFAMILY_ONLY" and gene.subfamily is None:
                # No PANTHER subfamily cross-reference, so we cannot tell whether the
                # gene falls inside the allowed set. That is missing information, not
                # a contradiction.
                results.append(
                    CrossCheck(
                        "SCOPE_VIOLATION", family, gene.symbol, None, term,
                        "/".join(sorted(actions)), Verdict.UNRESOLVED,
                        "gene has no PANTHER subfamily cross-reference, so it cannot be "
                        "placed inside or outside the term's allowed subfamilies",
                    )
                )
                continue
            retained = actions & RETAINING_ACTIONS
            if retained:
                where = (
                    "no member of this family may retain it"
                    if scope == "NOT_APPLICABLE"
                    else f"safe only for {sorted(allowed) or '(none listed)'}"
                )
                results.append(
                    CrossCheck(
                        "SCOPE_VIOLATION", family, gene.symbol, gene.subfamily, term,
                        "/".join(sorted(retained)), Verdict.CONFLICT,
                        f"family scopes this term {scope} ({where}) but the gene "
                        f"review keeps it",
                    )
                )
            else:
                results.append(
                    CrossCheck(
                        "SCOPE_VIOLATION", family, gene.symbol, gene.subfamily, term,
                        "/".join(sorted(actions)), Verdict.OK,
                        "gene review already flags this term, consistent with the family scope",
                    )
                )
    return results


def check_pruning_conflicts(
    review: dict, gene_index: dict[str, list[GeneRef]]
) -> list[CrossCheck]:
    """Genes retaining a term whose node assessment says their subfamily should be pruned."""
    family = review.get("family_id", "?")
    negative = {"NEEDS_PRUNING", "TOO_DEEP", "WRONG_NODE"}
    results: list[CrossCheck] = []

    for assessment in review.get("node_assessments") or []:
        if assessment.get("assessment") not in negative:
            continue
        node = assessment.get("node_id", "?")
        term = (assessment.get("asserted_term") or {}).get("id", "?")
        affected = {sf for sf, _ in _term_ids(assessment.get("affected_subfamilies"))}
        if not affected:
            continue

        for gene in gene_index.get(family, []):
            if gene.subfamily not in affected:
                continue
            actions = gene_actions_for_term(gene.review_path).get(term)
            if not actions:
                continue
            retained = actions & RETAINING_ACTIONS
            if retained:
                results.append(
                    CrossCheck(
                        "PRUNING_CONFLICT", family, gene.symbol, gene.subfamily, term,
                        "/".join(sorted(retained)), Verdict.CONFLICT,
                        f"family says {node} needs pruning for this subfamily, "
                        f"but the gene review keeps the term",
                    )
                )
            else:
                results.append(
                    CrossCheck(
                        "PRUNING_CONFLICT", family, gene.symbol, gene.subfamily, term,
                        "/".join(sorted(actions)), Verdict.OK,
                        f"gene review flags the term, consistent with pruning {node}",
                    )
                )
    return results


def check_family_gene_disagreement(
    review: dict, gene_index: dict[str, list[GeneRef]]
) -> list[CrossCheck]:
    """The converse: the family says a term is safe here, but the gene removes it.

    Reported because it is a genuine disagreement someone should adjudicate, not because
    the gene is presumed wrong -- a gene reviewer with target-specific experimental
    evidence may well be right and the family assessment too permissive.
    """
    family = review.get("family_id", "?")
    results: list[CrossCheck] = []

    for assessment in review.get("term_assessments") or []:
        scope = assessment.get("scope")
        term = (assessment.get("assessed_term") or {}).get("id", "?")
        allowed = {sf for sf, _ in _term_ids(assessment.get("applicable_subfamilies"))}

        for gene in gene_index.get(family, []):
            covered = scope == "FAMILY_WIDE" or (
                scope == "SUBFAMILY_ONLY" and gene.subfamily in allowed
            )
            if not covered:
                continue
            actions = gene_actions_for_term(gene.review_path).get(term)
            if not actions:
                continue
            removing = actions & {"REMOVE"}
            if removing:
                results.append(
                    CrossCheck(
                        "FAMILY_GENE_DISAGREEMENT", family, gene.symbol, gene.subfamily,
                        term, "REMOVE", Verdict.CONFLICT,
                        f"family scopes this term {scope} covering this gene, "
                        f"but the gene review removes it",
                    )
                )
    return results


def crosscheck_family_review(
    path: Path, genes_dir: Path = Path("genes")
) -> list[CrossCheck]:
    """Run all family/gene cross-checks for one family review."""
    review = yaml.load(path.read_text(), Loader=_Loader)
    gene_index = index_genes_by_family(genes_dir)
    return (
        check_scope_violations(review, gene_index)
        + check_pruning_conflicts(review, gene_index)
        + check_family_gene_disagreement(review, gene_index)
    )


def main(argv: list[str] | None = None) -> int:
    """Cross-check every family review against the gene corpus."""
    import argparse
    import sys

    parser = argparse.ArgumentParser(description="Cross-check family and gene reviews.")
    parser.add_argument("paths", nargs="*", type=Path)
    parser.add_argument("--genes-dir", type=Path, default=Path("genes"))
    args = parser.parse_args(argv)

    paths = args.paths or sorted(
        Path("interpro/panther").glob("PTHR*/PTHR*-review.yaml")
    )
    if not paths:
        print("No family review files found.")
        return 0

    gene_index = index_genes_by_family(args.genes_dir)
    conflicts, ok = 0, 0
    for path in paths:
        review = yaml.load(path.read_text(), Loader=_Loader)
        results = (
            check_scope_violations(review, gene_index)
            + check_pruning_conflicts(review, gene_index)
            + check_family_gene_disagreement(review, gene_index)
        )
        for r in results:
            if r.verdict is Verdict.CONFLICT:
                conflicts += 1
                print(r, file=sys.stderr)
            else:
                ok += 1

    print(
        f"family/gene cross-check over {len(paths)} family review(s): "
        f"{conflicts} conflict(s), {ok} consistent"
    )
    return 1 if conflicts else 0


if __name__ == "__main__":
    raise SystemExit(main())
