"""Initialize rule review YAML files with proper structure and TODO stubs.

This module provides functions to create initial rule review YAML files
that include all necessary fields and TODO placeholders for AI-assisted review.
"""

from pathlib import Path
from typing import Union
import yaml
from ai_gene_review.etl.arba import ARBAClient
from ai_gene_review.etl.unirule import UniRuleClient
from ai_gene_review.etl.rule_enrichment import enrich_rule_json


def init_rule_review(
    rule_id: str,
    cache_dir: Path = Path("rules/arba"),
    force: bool = False
) -> Path:
    """Initialize a rule review YAML file with proper structure and TODO stubs.

    Creates a rule review YAML file at {cache_dir}/{rule_id}/{rule_id}-review.yaml
    with all required fields populated and TODO placeholders where manual review is needed.

    Also ensures that:
    - The enriched.json file exists (fetches and enriches if missing)
    - The rule directory exists

    Args:
        rule_id: Rule identifier (e.g., 'ARBA00026249', 'UR000000070')
        cache_dir: Directory to store rule data (default: rules/arba)
        force: If True, overwrite existing review file

    Returns:
        Path to the created review YAML file

    Raises:
        FileExistsError: If review file exists and force=False

    Examples:
        >>> init_rule_review('ARBA00026249')  # doctest: +SKIP
        PosixPath('rules/arba/ARBA00026249/ARBA00026249-review.yaml')
    """
    # Determine rule type from ID
    client: Union[ARBAClient, UniRuleClient]
    if rule_id.startswith('ARBA'):
        rule_type = 'ARBA'
        client = ARBAClient(cache_dir=cache_dir)
    elif rule_id.startswith('UR'):
        rule_type = 'UniRule'
        client = UniRuleClient(cache_dir=cache_dir)
    else:
        raise ValueError(f"Unknown rule type for ID: {rule_id}")

    # Create rule directory
    rule_dir = cache_dir / rule_id
    rule_dir.mkdir(parents=True, exist_ok=True)

    # Check if review file already exists
    review_path = rule_dir / f"{rule_id}-review.yaml"
    if review_path.exists() and not force:
        raise FileExistsError(
            f"Review file already exists: {review_path}\n"
            f"Use force=True to overwrite"
        )

    # Fetch and enrich rule if enriched.json doesn't exist
    enriched_path = rule_dir / f"{rule_id}.enriched.json"
    import json

    if not enriched_path.exists():
        print(f"Fetching rule {rule_id}...")
        rule = client.fetch_rule(rule_id)
        if rule is None:
            raise ValueError(f"Rule {rule_id} not found")

        print(f"Enriching rule {rule_id}...")
        enriched_rule = enrich_rule_json(rule.to_json(), enricher=None)

        # Save enriched rule
        with open(enriched_path, 'w') as f:
            json.dump(enriched_rule, f, indent=2)
        print(f"✓ Created {enriched_path}")
    else:
        # Load existing enriched rule
        with open(enriched_path) as f:
            enriched_rule = json.load(f)

    # Create review YAML stub
    review_data = _create_review_stub(rule_id, rule_type, enriched_rule)

    # Write review YAML
    with open(review_path, 'w') as f:
        yaml.dump(review_data, f, default_flow_style=False, sort_keys=False, allow_unicode=True)

    print(f"✓ Created {review_path}")
    print("\nNext steps:")
    print(f"  1. Run: just analyze-rule {rule_id}")
    print(f"  2. Run: just sync-rule-review-single {rule_id}")
    print(f"  3. Run: just rules-deep-research-perplexity {rule_id}")
    print(f"  4. Edit {review_path} to fill in TODO placeholders")
    print(f"  5. Run: just render-rule {rule_id}")

    return review_path


def _create_review_stub(rule_id: str, rule_type: str, enriched_rule: dict) -> dict:
    """Create a review YAML stub with TODO placeholders.

    Args:
        rule_id: Rule identifier
        rule_type: 'ARBA' or 'UniRule'
        enriched_rule: Enriched rule data from rule_enrichment

    Returns:
        Dictionary with review structure and TODO placeholders
    """
    # Extract basic info from enriched rule
    condition_sets = enriched_rule.get('rule_set', {}).get('condition_sets', [])
    annotations = enriched_rule.get('rule_set', {}).get('annotations', [])

    # Build condition sets for review YAML (without pairwise_overlap - that comes from sync)
    review_condition_sets = []
    for cs_idx, cs in enumerate(condition_sets, start=1):
        conditions = []
        for cond in cs.get('conditions', []):
            # Extract condition info
            cond_dict = {
                'condition_type': cond.get('condition_type', ''),
                'value': cond.get('condition', ''),
                'curie': cond.get('curie', ''),
                'label': cond.get('label', ''),
                'negated': cond.get('negated', False)
            }
            conditions.append(cond_dict)

        review_cs = {
            'number': cs_idx,
            'conditions': conditions,
            'notes': 'TODO: Describe this condition set and what proteins it captures'
            # NOTE: pairwise_overlap will be added by sync-rule-review-single
        }
        review_condition_sets.append(review_cs)

    # Build GO annotations
    go_annotations = []
    for annot in annotations:
        if annot.get('annotation_type') == 'GO':
            go_annotations.append({
                'go_id': annot.get('go_id', ''),
                'go_label': annot.get('go_label', ''),
                'aspect': annot.get('aspect', '')
            })

    # Create review structure
    review_data = {
        'id': rule_id,
        'description': 'TODO: Provide a concise description of what this rule predicts and how',
        'status': 'IN_PROGRESS',
        'rule_type': rule_type,
        'rule': {
            'rule_id': rule_id,
            'condition_sets': review_condition_sets,
            'go_annotations': go_annotations,
            'reviewed_protein_count': enriched_rule.get('reviewed_protein_count', 0),
            'unreviewed_protein_count': enriched_rule.get('unreviewed_protein_count', 0),
            'created_date': enriched_rule.get('created_date', ''),
            'modified_date': enriched_rule.get('modified_date', ''),
            # NOTE: entries field will be added by sync-rule-review-single after analysis
        },
        'review_summary': 'TODO: Summarize the overall quality and utility of this rule',
        'action': 'UNDECIDED',
        'action_rationale': 'TODO: Explain why this action is recommended',
        'suggested_modifications': [
            'TODO: List specific modifications if action is MODIFY'
        ],
        'parsimony': {
            'assessment': 'UNDECIDED',
            'notes': 'TODO: Evaluate whether rule conditions are parsimonious or redundant'
        },
        'literature_support': {
            'assessment': 'UNDECIDED',
            'notes': 'TODO: Evaluate literature support for this annotation',
            'supported_by': [
                {
                    'reference_id': f'file:rules/{rule_type.lower()}/{rule_id}/{rule_id}-deep-research-perplexity.md',
                    'supporting_text': 'TODO: Add key findings from deep research'
                }
            ]
        },
        'condition_overlap': {
            'assessment': 'UNDECIDED',
            'notes': 'TODO: Analyze domain overlap patterns within and across condition sets',
            'supported_by': []
        },
        'go_specificity': {
            'assessment': 'UNDECIDED',
            'notes': 'TODO: Evaluate whether GO term is at appropriate specificity level',
            'supported_by': []
        },
        'taxonomic_scope': {
            'assessment': 'UNDECIDED',
            'notes': 'TODO: Evaluate whether taxonomic restrictions are appropriate',
            'supported_by': []
        },
        'confidence': 0.0,
        'references': [
            {
                'id': f'file:rules/{rule_type.lower()}/{rule_id}/{rule_id}-deep-research-perplexity.md',
                'title': 'Deep research analysis via Perplexity',
                'findings': [
                    {
                        'statement': 'TODO: Add key findings from literature review'
                    }
                ]
            }
        ],
        'supported_by': []
    }

    return review_data
