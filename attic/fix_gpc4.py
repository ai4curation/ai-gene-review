#!/usr/bin/env python3
"""Fix schema issues in GPC4-ai-review.yaml"""
import yaml

filepath = "genes/human/GPC4/GPC4-ai-review.yaml"

with open(filepath, 'r') as f:
    data = yaml.safe_load(f)

# Fix findings - convert strings to proper Finding objects
if 'references' in data:
    for ref in data['references']:
        if 'findings' in ref and ref['findings']:
            new_findings = []
            for finding in ref['findings']:
                if isinstance(finding, str):
                    new_findings.append({'statement': finding})
                else:
                    new_findings.append(finding)
            ref['findings'] = new_findings

# Fix proposed_replacement_terms in existing_annotations
if 'existing_annotations' in data:
    for ann in data['existing_annotations']:
        if 'review' in ann and 'proposed_replacement_terms' in ann['review']:
            terms = ann['review']['proposed_replacement_terms']
            new_terms = []
            for term in terms:
                if isinstance(term, str):
                    # Parse "GO:XXXXXXX term name" format
                    if term.startswith('GO:'):
                        parts = term.split(' ', 1)
                        term_id = parts[0]
                        term_label = parts[1] if len(parts) > 1 else ""
                        new_terms.append({'id': term_id, 'label': term_label})
                    else:
                        new_terms.append({'id': '', 'label': term})
                else:
                    new_terms.append(term)
            ann['review']['proposed_replacement_terms'] = new_terms

# Fix core_functions - convert 'term'/'summary' to 'molecular_function'/'description'
if 'core_functions' in data:
    new_core_funcs = []
    for cf in data['core_functions']:
        new_cf = {}
        # Handle molecular_function
        if 'term' in cf and 'molecular_function' not in cf:
            new_cf['molecular_function'] = cf['term']
        elif 'molecular_function' in cf:
            new_cf['molecular_function'] = cf['molecular_function']

        # Handle description
        if 'summary' in cf and 'description' not in cf:
            new_cf['description'] = cf['summary']
        elif 'description' in cf:
            new_cf['description'] = cf['description']
        elif 'evidence_summary' in cf:
            new_cf['description'] = cf['evidence_summary']

        # Copy supported_by if present
        if 'supported_by' in cf:
            new_cf['supported_by'] = cf['supported_by']

        # Copy directly_involved_in if present
        if 'directly_involved_in' in cf:
            new_cf['directly_involved_in'] = cf['directly_involved_in']

        # Copy locations if present
        if 'locations' in cf:
            new_cf['locations'] = cf['locations']

        new_core_funcs.append(new_cf)
    data['core_functions'] = new_core_funcs

# Fix suggested_questions - remove 'rationale' if present
if 'suggested_questions' in data:
    for q in data['suggested_questions']:
        if 'rationale' in q:
            del q['rationale']

# Fix suggested_experiments - rename 'experiment' to 'description'
if 'suggested_experiments' in data:
    for exp in data['suggested_experiments']:
        if 'experiment' in exp and 'description' not in exp:
            exp['description'] = exp.pop('experiment')
        if 'rationale' in exp:
            del exp['rationale']

with open(filepath, 'w') as f:
    yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False, width=120)

print("Fixed GPC4-ai-review.yaml")
