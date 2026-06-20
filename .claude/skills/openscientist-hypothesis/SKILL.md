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

## After Completion

- Verify the generated report does not include withheld local bioinformatics
  paths or `RESULTS.md` content.
- Compare the OpenScientist conclusion against the held-out local bioinformatics
  result after the run.
- Keep operational lessons in skills or agent instructions, not in user-facing
  project pages.
