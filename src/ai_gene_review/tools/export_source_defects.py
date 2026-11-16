#!/usr/bin/env python3
"""Collect structured source-database defects for upstream reporting.

Reviews record defects that live in a *source* record, not in this repository,
under ``source_defects`` (see ``docs/source_defects.md``). They appear in these
places:

* ``existing_annotations[].review.source_defects`` in gene reviews
  (``genes/*/*/*-ai-review.yaml``), where the defective record is the GOA/MOD
  annotation row described by the enclosing ``existing_annotations`` entry;
* ``references[].reference_review.source_defects`` in gene reviews, where the
  defect is in a cited source's own text (a MOD gene description, a UniProt
  FUNCTION comment);
* ``functional_isoforms[].source_defects`` in gene reviews, where the defect is in
  the source's record of an isoform (e.g. a literature isoform missing from the
  reviewed UniProt entry); the row's ``term_id`` carries the functional isoform id;
* ``activity_reviews[].source_defects`` in GO-CAM reviews
  (``gocams/*/*-review.yaml``), where it is the GO-CAM activity.

Four further document kinds *could* carry a defect, each reaching the slot only
through ``references[].reference_review``: ``ModuleReview`` (``modules/``),
``PredictionReview``, ``RuleReview`` and ``CuratedRule`` (``rules/``). None
currently does, so :func:`collect` does not glob them;
``test_the_schema_permits_source_defects_in_exactly_the_known_document_kinds``
and ``test_no_uncollected_document_kind_has_source_defects_to_lose`` fail if that
changes, rather than letting such a defect go unreported. Family reviews
(``interpro/panther/*/*-review.yaml``) cannot carry one at all: that schema is
standalone and its own ``Reference`` class has no ``reference_review``.

This module flattens them all into one row per defect and renders:

* ``reports/source-defects.tsv`` - one row per recorded instance, carrying the
  grouping and ranking columns so the data can be queried;
* ``reports/source-defects/<RESOURCE>.md`` - the open defects for one resource,
  the thing that is actually sent upstream;
* ``reports/source-defects/WORKLIST.md`` - every open defect once, worst first
  across all resources, so a maintainer can work the worst ones first.

The worklist groups identical instances (see :data:`GROUP_KEY_COLUMNS`) and
orders them by a small set of named, independently checkable reasons rather than
by a weighted score - see ``docs/source_defects.md``.

>>> row = _row(
...     source_path="genes/ARATH/X/X-ai-review.yaml",
...     context={"gene_symbol": "X", "subject_id": "UniProtKB:P1"},
...     defect={"defect_type": "WRONG_REFERENCE", "resource": "TAIR",
...             "asserted_value": "PMID:1", "confidence": "PROBABLE",
...             "explanation": "Mis-keyed."},
... )
>>> row["report_status"]
'NOT_REPORTED'
>>> row["resource"]
'TAIR'
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterator

from ruamel.yaml import YAML

COLUMNS = [
    "resource",
    "report_status",
    "defect_type",
    "confidence",
    "severity",
    "source_path",
    "gene_symbol",
    "subject_id",
    "record",
    "slot",
    "requested_change",
    "term_id",
    "term_label",
    "evidence_type",
    "original_reference_id",
    "qualifier",
    "asserted_value",
    "corrected_value",
    "corrected_label",
    "cause",
    "explanation",
    "supported_by",
    "report_url",
    "group_id",
    "group_rank",
    "group_size",
    "group_reasons",
    "group_severity",
]

DEFAULT_TSV = Path("reports/source-defects.tsv")
DEFAULT_REPORT_DIR = Path("reports/source-defects")
WORKLIST_NAME = "WORKLIST.md"

#: The fields that identify one upstream defect: who must change what, in which
#: field of which record, from what, to what. Everything else on a row is either
#: annotation context that varies across the instances of one fix (the gene, the
#: GO term, the evidence code) or a judgement about it (confidence, cause,
#: severity, explanation), which is aggregated across the group instead.
GROUP_KEY_COLUMNS = (
    "resource",
    "defect_type",
    "record",
    "slot",
    "asserted_value",
    "corrected_value",
    "requested_change",
)

#: Resources whose records are inherited rather than annotated one row at a time:
#: an InterPro2GO mapping or a PANTHER node association is wrong for every
#: protein that matches it, and a GOC defect is in a term, so the fix reaches
#: every annotation using it. GO_CENTRAL is deliberately absent: it is PAINT's
#: own IBD/IBA curation, not a pipeline (docs/source_defects.md, "Choosing a
#: resource"). A PAINT row that did over-propagate says so in its own `cause`,
#: which the cause limb below picks up.
PROPAGATING_RESOURCES = frozenset({"INTERPRO", "PANTHER", "GOC"})

#: Causes that say the defect spread past where its evidence holds, whatever the
#: resource: the fix is at the seed, node or mapping, not on the inherited rows.
PROPAGATING_CAUSES = frozenset({"OVER_PROPAGATION", "SCOPE_OVER_REACH"})

#: Cause values that identify no mechanism, so they neither support nor
#: contradict a propagation claim. `UNKNOWN` is "not identifiable at all";
#: `OTHER` is a mechanism that *was* identified and is not a spreading one, so it
#: counts against (docs/source_defects.md, "Choosing a cause").
UNIDENTIFIED_CAUSES = frozenset({"UNKNOWN"})

#: Defect types where the record asserts something false about a *different*
#: entity, or the opposite of the truth, rather than being imprecise about the
#: right one.
MISATTRIBUTING_DEFECT_TYPES = frozenset({"WRONG_GENE_PRODUCT", "MISSING_NEGATION"})

#: Weakest to strongest; a group takes the strongest confidence any instance
#: recorded, since one verified instance is enough to file as a correction.
CONFIDENCE_ORDER = ("SUSPECTED", "PROBABLE", "CONFIRMED")

#: Worst to least bad; a group takes the worst severity any instance recorded.
SEVERITY_ORDER = ("MISLEADING", "IMPRECISE", "COSMETIC")

#: The band a curator-set severity moves a defect into. MISLEADING sorts above
#: every unassessed defect and COSMETIC below every one; IMPRECISE shares the
#: default band, so recording it states that the consequence was assessed and is
#: ordinary without moving the defect.
SEVERITY_BANDS = {"MISLEADING": 0, "IMPRECISE": 1, "": 1, "COSMETIC": 2}

#: Statuses that take a defect out of the reports entirely (as in render_report).
CLOSED_STATUSES = frozenset({"FIXED", "DECLINED"})

#: Statuses meaning the report exists; such a defect needs chasing, not filing.
FILED_STATUSES = frozenset({"REPORTED", "ACKNOWLEDGED"})

#: Most to least advanced, for summarising a group's reporting state.
STATUS_ORDER = ("ACKNOWLEDGED", "REPORTED", "NOT_REPORTED")


def _load(path: Path) -> Any:
    """Load a YAML file, skipping files that do not mention source_defects."""
    text = path.read_text(encoding="utf-8")
    if "source_defects:" not in text:
        return None
    return YAML(typ="safe").load(text)


def _row(source_path: str, context: dict[str, Any], defect: dict[str, Any]) -> dict[str, str]:
    """Flatten one defect plus its record context into a TSV row."""
    row = {c: "" for c in COLUMNS}
    row.update({k: "" if v is None else str(v) for k, v in context.items()})
    for key in (
        "defect_type", "resource", "record", "slot", "requested_change",
        "asserted_value", "corrected_value",
        "corrected_label", "cause", "confidence", "severity", "explanation",
        "report_url",
    ):
        if defect.get(key) is not None:
            row[key] = " ".join(str(defect[key]).split())
    row["report_status"] = str(defect.get("report_status") or "NOT_REPORTED")
    row["supported_by"] = json.dumps(defect.get("supported_by") or [], ensure_ascii=False)
    row["source_path"] = source_path
    return row


def gene_review_rows(path: Path, root: Path) -> Iterator[dict[str, str]]:
    """Yield defect rows from a gene review's annotations, references and functional isoforms."""
    data = _load(path)
    if not data:
        return
    for ann in data.get("existing_annotations") or []:
        review = ann.get("review") or {}
        for defect in review.get("source_defects") or []:
            term = ann.get("term") or {}
            context = {
                "gene_symbol": data.get("gene_symbol", ""),
                "subject_id": f"UniProtKB:{data.get('id', '')}",
                "term_id": term.get("id", ""),
                "term_label": term.get("label", ""),
                "evidence_type": ann.get("evidence_type", ""),
                "original_reference_id": ann.get("original_reference_id", ""),
                "qualifier": ann.get("qualifier", ""),
            }
            yield _row(str(path.relative_to(root)), context, defect)
    for ref in data.get("references") or []:
        for defect in (ref.get("reference_review") or {}).get("source_defects") or []:
            context = {
                "gene_symbol": data.get("gene_symbol", ""),
                "subject_id": f"UniProtKB:{data.get('id', '')}",
                "original_reference_id": ref.get("id", ""),
                "term_label": ref.get("title", ""),
            }
            yield _row(str(path.relative_to(root)), context, defect)
    for isoform in data.get("functional_isoforms") or []:
        for defect in isoform.get("source_defects") or []:
            context = {
                "gene_symbol": data.get("gene_symbol", ""),
                "subject_id": f"UniProtKB:{data.get('id', '')}",
                "term_id": isoform.get("id", ""),
                "term_label": isoform.get("name", ""),
            }
            yield _row(str(path.relative_to(root)), context, defect)


def gocam_review_rows(path: Path, root: Path) -> Iterator[dict[str, str]]:
    """Yield defect rows from a GO-CAM review's activity reviews."""
    data = _load(path)
    if not data:
        return
    for act in data.get("activity_reviews") or []:
        for defect in act.get("source_defects") or []:
            context = {
                "subject_id": act.get("gene_product", ""),
                "term_id": act.get("molecular_function", ""),
            }
            row = _row(str(path.relative_to(root)), context, defect)
            if not row["record"]:
                row["record"] = act.get("activity_id", "")
            yield row


def collect(root: Path) -> list[dict[str, str]]:
    """Collect every source defect under ``root``, sorted for stable output."""
    rows: list[dict[str, str]] = []
    for path in sorted(root.glob("genes/*/*/*-ai-review.yaml")):
        rows.extend(gene_review_rows(path, root))
    for path in sorted(root.glob("gocams/*/*-review.yaml")):
        rows.extend(gocam_review_rows(path, root))
    rows.sort(key=lambda r: (r["resource"], r["source_path"], r["term_id"], r["asserted_value"]))
    return rows


@dataclass(frozen=True)
class Reason:
    """One named, independently checkable ground for a defect's rank.

    ``token`` is short and stable, so it can go in a TSV cell and be grepped for;
    ``because`` says why it is true of this particular defect, so a rank can be
    explained rather than asserted.
    """

    token: str
    because: str


@dataclass
class GroupedDefect:
    """One upstream defect, with every review instance that recorded it.

    A group is what gets filed: many instances of one qualifier convention
    problem are one ticket, not many. The instance count is a fact about this
    repository's reviewing, not about the resource.

    The committed reports confirm that grouping is right in one direction and
    cannot be made right in the other. Three ``GO:0004810`` instances on ``thiI``
    were filed as one upstream issue, which this key keeps together; two
    *different* defects on LCMT1 were filed as one issue too, which no key could
    predict. So the key errs towards splitting: a maintainer can bundle two items
    into one ticket, whereas a merge that hides a disagreement is not recoverable
    from the report.
    """

    key: tuple[str, ...]
    instances: list[dict[str, str]]

    def __getattr__(self, name: str) -> str:
        """Expose each key field (``resource``, ``slot``, ...) as an attribute."""
        if name in GROUP_KEY_COLUMNS:
            return self.key[GROUP_KEY_COLUMNS.index(name)]
        raise AttributeError(name)

    @property
    def id(self) -> str:
        """A stable id, a function of the key alone.

        >>> GroupedDefect(group_key({**{c: "" for c in COLUMNS}, "resource": "TAIR"}), []).id
        'SD-9e3bf8dce2'
        """
        digest = hashlib.sha256("\x1f".join(self.key).encode("utf-8")).hexdigest()
        return f"SD-{digest[:10]}"

    @property
    def count(self) -> int:
        """How many reviews recorded this defect."""
        return len(self.instances)

    @property
    def source_paths(self) -> tuple[str, ...]:
        """The reviews that recorded it, in path order."""
        return tuple(sorted({i["source_path"] for i in self.instances}))

    @property
    def confidence(self) -> str:
        """The strongest confidence any instance recorded."""
        return max((i["confidence"] for i in self.instances), key=_confidence_rank)

    @property
    def severity(self) -> str:
        """The worst curator-set severity any instance recorded, else ``""``."""
        recorded = [i["severity"] for i in self.instances if i["severity"]]
        return min(recorded, key=SEVERITY_ORDER.index) if recorded else ""

    @property
    def report_status(self) -> str:
        """The most advanced reporting status any instance recorded."""
        return min((i["report_status"] for i in self.instances), key=_status_rank)

    @property
    def report_urls(self) -> tuple[str, ...]:
        return tuple(sorted({i["report_url"] for i in self.instances if i["report_url"]}))

    @property
    def filed(self) -> bool:
        """True when every instance has been filed, so nothing is left to file."""
        return all(i["report_status"] in FILED_STATUSES for i in self.instances)

    @property
    def causes(self) -> tuple[str, ...]:
        """The mechanisms the instances named, if any."""
        return tuple(sorted({i["cause"] for i in self.instances if i["cause"]}))

    @property
    def subjects(self) -> tuple[str, ...]:
        """The gene products or models whose records carry this defect."""
        return tuple(sorted({i["subject_id"] for i in self.instances if i["subject_id"]}))

    @property
    def term_ids(self) -> tuple[str, ...]:
        """The annotations the instances were found on, where they name a term."""
        return tuple(sorted({i["term_id"] for i in self.instances if i["term_id"]}))

    @property
    def explanations(self) -> tuple[str, ...]:
        """The distinct explanations the instances wrote, in instance order."""
        seen: list[str] = []
        for instance in sorted(self.instances, key=lambda i: i["source_path"]):
            if instance["explanation"] and instance["explanation"] not in seen:
                seen.append(instance["explanation"])
        return tuple(seen)

    @property
    def propagates(self) -> bool:
        """One fix corrects every inheriting record, not one row."""
        return self.resource in PROPAGATING_RESOURCES or self._cause_says_it_spread()

    def _cause_says_it_spread(self) -> bool:
        """True when every mechanism the instances identified is a spreading one.

        Not "any instance named one": the largest group in the corpus is 55
        UniProt qualifier rows of which 5 say `SCOPE_OVER_REACH`, 25 say `OTHER`
        and 2 `PRACTICE_CHANGE`. Those are 55 separate GAF-row edits whose
        mechanism the reviews disagree about, so the group should not claim that
        one fix corrects them all. A threshold would be a coefficient in
        disguise; requiring the identified mechanisms to agree is a rule the enum
        already supports, since `UNKNOWN` records that no mechanism was
        identifiable while `OTHER` records one that was and is not propagation.
        """
        identified = set(self.causes) - UNIDENTIFIED_CAUSES
        return bool(identified) and identified <= PROPAGATING_CAUSES

    @property
    def misattributed(self) -> bool:
        """The record asserts something false about another entity, or the inverse."""
        return self.defect_type in MISATTRIBUTING_DEFECT_TYPES

    @property
    def confirmed(self) -> bool:
        """Verified against primary data, so it can be filed as a correction."""
        return self.confidence == "CONFIRMED"

    @property
    def reasons(self) -> tuple[Reason, ...]:
        """Why this defect ranks where it does, in the order the ranking applies.

        >>> rows = [{**{c: "" for c in COLUMNS}, "resource": "INTERPRO",
        ...          "defect_type": "WRONG_TERM", "confidence": "CONFIRMED",
        ...          "report_status": "NOT_REPORTED", "asserted_value": "GO:1",
        ...          "explanation": "e", "source_path": "p"}]
        >>> [r.token for r in group_defects(rows)[0].reasons]
        ['propagates', 'confirmed']
        """
        found: list[Reason] = []
        if self.propagates:
            found.append(Reason("propagates", self._propagation_ground()))
        if self.count > 1:
            found.append(
                Reason(
                    f"instances: {self.count}",
                    f"recorded independently by {self.count} reviews, so it is "
                    "systematic rather than a one-off",
                )
            )
        if self.misattributed:
            found.append(
                Reason(
                    "misattributed",
                    f"{self.defect_type}: the record asserts something false about "
                    "a different entity, or the opposite of the evidence, rather "
                    "than being imprecise about the right one",
                )
            )
        if self.confirmed:
            found.append(
                Reason(
                    "confirmed",
                    "at least one instance is CONFIRMED, so this can be filed as a "
                    "correction rather than a query (a tiebreaker, not a severity)",
                )
            )
        return tuple(found)

    def _propagation_ground(self) -> str:
        """Say which limb of the propagation test this defect satisfies."""
        grounds = []
        if self.resource in PROPAGATING_RESOURCES:
            grounds.append(
                f"{self.resource} records are inherited, so one fix corrects every "
                "record that matches"
            )
        if self._cause_says_it_spread():
            spreading = sorted(set(self.causes) - UNIDENTIFIED_CAUSES)
            grounds.append(
                f"cause {', '.join(spreading)}: every mechanism the instances "
                "identified says the evidence was spread past where it holds, so "
                "the fix is at the seed, node or mapping"
            )
        return "; ".join(grounds)

    @property
    def rank_key(self) -> tuple[Any, ...]:
        """The sort position: a curator band, then the named reasons, then the key.

        Lexicographic over independently-true facts, deliberately not a weighted
        score. Breadth first (``propagates``, then instance count), because a
        worklist orders by how many records one fix corrects; then kind of
        wrongness (``misattributed``); then certainty (``confirmed``), which
        decides how to file rather than how much it matters, so it only breaks
        ties. The full key last makes the order total.
        """
        return (
            SEVERITY_BANDS[self.severity],
            0 if self.propagates else 1,
            -self.count,
            0 if self.misattributed else 1,
            0 if self.confirmed else 1,
            self.key,
        )


def _confidence_rank(confidence: str) -> int:
    """Position in CONFIDENCE_ORDER, so ``max`` picks the strongest.

    >>> max(["SUSPECTED", "CONFIRMED", "PROBABLE"], key=_confidence_rank)
    'CONFIRMED'
    """
    return CONFIDENCE_ORDER.index(confidence) if confidence in CONFIDENCE_ORDER else -1


def _status_rank(status: str) -> int:
    """Position in STATUS_ORDER, so ``min`` picks the most advanced.

    >>> min(["NOT_REPORTED", "REPORTED"], key=_status_rank)
    'REPORTED'
    """
    return STATUS_ORDER.index(status) if status in STATUS_ORDER else len(STATUS_ORDER)


def group_key(row: dict[str, str]) -> tuple[str, ...]:
    """The grouping key of one exported row.

    >>> group_key({**{c: "" for c in COLUMNS}, "resource": "UNIPROT",
    ...            "defect_type": "WRONG_QUALIFIER", "slot": "Qualifier",
    ...            "asserted_value": "enables", "corrected_value": "contributes_to",
    ...            "requested_change": "REPOINT"})
    ('UNIPROT', 'WRONG_QUALIFIER', '', 'Qualifier', 'enables', 'contributes_to', 'REPOINT')
    """
    return tuple(row[column] for column in GROUP_KEY_COLUMNS)


def group_defects(rows: list[dict[str, str]]) -> list[GroupedDefect]:
    """Group rows into one item per upstream defect, in key order.

    Instances that are ``FIXED`` or ``DECLINED`` are dropped first, as they are
    from the per-resource reports, so a group's ``count`` is the work that
    remains; a group all of whose instances are closed disappears.

    >>> base = {**{c: "" for c in COLUMNS}, "resource": "TAIR",
    ...         "defect_type": "WRONG_TERM", "confidence": "PROBABLE",
    ...         "report_status": "NOT_REPORTED", "asserted_value": "GO:1",
    ...         "explanation": "e"}
    >>> rows = [{**base, "source_path": "a", "term_id": "GO:7"},
    ...         {**base, "source_path": "b", "term_id": "GO:8"},
    ...         {**base, "source_path": "c", "asserted_value": "GO:2"}]
    >>> [(g.asserted_value, g.count) for g in group_defects(rows)]
    [('GO:1', 2), ('GO:2', 1)]
    """
    grouped: dict[tuple[str, ...], list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        if row["report_status"] not in CLOSED_STATUSES:
            grouped[group_key(row)].append(row)
    return [GroupedDefect(key, grouped[key]) for key in sorted(grouped)]


def rank(groups: list[GroupedDefect]) -> list[GroupedDefect]:
    """Order grouped defects worst first; see :attr:`GroupedDefect.rank_key`."""
    return sorted(groups, key=lambda group: group.rank_key)


def _describe_change(r: dict[str, str]) -> str:
    """Describe the requested change in one line.

    >>> base = {"asserted_value": "A:1", "corrected_value": "", "corrected_label": "",
    ...         "slot": "has_input", "requested_change": "DELETE_VALUE"}
    >>> _describe_change(base)
    'remove A:1 from has_input'
    >>> _describe_change({**base, "requested_change": "", "corrected_value": "A:2"})
    'A:1 → A:2'
    >>> _describe_change({**base, "requested_change": "ADD", "slot": "",
    ...                   "corrected_value": "RefSeq:NP_1.1"})
    'add RefSeq:NP_1.1 to A:1'
    """
    asserted, corrected = r["asserted_value"], r["corrected_value"]
    label = f" ({r['corrected_label']})" if r["corrected_label"] else ""
    action = r["requested_change"]
    if action == "DELETE_VALUE":
        where = f" from {r['slot']}" if r["slot"] else ""
        return f"remove {asserted}{where}"
    if action == "DELETE_ROW":
        return f"delete the record asserting {asserted}"
    if action == "ADD":
        where = f" ({r['slot']})" if r["slot"] else ""
        if not corrected:
            return f"add the content described in the explanation to {asserted}{where}"
        return f"add {corrected}{label} to {asserted}{where}"
    if action == "CHECK" and r.get("defect_type", "").endswith("_STATEMENT"):
        where = f" in {r['slot']}" if r["slot"] else ""
        return f'revise "{asserted}"{where} (see explanation)'
    if action == "CHECK":
        return f"check {asserted} (alternatives in the explanation)"
    if corrected:
        return f"{asserted} → {corrected}{label}"
    return f"{asserted} (no replacement value; see explanation)"


def render_report(resource: str, rows: list[dict[str, str]]) -> str:
    """Render a Markdown report of open defects for one resource.

    Only rows that have not been fixed or declined are included.

    >>> md = render_report("TAIR", [{**{c: "" for c in COLUMNS}, "resource": "TAIR",
    ...     "report_status": "NOT_REPORTED", "defect_type": "WRONG_GENE_PRODUCT",
    ...     "confidence": "CONFIRMED", "asserted_value": "AGI_LocusCode:AT1G1",
    ...     "corrected_value": "AGI_LocusCode:AT1G2", "explanation": "Swap.",
    ...     "supported_by": "[]"}])
    >>> "AGI_LocusCode:AT1G1" in md and "→ AGI_LocusCode:AT1G2" in md
    True
    """
    open_rows = [r for r in rows if r["report_status"] not in ("FIXED", "DECLINED")]
    lines = [f"# Source-record defects for {resource}", ""]
    lines.append(
        f"{len(open_rows)} open defect(s), generated from `source_defects` blocks "
        "in this repository's reviews. Do not edit by hand."
    )
    for i, r in enumerate(open_rows, 1):
        target = r["record"] or (
            f"{r['subject_id']} {r['qualifier']} {r['term_id']} {r['term_label']} "
            f"({r['evidence_type']}, {r['original_reference_id']})"
        ).strip()
        lines += [
            "",
            f"## {i}. {r['defect_type']} ({r['confidence']}, {r['report_status']})",
            "",
            f"- **Record:** {target}",
        ]
        if r["record"] and r["subject_id"]:
            lines.append(f"- **Subject:** {r['subject_id']}")
        if r["slot"]:
            lines.append(f"- **Field:** {r['slot']}")
        lines.append(f"- **Change:** {_describe_change(r)}")
        if r["cause"]:
            lines.append(f"- **Likely cause:** {r['cause']}")
        lines.append(f"- **Recorded in:** `{r['source_path']}`")
        lines += ["", r["explanation"]]
        for ev in json.loads(r["supported_by"] or "[]"):
            text = " ".join(str(ev.get("supporting_text") or "").split())
            if text:
                lines += ["", f"> {text}", f"> — {ev.get('reference_id', '')}"]
            else:
                lines += ["", f"- **Evidence reference:** {ev.get('reference_id', '')}"]
    return "\n".join(lines) + "\n"


RANKING_NOTE = """\
Ordering, applied in this order and never as a weighted score, so every item can
say why it ranks where it does:

1. a **curator-set `severity`**, where one is recorded: `MISLEADING` above every
   unassessed defect, `COSMETIC` below every one. `IMPRECISE` is the default
   band, so it records an assessment without moving the defect.
2. **`propagates`** - one fix corrects every record that inherits it.
3. **`instances: N`**, descending - how many reviews recorded the same defect.
4. **`misattributed`** - the record asserts something false about a different
   entity, or the opposite of the evidence.
5. **`confirmed`** - a tiebreaker only. Certainty decides how to file a defect,
   not how much it matters; that is what `severity` is for.
6. the grouping key, so the order is total and the file is stable between runs.
"""


def _render_group(group: GroupedDefect, position: int) -> list[str]:
    """Render one grouped defect as the worklist's Markdown block."""
    representative = min(group.instances, key=lambda i: i["source_path"])
    lines = [
        "",
        f"## {position}. {group.resource} - {group.defect_type} ({group.id})",
        "",
        f"- **Change:** {_describe_change(representative)}",
    ]
    if group.record:
        lines.append(f"- **Record:** {group.record}")
    if group.slot:
        lines.append(f"- **Field:** {group.slot}")
    lines.append(f"- **Instances:** {group.count}")
    if len(group.subjects) > 1 or len(group.term_ids) > 1:
        # A GAF-row defect has no `record` of its own (the enclosing annotation
        # identifies it), so a group of them keyed on a generic asserted_value --
        # a qualifier, an evidence code -- is a class of row-level asks rather
        # than one upstream edit. Say what it spans so the reader can tell which.
        spans = []
        if len(group.subjects) > 1:
            spans.append(f"{len(group.subjects)} gene products")
        if len(group.term_ids) > 1:
            spans.append(f"{len(group.term_ids)} annotated terms")
        lines.append(f"- **Spans:** {' and '.join(spans)}")
    lines.append(
        "- **Severity:** "
        + (f"{group.severity} (curator-set)" if group.severity else "not assessed")
    )
    lines.append(f"- **Confidence:** {group.confidence}")
    if group.causes:
        lines.append(f"- **Likely cause:** {', '.join(group.causes)}")
    if group.report_status != "NOT_REPORTED":
        filed = f"- **Reported:** {group.report_status}"
        if group.report_urls:
            filed += " " + " ".join(group.report_urls)
        lines.append(filed)
    lines += ["", "**Why it ranks here:**", ""]
    lines += [f"- `{reason.token}` - {reason.because}" for reason in group.reasons] or [
        "- nothing distinguishes it: a single unconfirmed, non-propagating defect."
    ]
    lines += ["", group.explanations[0] if group.explanations else ""]
    if len(group.explanations) > 1:
        lines += [
            "",
            f"The instances recorded {len(group.explanations)} distinct explanations; "
            "the one above is from the first review listed below.",
        ]
    lines += ["", "**Recorded in:**", ""]
    for instance in sorted(
        group.instances,
        key=lambda i: (i["source_path"], i["term_id"], i["original_reference_id"]),
    ):
        evidence = ", ".join(
            part for part in (instance["evidence_type"], instance["original_reference_id"]) if part
        )
        context = " ".join(
            part
            for part in (
                instance["gene_symbol"],
                instance["term_id"],
                instance["term_label"],
                f"({evidence})" if evidence else "",
            )
            if part
        )
        lines.append(f"- `{instance['source_path']}`" + (f" - {context}" if context else ""))
    return lines


def render_worklist(groups: list[GroupedDefect]) -> str:
    """Render the cross-resource worklist, worst first.

    ``groups`` is expected in ranked order (:func:`rank`). Defects every instance
    of which has already been filed go into a trailing section: they need
    chasing, not filing, so they do not dilute the queue.

    >>> rows = [{**{c: "" for c in COLUMNS}, "resource": "INTERPRO",
    ...          "defect_type": "WRONG_TERM", "confidence": "PROBABLE",
    ...          "report_status": "NOT_REPORTED", "asserted_value": "GO:1",
    ...          "explanation": "Mapped term names another reaction.",
    ...          "source_path": "genes/ARATH/A/A-ai-review.yaml", "supported_by": "[]"}]
    >>> print(render_worklist(rank(group_defects(rows))).splitlines()[0])
    # Source-record defect worklist
    """
    queue = [g for g in groups if not g.filed]
    already_filed = [g for g in groups if g.filed]
    resources = len({g.resource for g in groups})
    instances = sum(g.count for g in groups)
    lines = [
        "# Source-record defect worklist",
        "",
        f"{len(queue)} defect(s) still to file, from {instances} recorded instance(s) "
        f"across {resources} resource(s), worst first. Generated from the "
        "`source_defects` blocks in this repository's reviews by "
        "`just export-source-defects`; do not edit by hand.",
        "",
        "Identical instances are grouped into one item per upstream defect, keyed on "
        + ", ".join(f"`{column}`" for column in GROUP_KEY_COLUMNS)
        + ". An item is what gets filed: many instances of one convention problem are "
        "one ticket. `FIXED` and `DECLINED` instances are excluded, as they are from "
        "the per-resource reports.",
        "",
        RANKING_NOTE,
    ]
    for position, group in enumerate(queue, 1):
        lines += _render_group(group, position)
    if already_filed:
        lines += [
            "",
            "# Already filed",
            "",
            f"{len(already_filed)} defect(s) whose every instance has been reported "
            "upstream and is not yet fixed or declined. These need chasing, not "
            "filing. Same ordering.",
        ]
        for position, group in enumerate(already_filed, 1):
            lines += _render_group(group, position)
    return "\n".join(lines) + "\n"


def write_outputs(root: Path, tsv: Path, report_dir: Path) -> list[dict[str, str]]:
    """Write the TSV, one Markdown report per resource, and the worklist.

    Returns the rows, each stamped with its grouping and ranking columns. A row
    whose group is closed (every instance ``FIXED`` or ``DECLINED``) still gets a
    ``group_id``, so the TSV stays joinable, but no rank.
    """
    rows = collect(root)
    ranked = rank(group_defects(rows))
    positions = {group.key: index for index, group in enumerate(ranked, 1)}
    by_key = {group.key: group for group in ranked}
    for row in rows:
        key = group_key(row)
        row["group_id"] = GroupedDefect(key, []).id
        group = by_key.get(key)
        if group is None:
            continue
        row["group_rank"] = str(positions[key])
        row["group_size"] = str(group.count)
        row["group_reasons"] = "; ".join(reason.token for reason in group.reasons)
        row["group_severity"] = group.severity
    tsv.parent.mkdir(parents=True, exist_ok=True)
    with tsv.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=COLUMNS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    report_dir.mkdir(parents=True, exist_ok=True)
    for resource in sorted({r["resource"] for r in rows}):
        subset = [r for r in rows if r["resource"] == resource]
        (report_dir / f"{resource}.md").write_text(render_report(resource, subset), encoding="utf-8")
    (report_dir / WORKLIST_NAME).write_text(render_worklist(ranked), encoding="utf-8")
    return rows


def main() -> None:
    """Command-line entry point."""
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--tsv", type=Path, default=DEFAULT_TSV)
    parser.add_argument("--report-dir", type=Path, default=DEFAULT_REPORT_DIR)
    args = parser.parse_args()
    rows = write_outputs(args.root, args.tsv, args.report_dir)
    groups = rank(group_defects(rows))
    queue = [g for g in groups if not g.filed]
    by_res: dict[str, int] = {}
    for r in rows:
        by_res[r["resource"]] = by_res.get(r["resource"], 0) + 1
    print(f"{len(rows)} source defect(s) -> {args.tsv}; reports in {args.report_dir}: {by_res}")
    print(
        f"{len(groups)} distinct defect(s) after grouping, {len(queue)} still to file "
        f"-> {args.report_dir / WORKLIST_NAME}"
    )
    for position, group in enumerate(queue[:10], 1):
        tokens = ", ".join(reason.token for reason in group.reasons) or "no distinguishing reason"
        print(f"  {position}. {group.resource} {group.defect_type} {group.asserted_value} [{tokens}]")


if __name__ == "__main__":
    main()
