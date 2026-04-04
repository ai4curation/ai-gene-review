"""Classification and novelty scoring for immunity predictions."""

from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path

import numpy as np
import yaml

from ai_gene_review.prok_immunity_prediction.models import (
    ExternalHit,
    FamilyDefinition,
    PreparedProteome,
    ProteinPrediction,
)


def load_family_config(path: Path) -> dict[str, FamilyDefinition]:
    """Load canonical defense families from YAML."""
    raw = yaml.safe_load(path.read_text(encoding="utf-8"))
    families: dict[str, FamilyDefinition] = {}
    for entry in raw.get("families", []):
        family = FamilyDefinition(
            name=entry["name"],
            term_id=entry["term_id"],
            description=entry["description"],
            aliases=list(entry.get("aliases", [])),
        )
        families[family.name] = family
    return families


def classify_proteins(
    prepared: PreparedProteome,
    embeddings: dict[str, np.ndarray],
    external_hits: list[ExternalHit],
    families: dict[str, FamilyDefinition],
    family_threshold: float = 0.55,
    novel_threshold: float = 0.62,
    neighborhood_window: int = 10,
) -> list[ProteinPrediction]:
    """Predict known defense families and nominate novel candidates."""
    hits_by_protein: dict[str, list[ExternalHit]] = defaultdict(list)
    for hit in external_hits:
        hits_by_protein[hit.protein_id].append(hit)

    seed_families: dict[str, str] = {}
    for protein_id, hits in hits_by_protein.items():
        canonical = resolve_consensus_family(hits, families)
        if canonical:
            seed_families[protein_id] = canonical

    centroids = compute_family_centroids(seed_families, embeddings)
    defense_centroid = compute_defense_centroid(seed_families, embeddings)
    neighborhood_scores = compute_neighborhood_scores(
        prepared=prepared,
        seed_protein_ids=set(seed_families),
        window_size=neighborhood_window,
    )

    predictions: list[ProteinPrediction] = []
    for protein in prepared.proteins:
        protein_embedding = embeddings[protein.protein_id]
        family_scores: dict[str, float] = {}
        for family_name, centroid in centroids.items():
            similarity = cosine_similarity(protein_embedding, centroid)
            family_scores[family_name] = max((similarity + 1.0) / 2.0, 0.0)

        external_family = seed_families.get(protein.protein_id)
        if external_family:
            family_scores[external_family] = max(family_scores.get(external_family, 0.0), 0.95)

        best_family, best_score = best_family_score(family_scores)
        neighborhood_score = neighborhood_scores.get(protein.protein_id, 0.0)
        defense_score = (
            max((cosine_similarity(protein_embedding, defense_centroid) + 1.0) / 2.0, 0.0)
            if defense_centroid is not None
            else 0.0
        )
        if external_family:
            defense_score = max(defense_score, 0.85)

        predicted_novel = False
        novel_score = 0.0
        if not hits_by_protein.get(protein.protein_id):
            novel_score = 0.65 * defense_score + 0.35 * neighborhood_score
            predicted_novel = novel_score >= novel_threshold and neighborhood_score >= 0.2

        evidence = build_evidence(
            protein_id=protein.protein_id,
            external_hits=hits_by_protein.get(protein.protein_id, []),
            best_family=best_family,
            best_score=best_score,
            defense_score=defense_score,
            neighborhood_score=neighborhood_score,
            predicted_novel=predicted_novel,
        )
        if best_score < family_threshold and not hits_by_protein.get(protein.protein_id):
            best_family = None

        predictions.append(
            ProteinPrediction(
                protein=protein,
                family_scores=dict(sorted(family_scores.items(), key=lambda item: item[1], reverse=True)),
                best_family=best_family,
                family_confidence=best_score,
                defense_score=defense_score,
                neighborhood_score=neighborhood_score,
                novel_score=novel_score,
                predicted_novel=predicted_novel,
                external_hits=hits_by_protein.get(protein.protein_id, []),
                evidence=evidence,
            )
        )
    return predictions


def resolve_consensus_family(
    hits: list[ExternalHit],
    families: dict[str, FamilyDefinition],
) -> str | None:
    """Resolve a canonical family name from tool-specific labels."""
    votes: Counter[str] = Counter()
    for hit in hits:
        label = " ".join(part for part in [hit.system, hit.subtype or "", hit.raw_label or ""] if part)
        canonical = canonicalize_family(label, families)
        if canonical:
            votes[canonical] += 1
    if not votes:
        return None
    return votes.most_common(1)[0][0]


def canonicalize_family(label: str, families: dict[str, FamilyDefinition]) -> str | None:
    """Map free-text system labels onto canonical defense families."""
    normalized = normalize_label(label)
    for family in families.values():
        if normalize_label(family.name) in normalized:
            return family.name
        for alias in family.aliases:
            alias_norm = normalize_label(alias)
            if alias_norm and alias_norm in normalized:
                return family.name
    return None


def compute_family_centroids(
    seed_families: dict[str, str],
    embeddings: dict[str, np.ndarray],
) -> dict[str, np.ndarray]:
    """Compute one centroid per seeded family."""
    vectors: dict[str, list[np.ndarray]] = defaultdict(list)
    for protein_id, family_name in seed_families.items():
        embedding = embeddings.get(protein_id)
        if embedding is not None:
            vectors[family_name].append(embedding)
    return {
        family_name: np.vstack(embedding_list).mean(axis=0)
        for family_name, embedding_list in vectors.items()
        if embedding_list
    }


def compute_defense_centroid(
    seed_families: dict[str, str],
    embeddings: dict[str, np.ndarray],
) -> np.ndarray | None:
    """Aggregate all seeded defense embeddings into one centroid."""
    vectors = [embeddings[protein_id] for protein_id in seed_families if protein_id in embeddings]
    if not vectors:
        return None
    return np.vstack(vectors).mean(axis=0)


def compute_neighborhood_scores(
    prepared: PreparedProteome,
    seed_protein_ids: set[str],
    window_size: int = 10,
) -> dict[str, float]:
    """Score local defense density along each contig."""
    by_contig: dict[str, list[str]] = defaultdict(list)
    for protein in prepared.proteins:
        contig = protein.contig or "unknown_contig"
        by_contig[contig].append(protein.protein_id)

    scores: dict[str, float] = {}
    for protein_ids in by_contig.values():
        for index, protein_id in enumerate(protein_ids):
            lo = max(0, index - window_size)
            hi = min(len(protein_ids), index + window_size + 1)
            neighborhood = protein_ids[lo:hi]
            if len(neighborhood) <= 1:
                scores[protein_id] = 0.0
                continue
            seeds = sum(1 for neighbor in neighborhood if neighbor in seed_protein_ids and neighbor != protein_id)
            scores[protein_id] = seeds / max(len(neighborhood) - 1, 1)
    return scores


def build_evidence(
    protein_id: str,
    external_hits: list[ExternalHit],
    best_family: str | None,
    best_score: float,
    defense_score: float,
    neighborhood_score: float,
    predicted_novel: bool,
) -> list[str]:
    """Create human-readable reasons for a call."""
    evidence: list[str] = []
    if external_hits:
        databases = ", ".join(sorted({hit.database for hit in external_hits}))
        labels = ", ".join(sorted({hit.raw_label or hit.system for hit in external_hits}))
        evidence.append(f"{protein_id} cross-referenced by {databases}: {labels}")
    if best_family:
        evidence.append(
            f"Embedding classifier favors {best_family} (score={best_score:.2f}, defense-score={defense_score:.2f})."
        )
    if neighborhood_score > 0:
        evidence.append(f"Defense-neighborhood score={neighborhood_score:.2f}.")
    if predicted_novel:
        evidence.append("Marked as a novel candidate because it lacks database hits but sits in a defense-rich neighborhood.")
    return evidence


def best_family_score(family_scores: dict[str, float]) -> tuple[str | None, float]:
    """Return the top family and score."""
    if not family_scores:
        return None, 0.0
    best_family = max(family_scores, key=family_scores.get)
    return best_family, family_scores[best_family]


def cosine_similarity(left: np.ndarray, right: np.ndarray | None) -> float:
    """Cosine similarity that tolerates missing centroids."""
    if right is None:
        return 0.0
    left_norm = np.linalg.norm(left)
    right_norm = np.linalg.norm(right)
    if left_norm == 0 or right_norm == 0:
        return 0.0
    return float(np.dot(left, right) / (left_norm * right_norm))


def normalize_label(label: str) -> str:
    """Lower-case and remove punctuation for substring matching."""
    return "".join(ch for ch in label.lower() if ch.isalnum())
