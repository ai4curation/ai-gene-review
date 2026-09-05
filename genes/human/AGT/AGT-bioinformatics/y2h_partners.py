"""Compartment check on AGT's `GO:0005515 protein binding` IPI partners.

GOA gives human AGT sixteen `protein binding` IPI rows. Ten of them come from a
single large-scale yeast two-hybrid interactome of *neurodegenerative disease*
proteins (PMID:32814053), and one from a yeast two-hybrid screen using a
hepatitis C virus protein as bait (PMID:16237761).

AGT is a secreted plasma glycoprotein with a cleaved signal peptide; a yeast
two-hybrid assay reconstitutes a transcription factor in the yeast **nucleus**,
so a secreted bait/prey is tested in a compartment it never occupies in vivo.
This script asks, for every IPI partner taken straight out of the GOA file,
where UniProt says that partner lives - so the compartment mismatch is counted
rather than asserted.

Run: uv run python y2h_partners.py
"""

from __future__ import annotations

import csv
from pathlib import Path

from uniprot import summarise, uniprot_entry

HERE = Path(__file__).parent
GOA = HERE.parent / "AGT-goa.tsv"

SECRETED_WORDS = ("Secreted", "Extracellular")


def main() -> None:
    with GOA.open() as fh:
        rows = [r for r in csv.DictReader(fh, delimiter="\t") if r["GO EVIDENCE CODE"] == "IPI"]

    target = summarise(uniprot_entry("P01019"))
    print(f"target P01019 AGT: locations={target['locations']}, "
          f"signal peptide keyword={'Signal' in target['keywords']}\n")

    out = []
    for r in rows:
        for tok in r["WITH/FROM"].split("|"):
            tok = tok.strip()
            if not tok.startswith("UniProtKB:"):
                continue
            acc = tok.split(":", 1)[1]
            s = summarise(uniprot_entry(acc))
            locs = s["locations"]
            secreted = any(any(w in loc for w in SECRETED_WORDS) for loc in locs)
            out.append(
                {
                    "reference": r["REFERENCE"],
                    "partner": acc,
                    "gene": s["gene"],
                    "organism": s["organism"],
                    "go_term": r["GO TERM"],
                    "locations": "; ".join(locs) or "(none annotated)",
                    "shares_secreted_compartment_with_AGT": "yes" if secreted else "no",
                }
            )

    dest = HERE / "y2h_partners.tsv"
    with dest.open("w", newline="") as fh:
        w = csv.DictWriter(fh, delimiter="\t", fieldnames=list(out[0]))
        w.writeheader()
        w.writerows(out)

    by_ref: dict[str, list[dict[str, str]]] = {}
    for o in out:
        by_ref.setdefault(o["reference"], []).append(o)

    for ref, group in sorted(by_ref.items(), key=lambda kv: -len(kv[1])):
        shared = sum(1 for g in group if g["shares_secreted_compartment_with_AGT"] == "yes")
        print(f"{ref}: {len(group)} partner(s); "
              f"{shared} share a secreted/extracellular compartment with AGT")
        for g in group:
            print(f"    {g['partner']:12} {g['gene']:10} {g['go_term']:12} "
                  f"{g['organism'][:22]:24} {g['locations'][:70]}")
        print()

    total = len(out)
    shared = sum(1 for o in out if o["shares_secreted_compartment_with_AGT"] == "yes")
    print(f"TOTAL IPI partners: {total}; sharing a secreted/extracellular "
          f"compartment with AGT: {shared} ({shared / total:.0%})")


if __name__ == "__main__":
    main()
