"""Resolve every WITH/FROM token in AGFG1-goa.tsv and, for each IBA/IEA row, ask
what evidence the named donor itself carries for the propagated term.

Two separate questions, kept separate on purpose (see the campaign brief):
  provenance  - who the donor is (bookkeeping; supports no verdict on its own);
  circularity - whether the donor's own evidence for THAT EXACT term is itself
                an IBA (this is what can carry a REMOVE).

``source_entities`` for the review YAML is built from the GOA WITH/FROM column
programmatically and asserted against it, never by hand.

Usage: uv run python donors.py
"""

from __future__ import annotations

import csv
import json
import pathlib
import urllib.parse
import urllib.request

import quickgo

HERE = pathlib.Path(__file__).parent
GOA = HERE.parent / "AGFG1-goa.tsv"
OUT = HERE / "donors.json"

EXPERIMENTAL = {
    "EXP",
    "IDA",
    "IPI",
    "IMP",
    "IGI",
    "IEP",
    "HTP",
    "HDA",
    "HMP",
    "HGI",
    "HEP",
}


def uniprot(acc: str) -> dict:
    url = (
        f"https://rest.uniprot.org/uniprotkb/{acc}.json"
        "?fields=accession,id,protein_name,gene_names,organism_name,length,cc_function"
    )
    with urllib.request.urlopen(url) as fh:
        assert fh.status == 200, f"HTTP {fh.status} for {url}"
        d = json.load(fh)
    # A merged/secondary accession returns HTTP 200 for a DIFFERENT protein.
    assert d["primaryAccession"] == acc, (
        f"{acc} resolved to {d['primaryAccession']} ({d.get('uniProtkbId')})"
    )
    return d


def uniprot_by_xref(db: str, ident: str) -> list[dict]:
    """Look a MOD id up through UniProt's xref index. Returns ALL hits: an
    ambiguous cross-reference is data, not an error."""
    q = urllib.parse.urlencode(
        {
            "query": f"xref:{db}-{ident}",
            "fields": "accession,id,protein_name,gene_names,organism_name,length",
            "format": "json",
            "size": "10",
        }
    )
    url = f"https://rest.uniprot.org/uniprotkb/search?{q}"
    with urllib.request.urlopen(url) as fh:
        assert fh.status == 200, f"HTTP {fh.status} for {url}"
        return json.load(fh)["results"]


def describe(entry: dict) -> str:
    genes = ",".join(g.get("geneName", {}).get("value", "?") for g in entry.get("genes", []))
    name = (
        entry.get("proteinDescription", {})
        .get("recommendedName", {})
        .get("fullName", {})
        .get("value")
    )
    if not name:
        sub = entry.get("proteinDescription", {}).get("submissionNames") or []
        name = sub[0]["fullName"]["value"] if sub else "?"
    status = (
        "Swiss-Prot"
        if entry["entryType"].startswith("UniProtKB reviewed")
        else "TrEMBL"
    )
    return (
        f"{entry['primaryAccession']} {entry['uniProtkbId']} [{status}] "
        f"{entry['organism']['scientificName']} gene={genes or '-'} "
        f"len={entry['sequence']['length']} :: {name}"
    )


def goa_rows() -> list[dict]:
    with GOA.open() as fh:
        rows = list(csv.DictReader(fh, delimiter="\t"))
    assert rows, "empty GOA file"
    return rows


def donor_evidence(accessions: list[str], go_id: str) -> list[dict]:
    """Evidence the donor itself carries for go_id or its descendants.

    QuickGO's ``geneProductId`` rejects every MOD id form (MGI:, FB:, RGD:, WB:)
    with HTTP 400, so MOD tokens must first be mapped to UniProt accessions -
    see probe_ids.py for the measured evidence, including a positive control.

    Returns dicts, not joined strings: a GO id contains a colon, so splitting a
    joined record on ':' silently reads the term number where the evidence code
    should be. (That bug produced "non-EXP only" for rows carrying IMP.)
    """
    assert accessions, "no accessions to query - would silently report zero"
    seen = set()
    out: list[dict] = []
    for acc in accessions:
        anns = quickgo.annotations(
            geneProductId=f"UniProtKB:{acc}",
            goId=go_id,
            goUsage="descendants",
            goUsageRelationships="is_a,part_of",
        )
        for a in anns:
            rec = {
                "accession": acc,
                "go_id": a["goId"],
                "evidence": a["goEvidence"],
                "reference": a["reference"],
            }
            key = tuple(sorted(rec.items()))
            if key not in seen:
                seen.add(key)
                out.append(rec)
    return sorted(out, key=lambda r: (r["accession"], r["go_id"], r["evidence"], r["reference"]))


def main() -> None:
    rows = goa_rows()
    print(f"{GOA.name}: {len(rows)} rows, {len({tuple(r.items()) for r in rows})} distinct")

    tokens: dict[str, list[str]] = {}
    for r in rows:
        wf = (r["WITH/FROM"] or "").strip()
        if wf:
            tokens.setdefault(wf, []).append(f"{r['GO TERM']}/{r['GO EVIDENCE CODE']}")

    # Flat token set, built FROM the file.
    flat = sorted({t for wf in tokens for t in wf.split("|")})
    print(f"\n{len(flat)} distinct WITH/FROM tokens across {len(tokens)} distinct fields")

    resolved: dict[str, object] = {}
    accs: dict[str, list[str]] = {}  # token -> UniProt accessions to query
    for tok in flat:
        db, _, ident = tok.partition(":")
        if db == "UniProtKB":
            resolved[tok] = describe(uniprot(ident))
            accs[tok] = [ident]
        elif db in ("MGI", "FB"):
            # MGI tokens arrive as MGI:MGI:nnn; UniProt's xref index wants the
            # bare number - a query containing the inner colon returns HTTP 400.
            xdb = "mgi" if db == "MGI" else "flybase"
            hits = uniprot_by_xref(xdb, ident.split(":")[-1])
            resolved[tok] = [describe(h) for h in hits] or ["NO UNIPROT HIT"]
            accs[tok] = [h["primaryAccession"] for h in hits]
            reviewed = [
                h["primaryAccession"]
                for h in hits
                if h["entryType"].startswith("UniProtKB reviewed")
            ]
            # "reviewed" is a substring of "unreviewed": test startswith.
            print(
                f"      -> {len(hits)} hit(s), {len(reviewed)} Swiss-Prot "
                f"{reviewed or '(none - falling back to unreviewed entries)'}"
            )
        else:
            resolved[tok] = f"not a protein id ({db})"
        print(f"  {tok}\n      {resolved[tok]}")

    # Donor evidence per (term, donor) pair, for the propagated rows only.
    print("\ndonor evidence for the propagated term (QuickGO, goUsage=descendants):")
    donor_ev: dict[str, dict[str, list[str]]] = {}
    for r in rows:
        wf = (r["WITH/FROM"] or "").strip()
        if r["GO EVIDENCE CODE"] not in ("IBA", "IEA", "ISS", "ISO") or not wf:
            continue
        go_id = r["GO TERM"]
        for tok in wf.split("|"):
            db = tok.split(":")[0]
            if db not in ("MGI", "FB", "UniProtKB", "RGD", "SGD", "WB", "ZFIN"):
                continue
            key = f"{go_id}|{tok}"
            if key in donor_ev:
                continue
            ev = donor_evidence(accs[tok], go_id)
            # The exact-term question is separate from the descendant question:
            # a donor can hold a descendant by IDA and nothing at the term itself.
            exact = [r for r in ev if r["go_id"] == go_id]
            exp = sorted({r["evidence"] for r in exact} & EXPERIMENTAL)
            exp_desc = sorted({r["evidence"] for r in ev} & EXPERIMENTAL)
            donor_ev[key] = {
                "queried_accessions": accs[tok],
                "annotations": ev,
                "experimental_codes_at_exact_term": exp,
                "experimental_codes_incl_descendants": exp_desc,
            }
            if exp:
                flag = f"OWN EXPERIMENTAL EVIDENCE AT THE EXACT TERM: {exp}"
            elif exp_desc:
                flag = f"experimental only at a DESCENDANT: {exp_desc}"
            elif ev:
                flag = "no experimental evidence (inferred rows only)"
            else:
                flag = "NO annotation to this term at all"
            print(f"  {go_id} <- {tok}: {flag}")
            for r in ev:
                print(
                    f"        {r['accession']} {r['go_id']} {r['evidence']} "
                    f"{r['reference']}"
                )

    OUT.write_text(
        json.dumps(
            {"withfrom_fields": tokens, "resolved": resolved, "donor_evidence": donor_ev},
            indent=2,
            sort_keys=True,
        )
        + "\n"
    )
    print(f"\nwrote {OUT}")


if __name__ == "__main__":
    main()
