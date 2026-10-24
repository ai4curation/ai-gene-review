# cbh1 notes

Identity: cbh1, UniProt O14423; current PomBase systematic identifier is recorded in the benchmark cohort. The UniProt sequence is the reviewed current record, whereas the source XML uses placeholder taxonomy and sequence fields. Those placeholders are not biological evidence.

## ProtNLM source provenance

Source: PRE-RELEASE post-processed-2026_02_28k.xml. The exact entry is in `cbh1-protnlm-source.xml`. No entry belongs to the published 26,856-record pilot list. Current API availability does not change the original source version.

The XML evidence keys, model scores, string-match hydration metadata and alignment accessions/scores are retained verbatim in that source file. Assessments use current sequence features and primary sources; annotation overlap and ARBA output do not independently validate a prediction.

## Biological evidence and interpretation

LSP: Purified fission-yeast Cbh1 directly binds centromeric K-type repeat DNA and was characterized by DNA-binding and footprinting assays. Its in vivo centromeric-chromatin association was independently examined. These are direct target observations supporting nucleic acid binding without relying on automated keyword transfer. The target already has the more precise experimental centromeric DNA-binding annotation GO:0019237, so the broad prediction is correct but less precise.

[PMID:9237993 "Cbh protein specifically interacts in vitro with the K-type repeat DNA, which is essential for centromere function."]

[PMID:10733588 "In vivo, epitope-tagged Cbhp associated with centromeric K repeat chromatin, as well as with noncentromeric regions."]


## Research-provider audit

The Falcon report was read alongside its cited primary studies and the current sequence/GOA evidence. Its negative literature search is not evidence that a curated target-specific observation does not exist. 

CENP-B family retrotransposon surveillance is supported by [PMID:18094683 "CENP-B homologues of S. pombe localize at and recruit histone deacetylases to silence Tf2 retrotransposons."]. The publisher preview identifies Figure 1 as genome-wide maps of Abp1 and Cbh1, confirming that Cbh1 is among the assayed family members. The broader description records this family role, without transferring every Abp1-specific recruitment mechanism to Cbh1. Later papers PMID:22907751 and PMID:26354768 were checked as additional leads; their cached abstracts emphasize Abp1, so detailed Cbh1-specific numerical effects in the generated report are not treated as independently verified.

QuickGO GO:0007059 was checked for the chromosome segregation process proposed in place of the biological-process ND root; the direct double-mutant evidence is [PMID:10733588 "The synergism between the two null mutations suggests that these proteins perform redundant functions in S. pombe chromosome segregation."].

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 output was not consulted for this section. I did not open the protnlm files or use them as evidence.

### Identity
O14423 (CBH1_SCHPO, SPAC9E9.10c) is the reviewed, canonical, full-length 514-aa product of cbh1. It is not an isoform, fragment or alternative gene model. It has the CENP-B-type HTH (PROSITE PS51253, residues 69-144), HTH_ABP1_N (PF18107) and the DDE_1 transposase-derived domain (PF03184). The only sequence annotation is a single conflict at residue 168.

### Phylogenetic placement
- PANTHER is PTHR19303:SF73 ("PROTEIN PDC2"). Its reviewed members are the three S. pombe CENP-B-like proteins (Abp1 P49777, Cbh1, Cbh2 O60108) plus S. cerevisiae and C. albicans Pdc2 (interpro/panther/PTHR19303/PTHR19303-entries.csv).
- Casola et al. 2008 found that the fission-yeast CENP-B-like proteins and mammalian CENP-B were domesticated independently from different pogo transposases. They also found that Pdc2 is not orthologous to them [PMID:17940212 "Thus, the Pdc2 orthologous gene cluster appears to be derived from yet another source of pogo -like transposase than the S. pombe CENP-B-like proteins."]. The SF73 grouping with Pdc2 therefore reflects similarity, not orthology, and I transfer no Pdc2-specific function (pyruvate decarboxylase gene regulation).
- In the IBA rows, PTN002712198 gives DNA binding (donors cbh1 itself, abp1 and PDC2) and nucleus (donors CENPB, Cenpb, TIGD6 and POGK). Both are generic family properties and are consistent with the direct data. PAINT did not propagate any centromere-specific term from the human CENP-B donors. I treat that as deliberate, which fits the convergent-domestication finding.
- Closest experimentally characterized relative by placement: the same-subfamily paralog Abp1 (P49777). It has no review in the repo.

### Literature checked (newly cached)
- PMID:12130537 (Nakagawa 2002): "In the absence of Abp1 or Cbh1, the centromeric association of Swi6 is diminished, resulting in a decrease in silencing of the region."
- PMID:11238404 (Irelan 2001): cbh1 abp1 double mutants are hypersensitive to a microtubule-destabilizing drug.
- PMID:21151105 (Zaratiegui 2011, full text): Cbh1 ChIP-seq at Tf2 and solo LTRs with Abp1 and Sap1. Abp1 is said to recruit Cbh1 to the LTRs. Double mutants accumulate Sap1-dependent DNA breaks.
- PMID:22907751 and PMID:26354768: the abstracts concern Abp1. The Falcon report's Cbh1-specific meiotic recombination numbers are not visible in the cache, so I do not use them.
- PMID:12130539 was cached by mistake while I was looking for Nakagawa 2002. It is an unrelated cyclin D paper and is not cited.

### Changes from the previous review
- GO:0000775 (IEA): ACCEPT changed to MODIFY → GO:0000779, the more specific term the gene already carries by IDA.
- ND biological_process: MODIFY → chromosome segregation changed to UNDECIDED. PomBase curated PMID:10733588 for both Cbh1 and Abp1 and gave neither a chromosome segregation annotation. Abp1, the dominant paralog, also lacks any centromeric heterochromatin formation term (checked in QuickGO). The evidence is mostly redundant-pair necessity. I raise this as a question for PomBase rather than asserting it.
- MF broad terms: MODIFY now lists both GO:0019237 and GO:1990837 (sequence-specific dsDNA binding), so that ARS3002 and LTR binding are covered.
- Added a second core function (sequence-specific dsDNA binding at non-centromeric chromatin) and removed directly_involved_in chromosome segregation from the core function.
- Added propagation_review to the DNA-binding IBA row.
- I rewrote the description to cover the domain architecture, the convergent-domestication origin, the absence of any demonstrated catalysis, and redundancy with Abp1.
- PMID:18094683 is kept in references but is no longer cited as support, because the abstract describes the CENP-B homologues collectively.
