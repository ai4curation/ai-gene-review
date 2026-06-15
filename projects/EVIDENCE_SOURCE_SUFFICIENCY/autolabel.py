#!/usr/bin/env python
"""Objective auto-labeling of the EVIDENCE_SOURCE_SUFFICIENCY instruments.

This fills the *objective* observation columns by locating each cited
supporting-text quote in the cached publication and the gene's deep-research
file. It answers a sharp, reproducible version of the hypotheses:

  "For an ACCEPT annotation, where does the curator's cited justifying quote
   actually live — the abstract, the full text, a review, the DR report?"

This is a **lower bound** on abstract-sufficiency: if a curator quoted a
Results sentence but the same fact is *also* stated in the abstract, the
snippet-location method records FULLTEXT, not ABSTRACT. Cells are left blank
(UNKNOWN) whenever the quote cannot be located in cached text — nothing is
guessed. The blind-ablation verdicts are deliberately NOT auto-filled; they are
the confirmation-bias control and require a genuine blinded pass.

Run:
    uv run python projects/EVIDENCE_SOURCE_SUFFICIENCY/autolabel.py
"""

from __future__ import annotations

import csv
import glob
import re
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import yaml

from ai_gene_review.etl.publication_type import classify_pubmed_publication_type
from ai_gene_review.tools.analyze_evidence_sources import load_type_cache

PUBS = Path("publications")
MIN_FRAG = 20  # min normalized chars for a fragment match
REVIEW_TYPES = {"REVIEW", "SYSTEMATIC_REVIEW", "META_ANALYSIS"}
SHALLOWNESS = ["TITLE", "ABSTRACT", "INTRODUCTION", "LITERATURE_REVIEW", "RESULTS",
               "DISCUSSION", "CONCLUSIONS", "OTHER"]
# Journal-name patterns that mark a review venue (PubMed PT under-tags reviews).
REVIEW_JOURNAL_RE = re.compile(
    r"nat(ure)? rev|trends in|annu(al)? rev|curr(ent)? opin|wiley interdiscip|"
    r"wires|physiol(ogical)? rev|pharmacol(ogical)? rev|chem(ical)? rev|"
    r"\breviews?\b",
    re.I,
)


def normalize(text: str) -> str:
    text = re.sub(r"\[[^\]]*\]", " ", text)  # drop [editorial] inserts
    text = text.lower()
    text = re.sub(r"[^a-z0-9 ]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def fragments(supporting_text: str) -> List[str]:
    raw = re.split(r"\.\.\.+|…", supporting_text or "")
    out = [normalize(f) for f in raw]
    return [f for f in out if len(f) >= MIN_FRAG] or [
        normalize(supporting_text or "")
    ]


def parse_pub(pmid: str) -> Optional[Tuple[str, str, dict]]:
    """Return (normalized_abstract, normalized_fulltext, frontmatter) for a PMID."""
    path = PUBS / f"PMID_{pmid}.md"
    if not path.exists():
        return None
    text = path.read_text()
    fm: dict = {}
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            fm = yaml.safe_load(parts[1]) or {}
            text = parts[2]
    abstract, fulltext = "", ""
    if "## Abstract" in text:
        after = text.split("## Abstract", 1)[1]
        if "## Full Text" in after:
            abstract, fulltext = after.split("## Full Text", 1)
        else:
            abstract = after
    elif "## Full Text" in text:
        fulltext = text.split("## Full Text", 1)[1]
    else:
        abstract = text
    return normalize(abstract), normalize(fulltext), fm


def locate(supporting_text: str, pmid: str) -> Tuple[str, dict]:
    """Classify where a quote lives: ABSTRACT / FULLTEXT / UNKNOWN."""
    parsed = parse_pub(pmid)
    if parsed is None:
        return "UNKNOWN", {"reason": "no cached pub"}
    abstract, fulltext, fm = parsed
    frags = fragments(supporting_text)
    in_abs = any(f in abstract for f in frags if f)
    in_full = any(f in fulltext for f in frags if f)
    if in_abs:
        return "ABSTRACT", {"journal": fm.get("journal", "")}
    if in_full:
        return "FULLTEXT", {"journal": fm.get("journal", "")}
    return "UNKNOWN", {
        "reason": "quote not found in cached abstract"
        + ("" if fulltext else " (abstract-only cache)"),
        "journal": fm.get("journal", ""),
    }


def is_review_ref(ref_id: str, type_cache: Dict[str, List[str]]) -> bool:
    if not ref_id.lower().startswith("pmid"):
        return False
    bare = ref_id.split(":", 1)[-1].strip()
    pts = type_cache.get(bare)
    if pts and classify_pubmed_publication_type(pts) in REVIEW_TYPES:
        return True
    parsed = parse_pub(bare)
    if parsed and REVIEW_JOURNAL_RE.search(parsed[2].get("journal", "") or ""):
        return True
    return False


def deep_research_text(gene_dir: Path) -> str:
    chunks = []
    for f in glob.glob(str(gene_dir / "*deep-research*.md")):
        chunks.append(normalize(Path(f).read_text()))
    return " ".join(chunks)


def main() -> None:
    sample = Path("projects/EVIDENCE_SOURCE_SUFFICIENCY/sample")
    type_cache = (
        load_type_cache() if Path("publications/publication_types.tsv").exists() else {}
    )

    # gene -> (yaml dict, gene_dir)
    gene_yaml: Dict[str, Tuple[dict, Path]] = {}
    for y in glob.glob("genes/human/*/*-ai-review.yaml"):
        d = yaml.safe_load(Path(y).read_text(encoding="utf-8"))
        if d:
            gene_yaml[d.get("gene_symbol")] = (d, Path(y).parent)

    # gene -> term_id -> list of supported_by snippets (across ACCEPT annotations)
    support_index: Dict[str, Dict[str, List[dict]]] = defaultdict(lambda: defaultdict(list))
    for gene, (d, _) in gene_yaml.items():
        for a in d.get("existing_annotations") or []:
            rv = a.get("review") or {}
            if rv.get("action") != "ACCEPT":
                continue
            tid = (a.get("term") or {}).get("id")
            support_index[gene][tid].extend(rv.get("supported_by") or [])

    dr_cache: Dict[str, str] = {}

    rows = list(
        csv.DictReader(
            (sample / "annotation_instrument.tsv").read_text(encoding="utf-8").splitlines(),
            delimiter="\t",
        )
    )
    filled = 0
    for r in rows:
        gene, tid = r["gene"], r["term_id"]
        snippets = support_index.get(gene, {}).get(tid, [])
        if not snippets:
            r["notes"] = "no cited supporting_text in review"
            r["labeler"] = "auto:cited_snippet_v1"
            continue

        if gene not in dr_cache:
            gdir = gene_yaml[gene][1] if gene in gene_yaml else Path(".")
            dr_cache[gene] = deep_research_text(gdir)
        dr_text = dr_cache[gene]

        sections: List[str] = []
        in_review = False
        in_dr = False
        justifying = ""
        for sb in snippets:
            st = sb.get("supporting_text") or ""
            if st and not justifying:
                justifying = re.sub(r"\s+", " ", st).strip()[:300]
            ref_id = sb.get("reference_id") or ""
            tagged = (sb.get("reference_section_type") or "").strip().upper()
            bare = ref_id.split(":", 1)[-1].strip() if ref_id.lower().startswith("pmid") else None
            if tagged in ("TITLE", "ABSTRACT"):
                sections.append(tagged)
            elif tagged:
                sections.append(tagged)
            elif bare:
                loc, _ = locate(st, bare)
                if loc == "ABSTRACT":
                    sections.append("ABSTRACT")
                elif loc == "FULLTEXT":
                    sections.append("OTHER")  # full-text, section unknown
            if is_review_ref(ref_id, type_cache):
                in_review = True
            for f in fragments(st):
                if f and dr_text and f in dr_text:
                    in_dr = True
                    break

        in_abstract = any(s in ("TITLE", "ABSTRACT") for s in sections)
        # shallowest known section
        sec_of_fact = ""
        for s in SHALLOWNESS:
            if s in sections:
                sec_of_fact = s
                break

        if in_abstract:
            tier = "ABSTRACT"
        elif in_review:
            tier = "REVIEW"
        elif in_dr:
            tier = "DEEP_RESEARCH"
        elif sections:  # located in full text only
            tier = "FULLTEXT_PRIMARY"
        else:
            tier = ""  # could not locate -> UNKNOWN, leave blank

        r["justifying_fact"] = justifying
        r["fact_in_abstract"] = "Y" if in_abstract else ("N" if sections else "")
        r["fact_in_review"] = "Y" if in_review else "N"
        r["fact_in_deep_research"] = "Y" if in_dr else "N"
        r["section_of_fact"] = sec_of_fact
        r["minimal_sufficient_tier"] = tier
        r["labeler"] = "auto:cited_snippet_v1"
        r["confidence"] = "located" if sections else "unlocated"
        if tier:
            filled += 1
        else:
            r["notes"] = "quote(s) not locatable in cached text"

    cols = rows[0].keys()
    with open(sample / "annotation_instrument.tsv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols, delimiter="\t", extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)

    # Reference instrument: fill publication_type_final + is_review_final.
    refs = list(
        csv.DictReader(
            (sample / "reference_instrument.tsv").read_text(encoding="utf-8").splitlines(),
            delimiter="\t",
        )
    )
    for rr in refs:
        ref_id = rr["reference_id"]
        auto = rr.get("publication_type_auto") or ""
        rr["publication_type_final"] = auto
        rr["is_review_final"] = "Y" if (auto in REVIEW_TYPES or is_review_ref(ref_id, type_cache)) else "N"
        rr["notes"] = "auto: PT + journal-name heuristic"
    with open(sample / "reference_instrument.tsv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=refs[0].keys(), delimiter="\t", extrasaction="ignore")
        w.writeheader()
        w.writerows(refs)

    print(f"annotation rows: {len(rows)}  tier-filled (locatable): {filled}")
    print(f"reference rows: {len(refs)}  marked review: {sum(1 for r in refs if r['is_review_final']=='Y')}")
    print("blind verdicts left empty by design (need a genuine blinded pass).")


if __name__ == "__main__":
    main()
