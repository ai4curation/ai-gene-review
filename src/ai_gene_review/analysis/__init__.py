"""Analysis utilities for gene reviews.

Currently provides the *subtraction report* (see :mod:`subtraction_report`):
a generic mechanism that, for a chosen reference/evidence-code (e.g. IBA), asks
what is lost if those annotations are removed -- which endorsed annotations
disappear and which ``core_functions`` remain grounded (taking ontology closure
into account).

This package re-exports the public API of :mod:`subtraction_report`; consumers
may import either from here or from the submodule directly.
"""

from ai_gene_review.analysis.subtraction_report import (
    CoreFunctionCoverage,
    GeneSubtractionResult,
    LostAnnotation,
    SubtractionFilter,
    SubtractionReporter,
    core_function_rows,
    effective_term_ids,
    iter_review_files,
    lost_annotation_rows,
    make_go_ancestor_fn,
    render_markdown,
    summarize,
    write_tsv_reports,
)

__all__ = [
    "CoreFunctionCoverage",
    "GeneSubtractionResult",
    "LostAnnotation",
    "SubtractionFilter",
    "SubtractionReporter",
    "core_function_rows",
    "effective_term_ids",
    "iter_review_files",
    "lost_annotation_rows",
    "make_go_ancestor_fn",
    "render_markdown",
    "summarize",
    "write_tsv_reports",
]
