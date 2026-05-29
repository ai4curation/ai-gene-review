#!/usr/bin/env python3
"""Submit a protein complex to the Biohub (biohub.ai) ESMFold2 hosted API.

This is the ESMFold2 counterpart to ``analysis/complex_iv_boltz/run_biolm_boltz2.py``.
It reads a multi-record FASTA (one record per chain), submits the chains as a
single complex prediction, and writes outputs using the SAME file convention as
the Boltz2 runs so the existing ``analyze_output.py`` scripts can read them
without modification:

  - ``esmfold2_model_0.cif``       (matched by the analyzers' ``*_model_0.cif`` / ``*.cif`` glob)
  - ``confidence_esmfold2.json``   (matched by the analyzers' ``confidence_*.json`` glob)
  - ``esmfold2_response.json``     (raw response, for provenance)

This makes the head-to-head re-run trivial, e.g.::

    python3 analysis/esmfold2/run_esmfold2.py \
        --fasta analysis/complex_iii_boltz/inputs/cyc1_uqcrfs1_ims_domains.fasta \
        --output-dir analysis/esmfold2/cyc1_uqcrfs1_domains_out
    python3 analysis/complex_iii_boltz/analyze_output.py \
        analysis/esmfold2/cyc1_uqcrfs1_domains_out

IMPORTANT / HONESTY NOTE
------------------------
The hosted endpoint is real (``https://biohub.ai``, model ``esmfold2-fast-2026-05``)
and the SDK is ``pip install esm`` (MIT, https://github.com/evolutionaryscale/esm).
However, the exact SDK method name and response attribute names below were taken
from the published docs/README and have NOT been executed against a live token in
this repo. The constructor, FASTA parsing, confidence extraction, and output
writing are all defensive, and the single network call is isolated and clearly
marked so it is a one-line fix if the installed SDK version differs. Run
``--check-sdk`` to print the resolved client surface before submitting.

No ESMFold2 output is GO curation evidence on its own; it is triage only.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent
DEFAULT_MODEL = "esmfold2-fast-2026-05"
DEFAULT_URL = "https://biohub.ai"
# The analyzers read these glob patterns; keep the names aligned.
CIF_NAME = "esmfold2_model_0.cif"
CONFIDENCE_NAME = "confidence_esmfold2.json"
RAW_NAME = "esmfold2_response.json"


def read_fasta(path: Path) -> list[tuple[str, str]]:
    """Return [(chain_id, sequence), ...].

    Chain id is the first ``|``-delimited field of the header if present
    (e.g. ``>A|CYC1|85-281|desc`` -> ``A``), else the first whitespace token,
    else an auto-assigned A, B, C, ...
    """
    records: list[tuple[str, list[str]]] = []
    header: str | None = None
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line:
            continue
        if line.startswith(">"):
            header = line[1:].strip()
            records.append((header, []))
        elif records:
            records[-1][1].append(line)
        else:
            raise ValueError(f"Sequence data before first header in {path}")

    alphabet = [chr(ord("A") + i) for i in range(26)]
    out: list[tuple[str, str]] = []
    for i, (hdr, seq_parts) in enumerate(records):
        token = hdr.split("|", 1)[0].split()[0] if hdr else ""
        chain_id = token if token else alphabet[i]
        out.append((chain_id, "".join(seq_parts).replace(" ", "").upper()))
    if not out:
        raise ValueError(f"No FASTA records found in {path}")
    return out


def build_structure_input(chains: list[tuple[str, str]]) -> Any:
    """Build an ESMFold2 complex input from (chain_id, sequence) pairs.

    Isolated so the SDK input-builder surface is easy to adjust in one place.
    """
    from esm.utils.structure.input_builder import (  # type: ignore
        ProteinInput,
        StructurePredictionInput,
    )

    proteins = [ProteinInput(sequence=seq, chain_id=cid) for cid, seq in chains]
    return StructurePredictionInput(proteins=proteins)


def make_client(model: str, url: str, token: str) -> Any:
    from esm.sdk.forge import SequenceStructureForgeInferenceClient  # type: ignore

    return SequenceStructureForgeInferenceClient(model=model, url=url, token=token)


def run_prediction(client: Any, structure_input: Any) -> Any:
    """Call the hosted fold endpoint.

    The published surface exposes a fold call on the client. We try the
    documented name and fall back across the small set of plausible aliases so a
    minor SDK rename surfaces a clear error rather than a silent failure.
    """
    for method_name in ("fold", "predict", "structure_predict"):
        method = getattr(client, method_name, None)
        if callable(method):
            return method(structure_input)
    raise AttributeError(
        "Could not find a fold/predict method on "
        f"{type(client).__name__}. Run with --check-sdk and adjust "
        "run_prediction() to match the installed esm SDK version."
    )


def _get(obj: Any, *names: str) -> Any:
    """Read a field from a dict or an object by trying several names."""
    for name in names:
        if isinstance(obj, dict) and name in obj:
            return obj[name]
        if hasattr(obj, name):
            return getattr(obj, name)
    return None


def extract_confidence(response: Any) -> dict[str, Any]:
    """Map ESMFold2 confidence onto the keys the Boltz analyzers already read.

    Boltz analyzers consume: ``confidence_score``, ``ptm``, ``iptm``,
    ``complex_plddt``, and a ``pair_chains_iptm`` matrix. We populate as many as
    ESMFold2 exposes (pLDDT mean, pTM, ipTM) and pass through any pair matrix.
    """
    summary: dict[str, Any] = {}

    iptm = _get(response, "iptm", "ipTM", "interface_ptm")
    ptm = _get(response, "ptm", "pTM", "predicted_tm")
    plddt = _get(response, "plddt", "pLDDT", "plddt_mean", "mean_plddt")
    pair = _get(response, "pair_chains_iptm", "pair_chain_iptm", "chain_pair_iptm")

    if ptm is not None:
        summary["ptm"] = ptm
    if iptm is not None:
        summary["iptm"] = iptm
        # Boltz analyzers treat confidence_score as the headline number.
        summary.setdefault("confidence_score", iptm)
    if plddt is not None:
        summary["complex_plddt"] = plddt
    if pair is not None:
        summary["pair_chains_iptm"] = pair
    return summary


def _to_jsonable(obj: Any) -> Any:
    try:
        json.dumps(obj)
        return obj
    except TypeError:
        for attr in ("model_dump", "dict", "to_dict", "__dict__"):
            val = getattr(obj, attr, None)
            if callable(val):
                try:
                    return _to_jsonable(val())
                except Exception:  # noqa: BLE001 - best-effort provenance dump
                    pass
            elif isinstance(val, dict):
                return {k: _to_jsonable(v) for k, v in val.items()}
        return repr(obj)


def extract_cif(response: Any) -> str | None:
    cif = _get(response, "cif", "structure", "mmcif", "cif_string")
    if isinstance(cif, str) and cif.strip():
        return cif
    # Some SDKs return a structure object with a to_cif/to_mmcif method.
    structure = _get(response, "protein_structure", "structure_object")
    for attr in ("to_cif", "to_mmcif_string", "to_pdb_string"):
        method = getattr(structure, attr, None) if structure is not None else None
        if callable(method):
            try:
                text = method()
                if isinstance(text, str) and text.strip():
                    return text
            except Exception:  # noqa: BLE001
                pass
    return None


def write_outputs(response: Any, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / RAW_NAME).write_text(
        json.dumps(_to_jsonable(response), indent=2) + "\n", encoding="utf-8"
    )

    cif = extract_cif(response)
    if cif is not None:
        (output_dir / CIF_NAME).write_text(cif, encoding="utf-8")
    else:
        sys.stderr.write(
            "WARNING: no CIF/structure text found in response; only raw response "
            f"written. Inspect {output_dir / RAW_NAME} and adjust extract_cif().\n"
        )

    summary = extract_confidence(response)
    if summary:
        (output_dir / CONFIDENCE_NAME).write_text(
            json.dumps(summary, indent=2) + "\n", encoding="utf-8"
        )
    else:
        sys.stderr.write(
            "WARNING: no confidence fields recognized; adjust extract_confidence().\n"
        )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--fasta",
        type=Path,
        required=False,
        help="Multi-record FASTA; one record per chain in the complex.",
    )
    parser.add_argument("--output-dir", type=Path, default=ROOT / "esmfold2_out")
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--url", default=DEFAULT_URL)
    parser.add_argument(
        "--check-sdk",
        action="store_true",
        help="Print the resolved esm SDK client/input surface and exit (no network call).",
    )
    args = parser.parse_args()

    import os

    token = os.environ.get("BIOHUB_API_TOKEN") or os.environ.get("ESM_API_TOKEN")

    if args.check_sdk:
        try:
            client = make_client(args.model, args.url, token or "DRY-RUN")
        except Exception as e:  # noqa: BLE001
            sys.stderr.write(f"Could not construct client: {e}\n")
            return 2
        fold_methods = [
            n for n in ("fold", "predict", "structure_predict")
            if callable(getattr(client, n, None))
        ]
        print(f"client: {type(client).__name__}")
        print(f"fold-like methods present: {fold_methods or 'NONE FOUND'}")
        return 0

    if not args.fasta:
        sys.stderr.write("--fasta is required unless using --check-sdk.\n")
        return 2
    if not token:
        sys.stderr.write(
            "Set BIOHUB_API_TOKEN (or ESM_API_TOKEN) with a biohub.ai token.\n"
        )
        return 2

    chains = read_fasta(args.fasta)
    print(f"Submitting {len(chains)} chains: {', '.join(c for c, _ in chains)}")

    try:
        client = make_client(args.model, args.url, token)
        structure_input = build_structure_input(chains)
        response = run_prediction(client, structure_input)
    except ModuleNotFoundError as e:
        sys.stderr.write(
            f"Missing dependency: {e}. Install with `uv sync` in analysis/esmfold2/ "
            "or `pip install esm`.\n"
        )
        return 2
    except Exception as e:  # noqa: BLE001 - surface the real error to the operator
        sys.stderr.write(f"Prediction failed: {type(e).__name__}: {e}\n")
        return 1

    write_outputs(response, args.output_dir)
    print(args.output_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
