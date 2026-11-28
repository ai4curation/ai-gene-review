"""Ask for the tree behind a verdict that overrules an IBA.

An IBA is a PAINT curator's placement of a function on a node of a PANTHER family tree,
made with the whole tree and the family alignment in view. ``REMOVE`` and
``MARK_AS_OVER_ANNOTATED`` argue with that placement, so the argument should rest on
where the node sits, where its seeds sit and where the gene sits -- not on the node id
and seed list alone, which is all a GOA row carries. A census of this repository found
that about 95% of overruled IBA rows had no tree or alignment artifact behind them.

``just phylo <org> <GENE>`` writes ``GENE-phylo.yaml`` with those facts for every IBA row
(see :mod:`ai_gene_review.etl.gene_phylo`). The checks here ask a review to use it:

``missing_tree_evidence``
    An IBA row with action ``REMOVE`` or ``MARK_AS_OVER_ANNOTATED`` has no ``supported_by``
    entry that quotes the gene's own ``GENE-phylo.yaml``.
``tree_evidence_other_row``
    It quotes the extract, but no quote names this row's term, so it describes another row.
``tree_evidence_adverse_unquoted``
    It quotes the row, but not a sentence of the row's summary that stands against the
    verdict: that the gene is itself a seed of the node, that it lies inside the clade the
    seeds span, that seeds share its own branch below the node, or, for a row overruled
    as ``WRONG_ORTHOLOG_OR_PARALOG``, that the tree relates every seed to the gene as an
    ortholog. A verdict can stand in spite of any of these, but it has to face them:
    quoting around such a sentence is how a selected slice of the tree ends up as the
    evidence (:func:`adverse_sentences`).
``kept_under_paint_loss``
    An IBA row is kept (``ACCEPT``, ``KEEP_AS_NON_CORE``, ``MODIFY``, ``TOO_GENERAL``)
    although its extract says PAINT has removed the term on the path to the gene and has
    not asserted it again below, and the row does not quote that sentence. The cached GOA
    row is then stale.
``missing_residue_evidence``
    A propagated row is overruled with failure mode ``PSEUDO_OR_SUBACTIVITY_LOSS`` and
    carries neither ``residue_claims`` nor ``residue_claims_not_applicable``. "Lacks the
    catalytic residues" was wrong about the mechanism in 4 of the 17 cases checked by
    alignment; the extract's ``residue_sites`` reads curated sites off PANTHER's alignment.

Whether a quote is really in the extract is checked separately, like every other
``file:`` quote (:mod:`ai_gene_review.validation.local_source_text`).

Severity is WARNING, as for the other action policies: the checks guide re-review and do
not block legacy files. Rows that keep the claim (``ACCEPT``, ``KEEP_AS_NON_CORE``,
``MODIFY``, ``TOO_GENERAL``) are asked only about a PAINT loss, and ``UNDECIDED`` rows are
not asked for the tree at all. Neither is a review row whose IBA is no longer in the
gene's GOA file: PAINT has withdrawn the annotation, so the extract, which describes the
rows of that file, has nothing to quote.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any, Iterable, Iterator, Optional, Sequence

import yaml

#: Actions that say PAINT's placement does not hold for this gene.
OVERRULING_ACTIONS = frozenset({"REMOVE", "MARK_AS_OVER_ANNOTATED"})
#: Actions that keep the claim, as it is or refined.
KEEPING_ACTIONS = frozenset({"ACCEPT", "KEEP_AS_NON_CORE", "MODIFY", "TOO_GENERAL"})
PHYLO_SUFFIX = "-phylo.yaml"
RESIDUE_FAILURE_MODE = "PSEUDO_OR_SUBACTIVITY_LOSS"
PARALOG_FAILURE_MODE = "WRONG_ORTHOLOG_OR_PARALOG"

_SELF_SEED = re.compile(r" is itself a seed: ")
_INSIDE_SEED_CLADE = re.compile(r"; .+ is inside that clade\.$")
_SEEDS_ON_OWN_BRANCH = re.compile(r"; (?!none )\S+ of (?:them|the other seeds) shares? .+'s own branch below it \(")
_RELATION = re.compile(r"^By the tree the (?:other )?seeds? (?:is|are) ")
_PAINT_LOSS = re.compile(r"^PAINT \S+ at \S+ \(\S*\) removes this term on the path to ")


def sentences(summary: str) -> list[str]:
    """Split an extract summary so that joining neighbours with a space gives the text back.

    >>> sentences("GO:1 (x): a node. cds1 is 4 steps below it; path length 1.512. Seeds: 2 of 2.")
    ['GO:1 (x): a node.', 'cds1 is 4 steps below it; path length 1.512.', 'Seeds: 2 of 2.']
    """
    parts = summary.strip().split(". ")
    return [part + "." for part in parts[:-1]] + [parts[-1]]


def quotes_from(summary: str, numbers: Iterable[int]) -> list[str]:
    """Verbatim quotes for the chosen sentences (1-based); neighbours are joined.

    The first sentence, which names the term and the node, is always quoted.

    >>> quotes_from("A b. C d. E f. G h.", [4, 2])
    ['A b. C d.', 'G h.']
    """
    parts = sentences(summary)
    chosen = sorted({1, *(n for n in numbers if 1 <= n <= len(parts))})
    groups: list[list[int]] = []
    for number in chosen:
        if groups and number == groups[-1][-1] + 1:
            groups[-1].append(number)
        else:
            groups.append([number])
    return [" ".join(parts[n - 1] for n in group) for group in groups]


def adverse_sentences(
    summary: str, failure_modes: Sequence[str] = (), kept: bool = False
) -> list[tuple[int, str, str]]:
    """The sentences of an extract row's summary that stand against a verdict on the row.

    Returns ``(sentence number, what it says, the sentence)``, numbered from 1 as
    :func:`sentences` splits the summary. For a verdict that overrules the row these are
    the sentences saying that the gene is itself a seed, that it is inside the clade the
    seeds span, that seeds share its own branch below a node they bracket, and, when the
    row is overruled as a wrong ortholog or paralog (``failure_modes``), that the tree
    relates every seed to the gene as an ortholog. For a row that is ``kept`` it is the
    sentence saying PAINT has removed the term on the path to the gene without asserting
    it again below.

    >>> text = ("GO:1 (x): PAINT node PTN1 is a speciation node at LUCA. Seeds: 2 of 2 resolved. "
    ...         "They all sit in one branch below the node: their common ancestor is PTN2; abc is inside that clade. "
    ...         "By the tree the seeds are 2 one-to-one orthologs of abc.")
    >>> [(number, what) for number, what, _ in adverse_sentences(text)]
    [(3, 'the gene is inside the clade the seeds span')]
    >>> [number for number, _, _ in adverse_sentences(text, failure_modes=["WRONG_ORTHOLOG_OR_PARALOG"])]
    [3, 4]
    >>> adverse_sentences(text, kept=True)
    []
    """
    found: list[tuple[int, str, str]] = []
    for number, sentence in enumerate(sentences(summary), 1):
        if kept:
            if _PAINT_LOSS.search(sentence) and "asserts it again below the loss" not in sentence:
                found.append((number, "PAINT has removed the term on the path to the gene", sentence))
            continue
        if _INSIDE_SEED_CLADE.search(sentence):
            found.append((number, "the gene is inside the clade the seeds span", sentence))
        if _SEEDS_ON_OWN_BRANCH.search(sentence):
            found.append((number, "seeds share the gene's own branch below the node", sentence))
        if _SELF_SEED.search(sentence):
            found.append((number, "the gene is itself a seed of the node", sentence))
        if (
            PARALOG_FAILURE_MODE in failure_modes
            and _RELATION.search(sentence)
            and "ortholog" in sentence
            and "paralog" not in sentence
            and "xenolog" not in sentence
        ):
            found.append((number, "the tree relates every seed to the gene as an ortholog", sentence))
    return found


def extract_summaries(yaml_file: Optional[Path]) -> dict[tuple[str, bool], str]:
    """The summary of every row of the extract beside a review, by ``(term id, negated)``.

    Empty when the review is not in a gene folder or the gene has no extract.

    >>> extract_summaries(None)
    {}
    >>> extract_summaries(Path("genes/human/NO_SUCH_GENE/NO_SUCH_GENE-ai-review.yaml"))
    {}
    """
    if yaml_file is None:
        return {}
    folder = Path(yaml_file).parent
    extract = folder / f"{folder.name}{PHYLO_SUFFIX}"
    if folder.parent.parent.name != "genes" or not extract.exists():
        return {}
    loader = getattr(yaml, "CSafeLoader", yaml.SafeLoader)
    doc = yaml.load(extract.read_text(encoding="utf-8"), Loader=loader) or {}
    found: dict[tuple[str, bool], str] = {}
    for tree in doc.get("trees") or []:
        for row in tree.get("rows") or []:
            found.setdefault((row["term"]["id"], bool(row.get("negated"))), row.get("summary", ""))
    return found


def phylo_reference_ids(yaml_file: Optional[Path]) -> set[str]:
    """Reference ids that name the extract of the gene a review file belongs to.

    Empty when the review is not in a ``genes/<org>/<GENE>/`` folder.

    >>> sorted(phylo_reference_ids(Path("genes/human/CIRBP/CIRBP-ai-review.yaml")))
    ['file:genes/human/CIRBP/CIRBP-phylo.yaml', 'file:human/CIRBP/CIRBP-phylo.yaml']
    """
    if yaml_file is None:
        return set()
    folder = Path(yaml_file).parent
    if folder.parent.parent.name != "genes":
        return set()
    relative = f"{folder.parent.name}/{folder.name}/{folder.name}{PHYLO_SUFFIX}"
    return {f"file:{relative}", f"file:genes/{relative}"}


def current_iba_rows(yaml_file: Optional[Path]) -> Optional[set[tuple[str, bool]]]:
    """``(term id, negated)`` of every IBA row in the GOA file beside a review.

    None when the review has no GOA file beside it, in which case nothing can be said
    about which of its rows are current.

    >>> current_iba_rows(None) is None
    True
    >>> current_iba_rows(Path("genes/human/NO_SUCH_GENE/NO_SUCH_GENE-ai-review.yaml")) is None
    True
    """
    if yaml_file is None:
        return None
    folder = Path(yaml_file).parent
    goa = folder / f"{folder.name}-goa.tsv"
    if not goa.exists():
        return None
    from ai_gene_review.etl.gene_phylo import read_iba_rows

    return {(row.term_id, row.negated) for row in read_iba_rows(goa)}


def _quotes(item: dict[str, Any]) -> list[str]:
    """The quoted text of one ``supported_by`` entry (a string or a list of strings)."""
    text = item.get("supporting_text")
    if isinstance(text, str):
        return [text]
    if isinstance(text, list):
        return [str(t.get("text", "")) if isinstance(t, dict) else str(t) for t in text]
    return []


def iter_tree_evidence_violations(
    data: dict[str, Any], yaml_file: Optional[Path] = None
) -> Iterator[tuple[int, str, str, str]]:
    """Yield ``(row index, check type, message, suggestion)`` for each policy violation."""
    own = phylo_reference_ids(yaml_file)
    gene = Path(yaml_file).parent.name if own and yaml_file is not None else "GENE"
    organism = Path(yaml_file).parent.parent.name if own and yaml_file is not None else "<org>"
    current: Optional[set[tuple[str, bool]]] = None
    goa_read = False
    summaries: Optional[dict[tuple[str, bool], str]] = None
    for index, annotation in enumerate(data.get("existing_annotations") or []):
        if not isinstance(annotation, dict):
            continue
        review = annotation.get("review")
        if not isinstance(review, dict):
            continue
        action = review.get("action")
        evidence = annotation.get("evidence_type")
        if action not in OVERRULING_ACTIONS and not (evidence == "IBA" and action in KEEPING_ACTIONS):
            continue
        term = annotation.get("term")
        term_id = term.get("id", "") if isinstance(term, dict) else ""
        key = (term_id, bool(annotation.get("negated")))
        propagation = review.get("propagation_review")
        propagation = propagation if isinstance(propagation, dict) else {}

        withdrawn = False
        cited: list[dict[str, Any]] = []
        if evidence == "IBA":
            if not goa_read:
                current, goa_read = current_iba_rows(yaml_file), True
            # No such IBA row in the gene's GOA file any more: the extract has no row to quote.
            withdrawn = current is not None and key not in current
            cited = [
                item
                for item in review.get("supported_by") or []
                if isinstance(item, dict)
                and (
                    str(item.get("reference_id", "")) in own
                    if own
                    else str(item.get("reference_id", "")).endswith(PHYLO_SUFFIX)
                )
            ]
            if summaries is None:
                summaries = extract_summaries(yaml_file)
        quoted = [quote for item in cited for quote in _quotes(item)]

        if action in KEEPING_ACTIONS:
            # Only reached for an IBA row: is it kept under a loss PAINT has not lifted?
            losses = [] if withdrawn else adverse_sentences((summaries or {}).get(key, ""), kept=True)
            for _, _, sentence in losses:
                if not any(sentence in quote for quote in quoted):
                    yield (
                        index,
                        "kept_under_paint_loss",
                        f"IBA row on {term_id} is kept ({action}) although PAINT has removed the term "
                        f"on the path to the gene: {sentence}",
                        "The cached GOA row is stale. If the loss holds for this gene, overrule the "
                        "row; if the loss is wrong or too broad, say so in the reason. Either way "
                        f"quote that sentence of the {term_id} row's summary in supported_by "
                        f"(reference_id file:{organism}/{gene}/{gene}{PHYLO_SUFFIX})",
                    )
            continue

        if evidence == "IBA" and not withdrawn:
            if not cited:
                yield (
                    index,
                    "missing_tree_evidence",
                    f"IBA row on {term_id} is overruled ({action}) without citing the gene's "
                    "PANTHER tree placement",
                    f"Run `just phylo {organism} {gene}`, read the row for {term_id} in "
                    f"{gene}{PHYLO_SUFFIX} (where the PAINT node sits, where its seeds sit, "
                    "how the gene compares with them in the family alignment), and quote that "
                    f"row's `summary` in supported_by with reference_id "
                    f"file:{organism}/{gene}/{gene}{PHYLO_SUFFIX}. If the tree does not "
                    "support the verdict, reconsider the verdict",
                )
            elif term_id and not any(term_id in quote for quote in quoted):
                yield (
                    index,
                    "tree_evidence_other_row",
                    f"IBA row on {term_id} cites {gene}{PHYLO_SUFFIX}, but no quote names {term_id}",
                    f"Quote the `summary` of the {term_id} row; each summary starts with its term id",
                )
            else:
                adverse = adverse_sentences(
                    (summaries or {}).get(key, ""), failure_modes=propagation.get("failure_modes") or []
                )
                unquoted = [
                    (number, what)
                    for number, what, sentence in adverse
                    if not any(sentence in quote for quote in quoted)
                ]
                if unquoted:
                    numbers = ", ".join(str(number) for number in sorted({number for number, _ in unquoted}))
                    yield (
                        index,
                        "tree_evidence_adverse_unquoted",
                        f"IBA row on {term_id} is overruled ({action}) and quotes {gene}{PHYLO_SUFFIX}, "
                        "but not what stands against the verdict there: "
                        + "; ".join(what for _, what in unquoted),
                        f"Quote sentence {numbers} of the {term_id} row's summary as well (sentences "
                        "are counted from 1 and end at a full stop followed by a space), and say in "
                        "the reason why the verdict holds in spite of it",
                    )

        if (
            RESIDUE_FAILURE_MODE in (propagation.get("failure_modes") or [])
            and not propagation.get("residue_claims")
            and not propagation.get("residue_claims_not_applicable")
        ):
            yield (
                index,
                "missing_residue_evidence",
                f"{evidence} row on {term_id} is overruled ({action}) for residue or sub-activity "
                "loss without a checkable residue claim",
                "Add propagation_review.residue_claims (anchor and target position and residue; "
                f"{gene}{PHYLO_SUFFIX} lists the family's curated sites read off the PANTHER "
                "alignment under residue_sites), or say in residue_claims_not_applicable why "
                "the argument is not a point-residue question",
            )


def check_tree_evidence(data: dict[str, Any], report: Any, yaml_file: Optional[Path] = None) -> None:
    """Add a WARNING to ``report`` for each tree-evidence policy violation."""
    from ai_gene_review.validation.validation_report import ValidationSeverity

    for index, check_type, message, suggestion in iter_tree_evidence_violations(data, yaml_file):
        report.add_issue(
            ValidationSeverity.WARNING,
            message,
            path=f"existing_annotations[{index}].review",
            suggestion=suggestion,
            validation_category="BestPractices",
            check_type=check_type,
        )
