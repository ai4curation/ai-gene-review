"""Append repository dependencies and then run BioReason's own site customizer."""

import os
from pathlib import Path
import runpy
import site
import sys

# Keep this literal synchronized with run_bioreason_python.REPOSITORY_SITE_ENV.
repository_site = os.environ.get("AIGR_REPOSITORY_SITE_PACKAGES")
if repository_site:
    site.addsitedir(repository_site)

# This shim is first on PYTHONPATH, so explicitly chain the first different
# sitecustomize that BioReason's normal sys.path would otherwise have imported.
current_file = Path(__file__).resolve()
for path_entry in sys.path:
    entry = Path(path_entry or os.curdir)
    candidates = (
        entry / "sitecustomize.py",
        entry / "sitecustomize" / "__init__.py",
    )
    chained = next(
        (
            candidate
            for candidate in candidates
            if candidate.is_file() and candidate.resolve() != current_file
        ),
        None,
    )
    if chained:
        runpy.run_path(str(chained), run_name="_bioreason_original_sitecustomize")
        break
