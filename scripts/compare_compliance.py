"""Compare review revisions with one schema and action-stable evidence policy.

Run from the repository root. The inclusive comparison holds UNDECIDED and all
conclusive actions in each configured rule's denominator, including ACCEPT for
inferred annotations. It is a sensitivity analysis, not the default QC policy.
"""

import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import tempfile
from typing import Any

from linkml_data_qc.models import ComplianceReport

from ai_gene_review.compliance import GeneComplianceAnalyzer, GeneQCConfig


GENES = (
    "ABI1",
    "FLS2",
    "MYC2",
    "GL1",
    "FBL22",
    "EIN2",
    "AGO1",
    "CASPL1D1",
    "DRB1",
    "EIN3",
    "COI1",
)
ACTIONS = [
    "ACCEPT",
    "MODIFY",
    "REMOVE",
    "KEEP_AS_NON_CORE",
    "MARK_AS_OVER_ANNOTATED",
    "NEW",
    "UNDECIDED",
]


def comparison_policy(config: GeneQCConfig) -> GeneQCConfig:
    """Freeze action applicability while preserving evidence codes and weights."""
    inclusive = config.model_copy(deep=True)
    for rule in inclusive.annotation_rules.values():
        rule.actions = list(ACTIONS)
    return inclusive


def digest(content: bytes) -> str:
    """Record an exact input fingerprint for reproducibility."""
    return hashlib.sha256(content).hexdigest()


def summarize(report: ComplianceReport) -> dict[str, Any]:
    """Expose weighted and rule denominators, not just percentages."""
    scores = report.aggregated_scores
    return {
        "weighted_percentage": report.weighted_compliance,
        "weighted_populated": sum(s.populated * s.weight for s in scores),
        "weighted_total": sum(s.total * s.weight for s in scores),
        "total_populated": report.total_populated,
        "total_checks": report.total_checks,
        "support_counts": {
            name: {
                "populated": sum(s.populated for s in scores if s.slot_name == name),
                "total": sum(s.total for s in scores if s.slot_name == name),
            }
            for name in ("literature_support", "inference_support")
        },
    }


def main() -> None:
    """Read baseline YAMLs from git and current YAMLs without altering either."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", required=True, help="Git revision before curation")
    parser.add_argument("--genes", nargs="+", default=list(GENES))
    parser.add_argument(
        "--schema",
        type=Path,
        default=Path("src/ai_gene_review/schema/gene_review.yaml"),
    )
    parser.add_argument("--config", type=Path, default=Path("conf/qc_config.yaml"))
    parser.add_argument(
        "--baseline-json",
        type=Path,
        help="Optional historical contextual report, for cross-check only",
    )
    parser.add_argument(
        "--output",
        type=Path,
        required=True,
        help="Markdown report; matching .json contains exact counts/provenance",
    )
    args = parser.parse_args()
    base = subprocess.check_output(["git", "rev-parse", args.base], text=True).strip()
    historical = {}
    if args.baseline_json:
        historical = {
            r["file_path"]: r["weighted_compliance"]
            for r in json.loads(args.baseline_json.read_text())
        }
    config = GeneQCConfig.from_yaml(args.config)
    inclusive = comparison_policy(config)
    analyzers = {
        "contextual": GeneComplianceAnalyzer(args.schema, config),
        "inclusive": GeneComplianceAnalyzer(args.schema, inclusive),
    }
    results = []
    with tempfile.TemporaryDirectory(prefix="compliance-comparison-") as temp:
        for gene in args.genes:
            path = Path(f"genes/ARATH/{gene}/{gene}-ai-review.yaml")
            before = subprocess.check_output(["git", "show", f"{base}:{path}"])
            after = path.read_bytes()
            row = {
                "gene": gene,
                "baseline_sha256": digest(before),
                "current_sha256": digest(after),
            }
            for state, content in [("before", before), ("after", after)]:
                temporary = Path(temp) / f"{gene}-{state}.yaml"
                temporary.write_bytes(content)
                row[state] = {
                    policy: summarize(analyzer.analyze_file(temporary))
                    for policy, analyzer in analyzers.items()
                }
            if str(path) in historical:
                row["historical_contextual_percentage"] = historical[str(path)]
                row["historical_vs_recomputed_baseline_delta"] = (
                    row["before"]["contextual"]["weighted_percentage"]
                    - historical[str(path)]
                )
            results.append(row)
    metadata = {
        "baseline_revision": base,
        "current_head": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True
        ).strip(),
        "current_is_working_tree": True,
        "schema_sha256": digest(args.schema.read_bytes()),
        "analyzer_sha256": digest(
            Path("src/ai_gene_review/compliance.py").read_bytes()
        ),
        "comparison_script_sha256": digest(Path(__file__).read_bytes()),
        "policy_sha256": digest(args.config.read_bytes()),
        "contextual_policy": config.model_dump(),
        "inclusive_policy": inclusive.model_dump(),
        "historical_report_sha256": digest(args.baseline_json.read_bytes())
        if args.baseline_json
        else None,
        "results": results,
    }
    lines = [
        "# ARATH compliance comparison",
        "",
        f"Baseline YAML revision: `{base}`. Current input: working tree (individual SHA-256 fingerprints in the companion JSON).",
        "",
        "Both revisions are recomputed with the same current analyzer, schema, weights and evidence-code rules. "
        "The inclusive policy uses ACCEPT, MODIFY, REMOVE, KEEP_AS_NON_CORE, MARK_AS_OVER_ANNOTATED, NEW and UNDECIDED "
        "for every evidence rule. Thus changing a decision among these actions cannot remove that annotation from a rule denominator. "
        "PENDING or missing reviews remain outside action-conditioned rules. IEA does not require quotations; its inclusive check is sourced rationale.",
        "",
        "These are completeness scores, not evidence-quality scores. Inclusive gains can reflect changed reference findings, core functions, "
        "other recommended fields, added/deleted rows and evidence presence. They do not isolate added evidence. "
        "New objects can still change total denominators; exact weighted numerators/denominators and rule counts are included below and in JSON.",
        "",
        "| Gene | Contextual before → after | Inclusive before → after | Inclusive weighted numerator/denominator before → after | Literature support before → after | Inference support before → after |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for row in results:
        b, a = row["before"], row["after"]

        def counts(state: dict[str, Any], name: str) -> str:
            """Format the populated and applicable evidence opportunities."""
            score = state["inclusive"]["support_counts"][name]
            return f"{score['populated']}/{score['total']}"

        lines.append(
            f"| {row['gene']} | {b['contextual']['weighted_percentage']:.2f}% → {a['contextual']['weighted_percentage']:.2f}% | "
            f"{b['inclusive']['weighted_percentage']:.2f}% → {a['inclusive']['weighted_percentage']:.2f}% | "
            f"{b['inclusive']['weighted_populated']:g}/{b['inclusive']['weighted_total']:g} → {a['inclusive']['weighted_populated']:g}/{a['inclusive']['weighted_total']:g} | "
            f"{counts(b, 'literature_support')} → {counts(a, 'literature_support')} | {counts(b, 'inference_support')} → {counts(a, 'inference_support')} |"
        )
    if historical:
        deltas = [
            abs(r["historical_vs_recomputed_baseline_delta"])
            for r in results
            if "historical_vs_recomputed_baseline_delta" in r
        ]
        lines += [
            "",
            f"Historical contextual snapshot cross-check: {len(deltas)} genes matched by path; maximum absolute difference from recomputed baseline: {max(deltas, default=0):.6f} percentage points. Historical scores are not used in either comparison denominator.",
        ]
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text("\n".join(lines) + "\n")
    args.output.with_suffix(".json").write_text(json.dumps(metadata, indent=2) + "\n")
    print(args.output)


if __name__ == "__main__":
    main()
