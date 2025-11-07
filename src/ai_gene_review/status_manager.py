"""Status management for gene reviews.

This module provides reusable functions to compute and manage the status
of gene reviews based on their annotation states and validation warnings.

Status levels:
- INITIALIZED: All annotations have action PENDING
- IN_PROGRESS: At least one annotation is PENDING and at least one is not PENDING
- DRAFT: No PENDING annotations, but may have validation warnings
- COMPLETE: No PENDING annotations and no validation warnings
"""

from pathlib import Path
from typing import Dict, Any, Optional, Tuple
import yaml

from ai_gene_review.validation import validate_gene_review, ValidationReport


def compute_status_from_data(
    data: Dict[str, Any], validation_report: Optional[ValidationReport] = None
) -> str:
    """Compute the expected status from gene review data.

    Args:
        data: Gene review data dictionary
        validation_report: Optional validation report to check for warnings

    Returns:
        Expected status: INITIALIZED, IN_PROGRESS, DRAFT, or COMPLETE

    Example:
        >>> data = {
        ...     "id": "Q123",
        ...     "gene_symbol": "GENE1",
        ...     "existing_annotations": [
        ...         {"review": {"action": "PENDING"}},
        ...         {"review": {"action": "PENDING"}}
        ...     ]
        ... }
        >>> compute_status_from_data(data)
        'INITIALIZED'
        >>> data["existing_annotations"][0]["review"]["action"] = "ACCEPT"
        >>> compute_status_from_data(data)
        'IN_PROGRESS'
    """
    existing_annotations = data.get("existing_annotations", [])

    if not existing_annotations:
        # No annotations - consider this INITIALIZED
        return "INITIALIZED"

    # Count PENDING annotations
    pending_count = 0
    total_count = len(existing_annotations)

    for annotation in existing_annotations:
        review = annotation.get("review", {})
        action = review.get("action", "")
        if action == "PENDING":
            pending_count += 1

    # Determine status based on PENDING count
    if pending_count == total_count:
        # All are PENDING
        return "INITIALIZED"
    elif pending_count > 0:
        # Some but not all are PENDING
        return "IN_PROGRESS"
    else:
        # No PENDING annotations
        # Check for validation warnings
        if validation_report and validation_report.has_warnings:
            return "DRAFT"
        else:
            return "COMPLETE"


def compute_status_from_file(file_path: Path, check_validation: bool = True) -> Tuple[str, Optional[ValidationReport]]:
    """Compute the expected status from a gene review YAML file.

    Args:
        file_path: Path to the gene review YAML file
        check_validation: Whether to run validation to check for warnings (default: True)

    Returns:
        Tuple of (expected_status, validation_report)

    Example:
        >>> from pathlib import Path
        >>> # status, report = compute_status_from_file(Path("genes/human/GENE/GENE-ai-review.yaml"))
    """
    # Load the YAML data
    with open(file_path, "r") as f:
        data = yaml.safe_load(f)

    # Run validation if requested
    validation_report = None
    if check_validation:
        validation_report = validate_gene_review(file_path, check_best_practices=True)

    # Compute status
    status = compute_status_from_data(data, validation_report)

    return status, validation_report


def check_and_update_status(
    file_path: Path, dry_run: bool = False, verbose: bool = False
) -> Dict[str, Any]:
    """Check the status of a gene review and optionally update it.

    Args:
        file_path: Path to the gene review YAML file
        dry_run: If True, don't actually update the file (default: False)
        verbose: If True, print detailed information (default: False)

    Returns:
        Dictionary with:
            - file: file path
            - current_status: current status in file (or None if not set)
            - expected_status: computed expected status
            - needs_update: whether update is needed
            - status_mismatch: whether there's a mismatch
            - updated: whether file was updated
            - has_warnings: whether validation has warnings
            - validation_warning_count: number of validation warnings

    Example:
        >>> from pathlib import Path
        >>> # result = check_and_update_status(Path("genes/human/GENE/GENE-ai-review.yaml"))
        >>> # if result["status_mismatch"]:
        >>> #     print(f"Mismatch: {result['current_status']} vs {result['expected_status']}")
    """
    # Compute expected status
    expected_status, validation_report = compute_status_from_file(file_path, check_validation=True)

    # Load current data
    with open(file_path, "r") as f:
        data = yaml.safe_load(f)

    current_status = data.get("status")

    # Determine if update is needed
    needs_update = current_status is None
    status_mismatch = current_status is not None and current_status != expected_status

    # Build result
    result = {
        "file": str(file_path),
        "current_status": current_status,
        "expected_status": expected_status,
        "needs_update": needs_update,
        "status_mismatch": status_mismatch,
        "updated": False,
        "has_warnings": validation_report.has_warnings if validation_report else False,
        "validation_warning_count": validation_report.warning_count if validation_report else 0,
    }

    # Update if needed and not dry run
    if needs_update and not dry_run:
        data["status"] = expected_status

        # Write back to file
        with open(file_path, "w") as f:
            yaml.dump(data, f, default_flow_style=False, sort_keys=False, allow_unicode=True)

        result["updated"] = True

        if verbose:
            print(f"Updated {file_path}: status set to {expected_status}")
    elif needs_update and dry_run:
        if verbose:
            print(f"Would update {file_path}: status should be {expected_status}")
    elif status_mismatch:
        if verbose:
            print(f"Mismatch in {file_path}: current={current_status}, expected={expected_status}")

    return result
