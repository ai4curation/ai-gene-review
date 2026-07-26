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

    The key is read from the ``---``-delimited frontmatter block only, because full text can
    quote the string in prose. An earlier version guarded against that by truncating the read at
    a fixed byte count, which would silently miss the key in any record whose frontmatter grew
    past it; parsing the actual block has no such cliff.
    """
    availability: dict[str, bool] = {}
    for path in publications_dir.glob("PMID_*.md"):
        frontmatter = _frontmatter(path)
        if frontmatter is None or "full_text_available" not in frontmatter:
            continue
        availability[path.stem.split("_", 1)[1]] = bool(
            frontmatter["full_text_available"]
        )
    return availability


def _frontmatter(path: Path) -> dict | None:
    """Parse a cached publication's YAML frontmatter; None if absent or not a mapping."""
    text = path.read_text()
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    parsed = yaml.safe_load(text[3:end])
    return parsed if isinstance(parsed, dict) else None


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
    """Delete the reference-level ``full_text_unavailable`` key for the named PMIDs, in place.

    The file is edited line-wise rather than round-tripped through ``yaml.dump`` so that the
    rest of the review — quoting style, block scalars, key order, comments — is untouched. A
    reformat would produce an unreviewable diff across dozens of unrelated genes.

    Only the flag at the **same indentation as the reference's own keys** is removed. A first
    version matched the flag at any indentation until the next ``id:`` line, which also stripped
    a *Finding*-level flag under ``findings:`` (this happened to ``genes/MYCTU/clpP2``,
    ``PMID:35507665``). :func:`find_stale_flags` only inspects reference-level flags, so it
    could not see the over-removal — the detector and the mutator have to agree on scope, or the
    post-fix re-check is structurally blind to the damage.

    ``reference_id:`` deliberately does not reset the current reference either: a
    ``SupportingTextInReference`` block is keyed by that name, and treating it as a new reference
    would let a nested flag be attributed to it.
    """
    lines = review_path.read_text().splitlines(keepends=True)
    wanted = {f"PMID:{pmid}" for pmid in pmids}
    out: list[str] = []
    current_id: str | None = None
    key_indent: int | None = None
    removed = 0
    for line in lines:
        id_match = re.match(r"(\s*)(-\s*)?id:\s*(\S+)", line)
        if id_match is not None:
            current_id = id_match.group(3).strip("\"'")
            # Sibling keys of this reference sit at the column where `id:` itself starts.
            key_indent = len(id_match.group(1)) + len(id_match.group(2) or "")
        flag_match = re.match(r"(\s*)full_text_unavailable:\s*true\s*$", line)
        if (
            flag_match is not None
            and current_id in wanted
            and len(flag_match.group(1)) == key_indent
        ):
            removed += 1
            continue
        out.append(line)
    if removed:
        review_path.write_text("".join(out))
    return removed


def audit(
    repo_root: Path,
    gene_dirs: list[Path] | None = None,
    fix: bool = False,
    echo=print,
) -> int:
    """Report, and optionally remove, stale flags. Returns a process exit code.

    Shared by the module entry point and the ``ai-gene-review`` subcommand. It exists because a
    first version duplicated this logic in both places and the copies had already drifted — the
    CLI copy silently lost ``--gene-dir`` and reported a different failure message.
    """
    publications = repo_root / "publications"
    if not publications.is_dir():
        raise FileNotFoundError(f"no publications directory under {repo_root}")

    availability = cached_full_text_availability(publications)
    if gene_dirs:
        review_paths = sorted(p for d in gene_dirs for p in d.glob("*-ai-review.yaml"))
    else:
        review_paths = sorted((repo_root / "genes").glob("*/*/*-ai-review.yaml"))

    stale = find_stale_flags(review_paths, availability)
    echo(
        f"scanned {len(review_paths)} reviews against {len(availability)} cached publications"
    )
    if not stale:
        echo("no stale full_text_unavailable flags")
        return 0

    by_review: dict[Path, list[StaleFlag]] = {}
    for flag in stale:
        by_review.setdefault(flag.review_path, []).append(flag)

    suppressed = sum(1 for f in stale if f.suppressed_evidence)
    echo(
        f"{len(stale)} stale flag(s) in {len(by_review)} review(s); "
        f"{suppressed} sit on a reference with zero findings"
    )
    for review_path, flags in sorted(by_review.items()):
        pmids = ", ".join(
            f.pmid + (" (0 findings)" if f.suppressed_evidence else "") for f in flags
        )
        echo(f"  {len(flags):3d}  {review_path}: {pmids}")

    if not fix:
        return 1

    total = sum(
        remove_stale_flags(rp, {f.pmid for f in fl})
        for rp, fl in sorted(by_review.items())
    )
    echo(f"removed {total} flag(s)")
    if total != len(stale):
        # The mutator and the detector must agree on scope; a mismatch means one of them is
        # looking at flags the other cannot see, which is how a nested Finding-level flag was
        # once stripped without ever being reported.
        echo(
            f"ERROR: detected {len(stale)} flag(s) but removed {total} - scope mismatch"
        )
        return 1
    if find_stale_flags(sorted(by_review), availability):
        echo("ERROR: stale flags survived the fix")
        return 1
    echo("verified: no stale flags remain in the edited reviews")
    return 0


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
    try:
        code = audit(repo_root, gene_dir, fix, echo=typer.echo)
    except FileNotFoundError as exc:
        raise typer.BadParameter(str(exc)) from exc
    if code:
        raise typer.Exit(code=code)


if __name__ == "__main__":
    app()
