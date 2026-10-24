"""Resolve every WITH/FROM entity on the APLN GOA rows and emit the ``source_entities``
scaffolding for the review's ``propagation_review`` blocks.

The point is that source_entities must be *derived* from the seeded
``supporting_entities``, never retyped: a hand-written donor list drifts from the GOA
row it claims to describe, and the drift is invisible. This script reads the YAML,
resolves each identifier against a live database, and writes one YAML fragment per row.

Resolvers, all live:
  UniProtKB:<acc>        -> rest.uniprot.org/uniprotkb (entry name, protein, organism, reviewed)
  RGD:<id>               -> rest.uniprot.org search on xref:rgd-<id> (reports multi-hits)
  ensembl:<ENSxxxP...>   -> rest.uniprot.org search on xref:ensembl-<id>
  PANTHER:PTN...         -> the committed PAINT slice interpro/panther/<FAM>/<FAM>-paint.tsv
  InterPro:IPR...        -> www.ebi.ac.uk/interpro/api/entry/interpro/<id>
  UniProtKB-SubCell:SL-  -> rest.uniprot.org/locations/<id>
  RNAcentral:URS...      -> rnacentral.org/api/v1/rna/<urs>

    uv run python resolve_withfrom.py     # -> withfrom_resolved.tsv, source_entities.yaml
"""

from __future__ import annotations

import json
import pathlib
import sys

import requests
import yaml

HERE = pathlib.Path(__file__).resolve().parent
GENE_DIR = HERE.parent
REPO = GENE_DIR.parents[2]
REVIEW = GENE_DIR / "APLN-ai-review.yaml"
PAINT = REPO / "interpro" / "panther" / "PTHR15953" / "PTHR15953-paint.tsv"
CACHE = HERE / "cache"
OUT_TSV = HERE / "withfrom_resolved.tsv"
OUT_YAML = HERE / "source_entities.yaml"

# propagation_review is required on these evidence codes when the row carries WITH/FROM
PROPAGATED = {"IBA", "ISS", "ISO", "IEA", "IC"}


def get_json(url: str, key: str, params: dict | None = None):
    CACHE.mkdir(exist_ok=True)
    path = CACHE / f"{key}.json"
    if path.exists():
        return json.loads(path.read_text())
    resp = requests.get(url, params=params or {}, headers={"Accept": "application/json"}, timeout=120)
    resp.raise_for_status()
    path.write_text(resp.text)
    return resp.json()


def uniprot_search(query: str, key: str) -> list[dict]:
    data = get_json(
        "https://rest.uniprot.org/uniprotkb/search",
        key,
        {"query": query, "fields": "accession,id,protein_name,gene_names,organism_name,reviewed", "size": "5"},
    )
    return data.get("results", [])


def fmt_entry(e: dict) -> str:
    genes = e.get("genes") or []
    sym = genes[0].get("geneName", {}).get("value", "?") if genes else "?"
    name = e.get("proteinDescription", {}).get("recommendedName", {}).get("fullName", {}).get("value", "?")
    rev = "Swiss-Prot" if e["entryType"].startswith("UniProtKB reviewed") else "TrEMBL"
    return f"{e['primaryAccession']} ({e['uniProtkbId']}) {sym} | {name} | {e['organism']['scientificName']} | {rev}"


def resolve(ident: str) -> str:
    if ident.startswith("UniProtKB:"):
        acc = ident.split(":", 1)[1]
        hits = uniprot_search(f"accession:{acc}", f"up_{acc}")
        if not hits:
            return "UNRESOLVED"
        return "; ".join(fmt_entry(h) for h in hits)
    if ident.startswith("RGD:"):
        num = ident.split(":", 1)[1]
        hits = uniprot_search(f"xref:rgd-{num}", f"rgd_{num}")
        if not hits:
            return "UNRESOLVED"
        return f"[{len(hits)} hit(s)] " + "; ".join(fmt_entry(h) for h in hits)
    if ident.startswith("ensembl:"):
        eid = ident.split(":", 1)[1]
        hits = uniprot_search(f"xref:ensembl-{eid}", f"ens_{eid}")
        if not hits:
            return "UNRESOLVED"
        return f"[{len(hits)} hit(s)] " + "; ".join(fmt_entry(h) for h in hits)
    if ident.startswith("PANTHER:PTN"):
        node = ident.split(":", 1)[1]
        if not PAINT.exists():
            return "UNRESOLVED (no PAINT slice)"
        rows = [ln.split("\t") for ln in PAINT.read_text().strip().splitlines()[1:]]
        mine = [r for r in rows if r[1] == node]
        if not mine:
            return f"UNRESOLVED (node not in {PAINT.name})"
        return "; ".join(
            f"{r[0]} node {r[1]} {r[4]} {r[2]} (aspect {r[3]}, negated={r[5]}, taxon {r[7]}) seeds={r[6]}"
            for r in mine
        )
    if ident.startswith("InterPro:"):
        ipr = ident.split(":", 1)[1]
        data = get_json(f"https://www.ebi.ac.uk/interpro/api/entry/interpro/{ipr}/", f"ipr_{ipr}")
        md = data["metadata"]
        counts = md.get("counters", {})
        return f"{md['accession']} '{md['name']['name']}' type={md['type']} proteins={counts.get('proteins')}"
    if ident.startswith("UniProtKB-SubCell:"):
        sl = ident.split(":", 1)[1]
        data = get_json(f"https://rest.uniprot.org/locations/{sl}", f"sl_{sl}")
        return f"{data['id']} '{data['name']}' category={data.get('category')}"
    if ident.startswith("RNAcentral:"):
        # keep the _<taxid> suffix: the bare URS is the cross-species sequence and its
        # description ("ncRNA from 16 species") hides which human RNA the row means.
        urs = ident.split(":", 1)[1]
        data = get_json(f"https://rnacentral.org/api/v1/rna/{urs}", f"urs_{urs}")
        return f"{data['rnacentral_id']} {data.get('rna_type')} len={data.get('length')} '{data.get('description')}'"
    return "UNRESOLVED (no resolver)"


def main() -> int:
    doc = yaml.safe_load(REVIEW.read_text())
    rows = [a for a in doc["existing_annotations"] if a.get("supporting_entities")]
    resolved: dict[str, str] = {}
    lines = ["\t".join(["go_id", "go_label", "evidence", "reference", "identifier", "resolution"])]
    frag: list[dict] = []

    for ann in rows:
        entities = ann["supporting_entities"]
        block = {
            "go_id": ann["term"]["id"],
            "go_label": ann["term"]["label"],
            "evidence_type": ann["evidence_type"],
            "original_reference_id": ann["original_reference_id"],
            "propagation_review_required": ann["evidence_type"] in PROPAGATED,
            "source_entities": [],
        }
        for ident in entities:
            if ident not in resolved:
                resolved[ident] = resolve(ident)
            lines.append(
                "\t".join([ann["term"]["id"], ann["term"]["label"], ann["evidence_type"],
                           ann["original_reference_id"], ident, resolved[ident]])
            )
            block["source_entities"].append({"source_id": ident, "resolution": resolved[ident]})
        frag.append(block)

    OUT_TSV.write_text("\n".join(lines) + "\n")
    OUT_YAML.write_text(yaml.dump(frag, sort_keys=False, width=110, allow_unicode=True))

    n_req = sum(1 for b in frag if b["propagation_review_required"])
    by_ev: dict[str, int] = {}
    for b in frag:
        if b["propagation_review_required"]:
            by_ev[b["evidence_type"]] = by_ev.get(b["evidence_type"], 0) + 1
    print(f"rows carrying supporting_entities        : {len(rows)}")
    print(f"rows requiring propagation_review        : {n_req}  {by_ev}")
    print(f"rows with supporting_entities but not propagated: "
          f"{[ (b['evidence_type'], b['go_id']) for b in frag if not b['propagation_review_required'] ]}")
    print(f"distinct identifiers                     : {len(resolved)}")
    print()
    for ident in sorted(resolved):
        print(f"  {ident}\n      {resolved[ident]}")
    unresolved = [i for i, r in resolved.items() if r.startswith("UNRESOLVED")]
    print()
    print(f"unresolved: {unresolved or 'none'}")
    print(f"wrote {OUT_TSV.name}, {OUT_YAML.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
