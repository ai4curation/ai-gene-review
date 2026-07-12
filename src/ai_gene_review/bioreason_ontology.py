"""Frozen GO ontology access for the BioReason benchmark audit."""
from __future__ import annotations

import urllib.request
from pathlib import Path
from typing import Any


GO_RELEASE = "2026-03-25"
FROZEN_GO_ADAPTER = f"frozen-go-{GO_RELEASE}"
GO_RELEASE_URL = (
    f"https://release.geneontology.org/{GO_RELEASE}/ontology/go-basic.obo"
)
REPO_ROOT = Path(__file__).resolve().parents[2]
FROZEN_GO_PATH = REPO_ROOT / "cache" / "ontologies" / f"go-basic-{GO_RELEASE}.obo"


def ensure_frozen_go() -> Path:
    """Return the pinned GO file, downloading the archived release if needed."""
    if FROZEN_GO_PATH.exists() and FROZEN_GO_PATH.stat().st_size > 1_000_000:
        return FROZEN_GO_PATH

    FROZEN_GO_PATH.parent.mkdir(parents=True, exist_ok=True)
    temporary = FROZEN_GO_PATH.with_suffix(".obo.tmp")
    request = urllib.request.Request(
        GO_RELEASE_URL,
        headers={"User-Agent": "ai-gene-review-bioreason-audit/1.0"},
    )
    with urllib.request.urlopen(request, timeout=120) as response, temporary.open(
        "wb"
    ) as handle:
        while chunk := response.read(1024 * 1024):
            handle.write(chunk)
    if temporary.stat().st_size <= 1_000_000:
        temporary.unlink(missing_ok=True)
        raise RuntimeError(f"Downloaded GO release is unexpectedly small: {GO_RELEASE_URL}")
    temporary.replace(FROZEN_GO_PATH)
    return FROZEN_GO_PATH


def get_go_adapter(adapter_spec: str = FROZEN_GO_ADAPTER) -> Any:
    """Load the pinned GO release or an explicitly requested OAK adapter."""
    from oaklib import get_adapter

    if adapter_spec == FROZEN_GO_ADAPTER:
        return get_adapter(f"pronto:{ensure_frozen_go()}")
    return get_adapter(adapter_spec)
