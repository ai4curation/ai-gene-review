"""Invariant lint for the ARFGEF2 review.

Checks things no repo validator covers, over the CLASS of each error rather than
over a hand-enumerated list of sites:

1. **Duplicate YAML keys.** PyYAML keeps the last occurrence of a duplicated
   mapping key and silently discards the earlier one, so a quote can be deleted
   before any gate that walks the parsed document ever sees it. Detected by a
   strict loader that raises, plus a raw-vs-parsed count reconciliation on an
   anchored regex.
2. **Verbatim `supporting_text`.** Every quote is re-checked against its source.
   `PMID:` quotes are whitespace-normalised substrings of the cached publication;
   `file:` quotes - which CI does not check at all - must appear exactly, and a
   quote citing the UniProt flat file must additionally sit on ONE physical line,
   since a span crossing a `CC       ` continuation can never match.
3. **Reference titles** match the cached publication frontmatter exactly. A title
   written from memory fails CI but not `just validate`.
4. **`supporting_entities` are derived from GOA**, not hand-maintained: the
   review's per-row list must equal the GOA WITH/FROM column, token for token.
5. **Row coverage**: one reviewed entry per GOA row, plus explicitly counted NEW
   rows, and no PENDING actions left.
6. **Numbers asserted in prose** (`RESULTS.md`, `ARFGEF2-notes.md`, the review
   YAML) still match `provenance_audit.json`. A number that drifts is the most
   common way a correct analysis becomes a wrong claim.
7. **Retracted phrasings**: claims this review considered and withdrew must not
   reappear anywhere.

Run:
    uv run --no-project --with pyyaml python audit_claims.py
    uv run --no-project --with pyyaml python audit_claims.py --self-test

`--self-test` breaks each invariant in memory and asserts the corresponding
check fires. It asserts each mutation's target is present **before** mutating,
so a drifted fixture is an error rather than a guard that "passes" against a
mutation that silently no-opped. A passing self-test proves the guards that were
written fire; it cannot tell you which guard was never written.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import yaml


# --------------------------------------------------------------- locations --
def repo_root() -> Path:
    """Derive the repo root; never assert a worktree path.

    A shared script with a hardcoded root resolves quotes against another
    worktree's publications/ cache and reports confident false failures.
    """
    for d in [Path(__file__).resolve()] + list(Path(__file__).resolve().parents):
        if (d / "src").is_dir() and (d / "publications").is_dir():
            return d
    raise RuntimeError(
        "could not locate the repo root (a directory containing both src/ and publications/) "
        f"walking up from {Path(__file__).resolve()}"
    )


ROOT = repo_root()
HERE = Path(__file__).resolve().parent
GENE_DIR = HERE.parent
REVIEW = GENE_DIR / "ARFGEF2-ai-review.yaml"
GOA = GENE_DIR / "ARFGEF2-goa.tsv"
NOTES = GENE_DIR / "ARFGEF2-notes.md"
RESULTS = HERE / "RESULTS.md"
AUDIT = HERE / "provenance_audit.json"
PUBS = ROOT / "publications"

N_NEW_ROWS = 2  # rows this review adds beyond GOA; stated, not inferred.

# The PR description publishes this histogram, and the PR body is outside any
# lint's scan surface. Pinning it here means a later edit that changes an action
# fails the lint instead of silently contradicting the published description.
# The first draft of that table was wrong on three of six rows and was caught
# only by recomputing it.
EXPECTED_ACTIONS = {
    "ACCEPT": 27,
    "KEEP_AS_NON_CORE": 25,
    "REMOVE": 10,
    "MARK_AS_OVER_ANNOTATED": 3,
    "MODIFY": 1,
    "NEW": 2,
}

# Claims this review considered and withdrew. Each entry matches the SHAPE of the
# error (a bounded regex over whitespace-normalised text), not a literal sentence:
# a hand-enumerated list of sentences never terminates, because the next wording
# is always outside it.
RETRACTED_PHRASINGS = [
    # The lookbehinds matter: "GO:0005086 no longer exists as a distinct term" is
    # the CORRECT statement, and a naive keyword match flags it - a guard that
    # fires on the true claim is worse than no guard.
    (r"GO:0005086[^.]{0,140}?(?<!no longer )(?<!not )(?<!never )"
     r"\b(exists|is available|can be used|can be proposed|should be proposed|"
     r"propose(?:d)? as a child|is a distinct term)\b",
     "GO:0005086 was merged into GO:0005085 and survives only as a secondaryId; proposing it "
     "would recreate a deliberate merge"),
    (r"\b(axoneme|axonemal)\b[^.]{0,160}?\b(is wrong|is incorrect|is false|is erroneous|"
     r"was a mistake|mis-?annotation by the curator)",
     "the rat axonemal-microtubule IDA is flagged for re-examination, never asserted to be wrong - "
     "its full text is paywalled and was not read"),
    (r"myosin binding\b[^.]{0,80}?\b(is false|is wrong|is incorrect|does not occur)",
     "GO:0017022 is independently true of BIG2 via PMID:23918382; only its GOA evidence chain is "
     "paralog-derived"),
    (r"\b(neuronal|neural|neuron) migration\b[^.]{0,100}?\b(IMP|IDA|annotated as|NEW row)",
     "no neurodevelopmental BP term is annotated: the disease-paper cell biology uses brefeldin A "
     "and a dominant-negative construct, neither of which isolates BIG2"),
    (r"\bgates_passed\b[^.]{0,60}?\b(true|True)",
     "the affinage record for this gene has no gates_passed field at all; do not report one"),
]


class DuplicateKeyLoader(yaml.SafeLoader):
    """SafeLoader that refuses to silently drop a duplicated mapping key."""


def _no_duplicates(loader, node, deep=False):
    mapping = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in mapping:
            raise yaml.constructor.ConstructorError(
                None, None, f"duplicate key {key!r} in mapping", key_node.start_mark
            )
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


DuplicateKeyLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _no_duplicates
)


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def require(path: Path, fix: str) -> str:
    if not path.exists():
        raise FileNotFoundError(f"{path} is missing. Regenerate it with: {fix}")
    return path.read_text()


# ------------------------------------------------------------------ checks --
def check_duplicate_keys(raw: str, problems: list[str]) -> None:
    try:
        yaml.load(raw, Loader=DuplicateKeyLoader)
    except yaml.constructor.ConstructorError as e:
        problems.append(f"duplicate YAML key: {e}")
        return
    # Raw-vs-parsed reconciliation, anchored so `original_reference_id:` cannot
    # masquerade as `reference_id:`.
    raw_count = len(re.findall(r"^\s*-?\s*reference_id:", raw, flags=re.MULTILINE))
    doc = yaml.safe_load(raw)
    parsed = 0
    for holder in _quote_holders(doc):
        parsed += len(holder)
    if raw_count != parsed:
        problems.append(
            f"reference_id count mismatch: {raw_count} in the raw text vs {parsed} after parsing. "
            "Do not rationalise this gap - derive the expected number independently."
        )


def _quote_holders(doc) -> list[list[dict]]:
    out = []
    for a in doc.get("existing_annotations") or []:
        rev = a.get("review") or {}
        if rev.get("supported_by"):
            out.append(rev["supported_by"])
        for kg in rev.get("knowledge_gaps") or []:
            if kg.get("provenance"):
                out.append(kg["provenance"])
    for cf in doc.get("core_functions") or []:
        if cf.get("supported_by"):
            out.append(cf["supported_by"])
        for kg in cf.get("knowledge_gaps") or []:
            if kg.get("provenance"):
                out.append(kg["provenance"])
    for r in doc.get("references") or []:
        for f in r.get("findings") or []:
            if f.get("supporting_text"):
                out.append([f])
    return out


def _source_text(ref_id: str, cache: dict[str, str]) -> tuple[str, bool] | None:
    """Return (text, is_file_ref) for a reference id, or None if not resolvable."""
    if ref_id in cache:
        return cache[ref_id], ref_id.startswith("file:")
    if ref_id.startswith("PMID:"):
        p = PUBS / f"PMID_{ref_id.split(':', 1)[1]}.md"
        if not p.exists():
            return None
        cache[ref_id] = p.read_text()
        return cache[ref_id], False
    if ref_id.startswith("file:"):
        p = ROOT / "genes" / ref_id.split(":", 1)[1]
        if not p.exists():
            raise FileNotFoundError(f"file: reference points at a missing path: {p}")
        cache[ref_id] = p.read_text()
        return cache[ref_id], True
    return None


def check_quotes(doc, problems: list[str]) -> int:
    cache: dict[str, str] = {}
    checked = 0
    for holder in _quote_holders(doc):
        for sb in holder:
            text = sb.get("supporting_text")
            ref = sb.get("reference_id")
            if not text or not ref:
                continue
            got = _source_text(ref, cache)
            if got is None:
                problems.append(f"{ref}: no cached source to verify a quote against")
                continue
            body, is_file = got
            checked += 1
            if is_file:
                # file: quotes are NOT checked by CI - the fabrication surface.
                if text not in body:
                    problems.append(f"{ref}: file quote not found verbatim: {text[:90]!r}")
                elif ref.endswith("-uniprot.txt") and not any(
                    text in line for line in body.splitlines()
                ):
                    problems.append(
                        f"{ref}: UniProt quote spans a CC continuation line and can never "
                        f"match verbatim: {text[:90]!r}"
                    )
            else:
                if norm(text) not in norm(body):
                    problems.append(f"{ref}: quote not found in cached publication: {text[:90]!r}")
    return checked


def check_reference_titles(doc, problems: list[str]) -> int:
    checked = 0
    for r in doc.get("references") or []:
        rid = r.get("id", "")
        if not rid.startswith("PMID:"):
            continue
        p = PUBS / f"PMID_{rid.split(':', 1)[1]}.md"
        if not p.exists():
            problems.append(f"{rid}: cited but not cached under publications/")
            continue
        fm = yaml.safe_load(p.read_text().split("---", 2)[1])
        checked += 1
        if norm(r.get("title", "")) != norm(fm.get("title", "")):
            problems.append(
                f"{rid}: title does not match the cached record.\n"
                f"    review: {r.get('title')!r}\n"
                f"    cached: {fm.get('title')!r}"
            )
    return checked


def check_supporting_entities(doc, goa_rows, problems: list[str]) -> int:
    """The review's per-row supporting_entities must equal GOA's WITH/FROM."""
    expected: dict[tuple[str, str, str], list[list[str]]] = {}
    for row in goa_rows:
        key = (row["GO TERM"], row["GO EVIDENCE CODE"], row["REFERENCE"])
        toks: list[str] = []
        for t in (row["WITH/FROM"] or "").split("|"):
            t = t.strip()
            if t and t not in toks:
                toks.append(t)
        expected.setdefault(key, []).append(toks)

    seen: dict[tuple[str, str, str], int] = {}
    checked = 0
    for a in doc["existing_annotations"]:
        if (a.get("review") or {}).get("action") == "NEW":
            continue
        key = (a["term"]["id"], a["evidence_type"], a["original_reference_id"])
        if key not in expected:
            problems.append(f"review row {key} has no matching GOA row")
            continue
        i = seen.get(key, 0)
        seen[key] = i + 1
        if i >= len(expected[key]):
            problems.append(f"review has more rows than GOA for {key}")
            continue
        want = sorted(expected[key][i])
        have = sorted(a.get("supporting_entities") or [])
        checked += 1
        if want != have:
            problems.append(
                f"supporting_entities drift on {key}:\n    GOA:    {want}\n    review: {have}"
            )
    for key, lists in expected.items():
        if seen.get(key, 0) != len(lists):
            problems.append(
                f"GOA row {key} appears {len(lists)}x but the review has {seen.get(key, 0)}"
            )
    return checked


def check_coverage(doc, goa_rows, problems: list[str]) -> None:
    ann = doc["existing_annotations"]
    n_new = sum(1 for a in ann if (a.get("review") or {}).get("action") == "NEW")
    if n_new != N_NEW_ROWS:
        problems.append(f"expected {N_NEW_ROWS} NEW rows, found {n_new}")
    if len(ann) - n_new != len(goa_rows):
        problems.append(
            f"row count mismatch: {len(ann)} entries - {n_new} NEW = {len(ann) - n_new}, "
            f"but the GOA tsv has {len(goa_rows)} rows"
        )
    pending = [a["term"]["id"] for a in ann if (a.get("review") or {}).get("action") == "PENDING"]
    if pending:
        problems.append(f"{len(pending)} rows still PENDING: {pending}")

    from collections import Counter
    got = Counter((a.get("review") or {}).get("action") for a in ann)
    if dict(got) != EXPECTED_ACTIONS:
        problems.append(
            f"action histogram drift: published description says {EXPECTED_ACTIONS}, file has "
            f"{dict(got)}. Update both, or neither."
        )


def check_numbers(audit: dict, texts: dict[str, str], problems: list[str]) -> int:
    """Numbers asserted in prose must still match the computed audit."""
    f = audit["rat_funnel"]
    solely = [r for r in f["human_rows_from_rat_donor"]
              if r["rat_primary_references"] == ["PMID:15198677"]]
    p15644318 = audit["reference_profiles"]["15644318"]
    p15198677 = audit["reference_profiles"]["15198677"]
    p19946888 = audit["reference_profiles"]["19946888"]

    claims = [
        (str(f["n_human_rows"]), "20", "rows projected from rat Q7TSU1"),
        (str(f["n_distinct_terms"]), "13", "distinct GO terms in the rat funnel"),
        (str(len(solely)), "17", "rows resting solely on PMID:15198677"),
        (str(audit["goa_rows"]), "66", "GOA rows"),
        (str(p15644318["n_entities"]), "7", "entities annotated by PMID:15644318"),
        (str(p15644318["n_annotations"]), "18", "annotations from PMID:15644318"),
        (str(p15644318["n_on_paralog"]), "6", "PMID:15644318 annotations on ARFGEF1"),
        (str(p15644318["n_on_subject"]), "0", "PMID:15644318 annotations on ARFGEF2"),
        (str(p15198677["n_entities"]), "2", "entities annotated by PMID:15198677"),
        (str(p19946888["n_entities"]), "1142", "entities given GO:0016020 by PMID:19946888"),
        (str(len(audit["literature_pmids"])), "43", "literature PMIDs"),
        (str(len(audit["pmids_with_zero_go_annotations_anywhere"])), "26",
         "literature PMIDs with zero GO annotations anywhere"),
        (str(len(audit["pmids_with_zero_annotations_on_subject"])), "33",
         "literature PMIDs with zero annotations on ARFGEF2"),
        (str(audit["cilium_census"]["cohort_size"]), "13", "accessions in the cilium census"),
        (str(len(audit["cilium_census"]["large_arfgef_cilium_holders"])), "1",
         "large ArfGEFs holding a cilium-compartment term"),
    ]
    # The cilium census's conclusion is a membership claim, not a count, so check
    # membership too: a cohort of the right SIZE with the wrong members would
    # pass every numeric check. This is the COPG1-for-GBF1 bug, guarded.
    census = audit["cilium_census"]
    resolved = {v["resolved_gene"] for v in census["per_accession"].values()}
    for sym in ("ARFGEF1", "ARFGEF2", "ARFGEF3", "GBF1"):
        if sym not in resolved:
            problems.append(f"cilium census cohort is missing {sym}; the census claim is about the "
                            f"four human large ArfGEFs and cannot be made without it")
    if census["large_arfgef_cilium_holders"] != ["Q9Y6D5"]:
        problems.append(
            f"cilium census: expected ARFGEF2 (Q9Y6D5) to be the only large-ArfGEF holder, got "
            f"{census['large_arfgef_cilium_holders']}"
        )
    exoc7 = next((v for v in census["per_accession"].values() if v["resolved_gene"] == "EXOC7"), None)
    if exoc7 is None or "GO:0036064" not in exoc7["cilium_terms"]:
        problems.append(
            "cilium census: the EXOC7 ciliary-basal-body result is asserted in RESULTS.md and the "
            "notes as the counterweight to the axoneme argument, but the audit no longer shows it"
        )
    for computed, asserted, what in claims:
        if computed != asserted:
            problems.append(
                f"number drift: prose asserts {asserted} for '{what}' but the audit computes "
                f"{computed}. The gap IS the bug report - do not find a story that explains it."
            )
    # And the asserted value must actually appear in the prose that claims it.
    prose = "\n".join(texts.values())
    for _computed, asserted, what in claims:
        if asserted not in prose:
            problems.append(f"'{what}' = {asserted} is asserted nowhere in RESULTS.md / notes")
    return len(claims)


def check_retracted(texts: dict[str, str], problems: list[str]) -> int:
    checked = 0
    for name, body in texts.items():
        flat = norm(body)
        for pattern, why in RETRACTED_PHRASINGS:
            checked += 1
            m = re.search(pattern, flat, flags=re.IGNORECASE)
            if m:
                problems.append(
                    f"{name}: retracted phrasing {m.group(0)[:120]!r} - {why}"
                )
    return checked


# ------------------------------------------------------------------- main ---
def load_goa() -> list[dict[str, str]]:
    import csv
    text = require(GOA, "just fetch-gene human ARFGEF2")
    return list(csv.DictReader(text.splitlines(), delimiter="\t"))


def run(raw_review: str, texts: dict[str, str], audit: dict, goa_rows) -> list[str]:
    problems: list[str] = []
    check_duplicate_keys(raw_review, problems)
    doc = yaml.safe_load(raw_review)
    n_quotes = check_quotes(doc, problems)
    n_titles = check_reference_titles(doc, problems)
    n_se = check_supporting_entities(doc, goa_rows, problems)
    check_coverage(doc, goa_rows, problems)
    n_nums = check_numbers(audit, texts, problems)
    # Scan the review's own prose too: a retracted claim restated in a summary or
    # reason is a live defect even when the notes and RESULTS are clean.
    n_ret = check_retracted({**texts, "ARFGEF2-ai-review.yaml": raw_review}, problems)
    run.counts = {"quotes": n_quotes, "titles": n_titles, "supporting_entities": n_se,
                  "numbers": n_nums, "retracted_patterns": n_ret}
    return problems


def self_test(raw_review: str, texts: dict[str, str], audit: dict, goa_rows) -> None:
    """Break each invariant and assert its guard fires."""
    import copy

    cases = []

    # 1. duplicate key
    anchor = "    action: ACCEPT\n"
    assert anchor in raw_review, "self-test anchor missing: action: ACCEPT"
    cases.append(("duplicate YAML key",
                  raw_review.replace(anchor, anchor + anchor, 1),
                  texts, audit, goa_rows, "duplicate YAML key"))

    # 2. fabricated quote
    doc = yaml.safe_load(raw_review)
    sb = doc["existing_annotations"][4]["review"]["supported_by"][0]
    assert sb["reference_id"].startswith("PMID:"), sb
    mutated = copy.deepcopy(doc)
    mutated["existing_annotations"][4]["review"]["supported_by"][0]["supporting_text"] = \
        "BIG2 was shown to hydrolyse GTP on ARF1 in a wholly invented experiment."
    cases.append(("fabricated quote", yaml.dump(mutated, sort_keys=False, allow_unicode=True),
                  texts, audit, goa_rows, "quote not found"))

    # 2b. fabricated file: quote (the surface CI does not check)
    file_refs = [(i, j) for i, a in enumerate(doc["existing_annotations"])
                 for j, s in enumerate((a.get("review") or {}).get("supported_by") or [])
                 if s["reference_id"].startswith("file:")]
    assert file_refs, "self-test anchor missing: no file: quote in the review"
    i, j = file_refs[0]
    mutated = copy.deepcopy(doc)
    mutated["existing_annotations"][i]["review"]["supported_by"][j]["supporting_text"] = \
        "This sentence does not appear in the analysis file."
    cases.append(("fabricated file: quote", yaml.dump(mutated, sort_keys=False, allow_unicode=True),
                  texts, audit, goa_rows, "file quote not found"))

    # 3. wrong reference title
    mutated = copy.deepcopy(doc)
    tgt = next(r for r in mutated["references"] if r["id"].startswith("PMID:"))
    old = tgt["title"]
    tgt["title"] = "A title written from memory that does not match the record."
    assert tgt["title"] != old
    cases.append(("wrong reference title", yaml.dump(mutated, sort_keys=False, allow_unicode=True),
                  texts, audit, goa_rows, "title does not match"))

    # 4. supporting_entities drift (delete one token)
    mutated = copy.deepcopy(doc)
    tgt = next(a for a in mutated["existing_annotations"] if len(a.get("supporting_entities") or []) > 1)
    assert tgt["supporting_entities"], "self-test anchor missing: no multi-token supporting_entities"
    tgt["supporting_entities"] = tgt["supporting_entities"][:-1]
    cases.append(("supporting_entities drift", yaml.dump(mutated, sort_keys=False, allow_unicode=True),
                  texts, audit, goa_rows, "supporting_entities drift"))

    # 4b. supporting_entities deleted entirely (a guard that only validates on
    #     match would pass here - assert presence, don't just validate on match)
    mutated = copy.deepcopy(doc)
    tgt = next(a for a in mutated["existing_annotations"] if a.get("supporting_entities"))
    del tgt["supporting_entities"]
    cases.append(("supporting_entities deleted", yaml.dump(mutated, sort_keys=False, allow_unicode=True),
                  texts, audit, goa_rows, "supporting_entities drift"))

    # 5. a row left PENDING
    mutated = copy.deepcopy(doc)
    mutated["existing_annotations"][0]["review"]["action"] = "PENDING"
    cases.append(("PENDING row", yaml.dump(mutated, sort_keys=False, allow_unicode=True),
                  texts, audit, goa_rows, "still PENDING"))

    # 6. a dropped annotation row
    mutated = copy.deepcopy(doc)
    n_before = len(mutated["existing_annotations"])
    del mutated["existing_annotations"][10]
    assert len(mutated["existing_annotations"]) == n_before - 1
    cases.append(("dropped row", yaml.dump(mutated, sort_keys=False, allow_unicode=True),
                  texts, audit, goa_rows, "row count mismatch"))

    # 7. number drift in the audit
    mutated_audit = copy.deepcopy(audit)
    assert mutated_audit["rat_funnel"]["n_human_rows"] == 20
    mutated_audit["rat_funnel"]["n_human_rows"] = 19
    cases.append(("number drift", raw_review, texts, mutated_audit, goa_rows, "number drift"))

    # 7b. cohort membership broken while the COUNT stays right - the
    #     COPG1-for-GBF1 bug, which no numeric check can see.
    mutated_audit = copy.deepcopy(audit)
    gbf1 = next(a for a, v in mutated_audit["cilium_census"]["per_accession"].items()
                if v["resolved_gene"] == "GBF1")
    mutated_audit["cilium_census"]["per_accession"][gbf1]["resolved_gene"] = "COPG1"
    assert mutated_audit["cilium_census"]["cohort_size"] == audit["cilium_census"]["cohort_size"]
    cases.append(("cohort membership (count unchanged)", raw_review, texts, mutated_audit, goa_rows,
                  "missing GBF1"))

    # 7c. the counterweight result silently disappearing
    mutated_audit = copy.deepcopy(audit)
    exo = next(a for a, v in mutated_audit["cilium_census"]["per_accession"].items()
               if v["resolved_gene"] == "EXOC7")
    assert mutated_audit["cilium_census"]["per_accession"][exo]["cilium_terms"] == ["GO:0036064"]
    mutated_audit["cilium_census"]["per_accession"][exo]["cilium_terms"] = []
    cases.append(("EXOC7 counterweight lost", raw_review, texts, mutated_audit, goa_rows,
                  "EXOC7 ciliary-basal-body result"))

    # 7d. an action flipped - histogram drifts away from the published description
    mutated = copy.deepcopy(doc)
    tgt = next(a for a in mutated["existing_annotations"]
               if a["review"]["action"] == "KEEP_AS_NON_CORE")
    tgt["review"]["action"] = "ACCEPT"
    cases.append(("action histogram drift", yaml.dump(mutated, sort_keys=False, allow_unicode=True),
                  texts, audit, goa_rows, "action histogram drift"))

    # 8. a retracted phrasing reappearing
    mutated_texts = dict(texts)
    mutated_texts["injected"] = "GO:0005086 is available and should be proposed as a child."
    cases.append(("retracted phrasing", raw_review, mutated_texts, audit, goa_rows,
                  "retracted phrasing"))

    failures = []
    for name, rv, tx, au, gr, expect in cases:
        got = run(rv, tx, au, gr)
        if not any(expect in p for p in got):
            failures.append(f"guard did NOT fire for {name!r} (expected a problem containing "
                            f"{expect!r}); got {got[:2]}")
        else:
            print(f"  ok   guard fires for {name}")
    if failures:
        for f in failures:
            print(f"  FAIL {f}")
        raise SystemExit(1)
    print(f"self-test: {len(cases)}/{len(cases)} guards fire")


def main() -> None:
    raw_review = require(REVIEW, "just fetch-gene human ARFGEF2")
    texts = {
        "RESULTS.md": require(RESULTS, "see genes/human/ARFGEF2/ARFGEF2-bioinformatics/README.md"),
        "ARFGEF2-notes.md": require(NOTES, "hand-written; see CLAUDE.md"),
    }
    audit = json.loads(require(AUDIT, "uv run python provenance_audit.py"))
    goa_rows = load_goa()

    if "--self-test" in sys.argv:
        # A clean baseline first: a self-test run against an already-broken file
        # would be meaningless.
        base = run(raw_review, texts, audit, goa_rows)
        if base:
            print("baseline is not clean; fix these before running --self-test:")
            for p in base:
                print(f"  - {p}")
            raise SystemExit(1)
        self_test(raw_review, texts, audit, goa_rows)
        return

    problems = run(raw_review, texts, audit, goa_rows)
    c = run.counts
    print(f"checked: {c['quotes']} quotes, {c['titles']} reference titles, "
          f"{c['supporting_entities']} supporting_entities lists, {c['numbers']} numeric claims, "
          f"{c['retracted_patterns']} retracted-phrasing scans")
    if problems:
        print(f"\n{len(problems)} problem(s):")
        for p in problems:
            print(f"  - {p}")
        raise SystemExit(1)
    print("0 problems")


if __name__ == "__main__":
    main()
