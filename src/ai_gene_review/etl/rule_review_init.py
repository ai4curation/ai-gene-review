"""Initialize rule review YAML files with proper structure and TODO stubs.

This module provides functions to create initial rule review YAML files
that include all necessary fields and TODO placeholders for AI-assisted review.
"""

import shlex
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
    if rule_type == 'ARBA':
        cache_text = str(cache_dir)
        analyze_command = shlex.join(
            ["just", "analyze-rule", rule_id, "--cache-dir", cache_text]
        )
        sync_command = shlex.join(
            ["just", "sync-rule-review-single", rule_id, cache_text]
        )
        render_command = shlex.join(
            ["just", "render-rule", rule_id, cache_text]
        )
        print(f"  1. Run: {analyze_command}")
        print(f"  2. Run: {sync_command}")
        print(f"  3. Run: just rules-deep-research-perplexity {rule_id}")
        print(f"  4. Edit {review_path} to fill in TODO placeholders")
        print(f"  5. Run: {render_command}")
    else:
        print(f"  1. Run: just rules-deep-research-perplexity {rule_id}")
        print(f"  2. Edit {review_path} to fill in TODO placeholders")
        print(
            "  Note: Post-enrichment analysis-dependent workflows currently "
            "support ARBA IDs only."
        )

    return review_path


CONDITION_TYPE_MAP = {
    "InterPro id": "INTERPRO",
    "FunFam id": "FUNFAM",
    "PANTHER id": "PANTHER",
    "Pfam id": "PFAM",
    "taxon": "TAXON",
}

NAME_SLOTS = (
    ("recommendedName", "RECOMMENDED"),
    ("alternativeNames", "ALTERNATIVE"),
    ("submissionNames", "SUBMISSION"),
)


def extract_condition_sets(rule_json: dict) -> list[dict]:
    """Build review-YAML condition sets from an (enriched) ARBA/UniRule JSON.

    Negation is read from the condition's ``isNegative`` flag. Accepts either
    a full rule JSON or its bare ``mainRule`` object.

    Args:
        rule_json: Rule JSON in UniProt format (``mainRule.conditionSets``)

    Returns:
        List of condition-set dicts matching ``RuleConditionSet``

    Examples:
        >>> rule = {"mainRule": {"conditionSets": [{"conditions": [
        ...     {"type": "taxon", "isNegative": False,
        ...      "conditionValues": [{"value": "Archaea", "curie": "NCBITaxon:2157"}]}]}]}}
        >>> cs = extract_condition_sets(rule)
        >>> cs[0]["conditions"][0]["condition_type"], cs[0]["conditions"][0]["curie"]
        ('TAXON', 'NCBITaxon:2157')
    """
    condition_sets = []
    # Accept either a full rule ({"mainRule": {...}}) or a bare main rule
    main_rule = rule_json.get("mainRule", rule_json)
    for cs_idx, cs in enumerate(main_rule.get("conditionSets", []), start=1):
        conditions = []
        for cond in cs.get("conditions", []):
            cond_type = cond.get("type", "")
            for cv in cond.get("conditionValues", []):
                conditions.append({
                    "condition_type": CONDITION_TYPE_MAP.get(cond_type, "OTHER"),
                    "value": cv.get("value", ""),
                    "curie": cv.get("curie", ""),
                    "label": cv.get("label", ""),
                    "negated": bool(cond.get("isNegative", False)),
                })
        condition_sets.append({"number": cs_idx, "conditions": conditions})
    return condition_sets


def _protein_names(protein_description: dict) -> list[dict]:
    """Flatten a UniProt ``proteinDescription`` into ``RuleProteinNameAnnotation`` dicts.

    Examples:
        >>> _protein_names({"recommendedName": {"fullName": {}, "ecNumbers": [{"value": "1.2.1.75"}]}})
        [{'name_type': 'RECOMMENDED', 'ec_numbers': ['1.2.1.75']}]
    """
    names = []
    for key, name_type in NAME_SLOTS:
        slot = protein_description.get(key)
        if slot is None:
            continue
        for name in slot if isinstance(slot, list) else [slot]:
            entry: dict = {"name_type": name_type}
            full_name = name.get("fullName", {}).get("value")
            if full_name:
                entry["full_name"] = full_name
            short_names = [sn["value"] for sn in name.get("shortNames", []) if sn.get("value")]
            if short_names:
                entry["short_names"] = short_names
            ec_numbers = [ec["value"] for ec in name.get("ecNumbers", []) if ec.get("value")]
            if ec_numbers:
                entry["ec_numbers"] = ec_numbers
            names.append(entry)
    return names


def extract_rule_annotations(rule_json: dict) -> dict[str, list[dict]]:
    """Collect a rule's consequents by kind: GO terms, protein names, catalytic activities.

    Args:
        rule_json: Rule JSON in UniProt format (``mainRule.annotations``)

    Returns:
        Dict with ``go_annotations``, ``protein_name_annotations`` and
        ``catalytic_activity_annotations`` lists

    Examples:
        >>> rule = {"mainRule": {"annotations": [{"comment": {
        ...     "commentType": "CATALYTIC ACTIVITY",
        ...     "reaction": {"name": "A = B", "ecNumber": "1.1.1.1",
        ...                  "reactionCrossReferences": [{"database": "Rhea", "id": "RHEA:1"}]}}}]}}
        >>> extract_rule_annotations(rule)["catalytic_activity_annotations"]
        [{'reaction_name': 'A = B', 'rhea_id': 'RHEA:1', 'ec_number': '1.1.1.1'}]
    """
    result: dict[str, list[dict]] = {
        "go_annotations": [],
        "protein_name_annotations": [],
        "catalytic_activity_annotations": [],
    }
    for ann in rule_json.get("mainRule", {}).get("annotations", []):
        dbref = ann.get("dbReference")
        if dbref and dbref.get("database") == "GO":
            go: dict = {"go_id": dbref.get("id", "")}
            if dbref.get("label"):
                go["go_label"] = dbref["label"]
            result["go_annotations"].append(go)
        if "proteinDescription" in ann:
            result["protein_name_annotations"].extend(_protein_names(ann["proteinDescription"]))
        reaction = ann.get("comment", {}).get("reaction")
        if reaction:
            activity: dict = {"reaction_name": reaction.get("name", "")}
            rhea = [x["id"] for x in reaction.get("reactionCrossReferences", [])
                    if x.get("database") == "Rhea"]
            if rhea:
                activity["rhea_id"] = rhea[0]
            if reaction.get("ecNumber"):
                activity["ec_number"] = reaction["ecNumber"]
            result["catalytic_activity_annotations"].append(activity)
    return result


def _create_review_stub(rule_id: str, rule_type: str, enriched_rule: dict) -> dict:
    """Create a review YAML stub with TODO placeholders.

    Args:
        rule_id: Rule identifier
        rule_type: 'ARBA' or 'UniRule'
        enriched_rule: Enriched rule data from rule_enrichment

    Returns:
        Dictionary with review structure and TODO placeholders
    """
    review_condition_sets = extract_condition_sets(enriched_rule)
    for cs in review_condition_sets:
        # pairwise_overlap is added later by sync-rule-review-single
        cs["notes"] = "TODO: Describe this condition set and what proteins it captures"
    consequents = extract_rule_annotations(enriched_rule)
    statistics = enriched_rule.get("statistics", {})

    # Create review structure
    review_data = {
        'id': rule_id,
        'description': 'TODO: Provide a concise description of what this rule predicts and how',
        'status': 'IN_PROGRESS',
        'rule_type': rule_type,
        'rule': {
            'rule_id': rule_id,
            'condition_sets': review_condition_sets,
            **consequents,
            'reviewed_protein_count': statistics.get('reviewedProteinCount', 0),
            'unreviewed_protein_count': statistics.get('unreviewedProteinCount', 0),
            'created_date': enriched_rule.get('createdDate', ''),
            'modified_date': enriched_rule.get('modifiedDate', ''),
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
