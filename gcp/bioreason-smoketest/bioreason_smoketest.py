#!/usr/bin/env python3
"""Minimal BioReason smoke-test runner for GCP Batch.

This intentionally uses a reduced path:
- default BioReason checkpoint: public SFT checkpoint
- default GO-GPT checkpoint: public `wanglab/gogpt`
- no GO graph embedding injection for the first smoke test
- GO-GPT output is passed as text context in the prompt

The primary goal is to validate:
1. GPU container startup
2. checkpoint download/loading
3. prompt construction
4. single-sequence end-to-end generation
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Any

import torch
from huggingface_hub import snapshot_download


BIOREASON_PRO_DIR = Path(os.environ.get("BIOREASON_PRO_DIR", "/opt/BioReason-Pro"))
sys.path.insert(0, str(BIOREASON_PRO_DIR))
sys.path.insert(0, str(BIOREASON_PRO_DIR / "gogpt" / "src"))

from esm.models.esm3 import ESM3  # noqa: E402
from esm.pretrained import register_local_model  # noqa: E402

from bioreason2.dataset.cafa5.processor import _GO_INFO  # noqa: E402
from bioreason2.dataset.prompts.cafa5 import CAFA5_REASONING_TEMPLATE_WITH_CONTEXT  # noqa: E402
from bioreason2.models.protein_vllm import ProteinLLMModel  # noqa: E402
from gogpt.inference import GOGPTPredictor  # noqa: E402


BIOREASON_SFT_ALLOW_PATTERNS = [
    "added_tokens.json",
    "chat_template.jinja",
    "config.json",
    "generation_config.json",
    "merges.txt",
    "model-*.safetensors",
    "model.safetensors.index.json",
    "protein_model/*",
    "protein_projection.pt",
    "special_tokens_map.json",
    "tokenizer.json",
    "tokenizer_config.json",
    "vocab.json",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run a one-sequence BioReason smoke test.")
    parser.add_argument("--input-json", required=True, help="Input JSON with sequence + organism.")
    parser.add_argument("--output-dir", required=True, help="Directory for outputs.")
    parser.add_argument(
        "--bioreason-model-id",
        default="wanglab/bioreason-pro-sft",
        help="Hugging Face model id for the BioReason checkpoint.",
    )
    parser.add_argument(
        "--bioreason-checkpoint-dir",
        default=None,
        help="Local checkpoint directory. If set, skips HF download.",
    )
    parser.add_argument(
        "--gogpt-model-id",
        default="wanglab/gogpt",
        help="Hugging Face model id for GO-GPT.",
    )
    parser.add_argument(
        "--skip-gogpt",
        action="store_true",
        help="Skip GO-GPT and require go_speculations_text in the input JSON.",
    )
    parser.add_argument(
        "--cache-dir",
        default=os.environ.get("HF_HOME", "/workdir/hf-cache"),
        help="Shared cache directory for Hugging Face downloads.",
    )
    parser.add_argument(
        "--protein-model-name",
        default="esm3_sm_open_v1",
        help="Protein encoder name expected by BioReason-Pro.",
    )
    parser.add_argument(
        "--max-length-protein",
        type=int,
        default=2000,
        help="Maximum protein length to pass to the model.",
    )
    parser.add_argument(
        "--max-model-len",
        type=int,
        default=8192,
        help="vLLM max_model_len. Lower is better for this smoke test.",
    )
    parser.add_argument("--max-new-tokens", type=int, default=1200)
    parser.add_argument("--temperature", type=float, default=0.0)
    parser.add_argument("--top-p", type=float, default=0.95)
    parser.add_argument(
        "--enable-thinking",
        action="store_true",
        default=True,
        help="Keep Qwen thinking mode enabled.",
    )
    return parser.parse_args()


def load_input(path: str) -> dict[str, Any]:
    with open(path) as handle:
        data = json.load(handle)

    required = ["organism", "sequence"]
    missing = [field for field in required if not data.get(field)]
    if missing:
        raise ValueError(f"Missing required input fields: {', '.join(missing)}")

    data["sequence"] = data["sequence"].strip().upper()
    return data


def ensure_dir(path: str | Path) -> Path:
    resolved = Path(path)
    resolved.mkdir(parents=True, exist_ok=True)
    return resolved


def format_go_predictions(predictions: dict[str, list[str]]) -> str:
    aspect_names = {
        "MF": "Molecular Function",
        "BP": "Biological Process",
        "CC": "Cellular Component",
    }
    lines: list[str] = []
    for aspect in ["MF", "BP", "CC"]:
        ids = predictions.get(aspect, [])
        if not ids:
            lines.append(f"- {aspect_names[aspect]}: none")
            continue
        rendered = []
        for go_id in ids:
            label = _GO_INFO.get(go_id, ("Unknown", ""))[0]
            rendered.append(f"{go_id} ({label})")
        lines.append(f"- {aspect_names[aspect]}: " + "; ".join(rendered))
    return "\n".join(lines)


def maybe_download_bioreason_checkpoint(args: argparse.Namespace) -> Path:
    if args.bioreason_checkpoint_dir:
        return Path(args.bioreason_checkpoint_dir).resolve()

    cache_dir = ensure_dir(args.cache_dir)
    ckpt_dir = snapshot_download(
        repo_id=args.bioreason_model_id,
        cache_dir=str(cache_dir),
        allow_patterns=BIOREASON_SFT_ALLOW_PATTERNS,
    )
    return Path(ckpt_dir).resolve()


def register_checkpoint_protein_model(ckpt_dir: Path, protein_model_name: str) -> bool:
    protein_model_dir = ckpt_dir / "protein_model"
    if not protein_model_dir.exists():
        return False

    def _local_builder(device: torch.device | str = "cpu") -> ESM3:
        return ESM3.from_pretrained(str(protein_model_dir), device=device)

    register_local_model(protein_model_name, _local_builder)
    return True


def load_gogpt_predictions(
    sequence: str,
    organism: str,
    args: argparse.Namespace,
    cached_text: str | None,
) -> tuple[str, dict[str, list[str]] | None]:
    if cached_text:
        return cached_text, None
    if args.skip_gogpt:
        raise ValueError("GO-GPT was skipped but the input JSON did not include go_speculations_text.")

    predictor = GOGPTPredictor.from_pretrained(
        model_id=args.gogpt_model_id,
        cache_dir=args.cache_dir,
        device="cuda" if torch.cuda.is_available() else None,
        verbose=True,
    )
    predictions = predictor.predict(sequence=sequence, organism=organism)
    return format_go_predictions(predictions), predictions


def build_messages(organism: str, interpro_text: str, go_speculations_text: str) -> list[dict[str, Any]]:
    system_prompt = CAFA5_REASONING_TEMPLATE_WITH_CONTEXT["system_prompt"].strip()
    user_prompt = CAFA5_REASONING_TEMPLATE_WITH_CONTEXT["user_prompt"].format(
        organism=organism,
        interpro_data=interpro_text,
        go_speculations=go_speculations_text,
    ).strip()
    return [
        {
            "role": "user",
            "content": [
                {"type": "protein", "text": None},
                {
                    "type": "text",
                    "text": f"{system_prompt}\n\n{user_prompt}",
                },
            ],
        }
    ]


def main() -> int:
    args = parse_args()

    if not torch.cuda.is_available():
        raise RuntimeError("This smoke test expects a CUDA-capable GPU environment.")

    output_dir = ensure_dir(args.output_dir)
    input_data = load_input(args.input_json)

    if len(input_data["sequence"]) > args.max_length_protein:
        input_data["sequence"] = input_data["sequence"][: args.max_length_protein]

    ckpt_dir = maybe_download_bioreason_checkpoint(args)
    protein_model_registered = register_checkpoint_protein_model(
        ckpt_dir=ckpt_dir,
        protein_model_name=args.protein_model_name,
    )
    if not protein_model_registered:
        raise RuntimeError(
            "Checkpoint does not contain protein_model/. "
            "For the first smoke test, use the SFT checkpoint or provide a local protein_model bundle."
        )

    interpro_text = input_data.get("interpro_text") or "None"
    go_speculations_text, raw_go_predictions = load_gogpt_predictions(
        sequence=input_data["sequence"],
        organism=input_data["organism"],
        args=args,
        cached_text=input_data.get("go_speculations_text"),
    )

    model = ProteinLLMModel(
        ckpt_dir=str(ckpt_dir),
        protein_model_name=args.protein_model_name,
        max_length_protein=args.max_length_protein,
        max_length_text=args.max_model_len,
        max_model_len=args.max_model_len,
        max_num_seqs=1,
    )

    messages = build_messages(
        organism=input_data["organism"],
        interpro_text=interpro_text,
        go_speculations_text=go_speculations_text,
    )
    prompt_text = model.text_tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True,
        enable_thinking=args.enable_thinking,
    )

    model_inputs = model.processor(
        text=[prompt_text],
        batch_protein_sequences=[[input_data["sequence"]]],
        batch_go_aspects=None,
        max_length_text=args.max_model_len,
        max_length_protein=args.max_length_protein,
        device=str(model.device),
    )

    outputs = model.generate(
        input_ids=model_inputs["input_ids"],
        attention_mask=model_inputs["attention_mask"],
        protein_sequences=model_inputs["protein_sequences"],
        batch_idx_map=model_inputs["batch_idx_map"],
        go_aspects=None,
        max_new_tokens=args.max_new_tokens,
        temperature=args.temperature,
        top_p=args.top_p,
    )

    output_text = outputs[0]
    result = {
        "mode": "smoke-test-no-go-graph",
        "bioreason_model_id": args.bioreason_model_id,
        "bioreason_checkpoint_dir": str(ckpt_dir),
        "gogpt_model_id": None if args.skip_gogpt else args.gogpt_model_id,
        "input": input_data,
        "go_speculations_text": go_speculations_text,
        "raw_go_predictions": raw_go_predictions,
        "prompt_text": prompt_text,
        "output_text": output_text,
    }

    json_path = output_dir / "result.json"
    text_path = output_dir / "output.txt"
    json_path.write_text(json.dumps(result, indent=2))
    text_path.write_text(output_text)

    print(f"Wrote {json_path}")
    print(f"Wrote {text_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
