"""Scan model-organism proteomes for IBA annotations on proteins with transposable-element domains.

A protein that carries a reverse transcriptase, integrase or transposase domain is either a
transposable-element (TE) ORF or a host gene domesticated from one. IBA annotations reach both
kinds whenever PANTHER groups them with a characterised host gene. This scan lists, for each PAINT
node, which GO terms it propagates to TE-domain proteins in the chosen proteomes, so that each node
can be judged by hand: a domesticated gene with its own function, or a TE ORF that inherited a host
gene's biology.

Steps:
1. For each proteome taxon and each TE Pfam domain below, collect UniProtKB accessions from the
   UniProt REST API.
2. Fetch the IBA annotations (GO evidence IBA) for those accessions from QuickGO.
3. Group rows by the PANTHER PTN node in WITH/FROM and the GO term, and write a YAML summary with
   counts, taxa and example proteins, reviewed (Swiss-Prot) entries listed separately.

The script reports what the APIs return on the day it runs; nothing is hard-coded but the input
lists. Run from the repository root:

    uv run python projects/TRANSPOSON_DERIVED_ANNOTATIONS/scripts/scan_te_iba.py \
        -o projects/TRANSPOSON_DERIVED_ANNOTATIONS/data/te_iba_scan.yaml
"""

from __future__ import annotations

import argparse
import collections
import datetime
import json
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

import yaml

# Eukaryotic proteomes of the Wei et al. 2020 RAR screen that have IBA coverage, plus zebrafish and
# rat, which carry many TE ORFs.
TAXA = {
    9606: "Homo sapiens",
    10090: "Mus musculus",
    10116: "Rattus norvegicus",
    9031: "Gallus gallus",
    7955: "Danio rerio",
    7227: "Drosophila melanogaster",
    6239: "Caenorhabditis elegans",
    3702: "Arabidopsis thaliana",
    559292: "Saccharomyces cerevisiae S288C",
    284812: "Schizosaccharomyces pombe 972h-",
    237561: "Candida albicans SC5314",
    44689: "Dictyostelium discoideum",
}

# Pfam domains characteristic of transposable elements (names from the InterPro API).
TE_PFAM = {
    "PF00078": "Reverse transcriptase (RNA-dependent DNA polymerase)",
    "PF07727": "Reverse transcriptase (RNA-dependent DNA polymerase)",
    "PF00665": "Integrase core domain",
    "PF05380": "Pao retrotransposon-like RNaseH-like domain",
    "PF03184": "DDE superfamily endonuclease",
    "PF13359": "DDE superfamily endonuclease",
    "PF13843": "Transposase IS4",
}

UNIPROT = "https://rest.uniprot.org/uniprotkb/stream"
QUICKGO = "https://www.ebi.ac.uk/QuickGO/services/annotation/search"


def _get(url: str, accept: str = "application/json", attempts: int = 5) -> bytes:
    for i in range(attempts):
        try:
            req = urllib.request.Request(url, headers={"Accept": accept})
            with urllib.request.urlopen(req, timeout=180) as resp:
                return resp.read()
        except Exception:  # noqa: BLE001 - network retries
            if i == attempts - 1:
                raise
            time.sleep(2 ** i)
    raise RuntimeError("unreachable")


def te_accessions() -> dict[str, dict]:
    """Accession -> {taxon, reviewed, gene, name, pfam: set} for TE-domain proteins."""
    out: dict[str, dict] = {}
    for taxon in TAXA:
        for pfam in TE_PFAM:
            query = f"organism_id:{taxon} AND xref:pfam-{pfam}"
            url = (f"{UNIPROT}?query={urllib.parse.quote(query)}"
                   "&fields=accession,reviewed,gene_primary,protein_name&format=tsv")
            lines = _get(url, accept="text/plain").decode().splitlines()[1:]
            for line in lines:
                acc, reviewed, gene, name = (line.split("\t") + ["", "", "", ""])[:4]
                rec = out.setdefault(acc, {"taxon": taxon, "reviewed": reviewed == "reviewed",
                                           "gene": gene, "name": name, "pfam": set()})
                rec["pfam"].add(pfam)
    return out


def iba_rows(accessions: list[str]) -> list[dict]:
    rows = []
    for i in range(0, len(accessions), 100):
        batch = ",".join(accessions[i:i + 100])
        page = 1
        while True:
            url = (f"{QUICKGO}?geneProductId={batch}&goEvidence=IBA&limit=200&page={page}")
            data = json.loads(_get(url))
            rows.extend(data.get("results", []))
            info = data.get("pageInfo") or {}
            if page >= (info.get("total") or 1):
                break
            page += 1
    return rows


def term_names(go_ids: list[str]) -> dict[str, str]:
    names = {}
    for i in range(0, len(go_ids), 50):
        url = ("https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/"
               + ",".join(go_ids[i:i + 50]))
        for r in json.loads(_get(url)).get("results", []):
            names[r["id"]] = r["name"]
    return names


def ptn_of(row: dict) -> str:
    for group in row.get("withFrom") or []:
        for x in group.get("connectedXrefs", []):
            if x.get("db") == "PANTHER" and x.get("id", "").startswith("PTN"):
                return "PANTHER:" + x["id"]
    return "PANTHER:unknown"


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("-o", "--output", type=Path, required=True)
    args = ap.parse_args(argv)

    prots = te_accessions()
    rows = iba_rows(sorted(prots))
    names = term_names(sorted({r["goId"] for r in rows}))

    nodes: dict[str, dict] = {}
    for r in rows:
        acc = r["geneProductId"].split(":", 1)[1]
        p = prots.get(acc)
        if p is None:
            continue
        node = nodes.setdefault(ptn_of(r), {"terms": collections.defaultdict(set),
                                            "proteins": set()})
        node["terms"][r["goId"]].add(acc)
        node["proteins"].add(acc)

    def describe(acc: str) -> str:
        p = prots[acc]
        label = p["gene"] or p["name"]
        return f"UniProtKB:{acc} {label} ({TAXA[p['taxon']]})"

    summary = []
    for node_id, node in sorted(nodes.items(), key=lambda kv: -len(kv[1]["proteins"])):
        accs = sorted(node["proteins"])
        reviewed = [a for a in accs if prots[a]["reviewed"]]
        summary.append({
            "node": node_id,
            "te_domain_proteins": len(accs),
            "reviewed_proteins": [describe(a) for a in reviewed],
            "taxa": sorted({TAXA[prots[a]["taxon"]] for a in accs}),
            "terms": [{"go_id": g, "label": names.get(g, ""), "proteins": len(a)}
                      for g, a in sorted(node["terms"].items(), key=lambda kv: -len(kv[1]))],
            "examples": [describe(a) for a in accs if not prots[a]["reviewed"]][:5],
        })

    out = {
        "source": {
            "generated_by": "projects/TRANSPOSON_DERIVED_ANNOTATIONS/scripts/scan_te_iba.py",
            "run_date": datetime.date.today().isoformat(),
            "taxa": {str(k): v for k, v in TAXA.items()},
            "te_pfam_domains": TE_PFAM,
            "te_domain_proteins": len(prots),
            "te_domain_proteins_with_iba": len({r["geneProductId"] for r in rows}),
            "iba_rows": len(rows),
            "nodes": len(summary),
        },
        "nodes": summary,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(yaml.safe_dump(out, sort_keys=False, width=100, allow_unicode=True))
    print(json.dumps(out["source"], indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
