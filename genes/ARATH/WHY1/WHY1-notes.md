# WHY1 (ARATH, Q9M9S3) review notes

## Setup
- `just fetch-gene ARATH WHY1` resolved Q9M9S3 (TAIR AT1G14410, GeneID 838003), 39 GOA rows (38 after merge).
- No deep-research key; manual synthesis in `WHY1-deep-research-manual.md`.
- Full text read: PMID:21911368 (key paper), PMID:20551348, PMID:24192350, PMID:19666500,
  PMID:23922267, PMID:28887381 (localization categories), PMID:32344669. Abstract only: PMID:14960277,
  PMID:15967440, PMID:17217467, PMID:19669906, PMID:35510566, PMID:16326926, PMID:27729395.

## Synthesis
WHY1 is a dual-located (chloroplast nucleoid + nucleus) Whirly ssDNA-binding tetramer.
Plastid: binds ssDNA non-specifically and protects against microhomology-mediated
rearrangements [PMID:20551348 "This pathway is negatively regulated by the single-stranded DNA (ssDNA) binding proteins from the Whirly family"].
Nucleus: telomeric ssDNA binding and negative regulation of telomerase
[PMID:17217467 "AtWHY1 specifically binds the single-stranded plant telomeric DNA sequences, but not double-stranded telomeric DNA."];
promoter binding and repression (KP1, WRKY53, with HDA15).

## Decisions worth expert attention
- GO:0005739 mitochondrion IBA: With/From is WHY2 (AT1G71260) only; WHY1 is plastid-targeted. REMOVE + source defect.
- GO:0005576 extracellular region HDA (PMID:28887381): the paper's compartment classes come from SUBAcon
  predictions; WHY1 has a chloroplast transit peptide. REMOVE + source defect.
- NOT|nucleus IDA (PMID:15967440): contradicted by later nuclear localization data
  (PMID:23269926, PMID:22154598, PMID:23922267). MARK_AS_OVER_ANNOTATED + source defect (CHECK).
- transcription corepressor activity (IDA PMID:35510566, abstract only): WHY1 itself binds DNA, so a
  DNA-binding repressor term might fit better; kept as non-core and raised as a question.
- NEW: GO:1901592 negative regulation of double-strand break repair via break-induced replication,
  per PMID:20551348 (WHY1 binds the resected ssDNA intermediates; it does part of the work).
