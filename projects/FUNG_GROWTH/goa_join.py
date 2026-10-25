#!/usr/bin/env python3
"""Join FUNG-GROWTH plate calls to GOA for the species reviewed in this repo.

For each reviewed species, fetch from QuickGO every GOA annotation to the GO
terms mapped to FUNG-GROWTH carbon sources by build_go_map.py, in two tiers:

  process   the substrate's catabolic process (carbon_source_go_map.tsv),
            with is_a/part_of descendants
  activity  substrate-specific enzyme activities, binding or polymer
            breakdown (carbon_source_go_activity_map.tsv), with the term
            scope (exact or descendants) given in that file

and set each annotation beside the plate call for that species.

A row is FLAGGED when the annotation asserts the process (not a NOT
qualifier) and the plate is a killer call: the strain grows no better than on
its no-carbon control on a substrate comparable fungi use. FLAGGED rows are
split by evidence:

  automated     IEA (electronic mappings: InterPro2GO, EC2GO, ARBA, UniRule ...)
  phylogenetic  IBA (PAINT ancestral-node assertion; a curator judgement)
  sequence      ISS, ISO, ISA, ISM, IGC, RCA
  experimental  EXP, IDA, IPI, IMP, IGI, IEP and the HT codes
  author        TAS, NAS, IC, ND

A flag is a prompt to look, not a verdict. An organism can carry a working
enzyme for a process and still fail a plate test (uptake, regulation,
germination, plate chemistry), so experimental rows in particular need the
paper read before anything is changed.

Writes:
  data/goa_carbon_annotations.tsv  every fetched annotation with the plate call
  data/goa_killer_flags.tsv        the FLAGGED subset
  data/goa_species_process.tsv     species x process: plate call and annotation counts
"""

from __future__ import annotations

import csv
import json
import sys
import time
import urllib.parse
import urllib.request
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).parent
DATA = HERE / "data"
QUICKGO = "https://www.ebi.ac.uk/QuickGO/services/annotation/search"

# FUNG-GROWTH strain -> (repo species dir, NCBI taxon id from the repo's own
# *-uniprot.txt OX lines). Species-level ids are queried with
# taxonUsage=descendants so strain-level GOA rows are included.
SPECIES = {
    "Schizosaccharomyces pombe 972h-": ("SCHPO", 284812),
    "Saccharomyces cerevisiae S288C": ("yeast", 559292),
    "Candida albicans SC5314": ("CANAL", 237561),
    "Ustilago maydis": ("MYCMD", 5270),
    "Penicillium rubens Wisconsin 54-1255": ("PENCH", 5076),
    "Neurospora crassa OR74A": ("NEUCR", 367110),
    "Aspergillus nidulans FGSC A4": ("EMENI", 227321),
    "Aspergillus niger CBS 513.88": ("ASPNG", 5061),
    "Aspergillus oryzae RIB40": ("ASPOR", 510516),
    "Trichoderma reesei": ("HYPJE", 51453),
    "Pyricularia oryzae Guy11": ("PYROR", 318829),
}

EVIDENCE_CLASS = {
    "IEA": "automated",
    "IBA": "phylogenetic",
    **{c: "sequence" for c in ("ISS", "ISO", "ISA", "ISM", "IGC", "RCA")},
    **{c: "experimental" for c in ("EXP", "IDA", "IPI", "IMP", "IGI", "IEP",
                                   "HTP", "HDA", "HMP", "HGI", "HEP")},
    **{c: "author" for c in ("TAS", "NAS", "IC", "ND")},
}


def get(url: str, retries: int = 4):
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(url, timeout=120) as r:
                return json.loads(r.read())
        except Exception as exc:
            if attempt == retries - 1:
                raise
            print(f"retry ({exc})", file=sys.stderr)
            time.sleep(2 ** (attempt + 1))


def fetch(taxon: int, go_id: str, usage: str = "descendants") -> list[dict]:
    out, page = [], 1
    while True:
        q = urllib.parse.urlencode({
            "taxonId": taxon, "taxonUsage": "descendants",
            "goId": go_id, "goUsage": usage,
            "includeFields": "goName,taxonName", "limit": 100, "page": page,
        })
        res = get(f"{QUICKGO}?{q}")
        out += res["results"]
        if page >= res["pageInfo"]["total"]:
            return out
        page += 1


def with_from(a: dict) -> str:
    return "|".join(",".join(f"{x['db']}:{x['id']}" for x in g["connectedXrefs"])
                    for g in (a.get("withFrom") or []))


def plate_calls() -> dict[tuple[str, str], dict]:
    """(strain, carbon source) -> rating, control, delta, call, killer basis."""
    killers = {(k["strain"], k["carbon_source"]): k["basis"]
               for k in csv.DictReader(open(DATA / "killer_phenotypes.tsv"), delimiter="\t")}
    calls = {}
    for r in csv.DictReader(open(DATA / "fung_growth_matrix.tsv"), delimiter="\t"):
        if r["strain"] not in SPECIES or r["no carbon source"] == "":
            continue
        base = int(r["no carbon source"])
        for src, v in r.items():
            if src in ("strain", "no carbon source") or v == "":
                continue
            d = int(v) - base
            call = "NO_GROWTH" if d <= 0 else "WEAK" if d <= 2 else "GROWTH"
            calls[(r["strain"], src)] = {"rating": int(v), "control": base, "delta": d, "call": call,
                                         "killer": killers.get((r["strain"], src), "")}
    return calls


def queries() -> list[dict]:
    """One query per (tier, GO term), with the carbon sources it speaks to."""
    q: dict[tuple[str, str], dict] = {}
    for r in csv.DictReader(open(DATA / "carbon_source_go_map.tsv"), delimiter="\t"):
        if r["status"] == "OK":
            e = q.setdefault(("process", r["go_id"]), {"tier": "process", "go_id": r["go_id"],
                                                       "label": r["go_label"], "usage": "descendants",
                                                       "sources": []})
            e["sources"].append(r["carbon_source"])
    for r in csv.DictReader(open(DATA / "carbon_source_go_activity_map.tsv"), delimiter="\t"):
        if r["status"] == "OK":
            e = q.setdefault(("activity", r["go_id"]), {"tier": "activity", "go_id": r["go_id"],
                                                        "label": r["go_label"], "usage": r["go_usage"],
                                                        "sources": []})
            e["sources"].append(r["carbon_source"])
    return list(q.values())


def main() -> None:
    qs = queries()
    calls = plate_calls()
    reviewed = {(p.parent.parent.name, p.name.removesuffix("-ai-review.yaml"))
                for p in (HERE.parent.parent / "genes").glob("*/*/*-ai-review.yaml")}

    rows, summary = [], []
    for strain, (sp, taxon) in SPECIES.items():
        for qd in qs:
            annots = fetch(taxon, qd["go_id"], qd["usage"])
            print(f"{sp:6} {qd['tier']:8} {qd['go_id']} {qd['label']:38} {len(annots)}", file=sys.stderr)
            plates = [(s_, calls.get((strain, s_))) for s_ in qd["sources"]]
            plates = [(s_, c) for s_, c in plates if c]
            plate_txt = "; ".join(f"{s_}={c['rating']}/{c['control']} {c['call']}" for s_, c in plates)
            killer_plates = "; ".join(s_ for s_, c in plates if c["killer"])
            pos = []
            for a in annots:
                ev = a["goEvidence"]
                negated = a["qualifier"].startswith("NOT")
                row = {
                    "species": sp, "strain": strain, "tier": qd["tier"], "query_id": qd["go_id"],
                    "query_term": qd["label"], "query_scope": qd["usage"],
                    "plates": plate_txt, "killer_plates": killer_plates,
                    "gene_product": a["geneProductId"], "symbol": a.get("symbol") or "",
                    "has_review": "yes" if (sp, a.get("symbol") or "") in reviewed else "",
                    "qualifier": a["qualifier"], "go_id": a["goId"], "go_name": a.get("goName") or "",
                    "evidence": ev, "evidence_class": EVIDENCE_CLASS.get(ev, "other"),
                    "reference": a.get("reference") or "", "with_from": with_from(a),
                    "assigned_by": a.get("assignedBy") or "", "taxon": a.get("taxonId"),
                    "flag": "FLAGGED" if killer_plates and not negated else "",
                }
                rows.append(row)
                if not negated:
                    pos.append(row)
            classes = ["automated", "phylogenetic", "sequence", "experimental", "author", "other"]
            summary.append([sp, qd["tier"], qd["go_id"], qd["label"], qd["usage"], plate_txt, killer_plates,
                            len({r["gene_product"] for r in pos}),
                            *(sum(r["evidence_class"] == c for r in pos) for c in classes),
                            sum(r["qualifier"].startswith("NOT") for r in annots)])

    cols = list(rows[0]) if rows else []
    for name, subset in (("goa_carbon_annotations.tsv", rows),
                         ("goa_killer_flags.tsv", [r for r in rows if r["flag"]])):
        with open(DATA / name, "w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=cols, delimiter="\t")
            w.writeheader()
            w.writerows(sorted(subset, key=lambda r: (r["species"], r["tier"], r["query_term"],
                                                      r["symbol"], r["go_id"], r["evidence"])))
    with open(DATA / "goa_species_process.tsv", "w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t")
        w.writerow(["species", "tier", "query_id", "query_term", "query_scope", "plates", "killer_plates",
                    "n_gene_products", "automated", "phylogenetic", "sequence", "experimental", "author",
                    "other", "n_not"])
        w.writerows(summary)

    flagged = [r for r in rows if r["flag"]]
    print(f"{len(rows)} annotations fetched; {len(flagged)} FLAGGED "
          f"({sum(r['evidence_class'] == 'automated' for r in flagged)} IEA)")


if __name__ == "__main__":
    main()
