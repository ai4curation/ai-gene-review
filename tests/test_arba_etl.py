"""Tests for ARBA ETL functionality."""

import tempfile
from pathlib import Path

import pytest

from ai_gene_review.etl.arba import (
    ARBAClient,
    ARBARule,
    Annotation,
    Condition,
    ConditionValue,
    DBReference,
    Keyword,
    Reaction,
    ReactionCrossReference,
    Statistics,
)


# Sample ARBA rule JSON for testing
SAMPLE_RULE_JSON = {
    "uniRuleId": "ARBA00000001",
    "information": {"version": "0"},
    "mainRule": {
        "conditionSets": [
            {
                "conditions": [
                    {
                        "conditionValues": [{"value": "IPR040234"}],
                        "type": "InterPro id",
                        "isNegative": False,
                    },
                    {
                        "conditionValues": [{"value": "Metazoa", "cvId": "33208"}],
                        "type": "taxon",
                        "isNegative": False,
                    },
                ]
            }
        ],
        "annotations": [
            {
                "annotationType": "ANNOTATION",
                "comment": {
                    "commentType": "CATALYTIC ACTIVITY",
                    "reaction": {
                        "name": "ATP hydrolysis",
                        "reactionCrossReferences": [
                            {"database": "Rhea", "id": "RHEA:23652"},
                            {"database": "ChEBI", "id": "CHEBI:28938"},
                        ],
                        "ecNumber": "2.3.2.5",
                    },
                },
            }
        ],
    },
    "statistics": {"reviewedProteinCount": 5, "unreviewedProteinCount": 100},
    "createdDate": "2020-05-12",
    "modifiedDate": "2025-03-21",
}


SAMPLE_KEYWORD_RULE_JSON = {
    "uniRuleId": "ARBA00022426",
    "information": {"version": "0"},
    "mainRule": {
        "conditionSets": [
            {
                "conditions": [
                    {
                        "conditionValues": [{"value": "IPR001234"}],
                        "type": "InterPro id",
                        "isNegative": False,
                    }
                ]
            }
        ],
        "annotations": [
            {
                "annotationType": "ANNOTATION",
                "keyword": {
                    "id": "KW-0171",
                    "name": "Cobalt transport",
                    "category": "Ligand",
                },
            }
        ],
    },
    "statistics": {"reviewedProteinCount": 0, "unreviewedProteinCount": 50},
    "createdDate": "2020-05-12",
    "modifiedDate": "2020-05-12",
}


SAMPLE_GO_RULE_JSON = {
    "uniRuleId": "ARBA00089714",
    "information": {"version": "0"},
    "mainRule": {
        "conditionSets": [
            {
                "conditions": [
                    {
                        "conditionValues": [{"value": "1.10.510.10:FF:000100"}],
                        "type": "FunFam id",
                        "isNegative": False,
                    }
                ]
            }
        ],
        "annotations": [
            {
                "annotationType": "ANNOTATION",
                "dbReference": {
                    "database": "GO",
                    "id": "GO:0036435",
                    "properties": [
                        {"key": "GoTerm", "value": "-"},
                        {"key": "GoEvidenceType", "value": ":-"},
                    ],
                },
            }
        ],
    },
    "statistics": {"reviewedProteinCount": 0, "unreviewedProteinCount": 0},
    "createdDate": "2025-03-21",
    "modifiedDate": "2025-03-21",
}


def test_condition_value():
    """Test ConditionValue creation."""
    cv = ConditionValue(value="IPR040234", cv_id="33208")
    assert cv.value == "IPR040234"
    assert cv.cv_id == "33208"


def test_condition():
    """Test Condition creation."""
    cond = Condition(
        condition_type="InterPro id",
        values=[ConditionValue(value="IPR040234")],
        is_negative=False,
    )
    assert cond.condition_type == "InterPro id"
    assert len(cond.values) == 1
    assert not cond.is_negative


def test_statistics():
    """Test Statistics creation and total count."""
    stats = Statistics(reviewed_count=5, unreviewed_count=100)
    assert stats.reviewed_count == 5
    assert stats.unreviewed_count == 100
    assert stats.total_count == 105


def test_reaction():
    """Test Reaction creation."""
    rxn = Reaction(
        name="ATP hydrolysis",
        cross_references=[
            ReactionCrossReference(database="Rhea", ref_id="RHEA:23652")
        ],
        ec_number="3.6.1.3",
    )
    assert rxn.name == "ATP hydrolysis"
    assert rxn.ec_number == "3.6.1.3"
    assert len(rxn.cross_references) == 1


def test_keyword():
    """Test Keyword creation."""
    kw = Keyword(kw_id="KW-0171", name="Cobalt transport", category="Ligand")
    assert kw.kw_id == "KW-0171"
    assert kw.name == "Cobalt transport"
    assert kw.category == "Ligand"


def test_annotation_with_reaction():
    """Test Annotation with catalytic activity."""
    ann = Annotation(
        annotation_type="ANNOTATION",
        comment_type="CATALYTIC ACTIVITY",
        reaction=Reaction(name="test reaction", ec_number="1.1.1.1"),
    )
    assert ann.annotation_type == "ANNOTATION"
    assert ann.comment_type == "CATALYTIC ACTIVITY"
    assert ann.reaction is not None
    assert ann.reaction.ec_number == "1.1.1.1"


def test_annotation_with_keyword():
    """Test Annotation with keyword."""
    ann = Annotation(
        annotation_type="ANNOTATION",
        keyword=Keyword(kw_id="KW-0001", name="Test keyword"),
    )
    assert ann.keyword is not None
    assert ann.keyword.name == "Test keyword"


def test_annotation_with_db_reference():
    """Test Annotation with database reference (GO term)."""
    ann = Annotation(
        annotation_type="ANNOTATION",
        db_reference=DBReference(
            database="GO",
            ref_id="GO:0036435",
            properties={"GoTerm": "-", "GoEvidenceType": ":-"}
        ),
    )
    assert ann.db_reference is not None
    assert ann.db_reference.database == "GO"
    assert ann.db_reference.ref_id == "GO:0036435"


def test_arba_rule_from_json():
    """Test parsing ARBA rule from JSON."""
    rule = ARBARule.from_json(SAMPLE_RULE_JSON)

    assert rule.uni_rule_id == "ARBA00000001"
    assert rule.version == "0"
    assert rule.created_date == "2020-05-12"
    assert rule.modified_date == "2025-03-21"

    # Check statistics
    assert rule.statistics.reviewed_count == 5
    assert rule.statistics.unreviewed_count == 100
    assert rule.statistics.total_count == 105

    # Check conditions
    assert len(rule.condition_sets) == 1
    assert len(rule.condition_sets[0].conditions) == 2

    # Check annotations
    assert len(rule.annotations) == 1
    assert rule.annotations[0].comment_type == "CATALYTIC ACTIVITY"
    assert rule.annotations[0].reaction is not None
    assert rule.annotations[0].reaction.ec_number == "2.3.2.5"


def test_arba_rule_from_json_with_keyword():
    """Test parsing ARBA rule with keyword annotation."""
    rule = ARBARule.from_json(SAMPLE_KEYWORD_RULE_JSON)

    assert rule.uni_rule_id == "ARBA00022426"
    assert len(rule.annotations) == 1
    assert rule.annotations[0].keyword is not None
    assert rule.annotations[0].keyword.kw_id == "KW-0171"
    assert rule.annotations[0].keyword.name == "Cobalt transport"


def test_arba_rule_from_json_with_go():
    """Test parsing ARBA rule with GO annotation."""
    rule = ARBARule.from_json(SAMPLE_GO_RULE_JSON)

    assert rule.uni_rule_id == "ARBA00089714"
    assert len(rule.annotations) == 1
    assert rule.annotations[0].db_reference is not None
    assert rule.annotations[0].db_reference.database == "GO"
    assert rule.annotations[0].db_reference.ref_id == "GO:0036435"
    assert rule.get_go_ids() == ["GO:0036435"]


def test_arba_rule_to_json():
    """Test serializing ARBA rule to JSON."""
    rule = ARBARule.from_json(SAMPLE_RULE_JSON)
    json_output = rule.to_json()

    assert json_output["uniRuleId"] == "ARBA00000001"
    assert json_output["information"]["version"] == "0"
    assert json_output["statistics"]["reviewedProteinCount"] == 5
    assert json_output["statistics"]["unreviewedProteinCount"] == 100


def test_arba_rule_roundtrip():
    """Test JSON roundtrip serialization."""
    original = ARBARule.from_json(SAMPLE_RULE_JSON)
    json_output = original.to_json()
    restored = ARBARule.from_json(json_output)

    assert restored.uni_rule_id == original.uni_rule_id
    assert restored.version == original.version
    assert restored.statistics.total_count == original.statistics.total_count
    assert len(restored.annotations) == len(original.annotations)


def test_arba_rule_get_interpro_ids():
    """Test extracting InterPro IDs from rule conditions."""
    rule = ARBARule.from_json(SAMPLE_RULE_JSON)
    interpro_ids = rule.get_interpro_ids()

    assert "IPR040234" in interpro_ids


def test_arba_rule_get_ec_numbers():
    """Test extracting EC numbers from rule annotations."""
    rule = ARBARule.from_json(SAMPLE_RULE_JSON)
    ec_numbers = rule.get_ec_numbers()

    assert "2.3.2.5" in ec_numbers


def test_arba_rule_get_rhea_ids():
    """Test extracting Rhea IDs from rule annotations."""
    rule = ARBARule.from_json(SAMPLE_RULE_JSON)
    rhea_ids = rule.get_rhea_ids()

    assert "RHEA:23652" in rhea_ids


def test_arba_client_cache():
    """Test ARBA client caching functionality."""
    with tempfile.TemporaryDirectory() as tmpdir:
        cache_dir = Path(tmpdir)
        client = ARBAClient(cache_dir=cache_dir)

        # Create a rule and save it
        rule = ARBARule.from_json(SAMPLE_RULE_JSON)
        client._save_to_cache(rule)

        # Check directory and file were created (new layout: arba/ARBANNN/ARBANNN.json)
        rule_dir = cache_dir / "ARBA00000001"
        cache_file = rule_dir / "ARBA00000001.json"
        assert rule_dir.exists()
        assert cache_file.exists()

        # Load from cache
        loaded = client._load_from_cache("ARBA00000001")
        assert loaded is not None
        assert loaded.uni_rule_id == "ARBA00000001"

        # Non-existent rule should return None
        assert client._load_from_cache("ARBA99999999") is None


def test_arba_client_cache_stats():
    """Test ARBA client cache statistics."""
    with tempfile.TemporaryDirectory() as tmpdir:
        cache_dir = Path(tmpdir)
        client = ARBAClient(cache_dir=cache_dir)

        # Empty cache
        stats = client.get_cache_stats()
        assert stats["cached_rules"] == 0

        # Save a rule
        rule = ARBARule.from_json(SAMPLE_RULE_JSON)
        client._save_to_cache(rule)

        stats = client.get_cache_stats()
        assert stats["cached_rules"] == 1
        assert stats["cache_size_bytes"] > 0


def test_arba_client_get_cached_rules():
    """Test iterating over cached rules."""
    with tempfile.TemporaryDirectory() as tmpdir:
        cache_dir = Path(tmpdir)
        client = ARBAClient(cache_dir=cache_dir)

        # Save multiple rules
        rule1 = ARBARule.from_json(SAMPLE_RULE_JSON)
        client._save_to_cache(rule1)

        rule2 = ARBARule.from_json(SAMPLE_KEYWORD_RULE_JSON)
        client._save_to_cache(rule2)

        # Get all cached rules
        cached = list(client.get_cached_rules())
        assert len(cached) == 2

        rule_ids = {r.uni_rule_id for r in cached}
        assert "ARBA00000001" in rule_ids
        assert "ARBA00022426" in rule_ids


@pytest.mark.integration
def test_arba_client_get_total_count():
    """Test getting total ARBA rule count from API.

    This test requires network access and is marked as integration.
    """
    client = ARBAClient()
    count = client.get_total_count()

    # ARBA has ~80,000 rules as of 2025
    assert count > 80000


@pytest.mark.integration
def test_arba_client_fetch_rule():
    """Test fetching a single ARBA rule from API.

    This test requires network access and is marked as integration.
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        cache_dir = Path(tmpdir)
        client = ARBAClient(cache_dir=cache_dir)

        rule = client.fetch_rule("ARBA00000001")

        assert rule is not None
        assert rule.uni_rule_id == "ARBA00000001"
        assert rule.statistics.unreviewed_count > 0

        # Should have catalytic activity annotation
        assert len(rule.annotations) > 0
        assert rule.annotations[0].reaction is not None


@pytest.mark.integration
def test_arba_client_search():
    """Test searching ARBA rules from API.

    This test requires network access and is marked as integration.
    """
    client = ARBAClient()

    # Search for rules with EC 2.3.2.5
    rules, next_cursor = client.search(query="ec:2.3.2.5", size=10)

    assert len(rules) > 0
    assert rules[0].annotations[0].reaction is not None
    assert rules[0].annotations[0].reaction.ec_number == "2.3.2.5"


@pytest.mark.integration
def test_arba_client_iter_limited():
    """Test iterating over a limited number of ARBA rules.

    This test requires network access and is marked as integration.
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        cache_dir = Path(tmpdir)
        client = ARBAClient(cache_dir=cache_dir, request_delay=0.1)

        # Iterate with a small limit
        rules = []
        for rule in client.iter_all_rules(batch_size=10, cache=True):
            rules.append(rule)
            if len(rules) >= 5:
                break

        assert len(rules) == 5

        # Check rules were cached
        stats = client.get_cache_stats()
        assert stats["cached_rules"] >= 5
