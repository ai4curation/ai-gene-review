# csr-1 — curation notes

## 2026-08-29 — gene-identity error corrected (UniProt accession)

This folder previously held data for **the wrong gene**. Recorded here rather than in the
review's `description`, which is for gene biology only.

**What was wrong.** `csr-1-uniprot.txt` and `csr-1-goa.tsv` contained UniProt **Q17370 /
NHR47_CAEEL** — `nhr-47`, a 579 aa nuclear hormone receptor — not CSR-1, the essential
Argonaute. The review's `id:` said `Q21992`, which is a third accession, now **deleted** from
UniProtKB (UniParc only). So the id, the fetched record and the prose all disagreed.

**Root cause.** `resolve_gene_to_uniprot` issues `(gene_exact:csr-1) AND (organism_id:6239)`
and prefers reviewed entries. `gene_exact:` matches gene *synonyms*, and Q17370 carries `csr-1`
as a stale synonym of `nhr-47`; the real gene is TrEMBL-only, so the reviewed-preference picked
the wrong protein. Filed as
[#2721](https://github.com/ai4curation/ai-gene-review/issues/2721); this gene's instance is
[#2720](https://github.com/ai4curation/ai-gene-review/issues/2720).

```
Entry    Entry Name     Reviewed     Gene Names                 Length
Q17370   NHR47_CAEEL    reviewed     nhr-47 csr-1 C24G6.4         579   <- what was fetched
H2KZD5   H2KZD5_CAEEL   unreviewed   csr-1 CELE_F20D12.1         1030   <- CSR-1A, now used
Q27GU1   Q27GU1_CAEEL   unreviewed   csr-1 CELE_F20D12.1          867   <- CSR-1B
```

**Accession chosen: H2KZD5.** 1030 aa, the longer isoform; `Q27GU1` is 867 aa and the two differ
by exactly the 163-residue N-terminal extension the literature assigns to CSR-1A. H2KZD5 also
carries the most GOA annotations (21 rows vs 9 for Q27GU1), so it is the practical anchor for
`existing_annotations`.

**What was done.**

- Re-fetched with `fetch-gene worm csr-1 --uniprot-id H2KZD5 --force`.
- `id:` Q21992 → H2KZD5; cohort list `projects/BIOREASON_COMPARISON/genes.csv` updated to match.
- Dropped the 16 nhr-47 annotations that a previous pass had marked `REMOVE`. They were never
  this gene's annotations, and `REMOVE` wrongly implies a curation judgement about CSR-1.
- Kept the 7 hand-added CSR-1 entries. Two of them (`GO:0016442` RISC complex, `GO:0043186`
  P granule) are present in the corrected GOA, so they became `ACCEPT` with the evidence and
  reference taken from the real GOA rows; the other five remain `NEW`.
- Deleted `csr-1-deep-research-falcon.md` — the whole report was researched against nhr-47 and
  would mislead any future reviewer. **A fresh deep-research run for CSR-1 is still needed.**
- Dropped 7 references orphaned by the removal (4 GO_REFs, the interactome PMID:19123269 and the
  TF-network PMID:23791784, both nhr-47 studies, and the falcon file reference).
- Status COMPLETE → IN_PROGRESS: the 20 newly seeded GOA annotations are `PENDING` and unreviewed.

**Effect on the model evaluations.** All three prediction sets in this folder were generated
from the NHR-47 sequence, confirmed by the BioReason RL export, which embeds that 579 aa sequence
verbatim and reasons entirely about zinc fingers and ligand-binding domains. ProTrek has been
re-run on the correct sequence. BioReason-SFT and GO-GPT are web-app exports and cannot be
regenerated here, so their rows are marked uncertain with `WRONG_INPUT_SEQUENCE` rather than
scored against CSR-1.

**Still open.** The 20 `PENDING` annotations need review, and a CSR-1 deep-research report needs
generating.
