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

  4. **Slim-aware scoring.** Every GO id Affinage emits is a ``goslim_generic``
     term (43/43 across the 42-gene cohort), so an exact match against a leaf
     curated term is near-impossible by construction. We therefore also map each
     curated core MF / core location up to its ``goslim_generic`` bins (reflexive
     ``is_a`` + ``part_of`` closure over the pinned GO release used by the
     BioReason audit, ``cache/ontologies/go-basic-2026-03-25.obo``) and ask
     whether Affinage emitted the right *bin*.
  5. ``shared`` exact ids are reported twice: all GOA terms, and excluding terms
     every one of whose annotations the review REMOVEd or MARK_AS_OVER_ANNOTATED.

Nothing here is hard-coded: every number is derived from the fetched JSON, the
committed YAML and the pinned ontology. Missing data (no Affinage record, no
core_functions) is reported as such, never invented.

Usage:
    uv run python compare_affinage.py GPX4 TP53 ...      # specific genes
    uv run python compare_affinage.py --genes-file genes.txt  # one symbol per line
    uv run python compare_affinage.py --genes-file pilot-genes.txt --no-slim
Records are fetched once from the live API and cached **trimmed** (see
``trim_record``) under affinage-cache/; ``--refresh`` re-fetches.
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


def trim_record(data: dict) -> dict:
    """Keep only the fields this project uses (README: 'trimmed' cache).

    >>> trim_record({"gene": "X", "run_date": "d", "timeline": {"current_model": "m",
    ...   "discoveries": [1]}, "narrative": {"mechanism_profile": {"a": 1},
    ...   "mechanistic_narrative": "long"}, "prefetch_data": {"uniprot": {
    ...   "accession": "P1", "full_name": "n", "sequence": "MK"}, "hpa": {}},
    ...   "evaluation": {"pairwise": "win"}, "cost": {"total_usd": 0.1, "x": 2}})
    ... # doctest: +NORMALIZE_WHITESPACE
    {'gene': 'X', 'run_date': 'd', 'timeline': {'current_model': 'm'},
     'narrative': {'mechanism_profile': {'a': 1}},
     'prefetch_data': {'uniprot': {'accession': 'P1', 'full_name': 'n'}},
     'evaluation': {'pairwise': 'win'}, 'cost': {'total_usd': 0.1}}
    """
    uni = (data.get("prefetch_data") or {}).get("uniprot") or {}
    return {
        "gene": data.get("gene"),
        "run_date": data.get("run_date"),
        "timeline": {"current_model": (data.get("timeline") or {}).get("current_model", "")},
        "narrative": {"mechanism_profile":
                      (data.get("narrative") or {}).get("mechanism_profile") or {}},
        "prefetch_data": {"uniprot": {k: uni.get(k) for k in ("accession", "full_name")}},
        "evaluation": data.get("evaluation") or {},
        "cost": {"total_usd": (data.get("cost") or {}).get("total_usd")},
    }


def fetch_affinage(sym: str, refresh: bool = False) -> dict | None:
    """Return the (trimmed) Affinage JSON for a gene, caching under affinage-cache/."""
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
    if not isinstance(data, dict) or "narrative" not in data:
        print(f"  ! no Affinage record for {sym}", file=sys.stderr)
        return None
    data = trim_record(data)
    fp.write_text(json.dumps(data, indent=1) + "\n")
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


def rejected_ids(goa: dict) -> set[str]:
    """GOA term ids every one of whose reviewed annotations is in NEG_ACTIONS.

    A term with at least one ACCEPT/KEEP_AS_NON_CORE/MODIFY/... annotation (or an
    unreviewed one) is not rejected.

    >>> rejected_ids({"GO:1": {"actions": {"REMOVE"}},
    ...               "GO:2": {"actions": {"REMOVE", "ACCEPT"}},
    ...               "GO:3": {"actions": set()}})
    {'GO:1'}
    """
    return {t for t, rec in goa.items()
            if rec["actions"] and rec["actions"] <= NEG_ACTIONS}


# --------------------------------------------------------------------------
# GO slim mapping (pinned release, stdlib OBO parse)
# --------------------------------------------------------------------------
SLIM = "goslim_generic"
SLIM_RELS = ("is_a", "part_of")


def load_obo(path: Path) -> dict:
    """Parse a GO OBO file into {id: {label, namespace, parents:set, subsets:set}}."""
    terms: dict[str, dict] = {}
    cur = None
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("["):
            cur = None
            if line == "[Term]":
                cur = {"label": "", "namespace": "", "parents": set(), "subsets": set()}
            continue
        if cur is None or ": " not in line:
            continue
        key, val = line.split(": ", 1)
        if key == "id":
            terms[val] = cur
        elif key == "name":
            cur["label"] = val
        elif key == "namespace":
            cur["namespace"] = val
        elif key == "subset":
            cur["subsets"].add(val)
        elif key == "is_a":
            cur["parents"].add(val.split()[0])
        elif key == "relationship":
            rel, tgt = val.split()[:2]
            if rel in SLIM_RELS:
                cur["parents"].add(tgt)
    return terms


def slim_bins(tid: str, go: dict, cache: dict) -> set[str]:
    """Reflexive is_a/part_of ancestors of ``tid`` that are in the slim."""
    if tid in cache:
        return cache[tid]
    seen, stack = set(), [tid]
    while stack:
        t = stack.pop()
        if t in seen or t not in go:
            continue
        seen.add(t)
        stack.extend(go[t]["parents"])
    cache[tid] = {t for t in seen if SLIM in go[t]["subsets"]}
    return cache[tid]


def slim_scores(aff: dict, rev: dict, go: dict, cache: dict) -> dict:
    """Slim-level agreement between Affinage's MF/CC bins and the curated core."""
    aff_mf, aff_cc = set(aff["mf"]), set(aff["cc"])
    out: dict = {"aff_ids_not_in_slim": sorted(
        t for t in aff_mf | aff_cc if SLIM not in go.get(t, {}).get("subsets", set()))}
    for aspect, core, emitted in (("mf", rev["core_mf"], aff_mf),
                                  ("cc", rev["core_loc"], aff_cc)):
        per_core = {c: sorted(slim_bins(c, go, cache)) for c in core}
        bins = set().union(*map(set, per_core.values())) if per_core else set()
        hit_cores = [c for c, b in per_core.items() if set(b) & emitted]
        out[f"core_{aspect}_bins"] = per_core
        out[f"{aspect}_bins_hit"] = sorted(bins & emitted)
        # Any core term whose slim bin Affinage emitted (None when no core terms).
        out[f"{aspect}_slim_captured"] = (bool(hit_cores) if core else None)
        out[f"{aspect}_core_terms_binned"] = len(hit_cores)
        out[f"{aspect}_core_terms"] = len(core)
        # Affinage terms that are not a slim bin of *any* core term.
        out[f"aff_{aspect}_off_core_bins"] = sorted(emitted - bins)
    # Is Affinage's single most-supported MF a bin of some core MF?
    if aff["mf"] and rev["core_mf"]:
        top_n = max(v["n_support"] for v in aff["mf"].values())
        tops = sorted(t for t, v in aff["mf"].items() if v["n_support"] == top_n)
        allbins = set().union(*(set(b) for b in out["core_mf_bins"].values()))
        out["aff_top_mf"] = tops
        out["aff_top_mf_in_core_bin"] = any(t in allbins for t in tops)
    else:
        out["aff_top_mf"] = sorted(aff["mf"])
        out["aff_top_mf_in_core_bin"] = None
    return out


def compare(sym: str, aff: dict, rev: dict) -> dict:
    goa_ids = set(rev["goa"])
    rejected = rejected_ids(rev["goa"])
    aff_mf, aff_cc = set(aff["mf"]), set(aff["cc"])
    aff_all = aff_mf | aff_cc
    core_mf = set(rev["core_mf"])

    core_captured = None
    if core_mf:
        core_captured = bool(core_mf & aff_mf)

    aff_only = sorted(aff_all - goa_ids)
    shared = sorted(aff_all & goa_ids)
    shared_rej = sorted(set(shared) & rejected)
    return {
        "gene": sym,
        "aff_mf_n": len(aff_mf),
        "aff_cc_n": len(aff_cc),
        "goa_n": len(goa_ids),
        "shared_ids": shared,
        "shared_n": len(shared),
        # Shared ids whose every GOA annotation the review REMOVEd/over-annotated.
        "shared_rejected_ids": shared_rej,
        "shared_endorsed_n": len(shared) - len(shared_rej),
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
    ap.add_argument("--no-slim", action="store_true",
                    help="skip goslim_generic scoring (no GO release needed)")
    ap.add_argument("--go-obo", help="GO OBO to use for slim closure "
                    "(default: the pinned release via ai_gene_review.bioreason_ontology)")
    ap.add_argument("--offline", action="store_true",
                    help="never hit the API; use only affinage-cache/")
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

    go, slim_cache, go_src = None, {}, None
    if not args.no_slim:
        if args.go_obo:
            obo = Path(args.go_obo)
        else:
            sys.path.insert(0, str(REPO / "src"))
            from ai_gene_review.bioreason_ontology import ensure_frozen_go
            obo = ensure_frozen_go()
        go, go_src = load_obo(obo), obo.name

    RESULTS.mkdir(parents=True, exist_ok=True)
    rows = []
    for sym in genes:
        print(f"== {sym} ==")
        if args.offline and not (CACHE / f"{sym}.json").exists():
            print("  not cached and --offline; skipping")
            continue
        aff = fetch_affinage(sym, refresh=args.refresh)
        rev = load_review(sym)
        if aff is None:
            print("  no Affinage record; skipping")
            continue
        if rev is None:
            print("  no local review; skipping")
            continue
        ago = affinage_go(aff)
        row = compare(sym, ago, rev)
        if go is not None:
            row["slim"] = slim_scores(ago, rev, go, slim_cache)
            row["slim"]["go_release"] = go_src
        rows.append(row)

    (RESULTS / "per-gene.json").write_text(json.dumps(rows, indent=2))

    with (RESULTS / "summary.csv").open("w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["gene", "aff_mf_n", "aff_cc_n", "goa_n", "shared_n",
                    "shared_endorsed_n", "aff_only_n", "core_mf_captured",
                    "mf_slim_captured", "cc_slim_captured", "aff_top_mf_in_core_bin",
                    "reactome_n", "partners_n"])
        def b(v):
            return "" if v is None else v
        for r in rows:
            sl = r.get("slim") or {}
            w.writerow([r["gene"], r["aff_mf_n"], r["aff_cc_n"], r["goa_n"],
                        r["shared_n"], r["shared_endorsed_n"], r["aff_only_n"],
                        b(r["core_mf_captured"]), b(sl.get("mf_slim_captured")),
                        b(sl.get("cc_slim_captured")),
                        b(sl.get("aff_top_mf_in_core_bin")),
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
    if go is not None and rows:
        def cnt(key):
            vals = [r["slim"][key] for r in rows if r["slim"][key] is not None]
            return f"{sum(vals)}/{len(vals)}"
        lines += [
            f"**Slim-level ({SLIM}, is_a+part_of closure over `{go_src}`):** "
            f"core MF bin emitted {cnt('mf_slim_captured')}; "
            f"Affinage's top-supported MF is a bin of a core MF {cnt('aff_top_mf_in_core_bin')}; "
            f"core location bin emitted {cnt('cc_slim_captured')}.",
            "",
            f"**Shared exact ids:** {sum(r['shared_n'] for r in rows)} in total, "
            f"{sum(r['shared_endorsed_n'] for r in rows)} after excluding GOA terms the "
            f"review wholly REMOVEd / MARK_AS_OVER_ANNOTATED.",
            ""]
    tick = {True: "✅", False: "❌", None: "—"}
    lines += ["| gene | Aff MF | Aff CC | GOA terms | shared (exact) | shared, excl. rejected "
              "| Aff-only | core MF exact | core MF slim bin | top Aff MF in core bin | core CC slim bin |",
              "|------|-------:|-------:|----------:|---------------:|------:|---------:"
              "|:---:|:---:|:---:|:---:|"]
    for r in rows:
        sl = r.get("slim") or {}
        lines.append(f"| {r['gene']} | {r['aff_mf_n']} | {r['aff_cc_n']} | "
                     f"{r['goa_n']} | {r['shared_n']} | {r['shared_endorsed_n']} | "
                     f"{r['aff_only_n']} | {tick[r['core_mf_captured']]} | "
                     f"{tick[sl.get('mf_slim_captured')]} | "
                     f"{tick[sl.get('aff_top_mf_in_core_bin')]} | "
                     f"{tick[sl.get('cc_slim_captured')]} |")
    (RESULTS / "summary.md").write_text("\n".join(lines) + "\n")
    print(f"\nWrote {RESULTS} ({n} genes). Core MF captured: "
          f"{len(captured)}/{len(with_core)}")


if __name__ == "__main__":
    main()
