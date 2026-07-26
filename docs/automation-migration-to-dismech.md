# Migrating ai-gene-review automation to the dismech pattern

This is an execution guide for bringing `ai-gene-review`'s GitHub Actions
automation up to the state of `monarch-initiative/dismech`. The two repos share a
common ancestor (the agentic workflows were copied around 2026-07-03) but dismech
has since had a substantial security-hardening and centralization pass that
ai-gene-review has not received.

The **security half** of this migration (getting off the exposed `PAT_FOR_PR` /
`dragon-ai-agent` machine account and onto short-lived GitHub App tokens) is the
same remediation dismech completed for the
[dragon-ai-agent PAT exposure incident](https://github.com/ai4curation/ai-security-private/blob/main/docs/incidents/2026-07-dragon-ai-agent-pat-exposure.md).
The step-by-step record and the copy-paste token pattern live in the
security repo:

> **[ai-security-private → docs/history/2026-07-25-dismech-pat-to-app-migration.md](https://github.com/ai4curation/ai-security-private/blob/main/docs/history/2026-07-25-dismech-pat-to-app-migration.md)**

Read that first for the *why* and the exact per-workflow token block. This guide
is the ai-gene-review-specific *what* and *in what order*.

---

## Current gap (ai-gene-review vs dismech)

| Area | ai-gene-review today | dismech target |
|---|---|---|
| **Write auth** | `PAT_FOR_PR` in 8 workflows: `ai`, `pr-shepherd`, `dragon-ai`, `curation-scanner`, `go-annotation-scanner`, `litscan-module-member`, `warm-reference-cache`, `generate-pages` | short-lived `ai4c-agent` App token, `PAT_FOR_PR` fully retired |
| **`.git/config` exposure** | `persist-credentials: false` only in `main.yaml`; every agent checkout persists its token to disk (the incident vector) | `persist-credentials: false` on every agent checkout + `gh auth setup-git` |
| **Reviewer identity** | `claude-code-review` uses the **same** `AI4C_AGENT` app as writers | separate `ai4c-reviewer` App (independent review; approval actually counts) |
| **Model config** | hardcoded, scattered, stale (`claude-opus-4-7` ×12, `claude-sonnet-4-6` ×8, `claude-haiku-4-5` ×8) | central `.github/agent-config.yaml` + `resolve-agent-config` action; Opus 5 / Sonnet 5 |
| **Cron cadence** | hardcoded `schedule:` per workflow | central `.github/cron-profiles.yaml` + `scripts/apply_cron_profile.py` |
| **Fork-PR injection gate** | none | `close-fork-prs.yml` (`pull_request_target`, closes fork PRs at the door) |
| **Untrusted-comment guard** | none | `untrusted-comment-guard.yml` |
| **Run reports** | agent output buried in raw log | injection-safe step-summary in every agentic workflow |
| **Dispatch model dropdowns** | `type: choice` defaults silently override any central config | no-override string inputs (`default: ""`) |

ai-gene-review already has `create-github-app-token` wired in `claude-code-review.yml`
(using `AI4C_AGENT`), so the App-token mechanism is proven in this repo — the work
is extending it to the writer workflows and splitting the reviewer identity.

---

## Prerequisites (one-time, org/admin — cannot be scripted)

1. **Confirm the `ai4c-agent` GitHub App is installed on `ai4curation/ai-gene-review`**
   with Repository permissions: Contents R/W, Pull requests R/W, Issues R/W, and
   (if you keep the discussion/annotation scanners) Discussions R/W. Its secrets
   `AI4C_AGENT_APP_ID` / `AI4C_AGENT_PRIVATE_KEY` already exist here.
2. **Provision (or install) a second App, `ai4c-reviewer`**, for the reviewer role.
   Repository permissions: Pull requests R/W **and Contents: Read & write** — the
   reviewer's approval only counts toward branch protection if it has write access,
   which for an App is governed by Contents (a GitHub quirk documented in the
   security-repo playbook). Add `AI4C_REVIEWER_APP_ID` / `AI4C_REVIEWER_PRIVATE_KEY`.
   *Creating an App and installing it on the repo are separate steps; without
   Repository-scoped permissions GitHub won't offer repo scoping and the token mint
   404s.*
3. **Do not delete the `PAT_FOR_PR` secret yet** — do that only at the end
   (Phase 6), after no workflow references it.

---

## Phase 1 — Kill the incident vector (highest priority)

Migrate each `PAT_FOR_PR` workflow to the App-token pattern. **The single most
important line is `persist-credentials: false`** — it closes the exact
`.git/config` → agent-`cat` → public-trace exposure chain from the incident.

For each of the 8 workflows above, apply the target block from the
[security-repo playbook](https://github.com/ai4curation/ai-security-private/blob/main/docs/history/2026-07-25-dismech-pat-to-app-migration.md#the-target-pattern-per-workflow):

```yaml
permissions:
  contents: read        # scope the default GITHUB_TOKEN down; the App token does the work

steps:
  - name: Generate ai4c-agent token
    id: ai4c-token
    uses: actions/create-github-app-token@d72941d797fd3113feb6b93fd0dec494b13a2547 # v1 (SHA-pinned)
    with:
      app-id: ${{ secrets.AI4C_AGENT_APP_ID }}
      private-key: ${{ secrets.AI4C_AGENT_PRIVATE_KEY }}

  - name: Checkout
    uses: actions/checkout@v6
    with:
      token: ${{ steps.ai4c-token.outputs.token }}
      persist-credentials: false        # <-- closes the incident exposure vector

  - name: Configure git identity + credential helper
    env:
      GH_TOKEN: ${{ steps.ai4c-token.outputs.token }}
      APP_SLUG: ${{ steps.ai4c-token.outputs.app-slug }}
    run: |
      APP_USER_ID="$(gh api "/users/${APP_SLUG}[bot]" --jq .id)"
      git config --global user.name "${APP_SLUG}[bot]"
      git config --global user.email "${APP_USER_ID}+${APP_SLUG}[bot]@users.noreply.github.com"
      gh auth setup-git

  - name: Run agent
    uses: anthropics/claude-code-action@44423bdec74b97d67543eb16c110546762c110b2 # v1 (SHA-pinned)
    env:
      GH_TOKEN: ${{ steps.ai4c-token.outputs.token }}
      GITHUB_TOKEN: ${{ steps.ai4c-token.outputs.token }}
    with:
      github_token: ${{ steps.ai4c-token.outputs.token }}
```

Reference implementations in dismech (copy structure, adapt content):

| ai-gene-review workflow | dismech reference PR |
|---|---|
| `pr-shepherd.yml` | [dismech#6890](https://github.com/monarch-initiative/dismech/pull/6890) |
| `curation-scanner.yml` + any scanner | [dismech#6918](https://github.com/monarch-initiative/dismech/pull/6918) |
| `weekly-compliance.yaml` | [dismech#6934](https://github.com/monarch-initiative/dismech/pull/6934) (also fixes a false-green: no `github_token` → silent no-PR) |
| `dragon-ai.yml` | [dismech#6979](https://github.com/monarch-initiative/dismech/pull/6979) |
| `ai.yml`, `go-annotation-scanner.yml`, `litscan-module-member.yml`, `generate-pages.yaml`, `warm-reference-cache.yaml` | same pattern; page/cache jobs can use `github-actions[bot]` + the built-in `GITHUB_TOKEN` if they only push to their own auto-branches |

**dragon-ai.yml specifics** (dismech#6979): also drop the `assigned` trigger —
**GitHub Apps cannot be assignees**, so assignment-based dispatch cannot move to
an App; keep only the `@dragon-ai-agent please` text-keyword mention. And harden
the mention path: read the controller allowlist (`.github/ai-controllers.json`)
from the **default branch**, not the PR ref (else a pusher self-authorizes); pass
prompt values via `env:` + `printf`, never `echo "${{ ... }}"`; strip code spans
before the mention regex so documenting the keyword doesn't self-trigger.

**Verify per workflow** after editing:
```bash
python3 -c "import yaml,sys; yaml.safe_load(open(sys.argv[1]))" .github/workflows/<wf>.yml
grep -n "PAT_FOR_PR\|persist-credentials" .github/workflows/<wf>.yml
```

## Phase 2 — Split the reviewer identity

`claude-code-review.yml` currently mints an `AI4C_AGENT` token — the same identity
the writers use, so it can "review its own work" and its approval may not count.
Point it at the reviewer App and add the writer to `allowed_bots`
(dismech commit `2a2300df52`):

```yaml
  - name: Generate ai4c-reviewer token
    id: reviewer-token
    uses: actions/create-github-app-token@d72941d797fd3113feb6b93fd0dec494b13a2547 # v1
    with:
      app-id: ${{ secrets.AI4C_REVIEWER_APP_ID }}
      private-key: ${{ secrets.AI4C_REVIEWER_PRIVATE_KEY }}
  # ...
      github_token: ${{ steps.reviewer-token.outputs.token || github.token }}
      allowed_bots: 'claude,github-actions,ai4c-agent'   # writer must be listed or its
                                                         # dispatched/pushed reviews are rejected
```

Why `allowed_bots` must include `ai4c-agent`: `claude-code-action` rejects a run
whose *initiating actor* is a bot not in the list — even for `workflow_dispatch`.
And note the **App-token push behavior**: unlike the built-in `GITHUB_TOKEN`,
a push made with an App token fires `pull_request: synchronize`, so review
auto-triggers on writer pushes (no manual re-dispatch needed).

## Phase 3 — Add the injection controls

1. **`close-fork-prs.yml`** — the single highest-leverage control. Copy dismech's
   ([dismech#6895](https://github.com/monarch-initiative/dismech/pull/6895)). It's a
   `pull_request_target` job that closes any fork PR on open/reopen and points the
   author at `CONTRIBUTING.md`. It runs from the base repo's copy of the workflow,
   **never checks out fork code** (only `gh` API calls), needs only
   `pull-requests: write`, and leaves same-repo PRs untouched. A fork PR is the
   main way external attacker-authored content reaches an agentic workflow's
   context — refusing it at the door beats trying to contain it.
2. **`untrusted-comment-guard.yml`** — copy dismech's; it gates agent responses to
   comments from untrusted authors (see the security repo's
   [untrusted-comment incident](https://github.com/ai4curation/ai-security-private/blob/main/docs/incidents/2026-07-08-dismech-untrusted-comment-attempt.md)).
3. If you keep a **discussion/annotation scanner** that reads arbitrary public
   discussion text, port dismech's deterministic trust gate
   `.github/scripts/github-trust-gate.js` — it pre-filters candidates to those
   where every non-bot participant is an allow-listed controller, so untrusted
   discussion text never reaches the agent.

## Phase 4 — Centralize model + cron config

1. **`.github/agent-config.yaml` + `.github/actions/resolve-agent-config`** — one
   source of truth for which model backs each workflow. Copy both from dismech.
   Each managed workflow gains a `Resolve agent config` step that exports
   `AGENT_MODEL`; the agent step uses `--model ${{ env.AGENT_MODEL }}` instead of a
   hardcoded ID. A test enforces no workflow re-hardcodes `--model`. (Background:
   dismech issue #5218.)
2. **`.github/cron-profiles.yaml` + `scripts/apply_cron_profile.py`** — named cadence
   profiles (`slow`/`medium`/`fast`/`off`) instead of hand-edited `schedule:` lines.
   Switch with `just cron-profile <name>`. This also prevents schedule drift (a
   workflow managed in the config but missing its `on.schedule` block gets one
   re-inserted — the resurrection hazard that retired dismech's `stale-pr-reassign`
   in [dismech#6958](https://github.com/monarch-initiative/dismech/pull/6958)).

## Phase 5 — Model bump + dispatch hygiene

1. **Bump defaults to current models** in `agent-config.yaml`: `claude-opus-5`,
   `claude-sonnet-5` (Haiku has no v5 yet). **Verify exact IDs against the live
   Anthropic model docs, never from memory** — dismech was once burned by a
   fabricated model ID that silently no-op'd runs into phantom green checks
   ([dismech#6933](https://github.com/monarch-initiative/dismech/pull/6933)).
2. **Convert every `workflow_dispatch` `model:` input** from `type: choice` to a
   no-override string (`default: ""`). A `choice` input always sends its default,
   silently overriding the central config on every manual run; the resolver treats
   an empty override as "use the config" (same PR).

## Phase 6 — Reports, and the final teardown

1. **Add injection-safe step summaries** to every agentic workflow so the agent's
   report shows on the Actions run screen, not just the raw log
   ([dismech#6998](https://github.com/monarch-initiative/dismech/pull/6998)):
   ```yaml
     - name: Write step summary
       if: ${{ always() && steps.<agent-step-id>.outputs.result != '' }}
       env:
         RESULT: ${{ steps.<agent-step-id>.outputs.result }}   # via env, never echo "${{ }}"
       run: |
         { echo "## <emoji> <Workflow> Run"; echo ''; echo '```'; printf '%s\n' "$RESULT"; echo '```'; } >> "$GITHUB_STEP_SUMMARY"
   ```
2. **Teardown:** once `grep -rn "secrets.PAT_FOR_PR" .github/` is empty, **delete
   the `PAT_FOR_PR` secret** and confirm the token is revoked. Decide the fate of
   the `dragon-ai-agent` account (its only remaining use is the mention keyword,
   a text match that works without the account).

---

## Optional: adopt the dismech scanner fleet

dismech has agentic scanners ai-gene-review lacks — adopt only the ones that fit
GO/gene-review curation, and migrate their auth with the Phase 1 pattern as you go:

- `discussion-scanner.yml` — responds to GitHub Discussions (needs the trust gate).
- `literature-scan.yml` / `preprint-scan.yml` / `knowledge-gap-scan.yml` — mine new
  literature/preprints/knowledge-gaps into curation handoff issues.
- `post-review-agent.yml` — turns human review comments into suggested changes.
- `auto-merge-compliance.yml` — auto-merges clean compliance PRs.

ai-gene-review's own domain scanners (`arba-issue-monitor`, `go-annotation-scanner`,
`litscan-module-member`) stay — just migrate their auth (Phase 1).

---

## Suggested PR sequencing

Do it as several small PRs, not one, so each is reviewable and the reviewer split
lands early:

1. **Phase 2** first (reviewer → `ai4c-reviewer`) — so subsequent writer PRs get
   independent review.
2. **Phase 1** per-workflow (or a few at a time) — the security-critical bulk.
3. **Phase 3** (fork-close + untrusted-comment guard).
4. **Phase 4–5** (centralize config, bump models, dispatch hygiene).
5. **Phase 6** (reports), then delete the `PAT_FOR_PR` secret.

## Final verification

```bash
# no PAT references remain
grep -rn "secrets.PAT_FOR_PR" .github/            # -> empty

# every agent checkout is non-persisting
grep -rL "persist-credentials: false" $(grep -rl "actions/checkout" .github/workflows/)

# no hardcoded --model (models come from the resolver)
grep -rnE "\-\-model .*claude-(opus|sonnet|haiku)-" .github/workflows/   # -> empty

# app-token consistency
grep -rn "AI4C_AGENT_APP_ID\|AI4C_REVIEWER_APP_ID" .github/workflows/
```
