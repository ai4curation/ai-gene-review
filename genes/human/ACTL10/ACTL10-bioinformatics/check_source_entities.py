#!/usr/bin/env python3
"""Assert the review's propagation_review.source_entities match the GOA WITH/FROM field exactly.

Hand-maintained source lists have drifted on every gene in this campaign that tried to build
them by eye (documented 4-of-7, 3-of-6, and a silently missing PANTHER node on ACTR10). This
is the invariant that catches it: for every IBA/ISS/IEA row that carries a propagation_review,
the SET of source_id values must equal the SET of WITH/FROM tokens on the same GOA row.

Design notes, each from a failure mode that has actually occurred:

- The check **asserts presence** rather than validating only on match. A guard that loops over
  source_entities and skips non-matching ids passes silently when an entity is deleted, when
  the list is dropped, or when source_id is relabelled. Here the review row must exist, must
  carry a propagation_review, and its id set must be equal - not a subset.
- Set equality is checked in **both directions**, so an extra invented source fails as loudly
  as a missing one.
- `--self-test` mutates the parsed data in memory in four ways and requires each to be caught,
  and it **asserts the mutation target exists before mutating**, so a self-test cannot "pass"
  by mutating nothing.

Run:  uv run python check_source_entities.py [--self-test]
"""

from __future__ import annotations

import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
GENE_DIR = HERE.parent
GOA_TSV = GENE_DIR / "ACTL10-goa.tsv"
REVIEW = GENE_DIR / "ACTL10-ai-review.yaml"

# Evidence codes whose rows carry a WITH/FROM that must be mirrored in source_entities.
PROPAGATED_CODES = {"IBA", "ISS", "ISO", "ISA", "ISM", "IGC", "IEA", "IRD", "IBD", "IKR"}


def require(path: Path, fix: str) -> Path:
    if not path.exists():
        raise FileNotFoundError(f"missing required input {path}\n  regenerate with: {fix}")
    return path


def goa_withfrom() -> dict[tuple[str, str], set[str]]:
    """{(go_id, evidence_code): {tokens}} for every GOA row carrying a WITH/FROM."""
    lines = require(GOA_TSV, "just fetch-gene human ACTL10").read_text().splitlines()
    header = lines[0].split("\t")
    out: dict[tuple[str, str], set[str]] = {}
    for ln in lines[1:]:
        if not ln.strip():
            continue
        row = dict(zip(header, ln.split("\t")))
        code = row["GO EVIDENCE CODE"]
        if code not in PROPAGATED_CODES:
            continue
        toks = {t for t in row["WITH/FROM"].split("|") if t.strip()}
        if not toks:
            continue
        key = (row["GO TERM"], code)
        if key in out:
            raise RuntimeError(
                f"GOA has two rows for {key}; this check assumes one row per (term, code) "
                "and must be extended before it can be trusted")
        out[key] = toks
    if not out:
        raise RuntimeError(f"parsed zero WITH/FROM-bearing rows from {GOA_TSV}")
    return out


def review_sources(doc: dict) -> dict[tuple[str, str], set[str]]:
    out: dict[tuple[str, str], set[str]] = {}
    for ann in doc["existing_annotations"]:
        code = ann.get("evidence_type")
        key = (ann["term"]["id"], code)
        pr = (ann.get("review") or {}).get("propagation_review")
        if pr is None:
            continue
        ents = pr.get("source_entities")
        if not ents:
            raise RuntimeError(
                f"{key} has a propagation_review with no source_entities; the list is required "
                "so that its absence cannot be mistaken for agreement")
        ids = []
        for e in ents:
            if "source_id" not in e:
                raise RuntimeError(f"{key} has a source entity with no source_id: {e}")
            ids.append(e["source_id"])
        if len(ids) != len(set(ids)):
            dup = sorted({i for i in ids if ids.count(i) > 1})
            raise RuntimeError(f"{key} lists duplicate source_id values: {dup}")
        out[key] = set(ids)
    return out


def check(goa: dict, rev: dict) -> list[str]:
    problems: list[str] = []
    for key, toks in goa.items():
        if key not in rev:
            problems.append(
                f"{key[0]} ({key[1]}): GOA carries {len(toks)} WITH/FROM tokens but the review "
                "row has no propagation_review.source_entities")
            continue
        got = rev[key]
        missing = sorted(toks - got)
        extra = sorted(got - toks)
        if missing:
            problems.append(f"{key[0]} ({key[1]}): {len(missing)} GOA token(s) absent from "
                            f"source_entities: {missing}")
        if extra:
            problems.append(f"{key[0]} ({key[1]}): {len(extra)} source_entities not in the GOA "
                            f"WITH/FROM field: {extra}")
        if not missing and not extra:
            print(f"  OK  {key[0]} ({key[1]}): {len(toks)} tokens match exactly")
    for key in rev:
        if key not in goa:
            problems.append(f"{key[0]} ({key[1]}): review has source_entities but GOA has no "
                            "such propagated row")
    return problems


def self_test(goa: dict, doc: dict) -> None:
    """Each mutation must be caught, and each mutation target must exist before mutating."""
    import copy

    cases: list[tuple[str, callable]] = []

    def drop_one_entity(d):
        ann = next(a for a in d["existing_annotations"] if a["term"]["id"] == "GO:0015629")
        ents = ann["review"]["propagation_review"]["source_entities"]
        assert len(ents) > 1, "mutation target missing: expected >1 source entity to drop one"
        ents.pop()
    cases.append(("drop one source entity", drop_one_entity))

    def add_bogus_entity(d):
        ann = next(a for a in d["existing_annotations"] if a["term"]["id"] == "GO:0005200")
        ents = ann["review"]["propagation_review"]["source_entities"]
        assert ents, "mutation target missing: no source entities to append to"
        ents.append({"source_id": "UniProtKB:P00000", "source_label": "bogus",
                     "source_status": "SUPPORTS_TRANSFER", "comment": "injected by self-test"})
    cases.append(("add a source entity absent from GOA", add_bogus_entity))

    def relabel_source_id(d):
        ann = next(a for a in d["existing_annotations"] if a["term"]["id"] == "GO:0005200")
        ents = ann["review"]["propagation_review"]["source_entities"]
        target = next(e for e in ents if e["source_id"] == "PANTHER:PTN000940351")
        assert target, "mutation target missing: PANTHER:PTN000940351"
        target["source_id"] = "PANTHER:PTN999999999"
    cases.append(("relabel a source_id", relabel_source_id))

    def drop_whole_propagation_review(d):
        ann = next(a for a in d["existing_annotations"] if a["term"]["id"] == "GO:0015629")
        assert "propagation_review" in ann["review"], "mutation target missing: propagation_review"
        del ann["review"]["propagation_review"]
    cases.append(("delete a whole propagation_review", drop_whole_propagation_review))

    failures = []
    for name, mutate in cases:
        d = copy.deepcopy(doc)
        mutate(d)
        try:
            problems = check(goa, review_sources(d))
        except RuntimeError as exc:
            problems = [str(exc)]
        if problems:
            print(f"  caught: {name}")
        else:
            failures.append(name)
    if failures:
        raise SystemExit(f"SELF-TEST FAILED - these mutations were not caught: {failures}")
    print(f"self-test: all {len(cases)} mutations caught")
    print("NOTE: a passing self-test proves the guards written here fire. It cannot show which "
          "guard was never written.")


def main() -> None:
    doc = yaml.safe_load(require(REVIEW, "see genes/human/ACTL10/").read_text())
    goa = goa_withfrom()
    print(f"checking {len(goa)} propagated GOA row(s) against {REVIEW.name}")
    problems = check(goa, review_sources(doc))
    if problems:
        for p in problems:
            print(f"  FAIL  {p}")
        raise SystemExit(f"{len(problems)} source_entities mismatch(es)")
    print("source_entities match the GOA WITH/FROM field exactly")
    if "--self-test" in sys.argv:
        print("\nrunning self-test (mutate, then require detection)")
        self_test(goa, doc)


if __name__ == "__main__":
    main()
