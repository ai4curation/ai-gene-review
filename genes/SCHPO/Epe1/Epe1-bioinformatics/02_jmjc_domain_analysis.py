#!/usr/bin/env python3
"""
JmjC domain and Fe(II)-ligand analysis for Epe1 and active JmjC demethylases.

Domain boundaries and Fe(II) ligands come from UniProt feature records
(FT DOMAIN "JmjC" and FT BINDING with an iron ligand), not from a sequence
motif. For Epe1 the source is the gene folder's own UniProt flat file
(../Epe1-uniprot.txt); comparators use the UniProt JSON saved by
01_fetch_sequences.py.

A bare H.[DE] motif scan is reported only as a cross-check: each hit is
labelled with whether its His is an annotated Fe(II) ligand, because such a
scan matches any His-X-Asp/Glu string and does not by itself locate the site.
"""

import re
from pathlib import Path

from uniprot_features import ligand_residues, parse_uniprot_json, parse_uniprot_txt

EPE1_TXT = Path(__file__).parent.parent / "Epe1-uniprot.txt"


def load_records() -> dict:
    """Epe1 from its flat file; comparators from data/kdm*.json."""
    records = {"Epe1": parse_uniprot_txt(EPE1_TXT)}
    for path in sorted(Path("data").glob("kdm*.json")):
        rec = parse_uniprot_json(path)
        records[rec["entry_name"] or path.stem.upper()] = rec
    return records


def motif_hits(rec: dict) -> list:
    """H.[DE] hits inside the annotated JmjC domain, 1-based position of the His,
    each labelled with whether that His is an annotated Fe(II) ligand."""
    start, end = rec["jmjc"]
    domain = rec["sequence"][start - 1:end]
    hits = []
    for m in re.finditer(r"H.[DE]", domain):
        pos = start + m.start()
        hits.append((pos, m.group(), pos in rec["fe_ligands"]))
    return hits


def main():
    print("=" * 60)
    print("JmjC Domain and Fe(II)-Ligand Analysis (from UniProt features)")
    print("=" * 60)

    records = load_records()
    lines = ["JmjC Domain Analysis Results", "=" * 60, "",
             "Source: UniProt FT DOMAIN (JmjC) and FT BINDING (Fe ligand) features.",
             "Epe1 from ../Epe1-uniprot.txt; comparators from data/kdm*.json.", ""]

    header = f"{'Protein':<14} {'Accession':<10} {'JmjC':<12} {'Fe ligands (UniProt)':<24} {'n'}"
    lines += [header, "-" * len(header)]
    for name, rec in records.items():
        if rec["jmjc"] is None:
            lines.append(f"{name:<14} {rec['accession']:<10} no JmjC domain feature")
            continue
        dom = f"{rec['jmjc'][0]}-{rec['jmjc'][1]}"
        ligs = ", ".join(ligand_residues(rec)) or "none"
        lines.append(f"{name:<14} {rec['accession']:<10} {dom:<12} {ligs:<24} {len(rec['fe_ligands'])}")

    epe1 = records["Epe1"]
    comparators = {k: v for k, v in records.items() if k != "Epe1" and v["jmjc"]}
    lines += ["", "Epe1 details:"]
    lines.append(f"- JmjC domain (FT DOMAIN): {epe1['jmjc'][0]}-{epe1['jmjc'][1]}")
    lines.append(f"- Fe(II) ligands (FT BINDING, Fe): {', '.join(ligand_residues(epe1))}")
    for pos, expected, found in epe1["caution_positions"]:
        actual = epe1["sequence"][pos - 1]
        lines.append(
            f"- UniProt CC CAUTION: catalytic {expected} at {pos} replaced by {found}; "
            f"residue in sequence at {pos}: {actual}"
        )
    for pos, lig in epe1["binding"]:
        if pos not in epe1["fe_ligands"]:
            lines.append(f"- Other FT BINDING: {epe1['sequence'][pos - 1]}{pos} (ligand: {lig})")
    for pos, note in epe1["mutagen"]:
        lines.append(f"- FT MUTAGEN: {epe1['sequence'][pos - 1]}{pos} ({note})")

    counts = sorted({len(v["fe_ligands"]) for v in comparators.values()})
    if comparators:
        lines += ["", "Comparison (computed):",
                  f"- Annotated Fe(II) ligands per comparator JmjC domain: {counts}",
                  f"- Annotated Fe(II) ligands in Epe1: {len(epe1['fe_ligands'])}"]
        if len(epe1["fe_ligands"]) < min(counts):
            lines.append("- Epe1 has fewer annotated Fe(II) ligands than every comparator.")

    lines += ["", "H.[DE] motif scan inside each JmjC domain (cross-check only):"]
    for name, rec in records.items():
        if rec["jmjc"] is None:
            continue
        hits = motif_hits(rec)
        desc = "; ".join(
            f"{motif}@{pos}{' (annotated Fe ligand)' if is_fe else ' (not an annotated Fe ligand)'}"
            for pos, motif, is_fe in hits
        ) or "no hits"
        lines.append(f"- {name}: {desc}")

    text = "\n".join(lines) + "\n"
    print(text)
    out = Path("results") / "jmjc_domain_analysis.txt"
    out.parent.mkdir(exist_ok=True)
    out.write_text(text, encoding="utf-8")
    print(f"✓ Results saved to: {out}")


if __name__ == "__main__":
    main()
