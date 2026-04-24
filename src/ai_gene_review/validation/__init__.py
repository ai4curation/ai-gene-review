"""Validation subpackage for ai-gene-review.

This package contains all validation-related modules:
- CLI tool runners for schema, term, and reference validation
- Custom best-practices checks (Python)
- Validation reporting
"""

from ai_gene_review.validation.validation_report import (
    BatchValidationReport,
    ValidationIssue,
    ValidationReport,
    ValidationSeverity,
)
from ai_gene_review.validation.validator import (
    check_best_practices_rules,
    get_schema_path,
    get_validation_summary,
    load_schema,
    run_reference_validation,
    run_schema_validation,
    run_term_validation,
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
    # CLI tool runners
    "run_schema_validation",
    "run_term_validation",
    "run_reference_validation",
    # Best practices
    "check_best_practices_rules",
    # Validation reporting
    "ValidationReport",
    "ValidationIssue",
    "ValidationSeverity",
    "BatchValidationReport",
]
