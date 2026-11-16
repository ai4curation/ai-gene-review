"""Write a compact reading dossier for one human gene review.

Usage, from the ai-gene-review root:

    uv run python projects/DISMECH_VISION_ALIGNMENT/tools/make_dossier.py RHO OUT_DIR \
        --names "rhodopsin,opsin"

A reviewer otherwise opens the UniProt record, the review stub and every cited paper one
file at a time. The dossier puts what a review needs in one file: the UniProt comment
blocks and key features, the seeded annotation rows as a numbered table, and for each
cited reference its title, abstract and (for full-text papers) the paragraphs that
mention the gene. Paths are given so that exact quotes can be checked in the source.
Nothing here is evidence in its own right; quotes must be verified against the cached
source files, which stay authoritative.
"""
import argparse
import os
import re
import subprocess

import yaml

Loader = getattr(yaml, "CSafeLoader", yaml.SafeLoader)
KEEP_FT = ("BINDING", "ACT_SITE", "SITE", "MOD_RES", "LIPID", "CARBOHYD", "DISULFID", "MOTIF", "DOMAIN",
           "REGION", "DNA_BIND", "ZN_FING", "SIGNAL", "TRANSIT", "PROPEP", "CHAIN", "PEPTIDE", "TOPO_DOM",
           "TRANSMEM", "INTRAMEM", "COILED", "REPEAT", "CROSSLNK")
SKIP_CC = ("INTERACTION", "WEB RESOURCE", "SEQUENCE CAUTION", "MASS SPECTROMETRY", "RNA EDITING")


def uniprot_digest(path, max_ft=120):
    lines = open(path).read().splitlines()
    out, cc, ft, keep_cc = [], [], [], True
    for ln in lines:
        tag = ln[:2]
        if tag in ("ID", "AC", "DE", "GN", "OS", "KW") or (tag == "DR" and re.match(r"DR   (PANTHER|InterPro|Pfam|NCBIfam|PROSITE|Reactome|HGNC);", ln)):
            out.append(ln)
        elif tag == "CC":
            if ln.startswith("CC   -!- "):
                keep_cc = not any(ln.startswith(f"CC   -!- {s}") for s in SKIP_CC)
            if ln.startswith("CC   ---"):
                keep_cc = False
            if keep_cc:
                cc.append(ln)
        elif tag == "FT":
            ft.append(ln)
    feats, cur = [], None
    for ln in ft:
        m = re.match(r"FT   (\S+)\s+(\S+)", ln)
        if m and not ln.startswith("FT    "):
            cur = [m.group(1), ln]
            feats.append(cur)
        elif cur:
            cur.append(ln)
    counts = {}
    kept = []
    for f in feats:
        counts[f[0]] = counts.get(f[0], 0) + 1
        if f[0] in KEEP_FT and len(kept) < max_ft:
            kept.append("\n".join(f[1:]))
    summary = ", ".join(f"{k} x{v}" for k, v in sorted(counts.items()))
    return "\n".join(out) + "\n" + "\n".join(cc) + "\n\nFeature counts: " + summary + "\n\n" + "\n".join(kept)


def paper_digest(pmid, names, max_paras=8, max_chars=900):
    path = f"publications/PMID_{pmid}.md"
    if not os.path.exists(path):
        return f"(not cached: {path})"
    text = open(path).read()
    fm = {}
    if text.startswith("---"):
        end = text.index("\n---", 3)
        fm = yaml.load(text[3:end], Loader=Loader) or {}
        body = text[end + 4:]
    else:
        body = text
    abstract, full = body, ""
    if "## Full Text" in body:
        abstract, full = body.split("## Full Text", 1)
    abstract = re.sub(r"\n{3,}", "\n\n", abstract.split("## Abstract", 1)[-1]).strip()
    out = [f"path: {path}", f"title: {fm.get('title')}", f"journal: {fm.get('journal')} ({fm.get('year')}); "
           f"type: {fm.get('publication_type')}; full_text_available: {fm.get('full_text_available')}", "",
           "ABSTRACT:", abstract[:3500]]
    if full:
        pat = re.compile("|".join(re.escape(n) for n in names), re.I)
        paras = [p.strip() for p in re.split(r"\n\s*\n", full) if pat.search(p) and len(p.strip()) > 60]
        out += ["", f"FULL TEXT: {len(full)} characters, {len(paras)} paragraphs mention {'/'.join(names)}. "
                f"First {min(len(paras), max_paras)} (each cut at {max_chars} characters; read the file for more):"]
        for p in paras[:max_paras]:
            out.append("  > " + re.sub(r"\s+", " ", p)[:max_chars])
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("gene")
    ap.add_argument("out_dir")
    ap.add_argument("--names", default="", help="comma-separated protein names to search for in full texts")
    a = ap.parse_args()
    g = a.gene
    names = [g] + [n.strip() for n in a.names.split(",") if n.strip()]
    d = yaml.load(open(f"genes/human/{g}/{g}-ai-review.yaml"), Loader=Loader)
    rows = d.get("existing_annotations") or []
    parts = [f"# Review dossier: human {g} ({d.get('id')})", "",
             "Generated reading aid. Quotes must be checked against the source files named below.", "",
             "## 1. UniProt record (comment blocks, names, family cross-references, key features)", "",
             f"Source: genes/human/{g}/{g}-uniprot.txt (cite as file:human/{g}/{g}-uniprot.txt)", "", "```",
             uniprot_digest(f"genes/human/{g}/{g}-uniprot.txt"), "```", "",
             "## 2. Seeded annotation rows", "",
             "row | term | label | evidence | reference | qualifier | with/from", "---|---|---|---|---|---|---"]
    refs = []
    for i, r in enumerate(rows):
        t = r["term"]
        ref = r.get("original_reference_id", "")
        if ref and ref not in refs:
            refs.append(ref)
        extra = ("NOT " if r.get("negated") else "") + (f"isoform {r['isoform']} " if r.get("isoform") else "")
        parts.append(f"{i} | {t['id']} | {t['label']} | {r['evidence_type']} | {ref} | {extra}{r.get('qualifier', '')} | "
                     f"{', '.join(r.get('supporting_entities') or [])[:160]}")
    parts += ["", "## 3. Cited references", ""]
    titles = {r["id"]: r.get("title") for r in d.get("references") or []}
    for ref in refs:
        parts.append(f"### {ref}")
        if ref.startswith("PMID:"):
            parts.append(paper_digest(ref.split(":")[1], names))
        elif ref.startswith("Reactome:"):
            p = f"reactome/{ref.split(':')[1]}.md"
            parts.append(f"path: {p}\n" + (open(p).read()[:2500] if os.path.exists(p) else "(not cached)"))
        else:
            parts.append(f"title: {titles.get(ref)}")
        parts.append("")
    parts += ["## 4. PAINT losses on the gene's lineage", "", "```"]
    try:
        res = subprocess.run(["uv", "run", "python", "-m", "ai_gene_review.validation.gene_paint_losses", "human", g],
                             capture_output=True, text=True, timeout=300)
        parts.append(res.stdout.strip() or res.stderr.strip()[-600:])
    except Exception as exc:  # noqa: BLE001 - reported in the dossier, not fatal
        parts.append(f"(could not run paint-losses: {exc})")
    parts += ["```", "", "## 5. Other material in the gene folder", ""]
    for f in sorted(os.listdir(f"genes/human/{g}")):
        if os.path.isfile(f"genes/human/{g}/{f}"):
            parts.append(f"- genes/human/{g}/{f} ({os.path.getsize(f'genes/human/{g}/{f}')} bytes)")
    os.makedirs(a.out_dir, exist_ok=True)
    out = os.path.join(a.out_dir, f"{g}.md")
    open(out, "w").write("\n".join(parts) + "\n")
    print(out, os.path.getsize(out), "bytes;", len(rows), "rows;", len(refs), "references")


if __name__ == "__main__":
    main()
