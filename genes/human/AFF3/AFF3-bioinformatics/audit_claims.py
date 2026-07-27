#!/usr/bin/env python3
"""Local gate for the AFF3 review. Walks the EMITTED YAML, not a generator.

Closes gaps the repo's own checks are known to have (campaign brief):

  A. Duplicate mapping keys. PyYAML keeps the LAST occurrence of a duplicated key and
     discards the earlier one silently, so data can be gone before any gate that walks
     the parsed tree runs. Loaded here with a strict loader that raises.
  B. Raw-vs-parsed reconciliation of quote-bearing keys, which is the only signal a
     duplicate key or a YAML alias gives you.
  C. No YAML anchors/aliases: an alias MULTIPLIES a quote on parse, so every gate
     verifies the same string N times and reports N successes.
  D. `knowledge_gaps[].provenance[]` quotes, which `checkquotes.py` does not walk.
  E. Every `file:` quote verified by exact substring against the real file, and every
     UniProt `file:` quote additionally required to lie on ONE physical line. CI does
     not check `file:` quotes at all, so this is the only gate on a fabrication surface.
  F. Both directions of core_functions backing: every core_functions term is backed by a
     kept/NEW row (or a MODIFY's replacement term), and every ACCEPT/NEW row's term
     appears in core_functions unless it is on the documented exemption list.
  G. Prose-vs-action agreement: no review block's prose may name a DIFFERENT action for
     itself. Attributed cross-references to another row's action are legitimate and are
     deliberately exempted.
  H. Withdrawn-claim guards, for the three claims this review retracted:
       - the wrong-way-round GO:0030674 / GO:0005515 ancestry claim (phrase-shaped, with
         the negated form explicitly exempted and that exemption break-tested);
       - the hand-counted CDK9 IntAct figure, guarded STRUCTURALLY by checking any stated
         record/publication/method count against intact_partners.json rather than by
         pinning a literal phrase, and break-tested against the version that actually
         shipped (`git show HEAD:...`) rather than only against a synthetic mutation.
         The narration exemption is OFF by default and switched on only by
         `audit_sibling_surfaces()`, so the review YAML is checked unconditionally --
         round 3 applied it everywhere and thereby un-guarded the YAML's own
         correction-announcing sentence, which round 4 caught;
       - the "donors disagree in sign" premise, with a PER-OCCURRENCE narration exemption.
         The one-shot repair script's exemption was file-scoped, which made it blind to two
         surviving instances inside the very file it exempted, so the check moved here to
         run on every audit.

LIMITATION, stated rather than implied: check G and the first and third parts of H match on
sentence shape and fixed phrases. They cannot catch a paraphrase. When a claim is withdrawn,
every prose surface still needs re-reading by hand -- and the low-salience ones (a
reference_review note, a source_entities comment, a script docstring, a notes bullet) are
where a retracted claim actually survives; all four of those happened here. The IntAct part
of H does not have that limitation, because it compares numbers to a computed artifact, which
is why the numeric retraction could be guarded structurally and the other two could not.

Usage:
    uv run python genes/human/AFF3/AFF3-bioinformatics/audit_claims.py
    uv run python genes/human/AFF3/AFF3-bioinformatics/audit_claims.py --self-test
"""

from __future__ import annotations

import copy
import json
import re
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]
REVIEW = HERE.parent / "AFF3-ai-review.yaml"
GOA = HERE.parent / "AFF3-goa.tsv"

# Terms legitimately annotated but deliberately NOT core functions, each with a reason.
# An enumerated exemption list with a stated reason per case, not a size threshold.
NON_CORE_EXEMPT = {
    "GO:0050877": "kept as non-core: organ-system process, retained on human genetics",
    "GO:0035116": "kept as non-core: downstream developmental role",
    "GO:0001822": "proposed as non-core: downstream developmental role",
    "GO:0021795": "proposed as non-core: downstream developmental role",
    "GO:0010468": "accepted as a redundant ancestor of the GO:0006355 core row",
    "GO:0006354": "the MODIFY source term; its replacement GO:0006368 is the core term",
}

# The claim was written the wrong way round on the first pass and term_relations.py
# caught it. It must not come back -- but the CORRECTED, negated statement is the whole
# point of documenting the retraction, so the guard must fire on the affirmative form
# and stay silent on the negated one. The gap between the two ids therefore excludes
# any negation token. Both directions are break-tested; an exemption nobody tests is
# how a guard gets discredited by its first false positive.
_NO_NEG = r"(?:(?!\bnot\b|\bn't\b|\bnever\b)[^.])"
WITHDRAWN_PATTERNS = [
    re.compile(rf"GO:0030674{_NO_NEG}{{0,90}}(?:descendant of|is a child of|sits under)"
               rf"{_NO_NEG}{{0,30}}GO:0005515", re.I),
    re.compile(rf"GO:0030674{_NO_NEG}{{0,90}}refinement of protein binding", re.I),
]

# Second retraction, guarded STRUCTURALLY rather than by phrase pin. The hand-counted
# claim was "CDK9 in five records across four distinct publications and four distinct
# methods with a MI score of 0.73"; every one of those four numbers was wrong. A literal
# phrase pin would be defeated by the next rewording, so instead any prose that states
# CDK9's record/publication/method counts is checked AGAINST intact_partners.json. Word
# forms are matched as well as digits, because a number spelled as a word evades a digit
# grep (the AEBP2 lesson).
INTACT_JSON = HERE / "intact_partners.json"
WORD_NUM = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6,
            "seven": 7, "eight": 8, "nine": 9, "ten": 10}
CDK9_COUNT_RE = re.compile(
    r"CDK9 in (?P<rec>\d+|[a-z]+) records across (?P<pub>\d+|[a-z]+) distinct "
    r"publications and\s+(?P<meth>\d+|[a-z]+) distinct methods", re.I)


def _as_int(tok: str) -> int | None:
    return int(tok) if tok.isdigit() else WORD_NUM.get(tok.lower())


# Third retraction, and the one that survived a whole round on two low-salience surfaces (a
# reference_review note and a source_entities comment) because `fix_sign_claim.py`'s
# narration exemption was FILE-scoped: exempting AFF3-ai-review.yaml wholesale made the
# re-grep blind to every unnarrated instance inside it. The check therefore lives here now,
# runs on every audit, and the exemption is PER-OCCURRENCE -- a sentence asserting the
# retracted premise passes only if the surrounding window marks it as retracted.
SIGN_RE = re.compile(r"[^.]*disagree[sd]? in \*?sign\*?[^.]*\.", re.I)

# A retracted claim must be quotable in three legitimate contexts: narrating its own
# retraction, serving as a find-and-replace ANCHOR in a repair script, and serving as a
# PATTERN or fixture in the guard that detects it. Forbidding those would make the guard
# unable to coexist with its own implementation -- and a guard that forbids legitimate
# practice gets worked around rather than obeyed.
#
# The exemption stays PER-OCCURRENCE (a window around each match), not per-file. That
# distinction is the whole point: a file-scoped exemption is what let two instances survive
# inside the file it exempted, which is guard-defeat mode "an exemption coarser than the
# thing it exempts". Both directions are break-tested.
#
# ROUND 4: the vocabulary is SPLIT, because a single set was the same mode one level over --
# coarser in surface scope. Two problems it caused:
#   * `guard` and `premise` are ordinary words in this document, so a future unnarrated sign
#     claim written near either would have been exempt on a PROSE surface.
#   * the code-shaped tokens exist only to let repair scripts hold find anchors and let this
#     file hold fixtures; they have no business exempting anything in the review YAML.
# So the code-shaped set applies only on `.py` surfaces.
NARRATED_PROSE_RE = re.compile(
    r"retract|wrong|earlier draft|earlier version|earlier wording|misread|misreading|"
    r"refuted|was false|is actually|hand-counted", re.I)
NARRATED_CODE_RE = re.compile(
    r"anchor|pattern|fixture|guard|break-test|surviving|still assert|premise|"
    r"ACCEPTED, both fixed|failures\.append|startswith|finditer|re\.compile", re.I)


def _narrated(window: str, code_context: bool) -> bool:
    """Is this occurrence a narration, or (on a .py surface) an anchor/pattern/fixture?"""
    if NARRATED_PROSE_RE.search(window):
        return True
    return bool(code_context and NARRATED_CODE_RE.search(window))


def check_sign_claim(flat: str, code_context: bool = False) -> list[str]:
    """Every 'donors disagree in sign' sentence must be narrated, anchored or patterned.

    The narration exemption DOES apply on the review YAML here, unlike the count guard: the
    YAML is where this review narrates its own retraction, so forbidding it there would
    forbid the document from recording what it withdrew.
    """
    out = []
    for m in SIGN_RE.finditer(flat):
        window = flat[max(0, m.start() - 260): m.end() + 260]
        if not _narrated(window, code_context):
            out.append(
                f"H: unnarrated 'donors disagree in sign' claim (retracted in round 2, and "
                f"GO:0032786 is POSITIVE): {m.group(0).strip()[:150]!r}"
            )
    return out


def check_intact_counts(flat: str, allow_narrated: bool = False,
                        code_context: bool = False) -> list[str]:
    """Assert every stated CDK9 count matches the computed one.

    `allow_narrated` defaults to FALSE, and that default is the point. Round 4 caught the
    exemption being applied on the review YAML, where it is not needed and where it silently
    un-guarded the sentence at the GO:0032783 reason -- the counts are stated ~170 characters
    before "the hand-counted version of them was wrong", so that occurrence became exempt and
    the numbers could have been reverted there with the audit still passing. On the one file
    the guard exists for, at the sentence announcing the correction.

    Verified before restoring the default: neither of the YAML's two count statements quotes
    the retracted numbers, so nothing on that surface needs the exemption. Only the sibling
    surfaces do -- `fix_intact_counts.py`'s find anchors and this file's own fixtures -- and
    `audit_sibling_surfaces()` passes it in explicitly.
    """
    if not INTACT_JSON.exists():
        return [f"H: {INTACT_JSON.name} missing -- cannot check the IntAct counts, which "
                f"is a loud failure rather than a silent skip"]
    p = json.loads(INTACT_JSON.read_text())["partners"]["P50750"]
    want = (p["records"], p["n_publications"], p["n_methods"])
    out = []
    n = 0
    for m in CDK9_COUNT_RE.finditer(flat):
        n += 1
        got = tuple(_as_int(m.group(k)) for k in ("rec", "pub", "meth"))
        # Per-occurrence anchor/fixture exemption, applied ONLY where the caller asks for it
        # (the sibling sweep). Off by default, so the review YAML is fully guarded.
        window = flat[max(0, m.start() - 260): m.end() + 260]
        if got != want and allow_narrated and _narrated(window, code_context):
            continue
        if got != want:
            out.append(
                f"H: retracted IntAct count restated: prose says CDK9 = {got} "
                f"(records, publications, methods) but intact_partners.json computes "
                f"{want}: {m.group(0)!r}"
            )
    if n == 0:
        out.append("H: no CDK9 count sentence found to check -- the guard would pass "
                   "vacuously, so this is reported rather than ignored")
    return out

ACTION_WORDS = {
    "ACCEPT": ["accepted", "accept"],
    "KEEP_AS_NON_CORE": ["kept as non-core", "keep as non-core"],
    "REMOVE": ["removed", "remove"],
    "MODIFY": ["modified", "modify"],
    "MARK_AS_OVER_ANNOTATED": ["over-annotated"],
    "NEW": ["proposed"],
}
# Attributed cross-references to another row's action are legitimate and useful; a guard
# that forbade them would be worked around rather than obeyed.
ATTRIBUTED = re.compile(
    r"(AFF1|AFF4|sibling|merged|the other|that one|this review|elsewhere|review)\b",
    re.I,
)


class StrictLoader(yaml.SafeLoader):
    """Rejects duplicate mapping keys instead of silently keeping the last one."""


def _no_dupes(loader, node, deep=False):
    mapping = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in mapping:
            raise yaml.YAMLError(
                f"duplicate mapping key {key!r} at line {key_node.start_mark.line + 1}"
            )
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


StrictLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _no_dupes
)


def norm(t: str) -> str:
    return re.sub(r"\s+", " ", t).strip()


def walk_quotes(node, path=""):
    """Yield (path, reference_id, supporting_text) for every quote-bearing key.

    Covers supported_by, findings AND knowledge_gaps[].provenance -- the last of which
    checkquotes.py does not walk.
    """
    if isinstance(node, dict):
        for k, v in node.items():
            if k in ("supported_by", "provenance") and isinstance(v, list):
                for i, e in enumerate(v):
                    if isinstance(e, dict) and e.get("supporting_text"):
                        yield (f"{path}.{k}[{i}]", e.get("reference_id"),
                               e["supporting_text"])
            elif k == "findings" and isinstance(v, list):
                for i, e in enumerate(v):
                    if isinstance(e, dict) and e.get("supporting_text"):
                        yield (f"{path}.findings[{i}]", node.get("id"),
                               e["supporting_text"])
            else:
                yield from walk_quotes(v, f"{path}.{k}")
    elif isinstance(node, list):
        for i, e in enumerate(node):
            yield from walk_quotes(e, f"{path}[{i}]")


def source_path(ref_id: str) -> Path | None:
    if ref_id.startswith("PMID:"):
        return REPO / "publications" / f"PMID_{ref_id.split(':', 1)[1]}.md"
    if ref_id.startswith("file:"):
        rel = ref_id.split(":", 1)[1]
        p = REPO / "genes" / rel
        return p if p.exists() else REPO / rel
    return None


def audit(text: str) -> list[str]:
    problems: list[str] = []

    # --- A. duplicate mapping keys -------------------------------------------------
    try:
        doc = yaml.load(text, Loader=StrictLoader)
    except yaml.YAMLError as exc:
        return [f"A: strict load failed: {exc}"]

    # --- C. no anchors/aliases -----------------------------------------------------
    anchors = re.findall(r"(?<![\w])&id\d+", text)
    aliases = re.findall(r"(?<![\w])\*id\d+", text)
    if anchors or aliases:
        problems.append(
            f"C: YAML anchors/aliases present ({len(anchors)} anchors, {len(aliases)} "
            f"aliases) -- an alias multiplies a quote on parse so every gate verifies "
            f"the same string N times"
        )

    quotes = list(walk_quotes(doc))

    # --- B. raw vs parsed reconciliation -------------------------------------------
    # Anchor the key match: `reference_id:` is a substring of `original_reference_id:`.
    raw_refs = len(re.findall(r"^\s*(?:-\s*)?reference_id:", text, re.M))
    if raw_refs != len(quotes):
        # Only quote-bearing entries are walked, so count raw entries WITH a
        # supporting_text sibling instead of assuming every reference_id has one.
        raw_with_text = len(re.findall(
            r"^\s*(?:-\s*)?reference_id:.*?\n(?:\s+.*\n)*?\s+supporting_text:",
            text, re.M))
        if raw_with_text != len(quotes):
            problems.append(
                f"B: raw-vs-parsed mismatch: {raw_with_text} raw reference_id entries "
                f"with a supporting_text, {len(quotes)} parsed. Investigate rather than "
                f"reconciling -- a gap here is the bug report."
            )

    # --- D + E. every quote verified ------------------------------------------------
    checked = 0
    for path, ref, txt in quotes:
        p = source_path(ref or "")
        if p is None:
            continue  # GO_REF / Reactome carry no text
        if not p.exists():
            problems.append(f"E: {path} cites {ref} but {p} does not exist")
            continue
        body = p.read_text()
        if norm(txt) not in norm(body):
            problems.append(f"E: {path} quote NOT verbatim in {ref}: {txt[:90]!r}")
            continue
        checked += 1
        if ref.startswith("file:") and ref.endswith("-uniprot.txt"):
            # A UniProt quote crossing a `CC       ` continuation is broken even though
            # whitespace normalisation makes it look fine.
            if not any(norm(txt) == norm(line) or norm(txt) in norm(line)
                       for line in body.splitlines()):
                problems.append(
                    f"E: {path} UniProt quote spans more than one physical line: "
                    f"{txt[:90]!r}"
                )
    if checked == 0:
        problems.append("E: checked ZERO quotes -- a checker that finds nothing to "
                        "check is reporting coverage it does not have")

    # --- F. core_functions backing, BOTH directions ---------------------------------
    kept_actions = {"ACCEPT", "KEEP_AS_NON_CORE", "NEW"}
    row_terms: dict[str, str] = {}
    replacement_terms: set[str] = set()
    for a in doc.get("existing_annotations") or []:
        act = ((a.get("review") or {}).get("action")) or ""
        tid = (a.get("term") or {}).get("id")
        if tid and act in kept_actions:
            row_terms[tid] = act
        for r in ((a.get("review") or {}).get("proposed_replacement_terms") or []):
            if r.get("id"):
                replacement_terms.add(r["id"])
    backed = set(row_terms) | replacement_terms

    cf_terms: set[str] = set()
    cfs = doc.get("core_functions") or []
    if not cfs:
        problems.append("F: core_functions is empty -- fail loudly rather than pass "
                        "vacuously")
    for cf in cfs:
        for slot in ("molecular_function", "contributes_to_molecular_function",
                     "in_complex"):
            t = cf.get(slot)
            if isinstance(t, dict) and t.get("id"):
                cf_terms.add(t["id"])
        for slot in ("directly_involved_in", "locations", "anatomical_locations",
                     "substrates"):
            for t in cf.get(slot) or []:
                if isinstance(t, dict) and t.get("id"):
                    cf_terms.add(t["id"])
    if not cf_terms:
        problems.append("F: no terms found in core_functions -- vacuous pass")

    for t in sorted(cf_terms - backed):
        problems.append(
            f"F: core_functions term {t} is not backed by any ACCEPT/KEEP_AS_NON_CORE/"
            f"NEW row or MODIFY replacement"
        )
    for t in sorted(set(row_terms) - cf_terms - set(NON_CORE_EXEMPT)):
        problems.append(
            f"F: row term {t} has action {row_terms[t]} but is absent from "
            f"core_functions and is not on the exemption list"
        )

    # --- G. prose names its own action ---------------------------------------------
    for i, a in enumerate(doc.get("existing_annotations") or []):
        rv = a.get("review") or {}
        act = rv.get("action")
        if not act:
            problems.append(f"G: existing_annotations[{i}] has no action -- fail loudly")
            continue
        prose = norm(f"{rv.get('summary', '')} {rv.get('reason', '')}")
        opener = norm(rv.get("summary", "")).split(".")[0].lower()
        for other, words in ACTION_WORDS.items():
            if other == act:
                continue
            for w in words:
                if w in opener and not ATTRIBUTED.search(opener):
                    problems.append(
                        f"G: existing_annotations[{i}] action is {act} but its summary "
                        f"opens by naming {other} ({w!r}): {opener[:110]!r}"
                    )
        if not prose:
            problems.append(f"G: existing_annotations[{i}] has empty summary and reason")

    # --- H. withdrawn claim ---------------------------------------------------------
    flat = norm(text)
    for pat in WITHDRAWN_PATTERNS:
        for m in pat.finditer(flat):
            problems.append(
                f"H: withdrawn GO:0030674/GO:0005515 ancestry claim reappeared: "
                f"{flat[max(0, m.start() - 60):m.end() + 60]!r}"
            )
    problems.extend(check_intact_counts(flat))
    problems.extend(check_sign_claim(flat))

    # --- row count vs the GOA TSV ---------------------------------------------------
    if not GOA.exists():
        problems.append(f"missing {GOA} -- run: just fetch-gene human AFF3")
    else:
        lines = [ln for ln in GOA.read_text().splitlines()[1:] if ln.strip()]
        n_goa = len(set(lines))
        n_reviewed = sum(1 for a in doc.get("existing_annotations") or []
                         if ((a.get("review") or {}).get("action")) != "NEW")
        if n_goa != n_reviewed:
            problems.append(
                f"GOA reconciliation: {n_goa} distinct GOA rows but {n_reviewed} "
                f"non-NEW existing_annotations entries"
            )
    return problems


def self_test() -> int:
    """Every break-test asserts three things in order: the mutation applied, the guard
    fired, and the failure message is the expected one."""
    text = REVIEW.read_text()
    doc = yaml.load(text, Loader=StrictLoader)
    failures = []

    def expect(name: str, mutated: str, marker: str, changed: bool = True) -> None:
        if changed and mutated == text:
            failures.append(f"{name}: MUTATION DID NOT CHANGE THE DOCUMENT")
            return
        probs = audit(mutated)
        hit = [p for p in probs if p.startswith(marker)]
        if not hit:
            failures.append(f"{name}: guard did NOT fire (expected {marker!r}); "
                            f"got {probs[:2]}")
        else:
            print(f"  ok  {name}: {hit[0][:130]}")

    # A: duplicate mapping key
    dup = text.replace("gene_symbol: AFF3", "gene_symbol: AFF3\ngene_symbol: AFF3", 1)
    expect("A duplicate key", dup, "A:")

    # C: an alias
    alias = text.replace("core_functions:", "core_functions: &id001", 1)
    expect("C anchor present", alias, "C:")

    # E: a fabricated quote
    fake = text.replace(
        "In vitro-translated LAF-4 was able to bind strongly to double-stranded DNA",
        "LAF-4 was shown to be a sequence-specific transcription factor in vivo", 1)
    expect("E fabricated quote", fake, "E:")

    # E: a file: quote that does not exist in the target
    badfile = text.replace(
        "IPR007797 AND IPR043640 AND taxon Eukaryota  ->  GO:0005634",
        "IPR999999 AND IPR000000 AND taxon Bacteria  ->  GO:0005634", 1)
    expect("E bad file quote", badfile, "E:")

    # F: drop a core_functions term's backing row action so the term is unbacked.
    # Mutate whatever the first location happens to be, then assert it changed.
    cf_drop = text.replace("    id: GO:0016607\n    label: nuclear speck\n",
                           "    id: GO:0000001\n    label: made up\n", 1)
    expect("F unbacked core_functions term", cf_drop, "F:")

    # F, other direction: a kept row whose term is absent from core_functions and not
    # exempt. Asserted on the SPECIFIC message, because the first direction also emits
    # an "F:" problem and a bare prefix match would let this direction pass on the
    # wrong finding -- a mutation coarser than the claim it certifies.
    other_dir = text.replace(
        "- term:\n    id: GO:0001822\n    label: kidney development\n",
        "- term:\n    id: GO:0000002\n    label: invented unrepresented row\n", 1)
    expect("F unrepresented kept row", other_dir,
           "F: row term GO:0000002 has action NEW")

    # E, single-physical-line rule for UniProt quotes. This span IS present in the file
    # after whitespace normalisation (the `CC` continuation tokens are included, so the
    # verbatim check passes) but crosses two physical lines, which is exactly the
    # silent-breakage case the rule exists for.
    crossline = text.replace(
        "'CC   -!- SUBCELLULAR LOCATION: Nucleus.'",
        "'CC   -!- FUNCTION: Putative transcription activator that may function in CC       lymphoid development'",
        1)
    expect("E UniProt quote crosses a continuation line", crossline,
           "E: .existing_annotations[5].review.supported_by[1] UniProt quote spans")

    # G: prose naming the wrong action, in the summary opener
    wrong_action = text.replace(
        "Removed. The sole supporting paper is a pharmacogenetic",
        "Accepted. The sole supporting paper is a pharmacogenetic", 1)
    expect("G prose-vs-action", wrong_action, "G:")

    # H: the withdrawn ancestry claim, affirmative form -> must fire
    withdrawn = text.replace(
        "GO:0030674 was verified NOT to be a descendant of GO:0005515",
        "GO:0030674 is a descendant of GO:0005515", 1)
    expect("H withdrawn claim", withdrawn, "H:")

    # H, the other direction: the CORRECTED negated form must NOT fire, otherwise the
    # guard forbids documenting its own retraction and gets worked around. Assert the
    # phrase is present first, so the check cannot pass because the target drifted.
    negated = "GO:0030674 was verified NOT to be a descendant of GO:0005515"
    if negated not in text:
        failures.append("H negated form: target phrase absent, so this direction is "
                        "vacuous")
    elif any(p.startswith("H:") for p in audit(text)):
        failures.append("H negated form: guard fired on the corrected, negated "
                        "statement -- it forbids documenting the retraction")
    else:
        print("  ok  H negated form: guard correctly silent on the corrected statement")

    # H, second retraction: the hand-counted IntAct figure, run against THE DEFECT THAT
    # ACTUALLY SHIPPED rather than a mutation I invented. Git holds the wrong version.
    import subprocess
    shipped = subprocess.run(
        ["git", "show", "HEAD:genes/human/AFF3/AFF3-ai-review.yaml"],
        capture_output=True, text=True, cwd=REPO,
    )
    if shipped.returncode != 0:
        failures.append("H shipped IntAct count: could not read HEAD version from git, "
                        "so this direction is vacuous")
    elif "four distinct publications and four" not in shipped.stdout:
        # After this fix is committed, HEAD no longer holds the defect; fall back to a
        # synthetic mutation but say which path was taken rather than passing silently.
        # Pick an occurrence whose window is NOT narrated, and assert that before
        # mutating: otherwise the per-occurrence exemption legitimately suppresses the
        # synthetic mutation and the direction fails for the wrong reason -- which is
        # exactly what happened the first time this fallback ran.
        # The RAW anchor must belong to the UN-NARRATED occurrence. There are two CDK9
        # count sentences; the first sits inside a window that explains the retraction and
        # is exempt by design, so mutating it fails for the wrong reason. This anchor is
        # unique to the second, and the raw/flat distinction matters because the phrase is
        # line-wrapped differently at the two sites.
        flat_now = norm(text)
        targets = [m for m in CDK9_COUNT_RE.finditer(flat_now)
                   if not NARRATED_PROSE_RE.search(
                       flat_now[max(0, m.start() - 260): m.end() + 260])]
        anchor = "5 distinct publications and 3 distinct methods ("
        n_anchor = text.count(anchor)
        if not targets:
            failures.append("H IntAct count: every occurrence sits in a narrated window, so "
                            "no synthetic mutation can exercise the guard here -- say so "
                            "rather than passing")
        elif n_anchor != 1:
            failures.append(f"H IntAct count: raw anchor found {n_anchor} times, expected 1; "
                            f"this direction would be vacuous or ambiguous")
        else:
            recount = text.replace(
                anchor, "4 distinct publications and 3 distinct methods (", 1)
            expect("H retracted IntAct count (synthetic; HEAD is already fixed)",
                   recount, "H: retracted IntAct count restated")
    else:
        probs = audit(shipped.stdout)
        hit = [p for p in probs if p.startswith("H: retracted IntAct count restated")]
        if not hit:
            failures.append("H shipped IntAct count: the guard does NOT fire on the "
                            f"version that actually shipped; got {probs[:2]}")
        else:
            print(f"  ok  H shipped IntAct count (run against HEAD): {hit[0][:150]}")

    # H, the direction round 4 asked for and that would have caught round 3's regression:
    # mutating the counts at the NARRATED occurrence must still fire on the review YAML,
    # because `allow_narrated` is False there. Before the fix this passed silently -- the
    # exemption reached the one file the guard exists for. Assert the target's window IS
    # narrated first, so the direction cannot pass by accidentally hitting the other site.
    nar_anchor = "records CDK9 in 6 records across 5 distinct publications and"
    n_nar = text.count(nar_anchor)
    if n_nar != 1:
        failures.append(f"H narrated-occurrence coverage: anchor found {n_nar} times, "
                        f"expected 1; this direction would be vacuous")
    else:
        flat_chk = norm(text)
        m = next((m for m in CDK9_COUNT_RE.finditer(flat_chk)
                  if NARRATED_PROSE_RE.search(
                      flat_chk[max(0, m.start() - 260): m.end() + 260])), None)
        if m is None:
            failures.append("H narrated-occurrence coverage: no narrated occurrence exists, "
                            "so this direction cannot exercise the default")
        else:
            mutated = text.replace(
                nar_anchor, "records CDK9 in 5 records across 4 distinct publications and", 1)
            expect("H narrated occurrence is STILL guarded on the review YAML",
                   mutated, "H: retracted IntAct count restated")

    # And the mirror: the sibling sweep must still tolerate that same shape on a .py surface,
    # or the coexistence fix from round 3 is undone.
    if any(p.startswith("H: retracted IntAct count restated")
           for p in audit_sibling_surfaces()):
        failures.append("H anchor tolerance: the sweep fires on a repair script's find "
                        "anchors, which would forbid the guard from coexisting with its own "
                        "implementation")
    else:
        print("  ok  H anchor tolerance: sweep still silent on .py find anchors and fixtures")

    # H, third retraction: an unnarrated sign-disagreement sentence must fire. Run against
    # THE DEFECT THAT ACTUALLY SHIPPED - the two instances the round-1 commit left standing -
    # rather than a synthetic mutation, and fall back to a synthetic one only once HEAD is
    # clean, saying which path was taken.
    shipped2 = subprocess.run(
        ["git", "show", "2bf0d3d5e:genes/human/AFF3/AFF3-ai-review.yaml"],
        capture_output=True, text=True, cwd=REPO,
    )
    if shipped2.returncode == 0 and "donors disagree in sign" in shipped2.stdout:
        probs = audit(shipped2.stdout)
        hit = [p for p in probs if p.startswith("H: unnarrated 'donors disagree in sign'")]
        if not hit:
            failures.append("H shipped sign claim: guard does NOT fire on 2bf0d3d5e, the "
                            f"commit that shipped the defect; got {probs[:2]}")
        else:
            print(f"  ok  H shipped sign claim (run against 2bf0d3d5e): {hit[0][:150]}")
    else:
        inject = text.replace(
            "reason is the recipient rather than the donors.",
            "reason is the recipient rather than the donors, who disagree in sign.", 1)
        expect("H sign claim (synthetic; 2bf0d3d5e unavailable)", inject,
               "H: unnarrated 'donors disagree in sign'")

    # H, narration exemption for the sign claim must NOT fire on the retracted forms that
    # remain in the document by design.
    if any(p.startswith("H: unnarrated 'donors disagree in sign'") for p in audit(text)):
        failures.append("H sign narration: guard fires on the current file, whose remaining "
                        "instances are all explicitly marked as retracted")
    else:
        print("  ok  H sign narration: guard silent on the narrated retractions")

    # H, vacuity direction: if the CDK9 count sentence disappears entirely the guard must
    # SAY so rather than pass. This is the fifth vacuous-pass shape in the campaign.
    #
    # NOTE the mutation operates on the RAW text while the guard runs over the
    # whitespace-NORMALISED text, so it cannot be done with CDK9_COUNT_RE itself -- the
    # pattern spans a YAML line wrap in the raw file and matches only after folding. That
    # is the detector-and-mutator-must-share-a-representation trap; the first version of
    # this direction fell into it and passed nothing.
    anchor = "records CDK9 in 6 records across"
    n_anchor = text.count(anchor)
    if n_anchor != 2:
        failures.append(f"H vacuity: anchor found {n_anchor} times, expected 2 -- the "
                        f"direction would be vacuous")
    else:
        stripped = text.replace(anchor, "records CDK9 as an interactor across")
        expect("H vacuity", stripped, "H: no CDK9 count sentence found")

    # GOA reconciliation
    dropped_row = re.sub(
        r"- term:\n    id: GO:0035116\n    label: embryonic hindlimb morphogenesis\n",
        "- term:\n    id: GO:0035116\n    label: embryonic hindlimb morphogenesis\n"
        "  retired: false\n", text, count=1)
    # that one does not change the count; instead mark a non-NEW row as NEW
    recount = text.replace("    action: REMOVE", "    action: NEW", 1)
    expect("GOA reconciliation", recount, "GOA reconciliation")

    # Sibling-surface sweep, both directions. This is round 3's point: the two prose guards
    # were scoped to the review YAML while the folder-wide sweep lived in a one-shot script,
    # so the notes, RESULTS.md and the scripts had no standing guard.
    notes = (HERE.parent / "AFF3-notes.md").read_text()
    injected = notes.replace(
        "## Process",
        "## Process\n\nThe GO:0006355 row is kept unsigned because its donors disagree in "
        "sign.\n", 1)
    assert injected != notes, "sibling-sweep mutation did not change the document"
    probs = audit_sibling_surfaces({"AFF3-notes.md": injected})
    hit = [p for p in probs if p.startswith("H: unnarrated 'donors disagree in sign'")
           and "AFF3-notes.md" in p]
    if not hit:
        failures.append("sibling sweep: an unnarrated sign claim injected into the NOTES did "
                        f"not fire; got {probs[:2]}")
    else:
        print(f"  ok  sibling sweep fires on a non-YAML surface: {hit[0][:120]}")

    # ...and the other direction: the anchors and patterns that legitimately quote the
    # retracted claims must stay silent, or the guard cannot coexist with its own repair
    # scripts and would be worked around rather than obeyed.
    clean = audit_sibling_surfaces()
    if clean:
        failures.append(f"sibling sweep: fires on the unmutated folder, whose remaining "
                        f"occurrences are all anchors, patterns or narrated history: {clean}")
    else:
        print("  ok  sibling sweep silent on anchors, patterns and narrated history")

    # Happy path must be clean -- a check can be wrong about success as easily as
    # about failure.
    baseline = audit(text) + audit_sibling_surfaces()
    if baseline:
        failures.append(f"HAPPY PATH: audit reports {len(baseline)} problem(s) on the "
                        f"unmutated tree: {baseline}")
    else:
        print("  ok  happy path clean")

    if failures:
        for f in failures:
            print(f"  FAIL {f}")
        return 1
    print(f"\nself-test: all break-tests fired, happy path clean "
          f"({len(doc['existing_annotations'])} annotations)")
    return 0


def audit_sibling_surfaces(override: dict[str, str] | None = None) -> list[str]:
    """Run the two prose guards over EVERY surface in the gene folder, not just the YAML.

    Round 3's point, and it is the right one: `check_intact_counts` and `check_sign_claim`
    were scoped to the review YAML while the folder-wide sweep lived inside a one-shot repair
    script, so the notes, RESULTS.md and the scripts had no STANDING guard -- which is exactly
    how the docstring and the PIP4K2A bullet survived a round. The sweep now lives here and
    runs on every audit.

    The CDK9-count guard's vacuity branch is deliberately suppressed per file: most surfaces
    legitimately do not state the counts, and requiring each one to would make the check fire
    everywhere. The vacuity condition is still enforced, once, against the review YAML.
    """
    problems: list[str] = []
    scanned = 0
    for p in sorted(HERE.parent.rglob("*")):
        if not p.is_file() or p.suffix not in {".md", ".yaml", ".py"}:
            continue
        if p == REVIEW:
            continue  # covered by the main audit, vacuity branch included
        raw = (override or {}).get(p.name, p.read_text(errors="ignore"))
        flat = norm(raw)
        scanned += 1
        code = p.suffix == ".py"
        for prob in check_sign_claim(flat, code_context=code):
            problems.append(f"{prob}  [in {p.name}]")
        for prob in check_intact_counts(flat, allow_narrated=True, code_context=code):
            if prob.startswith("H: no CDK9 count sentence found"):
                continue  # not every surface must state the counts
            problems.append(f"{prob}  [in {p.name}]")
    if scanned == 0:
        problems.append("H: sibling-surface sweep scanned ZERO files -- a checker that finds "
                        "nothing to check is reporting coverage it does not have")
    return problems


def main() -> int:
    if not REVIEW.exists():
        raise SystemExit(f"FATAL: missing {REVIEW}")
    if "--self-test" in sys.argv:
        return self_test()
    probs = audit(REVIEW.read_text()) + audit_sibling_surfaces()
    for p in probs:
        print(f"PROBLEM {p}")
    print(f"\n{len(probs)} problem(s)")
    return 1 if probs else 0


if __name__ == "__main__":
    sys.exit(main())
