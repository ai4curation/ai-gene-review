"""Summarize the Arabidopsis (ARATH) corpus across gene reviews, modules,
PANTHER family reviews, GO-CAMs, prediction reviews and project pages.

Run from the repository root:

    uv run python projects/ARATH/scripts/arath_corpus_stats.py

Writes projects/ARATH/ARATH-corpus-stats.yaml. Everything is computed from
files in the repository; nothing is hardcoded.
"""

from __future__ import annotations

import csv
import re
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[3]
GENES = ROOT / "genes" / "ARATH"
OUT = ROOT / "projects" / "ARATH" / "ARATH-corpus-stats.yaml"

EXPERIMENTAL = {"EXP", "IDA", "IPI", "IMP", "IGI", "IEP", "HDA", "HMP", "HGI", "HEP", "HTP"}
PHYLO = {"IBA", "IBD", "IKR", "IRD"}
ELECTRONIC = {"IEA"}
AUTHOR = {"TAS", "NAS", "IC", "ND"}
SIMILARITY = {"ISS", "ISO", "ISA", "ISM", "RCA", "IGC"}


def evidence_class(code: str | None) -> str:
    if not code:
        return "none"
    if code in EXPERIMENTAL:
        return "experimental"
    if code in PHYLO:
        return "phylogenetic"
    if code in ELECTRONIC:
        return "electronic"
    if code in SIMILARITY:
        return "similarity"
    if code in AUTHOR:
        return "author/curator"
    return "other"


def load(path: Path):
    with path.open() as fh:
        return yaml.safe_load(fh)


XTAB: dict[str, Counter] = defaultdict(Counter)
TERM_ACTIONS: dict[tuple[str, str], Counter] = defaultdict(Counter)


def gene_reviews():
    rows = []
    folders_without_review = []
    for d in sorted(p for p in GENES.iterdir() if p.is_dir()):
        f = d / f"{d.name}-ai-review.yaml"
        if not f.exists():
            folders_without_review.append(d.name)
            continue
        doc = load(f) or {}
        anns = doc.get("existing_annotations") or []
        actions = Counter()
        ev_class = Counter()
        pending = 0
        for a in anns:
            act = (a.get("review") or {}).get("action") or "NONE"
            if act in ("PENDING", "NONE"):
                pending += 1
            actions[act] += 1
            ev_class[evidence_class(a.get("evidence_type"))] += 1
            XTAB[evidence_class(a.get("evidence_type"))][act] += 1
            term = a.get("term") or {}
            TERM_ACTIONS[(term.get("id"), term.get("label"))][act] += 1
        cfs = doc.get("core_functions") or []
        rows.append(
            {
                "folder": d.name,
                "id": doc.get("id"),
                "gene_symbol": doc.get("gene_symbol"),
                "status": doc.get("status"),
                "n_annotations": len(anns),
                "n_pending": pending,
                "actions": dict(actions),
                "evidence_classes": dict(ev_class),
                "n_core_functions": len(cfs),
                "n_proposed_new_terms": len(doc.get("proposed_new_terms") or []),
                "n_references": len(doc.get("references") or []),
                "has_deep_research": any(d.glob(f"{d.name}-deep-research*.md")),
                "has_notes": (d / f"{d.name}-notes.md").exists(),
                "has_bioinformatics": (d / f"{d.name}-bioinformatics").is_dir(),
                "prediction_reviews": sorted(p.name for p in d.glob("*predictions-review.yaml")),
            }
        )
    return rows, folders_without_review


def modules(acc2folder):
    out = []
    for f in sorted((ROOT / "modules").glob("*.yaml")):
        text = f.read_text()
        accs = set(re.findall(r"UniProtKB:([A-Z0-9]+)", text))
        hits = sorted({acc2folder[a] for a in accs if a in acc2folder})
        refs = sorted(set(re.findall(r"genes/ARATH/([A-Za-z0-9_.-]+)/", text)))
        members = sorted(set(hits) | set(refs))
        if not members and "Arabidopsis" not in text:
            continue
        doc = load(f) or {}
        out.append(
            {
                "module": f.stem,
                "title": doc.get("title"),
                "status": doc.get("status"),
                "arath_reviewed_members": members,
            }
        )
    return out


def families():
    out = []
    for f in sorted((ROOT / "interpro" / "panther").glob("*/*-review.yaml")):
        text = f.read_text()
        members = sorted(set(re.findall(r"genes/ARATH/([A-Za-z0-9_.-]+)/", text)))
        if not members:
            continue
        doc = load(f) or {}
        out.append(
            {
                "family_id": doc.get("family_id"),
                "family_name": doc.get("family_name"),
                "functional_coherence": doc.get("functional_coherence"),
                "arath_reviewed_members": members,
                "path": str(f.relative_to(ROOT)),
            }
        )
    return out


def gocams():
    models = defaultdict(set)
    with (ROOT / "gocams" / "index.tsv").open() as fh:
        for r in csv.DictReader(fh, delimiter="\t"):
            if r["taxon"] == "NCBITaxon:3702":
                models[(r["model_id"], r["model_title"])].add(r["gene_label"])
    return [
        {"model_id": m, "title": t, "genes": sorted(g)} for (m, t), g in sorted(models.items())
    ]


def projects():
    out = []
    for f in sorted((ROOT / "projects").glob("*.md")):
        if f.stem in ("ARATH", "README"):
            continue
        text = f.read_text()
        m = re.match(r"---\n(.*?)\n---", text, re.S)
        fm = yaml.safe_load(m.group(1)) if m else {}
        species = (fm or {}).get("species") or []
        if "ARATH" in species:
            out.append({"project": f.stem, "title": fm.get("title"), "species": species})
    return out


def main():
    rows, missing = gene_reviews()
    acc2folder = {r["id"]: r["folder"] for r in rows if r["id"]}
    totals = Counter()
    ev_totals = Counter()
    for r in rows:
        totals.update(r["actions"])
        ev_totals.update(r["evidence_classes"])
    mods = modules(acc2folder)
    fams = families()
    in_module = {g for m in mods for g in m["arath_reviewed_members"]}
    in_family = {g for f in fams for g in f["arath_reviewed_members"]}
    summary = {
        "generated": date.today().isoformat(),
        "n_gene_folders": len(rows) + len(missing),
        "n_gene_reviews": len(rows),
        "folders_without_review": missing,
        "review_status": dict(Counter(str(r["status"]) for r in rows)),
        "n_annotations": sum(r["n_annotations"] for r in rows),
        "n_annotations_pending": sum(r["n_pending"] for r in rows),
        "action_totals": dict(totals.most_common()),
        "evidence_class_totals": dict(ev_totals.most_common()),
        "n_reviews_with_deep_research": sum(r["has_deep_research"] for r in rows),
        "n_reviews_with_bioinformatics": sum(r["has_bioinformatics"] for r in rows),
        "n_reviews_with_no_core_functions": sum(r["n_core_functions"] == 0 for r in rows),
        "n_reviews_in_a_module": len(in_module),
        "n_reviews_in_a_family_review": len(in_family),
        "n_modules": len(mods),
        "n_family_reviews": len(fams),
        "n_gocam_models_indexed": len(gocams()),
    }
    def top_terms(action, n=15):
        ranked = sorted(TERM_ACTIONS.items(), key=lambda kv: -kv[1][action])
        return [
            {"id": t[0], "label": t[1], "count": c[action], "total_rows": sum(c.values())}
            for t, c in ranked[:n]
            if c[action]
        ]

    doc = {
        "summary": summary,
        "action_by_evidence_class": {k: dict(v.most_common()) for k, v in XTAB.items()},
        "most_removed_terms": top_terms("REMOVE"),
        "most_modified_terms": top_terms("MODIFY"),
        "most_over_annotated_terms": top_terms("MARK_AS_OVER_ANNOTATED"),
        "most_proposed_new_terms": top_terms("NEW"),
        "projects": projects(),
        "modules": mods,
        "families": fams,
        "gocams": gocams(),
        "genes": rows,
    }
    OUT.write_text(yaml.safe_dump(doc, sort_keys=False, width=100))
    print(yaml.safe_dump(summary, sort_keys=False))


if __name__ == "__main__":
    main()
