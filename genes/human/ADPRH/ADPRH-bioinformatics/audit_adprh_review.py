"""Invariant checks on ADPRH-ai-review.yaml that no repo validator performs.

Each check here exists because the corresponding defect has actually shipped somewhere
in this campaign. They run over the EMITTED YAML file, not over any generator, because
that is what ships and what a reviewer greps.

Checks
  A  duplicate mapping keys -- PyYAML keeps the LAST occurrence and silently discards
     the earlier one, so provenance can be deleted before any quote gate runs.  Detected
     only by a strict loader over the raw text.
  B  YAML anchors/aliases -- an alias multiplies one object across N rows, so N
     "independent" quotes are really one, and every parsed-tree checker reports N passes.
  C  raw-vs-parsed reconciliation of quote-bearing keys.  A mismatch is the only signal
     a duplicate key or an alias gives you.
  D  GOA row count vs existing_annotations count, against DISTINCT GOA lines (the TSV can
     contain byte-identical duplicates, and the fetch-gene seeder can collapse rows that
     differ only in WITH/FROM).
  E  logical-opposite citation cross-product: for any positive/negative regulation pair,
     a shared reference is a defect visible from the TSV alone.
  F  the first clause of every review summary must not name an action other than the row's
     own.  An attributed cross-reference to another row's action is allowed deliberately;
     a guard that forbade legitimate practice would be worked around rather than obeyed.
  G  core_functions <-> existing_annotations agreement, in BOTH directions:
       G1 every core_functions term is backed by an ACCEPT/NEW row or a MODIFY replacement;
       G2 every term marked ACCEPT on a molecular_function row appears in core_functions,
          unless it is listed in ACCEPT_MF_NOT_CORE with a reason.  Unwritten is not the
          same as passing.
  H  a review with status COMPLETE must contain no PENDING actions, no TODO summaries
     and no TODO description.  Found by running this audit against the fetch-gene stub,
     where every check but G passed on 15 entirely unreviewed rows.
  I  AT LEAST ONE supporting_text on a row must contain a surface form of that row's OWN
     term (the predicate is `any`, not `every` -- a row may legitimately carry a
     corroborating quote about something else alongside the on-point one).  A quote can be
     verbatim, correctly attributed and about a different row; every other gate passes it.
     The declared forms must be pairwise disjoint, which is itself asserted.

Run:  uv run python audit_adprh_review.py
      uv run python audit_adprh_review.py --self-test
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from collections import Counter
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
GENE_DIR = HERE.parent
REVIEW = GENE_DIR / "ADPRH-ai-review.yaml"
GOA = GENE_DIR / "ADPRH-goa.tsv"

# Molecular-function terms that are ACCEPTed but deliberately absent from core_functions,
# each with the reason.  Empty entries are rejected, so the list cannot be used to wave
# a term through silently.
ACCEPT_MF_NOT_CORE: dict[str, str] = {}

# GO ids that are logically opposed to one another.  Checked as a pair regardless of
# whether both are present, so the check is meaningful when one is added later.
OPPOSITE_PAIRS: list[tuple[str, str]] = []

# Check I.  Surface forms that a supporting_text must contain for the row's term to count
# as quoted rather than merely asserted.  Keyed on the GO id, which is the stable entity -
# the term label and the surrounding prose both get reworded, the id does not.
#
# LIMITATION, stated rather than implied: this matches SURFACE FORMS.  A quote that
# supports the claim in words not listed here will be reported as a problem until a form
# is added, and conversely a quote that merely contains the word is not thereby shown to
# support the claim.  It catches the cross-row citation slip - a potassium quote under a
# magnesium row - and nothing subtler.
# The form sets must be PAIRWISE DISJOINT, asserted below.  An earlier version listed
# table-cell fragments ("| k, mg |", ", mg |") that the SAME RESULTS.md row satisfied for
# both the magnesium and the potassium term, so the check could not have discriminated the
# two on that row - which is the one discrimination it exists to make.
TERM_SURFACE_FORMS: dict[str, tuple[str, ...]] = {
    "GO:0000287": ("magnesium", "mg2+", "mg(2+)"),
    "GO:0030955": ("potassium", "k+", "k(+)"),
    # "hydrolase" belongs to the activity term only, and the bare word "modification" was
    # removed from GO:0036211 - both were flagged by the disjointness assertion below.
    "GO:0003875": ("arginine", "adp-ribosylarginine", "hydrolase"),
    "GO:0051725": ("de-adp-ribosyl", "de-modification", "removing one or more adp-ribose"),
    "GO:0036211": ("reversible modification",),
    "GO:0005576": ("extracellular", "cerebrospinal", "csf"),
    "GO:0005515": ("interact", "two-hybrid", "two hybrid", "binary", "protein-protein"),
}

ACTION_WORDS = {
    "ACCEPT": ["accept"],
    "MODIFY": ["modif"],
    "REMOVE": ["remove", "removed", "removal"],
    "MARK_AS_OVER_ANNOTATED": ["over-annotat", "overannotat"],
    "KEEP_AS_NON_CORE": ["non-core", "keep as non"],
    "UNDECIDED": ["undecided"],
}


class AuditError(RuntimeError):
    """A missing input.  Never degrade silently."""


class StrictLoader(yaml.SafeLoader):
    """SafeLoader that raises on a duplicate mapping key instead of discarding data."""


def _no_duplicates(loader, node, deep=False):
    mapping = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in mapping:
            raise yaml.constructor.ConstructorError(
                None, None, f"duplicate key {key!r}", key_node.start_mark
            )
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


StrictLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _no_duplicates)


def walk_quotes(node, path=""):
    """Yield (path, reference_id, supporting_text) from EVERY quote-bearing container,
    including the two that checkquotes.py does not walk: `provenance` and
    `knowledge_gaps[].provenance`."""
    if isinstance(node, dict):
        for k, v in node.items():
            if k in ("supported_by", "provenance", "findings") and isinstance(v, list):
                for i, e in enumerate(v):
                    if isinstance(e, dict) and e.get("supporting_text"):
                        yield (
                            f"{path}.{k}[{i}]",
                            e.get("reference_id") or node.get("id"),
                            e["supporting_text"],
                        )
            if isinstance(v, (dict, list)):
                yield from walk_quotes(v, f"{path}.{k}")
    elif isinstance(node, list):
        for i, e in enumerate(node):
            yield from walk_quotes(e, f"{path}[{i}]")


def load() -> tuple[str, dict]:
    if not REVIEW.exists():
        raise AuditError(f"missing input {REVIEW}; run `just fetch-gene human ADPRH`")
    if not GOA.exists():
        raise AuditError(f"missing input {GOA}; run `just fetch-gene human ADPRH`")
    raw = REVIEW.read_text()
    data = yaml.load(raw, Loader=StrictLoader)  # check A happens here
    return raw, data


def audit(raw: str, data: dict) -> list[str]:
    problems: list[str] = []

    # ---- B: anchors and aliases -------------------------------------------------
    # Match anywhere on the line: PyYAML emits `- &id024` on a list-item line, but an
    # anchor can equally appear inline as `key: &id001`, and the line-anchored form of
    # this regex missed that (found by break-testing, not by reading).
    anchors = re.findall(r"&id\d+", raw)
    aliases = re.findall(r"\*id\d+", raw)
    if anchors or aliases:
        problems.append(
            f"B: YAML anchors/aliases present ({len(anchors)} anchors, {len(aliases)} aliases); "
            "an alias multiplies one quote across rows and every parsed-tree checker will "
            "report it as N independent passes"
        )

    # ---- C: raw vs parsed reconciliation ----------------------------------------
    # Anchor the regex: a bare 'reference_id:' substring also matches
    # 'original_reference_id:', and PyYAML puts an anchor on the list-item line so
    # '^\s*- reference_id:' alone undercounts.
    raw_refs = len(re.findall(r"(?m)^\s*(?:-\s*)?reference_id:", raw))
    raw_orig = len(re.findall(r"(?m)^\s*original_reference_id:", raw))
    raw_quotes = len(re.findall(r"(?m)^\s*supporting_text:", raw))
    parsed = list(walk_quotes(data))
    parsed_quotes = len(parsed)
    if raw_quotes != parsed_quotes:
        problems.append(
            f"C: raw supporting_text count {raw_quotes} != parsed count {parsed_quotes}; "
            "investigate rather than reconcile - a gap here is a duplicate key or an alias"
        )
    if raw_orig != len(data.get("existing_annotations", [])):
        problems.append(
            f"C: {raw_orig} original_reference_id lines vs "
            f"{len(data.get('existing_annotations', []))} existing_annotations"
        )

    # ---- D: GOA row reconciliation ----------------------------------------------
    with GOA.open() as fh:
        rows = list(csv.reader(fh, delimiter="\t"))
    header, body = rows[0], [r for r in rows[1:] if r]
    distinct = {tuple(r) for r in body}
    n_ann = len(data.get("existing_annotations", []))
    if len(distinct) != n_ann:
        problems.append(
            f"D: GOA has {len(body)} lines ({len(distinct)} distinct) but the review has "
            f"{n_ann} existing_annotations; reconcile explicitly and document any collapse"
        )
    # every distinct (GO id, evidence code) pair in the TSV must appear in the review
    gi, ei = header.index("GO TERM"), header.index("GO EVIDENCE CODE")
    goa_pairs = Counter((r[gi], r[ei]) for r in body)
    rev_pairs = Counter(
        (a["term"]["id"], a["evidence_type"]) for a in data.get("existing_annotations", [])
    )
    for k, v in goa_pairs.items():
        if rev_pairs.get(k, 0) != v:
            problems.append(
                f"D: {k[0]} / {k[1]} appears {v}x in GOA but {rev_pairs.get(k, 0)}x in the review"
            )

    # ---- E: logical-opposite citation cross-product ------------------------------
    # Derive the pairs from the data rather than only from the hardcoded list, so a
    # positive/negative pair added later is caught without editing this file.
    labels = {a["term"]["id"]: a["term"]["label"] for a in data.get("existing_annotations", [])}
    derived: list[tuple[str, str]] = []
    for gid, lab in labels.items():
        if lab.startswith("positive regulation of "):
            tail = lab[len("positive regulation of ") :]
            for gid2, lab2 in labels.items():
                if lab2 == "negative regulation of " + tail:
                    derived.append((gid, gid2))
    for a_id, b_id in list(OPPOSITE_PAIRS) + derived:
        refs_a = {
            a["original_reference_id"]
            for a in data.get("existing_annotations", [])
            if a["term"]["id"] == a_id
        }
        refs_b = {
            a["original_reference_id"]
            for a in data.get("existing_annotations", [])
            if a["term"]["id"] == b_id
        }
        shared = refs_a & refs_b
        if shared:
            problems.append(
                f"E: {a_id} and {b_id} are logical opposites and share reference(s) {sorted(shared)}; "
                "no single reference can support both directions"
            )

    # ---- F: summary opener must not name a different action ----------------------
    for i, a in enumerate(data.get("existing_annotations", [])):
        review = a.get("review") or {}
        action = review.get("action")
        summary = (review.get("summary") or "").strip()
        if not action:
            problems.append(f"F: existing_annotations[{i}] has no review.action")
            continue
        if not summary:
            problems.append(f"F: existing_annotations[{i}] ({action}) has an empty summary")
            continue
        opener = summary.split(".")[0].lower()
        for other, words in ACTION_WORDS.items():
            if other == action:
                continue
            for w in words:
                if w in opener:
                    # An ATTRIBUTED cross-reference to another row is legitimate and must
                    # not fire; only an unqualified opener claiming the other action does.
                    if re.search(r"\b(unlike|whereas|as for|compared with|rather than)\b", opener):
                        continue
                    problems.append(
                        f"F: existing_annotations[{i}] action={action} but its summary opens "
                        f'with wording for {other}: "{summary.split(".")[0]}"'
                    )
    if not data.get("existing_annotations"):
        problems.append("F: existing_annotations is empty or absent - refusing to pass vacuously")

    # ---- G: core_functions <-> existing_annotations, both directions -------------
    accepted, new_terms, replacements, mf_accepted = set(), set(), set(), set()
    for a in data.get("existing_annotations", []):
        review = a.get("review") or {}
        action = review.get("action")
        tid = a["term"]["id"]
        if action == "ACCEPT":
            accepted.add(tid)
            if a.get("qualifier") in ("enables", "contributes_to"):
                mf_accepted.add(tid)
        if action == "NEW":
            new_terms.add(tid)
        if action == "MODIFY":
            for r in review.get("proposed_replacement_terms") or []:
                replacements.add(r["id"])

    cfs = data.get("core_functions") or []
    if not cfs:
        problems.append("G: core_functions is empty or absent - refusing to pass vacuously")
    cf_terms = set()
    for i, cf in enumerate(cfs):
        for slot in ("molecular_function", "contributes_to_molecular_function"):
            term = cf.get(slot)
            if isinstance(term, dict) and "id" in term:
                cf_terms.add(term["id"])
                if term["id"] not in accepted | new_terms | replacements:
                    problems.append(
                        f"G1: core_functions[{i}].{slot} {term['id']} is not backed by any "
                        "ACCEPT/NEW row or MODIFY replacement"
                    )
        for slot in ("directly_involved_in", "locations"):
            for term in cf.get(slot) or []:
                if isinstance(term, dict) and term.get("id") not in accepted | new_terms | replacements:
                    problems.append(
                        f"G1: core_functions[{i}].{slot} {term.get('id')} is not backed by any "
                        "ACCEPT/NEW row or MODIFY replacement"
                    )
    for tid in sorted(mf_accepted - cf_terms):
        reason = ACCEPT_MF_NOT_CORE.get(tid, "")
        if not reason.strip():
            problems.append(
                f"G2: {tid} is ACCEPTed on a molecular-function row but is absent from "
                "core_functions and has no entry in ACCEPT_MF_NOT_CORE"
            )
    for tid, reason in ACCEPT_MF_NOT_CORE.items():
        if not reason.strip():
            problems.append(f"G2: ACCEPT_MF_NOT_CORE[{tid}] has an empty reason")
        if tid not in mf_accepted:
            problems.append(
                f"G2: ACCEPT_MF_NOT_CORE lists {tid}, which is not an ACCEPTed "
                "molecular-function row - the exemption is unreachable"
            )

    # ---- self-description: the docstring must enumerate exactly the checks implemented.
    # Lives here rather than in self_test() so it runs on every invocation, like the
    # disjointness assertion.  The count drifted onto three prose surfaces at once when
    # check I was added; this is the one surface that can police itself.
    src_text = Path(__file__).read_text()
    documented = set(re.findall(r"(?m)^  ([A-Z])  ", src_text.split('"""')[1]))
    implemented = set(re.findall(r'problems\.append\(\s*\n?\s*f?"([A-Z])[0-9]?:', src_text))
    # Check A is enforced by StrictLoader at PARSE time and never reaches `problems`.
    # Credit it only if the loader demonstrably rejects a duplicate key - established
    # behaviourally, not by grepping for the class name.
    try:
        yaml.load("a: 1\na: 2\n", Loader=StrictLoader)
    except yaml.constructor.ConstructorError:
        implemented.add("A")
    if documented != implemented:
        problems.append(
            f"self-description: docstring documents {sorted(documented)} but the code "
            f"implements {sorted(implemented)}"
        )

    # ---- I: each supporting_text set must be about its own row's term ------------
    # Two terms sharing a surface form would make the check unable to tell them apart on a
    # quote containing that form.  Enforce disjointness rather than trusting the table.
    for a_id, a_forms in TERM_SURFACE_FORMS.items():
        for b_id, b_forms in TERM_SURFACE_FORMS.items():
            if a_id >= b_id:
                continue
            for fa in a_forms:
                for fb in b_forms:
                    if fa in fb or fb in fa:
                        problems.append(
                            f"I: TERM_SURFACE_FORMS[{a_id}] and [{b_id}] share the overlapping "
                            f"forms {fa!r}/{fb!r}; the check cannot discriminate the two terms"
                        )

    # The cross-row citation slip: a quote that is verbatim, correctly attributed, and
    # about a DIFFERENT row.  Every mechanical gate in this repo passes it, because each
    # validates a quote against its source and none against the claim it is attached to.
    for i, a in enumerate(data.get("existing_annotations", [])):
        tid = a["term"]["id"]
        forms = TERM_SURFACE_FORMS.get(tid)
        quotes = [
            sb.get("supporting_text", "")
            for sb in ((a.get("review") or {}).get("supported_by") or [])
        ]
        if not quotes:
            continue  # a row with no supported_by is a separate question, not this check's
        if forms is None:
            problems.append(
                f"I: existing_annotations[{i}] {tid} has quotes but no entry in "
                "TERM_SURFACE_FORMS - the check cannot run and must not pass vacuously"
            )
            continue
        norm = [" ".join(q.split()).lower() for q in quotes]
        if not any(any(f in q for f in forms) for q in norm):
            problems.append(
                f"I: existing_annotations[{i}] {tid} ({a['term']['label']}) has "
                f"{len(quotes)} supporting_text(s), none containing any surface form of its "
                f"own term {forms}"
            )
    for i, cf in enumerate(data.get("core_functions") or []):
        mf = cf.get("molecular_function") or {}
        tid = mf.get("id")
        quotes = [sb.get("supporting_text", "") for sb in (cf.get("supported_by") or [])]
        if not tid or not quotes:
            continue
        forms = TERM_SURFACE_FORMS.get(tid)
        if forms is None:
            problems.append(f"I: core_functions[{i}] {tid} has no entry in TERM_SURFACE_FORMS")
            continue
        norm = [" ".join(q.split()).lower() for q in quotes]
        if not any(any(f in q for f in forms) for q in norm):
            problems.append(
                f"I: core_functions[{i}] {tid} ({mf.get('label')}) has {len(quotes)} "
                f"supporting_text(s), none containing any surface form of its own term {forms}"
            )

    # ---- H: a COMPLETE review must contain no PENDING rows ----------------------
    # Added after running this audit against the fetch-gene stub: every check passed
    # except G, even though all 15 rows were still `action: PENDING`.  A guard that
    # clears an entirely unreviewed file is worse than no guard.
    if data.get("status") == "COMPLETE":
        pending = [
            i
            for i, a in enumerate(data.get("existing_annotations", []))
            if (a.get("review") or {}).get("action") == "PENDING"
        ]
        if pending:
            problems.append(
                f"H: status is COMPLETE but existing_annotations {pending} are still PENDING"
            )
        todos = [
            i
            for i, a in enumerate(data.get("existing_annotations", []))
            if "TODO" in ((a.get("review") or {}).get("summary") or "")
        ]
        if todos:
            problems.append(f"H: status is COMPLETE but existing_annotations {todos} have TODO summaries")
        if "TODO" in str(data.get("description", "")):
            problems.append("H: status is COMPLETE but description is still a TODO placeholder")

    return problems


def self_test() -> int:
    """Break-test every check in the direction it exists to catch.

    A passing self-test proves the guards I thought of fire; it cannot tell me which
    guard I failed to write.  Each mutation asserts its target string is present before
    replacing, so a mutation that has silently drifted is an error rather than a
    vacuous pass.
    """
    raw, data = load()
    baseline = audit(raw, data)
    failures: list[str] = []
    if baseline:
        failures.append(f"baseline is not clean: {baseline}")

    def mutate(text: str, old: str, new: str) -> str:
        if old not in text:
            raise AuditError(f"self-test mutation target has drifted: {old[:70]!r}")
        return text.replace(old, new, 1)

    def expect(tag: str, mutated_raw: str, mutated_data: dict | None = None):
        try:
            d = mutated_data if mutated_data is not None else yaml.load(mutated_raw, Loader=StrictLoader)
        except yaml.constructor.ConstructorError:
            return  # check A fired at parse time, which is the intended behaviour
        got = audit(mutated_raw, d)
        if not any(p.startswith(tag) for p in got):
            failures.append(f"check {tag} did not fire; got {got}")

    # A: duplicate key must raise at parse time
    dup = mutate(raw, "gene_symbol: ADPRH\n", "gene_symbol: ADPRH\ngene_symbol: ADPRH\n")
    try:
        yaml.load(dup, Loader=StrictLoader)
        failures.append("check A: strict loader accepted a duplicate key")
    except yaml.constructor.ConstructorError:
        pass
    # ... and prove PyYAML's default loader would NOT have caught it
    if yaml.safe_load(dup).get("gene_symbol") != "ADPRH":
        failures.append("check A: sanity - safe_load did not silently keep the last key")

    # B: an anchor/alias must be reported
    expect("B", mutate(raw, "existing_annotations:\n", "existing_annotations: &id001\n"))
    expect(
        "B",
        mutate(raw, "  supported_by:\n  - reference_id:", "  supported_by:\n  - &id024\n    reference_id:"),
    )

    # C: raw > parsed, the shape a duplicate key or an alias produces.  An earlier
    # version of this mutation inserted a COMMENTED-OUT supporting_text line, which the
    # raw regex correctly ignores - so it was a silent no-op that "proved" the guard.
    dC = yaml.load(raw, Loader=StrictLoader)
    for a in dC["existing_annotations"]:
        sb = (a.get("review") or {}).get("supported_by")
        if sb:
            sb.pop()
            break
    else:
        raise AuditError("self-test mutation target has drifted: no supported_by to drop")
    expect("C", raw, dC)

    # D: drop an annotation
    d2 = yaml.load(raw, Loader=StrictLoader)
    d2["existing_annotations"] = d2["existing_annotations"][:-1]
    expect("D", raw, d2)

    # E: manufacture a positive/negative pair sharing a reference
    d3 = yaml.load(raw, Loader=StrictLoader)
    for lab, gid in (("positive regulation of foo", "GO:9999901"), ("negative regulation of foo", "GO:9999902")):
        d3["existing_annotations"].append(
            {
                "term": {"id": gid, "label": lab},
                "evidence_type": "ISS",
                "original_reference_id": "PMID:1",
                "qualifier": "involved_in",
                "review": {"summary": "x.", "action": "ACCEPT"},
            }
        )
    expect("E", raw, d3)

    # F: an ACCEPT row whose summary opens by claiming removal
    d4 = yaml.load(raw, Loader=StrictLoader)
    row = next(a for a in d4["existing_annotations"] if a["review"]["action"] == "ACCEPT")
    row["review"]["summary"] = "Removed as unsupported. Rest of the reasoning unchanged."
    expect("F", raw, d4)

    # F: an ATTRIBUTED cross-reference must NOT fire (the happy direction)
    d4b = yaml.load(raw, Loader=StrictLoader)
    row = next(a for a in d4b["existing_annotations"] if a["review"]["action"] == "ACCEPT")
    row["review"]["summary"] = (
        "Accepted, unlike the Y2H rows which are marked over-annotated. Reasoning unchanged."
    )
    if any(p.startswith("F") for p in audit(raw, d4b)):
        failures.append("check F fired on a legitimate attributed cross-reference")

    # F: a row with no action must fail loudly rather than pass vacuously
    d4c = yaml.load(raw, Loader=StrictLoader)
    d4c["existing_annotations"][0]["review"].pop("action")
    expect("F", raw, d4c)

    # G1: a core function term with no backing row
    d5 = yaml.load(raw, Loader=StrictLoader)
    d5["core_functions"][0]["molecular_function"] = {"id": "GO:9999999", "label": "invented"}
    expect("G1", raw, d5)

    # G2: an ACCEPTed MF term dropped from core_functions
    d6 = yaml.load(raw, Loader=StrictLoader)
    d6["core_functions"] = [d6["core_functions"][0]]  # drops the GO:0000287 core function
    expect("G2", raw, d6)

    # G: empty core_functions must fail loudly
    d7 = yaml.load(raw, Loader=StrictLoader)
    d7["core_functions"] = []
    expect("G", raw, d7)

    # H: a COMPLETE review with a PENDING row
    d8 = yaml.load(raw, Loader=StrictLoader)
    d8["existing_annotations"][0]["review"]["action"] = "PENDING"
    expect("H", raw, d8)

    # H: a COMPLETE review with a TODO description
    d9 = yaml.load(raw, Loader=StrictLoader)
    d9["description"] = "TODO: Add description for ADPRH"
    expect("H", raw, d9)

    # I: move the potassium quote onto the magnesium row - the exact defect that shipped
    dI = yaml.load(raw, Loader=StrictLoader)
    row = next(
        a
        for a in dI["existing_annotations"]
        if a["term"]["id"] == "GO:0000287" and a["original_reference_id"] == "PMID:30472116"
    )
    row["review"]["supported_by"] = [
        {
            "reference_id": "PMID:19407395",
            "supporting_text": (
                "hARH1 has been cloned, expressed heterologously in Escherichia coli, "
                "purified and crystallized in complex with K(+) and ADP."
            ),
        }
    ]
    expect("I", raw, dI)

    # I: a term with quotes but no surface forms declared must fail loudly, not pass
    dI2 = yaml.load(raw, Loader=StrictLoader)
    dI2["existing_annotations"][0]["term"]["id"] = "GO:9999998"
    expect("I", raw, dI2)

    # I: overlapping surface forms must be rejected, not silently tolerated
    global TERM_SURFACE_FORMS
    saved_forms = dict(TERM_SURFACE_FORMS)
    TERM_SURFACE_FORMS = dict(TERM_SURFACE_FORMS, **{"GO:0030955": ("potassium", "magnesium")})
    try:
        expect("I", raw, yaml.load(raw, Loader=StrictLoader))
    finally:
        TERM_SURFACE_FORMS = saved_forms

    # H must NOT fire while the review is still in progress (the happy direction)
    d10 = yaml.load(raw, Loader=StrictLoader)
    d10["status"] = "IN_PROGRESS"
    d10["existing_annotations"][0]["review"]["action"] = "PENDING"
    if any(p.startswith("H") for p in audit(raw, d10)):
        failures.append("check H fired on a non-COMPLETE review, where PENDING is legitimate")

    for f in failures:
        print("SELF-TEST FAIL:", f)
    print(f"self-test: {len(failures)} problem(s)")
    return 1 if failures else 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    if args.self_test:
        return self_test()
    raw, data = load()
    problems = audit(raw, data)
    for p in problems:
        print("PROBLEM:", p)
    print(f"audit: {len(problems)} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
