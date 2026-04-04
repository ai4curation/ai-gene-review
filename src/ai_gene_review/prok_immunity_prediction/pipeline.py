"""End-to-end pipeline for prokaryotic immunity prediction."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import pandas as pd

from ai_gene_review.prok_immunity_prediction.aigr_export import export_predictions_to_aigr
from ai_gene_review.prok_immunity_prediction.classifier import classify_proteins, load_family_config
from ai_gene_review.prok_immunity_prediction.cross_reference import gather_cross_reference_hits
from ai_gene_review.prok_immunity_prediction.embeddings import build_embedder
from ai_gene_review.prok_immunity_prediction.io import prepare_analysis_inputs


def run_pipeline(
    input_path: Path,
    output_dir: Path,
    family_config_path: Path,
    organism_code: str,
    taxon_id: str,
    gff_path: Path | None = None,
    embedder_name: str = "esm2",
    model_name: str = "facebook/esm2_t6_8M_UR50D",
    prodigal_mode: str = "single",
    defense_finder_dir: Path | None = None,
    padloc_dir: Path | None = None,
    casfinder_dir: Path | None = None,
    run_external: bool = True,
    export_aigr_root: Path | None = None,
    family_threshold: float = 0.55,
    novel_threshold: float = 0.62,
    neighborhood_window: int = 10,
) -> dict[str, Any]:
    """Run the immunity pipeline and materialize project outputs."""
    output_dir = output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    prepared = prepare_analysis_inputs(
        input_path=input_path,
        output_dir=output_dir,
        gff_path=gff_path,
        prodigal_mode=prodigal_mode,
    )
    embedder = build_embedder(embedder_name, model_name=model_name)
    embeddings = embedder.embed_many(prepared.proteins)
    families = load_family_config(family_config_path)
    external_hits = gather_cross_reference_hits(
        prepared=prepared,
        output_dir=output_dir / "cross_reference",
        defense_finder_dir=defense_finder_dir,
        padloc_dir=padloc_dir,
        casfinder_dir=casfinder_dir,
        run_missing=run_external,
    )
    predictions = classify_proteins(
        prepared=prepared,
        embeddings=embeddings,
        external_hits=external_hits,
        families=families,
        family_threshold=family_threshold,
        novel_threshold=novel_threshold,
        neighborhood_window=neighborhood_window,
    )

    predictions_path = write_predictions_table(predictions, output_dir / "predictions.tsv")
    external_hits_path = write_external_hits_table(external_hits, output_dir / "cross_reference_hits.tsv")
    source_documents = [predictions_path, external_hits_path]
    if prepared.gff_path is not None and prepared.gff_path != prepared.faa_path:
        source_documents.append(prepared.gff_path)
    source_documents.append(prepared.faa_path)

    summary = {
        "n_proteins": len(prepared.proteins),
        "n_cross_reference_hits": len(external_hits),
        "n_known_family_predictions": sum(1 for prediction in predictions if prediction.best_family),
        "n_novel_candidates": sum(1 for prediction in predictions if prediction.predicted_novel),
        "embedder": embedder_name,
        "model_name": model_name,
        "input_path": str(input_path.resolve()),
        "output_dir": str(output_dir),
        "notes": prepared.notes,
    }

    manifest_path = None
    if export_aigr_root is not None:
        manifest_path = export_predictions_to_aigr(
            predictions=predictions,
            family_config_path=family_config_path,
            output_root=export_aigr_root,
            organism_code=organism_code,
            taxon_id=taxon_id,
            source_documents=source_documents,
        )
        summary["aigr_manifest"] = str(manifest_path)

    summary_path = output_dir / "summary.json"
    summary_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    return summary


def write_predictions_table(predictions: list[Any], output_path: Path) -> Path:
    """Write the main per-protein prediction table."""
    rows: list[dict[str, Any]] = []
    for prediction in predictions:
        rows.append(
            {
                "protein_id": prediction.protein.protein_id,
                "gene_symbol": prediction.protein.gene_symbol or "",
                "locus_tag": prediction.protein.locus_tag or "",
                "display_name": prediction.protein.display_name,
                "contig": prediction.protein.contig or "",
                "index": prediction.protein.index,
                "predicted_family": prediction.best_family or "",
                "family_confidence": round(prediction.family_confidence, 4),
                "defense_score": round(prediction.defense_score, 4),
                "neighborhood_score": round(prediction.neighborhood_score, 4),
                "novel_score": round(prediction.novel_score, 4),
                "predicted_novel": prediction.predicted_novel,
                "external_databases": ",".join(sorted({hit.database for hit in prediction.external_hits})),
                "evidence": " | ".join(prediction.evidence),
            }
        )
    pd.DataFrame(rows).to_csv(output_path, sep="\t", index=False)
    return output_path


def write_external_hits_table(external_hits: list[Any], output_path: Path) -> Path:
    """Write a flat table of external-tool evidence."""
    rows = [
        {
            "database": hit.database,
            "protein_id": hit.protein_id,
            "system": hit.system,
            "subtype": hit.subtype or "",
            "raw_label": hit.raw_label or "",
        }
        for hit in external_hits
    ]
    pd.DataFrame(rows).to_csv(output_path, sep="\t", index=False)
    return output_path
