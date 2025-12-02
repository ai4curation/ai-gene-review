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
import json
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


def get_swissprot_count_for_go(
    go_id: str,
    reviewed_only: bool = True,
    request_delay: float = 0.1
) -> int:
    """Query UniProt API for protein count annotated with a GO term.

    Uses UniProt query: (go:{numeric_id}) AND (reviewed:true)
    Returns count from X-Total-Results header without fetching proteins.

    Args:
        go_id: GO identifier (e.g., "GO:0003674")
        reviewed_only: Only count SwissProt (reviewed) proteins
        request_delay: Delay after request to avoid rate limiting

    Returns:
        Number of matching proteins

    Example:
        >>> count = get_swissprot_count_for_go("GO:0003674")
        >>> count > 0
        True
    """
    # UniProt expects numeric ID without "GO:" prefix
    numeric_id = go_id.replace('GO:', '') if go_id.startswith('GO:') else go_id
    query_parts = [f"(go:{numeric_id})"]
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

    Supports InterPro IDs (structured xref), FunFam IDs (text search), and GO terms (annotation).
    Each condition is a tuple of (condition_type, condition_id).

    Args:
        conditions: List of (type, id) tuples, where type is "interpro", "funfam", or "go"
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
        elif condition_type == "go":
            # UniProt expects numeric ID without "GO:" prefix
            numeric_id = condition_id.replace('GO:', '') if condition_id.startswith('GO:') else condition_id
            query_parts.append(f"(go:{numeric_id})")
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


def get_interpro_name(interpro_id: str, request_delay: float = 0.1) -> str:
    """Fetch InterPro entry name from InterPro API.

    Args:
        interpro_id: InterPro identifier (e.g., "IPR005982")
        request_delay: Delay after request to avoid rate limiting

    Returns:
        InterPro entry name, or the ID itself if fetch fails

    Example:
        >>> name = get_interpro_name("IPR005982")
        >>> len(name) > 0
        True
    """
    try:
        url = f"https://www.ebi.ac.uk/interpro/api/entry/InterPro/{interpro_id}/"
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        data = response.json()

        if request_delay > 0:
            time.sleep(request_delay)

        return data.get("metadata", {}).get("name", interpro_id)
    except Exception:
        # If fetch fails, return the ID
        return interpro_id


def get_funfam_name(funfam_id: str) -> str:
    """Get a descriptive name for a FunFam ID.

    FunFam IDs don't have official human-readable names in CATH database.
    This function returns the superfamily portion as a semi-descriptive label.

    Args:
        funfam_id: FunFam identifier (e.g., "3.50.50.60:FF:000064")

    Returns:
        Superfamily ID extracted from FunFam ID

    Example:
        >>> name = get_funfam_name("3.50.50.60:FF:000064")
        >>> name
        'CATH 3.50.50.60'
    """
    # FunFam format: superfamily:FF:number
    # Extract superfamily portion
    if ":FF:" in funfam_id:
        superfamily = funfam_id.split(":FF:")[0]
        return f"CATH {superfamily}"
    return funfam_id


def fetch_domain_names(
    domain_ids: list[str],
    request_delay: float = 0.1
) -> dict[str, str]:
    """Fetch names for a list of domain IDs (InterPro or FunFam).

    Args:
        domain_ids: List of domain identifiers
        request_delay: Delay between InterPro API requests

    Returns:
        Dictionary mapping domain ID to name

    Example:
        >>> names = fetch_domain_names(["IPR005982", "3.50.50.60:FF:000064"])
        >>> len(names) == 2
        True
    """
    domain_names = {}

    for domain_id in domain_ids:
        if domain_id.startswith("IPR"):
            # InterPro ID - fetch from API
            domain_names[domain_id] = get_interpro_name(domain_id, request_delay)
        elif ":FF:" in domain_id:
            # FunFam ID - generate descriptive label
            domain_names[domain_id] = get_funfam_name(domain_id)
        else:
            # Unknown format
            domain_names[domain_id] = domain_id

    return domain_names


def extract_domain_labels_from_enriched_rule(
    rule_id: str,
    cache_dir: Path
) -> dict[str, str]:
    """Extract domain labels from enriched ARBA rule JSON.

    The enriched JSON contains labels for all InterPro and FunFam condition values.

    Args:
        rule_id: ARBA rule ID
        cache_dir: Cache directory containing enriched JSON

    Returns:
        Dictionary mapping domain ID to label

    Example:
        >>> labels = extract_domain_labels_from_enriched_rule("ARBA00026249", Path("rules/arba"))
        >>> "IPR005982" in labels
        True
    """
    import json

    enriched_path = cache_dir / rule_id / f"{rule_id}.enriched.json"

    if not enriched_path.exists():
        return {}

    try:
        with open(enriched_path) as f:
            enriched_data = json.load(f)

        domain_labels = {}

        # Extract labels from condition sets
        for condition_set in enriched_data.get("mainRule", {}).get("conditionSets", []):
            for condition in condition_set.get("conditions", []):
                # Check if this is a domain condition (InterPro or FunFam)
                cond_type = condition.get("type", "")
                if cond_type in ("InterPro id", "FunFam id"):
                    for cv in condition.get("conditionValues", []):
                        domain_id = cv.get("value")
                        label = cv.get("label")
                        if domain_id and label:
                            domain_labels[domain_id] = label

        return domain_labels

    except Exception:
        # If enriched file doesn't exist or is malformed, return empty dict
        return {}


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
    condition_set_membership = {}  # Maps (type, id) -> list of 1-based condition set indices

    for cs_idx, cs in enumerate(rule.condition_sets, start=1):
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

    # Add domain-GO pairs if the rule has GO annotations
    go_ids = rule.get_go_ids()
    if go_ids and all_domain_conditions:
        for go_id in go_ids:
            # Get GO term count
            count_go = get_swissprot_count_for_go(go_id, request_delay=request_delay)

            # Create pairs between each domain and the GO term
            for type_domain, id_domain in all_domain_conditions:
                # Get domain count (already fetched above but need to refetch for consistency)
                if type_domain == "interpro":
                    count_domain = get_swissprot_count_for_interpro(id_domain, request_delay=request_delay)
                else:  # funfam
                    count_domain = get_swissprot_count_for_funfam(id_domain, request_delay=request_delay)

                # Get intersection count (domain AND GO term)
                count_intersection = get_swissprot_count_for_mixed_conditions(
                    [(type_domain, id_domain), ("go", go_id)],
                    request_delay=request_delay
                )

                # Calculate metrics
                jaccard = count_intersection / (count_domain + count_go - count_intersection) if (count_domain + count_go - count_intersection) > 0 else 0.0
                containment_domain_in_go = count_intersection / count_domain if count_domain > 0 else 0.0
                containment_go_in_domain = count_intersection / count_go if count_go > 0 else 0.0

                # Calculate set differences
                domain_minus_go_count = count_domain - count_intersection
                go_minus_domain_count = count_go - count_intersection

                # Determine interpretation
                if count_intersection == 0:
                    interpretation = "DISJOINT"
                elif jaccard > 0.9:
                    interpretation = "REDUNDANT"
                elif containment_domain_in_go > 0.95 or containment_go_in_domain > 0.95:
                    interpretation = "SUBSET"
                elif jaccard > 0.5:
                    interpretation = "HIGH_OVERLAP"
                elif jaccard > 0.2:
                    interpretation = "MODERATE"
                else:
                    interpretation = "LOW"

                # Add pair (domain, GO term)
                pairs_analysis.append({
                    "condition_a": id_domain,
                    "condition_b": go_id,
                    "condition_a_in_sets": condition_set_membership[(type_domain, id_domain)],
                    "condition_b_in_sets": [],  # GO terms not in condition sets
                    "protein_database": "SWISSPROT",
                    "count_a": count_domain,
                    "count_b": count_go,
                    "intersection_count": count_intersection,
                    "a_minus_b_count": domain_minus_go_count,
                    "b_minus_a_count": go_minus_domain_count,
                    "jaccard_similarity": jaccard,
                    "containment_a_in_b": containment_domain_in_go,
                    "containment_b_in_a": containment_go_in_domain,
                    "interpretation": interpretation
                })

    # Generate summary
    num_domain_pairs = len([p for p in pairs_analysis if not p['condition_b'].startswith('GO:')])
    num_domain_go_pairs = len([p for p in pairs_analysis if p['condition_b'].startswith('GO:')])

    avg_jaccard = sum(p["jaccard_similarity"] for p in pairs_analysis) / len(pairs_analysis) if pairs_analysis else 0.0
    high_overlap_pairs = [p for p in pairs_analysis if p["jaccard_similarity"] > 0.5]
    subset_pairs = [p for p in pairs_analysis if p["interpretation"] == "SUBSET"]

    summary = f"Analyzed {num_domain_pairs} domain-domain pairs and {num_domain_go_pairs} domain-GO pairs across entire rule. "
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
    request_delay: float = 0.1,
    max_condition_sets: int = 12
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
        max_condition_sets: Maximum number of condition sets to analyze (default: 12)

    Returns:
        Complete analysis dict suitable for adding to enriched JSON

    Raises:
        ValueError: If rule has more than max_condition_sets condition sets

    Example:
        >>> from ai_gene_review.etl.arba import ARBAClient
        >>> from pathlib import Path
        >>> client = ARBAClient()
        >>> rule = client.fetch_rule("ARBA00026249")
        >>> analysis = analyze_rule_post_enrichment(rule, Path("rules/arba"))
        >>> "rule_id" in analysis and "ipr2go_redundancy" in analysis
        True
    """
    # Check condition set limit
    num_condition_sets = len(rule.condition_sets)
    if num_condition_sets > max_condition_sets:
        raise ValueError(
            f"Rule {rule.uni_rule_id} has {num_condition_sets} condition sets, "
            f"which exceeds the maximum of {max_condition_sets}. "
            f"Analysis is skipped for rules with too many condition sets "
            f"as they would require excessive UniProt API queries and take too long."
        )

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
    for cs_idx, cs in enumerate(rule.condition_sets, start=1):
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

    # Extract domain labels from enriched JSON if available
    domain_labels = extract_domain_labels_from_enriched_rule(rule.uni_rule_id, cache_dir)

    return {
        "rule_id": rule.uni_rule_id,
        "domain_overlap_analysis": all_pairs_analysis,
        "condition_sets_summary": condition_sets_summary,
        "ipr2go_redundancy": redundancy_analysis,
        "domain_labels": domain_labels
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
    figsize: tuple[float, float] = (18, 16),
    domain_labels: Optional[dict[str, str]] = None
) -> None:
    """Generate asymmetric heatmap showing domain containment relationships.

    Creates a heatmap where cell (i,j) shows the containment of domain i in domain j
    (i.e., what fraction of proteins with domain i also have domain j).
    Domains are grouped by condition set with separators.

    Args:
        analysis: Analysis dict from analyze_rule_post_enrichment
        output_path: Optional path to save figure (PNG format)
        figsize: Figure size in inches (width, height) - default (18, 16) for domain names
        domain_labels: Optional dict mapping domain IDs to human-readable labels.
            If None, domain names are automatically fetched from InterPro API

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
    # GO terms have empty sets, so they sort last (using infinity)
    domains = sorted(
        domain_to_sets.keys(),
        key=lambda d: (min(domain_to_sets[d]) if domain_to_sets[d] else float('inf'), d)
    )

    n_domains = len(domains)

    # Use domain labels from analysis if not explicitly provided
    if domain_labels is None:
        domain_labels = analysis.get("domain_labels", {})

    # Build a mapping of domain ID to protein count from the pairs data
    domain_counts = {}
    for pair in pairs:
        if pair["condition_a"] not in domain_counts:
            domain_counts[pair["condition_a"]] = pair["count_a"]
        if pair["condition_b"] not in domain_counts:
            domain_counts[pair["condition_b"]] = pair["count_b"]

    # Create display labels (ID + label + count on three lines)
    display_labels = []
    for domain in domains:
        if domain_labels and domain in domain_labels:
            # Show ID, label, and protein count
            count = domain_counts.get(domain, "?")
            label = f"{domain}\n{domain_labels[domain]}\n(n={count})"
        else:
            # Fallback to ID with count if no label available
            count = domain_counts.get(domain, "?")
            label = f"{domain}\n(n={count})"
        display_labels.append(label)

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

    # Calculate condition set boundaries first
    cs_boundaries = []
    prev_cs = None
    for i, domain in enumerate(domains):
        curr_cs = min(domain_to_sets[domain]) if domain_to_sets[domain] else float('inf')
        if prev_cs is not None and curr_cs != prev_cs:
            cs_boundaries.append(i)
        prev_cs = curr_cs

    # Calculate condition set labels and positions
    cs_labels = []
    cs_positions_y = []
    cs_positions_x = []
    prev_boundary = 0
    for boundary in cs_boundaries + [n_domains]:
        mid_idx = (prev_boundary + boundary) // 2
        domain_sets = domain_to_sets[domains[mid_idx]]
        if domain_sets:
            cs_num = min(domain_sets)
            cs_labels.append(f"CS{cs_num}")
        else:
            cs_labels.append("TGT")  # GO term target
        cs_positions_y.append((prev_boundary + boundary) / 2)
        cs_positions_x.append((prev_boundary + boundary) / 2)
        prev_boundary = boundary

    # Create heatmap WITHOUT colorbar
    sns.heatmap(
        containment_matrix,
        xticklabels=display_labels,
        yticklabels=display_labels,
        annot=True,
        fmt=".2f",
        cmap="YlOrRd",
        vmin=0,
        vmax=1,
        cbar=False,  # Remove colorbar
        square=True,  # Use square cells
        linewidths=0.5,
        linecolor='gray',
        ax=ax,
        annot_kws={'fontsize': 8}
    )

    # Draw separator lines between condition sets
    for boundary in cs_boundaries:
        ax.axhline(y=boundary, color='black', linewidth=2.5)
        ax.axvline(x=boundary, color='black', linewidth=2.5)

    # Add text annotations for condition sets on right and top
    # Right side (Y-axis)
    for i, (label, pos) in enumerate(zip(cs_labels, cs_positions_y)):
        ax.text(n_domains + 0.3, pos, label,
                ha='left', va='center', fontsize=10, fontweight='bold')

    # Top (X-axis)
    for i, (label, pos) in enumerate(zip(cs_labels, cs_positions_x)):
        ax.text(pos, -0.3, label,
                ha='center', va='bottom', fontsize=10, fontweight='bold')

    # Rotate x-axis labels and adjust alignment
    plt.setp(ax.xaxis.get_majorticklabels(), rotation=45, ha='right', fontsize=7)
    plt.setp(ax.yaxis.get_majorticklabels(), fontsize=7)

    # Set titles and labels
    ax.set_xlabel("Domain (Column)", fontsize=11)
    ax.set_ylabel("Domain (Row)", fontsize=11)
    ax.set_title(
        f"Domain Containment Matrix: {analysis['rule_id']}\n"
        f"Cell (i,j) = fraction of proteins with domain i that also have domain j",
        pad=30,
        fontsize=13
    )

    # Use subplots_adjust to allocate more space for domain name labels
    plt.subplots_adjust(left=0.20, right=0.90, top=0.93, bottom=0.22)

    if output_path:
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        print(f"Heatmap saved to {output_path}")
    else:
        plt.show()

    plt.close()


def build_heatmap_table_data(
    analysis: dict,
    rule_data: dict,
    enriched_rule: Optional[dict] = None,
    cache_dir: Optional[Path] = None
) -> Optional[dict]:
    """Build data structure for rendering heatmap as HTML table.

    Args:
        analysis: Analysis dict from analyze_rule_post_enrichment
        rule_data: Rule review YAML data
        enriched_rule: Enriched rule data with labels and taxon info

    Returns:
        Dict with domains, matrix data, and metadata, or None if no analysis available
    """
    if not analysis or 'domain_overlap_analysis' not in analysis:
        return None

    pairs = analysis['domain_overlap_analysis']['pairs']
    if not pairs:
        return None

    # Build domain metadata map and condition set taxon info from enriched rule if available
    domain_metadata = {}
    cs_taxon_labels = {}  # Map from CS index to taxon label
    if enriched_rule:
        # Extract condition sets from enriched rule (may be at top level or in mainRule)
        cond_sets = enriched_rule.get('conditionSets') or enriched_rule.get('mainRule', {}).get('conditionSets', [])
        for cs_idx, cond_set in enumerate(cond_sets):
            cs_taxon_label = None
            for condition in cond_set.get('conditions', []):
                cond_type = condition.get('type', '')
                for cond_val in condition.get('conditionValues', []):
                    # Extract taxon label from taxon conditions
                    if cond_type == 'taxon':
                        cs_taxon_label = cond_val.get('label')
                    # Extract domain labels and types for all non-taxon conditions
                    # This includes InterPro id, FunFam id, PANTHER id, and any future types
                    domain_id = cond_val.get('value')
                    if domain_id and cond_type != 'taxon':
                        domain_metadata[domain_id] = {
                            'label': cond_val.get('label'),
                            'type': cond_val.get('type'),  # InterPro type from enriched data
                            'condition_type': cond_type  # Store the condition type (e.g., 'PANTHER id', 'InterPro id')
                        }
            # Store taxon label for this CS
            if cs_taxon_label:
                cs_taxon_labels[cs_idx] = cs_taxon_label

    # Collect all unique domains and their metadata
    domains = {}
    for pair in pairs:
        for domain_id, sets_key in [(pair['condition_a'], 'condition_a_in_sets'),
                                     (pair['condition_b'], 'condition_b_in_sets')]:
            if domain_id not in domains:
                metadata = domain_metadata.get(domain_id, {})
                domains[domain_id] = {
                    'id': domain_id,
                    'label': metadata.get('label'),
                    'type': metadata.get('type'),  # InterPro type (family, domain, active_site, etc.)
                    'condition_sets': pair[sets_key],
                    'count': pair['count_a'] if domain_id == pair['condition_a'] else pair['count_b']
                }

    # Also add any domains from domain_metadata that aren't in pairs (e.g., PANTHER signatures)
    # These domains won't have protein counts but should still appear in the table
    if enriched_rule:
        cond_sets = enriched_rule.get('conditionSets') or enriched_rule.get('mainRule', {}).get('conditionSets', [])
        for cs_idx, cond_set in enumerate(cond_sets):
            for condition in cond_set.get('conditions', []):
                for cond_val in condition.get('conditionValues', []):
                    domain_id = cond_val.get('value')
                    if domain_id and domain_id not in domains and domain_id in domain_metadata:
                        domains[domain_id] = {
                            'id': domain_id,
                            'label': domain_metadata[domain_id].get('label'),
                            'type': domain_metadata[domain_id].get('type'),
                            'condition_sets': [cs_idx],  # This domain appears in this CS
                            'count': None  # No protein count available
                        }

    # Order domains by condition set, then alphabetically
    # GO terms have empty condition_sets, so they sort last (using infinity)
    domain_list = sorted(domains.values(), key=lambda d: (min(d['condition_sets']) if d['condition_sets'] else float('inf'), d['id']))
    domain_ids = [d['id'] for d in domain_list]

    # Extract GO term target from enriched rule if available
    go_term = None
    if enriched_rule:
        main_rule = enriched_rule.get('mainRule', enriched_rule)
        annots = main_rule.get('annotations', [])
        if annots:
            db_ref = annots[0].get('dbReference', {})
            if db_ref.get('database') == 'GO':
                go_id = db_ref.get('id')
                # Get protein count for GO term from pairs if available
                go_count = None
                for pair in pairs:
                    if pair['condition_b'] == go_id:
                        go_count = pair['count_b']
                        break
                go_term = {
                    'id': go_id,
                    'label': db_ref.get('label'),
                    'type': 'GO_TERM',
                    'condition_sets': [],  # GO terms don't appear in condition sets
                    'count': go_count  # Get from pairs analysis
                }

    # Append GO term to domain list if found and not already there (will appear as TGT column)
    # The GO term may already be in the list from the pairs loop
    if go_term and go_term['id'] not in domain_ids:
        domain_list.append(go_term)
        domain_ids.append(go_term['id'])

    # Build condition set groups for two-level headers and track CS boundary columns
    # Use 1-based indexing for CS labels (biologist-friendly)
    # Exclude GO term from this loop (it has no condition sets and will be added separately)
    cs_groups = []
    cs_boundary_cols = set()  # Columns that start a new CS
    current_cs = None
    current_group = {'cs_label': None, 'domains': [], 'taxon_label': None}

    # Only process domains (not GO term) for CS grouping
    num_domains = len(domain_list) - (1 if go_term else 0)
    for idx in range(num_domains):
        domain = domain_list[idx]
        # Skip if this domain has no condition sets (e.g., GO terms that got added from pairs)
        if not domain['condition_sets']:
            continue
        cs = min(domain['condition_sets'])
        if cs != current_cs:
            if current_group['domains']:
                cs_groups.append(current_group)
            cs_boundary_cols.add(idx)  # Mark this column as a CS boundary
            current_cs = cs
            current_group = {
                'cs_label': f'CS {cs + 1}',  # 1-based indexing
                'domains': [domain],
                'taxon_label': cs_taxon_labels.get(cs)  # Get taxon label for this CS
            }
        else:
            current_group['domains'].append(domain)

    if current_group['domains']:
        cs_groups.append(current_group)

    # Add GO term as a separate "TGT" (target) group
    if go_term:
        cs_groups.append({
            'cs_label': 'TGT',
            'domains': [go_term],
            'taxon_label': None
        })
        # Mark GO term column as a boundary
        cs_boundary_cols.add(len(domain_list) - 1)

    # Build matrix: matrix[i][j] = containment of domain i in domain j (i PREDICTS j)
    n = len(domain_ids)
    matrix = [[None for _ in range(n)] for _ in range(n)]

    # Fill matrix from pairs
    for pair in pairs:
        i = domain_ids.index(pair['condition_a'])
        j = domain_ids.index(pair['condition_b'])

        # Cell (i, j): how much of domain i is in domain j (A in B)
        matrix[i][j] = {
            'containment': pair['containment_a_in_b'],
            'jaccard': pair['jaccard_similarity'],
            'intersection': pair['intersection_count'],
            'interpretation': pair['interpretation']
        }

        # Cell (j, i): how much of domain j is in domain i (B in A)
        if i != j:
            matrix[j][i] = {
                'containment': pair['containment_b_in_a'],
                'jaccard': pair['jaccard_similarity'],
                'intersection': pair['intersection_count'],
                'interpretation': pair['interpretation']
            }

    return {
        'domains': domain_list,
        'matrix': matrix,
        'cs_groups': cs_groups,
        'cs_boundary_cols': list(cs_boundary_cols)
    }


def render_rule_review_html(
    rule_id: str,
    cache_dir: Path,
    output_path: Optional[Path] = None,
    template_path: Optional[Path] = None
) -> Path:
    """Render a rule review YAML file to HTML with embedded heatmap and analysis.

    Args:
        rule_id: The rule ID (e.g., ARBA00026249)
        cache_dir: Directory containing rule files
        output_path: Optional output path for HTML file
        template_path: Optional path to custom Jinja2 template

    Returns:
        Path to the generated HTML file

    Example:
        >>> from pathlib import Path
        >>> rule_id = "ARBA00026249"
        >>> cache_dir = Path("rules/arba")
        >>> # html_path = render_rule_review_html(rule_id, cache_dir)  # doctest: +SKIP
    """
    from jinja2 import Environment, FileSystemLoader, select_autoescape

    # Locate the review YAML file
    rule_dir = cache_dir / rule_id
    review_yaml_path = rule_dir / f"{rule_id}-review.yaml"

    if not review_yaml_path.exists():
        raise FileNotFoundError(f"Rule review YAML not found: {review_yaml_path}")

    # Load review YAML
    with open(review_yaml_path, 'r') as f:
        rule_data = yaml.safe_load(f)

    # Read raw YAML content for preview
    with open(review_yaml_path, 'r') as f:
        yaml_content = f.read()

    # Load analysis JSON if available (for heatmap table)
    analysis_json_path = rule_dir / f"{rule_id}-analysis.json"
    analysis = None
    if analysis_json_path.exists():
        with open(analysis_json_path, 'r') as f:
            analysis = json.load(f)

    # Load enriched rule if available (for domain labels and taxon constraints)
    enriched_rule_path = rule_dir / f"{rule_id}.enriched.json"
    enriched_rule = None
    if enriched_rule_path.exists():
        with open(enriched_rule_path, 'r') as f:
            enriched_rule = json.load(f)

    # Generate stats from the rule data
    stats = {}
    if 'rule' in rule_data and 'condition_sets' in rule_data['rule']:
        condition_sets = rule_data['rule']['condition_sets']
        stats['condition_sets'] = len(condition_sets)

        # Count total pairwise overlaps from all condition sets
        total_pairs = 0
        subset_count = 0
        for cs in condition_sets:
            if 'pairwise_overlap' in cs and cs['pairwise_overlap']:
                total_pairs += len(cs['pairwise_overlap'])
                for pair in cs['pairwise_overlap']:
                    if pair.get('interpretation') == 'SUBSET':
                        subset_count += 1

        stats['total_pairs'] = total_pairs
        stats['subset_relationships'] = subset_count

    # Get redundant annotation count
    if 'rule' in rule_data and 'ipr2go_redundancy' in rule_data['rule']:
        redundancy_info = rule_data['rule']['ipr2go_redundancy']
        stats['redundant_annotations'] = len(redundancy_info.get('redundant_annotations', []))
    else:
        stats['redundant_annotations'] = 0

    rule_data['stats'] = stats

    # Check for heatmap image and embed as base64
    import base64
    heatmap_path = rule_dir / f"{rule_id}-heatmap.png"
    if heatmap_path.exists():
        # Read PNG and convert to base64 data URI
        with open(heatmap_path, 'rb') as f:
            heatmap_data = base64.b64encode(f.read()).decode('utf-8')
        rule_data['heatmap_data'] = f"data:image/png;base64,{heatmap_data}"
    else:
        rule_data['heatmap_data'] = None

    # Set default template if not provided
    if template_path is None:
        module_dir = Path(__file__).parent.parent  # Go up to src/ai_gene_review
        template_path = module_dir / "templates" / "rule_review.html.j2"
        if not template_path.exists():
            raise FileNotFoundError(f"Default template not found at {template_path}")

    # Build heatmap table data if analysis is available
    heatmap_table = build_heatmap_table_data(analysis, rule_data, enriched_rule, cache_dir) if analysis else None

    # Set default output path if not provided
    if output_path is None:
        output_path = rule_dir / f"{rule_id}-review.html"

    # Set up Jinja2 environment
    template_dir = template_path.parent
    env = Environment(
        loader=FileSystemLoader(template_dir),
        autoescape=select_autoescape(['html', 'j2'])
    )

    # Load and render template
    template = env.get_template(template_path.name)
    html = template.render(
        rule=rule_data,
        yaml_content=yaml_content,
        stats=stats,
        heatmap_data=rule_data.get('heatmap_data'),
        heatmap_table=heatmap_table,
        analysis=analysis
    )

    # Write output
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"HTML review rendered to {output_path}")
    return output_path
