"""Fetch definitions, obsoletion status and secondaryIds for every GO term this
review leans on, and assert every ancestry claim rather than inferring one from a
label.

Rationale from the campaign brief: OLS reports a MERGED id and an ABSENT id
identically, `just validate` passing is not proof a term is current, and
"regulation of" / "activity vs binding" relations do not subsume. So each
load-bearing relation is fetched and asserted here.

Usage: uv run python terms.py
"""

from __future__ import annotations

import json
import pathlib
import sys

import quickgo

OUT = pathlib.Path(__file__).parent / "terms.json"

TERMS = [
    # on the gene now
    "GO:0005096",  # GTPase activator activity (IEA InterPro)
    "GO:0003723",  # RNA binding (TAS PINC)
    "GO:0005515",  # protein binding
    "GO:0005634",  # nucleus
    "GO:0005643",  # nuclear pore
    "GO:0005737",  # cytoplasm
    "GO:0005829",  # cytosol
    "GO:0031410",  # cytoplasmic vesicle
    "GO:0006406",  # mRNA export from nucleus
    "GO:0001675",  # acrosome assembly
    "GO:0007289",  # spermatid nucleus differentiation
    "GO:0045109",  # intermediate filament organization
    # candidate replacements / additions
    "GO:0140312",  # cargo adaptor activity
    "GO:0060090",  # molecular adaptor activity
    "GO:0030276",  # clathrin binding
    "GO:0072583",  # clathrin-dependent endocytosis
    "GO:0030136",  # clathrin-coated vesicle
    "GO:0005905",  # clathrin-coated pit
    "GO:0046784",  # viral mRNA export from host cell nucleus?
    "GO:0075733",  # intracellular transport of virus?
    "GO:0034399",  # nuclear periphery
    "GO:0005635",  # nuclear envelope
    "GO:0019068",  # virion assembly?
    "GO:0006886",  # intracellular protein transport
    "GO:0016192",  # vesicle-mediated transport
    "GO:0000045",  # autophagosome assembly (control: unrelated)
    "GO:0000149",  # SNARE binding
    "GO:0019905",  # syntaxin binding
    "GO:0035615",  # clathrin adaptor activity?
    "GO:0019080",  # viral gene expression
    "GO:0016032",  # viral process
    # Raised by the round-1 reviewer: is there an acrosome-associated CC or a more
    # specific BP for what the mouse null actually blocks?
    "GO:0001669",  # acrosomal vesicle
    "GO:0120211",  # proacrosomal vesicle fusion
    "GO:0140042",  # lipid droplet formation (control: unrelated)
]

# (child, ancestor) pairs the review's prose depends on. Checked by asking
# QuickGO whether `child` is returned when querying `ancestor` with
# goUsage=descendants over is_a,part_of only - regulation edges must NOT count.
ANCESTRY_CLAIMS = [
    ("GO:0140312", "GO:0060090"),  # cargo adaptor activity under molecular adaptor
    ("GO:0005643", "GO:0005635"),  # nuclear pore part_of nuclear envelope
    ("GO:0072583", "GO:0016192"),  # clathrin-dependent endocytosis under vesicle transport
    ("GO:0035615", "GO:0140312"),  # clathrin-cargo adaptor under cargo adaptor activity
    ("GO:0035615", "GO:0060090"),  # ... and therefore under molecular adaptor activity
    ("GO:0120211", "GO:0001675"),  # proacrosomal vesicle fusion under acrosome assembly
    # Negative controls: these must come back False, or the checker is vacuous.
    ("GO:0075733", "GO:0006406"),  # viral transport is NOT under mRNA export
    ("GO:0003723", "GO:0005515"),  # RNA binding is NOT under protein binding
]


def main() -> None:
    out = {}
    for t in TERMS:
        try:
            res = quickgo.term(t)
        except AssertionError as exc:
            out[t] = {"error": str(exc)}
            print(f"{t}: {exc}")
            continue
        out[t] = {
            "name": res["name"],
            "aspect": res.get("aspect"),
            "isObsolete": res.get("isObsolete"),
            "secondaryIds": res.get("secondaryIds"),
            "replacedBy": res.get("replacements"),
            "definition": (res.get("definition") or {}).get("text"),
        }
        obs = " *** OBSOLETE ***" if res.get("isObsolete") else ""
        sec = f" secondaryIds={res['secondaryIds']}" if res.get("secondaryIds") else ""
        print(f"\n{t} [{res.get('aspect')}] {res['name']}{obs}{sec}")
        print(f"    {(res.get('definition') or {}).get('text')}")

    print("\n=== ancestry claims (is_a/part_of only; regulation must NOT count) ===")
    checks = {}
    for child, ancestor in ANCESTRY_CLAIMS:
        desc = quickgo.descendants(ancestor)
        ok = child in desc
        checks[f"{child} under {ancestor}"] = ok
        print(f"  {child} is a descendant of {ancestor} (is_a/part_of): {ok}")
    out["_ancestry_claims"] = checks
    # A checker whose every expectation is True cannot distinguish a working
    # query from one that returns everything, so two claims above are negative
    # controls and are asserted to be False.
    assert checks["GO:0075733 under GO:0006406"] is False, (
        "negative control failed: the descendant query is not discriminating"
    )
    assert checks["GO:0003723 under GO:0005515"] is False, (
        "negative control failed: the descendant query is not discriminating"
    )
    negatives = {"GO:0075733 under GO:0006406", "GO:0003723 under GO:0005515"}
    positives = set(checks) - negatives
    for positive in sorted(positives):
        assert checks[positive] is True, f"expected ancestry claim failed: {positive}"
    # Counts derived, not hardcoded: a literal here goes stale the moment a claim
    # is added, and then reports coverage it does not have.
    print(
        f"\nancestry checks OK ({len(positives)} positive, {len(negatives)} negative "
        "controls)"
    )

    OUT.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(f"\nwrote {OUT}", file=sys.stderr)


if __name__ == "__main__":
    main()
