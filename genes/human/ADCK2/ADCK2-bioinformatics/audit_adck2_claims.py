#!/usr/bin/env python3
"""Invariant checks on the ADCK2 review, run before every push.

Motivated by three recurring failures in this campaign:

* "fixed in N places, landed in N-1" -- so every claim is checked by counting, not by eye;
* `source_entities` silently drifting from the GOA WITH/FROM field on 3 of 3 genes that
  maintained the list by hand -- so it is rebuilt from the TSV and compared;
* a duplicate YAML key silently discarding data before any quote gate can see it -- so the
  file is loaded with a strict loader that rejects repeated keys. Note that StrictLoader
  alone closes that case: the separate raw-vs-parsed count below is NOT a duplicate-key
  guard (run() returns early on the loader error and never reaches it) and earns its place
  on different grounds, spelled out in check_raw_vs_parsed's own docstring.

Design rules learned the hard way: a check appends to `problems` and never raises, so one
failure cannot abort the rest of the harness; and `--self-test` mutates the document to
prove each guard actually fires, asserting the mutation target exists first so a drifted
target cannot "pass" by no-op.

Usage:
    uv run python audit_adck2_claims.py
    uv run python audit_adck2_claims.py --self-test
"""

from __future__ import annotations

import contextlib
import csv
import importlib.util
import io
import json
import re
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
GENE_DIR = HERE.parent
REVIEW = GENE_DIR / "ADCK2-ai-review.yaml"
GOA = GENE_DIR / "ADCK2-goa.tsv"
NOTES = GENE_DIR / "ADCK2-notes.md"
RESULTS_JSON = HERE / "results.json"

SUBJECT = "Q7Z695"


class StrictLoader(yaml.SafeLoader):
    """SafeLoader that refuses duplicate mapping keys instead of silently keeping the last."""


def _no_duplicates(loader, node, deep=False):
    mapping = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in mapping:
            raise yaml.constructor.ConstructorError(
                None, None, f"duplicate key {key!r} at line {key_node.start_mark.line + 1}"
            )
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


StrictLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _no_duplicates
)


def load_goa(path: Path) -> list[dict]:
    with path.open() as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def check_row_coverage(doc: dict, goa: list[dict], problems: list[str]) -> None:
    """Every distinct GOA annotation must have a reviewed entry, and none may stay PENDING."""
    entries = doc.get("existing_annotations") or []
    distinct = {
        (r["GO TERM"], r["GO EVIDENCE CODE"], r["REFERENCE"], r["QUALIFIER"])
        for r in goa
    }
    if len(entries) != len(distinct):
        problems.append(
            f"coverage: {len(entries)} review entries vs {len(distinct)} distinct GOA "
            f"annotations ({len(goa)} raw rows). Reconcile explicitly; an unexplained "
            f"mismatch is either missing coverage or a silent collapse."
        )
    reviewed = {
        (e["term"]["id"], e["evidence_type"], e.get("original_reference_id"),
         e.get("qualifier"))
        for e in entries
    }
    for d in sorted(distinct - reviewed):
        problems.append(f"coverage: GOA annotation with no matching review entry: {d}")
    for i, e in enumerate(entries):
        action = ((e.get("review") or {}).get("action"))
        if action in (None, "PENDING"):
            problems.append(
                f"coverage: existing_annotations[{i}] ({e['term']['id']}) has action="
                f"{action!r}; every row must carry a decided verdict."
            )


def check_source_entities(doc: dict, goa: list[dict], problems: list[str]) -> None:
    """source_entities must be reconstructible from the GOA WITH/FROM column, not by hand."""
    for i, e in enumerate(doc.get("existing_annotations") or []):
        review = e.get("review") or {}
        prop = review.get("propagation_review")
        if not prop:
            continue
        listed = {s["source_id"] for s in (prop.get("source_entities") or [])}
        matching = [
            r for r in goa
            if r["GO TERM"] == e["term"]["id"]
            and r["GO EVIDENCE CODE"] == e["evidence_type"]
            and r["REFERENCE"] == e.get("original_reference_id")
        ]
        if not matching:
            problems.append(
                f"source_entities: existing_annotations[{i}] has a propagation_review but "
                f"no GOA row matches its (term, evidence, reference); cannot verify."
            )
            continue
        expected = {
            tok for r in matching for tok in (r["WITH/FROM"] or "").split("|") if tok
        }
        if listed != expected:
            problems.append(
                f"source_entities: existing_annotations[{i}] ({e['term']['id']}) lists "
                f"{sorted(listed)} but GOA WITH/FROM is {sorted(expected)}; "
                f"missing={sorted(expected - listed)} extra={sorted(listed - expected)}"
            )


def check_supporting_entities(doc: dict, goa: list[dict], problems: list[str]) -> None:
    """Same invariant for the top-level supporting_entities list on IBA rows."""
    for i, e in enumerate(doc.get("existing_annotations") or []):
        listed = e.get("supporting_entities")
        if listed is None:
            continue
        matching = [
            r for r in goa
            if r["GO TERM"] == e["term"]["id"]
            and r["GO EVIDENCE CODE"] == e["evidence_type"]
            and r["REFERENCE"] == e.get("original_reference_id")
        ]
        expected = {
            tok for r in matching for tok in (r["WITH/FROM"] or "").split("|") if tok
        }
        if set(listed) != expected:
            problems.append(
                f"supporting_entities: existing_annotations[{i}] lists {sorted(listed)} "
                f"but GOA WITH/FROM is {sorted(expected)}"
            )


def check_motif_claims(doc: dict, notes: str, results: dict, problems: list[str]) -> None:
    """Residue claims in prose must match the computed alignment, not a remembered number."""
    sites = {r["site"]: r["targets"][SUBJECT] for r in results["sites"]}
    for site, expected_aa, expected_pos in [
        ("KxGQ_K", "K", 147),
        ("KxGQ_Q", "Q", 150),
        ("beta3_K", "K", 311),
        ("cat_D", "D", 445),
        ("DFG_D", "D", 493),
        ("Arich_A1", "G", 207),
        ("Arich_A3", "G", 209),
    ]:
        got = sites.get(site)
        if got is None:
            problems.append(f"motif: results.json has no site {site}")
            continue
        if (got["aa"], got["pos"]) != (expected_aa, expected_pos):
            problems.append(
                f"motif: {site} computed as {got['aa']}{got['pos']} but this script "
                f"expects {expected_aa}{expected_pos}; prose citing the old value is stale."
            )
    blob = yaml.safe_dump(doc) + notes
    for token in ["K147", "K311", "D445", "D493", "G207", "G209"]:
        if token not in blob:
            problems.append(f"motif: residue {token} is computed but cited nowhere in prose")
    # The alignment must remain trustworthy, or every residue claim above is unfounded.
    cc = results["control_checks"]
    if cc["pka_kxgq_matches"] != 0:
        problems.append(
            f"motif: negative control now matches {cc['pka_kxgq_matches']} KxGQ positions, "
            f"so KxGQ is no longer UbiB-diagnostic and the prose claim is unfounded."
        )
    if cc["columns_in_register"] < 6:
        problems.append(
            f"motif: only {cc['columns_in_register']}/{cc['columns_total']} columns in "
            f"register; the review claims 6."
        )


def check_retracted_phrasings(raw_review: str, notes: str, problems: list[str]) -> None:
    """Claims considered and rejected during review must not survive anywhere.

    Scans the RAW review text, not the parsed document: the parsed form drops comments,
    so a detector built on it is blind to part of the file it is supposed to police.
    Whitespace is normalised first, because YAML block scalars wrap long sentences and an
    un-normalised regex would miss any claim that happens to straddle a line break.
    """
    blob = re.sub(r"\s+", " ", raw_review + "\n" + notes)
    # Each pattern encodes the AFFIRMATIVE form of a rejected claim, and every hit is then
    # tested for a preceding negator. Two earlier versions of this check fired on correct
    # statements -- first on the bare word "pseudokinase", then on "neither is a
    # pseudokinase" after mere anchoring. A guard that rejects the truth is worse than no
    # guard, so negation handling is explicit rather than encoded in ever-longer regexes.
    # The negator must be in the SAME CLAUSE as the claim, so the window stops at any
    # sentence or clause boundary. A window that only forbids a full stop is too permissive:
    # "ADCK2 has no measured activity, and ADCK2 is a serine/threonine kinase" would be
    # suppressed by an incidental "no" belonging to a different clause. Punctuation and
    # coordinating conjunctions both close the window.
    # The clause-boundary lookahead is what does the work. A separate character budget can
    # now only ADD false positives -- it cannot make the guard stricter in any useful way,
    # because the boundary check already stops at punctuation and at coordinating
    # conjunctions -- and it introduced its own cliff (30 was too short for "no experiment
    # has ever shown that <claim>", 32 characters). So there is exactly one length limit
    # now, the size of the preceding window, rather than two that can disagree.
    negator = re.compile(
        r"\b(?:not|never|neither|nor|no|cannot|rather than|instead of|without|"
        r"isn't|dis(?:proved|proven)|refut\w*)\b(?:(?!\band\b|\bbut\b|\bwhile\b|"
        r"\bwhereas\b|\bhowever\b)[^.;,:])*$",
        re.I,
    )
    for pattern, why in [
        (r"ADCK2 is a (?:protein )?serine/threonine kinase", "never demonstrated"),
        (r"ADCK2 (?:is|acts as) an ATPase", "never measured for ADCK2"),
        (r"\bis a pseudokinase\b", "refuted: all four catalytic positions are intact"),
        (r"ADCK2 .{0,40}\bcatalys(?:es|is|ing) a step", "refuted by the labelling experiment"),
    ]:
        for m in re.finditer(pattern, blob, re.I):
            preceding = blob[max(0, m.start() - 90): m.start()]
            if negator.search(preceding):
                continue  # a negated mention is the correct statement, not a retracted one
            problems.append(f"retracted phrasing present ({why}): {m.group(0)!r}")


def check_sweep_exclusions_disclosed(raw_review: str, notes: str,
                                     problems: list[str]) -> None:
    """If the ontology sweep applies the quinoline false-friend exclusion, both prose
    surfaces must disclose it.

    This guards the exact defect a reviewer caught: after ``quinol`` was added to KEYWORDS,
    the sweep began applying TWO exclusion categories, while the justification still
    summarised only one ("every transport-flavoured one is an electron-transport term") --
    which the widening had made false. The script stayed honest; the prose describing it
    drifted. Keyed on the stable identifiers (the GO id and the code symbol) rather than on
    any sentence, because the sentence is the thing that gets reworded.
    """
    sweep = HERE / "coq_transport_term_check.py"
    if not sweep.exists():
        problems.append(f"sweep script missing: {sweep.name}")
        return
    src = sweep.read_text()
    if "QUINOLINE_FALSE_FRIEND" not in src:
        return  # the second exclusion category is not in play
    example = re.search(r"GO:\d{7}(?=\s+\"?quinolinic)", src) or re.search(
        r"(GO:1903222)", src
    )
    if not example:
        problems.append(
            "sweep applies the quinoline exclusion but names no GO id for it, so the "
            "prose surfaces cannot be checked against a stable identifier."
        )
        return
    gid = example.group(0)
    for surface, text in (("ADCK2-ai-review.yaml", raw_review), ("ADCK2-notes.md", notes)):
        if gid not in text:
            problems.append(
                f"sweep-exclusion disclosure: the ontology sweep excludes {gid} on "
                f"false-friend grounds, a second category beyond electron transport, but "
                f"{surface} never mentions it. Prose summarising the sweep must state "
                f"every exclusion category the sweep applies."
            )


# Import names of the dependencies this directory actually declares. Classifying an
# import failure as "environmental" against no reference set would announce an undeclared
# or misspelled import -- a real defect in the analysis code -- as a missing wheel, and
# skip it. Only a declared dependency going missing is an environment fact.
_DIST_TO_IMPORT = {"biopython": "Bio", "pyyaml": "yaml", "requests": "requests"}


def _declared_dependencies(directory: Path) -> tuple[set[str], list[str]]:
    """Top-level import names declared in this directory's pyproject.toml.

    Returns (import names, unmapped distribution names). Anchored on a line-initial
    ``dependencies`` key so a ``dev-dependencies``/``optional-dependencies`` table
    appearing first is not parsed instead. Every degenerate path yields an empty set,
    which makes the caller REPORT rather than excuse -- the correct bias for a classifier
    whose failure mode is excusing a defect.
    """
    pyproject = directory / "pyproject.toml"
    if not pyproject.exists():
        return set(), []
    block = re.search(r"^dependencies\s*=\s*\[(.*?)\]", pyproject.read_text(),
                      re.S | re.M)
    if not block:
        return set(), []
    names: set[str] = set()
    unmapped: list[str] = []
    for raw in re.findall(r"[\"']([^\"']+)[\"']", block.group(1)):
        dist = re.split(r"[<>=!~\[; ]", raw.strip(), maxsplit=1)[0].lower()
        if dist not in _DIST_TO_IMPORT:
            # An unmapped dist is not silently guessed at: guessing would drop it from the
            # declared set on the next dependency whose import name differs from its
            # distribution name, quietly re-opening the failure this classifier fixes.
            unmapped.append(dist)
            continue
        names.add(_DIST_TO_IMPORT[dist])
    return names, unmapped


def _is_missing_declared_dep(exc: BaseException, path: Path, module_name: str) -> bool:
    """True only for a DECLARED third-party dependency that this environment lacks."""
    if not isinstance(exc, ModuleNotFoundError):
        return False
    missing = getattr(exc, "name", None)
    if missing in (None, module_name):
        return False
    if (path.parent / f"{missing}.py").exists():
        return False  # a sibling script, so a genuine intra-repo break
    top = missing.split(".")[0]
    declared, _unmapped = _declared_dependencies(path.parent)
    if top not in declared:
        return False
    # A bad SUBMODULE of a dependency that IS installed is a defect in the sibling script,
    # not a missing wheel: "import requests.sessionz" raises with name requests.sessionz,
    # whose top-level component is declared and present. Only an absent top-level package
    # is an environment fact.
    # This function is called from inside _load_local_module's exception handler, whose
    # documented contract is that it returns rather than raises -- a raising check aborts
    # every later check. find_spec can itself raise (a ValueError for a module with no
    # __spec__, an ImportError while importing a parent package), so the one call that can
    # is made total here. Not error-hiding: any failure resolves to False, i.e. REPORT the
    # import failure rather than excuse it, which is this classifier's safe direction.
    try:
        return importlib.util.find_spec(top) is None
    except Exception:  # noqa: BLE001 - deliberately total; failure means "report"
        return False


_MODULE_CACHE: dict[str, object] = {}


def _load_local_module(path: Path):
    """Import a sibling analysis script once per process (run() is called ~15x by
    --self-test), returning None if it cannot be imported.

    Two non-obvious requirements. The module must be registered in ``sys.modules`` before
    execution -- documented practice for ``spec_from_file_location`` generally, and the
    observed failure here was ``@dataclass`` resolving its class's ``__module__`` through
    ``sys.modules`` and dying with an opaque ``AttributeError``; that was the symptom that
    surfaced it, not necessarily the only consumer. And an import failure is returned
    rather than raised, because a check that raises aborts every later check in this
    harness -- the rule this file states in its own header.
    """
    key = str(path)
    if key not in _MODULE_CACHE:
        name = f"_audit_{path.stem}"
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        sys.modules[name] = mod
        try:
            spec.loader.exec_module(mod)
        except Exception as exc:  # noqa: BLE001 - reported, not swallowed
            sys.modules.pop(name, None)
            _MODULE_CACHE[key] = None
            _MODULE_CACHE[key + ":error"] = f"{type(exc).__name__}: {exc}"
            # A third-party import the sibling script needs but this environment lacks is
            # an environment fact, not a defect in the review. Conflating the two would
            # make a missing wheel read as a claim failure and, because run(base) is
            # evaluated before every mutation, abort --self-test entirely -- turning a
            # degraded harness into an unrunnable one.
            _MODULE_CACHE[key + ":environmental"] = _is_missing_declared_dep(exc, path, name)
        else:
            _MODULE_CACHE[key] = mod
    return _MODULE_CACHE[key]


def _import_problem(path: Path) -> str:
    return (f"could not import {path.name}: "
            f"{_MODULE_CACHE.get(str(path) + ':error', 'unknown error')}")


def _report_import_failure(path: Path, problems: list[str]) -> None:
    """Append a problem for a genuine break; announce loudly and skip for a missing
    third-party dependency, so a degraded environment never masquerades as a defect and
    never silently reduces coverage either."""
    err = _MODULE_CACHE.get(str(path) + ":error", "unknown error")
    if _MODULE_CACHE.get(str(path) + ":environmental"):
        # Announce once per path: --self-test calls run() ~16 times, and repeating the
        # notice would bury the mutation log it is meant to be read alongside.
        if not _MODULE_CACHE.get(str(path) + ":announced"):
            _MODULE_CACHE[str(path) + ":announced"] = True
            print(f"  SKIPPED unit pin on {path.name}: {err} "
                  f"(environment lacks a declared dependency; this is not a claim defect, "
                  f"but the check did NOT run)")
        return
    problems.append(_import_problem(path))


def check_prose_join_helper(problems: list[str]) -> None:
    """Pin the motif report's prose list-join at 0/1/2/3 items.

    Three-plus is unreachable at the current alignment membership, which is exactly why a
    regression there would ship unnoticed -- the same reason the bare ' and '.join it
    replaced survived several rounds. Cheap to pin, so pinned in the tree rather than in a
    commit message.
    """
    motif = HERE / "ubib_motif_analysis.py"
    if not motif.exists():
        problems.append(f"motif script missing: {motif.name}")
        return
    mod = _load_local_module(motif)
    if mod is None:
        _report_import_failure(motif, problems)
        return
    fn = getattr(mod, "_english_list", None)
    if fn is None:
        problems.append("motif script no longer defines _english_list")
        return
    for items, expected in [
        ([], "none"),
        (["A"], "A"),
        (["A", "B"], "A and B"),
        (["A", "B", "C"], "A, B and C"),
    ]:
        got = fn(items)
        if got != expected:
            problems.append(f"prose join: {items} -> {got!r}, expected {expected!r}")


def check_import_failure_reporter(problems: list[str]) -> None:
    """Pin _report_import_failure on both classes, and the dependency classifier itself.

    Mostly cheap: the reporter reads only _MODULE_CACHE, so its two paths are exercised by
    seeding synthetic keys, with no broken file on disk. The two classifier assertions that
    depend on whether a wheel is installed DO scope importlib.util.find_spec for their
    duration, restoring it in a finally -- one because the absent-wheel branch is
    unreachable in a healthy environment, the other because the installed-wheel branch is
    unreachable in a degraded one. Pinning either to the ambient environment would make
    this pin report a claim defect on a machine that merely lacks a dependency, which is
    the failure it exists to prevent.

    Note the limit of the mandatory-map assertion below: it pins that every declared
    distribution HAS an entry in _DIST_TO_IMPORT, not that the entry is correct. Checking
    correctness would mean importing each name, which is environment-dependent and so
    reintroduces the very coupling this docstring is about.
    """
    fake = HERE / "__synthetic_for_audit__.py"
    key = str(fake)
    saved = {k: _MODULE_CACHE.get(k) for k in
             (key, key + ":error", key + ":environmental", key + ":announced")}
    try:
        # Genuine break must be reported.
        _MODULE_CACHE[key + ":error"] = "RuntimeError: synthetic"
        _MODULE_CACHE[key + ":environmental"] = False
        _MODULE_CACHE.pop(key + ":announced", None)
        found: list[str] = []
        _report_import_failure(fake, found)
        if len(found) != 1:
            problems.append(
                f"import reporter: a genuine break produced {len(found)} problems, expected 1"
            )
        # Missing declared dependency must skip rather than report, and must announce
        # exactly once however many times run() calls it. Output is captured so this pin
        # neither emits a notice about a file that does not exist nor suppresses a real one.
        _MODULE_CACHE[key + ":environmental"] = True
        _MODULE_CACHE.pop(key + ":announced", None)
        skipped: list[str] = []
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            _report_import_failure(fake, skipped)
            _report_import_failure(fake, skipped)
        if skipped:
            problems.append(
                f"import reporter: a missing declared dependency was reported as a "
                f"problem ({skipped[0]}) instead of skipped"
            )
        notices = buf.getvalue().count("SKIPPED unit pin")
        if notices != 1:
            problems.append(
                f"import reporter: two calls emitted {notices} SKIPPED notices, expected "
                f"exactly 1 (announce once per path, not once per run)"
            )
        # The classifier must excuse exactly one thing: a declared dependency that is
        # genuinely absent. Everything else is a defect in the code under audit.
        def _mnfe(name: str) -> ModuleNotFoundError:
            exc = ModuleNotFoundError(f"No module named '{name}'")
            exc.name = name
            return exc

        if _is_missing_declared_dep(_mnfe("definitely_not_declared"), fake, "_x"):
            problems.append(
                "import classifier: an UNDECLARED missing module was classified as an "
                "environment fact; an undeclared or misspelled import is a code defect."
            )
        # Scope find_spec to report the package PRESENT, mirroring the absent-wheel case
        # below. Without this the assertion hardcodes the requests wheel: on a machine
        # without it, "import requests.sessionz" genuinely IS a missing-wheel event, the
        # classifier correctly returns True, and this pin would report a claim defect
        # saying "requests is present" in an environment where it is not.
        real_find_spec = importlib.util.find_spec
        try:
            importlib.util.find_spec = (
                lambda n, *a, **k: object() if n == "requests"
                else real_find_spec(n, *a, **k)
            )
            if _is_missing_declared_dep(_mnfe("requests.sessionz"), fake, "_x"):
                problems.append(
                    "import classifier: a bad SUBMODULE of an installed declared "
                    "dependency was excused as a missing wheel; the top-level package is "
                    "present, so that is a typo in the sibling script."
                )
        finally:
            importlib.util.find_spec = real_find_spec
        # The absent-wheel branch depends on the environment, so it is unreachable while
        # every declared dependency is installed. Reached by scoping find_spec to report
        # the package absent, restored immediately -- the only way to exercise it at all.
        real_find_spec2 = importlib.util.find_spec
        try:
            importlib.util.find_spec = (
                lambda n, *a, **k: None if n == "requests" else real_find_spec2(n, *a, **k)
            )
            if not _is_missing_declared_dep(_mnfe("requests"), fake, "_x"):
                problems.append(
                    "import classifier: a DECLARED dependency that is absent was not "
                    "recognised, so a missing wheel would report as a claim defect."
                )
        finally:
            importlib.util.find_spec = real_find_spec2
        # Every declared distribution must be mapped, or it silently leaves the declared
        # set and re-opens the failure this classifier exists to fix.
        _declared, unmapped = _declared_dependencies(HERE)
        if unmapped:
            problems.append(
                f"import classifier: declared distributions with no entry in "
                f"_DIST_TO_IMPORT: {sorted(unmapped)}. Add their import names; guessing "
                f"would drop them from the declared set silently."
            )
    finally:
        for k, v in saved.items():
            if v is None:
                _MODULE_CACHE.pop(k, None)
            else:
                _MODULE_CACHE[k] = v


def check_false_friend_helper(problems: list[str]) -> None:
    """Pin the sweep's false-friend classifier with labels that discriminate the two rules.

    The distinguishing case is `pyrroloquinoline quinone biosynthetic process`: it contains
    the false friend AND matches on its own `quinone`, so the superseded "contains quinolin
    and names no real CoQ species" rule would have excluded it while reporting the wrong
    reason. Living in the audit rather than in a commit message means the next edit to that
    function has to keep it true.
    """
    sweep = HERE / "coq_transport_term_check.py"
    if not sweep.exists():
        problems.append(f"sweep script missing: {sweep.name}")
        return
    mod = _load_local_module(sweep)
    if mod is None:
        _report_import_failure(sweep, problems)
        return
    fn = getattr(mod, "matched_only_via_quinoline", None)
    if fn is None:
        problems.append(
            "sweep no longer defines matched_only_via_quinoline; the false-friend "
            "classifier is unguarded."
        )
        return
    for label, expected in [
        ("quinolinic acid transmembrane transport", True),
        ("pyrroloquinoline quinone biosynthetic process", False),
        ("ubiquinol transport", False),
        ("quinoline metabolic process", True),
        ("ubiquinol-quinoline hybrid transport", False),
    ]:
        got = fn(label)
        if got is not expected:
            problems.append(
                f"false-friend classifier: {label!r} -> {got}, expected {expected}"
            )


def check_raw_vs_parsed(raw: str, problems: list[str]) -> None:
    """Reconcile raw ``- reference_id:`` lines against parsed ``supported_by`` entries.

    NOT a duplicate-key guard, despite what this docstring used to claim. StrictLoader owns
    that case outright: ``_no_duplicates`` raises ``ConstructorError``, a ``YAMLError``
    subclass, and ``run()`` returns early on it, so a duplicated key never reaches here.
    Verified by injecting one -- ``run()`` returns a single "YAML: duplicate key" problem and
    this check is never called.

    What the count comparison still catches is the residual: a ``supported_by`` entry that
    has lost its ``reference_id`` key, or a ``reference_id`` line buried in a block scalar
    where parsing will not see it. The check earns its place, just not for the reason
    originally stated.

    Takes the document text rather than re-reading REVIEW from disk, so it inspects the same
    document as every other check in ``run()`` and needs no gate.
    """
    raw_count = len(re.findall(r"^\s*- reference_id:", raw, re.M))
    doc = yaml.safe_load(raw)

    def walk(node):
        if isinstance(node, dict):
            for k, v in node.items():
                if k == "supported_by" and isinstance(v, list):
                    yield from (e for e in v if isinstance(e, dict))
                else:
                    yield from walk(v)
        elif isinstance(node, list):
            for e in node:
                yield from walk(e)

    parsed_count = sum(1 for _ in walk(doc))
    if raw_count != parsed_count:
        problems.append(
            f"raw/parsed: {raw_count} '- reference_id:' lines in the file but "
            f"{parsed_count} parsed supported_by entries. Do not explain the gap away - "
            f"derive the expected count independently. Likely causes: a supported_by entry "
            f"that has lost its reference_id key, or a reference_id line inside a block "
            f"scalar. (Duplicate mapping keys cannot cause this - StrictLoader rejects "
            f"those before this check runs.)"
        )


def run(review_text: str | None = None, notes_text: str | None = None) -> list[str]:
    problems: list[str] = []
    raw = review_text if review_text is not None else REVIEW.read_text()
    try:
        doc = yaml.load(raw, Loader=StrictLoader)
    except yaml.YAMLError as exc:
        return [f"YAML: {exc}"]
    goa = load_goa(GOA)
    notes = notes_text if notes_text is not None else NOTES.read_text()
    results = json.loads(RESULTS_JSON.read_text())

    check_row_coverage(doc, goa, problems)
    check_source_entities(doc, goa, problems)
    check_supporting_entities(doc, goa, problems)
    check_motif_claims(doc, notes, results, problems)
    check_retracted_phrasings(raw, notes, problems)
    check_sweep_exclusions_disclosed(raw, notes, problems)
    # None of the checks below needs a gate, for two reasons. The unit pins inspect
    # sibling modules or this file's own helpers rather than the document, so the
    # caller's overrides cannot affect them. And the raw/parsed check now inspects
    # whichever document run() was given instead of re-reading REVIEW from disk.
    # Deliberately phrased without a count: two earlier versions of this comment named a
    # number that the next commit changed, which is the N-1 shape the header opens with.
    check_import_failure_reporter(problems)
    check_false_friend_helper(problems)
    check_prose_join_helper(problems)
    check_raw_vs_parsed(raw, problems)
    return problems


def self_test() -> int:
    """Each mutation must make the audit fail. Assert the target exists before mutating,
    so a drifted anchor is an error rather than a guard that silently proves nothing."""
    base = REVIEW.read_text()
    base_notes = NOTES.read_text()
    if run(base):
        print("SELF-TEST ABORTED: the unmutated document already fails")
        for p in run(base):
            print("  -", p)
        return 1

    mutations = [
        ("drop a source_entity", "      - source_id: SGD:S000006030", ""),
        ("relabel a source_id", "source_id: MGI:MGI:1889336", "source_id: MGI:MGI:9999999"),
        ("revert a verdict to PENDING", "    action: MARK_AS_OVER_ANNOTATED",
         "    action: PENDING"),
        ("delete a whole annotation entry", "- term:\n    id: GO:0010795", "- term:\n    id: GO:9999999"),
        ("assert a refuted claim", "gene_symbol: ADCK2",
         "gene_symbol: ADCK2\ndescription_note: ADCK2 is a serine/threonine kinase"),
        ("assert the pseudokinase claim", "gene_symbol: ADCK2",
         "gene_symbol: ADCK2\ndescription_note: the protein is a pseudokinase"),
        ("assert ADCK2 catalyses a pathway step", "gene_symbol: ADCK2",
         "gene_symbol: ADCK2\ndescription_note: ADCK2 catalyses a step of CoQ synthesis"),
        # Decoy negator in a DIFFERENT clause: the guard must not be disarmed by an
        # incidental "no" that does not negate the claim itself.
        ("decoy negator before an asserted claim", "gene_symbol: ADCK2",
         "gene_symbol: ADCK2\ndescription_note: there is no purified protein, and ADCK2 is"
         " a serine/threonine kinase"),
        ("drop the GO:1903222 sweep-exclusion disclosure", "GO:1903222", "GO:0000000"),
        # Drives check_raw_vs_parsed: renaming the key drops a raw "- reference_id:"
        # line while the parsed supported_by entry survives, so the counts diverge. This
        # became testable only once the check took the document text instead of re-reading
        # REVIEW from disk.
        ("strip a reference_id key from a supported_by entry",
         "    - reference_id: PMID:34362905", "    - reference_id_typo: PMID:34362905"),
        ("decoy negator across a full stop", "gene_symbol: ADCK2",
         "gene_symbol: ADCK2\ndescription_note: the assay was not run. ADCK2 is a"
         " serine/threonine kinase"),
    ]
    failures = 0

    # False-positive tests: these mutations are CORRECT statements and must NOT be
    # flagged. Two successive versions of the retracted-phrasing check failed exactly
    # here, so the "guard must stay quiet" case is tested as deliberately as the
    # "guard must fire" case.
    must_not_fire = [
        ("negated pseudokinase claim", "gene_symbol: ADCK2",
         "gene_symbol: ADCK2\ndescription_note: neither gene is a pseudokinase"),
        ("negated kinase claim", "gene_symbol: ADCK2",
         "gene_symbol: ADCK2\ndescription_note: it is not the case that ADCK2 is a"
         " serine/threonine kinase"),
        # A long but genuine negation: 32 characters separate the negator from the claim,
        # which the earlier 30-character budget wrongly rejected.
        ("long-range negation in the same clause", "gene_symbol: ADCK2",
         "gene_symbol: ADCK2\ndescription_note: no experiment has ever shown that ADCK2 is"
         " a serine/threonine kinase"),
    ]
    for name, target, replacement in must_not_fire:
        if target not in base:
            print(f"  BROKEN GUARD: false-positive target for {name!r} not present")
            failures += 1
            continue
        if run(base.replace(target, replacement, 1)):
            print(f"  FALSE POSITIVE: {name} was flagged but is a correct statement")
            failures += 1
        else:
            print(f"  correctly ignored: {name}")

    # The two-surface disclosure guard has a notes branch that no review-text mutation can
    # reach. Exercise it directly, or half of that loop is only asserted, never observed.
    notes_mutations = [
        ("drop the GO:1903222 disclosure from the NOTES surface", "GO:1903222", "GO:0000000"),
    ]
    for name, target, replacement in notes_mutations:
        if target not in base_notes:
            print(f"  BROKEN GUARD: notes mutation target for {name!r} not present")
            failures += 1
            continue
        if not run(notes_text=base_notes.replace(target, replacement)):
            print(f"  NOT CAUGHT: {name}")
            failures += 1
        else:
            print(f"  caught: {name}")

    for name, target, replacement in mutations:
        if target not in base:
            print(f"  BROKEN GUARD: mutation target for {name!r} not present in the file; "
                  f"this self-test proves nothing")
            failures += 1
            continue
        mutated = base.replace(target, replacement, 1)
        if mutated == base:
            print(f"  BROKEN GUARD: mutation {name!r} was a no-op")
            failures += 1
            continue
        if not run(mutated):
            print(f"  NOT CAUGHT: {name}")
            failures += 1
        else:
            print(f"  caught: {name}")
    print("self-test:", "PASS" if failures == 0 else f"FAIL ({failures})")
    return 1 if failures else 0


def main() -> int:
    if "--self-test" in sys.argv:
        return self_test()
    problems = run()
    if problems:
        print(f"{len(problems)} problem(s):")
        for p in problems:
            print("  -", p)
        return 1
    print("audit: all invariants hold")
    return 0


if __name__ == "__main__":
    sys.exit(main())
