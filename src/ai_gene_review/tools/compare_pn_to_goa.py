"""Compare proteostasis workbook annotations against local GOA files.

This module performs a gene-by-gene, row-by-row comparison between the
Proteostasis Consortium workbook and local GOA TSV files.

The comparison is intentionally heuristic. The workbook uses a custom
proteostasis taxonomy rather than GO terms, so the script does not claim to
validate semantic equivalence. Instead, it:

1. Aligns workbook rows to local gene symbols and GOA files.
2. Scores each workbook row against GOA term names for the same gene.
3. Produces tabular reports showing likely matches and candidate gaps.

The output is useful for triage:

- rows with strong textual alignment are likely already reflected in GOA
- rows with weak or no textual alignment are good candidates for manual review
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
import re
from typing import Sequence

import pandas as pd
from rapidfuzz import fuzz

from ai_gene_review.validation.goa_validator import GOAAnnotation, GOAValidator

DEFAULT_WORKBOOK_SHEET = "dense"
DEFAULT_OUTPUT_DIR = Path("projects/PROTEOSTASIS/reports/pn_goa")
ALLOWED_SHORT_TOKENS = {"er", "ub", "ubl", "vcp"}
STOPWORDS = {
    "a",
    "an",
    "and",
    "associated",
    "branch",
    "class",
    "component",
    "components",
    "containing",
    "direct",
    "for",
    "function",
    "group",
    "in",
    "is",
    "network",
    "no",
    "of",
    "or",
    "pathway",
    "primarily",
    "process",
    "protein",
    "proteostasis",
    "specific",
    "subtype",
    "system",
    "the",
    "to",
    "type",
    "unknown",
    "various",
    "with",
}
TEXT_REPLACEMENTS = {
    "cct/tric": "cct tric",
    "co-chaperone": "cochaperone",
    "co-chaperones": "cochaperones",
    "endoplasmic-reticulum": "endoplasmic reticulum",
    "erad": "endoplasmic reticulum associated degradation",
    "hsp70-hsp90": "hsp70 hsp90",
    "pi3k": "phosphatidylinositol 3 kinase",
    "pn ": "proteostasis network ",
    "reglucosylation": "reglucosylation glucosylation",
    "tri c": "tric",
    "vps34": "vps34 phosphatidylinositol 3 kinase",
}
TOKEN_ALIASES = {
    "aggrephagy": {"autophagy", "aggregate"},
    "autophagophore": {"autophagy"},
    "casa": {"autophagy", "chaperone"},
    "cma": {"autophagy", "chaperone"},
    "cochaperone": {"cochaperone", "chaperone"},
    "glycoproteostasis": {"glycoprotein"},
    "hsp70": {"hsp70", "heat", "shock"},
    "hsp90": {"hsp90", "heat", "shock"},
    "lysophagy": {"autophagy", "lysosome"},
    "mitophagy": {"autophagy", "mitochondrial"},
    "pexophagy": {"autophagy", "peroxisome"},
    "reglucosylation": {"reglucosylation", "glucosylation"},
    "xenophagy": {"autophagy"},
}


@dataclass(frozen=True)
class ProteostasisAnnotation:
    """A single annotation row from the proteostasis workbook."""

    order: int | None
    gene_symbol: str
    gene_name: str
    branch: str
    class_name: str
    group: str
    type_name: str
    subtype: str
    notes: str

    def match_text(self, include_notes: bool = False) -> str:
        """Return the text used for heuristic GOA comparison."""
        parts = [self.branch, self.class_name, self.group, self.type_name, self.subtype]
        if include_notes and self.notes:
            parts.append(self.notes)
        return " ".join(part for part in parts if part)


@dataclass(frozen=True)
class AnnotationMatchResult:
    """Heuristic comparison of one workbook row to GOA."""

    best_goa_id: str
    best_goa_term: str
    best_goa_aspect: str
    best_goa_evidence: str
    best_keyword_overlap: int
    best_similarity: int
    matched_keywords: tuple[str, ...]
    match_level: str
    top_matches: tuple[str, ...]


def normalize_text(text: str) -> str:
    """Normalize free text for token-based comparison."""
    normalized = text.lower().strip()
    for source, target in TEXT_REPLACEMENTS.items():
        normalized = normalized.replace(source, target)
    normalized = normalized.replace("/", " ")
    normalized = normalized.replace("-", " ")
    normalized = re.sub(r"[^a-z0-9\s]+", " ", normalized)
    normalized = re.sub(r"\s+", " ", normalized).strip()
    return normalized


def tokenize_for_match(text: str) -> set[str]:
    """Tokenize text into a set of informative comparison keywords."""
    normalized = normalize_text(text)
    tokens: set[str] = set()
    for token in normalized.split():
        if token in STOPWORDS:
            continue
        if len(token) < 3 and token not in ALLOWED_SHORT_TOKENS:
            continue
        alias_tokens = TOKEN_ALIASES.get(token, {token})
        tokens.update(alias_tokens)
    return tokens


def extract_match_keywords(
    annotation: ProteostasisAnnotation, include_notes: bool = False
) -> set[str]:
    """Extract informative keywords from a proteostasis row."""
    return tokenize_for_match(annotation.match_text(include_notes=include_notes))


def _clean_cell(value: object) -> str:
    """Convert a dataframe cell to a clean string."""
    if pd.isna(value):
        return ""
    return str(value).strip()


def load_proteostasis_annotations(
    workbook: Path, sheet_name: str = DEFAULT_WORKBOOK_SHEET
) -> list[ProteostasisAnnotation]:
    """Load annotation rows from the proteostasis workbook."""
    dataframe = pd.read_excel(workbook, sheet_name=sheet_name)
    dataframe.columns = [str(column).strip() for column in dataframe.columns]
    dataframe = dataframe[dataframe["Gene Symbol"].notna()].copy()

    annotations: list[ProteostasisAnnotation] = []
    for row in dataframe.to_dict(orient="records"):
        raw_order = row.get("order")
        order = int(raw_order) if pd.notna(raw_order) else None
        annotations.append(
            ProteostasisAnnotation(
                order=order,
                gene_symbol=_clean_cell(row.get("Gene Symbol")),
                gene_name=_clean_cell(row.get("Gene Name")),
                branch=_clean_cell(row.get("Branch")),
                class_name=_clean_cell(row.get("Class")),
                group=_clean_cell(row.get("Group")),
                type_name=_clean_cell(row.get("Type")),
                subtype=_clean_cell(row.get("Subtype")),
                notes=_clean_cell(row.get("Notes")),
            )
        )

    return annotations


def _format_match_summary(
    annotation: GOAAnnotation,
    overlap: Sequence[str],
    similarity: int,
) -> str:
    """Format a compact summary string for a GOA match."""
    overlap_text = ",".join(overlap) if overlap else "-"
    return (
        f"{annotation.go_id} {annotation.go_term} "
        f"[aspect={annotation.go_aspect} overlap={len(overlap)}:{overlap_text} score={similarity}]"
    )


def compare_annotation_to_goa(
    annotation: ProteostasisAnnotation,
    goa_annotations: Sequence[GOAAnnotation],
    include_notes: bool = False,
) -> AnnotationMatchResult:
    """Compare one proteostasis row against GOA annotations for the same gene."""
    if not goa_annotations:
        return AnnotationMatchResult(
            best_goa_id="",
            best_goa_term="",
            best_goa_aspect="",
            best_goa_evidence="",
            best_keyword_overlap=0,
            best_similarity=0,
            matched_keywords=(),
            match_level="no_goa_annotations",
            top_matches=(),
        )

    pn_text = annotation.match_text(include_notes=include_notes)
    pn_keywords = extract_match_keywords(annotation, include_notes=include_notes)

    scored: list[tuple[int, int, tuple[str, ...], GOAAnnotation]] = []
    for goa_annotation in goa_annotations:
        goa_keywords = tokenize_for_match(goa_annotation.go_term)
        overlap = tuple(sorted(pn_keywords & goa_keywords))
        similarity = int(fuzz.token_set_ratio(normalize_text(pn_text), normalize_text(goa_annotation.go_term)))
        scored.append((len(overlap), similarity, overlap, goa_annotation))

    scored.sort(
        key=lambda item: (
            item[0],
            item[1],
            len(item[3].go_term),
        ),
        reverse=True,
    )

    best_overlap_count, best_similarity, best_overlap, best_annotation = scored[0]
    top_matches = tuple(
        _format_match_summary(goa_annotation, overlap, similarity)
        for overlap_count, similarity, overlap, goa_annotation in scored[:3]
    )

    if best_overlap_count >= 3 or (best_overlap_count >= 2 and best_similarity >= 55):
        match_level = "strong_text_match"
    elif best_overlap_count >= 1 or best_similarity >= 65:
        match_level = "weak_text_match"
    else:
        match_level = "no_text_match"

    return AnnotationMatchResult(
        best_goa_id=best_annotation.go_id,
        best_goa_term=best_annotation.go_term,
        best_goa_aspect=best_annotation.go_aspect,
        best_goa_evidence=best_annotation.evidence_code,
        best_keyword_overlap=best_overlap_count,
        best_similarity=best_similarity,
        matched_keywords=best_overlap,
        match_level=match_level,
        top_matches=top_matches,
    )


def _build_gene_summary(annotation_report: pd.DataFrame) -> pd.DataFrame:
    """Build a gene-level summary table from the row-level report."""
    if annotation_report.empty:
        return pd.DataFrame()

    grouped = annotation_report.groupby("gene_symbol", dropna=False)
    summary = grouped.agg(
        pn_annotation_rows=("gene_symbol", "size"),
        goa_annotation_count=("goa_annotation_count", "max"),
        strong_text_matches=("match_level", lambda values: int((values == "strong_text_match").sum())),
        weak_text_matches=("match_level", lambda values: int((values == "weak_text_match").sum())),
        no_text_matches=("match_level", lambda values: int((values == "no_text_match").sum())),
        no_goa_annotations=("match_level", lambda values: int((values == "no_goa_annotations").sum())),
        missing_goa_file=("goa_file_exists", lambda values: int((~values).sum())),
    ).reset_index()

    summary["candidate_gap_rows"] = summary["no_text_matches"] + summary["weak_text_matches"]
    return summary.sort_values(
        by=["candidate_gap_rows", "pn_annotation_rows", "gene_symbol"],
        ascending=[False, False, True],
    )


def generate_comparison_reports(
    workbook: Path,
    gene_root: Path,
    sheet_name: str = DEFAULT_WORKBOOK_SHEET,
    genes: Sequence[str] | None = None,
    include_notes: bool = False,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Generate row-level and gene-level reports comparing PN rows to GOA."""
    selected_genes = set(genes) if genes else None
    annotations = load_proteostasis_annotations(workbook, sheet_name=sheet_name)
    if selected_genes is not None:
        annotations = [annotation for annotation in annotations if annotation.gene_symbol in selected_genes]

    validator = GOAValidator()
    goa_cache: dict[str, list[GOAAnnotation]] = {}
    report_rows: list[dict[str, object]] = []

    for annotation in annotations:
        goa_file = gene_root / annotation.gene_symbol / f"{annotation.gene_symbol}-goa.tsv"
        if annotation.gene_symbol not in goa_cache:
            goa_cache[annotation.gene_symbol] = (
                validator.parse_goa_file(goa_file) if goa_file.exists() else []
            )
        goa_annotations = goa_cache[annotation.gene_symbol]
        match = compare_annotation_to_goa(
            annotation,
            goa_annotations,
            include_notes=include_notes,
        )

        report_rows.append(
            {
                "gene_symbol": annotation.gene_symbol,
                "gene_name": annotation.gene_name,
                "pn_order": annotation.order,
                "pn_branch": annotation.branch,
                "pn_class": annotation.class_name,
                "pn_group": annotation.group,
                "pn_type": annotation.type_name,
                "pn_subtype": annotation.subtype,
                "pn_keywords": ",".join(sorted(extract_match_keywords(annotation, include_notes=include_notes))),
                "goa_file_exists": goa_file.exists(),
                "goa_file": str(goa_file),
                "goa_annotation_count": len(goa_annotations),
                "goa_mf_count": sum(ann.go_aspect == "MF" for ann in goa_annotations),
                "goa_bp_count": sum(ann.go_aspect == "BP" for ann in goa_annotations),
                "goa_cc_count": sum(ann.go_aspect == "CC" for ann in goa_annotations),
                "best_goa_id": match.best_goa_id,
                "best_goa_term": match.best_goa_term,
                "best_goa_aspect": match.best_goa_aspect,
                "best_goa_evidence": match.best_goa_evidence,
                "best_keyword_overlap": match.best_keyword_overlap,
                "best_similarity": match.best_similarity,
                "matched_keywords": ",".join(match.matched_keywords),
                "match_level": match.match_level,
                "top_matches": " || ".join(match.top_matches),
            }
        )

    annotation_report = pd.DataFrame(report_rows).sort_values(
        by=["gene_symbol", "pn_order", "pn_branch", "pn_class", "pn_group"],
        ascending=[True, True, True, True, True],
    )
    gene_summary = _build_gene_summary(annotation_report)
    return annotation_report, gene_summary


def _parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description=(
            "Heuristically compare proteostasis workbook rows against local GOA files "
            "for the same human genes."
        )
    )
    parser.add_argument(
        "--workbook",
        type=Path,
        required=True,
        help="Path to the Human Proteostasis Network Excel workbook.",
    )
    parser.add_argument(
        "--gene-root",
        type=Path,
        default=Path("genes/human"),
        help="Root directory containing human gene folders with <GENE>-goa.tsv files.",
    )
    parser.add_argument(
        "--sheet",
        default=DEFAULT_WORKBOOK_SHEET,
        help=f"Workbook sheet name to read. Default: {DEFAULT_WORKBOOK_SHEET}.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
        help=f"Directory for TSV reports. Default: {DEFAULT_OUTPUT_DIR}.",
    )
    parser.add_argument(
        "--gene",
        action="append",
        default=[],
        help="Restrict comparison to one gene symbol. May be supplied multiple times.",
    )
    parser.add_argument(
        "--include-notes",
        action="store_true",
        help="Include workbook Notes text in heuristic matching.",
    )
    return parser.parse_args()


def main() -> None:
    """Run the workbook-vs-GOA comparison and write TSV reports."""
    args = _parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)

    annotation_report, gene_summary = generate_comparison_reports(
        workbook=args.workbook,
        gene_root=args.gene_root,
        sheet_name=args.sheet,
        genes=args.gene,
        include_notes=args.include_notes,
    )

    annotation_output = args.output_dir / "pn_goa_annotation_report.tsv"
    gene_output = args.output_dir / "pn_goa_gene_summary.tsv"
    annotation_report.to_csv(annotation_output, sep="\t", index=False)
    gene_summary.to_csv(gene_output, sep="\t", index=False)

    print(f"Wrote {len(annotation_report)} annotation rows to {annotation_output}")
    print(f"Wrote {len(gene_summary)} gene summaries to {gene_output}")
    if not annotation_report.empty:
        counts = annotation_report["match_level"].value_counts().to_dict()
        print("Match levels:")
        for match_level in sorted(counts):
            print(f"  {match_level}: {counts[match_level]}")


if __name__ == "__main__":
    main()
