#!/usr/bin/env python3
"""Fix remaining schema issues in GPC4 and GPC6 ai-review.yaml files"""
import yaml
import re

def fix_review(filepath):
    print(f"Fixing {filepath}...")
    with open(filepath, 'r') as f:
        data = yaml.safe_load(f)

    # Fix core_functions supported_by reference_id format
    if 'core_functions' in data:
        for cf in data['core_functions']:
            if 'supported_by' in cf:
                new_supported = []
                for s in cf['supported_by']:
                    if isinstance(s, dict):
                        if 'reference_id' in s:
                            ref_id = s['reference_id']
                            # If reference_id is a dict with 'id', extract it
                            if isinstance(ref_id, dict) and 'id' in ref_id:
                                s['reference_id'] = ref_id['id']
                        new_supported.append(s)
                    elif isinstance(s, str):
                        new_supported.append({'reference_id': s})
                cf['supported_by'] = new_supported

    # Collect existing reference IDs
    existing_refs = set()
    if 'references' in data:
        for ref in data['references']:
            if 'id' in ref:
                existing_refs.add(ref['id'])

    # Collect needed Reactome references from annotations
    needed_reactome = set()
    if 'existing_annotations' in data:
        for ann in data['existing_annotations']:
            ref_id = ann.get('original_reference_id', '')
            if ref_id.startswith('Reactome:') and ref_id not in existing_refs:
                needed_reactome.add(ref_id)

    # Add placeholder Reactome references
    for reactome_id in sorted(needed_reactome):
        print(f"  Adding placeholder for {reactome_id}")
        data['references'].append({
            'id': reactome_id,
            'type': 'database',
            'findings': []
        })

    with open(filepath, 'w') as f:
        yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False, width=120)

    print(f"  Fixed {filepath}")

if __name__ == "__main__":
    files = [
        "genes/human/GPC4/GPC4-ai-review.yaml",
        "genes/human/GPC6/GPC6-ai-review.yaml"
    ]
    for f in files:
        try:
            fix_review(f)
        except Exception as e:
            print(f"Error fixing {f}: {e}")
