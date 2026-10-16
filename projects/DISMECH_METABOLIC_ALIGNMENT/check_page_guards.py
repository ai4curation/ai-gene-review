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
import shutil
import subprocess
import sys
import tempfile

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
PRIMARY = os.path.join(HERE, "report.yaml")
ALT = os.path.join(HERE, "report-branch-local.yaml")
GEN = os.path.join(HERE, "make_page.py")

# The second report's own recorded revision, short, read from the file rather than written
# here. Two cases quote the generator's sentence about it, and hardcoding the sha is what
# made them fail the moment that report was regenerated - the same staleness the prose
# examples were guarded against. Only the wording stays declared.
ALT_SHORT = (yaml.safe_load(open(ALT))["provenance"].get("aigr_revision") or "")[:9]


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


def _twin_group(rep, gene):
    """Duplicate the entry holding `gene` so its movement group holds two rows.

    The "shows N of M rows" guard needs a group with more than one row, and which
    rows share a cause is decided by how the flags move between the two reports, not
    by anything a case can set directly. The committed pair currently yields only
    one-row groups for "the same modules carry different terms", so the case builds
    the shape it is about instead of depending on a report pair that happens to have
    it - which is what went stale when the reports were regenerated.
    """
    for e in list(rep["entries"]):
        if any(g.get("gene") == gene for g in e.get("genes") or []):
            twin = copy.deepcopy(e)
            twin["entry"] = e["entry"] + "_TWIN"
            # The twin's own row shows no coverage difference, so the group shows one
            # of its two rows. Cleared here rather than by _strip_cover, which works on
            # a whole report and would clear the original too.
            for g in twin.get("genes") or []:
                if g.get("gene") == gene:
                    g["covering_pairs"] = None
            rep["entries"].append(twin)
            return twin
    raise SystemExit(f"_twin_group: no entry holds {gene}")


def _strip_cover(rep, genes):
    for e in rep["entries"]:
        for g in e.get("genes") or []:
            if g.get("gene") in genes:
                g["covering_pairs"] = None


# A sha no checkout holds, returned by the shim as what the recorded revision resolves to.
# Deliberately not `HEAD`: the generator compares the resolved sha with the branch tip, and
# the branch-tip return is a different sentence from the one these cases are about.
_SHIM_RESOLVED = "1234567890abcdef1234567890abcdef12345678"


def _git_shim(tmp, mode):
    """A `git` earlier on PATH that answers the four questions the drift sentence asks.

    `_rev_state` reaches `unknown` only when `for-each-ref` fails after the revision has
    already resolved, and `unpublished` only when it succeeds with no output. Neither is
    reachable by mutating a report, so both were verified with a shim that lived outside the
    tree - evidence from an apparatus no committed artifact recorded, which is the position
    a figure in this project's round-9 history record had to be corrected for. This builds
    the same apparatus from the harness, so the two sentences a reader never sees can be
    re-rendered by anyone running the suite.

    It stubs the drift answer as well as the publication lookup, which is what makes the
    cases independent of the checkout rather than merely independent of its depth. An
    earlier version intercepted `for-each-ref` alone and let the rest reach the real git, so
    the sentence it asserted required the *second report's recorded revision to resolve* -
    four commits back on this branch, and absent in the `fetch-depth: 1` clone CI tests in.
    There `rev-parse --verify` failed before the interception was ever reached, the absence
    sentence rendered instead, and both cases failed: the clone dependence round 16 removed
    from `untampered`, reintroduced one layer down. Stubbing all four also makes the
    rendered figure deterministic, so each clause can be declared as one whole string.

    What is asserted is therefore the generator's assembly of the sentence from git's
    answers, not git's answers themselves. The real answers are what the committed page is
    rendered from, and `untampered` covers that path.

    Fails loudly with git absent rather than skipping: a case that cannot run is not a case
    that passed. `rev-parse --git-dir` and `rev-parse HEAD` are delegated, so the render
    still has to be inside a repository - true of any checkout, however shallow.
    """
    real = shutil.which("git")
    if not real:
        sys.exit("the shim cases need git on PATH to delegate to; it is not there")
    d = os.path.join(tmp, f"shim-{mode}")
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "git"), "w") as fh:
        fh.write(
            "#!/bin/sh\n"
            # `rev-parse --verify <rev>^{commit}`, not the bare `rev-parse HEAD` or
            # `--git-dir` the generator also runs, which fall through to the real git.
            f'if [ "$1" = "rev-parse" ] && [ "$2" = "--verify" ]; then'
            f' echo {_SHIM_RESOLVED}; exit 0; fi\n'
            'case "$1" in\n'
            # `notanc` is the one mode where the revision is not in this branch's
            # history, which is what separates a genuinely unpublished revision from one
            # that is merely not pushed yet.
            f'  merge-base) exit {"1" if mode == "notanc" else "0"} ;;\n'
            '  diff) exit 0 ;;\n'                # with nothing changed between the two
            f'  for-each-ref) exit {"129" if mode == "fail" else "0"} ;;\n'
            'esac\n'
            f'exec {real} "$@"\n')
    os.chmod(os.path.join(d, "git"), 0o755)
    return d


# (name, expectation, mutation, expect[, shim]) where `expect` is a substring the refusal
# message must contain, or - for an OK case - a substring the rendered page must contain.
# The optional fifth element names a `_git_shim` mode, rendered with that shim first on
# PATH. Exit status alone was not enough: an EXIT case passed when *any* guard fired rather
# than the declared one, and an OK case passed whenever the generator exited 0, whether or
# not the branch under test was taken. The OK cases exist to prove a clause renders, so
# without a string to look for they would still have passed with that clause deleted.
CASES = [
    # Deliberately NOT the drift clause: for the *committed* revision that sentence depends
    # on whether this checkout holds it, which CI's `fetch-depth: 1` guarantees it does not,
    # so declaring it made the suite's green depend on clone depth. The flag-count line is
    # derived from the reports alone. The drift sentences are covered by the three cases at
    # the end of this list. Two inject a revision whose state is the same in any checkout
    # that is a git repository at all - absent everywhere, or unresolvable everywhere. The
    # other two stub git's four answers outright. So none of the four depends on the clone's
    # depth, which is what made the round-15 attempt wrong, and none depends on the
    # repository holding any particular commit, which is what a first version of the shim
    # cases did depend on. All four still need a repository: `_alt_drift_tail` returns early
    # when `rev-parse HEAD` fails, so a run from an export with no `.git` fails them.
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
    # The twin doubles the group; stripping the twin's coverage in both reports leaves
    # the original showing a difference and the twin showing none, which is the
    # shows-fewer-than-the-group shape.
    ("coverage shown for some of its group", "EXIT",
     lambda p, a: [_twin_group(d, "TMEM70") for d in (p, a)],
     "cover_evidence shows 1 of 2 rows"),
    ("coverage shown for none of its group", "EXIT",
     lambda p, a: [_strip_cover(d, {"COQ8A", "HAO1", "TMEM70"}) for d in (p, a)],
     "cover_evidence shows 0 of 1 rows"),
    # Mutates the prose, not the revision, so the case exercises the regex that reads shas
    # out of aigr_tree as well as the comparison. The sha injected is well-formed and names
    # nothing the report records.
    # Distinct expected strings for the two reports, as with the glossary cases: the check
    # is one function applied twice, and a shared substring could not tell a primary-only
    # version of it - which is what it was for a round - from one that reads both.
    ("aigr_tree prose names no revision the report records, primary", "EXIT",
     lambda p, a: p["provenance"].update(
         aigr_tree="origin/main at 1234abc with the slices merged (merge commit 9f8e7d6c5)"),
     "the primary report's tree description names"),
    ("aigr_tree prose names no revision the report records, second", "EXIT",
     lambda p, a: a["provenance"].update(
         aigr_tree="the branch at 1234abc rebased onto 9f8e7d6c5"),
     "the second report's tree description names"),
    # The drift sentences. Declared in full to the final period, because a double period
    # survived rounds 15, 16 and 17 there while every declared string in this file stopped
    # short of a sentence boundary - and because CI, at `fetch-depth: 1`, renders the
    # `not_here` branch on every run. The injected sha is well-formed and absent from every
    # checkout, so the clause does not depend on how deep this one is.
    #
    # Both declarations end with the newline, and that is the whole point of them: `expect`
    # is tested by containment, so a string ending "either." is satisfied by a page saying
    # "either.." - the one defect these two cases exist to catch. The tail is the end of its
    # line, so the newline anchors it.
    ("the second run's tree is absent from every checkout", "OK",
     lambda p, a: a["provenance"].update(
         aigr_revision="1234567890abcdef1234567890abcdef12345678",
         aigr_tree="a harness tree at 1234567890abcdef"),
     "which this checkout does not hold, so the input-drift comparison below was not made."
     " Whether that revision is published could not be determined here, and a shallow clone"
     " will not hold it either.\n"),
    # A recorded value git cannot resolve and that is not shaped like an object name.
    # `rev-parse` exits 128 for it just as for an absent sha, so the sentence claims only
    # what the shape establishes - an earlier version decided the state from the shape and
    # then described the decision as git's.
    ("the second run records a value git cannot resolve", "OK",
     lambda p, a: a["provenance"].update(aigr_revision="not-a-revision",
                                         aigr_tree="a harness tree naming no revision"),
     "which git cannot resolve to a commit here and which is not shaped like an object"
     " name, so the input-drift comparison below was not made.\n"),
    # The two states no mutation can reach, each declared whole - including the drift answer
    # ahead of the clause, which is the part that matters. The clause alone does not
    # distinguish the fixed code from the version that grouped `unknown` with `not_here`:
    # that version printed the same clause behind "does not hold" and never ran the
    # comparison. "an ancestor of the branch tip" is produced only on the fall-through path,
    # checked against both versions.
    ("for-each-ref fails after the revision resolves", "OK",
     lambda p, a: None,
     (f"That second run read a tree recorded at `{ALT_SHORT}`, an ancestor of the branch tip,",
      "Whether that revision is published could not be determined, so nothing is claimed"
      " about re-running this elsewhere.\n"),
     "fail"),
    # On no remote ref *and* in this branch's history, which is the ordinary state between
    # rendering a round and pushing it. The softer clause is the point: the flat one was
    # written into a published page moments before the push made it false.
    ("for-each-ref finds the revision on no remote ref, but this branch holds it", "OK",
     lambda p, a: None,
     (f"That second run read a tree recorded at `{ALT_SHORT}`, an ancestor of the branch tip,",
      "That revision is this branch's own history and not yet on a pushed ref, so a clone"
      " holds it once this branch is pushed.\n"),
     "empty"),
    # The flat unpublished clause, which only a revision outside this branch's history can
    # now reach. Without this the softer branch-held sentence would be the only one tested,
    # and the clause that says a clone cannot re-run the comparison would have no case.
    ("for-each-ref finds no remote ref and this branch does not hold it", "OK",
     lambda p, a: None,
     "That revision is on no pushed ref, so no clone holds it and this comparison cannot"
     " be re-run elsewhere.\n",
     "notanc"),
    # A recorded ref, with the committed tree description left alone - the description names
    # a sha, so before the guard learned to compare only a recorded sha this configuration
    # made the generator exit instead of rendering. The shim forces the rest, so what is
    # asserted is that the ref reaches a drift answer at all.
    ("the second run records a ref rather than a sha", "OK",
     lambda p, a: a["provenance"].update(aigr_revision="HEAD~3"),
     ("That second run read a tree recorded at `HEAD~3`, an ancestor of the branch tip,",
      "That revision is this branch's own history and not yet on a pushed ref, so a clone"
      " holds it once this branch is pushed.\n"),
     "empty"),
    # An object this checkout holds that is not a commit. `rev-parse --verify <sha>^{commit}`
    # fails for it exactly as for an absent object, and the reason reached only stderr, so it
    # rendered as "this checkout does not hold" - false of the one case git can name exactly.
    # `HEAD^{tree}` rather than a named blob: a tree object exists wherever HEAD resolves,
    # at any clone depth and whatever the repository contains, so the case does not depend on
    # some particular file being there. The sha is read at render time, so the declaration
    # omits it and names the type instead.
    ("the second run records an object that is not a commit", "OK",
     lambda p, a: a["provenance"].update(
         aigr_revision=subprocess.run(["git", "rev-parse", "HEAD^{tree}"], cwd=HERE,
                                      capture_output=True, text=True).stdout.strip(),
         aigr_tree="a harness tree"),
     "which this checkout holds as a tree rather than a commit, so the input-drift comparison"
     " below was not made. Whether anything published names it could not be determined, since"
     " it is not a commit.\n"),
    # A value of a-f characters only, which is both a plausible ref name and sha-shaped by
    # length. Without the digit requirement this reads as an object the checkout lacks.
    ("the second run records an a-to-f word", "OK",
     lambda p, a: a["provenance"].update(aigr_revision="defaced",
                                         aigr_tree="a harness tree"),
     "at `defaced`, which git cannot resolve to a commit here and which is not shaped like an"
     " object name, so the input-drift comparison below was not made.\n"),
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
        for case in cases:
            name, want, mutate, expect = case[:4]
            shim = case[4] if len(case) > 4 else None
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
            env = dict(os.environ)
            if shim:
                env["PATH"] = _git_shim(tmp, shim) + os.pathsep + env.get("PATH", "")
            r = subprocess.run([sys.executable, GEN, pp, out_md, ap],
                               capture_output=True, text=True, env=env)
            got = "EXIT" if r.returncode else "OK"
            # Exit status is necessary and not sufficient. A refusal must carry the declared
            # message, or any other guard firing would pass the case; a render must contain
            # the declared clause, or deleting the branch under test would pass it.
            # A render now writes two files: the page, and the audit self-check page beside
            # it carrying the two-run comparison. Both are the generator's rendered output,
            # so a declared clause is looked for in either - checking only the page made
            # every comparison case fail when that section moved to its own file.
            _sub = os.path.join(os.path.dirname(os.path.abspath(out_md)),
                                "DISMECH_METABOLIC_ALIGNMENT", "audit-self-check.md")
            where = (r.stdout + r.stderr) if got == "EXIT" else "".join(
                open(f).read() for f in (out_md, _sub) if os.path.exists(f))
            why = "" if got == want else f"wanted {want}, got {got}"
            # A case may declare several fragments, all of which must appear. One
            # contiguous span would have to include whatever sits between them, and in
            # the drift sentence that is a file count and an example path - both of
            # which move whenever the compared trees do. Declaring the fragments keeps
            # the case about the clause rather than about today's numbers.
            wants = (expect,) if isinstance(expect, str) else tuple(expect)
            missing = [e for e in wants if e not in where]
            if not why and missing:
                why = (f"{'refusal message' if got == 'EXIT' else 'rendered page'} does not"
                       f" contain {missing[0]!r}")
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
