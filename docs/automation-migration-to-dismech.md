# ai-gene-review automation: the dismech migration (as built)

This records how `ai-gene-review`'s GitHub Actions automation was brought up to
the state of `monarch-initiative/dismech`. The two repos share a common ancestor
(the agentic workflows were copied around 2026-07-03); dismech then had a
security-hardening and centralization pass that this repo has now received too.

The **security half** — getting off the exposed `PAT_FOR_PR` / `dragon-ai-agent`
machine account and onto short-lived GitHub App tokens — is the same remediation
dismech completed for the
[dragon-ai-agent PAT exposure incident](https://github.com/ai4curation/ai-security-private/blob/main/docs/incidents/2026-07-dragon-ai-agent-pat-exposure.md).
The *why*, and the sharp edges found along the way, live in the security repo:

> **[ai-security-private → docs/history/2026-07-25-dismech-pat-to-app-migration.md](https://github.com/ai4curation/ai-security-private/blob/main/docs/history/2026-07-25-dismech-pat-to-app-migration.md)**

This document is the ai-gene-review-specific *what*, and — for anyone doing the
same migration in a third repo — the things that were different here.

---

## The end state

| Area | Before | Now |
|---|---|---|
| **Write auth** | `PAT_FOR_PR` in 8 workflows | short-lived `ai4c-agent` App token; **no workflow references `PAT_FOR_PR`** |
| **`.git/config` exposure** | `persist-credentials: false` only in `main.yaml` | **every** checkout in the repo is non-persisting; pushers use `gh auth setup-git` |
| **Reviewer identity** | `claude-code-review` used the same `AI4C_AGENT` app as the writers | separate `ai4c-reviewer` App |
| **Model config** | 28 model IDs pinned across workflows, several stale | `.github/agent-config.yaml` + `resolve-agent-config`; Opus 5 / Sonnet 5; a test forbids re-pinning |
| **Cron cadence** | hand-edited `schedule:` per workflow | `.github/cron-profiles.yaml` + `just cron-profile <name>`, with an `off` kill switch |
| **Fork-PR injection** | nothing | `close-fork-prs.yml` closes fork PRs at the door |
| **Untrusted comments** | nothing | `untrusted-comment-guard.yml` + a deterministic trust gate |
| **Mention dispatch** | `ai.yml` and `dragon-ai.yml`, byte-identical, both firing | one `ai.yml`, keyword `@ai4c-agent please` (legacy alias kept) |
| **Run reports** | `echo "${{ ... }}"` — an injection sink | `env:` + `printf`, tilde-fenced |

The push path is verified end to end, not just statically: `generate-pages` ran
47 minutes on the migrated workflow and opened
[#2277](https://github.com/ai4curation/ai-gene-review/pull/2277) with
`git push --force-with-lease` authenticated by `gh auth setup-git`, committed as
`ai4c-agent[bot] <242316268+ai4c-agent[bot]@users.noreply.github.com>` with
nothing in `.git/config`.

Verification, all of which should stay empty/green:

```bash
# Repo-wide, not just .github/ — the justfile recipes that re-installed this
# secret were the real footgun. --exclude-dir=docs because this file quotes it.
grep -rn "secrets.PAT_FOR_PR" . --exclude-dir=docs --exclude-dir=.git   # -> empty

# Model pins, action-manifest expressions, per-CHECKOUT credential persistence
# (a per-file grep passes a file with two checkouts where only one is flagged,
# and misses composite actions entirely), and cron-profile drift.
uv run pytest tests/test_agent_config.py tests/test_agent_run_summary.py \
  tests/test_apply_cron_profile.py
just test-js                                  # trust gate
```

---

## What we changed, in the order it merged

| PR | What |
|---|---|
| [#2259](https://github.com/ai4curation/ai-gene-review/pull/2259) | prerequisite: three tests were already failing on `main` (see "a green main is not a green suite" below) |
| [#2246](https://github.com/ai4curation/ai-gene-review/pull/2246) | `pr-shepherd` → App token; `.github/agent-config.yaml` + `resolve-agent-config`; model-pin guard test |
| [#2276](https://github.com/ai4curation/ai-gene-review/pull/2276) | reviewer split: `claude-code-review` runs as `ai4c-reviewer` (review history on the superseded [#2247](https://github.com/ai4curation/ai-gene-review/pull/2247)) |
| [#2249](https://github.com/ai4curation/ai-gene-review/pull/2249) | `close-fork-prs`, `untrusted-comment-guard` + trust gate, `@claude` author gating |
| [#2253](https://github.com/ai4curation/ai-gene-review/pull/2253) | the four scanners → App token; run summaries read `execution_file` |
| [#2255](https://github.com/ai4curation/ai-gene-review/pull/2255) | retire the duplicated dragon-ai mention workflows |
| [#2260](https://github.com/ai4curation/ai-gene-review/pull/2260) | pages / warm-cache / weekly-compliance → App token; last `persist-credentials` gaps |
| [#2261](https://github.com/ai4curation/ai-gene-review/pull/2261) | cron profiles |

Landing a stack this deep has one trap worth naming: **do not merge with
`--delete-branch` while a downstream PR still points at the branch.** GitHub
auto-closes that PR, and refuses to reopen it if its head has been force-pushed
since — which it will have been, if you rebase between review rounds. #2247 was
lost that way. The order that works is merge → retarget the next PR to `main`
→ *then* delete the branch.

## Why this order

Asked six times in review, so it belongs in the record. The sequencing was not
arbitrary:

1. **Reviewer split as early as the stack allows — which was not first, and
   that cost something.** The intent was to land it before anything else, so
   every later PR would be reviewed by an identity distinct from the one writing
   it. It did not work out: the reviewer-split PR was *stacked on* the
   pr-shepherd PR, so pr-shepherd had to merge first. #2259 (02:31Z) and #2246
   (04:35Z) therefore merged before the split (04:52Z), and both were
   self-reviewed — `gh pr view 2246 --json reviews` returns three reviews, all by
   `ai4c-agent`, the authoring App. Everything after was independently reviewed,
   and that reviewer went on to find a 🔴 and several 🟡s the author's own tests
   did not. **The lesson is to make the reviewer split the base of the stack,
   not the second entry** — otherwise you silently choose which PRs get
   self-reviewed, and they will be the foundational ones.
2. **Injection controls before the scanners.** `close-fork-prs` and the
   untrusted-comment guard reduce what can reach an agent's context; they should
   be in place before more agents get write-capable tokens, not after.
3. **Auth per workflow group, smallest blast radius first.** `pr-shepherd` alone,
   then the four scanners, then the mention responder, then the page/cache jobs.
   Each group is independently revertible, and a mistake in one does not strand
   the others.
4. **Teardown last, and it means more than the secret.** The `PAT_FOR_PR` secret
   is the obvious item, but the `just` recipes that *re-install* it are the ones
   that matter: while those existed, a single `just gh-add-secrets` could undo
   the whole migration. Remove the ability to recreate the credential before
   congratulating yourself on removing the credential.

Cron profiles came last because they are cadence, not security, and applying
them is behaviour-preserving.

## The token pattern

Every write-capable workflow now looks like this:

```yaml
permissions:
  contents: read        # scopes the DEFAULT token; the App token does the work

steps:
  - name: Generate ai4c-agent token
    id: ai4c-token
    uses: actions/create-github-app-token@bcd2ba49218906704ab6c1aa796996da409d3eb1 # v3.2.0
    with:
      app-id: ${{ secrets.AI4C_AGENT_APP_ID }}
      private-key: ${{ secrets.AI4C_AGENT_PRIVATE_KEY }}

  - name: Checkout repository
    uses: actions/checkout@v7
    with:
      token: ${{ steps.ai4c-token.outputs.token }}
      persist-credentials: false        # <-- closes the incident exposure vector

  - name: Configure git identity and credential helper
    env:
      GH_TOKEN: ${{ steps.ai4c-token.outputs.token }}
      APP_SLUG: ${{ steps.ai4c-token.outputs.app-slug }}
    run: |
      APP_USER_ID="$(gh api "/users/${APP_SLUG}[bot]" --jq .id)"
      git config --global user.name "${APP_SLUG}[bot]"
      git config --global user.email "${APP_USER_ID}+${APP_SLUG}[bot]@users.noreply.github.com"
      gh auth setup-git

  - name: Run agent
    uses: anthropics/claude-code-action@be7b93b1907a4abad570368f3c74b6fe3807510b # v1
    env:
      GH_TOKEN: ${{ steps.ai4c-token.outputs.token }}
      GITHUB_TOKEN: ${{ steps.ai4c-token.outputs.token }}
    with:
      github_token: ${{ steps.ai4c-token.outputs.token }}
```

`timeout-minutes: 55` goes with it: an App installation token expires 60 minutes
after minting and does not refresh, so a longer job can finish its analysis and
then 401 on every push.

---

## A green `main` is not a green suite

Worth knowing before you start, because it will look like your fault: `main.yaml`
only runs `just test` when the `src` paths-filter matches (`src/**`, `tests/**`,
`pyproject.toml`, `uv.lock`). A long run of gene-review-only commits never
executes the suite, so breakage accumulates behind a green `main` and lands
whole on the next PR that happens to touch `tests/`. Three failures were waiting
this way (two stale derived artifacts, one off-vocabulary project tag) and had to
be cleared in #2259 before any of this could go green. Reproduce on a pristine
`origin/main` checkout before assuming a red `test (3.12)` is yours.

## Things that were specific to this repo

Anyone porting this to a third repo should look for these shapes, not just copy
the token block.

**`ai.yml` and `dragon-ai.yml` were byte-identical.** `diff` returned nothing.
Both matched `@dragon-ai-agent please`, so every qualifying event ran the agent
**twice** — visible as paired runs with identical timestamps. They are now one
workflow keyed on `@ai4c-agent please`, with the old keyword as an alias.

**The credential was already dead, and nobody knew.** `pr-shepherd` failed
**121 scheduled runs in a row over 9 days** — 2026-07-16T15:18Z until the
migration ended it on 2026-07-26T01:09Z — before
this migration — every one at `Checkout repository`, the step that used
`token: ${{ secrets.PAT_FOR_PR }}`. The first run on the App token passed every
step. The same applied to every other workflow holding the PAT. Nothing alerted,
because a scheduled workflow's failures land in the Actions tab and nowhere else.
If an agentic workflow has quietly stopped producing output, check whether it is
failing at checkout before you look at the agent.

**Two workflows could not have worked.** `arba-issue-monitor` was still calling
`claude-code-action` with the v0 inputs `mode:`, `direct_prompt:` and
`allowed_tools:`, none of which exist in v1 — the prompt was never delivered.
`ai.yml` set `ANTHROPIC_API_KEY` from a secret this repo does not have, so its
agent had no credential at all. Neither failed loudly. If you inherit workflows
across a major action version, check the input names against the action's
`action.yml` at the SHA you pin.

**`weekly-compliance` had no `github_token`** — the same false-green that cost
dismech ~11 days of no-op runs. An agent workflow that can "succeed" without
producing its artifact needs both a real token and captured output.

**A grep is not a guard.** The obvious check —
`grep -rnE "\-\-model .*claude-(opus|sonnet|haiku)-"` — matched 3 of the 28
pinned model IDs in this repo. The other 25 were `workflow_dispatch` `default:`
values, `strategy.matrix` entries, an `env:` indirection
(`ISSUE_HANDOFF_MODEL`), and the bare alias `--model opus`.
`tests/test_agent_config.py` checks all four shapes instead, and treats a stale
allowlist entry as a failure so the list can only shrink.

**A manifest is not just YAML.** `agent-run-summary` shipped broken and took
the summary step down in seven workflows, because a manifest-level field — in
this case `description:`, but the same holds for `name:` and any input/output
`description`/`default` — contained an illustrative GitHub expression — the prose explaining the bug was
the bug. GitHub template-evaluates `description:` when an action manifest loads,
`steps` is not a valid manifest context, and the action failed to load outright.
CI's YAML parse passed the whole time: the file *is* valid YAML, and the
rejection happens in the expression layer above it. Note the shape of the
regression — before, that step succeeded while writing an empty report; after,
the report was still missing *and* the job went red. `tests/test_agent_config.py`
now checks every manifest-level field, which is the boundary that matters: the
same trap applies to `name:` and to any input/output `description`/`default`. Nothing in this repo parsed action
manifests before that, which is the same blind spot that hides
`.github/actions/claude-code-action`.

**Read trust from the default branch.** `ai.yml` read its controller allowlist
from the checked-out PR ref, so a proposer with push access could add themselves
to `.github/ai-controllers.json` on their own branch and self-authorize. Same
class of bug in `untrusted-comment-guard`: on `pull_request_review_comment` the
default `GITHUB_REF` is the PR merge ref, so a bare checkout would have fetched
fork code that `github-script` then `require()`s with a write-scoped token. Both
now pin `ref: ${{ github.event.repository.default_branch }}`.

**Don't trust bare bot names.** The ported trust gate listed `"claude"`,
`"dragon-ai-agent"` and `"github-actions"` as bot logins, and bots are trusted —
so registering one of those usernames would have granted automatic trust. Only
the `[bot]` suffix, which GitHub reserves for Apps, is a reliable signal.

**Strip code spans for the gate, not for the payload.** `ai.yml` strips fenced
and inline code before matching the mention keyword, so *documenting* the
trigger does not fire it. Extracting the request from that stripped copy would
silently delete inline code from a legitimate request
(`fix \`genes/human/TP53\`` → `fix `). Gate on the stripped text; extract from
the original.

**The review workflow's own failure mode moved.** At the SHA we pin,
`claude-code-action` already throws when the agent errors, so the "phantom green
check" it used to produce is closed by the pin itself. What remains worth
catching is *why*: a Claude weekly usage limit silently no-ops every agent
workflow account-wide and is otherwise indistinguishable from a problem with the
PR. The diagnostic step reports that specifically, and deliberately uses
`!cancelled()` rather than `always()` — with `cancel-in-progress: true`, every
follow-up push cancels the in-flight review, and `always()` turns the most
routine event in the repo into a red X.

---

## Known gaps

- **`ai4c-reviewer` has `Contents: read`.** GitHub ties "this approval counts
  toward branch protection" to *write* access, which for an App is governed by
  the Contents permission — so its approvals render as *"approved with read-only
  permissions."* `main` has no branch protection today, so nothing is blocked.
  If required-approval rules are ever enabled, raise the App to
  `Contents: write` first (an App-settings change plus accepting the permission
  bump on the org installation).
- **A stale `dragon-ai-agent` collaborator entry remains** on the repo. The
  account itself is deleted (`GET /users/dragon-ai-agent` 404s) so it grants
  nothing, but the entry should be removed — that is a settings click, not a
  code change. The recipes that re-added it, and that re-installed `PAT_FOR_PR`,
  were removed in the cleanup PR; before that, a single `just gh-add-secrets`
  would have reinstalled the exposed credential and undone this migration.
  Worth remembering that a revoked token is not a revoked account, and a deleted
  account is not a removed collaborator.
- **The `PAT_FOR_PR` secret still exists**, though nothing references it — the
  only mentions left in the tree are two do-not-reintroduce comments
  (`justfile:180`, `ai.yml:187`) and this document. It
  should be deleted. Note it is already non-functional — a checkout using it
  fails outright, which is how `pr-shepherd` came to fail 121 runs in a row — so
  deleting it is bookkeeping rather than a cutover.
- **Five workflows run with `--dangerously-skip-permissions`**:
  `arba-issue-monitor`, `curation-scanner`, `go-annotation-scanner`,
  `pr-shepherd` and `weekly-compliance`. Not just the scanners —
  **`pr-shepherd` reads PR titles, bodies, diffs and review comments**, a wider
  untrusted-input surface than upstream GO issue text. The mitigations are the
  prompt-level untrusted-input guardrail and the App token's scope, not tool
  restriction. `litscan-module-member`, `claude-code-review` and `claude` all
  enumerate `--allowedTools` instead, so the precedent for tightening the other
  five is already in the repo.
- **`.github/actions/claude-code-action` is a partly-unmanaged agent path.** It
  is an older composite — `npm install -g` plus a CBORG endpoint — sitting behind
  `claude-issue-summarize` and `claude-issue-triage`. The manifest and checkout
  tests do reach it, but the pinned-SHA, input-vocabulary and central-model
  guards do not: it never calls `anthropics/claude-code-action`, and it is not in
  `agent-config.yaml`, so its model and its agent version are uncontrolled.
  Migrating it is its own change.
- **`weekly-compliance` has no post-run assertion that it opened a PR.** The
  missing token that made it a no-op is fixed and its output is captured, but
  "the agent ran cleanly and produced nothing" is still indistinguishable from
  "there was nothing to fix." Closing that needs a decision about what should
  happen on a week with no low-scoring files, not just a check.

## Not adopted

dismech has scanners this repo deliberately did not take: `discussion-scanner`,
`literature-scan`, `preprint-scan`, `knowledge-gap-scan`. ai-gene-review does
less literature mining and more scanning of GO repositories, which its own
`go-annotation-scanner`, `arba-issue-monitor` and `litscan-module-member` cover.
`post-review-agent` (turns human review comments into suggested changes) and
`auto-merge-compliance` are still open candidates.
