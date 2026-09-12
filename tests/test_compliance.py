"""Evidence-aware compliance integration tests; no network or mocked analyzer."""

from pathlib import Path

import pytest
import yaml

from ai_gene_review.compliance import GeneComplianceAnalyzer, GeneQCConfig


SCHEMA = Path("src/ai_gene_review/schema/gene_review.yaml")


def analyze(tmp_path, annotations, config=None):
    """Analyze a minimal real YAML review through the schema and policy."""
    path = tmp_path / "review.yaml"
    path.write_text(yaml.safe_dump({"existing_annotations": annotations}))
    return GeneComplianceAnalyzer(SCHEMA, config).analyze_file(path)


def annotation(evidence="IMP", action="MODIFY", **review):
    """Create an annotation with a reason but no supplied evidence."""
    return {
        "evidence_type": evidence,
        "original_reference_id": "PMID:1",
        "review": {"action": action, "reason": "Use a more specific term.", **review},
    }


def metric(report, name):
    """Select a computed metric from the shared report format."""
    return next(s for s in report.aggregated_scores if s.slot_name == name)


@pytest.mark.parametrize("evidence", ["IMP", "IDA", "EXP", "HDA", "TAS"])
@pytest.mark.parametrize(
    "action",
    ["ACCEPT", "MODIFY", "REMOVE", "KEEP_AS_NON_CORE", "MARK_AS_OVER_ANNOTATED", "NEW"],
)
def test_literature_decisions_reward_quotes(tmp_path, evidence, action):
    report = analyze(
        tmp_path,
        [
            annotation(evidence, action),
            annotation(
                evidence,
                action,
                supported_by=[{"reference_id": "PMID:1", "supporting_text": "A quote"}],
            ),
        ],
    )
    score = metric(report, "literature_support")
    assert (score.populated, score.total, score.percentage) == (1, 2, 50)


@pytest.mark.parametrize(
    "support",
    [
        [],
        [{"reference_id": "PMID:1"}],
        [{"reference_id": "PMID:1", "supporting_text": "  "}],
        [{"supporting_text": "orphan quote"}],
        [{"reference_id": "file:research.md", "supporting_text": "summary"}],
    ],
)
def test_empty_or_nonliterature_support_does_not_count_as_quote(tmp_path, support):
    assert (
        metric(
            analyze(tmp_path, [annotation(supported_by=support)]), "literature_support"
        ).populated
        == 0
    )


def test_fulltext_quote_supported(tmp_path):
    report = analyze(
        tmp_path,
        [
            annotation(
                supported_by=[
                    {
                        "reference_id": "DOI:10.1/example",
                        "supporting_text_fulltext": "Full text excerpt",
                    }
                ]
            )
        ],
    )
    assert metric(report, "literature_support").populated == 1


def test_iea_and_undecided_excluded_from_quote_denominator(tmp_path):
    report = analyze(
        tmp_path,
        [
            annotation("IEA", "ACCEPT"),
            annotation("IMP", "UNDECIDED"),
            annotation("IMP", "PENDING"),
        ],
    )
    assert not any(
        s.slot_name in {"literature_support", "inference_support", "supported_by"}
        for s in report.aggregated_scores
    )


@pytest.mark.parametrize(
    "support",
    [
        {"supported_by": [{"reference_id": "GO_REF:0000002"}]},
        {"additional_reference_ids": ["file:analysis.md"]},
        {"propagation_review": {"source_entities": [{"source_id": "PANTHER:PTN1"}]}},
    ],
)
def test_inferred_corrections_reward_sources_without_quotes(tmp_path, support):
    report = analyze(tmp_path, [annotation("IEA", **support), annotation("IBA")])
    assert (
        metric(report, "inference_support").populated,
        metric(report, "inference_support").total,
    ) == (1, 2)
    assert not any(
        s.slot_name == "literature_support" for s in report.aggregated_scores
    )


def test_threshold_weights_and_consistent_totals(tmp_path):
    config = GeneQCConfig.from_yaml("conf/qc_config.yaml")
    config.paths["existing_annotations[].review.literature_support"].weight = 4
    config.paths["existing_annotations[].review.literature_support"].min_compliance = 80
    report = analyze(tmp_path, [annotation()], config)
    assert metric(report, "literature_support").weight == 4
    assert any(v.slot_name == "literature_support" for v in report.threshold_violations)
    assert report.total_checks == sum(
        s.total for p in report.path_scores for s in p.slot_scores
    )
    assert report.total_checks == sum(s.total for s in report.aggregated_scores)
    assert report.total_populated == sum(s.populated for s in report.aggregated_scores)
    assert report.weighted_compliance == pytest.approx(
        100
        * sum(s.populated * s.weight for s in report.aggregated_scores)
        / sum(s.total * s.weight for s in report.aggregated_scores)
    )


def test_config_can_change_applicability(tmp_path):
    config = GeneQCConfig.from_yaml("conf/qc_config.yaml")
    config.annotation_rules["literature_support"].actions = ["NEW"]
    report = analyze(tmp_path, [annotation()], config)
    assert not any(
        s.slot_name == "literature_support" for s in report.aggregated_scores
    )


def test_unknown_config_keys_fail():
    with pytest.raises(ValueError):
        GeneQCConfig.model_validate({"annotation_rulez": {}})


def test_raw_schema_mode_preserved(tmp_path):
    report = analyze(tmp_path, [annotation("IEA", "ACCEPT")], GeneQCConfig())
    assert metric(report, "supported_by").populated == 0


def test_implicit_inlining_and_class_specific_ranges(tmp_path):
    """Regression: upstream traversal skipped annotations and core functions."""
    path = tmp_path / "review.yaml"
    path.write_text(
        yaml.safe_dump(
            {
                "existing_annotations": [annotation()],
                "core_functions": [{"description": "function", "supported_by": [{}]}],
            }
        )
    )
    report = GeneComplianceAnalyzer(SCHEMA).analyze_file(path)
    paths = {p.path for p in report.path_scores}
    assert "existing_annotations[0].review" in paths
    assert "core_functions[0].supported_by[0]" in paths
    assert any(
        s.slot_name == "supporting_text" and s.populated == 0
        for p in report.path_scores
        if p.path == "core_functions[0].supported_by[0]"
        for s in p.slot_scores
    )


def test_inference_requires_reason_and_identified_source(tmp_path):
    report = analyze(
        tmp_path,
        [
            annotation("IEA", reason=" ", additional_reference_ids=["GO_REF:1"]),
            annotation("IEA", propagation_review={"source_entities": [{}]}),
        ],
    )
    assert metric(report, "inference_support").populated == 0


def test_iea_quote_does_not_add_extra_checks(tmp_path):
    plain = analyze(tmp_path, [annotation("IEA", "ACCEPT")])
    quoted = analyze(
        tmp_path,
        [
            annotation(
                "IEA",
                "ACCEPT",
                supported_by=[
                    {"reference_id": "GO_REF:1", "supporting_text": "Some text"}
                ],
            )
        ],
    )
    assert plain.total_checks == quoted.total_checks
    assert plain.total_populated == quoted.total_populated


def test_plugin_extension(tmp_path):
    from linkml_data_qc.models import PathCompliance, SlotCompliance

    class ExamplePlugin:
        """A computed property can participate without modifying the engine."""

        def evaluate(self, data, config):
            return [
                PathCompliance(
                    path="(root)",
                    parent_class="GeneReview",
                    item_count=1,
                    overall_percentage=0,
                    slot_scores=[
                        SlotCompliance(
                            path="(root)",
                            slot_name="example",
                            total=1,
                            populated=0,
                            percentage=0,
                        )
                    ],
                )
            ]

    path = tmp_path / "review.yaml"
    path.write_text("{}")
    report = GeneComplianceAnalyzer(SCHEMA, plugins=(ExamplePlugin(),)).analyze_file(
        path
    )
    assert metric(report, "example").total == 1


def test_cli_reports_and_opt_in_threshold_exit(tmp_path):
    import json
    from typer.testing import CliRunner
    from ai_gene_review.cli import app

    data = tmp_path / "review.yaml"
    data.write_text(
        yaml.safe_dump({"existing_annotations": [annotation("IEA"), annotation()]})
    )
    policy = GeneQCConfig.from_yaml("conf/qc_config.yaml")
    policy.paths["existing_annotations[].review.literature_support"].min_compliance = 80
    config = tmp_path / "config.yaml"
    policy.to_yaml(config)
    gaps, summary, details = [
        tmp_path / n for n in ["gaps.tsv", "summary.tsv", "details.json"]
    ]
    args = [
        "compliance",
        str(data),
        "--config",
        str(config),
        "--tsv-output",
        str(gaps),
        "--summary-output",
        str(summary),
        "--json-output",
        str(details),
    ]
    runner = CliRunner()
    result = runner.invoke(app, args)
    assert result.exit_code == 0, result.output
    assert "existing_annotations[1].review.literature_support" in gaps.read_text()
    assert "existing_annotations[0].review.literature_support" not in gaps.read_text()
    assert "weighted_compliance" in summary.read_text()
    report = json.loads(details.read_text())[0]
    assert report["threshold_violations"][0]["slot_name"] == "literature_support"
    assert runner.invoke(app, args + ["--fail-on-threshold"]).exit_code == 1
    assert runner.invoke(app, args + ["--schema-only"]).exit_code != 0
