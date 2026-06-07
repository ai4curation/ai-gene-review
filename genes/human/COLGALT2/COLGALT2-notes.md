# COLGALT2 (Q8IYK4) review notes

## Identity
- Gene: COLGALT2 (HGNC:16790); synonyms C1orf17, GLT25D2, KIAA0584.
- Protein: Procollagen galactosyltransferase 2 / Collagen beta(1-O)galactosyltransferase 2 (ColGalT 2) / Glycosyltransferase 25 family member 2 / Hydroxylysine galactosyltransferase 2.
- UniProt RecName lists EC=2.4.1.50 [file:human/COLGALT2/COLGALT2-uniprot.txt "EC=2.4.1.50 {ECO:0000269|PubMed:19075007}"].
- 626 aa precursor, signal peptide 1..27, C-terminal "...SRDEL" ER-retention motif (623..626, "Prevents secretion from ER", PROSITE PRU10138) [file:human/COLGALT2/COLGALT2-uniprot.txt].
- CAZy family GT25; belongs to the glycosyltransferase 25 family [file:human/COLGALT2/COLGALT2-uniprot.txt "Belongs to the glycosyltransferase 25 family"].
- Paralog of COLGALT1 (Q8NBJ5).

## Function
- "Beta-galactosyltransferase that transfers beta-galactose to hydroxylysine residues of collagen." [file:human/COLGALT2/COLGALT2-uniprot.txt FUNCTION, ECO:0000269|PubMed:19075007].
- Catalytic activity: (5R)-5-hydroxy-L-lysyl-[collagen] + UDP-alpha-D-galactose = (5R)-5-O-(beta-D-galactosyl)-5-hydroxy-L-lysyl-[collagen] + UDP + H(+); RHEA:12637; EC 2.4.1.50 [file:human/COLGALT2/COLGALT2-uniprot.txt CATALYTIC ACTIVITY].
- This is the first step of collagen O-glycosylation (Gal-O-Hyl), preceding glucosylation to form Glc-Gal-O-Hyl. Original characterization: Schegg B et al., Mol Cell Biol 2009 (PMID:19075007), "Core glycosylation of collagen is initiated by two beta(1-O)galactosyltransferases." (paper not cached in repo).
- Kinetics: KM=33.5 uM for UDP-galactose [file:human/COLGALT2/COLGALT2-uniprot.txt BIOPHYSICOCHEMICAL PROPERTIES, ECO:0000269|PubMed:19075007].
- CAUTION: Has no glucosyltransferase activity [file:human/COLGALT2/COLGALT2-uniprot.txt "Has no glucosyltransferase activity"].
- Mn2+-dependent: GT25 collagen galactosyltransferases are manganese-dependent (DXD motif metal coordination). Note: a manganese binding GO annotation is NOT present in the current GOA; established for the family/paralog in the literature.

## Localization
- SUBCELLULAR LOCATION: Endoplasmic reticulum lumen [file:human/COLGALT2/COLGALT2-uniprot.txt SUBCELLULAR LOCATION, ECO:0000255|PROSITE-ProRule:PRU10138]. Consistent with soluble ER-luminal enzyme bearing a C-terminal ...DEL ER-retention signal. The paralog GLT25D1/COLGALT1 was shown to be a soluble ER-localized protein (PMID:20470363).

## Tissue specificity
- "Expressed in brain and skeletal muscle." [file:human/COLGALT2/COLGALT2-uniprot.txt TISSUE SPECIFICITY, ECO:0000269|PubMed:19075007]. HPA: tissue enhanced (brain). More restricted expression than ubiquitous COLGALT1.

## Existing GO annotations (GOA)
- GO:0050211 procollagen galactosyltransferase activity — IBA (GO_REF:0000033), IEA (GO_REF:0000120, RHEA/EC), TAS (Reactome R-HSA-1981120). Core MF; well supported by direct biochemistry (PMID:19075007) and EC mapping. ACCEPT.
- GO:0005788 endoplasmic reticulum lumen — IEA (GO_REF:0000044 SubCell mapping) and TAS (Reactome x3). Core CC consistent with UniProt SUBCELLULAR LOCATION and DEL retention motif. ACCEPT one as representative.
- GO:0030199 collagen fibril organization — TAS Reactome (R-HSA-1650814). BP; downstream/pathway-level. COLGALT2 contributes to collagen biosynthesis/modification but a direct role in fibril organization is indirect. Keep as non-core.
- GO:0005515 protein binding — IPI, 4 separate high-throughput interactome papers (PMID:25416956 Rolland; PMID:28514442 Luck/Huttlin community map; PMID:32296183 Luck HuRI; PMID:33961781 BioPlex). Interactors are heterogeneous (C1QTNF3, HPCAL1, SEMG1, UBQLN1, UBQLN2 per UniProt INTERACTION) and not functionally informative. Bare "protein binding" is uninformative -> MARK_AS_OVER_ANNOTATED.

## Interactions (UniProt INTERACTION block)
- C1QTNF3 (Q9BXJ4), HPCAL1 (P37235), SEMG1 (P04279), UBQLN1 (Q9UMX0-2), UBQLN2 (Q9UHD9). These derive from binary interactome screens; no validated functional partnership relevant to galactosyltransferase activity.

## Decisions summary
- ACCEPT: galactosyltransferase activity (GO:0050211), ER lumen (GO:0005788).
- KEEP_AS_NON_CORE: collagen fibril organization (GO:0030199) — pathway-level/indirect.
- MARK_AS_OVER_ANNOTATED: all GO:0005515 protein binding (uninformative, HT interactome).
- Core function: collagen hydroxylysine galactosyltransferase (Gal-O-Hyl), first step of collagen O-glycosylation, in the ER lumen, Mn2+-dependent.
