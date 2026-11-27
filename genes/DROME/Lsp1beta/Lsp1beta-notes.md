# Lsp1beta review notes

## Identity
- beta subunit of larval serum protein 1 (LSP-1) hexamerin; hemocyanin/phenoloxidase superfamily (PANTHER PTHR11511:SF5).
- UniProt: heterohexamer of alpha, beta, gamma; secreted, larval hemolymph.

## Literature
- [PMID:410643 "Larval serum protein 1 is the major haemolymph protein just before puparium formation in Drosophila melanogaster."]
- [PMID:410643 "It has been purified and characterised as a family of hexamers (molecular weight 450000-480000) of three immunologically related polypeptides"]
- [PMID:6804227 "These observations show that the LSP-1 subunits are more closely related to each other than any is to LSP-2"]
- [PMID:38851190 "preventing hexamerin stores enhances the growth of early-developing organs while compromising the emergence of late-forming ones, consequently altering body allometry"] (abstract only in cache)

## Decisions
- Core MF nutrient reservoir activity (own activity as stored protein), in_complex GO:0005616, location extracellular region.
- Energy homeostasis kept as non-core (indirect; deferred to curator).
- No enzymatic or transport activity asserted; hexamerins lack the copper sites of hemocyanins/phenoloxidases.

## Deep research (falcon) additions
- Hemolymph proteomics [file:DROME/Lsp1beta/Lsp1beta-deep-research-falcon.md "Proteomics directly detected Lsp1b in larval hemolymph"]
- Co-regulation caveat [file:DROME/Lsp1beta/Lsp1beta-deep-research-falcon.md "silencing **any** of Lsp1α, Lsp1β, or Lsp1γ also drastically reduced the other Lsp1 transcripts"]
- Reported (not curated in GOA): enterocyte Lsp1beta RNAi slows pupariation, a small Lsp-expressing hemocyte cluster. Not added as annotations.
