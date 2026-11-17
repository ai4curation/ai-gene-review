# CodA assayed-protein identity

The official AY304485.1 record identifies strain ATCC8010, codA, protein AAP68832.1, and PMID14678796. Its complete 546-residue translation is identical to frozen UniProt Q7X2H8. Reproduce with `uv run python genes/ARTGO/codA/codA-source-analysis/verify_identity.py`. The SHA256 proof concerns sequence identity, not independently measured physiology.

PMID14678796 cloned ATCC8010 genomic DNA and purified recombinant protein from E. coli Rosetta(DE3)pLysS. PMID14690428 explicitly refers to this recombinant-enzyme preparation. Q7X2H8 merges another strain/source: its H255R conflict applies to CAA59321/AAS99880, not AAP68832.1. The earlier sequence had errors at residues298–410; the corrected deposited translation, not a protein-name match, grounds this review. PMID12795615 assigns flavin to His87 in an earlier sequence/variant, whereas PMID18072756 identifies His99 in the current structure; numbering is not silently interchanged.

The broad GMC family/domain membership supports oxidoreductase architecture, not substrate or electron-acceptor specificity. Frozen UniProt reports PTHR11552:SF152; its official PANTHER name is OXIDASE (CODA), PUTATIVE (AFU_ORTHOLOGUE AFUA_8G04090)-RELATED.
