# parS (PA1798, Q9I2U4) review notes

## Review session 2026-11-05 (PseudoCAP IBA-seed protocol, tier 2)

Fetched with `just fetch-gene PSEAE Q9I2U4 --alias parS` (symbol fetch hit
UniProt rate limits). Accession Q9I2U4 matches the worklist (rank 330).
Unreviewed TrEMBL entry, 428 aa. Checked against the existing review of its
cognate response regulator, `genes/PSEAE/parR` (same seed paper, same kind of
call). No deep-research provider was used.

### Identity

- Membrane sensor histidine kinase: Phobius TM helix 133-154, HAMP domain
  155-207, histidine kinase domain 215-428 (PROSITE PS50109) with HisKA
  (PF00512) and HATPase_c (PF02518); phosphohistidine site His218 (ProRule).
  PANTHER PTHR44936:SF10 (RstB-like).
- Cognate kinase of ParR (PA1799); parS and parR are adjacent.

### Literature

- Fernandez et al. 2010 (PMID:20547815; abstract only; the PubMed MCP returns
  no full text for PMC2916309): [PMID:20547815 "Here we describe the
  identification and characterization of a novel P. aeruginosa two-component
  regulator affecting polymyxin-adaptive resistance, ParR-ParS
  (PA1799-PA1798)."] [PMID:20547815 "This system was required for activation
  of the arnBCADTEF LPS modification operon in the presence of subinhibitory
  concentrations of polymyxin, colistin, or the bovine peptide indolicidin"].
  The abstract reports genetics and phenotypes, not a kinase or phosphotransfer
  assay.
- Wang et al. 2013 (PMID:24034668; full text cached): [PMID:24034668 "As is
  typical of TCST systems, the ParS/ParR system consists of a membrane-bound
  histidine sensor kinase (ParS) and a cytoplasmic response regulator
  (ParR)."] parS and parR mutants change the transcriptome in the same way:
  [PMID:24034668 "As shown in Figure 2, mutations in parS or parR caused
  similar changes in the PAO1 transcriptome at the mid log phase."]

### Clade check (cached PAINT IBD/leaf GAF; QuickGO 2026-11-05)

- PTN001293174 (GO:0000155 phosphorelay sensor kinase activity): seeds E. coli
  EnvZ P0AEJ4 (EcoCyc IDA PMID:2558046, PMID:2668953), P. aeruginosa PA5484
  KinB Q9HT87 (PseudoCAP IDA PMID:9218420) and ParS Q9I2U4 (this gene,
  PseudoCAP IMP). 30 leaf IBAs in 13 taxa: EnvZ, RstB, Shewanella PrrB,
  Xanthomonas and Bradyrhizobium RegS-type kinases, P. aeruginosa AmgS, BfmS,
  GtrS, PA1158, PA5484, plus Vibrio, Fusobacterium, Clostridium,
  Rhodopirellula and plant (Ricinus) members. A HisKA/HATPase sensor kinase
  clade; the term suits it.
- The plasma membrane IBD on the same node is seeded by EnvZ and RstB.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN001293174 | GO:0000155 phosphorelay sensor kinase activity | 3 | 30 (13 taxa) | GO:0000155, IMP, PMID:20547815 (PseudoCAP) | INDIRECT-PHENOTYPE | A molecular function asserted from a mutant phenotype: loss of parS abolishes peptide-induced arn expression and adaptive resistance; no kinase assay is described in the abstract. The term itself is almost certainly right (HisKA/HATPase domains with the conserved His218, cognate RR next door), so the row is kept and only the evidence code is questioned, at SUSPECTED, as for the parR GO:0000156 row. | E. coli EnvZ P0AEJ4 (IDA); P. aeruginosa KinB Q9HT87 (IDA) | Yes. Two seeds with direct kinase assays ground the node; no GO_CENTRAL defect. |

Defects filed: PSEUDOCAP WRONG_EVIDENCE_CODE (CHECK, SUSPECTED) on the
GO:0000155 IMP row, mirroring the parR defect from the same paper.

## Decisions summary

- ACCEPT: phosphorelay sensor kinase activity (IBA, IEA, IMP); phosphorelay
  signal transduction system (IEA); plasma membrane (IBA, IEA).
- TOO_GENERAL: protein histidine kinase activity, kinase activity, transferase
  activity, transferase activity transferring phosphorus-containing groups,
  signal transduction, membrane (all IEA; each entailed by an accepted term).
