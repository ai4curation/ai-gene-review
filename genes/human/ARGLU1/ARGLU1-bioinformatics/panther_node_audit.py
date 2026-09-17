#!/usr/bin/env python3
"""Audit the PANTHER PTN001271790 (ARGLU1 family) IBA propagations.

Human ARGLU1 (Q9NWB6) receives two cellular-component terms by IBA from the same
PANTHER ancestral node, ``PTN001271790``:

* ``GO:0005654`` nucleoplasm  -- WITH/FROM ``FB:FBgn0051712|MGI:MGI:2442985|PANTHER:PTN001271790|UniProtKB:Q9NWB6``
* ``GO:0005739`` mitochondrion -- WITH/FROM ``CGD:CAL0000179812|PANTHER:PTN001271790``

The question this script answers, for each term, is:

1. How many gene products in all of GOA receive the term by IBA from this node
   (the blast radius of the node placement), and across how many taxa?
2. Which gene products anywhere in that propagated set hold the term by their own
   **experimental** evidence (the donor pool that could justify the node)?

Both are needed: a broad propagation supported by many independent experimental
donors is sound phylogenetics; a broad propagation resting on a single
lineage-restricted donor is a node-placement defect.

Outputs ``results.json`` and prints a human-readable summary. Run:

    uv run python panther_node_audit.py

No API key needed. Network access to QuickGO and UniProt is required; a missing
network is a hard error, not a degraded result.
"""

from __future__ import annotations

import json
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter
from pathlib import Path

QUICKGO = "https://www.ebi.ac.uk/QuickGO/services/annotation/search"
UNIPROT = "https://rest.uniprot.org/uniprotkb/search"

NODE = "PANTHER:PTN001271790"
SUBJECT = "UniProtKB:Q9NWB6"  # human ARGLU1

# GO experimental evidence codes (GO's own "experimental evidence" set, including
# the high-throughput HTP/HDA/HMP/HGI/HEP codes).
EXPERIMENTAL = {"EXP", "IDA", "IPI", "IMP", "IGI", "IEP",
                "HTP", "HDA", "HMP", "HGI", "HEP"}

TERMS = {
    "GO:0005739": "mitochondrion",
    "GO:0005654": "nucleoplasm",
}


def _get(url: str) -> dict:
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=60) as fh:
                return json.load(fh)
        except urllib.error.HTTPError as exc:
            if exc.code in (429, 500, 502, 503) and attempt < 3:
                time.sleep(2 ** attempt)
                continue
            raise
    raise RuntimeError(f"unreachable: {url}")


def quickgo_paged(params: dict, page_size: int = 100) -> list[dict]:
    """Fetch every page of a QuickGO annotation search.

    The anti-truncation guard compares ``numberOfHits`` against the number of rows
    actually accumulated -- never against ``page_size``. QuickGO clamps the
    per-page limit rather than erroring, so a guard written against a chosen
    constant can be silently defeated (see the campaign brief).
    """
    rows: list[dict] = []
    page = 1
    total: int | None = None
    while True:
        qs = urllib.parse.urlencode({**params, "limit": page_size, "page": page})
        data = _get(f"{QUICKGO}?{qs}")
        if total is None:
            total = data["numberOfHits"]
        rows.extend(data["results"])
        if not data["results"] or len(rows) >= total:
            break
        page += 1
        if page > 200:
            raise RuntimeError("pagination runaway; refusing to loop forever")
        time.sleep(0.2)
    if total is None:
        raise RuntimeError("QuickGO returned no numberOfHits field")
    if len(rows) != total:
        raise RuntimeError(
            f"truncated fetch: numberOfHits={total} but accumulated {len(rows)} rows "
            f"for {params!r}"
        )
    return rows


def uniprot_entry(accession: str) -> dict:
    """Resolve one UniProt accession, printing entry name so a dead entry is loud.

    A deleted/inactive accession returns no gene name and no annotations, which is
    indistinguishable from 'this protein genuinely has no annotation' unless the
    lookup itself fails loudly.
    """
    qs = urllib.parse.urlencode({
        "query": f"accession:{accession}",
        "fields": "accession,id,protein_name,gene_names,organism_name,reviewed,lineage",
        "format": "json",
        "size": 5,
    })
    data = _get(f"{UNIPROT}?{qs}")
    results = data.get("results", [])
    if len(results) != 1:
        raise RuntimeError(
            f"{accession}: expected exactly 1 UniProt hit, got {len(results)}. "
            "An ambiguous or dead accession must be reported, not silently resolved."
        )
    r = results[0]
    entry_type = r.get("entryType", "")
    # "reviewed" is a substring of "unreviewed" -- anchor the test.
    reviewed = entry_type.startswith("UniProtKB reviewed")
    desc = r.get("proteinDescription", {})
    name = (desc.get("recommendedName", {}).get("fullName", {}).get("value")
            or (desc.get("submissionNames") or [{}])[0].get("fullName", {}).get("value")
            or "(no protein name)")
    # UniProt returns organism.lineage as a list of plain taxon-name strings.
    lineage = list(r.get("organism", {}).get("lineage", []))
    if lineage and not isinstance(lineage[0], str):
        raise RuntimeError(
            f"{accession}: unexpected lineage element type {type(lineage[0])}; "
            "the UniProt response shape changed -- fix the parser rather than guessing."
        )
    return {
        "accession": r["primaryAccession"],
        "entry_name": r.get("uniProtkbId", "(none)"),
        "entry_type": entry_type,
        "reviewed": reviewed,
        "protein_name": name,
        "genes": [g.get("geneName", {}).get("value") for g in r.get("genes", [])],
        "organism": r.get("organism", {}).get("scientificName"),
        "kingdom": next((t for t in lineage
                         if t in {"Metazoa", "Viridiplantae", "Fungi",
                                  "Eukaryota", "Amoebozoa"}), None),
    }


def audit_term(go_id: str, label: str) -> dict:
    # 1. blast radius: everything receiving this term by IBA from this node
    iba = quickgo_paged({
        "goId": go_id,
        "evidenceCode": "ECO:0000318",
        "withFrom": NODE,
    })
    entities = sorted({r["geneProductId"] for r in iba})
    taxa = sorted({r["taxonName"] for r in iba if r.get("taxonName")})

    # 2. donor pool: which of those entities hold the term (or a descendant) by
    #    their own experimental evidence?
    own = quickgo_paged({
        "goId": go_id,
        "goUsage": "descendants",
        "goUsageRelationships": "is_a,part_of",
        "withFrom": NODE,
    })
    by_code = Counter(r["goEvidence"] for r in own)

    # The withFrom filter only returns rows that themselves cite the node, i.e.
    # the IBAs. Experimental donors must be queried per entity.
    exp_holders: list[dict] = []
    for ent in entities:
        rows = quickgo_paged({
            "geneProductId": ent,
            "goId": go_id,
            "goUsage": "descendants",
            "goUsageRelationships": "is_a,part_of",
        })
        exp = [r for r in rows if r["goEvidence"] in EXPERIMENTAL]
        if exp:
            exp_holders.append({
                "gene_product": ent,
                "symbol": exp[0].get("symbol"),
                "taxon": exp[0].get("taxonName"),
                "evidence": sorted({r["goEvidence"] for r in exp}),
                "references": sorted({r["reference"] for r in exp}),
            })
        time.sleep(0.05)

    return {
        "go_id": go_id,
        "go_label": label,
        "iba_annotations_from_node": len(iba),
        "distinct_entities": len(entities),
        "distinct_taxa": len(taxa),
        "subject_receives_it": SUBJECT in entities,
        "iba_evidence_codes_citing_node": dict(by_code),
        "experimental_holders": exp_holders,
        "n_experimental_holders": len(exp_holders),
        "entities": entities,
    }


def main() -> int:
    out: dict = {"node": NODE, "subject": SUBJECT, "terms": {}}

    for go_id, label in TERMS.items():
        res = audit_term(go_id, label)
        out["terms"][go_id] = res

    # Resolve every experimental donor so its identity, reviewed status and
    # lineage are on the record rather than inferred from a symbol.
    donors: dict[str, dict] = {}
    for res in out["terms"].values():
        for h in res["experimental_holders"]:
            acc = h["gene_product"].split(":", 1)[1]
            if acc not in donors:
                donors[acc] = uniprot_entry(acc)
                time.sleep(0.1)
    out["donor_details"] = donors

    here = Path(__file__).resolve().parent
    (here / "results.json").write_text(json.dumps(out, indent=2, sort_keys=True))

    for go_id, res in out["terms"].items():
        print(f"\n=== {go_id} {res['go_label']} ===")
        print(f"  IBA rows citing {NODE}: {res['iba_annotations_from_node']}")
        print(f"  distinct gene products receiving it: {res['distinct_entities']}")
        print(f"  distinct taxa: {res['distinct_taxa']}")
        print(f"  human ARGLU1 among them: {res['subject_receives_it']}")
        print(f"  gene products with their OWN experimental evidence "
              f"for this term: {res['n_experimental_holders']}")
        for h in res["experimental_holders"]:
            d = donors[h["gene_product"].split(":", 1)[1]]
            status = "Swiss-Prot" if d["reviewed"] else "TrEMBL"
            print(f"    - {h['gene_product']} {d['genes']} ({status}) "
                  f"{d['organism']} [{d['kingdom']}] "
                  f"{h['evidence']} {h['references']}")
            print(f"      name: {d['protein_name']}")
    print(f"\nwrote {here / 'results.json'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
