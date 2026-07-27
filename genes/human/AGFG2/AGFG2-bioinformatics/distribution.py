#!/usr/bin/env python3
"""Two cited papers disagree about when AGFG2 arose. Test it, and record the taxa
that PAINT node PTN002919572 actually reaches.

* PMID:21284487 (Immunopharmacol Immunotoxicol 2011, from "the first section of the
  coding mRNAs" only): "AGFG2s, present in mammals only".
* PMID:23433073 (Traffic 2013, phylogenetic): the AGFG subfamily "undergone a single
  duplication" among subfamilies that duplicated "at the base of vertebrates".

The check is a UniProt gene-name census by clade, with positive controls, so a zero
cannot be a broken query.  A symbol census is NOT an orthologue census — it is a
name-matching pipeline's output — so the result is reported as what it is and the
Swiss-Prot/TrEMBL split is printed.

Separately, the taxon composition of PTN002919572 decides whether the acrosome and
spermatid terms it donates are being asserted outside mammals as well.
"""

from __future__ import annotations

import json
import pathlib
import sys
from collections import Counter

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from common import (  # noqa: E402
    get_json,
    is_reviewed,
    quickgo_annotations,
    uniprot_search,
    uniprot_search_total,
)

HERE = pathlib.Path(__file__).parent

CLADES = {
    # label: NCBI taxon id
    "Mammalia": 40674,
    "Aves": 8782,
    "Actinopterygii (bony fish)": 7898,
    "Amphibia": 8292,
    "Sauropsida (reptiles+birds)": 8457,
}
CONTROL_GENE = "agfg1"   # must be non-zero in every clade AGFG2 is tested in


PAGE = 200


def census(gene: str, taxon: int) -> dict:
    q = f"gene_exact:{gene} AND taxonomy_id:{taxon}"
    total = uniprot_search_total(q)          # from x-total-results, not from a page
    hits = uniprot_search(q, "accession,id,gene_names,organism_name,length,reviewed",
                          size=PAGE)
    # Compare against len(hits), never against the page-size constant: the server
    # may clamp `size` rather than error, and then a clamped page reads as a total.
    truncated = len(hits) < total
    return {
        "total": total,
        "n_fetched": len(hits),
        "truncated": truncated,
        "n_reviewed_in_fetched": sum(1 for h in hits if is_reviewed(h)),
        "organisms_in_fetched": sorted({h["organism"]["scientificName"] for h in hits})[:12],
    }


def main() -> None:
    out: dict = {"census": {}, "node_taxa": {}, "clade_taxon_ids": dict(CLADES)}
    for label, tx in CLADES.items():
        out["census"][label] = {
            "taxon_id": tx,
            "AGFG2": census("agfg2", tx),
            "AGFG1_control": census(CONTROL_GENE, tx),
        }
    for label, v in out["census"].items():
        if v["AGFG1_control"]["total"] == 0:
            raise AssertionError(
                f"positive control AGFG1 returned 0 in {label} — the query pattern is "
                f"broken, so the AGFG2 count there is uninterpretable"
            )

    rows = quickgo_annotations(withFrom="PANTHER:PTN002919572", limit=100)
    per_entity = {}
    for r in rows:
        per_entity.setdefault(r["geneProductId"], str(r.get("taxonId")))
    # QuickGO returns only taxonId here, so resolve names rather than printing bare
    # numbers — an unresolved id cannot support a claim about clade breadth.
    names = {}
    for tx in sorted(set(per_entity.values())):
        d = get_json(f"https://rest.uniprot.org/taxonomy/{tx}.json")
        got = str(d.get("taxonId"))
        if got != tx:
            raise AssertionError(f"taxonomy drift: asked {tx}, got {got}")
        names[tx] = d.get("scientificName")
    out["node_taxa"] = {
        "node": "PANTHER:PTN002919572",
        "n_annotations": len(rows),
        "n_entities": len(per_entity),
        "taxon_names": names,
        "entity_taxa": [[names[tx], n]
                        for tx, n in Counter(per_entity.values()).most_common()],
    }

    (HERE / "distribution.json").write_text(json.dumps(out, indent=2, sort_keys=True))

    print("UniProt gene-symbol census (a symbol count is NOT an orthologue count):")
    for label, v in out["census"].items():
        a2, a1 = v["AGFG2"], v["AGFG1_control"]
        print(f"  {label:28s} agfg2: {a2['total']:4d} total"
              f"{' (page truncated)' if a2['truncated'] else ''}   "
              f"agfg1 [control]: {a1['total']:4d} total"
              f"{' (page truncated)' if a1['truncated'] else ''}")
        if a2["total"]:
            print(f"      agfg2 organisms in first {a2['n_fetched']} fetched: "
                  f"{', '.join(a2['organisms_in_fetched'])}")

    nt = out["node_taxa"]
    print(f"\n{nt['node']}: {nt['n_annotations']} annotations over {nt['n_entities']} "
          f"gene products")
    for tx, n in nt["entity_taxa"]:
        print(f"    {n:3d}  {tx}")


if __name__ == "__main__":
    main()
