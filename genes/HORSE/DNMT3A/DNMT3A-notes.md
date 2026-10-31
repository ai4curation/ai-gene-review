# DNMT3A: paired human–horse review notes

## Biological evidence

Human structural/biochemical evidence establishes DNA cytosine methylation, oligomerization and chromatin-guided targeting. PWWP and ADD domains have distinct targeting/regulatory roles. The protein-cysteine methyltransferase annotation has a real source: slow mouse catalytic-cysteine automethylation in DNA-free assays, suppressed by natural CpG substrate. It is non-core biochemical capacity, not an established second physiological function.

- [PMID:29414941: Structural basis for DNMT3A-mediated de novo DNA methylation.](https://pubmed.ncbi.nlm.nih.gov/29414941/) — full text cached.
- [PMID:25383530: Structural insight into autoinhibition and histone H3-induced activation of DNMT3A.](https://pubmed.ncbi.nlm.nih.gov/25383530/) — abstract cached; full-text availability must be checked separately.
- [PMID:30478443: Gain-of-function DNMT3A mutations cause microcephalic dwarfism and hypermethylation of Polycomb-regulated regions.](https://pubmed.ncbi.nlm.nih.gov/30478443/) — full text cached.
- [PMID:21481189: Auto-methylation of the mouse DNA-(cytosine C5)-methyltransferase Dnmt3a at its active site cysteine residue.](https://pubmed.ncbi.nlm.nih.gov/21481189/) — abstract cached; full-text availability must be checked separately.
- [PMID:12138111: A novel Dnmt3a isoform produced from an alternative promoter localizes to euchromatin and its expression correlates with active de novo methylation.](https://pubmed.ncbi.nlm.nih.gov/12138111/) — abstract cached; full-text availability must be checked separately.
- [PMID:38705424: Different expression patterns of DNA methyltransferases during horse testis development.](https://pubmed.ncbi.nlm.nih.gov/38705424/) — abstract cached; full-text availability must be checked separately.

## Exact horse model

The horse deletionhuman339–374overlaps the PWWP-domain end, while ADD and catalytic domains are retained in a97.3%-identical alignment. Broad nuclear localization and expression regulation are supported; normal locus targeting is not established. Horse testis data measure DNMT3A expression and immunofluorescence but do not identify the selected accession or establish every catalytic/regulatory claim.

The reproducible alignment, source paths and hashes are in [the paired comparison](../../HORSE/DNMT3A/DNMT3A-bioinformatics/RESULTS.md). Current UniProt sequences have not been proven identical to the original ProtNLM input sequences. Sequence anomalies are therefore recorded as model/transfer limitations, not as proven wrong-input pipeline errors.

## Evidence gaps

The horse Edison report identifies further equine expression leads but misses the testis paper retrieved independently. Do not treat its statement about absent horse localization evidence as exhaustive. Inspect the PWWP fold and transcript model; resolve specialized exposure/germline annotations from their original source experiments.

## Review scope and checks

Every seeded annotation receives a current assessment. UNDECIDED marks unresolved source-specific or biological evidence; these are initial reviews rather than a claim that every original experimental assay has been independently reproduced or verified. The human Edison report is retained as a research synthesis and source-finding aid; decisive YAML excerpts cite primary publications, source records or reproducible analysis. The validator advisory to cite the deep-research file is deliberately not satisfied by citing AI prose as biological proof.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

### Identity of the benchmark accession
- A0A9L0TK01 (873 aa, Ensembl ENSECAT00000098563, no gene name in UniProt) is an
  **exon-skipping alternative splice model** of horse DNMT3A. It is not a fragment.
  New analyses: `DNMT3A-bioinformatics/compare_isoforms_rereview.py`,
  `compare_exons_rereview.py`, summary `RESULTS-rereview.md`.
- It aligns end-to-end to human Q9Y6K1 (912 aa) at 97.3% identity. The only human
  residues missing are 1-3 and 339-374. Human 339-374 is one 108-nt in-frame exon:
  exon 9 of the horse sibling transcript ENSECAT00000027101 and of human
  ENST00000321117. The benchmark transcript has 22 exons and lacks that exon.
- The skipped exon lies in the PWWP region (human PWWP 292-350). The ADD domain
  (133/133) and catalytic domain (279/279) are complete. C710->C671 (PC motif),
  E756->E717, R836->R797 (TRD CpG contact) and R882->R843 (tetramer interface)
  are conserved.
- None of the seven horse DNMT3A UniProt models (A0A9L0TK01, A0A3Q2IAR2, F6Q5D1,
  A0A9L0RGD3, A0A9L0T4V1, A0A3Q2HNA6, A0A9L0TMC0) is a complete canonical product.
  Each lacks a different exon or terminus, and there is no reviewed horse entry.
  The canonical reference is therefore human Q9Y6K1, in the same PANTHER subfamily
  (PTHR23068:SF10).

### Key evidence for what does and does not transfer
- [PMID:15456878 "We show that the Dnmt3a and Dnmt3b proteins with their PWWP domains disrupted failed to accumulate in pericentric heterochromatin, resulting in their inability to methylate the major satellite repeats."]
- [PMID:15456878 "The observation that these mutant proteins efficiently methylate other genomic sequences indicates that the PWWP domains are not required for enzymatic activities but are involved in functional specialization."]
- So catalytic activity, CpG-island silencing and nuclear localization transfer to
  this product, because the NLS basic stretches flank the PWWP domain and are retained.
  Pericentric/centromeric heterochromatin, constitutive heterochromatin formation
  and probably the XY body do not transfer with confidence. Those rows are
  UNDECIDED rather than REMOVE, because the full-length gene product has these
  properties and the deletion is untested.

### Changes from the previous version
- Broad process rows (GO:0000122, GO:0010468, IBA GO:0045892) changed from ACCEPT to
  MODIFY -> GO:0044027, matching the human review.
- GO:0003677 changed from ACCEPT to MODIFY -> GO:0045322 unmethylated CpG binding.
  GO:0000978 changed from UNDECIDED to MODIFY -> GO:0003682 chromatin binding, since
  sequence specificity comes from partner TFs.
- GO:0005634 rows changed from ACCEPT to MODIFY -> chromatin + nucleoplasm.
  GO:0005654 kept ACCEPT, now with support from the PWWP-mutant localization data.
- GO:0042802 and GO:1902494 changed from ACCEPT to KEEP_AS_NON_CORE. GO:0061629 and
  GO:0141196 changed from UNDECIDED to KEEP_AS_NON_CORE.
- The heterochromatin rows are still UNDECIDED, now with direct PWWP-disruption
  evidence (PMID:15456878) instead of the H3K36me-reader variant paper.
- lncRNA rows (GO:0106222, GO:0031048) are still UNDECIDED. The human source RNA is
  the PTENpg1 pseudogene antisense RNA (PMID:23435381), which has not been shown
  to be conserved in horse.
- Added propagation_review metadata for the 4 IBA rows, along with core function
  locations chromatin/nucleoplasm, a suggested question and a suggested experiment.

### Relative, family and modules
- Relative: human DNMT3A Q9Y6K1, an ortholog in the same PANTHER subfamily SF10
  that also descends from PAINT nodes PTN000552637 and PTN001497036. It is reviewed
  at genes/human/DNMT3A/ (status DRAFT, all rows actioned).
- The family review interpro/panther/PTHR23068/PTHR23068-review.yaml lists
  A0A9L0TK01 under SF10 and agrees with UniProt. There is no placement
  disagreement. Its residue_sites anchor on human C710, which matches horse C671.
- No module under modules/ references DNMT3A or PTHR23068.
