# TREM2 notes

## Review status

- First-pass review completed on 2026-06-19.
- `just fetch-gene-pmids human TREM2` completed successfully; all 31 PMID-backed publication caches were present after refresh.
- Falcon deep research was attempted with `timeout 180 just deep-research-falcon human TREM2 --fallback perplexity-lite`, but the process timed out and no provider deep-research artifact was written. These notes therefore rely on the cached UniProt, GOA, and publication files.
- `just validate human TREM2` passes cleanly.

## Functional synthesis

TREM2 is a plasma-membrane immunoreceptor expressed prominently in myeloid cells, including microglia. Its core function is ligand sensing through an extracellular immunoglobulin-like domain, with signaling through TYROBP/DAP12 and downstream kinase/Ca2+/ERK pathways. The original receptor characterization supports the surface receptor and DAP12 coupling model: [PMID:11602640 "TREM-2 is a cell surface receptor on human monocyte-derived DCs, which is associated with DAP12."] The same study supports downstream signaling and survival/maturation responses: [PMID:11602640 "TREM-2/DAP12 promotes upregulation of CC chemokine receptor 7, partial DC maturation, and DC survival through activation of protein tyrosine kinases and extracellular signal-regulated kinase."]

The best-supported ligand biology is lipid/apolipoprotein and damage-associated membrane sensing. TREM2 binds apolipoprotein and lipoprotein ligands, including APOE and CLU/APOJ: [PMID:27477018 "we identified a set of lipoprotein particles (including LDL) and apolipoproteins (including CLU/APOJ and APOE) as ligands"] This ligand binding is functionally tied to uptake: [PMID:27477018 "Overexpression of wild-type TREM2 was sufficient to enhance uptake of LDL, CLU, and APOE in heterologous cells"] and to microglial handling of amyloid-lipoprotein complexes: [PMID:27477018 "this complex is efficiently taken up by microglia in a TREM2-dependent fashion."]

Independent ligand work supports aminophospholipids on apoptotic cells as signal-transducing TREM2 ligands: [PMID:31101881 "TREM2-dependent signal transduction in response to apoptotic Neuro2a cells is mediated by aminophospholipid ligands, phosphatidylserine and phosphatidylethanolamine"] Myelin/lipid challenge studies further support lipid sensing as a microglial core function: [PMID:31902528 "TREM2 senses lipids and mediates myelin phagocytosis"] and identify a role in cholesterol-related transcriptional adaptation after chronic phagocytosis: [PMID:31902528 "TREM2 as a key transcriptional regulator of cholesterol transport and metabolism under conditions of chronic myelin phagocytic activity"]

Human microglia data support the downstream functional consequences of TREM2 loss: [PMID:33097708 "TREM2 deletion reduces microglial survival, impairs phagocytosis of key substrates including APOE"] and broader functional deficits in phagocytosis and migration. Earlier disease-variant work supports a microglial innate immune and phagocytic framing: [PMID:24990881 "TREM2 is an innate immune receptor preferentially expressed by microglia and is involved in inflammation and phagocytosis."] Variant studies also distinguish Nasu-Hakola and Alzheimer-risk mechanisms, with many Alzheimer-associated variants affecting ligand binding rather than complete loss of surface expression: [PMID:27995897 "Nasu-Hakola mutations impact protein stability and decrease folded TREM2 surface expression, whereas Alzheimer's risk variants impact binding to a TREM2 ligand."]

## Annotation decisions

- Accepted annotations for transmembrane signaling receptor activity, signaling receptor activity, lipid/apolipoprotein/phospholipid/amyloid ligand binding, TYROBP-linked signaling, phagocytosis/engulfment, apoptotic-cell clearance, microglial migration, microglial activation, lipid homeostasis, cholesterol transport/metabolism regulation, and plasma-membrane localization.
- Kept non-core annotations for broader disease/pathology phenotypes, amyloid plaque association, synapse and neuronal downstream effects, cytokine/TLR/inflammatory responses, osteoclast and dendritic-cell biology, adaptive immune phenotypes, and general cellular stress or developmental readouts.
- Marked generic `protein binding` and broad complex-binding annotations as over-annotated because they obscure the better-supported ligand and receptor-adapter biology.
- No annotations were removed. Experimental disease-model and immune-cell annotations were retained as non-core when they appear biologically plausible but secondary to the receptor-ligand signaling role.

Final action distribution: 117 ACCEPT, 151 KEEP_AS_NON_CORE, 5 MARK_AS_OVER_ANNOTATED.

## Knowledge gaps and experiments

- The most useful GO-level refinement would be a specific term for TREM2-style damage-associated lipid/apolipoprotein immune receptor activity if the ontology does not already have an exact fit.
- For Alzheimer-relevant mechanism, the key gap is how APOE isoform, lipidation state, amyloid-lipoprotein complexes, and myelin/apoptotic-cell ligands compete or cooperate in vivo.
- Useful experiments would combine human iPSC microglia with isogenic TREM2 variants, defined APOE isoform/lipidation substrates, plaque or myelin debris models, and rescue with TYROBP/SYK/PLC signaling perturbations.
- Spatial in-vivo work should separate direct TREM2 receptor functions from downstream plaque compaction, synapse remodeling, and inflammatory-state effects.

## 2026-06-20 second-pass audit

The second-pass audit added manual `reference_review` metadata for the main TREM2 receptor, DAP12 signaling, lipid/apolipoprotein ligand, amyloid-beta ligand, apoptotic-cell aminophospholipid ligand, myelin/cholesterol-response, and human microglia loss-of-function papers. No annotation action changes were needed: TREM2 remains curated as a myeloid/microglial immunoreceptor for damage-associated lipid, apolipoprotein, apoptotic-cell, and amyloid-associated ligands, with plaque, synaptic, and broad inflammatory phenotypes retained as non-core context where appropriate.
