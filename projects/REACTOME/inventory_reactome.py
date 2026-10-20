from __future__ import annotations

import argparse
import csv
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Iterable

import yaml


REACTOME_SOURCE_RE = re.compile(r"^Reactome:(R-[A-Z]+-\d+)$")
REACTOME_ID_RE = re.compile(r"^R-[A-Z]+-\d+$")
UNIPROTKB_RE = re.compile(r"^UniProtKB:[A-Z0-9]+(?:-\d+)?$")
GOA_ASPECTS = {
    "molecular_function": "MF",
    "biological_process": "BP",
    "cellular_component": "CC",
    "F": "MF",
    "P": "BP",
    "C": "CC",
}

GENE_FIELDS = [
    "organism",
    "gene",
    "review_path",
    "gene_symbol",
    "uniprot_id",
    "taxon_id",
    "taxon_label",
    "annotation_index",
    "reactome_id",
    "reactome_title",
    "reactome_cached",
    "reactome_path",
    "reactome_display_name",
    "reactome_species",
    "term_id",
    "term_label",
    "evidence_type",
    "qualifier",
    "aspect",
    "negated",
    "isoform",
    "review_action",
    "review_summary",
]

MODULE_FIELDS = [
    "module_id",
    "module_title",
    "module_path",
    "reactome_id",
    "scope",
    "node_id",
    "node_label",
    "node_type",
    "annoton_id",
    "annoton_label",
    "function_id",
    "function_label",
    "participant_ids",
    "participant_labels",
    "statement",
    "reactome_cached",
    "reactome_path",
    "reactome_display_name",
    "reactome_species",
]

GOCAM_FIELDS = [
    "gene_product",
    "gene_label",
    "model_id",
    "model_title",
    "taxon",
    "activity_id",
    "molecular_function",
    "mf_label",
    "biological_process",
    "bp_label",
    "cellular_component",
    "cc_label",
    "in_reactome_module",
    "matching_modules",
]

MF_SLICE_FIELDS = GENE_FIELDS + [
    "candidate_verdict",
    "candidate_bucket",
    "manual_verdict",
    "manual_bucket",
    "manual_reason",
    "candidate_flags",
    "genes_for_reactome_id",
    "matching_module_mfs",
]

REPEATED_MF_EVENT_FIELDS = [
    "reactome_id",
    "reactome_display_name",
    "reactome_species",
    "row_count",
    "gene_count",
    "organisms",
    "genes",
    "actions",
    "candidate_verdicts",
    "candidate_buckets",
    "terms",
    "audit_bucket",
    "audit_priority",
    "has_mixed_actions",
    "has_mixed_verdicts",
    "has_manual_failure",
    "has_local_module_mf",
    "row_details",
]

MANUAL_MF_VERDICT_FIELDS = [
    "organism",
    "gene",
    "annotation_index",
    "reactome_id",
    "term_id",
    "manual_verdict",
    "manual_bucket",
    "manual_reason",
]

MF_VERDICT_BY_ACTION = {
    "ACCEPT": "reaction_mf_exact",
    "KEEP_AS_NON_CORE": "reaction_mf_exact",
    "MODIFY": "reaction_mf_refine",
    "UNDECIDED": "insufficient_event_detail",
}

MF_BUCKET_BY_ACTION = {
    "ACCEPT": "accepted_mf",
    "KEEP_AS_NON_CORE": "accepted_non_core_mf",
    "MODIFY": "mf_term_refinement",
    "MARK_AS_OVER_ANNOTATED": "mixed_over_annotation",
    "REMOVE": "removed_mf",
    "UNDECIDED": "undecided_mf",
}

MANUAL_FAILURE_BUCKETS = {
    "activity_contradicted",
    "contested_direct_activity",
    "nonphysiological_side_activity",
    "obsolete_go_term",
    "regulator_not_executor",
    "wrong_executor",
    "wrong_go_branch",
    "wrong_transport_mechanism",
}


def load_yaml(path: Path) -> dict[str, Any]:
    return yaml.load(path.read_text(encoding="utf-8"), Loader=yaml.CSafeLoader) or {}


def contains_reactome_source(path: Path) -> bool:
    return "Reactome:R-" in path.read_text(encoding="utf-8")


def compact(value: Any) -> str:
    return " ".join(str(value or "").split())


def rel(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def reactome_stable_id(value: Any) -> str | None:
    if not isinstance(value, str):
        return None
    match = REACTOME_SOURCE_RE.match(value)
    return match.group(1) if match else None


def aspect_for_qualifier(qualifier: str) -> str:
    if qualifier in {"enables", "contributes_to"}:
        return "MF"
    if qualifier.startswith("involved_in") or qualifier.startswith("acts_upstream"):
        return "BP"
    if qualifier in {"located_in", "is_active_in", "part_of", "colocalizes_with"}:
        return "CC"
    return "UNKNOWN"


def load_goa_index(path: Path) -> dict[tuple[str, str, str], dict[str, str]]:
    rows: dict[tuple[str, str, str], dict[str, str]] = {}
    if not path.exists():
        return rows
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        for row in reader:
            rows[
                (
                    row.get("REFERENCE", ""),
                    row.get("GO TERM", ""),
                    row.get("GO EVIDENCE CODE", ""),
                )
            ] = row
    return rows


def load_reactome_cache(root: Path) -> dict[str, dict[str, str]]:
    cache: dict[str, dict[str, str]] = {}
    for path in sorted((root / "reactome").glob("R-*.md")):
        text = path.read_text(encoding="utf-8")
        frontmatter = {}
        if text.startswith("---\n"):
            try:
                _, raw_frontmatter, _ = text.split("---\n", 2)
                frontmatter = yaml.load(raw_frontmatter, Loader=yaml.CSafeLoader) or {}
            except ValueError:
                frontmatter = {}
        stable_id = str(frontmatter.get("stable_id") or path.stem)
        if not REACTOME_ID_RE.match(stable_id):
            continue
        cache[stable_id] = {
            "reactome_cached": "yes",
            "reactome_path": rel(path, root),
            "reactome_display_name": compact(frontmatter.get("display_name")),
            "reactome_species": compact(frontmatter.get("species")),
        }
    return cache


def cache_fields(stable_id: str, cache: dict[str, dict[str, str]]) -> dict[str, str]:
    return cache.get(
        stable_id,
        {
            "reactome_cached": "no",
            "reactome_path": "",
            "reactome_display_name": "",
            "reactome_species": "",
        },
    )


def inventory_gene_reviews(
    root: Path, reactome_cache: dict[str, dict[str, str]]
) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for path in sorted((root / "genes").glob("*/*/*-ai-review.yaml")):
        if not contains_reactome_source(path):
            continue
        doc = load_yaml(path)
        references = {
            str(ref.get("id")): compact(ref.get("title"))
            for ref in doc.get("references", [])
            if isinstance(ref, dict)
        }
        parts = path.relative_to(root).parts
        organism, gene = parts[1], parts[2]
        goa = load_goa_index(path.with_name(f"{gene}-goa.tsv"))

        for i, annotation in enumerate(doc.get("existing_annotations", []), start=1):
            if not isinstance(annotation, dict):
                continue
            stable_id = reactome_stable_id(annotation.get("original_reference_id"))
            if stable_id is None:
                continue

            term = annotation.get("term") or {}
            review = annotation.get("review") or {}
            goa_row = goa.get(
                (
                    annotation.get("original_reference_id", ""),
                    str(term.get("id") or ""),
                    annotation.get("evidence_type", ""),
                ),
                {},
            )
            qualifier = str(
                annotation.get("qualifier") or goa_row.get("QUALIFIER") or ""
            )
            aspect = GOA_ASPECTS.get(
                goa_row.get("GO ASPECT") or "", aspect_for_qualifier(qualifier)
            )
            taxon = doc.get("taxon") or {}
            rows.append(
                {
                    "organism": organism,
                    "gene": gene,
                    "review_path": rel(path, root),
                    "gene_symbol": str(doc.get("gene_symbol") or gene),
                    "uniprot_id": str(doc.get("id") or ""),
                    "taxon_id": str(taxon.get("id") or ""),
                    "taxon_label": compact(taxon.get("label")),
                    "annotation_index": str(i),
                    "reactome_id": stable_id,
                    "reactome_title": references.get(f"Reactome:{stable_id}", ""),
                    "term_id": str(term.get("id") or ""),
                    "term_label": compact(term.get("label")),
                    "evidence_type": str(annotation.get("evidence_type") or ""),
                    "qualifier": qualifier,
                    "aspect": aspect,
                    "negated": str(bool(annotation.get("negated"))).lower(),
                    "isoform": str(annotation.get("isoform") or ""),
                    "review_action": str(review.get("action") or "PENDING"),
                    "review_summary": compact(review.get("summary")),
                    **cache_fields(stable_id, reactome_cache),
                }
            )
    return sorted(
        rows,
        key=lambda row: (
            row["organism"],
            row["gene"],
            int(row["annotation_index"]),
            row["reactome_id"],
        ),
    )


def term_id(value: Any) -> str:
    if isinstance(value, dict):
        term = value.get("term") or {}
        if isinstance(term, dict):
            return str(term.get("id") or "")
    return ""


def term_label(value: Any) -> str:
    if isinstance(value, dict):
        term = value.get("term") or {}
        if isinstance(term, dict):
            return compact(term.get("label"))
    return ""


def source_scope(context: dict[str, str]) -> str:
    if context.get("annoton_id"):
        return "activity_evidence"
    if context.get("node_id"):
        return "node_evidence"
    return "module_evidence"


def uniprot_terms(value: Any) -> Iterable[tuple[str, str]]:
    if isinstance(value, dict):
        term = value.get("term")
        if isinstance(term, dict):
            term_id_value = str(term.get("id") or "")
            if UNIPROTKB_RE.match(term_id_value):
                yield term_id_value, compact(term.get("label"))
        for child in value.values():
            yield from uniprot_terms(child)
    elif isinstance(value, list):
        for child in value:
            yield from uniprot_terms(child)


def iter_module_sources(
    value: Any,
    context: dict[str, str],
    reactome_cache: dict[str, dict[str, str]],
) -> Iterable[dict[str, str]]:
    if isinstance(value, list):
        for child in value:
            yield from iter_module_sources(child, context, reactome_cache)
        return

    if not isinstance(value, dict):
        return

    stable_id = reactome_stable_id(value.get("source_id"))
    if stable_id is not None:
        yield {
            **context,
            "reactome_id": stable_id,
            "scope": source_scope(context),
            "statement": compact(value.get("statement")),
            **cache_fields(stable_id, reactome_cache),
        }

    annoton_context = context
    if "function" in value and ("participant" in value or "role_description" in value):
        participant_terms = sorted(set(uniprot_terms(value.get("participant") or {})))
        annoton_context = {
            **context,
            "annoton_id": str(value.get("id") or ""),
            "annoton_label": compact(value.get("label")),
            "function_id": term_id(value.get("function")),
            "function_label": term_label(value.get("function")),
            "participant_ids": "|".join(term_id for term_id, _ in participant_terms),
            "participant_labels": "|".join(
                label for _, label in participant_terms if label
            ),
        }

    for key, child in value.items():
        child_context = annoton_context
        if key == "node" and isinstance(child, dict):
            child_context = {
                **annoton_context,
                "node_id": str(child.get("id") or ""),
                "node_label": compact(child.get("label")),
                "node_type": str(child.get("module_type") or ""),
            }
        yield from iter_module_sources(child, child_context, reactome_cache)


def inventory_modules(
    root: Path, reactome_cache: dict[str, dict[str, str]]
) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for path in sorted((root / "modules").glob("*.yaml")):
        if not contains_reactome_source(path):
            continue
        doc = load_yaml(path)
        module = doc.get("module") or {}
        context = {
            "module_id": str(module.get("id") or doc.get("id") or path.stem),
            "module_title": compact(doc.get("title")),
            "module_path": rel(path, root),
            "node_id": "",
            "node_label": "",
            "node_type": "",
            "annoton_id": "",
            "annoton_label": "",
            "function_id": "",
            "function_label": "",
            "participant_ids": "",
            "participant_labels": "",
        }
        rows.extend(iter_module_sources(doc, context, reactome_cache))

    return sorted(
        rows,
        key=lambda row: (
            row["module_id"],
            row["reactome_id"],
            row["node_id"],
            row["annoton_id"],
        ),
    )


def inventory_gocams(
    root: Path, module_rows: list[dict[str, str]]
) -> list[dict[str, str]]:
    modules_by_member: dict[str, set[str]] = defaultdict(set)
    for row in module_rows:
        for member in row["participant_ids"].split("|"):
            if member:
                modules_by_member[member].add(row["module_id"])

    rows: list[dict[str, str]] = []
    with (root / "gocams" / "index.tsv").open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        for row in reader:
            if row.get("taxon") != "NCBITaxon:9606":
                continue
            modules = sorted(modules_by_member.get(row["gene_product"], []))
            rows.append(
                {
                    **{field: row.get(field, "") for field in GOCAM_FIELDS[:-2]},
                    "in_reactome_module": str(bool(modules)).lower(),
                    "matching_modules": "|".join(modules),
                }
            )
    return sorted(rows, key=lambda row: (row["model_id"], row["activity_id"]))


def write_tsv(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle, fieldnames=fieldnames, delimiter="\t", lineterminator="\n"
        )
        writer.writeheader()
        writer.writerows(rows)


def markdown_table(headers: list[str], rows: list[list[str | int]]) -> str:
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    for row in rows:
        lines.append(
            "| " + " | ".join(str(value).replace("|", "\\|") for value in row) + " |"
        )
    return "\n".join(lines)


def top_counts(
    rows: Iterable[dict[str, str]], field: str, limit: int = 10
) -> list[list[str | int]]:
    counts = Counter(row.get(field) or "(blank)" for row in rows)
    return [[label, count] for label, count in counts.most_common(limit)]


def counter_summary(counter: Counter[str]) -> str:
    return "|".join(
        f"{value}:{counter[value]}"
        for value in sorted(counter, key=lambda v: (-counter[v], v))
    )


def mf_manual_key(row: dict[str, str]) -> tuple[str, str, str, str, str]:
    return (
        row["organism"],
        row["gene"],
        row["annotation_index"],
        row["reactome_id"],
        row["term_id"],
    )


def repeated_event_bucket(rows: list[dict[str, str]]) -> str:
    buckets = {row["candidate_bucket"] for row in rows}
    verdicts = {row["candidate_verdict"] for row in rows}

    if buckets & MANUAL_FAILURE_BUCKETS:
        return "mixed_manual_failure"
    if "reaction_mf_refine" in verdicts or "insufficient_event_detail" in verdicts:
        return "mixed_refinement"
    if verdicts == {"reaction_mf_exact"}:
        return "uniform_exact"
    return "needs_review"


def repeated_event_priority(audit_bucket: str) -> str:
    if audit_bucket == "mixed_manual_failure":
        return "HIGH"
    if audit_bucket in {"mixed_refinement", "needs_review"}:
        return "MEDIUM"
    return "LOW"


def summarize_repeated_mf_events(mf_rows: list[dict[str, str]]) -> list[dict[str, str]]:
    rows_by_reactome: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in mf_rows:
        rows_by_reactome[row["reactome_id"]].append(row)

    repeated_events = []
    for reactome_id, rows in rows_by_reactome.items():
        genes = sorted({row["gene"] for row in rows})
        if len(genes) <= 1:
            continue

        bucket = repeated_event_bucket(rows)
        title = next(
            (
                row["reactome_display_name"] or row["reactome_title"]
                for row in rows
                if row["reactome_display_name"] or row["reactome_title"]
            ),
            "",
        )
        terms = {f"{row['term_id']} {row['term_label']}".strip() for row in rows}
        row_details = [
            (
                f"{row['organism']}/{row['gene']}"
                f":{row['review_action']}/{row['candidate_verdict']}"
            )
            for row in sorted(rows, key=lambda row: (row["organism"], row["gene"]))
        ]

        repeated_events.append(
            {
                "reactome_id": reactome_id,
                "reactome_display_name": title,
                "reactome_species": "|".join(
                    sorted(
                        {
                            row["reactome_species"]
                            for row in rows
                            if row["reactome_species"]
                        }
                    )
                ),
                "row_count": str(len(rows)),
                "gene_count": str(len(genes)),
                "organisms": "|".join(sorted({row["organism"] for row in rows})),
                "genes": "|".join(genes),
                "actions": counter_summary(
                    Counter(row["review_action"] for row in rows)
                ),
                "candidate_verdicts": counter_summary(
                    Counter(row["candidate_verdict"] for row in rows)
                ),
                "candidate_buckets": counter_summary(
                    Counter(row["candidate_bucket"] for row in rows)
                ),
                "terms": "|".join(sorted(terms)),
                "audit_bucket": bucket,
                "audit_priority": repeated_event_priority(bucket),
                "has_mixed_actions": str(
                    len({row["review_action"] for row in rows}) > 1
                ).lower(),
                "has_mixed_verdicts": str(
                    len({row["candidate_verdict"] for row in rows}) > 1
                ).lower(),
                "has_manual_failure": str(
                    bool(
                        {row["candidate_bucket"] for row in rows}
                        & MANUAL_FAILURE_BUCKETS
                    )
                ).lower(),
                "has_local_module_mf": str(
                    any(
                        "local_module_mf" in row["candidate_flags"].split("|")
                        for row in rows
                    )
                ).lower(),
                "row_details": "|".join(row_details),
            }
        )

    priority_order = {"HIGH": 0, "MEDIUM": 1, "LOW": 2}
    return sorted(
        repeated_events,
        key=lambda row: (
            priority_order[row["audit_priority"]],
            row["audit_bucket"],
            -int(row["row_count"]),
            row["reactome_id"],
        ),
    )


def load_manual_mf_verdicts(
    path: Path,
) -> dict[tuple[str, str, str, str, str], dict[str, str]]:
    if not path.exists():
        return {}

    overrides: dict[tuple[str, str, str, str, str], dict[str, str]] = {}
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        missing_fields = set(MANUAL_MF_VERDICT_FIELDS) - set(reader.fieldnames or [])
        if missing_fields:
            fields = ", ".join(sorted(missing_fields))
            raise ValueError(f"{path} is missing manual verdict fields: {fields}")

        for row in reader:
            key = mf_manual_key(row)
            if key in overrides:
                raise ValueError(f"duplicate manual MF verdict key: {key}")
            overrides[key] = {
                "manual_verdict": compact(row.get("manual_verdict")),
                "manual_bucket": compact(row.get("manual_bucket")),
                "manual_reason": compact(row.get("manual_reason")),
            }
    return overrides


def classify_mf_slice(
    gene_rows: list[dict[str, str]],
    module_rows: list[dict[str, str]],
    manual_mf_verdicts: dict[tuple[str, str, str, str, str], dict[str, str]],
) -> list[dict[str, str]]:
    module_mfs_by_reactome: dict[str, set[str]] = defaultdict(set)
    for row in module_rows:
        if row["scope"] != "activity_evidence" or not row["function_id"]:
            continue
        label = row["function_label"] or row["function_id"]
        module_mfs_by_reactome[row["reactome_id"]].add(
            f"{row['module_id']}:{row['function_id']} {label}"
        )

    mf_rows = [row for row in gene_rows if row["aspect"] == "MF"]
    genes_by_reactome: dict[str, set[str]] = defaultdict(set)
    for row in mf_rows:
        genes_by_reactome[row["reactome_id"]].add(row["gene"])

    classified_rows = []
    used_manual_keys = set()
    for row in mf_rows:
        flags = []
        title = (row["reactome_display_name"] or row["reactome_title"]).lower()
        matching_module_mfs = module_mfs_by_reactome.get(row["reactome_id"], set())
        manual_verdict = manual_mf_verdicts.get(mf_manual_key(row), {})
        if manual_verdict:
            used_manual_keys.add(mf_manual_key(row))
            flags.append("manual_verdict")

        if matching_module_mfs:
            flags.append("local_module_mf")
        if len(genes_by_reactome[row["reactome_id"]]) > 1:
            flags.append("multi_gene_reactome_id")
        if title.startswith("defective "):
            flags.append("reactome_disease_event")
        if row["reactome_cached"] != "yes":
            flags.append("uncached_reactome")
        if "todo: fetch title" in title:
            flags.append("missing_reactome_title")

        classified_rows.append(
            {
                **row,
                "candidate_verdict": manual_verdict.get("manual_verdict")
                or MF_VERDICT_BY_ACTION.get(row["review_action"], ""),
                "candidate_bucket": manual_verdict.get("manual_bucket")
                or MF_BUCKET_BY_ACTION.get(row["review_action"], "needs_manual_bucket"),
                "manual_verdict": manual_verdict.get("manual_verdict", ""),
                "manual_bucket": manual_verdict.get("manual_bucket", ""),
                "manual_reason": manual_verdict.get("manual_reason", ""),
                "candidate_flags": "|".join(flags),
                "genes_for_reactome_id": str(
                    len(genes_by_reactome[row["reactome_id"]])
                ),
                "matching_module_mfs": "|".join(sorted(matching_module_mfs)),
            }
        )

    unused_manual_keys = set(manual_mf_verdicts) - used_manual_keys
    if unused_manual_keys:
        keys = ", ".join(str(key) for key in sorted(unused_manual_keys))
        raise ValueError(f"manual MF verdicts did not match current MF rows: {keys}")

    return sorted(
        classified_rows,
        key=lambda row: (
            row["candidate_bucket"],
            row["organism"],
            row["gene"],
            int(row["annotation_index"]),
        ),
    )


def write_mf_slice_results(path: Path, mf_rows: list[dict[str, str]]) -> None:
    repair_rows = [
        row
        for row in mf_rows
        if row["review_action"] in {"MODIFY", "MARK_AS_OVER_ANNOTATED"}
    ]
    multi_gene_events = defaultdict(
        lambda: {"rows": 0, "genes": set(), "actions": Counter(), "title": ""}
    )
    for row in mf_rows:
        if int(row["genes_for_reactome_id"]) <= 1:
            continue
        event = multi_gene_events[row["reactome_id"]]
        event["rows"] += 1
        event["genes"].add(row["gene"])
        event["actions"][row["review_action"]] += 1
        event["title"] = row["reactome_display_name"] or row["reactome_title"]

    top_events = sorted(
        multi_gene_events.items(),
        key=lambda item: (-item[1]["rows"], item[0]),
    )[:10]

    path.write_text(
        "\n\n".join(
            [
                '---\ntitle: "Reactome MF Verdict Slice"\n---',
                "# Reactome MF Verdict Slice",
                "Generated by `inventory_reactome.py` from the molecular-function "
                "subset of `data/gene_reactome_annotations.tsv`.",
                "## Candidate Verdicts\n\n"
                + markdown_table(
                    ["Candidate verdict", "Rows"],
                    top_counts(mf_rows, "candidate_verdict", 20),
                ),
                "## Review-Action Buckets\n\n"
                + markdown_table(
                    ["Bucket", "Rows"],
                    top_counts(mf_rows, "candidate_bucket", 20),
                ),
                "## Manual Failure Modes\n\n"
                + markdown_table(
                    ["Failure mode", "Rows"],
                    top_counts(
                        (row for row in mf_rows if row["manual_bucket"]),
                        "manual_bucket",
                        20,
                    ),
                ),
                "## Existing Review Actions\n\n"
                + markdown_table(
                    ["Review action", "Rows"],
                    top_counts(mf_rows, "review_action", 20),
                ),
                "## Repeated Reactome Events\n\n"
                + markdown_table(
                    [
                        "Reactome ID",
                        "Rows",
                        "Genes",
                        "Actions",
                        "Event",
                    ],
                    [
                        [
                            reactome_id,
                            data["rows"],
                            len(data["genes"]),
                            ", ".join(
                                f"{action}:{count}"
                                for action, count in data["actions"].most_common()
                            ),
                            data["title"],
                        ]
                        for reactome_id, data in top_events
                    ],
                ),
                "## Repair-Prone GO Terms\n\n"
                + markdown_table(
                    ["GO term in MODIFY/MARK_AS_OVER_ANNOTATED rows", "Rows"],
                    [
                        [f"{term_id} {label}", count]
                        for (term_id, label), count in Counter(
                            (row["term_id"], row["term_label"]) for row in repair_rows
                        ).most_common(10)
                    ],
                ),
                "## Output Table\n\n"
                "- [`data/mf_verdict_slice.tsv`](data/mf_verdict_slice.tsv)\n"
                "- [`data/repeated_mf_events.tsv`](data/repeated_mf_events.tsv)\n"
                "- Manual overrides: "
                "[`mf_manual_verdicts.tsv`](mf_manual_verdicts.tsv)",
            ]
        )
        + "\n",
        encoding="utf-8",
    )


def write_repeated_mf_results(path: Path, repeated_rows: list[dict[str, str]]) -> None:
    high_priority = [row for row in repeated_rows if row["audit_priority"] == "HIGH"][
        :10
    ]
    medium_priority = [
        row for row in repeated_rows if row["audit_priority"] == "MEDIUM"
    ][:10]

    path.write_text(
        "\n\n".join(
            [
                '---\ntitle: "Repeated Reactome MF Events"\n---',
                "# Repeated Reactome MF Events",
                "Generated by `inventory_reactome.py` from repeated Reactome "
                "stable IDs in the molecular-function slice.",
                "## Headline Counts\n\n"
                + markdown_table(
                    ["Measure", "Count"],
                    [
                        ["Repeated stable IDs", len(repeated_rows)],
                        [
                            "Rows under repeated stable IDs",
                            sum(int(row["row_count"]) for row in repeated_rows),
                        ],
                        [
                            "Mixed review-action events",
                            sum(
                                row["has_mixed_actions"] == "true"
                                for row in repeated_rows
                            ),
                        ],
                        [
                            "Mixed candidate-verdict events",
                            sum(
                                row["has_mixed_verdicts"] == "true"
                                for row in repeated_rows
                            ),
                        ],
                        [
                            "Events with manual failure modes",
                            sum(
                                row["has_manual_failure"] == "true"
                                for row in repeated_rows
                            ),
                        ],
                    ],
                ),
                "## Audit Buckets\n\n"
                + markdown_table(
                    ["Audit bucket", "Events"],
                    top_counts(repeated_rows, "audit_bucket", 10),
                ),
                "## High-Priority Mixed Events\n\n"
                + markdown_table(
                    [
                        "Reactome ID",
                        "Rows",
                        "Genes",
                        "Verdicts",
                        "Event",
                    ],
                    [
                        [
                            row["reactome_id"],
                            row["row_count"],
                            row["genes"],
                            row["candidate_verdicts"],
                            row["reactome_display_name"],
                        ]
                        for row in high_priority
                    ],
                ),
                "## Medium-Priority Refinement Events\n\n"
                + markdown_table(
                    [
                        "Reactome ID",
                        "Rows",
                        "Genes",
                        "Verdicts",
                        "Event",
                    ],
                    [
                        [
                            row["reactome_id"],
                            row["row_count"],
                            row["genes"],
                            row["candidate_verdicts"],
                            row["reactome_display_name"],
                        ]
                        for row in medium_priority
                    ],
                ),
                "## Output Table\n\n"
                "- [`data/repeated_mf_events.tsv`](data/repeated_mf_events.tsv)",
            ]
        )
        + "\n",
        encoding="utf-8",
    )


def write_results(
    path: Path,
    gene_rows: list[dict[str, str]],
    module_rows: list[dict[str, str]],
    gocam_rows: list[dict[str, str]],
) -> None:
    modules = defaultdict(lambda: {"title": "", "rows": 0, "ids": set()})
    for row in module_rows:
        entry = modules[row["module_id"]]
        entry["title"] = row["module_title"]
        entry["rows"] += 1
        entry["ids"].add(row["reactome_id"])
    top_modules = sorted(
        modules.items(),
        key=lambda item: (-len(item[1]["ids"]), -item[1]["rows"], item[0]),
    )[:10]

    overlapping_gocams = [
        row for row in gocam_rows if row["in_reactome_module"] == "true"
    ]

    path.write_text(
        "\n\n".join(
            [
                '---\ntitle: "Reactome Inventory Results"\n---',
                "# Reactome Inventory Results",
                "Generated by `inventory_reactome.py` from local gene reviews, "
                "module YAMLs, cached Reactome records, and `gocams/index.tsv`.",
                "## Headline Counts\n\n"
                + markdown_table(
                    ["Inventory", "Rows", "Distinct Reactome IDs"],
                    [
                        [
                            "Gene-review existing annotations",
                            len(gene_rows),
                            len({row["reactome_id"] for row in gene_rows}),
                        ],
                        [
                            "Module source citations",
                            len(module_rows),
                            len({row["reactome_id"] for row in module_rows}),
                        ],
                        [
                            "Human GO-CAM activities",
                            len(gocam_rows),
                            "n/a",
                        ],
                        [
                            "Human GO-CAM activities overlapping Reactome-citing modules",
                            len(overlapping_gocams),
                            "n/a",
                        ],
                    ],
                ),
                "## Gene-Review Rows By Aspect\n\n"
                + markdown_table(
                    ["Aspect", "Rows"], top_counts(gene_rows, "aspect", 10)
                ),
                "## Gene-Review Rows By Action\n\n"
                + markdown_table(
                    ["Review action", "Rows"],
                    top_counts(gene_rows, "review_action", 10),
                ),
                "## Gene-Review Rows By Organism\n\n"
                + markdown_table(
                    ["Organism", "Rows"], top_counts(gene_rows, "organism", 10)
                ),
                "## Reactome-Rich Modules\n\n"
                + markdown_table(
                    ["Module", "Unique Reactome IDs", "Source rows"],
                    [
                        [module_id, len(data["ids"]), data["rows"]]
                        for module_id, data in top_modules
                    ],
                ),
                "## Output Tables\n\n"
                "- [`data/gene_reactome_annotations.tsv`](data/gene_reactome_annotations.tsv)\n"
                "- [`data/module_reactome_sources.tsv`](data/module_reactome_sources.tsv)\n"
                "- [`data/gocam_human_activities.tsv`](data/gocam_human_activities.tsv)\n"
                "- [`data/mf_verdict_slice.tsv`](data/mf_verdict_slice.tsv)\n"
                "- [`data/repeated_mf_events.tsv`](data/repeated_mf_events.tsv)",
            ]
        )
        + "\n",
        encoding="utf-8",
    )


def parse_args() -> argparse.Namespace:
    here = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(
        description="Inventory local Reactome links in gene reviews, modules, and GO-CAMs."
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=here.parents[1],
        help="Repository root. Defaults to this script's repository.",
    )
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=here / "data",
        help="Output directory for TSV inventories.",
    )
    parser.add_argument(
        "--results",
        type=Path,
        default=here / "RESULTS.md",
        help="Markdown summary to write.",
    )
    parser.add_argument(
        "--mf-slice-results",
        type=Path,
        default=here / "MF_VERDICT_SLICE.md",
        help="Markdown summary of the Reactome-backed MF slice to write.",
    )
    parser.add_argument(
        "--mf-manual-verdicts",
        type=Path,
        default=here / "mf_manual_verdicts.tsv",
        help="Manual verdict table for MF rows that cannot be inferred from review action.",
    )
    parser.add_argument(
        "--repeated-mf-results",
        type=Path,
        default=here / "REPEATED_MF_EVENTS.md",
        help="Markdown summary of repeated multi-gene Reactome MF stable IDs.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    root = args.root.resolve()
    out_dir = args.out_dir.resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    reactome_cache = load_reactome_cache(root)
    gene_rows = inventory_gene_reviews(root, reactome_cache)
    module_rows = inventory_modules(root, reactome_cache)
    gocam_rows = inventory_gocams(root, module_rows)
    manual_mf_verdicts = load_manual_mf_verdicts(args.mf_manual_verdicts.resolve())
    mf_slice_rows = classify_mf_slice(gene_rows, module_rows, manual_mf_verdicts)
    repeated_mf_rows = summarize_repeated_mf_events(mf_slice_rows)

    write_tsv(out_dir / "gene_reactome_annotations.tsv", GENE_FIELDS, gene_rows)
    write_tsv(out_dir / "module_reactome_sources.tsv", MODULE_FIELDS, module_rows)
    write_tsv(out_dir / "gocam_human_activities.tsv", GOCAM_FIELDS, gocam_rows)
    write_tsv(out_dir / "mf_verdict_slice.tsv", MF_SLICE_FIELDS, mf_slice_rows)
    write_tsv(
        out_dir / "repeated_mf_events.tsv",
        REPEATED_MF_EVENT_FIELDS,
        repeated_mf_rows,
    )
    write_results(args.results.resolve(), gene_rows, module_rows, gocam_rows)
    write_mf_slice_results(args.mf_slice_results.resolve(), mf_slice_rows)
    write_repeated_mf_results(args.repeated_mf_results.resolve(), repeated_mf_rows)

    print(f"gene_reactome_annotations\t{len(gene_rows)}")
    print(f"module_reactome_sources\t{len(module_rows)}")
    print(f"gocam_human_activities\t{len(gocam_rows)}")
    print(f"mf_verdict_slice\t{len(mf_slice_rows)}")
    print(f"repeated_mf_events\t{len(repeated_mf_rows)}")


if __name__ == "__main__":
    main()
