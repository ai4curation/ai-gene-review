# RAM1 (Medicago truncatula, G7L166) curation notes

Session 2026-10-02 (claude-code, PLANT_FUNGAL_INTERACTIONS project)

Sources: UniProt G7L166, falcon deep research, cached abstracts for PMID:23122845, 25971550, 26511916, 27020747, 28596311 and the full text of 26597293. The three GOA source papers are cached as abstracts only.

## Identity
- GRAS family protein, GRAS domain 288-673 (UniProt). Not the same as RAM2, which is the GPAT enzyme downstream of RAM1.

## Function
- RAM1 is required for Myc but not Nod signalling [PMID:23122845 "RAM1 is specifically required for Myc factor signaling and appears to have no role in Nod factor signaling."]
- ram1-1 has a hyphopodium defect [PMID:23122845 "Plants mutated in RAM1 are unable to be colonized by mycorrhizal fungi, with a defect in hyphopodia formation on the surface of the root."], BUT ram1-3 does not [PMID:26511916 "RAM1 is not necessary to enable hyphopodium formation or hyphal entry into the root but is essential to support arbuscule branching"]. Per the deep research, Park et al. compared ram1-1 and ram1-3 side by side and saw the same unbranched-arbuscule phenotype. So the "RAM1 -> RAM2 -> hyphopodium" link is disputed. The main defect is arbuscule branching.
- Targets: RAM2 is a direct target [PMID:28596311 "the glycerol-3-phosphate acyltransferase RAM2, a direct target of RAM1"]. RAM1 is required and sufficient for the arbuscule lipid biosynthesis program [PMID:28596311]. EXO70I, STR and RAD1 depend on RAM1 [PMID:26511916]. The deep research says Park et al. did not show RAM1 binding to the STR or EXO70I promoters.
- Upstream: in Lotus, a CCaMK-CYCLOPS-DELLA complex activates RAM1 [PMID:27020747 "The corresponding proteins form a complex that activates RAM1 expression via binding of CYCLOPS to a cis element in the RAM1 promoter."]. Ectopic RAM1 rescues cyclops mutants. In Medicago, DELLAs modulate RAM1 [PMID:26511916 "expression of RAM1 and RAD1 is modulated by DELLAs"].
- Pre-symbiotic stage: the response to Myc-LCOs requires both RAM1 and NSP1 [PMID:26597293 "gene expression activation by Myc-LCOs supplied at 10(-7/-8) M strictly required both the GRAS transcription factors RAM1 and NSP1"].
- Interactors (from UniProt, citing Park et al. 2015): NSP2 (Q5NE24), RAD1 (G7JMM0), TF80 (G7J1L1), all GRAS proteins.
- Phosphate: ram1-3 is insensitive to phosphate-mediated suppression of colonization [PMID:26511916].

## Decisions
- MF: kept DNA-binding TF activity (IBA, plus IMP deferring to curator). Direct DNA binding by RAM1 alone is still unresolved; this is listed as a suggested question.
- protein binding x3 changed by MODIFY to protein heterodimerization activity (GRAS-GRAS).
- detection of phosphate ion: MARK_AS_OVER_ANNOTATED. The phenotype shows RAM1 is needed for the phosphate response; it does not show that RAM1 perceives phosphate (necessity vs participation).
- GO:0006357 changed by MODIFY to GO:0045944 positive regulation of transcription by RNA polymerase II.
- Cytoplasm (ISS from Lotus RAM1, plus IEA): KEEP_AS_NON_CORE.
- PMID:25971550 IMP is about the petunia ATA ortholog going by the abstract. Accepted, and the evidence code is flagged as a question.
- No NEW terms. The plant-side process term GO:0036377 is adequate. The "arbuscule formation for nutrient acquisition" terms (GO:0075328 family) are fungus-side terms and do not apply to the plant protein.
