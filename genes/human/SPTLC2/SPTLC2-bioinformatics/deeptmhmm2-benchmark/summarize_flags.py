"""Summarize a completed topology flag panel, including proteins with no flags."""
import argparse
from collections import Counter
import csv
import hashlib
import json
from pathlib import Path

from ai_gene_review.tools.function_requirements import load_rules, evaluate, parse_uniprot_flatfile


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--repo", required=True, type=Path)
    p.add_argument("--manifest", required=True, type=Path)
    p.add_argument("--predictions", required=True, type=Path)
    p.add_argument("--flags", required=True, type=Path)
    p.add_argument("--selection", required=True, type=Path)
    p.add_argument("--cli", type=Path, help="Optional upstream CLI JSON for a diagnostic subset")
    p.add_argument("--output", required=True, type=Path)
    args = p.parse_args()
    manifest = list(csv.DictReader(args.manifest.open(), delimiter="\t"))
    flags = json.loads(args.flags.read_text())
    timing = json.loads((args.predictions / "timings.json").read_text())
    selection = json.loads(args.selection.read_text())
    rules_path = args.repo / "rules/function_requirements/function-requirement-rules.yaml"
    assert hashlib.sha256(rules_path.read_bytes()).hexdigest() == selection["rules_sha256"]
    rule = next(r for r in load_rules(rules_path) if r["id"] == "FRR:0004")
    closure = set(selection["frr0004_terms"])
    assert flags["proteins_evaluated"] == len(manifest)
    runs = {r["id"]: r for r in timing["runs"] if r["repeat"] == 1}
    assert set(runs) == {r["accession"] for r in manifest}
    summary, sources = [], {}
    for row in manifest:
        gene, acc = row["gene"], row["accession"]
        prediction_path = args.predictions / f"{acc}.r1.json"
        prediction = json.loads(prediction_path.read_text())[0]
        gene_flags = [f for f in flags["flags"] if f["accession"] == acc]
        run = runs[acc]
        assert run["sequence_sha256"] == row["sequence_sha256"]
        source = args.repo / row["source"]
        original = evaluate(rule, parse_uniprot_flatfile(source.read_text())).value
        goa = list(csv.DictReader((source.parent / f"{gene}-goa.tsv").open(), delimiter="\t"))
        scoped_rows = sum(r["GENE PRODUCT ID"] == acc and r["GO TERM"] in closure
                          and r["QUALIFIER"] in rule["qualifiers"] for r in goa)
        files = [source, source.parent / f"{gene}-goa.tsv", source.parent / f"{gene}-ai-review.yaml", prediction_path]
        sources[gene] = {str(path): hashlib.sha256(path.read_bytes()).hexdigest() for path in files}
        segments = prediction["segments"]
        summary.append(dict(gene=gene, accession=acc, cohort=row["cohort"], length=row["length"],
            uniprot_spans=len(row["transmem"].split(";")) if row["transmem"] else 0,
            predicted_spans=sum(s["name"] in {"TMhelix", "Beta sheet"} for s in segments),
            predicted_if_re=sum(s["name"] in {"interfacial", "reentrant"} for s in segments),
            predicted_type=prediction["type"], membrane_types=";".join(prediction["membrane_types"]),
            original_frr_verdict=original, in_scope_frr_rows=scoped_rows,
            features=";".join(f"{s['name']}({s['start']}-{s['end']})" for s in segments
                              if s["name"] in {"TMhelix", "Beta sheet", "interfacial", "reentrant", "signal", "transit_peptide"}),
            flag_count=len(gene_flags), rules=";".join(sorted({f["rule_id"] for f in gene_flags})),
            verdicts=";".join(sorted({f["verdict"] for f in gene_flags})),
            review_actions=";".join(sorted({a for f in gene_flags for a in f.get("review_actions", [])})),
            inference_seconds=round(run["inference_seconds"], 3)))
    args.output.mkdir(parents=True, exist_ok=True)
    with (args.output / "summary.tsv").open("w") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(summary[0]), delimiter="\t")
        writer.writeheader()
        writer.writerows(summary)
    stats = dict(proteins=len(summary), residues=sum(int(r["length"]) for r in summary),
                 length_range=[min(int(r["length"]) for r in summary), max(int(r["length"]) for r in summary)],
                 flagged_proteins=sum(r["flag_count"] > 0 for r in summary),
                 flags=len(flags["flags"]), flags_by_rule=dict(Counter(f["rule_id"] for f in flags["flags"])),
                 flags_by_verdict=dict(Counter(f["verdict"] for f in flags["flags"])),
                 original_frr_flagged_proteins=sum(r["in_scope_frr_rows"] > 0 and r["original_frr_verdict"] != "SATISFIED" for r in summary),
                 original_frr_flags_with_predicted_spans=[r["gene"] for r in summary if r["in_scope_frr_rows"] > 0 and r["original_frr_verdict"] != "SATISFIED" and r["predicted_spans"] > 0],
                 inference_seconds=sum(r["inference_seconds"] for r in timing["runs"]),
                 peak_rss_bytes=max(r["peak_rss_bytes"] for r in timing["runs"]),
                 imports_seconds=timing["imports_seconds"], model_load_seconds=timing["model_load_seconds"])
    (args.output / "summary.json").write_text(json.dumps(stats, indent=2) + "\n")
    (args.output / "source-hashes.json").write_text(json.dumps(sources, indent=2) + "\n")
    if args.cli:
        cli_predictions = [r for r in json.loads(args.cli.read_text()) if "id" in r]
        assert cli_predictions
        sequence_lines = (args.cli.parent / "predicted_topologies.3line").read_text().splitlines()
        assert len(sequence_lines) % 3 == 0
        cli_hashes = {sequence_lines[i][1:].split()[0]: hashlib.sha256(sequence_lines[i+1].encode()).hexdigest()
                      for i in range(0, len(sequence_lines), 3)}
        by_acc = {r["accession"]: r for r in manifest}
        comparisons = []
        for cli in cli_predictions:
            acc = cli["id"]
            assert cli_hashes[acc] == by_acc[acc]["sequence_sha256"]
            api = json.loads((args.predictions / f"{acc}.r1.json").read_text())[0]
            segments = [s if isinstance(s, dict) else dict(zip(("name", "start", "end"), s)) for s in cli["segments"]]
            comparisons.append(dict(gene=by_acc[acc]["gene"], accession=acc,
                type_match=api["type"] == cli["type"],
                membrane_labels_match=api["membrane_types"] == cli["membrane_types"],
                topology_match=api["topology_string"] == cli["topology_string"],
                segments_match=api["segments"] == segments))
        (args.output / "cli-comparison.json").write_text(json.dumps(comparisons, indent=2) + "\n")
    print(json.dumps(stats, indent=2))


if __name__ == "__main__":
    main()
