#!/usr/bin/env python3
"""Guard: the prose surfaces must not drift from the computed results.

Three prose surfaces restate numbers that `ubib_motif_analysis.py` and
`family_annotation_census.py` compute:

  * `ADCK5-bioinformatics/RESULTS.md`
  * `ADCK5-notes.md`
  * `ADCK5-ai-review.yaml`

Nothing generates those files, so a corrected number can land in one and not the others -
the "fixed in N places, landed in N-1" failure. This script re-reads the JSON outputs and
asserts every restated value against them, and asserts that phrasings this review explicitly
withdrew do not reappear.

Design constraints learned from earlier genes in this campaign:

  * Count **surfaces** (files containing a claim), never summed occurrences: a lint that
    sums passes when one file contains N copies and the other N-1 files contain none.
  * Assert the target is **present** before judging it. A check that `continue`s when it
    cannot find its subject passes silently if the subject is deleted.
  * Collect problems and return them; never `raise` from inside a check, or the first
    failure aborts every later check *and the self-test baseline* while the harness still
    prints as though it ran.

Run `--self-test` to break-test the guards. Every check is exercised in the direction it
exists to catch AND in the happy direction, because a check can be wrong about success as
easily as about failure.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
GENE_DIR = HERE.parent

RESULTS_MD = HERE / "RESULTS.md"
NOTES_MD = GENE_DIR / "ADCK5-notes.md"
REVIEW_YAML = GENE_DIR / "ADCK5-ai-review.yaml"
MOTIF_JSON = HERE / "results.json"
CENSUS_JSON = HERE / "family_census.json"
PARTNER_JSON = HERE / "partner_localisation.json"

# The paragraph that actually shipped with the withdrawn compartment claim unhedged, frozen
# as a file. It was originally read from branch commit 419dc9e37 by `git show` - but a
# branch-local SHA does not survive squash-merge, so the strongest test in this suite would
# have silently lost its fixture the moment the PR landed. Freeze the evidence, don't
# reference it.
HISTORICAL_FIXTURE = HERE / "fixtures" / "historical_unhedged_compartment_paragraph.md"

PROSE_SURFACES = [RESULTS_MD, NOTES_MD, REVIEW_YAML]

# Phrasings this review considered and withdrew after measuring. If one reappears, some
# surface has been reverted to a claim the data refused.
WITHDRAWN_PHRASES = [
    # The first draft of RESULTS.md said all 25 coIP partners were mitochondrial; measuring
    # each partner's UniProt subcellular location gave 17 of 25.
    "25 mitochondrial proteins",
    # ADCK5 has no protein-kinase GO annotation at all, so no such row can be "removed".
    "remove the protein kinase activity annotation",
    # The mirror error the brief warns about: the family demonstrably CAN phosphorylate a
    # protein (COQ8B -> COQ3), so a blanket denial is wrong.
    "UbiB proteins cannot phosphorylate proteins",
    "ADCK5 is a pseudokinase",
    # Conceded to the PR reviewer: the compartment argument assumes a membrane sidedness this
    # review elsewhere declines to assert, so it must be stated as an assumption, never as a
    # flat conclusion. This phrasing survived in three places after the first "fix" - the
    # canonical "fixed in N places, landed in N-1" failure - which is why it is pinned here.
    "topologically implausible",
    "topological objection",
]

# Prose surfaces are not the only place a withdrawn phrasing can hide: it also lived in a
# script docstring. Scan the whole gene folder for these, not just the three prose files.
WITHDRAWN_SCAN_GLOBS = ["*.md", "*.yaml", "ADCK5-bioinformatics/*.py", "ADCK5-bioinformatics/*.md"]

# ---------------------------------------------------------------------------------------
# A literal-phrase matcher CANNOT catch paraphrase. This is a property of the design, not a
# gap in the phrase list, and it has already cost this review one round: after
# "topologically implausible" was pinned above, the same withdrawn claim survived in
# RESULTS.md as "removes exactly the targeting constraint that makes the pairing implausible
# in vivo" - in a file that WAS in scope. Scope was widened; vocabulary was not.
#
# Adding two more literals would not fix that. So the compartment claim is guarded
# structurally instead, by a CO-OCCURRENCE INVARIANT keyed on the topic rather than on the
# wording of the conclusion:
#
#     any surface that discusses the ADCK5-NOTCH2NLA compartment argument at all
#     must also carry an explicit statement that ADCK5's membrane sidedness is unmeasured.
#
# Paraphrasing the conclusion cannot evade this, because the trigger is the topic.
#
# The invariant is enforced PER PARAGRAPH, not per file, and that distinction is the whole
# point. A file-level version of this check was written first and then tested against the
# actual text that shipped and was missed - and it PASSED, because the historical RESULTS.md
# hedged in a different section while asserting the claim under "Topology:". File-level
# co-occurrence is not proximity, and a guard that cannot catch the defect it was written
# for is worse than none, because it reads as coverage. So the hedge must appear in the same
# paragraph as the topic, or in the one immediately following it.
#
# `--self-test` replays that historical paragraph verbatim from git and requires a catch.
# Residual limit, stated rather than hidden: a hedge more than one paragraph away still
# evades this, so withdrawing a claim still calls for a human re-read of the prose.
# ---------------------------------------------------------------------------------------

# The trigger must fire on the ARGUMENT, not on every mention of the partner. What makes a
# paragraph an instance of the compartment argument is that it states NOTCH2NLA's own
# localisation - that is the contrast the argument is built from. Paragraphs that merely
# list NOTCH2NLA among partners, or name it in a verdict table, do not, and a first version
# keyed on "mentions the partner AND any compartment word" produced three false positives on
# exactly those.
COMPARTMENT_TOPIC_RE = re.compile(r"NOTCH2NLA|Q7Z3S9", re.I)
COMPARTMENT_CONTEXT_RE = re.compile(r"secreted|cytoplasm|cytosol", re.I)
# Any ONE of these counts as the hedge being present.
SIDEDNESS_HEDGE_RES = [
    re.compile(r"sidedness", re.I),
    re.compile(r"(never|has not|not) been (measured|determined)", re.I),
    re.compile(r"stated (here )?as an assumption", re.I),
    re.compile(r"supporting consideration", re.I),
]


def _paragraphs(text: str, name: str = "") -> list[str]:
    """Split a surface into the units the hedge invariant is enforced over.

    **This must be structure-aware, and the reason is a bug that shipped.** The first version
    split on blank lines only. `ADCK5-ai-review.yaml` contains *zero* blank lines, so the
    entire 550-line file came back as ONE paragraph - making the "paragraph-local" guard
    file-level again on the single most important surface, which is exactly the failure it
    was written to fix. The hedge in the GO:0016020 row was silently satisfying the check for
    an unhedged claim in a different annotation 60 lines away.

    So YAML is split by *scalar value*: each summary, reason, gap_statement, boundary,
    question and so on is its own unit, which is the granularity a reader actually reasons
    over. Markdown keeps blank-line paragraphs.
    """
    if name.endswith((".yaml", ".yml")):
        try:
            doc = yaml.safe_load(text)
        except yaml.YAMLError:
            # Fall back loudly rather than silently degrading to the broken behaviour.
            return [f"__UNPARSEABLE_YAML__ {text}"]
        out: list[str] = []

        def walk(o):
            if isinstance(o, str):
                out.append(o)
            elif isinstance(o, dict):
                for v in o.values():
                    walk(v)
            elif isinstance(o, list):
                for v in o:
                    walk(v)

        walk(doc)
        return out
    return [b for b in re.split(r"\n\s*\n", text)]


def check_compartment_hedge(texts: dict[str, str]) -> list[str]:
    """Structural guard: discussing the compartment argument obliges you to hedge it NEARBY.

    Keyed on the TOPIC, so it survives rewording of the conclusion - unlike the literal
    phrase list, which it exists to compensate for. Enforced per paragraph (with a
    one-paragraph lookahead) because the file-level version demonstrably failed to catch the
    real defect.
    """
    problems: list[str] = []
    triggered = 0
    for name, text in texts.items():
        paras = _paragraphs(text, name)
        for i, para in enumerate(paras):
            if not (COMPARTMENT_TOPIC_RE.search(para) and COMPARTMENT_CONTEXT_RE.search(para)):
                continue
            triggered += 1
            # Markdown paragraphs often continue an argument into the next block, so allow a
            # one-paragraph lookahead there. A YAML scalar is a self-contained field written
            # by one author about one thing, and the next scalar is usually an unrelated key -
            # letting it satisfy the hedge is how the file-level version went wrong. No
            # lookahead for YAML.
            if name.endswith((".yaml", ".yml")):
                window = para
            else:
                window = para + "\n" + (paras[i + 1] if i + 1 < len(paras) else "")
            if not any(r.search(window) for r in SIDEDNESS_HEDGE_RES):
                problems.append(
                    f"{name}: a paragraph discusses the ADCK5-NOTCH2NLA compartment argument "
                    f"with no statement nearby that ADCK5's membrane sidedness is unmeasured. "
                    f"The review withdrew the unhedged form of this claim. Paragraph starts: "
                    f"{para.strip()[:90]!r}"
                )
    if triggered == 0:
        problems.append(
            "compartment-hedge guard is vacuous: no paragraph matched the topic, so the "
            "invariant proved nothing. Check the topic pattern before trusting a pass."
        )
    return problems

# Claims that must appear on at least `min_surfaces` of the prose surfaces.
REQUIRED_CLAIMS = [
    ("K147", 2),  # KxGQ lysine
    ("A209", 2),  # A-rich loop alanine
    ("D382", 2),  # DFG aspartate (cited in the suggested kinase-dead control)
    ("17 of 25", 2),
]


def load_json(path: Path) -> dict:
    if not path.exists():
        raise SystemExit(
            f"FATAL: {path.name} is missing. Run the analysis scripts first:\n"
            f"  python3 {HERE / 'ubib_motif_analysis.py'}\n"
            f"  python3 {HERE / 'family_annotation_census.py'}"
        )
    return json.loads(path.read_text())


# Residue tokens that legitimately belong to OTHER proteins' numbering and so must not be
# read as drifted ADCK5 calls. Every entry is a residue this review cites from a named
# reference protein; the set is asserted DISJOINT from the computed ADCK5 tokens, because an
# allowlist that overlapped them could mask exactly the drift this guard exists to catch.
FOREIGN_RESIDUE_TOKENS = {
    "K276",  # COQ8A KxGQ lysine
    "A339",  # COQ8A A-rich loop alanine
    "D488",  # COQ8A catalytic base
    "D507",  # COQ8A DFG aspartate
    "K134",  # yeast Coq8p KxGQ lysine
    "A197",  # yeast Coq8p A-rich loop alanine
    "D365",  # yeast Coq8p active-site aspartate
    "G53",   # PKA Calpha G-rich loop, UniProt numbering
    "K73",   # PKA Calpha beta3 lysine
    "E92",   # PKA Calpha alphaC glutamate
    "D167",  # PKA Calpha catalytic aspartate
    "N172",  # PKA Calpha catalytic-loop asparagine
    "D185",  # PKA Calpha DFG aspartate
    "S181",  # SOX9 phosphosite
}

RESIDUE_TOKEN_RE = re.compile(r"\b([A-Z]\d{2,3})\b")


def check_residue_calls(motif: dict, texts: dict[str, str]) -> list[str]:
    """Residue tokens in the prose must be either a computed ADCK5 call or a declared
    foreign-numbering citation - nothing else.

    An earlier version of this check compared every computed residue against every
    same-letter token and so reported a conflict between K147 and K228, which are BOTH
    correct: it failed on perfect agreement. The lesson (and the campaign's) is that the
    happy path is the one most likely to go untested.
    """
    problems: list[str] = []

    computed = {
        f"{c['subject_residue']}{c['subject_position']}"
        for c in motif["columns"]
        if c.get("subject_position") is not None
    }
    if not computed:
        problems.append(
            "residue guard is vacuous: results.json yielded ZERO positioned subject "
            "residues, so nothing was actually checked"
        )
        return problems

    overlap = computed & FOREIGN_RESIDUE_TOKENS
    if overlap:
        problems.append(
            f"allowlist overlaps computed residues {sorted(overlap)} - the allowlist could "
            f"mask a drift in exactly those positions"
        )

    # Presence: assert each computed residue is actually stated somewhere. A guard that only
    # validates tokens it happens to find passes silently when the claim is deleted.
    for tok in sorted(computed):
        if not any(tok in t for t in texts.values()):
            problems.append(f"computed residue {tok} is not stated on any prose surface")

    # Absence of anything else: a drifted position becomes an unrecognised token.
    allowed = computed | FOREIGN_RESIDUE_TOKENS
    for name, text in texts.items():
        for m in RESIDUE_TOKEN_RE.finditer(text):
            tok = m.group(1)
            if tok not in allowed:
                problems.append(
                    f"{name}: unrecognised residue token {tok!r} - not a computed ADCK5 "
                    f"residue {sorted(computed)} nor a declared foreign citation"
                )
    return problems


def check_census_numbers(census: dict, texts: dict[str, str]) -> list[str]:
    problems: list[str] = []
    c = census["census"]

    # ADCK5 must be the ONLY human UbiB gene with zero IBA, and the prose says so.
    zero_iba = sorted(g for g, v in c.items() if v["n_iba"] == 0)
    if zero_iba != ["ADCK5"]:
        problems.append(
            f"census: genes with zero IBA are {zero_iba}, but the prose claims ADCK5 is "
            f"the only one"
        )

    # EC split: the assayed pair downgraded, the unassayed pair not.
    for gene, expected in [
        ("COQ8A", "2.7.-.-"),
        ("COQ8B", "2.7.-.-"),
        ("ADCK5", "2.7.11.-"),
        ("ADCK2", "2.7.11.-"),
    ]:
        got = c[gene]["ec_numbers"]
        if got != [expected]:
            problems.append(f"census: {gene} EC is {got}, prose asserts {expected}")

    # The NOT| rows that make the family argument.
    for gene in ("COQ8A", "COQ8B"):
        if len(c[gene]["negated_annotations"]) != 2:
            problems.append(
                f"census: {gene} has {len(c[gene]['negated_annotations'])} NOT| rows, "
                f"prose asserts 2"
            )

    # ADCK5 must still carry the Ser/Thr kinase keyword - the whole UniProt-correction
    # recommendation is void if UniProt has already fixed it.
    if not c["ADCK5"]["has_ser_thr_kinase_keyword"]:
        problems.append(
            "census: ADCK5 no longer has the Ser/Thr-kinase keyword - the UniProt "
            "correction request in suggested_questions is now stale and must be revised"
        )
    return problems


def check_partner_numbers(partner: dict, texts: dict[str, str]) -> list[str]:
    """The partner-topology numbers in the prose must equal the computed ones.

    These were asserted from an ad-hoc query before `partner_localisation.py` existed, which
    is precisely the "hand-written label drifts from the computed one" failure.
    """
    problems: list[str] = []
    mi = partner["mito_interactome"]

    # The exact phrase the prose uses, derived from the computation rather than typed.
    expected_fraction = mi["fraction_text"]  # e.g. "17 of 25"
    surfaces = [n for n, t in texts.items() if expected_fraction in t]
    if not surfaces:
        problems.append(
            f"computed mitochondrial fraction {expected_fraction!r} appears on no prose "
            f"surface - either the prose drifted or the measurement changed"
        )

    # Any OTHER "N of 25"/"N of M" fraction about this partner set would be a stale value.
    for name, text in texts.items():
        for m in re.finditer(r"\b(\d+) of (\d+)\b", text):
            if m.group(0) != expected_fraction and m.group(2) == str(mi["n_partners"]):
                problems.append(
                    f"{name}: stale partner fraction {m.group(0)!r}; computed value is "
                    f"{expected_fraction!r}"
                )

    # The IntAct record total, also restated in prose.
    n_rec = partner["n_intact_records"]
    if not any(f"{n_rec} IntAct" in t or f"all {n_rec} IntAct" in t for t in texts.values()):
        problems.append(
            f"computed IntAct record count ({n_rec}) is not stated on any prose surface"
        )

    # The MI score, and the per-PMID method split that carries the "one screen, three
    # sub-method labels" argument. Both were prose-only until partner_localisation.py emitted
    # them; the expected strings are derived from the JSON here rather than typed, so the
    # prose and the check cannot drift apart independently.
    for acc, g in partner["goa_binding_partners"].items():
        scores = g.get("mi_scores") or []
        if len(scores) == 1:
            score_str = f"MI score {scores[0]}"
            if not any(score_str in t for t in texts.values()):
                problems.append(
                    f"{acc}: computed single MI score {scores[0]} is not stated as "
                    f"{score_str!r} on any prose surface"
                )
        else:
            # More than one distinct score means "0.67 throughout" is no longer true.
            for name, text in texts.items():
                if "MI score 0.67" in text:
                    problems.append(
                        f"{name}: claims a single MI score but the computation now returns "
                        f"{scores} for {acc}"
                    )

        split = g.get("methods_by_pmid") or {}
        if not split:
            problems.append(f"{acc}: methods_by_pmid is empty, so the sub-method argument is unbacked")
        for pm, methods in split.items():
            if len(methods) > 1:
                # The prose must name this reference as the multi-sub-method one.
                if not any(pm in t for t in texts.values()):
                    problems.append(
                        f"{acc}: PMID:{pm} carries {len(methods)} sub-method labels "
                        f"({methods}) but is not named on any prose surface"
                    )
                for m in methods:
                    if not any(m in t for t in texts.values()):
                        problems.append(
                            f"{acc}: sub-method label {m!r} from PMID:{pm} is not stated on "
                            f"any prose surface, so the 'three labels, one screen' claim is "
                            f"not fully evidenced"
                        )

    # The load-bearing negative: no orthogonal (non-two-hybrid) assay for the GOA partner.
    orth = partner["orthogonal_assay_for_goa_partners"]
    if not orth:
        problems.append(
            "partner JSON lists no GO:0005515 partners at all - the 'no orthogonal assay' "
            "claim would be vacuous"
        )
    for acc, has_orth in orth.items():
        if has_orth:
            problems.append(
                f"partner {acc} now HAS a non-two-hybrid assay in IntAct - the review's "
                f"'no orthogonal assay' argument for MARK_AS_OVER_ANNOTATED is stale and "
                f"the verdict must be revisited"
            )
    return problems


def all_surfaces(texts: dict[str, str]) -> dict[str, str]:
    """The three prose surfaces plus every other file in the gene folder that can carry prose.

    Detector and mutator must agree on scope or the verification is structurally blind, so
    this is the single definition both the withdrawn-phrase and compartment-hedge checks use.
    Files are keyed by path relative to the gene directory, and the prose surfaces are keyed
    the same way, so RESULTS.md is not scanned twice under two different keys.
    """
    # A caller-supplied (possibly mutated) text wins; anything absent falls back to DISK,
    # never to an empty string. Blanking an unsupplied surface would silently shrink the
    # scanned corpus and turn a partial `texts` dict into a false pass.
    out = {}
    for p in PROSE_SURFACES:
        out[str(p.relative_to(GENE_DIR))] = texts.get(p.name, p.read_text())
    this_file = Path(__file__).resolve()
    for pattern in WITHDRAWN_SCAN_GLOBS:
        for f in sorted(GENE_DIR.glob(pattern)):
            # Skip only THIS file: it is the registry of withdrawn phrasings, so it
            # necessarily contains every one of them. Excluding it by resolved path rather
            # than by extension keeps every other script in scope - the docstring that hid
            # 'topological objection' was in a sibling .py.
            if f.resolve() == this_file:
                continue
            out.setdefault(str(f.relative_to(GENE_DIR)), f.read_text())
    return out


def check_withdrawn(texts: dict[str, str]) -> list[str]:
    """Withdrawn phrasings must not reappear on ANY surface in the gene folder.

    The scan deliberately covers more than the three prose files: 'topologically implausible'
    was softened in the review summary but survived in a second YAML field and in a script
    docstring, and a detector scoped narrower than the mutator cannot see what it missed.
    """
    problems = []
    for name, text in all_surfaces(texts).items():
        # Normalise quotation marks so a phrase cannot evade the matcher by being quoted
        # (a quote-splitting bypass was found on ACTA1).
        flat = re.sub(r"[\"'`]", "", text.lower())
        flat = re.sub(r"\s+", " ", flat)
        for phrase in WITHDRAWN_PHRASES:
            if re.sub(r"\s+", " ", phrase.lower()) in flat:
                problems.append(f"{name}: withdrawn phrasing reappeared: {phrase!r}")
    return problems


def check_required_claims(texts: dict[str, str]) -> list[str]:
    """Count SURFACES containing each claim, not total occurrences."""
    problems = []
    for claim, min_surfaces in REQUIRED_CLAIMS:
        surfaces = [n for n, t in texts.items() if claim in t]
        if len(surfaces) < min_surfaces:
            problems.append(
                f"required claim {claim!r} appears on {len(surfaces)} surface(s) "
                f"({surfaces}), expected at least {min_surfaces}"
            )
    return problems


def run_checks(texts: dict[str, str], motif: dict, census: dict, partner: dict) -> list[str]:
    problems: list[str] = []
    problems += check_residue_calls(motif, texts)
    problems += check_census_numbers(census, texts)
    problems += check_partner_numbers(partner, texts)
    problems += check_withdrawn(texts)
    problems += check_compartment_hedge(all_surfaces(texts))
    problems += check_required_claims(texts)
    return problems


def read_surfaces() -> dict[str, str]:
    texts = {}
    for p in PROSE_SURFACES:
        if not p.exists():
            raise SystemExit(f"FATAL: prose surface missing: {p}")
        texts[p.name] = p.read_text()
    return texts


def self_test() -> int:
    motif = load_json(MOTIF_JSON)
    census = load_json(CENSUS_JSON)
    partner = load_json(PARTNER_JSON)
    good = read_surfaces()

    failures: list[str] = []

    def expect_clean(desc: str, texts, motif=motif, census=census, partner=partner):
        probs = run_checks(texts, motif, census, partner)
        if probs:
            failures.append(f"{desc}: expected clean, got {probs}")
            print(f"  FAIL (flagged good input): {desc} -> {probs}")
        else:
            print(f"  PASS (accepted good input): {desc}")

    def expect_flag(desc: str, texts, motif=motif, census=census, partner=partner, match=None):
        """`match` names a substring the offending message must contain.

        Without it a break-test passes when ANY check fires, so a mutation could be
        'caught' by a completely unrelated guard while the one under test stayed blind -
        presence without the distinguishing attribute.
        """
        probs = run_checks(texts, motif, census, partner)
        if not probs:
            failures.append(f"{desc}: expected a problem, got none")
            print(f"  FAIL (missed): {desc}")
            return
        if match is not None and not any(match in p for p in probs):
            failures.append(
                f"{desc}: something fired but not the guard under test "
                f"(no message contains {match!r}); got {probs}"
            )
            print(f"  FAIL (wrong guard fired): {desc}")
            return
        print(f"  PASS (caught): {desc}")

    # happy direction first - a guard can be wrong about success as easily as failure
    expect_clean("unmodified surfaces", good)

    # 1. residue drift
    target = "A209"
    assert any(target in t for t in good.values()), "mutation target absent; guard vacuous"
    drifted = {k: v.replace(target, "A210") for k, v in good.items()}
    expect_flag("a residue position drifted (A209 -> A210)", drifted)

    # 2. withdrawn phrasing, plain and quote-split
    expect_flag(
        "withdrawn phrasing reappears",
        {**good, "RESULTS.md": good["RESULTS.md"] + "\n25 mitochondrial proteins\n"},
    )
    expect_flag(
        "withdrawn phrasing reappears with quotes inserted (bypass attempt)",
        {**good, "RESULTS.md": good["RESULTS.md"] + '\n25 "mitochondrial" proteins\n'},
    )

    # 3. required claim deleted from all but one surface (surface counting, not summing)
    stripped = dict(good)
    for k in list(stripped):
        if k != "RESULTS.md":
            stripped[k] = stripped[k].replace("17 of 25", "")
    # and pile extra copies into the remaining surface: a summing lint would pass here
    stripped["RESULTS.md"] = stripped["RESULTS.md"] + "\n17 of 25\n" * 5
    expect_flag("claim present 6x on ONE surface but deleted from the others", stripped)

    # 4. census drift
    bad_census = json.loads(json.dumps(census))
    bad_census["census"]["ADCK5"]["n_iba"] = 3
    expect_flag("ADCK5 gained IBA annotations", good, census=bad_census)

    bad_census2 = json.loads(json.dumps(census))
    bad_census2["census"]["ADCK5"]["has_ser_thr_kinase_keyword"] = False
    expect_flag("UniProt dropped the keyword (correction request now stale)", good, census=bad_census2)

    bad_census3 = json.loads(json.dumps(census))
    bad_census3["census"]["COQ8A"]["negated_annotations"] = []
    expect_flag("COQ8A lost its NOT| rows", good, census=bad_census3)

    # 5. partner-number drift
    bad_p = json.loads(json.dumps(partner))
    bad_p["mito_interactome"]["fraction_text"] = "19 of 25"
    expect_flag("mitochondrial fraction drifted (prose still says 17 of 25)", good, partner=bad_p)

    bad_p2 = json.loads(json.dumps(partner))
    for k in bad_p2["orthogonal_assay_for_goa_partners"]:
        bad_p2["orthogonal_assay_for_goa_partners"][k] = True
    expect_flag("an orthogonal assay appeared for the GO:0005515 partner", good, partner=bad_p2)

    bad_p3 = json.loads(json.dumps(partner))
    bad_p3["orthogonal_assay_for_goa_partners"] = {}
    expect_flag("no GOA partners in the JSON (claim would be vacuous)", good, partner=bad_p3)

    # The MI-score and per-PMID sub-method checks: each must be REACHABLE, not merely
    # present. A check that can never fire reads as coverage while providing none.
    dropped_label = {
        k: v.replace("two hybrid prey pooling approach", "XXX") for k, v in good.items()
    }
    expect_flag("a sub-method label vanished from the prose", dropped_label)

    drifted_mi = {k: v.replace("MI score 0.67", "MI score 0.90") for k, v in good.items()}
    expect_flag("the MI score in the prose drifted from the computed one", drifted_mi)

    bad_p4 = json.loads(json.dumps(partner))
    for a in bad_p4["goa_binding_partners"].values():
        a["mi_scores"] = [0.67, 0.42]
    expect_flag(
        "IntAct now reports more than one MI score, so 'MI score 0.67 throughout' is false",
        good,
        partner=bad_p4,
    )

    bad_p5 = json.loads(json.dumps(partner))
    for a in bad_p5["goa_binding_partners"].values():
        a["methods_by_pmid"] = {}
    expect_flag("methods_by_pmid emptied (sub-method argument would be unbacked)", good, partner=bad_p5)

    # The withdrawn-phrase scan covers the whole gene folder, and excludes exactly ONE file:
    # this one, which necessarily contains every withdrawn phrase because it defines them.
    # That exclusion must be narrow. Plant a phrase in a SIBLING script and require a catch.
    # Use a THROWAWAY file, never a tracked source: a self-test that mutates the repo can
    # leave it dirty if it dies between write and restore.
    throwaway = HERE / "_selftest_scope_probe.py"
    assert not throwaway.exists(), f"{throwaway.name} already exists; refusing to clobber it"
    try:
        throwaway.write_text("# topological objection\n")
        expect_flag(
            "withdrawn phrasing planted in a sibling .py (scan must not be too narrow)", good
        )
    finally:
        throwaway.unlink(missing_ok=True)
    assert not throwaway.exists(), "self-test failed to remove its throwaway file"
    expect_clean("throwaway removed, tree clean again", good)

    # --- the compartment-hedge guard, both directions ---
    # Catch: strip every hedge marker while leaving the topic in place. A literal-phrase
    # matcher cannot see this; the co-occurrence invariant must.
    unhedged = {}
    for k, v in good.items():
        for r in SIDEDNESS_HEDGE_RES:
            v = r.sub("REDACTED", v)
        unhedged[k] = v
    expect_flag("compartment argument discussed with every hedge removed", unhedged)

    # Catch by PARAPHRASE: reinstate the withdrawn conclusion in new words, no pinned literal
    # anywhere, hedges stripped. This is the exact failure that reached RESULTS.md.
    paraphrased = dict(unhedged)
    paraphrased["RESULTS.md"] = (
        unhedged["RESULTS.md"]
        + "\n\nY2H removes exactly the targeting constraint that makes the NOTCH2NLA "
        "pairing impossible in vivo.\n"
    )
    expect_flag("withdrawn claim reinstated as PARAPHRASE with no pinned literal", paraphrased)

    # Happy: the real surfaces discuss the topic AND hedge it.
    expect_clean("compartment argument discussed and properly hedged", good)

    # The strongest available test: replay the ACTUAL paragraph that shipped and was missed,
    # read from git rather than retyped. A synthetic mutation only proves the guard catches
    # the failure I imagined; this proves it catches the one that really happened. A
    # file-level version of this check passed here, which is why the guard is paragraph-local.
    if not HISTORICAL_FIXTURE.exists():
        failures.append(
            f"regression fixture missing: {HISTORICAL_FIXTURE}. The historical-defect replay "
            f"is the strongest test here; a missing fixture must fail loudly, not be skipped."
        )
        print("  FAIL (fixture missing): historical defect replay")
    else:
        hist = HISTORICAL_FIXTURE.read_text()
        if "makes the pairing implausible" not in hist:
            failures.append(
                "the regression fixture no longer contains the flagged wording, so the replay "
                "would prove nothing"
            )
            print("  FAIL (fixture corrupted): historical defect replay")
        else:
            expect_flag(
                "the REAL historical defect, replayed from the frozen fixture",
                {**good, "RESULTS.md": hist},
                match="compartment argument",
            )

    # 6. the residue guard must not silently pass when it has nothing to check
    empty_motif = {"columns": []}
    expect_flag("results.json has no positioned residues (guard must not pass vacuously)",
                good, motif=empty_motif)

    # --- invariants about the harness itself, not about the gene ---
    # A partial `texts` dict must fall back to DISK for the surfaces it omits. Blanking them
    # would shrink the scanned corpus and turn a partial dict into a false pass.
    partial = m_partial = all_surfaces({"ADCK5-notes.md": good["ADCK5-notes.md"]})
    blanked = [k for k, v in partial.items() if not v.strip()]
    if blanked:
        failures.append(f"all_surfaces() blanked {blanked} when given a partial dict")
        print("  FAIL: all_surfaces() blanks omitted surfaces")
    else:
        print("  PASS: all_surfaces() falls back to disk for omitted surfaces")

    # The regression fixture deliberately CONTAINS the unhedged claim. If it is ever pulled
    # into the live scan (e.g. by widening a glob to be recursive) the audit would fail on a
    # file whose whole purpose is to preserve the bad text.
    scanned = all_surfaces(good)
    leaked = [k for k in scanned if "fixtures" in k]
    if leaked:
        failures.append(
            f"the regression fixture is being scanned as a live surface: {leaked}. It holds "
            f"the withdrawn claim on purpose; exclude it or the audit will fail on itself."
        )
        print("  FAIL: regression fixture leaked into the live scan")
    else:
        print("  PASS: regression fixture is excluded from the live scan")

    print()
    if failures:
        for f in failures:
            print("SELF-TEST FAILURE:", f)
        return 1
    print("self-test: all guards behaved correctly in both directions")
    return 0


def main() -> int:
    if "--self-test" in sys.argv:
        return self_test()
    motif = load_json(MOTIF_JSON)
    census = load_json(CENSUS_JSON)
    partner = load_json(PARTNER_JSON)
    texts = read_surfaces()
    problems = run_checks(texts, motif, census, partner)
    print(f"audited {len(texts)} prose surfaces against 3 computed JSON outputs")
    if problems:
        print(f"\n{len(problems)} problem(s):")
        for p in problems:
            print("  -", p)
        return 1
    print("no drift detected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
