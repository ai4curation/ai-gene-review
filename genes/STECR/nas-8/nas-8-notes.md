# STECR nas-8 notes

## 2026-11-24

- Cross-checked the existing review as the remaining Steinernema astacin seed for the nematode pathogens lane.
- Did not run `just fetch-gene` or `just fetch-gene-pmids`: `D2KBH9` and `PMID:20670659` were already cached, and content PRs must not refresh existing `publications/` files.
- `just deep-research-falcon STECR nas-8 --fallback perplexity-lite` failed because the falcon and perplexity providers were unavailable; no provider deep-research file was written.
- `just paint-losses STECR nas-8` reported that `D2KBH9` is not a leaf of the current `PTHR10127` PAINT tree and that there are no IRD or IKR losses to check for this lineage.
- PANTHER `PTHR10127:SF883` places S. carpocapsae NAS-8 with C. elegans NAS-8 and metazoan astacins, whereas the cuticle DPY-31 enzymes curated in this project are in `PTHR10127:SF813`; NAS-8 remains a secreted astacin comparator, not another DPY-31-family cuticle-collagen processor.
- The single cached paper for Sc-AST, `PMID:20670659`, directly supports a secreted astacin zymogen architecture and recombinant, chelator-sensitive metalloendopeptidase activity against gelatin and azocasein. Its abstract supports host-tissue induction and a proposed role in parasitism but does not directly identify native substrates, show endogenous secretion, or assay `nas-8` loss of function during insect invasion.
- Updated the review to `COMPLETE`, converted the broad `GO:0008237` metallopeptidase parent from `MARK_AS_OVER_ANNOTATED` to `TOO_GENERAL`, and accepted `GO:0006508` proteolysis as the direct biological process executed by the protease without proposing a stronger host-interface process term.
- Addressed AI review by making the description qualify native secretion from the signal peptide and zymogen evidence, and by scoping the infection-process knowledge gap to the cached Sc-AST paper.
