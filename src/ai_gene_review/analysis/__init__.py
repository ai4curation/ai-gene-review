"""Analysis utilities for gene reviews.

Currently provides the *subtraction report* (see :mod:`subtraction_report`):
a generic mechanism that, for a chosen reference/evidence-code (e.g. IBA), asks
what is lost if those annotations are removed -- which endorsed annotations
disappear and which ``core_functions`` remain grounded (taking ontology closure
into account).
"""

from ai_gene_review.analysis.subtraction_report import (
    CoreFunctionCoverage,
    GeneSubtractionResult,
    LostAnnotation,
    SubtractionFilter,
    SubtractionReporter,
    make_go_ancestor_fn,
)

__all__ = [
    "CoreFunctionCoverage",
    "GeneSubtractionResult",
    "LostAnnotation",
    "SubtractionFilter",
    "SubtractionReporter",
    "make_go_ancestor_fn",
]
