"""Pilot A (gene view): are a gene's top tissues explained by its reviewed functions?

PAX6 is expressed in the eye; a reviewed PAX6 annotation such as ``eye
development`` (results_in_development_of UBERON:0000970 eye) should explain it.
For each gene this takes the top Bgee tissues (gold present calls, highest
expression score first, collapsing entities nested in one already taken) and
asks which retained annotations (ACCEPT, KEEP_AS_NON_CORE, MODIFY, NEW) name an
anatomy that contains, lies within, or develops into that tissue.

Unexplained top tissues are of two kinds a curator can tell apart: a function
the review is missing, or expression without a function there (leaky, or a
housekeeping role). The script reports them; it does not decide which.

A shuffled baseline (each gene scored against another gene's annotations)
shows how much explanation is expected by chance.

Outputs: ``results/tissue_explanation.yaml`` (corpus summary and case studies),
``results/tissue_explanation_cases.md`` (tables), and
``data/case_study_calls_human.tsv`` (the Bgee calls behind the case studies).

Usage (from repo root, after extract_corpus.py):
    uv run python projects/BGEEDB_EXPRESSION/scripts/explain_tissues.py
"""

from __future__ import annotations

import csv
import pickle
import random
import statistics
import sys
from collections import defaultdict
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).parent))
import bgee_common as bc  # noqa: E402

TOP_K = 10
SEED = 20261108
RETAINED = {"ACCEPT", "KEEP_AS_NON_CORE", "MODIFY", "NEW"}
REJECTED = {"REMOVE", "MARK_AS_OVER_ANNOTATED"}
CASES = [
    "PAX6", "ATOH1", "NEUROD1", "OLIG2", "MITF", "CRYAA", "INS", "GCG", "ALB", "HNF1A",
    "GATA1", "TH", "FOXN1", "AIRE",
    "GBX2", "FGF8", "PTF1A", "RORA", "RELN", "SHH", "SMO", "FBXO41", "DNER", "PTPN11", "EN1", "EN2",
    "G6PC1", "G6PC3",
]


def top_tissues(calls: list[bc.Call], anat: bc.Anatomy, k: int = TOP_K) -> list[bc.Call]:
    """Highest-scoring gold present calls, skipping entities nested in one taken."""
    taken: list[bc.Call] = []
    for c in sorted((c for c in calls if c.state == "present" and c.quality == "gold"), key=lambda c: -c.score):
        if c.entity in bc.CONTAINER_EXCLUDE:
            continue
        if any(anat.within(c.entity, t.entity) or anat.within(t.entity, c.entity) for t in taken):
            continue
        taken.append(c)
        if len(taken) == k:
            break
    return taken


def anatomy_terms(rows: list[dict], go: bc.GoAnatomy, actions: set[str]) -> dict[str, set[str]]:
    """GO term -> anatomy targets, for the gene's annotations with these actions."""
    out: dict[str, set[str]] = {}
    for r in rows:
        if r["negated"] or r["action"] not in actions:
            continue
        tg, _, _ = go.targets(r["go_id"])
        if tg:
            out[r["go_id"]] = {a for _, a in tg}
    return out


def explain(tissues: list[bc.Call], terms: dict[str, set[str]], anat: bc.Anatomy) -> list[dict]:
    """Per tissue: explaining terms, specific ones first (``broad`` = target is a huge structure)."""
    out = []
    for c in tissues:
        hits = []
        for gid, targets in sorted(terms.items()):
            how = bc.explain_tissue(c.entity, targets, anat)
            if how:
                hits.append((gid, how))
        hits.sort(key=lambda h: (h[1][2], anat.descendant_count(h[1][1]), h[0]))
        specific = any(not h[1][2] for h in hits)
        out.append({"entity": c.entity, "name": c.name, "score": c.score, "explained_by": hits,
                    "specific": specific})
    return out


def main() -> None:
    go = bc.load_go_anatomy()
    anat = bc.load_anatomy()
    with (bc.CACHE / "corpus_calls.pkl").open("rb") as fh:
        blob = pickle.load(fh)
    calls = blob["calls"]
    by_gene: dict[str, list[dict]] = defaultdict(list)
    ens_of: dict[str, str] = {}
    with (bc.CACHE / "corpus_annotations.tsv").open() as fh:
        for r in csv.DictReader(fh, delimiter="\t"):
            by_gene[r["gene"]].append(r)
            ens_of[r["gene"]] = r["ensembl"]

    retained = {g: anatomy_terms(rows, go, RETAINED) for g, rows in by_gene.items()}
    rejected = {g: anatomy_terms(rows, go, REJECTED) for g, rows in by_gene.items()}
    genes = sorted(g for g in by_gene if retained[g] and ens_of[g] in calls)
    rng = random.Random(SEED)

    real_frac, shuf_frac, top1_real, top1_shuf = [], [], 0, 0
    real_spec, shuf_spec = [], []
    rej_only = 0
    total_top = 0
    for g in genes:
        tissues = top_tissues(calls[ens_of[g]], anat)
        if not tissues:
            continue
        ex = explain(tissues, retained[g], anat)
        other = genes[rng.randrange(len(genes))]
        ex_s = explain(tissues, retained[other], anat)
        ex_rej = explain(tissues, rejected[g], anat)
        n_ex = sum(1 for e in ex if e["explained_by"])
        real_frac.append(n_ex / len(tissues))
        shuf_frac.append(sum(1 for e in ex_s if e["explained_by"]) / len(tissues))
        real_spec.append(sum(1 for e in ex if e["specific"]) / len(tissues))
        shuf_spec.append(sum(1 for e in ex_s if e["specific"]) / len(tissues))
        top1_real += bool(ex[0]["explained_by"])
        top1_shuf += bool(ex_s[0]["explained_by"])
        rej_only += sum(1 for a, b in zip(ex, ex_rej) if not a["explained_by"] and b["explained_by"])
        total_top += len(tissues)

    summary = {
        "bgee_release": bc.BGEE_RELEASE,
        "top_k_tissues": TOP_K,
        "genes_with_anatomy_bearing_retained_annotations": len(real_frac),
        "mean_fraction_top_tissues_explained": round(statistics.mean(real_frac), 3),
        "mean_fraction_explained_shuffled": round(statistics.mean(shuf_frac), 3),
        "mean_fraction_explained_specifically": round(statistics.mean(real_spec), 3),
        "mean_fraction_explained_specifically_shuffled": round(statistics.mean(shuf_spec), 3),
        "broad_target_threshold_descendants": bc.BROAD_TARGET,
        "top_tissue_explained": round(top1_real / len(real_frac), 3),
        "top_tissue_explained_shuffled": round(top1_shuf / len(real_frac), 3),
        "top_tissues_explained_only_by_rejected_annotations": f"{rej_only}/{total_top}",
    }

    cases = {}
    case_calls: dict[str, list[bc.Call]] = {}
    lines = ["---", 'title: "Top Bgee tissues and the reviewed annotations that explain them"', "species: [human]", "---", "",
             "# Top Bgee tissues and the reviewed annotations that explain them", "",
             f"Bgee release: {bc.BGEE_RELEASE}. Top {TOP_K} non-redundant gold present calls per gene; "
             "explanation = a retained annotation whose GO anatomy contains (within), develops into (precursor) "
             "or lies inside (container) the tissue. Generated by `scripts/explain_tissues.py`; do not edit.", ""]
    for g in CASES:
        if g not in by_gene or ens_of[g] not in calls:
            continue
        case_calls[ens_of[g]] = calls[ens_of[g]]
        tissues = top_tissues(calls[ens_of[g]], anat)
        ex = explain(tissues, retained[g], anat)
        ex_rej = explain(tissues, rejected[g], anat)
        n_ex = sum(1 for e in ex if e["explained_by"])
        n_spec = sum(1 for e in ex if e["specific"])
        cases[g] = {
            "explained": f"{n_ex}/{len(ex)}",
            "explained_specifically": f"{n_spec}/{len(ex)}",
            "tissues": [
                {
                    "tissue": f"{e['entity']} {e['name']}",
                    "score": e["score"],
                    "explained_by": [
                        f"{gid} {go.names.get(gid, '')} ({how[0]} {anat.name(how[1])}{', broad' if how[2] else ''})"
                        for gid, how in e["explained_by"]
                    ][:3],
                    "rejected_only": [f"{gid} {go.names.get(gid, '')}" for gid, _ in r["explained_by"]][:3]
                    if not e["explained_by"] else [],
                }
                for e, r in zip(ex, ex_rej)
            ],
        }
        lines += [f"## {g} ({n_spec}/{len(ex)} explained specifically, {n_ex}/{len(ex)} at all)", "", "| Bgee tissue | score | explained by (retained) | only a rejected row would explain |",
                  "|---|---|---|---|"]
        for t in cases[g]["tissues"]:
            lines.append(f"| {t['tissue']} | {t['score']:.1f} | {'; '.join(t['explained_by']) or '**unexplained**'} | "
                         f"{'; '.join(t['rejected_only'])} |")
        lines.append("")

    bc.RESULTS.mkdir(parents=True, exist_ok=True)
    (bc.RESULTS / "tissue_explanation.yaml").write_text(
        yaml.safe_dump({"summary": summary, "cases": cases}, sort_keys=False, width=110, allow_unicode=True))
    (bc.RESULTS / "tissue_explanation_cases.md").write_text("\n".join(lines))
    bc.write_calls_tsv(case_calls, {ens_of[g]: g for g in CASES if g in ens_of}, bc.DATA / "case_study_calls_human.tsv")
    print(yaml.safe_dump(summary, sort_keys=False))


if __name__ == "__main__":
    main()
