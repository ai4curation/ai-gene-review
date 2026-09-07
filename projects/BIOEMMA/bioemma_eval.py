#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["bioemma==0.4.3", "cobra>=0.29"]
# ///
"""Evaluate BioEMMA (KEGG KGML -> model-specific Escher map) against AI Gene Review modules.

What this does, end to end and without hard-coding any result:

1. Fetch KEGG *reference* KGML maps (``rn00220`` etc.) from the KEGG REST API and a
   genome-scale model (SBML) from BiGG, caching both under ``--workdir``.
2. Run ``bioemma.workflow.build_outputs`` for every map with FBA enabled.
3. Write ``results/<model>_map_summary.tsv``: per map, how many KEGG reactions exist,
   how many map to the model namespace, how many are retained after model filtering,
   by which identifier route they matched, and how many carry non-zero FBA flux.
4. Write ``results/<model>_retained_reactions.tsv``: every retained reaction with its
   KEGG id, model reaction id, FBA flux, GPR rule and model genes.
5. If ``--reviews-dir`` points at ``genes/<SPECIES>`` this repo's gene reviews are joined
   on the UniProt ``OrderedLocusNames`` (e.g. ``PP_5185``) so each model gene on a
   retained reaction is flagged reviewed / not reviewed
   (``results/<model>_gpr_review_coverage.tsv``).

Network access is required for the first run (KEGG REST + BiGG); later runs use the
cache. KEGG's REST API is free for academic use but rate-limited: be gentle.

Example (from the repo root)::

    uv run projects/BIOEMMA/bioemma_eval.py --model iJN1463 \
        --maps rn00010 rn00020 rn00220 --reviews-dir genes/PSEPK \
        --workdir /tmp/bioemma-work --out projects/BIOEMMA/results

Use ``--model-path`` for a local SBML file (e.g. BioEMMA's bundled ``e_coli_core.xml``)
and ``--kgml-dir`` for pre-downloaded KGML files.
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
import time
import urllib.request
from pathlib import Path

KEGG_KGML_URL = "https://rest.kegg.jp/get/{map_id}/kgml"
BIGG_MODEL_URL = "http://bigg.ucsd.edu/static/models/{model_id}.xml.gz"


def fetch(url: str, dest: Path, sleep: float = 0.5) -> Path:
    if dest.exists() and dest.stat().st_size > 0:
        return dest
    dest.parent.mkdir(parents=True, exist_ok=True)
    print(f"[fetch] {url} -> {dest}", file=sys.stderr)
    with urllib.request.urlopen(url, timeout=120) as resp, open(dest, "wb") as fh:
        fh.write(resp.read())
    time.sleep(sleep)
    return dest


def fetch_model(model_id: str, workdir: Path) -> Path:
    import gzip
    import shutil

    xml = workdir / "models" / f"{model_id}.xml"
    if xml.exists():
        return xml
    gz = fetch(BIGG_MODEL_URL.format(model_id=model_id), workdir / "models" / f"{model_id}.xml.gz")
    with gzip.open(gz, "rb") as src, open(xml, "wb") as dst:
        shutil.copyfileobj(src, dst)
    return xml


def load_review_locus_index(reviews_dir: Path) -> dict[str, str]:
    """Map ordered-locus names (PP_1234) -> gene review directory name."""
    index: dict[str, str] = {}
    pat = re.compile(r"OrderedLocusNames=([^;{]+)")
    for uniprot_txt in reviews_dir.glob("*/*-uniprot.txt"):
        gene_dir = uniprot_txt.parent.name
        for line in uniprot_txt.open(encoding="utf-8", errors="replace"):
            if not line.startswith("GN "):
                continue
            for m in pat.finditer(line):
                for locus in m.group(1).split(","):
                    locus = locus.strip()
                    if locus:
                        index.setdefault(locus, gene_dir)
    return index


def evaluate_map(model, kgml_path: Path, out_dir: Path, run_fba: bool) -> dict:
    from bioemma.workflow import build_outputs

    result = build_outputs(
        model=model,
        kgml=str(kgml_path),
        output_dir=str(out_dir),
        run_fba=run_fba,
        save_kegg_map=False,
    )
    slug = kgml_path.stem
    summary = json.load(open(out_dir / slug / "summary.json"))
    fluxes = {}
    flux_path = out_dir / slug / "fluxes.json"
    if flux_path.exists():
        fluxes = json.load(open(flux_path))
    escher = json.load(open(out_dir / slug / "escher_map.json"))
    return {"slug": slug, "summary": summary, "fluxes": fluxes, "escher": escher}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--model", help="BiGG model id to download (e.g. iJN1463, e_coli_core)")
    ap.add_argument("--model-path", help="local SBML model (overrides --model)")
    ap.add_argument("--maps", nargs="+", required=True, help="KEGG reference maps, e.g. rn00220")
    ap.add_argument("--kgml-dir", help="directory holding <map>.xml KGML files (skips download)")
    ap.add_argument("--reviews-dir", help="genes/<SPECIES> directory for GPR/review join")
    ap.add_argument("--workdir", default=".bioemma-work")
    ap.add_argument("--out", default="results")
    ap.add_argument("--no-fba", action="store_true")
    args = ap.parse_args()

    import cobra

    workdir = Path(args.workdir)
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)

    if args.model_path:
        model_path = Path(args.model_path)
    elif args.model:
        model_path = fetch_model(args.model, workdir)
    else:
        ap.error("--model or --model-path is required")
    model = cobra.io.read_sbml_model(str(model_path))
    model_tag = model.id or model_path.stem

    locus_index = load_review_locus_index(Path(args.reviews_dir)) if args.reviews_dir else {}

    summary_rows, reaction_rows, gpr_rows = [], [], []
    for map_id in args.maps:
        if args.kgml_dir:
            kgml = Path(args.kgml_dir) / f"{map_id}.xml"
        else:
            kgml = fetch(KEGG_KGML_URL.format(map_id=map_id), workdir / "kgml" / f"{map_id}.xml")
        res = evaluate_map(model, kgml, workdir / "out" / model_tag, run_fba=not args.no_fba)
        s = res["summary"]
        mm = s["map_stats"]["model_matching"]
        cov = s["identifier_coverage"]["reactions"]
        rxns = res["escher"][1]["reactions"]
        nonzero = 0
        for r in rxns.values():
            bigg_id = r["bigg_id"]
            flux = res["fluxes"].get(bigg_id)
            if flux is not None and abs(flux) > 1e-9:
                nonzero += 1
            model_rxn = model.reactions.get_by_id(bigg_id) if bigg_id in model.reactions else None
            genes = sorted(g.id for g in model_rxn.genes) if model_rxn else []
            reaction_rows.append(
                {
                    "map": map_id,
                    "kegg_reaction": r.get("name"),
                    "model_reaction": bigg_id,
                    "fba_flux": "" if flux is None else f"{flux:.6g}",
                    "gpr": model_rxn.gene_reaction_rule if model_rxn else "",
                    "genes": ";".join(genes),
                }
            )
            if locus_index or args.reviews_dir:
                for g in genes:
                    gpr_rows.append(
                        {
                            "map": map_id,
                            "kegg_reaction": r.get("name"),
                            "model_reaction": bigg_id,
                            "model_gene": g,
                            "review_dir": locus_index.get(g, ""),
                            "reviewed": "yes" if g in locus_index else "no",
                        }
                    )
        methods = mm.get("reaction_match_methods", {})
        summary_rows.append(
            {
                "map": map_id,
                "kegg_reactions": s["kegg"]["reactions"],
                "kegg_metabolites": s["kegg"]["metabolites"],
                "mapped_to_bigg": cov["BIGG"]["mapped"],
                "mapped_to_seed": cov["SEED"]["mapped"],
                "retained_reactions": mm["matched_reactions"],
                "retained_pct_of_kegg": round(100.0 * mm["matched_reactions"] / max(1, s["kegg"]["reactions"]), 1),
                "matched_by_bigg_id": methods.get("bigg", 0),
                "matched_by_kegg_id": methods.get("kegg", 0),
                "matched_by_seed_id": methods.get("seed", 0),
                "retained_with_nonzero_flux": nonzero,
                "retained_metabolites": mm["matched_metabolites"],
                "escher_nodes": s["escher"]["nodes"],
            }
        )
        print(f"[{map_id}] kegg={s['kegg']['reactions']} retained={mm['matched_reactions']} flux!=0: {nonzero}", file=sys.stderr)

    def write(name: str, rows: list[dict]):
        if not rows:
            return
        path = out / name
        with path.open("w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()), delimiter="\t")
            w.writeheader()
            w.writerows(rows)
        print(f"[write] {path} ({len(rows)} rows)", file=sys.stderr)

    write(f"{model_tag}_map_summary.tsv", summary_rows)
    write(f"{model_tag}_retained_reactions.tsv", reaction_rows)
    write(f"{model_tag}_gpr_review_coverage.tsv", gpr_rows)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
