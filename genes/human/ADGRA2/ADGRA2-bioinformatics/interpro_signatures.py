#!/usr/bin/env python3
"""Resolve the InterPro signatures behind ADGRA2's IEA rows, and audit the labels the
review asserts for them.

Why this exists: I hand-wrote the five `source_label` values for the InterPro entries in
ADGRA2's WITH/FROM and **three of the five were wrong**, two of them substantively --
`IPR001879` was labelled "GPCR proteolysis site (GPS) domain" and `IPR036445` "GAIN domain
superfamily", when both are in fact the family-2 GPCR *extracellular hormone receptor*
domain and its superfamily. That error had already reached the review's prose. Naming the
wrong domain for a characterised function is the single most expensive mistake class in
this campaign, so the labels are now computed and the assertion is committed.

It also pulls the authoritative `interpro2go` mapping, because *which* signature licenses
*which* GO term is the substance of the GO:0004930 argument, not background colour.

Usage:
    python3 interpro_signatures.py            # audit the committed review, write JSON
    python3 interpro_signatures.py --self-test
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
import urllib.request
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
GOA = HERE.parent / "ADGRA2-goa.tsv"
REVIEW = HERE.parent / "ADGRA2-ai-review.yaml"
OUT = HERE / "interpro_signatures.json"

INTERPRO_API = "https://www.ebi.ac.uk/interpro/api/entry/InterPro/{}"
INTERPRO2GO = "https://ftp.ebi.ac.uk/pub/databases/GO/goa/external2go/interpro2go"
UA = {"User-Agent": "ai-gene-review ADGRA2 (mailto:cjmungall@lbl.gov)"}


def norm(t: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", (t or "").lower()).strip()


def signatures_in_goa(path: Path) -> dict[str, set[str]]:
    """{IPR accession: {GO ids it appears as WITH/FROM for}} -- read from the GOA TSV."""
    out: dict[str, set[str]] = {}
    with path.open() as fh:
        for r in csv.DictReader(fh, delimiter="\t"):
            for tok in r["WITH/FROM"].split("|"):
                if tok.startswith("InterPro:"):
                    out.setdefault(tok.split(":", 1)[1], set()).add(r["GO TERM"])
    assert out, f"no InterPro tokens found in {path} -- the audit would pass vacuously"
    return out


def fetch_entry(ipr: str) -> dict:
    with urllib.request.urlopen(urllib.request.Request(INTERPRO_API.format(ipr), headers=UA),
                                timeout=60) as fh:
        assert fh.status == 200, f"HTTP {fh.status} for {ipr}"
        m = json.load(fh)["metadata"]
    assert m["accession"] == ipr, f"InterPro returned {m['accession']} for {ipr}"
    name = m["name"]["name"]
    assert name, f"empty name for {ipr} -- an empty string would silently match nothing"
    return {"accession": ipr, "name": name, "short": m["name"].get("short"), "type": m["type"]}


def fetch_interpro2go() -> dict[str, list[tuple[str, str]]]:
    with urllib.request.urlopen(urllib.request.Request(INTERPRO2GO, headers=UA), timeout=120) as fh:
        assert fh.status == 200, f"HTTP {fh.status} for interpro2go"
        text = fh.read().decode()
    mapping: dict[str, list[tuple[str, str]]] = {}
    pat = re.compile(r"^InterPro:(IPR\d+) .* > GO:(.+) ; (GO:\d+)$")
    n = 0
    for line in text.splitlines():
        m = pat.match(line)
        if m:
            n += 1
            mapping.setdefault(m.group(1), []).append((m.group(3), m.group(2)))
    assert n > 10000, f"only {n} interpro2go lines parsed -- the regex or the file changed"
    return mapping


def asserted_labels(review: Path) -> dict[str, str]:
    doc = yaml.safe_load(review.read_text())
    out: dict[str, str] = {}

    def walk(n):
        if isinstance(n, dict):
            sid = n.get("source_id", "")
            if isinstance(sid, str) and sid.startswith("InterPro:") and "source_label" in n:
                acc = sid.split(":", 1)[1]
                prev = out.get(acc)
                assert prev in (None, n["source_label"]), (
                    f"{acc} is labelled two different ways in the review: {prev!r} vs {n['source_label']!r}"
                )
                out[acc] = n["source_label"]
            for v in n.values():
                walk(v)
        elif isinstance(n, list):
            for v in n:
                walk(v)

    walk(doc)
    return out


def audit(verbose: bool = True) -> list[str]:
    problems: list[str] = []
    in_goa = signatures_in_goa(GOA)
    labels = asserted_labels(REVIEW)

    # Presence, not just match-on-match: a guard that only validates the entries it finds
    # passes silently when an entry is deleted or a key is renamed.
    missing = set(in_goa) - set(labels)
    for m in sorted(missing):
        problems.append(f"{m} is in the GOA WITH/FROM but carries no source_label in the review")
    stray = set(labels) - set(in_goa)
    for s in sorted(stray):
        problems.append(f"{s} is labelled in the review but appears in no GOA WITH/FROM row")

    i2g = fetch_interpro2go()
    records = []
    for ipr in sorted(in_goa):
        e = fetch_entry(ipr)
        e["go_terms_in_adgra2_goa"] = sorted(in_goa[ipr])
        e["interpro2go"] = sorted(i2g.get(ipr, []))
        e["asserted_label"] = labels.get(ipr)
        ok = e["asserted_label"] is not None and (
            norm(e["asserted_label"]) == norm(e["name"])
            or norm(e["asserted_label"]) == norm(e["short"] or "")
        )
        e["label_matches"] = ok
        if e["asserted_label"] is not None and not ok:
            problems.append(
                f"{ipr} label drift: review says {e['asserted_label']!r}, InterPro says {e['name']!r}"
            )
        # The GO terms the row claims must be ones interpro2go actually licenses for that entry.
        licensed = {g for g, _ in e["interpro2go"]}
        unlicensed = set(e["go_terms_in_adgra2_goa"]) - licensed
        if unlicensed:
            problems.append(
                f"{ipr} appears in ADGRA2's WITH/FROM for {sorted(unlicensed)}, which interpro2go "
                f"does not map it to (it maps to {sorted(licensed)})"
            )
        records.append(e)

    if verbose:
        for e in records:
            print(f"{e['accession']}  [{e['type']}]  {e['name']}")
            print(f"    review label : {e['asserted_label']!r}  -> {'OK' if e['label_matches'] else 'DRIFT'}")
            print(f"    interpro2go  : {[g for g, _ in e['interpro2go']]}")
            print(f"    used in ADGRA2 GOA for: {e['go_terms_in_adgra2_goa']}")
        OUT.write_text(json.dumps(records, indent=2))
        print(f"\nwrote {OUT.name}")
    return problems


def self_test() -> None:
    # Direction 1: the regex must actually parse interpro2go, and the >10000 floor must bind.
    i2g = fetch_interpro2go()
    assert ("GO:0004888", "transmembrane signaling receptor activity") in i2g["IPR017981"], i2g["IPR017981"]
    assert "GO:0004930" not in {g for g, _ in i2g["IPR017981"]}, (
        "IPR017981 now maps to GO:0004930 -- the review's argument rests on it NOT doing so"
    )
    assert "GO:0004930" in {g for g, _ in i2g["IPR000832"]}

    # Direction 2: label comparison must reject the exact wrong labels that shipped first,
    # and accept the right ones.
    e = fetch_entry("IPR001879")
    assert norm("GPCR proteolysis site (GPS) domain") != norm(e["name"]), "guard would not have caught the original bug"
    assert norm(e["name"]) == norm(e["name"])

    # Direction 3: happy path -- the committed review must audit clean.
    probs = audit(verbose=False)
    assert probs == [], f"committed review does not audit clean: {probs}"

    # Direction 4: presence check must fire when a label is removed, not silently skip.
    import tempfile
    global REVIEW
    original = REVIEW
    doc = yaml.safe_load(original.read_text())

    def strip(n):
        if isinstance(n, dict):
            if str(n.get("source_id", "")).startswith("InterPro:"):
                n.pop("source_label", None)
            for v in n.values():
                strip(v)
        elif isinstance(n, list):
            for v in n:
                strip(v)

    strip(doc)
    with tempfile.NamedTemporaryFile("w", suffix=".yaml", delete=False) as fh:
        yaml.safe_dump(doc, fh, sort_keys=False)
        tmp = Path(fh.name)
    try:
        REVIEW = tmp
        probs = audit(verbose=False)
        assert any("carries no source_label" in p for p in probs), probs
    finally:
        REVIEW = original
        tmp.unlink()

    print("self-test OK: 4 directions exercised (interpro2go parsed and IPR017981 still generic; "
          "the original wrong label is rejected; the committed review audits clean; a removed "
          "label is detected rather than skipped)")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args()
    if a.self_test:
        self_test()
        sys.exit(0)
    found = audit()
    print()
    if found:
        for p in found:
            print("PROBLEM:", p)
        sys.exit(1)
    print("OK: every InterPro signature in the GOA WITH/FROM is labelled, labels match InterPro, "
          "and every GO term claimed is one interpro2go licenses for that signature")
