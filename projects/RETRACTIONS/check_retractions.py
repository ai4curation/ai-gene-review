#!/usr/bin/env python3
"""Check every PMID cited by the gene reviews against PubMed's retraction metadata.

A retracted paper can sit behind a GO annotation indefinitely: nothing in the
fetch / validate pipeline notices that a cited PMID has since been withdrawn. This
script closes that gap.

What it does
------------

1. Walks every ``genes/*/*/*-ai-review.yaml`` and collects each ``PMID:`` citation
   together with *where* it is cited:

   * ``reference``        -- an entry in the top-level ``references:`` list
   * ``annotation``       -- an ``original_reference_id`` on an existing annotation
                             (i.e. the GO evidence line itself rests on this paper)
   * ``supporting_text``  -- a ``supported_by[].reference_id`` inside a review /
                             core function (the paper is quoted as support)

2. Queries PubMed in batches through NCBI E-utilities ``efetch`` (POST, XML) and
   reads two independent signals:

   * ``PublicationType`` containing ``Retracted Publication`` or
     ``Expression of Concern``
   * ``CommentsCorrections`` with ``RefType`` of ``RetractionIn``,
     ``ExpressionOfConcernIn`` or ``ErratumIn``

3. Writes a TSV + JSON report next to this script.

Severity is deliberately tiered, because the three signals are not equally serious:

``RETRACTED``
    The cited paper has been withdrawn. Actionable: the citation must be flagged
    (``is_invalid: true``) and any annotation resting on it re-examined.
``EXPRESSION_OF_CONCERN``
    The record is under question but not withdrawn. Worth a look, not an emergency.
``ERRATUM``
    A correction was published. **Usually benign** -- an erratum is very often an
    author-name spelling, a funding statement, or a figure legend. Reported quietly,
    for completeness only; it is not by itself evidence of any problem.

PMIDs that are themselves *notices* (publication type ``Retraction of Publication``
/ ``Published Erratum``) are recorded separately and are **not** problems: citing the
retraction notice is exactly what a careful review should do.

Usage::

    uv run --no-dev python projects/RETRACTIONS/check_retractions.py
    uv run --no-dev python projects/RETRACTIONS/check_retractions.py --limit 500
    uv run --no-dev python projects/RETRACTIONS/check_retractions.py --cache-only

Set ``NCBI_API_KEY`` in the environment to raise the NCBI rate limit (optional).
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import sys
import time
import xml.etree.ElementTree as ET
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional

import requests
import yaml

try:  # libyaml is ~5x faster over the 4.5k review files, but is optional
    from yaml import CSafeLoader as _Loader  # type: ignore[attr-defined]
except ImportError:  # pragma: no cover
    from yaml import SafeLoader as _Loader  # type: ignore[assignment]

REPO_ROOT = Path(__file__).resolve().parents[2]
GENES_DIR = REPO_ROOT / "genes"
OUT_DIR = Path(__file__).resolve().parent

EFETCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

# PubMed PublicationType values that mark the *cited* record as problematic.
PROBLEM_PUBTYPES = {
    "Retracted Publication": "RETRACTED",
    "Expression of Concern": "EXPRESSION_OF_CONCERN",
}
# PublicationType values that mark the record as a *notice about* another paper.
# (Note that PubMed puts "Expression of Concern" on the notice; the paper the
# notice is about carries the ExpressionOfConcernIn CommentsCorrections instead.)
NOTICE_PUBTYPES = {"Retraction of Publication", "Published Erratum"}
# CommentsCorrections RefTypes that point *backwards*, from a notice to its subject.
NOTICE_REFTYPES = {"RetractionOf", "ExpressionOfConcernFor", "ErratumFor"}
# CommentsCorrections RefTypes pointing from the cited paper to a later correction.
PROBLEM_REFTYPES = {
    "RetractionIn": "RETRACTED",
    "ExpressionOfConcernIn": "EXPRESSION_OF_CONCERN",
    "ErratumIn": "ERRATUM",
}

SEVERITY_ORDER = ["RETRACTED", "EXPRESSION_OF_CONCERN", "ERRATUM"]


# ---------------------------------------------------------------------------
# 1. Collect citations out of the gene reviews
# ---------------------------------------------------------------------------


@dataclass
class Citation:
    """One place a PMID is cited."""

    pmid: str
    organism: str
    gene: str
    site: str  # reference | annotation | supporting_text
    detail: str = ""  # GO term / action, when the site is an annotation
    already_invalid: bool = False  # the review already says is_invalid: true


def _norm_pmid(value: Any) -> Optional[str]:
    """Return a normalized ``PMID:12345`` string, or None if not a PMID."""
    if not isinstance(value, str):
        return None
    text = value.strip()
    if not text.upper().startswith("PMID:"):
        return None
    digits = text[5:].strip()
    if not digits.isdigit():
        return None
    return f"PMID:{digits}"


def _walk_reference_ids(node: Any) -> Iterable[str]:
    """Yield every ``reference_id`` / ``original_reference_id`` PMID under ``node``."""
    if isinstance(node, dict):
        for key, value in node.items():
            if key in ("reference_id", "original_reference_id"):
                values = value if isinstance(value, list) else [value]
                for item in values:
                    pmid = _norm_pmid(item)
                    if pmid:
                        yield pmid
            else:
                yield from _walk_reference_ids(value)
    elif isinstance(node, list):
        for item in node:
            yield from _walk_reference_ids(item)


def collect_citations(review_path: Path) -> List[Citation]:
    """Collect every PMID citation in one ``*-ai-review.yaml``."""
    try:
        data = yaml.load(review_path.read_text(), Loader=_Loader)
    except Exception as exc:  # pragma: no cover - corrupt file
        print(f"  ! could not parse {review_path}: {exc}", file=sys.stderr)
        return []
    if not isinstance(data, dict):
        return []

    gene = review_path.name.replace("-ai-review.yaml", "")
    organism = review_path.parent.parent.name
    out: List[Citation] = []

    # references:
    for ref in data.get("references") or []:
        if not isinstance(ref, dict):
            continue
        pmid = _norm_pmid(ref.get("id"))
        if pmid:
            out.append(
                Citation(
                    pmid=pmid,
                    organism=organism,
                    gene=gene,
                    site="reference",
                    already_invalid=bool(ref.get("is_invalid")),
                )
            )

    # existing_annotations: the evidence line itself, plus its supporting quotes
    for ann in data.get("existing_annotations") or []:
        if not isinstance(ann, dict):
            continue
        term = ann.get("term") or {}
        term_id = term.get("id", "") if isinstance(term, dict) else ""
        term_label = term.get("label", "") if isinstance(term, dict) else ""
        review = ann.get("review") or {}
        action = review.get("action", "") if isinstance(review, dict) else ""
        evidence = ann.get("evidence_type", "")
        detail = f"{term_id} {term_label} [{evidence}] action={action}".strip()

        pmid = _norm_pmid(ann.get("original_reference_id"))
        if pmid:
            out.append(
                Citation(
                    pmid=pmid,
                    organism=organism,
                    gene=gene,
                    site="annotation",
                    detail=detail,
                )
            )
        # supported_by anywhere inside the annotation (review, nested lists, ...)
        seen_support = set()
        for support_pmid in _walk_reference_ids(
            {k: v for k, v in ann.items() if k != "original_reference_id"}
        ):
            if support_pmid in seen_support:
                continue
            seen_support.add(support_pmid)
            out.append(
                Citation(
                    pmid=support_pmid,
                    organism=organism,
                    gene=gene,
                    site="supporting_text",
                    detail=detail,
                )
            )

    # everything else (core_functions, proposed_new_terms, ...)
    rest = {
        k: v
        for k, v in data.items()
        if k not in ("references", "existing_annotations")
    }
    for other_pmid in set(_walk_reference_ids(rest)):
        out.append(
            Citation(
                pmid=other_pmid, organism=organism, gene=gene, site="supporting_text"
            )
        )

    return out


# ---------------------------------------------------------------------------
# 2. Ask PubMed
# ---------------------------------------------------------------------------


@dataclass
class PubMedRecord:
    pmid: str
    title: str = ""
    journal: str = ""
    year: str = ""
    publication_types: List[str] = field(default_factory=list)
    # RefType -> list of PMIDs of the correcting/retracting notice
    comments_corrections: Dict[str, List[str]] = field(default_factory=dict)

    @property
    def flags(self) -> List[str]:
        """Severity labels implied by this record's metadata."""
        found = set()
        for ptype in self.publication_types:
            if ptype in PROBLEM_PUBTYPES:
                # "Expression of Concern" on a *notice* is handled by is_notice
                found.add(PROBLEM_PUBTYPES[ptype])
        for reftype in self.comments_corrections:
            if reftype in PROBLEM_REFTYPES:
                found.add(PROBLEM_REFTYPES[reftype])
        return [s for s in SEVERITY_ORDER if s in found]

    @property
    def is_notice(self) -> bool:
        """True if this record is itself a retraction / EoC / erratum *notice*.

        A notice is not a problem: citing the retraction notice alongside the
        retracted paper is good practice, and it must not be reported as if the
        notice itself had been withdrawn.
        """
        if any(p in NOTICE_PUBTYPES for p in self.publication_types):
            return True
        return any(rt in NOTICE_REFTYPES for rt in self.comments_corrections)

    @property
    def severity(self) -> str:
        flags = self.flags
        return flags[0] if flags else ""


def _text(elem: Optional[ET.Element]) -> str:
    if elem is None:
        return ""
    return "".join(elem.itertext()).strip()


def parse_efetch_xml(xml_text: str) -> Dict[str, PubMedRecord]:
    """Parse an efetch PubMed XML payload into PubMedRecords keyed by ``PMID:n``."""
    records: Dict[str, PubMedRecord] = {}
    root = ET.fromstring(xml_text)
    for article in root.iter("PubmedArticle"):
        citation = article.find("MedlineCitation")
        if citation is None:
            continue
        pmid_elem = citation.find("PMID")
        if pmid_elem is None or not (pmid_elem.text or "").strip():
            continue
        pmid = f"PMID:{pmid_elem.text.strip()}"
        rec = PubMedRecord(pmid=pmid)
        art = citation.find("Article")
        if art is not None:
            rec.title = _text(art.find("ArticleTitle"))
            journal = art.find("Journal")
            if journal is not None:
                rec.journal = _text(journal.find("ISOAbbreviation")) or _text(
                    journal.find("Title")
                )
                year = journal.find("JournalIssue/PubDate/Year")
                rec.year = _text(year) or _text(
                    journal.find("JournalIssue/PubDate/MedlineDate")
                )[:4]
            for ptype in art.findall("PublicationTypeList/PublicationType"):
                value = _text(ptype)
                if value:
                    rec.publication_types.append(value)
        for cc in citation.findall("CommentsCorrectionsList/CommentsCorrections"):
            reftype = cc.get("RefType", "")
            notice_pmid = _text(cc.find("PMID"))
            rec.comments_corrections.setdefault(reftype, [])
            if notice_pmid:
                rec.comments_corrections[reftype].append(notice_pmid)
        records[pmid] = rec
    return records


def fetch_records(
    pmids: List[str], batch_size: int = 200, delay: float = 0.5, retries: int = 3
) -> Dict[str, PubMedRecord]:
    """Fetch PubMed records for ``pmids`` (``PMID:n`` strings) in polite batches."""
    api_key = os.environ.get("NCBI_API_KEY")
    session = requests.Session()
    out: Dict[str, PubMedRecord] = {}
    batches = [pmids[i : i + batch_size] for i in range(0, len(pmids), batch_size)]
    for index, batch in enumerate(batches, start=1):
        payload = {
            "db": "pubmed",
            "id": ",".join(p.split(":", 1)[1] for p in batch),
            "retmode": "xml",
            "tool": "ai-gene-review-retraction-check",
        }
        if api_key:
            payload["api_key"] = api_key
        for attempt in range(1, retries + 1):
            try:
                resp = session.post(EFETCH_URL, data=payload, timeout=120)
                resp.raise_for_status()
                out.update(parse_efetch_xml(resp.text))
                break
            except Exception as exc:
                if attempt == retries:
                    print(
                        f"  ! batch {index}/{len(batches)} failed after {retries} "
                        f"attempts: {exc}",
                        file=sys.stderr,
                    )
                else:
                    time.sleep(delay * 4 * attempt)
        print(
            f"  batch {index}/{len(batches)} done ({len(out)} records)",
            file=sys.stderr,
        )
        time.sleep(delay)
    return out


# ---------------------------------------------------------------------------
# 3. Report
# ---------------------------------------------------------------------------


def write_reports(
    records: Dict[str, PubMedRecord],
    citations: Dict[str, List[Citation]],
    out_dir: Path,
    unresolved: List[str],
) -> Dict[str, Any]:
    """Write the TSV + JSON reports; return the summary dict."""
    # A record that is itself a notice is never a problem, only its subject is.
    flagged = {
        pmid: rec
        for pmid, rec in records.items()
        if rec.flags and not rec.is_notice
    }

    rows = []
    for pmid, rec in sorted(
        flagged.items(),
        key=lambda kv: (SEVERITY_ORDER.index(kv[1].severity), kv[0]),
    ):
        cites = citations.get(pmid, [])
        sites = sorted({c.site for c in cites})
        genes = sorted({f"{c.organism}/{c.gene}" for c in cites})
        notices = sorted(set(severity_notices(rec.comments_corrections, rec.severity)))
        rows.append(
            {
                "pmid": pmid,
                "severity": rec.severity,
                "flags": ";".join(rec.flags),
                "publication_types": ";".join(rec.publication_types),
                "comments_corrections": ";".join(
                    f"{k}:{','.join(v)}" for k, v in sorted(rec.comments_corrections.items())
                ),
                "notice_pmids": ";".join(notices),
                "title": rec.title,
                "journal": rec.journal,
                "year": rec.year,
                "n_citing_genes": len(genes),
                "citing_genes": ";".join(genes),
                "citation_sites": ";".join(sites),
                "used_as_annotation_evidence": any(
                    c.site == "annotation" for c in cites
                ),
                "already_flagged_is_invalid": any(c.already_invalid for c in cites),
                "annotation_details": ";".join(
                    sorted({f"{c.organism}/{c.gene} {c.detail}".strip() for c in cites if c.site == "annotation"})
                ),
            }
        )

    out_dir.mkdir(parents=True, exist_ok=True)
    tsv_path = out_dir / "retraction-check.tsv"
    fieldnames = list(rows[0].keys()) if rows else [
        "pmid",
        "severity",
        "flags",
        "publication_types",
        "comments_corrections",
        "notice_pmids",
        "title",
        "journal",
        "year",
        "n_citing_genes",
        "citing_genes",
        "citation_sites",
        "used_as_annotation_evidence",
        "already_flagged_is_invalid",
        "annotation_details",
    ]
    with tsv_path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, delimiter="\t")
        writer.writeheader()
        for row in rows:
            writer.writerow(row)

    by_severity: Dict[str, int] = defaultdict(int)
    for row in rows:
        by_severity[row["severity"]] += 1

    summary = {
        "generated_by": "projects/RETRACTIONS/check_retractions.py",
        "n_review_files": len({(c.organism, c.gene) for cl in citations.values() for c in cl}),
        "n_distinct_pmids_cited": len(citations),
        "n_pmids_resolved": len(records),
        "n_pmids_unresolved": len(unresolved),
        "unresolved_pmids": sorted(unresolved),
        "counts_by_severity": dict(by_severity),
        "flagged": rows,
    }
    json_path = out_dir / "retraction-check.json"
    json_path.write_text(json.dumps(summary, indent=2, sort_keys=False) + "\n")
    print(f"wrote {tsv_path}")
    print(f"wrote {json_path}")
    return summary


REGENERATE_CMD = "uv run --no-dev python projects/RETRACTIONS/check_retractions.py"

ERRATUM_TABLE_CAP = 40


SEVERITY_REFTYPE = {
    "RETRACTED": "RetractionIn",
    "EXPRESSION_OF_CONCERN": "ExpressionOfConcernIn",
    "ERRATUM": "ErratumIn",
}


def severity_notices(
    comments_corrections: Dict[str, List[str]], severity: str
) -> List[str]:
    """The notice PMIDs that match a row's severity.

    A paper can carry several kinds of correction at once (the BACE1 case here has
    both an ``ErratumIn`` from 2018 and a ``RetractionIn`` from 2026); reporting them
    together in one "notice" column would misattribute the erratum as a retraction.
    """
    return list(comments_corrections.get(SEVERITY_REFTYPE.get(severity, ""), []))


def _parse_cc_field(value: str) -> Dict[str, List[str]]:
    """Parse the flattened ``RefType:pmid,pmid;RefType:pmid`` TSV/JSON field."""
    out: Dict[str, List[str]] = {}
    for chunk in filter(None, value.split(";")):
        reftype, _, pmids = chunk.partition(":")
        out[reftype] = [p for p in pmids.split(",") if p]
    return out


def _cite_summary(row: Dict[str, Any]) -> str:
    """Human-readable description of how a flagged PMID is used."""
    sites = row["citation_sites"].split(";") if row["citation_sites"] else []
    labels = {
        "annotation": "GO annotation evidence",
        "reference": "reference list",
        "supporting_text": "supporting text",
    }
    return ", ".join(labels.get(s, s) for s in sites)


MAX_GENES_SHOWN = 8


def _genes_cell(row: Dict[str, Any], max_shown: int = MAX_GENES_SHOWN) -> str:
    """Citing genes, truncated - interactome papers are cited by hundreds."""
    genes = [g for g in row["citing_genes"].split(";") if g]
    if not genes:
        return "-"
    if len(genes) <= max_shown:
        return ", ".join(genes)
    return ", ".join(genes[:max_shown]) + f", ... (+{len(genes) - max_shown} more)"


def _register_table(rows: List[Dict[str, Any]], with_notice: bool = True) -> List[str]:
    """Render one severity section's table.

    ``with_notice`` also selects the *shape*: the retracted / EoC tables carry the
    notice PMID and the ``is_invalid`` state, while the erratum table is a bare
    inventory (no action is implied, so there is nothing to flag).
    """
    if with_notice:
        header = (
            "| PMID | Title | Journal / year | Notice | Cited by | Cited as | "
            "Annotation evidence? | Already flagged `is_invalid` |"
        )
    else:
        header = "| PMID | Title | Journal / year | Cited by | Cited as |"
    lines = [header, "|" + "---|" * (header.count("|") - 1)]
    for row in rows:
        title = row["title"].replace("|", "\\|")
        if len(title) > 110:
            title = title[:107] + "..."
        notice_ids = severity_notices(
            _parse_cc_field(row.get("comments_corrections", "")), row["severity"]
        ) or [n for n in row.get("notice_pmids", "").split(";") if n]
        notice = ", ".join(f"PMID:{n}" for n in sorted(set(notice_ids))) or "-"
        journal = f"{row['journal']} {row['year']}".strip() or "-"
        if with_notice:
            cells = [
                row["pmid"],
                title,
                journal,
                notice,
                _genes_cell(row),
                _cite_summary(row) or "-",
                "**yes**" if row["used_as_annotation_evidence"] else "no",
                "yes" if row["already_flagged_is_invalid"] else "no",
            ]
        else:
            n_genes = len([g for g in row["citing_genes"].split(";") if g])
            cells = [
                row["pmid"],
                title,
                journal,
                _genes_cell(row, 3) + (f" [{n_genes} genes]" if n_genes > 3 else ""),
                _cite_summary(row) or "-",
            ]
        lines.append("| " + " | ".join(cells) + " |")
    return lines


def write_register(summary: Dict[str, Any], out_dir: Path) -> Path:
    """Write the human-readable retraction register."""
    rows = summary["flagged"]
    by_sev = {sev: [r for r in rows if r["severity"] == sev] for sev in SEVERITY_ORDER}
    for sev in by_sev:
        by_sev[sev].sort(key=lambda r: (-r["n_citing_genes"], r["pmid"]))

    n_ret = len(by_sev["RETRACTED"])
    n_eoc = len(by_sev["EXPRESSION_OF_CONCERN"])
    n_err = len(by_sev["ERRATUM"])
    ret_as_evidence = [r for r in by_sev["RETRACTED"] if r["used_as_annotation_evidence"]]

    lines: List[str] = []
    lines.append("---")
    lines.append('title: "Retraction Register"')
    lines.append("---")
    lines.append("")
    lines.append("# Retraction Register")
    lines.append("")
    lines.append(
        f"<!-- GENERATED FILE. Do not edit by hand. Regenerate with `{REGENERATE_CMD}`. -->"
    )
    lines.append("")
    lines.append(
        f"Every `PMID:` cited anywhere in the gene reviews, checked against PubMed's "
        f"retraction metadata. Generated {date.today().isoformat()} from "
        f"**{summary['n_review_files']}** review files and "
        f"**{summary['n_distinct_pmids_cited']}** distinct cited PMIDs "
        f"(**{summary['n_pmids_resolved']}** resolved at PubMed, "
        f"**{summary['n_pmids_unresolved']}** unresolved). "
        f"See the [project page](../RETRACTIONS.md) for method and curation guidance."
    )
    lines.append("")
    lines.append(
        f"**{n_ret} retracted**, {n_eoc} under expression of concern, "
        f"{n_err} with a published erratum."
    )
    lines.append("")

    # --- retracted -------------------------------------------------------
    lines.append("## Retracted publications (actionable)")
    lines.append("")
    if n_ret == 0:
        lines.append(
            "No cited publication is currently marked retracted in PubMed."
        )
    else:
        lines.append(
            "A retraction withdraws the *source*. It does not by itself refute a GO "
            "annotation, but every annotation resting on one of these papers needs "
            "re-examination, and the citation itself should carry `is_invalid: true`."
        )
        lines.append("")
        lines.extend(_register_table(by_sev["RETRACTED"]))
        lines.append("")
        if ret_as_evidence:
            lines.append(
                f"Of these, **{len(ret_as_evidence)}** are cited as the "
                f"`original_reference_id` of a GO annotation "
                f"({', '.join(sorted({g for r in ret_as_evidence for g in r['citing_genes'].split(';')}))}) "
                "- these are the ones a curator should look at first."
            )
        else:
            lines.append(
                "**None** of them is the `original_reference_id` of a GO annotation, so no "
                "existing annotation rests directly on a retracted paper."
            )
        lines.append("")

    # --- expression of concern -------------------------------------------
    lines.append("## Expressions of concern")
    lines.append("")
    if n_eoc == 0:
        lines.append("None.")
    else:
        lines.append(
            "The record is questioned but not withdrawn. Worth reading the notice "
            "before leaning on the paper; not grounds for removing an annotation."
        )
        lines.append("")
        lines.extend(_register_table(by_sev["EXPRESSION_OF_CONCERN"]))
    lines.append("")

    # --- errata ----------------------------------------------------------
    lines.append("## Errata (informational)")
    lines.append("")
    if n_err == 0:
        lines.append("None.")
    else:
        lines.append(
            f"{n_err} cited papers have a published erratum. **An erratum is normally "
            "benign** - most correct an author name, an affiliation, a funding "
            "statement or a figure legend, and the science stands unchanged. They are "
            "listed here for completeness only and require no action unless the "
            "correction happens to touch the result being cited."
        )
        lines.append("")
        shown = by_sev["ERRATUM"][:ERRATUM_TABLE_CAP]
        lines.extend(_register_table(shown, with_notice=False))
        if n_err > len(shown):
            lines.append("")
            lines.append(
                f"({len(shown)} of {n_err} shown, most-cited first; the full list is in "
                "`retraction-check.tsv`.)"
            )
    lines.append("")

    if summary["n_pmids_unresolved"]:
        lines.append("## Unresolved PMIDs")
        lines.append("")
        unresolved = summary.get("unresolved_pmids") or []
        listed = ", ".join(unresolved[:10])
        lines.append(
            f"{summary['n_pmids_unresolved']} cited PMID(s) returned no PubMed record "
            "and could not be checked. These are typically malformed or withdrawn "
            "identifiers rather than retractions"
            + (f": {listed}" if listed else "")
            + ("" if len(unresolved) <= 10 else ", ... (full list in `retraction-check.json`)")
            + "."
        )
        lines.append("")

    path = out_dir / "retraction-register.md"
    path.write_text("\n".join(lines))
    print(f"wrote {path}")
    return path


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument(
        "--genes-dir", type=Path, default=GENES_DIR, help="root of the genes/ tree"
    )
    parser.add_argument("--out-dir", type=Path, default=OUT_DIR)
    parser.add_argument(
        "--batch-size", type=int, default=200, help="PMIDs per efetch request"
    )
    parser.add_argument(
        "--delay", type=float, default=0.5, help="seconds to pause between requests"
    )
    parser.add_argument(
        "--limit", type=int, default=0, help="only check the first N PMIDs (testing)"
    )
    parser.add_argument(
        "--pmids",
        nargs="*",
        default=None,
        help="check only these PMIDs (still reports where they are cited)",
    )
    parser.add_argument(
        "--from-json",
        type=Path,
        default=None,
        help="rebuild the register from an existing retraction-check.json (no network)",
    )
    parser.add_argument(
        "--no-register",
        action="store_true",
        help="skip writing retraction-register.md (e.g. for a partial run)",
    )
    args = parser.parse_args(argv)

    if args.from_json:
        summary = json.loads(Path(args.from_json).read_text())
        write_register(summary, args.out_dir)
        return 0

    review_files = sorted(args.genes_dir.glob("*/*/*-ai-review.yaml"))
    print(f"scanning {len(review_files)} review files ...")
    citations: Dict[str, List[Citation]] = defaultdict(list)
    for path in review_files:
        for cite in collect_citations(path):
            citations[cite.pmid].append(cite)
    print(f"found {len(citations)} distinct PMIDs cited")

    pmids = sorted(citations, key=lambda p: int(p.split(":")[1]))
    if args.pmids:
        wanted = {_norm_pmid(p) or _norm_pmid(f"PMID:{p}") for p in args.pmids}
        pmids = [p for p in wanted if p]
    if args.limit:
        pmids = pmids[: args.limit]

    print(f"querying PubMed for {len(pmids)} PMIDs ...")
    records = fetch_records(pmids, batch_size=args.batch_size, delay=args.delay)
    unresolved = [p for p in pmids if p not in records]

    summary = write_reports(records, citations, args.out_dir, unresolved)
    if not args.no_register:
        write_register(summary, args.out_dir)
    counts = summary["counts_by_severity"]
    print(
        "flagged: "
        + ", ".join(f"{k}={counts.get(k, 0)}" for k in SEVERITY_ORDER)
        + f" (unresolved PMIDs: {len(unresolved)})"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
