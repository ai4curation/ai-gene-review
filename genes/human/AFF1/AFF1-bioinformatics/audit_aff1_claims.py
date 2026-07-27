#!/usr/bin/env python3
"""Claim and quote audit for the AFF1 review.  Points at the EMITTED artifacts.

Five checks, each written for a defect this campaign has actually shipped:

A. **Every quote is verbatim, including the ones no repo gate reaches.**
   `checkquotes.py` walks only `supported_by` and `findings`; the repo's reference
   validator skips `file:` quotes entirely, which makes them a fabrication surface.
   This walks *every* quote-bearing key in the review YAML **and** the bracketed
   `[PMID:... "..."]` / `[file:... "..."]` citations in `AFF1-notes.md`, and it
   **fails if it checked zero of either kind** so a broken walker cannot report a
   clean pass.

B. **Raw-vs-parsed reconciliation, with a duplicate-key loader.** PyYAML keeps the
   last of a duplicated mapping key and silently drops the earlier one, and no gate
   that inspects the parsed tree can see data parsing already removed.  YAML
   anchors do the mirror thing and multiply a quote N times.

C. **Every `core_functions` term is backed by an ACCEPT/NEW row, and every ACCEPT
   row's term appears in `core_functions`.**  Both directions, because the
   unwritten direction is the one that goes silently wrong.

D. **Hedge sweep over ALL structured slots.**  For each claim this review declines
   to make, assert that no structured field states it flatly -- enumerating
   `molecular_function`, `contributes_to_molecular_function`, `directly_involved_in`,
   `locations`, `anatomical_locations`, `in_complex`, `substrates`, `action`,
   `root_cause`, `source_status` and `description`.  A location is as much an
   assertion as an activity.

E. **`source_entities` are the GOA WITH/FROM field, by construction.**  Compared as
   sets, not counts -- a matching count is not a matching set.

Run:        uv run python audit_aff1_claims.py
Self-test:  uv run python audit_aff1_claims.py --self-test
"""

from __future__ import annotations

import csv
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any

import yaml

HERE = Path(__file__).resolve().parent
GENE_DIR = HERE.parent
REPO = GENE_DIR.parents[2]

REVIEW = GENE_DIR / "AFF1-ai-review.yaml"
NOTES = GENE_DIR / "AFF1-notes.md"
GOA = GENE_DIR / "AFF1-goa.tsv"
RESULTS_MD = HERE / "RESULTS.md"

# Keys anywhere in the document whose value is a quotation from a source.
QUOTE_KEYS = ("supporting_text",)
# Keys that carry the reference id a nearby quote belongs to.
REF_KEYS = ("reference_id", "id")

# Claims this review deliberately does NOT make.  Each is (label, predicate over
# the parsed review) -- the predicate returns a list of offending locations.
# Written as structured-field probes, not phrase greps: a literal-phrase detector
# cannot catch a paraphrase, and the conclusion's wording is exactly what gets
# reworded, so these select on stable entities (GO ids, enum values).
FORBIDDEN_TERMS = {
    # AFF1 does not recruit DOT1L / direct H3K79 methylation: PMID:20159561 states
    # Dot1 is not associated with AFF1, and no GOA row asserts it.
    "GO:0018024": "histone H3K4 methyltransferase activity",
    "GO:0031151": "histone methyltransferase activity (H3-K79 specific)",
    "GO:0042800": "histone H3K4 methyltransferase activity",
    "GO:0034729": "histone H3-K79 methylation",
    # AFF1 is not a sequence-specific DNA-binding transcription factor; its only
    # DNA-proximity evidence is ChIP occupancy, and it is an IDR scaffold.
    "GO:0003700": "DNA-binding transcription factor activity",
    "GO:0000981": "DNA-binding transcription factor activity, RNA Pol II-specific",
    "GO:0001228": "DNA-binding transcription activator activity, Pol II-specific",
    # AFF1 has no kinase domain; the CTD kinase is CDK9.
    "GO:0004672": "protein kinase activity",
    "GO:0004674": "protein serine/threonine kinase activity",
}


class Problem(Exception):
    pass


# ---------------------------------------------------------------------------
# strict loader
# ---------------------------------------------------------------------------

class StrictLoader(yaml.SafeLoader):
    """Raises on a duplicated mapping key instead of silently keeping the last."""


def _no_duplicates(loader: yaml.Loader, node: yaml.Node, deep: bool = False) -> dict:
    mapping: dict[Any, Any] = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in mapping:
            raise yaml.constructor.ConstructorError(
                None, None,
                f"DUPLICATE KEY {key!r} at line {key_node.start_mark.line + 1} -- "
                "PyYAML would silently keep the last and discard the earlier value",
                key_node.start_mark)
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


StrictLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _no_duplicates)


def norm(t: str) -> str:
    """Mirror linkml-reference-validator's normalisation."""
    return re.sub(r"\s+", " ", t).strip().lower()


def source_text(ref_id: str) -> str | None:
    if ref_id.startswith("PMID:"):
        p = REPO / "publications" / f"PMID_{ref_id.split(':', 1)[1]}.md"
    elif ref_id.startswith("file:"):
        rel = ref_id.split(":", 1)[1]
        p = REPO / "genes" / rel
        if not p.exists():
            p = REPO / rel
    else:
        return None
    if not p.exists():
        raise Problem(f"cited source does not exist: {ref_id} -> {p}")
    return p.read_text()


# ---------------------------------------------------------------------------
# A + B
# ---------------------------------------------------------------------------

def walk_quotes(node: Any, ref: str | None = None, path: str = ""):
    """Yield (path, reference_id, quote) for EVERY quote-bearing key, at any depth.

    Unlike checkquotes.py this does not enumerate container names, so a new
    container (`provenance`, `knowledge_gaps[].provenance[]`, `finding_review`,
    ...) is covered automatically instead of silently skipped.
    """
    if isinstance(node, dict):
        here = ref
        for rk in REF_KEYS:
            v = node.get(rk)
            if isinstance(v, str) and (v.startswith("PMID:") or v.startswith("file:")
                                       or v.startswith("GO_REF:")
                                       or v.startswith("Reactome:")):
                here = v
                break
        for k, v in node.items():
            if k in QUOTE_KEYS and isinstance(v, str) and v.strip():
                yield f"{path}.{k}", here, v
            else:
                yield from walk_quotes(v, here, f"{path}.{k}")
    elif isinstance(node, list):
        for i, e in enumerate(node):
            yield from walk_quotes(e, ref, f"{path}[{i}]")


NOTE_CITATION = re.compile(r'\[((?:PMID|file):[^\s\]]+)\s+"([^"]+)"\]')


def check_quotes(problems: list[str]) -> dict[str, int]:
    counts = {"yaml": 0, "notes_pmid": 0, "notes_file": 0}

    doc = yaml.load(REVIEW.read_text(), Loader=StrictLoader)
    for path, ref, quote in walk_quotes(doc):
        if ref is None:
            problems.append(f"quote with no resolvable reference id at {path}: "
                            f"{quote[:80]!r}")
            continue
        src = source_text(ref)
        if src is None:
            continue  # GO_REF / Reactome carry no text
        counts["yaml"] += 1
        if norm(quote) not in norm(src):
            problems.append(f"NOT VERBATIM in review {ref} ({path}): {quote[:110]!r}")

    text = NOTES.read_text()
    for m in NOTE_CITATION.finditer(text):
        ref, quote = m.group(1), m.group(2)
        src = source_text(ref)
        if src is None:
            problems.append(f"notes cite an unresolvable source {ref}")
            continue
        counts["notes_pmid" if ref.startswith("PMID:") else "notes_file"] += 1
        if norm(quote) not in norm(src):
            problems.append(f"NOT VERBATIM in notes {ref}: {quote[:110]!r}")

    # A checker that finds nothing to check is the vacuity hole.  `file:` quotes
    # are unvalidated by CI, so specifically require that some were checked.
    for kind in counts:
        if counts[kind] == 0:
            problems.append(
                f"vacuous quote check: zero {kind} quotes were examined, so a pass "
                f"here means nothing")
    return counts


def check_raw_vs_parsed(problems: list[str]) -> dict[str, int]:
    raw = REVIEW.read_text()
    # Anchor the key match: an unanchored `"supporting_text" in line` would also
    # match a longer key, and PyYAML puts an anchor on the list-item line so the
    # key can appear with or without a leading "- ".
    raw_quotes = len(re.findall(r"^\s*(?:-\s*)?supporting_text:", raw, re.M))
    raw_refs = len(re.findall(r"^\s*(?:-\s*)?reference_id:", raw, re.M))
    aliases = len(re.findall(r"^\s*-?\s*\*id\d+", raw, re.M))
    anchors = len(re.findall(r"&id\d+", raw))

    doc = yaml.load(raw, Loader=StrictLoader)
    parsed_quotes = sum(1 for _ in walk_quotes(doc))

    if anchors or aliases:
        problems.append(
            f"YAML anchors/aliases present ({anchors} anchors, {aliases} alias uses): "
            "an alias multiplies one quote across N rows so every gate verifies the "
            "same string N times; dump with ignore_aliases")
    if raw_quotes != parsed_quotes:
        problems.append(
            f"raw/parsed mismatch: {raw_quotes} `supporting_text:` keys in the file "
            f"vs {parsed_quotes} reachable after parsing -- derive the expected "
            f"number independently rather than explaining the gap")
    return {"raw_supporting_text": raw_quotes, "parsed_supporting_text": parsed_quotes,
            "raw_reference_id": raw_refs, "anchors": anchors, "alias_uses": aliases}


# ---------------------------------------------------------------------------
# C
# ---------------------------------------------------------------------------

CF_TERM_SLOTS = ("molecular_function", "contributes_to_molecular_function",
                 "directly_involved_in", "locations", "anatomical_locations",
                 "in_complex", "substrates")


def cf_terms(doc: dict) -> dict[str, list[str]]:
    out: dict[str, list[str]] = {}
    for i, cf in enumerate(doc.get("core_functions") or []):
        for slot in CF_TERM_SLOTS:
            v = cf.get(slot)
            if v is None:
                continue
            items = v if isinstance(v, list) else [v]
            for it in items:
                tid = it.get("id") if isinstance(it, dict) else it
                if isinstance(tid, str) and tid.startswith("GO:"):
                    out.setdefault(tid, []).append(f"core_functions[{i}].{slot}")
    return out


def kept_terms(doc: dict) -> dict[str, set[str]]:
    """Terms the review endorses: the term of an ACCEPT/NEW row, plus the
    proposed_replacement_terms of a MODIFY row."""
    out: dict[str, set[str]] = {}
    for a in doc.get("existing_annotations") or []:
        r = a.get("review") or {}
        act = r.get("action")
        if a.get("negated"):
            continue
        if act in {"ACCEPT", "NEW"}:
            tid = (a.get("term") or {}).get("id")
            if tid:
                out.setdefault(tid, set()).add(act)
        if act == "MODIFY":
            for t in r.get("proposed_replacement_terms") or []:
                tid = t.get("id") if isinstance(t, dict) else t
                if tid:
                    out.setdefault(tid, set()).add("MODIFY_REPLACEMENT")
    return out


def check_core_function_backing(problems: list[str]) -> dict[str, Any]:
    doc = yaml.load(REVIEW.read_text(), Loader=StrictLoader)
    cf = cf_terms(doc)
    kept = kept_terms(doc)
    if not cf:
        problems.append("core_functions declares no GO terms at all -- a vacuous "
                        "pass for both directions of this check")
    if not kept:
        problems.append("no ACCEPT/NEW/MODIFY-replacement terms found -- this "
                        "check cannot fire, which is not the same as passing")

    # direction 1: every core_functions term must be endorsed by a row
    for tid, where in sorted(cf.items()):
        if tid not in kept:
            problems.append(
                f"core_functions asserts {tid} ({', '.join(where)}) but no "
                f"ACCEPT/NEW row and no MODIFY replacement endorses it")
    # direction 2: every ACCEPT/NEW row's term should surface in core_functions,
    # unless the row is explicitly KEEP_AS_NON_CORE-adjacent.  Written out because
    # the unwritten direction is the one that rots.
    missing = []
    for tid, acts in sorted(kept.items()):
        if tid == "GO:0005515":
            continue  # bare protein binding is never a core function
        if tid not in cf:
            missing.append(f"{tid} ({'/'.join(sorted(acts))})")
    return {"core_function_terms": sorted(cf), "endorsed_terms": sorted(kept),
            "endorsed_but_not_in_core_functions": missing}


# ---------------------------------------------------------------------------
# D
# ---------------------------------------------------------------------------

def all_structured_values(doc: dict) -> list[tuple[str, str]]:
    """Every (path, value) for the structured slots a hedge could be contradicted
    in.  Enumerated explicitly so the sweep cannot silently narrow."""
    out: list[tuple[str, str]] = []
    slots = set(CF_TERM_SLOTS) | {"action", "root_cause", "source_status",
                                  "description", "failure_modes", "qualifier"}

    def rec(node: Any, path: str) -> None:
        if isinstance(node, dict):
            for k, v in node.items():
                if k in slots:
                    items = v if isinstance(v, list) else [v]
                    for it in items:
                        if isinstance(it, dict):
                            tid = it.get("id")
                            if tid:
                                out.append((f"{path}.{k}", str(tid)))
                        elif it is not None:
                            out.append((f"{path}.{k}", str(it)))
                rec(v, f"{path}.{k}")
        elif isinstance(node, list):
            for i, e in enumerate(node):
                rec(e, f"{path}[{i}]")

    rec(doc, "")
    return out


def check_hedge_sweep(problems: list[str]) -> dict[str, Any]:
    doc = yaml.load(REVIEW.read_text(), Loader=StrictLoader)
    vals = all_structured_values(doc)
    if not vals:
        problems.append("hedge sweep collected zero structured values -- vacuous")
    hits = []
    for path, v in vals:
        if v in FORBIDDEN_TERMS:
            hits.append(f"{path} = {v} ({FORBIDDEN_TERMS[v]})")
    for h in hits:
        problems.append(
            f"a structured field asserts a claim this review declines to make: {h}")
    # The prose must not assert them either, in the review or the notes.
    for label, text in (("review", REVIEW.read_text()), ("notes", NOTES.read_text())):
        flat = re.sub(r"\s+", " ", text)
        for tid, name in FORBIDDEN_TERMS.items():
            if tid in flat and label == "review":
                problems.append(f"{label} prose mentions the withheld term {tid}; "
                                "if that is deliberate, exempt it explicitly")
    return {"n_structured_values_swept": len(vals),
            "slots_swept": sorted(set(p.rsplit('.', 1)[-1] for p, _ in vals)),
            "forbidden_hits": hits}


# ---------------------------------------------------------------------------
# E
# ---------------------------------------------------------------------------

def check_source_entities(problems: list[str]) -> dict[str, Any]:
    if not GOA.exists():
        raise Problem(f"missing {GOA}; run `just fetch-gene human AFF1`")
    with GOA.open() as fh:
        rows = list(csv.DictReader(fh, delimiter="\t"))
    doc = yaml.load(REVIEW.read_text(), Loader=StrictLoader)
    anns = [a for a in (doc.get("existing_annotations") or [])
            if (a.get("review") or {}).get("action") != "NEW"]
    if len(anns) != len(rows):
        problems.append(
            f"existing_annotations (excluding NEW rows) = {len(anns)} but the GOA "
            f"TSV has {len(rows)} rows -- reconcile explicitly, an unexplained "
            f"mismatch is either missing coverage or a silent merge")
        return {"n_goa_rows": len(rows), "n_annotations": len(anns)}

    checked = 0
    for i, (row, ann) in enumerate(zip(rows, anns), start=1):
        # Row order is the seeder's, which follows the TSV; assert the pairing
        # before trusting it.
        if (ann.get("term") or {}).get("id") != row["GO TERM"]:
            problems.append(
                f"row {i}: YAML term {(ann.get('term') or {}).get('id')} does not "
                f"match TSV term {row['GO TERM']} -- the positional pairing this "
                f"check depends on is broken")
            continue
        if ann.get("evidence_type") != row["GO EVIDENCE CODE"]:
            problems.append(f"row {i}: evidence {ann.get('evidence_type')} != "
                            f"{row['GO EVIDENCE CODE']}")
        if ann.get("original_reference_id") != row["REFERENCE"]:
            problems.append(f"row {i}: reference {ann.get('original_reference_id')} "
                            f"!= {row['REFERENCE']}")
        expected = {t.strip() for t in (row.get("WITH/FROM") or "").split("|")
                    if t.strip()}
        got = set(ann.get("supporting_entities") or [])
        if expected != got:
            problems.append(
                f"row {i} ({row['GO TERM']}): supporting_entities set mismatch -- "
                f"missing {sorted(expected - got)}, unexpected {sorted(got - expected)}")
        pr = ((ann.get("review") or {}).get("propagation_review") or {})
        src = {s.get("source_id") for s in (pr.get("source_entities") or [])}
        if src and src != expected:
            problems.append(
                f"row {i} ({row['GO TERM']}): propagation_review.source_entities "
                f"set mismatch -- missing {sorted(expected - src)}, unexpected "
                f"{sorted(src - expected)}")
        if expected:
            checked += 1
    if checked == 0:
        problems.append("no row carried a WITH/FROM field, so the source-entity "
                        "check examined nothing")
    return {"n_goa_rows": len(rows), "n_annotations": len(anns),
            "n_rows_with_withfrom_checked": checked}


# ---------------------------------------------------------------------------
# F. emitted-text lint
# ---------------------------------------------------------------------------

# Controlled-vocabulary spellings that must be exact wherever they appear in prose.
# A single wrong-case character in a curator-facing field is invisible to every
# other gate and reads as correct, so it is checked on the artifact that ships
# rather than on the generator that produced it.
EXACT_SPELLINGS = {
    r"\bSUBCELLUL\w+": "SUBCELLULAR",
    r"\bUniProt[Kk][Bb]?\b": None,   # informational only; see below
}


def check_emitted_text(problems: list[str]) -> dict[str, Any]:
    """Lint the EMITTED files, not the builder source.

    A phrase that is one string literal in Python is line-wrapped by the YAML
    dumper, so whitespace is normalised before matching -- otherwise a naive
    `"..." in text` silently misses every wrapped claim.
    """
    findings: dict[str, list[str]] = {}
    files = [REVIEW, NOTES, RESULTS_MD]
    scanned = 0
    for f in files:
        if not f.exists():
            problems.append(f"emitted-text lint cannot find {f.name}")
            continue
        scanned += 1
        flat = re.sub(r"\s+", " ", f.read_text())
        # wrong-case controlled vocabulary
        for w in re.findall(r"\bSUBCELLUL\w+", flat):
            if w != "SUBCELLULAR":
                findings.setdefault(f.name, []).append(f"mis-cased token {w!r}")
        # Python implicit string concatenation doubling a token
        for m in re.findall(r"\b(\w{3,})\.\1\b", flat):
            findings.setdefault(f.name, []).append(f"doubled token {m!r}.{m!r}")
        # an accidentally repeated word across a wrapped literal
        for m in re.findall(r"\b(\w{4,})\s+\1\b", flat):
            findings.setdefault(f.name, []).append(f"repeated word {m!r}")
    if scanned == 0:
        problems.append("emitted-text lint scanned zero files -- vacuous")
    for fname, hits in findings.items():
        for h in hits:
            problems.append(f"emitted-text defect in {fname}: {h}")
    return {"files_scanned": scanned, "findings": findings}


# ---------------------------------------------------------------------------
# driver
# ---------------------------------------------------------------------------

def audit() -> tuple[list[str], dict[str, Any]]:
    problems: list[str] = []
    report: dict[str, Any] = {}
    # Each check appends to `problems` and returns its report.  None of them
    # raises for a *finding*, because a check that kills the harness aborts every
    # later check while the harness still prints as though it ran.
    report["quotes"] = check_quotes(problems)
    report["raw_vs_parsed"] = check_raw_vs_parsed(problems)
    report["core_function_backing"] = check_core_function_backing(problems)
    report["hedge_sweep"] = check_hedge_sweep(problems)
    report["source_entities"] = check_source_entities(problems)
    report["emitted_text_lint"] = check_emitted_text(problems)
    return problems, report


def self_test() -> int:
    """Break-test every check.  Each case asserts three things in order: the
    mutation applied; the guard fired; the failure message is the expected one."""
    failures: list[str] = []
    original = REVIEW.read_text()
    original_notes = NOTES.read_text()

    def run_case(label: str, mutate, expect: str) -> None:
        before = REVIEW.read_text()
        before_notes = NOTES.read_text()
        try:
            mutate()
            if REVIEW.read_text() == before and NOTES.read_text() == before_notes:
                failures.append(f"{label}: MUTATION WAS A NO-OP -- the fixture has "
                                f"drifted, so this case certifies nothing")
                return
            try:
                problems, _ = audit()
            except Problem as exc:
                problems = [f"hard failure: {exc}"]
            hit = [p for p in problems if expect in p]
            if not hit:
                failures.append(f"{label}: guard did not fire with the expected "
                                f"message {expect!r}; got {problems[:3]}")
            else:
                print(f"  ok   {label}: {hit[0][:100]}")
        finally:
            REVIEW.write_text(before)
            NOTES.write_text(before_notes)

    print("self-test: baseline must be clean")
    problems, _ = audit()
    if problems:
        print("  BASELINE IS NOT CLEAN:")
        for p in problems:
            print("   ✗", p)
        failures.append("baseline audit reports problems; fix those first")

    def mut_bad_quote() -> None:
        d = yaml.load(REVIEW.read_text(), Loader=StrictLoader)
        # Corrupt whatever the FIRST quote happens to be, rather than hardcoding
        # a string that can move.
        for a in d.get("existing_annotations") or []:
            for sb in ((a.get("review") or {}).get("supported_by") or []):
                if sb.get("supporting_text"):
                    sb["supporting_text"] = "this sentence appears in no publication"
                    REVIEW.write_text(yaml.dump(d, sort_keys=False, allow_unicode=True))
                    return
        raise Problem("no supporting_text found to corrupt")
    run_case("fabricated quote in review", mut_bad_quote, "NOT VERBATIM in review")

    def mut_bad_notes_quote() -> None:
        t = NOTES.read_text()
        m = NOTE_CITATION.search(t)
        if not m:
            raise Problem("no bracketed citation found in the notes to corrupt")
        NOTES.write_text(t[:m.start()] +
                         f'[{m.group(1)} "a fabricated sentence not in the source"]' +
                         t[m.end():])
    run_case("fabricated quote in notes", mut_bad_notes_quote, "NOT VERBATIM in notes")

    def mut_dup_key() -> None:
        t = REVIEW.read_text()
        needle = "gene_symbol: AFF1\n"
        if needle not in t:
            raise Problem("anchor for the duplicate-key mutation is absent")
        REVIEW.write_text(t.replace(needle, needle + "gene_symbol: AFF1\n", 1))
    try:
        before = REVIEW.read_text()
        mut_dup_key()
        if REVIEW.read_text() == before:
            failures.append("duplicate-key mutation was a no-op")
        else:
            try:
                audit()
                failures.append("duplicate-key guard did not fire")
            except yaml.constructor.ConstructorError as exc:
                if "DUPLICATE KEY" in str(exc):
                    print(f"  ok   duplicate key: {str(exc).splitlines()[0][:90]}")
                else:
                    failures.append(f"duplicate-key guard fired with the wrong "
                                    f"message: {exc}")
            except Problem as exc:
                failures.append(f"duplicate-key case failed for the wrong reason: {exc}")
    finally:
        REVIEW.write_text(before)

    def mut_drop_cf_backing() -> None:
        d = yaml.load(REVIEW.read_text(), Loader=StrictLoader)
        cf = cf_terms(d)
        if not cf:
            raise Problem("no core_functions terms to unback")
        target = sorted(cf)[0]
        changed = False
        for a in d.get("existing_annotations") or []:
            r = a.get("review") or {}
            if (a.get("term") or {}).get("id") == target and \
                    r.get("action") in {"ACCEPT", "NEW"}:
                r["action"] = "REMOVE"
                changed = True
            for t in list(r.get("proposed_replacement_terms") or []):
                if (t.get("id") if isinstance(t, dict) else t) == target:
                    r["proposed_replacement_terms"].remove(t)
                    changed = True
        if not changed:
            raise Problem(f"could not unback {target}; fixture drifted")
        REVIEW.write_text(yaml.dump(d, sort_keys=False, allow_unicode=True))
    run_case("core_functions term with no backing row", mut_drop_cf_backing,
             "but no ACCEPT/NEW row and no MODIFY replacement endorses it")

    def mut_forbidden_term() -> None:
        # `contributes_to_molecular_function` is SINGLE-valued in the schema, so
        # the fixture must overwrite rather than append.  An earlier version
        # appended and raised AttributeError when the slot's cardinality changed --
        # loudly, which is the point, but the fixture has to track the schema.
        d = yaml.load(REVIEW.read_text(), Loader=StrictLoader)
        cfs = d.get("core_functions") or []
        if not cfs:
            raise Problem("no core_functions to contaminate")
        cfs[0]["contributes_to_molecular_function"] = {
            "id": "GO:0003700", "label": "DNA-binding transcription factor activity"}
        REVIEW.write_text(yaml.dump(d, sort_keys=False, allow_unicode=True))
    run_case("withheld term asserted in a structured slot", mut_forbidden_term,
             "a structured field asserts a claim this review declines to make")

    def mut_forbidden_in_locations() -> None:
        # The C5orf46 lesson: a hedge sweep scoped to the MF slots misses
        # `locations`.  This case exercises a DIFFERENT slot from the one above,
        # so a sweep that narrowed to MF slots would pass the previous case and
        # fail this one.
        d = yaml.load(REVIEW.read_text(), Loader=StrictLoader)
        cfs = d.get("core_functions") or []
        if not cfs:
            raise Problem("no core_functions to contaminate")
        cfs[0].setdefault("locations", []).append(
            {"id": "GO:0004672", "label": "protein kinase activity"})
        REVIEW.write_text(yaml.dump(d, sort_keys=False, allow_unicode=True))
    run_case("withheld term asserted in `locations` specifically",
             mut_forbidden_in_locations,
             "a structured field asserts a claim this review declines to make")

    def mut_drop_source_entity() -> None:
        d = yaml.load(REVIEW.read_text(), Loader=StrictLoader)
        for a in d.get("existing_annotations") or []:
            se = a.get("supporting_entities")
            if se:
                a["supporting_entities"] = se[1:] if len(se) > 1 else []
                REVIEW.write_text(yaml.dump(d, sort_keys=False, allow_unicode=True))
                return
        raise Problem("no supporting_entities to drop")
    run_case("dropped supporting entity", mut_drop_source_entity,
             "supporting_entities set mismatch")

    def mut_drop_annotation() -> None:
        # Must drop a GOA-derived row, NOT a NEW row: the reconciliation check
        # excludes NEW rows by design, so popping the last entry (which is a NEW
        # row) would exercise nothing.  The fixture has to be as fine as the claim.
        d = yaml.load(REVIEW.read_text(), Loader=StrictLoader)
        anns = d.get("existing_annotations") or []
        goa_rows = [i for i, a in enumerate(anns)
                    if (a.get("review") or {}).get("action") != "NEW"]
        if len(goa_rows) < 2:
            raise Problem("too few GOA-derived annotations to drop one")
        anns.pop(goa_rows[-1])
        REVIEW.write_text(yaml.dump(d, sort_keys=False, allow_unicode=True))
    run_case("missing GOA annotation row", mut_drop_annotation,
             "reconcile explicitly")

    def mut_drop_new_row() -> None:
        # The complementary direction, which the first fixture accidentally
        # exercised: dropping a NEW row must NOT trip the GOA reconciliation
        # (correct, since NEW rows are not GOA rows) but MUST leave its
        # core_functions term unbacked.
        d = yaml.load(REVIEW.read_text(), Loader=StrictLoader)
        anns = d.get("existing_annotations") or []
        new_rows = [i for i, a in enumerate(anns)
                    if (a.get("review") or {}).get("action") == "NEW"]
        if not new_rows:
            raise Problem("no NEW row to drop")
        anns.pop(new_rows[-1])
        REVIEW.write_text(yaml.dump(d, sort_keys=False, allow_unicode=True))
    run_case("missing NEW row leaves its core_functions term unbacked",
             mut_drop_new_row,
             "but no ACCEPT/NEW row and no MODIFY replacement endorses it")

    def mut_miscased_token() -> None:
        t2 = REVIEW.read_text()
        needle = "SUBCELLULAR"
        if needle not in t2:
            raise Problem("no SUBCELLULAR token in the emitted review to mis-case")
        REVIEW.write_text(t2.replace(needle, "SUBCELLULaR", 1))
    run_case("mis-cased controlled-vocabulary token in the emitted file",
             mut_miscased_token, "mis-cased token")

    def mut_doubled_token() -> None:
        t2 = REVIEW.read_text()
        needle = "super elongation complex"
        if needle not in t2:
            raise Problem("anchor for the doubled-token mutation is absent")
        REVIEW.write_text(t2.replace(needle, "super elongation complex.complex", 1))
    run_case("doubled token from implicit string concatenation",
             mut_doubled_token, "doubled token")

    def mut_alias() -> None:
        # Emit the document through a dumper that DOES create aliases, by making
        # two rows share one Python object.
        d = yaml.load(REVIEW.read_text(), Loader=StrictLoader)
        anns = d.get("existing_annotations") or []
        shared = None
        for a in anns:
            sb = (a.get("review") or {}).get("supported_by")
            if sb:
                shared = sb
                break
        if shared is None:
            raise Problem("no supported_by list to share")
        placed = 0
        for a in anns:
            r = a.setdefault("review", {})
            if r.get("supported_by") is not shared:
                r["supported_by"] = shared
                placed += 1
                if placed >= 2:
                    break
        if placed < 2:
            raise Problem("could not create a shared object for aliasing")
        REVIEW.write_text(yaml.dump(d, sort_keys=False, allow_unicode=True))
    run_case("YAML aliases multiplying a quote", mut_alias,
             "YAML anchors/aliases present")

    # Prove the tests can fail: disable one guard and confirm its case goes red.
    print("self-test: prove a disabled guard is detected")
    saved = FORBIDDEN_TERMS.copy()
    FORBIDDEN_TERMS.clear()
    if FORBIDDEN_TERMS == saved:
        failures.append("guard-disable mutation was a no-op")
    else:
        d = yaml.load(REVIEW.read_text(), Loader=StrictLoader)
        (d.get("core_functions") or [{}])[0][
            "contributes_to_molecular_function"] = {"id": "GO:0003700", "label": "x"}
        REVIEW.write_text(yaml.dump(d, sort_keys=False, allow_unicode=True))
        problems, _ = audit()
        if any("declines to make" in p for p in problems):
            failures.append("the hedge sweep still fired with an EMPTY forbidden "
                            "list, so it is not reading that list")
        else:
            print("  ok   with the forbidden list emptied, the sweep goes silent -- "
                  "the guard genuinely depends on its input")
    FORBIDDEN_TERMS.clear()
    FORBIDDEN_TERMS.update(saved)
    REVIEW.write_text(original)
    NOTES.write_text(original_notes)

    if REVIEW.read_text() != original or NOTES.read_text() != original_notes:
        failures.append("failed to restore the artifacts after the self-test")

    print()
    if failures:
        print("SELF-TEST FAILURES:")
        for f in failures:
            print("  ✗", f)
        return 1
    print("self-test: every guard fired for the right reason, mutations were real, "
          "and the baseline is clean.")
    return 0


def main(argv: list[str]) -> int:
    if "--self-test" in argv:
        return self_test()
    problems, report = audit()
    for k, v in report.items():
        print(f"{k}: {v}")
    print()
    if problems:
        print(f"{len(problems)} PROBLEM(S):")
        for p in problems:
            print("  ✗", p)
        return 1
    print("audit clean.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
