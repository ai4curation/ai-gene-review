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
and the SDK is pinned to Biohub/esm from GitHub (MIT, https://github.com/Biohub/esm).
The exact SDK surface has historically moved faster than the PyPI wheel, so this
caller targets the documented GitHub ``fold_all_atom`` API and keeps the single
network call isolated. Run ``--check-sdk`` to print the resolved client/input
surface before submitting.

No ESMFold2 output is GO curation evidence on its own; it is triage only.
"""

from __future__ import annotations

import argparse
import dataclasses
import json
import os
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

    proteins = [ProteinInput(id=cid, sequence=seq) for cid, seq in chains]
    return StructurePredictionInput(sequences=proteins)


def make_client(model: str, url: str, token: str) -> Any:
    from esm.sdk.forge import SequenceStructureForgeInferenceClient  # type: ignore

    return SequenceStructureForgeInferenceClient(model=model, url=url, token=token)


def make_folding_config() -> Any:
    from esm.sdk.api import FoldingConfig  # type: ignore

    return FoldingConfig(
        include_pair_chains_iptm=True,
        num_loops=3,
        num_sampling_steps=32,
    )


def check_input_builder_surface() -> bool:
    """Return whether the SDK input-builder classes needed for a run import."""
    try:
        from esm.sdk.api import FoldingConfig  # noqa: F401
        from esm.utils.structure.input_builder import (  # noqa: F401
            ProteinInput,
            StructurePredictionInput,
        )
    except ImportError as e:
        print(f"input-builder classes: IMPORT FAILED ({e})")
        return False
    print("input-builder classes: ProteinInput, StructurePredictionInput OK")
    return True


def run_prediction(client: Any, structure_input: Any) -> Any:
    """Call the hosted fold endpoint.

    The published Biohub ESMFold2 complex surface exposes ``fold_all_atom``.
    Keep this call isolated so any future SDK rename is localized.
    """
    method = getattr(client, "fold_all_atom", None)
    if callable(method):
        return method(structure_input, config=make_folding_config())
    raise AttributeError(
        "Could not find fold_all_atom on "
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
        summary["ptm"] = _to_jsonable(ptm)
    if iptm is not None:
        summary["iptm"] = _to_jsonable(iptm)
        # Boltz analyzers treat confidence_score as the headline number.
        summary.setdefault("confidence_score", _to_jsonable(iptm))
    if plddt is not None:
        summary["complex_plddt"] = _mean_or_jsonable(plddt)
    if pair is not None:
        summary["pair_chains_iptm"] = _to_jsonable(pair)
    return summary


def _mean_or_jsonable(obj: Any) -> Any:
    value = obj.detach().float().cpu() if hasattr(obj, "detach") else obj
    mean = getattr(value, "mean", None)
    if callable(mean):
        try:
            mean_value = mean()
            return mean_value.item() if hasattr(mean_value, "item") else mean_value
        except Exception:  # noqa: BLE001
            pass
    return _to_jsonable(obj)


def _to_jsonable(obj: Any) -> Any:
    if dataclasses.is_dataclass(obj):
        return {
            field.name: _to_jsonable(getattr(obj, field.name))
            for field in dataclasses.fields(obj)
        }
    if hasattr(obj, "tolist"):
        try:
            return obj.tolist()
        except Exception:  # noqa: BLE001
            pass
    if hasattr(obj, "item"):
        try:
            return obj.item()
        except Exception:  # noqa: BLE001
            pass
    if hasattr(obj, "detach"):
        try:
            return _to_jsonable(obj.detach().cpu().tolist())
        except Exception:  # noqa: BLE001
            pass
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
    complex_obj = _get(response, "complex")
    method = getattr(complex_obj, "to_mmcif", None)
    if callable(method):
        text = method()
        if isinstance(text, str) and text.strip():
            return text
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


def ensure_mmcif_occupancy(cif: str) -> str:
    """Fill default occupancy values when Biohub omits the atom_site column.

    Bio.PDB's MMCIFParser requires ``_atom_site.occupancy``. Biohub's current
    ``to_mmcif()`` output includes B-factors/confidence but omits occupancy, so
    add a neutral 1.00 occupancy column without altering coordinates.
    """
    lines = cif.splitlines()
    for loop_idx, line in enumerate(lines):
        if line.strip() != "loop_":
            continue
        col_start = loop_idx + 1
        col_end = col_start
        while col_end < len(lines) and lines[col_end].strip().startswith("_atom_site."):
            col_end += 1
        cols = [line.strip() for line in lines[col_start:col_end]]
        if not cols or "_atom_site.occupancy" in cols:
            continue
        if "_atom_site.B_iso_or_equiv" not in cols:
            continue
        insert_at = cols.index("_atom_site.B_iso_or_equiv") + 1
        lines.insert(col_start + insert_at, "_atom_site.occupancy")
        row_idx = col_end + 1
        while row_idx < len(lines) and lines[row_idx].strip() != "#":
            if lines[row_idx].startswith(("ATOM ", "HETATM ")):
                parts = lines[row_idx].split()
                if len(parts) == len(cols):
                    parts.insert(insert_at, "1.00")
                    lines[row_idx] = " ".join(parts)
            row_idx += 1
        return "\n".join(line.rstrip() for line in lines) + "\n"
    suffix = "\n" if cif.endswith("\n") else ""
    return "\n".join(line.rstrip() for line in lines) + suffix


def write_outputs(response: Any, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / RAW_NAME).write_text(
        json.dumps(_to_jsonable(response), indent=2) + "\n", encoding="utf-8"
    )

    cif = extract_cif(response)
    if cif is not None:
        cif = ensure_mmcif_occupancy(cif)
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

    token = os.environ.get("BIOHUB_API_TOKEN") or os.environ.get("ESM_API_TOKEN")

    if args.check_sdk:
        try:
            client = make_client(args.model, args.url, token or "DRY-RUN")
        except Exception as e:  # noqa: BLE001
            sys.stderr.write(f"Could not construct client: {e}\n")
            return 2
        fold_methods = [
            n for n in ("fold_all_atom", "fold", "predict", "structure_predict")
            if callable(getattr(client, n, None))
        ]
        print(f"client: {type(client).__name__}")
        print(f"fold-like methods present: {fold_methods or 'NONE FOUND'}")
        input_builder_ok = check_input_builder_surface()
        return 0 if "fold_all_atom" in fold_methods and input_builder_ok else 2

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
            "to get the pinned Biohub/esm SDK.\n"
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
