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

HERE = Path(__file__).resolve().parent
GENE_DIR = HERE.parent

RESULTS_MD = HERE / "RESULTS.md"
NOTES_MD = GENE_DIR / "ADCK5-notes.md"
REVIEW_YAML = GENE_DIR / "ADCK5-ai-review.yaml"
MOTIF_JSON = HERE / "results.json"
CENSUS_JSON = HERE / "family_census.json"
PARTNER_JSON = HERE / "partner_localisation.json"
PAINT_TSV = (
    GENE_DIR.parent.parent.parent
    / "interpro" / "panther" / "PTHR43173" / "PTHR43173-paint.tsv"
)

# The paragraph that actually shipped with the withdrawn compartment claim unhedged, frozen
# as a file. It was originally read from branch commit 419dc9e37 by `git show` - but a
# branch-local SHA does not survive squash-merge, so the strongest test in this suite would
# have silently lost its fixture the moment the PR landed. Freeze the evidence, don't
# reference it.
HISTORICAL_FIXTURE = HERE / "fixtures" / "historical_unhedged_compartment_paragraph.md"
PARITY_FIXTURE = HERE / "fixtures" / "historical_unhedged_parity_units.md"

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
# `--self-test` replays that historical paragraph from a frozen fixture and requires a catch.
# Residual limit, stated rather than hidden: a hedge more than one paragraph away still
# evades this, so withdrawing a claim still calls for a human re-read of the prose.
# ---------------------------------------------------------------------------------------

# The trigger must fire on the ARGUMENT, not on every mention of the partner. What makes a
# paragraph an instance of the compartment argument is that it states NOTCH2NLA's own
# localisation - that is the contrast the argument is built from. Paragraphs that merely
# list NOTCH2NLA among partners, or name it in a verdict table, do not, and a first version
# keyed on "mentions the partner AND any compartment word" produced three false positives on
# exactly those.
# ---------------------------------------------------------------------------------------
# Second structural invariant, for this review's OTHER retracted claim.
#
# An earlier draft argued the UniProt SL-0173 (Mitochondrion) vs SL-0162 (Membrane) split
# between the ADCK paralogs and ADCK5 showed identical evidence being treated differently.
# It does not: ADCK1 and ADCK2 each hold an experimental ECO:0000269|PubMed:33988507
# localisation from a kinome-wide screen whose library did not contain ADCK5. The retraction
# had to be applied FOUR times, and the occurrence that survived longest was in a
# `reference_review` note - a low-salience surface nobody re-reads.
#
# A literal phrase pin is the wrong instrument (paraphrase defeats it, as this PR already
# demonstrated), so this is keyed on the CONTRAST: any unit that discusses a paralog's
# UniProt subcellular treatment must also carry the untested-assay clause.
# ---------------------------------------------------------------------------------------
PARITY_TOPIC_RE = re.compile(r"\bADCK1\b|\bADCK2\b", re.I)
PARITY_CONTEXT_RE = re.compile(
    # Deliberately about UniProt's TREATMENT of localisation, not about mitochondria in
    # general: a bare "mitochondrial localisation" alternative was tried and fired on the
    # PAINT question and a knowledge_gaps entry, neither of which is about SubCell at all.
    r"SL-0173|SL-0162|subcellular location|SubCell|mitochondrial UniProt|"
    r"UniProt (mitochondrial|localisation|localization)",
    re.I,
)
# The heading of the RESULTS.md section this guard protects - "Why ADCK1 and ADCK2 get a
# mitochondrial UniProt annotation and ADCK5 does not" - was invisible to the first
# pattern. Benign in itself, but it is the paraphrase escape the guard exists to resist,
# sitting on the first line of the thing being guarded.
PARITY_HEDGE_RES = [
    re.compile(r"33988507"),
    re.compile(r"absent from (the|its) .*library", re.I),
    re.compile(r"untested", re.I),
    re.compile(r"never (been )?tested", re.I),
    re.compile(r"did not contain ADCK5", re.I),
]


def check_parity_hedge(texts: dict[str, str]) -> list[str]:
    """Discussing a paralog's UniProt localisation obliges you to note the assay asymmetry.

    Unlike check_compartment_hedge this deliberately has NO one-paragraph lookahead. The unit
    that most needs qualifying here is a section *heading*, and a heading that states the
    contrast is read on its own - in a table of contents, in a diff, in search results - so
    letting the body below satisfy it would exempt exactly the surface that travels furthest
    from its context.
    """
    problems: list[str] = []
    triggered_by_surface: dict[str, int] = {}
    for name, text in texts.items():
        triggered_by_surface.setdefault(name, 0)
        for i, unit in enumerate(_paragraphs(text, name)):
            if not (PARITY_TOPIC_RE.search(unit) and PARITY_CONTEXT_RE.search(unit)):
                continue
            triggered_by_surface[name] += 1
            if not any(r.search(unit) for r in PARITY_HEDGE_RES):
                problems.append(
                    f"{name}: a unit contrasts ADCK1/ADCK2 UniProt subcellular treatment with "
                    f"ADCK5's without noting that their SL-0173 rests on an assay ADCK5 was "
                    f"never in (PubMed:33988507). This review retracted the parity framing. "
                    f"Unit starts: {unit.strip()[:90]!r}"
                )
    # Per surface, not corpus-wide - the same correction check_compartment_hedge already
    # carries. A corpus-wide counter stays satisfied while the guard goes blind on the review
    # YAML, which is where the parity claim's most consequential statements live.
    for required in ("ADCK5-ai-review.yaml", "ADCK5-bioinformatics/RESULTS.md"):
        if triggered_by_surface.get(required, 0) == 0:
            problems.append(
                f"parity-hedge guard matched nothing in {required}, where the ADCK1/ADCK2 "
                f"comparison is made. Either it was removed, or PARITY_TOPIC_RE / "
                f"PARITY_CONTEXT_RE no longer match it and the guard is vacuous there."
            )
    return problems


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

    So a YAML surface is split at every mapping key: each summary, reason, gap_statement,
    boundary, question and so on becomes its own unit, which is the granularity a reader
    actually reasons over. Markdown keeps blank-line paragraphs. The split is a line scan
    rather than a parse, so there is no failure branch whose fallback would silently restore
    the file-level behaviour.
    """
    if name.endswith((".yaml", ".yml")):
        # Split at every mapping key, so each summary / reason / gap_statement / boundary is
        # its own unit. Done with a line scan rather than a YAML parse for two reasons:
        # the three sibling scripts in this folder are stdlib-only and RESULTS.md documents a
        # bare `python3` invocation, so pulling in PyYAML would make the documented command
        # fail on a clean interpreter; and a parse introduces a failure branch whose only
        # sane fallback is "treat the file as one blob", which is exactly the file-level
        # behaviour this function exists to abolish. No parse, no silent fallback.
        # Block scalars must be tracked, or prose inside them gets split at any line that
        # merely LOOKS like a key. Found by this file's own parity guard: the summary text
        # "...not fixable in GO: ADCK1 and ADCK2 receive SL-0173..." was cut in two at "GO:",
        # separating a claim from the clause that qualifies it two sentences later. A
        # splitter that fragments a scalar is as wrong as one that merges a whole file.
        units: list[str] = []
        cur: list[str] = []
        scalar_indent: int | None = None
        for line in text.splitlines():
            # The KEY's column, not the line's. For "- gap_statement: >-" the line indent is 0
            # but the key starts at column 2, and its sibling keys (boundary, significance,
            # provenance) also sit at column 2 - so a line-indent comparison absorbed the whole
            # entry into one ~2.4 kB unit instead of five. Same coarse-unit shape yet again.
            m_key = YAML_KEY_RE.match(line)
            indent = (
                m_key.group(0).index(m_key.group(0).lstrip("- ").lstrip()[0])
                if m_key and m_key.group(0).lstrip("- ").lstrip()
                else len(line) - len(line.lstrip())
            )
            stripped = line.strip()
            if scalar_indent is not None:
                # Inside a block scalar: anything more indented than its key belongs to it.
                if not stripped or indent > scalar_indent:
                    cur.append(line)
                    continue
                scalar_indent = None
            if YAML_KEY_RE.match(line):
                if cur:
                    units.append("\n".join(cur))
                cur = [line]
                if BLOCK_SCALAR_RE.search(line):
                    scalar_indent = indent
            else:
                cur.append(line)
        if cur:
            units.append("\n".join(cur))
        # NOTE: deliberately does NOT raise. A check that raises from inside a helper aborts
        # every later check and the self-test baseline, while the harness still prints as
        # though it ran. The under-split condition is reported by check_compartment_hedge().
        return units
    return [b for b in re.split(r"\n\s*\n", text)]


# ---------------------------------------------------------------------------------------
# THE CLASS-CLOSING INVARIANT.
#
# Four separate blocking items in this PR were the same thing: a claim about a *paralog's*
# database record, asserted in prose as established background, with nothing in the repo a
# reader could check it against. The parity framing, ADCK2's SubCell provenance, the
# supplied-vs-corroborated split, and the MitoCoP row - the last being literally the other
# half of the sentence whose first half was fixed the round before. Fixing them one at a time
# was losing to the rate of discovery.
#
# So: every cross-gene claim about a database record must be COVERED - the fact must live in
# family_census.json and be re-asserted here against the committed JSON. A prose unit that
# names a paralog together with a record token whose dimension is not in COVERAGE fails,
# which is what makes this close the class rather than patch the instance. Literature claims
# about paralogs (what COQ8A was shown to do) are out of scope: those are anchored by
# supporting_text and already checked verbatim against the cached publications.
# ---------------------------------------------------------------------------------------
PARALOGS = ("ADCK1", "ADCK2", "COQ8A", "COQ8B")
PARALOG_RE = re.compile(r"\b(ADCK1|ADCK2|COQ8A|COQ8B)\b")

# The GATE is generic, not a fixed list. RECORD_TOKENS below routes a unit to the dimension
# that covers it, but what *triggers* the requirement is any record-SHAPED token, so a claim
# in a dimension nobody thought to enumerate still fails. Getting this wrong once is the
# reason it is written this way: an earlier version keyed the gate on RECORD_TOKENS itself,
# whose keys mapped 1:1 onto the covered dimensions, so the "uncovered dimension" branch was
# unreachable for any real prose and the guard closed the enumerated dimensions, not the class.
#
# A bare GO:xxxxxxx is deliberately NOT a record signature: it names a TERM, and terms are
# discussed throughout the literature prose about what paralogs were shown to do. Evidence
# codes, GO_REF ids, ECO ids, SubCell ids, EC numbers and PANTHER node ids are record-shaped.
# The FULL GO evidence-code set, not a sample. An earlier version listed seven codes and a
# self-test probe using IEP sailed straight past the gate - the signature could not see a
# whole class of record claim. Enumerating a controlled vocabulary partially is the same
# defect as enumerating the dimensions partially, one layer down.
GO_EVIDENCE_CODES = (
    "EXP IDA IPI IMP IGI IEP HTP HDA HMP HGI HEP "
    "ISS ISO ISA ISM IGC IBA IBD IKR IRD RCA "
    "TAS NAS IC ND IEA"
).split()
RECORD_SIGNATURE_RE = re.compile(
    r"GO_REF:|ECO:\d{7}|\bEC[ =]?\d|SL-0\d|\bPTN\d|\b(" + "|".join(GO_EVIDENCE_CODES) + r")\b"
)

# There is no exemption list. One was added for a unit whose record token was ADCK5's
# own IPI, then found UNREACHABLE once routing moved to sentence level - the escape was
# described in RESULTS.md as active while no input could reach it. Restricting .py
# surfaces to prose removed the only case that motivated it, so the mechanism is gone
# rather than kept as decoration.

# record-token -> dimension name. A token in a paralog-mentioning unit demands that dimension.
RECORD_TOKENS = {
    r"\bIBA\b": "iba",
    r"PMID:34800366|MitoCoP|HTP row|GO:0005739": "mitocop_row",
    r"EC[= ]?2\.7|2\.7\.-\.-|2\.7\.11\.-": "ec",
    r"Ser/Thr-kinase keyword|Serine/threonine-protein kinase keyword|kinase keyword|keyword removal|UniProt keyword": "keyword",
    r"SL-0173|SL-0162|SUBCELLULAR LOCATION|subcellular location|mitochondrial inner membrane|Mitochondrion membrane": "subcellular",
    r"NOT\|": "negated",
    r"ECO:0000269\|PubMed:33988507|PubMed:33988507|PMID:33988507": "screen_provenance",
    r"ECO:0000269\|PubMed:(11888884|24270420|25498144)": "tag_sets",
    r"PTN\d+|PTHR43173|PAINT|SGD:S000004243|MCP2": "paint_node",
    r"GO:0004672|GO:0004674|GO:0016301|GO:0006468": "kinase_rows",
}


def _coverage(census_doc: dict, paint_text: str | None = None) -> dict[str, callable]:
    """dimension -> assertion re-derived from the COMMITTED census JSON."""
    c = census_doc["census"]
    prov = census_doc["mitochondrial_localisation_provenance"]

    def iba():
        bad = [g for g in PARALOGS if c[g]["n_iba"] == 0]
        return (
            f"prose says every paralog has an IBA row; {bad} do not" if bad else None
        )

    def mitocop():
        missing = [
            g
            for g in ("ADCK5", "ADCK1", "ADCK2")
            if not any(
                r["reference"] == "PMID:34800366" and r["evidence"] == "HTP"
                for r in c[g]["mitochondrion_go_rows"]
            )
        ]
        return (
            f"prose says ADCK5, ADCK1 and ADCK2 share the MitoCoP GO:0005739 HTP row; "
            f"{missing} do not carry it"
            if missing
            else None
        )

    def ec():
        exp = {"COQ8A": ["2.7.-.-"], "COQ8B": ["2.7.-.-"], "ADCK1": ["2.7.-.-"],
               "ADCK2": ["2.7.11.-"], "ADCK5": ["2.7.11.-"]}
        bad = {g: c[g]["ec_numbers"] for g in exp if c[g]["ec_numbers"] != exp[g]}
        return f"EC numbers changed: {bad}" if bad else None

    def keyword():
        exp = {"ADCK5": True, "ADCK1": True, "ADCK2": True, "COQ8A": False, "COQ8B": False}
        bad = {g: c[g]["has_ser_thr_kinase_keyword"] for g in exp
               if c[g]["has_ser_thr_kinase_keyword"] != exp[g]}
        return f"Ser/Thr-kinase keyword changed: {bad}" if bad else None

    def subcellular():
        if any(str(l["location"]).startswith("Mitochondrion")
               for l in c["ADCK5"]["subcellular_locations"]):
            return "ADCK5 now has a Mitochondrion SUBCELLULAR LOCATION; the request is stale"
        # EXACT, because the prose now names these strings: "COQ8A as Mitochondrion membrane,
        # single-pass, and ADCK1 as Mitochondrion". A startswith test would let a refinement
        # of either line pass green while the prose quietly became imprecise.
        for g in ("ADCK1", "ADCK2"):
            if not any(str(l["location"]) == "Mitochondrion"
                       and any(e.startswith("ECO:0000269") for e in l["evidence"])
                       for l in c[g]["subcellular_locations"]):
                return (
                    f"{g}'s experimental location is no longer exactly 'Mitochondrion': "
                    f"{[l['location'] for l in c[g]['subcellular_locations']]}"
                )
        # The review states COQ8A's location as "Mitochondrion membrane, single-pass" and
        # ADCK1's as "Mitochondrion"; assert both, since those are cross-gene record claims
        # like any other. (An earlier draft said both were "inner-mitochondrial-membrane
        # anchored" - unsupported for either: ADCK1's line is plain Mitochondrion and COQ8A's
        # says nothing about "inner". Found via the reviewer's note that a bare "anchored"
        # routing alternative was marking that sentence covered by a check which asserted
        # nothing of the kind - widening ROUTING silently shrinks what the gate reports.)
        for g in ("COQ8A", "COQ8B"):
            if not any(str(l["location"]) == "Mitochondrion membrane"
                       for l in c[g]["subcellular_locations"]):
                return (
                    f"{g}'s location is no longer exactly 'Mitochondrion membrane': "
                    f"{[l['location'] for l in c[g]['subcellular_locations']]}"
                )
        return None

    def negated():
        bad = [g for g in ("COQ8A", "COQ8B") if len(c[g]["negated_annotations"]) != 2]
        return f"prose says COQ8A and COQ8B each carry 2 NOT| rows; {bad} do not" if bad else None

    def screen():
        if prov["sole"] != ["ADCK1", "ADCK2"] or prov["absent"] != ["ADCK5"] \
                or prov["corroborating"] != ["COQ8A", "COQ8B"]:
            return f"screen provenance partition changed: {prov}"
        return None

    def tag_sets():
        # RESULTS.md pins the exact ECO:0000269 tag set per gene in a table. Bucket
        # membership alone would let a fourth COQ8A tag appear with the table left stale.
        expected = {
            "ADCK1": ["ECO:0000269|PubMed:33988507"],
            "ADCK2": ["ECO:0000269|PubMed:33988507"],
            "COQ8A": [
                "ECO:0000269|PubMed:11888884",
                "ECO:0000269|PubMed:25498144",
                "ECO:0000269|PubMed:33988507",
            ],
            "COQ8B": [
                "ECO:0000269|PubMed:24270420",
                "ECO:0000269|PubMed:33988507",
            ],
        }
        bad = {}
        for g, exp in expected.items():
            got = sorted(
                {
                    e
                    for l in c[g]["subcellular_locations"]
                    if str(l["location"]).startswith("Mitochondrion")
                    for e in l["evidence"]
                }
            )
            if got != exp:
                bad[g] = {"expected": exp, "got": got}
        return (
            f"the per-gene tag table in RESULTS.md is stale: {bad}" if bad else None
        )

    def paint_node():
        # Asserted against the committed PAINT table, not the census: PTHR43173's single
        # annotated node, its three terms and its single yeast seed are what the review's
        # PAINT question and the notes both rest on.
        # NOTE: PTHR43173-paint.tsv is SHARED repo state that this PR does not own - it is
        # regenerated by `just fetch-panther-paint`. If another branch re-fetches the family
        # and the node table changes, this gene's audit will fail. That is intended (the
        # review's PAINT claims really would need re-checking), but read such a failure as
        # "the upstream table moved", not "ADCK5's review drifted".
        # Content is injectable so the self-test never writes to the tracked table. An
        # earlier version mutated it in place and restored it, which round-tripped the line
        # endings and left the file dirty - the same hazard already fixed once for the
        # sibling-script probe.
        if paint_text is None and not PAINT_TSV.exists():
            return f"PAINT table missing: {PAINT_TSV}"
        raw = paint_text if paint_text is not None else PAINT_TSV.read_text()
        rows = [l.split("\t") for l in raw.splitlines()[1:] if l.strip()]
        nodes = {r[1] for r in rows}
        terms = sorted({r[2] for r in rows if r[1] == "PTN005148758"})
        seeds = sorted({s for r in rows if r[1] == "PTN005148758" for s in r[6].split("|")})
        if nodes != {"PTN005148758"}:
            return f"PTHR43173 no longer has exactly one annotated node: {sorted(nodes)}"
        if terms != ["GO:0005743", "GO:0007005", "GO:0055088"]:
            return f"PTN005148758's terms changed: {terms}"
        if seeds != ["SGD:S000004243"]:
            return f"PTN005148758 is no longer seeded by MCP2 alone: {seeds}"
        return None

    def kinase_rows():
        # The review states that GOA carries BOTH a NOT|enables and an enables GO:0004672 IDA
        # row for COQ8B, naming both papers. negated() only counts NOT| rows, so the positive
        # row and both references went unasserted.
        expected = {
            "COQ8B": [
                ("GO:0004672", "IDA", "NOT|enables", "PMID:27499294"),
                ("GO:0004672", "IDA", "enables", "PMID:38425362"),
            ],
            "COQ8A": [
                ("GO:0004672", "IDA", "NOT|enables", "PMID:27499294"),
                ("GO:0006468", "IDA", "NOT|involved_in", "PMID:27499294"),
            ],
        }
        # EXACT set, not a subset. Routing a claim to this dimension has to mean the claim is
        # covered; a subset check would pass a sentence describing a row the census never
        # asserted. The full sets are small and stable enough to pin.
        full = {
            "COQ8A": {
                ("GO:0004672", "IDA", "NOT|enables", "PMID:27499294"),
                ("GO:0004672", "ISS", "enables", "GO_REF:0000024"),
                ("GO:0006468", "IDA", "NOT|involved_in", "PMID:27499294"),
                ("GO:0016301", "IDA", "enables", "PMID:25498144"),
                ("GO:0016301", "IDA", "enables", "PMID:27499294"),
            },
            "COQ8B": {
                ("GO:0004672", "IDA", "NOT|enables", "PMID:27499294"),
                ("GO:0004672", "IDA", "enables", "PMID:38425362"),
                ("GO:0006468", "IDA", "NOT|involved_in", "PMID:27499294"),
            },
        }
        bad = {}
        for g, need in full.items():
            have = {
                (r["term"], r["evidence"], r["qualifier"], r["reference"])
                for r in c[g].get("kinase_rows", [])
            }
            if have != need:
                bad[g] = {"missing": sorted(need - have), "unexpected": sorted(have - need)}
        # `expected` is retained as the review-named subset, asserted implicitly by the above.
        assert all(set(v) <= full[k] for k, v in expected.items())
        if bad:
            return f"the paralogs' kinase-row sets changed: {bad}"
        if c["ADCK5"].get("kinase_rows"):
            return (
                f"ADCK5 now HAS a kinase-related GO row ({c['ADCK5']['kinase_rows']}); the "
                f"review's central finding that GOA carries none is stale"
            )
        return None

    return {
        "iba": iba, "mitocop_row": mitocop, "ec": ec, "keyword": keyword,
        "subcellular": subcellular, "negated": negated, "screen_provenance": screen,
        "tag_sets": tag_sets, "paint_node": paint_node, "kinase_rows": kinase_rows,
    }


def check_cross_gene_claims(census_doc: dict, texts: dict[str, str],
                            paint_text: str | None = None) -> list[str]:
    problems: list[str] = []
    coverage = _coverage(census_doc, paint_text)

    # 1. Every covered dimension must still hold against the committed JSON.
    for dim, fn in coverage.items():
        msg = fn()
        if msg:
            problems.append(f"cross-gene claim [{dim}]: {msg}")

    # 2. THE GATE. Any unit naming a paralog alongside a record-shaped token must route to a
    #    covered dimension. Generic by construction, so a claim in a dimension nobody
    #    enumerated fails rather than passing silently.
    triggered_by_surface: dict[str, int] = {}
    for name, text in texts.items():
        triggered_by_surface.setdefault(name, 0)
        scan = _py_prose(text) if name.endswith(".py") else text
        for unit in _paragraphs(scan, name):
            if not (PARALOG_RE.search(unit) and RECORD_SIGNATURE_RE.search(unit)):
                continue
            # NB: the vacuity counter is incremented in the SENTENCE loop below, not here.
            # A unit-level increment reported the guard exercised whenever a unit tripped the
            # pre-filter even if zero sentences routed - i.e. it could not see the gate's own
            # coverage collapse, which is the failure it exists to detect.
            # PER SENTENCE, not per unit. (Not per token: a sentence's tokens are unioned,
            # so a sentence carrying two record claims is still one decision - stated as a
            # residual limit in RESULTS.md rather than implied away.) Routing per unit meant
            # one covered token gave a
            # blanket pass to every other record claim in the same unit - and the fifth
            # instance was already in the tree because of it: the COQ8B double-GO:0004672
            # sentence tripped the gate, resolved to {negated} via its NOT| token, and sailed
            # through while the positive row and both PMIDs were unasserted. The self-test
            # "proved" the catch only because its probe was appended as its own paragraph,
            # where it carried no covered token. Each signature occurrence is now routed
            # independently.
            # Paralog and record token must occur in the SAME sentence. Carrying the
            # last-named paralog forward across sentences was tried and withdrawn: with the
            # colon no longer splitting, both in-tree claims this gate exists for already sit
            # in one sentence each, so forward-carry bought nothing and produced three false
            # positives on sentences about ADCK5's OWN evidence codes. The colon was the whole
            # bug. Anaphora that genuinely crosses a sentence boundary remains a stated
            # residual limit rather than an over-broad rule.
            for sentence in _sentences(unit):
                if not (
                    PARALOG_RE.search(sentence) and RECORD_SIGNATURE_RE.search(sentence)
                ):
                    continue
                triggered_by_surface[name] += 1
                tok = RECORD_SIGNATURE_RE.search(sentence).group()
                dims = {
                    d for pat, d in RECORD_TOKENS.items() if re.search(pat, sentence, re.I)
                }
                uncovered = {d for d in dims if d not in coverage}
                if uncovered:
                    problems.append(
                        f"{name}: cross-gene claim in dimension(s) {sorted(uncovered)}, which "
                        f"nothing in family_census.json asserts. Compute it, scope it down, "
                        f"or delete it."
                    )
                elif not dims:
                    problems.append(
                        f"{name}: a unit names a paralog alongside a record-shaped token "
                        f"({tok!r}) that matches no covered dimension. Either add a dimension "
                        f"that asserts it against a committed artifact, add a documented "
                        f"exemption, or scope the claim down. Unit starts: "
                        f"{unit.strip()[:80]!r}"
                    )
    # Per surface, not corpus-wide - third time this shape has come up in this file.
    for required in ("ADCK5-ai-review.yaml", "ADCK5-bioinformatics/RESULTS.md"):
        if triggered_by_surface.get(required, 0) == 0:
            problems.append(
                f"cross-gene guard matched nothing in {required}, so the invariant proved "
                f"nothing there. Check PARALOG_RE / RECORD_SIGNATURE_RE."
            )
    return problems


def _py_prose(text: str) -> str:
    """Comments and docstrings from a Python surface - the parts that make claims.

    Executable code is not prose: `for sym in ("ADCK1", "ADCK2")` names paralogs as string
    literals and embeds ECO ids in error-message f-strings, which the cross-gene gate read as
    an unasserted claim. Restricting to prose removes that whole class of noise without an
    exemption entry, and keeps docstrings in scope - a docstring is where one withdrawn
    phrasing actually hid.
    """
    out: list[str] = []
    in_doc = False
    for line in text.splitlines():
        s = line.strip()
        if in_doc:
            out.append(line)
            if TRIPLE_DQ in s or TRIPLE_SQ in s:
                in_doc = False
            continue
        if s.startswith(TRIPLE_DQ) or s.startswith(TRIPLE_SQ):
            out.append(line)
            body = s[3:]
            if not (body.endswith(TRIPLE_DQ) or body.endswith(TRIPLE_SQ)):
                in_doc = True
            continue
        if s.startswith("#"):
            out.append(line)
    return "\n".join(out)


def _sentences(unit: str) -> list[str]:
    """Split a unit into sentence-ish spans for per-claim routing.

    Routing per UNIT was the gap: one covered token gave a blanket pass to every other record
    claim in the same unit, and the fifth instance was already in the tree because of it.
    Per-sentence is finer and demonstrably catches that case. It is NOT per-claim: a single
    sentence mixing a covered and an uncovered record claim still passes, and that residual
    limit is stated in RESULTS.md rather than papered over. Regex cannot do better honestly.
    """
    # NOT on ":" - that was a real regression. This review's prose uses a colon to introduce
    # exactly the record claim whose subject was just named ("...the cost is on COQ8B, not on
    # ADCK5: GOA carries both..."), so splitting there severed the paralog from the token and
    # made the two claims this gate exists for INVISIBLE rather than caught. A colon almost
    # always introduces an elaboration of the same claim.
    flat = re.sub(r"\s+", " ", unit)
    return [s for s in re.split(r"(?<=[.;])\s+", flat) if s.strip()]


TRIPLE_DQ = chr(34) * 3
TRIPLE_SQ = chr(39) * 3

COARSE_UNIT_CHARS = 1500


def check_unit_granularity(texts: dict[str, str]) -> list[str]:
    """Markdown surfaces must stay finely split, or both hedge guards degrade silently.

    Runs on EVERY invocation, not only under --self-test: its YAML counterpart (a surface
    that yields <2 units) is reported by check_compartment_hedge on every run, and the
    surfaces that actually regressed were the markdown ones. A guard that only fires in the
    self-test cannot catch a regression introduced by someone editing the prose.
    """
    problems: list[str] = []

    # YAML granularity is a property of the SPLITTER, so it is guarded by exercising the
    # splitter on a fixture rather than by inspecting the real file. An inline "no unit holds
    # two sibling keys" check was written first and was UNREACHABLE - with the splitter
    # correct it can never fire, which is the read-as-coverage trap this file has hit before.
    # This probe reproduces the exact shape of the bug that shipped: a block-scalar key whose
    # siblings sit at the key's own column and were being absorbed.
    probe = (
        "- gap_statement: >-\n"
        "    text of the gap statement\n"
        "  boundary: >-\n"
        "    text of the boundary\n"
        "  status: OPEN\n"
    )
    probe_units = _paragraphs(probe, "probe.yaml")
    if len(probe_units) != 3:
        problems.append(
            f"splitter regression: a knowledge_gaps-shaped entry split into "
            f"{len(probe_units)} unit(s), expected 3 (gap_statement, boundary, status). "
            f"Sibling fields are being absorbed into the preceding block scalar, which lets "
            f"one field's qualification cover another field's claim."
        )

    for surface in ("ADCK5-notes.md", "ADCK5-bioinformatics/RESULTS.md"):
        if surface not in texts:
            problems.append(f"granularity guard: {surface} absent from the scanned surfaces")
            continue
        oversized = [
            u for u in _paragraphs(texts[surface], surface) if len(u) > COARSE_UNIT_CHARS
        ]
        if oversized:
            problems.append(
                f"{surface} has {len(oversized)} unit(s) over {COARSE_UNIT_CHARS} chars; the "
                f"hedge guards run per unit, so a coarse unit lets an unhedged claim ride "
                f"along with an unrelated hedge. First: {oversized[0].strip()[:70]!r}"
            )
    return problems


def check_compartment_hedge(texts: dict[str, str]) -> list[str]:
    """Structural guard: discussing the compartment argument obliges you to hedge it NEARBY.

    Keyed on the TOPIC, so it survives rewording of the conclusion - unlike the literal
    phrase list, which it exists to compensate for. Enforced per paragraph (with a
    one-paragraph lookahead) because the file-level version demonstrably failed to catch the
    real defect.
    """
    problems: list[str] = []
    triggered_by_surface: dict[str, int] = {}
    for name, text in texts.items():
        paras = _paragraphs(text, name)
        # A YAML surface that does not split means the invariant has silently gone
        # file-level - the bug that shipped twice. Report it; do not raise.
        if name.endswith((".yaml", ".yml")) and len(paras) < 2:
            problems.append(
                f"{name} split into {len(paras)} unit(s). A YAML review file must split per "
                f"field; one unit means the hedge invariant has become file-level again. "
                f"Check YAML_KEY_RE against the file's actual formatting."
            )
        triggered_by_surface.setdefault(name, 0)
        for i, para in enumerate(paras):
            if not (COMPARTMENT_TOPIC_RE.search(para) and COMPARTMENT_CONTEXT_RE.search(para)):
                continue
            triggered_by_surface[name] += 1
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
    # Vacuity is checked PER SURFACE, not corpus-wide. A corpus-wide counter stays non-zero
    # as long as ANY surface still discusses the topic, so the guard could go silently blind
    # on the review YAML - the surface where the annotation claims actually live - while
    # reporting itself exercised.
    for required in ("ADCK5-ai-review.yaml", "ADCK5-bioinformatics/RESULTS.md"):
        if triggered_by_surface.get(required, 0) == 0:
            problems.append(
                f"compartment-hedge guard matched nothing in {required}, where the compartment "
                f"argument is made. Either the argument was removed from that surface, or the "
                f"topic pattern no longer matches it and the guard is now vacuous there."
            )
    return problems

# Claims that must appear on at least `min_surfaces` of the prose surfaces.
REQUIRED_CLAIMS = [
    ("K147", 2),  # KxGQ lysine
    ("A209", 2),  # A-rich loop alanine
    ("D382", 2),  # DFG aspartate (cited in the suggested kinase-dead control)
    ("17 of 25", 2),
    # Load-bearing since the parity retraction: it is what makes ADCK5's missing
    # UniProt mitochondrial annotation "untested" rather than "tested and negative".
    ("absent from the library", 2),
    ("33988507", 3),
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

# A YAML mapping key, with or without a leading list dash. Used to split a review file
# into per-field units without a YAML parser.
YAML_KEY_RE = re.compile(r"^\s*(?:-\s+)?[A-Za-z_][A-Za-z0-9_]*:")
# A key introducing a block scalar (`>-`, `>`, `|`, `|-`, `|+`, `>+`), possibly with a
# trailing comment. Everything more-indented below it is scalar content, not structure.
BLOCK_SCALAR_RE = re.compile(r":\s*[|>][-+]?\s*$")


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
    problems += check_parity_hedge(all_surfaces(texts))
    problems += check_cross_gene_claims(census, all_surfaces(texts))
    problems += check_unit_granularity(all_surfaces(texts))
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
    expect_flag("a residue position drifted (A209 -> A210)", drifted, match="unrecognised residue token")

    # 2. withdrawn phrasing, plain and quote-split
    expect_flag(
        "withdrawn phrasing reappears",
        {**good, "RESULTS.md": good["RESULTS.md"] + "\n25 mitochondrial proteins\n"},
        match="withdrawn phrasing reappeared",
    )
    expect_flag(
        "withdrawn phrasing reappears with quotes inserted (bypass attempt)",
        {**good, "RESULTS.md": good["RESULTS.md"] + '\n25 "mitochondrial" proteins\n'},
        match="withdrawn phrasing reappeared",
    )

    # 3. required claim deleted from all but one surface (surface counting, not summing)
    stripped = dict(good)
    for k in list(stripped):
        if k != "RESULTS.md":
            stripped[k] = stripped[k].replace("17 of 25", "")
    # and pile extra copies into the remaining surface: a summing lint would pass here
    stripped["RESULTS.md"] = stripped["RESULTS.md"] + "\n17 of 25\n" * 5
    expect_flag("claim present 6x on ONE surface but deleted from the others", stripped,
                match="required claim")

    # 4. census drift
    bad_census = json.loads(json.dumps(census))
    bad_census["census"]["ADCK5"]["n_iba"] = 3
    expect_flag("ADCK5 gained IBA annotations", good, census=bad_census,
                match="only one")

    bad_census2 = json.loads(json.dumps(census))
    bad_census2["census"]["ADCK5"]["has_ser_thr_kinase_keyword"] = False
    expect_flag("UniProt dropped the keyword (correction request now stale)", good,
                census=bad_census2, match="Ser/Thr-kinase keyword")

    bad_census3 = json.loads(json.dumps(census))
    bad_census3["census"]["COQ8A"]["negated_annotations"] = []
    expect_flag("COQ8A lost its NOT| rows", good, census=bad_census3, match="NOT| rows")

    # 5. partner-number drift
    bad_p = json.loads(json.dumps(partner))
    bad_p["mito_interactome"]["fraction_text"] = "19 of 25"
    expect_flag("mitochondrial fraction drifted (prose still says 17 of 25)", good, partner=bad_p,
                match="mitochondrial fraction")

    bad_p2 = json.loads(json.dumps(partner))
    for k in bad_p2["orthogonal_assay_for_goa_partners"]:
        bad_p2["orthogonal_assay_for_goa_partners"][k] = True
    expect_flag("an orthogonal assay appeared for the GO:0005515 partner", good, partner=bad_p2,
                match="non-two-hybrid assay")

    bad_p3 = json.loads(json.dumps(partner))
    bad_p3["orthogonal_assay_for_goa_partners"] = {}
    expect_flag("no GOA partners in the JSON (claim would be vacuous)", good, partner=bad_p3,
                match="no GO:0005515 partners")

    # The MI-score and per-PMID sub-method checks: each must be REACHABLE, not merely
    # present. A check that can never fire reads as coverage while providing none.
    dropped_label = {
        k: v.replace("two hybrid prey pooling approach", "XXX") for k, v in good.items()
    }
    expect_flag("a sub-method label vanished from the prose", dropped_label,
                match="sub-method label")

    drifted_mi = {k: v.replace("MI score 0.67", "MI score 0.90") for k, v in good.items()}
    expect_flag("the MI score in the prose drifted from the computed one", drifted_mi,
                match="MI score")

    bad_p4 = json.loads(json.dumps(partner))
    for a in bad_p4["goa_binding_partners"].values():
        a["mi_scores"] = [0.67, 0.42]
    expect_flag(
        "IntAct now reports more than one MI score, so 'MI score 0.67 throughout' is false",
        good,
        partner=bad_p4,
        match="claims a single MI score",
    )

    bad_p5 = json.loads(json.dumps(partner))
    for a in bad_p5["goa_binding_partners"].values():
        a["methods_by_pmid"] = {}
    expect_flag("methods_by_pmid emptied (sub-method argument would be unbacked)", good,
                partner=bad_p5, match="methods_by_pmid is empty")

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
            "withdrawn phrasing planted in a sibling .py (scan must not be too narrow)", good,
            match="withdrawn phrasing reappeared",
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
    expect_flag("compartment argument discussed with every hedge removed", unhedged,
                match="compartment argument")

    # Catch by PARAPHRASE: reinstate the withdrawn conclusion in new words, no pinned literal
    # anywhere, hedges stripped. This is the exact failure that reached RESULTS.md.
    paraphrased = dict(unhedged)
    paraphrased["RESULTS.md"] = (
        unhedged["RESULTS.md"]
        + "\n\nY2H removes exactly the targeting constraint that makes the NOTCH2NLA "
        "pairing impossible in vivo.\n"
    )
    expect_flag("withdrawn claim reinstated as PARAPHRASE with no pinned literal", paraphrased,
                match="compartment argument")

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
                good, motif=empty_motif, match="residue guard is vacuous")

    # An under-splitting YAML surface must be REPORTED, not raised - a helper that raises
    # aborts every later check while the harness still prints as though it ran.
    unsplittable = {**good, "ADCK5-ai-review.yaml": "no mapping keys here at all, just prose"}
    expect_flag(
        "a YAML surface that does not split per field (invariant gone file-level)",
        unsplittable,
        match="split into 1 unit",
    )

    # Per-surface vacuity: the guard must notice if it stops matching the review YAML, even
    # though other surfaces still discuss the topic. A corpus-wide counter would not.
    no_topic_in_yaml = {**good, "ADCK5-ai-review.yaml": "summary: >-\n  nothing on topic here\n"}
    expect_flag(
        "compartment topic vanished from the review YAML while other surfaces still match",
        no_topic_in_yaml,
        match="matched nothing in ADCK5-ai-review.yaml",
    )

    # --- the parity guard, in both directions, against the REAL pre-retraction text ---
    if not PARITY_FIXTURE.exists():
        failures.append(f"parity regression fixture missing: {PARITY_FIXTURE}")
        print("  FAIL (fixture missing): parity retraction replay")
    else:
        parity_hist = PARITY_FIXTURE.read_text()
        if "SL-0173" not in parity_hist:
            failures.append("parity fixture no longer contains the contrast; replay proves nothing")
            print("  FAIL (fixture corrupted): parity retraction replay")
        else:
            expect_flag(
                "the REAL pre-retraction parity units, replayed from the frozen fixture",
                {**good, "ADCK5-notes.md": parity_hist},
                match="contrasts ADCK1/ADCK2 UniProt subcellular treatment",
            )
    expect_clean("parity claim discussed and properly qualified", good)

    # The splitter must not fragment a block scalar at prose that merely looks like a key.
    # This is how "…not fixable in GO: ADCK1 and ADCK2 receive SL-0173…" got cut in two,
    # separating a claim from its qualifying clause and producing a false positive.
    probe = (
        "existing_annotations:\n"
        "- review:\n"
        "    summary: >-\n"
        "      Something about GO: ADCK1 and ADCK2 receive SL-0173 here, and the qualifying\n"
        "      clause saying the screen library did not contain ADCK5 lives two lines later.\n"
        "    action: ACCEPT\n"
    )
    probe_units = _paragraphs(probe, "probe.yaml")
    joined = [u for u in probe_units if "SL-0173" in u]
    if len(joined) != 1 or "did not contain ADCK5" not in joined[0]:
        failures.append(
            f"splitter fragmented a block scalar at a prose colon: the SL-0173 sentence and "
            f"its qualifying clause landed in different units ({len(joined)} unit(s) matched)"
        )
        print("  FAIL: splitter fragments block scalars at prose colons")
    else:
        print("  PASS: splitter keeps a block scalar whole across prose colons")

    # --- the class-closing cross-gene invariant, one break-test per dimension ---
    import copy as _copy
    dim_muts = [
        ("ADCK1 loses its IBA row", lambda d: d["census"]["ADCK1"].__setitem__("n_iba", 0), "[iba]"),
        ("ADCK2 loses the MitoCoP row",
         lambda d: d["census"]["ADCK2"].__setitem__("mitochondrion_go_rows", []), "[mitocop_row]"),
        ("COQ8A's EC reverts to 2.7.11.-",
         lambda d: d["census"]["COQ8A"].__setitem__("ec_numbers", ["2.7.11.-"]), "[ec]"),
        ("COQ8A regains the Ser/Thr keyword",
         lambda d: d["census"]["COQ8A"].__setitem__("has_ser_thr_kinase_keyword", True), "[keyword]"),
        ("ADCK5 gains a mitochondrial SUBCELLULAR LOCATION",
         lambda d: d["census"]["ADCK5"]["subcellular_locations"].append(
             {"location": "Mitochondrion", "evidence": ["ECO:0000269|PubMed:1"]}), "[subcellular]"),
        ("COQ8B loses its NOT| rows",
         lambda d: d["census"]["COQ8B"].__setitem__("negated_annotations", []), "[negated]"),
        ("the screen-provenance partition shifts",
         lambda d: d["mitochondrial_localisation_provenance"].__setitem__("corroborating", ["COQ8A"]),
         "[screen_provenance]"),
        ("COQ8A gains a fourth localisation tag (RESULTS.md table would go stale)",
         lambda d: d["census"]["COQ8A"]["subcellular_locations"][0]["evidence"].append(
             "ECO:0000269|PubMed:99999999"), "[tag_sets]"),
    ]
    for desc, mut, marker in dim_muts:
        bad = _copy.deepcopy(census)
        mut(bad)
        expect_flag(f"cross-gene: {desc}", good, census=bad, match=marker)

    # THE CLASS-CLOSER. These are the reviewer's own predictions of what the fifth instance
    # would look like, and they must fail WITHOUT anyone adding a token first. An earlier
    # version could only be exercised by injecting a token into RECORD_TOKENS at runtime -
    # which tested "maintainer adds a token and forgets coverage", not the case the prose
    # promised. If these three ever pass, the guard has stopped closing the class.
    for probe, why in [
        (
            "ADCK1 has 8 annotations of which 4 are experimental (IDA).",
            "a new cross-gene claim about a paralog's annotation counts",
        ),
        (
            "COQ8B has three IPI rows for GO:0005515 naming distinct partners.",
            "a new cross-gene claim about a paralog's interaction rows",
        ),
        (
            "COQ8A carries an IEP row recording expression during stress.",
            "a new cross-gene claim in a dimension nobody enumerated (IEP)",
        ),
    ]:
        # NOTE: the two probes this list originally carried - about COQ8B's positive
        # GO:0004672 IDA row and its reference - now legitimately PASS, because the
        # kinase_rows dimension was added to cover exactly that claim after the reviewer
        # showed it was already in the tree and slipping through. They were replaced rather
        # than deleted so the reason is on the record.
        expect_flag(
            why,
            {**good, "ADCK5-notes.md": good["ADCK5-notes.md"] + "\n\n" + probe + "\n"},
            match="no covered dimension",
        )

    # The routed-but-uncovered branch, which is the other half of the gate.
    RECORD_TOKENS[r"ZZ_UNCOVERED_TOKEN_ZZ"] = "an_uncovered_dimension"
    try:
        expect_flag(
            "a maintainer adds a record token and forgets to add its coverage",
            {
                **good,
                "ADCK5-notes.md": good["ADCK5-notes.md"]
                + "\n\nCOQ8A ZZ_UNCOVERED_TOKEN_ZZ with an IDA row.\n",
            },
            match="an_uncovered_dimension",
        )
    finally:
        RECORD_TOKENS.pop(r"ZZ_UNCOVERED_TOKEN_ZZ", None)

    # paint_node, asserted against the committed PAINT table. Content is INJECTED, so the
    # tracked file is never written to.
    _paint = PAINT_TSV.read_text()
    _before = PAINT_TSV.stat().st_mtime_ns
    for mutated, desc, marker in [
        (_paint.replace("GO:0055088", "GO:9999999"), "the PAINT node's term set changed",
         "terms changed"),
        (_paint.replace("SGD:S000004243", "SGD:SXXXXXXXX"), "the PAINT node's seed changed",
         "seeded by MCP2"),
        (_paint.replace("PTN005148758", "PTN000000001", 1), "a second PAINT node appeared",
         "exactly one annotated node"),
    ]:
        probs = check_cross_gene_claims(census, all_surfaces(good), paint_text=mutated)
        if any(marker in p for p in probs):
            print(f"  PASS (caught): {desc}")
        else:
            failures.append(f"{desc}: paint_node guard did not fire")
            print(f"  FAIL (missed): {desc}")
    if PAINT_TSV.stat().st_mtime_ns != _before:
        failures.append("self-test touched the tracked PAINT table")
        print("  FAIL: tracked PAINT table was written to")
    else:
        print("  PASS: tracked PAINT table never written to")

    # Granularity now runs on every invocation, so break-test it there too.
    expect_flag(
        "a markdown surface coarsened into one giant unit",
        {**good, "ADCK5-notes.md": good["ADCK5-notes.md"].replace("\n\n", "\n")},
        match="over 1500 chars",
    )

    # The splitter-regression guard must be REACHABLE: swap in the pre-fix splitter (line
    # indent instead of key column) and require the guard to fire. Without this the guard
    # would be another check that can never trigger while reading as coverage.
    _orig_split = globals()["_paragraphs"]

    def _regressed(text, name=""):
        if not name.endswith((".yaml", ".yml")):
            return _orig_split(text, name)
        units, cur, si = [], [], None
        for line in text.splitlines():
            ind = len(line) - len(line.lstrip())
            s = line.strip()
            if si is not None:
                if not s or ind > si:
                    cur.append(line)
                    continue
                si = None
            if YAML_KEY_RE.match(line):
                if cur:
                    units.append("\n".join(cur))
                cur = [line]
                if BLOCK_SCALAR_RE.search(line):
                    si = ind
            else:
                cur.append(line)
        if cur:
            units.append("\n".join(cur))
        return units

    globals()["_paragraphs"] = _regressed
    try:
        probs = check_unit_granularity(all_surfaces(good))
        if any("splitter regression" in p for p in probs):
            print("  PASS (caught): the pre-fix splitter, which absorbed sibling YAML fields")
        else:
            failures.append("splitter-regression guard did not fire on the pre-fix splitter")
            print("  FAIL (missed): pre-fix splitter")
    finally:
        globals()["_paragraphs"] = _orig_split
    if globals()["_paragraphs"] is not _orig_split:
        failures.append("self-test failed to restore _paragraphs")

    # The vacuity counter, mutated at exactly the granularity of the claim being certified.
    # The existing "topic vanished" probe blanks the surface, driving BOTH the old unit-level
    # and the new sentence-level counters to zero - so it passed identically against the
    # correct and the incorrect implementation and certified nothing. This probe instead
    # constructs the discriminating case: a unit that TRIPS the pre-filter while no sentence
    # routes. Under the unit-level counter it reports the guard exercised; under the
    # sentence-level counter it reports vacuity.
    split_subject = "COQ8A is a paralog of interest. The row is IDA."
    expect_flag(
        "a unit trips the cross-gene pre-filter while no sentence routes",
        {
            **good,
            "ADCK5-ai-review.yaml": split_subject,
            "ADCK5-bioinformatics/RESULTS.md": split_subject,
        },
        match="proved nothing there",
    )

    # --- invariants about the harness itself, not about the gene ---
    # A partial `texts` dict must fall back to DISK for the surfaces it omits. Blanking them
    # would shrink the scanned corpus and turn a partial dict into a false pass.
    partial = all_surfaces({"ADCK5-notes.md": good["ADCK5-notes.md"]})
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
