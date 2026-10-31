# RUBCN review notes

## Scope

RUBCN/Rubicon is reviewed in the PN class III PI3K complex 2/autophagosome maturation branch. PN entries without PMIDs were used as context only. The central curation issue is that Rubicon is not an autophagy activator like UVRAG or Bif-1; it is an inhibitory PI3KC3-C2/Rab7/endosome maturation regulator.

## Evidence synthesis

Rubicon binds a UVRAG-containing Beclin 1/Vps34 complex and inhibits late autophagy. The discovery paper reports that "Rubicon binds only to a subpopulation of UVRAG complexes" and that "Knockdown of Rubicon caused enhancement of autophagy, especially at the maturation step" [PMID:19270696, "Rubicon binds only to a subpopulation of UVRAG complexes"; PMID:19270696, "Knockdown of Rubicon caused enhancement of autophagy, especially at the maturation step"]. This supports negative regulation of autophagosome maturation and negative regulation of autophagy.

The most specific molecular function is PI3K inhibitor activity. The RUN-domain paper states that "Rubicon serves as a negative regulator of PI3KC3 and autophagosome maturation", that it "interacts with the PI3KC3 catalytic subunit hVps34 via its RUN domain", and that the RUN domain contributes to "inhibition of PI3KC3 lipid kinase activity by Rubicon" [PMID:21062745, "negative regulator of PI3KC3 and autophagosome maturation"; PMID:21062745, "interacts with the PI3KC3 catalytic subunit hVps34 via its RUN domain"; PMID:21062745, "inhibition of PI3KC3 lipid kinase activity by Rubicon"]. UniProt also summarizes: "Inhibits PIK3C3 activity" and "negatively regulates PI3K complex II (PI3KC3-C2) function in autophagy" [file:human/RUBCN/RUBCN-uniprot.txt, "Inhibits PIK3C3 activity"; file:human/RUBCN/RUBCN-uniprot.txt, "negatively regulates PI3K complex II (PI3KC3-C2) function in autophagy"].

Rubicon also controls endosome maturation as a Rab7 effector. One paper states that Rubicon "prevents endosome maturation through differential interactions with Rab7 and UVRAG" and that it "sequesters UVRAG from C-VPS/HOPS" [PMID:20974968, "prevents endosome maturation through differential interactions with Rab7 and UVRAG"; PMID:20974968, "sequesters UVRAG from C-VPS/HOPS"]. A Rab7-domain paper reports that Rubicon and PLEKHM1 "specifically and directly interact with Rab7 via their RH domain" and that Rubicon uniquely regulates membrane trafficking by "simultaneously binding both Rab7 and PI3-kinase" [PMID:20943950, "specifically and directly interact with Rab7 via their RH domain"; PMID:20943950, "simultaneously binding both Rab7 and PI3-kinase"]. This supports negative regulation of endocytosis/endosome maturation and a non-core multivesicular body sorting context.

Subcellular location should be endosome/lysosome, not Golgi. UniProt states that Rubicon is "Predominantly located in late endosomes/lysosomes" and "not at all in the Golgi apparatus" [file:human/RUBCN/RUBCN-uniprot.txt, "Predominantly located in late endosomes/lysosomes"; file:human/RUBCN/RUBCN-uniprot.txt, "not at all in the Golgi apparatus"]. Therefore the negated `NOT colocalizes_with Golgi apparatus` row should be accepted; a positive Golgi annotation would not be supported.

Generic protein binding rows are mostly over-annotations. The useful annotations are PI3K inhibitor activity, PI3KC3-C2 association, Rab7/UVRAG regulatory context, and negative regulation of autophagosome/endosome maturation. Protein binding by itself loses the function.

## Falcon

Falcon deep research was run for RUBCN on 2026-06-02 but timed out after 600 seconds, and no `RUBCN-deep-research-falcon.md` report was produced. This review therefore uses the local GOA, UniProt, cached publication files, and the additional notes above.

## Description cleanup note

The YAML `description` field was revised to keep it as a standalone biological summary. Project-specific curation framing moved here instead.

- Moved out of the YAML description: the prior wording framed RUBCN in the Proteostasis Network context as a negative PI3KC3-C2/autophagosome maturation regulator rather than an autophagy activator, with UniProt pathogen/innate-immune interaction biology treated as non-core for the GOA rows.

## 2026-10-10 GOA refresh update (PTHR45971 family pass)

- GOA refresh added 25 GO:0005515 IPI rows. Policy: protein binding is never MARK_AS_OVER_ANNOTATED. Rows from the mechanistic papers (PMID:19270696, PMID:21062745) with PI3KC3-C2 subunits (BECN1, PIK3C3, PIK3R4, UVRAG) are now MODIFY to GO:0141039 phosphatidylinositol 3-kinase inhibitor activity [PMID:21062745 "inhibition of PI3KC3 lipid kinase activity by Rubicon"; PMID:19270693 "Rubicon reduces Vps34 activity and downregulates autophagy"]. All other protein-binding rows (interactome screens HuRI/BioPlex/OpenCell, EGFR, ORF3a, Beclin 2, Slamf1 studies) are REMOVE; removal does not imply the interactions are false.
- NEW GO:0031267 small GTPase binding (IDA, PMID:32632011): [PMID:32632011 "Rubicon-mediated inhibition of autophagy requires the interaction of the C-terminal Rubicon homology (RH) domain of Rubicon with Rab7-GTP"]; added as a second core function.
- GO:1901981 IBA (PTN002915557, Eukaryota root, seeded only by RUBCNL/Pacer) changed from KEEP_AS_NON_CORE to MARK_AS_OVER_ANNOTATED: [PMID:19270693 "Rubicon-EGFP was not pulled down by PtdIns(3)P-conjugated sepharose beads"]; [PMID:32632011 "Rubicon has not been reported to bind specifically to phospholipids"].
- A 2026 bioRxiv preprint (PMID:42845427) reports that the Rubicon PIKBD binds PI3KC3-C2 only via the BECN1 BARA domain [PMID:42845427 "Rubicon binds directly to PI3KC3-C2 only via the BARA domain of the BECN1 subunit"]; context only (preprint).
- Martinez et al. 2015 (PMID:26098576, LAP/NOX2) and 2016 (PMID:27096368, lupus-like disease) are retracted (PMID:38438803, PMID:36045298); not used as evidence. LAP/NOX2 involvement rests on other work (e.g. [PMID:22423966 "Rubicon is also an essential, positive regulator of the NADPH oxidase complex"]) and is treated as non-core; no NEW annotation proposed.
- Mouse ortholog reviewed in genes/mouse/Rubcn/.
