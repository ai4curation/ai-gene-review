"""The validation hooks must resolve their repo root from the file being edited.

Regression test for a defect that silently cost curation work: hooks are invoked as
``$CLAUDE_PROJECT_DIR/.claude/hooks/<hook>.py``, so anchoring the root on ``__file__``
made a subagent working in a git worktree validate the **main checkout** instead. Files
the agent had just written -- a ``GENE-bioinformatics/RESULTS.md`` cited by a ``file:``
reference, or a publication fetched into its own ``publications/`` -- do not exist there,
so valid content was reported missing and then deleted in response.
"""

import importlib.util
import sys
from pathlib import Path

import pytest

HOOKS_DIR = Path(__file__).resolve().parent.parent / ".claude" / "hooks"


def _load_hook_paths():
    spec = importlib.util.spec_from_file_location("hook_paths", HOOKS_DIR / "hook_paths.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules["hook_paths"] = module
    spec.loader.exec_module(module)
    return module


hook_paths = _load_hook_paths()


@pytest.fixture
def fake_checkout(tmp_path):
    """A directory that looks like a checkout of this repo."""
    root = tmp_path / "worktree"
    (root / "genes" / "human" / "GENE").mkdir(parents=True)
    (root / "src").mkdir()
    review = root / "genes" / "human" / "GENE" / "GENE-ai-review.yaml"
    review.write_text("id: X\n")
    return root, review


def test_resolves_root_from_the_edited_file(fake_checkout):
    """The worktree holding the file wins over the hook's own location."""
    root, review = fake_checkout
    elsewhere = Path("/some/other/checkout")
    assert hook_paths.find_repo_root(review, elsewhere) == root


def test_does_not_return_the_hook_script_root_for_a_worktree_file(fake_checkout):
    """This is the defect: the old code returned the fallback unconditionally.

    Written as an explicit inequality so the test fails if someone reinstates a
    ``__file__``-derived root, rather than only checking the happy path.
    """
    root, review = fake_checkout
    main_checkout = Path("/main/checkout")
    assert hook_paths.find_repo_root(review, main_checkout) != main_checkout


def test_falls_back_when_the_file_is_outside_any_checkout(tmp_path):
    """A path in no checkout must still yield a usable root, not raise."""
    stray = tmp_path / "stray" / "GENE-ai-review.yaml"
    stray.parent.mkdir(parents=True)
    stray.write_text("id: X\n")
    fallback = Path("/fallback/root")
    assert hook_paths.find_repo_root(stray, fallback) == fallback


def test_genes_alone_is_not_a_repo_root(tmp_path):
    """``genes/`` without ``src/`` is an agent scratch dir, not a checkout."""
    partial = tmp_path / "scratch"
    (partial / "genes").mkdir(parents=True)
    assert not hook_paths.is_repo_root(partial)


def test_real_repo_root_is_detected():
    """The marker pair must actually identify this repository."""
    assert hook_paths.is_repo_root(HOOKS_DIR.parent.parent)


@pytest.mark.parametrize(
    "hook",
    [
        "validate_ai_review_hook.py",
        "validate_ai_review_pretool_hook.py",
        "validate_rule_review_hook.py",
    ],
)
def test_hooks_no_longer_anchor_their_root_on_file(hook):
    """None of the hooks may reconstruct a root from ``__file__`` inline.

    ``hook_script_root(__file__)`` is still permitted -- it is the *fallback* -- so this
    asserts against the specific inline idioms the bug used.
    """
    source = (HOOKS_DIR / hook).read_text()
    assert "Path(__file__).parent.parent.parent" not in source
    assert "os.path.dirname(os.path.dirname(__file__))" not in source
    assert "find_repo_root" in source
