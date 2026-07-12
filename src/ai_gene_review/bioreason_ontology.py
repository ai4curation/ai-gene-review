"""Frozen GO ontology access for the BioReason benchmark audit."""
from __future__ import annotations

import hashlib
import urllib.request
from pathlib import Path
from typing import Any


GO_RELEASE = "2026-03-25"
FROZEN_GO_ADAPTER = f"frozen-go-{GO_RELEASE}"
GO_RELEASE_URL = (
    f"https://release.geneontology.org/{GO_RELEASE}/ontology/go-basic.obo"
)
GO_RELEASE_SHA256 = "a77e356737dab39a4f620dce35fc4d6eb531c4b6153af6cacaaa322b49b804bd"
GO_RELEASE_SENTINELS: dict[str, tuple[str, bool]] = {
    "GO:0000002": ("obsolete mitochondrial genome maintenance", True),
    "GO:0000003": ("obsolete reproduction", True),
    "GO:0005615": ("obsolete extracellular space", True),
    "GO:0005844": ("obsolete polysome", True),
    "GO:0007568": ("obsolete aging", True),
    "GO:0005576": ("extracellular region", False),
    "GO:0022414": ("reproductive process", False),
    "GO:0051082": ("unfolded protein binding", False),
}
REPO_ROOT = Path(__file__).resolve().parents[2]
FROZEN_GO_PATH = REPO_ROOT / "cache" / "ontologies" / f"go-basic-{GO_RELEASE}.obo"


def frozen_go_sha256(path: Path) -> str:
    """Return a streaming SHA-256 digest for a GO release file."""
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while chunk := handle.read(1024 * 1024):
            digest.update(chunk)
    return digest.hexdigest()


def validate_frozen_go_file(path: Path) -> None:
    """Fail if the cached ontology is not the pinned archived release."""
    actual = frozen_go_sha256(path)
    if actual != GO_RELEASE_SHA256:
        raise RuntimeError(
            f"GO release checksum mismatch for {path}: "
            f"expected {GO_RELEASE_SHA256}, found {actual}"
        )


def validate_frozen_go_adapter(adapter: Any) -> None:
    """Assert release-specific active and obsolete sentinel semantics."""
    obsolete = set(adapter.obsoletes())
    failures: list[str] = []
    for go_id, (expected_label, expected_obsolete) in GO_RELEASE_SENTINELS.items():
        actual_label = adapter.label(go_id)
        actual_obsolete = go_id in obsolete
        if (actual_label, actual_obsolete) != (expected_label, expected_obsolete):
            failures.append(
                f"{go_id}: expected {(expected_label, expected_obsolete)!r}, "
                f"found {(actual_label, actual_obsolete)!r}"
            )
    if failures:
        raise RuntimeError(
            f"GO release {GO_RELEASE} failed ontology sentinel checks: "
            + "; ".join(failures)
        )


def ensure_frozen_go() -> Path:
    """Return the pinned GO file, downloading the archived release if needed."""
    if FROZEN_GO_PATH.exists() and FROZEN_GO_PATH.stat().st_size > 1_000_000:
        validate_frozen_go_file(FROZEN_GO_PATH)
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
    try:
        validate_frozen_go_file(temporary)
    except RuntimeError:
        temporary.unlink(missing_ok=True)
        raise
    temporary.replace(FROZEN_GO_PATH)
    return FROZEN_GO_PATH


def get_go_adapter(adapter_spec: str = FROZEN_GO_ADAPTER) -> Any:
    """Load the pinned GO release or an explicitly requested OAK adapter."""
    from oaklib import get_adapter

    if adapter_spec == FROZEN_GO_ADAPTER:
        adapter = get_adapter(f"pronto:{ensure_frozen_go()}")
        validate_frozen_go_adapter(adapter)
        return adapter
    return get_adapter(adapter_spec)
