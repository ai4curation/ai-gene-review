"""Checks on ARHGAP36-ai-review.yaml that the schema validator does not make.

These are the failures that have actually shipped in this campaign, so each one is a
guard rather than a style note:

1. **Folded-scalar reflow.** ``>-`` turns a newline into a *space*, so wrapping
   ``arginine-finger`` across lines publishes ``arginine- finger``. Both forms are legal
   YAML and validation passes; only rendering shows the damage. No line inside a folded
   block may end in a hyphen.

2. **Duplicate YAML keys.** A duplicate key is silently last-wins in the default loader,
   so a second ``action:`` under one review would quietly override the first.

3. **GOA reconciliation.** Every row in the GOA TSV must appear in
   ``existing_annotations``, and every non-NEW entry must correspond to a GOA row. A
   hand tally of actions is checked against the file rather than written beside it.

4. **Residue claims are re-resolved against the actual sequences.** This is the point of
   the file. The review asserts that specific positions in specific proteins hold
   specific residues, and those assertions are cheap to make and easy to get wrong.
   Every ``anchor`` and ``target`` is fetched from UniProt and the residue is read off
   the sequence. A claim whose residue does not match is an error, not a warning.

5. **Propagated evidence that is demoted must say why.** Any REMOVE or
   MARK_AS_OVER_ANNOTATED on an IBA/IEA/ISS row must carry a ``propagation_review``.

6. **No experimental annotation may be removed or demoted.** ARHGAP36 has none today,
   so this check is vacuous now and is kept because it would stop being vacuous the
   moment GOA gains one.

Usage:
    uv run --no-project --with "pyyaml>=6.0" python check_review.py
    uv run --no-project --with "pyyaml>=6.0" python check_review.py --self-test
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
import urllib.error
import urllib.request
from collections import Counter
from pathlib import Path
from typing import Any

import yaml

SCRIPT_DIR = Path(__file__).resolve().parent
GENE_DIR = SCRIPT_DIR.parent
REVIEW = GENE_DIR / "ARHGAP36-ai-review.yaml"
GOA = GENE_DIR / "ARHGAP36-goa.tsv"
CACHE_DIR = SCRIPT_DIR / "cache"

PROPAGATED_EVIDENCE = {"IBA", "IEA", "ISS", "ISA", "ISO", "ISM", "IGC", "RCA", "IBD", "IKR", "IRD"}
EXPERIMENTAL_EVIDENCE = {"EXP", "IDA", "IPI", "IMP", "IGI", "IEP", "HDA", "HMP", "HGI", "HEP"}
DEMOTING_ACTIONS = {"REMOVE", "MARK_AS_OVER_ANNOTATED"}


class CheckError(RuntimeError):
    """A hard failure."""


class StrictLoader(yaml.SafeLoader):
    """SafeLoader that refuses duplicate mapping keys instead of silently last-winning."""


def _no_duplicates(loader: yaml.Loader, node: yaml.MappingNode, deep: bool = False) -> dict[str, Any]:
    mapping: dict[str, Any] = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in mapping:
            raise CheckError(f"duplicate YAML key {key!r} at line {key_node.start_mark.line + 1}")
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


StrictLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _no_duplicates)


# --- 1. folded-scalar reflow ----------------------------------------------------


def folded_block_hyphen_breaks(text: str) -> list[tuple[int, str]]:
    """Lines inside a folded (``>``) scalar that end in a hyphen and are followed by more text.

    Block extent is taken from the YAML parser's own scalar events rather than from
    indentation heuristics. The first attempt at this walked indentation by hand and
    flagged every *nested* block opener, because ``supporting_text: >-`` itself ends in a
    hyphen -- 43 false positives on a clean file. Asking the parser where each folded
    scalar starts and ends removes the guesswork.

    Only non-final body lines are flagged: a hyphen on the last line of a ``>-`` block
    folds into nothing, so it cannot produce the ``word- next`` corruption this guards
    against.
    """
    lines = text.splitlines()
    offenders: list[tuple[int, str]] = []
    for event in yaml.parse(text, Loader=yaml.SafeLoader):
        if not isinstance(event, yaml.ScalarEvent) or event.style != ">":
            continue
        first = event.start_mark.line  # 0-based; the line carrying the '>' indicator
        last = event.end_mark.line  # 0-based, exclusive-ish
        body = [(n, lines[n]) for n in range(first + 1, min(last, len(lines))) if lines[n].strip()]
        for idx, (n, line) in enumerate(body):
            if idx == len(body) - 1:
                continue  # final line: the fold has nothing to join it to
            if line.rstrip().endswith("-"):
                offenders.append((n + 1, line.strip()))
    return offenders


# --- 4. residue claims ----------------------------------------------------------


def fetch_sequence(acc: str) -> str:
    dest = CACHE_DIR / f"{acc}.json"
    if dest.exists() and dest.stat().st_size > 0:
        rec = json.loads(dest.read_bytes())
    else:
        dest.parent.mkdir(parents=True, exist_ok=True)
        url = f"https://rest.uniprot.org/uniprotkb/{acc}.json"
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"Accept": "application/json"}), timeout=120) as fh:
                payload = fh.read()
        except (urllib.error.URLError, urllib.error.HTTPError) as exc:
            raise CheckError(f"could not fetch {url}: {exc}; this check has no offline fallback") from exc
        dest.write_bytes(payload)
        rec = json.loads(payload)
    seq = rec.get("sequence", {}).get("value")
    if not seq:
        raise CheckError(f"UniProt {acc} returned no sequence")
    return seq


def iter_residue_claims(review: dict[str, Any]):
    for ann in review.get("existing_annotations", []):
        prop = (ann.get("review") or {}).get("propagation_review") or {}
        for claim in prop.get("residue_claims", []) or []:
            yield ann["term"]["id"], claim


def check_residue_claims(review: dict[str, Any], seq_override: dict[str, str] | None = None) -> list[dict[str, Any]]:
    rows = []
    for term_id, claim in iter_residue_claims(review):
        for side in ("anchor", "target"):
            spec = claim.get(side)
            if spec is None:
                continue
            acc = str(spec["accession"]).split(":", 1)[-1]
            seq = (seq_override or {}).get(acc) or fetch_sequence(acc)
            pos = int(spec["position"])
            if pos > len(seq):
                raise CheckError(
                    f"{term_id}: {side} {acc} position {pos} is past the end of the sequence ({len(seq)} aa)"
                )
            actual = seq[pos - 1]
            rows.append(
                {
                    "term": term_id,
                    "side": side,
                    "accession": acc,
                    "position": pos,
                    "claimed": spec["residue"],
                    "actual": actual,
                    "ok": actual == spec["residue"],
                }
            )
    return rows


# --- driver ---------------------------------------------------------------------


def load_review(path: Path = REVIEW) -> dict[str, Any]:
    return yaml.load(path.read_text(), Loader=StrictLoader)


def goa_rows(path: Path = GOA) -> list[dict[str, str]]:
    with path.open() as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def run(review_text: str | None = None, seq_override: dict[str, str] | None = None) -> dict[str, Any]:
    text = review_text if review_text is not None else REVIEW.read_text()
    review = yaml.load(text, Loader=StrictLoader)
    rows = goa_rows()

    errors: list[str] = []

    offenders = folded_block_hyphen_breaks(text)
    if offenders:
        errors.append(
            "folded block line(s) ending in a hyphen, which fold to 'word- next': "
            + "; ".join(f"line {n}: {t[-40:]!r}" for n, t in offenders)
        )

    anns = review.get("existing_annotations", [])
    actions = Counter((a.get("review") or {}).get("action") for a in anns)

    goa_terms = Counter(r["GO TERM"] for r in rows)
    reviewed_terms = Counter(a["term"]["id"] for a in anns if (a.get("review") or {}).get("action") != "NEW")
    missing = sorted(set(goa_terms) - set(reviewed_terms))
    extra = sorted(set(reviewed_terms) - set(goa_terms))
    if missing:
        errors.append(f"GOA terms with no non-NEW review row: {missing}")
    if extra:
        errors.append(f"non-NEW review rows with no GOA row: {extra}")

    for ann in anns:
        rev = ann.get("review") or {}
        action = rev.get("action")
        ev = ann.get("evidence_type")
        term = ann["term"]["id"]
        if action in DEMOTING_ACTIONS and ev in PROPAGATED_EVIDENCE and "propagation_review" not in rev:
            errors.append(f"{term}: {action} on propagated evidence {ev} without a propagation_review")
        if action in DEMOTING_ACTIONS and ev in EXPERIMENTAL_EVIDENCE:
            errors.append(f"{term}: {action} on EXPERIMENTAL evidence {ev}; experimental rows are not demoted here")
        if action == "MODIFY" and not rev.get("proposed_replacement_terms"):
            errors.append(f"{term}: MODIFY without proposed_replacement_terms")

    residues = check_residue_claims(review, seq_override=seq_override)
    for r in residues:
        if not r["ok"]:
            errors.append(
                f"{r['term']}: residue claim {r['side']} {r['accession']}:{r['position']} "
                f"says {r['claimed']} but the sequence holds {r['actual']}"
            )
    if not residues:
        errors.append("no residue claims found; this review's central argument is a residue claim")

    return {
        "n_goa_rows": len(rows),
        "n_annotations": len(anns),
        "actions": dict(actions),
        "residue_claims": residues,
        "folded_hyphen_offenders": offenders,
        "errors": errors,
    }


def self_test() -> int:
    failures: list[str] = []

    def check(label: str, cond: bool, detail: str = "") -> None:
        if cond:
            print(f"  ok    {label}")
        else:
            failures.append(label)
            print(f"  FAIL  {label}: {detail}")

    print("self-test")
    text = REVIEW.read_text()
    base = run(text)
    check("baseline: the review passes every check", not base["errors"], "; ".join(base["errors"]))
    check(
        "baseline: residue claims were actually found and resolved",
        len(base["residue_claims"]) >= 4,
        f"{len(base['residue_claims'])} sides resolved",
    )

    # Mutation 1: the folded-hyphen trap. Anchor on a folded body line and split a
    # hyphenated word across it, which is exactly how the damage happened.
    anchor = "      catalytic arginine finger is replaced by a threonine, the substitution is shared with the"
    if text.count(anchor) != 1:
        raise CheckError(f"self-test anchor matched {text.count(anchor)} times, expected exactly 1")
    broken = text.replace(anchor, "      catalytic arginine-\n      finger is replaced by a threonine, the substitution is shared with the")
    res = run(broken)
    check(
        "mutation: a hyphen at end of a folded line is caught",
        any("ending in a hyphen" in e for e in res["errors"]),
        "; ".join(res["errors"]) or "no error raised",
    )

    # Mutation 2: a residue claim that does not match the sequence.
    #
    # The anchor carries the whole anchor+target block of ONE claim, not just
    # "position: 258 / residue: T". The short form used to be unique and stopped being so
    # the moment a second claim was re-pointed to the same target -- and the
    # matched-exactly-once assertion below caught that immediately, with
    # "residue anchor matched 2 times, expected exactly 1", rather than silently mutating
    # whichever claim came first. Keep the block form.
    claim_anchor = (
        "          accession: UniProtKB:Q07960\n"
        "          position: 282\n"
        "          residue: R\n"
        "        target:\n"
        "          accession: UniProtKB:Q6ZRI8\n"
        "          position: 258\n"
        "          residue: T"
    )
    if text.count(claim_anchor) != 1:
        raise CheckError(f"residue anchor matched {text.count(claim_anchor)} times, expected exactly 1")
    wrong = text.replace(claim_anchor, claim_anchor[: -len("residue: T")] + "residue: R")
    res = run(wrong)
    check(
        "mutation: a residue claim contradicted by the sequence is caught",
        any("but the sequence holds" in e for e in res["errors"]),
        "; ".join(res["errors"]) or "no error raised",
    )

    # Mutation 3: a demotion on propagated evidence with its propagation_review removed.
    prop_anchor = "    propagation_review:\n      root_cause: PROPAGATION_BAD\n      failure_modes:\n      - COMPARTMENT_OR_COMPLEX_MISMATCH"
    if text.count(prop_anchor) != 1:
        raise CheckError(f"propagation anchor matched {text.count(prop_anchor)} times, expected exactly 1")
    stripped = text.replace(prop_anchor, "    propagation_review_REMOVED:\n      root_cause: PROPAGATION_BAD\n      failure_modes:\n      - COMPARTMENT_OR_COMPLEX_MISMATCH")
    res = run(stripped)
    check(
        "mutation: a demotion without a propagation_review is caught",
        any("without a propagation_review" in e for e in res["errors"]),
        "; ".join(res["errors"]) or "no error raised",
    )

    # Mutation 4: duplicate YAML key.
    dup = text.replace("id: Q6ZRI8\ngene_symbol: ARHGAP36", "id: Q6ZRI8\nid: Q6ZRI8\ngene_symbol: ARHGAP36", 1)
    try:
        run(dup)
    except CheckError as exc:
        check("mutation: a duplicate top-level key is refused", "duplicate YAML key" in str(exc), str(exc))
    else:
        check("mutation: a duplicate top-level key is refused", False, "no error raised")

    # Mutation 5: drop a GOA row from the review.
    drop_anchor = "- term:\n    id: GO:0007165\n    label: signal transduction\n  evidence_type: IEA"
    if text.count(drop_anchor) != 1:
        raise CheckError(f"drop anchor matched {text.count(drop_anchor)} times, expected exactly 1")
    renamed = text.replace(drop_anchor, "- term:\n    id: GO:9999999\n    label: signal transduction\n  evidence_type: IEA")
    res = run(renamed)
    check(
        "mutation: a GOA row missing from the review is caught",
        any("no non-NEW review row" in e for e in res["errors"]),
        "; ".join(res["errors"]) or "no error raised",
    )

    # Negative controls: edits that must change nothing.
    quiet = text.replace("status: COMPLETE", "status: COMPLETE  # a comment", 1)
    res = run(quiet)
    check("negative control: adding a comment raises nothing", not res["errors"], "; ".join(res["errors"]))
    quiet2 = text.replace("  - MGI:MGI:1196332\n", "  - MGI:MGI:1196332\n", 1)
    res = run(quiet2)
    check("negative control: an identity substitution raises nothing", not res["errors"], "; ".join(res["errors"]))
    # A hyphen at the end of a line OUTSIDE any folded block must stay silent: the guard
    # is about folding, not about hyphens.
    outside = text.replace("suggested_questions:", "# a trailing hyphen outside a block -\nsuggested_questions:", 1)
    res = run(outside)
    check(
        "negative control: a trailing hyphen outside a folded block raises nothing",
        not any("ending in a hyphen" in e for e in res["errors"]),
        "; ".join(res["errors"]),
    )

    print("PASS" if not failures else f"{len(failures)} FAILURE(S)")
    return 0 if not failures else 1


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args(argv)
    if args.self_test:
        return self_test()
    res = run()
    print(f"GOA rows:             {res['n_goa_rows']}")
    print(f"review annotations:   {res['n_annotations']}")
    print("actions:")
    for action, n in sorted(res["actions"].items()):
        print(f"  {action:24s} {n}")
    print("residue claims resolved against UniProt:")
    for r in res["residue_claims"]:
        mark = "ok " if r["ok"] else "BAD"
        print(f"  {mark} {r['side']:6s} {r['accession']}:{r['position']} claimed {r['claimed']} actual {r['actual']}")
    if res["errors"]:
        print(f"\n{len(res['errors'])} ERROR(S):")
        for e in res["errors"]:
            print(f"  - {e}")
        return 1
    print("\nOK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
