#!/usr/bin/env python3
"""Select DONKEY40: donkey proteins with ProtNLM2 GO output and TreeGrafter rows,
each paired with a horse ortholog that carries PAINT IBA rows.

Donkey (Equus asinus, NCBITaxon:9793) is not a PANTHER reference proteome, so
its proteins receive TreeGrafter (GO_REF:0000118) rather than PAINT IBA
(GO_REF:0000033). Horse (NCBITaxon:9796) is a reference proteome and receives
IBA. Pairing the two gives, on the same genes, three electronic sources to
compare: ProtNLM2 (donkey), TreeGrafter (donkey) and PAINT IBA (horse).

Steps, all from live services (no hard-coded results):
  1. donkey accessions from the official ProtNLM2 accession list (EBI FTP);
  2. ProtNLM2 predictions for each (UniProt /uniprotkb/protnlm API), keeping
     records with at least one GO prediction;
  3. TreeGrafter and IBA row counts per donkey accession (QuickGO);
  4. a horse ortholog per gene symbol: the HORSE40 accession when the gene is
     in that cohort, otherwise the UniProtKB horse entry (of up to 10 with the
     same exact gene name) with the most IBA rows;
  5. eligible = donkey has GO predictions and TreeGrafter rows, horse ortholog
     has IBA rows; one record per gene symbol; ranked by number of ProtNLM2 GO
     predictions, then TreeGrafter rows, then accession; first 40 taken.

Output: selection.yaml next to this script.

Run:
  python3 projects/PROTNLM_EVALUATION/donkey40/select_donkey40.py
"""
from __future__ import annotations

import csv
import io
import json
import os
import time
import urllib.parse
import urllib.request
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))
LIST_URL = ("https://ftp.ebi.ac.uk/pub/contrib/UniProt/ProtNLM2/"
            "List_of_UniProt_accessions_that_have_ProtNLM2_annotations.tsv")
QUICKGO = "https://www.ebi.ac.uk/QuickGO/services/annotation/search"
DONKEY, HORSE = "9793", "9796"
N = 40


def get(url: str) -> str:
    for attempt in range(4):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "ai-gene-review/donkey40"})
            with urllib.request.urlopen(req, timeout=120) as r:
                return r.read().decode()
        except Exception:
            if attempt == 3:
                raise
            time.sleep(2 ** attempt)


def quickgo_counts(accs: list[str], ref: str) -> dict:
    out: dict = {}
    for i in range(0, len(accs), 50):
        page = 1
        while True:
            q = urllib.parse.urlencode({"geneProductId": ",".join(accs[i:i + 50]),
                                        "reference": ref, "limit": 200, "page": page})
            d = json.loads(get(f"{QUICKGO}?{q}"))
            for x in d["results"]:
                k = x["geneProductId"].split(":", 1)[1]
                out[k] = out.get(k, 0) + 1
            if page >= d["pageInfo"]["total"]:
                break
            page += 1
    return out


def protnlm_go(acc: str) -> list[str]:
    d = json.loads(get(f"https://rest.uniprot.org/uniprotkb/protnlm/{acc}"))
    ids = []
    for ref in d.get("uniProtKBCrossReferences", []) or []:
        if ref.get("database") == "GO":
            ids.append(ref["id"])
    return sorted(set(ids))


def main() -> None:
    rows = list(csv.DictReader(io.StringIO(get(LIST_URL)), delimiter="\t"))
    donkey = [r for r in rows if r["Organism (ID)"] == DONKEY]
    horse40 = {}
    h40 = os.path.join(HERE, "..", "mammal-benchmark", "horse40.csv")
    for r in csv.DictReader(open(h40)):
        horse40[r["gene_symbol"].upper()] = r["accession"]

    go = {}
    for r in donkey:
        ids = protnlm_go(r["Entry"])
        if ids:
            go[r["Entry"]] = ids
    accs = sorted(go)
    tg = quickgo_counts(accs, "GO_REF:0000118")
    iba_donkey = quickgo_counts(accs, "GO_REF:0000033")

    cands = []
    for r in donkey:
        a = r["Entry"]
        if a not in go or not tg.get(a):
            continue
        gene = (r["Gene Names"].split() or [""])[0]
        if not gene:
            continue
        if gene.upper() in horse40:
            horse_choices = [horse40[gene.upper()]]
        else:
            q = urllib.parse.urlencode({"query": f"(gene_exact:{gene}) AND (organism_id:{HORSE})",
                                        "fields": "accession", "format": "tsv", "size": 10})
            horse_choices = [l for l in get(f"https://rest.uniprot.org/uniprotkb/search?{q}").split("\n")[1:] if l]
        if not horse_choices:
            continue
        hib = quickgo_counts(horse_choices, "GO_REF:0000033")
        best = max(horse_choices, key=lambda x: hib.get(x, 0))
        if not hib.get(best):
            continue
        cands.append({"donkey_accession": a, "gene_symbol": gene,
                      "protein_name": r["Protein names"].split(" (")[0],
                      "length": int(r["Length"]), "protnlm2_go": go[a],
                      "donkey_treegrafter_rows": tg[a],
                      "donkey_iba_rows": iba_donkey.get(a, 0),
                      "horse_accession": best, "horse_iba_rows": hib[best],
                      "horse_in_horse40": gene.upper() in horse40})
    cands.sort(key=lambda c: (-len(c["protnlm2_go"]), -c["donkey_treegrafter_rows"],
                              c["donkey_accession"]))
    seen, sel = set(), []
    for c in cands:
        if c["gene_symbol"].upper() in seen:
            continue
        seen.add(c["gene_symbol"].upper())
        sel.append(c)
    sel = sel[:N]
    out = os.path.join(HERE, "selection.yaml")
    with open(out, "w") as fh:
        fh.write("# Generated by select_donkey40.py; do not edit by hand.\n")
        fh.write(f"cohort: DONKEY40\nselected_on: '{date.today().isoformat()}'\n")
        fh.write(f"donkey_protnlm2_records: {len(donkey)}\n")
        fh.write(f"donkey_with_go_predictions: {len(go)}\n")
        fh.write(f"eligible: {len(cands)}\n")
        fh.write("records:\n")
        for i, c in enumerate(sel, 1):
            fh.write(f"  - order: {i}\n")
            for k, v in c.items():
                fh.write(f"    {k}: {json.dumps(v)}\n")
    print(f"{len(donkey)} donkey ProtNLM2 records, {len(go)} with GO, "
          f"{len(cands)} eligible, {len(sel)} selected -> {out}")


if __name__ == "__main__":
    main()
