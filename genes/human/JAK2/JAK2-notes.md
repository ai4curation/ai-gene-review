# JAK2 notes

Deep research (falcon / perplexity-lite) failed (providers unavailable). Notes from cached publications and UniProt O60674.

## Core biology
- Non-receptor tyrosine kinase; FERM-SH2 region binds cytokine receptor box1/box2; JH2 pseudokinase (regulatory, weak dual-specificity kinase [PMID:21841788 "Here we show that JH2 is a dual-specificity protein kinase that phosphorylates two negative regulatory sites in JAK2: Ser523 and Tyr570."]); JH1 kinase.
- Activation loop Y1007 essential [PMID:9111318 "Mutation of Y1007, or both Y1007 and Y1008, to phenylalanine essentially eliminated kinase activity"].
- EPO signaling in primary human erythroid cells [PMID:9657743 "We found that erythropoietin induces tyrosine phosphorylation of Jak2, STAT5A, and STAT5B."].
- beta c association [PMID:8007942 "JAK2 physically associates with the beta c chain but not with the alpha chain."]; IL-23R [PMID:12023369 "IL-23R associates constitutively with Jak2"]; gp130/LIFR [PMID:8272873].
- FERM domain/box1-box2 needed for TpoR surface expression and stability [PMID:15899890].
- Knockout: no definitive erythropoiesis, no IFN-gamma response [PMID:9590174 "Primitive erythrocytes are found, but definitive erythropoiesis is absent."].
- Nuclear H3Y41 phosphorylation [PMID:19783980 "human JAK2 is present in the nucleus of haematopoietic cells and directly phosphorylates Tyr 41 (Y41) on histone H3"] -- treated as non-core.

## Localization
Cytoplasmic, peripheral at the inner (cytoplasmic) face of the plasma membrane via receptor binding; no TM, no
extracellular exposure. Also endomembranes during receptor trafficking, and a reported nuclear pool.
Reactome "endosome lumen" assignment is topologically impossible -> REMOVE.

## Curation approach
396 GOA rows (159 Reactome cytosol rows). Core: PTK activity, cytokine receptor binding, JAK-STAT and specific
cytokine pathways. Downstream physiology KEEP_AS_NON_CORE; apoptosis machinery / response-to-chemical / adhesion
machinery terms marked over-annotated; generic protein binding removed except receptor partners (-> cytokine receptor binding).

## 2026-11-23 ORGANELLES endosome batch 1

- GO:0005768 row: IEA from ARBA00028568 only (unvetted ML rule). UniProt gives JAK2 an endomembrane item by similarity, cytoplasm and nucleus, no endosome. The earlier reason's PMID:15899890 localises TpoR (with recycling transferrin), not JAK2.
- PubMed searches (2026-11-23) for JAK2 with endosome/endosomal plus localization, colocalization, fractionation or EEA1 found no study placing JAK2 itself in endosomes (hits localised GM-CSF receptor beta in rat mesothelium, PMID:31212003; PAF receptor, PMID:27098179; EPOR-GFP in endosome-like puncta, PMID:11997394). None cached or cited.
- KEEP_AS_NON_CORE -> MARK_AS_OVER_ANNOTATED (consistent JAK rule: JAK1 has an endogenous EEA1-endosome line, JAK3 an abstract-level line, JAK2 none).
- Out-of-survey sub-compartment row GO:0031904 endosome lumen (Reactome TAS R-HSA-1170539): REMOVE kept (a cytosolic kinase cannot be luminal); added a WRONG_TERM CHECK source defect for Reactome.
