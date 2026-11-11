#!/usr/bin/env python3
"""Fetch RGD Pathway Ontology (PW) inputs and the RGD interactive pathway pages.

Downloads (into a git-ignored cache, default ``.cache/rgd_pw/``):

* ``pw.obo`` -- the Pathway Ontology (OBO PURL)
* ``go-basic.obo`` -- GO, for lexical PW->GO matching
* ``homo_genes_pw`` / ``rattus_genes_pw`` -- RGD's PW gene annotation files
* ``hgnc_complete_set.txt`` -- HGNC symbol -> UniProt, for module/GO-CAM joins
* ``html/PW_NNNNNNN.html`` -- one RGD pathway-diagram page per pathway that has
  an interactive diagram. The list of such pathways is read from RGD's own
  "Select Pathway from List" page, so it is never hardcoded here.

Then parses every pathway page into a compact YAML record under
``projects/RGD_PATHWAY_ONTOLOGY/pathways/PW_NNNNNNN.yaml``:

* title and curated description (the RGD free text)
* GO / KEGG ids that RGD cites in the description trailer ("associated GO term")
* diagram image URL and the clickable image-map regions: links to other PW
  terms (sub-pathways / connected pathways), RGD gene reports, chemicals
  (ChEBI/PubChem/KEGG/HMDB), RGD disease terms, interaction edges
  ("A ---> B", "A ---| B", "A ---- B") and unlinked labels
* references cited on the page (RGD reference ids + citation strings)

Gene membership is deliberately NOT scraped from the HTML gene table: RGD's
bulk annotation files carry the same rows with evidence codes and sources, so
``analyze_rgd_pathways.py`` reads those instead.

Usage::

    uv run python projects/RGD_PATHWAY_ONTOLOGY/scripts/fetch_rgd_pathways.py
    uv run python projects/RGD_PATHWAY_ONTOLOGY/scripts/fetch_rgd_pathways.py --parse-only
"""

from __future__ import annotations

import argparse
import html
import re
import sys
import time
from pathlib import Path
from urllib.parse import unquote

import requests
import yaml

RGD = "https://rgd.mcw.edu"
LIST_URL = f"{RGD}/rgdweb/pathway/pathwayRecord.html?acc_id=PW:0000034"
RECORD_URL = (
    f"{RGD}/rgdweb/pathway/pathwayRecord.html?processType=view&species=Rat&acc_id={{acc}}"
)
DOWNLOADS = {
    "pw.obo": "http://purl.obolibrary.org/obo/pw.obo",
    "go-basic.obo": "http://purl.obolibrary.org/obo/go/go-basic.obo",
    "homo_genes_pw": "https://download.rgd.mcw.edu/data_release/annotated_rgd_objects_by_ontology/homo_genes_pw",
    "rattus_genes_pw": "https://download.rgd.mcw.edu/data_release/annotated_rgd_objects_by_ontology/rattus_genes_pw",
    "hgnc_complete_set.txt": "https://storage.googleapis.com/public-download-files/hgnc/tsv/tsv/hgnc_complete_set.txt",
}

# RGD returns 403 to the default python-requests User-Agent.
HEADERS = {"User-Agent": "ai-gene-review RGD_PATHWAY_ONTOLOGY fetcher (+https://github.com/ai4curation/ai-gene-review)"}

# Newer (Pathway Studio) diagrams encode interactions as unlinked image-map
# regions whose alt text is "A ---> B" (activation), "A ---| B" (inhibition),
# "A ---- B" (binding/association) or "A <--> B".
EDGE_TYPES = {"--->": "positively_affects", "---|": "negatively_affects", "----": "associated_with",
              "<-->": "mutually_affects"}
EDGE_RE = re.compile(r"^(.+?)\s+(--->|---\||----|<-->)\s+(.+)$")
CHEMICAL_HOSTS = ("pubchem.ncbi", "ebi.ac.uk/chebi", "hmdb.ca", "genome.jp/dbget-bin/www_bget?cpd",
                  "pccompound")
VENDOR_HOSTS = ("ariadnegenomics", "pathwaystudio.com")

ROOT = Path(__file__).resolve().parents[3]
PROJECT = ROOT / "projects" / "RGD_PATHWAY_ONTOLOGY"


def fetch(url: str, dest: Path, force: bool = False) -> Path:
    if dest.exists() and dest.stat().st_size > 0 and not force:
        return dest
    dest.parent.mkdir(parents=True, exist_ok=True)
    for attempt in range(4):
        try:
            r = requests.get(url, timeout=120, headers=HEADERS)
            r.raise_for_status()
            dest.write_bytes(r.content)
            return dest
        except requests.RequestException as e:  # pragma: no cover - network
            wait = 2 ** (attempt + 1)
            print(f"  retry {url} in {wait}s ({e})", file=sys.stderr)
            time.sleep(wait)
    raise RuntimeError(f"failed to fetch {url}")


def text(fragment: str) -> str:
    fragment = re.sub(r"<script.*?</script>|<style.*?</style>", "", fragment, flags=re.S)
    s = html.unescape(re.sub(r"<[^>]+>", " ", fragment))
    return re.sub(r"\s+", " ", s).strip()


def chemical_curie(url: str) -> str:
    """Normalize a chemical link to a CURIE where the id is recoverable; else keep the URL."""
    url = unquote(url)
    for pat, prefix in (
        (r"chebiId=(?:CHEBI:)?(\d+)", "CHEBI:"),
        (r"[?&]sid=(\d+)", "PUBCHEM.SUBSTANCE:"),
        (r"substance/(\d+)", "PUBCHEM.SUBSTANCE:"),
        (r"[?&]cid=(\d+)", "PUBCHEM.COMPOUND:"),
        (r"term=(\d+)\[uid\]", "PUBCHEM.COMPOUND:"),
        (r"compound/(\d+)", "PUBCHEM.COMPOUND:"),
        (r"www_bget\?cpd[:+](C\d{5})", "KEGG.COMPOUND:"),
        (r"metabolites/(hmdb\d+)", "HMDB:"),
    ):
        m = re.search(pat, url, flags=re.I)
        if m:
            return prefix + (m.group(1).upper() if prefix == "HMDB:" else m.group(1))
    return url


def diagram_accessions(list_html: str) -> list[str]:
    return sorted(set(re.findall(r"processType=view&species=Rat&acc_id=(PW:\d{7})", list_html)))


def parse_record(acc: str, page: str) -> dict:
    rec: dict = {"id": acc, "rgd_url": RECORD_URL.format(acc=acc)}
    m = re.search(r'<h3 align="justify">(.*?)\(PW:\d{7}\)\s*</h3>', page, flags=re.S)
    rec["title"] = text(m.group(1)).lower() if m else None

    # Description: between the Description header and the Pathway Diagram header.
    m = re.search(r"<h3 align=\"justify\">Description</h3>(.*?)<h3>Pathway Diagram", page, flags=re.S)
    if m:
        desc = text(m.group(1))
        desc = re.sub(r"\s*\.\.\.\(more\)\s*", "", desc)
        desc = re.sub(r"\s*\.\.\.\(less\)\s*", "", desc)
        tail = re.search(r"\s*To see the ontology( report)?\b.*$", desc, flags=re.I)
        if tail:
            xrefs = sorted(set(
                re.findall(r"GO:\d{7}", tail.group(0))
                + [f"KEGG:{k}" for k in re.findall(r"\b(map\d{5})\b", tail.group(0))]
            ))
            if xrefs:
                rec["description_xrefs"] = xrefs
            desc = desc[: tail.start()]
        rec["description"] = desc.strip()

    img = re.search(r'<IMG[^>]+SRC="(/pathway/[^"]+)"[^>]*USEMAP', page, flags=re.I)
    rec["diagram_image"] = RGD + img.group(1) if img else None
    gpp = re.search(r'href="(/pathway/[^"]+\.gpp)"', page)
    rec["pathway_studio_file"] = RGD + gpp.group(1).replace(" ", "%20") if gpp else None

    linked_pathways: dict[str, str] = {}
    linked_genes: dict[str, str] = {}
    chemicals: dict[str, str] = {}
    diseases: dict[str, str] = {}
    edges: list[dict] = []
    labels: set[str] = set()
    other_links: dict[str, str] = {}
    m = re.search(r'<MAP[^>]*NAME="pwmap"[^>]*>(.*?)</MAP>', page, flags=re.S | re.I)
    if m:
        for area in re.findall(r"<AREA([^>]*)>", m.group(1), flags=re.I):
            href = re.search(r'HREF="([^"]*)"', area, flags=re.I)
            alt = re.search(r'ALT="([^"]*)"', area, flags=re.I)
            alt_s = re.sub(r"\s+", " ", html.unescape(alt.group(1))).strip() if alt else ""
            h = html.unescape(href.group(1)) if href else ""
            onto = re.search(r"acc_id=([A-Z]+:\d+)", h)
            gene = re.search(r"report/gene/main\.html\?id=(\d+)", h)
            edge = EDGE_RE.match(alt_s) if not h else None
            if onto and onto.group(1).startswith("PW:"):
                if onto.group(1) != acc:
                    linked_pathways[onto.group(1)] = alt_s
            elif onto and onto.group(1).startswith("CHEBI:"):
                chemicals[onto.group(1)] = alt_s
            elif onto and onto.group(1).startswith(("RDO:", "DOID:")):
                diseases[onto.group(1)] = alt_s
            elif gene:
                linked_genes[f"RGD:{gene.group(1)}"] = alt_s
            elif h and any(k in h for k in CHEMICAL_HOSTS):
                chemicals[chemical_curie(h)] = alt_s
            elif edge:
                edges.append({"source": edge.group(1).strip(), "relation": EDGE_TYPES[edge.group(2)],
                              "target": edge.group(3).strip()})
            elif h and not any(k in h for k in VENDOR_HOSTS):
                other_links[h] = alt_s
            elif alt_s and not h:
                labels.add(alt_s)
    rec["diagram_pathway_links"] = [
        {"id": k, "label": v} for k, v in sorted(linked_pathways.items())
    ]
    rec["diagram_gene_links"] = [
        {"id": k, "label": v} for k, v in sorted(linked_genes.items(), key=lambda kv: kv[1].lower())
    ]
    rec["diagram_chemicals"] = [
        {"id": k, "label": v} for k, v in sorted(chemicals.items(), key=lambda kv: kv[1].lower())
    ]
    if diseases:
        rec["diagram_diseases"] = [{"id": k, "label": v} for k, v in sorted(diseases.items())]
    uniq_edges = {(e["source"], e["relation"], e["target"]): e for e in edges}
    rec["diagram_edges"] = [uniq_edges[k] for k in sorted(uniq_edges)]
    rec["diagram_labels"] = sorted(labels, key=str.lower)
    if other_links:
        rec["diagram_other_links"] = [{"href": k, "label": v} for k, v in sorted(other_links.items())]

    refs = []
    m = re.search(r'<a name="References">(.*?)</ul>', page, flags=re.S)
    if m:
        for rid, cit in re.findall(
            r'<a href="/rgdweb/report/reference/main\.html\?id=(\d+)">(.*?)</a>', m.group(1), flags=re.S
        ):
            refs.append({"id": f"RGD:{rid}", "citation": text(cit)})
    rec["references"] = refs
    return rec


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--cache", type=Path, default=ROOT / ".cache" / "rgd_pw")
    ap.add_argument("--out", type=Path, default=PROJECT / "pathways")
    ap.add_argument("--parse-only", action="store_true", help="do not hit the network")
    ap.add_argument("--force", action="store_true", help="re-download cached files")
    ap.add_argument("--delay", type=float, default=0.5, help="seconds between page fetches")
    args = ap.parse_args()

    cache: Path = args.cache
    if not args.parse_only:
        for name, url in DOWNLOADS.items():
            print(f"fetch {name}")
            fetch(url, cache / name, force=args.force)
        fetch(LIST_URL, cache / "pathway_list.html", force=True)

    accs = diagram_accessions((cache / "pathway_list.html").read_text(errors="ignore"))
    print(f"{len(accs)} pathways with RGD diagram pages")
    args.out.mkdir(parents=True, exist_ok=True)
    for i, acc in enumerate(accs, 1):
        dest = cache / "html" / f"{acc.replace(':', '_')}.html"
        if not args.parse_only and not dest.exists():
            print(f"[{i}/{len(accs)}] {acc}")
            fetch(RECORD_URL.format(acc=acc), dest)
            time.sleep(args.delay)
        if not dest.exists():
            print(f"  missing page for {acc}", file=sys.stderr)
            continue
        rec = parse_record(acc, dest.read_text(errors="ignore"))
        with open(args.out / f"{acc.replace(':', '_')}.yaml", "w") as fh:
            yaml.safe_dump(rec, fh, sort_keys=False, allow_unicode=True, width=100)
    return 0


if __name__ == "__main__":
    sys.exit(main())
