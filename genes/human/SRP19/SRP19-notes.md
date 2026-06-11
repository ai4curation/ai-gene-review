# SRP19 (P09132, human) review notes

## Identity and overview
- UniProt P09132, SRP19_HUMAN, "Signal recognition particle 19 kDa protein", 144 aa, HGNC:11300, gene on chromosome 5.
- Member of the SRP19 family [file:human/SRP19/SRP19-uniprot.txt "Belongs to the SRP19 family"].
- Component of the signal recognition particle (SRP), a ribonucleoprotein that mediates cotranslational targeting of secretory/membrane proteins to the ER [file:human/SRP19/SRP19-uniprot.txt "Component of the signal recognition particle (SRP) complex, a ribonucleoprotein complex that mediates the cotranslational targeting of secretory and membrane proteins to the endoplasmic reticulum (ER)"].
- SRP19 binds directly to 7SL (SRP) RNA and mediates binding of SRP54 to the SRP complex [file:human/SRP19/SRP19-uniprot.txt "Binds directly to 7SL RNA (By similarity). Mediates binding of SRP54 to the SRP complex (By similarity)."].

## Core molecular function: SRP RNA binding / scaffolding required for SRP54 recruitment (S-domain assembly)
- SRP19 is a scaffolding protein that clamps helices 6 and 8 of SRP RNA, and this prepares the asymmetric loop of helix 8 for SRP54 binding [PMID:27899666 "SRP19 is a scaffolding protein clamping helices 6 and 8 of SRP RNA"] [PMID:27899666 "SRP19 binding to the apical tetra-nucleotide loops (tetraloops) of helices 6 and 8 prepares the flexible internal 'asymmetric loop' within helix 8 for SRP54 binding"].
- In vitro reconstitution shows SRP19 must bind SRP RNA before SRP54 can bind ("SRP54-late" assembly), effecting a conformational change in the RNA that promotes SRP54 binding [PMID:10618370 "in vitro reconstitution experiments showing that SRP19 must bind to SRP RNA before SRP54 binds"] [PMID:10618370 "SRP19 probably effects a conformational change in the SRP RNA that promotes SRP54 binding"].
- SRP19 is unstructured when free and folds (compact core + two extended RNA-binding loops) upon SRP RNA binding; SRP54 then binds the preformed SRP19-RNA complex forming a threefold RNA-protein interface [PMID:17434535 "The SRP19 protein is unstructured but forms a compact core domain and two extended RNA-binding loops upon binding the signal recognition particle (SRP) RNA. The SRP54 protein subsequently binds to the fully assembled SRP19-RNA complex"].
- SRP19 binds SRP RNA independently of other SRP proteins [PMID:10618370 "SRP19 protein is known to bind SRP RNA independently of other SRP proteins or factors"].
- This is an RNA-binding/scaffolding function, NOT a GTPase. The GTPase of SRP is SRP54 (and the SRP receptor SRalpha); SRP19 is not a GTPase. [PMID:27899666 "The heterodimeric targeting complex formed by the SRP GTPases SRP54 and SRalpha constitutes the core of the SRP system"]

## GO term mapping
- 7S RNA binding (GO:0008312) is the most specific MF term for the SRP RNA-binding activity, directly supported by IDA in PMID:27899666 (CAFA) and PMID:17434535. RNA binding (GO:0003723) is the parent; HDA (PMID:22658674 mRNA interactome capture) and DisProt IPI (PMID:17434535) annotations are to this generic parent.
- signal recognition particle / SRP, ER targeting (GO:0048500, GO:0005786) — SRP19 is a constitutive subunit of the 6-protein + 7SL RNA SRP [file:human/SRP19/SRP19-uniprot.txt "Component of a signal recognition particle complex that consists of a 7SL RNA molecule of 300 nucleotides and 6 protein subunits: SRP72, SRP68, SRP54, SRP19, SRP14 and SRP9"].
- SRP-dependent cotranslational protein targeting to membrane (GO:0006614) and the signal-sequence-recognition child (GO:0006617) and the older parent cotranslational protein targeting to membrane (GO:0006613) — all correct BP annotations.

## Subcellular location
- Cytoplasm / cytosol (site of SRP function) [file:human/SRP19/SRP19-uniprot.txt "SUBCELLULAR LOCATION: Cytoplasm"]. Experimental cytoplasm annotations from PMID:10618370 and PMID:11682607.
- Nucleus, nucleolus and nucleoplasm — SRP partially assembles in the nucleus/nucleolus; GFP-SRP19 shows prominent nucleolar plus nucleoplasmic localization [PMID:10618370 "GFP-SRP19 ... displayed prominent nucleolar localization as well as the cytoplasmic localization expected"] [PMID:10618370 "both of the GFP-SRP19 fusion proteins also were present in the nucleoplasm"]. SRP19 is actively imported to the nucleus by importin 8 and transportin [PMID:11682607 "the 19 kDa protein subunit of mammalian SRP, SRP19, was efficiently imported into the nucleus in vitro by two members of the importin beta superfamily of transport receptors, importin 8 and transportin"] [PMID:11682607 "a significant pool of endogenous SRP19 is located in the nucleus, as well as the nucleolus"].
- Nucleus/nucleolus are real but represent the assembly compartment, not the core ER-targeting site of action; keep as non-core localizations.

## ribosome binding (GO:0043022, contributes_to, IDA PMID:27899666)
- SRP72-RBD remodels the 5f-loop "involved in ribosome binding" and the paper concerns SRP RNA remodeling/ribosome interaction; SRP19 is one component clamping the RNA. SRP as a whole binds ribosomes. The contributes_to qualifier is appropriate (SRP19 contributes to the complex's ribosome binding). Keep as non-core. [PMID:27899666 "SRP72-RBD remodels the 5f-loop involved in ribosome binding"]

## protein binding (GO:0005515) IPI annotations
- PMID:33961781 (BioPlex / Huttlin dual proteome-scale network) and PMID:35271311 (OpenCell endogenous tagging) — both have WITH=UniProtKB:Q9UHB9 (SRP68). These capture the SRP19-SRP68 interaction within the SRP S domain. UniProt records this IntAct interaction: [file:human/SRP19/SRP19-uniprot.txt "P09132; Q9UHB9: SRP68; NbExp=6"]. Bare protein binding is uninformative per curation guidelines; keep as non-core (genuine interaction, but covered by SRP complex membership).

## PMID:1678319 (familial polyposis locus)
- This is the original positional cloning paper that mapped SRP19 near the APC locus on chromosome 5; one of the new genes "contained sequence identical to SRP19, the gene coding for the 19 kd component of the ribosomal signal recognition particle" [PMID:1678319 "One of the new genes contained sequence identical to SRP19, the gene coding for the 19 kd component of the ribosomal signal recognition particle"]. Used as the TAS source for SRP membership (GO:0005786) and cotranslational targeting (GO:0006613). The annotations are correct (SRP membership / cotranslational targeting), even though the paper's primary topic is the APC polyposis locus.

## PMID:18089836 (TAS-103 drug target screen) — IDA for SRP membership (GO:0005786)
- This drug-target paper found SRP as the target of TAS-103; it identified the SRP54 subunit as the binding protein, and showed TAS-103 disrupts SRP complex formation and reduces the amount of SRP14 and SRP19 [PMID:18089836 "TAS-103 disrupts SRP complex formation and reduces the amount of SRP14 and SRP19"]. SRP19 is detected as part of the SRP complex here; supports SRP membership (part_of GO:0005786). Per guidelines (do not REMOVE an IDA just because the abstract foregrounds SRP54), accept the SRP-membership annotation.

## PMID:34208095 (review, ComplexPortal NAS source)
- Review stating SRP19 functions to stabilize the 7SL structure: [PMID:34208095 "SRP19 functions to stabilize the 7SL structure"]. SRP is a six-protein + 7SL RNA complex with Alu and S domains; SRP19 binds in the S domain. Supports SRP membership and cotranslational targeting BP.

## Summary of core vs non-core
- CORE MF: 7S RNA binding (GO:0008312) — SRP RNA binding/scaffolding required for SRP54 recruitment and S-domain assembly.
- CORE complex: signal recognition particle (GO:0048500 / GO:0005786, part_of).
- CORE BP: SRP-dependent cotranslational protein targeting to membrane (GO:0006614 and children GO:0006617/GO:0006613).
- Non-core: generic RNA binding (GO:0003723, parent of 7S RNA binding); ribosome binding (contributes_to, complex-level); protein binding (IPI to SRP68); nucleus/nucleolus/nucleoplasm/cytoplasm localizations (assembly + steady-state compartments, not the defining ER-targeting site).
- No GTPase function (SRP19 is not a GTPase).
