# MESK2 (CG15669, FBgn0043070) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

No ProtNLM2 file or prediction-evidence folder was opened; this review uses only GOA/UniProt,
PANTHER/PAINT, the cached literature and new sequence analysis.

### Identity of the benchmark accession

- Benchmark accession Q8T0V2 (TrEMBL, 447 aa; cDNAs GH02495/GH02835) is sequence-identical to
  A4UZR7, the reference-proteome (UP000000803) record for MESK2 isoforms A/E/F
  (RefSeq NP_726076.1, NP_995912.1, NP_995913.1). It is a full-length alternative isoform, not a
  fragment or a defective gene model [file:DROME/MESK2/MESK2-bioinformatics/RESULTS-rereview.md
  "Q8T0V2 == A4UZR7 (sequence identical): True"].
- UniProt has no Swiss-Prot entry for MESK2. The gene-centric canonical in UP000000803 is Q7KVN0
  (isoform I, 485 aa), sequence-identical to the cDNA record Q9GU50; QuickGO (queried 2026-10-21)
  places the gene's GO rows on these two accessions (IBA cytoplasm and IBA signal transduction on
  Q9GU50 from PAINT node PTN000867215; HDA serine hydrolase activity on Q7KVN0 from
  PMID:33827210). Q8T0V2 itself has no GOA rows, so `existing_annotations` is empty.
- Q8T0V2 residues 83-420 are identical to Q7KVN0 residues 1-338 and contain the whole Ndr
  (PF03096) alpha/beta-hydrolase-fold domain. Q8T0V2 adds an 82-residue N-terminal extension
  (MobiDB-lite disorder at 1-27 and 67-87) and a 27-residue isoform-specific C-terminus; isoform I
  instead has a 147-residue polar/Gly-rich C-terminal tail. No domain is missing from Q8T0V2.

### Evolutionary placement

- PANTHER PTHR11034 (N-MYC DOWNSTREAM REGULATED); subfamily PTHR11034:SF56 ("GH09802P"), whose
  members include MESK2, worm Y48G10A.3, Dictyostelium DDB_G0270324 and Arabidopsis NDL1. The
  human NDRG1-4 proteins sit in separate subfamilies SF18/SF17/SF20/SF21. DIOPT lists all four
  human NDRGs as orthologs, NDRG3 best (14/14 methods). So MESK2 is the single fly
  representative of the animal NDRG clade but is not in any human NDRG subfamily; paralog-specific
  NDRG1-4 functions should not be transferred.
- PAINT: PTN000867215 (taxon 6072, Eumetazoa) carries IBD cytoplasm (seeded by NDRG1-4 from
  human, mouse and rat) and IBD signal transduction (seeded only by human NDRG1). A second node,
  PTN002592750 (Euteleostomi), carries positive regulation of ERK1/ERK2 cascade (seed NDRG4) and
  is deliberately not inherited by fly MESK2. That omission is consistent with the fly evidence
  being a misexpression genetic interaction only.
- Family review interpro/panther/PTHR11034/PTHR11034-review.yaml (functional_coherence UNKNOWN)
  agrees: NDRG2 structures lack the catalytic triad, and MESK2 is not assigned NDRG2 functions.
  No disagreement on subfamily placement; the family review asserts no subfamily for MESK2.

### Catalytic residues

- At the nucleophile-elbow position MESK2 has Gly (Q8T0V2 G234, Q7KVN0 G152) in IGFGVGAGANI,
  matching Gly146 of human NDRG2 (Gly132 in the 357-aa isoform numbering of PMID:21247902)
  [file:DROME/MESK2/MESK2-bioinformatics/RESULTS-rereview.md "hNDRG2 146G -> Q8T0V2 (234, 'G')"].
  NDRG2 crystal structures show "the absence of the classical catalytic triad, Ser-His-Asp"
  [PMID:21247902]. MESK2 thus shares the noncatalytic NDRG configuration.
- The gene-level HDA "serine hydrolase activity" (Kumar et al. 2021, PMID:33827210) comes from
  fluorophosphonate activity-based protein profiling. Only the abstract is cached. A protein
  without a serine nucleophile at the canonical elbow is an unexpected FP-probe target; the
  enrichment may reflect a non-canonical reactive residue or co-enrichment. This row is on
  Q7KVN0, not on Q8T0V2. It should be assessed in the canonical review (UNDECIDED unless the
  full text shows probe-dependent, competable labelling of MESK2 peptides). It is not used as a
  core function here.

### Biology from the literature

- Huang & Rubin 2000 (PMID:11063696): MESK2 was recovered in a misexpression screen as a gene that
  modulates RAS1/KSR signalling in the eye; the abstract states these genes "may represent new
  components of the RAS pathway or components of other signaling pathways". That is
  overexpression-only genetic interaction, so no Ras-pathway process annotation is proposed.
- You et al. 2018 (PMID:29487148): "glial knockdown of MESK2 using either of two different RNAi
  transgenes also decreased rhythmicity"; MESK2 RNA showed only a nonsignificant decrease after
  miR-274 overexpression. This is an organismal behavioural phenotype from RNAi; under the
  CLAUDE.md participation rule it does not justify a circadian-process annotation.
- Molnar et al. 2006 (PMID:16980395): a wing gain-of-function insertion associated with
  CG15669/Mesk2 (screen-level only, per the deep-research summary; abstract does not name MESK2).
- FlyBase: many recessive lethal insertion alleles (l(2)01467 and others), so the gene is
  essential, but no molecular function is established.

### Decisions

- No existing annotations on Q8T0V2.
- One NEW row: cytoplasm (IBA, GO_REF:0000033), because the PAINT IBD at PTN000867215 applies to
  every full-length MESK2 product and GOA propagates it only to Q9GU50. The signal transduction
  IBD (seeded only by NDRG1) is not added for this record: it is very broad and the fly evidence
  for Ras modulation is misexpression-only; it should be judged on the canonical record.
  Ras/circadian/wing evidence is genetic and phenotypic only, so no process term is proposed.
- Core function: one entry for an NDRG-family noncatalytic alpha/beta-hydrolase-fold protein
  of unknown molecular activity, with cytoplasm as its location (PAINT IBD at Eumetazoa).
- Relative to review next: the canonical product of the same gene, Q7KVN0 (= Q9GU50), which
  carries the gene's GOA rows and has no review. Suggested folder genes/DROME/MESK2__Q7KVN0
  (genes/DROME/MESK2 is keyed to Q8T0V2).
- Modules: no module in modules/ covers NDRG proteins or MESK2.
