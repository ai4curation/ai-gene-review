# BioReason GCP Smoke Test

This directory contains a minimal first-pass GCP deployment path for running a
single BioReason smoke test in project `test-project-covid-19-277821`.

## Why Batch

This path uses Google Cloud Batch instead of Vertex AI because the first goal is
to run one offline GPU container job, not stand up a managed endpoint or a
training workflow. Batch is the shortest path from "container + GPU + input JSON"
to "did BioReason generate output?".

## What This Smoke Test Does

- Builds a Linux GPU container that clones `BioReason-Pro`.
- Downloads the public BioReason SFT checkpoint and GO-GPT checkpoint at runtime.
- Runs GO-GPT first to get textual GO speculations.
- Runs the BioReason SFT checkpoint on a single sequence and writes JSON/text
  outputs.
- Uploads results back to GCS if `OUTPUT_GCS_PREFIX` is set.

## Why SFT, Not RL

The published RL checkpoint does not bundle `protein_model/`, while the open
source inference code tries to initialize `esm3_sm_open_v1` before it loads any
checkpoint-local protein model. In this environment, `esm3_sm_open_v1` resolves
to the gated repo `EvolutionaryScale/esm3-sm-open-v1`. The SFT checkpoint does
bundle `protein_model/`, so this smoke test uses SFT and registers that local
protein model before model construction.

## What This Smoke Test Intentionally Skips

- The GO graph embedding path is disabled for the first smoke test.
- The runner injects GO-GPT predictions as text context instead.
- InterPro and PPI are optional and default to `"None"`.

This keeps the first run focused on the main blockers: container build, GPU
execution, checkpoint loading, prompt construction, and end-to-end generation.

## Files

- `Dockerfile`: GPU runtime image for the smoke test.
- `bioreason_smoketest.py`: single-sequence smoke-test runner.
- `run_smoketest.sh`: container entrypoint used by Batch.
- `batch-job.template.json`: Batch job template with placeholders.
- `build-and-push.sh`: local Docker build and push helper.
- `submit-batch.sh`: render + submit helper for Batch.
- `CHECKLIST.md`: IAM/services checklist.
- `examples/tp53-smoketest.json`: example input.

## Exact Commands

Set your shell variables first:

```bash
export PROJECT_ID=test-project-covid-19-277821
export PROJECT_NUMBER=1091817516808
export LOCATION=us-central1
export AR_REPO=bioreason-smoke
export IMAGE_NAME=bioreason-smoke
export TAG=20260330
export IMAGE_URI="${LOCATION}-docker.pkg.dev/${PROJECT_ID}/${AR_REPO}/${IMAGE_NAME}:${TAG}"
export BUCKET="gs://${PROJECT_ID}-bioreason-smoke"
export JOB_NAME="bioreason-smoke-$(date -u +%Y%m%d-%H%M%S)"
export SERVICE_ACCOUNT="REPLACE_ME_BATCH_RUNTIME_SA@${PROJECT_ID}.iam.gserviceaccount.com"
```

Enable the required services:

```bash
gcloud services enable \
  artifactregistry.googleapis.com \
  batch.googleapis.com \
  compute.googleapis.com \
  logging.googleapis.com \
  storage.googleapis.com \
  cloudbuild.googleapis.com \
  --project "${PROJECT_ID}"
```

Create an Artifact Registry repo and a staging bucket if they do not already exist:

```bash
gcloud artifacts repositories describe "${AR_REPO}" \
  --location "${LOCATION}" \
  --project "${PROJECT_ID}" >/dev/null 2>&1 || \
gcloud artifacts repositories create "${AR_REPO}" \
  --repository-format=docker \
  --location "${LOCATION}" \
  --description="BioReason smoke-test images" \
  --project "${PROJECT_ID}"

gcloud storage buckets describe "${BUCKET}" --project "${PROJECT_ID}" >/dev/null 2>&1 || \
gcloud storage buckets create "${BUCKET}" \
  --location "${LOCATION}" \
  --project "${PROJECT_ID}"
```

Build and push the image from this directory:

```bash
PROJECT_ID="${PROJECT_ID}" \
LOCATION="${LOCATION}" \
AR_REPO="${AR_REPO}" \
IMAGE_NAME="${IMAGE_NAME}" \
TAG="${TAG}" \
./build-and-push.sh
```

Upload the example input:

```bash
gcloud storage cp \
  examples/tp53-smoketest.json \
  "${BUCKET}/inputs/tp53-smoketest.json"
```

Submit the Batch job:

```bash
PROJECT_ID="${PROJECT_ID}" \
LOCATION="${LOCATION}" \
JOB_NAME="${JOB_NAME}" \
IMAGE_URI="${IMAGE_URI}" \
SERVICE_ACCOUNT="${SERVICE_ACCOUNT}" \
INPUT_GCS_URI="${BUCKET}/inputs/tp53-smoketest.json" \
OUTPUT_GCS_PREFIX="${BUCKET}/outputs" \
./submit-batch.sh
```

Inspect the job:

```bash
gcloud batch jobs describe "${JOB_NAME}" \
  --location "${LOCATION}" \
  --project "${PROJECT_ID}"
```

List outputs:

```bash
gcloud storage ls "${BUCKET}/outputs/"
```

Download outputs locally:

```bash
mkdir -p /tmp/bioreason-smoke
gcloud storage cp --recursive \
  "${BUCKET}/outputs/" \
  /tmp/bioreason-smoke
```

## Notes

- The default machine type in the Batch template is `a2-highgpu-1g`. This is
  conservative for a first run.
- The Batch template keeps external IPs enabled so the container can fetch
  public Hugging Face artifacts. That is deliberate for the first smoke test.
- I did not submit any jobs from this repo because current access to the target
  project is not sufficient to verify enabled services, quotas, or Batch
  runtime permissions.
