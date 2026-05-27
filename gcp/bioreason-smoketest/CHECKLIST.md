# IAM And Services Checklist

## APIs

Enable these in `test-project-covid-19-277821`:

- `artifactregistry.googleapis.com`
- `batch.googleapis.com`
- `compute.googleapis.com`
- `logging.googleapis.com`
- `storage.googleapis.com`
- `cloudbuild.googleapis.com`

## Human Roles

The person building and submitting the smoke test should have enough access for:

- enabling services
- creating or reading Artifact Registry repositories
- pushing container images
- creating or reading Cloud Storage buckets and objects
- submitting and describing Batch jobs
- acting as the Batch runtime service account

In practice, the minimum roles usually include some combination of:

- `roles/serviceusage.serviceUsageAdmin`
- `roles/artifactregistry.admin` or `roles/artifactregistry.writer`
- `roles/storage.admin` or narrower object-level roles
- `roles/batch.jobsEditor`
- `roles/iam.serviceAccountUser`

## Batch Runtime Service Account

The runtime service account should have enough access for:

- reading the Batch container image from Artifact Registry
- reading the input JSON from GCS
- writing the output JSON/text back to GCS
- writing logs

In practice, that usually means:

- `roles/artifactregistry.reader`
- `roles/storage.objectViewer` on the input bucket/prefix
- `roles/storage.objectCreator` or `roles/storage.objectAdmin` on the output bucket/prefix
- `roles/logging.logWriter`

## Quota Checks

Before the first submission, verify:

- GPU quota in the chosen region
- availability of `a2-highgpu-1g` in the chosen region
- Artifact Registry and GCS access from the submitting account

## Explicit Smoke-Test Assumptions

- external IPs are allowed for the Batch VM
- public Hugging Face downloads are allowed
- no gated EvolutionaryScale access is required because this path uses the SFT
  checkpoint and the bundled `protein_model/`
