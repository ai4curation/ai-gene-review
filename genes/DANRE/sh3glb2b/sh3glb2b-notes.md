# sh3glb2b notes

## Setup and provenance

- Fetched with `just fetch-gene` on A0A8M9Q303 (TrEMBL, RefSeq XP_021331719.1 "Endophilin-B2b
  isoform X1", 421 aa), the sh3glb2b accession with the most GOA rows (5: 4 IBA, 1 IEA; no PMID
  rows). The gene has 11 UniProt entries for RefSeq isoforms (e.g. Q802U5 / NP_957413.1, 373 aa);
  each other entry holds only 1 GOA row and none has experimental rows (checked with
  `projects/DANRE_DUPLICATION/scripts/accession_audit.py`, terminal output only). ZFIN
  ZDB-GENE-040426-833; Ensembl ENSDARG00000035470, chromosome 5 (plus an alternate-contig model
  ENSDARG00000109833).
- **Deep research unavailable**: Edison returned 402 Payment Required and the OpenAI key is
  invalid, so no `-deep-research-*.md` file exists. Literature searched by hand in Europe PMC
  (`sh3glb2a`, `sh3glb2b`, `zebrafish AND (sh3glb2 OR "endophilin B2")`, and mammalian
  endophilin-B2 searches). No zebrafish paper studies either copy.
- DANRE_DUPLICATION batch 4 (random draw, seed 20260928); paralog sh3glb2a. Compara duplication
  node Osteoglossocephalai; PANTHER call TGD_tree.

## Zebrafish data

- Only expression: ZFIN curated wild-type in situ records (high-throughput screen,
  ZDB-PUB-040907-1) give sh3glb2b in central nervous system and eye/lens from segmentation
  to hatching stages, and sh3glb2a as whole-organism (ubiquitous-type) signal. See
  `sh3glb2b-bioinformatics/RESULTS.md`.

## Mammalian endophilin-B2 (SH3GLB2)

- Identified as an SH3GLB1 partner; SH3GLB proteins form homo/heterodimers through a
  coiled-coil core and are cytoplasmic
  [PMID:11161816 "Reversing prey to bait in the yeast screen, a second protein, SH3GLB2, of 395 amino acids showing 65% identity to SH3GLB1 was identified as an interacting partner of SH3GLB1."]
  [PMID:11161816 "Furthermore, SH3GLB members colocalize to the cytoplasmic compartment of the cell together with Bax and are excluded from the nucleus."].
- N-BAR + SH3 architecture; mouse knockout viable; endosome maturation defects in cells
  [PMID:28455444 "The endophilin B family of proteins contains an N-terminal Bin/amphiphysin/Rvs (N-BAR) domain that induces membrane curvature to regulate intracellular membrane dynamics."]
  [PMID:28455444 "In this study, we used genetic approaches that revealed that endophilin B2 is not required for embryonic development in vivo but that endophilin B2 deficiency impairs endosomal trafficking in vitro, as evidenced by suppressed endosome acidification, EGFR degradation, autophagic flux, and influenza A viral RNA nuclear entry and replication."]
  [PMID:28455444 "Mechanistically, although the loss of endophilin B2 did not affect endocytic internalization and lysosomal function, endophilin B2 appeared to regulate the trafficking of endocytic vesicles and autophagosomes to late endosomes or lysosomes."]
  [PMID:28455444 "Interestingly, we found that the N-BAR domain of endophilin B2 is required to rescue EGFR degradation in endophilin B2-deficient cells, whereas the SH3 domain appears to be dispensable"].
- Mitophagy: heterodimer with endophilin-B1
  [PMID:27112121 "Here we report that EB2 plays an indispensable role in mitochondria sequestration and inner mitochondrial membrane (IMM) protein degradation during mitophagy."].

## IBA sources (sh3glb2b)

- endocytosis, membrane, membrane organization: node PTN009017136 (endophilin clade; donors
  include SH3GLB1 Q9Y371, mouse/rat endophilins, fly and worm endophilins).
- protein-macromolecule adaptor activity: node PTN009017043, a deeper node whose donors are
  human SORBS1 (Q9BX66) and two mouse genes; not an endophilin-specific assertion.
- sh3glb2a has none of these IBAs: every sh3glb2a UniProt entry is classified in PANTHER
  subfamily PTHR14167:SF68 "DREBRIN-LIKE PROTEIN-RELATED", while sh3glb2b is in SF106
  "ENDOPHILIN-B2 ISOFORM X1" (UniProt DR lines). The PANTHER v19 pair table used
  A0A8M6Z0F0 for sh3glb2a, which no longer resolves in UniProtKB (HTTP 404, 2026-09-28).

## Pair analysis

See `sh3glb2b-bioinformatics/RESULTS.md`.
