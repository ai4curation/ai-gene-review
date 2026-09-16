"""Resolve every WITH/FROM token in the AGGF1 GOA file, and ask what evidence
each donor itself carries for the term it is donating.

Two questions, kept separate on purpose:

1. *Who is the donor?*  -> accession, gene symbol, organism, Swiss-Prot vs
   TrEMBL, sequence length.  A paralogue donor is legitimate for IBA but means
   no ortholog-strength inference is available on that row.
2. *What does the donor itself hold for this term?*  -> QuickGO annotation
   search restricted to the propagated GO id with `goUsage=descendants`, then
   the evidence codes collected per donor.  "The source only carries the same
   family-level inference" is a testable claim, and usually false.

Outputs `withfrom_resolved.tsv` (one row per (GOA row, token)) and
`donor_evidence.tsv` (one row per (GOA row, donor, term the donor holds)).

Nothing is hardcoded: every field is derived from the GOA file plus live API
calls.  Missing input is a hard error naming the fix command.

Run: uv run python resolve_withfrom.py
"""

from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

import requests

from uniprot import _cached_get, resolve_mod_id, summarise, uniprot_entry

HERE = Path(__file__).parent
GOA = HERE.parent / "AGGF1-goa.tsv"
EXPERIMENTAL = {"EXP", "IDA", "IPI", "IMP", "IGI", "IEP", "HTP", "HDA", "HMP", "HGI", "HEP"}


def load_goa() -> list[dict[str, str]]:
    if not GOA.exists():
        raise SystemExit(f"missing {GOA}; run `just fetch-gene human AGGF1` first")
    with GOA.open() as fh:
        rows = list(csv.DictReader(fh, delimiter="\t"))
    if not rows:
        raise SystemExit(f"{GOA} has no data rows; run `just fetch-gene human AGGF1` first")
    return rows


def resolve_token(token: str) -> dict[str, str]:
    """Resolve one WITH/FROM token. Ambiguity is reported, never collapsed."""
    db, _, _local = token.partition(":")
    if db == "UniProtKB":
        acc = token.split(":", 1)[1]
        entry = uniprot_entry(acc)
        s = summarise(entry)
        if not s["id"]:
            raise SystemExit(f"{token} resolved to an entry with no entry name -- dead accession?")
        return {
            "token": token,
            "kind": "protein",
            "accession": s["accession"],
            "entry_name": s["id"],
            "gene": s["gene"],
            "protein": s["protein"],
            "organism": s["organism"],
            # "reviewed" is a substring of "unreviewed"; test the prefix.
            "status": "Swiss-Prot" if s["reviewed"] else "TrEMBL",
            "length": str(s["length"]),
            "n_hits": "1",
        }
    if db in {"MGI", "RGD", "FB", "ZFIN", "AGI_LocusCode"}:
        hits = resolve_mod_id(token)
        if not hits:
            return {"token": token, "kind": "mod-id", "accession": "", "entry_name": "",
                    "gene": "", "protein": "UNRESOLVED", "organism": "", "status": "",
                    "length": "", "n_hits": "0"}
        reviewed = [h for h in hits if h.get("entryType", "").startswith("UniProtKB reviewed")]
        best = (reviewed or hits)[0]
        s = summarise(uniprot_entry(best["primaryAccession"]))
        return {
            "token": token,
            "kind": "mod-id",
            "accession": s["accession"],
            "entry_name": s["id"],
            "gene": s["gene"],
            "protein": s["protein"],
            "organism": s["organism"],
            "status": "Swiss-Prot" if s["reviewed"] else "TrEMBL",
            "length": str(s["length"]),
            "n_hits": str(len(hits)),
        }
    if db == "PANTHER":
        return {"token": token, "kind": "panther-node", "accession": "", "entry_name": "",
                "gene": "", "protein": "PANTHER tree node (not a protein)", "organism": "",
                "status": "", "length": "", "n_hits": ""}
    return {"token": token, "kind": db.lower(), "accession": "", "entry_name": "", "gene": "",
            "protein": "not a protein identifier", "organism": "", "status": "",
            "length": "", "n_hits": ""}


def quickgo_annotations(gene_product_id: str, go_id: str) -> list[dict]:
    """All annotations of `gene_product_id` to `go_id` or a descendant.

    Anti-truncation guard compares numberOfHits against len(results), never
    against the page-size constant we chose -- a server that clamps instead of
    erroring would sail past the latter.
    """
    url = (
        "https://www.ebi.ac.uk/QuickGO/services/annotation/search"
        f"?geneProductId={gene_product_id}&goId={go_id}"
        "&goUsage=descendants&goUsageRelationships=is_a,part_of&limit=100"
    )
    key = f"qg_{gene_product_id.replace(':', '_')}_{go_id.replace(':', '_')}"
    d = json.loads(_cached_get(url, key))
    if d["numberOfHits"] > len(d["results"]):
        raise SystemExit(
            f"truncated QuickGO result for {gene_product_id}/{go_id}: "
            f"{d['numberOfHits']} hits, {len(d['results'])} read"
        )
    return d["results"]


def main() -> None:
    goa = load_goa()
    resolved_rows: list[dict[str, str]] = []
    donor_rows: list[dict[str, str]] = []
    cache: dict[str, dict[str, str]] = {}

    for row in goa:
        raw = row["WITH/FROM"].strip()
        if not raw:
            continue
        for token in raw.split("|"):
            if token not in cache:
                cache[token] = resolve_token(token)
            r = dict(cache[token])
            r["go_id"] = row["GO TERM"]
            r["go_name"] = row["GO NAME"]
            r["evidence"] = row["GO EVIDENCE CODE"]
            r["reference"] = row["REFERENCE"]
            resolved_rows.append(r)

            if row["GO EVIDENCE CODE"] != "IBA" or not r["accession"]:
                continue
            gp = f"UniProtKB:{r['accession']}"
            anns = quickgo_annotations(gp, row["GO TERM"])
            if not anns:
                donor_rows.append({
                    "propagated_term": row["GO TERM"], "propagated_name": row["GO NAME"],
                    "donor_token": token, "donor_acc": r["accession"], "donor_gene": r["gene"],
                    "donor_organism": r["organism"], "donor_term": "", "donor_term_name": "",
                    "donor_evidence": "NONE", "donor_reference": "", "experimental": "no",
                })
                continue
            for a in anns:
                donor_rows.append({
                    "propagated_term": row["GO TERM"], "propagated_name": row["GO NAME"],
                    "donor_token": token, "donor_acc": r["accession"], "donor_gene": r["gene"],
                    "donor_organism": r["organism"], "donor_term": a["goId"],
                    "donor_term_name": a.get("goName") or "",
                    "donor_evidence": a["goEvidence"],
                    "donor_reference": a.get("reference") or "",
                    "experimental": "yes" if a["goEvidence"] in EXPERIMENTAL else "no",
                })

    with (HERE / "withfrom_resolved.tsv").open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(resolved_rows[0]), delimiter="\t")
        w.writeheader()
        w.writerows(resolved_rows)
    with (HERE / "donor_evidence.tsv").open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(donor_rows[0]), delimiter="\t")
        w.writeheader()
        w.writerows(donor_rows)

    # Report, including the negatives.
    print(f"{len(goa)} GOA rows; {len(resolved_rows)} (row, token) pairs; "
          f"{len(cache)} distinct tokens")
    unresolved = [t for t, r in cache.items() if r["kind"] != "panther-node" and not r["accession"]]
    print(f"unresolved protein tokens: {unresolved or 'none'}")
    for token, r in sorted(cache.items()):
        print(f"  {token:38s} {r['kind']:13s} {r['accession']:10s} {r['gene']:10s} "
              f"{r['status']:10s} {r['length']:>6s} aa  {r['organism']}")
    print()
    by_term: dict[str, list[dict[str, str]]] = {}
    for d in donor_rows:
        by_term.setdefault(d["propagated_term"], []).append(d)
    for term, ds in sorted(by_term.items()):
        donors = sorted({d["donor_acc"] for d in ds})
        exp = sorted({d["donor_acc"] for d in ds if d["experimental"] == "yes"})
        print(f"{term} {ds[0]['propagated_name']}: {len(donors)} resolvable donors, "
              f"{len(exp)} with own experimental evidence for the term or a descendant")
        for d in ds:
            if d["donor_evidence"] == "NONE":
                print(f"    {d['donor_gene']:10s} ({d['donor_acc']}) {d['donor_organism']:25s} "
                      f"-> NO annotation to this term or a descendant")
            else:
                print(f"    {d['donor_gene']:10s} ({d['donor_acc']}) {d['donor_organism']:25s} "
                      f"-> {d['donor_term']} {d['donor_term_name']} [{d['donor_evidence']}] "
                      f"{d['donor_reference']}")
        print()


if __name__ == "__main__":
    sys.exit(main())
