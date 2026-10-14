# mapre3a notes

## Setup and provenance

- Fetched with `just fetch-gene` on A0A8M2B5B2 (TrEMBL, RefSeq XP_005158903.1, 273 aa), the
  mapre3a accession with the most GOA rows (10: 8 IBA, 2 IEA, none with a PMID). Other
  accessions for the gene (Q4V903 and A0ACM8Q7J9, RefSeq NP_001025298.1, 259 aa) carry only 2
  GOA rows each and no experimental rows (checked with
  `projects/DANRE_DUPLICATION/scripts/accession_audit.py`, printed to the terminal only).
  ZFIN ZDB-GENE-050913-88; Ensembl ENSDARG00000020231, chromosome 17.
- **Deep research unavailable**: Edison returned 402 Payment Required and the OpenAI key is
  invalid, so no `-deep-research-*.md` file exists. Literature was searched by hand in Europe
  PMC (`mapre3a`, `mapre3b`, `mapre3 AND zebrafish`, `zebrafish AND (EB3 OR mapre3)`, and
  EB3/MAPRE3 mammalian searches).
- DANRE_DUPLICATION batch 4 (random draw, seed 20260928); paralog mapre3b. Compara duplication
  node Clupeocephala; PANTHER call TGD_tree.

## Zebrafish literature

- No functional study of mapre3a (or mapre3b). Most zebrafish "EB3" hits use tagged mammalian
  EB3 (EB3-GFP) as a reporter of microtubule growth, which says nothing about the zebrafish genes.
- mapre3a appears only in a list of genes near hypermethylated CpGs after developmental
  glucocorticoid exposure
  [PMID:38989456 "In addition, we found hypermethylated CpGs in genomic regions associated with hdGC-primed genes, auts2a, mapre3a, igfbp5a, and pde4cb, which overlapped with identified GC-primed DEGs in in vitro dexamethasone-treated human neurons13 (Table S8)."].
  This is an expression/methylation observation, not function.
- ZFIN has no curated wild-type expression for mapre3a (ZFIN download checked by
  `mapre3a-bioinformatics/pair_analysis.py`).

## Mammalian EB3 (MAPRE3)

- Identified as an APCL-binding EB1 homolog, brain enriched
  [PMID:10644998 "The full-length cDNA of this novel homologue of EB1, named EB3, encoded a protein of 282 amino acids with 54% identity to EB1, and it was expressed preferentially in brain tissue on Northern blots."];
  on the cytoplasmic microtubule network
  [PMID:10644998 "Confocal microscopy demonstrated that exogenous EB3, like EB1, is associated with the cytoplasmic microtubule network."].
- Endogenous EB3 is enriched in brain extracts and marks growing microtubule ends in neurons
  [PMID:12684451 "Using EB3-GFP as a marker of microtubule growth in live cells, we subsequently analyze microtubule dynamics in neurons."].
- EB1 and EB3 (not EB2) promote persistent microtubule growth by suppressing catastrophes;
  plus-end tracking depends on the CH domain, anti-catastrophe activity needs dimerization
  [PMID:19255245 "Protein depletion and rescue experiments showed that EB1 and EB3, but not EB2, promote persistent microtubule growth by suppressing catastrophes."]
  [PMID:19255245 "Furthermore, we demonstrated in vitro and in cells that the EB plus-end tracking behavior depends on the calponin homology domain but does not require dimer formation."]
  [PMID:19255245 "EBs terminate with a flexible acidic tail containing the C-terminal EEY/F sequence, which is important for self-inhibition and binding to various partners"].

## IBA sources

- All 8 IBA rows come from PANTHER node PTN000065701 (the RP/EB family); donors include
  human MAPRE1 (Q15691) and MAPRE3 (Q9UPY8), yeast Bim1 (SGD:S000000818), fission yeast Mal3
  (PomBase:SPAC18G6.15), Arabidopsis EB1 genes, worm, fly and Dictyostelium EBs. This is a
  deep, very conserved node; both zebrafish copies are inside it.

## Pair analysis

See `mapre3a-bioinformatics/RESULTS.md` (protein identity, domain conservation, relative rate
with gar, expression from E-ERAD-475, Bgee and ZFIN, and synteny).
