"""Utilities for working with PMIDs in YAML files."""

from pathlib import Path
from typing import List, Optional


def mark_invalid_pmids(
    yaml_file: Path, pmids: List[str], output_file: Optional[Path] = None
) -> int:
    """Mark specific PMIDs as invalid in a YAML file.

    This function adds is_invalid: true to references that can't be retrieved,
    so they won't be validated in future runs.

    Args:
        yaml_file: Path to the YAML file to update
        pmids: List of PMID strings (e.g., ["PMID:12345", "34521819"])
        output_file: Optional output path (defaults to input file)

    Returns:
        Number of references marked as invalid
    """
    import yaml

    # Normalize PMIDs
    normalized_pmids = set()
    for pmid in pmids:
        if pmid.startswith("PMID:"):
            normalized_pmids.add(pmid)
            normalized_pmids.add(pmid[5:])  # Also add without prefix
        else:
            normalized_pmids.add(f"PMID:{pmid}")
            normalized_pmids.add(pmid)

    # Load YAML file
    with open(yaml_file, "r") as f:
        data = yaml.safe_load(f)

    marked_count = 0

    # Update references section
    if "references" in data and isinstance(data["references"], list):
        for ref in data["references"]:
            if isinstance(ref, dict) and "id" in ref:
                ref_id = ref["id"]
                # Check if this PMID should be marked invalid
                if ref_id in normalized_pmids or (
                    ref_id.startswith("PMID:") and ref_id[5:] in normalized_pmids
                ):
                    if not ref.get("is_invalid", False):
                        ref["is_invalid"] = True
                        marked_count += 1
                        # Add a note about why it's invalid
                        if "title" in ref and ref["title"] == "TODO: Fetch title":
                            ref["title"] = (
                                "INVALID: Cannot retrieve from PubMed (possibly replaced or retracted)"
                            )

    # Save the updated YAML
    if output_file is None:
        output_file = yaml_file

    with open(output_file, "w") as f:
        yaml.dump(
            data, f, default_flow_style=False, sort_keys=False, allow_unicode=True
        )

    return marked_count
