#!/usr/bin/env python3
"""Invariant gates over the EMITTED ``AFF4-ai-review.yaml``.

These checks read the artifact that ships, not the reasoning that produced it,
because a phrase that is contiguous in prose is line-wrapped in the dumped YAML
and a detector that runs over the wrong representation is blind by construction.

Checks
------
A. strict load -- a duplicate mapping key silently DESTROYS data on parse (PyYAML
   keeps the last occurrence), and no quote gate can see data that parsing already
   removed. Also refuses YAML anchors, which silently MULTIPLY data.
B. raw-vs-parsed quote reconciliation. The only signal that a quote has been lost
   or duplicated is a count that refuses to add up.
C. every ``supporting_text`` is verbatim in its source, INCLUDING the `file:` ones
   the repo validator skips entirely and the ``provenance`` ones ``checkquotes.py``
   does not walk. Fails if it checks zero.
D. annotation coverage: one entry per distinct GOA row, plus the review's own NEW
   rows, asserted against the TSV rather than against the fetch-gene stub.
E. ``source_entities`` set-equality against the GOA WITH/FROM field, per row.
   Asserted on MEMBERSHIP, not cardinality: a matching count is not a matching set.
F. every ``summary`` opens with a clause naming its own row's action.
G. core_functions <-> existing_annotations, in BOTH directions.
H. the hedge sweep, over EVERY structured slot: nothing this review declines in
   prose may be asserted flatly in a slot.
I. quote SUBJECT: every row must have at least one PMID quote naming AFF4 or the row's
   own partner. Verbatim is not the same as relevant and nothing else checks it.
J. ``full_text_unavailable`` flags must agree with the cache BODY, not with the cache's own
   frontmatter flag. This review shipped the harm that rule exists to prevent.

Usage::

    uv run --with requests python audit_aff4_review.py
    uv run --with requests python audit_aff4_review.py --self-test
"""

from __future__ import annotations

import argparse
import collections
import re
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
GENE_DIR = HERE.parent
REPO = GENE_DIR.parents[2]
REVIEW = GENE_DIR / "AFF4-ai-review.yaml"
GOA = GENE_DIR / "AFF4-goa.tsv"
UNIPROT_FLATFILE = GENE_DIR / "AFF4-uniprot.txt"

# Terms this review deliberately declines to assert. Selecting on the STABLE
# ENTITY (the GO id) rather than on the conclusion's wording, because the wording
# is exactly what gets reworded.
DECLINED_TERMS = {
    "GO:0001650": "fibrillar centre: kept as an observation, explicitly NOT a core location",
    "GO:0016604": "nuclear body: kept as an observation, explicitly NOT a core location",
    "GO:0034976": "response to ER stress: marked over-annotated, must not be asserted anywhere",
    "GO:0030332": "cyclin binding: argued to be inapplicable to cyclin T1, so must not be used",
    "GO:0003677": "DNA binding: the CHD nucleic-acid result is in vitro only and is declined",
    "GO:0003723": "RNA binding: same -- declined, and filed as an experiment to do instead",
}

# Every slot in which a Term id can be asserted. Enumerated as a list rather than
# inferred, so that a slot added later fails loudly instead of going unswept.
CORE_FUNCTION_TERM_SLOTS = [
    "molecular_function",
    "contributes_to_molecular_function",
    "directly_involved_in",
    "locations",
    "anatomical_locations",
    "substrates",
    "in_complex",
]

ACTION_OPENERS = {
    "ACCEPT": ("accepted",),
    "KEEP_AS_NON_CORE": ("kept as non-core",),
    "MODIFY": ("modified",),
    "MARK_AS_OVER_ANNOTATED": ("marked as over-annotated",),
    "REMOVE": ("removed",),
    "UNDECIDED": ("undecided",),
    "NEW": ("new annotation proposed",),
}


class AuditError(RuntimeError):
    pass


# --------------------------------------------------------------------------- #

class StrictLoader(yaml.SafeLoader):
    """Rejects duplicate mapping keys, which PyYAML otherwise drops silently."""


def _no_duplicate_keys(loader, node, deep=False):
    mapping = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in mapping:
            raise AuditError(
                f"duplicate mapping key {key!r} at line {key_node.start_mark.line + 1} -- "
                "PyYAML keeps only the last occurrence, so data has already been destroyed "
                "before any quote gate can see it."
            )
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


StrictLoader.construct_mapping = _no_duplicate_keys


def norm(t: str) -> str:
    """Whitespace-normalising comparison, mirroring linkml-reference-validator."""
    return re.sub(r"\s+", " ", t).strip().lower()


def load_review(text: str | None = None) -> tuple[dict, str]:
    if text is None:
        if not REVIEW.exists():
            raise AuditError(f"missing input {REVIEW}. Run: just fetch-gene human AFF4")
        text = REVIEW.read_text()
    if "&id" in text:
        raise AuditError(
            "YAML anchors (&id...) present. An alias makes N rows share ONE object, so every "
            "gate verifies the same quote N times and reports N successes. Dump with "
            "ignore_aliases=True."
        )
    data = yaml.load(text, Loader=StrictLoader)
    return data, text


def quote_entries(data: dict) -> list[tuple[str, str, str, str]]:
    """(container_key, path, reference_id, supporting_text) for every quote-bearing entry."""
    out: list[tuple[str, str, str, str]] = []

    def walk(node, path=""):
        if isinstance(node, dict):
            for k, v in node.items():
                if k in ("supported_by", "provenance", "findings") and isinstance(v, list):
                    for i, e in enumerate(v):
                        if isinstance(e, dict) and e.get("supporting_text"):
                            out.append((k, f"{path}.{k}[{i}]",
                                        e.get("reference_id") or node.get("id") or "",
                                        e["supporting_text"]))
                walk(v, f"{path}.{k}")
        elif isinstance(node, list):
            for i, e in enumerate(node):
                walk(e, f"{path}[{i}]")

    walk(data)
    return out


def source_text(reference_id: str) -> tuple[Path, str]:
    if reference_id.startswith("PMID:"):
        p = REPO / "publications" / f"PMID_{reference_id.split(':', 1)[1]}.md"
    elif reference_id.startswith("file:"):
        rel = reference_id.split(":", 1)[1]
        p = REPO / "genes" / rel
        if not p.exists():
            p = REPO / rel
    else:
        return Path("/dev/null"), ""  # GO_REF / Reactome: not text-checkable
    if not p.exists():
        raise AuditError(f"source for {reference_id} not found at {p}")
    return p, p.read_text()


def read_goa_rows() -> list[dict]:
    if not GOA.exists():
        raise AuditError(f"missing input {GOA}. Run: just fetch-gene human AFF4")
    lines = GOA.read_text().splitlines()
    idx = {n: i for i, n in enumerate(lines[0].split("\t"))}
    rows = []
    for line in lines[1:]:
        if not line.strip():
            continue
        f = line.split("\t")
        rows.append({
            "go_id": f[idx["GO TERM"]],
            "evidence": f[idx["GO EVIDENCE CODE"]],
            "reference": f[idx["REFERENCE"]],
            "with_from": f[idx["WITH/FROM"]],
            "qualifier": f[idx["QUALIFIER"]],
        })
    return rows


# --------------------------------------------------------------------------- #
# Checks. Each appends to ``problems``; none raises, so a new check cannot abort
# the ones after it (a check that kills the harness is worse than no check,
# because the harness still prints as though it ran).
# --------------------------------------------------------------------------- #

def check_b_raw_vs_parsed(data: dict, text: str, problems: list[str]) -> None:
    raw_quotes = len(re.findall(r"^\s*(?:-\s*)?supporting_text:", text, re.M))
    raw_refs = len(re.findall(r"^\s*(?:-\s*)?reference_id:", text, re.M))
    parsed = quote_entries(data)
    if raw_quotes != len(parsed):
        problems.append(
            f"[B] raw supporting_text occurrences {raw_quotes} != parsed quote entries "
            f"{len(parsed)}. Do NOT rationalise this gap -- derive the expected number "
            "independently and find out what parsing removed or multiplied."
        )
    if raw_refs != raw_quotes:
        problems.append(
            f"[B] raw reference_id occurrences {raw_refs} != raw supporting_text "
            f"{raw_quotes}; every quote must carry its own reference."
        )


def check_c_quotes(data: dict, problems: list[str]) -> int:
    entries = quote_entries(data)
    if not entries:
        problems.append("[C] zero quotes found -- refusing a vacuous pass.")
        return 0
    checked = 0
    for container, path, ref, quote in entries:
        p, text = source_text(ref)
        if not text:
            continue  # GO_REF / Reactome
        checked += 1
        if norm(quote) not in norm(text):
            problems.append(f"[C] NOT VERBATIM at {path} [{ref}]: {quote[:110]!r}")
            continue
        # A `file:` quote into the UniProt flat file must be on ONE physical line:
        # a quote spanning a `CC       ` continuation is skipped by the repo
        # validator and so passes silently while being unquotable in reality.
        if ref.startswith("file:") and p == UNIPROT_FLATFILE:
            if not any(quote in ln for ln in text.splitlines()):
                problems.append(
                    f"[C] at {path}: quote is not on ONE physical line of "
                    f"{p.name} -- `file:` quotes are unvalidated by CI, so this would ship "
                    f"unnoticed: {quote[:90]!r}"
                )
        # Every quote must contain the entity its row is about, or say why not.
    if checked == 0:
        problems.append("[C] checked zero text-bearing quotes -- refusing a vacuous pass.")
    return checked


def check_d_coverage(data: dict, problems: list[str]) -> None:
    goa = read_goa_rows()
    distinct = {(r["go_id"], r["evidence"], r["reference"], r["with_from"], r["qualifier"])
                for r in goa}
    anns = data["existing_annotations"]
    new_rows = [a for a in anns if a["review"]["action"] == "NEW"]
    reviewed = [a for a in anns if a["review"]["action"] != "NEW"]
    if len(reviewed) != len(distinct):
        problems.append(
            f"[D] {len(reviewed)} non-NEW annotations against {len(distinct)} distinct GOA "
            f"rows ({len(goa)} raw lines). The fetch-gene stub collapses GO:0005515 rows that "
            "differ only in WITH/FROM, so this must be reconciled against the TSV."
        )
    # Every distinct GOA row must be represented, matched on the stable fields.
    have = collections.Counter(
        (a["term"]["id"], a["evidence_type"], _ref(a), _wf(a), a.get("qualifier", ""))
        for a in reviewed
    )
    want = collections.Counter(distinct)
    missing = want - have
    extra = have - want
    if missing or extra:
        problems.append(
            f"[D] GOA row set mismatch. missing from review: {sorted(missing)}; "
            f"present but not in GOA: {sorted(extra)}"
        )
    if not new_rows:
        problems.append("[D] no NEW rows -- expected the review's own proposals to be present.")


def _ref(a: dict) -> str:
    r = a.get("original_reference_id")
    return r if isinstance(r, str) else (r or {}).get("id", "")


def _wf(a: dict) -> str:
    return "|".join(a.get("supporting_entities") or [])


def check_e_source_entities(data: dict, problems: list[str]) -> None:
    """source_entities in propagation_review must equal the GOA WITH/FROM token set.

    Built from the GOA field, so counts match by construction; asserted on
    membership because a matching count is not a matching set. Presence is
    asserted too, so deleting an entity cannot make the check pass silently.
    """
    goa = read_goa_rows()
    by_key = {}
    for r in goa:
        by_key[(r["go_id"], r["evidence"], r["reference"], r["with_from"], r["qualifier"])] = r
    propagated = {"IBA", "ISS", "IEA", "ISO", "IBD"}
    n_checked = 0
    for a in data["existing_annotations"]:
        if a["review"]["action"] == "NEW":
            continue
        if a["evidence_type"] not in propagated:
            continue
        key = (a["term"]["id"], a["evidence_type"], _ref(a), _wf(a), a.get("qualifier", ""))
        row = by_key.get(key)
        if row is None:
            problems.append(f"[E] no GOA row matches propagated annotation {key}")
            continue
        expected = {t for t in row["with_from"].split("|") if t}
        pr = a["review"].get("propagation_review")
        if pr is None:
            problems.append(
                f"[E] {a['term']['id']} {a['evidence_type']}: propagated row with no "
                "propagation_review"
            )
            continue
        ents = pr.get("source_entities")
        if not ents:
            problems.append(
                f"[E] {a['term']['id']} {a['evidence_type']}: propagation_review has no "
                "source_entities -- a guard that only validates on match passes when the "
                "list is deleted, so presence is asserted."
            )
            continue
        got = {e["source_id"] for e in ents}
        if got != expected:
            problems.append(
                f"[E] {a['term']['id']} {a['evidence_type']}: source_entities != GOA WITH/FROM. "
                f"missing {sorted(expected - got)}, unexpected {sorted(got - expected)}"
            )
        n_checked += 1
    if n_checked == 0:
        problems.append("[E] checked zero propagated rows -- refusing a vacuous pass.")


def check_f_summary_openers(data: dict, problems: list[str]) -> None:
    n = 0
    for a in data["existing_annotations"]:
        action = a["review"]["action"]
        summary = a["review"].get("summary", "")
        opener = norm(summary)[:60]
        expected = ACTION_OPENERS.get(action)
        if expected is None:
            problems.append(f"[F] no expected opener registered for action {action}")
            continue
        if not any(opener.startswith(e) for e in expected):
            problems.append(
                f"[F] {a['term']['id']} {a['evidence_type']}: action is {action} but the summary "
                f"opens {opener!r}. The opener is the first thing a reader sees, and a stale "
                "opener after an action change is this campaign's most repeated defect."
            )
        n += 1
    if n == 0:
        problems.append("[F] checked zero summaries -- refusing a vacuous pass.")


def _core_function_terms(data: dict) -> dict[str, list[str]]:
    """{go_id: [slot, ...]} over every slot a Term can occupy in core_functions."""
    out: dict[str, list[str]] = collections.defaultdict(list)
    for cf in data.get("core_functions") or []:
        for slot in CORE_FUNCTION_TERM_SLOTS:
            v = cf.get(slot)
            if v is None:
                continue
            items = v if isinstance(v, list) else [v]
            for t in items:
                out[t["id"]].append(slot)
        # Fail loudly if a NEW slot appears that this sweep does not know about.
        unknown = set(cf) - set(CORE_FUNCTION_TERM_SLOTS) - {"description", "supported_by"}
        if unknown:
            out.setdefault("__unknown_slots__", []).extend(sorted(unknown))
    return out


def check_g_core_functions(data: dict, problems: list[str]) -> None:
    cf_terms = _core_function_terms(data)
    if "__unknown_slots__" in cf_terms:
        problems.append(
            f"[G] core_functions carries slot(s) this sweep does not enumerate: "
            f"{sorted(set(cf_terms['__unknown_slots__']))}. Add them to "
            "CORE_FUNCTION_TERM_SLOTS -- an unswept slot is an unchecked assertion."
        )
        del cf_terms["__unknown_slots__"]
    if not cf_terms:
        problems.append("[G] core_functions asserts no terms -- refusing a vacuous pass.")
        return

    # Direction 1: every core_functions term must be backed by a row.
    backing: dict[str, set[str]] = collections.defaultdict(set)
    for a in data["existing_annotations"]:
        action = a["review"]["action"]
        backing[a["term"]["id"]].add(action)
        for rt in a["review"].get("proposed_replacement_terms") or []:
            backing[rt["id"]].add(f"{action}->replacement")
    ok_actions = {"ACCEPT", "KEEP_AS_NON_CORE", "NEW", "MODIFY->replacement"}
    for term, slots in cf_terms.items():
        acts = backing.get(term, set())
        if not (acts & ok_actions):
            problems.append(
                f"[G] core_functions asserts {term} (slots {slots}) but no annotation row "
                f"supports it (row actions: {sorted(acts) or 'none'})."
            )

    # Direction 2 -- the one that would otherwise go unwritten. Every ACCEPT or NEW
    # row's term must either appear in core_functions or its reason must ADDRESS its
    # absence. "Unwritten is not the same as passing."
    #
    # The trigger is the literal field name `core_functions`, not a list of accepted
    # phrasings. A phrase whitelist is a paraphrase trap: the first legitimate
    # rewording fails it (this check rejected "deliberately absent from
    # core_functions" while it pinned five other spellings). A field name is a stable
    # token and does not get reworded.
    #
    # LIMITATION, stated rather than implied: this verifies that the reason *addresses*
    # core_functions membership, not that the argument it gives is sound. Judging the
    # argument is a reading task and no string check can do it.
    n = 0
    for a in data["existing_annotations"]:
        action = a["review"]["action"]
        if action not in ("ACCEPT", "NEW"):
            continue
        term = a["term"]["id"]
        if term == "GO:0005515":
            continue  # bare protein binding is never a core function by policy
        n += 1
        if term in cf_terms:
            continue
        reason = norm(a["review"].get("reason", ""))
        if "core_functions" not in reason:
            problems.append(
                f"[G] {term} has action {action} but is absent from core_functions and its "
                "reason never mentions core_functions, so the omission is unexplained."
            )
    if n == 0:
        problems.append("[G] direction 2 examined zero rows -- refusing a vacuous pass.")


def check_h_hedge_sweep(data: dict, problems: list[str]) -> None:
    """For every claim the review declines in prose, confirm no structured slot
    states it flatly. Enumerates ALL slots, not only the molecular-function ones:
    a location is as much an assertion as an activity."""
    cf_terms = _core_function_terms(data)
    cf_terms.pop("__unknown_slots__", None)
    n = 0
    for term, why in DECLINED_TERMS.items():
        n += 1
        if term in cf_terms:
            problems.append(
                f"[H] {term} appears in core_functions slots {cf_terms[term]} but the review "
                f"declines it: {why}"
            )
        # It must also not appear as a proposed replacement term or a proposed new term.
        for a in data["existing_annotations"]:
            for rt in a["review"].get("proposed_replacement_terms") or []:
                if rt["id"] == term:
                    problems.append(
                        f"[H] {term} is proposed as a replacement on {a['term']['id']} but the "
                        f"review declines it: {why}"
                    )
        for pt in data.get("proposed_new_terms") or []:
            pp = pt.get("proposed_parent") or {}
            if pp.get("id") == term and term == "GO:0030332":
                problems.append(
                    f"[H] {term} is used as a proposed_parent, but the review argues it is "
                    "inapplicable; the request must not hang off it."
                )
    if n == 0:
        problems.append("[H] swept zero declined terms -- refusing a vacuous pass.")
    # And the specific inversion this gene invites: the complex's activity must be
    # recorded as a contribution, never as AFF4's own molecular_function.
    for cf in data.get("core_functions") or []:
        mf = (cf.get("molecular_function") or {}).get("id")
        if mf == "GO:0003711":
            problems.append(
                "[H] GO:0003711 transcription elongation factor activity is asserted as AFF4's "
                "own molecular_function. The review argues throughout that this activity belongs "
                "to the complex and AFF4 contributes to it; it must sit in "
                "contributes_to_molecular_function."
            )


"""Subject tokens that make a quote about THIS gene rather than about something else."""
SUBJECT_TOKENS = (r"\bAFF4\b", r"\bAff4\b", r"\bMCEF\b", r"\bAF5q31\b", r"\bAF4\b")

# Rows whose quotes deliberately do NOT name AFF4, with the reason. Each is a case where
# naming a different entity IS the evidence, so a blanket rule would be wrong -- but the
# exemption is enumerated per row rather than left to a global "usually fine".
SUBJECT_EXEMPT = {
    ("GO:0050877", "IBA"): "the whole point of the row is that the donor evidence is on "
                           "paralogues (mouse Aff2/Fmr2 and Drosophila lilli), not on AFF4",
    ("GO:0034976", "IEA"): "the whole point of the row is that the donor's reference is a "
                           "genipin/lung-injury study in which Aff4 is not the subject",
}


def check_i_quote_subject(data: dict, problems: list[str]) -> None:
    """Every quote must name the entity its row is about.

    Verbatim is not the same as relevant, and nothing else in this repo checks it. Two
    refinements that cost a round elsewhere are built in:
      * on a MODIFY row the subject is the **proposed replacement**, not the term the row
        is moving away from;
      * a quote may instead name the row's **interaction partner**, since a partner-naming
        sentence is exactly what a protein-binding row needs.
    Quotes into the computed audit artifact are exempt: those rows carry accessions and
    GO ids rather than symbols, by design.
    """
    n_rows = 0
    for a in data["existing_annotations"]:
        key = (a["term"]["id"], a["evidence_type"])
        partners = []
        for e in a.get("extensions") or []:
            lab = (e.get("term") or {}).get("label", "")
            partners += [w for w in re.split(r"[ /()]+", lab) if len(w) > 2]
        pmid_quotes = [sb for sb in a["review"].get("supported_by") or []
                       if sb["reference_id"].startswith("PMID:")]
        if not pmid_quotes:
            continue
        n_rows += 1

        def names_subject(q: str) -> bool:
            return (any(re.search(pat, q) for pat in SUBJECT_TOKENS)
                    or any(pr in q for pr in partners))

        # The gate is PER ROW: the ADPRS defect was a row whose evidence was entirely
        # about a different subject. A per-QUOTE rule would reject legitimate contextual
        # quotes (a sentence establishing that the compartment belongs to polymerase I,
        # say) and a guard that forbids legitimate practice gets worked around, not obeyed.
        if not any(names_subject(sb["supporting_text"]) for sb in pmid_quotes):
            if key not in SUBJECT_EXEMPT:
                problems.append(
                    f"[I] {key[0]} {key[1]} ({a['review']['action']}): not one of its "
                    f"{len(pmid_quotes)} PMID quotes names AFF4 or the row's partner "
                    f"{partners or '(none)'}, and the row is not an enumerated exemption."
                )
        # Contextual quotes that name neither are reported but do not fail, EXCEPT that a
        # quote from an abstract-only cache must say so, otherwise it reads as evidence
        # about the gene when the gene-specific data are in text we do not have.
        for sb in pmid_quotes:
            if names_subject(sb["supporting_text"]) or key in SUBJECT_EXEMPT:
                continue
            _, src = source_text(sb["reference_id"])
            abstract_only = re.search(r"^full_text_available:\s*false", src, re.M) is not None
            if abstract_only and not sb.get("full_text_unavailable"):
                problems.append(
                    f"[I] {key[0]} {key[1]}: contextual quote from {sb['reference_id']} names "
                    "neither AFF4 nor the partner and comes from an abstract-only cache, but "
                    "carries no full_text_unavailable flag -- the limitation must be stated."
                )
    if n_rows == 0:
        problems.append("[I] examined zero rows with PMID quotes -- refusing a vacuous pass.")


# References whose cache has a `## Full Text` body that does NOT invalidate the
# `full_text_unavailable` flag, each with the reason it was inspected and allowed. An
# enumerated exception, not a size threshold: length is not a proxy for content.
FULLTEXT_FLAG_EXEMPT = {
    "PMID:22190034": "body is the abstract restated plus a Methods Summary, with no results "
                     "section and no mention of AFF4, ELL2, P-TEFb, CDK9 or the super "
                     "elongation complex -- inspected, not inferred from its length",
}


def check_j_fulltext_flags(data: dict, problems: list[str]) -> None:
    """Every ``full_text_unavailable: true`` must agree with the cache BODY, not the
    cache's own frontmatter flag.

    This review shipped an instance of the harm: `PMID:32257529`'s frontmatter reads
    ``full_text_available: false`` while the body twenty lines below states the whole
    correction, and five surfaces of this review consequently asserted that the erratum's
    scope could not be established. PR #2287 removed 80 such stale flags across the corpus
    for exactly this reason -- the flag suppresses the extraction the annotation needs.
    So the flag is never the authority; the body is.
    """
    seen = 0

    def bodies(ref: str) -> int:
        if not ref.startswith("PMID:"):
            return 0
        _, txt = source_text(ref)
        if "## Full Text" not in txt:
            return 0
        return len(txt.split("## Full Text", 1)[1].strip())

    def flagged(ref: str, where: str) -> None:
        nonlocal seen
        seen += 1
        n = bodies(ref)
        if n < 200 or ref in FULLTEXT_FLAG_EXEMPT:
            return
        problems.append(
            f"[J] {where} marks {ref} full_text_unavailable, but its cache has a "
            f"{n}-character `## Full Text` body. Read the body before flagging -- the "
            "frontmatter flag is the unreliable half of the file. If the body is a junk or "
            "partial extraction, add the reference to FULLTEXT_FLAG_EXEMPT with the reason."
        )

    for r in data.get("references") or []:
        if r.get("full_text_unavailable"):
            flagged(r["id"], f"references[{r['id']}]")

    def walk(node):
        if isinstance(node, dict):
            for k, v in node.items():
                if k in ("supported_by", "provenance", "findings") and isinstance(v, list):
                    for e in v:
                        if isinstance(e, dict) and e.get("full_text_unavailable"):
                            flagged(e["reference_id"], f"{k} entry")
                walk(v)
        elif isinstance(node, list):
            for e in node:
                walk(e)

    walk(data)
    if seen == 0:
        problems.append("[J] examined zero full_text_unavailable flags -- refusing a vacuous pass.")


def audit(text: str | None = None) -> list[str]:
    problems: list[str] = []
    data, raw = load_review(text)  # check A: raises on duplicate keys / anchors
    check_b_raw_vs_parsed(data, raw, problems)
    check_c_quotes(data, problems)
    check_d_coverage(data, problems)
    check_e_source_entities(data, problems)
    check_f_summary_openers(data, problems)
    check_g_core_functions(data, problems)
    check_h_hedge_sweep(data, problems)
    check_i_quote_subject(data, problems)
    check_j_fulltext_flags(data, problems)
    return problems


# --------------------------------------------------------------------------- #
# Break-tests. Each asserts, in order: the mutation APPLIED (changed something),
# the guard FIRED, and the failure MESSAGE is the expected one.
# --------------------------------------------------------------------------- #

def _expect_problem(mutated: str, tag: str, needle: str, what: str) -> None:
    baseline = REVIEW.read_text()
    assert mutated != baseline, f"{what}: mutation changed NOTHING -- the break-test is a no-op."
    try:
        problems = audit(mutated)
    except AuditError as e:
        if tag not in str(e) and needle.lower() not in str(e).lower():
            raise AssertionError(f"{what}: raised, but with the wrong message: {e}")
        print(f"  ok   {what}  (raised, matched)")
        return
    hits = [p for p in problems if p.startswith(tag) and needle.lower() in p.lower()]
    if not hits:
        raise AssertionError(
            f"{what}: guard did NOT fire.\n  wanted {tag} containing {needle!r}\n"
            f"  got: {problems}"
        )
    print(f"  ok   {what}  ({hits[0][:100]}...)")


def _expect_raise(mutated: str, needle: str, what: str) -> None:
    baseline = REVIEW.read_text()
    assert mutated != baseline, f"{what}: mutation changed NOTHING -- the break-test is a no-op."
    try:
        audit(mutated)
    except AuditError as e:
        if needle.lower() not in str(e).lower():
            raise AssertionError(
                f"{what}: raised for the WRONG reason.\n  wanted {needle!r}\n  got: {e}")
        print(f"  ok   {what}  (raised, matched {needle!r})")
        return
    raise AssertionError(f"{what}: did not raise.")


def self_test() -> int:
    print("break-tests (each: mutation applied -> guard fired -> expected message)")
    base = REVIEW.read_text()
    clean = audit(base)
    if clean:
        print("  !! the CURRENT file has problems; fix them before trusting the break-tests:")
        for p in clean:
            print("     ", p)
        return 1
    print("  ok   the current file is clean (precondition)")

    # A. duplicate mapping key destroys data on parse.
    anchor = "  evidence_type: IBA\n  original_reference_id: GO_REF:0000033\n"
    assert anchor in base, "fixture drifted: duplicate-key anchor not found"
    _expect_raise(base.replace(anchor, anchor + "  evidence_type: IDA\n", 1),
                  "duplicate mapping key",
                  "A: strict loader rejects a duplicate mapping key")

    # A. YAML anchors multiply data.
    _expect_raise(base.replace("existing_annotations:\n- term:",
                               "existing_annotations:\n- &id001\n  term:", 1),
                  "yaml anchors",
                  "A: loader rejects YAML anchors")

    # B/C. a quote that is not verbatim in its source.
    quote = "Without Tat, AFF4 can mediate the ELL2-P-TEFb interaction, albeit"
    assert quote in base, "fixture drifted: the verbatim quote anchor is gone"
    _expect_problem(base.replace(quote, "Without Tat, AFF4 cannot mediate the ELL2-P-TEFb bond, albeit", 1),
                    "[C]", "not verbatim",
                    "C: a non-verbatim quote is caught")

    # C. a `file:` UniProt quote broken across a CC continuation.
    #    Assert the mutation is real: the spanning form must be absent from the flat file.
    #    The fixture must be whitespace-normalised-PRESENT (so it reaches the
    #    one-physical-line check rather than failing the verbatim check first), which
    #    means it has to carry the `CC` continuation marker the flat file interposes.
    #    A mutation coarser than that would not discriminate between the two checks.
    spanning = ("SUBUNIT: Component of the super elongation complex (SEC), at least "
                "CC composed of EAF1")
    flat = UNIPROT_FLATFILE.read_text()
    assert spanning not in flat, "fixture drifted: the spanning quote is on one line after all"
    assert norm(spanning) in norm(flat), \
        "fixture drifted: the spanning quote is not even whitespace-normalised-present, so it " \
        "would fail the verbatim check instead of the one-physical-line check"
    old = "      supporting_text: 'SIMILARITY: Belongs to the AF4 family. {ECO:0000305}.'"
    assert old in base, "fixture drifted: the file: quote anchor is gone"
    _expect_problem(base.replace(old, f"      supporting_text: '{spanning}'", 1),
                    "[C]", "one physical line",
                    "C: a file: quote crossing a CC continuation is caught")

    # D. deleting a whole annotation must break coverage against the TSV.
    first = base.index("- term:\n    id: GO:0003712")
    second = base.index("- term:\n    id: GO:0006354")
    dropped = base[:first] + base[second:]
    _expect_problem(dropped, "[D]", "distinct goa rows",
                    "D: dropping an annotation breaks TSV coverage")

    # E. deleting a source_entities list must fire (not pass silently).
    ent = ("      - source_id: UniProtKB:P51825\n"
           "        source_label: human AFF1\n"
           "        source_status: SUPPORTS_TRANSFER\n"
           "        comment: Holds GO:0006354 by its own EXP annotation (PMID:22547686).\n")
    assert ent in base, "fixture drifted: source_entities anchor not found"
    _expect_problem(base.replace(ent, "", 1), "[E]", "source_entities != goa with/from",
                    "E: a removed source entity is caught by set comparison")

    # F. a summary opener that names the wrong action.
    opener = "      Kept as non-core. Both donor experiments"
    assert opener in base, "fixture drifted: summary opener anchor not found"
    _expect_problem(base.replace(opener, "      Accepted. Both donor experiments", 1),
                    "[F]", "opens",
                    "F: a summary opener contradicting its action is caught")

    # G direction 1: a core_functions term with no backing row.
    _expect_problem(base.replace("    id: GO:0042803\n    label: protein homodimerization activity\n  locations:",
                                 "    id: GO:0051082\n    label: unfolded protein binding\n  locations:", 1),
                    "[G]", "no annotation row supports it",
                    "G1: an unbacked core_functions term is caught")

    # G direction 2 -- the direction that would otherwise go unwritten: an ACCEPT
    # row absent from core_functions whose reason no longer justifies the absence.
    just = ("GO:0032968, so it is retained as correct and not separately restated "
            "in core_functions.")
    assert just in base, "fixture drifted: the G2 justification anchor is gone"
    mutated = base.replace(just, "GO:0032968, so it is retained as correct.", 1)
    assert "core_functions" not in mutated.split("- term:\n    id: GO:0005515")[0].split(
        "id: GO:0010468")[-1], "mutation did not actually remove the core_functions mention"
    _expect_problem(mutated, "[G]", "never mentions core_functions",
                    "G2: an ACCEPT row absent from core_functions with no explanation is caught")

    # H: a declined term asserted flatly in a structured slot -- and note the slot
    #    chosen is `locations`, which an MF-only sweep would have missed.
    loc = "  locations:\n  - id: GO:0005654\n    label: nucleoplasm\n  - id: GO:0000791\n    label: euchromatin"
    assert loc in base, "fixture drifted: the locations anchor is gone"
    _expect_problem(base.replace(loc, loc + "\n  - id: GO:0016604\n    label: nuclear body", 1),
                    "[H]", "declines it",
                    "H: a declined term asserted in `locations` is caught")

    # H: the inversion this gene invites -- the complex's activity claimed as AFF4's own.
    mf = ("  molecular_function:\n    id: GO:0030674\n    label: protein-macromolecule adaptor "
          "activity\n  contributes_to_molecular_function:\n    id: GO:0003711")
    assert mf in base, "fixture drifted: the MF/contributes_to anchor is gone"
    _expect_problem(base.replace(
        mf,
        "  molecular_function:\n    id: GO:0003711\n    label: transcription elongation factor "
        "activity\n  contributes_to_molecular_function:\n    id: GO:0003711", 1),
        "[H]", "belongs\nto the complex".replace("\n", " "),
        "H: GO:0003711 asserted as AFF4's own molecular_function is caught")

    # An unswept core_functions slot must fail loudly rather than go unchecked.
    global CORE_FUNCTION_TERM_SLOTS
    saved = list(CORE_FUNCTION_TERM_SLOTS)
    CORE_FUNCTION_TERM_SLOTS = [s for s in CORE_FUNCTION_TERM_SLOTS if s != "locations"]
    assert CORE_FUNCTION_TERM_SLOTS != saved, "fixture drifted: slot list unchanged"
    try:
        problems = audit(base)
        hits = [p for p in problems if p.startswith("[G]") and "does not enumerate" in p]
        assert hits, (
            "an unswept core_functions slot did NOT fire -- the sweep would silently stop "
            f"covering it. got: {problems}"
        )
        print(f"  ok   G/H: an unenumerated core_functions slot fails loudly ({hits[0][:80]}...)")
    finally:
        CORE_FUNCTION_TERM_SLOTS = saved
    assert not audit(base), "restore failed: the file is no longer clean"

    # I: a row all of whose PMID quotes name neither the gene nor its partner. The
    #    mutation must keep the quote VERBATIM in its source, so that check C stays
    #    silent and only check I can fire -- a mutation coarser than that (an invented
    #    quote) would be caught by a much weaker implementation and would not
    #    discriminate. A row with exactly ONE PMID quote is required, because the gate
    #    is per row.
    only_quote = """    - reference_id: PMID:25730767
      supporting_text: Transcriptome and chromatin immunoprecipitation sequencing (ChIP-seq)
        analyses demonstrated similar alterations of genome-wide binding of AFF4, cohesin
        and RNAP2 in CdLS and CHOPS syndrome.
- term:
    id: GO:0005654
    label: nucleoplasm
  evidence_type: TAS
  original_reference_id: Reactome:R-HSA-112379"""
    assert base.count(only_quote) == 1, "fixture drifted: the single-PMID-quote row anchor is gone"
    src = (REPO / "publications" / "PMID_25730767.md").read_text()
    replacement = "Transcriptional elongation is critical for gene expression regulation during"
    assert norm(replacement) in norm(src), (
        "fixture drifted: the substitute quote is not verbatim in PMID:25730767, so check C "
        "would fire instead of check I and the test would not discriminate")
    assert not any(re.search(pat, replacement) for pat in SUBJECT_TOKENS), \
        "fixture drifted: the substitute quote names AFF4, so check I could not fire"
    mutated = base.replace(only_quote, only_quote.replace(
        """supporting_text: Transcriptome and chromatin immunoprecipitation sequencing (ChIP-seq)
        analyses demonstrated similar alterations of genome-wide binding of AFF4, cohesin
        and RNAP2 in CdLS and CHOPS syndrome.""",
        f"supporting_text: {replacement}"), 1)
    got = audit(mutated)
    assert not [x for x in got if x.startswith("[C]")], (
        f"the mutation also tripped check C, so this test does not isolate check I: {got}")
    _expect_problem(mutated, "[I]", "names AFF4 or the row's partner",
                    "I: a row whose only PMID quote names neither gene nor partner is caught")

    # J: a full_text_unavailable flag on a reference whose cache body states the very
    #    thing the review would otherwise call unknowable. The mutation must target the
    #    erratum specifically, because that is the reference the defect actually shipped on.
    era = """- id: PMID:32257529
  title: 'Correction to: AFF1 and AFF4 differentially regulate the osteogenic differentiation
    of human MSCs.'
  publication_type: COMMENT_EDITORIAL"""
    assert base.count(era) == 1, "fixture drifted: the erratum reference anchor is gone"
    _, ertxt = source_text("PMID:32257529")
    assert "## Full Text" in ertxt and len(ertxt.split("## Full Text", 1)[1].strip()) >= 200, (
        "fixture drifted: PMID:32257529's cache no longer has a full-text body, so this "
        "break-test would pass vacuously")
    assert "PMID:32257529" not in FULLTEXT_FLAG_EXEMPT, \
        "fixture drifted: the erratum is exempted, so check J could not fire on it"
    _expect_problem(base.replace(era, era + "\n  full_text_unavailable: true", 1),
                    "[J]", "character `## Full Text` body",
                    "J: a full_text_unavailable flag contradicted by the cache body is caught")

    print("all break-tests passed")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args()
    if a.self_test:
        return self_test()
    problems = audit()
    if problems:
        print(f"{len(problems)} problem(s):")
        for p in problems:
            print("  -", p)
        return 1
    data, text = load_review()
    print(f"OK: {len(data['existing_annotations'])} annotations, "
          f"{len(quote_entries(data))} quotes, no problems.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
