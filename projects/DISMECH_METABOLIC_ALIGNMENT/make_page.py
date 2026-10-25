"""Render the dismech<->AIGR alignment audit as a markdown project page.

This generator refuses to render rather than publish a claim it cannot support, and those
refusals are themselves exercised: ``check_page_guards.py`` beside it breaks one thing in a
copy of each report and checks that the generator either refuses or, where the branch is a
legitimate state, still renders.

    just check-alignment-page-guards

It runs under pytest too (`tests/test_dismech_alignment_page_guards.py`), so a regression in
a refusal fails the suite rather than waiting to be noticed.

Usage::

    make_page.py <report.yaml> <out.md> [<second-report.yaml>]

With a second report, the two runs are reconciled flag by flag onto a self-check page
written to DISMECH_METABOLIC_ALIGNMENT/audit-self-check.md in <out.md>'s directory, and
the page links to it.

WITHOUT one, that self-check page is DELETED if it exists. Run from the repository the
two-argument form therefore removes the committed
``projects/DISMECH_METABOLIC_ALIGNMENT/audit-self-check.md``, leaving an uncommitted
deletion of curated content. That is deliberate - with no second run there is nothing to
reconcile, and render-projects walks the whole tree, so a file left behind keeps
publishing an earlier run's figures with nothing linking to it - but it is stated here
because the Method paragraph that also states it is written by the run that does the
deleting, which is too late to warn anyone.
"""
import os
import re
import subprocess
import sys

import yaml


def load(path):
    """Return (provenance, entries, review-independent flag names) for a report."""
    d = yaml.safe_load(open(path))
    # Both committed reports are now produced by the current script, so the old leniency
    # here - added when the all-slices report could not be regenerated from this branch -
    # is gone: a missing key is a superseded report and the callers exit on it.
    if isinstance(d, dict):
        prov = dict(d.get("provenance") or {})
        # Carried on the provenance mapping so the renderer reads the groups the run
        # recorded rather than a copy of them kept here.
        # Keyed on presence, not truthiness: an empty map is a run that matched no pairs,
        # which is a different fact from a report that predates the key. Gating on
        # truthiness made the two indistinguishable and left the empty-case branch below
        # unreachable, so a legitimate empty run was told its script was superseded.
        if "flag_groups" in d:
            prov["_flag_groups"] = d["flag_groups"]
        if "term_aspects" in d:
            prov["_term_aspects"] = d["term_aspects"]
        return (prov, d.get("entries") or [],
                tuple(d.get("review_independent_flags") or ()))
    return {}, d, ()


PROV, rep, _INDEP = load(sys.argv[1])
out = sys.argv[2]
# Optional third argument: a second report over the same scope, whose counts the
# provenance section compares against this one's. Passing it is what makes the
# branch-local comparison a measurement; without it the comparison is simply not printed,
# which is the right behaviour once every slice has merged and there is nothing to compare.
ALT_PATH = sys.argv[3] if len(sys.argv) > 3 else None
ALT_PROV, ALT_REP, ALT_INDEP = load(ALT_PATH) if ALT_PATH else ({}, [], ())


def flag_counts(entries):
    """Flag -> occurrences over every gene row, and the row total."""
    c, n = {}, 0
    for e in entries:
        for g in e.get("genes") or []:
            n += 1
            for f in g.get("flags") or []:
                c[f] = c.get(f, 0) + 1
    return c, n


def row_index(entries):
    """Map every gene row to its record, keyed by (entry, gene, nth occurrence).

    The ordinal is defensive, not load-bearing on this data: no gene holds two rows
    inside one entry in either report, so it is always 0 today. An earlier version of
    this docstring said otherwise and cited ABCC8 and APOB - both of which do hold
    several rows, but each in a different entry (ABCC8 in Congenital_Isolated_
    Hyperinsulinism and Hyperinsulinemic_Hypoglycemia; APOB in three), which
    (entry, gene) already separates. It is kept because a duplicate would otherwise
    collapse two rows into one silently, and REPEATED_ROWS below records whether any
    exists rather than leaving the question to a comment.
    """
    out, seen = {}, {}
    for e in entries:
        for g in e.get("genes") or []:
            k = (e.get("entry"), g.get("gene"))
            n = seen.get(k, 0)
            seen[k] = n + 1
            out[(k[0], k[1], n)] = g
    return out


ROWS_HERE, ROWS_THERE = row_index(rep), row_index(ALT_REP) if ALT_REP else {}


# Worked examples named in the prose below, re-checked against the report that is
# rendering this page. The figures on this page are all derived; these examples were not,
# and the aspect() docstring records one of them having silently stopped being true when
# the input tree changed. Asserting them turns that into a render failure rather than a
# published claim. Each tuple is (symbol, terms that must be aligned, terms that must be
# unaligned, pairs that must hold as node->core).
# UCP2 aligns only against a term the review keeps as non-core, so its match is recorded
# in aligned_noncore_terms/-_pairs rather than in aligned_terms, and the node term stays
# in dismech_only. The prose says exactly that, so the guard checks it that way.
PROSE_EXAMPLES = [
    ("DMP1", ["GO:0005509"], [], {}, [], {}),
    ("GLUD1", ["GO:0004353"], [], {"GO:0004353": "GO:0004353"}, [], {}),
    ("LCT", ["GO:0000016"], ["GO:0006366"], {}, [], {}),
    ("NDUFA1", ["GO:0008137"], [], {}, [], {}),
    ("UCP2", [], ["GO:0050796"], {}, ["GO:0050796"], {"GO:0050796": "GO:0061179"}),
]


def _check_prose_examples():
    """Fail the render when a hardcoded example no longer matches the report."""
    by_sym = {}
    for (_entry, sym, _n), g in ROWS_HERE.items():
        by_sym.setdefault(sym, []).append(g)
    bad = []
    for sym, must_align, must_not_align, pairs, must_noncore, noncore_pairs in PROSE_EXAMPLES:
        rows = by_sym.get(sym)
        if not rows:
            bad.append(f"{sym}: named in the prose but holds no row in this report")
            continue
        aligned, unaligned, noncore = set(), set(), set()
        pairmap, ncpairmap = {}, {}
        for g in rows:
            aligned |= set(g.get("aligned_terms") or [])
            unaligned |= set(g.get("dismech_only") or [])
            noncore |= set(g.get("aligned_noncore_terms") or [])
            for src, dest in ((g.get("aligned_pairs") or {}, pairmap),
                              (g.get("aligned_noncore_pairs") or {}, ncpairmap)):
                for k, v in src.items():
                    dest.setdefault(k, set()).update(v if isinstance(v, list) else [v])
        for terms, have, what in ((must_align, aligned, "aligned"),
                                  (must_not_align, unaligned, "unaligned"),
                                  (must_noncore, noncore, "aligned against a non-core term")):
            for t in terms:
                if t not in have:
                    bad.append(f"{sym}: prose calls {t} {what}; report does not")
        for prs, have, what in ((pairs, pairmap, "pairs"),
                                (noncore_pairs, ncpairmap, "non-core pairs")):
            for k, v in prs.items():
                if v not in have.get(k, set()):
                    bad.append(f"{sym}: prose {what} {k}->{v}; report has "
                               f"{sorted(have.get(k, set())) or 'no such pair'}")
    if bad:
        sys.exit("prose examples no longer match the report, so the page would publish a "
                 "stale claim:\n  " + "\n  ".join(bad))


_check_prose_examples()
# Whether the ordinal in the key is doing anything, measured rather than asserted.
REPEATED_ROWS = sorted({(e, g) for (e, g, n) in list(ROWS_HERE) + list(ROWS_THERE) if n})
# Symbols holding more than one row anywhere in either report. Scoped to the reports, not
# to one flag's movement: a gene with rows in three entries prints bare wherever only one
# of them moved, and the same page then prints the same symbol both ways - HADH
# disambiguated in one bullet and bare two bullets later. 20 symbols qualify.
# Counted over the union of row keys, so a row present in both reports counts once and the
# threshold is "more than one row" rather than an artifact of concatenating two lists.
_ALL_SYMS = [g for (_, g, _) in set(ROWS_HERE) | set(ROWS_THERE)]
AMBIGUOUS_SYMS = {g for g in set(_ALL_SYMS) if _ALL_SYMS.count(g) > 1}
# Global, but only the comparison section and the module-reason list consult it: the table
# renders from the primary report and carries the entry in its own column, so a symbol
# there is never ambiguous. Both reports hold the same rows, which the row-count guard in
# alt_comparison enforces, so one set is correct for both.
if REPEATED_ROWS:
    # Fatal rather than a console note. A true duplicate is exactly the case the page
    # cannot disambiguate - show_rows prints the entry, which would be identical - so the
    # accounting below would name two rows a reader cannot tell apart, silently.
    sys.exit(f"{len(REPEATED_ROWS)} gene(s) hold more than one row inside one entry "
             f"({', '.join(f'{g} ({e})' for e, g in REPEATED_ROWS)}); the movement "
             "accounting names rows by entry and symbol, which cannot separate them")


def flag_rows(entries, flag):
    """The set of row keys carrying `flag`.

    Counts are not identity: two runs can report the same number of occurrences over
    wholly different rows, which is what PARTIAL_COVERAGE does here - 14 against 14, with
    9 rows shared and 5 distinct on each side. A net count hides it twice over, since
    NO_MODULE_MEMBERSHIP's fall of 10 is 24 departures against 14 arrivals. Every
    explanation this page attaches to a flag's movement is therefore computed from the
    rows, not from the totals.
    """
    idx = ROWS_HERE if entries is rep else ROWS_THERE if entries is ALT_REP else row_index(entries)
    return {k for k, g in idx.items() if flag in (g.get("flags") or ())}


# One definition, consulted by both the Method paragraph and the comparison section, which
# had computed it identically.
ALT_TREE = (ALT_PROV.get("aigr_tree") or ALT_PROV.get("aigr_branch") or "a second tree"
            ) if ALT_PROV else ""
# The same tree in a few words. aigr_tree is a whole sentence - deliberately, it is the
# provenance - so naming it in two places printed ~190 characters and the revision twice.
# The comparison section carries the full description; the Method paragraph takes this.
# Structured fields only. The branch name is "HEAD" for a detached checkout - which the
# provenance block already special-cases - and splitting aigr_tree on its punctuation was
# string surgery on a sentence the audit formatted for a reader.
_alt_branch = (ALT_PROV.get("aigr_branch") or "") if ALT_PROV else ""
ALT_TREE_SHORT = ((_alt_branch if _alt_branch and _alt_branch != "HEAD"
                   else (ALT_PROV.get("aigr_revision") or "")[:9] or "a second tree")
                  if ALT_PROV else "")


def _sha_shaped(value):
    """Whether a string looks like an abbreviated object name, digit required.

    The digit is the same precaution `_check_tree_names_revision` takes, and it matters more
    here because this test starts at four characters: `cafe`, `facade`, `beaded` and
    `defaced` are all a-f only, so without it a ref with such a name would be reported as an
    object this checkout does not hold - a claim about the object store about a string that
    was never an object, which is the defect this test exists to avoid making.
    """
    return bool(re.fullmatch(r"[0-9a-f]{4,40}", value or "")) and any(c.isdigit() for c in value)


def _in_span(value, limit=60):
    """An operator-supplied value, safe to interpolate inside a backtick code span.

    Every other revision this page prints is `[:9]` of a sha git resolved. The unresolvable
    sentences print what was recorded instead, which is whatever went into `AIGR_REVISION` -
    a backtick would close the span and a pipe would end the surrounding table cell.
    """
    return re.sub(r"\s+", " ", (value or "")[:limit]).replace("`", "'").replace("|", "/")


def _check_tree_names_revision(which, text, rev):
    """Refuse when a report's tree description names shas but not the one it records.

    `aigr_tree` is operator-supplied text and routinely names a sha in prose. Nothing
    compared it with `aigr_revision`, so the description and the sentence derived from the
    recorded revision agreed only by coincidence. Checked rather than trusted: any 7-to-40
    hex run in that text that looks like a sha must be a prefix of, or prefixed by, the
    recorded revision.

    The text legitimately names several revisions - the base commit, each merged branch
    tip, the resulting merge - so the invariant is not "every sha is the recorded one",
    which a first draft of this check asserted and which the committed text refutes. It is
    that the revision the report records appears among them: otherwise the description and
    the derived sentence describe different commits. Where the text names no sha at all -
    `ALT_TREE` falls back to the branch name - there is nothing to disagree with and the
    invariant is vacuously satisfied rather than checked.

    Applied to both reports. It was primary-only for a round, although the second report's
    pair is the closer of the two on the page - the description and the sentence derived
    from `aigr_revision` render three lines apart, agreeing by exactly the coincidence this
    check exists to end. Run here rather than inside the section that prints either, so a
    mismatch refuses whichever sections a given run renders.
    """
    # At least one digit required: a 7-to-40 character run of a-f is also an ordinary word
    # ("defaced"), and a description naming no sha but containing one would have refused to
    # render with a provenance-mismatch message.
    named = [m for m in re.findall(r"\b[0-9a-f]{7,40}\b", text or "")
             if any(c.isdigit() for c in m)]
    # Only a recorded sha is compared. `aigr_revision` may hold anything gitrevisions(7)
    # admits - a ref, a tag, `HEAD~3` - and such a value satisfies neither `startswith`
    # direction against a description that names a sha, so this guard refused to render the
    # very input the resolve step was added to handle. A short abbreviation is still
    # compared, which is the case the guard was written for.
    if rev and _sha_shaped(rev) and named and not any(rev.startswith(m) or m.startswith(rev)
                                                      for m in named):
        sys.exit(f"the {which} report's tree description names {', '.join(named[:4])} but "
                 f"not the revision it records (`{rev[:9]}`); the provenance block and the "
                 "derived sentence below would describe different commits")


_check_tree_names_revision("primary", PROV.get("aigr_tree"), PROV.get("aigr_revision") or "")
if ALT_PROV:
    # ALT_TREE, not the raw `aigr_tree`: that is the string the page prints, and it falls
    # back to the branch name when the second run recorded no tree description.
    _check_tree_names_revision("second", ALT_TREE, ALT_PROV.get("aigr_revision") or "")


# `_rev_state`'s memo: one key, holding both the state and the sha the value resolved to.
# Two dicts keyed identically, one filled as a side effect of the other, let a reader of the
# second get a silent fallback without having called the first - the same argument that
# retired the duplicate flag-group copies this page used to keep.
_REV_STATE = {}
_IN_REPO = None


def _in_repo():
    """Whether git will answer about this directory at all. Asked once per process.

    Kept out of `_rev_state`'s memo because the answer varies with neither the revision nor
    the call: a directory either is a repository or is not. Caching it under a per-revision
    key stored a property of the process under a key describing something else, and re-ran
    the probe for each distinct revision.

    git absent from PATH raises rather than exiting, and `_primary_drift_tail` calls
    `_rev_state` with no guard of its own, so without the catch the generator would die
    with a traceback instead of claiming nothing.
    """
    global _IN_REPO
    if _IN_REPO is None:
        try:
            _IN_REPO = subprocess.run(["git", "rev-parse", "--git-dir"],
                                      capture_output=True).returncode == 0
        except Exception:
            _IN_REPO = False
    return _IN_REPO


def _rev_state(rev):
    """Three facts about a recorded revision, kept to their own scopes.

    Rounds 13 to 15 each got this wrong by letting one fact stand in for another, so the
    scopes are stated here rather than left to the call sites:

    * **published** - reachable from a remote-tracking ref. Environment-independent in its
      consequence: a revision on no pushed ref is in nobody's clone, which is a fact about
      the revision and safe to put on a published page.
    * **local** - the object is in *this* checkout. Purely local: CI clones at
      ``fetch-depth: 1``, so an ordinary pushed commit is absent there. It licenses
      *computing* a diff and licenses no claim about the revision itself - in particular
      never a claim about *why* it is missing, which git cannot answer and which earlier
      rounds glossed as "a tree assembled for that run".
    * the drift answer itself, which needs the object present and, once computed, is a fact
      about two commits and so the same everywhere.

    Reachability cannot be computed without the object, so ``unpublished`` is obtainable
    only where the object is local: a reader re-rendering in a shallow clone gets the weaker
    ``not_here`` sentence for a revision this page calls unpublished. That is a limit on the
    claim's *availability*, not on its content - nothing published becomes false - but it is
    why a re-render can say less than the committed page.

    Returns ``published``, ``unpublished`` (resolves here, on no pushed ref), ``not_here``
    (does not resolve here and is shaped like an object name, so most likely an object this
    checkout lacks), ``unresolvable`` (does not resolve here and is not shaped like one) or
    ``unknown`` (git could not be asked). ``unknown`` says nothing about the object store,
    and in particular is not a weaker ``not_here``: reached from `_alt_drift_tail` it means
    the revision resolved and only its publication is unanswerable.

    ``not_here`` and ``unresolvable`` split one failure git reports once - `rev-parse`
    exits 128 for an absent object and for an unusable string alike - so the shape of the
    recorded value is the only evidence for which it is, and neither sentence claims more
    than that. What is *not* done is to decide the state from the shape and then describe
    the decision as git's: a shape test printing "not a revision git can look up" was false
    for every ref, tag and short abbreviation an operator can put in ``AIGR_REVISION``.

    Memoized, which on this run never hits: the two callers ask about two different
    revisions, one each. It is here so that adding a caller cannot quietly multiply git
    calls - an earlier comment claimed each caller asked twice, which was not true of that
    code either.
    """
    if rev in _REV_STATE:
        return _REV_STATE[rev][0]
    state = "unknown"
    # Nothing about the recorded value is decided before this: `cat-file -e` exits 128 both
    # for a missing object and for a fatal such as "not a git repository", so its exit code
    # alone cannot tell absence from failure, and a test of the value's *shape* run ahead of
    # this probe published a claim about what git can resolve from a process that had asked
    # git nothing. `_in_repo` asks once per process rather than once per revision.
    if not _in_repo():
        _REV_STATE[rev] = ("unknown", None, None)
        return "unknown"
    # git is asked to resolve the value, rather than the value being matched against the
    # shape of an abbreviated object name. The two differ for most of what gitrevisions(7)
    # calls a revision - a ref, a tag, `HEAD~3`, an abbreviation shorter than seven - all of
    # which resolve and all of which a shape test called unusable; `aigr_revision` comes
    # from an environment variable, so a ref there is an operator slip rather than a
    # hypothetical. It also separates a 40-hex object that is present but is a blob or a
    # tree, which `cat-file -e <sha>^{commit}` failed and so reported as not held.
    #
    # `--verify <rev>^{commit}`, never bare `--verify`, which exits 0 for any well-formed
    # 40-character sha whether or not an object matches it.
    #
    # Wrapped, as the two calls below it are. Unreachable in practice - `_in_repo()` has
    # already run git successfully - but two of the four being wrapped and two not is the
    # kind of inconsistency that reads as a decision when it is an oversight.
    try:
        r = subprocess.run(["git", "rev-parse", "--verify", f"{rev}^{{commit}}"],
                           capture_output=True, text=True)
    except Exception:
        _REV_STATE[rev] = ("unknown", None, None)
        return "unknown"
    resolved = detail = None
    if r.returncode != 0:
        # `--verify <rev>^{commit}` exits 128 for three different things: an object this
        # checkout lacks, an object it holds that is not a commit, and a string that is not
        # a revision at all. git distinguishes the first two itself - `cat-file -t` reports
        # the type of anything in the object store - so the one that was previously folded
        # into "this checkout does not hold" is now asked about rather than guessed at. The
        # reason only reached stderr before, which this code discarded.
        try:
            t = subprocess.run(["git", "cat-file", "-t", rev],
                               capture_output=True, text=True)
        except Exception:
            _REV_STATE[rev] = ("unknown", None, None)
            return "unknown"
        if t.returncode == 0:
            # The type goes in the memo, not into the state name: the two sentence tables
            # below are keyed exhaustively so that a new state raises rather than rendering
            # a blank, and a name carrying a payload would defeat that.
            state, detail = "not_a_commit", (t.stdout.strip() or "object")
        else:
            # Neither resolvable nor present, so the shape of the value is the only evidence
            # left for which it was meant to be, and each sentence claims only that much.
            state = "not_here" if _sha_shaped(rev) else "unresolvable"
    else:
        # The full sha, so the branch-tip comparison is not defeated by an abbreviation that
        # resolves to the tip, and so the three calls that follow are given a commit rather
        # than whatever string the operator recorded.
        resolved = r.stdout.strip() or rev
        try:
            f = subprocess.run(["git", "for-each-ref", "--contains", resolved, "refs/remotes"],
                               capture_output=True, text=True)
        except Exception:
            _REV_STATE[rev] = ("unknown", resolved, detail)
            return "unknown"
        if f.returncode == 0:
            if f.stdout.strip():
                state = "published"
            else:
                # A revision that is this branch's own history but not yet on a remote is
                # the ordinary state while a round is being prepared: the page is rendered,
                # then committed, then pushed, and the flat "no clone holds it" was written
                # into the artifact moments before the push made it false. Reported as its
                # own state so the sentence is true on both sides of that push.
                # Three outcomes, not two. `merge-base --is-ancestor` exits 1 for "not an
                # ancestor" and 128 for a genuine error - an unborn HEAD among them, which
                # this function does not rule out before asking. Reading everything non-zero
                # as "not an ancestor" would publish the definite claim that no clone holds
                # the revision on the strength of a git failure, which is the failure the
                # sibling `_alt_drift_tail` splits these exact codes to avoid.
                try:
                    anc = subprocess.run(
                        ["git", "merge-base", "--is-ancestor", resolved, "HEAD"],
                        capture_output=True)
                except Exception:
                    state = "unknown"
                else:
                    if anc.returncode == 0:
                        state = "unpushed_here"
                    elif anc.returncode == 1:
                        state = "unpublished"
                    else:
                        state = "unknown"
    _REV_STATE[rev] = (state, resolved, detail)
    return state


def _resolved(rev):
    """The sha `rev` resolved to, or `rev` itself where it did not resolve.

    Reads the memo `_rev_state` fills, so calling it without having called `_rev_state`
    returns the fallback. Every caller below asks for the state first.
    """
    return (_REV_STATE.get(rev) or (None, None, None))[1] or rev


def _obj_type(rev):
    """What `cat-file -t` called the object, for the `not_a_commit` sentences."""
    return (_REV_STATE.get(rev) or (None, None, None))[2] or "object"


# What each state means for a reader, as its own clause. Appended after the drift answer,
# because publication bears on whether a reader can re-run the comparison rather than on
# whether the inputs moved. Every state has an entry, so a new state cannot render a blank
# clause by omission - a missing key raises where an empty string would quietly print
# nothing. `unresolvable`'s entry is never read: both tails return before consulting this
# dict, because a value git could not resolve leaves nothing to say about publication. It
# is here to keep the mapping total, not because it renders.
_REPRODUCIBLE = {
    "published": "",
    "unpublished": " That revision is on no pushed ref, so no clone holds it and this"
                   " comparison cannot be re-run elsewhere.",
    # True before and after the push that follows rendering, which the flat `unpublished`
    # sentence was not: it is this branch's history either way.
    "unpushed_here": " That revision is this branch's own history and not yet on a pushed"
                     " ref, so a clone holds it once this branch is pushed.",
    # The one clause that names a cause, which the drift answer deliberately never does. It
    # is admissible because it is about *this* checkout, which is observable, rather than
    # about the revision - a shallow clone is the ordinary reason and naming it tells a
    # reader why re-rendering may say less than the committed page does. It renders only
    # behind the `not_here` sentence, which has already said the object is absent, so the
    # clause no longer repeats that: it said it twice in consecutive sentences.
    "not_here": " Whether that revision is published could not be determined here, and a"
                " shallow clone will not hold it either.",
    "unknown": " Whether that revision is published could not be determined, so nothing is"
               " claimed about re-running this elsewhere.",
    "unresolvable": "",
    # The object is here, so publication is answerable in principle - but it is not a commit,
    # and `for-each-ref --contains` takes a commit. Nothing was asked, so nothing is claimed.
    "not_a_commit": " Whether anything published names it could not be determined, since it"
                    " is not a commit.",
}


def _primary_drift_tail():
    """What can be said about the primary report's own tree, whose figures the table shows.

    Leads with publication rather than with local presence. "Is a commit here" was true on
    the machine that rendered it and false for every reader, which is the environment
    dependence this function has now been corrected for twice; whether a revision is on a
    pushed ref is a fact about the revision.
    """
    rev = (PROV or {}).get("aigr_revision")
    if not rev:
        return "The primary run records no revision, so its tree cannot be located."
    short = rev[:9]
    return {
        "published": f"The primary run's tree (`{short}`) is on a pushed ref, so the same"
                     " comparison can be made for the table's own figures.",
        "unpublished": f"The primary run's tree (`{short}`) is on no pushed ref, so no clone"
                       " holds it and the same comparison cannot be made from one.",
        "unpushed_here": f"The primary run's tree (`{short}`) is this branch's own history"
                         " and not yet on a pushed ref, so the same comparison can be made"
                         " from a clone once this branch is pushed.",
        "not_here": f"The primary run's tree (`{short}`) is not in this checkout, so nothing"
                    " is claimed about whether a clone could compare the table's own figures.",
        "unknown": f"Whether the primary run's tree (`{short}`) is published could not be"
                   " determined, so nothing is claimed about the table's own figures.",
        "unresolvable": f"The primary run records `{_in_span(rev)}` as its tree, which git"
                        " cannot resolve to a commit here and which is not shaped like an"
                        " object name, so nothing is claimed about the table's own figures.",
        "not_a_commit": f"The primary run's tree (`{short}`) is in this checkout as a"
                        f" {_obj_type(rev)} rather than a commit, so nothing is claimed about"
                        " the table's own figures.",
    }[_rev_state(rev)]


def _alt_drift_tail():
    """Whether the audit's inputs moved between the second run's tree and the branch now.

    The recorded revision is usually an ancestor of the branch tip, because the commit that
    carries each round's own changes comes after the audit that fed it. That is honest
    provenance and not a defect, but it leaves a reader checking the branch out on a
    different commit from the one the figures were read on - so whether it matters is
    measured rather than assumed. It is not *necessarily* an ancestor: a run over a tree
    assembled for the run records a revision no clone has.

    Ancestry is tested before publication, and publication is reported as its own clause:
    a revision committed here and not yet pushed answers the drift question perfectly, and
    gating on publication once printed that there was nothing to compare.

    This function owns all of its punctuation, including the final period. Splitting that
    with the caller produced a double period in three of the four states - every one whose
    reproducibility clause is a sentence of its own - and left the docstring, a comment and
    the code disagreeing three ways about who supplies it. The caller appends nothing.
    """
    rev = (ALT_PROV or {}).get("aigr_revision")
    if not rev:
        return " at a revision the report does not name."
    try:
        head = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True, text=True,
                              check=True).stdout.strip()
    except Exception:
        return (f" at `{rev[:9]}`; git could not be asked where this branch is, so nothing is"
                " claimed about whether the audit's inputs moved since.")
    state = _rev_state(rev)
    if state == "unresolvable":
        return (f" at `{_in_span(rev)}`, which git cannot resolve to a commit here and which"
                " is not shaped like an object name, so the input-drift comparison below was"
                " not made.")
    if state == "not_a_commit":
        # Previously folded into "this checkout does not hold", which was false of the one
        # case where git knows exactly what the value is.
        return (f" at `{rev[:9]}`, which this checkout holds as a {_obj_type(rev)} rather"
                " than a commit, so the input-drift comparison below was not made."
                f"{_REPRODUCIBLE[state]}").rstrip()
    if _resolved(rev) == head:
        # Compared on the resolved sha, not on the recorded string: an abbreviation that is
        # the tip took the ancestor path and printed the other of two true sentences.
        #
        # The reproducibility clause belongs here too: a tip committed and not yet pushed is
        # the ordinary state while a round is being prepared, and this return used to be the
        # one that skipped `_rev_state` and so said nothing about whether a clone has it.
        # "Nothing to compare" is said rather than left to the reader: every sibling return
        # states what the comparison found, so a bare "this branch's tip" read as an omission.
        return (f" at `{rev[:9]}`, which is this branch's tip, so there is nothing to"
                f" compare.{_REPRODUCIBLE[state]}").rstrip()
    if state == "not_here":
        # No gloss on *why* the object is missing: a shallow clone, a pruned object and a
        # tree never committed are indistinguishable here, and earlier rounds asserted the
        # last of the three.
        return (f" at `{rev[:9]}`, which this checkout does not hold, so the input-drift"
                f" comparison below was not made.{_REPRODUCIBLE[state]}").rstrip()
    # `unknown` deliberately falls through to the drift answer rather than joining the
    # branch above. Every `unknown` that can arrive here was set after `cat-file -e`
    # succeeded, so the object *is* in this checkout and `merge-base` and `diff` will both
    # answer; the only other `unknown` - no repository at all - cannot reach this line,
    # because `rev-parse HEAD` returned above. Grouping the two printed "which this
    # checkout does not hold" for the one state that proves the object is held, and skipped
    # a `merge-base` and `diff` git would have answered - they never ran, so the answer was
    # forgone rather than discarded. What is unknown is publication alone, which is what the
    # clause at the end of this function says.
    # The resolved sha, for the reason the resolve step records: these ask about a commit
    # rather than about whatever string the operator recorded.
    anc = subprocess.run(["git", "merge-base", "--is-ancestor", _resolved(rev), "HEAD"],
                         capture_output=True)
    if anc.returncode == 1:
        base = (f" at `{rev[:9]}`, which is not an ancestor of this branch's tip, so the two"
                " cannot be compared by diffing and the figures stand only for the recorded"
                " tree")
    elif anc.returncode != 0:
        return (f" at `{rev[:9]}`; git could not say whether it is an ancestor of this branch,"
                " so nothing is claimed.")
    else:
        try:
            out = subprocess.run(["git", "diff", "--name-only", f"{_resolved(rev)}..HEAD",
                                  "--", "genes", "modules"],
                                 capture_output=True, text=True, check=True).stdout.split()
        except Exception:
            return (f" at `{rev[:9]}`, an ancestor of the branch tip; git could not list what"
                    " changed between the two, so nothing is claimed.")
        if not out:
            base = (f" at `{rev[:9]}`, an ancestor of the branch tip, with no file under"
                    " `genes/` or `modules/` changed between the two - the audit's whole input"
                    " surface - so the figures stand for either")
        else:
            base = (f" at `{rev[:9]}`, an ancestor of the branch tip, with **{len(out)} of the"
                    " audit's input files changed between the two**, so the figures below"
                    f" describe the recorded commit rather than the tip - e.g. `{out[0]}`")
    # `base` has no terminal period and each clause is a sentence of its own, so the period
    # between them is always needed and the one after them always ours.
    return (base + "." + _REPRODUCIBLE[state]).rstrip()


def alt_comparison():
    """The second report's flag counts against this one's, derived rather than quoted.

    Nothing is printed without a second report, so once every slice has merged and there
    is no second tree to compare, the paragraph disappears instead of going stale. The
    previous version of this section hardcoded six numbers in this file, which made the
    one artifact added to support the disclosure the one artifact nobody could check.
    """
    if not ALT_REP:
        return []
    here, n_here = flag_counts(rep)
    there, n_there = flag_counts(ALT_REP)
    if n_here != n_there:
        # The comparison's whole premise is that the two runs cover the same rows, so a
        # mismatch is a bug in the scope or the trees, not something to paper over.
        sys.exit(f"report row counts differ ({n_here} vs {n_there}); the two runs do not "
                 "cover the same scope and cannot be compared flag by flag")
    # No fallback copy of the audit's set: a second copy here is the drift the export was
    # added to prevent, moved from prose into code. A report without the field cannot be
    # compared, and saying so is stricter and matches how MODULE_REASONS fails.
    if not ALT_INDEP:
        sys.exit("the second report has no review_independent_flags; it was produced by a "
                 "superseded align_audit.py and cannot be compared - re-run the audit")
    # The exact check the presence tests below were a proxy for: same script, same report
    # semantics. Two reports from different script versions cannot be compared flag by flag.
    if not (PROV.get("audit_sha256") and ALT_PROV.get("audit_sha256")):
        # Required, not optional: a conditional check lets a report without the field fall
        # back on the presence proxies, when the other three fields are hard requirements.
        sys.exit("a report carries no audit_sha256; it was produced by a superseded "
                 "align_audit.py and the two cannot be shown to come from one script")
    if PROV["audit_sha256"] != ALT_PROV["audit_sha256"]:
        sys.exit(f"the two reports were produced by different align_audit.py versions "
                 f"({PROV['audit_sha256']} vs {ALT_PROV['audit_sha256']}); their flags are "
                 "not necessarily comparable - re-run both from one script")
    if _INDEP and set(_INDEP) != set(ALT_INDEP):
        # Otherwise two reports could disagree about which flags are review-independent and
        # the identity guard below would silently be checking the wrong set.
        sys.exit("the two reports disagree about which flags are review-independent "
                 f"({sorted(set(_INDEP) ^ set(ALT_INDEP))}); they come from different "
                 "align_audit.py versions and cannot be compared")
    indep = ALT_INDEP
    # Enforced, not asserted: these are the flags decided before the gene review is read,
    # so they must be identical between two runs over the same dismech tree. If one moves,
    # the difference is not the review set and the explanation below would be wrong.
    moved = [f for f in indep if here.get(f, 0) != there.get(f, 0)]
    if moved:
        sys.exit("flags that do not read a gene review differ between the two reports "
                 f"({', '.join(moved)}); the difference between the runs is not the review "
                 "set, so the explanation on the page would be false")
    rose = sorted(f for f in set(here) | set(there)
                  if there.get(f, 0) > here.get(f, 0) and f not in indep)
    fell = sorted(f for f in set(here) | set(there)
                  if there.get(f, 0) < here.get(f, 0) and f not in indep)

    def pairs(fs):
        return ", ".join(f"`{f}` {there.get(f, 0)} against {here.get(f, 0)}" for f in fs)

    mods_here = (PROV.get("module_accessions") or {}).get("modules_read")
    mods_there = (ALT_PROV.get("module_accessions") or {}).get("modules_read")
    # Each risen flag is explained by the group it belongs to, read from the report rather
    # than inferred by subtraction. The previous version split the rises into "module
    # flags" and "everything else", and told the reader everything else counted *absent*
    # reviews - wrong for AIGR_NOT_COMPLETE and NO_CORE_FUNCTION_TERMS, which fire where a
    # review was found, and so wrong for 85 of 87 rows in the run it was written against.
    groups = ALT_PROV.get("_flag_groups")
    if "_flag_groups" not in ALT_PROV:
        sys.exit("the second report has no flag_groups; it was produced by a superseded "
                 "align_audit.py and its risen flags cannot be explained - re-run the audit")
    if not groups:
        # Present but empty is a separate failure from absent, and unlike term_aspects it is
        # never legitimate: without the groups every risen flag falls through to "cause not
        # established", which would read as a finding rather than as a broken input.
        sys.exit("the second report's flag_groups is empty; every risen flag would be reported "
                 "as unexplained rather than grouped - re-run the audit")
    if "_term_aspects" not in ALT_PROV:
        # Not read for the cross-aspect figures, which come from the primary report, but a
        # second report missing it is a superseded one and the two are then not comparable.
        sys.exit("the second report has no term_aspects; it was produced by a superseded "
                 "align_audit.py - re-run the audit")
    absent = tuple(groups.get("review_absent") or ())
    thin = tuple(groups.get("review_present_thin") or ())
    modular = tuple(groups.get("module_sourced") or ())
    rose_absent = [f for f in rose if f in absent]
    rose_thin = [f for f in rose if f in thin]
    rose_mod = [f for f in rose if f in modular]
    rose_other = [f for f in rose if f not in absent + thin + modular]

    def names(fs):
        return ", ".join(f"`{f}`" for f in fs)

    def move_cause(flag, mine, theirs):
        """Why one row carries `flag` on one tree and not on the other.

        Read from that row's own record on **both** sides, never from the flag's group.
        Group membership says where in the audit a flag is computed; it does not say why
        a given row moved, and attributing a whole movement to the group was wrong in
        both directions - PEX5 leaves PARTIAL_COVERAGE because its review is a stub while
        its covering module is present on both trees, and ABCG5, ABCG8 and POMC arrive at
        NO_MODULE_MEMBERSHIP with complete reviews because a module is absent.

        `mine` is the row on the tree that carries the flag, `theirs` the tree that does
        not. Both are consulted: a row can gain an alignment flag because the review on
        its *own* side is a stub, which is an artifact of the missing slices, and reading
        only the other side reported those as a substantive difference between the two
        reviews - the artifact-versus-finding call this whole section exists to make.

        The order follows the audit's own control flow: a row with no review returns
        before any module test runs, so an absent review is the cause even where the
        module set also differs. The first two cases are definitional rather than
        inferred - a flag that counts absent or thin reviews is its own explanation - and
        are phrased without naming a side, since they fire for a departure as readily as
        for an arrival.
        """
        ours, thrs = set(mine.get("flags") or ()), set(theirs.get("flags") or ())
        if flag in absent:
            return "the flag is itself the absence of a review on the tree carrying it"
        if flag in thin:
            return ("the flag is itself a stub review, or the absence of core-function"
                    " terms, on the tree carrying it")
        if set(absent) & thrs:
            return "the row has no review on the other tree"
        mods = (set(mine.get("modules") or ()), set(theirs.get("modules") or ()))
        terms = (set(mine.get("aligned_terms") or ()), set(theirs.get("aligned_terms") or ()))
        if flag in modular and mods[0] != mods[1]:
            return "the modules containing the gene differ"
        # The module causes come first and are read from the recorded module and coverage
        # lists. A stub review is checked only where it could have done the work - where
        # the aligned-term sets differ - because that is the only route by which a thin
        # review changes a module verdict. HAO1 is the case that fixes the order: same
        # modules, identical aligned terms, and glyoxylate_oxalate_metabolism covering two
        # of them here and one there, so its PARTIAL_COVERAGE arrival is the module's own
        # contents and its stub review is incidental.
        if flag in modular and terms[0] == terms[1]:
            return "the same modules carry different terms"
        # Both thin checks sit here, below the module causes and behind the same gate.
        # Only the *absent* case is justified by the audit's control flow: a row with no
        # review returns before any module test, while AIGR_NOT_COMPLETE does not
        # short-circuit them (align_audit.py). So a thin review on either side can only
        # have moved a module verdict by changing the aligned terms, and is checked where
        # that is true. PEX5 keeps its cause, its terms being absent on the second tree.
        if set(thin) & thrs and terms[0] != terms[1]:
            return "the review on the other tree is a stub or has no core-function terms"
        if set(thin) & ours and terms[0] != terms[1]:
            return ("the review on the flagged side is itself a stub, so the flag is an"
                    " artifact of the thin review rather than a difference between the"
                    " two reviews")
        if terms[0] != terms[1]:
            return "the row's own aligned terms differ, so the two reviews differ"
        return "a reason this comparison does not establish"

    def cover_evidence(flag, rows):
        """Show a same-modules-different-coverage case from covering_pairs.

        The one cause in the chain that was reached by elimination rather than read: with
        the same modules and the same aligned terms, a coverage difference can only be the
        modules' own contents, which covering_pairs records per module. Every row in the
        group is shown, not the first - asserting the cause for a group and showing it for
        one row leaves the rest where the cause as a whole was before it was read - and the
        count is asserted against the group's size so that cannot regress silently.
        """
        shown = []
        for k in rows:
            a_, b_ = ROWS_HERE.get(k, {}), ROWS_THERE.get(k, {})
            pa, pb = a_.get("covering_pairs") or {}, b_.get("covering_pairs") or {}
            _nm = f"{k[1]} ({k[0]})" if k[1] in AMBIGUOUS_SYMS else k[1]
            per_row = []
            # Either side's covering_pairs, not their intersection: the flagged side of
            # MODULE_NOT_COVERING has no covering pairs at all, and that absence against
            # the other side's coverage is itself the content difference to show. A third
            # term intersecting the two `modules` lists was inert - a module in neither
            # side's covering_pairs yields two empty term sets and is skipped - and
            # operator precedence made it an intersection rather than part of the union.
            for m in sorted(set(pa) | set(pb)):
                ta = {t for t, _ in pa.get(m) or ()}
                tb = {t for t, _ in pb.get(m) or ()}
                if ta != tb:
                    def _f(ts):
                        return ", ".join(f"`{t}`" for t in sorted(ts)) or "nothing"
                    # No break: a row with two modules would otherwise show one
                    # difference and read as the whole of it. Inert today, every row in
                    # this group being single-module.
                    per_row.append(f"`{m}` covers {_f(ta)} here and {_f(tb)} there")
            if per_row:
                shown.append(f"{_nm}: " + ", and ".join(per_row))
        # Asserted, not hoped for: a member with no differing module in covering_pairs
        # would be dropped with no count, which is the show-fewer-than-claimed shape this
        # per-group change was made to remove.
        # Unconditional: `shown and ...` exempted the all-empty case, which is the worst
        # form of the defect rather than the mild one - no row having a recorded difference
        # prints the cause for the group with nothing after it. Reachable, since load() does
        # not require covering_pairs and a report predating it gives every row an empty map.
        if len(shown) != len(rows):
            sys.exit(f"cover_evidence shows {len(shown)} of {len(rows)} rows attributed to "
                     f"differing module contents for {flag}; the page would assert the cause "
                     "for the group and show it for a subset")
        return (" - " + "; ".join(shown)) if shown else ""

    def show_rows(rows, cap=8):
        """Name rows, adding the entry where the symbol alone is ambiguous.

        Ambiguity is read from AMBIGUOUS_SYMS, which is every symbol holding more than one
        row anywhere in either report - not every symbol repeated within the movement being
        described. Scoping it to the movement left a gene with rows in three entries bare
        wherever only one of them moved, so the same page printed HADH disambiguated under
        one flag and bare two bullets later under another.

        The cap applies per cause rather than per side, so a small group - the
        module-contents and module-set causes this page argues from - is enumerable
        rather than being a count with examples. It is still a cap: six groups on this
        run exceed eight and print the remainder ("and 70 more"), because inlining 78
        symbols would bury the causes the section exists to separate.
        """
        out = ", ".join(f"{g} ({e})" if g in AMBIGUOUS_SYMS else g
                        for e, g, _ in rows[:cap])
        return out + (f", and {len(rows) - cap} more" if len(rows) > cap else "")

    def movement(flag):
        """Row-level accounting for a flag whose rows moved.

        The shape of the sentence is derived, not fixed. Five of the nine flags on this
        run move in one direction only, and for those the net count is an exact summary -
        telling the reader it was misleading would be a finding manufactured by the
        template. Only a flag with both departures and arrivals has a net that hides
        something.
        """
        a_, b_ = flag_rows(rep, flag), flag_rows(ALT_REP, flag)
        left, came, shared = sorted(a_ - b_), sorted(b_ - a_), a_ & b_
        if not left and not came:
            return None
        bits = []
        for label, rows, other_idx, mine_idx in (
                ("left", left, ROWS_THERE, ROWS_HERE),
                ("arrived", came, ROWS_HERE, ROWS_THERE)):
            if not rows:
                continue
            by = {}
            for k in rows:
                by.setdefault(move_cause(flag, mine_idx.get(k, {}), other_idx.get(k, {})),
                              []).append(k)
            parts = []
            for c, v in sorted(by.items(), key=lambda kv: -len(kv[1])):
                part = f"{len(v)} because {c} ({show_rows(v)})"
                if c == "the same modules carry different terms":
                    part += cover_evidence(flag, v)
                parts.append(part)
            bits.append(f"{len(rows)} {label} - " + "; ".join(parts))
        head = (f"`{flag}` {there.get(flag, 0)} against {here.get(flag, 0)}")
        if left and came:
            head += (f" moves in both directions, so the net is not the movement:"
                     f" {len(shared)} rows carry it on both trees, ")
        else:
            head += (f" moves in one direction only, so the net count is exact:"
                     f" {len(shared)} rows carry it on both trees, ")
        return head + "; ".join(bits) + "."

    mods_here = (PROV.get("module_accessions") or {}).get("modules_read")
    mods_there = (ALT_PROV.get("module_accessions") or {}).get("modules_read")
    # Each risen flag is explained by the group it belongs to, read from the report rather
    # than inferred by subtraction. The previous version split the rises into "module
    # flags" and "everything else", and told the reader everything else counted *absent*
    # reviews - wrong for AIGR_NOT_COMPLETE and NO_CORE_FUNCTION_TERMS, which fire where a
    # review was found, and so wrong for 85 of 87 rows in the run it was written against.
    groups = ALT_PROV.get("_flag_groups")
    if "_flag_groups" not in ALT_PROV:
        sys.exit("the second report has no flag_groups; it was produced by a superseded "
                 "align_audit.py and its risen flags cannot be explained - re-run the audit")
    if not groups:
        # Present but empty is a separate failure from absent, and unlike term_aspects it is
        # never legitimate: without the groups every risen flag falls through to "cause not
        # established", which would read as a finding rather than as a broken input.
        sys.exit("the second report's flag_groups is empty; every risen flag would be reported "
                 "as unexplained rather than grouped - re-run the audit")
    if "_term_aspects" not in ALT_PROV:
        # Not read for the cross-aspect figures, which come from the primary report, but a
        # second report missing it is a superseded one and the two are then not comparable.
        sys.exit("the second report has no term_aspects; it was produced by a superseded "
                 "align_audit.py - re-run the audit")
    absent = tuple(groups.get("review_absent") or ())
    thin = tuple(groups.get("review_present_thin") or ())
    modular = tuple(groups.get("module_sourced") or ())
    rose_absent = [f for f in rose if f in absent]
    rose_thin = [f for f in rose if f in thin]
    rose_mod = [f for f in rose if f in modular]
    rose_other = [f for f in rose if f not in absent + thin + modular]

    def names(fs):
        return ", ".join(f"`{f}`" for f in fs)

    out = [
        "The audit also runs over a second tree, and comparing the two runs shows which flags",
        f"are artifacts of the missing slices rather than findings. That tree is {ALT_TREE}.",
        "Both cover the same",
        f"{n_here} gene rows. Flags that fall: {pairs(fell)}. Flags that rise: {pairs(rose)}.",
        # Its own sentence, not a clause appended to the tree description, where it landed
        # several clauses away from the revision it qualifies and repeated that revision.
        f"That second run read a tree recorded{_alt_drift_tail()}",
        "",
        "Every movement below is accounted for row by row rather than from the net counts: a"
        " flag's total can fall while rows arrive at it, and each row's cause is read from that"
        " row's own record on **both** trees, not from the flag's group. Where a flag moves in"
        " one direction only the net count is exact, and the line says so rather than implying"
        " the count was misleading.",
    ]
    for f in fell:
        line = movement(f)
        if line:
            out += ["", f"- {line}"]
    if rose:
        out += ["", "The rises, on the same basis:"]
    for f in rose:
        line = movement(f)
        if line:
            out += ["", f"- {line}"]
    out += ["", "The groups below say where in the audit each flag is computed, which is why"
                " those causes are the ones available to it - not why any particular row moved."]
    if rose_absent:
        out += ["", f"- {names(rose_absent)} counts rows with no review at all. This is the only"
                    " risen flag the missing slices raise directly."]
    if rose_thin:
        verb = "fire" if len(rose_thin) > 1 else "fires"
        out += ["", f"- {names(rose_thin)} {verb} where a review **was** found and is thin: a stub"
                    " status, or no core-function terms to compare against. These count stub"
                    " reviews present on the second tree, not reviews missing from it - a"
                    " different claim, and the larger share of the movement."]
    if rose_mod:
        _mw = {1: "The one module flag is", 2: "Both module flags are"}.get(
            len(modular), f"All {len(modular)} module flags are")
        line = (f"- {names(rose_mod)} cannot have either cause. {_mw} computed"
                " only once a review has been found, so a missing review **removes** one rather"
                " than adding it. Which module fact moved each row is in the accounting above,"
                " per row, rather than asserted for the group here; what follows is only the"
                " shape of the two module sets:")
        if mods_here and mods_there:
            # The direction is read, not assumed: a second run with more modules would have
            # printed "so fewer are available" as a fact. Same unchecked-direction shape the
            # nesting clause below had removed in round 5.
            _dir = ("fewer are available to cover a gene's aligned terms"
                    if mods_there < mods_here else
                    "more are available, so this flag's rise is not a shortage of modules"
                    if mods_there > mods_here else
                    "the same number is available, so a count difference is not the driver")
            line += (f" the second run reads {mods_there} modules against {mods_here} here, so"
                     f" {_dir}.")
        # Nesting is a set question, not a count question: 448 < 451 is equally consistent
        # with the smaller tree being a subset. Derived from the recorded module lists, and
        # simply not claimed when a report does not carry them.
        here_mods = set(PROV.get("modules") or ())
        there_mods = set(ALT_PROV.get("modules") or ())
        if here_mods and there_mods:
            only_there = sorted(there_mods - here_mods)
            only_here = sorted(here_mods - there_mods)
            if only_there and only_here:
                line += (f" The two sets are not nested either way: {len(only_here)} modules are"
                         f" here and not there, and {len(only_there)} there and not here"
                         f" (e.g. `{only_here[0]}` and `{only_there[0]}`).")
            elif only_here:
                line += (f" The second set is a strict subset **by name**: {len(only_here)} modules"
                         f" are here and not there (e.g. `{only_here[0]}`), and none the other way."
                         " provenance.modules records stems, so that says nothing about the"
                         " contents of a module present in both - and the row accounting above"
                         " attributes some arrivals to shared modules whose own terms differ, so"
                         " the names are nested while the contents are not.")
            elif only_there:
                line += (f" This set is the strict subset: {len(only_there)} modules are there and"
                         f" not here (e.g. `{only_there[0]}`).")
            else:
                line += " The two runs read the same module set, so the counts above must differ for another reason."
        else:
            line += (" Whether the two module sets are nested is not derivable here, since at"
                     " least one report does not record which modules it read.")
        out += ["", line]
    if rose_other:
        # Not silently folded into one of the groups above: an unclassified flag would
        # otherwise inherit whichever explanation it happened to land next to.
        out += ["", f"- {names(rose_other)} is not in any group this page knows how to explain;"
                    " its cause has not been established here."]
    steady = sorted(f for f in set(here) | set(there)
                    if f not in indep and here.get(f, 0) == there.get(f, 0) and here.get(f, 0))
    if steady:
        steady_mod = [f for f in steady if f in modular]
        steady_rev = [f for f in steady if f not in modular]
        verb = "are" if len(steady) > 1 else "is"
        out += ["", f"{names(steady)} {verb} identical in **total** in both runs while depending"
                    " on a review, so they appear in neither list above. An equal total is not an"
                    " equal set of rows, and the difference matters here, so each is compared row"
                    " by row below rather than read off the count."]
        # Counts only say the totals match. Whether the same rows carry the flag is a
        # different question, asked here rather than inferred - and asked before any
        # interpretation is offered, because "a stable property of the dismech side" is not
        # even available as a reading for a flag whose rows moved.
        same_rows, moved_rows = [], []
        for f in steady:
            (same_rows if flag_rows(rep, f) == flag_rows(ALT_REP, f) else moved_rows).append(f)
        if same_rows:
            out += ["", f"{names(same_rows)} {'are' if len(same_rows) > 1 else 'is'} identical row"
                        " for row as well: the same rows, keyed by entry, gene and occurrence,"
                        " carry the flag on each tree."]
            _sr = [f for f in same_rows if f in steady_rev]
            for f in _sr:
                # "A stable property of the dismech side" is not an available reading for a
                # review-sourced flag - round 4 removed ALIGNED_CONTRIBUTES_ONLY from
                # REVIEW_INDEPENDENT_FLAGS for exactly that reason - and the reports answer
                # the question outright, so neither branch of the old hedge was needed.
                _rows = sorted(flag_rows(rep, f))
                _diff, _same_ctb = [], []
                for k in _rows:
                    _a, _b = ROWS_HERE.get(k, {}), ROWS_THERE.get(k, {})
                    if _a.get("aigr_status") != _b.get("aigr_status"):
                        _diff.append((k, _a.get("aigr_status"), _b.get("aigr_status")))
                    if (_a.get("aligned_via_contributes_to") or []) == \
                            (_b.get("aligned_via_contributes_to") or []):
                        _same_ctb.append(k)
                line = (f"`{f}` is review-sourced, so a stable count there cannot be a property"
                        " of the dismech side either.")
                if _diff:
                    k, sa, sb = _diff[0]
                    line += (f" The reviews are not even the same: {k[1]} is `{sa}` here and"
                             f" `{sb}` on the second tree.")
                if len(_same_ctb) == len(_rows) and _rows:
                    _t = (ROWS_HERE.get(_rows[0], {}).get("aligned_via_contributes_to") or [])
                    line += (" What is stable is the contributes-to term the row aligns on"
                             + (f", `{_t[0]}` for {_rows[0][1]}" if _t else "")
                             + ", which both reports record identically - so the flag survives a"
                               " change in the review around it.")
                out += [line]
        for f in moved_rows:
            line = movement(f)
            if line:
                # Same accounting as the risen and fallen flags, because an equal total is
                # the case where reading the group instead of the rows is least visible:
                # nothing in the counts suggests anything moved at all.
                out += ["", f"{line} So the equal total is a coincidence of two populations,"
                            " and nothing about stability follows from it."]
        if steady_mod and not moved_rows:
            # Only sayable once the row sets have been compared, which is why it is here
            # rather than attached to the count.
            out += [f"{names(steady_mod)} is module-sourced, so a count stable across two"
                    " different module sets would otherwise prove nothing; here the rows are"
                    " the same ones, which does mean their covering modules are present in both"
                    " trees."]
    out += [
        "",
        "The flags decided before any review is read are identical in both runs",
        f"({', '.join('`%s` %d' % (f, here.get(f, 0)) for f in indep)}), which is what separates",
        "missing inputs from the script behaving differently - and that identity is enforced",
        "rather than stated: the generator exits if one of those counts moves, or if the two runs",
        "do not cover the same rows. So a second run tests that the audit works; the figures",
        "on the project page come from the tree holding every reviewed gene, which with all",
        "ten slices merged is this branch itself.",
        "",
    ]
    return out

# Recorded justifications for flags that are deliberate, keyed (entry, gene) or (entry, None).
NOTES = {
    ("Inborn_Disorder_of_Bile_Acid_Synthesis", None): "Grouping-like entry; genes are carried by its subtypes.",
    ("Triglyceride_Storage_Disease_Type_1", None): "Historical OMIM:190420 phenotype; no gene has been reported (ABHD5 content lives in Dorfman_Chanarin_Disease).",
    ("Vitamin_D-Dependent_Rickets_Type_2B", None): "Genetic basis unknown; HNRNPC is modelled as a mechanism actor, not a causal gene.",
}
# Keyed by gene symbol. Every principal row carrying a module flag must appear here, or
# the run fails: the page claims each such gene has a stated reason, so that claim is
# enforced rather than asserted. A key may name several genes separated by " / ".
MODULE_REASONS = {
    "TRMT10C": "RNase P partners (HSD17B10, PRORP, ELAC2) lack completed reviews.",
    "ANGPTL3": "No LPL / plasma triglyceride clearance module; LPL review still DRAFT.",
    "CTNS": "Lysosomal cystine export is a single step.",
    "SLC26A1": "Epithelial oxalate/sulfate transport has no coherent multi-part module yet; SLC26A1's oxalate role is contested.",
    "SLC26A6": "As SLC26A1; a two-part oxalate-transport module is possible later.",
    "DMP1": "No module contains DMP1 as a part. It is named in the notes of fgf23_klotho_phosphate_homeostasis as regulatory context, which this audit deliberately does not count as membership, and its mechanism is undefined.",
    "SLC10A7": "Single gene with unknown transported substrate.",
    "DNAJC30": "Complex I N-module repair is not assembly; no repair module exists.",
    "LCT": "Brush-border disaccharide digestion: only LCT has a completed review (SI, MGAM, TREH missing).",
    "HNF1A / HNF4A": "Transcription factors whose hyperinsulinism and MODY roles act through many target genes; no beta-cell transcriptional-network module exists yet.",
    "SLC16A1": "Disease mechanism is ectopic beta-cell expression of a transporter whose normal role (lactate/pyruvate transport) belongs to no beta-cell pathway; a monocarboxylate-transport module would not include the disease mechanism.",
    "SIM1": "Transcription factor needed for paraventricular hypothalamic neuron development and function; it acts on, rather than within, the leptin_melanocortin_signaling module, whose parts are the ligand, processing and receptor steps.",
    "MT-TL1 / MT-TQ / MT-TH / MT-TK / MT-TC / MT-TS1 / MT-TS2 / MT-TV / MT-TW / MT-TM": "No mitochondrial translation module exists; in mitochondrial_trna_charging_and_initiator_formylation a tRNA would appear only as a synthetase substrate, which the substrate guidance excludes, and module parts are UniProt proteins.",
    "UCP2": "Causal role disputed (relationship DISPUTED); its transported substrate is itself contested.",
    "AIFM1": "The aligned function is the mitochondrial disulfide relay (CHCHD4 anchoring); no module covers the relay. AIFM1 is a part of apoptotic_execution_phase, whose AIFM1 annoton carries DNA binding, nucleus and positive regulation of apoptotic process: a different AIFM1 activity, and not the encephalomyopathy mechanism.",
    "APOB": "The aligned term is GO:0034379 very-low-density lipoprotein particle assembly, and there is no VLDL-assembly module. APOB is a part of chylomicron_assembly_secretion, whose scope is GO:0034378 chylomicron assembly, and of ldl_receptor_mediated_endocytosis, which is about the receptor taking the particle up. GO:0034378 and GO:0034379 are siblings, not one inside the other, so the hepatic VLDL step is genuinely unmodelled. APOB's other row, the LDL-receptor-binding one, is covered.",
    "NUBPL": "The aligned term is GO:0016226 iron-sulfur cluster assembly. NUBPL is a part of complex_i_assembly_factors, whose scope is GO:0032981 mitochondrial respiratory chain complex I assembly: NUBPL delivers an Fe-S cluster to the assembling complex, and the cluster's own assembly is a different process that no module covers.",
    "NDUFA1": "A limitation of the coverage test rather than a modelling gap, and left flagged rather than waived. The module is the right one; the cause is an asymmetry in how the two sides may say the same thing. The dismech node binds GO:0008137 NADH dehydrogenase (ubiquinone) activity, which the review carries as contributes_to_molecular_function, so the row aligns. complex_i_accessory_subunits says the identical relation the GO-idiomatic way, giving its NDUFA1 annoton GO:0005198 structural molecule activity as part of complex I, and GO:0005198 does not relate to GO:0008137 by is_a/part_of ancestry: a structural role and the activity it supports are different branches of molecular function. Coverage accepts a contributes-to term from the review but has no way to read the module\'s structural-plus-part_of idiom as the same claim. (The module also declares GO:0006120 as its process scope, which ancestry does not reach from GO:0008137 either - but that is a fact about this particular pair, not about the aspects: is_a/part_of does cross between molecular function and biological process, and MT-ND1 in this same table aligns GO:0008137 to GO:1902600 by doing so. Either way the aspect question is not what decides this row.)",
}
# Read from the run rather than kept here: a hardcoded pair went stale the moment the audit
# added PARTIAL_COVERAGE to module_sourced, leaving alt_comparison reading the triple while
# the reasons enforcement and the "(not covering)" marker read the pair.
MODULE_FLAGS = tuple((PROV.get("_flag_groups") or {}).get("module_sourced") or ())
if not MODULE_FLAGS:
    sys.exit("the report records no module_sourced flag group; it was produced by a "
             "superseded align_audit.py - re-run the audit")
# Which module flags oblige a hand-written reason. PARTIAL_COVERAGE does not, and the page
# now says so rather than leaving it to be inferred from the constant: the other two are
# verdicts about a module ("none contains this gene", "one does and misses its function")
# that only a reader of the module can justify, whereas PARTIAL_COVERAGE reports which
# aligned terms no module term reached, and the row prints them. The distinction is
# obligation, not importance.
REASON_REQUIRING_MODULE_FLAGS = tuple(
    (PROV.get("_flag_groups") or {}).get("module_sourced_reason_required") or ())
if not REASON_REQUIRING_MODULE_FLAGS:
    sys.exit("the report records no module_sourced_reason_required flag group; it was "
             "produced by a superseded align_audit.py - re-run the audit")
# Flags that qualify a row rather than mark it defective. PARTIAL_ALIGNMENT,
# ALIGNED_CONTRIBUTES_ONLY and ALIGNED_ON_SHARED_NODE_ONLY are counted and reported
# individually below rather than folded into one "clean" figure, because each is a way
# the test can be weaker than the row looks.
QUALIFYING = ("PARTIAL_ALIGNMENT", "ALIGNED_CONTRIBUTES_ONLY",
              "ALIGNED_ON_SHARED_NODE_ONLY", "PARTIAL_COVERAGE")
# Read from the run, not built here from MODULE_FLAGS: deriving it made "soft" the
# default for any module flag the audit added later, so a flag marking a real
# contradiction would have been absorbed into the clean count with nothing failing.
SOFT = tuple((PROV.get("_flag_groups") or {}).get("soft") or ())
if not SOFT:
    sys.exit("the report records no soft flag group; it was produced by a superseded "
             "align_audit.py - re-run the audit")
# The page names these three in prose, so a run whose soft set stopped containing them
# would print a sentence its own figures contradict.
_missing_soft = [f for f in ("ALIGNED_NONCORE", "ALIGNED_PROPOSED") + QUALIFYING
                 if f not in SOFT]
if _missing_soft:
    sys.exit(f"the report's soft flag group omits {', '.join(_missing_soft)}, which this "
             "page describes as tolerated by the clean count - re-run the audit or amend "
             "the prose")

# Flag glossary, keyed on the flag name. Checked against the flags the run actually
# emitted rather than hand-maintained beside them: PARTIAL_COVERAGE was published on 14
# rows and defined nowhere, because the previous legend was prose carrying its own
# arithmetic ("the last seven are informational") that counted an older vocabulary.
FLAG_GLOSS = {
    "UNTYPED": "the dismech genetic record carries no relationship type",
    "NO_ORIGIN": "the dismech genetic record carries no variant origin",
    "GENE_ON_NO_NODE": "no pathophysiology node names the gene",
    "NO_GO_ON_GENE_NODES": "no node naming the gene carries a GO term",
    "NO_AIGR_REVIEW": "no ai-gene-review review exists for the gene",
    "AIGR_NOT_COMPLETE": "a review exists but its status is not COMPLETE",
    "NO_CORE_FUNCTION_TERMS": "a review exists but has no core-function GO term to compare against",
    "NO_GO_ALIGNMENT": "no node term matches a core function, an annotation the review keeps, or a term it proposes",
    "ALIGNED_NONCORE": "node terms match only annotations the review keeps as non-core",
    "ALIGNED_PROPOSED": "node terms match only terms the review proposes as NEW, which are not yet annotations",
    "PARTIAL_ALIGNMENT": "some node terms aligned and others matched nothing in the review",
    "ALIGNED_CONTRIBUTES_ONLY": "every aligned term matched only a contributes-to function, not an enabled one",
    "ALIGNED_ON_SHARED_NODE_ONLY": "every aligned term came from a node the gene shares with another gene",
    "NO_MODULE_MEMBERSHIP": "no module contains the gene's accession",
    "MODULE_NOT_COVERING": "a module contains it, but no annoton term there relates to the aligned terms",
    "PARTIAL_COVERAGE": "a module covers some aligned terms and no module term reaches the rest",
}


def flag_legend():
    """The whole glossary as bullets, grouped, enforcing that every emitted flag is defined.

    Prints every entry rather than only the emitted ones. Filtering to what the primary
    report emits was a regression: it dropped the definitions of four flags the page's own
    prose names, NO_GO_ALIGNMENT among them - the headline negative result - so the fix for
    one undefined flag left four more undefined. A flag the run does not emit is still a
    flag a reader meets in the text, and the glossary is small enough to print whole.

    Enforcement runs the other way and over both reports, since a flag emitted by either
    would be published without a definition.
    """
    emitted = {f for src in (rep, ALT_REP) for e in src for g in e.get("genes") or []
               for f in g.get("flags") or []}
    missing = sorted(emitted - set(FLAG_GLOSS))
    if missing:
        sys.exit(f"flags emitted by a run with no entry in FLAG_GLOSS: {', '.join(missing)}; "
                 "they would be published in the table and the summary with no definition")
    # Ordered by the groups the comparison section argues from, not alphabetically, so the
    # legend carries the same structure as the explanation.
    groups = PROV.get("_flag_groups") or {}
    order, seen = [], set()
    for key in ("review_independent", "review_absent", "review_present_thin", "module_sourced"):
        for f in groups.get(key) or []:
            if f in FLAG_GLOSS and f not in seen:
                order.append(f); seen.add(f)
    order += [f for f in sorted(FLAG_GLOSS) if f not in seen]
    out = []
    for f in order:
        mark = " *(qualifying)*" if f in QUALIFYING else ""
        # "either" is only true when there are two runs. With one report ALT_REP is empty,
        # so the claim would cover a run this page has not read - and the branch-local
        # report does emit NO_CORE_FUNCTION_TERMS, which such a page would deny.
        _scope = "either run" if ALT_PATH else "this run"
        note = "" if f in emitted else f" - not emitted by {_scope}"
        out.append(f"- `{f}`{mark} - {FLAG_GLOSS[f]}{note}")
    return out


# Written into both this page's frontmatter and the self-check sub-page's. render-projects
# reads `species_hints` from each page's own frontmatter, so a sub-page without it leaves
# every symbol that exists in more than one species unlinked - ODC1, COX20 and COQ2 are all
# human and yeast. One constant rather than two literals, so the two cannot diverge and
# silently unlink those symbols again.
SPECIES_FRONTMATTER = "species: [human]"

lines = [
    "---",
    "title: dismech metabolic disorders aligned with ai-gene-review",
    "maturity: IN_PROGRESS",
    "description: Per-entry check that dismech metabolic disease mechanisms agree with ai-gene-review core functions and modules",
    SPECIES_FRONTMATTER,
]

from collections import Counter

# Suggestion from review: ALIGNED_ON_SHARED_NODE_ONLY fires on a large minority of rows, so
# the page says how many of them align on a term the review asserts in its own right. An
# identical node/core term means the shared node is not what earned the match.
def _shared_node_split(entries):
    """Rows flagged shared-node-only, split by how much of the row is self-identical.

    Two figures, because they license different claims. `some` counts a row with at
    least one node term identical to a core term; `all` counts a row where every
    aligned term is. The inference "the shared node is not doing the work" holds for
    the identical terms only, so a row in `some` but not `all` still has partner-derived
    matches carrying part of its verdict.
    """
    tot = some = every = 0
    for e in entries:
        for g in e.get("genes") or []:
            if g.get("relationship") not in (None, "CAUSATIVE"):
                continue
            if "ALIGNED_ON_SHARED_NODE_ONLY" not in (g.get("flags") or []):
                continue
            tot += 1
            pairs_ = (g.get("aligned_pairs") or {}).items()
            hits = [t in (v if isinstance(v, list) else [v]) for t, v in pairs_]
            if any(hits):
                some += 1
            if hits and all(hits):
                every += 1
    return tot, some, every


n_shared, n_shared_exact, n_shared_all = _shared_node_split(rep)
def cross_aspect_rows(entries, aspects):
    """Matched pairs whose two terms sit in different GO aspects.

    Derived rather than named. The page used to cite three examples in prose; when the
    input tree changed, one of them (SLC16A1) stopped being cross-aspect and the sentence
    became false while reading exactly as before. A pair counts only where both aspects
    are known and differ, and a row is only listed where it has no same-aspect pair of
    its own, since otherwise the crossing is not what earned the row.
    """
    sole, any_ = [], 0
    for e in entries:
        for g in e.get("genes") or []:
            crossings, same = [], False
            for t, v in (g.get("aligned_pairs") or {}).items():
                for c in (v if isinstance(v, list) else [v]):
                    a, b = aspects.get(t), aspects.get(c)
                    if a and b and a != b:
                        crossings.append((t, c, a, b))
                    elif a and b:
                        same = True
            if crossings:
                any_ += 1
                if not same:
                    sole.append((g["gene"], crossings[0]))
    return sole, any_


TERM_ASPECTS = PROV.get("_term_aspects")
if TERM_ASPECTS == {}:
    # An empty map is what a run with no matched pairs legitimately produces, which is a
    # different thing from a report that predates the field.
    print("note: the report records term_aspects as empty, so this run matched no pairs")
if TERM_ASPECTS is None:
    # Without aspects the cross-aspect figures are zero, and zero renders as "no matched
    # pair crosses the aspects" - a lookup failure or an old report printing as a finding.
    sys.exit("the report has no term_aspects key at all; it was produced by a superseded "
             "align_audit.py and the cross-aspect figures would read as an absence rather "
             "than as missing data - re-run the audit")
_n_all_rows = sum(1 for e in rep for g in e.get('genes') or [])
_ca_sole, _ca_any = cross_aspect_rows(rep, TERM_ASPECTS)
if _ca_sole:
    _g, (_t, _c, _a, _b) = _ca_sole[0]
    _cross_aspect_sentence = (
        f"{_ca_any} rows of all {_n_all_rows} - not only the principal ones - carry at least one such"
        f" pair, and on {len(_ca_sole)} of them the row has no"
        f" same-aspect pair at all, so the crossing is what earns the verdict - {_g} matches"
        f" `{_t}` ({_a}) to `{_c}` ({_b}).")
elif _ca_any:
    _cross_aspect_sentence = (
        f"{_ca_any} rows of all {_n_all_rows} carry at least one such pair, though every one also has a"
        " same-aspect pair, so on this run the crossing never decides a row by itself.")
else:
    _cross_aspect_sentence = (
        "On this run no matched pair crosses the aspects, so nothing here depends on it.")

# The audit records terms it could place under no single aspect root. They are a gap in the
# figures above - a pair involving one is neither crossing nor same-aspect - so the page
# states them rather than leaving the count to read as complete. Written unconditionally by
# the audit, so an absent key is a superseded report and an empty list is a clean run.
_unres = PROV.get("aspect_unresolved")
if _unres is None:
    sys.exit("the report has no aspect_unresolved key; it was produced by a superseded "
             "align_audit.py and the cross-aspect figures would read as covering every term")
if _unres:
    _cross_aspect_sentence += (
        f" {len(_unres)} term(s) sit under no single aspect root and are outside both figures"
        f" ({', '.join('`%s`' % t for t in _unres[:5])}"
        + (", ..." if len(_unres) > 5 else "") + ").")

# Whitelist, so a renamed or new dismech relationship value does not silently become
# principal and inflate the clean count.
PRINCIPAL_RELATIONSHIPS = (None, "CAUSATIVE")
principal = lambda g: g.get("relationship") in PRINCIPAL_RELATIONSHIPS
# Scale of the third membership/coverage state, derived rather than written, for the bullet below.
_n_partial_cov = sum(1 for e in rep for g in e.get("genes", [])
                     if principal(g) and "PARTIAL_COVERAGE" in g["flags"])

# Only genes the audit actually matched to a review. Listing every symbol in the report
# would count modifier and susceptibility genes with no review (SAR1A, APOA5, SH2B1,
# NCOA1, TYK2) toward this project's gene coverage in the all-projects table, and
# `resolve_frontmatter_gene_links` leaves an unresolvable symbol silently unlinked.
reviewed_genes = sorted({g["gene"] for e in rep for g in e.get("genes", [])
                         if g.get("aigr_status")})
lines += [
    "genes: [" + ", ".join(reviewed_genes) + "]",
    "---",
    "",
    "# dismech metabolic disorders aligned with ai-gene-review",
    "",
    "This page records, for every dismech metabolic disorder in scope, whether the causal gene's",
    "dysfunction as modelled in the dismech pathograph agrees with the gene's normal function in its",
    "ai-gene-review review, and whether the gene sits in an ai-gene-review module.",
    "",
    "**Scope.** dismech entries with Harrison's chapter `ENDOCRINOLOGY_METABOLISM` or a metabolic",
    "`category`, excluding primarily endocrine-gland, autoimmune, complex, neoplastic and gynecologic",
    "conditions, plus two entries created in this work (Mitchell syndrome, SLC26A1-related hypersulfaturia).",
    "",
    "**Method.** For each gene bound in an entry's `genetic` records, the GO molecular functions and",
    "biological processes on the pathograph nodes naming that gene are compared with the gene's",
    "ai-gene-review core functions. The audit script (`align_audit.py`), the page generator",
    "(`make_page.py`), the entry list (`scope.yaml`) and the committed report of the run behind this",
    f"table (`report.yaml`) are in the `projects/DISMECH_METABOLIC_ALIGNMENT/` directory of the"
    + (" repository, with `check_page_guards.py` exercising the generator's refusals"
       " (`just check-alignment-page-guards`, also run by the pytest suite), together"
       " with the second report the audit self-check page beside this one"
       " ([audit-self-check](DISMECH_METABOLIC_ALIGNMENT/audit-self-check.md)) is derived from"
       f" (`{os.path.basename(ALT_PATH)}`), the same audit run over `{ALT_TREE_SHORT}`."
       if ALT_PATH else
       " repository. Run with only the report, as here, the generator deletes any"
       " self-check page beside this one: with no second run there is nothing to"
       " reconcile, and a left-behind copy would keep publishing an earlier run's"
       " figures with nothing linking to it."),
    "",
    "**What \"aligned\" does and does not claim.** Five properties of the test make it a weak",
    "check, and any of them can turn a row green that a curator would not:",
    "",
    "- The relation is **symmetric** and **unbounded in distance**. A node term counts as aligned",
    "  when either it or the core term is an is_a/part_of ancestor of the other, at any depth. So a",
    "  dismech node bound to something broad aligns with a specific core function, and the reverse,",
    "  and two terms many levels apart still align. The table therefore prints the core term each",
    "  node term matched (`node->core`, or the term alone where the two are identical), so the",
    "  distance behind a match is visible per row. `DMP1 | GO:0005509` (calcium ion binding) is the",
    "  clearest row where the verdict carries little information; reading a row as agreement means",
    "  reading its pair.",
    "- A dismech node binds its GO terms **at node level**, and a node may name several genes.",
    "  dismech has no per-gene attribution inside a node, so every term on a shared node is read",
    "  for every gene on it, and a row can align on a co-named partner's activity. The column",
    "  marks such a term `s`, and `ALIGNED_ON_SHARED_NODE_ONLY` fires where *every* term a row",
    "  aligned on came from a shared node. The hyperinsulinism node naming both GLUD1 and HADH,",
    "  which carries glutamate dehydrogenase activity and enzyme inhibitor activity together, is",
    "  the case to read: each gene is credited with both, and here that happens to be right in",
    "  both directions (HADH does inhibit GLUD1), which is exactly why it needs marking rather",
    "  than trusting. The flag is conservative by construction and fires on a large minority of",
    f"  rows, so read it with this alongside: of the {n_shared} principal rows it fires on,",
    f"  {n_shared_all} align **only** on node terms identical to one of the gene's own core",
    "  functions, so the review asserts each of those activities in its own right and the shared",
    f"  node earned none of the match. A further {n_shared_exact - n_shared_all} have at least one",
    "  such identical term but not all of them, so part of the verdict still rests on a",
    f"  partner-derived term, and {n_shared - n_shared_exact} have none at all. GLUD1 and its",
    "  `GO:0004353` are of the first shape. Only the identical terms license reading the flag as",
    "  harmless, which is why the three figures are given separately rather than summed.",
    "- `contributes_to_molecular_function` is compared **alongside** core molecular function. A",
    "  subunit that contributes to a complex-level activity without enabling it is doing what the",
    "  dismech node describes, so excluding it would lose real agreement; but it is a weaker claim,",
    "  so a term matched only that way is marked `c` and `ALIGNED_CONTRIBUTES_ONLY` fires where a",
    "  row's whole alignment rests on one.",
    "- Node MF and BP terms are compared against **one pooled set** of the review's core molecular",
    "  functions and `directly_involved_in` processes, so a node activity term can be satisfied by",
    "  a core process and the reverse. Such a match is genuine agreement but weaker than a",
    "  same-aspect one; the cross-aspect paragraph below gives the figures and a worked row.",
    "- Module **membership** is not module **coverage**. Membership says the gene is a part of some",
    "  module; coverage says a module is about the function the row aligned on, which is a different",
    "  and stronger claim. They are flagged separately in three states: `NO_MODULE_MEMBERSHIP` means",
    "  no module contains the gene; `MODULE_NOT_COVERING` means one does but no term anywhere in any",
    "  of those modules is related to the aligned terms, and such a module is marked",
    f"  `(not covering)` in the Modules column; and `PARTIAL_COVERAGE` ({_n_partial_cov} principal",
    "  rows) means a module covers some of the aligned terms while no module term reaches the rest,",
    "  which the Modules column names term by term after `- uncovered:`. The third state is not a",
    "  defect to fix: a module is scoped to a process, so it will often reach the aligned term that",
    "  names that process and not a second term naming a different activity of the same gene.",
    "  AIFM1 is the row `MODULE_NOT_COVERING` exists to catch: it sits",
    "  in `apoptotic_execution_phase`, whose AIFM1 annoton carries DNA binding, nucleus and",
    "  positive regulation of apoptotic process, while the aligned function is the mitochondrial",
    "  disulfide relay. No module covers the relay.",
    "",
    "Coverage reads the module's declared `concepts`, at module level and per node, as well as its",
    "annotons' terms: a module states its scope as processes while its annotons carry the molecular",
    "functions of individual parts, so annotons alone miss what the module is about. One limitation",
    "survives that and is left visible rather than waived: coverage is asymmetric about complex",
    "membership. It accepts a `contributes_to_molecular_function` term from the review, but cannot",
    "read a module's GO-idiomatic way of saying the same thing - a subunit given `GO:0005198`",
    "structural molecule activity as part of the complex - as the same claim, because a structural",
    "role and the activity it supports are unrelated branches of molecular function. NDUFA1 is the",
    "row where that decides the verdict.",
    "",
    "`is_a`/`part_of` ancestry does cross between molecular function and biological process, and",
    "that crossing is a real source of alignment here: GO asserts `part_of` from transporter",
    "activities to the transport processes they carry out.",
    _cross_aspect_sentence,
    "Where a particular pair does not meet, that is a fact about the pair rather than about the",
    "aspects - `GO:0008137` does not reach `GO:0006120`. Two things follow. Cross-aspect",
    "`part_of` is a real source of",
    "alignment in this table, not an artefact - and since node MF and BP terms are compared against",
    "one pooled set of the review's core molecular functions and `directly_involved_in` processes,",
    "a node activity term can be satisfied by a core process and the reverse. Such a match is",
    "genuine agreement but weaker than a same-aspect one, and `aligned_pairs` records which core",
    "term each node term matched so a reader can see which shape any given row is.",
    "",
    "Membership is read from the module structure (`parts[].node.annotons[]`, following the",
    "participant whichever selector it uses - `gene_product`, `gene`, `ortholog_of`, `homolog_of`,",
    "a `FAMILY` participant's `representative_members`, and a protein complex's `active_units`) and",
    "following nested parts and variant sets, so a gene named only in a module's notes or evidence",
    "does not count as a part. The run records both counts in its provenance below, so the gap",
    "between reading the structure and reading the file text is a measured figure rather than a",
    "quoted one.",
    "",
    "Flags, with the qualifying ones marked - a qualifying flag says the verdict is weaker than",
    "`ok` would suggest, so those are counted separately below rather than absorbed into one",
    "clean figure:",
    "",
] + flag_legend() + [
    "",
]
# The two-run comparison, computed once and read twice: by the provenance section's link
# below and by the self-check write at the end. Bound here rather than at either use so it
# exists whether or not PROV does.
_self_check = alt_comparison()

if PROV:
    lines += [
        "**Provenance of this run.** The table is generated, so it is only as current as the inputs it",
        "was generated from, and those inputs live in two repositories.",
        "",
        f"- run date: `{PROV.get('run_date') or 'unrecorded'}`",
        f"- dismech revision: `{PROV.get('dismech_revision') or 'unrecorded'}`"
        + (f" ({PROV['dismech_describe']})" if PROV.get("dismech_describe") else ""),
        f"- ai-gene-review revision: `{PROV.get('aigr_revision') or 'unrecorded'}`"
        # "HEAD" is what git reports for a detached checkout, so printing it as a branch
        # names a non-branch beside the aigr_tree line that gives the real answer.
        + (" (detached checkout, so no branch name)" if PROV.get("aigr_branch") == "HEAD"
           else f" (branch `{PROV['aigr_branch']}`)" if PROV.get("aigr_branch") else ""),
        f"- GO release: `{PROV.get('go_version') or 'unrecorded'}`, adapter `{PROV.get('go_adapter') or 'unrecorded'}`",
    ]
    _ad = PROV.get("audit_revision") or "unrecorded"
    _ah = PROV.get("audit_sha256") or "unrecorded"
    _DIRT_NAMES = {"audit_dirty": "the audit script itself",
                   "aigr_dirty": "the ai-gene-review tree",
                   "dismech_dirty": "the dismech tree"}
    # Three states, not two. None means git could not answer, and treating it as False -
    # which `if PROV.get(k)` did - published an unanswerable tree as a clean one, which is
    # the assertion the audit-side fix was made to stop. Rendered separately.
    # Four states, not three. PROV.get(k) returns None both for a run whose git could not
    # answer and for a report produced before these fields existed, so a stale report would
    # have published a confident claim about a git failure that never happened. Presence in
    # the mapping separates them, the same distinction this round applied to flag_groups,
    # term_aspects and aspect_unresolved.
    _dirt = [v for k, v in _DIRT_NAMES.items() if PROV.get(k) is True]
    _unknown = [v for k, v in _DIRT_NAMES.items() if k in PROV and PROV[k] is None]
    _unrecorded = [v for k, v in _DIRT_NAMES.items() if k not in PROV]
    # Where the companion run answers the same question for the same script, say so rather
    # than leaving "not established" standing next to a report that holds the answer.
    _alt_dirt = (f"; the companion run over {ALT_PROV.get('aigr_branch') or 'the second tree'}"
                 f" records the audit script as {'modified' if ALT_PROV.get('audit_dirty') else 'clean'}"
                 " at the same sha256"
                 if ALT_PROV.get("audit_sha256") == PROV.get("audit_sha256")
                 and "audit_dirty" in ALT_PROV and ALT_PROV["audit_dirty"] is not None
                 and PROV.get("audit_dirty") is None and "audit_dirty" in PROV else "")
    lines.append(
        f"- audit script: `{_ah}` (sha256 of `align_audit.py`), last committed at `{_ad}`"
        + ("; unrecorded because the project directory has no history in the tree that was"
           " read, which is the case for a scratch tree the script was copied into, so the"
           " sha256 is the identifier to use" if _ad == "unrecorded" else "")
        + (f"; **uncommitted changes at run time in: {', '.join(_dirt)}**, so the revisions"
           " above name commits that are not exactly what ran" if _dirt else "")
        + (f"; **git could not be asked about: {', '.join(_unknown)}**, so whether the revisions"
           f" above name what ran is not established either way{_alt_dirt}" if _unknown else "")
        + (f"; this report does not record whether {', '.join(_unrecorded)} had uncommitted"
           " changes, so nothing is claimed either way" if _unrecorded else "")
    )
    if PROV.get("aigr_tree"):
        lines.append(f"- ai-gene-review tree: {PROV['aigr_tree']}")
    # The description-names-its-revision guard for both reports runs at import, beside
    # ALT_TREE, rather than here: it was primary-only while it lived in this function.
    # Outside alt_comparison(), which returns nothing without a second report: this is a
    # claim about the primary report alone, and the table renders from it either way.
    lines.append(f"- {_primary_drift_tail()}")
    _ma = PROV.get("module_accessions") or {}
    if _ma:
        lines.append(
            f"- modules read: `{_ma.get('modules_read')}`; UniProt accessions reached as parts:"
            f" `{_ma.get('accessions_as_parts')}`, against `{_ma.get('accessions_in_file_text')}`"
            " matching the accession pattern anywhere in the module file text. Both are sums over"
            " modules of that module's distinct accessions, so a protein in several modules counts"
            " once per module; the difference is accessions mentioned in notes or evidence of a"
            " module they are not a part of, which this audit does not count as membership."
        )
    lines += [
        "",
        "The gene reviews and modules this table asserts `COMPLETE` for are on `main`: the ten",
        "themed PRs split out of #4690 have all merged, so an ordinary checkout holds them.",
    ]
    if PROV.get("aigr_tree"):
        lines.append(f"The run above read {PROV['aigr_tree']}.")
    elif PROV.get("aigr_dirty") is False:
        # A clean checkout needs no tree description: the revision above is the whole
        # answer, and saying otherwise would report a complete provenance as incomplete.
        lines.append(
            "The run above read a clean checkout, so the revision above describes its tree"
            " in full."
        )
    else:
        # No guessing from aigr_dir. The previous version inferred "this was a scratch
        # directory" from the path not starting with /home, which asserted two things the
        # provenance does not record and was false for any ordinary checkout.
        lines.append(
            "That run's provenance records no `aigr_tree`, so it does not say how its tree was"
            " built - only the revision and directory above. Set `AIGR_TREE` when running the"
            " audit over a tree that is not a plain checkout."
        )
    lines.append("")
    # The two-run comparison is a statement about this generator, not about dismech/AIGR
    # agreement, and it names individual rows and stub statuses. It goes to its own page
    # under the projects/FOO/ convention; only a link to it belongs here.
    #
    # Computed once, here rather than at the write below, for two reasons. It is the whole
    # row-level accounting, so asking it twice to answer "is there a second report" repeats
    # that work; and its own guards exit on a report that cannot be compared, which has to
    # happen before the page is written rather than after.
    if _self_check:
        lines.append(
            "The same audit was run a second time over a different tree, and the two runs'"
            " flag counts are reconciled row by row in"
            " [the audit self-check](DISMECH_METABOLIC_ALIGNMENT/audit-self-check.md). That"
            " is a check on the generator rather than a finding about the two resources, so"
            " it is kept beside the page rather than in it."
        )


def aligned_cell(g):
    """Node term with the core term it matched, so an unbounded match is visible.

    Every match is shown where a node term relates to more than one core term: picking
    one would show the alphabetically smallest GO id, which need not be the nearest.
    A term matched only through `contributes_to_molecular_function` is marked, and so is
    one held only because another gene shares the node it came from.
    """
    pairs = g.get("aligned_pairs") or {}
    terms = g.get("aligned_terms") or []
    if not terms:
        return "-"
    contrib = set(g.get("aligned_via_contributes_to") or [])
    shared = set(g.get("shared_node_terms") or [])
    cells = []
    for t in terms:
        c = pairs.get(t)
        cs = c if isinstance(c, list) else [c]
        cs = [x for x in cs if x is not None]
        if not cs or cs == [t]:
            cell = t
        else:
            cell = f"{t}&rarr;" + "/".join(cs)
        marks = ("c" if t in contrib else "") + ("s" if t in shared else "")
        cells.append(cell + (f" <sup>{marks}</sup>" if marks else ""))
    return " ".join(cells)


def unaligned_cell(g):
    """Node terms that matched no core function: the half that shows disagreement."""
    terms = g.get("dismech_only") or []
    if not terms:
        return "-"
    shared = set(g.get("shared_node_terms") or [])
    return " ".join(t + " <sup>s</sup>" if t in shared else t for t in terms)


def modules_cell(g):
    """Modules the gene is a part of, linked, marking a non-covering one only when flagged.

    `(not covering)` used to print on any module outside `covering_modules`, including on
    rows carrying no flag, where it only means the gene's other module is about its other
    function. Marking it only where `MODULE_NOT_COVERING` fires keeps it to the rows the
    page has a stated reason for.
    """
    mods = g.get("modules") or []
    if not mods:
        return "-"
    pairs_ = g.get("covering_pairs") or {}

    def link(m):
        # Which module term earned the coverage, as the Aligned column shows which core
        # term earned the alignment. Coverage is tested against every term anywhere in a
        # module, so without the pair a reader cannot tell a relevant match from a remote
        # ancestor of one.
        cell = f"[{m}](../modules/{m}.html)"
        hits = pairs_.get(m) or []
        if hits:
            # Formatted here rather than in the report, so the uncovered set is derived
            # from the pairs themselves instead of by re-parsing a display string.
            shown = [f"{t}->{mt}" for t, mt in hits[:2]]
            cell += " (" + ", ".join(shown) + (", ..." if len(hits) > 2 else "") + ")"
        return cell

    cov = g.get("covering_modules") or []
    flags_ = g.get("flags") or []
    out = " ".join(link(m) if m in cov or "MODULE_NOT_COVERING" not in flags_
                   else f"[{m}](../modules/{m}.html) (not covering)" for m in mods)
    if "PARTIAL_COVERAGE" in flags_:
        # Coverage is existential, so a covered row can still leave aligned terms that no
        # module term reached. Named here rather than left to the flag alone.
        unc = g.get("uncovered_aligned_terms") or []
        out += " - uncovered: " + " ".join(unc[:3]) + (" ..." if len(unc) > 3 else "")
    return out


c = Counter(f for e in rep for g in e.get("genes", []) if principal(g) for f in g["flags"])
n_rows = sum(1 for e in rep for g in e.get("genes", []) if principal(g))
n_clean = sum(1 for e in rep for g in e.get("genes", [])
              if principal(g) and not [f for f in g["flags"] if f not in SOFT])
n_partial = sum(1 for e in rep for g in e.get("genes", [])
                if principal(g) and "PARTIAL_ALIGNMENT" in g["flags"])
n_full = sum(1 for e in rep for g in e.get("genes", [])
             if principal(g) and g.get("aligned_terms") and not g.get("dismech_only"))
n_untyped = sum(1 for e in rep for g in e.get("genes", [])
                if principal(g) and g.get("relationship") is None)
# The whitelist admits untyped rows defensively, but saying "causative and untyped" when a
# run holds none of the latter describes the predicate rather than the table.
_principal_desc = (f"causative and untyped; {n_untyped} untyped" if n_untyped
                   else "all causative in this run; the predicate also admits untyped")
lines += [
    f"**Summary.** {len(rep)} entries; {n_rows} principal gene rows ({_principal_desc}), of"
    f" which {n_full} align every GO term their dismech nodes carry and {n_partial} align some"
    " and leave others unaligned. Read that split first: the flag-free count below is close to"
    " true by construction, because `NO_GO_ALIGNMENT` is the only hard flag while"
    " `PARTIAL_ALIGNMENT`, `ALIGNED_ON_SHARED_NODE_ONLY` and `PARTIAL_COVERAGE` are all soft,"
    " so it is not a measure of full agreement.",
    "",
    f"{n_clean} principal rows carry no flag other than a module flag or one of the qualifying"
    " flags - none"
    " carries `NO_GO_ALIGNMENT`, `NO_CORE_FUNCTION_TERMS`, `NO_GO_ON_GENE_NODES` or"
    " `GENE_ON_NO_NODE`. That count also tolerates `ALIGNED_NONCORE` and `ALIGNED_PROPOSED`,"
    " which say a row aligned only against a retained non-core or a proposed term rather than"
    " a core function; no principal row in this run carries either."
    + (" Flag counts on principal rows: " + ", ".join(f"`{k}` {v}" for k, v in sorted(c.items()))
       # Only worth saying when the provenance section printed all-row counts to compare with.
       + (". These are principal rows only, so they are smaller than the all-row counts in the"
          " provenance section above wherever a flag also falls on a modifier, susceptibility"
          " or disputed row." if ALT_REP else ".")
       if c else " No principal row carries a flag."),
    "",
    f"**Agreement is partial on many rows, and the table shows both halves.** {n_full} principal",
    f"rows align every GO term their dismech nodes carry; {n_partial} align some and leave others",
    "matching nothing in the gene review. A partial row is usually not a defect in either",
    "repository - it is dismech modelling a step of the disease mechanism that is not part of the",
    "gene's normal function, which is what the two resources are each for. `LCT` is the clearest",
    "case: the row aligns `GO:0000016` lactase activity and leaves `GO:0006366` transcription by",
    "RNA polymerase II unaligned, because the hypolactasia mechanism is the enhancer that switches",
    "the gene off, and transcribing its own gene is not a function of lactase. Reading such a row",
    "as full agreement would be wrong in the other direction, so the unaligned terms are printed",
    "rather than dropped.",
    "",
    "Polygenic entries (Type I diabetes) and modifier/susceptibility genes are",
    "listed but were not required to align: their genes are risk loci or modifiers, not the",
    "normal-function owners of a single pathway step.",
    "",
    "In the GO-term columns, <sup>c</sup> marks a term matched only through the review's",
    "`contributes_to_molecular_function`, and <sup>s</sup> a term the gene holds only because",
    "another gene is named on the same dismech node. Where a node term relates to several core",
    "terms, all of them are shown separated by `/`.",
    "",
    "| Entry | Gene | Relationship | AIGR | Aligned GO terms (node&rarr;core) | Unaligned node terms | Modules | Flags |",
    "|---|---|---|---|---|---|---|---|",
]
for e in rep:
    if not e.get("genes"):
        lines.append(f"| {e['entry']} | - | - | - | - | - | - | {e.get('problem','')}: {NOTES.get((e['entry'], None), '')} |")
        continue
    for g in e["genes"]:
        flags = ", ".join(g["flags"]) or "ok"
        lines.append(
            f"| {e['entry']} | {g['gene']} | {g.get('relationship') or '-'} | {g.get('aigr_status') or '-'} | "
            f"{aligned_cell(g)} | {unaligned_cell(g)} | {modules_cell(g)} | {flags} |"
        )
lines += [
    "",
    "## Notes on remaining flags",
    "",
    "- **No causative row carries `NO_GO_ALIGNMENT`**, which is the flag that would mark a real",
    "  contradiction: every causative gene has at least one node term matching a core function.",
    "  The flags causative rows do carry say something weaker. The three module flags",
    "  (`NO_MODULE_MEMBERSHIP`, `MODULE_NOT_COVERING`, `PARTIAL_COVERAGE`) are about what is",
    "  modelled elsewhere in ai-gene-review, not about this gene's function.",
    "  `PARTIAL_ALIGNMENT` marks non-overlap rather than conflict - dismech modelling a step the",
    "  gene's normal function does not include - and `ALIGNED_CONTRIBUTES_ONLY` and",
    "  `ALIGNED_ON_SHARED_NODE_ONLY` mark a match that rests on a weaker relation than the row",
    "  looks. `ALIGNED_NONCORE` falls only on UCP2, a DISPUTED gene that was never required to",
    "  align, as do the `NO_AIGR_REVIEW` and `AIGR_NOT_COMPLETE` rows.",
    "- **MELAS mtDNA genes**: MT-ND1, MT-ND5 and MT-ND6 have reviews and are parts of",
    "  mitochondrial_complex_i_core, aligning with the dismech complex I node (NADH:ubiquinone",
    "  oxidoreductase activity, DECREASED). The ten mt-tRNA genes (MT-TL1, MT-TQ, MT-TH, MT-TK,",
    "  MT-TC, MT-TS1, MT-TS2, MT-TV, MT-TW, MT-TM) have ncRNA reviews (RNAcentral ids) whose core",
    "  function, triplet codon-amino acid adaptor activity in mitochondrial translation, matches",
    "  the dismech translation-defect nodes.",
    "- **UCP2** (DISPUTED): dismech binds regulation of insulin secretion (GO:0050796), which",
    "  is the parent of a UCP2 annotation the review keeps as non-core (GO:0061179), so the row",
    "  is `ALIGNED_NONCORE`. dismech deliberately binds no UCP2",
    "  activity, because its causal role in hyperinsulinism and its transported substrate",
    "  are both disputed.",
    "- **TMEM251** is the dismech/HGNC-build label for the gene now named LYSET; it is matched to",
    "  the LYSET review.",
    "- **Type I diabetes risk loci** (PTPN22, IL2RA, CTLA4, IFIH1, BACH2, TNFAIP3, EGR2, IRF4, IKZF1,",
    "  TYK2) are SUSCEPTIBILITY records with no single pathway step; several ai-gene-review entries",
    "  for them are still drafts from other projects.",
]
# Which module flag each named gene actually carries, and whether its row is principal,
# so the list cannot read as "these causative genes are all in a module that misses their
# function" when most of them are in no module at all and one is not causative.
flag_by_gene, principal_genes = {}, set()
for e in rep:
    for g in e.get("genes", []):
        for f in g["flags"]:
            if f in REASON_REQUIRING_MODULE_FLAGS:
                flag_by_gene.setdefault(g["gene"], set()).add(f)
        if principal(g):
            principal_genes.add(g["gene"])

lines += ["", "## Genes with a module flag, and why", "",
          "`NO_MODULE_MEMBERSHIP` means no module contains the gene; `MODULE_NOT_COVERING` means",
          "one does but nothing in it is about the function the row aligned on. Rows that are not",
          "causative are marked, since they were never required to align. `PARTIAL_COVERAGE` is",
          "the third module flag and is deliberately absent from this list: it reports which of a",
          "row's aligned terms a module reached and which it did not, so the covering pairs and the",
          "`- uncovered:` list in the Modules column already say everything a hand-written reason",
          "could, and the generator",
          "does not require one. The distinction is obligation, not importance.", ""]
# Which entries each named gene's flagged rows are in, so a multi-row gene in this list is
# as locatable as one in the movement accounting. Hand-keyed display strings do not pass
# through show_rows, so APOB, SLC16A1 and HNF4A were named bare here while the accounting
# above disambiguated them.
_reason_entries = {}
for _e in rep:
    for _g in _e.get("genes") or []:
        # The enforced set, not all module flags: the list this labels is enforced over
        # REASON_REQUIRING_MODULE_FLAGS, so keying on the wider set would print an entry
        # whose row the reason beside it does not cover.
        if [f for f in (_g.get("flags") or ()) if f in REASON_REQUIRING_MODULE_FLAGS]:
            _reason_entries.setdefault(_g.get("gene"), []).append(_e.get("entry"))
for k, v in MODULE_REASONS.items():
    names = [n.strip() for n in k.split("/")]
    k = " / ".join(
        f"{n} ({', '.join(sorted(_reason_entries.get(n, [])))})"
        if n in AMBIGUOUS_SYMS and _reason_entries.get(n) else n
        for n in names)
    fl = sorted({f for n in names for f in flag_by_gene.get(n, ())})
    tag = ", ".join(f"`{f}`" for f in fl) or "`no module flag on this run`"
    if names and not any(n in principal_genes for n in names):
        tag += ", not causative"
    lines.append(f"- **{k}** ({tag}): {v}")

# Enforce the claim above in both directions: every principal row carrying a module flag
# must have a reason, and every reason must still name a gene that carries one. The
# unused side used to compare against every gene in the report, so a reason that had
# stopped applying lingered silently.
covered = {g.strip() for key in MODULE_REASONS for g in key.split("/")}
missing = sorted({g["gene"] for e in rep for g in e.get("genes", [])
                  if principal(g)
                  and [f for f in g["flags"] if f in REASON_REQUIRING_MODULE_FLAGS]} - covered)
if missing:
    sys.exit("MODULE_REASONS has no entry for principal rows flagged "
             f"{'/'.join(REASON_REQUIRING_MODULE_FLAGS)}: {', '.join(missing)}")
unused = sorted(covered - set(flag_by_gene))
if unused:
    sys.exit("MODULE_REASONS names genes that carry no module flag on this run, so the "
             f"stated reason no longer applies: {', '.join(unused)}")

open(out, "w").write("\n".join(lines) + "\n")

# The self-check page, written beside the project page under the projects/FOO/ convention.
# With no second report there is nothing to compare, and the page's link to it is dropped
# too - so any committed copy is removed rather than left behind. Not writing one was not
# enough: render-projects walks the whole projects/ tree, so the stale file kept publishing
# its previous run's row-level figures with nothing linking to it.
_sc_path = os.path.join(os.path.dirname(os.path.abspath(out)),
                        "DISMECH_METABOLIC_ALIGNMENT", "audit-self-check.md")
if not _self_check and os.path.exists(_sc_path):
    os.remove(_sc_path)
    print("removed stale", _sc_path, "- no second report to compare")
if _self_check:
    os.makedirs(os.path.dirname(_sc_path), exist_ok=True)
    open(_sc_path, "w").write("\n".join([
        # No `maturity:`, unlike the project page: render_projects_table collects
        # top-level pages only, so a sub-page is not a row in the all-projects table and
        # has no status column to fill. `species:` is shared with the page above through
        # one constant, for the reason recorded there.
        "---",
        "title: 'dismech metabolic alignment: audit self-check'",
        "description: Two runs of the same audit reconciled flag by flag, as a check on the"
        " generator",
        SPECIES_FRONTMATTER,
        "---",
        "",
        "# DISMECH metabolic alignment: audit self-check",
        "",
        "[Back to the project page](../DISMECH_METABOLIC_ALIGNMENT.md)",
        "",
        "This page reconciles two runs of the same audit over different trees. It is a check"
        " on the generator - that the flags which should not depend on which gene reviews"
        " exist do not - and not a finding about how dismech and ai-gene-review agree. It"
        " names individual rows and review statuses for that reason.",
        "",
    ] + ([
        # The mirror of the clause the provenance section uses for the primary: leaving
        # "not established" to stand next to a run holding the answer for the same sha256
        # says less than is known.
        #
        # No gloss on *why* the second run has no answer. `_dirty` returns None for any git
        # failure, so the absence alone cannot name its cause - the same reason the
        # `not_here` branch refuses to say why an object is missing. What the report does
        # establish is narrower and is stated instead: `aigr_dirty` is an answer from the
        # same `git status` in the same directory, differing only in the pathspec that
        # names the script, so git answered for the audited tree and not for the script.
        f"The second run records no answer for whether `align_audit.py` was modified when"
        f" it ran"
        + ("" if ALT_PROV.get("aigr_dirty") is None else
           f", though git answered for the audited tree itself:"
           f" {'modified' if ALT_PROV.get('aigr_dirty') else 'clean'}. Both runs record the"
           f" same script (`{PROV.get('audit_sha256')}`), in which the two answers come"
           f" from one command in one directory differing only in the pathspec that names"
           f" the script - which is why `audit_revision` is unrecorded for that run as"
           f" well")
        + f". The primary run answers it:"
          f" {'modified' if PROV.get('audit_dirty') else 'clean'}.",
        "",
    ] if ALT_PROV.get("audit_dirty") is None
         and PROV.get("audit_dirty") is not None
         and ALT_PROV.get("audit_sha256") == PROV.get("audit_sha256") else [])
    + _self_check) + "\n")
    print("wrote", _sc_path)
print("wrote", out, n_rows, n_clean)
