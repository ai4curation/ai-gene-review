"""Custom best-practices validator for gene review YAML files.

Schema, term, and reference validation are handled by the standard
LinkML CLI tools (``linkml-validate``, ``linkml-term-validator``,
``linkml-reference-validator``) invoked from the justfile.  This
module contains only the domain-specific best-practices checks that
have no upstream equivalent.

Example:
    >>> from ai_gene_review.validation import validate_gene_review
    >>> from pathlib import Path
    >>> # Example usage with a gene review file
    >>> # report = validate_gene_review(Path("genes/human/GENE/GENE-ai-review.yaml"))
    >>> # if report.is_valid:
    >>> #     print("Valid!")
    >>> # else:
    >>> #     print(f"Validation errors: {report.error_count}")
"""

from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple, Callable
import yaml
import time
from contextlib import contextmanager
from functools import lru_cache
from linkml_runtime.utils.schemaview import SchemaView  # type: ignore[import-untyped]

from ai_gene_review.validation.validation_report import (
    ValidationReport,
    ValidationSeverity,
    BatchValidationReport,
)
from ai_gene_review.validation.goa_validator import GOAValidator


@contextmanager
def timer(name: str, callback: Optional[Callable] = None):
    """Context manager for timing operations with optional progress callback."""
    start = time.perf_counter()
    if callback:
        callback(f"{name}...")
    try:
        yield
    finally:
        duration = time.perf_counter() - start
        if callback:
            callback(f"{name} ({duration:.2f}s)")


def get_project_root() -> Path:
    """Get the project root directory (contains conf/, scripts/, genes/).

    Returns:
        Path to the project root
    """
    return Path(__file__).parent.parent.parent.parent


def get_schema_path() -> Path:
    """Get the path to the LinkML schema file.

    Returns:
        Path to the gene_review.yaml schema file
    """
    return Path(__file__).parent.parent / "schema" / "gene_review.yaml"


def load_schema() -> SchemaView:
    """Load the LinkML schema.

    Returns:
        SchemaView object for the gene review schema

    Raises:
        FileNotFoundError: If schema file is not found
    """
    schema_path = get_schema_path()
    if not schema_path.exists():
        raise FileNotFoundError(f"Schema file not found: {schema_path}")

    return SchemaView(str(schema_path))


# ---------------------------------------------------------------------------
# GO branch binding validation (cached)
# ---------------------------------------------------------------------------

# Fields in core_functions -> (dynamic enum name, human-readable branch label)
_BINDING_CHECKS: List[Tuple[str, str, str]] = [
    ("molecular_function", "GOMolecularActivityEnum", "molecular_function"),
    ("contributes_to_molecular_function", "GOMolecularActivityEnum", "molecular_function"),
    ("directly_involved_in", "GOBiologicalProcessEnum", "biological_process"),
    ("locations", "GOCellularLocationEnum", "cellular_component"),
    ("in_complex", "GOProteinContainingComplexEnum", "protein-containing complex"),
]


@lru_cache(maxsize=1)
def _get_expanded_enums() -> Dict[str, set]:
    """Lazily load and cache the expanded dynamic enum sets.

    Uses DynamicEnumPlugin to resolve reachable_from constraints
    (e.g. GOMolecularActivityEnum = all descendants of GO:0003674).
    The result is cached so that batch validation doesn't re-download
    ontology databases for every file.
    """
    from linkml_term_validator.plugins import DynamicEnumPlugin

    schema_path = get_schema_path()
    project_root = get_project_root()
    cache_dir = project_root / "cache"
    oak_config_path = project_root / "conf" / "oak_config.yaml"

    plugin = DynamicEnumPlugin(
        cache_dir=str(cache_dir),
        oak_config_path=str(oak_config_path) if oak_config_path.exists() else None,
    )

    sv = SchemaView(str(schema_path))
    result: Dict[str, set] = {}
    for enum_name in [bc[1] for bc in _BINDING_CHECKS]:
        if enum_name in result:
            continue
        enum_def = sv.get_enum(enum_name)
        if enum_def:
            result[enum_name] = plugin.expand_enum(enum_def, sv)
    return result


def _check_go_branch_bindings(data: Dict[str, Any], report: ValidationReport) -> None:
    """Validate GO branch membership for bindings in core_functions.

    The term validator CLI handles direct slot ranges with dynamic enums,
    but BindingValidationPlugin skips dynamic enums (reachable_from) and
    DynamicEnumPlugin only checks direct ranges, not bindings. This
    function fills that gap.
    """
    if "core_functions" not in data or not data["core_functions"]:
        return

    expanded = _get_expanded_enums()
    if not expanded:
        return

    for i, cf in enumerate(data["core_functions"]):
        if not isinstance(cf, dict):
            continue
        for field, enum_name, branch_label in _BINDING_CHECKS:
            values = cf.get(field)
            if values is None:
                continue
            # Normalize to list (in_complex and molecular_function are single-valued)
            if isinstance(values, dict):
                values = [values]
            if not isinstance(values, list):
                continue
            if enum_name not in expanded:
                continue
            valid_ids = expanded[enum_name]
            for j, val in enumerate(values):
                if isinstance(val, dict) and "id" in val:
                    term_id = val["id"]
                    if term_id not in valid_ids:
                        idx = f"[{j}]" if isinstance(cf.get(field), list) else ""
                        # WARNING not ERROR: the expanded enum depends on which
                        # GO release is cached locally; obsolete terms (like
                        # GO:0005615) will fail here but may be valid in
                        # the GO version the curation was done against.
                        report.add_issue(
                            ValidationSeverity.WARNING,
                            f"Term {term_id} ({val.get('label', '?')}) is not in the {branch_label} branch (expected {enum_name})",
                            path=f"core_functions[{i}].{field}{idx}.id",
                            validation_category="LTVValidator",
                            check_type="go_branch_validation",
                        )


# ---------------------------------------------------------------------------
# Main validation entry points
# ---------------------------------------------------------------------------

def validate_gene_review(
    yaml_file: Path | str,
    schema_path: Optional[Path | str] = None,
    check_best_practices: bool = True,
    check_goa: bool = True,
    check_supporting_text: bool = True,
    progress_callback: Optional[Callable] = None,
) -> ValidationReport:
    """Run custom best-practices checks on a gene review YAML file.

    Schema, term, and reference validation are handled by the standard
    LinkML CLI tools invoked from the justfile.  This function runs only
    the domain-specific checks that have no upstream equivalent.

    Args:
        yaml_file: Path to the YAML file to validate
        schema_path: Unused (kept for backward compatibility)
        check_best_practices: Whether to check for best practices (soft failures)
        check_goa: Whether to validate against GOA file (enabled by default)
        check_supporting_text: Unused (handled by linkml-reference-validator CLI)
        progress_callback: Optional callback function to report progress steps

    Returns:
        ValidationReport with detailed validation results

    Example:
        >>> # Create a test file
        >>> import tempfile, yaml
        >>> from pathlib import Path
        >>> data = {
        ...     "id": "Q12345",
        ...     "gene_symbol": "TEST",
        ...     "taxon": {"id": "NCBITaxon:9606", "label": "Homo sapiens"},
        ...     "description": "A test gene for demonstration purposes"
        ... }
        >>> with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
        ...     yaml.dump(data, f)
        ...     test_file = Path(f.name)
        >>> report = validate_gene_review(test_file)  # doctest: +ELLIPSIS
        ...
        >>> print("Valid!" if report.is_valid else f"Errors: {report.error_count}")
        Valid!
        >>> test_file.unlink()  # Clean up
    """
    yaml_file_path: Path = Path(yaml_file)
    report = ValidationReport(file_path=yaml_file_path, is_valid=True)

    if progress_callback:
        progress_callback("Checking file existence")

    if not yaml_file_path.exists():
        report.add_issue(
            ValidationSeverity.ERROR, f"File not found: {yaml_file_path}", path=None
        )
        return report

    with open(yaml_file_path, "r") as f:
        data = yaml.safe_load(f)

    if check_best_practices:
        if progress_callback:
            progress_callback("Best practices validation")

        check_best_practices_rules(
            data,
            report,
            yaml_file_path if check_goa else None,
            progress_callback=progress_callback,
        )

    return report


def check_best_practices_rules(
    data: Dict[str, Any],
    report: ValidationReport,
    yaml_file: Optional[Path] = None,
    check_supporting_text: bool = True,
    progress_callback: Optional[Callable] = None,
) -> None:
    """Check for best practices and add soft failures (warnings).

    This function contains only the custom domain-specific checks.
    Schema, term-label, and reference/snippet validation are handled
    by the CLI tools invoked from the justfile.

    Args:
        data: The parsed YAML data
        report: ValidationReport to add warnings to
        yaml_file: Path to YAML file for GOA validation (if enabled)
        check_supporting_text: Unused (kept for backward compatibility)
        progress_callback: Optional callback function to report progress steps
    """
    if progress_callback:
        progress_callback("Running best-practices checks")

    # Validate GO branch membership for bindings in core_functions.
    # The term validator CLI handles direct slot ranges, but not bindings
    # with dynamic enums (reachable_from). We check bindings here using
    # a lazily-cached DynamicEnumPlugin instance (shared across files).
    _check_go_branch_bindings(data, report)

    # Check for TODO in description
    if "description" in data and "TODO" in str(data["description"]):
        report.add_issue(
            ValidationSeverity.WARNING,
            "Description contains TODO placeholder",
            path="description",
            suggestion="Complete the gene description",
            validation_category="BestPractices",
            check_type="todo_placeholder",
        )

    # Check for missing references
    if "references" not in data or not data["references"]:
        report.add_issue(
            ValidationSeverity.WARNING,
            "No references provided",
            path="references",
            suggestion="Add relevant literature references",
            validation_category="BestPractices",
            check_type="missing_references",
        )

    # Check that all original_reference_ids in annotations point to valid references
    if "existing_annotations" in data and data["existing_annotations"]:
        # Build set of valid reference IDs
        valid_ref_ids = set()
        if "references" in data and data["references"]:
            for ref in data["references"]:
                if isinstance(ref, dict) and "id" in ref:
                    valid_ref_ids.add(ref["id"])

        # Check each annotation's original_reference_id
        for i, annotation in enumerate(data["existing_annotations"]):
            if isinstance(annotation, dict) and "original_reference_id" in annotation:
                ref_id = annotation["original_reference_id"]
                if ref_id and ref_id not in valid_ref_ids:
                    report.add_issue(
                        ValidationSeverity.ERROR,
                        f"Annotation references non-existent reference ID: {ref_id}",
                        path=f"existing_annotations[{i}].original_reference_id",
                        suggestion=f"Add a reference with ID '{ref_id}' to the references section or correct the reference ID",
                    )

    # Helper function to validate file references
    def validate_file_reference(ref_id: str, path: str) -> None:
        """Validate a file reference and add issues to report if invalid.

        File references are resolved in this order:
        1. Relative to genes/ directory (for gene-specific files like SPECIES/GENE/file.md)
        2. Relative to project root (for shared files like interpro/panther/PTHR10314/notes.md)
        """
        if ref_id.startswith("file:"):
            # Extract the file path after 'file:'
            file_path_str = ref_id[5:]  # Remove 'file:' prefix

            # Check if the file exists relative to the genes directory first,
            # then fall back to project root for shared resources
            genes_path = Path("genes") / file_path_str
            root_path = Path(file_path_str)

            # Determine which path to use
            if genes_path.exists():
                full_path = genes_path
            elif root_path.exists():
                full_path = root_path
            else:
                report.add_issue(
                    ValidationSeverity.ERROR,
                    f"File reference points to non-existent file: {file_path_str}",
                    path=path,
                    suggestion=f"Ensure the file exists at: genes/{file_path_str} or {file_path_str}",
                    validation_category="ReferenceValidator",
                    check_type="file_not_found",
                )
                return

            if not full_path.is_file():
                report.add_issue(
                    ValidationSeverity.ERROR,
                    f"File reference points to a directory, not a file: {file_path_str}",
                    path=path,
                    suggestion="File references must point to actual files, not directories",
                    validation_category="ReferenceValidator",
                    check_type="file_is_directory",
                )

    # Check file: references in main references section
    if "references" in data and data["references"]:
        for i, ref in enumerate(data["references"]):
            if isinstance(ref, dict) and "id" in ref:
                validate_file_reference(ref["id"], f"references[{i}].id")

                # Also check findings.supported_by in references
                findings = ref.get("findings", [])
                for j, finding in enumerate(findings):
                    if isinstance(finding, dict):
                        supported_by_list = finding.get("supported_by", [])
                        for k, sb in enumerate(supported_by_list):
                            if isinstance(sb, dict) and "reference_id" in sb:
                                validate_file_reference(
                                    sb["reference_id"],
                                    f"references[{i}].findings[{j}].supported_by[{k}].reference_id",
                                )

    # Check for PENDING annotations (placeholder state that should be resolved)
    if "existing_annotations" in data and data["existing_annotations"]:
        pending_count = 0
        pending_examples: List[str] = []
        for i, annotation in enumerate(data["existing_annotations"]):
            if isinstance(annotation, dict) and "review" in annotation:
                review = annotation.get("review", {})
                if isinstance(review, dict) and review.get("action") == "PENDING":
                    pending_count += 1
                    if len(pending_examples) < 3:  # Collect first 3 examples
                        term = annotation.get("term", {})
                        term_label = (
                            term.get("label", "unknown")
                            if isinstance(term, dict)
                            else "unknown"
                        )
                        pending_examples.append(f"{term_label}")

        if pending_count > 0:
            examples_text = ", ".join(pending_examples)
            if pending_count > 3:
                examples_text += f" ... and {pending_count - 3} more"
            report.add_issue(
                ValidationSeverity.WARNING,
                f"Review incomplete: {pending_count} annotations marked as PENDING ({examples_text})",
                path="existing_annotations",
                suggestion="Complete the review by resolving PENDING annotations",
                validation_category="BestPractices",
                check_type="pending_annotations",
            )

    # Check for review-term-consistency: all annotations to the same term should have the same action
    if "existing_annotations" in data and data["existing_annotations"]:
        # Build a map from term ID to list of (index, action, evidence_code) tuples
        term_actions: Dict[str, List[Tuple[int, str, str]]] = {}

        for i, annotation in enumerate(data["existing_annotations"]):
            if isinstance(annotation, dict):
                term = annotation.get("term", {})
                if isinstance(term, dict) and "id" in term:
                    term_id = term["id"]

                    review = annotation.get("review", {})
                    if isinstance(review, dict) and "action" in review:
                        action = review["action"]
                        # Skip PENDING actions in consistency check
                        if action == "PENDING":
                            continue
                        evidence_code = annotation.get("evidence_type", "unknown")

                        if term_id not in term_actions:
                            term_actions[term_id] = []
                        term_actions[term_id].append((i, action, evidence_code))

        # Check for inconsistencies
        for term_id, actions_list in term_actions.items():
            if len(actions_list) > 1:
                # Skip consistency check for GO:0005515 (protein binding) as it's a special case
                if term_id == "GO:0005515":
                    continue

                unique_actions = set(action for _, action, _ in actions_list)

                if len(unique_actions) > 1:
                    # Special case: NEW annotations with supported_by are allowed to coexist
                    if "NEW" in unique_actions:
                        new_annotations_valid = True
                        for idx, action, _ in actions_list:
                            if action == "NEW":
                                annotation = data["existing_annotations"][idx]
                                review = annotation.get("review", {})
                                supported_by = review.get("supported_by", [])
                                if not supported_by or len(supported_by) == 0:
                                    new_annotations_valid = False
                                    break

                        if new_annotations_valid:
                            non_new_actions = set(
                                action
                                for _, action, _ in actions_list
                                if action != "NEW"
                            )
                            if len(non_new_actions) <= 1:
                                continue

                    # Get the term label for better error messages
                    term_label = None
                    for annotation in data["existing_annotations"]:
                        if isinstance(annotation, dict):
                            term = annotation.get("term", {})
                            if isinstance(term, dict) and term.get("id") == term_id:
                                term_label = term.get("label", term_id)
                                break

                    action_summary = []
                    for action in sorted(unique_actions):
                        evidence_codes = [
                            ec for _, a, ec in actions_list if a == action
                        ]
                        action_summary.append(f"{action} ({', '.join(evidence_codes)})")

                    report.add_issue(
                        ValidationSeverity.WARNING,
                        f"Inconsistent review actions for term {term_id} ({term_label or 'unknown'}): {'; '.join(action_summary)}",
                        path="existing_annotations",
                        suggestion="All annotations to the same term should have consistent review actions, regardless of evidence type",
                        validation_category="BestPractices",
                        check_type="inconsistent_review_actions",
                    )

    # Check for usage of deep research results (including falcon, gemini, etc.)
    if "existing_annotations" in data and data["existing_annotations"]:
        has_research_support = False

        for annotation in data["existing_annotations"]:
            if isinstance(annotation, dict):
                review = annotation.get("review", {})
                if isinstance(review, dict):
                    supported_by_list = review.get("supported_by", [])
                    for sb in supported_by_list:
                        if isinstance(sb, dict) and "reference_id" in sb:
                            ref_id = sb["reference_id"]
                            if (
                                ref_id.startswith("file:")
                                and "research" in ref_id
                                and ref_id.endswith(".md")
                            ):
                                has_research_support = True
                                break
                    if has_research_support:
                        break

        if not has_research_support:
            if yaml_file is not None:
                research_files = list(yaml_file.parent.glob("*research*.md"))
                if research_files:
                    research_file_names = [
                        f.name for f in research_files[:3]
                    ]
                    examples = ", ".join(research_file_names)
                    if len(research_files) > 3:
                        examples += f" and {len(research_files) - 3} more"

                    report.add_issue(
                        ValidationSeverity.WARNING,
                        f"No annotations reference available deep research files ({examples})",
                        path="existing_annotations",
                        suggestion="Consider using deep research findings to support annotation decisions where relevant",
                        validation_category="BestPractices",
                        check_type="no_deep_research_results",
                    )

    # Check for missing core functions
    if "core_functions" not in data or not data["core_functions"]:
        report.add_issue(
            ValidationSeverity.WARNING,
            "No core functions defined",
            path="core_functions",
            suggestion="Define the core molecular functions of the gene",
            validation_category="BestPractices",
            check_type="missing_core_functions",
        )
    else:
        # Validate that core function terms are properly supported
        accepted_terms = set()
        proposed_replacement_terms = set()
        new_annotation_terms = set()

        if "existing_annotations" in data and data["existing_annotations"]:
            for annotation in data["existing_annotations"]:
                if isinstance(annotation, dict):
                    review = annotation.get("review", {})
                    if isinstance(review, dict):
                        action = review.get("action")

                        if action == "ACCEPT":
                            term = annotation.get("term", {})
                            if isinstance(term, dict) and "id" in term:
                                accepted_terms.add(term["id"])

                        if action == "NEW":
                            term = annotation.get("term", {})
                            if isinstance(term, dict) and "id" in term:
                                new_annotation_terms.add(term["id"])

                        if action == "MODIFY":
                            replacements = review.get("proposed_replacement_terms", [])
                            if replacements:
                                for replacement in replacements:
                                    if (
                                        isinstance(replacement, dict)
                                        and "id" in replacement
                                    ):
                                        proposed_replacement_terms.add(
                                            replacement["id"]
                                        )

        modified_terms = set()
        if "existing_annotations" in data and data["existing_annotations"]:
            for annotation in data["existing_annotations"]:
                if isinstance(annotation, dict):
                    review = annotation.get("review", {})
                    if isinstance(review, dict):
                        action = review.get("action")

                        if action == "MODIFY":
                            term = annotation.get("term", {})
                            if isinstance(term, dict) and "id" in term:
                                term_id = term["id"]
                                if (
                                    term_id not in accepted_terms
                                    and term_id not in proposed_replacement_terms
                                ):
                                    modified_terms.add(term_id)

        core_function_terms = set()

        for i, core_func in enumerate(data["core_functions"]):
            if isinstance(core_func, dict):
                # Get the molecular_function term
                mol_func = core_func.get("molecular_function", {})
                if isinstance(mol_func, dict) and "id" in mol_func:
                    term_id = mol_func["id"]
                    term_label = mol_func.get("label", term_id)
                    core_function_terms.add(term_id)

                    is_from_annotations = (
                        term_id in accepted_terms
                        or term_id in new_annotation_terms
                        or term_id in proposed_replacement_terms
                    )

                    supported_by = core_func.get("supported_by", [])
                    has_support = bool(supported_by)

                    # Validate file references in supported_by
                    for j, sb in enumerate(supported_by):
                        if isinstance(sb, dict) and "reference_id" in sb:
                            validate_file_reference(
                                sb["reference_id"],
                                f"core_functions[{i}].supported_by[{j}].reference_id",
                            )

                    if not is_from_annotations and not has_support:
                        report.add_issue(
                            ValidationSeverity.ERROR,
                            f"Core function term {term_id} ({term_label}) is not from an ACCEPTED/NEW annotation and lacks supported_by references",
                            path=f"core_functions[{i}].molecular_function",
                            suggestion="Either use a term from ACCEPTED/NEW existing annotations/proposed replacements, or add supported_by references",
                        )

                    if not is_from_annotations and has_support:
                        report.add_issue(
                            ValidationSeverity.WARNING,
                            f"Core function term {term_id} ({term_label}) is not reflected in existing_annotations block",
                            path=f"core_functions[{i}].molecular_function",
                            suggestion="Consider adding this term to existing_annotations with action: NEW if it's a novel annotation",
                            validation_category="BestPractices",
                            check_type="core_function_molecular_function_not_in_annotations",
                        )

                # Check locations field (should be CC terms)
                locations = core_func.get("locations", [])
                for j, location in enumerate(locations):
                    if isinstance(location, dict) and "id" in location:
                        loc_id = location["id"]
                        loc_label = location.get("label", loc_id)
                        core_function_terms.add(loc_id)

                        if loc_id in modified_terms:
                            report.add_issue(
                                ValidationSeverity.ERROR,
                                f"Location term {loc_id} ({loc_label}) was marked for MODIFY and should not be used directly",
                                path=f"core_functions[{i}].locations[{j}]",
                                suggestion="Use the proposed replacement term instead of the original term marked for modification",
                            )
                            continue

                        is_from_annotations = (
                            loc_id in accepted_terms
                            or loc_id in new_annotation_terms
                            or loc_id in proposed_replacement_terms
                        )

                        supported_by = core_func.get("supported_by", [])
                        has_support = bool(supported_by)

                        if not is_from_annotations and not has_support:
                            report.add_issue(
                                ValidationSeverity.ERROR,
                                f"Location term {loc_id} ({loc_label}) is not from an ACCEPTED/NEW annotation and the core function lacks supported_by references",
                                path=f"core_functions[{i}].locations[{j}]",
                                suggestion="Either use a location from ACCEPTED/NEW existing annotations/proposed replacements, or add supported_by references to the core function",
                            )

                        if not is_from_annotations and has_support:
                            report.add_issue(
                                ValidationSeverity.WARNING,
                                f"Location term {loc_id} ({loc_label}) is not reflected in existing_annotations block",
                                path=f"core_functions[{i}].locations[{j}]",
                                suggestion="Consider adding this term to existing_annotations with action: NEW if it's a novel annotation",
                                validation_category="BestPractices",
                                check_type="core_function_location_not_in_annotations",
                            )

                # Check directly_involved_in field (should be BP terms)
                directly_involved = core_func.get("directly_involved_in", [])
                for j, process in enumerate(directly_involved):
                    if isinstance(process, dict) and "id" in process:
                        proc_id = process["id"]
                        proc_label = process.get("label", proc_id)
                        core_function_terms.add(proc_id)

                        is_from_annotations = (
                            proc_id in accepted_terms
                            or proc_id in new_annotation_terms
                            or proc_id in proposed_replacement_terms
                        )

                        supported_by = core_func.get("supported_by", [])
                        has_support = bool(supported_by)

                        if not is_from_annotations and not has_support:
                            report.add_issue(
                                ValidationSeverity.ERROR,
                                f"Process term {proc_id} ({proc_label}) is not from an ACCEPTED/NEW annotation and the core function lacks supported_by references",
                                path=f"core_functions[{i}].directly_involved_in[{j}]",
                                suggestion="Either use a process from ACCEPTED/NEW existing annotations/proposed replacements, or add supported_by references to the core function",
                            )

                        if not is_from_annotations and has_support:
                            report.add_issue(
                                ValidationSeverity.WARNING,
                                f"Process term {proc_id} ({proc_label}) is not reflected in existing_annotations block",
                                path=f"core_functions[{i}].directly_involved_in[{j}]",
                                suggestion="Consider adding this term to existing_annotations with action: NEW if it's a novel annotation",
                                validation_category="BestPractices",
                                check_type="core_function_process_not_in_annotations",
                            )

                # Check in_complex field
                in_complex = core_func.get("in_complex")
                if isinstance(in_complex, dict) and "id" in in_complex:
                    complex_id = in_complex["id"]
                    complex_label = in_complex.get("label", complex_id)
                    core_function_terms.add(complex_id)

                    is_from_annotations = (
                        complex_id in accepted_terms
                        or complex_id in new_annotation_terms
                        or complex_id in proposed_replacement_terms
                    )

                    supported_by = core_func.get("supported_by", [])
                    has_support = bool(supported_by)

                    if not is_from_annotations and not has_support:
                        report.add_issue(
                            ValidationSeverity.ERROR,
                            f"Complex term {complex_id} ({complex_label}) is not from an ACCEPTED/NEW annotation and the core function lacks supported_by references",
                            path=f"core_functions[{i}].in_complex",
                            suggestion="Either use a complex from ACCEPTED/NEW existing annotations/proposed replacements, or add supported_by references to the core function",
                        )

                    if not is_from_annotations and has_support:
                        report.add_issue(
                            ValidationSeverity.WARNING,
                            f"Complex term {complex_id} ({complex_label}) is not reflected in existing_annotations block",
                            path=f"core_functions[{i}].in_complex",
                            suggestion="Consider adding this term to existing_annotations with action: NEW if it's a novel annotation",
                        )

    # Check for file references in existing_annotations.review.supported_by
    if "existing_annotations" in data and data["existing_annotations"]:
        for i, annotation in enumerate(data["existing_annotations"]):
            if isinstance(annotation, dict):
                review = annotation.get("review", {})
                if isinstance(review, dict):
                    supported_by_list = review.get("supported_by", [])
                    for j, sb in enumerate(supported_by_list):
                        if isinstance(sb, dict) and "reference_id" in sb:
                            validate_file_reference(
                                sb["reference_id"],
                                f"existing_annotations[{i}].review.supported_by[{j}].reference_id",
                            )

    # Check for ACCEPT annotations with PMIDs lacking supported_by
    # Only warn if the publication file exists (full text is available)
    if "existing_annotations" in data and data["existing_annotations"]:
        for i, annotation in enumerate(data["existing_annotations"]):
            if isinstance(annotation, dict):
                review = annotation.get("review", {})
                if isinstance(review, dict) and review.get("action") == "ACCEPT":
                    ref_id = annotation.get("original_reference_id", "")
                    if ref_id and ref_id.startswith("PMID:"):
                        supported_by = review.get("supported_by", [])
                        if not supported_by:
                            pmid_number = ref_id.replace("PMID:", "")
                            if yaml_file is not None:
                                project_root = yaml_file.parent
                                while (
                                    project_root.parent != project_root
                                    and not (project_root / "publications").exists()
                                ):
                                    project_root = project_root.parent
                                pub_file = (
                                    project_root
                                    / "publications"
                                    / f"PMID_{pmid_number}.md"
                                )
                            else:
                                pub_file = (
                                    Path("publications") / f"PMID_{pmid_number}.md"
                                )

                            full_text_available = False
                            if pub_file.exists():
                                import yaml as yaml_lib

                                with open(pub_file, "r") as f:
                                    content = f.read()
                                    if content.startswith("---"):
                                        end_marker = content.find("---", 3)
                                        if end_marker != -1:
                                            frontmatter = content[3:end_marker]
                                            pub_data = yaml_lib.safe_load(
                                                frontmatter
                                            )
                                            full_text_available = pub_data.get(
                                                "full_text_available", False
                                            )

                            if full_text_available:
                                report.add_issue(
                                    ValidationSeverity.WARNING,
                                    f"ACCEPT annotation with {ref_id} lacks supported_by references",
                                    path=f"existing_annotations[{i}].review.supported_by",
                                    suggestion=f"Add supported_by with reference_id and supporting_text from {ref_id}",
                                )

    # Check for incomplete taxon information
    if "taxon" in data:
        taxon = data["taxon"]
        if isinstance(taxon, dict):
            if "id" in taxon and not taxon["id"].startswith("NCBITaxon:"):
                report.add_issue(
                    ValidationSeverity.INFO,
                    "Taxon ID should use NCBITaxon prefix",
                    path="taxon.id",
                    suggestion=f"Use 'NCBITaxon:{taxon['id']}' format",
                )

    # Check description length
    if "description" in data and len(str(data["description"])) < 20:
        report.add_issue(
            ValidationSeverity.WARNING,
            "Description is very short",
            path="description",
            suggestion="Provide a more detailed description of the gene",
        )

    # Validate against GOA file if enabled
    if yaml_file is not None and "existing_annotations" in data:
        if progress_callback:
            progress_callback("Validating against GOA")
        goa_validator = GOAValidator()
        goa_result = goa_validator.validate_against_goa(yaml_file)

        if not goa_result.is_valid:
            if goa_result.error_message:
                report.add_issue(
                    ValidationSeverity.WARNING,
                    f"GOA validation: {goa_result.error_message}",
                    path="existing_annotations",
                )

            if goa_result.missing_in_yaml:
                missing_count = len(goa_result.missing_in_yaml)
                missing_examples: List[str] = []
                for ann in goa_result.missing_in_yaml[:5]:
                    missing_examples.append(
                        f"{ann.go_id} ({ann.go_term}) - {ann.evidence_code} - {ann.reference}"
                    )

                if missing_count <= 5:
                    detail = ": " + "; ".join(missing_examples)
                else:
                    detail = (
                        " (showing first 5): "
                        + "; ".join(missing_examples)
                        + f" ... and {missing_count - 5} more"
                    )

                report.add_issue(
                    ValidationSeverity.ERROR,
                    f"Missing {missing_count} annotations from GOA{detail}",
                    path="existing_annotations",
                    suggestion="Review GOA file and add missing annotations or document why they were excluded",
                )

            if goa_result.missing_in_goa:
                missing_count = len(goa_result.missing_in_goa)
                extra_examples: List[str] = []
                for ann_dict in goa_result.missing_in_goa[:5]:
                    go_id = ann_dict.get("term", {}).get("id", "unknown")
                    go_label = ann_dict.get("term", {}).get("label", "unknown")
                    evidence = ann_dict.get("evidence_type", "unknown")
                    ref = ann_dict.get("original_reference_id", "unknown")
                    extra_examples.append(f"{go_id} ({go_label}) - {evidence} - {ref}")

                if missing_count <= 5:
                    detail = ": " + "; ".join(extra_examples)
                else:
                    detail = (
                        " (showing first 5): "
                        + "; ".join(extra_examples)
                        + f" ... and {missing_count - 5} more"
                    )

                report.add_issue(
                    ValidationSeverity.ERROR,
                    f"Found {missing_count} annotations not in GOA{detail}",
                    path="existing_annotations",
                    suggestion="Verify these annotations are correct or remove if not supported by GOA",
                )

            if goa_result.mismatched_evidence:
                report.add_issue(
                    ValidationSeverity.WARNING,
                    f"Found {len(goa_result.mismatched_evidence)} evidence type mismatches with GOA file",
                    path="existing_annotations",
                    suggestion="Consider updating evidence types to match GOA file",
                )


def validate_multiple_files(
    yaml_files: List[Path | str],
    schema_path: Optional[Path | str] = None,
    check_best_practices: bool = True,
    check_goa: bool = True,
    check_supporting_text: bool = True,
    show_progress: bool = False,
) -> BatchValidationReport:
    """Validate multiple gene review YAML files.

    Args:
        yaml_files: List of paths to YAML files
        schema_path: Unused (kept for backward compatibility)
        check_best_practices: Whether to check for best practices
        check_goa: Whether to validate against GOA files
        check_supporting_text: Unused (handled by linkml-reference-validator CLI)
        show_progress: Whether to show a progress bar for multiple files

    Returns:
        BatchValidationReport with results for all files

    Example:
        >>> # Create test files
        >>> import tempfile, yaml
        >>> from pathlib import Path
        >>> files = []
        >>> for i in range(2):
        ...     data = {
        ...         "id": f"Q{i}",
        ...         "gene_symbol": f"TEST{i}",
        ...         "taxon": {"id": "NCBITaxon:9606", "label": "Homo sapiens"},
        ...         "description": f"Test gene {i}"
        ...     }
        ...     with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
        ...         yaml.dump(data, f)
        ...         files.append(Path(f.name))
        >>> batch_report = validate_multiple_files(files)  # doctest: +ELLIPSIS
        ...
        >>> print(f"Valid: {batch_report.valid_files}, Invalid: {batch_report.invalid_files}")
        Valid: 2, Invalid: 0
        >>> for f in files:
        ...     f.unlink()  # Clean up
    """
    batch_report = BatchValidationReport()

    if show_progress and len(yaml_files) > 1:
        from rich.progress import (
            Progress,
            SpinnerColumn,
            TextColumn,
            BarColumn,
            TaskProgressColumn,
            TimeElapsedColumn,
        )

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TaskProgressColumn(),
            TimeElapsedColumn(),
            console=None,
        ) as progress:
            main_task = progress.add_task("Validating files...", total=len(yaml_files))

            for yaml_file in yaml_files:
                yaml_file_path = Path(yaml_file)
                progress.update(
                    main_task, description=f"Validating {yaml_file_path.name}"
                )

                def step_callback(step: str):
                    progress.update(
                        main_task, description=f"{yaml_file_path.name}: {step}"
                    )

                report = validate_gene_review(
                    yaml_file_path,
                    schema_path,
                    check_best_practices,
                    check_goa,
                    check_supporting_text,
                    progress_callback=step_callback,
                )
                batch_report.reports.append(report)
                progress.advance(main_task)
    else:
        for yaml_file in yaml_files:
            yaml_file = Path(yaml_file)
            report = validate_gene_review(
                yaml_file,
                schema_path,
                check_best_practices,
                check_goa,
                check_supporting_text,
            )
            batch_report.reports.append(report)

    return batch_report


def get_validation_summary(results: Dict[str, Tuple[bool, List[str]]]) -> str:
    """Legacy function for backward compatibility.

    Args:
        results: Dictionary from old validate_multiple_files

    Returns:
        Human-readable summary string
    """
    batch_report = BatchValidationReport()

    for file_path, (is_valid, errors) in results.items():
        report = ValidationReport(file_path=Path(file_path), is_valid=is_valid)
        for error in errors:
            report.add_issue(ValidationSeverity.ERROR, error)
        batch_report.reports.append(report)

    return batch_report.summary()


def validate_rule_review(
    yaml_file: Path | str,
    schema_path: Optional[Path | str] = None,
    check_publications: bool = True,
    progress_callback: Optional[Callable] = None,
) -> ValidationReport:
    """Validate a rule review YAML file.

    Schema and reference validation are handled by the CLI tools
    invoked from the justfile.  This is a minimal stub that checks
    file existence.

    Args:
        yaml_file: Path to the YAML file to validate
        schema_path: Unused (kept for backward compatibility)
        check_publications: Unused (handled by linkml-reference-validator CLI)
        progress_callback: Optional callback function to report progress steps

    Returns:
        ValidationReport with detailed validation results

    Example:
        >>> # Example: validate_rule_review(Path("rules/reviews/ARBA00026249-review.yaml"))
    """
    yaml_file_path: Path = Path(yaml_file)
    report = ValidationReport(file_path=yaml_file_path, is_valid=True)

    if not yaml_file_path.exists():
        report.add_issue(
            ValidationSeverity.ERROR, f"File not found: {yaml_file_path}", path=None
        )

    return report
