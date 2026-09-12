"""Populate (or verify) ``propagation_review.source_entities`` from the GOA TSV.

Hand-maintained source lists have drifted on every gene in this campaign that
tried them, and the drift was only ever caught by scripting a diff against the
GOA WITH/FROM field. So this script is the only thing that writes those lists.

Two modes:
  (default)  rewrite the review YAML through the YAML parser, replacing every
             ``source_entities`` list with one built from the GOA field
  --check    verify the committed lists still match the GOA, exit non-zero if not

The invariant, asserted in both modes: for every annotation carrying a
``propagation_review``, the number of ``source_entities`` equals the number of
``|``-separated tokens in that GOA row's WITH/FROM column, and the token sets are
equal. A detector and a mutator that disagree on scope make verification blind,
so both modes compute the expected lists with the same function.
"""
import argparse
import csv
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
GENE_DIR = HERE.parent
GOA = GENE_DIR / "ACTA1-goa.tsv"
REVIEW = GENE_DIR / "ACTA1-ai-review.yaml"
RESOLUTION = HERE / "withfrom_resolution.json"

from ruamel.yaml import YAML  # noqa: E402  (kept after the stdlib block)

# Round-trip mode, NOT safe_load/dump. A plain dump reflows every prose scalar and
# silently deletes the section comments that mark which GOA rows each block covers -
# a mutation far larger than the one intended. Round-trip preserves both while still
# editing through the parser rather than by string surgery.
_yaml = YAML()
_yaml.preserve_quotes = True
_yaml.width = 100
_yaml.indent(mapping=2, sequence=2, offset=0)


def goa_withfrom() -> dict[tuple[str, str, str], list[list[str]]]:
    """Map (term, evidence, reference) -> every WITH/FROM token list under that key.

    The three-part key is NOT unique in general: the seven ACTA1 interaction rows
    from PMID:32814053 share it and differ only in their single partner token. So
    the value is a list of token lists, and uniqueness is required only where a
    caller actually needs one answer.
    """
    if not GOA.exists():
        raise SystemExit(f"missing input {GOA}; run: just fetch-gene human ACTA1")
    out: dict[tuple[str, str, str], list[list[str]]] = {}
    with GOA.open() as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            wf = (row["WITH/FROM"] or "").strip()
            if not wf:
                continue
            key = (row["GO TERM"], row["GO EVIDENCE CODE"], row["REFERENCE"])
            out.setdefault(key, []).append(wf.split("|"))
    return out


def sole(key: tuple[str, str, str], lists: list[list[str]]) -> list[str]:
    """The one token list under a key, refusing to guess when there are several."""
    distinct = {tuple(t) for t in lists}
    if len(distinct) != 1:
        raise RuntimeError(
            f"key {key} maps to {len(distinct)} distinct WITH/FROM fields in the GOA; "
            "cannot choose one for source_entities without corrupting a row"
        )
    return lists[0]


def labels_from_resolution() -> dict[str, str]:
    """Human-readable labels for source tokens, from the resolver's output.

    Labels are cosmetic, so a missing resolution file degrades to bare tokens -
    but it must say so rather than pretend the labels were never wanted.
    """
    if not RESOLUTION.exists():
        print(f"NOTE: {RESOLUTION.name} absent; source_label will be omitted. "
              "Run resolve_withfrom.py first for labelled output.", file=sys.stderr)
        return {}
    data = json.loads(RESOLUTION.read_text())
    labels: dict[str, str] = {}
    for row in data["rows"]:
        for src in row["sources"]:
            if src["kind"] != "protein":
                continue
            cands = src.get("candidates") or []
            if not cands:
                continue
            c = cands[0]
            genes = ",".join(g for g in c["genes"] if g) or c["entry_name"]
            status = "Swiss-Prot" if c["reviewed"] else "TrEMBL"
            labels[src["token"]] = f"{genes} ({c['organism']}, {status})"
    return labels


SELF = "UniProtKB:P68133"


def build(tokens: list[str], labels: dict[str, str], root_cause: str) -> list[dict]:
    entries = []
    for tok in tokens:
        entry: dict[str, str] = {"source_id": tok}
        if tok in labels:
            entry["source_label"] = labels[tok]
        elif tok.startswith("PANTHER:"):
            entry["source_label"] = "PANTHER tree node (not a gene product)"
        elif tok.startswith("UniProtKB-"):
            entry["source_label"] = "UniProt controlled-vocabulary term (not a gene product)"
        elif tok.startswith("ensembl:"):
            entry["source_label"] = "Ensembl protein identifier"

        if tok == SELF:
            entry["source_status"] = "SUPPORTS_TRANSFER"
            entry["comment"] = "ACTA1 itself: this is a self-referential PAN-GO seed, not a transfer"
        elif root_cause == "PROPAGATION_BAD":
            entry["source_status"] = "SUPPORTS_SOURCE_BUT_NOT_TARGET"
        elif tok.startswith(("PANTHER:", "UniProtKB-", "ensembl:")):
            entry["source_status"] = "NOT_RELEVANT"
            entry.setdefault("comment", "not a gene product; no evidence of its own to query")
        else:
            entry["source_status"] = "SUPPORTS_TRANSFER"
        entries.append(entry)
    return entries


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--check", action="store_true",
                    help="verify instead of rewriting; exit 1 on any mismatch")
    args = ap.parse_args()

    wf = goa_withfrom()
    labels = labels_from_resolution()
    with REVIEW.open() as fh:
        doc = _yaml.load(fh)

    detected = 0   # annotations carrying a propagation_review
    changed = 0    # annotations whose source_entities this run wrote or verified
    problems: list[str] = []

    for ann in doc["existing_annotations"]:
        review = ann.get("review") or {}
        pr = review.get("propagation_review")
        if pr is None:
            continue
        detected += 1
        key = (ann["term"]["id"], ann["evidence_type"], ann["original_reference_id"])
        if key not in wf:
            problems.append(f"{key}: has a propagation_review but no WITH/FROM row in the GOA")
            continue
        expected = build(sole(key, wf[key]), labels, pr.get("root_cause", ""))
        if args.check:
            actual = pr.get("source_entities") or []
            got = [e.get("source_id") for e in actual]
            want = [e["source_id"] for e in expected]
            if got != want:
                problems.append(
                    f"{key}: source_entities drifted - {len(got)} present, "
                    f"{len(want)} in GOA; missing={sorted(set(want) - set(got))}, "
                    f"extra={sorted(set(got) - set(want))}"
                )
                continue
        else:
            pr["source_entities"] = expected
        changed += 1

    # A detector and a mutator that disagree on scope make the re-check blind, so
    # require them to agree and fail loudly on any gap rather than reporting success.
    if problems:
        for p in problems:
            print(f"FAIL {p}", file=sys.stderr)
        raise SystemExit(
            f"{len(problems)} problem(s); detected={detected} handled={changed}"
        )
    if detected != changed:
        raise SystemExit(
            f"detected {detected} propagation_review blocks but handled {changed}; "
            "these must be equal or the verification cannot see what it missed"
        )

    check_supporting_entities(doc, wf)

    if args.check:
        print(f"OK: {changed}/{detected} propagation_review blocks match the GOA WITH/FROM field")
        return

    before = REVIEW.read_text()
    with REVIEW.open("w") as fh:
        _yaml.dump(doc, fh)
    after = REVIEW.read_text()
    # Guard against the round-trip itself becoming the edit: the only lines that may
    # change are ones this script is responsible for. Comment lines are a cheap,
    # sensitive canary because a non-round-trip dumper deletes all of them.
    n_before = sum(1 for ln in before.splitlines() if ln.lstrip().startswith("#"))
    n_after = sum(1 for ln in after.splitlines() if ln.lstrip().startswith("#"))
    if n_after < n_before:
        raise SystemExit(
            f"the dump dropped {n_before - n_after} comment line(s); refusing to treat "
            "a formatting loss as a successful edit"
        )
    print(f"wrote {REVIEW}: populated {changed} source_entities lists from {GOA.name} "
          f"({n_after} comment lines preserved)")


def check_supporting_entities(doc: dict, wf: dict[tuple[str, str, str], list[list[str]]]) -> None:
    """Verify hand-written ``supporting_entities`` against the GOA, always.

    This is the check the ACTR5 lesson calls for. The ``fetch-gene`` stub collapsed
    the seven PMID:32814053 interaction rows into one; they were restored by hand so
    each partner gets its own verdict, and a hand-restored list is exactly the kind
    that drifts. Because those seven rows share a (term, evidence, reference) key,
    the test is a multiset comparison: the partner lists written in the review must
    be a permutation of the WITH/FROM fields the GOA has under that key - no
    duplicates, no omissions, no invented partners.
    """
    written: dict[tuple[str, str, str], list[tuple[str, ...]]] = {}
    for ann in doc["existing_annotations"]:
        ents = ann.get("supporting_entities")
        if not ents:
            continue
        key = (ann["term"]["id"], ann["evidence_type"], ann["original_reference_id"])
        written.setdefault(key, []).append(tuple(ents))

    problems: list[str] = []
    for key, lists in written.items():
        if key not in wf:
            problems.append(f"{key}: supporting_entities present but no WITH/FROM row in the GOA")
            continue
        want = sorted(tuple(t) for t in wf[key])
        got = sorted(lists)
        if got != want:
            problems.append(
                f"{key}: supporting_entities do not match the GOA - "
                f"{len(got)} row(s) written against {len(want)} GOA row(s); "
                f"missing={sorted(set(want) - set(got))} extra={sorted(set(got) - set(want))}"
            )

    # The converse direction: a GOA row whose WITH/FROM names gene products, on an
    # interaction term, but which no review row claims, means a row was dropped.
    for key, lists in wf.items():
        if key[0] != "GO:0005515":
            continue
        if key not in written:
            problems.append(
                f"{key}: {len(lists)} GOA interaction row(s) carry a partner but no "
                "review row records supporting_entities for them"
            )
        elif len(written[key]) != len(lists):
            problems.append(
                f"{key}: {len(written[key])} review row(s) against {len(lists)} GOA row(s) - "
                "a collapsed or duplicated interaction row"
            )

    if problems:
        for p in problems:
            print(f"FAIL {p}", file=sys.stderr)
        raise SystemExit(f"{len(problems)} supporting_entities problem(s)")
    n = sum(len(v) for v in written.values())
    print(f"OK: {n} supporting_entities row(s) match the GOA WITH/FROM field one-to-one")


if __name__ == "__main__":
    main()
