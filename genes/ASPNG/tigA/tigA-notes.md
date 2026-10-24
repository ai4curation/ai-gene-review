# tigA notes

## Re-review 2026-10-01 (GOA refresh)

- Two rows vanished from the current GOA snapshot and are marked `retired: true`
  (reviews kept):
  - GO:0016853 isomerase activity (IEA, GO_REF:0000043 keyword mapping) - keyword-derived
    row no longer emitted; the specific GO:0003756 protein disulfide isomerase activity
    IEA row remains.
  - GO:0051082 unfolded protein binding (IDA, PMID:16234854) - GO:0051082 is now
    obsolete (verified in the local GO build). The existing MODIFY to GO:0044183 protein
    folding chaperone stands as the substantive judgment; the replacement IDA
    GO:0006457 protein folding row from the same paper is present and reviewed.
- No PENDING rows. Added supporting text to two ACCEPT rows that lacked it.
