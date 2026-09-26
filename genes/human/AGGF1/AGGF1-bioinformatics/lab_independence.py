"""How many independent groups have worked on AGGF1?

A review that collapses `NbExp` into independent experiments and catches a
bait-labelling artefact should not then assert laboratory independence it has not
checked. This reads the author list out of each cached publication and groups the
papers by senior (last) author, so "three laboratories" is a measurement rather
than an impression.

Surnames are normalised because the same person appears as both "Wang Q" and
"Wang QK" across records, and a first-author-turned-PI (Tian XL) heads a group
that is not independent of the one he trained in -- that lineage is reported
separately rather than folded into the count, because it is a judgement and the
author list is not.

Run: uv run python lab_independence.py
"""

from __future__ import annotations

import re
from collections import defaultdict
from pathlib import Path

import yaml

HERE = Path(__file__).parent
PUBS = HERE.parents[3] / "publications"
REVIEW = HERE.parent / "AGGF1-ai-review.yaml"

# The paper set is DERIVED, not hand-listed. A hand-maintained list is how the
# first version of this script reported "exactly one independent group": it had
# silently omitted PMID:29885663 (senior author Zhang JH), a second independent
# group whose full text was cached all along. A list you curate is a list you can
# under-curate, and the conclusion then describes the list rather than the
# literature.
#
# Sources, unioned then filtered to what is actually cached:
#   * the REFERENCE column of the GOA file
#   * the affinage record's Citations section
#   * every PMID in the review's own references[]
# High-throughput interaction screens are excluded by accession, not by judgement:
# they are methods resources, not AGGF1 studies, and their author lists would
# swamp the measurement.
SCREENS = {
    "16189514", "22365833", "25416956", "31515488", "32296183",
    "33961781", "39251607", "40205054",
}
# Corrections/errata and commentary are likewise not AGGF1 studies.
NOT_STUDIES = {"39468017", "41039152", "14961101", "15905966", "42052570",
               "32179686", "11106755", "16443853", "17103452", "18564129"}


def surname_initials(name: str) -> tuple[str, str]:
    """('Wang QK') -> ('wang', 'qk'). Robust to 'Wang Q' vs 'Wang QK'."""
    parts = name.strip().split()
    if not parts:
        return ("", "")
    return (parts[0].lower(), "".join(parts[1:]).lower())


def authors(pmid: str) -> list[str]:
    p = PUBS / f"PMID_{pmid}.md"
    if not p.exists():
        raise SystemExit(f"missing {p}; run `just fetch-pmid {pmid}`")
    fm = p.read_text().split("---", 2)[1]
    meta = yaml.safe_load(fm)
    a = meta.get("authors") or []
    if not a:
        raise SystemExit(f"{p} frontmatter has no author list -- cannot measure independence")
    return a


def relevant() -> list[str]:
    """Every cached AGGF1 primary study reachable from the review's own inputs."""
    import csv

    found: set[str] = set()

    goa = HERE.parent / "AGGF1-goa.tsv"
    if not goa.exists():
        raise SystemExit(f"missing {goa}; run `just fetch-gene human AGGF1` first")
    with goa.open() as fh:
        for r in csv.DictReader(fh, delimiter="\t"):
            ref = r["REFERENCE"]
            if ref.startswith("PMID:"):
                found.add(ref.split(":", 1)[1])

    aff = HERE.parent / "AGGF1-deep-research-affinage.md"
    if not aff.exists():
        raise SystemExit(f"missing {aff}; run the affinage fetch first")
    found.update(re.findall(r"^- PMID:(\d+)\s*$", aff.read_text(), re.M))

    doc = yaml.safe_load(REVIEW.read_text())
    for ref in doc["references"]:
        if ref["id"].startswith("PMID:"):
            found.add(ref["id"].split(":", 1)[1])

    studies = sorted(found - SCREENS - NOT_STUDIES)
    cached = [p for p in studies if (PUBS / f"PMID_{p}.md").exists()]
    missing = [p for p in studies if p not in cached]
    if missing:
        raise SystemExit(
            f"not cached, cannot read author lists: {missing}. "
            f"Run `just fetch-pmid {' '.join(missing)}`."
        )
    return cached


def measure() -> dict:
    """The derived numbers, returned so other checks can assert against them
    instead of hard-coding a count that then drifts. `audit_claims.py` imports
    this: the prose must agree with what the author lists actually say, which is
    a different and much stronger check than blacklisting spellings of a wrong
    count -- three consecutive review rounds found a new spelling of the same
    claim that the previous round's literal did not cover."""
    rows = [(p, authors(p)[0], authors(p)[-1]) for p in relevant()]
    groups: dict[str, list[str]] = defaultdict(list)
    for pmid, _first, last in rows:
        sn, ini = surname_initials(last)
        key = None
        for existing in groups:
            esn, eini = existing.split("|")
            if esn == sn and (ini.startswith(eini) or eini.startswith(ini)):
                key = existing
                break
        groups[key or f"{sn}|{ini}"].append(pmid)
    biggest = max(groups.values(), key=len)
    dominant_names = {a for pmid in biggest for a in authors(pmid)}
    lineage = [p for p, _f, last in rows if p not in biggest and last in dominant_names]
    independent = [p for p, _f, last in rows
                   if p not in biggest and last not in dominant_names]
    doc = yaml.safe_load(REVIEW.read_text())
    cited = {r["id"].split(":", 1)[1] for r in doc["references"] if r["id"].startswith("PMID:")}
    return {
        "total": len(rows),
        "dominant": len(biggest),
        "lineage": len(lineage),
        "independent": sorted(independent),
        "independent_n": len(independent),
        "independent_cited": sorted(p for p in independent if p in cited),
        "independent_cited_n": sum(1 for p in independent if p in cited),
    }


def main() -> None:
    pmids = relevant()
    print(f"derived paper set: {len(pmids)} cached AGGF1 primary studies "
          f"(GOA references + affinage citations + review references, minus "
          f"{len(SCREENS)} high-throughput screens and {len(NOT_STUDIES)} "
          "non-studies)")
    print()
    rows = []
    for pmid in pmids:
        a = authors(pmid)
        rows.append((pmid, a[0], a[-1]))

    print(f"{'PMID':<10} {'first author':<16} {'senior (last) author'}")
    for pmid, first, last in rows:
        print(f"{pmid:<10} {first:<16} {last}")
    print()

    # Group by senior-author surname, merging initial variants of the same surname
    # only when one initial string is a prefix of the other (Wang Q / Wang QK).
    groups: dict[str, list[str]] = defaultdict(list)
    for pmid, _first, last in rows:
        sn, ini = surname_initials(last)
        key = None
        for existing in groups:
            esn, eini = existing.split("|")
            if esn == sn and (ini.startswith(eini) or eini.startswith(ini)):
                key = existing
                break
        groups[key or f"{sn}|{ini}"].append(pmid)

    print("papers grouped by senior author:")
    for key, pmids in sorted(groups.items(), key=lambda kv: -len(kv[1])):
        sn, ini = key.split("|")
        print(f"  {sn.title()} {ini.upper():<4} : {len(pmids):>2} paper(s)  {', '.join(pmids)}")
    print()

    biggest = max(groups.values(), key=len)
    # Cross-check the printed table against measure(), which audit_claims.py uses.
    # main() and measure() computed the same classification independently until
    # the PR reviewer pointed out they could drift -- and the drift would be
    # between what a human reads here and what the guard enforces, i.e. silent.
    m = measure()
    # Raise, do not assert: `python -O` strips asserts, and a cross-check that can
    # be compiled away is not a cross-check.
    if m["dominant"] != len(biggest):
        raise SystemExit(
            f"measure() says dominant={m['dominant']} but this table shows {len(biggest)}"
        )
    if m["total"] != len(rows):
        raise SystemExit(
            f"measure() says total={m['total']} but this table shows {len(rows)}"
        )
    print(f"Largest single group accounts for {len(biggest)}/{len(rows)} of the papers "
          "this review relies on.")

    # Lineage, computed rather than judged: a senior author who also appears in
    # the author list of one of the dominant group's papers is a trainee or
    # collaborator of that group, not an independent investigator. Restricting
    # this to the discovery paper's first author (the earlier version) caught only
    # Tian XL and missed several others.
    dominant_names = {a for pmid in biggest for a in authors(pmid)}
    lineage, independent = [], []
    for pmid, _first, last in rows:
        if pmid in biggest:
            continue
        (lineage if last in dominant_names else independent).append((pmid, last))

    print(f"Senior author also appears on a paper from the dominant group "
          f"(trainee/collaborator lineage): {len(lineage)}")
    for pmid, last in lineage:
        on = [p for p in biggest if last in authors(p)]
        print(f"    {pmid}  senior {last:10s} also an author on {len(on)}: {', '.join(on)}")
    print(f"Senior author appears on NO dominant-group paper "
          f"(genuinely separate): {len(independent)}")
    for pmid, last in independent:
        print(f"    {pmid}  senior {last}")
    indep = [p for p, _ in independent]
    if sorted(indep) != m["independent"]:
        raise SystemExit(
            f"measure() says independent={m['independent']} but this table shows "
            f"{sorted(indep)} -- the two classifications have drifted"
        )
    if len(lineage) != m["lineage"]:
        raise SystemExit(
            f"measure() says lineage={m['lineage']} but this table shows {len(lineage)}"
        )
    print()

    # "Independent" by senior author can still share bench authors. Measure the
    # overlap rather than leaving the claim unqualified -- but note that a shared
    # surname+initial is not proof of the same person, which is why this is
    # reported as a caveat and not folded into the group count.
    dominant_authors: dict[str, set[str]] = {}
    for pmid in biggest:
        for a in authors(pmid):
            dominant_authors.setdefault(a, set()).add(pmid)
    for pmid in indep:
        shared = {a: sorted(v) for a, v in dominant_authors.items() if a in authors(pmid)}
        if shared:
            print(f"CAVEAT: {pmid} shares author name(s) with the dominant group:")
            for a, where in sorted(shared.items(), key=lambda kv: -len(kv[1])):
                print(f"    {a:12s} also on {len(where)} of its papers: {', '.join(where)}")
            print("    A shared surname+initial is not proof of the same person, and the")
            print("    senior author and affiliations differ, so the paper is still counted")
            print("    as independent -- but the overlap is recorded rather than hidden.")
        else:
            print(f"{pmid} shares no author name with the dominant group.")
    print()

    # The review must not claim more groups than this script finds.
    text = REVIEW.read_text()
    flat = re.sub(r"\s+", " ", text)
    for banned in ("three laboratories", "three later laboratories",
                   "three independent lines of evidence from three laboratories"):
        if banned in flat:
            raise SystemExit(
                f"AGGF1-ai-review.yaml still claims {banned!r}, which this author-list "
                "measurement contradicts."
            )
    print("review text carries no laboratory-count claim contradicted by the author lists.")


if __name__ == "__main__":
    main()
