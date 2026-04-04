# BioReason GCP Smoke Test

This directory contains a minimal first-pass GCP deployment path for running a
single BioReason smoke test in project `test-project-covid-19-277821`.

## Why Batch

This path uses Google Cloud Batch instead of Vertex AI because the first goal is
to run one offline GPU container job, not stand up a managed endpoint or a
training workflow. Batch is the shortest path from "container + GPU + input JSON"
to "did BioReason generate output?".

Vertex custom jobs would also work, but they add AI Platform-specific control
plane concepts that do not buy much for a one-container smoke test. For the
first real attempt in this project, Batch is the better fit.

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
- `validate-local.sh`: safe local validation, including Batch config rendering.
- `CHECKLIST.md`: IAM/services checklist.
- `run.env.example`: concrete variable names and defaults.
- `examples/tp53-smoketest.json`: example input.

## Exact Commands

Start from this directory:

```bash
cd /Users/cjm/repos/ai-gene-review/gcp/bioreason-smoketest
```

Set your shell variables first. The easiest path is to copy the example file:

```bash
cp run.env.example run.env
source run.env

export SERVICE_ACCOUNT="${SERVICE_ACCOUNT_NAME}@${PROJECT_ID}.iam.gserviceaccount.com"
export IMAGE_URI="${LOCATION}-docker.pkg.dev/${PROJECT_ID}/${AR_REPO}/${IMAGE_NAME}:${TAG}"
export INPUT_GCS_URI="${BUCKET}/${INPUT_OBJECT}"
export JOB_NAME="${JOB_PREFIX}-$(date -u +%Y%m%d-%H%M%S)"
export OUTPUT_GCS_PREFIX="${BUCKET}/outputs/${JOB_NAME}"
```

If you prefer not to create `run.env`, these are the exact variables:

```bash
export PROJECT_ID=test-project-covid-19-277821
export PROJECT_NUMBER=1091817516808
export LOCATION=${REGION}
export ALLOWED_LOCATION=regions/${REGION}
export PROVISIONING_MODEL=STANDARD
export MACHINE_TYPE=a2-highgpu-1g
export AR_REPO=bioreason-smoke
export IMAGE_NAME=bioreason-smoke
export TAG=20260330
export SERVICE_ACCOUNT_NAME=bioreason-batch-runner
export IMAGE_URI="${LOCATION}-docker.pkg.dev/${PROJECT_ID}/${AR_REPO}/${IMAGE_NAME}:${TAG}"
export BUCKET="gs://${PROJECT_ID}-bioreason-smoke"
export INPUT_OBJECT=inputs/tp53-smoketest.json
export INPUT_GCS_URI="${BUCKET}/${INPUT_OBJECT}"
export JOB_PREFIX=bioreason-smoke-tp53
export JOB_NAME="${JOB_PREFIX}-$(date -u +%Y%m%d-%H%M%S)"
export SERVICE_ACCOUNT="${SERVICE_ACCOUNT_NAME}@${PROJECT_ID}.iam.gserviceaccount.com"
export OUTPUT_GCS_PREFIX="${BUCKET}/outputs/${JOB_NAME}"
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

Create the dedicated Batch runtime service account if it does not already exist:

```bash
gcloud iam service-accounts describe "${SERVICE_ACCOUNT}" \
  --project "${PROJECT_ID}" >/dev/null 2>&1 || \
gcloud iam service-accounts create "${SERVICE_ACCOUNT_NAME}" \
  --display-name="BioReason Batch runtime" \
  --project "${PROJECT_ID}"
```

Grant the minimum runtime roles to that service account:

```bash
gcloud projects add-iam-policy-binding "${PROJECT_ID}" \
  --member "serviceAccount:${SERVICE_ACCOUNT}" \
  --role roles/artifactregistry.reader

gcloud projects add-iam-policy-binding "${PROJECT_ID}" \
  --member "serviceAccount:${SERVICE_ACCOUNT}" \
  --role roles/logging.logWriter

gcloud storage buckets add-iam-policy-binding "${BUCKET}" \
  --member "serviceAccount:${SERVICE_ACCOUNT}" \
  --role roles/storage.objectViewer

gcloud storage buckets add-iam-policy-binding "${BUCKET}" \
  --member "serviceAccount:${SERVICE_ACCOUNT}" \
  --role roles/storage.objectCreator
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

Safe local dry-run: render the exact Batch config without touching GCP:

```bash
PROJECT_ID="${PROJECT_ID}" \
LOCATION="${LOCATION}" \
AR_REPO="${AR_REPO}" \
IMAGE_NAME="${IMAGE_NAME}" \
TAG="${TAG}" \
SERVICE_ACCOUNT_NAME="${SERVICE_ACCOUNT_NAME}" \
BUCKET="${BUCKET}" \
JOB_PREFIX="${JOB_PREFIX}" \
RENDER_ONLY=1 \
./submit-batch.sh

python3 -m json.tool .rendered-batch-job.json >/dev/null
```

Or run the bundled local validator:

```bash
./validate-local.sh
```

Submit the Batch job:

```bash
PROJECT_ID="${PROJECT_ID}" \
LOCATION="${LOCATION}" \
JOB_NAME="${JOB_NAME}" \
IMAGE_URI="${IMAGE_URI}" \
SERVICE_ACCOUNT="${SERVICE_ACCOUNT}" \
INPUT_GCS_URI="${BUCKET}/inputs/tp53-smoketest.json" \
OUTPUT_GCS_PREFIX="${OUTPUT_GCS_PREFIX}" \
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
gcloud storage ls "${OUTPUT_GCS_PREFIX%/}/"
```

Download outputs locally:

```bash
mkdir -p /tmp/bioreason-smoke
gcloud storage cp --recursive \
  "${OUTPUT_GCS_PREFIX%/}/" \
  /tmp/bioreason-smoke
```

## Notes

- The default machine type in the Batch template is `a2-highgpu-1g`. This is
  conservative for a first run.
- The exact job naming convention is `bioreason-smoke-tp53-YYYYmmdd-HHMMSS`.
- The Batch template keeps external IPs enabled so the container can fetch
  public Hugging Face artifacts. That is deliberate for the first smoke test.
- I did not submit any jobs from this repo because current access to the target
  project is not sufficient to verify enabled services, quotas, or Batch
  runtime permissions.
