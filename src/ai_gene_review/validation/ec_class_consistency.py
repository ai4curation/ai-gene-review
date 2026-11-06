"""Warn when a kept molecular-function term names a different class of reaction.

A GO molecular-function term that carries an EC cross-reference states which
reaction the gene product catalyses. When that EC number is in a different EC
*class* (the first digit: oxidoreductase, transferase, hydrolase, lyase,
isomerase, ligase, translocase) from every EC number on the protein's own
UniProt record, the term almost certainly names a different enzyme, not a
broader or narrower description of the same one.

The motivating case is ``genes/PSEPK/PP_2213``. TreeGrafter gave this
AMP-forming acyl-CoA *synthetase* (EC 6.2.1.-, a ligase) ``GO:0004321
fatty-acyl-CoA synthase activity``, which is the fatty acid *synthase* reaction
(EC 2.3.1.86, acetyl-CoA + n malonyl-CoA -> long-chain acyl-CoA). The review
MODIFYed it as "broad ... less precise than fatty acid ligase activity", so a
wrong-reaction term was handled as a refinement. The term was inherited from
one PAINT IBD on the PTHR43605 root, seeded by an RGD IDA on rat Acsm4
(PMID:12709059) whose paper measured "acyl-CoA synthetase activity for fatty
acid activation". Synthase (any enzyme that makes something) and synthetase
(historically, an ATP-dependent ligase) are easy to swap by name, and the EC
class is the cheapest mechanical signal that a swap happened.

What is flagged (WARNING, ``check_type: ec_class_conflict``):

* an ``ACCEPT``, ``KEEP_AS_NON_CORE`` or ``NEW`` existing-annotation row, or a
  ``core_functions`` molecular function, whose term's fully specified EC
  numbers are all in a class the protein's UniProt EC numbers never use;
* a ``MODIFY`` row on such a term whose ``reason``/``summary`` treats it as too
  broad or general. A term for a different reaction is not a broader one: the
  row is either a lateral correction (say so) or a ``REMOVE``.

What is not flagged:

* rows the review already rejects (``REMOVE``, ``MARK_AS_OVER_ANNOTATED``,
  ``UNDECIDED``), ``NOT`` rows, and ``contributes_to`` rows (a subunit can
  contribute to a complex activity in another class: GatA's glutaminase to the
  GatCAB amidotransferase ligase);
* grouping terms whose EC is partial (``1.-.-.-``, ``7.2.2.-``): EC
  reclassification (complex I from 1.6.5.3 to 7.1.1.2, ABC transporters from
  3.6.3 to 7.x) makes those collide with correct proteins;
* proteins with no EC number on the UniProt record;
* class pairs listed in :data:`BENIGN_CLASS_PAIRS`, each with its reason.

Severity is WARNING: the check cannot see a multifunctional protein whose
UniProt record lists only some of its EC numbers, or a moonlighting activity.
In those cases, say in ``reason`` why the term holds despite the EC class.

The audit entry point (``python -m ai_gene_review.validation.ec_class_consistency``)
lists every hit across the review corpus, for fishing upstream errors.
"""

from __future__ import annotations

import re
from functools import lru_cache
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable, Dict, FrozenSet, Iterable, Iterator, List, Optional

from ai_gene_review.validation.validation_report import (
    ValidationReport,
    ValidationSeverity,
)

#: term id -> EC numbers from the GO term's ``EC:`` cross-references.
TermEcLookup = Callable[[str], FrozenSet[str]]

CHECK_TYPE = "ec_class_conflict"

KEPT_ACTIONS = frozenset({"ACCEPT", "KEEP_AS_NON_CORE", "NEW"})

_FULL_EC = re.compile(r"^\d+\.\d+\.\d+\.n?\d+$")
_UNIPROT_EC = re.compile(r"EC=(\d+\.[0-9n.\-]+)")

#: Review wording that treats the term as the right reaction, only too broad.
_REFINEMENT = re.compile(
    r"\b(too (general|broad)|overly (general|broad)|broad|less (precise|specific)"
    r"|more specific|refine)",
    re.IGNORECASE,
)


@dataclass(frozen=True)
class BenignPair:
    """A (term EC prefix, protein EC prefix) pairing that is not a conflict."""

    term_prefix: str
    protein_prefix: str
    reason: str

    def matches(self, term_ec: str, protein_ec: str) -> bool:
        """Whether this pair covers a term EC and a protein EC (either order).

        >>> BenignPair("3.6.4.", "5.6.2.", "x").matches("5.6.2.3", "3.6.4.12")
        True
        >>> BenignPair("3.6.4.", "5.6.2.", "x").matches("3.6.1.1", "5.6.2.3")
        False
        """
        return (
            term_ec.startswith(self.term_prefix)
            and protein_ec.startswith(self.protein_prefix)
        ) or (
            term_ec.startswith(self.protein_prefix)
            and protein_ec.startswith(self.term_prefix)
        )


#: Pairs in which the two EC numbers legitimately describe one protein.
BENIGN_CLASS_PAIRS: tuple[BenignPair, ...] = (
    BenignPair(
        "3.6.4.",
        "5.6.2.",
        "helicases: UniProt keeps the NTP-hydrolysis EC (3.6.4.12/13) while GO's "
        "polarity-specific helicase terms cross-reference the 5.6.2 isomerase class",
    ),
    BenignPair(
        "3.5.1.2",
        "6.3.",
        "glutamine amidotransferases: the glutaminase half-reaction (3.5.1.2) of a "
        "glutamine-dependent ligase (6.3.4/6.3.5) is a real activity of the same chain",
    ),
)


def ec_class(ec: str) -> str:
    """The EC class (first digit).

    >>> ec_class("6.2.1.3")
    '6'
    """
    return ec.split(".", 1)[0]


def is_full_ec(ec: str) -> bool:
    """Whether an EC number is specified to the fourth level.

    >>> is_full_ec("2.3.1.86"), is_full_ec("4.2.2.n2"), is_full_ec("7.2.2.-")
    (True, True, False)
    """
    return bool(_FULL_EC.match(ec))


def uniprot_ec_numbers(uniprot_text: str) -> FrozenSet[str]:
    """EC numbers on the ``DE`` lines of a UniProt flat file.

    ``Includes:`` and ``Contains:`` sections are kept, so a fused or polyprotein
    record contributes all of its activities.

    >>> sorted(uniprot_ec_numbers(
    ...     "DE   SubName: Full=Acyl-CoA synthetase;\\n"
    ...     "DE            EC=6.2.1.- {ECO:0000313|EMBL:AAN67826.1};\\n"
    ...     "CC   -!- FUNCTION: EC=1.1.1.1 is not on a DE line.\\n"))
    ['6.2.1.-']
    """
    found: set[str] = set()
    for line in uniprot_text.splitlines():
        if line.startswith("DE "):
            found.update(_UNIPROT_EC.findall(line))
    return frozenset(found)


def class_conflict(term_ecs: Iterable[str], protein_ecs: Iterable[str]) -> bool:
    """Whether every full term EC is outside every protein EC's class.

    Benign pairs (:data:`BENIGN_CLASS_PAIRS`) count as agreement. Partial term
    ECs are ignored, and no full term EC or no protein EC means no conflict.

    >>> class_conflict({"2.3.1.86"}, {"6.2.1.-"})
    True
    >>> class_conflict({"6.2.1.3"}, {"6.2.1.-"})
    False
    >>> class_conflict({"1.-.-.-"}, {"7.1.1.2"})
    False
    >>> class_conflict({"5.6.2.3"}, {"3.6.4.12"})
    False
    >>> class_conflict({"2.3.1.86"}, set())
    False
    """
    full = [e for e in term_ecs if is_full_ec(e)]
    proteins = list(protein_ecs)
    if not full or not proteins:
        return False
    for term_ec in full:
        for protein_ec in proteins:
            if ec_class(term_ec) == ec_class(protein_ec):
                return False
            if any(p.matches(term_ec, protein_ec) for p in BENIGN_CLASS_PAIRS):
                return False
    return True


@dataclass(frozen=True)
class EcClassConflict:
    """One flagged term: where it sits, the action, and the two EC sets."""

    path: str
    term_id: str
    term_label: str
    action: str
    evidence_type: str
    term_ecs: FrozenSet[str]
    protein_ecs: FrozenSet[str]

    @property
    def is_refinement_modify(self) -> bool:
        """True for a MODIFY row (only refinement-worded MODIFYs are collected)."""
        return self.action == "MODIFY"


def find_ec_class_conflicts(
    data: Dict[str, Any],
    protein_ecs: FrozenSet[str],
    term_ecs: TermEcLookup,
) -> Iterator[EcClassConflict]:
    """Kept MF terms whose EC class contradicts the protein's own EC numbers.

    >>> lookup = {"GO:0004321": frozenset({"2.3.1.86"}),
    ...           "GO:0031956": frozenset({"6.2.1.2"})}.get
    >>> data = {"existing_annotations": [
    ...     {"term": {"id": "GO:0004321", "label": "fatty-acyl-CoA synthase activity"},
    ...      "evidence_type": "IEA",
    ...      "review": {"action": "MODIFY", "reason": "this broad term"}},
    ...     {"term": {"id": "GO:0031956", "label": "medium-chain fatty acid-CoA ligase activity"},
    ...      "evidence_type": "IEA", "review": {"action": "ACCEPT"}}]}
    >>> [(c.term_id, c.action) for c in find_ec_class_conflicts(
    ...     data, frozenset({"6.2.1.-"}), lambda t: lookup(t, frozenset()))]
    [('GO:0004321', 'MODIFY')]
    """
    if not protein_ecs:
        return
    for i, ann in enumerate(data.get("existing_annotations") or []):
        if not isinstance(ann, dict) or ann.get("negated"):
            continue
        if str(ann.get("qualifier") or "").startswith("contributes_to"):
            continue
        term = ann.get("term") or {}
        review = ann.get("review") or {}
        action = review.get("action")
        if action == "MODIFY":
            text = f"{review.get('reason') or ''} {review.get('summary') or ''}"
            if not _REFINEMENT.search(text):
                continue
        elif action not in KEPT_ACTIONS:
            continue
        term_id = term.get("id")
        if not term_id:
            continue
        ecs = term_ecs(term_id)
        if class_conflict(ecs, protein_ecs):
            yield EcClassConflict(
                path=f"existing_annotations[{i}].term",
                term_id=term_id,
                term_label=str(term.get("label") or ""),
                action=str(action),
                evidence_type=str(ann.get("evidence_type") or ""),
                term_ecs=frozenset(ecs),
                protein_ecs=protein_ecs,
            )
    for i, core in enumerate(data.get("core_functions") or []):
        mf = (core or {}).get("molecular_function") or {}
        term_id = mf.get("id")
        if not term_id:
            continue
        ecs = term_ecs(term_id)
        if class_conflict(ecs, protein_ecs):
            yield EcClassConflict(
                path=f"core_functions[{i}].molecular_function",
                term_id=term_id,
                term_label=str(mf.get("label") or ""),
                action="CORE_FUNCTION",
                evidence_type="",
                term_ecs=frozenset(ecs),
                protein_ecs=protein_ecs,
            )


def protein_ecs_for_review(yaml_file: Path) -> FrozenSet[str]:
    """EC numbers from the UniProt record beside a review (empty if none)."""
    records = sorted(Path(yaml_file).parent.glob("*-uniprot.txt"))
    if not records:
        return frozenset()
    return uniprot_ec_numbers(records[0].read_text())


def _message(conflict: EcClassConflict) -> tuple[str, str]:
    """Warning message and suggestion for one conflict."""
    term_ecs = ", ".join(sorted(e for e in conflict.term_ecs if is_full_ec(e)))
    protein_ecs = ", ".join(sorted(conflict.protein_ecs))
    head = (
        f"{conflict.term_id} {conflict.term_label} is EC {term_ecs}, but the "
        f"protein's UniProt EC is {protein_ecs}: a different EC class, so the term "
        "names a different reaction"
    )
    if conflict.is_refinement_modify:
        return (
            f"{head}, yet the MODIFY reason treats it as too broad",
            "A wrong-reaction term is not a general one: use REMOVE with "
            "source_defects (or a MODIFY whose reason says the reaction is wrong). "
            "Check for synthase/synthetase or similar name confusion.",
        )
    return (
        f"{head} ({conflict.action})",
        "Check the term is the protein's reaction (watch synthase vs synthetase); "
        "if it is a genuine additional or moonlighting activity, say so in reason.",
    )


def check_ec_class_consistency(
    data: Dict[str, Any],
    report: ValidationReport,
    yaml_file: Optional[Path],
    term_ecs: Optional[TermEcLookup],
) -> None:
    """Add an ``ec_class_conflict`` warning for each flagged term."""
    if yaml_file is None or term_ecs is None:
        return
    protein_ecs = protein_ecs_for_review(Path(yaml_file))
    for conflict in find_ec_class_conflicts(data, protein_ecs, term_ecs):
        message, suggestion = _message(conflict)
        report.add_issue(
            ValidationSeverity.WARNING,
            message,
            path=conflict.path,
            suggestion=suggestion,
            validation_category="BestPractices",
            check_type=CHECK_TYPE,
        )


@lru_cache(maxsize=1)
def go_term_ecs() -> TermEcLookup:
    """The shared, cached term -> EC lookup over the local GO sqlite (oaklib)."""
    from ai_gene_review.validation.decomposition import _go_adapter

    adapter = _go_adapter()
    cache: Dict[str, FrozenSet[str]] = {}

    def lookup(term_id: str) -> FrozenSet[str]:
        if term_id not in cache:
            cache[term_id] = frozenset(
                obj[3:]
                for _pred, obj in adapter.simple_mappings_by_curie(term_id)
                if obj.startswith("EC:")
            )
        return cache[term_id]

    return lookup


def audit(paths: List[Path], term_ecs: TermEcLookup) -> Iterator[List[str]]:
    """TSV rows (header first) of every conflict across the given reviews."""
    import yaml

    yield [
        "file",
        "path",
        "action",
        "evidence_type",
        "term_id",
        "term_label",
        "term_ec",
        "protein_ec",
    ]
    for path in paths:
        protein_ecs = protein_ecs_for_review(path)
        if not protein_ecs:
            continue
        data = yaml.safe_load(path.read_text()) or {}
        for c in find_ec_class_conflicts(data, protein_ecs, term_ecs):
            yield [
                str(path),
                c.path,
                c.action,
                c.evidence_type,
                c.term_id,
                c.term_label,
                ",".join(sorted(c.term_ecs)),
                ",".join(sorted(c.protein_ecs)),
            ]


def main() -> None:
    """Write the corpus-wide audit TSV (default ``reports/ec-class-conflicts.tsv``)."""
    import argparse
    import csv
    import sys

    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "paths", nargs="*", type=Path, help="review YAMLs (default: all)"
    )
    parser.add_argument(
        "-o", "--output", type=Path, default=Path("reports/ec-class-conflicts.tsv")
    )
    args = parser.parse_args()
    paths = args.paths or sorted(Path("genes").glob("*/*/*-ai-review.yaml"))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    rows = list(audit(paths, go_term_ecs()))
    with args.output.open("w", newline="") as fh:
        csv.writer(fh, delimiter="\t", lineterminator="\n").writerows(rows)
    print(
        f"{len(rows) - 1} EC-class conflicts in {len(paths)} reviews -> {args.output}",
        file=sys.stderr,
    )


if __name__ == "__main__":
    main()
