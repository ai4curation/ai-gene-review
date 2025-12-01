"""Sync rule review YAML files with analysis data.

This module provides functions to update rule review YAML files with:
- Pairwise overlap data for each condition set
- Global pairwise overlap data across all condition sets
"""

import json
from pathlib import Path
from typing import Optional

import yaml


def sync_review_with_analysis(
    review_yaml_path: Path,
    analysis_json_path: Optional[Path] = None,
    containment_threshold: float = 0.8,
    dry_run: bool = False
) -> dict:
    """Sync a rule review YAML file with its analysis JSON data.

    Updates the review YAML with:
    1. pairwise_overlap sections for each condition set (from analysis data)
    2. global_pairwise_overlap section at rule level (filtered by containment threshold)

    Args:
        review_yaml_path: Path to the rule review YAML file
        analysis_json_path: Optional path to analysis JSON (defaults to sibling file)
        containment_threshold: Minimum containment_a_in_b to include in global_pairwise_overlap
        dry_run: If True, return changes without writing to file

    Returns:
        Dict with update statistics

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
        'global_pairs_added': 0,
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

    # Create global_pairwise_overlap (filtered by containment threshold)
    # Since containment is asymmetric, test both directions (A→B and B→A)
    # Only include one direction if both pass the threshold
    global_pairs = []
    seen_pairs = set()  # Track (cond_a, cond_b) tuples to avoid duplicates

    for pair in all_pairs:
        cond_a = pair['condition_a']
        cond_b = pair['condition_b']

        # Test both directions
        a_in_b = pair.get('containment_a_in_b', 0)
        b_in_a = pair.get('containment_b_in_a', 0)

        # Include if either direction passes threshold
        if a_in_b >= containment_threshold or b_in_a >= containment_threshold:
            # Create canonical key to avoid duplicates (same pair in both directions)
            pair_key = tuple(sorted([cond_a, cond_b]))

            if pair_key not in seen_pairs:
                seen_pairs.add(pair_key)
                global_pairs.append({
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
                    'interpretation': pair['interpretation'],
                    'condition_a_in_sets': pair.get('condition_a_in_sets', []),
                    'condition_b_in_sets': pair.get('condition_b_in_sets', [])
                })

    stats['global_pairs_added'] = len(global_pairs)

    if global_pairs:
        if 'rule' not in review_data:
            review_data['rule'] = {}
        review_data['rule']['global_pairwise_overlap'] = global_pairs

        # Add thresholds metadata
        review_data['rule']['global_pairwise_overlap_thresholds'] = {
            'containment_a_in_b_threshold': containment_threshold
        }

    # Write updated YAML
    if not dry_run:
        with open(review_yaml_path, 'w') as f:
            yaml.dump(review_data, f, default_flow_style=False, sort_keys=False, allow_unicode=True)

    return stats


def sync_all_reviews(
    cache_dir: Path,
    rule_type: str = "all",
    containment_threshold: float = 0.8,
    dry_run: bool = False
) -> dict:
    """Sync all rule review YAML files in a directory.

    Args:
        cache_dir: Base cache directory (e.g., Path("rules"))
        rule_type: "arba", "unirule", or "all"
        containment_threshold: Minimum containment_a_in_b for global_pairwise_overlap
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
        'total_global_pairs_added': 0
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
                containment_threshold=containment_threshold,
                dry_run=dry_run
            )

            overall_stats['reviews_processed'] += 1

            if stats['status'] == 'updated':
                overall_stats['reviews_updated'] += 1
                overall_stats['total_condition_sets_updated'] += stats['condition_sets_updated']
                overall_stats['total_global_pairs_added'] += stats['global_pairs_added']
            elif stats['status'] == 'skipped':
                overall_stats['reviews_skipped'] += 1

    return overall_stats
