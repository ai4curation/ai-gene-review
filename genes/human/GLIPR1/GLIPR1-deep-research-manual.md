# Manual literature synthesis for human GLIPR1 (P48060)

## Scope and evidence boundary

The configured automated deep-research providers were unavailable on 2026-07-18 (Falcon/Edison HTTP 402; Perplexity-lite HTTP 401). This manual synthesis uses the reviewed human UniProt record, local PAINT and Reactome data, and primary publications cached in `publications/`. The normal physiological molecular activity remains less well defined than the disease-cell phenotypes.

## Molecular architecture and localization

Canonical human GLIPR1 is synthesized with an N-terminal signal peptide, contains a large CAP/SCP domain, and is retained by a C-terminal transmembrane helix as a type-I single-pass membrane protein. The CAP domain is therefore extracellular-facing, while the cytoplasmic tail is only approximately 11 residues. The crystal structure of the isolated human CAP domain shows the conserved CAP fold and zinc coordination in its central cavity, but no physiological ligand or enzymatic reaction was identified. [PMID:21931216, "GLIPR1 is composed of a signal peptide that directs its secretion, a conserved cysteine-rich CAP (cysteine-rich secretory proteins, antigen 5 and pathogenesis-related 1 proteins) domain and a transmembrane domain."]

Canonical GLIPR1 can be released or experimentally supplied as a soluble transmembrane-deleted ectodomain, and prostate cancer cells internalize recombinant protein. Thus both the external plasma-membrane pool and a soluble extracellular pool are biologically plausible. The azurophil-granule localization captured by Reactome is a specialized neutrophil trafficking context, not evidence that granules define the protein's general function.

## Context-dependent cellular functions

In prostate cancer cells, GLIPR1 restoration induces ROS-JNK-dependent apoptosis, suppresses colony growth, redistributes CK1alpha, reduces beta-catenin/TCF4-dependent c-MYC transcription, and promotes c-Myc turnover. It also interacts with Hsc70 in a pathway associated with SP1/c-Myb destabilization and reduced AURKA/TPX2 expression. These experiments support positive regulation of apoptosis and negative regulation of cell proliferation, but the direct biochemical action of GLIPR1 upstream of ROS, CK1alpha redistribution, and Hsc70 remains unresolved. [PMID:18199537, "Overexpression of GLIPR1 in cancer cells leads to suppression of colony growth and induction of apoptosis."] [PMID:22025562, "Restoration of GLIPR1 expression in prostate cancer cells downregulated c-myc levels, inhibiting cell-cycle progression."]

In glioma cells and glioma stem cells, GLIPR1 instead promotes spreading, migration, invasion, invadopodia/podosome formation, and extracellular-matrix degradation. It interacts with N-WASP and hnRNPK, and N-WASP depletion attenuates the motility phenotype. GLIPR1 overexpression reduces the inhibitory N-WASP-hnRNPK association. [PMID:26305187, "We found that RTVP-1 increased cell spreading, migration and invasion and these effects were at least partly mediated by N-WASP."] These findings support positive regulation of cell migration in this context, not a universal tumor-suppressor role.

## Molecular-adaptor PAINT inference

The local PTHR10334 PAINT export shows GO:0060090 `molecular adaptor activity` at ancestral node PTN000036124 with mouse Glipr1l1 as its only experimental seed. The source GO-CAM activity `gomodel:62f58d8800005094/62f58d8800005346` places mouse Glipr1l1 molecular adaptor activity at the outer acrosomal membrane, in protein localization involved in the acrosome reaction [file:gocams/62f58d8800005094/62f58d8800005094-src.yaml]. Human GLIPR1's own interactions do not demonstrate the GO-defined activity of bringing two molecules together. Its best-resolved glioma mechanism instead weakens N-WASP-hnRNPK association. Therefore the adaptor IBA is a paralog- and tissue-context over-propagation.

## Evidence-bounded conclusion

GLIPR1 is an extracellular-facing membrane CAP protein whose direct ligand and biochemical activity are unknown. It regulates distinct protein-interaction/signaling systems in different cell contexts: pro-apoptotic and antiproliferative pathways in prostate cancer cells, and N-WASP-dependent motility pathways in glioma cells. The disease-context evidence is strong, but whether either output represents the protein's dominant normal physiological role remains open.
