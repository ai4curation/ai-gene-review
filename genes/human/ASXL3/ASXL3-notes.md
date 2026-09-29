# ASXL3 evidence notes

Human ASXL3 is UniProt Q9C0F0 (HGNC:29357), a 2248-residue nuclear chromatin regulator. The normal seed contains nine annotation assertions and two alternative products. Isoform 2 changes residues 294–317 and lacks residues 318–2248; its existence in the record does not establish that every function of full-length ASXL3 applies to this truncated product.

## Direct functional evidence

- [PMID:26739236](https://pmc.ncbi.nlm.nih.gov/articles/PMC4729829/): the original Results and Figure 1e legend explicitly include human ASXL3 DEUBAD in assays stimulating BAP1 against nucleosomal H2A. This supports a non-catalytic activator role; BAP1 performs hydrolysis. The detailed ASXL1 kinetic and structural experiments are not all ASXL3 experiments. Root inspected indexed primary Results/legend text; direct page access was challenged. The normal cache is pending through the existing source request.
- [PMID:32669118](https://link.springer.com/article/10.1186/s13073-020-00760-3): ASXL3 associates with BAP1 and directly binds BRD4 through a mapped motif. Human SCLC experiments combine two ASXL3 shRNAs, chromatin profiling and expression measurements, supporting enhancer-associated transcriptional coactivation. Root inspected the original abstract, cell/IP/construct/ChIP Methods and Results/legends for Figures 2–4. ChIP supports chromatin association, not isolated DNA binding. No claim that ASXL3 is universally the only ASXL paralog capable of binding BRD4 is intended; the 2020 paralog comparison is experiment-specific. Figure pixels and raw datasets were not reanalyzed.
- [PMID:25450400](https://pubmed.ncbi.nlm.nih.gov/25450400/): the normal cache and official abstract describe ASXL3-mediated repression of LXRα/TRβ, receptor interactions, recruitment to LXR-response elements, and reciprocal effects of ASXL3 overexpression/depletion on lipid accumulation in Hep3B cells. This is context-specific transcriptional repression, compatible with activation in another setting. LXR and TR are not PPAR receptors. Complete Methods and lipid-flux assays were not inspected, so the narrower biosynthesis wording needs careful treatment rather than rejection of the experimental annotation from an abstract alone.
- [PMID:26647312](https://pubmed.ncbi.nlm.nih.gov/26647312/): official indexed PubMed/PMC records verify the title, DOI and identifiers. Primary indexed Results describe BAP1 interaction with an N-terminal ASXL3 fragment and increased H2AK119ub1 in patient fibroblasts. The patient-cell observation connects ASXL3 dysfunction with chromatin regulation; it does not establish that ASXL3 is itself a hydrolase. Direct page access was challenged. A complete Methods/figure review is not claimed.

## Annotation boundaries

The DNA-binding IEA is sourced specifically to the ASX-like PHD domain (IPR026905), whereas the transcription-regulation IEA uses HARE-HTH (IPR007759). These domain mappings must not be interchanged. Chromatin occupancy alone does not demonstrate direct DNA binding by either isolated domain.

The PPAR-binding IBA is an ancestral PAINT assertion, not merely a similarity transfer from the listed ASXL2 donors. ASXL3's LXR/TR evidence does not prove or disprove PPAR recognition. Its clade placement and possible receptor-specific divergence require an independent assessment before changing the decision.

No ASXL3/Q9C0F0 entry was found in the local GO-CAM index on 2026-09-29. No new developmental or lipid-process annotation is proposed from phenotype or expression enrichment alone.

## Research and source provenance

The three normal seed files and the abstract-only PMID:25450400 cache were imported through the verified seed workflow. Two accompanying family exports remain quarantined. A single falcon request with the configured perplexity-lite fallback produced no research file. One normal request each for PMID:32669118 and PMID:26647312 failed with name-resolution errors and created no cache. These notes are manual research, not a provider-generated report.

Existing requests own PMID:26739236/40729547 and PMID:30664650/36180891; no duplicate requests were made. The canonical annotation YAML remains a pending seed until the source review and independent annotation consultation are complete.


## 2026-09-29 — recovered primary sources and final initial review

All nine original source assertions and both products are preserved. The review contains five ACCEPT, two KEEP_AS_NON_CORE and two UNDECIDED decisions, plus one NEW molecular function: deubiquitinase activator activity. One integrated core describes ASXL3 as a nuclear PR-DUB regulatory partner. No new biological process or intrinsic hydrolase activity is asserted.

PMID:26739236 explicitly tests human ASXL3 Q9C0F0 DEUBAD residues 244-360 despite its ASXL1-focused title. The bacterially expressed fragment activates separately produced BAP1 on nucleosomal H2A-K119ub (Figure 1e and protein-expression Methods). This is direct activator work; it is not an inference from disease necessity or complex membership. The fragment experiment does not assign activity independently to both full-length products. Complete figure pixels and kinetic supplements were not inspected.

The actual normal HTML cache for PMID:26647312 distinguishes reciprocal 293T co-IP of FLAG-BAP1 with human ASXL3 residues 1-484 from patient primary fibroblast phenotypes. The c.1448dupT fibroblasts showed reduced full-length protein, no detectable stable truncated product and approximately fivefold higher H2AK119ub. Selected dosage, interaction, chromatin and transcriptome Results plus cloning/co-IP Methods were read (root extraction paragraphs 24,26,28-30,32,42,43,48,53,55,59). Normal CASE_REPORT metadata is preserved. The patient perturbation is not an isolated ASXL3 enzyme assay.

Actual XML PMID:32669118 supports endogenous ASXL3/BAP1/BRD4 association in human NCI-H1963 SCLC, nuclear complex recovery, and chromatin recruitment. Purified recombinant ASXL3 BBM and BRD4 ET domains bind directly; deleting the 20-residue BBM disrupts BRD4 binding while sparing BAP1 binding. ASXL3 depletion reduces BRD4 and BAP1 chromatin occupancy and enhancer-associated transcription without lowering total BRD4 protein. Human endogenous assays, tagged HEK293T constructs and separate mouse experiments are distinguished. Cell-line/construct Methods and interaction/chromatin Results with Figures 2-4/6 legends were read (paragraphs 11,19,50-52,55,56,59,60,67,68); raw figure pixels and supplementary datasets were not inspected.

The PHD-associated DNA-binding IEA remains UNDECIDED: MBD5/6 association and chromatin occupancy do not test direct DNA recognition. The PPAR-binding IBA also remains UNDECIDED: LXRalpha/TRbeta are different receptors, and the PTN000339788 ancestral evidence has not been reconstructed. No negative assay or inference of weak evidence from donor count is invented. PMID:25450400 remains abstract-only; its Hep3B lipid accumulation and receptor repression findings support retaining the existing experimental lipid-process annotation as contextual.

PMID:36180891 supports ASXL PHD-dependent MBD5/6 association and complex stability. ASXL2/Asx histone-binding experiments in PMID:40729547 and ASXL1/2 deletion in ASXL3-negative HAP1 cells in PMID:30664650 are not recast as direct ASXL3 assays. Five literal source findings and a quoted NEW assertion anchor this synthesis. Availability of full text is recorded separately from the specific passages actually read.


## BRD4 adaptor evidence following PR 3543 review

The original PMID:32669118 Methods, Results and Figure 2-4 legends support a protein bridge separate from DEUBAD-mediated BAP1 activation. Human NCI-H1963 endogenous co-IP and HEK293T human ASXL3 constructs are distinguished from mouse KP3 experiments. E. coli-produced BBM and BRD4 ET fragments directly associate; deleting BBM selectively disrupts BRD4 association while retaining BAP1 association. Depletion-dependent enhancer occupancy is chromatin recruitment evidence, not direct DNA recognition. The exact selected source statement is:

> depletion of the 20 amino acids (ΔBBM) does not affect ASXL3/BAP1 interaction, but only completely abolished ASXL3/BRD4 interaction

Source: [PMID:32669118, original PMC article](https://pmc.ncbi.nlm.nih.gov/articles/PMC7362484/), interaction Results and Figure 2g; actual normal cache inspected. Cell-line, IP, RNA-interference, plasmid and ChIP Methods and the targeted Results/legends were read. No new inspection of figure pixels, raw data or complete supplementary tables is claimed.

GO:0030674 records the demonstrated BAP1-BRD4 bridge. GO:0140463 is a more specific chromatin-recruitment child; the broad bridge is selected for the directly tested protein-interface mechanism, with enhancer recruitment retained as context. This choice does not imply that the child requires direct DNA binding or is disproved. Only one adaptor term is proposed, avoiding parent/child duplication. GO:0140378 describes integral complex scaffolding; the proposed activity specifically connects a BRD4 partner with BAP1-associated ASXL3, rather than asserting an obligate structural requirement for intact PR-DUB. These definitions and relationships were checked in official AmiGO pages. The adaptor and deubiquitinase-activation functions are distinct molecular work; no new biological process is added.

The original nine source assertions and existing DEUBAD NEW annotation remain unchanged. DNA binding remains UNDECIDED: protein association and chromatin recruitment do not settle the source-domain DNA-recognition question. PPAR binding remains independently unresolved. The two UniProt alternative products remain intact; the shortened second product is explicitly a research question, not assigned the full-length assays. Negative ASXL1/2 co-IP results in this paper are experiment-specific, not a universal paralog exclusion. PMID:32669118 is marked VERIFIED after original evidence and official PMID/DOI/PMCID checks; the other four reference judgments are preserved rather than changing them solely on the reviewer's suggestion.
