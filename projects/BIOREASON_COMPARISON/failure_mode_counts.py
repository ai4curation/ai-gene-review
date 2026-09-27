#!/usr/bin/env python3
"""Count controlled failure-mode tags (``review.error_type``) behind the
BioReason-Pro failure-mode taxonomy, with denominators.

Sources (all committed):
  * ARGO95 SFT term reviews: the ``source_file`` of every ``argo95_sft_terms`` row
    in benchmark-genes.csv (``*-sft-predictions.yaml``).
  * ARGO139 GO-GPT leaf reviews: ``*-gogpt-leaf-predictions.yaml`` for every gene
    in genes.csv (the upstream GO-GPT input; reported separately).
  * ARGO139 RL narrative reviews (``*-bioreason-rl-review.md``): these carry no
    controlled tag. We count only explicit, conservative text markers that a
    reader can check; they are flags, not adjudicated labels (see MARKERS).

Usage (from repo root):
    uv run python projects/BIOREASON_COMPARISON/failure_mode_counts.py

Writes failure-mode-counts.json and failure-mode-rl-flags.csv next to this
script and prints Markdown tables. Nothing is hard-coded except the marker
regexes, which are printed with the output.
"""

import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
DISCORDANT = {"NPI", "PLI", "REP"}

# Page mode -> controlled error_type values that embody it on a GO term.
MODE_TO_ERROR_TYPES = {
    "1 pseudo-enzyme": ["PSEUDOENZYME_OVERANNOTATION"],
    "2 localization default": ["LOCALIZATION_DEFAULT"],
    "3 paralog indistinguishability": ["PARALOG_OVERANNOTATION"],
    "5 neo-functionalization/moonlighting": ["MULTIPLE_FUNCTIONS"],
    "7 cross-kingdom fold bias": ["TAXON_CONSTRAINT_VIOLATION"],
    "9 wrong input data": ["WRONG_INPUT_SEQUENCE"],
}

# Conservative RL-review text markers. A flag means the review's own prose
# explicitly names the failure for the Functional Summary; absence of a match does
# not mean absence of the failure (recall is not measured). Matches whose context
# window mentions the reasoning "trace" are dropped, because trace-only errors are
# not scored. Only modes with an unambiguous wording convention are flagged; the
# other page modes are illustrative. Case-insensitive.
MARKERS = {
    "2 localization default": (
        r"wrong (?:sub)?cellular (?:location|localization|compartment)|wrong locali[sz]ation"
        r"|locali[sz]ation (?:is |was )?(?:wrong|incorrect)|locali[sz]ation error|mis-?locali[sz]"
        r"|incorrect locali[sz]ation|locali[sz]ation incorrect|is (?:emphatically )?not (?:cytosolic|cytoplasmic|nuclear)"
    ),
    "9 wrong input data": r"wrong (?:input|protein|sequence|gene)",
}
CONTEXT_EXCLUDE = re.compile(r"trace", re.I)


def marker_hit(rx, text):
    for m in re.finditer(rx, text, re.I):
        window = text[max(0, m.start() - 60): m.end() + 60]
        if not CONTEXT_EXCLUDE.search(window):
            return True
    return False


def load_yaml_preds(path):
    try:
        d = yaml.safe_load(open(path))
    except FileNotFoundError:
        return None
    return d.get("predictions") or []


def tally(paths):
    total = Counter()
    by_type = Counter()
    by_type_genes = defaultdict(set)
    untagged = Counter()
    n_files = 0
    for key, p in paths:
        preds = load_yaml_preds(ROOT / p)
        if preds is None:
            continue
        n_files += 1
        for pr in preds:
            rv = pr.get("review") or {}
            a = rv.get("assessment")
            total[a] += 1
            if a in DISCORDANT:
                et = rv.get("error_type")
                if et:
                    by_type[et] += 1
                    by_type_genes[et].add(key)
                else:
                    untagged[a] += 1
    n_terms = sum(total.values())
    n_disc = sum(total[a] for a in DISCORDANT)
    return {
        "n_files": n_files,
        "n_terms": n_terms,
        "assessment_counts": dict(total.most_common()),
        "n_discordant": n_disc,
        "n_discordant_tagged": sum(by_type.values()),
        "n_discordant_untagged": sum(untagged.values()),
        "untagged_by_assessment": dict(untagged),
        "error_type_term_counts": dict(by_type.most_common()),
        "error_type_gene_counts": {k: len(v) for k, v in sorted(by_type_genes.items(), key=lambda x: -len(x[1]))},
        "error_type_genes": {k: sorted("/".join(g) for g in v) for k, v in by_type_genes.items()},
    }


def main():
    bg = list(csv.DictReader(open(HERE / "benchmark-genes.csv")))
    argo95 = [((r["organism"], r["gene"]), r["source_file"]) for r in bg if r["benchmark"] == "argo95_sft_terms"]
    genes = list(csv.DictReader(open(HERE / "genes.csv")))
    rl_rows = {(r["organism"], r["gene"]): r for r in bg if r["benchmark"] == "argo139_rl_narrative"}

    gogpt = []
    for g in genes:
        hits = list((ROOT / "genes" / g["species"]).glob(f"*/{g['symbol']}-gogpt-leaf-predictions.yaml"))
        if hits:
            gogpt.append(((g["species"], g["symbol"]), str(hits[0].relative_to(ROOT))))

    sft = tally(argo95)
    gg = tally(gogpt)

    # RL narrative text flags
    flags = []
    mode_counts = Counter()
    n_reviews = 0
    for key, r in rl_rows.items():
        p = ROOT / r["source_file"]
        if not p.exists():
            continue
        n_reviews += 1
        text = p.read_text()
        row = {"species": key[0], "gene": key[1], "correctness": r["correctness"],
               "performance_included": r["performance_included"]}
        for mode, rx in MARKERS.items():
            hit = marker_hit(rx, text)
            row[mode] = hit
            mode_counts[(mode, r["performance_included"])] += hit
        flags.append(row)
    with open(HERE / "failure-mode-rl-flags.csv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(flags[0]))
        w.writeheader()
        w.writerows(sorted(flags, key=lambda x: (x["species"], x["gene"])))

    mode_table = []
    for mode, ets in MODE_TO_ERROR_TYPES.items():
        mode_table.append({
            "mode": mode,
            "error_types": ets,
            "argo95_sft_terms": sum(sft["error_type_term_counts"].get(e, 0) for e in ets),
            "argo95_sft_genes": len({g for e in ets for g in sft["error_type_genes"].get(e, [])}),
            "argo139_gogpt_terms": sum(gg["error_type_term_counts"].get(e, 0) for e in ets),
            "argo139_gogpt_genes": len({g for e in ets for g in gg["error_type_genes"].get(e, [])}),
        })
    out = {
        "argo95_sft": sft,
        "argo139_gogpt": gg,
        "mode_table": mode_table,
        "rl_text_flags": {
            "n_reviews": n_reviews,
            "n_performance_reviews": sum(r["performance_included"] == "true" for r in flags),
            "markers": MARKERS,
            "counts_performance_set": {m: mode_counts[(m, "true")] for m in MARKERS},
            "counts_excluded_inputs": {m: mode_counts[(m, "false")] for m in MARKERS},
            "flagged_genes": {m: sorted(f"{r['species']}/{r['gene']}" for r in flags if r[m]) for m in MARKERS},
        },
    }
    (HERE / "failure-mode-counts.json").write_text(json.dumps(out, indent=2) + "\n")

    for name, t in [("ARGO95 SFT", sft), ("ARGO139 GO-GPT", gg)]:
        print(f"\n{name}: {t['n_files']} files, {t['n_terms']} terms, discordant {t['n_discordant']}, "
              f"tagged {t['n_discordant_tagged']}, untagged {t['n_discordant_untagged']} {t['untagged_by_assessment']}")
        print("error_type terms:", t["error_type_term_counts"])
        print("error_type genes:", t["error_type_gene_counts"])
    print("\n| Mode | error_type | ARGO95 SFT terms (genes) | ARGO139 GO-GPT terms (genes) |")
    print("|---|---|---|---|")
    for m in mode_table:
        print(f"| {m['mode']} | {', '.join(m['error_types'])} | {m['argo95_sft_terms']} ({m['argo95_sft_genes']}) | {m['argo139_gogpt_terms']} ({m['argo139_gogpt_genes']}) |")
    print("\nRL narrative text flags:", json.dumps(out["rl_text_flags"], indent=1))


if __name__ == "__main__":
    main()
