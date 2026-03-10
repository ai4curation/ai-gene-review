#!/usr/bin/env python3
"""Generate de novo GO candidate assignments from a cached publication.

This is a curator-assist workflow for PMIDs that do not yet have GOA/QuickGO
annotations. It does NOT make final annotations automatically. Instead, it:

1. Reads a cached publication markdown file in publications/PMID_<pmid>.md
2. Extracts evidence sentences relevant to a gene symbol
3. Generates candidate GO search phrases from those sentences
4. Fuzzy-matches those phrases against the local GO cache in cache/ontologies/go.tsv
5. Writes a YAML review scaffold for curator completion
"""

from __future__ import annotations

import argparse
import csv
import re
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

import yaml
from rapidfuzz import fuzz


@dataclass(frozen=True)
class GOTerm:
    term_id: str
    label: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate de novo GO candidate assignments from a publication")
    parser.add_argument("pmid", help="PMID, with or without PMID: prefix")
    parser.add_argument("gene", help="Gene symbol to focus on")
    parser.add_argument(
        "--publication-file",
        default=None,
        help="Path to cached publication markdown. Default: publications/PMID_<pmid>.md",
    )
    parser.add_argument(
        "--go-cache",
        default="cache/ontologies/go.tsv",
        help="Path to GO label cache TSV",
    )
    parser.add_argument(
        "--max-sentences",
        type=int,
        default=25,
        help="Maximum number of evidence sentences to include",
    )
    parser.add_argument(
        "--output",
        default=None,
        help="Output YAML path. Default: projects/publication_annotation_review/reviews/PMID_<pmid>-<gene>-denovo.yaml",
    )
    return parser.parse_args()


def normalize_pmid(raw: str) -> str:
    return re.sub(r"^(PMID:)\s*", "", raw.strip(), flags=re.IGNORECASE)


def read_publication_text(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    if text.startswith("---\n"):
        parts = text.split("---\n", 2)
        if len(parts) == 3:
            text = parts[2]
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"\1", text)
    text = re.sub(r"^#+\s+", "", text, flags=re.MULTILINE)
    return text


def split_sentences(text: str) -> list[str]:
    text = re.sub(r"\s+", " ", text)
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z0-9])", text)
    return [p.strip() for p in parts if len(p.strip()) > 40]


RESULT_HINTS = [
    "increase", "increased", "decrease", "decreased", "enhanced", "reduced",
    "promotes", "promoted", "inhibits", "inhibited", "required", "necessary",
    "binds", "binding", "activity", "localized", "localization", "cytoplasm",
    "cytosol", "nucleus", "membrane", "complex", "autophagy", "signaling",
    "production", "secretion", "expression", "phosphorylation",
]


def select_evidence_sentences(text: str, gene: str, max_sentences: int) -> list[str]:
    sentences = split_sentences(text)
    gene_upper = gene.upper()
    ranked: list[tuple[int, str]] = []
    for sent in sentences:
        score = 0
        sent_upper = sent.upper()
        if gene_upper in sent_upper:
            score += 5
        for hint in RESULT_HINTS:
            if hint in sent.lower():
                score += 1
        if score > 0:
            ranked.append((score, sent))
    ranked.sort(key=lambda x: (-x[0], len(x[1])))

    seen: set[str] = set()
    chosen: list[str] = []
    for _, sent in ranked:
        norm = sent.lower()
        if norm in seen:
            continue
        seen.add(norm)
        chosen.append(sent)
        if len(chosen) >= max_sentences:
            break
    return chosen


def infer_search_phrases(sentence: str, gene: str) -> list[str]:
    s = sentence.strip()
    low = s.lower()
    phrases: list[str] = []

    # Direct regulation phrases already present in text
    direct_patterns = [
        r"(positive regulation of [a-z0-9\- ]+)",
        r"(negative regulation of [a-z0-9\- ]+)",
        r"(regulation of [a-z0-9\- ]+)",
        r"([a-z0-9\- ]+ activity)",
        r"([a-z0-9\- ]+ binding)",
    ]
    for pattern in direct_patterns:
        for match in re.findall(pattern, low):
            phrase = re.sub(r"\s+", " ", match).strip(" .,;:")
            if 4 <= len(phrase) <= 100:
                phrases.append(phrase)

    keyword_map = {
        "autophagy": ["autophagy"],
        "il-8": ["interleukin-8 production"],
        "interleukin-8": ["interleukin-8 production"],
        "il-6": ["interleukin-6 production"],
        "interleukin-6": ["interleukin-6 production"],
        "tnf": ["tumor necrosis factor production"],
        "nf-κb": ["NF-kappaB signaling"],
        "nf-kappab": ["NF-kappaB signaling"],
        "jnk": ["JUN kinase activity"],
        "erk": ["ERK1 and ERK2 cascade"],
        "phosphatase": ["phosphatase activity", "protein tyrosine phosphatase activity"],
        "cytoplasm": ["cytoplasm"],
        "cytosol": ["cytosol"],
        "nucleus": ["nucleus"],
        "membrane": ["membrane"],
        "ubiquitination": ["protein K63-linked ubiquitination"],
        "lipopolysaccharide": ["response to lipopolysaccharide", "lipopolysaccharide-mediated signaling pathway"],
        "muramyl dipeptide": ["cellular response to muramyl dipeptide"],
        "nod2": ["nucleotide-binding oligomerization domain containing 2 signaling pathway"],
    }
    for token, vals in keyword_map.items():
        if token in low:
            phrases.extend(vals)

    # Simple polarity inference from perturbation language
    if re.search(r"(loss|deficien|knockdown|deletion) of .* (increase|enhance)", low) or re.search(r"(deficien|knockdown).*(increased|enhanced)", low):
        if "autophagy" in low:
            phrases.append("negative regulation of autophagy")
        if "il-8" in low or "interleukin-8" in low:
            phrases.append("negative regulation of interleukin-8 production")
        if "il-6" in low or "interleukin-6" in low:
            phrases.append("negative regulation of interleukin-6 production")
        if "tnf" in low:
            phrases.append("negative regulation of tumor necrosis factor production")
    if re.search(r"(loss|deficien|knockdown|deletion) of .* (reduce|decrease)", low) or re.search(r"(deficien|knockdown).*(reduced|decreased)", low):
        if "autophagy" in low:
            phrases.append("positive regulation of autophagy")

    # Clean
    cleaned: list[str] = []
    seen: set[str] = set()
    for phrase in phrases:
        phrase = re.sub(re.escape(gene.lower()), "", phrase.lower())
        phrase = re.sub(r"\s+", " ", phrase).strip(" ,.;:")
        if phrase and phrase not in seen:
            seen.add(phrase)
            cleaned.append(phrase)
    return cleaned[:8]


def load_go_cache(path: Path) -> list[GOTerm]:
    terms: list[GOTerm] = []
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        for row in reader:
            if str(row.get("is_obsolete", "")).lower() == "true":
                continue
            terms.append(GOTerm(term_id=row["term_id"], label=row["label"]))
    return terms


def guess_aspect(label: str) -> str:
    low = label.lower()
    if any(x in low for x in ["activity", "binding", "transporter", "receptor", "catalytic"]):
        return "molecular_function"
    if any(x in low for x in ["nucleus", "cytoplasm", "cytosol", "membrane", "complex", "organelle", "chromosome", "vesicle"]):
        return "cellular_component"
    return "biological_process"


def match_terms(phrases: list[str], terms: list[GOTerm], limit: int = 5) -> list[dict[str, Any]]:
    matches: list[dict[str, Any]] = []
    seen: set[str] = set()
    for phrase in phrases:
        scored: list[tuple[float, GOTerm]] = []
        for term in terms:
            score = max(
                fuzz.ratio(phrase, term.label.lower()),
                fuzz.token_sort_ratio(phrase, term.label.lower()),
                fuzz.partial_ratio(phrase, term.label.lower()),
            )
            if score >= 86:
                scored.append((score, term))
        scored.sort(key=lambda x: (-x[0], len(x[1].label)))
        for score, term in scored[:limit]:
            if term.term_id in seen:
                continue
            seen.add(term.term_id)
            matches.append(
                {
                    "query_phrase": phrase,
                    "term": {
                        "id": term.term_id,
                        "label": term.label,
                        "aspect_guess": guess_aspect(term.label),
                    },
                    "match_score": round(float(score), 1),
                }
            )
    return matches[:limit]


def build_entry(idx: int, sentence: str, gene: str, go_terms: list[GOTerm]) -> dict[str, Any]:
    phrases = infer_search_phrases(sentence, gene)
    return {
        "candidate_id": f"CAND-{idx:04d}",
        "evidence_sentence": sentence,
        "suggested_go_search_phrases": phrases,
        "matched_go_terms": match_terms(phrases, go_terms),
        "curator_review": {
            "decision": "PENDING",
            "selected_term": None,
            "confidence": "",
            "supporting_text": sentence,
            "notes": "",
        },
    }


def main() -> None:
    args = parse_args()
    pmid = normalize_pmid(args.pmid)
    pub_path = Path(args.publication_file) if args.publication_file else Path("publications") / f"PMID_{pmid}.md"
    if not pub_path.exists():
        raise SystemExit(f"Publication file not found: {pub_path}. Run 'just fetch-pmid {pmid}' first.")

    go_cache_path = Path(args.go_cache)
    if not go_cache_path.exists():
        raise SystemExit(f"GO cache not found: {go_cache_path}")

    text = read_publication_text(pub_path)
    evidence_sentences = select_evidence_sentences(text, args.gene, args.max_sentences)
    if not evidence_sentences:
        raise SystemExit(f"No evidence sentences found for gene {args.gene} in {pub_path}")

    go_terms = load_go_cache(go_cache_path)
    candidates = [build_entry(i, sent, args.gene, go_terms) for i, sent in enumerate(evidence_sentences, start=1)]

    payload = {
        "publication_denovo_review": {
            "reference_id": f"PMID:{pmid}",
            "gene_symbol": args.gene,
            "generated_at": datetime.now(UTC).isoformat(),
            "source_publication_file": str(pub_path),
            "method": "sentence extraction + heuristic GO phrase generation + fuzzy match to local GO cache",
            "limitations": [
                "Candidate GO terms are suggestions only and require curator review.",
                "Directionality inference is heuristic and may be wrong.",
                "Only GO terms present in the local cache can be matched automatically.",
                "Figure legends and tables are only used if present in the cached publication text.",
            ],
            "candidates": candidates,
        }
    }

    output_path = Path(args.output) if args.output else Path("projects/publication_annotation_review/reviews") / f"PMID_{pmid}-{args.gene}-denovo.yaml"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as handle:
        yaml.safe_dump(payload, handle, sort_keys=False, allow_unicode=True, width=120)
    print(f"Wrote {len(candidates)} de novo candidates to {output_path}")


if __name__ == "__main__":
    main()
