#!/usr/bin/env python
"""One-off: enrich top-level project frontmatter with maturity/tags/species/genes.

Adds controlled-vocabulary metadata to every ``projects/*.md`` page so the
auto-generated all-projects index is transparent about coverage and project
state. Managed keys (``maturity``, ``tags``, ``species``, ``genes``) are inserted
immediately after ``title`` without reflowing any other existing frontmatter.

Vocabularies
------------
maturity: SCOPING | IN_PROGRESS | MATURE | COMPLETE | ARCHIVED
tags:     FLAGSHIP | OBSOLETION | PIPELINE | BIOLOGY_DOMAIN

Run with ``--dry`` to preview the classification without writing.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, "src")
from ai_gene_review.render_projects import parse_frontmatter  # noqa: E402

PROJECTS = Path("projects")

# Projects currently featured on the hand-curated index page -> FLAGSHIP.
FLAGSHIP = {
    "AD_HOC_BIOINFORMATICS", "ANTIMICROBIAL_RESISTANCE", "ANTI_CRISPR",
    "ARATH_HEAT_STRESS", "BACSU", "BGC", "BIOREASON_COMPARISON",
    "CAEEL_CILIOPATHY", "CAEEL_MITOPHAGY", "CAEEL_PROTEOSTASIS",
    "CAEEL_P_GRANULES", "CAEEL_SURVEILLANCE_IMMUNITY", "CAEEL_UPR_STRESS",
    "CELLULOSOME", "CEPHALOPOD", "CGAS_STING_PATHWAY", "CONTESTED_FUNCTION",
    "ECM", "ENZYME_SPECIFICITY", "ER_EXIT_SITE_LOCALIZATION_OBSOLETION",
    "ER_PHAGY", "ER_PM_TETHERING_OBSOLETION", "EVIDENCE_SOURCE_SUFFICIENCY",
    "FERROPTOSIS", "FUNCTION_KNOWLEDGE_GAPS", "IBA_REVIEW",
    "INTEGRATED_STRESS_RESPONSE", "IRON_SULFUR_CLUSTER_BIOGENESIS",
    "ISOFORMS", "KAURENE_OXIDATION_OBSOLETION", "MECHANOBIOLOGY",
    "METABOLIC_MODEL_ANALYSIS", "METEA_MLL_CLUSTER", "MIRNA_DEGRADATION",
    "MITOCHONDRION_TARGETING_SEQUENCE_BINDING_OBSOLETION", "MITOPHAGY",
    "MITO_ER_TETHERING_OBSOLETION", "NEUROBLAST_PROLIFERATION_DISAMBIGUATION",
    "NEURON_DEVELOPMENT", "NICOTINE_BIOSYNTHESIS", "NITV2_PATHWAYS",
    "NLRP3_INFLAMMASOME", "OVER_ANNOTATION_PATTERNS", "PAINT",
    "PHOSPHORYLATION_REFACTOR", "PROTEIN_COMPLEX_FUNCTIONS", "PROTEOSTASIS",
    "PSEUDOENZYMES", "RIBOSOME_QUALITY_CONTROL", "SDH_GP2TERM_CONTRIBUTES_TO",
    "SPKW", "STRESS_GRANULES", "SURVEILLANCE_IMMUNITY_CURATION_RECOMMENDATIONS",
    "SYNAPTIC_VESICLE_DOCKING_OBSOLETION", "TARDIGRADE_STRESS_RESPONSE",
    "UNFOLDED_PROTEIN_BINDING", "UNIPATHWAY", "UNIPROT_CAUTION_NOTE",
    "VALIDATING_ECOLI_PREDICTIONS", "VESICLE_TARGETING_OBSOLETION",
    "YEAST_CELL_CYCLE", "YEAST_DNA_REPAIR_CHROMATIN",
    "YEAST_EPIGENETICS_HISTONE_INHERITANCE", "YEAST_METABOLIC_ENGINEERING",
    "YEAST_REPLICATIVE_AGING",
}

# Cross-cutting methodology / tooling / annotation-process projects -> PIPELINE.
# Everything non-obsoletion that is NOT here is treated as BIOLOGY_DOMAIN.
PIPELINE = {
    "AD_HOC_BIOINFORMATICS", "ALPHAFOLD", "ASSAY_TO_FUNCTION", "BIOINFORMATICS",
    "BIOREASON_COMPARISON", "CONTESTED_FUNCTION", "ENZYME_SPECIFICITY",
    "EVIDENCE_SOURCE_SUFFICIENCY", "FUNCTION_KNOWLEDGE_GAPS", "IBA_REVIEW",
    "ISO", "ISOFORMS", "METABOLIC_MODEL_ANALYSIS", "ORTHOLOG_CONJECTURE",
    "OVER_ANNOTATION_PATTERNS", "PAINT", "PDB", "PHOSPHORYLATION_REFACTOR",
    "PROKARYOTIC_IMMUNITY_TERM_PREDICTION", "PROTEIN_COMPLEX_FUNCTIONS",
    "PROTEOME_REMOVAL", "PSEUDOENZYMES", "REACTOME_GAP_FILLING",
    "SDH_GP2TERM_CONTRIBUTES_TO", "SPKW", "STRUCTURE_FUNCTION", "TOP_NOTS",
    "UNIPATHWAY", "UNIPROT_CAUTION_NOTE", "VALIDATING_ECOLI_PREDICTIONS",
}

# Explicit species assignments (slugs not listed keep any existing species and
# are otherwise left blank rather than guessed).
SPECIES = {
    "ARATH_HEAT_STRESS": ["ARATH"],
    "AUTOIMMUNE": ["human"],
    "BACSU": ["BACSU"],
    "CGAS_STING_PATHWAY": ["human"],
    "ECM": ["human"],
    "ER_PHAGY": ["human"],
    "FERROPTOSIS": ["human"],
    "INTEGRATED_STRESS_RESPONSE": ["human"],
    "IRON_SULFUR_CLUSTER_BIOGENESIS": ["human"],
    "MECHANOBIOLOGY": ["human"],
    "METEA_MLL_CLUSTER": ["METEA"],
    "MITOCHONDRIAL_IMPORT_PATHWAYS": ["human"],
    "MITOPHAGY": ["human"],
    "NITV2_PATHWAYS": ["DESVH"],
    "NLRP3_INFLAMMASOME": ["human"],
    "PAINT": ["human"],
    "PEROXISOME": ["human"],
    "RIBOSOME_QUALITY_CONTROL": ["human"],
    "STRESS_GRANULES": ["human"],
    "TARDIGRADE_STRESS_RESPONSE": ["RAMVA"],
    "VALIDATING_ECOLI_PREDICTIONS": ["ECOLI"],
}

# Small, explicitly enumerated gene sets (from project sidecar genes.csv files).
GENES = {
    "MIRNA_DEGRADATION": [
        "ZSWIM8", "CUL3", "ARIH1", "ELOB", "ELOC", "AGO2", "AGO1", "AGO3", "AGO4",
    ],
    "NICOTINE_BIOSYNTHESIS": [
        "NaAO2", "NaNAMNH", "NaQPT2", "NaODC1", "NaODC2", "NaPMT1.1", "NaPMT1.2",
        "NaMPO1", "NaUGT1", "NaA622", "NaBBL1", "NaBBL2", "NaBGL1", "NaBGL2",
        "NaMATE1", "NaNUP", "NaERF1-like", "NaMYC2",
    ],
    "ISOFORMS": [
        "POMC", "App", "APP", "AGRN", "WT1", "BCL2L1", "Ang2", "Ghr", "Myc",
        "Akt1", "Casp3", "VEGFA", "FAS", "CASP9", "FN1", "TPM1", "FGFR2", "PKM",
    ],
}

# Maturity overrides derived from explicit in-body / frontmatter status signals.
MATURITY = {
    "ANTI_CRISPR": "COMPLETE",
    "ENZYME_SPECIFICITY": "COMPLETE",
    "IBA_REVIEW": "COMPLETE",
    "METABOLIC_MODEL_ANALYSIS": "COMPLETE",
    "P_PUTIDA": "COMPLETE",
    "YEAST_REPLICATIVE_AGING": "COMPLETE",
    "SURVEILLANCE_IMMUNITY_ANNOTATION_EDITS": "COMPLETE",
    "SURVEILLANCE_IMMUNITY_CURATION_FINDINGS": "COMPLETE",
    "SURVEILLANCE_IMMUNITY_CURATION_RECOMMENDATIONS": "COMPLETE",
    "SURVEILLANCE_IMMUNITY_GENES_REVIEW": "COMPLETE",
    "SURVEILLANCE_IMMUNITY_GENE_REVIEW_SUMMARY": "COMPLETE",
    "BGC": "SCOPING",
    "PROTEOSTASIS": "SCOPING",
    "CEPHALOPOD": "IN_PROGRESS",
}

SPECIES_PREFIX = {
    "CAEEL_": ["worm"],
    "YEAST_": ["yeast"],
    "SURVEILLANCE_IMMUNITY_": ["worm"],
}


def maturity_for(slug: str, body: str, has_dir: bool) -> str:
    """Return an initial maturity estimate (curators can refine)."""
    if slug in MATURITY:
        return MATURITY[slug]
    words = len(body.split())
    if has_dir or words >= 2500:
        return "MATURE"
    if words >= 800:
        return "IN_PROGRESS"
    return "SCOPING"


def species_for(slug: str) -> list[str] | None:
    if slug in SPECIES:
        return SPECIES[slug]
    for prefix, value in SPECIES_PREFIX.items():
        if slug.startswith(prefix):
            return value
    return None


def tags_for(slug: str) -> list[str]:
    tags: list[str] = []
    if "OBSOLETION" in slug:
        tags.append("OBSOLETION")
    elif slug in PIPELINE:
        tags.append("PIPELINE")
    else:
        tags.append("BIOLOGY_DOMAIN")
    if slug in FLAGSHIP:
        tags.append("FLAGSHIP")
    return tags


def flow(values: list[str]) -> str:
    return "[" + ", ".join(values) + "]"


def split_frontmatter(text: str) -> tuple[list[str], str]:
    """Return (frontmatter_lines, rest_including_closing_and_body)."""
    lines = text.split("\n")
    end = None
    for i, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            end = i
            break
    assert end is not None, "expected closing frontmatter delimiter"
    return lines[1:end], "\n".join(lines[end:])


def top_level_keys(block: list[str]) -> set[str]:
    keys = set()
    for line in block:
        m = re.match(r"^([A-Za-z_][\w-]*):", line)
        if m:
            keys.add(m.group(1))
    return keys


def enrich(path: Path, dry: bool) -> str:
    slug = path.stem
    text = path.read_text()
    fm, body = parse_frontmatter(text)
    assert text.startswith("---"), f"{slug}: no frontmatter"

    block, rest = split_frontmatter(text)
    existing = top_level_keys(block)
    has_dir = (PROJECTS / slug).is_dir()

    maturity = maturity_for(slug, body, has_dir)
    tags = tags_for(slug)
    species = species_for(slug)
    genes = GENES.get(slug)

    # Drop any old top-level `status:` line; it is replaced by `maturity`.
    new_block: list[str] = []
    title_idx = None
    for line in block:
        if re.match(r"^status:", line):
            continue
        new_block.append(line)
        if title_idx is None and re.match(r"^title:", line):
            title_idx = len(new_block) - 1

    if title_idx is None:
        title_idx = -1  # insert at top if no title (shouldn't happen)

    inserts: list[str] = []
    if "maturity" not in existing:
        inserts.append(f"maturity: {maturity}")
    if "tags" not in existing:
        inserts.append(f"tags: {flow(tags)}")
    if species and "species" not in existing:
        inserts.append(f"species: {flow(species)}")
    if genes and "genes" not in existing:
        inserts.append(f"genes: {flow(genes)}")

    summary = (
        f"{slug:50s} mat={maturity:11s} tags={','.join(tags):30s} "
        f"species={flow(species) if species else '-':16s} "
        f"genes={'+'+str(len(genes)) if genes else '-'}"
    )

    if not inserts:
        return summary + "  (no change)"

    for off, line in enumerate(inserts, start=1):
        new_block.insert(title_idx + off, line)

    new_text = "---\n" + "\n".join(new_block) + "\n" + rest
    if not dry:
        path.write_text(new_text)
    return summary


def main() -> None:
    dry = "--dry" in sys.argv
    paths = sorted(p for p in PROJECTS.glob("*.md") if p.name != "README.md")
    for p in paths:
        print(enrich(p, dry))
    print(f"\n{'DRY RUN; ' if dry else ''}{len(paths)} projects processed")


if __name__ == "__main__":
    main()
