#!/usr/bin/env python
"""Score ARBA biological-process annotations by module deployment.

An ARBA process call on a single sequence bundles two inferences:

1. sequence -> activity (the molecular function), and
2. activity -> process: that activity is *deployed* in the process in this organism.

GO does not encode (2): a molecular-function term carries no ``part_of`` link to
the pathways that use it. Curated modules do. This script makes (2) explicit:

    protein P is involved_in process T in organism O  if
      (a) P's own MF annotations fill a step of a module M whose process concept
          is T or a descendant of T, and
      (b) M is satisfiable in O, where a step holds if any O protein carries the
          step's activity (GOA MF annotation, any evidence, via QuickGO).

Each ARBA process row in a reviewed gene is classified:

* ``ENTAILED``           - (a) and (b) hold for some module.
* ``MODULE_INCOMPLETE``  - (a) holds but every such module has an unfilled step in O.
* ``NOT_ENTAILED``       - modules exist under T but P fills none of their steps
                           (``other_modules`` lists modules P does fill).
* ``NO_MODULE``          - no module's process falls under T; not scored.

Only modules applicable to O are considered: a module with ``context.taxa`` applies
when O's NCBI lineage (UniProt taxonomy REST, cached) includes one of those taxa;
a module without taxa applies everywhere.

The verdict is then cross-tabulated against the gene review's action on that row.
Oracle results are fetched live from QuickGO and cached under ``.cache/``; nothing
is hard-coded. A failed fetch counts as "absent" and is reported in RESULTS.md.

Usage::

    uv run python projects/PATHWAY_SATISFIABILITY/arba_deployment/deploy_check.py
"""

from __future__ import annotations

import collections
import csv
import datetime
import functools
import glob
import json
import os
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import requests
import yaml
from oaklib import get_adapter

from ai_gene_review.module_logic import (
    Atom,
    compile_module,
    is_satisfied,
    iter_atoms,
    step_id,
    unsatisfied_steps,
)

HERE = Path(__file__).parent
CACHE = Path(".cache/arba_deployment/quickgo.json")
LINEAGE_CACHE = Path(".cache/arba_deployment/lineage.json")
ARBA = "GO_REF:0000117"
QUICKGO = "https://www.ebi.ac.uk/QuickGO/services/annotation/search"
PREDS = ["rdfs:subClassOf", "BFO:0000050"]

go = get_adapter("sqlite:obo:go")


@functools.lru_cache(None)
def ancestors(term: str) -> frozenset[str]:
    """Reflexive is_a/part_of ancestors (unknown or obsolete ids map to themselves)."""
    try:
        return frozenset(go.ancestors(term, predicates=PREDS, reflexive=True))
    except Exception:
        return frozenset([term])


def load_modules() -> list[dict]:
    """Modules with at least one GO process concept and one activity-typed step."""
    out = []
    for path in sorted(glob.glob("modules/*.yaml")):
        doc = yaml.load(open(path), Loader=yaml.CSafeLoader)
        concepts = [c["term"]["id"] for c in doc["module"].get("concepts") or []
                    if str((c.get("term") or {}).get("id", "")).startswith("GO:")]
        circuit = compile_module(doc)
        atoms = list(iter_atoms(circuit))
        declared = (doc["module"].get("context") or {}).get("taxa") or []
        taxa = {str((t.get("term") or {}).get("id", "")).split(":")[-1] for t in declared}
        taxa.discard("")
        if concepts and any(a.function_ids for a in atoms):
            out.append({"id": Path(path).stem, "concepts": concepts, "taxa": taxa,
                        "ungrounded": bool(declared) and not taxa,
                        "circuit": circuit, "atoms": atoms})
    return out


def lineage(taxon: str) -> dict:
    """NCBI lineage ids of ``taxon`` (inclusive) from UniProt taxonomy REST."""
    try:
        r = requests.get(f"https://rest.uniprot.org/taxonomy/{taxon}",
                         headers={"Accept": "application/json"}, timeout=60)
        r.raise_for_status()
        ids = [str(x["taxonId"]) for x in r.json().get("lineage") or []]
        return {"ok": True, "ids": ids + [taxon]}
    except Exception as e:
        return {"ok": False, "error": str(e)[:200], "ids": [taxon]}


def applies(module: dict, lineage_ids: set[str]) -> bool:
    """A module applies to an organism inside any of its declared taxa, or everywhere if it declares none.

    A module whose taxa are declared only as free text (no NCBITaxon id) has a
    scope that cannot be checked, so it applies nowhere rather than everywhere.

    >>> applies({"taxa": set(), "ungrounded": False}, {"9606"})
    True
    >>> applies({"taxa": set(), "ungrounded": True}, {"9606"})
    False
    >>> applies({"taxa": {"33090"}, "ungrounded": False}, {"9606", "2759"})
    False
    """
    if module["ungrounded"]:
        return False
    return not module["taxa"] or bool(module["taxa"] & lineage_ids)


def fills(atom: Atom, mf_closure: set[str]) -> bool:
    """True if a protein whose MF ancestor closure is ``mf_closure`` performs ``atom``."""
    return any(f in mf_closure for f in atom.function_ids)


def quickgo_presence(taxon: str, mf: str) -> dict:
    """Proteins in ``taxon`` with a non-NOT annotation to ``mf`` or an is_a descendant."""
    params = {"goId": mf, "goUsage": "descendants", "goUsageRelationships": "is_a",
              "taxonId": taxon, "taxonUsage": "exact", "aspect": "molecular_function",
              "limit": 100}
    try:
        r = requests.get(QUICKGO, params=params, headers={"Accept": "application/json"}, timeout=60)
        r.raise_for_status()
        res = r.json()["results"]
    except Exception as e:  # recorded, never silently invented
        return {"ok": False, "error": str(e)[:200], "proteins": []}
    prots = sorted({x["geneProductId"].split(":", 1)[-1] for x in res
                    if not str(x.get("qualifier", "")).startswith("NOT")})
    return {"ok": True, "proteins": prots[:10]}


def gene_rows() -> list[dict]:
    """Every reviewed gene with a GOA file: its MF closure and ARBA BP rows."""
    genes = []
    for goa in sorted(glob.glob("genes/*/*/*-goa.tsv")):
        rows = list(csv.DictReader(open(goa), delimiter="\t"))
        if not rows:
            continue
        mfs = {r["GO TERM"] for r in rows if r["GO ASPECT"] == "molecular_function"
               and not r["QUALIFIER"].startswith("NOT")}
        arba = [r for r in rows if r["REFERENCE"] == ARBA and r["GO ASPECT"] == "biological_process"
                and not r["QUALIFIER"].startswith("NOT")]
        if not arba:
            continue
        closure: set[str] = set()
        for m in mfs:
            closure |= ancestors(m)
        review = Path(goa.replace("-goa.tsv", "-ai-review.yaml"))
        actions = {}
        if review.exists():
            doc = yaml.load(open(review), Loader=yaml.CSafeLoader) or {}
            for a in doc.get("existing_annotations") or []:
                if a.get("original_reference_id") == ARBA:
                    actions[a["term"]["id"]] = (a.get("review") or {}).get("action") or ""
        genes.append({"gene": "/".join(goa.split("/")[1:3]), "protein": rows[0]["GENE PRODUCT ID"],
                      "taxon": rows[0]["TAXON ID"].split(":")[-1], "closure": closure,
                      "arba": arba, "actions": actions})
    return genes


def main() -> None:
    all_modules = load_modules()
    genes = gene_rows()

    lineages = json.loads(LINEAGE_CACHE.read_text()) if LINEAGE_CACHE.exists() else {}
    taxa = sorted({g["taxon"] for g in genes if not lineages.get(g["taxon"], {}).get("ok")})
    with ThreadPoolExecutor(8) as pool:
        for t, res in zip(taxa, pool.map(lineage, taxa)):
            lineages[t] = res
    LINEAGE_CACHE.parent.mkdir(parents=True, exist_ok=True)
    LINEAGE_CACHE.write_text(json.dumps(lineages, indent=0, sort_keys=True))
    for g in genes:
        g["modules"] = [m for m in all_modules if applies(m, set(lineages[g["taxon"]]["ids"]))]

    # Which modules does each protein fill a step of, and which (taxon, MF) lookups follow?
    needed: set[tuple[str, str]] = set()
    for g in genes:
        g["filled"] = {m["id"]: [a for a in m["atoms"] if fills(a, g["closure"])] for m in g["modules"]}
        g["filled"] = {k: v for k, v in g["filled"].items() if v}
        for m in g["modules"]:
            if m["id"] in g["filled"]:
                needed |= {(g["taxon"], f) for a in m["atoms"] for f in a.function_ids}

    cache = json.loads(CACHE.read_text()) if CACHE.exists() else {}
    todo = [k for k in needed if f"{k[0]}|{k[1]}" not in cache or not cache[f"{k[0]}|{k[1]}"]["ok"]]
    with ThreadPoolExecutor(8) as pool:
        for key, res in zip(todo, pool.map(lambda k: quickgo_presence(*k), todo)):
            cache[f"{key[0]}|{key[1]}"] = res
    CACHE.parent.mkdir(parents=True, exist_ok=True)
    CACHE.write_text(json.dumps(cache, indent=0, sort_keys=True))

    by_id = {m["id"]: m for m in all_modules}
    out = []
    for g in genes:
        def holds(atom: Atom, g=g) -> bool:
            if not atom.function_ids:  # untyped step: cannot test, assume present
                return True
            if fills(atom, g["closure"]):
                return True
            return any(cache.get(f"{g['taxon']}|{f}", {}).get("proteins") for f in atom.function_ids)

        for r in g["arba"]:
            t = r["GO TERM"]
            under = [m for m in g["modules"] if any(t in ancestors(c) for c in m["concepts"])]
            mine = [m for m in under if m["id"] in g["filled"]]
            detail, gaps = [], []
            if mine:
                sat = [m for m in mine if is_satisfied(m["circuit"], holds)]
                if sat:
                    verdict = "ENTAILED"
                    detail = [m["id"] for m in sat]
                else:
                    verdict = "MODULE_INCOMPLETE"
                    detail = [m["id"] for m in mine]
                    for m in mine:
                        gaps += [f"{m['id']}:{step_id(s)}" for s in unsatisfied_steps(m["circuit"], holds)]
            elif under:
                verdict = "NOT_ENTAILED"
                detail = [m["id"] for m in under][:5]
            else:
                verdict = "NO_MODULE"
            exact = any(t in by_id[d]["concepts"] for d in detail if d in by_id)
            out.append({
                "gene": g["gene"], "protein": g["protein"], "taxon": g["taxon"],
                "term": t, "label": r["GO NAME"], "rule": r["WITH/FROM"],
                "verdict": verdict, "exact_concept": exact,
                "modules": "|".join(detail), "gaps": "|".join(gaps),
                "steps_filled": "|".join(sorted({f"{mid}:{a.node_id}" for mid in (d for d in detail if d in g["filled"])
                                                  for a in g["filled"][mid]})),
                "other_modules": "|".join(sorted(set(g["filled"]) - {m["id"] for m in under}))[:300],
                "review_action": g["actions"].get(t, ""),
            })

    if not out:
        raise SystemExit("no ARBA biological-process rows found")
    with open(HERE / "results.tsv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(out[0]), delimiter="\t")
        w.writeheader()
        w.writerows(out)
    write_summary(out, cache, lineages, all_modules)


def write_summary(out: list[dict], cache: dict, lineages: dict, modules: list[dict]) -> None:
    scored = [r for r in out if r["verdict"] != "NO_MODULE"]
    verdicts = ["ENTAILED", "MODULE_INCOMPLETE", "NOT_ENTAILED"]
    actions = ["ACCEPT", "KEEP_AS_NON_CORE", "MODIFY", "MARK_AS_OVER_ANNOTATED", "TOO_GENERAL", "REMOVE",
               "UNDECIDED", "PENDING", ""]
    xt = collections.Counter((r["verdict"], r["review_action"]) for r in scored)
    failed = sum(1 for v in cache.values() if not v["ok"])
    ungrounded = sorted(m["id"] for m in modules if m["ungrounded"])
    lines = [
        "# ARBA process rows scored by module deployment",
        "",
        "Generated by `deploy_check.py`; do not edit by hand. Per-row detail is in",
        "[results.tsv](results.tsv).",
        "",
        f"- ARBA biological-process rows in reviewed genes: **{len(out)}**",
        f"- rows with a module whose process falls under the row term (scored): **{len(scored)}**",
        f"- QuickGO lookups: {len(cache)} cached, {failed} failed (failed lookups count as absent)",
        f"- taxonomy lookups: {len(lineages)}, {sum(1 for v in lineages.values() if not v['ok'])} failed "
        "(a failed lineage keeps only taxon-free modules)",
        f"- modules with activity-typed steps: {len(modules)}; {len(ungrounded)} declare taxa only as "
        "free text (no NCBITaxon id) and are excluded, since their scope cannot be checked",
        f"- snapshot: {datetime.date.today().isoformat()}",
        "",
        "## Verdict vs. gene-review action",
        "",
        "| verdict | " + " | ".join(a or "(not reviewed)" for a in actions) + " | total |",
        "|---|" + "---:|" * (len(actions) + 1),
    ]
    for v in verdicts:
        row = [xt[(v, a)] for a in actions]
        lines.append(f"| {v} | " + " | ".join(map(str, row)) + f" | {sum(row)} |")
    lines += ["", "## Kept and rejected, by verdict and module concept", "",
              "Kept is ACCEPT or KEEP_AS_NON_CORE; rejected is REMOVE, MARK_AS_OVER_ANNOTATED or "
              "TOO_GENERAL. Shares are of reviewed rows.", "",
              "| verdict | module concept | rows | kept | rejected |", "|---|---|---:|---:|---:|"]
    kept, rejected = {"ACCEPT", "KEEP_AS_NON_CORE"}, {"REMOVE", "MARK_AS_OVER_ANNOTATED", "TOO_GENERAL"}
    for v in verdicts:
        for exact, name in [(True, "exact"), (False, "ancestor of concept")]:
            sel = [r for r in scored if r["verdict"] == v and r["exact_concept"] == exact and r["review_action"]]
            if sel:
                k = sum(r["review_action"] in kept for r in sel) / len(sel)
                x = sum(r["review_action"] in rejected for r in sel) / len(sel)
                lines.append(f"| {v} | {name} | {len(sel)} | {k:.0%} | {x:.0%} |")
    if ungrounded:
        lines += ["", "Excluded modules (taxa declared without an id): " + ", ".join(ungrounded)]
    lines += ["", "## Rows where the verdict and the review disagree", ""]
    neg = {"REMOVE", "MARK_AS_OVER_ANNOTATED"}
    for title, pick in [
        ("Entailed by a satisfiable module, but the review rejected it",
         lambda r: r["verdict"] == "ENTAILED" and r["review_action"] in neg),
        ("Accepted by the review, but the protein fills no step of a module under the term",
         lambda r: r["verdict"] == "NOT_ENTAILED" and r["review_action"] == "ACCEPT"),
        ("Protein fills a step, but the module has an unfilled step in this organism",
         lambda r: r["verdict"] == "MODULE_INCOMPLETE"),
    ]:
        sel = [r for r in scored if pick(r)]
        lines += [f"### {title} ({len(sel)})", "",
                  "| gene | term | modules | gaps / other modules | review |", "|---|---|---|---|---|"]
        for r in sel[:40]:
            extra = r["gaps"] or r["other_modules"]
            lines.append(f"| {r['gene']} | {r['term']} {r['label']} | {r['modules'].replace('|', ', ')} "
                         f"| {extra.replace('|', ', ')[:160]} | {r['review_action']} |")
        if len(sel) > 40:
            lines.append(f"| … {len(sel) - 40} more in results.tsv | | | | |")
        lines.append("")
    (HERE / "RESULTS.md").write_text("\n".join(lines))
    print("\n".join(lines[:22]))


if __name__ == "__main__":
    os.environ.setdefault("PYTHONWARNINGS", "ignore")
    main()
