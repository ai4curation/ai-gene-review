# R3HDML manual deep research

Date: 2026-07-18

## Scope and source limitations

The configured Falcon deep-research request failed with HTTP 402, and its Perplexity-lite fallback failed with HTTP 401 because provider quota was exhausted. This manual synthesis uses the reviewed human UniProt record, the local PAINT family export and GO-CAM index, and the full-text primary mouse study PMID:31524320. It is not a provider-generated report.

## Protein identity and maturation

Human R3HDML (UniProt Q9H3Y0) encodes a 253-residue CAP-superfamily precursor. The reviewed sequence contains a signal peptide at residues 1–24, a predicted propeptide at 25–56, and a mature CAP/SCP-domain chain beginning at residue 57. The name is misleading: UniProt explicitly cautions that the protein has no R3H domain [file:human/R3HDML/R3HDML-uniprot.txt, "Despite its name, it does not contain a R3H domain."].

The mouse functional study experimentally supports secretion and processing. Differentiating satellite-cell cultures released an approximately 21-kDa form into conditioned medium, and mass spectrometry of overexpressed protein showed cleavage before secretion. The authors summarize that “R3hdml protein was secreted upon satellite cell differentiation” [PMID:31524320, "R3hdml protein was secreted upon satellite cell differentiation."]. Signal peptide, propeptide, and CAP-domain conservation make extracellular localization a safe orthology-supported conclusion for the human protein.

## Supported biological role in mouse skeletal muscle

R3hdml expression is high during early postnatal skeletal-muscle development and is induced when isolated satellite cells differentiate. R3hdml knockdown in C2C12 cells attenuated myotube formation; adding extracellular R3hdml protein rescued the phenotype [PMID:31524320, "Silencing of the R3hdml gene in C2C12 cells attenuated myotube formation, and those phenotypes were rescued in the presence of R3hdml protein."].

R3hdml-null mice had lower body and skeletal-muscle mass, reduced satellite-cell proliferation and cell-cycle-marker expression, reduced IGF-1 expression and Akt phosphorylation, and impaired recovery after cardiotoxin injury. Re-expression in the forearm rescued recovery. The study concludes that loss inhibits “satellite cell proliferation, skeletal muscle development, and regeneration” [PMID:31524320, "Knockout of this gene inhibited satellite cell proliferation, skeletal muscle development, and regeneration."]. These genetic and rescue experiments support positive regulation of myoblast proliferation, muscle-cell differentiation, skeletal-muscle development, and skeletal-muscle regeneration. For a human review they are orthology transfers, not direct human evidence.

## Molecular activity remains unknown

The extracellular mode of action is demonstrated because protein added to culture medium rescues R3hdml-silenced cells [PMID:31524320, "adding the R3hdml protein to the culture media rescued the phenotypes seen in R3hdml‐silenced C2C12 cells"]. The immediate receptor, binding partner, substrate, and biochemical activity are nevertheless unknown. The investigators could not demonstrate direct binding to Akt and explicitly frame receptor activation versus extracellular-matrix regulation through a predicted protease-inhibitor activity as alternative hypotheses [PMID:31524320, "we were unable to show direct binding of R3hdml to Akt."; PMID:31524320, "we speculate that it may work through the activation of certain receptors or by regulation of the ECM surrounding satellite cells via the predicted protease inhibitor functions based on R3hdml protein structure"]. Thus neither peptidase-inhibitor activity nor receptor-ligand activity is established strongly enough to serve as the core molecular function.

## PAINT molecular-adaptor propagation

The PTHR10334 PAINT export shows that GO:0060090 `molecular adaptor activity` at node PTN000036124 has only one experimental seed, mouse Glipr1l1 (MGI:MGI:1916536). The production GO-CAM places Glipr1l1 on the outer acrosomal membrane in protein localization during the acrosome reaction. GLIPR1L1 is a specialized sperm CAP-family paralog, whereas R3HDML is a processed secreted satellite-cell factor in the only causal study. CAP-domain membership does not establish a shared adaptor activity across this highly functionally diversified family, so the transfer to R3HDML should be removed.

## Human evidence boundary

The human sequence and secretion signals support an extracellular processed CAP protein. The direct functional experiments are in mouse cells and mice, and current human expression resources emphasize intestinal rather than adult skeletal-muscle RNA. Human satellite-cell secretion, myogenic phenotypes, receptor engagement, and protease inhibition therefore require direct testing.
