"""The CI guard that keeps rendered gene review HTML out of Git (#6221)."""

import subprocess
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / ".github/scripts/reject_added_review_html.sh"
REVIEW_HTML = "genes/human/A/A-ai-review.html"


def git(repo: Path, *args: str) -> None:
    subprocess.run(["git", *args], cwd=repo, check=True, capture_output=True)


def run_guard(repo: Path) -> subprocess.CompletedProcess:
    return subprocess.run(["bash", str(SCRIPT)], cwd=repo, capture_output=True, text=True)


@pytest.fixture
def repo(tmp_path: Path) -> Path:
    git(tmp_path, "init", "-q", "-b", "main")
    git(tmp_path, "config", "user.email", "t@example.org")
    git(tmp_path, "config", "user.name", "t")
    (tmp_path / "genes/human/A").mkdir(parents=True)
    (tmp_path / REVIEW_HTML).write_text("<p>old</p>")
    (tmp_path / "genes/human/A/A-ai-review.yaml").write_text("id: A\n")
    git(tmp_path, "add", ".")
    git(tmp_path, "commit", "-qm", "base")
    return tmp_path


def commit(repo: Path, change: str) -> None:
    if change == "add_nested":
        path = repo / "genes/human/B/B-ai-review.html"
        path.parent.mkdir(parents=True)
        path.write_text("<p>new</p>")
    elif change == "add_top_level":
        (repo / "genes/Z-ai-review.html").write_text("<p>new</p>")
    elif change == "add_other_html":
        (repo / "genes/human/A/A-pathway.html").write_text("<p>pathway</p>")
    elif change == "modify":
        (repo / REVIEW_HTML).write_text("<p>re-rendered</p>")
    elif change == "delete":
        (repo / REVIEW_HTML).unlink()
    elif change == "rename_folder":
        git(repo, "mv", "genes/human/A", "genes/human/A2")
    elif change == "yaml_only":
        (repo / "genes/human/A/A-ai-review.yaml").write_text("id: A\nchanged: true\n")
    git(repo, "add", "-A", "-f")
    git(repo, "commit", "-qm", change)


@pytest.mark.parametrize(
    "change,fails",
    [
        ("add_nested", True),
        # `:(glob)genes/**/` also matches zero directories; a bare `genes/*` would not.
        ("add_top_level", True),
        # A folder rename re-adds the HTML at the new path; it should be untracked.
        ("rename_folder", True),
        ("modify", False),
        ("delete", False),
        ("add_other_html", False),
        ("yaml_only", False),
    ],
)
def test_guard_rejects_only_added_review_html(repo: Path, change: str, fails: bool):
    commit(repo, change)
    result = run_guard(repo)
    assert (result.returncode != 0) == fails, result.stdout + result.stderr
    if fails:
        assert "Rendered HTML added" in result.stdout


def test_guard_still_fires_in_a_depth_one_clone(repo: Path, tmp_path: Path):
    # CI checks out with fetch-depth: 1, where history-walking commands such as
    # `git log --pretty=%P` see no parent and would make the guard pass silently.
    commit(repo, "add_nested")
    clone = tmp_path / "shallow"
    subprocess.run(
        ["git", "clone", "-q", "--depth=1", repo.as_uri(), str(clone)],
        check=True,
        capture_output=True,
    )
    result = run_guard(clone)
    assert result.returncode != 0, result.stdout + result.stderr
    assert "genes/human/B/B-ai-review.html" in result.stdout


def test_guard_passes_on_root_commit(tmp_path: Path):
    git(tmp_path, "init", "-q", "-b", "main")
    git(tmp_path, "config", "user.email", "t@example.org")
    git(tmp_path, "config", "user.name", "t")
    (tmp_path / "genes/human/A").mkdir(parents=True)
    (tmp_path / REVIEW_HTML).write_text("<p>x</p>")
    git(tmp_path, "add", "-A", "-f")
    git(tmp_path, "commit", "-qm", "root")
    assert run_guard(tmp_path).returncode == 0


def test_guard_runs_ungated_before_the_path_filter():
    workflow = yaml.safe_load((ROOT / ".github/workflows/main.yaml").read_text())
    steps = workflow["jobs"]["validation"]["steps"]
    names = [s.get("name") for s in steps]
    guard = steps[names.index("Reject newly added gene review HTML")]
    assert guard["run"] == "bash .github/scripts/reject_added_review_html.sh"
    assert "if" not in guard and not guard.get("continue-on-error")
    changes = next(i for i, s in enumerate(steps) if s.get("id") == "changes")
    assert names.index("Reject newly added gene review HTML") < changes


def test_gitignore_covers_review_html_only():
    def ignored(path: str) -> bool:
        result = subprocess.run(
            ["git", "check-ignore", "--no-index", "-q", path], cwd=ROOT, check=False
        )
        return result.returncode == 0

    assert ignored("genes/human/TP53/TP53-ai-review.html")
    assert not ignored("genes/human/TP53/TP53-ai-review.yaml")
    assert not ignored("genes/human/TP53/TP53-pathway.html")
