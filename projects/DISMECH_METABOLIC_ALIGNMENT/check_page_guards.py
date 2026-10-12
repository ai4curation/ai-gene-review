"""Run make_page.py against deliberately broken reports and check each guard fires.

Committed because the guard counts quoted in this project's history records were not
reproducible from the tree: a reader had only my word for "eighteen of twenty-one exit 1",
and the figures did not reconcile across rounds. This script is the harness those counts
came from, so the claim is now checkable rather than asserted - the same move this project
made for the branch-local comparison, the aspect figures and the module-flag reasons.

    just check-alignment-page-guards
    just check-alignment-page-guards --case coverage

`tests/test_dismech_alignment_page_guards.py` runs it under pytest, so a regression in any
of the refusals fails the suite rather than waiting for someone to type the command.

Each case copies the two committed reports, breaks one thing, and renders. A case marked
EXIT must make the generator refuse **with the message it declares**, so that another
guard firing does not pass it; a case marked OK must still render **and contain the clause
it declares**, because those cases exist to prove a branch renders and would otherwise
pass with that branch deleted. Exit status is 0 only if every case behaves as declared.

`--case <substring>` runs the matching cases only, since each render reads the full
183-row reports.
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


# (name, expectation, mutation, expect) where `expect` is a substring the refusal message
# must contain, or - for an OK case - a substring the rendered page must contain. Exit status
# alone was not enough: an EXIT case passed when *any* guard fired rather than the declared
# one, and an OK case passed whenever the generator exited 0, whether or not the branch under
# test was taken. The three OK cases exist to prove a clause renders, so without a string to
# look for they would still have passed with that clause deleted.
CASES = [
    # Deliberately NOT the drift clause: that sentence depends on whether this checkout
    # holds the second run's recorded revision, which CI's `fetch-depth: 1` guarantees it
    # does not. Declaring it made the suite's green depend on clone depth. The flag-count
    # line is derived from the reports alone.
    ("untampered", "OK", lambda p, a: None,
     "Flag counts on principal rows:"),
    ("audit_sha256 differs", "EXIT",
     lambda p, a: a["provenance"].update(audit_sha256="deadbeefdead"),
     "produced by different align_audit.py versions"),
    ("row counts differ", "EXIT", lambda p, a: a.__setitem__("entries", a["entries"][:-1]),
     "report row counts differ"),
    ("review-independent flag moves", "EXIT",
     lambda p, a: _drop_flag(a, "GENE_ON_NO_NODE"),
     "flags that do not read a gene review differ"),
    ("review_independent_flags absent", "EXIT",
     lambda p, a: a.pop("review_independent_flags", None),
     "no review_independent_flags"),
    ("flag_groups absent", "EXIT", lambda p, a: a.pop("flag_groups", None),
     "has no flag_groups"),
    ("flag_groups empty", "EXIT", lambda p, a: a.__setitem__("flag_groups", {}),
     "flag_groups is empty"),
    ("module_sourced_reason_required absent", "EXIT",
     lambda p, a: p["flag_groups"].pop("module_sourced_reason_required", None),
     "no module_sourced_reason_required flag group"),
    ("soft group absent", "EXIT", lambda p, a: p["flag_groups"].pop("soft", None),
     "no soft flag group"),
    ("soft group loses a flag the prose names", "EXIT",
     lambda p, a: p["flag_groups"].__setitem__(
         "soft", [f for f in p["flag_groups"]["soft"] if f != "ALIGNED_NONCORE"]),
     "soft flag group omits ALIGNED_NONCORE"),
    ("term_aspects absent from the primary report", "EXIT",
     lambda p, a: p.pop("term_aspects", None),
     "no term_aspects key at all"),
    ("term_aspects absent from the second report", "EXIT",
     lambda p, a: a.pop("term_aspects", None),
     "second report has no term_aspects"),
    ("term_aspects empty in both", "OK",
     lambda p, a: (p.__setitem__("term_aspects", {}), a.__setitem__("term_aspects", {})),
     "no matched pair crosses the aspects"),
    ("aspect_unresolved absent", "EXIT",
     lambda p, a: p["provenance"].pop("aspect_unresolved", None),
     "no aspect_unresolved key"),
    ("aspect_unresolved non-empty", "OK",
     lambda p, a: p["provenance"].__setitem__("aspect_unresolved", ["GO:0000001"]),
     "sit under no single aspect root"),
    # Distinct invented names, so the assertion shows which report's injection fired: the
    # guard reads the union of both reports' flags, and one string could not tell the two
    # cases apart - which is the split they exist to prove.
    ("a flag with no glossary entry, primary", "EXIT",
     lambda p, a: p["entries"][0]["genes"][0]["flags"].append("INVENTED_IN_PRIMARY"),
     "no entry in FLAG_GLOSS: INVENTED_IN_PRIMARY"),
    ("a flag with no glossary entry, second", "EXIT",
     lambda p, a: a["entries"][0]["genes"][0]["flags"].append("INVENTED_IN_SECOND"),
     "no entry in FLAG_GLOSS: INVENTED_IN_SECOND"),
    ("a principal module flag with no stated reason", "EXIT",
     lambda p, a: _add_flag_to_principal(p, "MODULE_NOT_COVERING"),
     "MODULE_REASONS has no entry for principal rows"),
    ("two rows for one gene in one entry", "EXIT",
     lambda p, a: [d["entries"][0]["genes"].append(copy.deepcopy(d["entries"][0]["genes"][0]))
                   for d in (p, a)],
     "hold more than one row inside one entry"),
    ("coverage shown for some of its group", "EXIT",
     lambda p, a: [_strip_cover(d, {"COQ8A"}) for d in (p, a)],
     "cover_evidence shows 1 of 2 rows"),
    ("coverage shown for none of its group", "EXIT",
     lambda p, a: [_strip_cover(d, {"COQ8A", "HAO1", "TMEM70"}) for d in (p, a)],
     "cover_evidence shows 0 of 1 rows"),
    # Mutates the prose, not the revision, so the case exercises the regex that reads shas
    # out of aigr_tree as well as the comparison. The sha injected is well-formed and names
    # nothing the report records.
    ("aigr_tree prose names no revision the report records", "EXIT",
     lambda p, a: p["provenance"].update(
         aigr_tree="origin/main at 1234abc with the slices merged (merge commit 9f8e7d6c5)"),
     "but not the revision it records"),
]


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    only = None
    # Fails on a bare --case and on anything unrecognised, rather than ignoring it and
    # reporting success over every case as though it had filtered.
    while argv:
        arg = argv.pop(0)
        if arg == "--case":
            if not argv:
                sys.exit("--case needs a substring; names are:\n  "
                         + "\n  ".join(c[0] for c in CASES))
            only = argv.pop(0)
        else:
            sys.exit(f"unrecognised argument {arg!r}; the only option is --case <substring>")
    # The counts are printed at the end from CASES, never written down here: an earlier
    # comment in this file quoted "21 cases" and went stale in the round that added one.
    cases = [c for c in CASES if only is None or only.lower() in c[0].lower()]
    if not cases:
        sys.exit(f"no case matches {only!r}; names are:\n  "
                 + "\n  ".join(c[0] for c in CASES))
    primary = yaml.safe_load(open(PRIMARY))
    alt = yaml.safe_load(open(ALT))
    bad = 0
    with tempfile.TemporaryDirectory() as tmp:
        pp0, ap0 = os.path.join(tmp, "p.yaml"), os.path.join(tmp, "a.yaml")
        yaml.safe_dump(primary, open(pp0, "w"), sort_keys=False)
        yaml.safe_dump(alt, open(ap0, "w"), sort_keys=False)
        on_disk_mutated = {pp0: False, ap0: False}
        for name, want, mutate, expect in cases:
            p, a = copy.deepcopy(primary), copy.deepcopy(alt)
            mutate(p, a)
            pp, ap = os.path.join(tmp, "p.yaml"), os.path.join(tmp, "a.yaml")
            # Removed between cases so a previous render cannot satisfy this case's clause.
            out_md = os.path.join(tmp, "out.md")
            if os.path.exists(out_md):
                os.remove(out_md)
            # Each report is ~100 KB of YAML and most cases mutate one of the two, so a
            # report is re-dumped only when this case mutated it, or when the previous case
            # left a mutation on disk. Skipping that second condition silently reused the
            # previous case's mutation and failed three cases.
            #
            # The comparison is cheaper than the dump it avoids by three orders of
            # magnitude - measured at 0.1 ms against 147.6 ms for these reports - and it is
            # derived from the mutation rather than declared beside it, so it cannot drift
            # from what a case actually does.
            for obj, path, pristine in ((p, pp, primary), (a, ap, alt)):
                mutated = obj != pristine
                if mutated or on_disk_mutated[path]:
                    yaml.safe_dump(obj, open(path, "w"), sort_keys=False)
                on_disk_mutated[path] = mutated
            r = subprocess.run([sys.executable, GEN, pp, out_md, ap],
                               capture_output=True, text=True)
            got = "EXIT" if r.returncode else "OK"
            # Exit status is necessary and not sufficient. A refusal must carry the declared
            # message, or any other guard firing would pass the case; a render must contain
            # the declared clause, or deleting the branch under test would pass it.
            where = (r.stdout + r.stderr) if got == "EXIT" else (
                open(out_md).read() if os.path.exists(out_md) else "")
            why = "" if got == want else f"wanted {want}, got {got}"
            if not why and expect not in where:
                why = (f"{'refusal message' if got == 'EXIT' else 'rendered page'} does not"
                       f" contain {expect!r}")
            bad += bool(why)
            print(f"{'ok  ' if not why else 'FAIL'} {name}" + (f": {why}" if why else ""))
    n_exit = sum(1 for c in cases if c[1] == "EXIT")
    print(f"\n{len(cases)} cases: {n_exit} must refuse, {len(cases) - n_exit} must render;"
          " each checked for exit status and for the message or clause it declares.")
    if bad:
        sys.exit(f"{bad} case(s) did not behave as declared")
    print("every guard behaved as declared")


if __name__ == "__main__":
    main()
