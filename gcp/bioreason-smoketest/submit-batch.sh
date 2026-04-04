#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TEMPLATE_PATH="${SCRIPT_DIR}/batch-job.template.json"
RENDERED_PATH="${SCRIPT_DIR}/.rendered-batch-job.json"

: "${PROJECT_ID:?Set PROJECT_ID}"
LOCATION="${LOCATION:-${REGION}}"
AR_REPO="${AR_REPO:-bioreason-smoke}"
IMAGE_NAME="${IMAGE_NAME:-bioreason-smoke}"
TAG="${TAG:-latest}"
IMAGE_URI="${IMAGE_URI:-${LOCATION}-docker.pkg.dev/${PROJECT_ID}/${AR_REPO}/${IMAGE_NAME}:${TAG}}"
JOB_PREFIX="${JOB_PREFIX:-bioreason-smoke-tp53}"
JOB_NAME="${JOB_NAME:-${JOB_PREFIX}-$(date -u +%Y%m%d-%H%M%S)}"
SERVICE_ACCOUNT_NAME="${SERVICE_ACCOUNT_NAME:-bioreason-batch-runner}"
SERVICE_ACCOUNT="${SERVICE_ACCOUNT:-${SERVICE_ACCOUNT_NAME}@${PROJECT_ID}.iam.gserviceaccount.com}"
BUCKET="${BUCKET:-gs://${PROJECT_ID}-bioreason-smoke}"
INPUT_OBJECT="${INPUT_OBJECT:-inputs/tp53-smoketest.json}"
INPUT_GCS_URI="${INPUT_GCS_URI:-${BUCKET}/${INPUT_OBJECT}}"
OUTPUT_PREFIX="${OUTPUT_PREFIX:-outputs/${JOB_NAME}}"
OUTPUT_GCS_PREFIX="${OUTPUT_GCS_PREFIX:-${BUCKET}/${OUTPUT_PREFIX}}"
PROVISIONING_MODEL="${PROVISIONING_MODEL:-STANDARD}"
MACHINE_TYPE="${MACHINE_TYPE:-a2-highgpu-1g}"
ALLOWED_LOCATION="${ALLOWED_LOCATION:-regions/${REGION}}"
RENDER_ONLY="${RENDER_ONLY:-0}"
PYTHON_BIN="${PYTHON_BIN:-python3}"
export LOCATION
export IMAGE_URI
export JOB_NAME
export SERVICE_ACCOUNT
export INPUT_GCS_URI
export OUTPUT_GCS_PREFIX
export PROVISIONING_MODEL
export MACHINE_TYPE
export ALLOWED_LOCATION

"${PYTHON_BIN}" - "$TEMPLATE_PATH" "$RENDERED_PATH" <<'PY'
import json
import os
import sys
from pathlib import Path

template_path = Path(sys.argv[1])
rendered_path = Path(sys.argv[2])

content = template_path.read_text()
replacements = {
    "__IMAGE_URI__": os.environ["IMAGE_URI"],
    "__INPUT_GCS_URI__": os.environ["INPUT_GCS_URI"],
    "__OUTPUT_GCS_PREFIX__": os.environ["OUTPUT_GCS_PREFIX"],
    "__SERVICE_ACCOUNT__": os.environ["SERVICE_ACCOUNT"],
    "__PROVISIONING_MODEL__": os.environ.get("PROVISIONING_MODEL", "STANDARD"),
    "__MACHINE_TYPE__": os.environ.get("MACHINE_TYPE", "a2-highgpu-1g"),
    "__ALLOWED_LOCATION__": os.environ.get("ALLOWED_LOCATION", "regions/${REGION}"),
}

for needle, value in replacements.items():
    content = content.replace(needle, value)

rendered = json.loads(content)
rendered_path.write_text(json.dumps(rendered, indent=2))
print(rendered_path)
PY

if [[ "${RENDER_ONLY}" == "1" ]]; then
  echo "Rendered Batch config: ${RENDERED_PATH}"
  echo "Submit command:"
  echo "gcloud batch jobs submit \"${JOB_NAME}\" --location \"${LOCATION}\" --project \"${PROJECT_ID}\" --config \"${RENDERED_PATH}\""
  exit 0
fi

gcloud batch jobs submit "${JOB_NAME}" \
  --location "${LOCATION}" \
  --project "${PROJECT_ID}" \
  --config "${RENDERED_PATH}"
