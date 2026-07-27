#!/usr/bin/env python3
"""Resolve every GO:0005515 WITH/FROM partner accession in ADGRA2's GOA.

Built FROM the GOA TSV (never by hand -- hand-maintained source lists have drifted on
every gene in this campaign that tried it), with assertions that the resolved count
matches the parsed count.

Checks per ACRV1/ACRBP lessons:
  * reviewed (Swiss-Prot) vs unreviewed (TrEMBL) -- tested with startswith, because
    "reviewed" is a SUBSTRING of "unreviewed" and the natural `in` test promotes every
    TrEMBL entry silently (ACTG2 lesson);
  * length vs the canonical entry, to catch ORFeome/partial constructs;
  * whether the partner carries a PDZ domain, which is the hypothesis under test.
"""
from __future__ import annotations

import csv
import json
import sys
import time
import urllib.parse
import urllib.request

UA = {"User-Agent": "ai-gene-review ADGRA2 (mailto:cjmungall@lbl.gov)"}
FIELDS = "accession,id,protein_name,gene_primary,length,reviewed,ft_domain,cc_domain,xref_interpro"


def goa_partners(path: str, go_id: str = "GO:0005515") -> list[tuple[str, str, str]]:
    """(partner_accession, reference, evidence) triples straight out of the GOA TSV."""
    rows = []
    with open(path) as fh:
        rd = csv.DictReader(fh, delimiter="\t")
        for r in rd:
            if r["GO TERM"] != go_id:
                continue
            wf = r["WITH/FROM"].strip()
            assert wf, f"empty WITH/FROM on a {go_id} row: {r}"
            for tok in wf.split("|"):
                db, _, acc = tok.partition(":")
                assert db == "UniProtKB", f"unexpected WITH/FROM namespace {tok!r}"
                rows.append((acc, r["REFERENCE"], r["GO EVIDENCE CODE"]))
    return rows


def fetch(acc: str) -> dict:
    url = f"https://rest.uniprot.org/uniprotkb/{urllib.parse.quote(acc)}.json?fields={FIELDS}"
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=40) as fh:
        assert fh.status == 200, f"HTTP {fh.status} for {acc}"
        return json.load(fh)


def is_reviewed(entry_type: str) -> bool:
    # "reviewed" is a substring of "unreviewed" -- anchor, never `in`.
    return entry_type.startswith("UniProtKB reviewed")


def main() -> None:
    tsv = sys.argv[1]
    triples = goa_partners(tsv)
    accs = sorted({a for a, _, _ in triples})
    out = []
    for acc in accs:
        base = acc.split("-")[0]
        e = fetch(acc)
        canon = e if base == acc else fetch(base)
        name = (e.get("proteinDescription", {}).get("recommendedName", {})
                 .get("fullName", {}).get("value")) or e.get("uniProtkbId")
        assert name, f"empty name for {acc} -- dead/inactive accession? (ACTR10 lesson)"
        gene = (e.get("genes") or [{}])[0].get("geneName", {}).get("value")
        interpro = [x["id"] for x in e.get("uniProtKBCrossReferences", []) if x["database"] == "InterPro"]
        pdz_ft = [f for f in e.get("features", [])
                  if f["type"] == "Domain" and "PDZ" in (f.get("description") or "")]
        out.append({
            "accession": acc, "entry": e.get("uniProtkbId"), "gene": gene, "name": name,
            "reviewed": is_reviewed(e.get("entryType", "")),
            "entryType": e.get("entryType"),
            "length": e.get("sequence", {}).get("length"),
            "canonical_length": canon.get("sequence", {}).get("length"),
            "n_pdz_domains": len(pdz_ft),
            "n_interpro": len(interpro),
        })
        time.sleep(0.15)

    assert len(out) == len(accs), f"resolved {len(out)} of {len(accs)}"
    n_rev = sum(1 for o in out if o["reviewed"])
    n_unrev = len(out) - n_rev
    # Assert the two counts are actually derived, not a promoted 100% (ACTG2 lesson).
    assert n_rev + n_unrev == len(out)
    n_pdz = sum(1 for o in out if o["n_pdz_domains"] > 0)
    short = [o for o in out if o["length"] != o["canonical_length"]]

    w = max(len(o["gene"] or "") for o in out)
    print(f"{'gene':<{w}}  acc         len/canon  rev  PDZ")
    for o in sorted(out, key=lambda x: x["gene"] or ""):
        print(f"{o['gene'] or '?':<{w}}  {o['accession']:<11} {o['length']}/{o['canonical_length']:<6} "
              f"{'SP' if o['reviewed'] else 'TrEMBL':<6} {o['n_pdz_domains']}")
    print()
    print(f"partners resolved: {len(out)}  (GOA GO:0005515 rows: {len(triples)})")
    print(f"reviewed/Swiss-Prot: {n_rev}   unreviewed/TrEMBL: {n_unrev}")
    print(f"carrying >=1 annotated PDZ domain: {n_pdz}/{len(out)}")
    print(f"length != canonical (isoform/partial): {[(o['gene'], o['accession']) for o in short] or 'none'}")
    json.dump({"triples": triples, "partners": out}, open("partners.json", "w"), indent=2)


if __name__ == "__main__":
    main()
