#!/usr/bin/env python3
"""Does every partner retyped to GO:0030165 actually carry a PDZ domain?

The review converts 42 of ARHGEF16's 57 ``GO:0005515 protein binding`` rows to
``GO:0030165 PDZ domain binding``, on the argument that they all report one
binding determinant -- ARHGEF16's C-terminal ``...ETDV`` motif (UniProt ``MOTIF
707-709``) -- engaging the PDZ domain of the partner.  That argument is a
testable proposition about 42 UniProt records, so it is tested here rather than
asserted.

The script reads the **committed review** rather than a hardcoded list, so it
cannot drift away from the document it defends: if a row is added to or removed
from the ``GO:0030165`` set, the check follows.  For every partner named in a
retyped row it asks UniProt whether the entry carries a PDZ domain, and it fails
if any does not.

Two guards, because "they all have PDZ domains" is only half the claim:

* every partner of a **retyped** row must have a PDZ domain -- otherwise the
  replacement term is wrong for that row;
* every partner of a row **not** retyped to that term must NOT have one --
  otherwise the review retyped inconsistently and left PDZ partners behind. That
  bucket holds both the rows kept as generic ``protein binding`` and the seven
  retyped to ``GO:0071889 14-3-3 protein binding``, which makes it a slightly
  stronger control: the 14-3-3 partners had to be excluded on domain content
  rather than merely overlooked.

The second is the negative control, and it is the one that would catch a lazy
"retype everything from the big screen" rule.  The target's own PDZ-binding motif
is also verified from its UniProt features, since the whole argument rests on it.

Run:    uv run --with requests python pdz_partner_check.py
        uv run --with requests python pdz_partner_check.py --self-test
Writes: pdz_partner_check.json
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import requests
import yaml

UNIPROT = "https://rest.uniprot.org/uniprotkb/{acc}.json"
TIMEOUT = 120

TARGET = "Q5VV41"
RETYPE_TERM = "GO:0030165"
GENERIC_TERM = "GO:0005515"


def repo_root() -> Path:
    p = Path(__file__).resolve()
    for parent in p.parents:
        if (parent / "genes").is_dir() and (parent / "publications").is_dir():
            return parent
    raise RuntimeError("could not locate the repository root above this script")


def review_path() -> Path:
    return repo_root() / "genes/human/ARHGEF16/ARHGEF16-ai-review.yaml"


def partition(doc: dict) -> tuple[dict[str, list[str]], dict[str, list[str]]]:
    """Split the generic protein-binding rows by whether they were retyped to PDZ.

    Returns ``(retyped, not_retyped)`` as accession -> list of citing references.
    ``not_retyped`` holds everything else, including the rows retyped to
    ``GO:0071889``, so the negative control covers those partners too.
    """
    retyped: dict[str, list[str]] = {}
    kept: dict[str, list[str]] = {}
    for a in doc.get("existing_annotations") or []:
        if a.get("term", {}).get("id") != GENERIC_TERM:
            continue
        review = a.get("review") or {}
        repl = {t.get("id") for t in (review.get("proposed_replacement_terms") or [])}
        accs = [
            s.split(":", 1)[1].split("-")[0]
            for s in (a.get("supporting_entities") or [])
            if s.startswith("UniProtKB:")
        ]
        bucket = retyped if RETYPE_TERM in repl else kept
        for acc in accs:
            bucket.setdefault(acc, []).append(a.get("original_reference_id", "?"))
    return retyped, kept


def has_pdz(acc: str) -> dict[str, object]:
    r = requests.get(UNIPROT.format(acc=acc), timeout=TIMEOUT)
    r.raise_for_status()
    e = r.json()
    doms = [
        f.get("description", "").strip()
        for f in e.get("features", [])
        if f["type"] == "Domain"
    ]
    pdz = [d for d in doms if d == "PDZ" or d.startswith("PDZ ")]
    return {
        "symbol": (e.get("genes") or [{}])[0].get("geneName", {}).get("value"),
        "domains": doms,
        "n_pdz": len(pdz),
        "has_pdz": bool(pdz),
    }


def target_motif() -> dict[str, object]:
    r = requests.get(UNIPROT.format(acc=TARGET), timeout=TIMEOUT)
    r.raise_for_status()
    e = r.json()
    seq = e["sequence"]["value"]
    motifs = [
        (f["location"]["start"]["value"], f["location"]["end"]["value"], f.get("description", ""))
        for f in e.get("features", [])
        if f["type"] == "Motif"
    ]
    pdz_motifs = [m for m in motifs if "PDZ" in m[2]]
    return {
        "accession": TARGET,
        "length": len(seq),
        "c_terminal_residues": seq[-4:],
        "pdz_binding_motifs": pdz_motifs,
        "motif_is_c_terminal": bool(pdz_motifs and pdz_motifs[0][1] == len(seq)),
    }


def run() -> dict[str, object]:
    doc = yaml.safe_load(review_path().read_text())
    retyped, kept = partition(doc)
    if not retyped:
        raise RuntimeError(f"no rows retyped to {RETYPE_TERM}; the review changed shape")
    if not kept:
        raise RuntimeError("no non-PDZ rows left; the negative control has no members")

    motif = target_motif()
    if not motif["motif_is_c_terminal"]:
        raise RuntimeError(
            f"{TARGET} has no C-terminal PDZ-binding motif in UniProt; "
            "the whole argument for retyping rests on it"
        )

    seen: dict[str, dict[str, object]] = {}
    for acc in sorted(set(retyped) | set(kept)):
        seen[acc] = has_pdz(acc)

    failures: list[str] = []
    for acc, refs in sorted(retyped.items()):
        if not seen[acc]["has_pdz"]:
            failures.append(
                f"retyped to {RETYPE_TERM} but no PDZ domain: {seen[acc]['symbol']} "
                f"({acc}) from {sorted(set(refs))}"
            )
    for acc, refs in sorted(kept.items()):
        if seen[acc]["has_pdz"]:
            failures.append(
                f"not retyped to {RETYPE_TERM} but HAS a PDZ domain: "
                f"{seen[acc]['symbol']} ({acc}) from {sorted(set(refs))}"
            )
    if failures:
        raise RuntimeError("partition failure:\n  " + "\n  ".join(failures))

    return {
        "target_motif": motif,
        "n_rows_retyped": sum(len(v) for v in retyped.values()),
        "n_partners_retyped": len(retyped),
        "n_rows_not_retyped_to_pdz": sum(len(v) for v in kept.values()),
        "n_partners_not_retyped_to_pdz": len(kept),
        "retyped_partners": {
            acc: {**seen[acc], "references": sorted(set(refs))} for acc, refs in sorted(retyped.items())
        },
        "partners_not_retyped_to_pdz": {
            acc: {**seen[acc], "references": sorted(set(refs))} for acc, refs in sorted(kept.items())
        },
        "verdict": {
            "every_retyped_partner_has_a_pdz_domain": True,
            "no_partner_outside_the_retyped_set_has_a_pdz_domain": True,
            "total_pdz_domains_across_retyped_partners": sum(
                int(seen[a]["n_pdz"]) for a in retyped
            ),
        },
    }


def self_test() -> int:
    checks: list[tuple[str, str]] = []
    doc = yaml.safe_load(review_path().read_text())
    retyped, kept = partition(doc)

    checks.append(
        ("partition finds both classes",
         "PASS" if retyped and kept else f"FAIL {len(retyped)}/{len(kept)}")
    )

    # 1. POSITIVE: a canonical PDZ scaffold must be detected.
    d = has_pdz("Q14160")  # SCRIB
    checks.append(("SCRIB detected as a PDZ protein",
                   "PASS" if d["has_pdz"] and d["n_pdz"] >= 4 else f"FAIL {d}"))

    # 2. NEGATIVE CONTROL: a protein with no PDZ domain must not be detected as
    #    one. Without this, a detector that always says yes would pass check 1.
    d = has_pdz("P31943")  # HNRNPH1, RRM domains only
    checks.append(("HNRNPH1 not detected as a PDZ protein",
                   "PASS" if not d["has_pdz"] else f"FAIL {d}"))

    # 3. The detector must not be fooled by a substring: PDZD7 is named for PDZ
    #    and does carry the domain, while PDZRN4's name also contains PDZ.
    #    Both should be positive, but for the domain, not the name.
    d = has_pdz("Q9H5P4")
    checks.append(("PDZD7 positive on domain content, not on its name",
                   "PASS" if d["has_pdz"] else f"FAIL {d}"))

    # 4. Injecting a non-PDZ partner into the retyped set must abort the run.
    real = globals()["partition"]
    try:
        globals()["partition"] = lambda _doc: (
            {**real(_doc)[0], "P31943": ["PMID:0"]},
            real(_doc)[1],
        )
        run()
        checks.append(("non-PDZ partner in the retyped set aborts", "FAIL (no exception)"))
    except RuntimeError as e:
        checks.append(("non-PDZ partner in the retyped set aborts",
                       "PASS" if "no PDZ domain" in str(e) else f"FAIL {e}"))
    finally:
        globals()["partition"] = real

    # 5. Injecting a PDZ partner into the non-retyped set must abort too --
    #    the guard has to work in both directions.
    try:
        globals()["partition"] = lambda _doc: (
            real(_doc)[0],
            {**real(_doc)[1], "Q14160": ["PMID:0"]},
        )
        run()
        checks.append(("PDZ partner outside the retyped set aborts", "FAIL (no exception)"))
    except RuntimeError as e:
        checks.append(("PDZ partner outside the retyped set aborts",
                       "PASS" if "HAS a PDZ domain" in str(e) else f"FAIL {e}"))
    finally:
        globals()["partition"] = real

    # 6. NEGATIVE CONTROL for 4 and 5: untouched, the run must complete silently.
    try:
        run()
        checks.append(("the committed review passes unmodified", "PASS"))
    except RuntimeError as e:
        checks.append(("the committed review passes unmodified", f"FAIL {e}"))

    for name, verdict in checks:
        mark = verdict.split()[0]
        print(f"  [{mark}] {name}" + ("" if mark == "PASS" else f" -- {verdict}"))
    bad = [c for c in checks if not c[1].startswith("PASS")]
    print(f"\n{len(checks) - len(bad)}/{len(checks)} self-tests passed")
    return 1 if bad else 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    if args.self_test:
        return self_test()

    out = run()
    dest = Path(__file__).with_name("pdz_partner_check.json")
    dest.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")

    m = out["target_motif"]
    print(f"{TARGET} is {m['length']} aa, ends ...{m['c_terminal_residues']}, "
          f"PDZ-binding motif {m['pdz_binding_motifs']}")
    print(f"\nretyped to {RETYPE_TERM}: {out['n_rows_retyped']} rows over "
          f"{out['n_partners_retyped']} partners")
    for acc, d in out["retyped_partners"].items():
        print(f"  {d['symbol']:<12} {acc:<10} {d['n_pdz']} PDZ  {','.join(d['references'])}")
    print(f"\nnot retyped to {RETYPE_TERM}: {out['n_rows_not_retyped_to_pdz']} rows over "
          f"{out['n_partners_not_retyped_to_pdz']} partners "
          f"(generic {GENERIC_TERM} plus the 14-3-3 retypes)")
    for acc, d in out["partners_not_retyped_to_pdz"].items():
        print(f"  {d['symbol']:<12} {acc:<10} {d['n_pdz']} PDZ  domains={d['domains']}")
    v = out["verdict"]
    print(f"\n  every retyped partner has a PDZ domain: {v['every_retyped_partner_has_a_pdz_domain']}")
    print(f"  no partner outside that set has one:    {v['no_partner_outside_the_retyped_set_has_a_pdz_domain']}")
    print(f"  PDZ domains across retyped partners:    {v['total_pdz_domains_across_retyped_partners']}")
    print(f"\nwrote {dest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
