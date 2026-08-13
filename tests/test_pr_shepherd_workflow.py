"""Security contracts for the deterministic PR Shepherd closing pass."""

import re
import subprocess
from pathlib import Path

import yaml


ROOT = Path(__file__).parents[1]
SHEPHERD = ROOT / ".github/workflows/pr-shepherd.yml"
GENERATE_PAGES = ROOT / ".github/workflows/generate-pages.yaml"
CLAUDE_REVIEW = ROOT / ".github/workflows/claude-code-review.yml"
APPROVE_REGEN = ROOT / ".github/actions/approve-regen-pr/action.yml"


def _workflow(path: Path) -> dict:
    return yaml.safe_load(path.read_text())


def _step(job: dict, name: str) -> dict:
    return next(step for step in job["steps"] if step.get("name") == name)


def _action_uses(job: dict) -> set[str]:
    return {str(step["uses"]) for step in job["steps"] if "uses" in step}


def test_merge_controller_is_a_separate_job_with_trusted_checkout():
    jobs = _workflow(SHEPHERD)["jobs"]
    assert {"shepherd", "merge-ready"} <= jobs.keys()
    shepherd_job = jobs["shepherd"]
    merge_job = jobs["merge-ready"]

    # Separate jobs always receive separate runners; a future `needs` edge would
    # only order them and must not be confused with runner/process sharing.
    shepherd_actions = _action_uses(shepherd_job)
    merge_actions = _action_uses(merge_job)
    assert any(
        action.startswith("anthropics/claude-code-action@")
        for action in shepherd_actions
    )
    assert not any(
        action.startswith("anthropics/claude-code-action@") for action in merge_actions
    )
    assert _step(merge_job, "Generate scoped merge token")

    checkout = _step(merge_job, "Checkout trusted default branch")
    assert checkout["with"]["ref"] == "${{ github.event.repository.default_branch }}"
    assert checkout["with"]["token"] == "${{ github.token }}"
    assert checkout["with"]["persist-credentials"] is False


def test_audit_and_execute_have_literal_modes_and_distinct_tokens():
    workflow = _workflow(SHEPHERD)
    # PyYAML 1.1 parses the unquoted workflow key `on` as boolean true.
    include_drafts = workflow[True]["workflow_dispatch"]["inputs"]["include_drafts"]
    assert include_drafts["type"] == "boolean"
    assert include_drafts["default"] is False
    merge_job = workflow["jobs"]["merge-ready"]
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
        assert "--trusted-reviewer" not in step["run"]
        assert "--allowed-path-prefix" not in step["run"]
        assert "draft_args+=(--include-drafts)" in step["run"]
        assert '"${draft_args[@]}"' in step["run"]


def test_execute_is_feature_gated_main_only_and_narrowly_scoped():
    merge_job = _workflow(SHEPHERD)["jobs"]["merge-ready"]
    assert "PR_SHEPHERD_MERGE_ENABLED" in merge_job["env"]["MERGE_MODE"]

    guard = _step(merge_job, "Validate execute-mode rollout guards")
    assert "PR_SHEPHERD_MERGE_ENABLED" in guard["env"]["MERGE_ENABLED"]
    assert "refs/heads/$DEFAULT_BRANCH" in guard["run"]
    assert "branches/$DEFAULT_BRANCH" in guard["run"]
    assert 'if [ "$protected" != "true" ]' in guard["run"]
    assert "::notice title=Protection smoke check passed::" in guard["run"]
    assert "manual verification" in guard["run"]

    token = _step(merge_job, "Generate scoped merge token")
    permissions = {
        name: value
        for name, value in token["with"].items()
        if name.startswith("permission-")
    }
    assert permissions == {
        "permission-contents": "write",
        "permission-pull-requests": "write",
    }
    assert "permission-issues" not in token["with"]
    assert "|| github.token" not in str(token)


def test_reviewer_app_token_cannot_write_pr_contents():
    job = _workflow(CLAUDE_REVIEW)["jobs"]["claude-review"]
    token = _step(job, "Generate ai4c-reviewer token")
    permissions = {
        name: value
        for name, value in token["with"].items()
        if name.startswith("permission-")
    }
    assert permissions == {"permission-pull-requests": "write"}


def test_generated_pages_waits_for_ci_and_exact_head_approval():
    workflow = _workflow(GENERATE_PAGES)
    job = workflow["jobs"]["generate-pages"]
    checkout = _step(job, "Checkout repository")
    create = _step(job, "Create or update regeneration PR")
    approve = _step(job, "Approve exact generated commit")
    warning = _step(job, "Warn when generated approval is unavailable")
    auto_merge = _step(job, "Validate protection and arm generated auto-merge")
    create_script = create["run"]
    auto_script = auto_merge["run"]

    step_names = [step.get("name") for step in job["steps"]]
    assert step_names.index("Create or update regeneration PR") < step_names.index(
        "Approve exact generated commit"
    )
    assert step_names.index("Approve exact generated commit") < step_names.index(
        "Warn when generated approval is unavailable"
    )
    assert step_names.index(
        "Warn when generated approval is unavailable"
    ) < step_names.index("Validate protection and arm generated auto-merge")

    assert checkout["with"]["ref"] == "${{ github.event.repository.default_branch }}"
    assert create["env"]["GH_TOKEN"] == "${{ steps.ai4c-token.outputs.token }}"
    assert "DEFAULT_BRANCH" not in create["env"]
    assert "MERGE_ENABLED" not in create["env"]
    assert "--auto" not in create_script
    assert "branches/main" not in create_script
    assert 'echo "head_sha=$(git rev-parse HEAD)" >> "$GITHUB_OUTPUT"' in (
        create_script
    )

    assert auto_merge["env"]["GH_TOKEN"] == "${{ steps.ai4c-token.outputs.token }}"
    assert auto_merge["env"]["DEFAULT_BRANCH"] == (
        "${{ github.event.repository.default_branch }}"
    )
    assert auto_merge["env"]["PR_NUMBER"] == ("${{ steps.regen-pr.outputs.pr_number }}")
    assert auto_merge["env"]["EXPECTED_HEAD"] == (
        "${{ steps.regen-pr.outputs.head_sha }}"
    )
    assert auto_merge["env"]["APPROVAL_OUTCOME"] == (
        "${{ steps.approve-generated.outcome }}"
    )
    assert "!cancelled()" in auto_merge["if"]
    assert "steps.regen-pr.outcome == 'success'" in auto_merge["if"]
    assert "--auto" in auto_script
    assert '--match-head-commit "$EXPECTED_HEAD"' in auto_script
    assert "MERGE_ENABLED" in auto_script

    flag_guard = auto_script.index('if [ "$MERGE_ENABLED" != "true" ]')
    branch_guard = auto_script.index('if [ "$DEFAULT_BRANCH" != "main" ]')
    pr_base_read = auto_script.index("--json baseRefName")
    pr_base_guard = auto_script.index('if [ "$pr_base" != "main" ]')
    protection_read = auto_script.index('"repos/$GITHUB_REPOSITORY/branches/main"')
    protection_guard = auto_script.index('if [ "$protected" != "true" ]')
    approval_guard = auto_script.index('if [ "$APPROVAL_OUTCOME" != "success" ]')
    head_guard = auto_script.index('if [ -z "$EXPECTED_HEAD" ]')
    arm = auto_script.index('echo "Arming auto-merge')
    merge = auto_script.index('gh pr merge "$PR_NUMBER"')
    assert (
        flag_guard
        < branch_guard
        < pr_base_read
        < pr_base_guard
        < protection_read
        < protection_guard
        < approval_guard
        < head_guard
        < arm
        < merge
    )
    assert "--base main" in create_script
    assert 'if ! protected="$(gh api' in auto_script
    assert "Generated auto-merge base check failed" in auto_script
    assert "Generated auto-merge protection check failed" in auto_script
    assert "Generated auto-merge head pin missing" in auto_script
    assert "refusing to arm auto-merge" in auto_script

    assert approve["id"] == "approve-generated"
    assert approve["continue-on-error"] is True
    assert approve["uses"] == "./.github/actions/approve-regen-pr"
    assert approve["with"]["pr-number"] == "${{ steps.regen-pr.outputs.pr_number }}"
    assert approve["with"]["base-branch"] == "main"
    assert approve["with"]["expected-author"] == "app/ai4c-agent"
    assert "always()" in warning["if"]
    assert "steps.approve-generated.outcome == 'failure'" in warning["if"]
    assert "!= 'success'" not in warning["if"]
    assert "::warning title=Generated PR approval unavailable::" in warning["run"]
    assert "the later step will not arm auto-merge" in warning["run"]

    action = APPROVE_REGEN.read_text()
    assert 'gh pr view "$PR_NUMBER"' in action
    assert '[ "$pr_base" != "$BASE_BRANCH" ]' in action
    assert '[ "$pr_author" != "$EXPECTED_AUTHOR" ]' in action
    assert '-f commit_id="$built_sha"' in action
    assert "permission-pull-requests: write" in action
    assert "permission-contents: write" not in action


def test_generated_artifact_allowlist_is_fully_anchored():
    workflow = _workflow(GENERATE_PAGES)
    job = workflow["jobs"]["generate-pages"]
    create_script = _step(job, "Create or update regeneration PR")["run"]
    match = re.search(r"grep -vE '([^']+)'", create_script)
    assert match, "could not find the generated-artifact allowlist"
    allowlist = match.group(1)

    def allowed(path: str) -> bool:
        result = subprocess.run(
            ["grep", "-Eq", allowlist],
            input=f"{path}\n",
            text=True,
            check=False,
        )
        return result.returncode == 0

    for path in (
        "genes/human/TP53/TP53-ai-review.html",
        "pages/projects/index.html",
        "pages/projects/nested/report.html",
        "app/index.html",
        "app/data.js",
        "app/schema.js",
        "reports/validation-all.tsv",
    ):
        assert allowed(path), path

    for path in (
        "genes/human/TP53/TP53-ai-review.yaml",
        "genes/human/TP53/TP53-ai-review.html-notes.md",
        "pages",
        "app/extra.js",
        "reports",
        "src/ai_gene_review/render.py",
    ):
        assert not allowed(path), path
