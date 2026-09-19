#!/usr/bin/env python3
"""Invariant checks over the committed ARGLU1 review.

Every check here exists because the corresponding mistake has actually been made
somewhere in this campaign:

1. **Duplicate YAML keys silently delete data.** PyYAML keeps the last occurrence
   of a repeated mapping key and discards the earlier one without warning, and
   every other gate in this repo walks the *parsed* document, so the data is gone
   before validation runs. Detection requires a strict loader plus a raw-text
   count.
2. **The `fetch-gene` stub collapses GOA rows.** The review must be reconciled
   against the GOA tsv, not against the stub. Non-NEW `existing_annotations` must
   correspond one-to-one with tsv data rows.
3. **Hand-maintained `source_entities` drift.** They are rebuilt here from the
   GOA WITH/FROM column and compared, so a drift is an error rather than an
   unnoticed inconsistency.
4. **Numbers in prose drift from the artefacts they came from.** Each quantitative
   claim the review makes is re-derived from the committed JSON and compared.

Run:   uv run python audit_arglu1_review.py
Self-test: uv run python audit_arglu1_review.py --self-test

The self-test mutates copies of the real inputs and asserts each guard fires. It
asserts the mutation target is present before mutating, so a drifted target is an
error rather than a vacuous pass. Note what a self-test can and cannot do: it
proves the guards that exist fire; it cannot tell you which guard was never
written.
"""

from __future__ import annotations

import copy
import json
import re
import sys
from pathlib import Path

import yaml


def repo_root() -> Path:
    """Derive the repository root. Never hardcode a worktree path."""
    for base in (Path(__file__).resolve(), Path.cwd().resolve()):
        for p in (base, *base.parents):
            if (p / "genes").is_dir() and (p / "src").is_dir():
                return p
    raise SystemExit(
        "cannot locate the repository root (a directory containing 'genes/' and 'src/')"
    )


ROOT = repo_root()
GENE_DIR = ROOT / "genes" / "human" / "ARGLU1"
BIO_DIR = GENE_DIR / "ARGLU1-bioinformatics"
REVIEW = GENE_DIR / "ARGLU1-ai-review.yaml"
GOA = GENE_DIR / "ARGLU1-goa.tsv"


class StrictLoader(yaml.SafeLoader):
    """SafeLoader that raises on a duplicate mapping key instead of silently dropping."""


def _no_duplicates(loader, node, deep=False):
    mapping = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in mapping:
            raise yaml.constructor.ConstructorError(
                "while constructing a mapping", node.start_mark,
                f"found duplicate key {key!r}", key_node.start_mark,
            )
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


StrictLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _no_duplicates
)


def require(path: Path) -> Path:
    if not path.exists():
        raise SystemExit(
            f"missing input {path}\n"
            f"Regenerate with: just fetch-gene human ARGLU1  (for gene files), or "
            f"run the scripts in {BIO_DIR} (for JSON artefacts)."
        )
    return path


# ---------------------------------------------------------------- GOA parsing

def read_goa(path: Path) -> list[dict]:
    lines = require(path).read_text().splitlines()
    header = lines[0].split("\t")
    rows = []
    for line in lines[1:]:
        if not line.strip():
            continue
        rows.append(dict(zip(header, line.split("\t"))))
    if not rows:
        raise SystemExit(f"{path}: no data rows parsed; the tsv layout changed.")
    return rows


def goa_key(row: dict) -> tuple:
    return (
        row["GO TERM"],
        row["GO EVIDENCE CODE"],
        row["REFERENCE"],
        row["WITH/FROM"],
        row["ASSIGNED BY"],
    )


def review_key(ann: dict) -> tuple:
    ents = ann.get("supporting_entities") or []
    return (
        ann["term"]["id"],
        ann.get("evidence_type"),
        ann.get("original_reference_id"),
        "|".join(ents),
    )


# ------------------------------------------------------------------- checks

def check_duplicate_keys(problems: list[str], text: str) -> None:
    try:
        yaml.load(text, Loader=StrictLoader)
    except yaml.constructor.ConstructorError as exc:
        problems.append(f"duplicate YAML key in the review: {exc}")


def check_raw_vs_parsed(problems: list[str], text: str, doc: dict) -> None:
    """Reconcile a raw-text count against the parsed count.

    Anchored to the line start so `original_reference_id:` cannot match
    `reference_id:` -- any substring test on a controlled vocabulary needs an
    anchor.
    """
    raw = len(re.findall(r"^\s*- reference_id:", text, re.M))
    parsed = 0
    def walk(node):
        nonlocal parsed
        if isinstance(node, dict):
            if "reference_id" in node and "supporting_text" in node:
                parsed += 1
            for v in node.values():
                walk(v)
        elif isinstance(node, list):
            for v in node:
                walk(v)
    walk(doc)
    if raw != parsed:
        problems.append(
            f"reference_id count mismatch: {raw} in raw text vs {parsed} after parsing. "
            "Do not rationalise this gap -- an off-by-N here means parsing dropped "
            "provenance (duplicate key) or the anchor is wrong."
        )


def check_row_coverage(problems: list[str], doc: dict, goa_rows: list[dict]) -> None:
    anns = doc["existing_annotations"]
    new_rows = [a for a in anns if (a.get("review") or {}).get("action") == "NEW"]
    existing = [a for a in anns if (a.get("review") or {}).get("action") != "NEW"]

    if len(existing) != len(goa_rows):
        problems.append(
            f"row coverage: {len(existing)} non-NEW existing_annotations vs "
            f"{len(goa_rows)} GOA tsv data rows. CLAUDE.md requires one entry per tsv "
            f"line; the fetch-gene stub is known to collapse rows, so reconcile against "
            f"the tsv, not the stub. (NEW proposals in this review: {len(new_rows)})"
        )

    # Every GOA (term, evidence, reference) triple must appear.
    goa_triples = sorted({(r["GO TERM"], r["GO EVIDENCE CODE"], r["REFERENCE"])
                          for r in goa_rows})
    rev_triples = sorted({(a["term"]["id"], a.get("evidence_type"),
                           a.get("original_reference_id")) for a in existing})
    missing = [t for t in goa_triples if t not in rev_triples]
    if missing:
        problems.append(f"GOA rows with no review entry: {missing}")

    # Every non-NEW review row must exist in GOA (no invented existing rows).
    extra = [t for t in rev_triples if t not in goa_triples]
    if extra:
        problems.append(
            f"non-NEW review rows absent from GOA (should they be action: NEW?): {extra}"
        )

    # Every row must have been adjudicated.
    pending = [a["term"]["id"] for a in anns
               if (a.get("review") or {}).get("action") in (None, "PENDING")]
    if pending:
        problems.append(f"rows left PENDING or with no action: {pending}")


def check_propagation_sources(problems: list[str], doc: dict,
                              goa_rows: list[dict]) -> None:
    """Rebuild source_entities from the GOA WITH/FROM column and compare.

    Assert presence first: a guard that only validates on match passes silently if
    the thing it guards is deleted.
    """
    found = False
    for ann in doc["existing_annotations"]:
        pr = (ann.get("review") or {}).get("propagation_review")
        if not pr:
            continue
        found = True
        term = ann["term"]["id"]
        ref = ann.get("original_reference_id")
        ev = ann.get("evidence_type")
        matches = [r for r in goa_rows
                   if r["GO TERM"] == term and r["REFERENCE"] == ref
                   and r["GO EVIDENCE CODE"] == ev]
        if not matches:
            problems.append(
                f"propagation_review on {term}/{ev}/{ref} has no matching GOA row"
            )
            continue
        expected = set()
        for r in matches:
            expected |= {t for t in r["WITH/FROM"].split("|") if t}
        declared = {s["source_id"] for s in (pr.get("source_entities") or [])}
        if declared != expected:
            problems.append(
                f"source_entities on {term} do not match the GOA WITH/FROM field.\n"
                f"    declared: {sorted(declared)}\n"
                f"    GOA says: {sorted(expected)}\n"
                "    Build source_entities FROM the tsv, never by hand."
            )
    if not found:
        problems.append(
            "no propagation_review block found in the review. This review is expected "
            "to carry one on the GO:0005739 mitochondrion IBA row; if it was removed, "
            "remove this guard deliberately rather than letting it pass vacuously."
        )


def check_numeric_claims(problems: list[str], text: str,
                         extra_docs: dict[str, str] | None = None) -> None:
    """Re-derive every quantitative claim from the committed artefacts.

    The number is bound to its *context* by a capturing regex rather than merely
    looked for in the document. Presence-only matching is not a guard: the value
    111 appears in this review in three different sentences, so changing one of
    them to 99 leaves 111 present and a presence check passes. (Found by the
    self-test; it is exactly the 'guard defeatable by the thing it guards'
    failure mode.)

    The same claims are checked in the notes and RESULTS.md as well, because a
    claim asserted at several sites with no generation relationship between them
    is this campaign's most common residual defect.
    """
    node = json.loads(require(BIO_DIR / "results.json").read_text())
    refscope = json.loads(require(BIO_DIR / "reference_scope.json").read_text())
    comp = json.loads(require(BIO_DIR / "composition.json").read_text())
    sibs = json.loads(require(BIO_DIR / "sibling_verdicts.json").read_text())

    mito = node["terms"]["GO:0005739"]
    nucp = node["terms"]["GO:0005654"]
    by_ref = {(r["reference"], r["go_id"]): r for r in refscope}
    ecad = by_ref[("PMID:25468996", "GO:0045296")]
    bioplex = by_ref[("PMID:33961781", "GO:0005515")]
    ptmod = by_ref[("PMID:39251607", "GO:0005515")]
    nterm = comp["regions"]["N-terminal RNA-binding region (1-74)"]
    ecad_sib = sibs["GO:0045296|PMID:25468996"]
    mito_sib = sibs["GO:0005739|GO_REF:0000033"]

    # (label, regex capturing the number in context, expected value).
    # Whitespace in the prose is YAML-wrapped, so \s+ is used between words.
    rules: list[tuple[str, str, object]] = [
        ("node reach (entities)",
         r"same\s+(\d+)\s+gene\s+products", mito["distinct_entities"]),
        ("node reach (taxa)",
         r"(\d+)\s+NCBI\s+taxa", mito["distinct_taxon_ids"]),
        ("mitochondrion rows naming the donor",
         r"the\s+(\d+)\s+mitochondrion\s+rows", mito["iba_annotations_from_node"]),
        ("propagated set size",
         r"(\d+)-member\s+propagated\s+set", mito["distinct_entities"]),
        ("E-cadherin annotation count",
         r"(\d+)\s+GO:0045296\s+annotations", ecad["annotations"]),
        ("E-cadherin entity count",
         r"GO:0045296\s+annotations\s+over\s+(\d+)\s+distinct\s+gene\s+products",
         ecad["entities"]),
        ("E-cadherin HDA count",
         r"(\d+)\s+of\s+them\s+HDA", ecad["evidence_codes"]["HDA"]),
        ("BioPlex annotation count",
         r"produced\s+(\d+)\s+GO:0005515\s+annotations,\s+too\s+many",
         bioplex["annotations"]),
        ("post-transcriptional-modules annotation count",
         r"reference\s+produced\s+(\d+)\s+GO:0005515\s+annotations",
         ptmod["annotations"]),
        ("post-transcriptional-modules entity count",
         r"GO:0005515\s+annotations\s+over\s+(\d+)\s+distinct\s+gene\s+products",
         ptmod["entities"]),
        ("N-terminal Arg percent",
         r"([\d.]+)\s+percent\s+Arg", nterm["pct_R"]),
        ("N-terminal Ser percent",
         r"([\d.]+)\s+percent\s+Ser", nterm["pct_S"]),
        ("RS dipeptide count",
         r"(\d+)\s+RS\s+plus\s+\d+\s+SR\s+dipeptides", nterm["RS_dipeptides"]),
        ("SR dipeptide count",
         r"\d+\s+RS\s+plus\s+(\d+)\s+SR\s+dipeptides", nterm["SR_dipeptides"]),
        ("alternating run length",
         r"unbroken\s+(\d+)-dipeptide\s+alternating\s+run",
         nterm["longest_alternating_RS_run_dipeptides"]),
        ("E-cadherin sibling row count",
         r"(\d+)\s+merged\s+reviews\s+carrying\s+this\s+same\s+term", ecad_sib["n_rows"]),
        ("E-cadherin sibling modal count",
         r"MARK_AS_OVER_ANNOTATED\s+(\d+)\s+times",
         ecad_sib["actions"]["MARK_AS_OVER_ANNOTATED"]),
        ("mitochondrion sibling row count",
         r"(\d+)\s+merged\s+reviews\s+in\s+this\s+repository\s+carry\s+a\s+GO:0005739",
         mito_sib["n_rows"]),
    ]

    docs = {"review": text}
    docs.update(extra_docs or {})

    for label, pattern, expected in rules:
        seen_anywhere = False
        for doc_name, body in docs.items():
            hits = re.findall(pattern, body)
            if not hits:
                continue
            seen_anywhere = True
            for hit in hits:
                if str(hit) != str(expected):
                    problems.append(
                        f"[{doc_name}] {label}: prose says {hit}, committed artefact "
                        f"says {expected}. A number that refuses to add up is the bug "
                        f"report -- do not find a story that makes the gap acceptable."
                    )
        if not seen_anywhere:
            problems.append(
                f"{label}: no sentence in the review or its companion documents "
                f"states this claim any more (expected {expected} via /{pattern}/). "
                "Either the prose was reworded, in which case update the rule, or the "
                "claim was dropped, in which case check nothing depends on it."
            )

    # Structural facts the argument turns on.
    if mito["n_experimental_holders"] != 1:
        problems.append(
            f"the mitochondrion argument assumes exactly ONE experimental donor; the "
            f"artefact now reports {mito['n_experimental_holders']}. Re-read the review."
        )
    if nucp["n_experimental_holders"] != 3:
        problems.append(
            f"the nucleoplasm control assumes THREE experimental donors; the artefact "
            f"now reports {nucp['n_experimental_holders']}. Re-read the review."
        )
    if mito["distinct_entities"] != nucp["distinct_entities"]:
        problems.append(
            "the argument turns on the two terms having IDENTICAL reach from the same "
            f"node; artefacts now report {mito['distinct_entities']} vs "
            f"{nucp['distinct_entities']}."
        )
    holders = [h["gene_product"] for h in mito["experimental_holders"]]
    if holders != ["UniProtKB:A0A1D8PRM3"]:
        problems.append(
            f"the sole mitochondrion donor is expected to be UniProtKB:A0A1D8PRM3 "
            f"(Candida TLO16); artefacts report {holders}."
        )


def check_retracted_reference(problems: list[str], doc: dict) -> None:
    """The retracted PMID must be present AND flagged invalid AND unused as evidence."""
    refs = {r["id"]: r for r in doc.get("references", [])}
    rid = "PMID:35082911"
    if rid not in refs:
        problems.append(
            f"{rid} is RETRACTED and should be listed in references with "
            "is_invalid: true so the retraction is on the record."
        )
        return
    if not refs[rid].get("is_invalid"):
        problems.append(f"{rid} is retracted but is_invalid is not set true.")
    # It must not be cited as supporting evidence anywhere.
    cited = []
    def walk(node, path="root"):
        if isinstance(node, dict):
            if node.get("reference_id") == rid:
                cited.append(path)
            for k, v in node.items():
                walk(v, f"{path}.{k}")
        elif isinstance(node, list):
            for i, v in enumerate(node):
                walk(v, f"{path}[{i}]")
    walk(doc)
    if cited:
        problems.append(f"retracted {rid} is used as supporting evidence at: {cited}")


def run_checks(text: str, doc: dict, goa_rows: list[dict]) -> list[str]:
    problems: list[str] = []
    # Each check appends; none raises. A check that kills the harness is worse than
    # no check, because the harness still prints as though it ran.
    check_duplicate_keys(problems, text)
    check_raw_vs_parsed(problems, text, doc)
    check_row_coverage(problems, doc, goa_rows)
    check_propagation_sources(problems, doc, goa_rows)
    check_numeric_claims(problems, text)
    check_retracted_reference(problems, doc)
    return problems


# ---------------------------------------------------------------- self-test

def self_test() -> int:
    text = require(REVIEW).read_text()
    doc = yaml.safe_load(text)
    goa_rows = read_goa(GOA)

    baseline = run_checks(text, doc, goa_rows)
    if baseline:
        print("SELF-TEST ABORTED: the unmutated review already has problems:")
        for p in baseline:
            print("  -", p)
        return 1

    failures = []

    def expect_fire(name, t, d, g):
        probs = run_checks(t, d, g)
        if not probs:
            failures.append(f"{name}: guard did NOT fire")
        else:
            print(f"  ok  {name}: fired ({probs[0][:90]}...)")

    # 1. duplicate key. The anchor is the first line of the document, so match it
    #    at the start rather than assuming a preceding newline.
    anchor = "id: Q9NWB6\n"
    assert text.startswith(anchor), (
        "self-test anchor 'id: Q9NWB6' is no longer the first line; target drifted. "
        "A mutation whose target has moved would 'prove' the guard fires while "
        "breaking nothing."
    )
    expect_fire("duplicate-key", anchor + text, doc, goa_rows)

    # 2. dropped annotation row
    d2 = copy.deepcopy(doc)
    assert len(d2["existing_annotations"]) > 1
    d2["existing_annotations"] = d2["existing_annotations"][1:]
    expect_fire("row-coverage", text, d2, goa_rows)

    # 3. source_entities drift (delete one entity)
    d3 = copy.deepcopy(doc)
    mutated = False
    for ann in d3["existing_annotations"]:
        pr = (ann.get("review") or {}).get("propagation_review")
        if pr and len(pr.get("source_entities") or []) > 1:
            pr["source_entities"] = pr["source_entities"][:1]
            mutated = True
            break
    assert mutated, "self-test could not find a propagation_review to mutate"
    expect_fire("source-entities-drift", text, d3, goa_rows)

    # 3b. source_entities deleted entirely -- a guard must not be defeatable by
    #     deleting the thing it guards.
    d3b = copy.deepcopy(doc)
    mutated = False
    for ann in d3b["existing_annotations"]:
        review = ann.get("review") or {}
        if review.get("propagation_review"):
            del review["propagation_review"]
            mutated = True
            break
    assert mutated, "self-test could not find a propagation_review to delete"
    expect_fire("propagation-review-deleted", text, d3b, goa_rows)

    # 4. numeric claim drift
    assert "111 gene products" in text, "self-test anchor '111 gene products' drifted"
    expect_fire("numeric-claim", text.replace("111 gene products", "99 gene products"),
                doc, goa_rows)

    # 5. retracted reference un-flagged
    d5 = copy.deepcopy(doc)
    hit = [r for r in d5["references"] if r["id"] == "PMID:35082911"]
    assert hit, "self-test could not find the retracted reference"
    hit[0].pop("is_invalid", None)
    expect_fire("retraction-flag", text, d5, goa_rows)

    # 6. a PENDING row
    d6 = copy.deepcopy(doc)
    d6["existing_annotations"][0]["review"]["action"] = "PENDING"
    expect_fire("pending-action", text, d6, goa_rows)

    if failures:
        print("\nSELF-TEST FAILED:")
        for f in failures:
            print("  -", f)
        return 1
    print("\nself-test: all guards fired")
    return 0


def main() -> int:
    if "--self-test" in sys.argv:
        return self_test()

    text = require(REVIEW).read_text()
    doc = yaml.safe_load(text)
    goa_rows = read_goa(GOA)

    anns = doc["existing_annotations"]
    n_new = sum(1 for a in anns if (a.get("review") or {}).get("action") == "NEW")
    print(f"GOA tsv data rows        : {len(goa_rows)}")
    print(f"existing_annotations     : {len(anns)}  "
          f"({len(anns) - n_new} reviewed GOA rows + {n_new} NEW proposals)")

    problems = run_checks(text, doc, goa_rows)
    if problems:
        print(f"\n{len(problems)} problem(s):")
        for p in problems:
            print("  -", p)
        return 1
    print("\nall checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
