#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

: "${PROJECT_ID:?Set PROJECT_ID}"
LOCATION="${LOCATION:-${REGION}}"
AR_REPO="${AR_REPO:-bioreason-smoke}"
IMAGE_NAME="${IMAGE_NAME:-bioreason-smoke}"
TAG="${TAG:-$(date -u +%Y%m%d-%H%M%S)}"
BIOREASON_PRO_REF="${BIOREASON_PRO_REF:-main}"

IMAGE_URI="${LOCATION}-docker.pkg.dev/${PROJECT_ID}/${AR_REPO}/${IMAGE_NAME}:${TAG}"

gcloud auth configure-docker "${LOCATION}-docker.pkg.dev" --quiet

docker buildx build \
  --platform linux/amd64 \
  --build-arg BIOREASON_PRO_REF="${BIOREASON_PRO_REF}" \
  -t "${IMAGE_URI}" \
  "${SCRIPT_DIR}"

docker push "${IMAGE_URI}"

echo "${IMAGE_URI}"
