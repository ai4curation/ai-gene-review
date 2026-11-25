# GDCST (At1g11860, UniProt O65396) - curation notes

**Deep research could not be run** in this environment (no provider API keys).
These notes are a manual literature summary built only from the cached
publications in `publications/`, the UniProt record (`GDCST-uniprot.txt`) and
PubMed searches. No `-deep-research-*.md` file exists for this gene.

## Identity

- UniProt O65396 (GCST_ARATH), "Aminomethyltransferase, mitochondrial", EC 2.1.2.10,
  AltName "Glycine cleavage system T protein"; gene GDCST, synonym GDT1, locus At1g11860.
- Predicted N-terminal mitochondrial transit peptide (residues 1-24, ECO:0000255).
- Family: GcvT family (InterPro IPR006223 GcvT; NCBIfam TIGR00528 gcvT;
  PANTHER PTHR43757:SF2 "AMINOMETHYLTRANSFERASE, MITOCHONDRIAL").
- Single-copy gene in Arabidopsis
  [PMID:22303256 "one gene for T-protein (At1g11860)"].

## Biochemical function

- T-protein is the aminomethyltransferase of the glycine cleavage system (GCS;
  glycine decarboxylase complex, GDC): it accepts the aminomethyl group carried on
  the lipoyl arm of H-protein, releases NH3, and transfers the methylene unit to
  tetrahydrofolate (THF) forming 5,10-methylene-THF
  [PMID:22303256 "The amino methylene group bound to the H-protein is further metabolized by the monomeric aminomethyltransferase T-protein (EC 2.1.2.10)"]
  [PMID:22303256 "During this reaction, NH 3 is released and a methylene group is transferred to tetrahydrofolate resulting in the formation of 5,10-methylene tetrahydrofolate (CH 2 -THF)"].
- UniProt catalytic activity: RHEA:16945 (aminomethyl-dihydrolipoyl-[protein] + THF =
  dihydrolipoyl-[protein] + 5,10-methylene-THF + NH4+); this is annotated by
  similarity (no Arabidopsis-specific kinetic data in the cache).
- The GDC is composed of four proteins, P, T, L and H (UniProt SUBUNIT).
  In pea the complex stoichiometry was 4P:27H:9T:2L
  [PMID:22303256 "For pea, a subunit stoichiometry of 4P:27H:9T:2L was observed"].

## Physiological role

- GDC + mitochondrial SHMT form the mitochondrial part of the photorespiratory C2
  cycle [PMID:22303256 "The combined reaction of glycine decarboxylase (GLD) and serine hydroxymethyltransferase (SHM) represents the mitochondrial part of the major photorespiratory pathway"].
- Timm et al. 2018 (abstract only in cache): T-protein is essential for
  photorespiration and one-carbon metabolism; knockout is lethal even in 1% CO2,
  whereas a knockdown with ~5% residual T-protein survives in air with moderate
  glycine accumulation; overexpression (up to 3x) has no effect on photosynthesis
  or growth; T-protein is in large excess over the other GCS proteins
  [PMID:28866761 "T-protein is the aminomethyltransferase of the glycine cleavage multienzyme system (GCS), also known as the glycine decarboxylase complex, and essential for photorespiration and one-carbon metabolism"]
  [PMID:28866761 "the knockout mutation was lethal even in the non-photorespiratory environment of air enriched to 1% CO2"]
  [PMID:28866761 "displayed only some minor changes, such as a moderate glycine accumulation in combination with somewhat delayed growth"].
- The lethality at high CO2 indicates the non-photorespiratory (one-carbon supply)
  role of GCS is essential; this matches GLDP1/GLDP2 double mutants (see the C2
  cycle module).
- T-protein knockdown (gldt1) has been used as a genetic background for
  photorespiration studies [PMID:38518065 "the glycine decarboxylase T-protein knockdown (gldt1) background"].

## Localization

- Mitochondrion (matrix enzyme; predicted transit peptide). Repeated detection in
  mitochondrial proteomes (PMID:18385124, PMID:25293756) and IDA (PMID:28866761,
  curator-assigned; full text not cached).
- Detections in chloroplast (PMID:18431481, PMID:20061580, PMID:12938931),
  cytosolic ribosome (PMID:15821981), apoplast (PMID:18538804) and extracellular
  region (PMID:28887381) proteomes are most consistent with carry-over of an
  abundant leaf mitochondrial protein. The chloroplast proteome authors themselves
  estimate many non-plastid contaminants
  [PMID:18431481 "from manual evaluation we estimate that 300–350 proteins likely represent false positive identifications and/or non-chloroplast contaminations"].
  The 80S ribosome study reports co-migrating non-ribosomal proteins
  [PMID:15821981 "we have identified a number of non-ribosomal proteins that co-migrate with the plant 80S ribosomes during gradient centrifugation"].

## Other annotations

- mRNA binding (IDA, PMID:32344669): from a leaf RNA interactome capture screen,
  which found many metabolic/photosynthetic proteins without canonical RBDs
  [PMID:32344669 "a large proportion of leaf RBPs lack known RNA-binding domains, suggesting unconventional modes of RNA binding"].
  Physiological relevance unknown.

## Curation decisions summary

- Core: GO:0004047 aminomethyltransferase activity; GO:0019464 glycine
  decarboxylation via glycine cleavage system; part of GO:0005960 glycine cleavage
  complex; located in mitochondrion.
- NEW: GO:0009853 photorespiration (IMP, PMID:28866761). T-protein catalyses a
  step of the photorespiratory glycine-to-serine conversion (participation test
  passed: it performs the aminomethyl transfer). Comparator check: the other
  C2-cycle enzymes reviewed in this repository (SHM1, GGAT1, AGT1, HPR, GLYK) carry
  GO:0009853 in GOA; the GDC subunits (GLDP1, GLDP2, GDCH, GDCST) do not, which
  looks like a curation gap rather than a convention, because the GDC subunits
  catalyse photorespiratory steps just like SHM1 does.
- Proteome-only non-mitochondrial locations marked as over-annotations.

## Module cross-check

- `modules/glycine_cleavage_system.yaml` T-protein role: GO:0004047, family
  PANTHER PTHR43757:SF2 (the same subfamily as GDCST in UniProt), process
  GO:0019464. Consistent with this review.
- `modules/photorespiration_c2_cycle.yaml` lists GDCST (O65396) as the
  Arabidopsis T protein. Consistent.
