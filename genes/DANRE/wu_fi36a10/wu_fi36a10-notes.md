# wu:fi36a10 (magi3a) notes

Current names: ZFIN `wu:fi36a10` (ZDB-GENE-030131-6139, chromosome 23); NCBI Gene 561689 `magi3a`
(aliases magi3, si:ch211-139k15.1, wu:fi36a10); Ensembl ENSDARG00000101869 (transcript magi3a-202).
UniProt A0A0R4IGT8 (TrEMBL, 1355 aa). Paralog: magi3b (directory `LOC564220`). Reviewed as part of
DANRE_DUPLICATION batch 3 (random sample).

## Deep research

Deep research was not available for this batch (Edison returned 402 Payment Required, and the
OpenAI key is invalid). I searched Europe PMC myself for "magi3a", "magi3b",
"magi3 AND zebrafish" and "wu:fi36a10"; the ZFIN name returns no hits.

## Literature (zebrafish)

- **America et al. 2022 (PMID:35649360)**, which calls this gene "magi3a". The paper's magi3a probe
  primers match wu:fi36a10 with 0 mismatches and magi3b with 7-8 mismatches
  (file:DANRE/wu_fi36a10/wu_fi36a10-bioinformatics/RESULTS.md).
  - [PMID:35649360 "the PDZ proteins membrane-associated guanylate kinase, WW, and PDZ domain containing 3 (Magi3a) and discs large MAGUK scaffold protein 4 (Dlg4a) bound to Gpr124 via its C-terminal ETTV motif."]
  - [PMID:35649360 "Targeting magi3a, magi3b, or dlg4b, but not dlg4a, partially impaired brain vascularization (Figures 4H and 4I), in agreement with the expression data."]
  - [PMID:35649360 "This lack of additive effect suggests that Dlg4b, Magi3a, and Magi3b act within the same pathway, in which they are individually required."]
  - [PMID:35649360 "Not unexpectedly, the ETTV motif of mouse and human GPR124 also interacted with Dlg4a and Magi3a in a yeast two-hybrid assay (Figure 5D)."]
- Passing mentions: magi3a was knocked down with no effect on FVIIa in an adult vivo-morpholino
  screen (PMID:33134781). In PMID:34784297 it appears only as a background mutation in the
  sa10150 line. Neither is informative for function.

## Sequence and expression (RESULTS.md)

- 58.2% identity to magi3b. This copy is closer to gar magi3 (63.5% vs 55.1%) and human MAGI3
  (54.5% vs 50.4%).
- The pseudo-GK domain has no Walker A motif, so the kinase/ATP/nucleotide IEA rows are removed.
- Bgee RNA-Seq calls are broad (22 anatomical entities, including gill, skin, intestine, liver, heart,
  muscle and kidney), similar to gar magi3. magi3b calls are a subset of these.

- Synteny: wu:fi36a10 keeps the gar magi3 neighbourhood (ptpn22, RSBN1). There is no double-conserved
  synteny with the magi3b region.

## Decisions

- Kinase / transferase / ATP / nucleotide binding: REMOVE. Nucleus IEA: KEEP_AS_NON_CORE.
- Location IBA/IEA and signal transduction IBA: ACCEPT.
- No NEW terms (see LOC564220-notes.md for why).
