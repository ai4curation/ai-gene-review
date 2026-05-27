from pathlib import Path

import yaml

from scripts import gene_hypothesis_deep_research as ghr


def write_yaml(path: Path, data: dict) -> None:
    path.write_text(yaml.safe_dump(data, sort_keys=False), encoding="utf-8")


def make_gene_workspace(tmp_path: Path) -> Path:
    genes_root = tmp_path / "genes"
    gene_dir = genes_root / "human" / "TEST"
    gene_dir.mkdir(parents=True)
    write_yaml(
        gene_dir / "TEST-ai-review.yaml",
        {
            "id": "Q12345",
            "gene_symbol": "TEST",
            "taxon": {"id": "NCBITaxon:9606", "label": "Homo sapiens"},
            "existing_annotations": [
                {
                    "term": {"id": "GO:0005515", "label": "protein binding"},
                    "evidence_type": "IPI",
                    "original_reference_id": "PMID:1",
                    "review": {
                        "action": "REMOVE",
                        "summary": "Generic binding is not informative.",
                        "reason": "A specific adapter or assembly role is more likely.",
                        "supported_by": [
                            {
                                "reference_id": "PMID:2",
                                "supporting_text": "Interacts with a pathway component.",
                            }
                        ],
                    },
                },
                {
                    "term": {"id": "GO:0099999", "label": "test process"},
                    "evidence_type": "IMP",
                    "original_reference_id": "PMID:3",
                    "review": {
                        "action": "NEW",
                        "reason": "Loss of function blocks the process.",
                    },
                },
            ],
            "core_functions": [
                {
                    "molecular_function": {
                        "id": "GO:0003677",
                        "label": "DNA binding",
                    },
                    "description": "TEST directly binds DNA.",
                    "directly_involved_in": [
                        {
                            "id": "GO:0006355",
                            "label": "regulation of DNA-templated transcription",
                        }
                    ],
                    "supported_by": [
                        {"reference_id": "PMID:4", "supporting_text": "DNA binding."}
                    ],
                }
            ],
        },
    )
    write_yaml(
        gene_dir / "TEST-predictions-review.yaml",
        {
            "id": "Q12345",
            "gene_symbol": "TEST",
            "taxon": {"id": "NCBITaxon:9606", "label": "Homo sapiens"},
            "predictions": [
                {
                    "source_method": "DeepECTF",
                    "source_reference_id": "PMID:5",
                    "predicted_term": {
                        "id": "EC:1.2.3.4",
                        "label": "test oxidoreductase",
                    },
                    "predicted_term_type": "EC",
                    "review": {
                        "assessment": "PLI",
                        "error_type": "PARALOG_OVERANNOTATION",
                        "summary": "Wrong paralog subfamily.",
                        "supported_by": [
                            {
                                "reference_id": "PMID:6",
                                "supporting_text": "Does not complement.",
                            }
                        ],
                    },
                }
            ],
        },
    )
    return genes_root


def test_slugify_normalizes_identifiers() -> None:
    assert ghr.slugify("GO:0005515") == "go-0005515"
    assert ghr.slugify("  Core function: DNA binding! ") == "core-function-dna-binding"


def test_candidate_records_cover_review_and_prediction_sources(tmp_path: Path) -> None:
    genes_root = make_gene_workspace(tmp_path)

    records = ghr.candidate_records(genes_root, "human", "TEST")
    by_slug = {record.slug: record for record in records}

    assert by_slug["existing-go-0005515-remove"].focus_type == (
        "existing_go_annotation_decision"
    )
    assert by_slug["new-go-0099999-new"].focus_type == "proposed_go_term"
    assert by_slug["core-function-1-go-0003677"].focus_type == "core_function"
    assert by_slug["prediction-deepectf-ec-1-2-3-4"].focus_type == (
        "computational_prediction"
    )
    assert "PMID:4" in by_slug["core-function-1-go-0003677"].reference_context


def test_select_record_and_build_command_use_sidecar_output(tmp_path: Path) -> None:
    genes_root = make_gene_workspace(tmp_path)
    records = ghr.candidate_records(genes_root, "human", "TEST")
    record = ghr.select_record(records, annotation_term_id="GO:0005515")

    command = ghr.build_command(
        record,
        provider="edison",
        genes_root=genes_root,
        template=Path("templates/gene_hypothesis_deep_research.md"),
        extra_args=["--param", "max_sources=20"],
    )

    output_path = (
        genes_root
        / "human"
        / "TEST"
        / "TEST-hypotheses"
        / "existing-go-0005515-remove"
        / "falcon.md"
    )
    assert command[:6] == [
        "uv",
        "run",
        "deep-research-client",
        "research",
        "--template",
        "templates/gene_hypothesis_deep_research.md",
    ]
    assert ["--provider", "falcon"] == command[-8:-6]
    assert ["--output", str(output_path)] == command[-6:-4]
    assert ["--separate-citations", f"{output_path}.citations.md"] == command[-4:-2]
    assert command[-2:] == ["--param", "max_sources=20"]
    assert any(
        item == "hypothesis_slug=existing-go-0005515-remove" for item in command
    )


def test_dry_run_does_not_create_output_directory(tmp_path: Path) -> None:
    genes_root = make_gene_workspace(tmp_path)
    record = ghr.select_record(
        ghr.candidate_records(genes_root, "human", "TEST"),
        prediction_term_id="EC:1.2.3.4",
    )

    result = ghr.run_record(
        record,
        provider="perplexity-lite",
        genes_root=genes_root,
        template=Path("templates/gene_hypothesis_deep_research.md"),
        extra_args=[],
        timeout_seconds=1,
        dry_run=True,
        overwrite=False,
    )

    assert result.status == "DRY_RUN"
    assert result.output_file.name == "perplexity-lite.md"
    assert not result.output_file.parent.exists()
