#!/usr/bin/env python3
"""Submit a prepared payload to BioLM's hosted Boltz-2 API."""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parent
DEFAULT_PAYLOAD = ROOT / "inputs" / "cox2_sco1_sco2_coa6_domains_biolm.json"
DEFAULT_OUTPUT_DIR = ROOT / "biolm_boltz2_api_out"
DEFAULT_ENDPOINT = "https://biolm.ai/api/v3/boltz2/predict/"


def post_json(endpoint: str, payload: dict[str, Any], timeout: int) -> dict[str, Any]:
    api_key = os.environ.get("BIOLM_API_KEY") or os.environ.get("BIOLMAI_TOKEN")
    if not api_key:
        raise RuntimeError("Set BIOLM_API_KEY or BIOLMAI_TOKEN before calling the BioLM API.")

    request = Request(
        endpoint,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Token {api_key}",
        },
        method="POST",
    )

    with urlopen(request, timeout=timeout) as response:
        return json.loads(response.read().decode("utf-8"))


def write_text_if_string(path: Path, value: Any) -> None:
    if isinstance(value, str) and value.strip():
        path.write_text(value, encoding="utf-8")


def write_outputs(result: dict[str, Any], output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "boltz2_biolm_response.json").write_text(
        json.dumps(result, indent=2) + "\n",
        encoding="utf-8",
    )

    # BioLM may return structure text at top level or inside per-item outputs,
    # depending on API version and requested output format. Keep extraction broad
    # but preserve the full raw JSON either way.
    write_text_if_string(output_dir / "boltz2_biolm_model.cif", result.get("structure"))
    write_text_if_string(output_dir / "boltz2_biolm_model.cif", result.get("cif"))

    for collection_key in ("results", "items"):
        items = result.get(collection_key)
        if not isinstance(items, list):
            continue
        for i, item in enumerate(items):
            if not isinstance(item, dict):
                continue
            write_text_if_string(output_dir / f"boltz2_biolm_{collection_key}_{i}.cif", item.get("structure"))
            write_text_if_string(output_dir / f"boltz2_biolm_{collection_key}_{i}.cif", item.get("cif"))

    top_level_summary = {
        key: result.get(key)
        for key in [
            "confidence",
            "confidence_score",
            "confidence_scores",
            "ptm",
            "iptm",
            "protein_iptm",
            "complex_plddt",
            "complex_iplddt",
        ]
        if key in result
    }
    result_summaries = []
    results = result.get("results")
    if isinstance(results, list):
        for item in results:
            if isinstance(item, dict) and "confidence" in item:
                result_summaries.append(item["confidence"])

    summary = top_level_summary
    if result_summaries:
        summary["results"] = result_summaries

    if summary:
        (output_dir / "boltz2_biolm_summary.json").write_text(
            json.dumps(summary, indent=2) + "\n",
            encoding="utf-8",
        )


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Submit a Boltz-2 JSON payload to BioLM's hosted API."
    )
    parser.add_argument("--payload", type=Path, default=DEFAULT_PAYLOAD)
    parser.add_argument(
        "--endpoint",
        default=os.environ.get("BIOLM_BOLTZ2_URL", DEFAULT_ENDPOINT),
        help="Prediction endpoint URL. Can also be set with BIOLM_BOLTZ2_URL.",
    )
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--timeout", type=int, default=3600)
    args = parser.parse_args()

    payload = json.loads(args.payload.read_text(encoding="utf-8"))

    try:
        result = post_json(args.endpoint, payload, args.timeout)
    except RuntimeError as e:
        sys.stderr.write(str(e) + "\n")
        return 2
    except HTTPError as e:
        sys.stderr.write(f"HTTP {e.code} from {args.endpoint}\n")
        sys.stderr.write(e.read().decode("utf-8", errors="replace") + "\n")
        return 1
    except URLError as e:
        sys.stderr.write(f"Could not reach {args.endpoint}: {e.reason}\n")
        return 1

    write_outputs(result, args.output_dir)
    print(args.output_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
