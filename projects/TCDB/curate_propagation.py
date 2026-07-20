#!/usr/bin/env python3
"""Curate PROPAGATION justifiability for every GO->TC xref source, from UniProt evidence.

GO's TC xrefs (tc2go.from_go.sssom.yaml) are unreviewed leads. The propagation
question -- "is it justifiable for a protein carrying this TC id to inherit this
GO term?" -- is answered here with **empirical evidence**, not assertion:

  For each (TC, GO) source pair, fetch the reviewed (Swiss-Prot) proteins carrying
  that TC id, and measure what fraction also carry the GO term (ontology-closure
  expanded, so a member with a more specific child term still counts). The
  fraction is the propagation signal:

    frac high  -> the activity is shared across the TC group  -> PROPAGATION JUSTIFIED
    frac low   -> the GO term is a minority/subfamily property -> NOT JUSTIFIED here
    no members -> nothing to test                              -> UNCERTAIN (kept a source)

TC id matching respects level: a 5-level system is matched exactly; a coarser id
(family/subfamily) is matched by `<id>` OR `<id>.*` (the dot forces a boundary so
`2.A.1` does not spuriously match `2.A.10`). GO closure is computed locally from
the cached ``go-basic.obo`` (is_a), so only ONE UniProt call per TC is needed.

Verdict rule (encoded as the SSSOM predicate):
  * exactMatch  (JUSTIFIED)      : N>=2 and frac>=0.7, or N==1 and frac==1.0
  * narrowMatch (NOT_AT_LEVEL)   : N>=3 and frac<0.5
  * relatedMatch(UNCERTAIN)      : everything else (no members, or ambiguous middle)

Emits:
  * data/propagation_evidence.tsv   -- tc, go, level, n_members, n_with_go, frac, verdict, members
  * tc2go.propagation.sssom.yaml    -- the same, as an SSSOM set with evidence in each comment

Usage::

    uv run python curate_propagation.py                 # full run (~185 UniProt calls)
    uv run python curate_propagation.py --limit 10       # smoke test
"""
from __future__ import annotations

import argparse
import time
import urllib.parse
import urllib.request
from collections import defaultdict
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
OBO = DATA / "go-basic.obo"
FROM_GO = HERE / "tc2go.from_go.sssom.yaml"
EVIDENCE_TSV = DATA / "propagation_evidence.tsv"
UNIPROT = "https://rest.uniprot.org/uniprotkb/search"


def go_descendants() -> dict[str, set[str]]:
    """Build {term: set of descendants incl. self} from go-basic.obo is_a edges."""
    parents: dict[str, set[str]] = defaultdict(set)
    cur = None
    for line in OBO.read_text().splitlines():
        if line == "[Term]":
            cur = None
        elif line.startswith("id: GO:"):
            cur = line[4:].strip()
        elif cur and line.startswith("is_a: GO:"):
            parents[cur].add(line.split("is_a:", 1)[1].strip().split()[0])
    children: dict[str, set[str]] = defaultdict(set)
    for c, ps in parents.items():
        for p in ps:
            children[p].add(c)
    # descendants via BFS
    desc: dict[str, set[str]] = {}

    def collect(term: str) -> set[str]:
        if term in desc:
            return desc[term]
        out = {term}
        for ch in children.get(term, ()):
            out |= collect(ch)
        desc[term] = out
        return out

    all_terms = set(parents) | set(children)
    for t in all_terms:
        collect(t)
    return desc


def normalize_tc(tc: str) -> str:
    """Strip TCDB placeholder segments ('-') so 1.B.1.-.- -> 1.B.1, 3.A.3.-.- -> 3.A.3."""
    parts = tc.split(".")
    while parts and parts[-1] == "-":
        parts.pop()
    return ".".join(parts)


def tc_query(tc: str) -> str:
    """UniProt query matching reviewed proteins carrying this (normalized) TC id, level-aware."""
    if tc.count(".") >= 4:  # 5-level system -> exact
        return f"xref:tcdb-{tc} AND reviewed:true"
    # coarser -> exact OR dot-bounded descendants (the dot stops 2.A.1 matching 2.A.10)
    return f"(xref:tcdb-{tc} OR xref:tcdb-{tc}.*) AND reviewed:true"


def fetch_members(tc: str) -> list[tuple[str, set[str]]]:
    """Return [(accession, {go_ids})] for reviewed proteins carrying the TC id."""
    q = urllib.parse.urlencode({"query": tc_query(tc), "fields": "accession,go_id",
                                "format": "tsv", "size": 500})
    req = urllib.request.Request(f"{UNIPROT}?{q}", headers={"Accept": "text/plain"})
    with urllib.request.urlopen(req, timeout=90) as r:  # noqa: S310
        lines = r.read().decode("utf-8", "replace").splitlines()
    out = []
    for line in lines[1:]:  # skip header
        parts = line.split("\t")
        acc = parts[0]
        gos = {g.strip() for g in (parts[1].split(";") if len(parts) > 1 else []) if g.strip()}
        out.append((acc, gos))
    return out


CAP = 500  # UniProt page size; n at the cap is a floor, not an exact count


def verdict(n: int, k: int, level: int) -> tuple[str, str, str]:
    """(predicate_id, predicate_label, label) from member count n, GO-carrying count k, TC level.

    Class/subclass-level xrefs (level <= 2) and capped member sets are too coarse to score, so
    they stay UNCERTAIN regardless of fraction.
    """
    if level <= 2 or n >= CAP:
        return "skos:relatedMatch", "related match", "UNCERTAIN"
    frac = k / n if n else 0.0
    if (n >= 2 and frac >= 0.7) or (n == 1 and frac == 1.0):
        return "skos:exactMatch", "exact match", "JUSTIFIED"
    if n >= 3 and frac < 0.5:
        return "skos:narrowMatch", "narrow match", "NOT_JUSTIFIED_AT_LEVEL"
    return "skos:relatedMatch", "related match", "UNCERTAIN"


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--limit", type=int, default=0, help="only process the first N TC ids (smoke test)")
    ap.add_argument("--delay", type=float, default=0.1, help="seconds between UniProt calls")
    args = ap.parse_args(argv)

    src = yaml.safe_load(FROM_GO.read_text())
    # tc -> list of (go, go_label)
    tc_map: dict[str, list[tuple[str, str]]] = defaultdict(list)
    for m in src["mappings"]:
        tc_map[m["subject_id"].replace("TC:", "")].append((m["object_id"], m["object_label"]))
    desc = go_descendants()
    tcs = sorted(tc_map)
    if args.limit:
        tcs = tcs[: args.limit]

    rows = []
    for i, tc in enumerate(tcs, 1):
        norm = normalize_tc(tc)
        level = norm.count(".") + 1
        members = fetch_members(norm)
        n = len(members)
        for go, go_label in tc_map[tc]:
            targets = desc.get(go, {go})
            k = sum(1 for _acc, gos in members if gos & targets)
            pred_id, pred_lab, verd = verdict(n, k, level)
            rows.append({
                "tc": tc, "go": go, "go_label": go_label,
                "level": level, "n": n, "k": k,
                "frac": round(k / n, 3) if n else 0.0,
                "verdict": verd, "pred_id": pred_id, "pred_lab": pred_lab,
                "members": ";".join(acc for acc, _ in members[:20]),
            })
        print(f"[{i}/{len(tcs)}] TC:{tc}"
              + (f" (norm {norm})" if norm != tc else "") + f"  members={n}")
        time.sleep(args.delay)

    # evidence TSV
    DATA.mkdir(exist_ok=True)
    cols = ["tc", "go", "go_label", "level", "n", "k", "frac", "verdict", "members"]
    with EVIDENCE_TSV.open("w") as f:
        f.write("\t".join(cols) + "\n")
        for r in rows:
            f.write("\t".join(str(r[c]) for c in cols) + "\n")

    # SSSOM
    counts = defaultdict(int)
    mappings = []
    for r in sorted(rows, key=lambda r: (r["tc"], r["go"])):
        counts[r["verdict"]] += 1
        mappings.append({
            "subject_id": f"TC:{r['tc']}",
            "subject_label": "",
            "predicate_id": r["pred_id"],
            "predicate_label": r["pred_lab"],
            "object_id": r["go"],
            "object_label": r["go_label"],
            "mapping_justification": "semapv:CompositeMatching",
            "comment": (
                f"Propagation: {r['verdict']}. Evidence: {r['k']}/{r['n']} reviewed Swiss-Prot "
                f"proteins carrying TC {r['tc']} (level {r['level']}) also carry {r['go']} "
                f"(GO closure). Source: GO xref + UniProt member evidence."
            ),
        })
    doc = {
        "curie_map": {
            "TC": "http://www.tcdb.org/search/result.php?tc=",
            "GO": "http://purl.obolibrary.org/obo/GO_",
            "skos": "http://www.w3.org/2004/02/skos/core#",
            "semapv": "https://w3id.org/semapv/vocab/",
        },
        "mapping_set_id": "https://w3id.org/ai4curation/ai-gene-review/mappings/tc2go-propagation",
        "mapping_set_title": "TC -> GO propagation verdicts (GO xref leads scored by UniProt evidence)",
        "mapping_set_description": (
            "Every GO->TC xref source (tc2go.from_go.sssom.yaml), scored for propagation "
            "justifiability against UniProt member evidence: fraction of reviewed proteins carrying "
            "the TC id that also carry the GO term (closure). exactMatch = JUSTIFIED (activity shared "
            "across the TC group); narrowMatch = NOT justified at this TC level (minority/subfamily "
            "property); relatedMatch = UNCERTAIN (no members or ambiguous). Evidence in each comment; "
            f"full table in data/propagation_evidence.tsv. Verdicts: {dict(counts)}."
        ),
        "license": "https://creativecommons.org/licenses/by/4.0/",
        "creator_label": ["AI Gene Review project (curate_propagation.py; GO xref + UniProt evidence)"],
        "subject_source": "tcdb",
        "object_source": "GO",
        "mappings": mappings,
    }
    header = (
        "# TC -> GO PROPAGATION verdicts (SSSOM) -- GENERATED by curate_propagation.py\n"
        "# Each GO TC-xref lead scored against UniProt member evidence (fraction of reviewed proteins\n"
        "# with the TC id that also carry the GO term, closure-expanded). exactMatch=JUSTIFIED,\n"
        "# narrowMatch=NOT justified at this TC level, relatedMatch=UNCERTAIN. Evidence in comments;\n"
        "# full table in data/propagation_evidence.tsv. DO NOT HAND-EDIT (regenerate).\n"
    )
    (HERE / "tc2go.propagation.sssom.yaml").write_text(
        header + yaml.safe_dump(doc, sort_keys=False, default_flow_style=False, width=100, allow_unicode=True)
    )
    print(f"\n# {len(rows)} pairs scored -> verdicts {dict(counts)}")
    print(f"# wrote {EVIDENCE_TSV} and tc2go.propagation.sssom.yaml")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
