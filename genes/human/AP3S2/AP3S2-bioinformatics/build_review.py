"""Generate `AP3S2-ai-review.yaml` from the GOA file plus `AP3S2_decisions.py`.

The point of generating rather than hand-writing is fidelity of the mechanical
fields. Term ids and labels, evidence codes, references and qualifiers are copied
from `AP3S2-goa.tsv`; `supporting_entities` is the `|`-split WITH/FROM column;
and `propagation_review.source_entities` is built from that same list, so neither
can drift from GOA the way hand-maintained copies do. Reference titles are read
out of the cached publication frontmatter rather than typed. All prose comes from
`AP3S2_decisions.py`.

Run: uv run python build_review.py
Then: uv run python check_goa_reconciliation.py

`alternative_products` is carried forward verbatim from the existing review file
(originally the fetch-gene seed), so regenerating never drops it.
"""

from __future__ import annotations

import csv
from pathlib import Path

import yaml

import AP3S2_decisions as D

HERE = Path(__file__).parent
REPO = HERE.parents[3]
GOA = HERE.parent / "AP3S2-goa.tsv"
OUT = HERE.parent / "AP3S2-ai-review.yaml"

PROPAGATION_CODES = {"IBA", "ISS", "ISO", "IEA", "IC"}


def norm_entities(raw: str) -> list[str]:
    out: list[str] = []
    for tok in raw.split("|"):
        tok = tok.strip()
        if tok and tok not in out:
            out.append(tok)
    return out


def cache_frontmatter(pmid_ref: str) -> dict:
    """Parse the YAML frontmatter of a cached publication."""
    path = REPO / "publications" / f"PMID_{pmid_ref.split(':', 1)[1]}.md"
    if not path.exists():
        raise SystemExit(f"no cached publication for {pmid_ref}")
    text = path.read_text()
    if not text.startswith("---"):
        raise SystemExit(f"{path} has no frontmatter")
    block = text.split("---", 2)[1]
    data = yaml.safe_load(block)
    if "title" not in data:
        raise SystemExit(f"{path} frontmatter has no title")
    return data


def seed_fields() -> tuple[list[dict], dict[str, str]]:
    """alternative_products and GO_REF titles, carried forward from the current file."""
    if not OUT.exists():
        raise SystemExit(f"{OUT} missing; run `just fetch-gene human AP3S2` first")
    doc = yaml.safe_load(OUT.read_text())
    alt = doc.get("alternative_products") or []
    goref = {r["id"]: r["title"] for r in doc.get("references") or []
             if r["id"].startswith("GO_REF:")}
    return alt, goref


def build_references(goref_titles: dict[str, str]) -> list[dict]:
    out = []
    for r in D.REFERENCES:
        rid = r["id"]
        ref: dict = {"id": rid}
        if rid.startswith("GO_REF:"):
            if rid not in goref_titles:
                raise SystemExit(f"no seeded title for {rid}")
            ref["title"] = goref_titles[rid]
        elif rid.startswith("PMID:"):
            fm = cache_frontmatter(rid)
            ref["title"] = fm["title"]
            if fm.get("full_text_available") is False:
                ref["full_text_unavailable"] = True
        elif rid == D.UNIPROT:
            ref["title"] = "UniProtKB entry P59780 (AP3S2_HUMAN), AP-3 complex subunit sigma-2"
        elif rid == D.BIOINF:
            ref["title"] = ("AP3S2 bioinformatics: dileucine pocket conservation, WITH/FROM "
                            "resolution and ARBA rule specificity")
        elif rid == D.AFFINAGE:
            ref["title"] = "Affinage mechanistic annotation for AP3S2 (human)"
        else:
            raise SystemExit(f"no title rule for reference {rid}")
        rv = r["review"]
        ref["reference_review"] = {
            "relevance": rv["relevance"],
            "correctness": rv["correctness"],
            "review_notes": rv["notes"],
        }
        out.append(ref)
    return out


def source_entities(tokens: list[str], prop: dict) -> list[dict]:
    """One PropagationSource per WITH/FROM token, in GOA order, built from GOA."""
    status = prop["status"]
    out = []
    for tok in tokens:
        if tok not in status:
            raise SystemExit(f"no source_status for WITH/FROM token {tok}")
        st, comment = status[tok]
        out.append({"source_id": tok, "source_status": st, "comment": comment})
    extra = set(status) - set(tokens)
    if extra:
        raise SystemExit(f"source_status given for tokens not in this row's WITH/FROM: {extra}")
    return out


def build_entry(row: dict[str, str], dec: dict) -> dict:
    tokens = norm_entities(row["WITH/FROM"])
    review: dict = {
        "summary": dec["summary"],
        "action": dec["action"],
        "reason": dec["reason"],
    }
    if dec.get("replace"):
        review["proposed_replacement_terms"] = [
            {"id": gid, "label": lbl} for gid, lbl in dec["replace"]
        ]
    if dec.get("prop"):
        prop = dec["prop"]
        pr: dict = {"root_cause": prop["root_cause"]}
        if prop.get("modes"):
            pr["failure_modes"] = list(prop["modes"])
        pr["source_entities"] = source_entities(tokens, prop)
        if prop.get("residue_claims"):
            pr["residue_claims"] = prop["residue_claims"]
        if prop.get("residue_claims_not_applicable"):
            pr["residue_claims_not_applicable"] = prop["residue_claims_not_applicable"]
        review["propagation_review"] = pr
    elif tokens and row["GO EVIDENCE CODE"] in PROPAGATION_CODES:
        raise SystemExit(
            f"row {row['GO TERM']} {row['GO EVIDENCE CODE']} {row['REFERENCE']} carries a "
            "WITH/FROM but no propagation_review")
    review["supported_by"] = [
        {"reference_id": ref, "supporting_text": txt} for ref, txt in dec["supported_by"]
    ]
    entry: dict = {
        "term": {"id": row["GO TERM"], "label": row["GO NAME"]},
        "evidence_type": row["GO EVIDENCE CODE"],
        "original_reference_id": row["REFERENCE"],
    }
    if row["QUALIFIER"]:
        entry["qualifier"] = row["QUALIFIER"]
    if tokens:
        entry["supporting_entities"] = tokens
    entry["review"] = review
    return entry


def main() -> None:
    with GOA.open() as fh:
        rows = list(csv.DictReader(fh, delimiter="\t"))
    alt_products, goref_titles = seed_fields()

    entries: list[dict] = []
    seen: set[tuple] = set()
    for i, row in enumerate(rows, start=1):
        key = (row["GO TERM"], row["GO EVIDENCE CODE"], row["REFERENCE"],
               row["QUALIFIER"], "|".join(norm_entities(row["WITH/FROM"])))
        if key in seen:
            print(f"  row {i}: exact duplicate of an earlier GOA row, collapsed ({key[0]} "
                  f"{key[1]} {key[2]})")
            continue
        seen.add(key)
        if i not in D.DECISIONS:
            raise SystemExit(f"no decision for GOA row {i}: {key}")
        entries.append(build_entry(row, D.DECISIONS[i]))

    existing_terms = {(e["term"]["id"]) for e in entries}
    for n in D.NEW_ROWS:
        if n["term"][0] in existing_terms:
            raise SystemExit(f"NEW row {n['term'][0]} duplicates a term already in GOA")
        new_entry = {
            "term": {"id": n["term"][0], "label": n["term"][1]},
            "evidence_type": n["evidence_type"],
            "original_reference_id": n["reference"],
            "qualifier": n["qualifier"],
        }
        # NEW rows have no GOA line, so their supporting_entities (when the evidence code
        # calls for one, e.g. the interactor of an IPI) come from the decisions module.
        if n.get("supporting_entities"):
            new_entry["supporting_entities"] = list(n["supporting_entities"])
        new_entry.update({
            "review": {
                "summary": n["summary"],
                "action": "NEW",
                "reason": n["reason"],
                "supported_by": [
                    {"reference_id": r, "supporting_text": t} for r, t in n["supported_by"]
                ],
            },
        })
        entries.append(new_entry)

    doc = {
        "id": "P59780",
        "gene_symbol": "AP3S2",
        "product_type": "PROTEIN",
        "status": "COMPLETE",
        "taxon": {"id": "NCBITaxon:9606", "label": "Homo sapiens"},
        "description": D.DESCRIPTION,
        "alternative_products": alt_products,
        "references": build_references(goref_titles),
        "existing_annotations": entries,
        "core_functions": D.CORE_FUNCTIONS,
        "proposed_new_terms": D.PROPOSED_NEW_TERMS,
        "knowledge_gaps": D.KNOWLEDGE_GAPS,
        "suggested_questions": D.SUGGESTED_QUESTIONS,
        "suggested_experiments": D.SUGGESTED_EXPERIMENTS,
    }

    class Dumper(yaml.SafeDumper):
        pass

    def str_presenter(dumper, data):
        if "\n" in data or len(data) > 90:
            return dumper.represent_scalar("tag:yaml.org,2002:str", data, style=">")
        return dumper.represent_scalar("tag:yaml.org,2002:str", data)

    Dumper.add_representer(str, str_presenter)
    Dumper.ignore_aliases = lambda *args: True

    OUT.write_text(yaml.dump(doc, Dumper=Dumper, sort_keys=False, width=92,
                             allow_unicode=True, default_flow_style=False))

    actions: dict[str, int] = {}
    for e in entries:
        a = e["review"]["action"]
        actions[a] = actions.get(a, 0) + 1
    n_prop = sum(1 for e in entries if e["review"].get("propagation_review"))
    n_src = sum(len(e["review"]["propagation_review"]["source_entities"])
                for e in entries if e["review"].get("propagation_review"))
    n_quotes = sum(len(e["review"]["supported_by"]) for e in entries)
    print(f"wrote {OUT.name}: {len(entries)} entries from {len(rows)} GOA rows "
          f"({len(D.NEW_ROWS)} NEW)")
    print(f"  actions: " + ", ".join(f"{k}={v}" for k, v in sorted(actions.items())))
    print(f"  propagation_review blocks: {n_prop}, source_entities: {n_src}")
    print(f"  supporting_text quotes on annotations: {n_quotes}")
    print(f"  references: {len(doc['references'])}, core_functions: "
          f"{len(doc['core_functions'])}, proposed_new_terms: "
          f"{len(doc['proposed_new_terms'])}, knowledge_gaps: {len(doc['knowledge_gaps'])}")


if __name__ == "__main__":
    main()
