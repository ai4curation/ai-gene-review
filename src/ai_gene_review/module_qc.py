#!/usr/bin/env python
"""Derived quality-control statistics for module documents.

This module computes the derived stats surfaced on rendered module pages:

1. ``run_data_qc`` -- LinkML recommended-field compliance (via ``linkml-data-qc``)
2. ``leaf_nodes_missing_representatives`` -- terminal nodes that do not ground to
   any concrete protein (a "representative member")
3. ``conformance_violations`` -- for every node declaring ``conforms_to`` a
   template motif, whether the bundle's tiers and connection topology match it
4. ``module_gene_review_summary`` -- for every ``UniProtKB`` grounding in a module,
   whether the gene has a review, whether that review is complete, and whether it
   has deep research
5. ``module_deep_research`` -- whether the module document as a whole has an
   associated deep-research report

The functions are deliberately pure (apart from the filesystem-scanning helpers)
so they can be unit-tested directly against the YAML documents in ``modules/``.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any, Callable, Optional

import yaml

DEFAULT_SCHEMA_PATH = Path(__file__).parent / "schema" / "gene_review.yaml"

# Repository modules directory, used to resolve conformance `template` references.
DEFAULT_MODULES_DIR = Path("modules")

# A predicate (child_curie, parent_curie) -> bool answering "is child a subclass
# of parent?". Conformance tier matching uses it to accept a more specific term
# than the template's. Default is identity (exact-term) matching only.
SubclassPredicate = Callable[[str, str], bool]

# Selector types whose participant can ground to a concrete protein.
_GROUNDED_TERM_PREFIXES = ("UniProtKB:",)

# Action values that mean an annotation has not actually been adjudicated yet.
_UNREVIEWED_ACTIONS = {"PENDING", "UNDECIDED", "", None}


def as_list(value: Any) -> list[Any]:
    """Return a value as a list, treating null and missing values as empty.

    >>> as_list(None)
    []
    >>> as_list([1, 2])
    [1, 2]
    >>> as_list("x")
    ['x']
    """
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def base_accession(curie_or_id: Any) -> Optional[str]:
    """Return the bare UniProt accession for a curie or id, dropping isoform suffix.

    >>> base_accession("UniProtKB:Q9NPJ1")
    'Q9NPJ1'
    >>> base_accession("UniProtKB:P19544-1")
    'P19544'
    >>> base_accession("Q9NPJ1")
    'Q9NPJ1'
    >>> base_accession(None) is None
    True
    """
    if not curie_or_id:
        return None
    text = str(curie_or_id)
    if ":" in text:
        text = text.split(":", 1)[1]
    # Drop a UniProt isoform suffix (e.g. P19544-1 -> P19544).
    return text.split("-", 1)[0] or None


# ---------------------------------------------------------------------------
# Module tree traversal
# ---------------------------------------------------------------------------


def iter_nodes(data: dict[str, Any]) -> list[dict[str, Any]]:
    """Return every module node, including the root and all nested descendants.

    Nodes are reachable via ``parts[].node`` and ``variant_sets[].variants[]``.
    """
    nodes: list[dict[str, Any]] = []

    def walk(node: Any) -> None:
        if not isinstance(node, dict):
            return
        nodes.append(node)
        for part in as_list(node.get("parts")):
            if isinstance(part, dict):
                walk(part.get("node"))
        for variant_set in as_list(node.get("variant_sets")):
            if isinstance(variant_set, dict):
                for variant in as_list(variant_set.get("variants")):
                    walk(variant)

    walk(data.get("module"))
    return nodes


def is_leaf_node(node: dict[str, Any]) -> bool:
    """Return True when a node has no child parts and no variant sets.

    >>> is_leaf_node({"id": "a"})
    True
    >>> is_leaf_node({"id": "a", "parts": [{"node": {"id": "b"}}]})
    False
    """
    return not as_list(node.get("parts")) and not as_list(node.get("variant_sets"))


def _selector_representative_groundings(selector: Any) -> list[dict[str, Any]]:
    """Return concrete protein groundings (representative members) for a selector.

    A grounding is a concrete protein example: a ``gene``/``gene_product`` carrying
    a ``UniProtKB`` term, a ``protein_complex`` active unit that resolves the same
    way, or a ``family``'s ``representative_members``. Abstract selectors
    (``FAMILY`` with no representatives, ``ANY_WITH_FUNCTION``, etc.) return [].
    """
    if not isinstance(selector, dict):
        return []

    groundings: list[dict[str, Any]] = []

    def add_descriptor(descriptor: Any) -> None:
        if not isinstance(descriptor, dict):
            return
        term = descriptor.get("term")
        term_id = term.get("id") if isinstance(term, dict) else None
        label = (
            descriptor.get("preferred_term")
            or (term.get("label") if isinstance(term, dict) else None)
            or term_id
        )
        groundings.append({"id": term_id, "label": label})

    # Concrete gene / gene product participants.
    for slot in ("gene", "gene_product"):
        descriptor = selector.get(slot)
        if isinstance(descriptor, dict):
            add_descriptor(descriptor)

    # Protein complex: drill into active units.
    complex_descriptor = selector.get("protein_complex")
    if isinstance(complex_descriptor, dict):
        for unit in as_list(complex_descriptor.get("active_units")):
            if isinstance(unit, dict):
                groundings.extend(
                    _selector_representative_groundings(unit.get("participant"))
                )

    # Family: representative members are the concrete examples.
    family = selector.get("family")
    if isinstance(family, dict):
        for member in as_list(family.get("representative_members")):
            add_descriptor(member)

    return groundings


def node_representative_groundings(node: dict[str, Any]) -> list[dict[str, Any]]:
    """Return all concrete protein groundings declared by a node's annotons."""
    groundings: list[dict[str, Any]] = []
    for annoton in as_list(node.get("annotons")):
        if isinstance(annoton, dict):
            groundings.extend(
                _selector_representative_groundings(annoton.get("participant"))
            )
    return groundings


def leaf_nodes_missing_representatives(
    data: dict[str, Any],
) -> list[dict[str, Any]]:
    """Return leaf nodes that do not ground to any representative protein member.

    A leaf node (no parts, no variant sets) is flagged when none of its annotons'
    participants resolve to a concrete protein -- e.g. abstract ``FAMILY`` or
    ``ANY_WITH_FUNCTION`` selectors with no ``representative_members``.
    """
    flagged: list[dict[str, Any]] = []
    for node in iter_nodes(data):
        if not is_leaf_node(node):
            continue
        groundings = node_representative_groundings(node)
        if not groundings:
            selector_types = sorted(
                {
                    str(annoton.get("participant", {}).get("selector_type"))
                    for annoton in as_list(node.get("annotons"))
                    if isinstance(annoton, dict)
                    and isinstance(annoton.get("participant"), dict)
                }
            )
            flagged.append(
                {
                    "id": node.get("id"),
                    "label": node.get("label") or node.get("id"),
                    "annoton_count": len(as_list(node.get("annotons"))),
                    "selector_types": selector_types,
                }
            )
    return flagged


def collect_uniprot_groundings(data: dict[str, Any]) -> list[dict[str, Any]]:
    """Return unique ``UniProtKB`` groundings (base accession) referenced anywhere.

    Recursively scans the whole document for ``term`` dicts whose id is a
    ``UniProtKB`` curie, so it captures concrete subunits, representative members,
    and active units alike. Deduplicated on base accession.
    """
    found: dict[str, dict[str, Any]] = {}

    def walk(obj: Any, label_hint: Optional[str] = None) -> None:
        if isinstance(obj, dict):
            term = obj.get("term")
            term_id = term.get("id") if isinstance(term, dict) else None
            if isinstance(term_id, str) and term_id.startswith(_GROUNDED_TERM_PREFIXES):
                acc = base_accession(term_id)
                if acc and acc not in found:
                    found[acc] = {
                        "accession": acc,
                        "curie": term_id,
                        "label": (
                            obj.get("preferred_term")
                            or (term.get("label") if isinstance(term, dict) else None)
                            or term_id
                        ),
                    }
            for value in obj.values():
                walk(value)
        elif isinstance(obj, list):
            for item in obj:
                walk(item)

    walk(data.get("module"))
    return [found[key] for key in sorted(found)]


# ---------------------------------------------------------------------------
# Conformance checking
# ---------------------------------------------------------------------------


def _node_function_term_id(node: dict[str, Any]) -> Optional[str]:
    """Return the representative molecular-function term id of a tier node.

    Prefers a declared ``function`` role; falls back to the participant's
    ``required_function`` selector. Returns the first such term id found across
    the node's annotons.
    """
    for annoton in as_list(node.get("annotons")):
        if not isinstance(annoton, dict):
            continue
        for holder_key in ("function",):
            holder = annoton.get(holder_key)
            if isinstance(holder, dict):
                term = holder.get("term")
                if isinstance(term, dict) and isinstance(term.get("id"), str):
                    return term["id"]
        participant = annoton.get("participant")
        if isinstance(participant, dict):
            required = participant.get("required_function")
            if isinstance(required, dict):
                term = required.get("term")
                if isinstance(term, dict) and isinstance(term.get("id"), str):
                    return term["id"]
    return None


def node_tier_terms(node: dict[str, Any]) -> list[dict[str, Any]]:
    """Return the ordered child steps of a node as tier descriptors.

    Each entry is ``{"id", "role", "function_id"}`` for one ``parts[].node``,
    ordered by the part ``order`` (parts without an explicit order keep their
    document order, sorted after ordered ones).
    """
    parts = [p for p in as_list(node.get("parts")) if isinstance(p, dict)]

    def sort_key(item: tuple[int, dict[str, Any]]) -> tuple[int, int]:
        index, part = item
        order = part.get("order")
        return (0, order) if isinstance(order, int) else (1, index)

    tiers: list[dict[str, Any]] = []
    for _, part in sorted(enumerate(parts), key=sort_key):
        child = part.get("node")
        if not isinstance(child, dict):
            continue
        tiers.append(
            {
                "id": child.get("id"),
                "role": part.get("role"),
                "function_id": _node_function_term_id(child),
            }
        )
    return tiers


def _normalized_edges(node: dict[str, Any]) -> set[tuple[int, int, str]]:
    """Return a node's internal connections as positional ``(i, j, type)`` edges.

    Child-step ids are indexed by tier order, so the topology can be compared
    across a template and a conforming bundle independently of id naming.
    Connections that reference ids outside the node's own child steps are
    ignored (they wire the bundle to its surroundings, not the motif).
    """
    tiers = node_tier_terms(node)
    index = {t["id"]: i for i, t in enumerate(tiers) if t["id"] is not None}
    edges: set[tuple[int, int, str]] = set()
    for connection in as_list(node.get("connections")):
        if not isinstance(connection, dict):
            continue
        source = connection.get("source")
        target = connection.get("target")
        if source in index and target in index:
            edges.add(
                (index[source], index[target], str(connection.get("connection_type")))
            )
    return edges


def resolve_template_node(
    template_ref: str,
    modules_dir: Path = DEFAULT_MODULES_DIR,
) -> Optional[dict[str, Any]]:
    """Resolve a conformance ``template`` reference to its module node.

    The reference is ``<stem>`` (the module file ``<stem>.yaml``, whose root
    ``module`` node is the motif) or ``<stem>#<node_id>`` to select a nested
    node. Returns ``None`` if the file or node cannot be found.
    """
    stem, _, node_id = template_ref.partition("#")
    path = Path(modules_dir) / f"{stem}.yaml"
    if not path.exists():
        return None
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    if not node_id:
        module = data.get("module")
        return module if isinstance(module, dict) else None
    for node in iter_nodes(data):
        if node.get("id") == node_id:
            return node
    return None


def _terms_match(
    child_id: Optional[str],
    parent_id: Optional[str],
    subclass_of: Optional[SubclassPredicate],
) -> bool:
    """Return True when ``child_id`` equals or is a subclass of ``parent_id``."""
    if child_id is not None and child_id == parent_id:
        return True
    if subclass_of and child_id and parent_id and subclass_of(child_id, parent_id):
        return True
    return False


def _check_one_conformance(
    node: dict[str, Any],
    conformance: dict[str, Any],
    modules_dir: Path,
    subclass_of: Optional[SubclassPredicate],
) -> list[dict[str, Any]]:
    """Check a single ``conforms_to`` entry on a node, returning violations.

    Severity policy keyed on the declared ``status``:

    - ``EXACT`` (or unset): structural mismatches are ``error``.
    - ``WITH_DEVIATIONS``: structural mismatches are downgraded to ``info``
      (they are expected, explained by ``deviations``); a ``warning`` is raised
      if ``WITH_DEVIATIONS`` is declared with no deviations listed.
    - ``EXTENDS``: the node must contain every template tier (by term, in order)
      and may add more; only missing tiers are reported, as ``error``.
    """
    node_id = node.get("id")
    template_ref = str(conformance.get("template"))
    status = (conformance.get("status") or "EXACT").upper()
    deviations = as_list(conformance.get("deviations"))

    def violation(message: str, severity: str) -> dict[str, Any]:
        return {
            "node_id": node_id,
            "template": template_ref,
            "status": status,
            "severity": severity,
            "message": message,
        }

    template_node = resolve_template_node(template_ref, modules_dir)
    if template_node is None:
        return [violation(f"conformance template '{template_ref}' not found", "error")]

    expected = node_tier_terms(template_node)
    actual = node_tier_terms(node)

    # Severity for structural mismatches depends on the declared status.
    mismatch_severity = "info" if status == "WITH_DEVIATIONS" else "error"
    violations: list[dict[str, Any]] = []

    if status == "WITH_DEVIATIONS" and not deviations:
        violations.append(
            violation("status WITH_DEVIATIONS but no deviations listed", "warning")
        )

    if status == "EXTENDS":
        # Template tiers must appear, in order, as a subsequence of the node's.
        actual_terms = [a["function_id"] for a in actual]
        cursor = 0
        for tier in expected:
            match_at = None
            for j in range(cursor, len(actual_terms)):
                if _terms_match(actual_terms[j], tier["function_id"], subclass_of):
                    match_at = j
                    break
            if match_at is None:
                violations.append(
                    violation(
                        f"EXTENDS: template tier {tier['function_id']} "
                        "missing from the bundle",
                        "error",
                    )
                )
            else:
                cursor = match_at + 1
        return violations

    # EXACT / WITH_DEVIATIONS: counts, per-tier terms, and topology must match.
    if len(actual) != len(expected):
        violations.append(
            violation(
                f"tier count {len(actual)} does not match template "
                f"{len(expected)} ({template_ref})",
                mismatch_severity,
            )
        )
    for position, (exp, act) in enumerate(zip(expected, actual), start=1):
        if not _terms_match(act["function_id"], exp["function_id"], subclass_of):
            violations.append(
                violation(
                    f"tier {position} function {act['function_id']} does not "
                    f"match template {exp['function_id']}",
                    mismatch_severity,
                )
            )
    if _normalized_edges(node) != _normalized_edges(template_node):
        violations.append(
            violation(
                "connection topology does not match the template motif",
                mismatch_severity,
            )
        )
    return violations


def conformance_violations(
    data: dict[str, Any],
    modules_dir: Path = DEFAULT_MODULES_DIR,
    subclass_of: Optional[SubclassPredicate] = None,
) -> list[dict[str, Any]]:
    """Return all conformance violations across a module document.

    Walks every node, and for each ``conforms_to`` entry resolves the template
    motif and verifies the node's tiers and topology against it. An empty list
    means every declared conformance holds.
    """
    violations: list[dict[str, Any]] = []
    for node in iter_nodes(data):
        for conformance in as_list(node.get("conforms_to")):
            if isinstance(conformance, dict):
                violations.extend(
                    _check_one_conformance(
                        node, conformance, Path(modules_dir), subclass_of
                    )
                )
    return violations


# ---------------------------------------------------------------------------
# Gene-review index and join
# ---------------------------------------------------------------------------

_ID_RE = re.compile(r"^id:\s*(\S+)\s*$")
_SYMBOL_RE = re.compile(r"^gene_symbol:\s*(\S+)\s*$")


def _read_review_header(path: Path) -> tuple[Optional[str], Optional[str]]:
    """Cheaply read the top-level ``id`` and ``gene_symbol`` of a review file."""
    review_id: Optional[str] = None
    symbol: Optional[str] = None
    with path.open(encoding="utf-8") as handle:
        for _, line in zip(range(40), handle):
            if review_id is None:
                match = _ID_RE.match(line)
                if match:
                    review_id = match.group(1)
            if symbol is None:
                match = _SYMBOL_RE.match(line)
                if match:
                    symbol = match.group(1)
            if review_id is not None and symbol is not None:
                break
    return review_id, symbol


def index_gene_reviews(genes_dir: Path = Path("genes")) -> dict[str, Path]:
    """Map base UniProt accession -> gene review YAML path.

    Scans ``genes/<org>/<gene>/<gene>-ai-review.yaml`` and reads only each file's
    header, so the index is cheap to build even across thousands of genes.
    """
    index: dict[str, Path] = {}
    if not genes_dir.exists():
        return index
    for path in genes_dir.glob("*/*/*-ai-review.yaml"):
        review_id, _ = _read_review_header(path)
        acc = base_accession(review_id)
        if acc:
            index.setdefault(acc, path)
    return index


def review_completeness(review_path: Path) -> dict[str, Any]:
    """Summarize annotation-review completeness and deep-research presence."""
    data = yaml.safe_load(review_path.read_text(encoding="utf-8")) or {}
    annotations = as_list(data.get("existing_annotations"))
    total = len(annotations)
    reviewed = 0
    for annotation in annotations:
        if not isinstance(annotation, dict):
            continue
        review = annotation.get("review")
        if isinstance(review, dict):
            action = review.get("action")
        else:
            action = annotation.get("action")
        if action not in _UNREVIEWED_ACTIONS:
            reviewed += 1

    gene_dir = review_path.parent
    deep_research = sorted(
        md.name
        for md in gene_dir.glob("*-deep-research*.md")
        if md.is_file()
        and not md.name.endswith("-citations.md")
        and not md.name.endswith(".citations.md")
    )

    return {
        "symbol": data.get("gene_symbol"),
        "total_annotations": total,
        "reviewed_annotations": reviewed,
        "complete": total > 0 and reviewed == total,
        "has_deep_research": bool(deep_research),
        "deep_research_files": deep_research,
    }


def module_gene_review_summary(
    data: dict[str, Any],
    gene_index: Optional[dict[str, Path]] = None,
    genes_dir: Path = Path("genes"),
) -> dict[str, Any]:
    """Join a module's UniProt groundings against the gene-review corpus.

    Returns per-gene rows (review present? complete? deep research?) plus
    aggregate counts used by the module page.
    """
    if gene_index is None:
        gene_index = index_gene_reviews(genes_dir)

    rows: list[dict[str, Any]] = []
    for grounding in collect_uniprot_groundings(data):
        acc = grounding["accession"]
        review_path = gene_index.get(acc)
        row: dict[str, Any] = {
            "accession": acc,
            "curie": grounding["curie"],
            "label": grounding["label"],
            "has_review": review_path is not None,
            "symbol": None,
            "complete": False,
            "has_deep_research": False,
            "total_annotations": 0,
            "reviewed_annotations": 0,
            "review_href": None,
        }
        if review_path is not None:
            completeness = review_completeness(review_path)
            row.update(
                {
                    "symbol": completeness["symbol"],
                    "complete": completeness["complete"],
                    "has_deep_research": completeness["has_deep_research"],
                    "total_annotations": completeness["total_annotations"],
                    "reviewed_annotations": completeness["reviewed_annotations"],
                    "review_path": review_path.as_posix(),
                }
            )
        rows.append(row)

    rows.sort(key=lambda item: (item["symbol"] or item["accession"]).lower())
    total = len(rows)
    return {
        "genes": rows,
        "total_genes": total,
        "with_review": sum(1 for row in rows if row["has_review"]),
        "without_review": sum(1 for row in rows if not row["has_review"]),
        "complete_reviews": sum(1 for row in rows if row["complete"]),
        "with_deep_research": sum(1 for row in rows if row["has_deep_research"]),
        "without_deep_research": sum(
            1 for row in rows if row["has_review"] and not row["has_deep_research"]
        ),
    }


# ---------------------------------------------------------------------------
# Module-level deep research
# ---------------------------------------------------------------------------


def module_deep_research(yaml_path: Path) -> dict[str, Any]:
    """Detect a module-level deep-research report next to the module YAML.

    Looks for ``<stem>-deep-research*.md`` siblings (e.g.
    ``photosynthesis-deep-research-falcon.md``) and infers their providers.
    """
    stem = yaml_path.stem
    parent = yaml_path.parent
    files = sorted(
        md
        for md in parent.glob(f"{stem}-deep-research*.md")
        if md.is_file()
        and not md.name.endswith("-citations.md")
        and not md.name.endswith(".citations.md")
    )
    providers: list[dict[str, Any]] = []
    marker = "-deep-research-"
    for md in files:
        report_stem = md.name.removesuffix(".md")
        provider = report_stem.rsplit(marker, 1)[-1] if marker in report_stem else None
        providers.append({"file": md.name, "provider": provider or None})
    return {"has_deep_research": bool(files), "reports": providers}


# ---------------------------------------------------------------------------
# linkml-data-qc compliance
# ---------------------------------------------------------------------------


def run_data_qc(
    yaml_path: Path,
    schema_path: Path = DEFAULT_SCHEMA_PATH,
    target_class: str = "ModuleReview",
) -> dict[str, Any]:
    """Run ``linkml-data-qc`` recommended-field analysis for a module document.

    Returns the global/weighted compliance percentages plus a list of recommended
    slots that are populated below 100% (``missing``).
    """
    from linkml_data_qc.analyzer import ComplianceAnalyzer  # type: ignore[import-untyped]

    analyzer = ComplianceAnalyzer(str(schema_path))
    report = analyzer.analyze_file(str(yaml_path), target_class)

    missing: list[dict[str, Any]] = []
    for path_score in report.path_scores:
        for slot_score in path_score.slot_scores:
            if slot_score.populated < slot_score.total:
                missing.append(
                    {
                        "path": path_score.path,
                        "slot": slot_score.slot_name,
                        "populated": slot_score.populated,
                        "total": slot_score.total,
                        "percentage": round(slot_score.percentage, 1),
                    }
                )
    return {
        "global_compliance": round(report.global_compliance, 1),
        "weighted_compliance": round(report.weighted_compliance, 1),
        "recommended_slots": sorted(report.recommended_slots),
        "missing": missing,
    }


def collect_module_qc(
    yaml_path: Path,
    data: dict[str, Any],
    schema_path: Path = DEFAULT_SCHEMA_PATH,
    gene_index: Optional[dict[str, Path]] = None,
    genes_dir: Path = Path("genes"),
) -> dict[str, Any]:
    """Collect all derived QC stats for a module document in one structure."""
    try:
        data_qc = run_data_qc(yaml_path, schema_path=schema_path)
    except Exception as error:  # external tool: degrade gracefully, never crash render
        data_qc = {"error": str(error)}

    return {
        "data_qc": data_qc,
        "leaf_nodes_missing_representatives": leaf_nodes_missing_representatives(data),
        "conformance_violations": conformance_violations(
            data, modules_dir=yaml_path.parent
        ),
        "gene_reviews": module_gene_review_summary(
            data, gene_index=gene_index, genes_dir=genes_dir
        ),
        "module_deep_research": module_deep_research(yaml_path),
    }
