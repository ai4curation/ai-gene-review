#!/usr/bin/env python3
"""Resolve every WITH/FROM token on ADAMTSL5's IBA row and query each donor's own
evidence for the propagated GO term.

Fails loudly on a missing input or an empty UniProt record (a dead accession is a
silent false negative -- see campaign brief).
"""

import csv
import json
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

GOA = Path(__file__).resolve().parent.parent / "ADAMTSL5-goa.tsv"
UA = {"User-Agent": "ai-gene-review/ADAMTSL5 (cjmungall@lbl.gov)"}


def get_json(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as fh:
        return json.load(fh)


def uniprot_search(query, fields):
    url = (
        "https://rest.uniprot.org/uniprotkb/search?query="
        + urllib.parse.quote(query)
        + "&fields=" + fields
        + "&size=5"  # never size=1: an ambiguous xref is data, not an error
    )
    return get_json(url)["results"]


FIELDS = "accession,id,protein_name,gene_names,organism_name,length,reviewed,cc_function,xref_panther"


def describe(entry):
    acc = entry["primaryAccession"]
    name = entry.get("uniProtkbId", "?")
    desc = entry.get("proteinDescription", {})
    rec = desc.get("recommendedName") or {}
    pname = (rec.get("fullName") or {}).get("value")
    if not pname:
        sub = desc.get("submissionNames") or []
        pname = sub[0]["fullName"]["value"] if sub else "?"
    genes = ";".join(
        g.get("geneName", {}).get("value", "?") for g in entry.get("genes", [])
    ) or "-"
    return {
        "accession": acc,
        "entry_name": name,
        "protein_name": pname,
        "gene": genes,
        "organism": entry.get("organism", {}).get("scientificName", "?"),
        "length": entry.get("sequence", {}).get("length"),
        "reviewed": "Swiss-Prot" if entry.get("entryType", "").startswith("UniProtKB reviewed") else "TrEMBL",
    }


def resolve(token):
    """Return list of candidate dicts. Multi-hit is reported, never silently reduced."""
    if token.startswith("UniProtKB:"):
        acc = token.split(":", 1)[1]
        res = uniprot_search(f"accession:{acc}", FIELDS)
        if not res:
            raise SystemExit(
                f"FATAL: UniProt returned NOTHING for {token}. A dead/deleted accession "
                f"reads identically to a subunit with no annotations -- investigate at "
                f"https://rest.uniprot.org/uniprotkb/{acc}.json"
            )
        return [describe(e) for e in res]
    if token.startswith("PANTHER:"):
        return [{"accession": token, "entry_name": "PANTHER tree node",
                 "protein_name": "internal PANTHER tree node -- NOT a protein",
                 "gene": "-", "organism": "-", "length": None, "reviewed": "n/a"}]
    db, ident = token.split(":", 1)
    xref = {"MGI": "mgi", "RGD": "rgd", "FB": "flybase", "WB": "wormbase",
            "ZFIN": "zfin", "SGD": "sgd"}[db]
    if db == "MGI":
        ident = ident.split(":")[-1]  # MGI:MGI:109249 -> 109249; inner colon => HTTP 400
    res = uniprot_search(f"xref:{xref}-{ident}", FIELDS)
    if not res and db == "WB":
        # MEASURED: UniProt does NOT index the WBGene id (xref:wormbase-WBGene00003242
        # returns []); its WormBase xrefs are keyed on the CDS/sequence name (C37C3.6).
        # So resolve WBGene -> public gene symbol via the WormBase REST, then search by
        # symbol. Without this the token reads as "unresolvable", which is a false
        # negative, not a null result.
        label = get_json(
            f"https://rest.wormbase.org/rest/field/gene/{ident}/name"
        )["name"]["data"]["label"]
        # gene_exact, NOT gene: a fuzzy `gene:mig-6` also returns mig-10/mig-5/mig-14/
        # mig-18 and puts the WRONG entry first. An ambiguous head is the `size=1` trap
        # in a new guise -- the count must not rest on a fuzzy match.
        res = uniprot_search(
            f"gene_exact:{label} AND organism_id:6239 AND reviewed:true", FIELDS
        )
        if not res:
            raise SystemExit(
                f"FATAL: {token} resolved to WormBase symbol {label!r} but no reviewed "
                f"C. elegans UniProt entry matched. Investigate before treating this "
                f"token as unresolvable."
            )
    if not res:
        return [{"accession": token, "entry_name": "UNRESOLVED",
                 "protein_name": "no UniProt entry found for this xref",
                 "gene": "-", "organism": "-", "length": None, "reviewed": "n/a"}]
    return [describe(e) for e in res]


EXPERIMENTAL = {"EXP", "IDA", "IPI", "IMP", "IGI", "IEP", "HTP", "HDA", "HMP", "HGI", "HEP"}


def quickgo_evidence(gene_product_id, go_id):
    """What evidence does this donor itself carry for go_id (or a descendant)?"""
    url = (
        "https://www.ebi.ac.uk/QuickGO/services/annotation/search"
        f"?geneProductId={urllib.parse.quote(gene_product_id)}"
        f"&goId={urllib.parse.quote(go_id)}"
        "&goUsage=descendants&goUsageRelationships=is_a,part_of&limit=100"
    )
    data = get_json(url)
    hits = []
    for r in data.get("results", []):
        hits.append((r.get("goId"), r.get("goName"), r.get("goEvidence"),
                     r.get("reference"), r.get("assignedBy")))
    return hits


def main():
    if not GOA.exists():
        raise SystemExit(f"FATAL: missing {GOA}. Run: just fetch-gene human ADAMTSL5")

    with GOA.open() as fh:
        rows = [r for r in csv.DictReader(fh, delimiter="\t")]
    iba = [r for r in rows if r["GO EVIDENCE CODE"] == "IBA"]
    if len(iba) != 1:
        raise SystemExit(f"FATAL: expected exactly 1 IBA row, found {len(iba)}")
    row = iba[0]
    go_id = row["GO TERM"]
    tokens = row["WITH/FROM"].split("|")
    print(f"# IBA row: {go_id} {row['GO NAME']} ({row['QUALIFIER']})")
    print(f"# WITH/FROM token count (from GOA, authoritative): {len(tokens)}\n")

    out = []
    for tok in tokens:
        cands = resolve(tok)
        for c in cands:
            c["token"] = tok
        # Donor's own evidence for the propagated term.
        #
        # MEASURED: QuickGO's annotation-search `geneProductId` REJECTS MOD ids with
        # HTTP 400 ("contains invalid values") for every form tried -- MGI:MGI:109249,
        # MGI:109249, FB:FBgn0003137, FBgn0003137, WB:WBGene..., RGD:621241. It indexes
        # UniProtKB (+ComplexPortal/RNAcentral) only. So a MOD donor can only be queried
        # through its resolved UniProt accession.
        #
        # Never leave a token unqueried while printing "NONE" -- that is a silent
        # degradation masquerading as a null result. Unqueryable is its own state.
        gps = []
        if tok.startswith("PANTHER:"):
            note = "tree node -- not a gene product"
        else:
            reviewed = [c for c in cands if c["reviewed"] == "Swiss-Prot"]
            targets = reviewed or [c for c in cands if c["entry_name"] != "UNRESOLVED"]
            gps = ["UniProtKB:" + c["accession"] for c in targets]
            note = ("via reviewed accession" if reviewed
                    else ("via UNREVIEWED accession only -- weaker" if targets
                          else "UNRESOLVED -- cannot be dismissed, only deferred"))
        ev = []
        for gp in gps:
            ev.extend(quickgo_evidence(gp, go_id))
        queried = gps or None
        codes = sorted({e[2] for e in ev})
        exp = sorted({e[2] for e in ev} & EXPERIMENTAL)
        terms = sorted({(e[0], e[1] or "") for e in ev if e[2] in EXPERIMENTAL})
        rec = {
            "token": tok,
            "n_candidates": len(cands),
            "candidates": cands,
            "queried_as": queried,
            "query_note": note,
            "own_evidence_codes": codes,
            "own_experimental_codes": exp,
            "own_experimental_terms": terms,
        }
        out.append(rec)
        head = cands[0]
        flag = "  <-- MULTI-HIT" if len(cands) > 1 else ""
        print(f"{tok}")
        print(f"    -> {head['accession']} {head['entry_name']} [{head['reviewed']}] "
              f"{head['gene']} / {head['organism']} / {head['length']}aa{flag}")
        print(f"       {head['protein_name']}")
        if len(cands) > 1:
            for c in cands[1:]:
                print(f"       ALSO: {c['accession']} {c['entry_name']} [{c['reviewed']}] "
                      f"{c['gene']} {c['protein_name']}")
        state = "UNQUERYABLE" if queried is None else (codes or "NONE")
        print(f"       queried as: {queried}  [{note}]")
        print(f"       own evidence for {go_id}(+desc): {state}"
              f"  experimental: {exp or 'NONE'}")
        for t in terms:
            print(f"         exp term: {t[0]} {t[1]}")
        print()
        time.sleep(0.3)

    n_exp = sum(1 for r in out if r["own_experimental_codes"])
    n_prot = sum(1 for r in out if not r["token"].startswith("PANTHER:"))
    print(f"## tokens: {len(tokens)}   protein tokens: {n_prot}   "
          f"tokens whose donor carries its OWN experimental evidence for {go_id}: {n_exp}")

    dest = Path(__file__).resolve().parent / "withfrom_resolution.json"
    dest.write_text(json.dumps({"go_id": go_id, "n_tokens": len(tokens), "records": out}, indent=2))
    print(f"\nwrote {dest}")


if __name__ == "__main__":
    main()
