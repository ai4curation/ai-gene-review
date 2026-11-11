# Merge queue

The queue tests approved PRs against current `main` on a temporary integration
commit. It leaves the reviewed PR head unchanged, avoiding branch-update pushes
that dismiss approval and trigger another review. It does not accelerate an
individual validation job or supply missing reviews, and integration builds still
consume Actions capacity.

This follows [dismech's queue implementation](https://github.com/monarch-initiative/dismech/blob/main/.github/workflows/main.yaml),
with **up to eight concurrent integration builds**, one PR per merge, and up to **50 total
queue entries** admitted by the shepherd. Each sweep attempts at most **50
admissions**, including failed attempts. Waiting entries do not increase build
concurrency. The summary distinguishes the observed entry limit from the attempt
budget and includes the counts for whichever limit stopped admission. The scheduled
job also stops starting new PRs after 30 minutes (`--time-budget-seconds 1800`,
inside its 45-minute job timeout) so a long sweep still writes its summary. Manual admissions
can exceed the shepherd's queue-size limit; GitHub's build-concurrency limit still
applies. Existing approval and `test (3.12)` branch protection remain in force.

## CI coverage

`Build and test` handles `merge_group` with the same required check name. The paths
filter understands the merge group, so changed-gene, prediction and reference
checks use integration changes. Every group also runs the complete test suite,
example tests, automation checks, all gene schemas, module/family checks and history
validation. Validation-infrastructure changes retain full gene validation.
Repo-wide literature/ontology revalidation and upstream PAINT verification retain
their scheduled/manual coverage. This avoids refetching all literature per merge.

Validation and tests run concurrently in the `validation (3.12)` and
`suite (3.12)` jobs, each with its own checkout. Both use the same path rules in
`.github/ci-path-filters.yaml`. The test job skips dependency setup when no tests
are selected; merge groups always run the full suite. Only the validation job
saves ontology, PANTHER and UniProt data caches; the test job can restore them
but cannot publish data modified by fixtures.

The final `test (3.12)` job retains the existing branch-protection context and
requires **both** jobs to succeed. It runs even if a worker fails, is cancelled,
or is skipped, and rejects all those outcomes. No branch-protection setting
needs to change. Splitting adds a second checkout and runner, trading some
Actions minutes for a shorter critical path; compare merge-group wall time
before and after rollout rather than adding the two job durations.

Superseded PR and main-push runs are cancelled. Integration, scheduled and manual
runs have unique concurrency groups. Queue CI failure is blocking; GitHub removes
the failing entry.

## Shepherd admission

The deterministic controller discovers queue configuration and all entries before
processing PRs. An unreadable, partial or inconsistent response aborts without
writes, including before queue rollout in direct-merge mode. A GraphQL outage can
therefore make the shepherd fail without merging anything. It skips queued PRs,
preserves the existing age, review, exact-head, file,
assignment, hold-label and required-check guards, and repeats verification before
writing. The enqueue mutation pins `expectedHeadOid` and never falls back to direct
merge. Only write subprocesses receive the dedicated merge credential.

As in dismech, two `failed_checks` queue removals after the current head's commit
timestamp stop automated retries. The latest 100 removal events are examined; one
retry is allowed for transient/collateral failures. This is a timestamp heuristic,
not an event-to-SHA mapping, so restored old commits or unusual commit timestamps
may need manual investigation. Unreadable removal history holds the candidate.
A maintainer can investigate and explicitly enqueue a held head; new commits must
earn review/check approval again. Already queued PRs are left alone by the agent.

## Rollout and operation

1. Merge the workflow/controller changes before enabling the rule. Existing PRs do
   not need rebasing to receive the current-main workflow on their queue commit.
   They still need the normal review and PR checks before admission.
2. Run the controller in its default audit mode and inspect the summary:

   ```sh
   uv run python scripts/auto_merge_ready_prs.py --repo ai4curation/ai-gene-review \
     --required-check 'test (3.12)' --dry-run
   ```

3. Apply [the ruleset](../.github/merge-queue-ruleset.yaml) through GitHub's repository
   rulesets API/UI, preserving existing branch protection and live bypass actors.
   Build concurrency is eight, `ALLGREEN`, squash merges, with a 360-minute check timeout
   to accommodate runner waits that have already exceeded two hours. This bounds
   waiting; it does not guarantee completion during a prolonged backlog.
   Before creating it, check for an existing `merge-queue-main` rule to avoid duplicates.
4. Verify an approved PR enters the queue, receives `test (3.12)` on its merge-group
   SHA, and merges after success. Watch queue-build duration, ejections and Actions
   backlog when tuning concurrency. Eight groups can use up to sixteen runners
   for `validation (3.12)` and `suite (3.12)`. Each short-lived `test (3.12)`
   gate starts only after both workers finish, so it does not add a third
   simultaneous runner per group. Superseded builds still finishing and other
   Actions workloads can consume additional runners.
   Earlier failures or queue jumps can require rebuilding later speculative groups.

The eight-build rollout relies on GitHub's native merge-queue checks:
`ALLGREEN` requires passing checks for every entry, and `max_entries_to_merge: 1`
keeps merges to one PR each. GitHub's documented failure handling rebuilds later
groups without a failed earlier entry. This covers ordinary speculative-build
failures; it does not independently verify the content GitHub ultimately merges.
DisMech's [post-merge integrity monitor](https://github.com/monarch-initiative/dismech/blob/main/.github/workflows/verify-merge-integrity.yaml)
recomputes expected merge trees to detect content-corrupting merge anomalies that
can escape CI. We evaluated that distinction and are proceeding with eight builds
without porting this monitor in this change. The residual risk is explicit:
ai-gene-review has no equivalent independent merge-tree audit, and green checks
alone do not rule out such anomalies. `ALLGREEN` and single-PR merges do not
replace that additional detection.

As of 2026-10-19, the organization API reports ai4curation's plan as Free.
GitHub [documents a default limit of 20 concurrent standard hosted jobs](https://docs.github.com/en/actions/reference/limits#job-concurrency-limits-for-github-hosted-runners)
for that plan, leaving nominal headroom of four when all sixteen queue workers
are running. A support-granted limit increase has not been verified. PR checks,
reviews, other repositories, and lingering superseded builds share that headroom;
watch runner wait times and lower build concurrency if admission checks starve.

The template has no bypass actors; the live repository ruleset separately allows
administrators to bypass the queue. Preserve those live bypass actors when updating
build concurrency rather than replacing the whole ruleset with the template.

The removal-reason string for a queue timeout has not yet been observed here: inspect it on the first timeout
before changing retry policy. Currently only `failed_checks` removals count toward
the automated retry hold; manual re-enqueue after investigation does not require
pushing a new commit or dismissing an otherwise valid approval.

The shepherd automatically switches to enqueueing when the queue exists. It reports
queued PRs as queued, not merged. Both audit and execute modes use the same capacity
limits. Repository rollout flags still control whether the shepherd writes at all.

To pause automatic admissions, use the shepherd's existing audit/off mode; queued
entries continue through GitHub. To remove the queue requirement, disable its
ruleset, leaving existing branch protection intact. The controller then returns to
its previous direct-merge policy on the next sweep. A configuration change observed
during a sweep aborts that candidate's write so the next sweep can reassess.

GitHub's [merge queue documentation](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-a-merge-queue)
describes build concurrency and ejection behavior. Merge limits control merges;
they do not batch several CI builds into one.
