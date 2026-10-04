#!/usr/bin/env python3
"""Normalize top-level ``taxon.label`` values to their NCBITaxon labels.

The ``taxon`` slot of ``GeneReview`` and ``PredictionReview`` is bound to the
``NCBITaxonEnum`` dynamic enum, so ``linkml-term-validator --labels`` requires
the label to equal the NCBITaxon label verbatim. Many older reviews carry
UniProt ``OS``-line strain wording (e.g. ``Saccharomyces cerevisiae`` for
``NCBITaxon:559292``, whose label is ``Saccharomyces cerevisiae S288C``).

This script finds every YAML file with a top-level ``taxon:`` block, looks the
id up in NCBITaxon (through OAK, default ``ols:ncbitaxon``), and rewrites only
the ``label`` value of that block, leaving the rest of the file byte-for-byte
unchanged. Ids that do not resolve are reported and never rewritten.

With ``--from-gene-review``, a file whose taxon id is not an NCBITaxon CURIE
(BioReason prediction files used ``uniprot:<CODE>``) gets the id and label of
the sibling ``<GENE>-ai-review.yaml`` instead, when that review has one.

Dry run by default; pass ``--apply`` to write.

Examples::

    uv run python scripts/normalize_taxon_labels.py
    uv run python scripts/normalize_taxon_labels.py --apply genes
    uv run python scripts/normalize_taxon_labels.py --apply --from-gene-review genes
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

# Top-level taxon block: "taxon:" then an indented id line and a label that is
# either a one-line scalar or a folded/literal block scalar with continuation
# lines indented deeper than the key.
BLOCK_RE = re.compile(
    r"^taxon:\n"
    r"(?P<body>(?:[ \t]+.*\n?)+)",
    re.MULTILINE,
)
ID_RE = re.compile(r"^(?P<indent>[ \t]+)id:[ \t]*['\"]?(?P<id>[^'\"\s#]+)['\"]?[ \t]*$", re.MULTILINE)
LABEL_RE = re.compile(
    r"^(?P<indent>[ \t]+)label:[ \t]*(?P<value>.*)\n?"
    r"(?P<cont>(?:(?P=indent)[ \t]+.*\n?)*)",
    re.MULTILINE,
)


# Flow-style mapping on one line: ``taxon: {id: "NCBITaxon:1", label: Foo}``.
FLOW_RE = re.compile(
    r"^taxon:[ \t]*\{[ \t]*id:[ \t]*(?P<q>['\"]?)(?P<id>[^'\",}\s]+)(?P=q)[ \t]*,"
    r"[ \t]*label:[ \t]*(?P<label>.*?)[ \t]*\}[ \t]*$",
    re.MULTILINE,
)


def find_flow_taxon(text: str) -> re.Match | None:
    """Locate a one-line flow-style top-level taxon mapping."""
    return FLOW_RE.search(text)


def yaml_scalar(text: str) -> str:
    """Return a safe single-line YAML plain or quoted scalar for ``text``."""
    if re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9 .,/()'_+=-]*[A-Za-z0-9.)']", text) and ": " not in text and " #" not in text:
        return text
    return json.dumps(text, ensure_ascii=False)


def find_taxon_block(text: str) -> tuple[int, int, str, re.Match, re.Match] | None:
    """Locate the top-level taxon block; return (start, end, curie, id_match, label_match)."""
    m = BLOCK_RE.search(text)
    if not m:
        return None
    body = m.group("body")
    id_m = ID_RE.search(body)
    label_m = LABEL_RE.search(body)
    if not id_m or not label_m:
        return None
    return m.start("body"), m.end("body"), id_m.group("id"), id_m, label_m


def current_label(label_m: re.Match) -> str:
    """Best-effort current label text (joins folded continuation lines)."""
    value = label_m.group("value").strip()
    cont = label_m.group("cont")
    if value in {">-", ">", "|", "|-"} or (cont and value):
        parts = [value] if value not in {">-", ">", "|", "|-"} else []
        parts += [ln.strip() for ln in cont.splitlines() if ln.strip()]
        return " ".join(parts).strip("'\"")
    return value.strip("'\"")


def sibling_review_taxon(path: Path) -> dict[str, str] | None:
    """Return the NCBITaxon taxon of the gene review next to ``path``, if any."""
    from ai_gene_review.taxon import review_taxon

    review = path.parent / f"{path.parent.name}-ai-review.yaml"
    if review == path or not review.exists():
        return None
    try:
        return review_taxon(review)
    except ValueError:
        return None


def replace_taxon(path: Path, curie: str, label: str) -> None:
    """Rewrite the id and label of the top-level taxon (block or flow style) of ``path``."""
    text = path.read_text()
    hit = find_taxon_block(text)
    if hit is None:
        flow = find_flow_taxon(text)
        if flow is None:
            raise ValueError(f"No top-level taxon in {path}")
        q = flow.group("q") or '"'
        line = f"taxon: {{id: {q}{curie}{q}, label: {json.dumps(label, ensure_ascii=False)}}}"
        path.write_text(text[: flow.start()] + line + text[flow.end():])
        return
    start, end, _, id_m, label_m = hit
    body = text[start:end]
    edits = sorted(
        [
            (id_m.start(), id_m.end(), f"{id_m.group('indent')}id: {curie}"),
            (label_m.start(), label_m.end(), f"{label_m.group('indent')}label: {yaml_scalar(label)}\n"),
        ],
        reverse=True,
    )
    for a, b, repl in edits:
        body = body[:a] + repl + body[b:]
    path.write_text(text[:start] + body + text[end:])


def load_cache(path: Path) -> dict[str, str]:
    if path.exists():
        return json.loads(path.read_text())
    return {}


def resolve_labels(curies: set[str], adapter_spec: str, cache: dict[str, str]) -> dict[str, str | None]:
    """Resolve NCBITaxon CURIEs to labels via OAK, using and filling ``cache``."""
    todo = sorted(c for c in curies if c not in cache)
    if todo:
        from oaklib import get_adapter

        adapter = get_adapter(adapter_spec)
        for curie in todo:
            label: str | None = None
            if re.fullmatch(r"NCBITaxon:\d+", curie):
                try:
                    label = adapter.label(curie)
                except Exception as exc:  # network/OLS failure: leave unresolved
                    print(f"WARN: lookup failed for {curie}: {exc}", file=sys.stderr)
                    continue
            if label:  # never cache a miss, so a later run can retry it
                cache[curie] = label
    return {c: cache.get(c) for c in curies}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("roots", nargs="*", default=["genes", "projects", "tests/data"], help="Directories to scan")
    parser.add_argument("--apply", action="store_true", help="Write changes (default: dry run)")
    parser.add_argument("--adapter", default="ols:ncbitaxon", help="OAK adapter for NCBITaxon")
    parser.add_argument("--cache", default=".cache/ncbitaxon-labels.json", help="Label cache file")
    parser.add_argument(
        "--from-gene-review",
        action="store_true",
        help="Replace a non-NCBITaxon taxon id with the sibling gene review's taxon",
    )
    args = parser.parse_args()

    # tests/data/invalid holds deliberately wrong taxa (e.g. a CHLRE label); never "fix" them.
    files = sorted(
        p for root in args.roots for p in Path(root).rglob("*.yaml") if "tests/data/invalid" not in p.as_posix()
    )
    found: list[tuple[Path, str, str]] = []
    for path in files:
        text = path.read_text()
        hit = find_taxon_block(text)
        if hit:
            _, _, curie, _, label_m = hit
            found.append((path, curie, current_label(label_m)))
            continue
        flow = find_flow_taxon(text)
        if flow:
            found.append((path, flow.group("id"), flow.group("label").strip("'\"")))

    cache_path = Path(args.cache)
    cache = load_cache(cache_path)
    labels = resolve_labels({c for _, c, _ in found}, args.adapter, cache)
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    cache_path.write_text(json.dumps(cache, indent=1, sort_keys=True))

    changed = unresolved = replaced = 0
    for path, curie, old in found:
        if args.from_gene_review and not re.fullmatch(r"NCBITaxon:\d+", curie):
            sibling = sibling_review_taxon(path)
            if sibling:
                replaced += 1
                print(f"REPLACE\t{path}\t{curie} {old!r} -> {sibling['id']} {sibling['label']!r}")
                if args.apply:
                    replace_taxon(path, sibling["id"], sibling["label"])
                continue
        new = labels.get(curie)
        if new is None:
            unresolved += 1
            print(f"UNRESOLVED\t{path}\t{curie}\t{old}")
            continue
        if new == old:
            continue
        changed += 1
        print(f"RELABEL\t{path}\t{curie}\t{old!r} -> {new!r}")
        if args.apply:
            replace_taxon(path, curie, new)

    print(
        f"files with taxon: {len(found)}; to relabel: {changed}; replaced from gene review: {replaced}; "
        f"unresolved: {unresolved}"
        f"{'' if args.apply else ' (dry run)'}",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
