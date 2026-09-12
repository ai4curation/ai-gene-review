"""Validate the explicitly scoped ProtNLM benchmark and context family reviews.

Run from any working directory with the repository environment, for example::

    UV_NO_SYNC=1 uv run python projects/PROTNLM_EVALUATION/family-curation/validate_families.py

Scope comes from family-groups.json plus additional-context-families.json. The
context-only families remain distinct from exact prediction-target assignments.
This performs mechanical validation; biological evidence relevance needs manual
review, and ontology validation is recorded separately.
"""

from __future__ import annotations

import gzip
import hashlib
import json
import os
import subprocess
from collections import Counter
from datetime import UTC, datetime
from functools import lru_cache
from pathlib import Path
from typing import Any

import yaml

from ai_gene_review.validation.family_gene_crosscheck import (
    check_family_gene_disagreement,
    check_pruning_conflicts,
    check_scope_violations,
    index_genes_by_family,
)
from ai_gene_review.validation.family_residue_validator import (
    SequenceCache,
    _panther_index,
    check_anchor_residues,
    check_controls,
    check_node_assessments,
    check_panther_ids,
    check_term_assessment_site_refs,
)
from ai_gene_review.validation.module_validator import load_paint_index

BUNDLE = Path(__file__).resolve().parent
ROOT = BUNDLE.parents[2]


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def write_json(path: Path, data: Any) -> None:
    path.write_text(json.dumps(data, indent=2) + "\n")


def resolve_reference(reference: str) -> Path | None:
    if reference.startswith("PMID:"):
        return ROOT / "publications" / (reference.replace(":", "_") + ".md")
    if reference.startswith("file:"):
        raw = reference[5:]
        candidates = [ROOT / raw, ROOT / "genes" / raw]
        return next((path for path in candidates if path.is_file()), candidates[0])
    return None


@lru_cache(maxsize=None)
def read_source(path: Path) -> str:
    if path.suffix == ".gz":
        with gzip.open(path, "rt") as stream:
            return stream.read()
    return path.read_text()


def check_quotes(value: Any, review_path: str) -> list[dict]:
    checks = []
    if isinstance(value, dict):
        if "reference_id" in value and "supporting_text" in value:
            reference = value["reference_id"]
            source = resolve_reference(reference)
            quote = value["supporting_text"]
            if source is None:
                status = "EXTERNAL_NOT_CHECKED"
            elif not source.is_file():
                status = "MISSING_SOURCE"
            elif quote in read_source(source):
                status = "PASS"
            else:
                status = "NOT_LITERAL_SUBSTRING"
            checks.append(
                {
                    "path": review_path,
                    "reference": reference,
                    "status": status,
                    "supporting_text": quote if status != "PASS" else None,
                }
            )
        for child in value.values():
            checks.extend(check_quotes(child, review_path))
    elif isinstance(value, list):
        for child in value:
            checks.extend(check_quotes(child, review_path))
    return checks


def frozen_sequence_cache() -> SequenceCache:
    """Use source-version sequences; other controls use the normal UniProt cache."""
    cache = SequenceCache(ROOT / ".cache/uniprot_seq")

    def add(record: dict) -> None:
        accession = record["primaryAccession"]
        cache._mem[accession] = record["sequence"]["value"]
        cache._versions[accession] = record["entryAudit"]["sequenceVersion"]

    for name in ["uniprot-records.jsonl.gz", "uniprot-retries.jsonl.gz"]:
        with gzip.open(BUNDLE / name, "rt") as stream:
            for line in stream:
                response = json.loads(line)
                if response["status"] == 200:
                    add(response["record"])
    for path in (BUNDLE / "evidence-c/controls").glob("*.json"):
        record = json.loads(path.read_text())
        if "primaryAccession" in record:
            add(record)
    return cache


def main() -> int:
    exact_families = set(json.loads((BUNDLE / "family-groups.json").read_text()))
    context_path = BUNDLE / "additional-context-families.json"
    context = json.loads(context_path.read_text()) if context_path.is_file() else []
    context_families = {row["family"] for row in context}
    families = sorted(exact_families | context_families)
    expected = [
        ROOT / "interpro/panther" / family / f"{family}-review.yaml"
        for family in families
    ]
    for row in context:
        assert (
            row["review"]
            == f"interpro/panther/{row['family']}/{row['family']}-review.yaml"
        )
    paths = [path for path in expected if path.is_file()]
    docs = {relative(path): yaml.safe_load(path.read_text()) for path in paths}
    result = {
        "checked_at": datetime.now(UTC).isoformat(),
        "exact_assignment_families": len(exact_families),
        "additional_context_families": sorted(context_families - exact_families),
        "expected_families": len(expected),
        "present_reviews": len(paths),
        "missing_reviews": [relative(path) for path in expected if not path.is_file()],
        "input_sha256": {
            relative(path): hashlib.sha256(path.read_bytes()).hexdigest()
            for path in paths
        },
    }
    command = [
        "uv",
        "run",
        "linkml-validate",
        "-s",
        "src/ai_gene_review/schema/family_review.yaml",
        "-C",
        "FamilyReview",
        *docs,
    ]
    schema = subprocess.run(
        command,
        cwd=ROOT,
        capture_output=True,
        text=True,
        env={**os.environ, "UV_NO_SYNC": "1"},
    )
    (BUNDLE / "schema-validation-all.txt").write_text(schema.stdout + schema.stderr)
    result["schema_returncode"] = schema.returncode
    panther = ROOT / "interpro/panther"
    labels, members, gaps = _panther_index(panther)
    paint = load_paint_index(panther)
    cache = frozen_sequence_cache()
    checks, sources, quotes = [], [], []
    for path, document in docs.items():
        try:
            outcomes = (
                check_panther_ids(document, labels, members, gaps)
                + check_term_assessment_site_refs(document)
                + check_node_assessments(document, paint)
                + check_anchor_residues(document, cache)
                + check_controls(document, cache)
            )
        except Exception as error:
            checks.append(
                {
                    "path": path,
                    "outcome": "FAIL",
                    "message": str(error),
                    "kind": "CHECK_EXCEPTION",
                }
            )
            outcomes = []
        for check in outcomes:
            checks.append(
                {
                    "path": path,
                    "outcome": check.outcome.value,
                    "message": str(check),
                    "kind": check.kind,
                }
            )
        for reference in document.get("references", []):
            source = resolve_reference(reference["id"])
            status = (
                ("PASS" if source.is_file() else "MISSING")
                if source
                else "EXTERNAL_NOT_CHECKED"
            )
            sources.append(
                {"path": path, "reference": reference["id"], "status": status}
            )
        quotes.extend(check_quotes(document, path))
    gene_index = index_genes_by_family(ROOT / "genes")
    crosschecks = []
    crosscheck_lines = []
    for path, document in docs.items():
        findings = (
            check_scope_violations(document, gene_index)
            + check_pruning_conflicts(document, gene_index)
            + check_family_gene_disagreement(document, gene_index)
        )
        for finding in findings:
            crosschecks.append(
                {
                    "path": path,
                    "kind": finding.kind,
                    "family": finding.family,
                    "gene": finding.gene,
                    "subfamily": finding.subfamily,
                    "term": finding.term,
                    "gene_action": finding.gene_action,
                    "verdict": finding.verdict.value,
                    "message": finding.message,
                }
            )
            crosscheck_lines.append(str(finding))
    conflicts = sum(row["verdict"] == "CONFLICT" for row in crosschecks)
    crosscheck_header = (
        f"family/gene cross-check over {len(paths)} family review(s): "
        f"{conflicts} conflict(s), {len(crosschecks) - conflicts} other finding(s)"
    )
    write_json(BUNDLE / "family-gene-crosscheck.json", crosschecks)
    (BUNDLE / "family-gene-crosscheck.txt").write_text(
        crosscheck_header + "\n" + "\n".join(crosscheck_lines) + "\n"
    )
    result.update(
        {
            "family_gene_crosscheck_summary": dict(
                Counter(row["verdict"] for row in crosschecks)
            ),
            "family_gene_crosscheck_conflicts": conflicts,
            "family_gene_crosscheck_scope": (
                "Checks explicit family grants and exclusions against existing gene reviews. "
                "UNRESOLVED family scope does not assert automatic consistency."
            ),
            "check_summary": dict(Counter(row["outcome"] for row in checks)),
            "source_summary": dict(Counter(row["status"] for row in sources)),
            "quote_summary": dict(Counter(row["status"] for row in quotes)),
            "checks": checks,
            "sources": sources,
            "quotes": quotes,
            "changed_during_validation": [
                relative(path)
                for path in paths
                if hashlib.sha256(path.read_bytes()).hexdigest()
                != result["input_sha256"][relative(path)]
            ],
        }
    )
    write_json(BUNDLE / "validation-all.json", result)
    failures = (
        result["missing_reviews"]
        + result["changed_during_validation"]
        + [row for row in checks if row["outcome"] == "FAIL"]
        + [row for row in crosschecks if row["verdict"] == "CONFLICT"]
        + [row for row in sources if row["status"] == "MISSING"]
        + [
            row
            for row in quotes
            if row["status"] not in {"PASS", "EXTERNAL_NOT_CHECKED"}
        ]
    )
    print(
        json.dumps(
            {
                key: value
                for key, value in result.items()
                if key not in {"input_sha256", "checks", "sources", "quotes"}
            },
            indent=2,
        )
    )
    if failures:
        print(json.dumps(failures, indent=2))
    return int(bool(schema.returncode or failures))


if __name__ == "__main__":
    raise SystemExit(main())
