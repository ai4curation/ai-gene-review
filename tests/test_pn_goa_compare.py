"""Tests for comparing proteostasis workbook annotations against GOA."""

from pathlib import Path

import pandas as pd

from ai_gene_review.tools.compare_pn_to_goa import (
    ProteostasisAnnotation,
    compare_annotation_to_goa,
    extract_match_keywords,
    load_proteostasis_annotations,
)
from ai_gene_review.validation.goa_validator import GOAAnnotation


def test_extract_match_keywords_removes_generic_tokens() -> None:
    """Keyword extraction should keep informative biology terms only."""
    annotation = ProteostasisAnnotation(
        order=1,
        gene_symbol="DNAJB1",
        gene_name="DnaJ heat shock protein family (Hsp40) member B1",
        branch="Cytonuclear proteostasis",
        class_name="Chaperone",
        group="HSP70 system",
        type_name="J-domain containing HSP70 cochaperone",
        subtype="(no Subtype)",
        notes="",
    )

    keywords = extract_match_keywords(annotation)

    assert "hsp70" in keywords
    assert "chaperone" in keywords
    assert "cochaperone" in keywords
    assert "system" not in keywords
    assert "subtype" not in keywords
    assert "proteostasis" not in keywords


def test_compare_annotation_to_goa_prefers_relevant_term() -> None:
    """The strongest GOA text hit should be surfaced for a PN row."""
    annotation = ProteostasisAnnotation(
        order=1,
        gene_symbol="DNAJB1",
        gene_name="DnaJ heat shock protein family (Hsp40) member B1",
        branch="Cytonuclear proteostasis",
        class_name="Chaperone",
        group="HSP70 system",
        type_name="J-domain containing HSP70 cochaperone",
        subtype="(no Subtype)",
        notes="",
    )

    goa_annotations = [
        GOAAnnotation(
            database="UniProtKB",
            db_object_id="P25685",
            db_object_symbol="DNAJB1",
            qualifier="",
            go_id="GO:0031072",
            go_term="heat shock protein binding",
            go_aspect="MF",
            evidence_code="IDA",
            evidence_type="ECO:0000314",
            reference="PMID:1",
            with_from="",
            taxon_id="NCBITaxon:9606",
            taxon_label="Homo sapiens",
            assigned_by="UniProt",
            annotation_extension="",
            date="20260408",
        ),
        GOAAnnotation(
            database="UniProtKB",
            db_object_id="P25685",
            db_object_symbol="DNAJB1",
            qualifier="",
            go_id="GO:0005515",
            go_term="protein binding",
            go_aspect="MF",
            evidence_code="IPI",
            evidence_type="ECO:0000353",
            reference="PMID:2",
            with_from="",
            taxon_id="NCBITaxon:9606",
            taxon_label="Homo sapiens",
            assigned_by="UniProt",
            annotation_extension="",
            date="20260408",
        ),
    ]

    result = compare_annotation_to_goa(annotation, goa_annotations)

    assert result.best_goa_id == "GO:0031072"
    assert result.best_goa_term == "heat shock protein binding"
    assert result.best_keyword_overlap >= 1
    assert result.match_level in {"strong_text_match", "weak_text_match"}


def test_compare_annotation_to_goa_detects_strong_autophagy_match() -> None:
    """A clear ALP/CMA alignment should be labeled as a strong text match."""
    annotation = ProteostasisAnnotation(
        order=2,
        gene_symbol="HSPA8",
        gene_name="heat shock protein family A (Hsp70) member 8",
        branch="Autophagy-Lysosome Pathway",
        class_name="Chaperone-mediated autophagy",
        group="Effectors of chaperone-mediated autophagy",
        type_name="Substrate delivery",
        subtype="(no Subtype)",
        notes="",
    )

    goa_annotations = [
        GOAAnnotation(
            database="UniProtKB",
            db_object_id="P11142",
            db_object_symbol="HSPA8",
            qualifier="",
            go_id="GO:0061684",
            go_term="chaperone-mediated autophagy",
            go_aspect="BP",
            evidence_code="IDA",
            evidence_type="ECO:0000314",
            reference="PMID:3",
            with_from="",
            taxon_id="NCBITaxon:9606",
            taxon_label="Homo sapiens",
            assigned_by="UniProt",
            annotation_extension="",
            date="20260408",
        )
    ]

    result = compare_annotation_to_goa(annotation, goa_annotations)

    assert result.best_goa_id == "GO:0061684"
    assert result.match_level == "strong_text_match"
    assert result.best_keyword_overlap >= 2


def test_load_proteostasis_annotations_from_dense_workbook(tmp_path: Path) -> None:
    """The loader should skip spacer rows and preserve meaningful values."""
    workbook = tmp_path / "pn.xlsx"
    dense = pd.DataFrame(
        [
            {
                "order": 1,
                "Gene Symbol": "HSPA1A",
                "Gene Name": "heat shock protein family A member 1A",
                "Branch": "Cytonuclear proteostasis",
                "Class": "Chaperone",
                "Group": "HSP70 system",
                "Type": "HSP70",
                "Subtype": "(no Subtype)",
                "Notes": None,
            },
            {
                "order": 2,
                "Gene Symbol": None,
                "Gene Name": None,
                "Branch": "Cytonuclear proteostasis",
                "Class": "Chaperone",
                "Group": None,
                "Type": None,
                "Subtype": None,
                "Notes": None,
            },
        ]
    )
    with pd.ExcelWriter(workbook) as writer:
        dense.to_excel(writer, index=False, sheet_name="dense")

    annotations = load_proteostasis_annotations(workbook)

    assert len(annotations) == 1
    assert annotations[0].gene_symbol == "HSPA1A"
    assert annotations[0].branch == "Cytonuclear proteostasis"
