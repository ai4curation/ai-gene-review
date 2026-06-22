from pathlib import Path

import pytest
import yaml

from scripts import gene_hypothesis_deep_research as ghr


def write_yaml(path: Path, data: dict) -> None:
    path.write_text(yaml.safe_dump(data, sort_keys=False), encoding="utf-8")


def make_gene_workspace(tmp_path: Path) -> Path:
    genes_root = tmp_path / "genes"
    gene_dir = genes_root / "human" / "TEST"
    gene_dir.mkdir(parents=True)
    bioinformatics_dir = gene_dir / "TEST-bioinformatics"
    bioinformatics_dir.mkdir()
    (bioinformatics_dir / "RESULTS.md").write_text(
        "# TEST Bioinformatics Results\n\n"
        "Local analysis supports replacing generic protein binding with a more "
        "specific adaptor-function hypothesis.\n",
        encoding="utf-8",
    )
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
                            },
                            {
                                "reference_id": "file:human/TEST/TEST-bioinformatics/RESULTS.md",
                                "supporting_text": (
                                    "Local analysis supports replacing generic "
                                    "protein binding."
                                ),
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


def make_iba_workspace(tmp_path: Path) -> Path:
    """Gene workspace with a mix of supported and unsupported IBA annotations."""
    genes_root = tmp_path / "genes"
    gene_dir = genes_root / "human" / "IBAT"
    gene_dir.mkdir(parents=True)
    write_yaml(
        gene_dir / "IBAT-ai-review.yaml",
        {
            "id": "Q99999",
            "gene_symbol": "IBAT",
            "taxon": {"id": "NCBITaxon:9606", "label": "Homo sapiens"},
            "existing_annotations": [
                {
                    # IBA with NO independent support -> a candidate
                    "term": {"id": "GO:0005737", "label": "cytoplasm"},
                    "evidence_type": "IBA",
                    "original_reference_id": "GO_REF:0000033",
                    "review": {"action": "ACCEPT", "summary": "Plausible location."},
                },
                {
                    # IBA WITH independent PMID support -> skipped by default
                    "term": {"id": "GO:0005515", "label": "protein binding"},
                    "evidence_type": "IBA",
                    "original_reference_id": "GO_REF:0000033",
                    "review": {
                        "action": "KEEP_AS_NON_CORE",
                        "summary": "Has an interaction paper.",
                        "supported_by": [
                            {
                                "reference_id": "PMID:111",
                                "supporting_text": "Interacts with partner X.",
                            }
                        ],
                    },
                },
                {
                    # Non-IBA annotation -> never a candidate
                    "term": {"id": "GO:0003674", "label": "molecular_function"},
                    "evidence_type": "IEA",
                    "original_reference_id": "GO_REF:0000002",
                    "review": {"action": "ACCEPT"},
                },
            ],
        },
    )
    return genes_root


def test_annotation_independent_literature_refs_excludes_original() -> None:
    supported = {
        "original_reference_id": "GO_REF:0000033",
        "review": {
            "supported_by": [{"reference_id": "PMID:111"}],
            "additional_reference_ids": ["GO_REF:0000033", "file:x.md"],
        },
    }
    unsupported = {
        "original_reference_id": "GO_REF:0000033",
        "review": {"supported_by": [{"reference_id": "file:local.md"}]},
    }
    assert ghr.annotation_independent_literature_refs(supported) == ["PMID:111"]
    assert ghr.annotation_independent_literature_refs(unsupported) == []


def test_iba_support_records_default_only_unsupported(tmp_path: Path) -> None:
    genes_root = make_iba_workspace(tmp_path)
    records = ghr.iba_support_records(genes_root, "human", "IBAT")
    slugs = {record.slug for record in records}
    assert slugs == {"function-support-go-0005737"}
    record = records[0]
    # IBA is a thin wrapper that produces neutral function-support records.
    assert record.focus_type == "function_support"
    assert record.source_selector == "existing_annotations[1]"
    assert record.hypothesis_text == "IBAT has cytoplasm (GO:0005737)."


def test_iba_support_records_include_supported(tmp_path: Path) -> None:
    genes_root = make_iba_workspace(tmp_path)
    records = ghr.iba_support_records(
        genes_root, "human", "IBAT", only_unsupported=False
    )
    slugs = {record.slug for record in records}
    assert slugs == {"function-support-go-0005737", "function-support-go-0005515"}


def test_iba_support_record_blinds_prior_review_action(tmp_path: Path) -> None:
    genes_root = make_iba_workspace(tmp_path)
    record = ghr.iba_support_records(genes_root, "human", "IBAT")[0]
    command_text = "\n".join(
        ghr.build_command(
            record,
            provider="asta",
            genes_root=genes_root,
            template=ghr.DEFAULT_FUNCTION_SUPPORT_TEMPLATE,
            extra_args=[],
        )
    )
    # The existing curation action/summary must not leak into the prompt.
    assert "ACCEPT" not in command_text
    assert "Plausible location" not in command_text


def test_function_support_build_command_slug_and_template(tmp_path: Path) -> None:
    genes_root = make_iba_workspace(tmp_path)
    record = ghr.iba_support_records(genes_root, "human", "IBAT")[0]
    command = ghr.build_command(
        record,
        provider="asta",
        genes_root=genes_root,
        template=ghr.DEFAULT_FUNCTION_SUPPORT_TEMPLATE,
        extra_args=[],
    )
    output_path = (
        genes_root
        / "human"
        / "IBAT"
        / "IBAT-hypotheses"
        / "function-support-go-0005737"
        / "asta.md"
    )
    assert ["--provider", "asta"] == command[-6:-4]
    assert ["--output", str(output_path)] == command[-4:-2]


def test_run_iba_support_dry_run(tmp_path: Path) -> None:
    genes_root = make_iba_workspace(tmp_path)
    exit_code = ghr.main(
        [
            "run-iba-support",
            "human",
            "IBAT",
            "asta",
            "--genes-root",
            str(genes_root),
            "--dry-run",
        ]
    )
    assert exit_code == 0
    assert not (genes_root / "human" / "IBAT" / "IBAT-hypotheses").exists()


def test_function_support_free_text_hypothesis(tmp_path: Path) -> None:
    genes_root = make_iba_workspace(tmp_path)
    args = ghr.parse_args(
        [
            "run-function-support",
            "human",
            "IBAT",
            "asta",
            "--genes-root",
            str(genes_root),
            "--hypothesis",
            "IBAT is a cytoskeletal adaptor",
        ]
    )
    record = ghr.function_support_record_from_args(args)
    assert record.focus_type == "function_support"
    assert record.hypothesis_text == "IBAT is a cytoskeletal adaptor"
    assert record.source_selector == "free-text"


def test_function_support_from_term_id(tmp_path: Path) -> None:
    genes_root = make_iba_workspace(tmp_path)
    args = ghr.parse_args(
        [
            "run-function-support",
            "human",
            "IBAT",
            "asta",
            "--genes-root",
            str(genes_root),
            "--term-id",
            "GO:0003700",
            "--term-label",
            "DNA-binding transcription factor activity",
        ]
    )
    record = ghr.function_support_record_from_args(args)
    assert record.slug == "function-support-go-0003700"
    assert record.hypothesis_text == (
        "IBAT has DNA-binding transcription factor activity (GO:0003700)."
    )


def test_function_support_requires_exactly_one_selector(tmp_path: Path) -> None:
    genes_root = make_iba_workspace(tmp_path)
    args = ghr.parse_args(
        [
            "run-function-support",
            "human",
            "IBAT",
            "asta",
            "--genes-root",
            str(genes_root),
        ]
    )
    with pytest.raises(ValueError):
        ghr.function_support_record_from_args(args)


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


def test_provider_prompt_redacts_cited_local_bioinformatics(tmp_path: Path) -> None:
    genes_root = make_gene_workspace(tmp_path)
    records = ghr.candidate_records(genes_root, "human", "TEST")
    record = ghr.select_record(records, annotation_term_id="GO:0005515")
    reference_ids = ghr.reference_ids_from_context(record.reference_context)

    comparison_context = ghr.format_local_bioinformatics_context(
        reference_ids,
        genes_root=genes_root,
    )

    assert "file:human/TEST/TEST-bioinformatics/RESULTS.md" in comparison_context
    assert "# TEST Bioinformatics Results" in comparison_context
    assert "Included full local report" in comparison_context

    command = ghr.build_command(
        record,
        provider="openscientist",
        genes_root=genes_root,
        template=Path("templates/gene_hypothesis_deep_research.md"),
        extra_args=[],
    )
    command_text = "\n".join(command)

    assert "file:human/TEST/TEST-bioinformatics/RESULTS.md" not in command_text
    assert "# TEST Bioinformatics Results" not in command_text
    assert "Local analysis supports replacing generic protein binding" not in command_text
    assert "reference_context=- PMID:1\n- PMID:2" in command


def test_function_assignment_prompt_blinds_prior_review_decision(
    tmp_path: Path,
) -> None:
    genes_root = make_gene_workspace(tmp_path)
    records = ghr.candidate_records(genes_root, "human", "TEST")
    decision_record = ghr.select_record(records, annotation_term_id="GO:0005515")

    record = ghr.function_assignment_record(decision_record)
    command = ghr.build_command(
        record,
        provider="openscientist",
        genes_root=genes_root,
        template=Path("templates/gene_hypothesis_deep_research.md"),
        extra_args=[],
    )
    command_text = "\n".join(command)

    assert record.focus_type == "function_assignment"
    assert record.slug == "function-hypothesis-go-0005515"
    assert record.hypothesis_text == "TEST has protein binding (GO:0005515)."
    assert "review action REMOVE" not in command_text
    assert "Generic binding is not informative" not in command_text
    assert "specific adapter or assembly role" not in command_text
    assert "file:human/TEST/TEST-bioinformatics/RESULTS.md" not in command_text
    assert "# TEST Bioinformatics Results" not in command_text
    assert "hypothesis_text=TEST has protein binding (GO:0005515)." in command


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
