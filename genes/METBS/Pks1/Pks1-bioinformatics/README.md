# Pks1 Bioinformatics Audit

The generated PKS1 reports in this directory are retained as stale analysis
artifacts, not as curated evidence for `Pks1-ai-review.yaml`. They are retained
rather than deleted so future readers can see why this generated sidecar was
rejected instead of rediscovering unbannered copies of the same reports.

The 2026-10-10 audit found that the embedded `PKS1_SEQUENCE` was 2137 aa while
the cached UniProt record is 2148 aa and diverges by residue 40, so current
UniProt `ACT_SITE` and `MOD_RES` coordinates were indexed into the wrong
sequence. The failed residue checks are artifacts and do not impeach the
UniProt `MOD_RES` 1712/1830 evidence supporting the accepted GO:0031177
phosphopantetheine binding annotation.

The scripts also hand-enter homolog identity values rather than recompute them,
hard-code the evolutionary summary and selection claims, and recommend process
terms that were rejected or narrowed in the 2026-10-01 re-review.

Use the cached UniProt record and PMID:29958281 for curated support.
