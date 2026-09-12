#!/usr/bin/env python3
"""Quantify EC-masking and EC/RHEA/GO specificity for the RHEA project.

Companion to ``rhea_go_gap_probe.py``. Where that script asks the *reverse-gap*
question (UniProt RHEA annotations that never propagate to GO), this script
asks the questions raised when RHEA is compared against EC:

1. MASKING. RHEA reaches GO via ``rhea2go`` (GOA ``GO_REF:0000116``); EC reaches
   GO via ``ec2go`` (GOA ``GO_REF:0000003``). For an enzyme carrying both an EC
   number and a RHEA reaction, EC2GO already supplies a GO MF term. How often is
   the term ``rhea2go`` would add *identical* to one EC2GO already supplies (so
   RHEA's contribution is masked), versus genuinely additional?

2. SPECIFICITY. A single EC number typically corresponds to many RHEA reactions
   (different substrates / cofactors / directions). Does that reaction-level
   specificity survive the trip to GO, or does it collapse onto one generic GO
   activity term?

3. GAPS. Which enzymatic RHEA reactions (those carrying an EC) have no
   ``rhea2go`` GO target at all?

All inputs are fetched live; no results are hardcoded. The EC mapping is pulled
from the RHEA REST API (``ftp.expasy.org`` is often blocked, the REST API is
not). Run:

    uv run python rhea_ec_specificity.py
"""
from __future__ import annotations

import re
import sys
import urllib.parse
import urllib.request
from collections import defaultdict

RHEA2GO_URL = "https://current.geneontology.org/ontology/external2go/rhea2go"
EC2GO_URL = "https://current.geneontology.org/ontology/external2go/ec2go"
RHEA_API = "https://www.rhea-db.org/rhea"

_R2G = re.compile(r"RHEA:(\d+) > GO:(.+) ; (GO:\d+)")
_E2G = re.compile(r"EC:(\S+) > GO:(.+) ; (GO:\d+)")


def _get(url: str, timeout: int = 90) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "ai-gene-review-rhea/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read().decode()


def load_rhea2go() -> dict[str, tuple[str, str]]:
    out: dict[str, tuple[str, str]] = {}
    for line in _get(RHEA2GO_URL).splitlines():
        m = _R2G.match(line)
        if m:
            out[m.group(1)] = (m.group(3), m.group(2))
    return out


def load_ec2go() -> tuple[dict[str, set[str]], dict[str, str]]:
    ec2g: dict[str, set[str]] = defaultdict(set)
    label: dict[str, str] = {}
    for line in _get(EC2GO_URL).splitlines():
        m = _E2G.match(line)
        if m:
            ec2g[m.group(1)].add(m.group(3))
            label[m.group(3)] = m.group(2)
    return ec2g, label


def load_rhea2ec() -> dict[str, str]:
    params = urllib.parse.urlencode(
        {"query": "", "columns": "rhea-id,ec", "format": "tsv", "limit": 200000}
    )
    out: dict[str, str] = {}
    for line in _get(f"{RHEA_API}?{params}").splitlines()[1:]:
        parts = line.split("\t")
        if len(parts) >= 2 and parts[1].strip():
            out[parts[0].replace("RHEA:", "")] = parts[1].replace("EC:", "")
    return out


def main() -> int:
    r2g = load_rhea2go()
    ec2g, _ = load_ec2go()
    rhea2ec = load_rhea2ec()
    go_label = {go: lab for go, lab in r2g.values()}

    rhea_terms = {go for go, _ in r2g.values()}
    ec_terms = {go for s in ec2g.values() for go in s}
    print("== mapping sizes ==")
    print(f"rhea2go: {len(r2g)} reactions -> {len(rhea_terms)} GO terms")
    print(f"ec2go  : {sum(len(s) for s in ec2g.values())} rows -> {len(ec_terms)} GO terms")
    print(f"shared GO terms (RHEA maskable by EC): {len(rhea_terms & ec_terms)}")
    print(f"RHEA-only GO terms (EC cannot deliver): {len(rhea_terms - ec_terms)}")
    print(f"EC-only GO terms                      : {len(ec_terms - rhea_terms)}")

    print("\n== reaction-level EC masking ==")
    both = same = differ = ec_no_go = 0
    for rid, (go, _) in r2g.items():
        ec = rhea2ec.get(rid)
        if not ec:
            continue
        both += 1
        ecgos = ec2g.get(ec)
        if not ecgos:
            ec_no_go += 1
        elif go in ecgos:
            same += 1
        else:
            differ += 1
    print(f"RHEA reactions with both a rhea2go term and an EC: {both}")
    print(f"  EC has an ec2go term: {both - ec_no_go} | EC has no ec2go term: {ec_no_go}")
    print(f"  RHEA term == an EC term (fully masked): {same}")
    print(f"  RHEA term differs from EC term        : {differ}")

    print("\n== EC -> RHEA -> GO specificity ==")
    ec_to_rheas: dict[str, set[str]] = defaultdict(set)
    for rid in r2g:
        ec = rhea2ec.get(rid)
        if ec:
            ec_to_rheas[ec].add(rid)
    multi = {ec: rs for ec, rs in ec_to_rheas.items() if len(rs) > 1}
    collapse = sum(1 for rs in multi.values() if len({r2g[r][0] for r in rs}) == 1)
    spread = len(multi) - collapse
    print(f"ECs mapping to >1 RHEA reaction: {len(multi)} of {len(ec_to_rheas)}")
    print(f"  collapse to ONE GO term (specificity lost): {collapse}")
    print(f"  spread across MULTIPLE GO terms (GO keeps a split EC lumps): {spread}")

    from collections import Counter
    cnt = Counter(go for go, _ in r2g.values())
    print(f"GO terms backed by >1 RHEA reaction: {sum(1 for v in cnt.values() if v > 1)}")
    print("top specificity-collapse GO terms:")
    for go, n in cnt.most_common(8):
        print(f"  {n:3d}  {go}  {go_label[go]}")

    print("\n== gaps: enzymatic reactions with no GO target ==")
    ec_rheas: dict[str, set[str]] = defaultdict(set)
    for rid, ec in rhea2ec.items():
        ec_rheas[ec].add(rid)
    ec_covered = {ec for ec, rs in ec_rheas.items() if any(r in r2g for r in rs)}
    no_go = [r for r in rhea2ec if r not in r2g]
    ec_level = [r for r in no_go if rhea2ec[r] not in ec_covered]
    print(f"EC-carrying RHEA reactions: {len(rhea2ec)}")
    print(f"  with a rhea2go term   : {len(rhea2ec) - len(no_go)}")
    print(f"  with NO rhea2go term  : {len(no_go)} ({100*len(no_go)/len(rhea2ec):.0f}%)")
    print(f"    EC-level rhea2go gap (no sibling covered): {len(ec_level)}"
          f" across {len({rhea2ec[r] for r in ec_level})} ECs")
    print(f"    specific-reaction-only gap (sibling covered): {len(no_go) - len(ec_level)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
