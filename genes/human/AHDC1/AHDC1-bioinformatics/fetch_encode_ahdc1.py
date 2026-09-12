#!/usr/bin/env python3
"""Fetch and cache the ENCODE metadata for the AHDC1 ChIP-seq experiment ENCSR168AUX.

Why this is a script and not a hand-written table. The AHDC1 review leans on one
non-obvious fact: the ENCODE HepG2 replication of AHDC1 chromatin occupancy is a
**CRISPR knock-in of a C-terminal 3xFLAG tag at the endogenous locus**, not a
transfected construct. That is what upgrades the replication from "different lab
and lineage" to "native promoter, endogenous expression level" -- which is the
axis the Stanford PiggyBac transgene cannot control, and therefore the axis that
matters for reading site occupancy. A claim doing that much work should be
re-derivable rather than transcribed.

The script answers two questions and refuses to guess at either:

  1. Is the ChIP target epitope-tagged?  (an eGFP/FLAG target is named as such,
     and any tag is recorded on the biosample's genetic_modifications)
  2. If tagged, was the tag introduced by CRISPR knock-in at the endogenous locus,
     or by transfecting a construct?  (`method` and `category` on the modification)

Writes ENCSR168AUX.json next to this file and prints the summary table that
RESULTS.md reproduces.

Run: uv run python genes/human/AHDC1/AHDC1-bioinformatics/fetch_encode_ahdc1.py
"""

from __future__ import annotations

import json
import sys
import urllib.request
from pathlib import Path

BASE = "https://www.encodeproject.org"
ACCESSION = "ENCSR168AUX"
OUT = Path(__file__).resolve().parent / f"{ACCESSION}.json"

TAG_TOKENS = ("egfp", "gfp", "flag", "ha-", "myc", "tag")


def get(path: str) -> dict:
    url = BASE + path + ("&" if "?" in path else "?") + "frame=object&format=json"
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    return json.load(urllib.request.urlopen(req))


def main() -> int:
    exp = get(f"/experiments/{ACCESSION}/")
    assert exp["accession"] == ACCESSION, f"fetched {exp['accession']}, wanted {ACCESSION}"
    assert exp["assay_term_name"] == "ChIP-seq", exp["assay_term_name"]

    target = get(exp["target"])
    # A tagged ENCODE target is NAMED for its tag (eGFP-AHDC1). An untagged target
    # name is therefore necessary but NOT sufficient -- the tag can still be
    # recorded on the biosample, which is exactly the case here.
    name_implies_tag = any(t in target["label"].lower() for t in TAG_TOKENS)

    mods: dict[str, dict] = {}
    antibodies: dict[str, dict] = {}
    for rep_path in exp["replicates"]:
        rep = get(rep_path)
        if rep.get("antibody"):
            ab = get(rep["antibody"])
            antibodies[ab["accession"]] = ab
        lib = rep.get("library")
        assert lib, f"replicate {rep_path} has no library"
        biosample_path = get(lib).get("biosample")
        assert biosample_path, f"library for {rep_path} has no biosample"
        for gm_path in get(biosample_path).get("genetic_modifications") or []:
            gm = get(gm_path)
            mods[gm["accession"]] = gm

    record = {
        "experiment": exp,
        "target": target,
        "genetic_modifications": mods,
        "antibodies": antibodies,
    }
    OUT.write_text(json.dumps(record, indent=2, sort_keys=True))

    print(f"{ACCESSION}: {exp['description']}  lab={exp['lab']}")
    print(f"  target                 {target['@id']}  label={target['label']!r}")
    print(f"  target name implies a tag?  {name_implies_tag}")
    print(f"  investigated_as        {target.get('investigated_as')}")
    if not mods:
        print("  genetic_modifications  NONE -- antibody against untagged endogenous protein")
    for acc, gm in sorted(mods.items()):
        tags = [f"{t['name']} ({t['location']})" for t in gm.get("introduced_tags") or []]
        print(
            f"  modification {acc}  category={gm['category']} purpose={gm['purpose']} "
            f"method={gm['method']} perturbation={gm['perturbation']}"
        )
        print(f"     introduced_tags     {tags}")
        print(f"     modified_site       {gm.get('modified_site_by_target_id')}")
    for acc, ab in sorted(antibodies.items()):
        print(f"  antibody {acc}  targets={ab.get('targets')}")

    # The two conclusions the review depends on, asserted rather than eyeballed.
    knockin = [
        g
        for g in mods.values()
        if g.get("method") == "CRISPR" and g.get("category") == "insertion"
    ]
    tagged = [g for g in mods.values() if g.get("introduced_tags")]
    print()
    print(f"  => epitope-tagged:            {bool(tagged)}")
    print(f"  => tag at endogenous locus:   {bool(knockin)} (CRISPR insertion)")
    print(f"  => cached to:                 {OUT.name}")

    problems = verdict_problems(mods)
    if problems:
        print()
        for p in problems:
            print("  x", p)
        return 1
    return 0


def verdict_problems(mods: dict[str, dict]) -> list[str]:
    """Return the reasons the review's GO:0003682 claims would need revising.

    Separated from ``main`` so it can be exercised on synthetic inputs. A check
    that reports but does not gate is not a check: both of these are conclusions
    the review rests on, so a run in which either flips must exit non-zero rather
    than print a warning into a log nobody reads.
    """
    knockin = [
        g for g in mods.values()
        if g.get("method") == "CRISPR" and g.get("category") == "insertion"
    ]
    tagged = [g for g in mods.values() if g.get("introduced_tags")]
    problems: list[str] = []
    if not tagged:
        problems.append(
            "target is NOT tagged - the review's 'both datasets are epitope-tagged' "
            "caveat would need revising"
        )
    if tagged and not knockin:
        problems.append(
            "tagged but NOT a CRISPR knock-in at the endogenous locus - the review's "
            "'native promoter, endogenous level' claim would need revising"
        )
    return problems


def self_test() -> int:
    """Break the gate on purpose. Each case must produce the problem it should."""
    real = json.loads(OUT.read_text())["genetic_modifications"] if OUT.exists() else None
    assert real, f"{OUT.name} missing - run the fetch first so the baseline is real data"

    cases = {
        "real_record_passes": (real, 0),
        "untagged_fails": (
            {"X": {"method": "CRISPR", "category": "insertion", "introduced_tags": []}},
            1,
        ),
        "transfected_tag_fails": (
            {
                "X": {
                    "method": "transfection",
                    "category": "insertion",
                    "introduced_tags": [{"name": "eGFP", "location": "N-terminal"}],
                }
            },
            1,
        ),
        "no_modifications_fails": ({}, 1),
    }
    ok = True
    print("self-test:")
    for name, (mods, want) in cases.items():
        got = len(verdict_problems(mods))
        passed = (got > 0) == (want > 0)
        ok = ok and passed
        print(f"  {name}: {'OK' if passed else 'BROKEN'} (problems={got}, expected>0={want > 0})")
    return 0 if ok else 1


if __name__ == "__main__":
    if "--self-test" in sys.argv:
        sys.exit(self_test())
    sys.exit(main())
