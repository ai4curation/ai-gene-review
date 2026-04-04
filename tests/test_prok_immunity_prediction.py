"""Tests for the prokaryotic immunity prediction project."""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
import yaml

from ai_gene_review.prok_immunity_prediction.aigr_export import export_predictions_to_aigr
from ai_gene_review.prok_immunity_prediction.classifier import classify_proteins, load_family_config
from ai_gene_review.prok_immunity_prediction.evaluation import evaluate_predictions
from ai_gene_review.prok_immunity_prediction.io import prepare_analysis_inputs
from ai_gene_review.prok_immunity_prediction.models import ExternalHit


PROJECT_DIR = Path("projects/prok-immunity-prediction")
EXAMPLE_FASTA = PROJECT_DIR / "data/example/example_proteome.faa"
EXAMPLE_GFF = PROJECT_DIR / "data/example/example_annotations.gff"
FAMILY_CONFIG = PROJECT_DIR / "config/defense_families.yaml"


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
