#!/usr/bin/env python3
"""Build the IBA row's `source_entities` FROM the GOA WITH/FROM field and inject it
into the review YAML at a marked anchor.

Hand-maintained source lists have drifted on every gene in this campaign that tried
them, so this is generated with an assertion in both directions:

  * the anchor MUST be present before the mutation (a mutation that silently no-ops
    "proves" nothing);
  * the number of entities written MUST equal the number of GOA tokens, and the
    number parsed back out MUST equal it too (detector and mutator agree on scope).

Run from the repo root:
    uv run python genes/human/ADAMTSL5/ADAMTSL5-bioinformatics/inject_source_entities.py
"""

import csv
import json
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[3].parent
GENE_DIR = Path(__file__).resolve().parent.parent
GOA = GENE_DIR / "ADAMTSL5-goa.tsv"
RESOLUTION = Path(__file__).resolve().parent / "withfrom_resolution.json"
STAGING = GENE_DIR / "_staging_review.yaml"
TARGET = GENE_DIR / "ADAMTSL5-ai-review.yaml"
ANCHOR = "      # __INJECT_SOURCE_ENTITIES__ generated from the GOA WITH/FROM field"


class DuplicateKeyLoader(yaml.SafeLoader):
    """PyYAML keeps the LAST of a duplicated mapping key and discards the earlier one
    silently, deleting data before any quote gate can see it. Refuse to load such a
    document at all."""


def _no_duplicates(loader, node, deep=False):
    mapping = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in mapping:
            raise yaml.constructor.ConstructorError(
                None, None, f"duplicate key {key!r} in mapping", key_node.start_mark)
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


DuplicateKeyLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _no_duplicates)


def build_block(tokens, records):
    lines = ["      source_entities:"]
    for tok in tokens:
        r = records[tok]
        head = r["candidates"][0]
        if tok.startswith("PANTHER:"):
            status = "SUPPORTS_TRANSFER"
            label = "PANTHER tree node (ADAMTS/ADAMTS-like family)"
            comment = ("Internal PANTHER tree node, not a protein. The node carries four "
                       "IBD terms but only GO:0031012 reached ADAMTSL5.")
        elif tok == "UniProtKB:Q6ZMM2":
            status = "CIRCULAR_OR_REDUNDANT"
            label = "ADAMTSL5 (H. sapiens) - the target itself"
            comment = ("Self-referential seed. Valid: it records a PAINT curator judging "
                       "this function core for the gene. ADAMTSL5 independently holds its "
                       "own IDA to GO:0031012 from PMID:23010571.")
        else:
            status = "SUPPORTS_TRANSFER"
            org = head["organism"].split()
            label = f"{head['gene']} ({org[0][0]}. {org[1]})"
            terms = ", ".join(t[0] for t in r["own_experimental_terms"]) or "none"
            comment = (f"{head['reviewed']} {head['accession']}; carries its own "
                       f"{'/'.join(r['own_experimental_codes'])} to {terms}.")
        lines += [
            f"      - source_id: {tok}",
            f"        source_label: {label}",
            f"        source_status: {status}",
            "        comment: >-",
            f"          {comment}",
        ]
    return "\n".join(lines)


def main():
    for p in (GOA, RESOLUTION, STAGING):
        if not p.exists():
            raise SystemExit(
                f"FATAL: missing required input {p}. "
                f"Run `just fetch-gene human ADAMTSL5` and resolve_withfrom.py first.")

    rows = list(csv.DictReader(GOA.open(), delimiter="\t"))
    iba = [r for r in rows if r["GO EVIDENCE CODE"] == "IBA"]
    if len(iba) != 1:
        raise SystemExit(f"FATAL: expected exactly 1 IBA row in GOA, found {len(iba)}")
    tokens = iba[0]["WITH/FROM"].split("|")

    records = {r["token"]: r for r in json.loads(RESOLUTION.read_text())["records"]}
    if set(records) != set(tokens):
        raise SystemExit("FATAL: withfrom_resolution.json does not cover the GOA tokens "
                         f"exactly. Only in GOA: {sorted(set(tokens)-set(records))}; "
                         f"only in JSON: {sorted(set(records)-set(tokens))}")

    text = STAGING.read_text()
    # Assert the target is present BEFORE mutating: a no-op mutation proves nothing.
    if text.count(ANCHOR) != 1:
        raise SystemExit(f"FATAL: expected exactly 1 anchor in {STAGING}, "
                         f"found {text.count(ANCHOR)}")

    out = text.replace(ANCHOR, build_block(tokens, records))
    TARGET.write_text(out)

    # Detector and mutator must agree on scope, or the verification is blind.
    doc = yaml.load(TARGET.read_text(), Loader=DuplicateKeyLoader)
    iba_ann = [a for a in doc["existing_annotations"] if a["evidence_type"] == "IBA"]
    assert len(iba_ann) == 1, f"parsed {len(iba_ann)} IBA annotations, expected 1"
    parsed = iba_ann[0]["review"]["propagation_review"]["source_entities"]
    assert len(parsed) == len(tokens), (
        f"wrote/parsed {len(parsed)} source_entities for {len(tokens)} GOA tokens")
    assert [e["source_id"] for e in parsed] == tokens, \
        "source_entities order/content does not match the GOA WITH/FROM field"

    # Raw-vs-parsed reconciliation: a duplicate key would silently drop entries.
    #
    # SCOPE MATTERS. The first version of this check counted `- source_id:` across the
    # WHOLE document and asserted it equalled the IBA token count. It fired with
    # raw=18 / parsed=17 -- not a data bug, but a bug in the guard: the GO:0030198 row
    # has its own propagation_review carrying InterPro:IPR013273 at the same
    # indentation. A detector whose scope differs from the mutator's is structurally
    # blind, so the two counts are now reconciled separately and the document-wide
    # expectation is DERIVED, never hand-set.
    block_raw = build_block(tokens, records).count("      - source_id: ")
    assert block_raw == len(parsed) == len(tokens), (
        f"injected block raw={block_raw} parsed={len(parsed)} tokens={len(tokens)} "
        "-- investigate, do not rationalise")

    doc_expected = sum(
        len(a["review"]["propagation_review"]["source_entities"])
        for a in doc["existing_annotations"]
        if a.get("review", {}).get("propagation_review", {}).get("source_entities"))
    doc_raw = out.count("      - source_id: ")
    assert doc_raw == doc_expected, (
        f"document-wide raw={doc_raw} but parsed propagation_review entities="
        f"{doc_expected} -- a duplicate YAML key may have silently dropped provenance")
    raw = block_raw

    STAGING.unlink()
    print(f"OK: injected {len(parsed)} source_entities == {len(tokens)} GOA WITH/FROM "
          f"tokens (raw count {raw}); wrote {TARGET}; removed staging file")


if __name__ == "__main__":
    main()
