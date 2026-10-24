"""Turn validation-all warnings into low-effort cleanup issues.

The weekly full validation writes ``reports/validation-all.tsv``. This module
selects the warnings whose fix is mechanical (a split hyphen, a baselined local
quote that no longer matches its regenerated source), groups them per review file, and renders one GitHub issue per file. The curation
scanner's ``low_effort`` tier then picks those issues up.

Warnings that need curatorial judgement are deliberately not in
:data:`LOW_EFFORT_CHECKS`: action consistency, missing core functions, deep
research, and the ``uniprot_quote_*`` checks, whose fix is to find different
evidence or change the action (deleting the quote would also silence them,
leaving an ACCEPT with no evidence). So is the sanctioned-legacy protein-binding
policy.
"""

import csv
from dataclasses import dataclass, field
from pathlib import Path

TITLE_PREFIX = "[validation-cleanup]"

# check_type -> how to fix it, rendered into the issue body.
CHECK_GUIDANCE = {
    "folded_scalar_hyphen": (
        "Rewrap the folded scalar so no line ends in a hyphen; change no words."
    ),
    "local_source_supporting_text": (
        "The quote is listed in `conf/local_quote_baseline.yaml` because its source "
        "no longer contains it. Edit only the review YAML, never the cited source "
        "file: re-quote verbatim text from the current source that makes the same "
        "point (do not trim the quote until it matches); if the source no longer "
        "supports anything equivalent, leave the warning. If the warning says the "
        "reference does not resolve, run the suggested cache command for a "
        "`Reactome:` id, and leave a `file:` id alone (re-pointing it is a "
        "judgement). Then run `just local-quote-baseline --prune`, which drops "
        "every entry that now passes across the corpus, so unrelated removals in "
        "the diff are expected. Never add entries or run "
        "`just local-quote-baseline --write`."
    ),
}

LOW_EFFORT_CHECKS = frozenset(CHECK_GUIDANCE)


@dataclass
class CleanupWarning:
    check_type: str
    path: str
    message: str
    suggestion: str


@dataclass
class CleanupIssue:
    review_file: str
    warnings: list[CleanupWarning] = field(default_factory=list)

    @property
    def gene_dir(self) -> str:
        """The gene folder, e.g. ``genes/human/ABCA1``.

        >>> CleanupIssue("genes/human/ABCA1/ABCA1-ai-review.yaml").gene_dir
        'genes/human/ABCA1'
        """
        return str(Path(self.review_file).parent)

    @property
    def title(self) -> str:
        """Issue title; also the dedup key against open issues.

        >>> CleanupIssue("genes/human/ABCA1/ABCA1-ai-review.yaml").title
        '[validation-cleanup] genes/human/ABCA1'
        """
        return f"{TITLE_PREFIX} {self.gene_dir}"

    @property
    def body(self) -> str:
        organism, gene = Path(self.gene_dir).parts[-2:]
        lines = [
            f"Validation warnings with mechanical fixes in `{self.review_file}`,",
            "from the weekly full validation (`reports/validation-all.tsv`).",
            "",
            "## Warnings",
            "",
        ]
        for w in self.warnings:
            lines.append(f"- **{w.check_type}** at `{w.path or '(file)'}`: {w.message}")
            if w.suggestion:
                lines.append(f"  - suggestion: {w.suggestion}")
        lines += ["", "## How to fix", ""]
        for check_type in sorted({w.check_type for w in self.warnings}):
            lines.append(f"- **{check_type}**: {CHECK_GUIDANCE[check_type]}")
        lines += [
            "",
            "## Handoff Objective",
            "",
            f"Fix the warnings above in `{self.review_file}` without changing any",
            "curation decision, then confirm they are gone with",
            f"`just validate {organism} {gene}`. Do not delete a `supporting_text`",
            "or `supported_by` entry, or change an action, to silence a warning. If",
            "a fix would need a curation judgement (a different action, term or",
            "reference), leave that warning and say so in the PR.",
        ]
        return "\n".join(lines) + "\n"


def _repo_relative(file_path: str) -> str | None:
    """Strip the checkout prefix the validator writes; None if not a gene review.

    >>> _repo_relative("/home/runner/work/x/x/genes/human/A/A-ai-review.yaml")
    'genes/human/A/A-ai-review.yaml'
    >>> _repo_relative("genes/human/A/A-ai-review.yaml")
    'genes/human/A/A-ai-review.yaml'
    >>> _repo_relative("/work/mygenes/human/A/A-ai-review.yaml") is None
    True
    """
    if file_path.startswith("genes/"):
        return file_path
    idx = file_path.rfind("/genes/")
    return file_path[idx + 1 :] if idx >= 0 else None


def collect_issues(tsv_path: Path) -> list[CleanupIssue]:
    """Group low-effort warnings by review file, sorted by path."""
    by_file: dict[str, CleanupIssue] = {}
    with tsv_path.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f, delimiter="\t"):
            if row["severity"] != "warning" or row["check_type"] not in LOW_EFFORT_CHECKS:
                continue
            review_file = _repo_relative(row["file_path"])
            if review_file is None:
                continue
            issue = by_file.setdefault(review_file, CleanupIssue(review_file))
            issue.warnings.append(
                CleanupWarning(row["check_type"], row["path"], row["message"], row["suggestion"])
            )
    return [by_file[k] for k in sorted(by_file)]


def select_issues(
    issues: list[CleanupIssue],
    open_titles: set[str],
    closed_titles: set[str],
    max_new: int,
    max_open: int,
    max_warnings: int,
) -> list[CleanupIssue]:
    """Pick the issues to file this run.

    Skips files that have an open cleanup issue, or one closed recently
    (``closed_titles``: closed with warnings left means the rest needs a human,
    and re-filing it every week would starve the budget), and files with more
    than ``max_warnings`` warnings (no longer a small edit). Keeps the open
    backlog at or below ``max_open`` and prefers the smallest fixes.

    >>> a = CleanupIssue("genes/human/A/A-ai-review.yaml", [CleanupWarning("x", "", "", "")] * 3)
    >>> b = CleanupIssue("genes/human/B/B-ai-review.yaml", [CleanupWarning("x", "", "", "")])
    >>> c = CleanupIssue("genes/human/C/C-ai-review.yaml", [CleanupWarning("x", "", "", "")] * 20)
    >>> [i.gene_dir for i in select_issues([a, b, c], set(), set(), 5, 10, 10)]
    ['genes/human/B', 'genes/human/A']
    >>> [i.gene_dir for i in select_issues([a, b], {b.title}, set(), 5, 10, 10)]
    ['genes/human/A']
    >>> [i.gene_dir for i in select_issues([a, b], set(), {b.title}, 5, 10, 10)]
    ['genes/human/A']
    >>> select_issues([a, b], {"t1", "t2"}, set(), 5, 2, 10)
    []
    """
    budget = min(max_new, max_open - len(open_titles))
    if budget <= 0:
        return []
    candidates = [
        i
        for i in issues
        if i.title not in open_titles | closed_titles and len(i.warnings) <= max_warnings
    ]
    candidates.sort(key=lambda i: (len(i.warnings), i.review_file))
    return candidates[:budget]
