# sh3glb2a notes

## Setup and provenance

- Fetched with `just fetch-gene` on A0A8M1N8K5 (TrEMBL, RefSeq NP_001035087.2, 381 aa); 1 GOA
  row (cytoplasm, IEA, GO_REF:0000120).
- **Accession check.** All six UniProt entries for sh3glb2a (A0A8M6Z818, A0AB32TT96,
  A0A8M1N8K5, A0AB32TWL9, Q502S2, Q6TNQ7) hold exactly 1 GOA row and none holds experimental
  rows (`projects/DANRE_DUPLICATION/scripts/accession_audit.py`, terminal output only). The chosen
  entry carries the RefSeq reference protein (NP_), so the choice is sensible. The concern is
  not the accession but the PANTHER classification: every sh3glb2a entry is placed in
  PTHR14167:SF68 "DREBRIN-LIKE PROTEIN-RELATED" (UniProt DR lines), whereas sh3glb2b is in
  SF106 "ENDOPHILIN-B2 ISOFORM X1". That is why sh3glb2a has no IBA rows. The PANTHER v19 pair
  table lists A0A8M6Z0F0 for sh3glb2a; that accession no longer resolves in UniProtKB (HTTP
  404 on 2026-09-28), so it was presumably merged or deleted.
- ZFIN ZDB-GENE-061201-8; Ensembl ENSDARG00000008983, chromosome 8.
- **Deep research unavailable**: Edison returned 402 Payment Required and the OpenAI key is
  invalid, so no `-deep-research-*.md` file exists. Literature searched by hand in Europe PMC
  (`sh3glb2a`: 0 hits; `zebrafish AND (sh3glb2 OR "endophilin B2")`: no relevant hits).
- DANRE_DUPLICATION batch 4 (random draw, seed 20260928); paralog sh3glb2b.

## Evidence used

- Mammalian endophilin-B2 literature: see `genes/DANRE/sh3glb2b/sh3glb2b-notes.md`
  (PMID:11161816, PMID:27112121, PMID:28455444).
- Pair analysis: `genes/DANRE/sh3glb2b/sh3glb2b-bioinformatics/RESULTS.md`. sh3glb2a keeps the
  amphipathic helix (85% identical to human), BAR domain (77%) and SH3 domain (89%); it peaks at
  blastula (27-28 TPM) and is low (2-4 TPM) afterwards in whole embryos; adult Bgee calls are
  broad and all shared with sh3glb2b.

## Review decisions

- Cytoplasm (IEA): accepted.
- NEW membrane (ISS, from the pair analysis): proposed because the IBA that sh3glb2b receives
  is missing here only through the PANTHER subfamily split. Process terms were not proposed.
