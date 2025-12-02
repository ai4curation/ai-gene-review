"""Sync rule review YAML files with analysis data.

This module provides functions to update rule review YAML files with:
- Pairwise overlap data for each condition set
- Global pairwise overlap data across all condition sets
- Entry-centric view of all entities (domains and GO terms) with relationships
"""

import json
from pathlib import Path
from typing import Optional, Dict, List, Tuple

import yaml


def categorize_relationship(
    jaccard: float,
    containment_a_in_b: float,
    containment_b_in_a: float,
    jaccard_boost: float = 0.05
) -> str:
    """Categorize pairwise relationship based on similarity metrics.

    Compares jaccard_boosted, containment_a_in_b, and containment_b_in_a
    to determine the best relationship category.

    Args:
        jaccard: Jaccard similarity coefficient (0-1)
        containment_a_in_b: Fraction of A contained in B (0-1)
        containment_b_in_a: Fraction of B contained in A (0-1)
        jaccard_boost: Boost to add to jaccard for EQUIV preference (default 0.05)

    Returns:
        One of: 'PREDICTS', 'PREDICTED_BY', 'EQUIV'

    Examples:
        >>> categorize_relationship(0.9, 0.95, 0.94)  # High jaccard wins
        'EQUIV'
        >>> categorize_relationship(0.5, 1.0, 0.5)  # A⊆B wins
        'PREDICTS'
        >>> categorize_relationship(0.5, 0.5, 1.0)  # B⊆A wins
        'PREDICTED_BY'
    """
    jaccard_boosted = min(1.0, jaccard + jaccard_boost)

    scores = {
        'EQUIV': jaccard_boosted,
        'PREDICTS': containment_a_in_b,
        'PREDICTED_BY': containment_b_in_a
    }

    return max(scores, key=scores.get)


def infer_entry_type(entry_id: str) -> str:
    """Infer entry type from ID pattern.

    Args:
        entry_id: Entry identifier (e.g., 'IPR005982', '3.50.50.60:FF:000064', 'GO:0004791')

    Returns:
        One of: 'INTERPRO', 'FUNFAM', 'PANTHER', 'GO_TERM'

    Examples:
        >>> infer_entry_type('IPR005982')
        'INTERPRO'
        >>> infer_entry_type('3.50.50.60:FF:000064')
        'FUNFAM'
        >>> infer_entry_type('PTHR10000')
        'PANTHER'
        >>> infer_entry_type('GO:0004791')
        'GO_TERM'
    """
    if entry_id.startswith('GO:'):
        return 'GO_TERM'
    elif entry_id.startswith('IPR'):
        return 'INTERPRO'
    elif entry_id.startswith('PTHR'):
        return 'PANTHER'
    elif ':FF:' in entry_id:  # CATH FunFam pattern
        return 'FUNFAM'
    else:
        # Default to INTERPRO for unknown patterns
        return 'INTERPRO'


def generate_entries(
    analysis_data: dict,
    review_data: dict,
    jaccard_boost: float = 0.05
) -> List[dict]:
    """Generate entry-centric view from pairwise overlap data.

    Creates one entry per domain/family condition AND per GO term target.
    Each entry has nested relationships categorized as PREDICTS, PREDICTED_BY, or EQUIV.

    Args:
        analysis_data: Analysis JSON with domain_overlap_analysis.pairs
        review_data: Review YAML with rule.condition_sets and rule.annotations
        jaccard_boost: Boost for jaccard in relationship categorization (default 0.05)

    Returns:
        List of entry dicts with id, label, type, appears_in_condition_sets,
        protein_count, and related_entries
    """
    # Collect all unique entities (domains/families + GO terms)
    entities = {}  # id -> {label, type, appears_in_sets, protein_count}
    relationships = {}  # id -> list of (target_id, relationship, metrics)

    # Extract domain conditions from condition sets
    # Only include INTERPRO, FUNFAM, PANTHER (not TAXON, PROTEIN, etc.)
    condition_sets = review_data.get('rule', {}).get('condition_sets', [])
    for cs_idx, cs in enumerate(condition_sets, start=1):
        for condition in cs.get('conditions', []):
            # Skip non-domain/family conditions
            condition_type = condition.get('condition_type', '')
            if condition_type not in ('INTERPRO', 'FUNFAM', 'PANTHER'):
                continue

            # Try both 'condition' and 'value' keys
            cond_id = condition.get('condition') or condition.get('value')
            if cond_id and cond_id not in entities:
                entities[cond_id] = {
                    'id': cond_id,
                    'label': condition.get('label', ''),
                    'type': infer_entry_type(cond_id),
                    'appears_in_condition_sets': [],
                    'protein_count': None
                }
            if cond_id:
                if cs_idx not in entities[cond_id]['appears_in_condition_sets']:
                    entities[cond_id]['appears_in_condition_sets'].append(cs_idx)

    # Extract GO term targets from annotations
    annotations = review_data.get('rule', {}).get('annotations', [])
    for annot in annotations:
        go_id = annot.get('go_id')
        if go_id and go_id not in entities:
            entities[go_id] = {
                'id': go_id,
                'label': annot.get('go_label', ''),
                'type': 'GO_TERM',
                'appears_in_condition_sets': [],  # GO terms don't appear in condition sets
                'protein_count': None
            }

    # Process pairwise overlaps to build relationships
    all_pairs = analysis_data.get('domain_overlap_analysis', {}).get('pairs', [])

    for pair in all_pairs:
        cond_a = pair['condition_a']
        cond_b = pair['condition_b']
        jaccard = pair.get('jaccard_similarity', 0)
        containment_a_in_b = pair.get('containment_a_in_b', 0)
        containment_b_in_a = pair.get('containment_b_in_a', 0)

        # Update protein counts from pair data
        if cond_a in entities:
            entities[cond_a]['protein_count'] = pair.get('count_a')
        if cond_b in entities:
            entities[cond_b]['protein_count'] = pair.get('count_b')

        # Categorize relationship from A's perspective
        rel_type = categorize_relationship(jaccard, containment_a_in_b, containment_b_in_a, jaccard_boost)

        # Determine containment score and exclusive count based on relationship type
        if rel_type == 'PREDICTS':
            containment = containment_a_in_b
            exclusive_count = pair.get('a_minus_b_count', 0)
        elif rel_type == 'PREDICTED_BY':
            containment = containment_b_in_a
            exclusive_count = pair.get('b_minus_a_count', 0)
        else:  # EQUIV
            containment = max(containment_a_in_b, containment_b_in_a)
            exclusive_count = pair.get('a_minus_b_count', 0)

        # Add relationship from A to B
        if cond_a not in relationships:
            relationships[cond_a] = []
        relationships[cond_a].append({
            'relationship': rel_type,
            'target_id': cond_b,
            'containment': round(containment, 3),
            'jaccard_similarity': round(jaccard, 3),
            'intersection_count': pair.get('intersection_count'),
            'exclusive_count': exclusive_count
        })

        # Add reciprocal relationship from B to A
        # Flip relationship type for reciprocal
        if rel_type == 'PREDICTS':
            reciprocal_rel = 'PREDICTED_BY'
            reciprocal_containment = containment_b_in_a
            reciprocal_exclusive = pair.get('b_minus_a_count', 0)
        elif rel_type == 'PREDICTED_BY':
            reciprocal_rel = 'PREDICTS'
            reciprocal_containment = containment_a_in_b
            reciprocal_exclusive = pair.get('a_minus_b_count', 0)
        else:  # EQUIV
            reciprocal_rel = 'EQUIV'
            reciprocal_containment = containment
            reciprocal_exclusive = pair.get('b_minus_a_count', 0)

        if cond_b not in relationships:
            relationships[cond_b] = []
        relationships[cond_b].append({
            'relationship': reciprocal_rel,
            'target_id': cond_a,
            'containment': round(reciprocal_containment, 3),
            'jaccard_similarity': round(jaccard, 3),
            'intersection_count': pair.get('intersection_count'),
            'exclusive_count': reciprocal_exclusive
        })

    # Build final entry list
    entries = []
    for entity_id, entity_data in sorted(entities.items()):
        entry = {
            'id': entity_id,
            'type': entity_data['type']
        }

        if entity_data['label']:
            entry['label'] = entity_data['label']

        if entity_data['appears_in_condition_sets']:
            entry['appears_in_condition_sets'] = sorted(entity_data['appears_in_condition_sets'])

        if entity_data['protein_count'] is not None:
            entry['protein_count'] = entity_data['protein_count']

        if entity_id in relationships and relationships[entity_id]:
            entry['related_entries'] = relationships[entity_id]

        entries.append(entry)

    return entries


def sync_review_with_analysis(
    review_yaml_path: Path,
    analysis_json_path: Optional[Path] = None,
    dry_run: bool = False
) -> dict:
    """Sync a rule review YAML file with its analysis JSON data.

    Updates the review YAML with:
    1. pairwise_overlap sections for each condition set (from analysis data)
    2. entries section with entry-centric view of all entities and their relationships

    Also removes deprecated global_pairwise_overlap fields if present.

    Args:
        review_yaml_path: Path to the rule review YAML file
        analysis_json_path: Optional path to analysis JSON (defaults to sibling file)
        dry_run: If True, return changes without writing to file

    Returns:
        Dict with update statistics including entries_generated count

    Example:
        >>> # sync_review_with_analysis(Path("rules/arba/ARBA00026249/ARBA00026249-review.yaml"))
    """
    # Load review YAML
    with open(review_yaml_path, 'r') as f:
        review_data = yaml.safe_load(f)

    # Determine analysis JSON path
    if analysis_json_path is None:
        rule_id = review_data.get('id')
        analysis_json_path = review_yaml_path.parent / f"{rule_id}-analysis.json"

    if not analysis_json_path.exists():
        return {
            'status': 'skipped',
            'reason': f'Analysis file not found: {analysis_json_path}'
        }

    # Load analysis JSON
    with open(analysis_json_path, 'r') as f:
        analysis_data = json.load(f)

    # Track changes
    stats = {
        'status': 'updated',
        'condition_sets_updated': 0,
        'total_pairs_in_analysis': 0
    }

    # Get all pairwise overlap data from analysis
    all_pairs = analysis_data.get('domain_overlap_analysis', {}).get('pairs', [])
    stats['total_pairs_in_analysis'] = len(all_pairs)

    # Organize pairs by condition set membership
    pairs_by_cs = {}  # cs_index -> list of pairs

    for pair in all_pairs:
        # Get which condition sets each condition appears in
        cs_a = set(pair.get('condition_a_in_sets', []))
        cs_b = set(pair.get('condition_b_in_sets', []))

        # Find condition sets where both conditions appear together
        common_sets = cs_a & cs_b

        for cs_idx in common_sets:
            if cs_idx not in pairs_by_cs:
                pairs_by_cs[cs_idx] = []
            pairs_by_cs[cs_idx].append(pair)

    # Update each condition set with its pairwise_overlap
    condition_sets = review_data.get('rule', {}).get('condition_sets', [])

    for cs_idx, cs in enumerate(condition_sets, start=1):
        # Set the condition set number at the beginning by reconstructing the dict
        # to preserve key order (number should appear first)
        new_cs = {'number': cs_idx}
        new_cs.update(cs)

        # Replace the old dict with the new one that has number first
        for key in list(cs.keys()):
            del cs[key]
        cs.update(new_cs)

        if cs_idx in pairs_by_cs:
            # Format pairs for YAML
            pairwise_overlap = []
            for pair in pairs_by_cs[cs_idx]:
                pairwise_overlap.append({
                    'condition_a': pair['condition_a'],
                    'condition_b': pair['condition_b'],
                    'protein_database': pair['protein_database'],
                    'count_a': pair['count_a'],
                    'count_b': pair['count_b'],
                    'intersection_count': pair['intersection_count'],
                    'a_minus_b_count': pair['a_minus_b_count'],
                    'b_minus_a_count': pair['b_minus_a_count'],
                    'jaccard_similarity': pair['jaccard_similarity'],
                    'containment_a_in_b': pair['containment_a_in_b'],
                    'containment_b_in_a': pair['containment_b_in_a'],
                    'interpretation': pair['interpretation']
                })

            cs['pairwise_overlap'] = pairwise_overlap
            stats['condition_sets_updated'] += 1

    # Remove deprecated global_pairwise_overlap fields if present
    if 'rule' in review_data:
        if 'global_pairwise_overlap' in review_data['rule']:
            del review_data['rule']['global_pairwise_overlap']
        if 'global_pairwise_overlap_thresholds' in review_data['rule']:
            del review_data['rule']['global_pairwise_overlap_thresholds']

    # Generate entry-centric view (replaces deprecated global_pairwise_overlap)
    entries = generate_entries(analysis_data, review_data, jaccard_boost=0.05)
    stats['entries_generated'] = len(entries)

    if entries:
        if 'rule' not in review_data:
            review_data['rule'] = {}
        review_data['rule']['entries'] = entries

    # Write updated YAML
    if not dry_run:
        with open(review_yaml_path, 'w') as f:
            yaml.dump(review_data, f, default_flow_style=False, sort_keys=False, allow_unicode=True)

    return stats


def sync_all_reviews(
    cache_dir: Path,
    rule_type: str = "all",
    dry_run: bool = False
) -> dict:
    """Sync all rule review YAML files in a directory.

    Args:
        cache_dir: Base cache directory (e.g., Path("rules"))
        rule_type: "arba", "unirule", or "all"
        dry_run: If True, report changes without writing files

    Returns:
        Dict with overall statistics

    Example:
        >>> # sync_all_reviews(Path("rules"), rule_type="arba")
    """
    overall_stats = {
        'reviews_processed': 0,
        'reviews_updated': 0,
        'reviews_skipped': 0,
        'total_condition_sets_updated': 0,
        'total_entries_generated': 0
    }

    # Determine which directories to scan
    dirs_to_scan = []
    if rule_type in ("arba", "all"):
        arba_dir = cache_dir / "arba"
        if arba_dir.exists():
            dirs_to_scan.append(arba_dir)

    if rule_type in ("unirule", "all"):
        unirule_dir = cache_dir / "unirule"
        if unirule_dir.exists():
            dirs_to_scan.append(unirule_dir)

    for rule_dir in dirs_to_scan:
        # Find all review YAML files
        for review_yaml in sorted(rule_dir.glob("*/*-review.yaml")):
            stats = sync_review_with_analysis(
                review_yaml,
                dry_run=dry_run
            )

            overall_stats['reviews_processed'] += 1

            if stats['status'] == 'updated':
                overall_stats['reviews_updated'] += 1
                overall_stats['total_condition_sets_updated'] += stats['condition_sets_updated']
                overall_stats['total_entries_generated'] += stats.get('entries_generated', 0)
            elif stats['status'] == 'skipped':
                overall_stats['reviews_skipped'] += 1

    return overall_stats
