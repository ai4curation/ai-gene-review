"""Embedding backends used by the prokaryotic immunity pipeline."""

from __future__ import annotations

from typing import Protocol

import numpy as np

from ai_gene_review.prok_immunity_prediction.models import ProteinRecord

AMINO_ACIDS = "ACDEFGHIKLMNPQRSTVWY"


class ProteinEmbedder(Protocol):
    """Common interface for sequence embedders."""

    def embed_many(self, proteins: list[ProteinRecord]) -> dict[str, np.ndarray]:
        """Embed proteins keyed by protein ID."""


class CompositionEmbedder:
    """Lightweight fallback embedder for tests and dry runs."""

    def embed_many(self, proteins: list[ProteinRecord]) -> dict[str, np.ndarray]:
        embeddings: dict[str, np.ndarray] = {}
        for protein in proteins:
            embeddings[protein.protein_id] = composition_embedding(protein.sequence)
        return embeddings


class ESM2Embedder:
    """Embed proteins with a HuggingFace ESM-2 model."""

    def __init__(self, model_name: str = "facebook/esm2_t6_8M_UR50D") -> None:
        try:
            import torch
            from transformers import AutoTokenizer, EsmModel
        except ImportError as exc:  # pragma: no cover - optional dependency
            raise RuntimeError(
                "ESM-2 embedding requested but 'torch' and 'transformers' are not installed. "
                "Run via `uv run --with torch --with transformers ...` or use --embedder composition."
            ) from exc

        self._torch = torch
        self._tokenizer = AutoTokenizer.from_pretrained(model_name)
        self._model = EsmModel.from_pretrained(model_name)
        self._model.eval()
        self.model_name = model_name

    def embed_many(self, proteins: list[ProteinRecord]) -> dict[str, np.ndarray]:
        embeddings: dict[str, np.ndarray] = {}
        with self._torch.no_grad():  # pragma: no cover - exercised only with optional deps
            for protein in proteins:
                sequence = protein.sequence
                encoded = self._tokenizer(
                    sequence,
                    return_tensors="pt",
                    truncation=True,
                    max_length=1024,
                )
                outputs = self._model(**encoded)
                hidden = outputs.last_hidden_state[0]
                mask = encoded["attention_mask"][0].bool()
                pooled = hidden[mask].mean(dim=0)
                embeddings[protein.protein_id] = pooled.cpu().numpy()
        return embeddings


def build_embedder(name: str, model_name: str) -> ProteinEmbedder:
    """Factory for supported embedders."""
    normalized = name.lower()
    if normalized in {"composition", "heuristic", "aa-composition"}:
        return CompositionEmbedder()
    if normalized in {"esm2", "esm-2"}:
        return ESM2Embedder(model_name=model_name)
    raise ValueError(f"Unknown embedder '{name}'. Expected 'esm2' or 'composition'.")


def composition_embedding(sequence: str) -> np.ndarray:
    """Encode a sequence as simple composition and physicochemical features."""
    length = max(len(sequence), 1)
    aa_counts = np.array([sequence.count(aa) / length for aa in AMINO_ACIDS], dtype=float)
    hydrophobic = sum(sequence.count(aa) for aa in "AILMFWVY") / length
    polar = sum(sequence.count(aa) for aa in "STNQCY") / length
    charged = sum(sequence.count(aa) for aa in "DEKRH") / length
    gly_pro = sum(sequence.count(aa) for aa in "GP") / length
    length_feature = min(length / 2000.0, 1.0)
    return np.concatenate(
        [
            aa_counts,
            np.array([hydrophobic, polar, charged, gly_pro, length_feature], dtype=float),
        ]
    )
