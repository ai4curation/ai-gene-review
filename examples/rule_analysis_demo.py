#!/usr/bin/env python
"""Demonstration of ARBA rule post-enrichment analysis.

This script demonstrates how to use the rule_analysis module to:
1. Analyze InterPro domain overlap using Jaccard similarity
2. Detect redundancy with InterPro2GO mappings
3. Generate comprehensive analysis reports

Example usage:
    # Generate all formats in one run (most efficient)
    uv run python examples/rule_analysis_demo.py ARBA00026249 --output-dir rules/arba/ARBA00026249

    # Generate single format
    uv run python examples/rule_analysis_demo.py ARBA00026249 --output analysis.yaml
    uv run python examples/rule_analysis_demo.py ARBA00026249 --output analysis.json
    uv run python examples/rule_analysis_demo.py ARBA00026249 --output report.txt --format text

    # Console output only
    uv run python examples/rule_analysis_demo.py ARBA00026249
"""

import argparse
import json
from pathlib import Path

from ai_gene_review.etl.arba import ARBAClient
from ai_gene_review.etl.rule_analysis import (
    analyze_rule_post_enrichment,
    export_analysis_to_yaml,
    format_analysis_as_text,
    plot_domain_overlap_heatmap
)


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Analyze ARBA rule for InterPro overlap and ipr2go redundancy"
    )
    parser.add_argument(
        "rule_id",
        help="ARBA rule ID (e.g., ARBA00026249)"
    )
    parser.add_argument(
        "--cache-dir",
        type=Path,
        default=Path("rules/arba"),
        help="Cache directory for rules and ipr2go file (default: rules/arba)"
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Output file for analysis results (optional, format auto-detected from extension)"
    )
    parser.add_argument(
        "--format",
        choices=["yaml", "json", "text"],
        help="Output format (if not specified, inferred from --output extension or defaults to yaml)"
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        help="Output directory to write all formats (YAML, JSON, text, heatmap)"
    )
    parser.add_argument(
        "--no-report",
        action="store_true",
        help="Skip printing human-readable report to console"
    )
    parser.add_argument(
        "--heatmap",
        type=Path,
        help="Generate containment heatmap and save to this path (PNG format)"
    )

    args = parser.parse_args()

    # Fetch rule
    print(f"Fetching rule {args.rule_id}...")
    client = ARBAClient(cache_dir=args.cache_dir)
    rule = client.fetch_rule(args.rule_id)

    if not rule:
        print(f"Error: Rule {args.rule_id} not found")
        return 1

    # Run analysis
    print("Running post-enrichment analysis...")
    analysis = analyze_rule_post_enrichment(rule, args.cache_dir)

    # Handle --output-dir mode (write all formats to directory)
    if args.output_dir:
        args.output_dir.mkdir(parents=True, exist_ok=True)

        # Write YAML
        yaml_path = args.output_dir / f"{args.rule_id}-analysis.yaml"
        export_analysis_to_yaml(analysis, yaml_path)
        print(f"Analysis saved to {yaml_path} (YAML format)")

        # Write JSON
        json_path = args.output_dir / f"{args.rule_id}-analysis.json"
        json_path.write_text(json.dumps(analysis, indent=2))
        print(f"Analysis saved to {json_path} (JSON format)")

        # Write text
        text_path = args.output_dir / f"{args.rule_id}-analysis.txt"
        text_path.write_text(format_analysis_as_text(analysis))
        print(f"Analysis saved to {text_path} (Text format)")

        # Generate heatmap (function prints its own message)
        heatmap_path = args.output_dir / f"{args.rule_id}-heatmap.png"
        plot_domain_overlap_heatmap(analysis, heatmap_path)

    # Handle single --output mode
    elif args.output:
        if args.format:
            output_format = args.format
        else:
            # Infer from extension
            suffix = args.output.suffix.lower()
            if suffix == ".yaml" or suffix == ".yml":
                output_format = "yaml"
            elif suffix == ".json":
                output_format = "json"
            elif suffix == ".txt" or suffix == ".md":
                output_format = "text"
            else:
                output_format = "yaml"  # Default

        # Write output
        args.output.parent.mkdir(parents=True, exist_ok=True)

        if output_format == "yaml":
            export_analysis_to_yaml(analysis, args.output)
            print(f"Analysis saved to {args.output} (YAML format)")
        elif output_format == "json":
            args.output.write_text(json.dumps(analysis, indent=2))
            print(f"Analysis saved to {args.output} (JSON format)")
        elif output_format == "text":
            args.output.write_text(format_analysis_as_text(analysis))
            print(f"Analysis saved to {args.output} (Text format)")

        # Generate heatmap if requested
        if args.heatmap:
            plot_domain_overlap_heatmap(analysis, args.heatmap)

    # Handle standalone --heatmap mode
    elif args.heatmap:
        plot_domain_overlap_heatmap(analysis, args.heatmap)

    # Print report to console
    if not args.no_report:
        print()
        print(format_analysis_as_text(analysis))

    return 0


if __name__ == "__main__":
    exit(main())
