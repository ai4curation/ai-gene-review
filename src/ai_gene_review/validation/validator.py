"""Validator for gene review YAML files using LinkML schema.

This module provides functionality to validate gene review YAML files
against the LinkML schema defined in schema/gene_review.yaml.

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
import re
import traceback
import time
from contextlib import contextmanager
from linkml_runtime.utils.schemaview import SchemaView  # type: ignore[import-untyped]
from linkml.validators.jsonschemavalidator import JsonSchemaDataValidator  # type: ignore[import-untyped]

from ai_gene_review.validation.validation_report import (
    ValidationReport,
    ValidationSeverity,
    BatchValidationReport,
)
from ai_gene_review.validation.term_validator import TermValidator
from ai_gene_review.validation.publication_validator import PublicationValidator

# Import linkml-term-validator plugins for ontology term validation
from linkml.validator import Validator as LinkMLValidator
from linkml_term_validator.plugins import BindingValidationPlugin
from ai_gene_review.validation.goa_validator import GOAValidator
from ai_gene_review.validation.supporting_text_validator import (
    SupportingTextValidator,
    SupportingTextSubstringValidator,
)


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


def validate_gene_review(
    yaml_file: Path | str,
    schema_path: Optional[Path | str] = None,
    check_best_practices: bool = True,
    check_goa: bool = True,
    check_supporting_text: bool = True,
    progress_callback: Optional[Callable] = None,
) -> ValidationReport:
    """Validate a gene review YAML file against the LinkML schema.

    Args:
        yaml_file: Path to the YAML file to validate
        schema_path: Optional path to schema file (uses default if not provided)
        check_best_practices: Whether to check for best practices (soft failures)
        check_goa: Whether to validate against GOA file (enabled by default)
        check_supporting_text: Whether to validate supporting_text against cached publications
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

    # Check if file exists
    if not yaml_file_path.exists():
        report.add_issue(
            ValidationSeverity.ERROR, f"File not found: {yaml_file_path}", path=None
        )
        return report

    try:
        if progress_callback:
            progress_callback("Loading schema")

        # Load schema
        if schema_path:
            schema_path_obj = Path(schema_path)
            if not schema_path_obj.exists():
                report.add_issue(
                    ValidationSeverity.ERROR,
                    f"Schema file not found: {schema_path_obj}",
                    path=None,
                )
                return report
            SchemaView(str(schema_path_obj))  # Validate schema can be loaded
            schema_path = schema_path_obj  # Update schema_path to Path object
        else:
            load_schema()  # Validate schema can be loaded

        if progress_callback:
            progress_callback("Parsing YAML")

        # Load YAML data
        with open(yaml_file_path, "r") as f:
            data = yaml.safe_load(f)

        if progress_callback:
            progress_callback("Schema validation")

        # Create validator
        validator = JsonSchemaDataValidator(str(schema_path or get_schema_path()))

        # Validate against schema
        linkml_report = validator.validate_dict(data, target_class="GeneReview")

        # Process LinkML validation results
        if linkml_report and linkml_report.results:
            for result in linkml_report.results:
                # Extract error message and path
                message = result.message if hasattr(result, "message") else str(result)

                # Try to extract JSON path from message
                path_match = re.search(r"in \$\.(.+)$", message)
                path = path_match.group(1) if path_match else None

                # Schema validation errors are hard failures
                report.add_issue(
                    ValidationSeverity.ERROR,
                    message,
                    path=path,
                    validation_category="SchemaValidator",
                    check_type="schema_validation"
                )

        # Check best practices if enabled and no hard errors
        if check_best_practices and not report.has_errors:
            if progress_callback:
                progress_callback("Best practices validation")
            check_best_practices_rules(
                data, report, yaml_file_path if check_goa else None, check_supporting_text, progress_callback
            )

        return report

    except yaml.YAMLError as e:
        report.add_issue(
            ValidationSeverity.ERROR, f"YAML parsing error: {str(e)}", path=None
        )
        return report
    except FileNotFoundError as e:
        report.add_issue(ValidationSeverity.ERROR, f"File error: {str(e)}", path=None)
        return report
    except ImportError as e:
        report.add_issue(
            ValidationSeverity.ERROR,
            f"Import error (check dependencies): {str(e)}",
            path=None,
        )
        return report
    except Exception as e:
        # For debugging: include the exception type
        error_type = type(e).__name__
        tb = traceback.format_exc()
        # Only show the last line of traceback to avoid clutter
        last_tb_line = tb.strip().split("\n")[-1] if tb else ""
        report.add_issue(
            ValidationSeverity.ERROR,
            f"Validation error ({error_type}): {str(e)} - {last_tb_line}",
            path=None,
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

    Args:
        data: The parsed YAML data
        report: ValidationReport to add warnings to
        yaml_file: Path to YAML file for GOA validation (if enabled)
        check_supporting_text: Whether to validate supporting_text against publications
        progress_callback: Optional callback function to report progress steps
    """
    if progress_callback:
        progress_callback("Validating ontology terms")

    # Use linkml-term-validator plugins for term validation
    # These provide three-tier caching (in-memory → file-based CSV → lazy OAK)
    # and validate against dynamic enums defined in the schema
    schema_path = get_schema_path()
    cache_dir = schema_path.parent.parent.parent.parent / "cache"  # project root/cache

    # Note: DynamicEnumPlugin is intentionally omitted here because:
    # 1. It's very slow (~7s) as it queries OAK for all GO descendants on every run
    # 2. GO branch validation is already handled by the legacy TermValidator below,
    #    which uses a persistent pickle cache for descendants
    # 3. BindingValidationPlugin handles label validation for all terms
    #
    # The oak_config.yaml file specifies which prefixes to skip (TEMP, PMID, etc.)
    # to avoid 404 errors when trying to download non-existent ontologies
    oak_config_path = schema_path.parent.parent.parent.parent / "config" / "oak_config.yaml"
    term_validation_plugins = [
        BindingValidationPlugin(
            validate_labels=True,
            cache_dir=str(cache_dir),
            oak_config_path=str(oak_config_path) if oak_config_path.exists() else None,
        ),
    ]

    term_validator = LinkMLValidator(
        schema=str(schema_path),
        validation_plugins=term_validation_plugins,
    )

    # Validate the data using linkml-term-validator
    term_report = term_validator.validate(data, target_class="GeneReview")

    # Process results from linkml-term-validator
    if term_report and term_report.results:
        for result in term_report.results:
            message = result.message if hasattr(result, "message") else str(result)
            severity_str = result.severity.name if hasattr(result, "severity") else "ERROR"

            # Map severity
            if severity_str == "WARNING":
                severity = ValidationSeverity.WARNING
            elif severity_str == "INFO":
                severity = ValidationSeverity.INFO
            else:
                severity = ValidationSeverity.ERROR

            report.add_issue(
                severity,
                message,
                path=result.source_path if hasattr(result, "source_path") else None,
                validation_category="TermValidator",
                check_type="term_validation"
            )

    # GO branch validation for core_functions
    # This is needed because linkml-term-validator's BindingValidationPlugin skips
    # dynamic enums (those with reachable_from), expecting DynamicEnumPlugin to handle
    # them. But DynamicEnumPlugin only checks direct slot ranges, not bindings.
    # So bindings referencing dynamic enums are not validated by either plugin.
    # TODO: Fix this gap in linkml-term-validator library
    legacy_term_validator = TermValidator()
    core_function_results = legacy_term_validator.validate_terms_in_core_functions(data)
    for result in core_function_results:
        if not result.is_valid and result.error_message:
            # Only report branch errors (label mismatches are already handled by BindingValidationPlugin)
            if "branch but should be in" in result.error_message:
                report.add_issue(
                    ValidationSeverity.ERROR,
                    result.error_message,
                    path=result.path,
                    validation_category="TermValidator",
                    check_type="go_branch_validation"
                )

    # Check for obsolete terms and unrecognized prefixes using persistent cache only (no OAK fallback)
    # This avoids triggering OAK downloads for obsolete checking
    legacy_validator = TermValidator()
    legacy_validator._load_persistent_cache()  # Ensure cache is loaded

    # Use the legacy validator's EXCLUDED_PREFIXES set to avoid duplication
    # This includes PMID, PMC, DOI, UniProt, PDB, EC, Reactome, etc.
    SKIP_PREFIX_VALIDATION = legacy_validator.EXCLUDED_PREFIXES

    # Extract all term IDs from the data
    def extract_term_ids(obj: Any, path: str = "") -> List[Tuple[str, str, bool]]:
        """Extract (term_id, path, is_known_prefix) tuples from nested data."""
        results = []
        if isinstance(obj, dict):
            if "id" in obj and isinstance(obj["id"], str) and ":" in obj["id"]:
                term_id = obj["id"]
                prefix = term_id.split(":")[0]
                # Skip non-ontology prefixes
                if prefix not in SKIP_PREFIX_VALIDATION:
                    is_known = prefix in legacy_validator.ONTOLOGY_MAP
                    results.append((term_id, path, is_known))
            for key, value in obj.items():
                new_path = f"{path}.{key}" if path else key
                results.extend(extract_term_ids(value, new_path))
        elif isinstance(obj, list):
            for i, item in enumerate(obj):
                results.extend(extract_term_ids(item, f"{path}[{i}]"))
        return results

    for term_id, path, is_known_prefix in extract_term_ids(data):
        prefix = term_id.split(":")[0]

        # Check for unrecognized prefixes
        if not is_known_prefix:
            report.add_issue(
                ValidationSeverity.ERROR,
                f"Unrecognized identifier prefix '{prefix}' in {term_id}. Valid ontology prefixes are: {', '.join(sorted(legacy_validator.ONTOLOGY_MAP.keys()))}",
                path=path,
                validation_category="TermValidator",
                check_type="unrecognized_prefix"
            )
            continue  # Skip further checks for unknown prefixes

        # Only check persistent cache for obsolete status
        if term_id in legacy_validator._persistent_cache:
            if legacy_validator._persistent_cache[term_id].get("is_obsolete", False):
                report.add_issue(
                    ValidationSeverity.WARNING,
                    f"Term {term_id} is obsolete",
                    path=path,
                    suggestion="Consider using a non-obsolete term",
                    validation_category="TermValidator",
                    check_type="obsolete_term"
                )

    if progress_callback:
        progress_callback("Validating publications")

    # Validate publication references
    pub_validator = PublicationValidator()
    pub_results = pub_validator.validate_publications_in_data(data)

    for pub_result in pub_results:
        if not pub_result.is_valid:
            # Determine severity based on the error
            if pub_result.correct_title is None:
                # Could not find publication - this is a warning since it might be a network issue
                severity = ValidationSeverity.WARNING
                suggestion = "Check if PMID is correct or fetch the publication"
            else:
                # Title mismatch - this is an error
                severity = ValidationSeverity.ERROR
                suggestion = f"Use correct title: '{pub_result.correct_title}'"

            report.add_issue(
                severity,
                pub_result.error_message
                or f"Invalid publication: PMID:{pub_result.pmid}",
                path=pub_result.path,
                suggestion=suggestion,
            )
    # Check for TODO in description
    if "description" in data and "TODO" in str(data["description"]):
        report.add_issue(
            ValidationSeverity.WARNING,
            "Description contains TODO placeholder",
            path="description",
            suggestion="Complete the gene description",
            validation_category="BestPractices",
            check_type="todo_placeholder"
        )

    # Check for missing optional but recommended fields
    if "aliases" not in data:
        report.add_issue(
            ValidationSeverity.INFO,
            "No aliases provided for the gene",
            path="aliases",
            suggestion="Consider adding known gene aliases if available",
            validation_category="BestPractices",
            check_type="missing_aliases"
        )

    # Check for missing references
    if "references" not in data or not data["references"]:
        report.add_issue(
            ValidationSeverity.WARNING,
            "No references provided",
            path="references",
            suggestion="Add relevant literature references",
            validation_category="BestPractices",
            check_type="missing_references"
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
        """Validate a file reference and add issues to report if invalid."""
        if ref_id.startswith("file:"):
            # Extract the file path after 'file:'
            file_path_str = ref_id[5:]  # Remove 'file:' prefix

            # Check if the file exists relative to the genes directory
            # Assuming validation is run from project root
            base_path = Path("genes")
            full_path = base_path / file_path_str

            if not full_path.exists():
                report.add_issue(
                    ValidationSeverity.ERROR,
                    f"File reference points to non-existent file: {file_path_str}",
                    path=path,
                    suggestion=f"Ensure the file exists at: genes/{file_path_str}",
                    validation_category="ReferenceValidator",
                    check_type="file_not_found"
                )
            elif not full_path.is_file():
                report.add_issue(
                    ValidationSeverity.ERROR,
                    f"File reference points to a directory, not a file: {file_path_str}",
                    path=path,
                    suggestion="File references must point to actual files, not directories",
                    validation_category="ReferenceValidator",
                    check_type="file_is_directory"
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
                                    f"references[{i}].findings[{j}].supported_by[{k}].reference_id"
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
                        term_label = term.get("label", "unknown") if isinstance(term, dict) else "unknown"
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
                check_type="pending_annotations"
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
                    term_label = term.get("label", term_id)

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
                # that typically requires with/extensions to be meaningful
                if term_id == "GO:0005515":
                    continue

                # Get unique actions for this term (excluding PENDING which are already filtered out)
                unique_actions = set(action for _, action, _ in actions_list)

                # If there are different actions for the same term, check if it's a valid case
                if len(unique_actions) > 1:
                    # Special case: NEW annotations with supported_by are allowed to coexist
                    # with existing annotations (ACCEPT/MODIFY/REMOVE/etc.)
                    # This is because NEW represents novel curator-proposed annotations, not existing GOA annotations
                    if "NEW" in unique_actions:
                        # Check if all NEW annotations have supporting evidence
                        new_annotations_valid = True
                        for idx, action, _ in actions_list:
                            if action == "NEW":
                                annotation = data["existing_annotations"][idx]
                                review = annotation.get("review", {})
                                supported_by = review.get("supported_by", [])
                                if not supported_by or len(supported_by) == 0:
                                    new_annotations_valid = False
                                    break

                        # If all NEW annotations have supporting evidence, exclude them from inconsistency check
                        if new_annotations_valid:
                            # Filter out NEW actions and recheck
                            non_new_actions = set(action for _, action, _ in actions_list if action != "NEW")
                            if len(non_new_actions) <= 1:
                                # No inconsistency among non-NEW annotations
                                continue
                    # Get the term label for better error messages
                    term_label = None
                    for annotation in data["existing_annotations"]:
                        if isinstance(annotation, dict):
                            term = annotation.get("term", {})
                            if isinstance(term, dict) and term.get("id") == term_id:
                                term_label = term.get("label", term_id)
                                break

                    # Build a summary of the conflicting actions
                    action_summary = []
                    for action in sorted(unique_actions):
                        evidence_codes = [ec for _, a, ec in actions_list if a == action]
                        action_summary.append(f"{action} ({', '.join(evidence_codes)})")

                    report.add_issue(
                        ValidationSeverity.WARNING,
                        f"Inconsistent review actions for term {term_id} ({term_label or 'unknown'}): {'; '.join(action_summary)}",
                        path="existing_annotations",
                        suggestion="All annotations to the same term should have consistent review actions, regardless of evidence type",
                        validation_category="BestPractices",
                        check_type="inconsistent_review_actions"
                    )
    
    # Check for usage of deep research results (including falcon, gemini, etc.)
    if "existing_annotations" in data and data["existing_annotations"]:
        # Check if any annotation uses ANY research files (pattern: *research*.md)
        has_research_support = False

        for annotation in data["existing_annotations"]:
            if isinstance(annotation, dict):
                review = annotation.get("review", {})
                if isinstance(review, dict):
                    supported_by_list = review.get("supported_by", [])
                    for sb in supported_by_list:
                        if isinstance(sb, dict) and "reference_id" in sb:
                            ref_id = sb["reference_id"]
                            # Check if this references ANY research file (pattern: *research*.md)
                            # This includes deep-research, falcon-research, gemini-research, etc.
                            if ref_id.startswith("file:") and "research" in ref_id and ref_id.endswith(".md"):
                                has_research_support = True
                                break
                    if has_research_support:
                        break

        if not has_research_support:
            # Check if ANY research files exist for this gene
            if yaml_file is not None:
                # Look for ANY *research*.md files in the same directory as the YAML file
                research_files = list(yaml_file.parent.glob("*research*.md"))
                if research_files:
                    # Found research files but NONE are referenced
                    research_file_names = [f.name for f in research_files[:3]]  # Show up to 3 examples
                    examples = ", ".join(research_file_names)
                    if len(research_files) > 3:
                        examples += f" and {len(research_files) - 3} more"

                    report.add_issue(
                        ValidationSeverity.WARNING,
                        f"No annotations reference available deep research files ({examples})",
                        path="existing_annotations",
                        suggestion="Consider using deep research findings to support annotation decisions where relevant",
                        validation_category="BestPractices",
                        check_type="no_deep_research_results"
                    )

    # Check for missing core functions
    if "core_functions" not in data or not data["core_functions"]:
        report.add_issue(
            ValidationSeverity.WARNING,
            "No core functions defined",
            path="core_functions",
            suggestion="Define the core molecular functions of the gene",
            validation_category="BestPractices",
            check_type="missing_core_functions"
        )
    else:
        # Validate that core function terms are properly supported
        # Build set of accepted GO terms from existing_annotations
        accepted_terms = set()
        proposed_replacement_terms = set()
        new_annotation_terms = set()  # Terms from NEW action annotations

        # First pass: collect all ACCEPTED terms, NEW terms, and proposed replacements
        if "existing_annotations" in data and data["existing_annotations"]:
            for annotation in data["existing_annotations"]:
                if isinstance(annotation, dict):
                    review = annotation.get("review", {})
                    if isinstance(review, dict):
                        action = review.get("action")

                        # Collect ACCEPTED terms
                        if action == "ACCEPT":
                            term = annotation.get("term", {})
                            if isinstance(term, dict) and "id" in term:
                                accepted_terms.add(term["id"])

                        # Collect NEW terms (these are proposed new annotations)
                        if action == "NEW":
                            term = annotation.get("term", {})
                            if isinstance(term, dict) and "id" in term:
                                new_annotation_terms.add(term["id"])

                        # Collect proposed replacement terms from MODIFY actions
                        if action == "MODIFY":
                            replacements = review.get("proposed_replacement_terms", [])
                            if replacements:
                                for replacement in replacements:
                                    if isinstance(replacement, dict) and "id" in replacement:
                                        proposed_replacement_terms.add(replacement["id"])
        
        # Second pass: identify terms that should NOT be used
        # A term should not be used ONLY if:
        # 1. It has at least one MODIFY action AND
        # 2. It has NO ACCEPT actions AND  
        # 3. It's not a proposed replacement for something else
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
                                # Only mark as "should not use" if it's not accepted elsewhere
                                # and not a proposed replacement
                                if (term_id not in accepted_terms and 
                                    term_id not in proposed_replacement_terms):
                                    modified_terms.add(term_id)
        
        # Collect all GO terms used in core_functions for cross-checking
        core_function_terms = set()

        # Now check each core function
        for i, core_func in enumerate(data["core_functions"]):
            if isinstance(core_func, dict):
                # Get the molecular_function term
                mol_func = core_func.get("molecular_function", {})
                if isinstance(mol_func, dict) and "id" in mol_func:
                    term_id = mol_func["id"]
                    term_label = mol_func.get("label", term_id)
                    core_function_terms.add(term_id)

                    # Check if this term is from accepted annotations, NEW annotations, or proposed replacements
                    is_from_annotations = (term_id in accepted_terms or
                                         term_id in new_annotation_terms or
                                         term_id in proposed_replacement_terms)

                    # Check if it has supported_by references
                    supported_by = core_func.get("supported_by", [])
                    has_support = bool(supported_by)

                    # Validate file references in supported_by
                    for j, sb in enumerate(supported_by):
                        if isinstance(sb, dict) and "reference_id" in sb:
                            validate_file_reference(
                                sb["reference_id"],
                                f"core_functions[{i}].supported_by[{j}].reference_id"
                            )

                    # If neither condition is met, it's an error
                    if not is_from_annotations and not has_support:
                        report.add_issue(
                            ValidationSeverity.ERROR,
                            f"Core function term {term_id} ({term_label}) is not from an ACCEPTED/NEW annotation and lacks supported_by references",
                            path=f"core_functions[{i}].molecular_function",
                            suggestion="Either use a term from ACCEPTED/NEW existing annotations/proposed replacements, or add supported_by references",
                        )

                    # WARNING if term is not in existing_annotations at all
                    if not is_from_annotations and has_support:
                        report.add_issue(
                            ValidationSeverity.WARNING,
                            f"Core function term {term_id} ({term_label}) is not reflected in existing_annotations block",
                            path=f"core_functions[{i}].molecular_function",
                            suggestion="Consider adding this term to existing_annotations with action: NEW if it's a novel annotation",
                            validation_category="BestPractices",
                            check_type="core_function_molecular_function_not_in_annotations"
                        )
                
                # Check locations field (should be CC terms)
                locations = core_func.get("locations", [])
                for j, location in enumerate(locations):
                    if isinstance(location, dict) and "id" in location:
                        loc_id = location["id"]
                        loc_label = location.get("label", loc_id)
                        core_function_terms.add(loc_id)

                        # First check if this is a term marked for modification
                        if loc_id in modified_terms:
                            report.add_issue(
                                ValidationSeverity.ERROR,
                                f"Location term {loc_id} ({loc_label}) was marked for MODIFY and should not be used directly",
                                path=f"core_functions[{i}].locations[{j}]",
                                suggestion="Use the proposed replacement term instead of the original term marked for modification",
                            )
                            continue

                        # Check if this term is from accepted annotations, NEW annotations, or proposed replacements
                        is_from_annotations = (loc_id in accepted_terms or
                                             loc_id in new_annotation_terms or
                                             loc_id in proposed_replacement_terms)

                        # Locations don't have their own supported_by, they rely on the core function's supported_by
                        # So check if the core function has supported_by
                        supported_by = core_func.get("supported_by", [])
                        has_support = bool(supported_by)

                        # If neither condition is met, it's an error
                        if not is_from_annotations and not has_support:
                            report.add_issue(
                                ValidationSeverity.ERROR,
                                f"Location term {loc_id} ({loc_label}) is not from an ACCEPTED/NEW annotation and the core function lacks supported_by references",
                                path=f"core_functions[{i}].locations[{j}]",
                                suggestion="Either use a location from ACCEPTED/NEW existing annotations/proposed replacements, or add supported_by references to the core function",
                            )

                        # WARNING if term is not in existing_annotations at all
                        if not is_from_annotations and has_support:
                            report.add_issue(
                                ValidationSeverity.WARNING,
                                f"Location term {loc_id} ({loc_label}) is not reflected in existing_annotations block",
                                path=f"core_functions[{i}].locations[{j}]",
                                suggestion="Consider adding this term to existing_annotations with action: NEW if it's a novel annotation",
                                validation_category="BestPractices",
                                check_type="core_function_location_not_in_annotations"
                            )
                
                # Check directly_involved_in field (should be BP terms)
                directly_involved = core_func.get("directly_involved_in", [])
                for j, process in enumerate(directly_involved):
                    if isinstance(process, dict) and "id" in process:
                        proc_id = process["id"]
                        proc_label = process.get("label", proc_id)
                        core_function_terms.add(proc_id)

                        # Check if this term is from accepted annotations, NEW annotations, or proposed replacements
                        is_from_annotations = (proc_id in accepted_terms or
                                             proc_id in new_annotation_terms or
                                             proc_id in proposed_replacement_terms)

                        # Check if the core function has supported_by
                        supported_by = core_func.get("supported_by", [])
                        has_support = bool(supported_by)

                        # If neither condition is met, it's an error
                        if not is_from_annotations and not has_support:
                            report.add_issue(
                                ValidationSeverity.ERROR,
                                f"Process term {proc_id} ({proc_label}) is not from an ACCEPTED/NEW annotation and the core function lacks supported_by references",
                                path=f"core_functions[{i}].directly_involved_in[{j}]",
                                suggestion="Either use a process from ACCEPTED/NEW existing annotations/proposed replacements, or add supported_by references to the core function",
                            )

                        # WARNING if term is not in existing_annotations at all
                        if not is_from_annotations and has_support:
                            report.add_issue(
                                ValidationSeverity.WARNING,
                                f"Process term {proc_id} ({proc_label}) is not reflected in existing_annotations block",
                                path=f"core_functions[{i}].directly_involved_in[{j}]",
                                suggestion="Consider adding this term to existing_annotations with action: NEW if it's a novel annotation",
                                validation_category="BestPractices",
                                check_type="core_function_process_not_in_annotations"
                            )

                # Check in_complex field
                in_complex = core_func.get("in_complex")
                if isinstance(in_complex, dict) and "id" in in_complex:
                    complex_id = in_complex["id"]
                    complex_label = in_complex.get("label", complex_id)
                    core_function_terms.add(complex_id)

                    # Check if this term is from accepted annotations, NEW annotations, or proposed replacements
                    is_from_annotations = (complex_id in accepted_terms or
                                         complex_id in new_annotation_terms or
                                         complex_id in proposed_replacement_terms)

                    # Check if the core function has supported_by
                    supported_by = core_func.get("supported_by", [])
                    has_support = bool(supported_by)

                    # If neither condition is met, it's an error
                    if not is_from_annotations and not has_support:
                        report.add_issue(
                            ValidationSeverity.ERROR,
                            f"Complex term {complex_id} ({complex_label}) is not from an ACCEPTED/NEW annotation and the core function lacks supported_by references",
                            path=f"core_functions[{i}].in_complex",
                            suggestion="Either use a complex from ACCEPTED/NEW existing annotations/proposed replacements, or add supported_by references to the core function",
                        )

                    # WARNING if term is not in existing_annotations at all
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
                                f"existing_annotations[{i}].review.supported_by[{j}].reference_id"
                            )

    # Check for ACCEPT annotations with PMIDs lacking supported_by
    # Only warn if the publication file exists (full text is available)
    if "existing_annotations" in data and data["existing_annotations"]:
        for i, annotation in enumerate(data["existing_annotations"]):
            if isinstance(annotation, dict):
                # Check if this annotation has a review with ACCEPT action
                review = annotation.get("review", {})
                if isinstance(review, dict) and review.get("action") == "ACCEPT":
                    # Check if it has a PMID reference
                    ref_id = annotation.get("original_reference_id", "")
                    if ref_id and ref_id.startswith("PMID:"):
                        # Check if supported_by is missing or empty
                        supported_by = review.get("supported_by", [])
                        if not supported_by:
                            # Check if publication file exists and has full text available
                            pmid_number = ref_id.replace("PMID:", "")
                            # Look for publications directory relative to the YAML file or in project root
                            if yaml_file is not None:
                                # Look relative to the YAML file's project root
                                project_root = yaml_file.parent
                                while project_root.parent != project_root and not (project_root / "publications").exists():
                                    project_root = project_root.parent
                                pub_file = project_root / "publications" / f"PMID_{pmid_number}.md"
                            else:
                                pub_file = Path("publications") / f"PMID_{pmid_number}.md"
                            
                            # Check if full text is available in the publication file
                            full_text_available = False
                            if pub_file.exists():
                                try:
                                    import yaml as yaml_lib
                                    with open(pub_file, 'r') as f:
                                        content = f.read()
                                        # Extract frontmatter between --- markers
                                        if content.startswith('---'):
                                            end_marker = content.find('---', 3)
                                            if end_marker != -1:
                                                frontmatter = content[3:end_marker]
                                                pub_data = yaml_lib.safe_load(frontmatter)
                                                full_text_available = pub_data.get('full_text_available', False)
                                except Exception:
                                    # If we can't parse the file, assume no full text
                                    pass
                            
                            # Only warn if full text is available
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
        # yaml_file is guaranteed to be Path here
        goa_result = goa_validator.validate_against_goa(yaml_file)

        if not goa_result.is_valid:
            # Report GOA validation issues
            if goa_result.error_message:
                report.add_issue(
                    ValidationSeverity.WARNING,
                    f"GOA validation: {goa_result.error_message}",
                    path="existing_annotations",
                )

            if goa_result.missing_in_yaml:
                # Show first few missing annotations for debugging
                missing_count = len(goa_result.missing_in_yaml)
                missing_examples: List[str] = []
                for ann in goa_result.missing_in_yaml[:5]:  # Show first 5
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
                # Show first few annotations not in GOA for debugging
                missing_count = len(goa_result.missing_in_goa)
                extra_examples: List[str] = []
                for ann_dict in goa_result.missing_in_goa[:5]:  # Show first 5
                    # ann_dict is a Dict from the YAML, not a GOAAnnotation
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

            # Don't report label mismatches - we validate against ontology, not GOA
            # GOA files may use synonyms instead of primary labels

            if goa_result.mismatched_evidence:
                # Evidence mismatches are warnings, not errors
                report.add_issue(
                    ValidationSeverity.WARNING,
                    f"Found {len(goa_result.mismatched_evidence)} evidence type mismatches with GOA file",
                    path="existing_annotations",
                    suggestion="Consider updating evidence types to match GOA file",
                )

    # DEPRECATED: Validate supporting_text using fuzzy matching (kept for comparison)
    # This validator has false positives - use SupportingTextSubstringValidator instead
    # DISABLED: No longer run by default as it's slower and less accurate than substring matching
    # To re-enable, uncomment the code below
    # if check_supporting_text and "existing_annotations" in data:
    #     if progress_callback:
    #         progress_callback("Validating supporting text (fuzzy - deprecated)")
    #     st_validator = SupportingTextValidator()
    #     st_report = st_validator.validate_data(data)
    #
    #     if not st_report.is_valid:
    #         # Report invalid supporting texts
    #         for st_result in st_report.results:
    #             if not st_result.is_valid:
    #                 severity = ValidationSeverity.WARNING
    #
    #                 # Check if this is a PMID finding without supporting_text
    #                 if "PMID reference" in (
    #                     st_result.error_message or ""
    #                 ) and "without supporting_text" in (st_result.error_message or ""):
    #                     # Always WARNING for missing supporting_text in PMID findings
    #                     severity = ValidationSeverity.WARNING
    #                 elif st_result.similarity_score < 0.5:
    #                     # Very low similarity suggests incorrect reference
    #                     severity = ValidationSeverity.ERROR
    #
    #                 report.add_issue(
    #                     severity,
    #                     st_result.error_message
    #                     or "Supporting text not found in referenced publication",
    #                     path=st_result.annotation_path,
    #                     suggestion=st_result.suggested_fix,
    #                     validation_category="SupportingTextValidator",
    #                     check_type="supporting_text_not_found"
    #                 )

    # Validate supporting_text using deterministic substring matching
    if check_supporting_text and "existing_annotations" in data:
        if progress_callback:
            progress_callback("Validating supporting text (substring matching)")
        substring_validator = SupportingTextSubstringValidator()
        substring_report = substring_validator.validate_data(data)

        if not substring_report.is_valid:
            # Report invalid supporting texts using substring validation
            for st_result in substring_report.results:
                if not st_result.is_valid:
                    error_msg = st_result.error_message or "Supporting text not found in referenced publication"

                    # Distinguish between missing supporting_text (WARNING) vs incorrect quote (ERROR)
                    # Missing supporting_text is a recommendation, not a requirement
                    if "without supporting_text" in error_msg:
                        severity = ValidationSeverity.WARNING
                    else:
                        # Actual quote that doesn't match source is an error
                        severity = ValidationSeverity.ERROR

                    report.add_issue(
                        severity,
                        f"[Substring] {error_msg}",
                        path=st_result.annotation_path,
                        suggestion=st_result.suggested_fix,
                        validation_category="SupportingTextSubstringValidator",
                        check_type="supporting_text_substring_not_found"
                    )

        # Report coverage statistics separately for findings and annotations
        if substring_report.total_findings > 0:
            findings_coverage = substring_report.findings_coverage_rate
            if findings_coverage < 50:
                report.add_issue(
                    ValidationSeverity.INFO,
                    f"Only {findings_coverage:.1f}% of reference findings have supporting_text",
                    path="references",
                    suggestion="Consider adding supporting_text to more findings for better documentation",
                    validation_category="SupportingTextSubstringValidator",
                    check_type="low_findings_supporting_text_coverage"
                )

        if substring_report.total_annotations > 0:
            annotations_coverage = substring_report.annotations_coverage_rate
            if annotations_coverage < 50:
                # Use WARNING (not INFO) if coverage is 0% - that's a significant gap
                severity = ValidationSeverity.WARNING if annotations_coverage == 0 else ValidationSeverity.INFO
                report.add_issue(
                    severity,
                    f"Only {annotations_coverage:.1f}% of existing annotations have supporting_text",
                    path="existing_annotations",
                    suggestion="Consider adding supporting_text to more annotations for better documentation",
                    validation_category="SupportingTextSubstringValidator",
                    check_type="low_annotations_supporting_text_coverage"
                )

        # Stricter check: if PMIDs have available full text, we expect supporting_text
        if substring_report.annotations_with_validatable_refs > 0:
            validatable_coverage = substring_report.validatable_annotations_coverage_rate
            if validatable_coverage < 100:
                # This is a WARNING - we have the publications, so supporting_text should be present
                num_missing = (
                    substring_report.annotations_with_validatable_refs
                    - substring_report.validatable_annotations_with_supporting_text
                )
                report.add_issue(
                    ValidationSeverity.WARNING,
                    f"{num_missing} annotation(s) have PMID references with cached full text but no supporting_text "
                    f"({validatable_coverage:.1f}% coverage)",
                    path="existing_annotations",
                    suggestion="Add supporting_text with quotes from publications to document evidence",
                    validation_category="SupportingTextSubstringValidator",
                    check_type="missing_supporting_text_for_validatable_refs"
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
        schema_path: Optional path to schema file
        check_best_practices: Whether to check for best practices
        check_goa: Whether to validate against GOA files
        check_supporting_text: Whether to validate supporting_text against cached publications
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
        from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn, TimeElapsedColumn

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TaskProgressColumn(),
            TimeElapsedColumn(),
            console=None,  # Use default console
        ) as progress:
            main_task = progress.add_task("Validating files...", total=len(yaml_files))

            for yaml_file in yaml_files:
                yaml_file_path = Path(yaml_file)
                progress.update(main_task, description=f"Validating {yaml_file_path.name}")

                # Create a callback to show sub-steps for this file
                def step_callback(step: str):
                    progress.update(main_task, description=f"{yaml_file_path.name}: {step}")

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
        # No progress bar for single files or when disabled
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
    # Convert old format to new format
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
    """Validate a rule review YAML file against the LinkML schema.

    Args:
        yaml_file: Path to the YAML file to validate
        schema_path: Optional path to schema file (uses default if not provided)
        check_publications: Whether to validate PMID titles
        progress_callback: Optional callback function to report progress steps

    Returns:
        ValidationReport with detailed validation results

    Example:
        >>> # Example: validate_rule_review(Path("rules/reviews/ARBA00026249-review.yaml"))
    """
    yaml_file_path: Path = Path(yaml_file)
    report = ValidationReport(file_path=yaml_file_path, is_valid=True)

    if progress_callback:
        progress_callback("Checking file existence")

    # Check if file exists
    if not yaml_file_path.exists():
        report.add_issue(
            ValidationSeverity.ERROR, f"File not found: {yaml_file_path}", path=None
        )
        return report

    try:
        if progress_callback:
            progress_callback("Loading schema")

        # Load schema
        if schema_path:
            schema_path_obj = Path(schema_path)
            if not schema_path_obj.exists():
                report.add_issue(
                    ValidationSeverity.ERROR,
                    f"Schema file not found: {schema_path_obj}",
                    path=None,
                )
                return report
            SchemaView(str(schema_path_obj))
            schema_path = schema_path_obj
        else:
            load_schema()

        if progress_callback:
            progress_callback("Parsing YAML")

        # Load YAML data
        with open(yaml_file_path, "r") as f:
            data = yaml.safe_load(f)

        if progress_callback:
            progress_callback("Schema validation")

        # Create validator
        validator = JsonSchemaDataValidator(str(schema_path or get_schema_path()))

        # Validate against schema - use RuleReview class
        linkml_report = validator.validate_dict(data, target_class="RuleReview")

        # Process LinkML validation results
        if linkml_report and linkml_report.results:
            for result in linkml_report.results:
                message = result.message if hasattr(result, "message") else str(result)
                path_match = re.search(r"in \$\.(.+)$", message)
                path = path_match.group(1) if path_match else None

                report.add_issue(
                    ValidationSeverity.ERROR,
                    message,
                    path=path,
                    validation_category="SchemaValidator",
                    check_type="schema_validation"
                )

        # Validate publications if enabled and no hard schema errors
        if check_publications and not report.has_errors:
            if progress_callback:
                progress_callback("Validating publications")

            pub_validator = PublicationValidator()
            pub_results = pub_validator.validate_publications_in_data(data)

            for pub_result in pub_results:
                if not pub_result.is_valid:
                    if pub_result.correct_title is None:
                        severity = ValidationSeverity.WARNING
                        suggestion = "Check if PMID is correct or fetch the publication"
                    else:
                        severity = ValidationSeverity.ERROR
                        suggestion = f"Use correct title: '{pub_result.correct_title}'"

                    report.add_issue(
                        severity,
                        pub_result.error_message
                        or f"Invalid publication: PMID:{pub_result.pmid}",
                        path=pub_result.path,
                        suggestion=suggestion,
                        validation_category="PublicationValidator",
                        check_type="publication_title_mismatch"
                    )

        # Validate supporting_text in supported_by field (top-level and nested in assessments)
        if check_publications and not report.has_errors:
            if progress_callback:
                progress_callback("Validating supporting text")

            st_validator = SupportingTextSubstringValidator()

            # Helper to validate a supported_by list
            def validate_supported_by_list(items: list, path_prefix: str):
                for i, item in enumerate(items):
                    if not isinstance(item, dict):
                        continue
                    ref_id = item.get("reference_id", "")
                    supporting_text = item.get("supporting_text", "")

                    if supporting_text and ref_id:
                        st_result = st_validator.validate_supporting_text_against_reference(
                            supporting_text=supporting_text,
                            reference_id=ref_id,
                            annotation_path=f"{path_prefix}[{i}]",
                            yaml_data=data
                        )

                        if st_result and not st_result.is_valid:
                            report.add_issue(
                                ValidationSeverity.ERROR,
                                st_result.error_message or f"Supporting text not found in {ref_id}",
                                path=f"{path_prefix}[{i}].supporting_text",
                                suggestion=st_result.suggested_fix,
                                validation_category="SupportingTextSubstringValidator",
                                check_type="supporting_text_substring_not_found"
                            )

            # Validate top-level supported_by
            if "supported_by" in data:
                validate_supported_by_list(data.get("supported_by", []), "supported_by")

            # Validate nested supported_by in assessment objects
            assessment_fields = [
                "parsimony", "literature_support", "condition_overlap",
                "go_specificity", "taxonomic_scope"
            ]
            for field in assessment_fields:
                if field in data and isinstance(data[field], dict):
                    assessment = data[field]
                    if "supported_by" in assessment:
                        validate_supported_by_list(
                            assessment.get("supported_by", []),
                            f"{field}.supported_by"
                        )

        return report

    except yaml.YAMLError as e:
        report.add_issue(
            ValidationSeverity.ERROR, f"YAML parsing error: {str(e)}", path=None
        )
        return report
    except Exception as e:
        error_type = type(e).__name__
        tb = traceback.format_exc()
        last_tb_line = tb.strip().split("\n")[-1] if tb else ""
        report.add_issue(
            ValidationSeverity.ERROR,
            f"Validation error ({error_type}): {str(e)} - {last_tb_line}",
            path=None,
        )
        return report
