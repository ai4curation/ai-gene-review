#!/usr/bin/env python3
"""
Apply systematic reviews to P14713 annotations.
This updates the YAML file with curated decisions.
"""

import yaml
from pathlib import Path

# Load the YAML with proper settings to preserve structure
yaml_path = Path("P14713-ai-review.yaml")
with open(yaml_path) as f:
    data = yaml.safe_load(f)

# Import review decisions from batch_review.py
from batch_review import reviews

# Track statistics
stats = {
    "total": len(data['existing_annotations']),
    "updated": 0,
    "already_done": 0,
    "no_review_defined": 0,
}

# Apply reviews to each annotation
for ann in data['existing_annotations']:
    term_id = ann['term']['id']

    # Skip if already reviewed (not PENDING)
    if ann['review']['action'] != 'PENDING':
        stats['already_done'] += 1
        continue

    # Check if we have a review for this term
    if term_id not in reviews:
        stats['no_review_defined'] += 1
        continue

    # Apply the review
    review_data = reviews[term_id]
    ann['review']['summary'] = review_data['summary']
    ann['review']['action'] = review_data['action']

    # Add reason if provided
    if 'reason' in review_data:
        ann['review']['reason'] = review_data['reason']

    stats['updated'] += 1

# Report
print("Review Application Report")
print("=" * 50)
print(f"Total annotations: {stats['total']}")
print(f"Already reviewed:  {stats['already_done']}")
print(f"Newly updated:     {stats['updated']}")
print(f"No review defined: {stats['no_review_defined']}")
print()

# Show which terms still need review
if stats['no_review_defined'] > 0:
    print("Terms still needing review:")
    seen_terms = set()
    for ann in data['existing_annotations']:
        if ann['review']['action'] == 'PENDING':
            term_id = ann['term']['id']
            if term_id not in seen_terms and term_id not in reviews:
                print(f"  - {term_id}: {ann['term']['label']}")
                seen_terms.add(term_id)

# Save updated YAML
print(f"\nSaving to {yaml_path}...")
with open(yaml_path, 'w') as f:
    yaml.dump(data, f, default_flow_style=False, sort_keys=False, allow_unicode=True)

print("Done!")
