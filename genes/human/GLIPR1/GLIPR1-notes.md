# GLIPR1 review notes

Date: 2026-07-18

## Research provenance

- `just fetch-gene human GLIPR1` retrieved the reviewed UniProt record, 11 GOA annotation groups, and the local PANTHER family data.
- `just fetch-gene-pmids human GLIPR1` cached all four PMIDs cited by GOA.
- The configured automated research attempt failed: Falcon/Edison returned HTTP 402 and the Perplexity-lite fallback returned HTTP 401 because provider quota was exhausted. The evidence synthesis below was therefore performed manually from repository-cached primary publications, the UniProt record, Reactome records, and the local PANTHER export.

## Protein identity and topology

GLIPR1 (UniProt P48060; also RTVP-1) is a 266-amino-acid CAP/CRISP-superfamily protein. The canonical precursor has an N-terminal signal peptide (residues 1-21), an extracellular CAP/SCP domain, a single C-terminal transmembrane helix (233-255), and a short cytoplasmic tail. A crystal structure of the soluble human CAP domain showed the conserved CAP fold and a cavity capable of coordinating zinc, but the physiological ligand and direct biochemical activity remain unknown. [PMID:21931216, "GLIPR1 is composed of a signal peptide that directs its secretion, a conserved cysteine-rich CAP (cysteine-rich secretory proteins, antigen 5 and pathogenesis-related 1 proteins) domain and a transmembrane domain."] [PMID:21931216, "the putative binding cavity coordinates Zn2+ similarly to snake-venom CRISPs"]

The second human isoform, RTVP-1b, diverges after residue 141. It is broadly expressed, is increased in glioblastoma relative to normal brain and lower-grade tumors, and promoted glioma-cell proliferation when overexpressed without increasing migration. No normal isoform-specific function has been established. [PMID:17825796, "Overexpression of RTVP-1b increased glioma cell proliferation but did not affect cell migration."]

## Expression and context dependence

The initial cloning studies disagreed about normal-tissue breadth. One study reported expression in glioblastoma but not normal brain, while another found fetal expression in kidney and ubiquitous adult expression, with high expression in glial-derived tumor lines. [PMID:7607567, "The GLIPR gene is highly expressed in the human brain tumor, glioblastoma multiforme/astrocytoma, but neither in normal fetal or adult brain tissue, nor in other nervous system tumors."] [PMID:8973356, "Northern hybridization analysis revealed that in fetal tissue RTVP-1 RNA was detected only in the kidney, but its expression was ubiquitous in adult tissues including brain."] The reviewed UniProt record accordingly reports conflicting tissue-expression results rather than a single brain-specific pattern.

GLIPR1 has opposite experimentally observed effects in different tumor-cell contexts. In prostate cancer cells, GLIPR1 is frequently down-regulated and restoration or overexpression promotes apoptosis and growth suppression. In glioblastoma cells, GLIPR1 is elevated and promotes spreading, migration, invasion, and extracellular-matrix degradation. These results should be represented as context-dependent regulatory roles, not collapsed into a universal tumor-suppressor or oncogenic label.

## Prostate-cell growth suppression and apoptosis

Human prostate cancer studies establish a p53-responsive, pro-apoptotic role. GLIPR1 overexpression increases ROS and engages JNK-dependent apoptosis; Glipr1-null mice show increased tumor susceptibility. [PMID:18199537, "Mechanistic analysis indicated that GLIPR1 up-regulation increases the production of reactive oxygen species (ROS) leading to apoptosis through activation of the c-Jun-NH(2) kinase (JNK) signaling cascade."]

Additional mechanistic work showed that GLIPR1 redistributes CK1alpha and promotes beta-catenin and c-Myc destruction, reducing c-MYC transcription and cell-cycle progression. [PMID:22025562, "Restoration of GLIPR1 expression in prostate cancer cells downregulated c-myc levels, inhibiting cell-cycle progression."] GLIPR1 also interacts with Hsc70, with associated destabilization of SP1 and c-Myb and suppression of AURKA and TPX2; a recombinant transmembrane-deleted protein is internalized and can reproduce apoptosis/mitotic-catastrophe phenotypes. [PMID:23333597, "GLIPR1 interacts with heat shock cognate protein 70 (Hsc70); this interaction is associated with SP1 and c-Myb destabilization and suppression of SP1- and c-Myb-mediated AURKA and TPX2 transcription."]

These studies support positive regulation of apoptosis and negative regulation of cell population proliferation in the tested human cancer-cell contexts. They do not establish a catalytic molecular function for GLIPR1.

## Glioma-cell motility and invasion

In human glioma cells and glioma stem cells, gain- and loss-of-function experiments show that GLIPR1 promotes spreading, migration, invasion, invadopodia/podosome formation, and matrix degradation. GLIPR1 associates with N-WASP and hnRNPK; reciprocal immunoprecipitation and FRET support a direct GLIPR1-N-WASP interaction. N-WASP knockdown attenuates GLIPR1-driven cell spreading, migration, and matrix degradation. [PMID:26305187, "We found that RTVP-1 increased cell spreading, migration and invasion and these effects were at least partly mediated by N-WASP."]

GLIPR1 overexpression decreases the association between N-WASP and its inhibitor hnRNPK, thereby relieving inhibition of N-WASP-dependent motility. [PMID:26305187, "overexpression of RTVP-1 decreased the association of N-WASP and hnRNPK."] This supports positive regulation of cell migration in glioma cells. It does not cleanly satisfy `molecular adaptor activity`, whose GO definition requires bringing molecules together: the demonstrated effect is disruption of an inhibitory N-WASP-hnRNPK association.

## PAINT propagation assessment

The local `PTHR10334-paint.tsv` export places both GO:0005576 `extracellular region` and GO:0060090 `molecular adaptor activity` at the broad ancestral node PTN000036124. The localization inference is supported by numerous extracellular CAP-family seeds and independently fits GLIPR1's signal peptide, type-I membrane topology, extracellular CAP domain, and soluble active ectodomain.

The adaptor inference has only one experimental seed: mouse Glipr1l1 (MGI:MGI:1916536), a sperm/acrosomal GLIPR1-like paralog. The source GO-CAM activity `gomodel:62f58d8800005094/62f58d8800005346` models mouse Glipr1l1 molecular adaptor activity at the outer acrosomal membrane in protein localization involved in the acrosome reaction [file:gocams/62f58d8800005094/62f58d8800005094-src.yaml]. GLIPR1-specific human studies show interactions with N-WASP, hnRNPK, and Hsc70, but do not show GLIPR1 bringing two molecules together. In the best-defined glioma mechanism, GLIPR1 instead decreases N-WASP-hnRNPK association. The IBA adaptor annotation is therefore a paralog/context over-propagation and should be removed.

## Localization annotations

- Extracellular-region and membrane annotations are supported by canonical signal peptide/TM topology and the human soluble-domain structure. The more precise location for the canonical membrane-bound pool is the external side of the plasma membrane (GO:0009897).
- NK-cell membrane proteomics directly detected GLIPR1 in a membrane preparation, although the cached abstract does not enumerate individual proteins. [PMID:19946888, "The present study was initiated to define the composition of the membrane proteome of the Natural Killer (NK) like cell line YTS."]
- Reactome places GLIPR1 in the plasma membrane and, in neutrophils, the azurophil-granule membrane. The latter and the corresponding post-exocytosis plasma-membrane localization are defensible but context-specific rather than defining GLIPR1's general function.

## Interaction annotations

The GOA protein-binding rows report ALOXE3 in two BioPlex AP-MS networks and HTT in a neurodegeneration-focused interaction map. The ALOXE3 interaction is replicated across two high-throughput datasets, and UniProt/IntAct records both ALOXE3 and HTT. However, generic `protein binding` does not describe GLIPR1's molecular activity, and none of these high-throughput interactions has a demonstrated GLIPR1-specific functional consequence. All three should be marked over-annotated rather than used as core molecular functions.

## Curation conclusion

The strongest conserved structural conclusion is that canonical GLIPR1 is an extracellular-facing, single-pass membrane CAP protein that can also act in a released/soluble form. Its immediate physiological ligand and biochemical activity remain unresolved. Direct human-cell evidence supports context-specific regulation of apoptosis/proliferation and N-WASP-dependent migration, while the sperm-paralog-derived molecular-adaptor IBA is not transferable.
