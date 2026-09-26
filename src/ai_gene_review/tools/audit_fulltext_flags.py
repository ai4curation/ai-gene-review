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

from ai_gene_review.validation.supporting_text import NO_FULL_TEXT_CONTENT_TYPES

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

    When ``full_text_available`` is absent, ``content_type`` is consulted through the same
    ``NO_FULL_TEXT_CONTENT_TYPES`` negative list the validator uses. Skipping those records
    was right while ``content_type`` was unreadable here, but 1138 records omit the key and
    at least 242 of them name a full-text ``content_type`` -- so the audit and the validator
    disagreed by construction, and the audit's half of the disagreement is the one that
    hides false flags. The live case that forced this: ``PMID:38296963`` is
    ``content_type: full_text_pdf`` with a gold-OA local PDF, and carried the identical
    reference-level flag on both ARL8A and ARL8B. The ARL8B one was removed by hand as "the
    one genuinely false declaration"; the ARL8A one was invisible to this function.
    """
    availability: dict[str, bool] = {}
    for path in publications_dir.glob("PMID_*.md"):
        frontmatter = _frontmatter(path)
        if frontmatter is None:
            continue
        pmid = path.stem.split("_", 1)[1]
        if "full_text_available" in frontmatter:
            availability[pmid] = bool(frontmatter["full_text_available"])
            continue
        content_type = frontmatter.get("content_type")
        if isinstance(content_type, str):
            availability[pmid] = content_type.lower() not in NO_FULL_TEXT_CONTENT_TYPES
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


@dataclass(frozen=True)
class UnauditedFlag:
    """A ``full_text_unavailable`` flag that :func:`find_stale_flags` cannot see.

    Two kinds, both observed live:

    * **finding-level** -- the flag sits on a ``findings[]`` entry rather than on the
      reference. ``find_stale_flags`` only reads reference-level keys, so these were
      invisible to every audit.
    * **``file:`` reference** -- the flag claims the source text is not cached, about a file
      that is checked into this repository. ``cached_full_text_availability`` is keyed on
      PMIDs, and ``cached_full_text_available`` returns ``None`` (not ``False``) for a
      non-literature prefix, so such a flag scored as "not recorded" and passed.

    Found on ``genes/yeast/ESL1``: two finding-level flags under
    ``file:yeast/ESL1/ESL1-uniprot.txt``, both quotes verbatim in that very file.
    """

    review_path: Path
    reference_id: str
    finding_index: int | None
    reason: str


def _repo_file_for(reference_id: str, repo_root: Path) -> Path | None:
    """Resolve a ``file:`` reference to a path in the repo, or None."""
    if not reference_id.startswith("file:"):
        return None
    rel = reference_id.split(":", 1)[1]
    for candidate in (repo_root / rel, repo_root / "genes" / rel):
        if candidate.is_file():
            return candidate
    return None


def find_unaudited_flags(
    review_paths: list[Path], availability: dict[str, bool], repo_root: Path
) -> list[UnauditedFlag]:
    """Collect ``full_text_unavailable`` flags the reference-level PMID audit cannot reach.

    Reported separately from :func:`find_stale_flags` rather than merged into it, because
    ``--fix`` removes only reference-level PMID flags and :func:`audit` asserts that the
    detector and the mutator agree on scope. Folding these in would trip that guard on every
    run; the point of the guard is that a flag must not be stripped without being reported.
    """
    out: list[UnauditedFlag] = []
    for review_path in review_paths:
        doc = yaml.safe_load(review_path.read_text())
        if not isinstance(doc, dict):
            continue
        for reference in doc.get("references") or []:
            if not isinstance(reference, dict):
                continue
            identifier = str(reference.get("id") or "")
            source = _repo_file_for(identifier, repo_root)
            has_text = bool(source and source.read_text().strip())
            pmid = identifier.split(":", 1)[1] if identifier.startswith("PMID:") else None
            cached = availability.get(pmid) if pmid else None

            if reference.get("full_text_unavailable") is True and has_text:
                out.append(UnauditedFlag(review_path, identifier, None,
                                         f"source file is in the repo: {source}"))
            for index, finding in enumerate(reference.get("findings") or []):
                if not isinstance(finding, dict):
                    continue
                if finding.get("full_text_unavailable") is not True:
                    continue
                # Only demonstrably FALSE flags are reported. A finding-level flag on a
                # genuinely abstract-only record is accurate and common -- 30 of them in one
                # PR's changed files -- and reporting those as suspect would make the audit
                # noise, which is how a check stops being read.
                if has_text:
                    out.append(UnauditedFlag(review_path, identifier, index,
                                             f"source file is in the repo: {source}"))
                elif cached:
                    out.append(UnauditedFlag(review_path, identifier, index,
                                             "cached publication reports full text"))
    return out


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
    unaudited = find_unaudited_flags(review_paths, availability, repo_root)
    echo(
        f"scanned {len(review_paths)} reviews against {len(availability)} cached publications"
    )
    if unaudited:
        # Reported whether or not there are stale reference-level flags: these are the ones
        # no previous audit could see, so "no stale flags" was never the same as "no false
        # flags". --fix does not touch them; the scope guard below depends on that.
        by_path: dict[Path, list[UnauditedFlag]] = {}
        for unaudited_flag in unaudited:
            by_path.setdefault(unaudited_flag.review_path, []).append(unaudited_flag)
        echo(
            f"{len(unaudited)} flag(s) outside the reference-level PMID audit, in "
            f"{len(by_path)} review(s) - remove by hand, --fix does not touch these:"
        )
        for unaudited_path, unaudited_flags in sorted(by_path.items()):
            for unaudited_flag in unaudited_flags:
                where = (
                    "reference"
                    if unaudited_flag.finding_index is None
                    else f"findings[{unaudited_flag.finding_index}]"
                )
                echo(
                    f"       {unaudited_path}: {unaudited_flag.reference_id} "
                    f"({where}) - {unaudited_flag.reason}"
                )
    if not stale:
        if not unaudited:
            echo("no stale full_text_unavailable flags")
            return 0
        return 1

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
    # Every check runs and reports before anything returns. A first version returned as soon
    # as `unaudited` was non-empty -- which is the normal state, and the reason the detector
    # exists -- so a --fix run that over- or under-removed exited 1 with the right code and
    # *no ERROR line*, short-circuiting the very guard whose comment below explains why
    # silent stripping must never happen.
    failed = False
    if total != len(stale):
        # The mutator and the detector must agree on scope; a mismatch means one of them is
        # looking at flags the other cannot see, which is how a nested Finding-level flag was
        # once stripped without ever being reported.
        echo(
            f"ERROR: detected {len(stale)} flag(s) but removed {total} - scope mismatch"
        )
        failed = True
    if find_stale_flags(sorted(by_review), availability):
        echo("ERROR: stale flags survived the fix")
        failed = True
    if unaudited:
        # --fix does not touch these, so a run that removed everything it could must still
        # fail: reporting flags by hand and then exiting 0 tells CI everything is clean
        # while naming the flags that are not.
        echo(
            f"{len(unaudited)} flag(s) outside --fix's scope remain; remove them by hand"
        )
        failed = True
    if failed:
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
