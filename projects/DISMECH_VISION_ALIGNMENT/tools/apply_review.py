"""Merge a reviewer's decisions file into a seeded gene review.

Usage, from the ai-gene-review root:

    uv run python projects/DISMECH_VISION_ALIGNMENT/tools/apply_review.py RHO decisions/RHO.yaml

The decisions file is YAML with these optional top-level keys:

    description: text
    status: COMPLETE | DRAFT
    rows:                      # keyed by row number as shown in the dossier (0-based)
      7:
        term: GO:0001750       # checked against the row, to catch a slipped index
        summary: ...
        action: ACCEPT
        reason: ...
        supported_by: [{reference_id: PMID:1, supporting_text: "verbatim"}]
        proposed_replacement_terms: [{id: GO:..., label: ...}]
        # any other Review slot (source_defects, propagation_review, nd_case, ...) is copied as is
    groups:                    # the same review applied to several rows
      - rows: [0, 1, 2]
        review: {summary: ..., action: ..., reason: ..., supported_by: [...]}
    new_annotations: [ {term: {id, label}, evidence_type, original_reference_id, review: {...}} ]
    references:                # keyed by reference id; adds or updates
      PMID:1: {findings: [...], reference_review: {...}}
      file:human/RHO/RHO-notes.md: {title: ..., reference_review: {...}}
    core_functions: [...]
    proposed_new_terms: [...]
    suggested_questions: [...]
    suggested_experiments: [...]
    knowledge_gaps: [...]

Row reviews replace the seeded PENDING review. The script refuses a row number that does
not exist, a `term` that does not match the row, and a row that appears twice. Titles of
PMID references that are not yet listed are read from the publications cache, never typed.
Running it again with a corrected decisions file overwrites the same rows.
"""
import os
import sys

import yaml

Loader = getattr(yaml, "CSafeLoader", yaml.SafeLoader)
ORDER = ["id", "gene_symbol", "product_type", "aliases", "taxon", "description", "existing_annotations",
         "references", "core_functions", "proposed_new_terms", "suggested_questions", "suggested_experiments",
         "knowledge_gaps", "status"]


def cached_title(ref):
    if ref.startswith("PMID:"):
        p = f"publications/PMID_{ref.split(':')[1]}.md"
        if os.path.exists(p):
            text = open(p).read()
            if text.startswith("---"):
                fm = yaml.load(text[3:text.index('\n---', 3)], Loader=Loader) or {}
                return fm.get("title")
    return None


def main():
    gene, dec_path = sys.argv[1], sys.argv[2]
    path = f"genes/human/{gene}/{gene}-ai-review.yaml"
    d = yaml.load(open(path), Loader=Loader)
    dec = yaml.load(open(dec_path), Loader=Loader) or {}
    rows = d["existing_annotations"]
    seeded = [r for r in rows if (r.get("review") or {}).get("action") != "NEW"]
    reviews, errors = {}, []
    for grp in dec.get("groups") or []:
        for i in grp["rows"]:
            if i in reviews:
                errors.append(f"row {i} is reviewed twice")
            reviews[i] = dict(grp["review"])
    for i, rv in (dec.get("rows") or {}).items():
        i = int(i)
        if i in reviews:
            errors.append(f"row {i} is reviewed twice")
        reviews[i] = dict(rv)
    for i, rv in sorted(reviews.items()):
        if not 0 <= i < len(seeded):
            errors.append(f"row {i} does not exist (the review has {len(seeded)} seeded rows)")
            continue
        term = rv.pop("term", None)
        if term and term != seeded[i]["term"]["id"]:
            errors.append(f"row {i} is {seeded[i]['term']['id']} {seeded[i]['term']['label']}, not {term}")
        if not rv.get("action") or not rv.get("summary"):
            errors.append(f"row {i} needs both summary and action")
    if errors:
        sys.exit("refused:\n  " + "\n  ".join(errors))
    for i, rv in reviews.items():
        seeded[i]["review"] = rv
    if "new_annotations" in dec:
        rows[:] = seeded + list(dec["new_annotations"] or [])
    refs = d.setdefault("references", [])
    by_id = {r["id"]: r for r in refs}
    for rid, upd in (dec.get("references") or {}).items():
        upd = dict(upd or {})
        if rid not in by_id:
            title = cached_title(rid) or upd.get("title")
            if not title:
                sys.exit(f"refused: reference {rid} is new and has no cached or given title")
            by_id[rid] = dict(id=rid, title=title)
            refs.append(by_id[rid])
        upd.pop("title", None) if cached_title(rid) else None
        by_id[rid].update(upd)
    cited = set()
    for r in rows:
        rv = r.get("review") or {}
        for s in rv.get("supported_by") or []:
            cited.add(s.get("reference_id"))
        cited.update(rv.get("additional_reference_ids") or [])
    for cf in dec.get("core_functions") or d.get("core_functions") or []:
        for s in cf.get("supported_by") or []:
            cited.add(s.get("reference_id"))
    for rid in sorted(c for c in cited if c and c not in by_id):
        title = cached_title(rid)
        if not title:
            sys.exit(f"refused: {rid} is cited but is not in references and has no cached title; add it under references")
        by_id[rid] = dict(id=rid, title=title)
        refs.append(by_id[rid])
    for key in ("description", "status", "core_functions", "proposed_new_terms", "suggested_questions",
                "suggested_experiments", "knowledge_gaps"):
        if key in dec:
            d[key] = dec[key]
    ordered = {k: d[k] for k in ORDER if k in d}
    ordered.update({k: v for k, v in d.items() if k not in ordered})
    with open(path, "w") as fh:
        yaml.safe_dump(ordered, fh, sort_keys=False, width=110, allow_unicode=True)
    pending = sum(1 for r in rows if (r.get("review") or {}).get("action") == "PENDING")
    print(f"{path}: {len(reviews)} rows written, {pending} still PENDING, {len(refs)} references, "
          f"{len(d.get('core_functions') or [])} core functions")


if __name__ == "__main__":
    main()
