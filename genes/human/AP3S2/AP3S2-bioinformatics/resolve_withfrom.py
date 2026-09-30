"""Resolve every WITH/FROM donor in the AP3S2 GOA rows, and the PAINT IBD seeds.

Two things are resolved, both live:

1. Every token in the WITH/FROM column of `AP3S2-goa.tsv`. MOD identifiers
   (MGI:, RGD:, SGD:, PomBase:, FB:, WB:, CGD:, dictyBase:) are resolved through
   the UniProt cross-reference search (`query=xref:<db>-<id>`, size 5 so that a
   multi-hit is reported rather than silently collapsed); bare UniProtKB
   accessions are fetched directly.

2. The seed lists of the PANTHER IBD nodes in the committed PAINT slice
   `interpro/panther/PTHR11753/PTHR11753-paint.tsv`, so the review can state
   which seeds sit behind the IBA rather than guessing.

Output: withfrom_resolved.tsv
"""

from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

import requests

HERE = Path(__file__).parent
GOA = HERE.parent / "AP3S2-goa.tsv"
PAINT = HERE.parents[3] / "interpro" / "panther" / "PTHR11753" / "PTHR11753-paint.tsv"
CACHE = HERE / "cache"
OUT = HERE / "withfrom_resolved.tsv"

# UniProt xref database prefixes, keyed by the prefix used in GOA WITH/FROM.
XREF_DB = {
    "MGI": "mgi",
    "RGD": "rgd",
    "SGD": "sgd",
    "PomBase": "pombase",
    "FB": "flybase",
    "WB": "wormbase",
    "CGD": "cgd",
    "dictyBase": "dictybase",
    "AGI_LocusCode": "araport",
    "TAIR": "araport",
}


def cached_get(url: str, key: str) -> str:
    CACHE.mkdir(exist_ok=True)
    path = CACHE / f"{key}.txt"
    if path.exists():
        return path.read_text()
    resp = requests.get(url, timeout=60)
    resp.raise_for_status()
    path.write_text(resp.text)
    return resp.text


def resolve_via_go_api(token: str) -> tuple[str, str, list[str]] | None:
    """GO API bioentity record for a MOD identifier: (name, taxon CURIE, synonyms)."""
    key = "go_" + token.replace(":", "_")
    txt = cached_get(
        "https://api.geneontology.org/api/bioentity/" + token.replace(":", "%3A"), key)
    data = json.loads(txt)
    if not data:
        return None
    rec = data[0]
    return rec.get("bioentity_name", ""), rec.get("taxon", ""), rec.get("synonym") or []


def resolve(token: str) -> dict[str, str]:
    """Resolve one WITH/FROM or seed token to UniProt, reporting multi-hits."""
    if ":" not in token:
        return {"token": token, "status": "UNPARSEABLE", "hits": "", "detail": ""}
    prefix, rest = token.split(":", 1)

    if prefix == "PANTHER":
        return {"token": token, "status": "PANTHER_NODE", "hits": "",
                "detail": "ancestral node, not a donor gene product"}
    if prefix in {"InterPro", "ARBA", "UniProtKB-SubCell", "GO", "ensembl"}:
        return {"token": token, "status": "NOT_A_GENE_PRODUCT", "hits": "", "detail": prefix}

    if prefix == "UniProtKB":
        key = f"up_{rest.replace(':', '_')}"
        txt = cached_get(
            "https://rest.uniprot.org/uniprotkb/search?query=accession:"
            f"{rest}&fields=accession,id,protein_name,gene_names,organism_name,reviewed"
            "&format=tsv&size=5", key)
    else:
        db = XREF_DB.get(prefix)
        if db is None:
            return {"token": token, "status": "UNKNOWN_PREFIX", "hits": "", "detail": prefix}
        # MGI ids arrive as "MGI:MGI:1098244"; UniProt wants the bare number.
        bare = rest.split(":")[-1]
        key = f"xr_{db}_{bare.replace('/', '_')}"
        txt = cached_get(
            f"https://rest.uniprot.org/uniprotkb/search?query=xref:{db}-{bare}"
            "&fields=accession,id,protein_name,gene_names,organism_name,reviewed"
            "&format=tsv&size=5", key)

    lines = [ln for ln in txt.strip().splitlines()[1:] if ln.strip()]
    if not lines:
        # UniProt's xref index does not cover every MOD identifier (WormBase gene
        # ids in particular). Fall back to the GO API's own bioentity record,
        # which is the authority for what the WITH/FROM token denotes, then use
        # the returned locus synonym to find the protein.
        go_hit = resolve_via_go_api(token)
        if go_hit is None:
            return {"token": token, "status": "UNRESOLVED", "hits": "0", "detail": ""}
        name, taxon, synonyms = go_hit
        acc_detail = ""
        for syn in synonyms:
            key2 = f"gene_{syn.replace('.', '_').replace(':', '_')}"
            tsv = cached_get(
                "https://rest.uniprot.org/uniprotkb/search?query=gene:"
                f"{syn}+AND+organism_id:{taxon.split(':')[-1]}"
                "&fields=accession,id,protein_name,gene_names,organism_name,reviewed"
                "&format=tsv&size=5", key2)
            hits = [ln for ln in tsv.strip().splitlines()[1:] if ln.strip()]
            if hits:
                c = hits[0].split("\t")
                acc_detail = f"{c[0]} {c[1]} | {c[3]} | {c[4]} | {c[5]}"
                break
        detail = f"{acc_detail or name} [GO API: {name}, {taxon}]"
        return {"token": token, "status": "RESOLVED_VIA_GO_API", "hits": "1",
                "detail": detail}
    reviewed = [ln for ln in lines if ln.rsplit("\t", 1)[-1] == "reviewed"]
    best = reviewed[0] if reviewed else lines[0]
    cols = best.split("\t")
    detail = f"{cols[0]} {cols[1]} | {cols[3]} | {cols[4]} | {cols[5]}"
    return {"token": token, "status": "RESOLVED", "hits": str(len(lines)), "detail": detail}


def main() -> int:
    tokens: dict[str, list[str]] = {}

    with GOA.open() as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            raw = row["WITH/FROM"].strip()
            if not raw:
                continue
            ctx = f"GOA {row['GO TERM']} {row['GO EVIDENCE CODE']} {row['REFERENCE']}"
            for tok in raw.split("|"):
                tok = tok.strip()
                if tok:
                    tokens.setdefault(tok, []).append(ctx)

    paint_rows = []
    with PAINT.open() as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            paint_rows.append(row)
            ctx = f"PAINT {row['node']} {row['go_id']} {row['evidence']}"
            for tok in row["seeds"].split("|"):
                tok = tok.strip()
                if tok:
                    tokens.setdefault(tok, []).append(ctx)

    print(f"GOA WITH/FROM + PAINT seed tokens to resolve: {len(tokens)}")
    print(f"PAINT slice rows: {len(paint_rows)}")
    for row in paint_rows:
        n = len([s for s in row["seeds"].split("|") if s.strip()])
        print(f"  {row['node']} {row['go_id']} ({row['aspect']}) {row['evidence']} "
              f"seeds={n} date={row['date']}")

    rows = []
    for tok in sorted(tokens):
        res = resolve(tok)
        rows.append([tok, res["status"], res["hits"], res["detail"],
                     "; ".join(sorted(set(tokens[tok])))])
        print(f"  {tok:28s} {res['status']:18s} hits={res['hits']:3s} {res['detail']}")

    with OUT.open("w") as fh:
        fh.write("token\tstatus\tuniprot_hits\tresolved\tused_in\n")
        for r in rows:
            fh.write("\t".join(r) + "\n")
    print(f"\nwrote {OUT.name} ({len(rows)} rows)")

    unresolved = [r for r in rows if r[1] in {"UNRESOLVED", "UNKNOWN_PREFIX", "UNPARSEABLE"}]
    if unresolved:
        print(f"\n{len(unresolved)} token(s) not resolvable through UniProt xref search "
              "(report these as UNRESOLVED in the review rather than guessing):")
        for r in unresolved:
            print(f"  - {r[0]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
