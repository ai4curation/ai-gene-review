"""Tests for time-split benchmark building, checks, export and scoring (no network)."""

from __future__ import annotations

import json
import random
from pathlib import Path

import pytest
import yaml
from typer.testing import CliRunner

from ai_gene_review.benchmark.build import (
    add_decoys,
    collapse_rows,
    goa_candidates,
    make_item,
    review_targets,
)
from ai_gene_review.benchmark.checks import (
    Context,
    difficulty,
    grading_results,
    homolog_leakage,
    knowledge_category,
    near_duplicate,
    novelty,
    prior_prediction,
    run_checks,
    validate_schema,
)
from ai_gene_review.benchmark.cli import benchmark_app
from ai_gene_review.benchmark.run import (
    claims_rows,
    export,
    peptalk_verdicts,
    review_verdicts,
    score,
)
from ai_gene_review.benchmark.sources import (
    Annotation,
    InformationContent,
    Ontology,
    by_protein,
)

EXAMPLE = Path("benchmarks/human-goa-2025-06")

# root F -> kinase -> {ser kinase, tyr kinase}; obsolete old kinase replaced by ser kinase
OBO = """
[Term]
id: GO:0003674
name: molecular_function
namespace: molecular_function

[Term]
id: GO:0004672
name: protein kinase activity
namespace: molecular_function
is_a: GO:0003674

[Term]
id: GO:0106310
name: protein serine kinase activity
namespace: molecular_function
is_a: GO:0004672

[Term]
id: GO:0004713
name: protein tyrosine kinase activity
namespace: molecular_function
is_a: GO:0004672

[Term]
id: GO:0000001
name: old kinase
namespace: molecular_function
is_obsolete: true
replaced_by: GO:0106310

[Term]
id: GO:0005575
name: cellular_component
namespace: cellular_component

[Term]
id: GO:0005634
name: nucleus
namespace: cellular_component
is_a: GO:0005575
"""


def gaf(
    protein: str,
    term: str,
    evidence: str,
    reference: str = "PMID:1",
    aspect: str = "F",
    qualifier: str = "enables",
    date: str = "20260101",
) -> Annotation:
    """Build an Annotation through the GAF parser."""
    acc = protein.split(":", 1)[1]
    line = "\t".join(
        [
            "UniProtKB",
            acc,
            f"G{acc}",
            qualifier,
            term,
            reference,
            evidence,
            "",
            aspect,
            f"protein {acc}",
            "",
            "protein",
            "taxon:9606",
            date,
            "UniProt",
        ]
    )
    return Annotation.from_gaf_line(line)


@pytest.fixture
def ctx() -> Context:
    """Baseline and current releases over the toy ontology."""
    onto = Ontology.parse(OBO.splitlines())
    baseline = [
        gaf("UniProtKB:P1", "GO:0004672", "IDA"),  # P1 knows kinase (general)
        gaf("UniProtKB:P2", "GO:0000001", "IDA"),  # P2 knows obsolete -> ser kinase
        gaf("UniProtKB:P3", "GO:0004713", "IBA"),  # P3 predicted tyr kinase only
        gaf("UniProtKB:P4", "GO:0106310", "IDA"),  # P4 homolog of P5
        gaf("UniProtKB:P6", "GO:0005634", "IDA", aspect="C"),  # P6 knows a CC term only
    ]
    current = baseline + [
        gaf("UniProtKB:P1", "GO:0106310", "IDA", "PMID:10"),
        gaf("UniProtKB:P1", "GO:0106310", "IMP", "PMID:11"),
        gaf("UniProtKB:P2", "GO:0106310", "EXP", "PMID:12"),
        gaf("UniProtKB:P3", "GO:0004713", "IDA", "PMID:13"),
        gaf("UniProtKB:P5", "GO:0106310", "IDA", "PMID:14"),
        gaf("UniProtKB:P6", "GO:0004672", "IDA", "PMID:15", qualifier="NOT|enables"),
        gaf("UniProtKB:P7", "GO:0004713", "IEA", "GO_REF:0000002"),
    ]
    base = by_protein(baseline)
    experimental = {
        p: {a.term for a in rows if a.experimental} for p, rows in base.items()
    }
    return Context(
        ontology=onto,
        baseline=base,
        current=by_protein(current),
        ic=InformationContent.from_terms(onto, experimental),
        subfamily={
            "UniProtKB:P1": "PTHR2:SF1",
            "UniProtKB:P4": "PTHR1:SF1",
            "UniProtKB:P5": "PTHR1:SF1",
        },
        cutoff="2025-06-01",
        excluded_terms=frozenset({"GO:0003674", "GO:0005575"}),
    )


@pytest.mark.parametrize(
    "protein,term,negated,status",
    [
        ("UniProtKB:P1", "GO:0106310", False, "PASS"),  # baseline only has the ancestor
        ("UniProtKB:P1", "GO:0004672", False, "FAIL"),  # exact term known
        ("UniProtKB:P2", "GO:0106310", False, "FAIL"),  # known through an obsolete id
        ("UniProtKB:P2", "GO:0004672", False, "FAIL"),  # descendant known
        ("UniProtKB:P3", "GO:0004713", False, "PASS"),  # only IBA at baseline
        ("UniProtKB:P6", "GO:0004672", True, "PASS"),  # NOT target, no baseline NOT
    ],
)
def test_novelty(
    ctx: Context, protein: str, term: str, negated: bool, status: str
) -> None:
    assert novelty(ctx, protein, term, negated)["status"] == status


def test_prior_prediction_homolog_and_difficulty(ctx: Context) -> None:
    assert prior_prediction(ctx, "UniProtKB:P3", "GO:0004713")["status"] == "WARN"
    assert homolog_leakage(ctx, "UniProtKB:P5", "GO:0106310")["status"] == "WARN"
    assert homolog_leakage(ctx, "UniProtKB:P1", "GO:0106310")["status"] == "PASS"
    assert difficulty(grading_results(ctx, "UniProtKB:P3", "GO:0004713")) == "EASY"


def test_near_duplicate_uses_lin(ctx: Context) -> None:
    ctx.near_duplicate_threshold = 0.5
    r = near_duplicate(ctx, "UniProtKB:P1", "GO:0106310")
    assert "GO:0004672" in r["message"]
    assert r["status"] == (
        "WARN" if ctx.ic.lin("GO:0004672", "GO:0106310") >= 0.5 else "PASS"
    )


@pytest.mark.parametrize(
    "protein,aspect,category",
    [
        ("UniProtKB:P5", "F", "NO_KNOWLEDGE"),
        ("UniProtKB:P6", "F", "LIMITED_KNOWLEDGE"),
        ("UniProtKB:P1", "F", "PARTIAL_KNOWLEDGE"),
    ],
)
def test_knowledge_category(
    ctx: Context, protein: str, aspect: str, category: str
) -> None:
    assert knowledge_category(ctx, protein, aspect) == category


SPEC = {
    "id": "toy",
    "title": "Toy",
    "taxon": {"id": "NCBITaxon:9606", "label": "Homo sapiens", "gaf_code": "HUMAN"},
    "cutoff_date": "2025-06-01",
    "baseline_release": "2025-06-01",
    "current_release": "2026-08-05",
    "size": 4,
    "include_negated": True,
    "decoys_per_item": 1,
    "seed": 1,
    "conditions": [
        {
            "name": "blind",
            "context": "BLIND",
            "tool": "peptalk",
            "task": "ask-function",
            "model": "m1",
            "model_training_cutoff": "2025-01-01",
        }
    ],
}


def test_candidates_filter_evidence_novelty_and_negation(ctx: Context) -> None:
    candidates = goa_candidates(ctx, SPEC)
    assert sorted(candidates) == [
        "UniProtKB:P1",
        "UniProtKB:P3",
        "UniProtKB:P5",
        "UniProtKB:P6",
    ]
    no_not = goa_candidates(ctx, {**SPEC, "include_negated": False})
    assert "UniProtKB:P6" not in no_not
    dates = {"10": "2026-01-01", "11": "2025-07-01"}
    targets = collapse_rows(ctx, candidates["UniProtKB:P1"], dates)
    assert len(targets) == 1
    # earliest-published reference represents the target; all are kept
    assert targets[0]["reference"] == "PMID:11"
    assert targets[0]["supporting_references"] == ["PMID:10", "PMID:11"]


def build_items(ctx: Context, tmp_path: Path) -> list[dict]:
    """Items for every candidate, with decoys and a sequence, as the builder makes them."""
    rng = random.Random(1)
    items = []
    for protein, rows in sorted(goa_candidates(ctx, SPEC).items()):
        item = make_item(
            ctx,
            SPEC,
            protein,
            rows[0].symbol,
            rows[0].name,
            collapse_rows(ctx, rows, {}),
            [],
            rng,
            tmp_path,
        )
        item.update(
            {
                "entry_name": f"{rows[0].symbol}_HUMAN",
                "sequence": "MKVL",
                "sequence_version": 1,
            }
        )
        items.append(item)
    add_decoys(ctx, SPEC, items, rng)
    return items


def toy_benchmark(ctx: Context, tmp_path: Path) -> dict:
    return {
        "id": "toy",
        "title": "Toy",
        "created": "2026-11-25",
        "spec": SPEC,
        "sources": [],
        "items": build_items(ctx, tmp_path),
    }


def test_decoys_are_unrelated_to_current_annotations(
    ctx: Context, tmp_path: Path
) -> None:
    items = build_items(ctx, tmp_path)
    for item in items:
        for decoy in item.get("decoys", []):
            term = decoy["term"]["id"]
            for a in ctx.current[item["protein"]]:
                assert term not in ctx.ontology.ancestors(ctx.ontology.resolve(a.term))
                assert ctx.ontology.resolve(a.term) not in ctx.ontology.ancestors(term)


def test_run_checks_report_validates(ctx: Context, tmp_path: Path) -> None:
    benchmark = toy_benchmark(ctx, tmp_path)
    assert validate_schema(benchmark, "Benchmark") == []
    report = run_checks(benchmark, ctx, tmp_path, uniprot=False)
    assert validate_schema(report, "CheckReport") == []
    statuses = {(r["check"], r.get("item_id"), r["status"]) for r in report["results"]}
    assert ("novelty", "toy-P1", "PASS") in statuses
    assert ("prior_prediction", "toy-P3", "WARN") in statuses
    failed = sum(s["failed"] for s in report["summary"])
    assert failed == 0


def test_check_catches_hand_edited_old_target(ctx: Context, tmp_path: Path) -> None:
    benchmark = toy_benchmark(ctx, tmp_path)
    item = next(i for i in benchmark["items"] if i["protein"] == "UniProtKB:P1")
    item["target_annotations"][0]["term"] = {
        "id": "GO:0004672",
        "label": "protein kinase activity",
    }
    report = run_checks(benchmark, ctx, tmp_path, uniprot=False)
    assert any(
        r["check"] == "novelty" and r["status"] == "FAIL" for r in report["results"]
    )


def test_export_and_score_peptalk(ctx: Context, tmp_path: Path) -> None:
    benchmark = toy_benchmark(ctx, tmp_path)
    written, skipped = export(benchmark, ctx, tmp_path / "inputs")
    assert skipped == []
    assert (
        (tmp_path / "inputs" / "toy.fasta").read_text().startswith(">sp|P1|GP1_HUMAN")
    )
    assert (tmp_path / "inputs" / "baseline-goa" / "P1-goa.tsv") in written
    header = claims_rows(benchmark["items"])[0]
    assert header.split("\t") == ["id", "task", "term", "label", "position", "residue"]
    records = [
        {
            "id": "sp|P1|GP1_HUMAN",
            "task": "ask-function",
            "context": "blind",
            "model": "m1",
            "condition": "real",
            "params": {"term": "GO:0106310"},
            "answer": {"verdict": "yes"},
        },
        {
            "id": "sp|P1|GP1_HUMAN",
            "task": "ask-function",
            "context": "blind",
            "model": "m1",
            "condition": "shuffled",
            "params": {"term": "GO:0106310"},
            "answer": {"verdict": "no"},
        },
        {
            "id": "sp|P6|GP6_HUMAN",
            "task": "ask-function",
            "context": "blind",
            "model": "m1",
            "condition": "real",
            "params": {"term": "GO:0004672"},
            "answer": {"verdict": None},
        },
    ]
    report = score(benchmark, peptalk_verdicts(benchmark, records), ["stub"])
    assert validate_schema(report, "ScoreReport") == []
    rows = {(r["condition"], r["role"]): r for r in report["condition_scores"]}
    assert rows[("blind", "TARGET")]["n_yes"] == 1
    assert rows[("blind", "SHUFFLED_TARGET")]["n_no"] == 1
    assert rows[("blind", "NEGATED_TARGET")]["n_missing"] == 1


def write_review(genes: Path, acc: str, symbol: str, rows: list[dict]) -> Path:
    path = genes / "human" / symbol / f"{symbol}-ai-review.yaml"
    path.parent.mkdir(parents=True)
    path.write_text(
        yaml.safe_dump({"id": acc, "gene_symbol": symbol, "existing_annotations": rows})
    )
    return path


def test_review_derived_targets_and_review_verdicts(
    ctx: Context, tmp_path: Path
) -> None:
    rows = [
        {
            "term": {"id": "GO:0106310"},
            "evidence_type": "IDA",
            "original_reference_id": "PMID:10",
            "review": {"action": "ACCEPT"},
        },
        {
            "term": {"id": "GO:0004672"},
            "evidence_type": "IDA",
            "original_reference_id": "PMID:1",
            "review": {"action": "ACCEPT"},
        },  # known at baseline: not new
        {
            "term": {"id": "GO:0004713"},
            "evidence_type": "IEA",
            "original_reference_id": "GO_REF:1",
            "review": {"action": "REMOVE"},
        },
    ]
    path = write_review(tmp_path, "P1", "GP1", rows)
    targets = review_targets(ctx, SPEC, yaml.safe_load(path.read_text()), path)
    assert [t["term"]["id"] for t in targets] == ["GO:0106310"]
    benchmark = toy_benchmark(ctx, tmp_path)
    verdicts = review_verdicts(benchmark, ctx, tmp_path, "agent-review")
    assert verdicts[("agent-review", "", "toy-P1", "GO:0106310")] == "yes"
    decoy_roles = {
        verdicts[("agent-review", "", item["id"], d["term"]["id"])]
        for item in benchmark["items"]
        if item["protein"] == "UniProtKB:P1"
        for d in item.get("decoys", [])
    }
    assert decoy_roles <= {"missing"}  # a review is never asked about decoys


def test_review_verdicts_count_modify_replacements(
    ctx: Context, tmp_path: Path
) -> None:
    rows = [
        {
            "term": {"id": "GO:0004672"},
            "evidence_type": "IEA",
            "original_reference_id": "GO_REF:1",
            "review": {
                "action": "MODIFY",
                "proposed_replacement_terms": [{"id": "GO:0106310"}],
            },
        }
    ]
    write_review(tmp_path, "P1", "GP1", rows)
    verdicts = review_verdicts(
        toy_benchmark(ctx, tmp_path), ctx, tmp_path, "agent-review"
    )
    assert verdicts[("agent-review", "", "toy-P1", "GO:0106310")] == "yes"


def test_date_filter_drops_targets_with_any_old_reference(
    ctx: Context, tmp_path: Path
) -> None:
    from ai_gene_review.benchmark.build import date_filtered

    (tmp_path / "pubmed-dates.json").write_text(
        json.dumps(
            {
                "10": "2026-01-01",
                "11": "2020-01-01",
                "12": "2026-02-01",
                "13": "2026-02-01",
                "14": "2026-02-01",
                "15": "2026-02-01",
            }
        )
    )
    kept = date_filtered(goa_candidates(ctx, SPEC), "2025-06-01", tmp_path)
    # P1's ser-kinase target has PMID:11 from 2020, so the whole target goes
    assert "UniProtKB:P1" not in kept
    assert "UniProtKB:P5" in kept


def test_uniprot_stream_cache_is_keyed_by_query(tmp_path: Path) -> None:
    from ai_gene_review.benchmark.sources import uniprot_stream

    folder = tmp_path / "uniprot"
    folder.mkdir()
    import hashlib

    for query, accession in (("q1", "P1"), ("q2", "P2")):
        key = hashlib.sha256(f"{query}\tf".encode()).hexdigest()[:12]
        (folder / f"feat-{key}.tsv").write_text(f"Entry\n{accession}\n")
        (folder / f"feat-{key}.release").write_text("2026_04")
    assert uniprot_stream("q1", "f", tmp_path, "feat")[0] == [{"Entry": "P1"}]
    assert uniprot_stream("q2", "f", tmp_path, "feat")[0] == [{"Entry": "P2"}]


def test_homolog_check_without_subfamily_is_info(ctx: Context) -> None:
    assert homolog_leakage(ctx, "UniProtKB:P3", "GO:0004713")["status"] == "INFO"


def test_decoys_follow_target_aspects(ctx: Context) -> None:
    from ai_gene_review.benchmark.build import aspect_matched

    item = {"target_annotations": [{"aspect": "C"}]}
    eligible = [("GO:0004713", "a"), ("GO:0005634", "b")]
    assert aspect_matched(ctx, item, eligible, 1, random.Random(0)) == [
        ("GO:0005634", "b")
    ]


SUFFIX_CLASSES = {
    "-spec.yaml": "BenchmarkSpec",
    "-check-report.yaml": "CheckReport",
    "-agent-evaluation.yaml": "AgentEvaluation",
    "-scores.yaml": "ScoreReport",
}


def committed_benchmark_files() -> list[tuple[Path, str]]:
    """Every committed benchmark document with its schema class."""
    out = []
    for path in sorted(Path("benchmarks").glob("*/*.yaml")):
        cls = next(
            (c for suffix, c in SUFFIX_CLASSES.items() if path.name.endswith(suffix)),
            None,
        )
        out.append(
            (path, cls or ("Benchmark" if path.stem == path.parent.name else ""))
        )
    return out


@pytest.mark.parametrize("path,cls", committed_benchmark_files(), ids=lambda v: str(v))
def test_committed_benchmark_files_validate(path: Path, cls: str) -> None:
    assert cls, f"{path} has no recognised benchmark file name"
    result = CliRunner().invoke(benchmark_app, ["validate", str(path), "--class", cls])
    assert result.exit_code == 0, result.output


def test_example_is_committed() -> None:
    names = {p.name for p, _ in committed_benchmark_files()}
    assert {"human-goa-2025-06.yaml", "human-goa-2025-06-check-report.yaml"} <= names


def test_example_report_has_no_failures() -> None:
    report = yaml.safe_load(
        (EXAMPLE / "human-goa-2025-06-check-report.yaml").read_text()
    )
    assert all(s["failed"] == 0 for s in report["summary"])
    assert json.dumps(report["stats"])  # serialisable
