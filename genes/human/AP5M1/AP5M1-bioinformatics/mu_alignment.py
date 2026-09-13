"""Map the mu2 cargo pocket, and two AP5M1 residues of interest, across the mu family.

Inputs
  mu2_cargo_pocket.tsv   (from mu2_cargo_pocket.py; derived from PDB 1BXX)
  UniProt sequences, fetched live

Method
  MAFFT L-INS-i over the five human AP mu subunits plus the mouse and Arabidopsis
  AP5M1 orthologues (both are PTHR16082 members, per
  interpro/panther/PTHR16082/PTHR16082-entries.csv).  Positions are reported in
  each protein's own numbering, never as alignment columns.

Questions
  1. Does AP5M1 retain the mu2 YxxPhi-binding residues?
  2. Is AP5M1 Tyr313 -- the only missense allele among the AP-5 macular dystrophy
     variants (PMID:40081374) -- conserved across the paralogues, as that paper says?
  3. Are the caspase-3 sites reported for MUDENG (D276, D290; PMID:23665015)
     aspartates in the canonical Q9H0R1 sequence?

Writes mu_alignment.fasta and mu_cargo_pocket_mapping.tsv.
"""

from __future__ import annotations

import csv
import pathlib
import subprocess

from common import uniprot_record

HERE = pathlib.Path(__file__).parent

# Human AP mu subunits; mouse and Arabidopsis mu5 as PTHR16082 out-species.
ACCESSIONS = ["Q96CW1", "Q9BXS5", "Q9Y2T2", "O00189", "Q9H0R1", "Q8BJ63", "Q8W0Z6"]
MU2 = "Q96CW1"
MU5 = "Q9H0R1"


def align(records: dict[str, dict]) -> dict[str, str]:
    fasta = HERE / "mu_family.fasta"
    with fasta.open("w") as fh:
        for acc, rec in records.items():
            fh.write(f">{acc}\n{rec['sequence']}\n")
    out = subprocess.run(
        ["mafft", "--localpair", "--maxiterate", "1000", "--quiet", str(fasta)],
        check=True, capture_output=True, text=True,
    )
    aligned_path = HERE / "mu_alignment.fasta"
    aligned_path.write_text(out.stdout)
    aln: dict[str, list[str]] = {}
    name = None
    for line in out.stdout.splitlines():
        if line.startswith(">"):
            name = line[1:].strip()
            aln[name] = []
        elif name:
            aln[name].append(line.strip())
    seqs = {k: "".join(v).upper() for k, v in aln.items()}
    lengths = {len(v) for v in seqs.values()}
    if len(lengths) != 1:
        raise RuntimeError(f"MAFFT returned ragged alignment: {lengths}")
    for acc, rec in records.items():
        if seqs[acc].replace("-", "") != rec["sequence"]:
            raise RuntimeError(f"aligned sequence for {acc} does not degap to the UniProt sequence")
    return seqs


def column_index(aligned: str, position: int) -> int:
    """Alignment column (0-based) holding 1-based ungapped `position`."""
    seen = 0
    for col, ch in enumerate(aligned):
        if ch != "-":
            seen += 1
            if seen == position:
                return col
    raise IndexError(f"position {position} beyond sequence of length {seen}")


def residue_at(aligned: str, col: int) -> tuple[str, int | None]:
    """(residue, 1-based ungapped position) of alignment column `col`."""
    ch = aligned[col]
    if ch == "-":
        return "-", None
    pos = sum(1 for c in aligned[: col + 1] if c != "-")
    return ch, pos


def pct_identity(a: str, b: str) -> float:
    pairs = [(x, y) for x, y in zip(a, b) if x != "-" and y != "-"]
    if not pairs:
        return 0.0
    return 100.0 * sum(1 for x, y in pairs if x == y) / len(pairs)


def main() -> None:
    records = {acc: uniprot_record(acc) for acc in ACCESSIONS}
    for acc, r in records.items():
        print(f"{acc} {r['entry_name']:<14} {r['gene']:<7} {r['length']:>4} aa  sv{r['sequence_version']}  {r['organism']}")

    aln = align(records)
    print(f"\nMAFFT L-INS-i alignment: {len(next(iter(aln.values())))} columns")
    print("\npairwise %identity matrix (ungapped columns only):")
    print("         " + "".join(f"{records[a]['gene'][:7]:>9}" for a in ACCESSIONS))
    for a in ACCESSIONS:
        cells = "".join(f"{pct_identity(aln[a], aln[b]):>9.1f}" for b in ACCESSIONS)
        print(f"{records[a]['gene'][:7]:<9}{cells}")

    others = [a for a in ACCESSIONS if a != MU2]
    keys = {a: f"{records[a]['gene']}_{a}" for a in ACCESSIONS}

    pocket = list(csv.DictReader((HERE / "mu2_cargo_pocket.tsv").open(), delimiter="\t"))
    print(f"\n{len(pocket)} mu2 cargo-pocket residues mapped across the family:")
    rows = []
    for p in pocket:
        pos = int(p["mu2_position"])
        aa = p["mu2_residue"]
        if records[MU2]["sequence"][pos - 1] != aa:
            raise RuntimeError(f"{MU2} position {pos} is {records[MU2]['sequence'][pos-1]}, not {aa}")
        col = column_index(aln[MU2], pos)
        row = {"mu2_position": pos, "mu2_residue": aa, "peptide_contacts": p["peptide_contacts"]}
        for acc in ACCESSIONS:
            res, rpos = residue_at(aln[acc], col)
            row[keys[acc]] = f"{res}{rpos}" if rpos else "gap"
        rows.append(row)

    out = HERE / "mu_cargo_pocket_mapping.tsv"
    with out.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]), delimiter="\t")
        w.writeheader()
        w.writerows(rows)

    header = f"{'mu2':>7}  " + "  ".join(f"{records[a]['gene']:>9}" for a in others)
    print(f"{header}   peptide contacts")
    identical = 0
    for row in rows:
        cells = "  ".join(f"{row[keys[a]]:>9}" for a in others)
        mu5_cell = row[keys[MU5]]
        same = mu5_cell.startswith(row["mu2_residue"]) and mu5_cell != "gap"
        identical += same
        print(f"{row['mu2_residue']}{row['mu2_position']:>6}  {cells}   {row['peptide_contacts']}"
              f"{'   <-- identical in mu5' if same else ''}")
    print(f"\nAP5M1 retains {identical}/{len(rows)} of the mu2 cargo-pocket residues "
          f"({100.0*identical/len(rows):.0f}%)")
    for acc in ACCESSIONS:
        if acc in (MU2, MU5):
            continue
        n = sum(1 for row in rows
                if row[keys[acc]].startswith(row["mu2_residue"])
                and row[keys[acc]] != "gap")
        print(f"  ({records[acc]['gene']:<7} retains {n}/{len(rows)})")

    # Q2: AP5M1 Tyr313 across the paralogues.
    print("\nAP5M1 Tyr313 (PMID:40081374 missense allele c.938A>G p.Tyr313Cys):")
    mu5_seq = records[MU5]["sequence"]
    if mu5_seq[312] != "Y":
        raise RuntimeError(f"Q9H0R1 position 313 is {mu5_seq[312]}, not Y")
    col = column_index(aln[MU5], 313)
    for acc in ACCESSIONS:
        res, rpos = residue_at(aln[acc], col)
        print(f"  {records[acc]['gene']:<7} {acc}  {res}{rpos if rpos else ''}")

    # Q3: the reported caspase-3 sites.
    print("\nMUDENG caspase-3 sites reported in PMID:23665015:")
    for pos in (276, 290):
        print(f"  Q9H0R1 {pos}: {mu5_seq[pos - 1]}")
    print(f"  MHD (UniProt DOMAIN 206-476) contains both: {206 <= 276 <= 476 and 206 <= 290 <= 476}")


if __name__ == "__main__":
    main()
