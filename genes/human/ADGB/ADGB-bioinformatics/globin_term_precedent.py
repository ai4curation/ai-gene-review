"""Regenerate the curator-precedent table in ADGB-notes.md from QuickGO.

The PR reviewer's fair objection to the first version: the table was pasted from
an ad-hoc query, so it was unverifiable from the checkout - the comparator genes
are not in this repo and the review environment has no web search.  This script
makes the claim reproducible: run it and the table regenerates, so a stale or
invented number is caught by a diff rather than by trust.

    uv run python globin_term_precedent.py                 # print the table
    uv run python globin_term_precedent.py --check-notes   # diff vs ADGB-notes.md
    uv run python globin_term_precedent.py --self-test     # break the guards

What it answers: for each characterised human globin, and for the terms this
review argues about, which GO annotations exist and with what evidence codes.
Three specific claims in the review depend on it, and each is asserted here so
the script fails loudly if QuickGO's content moves under us:

  1. GO:0019825 KEEP is precedented - NGB and CYGB, hexacoordinate globins that
     are not O2 transporters, hold it by IDA.
  2. GO:0098809 is the term GOA uses for globin nitrite reductase activity, and
     none of the globins uses the GO:0050421 child.
  3. GO:0070026 is precedented for five-coordinate NO hemoprotein chemistry.
"""

from __future__ import annotations

import argparse
import json
import sys
import urllib.parse
import urllib.request
from pathlib import Path

QUICKGO = "https://www.ebi.ac.uk/QuickGO/services/annotation/search"

GLOBINS = [
    ("Q9NPG2", "neuroglobin"),
    ("Q8WWM9", "cytoglobin"),
    ("P02144", "myoglobin"),
    ("P69905", "haemoglobin alpha"),
]
TERMS = [
    ("GO:0019825", "O2 binding"),
    ("GO:0020037", "heme"),
    ("GO:0098809", "nitrite reductase"),
    ("GO:0050421", "nitrite reductase (NO-forming)"),
    ("GO:0070026", "NO binding"),
]
EXPERIMENTAL = {"EXP", "IDA", "IPI", "IMP", "IGI", "IEP",
                "HTP", "HDA", "HMP", "HGI", "HEP"}


def query(**params) -> list[dict]:
    """Query QuickGO, refusing to return a silently truncated page.

    Compare numberOfHits against len(results), never against a page-size
    constant we chose: if the service clamps instead of erroring, a
    constant-based guard sails past exactly the truncation it exists to catch.
    """
    params.setdefault("limit", 200)
    url = QUICKGO + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    with urllib.request.urlopen(req) as fh:
        d = json.load(fh)
    n, res = d.get("numberOfHits", 0), d.get("results", [])
    if n > len(res):
        raise SystemExit(
            f"FATAL: truncated response ({n} hits, {len(res)} returned) for {url}. "
            f"Paginate rather than reporting a page total as a whole.")
    return res


def codes_for(acc: str, go: str) -> list[str]:
    """Evidence codes for a gene product against one term (exact term, no descendants).

    goUsage is deliberately NOT set to descendants here: the question is which
    term the entry actually holds, so rolling children up would answer a
    different question and would make GO:0050421 indistinguishable from its
    GO:0098809 parent - the very distinction claim 2 rests on.
    """
    rows = query(geneProductId=f"UniProtKB:{acc}", goId=go)
    return sorted({r["goEvidence"] for r in rows if r["goId"] == go})


def build_table() -> tuple[list[list[str]], dict]:
    shown = [t for t in TERMS if t[0] in
             ("GO:0019825", "GO:0020037", "GO:0098809")]
    header = [""] + [f"{gid} {lab}" for gid, lab in shown]
    rows, data = [header], {}
    for acc, name in GLOBINS:
        data[acc] = {gid: codes_for(acc, gid) for gid, _ in TERMS}
        cells = []
        for gid, _ in shown:
            c = data[acc][gid]
            cell = " + ".join(c) if c else "-"
            if any(x in EXPERIMENTAL for x in c):
                cell = f"**{cell}**" if gid == "GO:0098809" else cell
            cells.append(cell)
        rows.append([f"{name} {acc}"] + cells)
    return rows, data


def render(rows: list[list[str]]) -> str:
    out = ["| " + " | ".join(rows[0]) + " |",
           "|" + "---|" * len(rows[0])]
    for r in rows[1:]:
        out.append("| " + " | ".join(r) + " |")
    return "\n".join(out)


def assert_claims(data: dict) -> tuple[list[str], dict]:
    """The three review claims, asserted so a QuickGO change fails loudly.

    Returns (problems, GO:0070026 holders keyed by symbol).  The annotation was
    previously ``-> list[str]`` while the body returned a tuple; corrected here
    rather than left as a comment, because a wrong signature is exactly what
    makes a caller unpack the wrong thing later.
    """
    problems = []
    # 1. NGB and CYGB hold GO:0019825 by IDA
    for acc in ("Q9NPG2", "Q8WWM9"):
        if "IDA" not in data[acc]["GO:0019825"]:
            problems.append(
                f"CLAIM 1 BROKEN: {acc} no longer holds GO:0019825 by IDA "
                f"(codes: {data[acc]['GO:0019825']})")
    # 2a. the three characterised globins hold GO:0098809 experimentally
    for acc in ("Q9NPG2", "Q8WWM9", "P02144"):
        if not (set(data[acc]["GO:0098809"]) & EXPERIMENTAL):
            problems.append(
                f"CLAIM 2 BROKEN: {acc} has no experimental GO:0098809 "
                f"(codes: {data[acc]['GO:0098809']})")
    # 2b. none of them uses the GO:0050421 child
    for acc, _ in GLOBINS:
        if data[acc]["GO:0050421"]:
            problems.append(
                f"CLAIM 2 BROKEN: {acc} DOES hold GO:0050421 "
                f"(codes: {data[acc]['GO:0050421']}) - the review says none does")
    # 3. GO:0070026 precedent, with each holder's own evidence code printed
    holders = query(goId="GO:0070026", taxonId=9606)
    by = {}
    for r in holders:
        by.setdefault(r.get("symbol") or r["geneProductId"], set()).add(r["goEvidence"])
    if "GUCY1B1" not in by:
        problems.append(f"CLAIM 3 BROKEN: GUCY1B1 absent from GO:0070026 holders "
                        f"({sorted(by)})")
    else:
        # Guard the DISTINCTION, not merely the presence.  The review originally
        # wrote that THAP4 and CPX-2158 "also" hold the term by IDA next to a
        # mention of GUCY1B1, which could be read as covering GUCY1B1 too - it is
        # IEA.  A guard that only checks GUCY1B1 is *present* leaves precisely
        # the corrected distinction unguarded, which is where the next
        # regression would land.
        if by["GUCY1B1"] != {"IEA"}:
            problems.append(
                f"CLAIM 3 EVIDENCE-CODE DRIFT: the review states GUCY1B1 holds "
                f"GO:0070026 by IEA and that the experimental precedent comes from "
                f"the other holders; QuickGO now reports {sorted(by['GUCY1B1'])}. "
                f"Update the wording on all three surfaces before relying on it.")
    # ... and the experimental precedent must actually be experimental.
    for sym in ("CBS", "THAP4"):
        if sym not in by:
            problems.append(f"CLAIM 3 BROKEN: {sym} absent from GO:0070026 holders "
                            f"({sorted(by)})")
        elif not (by[sym] & EXPERIMENTAL):
            problems.append(
                f"CLAIM 3 BROKEN: {sym} no longer holds GO:0070026 experimentally "
                f"(codes: {sorted(by[sym])}) - the review cites it as the "
                f"experimental precedent")
    # ADGB would be the first single-chain globin with GO:0070026
    for acc, _ in GLOBINS:
        if data[acc]["GO:0070026"]:
            problems.append(
                f"CLAIM 3 QUALIFIER BROKEN: {acc} now holds GO:0070026 - the review "
                f"says no individual monomeric globin does")
    return problems, by


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--check-notes", action="store_true")
    args = ap.parse_args()

    if args.self_test:
        fails = []
        # happy direction: the real data must satisfy every claim
        _, data = build_table()
        probs, _ = assert_claims(data)
        if probs:
            fails.append(f"[happy] real data violates a claim: {probs}")
        # catch direction: a doctored dataset must be rejected
        import copy
        bad = copy.deepcopy(data)
        bad["Q9NPG2"]["GO:0019825"] = ["IEA"]
        if not assert_claims(bad)[0]:
            fails.append("[catch] removing NGB's IDA did not break claim 1")
        bad2 = copy.deepcopy(data)
        bad2["P02144"]["GO:0050421"] = ["IDA"]
        if not assert_claims(bad2)[0]:
            fails.append("[catch] adding a GO:0050421 holder did not break claim 2b")
        bad3 = copy.deepcopy(data)
        bad3["Q8WWM9"]["GO:0070026"] = ["IDA"]
        if not assert_claims(bad3)[0]:
            fails.append("[catch] a monomeric globin gaining GO:0070026 did not break claim 3")
        # the GUCY1B1 evidence-code guard must fire on a code change, not just
        # on absence - this is the distinction the review had to correct, so it
        # is the one that most needs a break test.
        real = globals()["query"]

        def fake_query(**kw):
            if kw.get("goId") == "GO:0070026" and kw.get("taxonId") == 9606:
                return [{"symbol": "GUCY1B1", "goEvidence": "IDA", "goId": "GO:0070026"},
                        {"symbol": "CBS", "goEvidence": "IDA", "goId": "GO:0070026"},
                        {"symbol": "THAP4", "goEvidence": "IDA", "goId": "GO:0070026"}]
            return real(**kw)

        globals()["query"] = fake_query
        try:
            probs4 = assert_claims(copy.deepcopy(data))[0]
        finally:
            globals()["query"] = real
        if not any("EVIDENCE-CODE DRIFT" in p for p in probs4):
            fails.append("[catch] GUCY1B1 flipping IEA->IDA did not fire the "
                         "evidence-code guard")
        # ... and the happy direction of that same guard: real data must NOT fire it
        if any("EVIDENCE-CODE DRIFT" in p for p in assert_claims(copy.deepcopy(data))[0]):
            fails.append("[happy] evidence-code guard fires on the real data")
        # truncation guard must not be defeatable by a chosen page size
        try:
            query(goId="GO:0005515", taxonId=9606, limit=1)
            fails.append("[catch] truncation guard did not fire on a deliberately tiny page")
        except SystemExit:
            pass
        if fails:
            print("SELF-TEST FAILED:")
            for f in fails:
                print("  -", f)
            sys.exit(1)
        print("SELF-TEST PASSED: happy direction holds (twice - the claim set and "
              "the GUCY1B1 evidence-code guard specifically); 4 doctored datasets "
              "rejected, including GUCY1B1 flipping IEA->IDA, which is the exact "
              "distinction the review had to correct; truncation guard fires.")
        return

    rows, data = build_table()
    table = render(rows)
    print(table)
    problems, holders = assert_claims(data)
    print("\nGO:0070026 human holders, with their own evidence codes:")
    for k in sorted(holders):
        print(f"  {k}: {sorted(holders[k])}")
    print("\nGO:0050421 (NO-forming child) holders among these globins:",
          {a: data[a]['GO:0050421'] for a, _ in GLOBINS if data[a]['GO:0050421']} or "NONE")
    if problems:
        print("\nCLAIM CHECK FAILED:")
        for p in problems:
            print("  -", p)
        sys.exit(1)
    print("\nAll three review claims verified against QuickGO.")

    if args.check_notes:
        # Compare EVERY line, not just one row.  The first version checked only
        # table.split("\n")[2] - the neuroglobin row - leaving three of four data
        # rows unguarded, i.e. a check whose scope was narrower than the claim it
        # was protecting.  A detector and the thing it guards must agree on scope
        # or the verification is structurally blind.
        notes = (Path(__file__).resolve().parent.parent / "ADGB-notes.md").read_text()
        lines = table.split("\n")
        compared = [ln for ln in lines if ln.strip()]
        missing = [ln for ln in compared if ln not in notes]
        if missing:
            print(f"\nNOTES MISMATCH: {len(missing)} of {len(compared)} table lines are "
                  f"not in ADGB-notes.md - regenerate the table there.")
            for ln in missing:
                print("  missing:", ln)
            sys.exit(1)
        # ... and assert the check could actually have failed, so a table that
        # silently emptied cannot pass by having nothing to compare.
        data_rows = [ln for ln in lines if ln.startswith("| ") and "---" not in ln]
        if len(data_rows) != len(GLOBINS) + 1:
            print(f"\nFATAL: expected {len(GLOBINS) + 1} table lines (header + "
                  f"{len(GLOBINS)} globins), built {len(data_rows)} - the "
                  f"comparison would have been vacuous.")
            sys.exit(1)
        # Report the number actually compared, derived from the same list the
        # comparison used - never a neighbouring variable. `data_rows` counts
        # only header+globins and excludes the separator, so quoting it here
        # understated the check by one and is exactly the hand-written-label-
        # drifts-from-computed-value defect this campaign keeps hitting.
        print(f"Committed table in ADGB-notes.md matches a fresh query "
              f"({len(compared)} lines compared, all of them; "
              f"{len(data_rows)} of them data rows).")


if __name__ == "__main__":
    main()
