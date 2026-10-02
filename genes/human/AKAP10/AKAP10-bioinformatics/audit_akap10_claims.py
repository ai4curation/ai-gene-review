#!/usr/bin/env python3
"""Invariant checks over the AKAP10 review, plus a self-test that tries to break them.

Why this exists
---------------
Every mechanical gate in this repo validates a quote against its *source*. None
validates the review against its own arithmetic, and none notices when a claim the
review explicitly retracted creeps back in at a site nobody re-read. Both failure
modes have cost this campaign whole rounds.

The checks are written over the *class* of error rather than a hand-enumerated list
of sites, because a list of instances can always be one short (AHI1 found exactly
that, twice, one level apart).

Two families of check:

1. **Arithmetic** - every count asserted in the PR body is re-derived from the file,
   and each GOA row is matched to an `existing_annotations` entry by
   (term, evidence, reference, with/from), so coverage cannot silently drift.
2. **Claims** - terms this review argued *against* must not appear as annotated or
   proposed terms anywhere, and experimental evidence codes must not cite a
   reference whose experiments were done in another organism.

Run `python audit_akap10_claims.py` to check, `--self-test` to verify each check
actually fires. A self-test only proves the guards you thought of work; it cannot
tell you which guard you failed to write, so the coverage question stays a reading
question.
"""
from __future__ import annotations

import argparse
import collections
import copy
import csv
import pathlib
import re
import sys

import yaml

# ----------------------------------------------------------------------------
# Root resolution: derive, never assert. A hardcoded worktree path in a shared
# script reported 56 false failures on a clean file earlier in this campaign.
# ----------------------------------------------------------------------------


def find_root(start: pathlib.Path) -> pathlib.Path:
    for p in [start, *start.parents]:
        if (p / "genes").is_dir() and (p / "src").is_dir():
            return p
    raise SystemExit(
        "ERROR: could not locate the repository root above "
        f"{start} (looked for a directory containing both genes/ and src/)"
    )


ROOT = find_root(pathlib.Path(__file__).resolve())
REVIEW = ROOT / "genes/human/AKAP10/AKAP10-ai-review.yaml"
GOA = ROOT / "genes/human/AKAP10/AKAP10-goa.tsv"

EXPERIMENTAL = {"EXP", "IDA", "IPI", "IMP", "IGI", "IEP"}

# References whose experiments were NOT performed in human. An experimental code on
# a row citing one of these is the AHNAK defect: the term and the quote can both be
# right while the organism in the paper is not the organism being annotated.
NON_HUMAN_REFERENCES = {
    "PMID:14531807": "mouse D-AKAP2 in transfected opossum kidney cells",
    "PMID:17485678": "gene-trapped mouse ES cells and mutant mice",
    "PMID:11248059": "mouse brain cAMP-agarose pull-down; the human data are localisation only",
}

# Terms this review argues the gene does NOT have, or that would invert a direction.
# Asserted over the whole document, so a new site cannot evade the check.
FORBIDDEN_TERMS = {
    "GO:0005096": "GTPase activator activity - no Galpha GAP activity was ever measured "
    "and 0/5 contact residues are retained",
    "GO:2001137": "positive regulation of endocytic recycling - knockdown ACCELERATES "
    "recycling, so the wild-type protein is a negative regulator",
    "GO:0010738": "obsolete (regulation of protein kinase A signaling)",
    "GO:0017137": "merged into GO:0031267",
}

# A MODIFY away from these parents must not land back on the parent itself.
NEVER_A_REPLACEMENT = {"GO:0005515", "GO:0051018"}

EXPECTED = {
    "goa_rows": 39,
    "entries": 42,
    "MODIFY": 26,
    "ACCEPT": 9,
    "KEEP_AS_NON_CORE": 3,
    "MARK_AS_OVER_ANNOTATED": 1,
    "NEW": 3,
    "REMOVE": 0,
    "repl_GO:0030165": 22,
    "repl_GO:0034237": 4,
    "GO:0005515_rows": 23,
    "supporting_text_keys": 91,
}


class StrictLoader(yaml.SafeLoader):
    """Rejects duplicate mapping keys. PyYAML silently keeps the last one, which is
    how two provenance entries vanished from a merged review with every gate green."""


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


StrictLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _no_duplicates
)


def wf_key(raw: str) -> tuple[str, ...]:
    return tuple(sorted(t for t in (raw or "").split("|") if t))


def iter_terms(node):
    """Yield every GO id appearing anywhere in the document, at any depth."""
    if isinstance(node, dict):
        for k, v in node.items():
            if k == "id" and isinstance(v, str) and v.startswith("GO:"):
                yield v
            else:
                yield from iter_terms(v)
    elif isinstance(node, list):
        for v in node:
            yield from iter_terms(v)


def audit(doc, goa_rows, raw_text) -> list[str]:
    """Collect problems. Never raise from inside: a check that kills the harness is
    worse than no check, because the harness still prints as though it ran."""
    problems: list[str] = []

    def want(label, got, expected):
        if got != expected:
            problems.append(f"{label}: got {got!r}, expected {expected!r}")

    ann = doc.get("existing_annotations") or []
    actions = collections.Counter(a["review"]["action"] for a in ann)

    want("GOA data rows", len(goa_rows), EXPECTED["goa_rows"])
    want("existing_annotations entries", len(ann), EXPECTED["entries"])
    for act in ("MODIFY", "ACCEPT", "KEEP_AS_NON_CORE", "MARK_AS_OVER_ANNOTATED",
                "NEW", "REMOVE"):
        want(f"action {act}", actions[act], EXPECTED[act])
    want("action total", sum(actions.values()), len(ann))
    want(
        "reviewed rows (entries minus NEW) vs GOA rows",
        len(ann) - actions["NEW"],
        len(goa_rows),
    )

    repl = collections.Counter()
    for a in ann:
        terms = a["review"].get("proposed_replacement_terms") or []
        if a["review"]["action"] == "MODIFY" and not terms:
            problems.append(
                f"MODIFY without proposed_replacement_terms: {a['term']['id']} "
                f"/ {a['original_reference_id']}"
            )
        if terms and a["review"]["action"] != "MODIFY":
            problems.append(
                f"proposed_replacement_terms on a non-MODIFY row "
                f"({a['review']['action']}): {a['term']['id']}"
            )
        for t in terms:
            repl[t["id"]] += 1
            if t["id"] in NEVER_A_REPLACEMENT:
                problems.append(
                    f"replacement term {t['id']} is a parent this review moves away "
                    f"from, not a target"
                )
            if t["id"] == a["term"]["id"]:
                problems.append(f"replacement term equals the original term: {t['id']}")
    want("replacements to GO:0030165", repl["GO:0030165"], EXPECTED["repl_GO:0030165"])
    want("replacements to GO:0034237", repl["GO:0034237"], EXPECTED["repl_GO:0034237"])
    want("replacement rows vs MODIFY rows", sum(repl.values()), actions["MODIFY"])

    # Coverage: every GOA row must have an entry, and every non-NEW entry a GOA row.
    goa_keys = collections.Counter(
        (r["GO TERM"], r["GO EVIDENCE CODE"], r["REFERENCE"], wf_key(r["WITH/FROM"]))
        for r in goa_rows
    )
    yaml_keys = collections.Counter(
        (
            a["term"]["id"],
            a["evidence_type"],
            a["original_reference_id"],
            tuple(sorted(a.get("supporting_entities") or [])),
        )
        for a in ann
        if a["review"]["action"] != "NEW"
    )
    for key, n in (goa_keys - yaml_keys).items():
        problems.append(f"GOA row with no matching review entry (x{n}): {key}")
    for key, n in (yaml_keys - goa_keys).items():
        problems.append(f"non-NEW review entry with no matching GOA row (x{n}): {key}")

    want(
        "GO:0005515 rows",
        sum(1 for a in ann if a["term"]["id"] == "GO:0005515"),
        EXPECTED["GO:0005515_rows"],
    )

    # Claim guards, asserted over the whole document rather than a list of sites.
    present = set(iter_terms(doc))
    for gid, why in FORBIDDEN_TERMS.items():
        if gid in present:
            problems.append(f"forbidden term {gid} appears as a term id: {why}")

    # Species guard: an experimental code asserts the experiment was in this organism.
    for a in ann:
        if a["evidence_type"] in EXPERIMENTAL:
            ref = a["original_reference_id"]
            if ref in NON_HUMAN_REFERENCES:
                problems.append(
                    f"experimental code {a['evidence_type']} on {a['term']['id']} cites "
                    f"{ref}, whose experiments are {NON_HUMAN_REFERENCES[ref]}"
                )

    # Every cited reference must be declared.
    declared = {r["id"] for r in doc.get("references") or []}
    cited: set[str] = set()

    def walk(node):
        if isinstance(node, dict):
            if isinstance(node.get("reference_id"), str):
                cited.add(node["reference_id"])
            for v in node.values():
                walk(v)
        elif isinstance(node, list):
            for v in node:
                walk(v)

    walk(doc)
    for ref in sorted(cited - declared):
        problems.append(f"reference cited in supported_by but not declared: {ref}")

    # Raw-vs-parsed reconciliation. Anchored, because an unanchored substring test on
    # a controlled vocabulary matches the wrong thing (original_reference_id vs
    # reference_id was a real instance of this).
    raw_quotes = len(re.findall(r"^\s*supporting_text:", raw_text, flags=re.M))
    want("raw supporting_text keys", raw_quotes, EXPECTED["supporting_text_keys"])
    parsed_quotes = 0

    def count_quotes(node):
        nonlocal parsed_quotes
        if isinstance(node, dict):
            if "supporting_text" in node:
                parsed_quotes += 1
            for v in node.values():
                count_quotes(v)
        elif isinstance(node, list):
            for v in node:
                count_quotes(v)

    count_quotes(doc)
    want("parsed supporting_text entries vs raw keys", parsed_quotes, raw_quotes)

    return problems


def self_test(doc, goa_rows, raw_text) -> int:
    """Break each invariant deliberately and require the audit to notice.

    Each mutation asserts its target is present first, so a mutation whose anchor has
    drifted fails loudly instead of 'proving' a guard that was never exercised.
    """
    failures = 0

    def run(name, mutate_doc=None, mutate_goa=None, mutate_raw=None):
        nonlocal failures
        d2 = copy.deepcopy(doc)
        g2 = copy.deepcopy(goa_rows)
        r2 = raw_text
        if mutate_doc:
            mutate_doc(d2)
        if mutate_goa:
            g2 = mutate_goa(g2)
        if mutate_raw:
            r2 = mutate_raw(r2)
        found = audit(d2, g2, r2)
        if found:
            print(f"  OK   {name} -> caught ({found[0][:80]})")
        else:
            print(f"  FAIL {name} -> NOT caught")
            failures += 1

    print("self-test: each mutation must be caught")

    def drop_row(d):
        assert d["existing_annotations"], "no annotations to drop"
        d["existing_annotations"].pop()

    run("dropped an annotation row", mutate_doc=drop_row)

    def flip_action(d):
        target = next(
            a for a in d["existing_annotations"] if a["review"]["action"] == "ACCEPT"
        )
        target["review"]["action"] = "REMOVE"

    run("flipped an ACCEPT to REMOVE", mutate_doc=flip_action)

    def strip_replacement(d):
        target = next(
            a for a in d["existing_annotations"] if a["review"]["action"] == "MODIFY"
        )
        assert target["review"].get("proposed_replacement_terms")
        del target["review"]["proposed_replacement_terms"]

    run("MODIFY stripped of its replacement term", mutate_doc=strip_replacement)

    def parent_replacement(d):
        target = next(
            a
            for a in d["existing_annotations"]
            if a["review"].get("proposed_replacement_terms")
        )
        target["review"]["proposed_replacement_terms"][0]["id"] = "GO:0051018"

    run("replacement pointed back at the parent term", mutate_doc=parent_replacement)

    def inject_gap(d):
        # Injected into core_functions, NOT into existing_annotations. A first version
        # of this mutation changed an annotation's term id and was caught by the
        # coverage check instead of the forbidden-term check - i.e. the guard under
        # test was never exercised and the self-test still read as green. Placing the
        # term where no other check can see it is what makes this test real.
        assert d.get("core_functions"), "no core_functions to mutate"
        d["core_functions"][0]["molecular_function"]["id"] = "GO:0005096"

    run("GTPase activator term injected into core_functions", mutate_doc=inject_gap)

    def invert_direction(d):
        target = next(
            a for a in d["existing_annotations"] if a["term"]["id"] == "GO:2001136"
        )
        target["term"]["id"] = "GO:2001137"

    run("recycling direction inverted", mutate_doc=invert_direction)

    def species_mismatch(d):
        target = next(
            a for a in d["existing_annotations"] if a["review"]["action"] == "NEW"
        )
        target["original_reference_id"] = "PMID:17485678"

    run("experimental code given a mouse-only reference", mutate_doc=species_mismatch)

    def undeclared_ref(d):
        target = d["existing_annotations"][0]["review"]["supported_by"][0]
        assert "reference_id" in target
        target["reference_id"] = "PMID:99999999"

    run("supported_by cites an undeclared reference", mutate_doc=undeclared_ref)

    def drop_goa_row(g):
        assert g, "no GOA rows to drop"
        return g[:-1]

    run("a GOA row removed (coverage drift)", mutate_goa=drop_goa_row)

    def hide_a_quote(t):
        assert "\n      supporting_text:" in t
        return t.replace("\n      supporting_text:", "\n      supporting_texts:", 1)

    run("a raw supporting_text key renamed", mutate_raw=hide_a_quote)

    print(f"self-test: {failures} guard(s) failed to fire")
    return failures


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--self-test",
        action="store_true",
        help="break each invariant and require the audit to notice",
    )
    args = ap.parse_args()

    raw_text = REVIEW.read_text()
    try:
        doc = yaml.load(raw_text, Loader=StrictLoader)
    except yaml.constructor.ConstructorError as exc:
        print(f"DUPLICATE YAML KEY - data has already been discarded by the parser: {exc}")
        return 1

    with open(GOA) as fh:
        goa_rows = list(csv.DictReader(fh, delimiter="\t"))

    print(f"root:   {ROOT}")
    print(f"review: {REVIEW.relative_to(ROOT)}")
    print(f"goa:    {GOA.relative_to(ROOT)} ({len(goa_rows)} data rows)")
    print()

    problems = audit(doc, goa_rows, raw_text)
    if problems:
        print(f"{len(problems)} PROBLEM(S):")
        for p in problems:
            print("  -", p)
    else:
        print("audit: every asserted number and claim reproduces from the file")

    rc = 1 if problems else 0
    if args.self_test:
        print()
        rc = max(rc, 1 if self_test(doc, goa_rows, raw_text) else 0)
    return rc


if __name__ == "__main__":
    sys.exit(main())
