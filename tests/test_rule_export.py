"""Tests for rule CSV export functionality."""

import csv
import json
import tempfile
from pathlib import Path


from ai_gene_review.etl.rule_export import (
    COLUMNS,
    _extract_condition_fields,
    _extract_go_annotations,
    export_rules_to_csv,
    iter_rule_files,
    rule_to_rows,
)


# Sample rule JSON for testing
SAMPLE_ARBA_RULE = {
    "uniRuleId": "ARBA00026249",
    "mainRule": {
        "conditionSets": [
            {
                "conditions": [
                    {
                        "type": "FunFam id",
                        "conditionValues": [
                            {
                                "value": "1.10.510.10:FF:000100",
                                "curie": "CATH.FunFam:1.10.510.10:FF:000100",
                                "label": "Some Family"
                            }
                        ],
                        "isNegative": False
                    },
                    {
                        "type": "taxon",
                        "conditionValues": [
                            {
                                "value": "Bacteria",
                                "cvId": "2",
                                "curie": "NCBITaxon:2",
                                "label": "Bacteria"
                            }
                        ],
                        "isNegative": False
                    }
                ]
            },
            {
                "conditions": [
                    {
                        "type": "InterPro id",
                        "conditionValues": [
                            {
                                "value": "IPR000001",
                                "curie": "InterPro:IPR000001",
                                "label": "Kringle"
                            }
                        ],
                        "isNegative": True
                    }
                ]
            }
        ],
        "annotations": [
            {
                "dbReference": {
                    "database": "GO",
                    "id": "GO:0036435",
                    "label": "receptor activity"
                }
            }
        ]
    },
    "statistics": {
        "reviewedProteinCount": 5,
        "unreviewedProteinCount": 100
    },
    "createdDate": "2020-05-12",
    "modifiedDate": "2025-03-21"
}


SAMPLE_MULTI_GO_RULE = {
    "uniRuleId": "ARBA00026250",
    "mainRule": {
        "conditionSets": [
            {
                "conditions": [
                    {
                        "type": "taxon",
                        "conditionValues": [{"value": "Fungi"}],
                        "isNegative": False
                    }
                ]
            }
        ],
        "annotations": [
            {
                "dbReference": {
                    "database": "GO",
                    "id": "GO:0005515",
                    "label": "protein binding"
                }
            },
            {
                "dbReference": {
                    "database": "GO",
                    "id": "GO:0008150",
                    "label": "biological process"
                }
            },
            {
                "keyword": {"id": "KW-0001", "name": "Some keyword"}
            }
        ]
    },
    "statistics": {"reviewedProteinCount": 0, "unreviewedProteinCount": 50},
    "createdDate": "2021-01-01",
    "modifiedDate": "2021-06-15"
}


def test_extract_go_annotations_single():
    """Test extracting a single GO annotation."""
    go_ids, go_labels = _extract_go_annotations(SAMPLE_ARBA_RULE)
    assert go_ids == ["GO:0036435"]
    assert go_labels == ["receptor activity"]


def test_extract_go_annotations_multiple():
    """Test extracting multiple GO annotations."""
    go_ids, go_labels = _extract_go_annotations(SAMPLE_MULTI_GO_RULE)
    assert go_ids == ["GO:0005515", "GO:0008150"]
    assert go_labels == ["protein binding", "biological process"]


def test_extract_go_annotations_none():
    """Test with no GO annotations."""
    rule = {
        "mainRule": {
            "annotations": [
                {"keyword": {"id": "KW-0001", "name": "Test"}}
            ]
        }
    }
    go_ids, go_labels = _extract_go_annotations(rule)
    assert go_ids == []
    assert go_labels == []


def test_extract_condition_fields():
    """Test extracting condition fields for pivoted columns."""
    cond = {
        "type": "taxon",
        "conditionValues": [
            {
                "value": "Fungi",
                "cvId": "4751",
                "curie": "NCBITaxon:4751",
                "label": "Fungi"
            }
        ],
        "isNegative": False
    }
    fields = _extract_condition_fields(cond, 1)
    assert fields["term1_type"] == "taxon"
    assert fields["term1_id"] == "Fungi"
    assert fields["term1_curie"] == "NCBITaxon:4751"
    assert fields["term1_label"] == "Fungi"
    assert fields["term1_negated"] == "false"


def test_extract_condition_fields_negated():
    """Test extracting negated condition fields."""
    cond = {
        "type": "InterPro id",
        "conditionValues": [{"value": "IPR000001"}],
        "isNegative": True
    }
    fields = _extract_condition_fields(cond, 2)
    assert fields["term2_type"] == "InterPro id"
    assert fields["term2_negated"] == "true"


def test_rule_to_rows_basic():
    """Test converting rule to rows."""
    rows = rule_to_rows(SAMPLE_ARBA_RULE, "arba")

    # Should produce 2 rows (2 condition sets)
    assert len(rows) == 2

    # Check first row
    row1 = rows[0]
    assert row1["rule_id"] == "ARBA00026249"
    assert row1["rule_type"] == "arba"
    assert row1["condition_set_index"] == 0
    assert row1["term1_type"] == "FunFam id"
    assert row1["term1_id"] == "1.10.510.10:FF:000100"
    assert row1["term1_curie"] == "CATH.FunFam:1.10.510.10:FF:000100"
    assert row1["term2_type"] == "taxon"
    assert row1["term3_type"] == ""  # Empty third condition
    assert row1["go_ids"] == "GO:0036435"
    assert row1["go_labels"] == "receptor activity"

    # Check second row
    row2 = rows[1]
    assert row2["condition_set_index"] == 1
    assert row2["term1_type"] == "InterPro id"
    assert row2["term1_negated"] == "true"


def test_rule_to_rows_multi_go():
    """Test rule with multiple GO annotations."""
    rows = rule_to_rows(SAMPLE_MULTI_GO_RULE, "arba")

    assert len(rows) == 1
    row = rows[0]
    assert row["go_ids"] == "GO:0005515|GO:0008150"
    assert row["go_labels"] == "protein binding|biological process"


def test_rule_to_rows_has_all_columns():
    """Test that rows have all expected columns."""
    rows = rule_to_rows(SAMPLE_ARBA_RULE, "arba")

    for row in rows:
        for col in COLUMNS:
            assert col in row, f"Missing column: {col}"


def test_export_rules_to_csv():
    """Test full CSV export."""
    with tempfile.TemporaryDirectory() as tmpdir:
        cache_dir = Path(tmpdir)

        # Create ARBA directory and rule file
        arba_dir = cache_dir / "arba" / "ARBA00026249"
        arba_dir.mkdir(parents=True)
        rule_file = arba_dir / "ARBA00026249.json"
        rule_file.write_text(json.dumps(SAMPLE_ARBA_RULE))

        # Export
        output_path = cache_dir / "export.csv"
        rows_written = export_rules_to_csv(
            cache_dir=cache_dir,
            output_path=output_path,
            rule_type="arba",
            use_enriched=False
        )

        assert rows_written == 2
        assert output_path.exists()

        # Verify CSV content
        with open(output_path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            rows = list(reader)

        assert len(rows) == 2
        assert rows[0]["rule_id"] == "ARBA00026249"
        assert rows[0]["term1_type"] == "FunFam id"


def test_export_rules_prefers_enriched():
    """Test that export prefers .enriched.json files."""
    import copy

    with tempfile.TemporaryDirectory() as tmpdir:
        cache_dir = Path(tmpdir)

        # Create both raw and enriched files
        arba_dir = cache_dir / "arba" / "ARBA00026249"
        arba_dir.mkdir(parents=True)

        raw_file = arba_dir / "ARBA00026249.json"
        raw_rule = copy.deepcopy(SAMPLE_ARBA_RULE)
        raw_rule["mainRule"]["annotations"][0]["dbReference"]["label"] = ""
        raw_file.write_text(json.dumps(raw_rule))

        enriched_file = arba_dir / "ARBA00026249.enriched.json"
        enriched_file.write_text(json.dumps(SAMPLE_ARBA_RULE))

        # Export with enriched=True (default)
        output_path = cache_dir / "export.csv"
        export_rules_to_csv(
            cache_dir=cache_dir,
            output_path=output_path,
            use_enriched=True
        )

        with open(output_path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            rows = list(reader)

        # Should have label from enriched file
        assert rows[0]["go_labels"] == "receptor activity"


def test_iter_rule_files_filters_by_type():
    """Test that iter_rule_files respects rule_type filter."""
    with tempfile.TemporaryDirectory() as tmpdir:
        cache_dir = Path(tmpdir)

        # Create ARBA and UniRule directories
        arba_dir = cache_dir / "arba" / "ARBA00000001"
        arba_dir.mkdir(parents=True)
        (arba_dir / "ARBA00000001.json").write_text("{}")

        unirule_dir = cache_dir / "unirule" / "UR000000001"
        unirule_dir.mkdir(parents=True)
        (unirule_dir / "UR000000001.json").write_text("{}")

        # Filter for ARBA only
        arba_files = list(iter_rule_files(cache_dir, rule_type="arba", use_enriched=False))
        assert len(arba_files) == 1
        assert arba_files[0][1] == "arba"

        # Filter for UniRule only
        unirule_files = list(iter_rule_files(cache_dir, rule_type="unirule", use_enriched=False))
        assert len(unirule_files) == 1
        assert unirule_files[0][1] == "unirule"

        # All
        all_files = list(iter_rule_files(cache_dir, rule_type="all", use_enriched=False))
        assert len(all_files) == 2
