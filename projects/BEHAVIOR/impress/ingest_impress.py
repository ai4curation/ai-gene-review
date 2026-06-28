#!/usr/bin/env python3
"""Ingest IMPReSS standardized phenotyping assays from the IMPC API.

IMPReSS (International Mouse Phenotyping Resource of Standardised Screens) is the
closest thing to a standardized, versioned *list of phenotyping assays*. This
script pulls one or more pipelines' full procedure sets from the public API,
classifies the behavioural / neurological ones into canonical assay *types*
(so the per-centre variants of "Open Field", "Rotarod", … collapse together),
and writes:

- ``procedures.tsv``         — every procedure across the ingested pipelines
                               (pipeline, key, name, level, version, #parameters,
                               MP terms from the description, behavioural flag,
                               canonical assay type).
- ``behavioural_assays.yaml`` — behavioural/neurological assays grouped by
                               canonical type, each listing every (pipeline, key)
                               instance and the union of its MP terms.
- ``REPORT.md``              — counts + the canonical behavioural-assay table.

Nothing about the results is hard-coded: data is fetched live and the
classifiers are the regexes below. If the API is unreachable the script errors
rather than emitting stale data.

API base: https://api.mousephenotype.org/impress
Docs:     https://www.mousephenotype.org/phenodcc/impress-api-documentation/

Usage:
    uv run python projects/BEHAVIOR/impress/ingest_impress.py \
        --pipelines IMPC_001,JAX_001,ESLIM_002,GMC_001,ICS_001 \
        --out-dir projects/BEHAVIOR/impress
"""
from __future__ import annotations

import argparse
import csv
import os
import re
from collections import defaultdict

import requests
import yaml

API = "https://api.mousephenotype.org/impress"

# Default ingest set: the IMPC core pipeline plus the major centre/legacy
# pipelines that add assay types absent from IMPC_001 (Rotarod, Hole-board,
# Hot Plate, Tail Suspension, Von Frey).
DEFAULT_PIPELINES = ["IMPC_001", "JAX_001", "ESLIM_002", "GMC_001", "ICS_001"]

BEHAVIOURAL = re.compile(
    r"behav|locomot|anxiety|startle|pre-?pulse|\bPPI\b|SHIRPA|grip|rota-?rod|"
    r"\bmotor\b|hole.?board|light.?dark|open.?field|nocicept|hot.?plate|von.?frey|"
    r"acoustic|auditory|tremor|gait|exploratory|fear condition|learning|memory|"
    r"maze|tail.?suspension|sensorimotor|neurolog|calorimetr", re.I)

# Canonical assay TYPES (specific patterns first). Keyed name aligns with
# behavioural_assay_go_map.yaml.
CANONICAL = [
    ("Acoustic Startle and Pre-pulse Inhibition (PPI)", r"startle|pre-?pulse|\bppi\b"),
    ("Auditory Brain Stem Response", r"auditory brain|\babr\b"),
    ("Fear Conditioning", r"fear.?condition"),
    ("Y-maze", r"\by-?maze\b"),
    ("T-maze", r"\bt-?maze\b"),
    ("Open Field", r"open.?field"),
    ("Light-Dark Test", r"light.?dark"),
    ("Hole-board Exploration", r"hole.?board"),
    ("Rotarod", r"rota-?rod"),
    ("Grip Strength", r"grip"),
    ("Hot Plate (nociception)", r"hot.?plate|nociception hotplate"),
    ("Von Frey Test (nociception)", r"von.?frey"),
    ("Tail Suspension", r"tail.?suspension"),
    ("SHIRPA / Dysmorphology battery", r"shirpa"),
    ("Indirect Calorimetry", r"calorimetr"),
    ("Sleep-Wake", r"sleep"),
]
CANONICAL = [(n, re.compile(p, re.I)) for n, p in CANONICAL]
MP_RE = re.compile(r"MP:\d{7}")


def canonical_type(name: str) -> str | None:
    for cname, rx in CANONICAL:
        if rx.search(name):
            return cname
    return None


def fetch(pipeline: str) -> list[dict]:
    r = requests.get(f"{API}/procedure/belongingtopipeline/full/{pipeline}", timeout=60)
    r.raise_for_status()
    d = r.json()
    return list(d.values()) if isinstance(d, dict) else list(d)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--pipelines", default=",".join(DEFAULT_PIPELINES),
                    help="comma-separated IMPReSS pipeline keys")
    ap.add_argument("--out-dir", default="projects/BEHAVIOR/impress")
    args = ap.parse_args()
    os.makedirs(args.out_dir, exist_ok=True)
    pipelines = [p.strip() for p in args.pipelines.split(",") if p.strip()]

    rows = []
    for pl in pipelines:
        for p in fetch(pl):
            name = p.get("name", "")
            desc = p.get("description") or ""
            is_beh = bool(BEHAVIOURAL.search(name) or BEHAVIOURAL.search(desc))
            rows.append({
                "pipeline": pl,
                "procedure_key": p.get("procedureKey", ""),
                "name": name,
                "level": p.get("level", ""),
                "version": f"{p.get('majorVersion')}.{p.get('minorVersion')}",
                "n_parameters": len(p.get("parameterCollection") or []),
                "behavioural_neurological": is_beh,
                "canonical_assay": canonical_type(name) or ("Other behavioural" if is_beh else ""),
                "mp_terms": "|".join(sorted(set(MP_RE.findall(desc)))),
                "description": re.sub(r"\s+", " ", desc).strip(),
            })

    cols = ["pipeline", "procedure_key", "name", "level", "version", "n_parameters",
            "behavioural_neurological", "canonical_assay", "mp_terms", "description"]
    with open(os.path.join(args.out_dir, "procedures.tsv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, delimiter="\t")
        w.writeheader()
        w.writerows(sorted(rows, key=lambda r: (r["pipeline"], r["name"])))

    # Group behavioural assays by canonical type.
    groups: dict[str, dict] = defaultdict(lambda: {"instances": [], "mp_terms": set(), "example_desc": ""})
    for r in rows:
        if not r["behavioural_neurological"]:
            continue
        g = groups[r["canonical_assay"]]
        g["instances"].append({"pipeline": r["pipeline"], "key": r["procedure_key"], "name": r["name"]})
        g["mp_terms"].update(t for t in r["mp_terms"].split("|") if t)
        if len(r["description"]) > len(g["example_desc"]):
            g["example_desc"] = r["description"]

    assays = []
    for cname in sorted(groups):
        g = groups[cname]
        assays.append({
            "assay_type": cname,
            "n_instances": len(g["instances"]),
            "mp_terms": sorted(g["mp_terms"]),
            "instances": sorted(g["instances"], key=lambda x: x["key"]),
            "example_description": g["example_desc"][:600],
        })
    with open(os.path.join(args.out_dir, "behavioural_assays.yaml"), "w") as fh:
        yaml.safe_dump({"pipelines_ingested": pipelines,
                        "n_total_procedures": len(rows),
                        "n_behavioural_instances": sum(a["n_instances"] for a in assays),
                        "n_canonical_assay_types": len(assays),
                        "assays": assays},
                       fh, sort_keys=False, allow_unicode=True, width=100)

    lines = [f"# IMPReSS ingest — pipelines {', '.join(f'`{p}`' for p in pipelines)}\n",
             f"*Auto-generated by `ingest_impress.py` from {API}. Do not edit by hand.*\n",
             f"\n- Pipelines ingested: **{len(pipelines)}**",
             f"- Total procedures: **{len(rows)}**",
             f"- Canonical behavioural / neurological assay types: **{len(assays)}**\n",
             "\n## Canonical behavioural / neurological assays\n",
             "| Assay type | # instances (across pipelines) | MP terms |",
             "|---|---|---|"]
    for a in assays:
        lines.append(f"| {a['assay_type']} | {a['n_instances']} | {', '.join(a['mp_terms']) or '—'} |")
    report = "\n".join(lines) + "\n"
    with open(os.path.join(args.out_dir, "REPORT.md"), "w") as fh:
        fh.write(report)
    print(report)


if __name__ == "__main__":
    main()
