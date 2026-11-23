# A. fumigatus erg12 review notes

## Manual review, 2026-10-24

Falcon deep research was not generated for this branch because provider API keys are not configured. This review used the seeded GOA rows, the local UniProt flat file, cached PMID abstracts, and the PANTHER PTHR43290 PAINT snapshot.

erg12 / AFUA_4G07780 is in PANTHER `PTHR43290:SF2` with the official subfamily label `MEVALONATE KINASE`. PAINT node `PTN000048555` asserts `GO:0004496` mevalonate kinase activity, `GO:0019287` isopentenyl diphosphate biosynthetic process via mevalonate, and `GO:0005829` cytosol at the family root; PAINT node `PTN000825284` asserts the fungal `GO:0006696` ergosterol biosynthetic process from the S. cerevisiae ERG12 seed. These placements are appropriate for the A. fumigatus member.

The A. fumigatus-specific literature is pathway context rather than a direct Erg12 enzyme assay. Ferreira et al. review the roughly 20-gene A. fumigatus ergosterol pathway [PMID:16110826, "About 20 genes are involved in the A. fumigatus ergosterol biosynthesis pathway."]; UniProt's curated FUNCTION comment uses that pathway context and the Yasmin et al. mevalonate/TAFC study to place erg12 (AFUA_4G07780), erg8 (AFUA_5G10680), mvd1 (AFUA_4G07130), idi1 (AFUA_6G11160), and erg20 (AFUA_5G02450) in the mevalonate-to-farnesyl-diphosphate segment. Yasmin et al. show that the mevalonate pool links ergosterol and triacetylfusarinine C siderophore biosynthesis in A. fumigatus [PMID:22106303, "Here we demonstrate a link between TAFC and ergosterol biosynthetic pathways, which are both critical for virulence and treatment of fungal infections."]; the local UniProt entry separately records species-specific erg12 down-regulation during iron starvation as an ECO:0000269 statement from PMID:22106303.

Direct activity and genetic evidence come from the S. cerevisiae ortholog. Oulmouden and Karst sequenced ERG12 and characterized it as mevalonate kinase [PMID:1645230, "The nucleotide sequence of the ERG12 gene, encoding mevalonate kinase, from Saccharomyces cerevisiae is presented."]; Karst and Lacroute classified erg12 mutants among ergosterol auxotrophs lacking early pathway enzymes [PMID:200835, "Thermosensitive mutants, auxotrophic for ergosterol synthesis, have been isolated"]; and Song assayed mevalonate kinase in wild-type and ERG12-overexpressing yeast extracts [PMID:16477420, "This method has been successfully applied to S. cerevisiae strains containing a wild type level of mevalonate kinase."].

## Annotation decisions

- Accepted both mevalonate kinase activity rows. The PAINT IBA from `PTN000048555` and the InterPro/Rhea/EC IEA both point to the same `(R)-mevalonate + ATP = (R)-5-phosphomevalonate + ADP + H(+)` reaction.
- Accepted both `GO:0019287` IPP via mevalonate rows and both `GO:0006696` ergosterol rows. Erg12 performs the first ATP-dependent phosphorylation in the mevalonate-to-IPP branch, and that branch supplies fungal farnesyl diphosphate and ergosterol synthesis.
- Accepted cytosol as the specific predicted compartment for this soluble kinase.
- Kept ATP binding as non-core because it is an aspect of the kinase reaction.
- Marked broad cytoplasm and isoprenoid-biosynthesis rows `TOO_GENERAL`: cytosol is the accepted location, and `GO:0019287` is the specific accepted mevalonate-pathway process.
