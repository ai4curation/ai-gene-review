#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

python3 -m py_compile "${SCRIPT_DIR}/bioreason_smoketest.py"
bash -n \
  "${SCRIPT_DIR}/build-and-push.sh" \
  "${SCRIPT_DIR}/run_smoketest.sh" \
  "${SCRIPT_DIR}/submit-batch.sh"
python3 -m json.tool "${SCRIPT_DIR}/batch-job.template.json" >/dev/null
python3 -m json.tool "${SCRIPT_DIR}/examples/tp53-smoketest.json" >/dev/null

PROJECT_ID="example-project" \
LOCATION="us-central1" \
AR_REPO="bioreason-smoke" \
IMAGE_NAME="bioreason-smoke" \
TAG="dryrun" \
SERVICE_ACCOUNT_NAME="bioreason-batch-runner" \
BUCKET="gs://example-project-bioreason-smoke" \
JOB_PREFIX="bioreason-smoke-tp53" \
RENDER_ONLY=1 \
"${SCRIPT_DIR}/submit-batch.sh" >/dev/null

python3 -m json.tool "${SCRIPT_DIR}/.rendered-batch-job.json" >/dev/null
echo "local validation ok"
