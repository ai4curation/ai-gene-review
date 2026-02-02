#!/usr/bin/env python3
"""
Scan geneontology/go-annotation issues for ARBA mentions.

This script searches for open issues mentioning ARBA rules and extracts
the ARBA IDs. It can be run standalone for testing or called from a
GitHub Actions workflow.

Usage:
    uv run scripts/scan_arba_issues.py
    uv run scripts/scan_arba_issues.py --max-issues 100
    uv run scripts/scan_arba_issues.py --output json
"""

import json
import re
import subprocess
from typing import Optional

import typer

app = typer.Typer(help="Scan go-annotation issues for ARBA mentions")

ARBA_PATTERN = re.compile(r"ARBA[0-9]{8}")


def search_issues(max_issues: int = 50) -> list[dict]:
    """
    Search for ARBA mentions in geneontology/go-annotation issues.

    Returns a list of issue dicts with number, title, body, url.
    """
    cmd = [
        "gh",
        "search",
        "issues",
        "ARBA",
        "--repo",
        "geneontology/go-annotation",
        "--state",
        "open",
        "--limit",
        str(max_issues),
        "--json",
        "number,title,body,url",
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        typer.echo(f"Warning: gh search failed: {result.stderr}", err=True)
        return []

    return json.loads(result.stdout) if result.stdout.strip() else []


def extract_arba_ids(issues: list[dict]) -> list[str]:
    """
    Extract unique ARBA IDs from issue titles and bodies.

    >>> extract_arba_ids([{"title": "Problem with ARBA00012345", "body": "See ARBA00067890"}])
    ['ARBA00012345', 'ARBA00067890']
    >>> extract_arba_ids([{"title": "No mentions here", "body": "Nothing"}])
    []
    """
    arba_ids = set()
    for issue in issues:
        title = issue.get("title", "")
        body = issue.get("body", "") or ""
        arba_ids.update(ARBA_PATTERN.findall(title))
        arba_ids.update(ARBA_PATTERN.findall(body))
    return sorted(arba_ids)


def format_github_output(arba_ids: list[str]) -> str:
    """
    Format output for GitHub Actions.

    Returns lines to append to $GITHUB_OUTPUT.
    """
    lines = []
    if arba_ids:
        arba_json = json.dumps(arba_ids)
        lines.append(f"arba_ids={arba_json}")
        lines.append("has_arbas=true")
    else:
        lines.append("arba_ids=")
        lines.append("has_arbas=false")
    return "\n".join(lines)


@app.command()
def scan(
    max_issues: int = typer.Option(50, "--max-issues", "-n", help="Maximum issues to scan"),
    output: str = typer.Option(
        "text", "--output", "-o", help="Output format: text, json, or github"
    ),
    github_output: Optional[str] = typer.Option(
        None, "--github-output", envvar="GITHUB_OUTPUT", help="Path to GITHUB_OUTPUT file"
    ),
):
    """
    Scan go-annotation issues for ARBA mentions.

    Requires the `gh` CLI to be installed and authenticated.
    """
    typer.echo("Searching for ARBA mentions in geneontology/go-annotation issues...", err=True)

    issues = search_issues(max_issues)

    if output == "text" or output == "github":
        typer.echo(f"Found {len(issues)} issues mentioning ARBA:", err=True)
        for issue in issues:
            typer.echo(f"  - #{issue['number']}: {issue['title']}", err=True)

    arba_ids = extract_arba_ids(issues)

    if output == "json":
        print(json.dumps({"arba_ids": arba_ids, "issue_count": len(issues)}, indent=2))
    elif output == "github":
        github_out = format_github_output(arba_ids)
        print(github_out)
        if github_output:
            with open(github_output, "a") as f:
                f.write(github_out + "\n")
            typer.echo(f"Wrote output to {github_output}", err=True)
    else:  # text
        if arba_ids:
            typer.echo(f"\nFound {len(arba_ids)} unique ARBA IDs:")
            for arba_id in arba_ids:
                typer.echo(f"  {arba_id}")
        else:
            typer.echo("\nNo ARBA IDs found in issues.")

    # Exit with code 0 if ARBAs found, 1 if none (useful for scripting)
    raise typer.Exit(0 if arba_ids else 1)


if __name__ == "__main__":
    app()
