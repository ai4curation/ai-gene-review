---
name: openscientist-hypothesis
description: Use when running or wiring OpenScientist for AI Gene Review gene-function hypotheses, especially blinded comparisons against local bioinformatics analyses.
metadata:
  short-description: AIGR OpenScientist hypothesis workflow
---

# OpenScientist Hypothesis Workflow

Use this skill for AIGR work that runs, stages, or maintains OpenScientist
hypothesis jobs for gene function review.

## Core Rules

- Treat OpenScientist as an independent bioinformatics scientist exploring a
  hypothesis: gene `G` has function `F`.
- For existing annotations, prefer the neutral function-assignment mode:
  `--as-function-hypothesis`.
- Do not feed existing local `*-bioinformatics/RESULTS.md` analyses into
  OpenScientist prompts. Those are holdout evidence for post-run comparison.
- It is acceptable to pass bounded non-holdout review context, especially the
  selected term, original evidence reference, and a small number of relevant
  literature/deep-research references.
- Avoid sending every function for genes with large reviews; select the specific
  hypothesis being tested.

## Running Jobs

- Use the `just` recipes, not raw `deep-research-client`, for AIGR hypothesis
  jobs. The justfile carries project defaults such as OpenScientist iteration
  count.
- Be patient with OpenScientist. Jobs may run quietly for a long time before the
  local report is written.
- Do not interrupt a real OpenScientist run merely because the local wrapper is
  silent or the child process is sleeping.
- Check completed and running jobs at <https://www.openscientist.io/jobs> before
  deciding a job is stuck.
- One-iteration OpenScientist runs are smoke tests only. Real hypothesis jobs
  should use the project default of at least 3 iterations unless the user
  explicitly asks otherwise.

## Timeouts

- Give analyses ample time. Real 3-iteration runs commonly take ~50-70 minutes,
  and structural / fold-discovery jobs can run longer; they are cancelled
  mid-analysis if the timeout is too short (observed: a job cancelled at the
  upstream 3600s default after producing nothing).
- The `just` recipes now inject the maximum OpenScientist job timeout
  (`--param timeout=7200`, i.e. 2h) alongside `--param max_iterations=3`, and
  the wrapper's subprocess wall (`--timeout-seconds`, default 8100s) is kept
  above the job timeout so the child process is not killed first. If you ever
  bypass `just` and call the script directly, pass both: e.g.
  `-- --param max_iterations=3 --param timeout=7200` plus
  `--timeout-seconds 8100`. The two timeouts are independent — raising one
  without the other still cancels the run.
- 7200s is the API ceiling: `OpenScientistParams.timeout` is validated `le=7200`,
  so a larger value fails fast with a pydantic `less_than_equal` error and writes
  nothing. Do not exceed it.
- Do not lower these to "save time"; a too-short timeout wastes the whole run.
- When a job *still* hits the 7200s ceiling (common for human proteins asked a
  multi-faceted question), the fix is **scope, not time**: re-run with a single
  decisive analysis in the hypothesis (e.g. "Foldseek fold assignment" alone,
  not fold + disorder + motif + targeting) and/or `--param max_iterations=2`.
  Observed: C18orf21 7200s timeout -> 2708s when narrowed to Foldseek-only;
  HSPA12A/DNAJC28 likewise completed once narrowed. The paralog of a job that
  *did* finish (e.g. HSPA12B at 5208s) will usually finish on a plain retry —
  variance, not a hard limit.
- Scoping each hypothesis to one computable question up front (rather than a
  broad "characterize this gene") both avoids timeouts and gives cleaner,
  more decisive provenance.

## Failure Modes

- A job can exit 0 yet write no report. Always confirm `openscientist.md` (and
  the `openscientist_artifacts/` dir) actually exist before treating a run as
  done; an empty hypothesis directory means it failed.
- Two distinct failure signatures seen, both leaving an empty output dir:
  - `detail=... timed out after Ns ... has been cancelled` -> raise the timeout
    (see above) and re-run.
  - `detail=... Request ID: req_...` -> a transient OpenScientist-internal LLM
    error (their server-side agent call failed; the id is for their debugging).
    Re-run; if the same gene fails this way repeatedly, treat it as a
    persistent upstream issue, move on, and report it rather than retrying
    indefinitely.
- Remove the empty `GENE-hypotheses/<slug>/` directory before re-running so a
  failed attempt does not masquerade as a completed one.

## After Completion

- Verify the generated report does not include withheld local bioinformatics
  paths or `RESULTS.md` content.
- Compare the OpenScientist conclusion against the held-out local bioinformatics
  result after the run.
- Keep operational lessons in skills or agent instructions, not in user-facing
  project pages.

## Wiring Verdicts Into Reviews

- **A refuted *proposal* must be deleted, not set to `REMOVE`.** Validation
  enforces that annotations absent from GOA carry `action: NEW` (they are AI
  proposals, identifiable by having no `original_reference_id`). If a run refutes
  such a proposal, delete the annotation block *and* any `core_functions` entry
  built on it, and record the refutation in the `description` + an OpenScientist
  `file:` reference. `action: REMOVE` is only for real GOA annotations and will
  fail validation on a not-in-GOA term ("Found N annotations not in GOA").
- **Gate findings that depend on uncacheable references.** When a run's
  conclusion rests on very recent papers not in `publications/` (so their
  `supporting_text` cannot be verbatim-verified) and that you cannot otherwise
  confirm, record it as a clearly-labelled *lead* — keep the conservative
  existing annotation, note "not yet verified / PMIDs not cached", and cite the
  OpenScientist `file:` report — rather than asserting a new annotation. Verify,
  don't trust. (Example: C18orf21 -> RMP24 / RNase MRP, left as a lead pending
  primary-literature caching.)
- **Don't overstate disagreements.** Before wiring "the run overturns the prior
  review", check the primary data: the two analyses often *agree on the facts*
  (e.g. residues present) and differ only on *interpretation* (e.g. a PROSITE
  signature failure). Wire genuine standoffs as `UNDECIDED` with both lines of
  evidence and the decisive experiment, and do not import the run's secondary
  claims (e.g. a named degenerate paralog) unless corroborated by repo data.
- **Verbatim `supporting_text` gotchas:** plain (unquoted) YAML scalars cannot
  contain `": "` — single-quote any quote containing a colon-space (e.g.
  "Foldseek: zero ..."). The pre-edit hook catches these.

## Job Hygiene

- Background jobs are killed on container restart; the harness reports which.
  Check the `GENE-hypotheses/<slug>/` dir — if empty, clean it and re-launch.
- The API key is not persisted in the environment here; pass
  `OPENSCIENTIST_API_KEY` inline when calling the script directly. Wire it into
  the environment/setup config for reproducible `just` runs.
