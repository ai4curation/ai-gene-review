"""Retrospective CAFA-style scoring for ARGO139 SFT GO-term predictions.

This is not a true CAFA benchmark: ARGO139 is retrospective, the predictions
are not a timestamped pre-holdout submission, and BioReason-Pro SFT files do
not carry model confidence scores. The script therefore computes a single
threshold, CAFA-style GOA agreement score over propagated GO term sets.

Outputs are written under projects/BIOREASON_COMPARISON/cafa-style/.
"""
from __future__ import annotations

import argparse
import csv
import math
import urllib.request
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import matplotlib.pyplot as plt
import pandas as pd
import pronto
import yaml


PROJECT_DIR = Path(__file__).resolve().parent
REPO_ROOT = PROJECT_DIR.parents[1]
GENES_DIR = REPO_ROOT / "genes"
CACHE_DIR = REPO_ROOT / "cache" / "ontologies"
DEFAULT_ONTOLOGY = CACHE_DIR / "go-basic.obo"
OUT_DIR = PROJECT_DIR / "cafa-style"
FIGURE_PATH = PROJECT_DIR / "article" / "figures" / "cafa_style_argo139_sft.png"

GO_BASIC_URLS = [
    "https://current.geneontology.org/ontology/go-basic.obo",
    "http://purl.obolibrary.org/obo/go/go-basic.obo",
]

ASPECT_ROOTS = {
    "molecular_function": "GO:0003674",
    "biological_process": "GO:0008150",
    "cellular_component": "GO:0005575",
}
ROOT_IDS = set(ASPECT_ROOTS.values())

TERM_TYPE_TO_ASPECT = {
    "GO_MF": "molecular_function",
    "GO_BP": "biological_process",
    "GO_CC": "cellular_component",
}

GOA_ASPECT_ALIASES = {
    "molecular_function": "molecular_function",
    "biological_process": "biological_process",
    "cellular_component": "cellular_component",
    "F": "molecular_function",
    "P": "biological_process",
    "C": "cellular_component",
}

EXPERIMENTAL_EVIDENCE = {
    "EXP",
    "IDA",
    "IPI",
    "IMP",
    "IGI",
    "IEP",
    "HTP",
    "HDA",
    "HMP",
    "HGI",
    "HEP",
}


@dataclass(frozen=True)
class Prediction:
    organism: str
    gene: str
    source_version: str
    term_id: str
    term_label: str
    aspect: str
    assessment: str


@dataclass(frozen=True)
class GoaTerm:
    organism: str
    gene: str
    term_id: str
    term_label: str
    aspect: str
    evidence_code: str


class GoGraph:
    """Small wrapper around pronto for GO true-path propagation."""

    def __init__(self, path: Path) -> None:
        self.ontology = pronto.Ontology(path)
        self._closure_cache: dict[str, frozenset[str]] = {}
        self._direct_parent_cache: dict[str, frozenset[str]] = {}
        self.unresolved: Counter[str] = Counter()

    def aspect(self, term_id: str) -> str | None:
        term = self.ontology.get(term_id)
        if term is None:
            return None
        namespace = getattr(term, "namespace", None)
        return str(namespace) if namespace else None

    def direct_parents(self, term_id: str) -> frozenset[str]:
        if term_id in self._direct_parent_cache:
            return self._direct_parent_cache[term_id]
        term = self.ontology.get(term_id)
        if term is None:
            self.unresolved[term_id] += 1
            parents: frozenset[str] = frozenset()
            self._direct_parent_cache[term_id] = parents
            return parents

        parent_ids: set[str] = set()
        superclasses = term.superclasses(with_self=False, distance=1)
        superclass_set = (
            superclasses.to_set()
            if hasattr(superclasses, "to_set")
            else set(superclasses)
        )
        parent_ids.update(parent.id for parent in superclass_set)

        for relationship, targets in term.relationships.items():
            relationship_id = getattr(relationship, "id", str(relationship))
            if relationship_id != "part_of":
                continue
            parent_ids.update(parent.id for parent in targets)

        parents = frozenset(parent_ids)
        self._direct_parent_cache[term_id] = parents
        return parents

    def closure(self, term_id: str) -> frozenset[str]:
        """Return self plus is_a/part_of ancestors, excluding aspect roots."""
        if term_id in self._closure_cache:
            return self._closure_cache[term_id]

        visited: set[str] = set()
        stack = [term_id]
        while stack:
            current = stack.pop()
            if current in visited:
                continue
            visited.add(current)
            stack.extend(parent for parent in self.direct_parents(current) if parent not in visited)

        visited.difference_update(ROOT_IDS)
        closure = frozenset(visited)
        self._closure_cache[term_id] = closure
        return closure

    def close_set(self, term_ids: Iterable[str]) -> set[str]:
        closed: set[str] = set()
        for term_id in term_ids:
            closed.update(self.closure(term_id))
        return closed


def download_ontology(path: Path) -> None:
    if path.exists() and path.stat().st_size > 1_000_000:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    last_error: Exception | None = None
    for url in GO_BASIC_URLS:
        try:
            request = urllib.request.Request(
                url,
                headers={"User-Agent": "ai-gene-review-cafa-style/1.0"},
            )
            with urllib.request.urlopen(request, timeout=120) as response, path.open("wb") as handle:
                while True:
                    chunk = response.read(1024 * 1024)
                    if not chunk:
                        break
                    handle.write(chunk)
            if path.stat().st_size > 1_000_000:
                return
        except Exception as error:  # pragma: no cover - exercised only on network failure
            last_error = error
    raise RuntimeError(f"Could not download go-basic.obo: {last_error}")


def read_argo139() -> dict[tuple[str, str], str]:
    path = PROJECT_DIR / "genes.csv"
    rows: dict[tuple[str, str], str] = {}
    with path.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            rows[(row["species"], row["symbol"])] = row["uniprot_id"]
    return rows


def read_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def read_predictions(argo_keys: set[tuple[str, str]]) -> list[Prediction]:
    predictions: list[Prediction] = []
    for path in sorted(GENES_DIR.glob("*/*/*-sft-predictions.yaml")):
        organism, gene = path.parts[-3], path.parts[-2]
        if (organism, gene) not in argo_keys:
            continue
        doc = read_yaml(path)
        for pred in doc.get("predictions", []) or []:
            term = pred.get("predicted_term", {}) or {}
            term_id = str(term.get("id") or "")
            term_type = str(pred.get("predicted_term_type") or "")
            aspect = TERM_TYPE_TO_ASPECT.get(term_type, "")
            if not term_id.startswith("GO:") or not aspect:
                continue
            review = pred.get("review", {}) or {}
            predictions.append(
                Prediction(
                    organism=organism,
                    gene=gene,
                    source_version=str(pred.get("source_version") or ""),
                    term_id=term_id,
                    term_label=str(term.get("label") or ""),
                    aspect=aspect,
                    assessment=str(review.get("assessment") or ""),
                )
            )
    return predictions


def parse_goa_file(path: Path, organism: str, gene: str) -> list[GoaTerm]:
    if not path.exists():
        return []
    terms: list[GoaTerm] = []
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        for row in reader:
            qualifier = row.get("QUALIFIER", "")
            if "NOT" in qualifier.split("|"):
                continue
            term_id = row.get("GO TERM", "")
            aspect = GOA_ASPECT_ALIASES.get(row.get("GO ASPECT", ""))
            evidence_code = row.get("GO EVIDENCE CODE", "")
            if not term_id.startswith("GO:") or not aspect:
                continue
            terms.append(
                GoaTerm(
                    organism=organism,
                    gene=gene,
                    term_id=term_id,
                    term_label=row.get("GO NAME", ""),
                    aspect=aspect,
                    evidence_code=evidence_code,
                )
            )
    return terms


def read_goa_terms(argo_keys: set[tuple[str, str]]) -> list[GoaTerm]:
    terms: list[GoaTerm] = []
    for organism, gene in sorted(argo_keys):
        path = GENES_DIR / organism / gene / f"{gene}-goa.tsv"
        terms.extend(parse_goa_file(path, organism, gene))
    return terms


def score_counts(predicted: set[str], reference: set[str]) -> dict[str, float | int]:
    tp = len(predicted & reference)
    fp = len(predicted - reference)
    fn = len(reference - predicted)
    precision = tp / (tp + fp) if tp + fp else math.nan
    recall = tp / (tp + fn) if tp + fn else math.nan
    f1 = (
        2 * precision * recall / (precision + recall)
        if not math.isnan(precision)
        and not math.isnan(recall)
        and precision + recall > 0
        else math.nan
    )
    return {
        "tp": tp,
        "fp": fp,
        "fn": fn,
        "precision": precision,
        "recall": recall,
        "f1": f1,
    }


def leaf_filter_terms(terms: set[str], graph: GoGraph) -> set[str]:
    """Remove predicted terms that are ancestors of another predicted term."""
    if len(terms) < 2:
        return set(terms)
    ancestor_terms: set[str] = set()
    for term_id in terms:
        ancestor_terms.update(graph.closure(term_id) - {term_id})
    return set(terms) - ancestor_terms


def source_group(prediction: Prediction) -> str:
    return (
        "hf_catalogue"
        if prediction.source_version == "wanglab/protein_catalogue"
        else "web_export"
    )


def build_term_maps(
    predictions: list[Prediction],
    goa_terms: list[GoaTerm],
    graph: GoGraph,
) -> tuple[dict, dict]:
    pred_map: dict[tuple[str, str, str, str], set[str]] = defaultdict(set)
    ref_map: dict[tuple[str, str, str, str], set[str]] = defaultdict(set)

    for pred in predictions:
        for group in (source_group(pred), "all_sources"):
            pred_map[(group, pred.organism, pred.gene, pred.aspect)].add(pred.term_id)

    for term in goa_terms:
        ref_map[("goa_all", term.organism, term.gene, term.aspect)].add(term.term_id)
        if term.evidence_code in EXPERIMENTAL_EVIDENCE:
            ref_map[("goa_experimental", term.organism, term.gene, term.aspect)].add(term.term_id)

    # Touch all GO IDs once so unresolved reporting is deterministic.
    for terms in list(pred_map.values()) + list(ref_map.values()):
        for term_id in terms:
            graph.closure(term_id)
    return pred_map, ref_map


def summarize_scores(
    predictions: list[Prediction],
    goa_terms: list[GoaTerm],
    graph: GoGraph,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    pred_map, ref_map = build_term_maps(predictions, goa_terms, graph)
    keys = {(pred.organism, pred.gene) for pred in predictions}
    aspects = list(ASPECT_ROOTS)
    groups = ["hf_catalogue", "web_export", "all_sources"]
    reference_sets = ["goa_all", "goa_experimental"]
    modes = ["raw", "leaf_filtered"]

    per_gene_rows: list[dict] = []
    for group in groups:
        group_keys = {
            (pred.organism, pred.gene)
            for pred in predictions
            if group == "all_sources" or source_group(pred) == group
        }
        for reference_set in reference_sets:
            for mode in modes:
                for organism, gene in sorted(group_keys or keys):
                    for aspect in aspects:
                        pred_direct = set(pred_map.get((group, organism, gene, aspect), set()))
                        if mode == "leaf_filtered":
                            pred_direct = leaf_filter_terms(pred_direct, graph)
                        ref_direct = set(ref_map.get((reference_set, organism, gene, aspect), set()))
                        if not ref_direct:
                            continue

                        pred_closure = graph.close_set(pred_direct)
                        ref_closure = graph.close_set(ref_direct)
                        exact = score_counts(pred_direct, ref_direct)
                        closure = score_counts(pred_closure, ref_closure)
                        per_gene_rows.append(
                            {
                                "source_group": group,
                                "reference_set": reference_set,
                                "term_mode": mode,
                                "organism": organism,
                                "gene": gene,
                                "aspect": aspect,
                                "n_pred_direct": len(pred_direct),
                                "n_ref_direct": len(ref_direct),
                                "n_pred_closure": len(pred_closure),
                                "n_ref_closure": len(ref_closure),
                                **{f"exact_{key}": value for key, value in exact.items()},
                                **{f"closure_{key}": value for key, value in closure.items()},
                            }
                        )

    per_gene = pd.DataFrame(per_gene_rows)
    summary_rows: list[dict] = []
    for group_cols, frame in per_gene.groupby(
        ["source_group", "reference_set", "term_mode", "aspect"],
        dropna=False,
    ):
        source, reference_set, mode, aspect = group_cols
        summary_rows.append(summarize_frame(source, reference_set, mode, aspect, frame))
    for group_cols, frame in per_gene.groupby(
        ["source_group", "reference_set", "term_mode"],
        dropna=False,
    ):
        source, reference_set, mode = group_cols
        summary_rows.append(summarize_frame(source, reference_set, mode, "all_aspects", frame))
    summary = pd.DataFrame(summary_rows).sort_values(
        ["source_group", "reference_set", "term_mode", "aspect"]
    )
    return per_gene, summary


def summarize_frame(
    source_group_name: str,
    reference_set: str,
    mode: str,
    aspect: str,
    frame: pd.DataFrame,
) -> dict:
    row: dict[str, float | int | str] = {
        "source_group": source_group_name,
        "reference_set": reference_set,
        "term_mode": mode,
        "aspect": aspect,
        "n_gene_aspects": len(frame),
        "n_genes": frame[["organism", "gene"]].drop_duplicates().shape[0],
        "n_pred_direct": int(frame["n_pred_direct"].sum()),
        "n_ref_direct": int(frame["n_ref_direct"].sum()),
        "n_pred_closure": int(frame["n_pred_closure"].sum()),
        "n_ref_closure": int(frame["n_ref_closure"].sum()),
    }
    for prefix in ("exact", "closure"):
        tp = int(frame[f"{prefix}_tp"].sum())
        fp = int(frame[f"{prefix}_fp"].sum())
        fn = int(frame[f"{prefix}_fn"].sum())
        precision = tp / (tp + fp) if tp + fp else math.nan
        recall = tp / (tp + fn) if tp + fn else math.nan
        f1 = (
            2 * precision * recall / (precision + recall)
            if not math.isnan(precision)
            and not math.isnan(recall)
            and precision + recall > 0
            else math.nan
        )
        row.update(
            {
                f"{prefix}_tp": tp,
                f"{prefix}_fp": fp,
                f"{prefix}_fn": fn,
                f"{prefix}_precision": precision,
                f"{prefix}_recall": recall,
                f"{prefix}_f1": f1,
                f"{prefix}_macro_f1": frame[f"{prefix}_f1"].mean(skipna=True),
            }
        )
    return row


def assessment_overlap_table(
    predictions: list[Prediction],
    goa_terms: list[GoaTerm],
    graph: GoGraph,
) -> pd.DataFrame:
    goa_all_by_gene_aspect: dict[tuple[str, str, str], set[str]] = defaultdict(set)
    goa_exp_by_gene_aspect: dict[tuple[str, str, str], set[str]] = defaultdict(set)
    for term in goa_terms:
        key = (term.organism, term.gene, term.aspect)
        goa_all_by_gene_aspect[key].add(term.term_id)
        if term.evidence_code in EXPERIMENTAL_EVIDENCE:
            goa_exp_by_gene_aspect[key].add(term.term_id)

    rows = []
    for pred in predictions:
        key = (pred.organism, pred.gene, pred.aspect)
        all_direct = goa_all_by_gene_aspect.get(key, set())
        exp_direct = goa_exp_by_gene_aspect.get(key, set())
        all_closure = graph.close_set(all_direct)
        exp_closure = graph.close_set(exp_direct)
        pred_closure = graph.closure(pred.term_id)
        rows.append(
            {
                "source_group": source_group(pred),
                "organism": pred.organism,
                "gene": pred.gene,
                "aspect": pred.aspect,
                "term_id": pred.term_id,
                "assessment": pred.assessment,
                "exact_in_goa_all": pred.term_id in all_direct,
                "exact_in_goa_experimental": pred.term_id in exp_direct,
                "closure_intersects_goa_all": bool(pred_closure & all_closure),
                "closure_intersects_goa_experimental": bool(pred_closure & exp_closure),
            }
        )
    return pd.DataFrame(rows)


def write_markdown_summary(summary: pd.DataFrame, assessment_overlap: pd.DataFrame) -> None:
    rows = summary[
        (summary["reference_set"] == "goa_all")
        & (summary["term_mode"] == "raw")
        & (summary["aspect"] == "all_aspects")
    ].copy()
    rows = rows.set_index("source_group").loc[["hf_catalogue", "web_export", "all_sources"]]

    exp_rows = summary[
        (summary["reference_set"] == "goa_experimental")
        & (summary["term_mode"] == "raw")
        & (summary["aspect"] == "all_aspects")
    ].copy()
    exp_rows = exp_rows.set_index("source_group").loc[["hf_catalogue", "web_export", "all_sources"]]

    lines = [
        "# ARGO139 CAFA-style retrospective GOA agreement",
        "",
        "This is a retrospective CAFA-style score, not a true CAFA benchmark.",
        "Predictions are treated as an unranked single-threshold set because the",
        "BioReason-Pro SFT files do not contain model confidence scores.",
        "",
        "The score propagates predicted and reference GO terms over `is_a` and",
        "`part_of` ancestors from `go-basic.obo`, excluding the three GO aspect roots.",
        "",
        "## Propagated all-aspect agreement against current GOA",
        "",
        "| Source | genes | scored direct predictions | direct GOA terms | precision | recall | F1 |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    for source, row in rows.iterrows():
        lines.append(
            "| {source} | {genes} | {pred} | {ref} | {p:.3f} | {r:.3f} | {f:.3f} |".format(
                source=source,
                genes=int(row["n_genes"]),
                pred=int(row["n_pred_direct"]),
                ref=int(row["n_ref_direct"]),
                p=row["closure_precision"],
                r=row["closure_recall"],
                f=row["closure_f1"],
            )
        )

    lines.extend(
        [
            "",
            "## Propagated all-aspect agreement against experimental GOA only",
            "",
            "| Source | genes | scored direct predictions | experimental GOA terms | precision | recall | F1 |",
            "|---|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for source, row in exp_rows.iterrows():
        lines.append(
            "| {source} | {genes} | {pred} | {ref} | {p:.3f} | {r:.3f} | {f:.3f} |".format(
                source=source,
                genes=int(row["n_genes"]),
                pred=int(row["n_pred_direct"]),
                ref=int(row["n_ref_direct"]),
                p=row["closure_precision"],
                r=row["closure_recall"],
                f=row["closure_f1"],
            )
        )

    hf = assessment_overlap[assessment_overlap["source_group"] == "hf_catalogue"]
    exact_by_assessment = pd.crosstab(
        hf["assessment"],
        hf["exact_in_goa_all"],
        dropna=False,
    ).rename(columns={False: "not_exact_in_goa", True: "exact_in_goa"})
    hf_wrong = hf[hf["assessment"].isin(["NPI", "REP"])]
    wrong_exact = int(hf_wrong["exact_in_goa_all"].sum())
    wrong_closure = int(hf_wrong["closure_intersects_goa_all"].sum())
    lines.extend(
        [
            "",
            "## GOA agreement does not imply correctness",
            "",
            (
                f"In the HF catalogue subset, {wrong_exact}/{len(hf_wrong)} "
                "NPI/REP terms are exact matches to current GOA, and "
                f"{wrong_closure}/{len(hf_wrong)} have propagated overlap with "
                "current GOA. A retrospective GOA-agreement metric would therefore "
                "reward some terms that the evidence-grounded review classifies as "
                "wrong or frequency-biased."
            ),
            "",
            "## HF catalogue exact GOA overlap by AI-AUGR assessment",
            "",
            exact_by_assessment.to_markdown(),
            "",
            "Generated by `uv run python projects/BIOREASON_COMPARISON/cafa_style_argo139.py`.",
        ]
    )
    (OUT_DIR / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_figure(summary: pd.DataFrame) -> None:
    plot = summary[
        (summary["reference_set"] == "goa_all")
        & (summary["term_mode"] == "raw")
        & (summary["aspect"].isin(["molecular_function", "biological_process", "cellular_component"]))
    ].copy()
    source_order = ["hf_catalogue", "web_export", "all_sources"]
    aspect_order = ["molecular_function", "biological_process", "cellular_component"]
    colors = {
        "molecular_function": "#276749",
        "biological_process": "#2c5282",
        "cellular_component": "#975a16",
    }

    fig, axes = plt.subplots(1, 3, figsize=(10.5, 3.4), sharey=True)
    for ax, source in zip(axes, source_order, strict=True):
        frame = plot[plot["source_group"] == source].set_index("aspect")
        values = [frame.loc[aspect, "closure_f1"] if aspect in frame.index else math.nan for aspect in aspect_order]
        ax.bar(
            ["MF", "BP", "CC"],
            values,
            color=[colors[aspect] for aspect in aspect_order],
        )
        ax.set_title(source.replace("_", " "))
        ax.set_ylim(0, 1)
        for i, value in enumerate(values):
            if not math.isnan(value):
                ax.text(i, value + 0.02, f"{value:.2f}", ha="center", va="bottom", fontsize=9)
    axes[0].set_ylabel("propagated F1 vs current GOA")
    fig.suptitle("Retrospective CAFA-style GOA agreement for ARGO139 SFT terms", y=1.04)
    fig.tight_layout()

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    FIGURE_PATH.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT_DIR / "cafa_style_argo139_sft.png", dpi=180, bbox_inches="tight")
    fig.savefig(FIGURE_PATH, dpi=180, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--ontology",
        type=Path,
        default=DEFAULT_ONTOLOGY,
        help="Path to go-basic.obo; downloaded to cache if missing.",
    )
    args = parser.parse_args()

    download_ontology(args.ontology)
    graph = GoGraph(args.ontology)
    argo = read_argo139()
    argo_keys = set(argo)
    predictions = read_predictions(argo_keys)
    goa_terms = read_goa_terms(argo_keys)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    per_gene, summary = summarize_scores(predictions, goa_terms, graph)
    assessment_overlap = assessment_overlap_table(predictions, goa_terms, graph)

    per_gene.to_csv(OUT_DIR / "argo139_cafa_style_per_gene_aspect.csv", index=False)
    summary.to_csv(OUT_DIR / "argo139_cafa_style_summary.csv", index=False)
    assessment_overlap.to_csv(OUT_DIR / "argo139_prediction_goa_overlap.csv", index=False)
    write_markdown_summary(summary, assessment_overlap)
    write_figure(summary)

    unresolved = pd.DataFrame(
        [{"term_id": term_id, "count": count} for term_id, count in graph.unresolved.items()]
    ).sort_values(["count", "term_id"], ascending=[False, True])
    unresolved.to_csv(OUT_DIR / "unresolved_go_terms.csv", index=False)

    main_rows = summary[
        (summary["reference_set"] == "goa_all")
        & (summary["term_mode"] == "raw")
        & (summary["aspect"] == "all_aspects")
    ].set_index("source_group")
    print("Retrospective CAFA-style propagated all-aspect F1 vs current GOA")
    for source in ["hf_catalogue", "web_export", "all_sources"]:
        row = main_rows.loc[source]
        print(
            f"  {source}: P={row.closure_precision:.3f} "
            f"R={row.closure_recall:.3f} F1={row.closure_f1:.3f}"
        )
    if not unresolved.empty:
        print(f"Unresolved GO IDs: {len(unresolved)}; see {OUT_DIR / 'unresolved_go_terms.csv'}")
    print(f"Wrote {OUT_DIR}")


if __name__ == "__main__":
    main()
