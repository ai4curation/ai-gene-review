"""Export immunity predictions into AIGR-compatible review files."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

import yaml

from ai_gene_review.prok_immunity_prediction.classifier import load_family_config
from ai_gene_review.prok_immunity_prediction.models import FamilyDefinition, ProteinPrediction

MORDRET_REFERENCE = {
    "id": "doi:10.1126/science.adv8275",
    "title": "Mordret et al. 2026. Protein and genomic language models uncover the unexplored diversity of bacterial immunity systems.",
}

TOOL_REFERENCES = {
    "DefenseFinder": {
        "id": "doi:10.1038/s41467-022-30269-9",
        "title": "Systematic and quantitative view of the antiviral arsenal of prokaryotes (Tesson et al. 2022)",
    },
    "PADLOC": {
        "id": "doi:10.1093/nar/gkab883",
        "title": "Identification and classification of antiviral defence systems in bacteria and archaea with PADLOC reveals new system types (Payne et al. 2021)",
    },
    "CasFinder": {
        "id": "doi:10.1093/nar/gky425",
        "title": "CRISPRCasFinder, an update of CRISRFinder, includes a portable version, enhanced performance and integrates search for Cas proteins (Couvin et al. 2018)",
    },
}


def export_predictions_to_aigr(
    predictions: list[ProteinPrediction],
    family_config_path: Path,
    output_root: Path,
    organism_code: str,
    taxon_id: str,
    source_documents: list[Path],
    min_export_score: float = 0.55,
) -> Path:
    """Write one PredictionReview YAML per exported protein."""
    output_root.mkdir(parents=True, exist_ok=True)
    genes_root = output_root / "genes" / organism_code
    genes_root.mkdir(parents=True, exist_ok=True)
    families = load_family_config(family_config_path)
    manifest_rows: list[dict[str, str]] = []

    for prediction in predictions:
        if (
            prediction.best_family is None
            and not prediction.predicted_novel
            and prediction.family_confidence < min_export_score
        ):
            continue

        protein = prediction.protein
        gene_name = sanitize_name(protein.display_name)
        gene_dir = genes_root / gene_name
        gene_dir.mkdir(parents=True, exist_ok=True)
        yaml_path = gene_dir / f"{gene_name}-predictions-review.yaml"
        yaml_data = build_prediction_review(
            prediction=prediction,
            family=families.get(prediction.best_family or "", None),
            taxon_id=taxon_id,
            source_documents=source_documents,
        )
        yaml_path.write_text(
            yaml.safe_dump(yaml_data, sort_keys=False, allow_unicode=True),
            encoding="utf-8",
        )
        manifest_rows.append(
            {
                "gene_symbol": gene_name,
                "protein_id": protein.protein_id,
                "predicted_family": prediction.best_family or "",
                "predicted_novel": str(prediction.predicted_novel).lower(),
                "yaml_path": str(yaml_path),
            }
        )

    manifest_path = output_root / "aigr_manifest.json"
    manifest_path.write_text(json.dumps(manifest_rows, indent=2), encoding="utf-8")
    return manifest_path


def build_prediction_review(
    prediction: ProteinPrediction,
    family: FamilyDefinition | None,
    taxon_id: str,
    source_documents: list[Path],
) -> dict[str, object]:
    """Build a PredictionReview YAML document."""
    protein = prediction.protein
    assessment, confidence_score = determine_assessment(prediction)
    family_name = family.name if family else (prediction.best_family or "Novel defense candidate")
    term_id = family.term_id if family else "DEFENSE:NOVEL_CANDIDATE"
    references = [MORDRET_REFERENCE]
    used_databases = sorted({hit.database for hit in prediction.external_hits})
    for database in used_databases:
        tool_reference = TOOL_REFERENCES.get(database)
        if tool_reference:
            references.append(tool_reference)

    summary = " ".join(prediction.evidence) or (
        f"Predicted {family_name} with confidence {prediction.family_confidence:.2f}."
    )
    generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    return {
        "id": protein.protein_id,
        "gene_symbol": protein.display_name,
        "locus_tag": protein.locus_tag,
        "taxon": {
            "id": taxon_id,
            "label": taxon_id,
        },
        "status": "DRAFT",
        "description": (
            f"Prokaryotic immunity prediction generated {generated_at}. "
            f"Best family={family_name}; defense_score={prediction.defense_score:.2f}; "
            f"novel_score={prediction.novel_score:.2f}."
        ),
        "references": references,
        "source_documents": [str(path) for path in source_documents],
        "predictions": [
            {
                "source_method": "prok-immunity-prediction",
                "source_version": "initial-architecture",
                "source_reference_id": MORDRET_REFERENCE["id"],
                "predicted_term": {
                    "id": term_id,
                    "label": family_name,
                },
                "predicted_term_type": "DEFENSE_SYSTEM",
                "review": {
                    "assessment": assessment,
                    "confidence_score": confidence_score,
                    "summary": summary,
                },
            }
        ],
    }


def determine_assessment(prediction: ProteinPrediction) -> tuple[str, int]:
    """Translate pipeline confidence into the existing PredictionAssessment enum."""
    if prediction.external_hits:
        return "CNN", 2
    if prediction.predicted_novel:
        return "UNC", 1
    if prediction.best_family:
        return "UNC", 1
    return "UNC", 1


def sanitize_name(name: str) -> str:
    """Produce a filesystem-safe gene symbol fallback."""
    return name.replace("/", "_").replace(" ", "_")
