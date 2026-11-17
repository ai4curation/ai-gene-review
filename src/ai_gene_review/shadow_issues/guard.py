"""Detect text that would notify people on upstream trackers.

GitHub turns some text in commit messages, pull-request titles and bodies, and
issue comments into notifications or cross-reference events on *other*
repositories:

- a full issue or pull-request URL (``https://github.com/org/repo/issues/12``),
- the shorthand ``org/repo#12`` (and ``org/repo@<sha>`` for commits),
- an ``@handle`` mention outside code.

Shadowing an upstream tracker must never do either, so every commit message or
PR text we write is checked with :func:`find_notification_hazards`. Text inside
committed *files* creates no cross-reference, so cached issue threads may keep
their URLs and handles; the danger is only text GitHub renders as a message.

This module uses only the standard library so that it can run as a script from
a git ``commit-msg`` hook or a Claude Code hook without the project environment::

    python3 src/ai_gene_review/shadow_issues/guard.py MESSAGE_FILE [...]

>>> find_notification_hazards("Fixes #12 in this repo")
[]
>>> [h.kind for h in find_notification_hazards("See geneontology/go-annotation#6606")]
['shorthand_reference']
>>> [h.kind for h in find_notification_hazards("https://github.com/geneontology/go-annotation/issues/6606")]
['url_reference']
>>> [h.text for h in find_notification_hazards("thanks @ValWood and @cmungall")]
['@ValWood']
>>> find_notification_hazards("mail noreply@anthropic.com; `@decorator` in code")
[]
>>> find_notification_hazards("Co-authored-by: bot <1+a[bot]@users.noreply.github.com>")
[]
>>> [h.text for h in find_notification_hazards("Thanks @ValWood.")]
['@ValWood']
>>> find_notification_hazards("Shadow work for go-annotation 6606 (issues/go-annotation/6606)")
[]
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path

OWN_REPO = "ai4curation/ai-gene-review"
ALLOWED_HANDLES = frozenset({"cmungall"})

_FENCED_CODE = re.compile(r"```.*?(```|\Z)", re.DOTALL)
_INLINE_CODE = re.compile(r"`[^`\n]*`")
_URL_REF = re.compile(
    r"https?://(?:www\.)?github\.com/([\w.-]+)/([\w.-]+)/(?:issues|pull|discussions|commit)/\w+",
    re.IGNORECASE,
)
_SHORTHAND_REF = re.compile(
    r"(?<![\w/.-])([\w.-]+)/([\w.-]+)(?:#\d+|@[0-9a-f]{7,40}\b)"
)
# An ``@`` that ends an email local part (``x@lbl.gov``, ``1+bot[bot]@users.noreply``)
# is not a mention: GitHub needs a non-word character before it and no domain after it.
_MENTION = re.compile(
    r"(?<![\w`.@/\]+-])@([A-Za-z0-9](?:[A-Za-z0-9-]{0,38}))\b(?!\.\w)"
)


@dataclass(frozen=True)
class Hazard:
    """One piece of text that would notify someone outside this repository."""

    kind: str
    text: str

    def __str__(self) -> str:
        return f"{self.kind}: {self.text}"


def _strip_code(text: str) -> str:
    """Remove fenced and inline code, which GitHub never links.

    >>> _strip_code("a `@x` b\\n```\\n@y\\n```\\nc")
    'a  b\\n\\nc'
    """
    return _INLINE_CODE.sub("", _FENCED_CODE.sub("", text))


def _is_own(owner: str, repo: str) -> bool:
    return f"{owner}/{repo}".lower() == OWN_REPO


def find_notification_hazards(
    text: str, allowed_handles: frozenset[str] = ALLOWED_HANDLES
) -> list[Hazard]:
    """Return every reference or mention in ``text`` that reaches another repository.

    References to this repository and mentions of ``allowed_handles`` are permitted.

    >>> find_notification_hazards("ai4curation/ai-gene-review#5 and @CMungall")
    []
    >>> [h.kind for h in find_notification_hazards("geneontology/go-ontology@0123abcd")]
    ['shorthand_reference']
    """
    prose = _strip_code(text)
    hazards: list[Hazard] = []
    for m in _URL_REF.finditer(prose):
        if not _is_own(m.group(1), m.group(2)):
            hazards.append(Hazard("url_reference", m.group(0)))
    without_urls = _URL_REF.sub("", prose)
    for m in _SHORTHAND_REF.finditer(without_urls):
        if not _is_own(m.group(1), m.group(2)):
            hazards.append(Hazard("shorthand_reference", m.group(0)))
    allowed = {h.lower() for h in allowed_handles}
    for m in _MENTION.finditer(without_urls):
        if m.group(1).lower() not in allowed:
            hazards.append(Hazard("mention", m.group(0)))
    return hazards


def strip_git_comments(text: str) -> str:
    """Drop the ``#`` comment lines git adds to a commit-message template.

    >>> strip_git_comments("Title\\n# Please enter the commit message\\nBody")
    'Title\\nBody'
    """
    return "\n".join(line for line in text.splitlines() if not line.startswith("#"))


def main(argv: list[str]) -> int:
    """Check each named file; exit 1 on any hazard.

    With ``--commit-msg`` the files are git commit messages, whose ``#`` lines are
    template comments; otherwise (PR bodies, where ``#`` starts a heading) every
    line is checked.
    """
    commit_msg = "--commit-msg" in argv
    found = False
    for name in (a for a in argv if a != "--commit-msg"):
        text = Path(name).read_text()
        if commit_msg:
            text = strip_git_comments(text)
        for hazard in find_notification_hazards(text):
            found = True
            print(f"{name}: {hazard}", file=sys.stderr)
    if found:
        print(
            "Upstream references or @mentions would notify curators. Refer to an "
            "upstream issue by its folder (issues/<tracker>/<number>) instead, and "
            "mention no one but @cmungall.",
            file=sys.stderr,
        )
    return 1 if found else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
