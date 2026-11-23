"""Native representative-capacity cases using the production module compiler.

Presence means the curated molecular role is available; it does not predict growth,
ligand concentration, transport flux or the presence of unreviewed partners.
"""

from pathlib import Path
import yaml
from ai_gene_review.module_logic import compile_node, is_satisfied

ROOT = Path(__file__).resolve().parents[2]
SLUG = "bacterial_c_di_amp_signaling"
DATA = ROOT / "analysis/module_audits" / SLUG


def walk(x):
    if isinstance(x, dict):
        yield x
        for v in x.values():
            yield from walk(v)
    elif isinstance(x, list):
        for v in x:
            yield from walk(v)


def main():
    d = yaml.safe_load((ROOT / "modules" / (SLUG + ".yaml")).read_text())
    m = d["module"]
    panel = yaml.safe_load((DATA / "members.yaml").read_text())
    node = {n["id"]: n for n in walk(m) if n.get("id")}
    acts = {a["id"]: a for n in walk(m) for a in n.get("annotons", [])}
    reps = {
        k: {
            n["id"].split(":", 1)[1]
            for n in walk(a["participant"])
            if str(n.get("id", "")).startswith("UniProtKB:")
        }
        for k, a in acts.items()
    }
    native = {
        org: {r["accession"] for r in panel if r["organism"] == org}
        for org in {r["organism"] for r in panel}
    }
    access = {(r["organism"], r["gene"]): r["accession"] for r in panel}
    cases = []

    def check(name, target, org, present, expected):
        def holds(atom):
            return bool(reps[atom.node_id] & present & native[org])

        actual = is_satisfied(compile_node(node[target]), holds)
        assert actual == expected, (name, expected, actual)
        cases.append(
            {
                "case": name,
                "node": target,
                "strain_code": org,
                "present": sorted(present),
                "expected": expected,
                "observed": actual,
            }
        )

    check("Empty inventory", SLUG, "BACSU", set(), False)
    for org in sorted(native):
        check(
            "Scoped native representative panel " + org,
            SLUG,
            org,
            native[org],
            org in ["BACSU", "STAA8"],
        )
    for r in panel:
        check(
            "Single protein does not constitute motif "
            + r["organism"]
            + "/"
            + r["gene"],
            SLUG,
            r["organism"],
            {r["accession"]},
            False,
        )
    sa = native["STAA8"]
    for g in ["dacA", "gdpP"]:
        check("STAA8 loss of " + g, SLUG, "STAA8", sa - {access["STAA8", g]}, False)
    check(
        "STAA8 loss of KdpD retains PstA binding capacity",
        SLUG,
        "STAA8",
        sa - {access["STAA8", "kdpD"]},
        True,
    )
    check(
        "STAA8 loss of both sampled receptors",
        SLUG,
        "STAA8",
        sa - {access["STAA8", "kdpD"], access["STAA8", "pstA"]},
        False,
    )
    bs = native["BACSU"]
    for g in ["cdaA", "disA"]:
        check(
            "BACSU cyclase redundancy " + g,
            SLUG,
            "BACSU",
            bs - {access["BACSU", g]},
            True,
        )
    check(
        "BACSU loss of both cyclases",
        SLUG,
        "BACSU",
        bs - {access["BACSU", "cdaA"], access["BACSU", "disA"]},
        False,
    )
    check(
        "BACSU loss of sole sampled opener",
        SLUG,
        "BACSU",
        bs - {access["BACSU", "gdpP"]},
        False,
    )
    check(
        "S. aureus Pde2 does not replace a messenger opener",
        "c_di_amp_hydrolysis",
        "STAA3",
        {access["STAA3", "pde2"]},
        False,
    )
    check(
        "Pde2 supplies the optional linear-substrate step",
        "papa_clearance",
        "STAA3",
        {access["STAA3", "pde2"]},
        True,
    )
    check(
        "A receptor alone provides reception capacity",
        "c_di_amp_reception",
        "BACSU",
        {access["BACSU", "darB"]},
        True,
    )
    check(
        "A receptor does not supply synthesis",
        "c_di_amp_synthesis",
        "BACSU",
        {access["BACSU", "darB"]},
        False,
    )
    check(
        "Do not pool different strain panels",
        SLUG,
        "STAA3",
        sa | native["STAA3"],
        False,
    )
    # Localization and feedback boundaries must remain structural rather than prose-only.
    assert acts["cdaa_cyclase_activity"]["locations"][0]["term"]["id"] == "GO:0005886"
    assert acts["disa_cyclase_activity"]["locations"][0]["term"]["id"] == "GO:0005737"
    feedback = [e for e in m["connections"] if e["source"] == "papa_clearance"]
    assert len(feedback) == 1 and feedback[0]["target"] == "gdpp_phosphodiesterase"
    assert (
        next(p for p in m["parts"] if p["node"]["id"] == "papa_clearance")["optional"]
        is True
    )
    out = {
        "passed": len(cases),
        "interpretation": "Curated molecular-role capacity only; no growth or flux prediction. Native strain codes are not pooled. Incomplete panels are not evidence of biological absence.",
        "cases": cases,
    }
    (DATA / "capacity-results.yaml").write_text(yaml.safe_dump(out, sort_keys=False))
    print("PASS", len(cases), "capacity cases")


if __name__ == "__main__":
    main()
