#!/usr/bin/env python3
"""Extract suggested fixes for failing supporting_text validations.

Runs the LTV SupportingTextValidator on each failing supporting_text
and reports the best_match and similarity score for semi-automated fixing.

Usage:
    uv run python scripts/extract_supporting_text_fixes.py genes/human/ABL1/ABL1-ai-review.yaml
    uv run python scripts/extract_supporting_text_fixes.py genes/human/*/  # all human genes
"""

import sys
import yaml
from pathlib import Path

from linkml_reference_validator.validation.supporting_text_validator import SupportingTextValidator
from linkml_reference_validator.models import ReferenceValidationConfig


config = ReferenceValidationConfig(
    cache_dir="publications",
    literal_bracket_patterns=[r"[^a-zA-Z\s]"],
)
validator = SupportingTextValidator(config)

SKIP_PREFIXES = {
    "GO_REF", "GO", "Reactome", "UniProt", "UniProtKB",
    "PDB", "EC", "TEMP", "ISBN", "RHEA", "file",
    "curator_inference", "ComplexPortal", "HPA",
    "PROSITE", "CHEBI", "PMC", "CONTACT_INFO",
}


def check_file(filepath: Path):
    try:
        with open(filepath) as f:
            data = yaml.safe_load(f)
    except yaml.YAMLError:
        print(f"{filepath}\t\t\tYAML_ERROR\t0.00\t\t", file=sys.stderr)
        return
    if not data:
        return

    def walk_supported_by(obj, path=""):
        if isinstance(obj, dict):
            if "reference_id" in obj and "supporting_text" in obj:
                ref_id = obj["reference_id"]
                text = obj["supporting_text"]
                prefix = ref_id.split(":")[0] if ":" in ref_id else ref_id
                if prefix not in SKIP_PREFIXES and text:
                    yield path, ref_id, text
            else:
                for k, v in obj.items():
                    yield from walk_supported_by(v, f"{path}.{k}")
        elif isinstance(obj, list):
            for i, item in enumerate(obj):
                yield from walk_supported_by(item, f"{path}[{i}]")

    for path, ref_id, text in walk_supported_by(data):
        result = validator.validate(text, ref_id)
        if result.is_valid:
            continue

        mr = result.match_result
        sim = mr.similarity_score if mr else 0
        best = mr.best_match if mr else None
        fix = mr.suggested_fix if mr else None

        if sim >= 0.7 and best:
            status = "AUTOFIX"
        elif sim >= 0.5 and best:
            status = "REVIEW"
        elif best:
            status = "LOW_SIM"
        else:
            status = "NO_MATCH"

        print(f"{filepath}\t{path}\t{ref_id}\t{status}\t{sim:.2f}\t{text[:100]}\t{best[:100] if best else ''}")


def main():
    paths = [Path(p) for p in sys.argv[1:]]
    files = []
    for p in paths:
        if p.is_dir():
            files.extend(sorted(p.rglob("*-ai-review.yaml")))
        elif p.suffix == ".yaml":
            files.append(p)

    print("file\tpath\tref_id\tstatus\tsimilarity\tsupporting_text\tbest_match")
    for f in files:
        check_file(f)


if __name__ == "__main__":
    main()
