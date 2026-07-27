#!/usr/bin/env python3
"""Self-audit for the ADAMTSL5 review.

Checks the things no repo gate checks:

Numbering below matches the `--- N.` banners in check(), in execution order.

  1. Duplicate YAML keys -- PyYAML silently keeps the last and discards the earlier,
     deleting provenance before any quote gate can inspect it.
  2. Row coverage -- every GOA row must have exactly one reviewed annotation. NEW
     entries are our own proposals, NOT GOA rows, and are excluded from this count.
  3. NEW-proposal validity -- each NEW entry must name a term GOA does not already
     carry. This is the only assertion a NEW row can falsify, and it is what makes the
     review's "GOA is missing GO:0001527" claim checkable rather than merely asserted.
     Listed separately from (2) on purpose: conflating "coverage" with "NEW rows are
     accounted for" is precisely what produced the tautological guard this replaced.
  4. No PENDING actions left behind.
  5. `file:` supporting_text quotes -- the repo validator only verifies `PMID:` quotes,
     so a broken `file:` quote passes silently. Also enforces the one-physical-line rule
     for UniProt quotes, which must not cross a `CC       ` continuation.
  6. Required claims by occurrence COUNT, so a claim asserted at N sites cannot
     silently become N-1.
  7. Retracted phrasings -- rejected wordings whose reappearance is a regression.

Run from the repo root:
    uv run python genes/human/ADAMTSL5/ADAMTSL5-bioinformatics/audit_adamtsl5_claims.py
    uv run python .../audit_adamtsl5_claims.py --self-test
"""

import csv
import sys
from collections import Counter
from pathlib import Path

import yaml

GENE_DIR = Path(__file__).resolve().parent.parent
REPO = GENE_DIR.parents[2]
REVIEW = GENE_DIR / "ADAMTSL5-ai-review.yaml"
GOA = GENE_DIR / "ADAMTSL5-goa.tsv"


class StrictLoader(yaml.SafeLoader):
    pass


def _no_dupes(loader, node, deep=False):
    out = {}
    for k_node, v_node in node.value:
        k = loader.construct_object(k_node, deep=deep)
        if k in out:
            raise yaml.constructor.ConstructorError(
                None, None, f"DUPLICATE KEY {k!r} -- data would be silently dropped",
                k_node.start_mark)
        out[k] = loader.construct_object(v_node, deep=deep)
    return out


StrictLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _no_dupes)

# Claims that must appear, with the exact number of sites asserting them.
# "Fixed in N places, landed in N-1" is the campaign's most repeated defect.
# Counts here are OBSERVED, not assumed: each occurrence was listed and inspected
# individually before being pinned (a hand-guessed threshold is a latent bug -- the
# first version of this dict guessed 2/4/3 and was wrong on all three). Their purpose
# is to catch future drift, so a change in any count should be a deliberate edit here.
REQUIRED = {
    "All 16 protein donors": 4,        # IBA reason, IBA quote, RESULTS finding, its quote
    "PTN000347317": 5,                 # IBA summary, source_id, 2 suggested_questions, GO_REF:33
    "517": 6,                          # CYSRT1 partner count: summary, reason, 2 quotes, 2 findings
    "no HExxH substring at all": 1,    # RESULTS finding only; the review prose says it differently
}

# Phrasings that were considered and rejected; their reappearance is a regression.
RETRACTED = [
    "metalloendopeptidase activity",   # no such row exists on this gene
    "lacks catalytic domain therefore",
    "SOURCE_WEAK_OR_INFERRED",         # contradicted by 16/16 donors having own evidence
    "SOURCE_EVIDENCE_WEAK",            # same, and not legal in root_cause anyway
]


def walk_quotes(node, path="", out=None):
    if out is None:
        out = []
    if isinstance(node, dict):
        if "reference_id" in node and "supporting_text" in node:
            out.append((node["reference_id"], node["supporting_text"], path))
        for k, v in node.items():
            walk_quotes(v, f"{path}/{k}", out)
    elif isinstance(node, list):
        for i, v in enumerate(node):
            walk_quotes(v, f"{path}[{i}]", out)
    return out


def check(review_path, goa_path, problems):
    raw = review_path.read_text()
    try:
        doc = yaml.load(raw, Loader=StrictLoader)
    except yaml.constructor.ConstructorError as e:
        problems.append(f"DUPLICATE YAML KEY: {e}")
        return

    # --- 1. duplicate YAML keys: handled by StrictLoader above ------------------
    # --- 2. row coverage (NEW entries excluded; see 3) --------------------------
    goa_rows = [r for r in csv.DictReader(goa_path.open(), delimiter="\t")]
    n_goa = len(goa_rows)
    anns = doc["existing_annotations"]
    # NEW entries are our own proposals, not GOA rows, so reconcile them EXPLICITLY
    # rather than letting the count silently drift: reviewed == GOA, and the surplus
    # must be exactly the NEW proposals.
    new_rows = [a for a in anns if a["review"]["action"] == "NEW"]
    reviewed = [a for a in anns if a["review"]["action"] != "NEW"]
    if len(reviewed) != n_goa:
        problems.append(
            f"coverage: {len(reviewed)} non-NEW existing_annotations vs {n_goa} GOA rows "
            f"({len(new_rows)} NEW proposal(s))")
    # The real invariant a NEW proposal must satisfy: it names a term GOA does not
    # already have. (An earlier version asserted len(anns) == n_goa + len(new_rows),
    # which is a TAUTOLOGY -- new_rows and reviewed partition anns, so it restates the
    # check above and can never fire independently. A guard that cannot fire is worse
    # than no guard, because it reads as coverage. Caught by the PR reviewer on #2305.)
    # --- 3. NEW-proposal validity ------------------------------------------------
    goa_terms = {r["GO TERM"] for r in goa_rows}
    for a in new_rows:
        tid = a["term"]["id"]
        if tid in goa_terms:
            problems.append(
                f"NEW proposal {tid} ({a['term']['label']}) is already a GOA row -- "
                "a NEW entry must name a term GOA lacks")
    goa_key = Counter((r["GO TERM"], r["GO EVIDENCE CODE"]) for r in goa_rows)
    rev_key = Counter((a["term"]["id"], a["evidence_type"]) for a in reviewed)
    if goa_key != rev_key:
        problems.append(f"coverage mismatch by (term, evidence): "
                        f"GOA-only={goa_key - rev_key}, review-only={rev_key - goa_key}")
    # --- 4. no PENDING actions ---------------------------------------------------
    if any(a["review"]["action"] == "PENDING" for a in anns):
        problems.append("at least one annotation is still PENDING")

    # --- 5. file: quotes --------------------------------------------------------
    for ref, quote, path in walk_quotes(doc):
        if not str(ref).startswith("file:"):
            continue
        target = REPO / str(ref)[len("file:"):]
        if not target.exists():
            problems.append(f"file: reference does not exist: {target} (at {path})")
            continue
        text = target.read_text()
        if quote not in text:
            problems.append(f"file: quote NOT verbatim in {target.name} (at {path}): "
                            f"{quote[:70]!r}")
            continue
        if target.name.endswith("-uniprot.txt"):
            # A UniProt quote spanning a `CC       ` continuation is broken even though
            # it "matches" -- enforce that it sits on one physical line.
            if not any(quote in line for line in text.splitlines()):
                problems.append(
                    f"UniProt quote crosses a physical line break (at {path}): "
                    f"{quote[:70]!r}")

    # --- 6. required claims, by count -------------------------------------------
    for claim, expected in REQUIRED.items():
        got = raw.count(claim)
        if got != expected:
            problems.append(f"claim {claim!r}: found {got} occurrence(s), expected {expected}")

    # --- 7. retracted phrasings ---------------------------------------------------
    for bad in RETRACTED:
        if bad in raw:
            problems.append(f"RETRACTED phrasing present: {bad!r}")


def self_test():
    """A self-test proves the guards you thought of fire. Break each one deliberately;
    a mutation whose target string has drifted would otherwise 'pass' vacuously, so
    assert the target is present before mutating."""
    import tempfile
    base = REVIEW.read_text()
    cases = [
        ("duplicate key", "  evidence_type: IBA\n",
         "  evidence_type: IBA\n  evidence_type: IBA\n", "DUPLICATE"),
        ("broken file quote", "All 16 protein donors carry their own experimental (IDA/HDA) annotation",
         "All 16 protein donors carry their own IMAGINARY annotation", "NOT verbatim"),
        ("pending action", "    action: ACCEPT\n", "    action: PENDING\n", "PENDING"),
        ("retracted phrasing", "root_cause: NO_FAILURE_CORE",
         "root_cause: SOURCE_WEAK_OR_INFERRED", "RETRACTED"),
        ("claim count drift", "no HExxH substring at all",
         "no zinc motif at all", "expected 1"),
        # NEW proposal naming a term GOA already has (GO:0031012 is a real GOA row).
        ("NEW duplicates a GOA term", "    id: GO:0001527\n    label: microfibril\n  evidence_type: IDA",
         "    id: GO:0031012\n    label: extracellular matrix\n  evidence_type: IDA",
         "already a GOA row"),
    ]
    ok = True
    for name, target, repl, expect in cases:
        if target not in base:
            print(f"  SELF-TEST BROKEN [{name}]: mutation target absent -- the test "
                  f"would pass vacuously")
            ok = False
            continue
        mutated = base.replace(target, repl, 1)
        with tempfile.NamedTemporaryFile("w", suffix=".yaml", delete=False) as fh:
            fh.write(mutated)
            tmp = Path(fh.name)
        problems = []
        check(tmp, GOA, problems)
        tmp.unlink()
        fired = any(expect in p for p in problems)
        print(f"  [{'PASS' if fired else 'FAIL'}] {name}: guard "
              f"{'fired' if fired else 'DID NOT FIRE'}")
        ok = ok and fired
    return ok


def main():
    if not REVIEW.exists() or not GOA.exists():
        raise SystemExit(f"FATAL: missing {REVIEW} or {GOA}")
    if "--self-test" in sys.argv:
        sys.exit(0 if self_test() else 1)
    problems = []
    check(REVIEW, GOA, problems)
    for p in problems:
        print(f"  PROBLEM: {p}")
    print(f"audit: {len(problems)} problem(s)")
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
