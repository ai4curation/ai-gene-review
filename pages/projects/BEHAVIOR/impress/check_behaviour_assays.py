#!/usr/bin/env python3
"""Check behaviour annotations against the assay that produced them.

Complements ASSAY_TO_FUNCTION's ``mine_readouts.py`` (which cross-tabulates the
generic ``BEHAVIORAL_ASSAY`` readout class against reviewer action). This script
goes one step further using ``behavioural_assay_go_map.yaml``: when an
annotation's evidence text names a recognisable behavioural assay, it verifies
that the *specific GO term assigned* is one that assay can license, and that the
annotation was not accepted as a core function.

For every ``existing_annotations[*]`` whose evidence text (summary + reason +
supporting_text) mentions a known assay, and whose GO term is in the behaviour
domain, it emits a flag:

- ``MISMATCH``  — the assay does not license this GO term (e.g. Morris Water Maze,
                 a spatial-memory test, used to assign `swimming behavior`).
- ``OVER_CORE`` — action is ACCEPT, but a behavioural assay licenses a non-core
                 BP term at most.
- ``FENCED``    — the assay should license no behaviour term at all (Grip
                 Strength = neuromuscular; Tail Suspension = no GO despair term),
                 yet a behaviour-domain term was annotated.

Hits are reported with a snippet so each can be checked by hand. The script is
honest about coverage: most curators cite a PMID rather than naming the assay, so
the number of annotations that *name* an assay is reported alongside the flags.

Usage:
    uv run python projects/BEHAVIOR/impress/check_behaviour_assays.py \
        --genes-dir genes --map projects/BEHAVIOR/impress/behavioural_assay_go_map.yaml \
        --out-dir projects/BEHAVIOR/impress
"""
from __future__ import annotations

import argparse
import csv
import glob
import os
import re

import yaml

try:
    from yaml import CSafeLoader as Loader
except ImportError:  # pragma: no cover
    from yaml import SafeLoader as Loader  # type: ignore

# Detection patterns for each assay_type (must join to behavioural_assay_go_map).
ASSAY_PATTERNS: dict[str, str] = {
    "Morris Water Maze": r"morris\s*water\s*maze|\bMWM\b",
    "Open Field": r"open[-\s]*field",
    "Light-Dark Test": r"light[-/\s]*dark\s*(box|test)",
    "Y-maze": r"\bY[-\s]*maze\b",
    "Fear Conditioning": r"fear\s*conditioning",
    "Acoustic Startle and Pre-pulse Inhibition (PPI)": r"acoustic\s*startle|pre-?pulse\s*inhibition|\bPPI\b|startle\s*(response|reflex)",
    "Rotarod": r"rota-?rod",
    "Hole-board Exploration": r"hole[-\s]*board",
    "Hot Plate (nociception)": r"hot[-\s]*plate",
    "Von Frey Test (nociception)": r"von\s*frey",
    "Sleep-Wake": r"\bsleep[-/\s]*wake\b|PiezoSleep",
    "Indirect Calorimetry": r"indirect\s*calorimetry|metabolic\s*cage",
    "Auditory Brain Stem Response": r"auditory\s*brain\s*stem|\bABR\b",
    "Grip Strength": r"grip\s*strength",
    "Tail Suspension": r"tail\s*suspension",
}
ASSAY_RE = {a: re.compile(p, re.I) for a, p in ASSAY_PATTERNS.items()}

# A GO term is "behaviour-domain" (and thus in scope for this check) if its label
# matches one of these — avoids needing the ontology closure.
BEHAVIOUR_DOMAIN = re.compile(
    r"behavior|behaviour|locomot|exploration|learning|memory|startle|prepulse|"
    r"sleep|circadian|sensory perception of (sound|pain)|nocicept|feeding|"
    r"grooming|mating|anxiety|motor behavior", re.I)
NOT_REVIEWED = {None, "", "PENDING", "UNREVIEWED"}


def evidence_text(review: dict) -> str:
    parts = []
    for k in ("summary", "reason"):
        v = review.get(k)
        if isinstance(v, str):
            parts.append(v)
    for sb in review.get("supported_by") or []:
        if isinstance(sb, dict):
            v = sb.get("supporting_text")
            if isinstance(v, str):
                parts.append(v)
    return "\n".join(parts)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--genes-dir", default="genes")
    ap.add_argument("--map", default="projects/BEHAVIOR/impress/behavioural_assay_go_map.yaml")
    ap.add_argument("--out-dir", default="projects/BEHAVIOR/impress")
    args = ap.parse_args()
    os.makedirs(args.out_dir, exist_ok=True)

    gomap = yaml.safe_load(open(args.map))
    licensed: dict[str, set[str]] = {
        a["assay_type"]: {g["id"] for g in (a.get("supports_go") or [])}
        for a in gomap["assays"]
    }

    n_assay_mentions = 0
    flags = []
    for path in glob.glob(os.path.join(args.genes_dir, "**", "*-ai-review.yaml"), recursive=True):
        try:
            doc = yaml.load(open(path), Loader=Loader)
        except Exception:
            continue
        if not isinstance(doc, dict):
            continue
        gene = doc.get("gene_symbol", "?")
        species = path.split(os.sep)[1] if len(path.split(os.sep)) > 1 else "?"
        for ann in doc.get("existing_annotations") or []:
            review = ann.get("review") or {}
            action = review.get("action")
            text = evidence_text(review)
            if not text:
                continue
            hits = [a for a, rx in ASSAY_RE.items() if rx.search(text)]
            if not hits:
                continue
            term = ann.get("term") or {}
            label = term.get("label") or ""
            if not BEHAVIOUR_DOMAIN.search(label):
                continue  # the annotated term is not a behaviour-domain term
            n_assay_mentions += 1
            tid = term.get("id")
            for assay in hits:
                lic = licensed.get(assay, set())
                m = ASSAY_RE[assay].search(text)
                snip = re.sub(r"\s+", " ", text[max(0, m.start() - 70):m.end() + 70]).strip()
                flag = None
                if not lic:
                    flag = "FENCED"
                elif tid not in lic:
                    flag = "MISMATCH"
                elif action == "ACCEPT":
                    flag = "OVER_CORE"
                if flag:
                    flags.append({
                        "flag": flag, "species": species, "gene": gene,
                        "term_id": tid, "term_label": label, "assay": assay,
                        "action": action or "", "evidence_snippet": snip[:200],
                    })

    flags.sort(key=lambda f: (f["flag"], f["species"], f["gene"]))
    fields = ["flag", "species", "gene", "term_id", "term_label", "assay", "action", "evidence_snippet"]
    with open(os.path.join(args.out_dir, "assay_check_flags.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        w.writerows(flags)

    from collections import Counter
    by_flag = Counter(f["flag"] for f in flags)
    out = ["# Behaviour annotation vs. assay check\n",
           "*Auto-generated by `check_behaviour_assays.py`. Flags behaviour annotations whose evidence "
           "names an assay that does not license the assigned GO term, accepts it as core, or is fenced.*\n",
           f"\n- Behaviour-domain annotations whose evidence **names a recognised assay**: **{n_assay_mentions}** "
           "(most curators cite a PMID rather than the assay, so this is a floor, not the full population).",
           f"- Flags raised: **{len(flags)}** — " + (", ".join(f"{k}: {v}" for k, v in by_flag.most_common()) or "none") + "\n"]
    if flags:
        out += ["| Flag | Gene | Term | Assay | Action | Evidence |", "|---|---|---|---|---|---|"]
        for f in flags:
            out.append(f"| {f['flag']} | {f['species']}/{f['gene']} | {f['term_label']} ({f['term_id']}) | "
                       f"{f['assay']} | {f['action']} | …{f['evidence_snippet']}… |")
    report = "\n".join(out) + "\n"
    with open(os.path.join(args.out_dir, "ASSAY_CHECK.md"), "w") as fh:
        fh.write(report)
    print(report)


if __name__ == "__main__":
    main()
