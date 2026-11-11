"""Select a prospective panel from cached GOA, without inspecting model output.

Include every available review with a positive canonical FRR:0004-scope or exact
lipid-droplet GOA row, minus a supplied previous manifest. Explicit controls are
also included. Record the evaluated GO closure to make selection auditable.
"""
import argparse
import csv
import hashlib
import json
from pathlib import Path

from ai_gene_review.tools.function_requirements import load_rules, parse_uniprot_flatfile, term_closures


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--repo", required=True, type=Path)
    p.add_argument("--organism", required=True)
    p.add_argument("--exclude-manifest", required=True, type=Path)
    p.add_argument("--controls", nargs="*", default=[])
    p.add_argument("--output", required=True, type=Path)
    args = p.parse_args()
    excluded = {r["gene"] for r in csv.DictReader(args.exclude_manifest.open(), delimiter="\t")}
    rules_path = args.repo / "rules/function_requirements/function-requirement-rules.yaml"
    rule = next(r for r in load_rules(rules_path) if r["id"] == "FRR:0004")
    closure = term_closures([rule])[rule["id"]]
    targets, scanned, unavailable = [], 0, []
    for folder in sorted((args.repo / "genes" / args.organism).iterdir()):
        if not folder.is_dir():
            continue
        gene = folder.name
        if gene in excluded:
            continue
        paths = [folder / f"{gene}{suffix}" for suffix in ("-ai-review.yaml", "-goa.tsv", "-uniprot.txt")]
        if not all(path.exists() for path in paths):
            if paths[0].exists():
                unavailable.append(gene)
            continue
        scanned += 1
        features = parse_uniprot_flatfile(paths[2].read_text())
        rows = [r for r in csv.DictReader(paths[1].open(), delimiter="\t")
                if r["GENE PRODUCT ID"] == features.accession]
        cohorts = []
        if any(r["GO TERM"] in closure and r["QUALIFIER"] in rule["qualifiers"] for r in rows):
            cohorts.append("FRR0004")
        if any(r["GO TERM"] == "GO:0005811" and not r["QUALIFIER"].startswith("NOT") for r in rows):
            cohorts.append("lipid_droplet")
        if gene in args.controls:
            cohorts.append("control")
        if cohorts:
            targets.append(dict(gene=gene, cohort=";".join(cohorts)))
    missing_controls = set(args.controls) - {r["gene"] for r in targets}
    if missing_controls:
        raise ValueError(f"Unavailable or previously tested controls: {missing_controls}")
    args.output.mkdir(parents=True, exist_ok=True)
    with (args.output / "targets.tsv").open("w") as stream:
        writer = csv.DictWriter(stream, fieldnames=["gene", "cohort"], delimiter="\t")
        writer.writeheader()
        writer.writerows(targets)
    metadata = dict(selection="All positive canonical FRR:0004-scope or exact lipid-droplet GOA claims, plus explicit controls; previous panel excluded.",
                    reviews_scanned=scanned, unavailable_reviews=unavailable, proteins_selected=len(targets),
                    excluded_genes=sorted(excluded), controls=args.controls,
                    rules_sha256=hashlib.sha256(rules_path.read_bytes()).hexdigest(),
                    frr0004_terms=sorted(closure))
    (args.output / "selection.json").write_text(json.dumps(metadata, indent=2) + "\n")
    print(f"Selected {len(targets)} proteins from {scanned} eligible reviews; {len(unavailable)} reviews lack required source files.")


if __name__ == "__main__":
    main()
