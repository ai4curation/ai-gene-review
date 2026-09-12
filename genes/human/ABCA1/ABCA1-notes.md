# ABCA1 review notes

Deep research status: `just deep-research-falcon human ABCA1 --fallback perplexity-lite` was launched after `just fetch-gene human ABCA1` and `just fetch-gene-pmids human ABCA1`; it timed out after 180 seconds without writing a provider artifact. This note records the local evidence used for the first-pass GO review.

## Core functional picture

ABCA1 is a multipass ABCA-family transporter whose defining function is ATP-coupled lipid movement at the plasma membrane/endosomal system. UniProt summarizes the molecular role as phospholipid translocation coupled to ATP hydrolysis [file:human/ABCA1/ABCA1-uniprot.txt "Catalyzes the translocation of specific phospholipids"] and apolipoprotein-dependent HDL biogenesis [file:human/ABCA1/ABCA1-uniprot.txt "transfer to apolipoproteins"]. Direct reconstitution assays support phosphatidylcholine, phosphatidylserine, and sphingomyelin transport [PMID:24097981 "ABCA1 actively exported or flipped phosphatidylcholine, phosphatidylserine, and sphingomyelin"] and show lipid-stimulated ATPase activity [PMID:24097981 "The same phospholipids stimulated the ATPase activity of these ABCA transporters"].

ABCA1-dependent HDL formation is tied to apoA-I and other exchangeable apolipoproteins. Tangier-disease studies show that loss or inhibition of ABC1 reduces apolipoprotein-mediated lipid efflux [PMID:10525055 "Blocking the expression or activity of ABC1 reduces apolipoprotein-mediated lipid efflux"] and place the protein at the plasma membrane [PMID:10525055 "The protein is incorporated into the plasma membrane"]. ApoA-I extracellular-loop mutants impair cholesterol efflux and apoA-I interaction [PMID:12084722 "apoA-I-stimulated cholesterol efflux"] [PMID:12084722 "direct interaction with apolipoprotein A-I"]. A later structural/mechanistic study supports extracellular phospholipid extraction/export [PMID:35974019 "ABCA1 extracts lipid from the outer face of the plasma membrane"].

ABCA1 is also strongly tied to cholesterol efflux and apolipoprotein E lipidation. The original Tangier/familial HDL-deficiency genetics paper named ABC1/CERP for intracellular cholesterol transport [PMID:10431236 "intracellular cholesterol transport"] [PMID:10431236 "cholesterol efflux regulatory protein"]. ApoE can bind ABCA1 and induce cholesterol efflux, generating nascent apoE/cholesterol/phospholipid particles [PMID:14754908 "apoE3-mediated cholesterol efflux"] [PMID:14754908 "nascent apoE3/cholesterol/phospholipid complexes"]. This supports Alzheimer-relevant ABCA1 placement in APOE lipidation and lipid homeostasis modules.

## Annotation review decisions

Accept as core: ABC transporter/ATP binding and hydrolysis terms, ATPase-coupled transmembrane/lipid-carrier activity, floppase/phospholipid transfer terms, cholesterol transport/efflux/homeostasis, apoA-I/apolipoprotein binding or receptor activity, HDL assembly/reverse cholesterol transport, and direct plasma-membrane/endosomal membrane localizations.

Keep as non-core: experimentally plausible context terms such as apoA-I-triggered Cdc42/GPCR signaling, inflammatory/cytokine or LPS response, endothelial shear/LDL/nutrient response, ER/Golgi/perinuclear trafficking, lysosome or platelet dense-granule phenotypes, protein secretion/signal release, and phagocytic vesicle/membrane raft localization. These are credible ABCA1 biology but not the primary molecular function.

Mark as over-annotated: generic `protein binding`, broad signaling-receptor or ATPase-binding annotations, and other partner-binding labels that do not capture ABCA1's informative activity.

Modify: broad or misleading transport labels should be redirected to lipid-specific terms, especially cholesterol transport/transfer or phospholipid translocation/ATPase-coupled intramembrane lipid carrier activity.

## 2026-06-20 second-pass audit

The second-pass audit confirmed the existing ABCA1 review and manual reference metadata. No annotation action changes were needed: ABCA1 remains curated as an ATP-driven phospholipid/cholesterol transporter that enables apolipoprotein-dependent lipid efflux, HDL biogenesis, and APOE lipidation, with inflammatory, signaling, vesicle, secretion, trafficking, and generic binding annotations kept non-core or over-annotated unless they directly reflect lipid-transport biology.
