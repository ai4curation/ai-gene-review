"""Validation subpackage for ai-gene-review.

Schema, term, and reference validation are handled by CLI tools
(linkml-validate, linkml-term-validator, linkml-reference-validator)
invoked from the justfile.  This package contains only the custom
best-practices checks and validation reporting.
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
    # Best practices
    "check_best_practices_rules",
    # Validation reporting
    "ValidationReport",
    "ValidationIssue",
    "ValidationSeverity",
    "BatchValidationReport",
]
