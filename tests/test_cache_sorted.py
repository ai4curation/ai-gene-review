"""Guard: committed term-validator caches stay sorted by CURIE and deduplicated.

Older tool versions appended cache entries out of order, which let git's line-based
merge mis-align and duplicate rows. linkml-term-validator now writes these caches
sorted+deduped; this test keeps the committed files that way so the drift can't
return. If it fails, run:

    uv run python -m ai_gene_review.tools.cache_lint --fix
"""

import pytest

from ai_gene_review.tools.cache_lint import (
    check_file,
    default_repo_root,
    iter_cache_files,
)

_ROOT = default_repo_root()
_CACHE_FILES = iter_cache_files(_ROOT)


def test_cache_files_exist():
    """Sanity: we actually found the caches to guard (glob/root not silently empty)."""
    assert _CACHE_FILES, f"no cache CSV/TSV files found under {_ROOT}/cache"


@pytest.mark.parametrize("path", _CACHE_FILES, ids=lambda p: str(p.relative_to(_ROOT)))
def test_cache_sorted_and_deduped(path):
    problems = check_file(path)
    assert not problems, (
        f"{path.relative_to(_ROOT)} is not sorted/deduplicated: {problems}. "
        "Fix with: uv run python -m ai_gene_review.tools.cache_lint --fix"
    )
