#!/usr/bin/env python3
"""Follow-up audit statistics for the BioReason comparison page (2026-09-27).

Computes, from committed files only:
  * RL narrative score means by local-reference status (COMPLETE/DRAFT/...).
  * RL narrative score means by organism, including every n=1 species.
  * Leakage / novelty diagnostics for ARGO95 SFT CNN and COR calls: GOA DATE of
    the matching annotation(s) relative to an assumed model training cutoff,
    with sensitivity at two cutoffs.
  * Counts of the "Current-snapshot audit reclassified X to Y" rationales.
  * Counts of the scripted boilerplate CNN rationale.

Usage (from repo root):
    uv run python projects/BIOREASON_COMPARISON/audit_followup.py \
        [--test-parquet /path/to/bioreason-pro-test-data/test-00000-of-00001.parquet]

The optional parquet is the public BioReason-Pro temporal test split
(https://huggingface.co/datasets/wanglab/bioreason-pro-test-data, ~15 MB, not
committed). When given, the script also reports how many ARGO139 genes and how
many AIGR gene reviews are in that held-out split.

Writes audit-followup.json next to this script and prints Markdown tables.

Caveats encoded here, not hidden:
  * The GOA ``DATE`` column is the date the annotation line was created or last
    modified by the assigning group; electronic and phylogenetic (IEA/IBA/ISS...)
    lines are regenerated routinely, so a recent DATE does not prove the knowledge
    is recent. We therefore also report dates restricted to experimental codes.
  * The BioReason-Pro training cutoff is not stated in any file in this repo; the
    page only records a "post-2022" temporal test split. CUTOFFS are labelled
    assumptions.
"""

import argparse
import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from statistics import mean

import yaml

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent

CUTOFFS = {"assumed_2022-01-01": "20220101", "sensitivity_2023-01-01": "20230101"}
EXPERIMENTAL = {"EXP", "IDA", "IPI", "IMP", "IGI", "IEP", "HTP", "HDA", "HMP", "HGI", "HEP"}
BOILERPLATE = "Term is in GOA — already a known curated annotation."
# Templated rationales emitted by the original automated SFT review pass (the
# pre-audit version of scripts/auto_review_sft_predictions.py).
TEMPLATES = {
    "CNN_in_goa": BOILERPLATE,
    "UNC_generic": "Generic or ancestor term not confirmed or refuted by GOA or AI gene review.",
}
RECLASS_RE = re.compile(r"Current-snapshot audit reclassified (\w+) to (\w+) because ([^.]*)")


def goa_index(gene_dir: Path):
    """GO ID -> list of (date, evidence) from the gene's committed GOA TSV."""
    hits = sorted(gene_dir.glob("*-goa.tsv"))
    idx = defaultdict(list)
    if not hits:
        return None
    for row in csv.DictReader(open(hits[0]), delimiter="\t"):
        if "NOT" in (row.get("QUALIFIER") or ""):
            continue
        idx[row["GO TERM"]].append((row["DATE"], row["GO EVIDENCE CODE"]))
    return idx


def means(rows):
    return {
        "n": len(rows),
        "correctness": round(mean(int(r["correctness"]) for r in rows), 3),
        "completeness": round(mean(int(r["completeness"]) for r in rows), 3),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--test-parquet", type=Path)
    args = ap.parse_args()
    bg = list(csv.DictReader(open(HERE / "benchmark-genes.csv")))
    rl = [r for r in bg if r["benchmark"] == "argo139_rl_narrative" and r["performance_included"] == "true"]
    out = {}

    # reference status
    out["rl_by_reference_status"] = {
        st: means([r for r in rl if r["reference_status"] == st])
        for st in sorted({r["reference_status"] for r in rl})
    }
    out["rl_by_reference_status"]["non_COMPLETE"] = means([r for r in rl if r["reference_status"] != "COMPLETE"])
    out["rl_by_reference_status"]["all"] = means(rl)

    # organism
    orgs = sorted({r["organism"] for r in rl})
    out["rl_by_organism"] = {o: means([r for r in rl if r["organism"] == o]) for o in orgs}

    # ARGO95 leakage + rationale counts
    a95 = [r for r in bg if r["benchmark"] == "argo95_sft_terms"]
    assess = Counter()
    reclass = Counter()
    boiler = {"n": 0, "genes": set(), "exact_goa_match": 0}
    leak = {k: Counter() for k in CUTOFFS}
    cnn_dates = []
    cor_to_cnn_dates = []
    for r in a95:
        path = ROOT / r["source_file"]
        d = yaml.safe_load(open(path))
        idx = goa_index(path.parent)
        for p in d["predictions"]:
            rv = p["review"]
            a = rv["assessment"]
            assess[a] += 1
            s = " ".join(str(rv.get("summary", "")).split())
            m = RECLASS_RE.search(s)
            reason = None
            if m:
                reason = re.sub(r"\s*\(.*?\)|GO:\d+|PMID:\d+", "", m.group(3)).strip()
                reclass[f"{m.group(1)}->{m.group(2)}: {reason}"] += 1
            gid = p["predicted_term"]["id"]
            rows = (idx or {}).get(gid, [])
            if a == "CNN" and s == BOILERPLATE:
                boiler["n"] += 1
                boiler["genes"].add(f"{r['organism']}/{r['gene']}")
                boiler["exact_goa_match"] += bool(rows)
            if a not in ("CNN", "COR"):
                continue
            first_any = min((dt for dt, _ in rows), default=None)
            first_exp = min((dt for dt, ev in rows if ev in EXPERIMENTAL), default=None)
            if a == "CNN":
                cnn_dates.append((first_any, first_exp))
                if m and m.group(1) == "COR":
                    cor_to_cnn_dates.append((first_any, first_exp))
            for name, cut in CUTOFFS.items():
                c = leak[name]
                c[f"{a}_total"] += 1
                if not rows:
                    c[f"{a}_no_exact_goa_row"] += 1
                    continue
                c[f"{a}_exact_goa_row"] += 1
                c[f"{a}_all_matching_rows_after_cutoff"] += first_any > cut
                if first_exp is None:
                    c[f"{a}_no_experimental_row"] += 1
                else:
                    c[f"{a}_experimental_row"] += 1
                    c[f"{a}_earliest_experimental_after_cutoff"] += first_exp > cut

    out["argo95_assessments"] = dict(assess.most_common())
    out["argo95_current_snapshot_reclassifications"] = dict(reclass.most_common())
    out["argo95_reclassified_to_CNN"] = sum(v for k, v in reclass.items() if "->CNN" in k)
    out["argo95_boilerplate_cnn"] = {
        "text": BOILERPLATE,
        "n": boiler["n"],
        "n_genes": len(boiler["genes"]),
        "n_with_exact_goa_row": boiler["exact_goa_match"],
    }
    out["leakage"] = {k: dict(v) for k, v in leak.items()}

    def after(pairs, cut, i):
        vals = [p[i] for p in pairs if p[i]]
        return {"n_with_date": len(vals), "n_after": sum(v > cut for v in vals)}

    out["cor_to_cnn_goa_dates"] = {
        name: {"any_evidence": after(cor_to_cnn_dates, cut, 0), "experimental": after(cor_to_cnn_dates, cut, 1)}
        for name, cut in CUTOFFS.items()
    }
    out["cor_to_cnn_n"] = len(cor_to_cnn_dates)

    # Second-rater agreement reweighted to first-rater correctness prevalence.
    # The committed sample is 4 genes per first-rater correctness stratum, so raw
    # agreement over-represents the rare low-score strata.
    first = {(r["organism"], r["gene"]): r for r in rl}
    sr = list(csv.DictReader(open(HERE / "second-review-ratings.csv")))
    strata = defaultdict(list)
    for r in sr:
        a = first[(r["species"], r["gene"])]
        strata[int(a["correctness"])].append(
            (int(a["correctness"]), int(r["correctness"]), int(a["completeness"]), int(r["completeness"]))
        )
    prev = Counter(int(r["correctness"]) for r in rl)
    w = {k: prev[k] / len(rl) for k in strata}
    rw = {}
    for ax, (i, j) in {"correctness": (0, 1), "completeness": (2, 3)}.items():
        per = {k: sum(x[i] == x[j] for x in v) / len(v) for k, v in strata.items()}
        per1 = {k: sum(abs(x[i] - x[j]) <= 1 for x in v) / len(v) for k, v in strata.items()}
        rw[ax] = {
            "sample_exact": round(sum(per[k] * len(strata[k]) for k in strata) / len(sr), 3),
            "prevalence_weighted_exact": round(sum(w[k] * per[k] for k in strata) / sum(w.values()), 3),
            "prevalence_weighted_within_one": round(sum(w[k] * per1[k] for k in strata) / sum(w.values()), 3),
            "per_stratum_exact": {str(k): round(per[k], 2) for k in sorted(per)},
        }
    rw["stratum_sizes"] = {str(k): len(v) for k, v in sorted(strata.items())}
    rw["first_rater_prevalence"] = {str(k): prev[k] for k in sorted(prev)}
    out["second_rater_reweighted"] = rw

    # Templated (scripted) rationales in ARGO95 and in the supplemental union
    scripted = {}
    for bench in ("argo95_sft_terms", "supplement_sft_terms_union_all"):
        files = [r for r in bg if r["benchmark"] == bench]
        c = Counter()
        genes_any = set()
        n_terms = 0
        status = Counter()
        for r in files:
            p = ROOT / r["source_file"]
            if not p.exists():
                c["missing_file"] += 1
                continue
            d = yaml.safe_load(open(p))
            status[d.get("status")] += 1
            for pr in d["predictions"]:
                n_terms += 1
                s_ = " ".join(str(pr["review"].get("summary", "")).split())
                for name, text in TEMPLATES.items():
                    if s_ == text:
                        c[name] += 1
                        genes_any.add(f"{r['organism']}/{r['gene']}")
        scripted[bench] = {
            "n_files": len(files),
            "file_status": dict(status),
            "n_terms": n_terms,
            "templated_counts": dict(c),
            "n_templated": sum(v for k, v in c.items() if k in TEMPLATES),
            "n_genes_with_any_template": len(genes_any),
        }
    out["scripted_rationales"] = scripted

    # ARGO139 characterization at the assumed cutoff
    genes = list(csv.DictReader(open(HERE / "genes.csv")))
    char = Counter()
    for g in genes:
        gd = [p for p in (ROOT / "genes" / g["species"]).glob("*") if p.name.lower() == g["symbol"].lower()]
        idx = goa_index(gd[0]) if gd else None
        if idx is None:
            char["no_goa_file"] += 1
            continue
        exp_dates = [dt for rows in idx.values() for dt, ev in rows if ev in EXPERIMENTAL]
        for name, cut in CUTOFFS.items():
            char[f"{name}: >=1 experimental annotation dated on/before cutoff"] += any(dt <= cut for dt in exp_dates)
        char["any experimental annotation"] += bool(exp_dates)
        char["genes"] += 1
    out["argo139_characterization"] = dict(char)

    if args.test_parquet:
        import duckdb

        test_ids = {r[0] for r in duckdb.sql(f"SELECT protein_id FROM '{args.test_parquet}'").fetchall()}
        a139 = {g["uniprot_id"]: f"{g['species']}/{g['symbol']}" for g in genes}
        reviews = set()
        for p in ROOT.glob("genes/*/*/*-ai-review.yaml"):
            with open(p) as fh:
                for line in fh:
                    m = re.match(r"^id:\s*(\S+)", line)
                    if m:
                        reviews.add(m.group(1))
                        break
        out["bioreason_test_split_overlap"] = {
            "n_test_proteins": len(test_ids),
            "argo139_in_test": sorted(v for k, v in a139.items() if k in test_ids),
            "n_aigr_reviews": len(reviews),
            "n_aigr_reviews_in_test": len(reviews & test_ids),
        }

    (HERE / "audit-followup.json").write_text(json.dumps(out, indent=2) + "\n")

    print("| Reference status | n | Correctness | Completeness |\n|---|---|---|---|")
    for k, v in out["rl_by_reference_status"].items():
        print(f"| {k} | {v['n']} | {v['correctness']:.2f} | {v['completeness']:.2f} |")
    print("\n| Organism | n | Correctness | Completeness |\n|---|---|---|---|")
    for k, v in sorted(out["rl_by_organism"].items(), key=lambda x: (-x[1]["correctness"], x[0])):
        print(f"| {k} | {v['n']} | {v['correctness']:.1f} | {v['completeness']:.1f} |")
    for k in ("second_rater_reweighted", "argo95_assessments", "argo95_current_snapshot_reclassifications", "argo95_reclassified_to_CNN",
              "argo95_boilerplate_cnn", "scripted_rationales", "leakage", "bioreason_test_split_overlap", "cor_to_cnn_n", "cor_to_cnn_goa_dates", "argo139_characterization"):
        if k in out:
            print(f"\n{k}: {json.dumps(out[k], indent=1)}")


if __name__ == "__main__":
    main()
