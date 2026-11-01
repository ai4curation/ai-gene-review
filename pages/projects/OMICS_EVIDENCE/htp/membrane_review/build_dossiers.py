"""Build review dossiers for HTP-family `membrane` rows of proteins with no anchor feature.

This script decides nothing. It selects candidate rows and gathers the material a
reviewer needs to judge each one by hand; the decisions live in decisions.yaml, written
by a reviewer who has read the dossier (and, where it matters, the cited papers).

Candidates: existing_annotations rows with evidence_type HDA or HTP, not negated, term
GO:0016020 membrane, for a gene whose UniProt flat file has no structured membrane-anchor
feature (FT TRANSMEM / INTRAMEM / LIPID). An anchor feature makes `membrane` true by
construction, so those rows are not candidates; everything else needs a judgement.

Each dossier carries:
  * the row: index, reference (+ cached title), current action, summary and reason
  * UniProt: accession, SUBCELLULAR LOCATION text and FUNCTION text (verbatim, trimmed)
  * leads: the gene's other location (C) annotations from its *-goa.tsv, excluding
    high-throughput codes, each with code and reference; rows to GO:0016020 or an
    is_a/part_of descendant are flagged `membrane_family: true`. Leads are pointers to
    evidence to check, not evidence in themselves.

Usage:  python3 projects/OMICS_EVIDENCE/htp/membrane_review/build_dossiers.py
Writes: projects/OMICS_EVIDENCE/htp/membrane_review/dossiers.yaml
"""

from __future__ import annotations

import csv
import glob
import os
import re
import sys

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))
sys.path.insert(0, os.path.dirname(HERE))
from apply_dispositions import (  # noqa: E402
    CODES, HTP_FAMILY, LOADER, MEMBRANE, has_anchor_feature, membrane_closure,
)

OUT = os.path.join(HERE, "dossiers.yaml")


def cc_block(text: str, topic: str, limit: int) -> str:
    """Verbatim text of one UniProt CC topic (joined lines), trimmed to `limit` chars."""
    out, inside = [], False
    for line in text.split("\n"):
        if line.startswith("CC   -!- "):
            inside = line.startswith(f"CC   -!- {topic}:")
            if inside:
                out.append(line[len(f"CC   -!- {topic}:"):].strip())
        elif inside and line.startswith("CC       "):
            out.append(line[9:].strip())
        else:
            inside = False
    s = " ".join(out)
    return s[:limit] + (" ..." if len(s) > limit else "")


def pub_title(ref: str | None) -> str:
    if not ref or not ref.startswith("PMID:"):
        return ""
    p = os.path.join(ROOT, "publications", f"PMID_{ref[5:]}.md")
    if not os.path.exists(p):
        return ""
    m = re.search(r"^title:\s*(.+?)(?=^\w+:)", open(p).read(), re.M | re.S)
    return " ".join(m.group(1).split()).strip("'\"") if m else ""


def main() -> int:
    closure = membrane_closure()
    dossiers = []
    for path in sorted(glob.glob(os.path.join(ROOT, "genes", "*", "*", "*-ai-review.yaml"))):
        text = open(path).read()
        if MEMBRANE not in text:
            continue
        gdir = os.path.dirname(path)
        org, gene = path.split(os.sep)[-3], path.split(os.sep)[-2]
        uni = os.path.join(gdir, f"{gene}-uniprot.txt")
        goa = os.path.join(gdir, f"{gene}-goa.tsv")
        if not (os.path.exists(uni) and os.path.exists(goa)):
            continue
        utext = open(uni).read()
        if has_anchor_feature(utext):
            continue
        doc = yaml.load(text, Loader=LOADER)
        rows = [(i, a) for i, a in enumerate(doc.get("existing_annotations") or [])
                if a.get("evidence_type") in CODES and (a.get("term") or {}).get("id") == MEMBRANE
                and not a.get("negated")]
        if not rows:
            continue
        leads = {}
        with open(goa, newline="") as fh:
            for r in csv.DictReader(fh, delimiter="\t"):
                if r.get("GO ASPECT") != "cellular_component" or r.get("GO EVIDENCE CODE") in HTP_FAMILY:
                    continue
                key = (r["GO TERM"], r["GO NAME"], r["QUALIFIER"])
                leads.setdefault(key, set()).add(f'{r["GO EVIDENCE CODE"]} {r["REFERENCE"]}')
        lead_list = [{"term": f"{t} {n}", "qualifier": q, "evidence": sorted(ev),
                      **({"membrane_family": True} if t in closure else {})}
                     for (t, n, q), ev in sorted(leads.items())]
        acc = re.search(r"^AC   (\w+)", utext, re.M)
        for idx, a in rows:
            rv = a.get("review") or {}
            dossiers.append({
                "organism": org, "gene": gene, "accession": acc.group(1) if acc else "",
                "row_index": idx,
                "reference": a.get("original_reference_id"),
                "reference_title": pub_title(a.get("original_reference_id")),
                "evidence_type": a.get("evidence_type"),
                "current_action": rv.get("action"),
                "current_summary": " ".join(str(rv.get("summary") or "").split()),
                "current_reason": " ".join(str(rv.get("reason") or "").split()),
                "uniprot_subcellular_location": cc_block(utext, "SUBCELLULAR LOCATION", 700),
                "uniprot_function": cc_block(utext, "FUNCTION", 400),
                "leads": lead_list,
            })
    with open(OUT, "w") as fh:
        fh.write("# Generated by build_dossiers.py -- review material only; decisions are in decisions.yaml\n")
        yaml.safe_dump(dossiers, fh, sort_keys=False, width=120, allow_unicode=True)
    print(f"{len(dossiers)} dossiers for {len({(d['organism'], d['gene']) for d in dossiers})} genes -> {OUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
