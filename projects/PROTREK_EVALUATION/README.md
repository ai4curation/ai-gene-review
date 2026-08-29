# ProTrek evaluation — pipeline and reproduction

Scripts and data for evaluating ProTrek (Su et al., *Nat Biotechnol* 2026,
[doi:10.1038/s41587-025-02836-0](https://doi.org/10.1038/s41587-025-02836-0)) on the
two cohorts — **ARGO-ProtNLM-50** (50 unreviewed TrEMBL proteins, shared with the ProtNLM2
evaluation) and **ARGO139** (the 139 genes of the BioReason comparison). See
[`../PROTREK_EVALUATION.md`](../PROTREK_EVALUATION.md) for the findings.

## Why the predictions had to be generated, not downloaded

ProTrek is a **retrieval** model, not a function predictor: it publishes model weights and
precomputed embedding indexes, not a table of per-protein predictions. There is no
prediction file to download, and no API on the public server
([search-protrek.com](http://search-protrek.com)). Predictions were therefore generated
locally by reproducing the server's `sequence -> text` mode against the authors' own
released SwissProt text indexes.

## Prerequisites (not committed — several GB)

```bash
# model weights (3.4 GB)
huggingface-cli download westlake-repl/ProTrek_650M --local-dir weights/ProTrek_650M

# SwissProt text indexes (only the subsections used here, ~600 MB)
base=https://huggingface.co/datasets/westlake-repl/faiss_index/resolve/main/SwissProt/ProTrek_650M_UniRef50/text/subsections
for f in GO_annotation Function Subcellular_location Catalytic_activity; do
  curl -sSL -o faiss_index/$f.index      $base/$f.index
  curl -sSL -o faiss_index/${f}_ids.tsv  $base/${f}_ids.tsv
done
```

A CPU-only PyTorch environment is enough; the 50-protein run takes about 4 minutes on
4 cores and the 139-protein run about 8 minutes. Only ProTrek's protein encoder is loaded — the text side is the precomputed index.

## Pipeline

```bash
# 1. assemble query sequences from the cached UniProt flatfiles
uv run python projects/PROTREK_EVALUATION/build_inputs.py
uv run python projects/PROTREK_EVALUATION/build_controls.py

# 2. embed and retrieve (needs the downloads above)
python projects/PROTREK_EVALUATION/run_protrek_retrieval.py \
    --weights weights/ProTrek_650M --faiss-dir faiss_index \
    --queries projects/PROTREK_EVALUATION/argo50_sequences.tsv \
    --subsections GO_annotation Function Subcellular_location Catalytic_activity \
    --topk 25 --out projects/PROTREK_EVALUATION/argo50_protrek_hits.tsv

# 3. resolve retrieved GO labels to ids and categorise against GOA
uv run python projects/PROTREK_EVALUATION/analyze_hits.py \
    --hits projects/PROTREK_EVALUATION/argo50_protrek_hits.tsv --topk 5 \
    --out projects/PROTREK_EVALUATION/argo50_protrek_go_calls.csv \
    --summary-out projects/PROTREK_EVALUATION/argo50_protrek_summary.json

# 4. head-to-head with ProtNLM2 on the same proteins
uv run python projects/PROTREK_EVALUATION/compare_with_protnlm.py \
    --protrek projects/PROTREK_EVALUATION/argo50_protrek_go_calls.csv \
    --protnlm projects/PROTNLM_EVALUATION/bench50_evaluation_results.csv \
    --out projects/PROTREK_EVALUATION/argo50_head_to_head.json

# 5. training-set overlap check (UniProt REST)
uv run python projects/PROTREK_EVALUATION/check_training_overlap.py \
    --queries projects/PROTREK_EVALUATION/argo50_sequences.tsv \
    --out projects/PROTREK_EVALUATION/argo50_training_overlap.csv

# curation context for one protein
uv run python projects/PROTREK_EVALUATION/dump_context.py A0A3B6GK97
```

## Cohort 2: ARGO139

Same steps, different query set. Gene directories in this cohort are named by **gene symbol**
rather than accession, so cohort-aware scripts take `--queries` and address genes as
`SPECIES/SYMBOL` (several symbols — `Akt1`, `Egfr`, `Myc`, `Notch1`, `Pten` — occur in more
than one species).

```bash
# 1-3. build, retrieve, analyse
uv run python projects/PROTREK_EVALUATION/build_argo139_inputs.py
python projects/PROTREK_EVALUATION/run_protrek_retrieval.py \
    --weights weights/ProTrek_650M --faiss-dir faiss_index \
    --queries projects/PROTREK_EVALUATION/argo139_sequences.tsv \
    --subsections GO_annotation Function Subcellular_location Catalytic_activity \
    --topk 25 --out projects/PROTREK_EVALUATION/argo139_protrek_hits.tsv
uv run python projects/PROTREK_EVALUATION/analyze_hits.py \
    --hits projects/PROTREK_EVALUATION/argo139_protrek_hits.tsv --topk 5 \
    --queries projects/PROTREK_EVALUATION/argo139_sequences.tsv \
    --out projects/PROTREK_EVALUATION/argo139_protrek_go_calls.csv \
    --summary-out projects/PROTREK_EVALUATION/argo139_protrek_summary.json

# 4. the memorisation control: how many queries are SwissProt (i.e. in the searched index)
uv run python projects/PROTREK_EVALUATION/check_swissprot_membership.py

# 5. curation digests, then author judgement-only specs and emit review YAMLs
uv run python projects/PROTREK_EVALUATION/dump_argo139_context.py yeast/SIR2 worm/pink-1
uv run python projects/PROTREK_EVALUATION/write_reviews.py spec.json

# 6. aggregate the curated assessments, and compare with BioReason-SFT / GO-GPT
uv run python projects/PROTREK_EVALUATION/aggregate_reviews.py \
    --calls projects/PROTREK_EVALUATION/argo139_protrek_go_calls.csv \
    --out projects/PROTREK_EVALUATION/argo139_assessment_summary.json
uv run python projects/PROTREK_EVALUATION/argo139_three_way.py \
    --out projects/PROTREK_EVALUATION/argo139_three_way.json

# 7. render the interactive assessment table for this cohort only
uv run python -m ai_gene_review.render_prediction_eval \
    'genes/*/*/*-protrek-predictions-review.yaml' \
    --ids-from projects/PROTREK_EVALUATION/argo139_sequences.tsv \
    -o projects/PROTREK_EVALUATION/protrek-eval-argo139.html \
    --title 'ProTrek ARGO139 Prediction Evaluation'
```

`write_reviews.py` takes a compact JSON spec in which the reviewer supplies only judgement
(assessment code, rationale, error type, supporting references) and names the prediction by
**rank**; the GO id, label, aspect and score are filled in from the committed
`*_protrek_go_calls.csv`, so a review can never drift from the retrieval it describes. It
refuses any rank whose label did not resolve to a GO id.

## Files

| File | Description |
|------|-------------|
| `build_inputs.py` | Assembles the 50 query sequences from cached UniProt flatfiles |
| `build_controls.py` | Positive-control query set (5 characterised SwissProt proteins) |
| `run_protrek_retrieval.py` | Local re-implementation of ProTrek `sequence -> text` retrieval |
| `analyze_hits.py` | GO label resolution + GOA overlap categorisation |
| `compare_with_protnlm.py` | Head-to-head with the ProtNLM2 calls on the same proteins |
| `check_training_overlap.py` | UniRef50 representative check (training-set proxy) |
| `dump_context.py` | Per-protein curation context |
| `argo50_sequences.tsv` | Query set |
| `argo50_protrek_hits.tsv` | Raw ranked retrieval output (top 25 per subsection) |
| `argo50_protrek_go_calls.csv` | Top-5 GO calls with resolution + GOA overlap category |
| `argo50_protrek_summary.json` | Aggregate counts for the above |
| `argo50_head_to_head.json` | ProTrek vs ProtNLM2 comparison |
| `argo50_training_overlap.csv` | UniRef50 cluster / representative status per query |
| `control_protrek_hits.tsv` | Positive-control retrieval output |
| `build_argo139_inputs.py` | Assembles the 139 ARGO139 query sequences |
| `check_swissprot_membership.py` | SwissProt vs TrEMBL per query — the memorisation control |
| `dump_argo139_context.py` | Per-gene curation digest, addressed as `SPECIES/SYMBOL` |
| `write_reviews.py` | Emits prediction-review YAMLs from a judgement-only JSON spec |
| `aggregate_reviews.py` | Aggregates the curated assessments for one cohort |
| `argo139_three_way.py` | ProTrek vs BioReason-SFT vs GO-GPT on the same 139 genes |
| `core_function_recall.py` | Rank at which each curated core function is retrieved |
| `score_vs_length.py` | Top-1 score against sequence length across both cohorts |
| `argo139_sequences.tsv` | ARGO139 query set |
| `argo139_protrek_hits.tsv` | Raw ranked retrieval output for ARGO139 |
| `argo139_protrek_go_calls.csv` | Top-5 GO calls with resolution + GOA overlap category |
| `argo139_assessment_summary.json` | Curated assessment counts, error types, score calibration |
| `argo139_three_way.json` | Three-model comparison output |
| `argo139_swissprot_status.csv` | SwissProt section status per ARGO139 query |
