#!/usr/bin/env python3
"""Genome-content satisfiability check for IBA process/pathway over-annotations.

For each case in ``signatures.yaml`` this asks: does the TARGET taxon encode any
member of the obligate component, using TWO oracles?

  PANTHER family membership (PRIMARY, divergence-robust) -- IBA propagates along
      the PANTHER tree, so even a divergent ortholog that lost its domain
      signature is still placed in the family.
  InterPro domain signature (CONTRAST) -- sensitive to divergence, so it
      under-calls in distant lineages.

A control taxon (component known present) proves each query is sound.

Per-case status (PANTHER decides; InterPro adds a divergence flag):

  COMPONENT_PRESENT   PANTHER target > 0  -> satisfiable w.r.t. this component;
                                             not flagged. If InterPro target == 0
                                             here, a DIVERGENCE FLAG is raised:
                                             the ortholog exists but a domain
                                             screen would have wrongly called it
                                             absent.
  ABSENT              PANTHER target 0, control > 0 -> candidate unsatisfiable.
                                             Confidence HIGH when InterPro agrees
                                             (also 0), since two independent
                                             oracles concur.
  INCONCLUSIVE        PANTHER control 0 (bad family id) or a fetch error.

Counts are fetched LIVE from UniProt REST and never hard-coded; a failed fetch
yields INCONCLUSIVE, not a fabricated number. Even with PANTHER this remains a
triage screen: a genome could carry an unclassified member, so a confident
REMOVE still wants independent corroboration (the `corroboration` field).

Usage:
    uv run python detect.py [signatures.yaml] [--target TAXID] [--control TAXID]
    uv run python detect.py --write RESULTS.md
"""
from __future__ import annotations

import argparse
import json
import sys
import urllib.parse
import urllib.request
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.exit("PyYAML required: run via `uv run python detect.py` in this repo.")

UNIPROT = "https://rest.uniprot.org/uniprotkb/search"
UA = {"User-Agent": "aigr-taxon-absent-component/0.2 (ai-gene-review)"}


def count_members(xref_db: str, acc: str, taxon: int, timeout: int = 45) -> int | None:
    """UniProtKB entries in `taxon` carrying cross-ref `xref_db-acc`.

    `xref_db` is 'panther' or 'interpro'. Returns None on any failure (caller
    treats as INCONCLUSIVE). Only zero vs non-zero matters; the page cap is far
    above these lineage-restricted families.
    """
    query = f"(xref:{xref_db}-{acc}) AND (taxonomy_id:{taxon})"
    url = f"{UNIPROT}?query={urllib.parse.quote(query)}&format=list&size=500"
    try:
        req = urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            body = resp.read().decode()
    except Exception as exc:  # noqa: BLE001 - any failure -> inconclusive
        print(f"    ! fetch failed {xref_db}:{acc} tax:{taxon}: {exc}", file=sys.stderr)
        return None
    return len([ln for ln in body.splitlines() if ln.strip()])


def presence(accs: list[str], xref_db: str, target: int, control: int) -> dict:
    """Aggregate one oracle over its accession list (present if ANY has a member)."""
    per = []
    t_any = c_any = 0
    t_seen = c_seen = False
    for acc in accs or []:
        th = count_members(xref_db, acc, target)
        ch = count_members(xref_db, acc, control)
        per.append({"acc": acc, "target": th, "control": ch})
        if th is not None:
            t_seen = True
            t_any = max(t_any, th)
        if ch is not None:
            c_seen = True
            c_any = max(c_any, ch)
    return {
        "per": per,
        "target": t_any if t_seen else None,
        "control": c_any if c_seen else None,
    }


def evaluate(case: dict, target: int, control: int) -> dict:
    pan = presence(case.get("panther"), "panther", target, control)
    ipr = presence(case.get("interpro"), "interpro", target, control)

    # PANTHER is authoritative for the present/absent call.
    pt, pc = pan["target"], pan["control"]
    it = ipr["target"]
    if pt is None or pc is None:
        status, confidence = "INCONCLUSIVE", "-"
    elif pc == 0:
        status, confidence = "INCONCLUSIVE", "-"  # family id returns nothing even in control
    elif pt > 0:
        status = "COMPONENT_PRESENT"
        confidence = "-"
    else:  # pt == 0, pc > 0
        status = "ABSENT"
        # two independent oracles agreeing raises confidence
        confidence = "HIGH" if it == 0 else "MEDIUM"

    # divergence flag: present by PANTHER but missed by the InterPro domain screen
    divergent = status == "COMPONENT_PRESENT" and it == 0

    return {
        "id": case["id"],
        "go_term": case["go_term"],
        "go_label": case["go_label"],
        "component": case["obligate_component"],
        "panther": pan,
        "interpro": ipr,
        "status": status,
        "confidence": confidence,
        "divergent_ortholog": divergent,
        "corroboration": case.get("corroboration", "").strip(),
        "expected": case.get("expected"),
    }


def _fmt(x) -> str:
    return "err" if x is None else str(x)


def render_markdown(results: list[dict], target: int, control: int) -> str:
    L = [
        "# Taxon-absent-component detector — results",
        "",
        f"- **Target taxon:** {target}  ·  **Control taxon:** {control}",
        "- Two oracles per component: **PANTHER family** (primary, divergence-robust)",
        "  and **InterPro domain** (contrast). Counts fetched live from UniProt REST.",
        "- `COMPONENT_PRESENT` where PANTHER finds a member; `ABSENT` where it does",
        "  not (confidence HIGH when InterPro agrees). A **divergence flag** marks",
        "  components present by PANTHER but missed by the InterPro domain screen.",
        "",
        "| Case | GO term | Component | PANTHER (ctrl/tgt) | InterPro (ctrl/tgt) | Status | Conf | Divergent? |",
        "|------|---------|-----------|:------------------:|:-------------------:|--------|:----:|:----------:|",
    ]
    for r in results:
        p, i = r["panther"], r["interpro"]
        L.append(
            f"| {r['id']} | {r['go_term']} | {r['component']} "
            f"| {_fmt(p['control'])}/{_fmt(p['target'])} "
            f"| {_fmt(i['control'])}/{_fmt(i['target'])} "
            f"| **{r['status']}** | {r['confidence']} "
            f"| {'YES' if r['divergent_ortholog'] else '-'} |"
        )
    L += ["", "## Interpretation", ""]
    for r in results:
        L.append(f"### {r['id']} — {r['status']}"
                 + (f" (confidence {r['confidence']})" if r["confidence"] != "-" else ""))
        L.append("")
        L.append(f"- **Term:** {r['go_term']} — {r['go_label']}")
        pan = ", ".join(f"{s['acc']} ctrl {_fmt(s['control'])}/tgt {_fmt(s['target'])}" for s in r["panther"]["per"]) or "—"
        ipr = ", ".join(f"{s['acc']} ctrl {_fmt(s['control'])}/tgt {_fmt(s['target'])}" for s in r["interpro"]["per"]) or "—"
        L.append(f"- **PANTHER:** {pan}")
        L.append(f"- **InterPro:** {ipr}")
        if r["divergent_ortholog"]:
            L.append("- **⚠ Divergence flag:** present by PANTHER but the InterPro "
                     "domain signature scores zero — a domain-only screen would have "
                     "falsely called this absent.")
        if r["corroboration"]:
            L.append(f"- **Corroboration:** {r['corroboration']}")
        L.append("")
    return "\n".join(L) + "\n"


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("config", nargs="?", default=None)
    ap.add_argument("--target", type=int, default=None)
    ap.add_argument("--control", type=int, default=None)
    ap.add_argument("--write", metavar="MD", default=None)
    args = ap.parse_args()

    cfg_path = Path(args.config) if args.config else Path(__file__).with_name("signatures.yaml")
    cfg = yaml.safe_load(cfg_path.read_text())
    target = args.target or cfg["target_taxon"]
    control = args.control or cfg["control_taxon"]

    results = []
    for case in cfg["cases"]:
        print(f"[{case['id']}] {case['go_term']} obligate={case['obligate_component']}")
        r = evaluate(case, target, control)
        flag = "  (DIVERGENCE FLAG)" if r["divergent_ortholog"] else ""
        print(f"    PANTHER ctrl={_fmt(r['panther']['control'])} tgt={_fmt(r['panther']['target'])} | "
              f"InterPro ctrl={_fmt(r['interpro']['control'])} tgt={_fmt(r['interpro']['target'])} "
              f"-> {r['status']} {r['confidence']}{flag}")
        results.append(r)

    if args.write:
        out = Path(args.write)
        if not out.is_absolute():
            out = cfg_path.with_name(args.write)
        out.write_text(render_markdown(results, target, control))
        print(f"\nWrote {out}")

    print("\nJSON:")
    print(json.dumps(
        [{k: r[k] for k in ("id", "status", "confidence", "divergent_ortholog")} for r in results],
        indent=2,
    ))


if __name__ == "__main__":
    main()
