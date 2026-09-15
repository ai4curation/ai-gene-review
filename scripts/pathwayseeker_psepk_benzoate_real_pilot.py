#!/usr/bin/env python3
"""Generate a real-data PathwaySeeker pilot for P. putida KT2440."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
from pathlib import Path
from typing import Any

import pandas as pd
import yaml


COMMON_COMPOUNDS = {
    "C00001",  # H2O
    "C00002",  # ATP
    "C00003",  # NAD+
    "C00004",  # NADH
    "C00005",  # NADPH
    "C00006",  # NADP+
    "C00007",  # Oxygen
    "C00008",  # ADP
    "C00009",  # Orthophosphate
    "C00010",  # CoA
    "C00011",  # CO2
    "C00080",  # H+
    "C00390",  # Ubiquinol
    "C00399",  # Ubiquinone
    "C15602",  # Quinone
    "C15603",  # Hydroquinone
}

COMPOUND_LABELS = {
    "C00022": "Pyruvate",
    "C00024": "Acetyl-CoA",
    "C00025": "L-Glutamate",
    "C00026": "2-Oxoglutarate",
    "C00031": "D-Glucose",
    "C00036": "Oxaloacetate",
    "C00042": "Succinate",
    "C00049": "L-Aspartate",
    "C00074": "Phosphoenolpyruvate",
    "C00085": "D-Fructose 6-phosphate",
    "C00090": "Catechol",
    "C00092": "D-Glucose 6-phosphate",
    "C00111": "Glycerone phosphate",
    "C00118": "D-Glyceraldehyde 3-phosphate",
    "C00122": "Fumarate",
    "C00149": "(S)-Malate",
    "C00158": "Citrate",
    "C00180": "Benzoate",
    "C00198": "D-Glucono-1,5-lactone",
    "C00257": "D-Gluconate",
    "C00345": "6-Phospho-D-gluconate",
    "C00417": "cis-Aconitate",
    "C00846": "3-Oxoadipate",
    "C01236": "D-Glucono-1,5-lactone 6-phosphate",
    "C02480": "cis,cis-Muconate",
    "C03586": "2-Oxo-2,3-dihydrofuran-5-acetate",
    "C04442": "2-Dehydro-3-deoxy-6-phospho-D-gluconate",
    "C06321": "(1R,6S)-1,6-Dihydroxycyclohexa-2,4-diene-1-carboxylate",
    "C14610": "(S)-5-Oxo-2,5-dihydrofuran-2-acetate",
}


def load_yaml(path: Path) -> dict[str, Any]:
    with path.open() as handle:
        data = yaml.safe_load(handle)
    if not isinstance(data, dict):
        raise ValueError(f"Expected YAML mapping in {path}")
    return data


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def text_cell(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, float) and math.isnan(value):
        return ""
    return str(value).replace("\n", " ").replace("|", "\\|")


def fmt_num(value: Any) -> str:
    if value is None or pd.isna(value):
        return ""
    number = float(value)
    if number == 0:
        return "0"
    if abs(number) >= 100000:
        return f"{number:.3g}"
    if abs(number) >= 100:
        return f"{number:.0f}"
    return f"{number:.2f}"


def parse_equation_side(side: str) -> list[str]:
    return re.findall(r"C\d{5}", side)


def split_equation(equation: str) -> tuple[list[str], list[str]]:
    if "<=>" in equation:
        lhs, rhs = equation.split("<=>", 1)
    elif "=>" in equation:
        lhs, rhs = equation.split("=>", 1)
    elif "<=" in equation:
        rhs, lhs = equation.split("<=", 1)
    else:
        return [], []
    return parse_equation_side(lhs), parse_equation_side(rhs)


def parse_kegg_records(source_dir: Path) -> dict[str, dict[str, Any]]:
    records: dict[str, dict[str, Any]] = {}
    for path in sorted(source_dir.glob("*.txt")):
        text = path.read_text(errors="replace")
        for block in text.split("///"):
            entry_match = re.search(r"^ENTRY\s+(R\d+)\s+Reaction", block, re.M)
            if not entry_match:
                continue
            reaction_id = entry_match.group(1)
            record = {
                "id": reaction_id,
                "name": "",
                "definition": "",
                "equation": "",
                "enzyme": "",
                "source_file": str(path),
            }
            for field, key in [
                ("NAME", "name"),
                ("DEFINITION", "definition"),
                ("EQUATION", "equation"),
                ("ENZYME", "enzyme"),
            ]:
                match = re.search(rf"^{field}\s+(.+)$", block, re.M)
                if match:
                    record[key] = match.group(1).strip()
            lhs, rhs = split_equation(record["equation"])
            record["substrates"] = lhs
            record["products"] = rhs
            records[reaction_id] = record
    return records


def verified_lookup(mapping: dict[str, Any], project_dir: Path) -> bool:
    lookup_file = project_dir / mapping["kegg_lookup_file"]
    if not lookup_file.exists():
        return False
    target = mapping["kegg_id"]
    text = lookup_file.read_text(errors="replace")
    return bool(re.search(rf"^{re.escape(target)}\t", text, re.M))


def load_metabolomics(manifest: dict[str, Any], project_dir: Path) -> pd.DataFrame:
    maf = pd.read_csv(project_dir / "source_data/MTBLS1715_maf.tsv", sep="\t")
    mappings = {
        item["metabolite_identification"]: item
        for item in manifest["measured_metabolite_mappings"]
    }
    missing = sorted(set(maf["metabolite_identification"]) - set(mappings))
    if missing:
        raise ValueError(f"Missing KEGG mappings for MAF metabolites: {missing}")

    kegg_ids: list[str] = []
    lookup_statuses: list[str] = []
    lookup_files: list[str] = []
    for _, row in maf.iterrows():
        mapping = mappings[row["metabolite_identification"]]
        kegg_ids.append(mapping["kegg_id"])
        lookup_files.append(mapping["kegg_lookup_file"])
        lookup_statuses.append(
            "verified_in_cached_kegg_find"
            if verified_lookup(mapping, project_dir)
            else "mapping_not_verified_in_cache"
        )
    maf["KEGG_C_number"] = kegg_ids
    maf["kegg_lookup_status"] = lookup_statuses
    maf["kegg_lookup_file"] = lookup_files
    return maf


def sample_groups(project_dir: Path) -> dict[str, list[str]]:
    samples = pd.read_csv(project_dir / "source_data/MTBLS1715_samples.tsv", sep="\t")
    groups: dict[str, list[str]] = {}
    for _, row in samples.iterrows():
        sample = str(row.get("Sample Name", ""))
        match = re.match(r"^(Fe(?:Int|Lim)_T\d)_B\d+$", sample)
        if not match:
            continue
        source = str(row.get("Factor Value[13C source]", ""))
        variant = str(row.get("Characteristics[Variant]", ""))
        if "glucose with unlabeled benzoate" not in source:
            continue
        if "KT2440" not in variant:
            continue
        groups.setdefault(match.group(1), []).append(sample)
    return {key: sorted(value) for key, value in sorted(groups.items())}


def summarize_metabolites(maf: pd.DataFrame, groups: dict[str, list[str]]) -> pd.DataFrame:
    rows: list[dict[str, Any]] = []
    for _, row in maf.iterrows():
        out: dict[str, Any] = {
            "metabolite_identification": row["metabolite_identification"],
            "database_identifier": row["database_identifier"],
            "chemical_formula": row["chemical_formula"],
            "KEGG_C_number": row["KEGG_C_number"],
            "kegg_lookup_status": row["kegg_lookup_status"],
        }
        for condition, columns in groups.items():
            values = pd.to_numeric(row[columns], errors="coerce")
            out[f"{condition}_n"] = int(values.notna().sum())
            out[f"{condition}_mean"] = float(values.mean()) if values.notna().any() else None
            out[f"{condition}_sd"] = float(values.std()) if values.notna().sum() > 1 else None
        if out.get("FeInt_T1_mean") and out.get("FeLim_T1_mean"):
            out["FeLim_T1_vs_FeInt_T1_log2"] = math.log2(
                out["FeLim_T1_mean"] / out["FeInt_T1_mean"]
            )
        else:
            out["FeLim_T1_vs_FeInt_T1_log2"] = None
        rows.append(out)
    return pd.DataFrame(rows)


def load_gene_reviews(manifest: dict[str, Any], repo_root: Path) -> dict[str, dict[str, Any]]:
    reviews: dict[str, dict[str, Any]] = {}
    for relative in manifest["anchor_gene_reviews"]:
        path = repo_root / relative
        data = load_yaml(path)
        symbol = str(data.get("gene_symbol", path.parent.name))
        reviews[symbol] = {
            "gene_symbol": symbol,
            "uniprot_id": data.get("id", ""),
            "status": data.get("status", ""),
            "path": str(relative),
            "description": text_cell(data.get("description", "")),
            "core_terms": core_term_summary(data.get("core_functions", [])),
        }
        reviews[path.parent.name] = reviews[symbol]
    return reviews


def core_term_summary(core_functions: Any) -> str:
    labels: list[str] = []
    if not isinstance(core_functions, list):
        return ""
    for core in core_functions:
        if not isinstance(core, dict):
            continue
        for key in [
            "molecular_function",
            "contributes_to_molecular_function",
            "directly_involved_in",
            "locations",
        ]:
            value = core.get(key)
            if isinstance(value, dict) and value.get("label"):
                labels.append(str(value["label"]))
            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, dict) and item.get("label"):
                        labels.append(str(item["label"]))
    return "; ".join(dict.fromkeys(labels))


def reaction_status(
    reaction: dict[str, Any],
    measured: set[str],
    sample_context: set[str],
) -> tuple[str, str]:
    participants = [
        compound
        for compound in reaction.get("substrates", []) + reaction.get("products", [])
        if compound not in COMMON_COMPOUNDS
    ]
    unique = set(participants)
    measured_hits = sorted(unique & measured)
    sample_hits = sorted((unique - measured) & sample_context)
    if unique and unique <= measured:
        status = "measured_complete"
    elif measured_hits:
        status = "measured_partial"
    elif sample_hits:
        status = "sample_context_only"
    else:
        status = "kegg_topology_only"
    detail = "; ".join(
        [
            f"measured={','.join(measured_hits) if measured_hits else '-'}",
            f"sample_context={','.join(sample_hits) if sample_hits else '-'}",
            f"unmeasured={','.join(sorted(unique - measured - sample_context)) or '-'}",
        ]
    )
    return status, detail


def reaction_rows(
    reactions: list[dict[str, Any]],
    kegg_records: dict[str, dict[str, Any]],
    measured: set[str],
    sample_context: set[str],
) -> pd.DataFrame:
    rows: list[dict[str, Any]] = []
    for manifest_reaction in reactions:
        reaction_id = manifest_reaction["id"]
        record = kegg_records.get(reaction_id)
        if not record:
            raise ValueError(f"Missing cached KEGG reaction record for {reaction_id}")
        status, detail = reaction_status(record, measured, sample_context)
        rows.append(
            {
                "Reaction": reaction_id,
                "label": manifest_reaction["label"],
                "kegg_name": record["name"],
                "definition": record["definition"],
                "equation": record["equation"],
                "enzyme": record["enzyme"],
                "aigr_genes": ", ".join(manifest_reaction.get("aigr_genes", [])),
                "coverage_status": status,
                "coverage_detail": detail,
                "source_file": manifest_reaction.get("source_file", ""),
            }
        )
    return pd.DataFrame(rows)


def matched_rows(
    reaction_table: pd.DataFrame,
    kegg_records: dict[str, dict[str, Any]],
    measured: set[str],
    sample_context: set[str],
) -> pd.DataFrame:
    rows: list[dict[str, Any]] = []
    for _, reaction in reaction_table.iterrows():
        record = kegg_records[reaction["Reaction"]]
        for role, compounds in [("substrate", record["substrates"]), ("product", record["products"])]:
            for compound in compounds:
                if compound in COMMON_COMPOUNDS:
                    continue
                if compound in measured:
                    origin = "metabolomics"
                elif compound in sample_context:
                    origin = "sample_metadata"
                else:
                    origin = "kegg_topology"
                rows.append(
                    {
                        "Reaction": reaction["Reaction"],
                        "Compound": compound,
                        "CompoundLabel": COMPOUND_LABELS.get(compound, compound),
                        "Role": role,
                        "Origin": origin,
                        "coverage_status": reaction["coverage_status"],
                        "equation": reaction["equation"],
                    }
                )
    return pd.DataFrame(rows).drop_duplicates().sort_values(
        ["Reaction", "Role", "Compound"]
    )


def build_graph(
    reaction_table: pd.DataFrame,
    matched: pd.DataFrame,
    metabolite_summary: pd.DataFrame,
    gene_reviews: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    metabolite_by_id = metabolite_summary.set_index("KEGG_C_number").to_dict(orient="index")
    nodes: list[dict[str, Any]] = []
    edges: list[dict[str, Any]] = []

    compound_ids = sorted(set(matched["Compound"]))
    for compound_id in compound_ids:
        origin_values = sorted(set(matched.loc[matched["Compound"] == compound_id, "Origin"]))
        row = metabolite_by_id.get(compound_id, {})
        node = {
            "id": compound_id,
            "label": COMPOUND_LABELS.get(compound_id, row.get("metabolite_identification", compound_id)),
            "kind": "compound",
            "origins": origin_values,
            "measured": "metabolomics" in origin_values,
            "sample_context": "sample_metadata" in origin_values,
        }
        if row:
            node["metabolite_identification"] = row.get("metabolite_identification", "")
            node["FeInt_T1_mean"] = row.get("FeInt_T1_mean")
            node["FeLim_T1_mean"] = row.get("FeLim_T1_mean")
            node["FeLim_T1_vs_FeInt_T1_log2"] = row.get("FeLim_T1_vs_FeInt_T1_log2")
        nodes.append(node)

    for _, row in reaction_table.iterrows():
        reaction_id = row["Reaction"]
        nodes.append(
            {
                "id": reaction_id,
                "label": row["label"],
                "kind": "reaction",
                "coverage_status": row["coverage_status"],
                "equation": row["equation"],
                "enzyme": row["enzyme"],
            }
        )
        for gene_symbol in [item.strip() for item in str(row["aigr_genes"]).split(",") if item.strip()]:
            review = gene_reviews.get(gene_symbol)
            gene_id = f"gene:{gene_symbol}"
            if review:
                nodes.append(
                    {
                        "id": gene_id,
                        "label": gene_symbol,
                        "kind": "gene_review",
                        "uniprot_id": review["uniprot_id"],
                        "review_status": review["status"],
                        "review_path": review["path"],
                    }
                )
            edges.append(
                {
                    "source": gene_id,
                    "target": reaction_id,
                    "label": "reviewed_gene_context",
                    "origin": "aigr_review",
                }
            )

    for _, row in matched.iterrows():
        if row["Role"] == "substrate":
            source = row["Compound"]
            target = row["Reaction"]
        else:
            source = row["Reaction"]
            target = row["Compound"]
        edges.append(
            {
                "source": source,
                "target": target,
                "label": row["Role"],
                "origin": row["Origin"],
            }
        )

    deduped_nodes = {node["id"]: node for node in nodes}
    deduped_edges = {
        (edge["source"], edge["target"], edge["label"], edge["origin"]): edge
        for edge in edges
    }
    return {
        "nodes": [deduped_nodes[key] for key in sorted(deduped_nodes)],
        "edges": [deduped_edges[key] for key in sorted(deduped_edges)],
        "evidence_model": {
            "metabolomics": "Measured MTBLS1715 processed MAF abundance row",
            "sample_metadata": "Substrate named in MTBLS1715 sample factor value",
            "aigr_review": "Existing AI Gene Review gene-function anchor",
            "kegg_topology": "Unmeasured KEGG connector needed to state the reaction equation",
        },
    }


def write_source_metadata(project_dir: Path, manifest: dict[str, Any], output_path: Path) -> None:
    source_files = [
        "source_data/MTBLS1715_maf.tsv",
        "source_data/MTBLS1715_samples.tsv",
        "source_data/MTBLS1715_assay.tsv",
        "source_data/MTBLS1715_study.json",
        "source_data/PXD013605_project.json",
        "source_data/kegg_compound_reaction_links.tsv",
    ]
    source_files.extend(
        str(path.relative_to(project_dir))
        for path in sorted((project_dir / "source_data/kegg_find").glob("*.txt"))
    )
    source_files.extend(
        str(path.relative_to(project_dir))
        for path in sorted((project_dir / "source_data/kegg_reactions").glob("*.txt"))
    )
    metadata = {
        "title": manifest["title"],
        "generated_from": "scripts/pathwayseeker_psepk_benzoate_real_pilot.py",
        "source_data": manifest["source_data"],
        "files": {
            relative: {
                "path": relative,
                "sha256": sha256(project_dir / relative),
            }
            for relative in source_files
            if (project_dir / relative).exists()
        },
    }
    output_path.write_text(json.dumps(metadata, indent=2) + "\n")


def markdown_table(df: pd.DataFrame, columns: list[str], headers: list[str] | None = None) -> list[str]:
    if headers is None:
        headers = columns
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in columns) + " |",
    ]
    for _, row in df.iterrows():
        lines.append("| " + " | ".join(text_cell(row.get(column, "")) for column in columns) + " |")
    return lines


def report_markdown(
    manifest: dict[str, Any],
    metabolite_summary: pd.DataFrame,
    central_reactions: pd.DataFrame,
    aromatic_reactions: pd.DataFrame,
    matched: pd.DataFrame,
    gene_reviews: dict[str, dict[str, Any]],
    graph: dict[str, Any],
) -> str:
    measured_compounds = set(metabolite_summary["KEGG_C_number"])
    aromatic_compounds = {
        "C00180",
        "C06321",
        "C00090",
        "C02480",
        "C14610",
        "C03586",
        "C00846",
    }
    measured_aromatic = sorted(measured_compounds & aromatic_compounds)
    sample_context = ", ".join(
        f"{item['label']} (`{item['id']}`)" for item in manifest["sample_context_compounds"]
    )

    lines = [
        "---",
        "species:",
        f"  - {manifest['organism']}",
        f"title: {manifest['title']}",
        "---",
        "",
        f"# {manifest['title']}",
        "",
        "## What this pilot is",
        "",
        manifest["scope"],
        "",
        "This is a real-data pilot. The experimental evidence in this report is limited to:",
        "",
        "- processed MTBLS1715 metabolomics abundance rows for KT2440 samples;",
        "- MTBLS1715 sample metadata showing the carbon source context;",
        "- existing AIGR gene-review files for gene-function anchors.",
        "",
        "KEGG reaction records are used only as reaction topology and identifiers. They do not count as experimental omics evidence.",
        "",
        "## Source Data",
        "",
        f"- MetaboLights `{manifest['source_data']['metabolights_accession']}`: {manifest['source_data']['metabolights_url']}",
        f"- PRIDE `{manifest['source_data']['pride_accession']}`: {manifest['source_data']['pride_url']}",
        f"- Publication `{manifest['source_data']['publication']['id']}` / DOI `{manifest['source_data']['publication']['doi']}`: {manifest['source_data']['publication']['title']}",
        f"- Sample carbon-source context: {sample_context}.",
        "",
        "The MAF contains 14 measured metabolites across 16 KT2440 glucose-plus-benzoate sample columns. No processed MAF row maps to benzoate, catechol, cis,cis-muconate, muconolactone, or 3-oxoadipate.",
        "",
        "The cached PRIDE project metadata documents the matched proteomics accession, but this pilot does not parse raw PRIDE spectra or treat the PRIDE record as a protein-abundance matrix.",
        "",
        "## Measured Metabolites",
        "",
    ]
    summary_for_md = metabolite_summary.copy()
    for column in [
        "FeInt_T1_mean",
        "FeLim_T1_mean",
        "FeLim_T2_mean",
        "FeLim_T3_mean",
        "FeLim_T1_vs_FeInt_T1_log2",
    ]:
        summary_for_md[column] = summary_for_md[column].map(fmt_num)
    lines.extend(
        markdown_table(
            summary_for_md,
            [
                "metabolite_identification",
                "database_identifier",
                "KEGG_C_number",
                "FeInt_T1_mean",
                "FeLim_T1_mean",
                "FeLim_T2_mean",
                "FeLim_T3_mean",
                "FeLim_T1_vs_FeInt_T1_log2",
                "kegg_lookup_status",
            ],
            [
                "Metabolite",
                "Source ID",
                "KEGG",
                "FeInt T1 mean",
                "FeLim T1 mean",
                "FeLim T2 mean",
                "FeLim T3 mean",
                "log2 FeLim T1 / FeInt T1",
                "Mapping",
            ],
        )
    )
    lines.extend(
        [
            "",
            "## Central-Carbon Reaction Coverage",
            "",
            "Coverage status is computed from non-common reaction participants after removing water, ATP/ADP, redox cofactors, oxygen, phosphate, CO2, CoA, quinone/ubiquinone, and protons.",
            "",
        ]
    )
    central_for_md = central_reactions.copy()
    central_for_md["equation"] = central_for_md["equation"].map(lambda value: f"`{value}`")
    lines.extend(
        markdown_table(
            central_for_md,
            ["Reaction", "label", "aigr_genes", "coverage_status", "coverage_detail", "equation"],
            ["Reaction", "Step", "AIGR genes", "Coverage", "Detail", "Equation"],
        )
    )
    lines.extend(
        [
            "",
            "## Aromatic Branch Coverage Check",
            "",
        ]
    )
    if measured_aromatic:
        lines.append("Measured aromatic-branch compounds: " + ", ".join(measured_aromatic) + ".")
    else:
        lines.append(
            "No aromatic-ring-cleavage intermediates are present as measured compounds in the processed MAF. Benzoate is present only as a sample carbon-source context."
        )
    lines.append("")
    aromatic_for_md = aromatic_reactions.copy()
    aromatic_for_md["equation"] = aromatic_for_md["equation"].map(lambda value: f"`{value}`")
    lines.extend(
        markdown_table(
            aromatic_for_md,
            ["Reaction", "label", "aigr_genes", "coverage_status", "coverage_detail", "equation"],
            ["Reaction", "Step", "AIGR genes", "Coverage", "Detail", "Equation"],
        )
    )
    lines.extend(
        [
            "",
            "## AIGR Gene Anchors",
            "",
        ]
    )
    gene_rows = []
    seen: set[str] = set()
    for relative in manifest["anchor_gene_reviews"]:
        path = Path(relative)
        review = gene_reviews.get(path.parent.name)
        if not review or review["gene_symbol"] in seen:
            continue
        seen.add(review["gene_symbol"])
        gene_rows.append(review)
    lines.extend(
        markdown_table(
            pd.DataFrame(gene_rows),
            ["gene_symbol", "uniprot_id", "status", "core_terms", "path"],
            ["Gene", "UniProt", "Review status", "Core reviewed terms", "Review file"],
        )
    )
    lines.extend(
        [
            "",
            "## Generated PathwaySeeker Artifacts",
            "",
            "- `metabolomics_with_C_numbers.csv`: MAF-derived metabolite table with KEGG C numbers and cached lookup provenance.",
            "- `metabolite_condition_summary.csv`: condition-level abundance summary for the 16 KT2440 glucose-plus-benzoate samples.",
            "- `reaction_to_compounds_from_metabolomics.csv`: PathwaySeeker-compatible reaction/compound/role rows for the selected pathway reactions; the origin column separates measured metabolites from sample context and unmeasured topology.",
            "- `matched_metabolites_reactions_all.csv`: final merged reaction/compound table for this pilot; origins distinguish metabolomics, sample metadata, and KEGG topology.",
            "- `pathwayseeker_matched_reactions.csv`: AIGR-facing copy of the matched reaction table.",
            "- `pathwayseeker_reaction_coverage.csv`: central-carbon plus aromatic-branch coverage table.",
            "- `pathwayseeker_graph_subset.json`: graph JSON with compound, reaction, and reviewed-gene nodes; AIGR anchors appear here as `aigr_review` edges.",
            "- `source_metadata.json`: source-file checksums.",
            "",
            f"The graph subset has {len(graph['nodes'])} nodes and {len(graph['edges'])} edges.",
            "",
            "## Integration Decision",
            "",
            "This is suitable for an AIGR pilot as pathway-context evidence, not as direct evidence to create or accept enzymatic GO annotations.",
            "",
            "Specific implications:",
            "",
            "- The real metabolomics supports central-carbon coverage around gluconate, glucose-6-phosphate, 6-phosphogluconate, pyruvate/PEP, and TCA nodes during glucose-plus-benzoate growth.",
            "- The aromatic benzoate-to-catechol branch is not directly observed in the processed metabolomics table; its reviewed genes should stay supported by literature/review evidence, not by this MAF.",
            "- `gcd`, `zwf`, `edd`, and `eda` can be linked as reviewed anchors to the pathway graph, but the graph edge itself should be tagged as context unless both protein abundance and metabolite evidence are present.",
            "- A proteomics-enabled second pass needs a parsed KT2440 protein-abundance table from PXD013605 or supplementary data with stable locus/UniProt mapping.",
            "",
            "## Reproduce",
            "",
            "```bash",
            ".venv/bin/python scripts/pathwayseeker_psepk_benzoate_real_pilot.py projects/PATHWAYSEEKER/PSEPK_BENZOATE_REAL/manifest.yaml",
            ".venv/bin/ai-gene-review render-projects projects/PATHWAYSEEKER/PSEPK_BENZOATE_REAL/README.md -o projects/PATHWAYSEEKER/PSEPK_BENZOATE_REAL",
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("manifest", type=Path)
    args = parser.parse_args()

    repo_root = Path.cwd()
    manifest_path = args.manifest
    project_dir = manifest_path.parent
    manifest = load_yaml(manifest_path)
    artifact_dir = project_dir

    maf = load_metabolomics(manifest, project_dir)
    groups = sample_groups(project_dir)
    if set(groups) != {"FeInt_T1", "FeLim_T1", "FeLim_T2", "FeLim_T3"}:
        raise ValueError(f"Unexpected sample groups: {groups}")
    summary = summarize_metabolites(maf, groups)
    gene_reviews = load_gene_reviews(manifest, repo_root)
    kegg_records = parse_kegg_records(project_dir / "source_data/kegg_reactions")

    measured = set(summary["KEGG_C_number"])
    sample_context = {item["id"] for item in manifest["sample_context_compounds"]}
    central = reaction_rows(
        manifest["target_pathway"]["central_reactions"],
        kegg_records,
        measured,
        sample_context,
    )
    aromatic = reaction_rows(
        manifest["target_pathway"]["aromatic_coverage_reactions"],
        kegg_records,
        measured,
        sample_context,
    )
    all_reactions = pd.concat([central, aromatic], ignore_index=True)
    matched = matched_rows(all_reactions, kegg_records, measured, sample_context)
    graph = build_graph(all_reactions, matched, summary, gene_reviews)

    maf.to_csv(artifact_dir / "metabolomics_with_C_numbers.csv", index=False)
    summary.to_csv(artifact_dir / "metabolite_condition_summary.csv", index=False)
    matched.to_csv(artifact_dir / "reaction_to_compounds_from_metabolomics.csv", index=False)
    matched.to_csv(artifact_dir / "matched_metabolites_reactions_all.csv", index=False)
    matched.to_csv(artifact_dir / "pathwayseeker_matched_reactions.csv", index=False)
    all_reactions.to_csv(artifact_dir / "pathwayseeker_reaction_coverage.csv", index=False)
    (artifact_dir / "pathwayseeker_graph_subset.json").write_text(
        json.dumps(graph, indent=2) + "\n"
    )
    write_source_metadata(project_dir, manifest, artifact_dir / "source_metadata.json")
    (artifact_dir / "README.md").write_text(
        report_markdown(
            manifest,
            summary,
            central,
            aromatic,
            matched,
            gene_reviews,
            graph,
        )
    )


if __name__ == "__main__":
    main()
