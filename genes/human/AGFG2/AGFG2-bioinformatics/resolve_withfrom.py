#!/usr/bin/env python3
"""Resolve every WITH/FROM token in AGFG2's GOA file and query each donor's own
evidence for the term it is donating.

Two separate questions, kept separate on purpose:

1. *Provenance* — what entity is each WITH/FROM token?  (bookkeeping; on its own
   this supports no verdict)
2. *Donor evidence* — does that entity itself hold an experimental annotation to
   the term being propagated, and to **which** term?  A propagation that lands
   above its donor, or whose donors carry only the same inference, are different
   defects.

The ``source_entities`` lists in the review YAML are generated from this
script's output so they cannot drift from the GOA field.
"""

from __future__ import annotations

import csv
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from common import (  # noqa: E402
    EXPERIMENTAL_CODES,
    is_reviewed,
    quickgo_annotations,
    uniprot_entry,
    uniprot_search,
    withfrom_tokens,
)

HERE = pathlib.Path(__file__).parent
GOA = HERE.parent / "AGFG2-goa.tsv"
SUBJECT = "O95081"

# MOD-id -> UniProt resolution.  QuickGO's geneProductId rejects every MOD id
# form with HTTP 400, and UniProt's xref indexes want the *bare* number for MGI
# (a query containing the inner colon returns HTTP 400), so both are handled here.
XREF_DB = {"MGI": "mgi", "FB": "flybase", "SGD": "sgd", "RGD": "rgd", "WB": "wormbase"}


def resolve_token(token: str) -> dict:
    """Resolve one db:id token.  Never returns a single confident answer for an
    ambiguous cross-reference: all candidates are reported."""
    db, _, ident = token.partition(":")
    rec: dict = {"token": token, "db": db, "id": ident}

    if db == "UniProtKB":
        e = uniprot_entry(ident, "accession,id,protein_name,gene_names,organism_name,length,reviewed")
        rec.update(
            kind="protein",
            accessions=[ident],
            entry_name=e["uniProtkbId"],
            reviewed=is_reviewed(e),
            length=e["sequence"]["length"],
            organism=e["organism"]["scientificName"],
            gene=[g.get("geneName", {}).get("value") for g in e.get("genes", [])],
            name=(e.get("proteinDescription", {}).get("recommendedName", {})
                  .get("fullName", {}).get("value")),
            is_self=(ident == SUBJECT),
        )
        return rec

    if db == "PANTHER":
        rec.update(kind="panther_node", note="internal PANTHER tree node, not a protein")
        return rec

    if db == "InterPro":
        rec.update(kind="interpro_signature", note="InterPro signature, not a protein")
        return rec

    if db in XREF_DB:
        # MGI arrives as MGI:MGI:1333754 -> the xref index wants the bare number.
        bare = ident.split(":")[-1]
        hits = uniprot_search(
            f"xref:{XREF_DB[db]}-{bare}",
            "accession,id,protein_name,gene_names,organism_name,length,reviewed",
            size=25,
        )
        if not hits:
            rec.update(kind="unresolved", note=f"no UniProt entry indexes {db}:{bare}")
            return rec
        cands = [
            {
                "accession": h["primaryAccession"],
                "entry_name": h["uniProtkbId"],
                "reviewed": is_reviewed(h),
                "length": h["sequence"]["length"],
                "organism": h["organism"]["scientificName"],
                "gene": [g.get("geneName", {}).get("value") for g in h.get("genes", [])],
                "name": (h.get("proteinDescription", {}).get("recommendedName", {})
                         .get("fullName", {}).get("value")
                         or h.get("proteinDescription", {}).get("submissionNames", [{}])[0]
                         .get("fullName", {}).get("value")),
            }
            for h in hits
        ]
        reviewed = [c for c in cands if c["reviewed"]]
        rec.update(
            kind="protein",
            n_candidates=len(cands),
            candidates=cands,
            reviewed_candidates=[c["accession"] for c in reviewed],
            has_reviewed=bool(reviewed),
            # For QuickGO we query every candidate, not just one: a size=1 pick
            # converts an ambiguity into a confident wrong answer.
            accessions=[c["accession"] for c in cands],
        )
        return rec

    rec.update(kind="unknown_namespace")
    return rec


def donor_evidence(accessions: list[str], go_id: str) -> dict:
    """What does each candidate accession itself hold for go_id (or a descendant)?"""
    per_acc = {}
    for acc in accessions:
        rows = quickgo_annotations(
            geneProductId=f"UniProtKB:{acc}",
            goId=go_id,
            goUsage="descendants",
            goUsageRelationships="is_a,part_of",
        )
        per_acc[acc] = [
            {
                "goId": r["goId"],
                "goName": r["goName"],
                "evidence": r["goEvidence"],
                "reference": r["reference"],
                "assignedBy": r["assignedBy"],
                "qualifier": r.get("qualifier"),
            }
            for r in rows
        ]
    all_rows = [r for v in per_acc.values() for r in v]
    exp = [r for r in all_rows if r["evidence"] in EXPERIMENTAL_CODES]
    return {
        "per_accession": per_acc,
        "n_rows": len(all_rows),
        "n_experimental": len(exp),
        "experimental_terms": sorted({(r["goId"], r["goName"], r["evidence"]) for r in exp}),
        "all_evidence_codes": sorted({r["evidence"] for r in all_rows}),
    }


def main() -> None:
    with GOA.open() as fh:
        rows = list(csv.DictReader(fh, delimiter="\t"))

    # Positive control for the QuickGO endpoint: a zero from a donor must be
    # distinguishable from a rejected query.  AGFG1 has annotations, so a
    # non-zero here proves the call pattern works.
    # (goUsage requires goId — QuickGO answers HTTP 400 without it, which the
    # status assertion in common._get surfaces rather than silently zeroing.)
    control = quickgo_annotations(
        geneProductId="UniProtKB:P52594",
        goId="GO:0001675",
        goUsage="descendants",
        goUsageRelationships="is_a,part_of",
    )
    if not control:
        raise AssertionError("positive control returned zero: QuickGO call pattern is broken")

    out: dict = {
        "subject": SUBJECT,
        "quickgo_positive_control": {
            "geneProductId": "UniProtKB:P52594",
            "n_annotations": len(control),
        },
        "goa_rows": [],
        "tokens": {},
    }

    cache: dict[str, dict] = {}
    for r in rows:
        wf = withfrom_tokens(r["WITH/FROM"])
        entry = {
            "go_id": r["GO TERM"],
            "go_name": r["GO NAME"],
            "aspect": r["GO ASPECT"],
            "qualifier": r["QUALIFIER"],
            "evidence": r["GO EVIDENCE CODE"],
            "reference": r["REFERENCE"],
            "assigned_by": r["ASSIGNED BY"],
            "withfrom_raw": r["WITH/FROM"],
            "withfrom_tokens": wf,
            "n_tokens": len(wf),
            "donors": {},
        }
        for tok in wf:
            if tok not in cache:
                cache[tok] = resolve_token(tok)
            rec = cache[tok]
            out["tokens"][tok] = rec
            if rec.get("kind") == "protein" and rec.get("accessions"):
                entry["donors"][tok] = donor_evidence(rec["accessions"], r["GO TERM"])
        out["goa_rows"].append(entry)

    # Invariant: the token list per row is derived from the GOA field, so the
    # count must match by construction.  Assert it rather than trusting it.
    for e, r in zip(out["goa_rows"], rows, strict=True):
        expected = [t for t in r["WITH/FROM"].split("|") if t]
        assert e["withfrom_tokens"] == expected, (e, expected)
        assert e["n_tokens"] == len(expected)

    unresolved = [t for t, v in out["tokens"].items() if v.get("kind") == "unresolved"]
    out["unresolved_tokens"] = unresolved

    (HERE / "withfrom.json").write_text(json.dumps(out, indent=2, sort_keys=True))
    print(f"rows={len(out['goa_rows'])} tokens={len(out['tokens'])} unresolved={unresolved}")
    for e in out["goa_rows"]:
        print(f"\n{e['go_id']} {e['go_name']} [{e['evidence']}] tokens={e['n_tokens']}")
        for tok, dv in e["donors"].items():
            rec = out["tokens"][tok]
            label = rec.get("entry_name") or ",".join(rec.get("reviewed_candidates") or rec.get("accessions", []))
            print(f"   {tok} -> {label}: rows={dv['n_rows']} exp={dv['n_experimental']} "
                  f"codes={dv['all_evidence_codes']}")
            for t in dv["experimental_terms"]:
                print(f"        EXP {t}")


if __name__ == "__main__":
    main()
