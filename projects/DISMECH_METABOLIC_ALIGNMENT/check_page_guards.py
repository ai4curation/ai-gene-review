"""Run make_page.py against deliberately broken reports and check each guard fires.

Committed because the guard counts quoted in this project's history records were not
reproducible from the tree: a reader had only my word for "eighteen of twenty-one exit 1",
and the figures did not reconcile across rounds. This script is the harness those counts
came from, so the claim is now checkable rather than asserted - the same move this project
made for the branch-local comparison, the aspect figures and the module-flag reasons.

    uv run python projects/DISMECH_METABOLIC_ALIGNMENT/check_page_guards.py

Each case copies the two committed reports, breaks one thing, and renders. A case marked
EXIT must make the generator refuse; a case marked OK must still render, because the
branch it exercises is a legitimate state rather than a defect. Exit status is 0 only if
every case behaves as declared.
"""
import copy
import os
import subprocess
import sys
import tempfile

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
PRIMARY = os.path.join(HERE, "report.yaml")
ALT = os.path.join(HERE, "report-branch-local.yaml")
GEN = os.path.join(HERE, "make_page.py")


def _drop_flag(rep, flag):
    for e in rep["entries"]:
        for g in e.get("genes") or []:
            if flag in (g.get("flags") or ()):
                g["flags"].remove(flag)
                return


def _add_flag_to_principal(rep, flag):
    for e in rep["entries"]:
        for g in e.get("genes") or []:
            if g.get("relationship") == "CAUSATIVE" and flag not in (g.get("flags") or ()):
                g.setdefault("flags", []).append(flag)
                g.setdefault("modules", ["x"])
                return


def _strip_cover(rep, genes):
    for e in rep["entries"]:
        for g in e.get("genes") or []:
            if g.get("gene") in genes:
                g["covering_pairs"] = None


# (name, expectation, mutation). "EXIT" means the generator must refuse.
CASES = [
    ("untampered", "OK", lambda p, a: None),
    ("audit_sha256 differs", "EXIT",
     lambda p, a: a["provenance"].update(audit_sha256="deadbeefdead")),
    ("row counts differ", "EXIT", lambda p, a: a.__setitem__("entries", a["entries"][:-1])),
    ("review-independent flag moves", "EXIT",
     lambda p, a: _drop_flag(a, "GENE_ON_NO_NODE")),
    ("review_independent_flags absent", "EXIT",
     lambda p, a: a.pop("review_independent_flags", None)),
    ("flag_groups absent", "EXIT", lambda p, a: a.pop("flag_groups", None)),
    ("flag_groups empty", "EXIT", lambda p, a: a.__setitem__("flag_groups", {})),
    ("module_sourced_reason_required absent", "EXIT",
     lambda p, a: p["flag_groups"].pop("module_sourced_reason_required", None)),
    ("soft group absent", "EXIT", lambda p, a: p["flag_groups"].pop("soft", None)),
    ("soft group loses a flag the prose names", "EXIT",
     lambda p, a: p["flag_groups"].__setitem__(
         "soft", [f for f in p["flag_groups"]["soft"] if f != "ALIGNED_NONCORE"])),
    ("term_aspects absent from the primary report", "EXIT",
     lambda p, a: p.pop("term_aspects", None)),
    ("term_aspects absent from the second report", "EXIT",
     lambda p, a: a.pop("term_aspects", None)),
    ("term_aspects empty in both", "OK",
     lambda p, a: (p.__setitem__("term_aspects", {}), a.__setitem__("term_aspects", {}))),
    ("aspect_unresolved absent", "EXIT",
     lambda p, a: p["provenance"].pop("aspect_unresolved", None)),
    ("aspect_unresolved non-empty", "OK",
     lambda p, a: p["provenance"].__setitem__("aspect_unresolved", ["GO:0000001"])),
    ("a flag with no glossary entry, primary", "EXIT",
     lambda p, a: p["entries"][0]["genes"][0]["flags"].append("NEWLY_INVENTED_FLAG")),
    ("a flag with no glossary entry, second", "EXIT",
     lambda p, a: a["entries"][0]["genes"][0]["flags"].append("NEWLY_INVENTED_FLAG")),
    ("a principal module flag with no stated reason", "EXIT",
     lambda p, a: _add_flag_to_principal(p, "MODULE_NOT_COVERING")),
    ("two rows for one gene in one entry", "EXIT",
     lambda p, a: [d["entries"][0]["genes"].append(copy.deepcopy(d["entries"][0]["genes"][0]))
                   for d in (p, a)]),
    ("coverage shown for some of its group", "EXIT",
     lambda p, a: [_strip_cover(d, {"COQ8A"}) for d in (p, a)]),
    ("coverage shown for none of its group", "EXIT",
     lambda p, a: [_strip_cover(d, {"COQ8A", "HAO1", "TMEM70"}) for d in (p, a)]),
]


def main():
    primary = yaml.safe_load(open(PRIMARY))
    alt = yaml.safe_load(open(ALT))
    bad = 0
    with tempfile.TemporaryDirectory() as tmp:
        for name, want, mutate in CASES:
            p, a = copy.deepcopy(primary), copy.deepcopy(alt)
            mutate(p, a)
            pp, ap = os.path.join(tmp, "p.yaml"), os.path.join(tmp, "a.yaml")
            yaml.safe_dump(p, open(pp, "w"), sort_keys=False)
            yaml.safe_dump(a, open(ap, "w"), sort_keys=False)
            r = subprocess.run([sys.executable, GEN, pp, os.path.join(tmp, "out.md"), ap],
                               capture_output=True, text=True)
            got = "EXIT" if r.returncode else "OK"
            ok = got == want
            bad += not ok
            why = (r.stdout + r.stderr).strip().splitlines()
            print(f"{'ok  ' if ok else 'FAIL'} {name}: wanted {want}, got {got}"
                  + (f" - {why[-1][:90]}" if why and got == "EXIT" else ""))
    n_exit = sum(1 for _, w, _ in CASES if w == "EXIT")
    print(f"\n{len(CASES)} cases: {n_exit} must refuse, {len(CASES) - n_exit} must render.")
    if bad:
        sys.exit(f"{bad} case(s) did not behave as declared")
    print("every guard behaved as declared")


if __name__ == "__main__":
    main()
