#!/usr/bin/env python3
"""Fix Epe1 findings that have generic supporting text."""

import yaml
from pathlib import Path

yaml_path = Path('genes/pombe/Epe1/Epe1-ai-review.yaml')

with open(yaml_path, 'r') as f:
    data = yaml.safe_load(f)

# Remove findings with "See reference for details" supporting text
if 'references' in data:
    for ref in data['references']:
        if 'findings' in ref and isinstance(ref['findings'], list):
            # Keep only findings without generic supporting text or convert to empty list
            new_findings = []
            for finding in ref['findings']:
                if isinstance(finding, dict):
                    supporting_text = finding.get('supporting_text', '')
                    if supporting_text != 'See reference for details':
                        new_findings.append(finding)
            ref['findings'] = new_findings

with open(yaml_path, 'w') as f:
    yaml.dump(data, f, default_flow_style=False, sort_keys=False, allow_unicode=True)

print(f"Fixed {yaml_path.name}")