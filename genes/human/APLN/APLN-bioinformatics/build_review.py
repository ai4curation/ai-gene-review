"""Assemble APLN-ai-review.yaml from the seeded GOA rows plus the curation decisions.

Mechanism only. Every judgment lives in APLN_decisions.py and APLN_synthesis.py; every
``supporting_entities`` list is taken from the seeded row untouched, and every
``source_entities`` list is derived from it in order, so the two can never drift.

Reference titles are read from the cached publication frontmatter, never written from
memory. The script is idempotent: re-running it on its own output reproduces it.

    uv run python build_review.py            # rewrites ../APLN-ai-review.yaml
    uv run python build_review.py --check    # fail if the file would change
"""

from __future__ import annotations

import pathlib
import sys

import yaml

from APLN_decisions import AFFINAGE, BIOINF, DECISIONS, NEW_ROWS, Q, SOURCE_LABELS, UNIPROT
from APLN_synthesis import (
    CORE_FUNCTIONS,
    DESCRIPTION,
    KNOWLEDGE_GAPS,
    PROPOSED_NEW_TERMS,
    REFERENCE_REVIEWS,
    SUGGESTED_EXPERIMENTS,
    SUGGESTED_QUESTIONS,
)

HERE = pathlib.Path(__file__).resolve().parent
GENE_DIR = HERE.parent
REPO = GENE_DIR.parents[2]
REVIEW = GENE_DIR / "APLN-ai-review.yaml"
PUBS = REPO / "publications"

# Titles for non-PMID references keep whatever the seeder wrote; these two are the only
# reference ids with no machine source at all.
LOCAL_TITLES = {
    UNIPROT: "UniProtKB entry Q9ULZ1 (APEL_HUMAN), apelin",
    BIOINF: "APLN bioinformatics: apelin-13/-17 conservation, the ACE2 cleavage motif, and WITH/FROM resolution",
    AFFINAGE: "Affinage mechanistic annotation for APLN (human)",
}


def quote(key: str) -> str:
    if key not in Q:
        raise KeyError(f"unknown quote key {key!r}")
    return Q[key]


def supported(pairs) -> list[dict]:
    return [{"reference_id": ref, "supporting_text": quote(key)} for ref, key in pairs]


def cached_meta(pmid: str) -> dict:
    """Title and full-text availability, read from the cache - never written from memory."""
    path = PUBS / f"PMID_{pmid.split(':', 1)[1]}.md"
    if not path.exists():
        raise FileNotFoundError(f"{pmid} is cited but {path} is not cached")
    meta = yaml.safe_load(path.read_text().split("---", 2)[1])
    title = meta.get("title")
    if not title:
        raise ValueError(f"{path} has no title in its frontmatter")
    if "full_text_available" not in meta:
        raise ValueError(f"{path} frontmatter has no full_text_available flag")
    return {"title": " ".join(str(title).split()),
            "full_text_available": bool(meta["full_text_available"])}


def build_propagation(entities: list[str], prop: dict) -> dict:
    """Derive source_entities from the row's own supporting_entities, in order."""
    block: dict = {"root_cause": prop["root_cause"]}
    if prop.get("failure_modes"):
        block["failure_modes"] = list(prop["failure_modes"])
    status, comments = prop.get("status", {}), prop.get("comments", {})
    sources = []
    for ident in entities:
        entry: dict = {"source_id": ident}
        if ident in SOURCE_LABELS:
            entry["source_label"] = SOURCE_LABELS[ident]
        if ident not in status:
            raise KeyError(f"no source_status given for {ident}")
        entry["source_status"] = status[ident]
        if ident in comments:
            entry["comment"] = " ".join(comments[ident].split())
        sources.append(entry)
    if sources:
        block["source_entities"] = sources
    if prop.get("residue_claims"):
        block["residue_claims"] = prop["residue_claims"]
    if prop.get("residue_na"):
        block["residue_claims_not_applicable"] = " ".join(prop["residue_na"].split())
    return block


def build_review(dec: dict, entities: list[str]) -> dict:
    review: dict = {
        "summary": " ".join(dec["summary"].split()),
        "action": dec["action"],
        "reason": " ".join(dec["reason"].split()),
    }
    if dec.get("proposed_replacement_terms"):
        review["proposed_replacement_terms"] = dec["proposed_replacement_terms"]
    if dec.get("additional_reference_ids"):
        review["additional_reference_ids"] = dec["additional_reference_ids"]
    if dec.get("supported_by"):
        review["supported_by"] = supported(dec["supported_by"])
    if dec.get("prop"):
        if dec["action"] != "NEW" and not entities:
            raise ValueError("propagation_review on a row with no supporting_entities")
        review["propagation_review"] = build_propagation(entities, dec["prop"])
    return review


def main() -> int:
    doc = yaml.safe_load(REVIEW.read_text())

    seeded = [a for a in doc["existing_annotations"] if a.get("review", {}).get("action") != "NEW"]
    used = set()
    rebuilt = []
    for ann in seeded:
        ents = list(ann.get("supporting_entities") or [])
        key = (ann["term"]["id"], ann["evidence_type"], ann["original_reference_id"], tuple(ents))
        if key not in DECISIONS:
            raise KeyError(f"no decision for GOA row {key}")
        used.add(key)
        row = {k: v for k, v in ann.items() if k != "review"}
        row["review"] = build_review(DECISIONS[key], ents)
        rebuilt.append(row)
    unused = set(DECISIONS) - used
    if unused:
        raise KeyError(f"decisions that matched no GOA row: {sorted(unused)}")

    for spec in NEW_ROWS:
        ents = list(spec.get("supporting_entities") or [])
        row: dict = {"term": spec["term"], "evidence_type": spec["evidence_type"],
                     "original_reference_id": spec["original_reference_id"]}
        if ents:
            row["supporting_entities"] = ents
        row["review"] = build_review(spec, ents)
        rebuilt.append(row)

    doc["existing_annotations"] = rebuilt
    doc["description"] = DESCRIPTION
    doc["status"] = "COMPLETE"

    # --- synthesis ----------------------------------------------------------------------
    def core(cf: dict) -> dict:
        out = {"description": " ".join(cf["description"].split()),
               "supported_by": supported(cf["supported_by"]),
               "molecular_function": cf["molecular_function"]}
        if cf.get("directly_involved_in"):
            out["directly_involved_in"] = cf["directly_involved_in"]
        if cf.get("locations"):
            out["locations"] = cf["locations"]
        return out

    doc["core_functions"] = [core(cf) for cf in CORE_FUNCTIONS]

    def gap(g: dict) -> dict:
        out = {"gap_statement": " ".join(g["gap_statement"].split()),
               "boundary": " ".join(g["boundary"].split()),
               "gap_kind": g["gap_kind"],
               "dark_aspect": g["dark_aspect"],
               "status": g["status"],
               "significance": " ".join(g["significance"].split()),
               "resolution": " ".join(g["resolution"].split()),
               "provenance": supported(g["provenance"])}
        return out

    doc["knowledge_gaps"] = [gap(g) for g in KNOWLEDGE_GAPS]
    doc["proposed_new_terms"] = [
        {"proposed_name": t["proposed_name"],
         "proposed_definition": " ".join(t["proposed_definition"].split()),
         "justification": " ".join(t["justification"].split()),
         "proposed_parent": t["proposed_parent"],
         "supported_by": supported(t["supported_by"])}
        for t in PROPOSED_NEW_TERMS
    ]
    doc["suggested_questions"] = [{"question": " ".join(q["question"].split())}
                                  for q in SUGGESTED_QUESTIONS]
    doc["suggested_experiments"] = [
        {k: " ".join(v.split()) for k, v in e.items()} for e in SUGGESTED_EXPERIMENTS
    ]

    # --- references: every id used anywhere in the BUILT document -----------------------
    # Collected after the synthesis blocks are constructed, so that a reference cited only
    # in a knowledge gap, a proposed term or a core function cannot be dropped.
    cited: set[str] = set()

    def collect(node):
        if isinstance(node, dict):
            if "reference_id" in node:
                cited.add(node["reference_id"])
            for k, v in node.items():
                if k == "original_reference_id" and isinstance(v, str):
                    cited.add(v)
                if k == "additional_reference_ids":
                    cited.update(v)
                collect(v)
        elif isinstance(node, list):
            for v in node:
                collect(v)

    for key in ("existing_annotations", "core_functions", "knowledge_gaps",
                "proposed_new_terms"):
        collect(doc.get(key))

    seeded_titles = {r["id"]: r.get("title") for r in doc.get("references") or []}
    refs = []
    for rid in sorted(cited, key=lambda r: (r.split(":")[0], r)):
        entry: dict = {"id": rid}
        full_text_unavailable = None
        if rid.startswith("PMID:"):
            meta = cached_meta(rid)
            entry["title"] = meta["title"]
            full_text_unavailable = not meta["full_text_available"]
        elif rid in LOCAL_TITLES:
            entry["title"] = LOCAL_TITLES[rid]
        elif rid in seeded_titles and seeded_titles[rid]:
            entry["title"] = " ".join(str(seeded_titles[rid]).split())
        else:
            raise KeyError(f"no title available for reference {rid}")
        rr = REFERENCE_REVIEWS.get(rid)
        if rr is None:
            raise KeyError(f"no reference_review for {rid}")
        if full_text_unavailable:
            entry["full_text_unavailable"] = True
        entry["reference_review"] = {
            "relevance": rr["relevance"],
            "correctness": rr["correctness"],
            "review_notes": " ".join(rr["review_notes"].split()),
        }
        refs.append(entry)
    doc["references"] = refs
    unused_rr = set(REFERENCE_REVIEWS) - cited
    if unused_rr:
        raise KeyError(f"reference_review written for uncited references: {sorted(unused_rr)}")

    order = ["id", "gene_symbol", "product_type", "status", "taxon", "description",
             "references", "existing_annotations", "core_functions", "proposed_new_terms",
             "knowledge_gaps", "suggested_questions", "suggested_experiments"]
    ordered = {k: doc[k] for k in order if k in doc}
    ordered.update({k: v for k, v in doc.items() if k not in ordered})

    text = yaml.dump(ordered, sort_keys=False, width=98, allow_unicode=True, default_flow_style=False)
    if "--check" in sys.argv:
        if text != REVIEW.read_text():
            print("APLN-ai-review.yaml differs from what build_review.py would write")
            return 1
        print("APLN-ai-review.yaml is up to date")
        return 0
    REVIEW.write_text(text)
    n_prop = sum(1 for a in rebuilt if "propagation_review" in a["review"])
    actions: dict[str, int] = {}
    for a in rebuilt:
        actions[a["review"]["action"]] = actions.get(a["review"]["action"], 0) + 1
    print(f"wrote {REVIEW.relative_to(REPO)}")
    print(f"  annotations        : {len(rebuilt)} ({len(seeded)} from GOA + {len(NEW_ROWS)} NEW)")
    print(f"  actions            : {dict(sorted(actions.items()))}")
    print(f"  propagation_review : {n_prop}")
    print(f"  references         : {len(refs)} (all with reference_review)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
