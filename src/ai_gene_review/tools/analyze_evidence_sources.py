"""Analyze which evidence *sources* support GO annotation review decisions.

This tool was built to explore four hypotheses about GO annotation curation:

  (a) Published *review* papers are usually sufficient (and carry phylogenetic
      reasoning).
  (b) *Abstracts alone* are often sufficient.
  (c) *Deep research* reports have sufficient depth.
  (d) The *background/introduction* and *discussion/conclusions* sections are a
      rich vein of supporting text.

It joins two things already captured in the gene-review YAMLs:

  * ``reference_section_type`` on every supporting-text snippet (which manuscript
    section the quote came from), and
  * ``publication_type`` of the cited reference (review vs primary vs deep
    research vs database), inferred from PubMed PT metadata (cached in a TSV).

and cross-tabulates them against the curator's ``review.action`` (ACCEPT,
MODIFY, REMOVE, ...).

Run via the CLI:  ``ai-gene-review analyze-evidence-sources --organism human``
"""

from __future__ import annotations

from pathlib import Path
from typing import Dict, List, Optional

import pandas as pd
import yaml

from ai_gene_review.etl.publication_type import (
    classify_pubmed_publication_type,
    classify_reference_id,
    fetch_pubmed_publication_types,
)

DEFAULT_TYPE_CACHE = Path("publications/publication_types.tsv")

# Sections treated as "shallow" (available without full text) vs "deep".
SHALLOW_SECTIONS = {"TITLE", "ABSTRACT", "KEYWORDS"}
# Sections that are the "background + conclusions" vein in hypothesis (d).
NARRATIVE_SECTIONS = {
    "INTRODUCTION",
    "LITERATURE_REVIEW",
    "DISCUSSION",
    "CONCLUSIONS",
}


# --------------------------------------------------------------------------- #
# PMID -> publication-type cache
# --------------------------------------------------------------------------- #
def load_type_cache(cache_path: Path = DEFAULT_TYPE_CACHE) -> Dict[str, List[str]]:
    """Load a PMID -> raw PubMed PT list cache from a TSV file.

    The TSV has columns ``pmid<TAB>publication_type<TAB>raw_pts`` where
    ``raw_pts`` is a ``|``-joined list. Only ``pmid`` and ``raw_pts`` are read
    back (the classification is recomputed to stay in sync with the code).
    """
    cache: Dict[str, List[str]] = {}
    if not cache_path.exists():
        return cache
    for line in cache_path.read_text().splitlines():
        if not line.strip() or line.startswith("pmid\t"):
            continue
        parts = line.split("\t")
        pmid = parts[0].strip()
        raw = parts[2] if len(parts) > 2 else ""
        cache[pmid] = [p for p in raw.split("|") if p] if raw else []
    return cache


def save_type_cache(
    cache: Dict[str, List[str]], cache_path: Path = DEFAULT_TYPE_CACHE
) -> None:
    """Write the PMID -> PT cache to a TSV (sorted by PMID for stable diffs)."""
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    lines = ["pmid\tpublication_type\traw_pts"]
    for pmid in sorted(cache, key=lambda x: (len(x), x)):
        pts = cache[pmid]
        lines.append(
            f"{pmid}\t{classify_pubmed_publication_type(pts)}\t{'|'.join(pts)}"
        )
    cache_path.write_text("\n".join(lines) + "\n")


def ensure_types_cached(
    pmids: List[str],
    cache_path: Path = DEFAULT_TYPE_CACHE,
    refresh: bool = False,
    network: bool = True,
) -> Dict[str, List[str]]:
    """Return a PMID -> PT-list cache, fetching any missing PMIDs from PubMed.

    Args:
        pmids: bare PMIDs needed.
        cache_path: TSV cache location.
        refresh: if True, re-fetch all PMIDs even if cached.
        network: if False, never hit the network (missing PMIDs stay missing).
    """
    cache = {} if refresh else load_type_cache(cache_path)
    needed = sorted({p for p in pmids if refresh or p not in cache})
    if needed and network:
        print(f"Fetching PubMed publication types for {len(needed)} PMID(s)...")
        fetched = fetch_pubmed_publication_types(needed)
        # Record even PMIDs that returned nothing, as empty lists, so we do not
        # re-fetch them every run.
        for p in needed:
            cache[p] = fetched.get(p, [])
        save_type_cache(cache, cache_path)
    return cache


# --------------------------------------------------------------------------- #
# Collecting rows from the gene-review YAMLs
# --------------------------------------------------------------------------- #
def _bare_pmid(ref_id: str) -> Optional[str]:
    rid = (ref_id or "").strip()
    if rid.lower().startswith("pmid"):
        return rid.split(":", 1)[-1].strip()
    return None


def resolve_publication_type(
    ref_id: str, type_cache: Dict[str, List[str]]
) -> str:
    """Resolve a reference id to a PublicationTypeEnum value."""
    by_id = classify_reference_id(ref_id)
    if by_id is not None:
        return by_id
    bare = _bare_pmid(ref_id)
    if bare is not None and bare in type_cache:
        return classify_pubmed_publication_type(type_cache[bare])
    return "UNKNOWN"


def collect_pmids_from_review(data: dict) -> List[str]:
    """Collect every bare PMID referenced anywhere in a gene-review dict."""
    pmids: set[str] = set()

    def add(ref_id):
        b = _bare_pmid(ref_id or "")
        if b:
            pmids.add(b)

    for ref in data.get("references") or []:
        add(ref.get("id"))
    for ann in data.get("existing_annotations") or []:
        add(ann.get("original_reference_id"))
        review = ann.get("review") or {}
        for sb in review.get("supported_by") or []:
            add(sb.get("reference_id"))
        for rid in review.get("additional_reference_ids") or []:
            add(rid)
    for cf in data.get("core_functions") or []:
        for sb in cf.get("supported_by") or []:
            add(sb.get("reference_id"))
    for pt in data.get("proposed_new_terms") or []:
        for sb in pt.get("supported_by") or []:
            add(sb.get("reference_id"))
    return sorted(pmids)


def collect_rows(
    review_files: List[Path], type_cache: Dict[str, List[str]]
) -> Dict[str, pd.DataFrame]:
    """Build snippet/reference/annotation DataFrames across review files."""
    snippet_rows: List[dict] = []
    reference_rows: List[dict] = []
    annotation_rows: List[dict] = []

    for path in review_files:
        data = yaml.safe_load(path.read_text())
        if not data:
            continue
        gene = data.get("gene_symbol") or path.stem

        # ---- references table (one row per reference) ----
        for ref in data.get("references") or []:
            ref_id = ref.get("id") or ""
            ptype = resolve_publication_type(ref_id, type_cache)
            rr = ref.get("reference_review") or {}
            reference_rows.append(
                {
                    "gene": gene,
                    "reference_id": ref_id,
                    "publication_type": ptype,
                    "relevance": rr.get("relevance"),
                    "correctness": rr.get("correctness"),
                }
            )
            # findings are reference-level supporting snippets
            for finding in ref.get("findings") or []:
                snippet_rows.append(
                    {
                        "gene": gene,
                        "context": "finding",
                        "reference_id": ref_id,
                        "publication_type": ptype,
                        "section": finding.get("reference_section_type"),
                        "action": None,
                    }
                )

        # ---- annotation-level evidence ----
        for ann in data.get("existing_annotations") or []:
            review = ann.get("review") or {}
            action = review.get("action")
            term = (ann.get("term") or {}).get("id")
            supports = review.get("supported_by") or []
            support_types: List[str] = []
            sections: List[str] = []
            for sb in supports:
                ref_id = sb.get("reference_id") or ""
                ptype = resolve_publication_type(ref_id, type_cache)
                section = sb.get("reference_section_type")
                support_types.append(ptype)
                if section:
                    sections.append(section)
                snippet_rows.append(
                    {
                        "gene": gene,
                        "context": "annotation",
                        "reference_id": ref_id,
                        "publication_type": ptype,
                        "section": section,
                        "action": action,
                    }
                )

            annotation_rows.append(
                {
                    "gene": gene,
                    "term": term,
                    "action": action,
                    "n_support": len(supports),
                    "n_sections": len(sections),
                    "all_shallow": bool(sections)
                    and all(s in SHALLOW_SECTIONS for s in sections),
                    "any_deep": any(s not in SHALLOW_SECTIONS for s in sections),
                    "any_narrative": any(s in NARRATIVE_SECTIONS for s in sections),
                    "has_review": any(
                        t in ("REVIEW", "SYSTEMATIC_REVIEW", "META_ANALYSIS")
                        for t in support_types
                    ),
                    "has_primary": any(t == "PRIMARY_RESEARCH" for t in support_types),
                    "has_deep_research": any(
                        t == "DEEP_RESEARCH" for t in support_types
                    ),
                }
            )

        # ---- core_functions evidence (snippets only) ----
        for cf in data.get("core_functions") or []:
            for sb in cf.get("supported_by") or []:
                ref_id = sb.get("reference_id") or ""
                snippet_rows.append(
                    {
                        "gene": gene,
                        "context": "core_function",
                        "reference_id": ref_id,
                        "publication_type": resolve_publication_type(
                            ref_id, type_cache
                        ),
                        "section": sb.get("reference_section_type"),
                        "action": None,
                    }
                )

    return {
        "snippets": pd.DataFrame(snippet_rows),
        "references": pd.DataFrame(reference_rows),
        "annotations": pd.DataFrame(annotation_rows),
    }


# --------------------------------------------------------------------------- #
# Report
# --------------------------------------------------------------------------- #
def _pct(n: int, d: int) -> str:
    return f"{100 * n / d:.1f}%" if d else "n/a"


def build_report(frames: Dict[str, pd.DataFrame], organism: str) -> str:
    """Render a markdown report addressing the four hypotheses."""
    snip = frames["snippets"]
    refs = frames["references"]
    anns = frames["annotations"]

    lines: List[str] = []
    lines.append(f"# Evidence-source analysis ({organism})\n")
    lines.append(
        f"- Gene reviews analyzed: **{refs['gene'].nunique() if not refs.empty else 0}**\n"
        f"- References: **{len(refs)}**  |  Evidence snippets: **{len(snip)}**  "
        f"|  Reviewed annotations: **{len(anns)}**\n"
    )

    # ---------- Reference-level publication-type mix ----------
    lines.append("\n## Reference publication types\n")
    if not refs.empty:
        vc = refs["publication_type"].value_counts()
        lines.append("| publication_type | references | % |")
        lines.append("|---|---:|---:|")
        for t, n in vc.items():
            lines.append(f"| {t} | {n} | {_pct(n, len(refs))} |")

    # ---------- (b)/(d) Section distribution of evidence snippets ----------
    lines.append("\n## (b,d) Section of supporting-text snippets\n")
    sec = snip.dropna(subset=["section"]) if not snip.empty else snip
    if not sec.empty:
        vc = sec["section"].value_counts()
        n_total = len(sec)
        n_shallow = int(sec["section"].isin(SHALLOW_SECTIONS).sum())
        n_narr = int(sec["section"].isin(NARRATIVE_SECTIONS).sum())
        lines.append(
            f"Snippets with a section tag: **{n_total}**. "
            f"Shallow (title/abstract): **{_pct(n_shallow, n_total)}**. "
            f"Narrative (intro/lit-review/discussion/conclusions): "
            f"**{_pct(n_narr, n_total)}**.\n"
        )
        lines.append("| section | snippets | % |")
        lines.append("|---|---:|---:|")
        for s, n in vc.items():
            lines.append(f"| {s} | {n} | {_pct(n, n_total)} |")

    # ---------- (b) Abstract sufficiency by action ----------
    lines.append("\n## (b) Were abstracts alone enough? (per annotation)\n")
    if not anns.empty:
        scoped = anns[anns["n_sections"] > 0]
        lines.append(
            "Among annotations whose support carries section tags, share whose "
            "evidence is *entirely* title/abstract ('all_shallow'), broken down "
            "by curator action:\n"
        )
        lines.append("| action | annotations | all-abstract | % all-abstract |")
        lines.append("|---|---:|---:|---:|")
        for action, grp in scoped.groupby("action"):
            n = len(grp)
            sh = int(grp["all_shallow"].sum())
            lines.append(f"| {action} | {n} | {sh} | {_pct(sh, n)} |")

    # ---------- (a) Review papers ----------
    lines.append("\n## (a) Review-paper support by action\n")
    if not anns.empty:
        scoped = anns[anns["n_support"] > 0]
        lines.append(
            "Among annotations with at least one supporting reference, the share "
            "supported by a review/meta-analysis vs primary research, by action:\n"
        )
        lines.append(
            "| action | annotations | has review | % review | has primary | % primary |"
        )
        lines.append("|---|---:|---:|---:|---:|---:|")
        for action, grp in scoped.groupby("action"):
            n = len(grp)
            rv = int(grp["has_review"].sum())
            pr = int(grp["has_primary"].sum())
            lines.append(
                f"| {action} | {n} | {rv} | {_pct(rv, n)} | {pr} | {_pct(pr, n)} |"
            )

    # ---------- (c) Deep research ----------
    lines.append("\n## (c) Deep-research usage\n")
    if not refs.empty:
        n_dr_ref = int((refs["publication_type"] == "DEEP_RESEARCH").sum())
        n_genes_dr = (
            refs[refs["publication_type"] == "DEEP_RESEARCH"]["gene"].nunique()
        )
        n_dr_support = (
            int(anns["has_deep_research"].sum()) if not anns.empty else 0
        )
        lines.append(
            f"- Deep-research references: **{n_dr_ref}** across **{n_genes_dr}** "
            f"gene(s).\n"
            f"- Annotations citing a deep-research report as support: "
            f"**{n_dr_support}**.\n"
        )

    lines.append(
        "\n---\n*Generated by `ai-gene-review analyze-evidence-sources`. "
        "Publication types inferred from PubMed PT metadata; note PubMed under-tags "
        "some reviews, so REVIEW counts are a lower bound.*\n"
    )
    return "\n".join(lines)


def analyze_evidence_sources(
    organism: str = "human",
    genes_dir: Path = Path("genes"),
    cache_path: Path = DEFAULT_TYPE_CACHE,
    output_dir: Path = Path("reports/evidence_sources"),
    refresh: bool = False,
    network: bool = True,
) -> Path:
    """Run the full analysis and write TSVs + a markdown report.

    Returns the path to the markdown report.
    """
    review_files = sorted((genes_dir / organism).glob("*/*-ai-review.yaml"))
    if not review_files:
        raise FileNotFoundError(f"No review files under {genes_dir / organism}")

    # Gather PMIDs and ensure their types are cached.
    all_pmids: set[str] = set()
    parsed: List[tuple[Path, dict]] = []
    for path in review_files:
        data = yaml.safe_load(path.read_text())
        parsed.append((path, data or {}))
        if data:
            all_pmids.update(collect_pmids_from_review(data))

    type_cache = ensure_types_cached(
        sorted(all_pmids), cache_path, refresh=refresh, network=network
    )

    frames = collect_rows([p for p, _ in parsed], type_cache)

    output_dir.mkdir(parents=True, exist_ok=True)
    for name, df in frames.items():
        df.to_csv(output_dir / f"{organism}_{name}.tsv", sep="\t", index=False)

    report = build_report(frames, organism)
    report_path = output_dir / f"{organism}_evidence_sources.md"
    report_path.write_text(report)
    return report_path
