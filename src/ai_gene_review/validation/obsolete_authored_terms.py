"""Warn when an author-supplied GO term id has been obsoleted.

Term-id validation is deliberately asymmetric (see CLAUDE.md): ids that come
from GOA are trusted, ids the reviewer writes are checked. The checks that
exist do not close the author-supplied case for *obsoletion*, though:

* ``existing_annotations[].term.id`` is not hard-validated at all, because GOA
  legitimately lags or leads the ontology version used for validation.
* The ``core_functions`` slots are bound to dynamic enums, which test branch
  **reachability**. An obsoleted term is still reachable from its branch root,
  so a retired id satisfies the enum and passes.

So an obsolete id written into ``proposed_replacement_terms``, a ``NEW`` row or
``core_functions`` passes validation today. Modules are already covered
(``module_validator.validate_terms`` errors on an obsolete grounding); gene
reviews were not.

This check is a **warning**, not an error, for two reasons. The signals
available are incomplete, so a clean result does not mean the id is live (see
below); and a corpus sweep found ~50 files with obsolete
``proposed_replacement_terms``, which an error would turn into red CI on every
unrelated PR until the sweep lands.

Detection combines two offline signals, and neither is sufficient alone. GO's
sqlite build prefixes a retired term's label with ``obsolete ``, which is the
only obsoletion signal the label resolver exposes -- but the snapshot lags: of
eight ids this check was written for, it carried the prefix for one. The
``GENE-goa.tsv`` files are refetched per gene and so independently, and they
carry the same prefix; across the whole corpus they caught three of the eight
(including one, ``GO:0098734``, that the snapshot missed). Their union is four
of eight. Only a live QuickGO query caught all eight, and QuickGO additionally
resolves a *merged* id silently -- returning a different ``id`` rather than an
obsoletion -- which no offline signal here can see at all.

The practical consequence, and the reason the message says which source fired:
**a hit is informative, a miss proves nothing.** This check narrows the gap; it
does not close it. Closing it needs a refreshed GO snapshot or a networked
term-status pass, which is tracked separately.
"""

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from typing import Any, Callable, Dict, Iterable, Iterator, List, Optional, Sequence, Tuple

import yaml

from ai_gene_review.validation.local_source_text import PROJECT_ROOT
from ai_gene_review.validation.module_validator import is_obsolete_label
from ai_gene_review.validation.validation_report import (
    ValidationReport,
    ValidationSeverity,
)

OBSOLETE_AUTHORED_CHECK = "obsolete_authored_term"

#: ``NTR`` is the schema's placeholder for a term that does not exist yet.
NTR = "NTR"

#: Core-function slots whose range is a single ``Term``.
SINGLE_CORE_SLOTS = (
    "molecular_function",
    "contributes_to_molecular_function",
    "in_complex",
)

#: Core-function slots whose range is a list of ``Term``.
MULTI_CORE_SLOTS = (
    "directly_involved_in",
    "locations",
    "anatomical_locations",
    "substrates",
)

#: ``(source, label)`` pairs for one curie, from every consulted source.
LabelLookup = Callable[[str], Iterable[Tuple[str, str]]]


@dataclass(frozen=True, order=True)
class AuthoredTerm:
    """A GO term id the reviewer wrote, and where they wrote it."""

    path: str
    curie: str
    label: Optional[str]


def _term(node: Any, path: str) -> Iterator[AuthoredTerm]:
    """Yield the GO term in a ``Term``-ranged slot, if it holds a checkable id.

    >>> list(_term({"id": "GO:1", "label": "x"}, "p"))
    [AuthoredTerm(path='p', curie='GO:1', label='x')]
    >>> list(_term({"id": "NTR", "label": "x"}, "p"))
    []
    >>> list(_term({"id": "CHEBI:1"}, "p"))
    []
    >>> list(_term("GO:1", "p"))
    []
    """
    if not isinstance(node, dict):
        return
    curie = node.get("id")
    if not isinstance(curie, str) or curie == NTR or not curie.startswith("GO:"):
        return
    label = node.get("label")
    yield AuthoredTerm(path=path, curie=curie, label=label if isinstance(label, str) else None)


def iter_authored_go_terms(data: Any) -> Iterator[AuthoredTerm]:
    """Yield every GO term id in the document that the reviewer authored.

    A reviewed GOA row's own ``term`` is *not* authored -- it came from GOA --
    except on a ``NEW`` row, which is an annotation the reviewer proposes.

    >>> doc = {"core_functions": [{"molecular_function": {"id": "GO:1", "label": "x"}}]}
    >>> [t.path for t in iter_authored_go_terms(doc)]
    ['core_functions[0].molecular_function']
    """
    if not isinstance(data, dict):
        return

    for i, annotation in enumerate(data.get("existing_annotations") or []):
        if not isinstance(annotation, dict):
            continue
        review = annotation.get("review")
        review = review if isinstance(review, dict) else {}
        if review.get("action") == "NEW":
            yield from _term(annotation.get("term"), f"existing_annotations[{i}].term")
        for j, replacement in enumerate(review.get("proposed_replacement_terms") or []):
            yield from _term(
                replacement,
                f"existing_annotations[{i}].review.proposed_replacement_terms[{j}]",
            )

    for i, core in enumerate(data.get("core_functions") or []):
        if not isinstance(core, dict):
            continue
        for slot in SINGLE_CORE_SLOTS:
            yield from _term(core.get(slot), f"core_functions[{i}].{slot}")
        for slot in MULTI_CORE_SLOTS:
            for j, item in enumerate(core.get(slot) or []):
                yield from _term(item, f"core_functions[{i}].{slot}[{j}]")

    for i, proposed in enumerate(data.get("proposed_new_terms") or []):
        if isinstance(proposed, dict):
            yield from _term(
                proposed.get("proposed_parent"), f"proposed_new_terms[{i}].proposed_parent"
            )


def goa_obsolete_labels(project_root: Path = PROJECT_ROOT) -> Dict[str, Tuple[str, str]]:
    """Map every GO id some ``GENE-goa.tsv`` marks obsolete to its label and source.

    GOA files are refetched per gene, so one gene's file can be months staler
    than another's. Reading the whole corpus is what makes the signal useful:
    ``CPT1C-goa.tsv`` carried ``GO:0098734``'s live label from a January fetch
    while four sibling genes' files carried the ``obsolete`` prefix from July.
    Where several files disagree, the most recently dated row wins.
    """
    found: Dict[str, Tuple[str, str, str]] = {}
    for goa in sorted((project_root / "genes").rglob("*-goa.tsv")):
        with goa.open(newline="") as handle:
            for row in csv.DictReader(handle, delimiter="\t"):
                curie = (row.get("GO TERM") or "").strip()
                label = (row.get("GO NAME") or "").strip()
                if not curie or not is_obsolete_label(label):
                    continue
                date = (row.get("DATE") or "").strip()
                source = goa.name
                previous = found.get(curie)
                if previous is None or date >= previous[2]:
                    found[curie] = (label, source, date)
    return {curie: (label, source) for curie, (label, source, _) in found.items()}


@lru_cache(maxsize=4)
def _cached_goa_obsolete_labels(project_root: Path) -> Dict[str, Tuple[str, str]]:
    """``goa_obsolete_labels`` memoised, so a batch run scans the corpus once."""
    return goa_obsolete_labels(project_root)


@lru_cache(maxsize=None)
def _snapshot_label(curie: str) -> Optional[str]:
    """The GO sqlite snapshot's primary label for ``curie``, or None.

    The snapshot is an external system whose build may be missing or
    unreadable; an unavailable snapshot means no signal, never a false alarm.
    """
    from ai_gene_review.validation.module_validator import _get_cached_adapter

    adapter = _get_cached_adapter("sqlite:obo:go")
    if adapter is None:
        return None
    try:  # external system: ontology query may fail transiently
        return adapter.label(curie)
    except Exception:  # noqa: BLE001 - external system
        return None


def build_label_lookup(
    project_root: Path = PROJECT_ROOT, use_ontology: bool = True
) -> LabelLookup:
    """A lookup over the offline signals: the corpus GOA labels and GO's snapshot."""
    goa = _cached_goa_obsolete_labels(project_root)

    def lookup(curie: str) -> List[Tuple[str, str]]:
        pairs: List[Tuple[str, str]] = []
        if curie in goa:
            goa_label, source = goa[curie]
            pairs.append((f"GOA file {source}", goa_label))
        if use_ontology:
            snapshot = _snapshot_label(curie)
            if snapshot is not None:
                pairs.append(("the GO snapshot", snapshot))
        return pairs

    return lookup


def check_obsolete_authored_terms(
    data: Any,
    report: ValidationReport,
    lookup: LabelLookup,
) -> None:
    """Warn on every author-supplied GO id an offline signal marks obsolete."""
    for term in iter_authored_go_terms(data):
        hits = [
            (source, label) for source, label in lookup(term.curie) if is_obsolete_label(label)
        ]
        if not hits:
            continue
        source, label = hits[0]
        report.add_issue(
            ValidationSeverity.WARNING,
            f"{term.curie} is obsolete according to {source} ('{label}'), but it is "
            f"written here as an author-supplied term",
            path=term.path,
            suggestion=(
                "Repoint to a live term that the evidence on this row supports -- check "
                "the obsoleted term's replaced_by and consider against the gene rather "
                "than taking it as given, since the mapping is automated"
            ),
            validation_category="BestPractices",
            check_type=OBSOLETE_AUTHORED_CHECK,
        )


def main(argv: Optional[Sequence[str]] = None) -> int:
    """Report obsolete author-supplied terms in the given files.

    Exits 0 even when hits are found: these are warnings, and the corpus has a
    known backlog. Use ``--strict`` to exit 1 instead, for a targeted sweep.
    """
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("files", nargs="+", type=Path)
    parser.add_argument(
        "--no-ontology",
        action="store_true",
        help="use only the corpus GOA labels, not the GO sqlite snapshot",
    )
    parser.add_argument(
        "--strict", action="store_true", help="exit 1 when any obsolete term is found"
    )
    args = parser.parse_args(argv)

    lookup = build_label_lookup(use_ontology=not args.no_ontology)
    found = False
    for path in args.files:
        report = ValidationReport(file_path=path, is_valid=True)
        check_obsolete_authored_terms(yaml.safe_load(path.read_text()), report, lookup)
        for issue in report.issues:
            found = True
            print(f"{path}: {issue.path}: {issue.message}")
    return int(found and args.strict)


if __name__ == "__main__":
    raise SystemExit(main())
