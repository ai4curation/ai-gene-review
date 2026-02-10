"""Tests for ARBA rule analysis functionality.

This module tests the post-enrichment analysis of ARBA rules, including:
- Fetching and caching InterPro2GO mappings
- Querying UniProt API for protein counts
- Calculating Jaccard similarity for InterPro domain overlap
- Analyzing redundancy with existing ipr2go mappings

Test data is based on ARBA00026249 which has:
- Condition set 1: IPR005982 AND IPR008255 AND IPR023753
- Annotation: GO:0004791 (thioredoxin-disulfide reductase (NADPH) activity)
"""

import json
from pathlib import Path

import pytest

from ai_gene_review.etl.arba import ARBARule
from ai_gene_review.etl.rule_analysis import (
    analyze_interpro_overlap_in_condition_set,
    analyze_ipr2go_redundancy,
    analyze_rule_post_enrichment,
    calculate_jaccard_similarity,
    fetch_interpro2go_mappings,
    get_interpros_for_go,
    get_swissprot_count_for_interpro,
    get_swissprot_count_for_interpro_intersection,
)


@pytest.fixture
def arba00026249_rule() -> ARBARule:
    """Load ARBA00026249 from cached JSON file."""
    rule_file = Path("rules/arba/ARBA00026249/ARBA00026249.json")
    if not rule_file.exists():
        pytest.skip(f"Rule file not found: {rule_file}")

    data = json.loads(rule_file.read_text())
    return ARBARule.from_json(data)


@pytest.mark.integration
def test_fetch_interpro2go_mappings(tmp_path):
    """Test downloading and caching InterPro2GO file.

    Verifies:
    - File is downloaded from official GO source
    - File is cached locally
    - Cached file is reused on subsequent calls
    - Parsing returns dict mapping InterPro IDs to GO IDs
    """
    cache_dir = tmp_path / "cache"
    cache_dir.mkdir()

    # First call should download
    mappings = fetch_interpro2go_mappings(cache_dir)

    assert isinstance(mappings, dict)
    assert len(mappings) > 0

    # Check cache file exists
    cache_file = cache_dir / "_interpro2go.txt"
    assert cache_file.exists()

    # Check some expected mappings (these are stable in ipr2go)
    # Format should be: {interpro_id: [go_ids]}
    assert all(isinstance(v, list) for v in mappings.values())
    assert all(ipr_id.startswith("IPR") for ipr_id in mappings.keys())

    # Second call should use cache
    original_mtime = cache_file.stat().st_mtime
    mappings2 = fetch_interpro2go_mappings(cache_dir)
    assert cache_file.stat().st_mtime == original_mtime
    assert mappings == mappings2


def test_fetch_interpro2go_mappings_parsing(tmp_path):
    """Test parsing of InterPro2GO file format.

    The format is:
    InterPro:IPR000001 Kringle > GO:serine-type endopeptidase inhibitor activity ; GO:0004867
    """
    cache_dir = tmp_path / "cache"
    cache_dir.mkdir()

    # Create minimal test file
    test_content = """!date: 2025-01-15 $Revision: 1.2345 $
!Mapping of InterPro entries to GO
InterPro:IPR000001 Kringle > GO:serine-type endopeptidase inhibitor activity ; GO:0004867
InterPro:IPR000001 Kringle > GO:extracellular region ; GO:0005576
InterPro:IPR005982 Thioredoxin reductase > GO:thioredoxin-disulfide reductase (NADPH) activity ; GO:0004791
"""
    cache_file = cache_dir / "_interpro2go.txt"
    cache_file.write_text(test_content)

    mappings = fetch_interpro2go_mappings(cache_dir)

    # IPR000001 should have 2 GO mappings
    assert "IPR000001" in mappings
    assert len(mappings["IPR000001"]) == 2
    assert "GO:0004867" in mappings["IPR000001"]
    assert "GO:0005576" in mappings["IPR000001"]

    # IPR005982 should have 1 GO mapping
    assert "IPR005982" in mappings
    assert len(mappings["IPR005982"]) == 1
    assert "GO:0004791" in mappings["IPR005982"]


@pytest.mark.integration
def test_get_swissprot_count_for_interpro():
    """Test querying protein count for single InterPro ID.

    Tests the UniProt API query:
    (xref:interpro-{id}) AND (reviewed:true)
    """
    # Use a well-known InterPro domain
    count = get_swissprot_count_for_interpro("IPR005982")

    assert isinstance(count, int)
    assert count > 0
    # Thioredoxin reductase should have reasonable number of proteins
    assert count < 10000


@pytest.mark.integration
def test_get_swissprot_count_for_interpro_intersection():
    """Test querying protein count for InterPro intersection (AND query).

    Tests the UniProt API query with multiple domains:
    (xref:interpro-{id1}) AND (xref:interpro-{id2}) AND ... AND (reviewed:true)
    """
    # Test with two InterPro IDs from ARBA00026249
    interpro_ids = ["IPR005982", "IPR008255"]
    count = get_swissprot_count_for_interpro_intersection(interpro_ids)

    assert isinstance(count, int)
    assert count > 0

    # Intersection should be <= individual counts
    count_a = get_swissprot_count_for_interpro("IPR005982")
    count_b = get_swissprot_count_for_interpro("IPR008255")
    assert count <= count_a
    assert count <= count_b


@pytest.mark.integration
def test_get_swissprot_count_for_interpro_intersection_three_domains():
    """Test intersection with three InterPro domains from ARBA00026249."""
    # All three InterPro IDs from first condition set
    interpro_ids = ["IPR005982", "IPR008255", "IPR023753"]
    count = get_swissprot_count_for_interpro_intersection(interpro_ids)

    assert isinstance(count, int)
    assert count >= 0  # May be 0 if no proteins match all three


def test_calculate_jaccard_similarity_from_counts():
    """Test Jaccard calculation with known counts (unit test).

    Jaccard similarity = |A ∩ B| / |A ∪ B|
                       = |A ∩ B| / (|A| + |B| - |A ∩ B|)

    Example:
    - A has 100 proteins
    - B has 80 proteins
    - A ∩ B has 60 proteins
    - Jaccard = 60 / (100 + 80 - 60) = 60 / 120 = 0.5
    """
    # Mock the API calls by monkeypatching
    def mock_count_a(interpro_id, reviewed_only=True, request_delay=0.1):
        if interpro_id == "IPR_A":
            return 100
        elif interpro_id == "IPR_B":
            return 80
        return 0

    def mock_count_intersection(interpro_ids, reviewed_only=True, request_delay=0.1):
        if set(interpro_ids) == {"IPR_A", "IPR_B"}:
            return 60
        return 0

    import ai_gene_review.etl.rule_analysis as ra
    original_single = ra.get_swissprot_count_for_interpro
    original_inter = ra.get_swissprot_count_for_interpro_intersection

    try:
        ra.get_swissprot_count_for_interpro = mock_count_a
        ra.get_swissprot_count_for_interpro_intersection = mock_count_intersection

        similarity = calculate_jaccard_similarity("IPR_A", "IPR_B")
        assert similarity == pytest.approx(0.5, rel=0.01)
    finally:
        ra.get_swissprot_count_for_interpro = original_single
        ra.get_swissprot_count_for_interpro_intersection = original_inter


@pytest.mark.integration
def test_calculate_jaccard_similarity_arba00026249():
    """Test real Jaccard calculation for ARBA00026249 InterPro pairs.

    The rule has three InterPro IDs in the first condition set:
    - IPR005982: Thioredoxin reductase
    - IPR008255: Pyridine nucleotide-disulphide oxidoreductase, class-II, active site
    - IPR023753: FAD/NAD(P)-binding domain
    """
    # Test IPR005982 vs IPR008255
    similarity_12 = calculate_jaccard_similarity("IPR005982", "IPR008255")
    assert isinstance(similarity_12, float)
    assert 0.0 <= similarity_12 <= 1.0

    # Test IPR005982 vs IPR023753
    similarity_13 = calculate_jaccard_similarity("IPR005982", "IPR023753")
    assert isinstance(similarity_13, float)
    assert 0.0 <= similarity_13 <= 1.0

    # Test IPR008255 vs IPR023753
    similarity_23 = calculate_jaccard_similarity("IPR008255", "IPR023753")
    assert isinstance(similarity_23, float)
    assert 0.0 <= similarity_23 <= 1.0


@pytest.mark.integration
def test_analyze_interpro_overlap_in_condition_set(arba00026249_rule):
    """Test overlap analysis for condition set with 3 InterPro IDs.

    Should analyze all pairwise combinations and return:
    - Jaccard similarity for each pair
    - Containment ratios
    - Intersection protein counts
    """
    # Get first condition set (has 3 InterPro conditions)
    first_cs = arba00026249_rule.condition_sets[0]

    # Filter to only InterPro conditions
    interpro_conditions = [
        c for c in first_cs.conditions
        if c.condition_type == "InterPro id"
    ]
    assert len(interpro_conditions) == 3

    result = analyze_interpro_overlap_in_condition_set(first_cs)

    # Check result structure
    assert isinstance(result, dict)
    assert "pairs" in result
    assert "summary" in result

    # Should have 3 pairs: (A,B), (A,C), (B,C)
    pairs = result["pairs"]
    assert len(pairs) == 3

    # Each pair should have required metrics
    for pair in pairs:
        assert "condition_a" in pair
        assert "condition_b" in pair
        assert "protein_database" in pair
        assert "jaccard_similarity" in pair
        assert "intersection_count" in pair
        assert "a_minus_b_count" in pair
        assert "b_minus_a_count" in pair
        assert "containment_a_in_b" in pair
        assert "containment_b_in_a" in pair
        assert "interpretation" in pair

        # Validate metric ranges
        assert 0.0 <= pair["jaccard_similarity"] <= 1.0
        assert 0.0 <= pair["containment_a_in_b"] <= 1.0
        assert 0.0 <= pair["containment_b_in_a"] <= 1.0
        assert pair["intersection_count"] >= 0
        assert pair["a_minus_b_count"] >= 0
        assert pair["b_minus_a_count"] >= 0
        assert pair["protein_database"] == "SWISSPROT"


def test_analyze_ipr2go_redundancy(tmp_path):
    """Test checking if rule GO:0004791 is redundant with ipr2go mappings.

    ARBA00026249 annotates GO:0004791 based on InterPro conditions.
    If any of the InterPro domains already map to GO:0004791 in ipr2go,
    the rule annotation is redundant.
    """
    # Create test ipr2go mappings
    cache_dir = tmp_path / "cache"
    cache_dir.mkdir()

    test_content = """!date: 2025-01-15
InterPro:IPR005982 Thioredoxin reductase > GO:thioredoxin-disulfide reductase (NADPH) activity ; GO:0004791
InterPro:IPR008255 Active site > GO:oxidoreductase activity ; GO:0016491
InterPro:IPR023753 FAD binding > GO:FAD binding ; GO:0071949
"""
    cache_file = cache_dir / "_interpro2go.txt"
    cache_file.write_text(test_content)

    interpro_ids = ["IPR005982", "IPR008255", "IPR023753"]
    rule_go_ids = ["GO:0004791"]

    mappings = fetch_interpro2go_mappings(cache_dir)
    result = analyze_ipr2go_redundancy(interpro_ids, rule_go_ids, mappings)

    # Check result structure
    assert isinstance(result, dict)
    assert "redundant_annotations" in result
    assert "novel_annotations" in result
    assert "summary" in result

    # GO:0004791 should be redundant (already in IPR005982 mapping)
    redundant = result["redundant_annotations"]
    assert len(redundant) == 1
    assert redundant[0]["go_id"] == "GO:0004791"
    assert redundant[0]["interpro_source"] == "IPR005982"

    # No novel annotations
    assert len(result["novel_annotations"]) == 0


def test_analyze_ipr2go_redundancy_novel_annotation(tmp_path):
    """Test case where rule provides novel GO annotation."""
    cache_dir = tmp_path / "cache"
    cache_dir.mkdir()

    # ipr2go doesn't have the GO term the rule annotates
    test_content = """!date: 2025-01-15
InterPro:IPR005982 Domain > GO:some other term ; GO:0000001
"""
    cache_file = cache_dir / "_interpro2go.txt"
    cache_file.write_text(test_content)

    interpro_ids = ["IPR005982"]
    rule_go_ids = ["GO:0004791"]  # Not in ipr2go

    mappings = fetch_interpro2go_mappings(cache_dir)
    result = analyze_ipr2go_redundancy(interpro_ids, rule_go_ids, mappings)

    # GO:0004791 should be novel
    assert len(result["redundant_annotations"]) == 0
    assert len(result["novel_annotations"]) == 1
    assert "GO:0004791" in result["novel_annotations"]


@pytest.mark.integration
def test_analyze_rule_post_enrichment_arba00026249(tmp_path, arba00026249_rule):
    """Full end-to-end test with ARBA00026249.

    This is the main integration test that runs all 4 steps:
    1. Fetch SwissProt proteins for InterPro IDs
    2. Get ipr2go mappings
    3. Calculate overlap (Jaccard similarity)
    4. Analyze redundancy
    """
    result = analyze_rule_post_enrichment(arba00026249_rule, tmp_path)

    # Check top-level structure
    assert isinstance(result, dict)
    assert "rule_id" in result
    assert result["rule_id"] == "ARBA00026249"

    assert "condition_sets_summary" in result
    assert isinstance(result["condition_sets_summary"], list)

    # First condition set should have domain count and pair count info
    cs0_summary = result["condition_sets_summary"][0]
    assert "condition_set_index" in cs0_summary
    assert "domain_count" in cs0_summary
    assert "relevant_pair_count" in cs0_summary

    # Check domain overlap analysis structure
    assert "domain_overlap_analysis" in result
    overlap_analysis = result["domain_overlap_analysis"]
    assert "pairs" in overlap_analysis
    assert "summary" in overlap_analysis
    assert len(overlap_analysis["pairs"]) > 0

    # Check redundancy analysis
    assert "ipr2go_redundancy" in result
    redundancy = result["ipr2go_redundancy"]
    assert "redundant_annotations" in redundancy
    assert "novel_annotations" in redundancy
    assert "summary" in redundancy

    # Either some annotations are redundant or novel (or both)
    total_annotations = len(redundancy["redundant_annotations"]) + len(redundancy["novel_annotations"])
    assert total_annotations > 0


@pytest.mark.integration
def test_analyze_rule_post_enrichment_no_interpro(tmp_path):
    """Test analysis for rule with no InterPro conditions.

    Should handle gracefully and skip InterPro overlap analysis.
    """
    # Create minimal rule with no InterPro conditions
    from ai_gene_review.etl.arba import (
        Annotation,
        ARBARule,
        Condition,
        ConditionSet,
        ConditionValue,
        DBReference,
        Statistics,
    )

    rule = ARBARule(
        uni_rule_id="TEST00000001",
        version="1",
        condition_sets=[
            ConditionSet(
                conditions=[
                    Condition(
                        condition_type="taxon",
                        values=[ConditionValue(value="Bacteria", cv_id="2")],
                        is_negative=False
                    )
                ]
            )
        ],
        annotations=[
            Annotation(
                annotation_type="ANNOTATION",
                db_reference=DBReference(
                    database="GO",
                    ref_id="GO:0000001",
                    properties={}
                )
            )
        ],
        statistics=Statistics(),
        created_date="2025-01-01",
        modified_date="2025-01-01"
    )

    result = analyze_rule_post_enrichment(rule, tmp_path)

    assert result["rule_id"] == "TEST00000001"

    # Should have condition set summary but no InterPro overlap
    assert "condition_sets_summary" in result
    cs0_summary = result["condition_sets_summary"][0]
    assert cs0_summary["domain_count"] == 0  # No InterPro/FunFam/PANTHER conditions


def test_empty_condition_set():
    """Test handling of empty condition sets."""
    from ai_gene_review.etl.arba import ConditionSet

    cs = ConditionSet(conditions=[])
    result = analyze_interpro_overlap_in_condition_set(cs)

    assert result["pairs"] == []
    assert "summary" in result


def test_get_interpros_for_go():
    """Test reverse ipr2go lookup - finding InterPro IDs that map to a GO term."""
    mappings = {
        "IPR005982": ["GO:0004791"],
        "IPR006338": ["GO:0004791", "GO:0016491"],
        "IPR000001": ["GO:0000001"],
        "IPR008255": ["GO:0050660"],
    }

    # Should find both IPRs that map to GO:0004791
    result = get_interpros_for_go("GO:0004791", mappings)
    assert set(result) == {"IPR005982", "IPR006338"}

    # Should find only one IPR for GO:0016491
    result = get_interpros_for_go("GO:0016491", mappings)
    assert result == ["IPR006338"]

    # Should return empty list for unknown GO term
    result = get_interpros_for_go("GO:9999999", mappings)
    assert result == []


def test_get_interpros_for_go_empty_mappings():
    """Test reverse ipr2go lookup with empty mappings."""
    result = get_interpros_for_go("GO:0004791", {})
    assert result == []


@pytest.mark.integration
def test_external_iprs_included_in_analysis(tmp_path):
    """Test that external IPRs from ipr2go are included in overlap analysis."""
    # Use a real cached rule
    rule_file = Path("rules/arba/ARBA00026249/ARBA00026249.json")
    if not rule_file.exists():
        pytest.skip(f"Rule file not found: {rule_file}")

    import json
    from ai_gene_review.etl.arba import ARBARule

    data = json.loads(rule_file.read_text())
    rule = ARBARule.from_json(data)

    # Run analysis with external IPRs included (default)
    analysis = analyze_rule_post_enrichment(rule, Path("rules/arba"))

    # Should have external_ipr2go_domains section
    assert "external_ipr2go_domains" in analysis

    # The analysis should include external_ipr_ids in domain_overlap_analysis
    assert "external_ipr_ids" in analysis["domain_overlap_analysis"]

    # For GO:0004791, there should be some external IPRs (like IPR006338)
    external_ids = [x["interpro_id"] for x in analysis["external_ipr2go_domains"]]
    # Note: The actual external IPRs depend on the ipr2go file content
    # We just verify the structure is correct
    assert isinstance(external_ids, list)


@pytest.mark.integration
def test_external_iprs_in_pairs(tmp_path):
    """Test that external IPRs appear in pairwise overlap analysis."""
    # Use a real cached rule
    rule_file = Path("rules/arba/ARBA00026249/ARBA00026249.json")
    if not rule_file.exists():
        pytest.skip(f"Rule file not found: {rule_file}")

    import json
    from ai_gene_review.etl.arba import ARBARule

    data = json.loads(rule_file.read_text())
    rule = ARBARule.from_json(data)

    # Run analysis with external IPRs included
    analysis = analyze_rule_post_enrichment(rule, Path("rules/arba"))

    external_ipr_ids = analysis["domain_overlap_analysis"].get("external_ipr_ids", [])
    pairs = analysis["domain_overlap_analysis"]["pairs"]

    # If there are external IPRs, they should appear in pairwise comparisons
    if external_ipr_ids:
        # Find pairs involving external IPRs
        external_pairs = [
            p for p in pairs
            if p["condition_a"] in external_ipr_ids or p["condition_b"] in external_ipr_ids
        ]
        # External IPRs should be compared with rule domains and GO terms
        assert len(external_pairs) > 0, "External IPRs should appear in pairwise comparisons"

        # External IPRs should have empty condition_set membership
        for pair in external_pairs:
            if pair["condition_a"] in external_ipr_ids:
                assert pair["condition_a_in_sets"] == [], \
                    f"External IPR {pair['condition_a']} should have empty condition set membership"
            if pair["condition_b"] in external_ipr_ids:
                assert pair["condition_b_in_sets"] == [], \
                    f"External IPR {pair['condition_b']} should have empty condition set membership"
