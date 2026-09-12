"""Guard: the numbers written into RESULTS.md, the notes and the review YAML must
be the numbers the scripts actually produce.

A report that drifts from its generator is the campaign's most repeated defect.
This re-runs the analyses (from the on-disk HTTP cache, so it is fast and
offline) and asserts each load-bearing figure appears where it is claimed.

It also checks the inverse direction: phrasings that were retracted during the
review must NOT appear anywhere, so a corrected claim cannot silently come back.

Run: uv run python audit_claims.py [--self-test]
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).parent
GENE = HERE.parent
RESULTS = HERE / "RESULTS.md"
NOTES = GENE / "AGGF1-notes.md"
REVIEW = GENE / "AGGF1-ai-review.yaml"
DOMAIN_JSON = HERE / "domain_residues.json"


def _require(problems: list[str], text: str, needle: str, where: str, why: str) -> None:
    """Append a problem instead of raising: a check that kills the harness is
    worse than no check, because the harness still prints as though it ran."""
    if needle not in text:
        problems.append(f"{where}: missing {why} -- expected substring {needle!r}")


def _count(problems: list[str], text: str, needle: str, n: int, where: str) -> None:
    got = text.count(needle)
    if got != n:
        problems.append(f"{where}: {needle!r} appears {got}x, expected {n}x")


def check(paths: dict[str, str]) -> list[str]:
    problems: list[str] = []
    results, notes, review = paths["results"], paths["notes"], paths["review"]

    if not DOMAIN_JSON.exists():
        problems.append("domain_residues.json missing -- run `uv run python domain_residues.py`")
        return problems
    d = json.loads(DOMAIN_JSON.read_text())

    # --- G-patch conservation, derived not asserted ---
    gp = d["G-patch"]
    if (gp["conserved"], gp["matched"]) != (8, 8):
        problems.append(
            f"domain_residues.json says G-patch {gp['matched']}/{gp['conserved']}, "
            "but RESULTS.md and the review both claim 8/8"
        )
    _require(problems, results, "**8/8.**", "RESULTS.md", "the G-patch 8/8 headline")
    _require(problems, review, "8 of 8 columns conserved at 80 percent", "review",
             "the G-patch conservation claim")
    if gp["panel_members"] != 34 or gp["panel_genes"] != 33:
        problems.append(
            f"G-patch panel is {gp['panel_members']} domains / {gp['panel_genes']} genes, "
            "but the prose says 34 / 33"
        )
    _require(problems, results, "**34 annotated domains across 33 proteins**", "RESULTS.md",
             "the G-patch panel size")

    # --- NKRF anchor mapping ---
    nk = d["gpatch_vs_nkrf"]
    ok = [r for r in nk if r["identical"] and r["inside_nkrf_domain"]]
    if len(ok) != 8:
        problems.append(f"NKRF mapping retains {len(ok)}/8, but the prose claims 8/8")
    for r in nk:
        _require(problems, results,
                 f"AGGF1 {r['aggf1_res']}{r['aggf1_pos']} <- NKRF {r['nkrf_res']}{r['nkrf_pos']}",
                 "RESULTS.md", "an NKRF correspondence row")

    # --- FHA anchors ---
    fa = d["fha_anchors"]
    if fa["retained_strict"] != 6 or fa["total"] != 8:
        problems.append(
            f"FHA anchors are {fa['retained_strict']}/{fa['total']}, but the prose claims 6/8"
        )
    _require(problems, results, "**6/8 strict.**", "RESULTS.md", "the FHA 6/8 headline")
    for pos in ("G437", "R438", "S454", "N478"):
        _require(problems, results, pos, "RESULTS.md", f"FHA anchor {pos}")
        _require(problems, notes, pos, "notes", f"FHA anchor {pos}")
    # The FHA panel must be reported as having NO power, not silently rescued.
    if d["FHA"]["conserved"] != 0:
        problems.append(
            f"FHA column consensus now finds {d['FHA']['conserved']} conserved columns; "
            "RESULTS.md says zero and explains why. Re-read before changing the prose."
        )
    _require(problems, results, "maximum per-column\nagreement of 0.69", "RESULTS.md",
             "the FHA panel's lack of power")

    # --- review-level invariants ---
    doc = yaml.safe_load(review)
    anns = doc["existing_annotations"]
    n_new = sum(1 for a in anns if a["review"]["action"] == "NEW")
    if (len(anns), n_new) != (33, 9):
        problems.append(f"review has {len(anns)} entries / {n_new} NEW, expected 33 / 9")
    _require(problems, notes, "The review adds 9 `NEW` entries on top,", "notes",
             "the NEW-entry count")
    _require(problems, results, "existing_annotations entries: 33", "RESULTS.md",
             "the reconciliation block")

    # --- retracted phrasings must not come back ---
    retracted = {
        "0/8 anchor transfers retained":
            "the discarded global-alignment artefact",
        "8 `NEW` entries":
            "the superseded NEW-entry count (there are now nine, after adding the "
            "GO:0003723 IDA row the PR reviewer asked for)",
        "Eight `GO:0005515` rows":
            "the superseded GO:0005515 row count (there are nine)",
        "three studies, two assay types":
            "the superseded self-interaction count (the BioID row is an artefact)",
        "all four HuRI partners":
            "the over-claim that all four HuRI partners are nuclear; MAB21L3 has "
            "ZERO cellular-component annotations in GOA",
        "all four partners the HuRI":
            "the same over-claim in its other phrasing",
        "All four partners are nuclear":
            "the same over-claim in the reference finding",
        "MAB21L3, all nuclear":
            "the same over-claim in suggested_questions",
        # The PR reviewer found a FIFTH phrasing of the same claim that the four
        # above did not match, in a review.summary. Enumerating phrasings is a
        # losing game, so the pattern check below backs these up.
        "every partner in its own high-throughput interaction record is nuclear":
            "the fifth phrasing of the same over-claim (and 'its high-throughput "
            "record' is 695 BioID partners, not four)",
        # Laboratory-independence claims the author lists contradict.
        "three laboratories":
            "a laboratory count contradicted by the author lists: 18 of 27 papers "
            "share senior author Wang Q/QK",
        "Exactly one, PMID:39905000":
            "the superseded 'only one independent group' claim -- the derived "
            "27-paper set has FOUR senior authors on no Wang-group paper, two of "
            "them substantive (Zhang JH, Chen L)",
        "the only genuinely independent group":
            "the same superseded claim in its other phrasing",
        "the single substantive independent replication":
            "the same superseded claim in its third phrasing",
        "three later laboratories":
            "the same laboratory over-count for the extracellular rows",
        "reproduced repeatedly":
            "an independence claim for two same-senior-author papers",
    }
    for phrase, why in retracted.items():
        for name, text in (("RESULTS.md", results), ("notes", notes), ("review", review)):
            if phrase in re.sub(r"\s+", " ", text):
                problems.append(f"{name}: RETRACTED phrasing present ({why}): {phrase!r}")

    # Enumerating phrasings is a losing game -- the reviewer found a fifth wording
    # of the nuclear over-claim that four literal strings did not match. These
    # patterns catch the CLAIM rather than a spelling of it, in any of the three
    # files, with whitespace normalised so YAML wrapping cannot hide one.
    retracted_patterns = [
        (r"(?:all four|every)[^.]{0,80}partner[^.]{0,80}(?:is|are)\s+nuclear",
         "the nuclear over-claim in any phrasing (MAB21L3 has zero CC annotations)"),
        # Three rounds of this claim, three patterns, each too narrow for the next
        # wording. `lab\b` cannot match "labs" (b->s is not a word boundary), and
        # requiring a count word let the uncounted "confirmed by later labs"
        # through. The rule is now: a VAGUE plural attribution is forbidden,
        # whatever the quantifier.
        (r"\b(?:three|four|five|several|multiple|many|various|numerous|other|later"
         r"|across)\s+(?:\w+\s+){0,2}(?:labs?|laborator\w*|groups?|teams?)\b",
         "a vague plural-laboratory attribution. 18 of the 27 derived papers share "
         "one senior author and 5 more are trainee lineage. A counted, checkable "
         "claim naming the papers is fine -- 'two methods from two laboratories' "
         "(Vidal, Gygi) and 'two laboratories report opposite effects' (Wang QK, "
         "Chen L) are both true and deliberately not matched"),
        # An allele frequency must not be presented as a carrier frequency. gnomAD
        # AF for rs34203073 is ~1.4%; carriers are 2*AF*(1-AF) = 2.8%.
        (r"carried by (?:roughly |about |~)?1\.4\s?%",
         "a gnomAD ALLELE frequency used as a carrier frequency; carriers are ~2.8%"),
    ]
    for pat, why in retracted_patterns:
        for name, text in (("RESULTS.md", results), ("notes", notes), ("review", review)):
            for m in re.finditer(pat, re.sub(r"\s+", " ", text), re.I):
                problems.append(f"{name}: RETRACTED CLAIM ({why}): {m.group(0)[:90]!r}")

    # --- every MODIFY target named in the YAML must be the one the prose names ---
    # This caught a real drift: the notes still said the TNFSF12 row was modified
    # to GO:0043120 after the YAML had moved it to GO:0019955. A term id is the
    # easiest thing in a review to change in one file and forget in another.
    # NOT a dict keyed on the source term id: two of the three MODIFY rows are both
    # GO:0005515 (TNFSF12 and DHX15), so a dict silently drops one of them and the
    # guard then reports a false "target changed" failure. Collect a list.
    targets = [
        (a["term"]["id"], t["id"])
        for a in anns
        if a["review"]["action"] == "MODIFY"
        for t in a["review"].get("proposed_replacement_terms", [])
    ]
    if len(targets) != 3:
        problems.append(f"expected 3 MODIFY replacement terms, found {len(targets)}")
    chosen = {t for _, t in targets}
    if chosen != {"GO:0003723", "GO:0019955", "GO:0017151"}:
        problems.append(
            f"MODIFY targets changed to {sorted(chosen)}; the prose in RESULTS.md and "
            "the notes documents GO:0003723, GO:0019955 and GO:0017151. Update both "
            "before changing this guard."
        )
    for name, text in (("RESULTS.md", results), ("notes", notes)):
        flat = re.sub(r"\s+", " ", text)
        for go in sorted(chosen):
            if go not in flat:
                problems.append(f"{name}: MODIFY target {go} is never mentioned")
        # A rejected alternative may be discussed, but never as the chosen one.
        for verb in ("MODIFY to the informative `GO:0043120",
                     "MODIFY to `GO:0043120"):
            if verb in flat:
                problems.append(f"{name}: names GO:0043120 as the chosen MODIFY target; "
                                "the review chose GO:0019955")

    # --- the FHA claim must stay bounded in every place it is made ---
    _count(problems, results, "untested, not refuted", 1, "RESULTS.md")
    _require(problems, notes, "no phosphopeptide ever tested", "notes",
             "the bounded FHA claim")
    for name, text in (("RESULTS.md", results), ("notes", notes), ("review", review)):
        if re.search(r"AGGF1[^.]{0,80}binds a phosphopeptide\b(?!\.)", text):
            problems.append(f"{name}: appears to assert phosphopeptide binding as fact")

    return problems


def load() -> dict[str, str]:
    return {"results": RESULTS.read_text(), "notes": NOTES.read_text(),
            "review": REVIEW.read_text()}


def self_test() -> int:
    """Prove each guard fires. A passing self-test shows the guards you thought
    of work; it cannot tell you which guard you failed to write."""
    base = load()
    if check(base):
        print("SELF-TEST ABORTED: the unmutated inputs already fail:")
        for p in check(base):
            print("   ", p)
        return 1
    # `n` is how many occurrences to replace. A guard that tests "is this
    # substring present at all" is not exercised by replacing only the first of
    # several occurrences -- the mutation looks applied and the guard correctly
    # still passes, which reads as a missing guard. Replace all of them (n=0).
    mutations = [
        ("results", "**8/8.**", "**7/8.**", 1, "G-patch headline"),
        ("results", "**6/8 strict.**", "**5/8 strict.**", 1, "FHA headline"),
        ("results", "existing_annotations entries: 33", "entries: 31", 1, "reconciliation"),
        ("notes", "The review adds 9 `NEW` entries on top,",
         "The review adds 8 `NEW` entries on top,", 1, "NEW count"),
        ("notes", "G437", "G999", 0, "FHA anchor position in notes"),
        ("results", "N478", "N999", 0, "FHA anchor position in RESULTS.md"),
        ("results", "AGGF1 G631 <- NKRF G563", "AGGF1 G631 <- NKRF G999", 1, "NKRF mapping"),
        ("review", "8 of 8 columns conserved at 80 percent",
         "7 of 8 columns conserved at 80 percent", 1, "review conservation claim"),
        ("results", "maximum per-column\nagreement of 0.69",
         "maximum per-column agreement of 0.99", 1, "FHA panel power note"),
        ("notes", "no phosphopeptide ever tested", "phosphopeptide binding confirmed", 1,
         "the bounded FHA claim"),
        ("results", "untested, not refuted", "refuted outright", 1,
         "the 'untested not refuted' phrasing"),
        ("results", "three of the four HuRI partners", "all four HuRI partners", 1,
         "the retracted 'all four partners are nuclear' over-claim"),
        ("notes", "MODIFY to\n  `GO:0019955 cytokine binding`",
         "MODIFY to the informative `GO:0043120 tumor necrosis factor binding`", 1,
         "a MODIFY target named differently in the prose than in the YAML"),
        ("results", "GO:0017151", "GO:0017152", 0,
         "a MODIFY target missing from RESULTS.md"),
        # The two pattern guards, exercised with wordings the literal `retracted`
        # strings do NOT contain -- which is the whole reason the patterns exist.
        ("review", "Proposed. AGGF1 has no nucleus annotation anywhere in GOA",
         "Proposed. Every partner in this gene's interaction record is nuclear, and "
         "AGGF1 has no nucleus annotation anywhere in GOA", 1,
         "the nuclear over-claim in a wording no literal string covers"),
        ("notes", "This matters for how the review is worded",
         "The nucleus evidence comes from three independent laboratories. "
         "This matters for how the review is worded", 1,
         "a laboratory-count claim in a wording no literal string covers"),
        # Same guard, the wording the corrected prose actually uses.
        ("notes", "This matters for how the review is worded",
         "The nucleus evidence comes from three independent groups. "
         "This matters for how the review is worded", 1,
         "a group-count claim (the wording 'laborator' alone would miss)"),
        # The two wordings that reached a reviewer, both uncounted plurals in a
        # `summary` whose own `reason` already said the opposite.
        # Fragments chosen to sit on ONE physical line: the YAML is dumped at
        # width=100, so a longer span is wrapped and the mutation silently no-ops
        # (which reports as "mutation target absent", not as a passing guard).
        ("review", "by later work from the same group.",
         "by several later labs.", 1,
         "'several later labs' -- the wording that defeated the count-word pattern"),
        ("review", "confirmed by an independent group's",
         "confirmed by later labs including", 1,
         "'later labs' -- an uncounted plural the count-word pattern let through"),
        ("notes", "two substantive independent contributions",
         "the only genuinely independent group", 1,
         "the superseded 'one independent group' count"),
        ("review", "a benign polymorphism: its gnomAD v4 allele",
         "a benign polymorphism carried by roughly 1.4% of the population: its "
         "gnomAD v4 allele", 1,
         "an allele frequency presented as a carrier frequency"),
    ]
    failures = 0
    for key, old, new, n, label in mutations:
        if old not in base[key]:
            print(f"SELF-TEST BROKEN: mutation target absent in {key}: {old!r}")
            failures += 1
            continue
        mutated = dict(base)
        mutated[key] = base[key].replace(old, new) if n == 0 else base[key].replace(old, new, n)
        if mutated[key] == base[key]:
            print(f"SELF-TEST BROKEN: mutation for {label} changed nothing")
            failures += 1
            continue
        if not check(mutated):
            print(f"SELF-TEST FAILED: no guard fires for {label}")
            failures += 1
        else:
            print(f"  ok  guard fires for {label}")
    # And a mutation that should NOT fire anything.
    control = dict(base)
    control["notes"] = base["notes"] + "\n\nHarmless trailing sentence.\n"
    if check(control):
        print("SELF-TEST FAILED: a harmless edit was flagged")
        failures += 1
    else:
        print("  ok  harmless edit not flagged")
    print(f"\nself-test: {failures} failure(s)")
    return 1 if failures else 0


def main() -> int:
    if "--self-test" in sys.argv:
        return self_test()
    problems = check(load())
    for p in problems:
        print("PROBLEM:", p)
    print(f"{len(problems)} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
