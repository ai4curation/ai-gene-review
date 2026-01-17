"""CSV export for ARBA and UniRule rules.

Exports rules to a flat CSV format with one row per ConditionSet (the inner
conjunctive clause in the DNF structure). Uses positional pivot columns for
conditions (term1_*, term2_*, term3_*).

Example:
    >>> from ai_gene_review.etl.rule_export import rule_to_rows
    >>> rule = {
    ...     "uniRuleId": "ARBA00026249",
    ...     "mainRule": {
    ...         "conditionSets": [{
    ...             "conditions": [
    ...                 {"type": "taxon", "conditionValues": [{"value": "Fungi", "cvId": "4751"}]}
    ...             ]
    ...         }],
    ...         "annotations": [{"dbReference": {"database": "GO", "id": "GO:0006915"}}]
    ...     },
    ...     "statistics": {"reviewedProteinCount": 5, "unreviewedProteinCount": 100},
    ...     "createdDate": "2020-05-12",
    ...     "modifiedDate": "2025-03-21"
    ... }
    >>> rows = rule_to_rows(rule, "arba")
    >>> len(rows)
    1
    >>> rows[0]["term1_type"]
    'taxon'
"""

import csv
import json
from pathlib import Path
from typing import Callable, Iterator, Optional


# Column order for CSV output
COLUMNS = [
    "rule_id",
    "rule_type",
    "condition_set_index",
    "term1_type",
    "term1_id",
    "term1_curie",
    "term1_label",
    "term1_negated",
    "term2_type",
    "term2_id",
    "term2_curie",
    "term2_label",
    "term2_negated",
    "term3_type",
    "term3_id",
    "term3_curie",
    "term3_label",
    "term3_negated",
    "go_ids",
    "go_labels",
    "reviewed_count",
    "unreviewed_count",
    "created_date",
    "modified_date",
]


def _extract_go_annotations(rule_json: dict) -> tuple[list[str], list[str]]:
    """Extract GO IDs and labels from rule annotations.

    Args:
        rule_json: Rule JSON data

    Returns:
        Tuple of (go_ids list, go_labels list)

    Example:
        >>> rule = {"mainRule": {"annotations": [
        ...     {"dbReference": {"database": "GO", "id": "GO:0006915", "label": "apoptosis"}}
        ... ]}}
        >>> _extract_go_annotations(rule)
        (['GO:0006915'], ['apoptosis'])
    """
    go_ids = []
    go_labels = []

    main_rule = rule_json.get("mainRule", {})
    for ann in main_rule.get("annotations", []):
        dbref = ann.get("dbReference", {})
        if dbref.get("database") == "GO":
            go_id = dbref.get("id", "")
            go_label = dbref.get("label", "")
            if go_id:
                go_ids.append(go_id)
                go_labels.append(go_label or "")

    return go_ids, go_labels


def _extract_condition_fields(cond: dict, index: int) -> dict:
    """Extract fields for a single condition into term{N}_ prefixed dict.

    Args:
        cond: Condition dict from JSON
        index: 1-based index for column prefix (1, 2, or 3)

    Returns:
        Dict with term{N}_type, term{N}_id, term{N}_curie, term{N}_label, term{N}_negated

    Example:
        >>> cond = {
        ...     "type": "taxon",
        ...     "conditionValues": [{"value": "Fungi", "cvId": "4751", "curie": "NCBITaxon:4751", "label": "Fungi"}],
        ...     "isNegative": False
        ... }
        >>> fields = _extract_condition_fields(cond, 1)
        >>> fields["term1_type"]
        'taxon'
        >>> fields["term1_curie"]
        'NCBITaxon:4751'
    """
    prefix = f"term{index}_"
    cond_type = cond.get("type", "")
    is_negative = cond.get("isNegative", False)

    # Get first condition value (they are alternatives, typically just one)
    cv = {}
    cond_values = cond.get("conditionValues", [])
    if cond_values:
        cv = cond_values[0]

    return {
        f"{prefix}type": cond_type,
        f"{prefix}id": cv.get("value", ""),
        f"{prefix}curie": cv.get("curie", ""),
        f"{prefix}label": cv.get("label", ""),
        f"{prefix}negated": str(is_negative).lower(),
    }


def rule_to_rows(rule_json: dict, rule_type: str) -> list[dict]:
    """Convert a single rule JSON to list of row dicts.

    Creates one row per ConditionSet in the rule.

    Args:
        rule_json: Rule JSON data (from .json or .enriched.json)
        rule_type: "arba" or "unirule"

    Returns:
        List of row dicts, one per condition set

    Example:
        >>> rule = {
        ...     "uniRuleId": "TEST001",
        ...     "mainRule": {
        ...         "conditionSets": [
        ...             {"conditions": [{"type": "taxon", "conditionValues": [{"value": "Fungi"}]}]},
        ...             {"conditions": [{"type": "taxon", "conditionValues": [{"value": "Metazoa"}]}]}
        ...         ],
        ...         "annotations": []
        ...     },
        ...     "statistics": {"reviewedProteinCount": 0, "unreviewedProteinCount": 0},
        ...     "createdDate": "", "modifiedDate": ""
        ... }
        >>> rows = rule_to_rows(rule, "arba")
        >>> len(rows)
        2
    """
    rows = []

    rule_id = rule_json.get("uniRuleId", "")
    stats = rule_json.get("statistics", {})
    reviewed_count = stats.get("reviewedProteinCount", 0)
    unreviewed_count = stats.get("unreviewedProteinCount", 0)
    created_date = rule_json.get("createdDate", "")
    modified_date = rule_json.get("modifiedDate", "")

    # Extract GO annotations (same for all rows from this rule)
    go_ids, go_labels = _extract_go_annotations(rule_json)
    go_ids_str = "|".join(go_ids)
    go_labels_str = "|".join(go_labels)

    # Process each condition set
    main_rule = rule_json.get("mainRule", {})
    for cs_index, cs in enumerate(main_rule.get("conditionSets", [])):
        row = {
            "rule_id": rule_id,
            "rule_type": rule_type,
            "condition_set_index": cs_index,
            "go_ids": go_ids_str,
            "go_labels": go_labels_str,
            "reviewed_count": reviewed_count,
            "unreviewed_count": unreviewed_count,
            "created_date": created_date,
            "modified_date": modified_date,
        }

        # Initialize empty term columns
        for i in range(1, 4):
            prefix = f"term{i}_"
            row[f"{prefix}type"] = ""
            row[f"{prefix}id"] = ""
            row[f"{prefix}curie"] = ""
            row[f"{prefix}label"] = ""
            row[f"{prefix}negated"] = ""

        # Fill in conditions (up to 3)
        conditions = cs.get("conditions", [])
        for i, cond in enumerate(conditions[:3], start=1):
            cond_fields = _extract_condition_fields(cond, i)
            row.update(cond_fields)

        rows.append(row)

    return rows


def iter_rule_files(
    cache_dir: Path,
    rule_type: str = "all",
    use_enriched: bool = True
) -> Iterator[tuple[Path, str]]:
    """Iterate over rule files in cache directory.

    Args:
        cache_dir: Base cache directory (e.g., Path("rules"))
        rule_type: "arba", "unirule", or "all"
        use_enriched: If True, prefer .enriched.json files

    Yields:
        Tuple of (file_path, rule_type_str)

    Example:
        >>> # List would contain tuples like (Path("rules/arba/ARBA001/ARBA001.enriched.json"), "arba")
    """
    dirs_to_scan = []

    if rule_type in ("arba", "all"):
        arba_dir = cache_dir / "arba"
        if arba_dir.exists():
            dirs_to_scan.append((arba_dir, "arba", "ARBA*/ARBA*.json"))

    if rule_type in ("unirule", "all"):
        unirule_dir = cache_dir / "unirule"
        if unirule_dir.exists():
            dirs_to_scan.append((unirule_dir, "unirule", "UR*/UR*.json"))

    for rule_dir, rtype, pattern in dirs_to_scan:
        # Get all JSON files
        all_files = sorted(rule_dir.glob(pattern))

        # Group by rule ID (base name without .enriched)
        rule_files: dict[str, dict[str, Path]] = {}
        for f in all_files:
            if f.name.endswith(".enriched.json"):
                rule_id = f.name.replace(".enriched.json", "")
                rule_files.setdefault(rule_id, {})["enriched"] = f
            else:
                rule_id = f.stem
                rule_files.setdefault(rule_id, {})["raw"] = f

        # Yield preferred file for each rule
        for rule_id in sorted(rule_files.keys()):
            files = rule_files[rule_id]
            if use_enriched and "enriched" in files:
                yield files["enriched"], rtype
            elif "raw" in files:
                yield files["raw"], rtype


def export_rules_to_csv(
    cache_dir: Path,
    output_path: Path,
    rule_type: str = "all",
    use_enriched: bool = True,
    progress_callback: Optional[Callable[[int, int], None]] = None
) -> int:
    """Export rules to CSV with one row per condition set.

    Args:
        cache_dir: Base cache directory (e.g., Path("rules"))
        output_path: Output CSV file path
        rule_type: "arba", "unirule", or "all"
        use_enriched: If True, prefer .enriched.json files
        progress_callback: Optional callback(rules_processed, rows_written)

    Returns:
        Number of rows written

    Example:
        >>> # export_rules_to_csv(Path("rules"), Path("rules/export.csv"))
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)

    rows_written = 0
    rules_processed = 0

    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=COLUMNS)
        writer.writeheader()

        for rule_file, rtype in iter_rule_files(cache_dir, rule_type, use_enriched):
            rule_json = json.loads(rule_file.read_text())
            rows = rule_to_rows(rule_json, rtype)

            for row in rows:
                writer.writerow(row)
                rows_written += 1

            rules_processed += 1

            if progress_callback and rules_processed % 100 == 0:
                progress_callback(rules_processed, rows_written)

    if progress_callback:
        progress_callback(rules_processed, rows_written)

    return rows_written


def create_go_summary(
    main_csv_path: Path,
    summary_output_path: Optional[Path] = None
) -> Path:
    """Create a GO summary CSV from the main export CSV.

    Creates one row per unique (rule_id, GO term) combination with the count
    of condition sets that apply to that rule+GO combination.

    Args:
        main_csv_path: Path to the main export CSV (output from export_rules_to_csv)
        summary_output_path: Optional output path for summary CSV
            (defaults to {main_csv_path}-go-summary.csv)

    Returns:
        Path to the created summary CSV

    Example:
        >>> # create_go_summary(Path("rules/export.csv"))
        >>> # Creates rules/export-go-summary.csv with columns:
        >>> # rule_id, rule_type, go_id, go_label, condition_set_count
    """
    if summary_output_path is None:
        # Default: insert "-go-summary" before .csv extension
        stem = main_csv_path.stem
        summary_output_path = main_csv_path.parent / f"{stem}-go-summary.csv"

    # Read main CSV and aggregate
    summary_data: dict[tuple[str, str, str], dict] = {}

    with open(main_csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rule_id = row["rule_id"]
            rule_type = row["rule_type"]
            go_ids_str = row["go_ids"]
            go_labels_str = row["go_labels"]

            # Skip rows with no GO annotations
            if not go_ids_str:
                continue

            # Split pipe-separated GO IDs and labels
            go_ids = go_ids_str.split("|")
            go_labels = go_labels_str.split("|")

            # Ensure we have labels for all IDs (pad with empty strings if needed)
            while len(go_labels) < len(go_ids):
                go_labels.append("")

            # Process each GO term
            for go_id, go_label in zip(go_ids, go_labels):
                key = (rule_id, rule_type, go_id)
                if key not in summary_data:
                    summary_data[key] = {
                        "rule_id": rule_id,
                        "rule_type": rule_type,
                        "go_id": go_id,
                        "go_label": go_label,
                        "condition_set_count": 0
                    }
                summary_data[key]["condition_set_count"] += 1

    # Write summary CSV
    summary_output_path.parent.mkdir(parents=True, exist_ok=True)
    summary_columns = ["rule_id", "rule_type", "go_id", "go_label", "condition_set_count"]

    with open(summary_output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=summary_columns)
        writer.writeheader()

        # Sort by rule_id, then go_id
        for key in sorted(summary_data.keys()):
            writer.writerow(summary_data[key])

    return summary_output_path
