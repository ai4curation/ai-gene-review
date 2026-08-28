#!/usr/bin/env python3
"""Map ProTrek retrieved GO-annotation sentences to GO ids and compare with GOA.

The ProTrek SwissProt text index stores GO annotations as templated sentences
("The GO term for this protein involving <aspect> incorporates <label>."), so a
protein-to-text retrieval is turned back into a GO prediction by parsing the
label and resolving it against the frozen GO release used elsewhere in this repo
(``ai_gene_review.bioreason_ontology``).

Each prediction is then placed in the same overlap categories the ProtNLM2
evaluation used, so the two models can be compared on the same proteins:

  EXACT          predicted term is annotated in GOA for this protein
  LESS_SPECIFIC  predicted term is a strict ancestor of a GOA term
  MORE_SPECIFIC  predicted term is a strict descendant of a GOA term
  NO_OVERLAP     no is_a/part_of path to any GOA term
  NOT_IN_GOA     protein has no curated GOA annotations at all

Usage:
  uv run python projects/PROTREK_EVALUATION/analyze_hits.py \
      --hits projects/PROTREK_EVALUATION/argo50_protrek_hits.tsv \
      --topk 5 \
      --out projects/PROTREK_EVALUATION/argo50_protrek_go_calls.csv
"""
from __future__ import annotations

import argparse
import csv
import glob
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from ai_gene_review.bioreason_ontology import ensure_frozen_go  # noqa: E402

SENTENCE_RE = re.compile(
    r"^The GO term for this protein involving "
    r"(molecular function|biological process|cellular component)"
    r" incorporates (.+?)\.?$"
)
ASPECT_CODE = {"molecular function": "F", "biological process": "P", "cellular component": "C"}
CLOSURE_RELATIONS = ("is_a", "part_of")


def parse_obo(path: Path):
    """Return (label->ids, id->term) from a go-basic OBO file.

    Only ``is_a`` and ``part_of`` are followed for the closure, matching the
    graph GO itself uses for annotation propagation in go-basic.
    """
    by_label: dict[str, set[str]] = defaultdict(set)
    terms: dict[str, dict] = {}
    current = None
    in_term = False
    for line in path.read_text().splitlines():
        if line == "[Term]":
            in_term = True
            current = {"id": None, "name": None, "namespace": None,
                       "parents": set(), "obsolete": False, "synonyms": set()}
            continue
        if line.startswith("["):
            in_term = False
            current = None
            continue
        if not in_term or not line:
            if in_term and not line and current and current["id"]:
                terms[current["id"]] = current
                current = None
                in_term = False
            continue
        key, _, value = line.partition(": ")
        if key == "id":
            current["id"] = value
        elif key == "name":
            current["name"] = value
        elif key == "namespace":
            current["namespace"] = value
        elif key == "is_obsolete" and value == "true":
            current["obsolete"] = True
        elif key == "is_a":
            current["parents"].add(value.split(" ! ")[0].strip())
        elif key == "relationship" and value.startswith("part_of "):
            current["parents"].add(value.split()[1])
        elif key == "synonym" and " EXACT " in value:
            m = re.match(r'"(.+?)"', value)
            if m:
                current["synonyms"].add(m.group(1))
    if current and current.get("id"):
        terms[current["id"]] = current

    obsolete_by_label: dict[str, set[str]] = defaultdict(set)
    for tid, t in terms.items():
        if not t["name"]:
            continue
        # GO prefixes an obsoleted term's label with "obsolete "; the ProTrek
        # index still carries the pre-obsoletion spelling.
        if t["obsolete"] or t["name"].startswith("obsolete "):
            stripped = t["name"][len("obsolete "):] if t["name"].startswith("obsolete ") else t["name"]
            obsolete_by_label[stripped.lower()].add(tid)
            obsolete_by_label[normalize_label(stripped)].add(tid)
            continue
        for name in {t["name"], *t["synonyms"]}:
            by_label[name.lower()].add(tid)
            norm = normalize_label(name)
            if norm != name.lower():
                by_label[norm].add(tid)
    return by_label, terms, obsolete_by_label


def normalize_label(label: str) -> str:
    """Collapse punctuation differences so GO label renames still resolve.

    GO periodically restyles labels without changing the concept, e.g.
    "histone H3-K27 demethylation" -> "histone H3K27 demethylation". ProTrek's
    text index is frozen at its build date, so its sentences carry the older
    spellings.
    """
    return re.sub(r"[^a-z0-9]+", "", label.lower())


def ancestors(go_id: str, terms: dict, cache: dict) -> set[str]:
    """Reflexive is_a/part_of ancestor closure."""
    if go_id in cache:
        return cache[go_id]
    seen = {go_id}
    stack = [go_id]
    cache[go_id] = seen  # guard against cycles
    while stack:
        cur = stack.pop()
        for parent in terms.get(cur, {}).get("parents", ()):
            if parent not in seen:
                seen.add(parent)
                stack.append(parent)
    cache[go_id] = seen
    return seen


def load_goa(acc: str) -> set[str]:
    hits = glob.glob(str(ROOT / "genes" / "*" / acc / f"{acc}-goa.tsv"))
    if not hits:
        return set()
    terms = set()
    with open(hits[0]) as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            qualifier = (row.get("QUALIFIER") or "")
            if qualifier.startswith("NOT"):
                continue
            term = row.get("GO TERM")
            if term:
                terms.add(term.strip())
    return terms


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--hits", required=True, type=Path)
    ap.add_argument("--topk", type=int, default=5, help="ProTrek ranks kept as the prediction set")
    ap.add_argument("--out", required=True, type=Path)
    ap.add_argument("--summary-out", type=Path, default=None)
    args = ap.parse_args()

    obo = ensure_frozen_go()
    by_label, terms, obsolete_by_label = parse_obo(obo)
    print(f"GO release parsed: {len(terms)} terms, {len(by_label)} labels/synonyms", file=sys.stderr)

    rows = [r for r in csv.DictReader(args.hits.open(), delimiter="\t")
            if r["subsection"] == "GO_annotation" and int(r["rank"]) <= args.topk]

    cache: dict[str, set[str]] = {}
    goa_cache: dict[str, set[str]] = {}
    out_rows = []
    unresolved = defaultdict(int)

    for r in rows:
        acc = r["accession"]
        m = SENTENCE_RE.match(r["text"].strip())
        if not m:
            unresolved[f"UNPARSED::{r['text'][:60]}"] += 1
            continue
        aspect, label = m.group(1), m.group(2).strip()
        ids = sorted(by_label.get(label.lower(), set()))
        resolution = "exact_label" if ids else ""
        if not ids:
            ids = sorted(by_label.get(normalize_label(label), set()))
            resolution = "normalized_label" if ids else ""
        if not ids:
            ids = sorted(obsolete_by_label.get(label.lower(), set())
                         or obsolete_by_label.get(normalize_label(label), set()))
            resolution = "obsolete_in_go" if ids else "unresolved"
        # Prefer the id whose namespace matches the sentence's declared aspect.
        want_ns = aspect.replace(" ", "_")
        matched = [i for i in ids if terms[i]["namespace"] == want_ns]
        go_id = matched[0] if matched else (ids[0] if ids else "")
        if not go_id:
            unresolved[label] += 1

        if acc not in goa_cache:
            goa_cache[acc] = load_goa(acc)
        goa = goa_cache[acc]

        if resolution == "obsolete_in_go":
            category = "OBSOLETE_TERM"
            match_term = ""
        elif not goa:
            category = "NOT_IN_GOA"
            match_term = ""
        elif not go_id:
            category = "UNRESOLVED"
            match_term = ""
        elif go_id in goa:
            category = "EXACT"
            match_term = go_id
        else:
            pred_anc = ancestors(go_id, terms, cache)
            desc_of = [g for g in goa if g in pred_anc]          # prediction is below a GOA term
            anc_of = [g for g in goa if go_id in ancestors(g, terms, cache)]  # prediction is above one
            if anc_of:
                category = "LESS_SPECIFIC"
                match_term = sorted(anc_of)[0]
            elif desc_of:
                category = "MORE_SPECIFIC"
                match_term = sorted(desc_of)[0]
            else:
                category = "NO_OVERLAP"
                match_term = ""

        out_rows.append({
            "accession": acc,
            "rank": int(r["rank"]),
            "protrek_score": float(r["protrek_score"]),
            "aspect": ASPECT_CODE[aspect],
            "pred_label": label,
            "pred_id": go_id,
            "label_resolution": resolution,
            "match_category": category,
            "goa_match": match_term,
            "goa_match_label": terms.get(match_term, {}).get("name", "") if match_term else "",
            "n_goa_terms": len(goa),
        })

    with args.out.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(out_rows[0].keys()))
        w.writeheader()
        w.writerows(out_rows)
    print(f"wrote {len(out_rows)} predictions to {args.out}", file=sys.stderr)

    counts = defaultdict(int)
    for r in out_rows:
        counts[r["match_category"]] += 1
    summary = {
        "topk": args.topk,
        "n_proteins": len({r["accession"] for r in out_rows}),
        "n_predictions": len(out_rows),
        "match_categories": dict(sorted(counts.items())),
        "aspect_counts": dict(sorted({a: sum(1 for r in out_rows if r["aspect"] == a)
                                      for a in {r["aspect"] for r in out_rows}}.items())),
        "label_resolution": dict(sorted({
            r: sum(1 for x in out_rows if x["label_resolution"] == r)
            for r in {x["label_resolution"] for x in out_rows}
        }.items())),
        "unresolved_labels": dict(sorted(unresolved.items())),
    }
    text = json.dumps(summary, indent=2)
    print(text)
    if args.summary_out:
        args.summary_out.write_text(text + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
