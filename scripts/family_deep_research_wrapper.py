#!/usr/bin/env python3
"""Wrapper for deep-research-client for PANTHER/InterPro protein families.

This script:
1. Accepts family_id (e.g., PTHR10314) and provider
2. Reads family metadata from interpro/panther/{family_id}/
3. Calls deep-research-client with family-specific template
4. Outputs to interpro/panther/{family_id}/{family_id}-deep-research-{provider}.md
"""

import argparse
import subprocess
import sys
from pathlib import Path

import yaml


def load_family_metadata(family_id: str, base_dir: Path) -> dict:
    """Load family metadata from YAML file.

    Args:
        family_id: PANTHER family ID (e.g., PTHR10314)
        base_dir: Base directory for interpro data

    Returns:
        Dictionary with family metadata
    """
    # Determine database type from prefix
    if family_id.startswith("PTHR"):
        db = "panther"
    elif family_id.startswith("PF"):
        db = "pfam"
    else:
        db = "panther"  # default

    metadata_path = base_dir / db / family_id / f"{family_id}-metadata.yaml"

    if not metadata_path.exists():
        print(f"Warning: Metadata file not found: {metadata_path}")
        print(f"Run: just fetch-panther-family {family_id}")
        return {
            "family_id": family_id,
            "family_name": "Unknown",
            "interpro_id": "",
            "root_node": "",
            "subfamily_count": 0,
            "subfamilies": [],
        }

    with open(metadata_path) as f:
        data = yaml.safe_load(f)

    # Extract relevant fields
    metadata = data.get("metadata", {})
    subfamilies = data.get("subfamilies", [])

    return {
        "family_id": family_id,
        "family_name": metadata.get("name", "Unknown"),
        "interpro_id": metadata.get("integrated", ""),
        "root_node": metadata.get("root_node", ""),
        "subfamily_count": len(subfamilies),
        "subfamilies": subfamilies,
    }


def format_subfamily_summary(subfamilies: list) -> str:
    """Format subfamilies into human-readable summary.

    Args:
        subfamilies: List of subfamily dictionaries

    Returns:
        Formatted markdown string
    """
    if not subfamilies:
        return "No subfamily information available."

    lines = []
    for sf in subfamilies[:20]:  # Limit to first 20 for readability
        sf_id = sf.get("accession", "")
        sf_name = sf.get("name", "Unknown")
        lines.append(f"- **{sf_id}**: {sf_name}")

    if len(subfamilies) > 20:
        lines.append(f"- ... and {len(subfamilies) - 20} more subfamilies")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Deep research wrapper for PANTHER/InterPro protein families"
    )
    parser.add_argument("family_id", help="Family ID (e.g., PTHR10314)")
    parser.add_argument(
        "provider",
        choices=["openai", "perplexity", "perplexity-lite", "falcon", "cyberian"],
        help="Deep research provider",
    )
    parser.add_argument(
        "--base-dir",
        type=Path,
        default=Path("interpro"),
        help="Base directory for interpro data (default: interpro)",
    )
    parser.add_argument(
        "--template",
        type=Path,
        default=Path("templates/family_research.md"),
        help="Template file for research",
    )
    parser.add_argument(
        "--extra-args",
        nargs="*",
        default=[],
        help="Extra arguments to pass to deep-research-client",
    )

    args = parser.parse_args()

    # Determine database type
    if args.family_id.startswith("PTHR"):
        db = "panther"
    elif args.family_id.startswith("PF"):
        db = "pfam"
    else:
        db = "panther"

    # Load family metadata
    metadata = load_family_metadata(args.family_id, args.base_dir)

    # Format subfamily summary
    subfamily_summary = format_subfamily_summary(metadata.get("subfamilies", []))

    # Determine output path
    output_dir = args.base_dir / db / args.family_id
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / f"{args.family_id}-deep-research-{args.provider}.md"

    # Build deep-research-client command
    cmd = [
        "uv",
        "run",
        "deep-research-client",
        "research",
        "--template",
        str(args.template),
        "--var",
        f"family_id={args.family_id}",
        "--var",
        f"family_name={metadata['family_name']}",
        "--var",
        f"interpro_id={metadata['interpro_id']}",
        "--var",
        f"root_node={metadata['root_node']}",
        "--var",
        f"subfamily_count={metadata['subfamily_count']}",
        "--var",
        f"subfamily_summary={subfamily_summary}",
        "--provider",
        args.provider,
        "--output",
        str(output_file),
    ]

    # Add extra args
    cmd.extend(args.extra_args)

    print(f"Running deep research for family {args.family_id}...")
    print(f"Provider: {args.provider}")
    print(f"Output: {output_file}")
    print(f"Command: {' '.join(cmd)}")

    result = subprocess.run(cmd)
    sys.exit(result.returncode)


if __name__ == "__main__":
    main()
