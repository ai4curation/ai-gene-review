"""Pilot B: can expression argue against a paralog inheriting a function?

An IBA follows from descent below a PAINT node (PTN). When two paralogs below
that node both inherit an anatomy-bearing term, the paralog that *is* detected
in the term's anatomy is a positive control: it shows the anatomy was sampled
and the assay could see a family member there. Its sister's absence from the
same anatomy is then informative in a way that a lone absent call is not.

Part 1 (corpus): every (PTN, GO term) IBA group in the human GOA files that
covers two or more reviewed human genes is scored with the Pilot A classifier;
groups where one paralog is detected in the anatomy and another is absent are
listed, with the reviewers' actions on each IBA row.

Part 2 (cases, ``data/paralog_cases.yaml``): leaves below a named PTN are read
from the PANTHER tree, mapped to Bgee gene ids through UniProt, and compared
for the propagated terms (or, for terms without GO anatomy, an explicit
context such as the satisfiability engine's gluconeogenic tissues).

Outputs: ``results/paralog_divergence.yaml``, ``results/paralog_discordant_groups.tsv``,
``data/panther_leaves.tsv``, ``data/uniprot_bgee_map.tsv``,
``data/paralog_calls_{human,mouse}.tsv``.

Usage (from repo root, after extract_corpus.py):
    uv run python projects/BGEEDB_EXPRESSION/scripts/paralogs.py
"""

from __future__ import annotations

import csv
import json
import pickle
import sys
import urllib.parse
import urllib.request
from collections import defaultdict
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).parent))
import bgee_common as bc  # noqa: E402

TREEINFO = "https://pantherdb.org/services/oai/pantherdb/treeinfo?family={f}"
UNIPROT = "https://rest.uniprot.org/uniprotkb/accessions?{q}"
TAXA = {"human": 9606, "mouse": 10090}
DETECTED = {"ENRICHED", "CONSISTENT"}
STRICT_ABSENT = {"ABSENT"}
STAGE_MERGED_ABSENT = {"ABSENT_DEVELOPMENTAL"}


# ---------------------------------------------------------------------------
# PANTHER tree and UniProt -> Bgee mapping
# ---------------------------------------------------------------------------


def panther_tree(family: str) -> dict:
    path = bc.CACHE / "panther" / f"{family}.json"
    bc.fetch(TREEINFO.format(f=family), path, timeout=300)
    return json.loads(path.read_text())


def _kids(n: dict) -> list[dict]:
    c = n.get("children", {}).get("annotation_node", [])
    return [c] if isinstance(c, dict) else c


def _find(n: dict, pid: str, path: tuple[str, ...] = ()) -> tuple[dict, tuple[str, ...]] | None:
    here = path + (n.get("persistent_id", ""),)
    if n.get("persistent_id") == pid:
        return n, here
    for c in _kids(n):
        hit = _find(c, pid, here)
        if hit:
            return hit
    return None


def leaves_below(family: str, ptn: str) -> list[dict]:
    """Leaves under ``ptn`` with organism, UniProt accession and path from the node."""
    tree = panther_tree(family)
    root = tree["search"]["tree_topology"]["annotation_node"]
    hit = _find(root, ptn)
    if hit is None:
        raise SystemExit(f"{ptn} not found in {family}")
    node, _ = hit
    out = []

    def walk(n: dict, path: tuple[str, ...]) -> None:
        kids = _kids(n)
        if not kids:
            name = n.get("node_name", "")
            acc = name.split("UniProtKB=")[-1] if "UniProtKB=" in name else ""
            out.append({"leaf": n.get("persistent_id"), "organism": n.get("organism", ""), "uniprot": acc,
                        "definition": n.get("definition", ""), "path": path})
        for c in kids:
            walk(c, path + (c.get("persistent_id", ""),))

    walk(node, (ptn,))
    return out


def uniprot_bgee(accessions: list[str]) -> dict[str, dict]:
    """accession -> {taxon, gene, bgee}; cached in data/uniprot_bgee_map.tsv."""
    path = bc.DATA / "uniprot_bgee_map.tsv"
    known: dict[str, dict] = {}
    if path.exists():
        with path.open() as fh:
            known = {r["accession"]: r for r in csv.DictReader(fh, delimiter="\t")}
    todo = [a for a in accessions if a and a not in known]
    for i in range(0, len(todo), 100):
        q = urllib.parse.urlencode({"accessions": ",".join(todo[i:i + 100]),
                                    "fields": "accession,organism_id,gene_primary,xref_bgee", "format": "tsv"})
        req = urllib.request.Request(UNIPROT.format(q=q), headers={"User-Agent": "ai-gene-review/bgee-expression"})
        with urllib.request.urlopen(req, timeout=120) as r:
            lines = r.read().decode().splitlines()
        for row in csv.DictReader(lines, delimiter="\t"):
            known[row["Entry"]] = {"accession": row["Entry"], "taxon": row["Organism (ID)"],
                                   "gene": row["Gene Names (primary)"], "bgee": row["Bgee"].split(";")[0].strip()}
    bc.DATA.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as fh:
        w = csv.DictWriter(fh, ["accession", "taxon", "gene", "bgee"], delimiter="\t", lineterminator="\n")
        w.writeheader()
        for a in sorted(known):
            w.writerow({k: known[a][k] for k in ("accession", "taxon", "gene", "bgee")})
    return known


def calls_for(species: str, ids: dict[str, str]) -> dict[str, list[bc.Call]]:
    """Bgee simple calls for {ensembl: symbol}; cached in data/paralog_calls_<species>.tsv."""
    path = bc.DATA / f"paralog_calls_{species}.tsv"
    have, symbols = (bc.read_calls_tsv(path) if path.exists() else ({}, {}))
    missing = [g for g in ids if g not in have]
    if missing:
        have.update(bc.read_simple_calls(species, missing))
        symbols.update(ids)
        bc.write_calls_tsv(have, symbols, path)
    return {g: have.get(g, []) for g in ids}


# ---------------------------------------------------------------------------
# Scoring
# ---------------------------------------------------------------------------


def profile_percentile(calls: list[bc.Call], score: float) -> float:
    scores = [c.score for c in calls if c.quality in ("gold", "silver")]
    return sum(1 for s in scores if s < score) / len(scores) if scores else 0.0


def score_term(go_id: str, calls: list[bc.Call], go: bc.GoAnatomy, anat: bc.Anatomy, nonautonomous: bool) -> dict:
    v = bc.classify_annotation(go_id, calls, go, anat, nonautonomous=nonautonomous)
    best = None
    if v.cls in bc.CONSISTENT:
        present = [c for c in calls if c.entity in v.evidence and c.state == "present"]
        best = max(present, key=lambda c: c.score)
    pct = profile_percentile(calls, best.score) if best else 0.0
    tier = v.cls if v.cls not in bc.CONSISTENT else ("ENRICHED" if pct >= 0.9 else "CONSISTENT")
    return {"tier": tier, "relation": v.cls, "best": f"{best.entity} {best.name} ({best.score:.1f})" if best else None,
            "percentile_in_own_profile": round(pct, 2),
            "absent_in": [f"{c.entity} {c.name}" for c in calls if c.entity in v.evidence and c.state == "absent"][:6]
            if not best else []}


def score_context(targets: list[str], calls: list[bc.Call], anat: bc.Anatomy) -> dict:
    """Expression in an explicit tissue context (for terms with no GO anatomy)."""
    gold = [c for c in calls if c.quality in ("gold", "silver")]
    related = [c for c in gold if any(anat.within(c.entity, t) or anat.contains(c.entity, t) for t in targets)]
    present = [c for c in related if c.state == "present"]
    top = sorted((c for c in gold if c.state == "present"), key=lambda c: -c.score)[:10]
    in_ctx = [c for c in top if any(anat.within(c.entity, t) for t in targets)]
    all_present = [c for c in gold if c.state == "present"]
    ctx_share = sum(1 for c in all_present if any(anat.within(c.entity, t) for t in targets)) / len(all_present) if all_present else 0.0
    best = max(present, key=lambda c: c.score) if present else None
    return {
        "present_in_context": len(present),
        "absent_in_context": len(related) - len(present),
        "best_in_context": f"{best.entity} {best.name} ({best.score:.1f})" if best else None,
        "percentile_in_own_profile": round(profile_percentile(calls, best.score), 2) if best else 0.0,
        "top10_in_context": f"{len(in_ctx)}/{len(top)}",
        "expected_top10_in_context_by_chance": round(ctx_share * len(top), 1),
        "top_tissues": [f"{c.name} ({c.score:.0f})" for c in top[:5]],
        "breadth_present_fraction": round(sum(1 for c in gold if c.state == "present") / len(gold), 2) if gold else None,
    }


# ---------------------------------------------------------------------------
# Part 1: corpus IBA groups
# ---------------------------------------------------------------------------


def corpus_groups(go: bc.GoAnatomy, anat: bc.Anatomy) -> tuple[dict, list[dict]]:
    with (bc.CACHE / "corpus_calls.pkl").open("rb") as fh:
        blob = pickle.load(fh)
    calls = blob["calls"]
    ens_of = {sym: gid for gid, sym in blob["symbols"].items()}
    actions: dict[tuple[str, str], str] = {}
    rows_for_secretion = []
    with (bc.CACHE / "corpus_annotations.tsv").open() as fh:
        for r in csv.DictReader(fh, delimiter="\t"):
            rows_for_secretion.append(r)
            if r["evidence"] == "IBA" and not r["negated"]:
                actions[(r["gene"], r["go_id"])] = r["action"]
    secreted = bc.nonautonomous_genes(rows_for_secretion, go, {"REMOVE", "MARK_AS_OVER_ANNOTATED"})

    groups: dict[tuple[str, str], set[str]] = defaultdict(set)
    for goa in sorted(bc.REPO.glob("genes/human/*/*-goa.tsv")):
        gene = goa.parent.name
        if gene not in ens_of:
            continue
        with goa.open() as fh:
            for row in csv.DictReader(fh, delimiter="\t"):
                if row.get("GO EVIDENCE CODE") != "IBA" or "NOT" in (row.get("QUALIFIER") or ""):
                    continue
                for tok in (row.get("WITH/FROM") or "").split("|"):
                    if tok.startswith("PANTHER:PTN"):
                        groups[(tok.split(":", 1)[1], row["GO TERM"])].add(gene)

    memo: dict[tuple[str, str], dict] = {}
    multi = 0
    anatomy_groups = 0
    discordant = []
    for (ptn, gid), genes in sorted(groups.items()):
        if len(genes) < 2:
            continue
        multi += 1
        tg, _, _ = go.targets(gid)
        if not tg:
            continue
        anatomy_groups += 1
        scored = {}
        for g in sorted(genes):
            key = (g, gid)
            if key not in memo:
                memo[key] = score_term(gid, calls.get(ens_of[g], []), go, anat, g in secreted)
            scored[g] = memo[key]
        det = [g for g, s in scored.items() if s["tier"] in DETECTED]
        strict = [g for g, s in scored.items() if s["tier"] in STRICT_ABSENT]
        merged = [g for g, s in scored.items() if s["tier"] in STAGE_MERGED_ABSENT]
        if det and (strict or merged):
            discordant.append({
                "ptn": ptn, "go_id": gid, "go_label": go.names.get(gid, ""),
                "targets": "|".join(sorted({a for _, a in tg})),
                "detected": ",".join(f"{g}:{scored[g]['tier']}:{actions.get((g, gid), '-')}" for g in det),
                "absent_strict": ",".join(f"{g}:{actions.get((g, gid), '-')}" for g in strict),
                "absent_stage_merged": ",".join(f"{g}:{actions.get((g, gid), '-')}" for g in merged),
            })

    def action_mix(field: str) -> dict:
        mix: dict[str, int] = defaultdict(int)
        for d in discordant:
            for tok in filter(None, d[field].split(",")):
                mix[tok.rsplit(":", 1)[-1]] += 1
        return dict(sorted(mix.items(), key=lambda kv: -kv[1]))

    summary = {
        "iba_groups_with_2plus_reviewed_human_genes": multi,
        "of_which_anatomy_bearing": anatomy_groups,
        "discordant_groups": len(discordant),
        "discordant_with_strict_absence": sum(1 for d in discordant if d["absent_strict"]),
        "review_actions_on_detected_paralogs": action_mix("detected"),
        "review_actions_on_strictly_absent_paralogs": action_mix("absent_strict"),
        "review_actions_on_stage_merged_absent_paralogs": action_mix("absent_stage_merged"),
    }
    return summary, discordant


# ---------------------------------------------------------------------------
# Part 2: named cases
# ---------------------------------------------------------------------------


def run_case(case: dict, go: bc.GoAnatomy, anat: bc.Anatomy) -> tuple[dict, list[dict]]:
    leaves = leaves_below(case["family"], case["ibd_node"])
    mapping = uniprot_bgee([lf["uniprot"] for lf in leaves])
    wanted_taxa = {str(TAXA[s]): s for s in case["species"]}
    clade_of = {}
    for label, ptn in (case.get("clades") or {}).items():
        for lf in leaves:
            if ptn in lf["path"]:
                clade_of[lf["leaf"]] = label
    members = []
    for lf in leaves:
        m = mapping.get(lf["uniprot"])
        if not m or m["taxon"] not in wanted_taxa or not m["bgee"]:
            continue
        members.append({**lf, "species": wanted_taxa[m["taxon"]], "gene": m["gene"], "bgee": m["bgee"],
                        "clade": clade_of.get(lf["leaf"], "")})
    by_species: dict[str, dict[str, str]] = defaultdict(dict)
    for m in members:
        by_species[m["species"]][m["bgee"]] = m["gene"]
    calls = {}
    for sp, ids in by_species.items():
        calls.update(calls_for(sp, ids))

    for c in case.get("context", {}).get("anatomy", []):
        if c not in anat.names:
            raise SystemExit(f"context anatomy {c} not in UBERON")
    out_members = []
    for m in sorted(members, key=lambda m: (m["species"], m["gene"])):
        entry = {"gene": m["gene"], "species": m["species"], "uniprot": m["uniprot"], "bgee": m["bgee"],
                 "panther_leaf": m["leaf"], "clade": m["clade"], "terms": {}}
        for gid in case["terms"]:
            tg, _, _ = go.targets(gid)
            if tg:
                entry["terms"][f"{gid} {go.names.get(gid, '')}"] = score_term(gid, calls[m["bgee"]], go, anat, False)
            elif case.get("context"):
                entry["terms"][f"{gid} {go.names.get(gid, '')}"] = {
                    "context": case["context"]["label"],
                    **score_context(case["context"]["anatomy"], calls[m["bgee"]], anat),
                }
        out_members.append(entry)
    result = {"family": case["family"], "ibd_node": case["ibd_node"], "note": " ".join(case["ibd_node_note"].split()),
              "leaves_below_node": len(leaves), "scored_members": out_members}
    return result, members


def main() -> None:
    go = bc.load_go_anatomy()
    anat = bc.load_anatomy()
    summary, discordant = corpus_groups(go, anat)
    with (bc.RESULTS / "paralog_discordant_groups.tsv").open("w", newline="") as fh:
        fields = ["ptn", "go_id", "go_label", "targets", "detected", "absent_strict", "absent_stage_merged"]
        w = csv.DictWriter(fh, fields, delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(discordant)

    cfg = yaml.safe_load((bc.DATA / "paralog_cases.yaml").read_text())
    cases = {}
    leaf_rows = []
    for case in cfg["cases"]:
        res, members = run_case(case, go, anat)
        cases[case["id"]] = res
        for m in members:
            leaf_rows.append({"case": case["id"], "leaf": m["leaf"], "species": m["species"], "gene": m["gene"],
                              "uniprot": m["uniprot"], "bgee": m["bgee"], "clade": m["clade"],
                              "path": ">".join(m["path"])})
    with (bc.DATA / "panther_leaves.tsv").open("w", newline="") as fh:
        w = csv.DictWriter(fh, list(leaf_rows[0]), delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(leaf_rows)
    out = {"bgee_release": bc.BGEE_RELEASE, "corpus": summary, "cases": cases}
    (bc.RESULTS / "paralog_divergence.yaml").write_text(yaml.safe_dump(out, sort_keys=False, width=110))
    print(yaml.safe_dump(summary, sort_keys=False))


if __name__ == "__main__":
    main()
