#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Measure BioEMMA's recall against a model's *own* pathway assignment.

BiGG JSON models carry a ``subsystem`` per reaction (the SBML export does not).
For each (KEGG map, subsystem) pair given on the command line this script asks:
of the reactions the model itself files under that subsystem, how many did BioEMMA
retain on the model-specific map?  Every dropped reaction is classified:

* ``on_map_dropped``      the model reaction carries a KEGG xref that *is* a reaction
                          entry on the KGML map, yet BioEMMA dropped it  (a real miss);
* ``kegg_xref_not_on_map`` the model's KEGG xref is not drawn on this KGML map
                          (KEGG granularity / half-reactions / the reaction is drawn
                          on a different map);
* ``no_kegg_xref``        the model reaction has no ``kegg.reaction`` annotation, so
                          only a BiGG/SEED cross-reference could have matched it.

Inputs: the BiGG JSON model, the ``*_retained_reactions.tsv`` written by
``bioemma_eval.py`` and the directory of KGML files.  Output:
``<out>/<model>_subsystem_recall.tsv`` (one row per map/subsystem) and
``<out>/<model>_subsystem_dropped.tsv`` (one row per dropped reaction).

Example::

    uv run projects/BIOEMMA/subsystem_recall.py \
        --model-json /tmp/bioemma-work/models/iJN1463.json \
        --retained projects/BIOEMMA/results/iJN1463_retained_reactions.tsv \
        --kgml-dir /tmp/bioemma-work/kgml --out projects/BIOEMMA/results \
        --pair rn00010=S_Glycolysis --pair rn00020=S_TCA_Cycle
"""
from __future__ import annotations

import argparse
import csv
import json
import re
from pathlib import Path


def kgml_reaction_ids(kgml: Path) -> set[str]:
    text = kgml.read_text(encoding="utf-8", errors="replace")
    ids: set[str] = set()
    for m in re.finditer(r'<reaction [^>]*name="([^"]+)"', text):
        for token in m.group(1).split():
            if token.startswith("rn:"):
                ids.add(token[3:])
    return ids


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--model-json", required=True)
    ap.add_argument("--retained", required=True)
    ap.add_argument("--kgml-dir", required=True)
    ap.add_argument("--out", default="results")
    ap.add_argument("--pair", action="append", required=True, help="map=subsystem (repeatable; subsystem may be a '|'-joined list)")
    ap.add_argument("--skip-prefix", default="EX_,DM_,SK_,BIOMASS", help="comma list of reaction-id prefixes to ignore")
    args = ap.parse_args()

    model = json.load(open(args.model_json))
    model_id = model.get("id") or Path(args.model_json).stem
    skip = tuple(p for p in args.skip_prefix.split(",") if p)
    by_sub: dict[str, list[dict]] = {}
    for r in model["reactions"]:
        by_sub.setdefault(r.get("subsystem", ""), []).append(r)

    retained: dict[str, set[str]] = {}
    with open(args.retained) as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            retained.setdefault(row["map"], set()).add(row["model_reaction"])

    rows, dropped = [], []
    for pair in args.pair:
        map_id, subs = pair.split("=", 1)
        on_map = kgml_reaction_ids(Path(args.kgml_dir) / f"{map_id}.xml")
        kept = retained.get(map_id, set())
        members = [r for s in subs.split("|") for r in by_sub.get(s, []) if not r["id"].startswith(skip)]
        n_ret = 0
        for r in members:
            keggs = r.get("annotation", {}).get("kegg.reaction", [])
            if isinstance(keggs, str):
                keggs = [keggs]
            if r["id"] in kept:
                n_ret += 1
                continue
            if not keggs:
                reason = "no_kegg_xref"
            elif set(keggs) & on_map:
                reason = "on_map_dropped"
            else:
                reason = "kegg_xref_not_on_map"
            dropped.append({"map": map_id, "subsystem": subs, "model_reaction": r["id"], "name": r.get("name", ""),
                            "kegg_xrefs": ";".join(keggs), "reason": reason, "gpr": r.get("gene_reaction_rule", "")})
        n = len(members)
        rows.append({"map": map_id, "subsystem": subs, "subsystem_reactions": n, "retained_by_bioemma": n_ret,
                     "recall_pct": round(100.0 * n_ret / n, 1) if n else "",
                     "retained_on_map_total": len(kept),
                     "dropped_on_map": sum(1 for d in dropped if d["map"] == map_id and d["reason"] == "on_map_dropped"),
                     "dropped_xref_not_on_map": sum(1 for d in dropped if d["map"] == map_id and d["reason"] == "kegg_xref_not_on_map"),
                     "dropped_no_kegg_xref": sum(1 for d in dropped if d["map"] == map_id and d["reason"] == "no_kegg_xref")})

    out = Path(args.out); out.mkdir(parents=True, exist_ok=True)
    for name, data in ((f"{model_id}_subsystem_recall.tsv", rows), (f"{model_id}_subsystem_dropped.tsv", dropped)):
        with (out / name).open("w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=list(data[0].keys()), delimiter="\t"); w.writeheader(); w.writerows(data)
        print(f"[write] {out / name} ({len(data)} rows)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
