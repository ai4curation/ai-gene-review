"""Shared parsing/analysis helpers for the BioReason-Pro comparison stats notebooks.

Everything here reads the *committed* per-gene files under ``genes/`` and derives
the summary statistics quoted in ``projects/BIOREASON_COMPARISON.md`` and the
manuscript. Nothing is hard-coded: every number a notebook prints is computed
from the files on disk, so the notebooks double as an audit of those tables.

Data sources
------------
- ``genes/<species>/<gene>/<gene>-bioreason-rl-review.md``  -> RL narrative scores
- ``genes/<species>/<gene>/<gene>-bioreason-sft-review.md`` -> SFT narrative scores
  (each contains ``- **Correctness**: N/5`` and ``- **Completeness**: N/5`` lines)
- ``genes/<species>/<gene>/<gene>-gogpt-leaf-predictions.yaml`` -> per-term
  prediction assessments (de Crecy-Lagard taxonomy in ``review.assessment``)
"""
from __future__ import annotations

import re
from pathlib import Path

import pandas as pd
import yaml

# --- score lines look like:  - **Correctness**: 4/5
_CORR_RE = re.compile(r"Correctness\*\*:\s*([0-5])\s*/\s*5", re.IGNORECASE)
_COMPL_RE = re.compile(r"Completeness\*\*:\s*([0-5])\s*/\s*5", re.IGNORECASE)


def find_repo_root(start: Path | None = None) -> Path:
    """Walk upward until we find the repo root (a dir containing ``genes/``)."""
    here = (start or Path.cwd()).resolve()
    for cand in (here, *here.parents):
        if (cand / "genes").is_dir() and (cand / "projects").is_dir():
            return cand
    raise FileNotFoundError(
        "Could not locate repo root (no ancestor with genes/ and projects/)."
    )


def parse_narrative_reviews(kind: str, repo_root: Path | None = None) -> pd.DataFrame:
    """Parse all BioReason narrative review files of a given ``kind``.

    Parameters
    ----------
    kind : 'rl' or 'sft'
    Returns a DataFrame with columns: species, gene, correctness, completeness, path.
    Files without both parseable scores are reported via ``.attrs['skipped']``.
    """
    if kind not in {"rl", "sft"}:
        raise ValueError("kind must be 'rl' or 'sft'")
    repo_root = repo_root or find_repo_root()
    rows, skipped = [], []
    pattern = f"genes/*/*/*-bioreason-{kind}-review.md"
    for path in sorted(repo_root.glob(pattern)):
        text = path.read_text(encoding="utf-8")
        c = _CORR_RE.search(text)
        k = _COMPL_RE.search(text)
        # genes/<species>/<gene>/<file>
        species, gene = path.parts[-3], path.parts[-2]
        if c and k:
            rows.append(
                dict(
                    species=species,
                    gene=gene,
                    correctness=int(c.group(1)),
                    completeness=int(k.group(1)),
                    path=str(path.relative_to(repo_root)),
                )
            )
        else:
            skipped.append(str(path.relative_to(repo_root)))
    df = pd.DataFrame(rows)
    df.attrs["skipped"] = skipped
    df.attrs["kind"] = kind
    return df


def load_prediction_assessments(repo_root: Path | None = None) -> pd.DataFrame:
    """Load every per-term assessment from the *-gogpt-leaf-predictions.yaml files.

    Returns one row per predicted term with columns: species, gene, source_method,
    term_id, term_label, term_type, assessment, confidence_score, path.
    """
    repo_root = repo_root or find_repo_root()
    rows = []
    for path in sorted(repo_root.glob("genes/*/*/*-gogpt-leaf-predictions.yaml")):
        species, gene = path.parts[-3], path.parts[-2]
        try:
            doc = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        except yaml.YAMLError:
            continue
        for pred in doc.get("predictions", []) or []:
            term = pred.get("predicted_term", {}) or {}
            review = pred.get("review", {}) or {}
            rows.append(
                dict(
                    species=species,
                    gene=gene,
                    source_method=pred.get("source_method"),
                    term_id=term.get("id"),
                    term_label=term.get("label"),
                    term_type=pred.get("predicted_term_type"),
                    assessment=review.get("assessment"),
                    confidence_score=review.get("confidence_score"),
                    path=str(path.relative_to(repo_root)),
                )
            )
    return pd.DataFrame(rows)


# Canonical ordering for the de Crecy-Lagard assessment taxonomy.
ASSESSMENT_ORDER = ["COR", "CNN", "LSP", "UNC", "PLI", "NPI", "REP"]
ASSESSMENT_GLOSS = {
    "COR": "Correct novel",
    "CNN": "Correct but Not Novel (already in GOA)",
    "LSP": "Less Precise than existing annotation",
    "UNC": "Uncertain - cannot validate or refute",
    "PLI": "Paralog Incorrect",
    "NPI": "Nonparalog Incorrect (refuted)",
    "REP": "Repetition / frequency bias",
}
