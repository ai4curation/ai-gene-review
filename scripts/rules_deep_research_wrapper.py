#!/usr/bin/env python3
"""Wrapper for deep-research-client for UniProt annotation rules.

This script:
1. Accepts rule_id and provider
2. Auto-detects rule type from prefix (ARBA* -> arba, UR* -> unirule)
3. Reads enriched JSON for context
4. Calls deep-research-client with rule-specific template
5. Outputs to rules/{type}/{rule_id}/{rule_id}-deep-research-{provider}.md
"""

import argparse
import json
import subprocess
import sys
from pathlib import Path


def detect_rule_type(rule_id: str) -> str:
    """Detect rule type from rule ID prefix.

    Args:
        rule_id: Rule identifier (e.g., ARBA00026249, UR000000070)

    Returns:
        Rule type: 'arba' or 'unirule'

    Raises:
        ValueError: If rule ID prefix is not recognized
    """
    if rule_id.startswith("ARBA"):
        return "arba"
    elif rule_id.startswith("UR"):
        return "unirule"
    else:
        raise ValueError(f"Unknown rule ID prefix: {rule_id}. Expected ARBA* or UR*")


def format_conditions_summary(rule_json: dict) -> str:
    """Format conditions into human-readable summary.

    Args:
        rule_json: Rule JSON data (preferably enriched)

    Returns:
        Formatted string describing the rule conditions
    """
    lines = []
    main_rule = rule_json.get("mainRule", {})
    condition_sets = main_rule.get("conditionSets", [])

    for i, cs in enumerate(condition_sets, 1):
        conditions = cs.get("conditions", [])
        if not conditions:
            continue

        cond_strs = []
        for cond in conditions:
            cond_type = cond.get("type", "unknown")
            is_negative = cond.get("isNegative", False)
            neg_prefix = "NOT " if is_negative else ""

            # Get first condition value
            cv = {}
            cond_values = cond.get("conditionValues", [])
            if cond_values:
                cv = cond_values[0]

            value = cv.get("value", "")
            label = cv.get("label", "")
            curie = cv.get("curie", "")

            if label:
                cond_strs.append(f"{neg_prefix}{cond_type}: {label} ({curie or value})")
            else:
                cond_strs.append(f"{neg_prefix}{cond_type}: {value}")

        if cond_strs:
            lines.append(f"**Condition Set {i}:** " + " AND ".join(cond_strs))

    if len(condition_sets) > 1:
        return "\n\n".join(lines) + "\n\n*These condition sets are OR-ed together (any match triggers the annotation)*"
    return "\n\n".join(lines)


def format_go_terms(rule_json: dict) -> str:
    """Extract and format GO terms from rule.

    Args:
        rule_json: Rule JSON data

    Returns:
        Formatted string of GO terms
    """
    go_terms = []
    main_rule = rule_json.get("mainRule", {})

    for ann in main_rule.get("annotations", []):
        dbref = ann.get("dbReference", {})
        if dbref.get("database") == "GO":
            go_id = dbref.get("id", "")
            go_label = dbref.get("label", "")
            if go_id:
                if go_label:
                    go_terms.append(f"{go_id} ({go_label})")
                else:
                    go_terms.append(go_id)

    return ", ".join(go_terms) if go_terms else "No GO terms"


def get_protein_count(rule_json: dict) -> str:
    """Get protein count summary.

    Args:
        rule_json: Rule JSON data

    Returns:
        Formatted string with protein counts
    """
    stats = rule_json.get("statistics", {})
    reviewed = stats.get("reviewedProteinCount", 0)
    unreviewed = stats.get("unreviewedProteinCount", 0)
    total = reviewed + unreviewed
    return f"{total} total ({reviewed} reviewed, {unreviewed} unreviewed)"


def run_deep_research(
    rule_id: str,
    rule_type: str,
    provider: str,
    output_path: Path,
    rule_context: dict,
    extra_args: list = None,
    use_template: bool = True
) -> int:
    """Run deep-research-client with proper arguments.

    Args:
        rule_id: Rule identifier
        rule_type: Rule type (arba or unirule)
        provider: Provider name (openai, perplexity, perplexity-lite, falcon)
        output_path: Where to write output
        rule_context: Dictionary with rule context fields
        extra_args: Additional arguments to pass
        use_template: Whether to use template (False for perplexity-lite)

    Returns:
        Exit code from deep-research-client
    """
    # Map internal provider names to deep-research-client provider names
    actual_provider = "perplexity" if provider == "perplexity-lite" else provider

    if use_template:
        cmd = [
            "uv", "run", "deep-research-client", "research",
            "--template", "templates/rule_research.md",
            "--var", f"rule_id={rule_id}",
            "--var", f"rule_type={rule_type}",
            "--var", f"go_terms={rule_context.get('go_terms', '')}",
            "--var", f"conditions_summary={rule_context.get('conditions_summary', '')}",
            "--var", f"protein_count={rule_context.get('protein_count', '')}",
            "--provider", actual_provider,
            "--output", str(output_path)
        ]
    else:
        # For perplexity-lite, use direct query
        go_terms = rule_context.get('go_terms', 'unknown GO terms')
        query = (
            f"Research the UniProt annotation rule {rule_id} which predicts {go_terms}. "
            f"This rule annotates proteins based on: {rule_context.get('conditions_summary', '')}. "
            f"Evaluate whether the domain/signature combinations appropriately predict the GO term, "
            f"what experimental evidence supports this, and whether there are better GO terms."
        )
        cmd = [
            "uv", "run", "deep-research-client", "research",
            query,
            "--provider", actual_provider,
            "--param", "reasoning_effort=low",
            "--param", "model=sonar-pro",
            "--output", str(output_path)
        ]

    if extra_args:
        cmd.extend(extra_args)

    print(f"Running: {' '.join(cmd[:10])}...")  # Truncate for readability
    result = subprocess.run(cmd)
    return result.returncode


def main():
    parser = argparse.ArgumentParser(
        description="Deep research wrapper for UniProt annotation rules"
    )

    parser.add_argument("rule_id", help="Rule identifier (ARBA00026249, UR000000070)")
    parser.add_argument("provider", help="Provider (openai, perplexity, perplexity-lite, falcon)")
    parser.add_argument("--cache-dir", default="rules", help="Rules cache directory")
    parser.add_argument("--extra-args", nargs=argparse.REMAINDER, help="Extra args to pass")

    args = parser.parse_args()

    # Detect rule type from ID
    try:
        rule_type = detect_rule_type(args.rule_id)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

    # Find rule file
    cache_dir = Path(args.cache_dir)
    rule_dir = cache_dir / rule_type / args.rule_id

    # Prefer enriched JSON
    enriched_file = rule_dir / f"{args.rule_id}.enriched.json"
    raw_file = rule_dir / f"{args.rule_id}.json"

    if enriched_file.exists():
        rule_file = enriched_file
        print(f"Using enriched rule file: {rule_file}")
    elif raw_file.exists():
        rule_file = raw_file
        print(f"Warning: Using raw rule file (labels may be missing): {rule_file}")
    else:
        print(f"Error: Rule file not found in {rule_dir}", file=sys.stderr)
        print(f"Run 'just arba-sync' or 'just unirule-sync' first to fetch rules", file=sys.stderr)
        return 1

    # Load rule JSON
    with open(rule_file) as f:
        rule_json = json.load(f)

    # Extract context
    rule_context = {
        'go_terms': format_go_terms(rule_json),
        'conditions_summary': format_conditions_summary(rule_json),
        'protein_count': get_protein_count(rule_json)
    }

    print(f"Rule {args.rule_id} ({rule_type.upper()}):")
    print(f"  GO Terms: {rule_context['go_terms']}")
    print(f"  Proteins: {rule_context['protein_count']}")

    # Construct output path
    if args.provider == "perplexity-lite":
        output_file = rule_dir / f"{args.rule_id}-deep-research-perplexity-lite.md"
        use_template = False
    else:
        output_file = rule_dir / f"{args.rule_id}-deep-research-{args.provider}.md"
        use_template = True

    # Create directory if it doesn't exist
    rule_dir.mkdir(parents=True, exist_ok=True)

    # Run deep research
    return run_deep_research(
        rule_id=args.rule_id,
        rule_type=rule_type,
        provider=args.provider,
        output_path=output_file,
        rule_context=rule_context,
        extra_args=args.extra_args,
        use_template=use_template
    )


if __name__ == "__main__":
    sys.exit(main())
