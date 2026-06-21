"""Evidence-subtraction reporting for gene reviews.

Given a set of gene reviews and a *filter* over the source of an annotation
(an ``original_reference_id`` such as ``GO_REF:0000033`` and/or an
``evidence_type`` such as ``IBA``), this module simulates **removing** the
matching annotations and reports what would be lost:

1. **Endorsed annotations that disappear.** Every annotation the reviewer
   endorsed (``ACCEPT`` / ``KEEP_AS_NON_CORE``) that matches the filter is
   reported. Each is classified as *uniquely lost* or *redundantly covered* --
   the latter meaning a surviving annotation still asserts the same term or a
   more specific descendant of it (closure-aware).

2. **``core_functions`` grounding after subtraction.** Each GO term used in a
   ``core_functions`` entry (``molecular_function``,
   ``contributes_to_molecular_function``, ``directly_involved_in``,
   ``locations``, ``in_complex``) is classified as:

   - ``RETAINED`` -- still grounded by a surviving endorsed annotation,
   - ``LOST`` -- grounded only by subtracted annotations (this is what the
     subtraction costs), or
   - ``UNSUPPORTED`` -- not grounded by any annotation at all (pure synthesis;
     unaffected by the subtraction).

Closure semantics
-----------------
A core-function term ``T`` (or an endorsed term being checked for redundancy)
is considered *grounded by* an annotation whose effective term is ``X`` when
``T`` is a reflexive ancestor of ``X`` -- i.e. ``X`` is ``T`` itself or a more
specific descendant. A *more general* annotation does not ground a specific
core-function claim. Closure is over ``is_a`` + ``part_of`` by default.

The engine takes an injectable ``ancestors`` function so it can be unit-tested
without loading an ontology; :func:`make_go_ancestor_fn` builds an OAK-backed
implementation for real use.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable, Iterable, Optional, Sequence, Union

import yaml

# Default closure predicates (CURIEs understood by OAK adapters).
IS_A = "rdfs:subClassOf"
PART_OF = "BFO:0000050"

#: A function returning the *reflexive* ancestor set of a term (includes the
#: term itself). Injected into :class:`SubtractionReporter` so it can be tested
#: without an ontology backend.
AncestorFn = Callable[[str], "set[str]"]

#: ``review.action`` values whose (effective) term still grounds a core
#: function / counts as surviving information after subtraction.
DEFAULT_SUPPORTING_ACTIONS = frozenset({"ACCEPT", "KEEP_AS_NON_CORE", "MODIFY", "NEW"})

#: ``review.action`` values reported as a *loss* when subtracted -- the curator
#: explicitly endorsed these terms for the gene.
DEFAULT_ENDORSED_ACTIONS = frozenset({"ACCEPT", "KEEP_AS_NON_CORE"})

#: ``core_functions`` slots that hold GO terms (and so participate in closure).
#: Single-valued slots and list-valued slots are both handled.
CORE_FUNCTION_TERM_SLOTS = (
    "molecular_function",
    "contributes_to_molecular_function",
    "directly_involved_in",
    "locations",
    "in_complex",
)


def make_go_ancestor_fn(
    adapter_string: str = "sqlite:obo:go",
    predicates: Sequence[str] = (IS_A, PART_OF),
) -> AncestorFn:
    """Build a cached, reflexive GO ancestor function backed by OAK.

    Args:
        adapter_string: OAK adapter selector (default downloads/uses the GO
            SQLite build, ``sqlite:obo:go``).
        predicates: Closure predicates to traverse (default ``is_a`` +
            ``part_of``).

    Returns:
        A function mapping a term id to its reflexive ancestor set.
    """
    from oaklib import get_adapter

    adapter = get_adapter(adapter_string)
    preds = list(predicates)
    cache: dict[str, set[str]] = {}

    def ancestors(term: str) -> set[str]:
        cached = cache.get(term)
        if cached is None:
            # Not all adapters accept ``reflexive``; fall back and add term.
            try:
                anc = set(adapter.ancestors(term, predicates=preds, reflexive=True))
            except TypeError:
                anc = set(adapter.ancestors(term, predicates=preds))
            anc.add(term)
            cache[term] = anc
            cached = anc
        return cached

    return ancestors


def _identity_ancestor_fn(term: str) -> set[str]:
    """Ancestor function with no closure -- a term is only its own ancestor."""
    return {term}


@dataclass(frozen=True)
class SubtractionFilter:
    """Selects which annotations are removed in a subtraction scenario.

    An annotation matches when its ``original_reference_id`` is in
    :attr:`reference_ids` and/or its ``evidence_type`` is in
    :attr:`evidence_codes`. When both sets are populated, :attr:`mode` controls
    whether *either* (``"any"``) or *both* (``"all"``) must match.

    Set :attr:`complement` to ``True`` to invert the selection -- subtract
    everything that does *not* match. This expresses a "keep only X" scenario:
    ``SubtractionFilter.create(evidence_codes=["IBA"], complement=True)``
    removes every non-IBA annotation, so the report shows what is lost if IBA
    were the only evidence used (i.e. where IBA is too conservative).
    """

    reference_ids: frozenset[str] = frozenset()
    evidence_codes: frozenset[str] = frozenset()
    mode: str = "any"
    complement: bool = False

    def __post_init__(self) -> None:
        if self.mode not in ("any", "all"):
            raise ValueError(f"mode must be 'any' or 'all', got {self.mode!r}")
        if not self.reference_ids and not self.evidence_codes:
            raise ValueError(
                "SubtractionFilter requires at least one reference id or evidence code"
            )

    @classmethod
    def create(
        cls,
        reference_ids: Iterable[str] = (),
        evidence_codes: Iterable[str] = (),
        mode: str = "any",
        complement: bool = False,
    ) -> "SubtractionFilter":
        """Convenience constructor accepting any iterables."""
        return cls(
            reference_ids=frozenset(reference_ids),
            evidence_codes=frozenset(evidence_codes),
            mode=mode,
            complement=complement,
        )

    def matches(self, annotation: dict) -> bool:
        """Return True if ``annotation`` (a raw dict) would be subtracted."""
        checks: list[bool] = []
        if self.reference_ids:
            checks.append(annotation.get("original_reference_id") in self.reference_ids)
        if self.evidence_codes:
            checks.append(annotation.get("evidence_type") in self.evidence_codes)
        base = bool(checks) and (all(checks) if self.mode == "all" else any(checks))
        return (not base) if self.complement else base

    def describe(self) -> str:
        """Human-readable one-line description of the filter."""
        parts = []
        if self.reference_ids:
            parts.append("ref in {" + ", ".join(sorted(self.reference_ids)) + "}")
        if self.evidence_codes:
            parts.append("evidence in {" + ", ".join(sorted(self.evidence_codes)) + "}")
        joiner = " AND " if self.mode == "all" else " OR "
        inner = joiner.join(parts)
        if self.complement:
            return f"everything except ({inner})"
        return inner


@dataclass(frozen=True)
class LostAnnotation:
    """An endorsed annotation that would be removed by the subtraction."""

    gene_symbol: Optional[str]
    protein_id: Optional[str]
    term_id: str
    term_label: Optional[str]
    evidence_type: Optional[str]
    reference_id: Optional[str]
    action: Optional[str]
    redundant: bool
    covered_by: tuple[str, ...]


@dataclass(frozen=True)
class CoreFunctionCoverage:
    """Coverage status of one GO term inside a ``core_functions`` entry."""

    gene_symbol: Optional[str]
    protein_id: Optional[str]
    core_function_index: int
    core_function_description: Optional[str]
    slot: str
    term_id: str
    term_label: Optional[str]
    status: str  # RETAINED | LOST | UNSUPPORTED
    retained_support: tuple[str, ...]
    subtracted_support: tuple[str, ...]


@dataclass
class GeneSubtractionResult:
    """Per-gene outcome of an evidence subtraction."""

    gene_symbol: Optional[str]
    protein_id: Optional[str]
    n_total_annotations: int
    n_subtracted: int
    lost_annotations: list[LostAnnotation] = field(default_factory=list)
    core_function_coverage: list[CoreFunctionCoverage] = field(default_factory=list)

    @property
    def n_uniquely_lost(self) -> int:
        """Endorsed annotations removed with no surviving covering annotation."""
        return sum(1 for la in self.lost_annotations if not la.redundant)

    @property
    def n_core_terms_lost(self) -> int:
        """core_functions GO terms grounded only by subtracted annotations."""
        return sum(1 for c in self.core_function_coverage if c.status == "LOST")


def _term_id(term: Optional[dict]) -> Optional[str]:
    if isinstance(term, dict):
        return term.get("id")
    return None


def _term_label(term: Optional[dict]) -> Optional[str]:
    if isinstance(term, dict):
        return term.get("label")
    return None


def _effective_term_ids(annotation: dict) -> list[str]:
    """Return the term id(s) an annotation effectively asserts.

    For ``MODIFY`` actions with ``proposed_replacement_terms`` the replacement
    terms are used; otherwise the original annotation term.
    """
    review = annotation.get("review") or {}
    if review.get("action") == "MODIFY":
        replacements = review.get("proposed_replacement_terms") or []
        ids = [t["id"] for t in replacements if isinstance(t, dict) and t.get("id")]
        if ids:
            return ids
    tid = _term_id(annotation.get("term"))
    return [tid] if tid else []


def _iter_core_function_terms(core_function: dict):
    """Yield ``(slot, term_id, term_label)`` for each GO term in an entry."""
    for slot in CORE_FUNCTION_TERM_SLOTS:
        value = core_function.get(slot)
        if value is None:
            continue
        terms = value if isinstance(value, list) else [value]
        for term in terms:
            tid = _term_id(term)
            if tid:
                yield slot, tid, _term_label(term)


@dataclass
class SubtractionReporter:
    """Computes evidence-subtraction results for gene reviews.

    Args:
        ancestors: Reflexive ancestor function (injected for testability). When
            omitted, closure is disabled (exact-term matching only).
        supporting_actions: ``review.action`` values whose effective term counts
            as grounding a core function / surviving information.
        endorsed_actions: ``review.action`` values reported as losses when
            subtracted.
    """

    ancestors: AncestorFn = _identity_ancestor_fn
    supporting_actions: frozenset[str] = DEFAULT_SUPPORTING_ACTIONS
    endorsed_actions: frozenset[str] = DEFAULT_ENDORSED_ACTIONS

    def _is_grounded(self, target: str, effective_ids: Iterable[str]) -> bool:
        """True if some effective term is ``target`` or a descendant of it."""
        return any(target in self.ancestors(x) for x in effective_ids)

    def analyze_review(
        self, review: dict, filt: SubtractionFilter
    ) -> GeneSubtractionResult:
        """Analyze a single parsed gene review dict against a filter."""
        gene_symbol = review.get("gene_symbol")
        protein_id = review.get("id")
        annotations = review.get("existing_annotations") or []

        # Partition supporting annotations (non-negated, endorsed/usable action)
        # into those that survive and those that are subtracted, carrying their
        # effective term ids for closure checks.
        retained_support: list[str] = []
        subtracted_support: list[str] = []
        n_subtracted = 0

        for ann in annotations:
            subtracted = filt.matches(ann)
            if subtracted:
                n_subtracted += 1
            if ann.get("negated"):
                continue
            review_obj = ann.get("review") or {}
            action = review_obj.get("action")
            if action in self.supporting_actions:
                eff = _effective_term_ids(ann)
                (subtracted_support if subtracted else retained_support).extend(eff)

        result = GeneSubtractionResult(
            gene_symbol=gene_symbol,
            protein_id=protein_id,
            n_total_annotations=len(annotations),
            n_subtracted=n_subtracted,
        )

        # 1. Endorsed annotations that would be removed.
        for ann in annotations:
            if not filt.matches(ann) or ann.get("negated"):
                continue
            review_obj = ann.get("review") or {}
            action = review_obj.get("action")
            if action not in self.endorsed_actions:
                continue
            term_id = _term_id(ann.get("term"))
            if not term_id:
                continue
            covered_by = tuple(
                sorted({x for x in retained_support if term_id in self.ancestors(x)})
            )
            result.lost_annotations.append(
                LostAnnotation(
                    gene_symbol=gene_symbol,
                    protein_id=protein_id,
                    term_id=term_id,
                    term_label=_term_label(ann.get("term")),
                    evidence_type=ann.get("evidence_type"),
                    reference_id=ann.get("original_reference_id"),
                    action=action,
                    redundant=bool(covered_by),
                    covered_by=covered_by,
                )
            )

        # 2. core_functions grounding after subtraction.
        for idx, cf in enumerate(review.get("core_functions") or []):
            description = cf.get("description")
            for slot, term_id, term_label in _iter_core_function_terms(cf):
                retained_hits = tuple(
                    sorted(
                        {x for x in retained_support if term_id in self.ancestors(x)}
                    )
                )
                subtracted_hits = tuple(
                    sorted(
                        {x for x in subtracted_support if term_id in self.ancestors(x)}
                    )
                )
                if retained_hits:
                    status = "RETAINED"
                elif subtracted_hits:
                    status = "LOST"
                else:
                    status = "UNSUPPORTED"
                result.core_function_coverage.append(
                    CoreFunctionCoverage(
                        gene_symbol=gene_symbol,
                        protein_id=protein_id,
                        core_function_index=idx,
                        core_function_description=description,
                        slot=slot,
                        term_id=term_id,
                        term_label=term_label,
                        status=status,
                        retained_support=retained_hits,
                        subtracted_support=subtracted_hits,
                    )
                )

        return result

    def analyze_file(
        self, path: Union[str, Path], filt: SubtractionFilter
    ) -> Optional[GeneSubtractionResult]:
        """Analyze a single gene review YAML file.

        Returns None if the file cannot be parsed into a mapping.
        """
        with open(path, "r") as fh:
            data = yaml.safe_load(fh)
        if not isinstance(data, dict):
            return None
        return self.analyze_review(data, filt)

    def analyze_files(
        self, paths: Iterable[Union[str, Path]], filt: SubtractionFilter
    ) -> list[GeneSubtractionResult]:
        """Analyze many gene review files, skipping unparseable ones."""
        results: list[GeneSubtractionResult] = []
        for path in paths:
            try:
                result = self.analyze_file(path, filt)
            except Exception as exc:  # interfacing with on-disk files
                print(f"Error processing {path}: {exc}")
                continue
            if result is not None:
                results.append(result)
        return results


def iter_review_files(
    paths: Iterable[Union[str, Path]],
    pattern: str = "**/*-ai-review.yaml",
) -> list[Path]:
    """Expand a mix of files and directories into review YAML files.

    Directories are globbed with ``pattern``; files are taken as-is.
    """
    files: list[Path] = []
    for raw in paths:
        p = Path(raw)
        if p.is_dir():
            files.extend(sorted(p.glob(pattern)))
        elif p.is_file():
            files.append(p)
    return files


# ----------------------------------------------------------------------------
# Rendering
# ----------------------------------------------------------------------------


def lost_annotation_rows(results: Iterable[GeneSubtractionResult]) -> list[dict]:
    """Flatten lost annotations across genes into TSV-ready row dicts."""
    rows: list[dict] = []
    for res in results:
        for la in res.lost_annotations:
            rows.append(
                {
                    "gene_symbol": la.gene_symbol,
                    "protein_id": la.protein_id,
                    "term_id": la.term_id,
                    "term_label": la.term_label,
                    "evidence_type": la.evidence_type,
                    "reference_id": la.reference_id,
                    "action": la.action,
                    "loss_status": "REDUNDANT" if la.redundant else "UNIQUE",
                    "covered_by": "; ".join(la.covered_by),
                }
            )
    return rows


def core_function_rows(results: Iterable[GeneSubtractionResult]) -> list[dict]:
    """Flatten core-function coverage across genes into TSV-ready row dicts."""
    rows: list[dict] = []
    for res in results:
        for cov in res.core_function_coverage:
            rows.append(
                {
                    "gene_symbol": cov.gene_symbol,
                    "protein_id": cov.protein_id,
                    "core_function_index": cov.core_function_index,
                    "slot": cov.slot,
                    "term_id": cov.term_id,
                    "term_label": cov.term_label,
                    "status": cov.status,
                    "retained_support": "; ".join(cov.retained_support),
                    "subtracted_support": "; ".join(cov.subtracted_support),
                    "core_function_description": cov.core_function_description,
                }
            )
    return rows


def _write_tsv(rows: list[dict], path: Path) -> None:
    import csv

    if not rows:
        path.write_text("")
        return
    fieldnames = list(rows[0].keys())
    with open(path, "w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames, delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)


def write_tsv_reports(
    results: list[GeneSubtractionResult], output_prefix: Union[str, Path]
) -> tuple[Path, Path]:
    """Write two TSVs (``*-lost-annotations.tsv``, ``*-core-functions.tsv``).

    Returns the two written paths.
    """
    prefix = Path(output_prefix)
    prefix.parent.mkdir(parents=True, exist_ok=True)
    lost_path = prefix.with_name(prefix.name + "-lost-annotations.tsv")
    cf_path = prefix.with_name(prefix.name + "-core-functions.tsv")
    _write_tsv(lost_annotation_rows(results), lost_path)
    _write_tsv(core_function_rows(results), cf_path)
    return lost_path, cf_path


def summarize(
    results: Sequence[GeneSubtractionResult], filt: SubtractionFilter
) -> dict:
    """Compute aggregate counts across all analyzed genes."""
    lost_rows = lost_annotation_rows(results)
    cf_rows = core_function_rows(results)
    status_counts: dict[str, int] = {"RETAINED": 0, "LOST": 0, "UNSUPPORTED": 0}
    for row in cf_rows:
        status_counts[row["status"]] = status_counts.get(row["status"], 0) + 1
    return {
        "filter": filt.describe(),
        "n_genes": len(results),
        "n_genes_affected": sum(1 for r in results if r.n_subtracted),
        "n_subtracted_annotations": sum(r.n_subtracted for r in results),
        "n_lost_endorsed": len(lost_rows),
        "n_lost_endorsed_unique": sum(
            1 for r in lost_rows if r["loss_status"] == "UNIQUE"
        ),
        "n_lost_endorsed_redundant": sum(
            1 for r in lost_rows if r["loss_status"] == "REDUNDANT"
        ),
        "n_core_function_terms": len(cf_rows),
        "core_function_status_counts": status_counts,
    }


def render_markdown(
    results: list[GeneSubtractionResult],
    filt: SubtractionFilter,
    max_detail_genes: Optional[int] = None,
) -> str:
    """Render a human-readable markdown report of a subtraction scenario."""
    summary = summarize(results, filt)
    sc = summary["core_function_status_counts"]
    lines: list[str] = []
    lines.append(f"# Evidence subtraction report: {summary['filter']}")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(
        f"- Genes analyzed: **{summary['n_genes']}** "
        f"({summary['n_genes_affected']} affected by the subtraction)"
    )
    lines.append(f"- Annotations subtracted: **{summary['n_subtracted_annotations']}**")
    lines.append(
        f"- Endorsed (ACCEPT/KEEP_AS_NON_CORE) annotations lost: "
        f"**{summary['n_lost_endorsed']}** "
        f"({summary['n_lost_endorsed_unique']} uniquely lost, "
        f"{summary['n_lost_endorsed_redundant']} still covered by a survivor)"
    )
    lines.append(
        f"- core_functions GO terms: **{summary['n_core_function_terms']}** "
        f"-> RETAINED {sc['RETAINED']}, LOST {sc['LOST']}, "
        f"UNSUPPORTED {sc['UNSUPPORTED']}"
    )
    lines.append("")

    # Per-gene detail, only for genes that lose something meaningful.
    affected = [r for r in results if r.n_uniquely_lost or r.n_core_terms_lost]
    affected.sort(key=lambda r: (r.n_core_terms_lost, r.n_uniquely_lost), reverse=True)
    if max_detail_genes is not None:
        affected = affected[:max_detail_genes]

    if affected:
        lines.append("## Genes with uniquely-lost information")
        lines.append("")
        for res in affected:
            header = res.gene_symbol or res.protein_id or "(unknown)"
            lines.append(f"### {header} ({res.protein_id})")
            lines.append("")
            unique_lost = [la for la in res.lost_annotations if not la.redundant]
            if unique_lost:
                lines.append("Uniquely lost endorsed annotations:")
                lines.append("")
                lines.append("| Term | Label | Evidence | Reference | Action |")
                lines.append("|------|-------|----------|-----------|--------|")
                for la in unique_lost:
                    lines.append(
                        f"| {la.term_id} | {la.term_label or ''} | "
                        f"{la.evidence_type or ''} | {la.reference_id or ''} | "
                        f"{la.action or ''} |"
                    )
                lines.append("")
            lost_cf = [c for c in res.core_function_coverage if c.status == "LOST"]
            if lost_cf:
                lines.append(
                    "core_functions terms grounded only by subtracted evidence:"
                )
                lines.append("")
                lines.append("| Slot | Term | Label | Grounded by (subtracted) |")
                lines.append("|------|------|-------|--------------------------|")
                for c in lost_cf:
                    lines.append(
                        f"| {c.slot} | {c.term_id} | {c.term_label or ''} | "
                        f"{'; '.join(c.subtracted_support)} |"
                    )
                lines.append("")

    return "\n".join(lines)
