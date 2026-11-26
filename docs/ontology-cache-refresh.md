# Ontology cache maintenance

`just ontology-cache-coverage` measures cache coverage; its `--warm` mode fills
gaps. `just refresh-ontology-cache` **rechecks existing values** by starting LTV
with an empty staging cache. Both use the gene, prediction-review and PANTHER
family-review surfaces supported by the coverage tool. Module-specific validators
and arbitrary ontology metadata checks are outside this scope.

```bash
# Preview; retains the existing cache unchanged.
just refresh-ontology-cache

# Apply a verified candidate. Use a new output directory for each local run.
just refresh-ontology-cache --output-dir reports/refresh-2 --apply

# A small, explicitly scoped refresh.
just refresh-ontology-cache genes/human/TP53 --output-dir reports/refresh-tp53
```

The refresh runs real online LTV checks, with bounded retries for service outages,
a per-batch timeout, and a total runtime budget (`--max-runtime`, seconds).
It then checks the same input offline against only the
new cache. Unreadable files, unrecognized output, cache misses, blocking label
mismatches and validation errors prevent application. GO label mismatches remain
advisory under the existing CI policy. An error produces a report without changing
the retained cache; fix or investigate the reported source/data problem and rerun.
No validation gate is weakened by installing this job.

Successful refreshes retain unrelated cache files and labels not used by the
selected corpus; those retained entries are **not** claimed freshly checked.
Online validation explicitly uses LTV's `--saturate-enum-caches` to materialize
full closures, including members absent from the selected corpus. Fresh completion
markers travel with their CSVs; an incomplete replacement cannot be applied.
By default **any membership removal blocks application**. Inspect the per-enum
before/after counts and ontology changes, then explicitly authorize a bounded
number with `--max-enum-removals N` if justified. This is a removal budget, not
permission to use incomplete closures or ignore validation failures.

LTV keys enum files by their definition. Identical `GOTermEnum` definitions in
family and mapping schemas share a cache file; refreshing that full closure also
affects mapping checks. Labels outside the selected corpus remain unrefreshed.
Unchanged labels retain their timestamps to avoid
timestamp-only PRs; run-level provenance records when they were rechecked.

`refresh-ontology-cache.yaml` is initially manual-only on the default branch.
Enable a monthly schedule only after a full-corpus preview completes within the
measured runtime budget; the first clean measurement is a deployment prerequisite.
It opens or updates one `auto/refresh-ontology-cache` PR only after successful
checks and a cache change. It never merges that PR automatically. The cadence is
managed by `.github/cron-profiles.yaml`; all profiles initially leave this job
unscheduled. The hosted job has a 360-minute limit and gives the refresh a
300-minute internal budget, leaving time to finish diagnostics and upload artifacts.

Reports are checkpointed before validation and after every batch, with phase,
completed/planned batch counts and elapsed time. A timeout or candidate/apply error
leaves `ready: false` and a durable diagnostic report. The summary includes label
changes, per-enum membership additions/removals, completion state, advisory label
mismatches and source hashes, so the maintenance PR remains reviewable after its
logs expire. Use a fresh output directory for each attempt; existing evidence is
never overwritten. Interrupted cache swaps keep a recovery directory outside any
automatically deleted temporary context.

The scheduled job deliberately does not restore OAK SQLite databases, so the
available builds are resolved afresh. Locally, an existing OAK database **is**
reused: refreshing LTV's CSV files does not update that database. The report records
hashes of available local ontology sources, schema/configuration/input hashes,
tool versions and retrieval times. OLS remains a live, unpinned source, not an
asserted immutable release. Cache PR commit messages retain this provenance;
detailed reports/logs are workflow artifacts retained for 14 days.

This command owns LTV's label/membership caches, not `cache/ontologies/go.tsv`:
that separate label cache remains managed by `just update-cache go` and
`just fix-labels`. Relative CLI paths are resolved from the repository root,
including when invoked from a subdirectory.

The workflow leaves curated records and provider research untouched. If ontology
changes invalidate a record, it reports that drift for curation instead of fixing
the record automatically. A refresh cannot cover terms added after its run:
new-term PRs still need to warm and commit their required entries. Moving more
CI checks fully offline remains separate work tracked in #5731.
