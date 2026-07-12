#!/usr/bin/env python3
"""Genome-content satisfiability check for IBA process/pathway over-annotations.

For each case in ``signatures.yaml`` this asks: does the TARGET taxon encode any
member of the obligate component's InterPro signature(s)? A control taxon (where
the component is known to be present) proves the query itself is sound.

Classification per case:

  COMPONENT_PRESENT   target has >=1 member  -> pathway satisfiable w.r.t. this
                                               component; the annotation is NOT
                                               flagged.
  ABSENT_CANDIDATE    target 0, control >0   -> CANDIDATE unsatisfiable. The IBA
                                               transfer of this pathway term is a
                                               candidate LINEAGE_OR_TAXON_MISMATCH.
                                               MUST be corroborated: divergent
                                               orthologs can escape a signature.
  INCONCLUSIVE        control 0, or an API   -> query unsound (bad signature) or
                      error                     network failure. No call made.

This is a TRIAGE SCREEN, not an oracle. Signature-absence != genome-absence for
distant lineages (see the STAT and P2X control cases). Results are fetched live
from the UniProt REST API and are never hard-coded; a failed fetch yields
INCONCLUSIVE, not a fabricated count.

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
UA = {"User-Agent": "aigr-taxon-absent-component/0.1 (ai-gene-review)"}


def count_members(interpro: str, taxon: int, timeout: int = 45) -> int | None:
    """Return the number of UniProtKB entries in `taxon` carrying `interpro`.

    Returns None on any network/parse failure (caller treats as INCONCLUSIVE).
    We request a bounded page and count returned accessions; the cap (below) is
    far above the handful of members these lineage-restricted families have, and
    the only decision that matters is zero vs non-zero.
    """
    query = f"(xref:interpro-{interpro}) AND (taxonomy_id:{taxon})"
    url = f"{UNIPROT}?query={urllib.parse.quote(query)}&format=list&size=500"
    try:
        req = urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            body = resp.read().decode()
    except Exception as exc:  # noqa: BLE001 - any failure -> inconclusive
        print(f"    ! fetch failed for {interpro} tax:{taxon}: {exc}", file=sys.stderr)
        return None
    return len([ln for ln in body.splitlines() if ln.strip()])


def classify(target_hits: int | None, control_hits: int | None) -> str:
    if target_hits is None or control_hits is None:
        return "INCONCLUSIVE"
    if control_hits == 0:
        return "INCONCLUSIVE"  # signature returns nothing even in the control
    if target_hits > 0:
        return "COMPONENT_PRESENT"
    return "ABSENT_CANDIDATE"


def evaluate(case: dict, target: int, control: int) -> dict:
    """Component is present if ANY of its signatures has a target member."""
    per_sig = []
    t_any = 0
    c_any = 0
    t_seen = c_seen = False
    for ipr in case["interpro"]:
        th = count_members(ipr, target)
        ch = count_members(ipr, control)
        per_sig.append({"interpro": ipr, "target": th, "control": ch})
        if th is not None:
            t_seen = True
            t_any = max(t_any, th)
        if ch is not None:
            c_seen = True
            c_any = max(c_any, ch)
    target_hits = t_any if t_seen else None
    control_hits = c_any if c_seen else None
    return {
        "id": case["id"],
        "go_term": case["go_term"],
        "go_label": case["go_label"],
        "component": case["obligate_component"],
        "per_sig": per_sig,
        "target_hits": target_hits,
        "control_hits": control_hits,
        "status": classify(target_hits, control_hits),
        "corroboration": case.get("corroboration", "").strip(),
    }


def render_markdown(cfg: dict, results: list[dict], target: int, control: int) -> str:
    lines = [
        "# Taxon-absent-component detector — results",
        "",
        f"- **Target taxon:** {target}  ·  **Control taxon:** {control}",
        "- Source: UniProtKB REST (`xref:interpro-*` counts), fetched live.",
        "- **A zero in the target is a CANDIDATE absence, not proof** — divergent",
        "  orthologs can escape a metazoan signature. Read `corroboration`.",
        "",
        "| Case | GO term | Obligate component | Control | Target | Status |",
        "|------|---------|--------------------|--------:|-------:|--------|",
    ]
    for r in results:
        th = "err" if r["target_hits"] is None else r["target_hits"]
        ch = "err" if r["control_hits"] is None else r["control_hits"]
        lines.append(
            f"| {r['id']} | {r['go_term']} | {r['component']} | {ch} | {th} | **{r['status']}** |"
        )
    lines += ["", "## Interpretation", ""]
    for r in results:
        lines.append(f"### {r['id']} — {r['status']}")
        lines.append("")
        lines.append(f"- **Term:** {r['go_term']} — {r['go_label']}")
        sig = ", ".join(
            f"{s['interpro']} (control {s['control']}, target {s['target']})"
            for s in r["per_sig"]
        )
        lines.append(f"- **Signatures:** {sig}")
        if r["corroboration"]:
            lines.append(f"- **Corroboration:** {r['corroboration']}")
        lines.append("")
    return "\n".join(lines) + "\n"


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("config", nargs="?", default=None, help="signatures.yaml path")
    ap.add_argument("--target", type=int, default=None)
    ap.add_argument("--control", type=int, default=None)
    ap.add_argument("--write", metavar="MD", default=None, help="write results to markdown")
    args = ap.parse_args()

    cfg_path = Path(args.config) if args.config else Path(__file__).with_name("signatures.yaml")
    cfg = yaml.safe_load(cfg_path.read_text())
    target = args.target or cfg["target_taxon"]
    control = args.control or cfg["control_taxon"]

    results = []
    for case in cfg["cases"]:
        print(f"[{case['id']}] {case['go_term']} obligate={case['obligate_component']}")
        r = evaluate(case, target, control)
        print(f"    control={r['control_hits']} target={r['target_hits']} -> {r['status']}")
        results.append(r)

    if args.write:
        out = Path(args.write)
        if not out.is_absolute():
            out = cfg_path.with_name(args.write)
        out.write_text(render_markdown(cfg, results, target, control))
        print(f"\nWrote {out}")

    # machine-readable to stdout tail
    print("\nJSON:")
    print(json.dumps([{k: r[k] for k in ("id", "status", "control_hits", "target_hits")} for r in results], indent=2))


if __name__ == "__main__":
    main()
