# mapre3b notes

## Setup and provenance

- Fetched with `just fetch-gene` on A0A8M9Q0D6 (TrEMBL, RefSeq XP_021330664.2 /
  XP_021330665.2, 278 aa), the mapre3b accession with the most GOA rows (10: 8 IBA, 2 IEA,
  none with a PMID). Other accessions (Q6GMJ3 and A0A8M9Q5V0, RefSeq NP_001002170.1, 262 aa)
  carry 2 GOA rows each, none experimental (checked with
  `projects/DANRE_DUPLICATION/scripts/accession_audit.py`, terminal output only).
  ZFIN ZDB-GENE-040704-6 (synonyms wu:fj35g02, zgc:91952); Ensembl ENSDARG00000102878, chromosome 4.
- **Deep research unavailable**: Edison returned 402 Payment Required and the OpenAI key is
  invalid, so no `-deep-research-*.md` file exists. Literature searched by hand in Europe PMC
  (same searches as for mapre3a).
- DANRE_DUPLICATION batch 4 (random draw, seed 20260928); paralog mapre3a. Compara duplication
  node Clupeocephala; PANTHER call TGD_tree.

## Zebrafish literature

- No functional study. mapre3b is one of 394 genes selected as specific to young thrombocytes
  and knocked down in a screen
  [PMID:39939668 "This study employed a comprehensive screening approach through a piggyback knockdown strategy targeting 394 protein-encoding genes expressed explicitly in young thrombocytes."];
  mapre3b appears in the primer table but not among the eight hits
  [PMID:39939668 "This approach led us to identify eight candidate genes associated with thrombopoiesis, including spi1b, a transcription factor that potentially regulates thrombocyte development."].
  A negative result in a knockdown screen is weak evidence and I do not use it for GO.
- ZFIN has a single high-throughput in situ record (anatomy "unspecified", 1-cell to pec-fin).

## Mammalian EB3 and IBA sources

As in `genes/DANRE/mapre3a/mapre3a-notes.md` (PMID:10644998, PMID:12684451, PMID:19255245);
the eight IBA rows are identical to those on mapre3a (node PTN000065701), and all review calls
are the same on both copies.

## Pair analysis

See `genes/DANRE/mapre3a/mapre3a-bioinformatics/RESULTS.md`: 83.0% identity between the
reviewed accessions; all domains kept; no rate difference against gar; mapre3b maternal and
broadly expressed like gar MAPRE3, mapre3a zygotic and neural/retina/testis biased.
