# TZMP1 (A0A1B0GUW7) notes

## 2026-10-03 review session (claude-code, MICROPROTEINS Tier 2)

### Identity and locus
- 55-aa single-pass (predicted, TM 11-31) microprotein; former names SMIM27, C9orf133,
  TOPORS-AS1 (UniProt). Encoded on its own HGNC locus (HGNC:31420) antisense to TOPORS, so
  folder convention is the plain symbol (not a HOST__ACC alt-ORF folder).
- Locus overlap: [PMID:41270742 "the SMIM27 transcript is antisense to and partially overlapping with the TOPORS gene, such that start codon nucleotides are shared between the two open reading frames"]
- First shown to be translated in the Chen et al. ribosome-profiling/CRISPR study:
  [PMID:32139545 "the 55 aa peptide encoded on TOPORS-AS1"] ... "also form functional
  complexes consistent with their cellular localization" (supplementary figures only; no
  function assigned).

### Primary functional paper: Sun et al. 2025/2026 Dev Cell (PMID:41270742, full text cached)
- Hit in genome-wide microscopy-based CRISPR ciliation screen in RPE1 cells.
- KO + rescue: [PMID:41270742 "SMIM27 KO cells exhibited a severe loss of cilia labeled by Arl13b or polyglutamylated tubulin, and these defects were fully rescued by an sgRNA-resistant SMIM27-2xMyc transgene"]
  sgRNAs target exon 2, not overlapping TOPORS, so the phenotype is not a TOPORS artefact.
- Localization (tagged, rescue-validated transgene; expansion microscopy):
  [PMID:41270742 "we found that SMIM27 localizes at the transition zone, just distal to transition zone protein FAM92A and centriolar distal appendage protein CEP164"]
- AP-MS co-purification: [PMID:41270742 "mass spectrometry of proteins co-purifying with SMIM27-HRV3C-2xMyc revealed many components of the MKS protein complex"]
  -> authors: [PMID:41270742 "Thus, SMIM27 is a transition zone microprotein component of the MKS complex, and we propose the revised name TZMP1."]
- Stage of action: ciliary vesicle forms, CP110 removed, IFT recruited; [PMID:41270742 "Thus, the ciliary vesicle can likely form in the absence of TZMP1, but ciliary membrane growth and axoneme extension fail to occur."]
- Hierarchy: FAM92A, MKS1, TCTN1 still at TZ in TZMP1 KO; TMEM67 KO loses TZMP1 from TZ ->
  [PMID:41270742 "TZMP1 is required for cilium assembly subsequent to initial steps of ciliogenesis and has a relatively downstream role in the hierarchy of MKS module proteins"]
- Conservation: mouse NIH-3T3 Smim27 KO impaired ciliogenesis (milder). Xenopus tropicalis
  morphants: reduced MCC cilia (rescued by human SMIM27), impaired beating, LR patterning
  defects (dand5/pitx2c). [PMID:41270742 "smim27/tzmp1 is required for ciliogenesis, ciliary motility, and cilia-dependent tissue patterning in X. tropicalis"]
  These are ortholog data; not used for human GO process terms beyond cilium assembly.
- Absent in chicken and C. elegans; vertebrate-restricted.

### Other literature
- PubMed search (TZMP1 OR SMIM27 OR C9orf133 OR TOPORS-AS1) returns 3 PMIDs: 41270742,
  33820921, 29992774. PMID:33820921 (ovarian cancer) treats TOPORS-AS1 as an lncRNA acting with
  hnRNPA2B1 on Wnt/beta-catenin signalling [PMID:33820921 "inhibition of β-catenin by TOPORS-AS1
  required a RNA binding protein, hnRNPA2B1"]; this is an RNA-level claim and says nothing about
  the peptide. PMID:29992774 is a gastric-cancer lncRNA co-expression analysis (not fetched;
  not relevant to protein function).

### GOA review
- GO:0035869 ciliary transition zone (IMP, PMID:41270742): correct term; evidence code is odd
  (the localization is direct imaging, i.e. IDA) but the assertion is sound. ACCEPT.
- GO:0060170 ciliary membrane (IEA SubCell): consistent - predicted single-pass TM protein at
  the TZ, the membrane domain of which is part of the ciliary membrane. ACCEPT (TZ is the more
  precise location; membrane topology is predicted only).
- GO:0060271 cilium assembly (IMP): KO/rescue in RPE1. Participation test: as a TZ/MKS module
  component it contributes structure on which ciliary membrane growth depends (same shape as
  other MKS components). ACCEPT.

### Comparator check (QuickGO, 2026-10-03)
TMEM67, MKS1, CEP290, TCTN1, TMEM231, B9D1 all carry GO:0060271 cilium assembly and GO:0035869
ciliary transition zone; TMEM67/TMEM231 also GO:0060170 ciliary membrane; all six carry
GO:0036038 MKS complex (part_of; mostly IBA/ISS/NAS/IEA). TZMP1 matches comparators on the three
existing terms; the only comparator term it lacks is MKS complex.

### NEW
- GO:0036038 MKS complex (part_of), IDA via AP-MS co-purification of MKS1, B9D1/2, TCTN1/2/3,
  TMEM231, TMEM17, CC2D2A plus TMEM67-dependent TZ localization. Evidence is co-purification
  (not reconstitution), so moderate confidence; but it is the authors' explicit conclusion and
  UniProt SUBUNIT line.

### MF
No GO MF fits; no activity measured. Do not use protein binding.
