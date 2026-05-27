#!/usr/bin/env python3
"""Diagnose and report malformed reference_id values in gene review YAML files.

Generates a TSV report of all non-standard reference IDs with suggested fixes.

Usage:
    uv run python scripts/diagnose_malformed_refs.py
"""

import re
import sys
from pathlib import Path

import yaml


VALID_PREFIXES = {
    "PMID", "DOI", "GO_REF", "Reactome", "UniProtKB", "UniProt",
    "PDB", "EC", "TEMP", "ISBN", "RHEA", "UniRule", "ARBA",
    "InterPro", "file", "ComplexPortal", "HPA",
}

SKIP_FIELDS = {"source_reference_id", "original_reference_id"}


def classify_ref(ref_id: str, filepath: Path) -> tuple[str, str]:
    """Classify a reference ID and suggest a fix.

    Returns (category, suggested_fix).
    """
    if not ref_id or not ref_id.strip():
        return "empty", "REMOVE"

    ref_id = ref_id.strip()

    # Check if already valid
    prefix = ref_id.split(":")[0] if ":" in ref_id else ""
    if prefix in VALID_PREFIXES:
        return "valid", ""

    # Lowercase doi:
    if ref_id.startswith("doi:"):
        return "lowercase_doi", ref_id.replace("doi:", "DOI:", 1)

    # Deep research file references
    if "deep-research" in ref_id.lower() or "deep_research" in ref_id.lower():
        # Try to find the actual file
        gene_dir = filepath.parent
        candidates = list(gene_dir.glob("*deep-research*")) + list(gene_dir.glob("*deep_research*"))
        if candidates:
            # Build file: reference relative to genes/
            genes_root = Path("genes")
            for p in filepath.parents:
                if p.name == "genes":
                    genes_root = p
                    break
            rel = candidates[0].relative_to(genes_root)
            return "missing_file_prefix_dr", f"file:{rel}"
        return "missing_file_prefix_dr", f"LOOKUP_NEEDED:{ref_id}"

    # Data files (.tsv, .txt, .md)
    if ref_id.endswith((".tsv", ".txt", ".md")):
        gene_dir = filepath.parent
        candidate = gene_dir / ref_id
        if candidate.exists():
            genes_root = Path("genes")
            for p in filepath.parents:
                if p.name == "genes":
                    genes_root = p
                    break
            rel = candidate.relative_to(genes_root)
            return "missing_file_prefix_data", f"file:{rel}"
        # Try without extension variations
        return "missing_file_prefix_data", f"LOOKUP_NEEDED:{ref_id}"

    # Notes files
    if "-notes" in ref_id:
        gene_dir = filepath.parent
        candidate = gene_dir / ref_id
        if not candidate.exists():
            candidate = gene_dir / (ref_id + ".md")
        if candidate.exists():
            genes_root = Path("genes")
            for p in filepath.parents:
                if p.name == "genes":
                    genes_root = p
                    break
            rel = candidate.relative_to(genes_root)
            return "missing_file_prefix_notes", f"file:{rel}"
        return "missing_file_prefix_notes", f"LOOKUP_NEEDED:{ref_id}"

    # Bare UniProt accession (6-char alphanumeric)
    if re.match(r"^[A-Z][0-9][A-Z0-9]{3}[0-9]$", ref_id):
        return "bare_uniprot", f"UniProtKB:{ref_id}"

    # Long UniProt accession (10-char)
    if re.match(r"^[A-Z][0-9][A-Z0-9]{3}[0-9]{5}$", ref_id):
        return "bare_uniprot", f"UniProtKB:{ref_id}"

    # Free-text citation (lowercase word + year)
    if re.match(r"^[a-z].*\d{4}", ref_id):
        return "freetext_citation", f"LOOKUP_NEEDED:{ref_id}"

    # Generic "deep-research" or "Deep research"
    if ref_id.lower().replace(" ", "").replace("-", "") in ("deepresearch",):
        return "generic_deep_research", "REMOVE"

    # Falcon/research references
    if "falcon" in ref_id.lower() or "research" in ref_id.lower():
        gene_dir = filepath.parent
        candidates = list(gene_dir.glob(f"*{ref_id}*")) + list(gene_dir.glob("*deep-research*"))
        if candidates:
            genes_root = Path("genes")
            for p in filepath.parents:
                if p.name == "genes":
                    genes_root = p
                    break
            rel = candidates[0].relative_to(genes_root)
            return "missing_file_prefix_research", f"file:{rel}"
        return "missing_file_prefix_research", f"LOOKUP_NEEDED:{ref_id}"

    # curator_inference
    if ref_id == "curator_inference":
        return "curator_inference", "SKIP_PREFIX_NEEDED"

    return "unknown", f"MANUAL_REVIEW:{ref_id}"


def find_reference_ids(data, path=""):
    """Recursively find all reference_id values."""
    results = []
    if isinstance(data, dict):
        for key, val in data.items():
            if key in SKIP_FIELDS:
                continue
            if key == "reference_id" and isinstance(val, str):
                results.append((path + "." + key, val))
            else:
                results.extend(find_reference_ids(val, path + "." + key))
    elif isinstance(data, list):
        for i, item in enumerate(data):
            results.extend(find_reference_ids(item, path + f"[{i}]"))
    return results


def main():
    genes_dir = Path("genes")
    review_files = sorted(genes_dir.rglob("*-ai-review.yaml"))

    print("file\tpath\tref_id\tcategory\tsuggested_fix")

    counts = {}
    for filepath in review_files:
        try:
            with open(filepath) as f:
                data = yaml.safe_load(f)
        except yaml.YAMLError:
            continue

        if not data:
            continue

        for path, ref_id in find_reference_ids(data):
            cat, fix = classify_ref(ref_id, filepath)
            if cat == "valid":
                continue
            counts[cat] = counts.get(cat, 0) + 1
            print(f"{filepath}\t{path}\t{ref_id}\t{cat}\t{fix}")

    print("\n# Summary", file=sys.stderr)
    for cat, count in sorted(counts.items(), key=lambda x: -x[1]):
        print(f"#   {count:4d}  {cat}", file=sys.stderr)
    print(f"# Total: {sum(counts.values())}", file=sys.stderr)


if __name__ == "__main__":
    main()
