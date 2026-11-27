"""Tests for time-split benchmark building, checks, export and scoring (no network).

Tests over the benchmarks committed in ai-gene-review are in that repository's
``tests/test_benchmark_committed.py``.
"""

from __future__ import annotations

import json
import random
from pathlib import Path

import pytest
import yaml
from typer.testing import CliRunner

from aigr_benchmark.build import (
    add_decoys,
    collapse_rows,
    goa_candidates,
    make_item,
    review_targets,
)
from aigr_benchmark.checks import (
    Context,
    difficulty,
    grading_results,
    homolog_leakage,
    knowledge_category,
    near_duplicate,
    novelty,
    prior_prediction,
    run_checks,
    SCHEMA,
    validate_schema,
)
from aigr_benchmark.cli import benchmark_app
from aigr_benchmark.importers import peptalk as peptalk_importer
from aigr_benchmark.importers import reviews as reviews_importer
from aigr_benchmark.predictions import read_prediction_set, verdicts
from aigr_benchmark.run import export, score
from aigr_benchmark.sources import (
    Annotation,
    InformationContent,
    Ontology,
    by_protein,
)


#: The installed package folder, which holds the schema and generated models.
PACKAGE = SCHEMA.parents[1]

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
            "UniProtKB:P6": "PTHR2:SF1",
            "UniProtKB:P3": "PTHR3:SF1",
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
        {"name": "blind", "context": "BLIND", "shuffle_control": True},
        {"name": "agent-review", "context": "AGENT_REVIEW"},
    ],
    "predictors": [
        {"name": "peptalk:m1", "model": "m1", "model_training_cutoff": "2025-01-01"},
        {"name": "ai-gene-review:m1"},
        {"name": "ai-gene-review"},
        {"name": "deepgo"},
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


def test_export_writes_generic_claims(ctx: Context, tmp_path: Path) -> None:
    benchmark = toy_benchmark(ctx, tmp_path)
    written, skipped = export(benchmark, ctx, tmp_path / "inputs")
    assert skipped == []
    assert (
        (tmp_path / "inputs" / "toy.fasta").read_text().startswith(">sp|P1|GP1_HUMAN")
    )
    assert (tmp_path / "inputs" / "baseline-goa" / "P1-goa.tsv") in written
    claimset = yaml.safe_load((tmp_path / "inputs" / "toy-claims.yaml").read_text())
    assert validate_schema(claimset, "ClaimSet") == []
    # a claim never reveals whether its term is a target, NOT target or decoy
    assert all("role" not in c and "negated" not in c for c in claimset["claims"])
    asked = {
        (i["id"], t["term"]["id"])
        for i in benchmark["items"]
        for t in i["target_annotations"] + i.get("decoys", [])
    }
    assert {(c["item_id"], c["term"]["id"]) for c in claimset["claims"]} == asked


PEPTALK_RECORDS: list[dict] = [
    {
        "uid": "u1",
        "id": "sp|P1|GP1_HUMAN",
        "task": "ask-function",
        "context": "blind",
        "model": "m1",
        "condition": "real",
        "params": {"term": "GO:0106310"},
        "answer": {"verdict": "yes", "reason": "kinase domain"},
        "cost_usd": 0.01,
    },
    {
        "uid": "u2",
        "id": "sp|P1|GP1_HUMAN",
        "task": "ask-function",
        "context": "blind",
        "model": "m1",
        "condition": "shuffled",
        "params": {"term": "GO:0106310"},
        "answer": "{'verdict': 'no'}",
    },
    {
        "uid": "u3",
        "id": "sp|P6|GP6_HUMAN",
        "task": "ask-function",
        "context": "blind",
        "model": "m1",
        "condition": "real",
        "params": {"term": "GO:0004672"},
        "answer": {"verdict": None},
    },
]


def test_peptalk_importer_and_score(ctx: Context, tmp_path: Path) -> None:
    benchmark = toy_benchmark(ctx, tmp_path)
    records = [(tmp_path / "blind.jsonl", r) for r in PEPTALK_RECORDS]
    predictions = peptalk_importer.predictions(benchmark, records)
    assert (
        validate_schema(
            {"benchmark_id": "toy", "predictions": predictions}, "PredictionSet"
        )
        == []
    )
    assert {p["predictor"] for p in predictions} == {"peptalk:m1"}
    assert [p["sequence_control"] for p in predictions] == [
        "NATIVE",
        "SHUFFLED",
        "NATIVE",
    ]
    report = score(benchmark, verdicts(benchmark, predictions), ["stub"])
    assert validate_schema(report, "ScoreReport") == []
    rows = {(r["condition"], r["role"]): r for r in report["condition_scores"]}
    assert rows[("blind", "TARGET")]["n_yes"] == 1
    assert rows[("blind", "SHUFFLED_TARGET")]["n_no"] == 1
    assert rows[("blind", "NEGATED_TARGET")]["n_missing"] == 1
    assert {r["predictor"] for r in report["condition_scores"]} == {"peptalk:m1"}


def test_peptalk_claims_tsv_round_trip(ctx: Context, tmp_path: Path) -> None:
    from aigr_benchmark.predictions import claims

    benchmark = toy_benchmark(ctx, tmp_path)
    lines = peptalk_importer.claims_tsv(claims(benchmark["items"])).splitlines()
    assert lines[0].split("\t") == [
        "id",
        "task",
        "term",
        "label",
        "position",
        "residue",
    ]
    assert len(lines) - 1 == len(claims(benchmark["items"]))


def test_predictions_on_unknown_claims_are_rejected(
    ctx: Context, tmp_path: Path
) -> None:
    benchmark = toy_benchmark(ctx, tmp_path)
    bad = {
        "item_id": "toy-P1",
        "term": "GO:0005634",
        "predictor": "x",
        "condition": "c",
    }
    with pytest.raises(ValueError, match="matches no claim"):
        verdicts(benchmark, [bad])


@pytest.mark.parametrize(
    "prediction,threshold,expected",
    [
        ({"verdict": "no", "score": 0.9}, 0.5, "no"),  # an explicit verdict wins
        ({"score": 0.9}, None, "missing"),  # a bare score needs a threshold
        ({"score": 0.9}, 0.5, "yes"),
        ({"score": 0.1}, 0.5, "no"),
    ],
)
def test_score_only_predictions(
    ctx: Context,
    tmp_path: Path,
    prediction: dict,
    threshold: float | None,
    expected: str,
) -> None:
    benchmark = toy_benchmark(ctx, tmp_path)
    record = {
        "item_id": "toy-P1",
        "claim_id": "toy-P1/GO:0106310",
        "predictor": "deepgo",
        "condition": "blind",
        **prediction,
    }
    assert verdicts(benchmark, [record], threshold) == {
        ("blind", "deepgo", "toy-P1", "GO:0106310"): expected
    }


@pytest.mark.parametrize(
    "overrides, message",
    [
        ({"claim_id": "other/GO:0106310"}, "claim_id"),
        ({"claim_id": "toy-P1/GO:2"}, "claim_id"),
        ({"term": None, "claim_id": "missing-separator"}, "claim_id"),
        ({"term": None}, "claim_id or term"),
        ({"condition": "blnid"}, "unknown condition"),
        ({"context": "FULL"}, "disagrees with condition"),
    ],
)
def test_prediction_identifiers(ctx, tmp_path, overrides, message):
    benchmark = toy_benchmark(ctx, tmp_path)
    record = {
        "item_id": "toy-P1",
        "term": "GO:0106310",
        "condition": "blind",
        "predictor": "deepgo",
        **overrides,
    }
    with pytest.raises(ValueError, match=message):
        verdicts(benchmark, [record])


def test_prediction_needs_term_or_claim_in_schema():
    record = {
        "item_id": "x",
        "condition": "blind",
        "predictor": "test",
        "verdict": "yes",
    }
    assert validate_schema(record, "Prediction")
    assert validate_schema({"predictions": [record]}, "PredictionSet")


def test_undeclared_predictors_are_reported(ctx, tmp_path, caplog):
    benchmark = toy_benchmark(ctx, tmp_path)
    benchmark["spec"] = {
        k: v for k, v in benchmark["spec"].items() if k != "predictors"
    }
    report = run_checks(benchmark, ctx, tmp_path, uniprot=False)
    assert (
        next(r for r in report["summary"] if r["check"] == "reference_recency")["info"]
        == 1
    )
    record = {
        "item_id": "toy-P1",
        "term": "GO:0106310",
        "condition": "blind",
        "predictor": "new",
    }
    assert verdicts(benchmark, [record])
    benchmark["spec"] = SPEC
    assert verdicts(benchmark, [record])
    assert "Predictor 'new' is absent from the spec" in caplog.text


def test_peptalk_unknown_context(ctx, tmp_path):
    benchmark = toy_benchmark(ctx, tmp_path)
    with pytest.raises(ValueError, match="no declared condition"):
        peptalk_importer.predictions(
            benchmark,
            [(tmp_path / "run", {**PEPTALK_RECORDS[0], "context": "organism"})],
        )


def test_score_checks_each_yaml_input(ctx, tmp_path):
    benchmark = toy_benchmark(ctx, tmp_path)
    bench_file = tmp_path / "toy.yaml"
    bench_file.write_text(yaml.safe_dump(benchmark))
    path = tmp_path / "run.yaml"
    document = """benchmark_id: toy
predictions:
  - item_id: toy-P1
    term: GO:0106310
    prediction_date: 2026-11-26
    condition: blind
    predictor: deepgo
    verdict: "yes"
"""
    path.write_text(document)
    runner = CliRunner()
    args = ["score", str(bench_file), "-p", str(path)]
    assert runner.invoke(benchmark_app, args).exit_code == 0
    for args_, content, error in [
        (args + ["-p", str(path)], document, "duplicate prediction"),
        (args, document + document.split("predictions:\n")[1], "duplicate prediction"),
        (
            args,
            document.replace("benchmark_id: toy", "benchmark_id: other"),
            "benchmark_id",
        ),
        (args, bench_file.read_text(), "expected a PredictionSet"),
    ]:
        path.write_text(content)
        result = runner.invoke(benchmark_app, args_)
        assert result.exit_code != 0
        assert error in result.output


@pytest.mark.parametrize("suffix", [".jsonl", ".yaml"])
def test_import_and_score_cli(ctx: Context, tmp_path: Path, suffix: str) -> None:
    """End to end through the CLI: native peptalk output -> predictions -> scores."""
    benchmark = toy_benchmark(ctx, tmp_path)
    bench_file = tmp_path / "toy.yaml"
    bench_file.write_text(yaml.safe_dump(benchmark))
    native = tmp_path / "blind.jsonl"
    native.write_text("".join(json.dumps(r) + "\n" for r in PEPTALK_RECORDS))
    out = tmp_path / f"blind-peptalk-m1{suffix}"
    runner = CliRunner()
    result = runner.invoke(
        benchmark_app,
        ["import", str(bench_file), str(native), "--from", "peptalk", "-o", str(out)],
    )
    assert result.exit_code == 0, result.output
    assert len(read_prediction_set(out)["predictions"]) == 3
    result = runner.invoke(
        benchmark_app, ["validate", str(out), "--class", "PredictionSet"]
    )
    assert result.exit_code == 0, result.output
    result = runner.invoke(benchmark_app, ["score", str(bench_file), "-p", str(out)])
    assert result.exit_code == 0, result.output
    report = yaml.safe_load((tmp_path / "toy-scores.yaml").read_text())
    assert report["inputs"][0].startswith(str(out))


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
    predictions = reviews_importer.predictions(
        benchmark, ctx, tmp_path, "agent-review", "ai-gene-review:m1", "m1"
    )
    assert (
        validate_schema(
            {"benchmark_id": "toy", "predictions": predictions}, "PredictionSet"
        )
        == []
    )
    found = verdicts(benchmark, predictions)
    assert found[("agent-review", "ai-gene-review:m1", "toy-P1", "GO:0106310")] == "yes"
    decoys = {
        (item["id"], d["term"]["id"])
        for item in benchmark["items"]
        for d in item.get("decoys", [])
    }
    # a review is never asked about decoys, so it makes no prediction on them
    assert not {(p["item_id"], p["term"]) for p in predictions} & decoys


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
    benchmark = toy_benchmark(ctx, tmp_path)
    predictions = reviews_importer.predictions(
        benchmark, ctx, tmp_path, "agent-review", "ai-gene-review"
    )
    assert (
        verdicts(benchmark, predictions)[
            ("agent-review", "ai-gene-review", "toy-P1", "GO:0106310")
        ]
        == "yes"
    )


def test_date_filter_drops_targets_with_any_old_reference(
    ctx: Context, tmp_path: Path
) -> None:
    from aigr_benchmark.build import date_filtered

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
    from aigr_benchmark.sources import uniprot_stream

    folder = tmp_path / "uniprot"
    folder.mkdir()
    import hashlib

    for query, accession in (("q1", "P1"), ("q2", "P2")):
        key = hashlib.sha256(f"{query}\tf".encode()).hexdigest()[:12]
        (folder / f"feat-{key}.tsv").write_text(f"Entry\n{accession}\n")
        (folder / f"feat-{key}.release").write_text("2026_04")
    assert uniprot_stream("q1", "f", tmp_path, "feat")[0] == [{"Entry": "P1"}]
    assert uniprot_stream("q2", "f", tmp_path, "feat")[0] == [{"Entry": "P2"}]


def test_homolog_check_without_other_members_is_info(ctx: Context) -> None:
    # P3 is alone in its subfamily, P7 has none: nothing to check either way
    assert homolog_leakage(ctx, "UniProtKB:P3", "GO:0004713")["status"] == "INFO"
    assert homolog_leakage(ctx, "UniProtKB:P7", "GO:0004713")["status"] == "INFO"


def test_decoys_follow_target_aspects(ctx: Context) -> None:
    from aigr_benchmark.build import aspect_matched

    item = {"target_annotations": [{"aspect": "C"}]}
    eligible = [("GO:0004713", "a"), ("GO:0005634", "b")]
    assert aspect_matched(ctx, item, eligible, 1, random.Random(0)) == [
        ("GO:0005634", "b")
    ]


@pytest.mark.parametrize(
    "generator,committed",
    [
        ("gen-json-schema", PACKAGE / "schema" / "benchmark.schema.json"),
        ("gen-pydantic", PACKAGE / "datamodel" / "benchmark_model.py"),
    ],
)
def test_generated_benchmark_models_are_current(generator: str, committed: Path) -> None:
    """Regenerate with `just gen-benchmark-models` after editing schema/benchmark.yaml."""
    import shutil
    import subprocess

    pytest.importorskip("linkml", reason="LinkML is a dev dependency")
    exe = shutil.which(generator)
    assert exe, f"{generator} not installed"
    out = subprocess.run(
        [exe, str(SCHEMA.relative_to(PACKAGE.parent))],
        cwd=PACKAGE.parent,
        capture_output=True,
        text=True,
        check=True,
    ).stdout
    assert out == committed.read_text()


@pytest.mark.parametrize(
    "target_class,document",
    [
        ("CheckResult", {"check": "novelty", "status": "PASS", "message": "ok"}),
        ("CheckResult", {"check": "novelty", "status": "MAYBE", "message": "ok"}),
        ("CheckResult", {"check": "novelty", "status": "PASS"}),
        ("CheckResult", {"check": "novelty", "status": "PASS", "message": "ok", "extra": 1}),
        ("Prediction", {"item_id": "B-P1", "predictor": "p", "condition": "blind"}),
        ("PredictionSet", {"predictions": [{"item_id": "B-P1", "verdict": "maybe"}]}),
    ],
)
def test_validate_schema_matches_linkml(target_class: str, document: dict) -> None:
    """The bundled JSON Schema gives the errors LinkML's closed validator gives.

    Only their order may differ: the committed JSON Schema has sorted keys.
    """
    pytest.importorskip("linkml", reason="LinkML is a dev dependency")
    from linkml.validator import Validator
    from linkml.validator.plugins import JsonschemaValidationPlugin

    validator = Validator(
        str(SCHEMA), validation_plugins=[JsonschemaValidationPlugin(closed=True)]
    )
    expected = [r.message for r in validator.validate(document, target_class).results]
    assert sorted(validate_schema(document, target_class)) == sorted(expected)


def test_validate_schema_rejects_unknown_class() -> None:
    with pytest.raises(ValueError, match="not a class"):
        validate_schema({}, "NoSuchClass")


def test_cli_entry_point_help() -> None:
    result = CliRunner().invoke(benchmark_app, ["--help"])
    assert result.exit_code == 0
    for command in ("build", "check", "export", "import", "score", "validate"):
        assert command in result.output
