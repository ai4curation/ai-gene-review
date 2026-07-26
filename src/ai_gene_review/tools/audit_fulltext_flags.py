"""Audit ``full_text_unavailable`` flags in gene reviews against the publication cache.

A reference marked ``full_text_unavailable: true`` whose cached publication actually *has*
full text is a silent defect: no validator checks the pair, and the flag discourages anyone
from extracting the evidence the annotation needs. On human CDK2, ``PMID:11953320`` carried
the flag while ``publications/PMID_11953320.md`` had ``full_text_available: true`` and a
PMCID — and the reference had zero ``findings``.

**A stale flag together with an empty ``findings`` list is the signature to look for**: the
flag suppressed the extraction that would have supported the annotation.

Only the ``flag says unavailable`` / ``cache says available`` direction is reported. The
converse (no flag, cache lacks full text) is not a defect — the flag is optional.

Usage::

    ai-gene-review audit-fulltext-flags                  # report every stale flag
    ai-gene-review audit-fulltext-flags --fix            # also remove them

    # module form, which additionally supports narrowing to specific genes:
    python -m ai_gene_review.tools.audit_fulltext_flags --gene-dir genes/human/CDK2

Exits non-zero when stale flags remain, so it is usable as a CI gate.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

import typer
import yaml

app = typer.Typer(help=__doc__)

# The cache frontmatter sits at the top of the file; reading the whole publication (some are
# thousands of lines of full text) to find one key would make a repo-wide sweep needlessly slow.
_FRONTMATTER_BYTES = 4096
_FULL_TEXT_RE = re.compile(r"^full_text_available:\s*(\S+)", re.MULTILINE)


@dataclass(frozen=True)
class StaleFlag:
    """One reference whose ``full_text_unavailable`` flag is contradicted by the cache."""

    review_path: Path
    pmid: str
    n_findings: int

    @property
    def suppressed_evidence(self) -> bool:
        """True when the stale flag plausibly stopped anyone extracting findings."""
        return self.n_findings == 0


def cached_full_text_availability(publications_dir: Path) -> dict[str, bool]:
    """Map PMID -> whether its cached record reports full text.

    PMIDs whose cache omits ``full_text_available`` are absent from the result, so callers
    cannot mistake "not recorded" for "not available".
    """
    availability: dict[str, bool] = {}
    for path in publications_dir.glob("PMID_*.md"):
        with path.open() as handle:
            head = handle.read(_FRONTMATTER_BYTES)
        match = _FULL_TEXT_RE.search(head)
        if match is not None:
            availability[path.stem.split("_", 1)[1]] = (
                match.group(1).strip().lower() == "true"
            )
    return availability


def find_stale_flags(
    review_paths: list[Path], availability: dict[str, bool]
) -> list[StaleFlag]:
    """Collect references flagged unavailable whose cache reports full text."""
    stale: list[StaleFlag] = []
    for review_path in review_paths:
        doc = yaml.safe_load(review_path.read_text())
        if not isinstance(doc, dict):
            continue
        for reference in doc.get("references") or []:
            if reference.get("full_text_unavailable") is not True:
                continue
            identifier = str(reference.get("id") or "")
            if not identifier.startswith("PMID:"):
                continue
            pmid = identifier.split(":", 1)[1]
            if availability.get(pmid):
                stale.append(
                    StaleFlag(
                        review_path=review_path,
                        pmid=pmid,
                        n_findings=len(reference.get("findings") or []),
                    )
                )
    return stale


def remove_stale_flags(review_path: Path, pmids: set[str]) -> int:
    """Delete the ``full_text_unavailable`` key for the named PMIDs, editing text in place.

    The file is edited line-wise rather than round-tripped through ``yaml.dump`` so that the
    rest of the review — quoting style, block scalars, key order, comments — is untouched. A
    reformat would produce an unreviewable diff across dozens of unrelated genes.
    """
    lines = review_path.read_text().splitlines(keepends=True)
    wanted = {f"PMID:{pmid}" for pmid in pmids}
    out: list[str] = []
    current_id: str | None = None
    removed = 0
    for line in lines:
        id_match = re.match(r"\s*-?\s*id:\s*(\S+)", line)
        if id_match is not None:
            current_id = id_match.group(1).strip("\"'")
        if (
            current_id in wanted
            and re.match(r"\s*full_text_unavailable:\s*true\s*$", line) is not None
        ):
            removed += 1
            continue
        out.append(line)
    if removed:
        review_path.write_text("".join(out))
    return removed


@app.command()
def main(
    repo_root: Path = typer.Option(Path("."), help="Repository root."),
    gene_dir: list[Path] = typer.Option(
        None, help="Limit to specific gene directories; defaults to all of genes/."
    ),
    fix: bool = typer.Option(
        False, "--fix", help="Remove the stale flags as well as report."
    ),
) -> None:
    """Report (and optionally remove) ``full_text_unavailable`` flags the cache contradicts."""
    publications = repo_root / "publications"
    if not publications.is_dir():
        raise typer.BadParameter(f"no publications directory under {repo_root}")

    availability = cached_full_text_availability(publications)
    if gene_dir:
        review_paths = sorted(p for d in gene_dir for p in d.glob("*-ai-review.yaml"))
    else:
        review_paths = sorted((repo_root / "genes").glob("*/*/*-ai-review.yaml"))

    stale = find_stale_flags(review_paths, availability)
    typer.echo(
        f"scanned {len(review_paths)} reviews against {len(availability)} cached publications"
    )
    if not stale:
        typer.echo("no stale full_text_unavailable flags")
        return

    by_review: dict[Path, list[StaleFlag]] = {}
    for flag in stale:
        by_review.setdefault(flag.review_path, []).append(flag)

    suppressed = sum(1 for f in stale if f.suppressed_evidence)
    typer.echo(
        f"{len(stale)} stale flag(s) in {len(by_review)} review(s); "
        f"{suppressed} sit on a reference with zero findings"
    )
    for review_path, flags in sorted(by_review.items()):
        pmids = ", ".join(
            f"{f.pmid}{' (0 findings)' if f.suppressed_evidence else ''}" for f in flags
        )
        typer.echo(f"  {len(flags):3d}  {review_path}: {pmids}")

    if not fix:
        raise typer.Exit(code=1)

    total = 0
    for review_path, flags in sorted(by_review.items()):
        total += remove_stale_flags(review_path, {f.pmid for f in flags})
    typer.echo(f"removed {total} flag(s)")

    remaining = find_stale_flags(sorted(by_review), availability)
    if remaining:
        typer.echo(f"ERROR: {len(remaining)} flag(s) survived the fix")
        raise typer.Exit(code=1)
    typer.echo("verified: no stale flags remain in the edited reviews")


if __name__ == "__main__":
    app()
