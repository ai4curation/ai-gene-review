#!/usr/bin/env python3
"""Emit PredictionReview YAMLs for ProTrek calls from a compact JSON spec.

The reviewer supplies judgement (assessment, error type, rationale, supporting
evidence); everything mechanical -- taxon, rank, score, term label, source
metadata, the aspect-derived predicted_term_type, and the assessment tally in the
description -- is filled in from the cohort's committed retrieval output so it
cannot drift from the data.

Spec format (JSON):
  {"cohort": "argo139",
   "genes": {
     "SCHPO/tpx1": {
       "description": "free text; an assessment tally is appended automatically",
       "predictions": [
         {"rank": 1, "assessment": "CNN", "summary": "...",
          "error_type": "PARALOG_OVERANNOTATION",          # optional
          "support": [["GO_REF:0000033", "Annotation inferences using phylogenetic trees"]]}
       ]}}}

``rank`` selects the prediction from the cohort's *_protrek_go_calls.csv, so the
GO id and label always match what the model actually returned.

Usage: uv run python projects/PROTREK_EVALUATION/write_reviews.py spec.json
"""
from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).parent
CS = {"COR": 2, "CNN": 2, "LSP": 2, "UNC": 1, "PLI": 0, "NPI": 0, "REP": 0}
ASPECT_TYPE = {"F": "GO_MF", "P": "GO_BP", "C": "GO_CC"}
LABEL = {"COR": "correct novel", "CNN": "correct not novel", "LSP": "less precise",
         "UNC": "uncertain", "PLI": "paralog incorrect", "NPI": "nonparalog incorrect",
         "REP": "repetition"}
SOURCE = {
    "source_method": "ProTrek",
    "source_version": "ProTrek_650M, SwissProt ProTrek_650M_UniRef50 text index",
    "source_reference_id": "PMID:41039041",
}


class Str(str):
    pass


def _block(dumper, data):
    return dumper.represent_scalar("tag:yaml.org,2002:str", " ".join(data.split()), style=">")


yaml.add_representer(Str, _block)


def main() -> int:
    spec = json.loads(Path(sys.argv[1]).read_text())
    cohort = spec["cohort"]
    calls = {(r["accession"], int(r["rank"])): r
             for r in csv.DictReader((HERE / f"{cohort}_protrek_go_calls.csv").open())}
    queries = {f"{r['species_dir']}/{r['symbol']}": r
               for r in csv.DictReader((HERE / f"{cohort}_sequences.tsv").open(), delimiter="\t")}

    for key, g in spec["genes"].items():
        q = queries[key]
        acc, species, symbol = q["accession"], q["species_dir"], q["symbol"]
        preds, tally = [], []
        for p in g["predictions"]:
            call = calls[(acc, p["rank"])]
            if not call["pred_id"]:
                raise SystemExit(f"{key} rank {p['rank']} has no resolvable GO id; pick another rank")
            review = {"assessment": p["assessment"], "confidence_score": CS[p["assessment"]]}
            if p.get("error_type"):
                review["error_type"] = p["error_type"]
            review["summary"] = Str(p["summary"])
            if p.get("support"):
                review["supported_by"] = [{"reference_id": r, "supporting_text": Str(t)}
                                          for r, t in p["support"]]
            preds.append({**SOURCE,
                          "predicted_term": {"id": call["pred_id"], "label": call["pred_label"]},
                          "predicted_term_type": ASPECT_TYPE[call["aspect"]],
                          "review": review})
            tally.append(p["assessment"])

        counts = {k: tally.count(k) for k in ("COR", "CNN", "LSP", "UNC", "PLI", "NPI", "REP")}
        summary_line = "Assessment: " + ", ".join(
            f"{v} {LABEL[k]} ({k})" for k, v in counts.items() if v) + "."
        doc = {
            "id": acc,
            "gene_symbol": symbol,
            "taxon": {"id": f"NCBITaxon:{q['taxon_id']}", "label": q["organism"]},
            "status": "COMPLETE",
            "description": Str(g["description"] + " " + summary_line),
            "source_documents": [
                f"projects/PROTREK_EVALUATION/{cohort}_protrek_hits.tsv",
                f"genes/{species}/{symbol}/{symbol}-uniprot.txt",
                f"genes/{species}/{symbol}/{symbol}-goa.tsv",
            ],
            "predictions": preds,
        }
        out = ROOT / "genes" / species / symbol / f"{symbol}-protrek-predictions-review.yaml"
        out.write_text(yaml.dump(doc, sort_keys=False, width=96, allow_unicode=True))
        print(f"wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
