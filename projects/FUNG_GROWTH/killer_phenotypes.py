#!/usr/bin/env python3
"""Find decisive ("killer") carbon-source phenotypes in the FUNG-GROWTH matrix.

A plate rating on its own is hard to interpret because many fungi make thin
colonies with no carbon source at all (they scavenge agar, impurities and
reserves). Every call here is therefore made relative to the strain's own
"no carbon source" control plate:

  delta = rating(carbon source) - rating(no carbon source)

  NO_GROWTH   delta <= 0     (no better than starvation)
  WEAK        delta in 1..2
  GROWTH      delta >= 3

A "killer" phenotype is a NO_GROWTH call on a carbon source that comparable
fungi do use. Two comparators are reported:

  database   GROWTH in >= --min-users of all rated strains (default 75%)
  genus      GROWTH in >= --min-genus of the other strains of the same genus,
             with at least --genus-n such strains (defaults 50%, 3)

The genus comparator catches lineage-specific losses (e.g. D-galactose in
Aspergillus niger) on carbon sources that are rare across the whole database. Such a
cell is a sharp, easily falsifiable claim: the organism lacks a working route
for using that carbon source. It is the kind of phenotype that can confirm or
contradict a GO annotation to a catabolic process or to an uptake transporter.

Sister-plate rule. Pectin and xylan are each scored on more than one
preparation (apple and citrus pectin; beechwood, birchwood and oat spelt
xylan). A killer call on one of these plates is kept only if every sister
plate scored for the same strain is also NO_GROWTH. A strain that grows, even
weakly, on another preparation of the same polymer does have a route for
using it, so the lone no-growth plate is more likely an artefact of that
preparation or of the scoring. Rejected calls are written separately
(--no-sister-check turns the rule off).

Writes data/killer_phenotypes.tsv, data/killer_rejected_sister.tsv and
data/carbon_source_summary.tsv, and prints the calls for the species that
have gene reviews in this repository.
"""

from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path

DATA = Path(__file__).parent / "data"
BASELINE = "no carbon source"

# Plates that are different preparations of the same polymer
SISTERS = [
    ["apple pectin 1% pH=6", "citrus pectin 1% pH=6"],
    ["beechwood xylan 1%", "birchwood xylan 1%", "oat spelt xylan 1%"],
]
SISTER_OF = {p: [q for q in g if q != p] for g in SISTERS for p in g}

# FUNG-GROWTH strain -> repository species folder with gene reviews
REPO_STRAINS = {
    "Saccharomyces cerevisiae S288C": "yeast",
    "Schizosaccharomyces pombe 972h-": "SCHPO",
    "Candida albicans SC5314": "CANAL",
    "Neurospora crassa OR74A": "NEUCR",
    "Aspergillus nidulans FGSC A4": "EMENI",
    "Aspergillus niger CBS 513.88": "ASPNG",
    "Aspergillus oryzae RIB40": "ASPOR",
    "Trichoderma reesei": "HYPJE",
    "Pyricularia oryzae Guy11": "PYROR",
    "Penicillium rubens Wisconsin 54-1255": "PENCH",
    "Ustilago maydis": "MYCMD",
}


def call(delta: int) -> str:
    if delta <= 0:
        return "NO_GROWTH"
    if delta <= 2:
        return "WEAK"
    return "GROWTH"


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--min-users", type=float, default=0.75,
                    help="fraction of rated strains that must GROW for a NO_GROWTH call to count as killer")
    ap.add_argument("--min-genus", type=float, default=0.5,
                    help="fraction of same-genus strains that must GROW (genus comparator)")
    ap.add_argument("--genus-n", type=int, default=3,
                    help="minimum number of other same-genus strains rated (genus comparator)")
    ap.add_argument("--no-sister-check", action="store_true",
                    help="keep killer calls even when a sister plate of the same polymer shows growth")
    args = ap.parse_args()

    rows = list(csv.DictReader(open(DATA / "fung_growth_matrix.tsv"), delimiter="\t"))
    sources = [c for c in rows[0] if c not in ("strain", BASELINE)]

    calls: dict[str, dict[str, tuple[int, int, str]]] = {}
    for r in rows:
        if r[BASELINE] == "":
            continue
        base = int(r[BASELINE])
        calls[r["strain"]] = {
            s: (int(r[s]), base, call(int(r[s]) - base)) for s in sources if r[s] != ""
        }

    counts: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))
    for strain_calls in calls.values():
        for s, (_, _, c) in strain_calls.items():
            counts[s][c] += 1

    with open(DATA / "carbon_source_summary.tsv", "w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t")
        w.writerow(["carbon_source", "n_rated", "GROWTH", "WEAK", "NO_GROWTH", "frac_growth"])
        for s in sorted(sources, key=lambda x: -sum(counts[x].values())):
            n = sum(counts[s].values())
            if n:
                w.writerow([s, n, counts[s]["GROWTH"], counts[s]["WEAK"], counts[s]["NO_GROWTH"],
                            f"{counts[s]['GROWTH'] / n:.2f}"])

    common = {s for s in sources
              if sum(counts[s].values()) and counts[s]["GROWTH"] / sum(counts[s].values()) >= args.min_users}

    def genus(strain: str) -> str:
        return strain.split()[0].capitalize()

    killers, rejected = [], []
    for strain, strain_calls in calls.items():
        congeners = [o for o in calls if o != strain and genus(o) == genus(strain)]
        for s, (rating, base, c) in strain_calls.items():
            if c != "NO_GROWTH":
                continue
            n = sum(counts[s].values())
            peers = [calls[o][s][2] for o in congeners if s in calls[o]]
            g_frac = peers.count("GROWTH") / len(peers) if peers else 0.0
            basis = []
            if s in common:
                basis.append("database")
            if len(peers) >= args.genus_n and g_frac >= args.min_genus:
                basis.append("genus")
            if not basis:
                continue
            sisters = [(q, strain_calls[q]) for q in SISTER_OF.get(s, []) if q in strain_calls]
            sister_txt = "; ".join(f"{q}={r}/{b} {c2}" for q, (r, b, c2) in sisters)
            row = (strain, REPO_STRAINS.get(strain, ""), s, rating, base,
                   f"{counts[s]['GROWTH'] / n:.2f}",
                   f"{peers.count('GROWTH')}/{len(peers)}" if peers else "", "+".join(basis), sister_txt)
            if not args.no_sister_check and any(c2 != "NO_GROWTH" for _, (_, _, c2) in sisters):
                rejected.append(row)
            else:
                killers.append(row)
    killers.sort(key=lambda k: (k[0], k[2]))
    rejected.sort(key=lambda k: (k[0], k[2]))

    header = ["strain", "repo_species", "carbon_source", "rating", "no_carbon_rating",
              "frac_strains_growing", "genus_peers_growing", "basis", "sister_plates"]
    for name, data in (("killer_phenotypes.tsv", killers), ("killer_rejected_sister.tsv", rejected)):
        with open(DATA / name, "w", newline="") as fh:
            w = csv.writer(fh, delimiter="\t")
            w.writerow(header)
            w.writerows(data)

    print(f"{len(calls)} strains with a no-carbon control; {len(common)} carbon sources used by "
          f">= {args.min_users:.0%} of strains; {len(killers)} killer phenotypes "
          f"({len(rejected)} more rejected by the sister-plate rule)")
    print("\nKiller phenotypes for strains with gene reviews in this repo:")
    for strain, folder in REPO_STRAINS.items():
        if strain not in calls:
            print(f"  {strain}: not rated")
            continue
        ks = [k[2] for k in killers if k[0] == strain]
        print(f"  {strain} [{folder}] (no-carbon={next(iter(calls[strain].values()))[1]}): "
              f"{', '.join(ks) or '-'}")


if __name__ == "__main__":
    main()
