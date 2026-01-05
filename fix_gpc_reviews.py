#!/usr/bin/env python3
"""Fix schema issues in GPC4 and GPC6 ai-review.yaml files"""
import yaml
import sys

def fix_review(filepath):
    print(f"Fixing {filepath}...")
    with open(filepath, 'r') as f:
        data = yaml.safe_load(f)

    # Fix findings - convert strings/'finding' key to proper Finding objects with 'statement'
    if 'references' in data:
        for ref in data['references']:
            if 'findings' in ref and ref['findings']:
                new_findings = []
                for finding in ref['findings']:
                    if isinstance(finding, str):
                        new_findings.append({'statement': finding})
                    elif isinstance(finding, dict):
                        # Rename 'finding' to 'statement' if present
                        if 'finding' in finding and 'statement' not in finding:
                            new_finding = {'statement': finding['finding']}
                            # Copy any other valid fields
                            for key in ['supporting_text', 'full_text_unavailable', 'reference_section_type']:
                                if key in finding:
                                    new_finding[key] = finding[key]
                            new_findings.append(new_finding)
                        else:
                            new_findings.append(finding)
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
    # Also filter out BP terms
    if 'core_functions' in data:
        new_core_funcs = []
        for cf in data['core_functions']:
            new_cf = {}
            term_data = None

            # Get term data
            if 'term' in cf:
                term_data = cf['term']
            elif 'molecular_function' in cf:
                term_data = cf['molecular_function']

            if term_data:
                # Skip BP terms (common BP prefixes to filter)
                term_id = term_data.get('id', '') if isinstance(term_data, dict) else ''
                term_label = term_data.get('label', '') if isinstance(term_data, dict) else ''

                # Known BP terms to filter
                bp_terms = ['GO:0016055', 'GO:0098696', 'GO:0099560', 'GO:0007399', 'GO:0007275',
                           'GO:0060021', 'GO:0007605', 'GO:0060174', 'GO:0048513']

                if term_id in bp_terms:
                    print(f"  Skipping BP term: {term_id} {term_label}")
                    continue

                new_cf['molecular_function'] = term_data

            # Handle description
            if 'summary' in cf and 'description' not in cf:
                new_cf['description'] = cf['summary']
            elif 'description' in cf:
                new_cf['description'] = cf['description']
            elif 'evidence_summary' in cf:
                new_cf['description'] = cf['evidence_summary']

            # Copy supported_by - convert 'references' to 'supported_by' if needed
            if 'supported_by' in cf:
                new_cf['supported_by'] = cf['supported_by']
            elif 'references' in cf:
                # Convert references to supported_by format
                new_cf['supported_by'] = [{'reference_id': r} for r in cf['references']]

            # Copy directly_involved_in if present
            if 'directly_involved_in' in cf:
                new_cf['directly_involved_in'] = cf['directly_involved_in']

            # Copy locations if present
            if 'locations' in cf:
                new_cf['locations'] = cf['locations']

            if 'molecular_function' in new_cf:
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
