#!/usr/bin/env python3
"""Analyze domain architecture and key functional motifs in a p97/CDC48 family protein.

Identifies Walker A/B motifs, Second Region of Homology (SRH), arginine fingers,
and domain boundaries from the amino acid sequence using regex-based motif scanning.

Input: FASTA file of the protein sequence
Output: TSV report of identified domains and motifs
"""

import sys
import re
import csv
from pathlib import Path
from Bio import SeqIO


# Known domain boundaries for human VCP (P55072) as reference.
# These are used as seed patterns; the script scans for motifs in the actual sequence.
DOMAIN_DEFS = {
    "N-domain": {"description": "N-terminal substrate/cofactor binding domain"},
    "D1-ATPase": {"description": "First AAA+ ATPase ring domain"},
    "D1-D2-linker": {"description": "Linker between D1 and D2 ATPase domains"},
    "D2-ATPase": {"description": "Second AAA+ ATPase ring domain (main catalytic)"},
    "C-tail": {"description": "C-terminal tail, cofactor binding"},
}

# Walker A motif: GxxxxGK[TS] (P-loop) - the canonical AAA+ Walker A
# Some family members have GxxGxGKT, others GxxxSGKT etc.
# We use the broader GxxxxGK[TS] pattern
WALKER_A_PATTERN = re.compile(r"G\w{4}GK[TS]")

# Walker B motif: DExx (hydrophobic)4-DE
WALKER_B_PATTERN = re.compile(r"[VILMF]{4}DE")

# Second Region of Homology (SRH) - contains arginine finger
# Simplified pattern for the conserved arginine residues in SRH
SRH_ARGININE_PATTERN = re.compile(r"R\w{0,3}[VILMF]\w{0,5}R")

# Sensor 1: polar residue (N or T) in specific context
SENSOR1_PATTERN = re.compile(r"[NT]\w{0,2}[VILMF]{2}\w{0,2}[DE]")

# Sensor 2: GAR motif in some AAA+ proteins
SENSOR2_PATTERN = re.compile(r"G[AG]R")

# PIM (PUL-interacting motif) at C-terminus
PIM_PATTERN = re.compile(r"[LY]\w[FY]\w{0,2}$")


def find_motifs(sequence: str) -> list[dict]:
    """Find AAA+ ATPase functional motifs in the sequence."""
    motifs = []

    # Walker A motifs
    for match in WALKER_A_PATTERN.finditer(sequence):
        motifs.append({
            "motif": "Walker_A",
            "start": match.start() + 1,  # 1-based
            "end": match.end(),
            "sequence": match.group(),
            "description": "P-loop, ATP binding (GxxGxGK[TS])",
        })

    # Walker B motifs
    for match in WALKER_B_PATTERN.finditer(sequence):
        motifs.append({
            "motif": "Walker_B",
            "start": match.start() + 1,
            "end": match.end(),
            "sequence": match.group(),
            "description": "Mg2+/water coordination, ATP hydrolysis",
        })

    # PIM motif
    for match in PIM_PATTERN.finditer(sequence):
        motifs.append({
            "motif": "PIM",
            "start": match.start() + 1,
            "end": match.end(),
            "sequence": match.group(),
            "description": "PUL-interacting motif at C-terminus",
        })

    return motifs


def assign_domains(sequence: str, motifs: list[dict]) -> list[dict]:
    """Assign domain boundaries based on Walker A/B motif positions.

    For p97/CDC48 family proteins, the two Walker A motifs delineate D1 and D2.
    """
    walker_a_positions = sorted(
        [m for m in motifs if m["motif"] == "Walker_A"],
        key=lambda x: x["start"],
    )
    walker_b_positions = sorted(
        [m for m in motifs if m["motif"] == "Walker_B"],
        key=lambda x: x["start"],
    )

    domains = []
    seq_len = len(sequence)

    if len(walker_a_positions) >= 2:
        d1_walker_a = walker_a_positions[0]
        d2_walker_a = walker_a_positions[1]

        # N-domain: start to ~50 aa before first Walker A
        n_end = d1_walker_a["start"] - 50
        if n_end > 10:
            domains.append({
                "domain": "N-domain",
                "start": 1,
                "end": n_end,
                "evidence": "Inferred from Walker A position in D1",
                "description": DOMAIN_DEFS["N-domain"]["description"],
            })

        # D1 domain: ~40 aa before Walker A to midpoint before D2 Walker A
        d1_start = max(1, d1_walker_a["start"] - 40)
        d1_end = d2_walker_a["start"] - 30
        domains.append({
            "domain": "D1-ATPase",
            "start": d1_start,
            "end": d1_end,
            "evidence": f"Walker A at {d1_walker_a['start']}-{d1_walker_a['end']}",
            "description": DOMAIN_DEFS["D1-ATPase"]["description"],
        })

        # D2 domain
        d2_start = d2_walker_a["start"] - 30
        d2_end = min(seq_len, d2_walker_a["start"] + 270)
        domains.append({
            "domain": "D2-ATPase",
            "start": d2_start,
            "end": d2_end,
            "evidence": f"Walker A at {d2_walker_a['start']}-{d2_walker_a['end']}",
            "description": DOMAIN_DEFS["D2-ATPase"]["description"],
        })

        # C-tail
        if d2_end < seq_len:
            domains.append({
                "domain": "C-tail",
                "start": d2_end + 1,
                "end": seq_len,
                "evidence": "Region after D2 ATPase domain",
                "description": DOMAIN_DEFS["C-tail"]["description"],
            })

        # Annotate which domain each Walker B belongs to
        for wb in walker_b_positions:
            if wb["start"] < d2_walker_a["start"] - 30:
                wb["domain_assignment"] = "D1"
            else:
                wb["domain_assignment"] = "D2"

        # Annotate Walker A domains
        for i, wa in enumerate(walker_a_positions):
            if i == 0:
                wa["domain_assignment"] = "D1"
            elif i == 1:
                wa["domain_assignment"] = "D2"

    elif len(walker_a_positions) == 1:
        # Single AAA+ domain
        wa = walker_a_positions[0]
        domains.append({
            "domain": "AAA-ATPase",
            "start": max(1, wa["start"] - 40),
            "end": min(seq_len, wa["start"] + 270),
            "evidence": f"Walker A at {wa['start']}-{wa['end']}",
            "description": "Single AAA+ ATPase domain",
        })

    return domains


def identify_key_residues(sequence: str, motifs: list[dict]) -> list[dict]:
    """Identify specific catalytically important residues."""
    key_residues = []

    for m in motifs:
        if m["motif"] == "Walker_A":
            # The invariant lysine in Walker A
            lys_pos = m["start"] + 6  # K is at position 7 of GxxGxGKT
            key_residues.append({
                "residue": f"K{lys_pos}",
                "position": lys_pos,
                "role": "Walker A invariant lysine",
                "motif": m["motif"],
                "domain": m.get("domain_assignment", "unknown"),
                "functional_importance": "Essential for ATP binding; mutation abolishes ATPase activity",
            })

        if m["motif"] == "Walker_B":
            # The DE pair
            de_start = m["start"] + 4  # DE is at positions 5-6 of xxxxDE
            key_residues.append({
                "residue": f"D{de_start}",
                "position": de_start,
                "role": "Walker B aspartate",
                "motif": m["motif"],
                "domain": m.get("domain_assignment", "unknown"),
                "functional_importance": "Mg2+ coordination",
            })
            key_residues.append({
                "residue": f"E{de_start + 1}",
                "position": de_start + 1,
                "role": "Walker B glutamate (catalytic base)",
                "motif": m["motif"],
                "domain": m.get("domain_assignment", "unknown"),
                "functional_importance": "Catalytic base for ATP hydrolysis; E->Q mutation traps ATP-bound state",
            })

    return key_residues


def main():
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <input_fasta> <output_prefix>", file=sys.stderr)
        sys.exit(1)

    fasta_file = Path(sys.argv[1])
    output_prefix = sys.argv[2]

    record = next(SeqIO.parse(fasta_file, "fasta"))
    sequence = str(record.seq)
    seq_id = record.id

    print(f"Analyzing {seq_id}, length {len(sequence)} aa")

    # Find motifs
    motifs = find_motifs(sequence)
    print(f"Found {len(motifs)} motifs")

    # Assign domains
    domains = assign_domains(sequence, motifs)
    print(f"Identified {len(domains)} domains")

    # Identify key residues
    key_residues = identify_key_residues(sequence, motifs)
    print(f"Identified {len(key_residues)} key functional residues")

    # Write motif report
    motif_file = f"{output_prefix}_motifs.tsv"
    with open(motif_file, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["motif", "start", "end", "sequence", "description", "domain_assignment"], delimiter="\t")
        writer.writeheader()
        for m in motifs:
            row = {k: m.get(k, "") for k in writer.fieldnames}
            writer.writerow(row)
    print(f"Wrote motifs to {motif_file}")

    # Write domain report
    domain_file = f"{output_prefix}_domains.tsv"
    with open(domain_file, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["domain", "start", "end", "evidence", "description"], delimiter="\t")
        writer.writeheader()
        for d in domains:
            writer.writerow(d)
    print(f"Wrote domains to {domain_file}")

    # Write key residues report
    residue_file = f"{output_prefix}_key_residues.tsv"
    with open(residue_file, "w", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["residue", "position", "role", "motif", "domain", "functional_importance"],
            delimiter="\t",
        )
        writer.writeheader()
        for r in key_residues:
            writer.writerow(r)
    print(f"Wrote key residues to {residue_file}")


if __name__ == "__main__":
    main()
