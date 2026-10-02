"""Verify every quotation used for ARFGEF1 against its cached source.

Covers two surfaces that the repo's own gates leave open:

* **`file:` supporting_text.** CI verifies `supporting_text` verbatim only for
  `PMID:` references; quotes citing `file:human/ARFGEF1/...` are not checked at
  all. This script checks them.
* **Markdown prose.** `ARFGEF1-notes.md` quotes papers in blockquotes with a
  trailing `[PMID:...]` attribution. Nothing in the repo validates those.

It also re-checks the `PMID:` quotes in the review YAML, so one command covers
the whole gene.

Two deliberate design points:

* **The repo root is derived, never asserted.** A shared checker with a
  hardcoded worktree path resolves quotes against the wrong `publications/`
  cache and reports mass false failures on clean work -- worse than crashing.
* **Whitespace is normalised on both sides** before the substring test, because
  cached abstracts are hard-wrapped mid-sentence, but nothing else is: no case
  folding, no punctuation stripping.

Run from the repo root:
    uv run python genes/human/ARFGEF1/ARFGEF1-bioinformatics/arfgef1_quotes.py
    uv run python genes/human/ARFGEF1/ARFGEF1-bioinformatics/arfgef1_quotes.py --self-test
"""

from __future__ import annotations

import os
import re
import sys
from pathlib import Path

import yaml

GENE = "ARFGEF1"


def repo_root() -> Path:
    """Walk up from $AIGR_ROOT or $PWD for a directory holding src/ and publications/."""
    cur = Path(os.environ.get("AIGR_ROOT", Path.cwd())).resolve()
    while not ((cur / "src").is_dir() and (cur / "publications").is_dir()):
        if cur.parent == cur:
            raise SystemExit(
                "could not locate the repo root (a directory containing both src/ "
                "and publications/); run from inside the checkout or set AIGR_ROOT"
            )
        cur = cur.parent
    return cur


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


# Mirrors `literal_bracket_patterns` in conf/reference_validator_config.yaml, so
# this checker agrees with the repo's own validator about which bracketed spans
# are editorial markers and which are literal chemistry ([gamma-thio], [Ca2+]).
_LITERAL_BRACKET = [re.compile(p) for p in (r"[^a-zA-Z\s]", r"^[A-Z]{2,5}$")]


def strip_editorial_brackets(text: str) -> str:
    def sub(m: re.Match[str]) -> str:
        inner = m.group(1)
        if any(p.search(inner) for p in _LITERAL_BRACKET):
            return m.group(0)
        return ""

    return re.sub(r"\[([^\]]*)\]", sub, text)


class Checker:
    def __init__(self, root: Path) -> None:
        self.root = root
        self.problems: list[str] = []
        self.checked = 0
        self._cache: dict[str, str] = {}

    def source_text(self, ref: str) -> str | None:
        """Normalised text of a reference: a cached PMID file or a repo-relative file:."""
        if ref in self._cache:
            return self._cache[ref]
        if ref.startswith("PMID:"):
            p = self.root / "publications" / f"PMID_{ref.split(':', 1)[1]}.md"
        elif ref.startswith("file:"):
            p = self.root / "genes" / ref.split(":", 1)[1]
        else:
            return None
        if not p.exists():
            self.problems.append(f"source file missing for {ref}: {p}")
            return None
        text = norm(p.read_text())
        self._cache[ref] = text
        return text

    def check(self, ref: str, quote: str, where: str) -> None:
        src = self.source_text(ref)
        if src is None:
            return
        self.checked += 1
        q = norm(strip_editorial_brackets(quote))
        if not q:
            self.problems.append(f"{where}: empty quote for {ref}")
            return
        if q not in src:
            self.problems.append(f"{where}: quote not found verbatim in {ref}\n      {q[:220]}")

    # -- surfaces -------------------------------------------------------
    def check_yaml(self, path: Path) -> None:
        doc = yaml.safe_load(path.read_text())

        def walk(node: object, trail: str) -> None:
            if isinstance(node, dict):
                if "reference_id" in node and "supporting_text" in node:
                    self.check(str(node["reference_id"]), str(node["supporting_text"]), trail)
                for k, v in node.items():
                    walk(v, f"{trail}.{k}")
            elif isinstance(node, list):
                for i, v in enumerate(node):
                    walk(v, f"{trail}[{i}]")

        walk(doc, path.name)

    def check_markdown(self, path: Path) -> None:
        """Blockquote blocks whose final `>` line is a bare `[PMID:nnn]` attribution."""
        text = path.read_text()
        n_blocks = 0
        for raw in re.findall(r"(?:^>.*\n)+", text, re.M):
            lines = [re.sub(r"^>\s?", "", ln) for ln in raw.rstrip("\n").split("\n")]
            m = re.fullmatch(r"\s*\[(PMID:\d+|file:[^\]]+)\]\s*", lines[-1])
            if not m:
                continue
            n_blocks += 1
            quote = norm(" ".join(lines[:-1])).strip('"')
            self.check(m.group(1), quote, f"{path.name}:blockquote")
        if not n_blocks:
            self.problems.append(
                f"{path.name}: no attributed blockquotes found -- the extraction "
                "pattern no longer matches the file, so nothing was checked"
            )


def self_test(root: Path) -> int:
    """Break each surface and confirm the checker reports it."""
    ok = True
    c = Checker(root)
    c.check("PMID:15644318", "the GAP activity of myosin IXb was significantly inhibited", "st")
    if c.problems:
        print("self-test 0 FAILED: a known-good quote was rejected", c.problems)
        ok = False
    else:
        print("self-test 0 PASS: a known-good quote is accepted")

    c = Checker(root)
    c.check("PMID:15644318", "the GAP activity of myosin IXb was significantly enhanced", "st")
    if c.problems:
        print("self-test 1 PASS: an altered quote is rejected")
    else:
        print("self-test 1 FAILED: an altered quote was accepted")
        ok = False

    c = Checker(root)
    c.check("PMID:99999999", "anything", "st")
    if c.problems:
        print("self-test 2 PASS: a missing source file is reported")
    else:
        print("self-test 2 FAILED: a missing source file was ignored")
        ok = False

    # A markdown file with no attributed blockquote must report, not pass silently.
    import tempfile
    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / "empty-notes.md"
        p.write_text("# nothing quoted here\n")
        c = Checker(root)
        c.check_markdown(p)
        if c.problems:
            print("self-test 3 PASS: a markdown file yielding zero quotes is reported")
        else:
            print("self-test 3 FAILED: zero extracted quotes read as success")
            ok = False
    return 0 if ok else 1


def main() -> int:
    root = repo_root()
    print(f"repo root: {root}")
    if "--self-test" in sys.argv:
        return self_test(root)

    gene_dir = root / "genes" / "human" / GENE
    c = Checker(root)
    review = gene_dir / f"{GENE}-ai-review.yaml"
    notes = gene_dir / f"{GENE}-notes.md"
    if review.exists():
        c.check_yaml(review)
    else:
        c.problems.append(f"missing {review}")
    if notes.exists():
        c.check_markdown(notes)
    else:
        c.problems.append(f"missing {notes}")

    print(f"quotes checked: {c.checked}")
    if c.problems:
        print(f"PROBLEMS ({len(c.problems)}):")
        for p in c.problems:
            print(f"  - {p}")
        return 1
    print("OK: every quote is a verbatim substring of its cited source "
          "(whitespace-normalised).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
