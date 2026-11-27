# MDK curation notes

## Evidence

- `just deep-research-falcon human MDK --fallback perplexity-lite` was attempted on 2026-11-26, but both configured providers were unavailable before writing a file. The review therefore uses cached UniProt, GOA, PAINT, Reactome, and publication records directly.
- Midkine is a secreted heparin-binding pleiotrophin-family ligand. UniProt summarizes its core activity as: "Secreted protein that functions as a cytokine and growth factor and mediates its signal through cell-surface proteoglycan and non-proteoglycan receptors".
- PMID:9384573 directly supports heparin binding by MDK: "Basic residues on the beta-sheet of the C-terminal domain form another heparin-binding site."
- PMID:10212223 supports PTPRZ1 binding through glycosaminoglycans and downstream neuron migration: "These results suggested that PTPzeta is a common receptor for midkine and pleiotrophin."
- PMID:12084985 supports MDK binding to glypican-2 heparan sulfate chains, clustering GPC2 and SDC3, and inducing neuronal adhesion and neurite outgrowth.
- PMID:15466886 supports MDK binding to alpha4beta1 and alpha6beta1 integrins as functional receptor complexes for osteoblast migration and embryonic neurite outgrowth.
- PMID:27445335 supports the shared PTN/MDK PTPRZ mechanism: "Upon ligand application, PTPRZ-A/B in cultured oligodendrocyte precursor cells exhibited punctate localization on the cell surface instead of diffuse distribution, causing the inactivation of PTPRZ and oligodendrocyte differentiation."

## Review decisions

- Bare `GO:0005515` protein-binding rows are removed as uninformative unless a specific MF replacement is directly supported; removal does not reject the reported physical interaction.
- The rows on growth-factor, heparin-, heparan-sulfate-, and chondroitin-sulfate-binding activity capture the conserved extracellular ligand role and are accepted.
- Human experimental rows for MDK-mediated leukocyte recruitment, Notch2/STAT3 signaling in keratinocytes, integrin-mediated migration, and neurite outgrowth were kept as non-core downstream contexts of a secreted growth factor.
- Orthology-only transfers for high-level mouse behavioral, reproductive, adrenal, auditory, brain-region-development, and generic transcription/signaling phenotypes were treated as over-annotations onto the human ligand.
- The PMIDs cached for the myocardial-infarction rows were abstract-only, and the cached abstract did not support the exact blood-vessel branching or cardiac-muscle apoptosis GO calls strongly enough to keep them.

## PTHR13850 module and GO-CAM scope

PTHR13850 itself has only the two secreted ligands MDK and PTN. The recurring mechanism in Reactome is MDK/PTN binding to chondroitin-sulfated PTPRZ, PTPRZ clustering/inactivation, and downstream ALK signaling, but a useful module would need to include PTPRZ, ALK, and integrin or catenin branches from other families. No production GO-CAM in the local `gocams/index.tsv` mentions MDK or PTN, so this PR records the Reactome-supported signaling context in the gene reviews without adding a GO-CAM review.
