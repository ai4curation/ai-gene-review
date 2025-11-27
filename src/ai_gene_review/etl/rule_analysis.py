"""Post-enrichment analysis for ARBA and UniRule rules.

This module provides deterministic analysis of UniProt rules including:
- Fetching InterPro2GO mappings from GO Consortium
- Querying UniProt API for protein counts and intersections
- Calculating Jaccard similarity for InterPro domain overlap
- Analyzing redundancy with existing ipr2go mappings

Example:
    >>> from ai_gene_review.etl.arba import ARBAClient
    >>> from ai_gene_review.etl.rule_analysis import analyze_rule_post_enrichment
    >>> from pathlib import Path
    >>>
    >>> client = ARBAClient()
    >>> rule = client.fetch_rule("ARBA00026249")
    >>> analysis = analyze_rule_post_enrichment(rule, Path("rules/arba"))
    >>> print(analysis["ipr2go_redundancy"]["summary"])
"""

import re
import time
from itertools import combinations
from pathlib import Path
from typing import Optional

import matplotlib.pyplot as plt
import numpy as np
import requests
import seaborn as sns
import yaml
from scipy.cluster import hierarchy
from scipy.spatial.distance import squareform

from ai_gene_review.etl.arba import ARBARule, ConditionSet


# API endpoints
UNIPROT_SEARCH_API = "https://rest.uniprot.org/uniprotkb/search"
UNIPROT_SPARQL_ENDPOINT = "https://sparql.uniprot.org/sparql"
INTERPRO2GO_URL = "http://geneontology.org/external2go/interpro2go"


def fetch_interpro2go_mappings(cache_dir: Path) -> dict[str, list[str]]:
    """Download and parse InterPro2GO mappings from official file.

    The InterPro2GO file maps InterPro entries to GO terms. Format:
    InterPro:IPR000001 Kringle > GO:serine-type endopeptidase inhibitor activity ; GO:0004867

    Args:
        cache_dir: Directory for caching the downloaded file

    Returns:
        Dict mapping InterPro IDs to lists of GO IDs

    Example:
        >>> from pathlib import Path
        >>> mappings = fetch_interpro2go_mappings(Path("rules/arba"))
        >>> "IPR000001" in mappings
        True
        >>> all(go_id.startswith("GO:") for go_ids in mappings.values() for go_id in go_ids)
        True
    """
    cache_file = Path(cache_dir) / "_interpro2go.txt"

    # Download if not cached
    if not cache_file.exists():
        cache_file.parent.mkdir(parents=True, exist_ok=True)
        response = requests.get(INTERPRO2GO_URL, timeout=60)
        response.raise_for_status()
        cache_file.write_text(response.text)

    # Parse the file
    mappings: dict[str, list[str]] = {}
    content = cache_file.read_text()

    for line in content.split("\n"):
        line = line.strip()

        # Skip comments and empty lines
        if not line or line.startswith("!"):
            continue

        # Parse format: InterPro:IPR000001 Kringle > GO:name ; GO:0004867
        match = re.match(r"InterPro:(IPR\d+)\s+.*?;\s+(GO:\d+)", line)
        if match:
            interpro_id = match.group(1)
            go_id = match.group(2)

            if interpro_id not in mappings:
                mappings[interpro_id] = []
            mappings[interpro_id].append(go_id)

    return mappings


def get_swissprot_count_for_interpro(
    interpro_id: str,
    reviewed_only: bool = True,
    request_delay: float = 0.1
) -> int:
    """Query UniProt API for protein count matching InterPro ID.

    Uses UniProt query: (xref:interpro-{id}) AND (reviewed:true)
    Returns count from X-Total-Results header without fetching proteins.

    Args:
        interpro_id: InterPro identifier (e.g., "IPR005982")
        reviewed_only: Only count SwissProt (reviewed) proteins
        request_delay: Delay after request to avoid rate limiting

    Returns:
        Number of matching proteins

    Example:
        >>> count = get_swissprot_count_for_interpro("IPR005982")
        >>> count > 0
        True
    """
    query_parts = [f"(xref:interpro-{interpro_id})"]
    if reviewed_only:
        query_parts.append("(reviewed:true)")

    query = " AND ".join(query_parts)

    params = {
        "query": query,
        "size": 1  # Only need count from header
    }

    response = requests.get(UNIPROT_SEARCH_API, params=params, timeout=30)
    response.raise_for_status()

    count = int(response.headers.get("X-Total-Results", 0))

    if request_delay > 0:
        time.sleep(request_delay)

    return count


def get_swissprot_count_for_funfam(
    funfam_id: str,
    reviewed_only: bool = True,
    request_delay: float = 0.1
) -> int:
    """Query UniProt API for protein count matching FunFam ID.

    Uses UniProt text search with quoted FunFam ID (e.g., "3.50.50.60:FF:000064").
    FunFam IDs are stored in UniProt's FunFam database cross-references and are
    searchable via text queries but not structured xref queries.

    Args:
        funfam_id: FunFam identifier (e.g., "3.50.50.60:FF:000064")
        reviewed_only: Only count SwissProt (reviewed) proteins
        request_delay: Delay after request to avoid rate limiting

    Returns:
        Number of matching proteins

    Example:
        >>> count = get_swissprot_count_for_funfam("3.50.50.60:FF:000064")
        >>> count >= 0
        True
    """
    query_parts = [f'("{funfam_id}")']
    if reviewed_only:
        query_parts.append("(reviewed:true)")

    query = " AND ".join(query_parts)

    params = {
        "query": query,
        "size": 1  # Only need count from header
    }

    response = requests.get(UNIPROT_SEARCH_API, params=params, timeout=30)
    response.raise_for_status()

    count = int(response.headers.get("X-Total-Results", 0))

    if request_delay > 0:
        time.sleep(request_delay)

    return count


def get_swissprot_count_for_interpro_intersection(
    interpro_ids: list[str],
    reviewed_only: bool = True,
    request_delay: float = 0.1
) -> int:
    """Query UniProt API for protein count matching ALL InterPro IDs.

    Uses UniProt query: (xref:interpro-{id1}) AND (xref:interpro-{id2}) AND ...
    Returns intersection count without fetching actual proteins.

    Args:
        interpro_ids: List of InterPro identifiers
        reviewed_only: Only count SwissProt (reviewed) proteins
        request_delay: Delay after request to avoid rate limiting

    Returns:
        Number of proteins matching all InterPro IDs

    Example:
        >>> count = get_swissprot_count_for_interpro_intersection(["IPR005982", "IPR008255"])
        >>> count >= 0
        True
    """
    if not interpro_ids:
        return 0

    query_parts = [f"(xref:interpro-{ipr_id})" for ipr_id in interpro_ids]
    if reviewed_only:
        query_parts.append("(reviewed:true)")

    query = " AND ".join(query_parts)

    params = {
        "query": query,
        "size": 1  # Only need count from header
    }

    response = requests.get(UNIPROT_SEARCH_API, params=params, timeout=30)
    response.raise_for_status()

    count = int(response.headers.get("X-Total-Results", 0))

    if request_delay > 0:
        time.sleep(request_delay)

    return count


def get_swissprot_count_for_mixed_conditions(
    conditions: list[tuple[str, str]],
    reviewed_only: bool = True,
    request_delay: float = 0.1
) -> int:
    """Query UniProt API for protein count matching mixed domain conditions.

    Supports both InterPro IDs (structured xref) and FunFam IDs (text search).
    Each condition is a tuple of (condition_type, condition_id).

    Args:
        conditions: List of (type, id) tuples, where type is "interpro" or "funfam"
        reviewed_only: Only count SwissProt (reviewed) proteins
        request_delay: Delay after request to avoid rate limiting

    Returns:
        Number of proteins matching all conditions

    Example:
        >>> count = get_swissprot_count_for_mixed_conditions([
        ...     ("interpro", "IPR005982"),
        ...     ("funfam", "3.50.50.60:FF:000064")
        ... ])
        >>> count >= 0
        True
    """
    if not conditions:
        return 0

    query_parts = []
    for condition_type, condition_id in conditions:
        if condition_type == "interpro":
            query_parts.append(f"(xref:interpro-{condition_id})")
        elif condition_type == "funfam":
            query_parts.append(f'("{condition_id}")')
        else:
            raise ValueError(f"Unknown condition type: {condition_type}")

    if reviewed_only:
        query_parts.append("(reviewed:true)")

    query = " AND ".join(query_parts)

    params = {
        "query": query,
        "size": 1  # Only need count from header
    }

    response = requests.get(UNIPROT_SEARCH_API, params=params, timeout=30)
    response.raise_for_status()

    count = int(response.headers.get("X-Total-Results", 0))

    if request_delay > 0:
        time.sleep(request_delay)

    return count


def calculate_jaccard_similarity(
    interpro_a: str,
    interpro_b: str,
    request_delay: float = 0.1
) -> float:
    """Calculate Jaccard similarity between two InterPro domains.

    Jaccard similarity = |A ∩ B| / |A ∪ B|
                       = |A ∩ B| / (|A| + |B| - |A ∩ B|)

    Uses UniProt API queries to get counts without fetching proteins.

    Args:
        interpro_a: First InterPro ID
        interpro_b: Second InterPro ID
        request_delay: Delay between API requests

    Returns:
        Jaccard similarity coefficient (0.0 to 1.0)

    Example:
        >>> similarity = calculate_jaccard_similarity("IPR005982", "IPR008255")
        >>> 0.0 <= similarity <= 1.0
        True
    """
    count_a = get_swissprot_count_for_interpro(interpro_a, request_delay=request_delay)
    count_b = get_swissprot_count_for_interpro(interpro_b, request_delay=request_delay)
    count_intersection = get_swissprot_count_for_interpro_intersection(
        [interpro_a, interpro_b],
        request_delay=request_delay
    )

    # Handle edge case: no proteins
    if count_a == 0 and count_b == 0:
        return 0.0

    # Jaccard = intersection / union
    union_size = count_a + count_b - count_intersection
    if union_size == 0:
        return 0.0

    return count_intersection / union_size


def analyze_interpro_overlap_in_condition_set(
    condition_set: ConditionSet,
    request_delay: float = 0.1
) -> dict:
    """Analyze overlap for all domain condition pairs in a conjunctive condition set.

    Supports both InterPro and FunFam conditions. For each pair of domain conditions
    in the set, calculate:
    - Jaccard similarity
    - Containment ratios (A in B, B in A)
    - Intersection protein count
    - Set differences (uniqueness metrics)

    Args:
        condition_set: ConditionSet containing InterPro and/or FunFam conditions
        request_delay: Delay between API requests

    Returns:
        Dict with pairwise statistics and summary

    Example:
        >>> from ai_gene_review.etl.arba import ConditionSet, Condition, ConditionValue
        >>> cs = ConditionSet(conditions=[
        ...     Condition(condition_type="InterPro id", values=[ConditionValue(value="IPR005982")], is_negative=False),
        ...     Condition(condition_type="InterPro id", values=[ConditionValue(value="IPR008255")], is_negative=False)
        ... ])
        >>> result = analyze_interpro_overlap_in_condition_set(cs)
        >>> "pairs" in result and "summary" in result
        True
    """
    # Extract domain conditions (InterPro and FunFam)
    domain_conditions = []
    for condition in condition_set.conditions:
        if condition.condition_type == "InterPro id":
            for cv in condition.values:
                domain_conditions.append(("interpro", cv.value))
        elif condition.condition_type == "FunFam id":
            for cv in condition.values:
                domain_conditions.append(("funfam", cv.value))

    # No analysis needed if < 2 domain conditions
    if len(domain_conditions) < 2:
        return {
            "pairs": [],
            "summary": f"Atomic clause (only {len(domain_conditions)} domain condition), no pairwise analysis"
        }

    # Analyze all pairwise combinations
    pairs_analysis = []
    for (type_a, id_a), (type_b, id_b) in combinations(domain_conditions, 2):
        # Get individual counts
        if type_a == "interpro":
            count_a = get_swissprot_count_for_interpro(id_a, request_delay=request_delay)
        else:  # funfam
            count_a = get_swissprot_count_for_funfam(id_a, request_delay=request_delay)

        if type_b == "interpro":
            count_b = get_swissprot_count_for_interpro(id_b, request_delay=request_delay)
        else:  # funfam
            count_b = get_swissprot_count_for_funfam(id_b, request_delay=request_delay)

        # Get intersection count using mixed conditions
        count_intersection = get_swissprot_count_for_mixed_conditions(
            [(type_a, id_a), (type_b, id_b)],
            request_delay=request_delay
        )

        # Calculate metrics
        jaccard = count_intersection / (count_a + count_b - count_intersection) if (count_a + count_b - count_intersection) > 0 else 0.0
        containment_a_in_b = count_intersection / count_a if count_a > 0 else 0.0
        containment_b_in_a = count_intersection / count_b if count_b > 0 else 0.0

        # Calculate set differences (uniqueness metrics)
        a_minus_b_count = count_a - count_intersection
        b_minus_a_count = count_b - count_intersection

        # Determine interpretation
        if count_intersection == 0:
            interpretation = "DISJOINT"
        elif jaccard > 0.9:
            interpretation = "REDUNDANT"
        elif containment_a_in_b > 0.95 or containment_b_in_a > 0.95:
            interpretation = "SUBSET"
        elif jaccard > 0.5:
            interpretation = "HIGH_OVERLAP"
        elif jaccard > 0.2:
            interpretation = "MODERATE"
        else:
            interpretation = "LOW"

        pairs_analysis.append({
            "condition_a": id_a,
            "condition_b": id_b,
            "protein_database": "SWISSPROT",
            "count_a": count_a,
            "count_b": count_b,
            "intersection_count": count_intersection,
            "a_minus_b_count": a_minus_b_count,
            "b_minus_a_count": b_minus_a_count,
            "jaccard_similarity": jaccard,
            "containment_a_in_b": containment_a_in_b,
            "containment_b_in_a": containment_b_in_a,
            "interpretation": interpretation
        })

    # Generate summary
    avg_jaccard = sum(p["jaccard_similarity"] for p in pairs_analysis) / len(pairs_analysis) if pairs_analysis else 0.0
    high_overlap_pairs = [p for p in pairs_analysis if p["jaccard_similarity"] > 0.5]

    summary = f"Analyzed {len(pairs_analysis)} domain pairs. "
    summary += f"Average Jaccard similarity: {avg_jaccard:.3f}. "
    summary += f"{len(high_overlap_pairs)} pairs with >50% overlap."

    return {
        "pairs": pairs_analysis,
        "summary": summary
    }


def analyze_ipr2go_redundancy(
    interpro_ids: list[str],
    rule_go_ids: list[str],
    ipr2go_mappings: dict[str, list[str]]
) -> dict:
    """Analyze if rule GO annotations are redundant with ipr2go mappings.

    Check if any InterPro in conditions already maps to the GO terms
    that the rule annotates. If so, the rule is redundant.

    Args:
        interpro_ids: List of InterPro IDs from rule conditions
        rule_go_ids: List of GO IDs the rule annotates
        ipr2go_mappings: InterPro2GO mappings dict

    Returns:
        Dict with redundant_annotations, novel_annotations, and summary

    Example:
        >>> mappings = {"IPR005982": ["GO:0004791"]}
        >>> result = analyze_ipr2go_redundancy(
        ...     ["IPR005982"], ["GO:0004791"], mappings
        ... )
        >>> len(result["redundant_annotations"]) > 0
        True
    """
    redundant = []
    novel = []

    for go_id in rule_go_ids:
        is_redundant = False

        # Check if any InterPro already maps to this GO term
        for interpro_id in interpro_ids:
            if interpro_id in ipr2go_mappings:
                if go_id in ipr2go_mappings[interpro_id]:
                    redundant.append({
                        "go_id": go_id,
                        "interpro_source": interpro_id
                    })
                    is_redundant = True
                    break

        if not is_redundant:
            novel.append(go_id)

    # Generate summary
    if redundant:
        summary = f"{len(redundant)} redundant annotation(s) (already in ipr2go). "
    else:
        summary = "No redundant annotations. "

    if novel:
        summary += f"{len(novel)} novel annotation(s) not in ipr2go."
    else:
        summary += "All annotations already in ipr2go."

    return {
        "redundant_annotations": redundant,
        "novel_annotations": novel,
        "summary": summary
    }


def analyze_all_domain_pairs(
    rule: ARBARule,
    request_delay: float = 0.1
) -> dict:
    """Analyze all pairwise overlaps between domain conditions across entire rule.

    Extracts all domain conditions (InterPro and FunFam) from all condition sets,
    then performs pairwise overlap analysis. This flattened approach catches
    redundancy anywhere in the rule's boolean structure.

    Args:
        rule: ARBARule object to analyze
        request_delay: Delay between API requests

    Returns:
        Dict with pairs analysis and summary

    Example:
        >>> from ai_gene_review.etl.arba import ARBAClient
        >>> from pathlib import Path
        >>> client = ARBAClient()
        >>> rule = client.fetch_rule("ARBA00026249")
        >>> analysis = analyze_all_domain_pairs(rule)
        >>> "pairs" in analysis and "summary" in analysis
        True
    """
    # Collect all domain conditions from all condition sets
    all_domain_conditions = []
    condition_set_membership = {}  # Maps (type, id) -> list of condition set indices

    for cs_idx, cs in enumerate(rule.condition_sets):
        for condition in cs.conditions:
            if condition.condition_type == "InterPro id":
                for cv in condition.values:
                    domain_key = ("interpro", cv.value)
                    if domain_key not in [dc for dc in all_domain_conditions]:
                        all_domain_conditions.append(domain_key)
                    if domain_key not in condition_set_membership:
                        condition_set_membership[domain_key] = []
                    if cs_idx not in condition_set_membership[domain_key]:
                        condition_set_membership[domain_key].append(cs_idx)

            elif condition.condition_type == "FunFam id":
                for cv in condition.values:
                    domain_key = ("funfam", cv.value)
                    if domain_key not in [dc for dc in all_domain_conditions]:
                        all_domain_conditions.append(domain_key)
                    if domain_key not in condition_set_membership:
                        condition_set_membership[domain_key] = []
                    if cs_idx not in condition_set_membership[domain_key]:
                        condition_set_membership[domain_key].append(cs_idx)

    # No analysis if < 2 domain conditions total
    if len(all_domain_conditions) < 2:
        return {
            "pairs": [],
            "summary": f"Only {len(all_domain_conditions)} domain condition(s) in entire rule"
        }

    # Analyze all pairwise combinations
    pairs_analysis = []
    for (type_a, id_a), (type_b, id_b) in combinations(all_domain_conditions, 2):
        # Get individual counts
        if type_a == "interpro":
            count_a = get_swissprot_count_for_interpro(id_a, request_delay=request_delay)
        else:  # funfam
            count_a = get_swissprot_count_for_funfam(id_a, request_delay=request_delay)

        if type_b == "interpro":
            count_b = get_swissprot_count_for_interpro(id_b, request_delay=request_delay)
        else:  # funfam
            count_b = get_swissprot_count_for_funfam(id_b, request_delay=request_delay)

        # Get intersection count
        count_intersection = get_swissprot_count_for_mixed_conditions(
            [(type_a, id_a), (type_b, id_b)],
            request_delay=request_delay
        )

        # Calculate metrics
        jaccard = count_intersection / (count_a + count_b - count_intersection) if (count_a + count_b - count_intersection) > 0 else 0.0
        containment_a_in_b = count_intersection / count_a if count_a > 0 else 0.0
        containment_b_in_a = count_intersection / count_b if count_b > 0 else 0.0

        # Calculate set differences
        a_minus_b_count = count_a - count_intersection
        b_minus_a_count = count_b - count_intersection

        # Determine interpretation
        if count_intersection == 0:
            interpretation = "DISJOINT"
        elif jaccard > 0.9:
            interpretation = "REDUNDANT"
        elif containment_a_in_b > 0.95 or containment_b_in_a > 0.95:
            interpretation = "SUBSET"
        elif jaccard > 0.5:
            interpretation = "HIGH_OVERLAP"
        elif jaccard > 0.2:
            interpretation = "MODERATE"
        else:
            interpretation = "LOW"

        pairs_analysis.append({
            "condition_a": id_a,
            "condition_b": id_b,
            "condition_a_in_sets": condition_set_membership[(type_a, id_a)],
            "condition_b_in_sets": condition_set_membership[(type_b, id_b)],
            "protein_database": "SWISSPROT",
            "count_a": count_a,
            "count_b": count_b,
            "intersection_count": count_intersection,
            "a_minus_b_count": a_minus_b_count,
            "b_minus_a_count": b_minus_a_count,
            "jaccard_similarity": jaccard,
            "containment_a_in_b": containment_a_in_b,
            "containment_b_in_a": containment_b_in_a,
            "interpretation": interpretation
        })

    # Generate summary
    avg_jaccard = sum(p["jaccard_similarity"] for p in pairs_analysis) / len(pairs_analysis) if pairs_analysis else 0.0
    high_overlap_pairs = [p for p in pairs_analysis if p["jaccard_similarity"] > 0.5]
    subset_pairs = [p for p in pairs_analysis if p["interpretation"] == "SUBSET"]

    summary = f"Analyzed {len(pairs_analysis)} domain pairs across entire rule. "
    summary += f"Average Jaccard similarity: {avg_jaccard:.3f}. "
    summary += f"{len(high_overlap_pairs)} pairs with >50% overlap, "
    summary += f"{len(subset_pairs)} subset relationships."

    return {
        "pairs": pairs_analysis,
        "summary": summary
    }


def analyze_rule_post_enrichment(
    rule: ARBARule,
    cache_dir: Path,
    request_delay: float = 0.1
) -> dict:
    """Main analysis function - runs all steps deterministically.

    Steps:
    1. Flatten all domain conditions and analyze all pairwise overlaps
    2. Get ipr2go mappings from cached file
    3. Analyze redundancy with ipr2go mappings
    4. Summarize findings per condition set

    Args:
        rule: ARBARule object to analyze
        cache_dir: Directory for caching ipr2go file
        request_delay: Delay between API requests

    Returns:
        Complete analysis dict suitable for adding to enriched JSON

    Example:
        >>> from ai_gene_review.etl.arba import ARBAClient
        >>> from pathlib import Path
        >>> client = ARBAClient()
        >>> rule = client.fetch_rule("ARBA00026249")
        >>> analysis = analyze_rule_post_enrichment(rule, Path("rules/arba"))
        >>> "rule_id" in analysis and "ipr2go_redundancy" in analysis
        True
    """
    # Fetch ipr2go mappings
    ipr2go_mappings = fetch_interpro2go_mappings(cache_dir)

    # Analyze all domain pairs across entire rule (flattened)
    all_pairs_analysis = analyze_all_domain_pairs(rule, request_delay=request_delay)

    # Collect all InterPro IDs for ipr2go analysis
    all_interpro_ids = []
    for cs in rule.condition_sets:
        for condition in cs.conditions:
            if condition.condition_type == "InterPro id":
                for cv in condition.values:
                    if cv.value not in all_interpro_ids:
                        all_interpro_ids.append(cv.value)

    # Analyze ipr2go redundancy
    rule_go_ids = rule.get_go_ids()
    redundancy_analysis = analyze_ipr2go_redundancy(
        all_interpro_ids,
        rule_go_ids,
        ipr2go_mappings
    )

    # Build per-condition-set summaries (narrative only, no duplicate pair data)
    condition_sets_summary = []
    for cs_idx, cs in enumerate(rule.condition_sets):
        # Extract domain conditions in this set
        cs_domains = []
        for condition in cs.conditions:
            if condition.condition_type == "InterPro id":
                cs_domains.extend([("interpro", cv.value) for cv in condition.values])
            elif condition.condition_type == "FunFam id":
                cs_domains.extend([("funfam", cv.value) for cv in condition.values])

        # Find relevant pairs involving this condition set's domains
        relevant_pairs = []
        for pair in all_pairs_analysis.get("pairs", []):
            if cs_idx in pair["condition_a_in_sets"] or cs_idx in pair["condition_b_in_sets"]:
                relevant_pairs.append({
                    "condition_a": pair["condition_a"],
                    "condition_b": pair["condition_b"],
                    "interpretation": pair["interpretation"]
                })

        condition_sets_summary.append({
            "condition_set_index": cs_idx,
            "domain_count": len(cs_domains),
            "relevant_pair_count": len(relevant_pairs),
            "notes": f"Condition set {cs_idx} has {len(cs_domains)} domain condition(s), involved in {len(relevant_pairs)} pairwise comparison(s)"
        })

    return {
        "rule_id": rule.uni_rule_id,
        "domain_overlap_analysis": all_pairs_analysis,
        "condition_sets_summary": condition_sets_summary,
        "ipr2go_redundancy": redundancy_analysis
    }


def export_analysis_to_yaml(analysis: dict, output_path: Path) -> None:
    """Export analysis results to YAML file.

    Args:
        analysis: Analysis dict from analyze_rule_post_enrichment
        output_path: Path to write YAML file

    Example:
        >>> from pathlib import Path
        >>> from ai_gene_review.etl.arba import ARBAClient
        >>> client = ARBAClient()
        >>> rule = client.fetch_rule("ARBA00026249")
        >>> analysis = analyze_rule_post_enrichment(rule, Path("rules/arba"))
        >>> export_analysis_to_yaml(analysis, Path("/tmp/analysis.yaml"))
    """
    with open(output_path, 'w') as f:
        yaml.dump(analysis, f, default_flow_style=False, sort_keys=False, allow_unicode=True)


def format_analysis_as_text(analysis: dict) -> str:
    """Format analysis results as human-readable text.

    Args:
        analysis: Analysis dict from analyze_rule_post_enrichment

    Returns:
        Formatted text report

    Example:
        >>> analysis = {"rule_id": "ARBA00026249", "domain_overlap_analysis": {"pairs": [], "summary": "Test"}, "condition_sets_summary": [], "ipr2go_redundancy": {"summary": "Test", "redundant_annotations": [], "novel_annotations": []}}
        >>> text = format_analysis_as_text(analysis)
        >>> "ARBA00026249" in text
        True
    """
    lines = []
    lines.append(f"Rule Analysis: {analysis['rule_id']}")
    lines.append("=" * 60)
    lines.append("")

    # Domain overlap section (flattened, all pairs)
    lines.append("Domain Overlap Analysis (All Pairs):")
    lines.append("-" * 60)
    domain_analysis = analysis["domain_overlap_analysis"]
    lines.append(f"Summary: {domain_analysis['summary']}")
    lines.append("")

    if domain_analysis["pairs"]:
        for pair in domain_analysis["pairs"]:
            lines.append(f"{pair['condition_a']} ↔ {pair['condition_b']}:")
            lines.append(f"  Appears in condition sets: {pair['condition_a_in_sets']} / {pair['condition_b_in_sets']}")
            lines.append(f"  Database: {pair['protein_database']}")
            lines.append(f"  Counts: {pair['count_a']} / {pair['count_b']}")
            lines.append(f"  Intersection: {pair['intersection_count']}")
            lines.append(f"  Set differences: |A-B| = {pair['a_minus_b_count']}, |B-A| = {pair['b_minus_a_count']}")
            lines.append(f"  Jaccard similarity: {pair['jaccard_similarity']:.3f}")
            lines.append(f"  Containment: A in B = {pair['containment_a_in_b']:.3f}, B in A = {pair['containment_b_in_a']:.3f}")
            lines.append(f"  Interpretation: {pair['interpretation']}")
            lines.append("")

    # Condition set summaries
    lines.append("Condition Set Summaries:")
    lines.append("-" * 60)
    for cs_summary in analysis["condition_sets_summary"]:
        lines.append(f"Condition Set {cs_summary['condition_set_index']}: {cs_summary['notes']}")
    lines.append("")

    # InterPro2GO redundancy
    lines.append("InterPro2GO Redundancy Analysis:")
    lines.append("-" * 60)
    redundancy = analysis["ipr2go_redundancy"]
    lines.append(f"Summary: {redundancy['summary']}")
    lines.append("")

    if redundancy["redundant_annotations"]:
        lines.append("Redundant annotations:")
        for annot in redundancy["redundant_annotations"]:
            lines.append(f"  - {annot['go_id']} (already mapped by {annot['interpro_source']})")

    if redundancy["novel_annotations"]:
        lines.append("")
        lines.append("Novel annotations:")
        for go_id in redundancy["novel_annotations"]:
            lines.append(f"  - {go_id}")

    return "\n".join(lines)


def plot_domain_overlap_heatmap(
    analysis: dict,
    output_path: Optional[Path] = None,
    figsize: tuple[float, float] = (12, 10)
) -> None:
    """Generate asymmetric heatmap showing domain containment relationships.

    Creates a heatmap where cell (i,j) shows the containment of domain i in domain j
    (i.e., what fraction of proteins with domain i also have domain j).
    Domains are clustered by condition set and then by similarity within each set.

    Args:
        analysis: Analysis dict from analyze_rule_post_enrichment
        output_path: Optional path to save figure (PNG format)
        figsize: Figure size in inches (width, height)

    Example:
        >>> from ai_gene_review.etl.arba import ARBAClient
        >>> from pathlib import Path
        >>> client = ARBAClient()
        >>> rule = client.fetch_rule("ARBA00026249")
        >>> analysis = analyze_rule_post_enrichment(rule, Path("rules/arba"))
        >>> plot_domain_overlap_heatmap(analysis, Path("heatmap.png"))
    """
    pairs = analysis["domain_overlap_analysis"]["pairs"]

    if not pairs:
        print("No domain pairs to visualize")
        return

    # Extract all unique domains and their condition set membership
    domain_to_sets = {}
    for pair in pairs:
        domain_a = pair["condition_a"]
        domain_b = pair["condition_b"]

        if domain_a not in domain_to_sets:
            domain_to_sets[domain_a] = pair["condition_a_in_sets"]
        if domain_b not in domain_to_sets:
            domain_to_sets[domain_b] = pair["condition_b_in_sets"]

    # Sort domains by condition set, then alphabetically
    domains = sorted(
        domain_to_sets.keys(),
        key=lambda d: (min(domain_to_sets[d]), d)
    )

    n_domains = len(domains)

    # Build containment matrix: containment[i,j] = fraction of proteins with domain i that also have domain j
    containment_matrix = np.zeros((n_domains, n_domains))

    # Fill diagonal with 1.0 (perfect self-containment)
    np.fill_diagonal(containment_matrix, 1.0)

    # Build index mapping
    domain_to_idx = {d: i for i, d in enumerate(domains)}

    # Fill matrix from pairwise data
    for pair in pairs:
        i = domain_to_idx[pair["condition_a"]]
        j = domain_to_idx[pair["condition_b"]]

        # containment[i,j] = what fraction of i is contained in j
        containment_matrix[i, j] = pair["containment_a_in_b"]
        # containment[j,i] = what fraction of j is contained in i
        containment_matrix[j, i] = pair["containment_b_in_a"]

    # Create figure
    fig, ax = plt.subplots(figsize=figsize)

    # Create heatmap with asymmetric colormap (white=0, dark=1)
    sns.heatmap(
        containment_matrix,
        xticklabels=domains,
        yticklabels=domains,
        annot=True,
        fmt=".2f",
        cmap="YlOrRd",
        vmin=0,
        vmax=1,
        cbar_kws={"label": "Containment (fraction of row domain in column domain)"},
        square=True,
        linewidths=0.5,
        linecolor='gray',
        ax=ax
    )

    # Add condition set separators
    # Find positions where condition set changes
    cs_boundaries = []
    prev_cs = None
    for i, domain in enumerate(domains):
        curr_cs = min(domain_to_sets[domain])
        if prev_cs is not None and curr_cs != prev_cs:
            cs_boundaries.append(i)
        prev_cs = curr_cs

    # Draw separator lines
    for boundary in cs_boundaries:
        ax.axhline(y=boundary, color='black', linewidth=2)
        ax.axvline(x=boundary, color='black', linewidth=2)

    # Add condition set labels on the side
    cs_labels = []
    cs_positions = []
    prev_boundary = 0
    for boundary in cs_boundaries + [n_domains]:
        # Find which condition set this section represents
        mid_idx = (prev_boundary + boundary) // 2
        cs_num = min(domain_to_sets[domains[mid_idx]])
        cs_labels.append(f"CS{cs_num}")
        cs_positions.append((prev_boundary + boundary) / 2)
        prev_boundary = boundary

    # Add secondary y-axis for condition set labels
    ax2 = ax.twinx()
    ax2.set_ylim(ax.get_ylim())
    ax2.set_yticks(cs_positions)
    ax2.set_yticklabels(cs_labels)
    ax2.set_ylabel("Condition Set", rotation=270, labelpad=20)

    # Rotate x-axis labels
    plt.setp(ax.xaxis.get_majorticklabels(), rotation=45, ha='right')

    # Set titles and labels
    ax.set_xlabel("Domain (Column)")
    ax.set_ylabel("Domain (Row)")
    ax.set_title(
        f"Domain Containment Matrix: {analysis['rule_id']}\n"
        f"Cell (i,j) = fraction of proteins with domain i that also have domain j",
        pad=20
    )

    plt.tight_layout()

    if output_path:
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        print(f"Heatmap saved to {output_path}")
    else:
        plt.show()

    plt.close()
