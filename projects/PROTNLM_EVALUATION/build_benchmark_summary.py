"""Build separate GO-claim and narrative-record summaries from the frozen cohort scope.

Narrative categories are manually indexed from the actual reviews, never inferred
from occurrences of category names in prose. A review can contain multiple categories.
Run from any directory with ``uv run python path/to/build_benchmark_summary.py``.
"""

from collections import Counter, defaultdict
import csv
import hashlib
import json
from pathlib import Path
from typing import Any

import yaml

CODES = ("COR", "CNN", "LSP", "UNC", "NPI", "PLI", "REP")
PUBLIC = "https://github.com/ai4curation/ai-gene-review/blob/main/"


def collect(root: Path) -> dict[str, Any]:
    """Collect exact-accession results; overlapping cohorts do not duplicate the total."""
    base = root / "projects/PROTNLM_EVALUATION"
    scope = list(csv.DictReader((base / "family-curation/scope.csv").open()))
    targets = {r["accession"] for r in scope if r["role"] == "prediction_target"}
    go_counts: Counter[str] = Counter({c: 0 for c in CODES})
    by_accession: dict[str, Counter[str]] = {}
    for path in sorted((root / "genes").glob("*/*/*-protnlm-predictions-review.yaml")):
        doc = yaml.safe_load(path.read_text())
        if doc["id"] not in targets:
            continue
        assert doc["id"] not in by_accession, f"Duplicate prediction review: {path}"
        counts: Counter[str] = Counter()
        for prediction in doc.get("predictions") or []:
            assert prediction["predicted_term_type"] in ("GO_MF", "GO_BP", "GO_CC")
            category = prediction["review"]["assessment"]
            assert category in CODES
            counts[category] += 1
        by_accession[doc["id"]] = counts
        go_counts.update(counts)
    registry = yaml.safe_load((base / "narrative-review-index.yaml").read_text())
    narratives = []
    seen: set[str] = set()
    for entry in registry["reviews"]:
        path = root / entry["review_file"]
        assert path.is_file(), path
        assert (
            hashlib.sha256(path.read_bytes()).hexdigest() == entry["review_sha256"]
        ), f"Narrative index needs review: {path}"
        gene = "/".join(path.parts[-3:-1])
        assert gene not in seen, gene
        seen.add(gene)
        accessions = {
            r["accession"]
            for r in scope
            if r["role"] == "prediction_target"
            and r["species"] + "/" + r["gene_symbol"] == gene
        }
        assert len(accessions) == 1, (gene, accessions)
        categories = entry["categories"]
        assert categories and len(categories) == len(set(categories)), gene
        assert set(categories) <= set(CODES) | {"SUPPORTED"}, gene
        narratives.append(dict(gene=gene, accession=next(iter(accessions)), **entry))
    # A new function sidecar must enter the index; unrelated genes stay out of scope.
    for path in (root / "genes").glob("*/*/*-protnlm-function-review.md"):
        gene = "/".join(path.parts[-3:-1])
        if any(
            r["role"] == "prediction_target"
            and r["species"] + "/" + r["gene_symbol"] == gene
            for r in scope
        ):
            assert gene in seen, f"Unindexed narrative: {path}"
    narrative_counts: Counter[str] = Counter({c: 0 for c in (*CODES, "SUPPORTED")})
    for row in narratives:
        narrative_counts.update(row["categories"])
    cohorts: dict[str, set[str]] = defaultdict(set)
    for row in scope:
        cohorts[row["cohort"]].add(row["accession"])
    cohort_results = []
    for name, accessions in cohorts.items():
        counts: Counter[str] = Counter({c: 0 for c in CODES})
        for accession in accessions:
            counts.update(by_accession.get(accession, {}))
        cohort_results.append(
            dict(
                cohort=name,
                records=len(accessions),
                go_counts=dict(counts),
                narrative_records=sum(r["accession"] in accessions for r in narratives),
            )
        )
    return dict(
        distinct_records=len({r["accession"] for r in scope}),
        prediction_targets=len(targets),
        cohort_memberships=len(scope),
        go_review_files=len(by_accession),
        go_counts=dict(go_counts),
        narrative_counts=dict(narrative_counts),
        narrative_reviews=narratives,
        cohorts=cohort_results,
    )


def write_report(root: Path, data: dict[str, Any]) -> None:
    """Write a linked report with explicit, non-interchangeable denominators."""
    base = root / "projects/PROTNLM_EVALUATION"
    (base / "benchmark-summary.json").write_text(json.dumps(data, indent=2) + "\n")
    lines = [
        "---",
        "title: ProtNLM cross-cohort results",
        "---",
        "# Cross-cohort results",
        "",
        "[Project overview](../PROTNLM_EVALUATION.md) · [Source counts](benchmark-summary.json) · "
        "[Summary generator](build_benchmark_summary.py) · [Narrative category index](narrative-review-index.yaml)",
        "",
        f"The scope contains **{data['distinct_records']} distinct protein records**, including "
        f"**{data['prediction_targets']} prediction targets** and 40 paired human reference records. "
        "Overlapping selections are counted once in the combined totals. These purposive, retrospective "
        "cohorts test informative biological distinctions; their proportions do not estimate proteome-wide accuracy.",
        "",
        "## GO-term assessments",
        "",
        "Each row counted here is one emitted GO term. Narrative functions, protein names and SL localization "
        "outputs are excluded. Zero GO PLI or REP judgments does not imply the absence of narrative errors.",
        "",
        "| Category | GO claims |",
        "|---|---:|",
    ]
    lines += [f"| {c} | {data['go_counts'][c]} |" for c in CODES]
    lines += [
        f"| **Total** | **{sum(data['go_counts'].values())}** |",
        "",
        "## Narrative function reviews",
        "",
        f"**{len(data['narrative_reviews'])} gene/accession review records** assess emitted FUNCTION text. "
        "A record may contain multiple paragraphs and multiple claim categories. Each category below counts "
        "records with at least one such judgment, once per record; categories overlap and must not be summed "
        "or pooled with GO counts. These are neither atomic-claim counts nor one verdict per whole paragraph. "
        "Name and localization assessments remain in the gene notes and are outside both denominators.",
        "",
        "| Category present in function review | Review records |",
        "|---|---:|",
    ]
    lines += [f"| {c} | {data['narrative_counts'][c]} |" for c in (*CODES, "SUPPORTED")]
    lines += [
        "",
        "SUPPORTED records contain an explicitly supported claim whose review does not assign "
        "a novelty-specific COR/CNN/LSP category. They are preserved as such. References to separate "
        "GO judgments, hypothetical corrections, and claims explicitly not emitted are excluded.",
        "",
        "### Individual narrative records",
        "",
        "| Gene | Accession | Categories present | Evidence and claim distinctions |",
        "|---|---|---|---|",
    ]
    for row in sorted(data["narrative_reviews"], key=lambda x: x["gene"]):
        lines.append(
            f"| {row['gene']} | {row['accession']} | {', '.join(row['categories'])} | "
            f"[Function review]({PUBLIC}{row['review_file']}) |"
        )
    lines += [
        "",
        "## Cohort scope",
        "",
        "The cohort rows retain overlapping selections, including six fly targets selected twice. "
        "Paired reference records provide evidence and contribute no extra prediction assessments. "
        "Use the deduplicated totals above for the combined corpus.",
        "",
        "| Cohort | Records | GO claims | Narrative review records |",
        "|---|---:|---:|---:|",
    ]
    for row in data["cohorts"]:
        lines.append(
            f"| {row['cohort']} | {row['records']} | {sum(row['go_counts'].values())} | {row['narrative_records']} |"
        )
    lines += [
        "",
        "## Source metadata",
        "",
        "`source_method: ProtNLM2` names the model. `source_version` identifies the release, XML artifact "
        "or dated API snapshot. API retrieval timestamps are observation times, not model training dates. "
        "The pilot, exploratory XML and later API snapshots remain distinct; frozen responses and "
        "source references retain their original provenance.",
        "",
    ]
    (base / "benchmark-results.md").write_text("\n".join(lines))


if __name__ == "__main__":
    repository = Path(__file__).resolve().parents[2]
    result = collect(repository)
    write_report(repository, result)
    print(
        json.dumps(
            {
                k: v
                for k, v in result.items()
                if k not in ("narrative_reviews", "cohorts")
            },
            indent=2,
        )
    )
