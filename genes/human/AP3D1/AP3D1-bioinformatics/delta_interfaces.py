"""Are the delta-adaptin ARF1 and VAMP7 interfaces family features of PTHR22781?

Three structurally defined, residue-level interfaces have been mapped on HUMAN
AP3D1 (O14617) itself, so their positions need no cross-species inference to be
stated -- only to be tested for conservation:

* ARF1 site 1  F77, M110, L111            (PMID:42139345, PDB 9C5C-related mutants)
* ARF1 site 2  H157, K159, R163, R187     (PMID:42139345)
* VAMP7 hinge  I702, V704, L709, L713     (PMID:22521722, PDB 4AFI, O14617 680-729)

Question: are these delta-specific and family-wide, or do they also appear in the
other adaptor large subunits (which sit in different PANTHER families, PTHR22780
and PTHR11134)?

Method: build one MAFFT alignment over (a) every reviewed member of PTHR22781
listed in the committed InterPro slice and (b) the human large subunits of AP-1,
AP-2, AP-3-beta and AP-4 as out-of-family controls, then read off the column that
each human AP3D1 position occupies.

No result is hardcoded. Sequences are fetched live from UniProt and cached under
cache/.
"""

from __future__ import annotations

import csv
import subprocess
import sys
from pathlib import Path

import requests

HERE = Path(__file__).parent
CACHE = HERE / "cache"
ENTRIES = HERE.parents[3] / "interpro" / "panther" / "PTHR22781" / "PTHR22781-entries.csv"

TARGET = "O14617"

# Out-of-family controls: the large subunits of the other adaptor complexes.
# PANTHER puts alpha/gamma/epsilon in PTHR22780 and the betas in PTHR11134,
# so none of these is in PTHR22781 with AP3D1.
CONTROLS = {
    "O00203": "AP3B1 human beta-3A (PTHR11134)",
    "O43747": "AP1G1 human gamma-1 (PTHR22780)",
    "O95782": "AP2A1 human alpha-1 (PTHR22780)",
    "Q9UPM8": "AP4E1 human epsilon-1 (PTHR22780)",
}

SITES = {
    "ARF1_site1": [(77, "F"), (110, "M"), (111, "L")],
    "ARF1_site2": [(157, "H"), (159, "K"), (163, "R"), (187, "R")],
    "VAMP7_hinge": [(702, "I"), (704, "V"), (709, "L"), (713, "L")],
}


def fetch_fasta(acc: str) -> str:
    CACHE.mkdir(exist_ok=True)
    path = CACHE / f"{acc}.fasta"
    if not path.exists():
        r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
        r.raise_for_status()
        path.write_text(r.text)
    return path.read_text()


def seq_of(fasta: str) -> str:
    return "".join(line.strip() for line in fasta.splitlines() if not line.startswith(">"))


def read_family_members() -> dict[str, str]:
    """Accession -> label, from the committed InterPro family slice."""
    members = {}
    with ENTRIES.open() as fh:
        for row in csv.DictReader(fh):
            members[row["id"]] = f"{row['gene']} {row['source_tax_name']} ({row['subfamily']})"
    return members


def main() -> None:
    if not ENTRIES.exists():
        sys.exit(f"missing family slice {ENTRIES}")
    panel = read_family_members()
    panel.update(CONTROLS)
    if TARGET not in panel:
        sys.exit(f"{TARGET} absent from the family slice; refusing to guess")

    seqs = {acc: seq_of(fetch_fasta(acc)) for acc in panel}

    target_seq = seqs[TARGET]
    assert len(target_seq) == 1153, f"O14617 is {len(target_seq)} aa, expected 1153"
    for site, residues in SITES.items():
        for pos, res in residues:
            got = target_seq[pos - 1]
            assert got == res, f"{site}: O14617 position {pos} is {got}, not {res}"

    fasta_in = CACHE / "panel.fasta"
    fasta_in.write_text("".join(f">{a}\n{s}\n" for a, s in seqs.items()))
    aln_path = CACHE / "panel.aln.fasta"
    if not aln_path.exists():
        out = subprocess.run(
            ["mafft", "--auto", "--anysymbol", str(fasta_in)],
            capture_output=True, text=True, check=True,
        )
        aln_path.write_text(out.stdout)

    aln: dict[str, str] = {}
    acc = None
    for line in aln_path.read_text().splitlines():
        if line.startswith(">"):
            acc = line[1:].strip().split()[0]
            aln[acc] = ""
        elif acc:
            aln[acc] += line.strip()
    widths = {len(v) for v in aln.values()}
    assert len(widths) == 1, f"ragged alignment: {widths}"

    # map each ungapped target position to its alignment column
    col_of: dict[int, int] = {}
    p = 0
    for col, ch in enumerate(aln[TARGET]):
        if ch != "-":
            p += 1
            col_of[p] = col
    assert p == len(target_seq), f"alignment lost residues: {p} vs {len(target_seq)}"

    # ungapped position of each alignment column, per sequence
    native: dict[str, dict[int, int]] = {}
    for a, al in aln.items():
        m = {}
        q = 0
        for col, ch in enumerate(al):
            if ch != "-":
                q += 1
                m[col] = q
        native[a] = m

    rows = []
    in_family = set(read_family_members())
    for site, residues in SITES.items():
        for pos, res in residues:
            col = col_of[pos]
            for a in sorted(aln, key=lambda x: (x not in in_family, x)):
                rows.append({
                    "site": site,
                    "human_position": pos,
                    "human_residue": res,
                    "accession": a,
                    "label": panel[a],
                    "in_PTHR22781": a in in_family,
                    "aligned_residue": aln[a][col],
                    "native_position": native[a].get(col, ""),
                    "identical": aln[a][col] == res,
                })

    out = HERE / "delta_interfaces.tsv"
    with out.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]), delimiter="\t")
        w.writeheader()
        w.writerows(rows)

    print(f"panel: {len(seqs)} sequences ({len(in_family)} PTHR22781 members, {len(CONTROLS)} controls)")
    for a in sorted(seqs, key=lambda x: (x not in in_family, x)):
        print(f"  {a} {len(seqs[a]):5d} aa  {'FAM' if a in in_family else 'CTRL'}  {panel[a]}")
    print()
    for site in SITES:
        sub = [r for r in rows if r["site"] == site]
        n_pos = len({r["human_position"] for r in sub})
        for group, flag in (("PTHR22781", True), ("controls", False)):
            members = sorted({r["accession"] for r in sub if r["in_PTHR22781"] is flag} - {TARGET})
            per = []
            for a in members:
                k = sum(1 for r in sub if r["accession"] == a and r["identical"])
                per.append(f"{a}:{k}/{n_pos}")
            print(f"{site:12s} {group:10s} identity to human at the {n_pos} site positions: {' '.join(per)}")
        print()
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
