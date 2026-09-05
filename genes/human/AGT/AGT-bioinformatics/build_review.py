"""Generate `AGT-ai-review.yaml` from the GOA file plus `AGT_decisions.py`.

The point of generating rather than hand-writing is fidelity of the mechanical
fields. `supporting_entities` is copied from the GOA WITH/FROM column, and
`propagation_review.source_entities` is built from that same list, so neither can
drift from GOA the way hand-maintained copies do. All prose comes from
`AGT_decisions.py`.

Run: uv run python build_review.py
Then: uv run python check_goa_reconciliation.py
"""

from __future__ import annotations

import csv
from pathlib import Path

import yaml

import AGT_decisions as D

HERE = Path(__file__).parent
GOA = HERE.parent / "AGT-goa.tsv"
OUT = HERE.parent / "AGT-ai-review.yaml"
RESOLVED = HERE / "withfrom_resolved.tsv"

REACTOME_ROWS = range(21, 48)
Y2H_ROWS = range(11, 21)


def reactome_title(rid: str) -> str:
    md = HERE.parent.parent.parent.parent / "reactome" / f"{rid}.md"
    if not md.exists():
        raise SystemExit(f"no cached Reactome entry for {rid}")
    text = md.read_text()
    chunk = text.split("display_name: ", 1)[1]
    for stop in ("\nspecies:", "\nsummary:", "\nstable_id:"):
        if stop in chunk:
            chunk = chunk.split(stop, 1)[0]
    return " ".join(chunk.split())


def full_text_missing(pmid_ref: str) -> bool:
    """True only when the cached publication explicitly says full text is absent."""
    f = HERE.parent.parent.parent.parent / "publications" / f"PMID_{pmid_ref.split(':', 1)[1]}.md"
    if not f.exists():
        raise SystemExit(f"no cached publication for {pmid_ref}")
    for line in f.read_text().splitlines():
        if line.startswith("full_text_available:"):
            return line.split(":", 1)[1].strip().lower() == "false"
    raise SystemExit(f"{pmid_ref} cache has no full_text_available field")


def build_references() -> list[dict]:
    out = []
    for r in D.REFERENCES:
        ref: dict = {"id": r["id"]}
        ref["title"] = r.get("title") or reactome_title(r["id"].split(":", 1)[1])
        if r["id"].startswith("PMID:") and full_text_missing(r["id"]):
            ref["full_text_unavailable"] = True
        if r.get("review"):
            rv = r["review"]
            ref["reference_review"] = {
                "relevance": rv["relevance"],
                "correctness": rv["correctness"],
                "review_notes": rv["notes"],
            }
        elif r["id"].startswith("Reactome:"):
            # All 27 Reactome references support the same single claim - that AGT and its
            # peptides act extracellularly - so their assessment differs only in which
            # reaction is named. Generated so each names its own reaction rather than
            # carrying 27 copies of identical prose.
            ref["reference_review"] = {
                "relevance": "LOW",
                "correctness": "VERIFIED",
                "review_notes": (
                    f"Correctly cited Reactome reaction, \"{ref['title']}\". It supports only "
                    "the extracellular localisation annotation drawn from it, which is right. "
                    "One of 27 such references on this gene, together producing 27 identical "
                    "GO:0005576 rows - a quarter of the entire GOA record expressing one "
                    "claim once per reaction. Worth noting that Reactome names its "
                    "participants by peptide span (AGT(25-32), AGT(25-31) and so on), so it "
                    "distinguishes the precursor from its cleavage products where GO cannot."
                ),
            }
        out.append(ref)
    return out


def load_resolved() -> dict[str, dict[str, str]]:
    with RESOLVED.open() as fh:
        return {r["token"]: r for r in csv.DictReader(fh, delimiter="\t")}


def norm_entities(raw: str) -> list[str]:
    out: list[str] = []
    for tok in raw.split("|"):
        tok = tok.strip()
        if tok and tok not in out:
            out.append(tok)
    return out


def reactome_decision(row: dict[str, str]) -> dict:
    rid = row["REFERENCE"].split(":", 1)[1]
    md = HERE.parent.parent.parent.parent / "reactome" / f"{rid}.md"
    name = ""
    if md.exists():
        text = md.read_text()
        marker = "display_name: "
        if marker in text:
            chunk = text.split(marker, 1)[1]
            for stop in ("\nspecies:", "\nsummary:", "\nstable_id:"):
                if stop in chunk:
                    chunk = chunk.split(stop, 1)[0]
            name = " ".join(chunk.split())
    if not name:
        raise SystemExit(f"no display_name for {rid}; refusing to write a vague reason")
    return dict(
        summary=D.REACTOME_INTRO + f"{row['REFERENCE']}, \"{name}\".",
        action="ACCEPT",
        reason=D.REACTOME_REASON,
        supported_by=[D.Q_SECRETED, D.Q_LIVER],
    )


def y2h_decision(row: dict[str, str], resolved: dict[str, dict[str, str]]) -> dict:
    tok = norm_entities(row["WITH/FROM"])[0]
    r = resolved[tok]
    locs = r.get("protein", "")
    return dict(
        summary=(
            D.Y2H_INTRO
            + f"{tok} ({r['gene'] or 'no gene symbol'}, {locs}), which UniProt places "
            f"outside the secreted compartment AGT occupies. No functional consequence of "
            f"this pairing has been reported for either protein."
        ),
        action="MARK_AS_OVER_ANNOTATED",
        reason=D.Y2H_REASON,
        supported_by=[D.Q_Y2H, D.Q_Y2H_COMPART, D.Q_SECRETED],
    )


def source_entities(tokens: list[str], prop: dict, resolved: dict[str, dict[str, str]]) -> list[dict]:
    """One PropagationSource per WITH/FROM token, in GOA order, built from GOA."""
    status = prop.get("status", {})
    default = prop.get("default")
    out = []
    for tok in tokens:
        r = resolved.get(tok, {})
        label = r.get("gene") or r.get("protein") or ""
        organism = r.get("organism", "")
        if tok in status:
            st, comment = status[tok]
        elif default is not None:
            st, template = default
            merops = r.get("merops", "")
            merops_phrase = (
                f"MEROPS {merops}" if merops
                else "no MEROPS cross-reference on its own UniProt entry, though its human "
                     "orthologue is MEROPS-classified as an inhibitor"
            )
            comment = template.format(
                gene=label or tok,
                organism=organism or "organism not resolved",
                protein=r.get("protein", ""),
                merops_phrase=merops_phrase,
            )
        else:
            raise SystemExit(f"no source_status for WITH/FROM token {tok}")
        entry = {"source_id": tok}
        if label:
            entry["source_label"] = f"{label} ({organism})" if organism else label
        entry["source_status"] = st
        entry["comment"] = comment
        out.append(entry)
    return out


def build_entry(row: dict[str, str], dec: dict, resolved: dict[str, dict[str, str]]) -> dict:
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
        if tokens:
            pr["source_entities"] = source_entities(tokens, prop, resolved)
        if prop.get("residue_claims"):
            pr["residue_claims"] = prop["residue_claims"]
        if prop.get("residue_claims_not_applicable"):
            pr["residue_claims_not_applicable"] = prop["residue_claims_not_applicable"]
        review["propagation_review"] = pr
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
    resolved = load_resolved()

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
        if i in D.DECISIONS:
            dec = D.DECISIONS[i]
        elif i in REACTOME_ROWS:
            dec = reactome_decision(row)
        elif i in Y2H_ROWS:
            dec = y2h_decision(row, resolved)
        else:
            raise SystemExit(f"no decision for GOA row {i}: {key}")
        entries.append(build_entry(row, dec, resolved))

    for n in D.NEW_ROWS:
        entries.append(
            {
                "term": {"id": n["term"][0], "label": n["term"][1]},
                "evidence_type": n["evidence_type"],
                "original_reference_id": n["reference"],
                "qualifier": n["qualifier"],
                "review": {
                    "summary": n["summary"],
                    "action": "NEW",
                    "reason": n["reason"],
                    "supported_by": [
                        {"reference_id": r, "supporting_text": t} for r, t in n["supported_by"]
                    ],
                },
            }
        )

    doc = {
        "id": "P01019",
        "gene_symbol": "AGT",
        "product_type": "PROTEIN",
        "status": "COMPLETE",
        "taxon": {"id": "NCBITaxon:9606", "label": "Homo sapiens"},
        "description": D.DESCRIPTION,
        "references": build_references(),
        "existing_annotations": entries,
        "core_functions": D.CORE_FUNCTIONS,
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
    print(f"wrote {OUT} with {len(entries)} entries "
          f"({len(D.NEW_ROWS)} NEW) from {len(rows)} GOA rows")


if __name__ == "__main__":
    main()
