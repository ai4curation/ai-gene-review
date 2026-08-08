# RORA review notes

## Review scope and evidence availability

This is a manual review of the 87 seeded human RORA GO annotations. Automated deep-research attempts with Falcon and Perplexity Lite had already failed, so this review uses the reviewed UniProt record, the GOA table, all locally cached GOA publications, full-text flags, and the human RORA neurodevelopmental genetics paper. No provider-named deep-research file was created.

Most GOA papers are available locally as abstracts only. Experimental annotations whose specific claim could not be checked from the abstract were not rejected. In particular, PMID:18658046 supports RORA-dependent HIF1A activation and endothelial capillary-tube formation, but its cached abstract does not mention VEGF production; GO:0010575 was therefore marked `UNDECIDED`, not removed.

## Core molecular mechanism

RORA is a monomeric nuclear receptor whose DNA-binding domain recognizes ROR response elements (ROREs). Isoform-sensitive target recognition is directly demonstrated: [PMID:7926749, "Binding site selection using in vitro-synthesized proteins reveals that the ROR alpha 1 and ROR alpha 2 isoforms bind DNA as monomers to hormone response elements composed of a 6-bp AT-rich sequence preceding a half-site core motif PuGGTCA (RORE)."]

RORA can activate and repress transcription in a promoter- and cell-dependent manner. [PMID:9328355, "Mutational analysis revealed that RORalpha contains both transcriptional activation and transcriptional repression domains, with the repression domain being more active in some cell types."] The same study connects repression-capable fragments to N-CoR and SMRT binding: [PMID:9328355, "The abilities of RORalpha polypeptides to repress transcription correlate with their abilities to interact with the nuclear receptor corepressors N-CoR and SMRT in vitro."]

Coactivator recruitment is a direct part of the receptor mechanism. GRIP-1 and PBP/MED1 were recovered using the RORA activation domain, and GRIP-1 was functionally validated: [PMID:10478845, "GRIP-1 functioned as a coactivator for the RORalpha both in yeast and in mammalian cells."] BAF60c provides another mechanistic bridge to chromatin remodeling: [PMID:14701856, "Both isoforms are enriched in the central nervous system and also modulate the transcriptional activity of retinoic acid-related orphan receptor alpha1."]

RORA is ligand-modulated rather than simply constitutively active. [PMID:19965867, "Here, we demonstrate that 7-oxygenated sterols function as high affinity ligands for both RORalpha and RORgamma by directly binding to their ligand-binding domains (K(i) approximately 20 nM), modulating coactivator binding, and suppressing the transcriptional activity of the receptors."] This supports oxysterol binding, ligand-modulated transcription-factor activity, and intracellular receptor signaling as central annotations.

## Contextual physiological outputs

The following are well-supported or conservatively transferred outputs of the core transcriptional mechanism, but they are not separate molecular activities and were generally classified `KEEP_AS_NON_CORE`:

- Circadian regulation: RIP140 is recruited to ROR sites in the BMAL1 promoter and coactivates RORA. [PMID:21628546, "RIP140 is recruited to retinoid-related orphan receptor (ROR) binding sites on the BMAL1 promoter, directly interacts with RORα, and increases transcription from the BMAL1 promoter in a RORα-dependent manner."]
- Lipid metabolism: RORA1 directly increases human APOC3 promoter activity and maps to promoter half-sites. [PMID:11053433, "Transient transfection experiments in human hepatoma HepG2, human colonic CaCO2, and rabbit kidney RK13 cells demonstrated that overexpression of the human RORalpha1 isoform specifically increases human apo C-III promoter activity, indicating that RORalpha1 enhances human apo C-III gene transcription."]
- Glucose/sterol response: 7-alpha-hydroxycholesterol changes ROR target-gene expression and suppresses hepatocyte glucose output in an RORA/RORC-dependent setting. [PMID:19965867, "Furthermore, glucose output from hepatocytes is suppressed by 7alpha-OHC functioning as an RORalpha/gamma ligand."]
- Anti-inflammatory signaling: [PMID:11252722, "ROR alpha1 negatively interferes with the NF-kappaB signalling pathway by reducing p65 translocation as demonstrated by western blotting, immunostaining and electrophoretic mobility shift assays."]
- Hypoxia signaling: [PMID:18658046, "RORalpha was physically associated with HIF-1alpha through DNA binding domain, which was required to the RORalpha-induced stabilization and transcriptional activation of HIF-1alpha."]
- Myogenic differentiation: dominant-negative RORA delayed marker expression and morphological differentiation. [PMID:9862959, "Immunohistochemistry demonstrates that morpho-logical differentiation is delayed in cells expressing the RORDeltaE transcript."]
- Astrocyte inflammatory regulation: Rora directly activates Il6 under basal conditions while indirectly restraining excessive induced IL-6. The cached study is in mouse astrocytes. [PMID:19955433, "We have also demonstrated that ROR(alpha) directly trans-activates the Il-6 gene."]

## Cerebellar-development interpretation

The human genetics evidence firmly supports a developmental cerebellar role without changing the identity of the core molecular function. [PMID:29656859, "RORα, the RAR-related orphan nuclear receptor alpha, is essential for cerebellar development."] The same paper reports pathogenic human variants with neurodevelopmental delay and, in a subset, ataxia and cerebellar atrophy: [PMID:29656859, "individuals with de novo dominant toxic variants present with ID, ataxia, and cerebellar atrophy."]

GO:0021930 (cerebellar granule cell precursor proliferation) and GO:0008589 (regulation of smoothened signaling pathway) are mouse-to-human orthology transfers. They are retained as non-core contextual roles. The available human abstract does not establish the full Purkinje-cell RORA → SHH → granule-cell-precursor mechanism directly. A decisive human experiment would combine acute RORA loss in iPSC-derived Purkinje cells, RORA chromatin occupancy/nascent transcription, secreted SHH measurements, and co-culture rescue of granule-cell-precursor proliferation.

## Curation decisions

- Generic `protein binding` annotations were marked `MARK_AS_OVER_ANNOTATED`; the interaction evidence was not declared false. Specific transcription coactivator, corepressor, and coregulator binding terms were retained.
- Generic `DNA binding` and `DNA-binding transcription factor activity` terms were changed to more informative RORE/cis-regulatory, RNA polymerase II-specific, and nuclear-receptor terms.
- Nuclear, nucleoplasmic, and chromatin localization were retained as core-compatible. The HPA nucleolar pool was kept as non-core.
- Tissue-specific developmental, metabolic, immune, hypoxia, angiogenesis, and circadian outputs were retained as non-core rather than conflated with receptor activity.
- No experimental annotation was removed. One specific claim, positive regulation of VEGF production, remains undecided because the relevant full text is unavailable locally.
