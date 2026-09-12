"""Configurable, evidence-aware compliance built on linkml-data-qc reports.

Like dismech's QC plugins, computed metrics share the schema metrics' weights
and thresholds. Plugins emit per-instance scores so missing-item reports,
aggregate scores, and dashboards all use the same applicable denominator.
This measures evidence presence, not its biological correctness or verbatimness.
"""

from collections import defaultdict
from pathlib import Path
import re
from typing import Any, Literal, Protocol

import yaml
from pydantic import BaseModel, ConfigDict, Field
from linkml_runtime.utils.schemaview import SchemaView
from linkml_data_qc.config import QCConfig
from linkml_data_qc.models import (
    AggregatedPathScore,
    ComplianceReport,
    PathCompliance,
    SlotCompliance,
    ThresholdViolation,
)


class AnnotationRule(BaseModel):
    """Select applicable annotations and the form of evidence to reward."""

    model_config = ConfigDict(extra="forbid")
    evidence_types: list[str]
    actions: list[str]
    support: Literal["literature_quote", "sourced_rationale"]


class GeneQCConfig(QCConfig):
    """Extend dismech-compatible weights/thresholds with exclusions and rules.

    Empty configuration preserves raw recommended-field checks. Exclusions are
    exact normalized slot paths, or subtree prefixes ending in ``.**``.
    """

    model_config = ConfigDict(extra="forbid")
    excluded_paths: list[str] = Field(default_factory=list)
    annotation_rules: dict[str, AnnotationRule] = Field(default_factory=dict)


def default_config_path() -> Path:
    """Return the packaged policy, also exposed as conf/qc_config.yaml."""
    return Path(__file__).parent / "schema" / "qc_config.yaml"


def normalized(path: str) -> str:
    """Normalize list indices for path-specific weights and exclusions.

    >>> normalized('existing_annotations[12].review')
    'existing_annotations[].review'
    """
    return re.sub(r"\[\d+\]", "[]", path)


def has_text(value: Any) -> bool:
    """Treat whitespace-only strings as absent."""
    return isinstance(value, str) and bool(value.strip())


class QCMetricPlugin(Protocol):
    """Extension seam for computed checks, without changing the analyzer."""

    def evaluate(
        self, data: dict[str, Any], config: GeneQCConfig
    ) -> list[PathCompliance]:
        """Return per-instance applicable checks; omit inapplicable checks."""
        ...


class AnnotationSupportPlugin:
    """Reward quotes or sourced rationale using configured evidence/actions."""

    def evaluate(
        self, data: dict[str, Any], config: GeneQCConfig
    ) -> list[PathCompliance]:
        """Score one opportunity per applicable annotation, not per quotation."""
        scores = []
        for i, annotation in enumerate(data.get("existing_annotations") or []):
            review = annotation.get("review") or {}
            support = review.get("supported_by") or []
            for name, rule in config.annotation_rules.items():
                if (
                    annotation.get("evidence_type") not in rule.evidence_types
                    or review.get("action") not in rule.actions
                ):
                    continue
                if rule.support == "literature_quote":
                    passed = any(
                        has_text(s.get("reference_id"))
                        and s["reference_id"].startswith(("PMID:", "DOI:"))
                        and (
                            has_text(s.get("supporting_text"))
                            or has_text(s.get("supporting_text_fulltext"))
                        )
                        for s in support
                    )
                else:
                    sources = (review.get("propagation_review") or {}).get(
                        "source_entities"
                    ) or []
                    passed = has_text(review.get("reason")) and (
                        any(has_text(s.get("reference_id")) for s in support)
                        or any(
                            has_text(s)
                            for s in review.get("additional_reference_ids") or []
                        )
                        or any(has_text(s.get("source_id")) for s in sources)
                    )
                path = f"existing_annotations[{i}].review"
                scores.append(
                    PathCompliance(
                        path=path,
                        parent_class="Review",
                        item_count=1,
                        overall_percentage=100.0 if passed else 0.0,
                        slot_scores=[
                            SlotCompliance(
                                path=path,
                                slot_name=name,
                                populated=int(passed),
                                total=1,
                                percentage=100.0 if passed else 0.0,
                            )
                        ],
                    )
                )
        return scores


def rebuild_report(report: ComplianceReport, config: GeneQCConfig) -> ComplianceReport:
    """Recompute all summaries from applicable per-instance checks.

    Include root fields as well as list fields in weighted scoring. No private
    linkml-data-qc APIs are used; report and dashboard models remain compatible.
    """
    counts: dict[tuple[str, str, str], list[int]] = defaultdict(lambda: [0, 0])
    slots: dict[str, list[int]] = defaultdict(lambda: [0, 0])
    for path_score in report.path_scores:
        for score in path_score.slot_scores:
            key = (
                normalized(path_score.path),
                score.slot_name,
                path_score.parent_class,
            )
            counts[key][0] += score.populated
            counts[key][1] += score.total
            slots[score.slot_name][0] += score.populated
            slots[score.slot_name][1] += score.total
    report.aggregated_scores = [
        AggregatedPathScore(
            path=path,
            slot_name=slot,
            parent_class=cls,
            populated=pop,
            total=total,
            percentage=100 * pop / total,
            weight=config.get_weight(path, slot),
            min_compliance=config.get_min_compliance(path, slot),
        )
        for (path, slot, cls), (pop, total) in sorted(counts.items())
        if total
    ]
    scores = report.aggregated_scores
    report.total_checks = sum(s.total for s in scores)
    report.total_populated = sum(s.populated for s in scores)
    report.global_compliance = (
        100 * report.total_populated / report.total_checks
        if report.total_checks
        else 100.0
    )
    weighted_total = sum(s.total * s.weight for s in scores)
    report.weighted_compliance = (
        100 * sum(s.populated * s.weight for s in scores) / weighted_total
        if weighted_total
        else 100.0
    )
    report.summary_by_slot = {
        slot: 100 * pop / total for slot, (pop, total) in slots.items() if total
    }
    report.recommended_slots = sorted(slots)
    report.threshold_violations = [
        ThresholdViolation(
            path=f"{s.path}.{s.slot_name}",
            slot_name=s.slot_name,
            actual_compliance=s.percentage,
            min_required=s.min_compliance,
            shortfall=s.min_compliance - s.percentage,
        )
        for s in scores
        if s.min_compliance is not None and s.percentage < s.min_compliance
    ]
    return report


class GeneComplianceAnalyzer:
    """Compose schema completeness with configurable, contextual QC plugins."""

    def __init__(
        self,
        schema_path: str | Path,
        config: GeneQCConfig | None = None,
        plugins: tuple[QCMetricPlugin, ...] = (AnnotationSupportPlugin(),),
    ) -> None:
        self.config = (
            config
            if config is not None
            else GeneQCConfig.from_yaml(default_config_path())
        )
        self.schema_path = str(schema_path)
        self.schema = SchemaView(self.schema_path)
        self.plugins = plugins

    def schema_scores(
        self, data: dict[str, Any], class_name: str = "GeneReview", path: str = "(root)"
    ) -> list[PathCompliance]:
        """Traverse actual nested objects, including implicitly inlined slots.

        The upstream analyzer only follows explicitly inlined slots and uses
        global rather than induced slot definitions. GeneReview relies on both
        implicit inlining and class-specific slot definitions. String reference
        values are never traversed as objects.
        """
        result = []
        scores = []
        for slot in self.schema.class_induced_slots(class_name):
            value = data.get(slot.name)
            if slot.recommended:
                populated = (
                    value is not None
                    and value != []
                    and value != {}
                    and (not isinstance(value, str) or has_text(value))
                )
                scores.append(
                    SlotCompliance(
                        path=path,
                        slot_name=slot.name,
                        populated=int(populated),
                        total=1,
                        percentage=100.0 if populated else 0.0,
                    )
                )
            if slot.range in self.schema.all_classes():
                child_path = f"{path}.{slot.name}" if path != "(root)" else slot.name
                if isinstance(value, dict):
                    result.extend(self.schema_scores(value, slot.range, child_path))
                elif isinstance(value, list):
                    for i, item in enumerate(value):
                        if isinstance(item, dict):
                            result.extend(
                                self.schema_scores(
                                    item, slot.range, f"{child_path}[{i}]"
                                )
                            )
        if scores:
            result.append(
                PathCompliance(
                    path=path,
                    parent_class=class_name,
                    item_count=1,
                    slot_scores=scores,
                    overall_percentage=sum(s.percentage for s in scores) / len(scores),
                )
            )
        return result

    def analyze_file(self, path: str | Path) -> ComplianceReport:
        """Analyze one review, replacing excluded checks before adding plugins."""
        data = yaml.safe_load(Path(path).read_text())
        if not isinstance(data, dict):
            raise ValueError(f"Expected a gene review mapping in {path}")
        report = ComplianceReport(
            file_path=str(path),
            target_class="GeneReview",
            schema_path=self.schema_path,
            global_compliance=100,
            weighted_compliance=100,
            total_checks=0,
            total_populated=0,
            path_scores=self.schema_scores(data),
        )
        paths = []
        for score in report.path_scores:
            kept = []
            for slot in score.slot_scores:
                full_path = f"{normalized(score.path)}.{slot.slot_name}"
                if not any(
                    full_path == excluded
                    or (
                        excluded.endswith(".**") and full_path.startswith(excluded[:-2])
                    )
                    for excluded in self.config.excluded_paths
                ):
                    kept.append(slot)
            if kept:
                score.slot_scores = kept
                score.overall_percentage = (
                    100 * sum(s.populated for s in kept) / sum(s.total for s in kept)
                )
                paths.append(score)
        for plugin in self.plugins:
            paths.extend(plugin.evaluate(data, self.config))
        # Merge plugin and schema checks at the same object path for dashboards.
        merged: dict[tuple[str, str], PathCompliance] = {}
        for score in paths:
            key = (score.path, score.parent_class)
            if key in merged:
                merged[key].slot_scores.extend(score.slot_scores)
            else:
                merged[key] = score
        for score in merged.values():
            total = sum(s.total for s in score.slot_scores)
            score.overall_percentage = (
                100 * sum(s.populated for s in score.slot_scores) / total
                if total
                else 100.0
            )
        report.path_scores = list(merged.values())
        return rebuild_report(report, self.config)
