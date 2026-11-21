"""Benchmark installed DeepTMHMM2 on supplied FASTA; preserve predictions and timings."""
import argparse
import hashlib
import importlib.metadata
import json
import platform
import resource
import time
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("fasta", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--model-dir", type=Path, required=True)
    parser.add_argument("--threads", type=int, default=8)
    parser.add_argument("--repeats", type=int, default=2)
    parser.add_argument("--marginals", action="store_true")
    parser.add_argument("--cpu-autocast", action="store_true",
                        help="Use CPU autocast for task-model inference, matching the upstream CLI; ESM stays FP32")
    parser.add_argument("--unbatch-api", action="store_true",
                        help="Work around pinned upstream API passing batched topology lists to string postprocessing")
    args = parser.parse_args()
    if args.threads < 1 or args.repeats < 1:
        parser.error("threads and repeats must be positive")
    args.output.mkdir(parents=True, exist_ok=True)
    start = time.perf_counter()
    from Bio import SeqIO
    import torch
    from deeptmhmm2_predictor import DeepTMHMM2
    imports_seconds = time.perf_counter() - start
    records = list(SeqIO.parse(args.fasta, "fasta"))
    if not records or len({r.id for r in records}) != len(records):
        parser.error("FASTA must contain records with unique identifiers")
    if any(not str(r.seq) or not set(str(r.seq)) <= set("ACDEFGHIKLMNPQRSTVWY") for r in records):
        parser.error("FASTA must contain nonempty canonical protein sequences")
    torch.manual_seed(0)
    start = time.perf_counter()
    model = DeepTMHMM2(model_dir=args.model_dir, device="cpu", num_threads=args.threads)
    load_seconds = time.perf_counter() - start
    if args.cpu_autocast:
        model_predict = model._models.predict_single_model

        def predict_autocast(*positional, **keywords):
            with torch.autocast("cpu"):
                return model_predict(*positional, **keywords)

        model._models.predict_single_model = predict_autocast
    if args.unbatch_api:
        original_predict = model._models.predict_single_model

        def predict_unbatched(*positional, **keywords):
            topology, membrane_probs, marginals, duration = original_predict(*positional, **keywords)
            assert isinstance(topology, list) and len(topology) == 1
            return topology[0], membrane_probs, marginals[0] if marginals else None, duration

        model._models.predict_single_model = predict_unbatched
    report = {
        "platform": platform.platform(), "device": "cpu", "threads": args.threads,
        "torch": torch.__version__, "deeptmhmm2_predictor": importlib.metadata.version("deeptmhmm2_predictor"),
        "imports_seconds": imports_seconds, "model_load_seconds": load_seconds,
        "compute_marginals": args.marginals, "unbatch_api_workaround": args.unbatch_api, "runs": [],
        "task_model_cpu_autocast": args.cpu_autocast,
    }
    print(json.dumps({k: v for k, v in report.items() if k != "runs"}), flush=True)
    for repeat in range(args.repeats):
        for record in records:
            start = time.perf_counter()
            predictions = model.predict({record.id: str(record.seq)}, progress_bar=False,
                                        compute_marginals=args.marginals)
            elapsed = time.perf_counter() - start
            prediction = predictions[0]
            assert len(prediction.topology_string) == len(record.seq)
            if args.unbatch_api:
                assert prediction.segments[0][1] == 1
                assert prediction.segments[-1][2] == len(record.seq)
                assert all(left[2] + 1 == right[1] for left, right in zip(prediction.segments, prediction.segments[1:]))
            prefix = args.output / f"{record.id}.r{repeat + 1}"
            predictions.to_json(str(prefix) + ".json")
            predictions.to_gff3(str(prefix) + ".gff3")
            predictions.to_3line(str(prefix) + ".3line")
            predictions.to_memtype_tsv(str(prefix) + ".tsv")
            row = {"id": record.id, "length": len(record.seq), "repeat": repeat + 1,
                   "sequence_sha256": hashlib.sha256(str(record.seq).encode()).hexdigest(),
                   "inference_seconds": elapsed,
                   "peak_rss_bytes": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * (1 if platform.system() == "Darwin" else 1024)}
            report["runs"].append(row)
            (args.output / "timings.json").write_text(json.dumps(report, indent=2) + "\n")
            print(json.dumps(row), flush=True)


if __name__ == "__main__":
    main()
