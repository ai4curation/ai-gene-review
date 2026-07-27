"""Claim-level lint for the ACTRT2 review: assert corrected claims stay corrected, everywhere.

Six rounds of this review were spent on one failure mode, and the last instance landed in the
top-level `description` - the field a biologist reads first - because it had survived three
separate sweeps. The reviewer's diagnosis is the reason this file exists:

    It survived three sweeps because each grepped for a specific prior string rather than for
    the claim, and the description phrases the same claim in different words.

So a per-string grep is structurally the wrong check. This lint works on **claims**: each entry
pairs a set of retracted *patterns* (regexes, so paraphrases are caught) with an optional required
counter-claim and the number of distinct text **surfaces** that must carry it - surfaces, not
occurrences, which is what `required_min_surfaces` is named for. Every text field of the review YAML
plus the whole notes file and RESULTS.md are scanned, so a claim cannot hide in a field nobody
thought to grep.

Design notes, each from something that actually went wrong here:

* **Scan every field, not a chosen list.** The review is walked recursively and every string value
  is checked, including `description`, which the earlier sweeps never touched.
* **Regex, not literals.** "retains actin's nucleotide-binding pocket essentially intact" and
  "the nucleotide pocket itself is fully retained" are the same claim in different words; a literal
  grep for one misses the other.
* **Require the replacement, not just the absence of the error.** Deleting a wrong sentence and
  writing nothing is also a defect, so load-bearing corrections carry a `required` pattern with a
  minimum count.
* **Fail loudly, and test by breaking.** `--selftest` runs every check in `SELFTEST_CHECKS` and
  prints the registry, so this docstring does not enumerate them and cannot fall behind - which it
  did, four rounds running, each time omitting the check added most recently. The registry is the
  single source of truth: `selftest()` sums it, the success line formats from it, and adding a check
  means adding one tuple.
  Two findings from breaking this file are worth keeping, because they are why the registry exists
  rather than another guard. Injection alone is not sufficient: `audit(extra=...)` appends to
  `surfaces()`, so an injected surface is scanned however badly the real-file scan is broken, and of
  three deliberate sabotages (`surfaces()` returning `[]`, `review_strings()` losing its list
  recursion, inverting the search) injection caught only the third - the coverage assertion catches
  the other two. And a guard that resolved "is this check called?" by substring-searching
  `inspect.getsource(selftest)` was defeated by its own docstring, because `getsource` includes it:
  a check that was merely *documented* counted as *called*, so deleting it from the sum while
  leaving its bullet passed silently. Membership of a registry cannot be faked that way.

Usage:
    uv run python audit_claims.py            # lint; exit 1 on any violation
    uv run python audit_claims.py --selftest # prove each rule fires when the claim is reinstated
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
GENE_DIR = HERE.parent
REVIEW = GENE_DIR / "ACTRT2-ai-review.yaml"
NOTES = GENE_DIR / "ACTRT2-notes.md"
RESULTS = HERE / "RESULTS.md"

# Each rule: what was retracted, what must be present instead, and where it must be present.
# `required_min_surfaces` counts distinct TEXT SURFACES (one review field, the notes file, RESULTS.md)
# that must contain the counter-claim - NOT occurrences, which is what the earlier name implied.
# 0 means the counter-claim is optional.
RULES = [
    {
        "name": "pocket-not-fully-retained",
        "why": "The 10-position set omitted the three ATP contacts where ACTRT2 differs (E214, "
        "Y306, K336) and added three non-contacts (D11, D154, R183), so 'fully/essentially "
        "intact' and 'all ten nucleotide-contacting positions identical' were true but "
        "selectively bounded.",
        "retracted": [
            r"pocket\s+(?:itself\s+)?is\s+fully\s+retained",
            r"pocket\s+is\s+completely\s+retained",
            r"nucleotide-binding\s+pocket\s+essentially\s+intact",
            r"pocket\s+is\s+intact\s+at\s+all\s+ten",
            r"all\s+ten\s+named\s+nucleotide-contacting\s+positions",
            r"identical\s+to\s+actin\s+at\s+all\s+ten\s+nucleotide",
        ],
        "required": r"(?:largely\s+but\s+not\s+wholly|adenine/ribose\s+region|"
        r"phosphate-loop|phosphate-binding-loop|phosphate\s+loops)",
        "required_min_surfaces": 1,
    },
    {
        "name": "his161-carries-the-argument-alone",
        "why": "PMID:37009486 reports the A108G and P109A actin mutants polymerise and hydrolyse "
        "like wild type, so grouping Ala108 and Pro109 with His161 as residues that couple "
        "filament incorporation to hydrolysis overstates two of the three.",
        "retracted": [
            r"residues\s+that\s+couple\s+filament\s+incorporation\s+to\s+ATP\s+hydrolysis",
            r"lost\s+\*\*all\s+three\*\*\s+components\s+of\s+that\s+switch",
            r"\(Ala108,\s*Pro109,\s*His161\)\s+are\s+all\s+lost",
            r"hydrolysis\s+switch\s+is\s+not\s+intact",
        ],
        "required": r"(?:His161\s+carries\s+the\s+argument|context\s+rather\s+than\s+evidence|"
        r"governs\s+(?:its\s+rotamer|the\s+His161\s+rotamer)|ATP-hydrolysis\s+trigger)",
        "required_min_surfaces": 1,
    },
    {
        "name": "go5200-not-accepted",
        "why": "GO:0005200 was reversed from ACCEPT to MODIFY after the merged ACTRT3 review; the "
        "reason must not still argue in the present tense that the replaced term is earned.",
        "retracted": [
            r"The\s+term\s+is\s+nonetheless\s+earned\s+on\s+ACTRT2's\s+own",
            r"GO:0005200\s+is\s+kept\s+over\s+it\s+because",
            r"core\s+molecular\s+function,\s+but\s+the\s+route\s+by\s+which",
        ],
        "required": r"(?:no\s+ortholog-strength\s+donor|ACTR10\s+precedent\s+does\s+not\s+transfer)",
        "required_min_surfaces": 1,
    },
    {
        "name": "partner-arithmetic",
        "why": "IntAct returns 10 records over 9 distinct partners for ACTRT2, so it is EIGHT "
        "besides PDCL3; and 8 of the 9 spoke rows are at MI 0.35, the PDCL3 spoke row at 0.50.",
        "retracted": [
            r"nine\s+partners\s+besides\s+PDCL3",
            r"the\s+other\s+nine\s+(?:are|include)\s+TCP1",
            r"nine\s+spoke\s+partners",
            r"spoke-expanded\s+at\s+MI-score\s+0\.35\s+with\s+the\s+PDCL3\s+pair",
        ],
        "required": r"eight\s+(?:partners\s+)?besides\s+PDCL3",
        "required_min_surfaces": 1,
    },
    {
        "name": "annotation-count-is-not-an-entity-count",
        "why": "QuickGO's total counts annotations, not entities, and the BioPlex walk is capped, "
        "so the entity count there was never measured. 'thousands' was an inference in a "
        "measurement's place.",
        "retracted": [
            r"9,?514\s*\|\s*thousands",
            r"\|\s*thousands\s*\|",
        ],
        "required": r"(?:not\s+counted|annotation\s+count\s+is\s+not\s+an\s+entity\s+count|"
        r"GOA\s+\*\*annotations\*\*)",
        "required_min_surfaces": 1,
    },
]


def review_strings() -> list[tuple[str, str]]:
    """(field path, text) for every string in the review - including `description`."""
    doc = yaml.safe_load(REVIEW.read_text())
    out: list[tuple[str, str]] = []

    def walk(o, path="review"):
        if isinstance(o, str):
            out.append((path, o))
        elif isinstance(o, dict):
            for k, v in o.items():
                walk(v, f"{path}.{k}")
        elif isinstance(o, list):
            for i, v in enumerate(o):
                walk(v, f"{path}[{i}]")

    walk(doc)
    return out


def surfaces() -> list[tuple[str, str]]:
    """The text a curator or reader actually sees. This file is deliberately NOT among them.

    `RULES` necessarily contains every retracted phrasing as a regex literal, so scanning this file
    would make the lint report itself. The exclusion is therefore load-bearing rather than
    incidental, and is asserted below so that adding this file to the scan fails loudly instead of
    producing a confusing self-report.
    """
    surf = review_strings()
    surf.append(("notes", NOTES.read_text()))
    if RESULTS.exists():
        surf.append(("RESULTS.md", RESULTS.read_text()))
    assert not any(name == "audit_claims.py" for name, _ in surf), (
        "this lint's own source contains every retracted phrasing as a regex literal and must not "
        "be scanned; exclude it or the report becomes self-referential"
    )
    return surf


def audit(extra: list[tuple[str, str]] | None = None) -> list[str]:
    surf = surfaces() + (extra or [])
    problems: list[str] = []
    for rule in RULES:
        for pattern in rule["retracted"]:
            rx = re.compile(pattern, re.I | re.S)
            for where, text in surf:
                # Collapse whitespace so a claim wrapped across YAML lines is still matched -
                # the wrapping is exactly why literal greps missed the description.
                if rx.search(" ".join(text.split())):
                    problems.append(
                        f"[{rule['name']}] RETRACTED CLAIM present at {where}: /{pattern}/"
                    )
        if rule["required_min_surfaces"]:
            rx = re.compile(rule["required"], re.I | re.S)
            hits = sum(1 for _, text in surf if rx.search(" ".join(text.split())))
            if hits < rule["required_min_surfaces"]:
                problems.append(
                    f"[{rule['name']}] REPLACEMENT CLAIM missing: /{rule['required']}/ "
                    f"found in {hits} surfaces, need {rule['required_min_surfaces']}"
                )
    return problems


def _probe_for(pattern: str) -> str:
    """Build a literal string that `pattern` matches, so every rule can be tested by breaking it.

    Group handling is the fiddly part and it went wrong once: an optional group like
    `(?:itself\\s+)?` must VANISH, and an alternation like `(?:are|include)` must collapse to its
    first branch INCLUDING the `(?:` prefix - an earlier version stripped only the paren and left a
    stray colon, producing "the other nine :are TCP1", which matched nothing and would have left the
    rule silently untested.
    """
    # Escaped parens are LITERAL characters, not groups. Park them first, or a pattern like
    # `\(Ala108, Pro109, His161\)` gets eaten by the group logic below - which is what happened.
    LP, RP = "\x00LP\x00", "\x00RP\x00"
    probe = pattern.replace(r"\(", LP).replace(r"\)", RP)
    probe = re.sub(r"\((?:\?:)?[^()]*\)\?", "", probe)          # optional groups vanish
    def first_branch(m: re.Match[str]) -> str:
        inner = m.group(0)[1:-1]
        if inner.startswith("?:"):
            inner = inner[2:]
        return inner.split("|")[0]
    while re.search(r"\((?:\?:)?[^()]*\)", probe):               # alternations collapse
        probe = re.sub(r"\((?:\?:)?[^()]*\)", first_branch, probe, count=1)
    for a, b in ((r"\s+", " "), (r"\s*", " "),
                 (r"\|", "|"), (r"\.", "."), (r"\*", "*"), (",?", ",")):
        probe = probe.replace(a, b)
    probe = probe.replace("?", "").replace(LP, "(").replace(RP, ")")
    return " ".join(probe.split())


def selftest() -> int:
    """Run every check in `SELFTEST_CHECKS` and fail if any reports a problem.

    Deliberately enumerates nothing. Four consecutive review rounds found a hand-maintained list
    naming N-1 of N checks, each time omitting the one added most recently, because there were three
    such lists (this docstring, the module docstring, the success print) plus a hand-written `total`
    - all free to drift independently. Patching a count buys one round. `SELFTEST_CHECKS` is now the
    single source of truth: this function sums it, the success line formats from it, and the
    docstrings describe it rather than transcribe it, so the class of defect has nowhere left to
    live.
    """
    total = sum(fn() for fn, _ in SELFTEST_CHECKS)
    if total:
        print(f"selftest FAILED: {total} problem(s)")
        return 1
    n_patterns = sum(len(r["retracted"]) for r in RULES)
    print(f"selftest passed: {len(SELFTEST_CHECKS)} checks over {len(RULES)} rules "
          f"({n_patterns} retracted phrasings, {len(surfaces())} text surfaces)")
    for fn, description in SELFTEST_CHECKS:
        print(f"  {fn.__name__}: {description}")
    return 0


def _selftest_every_helper_is_registered() -> int:
    """Every `_selftest_*` helper defined here must be in `SELFTEST_CHECKS`.

    This is the one reachability question the registry does not answer by construction: a helper can
    be written and never wired in. It is a set comparison against the registry rather than a source
    scan, which also removes the bug that made this check's predecessor useless - it resolved calls
    by substring-searching `inspect.getsource(selftest)`, and `getsource` includes the docstring, so
    a helper that was merely *documented* counted as *called*. Deleting a helper from the sum while
    leaving its bullet therefore passed, and the coverage assertion silently stopped running.

    The prose checks that used to live here - that a docstring not say "occurrence count", that it
    mention the coverage assertion, that its enumeration match the code - are deleted rather than
    fixed. The registry removed what they policed, and an audit harness that needs its own audit
    harness is past the point of proportion on a gene whose curation settled several rounds ago.
    """
    # Residual gap, stated rather than closed: this check is itself a registry entry, so it protects
    # every other check but not its own removal. Deleting its tuple removes the only thing that would
    # have noticed. That is not worth a further guard - a guard guarding the guard is where this file
    # would stop being proportionate to a settled curation - so it is recorded here instead.
    defined = {
        name for name, obj in globals().items()
        if name.startswith("_selftest_") and callable(obj)
    }
    registered = {fn.__name__ for fn, _ in SELFTEST_CHECKS}
    failures = 0
    for orphan in sorted(defined - registered):
        print(f"  REGISTRY FAIL: {orphan}() is defined but not in SELFTEST_CHECKS, so it never "
              "runs; a check that is not run is documentation")
        failures += 1
    for ghost in sorted(registered - defined):
        print(f"  REGISTRY FAIL: SELFTEST_CHECKS names {ghost} which is not defined here")
        failures += 1
    return failures


def _selftest_probe_builder() -> int:
    """Can a literal be built that each pattern matches? A test of `_probe_for`, nothing more."""
    failures = 0
    for rule in RULES:
        for pattern in rule["retracted"]:
            probe = _probe_for(pattern)
            if not re.search(pattern, probe, re.I | re.S):
                print(f"  PROBE FAIL: cannot build a probe matching /{pattern}/ (got {probe!r}); "
                      "the rule would go untested")
                failures += 1
    return failures


def _selftest_lint_fires() -> int:
    """Inject each probe as a surface and require audit() to report that rule's pattern."""
    failures = 0
    for rule in RULES:
        for pattern in rule["retracted"]:
            probe = _probe_for(pattern)
            reported = audit(extra=[("SELFTEST-SURFACE", probe)])
            expected = f"[{rule['name']}] RETRACTED CLAIM present at SELFTEST-SURFACE: /{pattern}/"
            if expected not in reported:
                print(f"  LINT FAIL: audit() did not report /{pattern}/ for rule "
                      f"{rule['name']} when injected as a surface")
                failures += 1
    return failures


def _selftest_scan_coverage() -> int:
    """Assert the scan actually reaches the places a claim has hidden. This is the check that
    catches a sabotaged `surfaces()`.

    Added after break-testing the three sabotages the reviewer named. Injection tests
    (`_selftest_lint_fires`) pass even when the real-file scan is gutted, because the injected
    surface is scanned regardless - so `surfaces()` returning `[]` and `review_strings()` losing its
    list recursion were BOTH missed. Only a positive coverage assertion catches them, and each item
    below corresponds to a place a retracted claim has actually been found in this review:

      * `review.description`      - where the last instance hid, and not reachable without dict walk
      * a list-nested review path - where every annotation `reason` lives, and not reachable without
                                    list recursion
      * `notes`                   - where the lint found three instances manual sweeps had missed
      * `RESULTS.md`              - where the §8 rewrite stranded two quotes
    """
    failures = 0
    surf = surfaces()
    names = [name for name, _ in surf]
    for required in ("review.description", "notes", "RESULTS.md"):
        if required not in names:
            print(f"  COVERAGE FAIL: {required!r} is not among the scanned surfaces; a claim there "
                  "would be invisible")
            failures += 1
    if not any("[" in name for name in names):
        print("  COVERAGE FAIL: no list-nested field is scanned, so every annotation reason, "
              "knowledge_gap and reference finding is invisible")
        failures += 1
    if len(surf) < 100:
        print(f"  COVERAGE FAIL: only {len(surf)} surfaces scanned; this review has hundreds of "
              "text fields, so the walk is not reaching them")
        failures += 1
    if not any(len(text) > 500 for _, text in surf):
        print("  COVERAGE FAIL: no substantial text scanned; surfaces are present but empty")
        failures += 1
    return failures


def _selftest_detects_a_broken_lint() -> int:
    """Sabotage the scan and require audit() to stop passing.

    `_selftest_lint_fires` only proves the INJECTED surface is scanned. A `surfaces()` that returned
    nothing would still pass it, so the real-file scan is checked separately here: with `surfaces()`
    emptied, `audit()` must report the missing counter-claims rather than reporting clean.
    """
    global surfaces
    original = surfaces
    failures = 0
    try:
        surfaces = lambda: []  # noqa: E731 - deliberate sabotage
        empty = audit()
        if not any("REPLACEMENT CLAIM missing" in p for p in empty):
            print("  META FAIL: audit() reports clean with nothing to scan, so a broken "
                  "surfaces() would pass unnoticed")
            failures += 1
    finally:
        surfaces = original
    return failures


# The single source of truth for what `--selftest` runs. The callable IS the entry - its own
# `__name__` supplies the key - so a registry entry cannot name a function that does not exist, nor
# drift from the function it points at. `selftest()` sums this, the success line formats from it,
# and the docstrings describe it rather than transcribe it, so a new check is added in exactly one
# place and no enumeration can fall behind.
SELFTEST_CHECKS = (
    (_selftest_probe_builder,
     "a literal probe can be built that each retracted pattern matches"),
    (_selftest_lint_fires,
     "injected as a surface, audit() reports each retracted pattern"),
    (_selftest_scan_coverage,
     "the walk reaches review.description, a list-nested path, notes and RESULTS.md"),
    (_selftest_detects_a_broken_lint,
     "audit() stops passing when its scan is sabotaged"),
    (_selftest_every_helper_is_registered,
     "no _selftest_* helper exists outside this registry"),
)


def main() -> int:
    if "--selftest" in sys.argv:
        return selftest()
    problems = audit()
    if problems:
        print("CLAIM AUDIT FAILED:")
        for p in problems:
            print("  -", p)
        return 1
    print(f"claim audit clean: {len(RULES)} rules over {len(surfaces())} text surfaces")
    for rule in RULES:
        print(f"  ok  {rule['name']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
