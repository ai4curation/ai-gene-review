#!/usr/bin/env python3
"""Verify every ``supporting_text`` in ``AEBP2-ai-review.yaml`` against its source.

This exists because the repo's own gates have documented blind spots:

* the reference validator checks ``supporting_text`` verbatim **only for ``PMID:``
  references** — every ``file:`` quote is skipped entirely, which makes it the one
  place in the document where an invented quotation survives CI;
* ``checkquotes.py`` does not walk ``provenance`` or ``knowledge_gaps[].provenance``;
* a **duplicate YAML mapping key** is silently dropped on parse, so a quote that
  parsing removed cannot fail a check that inspects only what parsing produced;
* a **YAML anchor/alias** does the opposite — one object referenced N times is
  verified N times and reports N successes.

So this checker: loads with a strict loader that raises on duplicate keys, refuses
anchors, reconciles the raw occurrence count against the parsed walk, and then
verifies every quote — ``PMID:`` and ``file:`` alike — as an exact substring of the
target file. **It fails if it verifies zero quotes**, which closes the vacuity hole.

    uv run --no-project python check_review_quotes.py
    uv run --no-project python check_review_quotes.py --self-test
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
GENE_DIR = HERE.parent
REVIEW = GENE_DIR / "AEBP2-ai-review.yaml"
# genes/<org>/<gene>/ -> repo root is three levels up
REPO_ROOT = GENE_DIR.parent.parent.parent
PUBLICATIONS = REPO_ROOT / "publications"

QUOTE_KEY = "supporting_text"
# every slot in the schema that can hold a SupportingTextInReference list
QUOTE_CONTAINERS = ("supported_by", "provenance", "findings")


class StrictLoader(yaml.SafeLoader):
    """SafeLoader that raises on a duplicate mapping key instead of keeping the last."""


def _construct_mapping(loader, node, deep=False):  # noqa: ANN001
    seen: set = set()
    mapping = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in seen:
            raise ValueError(
                f"DUPLICATE YAML KEY {key!r} at line {key_node.start_mark.line + 1}: "
                "PyYAML keeps only the last occurrence, so data has been silently dropped"
            )
        seen.add(key)
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


StrictLoader.construct_mapping = _construct_mapping  # type: ignore[assignment]


def resolve_source(reference_id: str) -> Path | None:
    """Map a reference id onto the file its quotes must appear in."""
    if reference_id.startswith("PMID:"):
        return PUBLICATIONS / f"PMID_{reference_id.split(':', 1)[1]}.md"
    if reference_id.startswith("file:"):
        # file:<org>/<gene>/<path> is relative to genes/
        return REPO_ROOT / "genes" / reference_id.split(":", 1)[1]
    return None  # GO_REF:, Reactome: etc. have no local text to check


def collect_quotes(node, path: str = "") -> list[tuple[str, str, str]]:
    """Walk the parsed document and yield (yaml_path, reference_id, quote)."""
    out: list[tuple[str, str, str]] = []
    if isinstance(node, dict):
        if QUOTE_KEY in node and node.get(QUOTE_KEY):
            ref = node.get("reference_id")
            if not ref:
                out.append((path, "<MISSING reference_id>", node[QUOTE_KEY]))
            else:
                out.append((path, ref, node[QUOTE_KEY]))
        for key, value in node.items():
            out += collect_quotes(value, f"{path}.{key}" if path else str(key))
    elif isinstance(node, list):
        for i, value in enumerate(node):
            out += collect_quotes(value, f"{path}[{i}]")
    return out


def check(review_path: Path = REVIEW) -> list[str]:
    problems: list[str] = []
    raw = review_path.read_text()

    if re.search(r"&id\d+", raw):
        problems.append(
            "YAML anchors present: one object referenced N times is verified N times "
            "and reports N successes. Dump with ignore_aliases=True."
        )

    try:
        doc = yaml.load(raw, Loader=StrictLoader)
    except ValueError as exc:
        problems.append(str(exc))
        return problems

    quotes = collect_quotes(doc)

    # Reconcile raw text against the parsed walk. Anchor the regex: an unanchored
    # `"supporting_text" in line` also matches `supporting_text_fulltext`.
    raw_count = len(re.findall(rf"^\s*(?:-\s*)?{QUOTE_KEY}:", raw, re.M))
    if raw_count != len(quotes):
        problems.append(
            f"raw {QUOTE_KEY} occurrences ({raw_count}) != parsed ({len(quotes)}); "
            "do not rationalise the gap, inspect the data"
        )

    # VACUITY GUARD: a checker that finds nothing to check must fail, not pass.
    if not quotes:
        problems.append("zero quotes collected — this checker is vacuous, fix the walk")
        return problems

    # Coverage: the containers this document actually uses must all be reached, so a
    # future slot that the walk cannot see shows up as a missing container.
    reached = {c for c in QUOTE_CONTAINERS if any(c in p for p, _, _ in quotes)}
    declared = {c for c in QUOTE_CONTAINERS if re.search(rf"^\s*{c}:", raw, re.M)}
    unreached = {c for c in declared if c not in reached and re.search(
        rf"^\s*{c}:\s*$", raw, re.M)}
    if unreached:
        problems.append(
            f"quote-bearing containers present in the file but not reached by the walk: "
            f"{sorted(unreached)}"
        )

    checked_pmid = checked_file = skipped = 0
    for yaml_path, ref, quote in quotes:
        source = resolve_source(ref)
        if source is None:
            skipped += 1
            continue
        if not source.exists():
            problems.append(f"{yaml_path}: source file missing for {ref}: {source}")
            continue
        if quote not in source.read_text():
            problems.append(
                f"{yaml_path}: NOT VERBATIM in {ref}: {quote[:110]!r}"
            )
            continue
        if ref.startswith("PMID:"):
            checked_pmid += 1
        else:
            checked_file += 1

    # `file:` quotes are the fabrication surface CI cannot see. If this document
    # contains any and none were verified, the check has not done its job.
    if re.search(r"reference_id:\s*file:", raw) and checked_file == 0:
        problems.append(
            "the document contains file: quotes but zero were verified — the file: "
            "resolver is broken and CI will not catch it"
        )

    print(
        f"checked {checked_pmid} PMID quotes and {checked_file} file: quotes; "
        f"{skipped} non-textual references skipped; {len(problems)} problem(s)"
    )
    return problems


def self_test() -> int:
    """Break-test each direction and assert the failure MESSAGE, not just failure."""
    import tempfile

    failures: list[str] = []
    raw = REVIEW.read_text()

    def run_on(text: str) -> list[str]:
        with tempfile.NamedTemporaryFile("w", suffix=".yaml", delete=False) as fh:
            fh.write(text)
            tmp = Path(fh.name)
        try:
            return check(tmp)
        finally:
            tmp.unlink()

    def expect(label: str, text: str, needle: str) -> None:
        problems = run_on(text)
        blob = " || ".join(problems)
        if not problems:
            failures.append(f"{label}: guard did not fire")
        elif needle not in blob:
            failures.append(f"{label}: fired but message lacks {needle!r}: {blob!r}")

    # 0. happy path: the real file must be clean. The happy path is the untested path.
    real = check(REVIEW)
    if real:
        failures.append(f"real file is not clean: {real}")

    # 1. a corrupted PMID quote must be caught. Assert the anchor exists first, so a
    #    drifted target string cannot make the mutation a silent no-op.
    anchor = "supporting_text: PRC2 plus AEBP2 and JARID2"
    if anchor not in raw:
        failures.append(f"mutation anchor absent, break-test would be a no-op: {anchor!r}")
    else:
        expect("corrupted PMID quote",
               raw.replace(anchor, "supporting_text: PRC2 plus AEBP2 and JARID3", 1),
               "NOT VERBATIM in PMID:33514705")

    # 2. a corrupted file: quote must be caught — this is the class CI skips entirely,
    #    and the mutation is a single character so it also proves the check is exact
    #    rather than fuzzy.
    fanchor = "supporting_text: Important for nucleosome binding activity of the"
    if fanchor not in raw:
        failures.append(f"file: mutation anchor absent: {fanchor!r}")
    else:
        expect("corrupted file: quote",
               raw.replace(fanchor,
                           "supporting_text: Important for nucleosome binding activity in the", 1),
               "NOT VERBATIM in file:human/AEBP2/AEBP2-uniprot.txt")

    # 3. a duplicate mapping key must raise rather than silently drop data.
    expect("duplicate mapping key",
           raw.replace("gene_symbol: AEBP2", "gene_symbol: AEBP2\ngene_symbol: AEBP2", 1),
           "DUPLICATE YAML KEY")

    # 4. a YAML anchor must be reported.
    expect("yaml anchor",
           raw.replace("existing_annotations:", "existing_annotations: &id001", 1),
           "YAML anchors present")

    # 5. vacuity: a document with no quotes at all must FAIL, not pass silently.
    expect("vacuous document", "id: Q6ZN18\ngene_symbol: AEBP2\n", "vacuous")

    # 6. raw/parsed reconciliation must notice an injected duplicate-key drop. Adding a
    #    second supporting_text inside one mapping makes raw=N+1 while the strict
    #    loader raises first, so assert the loader wins — that ordering is the point.
    expect("duplicate supporting_text key inside one mapping",
           raw.replace(anchor, anchor + "\n      supporting_text: something else", 1),
           "DUPLICATE YAML KEY")

    for f in failures:
        print(f"SELF-TEST FAILURE: {f}", file=sys.stderr)
    print(f"self-test: {len(failures)} failure(s)")
    return 1 if failures else 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    if args.self_test:
        return self_test()
    problems = check()
    for p in problems:
        print("PROBLEM:", p)
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
