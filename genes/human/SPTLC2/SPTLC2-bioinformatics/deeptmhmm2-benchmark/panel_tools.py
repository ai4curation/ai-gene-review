"""Prepare a gene panel and compare measured API/CLI output with a supplied S20 table."""
import argparse
import csv
import hashlib
import json
import re
import statistics
from pathlib import Path


def read_tsv(path):
    with path.open() as stream:
        return list(csv.DictReader(stream, delimiter="\t"))


def write_tsv(path, rows):
    with path.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]), delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)


def prepare(args):
    from Bio import SeqIO
    targets = read_tsv(args.targets)
    assert len({t["gene"] for t in targets}) == len(targets), "Duplicate genes"
    args.output.mkdir(parents=True, exist_ok=True)
    records, manifest = [], []
    for target in targets:
        gene = target["gene"]
        source = args.repo / "genes" / args.organism / gene / f"{gene}-uniprot.txt"
        record = SeqIO.read(source, "swiss")
        assert record.annotations["ncbi_taxid"] == [args.taxon]
        sequence = str(record.seq)
        assert sequence and set(sequence) <= set("ACDEFGHIKLMNPQRSTVWY")
        features = {key: [] for key in ("TRANSMEM", "SIGNAL", "TRANSIT")}
        for feature in record.features:
            if feature.type in features:
                features[feature.type].append(f"{int(feature.location.start)+1}-{int(feature.location.end)}")
        manifest.append(dict(**target, accession=record.id, length=len(sequence),
                             sequence_sha256=hashlib.sha256(sequence.encode()).hexdigest(),
                             source=str(source.relative_to(args.repo)),
                             source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
                             **{key.lower(): ";".join(value) for key, value in features.items()}))
        record.description = gene
        records.append(record)
    assert len({r.id for r in records}) == len(records), "Duplicate accessions"
    SeqIO.write(records, args.output / "inputs.fasta", "fasta")
    write_tsv(args.output / "inputs.tsv", manifest)
    print(f"Prepared {len(records)} sequences; {sum(len(r.seq) for r in records)} residues")


def summarize(args):
    manifest = read_tsv(args.manifest)
    timings = json.loads((args.api / "timings.json").read_text())
    cli_records = json.loads(args.cli.read_text())
    cli = {p["id"]: p for p in cli_records if "id" in p}
    cli_metadata = [p["metadata"] for p in cli_records if "metadata" in p]
    # The CLI serializes region tuples; the API serializes dictionaries.
    for prediction in cli.values():
        prediction["segments"] = [
            segment if isinstance(segment, dict) else dict(zip(("name", "start", "end"), segment))
            for segment in prediction["segments"]
        ]
    three_line = (args.cli.parent / "predicted_topologies.3line").read_text().splitlines()
    assert len(three_line) % 3 == 0
    cli_sequences = {three_line[i][1:].split()[0]: three_line[i+1] for i in range(0, len(three_line), 3)}
    s20 = {r["accession"]: r for r in read_tsv(args.s20)}
    result = []
    agreement = []
    differences = []
    for entry in manifest:
        acc = entry["accession"]
        assert hashlib.sha256(cli_sequences[acc].encode()).hexdigest() == entry["sequence_sha256"]
        runs = [r for r in timings["runs"] if r["id"] == acc]
        assert runs and all(r["sequence_sha256"] == entry["sequence_sha256"] for r in runs)
        predictions = [json.loads((args.api / f"{acc}.r{r['repeat']}.json").read_text())[0] for r in runs]
        p = predictions[0]
        assert len(p["topology_string"]) == int(entry["length"])
        feature_segments = [(s["name"], s["start"], s["end"]) for s in p["segments"]
                            if s["name"] in {"interfacial", "reentrant", "transit_peptide", "signal", "TMhelix", "Beta sheet"}]
        source_features = None
        if acc in s20:
            source_features = [(n, int(a), int(b)) for n, a, b in re.findall(
                r"(interfacial|reentrant|transit_peptide|signal|TMhelix|Beta sheet)\((\d+)-(\d+)\)",
                s20[acc]["segments"])]
        fields = ("type", "topology_string", "segments", "membrane_types", "membrane_types_probabilities")
        cli_match = all(p[k] == cli[acc][k] for k in fields)
        repeat_match = all(all(p[k] == other[k] for k in fields) for other in predictions[1:])
        agreement.append(dict(gene=entry["gene"], cli_match=cli_match, repeat_match=repeat_match,
                              cli_topology_match=p["topology_string"] == cli[acc]["topology_string"],
                              cli_class_match=p["type"] == cli[acc]["type"],
                              cli_membrane_labels_match=p["membrane_types"] == cli[acc]["membrane_types"],
                              cli_scores_match=p["membrane_types_probabilities"] == cli[acc]["membrane_types_probabilities"],
                              s20_feature_match=feature_segments == source_features if source_features is not None else None))
        if not cli_match:
            differences.append(dict(gene=entry["gene"], accession=acc,
                                    fields={k: dict(api=p[k], cli=cli[acc][k]) for k in fields if p[k] != cli[acc][k]}))
        result.append(dict(gene=entry["gene"], accession=acc, cohort=entry["cohort"],
                           length=entry["length"], type=p["type"],
                           membrane_types=";".join(p["membrane_types"]),
                           tm_helices=sum(s["name"] == "TMhelix" for s in p["segments"]),
                           beta_strands=sum(s["name"] == "Beta sheet" for s in p["segments"]),
                           segments=";".join(f"{n}({a}-{b})" for n, a, b in feature_segments),
                           all_segments=";".join(f"{s['name']}({s['start']}-{s['end']})" for s in p["segments"]),
                           seconds_median=round(statistics.median(r["inference_seconds"] for r in runs), 3),
                           seconds_runs=";".join(f"{r['inference_seconds']:.3f}" for r in runs),
                           **{k: v for k, v in agreement[-1].items() if k != "gene"}))
    assert set(cli) == {e["accession"] for e in manifest}
    args.output.mkdir(parents=True, exist_ok=True)
    write_tsv(args.output / "summary.tsv", result)
    (args.output / "api_cli_differences.json").write_text(json.dumps(differences, indent=2) + "\n")
    stats = dict(sequences=len(manifest), residues=sum(int(r["length"]) for r in manifest),
                 length_min=min(int(r["length"]) for r in manifest),
                 length_max=max(int(r["length"]) for r in manifest),
                 imports_seconds=timings["imports_seconds"], model_load_seconds=timings["model_load_seconds"],
                 total_inference_seconds=sum(r["inference_seconds"] for r in timings["runs"]),
                 inference_seconds_by_repeat={str(i): sum(r["inference_seconds"] for r in timings["runs"] if r["repeat"] == i)
                                              for i in sorted({r["repeat"] for r in timings["runs"]})},
                 peak_rss_bytes=max(r["peak_rss_bytes"] for r in timings["runs"]),
                 cli_metadata=cli_metadata, comparisons=agreement)
    if args.precision_api:
        diagnostic_runs = json.loads((args.precision_api / "timings.json").read_text())["runs"]
        checks = []
        manifest_by_acc = {r["accession"]: r for r in manifest}
        for run in diagnostic_runs:
            acc = run["id"]
            assert run["sequence_sha256"] == manifest_by_acc[acc]["sequence_sha256"]
            prediction = json.loads((args.precision_api / f"{acc}.r{run['repeat']}.json").read_text())[0]
            checks.append(dict(gene=manifest_by_acc[acc]["gene"],
                               cli_match=all(prediction[k] == cli[acc][k] for k in fields)))
        stats["precision_diagnostic"] = checks
    (args.output / "summary.json").write_text(json.dumps(stats, indent=2) + "\n")
    print(json.dumps({k: v for k, v in stats.items() if k != "comparisons"}, indent=2))
    print("CLI matches:", sum(a["cli_match"] for a in agreement), "repeat matches:", sum(a["repeat_match"] for a in agreement))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    prep = sub.add_parser("prepare")
    prep.add_argument("--targets", type=Path, required=True)
    prep.add_argument("--repo", type=Path, required=True)
    prep.add_argument("--organism", required=True)
    prep.add_argument("--taxon", required=True)
    prep.add_argument("--output", type=Path, required=True)
    summary = sub.add_parser("summarize")
    summary.add_argument("--manifest", type=Path, required=True)
    summary.add_argument("--api", type=Path, required=True)
    summary.add_argument("--cli", type=Path, required=True)
    summary.add_argument("--s20", type=Path, required=True)
    summary.add_argument("--output", type=Path, required=True)
    summary.add_argument("--precision-api", type=Path)
    args = parser.parse_args()
    (prepare if args.command == "prepare" else summarize)(args)


if __name__ == "__main__":
    main()
