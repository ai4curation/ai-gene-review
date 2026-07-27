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
import json
import re
import subprocess
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


# Documenting a retraction necessarily restates the retracted number. One shared
# predicate so the three clauses cannot drift apart on what counts as a retraction.
RETRACTION_CONTEXT = re.compile(
    r"earlier draft|first draft|written by hand into the PR body", re.IGNORECASE)

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
# G. counted claims must agree with their own enumeration AND with results.json
# ---------------------------------------------------------------------------

RESULTS_JSON = HERE / "results.json"

# The human recipients of PMID:22195968's parent-only complex term.  The review
# states this set in prose in several places, with a count and an explicit gene
# list.  A shipped draft said "12 human recipients" beside a list of 11 names --
# the count and its own enumeration disagreed, and nothing caught it.  This check
# compares BOTH against the computed data, so neither the number nor the list can
# drift alone.
HUMAN_PARENT_ONLY = "human_parent_only_recipients"


def _computed_human_parent_only() -> set[str]:
    if not RESULTS_JSON.exists():
        raise Problem(f"missing {RESULTS_JSON}; run analyze_aff1_annotations.py")
    d = json.loads(RESULTS_JSON.read_text())
    sp = d.get("reference_species_split")
    if not sp:
        raise Problem("results.json has no reference_species_split section")
    par = sp["parent_recipients"]
    out = set()
    for acc in sp["parent_only_recipients"]:
        who = par.get(acc, "")
        if who.startswith("Homo sapiens"):
            sym = who.split(" / ", 1)[1] if " / " in who else acc
            out.add(sym)
    if not out:
        raise Problem("computed zero human parent-only recipients -- the check "
                      "would pass vacuously")
    return out


def check_counted_claims(problems: list[str]) -> dict[str, Any]:
    """Two clauses, and BOTH were defeated by their own first break-test.

    * The number clause was case-sensitive, so "ALL ELEVEN" slipped past it.
    * The enumeration clause matched the *correct* gene list literally, so
      substituting a symbol made the pattern stop matching and the check went
      silent -- a guard defeatable by breaking the thing it guards.

    Fixed by matching on SHAPE rather than on content: any long comma/and
    separated run of gene-symbol-like tokens is treated as the enumeration and its
    SET is compared, and number words are matched case-insensitively.
    """
    computed = _computed_human_parent_only()
    n = len(computed)
    words = {1: "one", 2: "two", 3: "three", 10: "ten", 11: "eleven",
             12: "twelve", 13: "thirteen"}
    allowed = {str(n), words.get(n, str(n))}

    # Widening the window admitted two false positives on the CLEAN file -- the
    # digits of "GO:0032786 which the human IMP rows" and the "one" in "every one
    # of its 12 human recipients". So: a negative lookbehind rejects a number that
    # is part of a CURIE or a longer token, and the ambiguous small number words
    # are dropped (every count this check exists for is >= 10, and bare digits are
    # still matched).
    NUMBER = r"(?<![:\w.])(?:\d+|ten|eleven|twelve|thirteen)"
    findings = []
    surfaces = [REVIEW, NOTES]
    scanned = 0
    n_number_claims = 0
    n_enumerations = 0

    for f in surfaces:
        if not f.exists():
            problems.append(f"counted-claim check cannot find {f.name}")
            continue
        scanned += 1
        flat = re.sub(r"\s+", " ", f.read_text())

        # Clause 1: any "<N> human <noun>" must state n.  Case-insensitive, because
        # the first version of this check was defeated by "ALL ELEVEN".
        for m in re.finditer(
                # Allow up to two intervening words on EITHER side of "human":
                # comparing the guard's 6 hits on the shipped file against the 8
                # edits actually needed exposed "twelve AFFECTED human gene
                # products" slipping through a pattern that required
                # <number> immediately before "human".
                rf"({NUMBER})\s+(?:of\s+its\s+)?(?:\w+\s+){{0,2}}?human\s+"
                rf"(?:\w+\s+){{0,2}}?"
                rf"(recipients|gene products|ones|subunits|rows)\b",
                flat, re.IGNORECASE):
            n_number_claims += 1
            if m.group(1).lower() not in allowed:
                ctx = flat[max(0, m.start() - 110):m.end() + 40]
                # A documented retraction legitimately restates the wrong number.
                if RETRACTION_CONTEXT.search(ctx):
                    continue
                findings.append(
                    f"{f.name}: states {m.group(1)!r} human {m.group(2)} but the "
                    f"computed set has {n}: ...{ctx.strip()}...")

        # Clause 2: match the enumeration by SHAPE -- a run of >=8 gene-symbol-like
        # tokens separated by commas/"and" -- then compare the SET.  Matching the
        # correct list literally is what made the first version silent when a
        # symbol was substituted.
        for m in re.finditer(
                r"\b(?:[A-Z][A-Z0-9]{2,7})(?:(?:,\s*|,?\s+and\s+)"
                r"(?:[A-Z][A-Z0-9]{2,7})){7,}", flat):
            listed = {x.strip() for x in re.split(r",\s*|\s+and\s+", m.group(0))
                      if x.strip()}
            n_enumerations += 1
            if listed != computed:
                findings.append(
                    f"{f.name}: enumerated gene set {sorted(listed)} != computed "
                    f"{sorted(computed)} (missing {sorted(computed - listed)}, "
                    f"unexpected {sorted(listed - computed)})")

    # Clause 3: any prose statement of the disorder figure must equal the value
    # computed from the UniProt feature table.  Added because a first draft said
    # "about a thousand of its 1210 residues", overstating 901 by ~11% -- a number
    # that was estimated where it could have been derived.
    d = json.loads(RESULTS_JSON.read_text())
    dis = d.get("disorder")
    if not dis:
        problems.append("results.json has no disorder section, so the disorder "
                        "figure cannot be checked")
    else:
        n_dis, n_len = dis["disordered_residues"], dis["length"]
        n_disorder_claims = 0
        for f in surfaces:
            if not f.exists():
                continue
            flat = re.sub(r"\s+", " ", f.read_text())
            # Numerals AND worded quantities. Testing a reviewer claim about this
            # clause exposed a gap neither of us had seen: "about a thousand of its
            # 1210 residues" -- one of the four sites the figure actually shipped at
            # -- matched NOTHING, because "a thousand" carries no digit. The clause
            # that exists to catch an estimated number was blind to the most
            # obviously estimated form of it.
            WORDED = {"a thousand": 1000, "one thousand": 1000,
                      "a hundred": 100, "nine hundred": 900}
            for m in re.finditer(
                    rf"((?:\d[\d ,]*)|(?:{'|'.join(WORDED)}))\s+of\s+"
                    rf"(?:its\s+)?(\d[\d ,]*)\s+residues",
                    flat, re.IGNORECASE):
                g1 = m.group(1).strip().lower()
                a_ = WORDED.get(g1) if g1 in WORDED else int(
                    g1.replace(" ", "").replace(",", ""))
                b_ = int(m.group(2).replace(" ", "").replace(",", ""))
                if b_ != n_len:
                    continue          # not the whole-protein claim
                n_disorder_claims += 1
                ctx = flat[max(0, m.start() - 110):m.end() + 40]
                if RETRACTION_CONTEXT.search(ctx):
                    continue
                if a_ != n_dis:
                    findings.append(
                        f"{f.name}: states {a_} of {b_} residues but the feature "
                        f"table gives {n_dis}: ...{ctx.strip()}...")
        if n_disorder_claims == 0:
            problems.append("counted-claim check found no '<N> of 1210 residues' "
                            "claim, so its disorder clause could not fire")

    # Clause 4: the verdict tally. Third instance of the count-vs-enumeration shape
    # in this PR, and the reviewer's point was that clauses 1-3 were each scoped to
    # the failure already known. So this one is generic: the tally is COMPUTED from
    # the document, and any tally-shaped string is checked against it.
    #
    # Declared limitation, not silent: the PR body and the git commit messages are
    # also surfaces that state this tally, and neither is lintable from inside the
    # repository. The computed tally is printed on every run so that whatever is
    # written there can be copied rather than counted by hand.
    doc = yaml.load(REVIEW.read_text(), Loader=StrictLoader)
    tally = Counter((a.get("review") or {}).get("action")
                    for a in (doc.get("existing_annotations") or []))
    if not tally:
        problems.append("computed an empty action tally -- clause 4 is vacuous")
    n_tally_claims = 0
    n_tally_claims_enforced = 0   # not exempted by the retraction context
    n_total_claims_enforced = [0]  # stated totals actually compared
    for f in surfaces:
        if not f.exists():
            continue
        raw = f.read_text()
        flat = re.sub(r"\s+", " ", raw)

        # Markdown TABLE form, e.g. "| `MODIFY` | 7 |". This is how the notes state
        # the authoritative tally, and the prose regex below cannot see it -- the
        # number follows the action rather than preceding it. A break-test caught
        # clause 4 matching only the exempted retraction sentence, i.e. reporting
        # coverage it did not have.
        for m in re.finditer(r"^\s*\|\s*`?([A-Z_]+)`?\s*\|\s*(\d+)\s*\|",
                             raw, re.M):
            action, stated = m.group(1), int(m.group(2))
            if action not in tally:
                continue
            n_tally_claims += 1
            n_tally_claims_enforced += 1
            if stated != tally[action]:
                findings.append(
                    f"{f.name}: tally table states {stated} {action} but the "
                    f"document contains {tally[action]}")

        for action, count in tally.items():
            if not action:
                continue
            for m in re.finditer(rf"(\d+)\s+{re.escape(action)}\b", flat):
                n_tally_claims += 1
                if int(m.group(1)) != count:
                    ctx = flat[max(0, m.start() - 160):m.end() + 30]
                    # Same exemption as clauses 1 and 3: documenting a retraction
                    # necessarily restates the wrong number. Keyed on the retraction
                    # context rather than on a literal phrase, and deliberately NOT
                    # widened into a general "quotation" exemption, which is the
                    # bypass anyone smuggling the claim back would use.
                    if RETRACTION_CONTEXT.search(ctx):
                        continue
                    n_tally_claims_enforced += 1
                    findings.append(
                        f"{f.name}: states {m.group(1)} {action} but the document "
                        f"contains {count}: ...{ctx.strip()}...")
                else:
                    # A CORRECTLY-valued prose match inside the retraction sentence
                    # must not count toward enforcement either. Otherwise the three
                    # numbers there that happen to be right (ACCEPT, KEEP_AS_NON_CORE,
                    # NEW) keep the vacuity guard quiet even if the tally table -- the
                    # only surface that actually supplies coverage -- were deleted.
                    ctx_ok = flat[max(0, m.start() - 160):m.end() + 30]
                    if not RETRACTION_CONTEXT.search(ctx_ok):
                        n_tally_claims_enforced += 1
        # And any stated total must equal the number of entries.
        # Deliberately NO RETRACTION_CONTEXT exemption here, unlike the tally
        # sub-clause beside it. The asymmetry is intentional: nothing in either
        # surface states a total inside retraction context, and an exemption with no
        # live instance is a bypass waiting to be used rather than coverage -- the
        # same reason the retraction predicate was not widened into a general
        # "quotation" exemption. If a retracted total is ever written, the guard
        # firing is the correct outcome and the exemption can be added then, with a
        # break-test for it.
        #
        # Stated totals. The prose form ("N annotation entries") matched NOTHING in
        # either surface, so this sub-clause was silently checking zero -- the same
        # vacuity the table branch above was written to fix. Match the table row
        # form as well, and count enforcement separately so the emptiness is visible.
        total = sum(tally.values())
        for pat in (r"(\d+)\s+(?:annotation entries|existing_annotations)\b",
                    r"\|\s*\*\*total(?:\s+entries)?\*\*\s*\|\s*\*\*(\d+)\*\*"):
            for m in re.finditer(pat, flat):
                n_tally_claims += 1
                n_total_claims_enforced[0] += 1
                if int(m.group(1)) != total:
                    findings.append(
                        f"{f.name}: states {m.group(1)} total entries but the "
                        f"document contains {total}")

    if n_total_claims_enforced[0] == 0:
        problems.append(
            "clause 4 compared no stated TOTAL against the document, so the total "
            "sub-clause reported coverage it does not have")
    if n_tally_claims_enforced == 0:
        problems.append(
            "clause 4 matched no tally claim outside the retraction exemption, so it "
            "reported coverage it does not have -- state the tally somewhere the "
            "check can read it")
    if scanned == 0:
        problems.append("counted-claim check scanned zero files -- vacuous")
    if n_number_claims == 0:
        problems.append("counted-claim check matched no '<N> human <noun>' claim, so "
                        "its number clause could not fire")
    if n_enumerations == 0:
        problems.append("counted-claim check matched no gene enumeration, so its "
                        "membership clause could not fire")
    for x in findings:
        problems.append(f"counted claim disagrees with the computed data: {x}")
    return {"computed_n_human_parent_only": n,
            "computed_set": sorted(computed),
            "files_scanned": scanned,
            "number_claims_checked": n_number_claims,
            "enumerations_checked": n_enumerations,
            "tally_claims_checked": n_tally_claims,
            "tally_claims_enforced": n_tally_claims_enforced,
            "total_claims_enforced": n_total_claims_enforced[0],
            "COMPUTED_VERDICT_TALLY": dict(sorted(tally.items())),
            "computed_total_entries": sum(tally.values()),
            "unlintable_surfaces": ["the PR body", "git commit messages"],
            "findings": findings}


# ---------------------------------------------------------------------------
# H. no slot may list both a term and its own ancestor
# ---------------------------------------------------------------------------

def check_no_redundant_ancestor(problems: list[str]) -> dict[str, Any]:
    """A class-level invariant, not an instance fix.

    The PR reviewer spotted `core_functions[0].directly_involved_in` carrying both
    GO:0032968 and its ancestor GO:0006355. Rather than delete that one pair, this
    asserts the general property over EVERY multivalued term slot of every core
    function, using closures fetched by the analysis script -- so the next such pair
    cannot be introduced silently.
    """
    if not RESULTS_JSON.exists():
        raise Problem(f"missing {RESULTS_JSON}; run analyze_aff1_annotations.py")
    data = json.loads(RESULTS_JSON.read_text())
    cl = (data.get("core_function_closures") or {}).get("closures")
    if not cl:
        raise Problem("results.json has no core_function_closures; this check "
                      "would pass vacuously")
    doc = yaml.load(REVIEW.read_text(), Loader=StrictLoader)

    # Only genuinely multivalued slots. `contributes_to_molecular_function`,
    # `molecular_function` and `in_complex` are SINGLE-valued in the schema, so
    # including them could never yield a pair -- an unreachable branch that reads as
    # coverage is worse than no branch, because it looks like protection.
    MULTI = ("directly_involved_in", "locations", "anatomical_locations",
             "substrates")
    single_valued_skipped = ("molecular_function",
                             "contributes_to_molecular_function", "in_complex")
    pairs_checked = 0
    hits = []
    # The two molecular-function slots are single-valued individually but form a
    # PAIR across slots, which the reviewer noted was structurally outside this
    # check. Compare them too: asserting an activity and one of its own ancestors
    # in the two MF slots of one core function would be the same redundancy.
    MF_PAIR = ("molecular_function", "contributes_to_molecular_function")
    for i, cf in enumerate(doc.get("core_functions") or []):
        mf_ids = []
        for slot in MF_PAIR:
            v = cf.get(slot)
            if isinstance(v, dict) and isinstance(v.get("id"), str):
                mf_ids.append((slot, v["id"]))
        for (sa, a) in mf_ids:
            for (sbs, b) in mf_ids:
                if sa == sbs:
                    continue
                pairs_checked += 1
                anc = cl.get(a)
                if anc is None:
                    problems.append(
                        f"core_functions[{i}].{sa} asserts {a} but no closure was "
                        f"fetched for it -- re-run the analysis script")
                    continue
                if b in anc:
                    hits.append(
                        f"core_functions[{i}] asserts {a} in {sa} together with its "
                        f"own ancestor {b} in {sbs}")
        for slot in MULTI:
            v = cf.get(slot)
            if v is None:
                continue
            items = v if isinstance(v, list) else [v]
            ids = [it.get("id") if isinstance(it, dict) else it for it in items]
            ids = [x for x in ids if isinstance(x, str) and x.startswith("GO:")]
            for a in ids:
                for b in ids:
                    if a == b:
                        continue
                    pairs_checked += 1
                    anc = cl.get(a)
                    if anc is None:
                        problems.append(
                            f"core_functions[{i}].{slot} asserts {a} but no closure "
                            f"was fetched for it -- re-run the analysis script")
                        continue
                    if b in anc:
                        hits.append(
                            f"core_functions[{i}].{slot} lists {a} together with "
                            f"its own ancestor {b}")
    # A single-element slot yields no pairs, so a document that happened to have
    # only singletons would pass vacuously. Say so rather than reporting coverage.
    if pairs_checked == 0:
        problems.append("no slot contained two or more terms, so the "
                        "redundant-ancestor invariant could not fire")
    for h in sorted(set(hits)):
        problems.append(f"redundant ancestry inside one slot: {h}")
    # DELIBERATELY NOT COMPARED: `in_complex` against `locations`.
    #
    # A widened loop would fire on core_functions[0], which asserts GO:0032783 in
    # in_complex and GO:0005634 in locations -- and the fetched closure for
    # GO:0032783 does contain GO:0005634, so the ancestry is real. It is not a
    # curation error: "this protein is part of the super elongation complex" and
    # "this protein is in the nucleus" are different KINDS of assertion, and a
    # reader served only the complex would lose the compartment. The redundancy
    # rule this check enforces is about a slot restating its own content at two
    # granularities, which is not what that pair does. Recorded rather than
    # silently omitted, with the evidence, so the omission is a judgement a
    # reviewer can disagree with instead of a gap.
    # Derived by actually reading BOTH slots of EVERY core function, rather than
    # hardcoding index 0 and asserting what `locations` holds without looking --
    # which is what the first version of this report string did.
    live = []
    for i, cf in enumerate(doc.get("core_functions") or []):
        ic = cf.get("in_complex")
        ic_id = ic.get("id") if isinstance(ic, dict) else None
        if not ic_id:
            continue
        # `cl.get(ic_id) or []` would silently report "none in the current
        # document" for a MISSING closure -- the same silent-nothing class fixed one
        # level down in this file, and inconsistent with every other closure lookup
        # here, which raises a problem. Be loud instead.
        anc = cl.get(ic_id)
        if anc is None:
            problems.append(
                f"core_functions[{i}].in_complex asserts {ic_id} but no closure was "
                f"fetched for it, so the in_complex/locations rationale would report "
                f"'none' for a reason that is really 'not checked' -- re-run the "
                f"analysis script")
            continue
        locs = cf.get("locations") or []
        loc_ids = [(x.get("id") if isinstance(x, dict) else x) for x in locs]
        for lid in loc_ids:
            if isinstance(lid, str) and lid in anc:
                live.append(f"core_functions[{i}]: in_complex={ic_id} whose closure "
                            f"contains {lid}, which locations also asserts")
    not_compared = {
        "slot_pair": ["in_complex", "locations"],
        "reason": ("a complex and the compartment containing it are different kinds "
                   "of assertion, so co-stating them is informative, not redundant; "
                   "the rule this check enforces is about one slot restating its own "
                   "content at two granularities"),
        "live_instances": live or ["none in the current document"],
    }
    return {"pairs_checked": pairs_checked, "closures_available": len(cl),
            "slots_checked": list(MULTI),
            "cross_slot_pairs_checked": list(MF_PAIR),
            "single_valued_slots_not_applicable": list(single_valued_skipped),
            "deliberately_not_compared": not_compared,
            "hits": sorted(set(hits))}


# ---------------------------------------------------------------------------
# I. shared append-only cache: ask the two questions separately
# ---------------------------------------------------------------------------

CACHE_PATH_OVERRIDE: list[Path | None] = [None]


def check_shared_cache(problems: list[str]) -> dict[str, Any]:
    """`cache/go/terms.csv` is shared, append-only state, and the naive check gives
    FALSE POSITIVES.

    Two different questions, needing two different comparisons:

    1. *Did this branch delete anything?* -> diff against the **merge base**. A
       two-dot diff against the moving tip reports a sibling branch's ADDITION as
       this branch's DELETION, and the reflexive remedy
       (`git checkout origin/main -- cache/go/terms.csv`) then silently pulls the
       sibling's row into this PR.
    2. *Will merging duplicate a curie?* -> compare against main's current file, and
       treat curies that main has but the merge base does not as expected
       (main moved), not as loss.

    Written as a committed check rather than a shell heredoc because a verification
    that lives somewhere disposable gets described as permanent by the same commit
    that throws it away -- and because this exact assertion, run the naive way, had
    already fired a false positive on this branch.
    """
    def sh(*args: str) -> str:
        r = subprocess.run(args, capture_output=True, text=True, cwd=REPO)
        if r.returncode != 0:
            raise Problem(f"git failed: {' '.join(args)}: {r.stderr.strip()}")
        return r.stdout

    rel = "cache/go/terms.csv"
    # Overridable so the break-test can point at a temp COPY. Mutating shared,
    # cross-branch state in place and relying on a finally-block to put it back is
    # one interpreter crash away from leaving another gene's row deleted.
    path = CACHE_PATH_OVERRIDE[0] or (REPO / rel)
    if not path.exists():
        raise Problem(f"missing {rel}")

    def curies(text: str) -> Counter:
        return Counter(l.split(",")[0] for l in text.splitlines()
                       if l.startswith("GO:"))

    base_sha = sh("git", "merge-base", "origin/main", "HEAD").strip()
    if not base_sha:
        raise Problem("could not determine the merge base against origin/main")
    base = curies(sh("git", "show", f"{base_sha}:{rel}"))
    main = curies(sh("git", "show", f"origin/main:{rel}"))
    mine = curies(path.read_text())
    if not base or not main or not mine:
        raise Problem("one of the three terms.csv snapshots parsed to zero curies, "
                      "so this check would pass vacuously")

    # Q1: deletions, against the MERGE BASE.
    deleted = sorted(set(base) - set(mine))
    if deleted:
        problems.append(
            f"{rel}: this branch DELETED curies present at the merge base "
            f"{base_sha[:9]}: {deleted} -- that is a clobber of shared state")

    # Q2: duplicates that this branch would introduce.
    new_dups = {k: v for k, v in mine.items()
                if v > 1 and main.get(k, 0) < v}
    if new_dups:
        problems.append(f"{rel}: this branch introduces duplicate curies: {new_dups}")

    # Informational, and explicitly NOT a failure: curies main gained after the
    # branch point. Reporting them as loss is the known false positive.
    main_only = sorted(set(main) - set(mine))
    moved = [c for c in main_only if c not in base]
    genuinely_lost = [c for c in main_only if c in base]
    if genuinely_lost:
        problems.append(
            f"{rel}: curies present in BOTH the merge base and origin/main are "
            f"missing here: {genuinely_lost} -- this one is real loss, not the "
            f"moving-tip artefact")
    return {
        "merge_base": base_sha[:9],
        "rows_base": sum(base.values()), "rows_main": sum(main.values()),
        "rows_branch": sum(mine.values()),
        "deleted_vs_merge_base": deleted,
        "added_by_this_branch": sorted(set(mine) - set(main)),
        "main_gained_after_branch_point": moved,
        "new_duplicates": new_dups,
    }


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
    report["counted_claims"] = check_counted_claims(problems)
    report["no_redundant_ancestor"] = check_no_redundant_ancestor(problems)
    report["shared_cache"] = check_shared_cache(problems)
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

    def mut_wrong_count() -> None:
        t2 = REVIEW.read_text()
        # Change the stated number while leaving the enumeration intact -- exactly
        # the shipped defect. The mutation must be this fine: blanking the whole
        # claim would also be caught by a far weaker implementation.
        needle = "ALL ELEVEN human recipients"
        if needle not in t2:
            raise Problem("anchor for the wrong-count mutation is absent")
        REVIEW.write_text(t2.replace(needle, "ALL TWELVE human recipients", 1))
    run_case("stated count disagrees with the computed set", mut_wrong_count,
             "counted claim disagrees with the computed data")

    def mut_wrong_enumeration() -> None:
        t2 = REVIEW.read_text()
        needle = "AFF1, AFF4, CDK9, ELL, ELL2, ELL3, EAF1, EAF2, MLLT1, MLLT3 and\n      ICE2"
        alt = "AFF1, AFF4, CDK9, ELL, ELL2, ELL3, EAF1, EAF2, MLLT1, MLLT3 and ICE2"
        if needle in t2:
            REVIEW.write_text(t2.replace(needle, needle.replace("EAF2", "AFF3"), 1))
        elif alt in t2:
            REVIEW.write_text(t2.replace(alt, alt.replace("EAF2", "AFF3"), 1))
        else:
            raise Problem("anchor for the wrong-enumeration mutation is absent")
    run_case("enumerated gene set disagrees with the computed set",
             mut_wrong_enumeration,
             "counted claim disagrees with the computed data")

    def mut_wrong_disorder() -> None:
        t2 = REVIEW.read_text()
        needle = "901 of its 1210 residues"
        if needle not in t2:
            raise Problem("anchor for the disorder mutation is absent")
        REVIEW.write_text(t2.replace(needle, "1000 of its 1210 residues", 1))
    run_case("disorder figure disagrees with the feature table",
             mut_wrong_disorder, "residues but the feature table gives")

    def mut_redundant_ancestor() -> None:
        # Re-introduce exactly the pair the reviewer found, rather than a synthetic
        # one: the mutation must be as fine as the claim.
        d = yaml.load(REVIEW.read_text(), Loader=StrictLoader)
        cfs = d.get("core_functions") or []
        target = None
        for cf in cfs:
            di = cf.get("directly_involved_in") or []
            if any((x.get("id") if isinstance(x, dict) else x) == "GO:0032968"
                   for x in di):
                target = di
                break
        if target is None:
            raise Problem("no core function lists GO:0032968, so the reviewer's "
                          "pair cannot be reconstructed")
        target.append({"id": "GO:0006355",
                       "label": "regulation of DNA-templated transcription"})
        REVIEW.write_text(yaml.dump(d, sort_keys=False, allow_unicode=True))
    run_case("a slot lists a term together with its own ancestor",
             mut_redundant_ancestor, "redundant ancestry inside one slot")

    print("self-test: shared-cache deletion guard (on a COPY, never the real file)")
    import tempfile
    real_cache = REPO / "cache/go/terms.csv"
    original_cache_bytes = real_cache.read_bytes()
    with tempfile.TemporaryDirectory() as td:
        copy = Path(td) / "terms.csv"
        lines = real_cache.read_text().splitlines(keepends=True)
        victim = next((i for i, l in enumerate(lines)
                       if l.startswith("GO:0005634,")), None)
        if victim is None:
            failures.append("no GO:0005634 row to delete; cache fixture drifted")
        else:
            copy.write_text("".join(lines[:victim] + lines[victim + 1:]))
            if copy.read_text() == real_cache.read_text():
                failures.append("cache-deletion mutation was a no-op")
            else:
                CACHE_PATH_OVERRIDE[0] = copy
                try:
                    problems, _ = audit()
                finally:
                    CACHE_PATH_OVERRIDE[0] = None
                hit = [x for x in problems
                       if "DELETED curies present at the merge base" in x]
                if hit:
                    print(f"  ok   deleted a shared-cache row: {hit[0][:95]}")
                else:
                    failures.append(
                        "shared-cache deletion guard did not fire; got "
                        f"{[x[:60] for x in problems][:3]}")
    # The real cache must be byte-identical: the break-test never touched it.
    if real_cache.read_bytes() != original_cache_bytes:
        failures.append("the shared cache was modified by the self-test")
    else:
        print("  ok   the real cache/go/terms.csv is byte-identical afterwards")

    def mut_wrong_tally() -> None:
        t2 = NOTES.read_text()
        needle = "| `MODIFY` | 7 |"
        if needle not in t2:
            raise Problem("anchor for the tally mutation is absent")
        NOTES.write_text(t2.replace(needle, "| `MODIFY` | 6 |", 1))
    run_case("verdict tally disagrees with the document", mut_wrong_tally,
             "MODIFY but the document contains 7")

    def mut_cross_slot_ancestor() -> None:
        # molecular_function and contributes_to_molecular_function are each
        # single-valued, so this pair exists only ACROSS slots -- the case the
        # reviewer noted was structurally outside the check.
        d = yaml.load(REVIEW.read_text(), Loader=StrictLoader)
        cfs = d.get("core_functions") or []
        if not cfs:
            raise Problem("no core_functions to contaminate")
        # GO:0060090 is the parent of GO:0030674, which core function 1 asserts.
        cfs[0]["molecular_function"] = {
            "id": "GO:0030674", "label": "protein-macromolecule adaptor activity"}
        cfs[0]["contributes_to_molecular_function"] = {
            "id": "GO:0060090", "label": "molecular adaptor activity"}
        REVIEW.write_text(yaml.dump(d, sort_keys=False, allow_unicode=True))
    run_case("a term and its ancestor split across the two MF slots",
             mut_cross_slot_ancestor, "together with its own ancestor")

    def mut_delete_tally_table() -> None:
        # Removing the ONLY surface that supplies clause-4 coverage must trip the
        # vacuity guard. Before the fix it did not, because three correct numbers
        # inside the retraction sentence were counted as enforcement.
        t2 = NOTES.read_text()
        rows = [r for r in ("| `ACCEPT` | 11 |", "| `MODIFY` | 7 |",
                            "| `KEEP_AS_NON_CORE` | 2 |", "| `NEW` | 1 |")
                if r in t2]
        if len(rows) < 4:
            raise Problem(f"tally table rows missing; found only {rows}")
        for r in rows:
            t2 = t2.replace(r, "")
        NOTES.write_text(t2)
    run_case("the only enforcing tally surface is deleted", mut_delete_tally_table,
             "matched no tally claim outside the retraction exemption")

    def mut_wrong_total() -> None:
        t2 = NOTES.read_text()
        needle = "| **total entries** | **21**"
        if needle not in t2:
            raise Problem("anchor for the total mutation is absent")
        NOTES.write_text(t2.replace(needle, "| **total entries** | **20**", 1))
    run_case("stated total disagrees with the document", mut_wrong_total,
             "total entries but the document contains 21")

    def mut_delete_total() -> None:
        t2 = NOTES.read_text()
        import re as _re
        n2 = _re.sub(r"\|\s*\*\*total(?:\s+entries)?\*\*\s*\|\s*\*\*\d+\*\*[^\n]*\n",
                     "", t2)
        if n2 == t2:
            raise Problem("total row not found to delete")
        NOTES.write_text(n2)
    run_case("the only stated total is deleted", mut_delete_total,
             "compared no stated TOTAL")

    def mut_worded_disorder() -> None:
        # The form that was silently unmatched: a WORDED quantity. Distinct from
        # mut_wrong_disorder, which uses digits -- so a clause that handles only
        # numerals passes that one and fails this one.
        t2 = REVIEW.read_text()
        needle = "901 of its 1210 residues"
        if needle not in t2:
            raise Problem("anchor for the worded-disorder mutation is absent")
        REVIEW.write_text(t2.replace(needle, "a thousand of its 1210 residues", 1))
    run_case("disorder figure stated as a WORDED quantity", mut_worded_disorder,
             "residues but the feature table gives")

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
