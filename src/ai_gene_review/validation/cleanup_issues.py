"""Turn validation-all warnings into low-effort cleanup issues.

The weekly full validation writes ``reports/validation-all.tsv``. This module
selects the warnings whose fix is mechanical (a split hyphen, a UniProt quote
that restates a label, a local quote that no longer matches its source), groups
them per review file, and renders one GitHub issue per file. The curation
scanner's ``low_effort`` tier then picks those issues up.

Warnings that need curatorial judgement (action consistency, missing core
functions, deep research) and sanctioned legacy warnings (the protein-binding
policy) are deliberately not in :data:`LOW_EFFORT_CHECKS`.
"""

import csv
from dataclasses import dataclass, field
from pathlib import Path

TITLE_PREFIX = "[validation-cleanup]"

LOW_EFFORT_CHECKS = frozenset(
    {
        "folded_scalar_hyphen",
        "local_source_supporting_text",
        "uniprot_quote_existence_as_support",
        "uniprot_quote_restating_field",
        "uniprot_quote_unvetted_prediction",
    }
)


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
        lines += [
            "",
            "## Handoff Objective",
            "",
            f"Fix the warnings above in `{self.review_file}` without changing any",
            "curation decision, then confirm they are gone with",
            f"`just validate {organism} {gene}`. If a fix would need a curation",
            "judgement (a different action, term or reference), leave that warning",
            "and say so in the PR.",
        ]
        return "\n".join(lines) + "\n"


def _repo_relative(file_path: str) -> str:
    """Strip the checkout prefix the validator writes.

    >>> _repo_relative("/home/runner/work/x/x/genes/human/A/A-ai-review.yaml")
    'genes/human/A/A-ai-review.yaml'
    >>> _repo_relative("genes/human/A/A-ai-review.yaml")
    'genes/human/A/A-ai-review.yaml'
    """
    idx = file_path.find("genes/")
    return file_path[idx:] if idx >= 0 else file_path


def collect_issues(tsv_path: Path) -> list[CleanupIssue]:
    """Group low-effort warnings by review file, sorted by path."""
    by_file: dict[str, CleanupIssue] = {}
    with tsv_path.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f, delimiter="\t"):
            if row["severity"] != "warning" or row["check_type"] not in LOW_EFFORT_CHECKS:
                continue
            review_file = _repo_relative(row["file_path"])
            issue = by_file.setdefault(review_file, CleanupIssue(review_file))
            issue.warnings.append(
                CleanupWarning(row["check_type"], row["path"], row["message"], row["suggestion"])
            )
    return [by_file[k] for k in sorted(by_file)]


def select_issues(
    issues: list[CleanupIssue],
    open_titles: set[str],
    max_new: int,
    max_open: int,
    max_warnings: int,
) -> list[CleanupIssue]:
    """Pick the issues to file this run.

    Skips files that already have an open cleanup issue and files with more than
    ``max_warnings`` warnings (no longer a small edit), keeps the open backlog at
    or below ``max_open``, and prefers the smallest fixes.

    >>> a = CleanupIssue("genes/human/A/A-ai-review.yaml", [CleanupWarning("x", "", "", "")] * 3)
    >>> b = CleanupIssue("genes/human/B/B-ai-review.yaml", [CleanupWarning("x", "", "", "")])
    >>> c = CleanupIssue("genes/human/C/C-ai-review.yaml", [CleanupWarning("x", "", "", "")] * 20)
    >>> [i.gene_dir for i in select_issues([a, b, c], set(), 5, 10, 10)]
    ['genes/human/B', 'genes/human/A']
    >>> [i.gene_dir for i in select_issues([a, b], {b.title}, 5, 10, 10)]
    ['genes/human/A']
    >>> select_issues([a, b], {"t1", "t2"}, 5, 2, 10)
    []
    """
    budget = min(max_new, max_open - len(open_titles))
    if budget <= 0:
        return []
    candidates = [
        i
        for i in issues
        if i.title not in open_titles and len(i.warnings) <= max_warnings
    ]
    candidates.sort(key=lambda i: (len(i.warnings), i.review_file))
    return candidates[:budget]
