#!/usr/bin/env python3
"""Quantify the marginal contribution of cazy2go OVER interpro2go.

The cazy2go mapping (CAZy family -> GO MF, via EC -> ec2go) is only worth maintaining where it
reaches a GO molecular-function term that the family's proteins do NOT already get via the existing
InterPro2GO route. This is the CAZy analogue of the RHEA "masked by EC" analysis.

Method (all live, no hand input):
  * UniProtKB (reviewed) -> per entry: xref_cazy, ec, xref_interpro.
      fam_ec[fam]      = ECs seen on the family's reviewed members
      fam_interpro[fam]= InterPro signatures seen on the family's reviewed members
  * ec2go        : EC -> GO MF terms   (the cazy2go target route)
  * interpro2go  : InterPro -> GO terms (the competing route)
  * For each family:
      cazy_go     = union over its ECs of ec2go terms (generic-parent-filtered, as in the build)
      interpro_go = union over its InterPro signatures of interpro2go terms
      marginal    = cazy_go - interpro_go   (CAZy-reachable GO MF that InterPro does NOT supply)

Caveat: EXACT-ID comparison (no ontology closure), so `marginal` is an UPPER BOUND on the true
unique contribution -- a CAZy term may be an ancestor/descendant of an InterPro-supplied term.
interpro_go includes all GO aspects (BP/CC too), which only makes the masking test more conservative.

Usage:  uv run python projects/GLYCOBIOLOGY/compare_cazy_interpro.py
"""

from __future__ import annotations

import re
import sys
import urllib.parse
import urllib.request
from collections import Counter, defaultdict

sys.path.insert(0, "projects/GLYCOBIOLOGY")
from build_cazy2go import load_ec2go, GENERIC_PARENTS  # noqa: E402

UNIPROT_URL = "https://rest.uniprot.org/uniprotkb/search"
UA = {"User-Agent": "ai-gene-review-cazy2go/1.0"}
INTERPRO2GO_URLS = [
    "https://current.geneontology.org/ontology/external2go/interpro2go",
    "https://ftp.ebi.ac.uk/pub/databases/GO/goa/external2go/interpro2go",
]


def _get(url):
    return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=120)


def load_interpro2go() -> dict[str, set[str]]:
    """Return {IPRxxxxxx: {GO:...}} from the GO interpro2go file.

    Lines look like:  InterPro:IPR000001 Kringle > GO:... ; GO:0005515
    """
    text = None
    for url in INTERPRO2GO_URLS:
        try:
            text = _get(url).read().decode("utf-8", "replace")
            break
        except Exception as e:  # noqa: BLE001
            print(f"  (interpro2go {url} failed: {type(e).__name__})", file=sys.stderr)
    if text is None:
        raise RuntimeError("could not fetch interpro2go")
    out: dict[str, set[str]] = defaultdict(set)
    line_re = re.compile(r"^InterPro:(IPR\d+)\b.*?;\s*(GO:\d+)\s*$")
    for line in text.splitlines():
        if line.startswith("!"):
            continue
        m = line_re.match(line.strip())
        if m:
            out[m.group(1)].add(m.group(2))
    return out


def load_cazy_ec_interpro():
    """Page UniProtKB reviewed CAZy entries; collect ECs and InterPro per family."""
    fam_ec: dict[str, set[str]] = defaultdict(set)
    fam_interpro: dict[str, set[str]] = defaultdict(set)
    fam_members: dict[str, set[str]] = defaultdict(set)
    params = {
        "query": "reviewed:true AND database:cazy AND ec:*",
        "fields": "accession,ec,xref_cazy,xref_interpro",
        "format": "tsv",
        "size": "500",
    }
    url = UNIPROT_URL + "?" + urllib.parse.urlencode(params)
    while url:
        resp = _get(url)
        lines = resp.read().decode("utf-8", "replace").splitlines()
        for line in lines[1:]:
            parts = line.split("\t")
            if len(parts) < 4:
                continue
            acc, ec_field, cazy_field, ipr_field = parts[0], parts[1], parts[2], parts[3]
            ecs = [e.strip() for e in ec_field.split(";") if e.strip()]
            fams = [f.strip() for f in cazy_field.split(";") if f.strip()]
            iprs = re.findall(r"IPR\d+", ipr_field)
            if not ecs or not fams:
                continue
            for fam in fams:
                fam_members[fam].add(acc)
                fam_ec[fam].update(ecs)
                fam_interpro[fam].update(iprs)
        m = re.search(r'<([^>]+)>;\s*rel="next"', resp.headers.get("Link", ""))
        url = m.group(1) if m else None
    return fam_ec, fam_interpro, fam_members


def cazy_go_for_family(ecs, ec2go):
    terms = {}
    for ec in ecs:
        for gid, lbl in ec2go.get(ec, []):
            terms[gid] = lbl
    spec = {g: l for g, l in terms.items() if g not in GENERIC_PARENTS}
    if spec and len(spec) < len(terms):
        terms = spec
    return terms


def main():
    print("Loading ec2go, interpro2go, UniProt CAZy+EC+InterPro ...", file=sys.stderr)
    ec2go = load_ec2go()
    ipr2go = load_interpro2go()
    fam_ec, fam_interpro, fam_members = load_cazy_ec_interpro()
    print(f"  ec2go={len(ec2go)} EC | interpro2go={len(ipr2go)} IPR | families={len(fam_ec)}",
          file=sys.stderr)

    stats = Counter()
    fully_masked, partial, marginal_examples = [], [], []
    total_marginal_pairs = 0
    for fam in fam_ec:
        cazy_go = cazy_go_for_family(fam_ec[fam], ec2go)
        if not cazy_go:
            continue
        stats["families_with_cazy_go"] += 1
        ipr_go = set()
        for ipr in fam_interpro[fam]:
            ipr_go |= ipr2go.get(ipr, set())
        marginal = {g: l for g, l in cazy_go.items() if g not in ipr_go}
        if not marginal:
            stats["families_fully_masked_by_interpro"] += 1
            fully_masked.append(fam)
        else:
            stats["families_with_marginal"] += 1
            total_marginal_pairs += len(marginal)
            partial.append((fam, len(marginal), len(cazy_go), len(fam_members[fam])))
            for gid, lbl in marginal.items():
                marginal_examples.append((fam, len(fam_members[fam]), gid, lbl))

    n = stats["families_with_cazy_go"]
    print("\n================ cazy2go vs interpro2go ================")
    print(f"families with a cazy2go GO MF term      : {n}")
    print(f"  fully masked by interpro2go (no gain) : {stats['families_fully_masked_by_interpro']} "
          f"({100*stats['families_fully_masked_by_interpro']/n:.0f}%)")
    print(f"  with >=1 MARGINAL GO MF term          : {stats['families_with_marginal']} "
          f"({100*stats['families_with_marginal']/n:.0f}%)")
    print(f"total marginal (family, GO) pairs       : {total_marginal_pairs}  (exact-match upper bound)")

    partial.sort(key=lambda x: -x[1])
    print("\n-- top families by # marginal GO MF terms (n_marginal / n_cazy_go / members) --")
    for fam, nm, nc, mem in partial[:15]:
        print(f"  {fam:7} {nm:2}/{nc:<2} terms  ({mem} members)")

    # exemplar families from the project
    print("\n-- project exemplar families --")
    want = {"GT31", "GT13", "GT29", "GT7", "GT65"}
    for fam, mem, gid, lbl in marginal_examples:
        if fam in want:
            print(f"  {fam:6} MARGINAL {gid} {lbl[:55]}")


if __name__ == "__main__":
    main()
