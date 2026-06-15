#!/usr/bin/env python
"""Assemble restricted evidence bundles for the blind-ablation validation.

For each row in ``blind_ablation_assignments.tsv`` this builds the *only* text a
blinded reviewer is allowed to see for that bundle type:

* ABSTRACT_ONLY      - the abstract(s) of the primary paper(s) cited in support
                       of the (gene, term) ACCEPT annotation.
* REVIEW_ONLY        - the abstract(s) of review-type references for the gene.
* DEEP_RESEARCH_ONLY - paragraphs from the gene's deep-research file mentioning
                       the term.

Writes ``blind_bundles.json`` (a list of rows with ``bundle_text``). The reviewer
is NOT told the original action; that is the point of the blinding.
"""

from __future__ import annotations

import csv
import glob
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).parent))
import autolabel as al  # noqa: E402

SAMPLE = Path("projects/EVIDENCE_SOURCE_SUFFICIENCY/sample")
MAXLEN = 2200  # cap per-source text to keep bundles focused


def abstract_text(pmid: str) -> str:
    parsed = al.parse_pub(pmid)
    if not parsed:
        return ""
    path = al.PUBS / f"PMID_{pmid}.md"
    text = path.read_text()
    if "## Abstract" in text:
        seg = text.split("## Abstract", 1)[1]
        seg = seg.split("## Full Text", 1)[0]
        return re.sub(r"\s+", " ", seg).strip()[:MAXLEN]
    return ""


def main() -> None:
    type_cache = (
        al.load_type_cache()
        if Path("publications/publication_types.tsv").exists()
        else {}
    )

    # gene -> term -> supported_by snippets (ACCEPT only); gene -> (references, dir)
    support = defaultdict(lambda: defaultdict(list))
    gene_refs: dict = {}
    gene_dir: dict = {}
    for y in glob.glob("genes/human/*/*-ai-review.yaml"):
        d = yaml.safe_load(Path(y).read_text(encoding="utf-8"))
        if not d:
            continue
        g = d.get("gene_symbol")
        gene_refs[g] = [r.get("id") for r in (d.get("references") or []) if r.get("id")]
        gene_dir[g] = Path(y).parent
        for a in d.get("existing_annotations") or []:
            rv = a.get("review") or {}
            if rv.get("action") == "ACCEPT":
                support[g][(a.get("term") or {}).get("id")].extend(
                    rv.get("supported_by") or []
                )

    # term labels from the annotation instrument
    labels: dict = {}
    for r in csv.DictReader(
        (SAMPLE / "annotation_instrument.tsv").read_text(encoding="utf-8").splitlines(),
        delimiter="\t",
    ):
        labels[(r["gene"], r["term_id"])] = r.get("term_label", "")

    rows = list(
        csv.DictReader(
            (SAMPLE / "blind_ablation_assignments.tsv").read_text(encoding="utf-8").splitlines(),
            delimiter="\t",
        )
    )
    out = []
    for i, r in enumerate(rows):
        g, tid, bundle = r["gene"], r["term_id"], r["bundle"]
        snippets = support.get(g, {}).get(tid, [])
        cited_pmids = [
            (sb.get("reference_id") or "").split(":")[-1].strip()
            for sb in snippets
            if (sb.get("reference_id") or "").lower().startswith("pmid")
        ]
        label = labels.get((g, tid), "")
        bundle_text = ""

        if bundle == "ABSTRACT_ONLY":
            chunks = [t for p in dict.fromkeys(cited_pmids) if (t := abstract_text(p))]
            bundle_text = "\n\n---\n\n".join(chunks)
        elif bundle == "REVIEW_ONLY":
            review_pmids = [
                ref.split(":")[-1].strip()
                for ref in gene_refs.get(g, [])
                if ref.lower().startswith("pmid") and al.is_review_ref(ref, type_cache)
            ]
            chunks = [t for p in dict.fromkeys(review_pmids) if (t := abstract_text(p))]
            bundle_text = "\n\n---\n\n".join(chunks)
        elif bundle == "DEEP_RESEARCH_ONLY":
            dr = " ".join(
                Path(f).read_text()
                for f in glob.glob(str(gene_dir.get(g, Path(".")) / "*deep-research*.md"))
            )
            if dr:
                # paragraphs mentioning a keyword from the term label
                kws = [w for w in re.findall(r"[a-zA-Z]{5,}", label.lower())]
                paras = re.split(r"\n\s*\n", dr)
                hits = [
                    re.sub(r"\s+", " ", p).strip()
                    for p in paras
                    if any(k in p.lower() for k in kws)
                ]
                bundle_text = "\n\n".join(hits)[:MAXLEN]

        out.append(
            {
                "idx": i,
                "gene": g,
                "term_id": tid,
                "term_label": label,
                "aspect": r["aspect"],
                "bundle": bundle,
                "has_evidence": bool(bundle_text.strip()),
                "bundle_text": bundle_text.strip(),
            }
        )

    (SAMPLE / "blind_bundles.json").write_text(json.dumps(out, indent=1), encoding="utf-8")
    empty = sum(1 for o in out if not o["has_evidence"])
    by = defaultdict(lambda: [0, 0])
    for o in out:
        by[o["bundle"]][0] += 1
        by[o["bundle"]][1] += 1 if o["has_evidence"] else 0
    print(f"wrote {len(out)} bundles; {empty} have NO evidence text")
    for b, (n, e) in sorted(by.items()):
        print(f"  {b}: {e}/{n} have evidence")


if __name__ == "__main__":
    main()
