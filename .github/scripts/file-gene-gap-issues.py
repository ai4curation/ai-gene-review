"""Publish eligible packet rows selected by read-only triage, once per paper."""

import argparse
import json
import os
import re
import subprocess
from pathlib import Path

from ai_gene_review.litscan.gene_gap import ledger_references, reference_ids
from ai_gene_review.shadow_issues.guard import find_notification_hazards


def selected_ranks(execution_log: Path) -> set[int]:
    events = json.loads(execution_log.read_text())
    result = next((e for e in reversed(events) if e.get("type") == "result"), {})
    if result.get("subtype") != "success" or result.get("is_error"):
        raise ValueError("Triage did not return a successful result")
    # Allow prose introducing a single array and an optional Markdown fence.
    # Multiple arrays or nested objects make the decision ambiguous.
    selection = re.fullmatch(
        r"[^\[\]{}]*(\[[^\[\]{}]*\])\s*(?:```)?\s*", result["result"]
    )
    if selection is None:
        raise ValueError("Expected one final JSON list of integer ranks")
    ranks = json.loads(selection[1])
    if not isinstance(ranks, list) or not all(type(rank) is int for rank in ranks):
        raise ValueError("Expected a JSON list of integer ranks")
    return set(ranks)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("packet", type=Path)
    parser.add_argument("execution_log", type=Path)
    parser.add_argument("ledger", type=Path)
    args = parser.parse_args()
    packet = json.loads(args.packet.read_text())
    approved = selected_ranks(args.execution_log)
    eligible = [row for row in packet["candidates"] if row["issue_eligible"]]
    if approved - {row["rank"] for row in eligible}:
        raise ValueError("Triage selected a rank outside the packet's issue cap")
    seen = ledger_references(json.loads(args.ledger.read_text()))
    for row in eligible:
        if row["rank"] not in approved:
            continue
        paper = row["paper"]
        refs = {paper["reference_id"]} | reference_ids(
            f"doi:{paper['doi']} {paper['europe_pmc_url']}"
        )
        if seen & refs:
            continue
        body = Path(row["issue_body_path"]).read_text(encoding="utf-8")
        if find_notification_hazards(
            row["issue_title"] + "\n" + body, allowed_handles=frozenset()
        ):
            print(
                f"Skipping rank {row['rank']} because the issue would notify another user or repository"
            )
            continue
        subprocess.run(
            [
                "gh",
                "issue",
                "create",
                "--repo",
                os.environ["GITHUB_REPOSITORY"],
                "--title",
                row["issue_title"],
                "--label",
                ",".join(row["issue_labels"]),
                "--body-file",
                row["issue_body_path"],
            ],
            check=True,
        )
        seen.update(refs)


if __name__ == "__main__":
    main()
