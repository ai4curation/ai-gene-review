#!/usr/bin/env python3
"""Enrich prioritized PDB entries with RCSB metadata (ligands + complex content).

For genes that currently LACK experimental molecular-function GO (from
pdb_gene_summary.tsv), query the RCSB Data API (GraphQL) for each deposited PDB
entry to find what is actually *in* the structure:
  - bound non-polymer ligands / cofactors / metals (the strongest functional clue)
  - number of distinct protein / nucleic-acid entities (i.e. is it a complex?)
  - structure title

Bulk crystallization/cryo additives are filtered out (BUFFER set) so that the
"meaningful ligand" count reflects substrates, products, cofactors, inhibitors,
and catalytic metals rather than glycerol and sulfate.

Network required (https://data.rcsb.org/graphql). Re-runnable; caches nothing,
writes data/pdb_enriched.tsv and data/pdb_gene_enriched.tsv.
"""
from __future__ import annotations

import csv
import json
import sys
import time
import urllib.error
import urllib.request
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
GRAPHQL = "https://data.rcsb.org/graphql"

# Common crystallization / cryoprotection / buffer components -- NOT functional.
BUFFER = {
    "HOH", "DOD", "GOL", "EDO", "PEG", "PG4", "PGE", "1PE", "P6G", "2PE", "PG0",
    "SO4", "PO4", "ACT", "ACY", "FMT", "CL", "BR", "IOD", "NA", "K", "CS", "RB",
    "MPD", "DMS", "TRS", "EPE", "MES", "BME", "DTT", "NO3", "CO3", "BCT", "CAC",
    "FLC", "IMD", "TLA", "MLI", "MRD", "BU3", "OLC", "LDA", "DDQ", "SCN", "AZI",
    "NH4", "UNX", "UNL", "PEO", "12P", "15P", "PE4", "PE8", "MYR", "BOG", "SR",
}
# Cofactors / catalytic metals / nucleotides we always want to surface as "rich".
RICH = {
    "FAD", "FMN", "NAD", "NAP", "NDP", "NAI", "SAM", "SAH", "ATP", "ADP", "AMP",
    "ANP", "AGS", "GTP", "GDP", "GNP", "GSP", "HEM", "HEC", "HEB", "SRM", "PLP",
    "TPP", "TDP", "COA", "ACO", "B12", "COB", "CNC", "F43", "FE", "FES", "SF4",
    "FE2", "ZN", "MN", "CU", "CU1", "NI", "CO", "MO", "MOO", "MGD", "PCD", "WO4",
    "PQQ", "MDO", "BTN", "THM", "GSH", "UDP", "UDG", "CDP", "F3S", "HC0", "BCB",
}


def query(ids):
    q = """
    query($ids:[String!]!){ entries(entry_ids:$ids){
      rcsb_id
      struct{ title }
      rcsb_primary_citation{ pdbx_database_id_PubMed pdbx_database_id_DOI year
                             rcsb_journal_abbrev }
      rcsb_entry_info{ polymer_entity_count_protein polymer_entity_count_nucleic_acid
                       nonpolymer_entity_count }
      nonpolymer_entities{ nonpolymer_comp{ chem_comp{ id name } } }
    }}"""
    body = json.dumps({"query": q, "variables": {"ids": ids}}).encode()
    req = urllib.request.Request(GRAPHQL, data=body,
                                 headers={"Content-Type": "application/json"})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.loads(r.read())["data"]["entries"]
        except (urllib.error.URLError, TimeoutError) as e:
            wait = 2 ** attempt
            print(f"  retry {attempt+1} after {wait}s ({e})", file=sys.stderr)
            time.sleep(wait)
    raise RuntimeError("RCSB query failed")


def main():
    gene_rows = list(csv.DictReader(open(DATA / "pdb_gene_summary.tsv"), delimiter="\t"))
    inv_rows = list(csv.DictReader(open(DATA / "pdb_inventory.tsv"), delimiter="\t"))

    # candidate genes: no experimental MF GO
    cand = {(r["organism"], r["gene"]) for r in gene_rows if int(r["exp_mf"]) == 0}
    ids_for = defaultdict(list)
    pdb_to_gene = {}
    for r in inv_rows:
        key = (r["organism"], r["gene"])
        if key in cand:
            ids_for[key].append(r["pdb_id"])
            pdb_to_gene[r["pdb_id"]] = key

    all_ids = sorted(set(pdb_to_gene))
    print(f"Candidate genes (no exp MF GO): {len(cand)}; PDB entries to query: {len(all_ids)}")

    results = {}
    B = 50
    for i in range(0, len(all_ids), B):
        batch = all_ids[i:i + B]
        for e in query(batch):
            results[e["rcsb_id"].upper()] = e
        print(f"  fetched {min(i+B,len(all_ids))}/{len(all_ids)}", file=sys.stderr)
        time.sleep(0.3)

    enriched = []
    for pdb_id in all_ids:
        e = results.get(pdb_id.upper())
        org, gene = pdb_to_gene[pdb_id]
        if not e:
            enriched.append({"organism": org, "gene": gene, "pdb_id": pdb_id,
                             "title": "", "pmid": "", "doi": "", "year": "",
                             "n_protein": "", "n_nucleic": "",
                             "ligands_all": "", "ligands_meaningful": "",
                             "n_meaningful": 0, "has_cofactor": 0, "is_complex": 0})
            continue
        cit = e.get("rcsb_primary_citation") or {}
        info = e.get("rcsb_entry_info") or {}
        np_ent = e.get("nonpolymer_entities") or []
        ligs = []
        for ne in np_ent:
            cc = (((ne or {}).get("nonpolymer_comp") or {}).get("chem_comp")) or {}
            cid = cc.get("id")
            if cid:
                ligs.append((cid, cc.get("name") or ""))
        meaningful = [(c, n) for c, n in ligs if c not in BUFFER]
        cofactor = [(c, n) for c, n in ligs if c in RICH]
        n_prot = info.get("polymer_entity_count_protein") or 0
        n_nuc = info.get("polymer_entity_count_nucleic_acid") or 0
        enriched.append({
            "organism": org, "gene": gene, "pdb_id": pdb_id,
            "title": (e.get("struct") or {}).get("title") or "",
            "pmid": cit.get("pdbx_database_id_PubMed") or "",
            "doi": cit.get("pdbx_database_id_DOI") or "",
            "year": cit.get("year") or "",
            "n_protein": n_prot, "n_nucleic": n_nuc,
            "ligands_all": ",".join(c for c, _ in ligs),
            "ligands_meaningful": ",".join(c for c, _ in meaningful),
            "n_meaningful": len(meaningful),
            "has_cofactor": int(bool(cofactor)),
            "is_complex": int(n_prot > 1 or n_nuc > 0),
        })

    out = DATA / "pdb_enriched.tsv"
    with out.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(enriched[0].keys()), delimiter="\t")
        w.writeheader()
        w.writerows(enriched)

    # Per-gene rollup
    roll = defaultdict(lambda: {"n_pdb": 0, "with_ligand": 0, "with_cofactor": 0,
                                "with_complex": 0, "cofactors": set(), "ligands": set(),
                                "has_nucleic": 0, "papers": {}})
    for r in enriched:
        key = (r["organism"], r["gene"])
        d = roll[key]
        d["n_pdb"] += 1
        if r["n_meaningful"]:
            d["with_ligand"] += 1
            for c in r["ligands_meaningful"].split(","):
                if c:
                    d["ligands"].add(c)
        if r["has_cofactor"]:
            d["with_cofactor"] += 1
            for c in r["ligands_meaningful"].split(","):
                if c in RICH:
                    d["cofactors"].add(c)
        if r["is_complex"]:
            d["with_complex"] += 1
        if r["n_nucleic"] not in ("", 0, "0"):
            d["has_nucleic"] = 1
        # collect distinct structure papers; remember which entry/ligands they describe
        if r["pmid"]:
            p = d["papers"].setdefault(r["pmid"], {"year": r["year"], "title": r["title"],
                                                   "rich": False, "pdb": r["pdb_id"]})
            if r["has_cofactor"] or r["n_meaningful"]:
                p["rich"] = True

    EUK = {"human", "mouse", "rat", "worm", "yeast", "ARATH", "SCHPO", "SCHJY", "DANRE",
           "DROME", "XENTR", "CHICK", "BOVIN", "CRIGR", "DICDI", "CHLRE", "CANAL", "CANGA",
           "NEUCR", "ASPNG", "ASPRC", "PICST", "HYPJE", "PENCH", "PENEN", "MAIZE", "ORYSJ",
           "SOYBN", "SOLLC", "SOLTU", "VITVI", "WHEAT", "MEDTR", "POPTR", "PHYPA", "BRADI",
           "SORBI", "PHAVU", "THLAR", "TOBAC", "NICAT", "OCTBM", "OCTVU", "SEPOF", "EUPSC",
           "DAPPU", "RAMVA", "MISSI", "DESRO", "DOROP", "DORPE", "9POAL"}

    gmap = {(r["organism"], r["gene"]): r for r in gene_rows}
    grows = []
    for key, d in roll.items():
        g = gmap[key]
        # up to 3 representative papers, ligand/cofactor-bearing first, newest first
        papers = sorted(d["papers"].items(),
                        key=lambda kv: (not kv[1]["rich"], -int(kv[1]["year"] or 0)))
        pmids = [f'PMID:{pid}' for pid, _ in papers[:3]]
        grows.append({
            "organism": key[0], "gene": key[1], "uniprot": g["uniprot"],
            "is_eukaryote": int(key[0] in EUK),
            "length": g["length"], "n_pdb": d["n_pdb"],
            "max_coverage_frac": g["max_coverage_frac"],
            "best_resolution_A": g["best_resolution_A"],
            "exp_total": g["exp_total"],
            "pdb_with_cofactor": d["with_cofactor"],
            "pdb_with_ligand": d["with_ligand"],
            "pdb_with_complex": d["with_complex"],
            "has_nucleic_acid": d["has_nucleic"],
            "cofactors": ",".join(sorted(d["cofactors"])),
            "ligands": ",".join(sorted(d["ligands"])[:25]),
            "structure_papers": ";".join(pmids),
        })

    # Priority score: structure richness, gated by current annotation sparsity.
    def score(r):
        s = 0.0
        s += 3.0 * (r["pdb_with_cofactor"] > 0)
        s += 2.0 * (r["pdb_with_ligand"] > 0)
        s += 2.0 * (r["pdb_with_complex"] > 0)
        s += 1.5 * (r["has_nucleic_acid"] > 0)
        s += 1.0 * (float(r["max_coverage_frac"]) >= 0.8)
        # sparsity multiplier: most useful where least is known
        s *= 1.5 if int(r["exp_total"]) == 0 else 1.0
        return round(s, 2)

    for r in grows:
        r["priority_score"] = score(r)
    grows.sort(key=lambda r: (-r["priority_score"], -int(r["pdb_with_cofactor"]),
                              -int(r["n_pdb"])))

    gout = DATA / "pdb_gene_enriched.tsv"
    fields = ["priority_score", "organism", "gene", "uniprot", "is_eukaryote", "length",
              "n_pdb", "max_coverage_frac", "best_resolution_A", "exp_total",
              "pdb_with_cofactor", "pdb_with_ligand", "pdb_with_complex",
              "has_nucleic_acid", "cofactors", "ligands", "structure_papers"]
    with gout.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields, delimiter="\t")
        w.writeheader()
        w.writerows(grows)

    print(f"\nWrote {out}")
    print(f"Wrote {gout}")
    print("\nTop 20 (overall):")
    for r in grows[:20]:
        tag = "EUK" if r["is_eukaryote"] else "   "
        print(f'  {r["priority_score"]:>5}  {tag} {r["organism"]:7s} {r["gene"]:14s} '
              f'cof[{r["pdb_with_cofactor"]}] lig[{r["pdb_with_ligand"]}] '
              f'cplx[{r["pdb_with_complex"]}]  {r["cofactors"][:24]:24s} {r["structure_papers"]}')
    print("\nTop 20 EUKARYOTIC:")
    for r in [x for x in grows if x["is_eukaryote"]][:20]:
        print(f'  {r["priority_score"]:>5}  {r["organism"]:7s} {r["gene"]:14s} '
              f'cof[{r["pdb_with_cofactor"]}] lig[{r["pdb_with_ligand"]}] '
              f'cplx[{r["pdb_with_complex"]}]  {r["cofactors"][:24]:24s} {r["structure_papers"]}')


if __name__ == "__main__":
    main()
