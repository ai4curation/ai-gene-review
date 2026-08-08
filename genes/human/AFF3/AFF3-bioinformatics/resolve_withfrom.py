#!/usr/bin/env python3
"""Resolve every WITH/FROM token on every IBA row of AFF3's GOA, and query each
donor's own evidence for the propagated GO term.

Two questions per token, kept separate (campaign brief):
  1. PROVENANCE -- what entity is this token, and is it the recipient itself?
  2. CIRCULARITY -- does that entity carry its own EXPERIMENTAL annotation for the
     propagated term, and if so *which* term?

Fails loudly on a missing input, a dead accession, a merged accession
(``primaryAccession`` != requested) or a silently-truncated query.

Usage:
    uv run python genes/human/AFF3/AFF3-bioinformatics/resolve_withfrom.py
"""

from __future__ import annotations

import csv
import json
import time
import urllib.parse
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
GOA = HERE.parent / "AFF3-goa.tsv"
SUBJECT_ACC = "P51826"  # AFF3, the recipient
UA = {"User-Agent": "ai-gene-review/AFF3 (cjmungall@lbl.gov)"}

FIELDS = "accession,id,protein_name,gene_names,organism_name,length,reviewed,xref_panther"
EXPERIMENTAL = {"EXP", "IDA", "IPI", "IMP", "IGI", "IEP", "HTP", "HDA", "HMP", "HGI", "HEP"}


def get_json(url: str) -> dict:
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=90) as fh:
        return json.load(fh)


def uniprot_search(query: str) -> list[dict]:
    """Never size=1 -- an ambiguous xref is data, not an error (campaign brief)."""
    url = (
        "https://rest.uniprot.org/uniprotkb/search?query="
        + urllib.parse.quote(query)
        + "&fields=" + FIELDS
        + "&size=10"
    )
    return get_json(url)["results"]


def is_reviewed(entry: dict) -> bool:
    # "reviewed" is a SUBSTRING of "unreviewed" -- must anchor (campaign brief).
    return entry.get("entryType", "").startswith("UniProtKB reviewed")


def describe(entry: dict) -> dict:
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
        "accession": entry["primaryAccession"],
        "entry_name": entry.get("uniProtkbId", "?"),
        "protein_name": pname,
        "gene": genes,
        "organism": entry.get("organism", {}).get("scientificName", "?"),
        "length": entry.get("sequence", {}).get("length"),
        "reviewed": "Swiss-Prot" if is_reviewed(entry) else "TrEMBL",
    }


def resolve(token: str) -> list[dict]:
    """Return candidate dicts. Multi-hit is reported, never silently reduced."""
    if token.startswith("PANTHER:"):
        return [{
            "accession": token, "entry_name": "PANTHER tree node",
            "protein_name": "internal PANTHER tree node -- NOT a protein",
            "gene": "-", "organism": "-", "length": None, "reviewed": "n/a",
        }]
    if token.startswith("UniProtKB:"):
        acc = token.split(":", 1)[1]
        res = uniprot_search(f"accession:{acc}")
        if not res:
            raise SystemExit(
                f"FATAL: UniProt returned NOTHING for {token}. A dead/deleted accession "
                f"reads identically to an entity with no annotations."
            )
        # A MERGED accession returns HTTP 200 for a DIFFERENT protein; only
        # primaryAccession reveals it (campaign brief).
        if not any(e["primaryAccession"] == acc for e in res):
            raise SystemExit(
                f"FATAL: {token} resolved to {[e['primaryAccession'] for e in res]} -- "
                f"the requested accession is not the primaryAccession of any hit. "
                f"This is the merged/secondary-accession trap."
            )
        return [describe(e) for e in res]

    db, ident = token.split(":", 1)
    xref = {"MGI": "mgi", "RGD": "rgd", "FB": "flybase", "WB": "wormbase",
            "ZFIN": "zfin", "SGD": "sgd", "TAIR": "araport"}[db]
    if db == "MGI":
        ident = ident.split(":")[-1]  # MGI:MGI:106927 -> 106927; inner colon => HTTP 400
    res = uniprot_search(f"xref:{xref}-{ident}")
    if not res:
        return [{
            "accession": token, "entry_name": "UNRESOLVED",
            "protein_name": "no UniProt entry found for this xref",
            "gene": "-", "organism": "-", "length": None, "reviewed": "n/a",
        }]
    return [describe(e) for e in res]


def quickgo_evidence(gene_product_id: str, go_id: str) -> list[tuple]:
    """What evidence does this donor itself carry for go_id (or a descendant)?"""
    url = (
        "https://www.ebi.ac.uk/QuickGO/services/annotation/search"
        f"?geneProductId={urllib.parse.quote(gene_product_id)}"
        f"&goId={urllib.parse.quote(go_id)}"
        "&goUsage=descendants&goUsageRelationships=is_a,part_of&limit=100"
    )
    data = get_json(url)
    results = data.get("results", [])
    # Compare against len(results), never a page-size constant: if the service
    # CLAMPS rather than errors, a constant-based guard sails past (campaign brief).
    n = data.get("numberOfHits")
    if n is not None and n > len(results):
        raise SystemExit(
            f"FATAL: silent truncation for {gene_product_id} / {go_id}: "
            f"numberOfHits={n} but {len(results)} results returned. Paginate."
        )
    return [
        (r.get("goId"), r.get("goName"), r.get("goEvidence"),
         r.get("reference"), r.get("assignedBy"))
        for r in results
    ]


def main() -> None:
    if not GOA.exists():
        raise SystemExit(f"FATAL: missing {GOA}. Run: just fetch-gene human AFF3")

    with GOA.open() as fh:
        rows = list(csv.DictReader(fh, delimiter="\t"))
    iba = [r for r in rows if r["GO EVIDENCE CODE"] == "IBA"]
    if not iba:
        raise SystemExit("FATAL: no IBA rows found -- did the GOA schema change?")

    cache: dict[str, list[dict]] = {}
    out = []
    for row in iba:
        go_id = row["GO TERM"]
        tokens = row["WITH/FROM"].split("|")
        print(f"\n{'=' * 78}\n# {go_id} {row['GO NAME']}  ({row['QUALIFIER']}, IBA)")
        print(f"# WITH/FROM tokens (from GOA, authoritative): {len(tokens)}\n")
        recs = []
        for tok in tokens:
            if tok not in cache:
                cache[tok] = resolve(tok)
                time.sleep(0.2)
            cands = cache[tok]

            gps: list[str] = []
            if tok.startswith("PANTHER:"):
                note = "tree node -- not a gene product"
            else:
                reviewed = [c for c in cands if c["reviewed"] == "Swiss-Prot"]
                targets = reviewed or [c for c in cands if c["entry_name"] != "UNRESOLVED"]
                gps = ["UniProtKB:" + c["accession"] for c in targets]
                note = ("via reviewed accession" if reviewed
                        else ("via UNREVIEWED accession only -- weaker" if targets
                              else "UNRESOLVED -- cannot be dismissed, only deferred"))
            ev: list[tuple] = []
            for gp in gps:
                ev.extend(quickgo_evidence(gp, go_id))
                time.sleep(0.2)

            codes = sorted({e[2] for e in ev})
            exp = sorted({e[2] for e in ev} & EXPERIMENTAL)
            exp_terms = sorted({(e[0], e[1] or "") for e in ev if e[2] in EXPERIMENTAL})
            self_ref = any(c["accession"] == SUBJECT_ACC for c in cands)

            rec = {
                "token": tok,
                "n_candidates": len(cands),
                "candidates": cands,
                "queried_as": gps or None,
                "query_note": note,
                "is_recipient_itself": self_ref,
                "own_evidence_codes": codes,
                "own_experimental_codes": exp,
                "own_experimental_terms": exp_terms,
            }
            recs.append(rec)

            head = cands[0]
            print(f"{tok}")
            print(f"    -> {head['accession']} {head['entry_name']} [{head['reviewed']}] "
                  f"{head['gene']} / {head['organism']} / {head['length']}aa"
                  + ("  <-- MULTI-HIT" if len(cands) > 1 else "")
                  + ("  <-- IS THE RECIPIENT ITSELF" if self_ref else ""))
            print(f"       {head['protein_name']}")
            for c in cands[1:]:
                print(f"       ALSO: {c['accession']} {c['entry_name']} [{c['reviewed']}] "
                      f"{c['gene']} {c['protein_name']}")
            state = "UNQUERYABLE" if not gps else (codes or "NONE")
            print(f"       queried as: {gps or None}  [{note}]")
            print(f"       own evidence for {go_id}(+desc): {state}   experimental: {exp or 'NONE'}")
            for t in exp_terms:
                print(f"         exp term: {t[0]} {t[1]}")

        n_prot = sum(1 for r in recs if not r["token"].startswith("PANTHER:"))
        n_exp = sum(1 for r in recs if r["own_experimental_codes"])
        print(f"\n## {go_id}: {len(tokens)} tokens, {n_prot} protein tokens, "
              f"{n_exp} donors carrying their OWN experimental evidence for the term")
        out.append({
            "go_id": go_id,
            "go_name": row["GO NAME"],
            "qualifier": row["QUALIFIER"],
            "withfrom_raw": row["WITH/FROM"],
            "n_tokens": len(tokens),
            "n_protein_tokens": n_prot,
            "n_donors_with_own_experimental": n_exp,
            "records": recs,
        })

    dest = HERE / "withfrom_resolution.json"
    dest.write_text(json.dumps({"subject": SUBJECT_ACC, "rows": out}, indent=2))
    print(f"\nwrote {dest}")


if __name__ == "__main__":
    main()
