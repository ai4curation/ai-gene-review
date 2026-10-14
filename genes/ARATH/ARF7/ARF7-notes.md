# ARF7 / NPH4 (At5g20730; P93022) curation notes

## 2026-10 review (auxin_nuclear_signaling module)

- Deep research (falcon) failed (HTTP 402); review based on cached literature.
- Identity: UniProt P93022 ARFG_ARATH, ARF7 (NPH4/MSG1/TIR5/BIP). Correct.

### Function
- "NPH4 encodes the auxin-regulated transcriptional activator ARF7"; required for differential growth (phototropism, gravitropism) [PMID:10810148].
- ARF7 restores auxin-responsive gene expression in nph4-1 protoplasts [PMID:15923351].
- arf7 arf19 lacks lateral roots, abnormal gravitropism; auxin-induced gene expression impaired [PMID:15659631]; ARF7/ARF19 directly activate LBD16/LBD29 [PMID:17259263].
- Leaf expansion and lateral roots [PMID:15960621]; ethylene responses in roots [PMID:16461383]; callus formation via ATXR2 and JMJ30 recruitment [PMID:29184030, PMID:29923261].
- PB1 domain structure: "Mutation of interface residues in the ARF7 PB1 domain yields monomeric protein and abolishes interaction with both itself and IAA17" [PMID:24706860].
- BIN2 phosphorylation weakens ARF7-Aux/IAA binding [PMID:24362628]; MYB77 cooperates with ARF7 [PMID:17675404].
- Cytoplasmic condensates in low-auxin-response tissues [PMID:31421981].

### Decisions
- Aux/IAA protein-binding IPIs -> MODIFY GO:0001222 transcription corepressor binding; BIN2 -> GO:0019901; MYB77 -> GO:0140297; ATXR2 -> GO:1990226; JMJ30 -> GO:0019899 (consistent with ARF19 review).
- Blue light signaling pathway IMP (PMID:10364413) -> MARK_AS_OVER_ANNOTATED (ARF7 acts in auxin response downstream).
- Developmental processes (lateral root, leaf, callus, tropisms, ethylene) -> KEEP_AS_NON_CORE.
- NEW: GO:0001216 DNA-binding transcription activator activity; GO:0009734 auxin-activated signaling pathway.
