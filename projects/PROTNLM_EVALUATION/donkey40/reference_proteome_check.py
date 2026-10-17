#!/usr/bin/env python3
"""Evidence for which ProtNLM2 mammal proteomes get PAINT IBA or TreeGrafter.

TreeGrafter (GO_REF:0000118) annotates proteins outside PANTHER's reference
proteomes; reference-proteome proteins get PAINT IBA (GO_REF:0000033). For each
species below, this takes the ProtNLM2 accessions of that species from the
official accession list (sorted; at most --per-species of them, a disclosed
cap) and counts, from QuickGO, how many carry at least one IBA row and how many
at least one TreeGrafter row. It also checks two pairing questions for DONKEY40:
whether each donkey record and its horse partner (selection.yaml) are in the
same PANTHER family per UniProt, and the IBA count of the HORSE40 MTMR9 entry.

Output: reference_proteome_check.tsv and donkey40_pair_panther.tsv next to this
script, with the run date in a comment line.

Run:
  python3 projects/PROTNLM_EVALUATION/donkey40/reference_proteome_check.py
"""
from __future__ import annotations

import argparse
import csv
import io
import json
import os
import time
import urllib.parse
import urllib.request
from datetime import datetime, timezone

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
LIST_URL = ("https://ftp.ebi.ac.uk/pub/contrib/UniProt/ProtNLM2/"
            "List_of_UniProt_accessions_that_have_ProtNLM2_annotations.tsv")
QUICKGO = "https://www.ebi.ac.uk/QuickGO/services/annotation/search"
SPECIES = {"9796": "Equus caballus (horse)", "9793": "Equus asinus (donkey)",
           "9598": "Pan troglodytes (chimpanzee)", "9544": "Macaca mulatta (rhesus macaque)",
           "9823": "Sus scrofa (pig)", "9541": "Macaca fascicularis (crab-eating macaque)",
           "9483": "Callithrix jacchus (marmoset)"}
MTMR9_HORSE40 = "A0A9L0T3C1"


def get(url: str) -> str | None:
    for attempt in range(4):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "ai-gene-review/donkey40",
                                                       "Accept": "application/json"})
            with urllib.request.urlopen(req, timeout=120) as r:
                return r.read().decode()
        except Exception:
            time.sleep(2 ** attempt)
    return None


def with_ref(accs: list[str], ref: str) -> set[str]:
    hit: set[str] = set()
    for i in range(0, len(accs), 50):
        page = 1
        while True:
            q = urllib.parse.urlencode({"geneProductId": ",".join(accs[i:i + 50]), "reference": ref,
                                        "limit": 200, "page": page})
            txt = get(f"{QUICKGO}?{q}")
            if txt is None:
                raise SystemExit(f"QuickGO failed for {ref} batch {i}")
            d = json.loads(txt)
            hit |= {x["geneProductId"].split(":", 1)[1] for x in d.get("results", [])}
            if page >= (d.get("pageInfo") or {}).get("total", 1):
                break
            page += 1
            time.sleep(0.2)
    return hit


def panther(acc: str) -> str:
    txt = get(f"https://rest.uniprot.org/uniprotkb/{acc}?fields=xref_panther&format=tsv")
    if not txt:
        return "?"
    lines = txt.strip().split("\n")[1:]
    fams = sorted({p.split(":")[0] for p in (lines[0].rstrip(";").split(";") if lines else []) if p})
    return ";".join(fams)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--per-species", type=int, default=200)
    args = ap.parse_args()
    run = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    rows = list(csv.DictReader(io.StringIO(get(LIST_URL) or ""), delimiter="\t"))
    if not rows:
        raise SystemExit("could not fetch the ProtNLM2 accession list")
    out = []
    for taxid, name in SPECIES.items():
        accs = sorted(r["Entry"] for r in rows if r["Organism (ID)"] == taxid)
        sample = accs[:args.per_species]
        iba = with_ref(sample, "GO_REF:0000033")
        tg = with_ref(sample, "GO_REF:0000118")
        out.append({"taxid": taxid, "species": name, "protnlm2_records": len(accs),
                    "checked": len(sample), "with_iba": len(iba), "with_treegrafter": len(tg),
                    "with_both": len(iba & tg)})
        print(out[-1])
    with open(os.path.join(HERE, "reference_proteome_check.tsv"), "w", newline="") as fh:
        fh.write(f"# reference_proteome_check.py run {run}; ProtNLM2 list {LIST_URL}; "
                 f"first {args.per_species} accessions per species (sorted)\n")
        w = csv.DictWriter(fh, fieldnames=list(out[0]), delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(out)
    mtmr9 = len(with_ref([MTMR9_HORSE40], "GO_REF:0000033"))
    print(f"HORSE40 MTMR9 {MTMR9_HORSE40}: has IBA rows = {bool(mtmr9)}")
    pairs = []
    for rec in yaml.safe_load(open(os.path.join(HERE, "selection.yaml")))["records"]:
        dfam, hfam = panther(rec["donkey_accession"]), panther(rec["horse_accession"])
        pairs.append({"gene_symbol": rec["gene_symbol"], "donkey_accession": rec["donkey_accession"],
                      "donkey_panther": dfam, "horse_accession": rec["horse_accession"],
                      "horse_panther": hfam,
                      "same_family": bool((set(dfam.split(";")) & set(hfam.split(";"))) - {"", "?"})})
        time.sleep(0.1)
    with open(os.path.join(HERE, "donkey40_pair_panther.tsv"), "w", newline="") as fh:
        fh.write(f"# reference_proteome_check.py run {run}; PANTHER families from UniProt xrefs; "
                 f"HORSE40 MTMR9 {MTMR9_HORSE40} has IBA rows: {bool(mtmr9)}\n")
        w = csv.DictWriter(fh, fieldnames=list(pairs[0]), delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(pairs)
    print(f"pairs sharing a PANTHER family: {sum(p['same_family'] for p in pairs)}/{len(pairs)}")


if __name__ == "__main__":
    main()
