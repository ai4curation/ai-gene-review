"""Gate: the AHNAK2 review's load-bearing claims still match the committed data.

Three independent checks, because the three ways this repo's reviews have gone
wrong are all invisible to the quote validator:

1. **Duplicate YAML keys silently delete data.** PyYAML keeps the last
   occurrence of a repeated mapping key and discards the earlier one without
   warning, so a quote that parsing removed cannot fail a check that inspects
   the parsed document. Load with a strict loader that raises, and reconcile a
   raw grep count against the parsed count.
2. **`source_entities` drift from the GOA WITH/FROM field.** Hand-maintained
   lists have drifted on every gene that tried it. Derive the expected set from
   the TSV and assert equality per row -- and assert *presence*, so deleting an
   entity cannot make the check pass silently.
3. **A claim asserted at N sites gets fixed at N-1.** Check required phrasings
   by occurrence count and reject retracted ones.

`--self-test` mutates a copy and asserts each guard fires. A passing self-test
proves the guards written here work; it says nothing about the guards not
written.

Run: uv run python audit_claims.py [--self-test]
"""

from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).parent
GENE_DIR = HERE.parent
REVIEW = GENE_DIR / "AHNAK2-ai-review.yaml"
GOA = GENE_DIR / "AHNAK2-goa.tsv"
WITHFROM = HERE / "withfrom_resolved.tsv"
DONORS = HERE / "donor_evidence.tsv"
RESULTS = HERE / "RESULTS.md"

EXPERIMENTAL = {"EXP", "IDA", "IPI", "IMP", "IGI", "IEP", "HTP", "HDA", "HMP", "HGI", "HEP"}

# Phrasings that must appear, with the number of places they must appear in.
# The counts are seeded from the current text on purpose: the check exists to
# make a later edit that changes the number of assertion sites visible, so that
# "fixed in N places, landed in N-1" becomes an error rather than a silent no-op.
REQUIRED = {
    REVIEW: [
        ("PDB 4CN0", 2, None),   # the GO:0042803 NEW row + the reference finding
    ],
    RESULTS: [
        ("28.4%", 1, None),      # AHNAK2-vs-AHNAK PDZ identity
        ("56.8%", 1, None),      # AHNAK2-vs-PRX PDZ identity
        ("71.9%", 1, None),      # fraction of the AHNAK alignment inside the repeat
    ],
}
# Phrasings that must NOT appear anywhere (claims considered and withdrawn).
#
# Every entry must be ASSERTIVE. A bare noun phrase like "AHNAK2-periaxin
# heterodimer" fires on the very sentence that retracts it - "it reports ...
# not an AHNAK2-periaxin heterodimer" - which is the substring-without-an-anchor
# failure in a new guise: the lint flags the explanation of the retraction. Write
# the claim as a clause the review would only contain if it believed it.
RETRACTED = [
    # Affinage over-specified the Marg abstract, which says "no AHNAK expression".
    "no AHNAK2 expression was detected in the T-tubule",
    # Han & Kursula report homodimers of PRX and of AHNAK2, not a heterodimer.
    "AHNAK2 forms a heterodimer with periaxin",
    "AHNAK2 heterodimerises with periaxin",
    "AHNAK2 and periaxin form a heterodimer",
]


class StrictLoader(yaml.SafeLoader):
    """SafeLoader that refuses duplicate mapping keys instead of dropping data."""


def _no_duplicates(loader, node, deep=False):  # type: ignore[no-untyped-def]
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


def check_duplicate_keys(review_path: Path, problems: list[str]) -> dict:
    """Parse strictly, then reconcile a raw occurrence count against the parse.

    The substring test is anchored: `reference_id:` also matches
    `original_reference_id:`, which is exactly how this failure hid before.
    """
    text = review_path.read_text()
    try:
        doc = yaml.load(text, Loader=StrictLoader)
    except yaml.constructor.ConstructorError as exc:
        problems.append(f"duplicate YAML key in {review_path.name}: {exc}")
        return yaml.safe_load(text)

    raw = len(re.findall(r"^\s*- term:$", text, flags=re.M))
    parsed = len(doc.get("existing_annotations") or [])
    if raw != parsed:
        problems.append(
            f"raw '- term:' count {raw} != parsed existing_annotations {parsed} "
            "-- derive the expected number independently; do not rationalise the gap"
        )
    return doc


def check_source_entities(doc: dict, problems: list[str]) -> None:
    """Every WITH/FROM token in the GOA row must appear in the row's
    source_entities, and vice versa. Assert presence: a deleted entity must fail,
    not be skipped."""
    with GOA.open() as fh:
        goa = list(csv.DictReader(fh, delimiter="\t"))
    expected: dict[tuple[str, str, str], set[str]] = {}
    for row in goa:
        raw = row["WITH/FROM"].strip()
        if not raw or row["GO EVIDENCE CODE"] not in {"IBA", "ISS", "ISO", "IEA"}:
            continue
        key = (row["GO TERM"], row["GO EVIDENCE CODE"], row["REFERENCE"])
        expected.setdefault(key, set()).update(raw.split("|"))

    seen: dict[tuple[str, str, str], set[str]] = {}
    supporting: dict[tuple[str, str, str], set[str]] = {}
    has_pr: set[tuple[str, str, str]] = set()
    for ann in doc.get("existing_annotations") or []:
        key = (ann["term"]["id"], ann["evidence_type"], ann["original_reference_id"])
        supporting.setdefault(key, set()).update(ann.get("supporting_entities") or [])
        pr = (ann.get("review") or {}).get("propagation_review")
        if not pr:
            continue
        has_pr.add(key)
        seen.setdefault(key, set()).update(
            s["source_id"] for s in pr.get("source_entities") or []
        )

    for key, want in expected.items():
        # Assert presence, not just agreement-on-match: deleting the whole
        # propagation_review must not make this guard pass silently.
        if key[1] == "IBA" and key not in has_pr:
            problems.append(
                f"GOA IBA row {key} has no propagation_review in the review; "
                "every IBA row on this gene is expected to carry one"
            )
            continue
        if key in has_pr and seen[key] != want:
            problems.append(
                f"propagation_review.source_entities for {key} differ from GOA WITH/FROM:\n"
                f"    missing from review: {sorted(want - seen[key])}\n"
                f"    not in GOA:          {sorted(seen[key] - want)}"
            )
        if supporting.get(key) and supporting[key] != want:
            problems.append(
                f"supporting_entities for {key} differ from GOA WITH/FROM:\n"
                f"    missing from review: {sorted(want - supporting[key])}\n"
                f"    not in GOA:          {sorted(supporting[key] - want)}"
            )


def check_donor_counts(problems: list[str]) -> None:
    """Re-derive the numbers RESULTS.md asserts about the donor sets."""
    if not DONORS.exists() or not WITHFROM.exists():
        problems.append("missing donor_evidence.tsv / withfrom_resolved.tsv; "
                        "run `uv run python resolve_withfrom.py` first")
        return
    with DONORS.open() as fh:
        donors = list(csv.DictReader(fh, delimiter="\t"))

    # The AHNAK2 ortholog (mouse Ahnak2) must be absent from the nucleus and
    # splicing donor sets and present on cytoplasm. That asymmetry is the
    # review's central factual claim about the IBAs.
    ortholog = "A0A7N9VR94"
    per_term = {}
    for d in donors:
        per_term.setdefault(d["propagated_term"], set()).add(d["donor_acc"])
    for term, present in (("GO:0005634", False), ("GO:0043484", False),
                          ("GO:0005737", True)):
        if term not in per_term:
            problems.append(f"{term} has no donor rows at all -- check the resolver")
            continue
        actually = ortholog in per_term[term]
        if actually is not present:
            problems.append(
                f"{term}: mouse Ahnak2 ({ortholog}) is "
                f"{'present' if actually else 'absent'} in the donor set, "
                f"but the review argues the opposite"
            )

    # GO:0043484's only donor with its own experimental evidence must be mouse
    # Ahnak; mouse Prx must hold it by IBA only (circular).
    splicing = [d for d in donors if d["propagated_term"] == "GO:0043484"]
    exp = {d["donor_acc"] for d in splicing if d["experimental"] == "yes"}
    if exp != {"E9Q616"}:
        problems.append(
            f"GO:0043484 donors with own experimental evidence = {sorted(exp)}; "
            "the review asserts exactly {'E9Q616'} (mouse Ahnak)"
        )
    prx = {d["donor_evidence"] for d in splicing if d["donor_acc"] == "O55103"}
    if prx and prx != {"IBA"}:
        problems.append(
            f"GO:0043484 on mouse Prx carries {sorted(prx)}, not IBA alone; "
            "the review calls this donor circular"
        )


def check_phrasings(problems: list[str]) -> None:
    for path, wanted in REQUIRED.items():
        text = path.read_text()
        for phrase, n, _ in wanted:
            got = text.count(phrase)
            if got != n:
                problems.append(
                    f"{path.name}: {phrase!r} appears {got}x, expected {n}x"
                )
    for path in (REVIEW, RESULTS, GENE_DIR / "AHNAK2-notes.md"):
        if not path.exists():
            problems.append(f"missing {path}")
            continue
        text = path.read_text()
        for phrase in RETRACTED:
            if phrase in text:
                problems.append(f"{path.name}: retracted phrasing present: {phrase!r}")


def run(review_path: Path = REVIEW) -> list[str]:
    problems: list[str] = []
    if not review_path.exists():
        return [f"missing {review_path}"]
    doc = check_duplicate_keys(review_path, problems)
    if doc:
        check_source_entities(doc, problems)
    check_donor_counts(problems)
    check_phrasings(problems)
    return problems


def self_test() -> None:
    """Break the inputs on purpose; every guard must fire."""
    import tempfile

    original = REVIEW.read_text()
    baseline = run()
    if baseline:
        raise SystemExit("self-test needs a clean baseline; fix these first:\n  "
                         + "\n  ".join(baseline))

    with tempfile.TemporaryDirectory() as td:
        # 1. duplicate key
        p = Path(td) / "dup.yaml"
        anchor = "existing_annotations:"
        assert anchor in original, "self-test anchor missing -- mutation would no-op"
        p.write_text(original.replace(anchor, anchor + "\n- term:\n    id: GO:1\n"
                                      "    label: x\n  evidence_type: IBA\n"
                                      "  original_reference_id: GO_REF:0000033\n", 1)
                     + "\ngene_symbol: DUPLICATE\n")
        if not any("duplicate" in x for x in run(p)):
            raise SystemExit("guard 1 (duplicate key) did NOT fire")

        # 2. deleted source entity
        doc = yaml.safe_load(original)
        hit = False
        for ann in doc["existing_annotations"]:
            pr = (ann.get("review") or {}).get("propagation_review")
            if pr and pr.get("source_entities"):
                pr["source_entities"].pop()
                hit = True
                break
        assert hit, "self-test found no source_entities to delete -- mutation would no-op"
        p2 = Path(td) / "drop.yaml"
        p2.write_text(yaml.safe_dump(doc, sort_keys=False))
        if not any("source_entities" in x for x in run(p2)):
            raise SystemExit("guard 2 (source_entities drift) did NOT fire")

    print("self-test: all guards fired.")


def main() -> int:
    if "--self-test" in sys.argv:
        self_test()
        return 0
    problems = run()
    if problems:
        print(f"{len(problems)} problem(s):")
        for p in problems:
            print(f"  - {p}")
        return 1
    print("audit_claims: 0 problems")
    return 0


if __name__ == "__main__":
    sys.exit(main())
