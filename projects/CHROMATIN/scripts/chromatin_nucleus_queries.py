"""How much does GO's chromatin/nucleus modelling change gene-level queries?

Two questions over one GAF (protein rows only; NOT and complex rows excluded):

1. Of the genes whose CC annotations reach chromatin (GO:0000785) by is_a/part_of,
   how many have no annotation that reaches nucleus (GO:0005634)? These are the
   genes a "nucleus" query misses because chromatin is not part_of nucleus.
2. If the part_of chromatin edges on protein-containing complexes (and on
   perichromatin fibrils) were removed, keeping nucleosome, how many genes would
   stop reaching chromatin, and through which complexes?

Usage:
    python chromatin_nucleus_queries.py go-basic.obo goa_human.gaf.gz
"""

from __future__ import annotations

import collections
import gzip
import sys
from typing import Dict, Set

from go_closure import load

CHROMATIN = "GO:0000785"
NUCLEUS = "GO:0005634"
COMPLEX = "GO:0032991"
NUCLEOSOME = "GO:0000786"
PERICHROMATIN_FIBRILS = "GO:0005726"


def read_cc(gaf_path: str, primary) -> Dict[str, Set[str]]:
    """Map gene symbol -> CC term ids from a gzipped GAF (protein rows, no NOT)."""
    terms: Dict[str, Set[str]] = collections.defaultdict(set)
    with gzip.open(gaf_path, "rt") as handle:
        for line in handle:
            if line.startswith("!"):
                continue
            cols = line.rstrip("\n").split("\t")
            if cols[8] != "C" or "NOT" in cols[3] or "complex" in cols[11]:
                continue
            terms[cols[2]].add(primary(cols[4]))
    return terms


def main(obo_path: str, gaf_path: str) -> None:
    """Print both measurements."""
    graph = load(obo_path)
    genes = read_cc(gaf_path, graph.primary)
    memo: Dict[str, Set[str]] = {}

    def anc(term: str) -> Set[str]:
        if term not in memo:
            memo[term] = graph.ancestors(term)
        return memo[term]

    def reaches(gene: str, target: str) -> bool:
        return any(target in anc(t) for t in genes[gene])

    chromatin = {g for g in genes if reaches(g, CHROMATIN)}
    no_nucleus = sorted(g for g in chromatin if not reaches(g, NUCLEUS))
    nucleus_total = sum(1 for g in genes if reaches(g, NUCLEUS))
    print(f"genes reaching chromatin: {len(chromatin)}")
    print(f"  with no annotation reaching nucleus: {len(no_nucleus)} "
          f"({100 * len(no_nucleus) / len(chromatin):.1f}%); "
          f"{100 * len(no_nucleus) / nucleus_total:.2f}% of the {nucleus_total} nucleus genes")
    print("  " + " ".join(no_nucleus))

    cut = sorted(
        t for t, ps in graph.parents.items()
        if CHROMATIN in ps and t != NUCLEOSOME
        and (COMPLEX in anc(t) or t == PERICHROMATIN_FIBRILS)
    )
    edited = {t: (ps - {CHROMATIN} if t in cut else ps) for t, ps in graph.parents.items()}
    memo2: Dict[str, Set[str]] = {}

    def anc2(term: str) -> Set[str]:
        if term not in memo2:
            memo2[term] = graph.ancestors(term, edited)
        return memo2[term]

    lost = sorted(g for g in chromatin if not any(CHROMATIN in anc2(t) for t in genes[g]))
    via = collections.Counter(c for g in lost for c in cut if any(c in anc(t) for t in genes[g]))
    still_nuclear = [g for g in lost if reaches(g, NUCLEUS)]
    print("\npart_of chromatin removed from: " + "; ".join(f"{t} {graph.names[t]}" for t in cut))
    print(f"genes that would stop reaching chromatin: {len(lost)}; "
          f"{len(still_nuclear)} of them reach nucleus through other annotations")
    print("  by complex: " + ", ".join(f"{graph.names[c]} {n}" for c, n in via.most_common()))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
