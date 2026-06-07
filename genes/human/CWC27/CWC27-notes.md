# CWC27 (Q6UX04) review notes

## Identity
- Gene: CWC27, HGNC:10664. UniProt Q6UX04, "Spliceosome-associated protein CWC27 homolog".
- Synonyms: NY-CO-10 (Antigen NY-CO-10), SDCCAG10 (Serologically defined colon cancer antigen 10).
- 472 aa. Domain architecture: N-terminal cyclophilin-type PPIase domain (~res 11-166) followed by a long disordered/coiled-coil C-terminal region (res ~206-472) [file:human/CWC27/CWC27-uniprot.txt].

## Core biology
CWC27 is the human ortholog of yeast Cwc27 and is a spliceosome-associated protein. As part of the spliceosome it functions in pre-mRNA splicing. It is recruited during activation as a component of the activated (Bact) spliceosome and is one of the first proteins released as the spliceosome matures toward the catalytic C complex.

- [PMID:29360106 "Structure of the human activated spliceosome in three conformational states", "two peptidyl prolyl isomerases (PPIs, NY-CO-10, and CypE)" ... "the late Bact complex no longer contains the splicing factors RNF113A (Cwc24 in yeast) and NY-CO-10 (Cwc27 in yeast) ... these two proteins only transiently associate with the spliceosome and are released during the Bact-to-B* transition"]. CWC27/NY-CO-10 is therefore a U2-type activated (Bact) spliceosome component; in the mature Bact complex the endonuclease-like domain of Prp8 directly binds NY-CO-10.
- CWC27 is also a component of the activated human minor (U12-dependent) spliceosome [PMID:33509932 "Structure of the activated human minor spliceosome"], supporting U12-type spliceosome membership and a role in splicing of U12-type introns.
- CWC27 is present in native purified spliceosomes (C-complex–enriched) used for 3D structural analysis [PMID:11991638]. This is the basis for the older catalytic step 2 spliceosome IDA/IC annotations, although the more detailed cryo-EM work (PMID:29360106) places CWC27 specifically in the activated B (Bact)/U2-type precatalytic-to-activated stage rather than acting in step 2 catalysis per se.
- CWC27 is part of the spliceosome activation machinery (Bact intermediates) [PMID:39068178 "Molecular basis for the activation of human spliceosome"].

## Catalytic (PPIase) status — pseudo-enzyme
The PPIase/cyclophilin domain of CWC27 is almost certainly catalytically inactive (a degenerate cyclophilin / pseudo-enzyme):
- [PMID:20676357 "Structural and biochemical characterization of the human cyclophilin family of peptidyl-prolyl isomerases", "No binding was detected for PPIL2, PPIL6, or SDCCAG-10, making these ... the first set of human cyclophilins that have been found incompetent to ligate cyclosporin"]. SDCCAG-10 = CWC27.
- [PMID:20676357 Table 1: "SDCCAG-10 ... no/no" for cyclosporin binding and tetrapeptide activity]. CWC27 showed neither cyclosporin binding nor isomerase activity against tetrapeptide substrates.
- Structural basis: CWC27 has a glutamic acid (Glu122) at the position equivalent to the catalytic Trp121 of PPIA; "glutamic acid in SDCCAG10" abrogates activity, and "Glutamic acid at this position seems to be incompatible with isomerase activity" [PMID:20676357]. The crystal structure (PDB 2HQ6, res 8-173) underlies this conclusion.
- UniProt curates CWC27 as "Probable inactive peptidyl-prolyl cis-trans isomerase" with a CAUTION: "Despite the fact that it belongs to the cyclophilin-type PPIase family, a report has shown that it has probably no peptidyl-prolyl cis-trans isomerase activity" [file:human/CWC27/CWC27-uniprot.txt].
- Consequently the GOA carries an explicit **NOT enables peptidyl-prolyl cis-trans isomerase activity** (GO:0003755, IDA, PMID:20676357). This negated annotation should be ACCEPTed; it correctly records the experimental finding of absent catalysis.

Implication for annotations:
- The InterPro2GO IEA transfer of **protein folding** (GO:0006457, GO_REF:0000002) is a family-level inference based on the cyclophilin/PPIase InterPro signature. Given that CWC27 is a demonstrated pseudo-PPIase with no isomerase/chaperone catalytic activity, this is an over-annotation (paralog/family transfer that ignores the loss of catalytic residues). MARK_AS_OVER_ANNOTATED.

## Disease
- Biallelic loss-of-function variants in CWC27 cause autosomal-recessive retinitis pigmentosa with or without skeletal/developmental anomalies (RPSKA; MIM:250410), including retinal degeneration, brachydactyly, short stature, craniofacial dysmorphism and neurologic defects [PMID:28285769 "Mutations in the spliceosome component CWC27 cause retinal degeneration with or without additional developmental anomalies"; summarized in UniProt DISEASE]. Truncating variants (e.g. p.7-472del, p.143-472del, p.206-472del, p.315-472del) underlie the phenotype. This supports an essential role in pre-mRNA splicing; no PMID_28285769 cached full text, so used UniProt as source.

## Localization
- Nuclear protein [file:human/CWC27/CWC27-uniprot.txt SUBCELLULAR LOCATION: Nucleus]. HPA IDA places it in the nucleoplasm (GO:0005654, GO_REF:0000052). Reactome TAS annotations also place it in nucleoplasm. Nuclear/nucleoplasm localization is consistent with a spliceosomal protein. ACCEPT nucleus/nucleoplasm.

## Annotation decisions summary
- Spliceosomal complex membership (GO:0005681, GO:0071013 catalytic step 2 spliceosome, GO:0071005 U2-type precatalytic spliceosome, GO:0071018 U12-type catalytic step 2 spliceosome): cellular_component annotations directly supported by structural/IPI evidence. The most strongly evidenced state from cryo-EM is the activated B (Bact)/U2-type precatalytic-to-activated spliceosome (PMID:29360106). KEEP. The IBA "catalytic step 2 spliceosome" transfer and older "catalytic step 2" IDA are broadly consistent with spliceosome membership; retained as non-core or accepted as appropriate.
- mRNA splicing, via spliceosome (GO:0000398): core biological process. ACCEPT.
- peptidyl-prolyl cis-trans isomerase activity (GO:0003755), NOT/negated: ACCEPT (correctly negated).
- protein folding (GO:0006457), IEA InterPro2GO: MARK_AS_OVER_ANNOTATED (pseudo-enzyme; catalytic chaperone/foldase activity not supported).
- nucleus (GO:0005634) IEA / nucleoplasm (GO:0005654) IDA & TAS: ACCEPT (nucleus) / KEEP.

## Possible better MF term
CWC27 acts as a cyclophilin-fold scaffold within the spliceosome rather than as an enzyme. There is no well-fitting catalytic MF. A non-catalytic structural/scaffolding role within the spliceosome is best captured by the CC (spliceosome complex) and BP (mRNA splicing) annotations; no confident replacement MF term is proposed. Note CWC27 pairs with CWC22 to position the EJC core factor eIF4A3 for deposition (from the broader literature / biological hint); this is a scaffolding/adaptor role but not directly evidenced in the cached publications, so no new MF term is asserted.
