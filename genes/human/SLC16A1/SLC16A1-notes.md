# SLC16A1 (MCT1, P53985) — review notes

Deep research: `just deep-research-falcon human SLC16A1` reported a timeout (600 s, all providers failed),
so the review was grounded in UniProt P53985, GOA, and cached publications. The falcon report
(`SLC16A1-deep-research-falcon.md`) was written afterwards. Checked against the review: its annotation
conclusion (basigin-associated, mainly plasma-membrane, proton-coupled L-lactate/monocarboxylate
transporter) matches the core function. It also mentions a proposed direct mitochondrial import role
(Cluntun et al. 2024), which it says should be annotated separately at its own level of evidence; there is
no GOA annotation for it and the review does not add one.

## Function
- Proton-coupled bidirectional monocarboxylate transporter of the plasma membrane: lactate, pyruvate,
  acetate, ketone bodies [file:human/SLC16A1/SLC16A1-uniprot.txt "Bidirectional proton-coupled monocarboxylate transporter"];
  [PMID:8124722 "properties resemble those of the erythrocyte MCT, including proton symport"].
- Surface expression needs BSG/CD147 [PMID:10921872 "CD147 facilitates proper expression of MCT1 and MCT4 at the cell surface"].
- pH-gated succinate export from exercising muscle [PMID:32946811 "succinate is rendered a transport substrate for monocarboxylate"].

## Disease link used in dismech (HHF7, exercise-induced hyperinsulinism)
- Promoter-activating variants de-repress MCT1 in beta cells, where it is normally silenced
  [PMID:17701893 "induce SLC16A1 expression in beta cells, where this gene is not usually transcribed, permitting pyruvate uptake and pyruvate-stimulated insulin release despite ensuing hypoglycemia"].
  This is a gain-of-expression disease state; normal beta cells do not use MCT1, so SLC16A1 is not a
  part of the normal GSIS module.

## Curation decisions
- Core MF lactate:proton symporter activity (GO:0015650); BP plasma membrane lactate transport,
  pyruvate transmembrane transport (matches dismech node GO:1901475 INCREASED).
- Centrosome / centrosome cycle (SSX2IP study) REMOVED as implausible screen artefacts.
- Mevalonate transport terms kept non-core: property of the MEV Phe->Cys gain-of-function mutant.
- protein binding (BSG, PDZ fragmentomics, SLC interactome) REMOVED as uninformative.
