"""Build separate GO-claim and narrative-record summaries from the frozen cohort scope.

Narrative categories are manually indexed from the actual reviews, never inferred
from occurrences of category names in prose. A review can contain multiple categories.
Gene files are read at the declared benchmark ``review_snapshot_commit``, not from
the working tree, so ordinary curation cannot stale the report. The curator-edited
config (cohort scope, narrative index) is read from ``config`` -- the working tree
in production -- so editing it takes effect, and an index hash that no longer
matches the snapshot review fails loudly. Refresh with ``just refresh-benchmark-snapshot``.
Run from any directory with ``uv run python path/to/build_benchmark_summary.py``.
"""

from collections import Counter, defaultdict
import csv
import hashlib
import io
import json
import statistics
from pathlib import Path
from typing import Any

import yaml

from ai_gene_review.source_tree import (
    ReviewSnapshot,
    SourceTree,
    WorkingTree,
    declared_review_snapshot,
    review_snapshot_tree,
)

CODES = ("COR", "CNN", "LSP", "UNC", "NPI", "PLI", "REP")
PUBLIC = "https://github.com/ai4curation/ai-gene-review/blob/main/"


def _goa_rows(tree: SourceTree, gene_dir: str) -> list[dict[str, str]] | None:
    """Rows of the target's cached GOA TSV at the snapshot (None if the file is absent)."""
    files = sorted(tree.glob(f"{gene_dir}/*-goa.tsv"))
    if not files:
        return None
    return list(csv.DictReader(io.StringIO(tree.read_text(files[0]), newline=""), delimiter="\t"))


def count_goa_rows(tree: SourceTree, gene_dir: str) -> int | None:
    """Count non-negated annotation rows in the target's cached GOA TSV (None if absent)."""
    rows = _goa_rows(tree, gene_dir)
    if rows is None:
        return None
    return sum(1 for r in rows if not (r.get("QUALIFIER") or "").startswith("NOT"))


def latest_goa_date(tree: SourceTree, gene_dir: str) -> str | None:
    """Latest annotation DATE (YYYYMMDD) in the cached GOA TSV; a lower bound on its snapshot date."""
    rows = _goa_rows(tree, gene_dir)
    dates = [r["DATE"] for r in rows or [] if r.get("DATE")]
    return max(dates) if dates else None


def collect(tree: SourceTree, config: SourceTree) -> dict[str, Any]:
    """Collect exact-accession results, retaining explicit zero-output review records.

    Gene files come from ``tree`` (the review snapshot); ``scope.csv`` and
    ``narrative-review-index.yaml`` come from ``config`` (the working tree).

    Overlapping cohorts do not duplicate the total. ``go_review_files`` remains a
    legacy alias for all ``prediction_review_files``, including empty reviews.
    """
    base = "projects/PROTNLM_EVALUATION"
    scope = list(
        csv.DictReader(
            io.StringIO(config.read_text(f"{base}/family-curation/scope.csv"), newline="")
        )
    )
    targets = {r["accession"] for r in scope if r["role"] == "prediction_target"}
    go_counts: Counter[str] = Counter({c: 0 for c in CODES})
    by_accession: dict[str, Counter[str]] = {}
    zero_go_reviews: list[dict[str, str]] = []
    goa_rows: dict[str, int | None] = {}
    goa_latest: dict[str, str | None] = {}
    for path in tree.glob("genes/*/*/*-protnlm-predictions-review.yaml"):
        doc = yaml.safe_load(tree.read_text(path))
        if doc["id"] not in targets:
            continue
        assert doc["id"] not in by_accession, f"Duplicate prediction review: {path}"
        predictions = doc.get("predictions")
        assert isinstance(predictions, list), (
            f"Explicit predictions list required: {path}"
        )
        if not predictions:
            description = doc.get("description")
            assert (
                doc.get("status") == "COMPLETE"
                and isinstance(description, str)
                and description.strip()
            ), f"Completed zero-output review with description required: {path}"
            zero_go_reviews.append(
                dict(
                    gene="/".join(path.split("/")[1:3]),
                    accession=doc["id"],
                    review_file=path,
                )
            )
        gene_dir = path.rsplit("/", 1)[0]
        goa_rows[doc["id"]] = count_goa_rows(tree, gene_dir)
        goa_latest[doc["id"]] = latest_goa_date(tree, gene_dir)
        counts: Counter[str] = Counter()
        for prediction in predictions:
            assert prediction["predicted_term_type"] in ("GO_MF", "GO_BP", "GO_CC")
            category = prediction["review"]["assessment"]
            assert category in CODES
            counts[category] += 1
        by_accession[doc["id"]] = counts
        go_counts.update(counts)
    registry = yaml.safe_load(config.read_text(f"{base}/narrative-review-index.yaml"))
    narratives = []
    seen: set[str] = set()
    for entry in registry["reviews"]:
        path = entry["review_file"]
        assert tree.is_file(path), path
        assert (
            hashlib.sha256(tree.read_bytes(path)).hexdigest() == entry["review_sha256"]
        ), f"Narrative index needs review: {path}"
        gene = "/".join(path.split("/")[-3:-1])
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
    for path in tree.glob("genes/*/*/*-protnlm-function-review.md"):
        gene = "/".join(path.split("/")[1:3])
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
    assessed_accessions = {
        accession for accession, counts in by_accession.items() if counts
    }
    zero_go_accessions = {row["accession"] for row in zero_go_reviews}
    narrative_accessions = {r["accession"] for r in narratives}
    reviewed_targets = targets & (set(by_accession) | narrative_accessions)
    cohort_results = []
    for name, accessions in cohorts.items():
        counts: Counter[str] = Counter({c: 0 for c in CODES})
        for accession in accessions:
            counts.update(by_accession.get(accession, {}))
        goa_sizes = sorted(
            goa_rows[a] for a in accessions & assessed_accessions if goa_rows.get(a) is not None
        )
        cohort_results.append(
            dict(
                cohort=name,
                records=len(accessions),
                records_with_go_assessments=len(accessions & assessed_accessions),
                records_with_zero_go_predictions=len(accessions & zero_go_accessions),
                records_with_any_review=len(accessions & reviewed_targets),
                records_with_narrative_review_only=len(
                    (accessions & narrative_accessions) - set(by_accession)
                ),
                records_without_any_review=len((accessions & targets) - reviewed_targets),
                go_counts=dict(counts),
                narrative_records=sum(r["accession"] in accessions for r in narratives),
                median_cached_goa_rows_per_go_assessed_record=(
                    statistics.median(goa_sizes) if goa_sizes else None
                ),
            )
        )
    return dict(
        distinct_records=len({r["accession"] for r in scope}),
        prediction_targets=len(targets),
        prediction_targets_with_any_review=len(reviewed_targets),
        prediction_targets_with_go_review_file=len(targets & set(by_accession)),
        prediction_targets_with_narrative_review_only=len(
            (targets & narrative_accessions) - set(by_accession)
        ),
        prediction_targets_without_any_review=len(targets - reviewed_targets),
        cohort_memberships=len(scope),
        prediction_review_files=len(by_accession),
        go_review_files=len(by_accession),
        records_with_go_assessments=len(assessed_accessions),
        records_with_zero_go_predictions=len(zero_go_reviews),
        zero_go_prediction_reviews=zero_go_reviews,
        go_counts=dict(go_counts),
        cached_goa_latest_annotation_year=dict(
            sorted(
                Counter((d[:4] if d else "no annotations") for d in goa_latest.values()).items()
            )
        ),
        narrative_counts=dict(narrative_counts),
        narrative_reviews=narratives,
        cohorts=cohort_results,
    )


def write_report(root: Path, data: dict[str, Any], snapshot: ReviewSnapshot) -> None:
    """Write a linked report with explicit, non-interchangeable denominators."""
    base = root / "projects/PROTNLM_EVALUATION"
    summary = {"review_snapshot": {"commit": snapshot.commit, "date": snapshot.date}}
    (base / "benchmark-summary.json").write_text(
        json.dumps({**summary, **data}, indent=2) + "\n"
    )
    zero_go_count = data["records_with_zero_go_predictions"]
    zero_go_noun = "record" if zero_go_count == 1 else "records"
    assessed_count = data["records_with_go_assessments"]
    assessed_noun = "record" if assessed_count == 1 else "records"
    lines = [
        "---",
        "title: ProtNLM cross-cohort results",
        "---",
        "# Cross-cohort results",
        "",
        "[Project overview](../PROTNLM_EVALUATION.md) · [Source counts](benchmark-summary.json) · "
        "[Summary generator](build_benchmark_summary.py) · [Narrative category index](narrative-review-index.yaml)",
        "",
        f"Counts are a dated snapshot: as of {snapshot.date} (commit `{snapshot.short}`). "
        f"The scope contains **{data['distinct_records']} distinct protein records**, including "
        f"**{data['prediction_targets']} prediction targets** and 40 paired human reference records. "
        "Overlapping selections are counted once in the combined totals. These purposive, retrospective "
        "cohorts test informative biological distinctions; their proportions do not estimate proteome-wide accuracy.",
        "",
        f"**{data['prediction_targets_with_any_review']} of the {data['prediction_targets']} prediction targets "
        "have been assessed** at the time of this build: "
        f"{data['prediction_targets_with_go_review_file']} have a GO prediction-review YAML (including "
        f"{data['records_with_zero_go_predictions']} reviewed empty GO outputs) and "
        f"{data['prediction_targets_with_narrative_review_only']} have only a narrative function review. "
        f"The remaining {data['prediction_targets_without_any_review']} are selected but not yet reviewed "
        "and contribute nothing to any count below.",
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
        "### GO assessments by cohort",
        "",
        "**COR here means \"biologically supported and absent from the target's cached GOA/UniProt "
        "record\"**, not novelty with respect to the model's training data (the VDCL sense). COR is only "
        "available when the target record lacks the term, so a cohort's COR rate reflects its records' "
        "existing annotation, which terms its predictions emit, and how its reviewers drew the LSP/COR line, "
        "as much as the model. Model-organism cohorts, where a supported prediction is usually already "
        "present (CNN) or less specific than an existing annotation (LSP), have almost no COR. Annotation "
        "density alone does not explain the split (compare the median GOA column), so per-cohort COR rates "
        "should not be read as a property of the model. Cohort rows overlap, so they are not summed. "
        "The median cached-GOA column counts non-NOT rows in each GO-assessed target's `*-goa.tsv`.",
        "",
        "Latest annotation date in each target's cached GOA file (a lower bound on when the file was "
        "fetched): "
        + ", ".join(
            f"{year}: {n}" for year, n in data["cached_goa_latest_annotation_year"].items()
        )
        + ". ProtNLM2 was trained on UniProt 2023_04, so COR/CNN are judged against a GOA state "
        "that post-dates training, and a COR term may still have been learnable from annotated "
        "orthologs in the training release.",
        "",
        "| Cohort | GO claims | " + " | ".join(CODES) + " | COR share | Median cached GOA rows per target |",
        "|---|---:|" + "---:|" * len(CODES) + "---:|---:|",
    ]
    for row in data["cohorts"]:
        total = sum(row["go_counts"].values())
        if not total:
            continue
        share = f"{100 * row['go_counts']['COR'] / total:.0f}%"
        median = row["median_cached_goa_rows_per_go_assessed_record"]
        lines.append(
            f"| {row['cohort']} | {total} | "
            + " | ".join(str(row["go_counts"][c]) for c in CODES)
            + f" | {share} | {'n/a' if median is None else f'{median:g}'} |"
        )
    entailment = base / "cor-goa-entailment.tsv"
    if entailment.is_file():
        rel = list(csv.DictReader(entailment.open(), delimiter="\t"))
        counts = Counter(r["relation"] for r in rel)
        flagged = [r for r in rel if r["relation"] in ("EXACT", "ANCESTOR_SAME_ASPECT", "ANCESTOR_CROSS_ASPECT")]
        lines += [
            "",
            f"A mechanical is_a/part_of check of all {len(rel)} COR calls against each target's cached GOA "
            "([`cor_goa_entailment.py`](cor_goa_entailment.py), [TSV](cor-goa-entailment.tsv)) finds "
            + ", ".join(f"{k}: {v}" for k, v in sorted(counts.items()))
            + f". {len(flagged)} COR "
            + ("call is" if len(flagged) == 1 else "calls are")
            + " entailed by an existing target annotation and are candidates for LSP/CNN re-review"
            + (
                " ("
                + "; ".join(f"{r['gene']} {r['term_label']} via {r['via_labels']}" for r in flagged)
                + ")"
                if flagged
                else ""
            )
            + ". Entailment by an existing MF through relations outside go-basic, or by an InterPro2GO "
            "domain mapping, is not checked.",
        ]
    lines += [
        "",
        "## Reviewed records with no GO predictions",
        "",
        f"The {data['prediction_review_files']} prediction-review YAML files include "
        f"{zero_go_count} {zero_go_noun} with zero emitted GO predictions and "
        f"{assessed_count} {assessed_noun} with GO assessments. Completed `predictions: []` records "
        "with a summary evaluation document reviewed output absence; a missing review file is not counted as zero output. "
        "Their descriptions record the available evidence for potential missed functions. "
        "No VDCL category or confidence score is assigned to an absent prediction, and these records "
        "do not enter the emitted GO-claim denominator. Zero output alone does not establish a "
        "biological false negative or a recall estimate.",
        "",
        "| Gene | Accession | Summary evaluation |",
        "|---|---|---|",
    ]
    for row in sorted(data["zero_go_prediction_reviews"], key=lambda x: x["gene"]):
        lines.append(
            f"| {row['gene']} | {row['accession']} | "
            f"[Prediction review]({PUBLIC}{row['review_file']}) |"
        )
    lines += [
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
        "| Cohort | Records | Records with GO assessments | Reviewed zero GO output | Narrative review only | Not yet reviewed | GO claims | Narrative review records |",
        "|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in data["cohorts"]:
        lines.append(
            f"| {row['cohort']} | {row['records']} | {row['records_with_go_assessments']} | "
            f"{row['records_with_zero_go_predictions']} | {row['records_with_narrative_review_only']} | "
            f"{row['records_without_any_review']} | {sum(row['go_counts'].values())} | "
            f"{row['narrative_records']} |"
        )
    lines += [
        "",
        "Reference-pair rows (HORSE40_HUMAN_PAIR) are evidence records, not prediction targets, so their "
        "\"not yet reviewed\" count is zero by construction.",
    ]
    lines += [
        "",
        "## Source metadata",
        "",
        "In the JSON summary, `prediction_review_files` counts all review YAML files, including "
        "explicit empty records. `go_review_files` is retained as a legacy alias for that same "
        "total; `records_with_go_assessments` counts only records with emitted GO claims.",
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
    result = collect(review_snapshot_tree(repository), WorkingTree(repository))
    write_report(repository, result, declared_review_snapshot(repository))
    print(
        json.dumps(
            {
                k: v
                for k, v in result.items()
                if k
                not in ("narrative_reviews", "zero_go_prediction_reviews", "cohorts")
            },
            indent=2,
        )
    )
