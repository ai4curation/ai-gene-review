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
below); and the corpus already carries a backlog an error would turn into red
CI on every unrelated PR until a sweep lands. The audit at introduction found
87 hits in 44 of 12,281 reviews -- 49 of them in ``proposed_replacement_terms``
and 29 in ``core_functions.directly_involved_in``.

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


@dataclass(frozen=True)
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
            # A NEW row's extensions are written by the reviewer along with the
            # row. On any other row they came from GOA with the annotation, so
            # they are machine-sourced and trusted, like the row's own term.
            #
            # This slot is walked for correctness, not because it currently
            # yields anything: of the 16 extension terms on NEW rows in the
            # corpus, NONE is a GO id (14 UniProtKB via RO:0002233 has input,
            # one UBERON, one CL), so every one is skipped by the GO prefix
            # filter before obsoletion is ever consulted. Its empty result is
            # therefore a fact about prefixes, not evidence that the terms
            # there are live. GO extensions legitimately take GO terms
            # (occurs_in, part_of), so the slot can start mattering at any time.
            for j, extension in enumerate(annotation.get("extensions") or []):
                if isinstance(extension, dict):
                    yield from _term(
                        extension.get("term"),
                        f"existing_annotations[{i}].extensions[{j}].term",
                    )
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

    for i, isoform in enumerate(data.get("functional_isoforms") or []):
        if not isinstance(isoform, dict):
            continue
        for j, item in enumerate(isoform.get("isoform_specific_terms") or []):
            yield from _term(
                item, f"functional_isoforms[{i}].isoform_specific_terms[{j}]"
            )

    # Deliberately NOT walked: proposed_ontology_changes[].about_node,
    # .has_direct_replacement, .has_nondirect_replacement and .subject. They are
    # author-supplied and Term-ranged, so they look like candidates, but naming a
    # retired term is exactly their purpose -- walking them would flag every
    # correctly recorded obsoletion.


def goa_obsolete_labels(project_root: Path = PROJECT_ROOT) -> Dict[str, Tuple[str, str]]:
    """Map every GO id some ``GENE-goa.tsv`` marks obsolete to its label and source.

    GOA files are refetched per gene, so one gene's file can be months staler
    than another's. Reading the whole corpus is what makes the signal useful:
    ``CPT1C-goa.tsv`` carried ``GO:0098734``'s live label from a January fetch
    while four sibling genes' files carried the ``obsolete`` prefix from July.

    That independence is real where several genes' files agree:
    ``GO:0008379`` carries the ``obsolete `` prefix in 14 different genes' GOA
    files, which is 14 separate fetches reaching the same answer.

    But a single prefixed row is enough on its own, and a majority of
    unprefixed rows means nothing. The starkest case when the check was written
    was ``GO:0005615``: 218 rows across 88 files carried it as ``extracellular
    space``, against six rows that all sit in **one** file
    (``genes/human/ANG/ANG-goa.tsv``) carrying ``obsolete extracellular
    space``. That one file was right -- QuickGO confirms the obsoletion -- so
    the rule is not a vote. A stale file can miss an obsoletion; it cannot
    invent one, short of GO reinstating a term it had retired.

    Files are read in sorted order and the first prefixed row names the source,
    so the message is deterministic. The row's own ``DATE`` is the date of the
    *annotation*, not of the fetch, so it says nothing about which file is
    fresher and is not consulted.

    One source is recorded per curie, by construction: the return type holds a
    single ``(label, source)`` and the corroboration count is not surfaced. So
    the row-versus-file distinction above cannot be read back out of this
    index -- it governs how its output should be *argued from*, not what the
    output contains.

    The source is a repository-relative path, not a basename: gene directory
    names repeat across organisms (``genes/human/ACO2`` and ``genes/yeast/ACO2``
    both hold an ``ACO2-goa.tsv``), and the citation is only useful if the
    reader can find the file it names.
    """
    found: Dict[str, Tuple[str, str]] = {}
    genes = project_root / "genes"
    for goa in sorted(genes.rglob("*-goa.tsv")):
        source = goa.relative_to(project_root).as_posix()
        with goa.open(newline="") as handle:
            for row in csv.DictReader(handle, delimiter="\t"):
                curie = (row.get("GO TERM") or "").strip()
                label = (row.get("GO NAME") or "").strip()
                if not curie or curie in found or not is_obsolete_label(label):
                    continue
                found[curie] = (label, source)
    return found


@lru_cache(maxsize=4)
def _cached_goa_obsolete_labels(project_root: Path) -> Dict[str, Tuple[str, str]]:
    """``goa_obsolete_labels`` memoised, so a batch run scans the corpus once.

    The key is the *resolved* path. Callers reach this from two directions --
    ``local_source_text.PROJECT_ROOT`` is already resolved while
    ``validator.get_project_root()`` is not -- and under a symlinked checkout
    the two spellings would otherwise each pay for their own corpus scan.
    """
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
    project_root: Path = PROJECT_ROOT,
    use_ontology: bool = True,
    goa_index_loader: Callable[[Path], Dict[str, Tuple[str, str]]] = _cached_goa_obsolete_labels,
) -> LabelLookup:
    """A lookup over the offline signals: the corpus GOA labels and GO's snapshot.

    Building the lookup is free: the corpus scan is deferred until a term is
    actually looked up, because most reviews reach this with no author-supplied
    GO id at all and should not pay for the index. ``goa_index_loader`` is
    injectable for testing.
    """
    resolved = project_root.resolve()
    goa: Optional[Dict[str, Tuple[str, str]]] = None

    def lookup(curie: str) -> List[Tuple[str, str]]:
        nonlocal goa
        if goa is None:
            goa = goa_index_loader(resolved)
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
            details={
                "term_id": term.curie,
                "written_label": term.label,
                "detected_label": label,
                "detected_by": source,
            },
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
