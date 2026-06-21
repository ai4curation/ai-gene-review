#!/usr/bin/env python3
"""Convert the NCBIFAM->GO SSSOM mapping set into the nested term-tuple form.

Mirrors projects/RHEA/sssom_to_terms.py. The SSSOM file
(``ncbifam2go.sssom.yaml``) uses flat columns (subject_id/subject_label,
predicate_id/predicate_label, object_id/object_label). linkml-term-validator
validates **nested** ``{id, label}`` objects, so this reshapes each row into

    {subject: {id, label}, predicate: {id, label}, object: {id, label}, mapping_justification, comment}

The output (``ncbifam2go.terms.yaml``, class ``NCBIFAMGOMappingSet``) is checked with::

    uv run linkml-term-validator validate-data projects/NCBIFam/ncbifam2go.terms.yaml \
        -s src/ai_gene_review/schema/ncbifam_go_mapping.yaml -t NCBIFAMGOMappingSet \
        --labels -c conf/oak_config.yaml

Only the GO object is ontology-label-validated (the NCBIFAM subject is a curated
family id/label tuple, not bound to an ontology enum). The SSSOM file is the
single source of truth; this nested file is generated.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import yaml

HEADER = (
    "# GENERATED FILE - do not edit by hand.\n"
    "# Source of truth: projects/NCBIFam/ncbifam2go.sssom.yaml\n"
    "# Regenerate: uv run python projects/NCBIFam/sssom_to_terms.py "
    "projects/NCBIFam/ncbifam2go.sssom.yaml -o projects/NCBIFam/ncbifam2go.terms.yaml\n"
    "# Validate:   uv run linkml-term-validator validate-data projects/NCBIFam/ncbifam2go.terms.yaml "
    "-s src/ai_gene_review/schema/ncbifam_go_mapping.yaml -t NCBIFAMGOMappingSet --labels -c conf/oak_config.yaml\n"
)


def sssom_to_terms(sssom: dict) -> dict:
    """Reshape an SSSOM mapping set dict into the nested NCBIFAMGOMappingSet shape."""
    mappings = []
    for m in sssom.get("mappings", []):
        if not str(m.get("object_id", "")).startswith("GO:"):
            continue  # only GO objects are term-validatable
        row = {
            "subject": {"id": m["subject_id"], "label": m["subject_label"]},
            "predicate": {
                "id": m["predicate_id"],
                "label": m.get("predicate_label", ""),
            },
            "object": {"id": m["object_id"], "label": m["object_label"]},
            "mapping_justification": m["mapping_justification"],
        }
        if m.get("comment"):
            row["comment"] = m["comment"]
        mappings.append(row)
    return {"mappings": mappings}


def render(terms: dict) -> str:
    body = yaml.safe_dump(terms, sort_keys=False, default_flow_style=False, width=100)
    return HEADER + body


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("sssom", type=Path, help="Input SSSOM mapping file")
    ap.add_argument(
        "-o", "--output", type=Path, required=True, help="Output nested terms YAML"
    )
    args = ap.parse_args(argv)

    sssom = yaml.safe_load(args.sssom.read_text())
    terms = sssom_to_terms(sssom)
    args.output.write_text(render(terms))
    print(f"# wrote {len(terms['mappings'])} mappings -> {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
