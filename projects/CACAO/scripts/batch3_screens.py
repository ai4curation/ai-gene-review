"""Three deterministic screens over the CACAO snapshot, each testing a batch-2 finding.

Batch 2 found three failure shapes that can be looked for without reading papers.
This script runs all three over the QuickGO snapshot and writes
projects/CACAO/batch3-screens.yaml.

1. adjacent_locus: numerically-named genes (the T4 gp5.4 shape, where papers
   writing "gp5" were annotated onto the entry named 5.4). Highest-risk subset is
   a numerically-named gene sharing a cited PMID with another numerically-named
   gene in the same taxon.
2. cross_isolate: a PMID cited by CACAO rows on gene products from more than one
   taxon (the Gag shape, where one isolate's experiments were given experimental
   codes on another isolate's entry).
3. odd_qualifier: CACAO rows whose qualifier is not one of the three standard
   ones (the AcrIIA5 shape, where acts_upstream_of_or_within_positive_effect was
   used for a process the protein executes).

Usage:
    uv run python projects/CACAO/scripts/batch3_screens.py [QUICKGO_TSV]
"""

import collections
import csv
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[3]
DEFAULT_TSV = ROOT / "projects/CACAO/data/cacao-quickgo-2026-10-28.tsv"
GROUPS = ROOT / "projects/CACAO/data/taxon-groups.yaml"
INVENTORY = ROOT / "projects/CACAO/cacao-inventory.yaml"
OUT = ROOT / "projects/CACAO/batch3-screens.yaml"

STANDARD_QUALIFIERS = {"involved_in", "enables", "part_of", "located_in"}
NUMERIC_SYMBOL = re.compile(r"^[0-9]+(\.[0-9]+)?$")


def main():
    tsv = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_TSV
    groups = yaml.safe_load(GROUPS.read_text())
    inv = yaml.safe_load(INVENTORY.read_text())
    reviewed = {g["accession"] for g in inv["genes"]}

    rows = []
    with open(tsv) as fh:
        for r in csv.DictReader(fh, delimiter="\t"):
            r["_taxon"] = int(r["TAXON ID"])
            r["_group"] = groups.get(r["_taxon"], {}).get("group", "Unclassified")
            r["_organism"] = groups.get(r["_taxon"], {}).get("name")
            rows.append(r)

    by_acc = collections.defaultdict(list)
    for r in rows:
        by_acc[r["GENE PRODUCT ID"]].append(r)

    def entry(acc, note=None):
        rs = by_acc[acc]
        d = {
            "accession": acc,
            "symbol": rs[0]["SYMBOL"],
            "taxon": f"NCBITaxon:{rs[0]['TAXON ID']}",
            "organism": rs[0]["_organism"],
            "group": rs[0]["_group"],
            "cacao_rows": len(rs),
            "reviewed": acc in reviewed,
        }
        if note:
            d["note"] = note
        return d

    # --- screen 1: numerically-named genes, and the shared-PMID subset
    numeric = {a for a, rs in by_acc.items() if NUMERIC_SYMBOL.match(rs[0]["SYMBOL"] or "")}
    pmid_to_numeric = collections.defaultdict(set)
    for a in numeric:
        for r in by_acc[a]:
            if r["REFERENCE"].startswith("PMID:"):
                pmid_to_numeric[(r["_taxon"], r["REFERENCE"])].add(a)
    collisions = {}
    for (taxon, pmid), accs in pmid_to_numeric.items():
        if len(accs) > 1:
            for a in accs:
                collisions.setdefault(a, set()).add(f"{pmid} shared with {sorted(accs - {a})}")
    screen1 = {
        "description": (
            "Numerically-named gene products carrying CACAO rows. A paper writing "
            "'gp5' can land on the entry named '5.4'; the T4 gp5.4 review found all "
            "four of its rows misattributed this way."
        ),
        "numeric_symbol_gene_products": len(numeric),
        "unreviewed": sorted(
            (entry(a) for a in numeric if a not in reviewed),
            key=lambda e: (-e["cacao_rows"], e["accession"]),
        ),
        "shared_pmid_with_another_numeric_gene": sorted(
            (entry(a, "; ".join(sorted(collisions[a]))) for a in collisions),
            key=lambda e: (e["reviewed"], -e["cacao_rows"]),
        ),
    }

    # --- screen 2: one PMID, CACAO rows on more than one taxon
    pmid_taxa = collections.defaultdict(set)
    pmid_accs = collections.defaultdict(set)
    for r in rows:
        if r["REFERENCE"].startswith("PMID:"):
            pmid_taxa[r["REFERENCE"]].add(r["_taxon"])
            pmid_accs[r["REFERENCE"]].add(r["GENE PRODUCT ID"])
    multi = {p: t for p, t in pmid_taxa.items() if len(t) > 1}

    def kin(names):
        """True when the organism names look like isolates of one species group.

        The point of this screen is the Gag shape: a paper on one isolate given
        experimental codes on a sibling isolate's entry. A paper spanning many
        distant taxa is a comparative study legitimately annotating each one, so
        taxon count alone over-flags badly (one reference here spans 25 taxa).
        The discriminator is taxonomic proximity: names sharing their leading
        tokens, e.g. two Human papillomavirus types or three Pseudomonas phages.
        """
        toks = [re.split(r"[\s(]+", n.strip())[0:2] for n in names if n]
        if len(toks) < 2:
            return False
        first = {t[0] for t in toks}
        if len(first) > 1:
            return False
        # same genus/first word; require a shared second token for 'Human
        # papillomavirus 59' vs 'Human herpesvirus 1' style collisions
        second = {t[1] if len(t) > 1 else "" for t in toks}
        return len(first) == 1 and (len(second) > 1 or len(toks) > 1)

    cands = []
    for p, taxa in multi.items():
        names = sorted({groups.get(t, {}).get("name") or str(t) for t in taxa})
        gs = {groups.get(t, {}).get("group") for t in taxa}
        cands.append({
            "reference": p,
            "taxa": sorted(f"NCBITaxon:{t}" for t in taxa),
            "organisms": names,
            "groups": sorted(g for g in gs if g),
            "gene_products": sorted(pmid_accs[p]),
            "any_reviewed": bool(pmid_accs[p] & reviewed),
            "_kin": kin(names),
            "_n": len(taxa),
        })
    likely = sorted(
        (c for c in cands if c["_kin"] and c["_n"] <= 4),
        key=lambda c: (c["any_reviewed"], -len(c["gene_products"])),
    )
    comparative = sorted((c for c in cands if c["_n"] > 6), key=lambda c: -c["_n"])
    for c in cands:
        c.pop("_kin", None)
        c.pop("_n", None)
    screen2 = {
        "description": (
            "A single PMID cited by CACAO rows on gene products from more than one "
            "taxon. The Gag review found four rows giving this isolate experimental "
            "codes for prototype-foamy-virus experiments, where ISS is the right "
            "code. Taxon count alone is a poor screen: the widest reference here "
            "spans 25 taxa and is a comparative study that legitimately annotates "
            "each. The candidate set is therefore references spanning 2-4 taxa whose "
            "organism names look like isolates of one species group; each still needs "
            "the paper read, since a paper may genuinely assay two of them."
        ),
        "references_spanning_taxa": len(multi),
        "likely_isolate_transfer": likely,
        "wide_comparative_studies_not_candidates": [
            {"reference": c["reference"], "taxa": c["_n"] if "_n" in c else len(c["taxa"]),
             "organisms_sample": c["organisms"][:3]}
            for c in comparative
        ],
    }

    # --- screen 3: non-standard qualifiers
    odd = [r for r in rows if r["QUALIFIER"] not in STANDARD_QUALIFIERS]
    by_qual = collections.Counter(r["QUALIFIER"] for r in odd)
    screen3 = {
        "description": (
            "CACAO rows whose qualifier is not involved_in, enables, part_of or "
            "located_in. AcrIIA5's 2025 row used "
            "acts_upstream_of_or_within_positive_effect for a process the protein "
            "executes directly, while the same group's earlier rows used involved_in."
        ),
        "qualifier_counts": dict(by_qual.most_common()),
        "rows": sorted(
            (
                {
                    "accession": r["GENE PRODUCT ID"],
                    "symbol": r["SYMBOL"],
                    "organism": r["_organism"],
                    "group": r["_group"],
                    "term": r["GO TERM"],
                    "evidence": r["GO EVIDENCE CODE"],
                    "reference": r["REFERENCE"],
                    "qualifier": r["QUALIFIER"],
                    "reviewed": r["GENE PRODUCT ID"] in reviewed,
                }
                for r in odd
            ),
            key=lambda d: (d["reviewed"], d["qualifier"], d["accession"]),
        ),
    }

    OUT.write_text(
        yaml.safe_dump(
            {
                "source": str(tsv.relative_to(ROOT)),
                "adjacent_locus": screen1,
                "cross_isolate": screen2,
                "odd_qualifier": screen3,
            },
            sort_keys=False,
            width=100,
            allow_unicode=True,
        )
    )
    print(f"screen 1 numeric-symbol gene products: {len(numeric)} "
          f"({sum(1 for a in numeric if a not in reviewed)} unreviewed); "
          f"{len(collisions)} share a PMID with another numeric gene")
    print(f"screen 2 references spanning >1 taxon: {len(multi)}")
    print(f"screen 3 non-standard-qualifier rows: {len(odd)} "
          f"({sum(1 for r in odd if r['GENE PRODUCT ID'] not in reviewed)} on unreviewed genes)")
    print(f"wrote {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
