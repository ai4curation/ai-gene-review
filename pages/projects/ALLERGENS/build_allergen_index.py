#!/usr/bin/env python3
"""Build the allergen -> UniProt -> gene-review index for the ALLERGENS project.

The index bridges the one-to-many relationship between an **allergen molecule**
(the WHO/IUIS unit, e.g. "Fel d 1") and the **gene/UniProt entries** that encode it
(e.g. CH1 + CH2). Membership is taken from the cached UniProt records, which carry:

  - the WHO/IUIS allergen name on a ``DE   AltName: Allergen=...`` line, and
  - Allergome cross-references on ``DR   Allergome; <id>; <name>.`` lines, and
  - the ``Allergen`` UniProt keyword (``KW`` lines).

Nothing here calls an external API: it parses the local ``genes/**/<g>-uniprot.txt``
records (already fetched by ``ai-gene-review fetch-gene``) and joins them to the
local ``*-ai-review.yaml`` files. To incorporate the official WHO/IUIS registry,
download its table to ``projects/ALLERGENS/iuis_allergens.tsv`` (columns including
an ``allergen`` name); if present it is merged in to flag registry membership.
This script never fabricates registry data.

Usage:
    uv run python projects/ALLERGENS/build_allergen_index.py \
        -o projects/ALLERGENS/allergen_index.tsv
"""

from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[2]
GENES_DIR = REPO_ROOT / "genes"
ISOALLERGEN_SUFFIX = re.compile(r"\.\d{4}$")  # e.g. "Fel d 1.0101"
CHAIN_SUFFIX = re.compile(r"[ -](?:chain\s*)?[0-9A-Z]$", re.IGNORECASE)  # "Fel d 1-A"


def parse_uniprot(path: Path) -> dict:
    """Extract allergen-relevant fields from a cached UniProt text record.

    Returns a dict with accession, gene name, taxon id, the Allergen keyword flag,
    the ``Allergen=`` name, and Allergome (id, label) cross-references.
    """
    acc = gene = taxon = allergen_name = None
    is_allergen_kw = False
    allergome: list[tuple[str, str]] = []
    for line in path.read_text().splitlines():
        if line.startswith("AC ") and acc is None:
            acc = line.split()[1].rstrip(";")
        elif line.startswith("GN ") and gene is None:
            m = re.search(r"Name=([^;{ ]+)", line)
            if m:
                gene = m.group(1)
        elif line.startswith("OX ") and taxon is None:
            m = re.search(r"NCBI_TaxID=(\d+)", line)
            if m:
                taxon = m.group(1)
        elif line.startswith("DE ") and "Allergen=" in line:
            raw = line.split("Allergen=", 1)[1].strip().rstrip(";")
            allergen_name = re.sub(r"\s*\{ECO:[^}]*\}", "", raw).strip()
        elif line.startswith("KW ") and "Allergen" in line:
            is_allergen_kw = True
        elif line.startswith("DR   Allergome;"):
            parts = [p.strip() for p in line[len("DR   "):].rstrip(".").split(";")]
            # parts == ["Allergome", "<id>", "<label>"]
            if len(parts) >= 3:
                allergome.append((parts[1], parts[2]))
    return {
        "accession": acc,
        "gene": gene,
        "taxon": taxon,
        # Reviewed entries carry the Allergen keyword / "Allergen=" name; unreviewed
        # (TrEMBL) allergens (e.g. Fel d 7, Fel d 8) are identified by an Allergome
        # cross-reference instead.
        "is_allergen": bool(is_allergen_kw or allergen_name or allergome),
        "allergen_name": allergen_name,
        "allergome": allergome,
    }


def molecule_name(rec: dict) -> str:
    """Derive the WHO/IUIS allergen-molecule name (the cohort unit).

    Prefer an Allergome label that is NOT an isoallergen (no ``.NNNN`` suffix);
    otherwise strip a trailing chain designator from the ``Allergen=`` name
    (``Fel d 1-A`` -> ``Fel d 1``).
    """
    molecule_labels = [
        label for _id, label in rec["allergome"] if not ISOALLERGEN_SUFFIX.search(label)
    ]
    if molecule_labels:
        return sorted(molecule_labels, key=len)[0]
    name = rec["allergen_name"] or rec["gene"] or rec["accession"] or "?"
    return CHAIN_SUFFIX.sub("", name).strip()


def allergome_molecule_id(rec: dict) -> str:
    """The Allergome id of the molecule-level (non-isoallergen) cross-reference."""
    for _id, label in rec["allergome"]:
        if not ISOALLERGEN_SUFFIX.search(label):
            return _id
    return ""


def review_stats(review_path: Path) -> dict:
    """Read review status and count core_functions / knowledge_gaps."""
    if not review_path.exists():
        return {"status": "UNREVIEWED", "n_core": 0, "n_gaps": 0}
    data = yaml.safe_load(review_path.read_text()) or {}
    core = data.get("core_functions") or []
    n_gaps = len(data.get("knowledge_gaps") or [])
    for cf in core:
        n_gaps += len(cf.get("knowledge_gaps") or [])
    return {"status": data.get("status", "UNKNOWN"), "n_core": len(core), "n_gaps": n_gaps}


def build_rows() -> list[dict]:
    rows: list[dict] = []
    for uniprot_file in sorted(GENES_DIR.glob("*/*/*-uniprot.txt")):
        rec = parse_uniprot(uniprot_file)
        if not rec["is_allergen"]:
            continue
        gene_dir = uniprot_file.parent
        species = gene_dir.parent.name
        gene = gene_dir.name
        review_path = gene_dir / f"{gene}-ai-review.yaml"
        stats = review_stats(review_path)
        rows.append(
            {
                "allergen_molecule": molecule_name(rec),
                "allergome_id": allergome_molecule_id(rec),
                "source_taxon_id": rec["taxon"] or "",
                "species_code": species,
                "gene_symbol": gene,
                "uniprot": rec["accession"] or "",
                "uniprot_allergen_name": rec["allergen_name"] or "",
                "review_path": str(review_path.relative_to(REPO_ROOT)) if review_path.exists() else "",
                "review_status": stats["status"],
                "n_core_functions": stats["n_core"],
                "n_knowledge_gaps": stats["n_gaps"],
                "function_gap_flagged": "yes" if stats["n_gaps"] else "no",
            }
        )
    rows.sort(key=lambda r: (r["allergen_molecule"], r["gene_symbol"]))
    return rows


FIELDS = [
    "allergen_molecule",
    "allergome_id",
    "source_taxon_id",
    "species_code",
    "gene_symbol",
    "uniprot",
    "uniprot_allergen_name",
    "review_path",
    "review_status",
    "n_core_functions",
    "n_knowledge_gaps",
    "function_gap_flagged",
]


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "-o",
        "--output",
        type=Path,
        default=Path("projects/ALLERGENS/allergen_index.tsv"),
        help="Output TSV path",
    )
    args = ap.parse_args()
    rows = build_rows()
    out = (REPO_ROOT / args.output) if not args.output.is_absolute() else args.output
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=FIELDS, delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)
    molecules = sorted({r["allergen_molecule"] for r in rows})
    print(f"Wrote {len(rows)} allergen gene rows ({len(molecules)} molecules) -> {out}")
    for mol in molecules:
        genes = [r["gene_symbol"] for r in rows if r["allergen_molecule"] == mol]
        print(f"  {mol}: {', '.join(genes)}")


if __name__ == "__main__":
    main()
