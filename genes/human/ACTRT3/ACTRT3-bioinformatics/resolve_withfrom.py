#!/usr/bin/env python3
"""Resolve every WITH/FROM token in ACTRT3's GOA rows and query each source's own
evidence for the GO term it donated.

Builds source_entities FROM the GOA WITH/FROM field by construction (never by hand),
and asserts the per-row token counts match GOA.

Outputs withfrom.json + withfrom.tsv in this directory.
"""
import csv, json, sys, time, urllib.parse, urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
GOA = HERE.parent / "ACTRT3-goa.tsv"
UNIPROT = "https://rest.uniprot.org/uniprotkb/search"
QUICKGO = "https://www.ebi.ac.uk/QuickGO/services/annotation/search"
EXP = {"EXP", "IDA", "IPI", "IMP", "IGI", "IEP", "HTP", "HDA", "HMP", "HGI", "HEP"}

# db name in the GOA WITH/FROM token -> UniProt xref db for a `xref:<db>-<id>` query
XREF_DB = {
    "MGI": "mgi", "RGD": "rgd", "SGD": "sgd", "FB": "flybase", "WB": "wormbase",
    "PomBase": "pombase", "dictyBase": "dictybase", "CGD": "cgd",
}


def get(url, params):
    q = urllib.parse.urlencode(params)
    req = urllib.request.Request(f"{url}?{q}", headers={"Accept": "application/json"})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=60) as fh:
                return json.load(fh)
        except Exception as exc:  # network flake only; a persistent failure must be loud
            if attempt == 3:
                raise RuntimeError(f"GET failed after 4 tries: {url}?{q}") from exc
            time.sleep(2 * (attempt + 1))


def uniprot_search(query, size=5):
    d = get(UNIPROT, {"query": query, "size": size, "format": "json",
                      "fields": "accession,id,gene_names,protein_name,length,reviewed,organism_name"})
    out = []
    for r in d.get("results", []):
        genes = ",".join(
            g.get("geneName", {}).get("value", "")
            for g in r.get("genes", []) if g.get("geneName")
        )
        pn = r.get("proteinDescription", {}).get("recommendedName", {}).get("fullName", {}).get("value")
        if pn is None:
            sub = r.get("proteinDescription", {}).get("submissionNames", [])
            pn = sub[0]["fullName"]["value"] if sub else ""
        out.append({
            "accession": r["primaryAccession"],
            "entry_name": r.get("uniProtkbId", ""),
            "gene": genes,
            "protein_name": pn,
            "length": r.get("sequence", {}).get("length"),
            "reviewed": r.get("entryType", "").startswith("UniProtKB reviewed"),
            "organism": r.get("organism", {}).get("scientificName", ""),
        })
    return out


def resolve(token):
    """Return (kind, [candidate dicts], note). Never silently pick one of several."""
    db, _, ident = token.partition(":")
    if db == "UniProtKB":
        cands = uniprot_search(f"accession:{ident}", size=2)
        # liveness guard: a merged/dead accession returns a DIFFERENT protein or nothing
        live = [c for c in cands if c["accession"] == ident]
        if not live:
            return "protein", cands, f"DEAD_OR_MERGED: requested {ident}, got {[c['accession'] for c in cands] or 'nothing'}"
        return "protein", live, ""
    if db == "PANTHER":
        return "panther_node", [], "PANTHER internal tree node, not a protein"
    if db in XREF_DB:
        # MGI tokens arrive as MGI:MGI:87906 -> UniProt wants the bare number
        bare = ident.split(":")[-1] if db == "MGI" else ident
        # An `xref:` miss is not the same as an absent protein: WormBase gene ids are not
        # indexed under xref:wormbase-, so a free-text fallback is tried before reporting
        # UNRESOLVED. An unresolved token can only be deferred, never dismissed.
        for query, how in ((f"xref:{XREF_DB[db]}-{bare}", "xref"), (bare, "free-text")):
            cands = uniprot_search(query, size=5)
            if not cands:
                continue
            rev = [c for c in cands if c["reviewed"]]
            note = "" if how == "xref" else "resolved by free-text fallback, not xref"
            if rev:
                extra = "" if len(rev) == 1 else f"; MULTI: {len(rev)} reviewed hits"
                return "protein", rev, note + extra
            return "protein", cands, (note + "; " if note else "") + \
                "NO_REVIEWED_ENTRY: unreviewed (TrEMBL) fallback"
        return "protein", [], "UNRESOLVED"
    return "unknown", [], f"unhandled db {db!r}"


def quickgo_evidence(acc, go_id):
    d = get(QUICKGO, {"geneProductId": f"UniProtKB:{acc}", "goId": go_id,
                      "goUsage": "descendants",
                      "goUsageRelationships": "is_a,part_of", "limit": 100})
    hits = [{"goId": r["goId"], "goName": r.get("goName", ""), "ev": r["goEvidence"]}
            for r in d.get("results", [])]
    return hits


def main():
    rows = list(csv.DictReader(GOA.open(), delimiter="\t"))
    assert len(rows) == 10, f"expected 10 GOA rows, got {len(rows)}"
    out = []
    for i, r in enumerate(rows, start=1):
        tokens = [t for t in r["WITH/FROM"].split("|") if t]
        rec = {"row": i, "go_id": r["GO TERM"], "go_name": r["GO NAME"],
               "evidence": r["GO EVIDENCE CODE"], "qualifier": r["QUALIFIER"],
               "reference": r["REFERENCE"], "n_tokens": len(tokens),
               "tokens": tokens, "sources": []}
        if r["GO EVIDENCE CODE"] not in ("IBA", "ISS", "IEA"):
            out.append(rec); continue
        for tok in tokens:
            kind, cands, note = resolve(tok)
            entry = {"token": tok, "kind": kind, "note": note, "candidates": cands,
                     "own_evidence": None}
            if kind == "protein" and len(cands) == 1 and not note.startswith("DEAD"):
                ev = quickgo_evidence(cands[0]["accession"], r["GO TERM"])
                entry["own_evidence"] = ev
                entry["has_experimental"] = any(h["ev"] in EXP for h in ev)
            rec["sources"].append(entry)
        # assertion: source count must match GOA by construction
        assert len(rec["sources"]) == len(tokens)
        out.append(rec)

    (HERE / "withfrom.json").write_text(json.dumps(out, indent=2))

    with (HERE / "withfrom.tsv").open("w") as fh:
        w = csv.writer(fh, delimiter="\t")
        w.writerow(["row", "go_id", "evidence", "token", "kind", "accession",
                    "entry_name", "gene", "organism", "length", "reviewed",
                    "own_terms_for_donated_go", "has_own_experimental", "note"])
        for rec in out:
            for s in rec["sources"]:
                c = s["candidates"][0] if len(s["candidates"]) == 1 else None
                terms = ";".join(f"{h['goId']}/{h['ev']}" for h in (s["own_evidence"] or []))
                w.writerow([rec["row"], rec["go_id"], rec["evidence"], s["token"], s["kind"],
                            c["accession"] if c else "|".join(x["accession"] for x in s["candidates"]),
                            c["entry_name"] if c else "",
                            c["gene"] if c else "|".join(x["gene"] for x in s["candidates"]),
                            c["organism"] if c else "",
                            c["length"] if c else "", c["reviewed"] if c else "",
                            terms, s.get("has_experimental", ""), s["note"]])
    print(f"wrote {HERE/'withfrom.tsv'}")


if __name__ == "__main__":
    main()
