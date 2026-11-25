# recG curation notes

- Q88C73 is a RecG-family ATP-dependent 3-prime-to-5-prime helicase that branch-migrates Holliday junctions and regresses stalled forks [UniProtKB:Q88C73, "Has a DNA unwinding activity characteristic of a DNA helicase with 3'-5' polarity"].
- RecG is modeled as a route parallel to RuvAB rather than as a RuvABC subunit or resolvase. Comparative work supports independent RecG and RuvABC branch-migration pathways [PMID:18375550, "they participate in independent pathways that branch migrate Holliday junctions during recombinational DNA repair"].
- The same study shows that RecG products and repair outcomes are taxon-dependent when a compatible resolver is absent [PMID:18375550, "deployment of the RecG pathway is lethal"]. The module therefore leaves the RecG-to-RuvC handoff unverified in KT2440.

## 2026-11-09 re-review (Claude, AI-assisted; module audit)

- Generic nucleotide binding, DNA helicase activity and hydrolase activity are TOO_GENERAL (their specific descendants are kept); nucleic acid binding is MODIFY to four-way junction DNA binding; DNA repair and DNA recombination are MODIFY to recombinational repair (GO:0000725).
- Q88C73 is unreviewed in UniProt and is not in the reviewed PTHR47964 entries list; its RecG identity rests on TIGR00643/IPR004609 and the RecG wedge domain, which separate RecG from Mfd in the mixed PTHR47964:SF1 subfamily.
- 2026-11-10: added a NEW ISS row and core MF for GO:0009378 four-way junction helicase activity, transferred from E. coli RecG via the RecG-specific family (TIGR00643, IPR004609).
