#!/usr/bin/env python3
"""Analyze cofactor binding interfaces on VCP/p97.

Maps known cofactor binding sites from UniProt annotations (mutagenesis and interaction
data) to the domain architecture. Identifies which interfaces are affected by disease
mutations.

Input: UniProt flat file, domain TSV, disease mutation TSV
Output: Cofactor interface report
"""

import sys
import re
import csv
from pathlib import Path


# Known VCP cofactor binding interfaces from structural studies
# These are recognized from UniProt annotations and literature
KNOWN_INTERFACES = {
    "NPLOC4/UFD1": {
        "description": "UFD1-NPLOC4 (UN) heterodimer binding site on N-domain",
        "key_residues_regex": r"NPLOC4|UFD1",
        "domain": "N-domain",
        "function": "Recruits VCP to ubiquitinated ERAD substrates",
    },
    "DERL1": {
        "description": "Derlin-1 binding site on N-domain",
        "key_residues_regex": r"DERL1",
        "domain": "N-domain",
        "function": "ER membrane retrotranslocation channel interaction",
    },
    "UBX-domain": {
        "description": "UBX/UBX-like domain cofactor binding",
        "key_residues_regex": r"UBXN|UBX",
        "domain": "C-tail",
        "function": "Recruits VCP to diverse cellular pathways",
    },
    "PIM-motif": {
        "description": "PUL-interacting motif at C-terminus (aa 802-806)",
        "key_residues_regex": r"PIM",
        "domain": "C-tail",
        "function": "Binding to PUL domain-containing cofactors (PLAA/UBXN6)",
    },
}


def parse_mutagenesis(uniprot_file: Path) -> list[dict]:
    """Parse FT MUTAGEN entries from UniProt to identify interaction sites."""
    mutagenesis = []
    current = None

    with open(uniprot_file) as f:
        for line in f:
            if line.startswith("FT   MUTAGEN"):
                pos_str = line[21:].strip()
                pos_match = re.match(r"(\d+)(?:\.\.(\d+))?", pos_str)
                if pos_match:
                    start = int(pos_match.group(1))
                    end = int(pos_match.group(2)) if pos_match.group(2) else start
                    current = {
                        "start": start,
                        "end": end,
                        "note": "",
                    }
            elif current and line.startswith("FT"):
                content = line[21:].strip() if len(line) > 21 else ""
                if content.startswith("/note="):
                    current["note"] = content.replace("/note=", "").strip('"')
                elif content.startswith("/evidence="):
                    current["evidence"] = content.replace("/evidence=", "").strip('"')
                    mutagenesis.append(current)
                    current = None
                elif current.get("note"):
                    current["note"] += " " + content.strip('"')
            elif not line.startswith("FT"):
                if current:
                    if current.get("note"):
                        mutagenesis.append(current)
                    current = None

    return mutagenesis


def parse_interactions(uniprot_file: Path) -> list[str]:
    """Parse CC INTERACTION entries to identify cofactors."""
    interactions = []
    in_interaction = False

    with open(uniprot_file) as f:
        for line in f:
            if "CC   -!- INTERACTION:" in line:
                in_interaction = True
            elif in_interaction:
                if line.startswith("CC       "):
                    # Look for interaction partner names
                    match = re.search(r"NbExp=(\d+).*IntAct", line)
                    if match:
                        in_interaction = False
                    name_match = re.search(r";\s*(\w+)", line)
                    if name_match:
                        interactions.append(name_match.group(1))
                elif not line.startswith("CC"):
                    in_interaction = False

    return list(set(interactions))


def map_mutagenesis_to_interfaces(mutagenesis: list[dict]) -> list[dict]:
    """Map mutagenesis data to known cofactor interfaces."""
    interface_residues = []

    for mut in mutagenesis:
        note = mut["note"]
        affected_partners = []

        # Check which cofactors are affected
        partner_patterns = [
            ("NPLOC4", r"NPLOC4|Npl4"),
            ("UFD1", r"UFD1|Ufd1"),
            ("DERL1", r"DERL1|Derlin.1"),
            ("DERL2", r"DERL2|Derlin.2"),
            ("UBXN6", r"UBXN6|UBXD1"),
            ("CAV1", r"CAV1|caveolin"),
            ("RHBDD1", r"RHBDD1"),
            ("RNF19A", r"RNF19A|dorfin"),
            ("SOD1", r"SOD1"),
            ("VCPKMT", r"VCPKMT|methylat"),
            ("ASPSCR1", r"ASPSCR1"),
            ("ZFAND1", r"ZFAND1"),
        ]

        for partner_name, pattern in partner_patterns:
            if re.search(pattern, note, re.IGNORECASE):
                affected_partners.append(partner_name)

        # Determine the effect
        effect = "unknown"
        if re.search(r"[Aa]bolish", note):
            effect = "abolishes"
        elif re.search(r"[Ss]everely reduced", note):
            effect = "severely_reduced"
        elif re.search(r"[Dd]ecreased|[Rr]educed", note):
            effect = "decreased"
        elif re.search(r"[Ii]ncreased", note):
            effect = "increased"
        elif re.search(r"[Ii]mpair", note):
            effect = "impaired"
        elif re.search(r"[Nn]o effect|[Dd]oes not", note):
            effect = "no_effect"

        if affected_partners:
            interface_residues.append({
                "start": mut["start"],
                "end": mut["end"],
                "partners": ",".join(affected_partners),
                "effect": effect,
                "note": note[:150],
            })

    return interface_residues


def main():
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} <uniprot_file> <domain_tsv> <output_prefix>", file=sys.stderr)
        sys.exit(1)

    uniprot_file = Path(sys.argv[1])
    domain_file = Path(sys.argv[2])
    output_prefix = sys.argv[3]

    # Parse domains
    domains = []
    with open(domain_file) as f:
        reader = csv.DictReader(f, delimiter="\t")
        for row in reader:
            row["start"] = int(row["start"])
            row["end"] = int(row["end"])
            domains.append(row)

    # Parse mutagenesis data
    mutagenesis = parse_mutagenesis(uniprot_file)
    print(f"Parsed {len(mutagenesis)} mutagenesis entries")

    # Map to interfaces
    interface_residues = map_mutagenesis_to_interfaces(mutagenesis)
    print(f"Found {len(interface_residues)} mutagenesis entries affecting cofactor interfaces")

    # Map each to a domain
    def get_domain(pos):
        for d in domains:
            if d["start"] <= pos <= d["end"]:
                return d["domain"]
        return "inter-domain"

    # Write interface residues report
    interface_file = f"{output_prefix}_cofactor_interfaces.tsv"
    with open(interface_file, "w", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["start", "end", "domain", "partners", "effect", "note"],
            delimiter="\t",
        )
        writer.writeheader()
        for ir in interface_residues:
            ir["domain"] = get_domain(ir["start"])
            writer.writerow(ir)
    print(f"Wrote cofactor interfaces to {interface_file}")

    # Build summary: which domain binds which cofactors
    domain_partner_map: dict[str, set[str]] = {}
    for ir in interface_residues:
        domain = ir["domain"]
        for partner in ir["partners"].split(","):
            domain_partner_map.setdefault(domain, set()).add(partner)

    summary_file = f"{output_prefix}_interface_summary.tsv"
    with open(summary_file, "w", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["domain", "cofactors", "n_cofactors", "n_mutagenesis_sites"],
            delimiter="\t",
        )
        writer.writeheader()
        for domain_name in sorted(domain_partner_map.keys()):
            partners = sorted(domain_partner_map[domain_name])
            n_sites = sum(1 for ir in interface_residues if ir["domain"] == domain_name)
            writer.writerow({
                "domain": domain_name,
                "cofactors": ",".join(partners),
                "n_cofactors": len(partners),
                "n_mutagenesis_sites": n_sites,
            })
    print(f"Wrote interface summary to {summary_file}")

    # Print summary
    print("\nCofactor interface summary:")
    for domain_name in sorted(domain_partner_map.keys()):
        partners = sorted(domain_partner_map[domain_name])
        print(f"  {domain_name}: {', '.join(partners)}")


if __name__ == "__main__":
    main()
