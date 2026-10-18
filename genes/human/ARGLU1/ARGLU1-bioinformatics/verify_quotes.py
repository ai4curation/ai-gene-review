#!/usr/bin/env python3
"""Check EVERY supporting_text in the review against its cached publication.

Why this is not redundant with `just validate`: for a reference whose cache is
abstract-only, `src/ai_gene_review/validation/validator.py:156` downgrades a
non-matching quote from ERROR to **WARNING**. So a paraphrase against an
abstract-only source does not fail the build.

**That downgrade is reachable on ONE path only.** The enclosing loop iterates
``reference.get("findings", [])`` with the path template
``references[{i}].findings[{j}].supporting_text`` (`validator.py:124-130`);
``review.supported_by`` and friends are validated by the external CLI instead, a
split that `validation/supporting_text.py:14-26` documents explicitly.

The first version of this script got that exactly backwards. Its collector
required ``reference_id`` and ``supporting_text`` on the **same dict**, but
``references[].findings[]`` entries carry ``statement`` + ``supporting_text`` with
the identifier on the **parent** ``references[].id``. So it silently skipped all
22 findings quotes -- covering the 61 that the strict CLI already gates and
missing every one of the 22 gated by the weak branch it cited as its reason for
existing. Eight of those 22 are on abstract-only sources.

It reported "quotes found: 61" and read as complete coverage at 73%.

Two structural fixes follow, both of which a future shape change has to survive:

* the collector inherits the parent ``references[].id`` when walking into
  ``findings``; and
* the number of quotes collected is asserted equal to the number of
  ``supporting_text:`` keys in the RAW text. A collector that cannot see part of
  the document now fails loudly instead of under-reporting.

Matching goes through ``build_supporting_text_validator()`` -- the repo's own
helper, configured from ``conf/reference_validator_config.yaml`` -- so "the same
matcher the validator uses" is literally true rather than approximately true, and
``literal_bracket_patterns`` / ``skip_prefixes`` apply as they do in the gate.

Run:        uv run python verify_quotes.py
Self-test:  uv run python verify_quotes.py --self-test
"""

from __future__ import annotations

import copy
import json
import re
import sys
from pathlib import Path

import yaml


def repo_root() -> Path:
    for base in (Path(__file__).resolve(), Path.cwd().resolve()):
        for p in (base, *base.parents):
            if (p / "genes").is_dir() and (p / "src").is_dir():
                return p
    raise SystemExit("repo root not found")


ROOT = repo_root()
REVIEW = ROOT / "genes/human/ARGLU1/ARGLU1-ai-review.yaml"
PUBS = ROOT / "publications"
OUT = Path(__file__).resolve().parent / "quote_verification.json"

sys.path.insert(0, str(ROOT / "src"))
from ai_gene_review.validation.supporting_text import (  # noqa: E402
    build_supporting_text_validator,
)


def make_validator():
    """Build the repo's configured validator, failing loudly if unavailable.

    ``build_supporting_text_validator`` returns ``(None, dir)`` when the external
    dependency is missing. Silently degrading to a hand-rolled substring test is
    how the previous version drifted away from the gate it claimed to mirror.
    """
    validator, pubdir = build_supporting_text_validator(PUBS)
    if validator is None:
        raise SystemExit(
            "linkml_reference_validator is not installed, so this script cannot use "
            "the same matcher as the repo validator.\n"
            "Install it (uv sync) rather than falling back to an approximate test."
        )
    return validator, pubdir


def collect(doc) -> list[dict]:
    """Every quote in the document, with the reference it is attributed to.

    Handles BOTH shapes:
      * same-dict:  {reference_id, supporting_text}   (review.supported_by, ...)
      * parent-id:  references[i].id + findings[j].supporting_text
    """
    out: list[dict] = []

    def walk(node, path="root", inherited_ref=None):
        if isinstance(node, dict):
            # A references[] entry supplies its id to everything beneath it.
            ref_here = node.get("id") if "findings" in node else None
            ref_for_children = ref_here or inherited_ref

            own_ref = node.get("reference_id")
            txt = node.get("supporting_text")
            if isinstance(txt, str) and txt.strip():
                ref = own_ref if isinstance(own_ref, str) else inherited_ref
                out.append({
                    "path": path,
                    "reference_id": ref,
                    "supporting_text": txt,
                    "via": "same-dict" if isinstance(own_ref, str) else "parent-id",
                })
            for k, v in node.items():
                walk(v, f"{path}.{k}", ref_for_children)
        elif isinstance(node, list):
            for i, v in enumerate(node):
                walk(v, f"{path}[{i}]", inherited_ref)

    walk(doc)
    return out


def raw_quote_key_count(text: str) -> int:
    return len(re.findall(r"^\s*supporting_text:", text, re.M))


def cache_is_abstract_only(pmid: str) -> bool | None:
    pub = PUBS / f"PMID_{pmid}.md"
    if not pub.exists():
        return None
    body = pub.read_text()
    if not body.startswith("---"):
        return True
    front = body.split("---", 2)[1]
    return "full_text_available: true" not in front


def check(doc, raw_text: str) -> tuple[list[str], dict]:
    validator, _ = make_validator()
    quotes = collect(doc)

    problems: list[str] = []

    # Coverage invariant: the collector must see every quote key in the raw file.
    raw_n = raw_quote_key_count(raw_text)
    if len(quotes) != raw_n:
        problems.append(
            f"COVERAGE: collector found {len(quotes)} quote(s) but the raw file has "
            f"{raw_n} 'supporting_text:' key(s). A collector that cannot see part of "
            "the document under-reports instead of failing -- fix the walk, do not "
            "adjust this assertion."
        )

    stats = {
        "quotes_total": len(quotes),
        "raw_supporting_text_keys": raw_n,
        "by_shape": {},
        "abstract_only_quotes": 0,
        "abstract_only_references": [],
        "checked": 0,
        "unresolved_reference": 0,
    }
    for q in quotes:
        stats["by_shape"][q["via"]] = stats["by_shape"].get(q["via"], 0) + 1

    for q in quotes:
        ref = q["reference_id"]
        if not isinstance(ref, str):
            problems.append(f"{q['path']}: quote has no resolvable reference id")
            stats["unresolved_reference"] += 1
            continue
        if not ref.startswith("PMID:"):
            continue
        pmid = ref.split(":", 1)[1]
        abstract_only = cache_is_abstract_only(pmid)
        if abstract_only is None:
            problems.append(f"{q['path']}: {ref} has no cached publication")
            continue
        if abstract_only:
            stats["abstract_only_quotes"] += 1
            if ref not in stats["abstract_only_references"]:
                stats["abstract_only_references"].append(ref)

        result = validator.validate(q["supporting_text"], ref)
        stats["checked"] += 1
        if not result.is_valid:
            gate = ("abstract-only: the repo gate would only WARN here"
                    if abstract_only else "full-text: the repo gate would ERROR")
            problems.append(
                f"{q['path']} [{q['via']}]: quote is NOT verbatim in {ref}  ({gate})"
                f"\n      {q['supporting_text'][:130]}"
            )

    stats["abstract_only_references"].sort()
    return problems, stats


def self_test() -> int:
    raw = REVIEW.read_text()
    doc = yaml.safe_load(raw)
    problems, stats = check(doc, raw)
    if problems:
        print("SELF-TEST ABORTED: baseline already has problems:")
        for p in problems:
            print("  -", p)
        return 1

    failures: list[str] = []

    def corrupt(target_path_contains: str, label: str, expect_gate: str):
        """Corrupt exactly one quote whose path matches, assert it is detected."""
        mutated = copy.deepcopy(doc)
        hits = [q for q in collect(mutated) if target_path_contains in q["path"]]
        if len(hits) != 1:
            failures.append(
                f"{label}: expected exactly 1 quote at {target_path_contains!r}, "
                f"found {len(hits)} -- target drifted, so this case would not test "
                "what it was written for"
            )
            return
        want = hits[0]["path"]
        changed = 0

        def walk(node, path="root"):
            nonlocal changed
            if isinstance(node, dict):
                if path == want and isinstance(node.get("supporting_text"), str):
                    node["supporting_text"] += " and then something nobody wrote."
                    changed += 1
                for k, v in node.items():
                    walk(v, f"{path}.{k}")
            elif isinstance(node, list):
                for i, v in enumerate(node):
                    walk(v, f"{path}[{i}]")

        walk(mutated)
        if changed != 1:
            failures.append(f"{label}: mutated {changed} quotes, expected 1")
            return
        probs, _ = check(mutated, raw)
        # Detection must name THIS path and THIS gate, not merely be non-empty.
        hit = [p for p in probs if want in p and expect_gate in p]
        if hit:
            print(f"  ok  {label}: detected at {want}")
        else:
            failures.append(
                f"{label}: corruption at {want} not detected with gate {expect_gate!r}; "
                "got: " + " | ".join(p[:110] for p in probs)
            )

    # The findings path on an abstract-only source is the case the previous
    # version could not see AND the only path the ERROR->WARNING downgrade covers.
    abs_findings = [q for q in collect(doc)
                    if q["via"] == "parent-id"
                    and q["reference_id"] == "PMID:22923044"]
    if not abs_findings:
        failures.append("no abstract-only findings quote found for PMID:22923044")
    else:
        corrupt(abs_findings[0]["path"], "findings path, abstract-only source",
                "abstract-only")

    full_supported = [q for q in collect(doc)
                      if q["via"] == "same-dict"
                      and q["reference_id"] == "PMID:30698747"]
    corrupt(full_supported[0]["path"], "supported_by path, full-text source",
            "full-text")

    # Coverage invariant must fire if the collector is crippled.
    crippled = copy.deepcopy(doc)
    for r in crippled.get("references", []):
        r.pop("findings", None)
    probs, _ = check(crippled, raw)
    if any("COVERAGE:" in p for p in probs):
        print("  ok  coverage invariant: fired when findings were removed")
    else:
        failures.append("coverage invariant did NOT fire on a crippled document")

    if failures:
        print("\nSELF-TEST FAILED:")
        for f in failures:
            print("  -", f)
        return 1
    print("\nself-test: all cases detected")
    return 0


def main() -> int:
    if "--self-test" in sys.argv:
        return self_test()

    raw = REVIEW.read_text()
    doc = yaml.safe_load(raw)
    problems, stats = check(doc, raw)

    print(f"supporting_text keys in file : {stats['raw_supporting_text_keys']}")
    print(f"quotes collected             : {stats['quotes_total']}  "
          f"{stats['by_shape']}")
    print(f"checked against cache        : {stats['checked']}")
    print(f"on abstract-only sources     : {stats['abstract_only_quotes']} quote(s) "
          f"across {len(stats['abstract_only_references'])} reference(s)")
    print(f"   {stats['abstract_only_references']}")
    print("   (the repo gate only WARNs on these, and only on the findings path)")
    print()

    OUT.write_text(json.dumps(
        {"stats": stats, "problems": problems}, indent=2, sort_keys=True))

    if problems:
        print(f"{len(problems)} problem(s):")
        for p in problems:
            print("  -", p)
        print(f"\nwrote {OUT}")
        return 1
    print("every quote is verbatim in its cached source (repo matcher)")
    print(f"wrote {OUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
