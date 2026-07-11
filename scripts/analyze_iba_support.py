#!/usr/bin/env python3
"""Summary statistics on independent literature support for IBA annotations.

Scans every ``genes/*/*/*-ai-review.yaml`` for annotations whose ``evidence_type``
is ``IBA`` and asks: how many of them already carry *independent* literature
support (a real PMID/DOI in ``supported_by`` or ``additional_reference_ids``,
i.e. something other than the PANTHER GO_REF the IBA itself came from)?

For the IBAs that are supported, it then breaks the support down by the
*cheapest source that suffices*, using the cached publications in
``publications/``:

* abstract-only  -- the verbatim ``supporting_text`` is found inside the
  abstract of the cited paper (or the cached paper is abstract-only), so an
  abstract is enough to confirm the annotation.
* review article -- the cited paper is a review (PubMed publication type
  ``Review`` / cached ``publication_type: REVIEW``).
* full-text only -- supporting text only appears in the full text of a
  primary paper (review/abstract did not suffice).

Outputs a TSV of per-annotation detail plus a printed summary.
"""

from __future__ import annotations

import csv
import glob
import re
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
PUB_DIR = ROOT / "publications"


# --------------------------------------------------------------------------- #
# Publication cache index
# --------------------------------------------------------------------------- #
def _split_frontmatter(text: str):
    """Return (frontmatter_dict, body_text) for a cached publication markdown."""
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) == 3:
            try:
                fm = yaml.safe_load(parts[1]) or {}
            except yaml.YAMLError:
                fm = {}
            return (fm if isinstance(fm, dict) else {}), parts[2]
    return {}, text


def _abstract_section(body: str) -> str:
    """Extract the text under a '## Abstract' header (up to the next '## ')."""
    m = re.search(r"##\s*Abstract\s*(.*?)(?:\n##\s|\Z)", body, re.DOTALL | re.IGNORECASE)
    return m.group(1) if m else ""


def _normalize(s: str) -> str:
    """Collapse whitespace so verbatim-substring checks survive line wrapping."""
    return re.sub(r"\s+", " ", s or "").strip().lower()


def build_pub_index() -> dict:
    """Map normalized reference id -> publication metadata + searchable text.

    Keyed by both 'PMID:xxxx' and 'DOI:xxxx' style ids so review references
    can be looked up directly.
    """
    index: dict[str, dict] = {}
    for path in glob.glob(str(PUB_DIR / "*.md")):
        text = Path(path).read_text(encoding="utf-8", errors="replace")
        fm, body = _split_frontmatter(text)
        pub_types = [str(t) for t in (fm.get("pubmed_publication_types") or [])]
        is_review = (
            str(fm.get("publication_type", "")).upper() == "REVIEW"
            or any(t.strip().lower() == "review" for t in pub_types)
        )
        entry = {
            "full_text_available": fm.get("full_text_available"),
            "is_review": is_review,
            "has_pubtype": bool(fm.get("publication_type") or fm.get("pubmed_publication_types")),
            "abstract_norm": _normalize(_abstract_section(body)),
            "full_norm": _normalize(body),
        }
        keys = []
        if fm.get("pmid"):
            keys.append(f"PMID:{str(fm['pmid']).strip()}")
        if fm.get("doi"):
            keys.append(f"DOI:{str(fm['doi']).strip()}")
        # also key off filename (PMID_xxxx.md / DOI_xxxx.md)
        stem = Path(path).stem
        if stem.startswith("PMID_"):
            keys.append(f"PMID:{stem[5:]}")
        elif stem.startswith("DOI_"):
            keys.append("DOI:" + stem[4:].replace("_", "/"))
        for k in keys:
            index.setdefault(k, entry)
    return index


# --------------------------------------------------------------------------- #
# Reference classification
# --------------------------------------------------------------------------- #
def is_literature_ref(ref_id: str) -> bool:
    """True for a PMID/DOI literature citation (not GO_REF / file: / Reactome)."""
    if not ref_id:
        return False
    rid = ref_id.strip()
    if rid.startswith("PMID:") or rid.startswith("DOI:"):
        return True
    return False


def collect_support_refs(ann: dict):
    """Yield (reference_id, supporting_text) for every support entry on an annotation."""
    out = []
    for sb in ann.get("supported_by") or []:
        if isinstance(sb, dict) and sb.get("reference_id"):
            out.append((str(sb["reference_id"]).strip(), str(sb.get("supporting_text") or "")))
    review = ann.get("review") or {}
    if isinstance(review, dict):
        for sb in review.get("supported_by") or []:
            if isinstance(sb, dict) and sb.get("reference_id"):
                out.append((str(sb["reference_id"]).strip(), str(sb.get("supporting_text") or "")))
        for rid in review.get("additional_reference_ids") or []:
            out.append((str(rid).strip(), ""))
    return out


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #
def main():
    print("Indexing publications cache...", flush=True)
    pub_index = build_pub_index()
    print(f"  indexed {len(pub_index)} reference keys", flush=True)

    review_files = sorted(glob.glob(str(ROOT / "genes" / "*" / "*" / "*-ai-review.yaml")))
    print(f"Scanning {len(review_files)} review files...", flush=True)

    rows = []
    total_iba = 0
    supported = 0
    counts = Counter()

    for rf in review_files:
        try:
            data = yaml.safe_load(Path(rf).read_text(encoding="utf-8", errors="replace"))
        except yaml.YAMLError:
            continue
        if not isinstance(data, dict):
            continue
        gene = data.get("gene_symbol", "")
        rel = str(Path(rf).relative_to(ROOT))

        for ann in data.get("existing_annotations") or []:
            if not isinstance(ann, dict) or ann.get("evidence_type") != "IBA":
                continue
            total_iba += 1
            term = ann.get("term") or {}
            term_id = term.get("id", "") if isinstance(term, dict) else ""

            refs = collect_support_refs(ann)
            lit_refs = [(rid, txt) for rid, txt in refs if is_literature_ref(rid)]

            has_support = bool(lit_refs)
            # coverage bookkeeping
            for rid, _ in lit_refs:
                counts["lit_refs_cited"] += 1
                entry0 = pub_index.get(rid)
                if entry0 is None:
                    counts["lit_refs_uncached"] += 1
                elif entry0.get("has_pubtype"):
                    counts["lit_refs_with_pubtype"] += 1
            abstract_ok = False
            review_ok = False
            fulltext_ok = False
            for rid, txt in lit_refs:
                entry = pub_index.get(rid)
                if not entry:
                    # cited but not in cache -> can't classify source depth
                    continue
                tnorm = _normalize(txt)
                if entry["is_review"]:
                    review_ok = True
                if entry["full_text_available"] is False:
                    # cache is abstract-only; any support came from the abstract
                    abstract_ok = True
                elif tnorm and entry["abstract_norm"] and tnorm in entry["abstract_norm"]:
                    abstract_ok = True
                elif tnorm and entry["full_norm"] and tnorm in entry["full_norm"]:
                    fulltext_ok = True

            if has_support:
                supported += 1
                # cheapest sufficient source
                if abstract_ok:
                    tier = "abstract"
                elif review_ok:
                    tier = "review_fulltext"
                elif fulltext_ok:
                    tier = "fulltext_primary"
                else:
                    tier = "support_not_localized"
                counts[tier] += 1
                if review_ok:
                    counts["any_review_source"] += 1
                if abstract_ok:
                    counts["any_abstract_source"] += 1
                if any((pub_index.get(rid) or {}).get("has_pubtype") for rid, _ in lit_refs):
                    counts["review_detectable"] += 1
            else:
                tier = "unsupported"

            rows.append({
                "file": rel,
                "gene": gene,
                "term_id": term_id,
                "n_lit_refs": len(lit_refs),
                "lit_refs": ";".join(rid for rid, _ in lit_refs),
                "has_independent_support": has_support,
                "abstract_ok": abstract_ok,
                "review_ok": review_ok,
                "fulltext_ok": fulltext_ok,
                "tier": tier,
            })

    out_tsv = ROOT / "reports" / "iba_support_stats.tsv"
    out_tsv.parent.mkdir(exist_ok=True)
    with open(out_tsv, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()), delimiter="\t")
        w.writeheader()
        w.writerows(rows)

    # ---- summary ---- #
    def pct(n, d):
        return f"{100*n/d:.1f}%" if d else "n/a"
    print("\n" + "=" * 60)
    print("IBA INDEPENDENT-SUPPORT SUMMARY")
    print("=" * 60)
    print(f"Total IBA annotations:                 {total_iba}")
    print(f"  with independent literature support: {supported}  ({pct(supported, total_iba)})")
    print(f"  without:                             {total_iba - supported}  ({pct(total_iba-supported, total_iba)})")
    print("\nOf the supported IBAs, cheapest sufficient source:")
    print(f"  abstract suffices:        {counts['abstract']}  ({pct(counts['abstract'], supported)})")
    print(f"  review (full text):       {counts['review_fulltext']}  ({pct(counts['review_fulltext'], supported)})")
    print(f"  primary full-text only:   {counts['fulltext_primary']}  ({pct(counts['fulltext_primary'], supported)})")
    print(f"  support not localized:    {counts['support_not_localized']}  ({pct(counts['support_not_localized'], supported)})")
    print("\nNon-exclusive source availability among supported IBAs:")
    print(f"  any abstract source:      {counts['any_abstract_source']}  ({pct(counts['any_abstract_source'], supported)})")
    print(f"  any review source:        {counts['any_review_source']}  ({pct(counts['any_review_source'], supported)})")
    print("\nReview-classification CEILING (metadata coverage):")
    print(f"  IBA-support literature refs cited:   {counts['lit_refs_cited']}")
    print(f"    not in publications cache:         {counts['lit_refs_uncached']}  ({pct(counts['lit_refs_uncached'], counts['lit_refs_cited'])})")
    print(f"    cached WITH pub-type metadata:     {counts['lit_refs_with_pubtype']}  ({pct(counts['lit_refs_with_pubtype'], counts['lit_refs_cited'])})")
    print(f"  supported IBAs citing >=1 paper with pub-type metadata: {counts['review_detectable']}  ({pct(counts['review_detectable'], supported)})")
    print("  -> review-vs-primary cannot be answered until pub-type metadata is backfilled.")
    print(f"\nPer-annotation detail written to: {out_tsv.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
