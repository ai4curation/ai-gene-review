#!/usr/bin/env python3
"""Analyze the RGD Pathway Ontology (PW) against GO, GO-CAM and our modules.

Inputs (from ``fetch_rgd_pathways.py``; cache default ``.cache/rgd_pw/``):
``pw.obo``, ``go-basic.obo``, ``homo_genes_pw``, ``hgnc_complete_set.txt``,
plus ``projects/RGD_PATHWAY_ONTOLOGY/pathways/*.yaml`` (parsed RGD diagram pages),
``gocams/index.tsv``, ``modules/*.yaml`` and ``genes/human/*``.

Outputs (``projects/RGD_PATHWAY_ONTOLOGY/data/``):

* ``pw_go_mappings.sssom.tsv`` -- candidate PW -> GO mappings, from two sources:
  GO ids that PW cites as a definition source (``def_xref``) and exact
  normalized label/synonym matches (``lexical``), plus the "associated GO
  term" that RGD diagram pages cite (``rgd_page_go_xref``). Every row is a *candidate*;
  ``predicate_id`` is conservative and no row is curator-verified.
* ``pw_gocam_completeness.tsv`` -- one row per PW term with human gene
  annotations: gene counts by evidence tier, how many of those genes appear in
  any human GO-CAM / have a gene review, the best-overlapping GO-CAM model, and
  GO-CAM models whose biological process falls under a mapped GO term.
* ``module_seeds.yaml`` -- one seed per RGD diagram pathway, joining the diagram
  structure (sub-pathways, labels), RGD-curated human genes, GO mappings,
  GO-CAM coverage and existing-module matches into a triage tier for module
  curation. Seeds are inputs to curation, not modules.
* ``summary.yaml`` -- headline counts used on the project page.

Nothing here asserts a GO annotation. Counts are recomputed from inputs; no
result is hardcoded.
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from collections import Counter, defaultdict
from datetime import date
from statistics import median
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[3]
PROJECT = ROOT / "projects" / "RGD_PATHWAY_ONTOLOGY"

BRANCHES = {
    "PW:0000002": "classic metabolic",
    "PW:0000003": "signaling",
    "PW:0000004": "regulatory",
    "PW:0000013": "disease",
    "PW:0000754": "drug",
}
MODULE_BRANCHES = {"classic metabolic", "signaling", "regulatory"}
# RGD's own curation (source column == RGD) excluding its electronic rows.
CURATED_EVIDENCE = {"TAS", "IDA", "IMP", "IGI", "IEP", "ISS", "ISO", "NAS", "IAGP", "EXP"}
MIN_SEED_GENES = 5
BROAD_GENES = 100


# --------------------------------------------------------------------------- OBO


def parse_obo(path: Path) -> dict[str, dict]:
    terms: dict[str, dict] = {}
    cur: dict | None = None
    in_term = False
    for line in path.read_text(errors="ignore").splitlines():
        if line.startswith("["):
            in_term = line.strip() == "[Term]"
            cur = None
            continue
        if not in_term or not line or ":" not in line:
            continue
        tag, _, val = line.partition(": ")
        if tag == "id":
            cur = terms.setdefault(
                val.strip(),
                {"id": val.strip(), "name": "", "namespace": "", "def_xrefs": [], "synonyms": [],
                 "is_a": [], "part_of": [], "obsolete": False, "replaced_by": []},
            )
            continue
        if cur is None:
            continue
        if tag == "name":
            cur["name"] = val.strip()
        elif tag == "namespace":
            cur["namespace"] = val.strip()
        elif tag == "def":
            m = re.search(r'"\s*\[(.*)\]\s*$', val)
            if m:
                cur["def_xrefs"] = [x.strip().split(" ")[0] for x in m.group(1).split(",") if x.strip()]
        elif tag == "synonym":
            m = re.match(r'"(.*)"\s+(EXACT|RELATED|NARROW|BROAD)', val)
            if m:
                cur["synonyms"].append((m.group(1), m.group(2)))
        elif tag == "is_a":
            cur["is_a"].append(val.split(" ")[0])
        elif tag == "relationship":
            parts = val.split(" ")
            if parts[0] == "part_of":
                cur["part_of"].append(parts[1])
        elif tag == "is_obsolete" and val.strip() == "true":
            cur["obsolete"] = True
        elif tag == "replaced_by":
            cur["replaced_by"].append(val.strip())
    return terms


def children_index(terms: dict[str, dict]) -> dict[str, set[str]]:
    kids: dict[str, set[str]] = defaultdict(set)
    for t in terms.values():
        for p in t["is_a"] + t["part_of"]:
            kids[p].add(t["id"])
    return kids


def descendants(tid: str, kids: dict[str, set[str]], memo: dict[str, frozenset]) -> frozenset:
    if tid in memo:
        return memo[tid]
    out = {tid}
    stack = [tid]
    while stack:
        for c in kids.get(stack.pop(), ()):
            if c not in out:
                out.add(c)
                stack.append(c)
    memo[tid] = frozenset(out)
    return memo[tid]


def ancestors(tid: str, terms: dict[str, dict]) -> set[str]:
    out, stack = set(), [tid]
    while stack:
        t = terms.get(stack.pop())
        if not t:
            continue
        for p in t["is_a"] + t["part_of"]:
            if p not in out:
                out.add(p)
                stack.append(p)
    return out


# ---------------------------------------------------------------- lexical match


def norm(s: str) -> str:
    s = s.lower().replace("signalling", "signaling")
    s = re.sub(r"[-_/,()']", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def pw_variants(name: str) -> set[str]:
    """GO-style renderings of a PW label (PW says 'pathway' where GO says 'process')."""
    n = norm(name)
    out = {n}
    rules = [
        (r" metabolic pathway$", " metabolic process"),
        (r" biosynthetic pathway$", " biosynthetic process"),
        (r" degradation pathway$", " catabolic process"),
        (r" catabolic pathway$", " catabolic process"),
        (r" pathway$", ""),
    ]
    for pat, rep in rules:
        if re.search(pat, n):
            out.add(re.sub(pat, rep, n))
    return {v for v in out if v}


# ------------------------------------------------------------------------- data


def load_rgd_annotations(path: Path) -> list[dict]:
    rows = []
    with open(path, errors="ignore") as fh:
        for line in fh:
            if line.startswith("!") or not line.strip():
                continue
            f = line.rstrip("\n").split("\t")
            if len(f) < 15 or "NOT" in f[3]:
                continue
            rows.append({"symbol": f[2], "term": f[4], "ref": f[5], "evidence": f[6], "source": f[14]})
    return rows


def load_hgnc(path: Path) -> tuple[dict[str, str], dict[str, str]]:
    sym2up: dict[str, str] = {}
    up2sym: dict[str, str] = {}
    with open(path, errors="ignore") as fh:
        for r in csv.DictReader(fh, delimiter="\t"):
            ups = [u for u in (r.get("uniprot_ids") or "").split("|") if u]
            if ups:
                sym2up[r["symbol"]] = ups[0]
                for u in ups:
                    up2sym.setdefault(u, r["symbol"])
    return sym2up, up2sym


def load_gocams(path: Path) -> tuple[dict[str, set[str]], dict[str, str], dict[str, set[str]]]:
    """Human GO-CAM index: symbol -> models, model -> title, model -> BP ids."""
    sym_models: dict[str, set[str]] = defaultdict(set)
    titles: dict[str, str] = {}
    model_bps: dict[str, set[str]] = defaultdict(set)
    with open(path) as fh:
        for r in csv.DictReader(fh, delimiter="\t"):
            titles[r["model_id"]] = r["model_title"]
            if r["biological_process"]:
                model_bps[r["model_id"]].add(r["biological_process"])
            if r["taxon"] == "NCBITaxon:9606" and r["gene_label"].endswith(" Hsap"):
                sym_models[r["gene_label"][: -len(" Hsap")]].add(r["model_id"])
    return sym_models, titles, model_bps


def load_modules(mod_dir: Path, up2sym: dict[str, str]) -> list[dict]:
    mods = []
    for f in sorted(mod_dir.glob("*.yaml")):
        txt = f.read_text(errors="ignore")
        title_m = re.search(r"^title:\s*(.+)$", txt, flags=re.M)
        ups = set(re.findall(r"UniProtKB:([A-Z0-9]{6,10})", txt))
        mods.append({
            "id": f.stem,
            "title": (title_m.group(1).strip().strip("'\"") if title_m else f.stem),
            "go": set(re.findall(r"GO:\d{7}", txt)),
            "pw": set(re.findall(r"PW:\d{7}", txt)),
            "symbols": {up2sym[u] for u in ups if u in up2sym},
        })
    return mods


def merge_go_maps(go_maps: list[dict]) -> list[dict]:
    """One entry per GO id; the strongest predicate wins, all sources are kept."""
    rank = {"skos:exactMatch": 0, "skos:closeMatch": 1, "skos:relatedMatch": 2}
    out: dict[str, dict] = {}
    for m in go_maps:
        e = out.setdefault(m["object_id"], {"id": m["object_id"], "label": m["object_label"],
                                             "predicate": m["predicate_id"], "sources": []})
        if rank[m["predicate_id"]] < rank[e["predicate"]]:
            e["predicate"] = m["predicate_id"]
        e["sources"].append(m["match_source"])
    return list(out.values())


# ------------------------------------------------------------------------- main


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--cache", type=Path, default=ROOT / ".cache" / "rgd_pw")
    ap.add_argument("--out", type=Path, default=PROJECT / "data")
    args = ap.parse_args()
    cache: Path = args.cache
    args.out.mkdir(parents=True, exist_ok=True)

    pw = parse_obo(cache / "pw.obo")
    go = parse_obo(cache / "go-basic.obo")
    pw_kids, go_kids = children_index(pw), children_index(go)
    pw_memo: dict[str, frozenset] = {}
    go_memo: dict[str, frozenset] = {}
    pw_live = {k: v for k, v in pw.items() if not v["obsolete"] and k != "PW:0000001"}

    def branch(tid: str) -> str:
        anc = ancestors(tid, pw) | {tid}
        hits = [BRANCHES[b] for b in BRANCHES if b in anc]
        return "|".join(sorted(hits)) or "other"

    # ---- PW -> GO candidate mappings
    go_index: dict[str, set[tuple[str, str]]] = defaultdict(set)
    for g in go.values():
        if g["obsolete"]:
            continue
        go_index[norm(g["name"])].add((g["id"], "label"))
        for syn, scope in g["synonyms"]:
            if scope == "EXACT":
                go_index[norm(syn)].add((g["id"], "exact_synonym"))

    page_xrefs: dict[str, list[str]] = {}
    for f in sorted((PROJECT / "pathways").glob("PW_*.yaml")):
        rec = yaml.safe_load(f.read_text())
        page_xrefs[rec["id"]] = [x for x in rec.get("description_xrefs", []) if x.startswith("GO:")]

    mappings: list[dict] = []
    for t in pw_live.values():
        seen: set[tuple[str, str]] = set()
        for x in page_xrefs.get(t["id"], []):
            g = go.get(x)
            status = "missing" if not g else ("obsolete" if g["obsolete"] else "ok")
            mappings.append({
                "subject_id": t["id"], "subject_label": t["name"],
                "predicate_id": "skos:closeMatch", "object_id": x,
                "object_label": g["name"] if g else "", "object_namespace": g["namespace"] if g else "",
                "mapping_justification": "semapv:ManualMappingCuration",
                "match_source": "rgd_page_go_xref", "object_status": status,
                "comment": "RGD pathway page cites this as the 'associated GO term'"
                + (f"; replaced_by {','.join(g['replaced_by'])}" if g and g["replaced_by"] else ""),
            })
        for x in t["def_xrefs"]:
            if not x.startswith("GO:") or (x, "def") in seen:
                continue
            seen.add((x, "def"))
            g = go.get(x)
            status = "missing" if not g else ("obsolete" if g["obsolete"] else "ok")
            mappings.append({
                "subject_id": t["id"], "subject_label": t["name"],
                "predicate_id": "skos:relatedMatch", "object_id": x,
                "object_label": g["name"] if g else "", "object_namespace": g["namespace"] if g else "",
                "mapping_justification": "semapv:ManualMappingCuration",
                "match_source": "pw_def_xref", "object_status": status,
                "comment": "GO id cited as a definition source in PW; scope not asserted"
                + (f"; replaced_by {','.join(g['replaced_by'])}" if g and g["replaced_by"] else ""),
            })
        names = [(t["name"], "label")] + [(s, "exact_synonym") for s, sc in t["synonyms"] if sc == "EXACT"]
        for nm, src in names:
            # verbatim rendering first, and GO labels before GO synonyms, so the
            # strongest evidence for a pair is the one recorded
            for v in sorted(pw_variants(nm), key=lambda v: (v != norm(nm), v)):
                for gid, gsrc in sorted(go_index.get(v, ()), key=lambda x: (x[1] != "label", x[0])):
                    if (gid, "lex") in seen:
                        continue
                    seen.add((gid, "lex"))
                    g = go[gid]
                    verbatim = v == norm(nm)
                    mappings.append({
                        "subject_id": t["id"], "subject_label": t["name"],
                        "predicate_id": "skos:exactMatch" if verbatim else "skos:closeMatch",
                        "object_id": gid, "object_label": g["name"], "object_namespace": g["namespace"],
                        "mapping_justification": "semapv:LexicalMatching",
                        "match_source": f"lexical:{src}->{gsrc}" + ("" if verbatim else ":pathway->process"),
                        "object_status": "ok", "comment": "",
                    })
    # ``comment`` is often empty, so it is not the last column (no trailing tab).
    # ---- QA for page-scraped GO ids: they are typed by hand on RGD pages and,
    # unlike definition citations, are not otherwise cross-checked. Demote a page
    # xref that disagrees with this subject's definition-citation or lexical
    # mappings (neither the same term nor an ancestor/descendant of one), and flag
    # a GO local id that repeats the PW local id (a likely typo). Flagged rows stay
    # in the SSSOM file but are not used for GO-CAM or module matching.
    others: dict[str, set[str]] = defaultdict(set)
    for m in mappings:
        if m["match_source"] != "rgd_page_go_xref" and m["object_status"] == "ok":
            others[m["subject_id"]].add(m["object_id"])
    page_flagged = {"disagrees": 0, "id_echo": 0}
    for m in mappings:
        if m["match_source"] != "rgd_page_go_xref":
            continue
        notes = []
        if m["object_id"].split(":")[1] == m["subject_id"].split(":")[1]:
            notes.append("GO local id equals PW local id (likely typo)")
            page_flagged["id_echo"] += 1
        alt = others.get(m["subject_id"], set())
        related = {d for o in alt for d in descendants(o, go_kids, go_memo)} | {
            a for o in alt for a in ancestors(o, go)}
        if alt and m["object_id"] not in alt | related:
            notes.append("disagrees with " + ",".join(sorted(alt)) + " from other sources")
            page_flagged["disagrees"] += 1
        if notes:
            m["predicate_id"] = "skos:relatedMatch"
            m["comment"] += "; QA: " + "; ".join(notes) + "; not used for matching"
            m["qa_flag"] = True

    mcols = ["subject_id", "subject_label", "predicate_id", "object_id", "object_label",
             "object_namespace", "mapping_justification", "comment", "match_source", "object_status"]
    with open(args.out / "pw_go_mappings.sssom.tsv", "w", newline="") as fh:
        fh.write("# curie_map:\n#   PW: http://purl.obolibrary.org/obo/PW_\n#   GO: http://purl.obolibrary.org/obo/GO_\n"
                 "#   skos: http://www.w3.org/2004/02/skos/core#\n#   semapv: https://w3id.org/semapv/vocab/\n"
                 "# mapping_set_id: https://github.com/ai4curation/ai-gene-review/blob/main/projects/RGD_PATHWAY_ONTOLOGY/data/pw_go_mappings.sssom.tsv\n"
                 f"# mapping_date: {date.today().isoformat()}\n"
                 "# comment: Candidate mappings generated by analyze_rgd_pathways.py; not curator-verified.\n")
        w = csv.DictWriter(fh, fieldnames=mcols, delimiter="\t", lineterminator="\n", extrasaction="ignore")
        w.writeheader()
        for m in sorted(mappings, key=lambda m: (m["subject_id"], m["object_id"])):
            w.writerow(m)

    by_pw_go: dict[str, list[dict]] = defaultdict(list)
    for m in mappings:
        if m["object_status"] == "ok" and m["object_namespace"] == "biological_process" \
                and not m.get("qa_flag"):
            by_pw_go[m["subject_id"]].append(m)

    # ---- gene sets
    ann = load_rgd_annotations(cache / "homo_genes_pw")
    direct_all: dict[str, set[str]] = defaultdict(set)
    direct_cur: dict[str, set[str]] = defaultdict(set)
    for a in ann:
        direct_all[a["term"]].add(a["symbol"])
        if a["source"] == "RGD" and a["evidence"] in CURATED_EVIDENCE:
            direct_cur[a["term"]].add(a["symbol"])

    def closure_genes(tid: str, direct: dict[str, set[str]]) -> set[str]:
        out: set[str] = set()
        for d in descendants(tid, pw_kids, pw_memo):
            out |= direct.get(d, set())
        return out

    sym2up, up2sym = load_hgnc(cache / "hgnc_complete_set.txt")
    sym_models, titles, model_bps = load_gocams(ROOT / "gocams" / "index.tsv")
    gocam_syms = set(sym_models)
    model_syms: dict[str, set[str]] = defaultdict(set)
    for sym, ms in sym_models.items():
        for m in ms:
            model_syms[m].add(sym)
    reviewed = {p.name for p in (ROOT / "genes" / "human").iterdir()
                if (p / f"{p.name}-ai-review.yaml").exists()}
    modules = load_modules(ROOT / "modules", up2sym)

    def go_closure(gids: list[str]) -> set[str]:
        out: set[str] = set()
        for g in gids:
            out |= descendants(g, go_kids, go_memo)
        return out

    rows = []
    for tid, t in sorted(pw_live.items()):
        genes_all = closure_genes(tid, direct_all)
        if not genes_all:
            continue
        genes_cur = closure_genes(tid, direct_cur)
        gene_basis = genes_cur if genes_cur else genes_all
        in_gocam = gene_basis & gocam_syms
        model_counts = Counter(m for s in gene_basis for m in sym_models.get(s, ()))
        best = model_counts.most_common(1)
        go_ids = sorted({m["object_id"] for m in by_pw_go.get(tid, [])})
        gclos = go_closure(go_ids)
        bp_models = sorted(m for m, bps in model_bps.items() if bps & gclos)
        in_matched = gene_basis & set().union(*(model_syms[m] for m in bp_models)) if bp_models else set()
        rows.append({
            "pw_id": tid, "pw_label": t["name"], "branch": branch(tid),
            "n_genes_all": len(genes_all), "n_genes_rgd_curated": len(genes_cur),
            "gene_basis": "rgd_curated" if genes_cur else "all",
            "n_basis_in_gocam": len(in_gocam),
            "frac_basis_in_gocam": round(len(in_gocam) / len(gene_basis), 3),
            "n_basis_reviewed": len(gene_basis & reviewed),
            "best_gocam_model": best[0][0] if best else "",
            "best_gocam_overlap": best[0][1] if best else 0,
            "best_gocam_title": titles.get(best[0][0], "") if best else "",
            "mapped_go_bp": "|".join(go_ids),
            "n_gocam_models_for_mapped_go": len(bp_models),
            "n_basis_in_matched_gocams": len(in_matched),
            "frac_basis_in_matched_gocams": round(len(in_matched) / len(gene_basis), 3),
            "gocam_models_for_mapped_go": "|".join(bp_models[:20]),
        })
    # Keep the often-empty model list away from the end of the row (no trailing tab).
    cols = [c for c in rows[0] if c != "gocam_models_for_mapped_go"]
    cols.insert(cols.index("n_gocam_models_for_mapped_go") + 1, "gocam_models_for_mapped_go")
    cols.remove("frac_basis_in_matched_gocams")
    cols.append("frac_basis_in_matched_gocams")
    with open(args.out / "pw_gocam_completeness.tsv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    row_by = {r["pw_id"]: r for r in rows}

    # ---- module seeds from RGD diagram pages
    seeds = []
    for f in sorted((PROJECT / "pathways").glob("PW_*.yaml")):
        rec = yaml.safe_load(f.read_text())
        tid = rec["id"]
        t = pw.get(tid, {})
        br = branch(tid)
        r = row_by.get(tid)
        cur = sorted(closure_genes(tid, direct_cur))
        go_maps = by_pw_go.get(tid, [])
        go_ids = sorted({m["object_id"] for m in go_maps})
        gclos = go_closure(go_ids)
        mod_hits = []
        for m in modules:
            reason = []
            if tid in m["pw"]:
                reason.append("cites PW id")
            if m["go"] & set(go_ids):
                reason.append("shares mapped GO term")
            elif m["go"] & gclos:
                reason.append("uses descendant of mapped GO term")
            shared = m["symbols"] & set(cur)
            if len(shared) >= 2 and len(shared) >= 0.5 * max(1, len(m["symbols"])):
                reason.append(f"{len(shared)}/{len(m['symbols'])} module genes in pathway")
            if reason:
                mod_hits.append({"module": m["id"], "title": m["title"], "basis": "; ".join(reason)})
        gene_grounded = any("cites PW id" in h["basis"] or "module genes" in h["basis"] for h in mod_hits)
        go_only = any("mapped GO term" in h["basis"] for h in mod_hits)
        # Disease ("altered ...") and drug pathways describe perturbed or
        # pharmacological states, not reusable normal-biology modules.
        title = (rec.get("title") or t.get("name") or "").lower()
        if "disease" in br or "drug" in br or title.startswith("altered ") \
                or not any(b in br for b in MODULE_BRANCHES):
            tier = "out_of_scope"
        elif gene_grounded:
            tier = "has_module"
        elif len(cur) < MIN_SEED_GENES:
            tier = "thin"
        elif go_only:
            tier = "related_module_only"
        elif not go_ids:
            tier = "needs_go_mapping"
        else:
            tier = "candidate"
        flags = []
        if len(cur) > BROAD_GENES:
            flags.append(f"broad: >{BROAD_GENES} curated genes; split along sub-pathways before modelling")
        seeds.append({
            "id": tid,
            "title": rec.get("title") or t.get("name"),
            "branch": br,
            "tier": tier,
            "flags": flags,
            "rgd_url": rec["rgd_url"],
            "diagram_image": rec.get("diagram_image"),
            "n_human_genes_rgd_curated": len(cur),
            "n_human_genes_all_sources": r["n_genes_all"] if r else 0,
            "frac_in_human_gocam": r["frac_basis_in_gocam"] if r else None,
            "n_reviewed": r["n_basis_reviewed"] if r else 0,
            "best_gocam": ({"model": r["best_gocam_model"], "title": r["best_gocam_title"],
                            "overlap": r["best_gocam_overlap"]} if r and r["best_gocam_model"] else None),
            "go_mappings": merge_go_maps(go_maps),
            "existing_modules": mod_hits,
            "subpathways": rec.get("diagram_pathway_links", []),
            "diagram_genes": [g["label"] for g in rec.get("diagram_gene_links", [])],
            "diagram_labels": rec.get("diagram_labels", []),
            "human_genes_rgd_curated": cur,
        })
    tier_order = {"candidate": 0, "related_module_only": 1, "needs_go_mapping": 2, "has_module": 3,
                  "thin": 4, "out_of_scope": 5}
    seeds.sort(key=lambda s: (tier_order[s["tier"]], -(s["n_human_genes_rgd_curated"]), s["id"]))
    with open(args.out / "module_seeds.yaml", "w") as fh:
        fh.write("# Generated by analyze_rgd_pathways.py -- module curation seeds, not modules.\n")
        yaml.safe_dump({"seeds": seeds}, fh, sort_keys=False, allow_unicode=True, width=100)

    # ---- agreement between PW's own GO citations and lexical matches
    defx: dict[str, set[str]] = defaultdict(set)
    lex: dict[str, set[str]] = defaultdict(set)
    for m in mappings:
        if m["object_status"] != "ok":
            continue
        if m["match_source"] == "pw_def_xref":
            defx[m["subject_id"]].add(m["object_id"])
        elif m["match_source"].startswith("lexical"):
            lex[m["subject_id"]].add(m["object_id"])
    both = [t for t in defx if t in lex]
    agree = sum(1 for t in both if defx[t] & lex[t])
    def_broader = sum(1 for t in both if not (defx[t] & lex[t]) and any(
        lx in descendants(d, go_kids, go_memo) for d in defx[t] for lx in lex[t]))

    # ---- diagram structure totals (from the parsed RGD pages)
    diagram_totals = Counter()
    for f in sorted((PROJECT / "pathways").glob("PW_*.yaml")):
        rec = yaml.safe_load(f.read_text())
        for key in ("diagram_edges", "diagram_gene_links", "diagram_chemicals", "diagram_pathway_links"):
            diagram_totals[key] += len(rec.get(key) or [])
    diagram_totals = dict(diagram_totals)

    # ---- summary
    diag_ids = {s["id"] for s in seeds}
    in_scope = [s["id"] for s in seeds if s["tier"] != "out_of_scope"]
    diag_rows = [row_by[i] for i in diag_ids if i in row_by]
    curated_rows = [r for r in rows if r["gene_basis"] == "rgd_curated" and r["n_genes_rgd_curated"] >= MIN_SEED_GENES]
    summary = {
        "generated": date.today().isoformat(),
        "pw_version": next((ln.split(": ", 1)[1] for ln in (cache / "pw.obo").read_text().splitlines()[:5]
                            if ln.startswith("data-version")), None),
        "go_version": next((ln.split(": ", 1)[1] for ln in (cache / "go-basic.obo").read_text().splitlines()[:5]
                            if ln.startswith("data-version")), None),
        "pw_terms_live": len(pw_live),
        "pw_terms_by_branch": dict(Counter(branch(t) for t in pw_live)),
        "pw_terms_with_go_def_xref": len({m["subject_id"] for m in mappings if m["match_source"] == "pw_def_xref"}),
        "pw_terms_with_rgd_page_go_xref": len({m["subject_id"] for m in mappings if m["match_source"] == "rgd_page_go_xref"}),
        "pw_terms_with_lexical_go_match": len({m["subject_id"] for m in mappings if m["match_source"].startswith("lexical")}),
        "pw_terms_with_any_ok_bp_mapping": len(by_pw_go),
        "pw_terms_with_def_xref_and_lexical_match": len(both),
        "def_xref_equals_lexical_match": agree,
        "def_xref_is_ancestor_of_lexical_match": def_broader,
        "def_xref_go_obsolete": sum(1 for m in mappings if m["match_source"] == "pw_def_xref" and m["object_status"] == "obsolete"),
        "def_xref_go_missing": sum(1 for m in mappings if m["match_source"] == "pw_def_xref" and m["object_status"] == "missing"),
        "rgd_page_go_xref_disagreeing": page_flagged["disagrees"],
        "rgd_page_go_xref_id_echo": page_flagged["id_echo"],
        "def_xref_go_not_bp": sum(1 for m in mappings if m["match_source"] == "pw_def_xref" and m["object_status"] == "ok" and m["object_namespace"] != "biological_process"),
        "human_pw_annotations_by_source_evidence": dict(Counter(f"{a['source']}:{a['evidence']}" for a in ann)),
        "pw_terms_with_human_genes": len(rows),
        "pw_terms_with_ge5_rgd_curated_human_genes": len(curated_rows),
        "diagram_pathways": len(seeds),
        "diagram_totals": diagram_totals,
        "diagram_pathways_by_tier": dict(Counter(s["tier"] for s in seeds)),
        "diagram_pathways_median_frac_in_gocam": sorted(r["frac_basis_in_gocam"] for r in diag_rows)[len(diag_rows) // 2] if diag_rows else None,
        "diagram_pathways_with_zero_gocam_genes": sum(1 for r in diag_rows if r["n_basis_in_gocam"] == 0),
        "diagram_pathways_with_gocam_for_mapped_go": sum(1 for r in diag_rows if r["n_gocam_models_for_mapped_go"] > 0),
        "diagram_pathways_median_frac_in_matched_gocams": sorted(r["frac_basis_in_matched_gocams"] for r in diag_rows)[len(diag_rows) // 2] if diag_rows else None,
        "in_scope_diagram_pathways": len(in_scope),
        "in_scope_median_frac_in_gocam": median([row_by[i]["frac_basis_in_gocam"] for i in in_scope if i in row_by]),
        "in_scope_with_ge_half_genes_in_gocam": sum(1 for i in in_scope if i in row_by and row_by[i]["frac_basis_in_gocam"] >= 0.5),
        "in_scope_with_any_gocam_for_mapped_go": sum(1 for i in in_scope if i in row_by and row_by[i]["n_gocam_models_for_mapped_go"] > 0),
        "in_scope_median_best_single_gocam_overlap": median([row_by[i]["best_gocam_overlap"] for i in in_scope if i in row_by]),
        "human_gocam_gene_symbols": len(gocam_syms),
    }
    with open(args.out / "summary.yaml", "w") as fh:
        yaml.safe_dump(summary, fh, sort_keys=False)
    print(yaml.safe_dump(summary, sort_keys=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
