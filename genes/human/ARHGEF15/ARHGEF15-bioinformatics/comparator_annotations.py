"""Record the QuickGO annotation facts the review asserts about OTHER genes.

The review makes several claims about proteins that have no local GOA file in this
repository, so they cannot be checked offline from the committed corpus:

- the `GO:0046875` MODIFY is justified by a comparator check — NGEF/Ephexin1 already
  carries that term for the same relationship;
- each `propagation_review.source_entities` comment names the evidence code and reference
  behind an IBD seed's own annotation (ARHGEF5 IDA PMID:15601624, ARHGEF16 IDA
  PMID:20679435, NGEF EXP PMID:15848799, and the GO:0032956 seeds);
- the ISS donors are said to carry the transferred term experimentally (mouse Arhgef15
  GO:0005085 IDA PMID:21029865; rat Arhgef15 GO:0005737 and GO:0051496 IDA PMID:12775584).

Each is fetched here and written to `comparator_annotations.json`, so the claim is a
recorded query result rather than an assertion. Expectations are declared up front and the
script fails if one is not met: a fetcher that only reports what it finds cannot tell you
that what you wrote is wrong.

Usage:
    uv run --no-project python comparator_annotations.py
    uv run --no-project python comparator_annotations.py --self-test
"""

from __future__ import annotations

import argparse
import json
import pathlib
import time
import urllib.parse
import urllib.request

HERE = pathlib.Path(__file__).parent
OUT = HERE / "comparator_annotations.json"

QUICKGO = "https://www.ebi.ac.uk/QuickGO/services/annotation/search"

# (accession, label, go_id, expected evidence codes, expected reference substring)
# Every entry is a sentence that appears in the review.
EXPECTATIONS = [
    ("Q8N5V2", "NGEF / Ephexin1", "GO:0046875", {"IEA"}, "GO_REF:0000107"),
    ("Q8N5V2", "NGEF / Ephexin1", "GO:0005085", {"EXP"}, "PMID:15848799"),
    ("Q12774", "ARHGEF5 / Ephexin3", "GO:0005085", {"IDA"}, "PMID:15601624"),
    ("Q5VV41", "ARHGEF16 / Ephexin4", "GO:0005085", {"IDA"}, "PMID:20679435"),
    ("Q12774", "ARHGEF5 / Ephexin3", "GO:0032956", {"IMP"}, "PMID:14662653"),
    ("Q8IW93", "ARHGEF19 / Ephexin2", "GO:0032956", {"IGI"}, "PMID:20643356"),
    ("Q5FWH6", "mouse Arhgef15 (ISS/Ensembl donor)", "GO:0005085", {"IDA"}, "PMID:21029865"),
    ("Q5FWH6", "mouse Arhgef15 (ISS/Ensembl donor)", "GO:2000297", {"IMP"}, "PMID:21029865"),
    ("Q5FWH6", "mouse Arhgef15 (ISS/Ensembl donor)", "GO:0030425", {"IDA"}, "PMID:21029865"),
    ("Q5FWH6", "mouse Arhgef15 (ISS/Ensembl donor)", "GO:0098794", {"IDA", "IMP"}, "PMID:28185854"),
    ("Q5FWH6", "mouse Arhgef15 (ISS/Ensembl donor)", "GO:0098978", {"IDA", "IMP"}, "PMID:28185854"),
    ("Q5FWH6", "mouse Arhgef15 (ISS/Ensembl donor)", "GO:0150052", {"IDA", "IMP"}, "PMID:28185854"),
    ("D3ZPJ8", "rat Arhgef15 (ISS donor)", "GO:0005737", {"IDA"}, "PMID:12775584"),
    ("D3ZPJ8", "rat Arhgef15 (ISS donor)", "GO:0051496", {"IDA"}, "PMID:12775584"),
    ("Q5VV41", "ARHGEF16 / Ephexin4", "GO:0032489", {"IDA"}, "PMID:21139582"),
]


def fetch(accession: str) -> list[dict]:
    url = (
        f"{QUICKGO}?geneProductId="
        + urllib.parse.quote("UniProtKB:" + accession)
        + "&limit=200&includeFields=goName"
    )
    req = urllib.request.Request(
        url, headers={"Accept": "application/json", "User-Agent": "ai-gene-review"}
    )
    with urllib.request.urlopen(req, timeout=120) as fh:
        return json.load(fh)["results"]


def analyse() -> dict:
    cache: dict[str, list[dict]] = {}
    rows = []
    for acc, label, go_id, codes, ref in EXPECTATIONS:
        if acc not in cache:
            cache[acc] = fetch(acc)
            time.sleep(0.3)
        matching = [
            {
                "goId": r["goId"],
                "goName": r.get("goName"),
                "evidence": r["goEvidence"],
                "qualifier": r.get("qualifier"),
                "reference": r["reference"],
            }
            for r in cache[acc]
            if r["goId"] == go_id
        ]
        found_codes = {m["evidence"] for m in matching}
        refs = {m["reference"] for m in matching}
        rows.append(
            {
                "accession": acc,
                "label": label,
                "go_id": go_id,
                "expected_evidence": sorted(codes),
                "expected_reference": ref,
                "observed": matching,
                "evidence_ok": codes <= found_codes,
                "reference_ok": any(ref in r for r in refs),
            }
        )
    return {
        "source": "QuickGO annotation search",
        "n_claims": len(rows),
        "n_failing": sum(1 for r in rows if not (r["evidence_ok"] and r["reference_ok"])),
        "claims": rows,
    }


def self_test() -> int:
    failures = []

    def expect(name: str, ok: bool, detail: str = "") -> None:
        print(f"  [{'PASS' if ok else 'FAIL'}] {name} {detail}")
        if not ok:
            failures.append(name)

    res = analyse()
    for r in res["claims"]:
        expect(
            f"{r['label']} carries {r['go_id']} by {'/'.join(r['expected_evidence'])} "
            f"from {r['expected_reference']}",
            r["evidence_ok"] and r["reference_ok"],
            "" if (r["evidence_ok"] and r["reference_ok"]) else str(r["observed"])[:200],
        )

    # The predicate must be able to fail: a claim nobody makes must not verify.
    bogus = [r for r in res["claims"] if r["go_id"] == "GO:0046875"][0]
    fake_ok = any("PMID:99999999" in m["reference"] for m in bogus["observed"])
    expect("a reference that is not there does not verify", not fake_ok)

    print()
    if failures:
        print(f"SELF-TEST FAILED: {failures}")
        return 1
    print("SELF-TEST PASSED")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    if args.self_test:
        return self_test()
    res = analyse()
    OUT.write_text(json.dumps(res, indent=2, sort_keys=True) + "\n")
    for r in res["claims"]:
        mark = "ok  " if (r["evidence_ok"] and r["reference_ok"]) else "FAIL"
        print(
            f"  {mark} {r['label']:<36} {r['go_id']}  expected "
            f"{'/'.join(r['expected_evidence'])} {r['expected_reference']}"
        )
        if mark == "FAIL":
            print(f"       observed: {r['observed']}")
    print(f"\n{res['n_claims'] - res['n_failing']}/{res['n_claims']} claims verified")
    print(f"wrote {OUT}")
    return 1 if res["n_failing"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
