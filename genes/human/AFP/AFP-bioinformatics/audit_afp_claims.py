#!/usr/bin/env python3
"""Integrity audit for the human AFP gene review.

These are not biological analyses; they are mechanical checks on the review
document itself, covering three gaps that the repository validators leave open:

1. **GOA row coverage and source_entities.**  The `fetch-gene` stub under-seeds:
   it collapses GOA rows that differ only by assigner or by interaction partner.
   For AFP the GOA TSV has 8 data rows and the stub produced 7.  This check
   rebuilds the expected `supporting_entities` straight from the GOA WITH/FROM
   column and asserts row-for-row coverage, so the review cannot silently
   under-review the gene and a `source_entities` list cannot drift from GOA.

2. **supporting_text verification, including `file:` references.**  CI verifies
   quotes verbatim only for `PMID:` references; quotes citing `file:...` are not
   checked at all.  This checks both, and additionally requires that a quote from
   a UniProt flat file lie wholly within ONE physical line, because a quote
   spanning a `CC       ` continuation can never match the raw file and would
   otherwise pass silently.

3. **Duplicate YAML keys.**  PyYAML keeps the last occurrence of a duplicated
   mapping key and discards the earlier one without warning, so the data is gone
   before any parsed-document gate runs.  This loads the raw text with a strict
   loader that raises instead, and reconciles the raw `supporting_text:` line
   count against the parsed count.

Usage, from the repository root:

    uv run python genes/human/AFP/AFP-bioinformatics/audit_afp_claims.py
    uv run python genes/human/AFP/AFP-bioinformatics/audit_afp_claims.py --write
    uv run python genes/human/AFP/AFP-bioinformatics/audit_afp_claims.py --self-test

`--write` regenerates RESULTS.md.  `--self-test` breaks the document on purpose
and asserts that each guard fires; it asserts the mutation target is present
first, so a drifted anchor is an error rather than a mutation that silently
no-ops and "proves" the guard works.

Exit status is 0 only when every check passes, so it is safe to gate a commit on.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

# .../genes/human/AFP/AFP-bioinformatics/this.py -> parents[4] is the repo root
ROOT = Path(__file__).resolve().parents[4]
assert (ROOT / "genes").is_dir(), f"repo root misresolved: {ROOT}"
REVIEW = ROOT / "genes" / "human" / "AFP" / "AFP-ai-review.yaml"
GOA = ROOT / "genes" / "human" / "AFP" / "AFP-goa.tsv"
RESULTS = Path(__file__).resolve().parent / "RESULTS.md"

# GOA TSV is 16 columns; 0-based: 4 GO term, 8 evidence code, 9 reference,
# 10 WITH/FROM, 13 assigned by.  Older one-liners keyed on column 7 for evidence
# and silently match nothing.
COL_TERM, COL_EV, COL_REF, COL_WITH, COL_BY = 4, 8, 9, 10, 13

EXPERIMENTAL_CODES = {"EXP", "IDA", "IPI", "IMP", "IGI", "IEP", "HTP", "HDA", "HMP", "HGI", "HEP"}


# --------------------------------------------------------------------------- #
# strict YAML loading
# --------------------------------------------------------------------------- #
class DupKeyLoader(yaml.SafeLoader):
    """SafeLoader that raises on a duplicated mapping key instead of silently
    keeping the last one."""


def _no_duplicates(loader, node, deep=False):  # type: ignore[no-untyped-def]
    mapping = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in mapping:
            raise ValueError(
                f"duplicate YAML key {key!r} at line {key_node.start_mark.line + 1}"
            )
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


DupKeyLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _no_duplicates
)


def norm(s: str) -> str:
    """Collapse whitespace: a quote legitimately wraps across YAML lines."""
    return re.sub(r"\s+", " ", s).strip()


# --------------------------------------------------------------------------- #
# inputs
# --------------------------------------------------------------------------- #
def goa_rows(path: Path = GOA) -> list[dict]:
    if not path.exists():
        raise SystemExit(f"missing input {path} - run `just fetch-gene human AFP`")
    lines = path.read_text().rstrip("\n").split("\n")
    header = lines[0].split("\t")
    if len(header) != 16:
        raise SystemExit(
            f"expected a 16-column GOA TSV, got {len(header)} columns; "
            "the column indices in this script are keyed to the 16-column schema"
        )
    return [
        {
            "term": f[COL_TERM],
            "evidence": f[COL_EV],
            "ref": f[COL_REF],
            "with": [t for t in f[COL_WITH].split("|") if t],
            "by": f[COL_BY],
        }
        for f in (ln.split("\t") for ln in lines[1:])
    ]


def load_source(ref_id: str) -> tuple[str, Path]:
    if ref_id.startswith("PMID:"):
        p = ROOT / "publications" / f"PMID_{ref_id[5:]}.md"
    elif ref_id.startswith("file:"):
        rel = ref_id[5:]
        p = ROOT / "genes" / rel
        if not p.exists():
            p = ROOT / rel
    else:
        raise ValueError(f"{ref_id} is not a quotable source")
    if not p.exists():
        raise SystemExit(f"missing cached source for {ref_id}: {p}")
    return p.read_text(), p


def iter_quotes(doc):  # type: ignore[no-untyped-def]
    """Yield (path, reference_id, supporting_text) for every quote.

    Two shapes carry quotes: `supported_by` entries, which name their own
    reference_id, and `references[].findings[]`, which inherit the enclosing
    reference's id and have no reference_id line of their own.  Counting only
    reference_id lines therefore under-counts, in a way that looks explainable.
    """

    def walk(node, path):  # type: ignore[no-untyped-def]
        if isinstance(node, dict):
            if "reference_id" in node and "supporting_text" in node:
                yield path, node["reference_id"], node["supporting_text"]
            for k, v in node.items():
                yield from walk(v, f"{path}.{k}")
        elif isinstance(node, list):
            for i, v in enumerate(node):
                yield from walk(v, f"{path}[{i}]")

    yield from walk(doc, "")

    for i, ref in enumerate(doc.get("references") or []):
        rid = ref.get("id")
        for j, f in enumerate(ref.get("findings") or []):
            if "supporting_text" in f and "reference_id" not in f:
                yield f"references[{i}].findings[{j}]", rid, f["supporting_text"]


# --------------------------------------------------------------------------- #
# checks.  Each APPENDS to `problems`; none raises, because a check that kills
# the harness is worse than no check -- the harness still prints as though it ran.
# --------------------------------------------------------------------------- #
def check_all(review_path: Path = REVIEW) -> tuple[list[str], dict]:
    problems: list[str] = []
    stats: dict = {}
    raw = review_path.read_text()

    try:
        doc = yaml.load(raw, Loader=DupKeyLoader)
    except ValueError as e:
        return [f"DUPLICATE YAML KEY: {e}"], stats

    rows = goa_rows()
    anns = doc["existing_annotations"]
    new = [a for a in anns if a.get("review", {}).get("action") == "NEW"]
    goa_derived = [a for a in anns if a.get("review", {}).get("action") != "NEW"]
    stats["goa_rows"] = len(rows)
    stats["entries"] = len(anns)
    stats["new"] = len(new)
    stats["goa_derived"] = len(goa_derived)

    # --- 1. row coverage -----------------------------------------------------
    if len(goa_derived) != len(rows):
        problems.append(
            f"row coverage: GOA has {len(rows)} data rows but the review has "
            f"{len(goa_derived)} non-NEW entries"
        )

    goa_key = sorted((r["term"], r["evidence"], r["ref"]) for r in rows)
    rev_key = sorted(
        (a["term"]["id"], a["evidence_type"], a["original_reference_id"])
        for a in goa_derived
    )
    if goa_key != rev_key:
        problems.append(f"row identity mismatch:\n    GOA={goa_key}\n    REV={rev_key}")

    # --- 2. supporting_entities rebuilt from GOA WITH/FROM --------------------
    used = [False] * len(rows)
    for a in goa_derived:
        key = (a["term"]["id"], a["evidence_type"], a["original_reference_id"])
        idx = next(
            (
                i
                for i, r in enumerate(rows)
                if not used[i] and (r["term"], r["evidence"], r["ref"]) == key
            ),
            None,
        )
        if idx is None:
            problems.append(f"{key}: no unused GOA row matches this review entry")
            continue
        used[idx] = True
        want = sorted(rows[idx]["with"])
        got = sorted(a.get("supporting_entities") or [])
        if want != got:
            problems.append(
                f"{key}: supporting_entities {got} != GOA WITH/FROM {want}"
            )
        # source_entities, when present, must cover the WITH/FROM exactly.
        # Assert PRESENCE rather than validating only on match, so deleting an
        # entity cannot make the check pass by having nothing left to compare.
        pr = (a.get("review") or {}).get("propagation_review") or {}
        se = pr.get("source_entities")
        if se is not None:
            ids = [x["source_id"] for x in se]
            if len(ids) != len(set(ids)):
                problems.append(f"{key}: duplicate source_id in source_entities")
            extra = sorted(set(ids) - set(want))
            missing = sorted(set(want) - set(ids))
            if extra:
                problems.append(f"{key}: source_entities not in GOA WITH/FROM: {extra}")
            if missing:
                problems.append(
                    f"{key}: GOA WITH/FROM tokens absent from source_entities: {missing}"
                )
    for i, u in enumerate(used):
        if not u:
            problems.append(f"GOA row matched by no review entry: {rows[i]}")

    # --- 3. quotes -----------------------------------------------------------
    raw_quotes = len(re.findall(r"^\s*supporting_text:", raw, re.M))
    # anchored: an unanchored 'reference_id' test also matches original_reference_id
    raw_refids = len(re.findall(r"^\s*-?\s*reference_id:", raw, re.M))
    parsed = list(iter_quotes(doc))
    n_findings = sum(1 for p, _r, _t in parsed if ".findings[" in p)
    n_supported_by = len(parsed) - n_findings
    stats["quotes"] = len(parsed)
    stats["quotes_supported_by"] = n_supported_by
    stats["quotes_findings"] = n_findings

    if raw_quotes != len(parsed):
        problems.append(
            f"raw/parsed mismatch: {raw_quotes} supporting_text lines but "
            f"{len(parsed)} parsed quotes - one has been dropped or double-counted"
        )
    if raw_refids != n_supported_by:
        problems.append(
            f"raw/parsed mismatch: {raw_refids} reference_id lines but "
            f"{n_supported_by} parsed supported_by quotes"
        )

    n_file_quotes = 0
    for path, rid, text in parsed:
        if rid is None:
            problems.append(f"{path}: quote with no resolvable reference id")
            continue
        try:
            body, p = load_source(rid)
        except ValueError as e:
            problems.append(f"{path}: {e}")
            continue
        if norm(text) not in norm(body):
            problems.append(f"{path}: NOT FOUND in {p.name}: {text[:80]!r}")
            continue
        if rid.startswith("file:"):
            n_file_quotes += 1
            if p.name.endswith("-uniprot.txt") and not any(
                norm(text) in norm(line) for line in body.splitlines()
            ):
                problems.append(
                    f"{path}: UniProt quote spans a CC continuation and so can never "
                    f"match the raw file: {text[:80]!r}"
                )
    stats["file_quotes"] = n_file_quotes

    # --- 4. descriptive counts used in the review's prose --------------------
    stats["experimental_goa_rows"] = sum(
        1 for r in rows if r["evidence"] in EXPERIMENTAL_CODES
    )
    stats["distinct_goa_terms"] = len({r["term"] for r in rows})
    stats["assigners"] = sorted({r["by"] for r in rows})
    return problems, stats


# --------------------------------------------------------------------------- #
def render(stats: dict, problems: list[str]) -> str:
    return f"""# AFP review integrity audit

Generated by `audit_afp_claims.py`. Run from the repository root:

```
uv run python genes/human/AFP/AFP-bioinformatics/audit_afp_claims.py
```

These are mechanical checks on `AFP-ai-review.yaml`, not biological analyses.
They cover three things the repository validators do not: that every GOA row has
its own reviewed entry (the `fetch-gene` stub collapses rows that differ only by
assigner), that `file:` quotes are verbatim (CI checks only `PMID:` quotes), and
that no duplicated YAML key has silently discarded data.

## Result

{"**PASS** - all checks clean." if not problems else f"**FAIL** - {len(problems)} problem(s):" + chr(10) + chr(10) + chr(10).join("- " + p for p in problems)}

## Counts

| quantity | value |
|---|---|
| GOA data rows | {stats.get('goa_rows')} |
| `existing_annotations` entries | {stats.get('entries')} |
| - derived from GOA | {stats.get('goa_derived')} |
| - proposed here (`action: NEW`) | {stats.get('new')} |
| distinct GO terms in GOA | {stats.get('distinct_goa_terms')} |
| GOA rows with an experimental evidence code | {stats.get('experimental_goa_rows')} |
| GOA assigners | {', '.join(stats.get('assigners', []))} |
| `supporting_text` quotes verified | {stats.get('quotes')} |
| - in `supported_by` | {stats.get('quotes_supported_by')} |
| - in `references[].findings[]` | {stats.get('quotes_findings')} |
| of which cite a `file:` source (unchecked by CI) | {stats.get('file_quotes')} |

## Notes on the counts

The GOA TSV has {stats.get('goa_rows')} data rows while the generated stub seeded 7: the two
`GO:0005515` rows for `PMID:26808496` differ only in assigner, IntAct versus
AgBase, and were collapsed into one. They are restored as separate entries so
each assigner gets its own verdict, and so that one co-immunoprecipitation is not
counted as two independent supports.

All {stats.get('experimental_goa_rows')} experimentally-coded GOA rows are `IPI` protein-binding rows. There is
no experimental molecular-function row of any other kind and no experimental
biological-process row, which is why this review's diagnosis is under-annotation
rather than over-annotation.
"""


def self_test() -> int:
    """Break the document on purpose; assert each guard fires.

    A self-test proves the guards you thought of fire. It cannot tell you which
    guard you failed to write, so the unexercised guard is named explicitly.
    """
    raw = REVIEW.read_text()
    tmp = REVIEW.parent / ".audit-selftest-ai-review.yaml"
    fired: dict[str, bool] = {}

    def run(mutated: str) -> bool:
        tmp.write_text(mutated)
        probs, _ = check_all(tmp)
        return bool(probs)

    try:
        # guard: a quote that is not in its source
        m = re.search(r"^(\s*supporting_text:)(.*)$", raw, re.M)
        assert m, "self-test anchor 'supporting_text:' absent - mutation would no-op"
        fired["quote_not_found"] = run(
            raw[: m.start(2)] + " ZZQQ fabricated quote ZZQQ" + raw[m.end(2) :]
        )

        # guard: duplicate mapping key
        anchor = "gene_symbol: AFP"
        assert anchor in raw, f"self-test anchor {anchor!r} absent - mutation would no-op"
        fired["duplicate_key"] = run(raw.replace(anchor, anchor + "\n" + anchor, 1))

        # guard: a deleted supporting_entities list
        doc = yaml.safe_load(raw)
        target = next(
            a for a in doc["existing_annotations"] if a.get("supporting_entities")
        )
        assert target, "self-test anchor: no entry with supporting_entities"
        target.pop("supporting_entities")
        fired["supporting_entities_dropped"] = run(yaml.dump(doc, sort_keys=False))

        # guard: a dropped GOA row (review under-covers the TSV)
        doc2 = yaml.safe_load(raw)
        before = len(doc2["existing_annotations"])
        doc2["existing_annotations"] = [
            a for a in doc2["existing_annotations"]
            if a.get("review", {}).get("action") != "ACCEPT"
        ]
        assert len(doc2["existing_annotations"]) < before, "no ACCEPT row to drop"
        fired["row_coverage"] = run(yaml.dump(doc2, sort_keys=False))
    finally:
        tmp.unlink(missing_ok=True)

    print("self-test:")
    ok = True
    for name, did in fired.items():
        print(f"  {name}: {'FIRED' if did else 'DID NOT FIRE  <<< guard is broken'}")
        ok &= did
    print(
        "  not exercised by any mutation above: the UniProt one-physical-line guard,\n"
        "  because constructing a quote that spans a CC continuation and is still a\n"
        "  whitespace-normalised substring requires hand-building the case."
    )
    return 0 if ok else 1


def main() -> int:
    if "--self-test" in sys.argv:
        return self_test()
    problems, stats = check_all()
    for k, v in stats.items():
        print(f"  {k}: {v}")
    if problems:
        print(f"\n{len(problems)} PROBLEM(S):")
        for p in problems:
            print("  x", p)
    else:
        print("\nall checks clean")
    if "--write" in sys.argv:
        RESULTS.write_text(render(stats, problems))
        print(f"wrote {RESULTS.relative_to(ROOT)}")
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
