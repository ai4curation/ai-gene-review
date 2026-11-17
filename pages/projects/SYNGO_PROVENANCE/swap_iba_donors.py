"""Check whether the swapped GABA receptor seeds are PAINT donors for any IBA.

A PAINT IBA row lists its donor genes in WITH/FROM by model-organism database
identifier (MGI, RGD, ...), not by UniProt accession, so a WITH/FROM search for
the seed's UniProt accession finds nothing even when the gene is a donor. And a
PAINT curator can place the IBD at a broader term than the donor's own
annotation, so a search restricted to the swapped terms can miss it too. This
script, for each swapped seed (gene product, paper) in
``data/gaba_receptor_swaps-verdicts.yaml``:

1. looks up the gene's MGI/RGD identifier from its UniProt record;
2. lists every IBA row (any term, any species) naming that identifier in WITH/FROM;
3. for each IBA term, lists the swapped terms at or below it (``is_a``/``part_of``),
   i.e. whether the swapped rows could have been among the IBD's inputs;
4. where they could, lists the donor's other experimental support for the term
   (descendants included, excluding the swapped paper), and does the same for
   every other donor of that PAINT node.

Being a donor does not make an IBA wrong: the PAINT node is placed from all
donors. The output says which IBAs a corrected seed would remove one donor
from, and whether the node keeps independent support. Output:
``data/gaba_receptor_swaps-iba.yaml``.

    python projects/SYNGO_PROVENANCE/swap_iba_donors.py
"""
from __future__ import annotations

import datetime
import json
import urllib.parse
import urllib.request
from pathlib import Path

import yaml

from gaba_receptor_swaps import quickgo

ROOT = Path(__file__).resolve().parents[2]
VERDICTS = ROOT / "projects/SYNGO_PROVENANCE/data/gaba_receptor_swaps-verdicts.yaml"
OUT = ROOT / "projects/SYNGO_PROVENANCE/data/gaba_receptor_swaps-iba.yaml"
EXPERIMENTAL = {"EXP", "IDA", "IMP", "IGI", "IPI", "IEP", "HDA", "HMP", "HTP", "HGI", "HEP"}
IBA_ECO = "ECO:0000318"


def get_json(url: str) -> dict:
    """GET a JSON document."""
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=120) as resp:
        return json.load(resp)


def mod_id(accession: str) -> str:
    """Return the WITH/FROM form of a UniProt entry's MGI or RGD identifier.

    QuickGO writes MGI donors as ``MGI:MGI:95619`` and RGD donors as ``RGD:2649``.
    """
    refs = get_json(f"https://rest.uniprot.org/uniprotkb/{accession}.json?fields=xref_mgi,xref_rgd")
    for ref in refs.get("uniProtKBCrossReferences", []):
        if ref["database"] in ("MGI", "RGD"):
            return f"{ref['database']}:{ref['id']}"
    raise ValueError(f"No MGI or RGD cross-reference on UniProtKB:{accession}")


def uniprot_for(donor: str) -> tuple[str, str] | None:
    """(UniProt accession, gene symbol) for a WITH/FROM donor id, or None if no reviewed entry."""
    db, ident = donor.split(":", 1)
    if db == "UniProtKB":
        query = urllib.parse.quote(f"accession:{ident}")
    else:
        ident = ident.removeprefix("MGI:")
        query = urllib.parse.quote(f"(xref:{db.lower()}-{ident}) AND reviewed:true")
    url = f"https://rest.uniprot.org/uniprotkb/search?query={query}&fields=accession,gene_primary&format=json"
    hits = get_json(url).get("results", [])
    if not hits:
        return None
    genes = hits[0].get("genes") or [{}]
    return hits[0]["primaryAccession"], genes[0].get("geneName", {}).get("value")


def ancestors(go_id: str) -> set[str]:
    """is_a/part_of ancestors of a GO term, including itself."""
    url = f"https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/{go_id}/ancestors?relations=is_a,part_of"
    return set(get_json(url)["results"][0]["ancestors"]) | {go_id}


def experimental_support(accession: str, go_id: str, exclude: set[str]) -> list[str]:
    """Experimental rows on a gene product for a term or its descendants, minus excluded papers."""
    rows = quickgo(geneProductId=accession, goId=go_id, goUsage="descendants")
    return sorted({f"{r['goEvidence']} {r['reference']} ({r['goId']})" for r in rows
                   if r["goEvidence"] in EXPERIMENTAL and r["reference"] not in exclude})


def donors(row: dict) -> set[str]:
    """MOD and UniProt donors named in an IBA row's WITH/FROM."""
    return {f"{x['db']}:{x['id']}" for w in row.get("withFrom") or [] for x in w.get("connectedXrefs", [])
            if x["db"] in ("MGI", "RGD", "UniProtKB", "ZFIN", "FB", "WB", "SGD", "TAIR", "PomBase")}


def seeds() -> list[tuple[str, str]]:
    """(UniProt accession, PMID) for every swapped seed in the verdicts file."""
    out = []
    for paper in yaml.safe_load(VERDICTS.read_text())["papers"]:
        for acc in paper.get("seed_accessions", []):
            out.append((acc, paper["reference"]))
    return out


def main() -> None:
    """Write the IBA donor check for every swapped seed."""
    swap_papers = {ref for _, ref in seeds()}
    records, fed_terms = [], {}
    for acc, ref in seeds():
        donor = mod_id(acc)
        seed_rows = [r for r in quickgo(geneProductId=acc, includeFields="goName")
                     if r["reference"] == ref and r["assignedBy"] == "SynGO"]
        swapped = {r["goId"]: r["goName"] for r in seed_rows}
        swapped_anc = {go: ancestors(go) for go in swapped}
        iba = quickgo(withFrom=donor, evidenceCode=IBA_ECO, evidenceCodeUsage="exact", includeFields="goName")
        if not iba:
            raise ValueError(f"No IBA names {donor}; check the WITH/FROM id format before trusting a zero")
        terms = []
        for go_id in sorted({r["goId"] for r in iba}):
            rows = [r for r in iba if r["goId"] == go_id]
            below = sorted(s for s, anc in swapped_anc.items() if go_id in anc)
            nodes = sorted({c["id"] for r in rows for w in r["withFrom"] or []
                            for c in w.get("connectedXrefs", []) if c["db"] == "PANTHER"})
            entry = {"go_id": go_id, "go_name": rows[0]["goName"], "iba_rows_naming_donor": len(rows),
                     "paint_nodes": nodes, "swapped_terms_at_or_below": below}
            if below:
                entry["donor_other_experimental_support"] = experimental_support(acc, go_id, swap_papers)
                fed_terms.setdefault((go_id, rows[0]["goName"], tuple(nodes)), set()).update(
                    d for r in rows for d in donors(r))
            terms.append(entry)
        records.append({"seed": f"UniProtKB:{acc}", "donor_id": donor, "reference": ref,
                        "swapped_terms": [{"go_id": k, "go_name": v} for k, v in sorted(swapped.items())],
                        "iba_terms": terms})
    nodes_out = []
    for (go_id, go_name, nodes), roster in sorted(fed_terms.items()):
        members = []
        for d in sorted(roster):
            hit = uniprot_for(d)
            members.append({"donor": d, "uniprot": hit[0] if hit else None,
                            "symbol": hit[1] if hit else None,
                            "experimental_support_excluding_swap_papers":
                                experimental_support(hit[0], go_id, swap_papers) if hit else "not checked: no reviewed UniProt entry"})
        nodes_out.append({"go_id": go_id, "go_name": go_name, "paint_nodes": list(nodes), "donors": members})
    OUT.write_text(yaml.safe_dump({"retrieved": datetime.date.today().isoformat(), "swap_papers": sorted(swap_papers),
                                   "seeds": records, "iba_terms_the_swaps_could_feed": nodes_out},
                                  sort_keys=False, allow_unicode=True, width=100))
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
