"""Tests for the prokaryotic immunity prediction project."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd
import yaml
from typer.testing import CliRunner

from ai_gene_review.cli import app as root_cli_app
from ai_gene_review.prok_immunity_prediction.aigr_export import export_predictions_to_aigr
from ai_gene_review.prok_immunity_prediction.classifier import classify_proteins, load_family_config
from ai_gene_review.prok_immunity_prediction.cross_reference import parse_defense_finder, parse_padloc
from ai_gene_review.prok_immunity_prediction.evaluation import (
    evaluate_predictions,
    evaluate_predictions_against_database,
    load_predictions_table,
)
from ai_gene_review.prok_immunity_prediction.io import prepare_analysis_inputs
from ai_gene_review.prok_immunity_prediction.pipeline import run_pipeline
from ai_gene_review.prok_immunity_prediction.models import ExternalHit


PROJECT_DIR = Path("projects/prok-immunity-prediction")
EXAMPLE_FASTA = PROJECT_DIR / "data/example/example_proteome.faa"
EXAMPLE_GFF = PROJECT_DIR / "data/example/example_annotations.gff"
FAMILY_CONFIG = PROJECT_DIR / "config/defense_families.yaml"
RUNNER = CliRunner()


def test_prepare_analysis_inputs_parses_example_proteome(tmp_path: Path) -> None:
    """Example FASTA + GFF should yield populated ProteinRecord metadata."""
    prepared = prepare_analysis_inputs(
        input_path=EXAMPLE_FASTA,
        output_dir=tmp_path,
        gff_path=EXAMPLE_GFF,
    )
    assert len(prepared.proteins) == 4
    assert prepared.proteins[0].gene_symbol == "casA"
    assert prepared.proteins[1].locus_tag == "LOCUS_0002"
    assert prepared.proteins[2].contig == "contig1"


def test_classify_proteins_uses_external_hits_and_novelty(tmp_path: Path) -> None:
    """Known hits should anchor the classifier and support novel candidate ranking."""
    prepared = prepare_analysis_inputs(
        input_path=EXAMPLE_FASTA,
        output_dir=tmp_path,
        gff_path=EXAMPLE_GFF,
    )
    embeddings = {
        "protA": np.array([1.0, 0.0], dtype=float),
        "protB": np.array([0.0, 1.0], dtype=float),
        "protC": np.array([0.7, 0.7], dtype=float),
        "protD": np.array([-1.0, 0.0], dtype=float),
    }
    families = load_family_config(FAMILY_CONFIG)
    external_hits = [
        ExternalHit(
            database="DefenseFinder",
            protein_id="protA",
            system="CRISPR-Cas",
            subtype="CAS_Class1-Subtype-I-E",
            raw_label="CAS_Class1-Subtype-I-E",
        ),
        ExternalHit(
            database="PADLOC",
            protein_id="protB",
            system="CBASS",
            raw_label="CBASS",
        ),
    ]

    predictions = classify_proteins(
        prepared=prepared,
        embeddings=embeddings,
        external_hits=external_hits,
        families=families,
        family_threshold=0.4,
        novel_threshold=0.5,
        neighborhood_window=5,
    )
    by_id = {prediction.protein.protein_id: prediction for prediction in predictions}

    assert by_id["protA"].best_family == "CRISPR-Cas"
    assert by_id["protB"].best_family == "CBASS"
    assert by_id["protC"].predicted_novel is True
    assert by_id["protD"].predicted_novel is False


def test_export_predictions_to_aigr_writes_prediction_review(tmp_path: Path) -> None:
    """Export should write DEFENSE_SYSTEM PredictionReview YAML files."""
    prepared = prepare_analysis_inputs(
        input_path=EXAMPLE_FASTA,
        output_dir=tmp_path / "run",
        gff_path=EXAMPLE_GFF,
    )
    embeddings = {
        "protA": np.array([1.0, 0.0], dtype=float),
        "protB": np.array([0.0, 1.0], dtype=float),
        "protC": np.array([0.7, 0.7], dtype=float),
        "protD": np.array([-1.0, 0.0], dtype=float),
    }
    families = load_family_config(FAMILY_CONFIG)
    predictions = classify_proteins(
        prepared=prepared,
        embeddings=embeddings,
        external_hits=[
            ExternalHit(
                database="DefenseFinder",
                protein_id="protA",
                system="CRISPR-Cas",
                subtype="CAS_Class1-Subtype-I-E",
                raw_label="CAS_Class1-Subtype-I-E",
            )
        ],
        families=families,
        family_threshold=0.4,
        novel_threshold=0.5,
        neighborhood_window=5,
    )

    source_document = tmp_path / "predictions.tsv"
    source_document.write_text("protein_id\tpredicted_family\nprotA\tCRISPR-Cas\n", encoding="utf-8")
    export_root = tmp_path / "export"
    manifest_path = export_predictions_to_aigr(
        predictions=predictions,
        family_config_path=FAMILY_CONFIG,
        output_root=export_root,
        organism_code="ECOLI",
        taxon_id="NCBITaxon:83333",
        source_documents=[source_document],
        min_export_score=0.4,
    )

    yaml_path = export_root / "genes/ECOLI/casA/casA-predictions-review.yaml"
    assert manifest_path.exists()
    assert yaml_path.exists()
    data = yaml.safe_load(yaml_path.read_text(encoding="utf-8"))
    assert data["predictions"][0]["predicted_term_type"] == "DEFENSE_SYSTEM"
    assert data["predictions"][0]["predicted_term"]["id"].startswith("DEFENSE:")


def test_evaluate_predictions_computes_basic_metrics(tmp_path: Path) -> None:
    """Evaluation should report precision and recall from normalized tables."""
    predictions_path = tmp_path / "predictions.tsv"
    benchmark_path = tmp_path / "benchmark.tsv"
    output_path = tmp_path / "metrics.json"

    pd.DataFrame(
        [
            {
                "protein_id": "protA",
                "predicted_family": "CRISPR-Cas",
                "family_confidence": 0.99,
                "predicted_novel": False,
            },
            {
                "protein_id": "protC",
                "predicted_family": "",
                "family_confidence": 0.0,
                "predicted_novel": True,
            },
        ]
    ).to_csv(predictions_path, sep="\t", index=False)

    pd.DataFrame(
        [
            {
                "protein_id": "protA",
                "is_defense": True,
                "family": "CRISPR-Cas",
                "is_novel": False,
            },
            {
                "protein_id": "protC",
                "is_defense": True,
                "family": "",
                "is_novel": True,
            },
            {
                "protein_id": "protD",
                "is_defense": False,
                "family": "",
                "is_novel": False,
            },
        ]
    ).to_csv(benchmark_path, sep="\t", index=False)

    metrics = evaluate_predictions(predictions_path, benchmark_path, output_path)
    assert metrics["precision"] == 1.0
    assert metrics["recall"] == 1.0
    assert metrics["novel_recall"] == 1.0
    assert output_path.exists()


def test_parse_defense_finder_systems_output(tmp_path: Path) -> None:
    """DefenseFinder systems output should expand multi-protein systems."""
    systems = tmp_path / "defense_finder_systems.tsv"
    systems.write_text(
        "\t".join(["sys_id", "type", "subtype", "protein_in_syst"]) + "\n"
        + "\t".join(["sys_1", "CRISPR-Cas", "CAS_Class1-Subtype-I-E", "protA,protB"])
        + "\n",
        encoding="utf-8",
    )
    hits = parse_defense_finder(tmp_path)
    assert [hit.protein_id for hit in hits] == ["protA", "protB"]
    assert all(hit.system == "CRISPR-Cas" for hit in hits)


def test_parse_defense_finder_alternate_system_columns(tmp_path: Path) -> None:
    """DefenseFinder parsing should tolerate alternate systems-table headers."""
    systems_path = tmp_path / "defense_finder_systems.tsv"
    pd.DataFrame(
        [
            {
                "system": "CBASS",
                "subtype": "cbass_type_i",
                "genes": "protC,protD",
            }
        ]
    ).to_csv(systems_path, sep="\t", index=False)
    hits = parse_defense_finder(tmp_path)
    assert [hit.protein_id for hit in hits] == ["protC", "protD"]
    assert all(hit.system == "CBASS" for hit in hits)


def test_parse_padloc_csv_output(tmp_path: Path) -> None:
    """PADLOC CSV output should map target names to ExternalHit rows."""
    csv_path = tmp_path / "sample_padloc.csv"
    pd.DataFrame(
        [
            {
                "target.name": "protB",
                "system": "CBASS",
                "protein.name": "cyclase",
            }
        ]
    ).to_csv(csv_path, index=False)
    hits = parse_padloc(tmp_path)
    assert len(hits) == 1
    assert hits[0].protein_id == "protB"
    assert hits[0].system == "CBASS"
    assert hits[0].subtype == "cyclase"


def test_run_pipeline_writes_outputs_with_database_dirs(tmp_path: Path) -> None:
    """A full pipeline run should consume provided DefenseFinder/PADLOC directories."""
    defensefinder_dir = tmp_path / "defensefinder"
    defensefinder_dir.mkdir()
    (defensefinder_dir / "defense_finder_systems.tsv").write_text(
        "\t".join(["sys_id", "type", "subtype", "protein_in_syst"]) + "\n"
        + "\t".join(["sys_1", "CRISPR-Cas", "CAS_Class1-Subtype-I-E", "protA"])
        + "\n",
        encoding="utf-8",
    )

    padloc_dir = tmp_path / "padloc"
    padloc_dir.mkdir()
    pd.DataFrame(
        [
            {
                "target.name": "protB",
                "system": "CBASS",
                "protein.name": "cyclase",
            }
        ]
    ).to_csv(padloc_dir / "sample_padloc.csv", index=False)

    output_dir = tmp_path / "pipeline-output"
    summary = run_pipeline(
        input_path=EXAMPLE_FASTA,
        output_dir=output_dir,
        family_config_path=FAMILY_CONFIG,
        organism_code="ECOLI",
        taxon_id="NCBITaxon:83333",
        gff_path=EXAMPLE_GFF,
        embedder_name="composition",
        defense_finder_dir=defensefinder_dir,
        padloc_dir=padloc_dir,
        run_external=False,
        family_threshold=0.4,
        novel_threshold=0.5,
        neighborhood_window=5,
    )
    predictions = pd.read_csv(output_dir / "predictions.tsv", sep="\t")
    assert summary["n_cross_reference_hits"] == 2
    assert summary["n_known_family_predictions"] >= 2
    assert set(predictions["predicted_family"]).issuperset({"CRISPR-Cas", "CBASS"})


def test_evaluate_predictions_against_database_outputs_metrics(tmp_path: Path) -> None:
    """Database comparison should compute metrics and emit a comparison TSV."""
    predictions_path = tmp_path / "predictions.tsv"
    pd.DataFrame(
        [
            {
                "protein_id": "protA",
                "predicted_family": "CRISPR-Cas",
                "family_confidence": 0.98,
                "predicted_novel": False,
            },
            {
                "protein_id": "protB",
                "predicted_family": "",
                "family_confidence": 0.0,
                "predicted_novel": False,
            },
            {
                "protein_id": "protC",
                "predicted_family": "CBASS",
                "family_confidence": 0.66,
                "predicted_novel": False,
            },
        ]
    ).to_csv(predictions_path, sep="\t", index=False)

    defensefinder_dir = tmp_path / "defensefinder"
    defensefinder_dir.mkdir()
    (defensefinder_dir / "defense_finder_systems.tsv").write_text(
        "\t".join(["sys_id", "type", "subtype", "protein_in_syst"]) + "\n"
        + "\t".join(["sys_1", "CRISPR-Cas", "CAS_Class1-Subtype-I-E", "protA"])
        + "\n"
        + "\t".join(["sys_2", "CBASS", "cbass_type_i", "protB"])
        + "\n",
        encoding="utf-8",
    )
    output_path = tmp_path / "defensefinder-eval.json"

    metrics = evaluate_predictions_against_database(
        predictions_path=predictions_path,
        database_dir=defensefinder_dir,
        database="defensefinder",
        family_config_path=FAMILY_CONFIG,
        output_path=output_path,
    )
    assert metrics["database"] == "DefenseFinder"
    assert metrics["true_positives"] == 1
    assert metrics["false_positives"] == 1
    assert metrics["false_negatives"] == 1
    assert metrics["precision"] == 0.5
    assert metrics["recall"] == 0.5
    assert output_path.exists()
    assert output_path.with_suffix(".comparison.tsv").exists()


def test_load_predictions_table_defaults_predicted_novel(tmp_path: Path) -> None:
    """Lean prediction exports should default predicted_novel to False."""
    predictions_path = tmp_path / "predictions.tsv"
    pd.DataFrame(
        [
            {
                "protein_id": "protA",
                "predicted_family": "CRISPR-Cas",
            }
        ]
    ).to_csv(predictions_path, sep="\t", index=False)
    predictions = load_predictions_table(predictions_path)
    assert list(predictions["predicted_novel"]) == [False]


def test_root_cli_exposes_prok_immunity_run_command(tmp_path: Path) -> None:
    """The main ai-gene-review CLI should expose the immunity pipeline subcommands."""
    output_dir = tmp_path / "cli-output"
    result = RUNNER.invoke(
        root_cli_app,
        [
            "prok-immunity",
            "run",
            "--input",
            str(EXAMPLE_FASTA),
            "--output-dir",
            str(output_dir),
            "--family-config",
            str(FAMILY_CONFIG),
            "--organism",
            "ECOLI",
            "--taxon-id",
            "NCBITaxon:83333",
            "--gff",
            str(EXAMPLE_GFF),
            "--embedder",
            "composition",
            "--skip-external",
            "--family-threshold",
            "0.4",
            "--novel-threshold",
            "0.5",
            "--neighborhood-window",
            "5",
        ],
    )
    assert result.exit_code == 0, result.stdout
    assert (output_dir / "predictions.tsv").exists()


def test_root_cli_exposes_prok_immunity_evaluation_commands(tmp_path: Path) -> None:
    """The main CLI should route benchmark and database evaluation commands."""
    predictions_path = tmp_path / "predictions.tsv"
    raw_benchmark_path = tmp_path / "raw-benchmark.csv"
    normalized_benchmark_path = tmp_path / "normalized-benchmark.tsv"
    evaluation_output_path = tmp_path / "evaluation.json"
    database_output_path = tmp_path / "defensefinder-evaluation.json"

    pd.DataFrame(
        [
            {
                "protein_id": "protA",
                "predicted_family": "CRISPR-Cas",
                "family_confidence": 0.99,
                "predicted_novel": False,
            },
            {
                "protein_id": "protB",
                "predicted_family": "",
                "family_confidence": 0.0,
                "predicted_novel": False,
            },
            {
                "protein_id": "protC",
                "predicted_family": "",
                "family_confidence": 0.0,
                "predicted_novel": True,
            },
        ]
    ).to_csv(predictions_path, sep="\t", index=False)
    pd.DataFrame(
        [
            {"protein": "protA", "label": "defense", "family": "CRISPR-Cas", "novel": "false"},
            {"protein": "protC", "label": "defense", "family": "", "novel": "true"},
            {"protein": "protD", "label": "negative", "family": "", "novel": "false"},
        ]
    ).to_csv(raw_benchmark_path, index=False)

    defensefinder_dir = tmp_path / "defensefinder"
    defensefinder_dir.mkdir()
    (defensefinder_dir / "defense_finder_systems.tsv").write_text(
        "\t".join(["sys_id", "type", "subtype", "protein_in_syst"]) + "\n"
        + "\t".join(["sys_1", "CRISPR-Cas", "CAS_Class1-Subtype-I-E", "protA"])
        + "\n"
        + "\t".join(["sys_2", "CBASS", "cbass_type_i", "protB"])
        + "\n",
        encoding="utf-8",
    )

    normalize_result = RUNNER.invoke(
        root_cli_app,
        [
            "prok-immunity",
            "normalize-benchmark",
            "--input",
            str(raw_benchmark_path),
            "--output",
            str(normalized_benchmark_path),
            "--protein-id-column",
            "protein",
            "--label-column",
            "label",
            "--family-column",
            "family",
            "--novel-column",
            "novel",
        ],
    )
    assert normalize_result.exit_code == 0, normalize_result.stdout
    assert normalized_benchmark_path.exists()

    evaluate_result = RUNNER.invoke(
        root_cli_app,
        [
            "prok-immunity",
            "evaluate",
            "--predictions",
            str(predictions_path),
            "--benchmark",
            str(normalized_benchmark_path),
            "--output",
            str(evaluation_output_path),
        ],
    )
    assert evaluate_result.exit_code == 0, evaluate_result.stdout
    assert evaluation_output_path.exists()
    evaluation_metrics = json.loads(evaluate_result.stdout)
    assert evaluation_metrics["precision"] == 1.0
    assert evaluation_metrics["recall"] == 1.0
    assert evaluation_metrics["novel_recall"] == 1.0

    database_result = RUNNER.invoke(
        root_cli_app,
        [
            "prok-immunity",
            "evaluate-database",
            "--predictions",
            str(predictions_path),
            "--database",
            "DefenseFinder",
            "--database-dir",
            str(defensefinder_dir),
            "--family-config",
            str(FAMILY_CONFIG),
            "--output",
            str(database_output_path),
        ],
    )
    assert database_result.exit_code == 0, database_result.stdout
    assert database_output_path.exists()
    assert database_output_path.with_suffix(".comparison.tsv").exists()
    database_metrics = json.loads(database_result.stdout)
    assert database_metrics["database"] == "DefenseFinder"
    assert database_metrics["precision"] == 0.5
    assert database_metrics["recall"] == 0.5


def test_readme_advertised_root_prok_immunity_commands_match_help() -> None:
    """README-advertised root CLI entrypoints should remain discoverable in help output."""
    readme_text = Path("README.md").read_text(encoding="utf-8")
    advertised_lines = [
        line.strip()
        for line in readme_text.splitlines()
        if line.strip().startswith("uv run ai-gene-review prok-immunity ")
    ]

    assert advertised_lines, "README should advertise root prok-immunity commands"

    advertised_tokens = {line.split()[4] for line in advertised_lines}
    assert "--help" in advertised_tokens

    root_help = RUNNER.invoke(root_cli_app, ["--help"])
    assert root_help.exit_code == 0, root_help.stdout
    assert "prok-immunity" in root_help.stdout

    prok_help = RUNNER.invoke(root_cli_app, ["prok-immunity", "--help"])
    assert prok_help.exit_code == 0, prok_help.stdout

    for subcommand in sorted(advertised_tokens - {"--help"}):
        assert subcommand in prok_help.stdout
