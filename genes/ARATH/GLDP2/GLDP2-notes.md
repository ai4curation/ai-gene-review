# GLDP2 (At2g26080, UniProt O80988) - curation notes

**Deep research could not be run** in this environment (no provider API keys). These notes
are a manual literature summary built only from cached publications (`publications/PMID_*.md`)
and the UniProt record (`GLDP2-uniprot.txt`). No `-deep-research-*.md` file exists for this gene.

## Identity

- Glycine dehydrogenase (decarboxylating) 2, mitochondrial; second P protein of the glycine
  decarboxylase complex (GDC). EC 1.4.4.2, PLP-dependent, GcvP family (PANTHER PTHR11773:SF1).
- Paralog of GLDP1 (At4g33010); 91% identical precursors [PMID:17496108 "A sequence comparison revealed
  91% sequence identity for the two predicted mitochondrial precursor P proteins."].

## Molecular function

- P-protein reaction (glycine decarboxylation with transfer of the aminomethyl group to lipoyl-H
  protein) [PMID:22303256 "P-protein (EC 1.4.4.2) is a pyridoxal-5-phosphate-containing homodimer,
  that catalyzes the actual glycine decarboxylation reaction"].
- GLDP2 is catalytically active but weaker than GLDP1 [PMID:33506579 "GLDP2, a paralog of GLDP1 with
  weaker catalytic activity"]; GLDP2 (not GLDP1) is targeted for degradation by the F-box protein
  InLYP1 [PMID:33506579 "could mediate the degradation of GLDP2 but not GLDP1"] (abstract only).

## Complex and location

- Part of the leaf GDC at ~1/4 the level of GLDP1 [PMID:32311173 "The Arabidopsis GDC contains four
  times more of the isoforms GCS-P1 and GCS-L1 in comparison with GCS-P2 and GCS-L2"].
- Mitochondrion (UniProt, experimental PubMed:14671022); matrix ATP-affinity proteome
  [PMID:17137349, abstract only]; detected in mitochondria in the ICP55 study, with lower abundance in
  icp55 [PMID:25862457 "Gly decarboxylase P-protein2 (At2g26080 and At4g33010"].
- Vacuole, cytosol, chloroplast and chloroplast envelope HDA rows are bulk-proteomics detections that
  conflict with the mitochondrial transit peptide and matrix localization; treated as contaminants.

## Biological role

- Functionally redundant with GLDP1 [PMID:17496108 "The corresponding P proteins, AtGLDP1 and AtGLDP2,
  can more or less fully substitute each other under standard growth conditions."]. GLDP2 transcripts
  dominate in roots [PMID:17496108 "AtGLDP1 transcripts dominate in photosynthesizing organs while
  AtGLDP2 transcripts are more abundant in roots."]. gldp1 gldp2 double mutant is seedling lethal even
  at high CO2 [PMID:17496108 "the double mutant does not develop beyond the cotyledon stage"],
  showing GDC is required for one-carbon metabolism as well as photorespiration.
- Note: unlike GLDP1, GLDP2 has no IMP annotation in GOA, although the same paper characterised
  gldp2 alleles and the double mutant.

## Annotation decisions (summary)

- Core: GO:0004375 (MF), GO:0019464 (BP), mitochondrion. NEW: GO:0005960 glycine cleavage complex
  (PMID:32311173) and GO:0009853 photorespiration (PMID:17496108; same comparator check as GLDP1).
- ATP binding (HDA, ATP-affinity capture): over-annotated; GcvP has no nucleotide-binding domain
  and capture of abundant matrix proteins can be indirect.
- mRNA binding (RNA interactome capture): over-annotated.
