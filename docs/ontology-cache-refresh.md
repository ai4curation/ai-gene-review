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

The refresh runs real online LTV checks, with bounded retries for service outages
and a per-batch timeout. It then checks the same input offline against only the
new cache. Unreadable files, unrecognized output, cache misses, blocking label
mismatches and validation errors prevent application. GO label mismatches remain
advisory under the existing CI policy. An error produces a report without changing
the retained cache; fix or investigate the reported source/data problem and rerun.
No validation gate is weakened by installing this job.

Successful refreshes retain unrelated cache files and labels not used by the
selected corpus; those retained entries are **not** claimed freshly checked.
Refreshed enum files are replaced with the memberships proven in this run, with
any old `.complete` marker removed. A positive corpus cache is not an exhaustive
ontology closure. Unchanged labels retain their timestamps to avoid weekly
timestamp-only PRs; run-level provenance records when they were rechecked.

`refresh-ontology-cache.yaml` runs weekly and manually on the default branch.
It opens or updates one `auto/refresh-ontology-cache` PR only after successful
checks and a cache change. It never merges that PR automatically. The cadence is
managed by `.github/cron-profiles.yaml`, including the `off` profile.

The scheduled job deliberately does not restore OAK SQLite databases, so the
available builds are resolved afresh. Locally, an existing OAK database **is**
reused: refreshing LTV's CSV files does not update that database. The report records
hashes of available local ontology sources, schema/configuration/input hashes,
tool versions and retrieval times. OLS remains a live, unpinned source, not an
asserted immutable release. Cache PR commit messages retain this provenance;
detailed reports/logs are workflow artifacts retained for 14 days.

The workflow leaves curated records and provider research untouched. If ontology
changes invalidate a record, it reports that drift for curation instead of fixing
the record automatically. A weekly job cannot cover terms added after its run:
new-term PRs still need to warm and commit their required entries. Moving more
CI checks fully offline remains separate work tracked in #5731.
