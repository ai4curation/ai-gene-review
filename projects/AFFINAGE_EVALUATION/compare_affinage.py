#!/usr/bin/env python3
"""Compare Affinage mechanism-profile GO terms against the local AIGR review/GOA.

For each gene we:
  1. Fetch the Affinage record (cached JSON under affinage-cache/) and pull the
     GO terms it grounds in ``narrative.mechanism_profile`` (molecular_activity +
     localization; ``pathway`` is Reactome, recorded separately).
  2. Load the local AIGR review (``genes/human/<GENE>/<GENE>-ai-review.yaml``):
     every existing GOA annotation (term id, GO aspect, evidence, review action)
     plus the reviewer-authored ``core_functions`` (the *specific* MF term and
     locations a curator judged to be the gene's core).
  3. Compute exact-id agreement per aspect and, crucially, whether Affinage's
     profile contains the reviewed **core molecular function** term.

Nothing here is hard-coded: every number is derived from the fetched JSON and the
committed YAML. Missing data (no Affinage record, no core_functions) is reported
as such, never invented.

Usage:
    python compare_affinage.py GPX4 TP53 ...      # specific genes
    python compare_affinage.py --genes genes.txt  # one symbol per line
Writes: results/per-gene.json, results/summary.csv, results/summary.md
"""
from __future__ import annotations

import argparse
import csv
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
CACHE = HERE / "affinage-cache"
RESULTS = HERE / "results"
API = "https://affinage.wi.mit.edu/api/gene/{sym}"

# Minimal GO aspect map for the cellular-component / molecular-function roots we
# need to bucket terms. We classify by which mechanism_profile list a term came
# from (authoritative) rather than guessing aspect from the id, so this is only a
# fallback label.


def fetch_affinage(sym: str, refresh: bool = False) -> dict | None:
    """Return the Affinage JSON for a gene, caching under affinage-cache/."""
    CACHE.mkdir(parents=True, exist_ok=True)
    fp = CACHE / f"{sym}.json"
    if fp.exists() and not refresh:
        try:
            return json.loads(fp.read_text())
        except json.JSONDecodeError:
            pass
    try:
        raw = subprocess.run(
            ["curl", "-sS", "--max-time", "60", API.format(sym=sym)],
            capture_output=True, text=True, check=True,
        ).stdout
        data = json.loads(raw)
    except (subprocess.CalledProcessError, json.JSONDecodeError) as e:
        print(f"  ! fetch failed for {sym}: {e}", file=sys.stderr)
        return None
    fp.write_text(json.dumps(data, indent=1))
    return data


def affinage_go(data: dict) -> dict:
    """Extract GO term sets from an Affinage record's mechanism_profile."""
    mp = (data.get("narrative") or {}).get("mechanism_profile") or {}

    def terms(key):
        out = {}
        for e in mp.get(key) or []:
            tid = e.get("term_id", "")
            if tid.startswith("GO:"):
                out[tid] = {
                    "label": e.get("term_label", ""),
                    "n_support": len(e.get("supporting_discovery_ids") or []),
                }
        return out

    return {
        "mf": terms("molecular_activity"),
        "cc": terms("localization"),
        "reactome": [e.get("term_id") for e in (mp.get("pathway") or [])
                     if str(e.get("term_id", "")).startswith("R-")],
        "partners": list(mp.get("partners") or []),
        "current_model": (data.get("timeline") or {}).get("current_model", ""),
    }


# GO ids whose aspect we resolve from the review file itself (we read the aspect
# from where the term appears). We only need MF vs CC vs BP coarsely; the review
# gives us the label, and core_functions gives us the authored MF + locations.

def load_review(sym: str) -> dict | None:
    import yaml
    fp = REPO / "genes" / "human" / sym / f"{sym}-ai-review.yaml"
    if not fp.exists():
        return None
    d = yaml.safe_load(fp.read_text())
    goa = {}  # term_id -> {label, actions:set, evidences:set}
    for a in d.get("existing_annotations") or []:
        t = a.get("term") or {}
        tid = t.get("id")
        if not tid:
            continue
        rec = goa.setdefault(tid, {"label": t.get("label", ""),
                                   "actions": set(), "evidences": set()})
        rv = a.get("review") or {}
        if rv.get("action"):
            rec["actions"].add(rv["action"])
        if a.get("evidence_type"):
            rec["evidences"].add(a["evidence_type"])
    core_mf, core_loc = {}, {}
    for cf in d.get("core_functions") or []:
        mf = cf.get("molecular_function") or {}
        if mf.get("id"):
            core_mf[mf["id"]] = mf.get("label", "")
        for loc in cf.get("locations") or []:
            if loc.get("id"):
                core_loc[loc["id"]] = loc.get("label", "")
    return {"goa": goa, "core_mf": core_mf, "core_loc": core_loc,
            "description": d.get("description", "")}


# Actions that mean the curator did NOT endorse the term as-is (a proxy for
# "GOA had it but review down-weighted it").
NEG_ACTIONS = {"REMOVE", "MARK_AS_OVER_ANNOTATED"}


def compare(sym: str, aff: dict, rev: dict) -> dict:
    goa_ids = set(rev["goa"])
    aff_mf, aff_cc = set(aff["mf"]), set(aff["cc"])
    aff_all = aff_mf | aff_cc
    core_mf = set(rev["core_mf"])

    core_captured = None
    if core_mf:
        core_captured = bool(core_mf & aff_mf)

    aff_only = sorted(aff_all - goa_ids)
    shared = sorted(aff_all & goa_ids)
    return {
        "gene": sym,
        "aff_mf_n": len(aff_mf),
        "aff_cc_n": len(aff_cc),
        "goa_n": len(goa_ids),
        "shared_ids": shared,
        "shared_n": len(shared),
        "aff_only_ids": aff_only,       # in Affinage profile, not in GOA
        "aff_only_n": len(aff_only),
        "core_mf": rev["core_mf"],
        "core_mf_captured": core_captured,  # None if no core_functions authored
        "aff_mf": aff["mf"],
        "aff_cc": aff["cc"],
        "reactome_n": len(aff["reactome"]),
        "partners_n": len(aff["partners"]),
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("genes", nargs="*")
    ap.add_argument("--genes-file")
    ap.add_argument("--refresh", action="store_true")
    ap.add_argument("--out-dir", help="write results here instead of ./results")
    args = ap.parse_args()

    global RESULTS
    if args.out_dir:
        RESULTS = Path(args.out_dir)

    genes = list(args.genes)
    if args.genes_file:
        genes += [l.strip() for l in Path(args.genes_file).read_text().splitlines()
                  if l.strip() and not l.startswith("#")]
    if not genes:
        ap.error("no genes given")

    RESULTS.mkdir(exist_ok=True)
    rows = []
    for sym in genes:
        print(f"== {sym} ==")
        aff = fetch_affinage(sym, refresh=args.refresh)
        rev = load_review(sym)
        if aff is None:
            print("  no Affinage record; skipping")
            continue
        if rev is None:
            print("  no local review; skipping")
            continue
        rows.append(compare(sym, affinage_go(aff), rev))

    (RESULTS / "per-gene.json").write_text(json.dumps(rows, indent=2))

    with (RESULTS / "summary.csv").open("w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["gene", "aff_mf_n", "aff_cc_n", "goa_n", "shared_n",
                    "aff_only_n", "core_mf_captured", "reactome_n", "partners_n"])
        for r in rows:
            w.writerow([r["gene"], r["aff_mf_n"], r["aff_cc_n"], r["goa_n"],
                        r["shared_n"], r["aff_only_n"],
                        "" if r["core_mf_captured"] is None else r["core_mf_captured"],
                        r["reactome_n"], r["partners_n"]])

    # Markdown summary (numbers computed, not hard-coded)
    n = len(rows)
    with_core = [r for r in rows if r["core_mf_captured"] is not None]
    captured = [r for r in with_core if r["core_mf_captured"]]
    lines = [f"# Affinage vs AIGR — automated GO overlap (n={n})", ""]
    if with_core:
        lines.append(
            f"**Core MF captured exactly:** {len(captured)}/{len(with_core)} genes "
            f"with an authored `core_functions` MF term had that exact term in "
            f"Affinage's `molecular_activity` profile.")
        lines.append("")
    lines += ["| gene | Aff MF | Aff CC | GOA terms | shared (exact) | Aff-only | core MF captured |",
              "|------|-------:|-------:|----------:|---------------:|---------:|:----------------:|"]
    for r in rows:
        cc = {True: "✅", False: "❌", None: "—"}[r["core_mf_captured"]]
        lines.append(f"| {r['gene']} | {r['aff_mf_n']} | {r['aff_cc_n']} | "
                     f"{r['goa_n']} | {r['shared_n']} | {r['aff_only_n']} | {cc} |")
    (RESULTS / "summary.md").write_text("\n".join(lines) + "\n")
    print(f"\nWrote results/ ({n} genes). Core MF captured: "
          f"{len(captured)}/{len(with_core)}")


if __name__ == "__main__":
    main()
