#!/usr/bin/env python3
"""Resolve every WITH/FROM entity in ARHGAP4's GOA rows, and ask what each PAINT
node's evidence base actually is.

Three things a GAF row will not tell you, and that the review's `propagation_review`
entries depend on:

1. **Who the donors are.**  `MGI:MGI:2152938` and `WB:WBGene00006406` are opaque.
   Whether an IBA's support comes from the target's own ortholog or exclusively
   from a distant paralogous branch changes what the IBA asserts.
2. **Where the IBD sits.**  Each `PANTHER:PTN…` is an ancestral node with its own
   taxon scope and its own seed list.  PANTHER's PAINT export
   (`interpro/panther/PTHR14166/PTHR14166-paint.tsv`) carries both; this script
   joins the review's WITH/FROM tokens onto it so a node can be argued with
   rather than taken on faith.
3. **Which nodes the target does *not* inherit.**  A sibling node that carries
   terms ARHGAP4 does not receive is evidence that the curator drew a boundary
   deliberately -- the most useful possible context for judging the nodes it does
   inherit.

Every identifier is resolved against its own authority (UniProt REST, MGI, RGD,
WormBase via the Alliance) rather than guessed.  An identifier that will not
resolve is reported unresolved; it is never replaced by a plausible substitute.

Run:    uv run --with requests python resolve_entities.py
        uv run --with requests python resolve_entities.py --self-test
Writes: entities.json
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

import requests

UNIPROT = "https://rest.uniprot.org/uniprotkb/{acc}.json"
ALLIANCE = "https://www.alliancegenome.org/api/gene/{curie}"
INTERPRO = "https://www.ebi.ac.uk/interpro/api/entry/interpro/{acc}/"
FAMILY = "PTHR14166"
TARGET = "UniProtKB:P98171"


def repo_root() -> Path:
    here = Path(__file__).resolve()
    return next(p for p in here.parents if (p / "interpro" / "panther").is_dir())


def goa_with_from() -> dict[str, list[str]]:
    """Read the WITH/FROM column straight out of the committed GOA TSV, so the
    entity list cannot drift away from the annotations being reviewed."""
    tsv = repo_root() / "genes" / "human" / "ARHGAP4" / "ARHGAP4-goa.tsv"
    seen: dict[str, list[str]] = {}
    with tsv.open() as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            for tok in (row["WITH/FROM"] or "").split("|"):
                tok = tok.strip()
                if not tok:
                    continue
                seen.setdefault(tok, []).append(
                    f"{row['GO TERM']}/{row['GO EVIDENCE CODE']}"
                )
    return seen


def resolve(token: str) -> dict[str, object]:
    """Resolve one WITH/FROM token against the authority that owns its namespace."""
    out: dict[str, object] = {"token": token, "resolved": False}
    try:
        if token.startswith("UniProtKB:"):
            acc = token.split(":", 1)[1]
            d = requests.get(UNIPROT.format(acc=acc), timeout=90).json()
            genes = d.get("genes") or []
            out |= {
                "resolved": True,
                "kind": "protein",
                "symbol": (genes[0].get("geneName", {}).get("value") if genes else None),
                "name": d.get("proteinDescription", {})
                .get("recommendedName", {})
                .get("fullName", {})
                .get("value")
                or (d.get("proteinDescription", {}).get("submissionNames") or [{}])[0]
                .get("fullName", {})
                .get("value"),
                "taxon": d.get("organism", {}).get("scientificName"),
                "reviewed": d.get("entryType"),
                "is_target": token == TARGET,
            }
        elif token.split(":")[0] in ("MGI", "RGD", "WB", "ZFIN", "FB", "SGD"):
            curie = token[4:] if token.startswith("MGI:MGI:") else token
            r = requests.get(
                ALLIANCE.format(curie=curie),
                headers={"Accept": "application/json"},
                timeout=90,
            )
            if r.status_code == 404:
                return out | {"kind": "gene", "error": "404 from Alliance"}
            r.raise_for_status()
            g = r.json().get("gene") or {}
            sym = (g.get("geneSymbol") or {}).get("displayText")
            out |= {
                "resolved": bool(sym),
                "kind": "gene",
                "symbol": sym,
                "name": (g.get("geneFullName") or {}).get("displayText"),
                "taxon": (g.get("taxon") or {}).get("name"),
            }
        elif token.startswith("PANTHER:PTN"):
            out |= {"resolved": True, "kind": "PAINT ancestral node"}
        elif token.startswith("InterPro:"):
            d = requests.get(
                INTERPRO.format(acc=token.split(":", 1)[1]),
                headers={"Accept": "application/json"},
                timeout=90,
            ).json()
            md = d.get("metadata", {})
            out |= {
                "resolved": True,
                "kind": "InterPro entry",
                "name": md.get("name", {}).get("name"),
                "type": md.get("type"),
            }
        else:
            # ensembl: and UniProtKB-SubCell: tokens are namespaced identifiers we
            # deliberately do not invent a resolver for.  Unresolved is a result.
            out |= {"kind": "unresolved namespace"}
    except Exception as exc:  # noqa: BLE001 - record the failure, do not guess
        out |= {"error": f"{type(exc).__name__}: {exc}"}
    return out


def paint_nodes() -> dict[str, list[dict[str, str]]]:
    tsv = repo_root() / "interpro" / "panther" / FAMILY / f"{FAMILY}-paint.tsv"
    nodes: dict[str, list[dict[str, str]]] = {}
    with tsv.open() as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            nodes.setdefault(row["node"], []).append(
                {
                    "go_id": row["go_id"],
                    "aspect": row["aspect"],
                    "evidence": row["evidence"],
                    "negated": row["negated"],
                    "seeds": row["seeds"].split("|"),
                    "taxon": row["taxon"],
                    "date": row["date"],
                }
            )
    return nodes


def family_members() -> list[dict[str, str]]:
    csv_path = repo_root() / "interpro" / "panther" / FAMILY / f"{FAMILY}-entries.csv"
    with csv_path.open() as fh:
        return list(csv.DictReader(fh))


def run() -> dict[str, object]:
    tokens = goa_with_from()
    entities = {t: {**resolve(t), "used_by": rows} for t, rows in tokens.items()}

    nodes = paint_nodes()
    inherited = {t for t in tokens if t.startswith("PANTHER:PTN")}
    not_inherited = {n: rows for n, rows in nodes.items() if f"PANTHER:{n}" not in inherited}

    # For each inherited node: is any seed the target's own ortholog group, or is
    # the whole evidence base a paralogous branch?  That is the substantive
    # question about an IBA, and it is answerable only after resolving the seeds.
    target_lineage = {"UniProtKB:P98171", "RGD:628901"}  # ARHGAP4 and its rat ortholog
    node_support = {}
    for node in sorted(inherited):
        rows = nodes.get(node.split(":", 1)[1], [])
        for r in rows:
            seeds = [s for s in r["seeds"] if s]
            node_support[f"{node} {r['go_id']}"] = {
                "go_id": r["go_id"],
                "taxon_scope": r["taxon"] or "(unscoped)",
                "seeds": seeds,
                "seed_symbols": [
                    entities.get(s, {}).get("symbol") or resolve(s).get("symbol") or s
                    for s in seeds
                ],
                "includes_target_lineage": bool(set(seeds) & target_lineage),
                "self_seeded_only": seeds == ["UniProtKB:P98171"],
            }

    unresolved = sorted(t for t, e in entities.items() if not e.get("resolved"))
    return {
        "family": FAMILY,
        "target": TARGET,
        "entities": entities,
        "unresolved_tokens": unresolved,
        "paint_nodes_inherited_by_target": node_support,
        "paint_nodes_not_inherited_by_target": not_inherited,
        "family_members": family_members(),
        "nodes_supported_only_by_paralogous_branch": sorted(
            k for k, v in node_support.items() if not v["includes_target_lineage"]
        ),
    }


def self_test() -> int:
    checks: list[tuple[str, str]] = []

    # 1. The WITH/FROM reader must find the tokens that are actually in the TSV.
    toks = goa_with_from()
    checks.append(
        (
            "WITH/FROM reader finds the known tokens",
            "PASS"
            if {"RGD:628901", "UniProtKB:O75044", "PANTHER:PTN002306152"} <= set(toks)
            else f"FAIL {sorted(toks)}",
        )
    )
    # 2. NEGATIVE CONTROL: it must not invent tokens that are not there.
    checks.append(
        (
            "negative control: no phantom tokens",
            "PASS" if "MGI:MGI:0000000" not in toks else "FAIL",
        )
    )
    # 3. A MOD id must resolve to a real symbol, not to None silently.
    r = resolve("RGD:628901")
    checks.append(
        (
            "MOD id resolves to a symbol",
            "PASS" if r.get("symbol") == "Arhgap4" else f"FAIL {r}",
        )
    )
    # 4. A deliberately bogus id must be reported unresolved, never substituted.
    b = resolve("MGI:MGI:99999999")
    checks.append(
        (
            "bogus id reports unresolved rather than guessing",
            "PASS" if not b.get("resolved") and not b.get("symbol") else f"FAIL {b}",
        )
    )
    # 5. The PAINT join must see a node the target does NOT inherit -- if every
    #    node came back inherited, the join key would be wrong and the
    #    'deliberate boundary' observation would be vacuous.
    out = run()
    checks.append(
        (
            "PAINT join identifies a node the target does not inherit",
            "PASS"
            if out["paint_nodes_not_inherited_by_target"]
            else "FAIL (all nodes inherited: join key is probably wrong)",
        )
    )
    # 6. ...and must also see nodes it does inherit.
    checks.append(
        (
            "PAINT join identifies inherited nodes",
            "PASS" if len(out["paint_nodes_inherited_by_target"]) >= 4 else "FAIL",
        )
    )

    for name, verdict in checks:
        print(
            f"  [{verdict.split()[0]}] {name}"
            + ("" if verdict.startswith("PASS") else f" -- {verdict}")
        )
    bad = [c for c in checks if not c[1].startswith("PASS")]
    print(f"\n{len(checks) - len(bad)}/{len(checks)} self-tests passed")
    return 1 if bad else 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    if args.self_test:
        return self_test()

    out = run()
    dest = Path(__file__).with_name("entities.json")
    dest.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")

    print("WITH/FROM entities")
    for tok, e in sorted(out["entities"].items()):
        flag = " <-- TARGET ITSELF" if e.get("is_target") else ""
        print(
            f"  {tok:<34} {str(e.get('symbol') or e.get('kind')):<22} "
            f"{str(e.get('taxon') or e.get('name') or ''):<44}{flag}"
        )
    print("\nunresolved:", out["unresolved_tokens"] or "none")

    print("\nPAINT nodes INHERITED by ARHGAP4")
    for k, v in out["paint_nodes_inherited_by_target"].items():
        print(f"  {k} taxon={v['taxon_scope']}")
        print(f"      seeds: {', '.join(v['seed_symbols'])}")
        print(
            f"      includes target lineage: {v['includes_target_lineage']}"
            f"   self-seeded only: {v['self_seeded_only']}"
        )
    print("\nPAINT nodes NOT inherited by ARHGAP4")
    for node, rows in out["paint_nodes_not_inherited_by_target"].items():
        for r in rows:
            print(f"  {node} {r['go_id']} ({r['aspect']}) taxon={r['taxon']}")
    print(
        "\nnodes supported ONLY by a paralogous branch:",
        out["nodes_supported_only_by_paralogous_branch"] or "none",
    )
    print(f"\nwrote {dest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
