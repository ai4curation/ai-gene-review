"""Advisory CI warnings for shared project/status files in content PRs."""

import importlib.util
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / ".github/scripts/warn_shared_content_paths.py"


def load_script():
    spec = importlib.util.spec_from_file_location("warn_shared_content_paths", SCRIPT)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def run_warning(*paths: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(SCRIPT), *paths],
        check=False,
        capture_output=True,
        text=True,
    )


def test_content_pr_with_project_status_warns():
    result = run_warning(
        "genes/BRUMA/bma-dpy-18.2/bma-dpy-18.2-ai-review.yaml",
        "history/genes/BRUMA/bma-dpy-18.2/session.yaml",
        "projects/NEMATODE_PATHOGENS.md",
    )
    assert result.returncode == 0
    assert "::warning title=Shared project/page files in content PR::" in result.stdout
    assert "projects/NEMATODE_PATHOGENS.md" in result.stdout


def test_content_pr_with_rendered_pages_warns():
    result = run_warning(
        "modules/nematode_cuticle_collagen_maturation.yaml",
        "pages/projects/NEMATODE_PATHOGENS.html",
        "pages/modules/nematode_cuticle_collagen_maturation.html",
    )
    assert result.returncode == 0
    assert "pages/projects/NEMATODE_PATHOGENS.html" in result.stdout
    assert "pages/modules/nematode_cuticle_collagen_maturation.html" in result.stdout


def test_content_pr_with_shared_cache_warns():
    result = run_warning(
        "genes/ASPFU/pptA/pptA-ai-review.yaml",
        "cache/go/terms.csv",
        "interpro/panther/panther.obo",
        "projects/collections.yaml",
    )
    assert result.returncode == 0
    assert "cache/go/terms.csv" in result.stdout
    assert "interpro/panther/panther.obo" in result.stdout
    assert "projects/collections.yaml" in result.stdout


def test_shared_cache_only_does_not_warn():
    result = run_warning(
        "cache/go/terms.csv",
        "interpro/panther/panther.obo",
    )
    assert result.returncode == 0
    assert "::warning" not in result.stdout


def test_workflow_stdin_path_warns():
    result = subprocess.run(
        [sys.executable, str(SCRIPT)],
        input=(
            "genes/ASPFU/pptA/pptA-ai-review.yaml\n"
            "projects/FUNGAL_PAINT_FAMILIES.md\n"
        ),
        check=False,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "projects/FUNGAL_PAINT_FAMILIES.md" in result.stdout


def test_status_only_and_project_subpages_do_not_warn():
    result = run_warning(
        "history/projects/NEMATODE_PATHOGENS/session.yaml",
        "projects/NEMATODE_PATHOGENS.md",
        "projects/NEMATODE_PATHOGENS/notes.md",
    )
    assert result.returncode == 0
    assert "::warning" not in result.stdout


def test_content_paths_include_family_reviews():
    script = load_script()

    assert script.is_content_path("interpro/panther/PTHR43323/PTHR43323-review.yaml")
    assert script.is_content_path("interpro/panther/PTHR43323/PTHR43323-paint.tsv")
    assert script.is_content_path("history/other/PTHR43323-family-review/session.yaml")
    assert script.is_shared_path("interpro/panther/panther.obo")
    assert not script.is_content_path("interpro/panther/panther.obo")
    assert not script.is_content_path("history/projects/FUNGAL_PAINT_FAMILIES/session.yaml")


def test_github_warning_property_escape_includes_commas_and_colons():
    script = load_script()

    assert script.escape_github_command("a:b,c%\n") == "a%3Ab%2Cc%25%0A"


def test_workflow_runs_warning_as_advisory_pr_check():
    workflow = yaml.safe_load((ROOT / ".github/workflows/main.yaml").read_text())
    steps = workflow["jobs"]["validation"]["steps"]
    step = next(s for s in steps if s.get("name") == "Warn about shared files")

    assert "github.event_name == 'pull_request'" in step["if"]
    assert not step.get("continue-on-error")
    assert ".github/scripts/warn_shared_content_paths.py" in step["run"]
    assert "python3" in step["run"]
    assert "gh api --paginate" in step["run"]
    assert "PIPESTATUS" in step["run"]
