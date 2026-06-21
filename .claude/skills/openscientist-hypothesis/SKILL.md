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
