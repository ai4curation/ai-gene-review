"""Security contracts for the deterministic PR Shepherd closing pass."""

from pathlib import Path

import yaml


ROOT = Path(__file__).parents[1]
SHEPHERD = ROOT / ".github/workflows/pr-shepherd.yml"
GENERATE_PAGES = ROOT / ".github/workflows/generate-pages.yaml"
APPROVE_REGEN = ROOT / ".github/actions/approve-regen-pr/action.yml"


def _workflow(path: Path) -> dict:
    return yaml.safe_load(path.read_text())


def _step(job: dict, name: str) -> dict:
    return next(step for step in job["steps"] if step.get("name") == name)


def test_merge_controller_has_a_fresh_runner_and_trusted_checkout():
    jobs = _workflow(SHEPHERD)["jobs"]
    assert {"shepherd", "merge-ready"} <= jobs.keys()
    merge_job = jobs["merge-ready"]
    assert "needs" not in merge_job
    assert "claude" not in str(merge_job).casefold()

    checkout = _step(merge_job, "Checkout trusted default branch")
    assert checkout["with"]["ref"] == "${{ github.event.repository.default_branch }}"
    assert checkout["with"]["token"] == "${{ github.token }}"
    assert checkout["with"]["persist-credentials"] is False


def test_audit_and_execute_have_literal_modes_and_distinct_tokens():
    merge_job = _workflow(SHEPHERD)["jobs"]["merge-ready"]
    audit = _step(merge_job, "Audit merge-ready PRs (deterministic)")
    execute = _step(merge_job, "Merge ready PRs (deterministic)")

    assert audit["env"]["GH_TOKEN"] == "${{ github.token }}"
    assert "--dry-run" in audit["run"]
    assert "--execute" not in audit["run"]
    assert execute["env"]["GH_TOKEN"] == "${{ github.token }}"
    assert execute["env"]["GH_MERGE_TOKEN"] == (
        "${{ steps.ai4c-token-merge.outputs.token }}"
    )
    assert "--execute" in execute["run"]
    assert "--dry-run" not in execute["run"]
    for step in (audit, execute):
        assert '--required-check "test (3.12)"' in step["run"]
        assert '--trusted-reviewer "ai4c-reviewer"' in step["run"]


def test_execute_is_feature_gated_main_only_and_narrowly_scoped():
    merge_job = _workflow(SHEPHERD)["jobs"]["merge-ready"]
    assert "PR_SHEPHERD_MERGE_ENABLED" in merge_job["env"]["MERGE_MODE"]

    guard = _step(merge_job, "Validate execute-mode rollout guards")
    assert "PR_SHEPHERD_MERGE_ENABLED" in guard["env"]["MERGE_ENABLED"]
    assert "refs/heads/$DEFAULT_BRANCH" in guard["run"]
    assert "branches/$DEFAULT_BRANCH" in guard["run"]
    assert 'if [ "$protected" != "true" ]' in guard["run"]

    token = _step(merge_job, "Generate scoped merge token")
    permissions = token["with"]
    assert permissions["permission-contents"] == "write"
    assert permissions["permission-pull-requests"] == "write"
    assert "permission-checks" not in permissions
    assert "permission-statuses" not in permissions
    assert "|| github.token" not in str(token)


def test_generated_pages_waits_for_ci_and_exact_head_approval():
    workflow = _workflow(GENERATE_PAGES)
    job = next(iter(workflow["jobs"].values()))
    checkout = _step(job, "Checkout repository")
    create = _step(job, "Create or update regeneration PR")
    approve = _step(job, "Approve exact generated commit")

    assert checkout["with"]["ref"] == "${{ github.event.repository.default_branch }}"
    assert "--auto" in create["run"]
    assert "--match-head-commit" in create["run"]
    assert "MERGE_ENABLED" in create["run"]
    assert "merging generated artifacts directly" not in create["run"]
    assert approve["uses"] == "./.github/actions/approve-regen-pr"
    assert approve["with"]["pr-number"] == "${{ steps.regen-pr.outputs.pr_number }}"
    assert approve["with"]["base-branch"] == "main"
    assert approve["with"]["expected-author"] == "app/ai4c-agent"

    action = APPROVE_REGEN.read_text()
    assert 'gh pr view "$PR_NUMBER"' in action
    assert '[ "$pr_base" != "$BASE_BRANCH" ]' in action
    assert '[ "$pr_author" != "$EXPECTED_AUTHOR" ]' in action
    assert '-f commit_id="$built_sha"' in action
    assert "permission-pull-requests: write" in action
    assert "permission-contents: write" not in action
