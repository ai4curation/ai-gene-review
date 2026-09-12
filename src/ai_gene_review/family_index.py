"""Collect authored family reviews for the searchable Families project index."""

from __future__ import annotations

import re
from collections import Counter
from pathlib import Path
from typing import Any

import yaml

PUBLIC_SOURCE = "https://github.com/ai4curation/ai-gene-review/blob/main/"


def collect_family_reviews(repo_root: Path) -> list[dict[str, Any]]:
    """Index authored reviews, merging YAML and prose reports for the same entry.

    Metadata and deep-research files alone do not establish a reviewed family.
    Missing status/coherence stays unrecorded; a complete review does not imply
    family-wide term support. Pfam proposal status is not family review status.
    """
    paths = sorted((repo_root / "interpro").glob("*/*/*-review.yaml"))
    paths += sorted((repo_root / "interpro").glob("*/*/*-review.md"))
    grouped: dict[tuple[str, str], list[Path]] = {}
    for path in paths:
        identifier = path.name.removesuffix("-review.yaml").removesuffix("-review.md")
        database = path.relative_to(repo_root).parts[1]
        grouped.setdefault((database, identifier), []).append(path)

    benchmark = (
        repo_root / "projects/PROTNLM_EVALUATION/family-curation/family-index.md"
    )
    benchmark_ids = (
        set(re.findall(r"^## (PTHR\d+)\s*$", benchmark.read_text(), re.MULTILINE))
        if benchmark.exists()
        else set()
    )
    rows = []
    for (database, identifier), sources in sorted(grouped.items()):
        structured = next((p for p in sources if p.suffix == ".yaml"), None)
        data = (yaml.safe_load(structured.read_text()) or {}) if structured else {}
        metadata_path = (
            repo_root
            / "interpro"
            / database
            / identifier
            / f"{identifier}-metadata.yaml"
        )
        metadata = (
            (yaml.safe_load(metadata_path.read_text()) or {}).get("metadata", {})
            if metadata_path.exists()
            else {}
        )
        names = metadata.get("name") or {}
        official_name = (
            data.get("family_name")
            or data.get("pfam_name")
            or (names.get("name") if isinstance(names, dict) else names)
            or identifier
        )
        name = data.get("preferred_name") or official_name
        status = data.get("review_status") or "NOT_RECORDED"
        if not structured:
            for source in sources:
                match = re.search(
                    r"\*\*Status\*\*:\s*(DRAFT|IN_PROGRESS|COMPLETE)\b",
                    source.read_text(),
                )
                if match:
                    status = match.group(1)
                    break
        terms = data.get("term_assessments") or []
        proposals = data.get("proposed_annotations") or []
        scopes = dict(
            sorted(Counter(t["scope"] for t in terms if t.get("scope")).items())
        )
        representatives = {
            str(member["id"])
            for subfamily in data.get("subfamilies") or []
            for member in subfamily.get("representative_members") or []
            if member.get("id")
        }
        source_links = [
            {
                "url": PUBLIC_SOURCE + p.relative_to(repo_root).as_posix(),
                "label": "YAML" if p.suffix == ".yaml" else "Report",
            }
            for p in sources
        ]
        url = source_links[0]["url"]
        if database == "panther" and identifier in benchmark_ids:
            url = f"PROTNLM_EVALUATION/family-curation/family-index.html#{identifier.lower()}"
        research = any(
            any(p.parent.glob(f"{identifier}-deep-research-*.md")) for p in sources
        )
        summary = data.get("summary") or data.get("pfam_description") or ""
        searchable_terms = [t.get("assessed_term") or {} for t in terms] + [
            t.get("term") or {} for t in proposals
        ]
        search = " ".join(
            [identifier, str(name), str(official_name), summary, database]
            + [str(v) for term in searchable_terms for v in term.values()]
            + sorted(representatives)
        )
        rows.append(
            {
                "id": identifier,
                "name": name,
                "summary": summary,
                "database": database.upper(),
                "status": status,
                "coherence": data.get("functional_coherence") or "NOT_RECORDED",
                "scopes": scopes,
                "terms": len(terms) + len(proposals),
                "members": len(representatives)
                if structured and database == "panther"
                else None,
                "research": research,
                "sources": source_links,
                "url": url,
                "search": search,
            }
        )
    return rows
