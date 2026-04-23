#!/usr/bin/env python3
"""Analyze disease mutation distribution relative to domain architecture.

Parses disease-associated variants from UniProt flat file and maps them to domains
identified by the domain analysis script. Computes clustering statistics.

Input: UniProt flat file, domain TSV from analyze_domains.py
Output: TSV report of mutations mapped to domains, clustering summary
"""

import sys
import re
import csv
from pathlib import Path
from collections import Counter


def parse_variants(uniprot_file: Path) -> list[dict]:
    """Parse FT VARIANT entries from UniProt flat file."""
    variants = []
    current_variant = None

    with open(uniprot_file) as f:
        for line in f:
            if line.startswith("FT   VARIANT"):
                # Parse position
                pos_str = line[21:].strip()
                pos_match = re.match(r"(\d+)", pos_str)
                if pos_match:
                    current_variant = {
                        "position": int(pos_match.group(1)),
                        "note": "",
                        "evidence": "",
                        "id": "",
                    }
            elif current_variant and line.startswith("FT"):
                content = line[21:].strip() if len(line) > 21 else ""
                if content.startswith("/note="):
                    current_variant["note"] = content.replace("/note=", "").strip('"')
                elif content.startswith("/evidence="):
                    current_variant["evidence"] = content.replace("/evidence=", "").strip('"')
                elif content.startswith("/id="):
                    current_variant["id"] = content.replace("/id=", "").strip('"')
                    variants.append(current_variant)
                    current_variant = None
                elif current_variant["note"]:
                    # Continuation of note
                    current_variant["note"] += " " + content.strip('"')
            else:
                if current_variant:
                    # End of FT block without /id - still save if we have note
                    if current_variant["note"]:
                        variants.append(current_variant)
                    current_variant = None

    return variants


def parse_domains(domain_file: Path) -> list[dict]:
    """Parse domain TSV file."""
    domains = []
    with open(domain_file) as f:
        reader = csv.DictReader(f, delimiter="\t")
        for row in reader:
            row["start"] = int(row["start"])
            row["end"] = int(row["end"])
            domains.append(row)
    return domains


def classify_variant(note: str) -> dict:
    """Extract disease classification and mutation details from variant note."""
    result = {
        "change": "",
        "disease": "",
        "is_disease": False,
        "functional_effect": "",
    }

    # Extract amino acid change
    change_match = re.match(r"(\w) -> (\w)", note)
    if change_match:
        result["change"] = f"{change_match.group(1)}->{change_match.group(2)}"

    # Check for disease associations
    disease_keywords = {
        "IBMPFD": "Inclusion body myopathy with Paget disease and frontotemporal dementia",
        "FTDALS": "Frontotemporal dementia and/or amyotrophic lateral sclerosis",
        "CMT2Y": "Charcot-Marie-Tooth disease type 2Y",
    }

    for keyword, full_name in disease_keywords.items():
        if keyword in note:
            result["disease"] = full_name
            result["is_disease"] = True
            break

    # Extract functional effects
    effects = []
    effect_patterns = [
        (r"increased ATPase activity", "increased ATPase activity"),
        (r"impaired autophagic function", "impaired autophagy"),
        (r"impaired.*ERAD", "impaired ERAD"),
        (r"reduced affinity for ADP", "reduced ADP affinity"),
        (r"increased affinity for ATP", "increased ATP affinity"),
        (r"decreased interaction with (\w+)", "decreased interaction"),
        (r"abolished? .*interaction", "abolished interaction"),
        (r"normal ATPase activity", "normal ATPase activity"),
    ]
    for pattern, effect in effect_patterns:
        if re.search(pattern, note, re.IGNORECASE):
            effects.append(effect)

    result["functional_effect"] = "; ".join(effects)
    return result


def map_to_domain(position: int, domains: list[dict]) -> str:
    """Map a position to its domain."""
    for d in domains:
        if d["start"] <= position <= d["end"]:
            return d["domain"]
    return "inter-domain"


def main():
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} <uniprot_file> <domain_tsv> <output_prefix>", file=sys.stderr)
        sys.exit(1)

    uniprot_file = Path(sys.argv[1])
    domain_file = Path(sys.argv[2])
    output_prefix = sys.argv[3]

    variants = parse_variants(uniprot_file)
    domains = parse_domains(domain_file)

    print(f"Parsed {len(variants)} variants from UniProt")
    print(f"Using {len(domains)} domain definitions")

    # Classify and map variants
    results = []
    for v in variants:
        classification = classify_variant(v["note"])
        domain = map_to_domain(v["position"], domains)
        results.append({
            "position": v["position"],
            "change": classification["change"],
            "disease": classification["disease"],
            "is_disease": classification["is_disease"],
            "domain": domain,
            "functional_effect": classification["functional_effect"],
            "variant_id": v["id"],
            "note_excerpt": v["note"][:120],
        })

    # Write full results
    output_file = f"{output_prefix}_mutations.tsv"
    with open(output_file, "w", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["position", "change", "disease", "is_disease", "domain", "functional_effect", "variant_id", "note_excerpt"],
            delimiter="\t",
        )
        writer.writeheader()
        for r in results:
            writer.writerow(r)
    print(f"Wrote mutations to {output_file}")

    # Compute clustering statistics
    disease_variants = [r for r in results if r["is_disease"]]
    domain_counts = Counter(r["domain"] for r in disease_variants)

    # Compute domain sizes
    domain_sizes = {}
    for d in domains:
        domain_sizes[d["domain"]] = d["end"] - d["start"] + 1

    summary_file = f"{output_prefix}_mutation_summary.tsv"
    with open(summary_file, "w", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["domain", "domain_size_aa", "n_disease_mutations", "mutations_per_100aa", "positions"],
            delimiter="\t",
        )
        writer.writeheader()

        for domain_name in sorted(domain_sizes.keys()):
            size = domain_sizes[domain_name]
            count = domain_counts.get(domain_name, 0)
            density = (count / size) * 100 if size > 0 else 0
            positions = sorted(set(r["position"] for r in disease_variants if r["domain"] == domain_name))
            writer.writerow({
                "domain": domain_name,
                "domain_size_aa": size,
                "n_disease_mutations": count,
                "mutations_per_100aa": f"{density:.2f}",
                "positions": ",".join(str(p) for p in positions),
            })

        # Also count inter-domain
        inter_count = domain_counts.get("inter-domain", 0)
        if inter_count > 0:
            total_len = sum(domain_sizes.values())
            seq_len = max(d["end"] for d in domains)
            inter_size = seq_len - total_len
            density = (inter_count / inter_size) * 100 if inter_size > 0 else 0
            positions = sorted(set(r["position"] for r in disease_variants if r["domain"] == "inter-domain"))
            writer.writerow({
                "domain": "inter-domain",
                "domain_size_aa": inter_size,
                "n_disease_mutations": inter_count,
                "mutations_per_100aa": f"{density:.2f}",
                "positions": ",".join(str(p) for p in positions),
            })

    print(f"Wrote mutation summary to {summary_file}")
    print(f"\nDisease mutation clustering:")
    for domain_name, count in domain_counts.most_common():
        print(f"  {domain_name}: {count} mutations")


if __name__ == "__main__":
    main()
