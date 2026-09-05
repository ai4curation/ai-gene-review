# Refreshing GOA source records

`just fetch-gene ORGANISM GENE --force` and `just seed-goa ORGANISM GENE`
preserve distinct WITH/FROM sources in `supporting_entities`. They retain an
existing review while backfilling its missing source metadata and create PENDING
rows for additional sources. Source ordering is deterministic.

Legacy rows without source metadata remain valid, including historically collapsed
rows. Validation compatibility does not imply that seeding is unnecessary:
`uv run ai-gene-review seed-goa PATH --dry-run` previews source expansion and
metadata backfills without changing the input.

When seeding adds pending rows, it recomputes status using the shared status
rules. A previously finished review with new pending work becomes `IN_PROGRESS`;
a review containing only pending work is `INITIALIZED`. Metadata-only backfills
do not change status. After completing curation and validation, check status with
`uv run ai-gene-review update-status PATH --verbose`. That helper fills a missing
status but only reports an existing mismatch, which the curator must reconcile.

Older reviews also combined multiple source lists into one `supporting_entities`
list. Such a row remains valid when it is exactly the union of complete GOA
source lists for the same term, evidence, reference, and polarity. Unsupported
IDs and truncated source groups still fail. Only the represented source rows
are covered; other GOA sources still need review records. Seeding preserves the
combined historical review and adds distinct source rows as PENDING, without
transferring its judgment to each source.

Expansion temporarily leaves the combined row alongside its new source rows.
After assessing every new row, preserve the combined historical rationale and
its source list in the gene notes, then remove the combined annotation row to
avoid counting the same evidence twice. Do not mark it `retired`: its sources
have not disappeared. This cleanup is a curator decision; the seeder neither
copies the old judgment to every source nor deletes the historical row.

## When a source changes

An explicitly recorded source that no longer occurs in refreshed GOA fails source
validation. A new donor or PAINT node can change the evidence behind an assertion;
the old judgment must not automatically transfer to the new source.

1. Refresh through `just fetch-gene ORGANISM GENE --force`. The new source is
   seeded as a PENDING annotation. The old record and its review are preserved.
2. Compare the old and current source evidence. If the old source has been
   withdrawn or replaced, set `retired: true` on its annotation record. Retain its
   original source and review, and explain the retirement in the gene notes.
   Do not delete the historical record or guess an equivalent replacement node.
3. Review the new record against its actual evidence, then run
   `just validate ORGANISM GENE`.

Retirement records disappearance from the current annotation snapshot; it is not
a biological REMOVE judgment. Retired rows are excluded from current GOA matching
and seeding. If a retired source later reappears, the seeder creates a new PENDING
record rather than silently reactivating the historical judgment.

Use the same explicit retirement path when a complete term/evidence/reference
assertion disappears. The seeder does not automatically retire curator-authored
records, because a transient or incomplete upstream snapshot must not silently
withdraw them.

`fix-goa-retired` does not implement donor replacement: it matches at a broader
term/evidence level and skips several inference codes. Use the explicit review
and retirement steps above for a WITH/FROM change.
