# parR (PA1799) review notes

UniProt: Q9I2U3 (unreviewed, 235 aa), "Two-component response regulator, ParR".
Locus PA1799; cognate sensor kinase ParS is PA1798.

## What is established

- ParR-ParS is the two-component system that mediates adaptive resistance to
  polymyxin B, colistin and antimicrobial peptides
  [PMID:20547815 "Here we describe the identification and characterization of a novel
  P. aeruginosa two-component regulator affecting polymyxin-adaptive resistance,
  ParR-ParS (PA1799-PA1798)."]. The system is required for induction of the
  arnBCADTEF lipid A modification operon by subinhibitory peptide concentrations
  [PMID:20547815 "This system was required for activation of the arnBCADTEF LPS
  modification operon in the presence of subinhibitory concentrations of polymyxin,
  colistin, or the bovine peptide indolicidin, leading to increased resistance to
  various polycationic antibiotics, including aminoglycosides."].
- ParR is a cytoplasmic OmpR/PhoB-family response regulator with a REC receiver
  domain and a winged-helix DNA-binding domain (InterPro IPR001789, IPR001867,
  IPR039420 on Q9I2U3)
  [PMID:24034668 "As is typical of TCST systems, the ParS/ParR system consists of a
  membrane-bound histidine sensor kinase (ParS) and a cytoplasmic response regulator
  (ParR)."].
- The ParS/ParR regulon is large and condition-dependent: over 100 genes in the
  presence of antimicrobials, including mexEF-oprN, oprD, quorum-sensing
  regulators, and arnBCADTEF-ugd only when the inducing peptide is present
  [PMID:24034668 "Interestingly, quantitative reverse transcriptase polymerase chain
  reaction (qRT-PCR) analysis revealed that ParR-dependent genes such as
  arnBCADTEF-ugd, pmrB, pagL and PA1797 are not induced by ParR in the absence of
  indolicidin, suggesting that the ParS/ParR system regulates gene expression in an
  environment-dependent manner"],
  [PMID:24034668 "Interestingly, data from all three studies indicate that ParS/ParR
  are responsible for the repression of the oprD gene (basic amino acid and carbapenem
  permeable porin) (Additional file 4: Table S4, Additional file 6: Figure S3A)."].
  So ParR both activates and represses transcription.

## Notes on specific annotations

- `GO:0071073 positive regulation of phospholipid biosynthetic process` (IMP,
  PMID:20547815). This looks odd but is defensible: lipid A biosynthesis
  (GO:0009245) is, in GO, a descendant of GO:0008654 phospholipid biosynthetic
  process, and ParR positively regulates the arn operon that modifies lipid A.
  No "regulation of lipid A biosynthetic process" term exists (checked against
  go-basic, 2026-11-05), so the asserted term is the most specific regulation
  term available in that branch and the row is kept rather than modified. Raised
  as a `suggested_questions` entry instead.
- The cited paper reports genetics (mutants fail to induce arn; resistance
  phenotypes). Nothing in the cached abstract reports phosphotransfer to ParR or
  ParR-DNA binding, which is why the `GO:0000156` IMP row is judged
  INDIRECT-PHENOTYPE below. The claim itself is not in doubt: the protein is a
  canonical OmpR/PhoB response regulator.

## Literature search

Europe PMC and PubMed, 2026-11-05: `aeruginosa AND ParR AND ParS`,
`TITLE:"ParR" AND aeruginosa`, `aeruginosa AND (parR OR ParRS) AND mexXY`.
PMC2916309 (PMID:20547815) returns an abstract only through the PubMed MCP, so
the full text of the seed paper was not read. Cached and used: PMID:20547815,
PMID:24034668. Also seen but not cached: PMID:24994873 (colistin resistance in
parR-inactivated mutants) and a 2026 report on ParR promoter architecture with
no PMID yet in Europe PMC.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN000724188 | GO:0000156 phosphorelay response regulator activity | 10 | 475 (45 taxa) | GO:0000156, IMP, PMID:20547815 (PseudoCAP) | INDIRECT-PHENOTYPE | A molecular function asserted from a mutant phenotype: the paper shows that loss of parR abolishes peptide-induced arn expression and adaptive resistance, not that ParR accepts a phosphoryl group or acts as a response regulator in a biochemical assay. The claim is almost certainly right (receiver domain plus winged-helix DNA-binding domain, cognate kinase ParS next door), so the row is kept; only the evidence coding is questioned, and at SUSPECTED confidence because the full text of the seed paper could contain a phosphorylation experiment that the abstract does not mention. | E. coli ArcA (P0A9Q1), OmpR (P0AA16), CpxR (P0AE88), PhoP/PhoB-family members P30843 and P38684, Bacillus O07776, Streptococcus Q8DPL7 and Q8DN02, P36556 | Yes. The E. coli response regulators carry direct experimental evidence for this activity, so the node assertion does not depend on ParR. No `GO_CENTRAL` defect. |

Node-level consistency: `PTN000724188` also carries IBDs for GO:0006355,
GO:0000976, GO:0032993 and GO:0005829, and both parR and copR in this batch are
leaves of it. The node-level judgement for all of them is the same - a broad,
well-seeded OmpR/PhoB response-regulator node whose terms suit the clade - and
is recorded once in `genes/PSEAE/copR/copR-notes.md`, the gene in this batch with
in-organism transcriptional data (PMID:17449606, full text). No `GO_CENTRAL`
defect is filed from either gene.

PseudoCAP defects from this gene: one, `WRONG_EVIDENCE_CODE` (SUSPECTED) on the
GO:0000156 IMP row, asking whether the row should be an IC or ISS-style
inference rather than IMP.
