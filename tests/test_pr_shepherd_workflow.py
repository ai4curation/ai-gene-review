"""Security contracts for the deterministic PR Shepherd closing pass."""

import re
import subprocess
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
        "permission-issues": "write",
        "permission-pull-requests": "write",
    }
    assert "|| github.token" not in str(token)


def test_generated_pages_waits_for_ci_and_exact_head_approval():
    workflow = _workflow(GENERATE_PAGES)
    job = next(iter(workflow["jobs"].values()))
    checkout = _step(job, "Checkout repository")
    create = _step(job, "Create or update regeneration PR")
    approve = _step(job, "Approve exact generated commit")
    warning = _step(job, "Warn when generated approval is unavailable")

    assert checkout["with"]["ref"] == "${{ github.event.repository.default_branch }}"
    assert "--auto" in create["run"]
    assert "--match-head-commit" in create["run"]
    assert "MERGE_ENABLED" in create["run"]
    assert approve["id"] == "approve-generated"
    assert approve["continue-on-error"] is True
    assert approve["uses"] == "./.github/actions/approve-regen-pr"
    assert approve["with"]["pr-number"] == "${{ steps.regen-pr.outputs.pr_number }}"
    assert approve["with"]["base-branch"] == "main"
    assert approve["with"]["expected-author"] == "app/ai4c-agent"
    assert "always()" in warning["if"]
    assert "steps.approve-generated.outcome != 'success'" in warning["if"]
    assert "::warning title=Generated PR approval unavailable::" in warning["run"]
    assert "protected main will keep the PR open and unmerged" in warning["run"]

    action = APPROVE_REGEN.read_text()
    assert 'gh pr view "$PR_NUMBER"' in action
    assert '[ "$pr_base" != "$BASE_BRANCH" ]' in action
    assert '[ "$pr_author" != "$EXPECTED_AUTHOR" ]' in action
    assert '-f commit_id="$built_sha"' in action
    assert "permission-pull-requests: write" in action
    assert "permission-contents: write" not in action


def test_generated_artifact_allowlist_is_fully_anchored():
    workflow = _workflow(GENERATE_PAGES)
    job = next(iter(workflow["jobs"].values()))
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
