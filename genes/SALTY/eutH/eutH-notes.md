# eutH (Salmonella Typhimurium LT2, P41796) notes

## Gene and family context
- Member of the 17-gene *eut* operon, induced by ethanolamine plus adenosylcobalamin; only six *eut* genes are needed for aerobic growth on ethanolamine under standard conditions [PMID:10464203 "Nonpolar insertion and deletion mutations made with the Tn10-derived transposable element T-POP showed that at least 10 of the 11 previously undetected eut genes have no Eut phenotype under the conditions tested."]
- Ethanolamine serves as sole C and N source only with vitamin B12, the cofactor of ethanolamine ammonia-lyase [PMID:3045078 "Ethanolamine can serve as the sole source of carbon and nitrogen for Salmonella typhimurium if vitamin B12 is present to serve as a cofactor."]
- First described as a hydrophobic permease-like protein [PMID:7868611 "The hydrophobic protein encoded by the eutH gene possesses some characteristics of bacterial permeases and might therefore be involved in the transport of ethanolamine."]
- PANTHER family PTHR40089 (ETHANOLAMINE UTILIZATION PROTEIN EUTH), single subfamily PTHR40089:SF1; InterPro IPR007441, Pfam PF04346, PIRSF019466, TCDB 9.A.28.1.1 "ethanolamine facilitator (Eaf) family"; eleven predicted TM helices (ECO:0000255) in the UniProt record.

## Function
- EutH facilitates diffusion of the uncharged ethanolamine species; the protonated form does not enter cells, and the uncharged fraction depends on pH (pK 9.5) [PMID:15466042 "Evidence is presented that protonated ethanolamine (Eth0) does not enter cells, while uncharged ethanolamine (Eth0) diffuses freely across the membrane."]
- Conditional requirement with a quantitative threshold [PMID:15466042 "When a lowered pH and/or ethanolamine concentration reduced the Eth0 concentration below 25 microM, EutH was needed to facilitate diffusion."]
- Behaves like a transporter also in conferring ethanolamine toxicity [PMID:15466042 "As predicted for a transporter, EutH contributed to the toxicity of ethanolamine seen under some conditions"]
- Membrane protein by YFP fusion [PMID:15466042 "fusion of EutH to fluorescent Yfp protein provided evidence that EutH is a membrane protein."]; UniProt curates the location as cell inner membrane from that work.
- In vivo relevance: acid-dependent role in the macrophage vacuole, conserved in *Listeria monocytogenes* [PMID:29531136 "Furthermore, in agreement with EutH being important in the acidic environment, neutralization of the vacuole abolished the requirement for EutH."] and important for dissemination rather than local intestinal infection.

## Review decisions (2026-11-04)
- Core: ethanolamine transmembrane transporter activity (GO:0034228), directly involved in ethanolamine transport (GO:0034229), located in plasma membrane (GO:0005886, i.e. the Gram-negative inner membrane).
- Both GO:0005886 rows (IBA from PAINT node PTN002219906 seeded by *E. coli* EutH P76552; IEA from UniProt SubCell SL-0037) are ACCEPT and mutually consistent; the IBA carries a `propagation_review` with `NO_FAILURE_CORE`.
- GO:0016020 membrane (InterPro2GO) is TOO_GENERAL: the accepted plasma-membrane rows entail it, and GO:0016020 is a generic location term rather than a root organelle term.
- GO:0046336 ethanolamine catabolic process (UniPathway mapping) is KEEP_AS_NON_CORE: EutH delivers the substrate but does not catalyse any step of the degradation; the growth phenotype is necessity, not participation. The transport rows carry the core claims.
- No IRD/IKR PAINT loss on this lineage (`just paint-losses SALTY eutH`).
- No source defects found: the GOA rows, their references and their WITH/FROM entries are all consistent with the record.

## Literature status
- All cited PMIDs are cached but **abstract-only** (`full_text_available: false`): 7868611, 3045078, 10464203, 15466042, 16585748, 29531136. Newly fetched in this session with `just fetch-pmid`: 10464203, 15466042, 16585748, 29531136. Quotes are therefore restricted to abstract text.
- PMID:16585748 is cited by UniProt for the pH-profile growth details (no growth at pH 5.5 or 8.5, wild-type at pH 7.0-8.0); the cached abstract does not state those numbers, so nothing is quoted from it and the review relies on PMID:15466042 instead.

## Deep research
- No `-deep-research-<provider>.md` file was generated: the repo's deep-research providers are not available in this environment (previous sessions recorded "Provider 'perplexity' not available"). This review was built from the cached publications above, the UniProt record (P41796), the PANTHER/PAINT slices for PTHR40089 and the GO definitions checked with oaklib (GO:0034228, GO:0034229, GO:0046336, GO:0005886, GO:0016020). The literature search covered every reference in the UniProt entry plus the GOA references; no further EutH-specific primary papers were identified.


## 2026-11-06 comparative re-audit

Full primary PMID15466042 explicitly states all strains are LT2 derivatives. In-frame deletions, a functional chromosomal EutH-Yfp fusion, toxicity and whole-cell swelling support conditional ethanolamine access. Standard growth used 41 mM total ethanolamine at pH 7.0; the roughly 25 micromolar uncharged-substrate requirement is a growth threshold, not a transporter Km. A normal force-fetch retained abstract-only cache, so scoped primary excerpts/provenance are in eutH-source-analysis/primary-assay-scope.yaml; raw HTML remains ignored cache. PMID29531136 macrophage experiments use SL1344, not LT2; this transfer is now explicit. The generic membrane term is refined to plasma membrane. The existing catabolic BP is ACCEPT as conditional participation through a specific substrate-delivery step within the degradation pathway: nonenzymatic transport is not automatically nonparticipation. This corrects the prior contradictory KEEP_AS_NON_CORE reason without asserting cleavage or universal transporter necessity. GO0046336 definition and ancestors were checked; precise transport remains the primary mechanistic claim. No new process row was manufactured. PAINT loss check found no IRD/IKR.

A normal Falcon research attempt failed with HTTP 403 authentication/access error; no provider report was fabricated. Review evidence comes from the primary sources, frozen UniProt/domain records and explicitly identified comparative inference. Original GOA/UniProt files and upstream row payloads are preserved. Source refreshes used only the normal publication fetch command; separately acquired full articles remain ignored, with small exact excerpts and provenance retained beside the reviews.
