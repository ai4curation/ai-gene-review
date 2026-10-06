"""Fetch the original YeastPathways (SGD Pathway Tools) BioPAX L3 exports and
distill them into a reviewable YAML summary.

YeastPathways (https://pathway.yeastgenome.org) is the SGD-curated YeastCyc PGDB.
The 189 `gomodel:YeastPathways_*` GO-CAMs cached under `gocams/` were produced from
these exports by the YeastPathways2GO converter (GO_REF:0000123); this script goes
back to the source BioPAX so that modules can be built against SGD's own
pathway definitions (reactions, EC numbers, catalysts, citations, comments)
rather than the converted GO-CAM.

Usage:
    uv run python projects/YEAST_PATHWAYS/scripts/fetch_yeastpathways_biopax.py \
        [--cache projects/YEAST_PATHWAYS/biopax] \
        [--out projects/YEAST_PATHWAYS/data/yeastpathways_summary.yaml]

Raw .owl files are cached (git-ignored); the YAML summary is committed.
"""

from __future__ import annotations

import argparse
import html
import re
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import rdflib
import yaml
from rdflib.namespace import RDF

BASE = "https://pathway.yeastgenome.org"
BP = rdflib.Namespace("http://www.biopax.org/release/biopax-level3.owl#")
PROTEOME: tuple[dict, dict] = ({}, {})
ORF_RE = re.compile(r"^(Y[A-P][LR]\d{3}[WC](?:-[A-Z])?|Q\d{4}|R\d{4}W|[A-Z0-9]+)-MONOMER$")


def list_pathways() -> list[str]:
    html = urllib.request.urlopen(
        f"{BASE}/YEAST/class-instances?object=Pathways", timeout=120
    ).read().decode("utf-8", "replace")
    ids = sorted(set(re.findall(r"object=([A-Za-z0-9+_.-]+)", html)))
    # the class page also links a few non-pathway browser classes
    skip = {"Pathways", "Compounds", "EC-Reactions", "Gene-Ontology-Terms"}
    return [i for i in ids if i not in skip]


def fetch(pid: str, cache: Path) -> Path:
    out = cache / f"{pid}.owl"
    if out.exists() and out.stat().st_size > 1000:
        return out
    url = f"{BASE}/YEAST/pathway-biopax?type=3&object={pid}"
    for attempt in range(4):
        try:
            data = urllib.request.urlopen(url, timeout=180).read()
            out.write_bytes(data)
            return out
        except Exception:  # noqa: BLE001 - network retry
            time.sleep(2 ** (attempt + 1))
    raise RuntimeError(f"failed to fetch {pid}")


def s(g, node, pred):
    v = g.value(node, pred)
    return str(v) if v is not None else None


def xrefs(g, node):
    out = []
    for x in g.objects(node, BP.xref):
        db, xid = s(g, x, BP.db), s(g, x, BP.id)
        if db and xid:
            out.append((db, xid))
    return out


def clean(text):
    if text is None:
        return None
    text = re.sub(r"<[^>]+>", "", html.unescape(text))
    return html.unescape(text).replace("\u2192", "->").replace("\u2190", "<-").replace("\u2194", "<->")


def entity_name(g, ent):
    return clean(s(g, ent, BP.standardName) or s(g, ent, BP.displayName) or s(g, ent, BP.name))


def gene_ids(g, ent, seen=None) -> list[str]:
    """Return YeastCyc ORF ids for a Protein or Complex (recursing components)."""
    seen = seen or set()
    if ent in seen:
        return []
    seen.add(ent)
    out = []
    types = set(g.objects(ent, RDF.type))
    if BP.Complex in types:
        for comp in g.objects(ent, BP.component):
            out += gene_ids(g, comp, seen)
        return out
    refs = [ent] + list(g.objects(ent, BP.entityReference))
    found = False
    for r in refs:
        for db, xid in xrefs(g, r):
            if db == "YeastCyc" and ORF_RE.match(xid) and not xid.startswith("MONOMER"):
                out.append("orf:" + xid[: -len("-MONOMER")])
                found = True
    if not found:
        # some YeastCyc frames (MONOMER3O-*) carry no ORF id; fall back to sequence
        for r in refs:
            seq = s(g, r, BP.sequence)
            if seq:
                out.append("seq:" + seq.strip().upper())
                break
    return sorted(set(out))


def load_proteome(cache: Path) -> tuple[dict, dict]:
    """Return ORF -> record and sequence -> record maps for the reviewed S. cerevisiae S288C proteome."""
    tsv = cache / "sce_proteome.tsv"
    if not tsv.exists():
        url = (
            "https://rest.uniprot.org/uniprotkb/stream?query=organism_id:559292+AND+reviewed:true"
            "&format=tsv&fields=accession,gene_primary,gene_oln,sequence"
        )
        tsv.write_bytes(urllib.request.urlopen(url, timeout=600).read())
    by_orf, by_seq = {}, {}
    for line in tsv.read_text().splitlines()[1:]:
        acc, sym, oln, seq = line.split("\t")
        rec = {"uniprot": f"UniProtKB:{acc}", "symbol": sym or None}
        for o in oln.replace(";", " ").split():
            by_orf[o] = {**rec, "orf": o}
        by_seq[seq] = {**rec, "orf": oln.split(";")[0].split()[0] if oln.strip() else None}
    return by_orf, by_seq


def resolve(keys, by_orf, by_seq):
    out = []
    for k in keys:
        kind, val = k.split(":", 1)
        rec = by_orf.get(val) if kind == "orf" else by_seq.get(val)
        if rec is None and kind == "orf" and val == "GCVH":  # YeastCyc legacy frame for GCV3
            rec = by_orf.get("YAL044C")
        out.append(rec or {"unresolved": val[:40]})
    uniq = {}
    for r in out:
        uniq[r.get("uniprot") or r.get("unresolved")] = r
    return sorted(uniq.values(), key=lambda r: r.get("symbol") or r.get("orf") or "")


def summarize(path: Path) -> dict:
    g = rdflib.Graph()
    g.parse(path, format="xml")
    pathways = list(g.subjects(RDF.type, BP.Pathway))
    # top pathway = one not referenced as a component of another
    comps = set(g.objects(None, BP.pathwayComponent))
    tops = [p for p in pathways if p not in comps] or pathways
    top = tops[0]

    def pathway_record(pw, depth=0):
        rec = {
            "name": entity_name(g, pw),
            "yeastcyc_id": next((x for db, x in xrefs(g, pw) if db == "YeastCyc"), None),
            "pmids": sorted({x for db, x in xrefs(g, pw) if db == "PubMed"}),
            "reactions": [],
            "subpathways": [],
        }
        comment = s(g, pw, BP.comment)
        if comment and depth == 0:
            rec["comment"] = re.sub(r"\s+", " ", clean(comment))[:4000]
        for c in g.objects(pw, BP.pathwayComponent):
            ctypes = set(g.objects(c, RDF.type))
            if BP.Pathway in ctypes:
                if depth < 3:
                    rec["subpathways"].append(pathway_record(c, depth + 1))
                continue
            if BP.Catalysis in ctypes or BP.Control in ctypes:
                continue
            rx = {
                "name": entity_name(g, c),
                "yeastcyc_id": next((x for db, x in xrefs(g, c) if db == "YeastCyc"), None),
                "ec": sorted({str(e) for e in g.objects(c, BP.eCNumber)}),
                "rhea": sorted({x for db, x in xrefs(g, c) if db.upper() == "RHEA"}),
                "left": sorted({entity_name(g, e) or "?" for e in g.objects(c, BP.left)}),
                "right": sorted({entity_name(g, e) or "?" for e in g.objects(c, BP.right)}),
                "genes": [],
                "pmids": sorted({x for db, x in xrefs(g, c) if db == "PubMed"}),
            }
            for cat in g.subjects(BP.controlled, c):
                for ctrl in g.objects(cat, BP.controller):
                    rx["genes"] += gene_ids(g, ctrl)
                rx["pmids"] = sorted(set(rx["pmids"]) | {x for db, x in xrefs(g, cat) if db == "PubMed"})
            rx["genes"] = sorted(set(rx["genes"]))
            rec["reactions"].append(rx)
        rec["reactions"].sort(key=lambda r: r["name"] or "")
        if not rec["subpathways"]:
            del rec["subpathways"]
        return rec

    rec = pathway_record(top)
    by_orf, by_seq = PROTEOME
    allg = {}

    def collect(r):
        for rx in r["reactions"]:
            rx["genes"] = resolve(rx["genes"], by_orf, by_seq)
            for gr in rx["genes"]:
                allg[gr.get("uniprot") or gr.get("unresolved")] = gr
        for sp in r.get("subpathways", []):
            collect(sp)

    collect(rec)
    rec["all_genes"] = sorted(allg.values(), key=lambda r: r.get("symbol") or r.get("orf") or "")
    return rec


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cache", default="projects/YEAST_PATHWAYS/biopax")
    ap.add_argument("--out", default="projects/YEAST_PATHWAYS/data/yeastpathways_summary.yaml")
    args = ap.parse_args()
    cache = Path(args.cache)
    cache.mkdir(parents=True, exist_ok=True)
    global PROTEOME
    PROTEOME = load_proteome(cache)
    pids = list_pathways()
    print(f"{len(pids)} pathways listed")
    with ThreadPoolExecutor(max_workers=4) as ex:
        paths = list(ex.map(lambda p: fetch(p, cache), pids))
    summary = {}
    for pid, path in zip(pids, paths):
        try:
            summary[pid] = summarize(path)
        except Exception as e:  # noqa: BLE001 - keep going, report
            summary[pid] = {"error": str(e)}
    Path(args.out).write_text(
        "# Generated by fetch_yeastpathways_biopax.py from YeastPathways BioPAX L3 exports; do not edit.\n"
        + yaml.safe_dump(summary, sort_keys=True, width=100, allow_unicode=True)
    )
    print(f"wrote {args.out}")


if __name__ == "__main__":
    main()
