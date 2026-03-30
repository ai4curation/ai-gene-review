#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TEMPLATE_PATH="${SCRIPT_DIR}/batch-job.template.json"
RENDERED_PATH="${SCRIPT_DIR}/.rendered-batch-job.json"

: "${PROJECT_ID:?Set PROJECT_ID}"
: "${LOCATION:?Set LOCATION}"
: "${JOB_NAME:?Set JOB_NAME}"
: "${IMAGE_URI:?Set IMAGE_URI}"
: "${SERVICE_ACCOUNT:?Set SERVICE_ACCOUNT}"
: "${INPUT_GCS_URI:?Set INPUT_GCS_URI}"
: "${OUTPUT_GCS_PREFIX:?Set OUTPUT_GCS_PREFIX}"

PROVISIONING_MODEL="${PROVISIONING_MODEL:-STANDARD}"
MACHINE_TYPE="${MACHINE_TYPE:-a2-highgpu-1g}"
ALLOWED_LOCATION="${ALLOWED_LOCATION:-regions/us-central1}"
export PROVISIONING_MODEL
export MACHINE_TYPE
export ALLOWED_LOCATION

python - "$TEMPLATE_PATH" "$RENDERED_PATH" <<'PY'
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
    "__ALLOWED_LOCATION__": os.environ.get("ALLOWED_LOCATION", "regions/us-central1"),
}

for needle, value in replacements.items():
    content = content.replace(needle, value)

rendered = json.loads(content)
rendered_path.write_text(json.dumps(rendered, indent=2))
print(rendered_path)
PY

gcloud batch jobs submit "${JOB_NAME}" \
  --location "${LOCATION}" \
  --project "${PROJECT_ID}" \
  --config "${RENDERED_PATH}"
