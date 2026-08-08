#!/usr/bin/env python3
"""Invariants for the ADIPOQ review, run over the EMITTED artifacts.

Deliberately runs over `ADIPOQ-ai-review.yaml`, `ADIPOQ-notes.md`, `RESULTS.md`
and `results.json` -- **not** over `build_review.py`.  A detector that inspects
the generator cannot see the text that ships: a sentence contiguous in the
Python source is line-wrapped by the YAML dumper.  Every phrase check therefore
normalises whitespace first.

Checks
------
A  coverage          every GOA row has an entry; entries == rows + NEW
B  no anchors        no YAML anchor/alias (aliases multiply quotes on parse)
C  no duplicate keys strict loader; PyYAML silently keeps the last of a repeat
D  quotes verbatim   EVERY supporting_text, including the `provenance` entries
                     that checkquotes.py does not walk
E  action/prose      no summary opener names an action other than the row's own
F  propagation       every IBA/ISS/IEA row with REMOVE or MARK_AS_OVER_ANNOTATED
                     carries a propagation_review, and every propagation_review
                     names sources that exist in that row's GOA WITH/FROM
G  core_functions    every core_functions term is backed by an ACCEPT/NEW/MODIFY
                     row (the direction that would otherwise go unwritten)
H  numbers agree     the load-bearing counts in RESULTS.md and the notes match
                     results.json
I  retracted claims  withdrawn/incorrect phrasings must not reappear

Run:  uv run python audit_review.py [--self-test]

LIMITATION, stated rather than implied: check I matches fixed phrases and
cannot catch a paraphrase.  Prose surfaces still need re-reading when a claim
is withdrawn.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
GENE_DIR = HERE.parent
REPO = GENE_DIR.parents[2]

REVIEW = GENE_DIR / "ADIPOQ-ai-review.yaml"
NOTES = GENE_DIR / "ADIPOQ-notes.md"
RESULTS_MD = HERE / "RESULTS.md"
RESULTS_JSON = HERE / "results.json"
GOA_TSV = GENE_DIR / "ADIPOQ-goa.tsv"

PROPAGATED = {"IBA", "ISS", "IEA", "ISO", "ISM", "ISA", "RCA"}
NEEDS_PROP = {"REMOVE", "MARK_AS_OVER_ANNOTATED"}

ACTION_WORDS = {
    "ACCEPT": ["accept"],
    "REMOVE": ["remov"],
    "MODIFY": ["modif"],
    "KEEP_AS_NON_CORE": ["non-core"],
    "MARK_AS_OVER_ANNOTATED": ["over-annot", "overannot"],
    "NEW": ["newly propose"],
}

# Phrasings that were considered and withdrawn during the review.  See the
# "Things I checked and got wrong" section of ADIPOQ-notes.md.
WITHDRAWN = [
    # GO:0038002 was briefly both KEEP_AS_NON_CORE and a core function
    "endocrine signaling is non-core",
    # the six cytosol-only partners were briefly presented as a total
    "all partners are cytosolic",
    # T-cadherin was briefly going to be annotated with GO:0045296
    "propose go:0045296 for t-cadherin",
    # FALSE ancestry claim that reached the shipped YAML: GO:0048018 is in the
    # activity branch (under GO:0140677), NOT under GO:0005102.  See RESULTS.md
    # section F and term_relations in results.json.
    "descendant of go:0048018 receptor ligand activity, which is a descendant",
    "go:0048018 is a descendant of go:0005102",
]

# A withdrawn phrase may be restated when it is being retracted.  One of these
# cues must appear shortly before it.
RETRACTION_CUES = {"withdrawn", "false", "first draft", "retract", "corrected",
                   "was wrong", "does not exist"}
RETRACTION_WINDOW = 400

REQUIRED_CLAIMS = {
    # claim -> minimum number of surfaces (files) it must appear on
    "self-referential": 2,
    "cross-product": 2,
    # the correction must stay stated, not merely be absent
    "go:0005102 is not among go:0005179": 1,
}


def norm(t: str) -> str:
    return re.sub(r"\s+", " ", t).strip().lower()


def read_goa() -> list[dict]:
    if not GOA_TSV.exists():
        raise SystemExit(f"missing {GOA_TSV}; run `just fetch-gene human ADIPOQ`")
    lines = GOA_TSV.read_text().splitlines()
    hdr = lines[0].split("\t")
    return [dict(zip(hdr, ln.split("\t"))) for ln in lines[1:] if ln.strip()]


class Strict(yaml.SafeLoader):
    pass


def _no_dupes(loader, node, deep=False):
    m = {}
    for k, v in node.value:
        key = loader.construct_object(k, deep=deep)
        if key in m:
            raise ValueError(
                f"duplicate key {key!r} at line {k.start_mark.line + 1}")
        m[key] = loader.construct_object(v, deep=deep)
    return m


Strict.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _no_dupes)


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
    return p.read_text() if p.exists() else ""


def audit(raw: str, doc: dict, notes: str, results_md: str,
          rj: dict) -> list[str]:
    problems: list[str] = []
    rows = read_goa()
    anns = doc.get("existing_annotations")

    # --- A. coverage --------------------------------------------------------
    if not anns:
        problems.append("A: existing_annotations missing or empty -- "
                        "every later check would pass vacuously")
        return problems
    n_new = sum(1 for a in anns if a["review"].get("action") == "NEW")
    n_from_goa = len(anns) - n_new
    if n_from_goa != len(rows):
        problems.append(
            f"A: {n_from_goa} GOA-derived entries but {len(rows)} GOA rows "
            f"({len(anns)} entries, {n_new} NEW). NOTE: n_new is derived from "
            "the same document, so this arithmetic alone cannot detect a "
            "deleted NEW row -- check G is what catches that.")
    # per-row presence, keyed on the stable entity (term+evidence+reference),
    # not on any conclusion wording
    have = {(a["term"]["id"], a.get("evidence_type"),
             a.get("original_reference_id")) for a in anns}
    for r in rows:
        k = (r["GO TERM"], r["GO EVIDENCE CODE"], r["REFERENCE"])
        if k not in have:
            problems.append(f"A: GOA row not reviewed: {k}")

    # --- B/C. anchors and duplicate keys ------------------------------------
    if re.search(r"&id\d+", raw):
        problems.append("B: YAML anchor present; rows share objects and quote "
                        "counts are inflated")
    if re.search(r"\*id\d+", raw):
        problems.append("B: YAML alias present")
    # C is enforced by the Strict loader at call site

    # --- D. quotes verbatim, including provenance ---------------------------
    quotes: list[tuple[str, str, str]] = []

    def walk(n, path=""):
        if isinstance(n, dict):
            if "supporting_text" in n and "reference_id" in n:
                quotes.append((path, n["reference_id"], n["supporting_text"]))
            for k, v in n.items():
                walk(v, f"{path}.{k}")
        elif isinstance(n, list):
            for i, e in enumerate(n):
                walk(e, f"{path}[{i}]")

    walk(doc)
    raw_n = len(re.findall(r"^\s*(?:-\s*)?supporting_text:", raw, re.M))
    if raw_n != len(quotes):
        problems.append(
            f"D: raw supporting_text keys={raw_n} but parsed={len(quotes)} -- "
            "derive the expected number independently, do not rationalise")
    for path, ref, q in quotes:
        src = source_text(ref)
        if src is None:
            continue
        if src == "":
            problems.append(f"D: missing source {ref} ({path})")
        elif norm(q) not in norm(src):
            problems.append(f"D: not verbatim {ref} ({path}): {q[:70]!r}")
    if not any(".provenance" in p for p, _, _ in quotes):
        problems.append("D: no provenance quotes found; this check exists "
                        "because checkquotes.py cannot see them, so an empty "
                        "result means the walker is broken or they were dropped")

    # --- E. summary opener vs action ---------------------------------------
    for i, a in enumerate(anns):
        act = a["review"].get("action")
        if not act:
            problems.append(f"E: entry {i} has no action -- vacuous pass")
            continue
        opener = norm(a["review"].get("summary", "")).split(".")[0]
        for other, pats in ACTION_WORDS.items():
            if other == act:
                continue
            for pat in pats:
                if pat in opener:
                    problems.append(
                        f"E: {a['term']['id']} action={act} but summary opener "
                        f"names {other}: {opener[:70]!r}")

    # --- F. propagation_review ---------------------------------------------
    wf_by_key: dict[tuple, set[str]] = {}
    for r in rows:
        wf_by_key.setdefault(
            (r["GO TERM"], r["GO EVIDENCE CODE"], r["REFERENCE"]), set()
        ).update(t for t in r["WITH/FROM"].split("|") if t)
    for a in anns:
        rev = a["review"]
        ev, act = a.get("evidence_type"), rev.get("action")
        pr = rev.get("propagation_review")
        if ev in PROPAGATED and act in NEEDS_PROP and not pr:
            problems.append(
                f"F: {a['term']['id']} {ev} {act} has no propagation_review")
        if pr:
            if not pr.get("root_cause"):
                problems.append(f"F: {a['term']['id']} propagation_review has "
                                "no root_cause")
            # a self-referential IBA must be NO_FAILURE_*, never CIRCULAR
            key = (a["term"]["id"], ev, a.get("original_reference_id"))
            wf = wf_by_key.get(key, set())
            if "UniProtKB:Q15848" in wf and pr.get("root_cause", "").startswith(
                    "EVIDENCE_CIRCULAR"):
                problems.append(
                    f"F: {a['term']['id']} is a self-referential IBA but is "
                    "classified CIRCULAR; that records a PAINT curator judging "
                    "the function core")
            # source_entities must be built FROM the GOA WITH/FROM field, not
            # by hand: hand-maintained lists have drifted on every gene that
            # tried it.  Only enforced where the row HAS a WITH/FROM.
            listed = {s.get("source_id")
                      for s in (pr.get("source_entities") or [])}
            if wf:
                if not listed:
                    problems.append(
                        f"F: {a['term']['id']} {ev} has WITH/FROM {sorted(wf)} "
                        "but propagation_review lists no source_entities")
                invented = listed - wf
                if invented:
                    problems.append(
                        f"F: {a['term']['id']} {ev} source_entities name "
                        f"{sorted(invented)}, absent from the GOA WITH/FROM "
                        f"{sorted(wf)}")
                dropped = wf - listed
                if dropped:
                    problems.append(
                        f"F: {a['term']['id']} {ev} source_entities omit "
                        f"{sorted(dropped)} from the GOA WITH/FROM")

    # --- G. core_functions backed by rows -----------------------------------
    backed = {a["term"]["id"] for a in anns
              if a["review"].get("action") in ("ACCEPT", "NEW", "MODIFY")}
    for a in anns:
        for t in a["review"].get("proposed_replacement_terms") or []:
            backed.add(t["id"])
    for i, cf in enumerate(doc.get("core_functions") or []):
        terms = []
        if cf.get("molecular_function"):
            terms.append(cf["molecular_function"]["id"])
        terms += [t["id"] for t in cf.get("directly_involved_in") or []]
        for t in terms:
            if t not in backed:
                problems.append(
                    f"G: core_functions[{i}] cites {t} with no ACCEPT/NEW/"
                    "MODIFY row or replacement term backing it")

    # --- H. numbers in prose match results.json -----------------------------
    rec = rj.get("goa_reconciliation") or {}
    ic = rj.get("intact_census") or {}
    expected = {
        "goa rows": (len(rows), [f"{len(rows)}"]),
        "collapse loss": (rec.get("collapse_loss"),
                          [str(rec.get("collapse_loss"))]),
        "intact interactions": (ic.get("intact_total_interactions"),
                                [str(ic.get("intact_total_interactions"))]),
        "huri interactions": (
            (ic.get("interactions_per_publication") or {}).get("32296183"),
            [str((ic.get("interactions_per_publication") or {}).get("32296183"))]),
        "ipi partners": (ic.get("goa_ipi_partners"),
                         [str(ic.get("goa_ipi_partners"))]),
        "two hybrid": (ic.get("n_two_hybrid_interactions"),
                       [str(ic.get("n_two_hybrid_interactions"))]),
    }
    nnotes, nres = norm(notes), norm(results_md)
    for label, (val, pats) in expected.items():
        if val is None:
            problems.append(f"H: results.json has no value for {label}")
            continue
        if not any(p in nnotes for p in pats):
            problems.append(f"H: notes do not state {label}={val}")
        if not any(p in nres for p in pats):
            problems.append(f"H: RESULTS.md does not state {label}={val}")

    # --- I. withdrawn phrasings ---------------------------------------------
    surfaces = {"review YAML": norm(raw), "notes": nnotes,
                "RESULTS.md": nres}
    for name, text in surfaces.items():
        for w in WITHDRAWN:
            start = 0
            while True:
                i = text.find(w, start)
                if i < 0:
                    break
                start = i + len(w)
                # An ATTRIBUTED mention is legitimate and must not fire:
                # explaining why a claim was withdrawn requires restating it.
                # A guard that forbade this would be worked around, not obeyed.
                # The exception is deliberately narrow -- a retraction cue must
                # appear in the RETRACTION_WINDOW characters before the phrase.
                window = text[max(0, i - RETRACTION_WINDOW):i]
                if any(cue in window for cue in RETRACTION_CUES):
                    continue
                problems.append(
                    f"I: withdrawn phrasing {w!r} present in {name} with no "
                    "retraction cue nearby (an attributed mention needs one of "
                    f"{sorted(RETRACTION_CUES)} within {RETRACTION_WINDOW} chars)")
    for claim, min_surfaces in REQUIRED_CLAIMS.items():
        hits = sum(1 for t in surfaces.values() if claim in t)
        if hits < min_surfaces:
            problems.append(
                f"I: required claim {claim!r} appears on {hits} surface(s), "
                f"expected at least {min_surfaces}")
    return problems


def load_all():
    raw = REVIEW.read_text()
    doc = yaml.load(raw, Loader=Strict)   # raises on duplicate keys
    return (raw, doc, NOTES.read_text(), RESULTS_MD.read_text(),
            json.loads(RESULTS_JSON.read_text()))


def self_test() -> int:
    """Break-test each check in the direction it exists to catch."""
    raw, doc, notes, res, rj = load_all()
    fails = []

    base = audit(raw, doc, notes, res, rj)
    if base:
        fails.append(f"baseline should be clean, got: {base}")

    def expect(name, needle, **kw):
        args = dict(raw=raw, doc=doc, notes=notes, results_md=res, rj=rj)
        args.update(kw)
        got = audit(**args)
        if not any(needle in g for g in got):
            fails.append(f"{name}: expected {needle!r}, got {got[:3]}")

    import copy

    # A: drop a GOA-derived entry (the direction A exists to catch)
    d = copy.deepcopy(doc)
    i = next(i for i, a in enumerate(d["existing_annotations"])
             if a["review"]["action"] != "NEW")
    d["existing_annotations"].pop(i)
    expect("A-drop", "GOA-derived entries but", doc=d)
    expect("A-drop-row", "GOA row not reviewed", doc=d)
    # A: deleting the NEW row must still be caught -- by G, not by arithmetic
    d = copy.deepcopy(doc)
    d["existing_annotations"] = [a for a in d["existing_annotations"]
                                 if a["review"]["action"] != "NEW"]
    expect("A-drop-new", "with no ACCEPT/NEW/MODIFY row", doc=d)
    # A: empty must fail loudly, not pass vacuously
    d = copy.deepcopy(doc); d["existing_annotations"] = []
    expect("A-empty", "vacuous", doc=d)
    # B: anchor in raw text
    expect("B-anchor", "YAML anchor present", raw=raw + "\n# &id001\n")
    # D: raw/parsed mismatch
    expect("D-count", "raw supporting_text keys",
           raw=raw + "\n  supporting_text: injected\n")
    # D: non-verbatim quote
    d = copy.deepcopy(doc)
    for a in d["existing_annotations"]:
        sb = a["review"].get("supported_by")
        if sb:
            sb[0]["supporting_text"] = "this sentence appears in no paper at all"
            break
    expect("D-verbatim", "not verbatim", doc=d)
    # E: opener naming the wrong action
    d = copy.deepcopy(doc)
    for a in d["existing_annotations"]:
        if a["review"]["action"] == "ACCEPT":
            a["review"]["summary"] = "Removed because it is wrong."
            break
    expect("E-prose", "summary opener names", doc=d)
    # E: missing action
    d = copy.deepcopy(doc); d["existing_annotations"][0]["review"].pop("action")
    expect("E-noaction", "no action", doc=d)
    # F: strip a required propagation_review
    d = copy.deepcopy(doc)
    hit = False
    for a in d["existing_annotations"]:
        if (a.get("evidence_type") in PROPAGATED
                and a["review"]["action"] in NEEDS_PROP
                and a["review"].get("propagation_review")):
            a["review"].pop("propagation_review"); hit = True; break
    if not hit:
        fails.append("F: no row to mutate -- the guard is untested")
    else:
        expect("F-strip", "has no propagation_review", doc=d)
    # F: invented source entity
    d = copy.deepcopy(doc)
    for a in d["existing_annotations"]:
        pr = a["review"].get("propagation_review")
        if pr and pr.get("source_entities"):
            pr["source_entities"].append({"source_id": "UniProtKB:P99999"})
            break
    expect("F-invented", "absent from the GOA WITH/FROM", doc=d)
    # F: dropped source entity
    d = copy.deepcopy(doc)
    for a in d["existing_annotations"]:
        pr = a["review"].get("propagation_review")
        if pr and len(pr.get("source_entities") or []) > 1:
            pr["source_entities"].pop(); break
    expect("F-dropped", "source_entities omit", doc=d)

    # G: core function citing an unbacked term
    d = copy.deepcopy(doc)
    d["core_functions"][0]["directly_involved_in"].append(
        {"id": "GO:9999999", "label": "not backed by any row"})
    expect("G-unbacked", "with no ACCEPT/NEW/MODIFY row", doc=d)
    # H: prose number disagreeing with results.json
    expect("H-notes", "notes do not state", notes="nothing numeric here")
    # I: withdrawn phrasing
    expect("I-withdrawn", "withdrawn phrasing",
           notes=notes + "\n\nendocrine signaling is non-core\n")
    # attributed mention (retraction cue nearby) must NOT fire -- the happy
    # direction, which is the one guards usually get wrong
    got = audit(raw, doc,
                notes + "\n\nThis was withdrawn: endocrine signaling is "
                        "non-core.\n", res, rj)
    if any("endocrine signaling is non-core" in g for g in got):
        fails.append("I-attributed: an attributed mention fired; the guard "
                     "would be worked around rather than obeyed")
    # I: required claim missing from enough surfaces
    expect("I-required", "required claim", notes="", results_md="")

    for f in fails:
        print("SELF-TEST FAIL:", f)
    print(f"self-test: {'OK' if not fails else str(len(fails)) + ' failure(s)'}")
    return 1 if fails else 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    if args.self_test:
        return self_test()
    problems = audit(*load_all())
    for p in problems:
        print("PROBLEM:", p)
    print(f"\n{len(problems)} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
