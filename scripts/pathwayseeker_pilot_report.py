#!/usr/bin/env python3
"""Import a real PathwaySeeker output subset for a pathway pilot."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path
from typing import Any

import pandas as pd
import yaml


SOURCE_FILES = {
    "matched_reactions": "matched_metabolites_reactions_all.csv",
    "graph": "graph_notebook.json",
    "ko_to_reactions": "ko_to_reactions.csv",
    "proteomics": "proteomics_with_ko.csv",
}


def load_yaml(path: Path) -> dict[str, Any]:
    with path.open() as handle:
        data = yaml.safe_load(handle)
    if not isinstance(data, dict):
        raise ValueError(f"Expected mapping in {path}")
    return data


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def source_commit(source_root: Path | None) -> str:
    if not source_root:
        return ""
    try:
        return subprocess.check_output(
            ["git", "-C", str(source_root), "rev-parse", "HEAD"],
            text=True,
            stderr=subprocess.DEVNULL,
        ).strip()
    except Exception:
        return ""


def reaction_id_from_edge(edge: dict[str, Any]) -> str:
    label = str(edge.get("label", ""))
    match = re.match(r"(R\d+)\b", label)
    return match.group(1) if match else ""


def reaction_origins(rows: pd.DataFrame) -> str:
    origins = sorted(str(value) for value in rows["Origin"].dropna().unique())
    return ";".join(origins)


def add_protein_means(proteomics: pd.DataFrame) -> pd.DataFrame:
    groups = {
        "AgitWOAO": [col for col in proteomics.columns if col == "AgitWOAO" or col.startswith("AgitWOAO.")],
        "AgitWAO": [col for col in proteomics.columns if col == "AgitWAO" or col.startswith("AgitWAO.")],
        "StatWOAO": [col for col in proteomics.columns if col == "StatWOAO" or col.startswith("StatWOAO.")],
        "StatWAO": [col for col in proteomics.columns if col == "StatWAO" or col.startswith("StatWAO.")],
    }
    out = proteomics.copy()
    for group, cols in groups.items():
        if cols:
            out[f"{group}_mean"] = out[cols].mean(axis=1).round(3)
    return out


def build_coverage(
    matched: pd.DataFrame,
    expected_reactions: list[dict[str, str]],
    target_compounds: dict[str, str],
) -> pd.DataFrame:
    rows: list[dict[str, str | int]] = []
    for reaction in expected_reactions:
        reaction_rows = matched[matched["Reaction"] == reaction["id"]]
        rows.append(
            {
                "type": "expected_reaction",
                "id": reaction["id"],
                "label": reaction["label"],
                "status": "observed" if not reaction_rows.empty else "missing",
                "matched_rows": len(reaction_rows),
                "origin": reaction_origins(reaction_rows) if not reaction_rows.empty else "",
            }
        )
    for compound_id, label in target_compounds.items():
        compound_rows = matched[matched["Compound"] == compound_id]
        rows.append(
            {
                "type": "target_compound",
                "id": compound_id,
                "label": label,
                "status": "observed" if not compound_rows.empty else "missing",
                "matched_rows": len(compound_rows),
                "origin": reaction_origins(compound_rows) if not compound_rows.empty else "",
            }
        )
    return pd.DataFrame(rows)


def build_graph_subset(
    graph: dict[str, Any],
    observed_reactions: set[str],
    target_compounds: dict[str, str],
) -> dict[str, Any]:
    edges = [
        edge
        for edge in graph.get("edges", [])
        if reaction_id_from_edge(edge) in observed_reactions
        or edge.get("source") in target_compounds
        or edge.get("target") in target_compounds
    ]
    node_ids = {edge["source"] for edge in edges} | {edge["target"] for edge in edges}
    source_nodes = {
        node.get("id"): node
        for node in graph.get("nodes", [])
        if node.get("id") in node_ids
    }
    nodes = []
    for node_id in sorted(node_ids):
        node = dict(source_nodes.get(node_id, {"id": node_id}))
        if node_id in target_compounds:
            node["label"] = target_compounds[node_id]
            node["target_compound"] = True
        nodes.append(node)
    return {"nodes": nodes, "edges": edges}


def write_metadata(source_root: Path | None, artifact_dir: Path, source_output: Path) -> None:
    metadata = {
        "source": "pnnl/PathwaySeeker public example output",
        "source_repository": "https://github.com/pnnl/PathwaySeeker",
        "source_root": str(source_root) if source_root else "",
        "source_commit": source_commit(source_root),
        "source_output": str(source_output),
        "files": {
            name: {
                "path": str(source_output / filename),
                "sha256": sha256(source_output / filename),
            }
            for name, filename in SOURCE_FILES.items()
        },
    }
    (artifact_dir / "source_metadata.json").write_text(json.dumps(metadata, indent=2) + "\n")


def cell(value: Any) -> str:
    if pd.isna(value):
        return ""
    return str(value)


def markdown_report(
    manifest: dict[str, Any],
    coverage: pd.DataFrame,
    matched_subset: pd.DataFrame,
    protein_evidence: pd.DataFrame,
    graph_subset: dict[str, Any],
    artifact_dir: Path,
    source_metadata: dict[str, Any],
) -> str:
    expected = coverage[coverage["type"] == "expected_reaction"]
    compounds = coverage[coverage["type"] == "target_compound"]
    exact_hits = expected[expected["status"] == "observed"]
    neighborhood = sorted(matched_subset["Reaction"].dropna().unique())

    lines: list[str] = []
    lines.append("---")
    lines.append("species: []")
    lines.append(f"title: {manifest['title']}")
    lines.append("---")
    lines.append("")
    lines.append(f"# {manifest['title']}")
    lines.append("")
    lines.append("## Source")
    lines.append("")
    lines.append(
        "This pilot imports the public PathwaySeeker example output directly: "
        "`matched_metabolites_reactions_all.csv`, `graph_notebook.json`, "
        "`ko_to_reactions.csv`, and `proteomics_with_ko.csv`."
    )
    commit = source_metadata.get("source_commit", "")
    if commit:
        lines.append("")
        lines.append(f"Source repository commit used for this run: `{commit}`.")
    lines.append("")
    lines.append(manifest["scope"])
    lines.append("")
    lines.append("## Target Pathway")
    lines.append("")
    lines.append("| KEGG reaction | Expected step | PathwaySeeker status | Origin |")
    lines.append("|---|---|---|---|")
    for _, row in expected.iterrows():
        lines.append(
            f"| {row['id']} | {row['label']} | {row['status']} | {row['origin']} |"
        )
    lines.append("")
    lines.append("## Real PathwaySeeker Result")
    lines.append("")
    if exact_hits.empty:
        lines.append(
            "The real PathwaySeeker output does not recover the selected benzoate-to-catechol / "
            "catechol ortho-cleavage pathway reactions. That is the important result: the "
            "integration should record this as absent or partial evidence, not fill the pathway "
            "from KEGG."
        )
    else:
        lines.append(
            f"PathwaySeeker recovered {len(exact_hits)} expected reaction(s) from the target pathway."
        )
    lines.append("")
    lines.append("Observed target-compound coverage:")
    lines.append("")
    lines.append("| Compound | Label | Status | Matched rows | Origin |")
    lines.append("|---|---|---|---:|---|")
    for _, row in compounds.iterrows():
        lines.append(
            f"| {row['id']} | {row['label']} | {row['status']} | {row['matched_rows']} | {row['origin']} |"
        )
    lines.append("")
    lines.append(
        f"The benzoate/catechol neighborhood contains {len(neighborhood)} PathwaySeeker reaction(s): "
        + ", ".join(f"`{reaction}`" for reaction in neighborhood)
        + "."
    )
    lines.append("")
    lines.append("| Reaction | Compound | Role | Origin | Equation |")
    lines.append("|---|---|---|---|---|")
    for _, row in matched_subset.iterrows():
        lines.append(
            f"| {row['Reaction']} | {row['Compound']} | {row['Role']} | "
            f"{row['Origin']} | `{row['equation']}` |"
        )
    lines.append("")
    lines.append("## Protein Evidence")
    lines.append("")
    if protein_evidence.empty:
        lines.append("No KO-linked protein evidence was found for the observed neighborhood reactions.")
    else:
        lines.append("| Reaction | KO | Protein ID | Description | AgitWOAO mean | AgitWAO mean | StatWOAO mean | StatWAO mean |")
        lines.append("|---|---|---|---|---:|---:|---:|---:|")
        for _, row in protein_evidence.iterrows():
            lines.append(
                "| {reaction} | {ko} | `{protein}` | {description} | {agit_woao} | {agit_wao} | {stat_woao} | {stat_wao} |".format(
                    reaction=cell(row.get("Reaction", "")),
                    ko=cell(row.get("KO", "")),
                    protein=cell(row.get("proteinID", "")),
                    description=cell(row.get("description", "")),
                    agit_woao=cell(row.get("AgitWOAO_mean", "")),
                    agit_wao=cell(row.get("AgitWAO_mean", "")),
                    stat_woao=cell(row.get("StatWOAO_mean", "")),
                    stat_wao=cell(row.get("StatWAO_mean", "")),
                )
            )
    lines.append("")
    lines.append("## Graph Subset")
    lines.append("")
    lines.append(
        f"The extracted real PathwaySeeker graph subset has {len(graph_subset['nodes'])} nodes "
        f"and {len(graph_subset['edges'])} edges."
    )
    lines.append("")
    lines.append("## Integration Implications")
    lines.append("")
    for item in manifest["integration_implications"]:
        lines.append(f"- {item}")
    lines.append("")
    lines.append("## Generated Artifacts")
    lines.append("")
    for artifact in [
        "pathwayseeker_reaction_coverage.csv",
        "pathwayseeker_matched_reactions.csv",
        "pathwayseeker_protein_evidence.csv",
        "pathwayseeker_graph_subset.json",
        "source_metadata.json",
    ]:
        lines.append(f"- `{artifact}`")
    lines.append("")
    lines.append("## Reproduce")
    lines.append("")
    lines.append("```bash")
    lines.append("git clone https://github.com/pnnl/PathwaySeeker.git /tmp/PathwaySeeker")
    lines.append(f"git -C /tmp/PathwaySeeker checkout {source_metadata.get('source_commit', '<commit>')}")
    lines.append(
        "uv run python scripts/pathwayseeker_pilot_report.py "
        "projects/PATHWAYSEEKER/BENZOATE_PILOT/manifest.yaml "
        "--pathwayseeker-output /tmp/PathwaySeeker/output "
        "--pathwayseeker-root /tmp/PathwaySeeker "
        "--output projects/PATHWAYSEEKER/BENZOATE_PILOT/README.md "
        "--artifact-dir projects/PATHWAYSEEKER/BENZOATE_PILOT"
    )
    lines.append(
        "uv run ai-gene-review render-projects "
        "projects/PATHWAYSEEKER/BENZOATE_PILOT/README.md "
        "-o projects/PATHWAYSEEKER/BENZOATE_PILOT"
    )
    lines.append("```")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--pathwayseeker-output", type=Path, required=True)
    parser.add_argument("--pathwayseeker-root", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--artifact-dir", type=Path, required=True)
    args = parser.parse_args()

    manifest = load_yaml(args.manifest)
    args.artifact_dir.mkdir(parents=True, exist_ok=True)

    matched = pd.read_csv(args.pathwayseeker_output / SOURCE_FILES["matched_reactions"])
    graph = json.loads((args.pathwayseeker_output / SOURCE_FILES["graph"]).read_text())
    ko_to_reactions = pd.read_csv(args.pathwayseeker_output / SOURCE_FILES["ko_to_reactions"])
    proteomics = add_protein_means(
        pd.read_csv(args.pathwayseeker_output / SOURCE_FILES["proteomics"])
    )

    expected_reactions = manifest["target_pathway"]["expected_reactions"]
    expected_reaction_ids = {reaction["id"] for reaction in expected_reactions}
    target_compounds = {
        compound["id"]: compound["label"]
        for compound in manifest["target_pathway"]["target_compounds"]
    }

    coverage = build_coverage(matched, expected_reactions, target_compounds)
    compound_hits = matched[matched["Compound"].isin(target_compounds)]
    observed_reaction_ids = set(compound_hits["Reaction"].dropna()) | expected_reaction_ids
    matched_subset = matched[matched["Reaction"].isin(observed_reaction_ids)].sort_values(
        ["Reaction", "Role", "Compound"]
    )

    observed_reactions = set(matched_subset["Reaction"].dropna())
    graph_subset = build_graph_subset(graph, observed_reactions, target_compounds)

    kos = ko_to_reactions[ko_to_reactions["Reaction"].isin(observed_reactions)].copy()
    protein_rows = proteomics.merge(kos, on="KO", how="inner")
    keep_cols = [
        "Reaction",
        "KO",
        "proteinID",
        "description",
        "AgitWOAO_mean",
        "AgitWAO_mean",
        "StatWOAO_mean",
        "StatWAO_mean",
    ]
    protein_evidence = protein_rows[keep_cols].sort_values(["Reaction", "KO", "proteinID"])

    coverage.to_csv(args.artifact_dir / "pathwayseeker_reaction_coverage.csv", index=False)
    matched_subset.to_csv(args.artifact_dir / "pathwayseeker_matched_reactions.csv", index=False)
    protein_evidence.to_csv(args.artifact_dir / "pathwayseeker_protein_evidence.csv", index=False)
    (args.artifact_dir / "pathwayseeker_graph_subset.json").write_text(
        json.dumps(graph_subset, indent=2) + "\n"
    )
    write_metadata(args.pathwayseeker_root, args.artifact_dir, args.pathwayseeker_output)
    source_metadata = json.loads((args.artifact_dir / "source_metadata.json").read_text())

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        markdown_report(
            manifest,
            coverage,
            matched_subset,
            protein_evidence,
            graph_subset,
            args.artifact_dir,
            source_metadata,
        )
    )


if __name__ == "__main__":
    main()
