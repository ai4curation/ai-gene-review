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

            # Extract condition values for faceting from enriched data
            interpro_ids = []
            funfam_ids = []
            condition_types = []

            if enriched:
                main_rule = enriched.get('mainRule', {})
                for cond_set in main_rule.get('conditionSets', []):
                    for cond in cond_set.get('conditions', []):
                        cond_type = cond.get('type', '')
                        if cond_type:
                            condition_types.append(cond_type)

                        for val in cond.get('conditionValues', []):
                            if cond_type == 'InterPro id':
                                ipr_id = val.get('value', '')
                                ipr_label = val.get('label', '')
                                if ipr_id:
                                    interpro_ids.append(f"{ipr_id} ({ipr_label})" if ipr_label else ipr_id)
                            elif cond_type == 'FunFam id':
                                funfam_id = val.get('value', '')
                                funfam_label = val.get('label', '')
                                if funfam_id:
                                    funfam_ids.append(f"{funfam_id} ({funfam_label})" if funfam_label else funfam_id)

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
                'go_term_ids': [f"{t['id']} ({t['label']})" if t.get('label') else t['id'] for t in go_terms],
                'go_term_labels': [t['label'] for t in go_terms],
                'interpro_ids': list(set(interpro_ids)),
                'funfam_ids': list(set(funfam_ids)),
                'condition_types': list(set(condition_types)),
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

        # Use mainRule from enriched data, not rule_obj
        main_rule = enriched.get('mainRule', {})
        rule_label = enriched.get('information', {}).get('label', '')

        # Get GO annotations
        go_terms = []
        go_annotations = main_rule.get('annotations', [])
        for go_ann in go_annotations:
            if go_ann.get('annotationType') == 'function':
                go_id = go_ann.get('value', '')
                go_label = go_ann.get('label', '')
                if go_id:
                    go_terms.append({'id': go_id, 'label': go_label})

        # Get protein counts
        stats = enriched.get('statistics', {})
        reviewed_count = stats.get('reviewedProteinCount', 0)
        unreviewed_count = stats.get('unreviewedProteinCount', 0)
        total_entries = reviewed_count + unreviewed_count

        # Extract condition values for faceting
        interpro_ids = []
        funfam_ids = []
        condition_types = []

        for cond_set in main_rule.get('conditionSets', []):
            for cond in cond_set.get('conditions', []):
                cond_type = cond.get('type', '')
                if cond_type:
                    condition_types.append(cond_type)

                for val in cond.get('conditionValues', []):
                    if cond_type == 'InterPro id':
                        ipr_id = val.get('value', '')
                        ipr_label = val.get('label', '')
                        if ipr_id:
                            interpro_ids.append(f"{ipr_id} ({ipr_label})" if ipr_label else ipr_id)
                    elif cond_type == 'FunFam id':
                        funfam_id = val.get('value', '')
                        funfam_label = val.get('label', '')
                        if funfam_id:
                            funfam_ids.append(f"{funfam_id} ({funfam_label})" if funfam_label else funfam_id)

        rule_info = {
            'id': rule_id,
            'rule_id': rule_id,
            'description': rule_label,
            'action': None,
            'status': 'NOT_REVIEWED',
            'confidence': None,
            'num_condition_sets': len(main_rule.get('conditionSets', [])),
            'num_entries': total_entries,
            'go_terms': go_terms,
            'go_term_ids': [f"{t['id']} ({t['label']})" if t.get('label') else t['id'] for t in go_terms],
            'go_term_labels': [t['label'] for t in go_terms],
            'interpro_ids': list(set(interpro_ids)),  # Remove duplicates
            'funfam_ids': list(set(funfam_ids)),
            'condition_types': list(set(condition_types)),
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
