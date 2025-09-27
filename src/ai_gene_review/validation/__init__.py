"""Validation subpackage for ai-gene-review.

This package contains all validation-related modules:
- Core validation logic
- Term validation (ontology terms)
- Publication validation
- Validation reporting
"""

from ai_gene_review.validation.publication_validator import (
    PublicationValidator,
    PublicationValidationResult,
)
from ai_gene_review.validation.term_validator import (
    TermValidator,
    TermValidationResult,
)
from ai_gene_review.validation.validation_report import (
    BatchValidationReport,
    ValidationIssue,
    ValidationReport,
    ValidationSeverity,
)
from ai_gene_review.validation.validator import (
    get_schema_path,
    get_validation_summary,
    load_schema,
    validate_gene_review,
    validate_multiple_files,
)

__all__ = [
    # Main validation functions
    "validate_gene_review",
    "validate_multiple_files",
    "get_validation_summary",
    "get_schema_path",
    "load_schema",
    # Term validation
    "TermValidator",
    "TermValidationResult",
    # Publication validation
    "PublicationValidator",
    "PublicationValidationResult",
    # Validation reporting
    "ValidationReport",
    "ValidationIssue",
    "ValidationSeverity",
    "BatchValidationReport",
]
