#!/usr/bin/env python3
"""Export ARBA rule reviews to JSON format for browser display."""

import yaml
import json
from pathlib import Path
from datetime import datetime
import sys


def export_rules_json(cache_dir: str = "rules/arba"):
    """Export rule reviews to JSON including both reviewed and enriched data."""
    cache_path = Path(cache_dir)
    review_files = sorted(cache_path.glob("*/*-review.yaml"))
    enriched_files = sorted(cache_path.glob("*/*.enriched.json"))

    # Create a map of rule IDs to enriched data
    enriched_data_map = {}
    for enriched_file in enriched_files:
        try:
            with open(enriched_file) as f:
                enriched = json.load(f)
                rule_id = enriched.get('rule', {}).get('ruleId', enriched_file.parent.name)
                enriched_data_map[rule_id] = enriched
        except Exception as e:
            print(f"Warning: Failed to load enriched data {enriched_file}: {e}")

    # Collect all rules (both reviewed and not)
    rules_data = []

    # Process reviewed files
    for review_file in review_files:
        try:
            with open(review_file) as f:
                data = yaml.safe_load(f)

            rule_id = data.get('id', review_file.parent.name)
            rule_obj = data.get('rule', {})

            # Get GO terms
            go_terms = []
            for go_ann in rule_obj.get('go_annotations', []):
                go_terms.append({
                    'id': go_ann.get('go_id', ''),
                    'label': go_ann.get('go_label', '')
                })

            parsimony = data.get('parsimony', {})
            literature = data.get('literature_support', {})

            # Get protein counts from enriched data if available
            enriched = enriched_data_map.get(rule_id, {})
            stats = enriched.get('statistics', {})
            reviewed_count = stats.get('reviewedProteinCount', 0)
            unreviewed_count = stats.get('unreviewedProteinCount', 0)
            total_entries = reviewed_count + unreviewed_count

            rule_info = {
                'id': rule_id,
                'rule_id': rule_id,
                'description': data.get('description', ''),
                'action': data.get('action', None),
                'status': data.get('status', 'REVIEWED'),
                'confidence': data.get('confidence', None),
                'num_condition_sets': len(rule_obj.get('condition_sets', [])),
                'num_entries': total_entries,
                'go_terms': go_terms,
                'go_term_ids': [t['id'] for t in go_terms],
                'go_term_labels': [t['label'] for t in go_terms],
                'parsimony_assessment': parsimony.get('assessment', None),
                'literature_support': literature.get('assessment', None),
                'review_link': f"../{rule_id}/{rule_id}-review.html",
                'is_reviewed': True
            }

            rules_data.append(rule_info)
        except Exception as e:
            print(f"Warning: Failed to process {review_file}: {e}")

    # Process enriched files that don't have reviews yet
    for rule_id, enriched in enriched_data_map.items():
        # Skip if already reviewed
        if any(r['rule_id'] == rule_id for r in rules_data):
            continue

        rule_obj = enriched.get('rule', {})

        # Get GO terms
        go_terms = []
        for go_ann in rule_obj.get('goAnnotations', []):
            go_terms.append({
                'id': go_ann.get('goId', ''),
                'label': go_ann.get('goName', '')
            })

        # Get protein counts
        stats = enriched.get('statistics', {})
        reviewed_count = stats.get('reviewedProteinCount', 0)
        unreviewed_count = stats.get('unreviewedProteinCount', 0)
        total_entries = reviewed_count + unreviewed_count

        rule_info = {
            'id': rule_id,
            'rule_id': rule_id,
            'description': rule_obj.get('label', ''),
            'action': None,
            'status': 'NOT_REVIEWED',
            'confidence': None,
            'num_condition_sets': len(rule_obj.get('conditionSets', [])),
            'num_entries': total_entries,
            'go_terms': go_terms,
            'go_term_ids': [t['id'] for t in go_terms],
            'go_term_labels': [t['label'] for t in go_terms],
            'parsimony_assessment': None,
            'literature_support': None,
            'review_link': None,
            'is_reviewed': False
        }

        rules_data.append(rule_info)

    # Write to JSON file
    output_file = cache_path / "rules_data.json"
    with open(output_file, 'w') as f:
        json.dump(rules_data, f, indent=2)

    print(f"✓ Exported {len(rules_data)} rules to {output_file}")
    return output_file


if __name__ == "__main__":
    cache_dir = sys.argv[1] if len(sys.argv) > 1 else "rules/arba"
    export_rules_json(cache_dir)
