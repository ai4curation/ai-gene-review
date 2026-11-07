#!/usr/bin/env python3
"""Generate Boltz-2 YAML input files for ranking candidate enzyme substrates.

For one protein sequence and a panel of candidate substrates (name + SMILES),
emit one Boltz-2 prediction YAML per candidate, each requesting an affinity
prediction for the ligand. Run the resulting YAMLs with `boltz predict` on a
GPU, then score them with `rank_affinity.py`.

This script does NOT run Boltz-2 (which requires a GPU); it only prepares inputs.

Input panel format (TSV or CSV), one candidate per row:
    name<TAB>smiles
    # lines starting with '#' are ignored
Include the GO-annotated substrate plus plausible alternatives and 1-2 decoys
(molecules that should NOT bind) as negative controls.

Example:
    python generate_inputs.py \
        --protein-id ENZ \
        --sequence-file enzyme.fasta \
        --panel substrates.tsv \
        --outdir boltz_inputs
"""
from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path


def read_sequence(path: Path) -> str:
    """Read a protein sequence from a FASTA file or a plain-text sequence file."""
    text = path.read_text().strip()
    if text.startswith(">"):
        lines = [ln.strip() for ln in text.splitlines() if not ln.startswith(">")]
        seq = "".join(lines)
    else:
        seq = "".join(text.split())
    seq = seq.upper()
    if not re.fullmatch(r"[ACDEFGHIKLMNPQRSTVWYXBZUO]+", seq):
        raise ValueError(f"{path} does not look like a protein sequence")
    return seq


def read_panel(path: Path) -> list[tuple[str, str]]:
    """Read (name, smiles) rows from a TSV/CSV panel, skipping comments/blank lines."""
    delim = "\t" if path.suffix.lower() in {".tsv", ".tab"} else ","
    rows: list[tuple[str, str]] = []
    with path.open() as fh:
        for raw in fh:
            if not raw.strip() or raw.lstrip().startswith("#"):
                continue
            parts = next(csv.reader([raw], delimiter=delim))
            if len(parts) < 2:
                raise ValueError(f"Panel row needs name and SMILES: {raw!r}")
            name, smiles = parts[0].strip(), parts[1].strip()
            rows.append((name, smiles))
    if not rows:
        raise ValueError(f"No candidates found in {path}")
    return rows


def safe_id(name: str) -> str:
    """Make a filesystem/YAML-safe identifier from a candidate name."""
    return re.sub(r"[^A-Za-z0-9_]+", "_", name).strip("_") or "candidate"


def yaml_for(protein_id: str, sequence: str, ligand_id: str, smiles: str,
             use_msa_server: bool) -> str:
    """Build a Boltz-2 YAML string for one protein+ligand complex with affinity.

    Schema per Boltz docs: sequences[].protein / sequences[].ligand (smiles),
    and a top-level properties[].affinity.binder pointing at the ligand chain id.
    """
    msa_line = "" if use_msa_server else "      msa: empty\n"
    # SMILES is single-quoted; escape any embedded single quotes per YAML rules.
    smiles_q = smiles.replace("'", "''")
    return (
        "version: 1\n"
        "sequences:\n"
        "  - protein:\n"
        f"      id: {protein_id}\n"
        f"      sequence: {sequence}\n"
        f"{msa_line}"
        "  - ligand:\n"
        f"      id: {ligand_id}\n"
        f"      smiles: '{smiles_q}'\n"
        "properties:\n"
        "  - affinity:\n"
        f"      binder: {ligand_id}\n"
    )


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--protein-id", default="A", help="Chain id for the protein (default: A)")
    ap.add_argument("--sequence-file", required=True, type=Path,
                    help="FASTA or plain-text protein sequence")
    ap.add_argument("--panel", required=True, type=Path,
                    help="TSV/CSV of candidate substrates: name,smiles")
    ap.add_argument("--ligand-id", default="L", help="Chain id for the ligand (default: L)")
    ap.add_argument("--outdir", required=True, type=Path, help="Directory for generated YAMLs")
    ap.add_argument("--no-msa-server", action="store_true",
                    help="Use single-sequence mode (msa: empty) instead of --use_msa_server")
    args = ap.parse_args()

    sequence = read_sequence(args.sequence_file)
    panel = read_panel(args.panel)
    args.outdir.mkdir(parents=True, exist_ok=True)

    written = []
    for name, smiles in panel:
        stem = safe_id(name)
        out = args.outdir / f"{stem}.yaml"
        out.write_text(yaml_for(args.protein_id, sequence, args.ligand_id, smiles,
                                use_msa_server=not args.no_msa_server))
        written.append(out)

    print(f"Wrote {len(written)} Boltz-2 input(s) to {args.outdir}/")
    print("\nNext (on a GPU machine):")
    msa_flag = "" if args.no_msa_server else " --use_msa_server"
    print(f"  boltz predict {args.outdir}{msa_flag} --out_dir boltz_out")
    print("  python rank_affinity.py --results boltz_out")


if __name__ == "__main__":
    main()
