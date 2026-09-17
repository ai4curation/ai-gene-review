# AKAP12 bioinformatics

Three scripts, all reproducible from files already in this repo. No network access
and no API keys are required; each derives the repo root itself rather than
hardcoding a worktree path.

**Run everything with `uv run python`, not bare `python3`.** The only third-party
dependency is `pyyaml`, which the repository's own `pyproject.toml` already provides, so
these scripts deliberately do *not* carry a nested `uv init` project — a second project
here would duplicate that dependency and pin it separately from the repo. `uv run` from
anywhere in the tree resolves the repo environment, which is all these need.

This matters concretely: the system `python3` on macOS is 3.9 and dies with
`TypeError: unsupported operand type(s) for |` on the `X | Y` annotations here. That
traceback is a *tooling* failure, not an analysis result — do not read it as the audit
finding a problem, and do not report quotes or counts as checked from a run that ended
that way.

## `akap12_motifs.py`

Tests whether the PKC-binding motifs reported for rodent SSeCKS
(`PMID:21903576`) actually occur in the **human** Q02952 sequence, and whether
they coincide with the UniProt-annotated AKAP CaM-binding (WSK) motifs.

The published motif windows are given in rodent numbering, so the script does not
transfer the coordinates. It searches the human sequence with the published
consensus expressed as a regex and reports where it genuinely matches.

```bash
uv run python akap12_motifs.py ../AKAP12-uniprot.txt
```

Output is committed as `motifs.out`.

## `akap12_audit.py`

Structural assertions over the parsed review document — action counts, 1:1
correspondence with the GOA rows, which GO ids the `MODIFY` rows may propose, and
that the retracted `PMID:27683220` keeps `is_invalid: true` and is never cited as
support.

```bash
python3 akap12_audit.py     # exit 0 = all assertions hold
```

The assertions are **structural**, computed from the parsed YAML. An earlier
version asserted a hand-chosen occurrence threshold ("`GO:0034237` appears at
least 4 times") that could not fire, because the term also appears in prose.

## `akap12_audit_selftest.py`

Mutation test for the audit. It perturbs the review document one defect at a time and
asserts the audit **fails** on each, with the expected message.

Each mutant is written to a **tempfile** and `akap12_audit.py` is pointed at it via its
optional path argument; the curated review file is never written, and the script asserts
that at the end. An earlier version mutated the real file in place and restored it in a
`finally`, which meant an interrupted run could leave deliberately corrupted YAML in the
working tree — a test must not be able to damage the artifact it is testing.

Two entries are **controls** that must *not* trip the audit, so a guard that fires on
everything is caught too.

```bash
python3 akap12_audit_selftest.py
```

This exists because a check that passes on a broken document is worse than no
check: it converts an unverified claim into an apparently verified one. The
self-test is what caught the unfireable threshold described above.
