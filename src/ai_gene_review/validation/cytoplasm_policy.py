"""Warn when a eukaryotic review treats ``GO:0005737`` cytoplasm as a core location.

GO defines cytoplasm as "The contents of a cell excluding the plasma membrane and
nucleus, but including other subcellular structures." In a eukaryote that takes in
the cytosol and every organelle, so the term says little more than "not nuclear, not
extracellular". It is true of almost every protein that is neither nuclear nor
secreted, it is what a naive predictor outputs (the ``LOCALIZATION_DEFAULT`` error
type), and when an author writes "cytoplasmic" they usually mean cytosolic. The
policy is ``projects/CYTOPLASM.md``. In short:

* **Eukaryotes.** Cytoplasm never names where a core activity happens, so a row is
  never ``ACCEPT`` (which marks the core function) and ``core_functions.locations``
  never names it. A row whose term is entailed by a more specific location the review
  asserts (cytosol, an organelle, a granule, the cell cortex) is ``TOO_GENERAL``. This
  is the "membrane (which membrane?)" case of the 2026-11-14 ruling. A row whose own
  evidence resolves a sub-location is ``MODIFY``. Otherwise it is ``KEEP_AS_NON_CORE``.
  A ``NEW`` cytoplasm row adds a claim that carries almost no information.
* **Prokaryotes.** With no organelles, cytoplasm is the main localisation contrast
  (with membrane, periplasm and the outside) and is informative. The normal rules
  apply, and like a root organelle term it is never ``TOO_GENERAL``.
* **Viruses** and entries whose lineage cannot be read are out of scope.

What is flagged (WARNING, ``check_type: cytoplasm_policy``), for eukaryotic entries
only, judged from the ``OC`` lineage of the UniProt record beside the review:

* an ``ACCEPT`` or ``NEW`` row on ``GO:0005737`` that is not ``NOT``-qualified;
* ``GO:0005737`` in ``core_functions[].locations``.

Severity is WARNING. Thousands of merged rows predate the policy, and it applies to
new and revisited reviews rather than condemning those. ``just validate`` runs per
gene, so an author sees only their own.

The audit entry point (``python -m ai_gene_review.validation.cytoplasm_policy``,
``just cytoplasm-audit``) lists every row the policy would change across the corpus,
including two categories the validator leaves alone because they need judgement:
``MODIFY`` on a propagated eukaryotic row, whose evidence stops at cytoplasm by
construction, and ``TOO_GENERAL`` rows that nothing in the review entails.
"""

from __future__ import annotations

import re
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable, Dict, FrozenSet, Iterator, List, Optional

CYTOPLASM = "GO:0005737"
CYTOPLASM_LABEL = "cytoplasm"
CHECK_TYPE = "cytoplasm_policy"

EUKARYOTA = "Eukaryota"
PROKARYOTES = frozenset({"Bacteria", "Archaea"})

#: Evidence codes whose source is itself a cytoplasm annotation, keyword or mapping
#: (a PAINT node, a UniProt subcellular location, an ortholog's row, a signature).
#: A MODIFY on one of these has no evidence of its own for the deeper term.
PROPAGATED_EVIDENCE = frozenset(
    {"IBA", "IBD", "IEA", "ISS", "ISO", "ISA", "ISM", "IGC", "RCA"}
)

#: Actions under which a row's term stays asserted as true.
ASSERTING_ACTIONS = frozenset({"ACCEPT", "KEEP_AS_NON_CORE", "NEW", "TOO_GENERAL"})

#: Maps a term id to its strict is_a/part_of ancestors.
Ancestors = Callable[[str], FrozenSet[str]]

_OC_RE = re.compile(r"^OC   ([A-Za-z]+)", re.M)


def uniprot_domain(uniprot_text: str) -> Optional[str]:
    """The top-level lineage name from a UniProt flat file's first ``OC`` line.

    >>> uniprot_domain("ID   X\\nOC   Eukaryota; Metazoa; Chordata;\\n")
    'Eukaryota'
    >>> uniprot_domain("OC   Bacteria; Pseudomonadota.\\n")
    'Bacteria'
    >>> uniprot_domain("ID   X\\n") is None
    True
    """
    match = _OC_RE.search(uniprot_text)
    return match.group(1) if match else None


def domain_for_review(yaml_file: Path) -> Optional[str]:
    """Lineage domain from the UniProt record beside a review (None if none)."""
    records = sorted(Path(yaml_file).parent.glob("*-uniprot.txt"))
    if not records:
        return None
    return uniprot_domain(records[0].read_text(errors="replace"))


def _term_id(annotation: Dict[str, Any]) -> Optional[str]:
    term = annotation.get("term")
    return term.get("id") if isinstance(term, dict) else None


def _action(annotation: Dict[str, Any]) -> Optional[str]:
    review = annotation.get("review")
    if not isinstance(review, dict):
        return None
    action = review.get("action")
    return action if isinstance(action, str) else None


def _annotations(data: Dict[str, Any]) -> List[Dict[str, Any]]:
    rows = data.get("existing_annotations")
    return [r for r in rows if isinstance(r, dict)] if isinstance(rows, list) else []


def _core_functions(data: Dict[str, Any]) -> List[Dict[str, Any]]:
    rows = data.get("core_functions")
    return [r for r in rows if isinstance(r, dict)] if isinstance(rows, list) else []


def _location_ids(core_function: Dict[str, Any]) -> List[str]:
    locations = core_function.get("locations")
    if not isinstance(locations, list):
        return []
    return [
        str(loc["id"])
        for loc in locations
        if isinstance(loc, dict) and isinstance(loc.get("id"), str)
    ]


def asserted_terms(data: Dict[str, Any], skip_index: Optional[int] = None) -> set[str]:
    """Term ids the review asserts as true, besides row *skip_index*.

    Rows kept under an asserting action, the replacements a MODIFY proposes, and the
    core-function locations. ``NOT`` rows assert nothing positive.

    >>> doc = {"existing_annotations": [
    ...     {"term": {"id": "GO:0005737"}, "review": {"action": "ACCEPT"}},
    ...     {"term": {"id": "GO:0005634"}, "review": {"action": "REMOVE"}},
    ...     {"term": {"id": "GO:0005739"}, "review": {"action": "MODIFY",
    ...      "proposed_replacement_terms": [{"id": "GO:0005759"}]}}],
    ...  "core_functions": [{"locations": [{"id": "GO:0005829"}]}]}
    >>> sorted(asserted_terms(doc, skip_index=0))
    ['GO:0005759', 'GO:0005829']
    """
    found: set[str] = set()
    for index, annotation in enumerate(_annotations(data)):
        if index == skip_index or annotation.get("negated"):
            continue
        action = _action(annotation)
        term_id = _term_id(annotation)
        if action in ASSERTING_ACTIONS and term_id:
            found.add(term_id)
        if action == "MODIFY":
            review = annotation.get("review") or {}
            for repl in review.get("proposed_replacement_terms") or []:
                if isinstance(repl, dict) and isinstance(repl.get("id"), str):
                    found.add(repl["id"])
    for core_function in _core_functions(data):
        found.update(_location_ids(core_function))
    return found


def entailing_terms(
    data: Dict[str, Any], skip_index: Optional[int], ancestors: Ancestors
) -> List[str]:
    """Asserted terms that have cytoplasm as an is_a/part_of ancestor.

    These are what make a cytoplasm row ``TOO_GENERAL``. Cytoskeleton, microtubule,
    centrosome, ribosome and nucleoid are not among them: GO does not place them
    under cytoplasm, because they also occur in the nucleus or in organelles.
    """
    return sorted(
        t
        for t in asserted_terms(data, skip_index)
        if t != CYTOPLASM and CYTOPLASM in ancestors(t)
    )


@dataclass(frozen=True)
class CytoplasmFinding:
    """One row or core-function location the policy would change."""

    category: str
    path: str
    action: str
    evidence_type: str
    reference: str
    entailing: tuple[str, ...]


#: Categories that ``just validate`` reports; the rest are audit-only.
WARNED_CATEGORIES = frozenset({"EUK_ACCEPT", "EUK_NEW", "EUK_CORE_LOCATION"})


def find_cytoplasm_findings(
    data: Dict[str, Any],
    domain: Optional[str],
    ancestors: Optional[Ancestors] = None,
) -> Iterator[CytoplasmFinding]:
    """Yield every place the cytoplasm policy would change in one review.

    Categories, eukaryotes:

    * ``EUK_ACCEPT``, ``EUK_NEW``: an ACCEPT or NEW cytoplasm row (warned);
    * ``EUK_CORE_LOCATION``: cytoplasm in ``core_functions.locations`` (warned);
    * ``EUK_MODIFY_PROPAGATED``: MODIFY on a propagated row, whose evidence stops at
      cytoplasm (use TOO_GENERAL, or KEEP_AS_NON_CORE plus a NEW row for the
      specific location on its own evidence);
    * ``EUK_TOO_GENERAL_UNENTAILED``: TOO_GENERAL, but nothing the review asserts
      entails cytoplasm (needs *ancestors*).

    Prokaryotes: ``PROK_TOO_GENERAL``, since cytoplasm is informative there.

    >>> doc = {"existing_annotations": [
    ...     {"term": {"id": "GO:0005737"}, "evidence_type": "IBA",
    ...      "review": {"action": "ACCEPT"}}]}
    >>> [f.category for f in find_cytoplasm_findings(doc, "Eukaryota")]
    ['EUK_ACCEPT']
    >>> list(find_cytoplasm_findings(doc, "Bacteria"))
    []
    """
    eukaryote = domain == EUKARYOTA
    prokaryote = domain in PROKARYOTES
    if not (eukaryote or prokaryote):
        return
    for index, annotation in enumerate(_annotations(data)):
        if _term_id(annotation) != CYTOPLASM or annotation.get("negated"):
            continue
        action = _action(annotation) or ""
        evidence = str(annotation.get("evidence_type") or "")
        reference = str(annotation.get("original_reference_id") or "")
        path = f"existing_annotations[{index}]"
        category: Optional[str] = None
        entailing: tuple[str, ...] = ()
        if ancestors is not None and (eukaryote or action == "TOO_GENERAL"):
            entailing = tuple(entailing_terms(data, index, ancestors))
        if prokaryote:
            if action == "TOO_GENERAL":
                category = "PROK_TOO_GENERAL"
        elif action == "ACCEPT":
            category = "EUK_ACCEPT"
        elif action == "NEW":
            category = "EUK_NEW"
        elif action == "MODIFY" and evidence in PROPAGATED_EVIDENCE:
            category = "EUK_MODIFY_PROPAGATED"
        elif action == "TOO_GENERAL" and ancestors is not None and not entailing:
            category = "EUK_TOO_GENERAL_UNENTAILED"
        if category:
            yield CytoplasmFinding(
                category,
                f"{path}.review.action",
                action,
                evidence,
                reference,
                entailing,
            )
    if not eukaryote:
        return
    for index, core_function in enumerate(_core_functions(data)):
        for loc_index, term_id in enumerate(_location_ids(core_function)):
            if term_id == CYTOPLASM:
                yield CytoplasmFinding(
                    "EUK_CORE_LOCATION",
                    f"core_functions[{index}].locations[{loc_index}]",
                    "CORE_FUNCTION",
                    "",
                    "",
                    (),
                )


def mentions_cytoplasm(data: Dict[str, Any]) -> bool:
    """Whether any row or core-function location uses cytoplasm.

    Lets the validator skip reading the UniProt record for most reviews.

    >>> mentions_cytoplasm({"core_functions": [{"locations": [{"id": "GO:0005737"}]}]})
    True
    >>> mentions_cytoplasm({"existing_annotations": [{"term": {"id": "GO:0005829"}}]})
    False
    """
    return any(_term_id(a) == CYTOPLASM for a in _annotations(data)) or any(
        CYTOPLASM in _location_ids(c) for c in _core_functions(data)
    )


def _row_advice(finding: CytoplasmFinding, ontology_checked: bool) -> str:
    """What to do instead, given what the review already asserts."""
    if finding.entailing:
        return (
            f"The review already asserts {', '.join(finding.entailing)}, which entails "
            "cytoplasm, so use TOO_GENERAL."
        )
    tail = (
        "Nothing the review asserts entails cytoplasm, so"
        if ontology_checked
        else "Otherwise"
    )
    return (
        "Use MODIFY if this row's own evidence resolves where in the cytoplasm the "
        "protein is (cytosol for diffuse staining or a high-speed supernatant; the "
        f"organelle or granule a marker identifies). {tail} use KEEP_AS_NON_CORE, and "
        "add a NEW row for a specific location only on evidence of its own."
    )


def _message(finding: CytoplasmFinding, ontology_checked: bool) -> tuple[str, str]:
    """Warning message and suggestion for a warned finding."""
    if finding.category == "EUK_CORE_LOCATION":
        return (
            "core_functions names GO:0005737 cytoplasm as a location: in a eukaryote "
            "cytoplasm includes the organelles, so it does not say where the activity "
            "happens",
            "Name the compartment where the activity is shown to happen (GO:0005829 "
            "cytosol, an organelle or its sub-compartment), or omit the location. See "
            "projects/CYTOPLASM.md.",
        )
    if finding.category == "EUK_NEW":
        return (
            "NEW GO:0005737 cytoplasm row on a eukaryotic protein: the term includes "
            "every organelle and adds almost no information",
            "Propose the specific location the evidence supports (GO:0005829 cytosol, "
            "an organelle, a granule), or drop the row. See projects/CYTOPLASM.md.",
        )
    return (
        "GO:0005737 cytoplasm is ACCEPTed (core) on a eukaryotic protein: cytoplasm "
        "includes every organelle, so it never names where a core activity happens",
        _row_advice(finding, ontology_checked) + " See projects/CYTOPLASM.md.",
    )


def check_cytoplasm_policy(
    data: Dict[str, Any],
    report: Any,
    yaml_file: Optional[Path],
    ancestors: Optional[Ancestors] = None,
) -> None:
    """Add a ``cytoplasm_policy`` warning for each warned finding in *data*."""
    from ai_gene_review.validation.validation_report import ValidationSeverity

    if yaml_file is None or not mentions_cytoplasm(data):
        return
    domain = domain_for_review(Path(yaml_file))
    for finding in find_cytoplasm_findings(data, domain, ancestors):
        if finding.category not in WARNED_CATEGORIES:
            continue
        message, suggestion = _message(finding, ancestors is not None)
        report.add_issue(
            ValidationSeverity.WARNING,
            message,
            path=finding.path,
            suggestion=suggestion,
            validation_category="BestPractices",
            check_type=CHECK_TYPE,
        )


def _load_yaml(path: Path) -> Dict[str, Any]:
    import yaml

    loader = getattr(yaml, "CSafeLoader", yaml.SafeLoader)
    with path.open() as fh:
        return yaml.load(fh, Loader=loader) or {}


AUDIT_HEADER = [
    "file",
    "domain",
    "category",
    "path",
    "action",
    "evidence_type",
    "original_reference_id",
    "entailing_terms",
]


def audit(
    paths: List[Path], ancestors: Optional[Ancestors]
) -> tuple[List[List[str]], Counter, Counter]:
    """Findings as TSV rows (header first), plus two tallies for the summary.

    The first tally counts every non-NOT cytoplasm row by ``(domain, action)``, the
    second counts findings by category.
    """
    rows: List[List[str]] = [AUDIT_HEADER]
    by_action: Counter = Counter()
    by_category: Counter = Counter()
    for path in paths:
        text = path.read_text(errors="replace")
        if CYTOPLASM not in text:
            continue
        data = _load_yaml(path)
        domain = domain_for_review(path) or "unknown"
        for annotation in _annotations(data):
            if _term_id(annotation) == CYTOPLASM and not annotation.get("negated"):
                by_action[(domain, _action(annotation) or "none")] += 1
        for f in find_cytoplasm_findings(data, domain, ancestors):
            by_category[f.category] += 1
            rows.append(
                [
                    str(path),
                    domain,
                    f.category,
                    f.path,
                    f.action,
                    f.evidence_type,
                    f.reference,
                    ",".join(f.entailing),
                ]
            )
    return rows, by_action, by_category


def main(argv: Optional[List[str]] = None) -> None:
    """Write the corpus-wide audit TSV (default ``reports/cytoplasm-policy.tsv``)."""
    import argparse
    import csv

    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "paths", nargs="*", type=Path, help="review YAMLs (default: all)"
    )
    parser.add_argument(
        "-o", "--output", type=Path, default=Path("reports/cytoplasm-policy.tsv")
    )
    parser.add_argument(
        "--no-ontology",
        action="store_true",
        help="skip the GO hierarchy (no TOO_GENERAL entailment check)",
    )
    args = parser.parse_args(argv)
    paths = args.paths or sorted(Path("genes").glob("*/*/*-ai-review.yaml"))
    ancestors: Optional[Ancestors] = None
    if not args.no_ontology:
        from ai_gene_review.validation.action_consistency import go_ancestors

        ancestors = go_ancestors().load()
    rows, by_action, by_category = audit(paths, ancestors)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", newline="") as fh:
        csv.writer(fh, delimiter="\t", lineterminator="\n").writerows(rows)

    print(f"cytoplasm (GO:0005737) rows in {len(paths)} reviews:", file=sys.stderr)
    domains = sorted({d for d, _ in by_action})
    actions = sorted(
        {a for _, a in by_action},
        key=lambda a: -sum(by_action[(d, a)] for d in domains),
    )
    print("  " + "\t".join(["action", *domains]), file=sys.stderr)
    for action in actions:
        cells = [str(by_action[(d, action)]) for d in domains]
        print("  " + "\t".join([action, *cells]), file=sys.stderr)
    print("findings by category:", file=sys.stderr)
    for category, count in sorted(by_category.items()):
        flag = " (warned)" if category in WARNED_CATEGORIES else ""
        print(f"  {category}\t{count}{flag}", file=sys.stderr)
    print(f"{len(rows) - 1} findings -> {args.output}", file=sys.stderr)


if __name__ == "__main__":
    main()
