# PTN curation notes

## Evidence

- `just deep-research-falcon human PTN --fallback perplexity-lite` was attempted on 2026-11-26, but both configured providers were unavailable before writing a file. The review therefore uses cached UniProt, GOA, PAINT, Reactome, and publication records directly.
- Pleiotrophin is the PTN subfamily paralog of midkine and is also a secreted heparin/chondroitin-sulfate-binding ligand.
- PMID:1733956 identified PTN as an extracellular heparin-binding growth factor secreted from human breast-cancer cells: "We report purification of an 18-kDa heparin-binding growth factor secreted from human cancer cells".
- PMID:10706604 supports PTN binding and inactivation of the receptor protein tyrosine phosphatase PTPRZ/RPTP beta/zeta and shows increased tyrosine phosphorylation of beta-catenin after PTN treatment.
- PMID:26896299 resolved PTN structure and chondroitin-sulfate binding, including the C-terminal contribution to the PTPRZ-relevant CS-A interaction.
- PMID:27445335 shows PTN-induced PTPRZ clustering/inactivation and delayed myelin-basic-protein expression in Ptn-deficient mouse brain, supporting the PTPRZ-to-oligodendrocyte-differentiation branch as a PTN-specific biological context.
- PMID:19141530 supports the alphaVbeta3 integrin branch for human endothelial-cell migration, but that receptor branch is peripheral to the family-level PTPRZ/glycosaminoglycan ligand function.

## Review decisions

- Bare `GO:0005515` protein-binding rows are removed as uninformative unless a specific MF replacement is directly supported; removal does not reject the reported physical interaction.
- `GO:0030246` carbohydrate binding was refined to the chondroitin-sulfate binding term directly supported by PMID:26896299 and already asserted in the PTN review.
- The PTPRZ protein-phosphatase inhibitor and receptor-clustering rows were accepted because PTPRZ clustering and inhibition are the best resolved PTN receptor mechanism.
- Integrin, endothelial-migration, osteoblast, proliferation, and oligodendrocyte-differentiation rows were kept as non-core contexts downstream of the secreted ligand activity.
- Orthology-only transfers for mouse auditory, reproductive, hematopoietic, synaptic, neural-development, and tissue-regeneration phenotypes were treated as over-annotations onto the human secreted ligand unless the cached human or primary mouse evidence supported a direct receptor mechanism.

## PTHR13850 module and GO-CAM scope

PTHR13850 itself contains the two extracellular ligands PTN and MDK. PTPRZ/ALK signaling is a real pathway, but its substantive phosphatase, receptor-kinase, catenin, integrin, and SRC/PI3K/AKT parts belong to other families; this ligand-only pass therefore records the family conclusions without introducing a partial module. No production GO-CAM in the local `gocams/index.tsv` mentions PTN or MDK.
