#!/usr/bin/env python3
"""Fix M2 validation error by using the exact text from the publication with smart quotes."""

import yaml
from pathlib import Path

# File to fix
file_path = Path("genes/9INFA/M2/M2-ai-review.yaml")

# Load the YAML file
with open(file_path, 'r') as f:
    data = yaml.safe_load(f)

# The correct text from the publication (with smart quotes)
correct_text = 'An early model envisioned a continuous aqueous channel that was gated by pH (shutter mechanism), 20 versus the currently accepted model in which protons diffuse along a water wire until reaching His37, where they are then "shuttled" by His37 through alternate protonation and deprotonation events'

# Find and update the supporting text
# It's in references[1].findings[8].supporting_text
if len(data['references']) > 1:
    ref1 = data['references'][1]
    if ref1.get('id') == 'PMID:18235504':
        if 'findings' in ref1 and len(ref1['findings']) > 8:
            # Update the supporting text with the version that has smart quotes
            ref1['findings'][8]['supporting_text'] = correct_text
            print("Updated supporting text with smart quotes version")

# Write the fixed YAML back
with open(file_path, 'w') as f:
    yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

print(f"Fixed M2 file: {file_path}")
print('The issue was that the publication uses smart quotes around "shuttled" while the YAML had regular quotes.')