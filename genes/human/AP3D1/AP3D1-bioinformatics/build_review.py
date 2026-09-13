"""Write the review blocks of AP3D1-ai-review.yaml from AP3D1_decisions.py.

Deliberately mechanical. The script only ever writes:

* each existing annotation's ``review`` block (summary/action/reason/quotes and,
  for propagated rows, ``propagation_review``);
* the top-level synthesis fields.

It never touches ``term``, ``evidence_type``, ``original_reference_id``,
``qualifier`` or ``supporting_entities`` on a seeded row, and it builds every
``propagation_review.source_entities`` list *from that row's own*
``supporting_entities`` -- a decision may attach a status and a comment to a
source id, but may not introduce one. A decision naming a source the row does
not carry is a hard error, which is the failure mode that hand-typed source
lists produce.

Idempotent: re-running after an edit re-applies the decisions in place.

    uv run python build_review.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import yaml

import AP3D1_decisions as D
import AP3D1_synthesis as S

HERE = Path(__file__).parent
REVIEW = HERE.parent / "AP3D1-ai-review.yaml"
PUBS = HERE.parents[3] / "publications"

STATUSES = {
    "SUPPORTS_TRANSFER", "SUPPORTS_SOURCE_BUT_NOT_TARGET", "SOURCE_BAD",
    "SOURCE_STALE_OR_MISSING", "SOURCE_WEAK_OR_INFERRED", "CIRCULAR_OR_REDUNDANT",
    "NOT_RELEVANT", "UNRESOLVED",
}
ACTIONS = {
    "ACCEPT", "KEEP_AS_NON_CORE", "REMOVE", "MODIFY", "MARK_AS_OVER_ANNOTATED",
    "UNDECIDED", "NEW",
}


def supported(pairs):
    return [{"reference_id": r, "supporting_text": t} for r, t in pairs]


def cache_title(pmid: str) -> tuple[str, bool]:
    """Read a publication title and full-text flag out of the cached markdown.

    Titles are never typed into the decision tables: the pre-write hook blocks a
    title that does not match the fetched record, and reading it here removes any
    chance of writing one from memory.
    """
    path = PUBS / f"PMID_{pmid.split(':', 1)[1]}.md"
    if not path.exists():
        sys.exit(f"{pmid}: no cached publication at {path}")
    text = path.read_text()
    front = text.split("---", 2)[1]
    meta = yaml.safe_load(front)
    title = str(meta["title"]).strip()
    return title, bool(meta.get("full_text_available"))


def collect_cited(doc) -> set[str]:
    found: set[str] = set()

    def walk(node):
        if isinstance(node, dict):
            for k, v in node.items():
                if k in {"reference_id", "original_reference_id"} and isinstance(v, str):
                    found.add(v)
                if k == "additional_reference_ids" and isinstance(v, list):
                    found.update(v)
                walk(v)
        elif isinstance(node, list):
            for v in node:
                walk(v)

    walk(doc)
    return found


def build_references(doc) -> list[dict]:
    """references[] = every id cited anywhere, plus the affinage record.

    GO_REF titles are carried over from the seeded file (they come from the
    pipeline); PMID titles are read from the publication cache; file: titles are
    supplied here because there is no record to read.
    """
    seeded = {r["id"]: r for r in doc.get("references", [])}
    file_titles = {
        "file:human/AP3D1/AP3D1-uniprot.txt": "UniProt entry O14617 (AP3D1_HUMAN)",
        "file:human/AP3D1/AP3D1-bioinformatics/RESULTS.md": "AP3D1 bioinformatics: delta-adaptin interface conservation and GOA reconciliation",
        "file:human/AP3D1/AP3D1-deep-research-affinage.md": "Affinage mechanistic annotation for AP3D1 (human)",
    }
    ids = collect_cited(doc) | {"file:human/AP3D1/AP3D1-deep-research-affinage.md"}
    refs = []
    for rid in sorted(ids):
        if rid.startswith("PMID:"):
            title, has_full = cache_title(rid)
            entry = {"id": rid, "title": title}
            if not has_full:
                entry["full_text_unavailable"] = True
        elif rid.startswith("file:"):
            entry = {"id": rid, "title": file_titles[rid]}
        else:
            if rid not in seeded:
                sys.exit(f"{rid}: no seeded title and not a PMID or file reference")
            entry = {"id": rid, "title": seeded[rid]["title"]}
        rr = S.REFERENCE_REVIEWS.get(rid)
        if rr is None:
            sys.exit(f"{rid}: no reference_review")
        entry["reference_review"] = {
            "relevance": rr[0], "correctness": rr[1], "review_notes": rr[2],
        }
        refs.append(entry)
    unused = sorted(set(S.REFERENCE_REVIEWS) - ids)
    if unused:
        sys.exit(f"reference_review supplied for ids that are not referenced: {unused}")
    return refs


def term(pair):
    return {"id": pair[0], "label": pair[1]}


def build_core_functions() -> list[dict]:
    out = []
    for cf in S.CORE_FUNCTIONS:
        entry = {"description": cf["description"]}
        if cf.get("molecular_function"):
            entry["molecular_function"] = term(cf["molecular_function"])
        if cf.get("contributes_to_molecular_function"):
            entry["contributes_to_molecular_function"] = term(cf["contributes_to_molecular_function"])
        if cf.get("directly_involved_in"):
            entry["directly_involved_in"] = [term(t) for t in cf["directly_involved_in"]]
        if cf.get("locations"):
            entry["locations"] = [term(t) for t in cf["locations"]]
        if cf.get("in_complex"):
            entry["in_complex"] = term(cf["in_complex"])
        entry["supported_by"] = supported(cf["supported_by"])
        out.append(entry)
    return out


def build_knowledge_gaps() -> list[dict]:
    out = []
    for g in S.KNOWLEDGE_GAPS:
        entry = {k: v for k, v in g.items() if k != "provenance"}
        entry["provenance"] = supported(g["provenance"])
        out.append(entry)
    return out


def build_review_block(dec: dict, supporting_entities: list[str], where: str) -> dict:
    assert dec["action"] in ACTIONS, f"{where}: bad action {dec['action']}"
    review = {"summary": dec["summary"], "action": dec["action"], "reason": dec["reason"]}
    if dec.get("proposed_replacement_terms"):
        review["proposed_replacement_terms"] = [
            {"id": i, "label": l} for i, l in dec["proposed_replacement_terms"]
        ]
    if dec.get("additional_reference_ids"):
        review["additional_reference_ids"] = list(dec["additional_reference_ids"])
    review["supported_by"] = supported(dec["supported_by"])

    prop = dec.get("prop")
    if prop:
        block: dict = {"root_cause": prop["root_cause"]}
        if prop.get("failure_modes"):
            block["failure_modes"] = list(prop["failure_modes"])
        sources = prop.get("sources") or {}
        unknown = [s for s in sources if s not in supporting_entities]
        if unknown:
            sys.exit(f"{where}: source_entities not in supporting_entities: {unknown}")
        entries = []
        for sid in supporting_entities:          # order comes from the seeded row
            if sid not in sources:
                continue
            label, status, comment = sources[sid]
            assert status in STATUSES, f"{where}: bad source_status {status}"
            entries.append({
                "source_id": sid,
                "source_label": label,
                "source_status": status,
                "comment": comment,
            })
        if entries:
            block["source_entities"] = entries
        if prop.get("residue_claims"):
            block["residue_claims"] = prop["residue_claims"]
        if prop.get("residue_claims_not_applicable"):
            block["residue_claims_not_applicable"] = prop["residue_claims_not_applicable"]
        review["propagation_review"] = block
    return review


def main() -> None:
    doc = yaml.safe_load(REVIEW.read_text())
    anns = [a for a in doc["existing_annotations"] if a["review"].get("action") != "NEW"]
    if len(anns) != len(D.KEY):
        sys.exit(f"expected {len(D.KEY)} GOA-derived rows, found {len(anns)}")

    for i, a in enumerate(anns):
        want = D.KEY[i]
        got = (a["term"]["id"], a["evidence_type"], a["original_reference_id"])
        if got != want:
            sys.exit(f"row {i}: seeded order changed, expected {want}, found {got}")
        dec = D.DECISIONS.get(i)
        if dec is None:
            sys.exit(f"row {i} {got}: no decision")
        a["review"] = build_review_block(dec, a.get("supporting_entities") or [], f"row {i} {got}")

    new_rows = []
    for n in D.NEW_ROWS:
        row = {
            "term": {"id": n["term"][0], "label": n["term"][1]},
            "evidence_type": n["evidence_type"],
            "original_reference_id": n["original_reference_id"],
            "qualifier": n["qualifier"],
            "review": build_review_block(n, [], f"NEW {n['term'][0]}"),
        }
        new_rows.append(row)

    doc["existing_annotations"] = anns + new_rows
    doc["description"] = S.DESCRIPTION
    doc["core_functions"] = build_core_functions()
    doc["knowledge_gaps"] = build_knowledge_gaps()
    doc["suggested_questions"] = [dict(q) for q in S.SUGGESTED_QUESTIONS]
    doc["suggested_experiments"] = [dict(e) for e in S.SUGGESTED_EXPERIMENTS]
    doc["references"] = build_references(doc)
    doc["status"] = "COMPLETE"

    order = ["id", "gene_symbol", "product_type", "status", "taxon", "description",
             "alternative_products", "existing_annotations", "core_functions",
             "knowledge_gaps", "suggested_questions", "suggested_experiments", "references"]
    doc = {k: doc[k] for k in order if k in doc} | {k: v for k, v in doc.items() if k not in order}

    REVIEW.write_text(
        yaml.safe_dump(doc, sort_keys=False, allow_unicode=True, width=100, default_flow_style=False)
    )
    print(f"wrote {REVIEW}: {len(anns)} reviewed GOA rows + {len(new_rows)} NEW rows")


if __name__ == "__main__":
    main()
