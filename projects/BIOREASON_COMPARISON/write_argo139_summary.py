"""Write ARGO139 cohort summaries and figures."""
from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path

import matplotlib.pyplot as plt


PROJECT_DIR = Path(__file__).resolve().parent
GENES_CSV = PROJECT_DIR / "genes.csv"
FIGURES_DIR = PROJECT_DIR / "article" / "figures"

SPECIALIST_RESOURCE_SPECIES = {
    "ARATH",
    "DROME",
    "ECOLI",
    "SCHPO",
    "human",
    "mouse",
    "rat",
    "worm",
    "yeast",
}

SPECIES_LABELS = {
    "9CAUD": "9CAUD phage",
    "AGKCO": "A. contortrix",
    "ANOGA": "A. gambiae",
    "ARATH": "A. thaliana",
    "BACSU": "B. subtilis",
    "DROME": "D. melanogaster",
    "ECOLI": "E. coli",
    "PSEPK": "P. putida",
    "SCHPO": "S. pombe",
    "human": "H. sapiens",
    "mouse": "M. musculus",
    "rat": "R. norvegicus",
    "worm": "C. elegans",
    "yeast": "S. cerevisiae",
}


def load_rows() -> list[dict[str, str]]:
    with GENES_CSV.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def context_for_species(species: str) -> str:
    if species in SPECIALIST_RESOURCE_SPECIES:
        return "model organism / specialist curation resource"
    return "non-MOD or less-specialized species"


def write_species_counts(rows: list[dict[str, str]]) -> None:
    counts = Counter(row["species"] for row in rows)
    path = PROJECT_DIR / "argo139-species-counts.csv"
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["species", "display_label", "n_genes", "curation_context"],
        )
        writer.writeheader()
        for species, n_genes in counts.most_common():
            writer.writerow(
                {
                    "species": species,
                    "display_label": SPECIES_LABELS.get(species, species),
                    "n_genes": n_genes,
                    "curation_context": context_for_species(species),
                }
            )


def write_context_counts(rows: list[dict[str, str]]) -> None:
    counts = Counter(context_for_species(row["species"]) for row in rows)
    path = PROJECT_DIR / "argo139-curation-context-counts.csv"
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["curation_context", "n_genes"])
        writer.writeheader()
        for context, n_genes in counts.most_common():
            writer.writerow({"curation_context": context, "n_genes": n_genes})


def write_species_figure(rows: list[dict[str, str]]) -> None:
    counts = Counter(row["species"] for row in rows)
    ordered = counts.most_common()
    species = [item[0] for item in ordered]
    values = [item[1] for item in ordered]
    colors = [
        "#2f6f73" if item in SPECIALIST_RESOURCE_SPECIES else "#b55d35"
        for item in species
    ]

    FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    fig, ax = plt.subplots(figsize=(8.4, 4.6), dpi=180)
    bars = ax.bar([SPECIES_LABELS.get(item, item) for item in species], values, color=colors)
    ax.set_ylabel("Genes")
    ax.set_title("ARGO139 species distribution")
    ax.spines[["top", "right"]].set_visible(False)
    ax.tick_params(axis="x", labelrotation=45)
    ax.grid(axis="y", color="#d8dee3", linewidth=0.8, alpha=0.7)
    ax.set_axisbelow(True)

    for bar, value in zip(bars, values):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            value + 0.4,
            str(value),
            ha="center",
            va="bottom",
            fontsize=8,
        )

    legend_handles = [
        plt.Rectangle((0, 0), 1, 1, color="#2f6f73"),
        plt.Rectangle((0, 0), 1, 1, color="#b55d35"),
    ]
    ax.legend(
        legend_handles,
        ["model organism / specialist curation resource", "non-MOD or less-specialized"],
        frameon=False,
        loc="upper right",
        fontsize=8,
    )
    fig.tight_layout()
    fig.savefig(FIGURES_DIR / "argo139_species_distribution.png")
    plt.close(fig)


def main() -> None:
    rows = load_rows()
    write_species_counts(rows)
    write_context_counts(rows)
    write_species_figure(rows)
    print(f"wrote {PROJECT_DIR / 'argo139-species-counts.csv'}")
    print(f"wrote {PROJECT_DIR / 'argo139-curation-context-counts.csv'}")
    print(f"wrote {FIGURES_DIR / 'argo139_species_distribution.png'}")


if __name__ == "__main__":
    main()
