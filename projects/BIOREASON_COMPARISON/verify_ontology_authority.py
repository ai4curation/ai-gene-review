"""Verify the BioReason frozen GO release against independent live authorities."""
from __future__ import annotations

import hashlib
import json
import urllib.parse
import urllib.request
from typing import Any

from ai_gene_review.bioreason_ontology import (
    GO_RELEASE_SENTINELS,
    GO_RELEASE_SHA256,
    GO_RELEASE_URL,
)


QUICKGO_URL = "https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/{go_id}"
OLS_URL = "https://www.ebi.ac.uk/ols4/api/ontologies/go/terms?obo_id={go_id}"
USER_AGENT = "ai-gene-review-bioreason-ontology-audit/1.0"


def open_url(url: str):
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    return urllib.request.urlopen(request, timeout=120)


def remote_sha256(url: str) -> str:
    digest = hashlib.sha256()
    with open_url(url) as response:
        while chunk := response.read(1024 * 1024):
            digest.update(chunk)
    return digest.hexdigest()


def fetch_json(url: str) -> dict[str, Any]:
    with open_url(url) as response:
        payload = json.load(response)
    if not isinstance(payload, dict):
        raise RuntimeError(f"Expected an object from {url}")
    return payload


def quickgo_state(go_id: str) -> tuple[str, bool]:
    encoded = urllib.parse.quote(go_id, safe="")
    payload = fetch_json(QUICKGO_URL.format(go_id=encoded))
    results = payload.get("results") or []
    if len(results) != 1 or results[0].get("id") != go_id:
        raise RuntimeError(f"QuickGO did not return exactly {go_id}")
    return str(results[0].get("name")), bool(results[0].get("isObsolete"))


def ols_state(go_id: str) -> tuple[str, bool]:
    encoded = urllib.parse.quote(go_id, safe="")
    payload = fetch_json(OLS_URL.format(go_id=encoded))
    terms = (payload.get("_embedded") or {}).get("terms") or []
    matches = [term for term in terms if term.get("obo_id") == go_id]
    if len(matches) != 1:
        raise RuntimeError(f"OLS did not return exactly {go_id}")
    return str(matches[0].get("label")), bool(matches[0].get("is_obsolete"))


def main() -> None:
    digest = remote_sha256(GO_RELEASE_URL)
    if digest != GO_RELEASE_SHA256:
        raise RuntimeError(
            f"Official archive checksum mismatch: expected {GO_RELEASE_SHA256}, found {digest}"
        )
    print(f"official_archive\t{digest}\tMATCH")

    for go_id, (expected_label, expected_obsolete) in GO_RELEASE_SENTINELS.items():
        if not expected_obsolete:
            continue
        quickgo = quickgo_state(go_id)
        ols = ols_state(go_id)
        expected = (expected_label, True)
        if quickgo != expected or ols != expected:
            raise RuntimeError(
                f"External authority mismatch for {go_id}: "
                f"expected {expected!r}, QuickGO={quickgo!r}, OLS={ols!r}"
            )
        print(f"{go_id}\t{expected_label}\tQuickGO=obsolete\tOLS=obsolete")


if __name__ == "__main__":
    main()
