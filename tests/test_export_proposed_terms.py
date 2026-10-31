import csv
import json
from pathlib import Path

import pytest
from ruamel.yaml import YAML

from ai_gene_review.tools.export_proposed_terms import (
    export_proposed_terms,
    expand_inputs,
    read_review_with_proposed_terms,
    rows_for_review,
)


def test_prefilter_skips_empty_and_absent_top_level_proposed_terms(
    tmp_path: Path,
) -> None:
    absent = tmp_path / "absent-ai-review.yaml"
    absent.write_text(
        """
id: P1
knowledge_gaps:
  - proposed_terms:
      - proposed_name: gap-specific term
""",
        encoding="utf-8",
    )
    empty = tmp_path / "empty-ai-review.yaml"
    empty.write_text("proposed_new_terms: []\n", encoding="utf-8")
    empty_with_comment = tmp_path / "empty-comment-ai-review.yaml"
    empty_with_comment.write_text(
        "proposed_new_terms: []  # none today\n", encoding="utf-8"
    )

    block = tmp_path / "block-ai-review.yaml"
    block.write_text(
        """
proposed_new_terms:
  - proposed_name: novel molecular function activity
""",
        encoding="utf-8",
    )

    assert read_review_with_proposed_terms(absent) is None
    assert read_review_with_proposed_terms(empty) is None
    assert read_review_with_proposed_terms(empty_with_comment) is None
    assert read_review_with_proposed_terms(block) is not None


def test_rows_include_path_context_and_full_nested_json() -> None:
    path = Path("genes/human/ARF1/ARF1-ai-review.yaml")
    review_text = """
id: P84077
gene_symbol: ARF1
taxon:
  id: NCBITaxon:9606
  label: Homo sapiens
proposed_new_terms:
  - proposed_name: brefeldin A-sensitive guanyl-nucleotide exchange factor activity
    proposed_definition: >
      Enables a specific guanyl-nucleotide exchange activity.
    justification: >
      A line-wrapped reason for tabular export.
    proposed_parent:
      id: GO:0005085
      label: guanyl-nucleotide exchange factor activity
    proposed_mappings:
      - predicate: rdfs:subClassOf
        target_term:
          id: GO:0005085
          label: guanyl-nucleotide exchange factor activity
          description: Parent description retained for curation context
          ontology: go
    supported_by:
      - reference_id: PMID:123456
        supporting_text: "verbatim\\n  text\\twith spacing"
        reference_section_type: RESULTS
"""

    rows = rows_for_review(path, review_text, YAML(typ="safe"))

    assert rows == [
        {
            "source_path": "genes/human/ARF1/ARF1-ai-review.yaml",
            "organism": "human",
            "gene_directory": "ARF1",
            "review_id": "P84077",
            "gene_symbol": "ARF1",
            "taxon_id": "NCBITaxon:9606",
            "taxon_label": "Homo sapiens",
            "term_index": "1",
            "proposed_name": "brefeldin A-sensitive guanyl-nucleotide exchange factor activity",
            "proposed_definition": "Enables a specific guanyl-nucleotide exchange activity.",
            "justification": "A line-wrapped reason for tabular export.",
            "proposed_parent_id": "GO:0005085",
            "proposed_parent_label": "guanyl-nucleotide exchange factor activity",
            "proposed_mappings": json.dumps(
                [
                    {
                        "predicate": "rdfs:subClassOf",
                        "target_term": {
                            "description": "Parent description retained for curation context",
                            "id": "GO:0005085",
                            "label": "guanyl-nucleotide exchange factor activity",
                            "ontology": "go",
                        },
                    }
                ],
                sort_keys=True,
                separators=(",", ":"),
            ),
            "supported_by": json.dumps(
                [
                    {
                        "reference_id": "PMID:123456",
                        "reference_section_type": "RESULTS",
                        "supporting_text": "verbatim\n  text\twith spacing",
                    }
                ],
                sort_keys=True,
                separators=(",", ":"),
            ),
        }
    ]


def test_export_writes_literal_json_cells(tmp_path: Path) -> None:
    review_dir = tmp_path / "genes" / "human" / "ARF1"
    review_dir.mkdir(parents=True)
    review_path = review_dir / "ARF1-ai-review.yaml"
    review_path.write_text(
        """
id: P84077
gene_symbol: ARF1
taxon:
  id: NCBITaxon:9606
  label: Homo sapiens
proposed_new_terms:
  - proposed_name: proposed activity
    supported_by:
      - reference_id: PMID:123456
        supporting_text: "verbatim\\n  text"
""",
        encoding="utf-8",
    )
    output_path = tmp_path / "reports" / "proposed_new_terms.tsv"

    row_count = export_proposed_terms([tmp_path / "genes"], output_path)

    assert row_count == 1
    raw_output = output_path.read_text(encoding="utf-8")
    assert '""reference_id""' not in raw_output
    assert '\t[{"reference_id":"PMID:123456"' in raw_output

    with output_path.open(encoding="utf-8", newline="") as handle:
        row = next(csv.DictReader(handle, delimiter="\t"))

    assert row["source_path"] == review_path.as_posix()
    assert row["organism"] == "human"
    assert row["gene_directory"] == "ARF1"
    assert json.loads(row["supported_by"]) == [
        {
            "reference_id": "PMID:123456",
            "supporting_text": "verbatim\n  text",
        }
    ]


def test_expand_inputs_reports_missing_paths(tmp_path: Path) -> None:
    missing = tmp_path / "genes" / "humn"

    with pytest.raises(FileNotFoundError, match="Review input does not exist"):
        expand_inputs([missing])
