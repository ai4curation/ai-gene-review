#!/usr/bin/env bash
set -euo pipefail

WORKDIR="${WORKDIR:-/workdir}"
CACHE_DIR="${MODEL_CACHE_DIR:-${WORKDIR}/hf-cache}"
RUN_ID="${RUN_ID:-$(date -u +%Y%m%dT%H%M%SZ)}"
RUN_DIR="${WORKDIR}/run-${RUN_ID}"

mkdir -p "${RUN_DIR}" "${CACHE_DIR}"

export HF_HOME="${CACHE_DIR}"
export TRANSFORMERS_CACHE="${CACHE_DIR}"
export HUGGINGFACE_HUB_CACHE="${CACHE_DIR}"

INPUT_JSON_LOCAL="${INPUT_JSON_LOCAL:-/app/examples/tp53-smoketest.json}"

if [[ -n "${INPUT_GCS_URI:-}" ]]; then
  INPUT_JSON_LOCAL="${RUN_DIR}/input.json"
  echo "Downloading input JSON from ${INPUT_GCS_URI}"
  gcloud storage cp "${INPUT_GCS_URI}" "${INPUT_JSON_LOCAL}"
fi

echo "Running BioReason smoke test"
echo "  Input: ${INPUT_JSON_LOCAL}"
echo "  Output dir: ${RUN_DIR}"
echo "  BioReason model: ${BIOREASON_MODEL_ID:-wanglab/bioreason-pro-sft}"
echo "  GO-GPT model: ${GOGPT_MODEL_ID:-wanglab/gogpt}"

python /app/bioreason_smoketest.py \
  --input-json "${INPUT_JSON_LOCAL}" \
  --output-dir "${RUN_DIR}" \
  --bioreason-model-id "${BIOREASON_MODEL_ID:-wanglab/bioreason-pro-sft}" \
  --gogpt-model-id "${GOGPT_MODEL_ID:-wanglab/gogpt}" \
  --cache-dir "${CACHE_DIR}" \
  --max-model-len "${MAX_MODEL_LEN:-8192}" \
  --max-new-tokens "${MAX_NEW_TOKENS:-1200}" \
  --temperature "${TEMPERATURE:-0.0}" \
  --top-p "${TOP_P:-0.95}"

if [[ -n "${OUTPUT_GCS_PREFIX:-}" ]]; then
  echo "Uploading outputs to ${OUTPUT_GCS_PREFIX}"
  gcloud storage cp --recursive "${RUN_DIR}" "${OUTPUT_GCS_PREFIX%/}/"
fi

echo "Smoke test finished"
