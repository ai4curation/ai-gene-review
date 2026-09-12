# ERP29 (ERp29, ERp28, ERp31, C12orf8) research notes

UniProt P30040. ER-lumenal, non-catalytic PDI-family escort/chaperone. Homodimer. KEEL ER-retention.

## Core function
- NOT a disulfide isomerase; lacks CXXC (CGHC) thioredoxin-box motif.
  - [PMID:9738895 "ERp28, a human endoplasmic-reticulum-lumenal protein, is a member of the protein disulfide isomerase family but lacks a CXXC thioredoxin-box motif."]
  - [file:human/ERP29/ERP29-uniprot.txt "Does not seem to be a disulfide isomerase. Plays an important role in the processing of secretory proteins within the endoplasmic reticulum (ER), possibly by participating in the folding of proteins in the ER."]
- Acts as a non-catalytic escort/chaperone promoting folding/processing/secretion of secretory cargo.
- Part of a large ER chaperone multiprotein complex with BiP/HSPA5, GRP94/HSP90B1, PDI, ERdj3/DNAJB11, cyclophilin B/PPIB, ERp72/PDIA4, UGGT1, SDF2L1, etc., binding nascent/unfolded Ig heavy chains.
  - [PMID:12475965 "large endoplasmic reticulum (ER)-localized multiprotein complex ... associated with unassembled, incompletely folded immunoglobulin heavy chains"]
- Homodimer (GO:0042803 homodimerization activity).
- ER lumen localization [file "SUBCELLULAR LOCATION: Endoplasmic reticulum lumen. Melanosome."]; also melanosome, cell surface (platelet), secreted.

## Other roles (ParkinsonsUK-UCL curated, PMID:22064321 breast cancer model)
- Cancer cell growth arrest via p38 MAPK activation, p58IPK upregulation; modulates gene expression and protein secretion.
  - [PMID:22064321 "ERp29-induced cancer cell growth arrest is modulated by ... phosphorylation of p38 and upregulation of ... p58(IPK)"]
- These (pos reg MAPK, pos/neg reg gene expr, neg reg protein secretion) are context-specific (cancer cell overexpression) downstream effects -> KEEP_AS_NON_CORE.
- protein unfolding (GO:0043335) NAS - ERp29 proposed to unfold cholera toxin/polyomavirus for membrane penetration; keep non-core.

## Action plan
- NOT|protein disulfide isomerase activity (GO:0003756) IKR negated - ACCEPT (correct, lacks CXXC).
- ER / ER lumen localizations - ACCEPT.
- smooth ER (ISS/IEA), melanosome, cell surface, extracellular, membrane - KEEP_AS_NON_CORE (secondary/peripheral).
- protein folding (GO:0006457) NAS - KEEP_AS_NON_CORE (chaperone-assisted, not foldase).
- protein secretion / intracellular protein transport / ER-Golgi transport - KEEP_AS_NON_CORE (processing of secretory proteins).
- protein homodimerization activity (GO:0042803) - ACCEPT (real, homodimer).
- protein-folding chaperone binding (GO:0051087) IEA/ISS - ACCEPT (binds chaperone complex; CORE MF candidate).
- protein binding IPI (GLP1R, HT) - KEEP_AS_NON_CORE.
- cancer/MAPK/gene-expr/secretion regulation - KEEP_AS_NON_CORE.
- protein unfolding - KEEP_AS_NON_CORE.
- ER stress apoptosis regulation IEA - KEEP_AS_NON_CORE.
- Core MF: protein-folding chaperone binding (GO:0051087) + escort/chaperone in secretory protein processing.
