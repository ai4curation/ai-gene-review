#!/usr/bin/env python
"""Demonstration of complete rule analysis and HTML rendering workflow.

This script shows how to:
1. Fetch an ARBA rule
2. Run post-enrichment analysis (domain overlap, InterPro2GO redundancy)
3. Generate a heatmap visualization
4. Render the rule review YAML to HTML with embedded statistics and visualization

Example:
    $ uv run python examples/render_rule_review_demo.py ARBA00026249
    $ uv run python examples/render_rule_review_demo.py ARBA00026249 --output-dir /tmp/demo
"""

import argparse
from pathlib import Path

from ai_gene_review.etl.arba import ARBAClient
from ai_gene_review.etl.rule_analysis import (
    analyze_rule_post_enrichment,
    plot_domain_overlap_heatmap,
    render_rule_review_html,
)


def main():
    parser = argparse.ArgumentParser(
        description="Analyze an ARBA rule and render HTML review",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument(
        "rule_id", help="ARBA rule ID (e.g., ARBA00026249)"
    )

    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("rules/arba"),
        help="Output directory for analysis files (default: rules/arba)",
    )

    parser.add_argument(
        "--skip-analysis",
        action="store_true",
        help="Skip analysis and just render existing YAML to HTML",
    )

    parser.add_argument(
        "--request-delay",
        type=float,
        default=0.2,
        help="Delay between API requests in seconds (default: 0.2)",
    )

    args = parser.parse_args()

    rule_id = args.rule_id
    output_dir = args.output_dir
    rule_dir = output_dir / rule_id

    # Create output directory if needed
    rule_dir.mkdir(parents=True, exist_ok=True)

    print(f"\n{'='*60}")
    print(f"Rule Analysis and HTML Rendering Demo")
    print(f"{'='*60}\n")
    print(f"Rule ID: {rule_id}")
    print(f"Output directory: {output_dir}\n")

    # Step 1: Fetch the rule
    print("Step 1: Fetching ARBA rule...")
    client = ARBAClient(cache_dir=output_dir)
    rule = client.fetch_rule(rule_id)
    print(f"  ✓ Fetched rule: {rule.uni_rule_id}")

    if not args.skip_analysis:
        # Step 2: Run post-enrichment analysis
        print("\nStep 2: Running post-enrichment analysis...")
        analysis = analyze_rule_post_enrichment(
            rule, output_dir, request_delay=args.request_delay
        )
        print(f"  ✓ Analyzed {len(analysis['domain_overlap_analysis']['pairs'])} domain pairs")
        print(f"  ✓ Found {len(analysis['ipr2go_redundancy']['redundant_annotations'])} redundant annotations")

        # Step 3: Generate heatmap
        print("\nStep 3: Generating domain overlap heatmap...")
        heatmap_path = rule_dir / f"{rule_id}-heatmap.png"
        plot_domain_overlap_heatmap(analysis, heatmap_path)
        print(f"  ✓ Heatmap saved to {heatmap_path}")
    else:
        print("\nStep 2-3: Skipped (--skip-analysis flag set)")

    # Step 4: Render HTML review
    print("\nStep 4: Rendering HTML review...")
    review_yaml = rule_dir / f"{rule_id}-review.yaml"

    if not review_yaml.exists():
        print(f"  ✗ Review YAML not found at {review_yaml}")
        print(f"    Please create a review YAML file first.")
        return

    html_path = render_rule_review_html(rule_id, output_dir)
    print(f"  ✓ HTML review rendered to {html_path}")

    print(f"\n{'='*60}")
    print("Summary of Generated Files:")
    print(f"{'='*60}")
    print(f"  Rule JSON:     {rule_dir / f'{rule_id}.json'}")
    print(f"  Enriched JSON: {rule_dir / f'{rule_id}.enriched.json'}")
    if not args.skip_analysis:
        print(f"  Analysis TXT:  {rule_dir / f'{rule_id}-analysis.txt'}")
        print(f"  Heatmap PNG:   {heatmap_path}")
    print(f"  Review YAML:   {review_yaml}")
    print(f"  Review HTML:   {html_path}")
    print(f"\nOpen the HTML file in a browser to view the complete review:")
    print(f"  open {html_path}")
    print()


if __name__ == "__main__":
    main()
