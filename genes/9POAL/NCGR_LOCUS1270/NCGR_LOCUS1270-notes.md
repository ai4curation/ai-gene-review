# NCGR_LOCUS1270 (A0A811M8A5) - Chloroplastic Fructose-1,6-bisphosphatase

## Gene Identity

- **UniProt**: A0A811M8A5 (unreviewed/TrEMBL)
- **Species**: *Miscanthus lutarioriparius* (NCBI Taxon: 422564)
- **Enzyme**: Fructose-1,6-bisphosphatase, chloroplastic (EC 3.1.3.11)
- **Alternative name**: D-fructose-1,6-bisphosphate 1-phosphohydrolase
- **Gene name**: NCGR_LOCUS1270
- **Length**: 411 AA, includes N-terminal transit peptide region (residues ~1-60)
- **Family**: FBPase class 1 family (HAMAP: MF_01855; Pfam: PF00316 + PF18913)
- **Predicted structure**: Homotetramer (active form); regulated by disulfide/dithiol interconversion

## 1. Role of Chloroplastic FBPase in the Calvin-Benson Cycle

Chloroplastic FBPase (cpFBPase, also called cFBP1) catalyzes the irreversible hydrolysis of fructose-1,6-bisphosphate (FBP) to fructose-6-phosphate (F6P) and inorganic phosphate within the Calvin-Benson-Bassham (CBB) cycle. This is one of two irreversible phosphatase reactions in the CBB cycle (the other being catalyzed by sedoheptulose-1,7-bisphosphatase, SBPase).

cpFBPase occupies a critical branch point in the CBB cycle: it controls the partitioning of carbon between RuBP regeneration and output of fixed carbon (as starch within the chloroplast or as triose-phosphate exported for sucrose synthesis in the cytosol) [PMID:16415064 "FBPase contributes to the partitioning of the fixed carbon for RuBP regeneration or starch synthesis"]. Overexpression of cyanobacterial FBPase/SBPase in tobacco chloroplasts increased photosynthetic CO2 fixation 1.24-fold and dry matter 1.5-fold [PMID:11581664 "expression of a single plastid-targeted enzyme has been shown to improve carbon fixation and growth in transgenic plants"]. Transgenic plants with enhanced chloroplastic FBPase showed increased starch in source leaves and higher RuBP levels [PMID:16415064 "TpF-11 plants with 2.3-fold higher FBPase activity... the amount of final dry matter was approximately 1.3-fold higher"].

The enzyme is essential for photoautotrophic growth. In cyanobacteria, mutants lacking the combined SBP/FBPase protein cannot grow photoautotrophically [PMID:36518499 "Mutants lacking the gene coding for SBP/FBPase protein are not able to grow photoautotrophically and require glucose to survive"]. Antisense reduction of chloroplastic FBPase in potato resulted in reduced photosynthetic assimilation rates, with saturation at much lower light intensities [PMID:10467036 "assimilation rates of the FBPase antisense plants were significantly reduced... Saturation of assimilation rates in transgenic plants occurred at a photon flux density of 200 micromol m-2 s-1"].

## 2. Chloroplastic vs. Cytosolic FBPase: Different Genes, Regulation, Pathways

The chloroplastic and cytosolic FBPase isoforms are encoded by **distinct genes** that arose through an ancient gene duplication early in eukaryotic evolution [PMID:8980497 "Chloroplast and cytosolic FBP isoenzymes of higher plants arose through a gene duplication event which occurred early in eukaryotic evolution"].

### Key differences:

| Feature | Chloroplastic FBPase (cpFBPase/cFBP1) | Cytosolic FBPase (cyFBPase) |
|---------|---------------------------------------|----------------------------|
| **Pathway** | Calvin-Benson cycle (CO2 fixation) | Sucrose biosynthesis; gluconeogenesis |
| **Localization** | Chloroplast stroma | Cytosol |
| **Regulation** | Redox-regulated by thioredoxin f; light-activated | Allosteric inhibition by fructose-2,6-bisphosphate and AMP |
| **Key regulatory feature** | Contains "loop 170" with regulatory Cys residues forming disulfide bridge | Lacks redox regulatory domain; regulated like mammalian/yeast FBPase |
| **pH optimum** | Alkaline (pH ~8.0-8.3, matching illuminated stroma) | Near-neutral |
| **Metal requirement** | Mg2+ (high concentration, reflecting stromal Mg2+ in light) | Mg2+ (lower concentration) |

The cytosolic FBPase shares higher sequence similarity with mammalian gluconeogenic FBPase than with the chloroplastic isoform from the same plant [PMID:24317825 "There is slightly higher similarity between mammalian FBPase and plant cytosolic FBPase than there is between the two plant FBPases"]. The kinetic and allosteric properties of the plant cytosolic FBPase "are remarkably similar to the mammalian and yeast FBPase, but differ greatly from those of the chloroplastic FBPase" [PMID:24317825].

The review by Serrato et al. (2009) provides a comprehensive overview of both isoforms in sugar partitioning, emphasizing their distinct regulatory mechanisms and the consequences of compartmentalization for plant metabolism [PMID:19325167 "The existence of two well-characterized isoforms is a consequence of the subcellular compartmentalization of photosynthetic eukaryotes, conditioning their respective regulatory mechanisms"].

## 3. Is cpFBPase Involved in Sucrose Biosynthesis? -- NO

**Sucrose biosynthesis is a cytosolic process.** The pathway for sucrose synthesis involves:
1. Export of triose-phosphates from the chloroplast via the triose-phosphate/phosphate translocator
2. Conversion to fructose-1,6-bisphosphate (by aldolase) in the cytosol
3. Dephosphorylation by **cytosolic FBPase** to fructose-6-phosphate
4. Conversion to glucose-6-phosphate, then glucose-1-phosphate, then UDP-glucose
5. Sucrose-phosphate synthase + sucrose-phosphate phosphatase produce sucrose

The chloroplastic FBPase operates within the chloroplast stroma and is NOT directly involved in sucrose biosynthesis. Loss of cytosolic FBPase in rice caused dramatically decreased sucrose levels and severe growth retardation [PMID:18811733 "OscFBP1 plays a major role in the cytosolic conversion of trioseP to sucrose in leaves during the day... oscfbp1 mutants exhibited markedly decreased photosynthetic rates and severe growth retardation with reduced chlorophyll content"]. This demonstrates that sucrose biosynthesis depends on the **cytosolic** isoform, not the chloroplastic one.

The GO annotation GO:0005986 (sucrose biosynthetic process) assigned by TreeGrafter to this chloroplastic FBPase is therefore **incorrect** -- this annotation likely results from the automated pipeline failing to distinguish between the two isoforms.

## 4. Subcellular Localization: Chloroplast Stroma

cpFBPase is localized to the **chloroplast stroma**. This has been demonstrated by:

- The UniProt entry states "Plastid, chloroplast" (ECO:0000256, ARBA:ARBA00004229)
- The N-terminal sequence (residues ~1-60 of this 411 AA protein) contains a predicted chloroplast transit peptide, consistent with stromal targeting
- Immunolocalization experiments on cpFBPaseII (a related chloroplastic isoform) confirmed stromal localization [PMID:19220782 "Immunolocalization experiments and chloroplast isolation confirmed that the new isoenzyme is located in the stroma"]
- The enzyme responds to stromal pH changes from ~7 (dark) to ~8 (light) which regulate its activity [PMID:6096140 "Since illumination brings about a pH rise of chloroplastic stroma from 7 to 8, the above results suggest that light activation of fructose bisphosphatase is at least in part due to a slow conformation change"]
- A recent study showed that active cFBP1 functions as a dimer specifically at the alkaline pH values that occur in illuminated chloroplast stroma [PMID:40485148 "active cFBP1 is strictly dimeric at pH values occurring in illuminated chloroplasts"]

The most specific GO CC term should be **GO:0009570 (chloroplast stroma)**, not just GO:0009507 (chloroplast).

**The GO:0005829 (cytosol) annotation from TreeGrafter is INCORRECT for this protein.** The cytosolic localization applies to the cytosolic FBPase isoform, not the chloroplastic one. TreeGrafter likely propagated this from an ancestor node that included both isoforms.

## 5. Is cpFBPase Involved in Gluconeogenesis? -- NO

Gluconeogenesis is a cytosolic/mitochondrial pathway that converts non-carbohydrate precursors (pyruvate, amino acids, etc.) to glucose. In plants, the **cytosolic FBPase** participates in gluconeogenesis, analogous to the mammalian liver enzyme [PMID:24317825 "In non-photosynthetic tissues, it regulates the rate of gluconeogenesis"].

The chloroplastic FBPase functions exclusively in the Calvin-Benson cycle within the chloroplast. The structural study of oxidized pea cpFBPase explicitly noted that "regulation of plant FBPases by thiol-disulfide interchange differs in every respect from the regulation of mammalian gluconeogenic FBPases by AMP" [PMID:10581254].

The GO annotation GO:0006094 (gluconeogenesis) assigned by TreeGrafter is therefore **incorrect** for this chloroplastic isoform -- it should only apply to the cytosolic FBPase.

## 6. Fructose Metabolic Process, Fructose 6-Phosphate Metabolic Process

- **GO:0006000 (fructose metabolic process)**: This is a very broad term. While cpFBPase does catalyze a reaction involving a fructose derivative (FBP to F6P), the biological process is the Calvin cycle, not "fructose metabolism" per se. The F6P produced by cpFBPase in the Calvin cycle is isomerized to glucose-6-phosphate and then used for RuBP regeneration or starch synthesis. This annotation is **overly vague** and not informative for a Calvin cycle enzyme.

- **GO:0006002 (fructose 6-phosphate metabolic process)**: Technically accurate in that the enzyme produces F6P, but again, using this term without the Calvin cycle context is misleading. The reductive pentose-phosphate cycle (GO:0019253) is the appropriate biological process term.

- **GO:0030388 (fructose 1,6-bisphosphate metabolic process)**: Similar -- technically the enzyme acts on FBP, but this is in the context of the Calvin cycle. This is an acceptable secondary annotation but less informative than the primary Calvin cycle annotation.

## 7. Is Cytosol an Appropriate Localization for cpFBPase? -- NO

**GO:0005829 (cytosol) is NOT appropriate for this chloroplastic protein.** The protein has a clear chloroplast transit peptide (N-terminal ~60 residues), is annotated by UniProt as chloroplast-localized (ARBA), classified in FunFam 3.30.540.10:FF:000014 as "Fructose-1,6-bisphosphatase, chloroplastic", and the HAMAP family MF_01855 (FBPase_class1) covers chloroplastic forms.

The cytosol annotation from TreeGrafter (GO_REF:0000118) is an error from automated phylogenetic propagation. The PANTHER family PTHR11556 includes both chloroplastic and cytosolic FBPases, and the annotation was likely inherited from an ancestral node without proper isoform distinction.

## 8. Regulatory Mechanisms

### Thioredoxin-mediated redox regulation (primary mechanism)

cpFBPase is one of the best-characterized targets of the ferredoxin/thioredoxin (Fd/Trx) system in chloroplasts [PMID:18377232 "Forty years ago, ferredoxin was shown to activate fructose 1,6-bisphosphatase in illuminated chloroplast preparations, thereby laying the foundation for the field now known as redox biology"].

The regulatory mechanism:
1. Light drives photosynthetic electron transport
2. Reduced ferredoxin is produced by PSI
3. Ferredoxin:thioredoxin reductase (FTR) reduces thioredoxin f
4. Thioredoxin f reduces the regulatory disulfide bridge in cpFBPase (Cys153-Cys173 in pea)
5. Reduction activates the enzyme

In darkness, cpFBPase is oxidized (disulfide formed) and inactive, preventing futile cycling with phosphofructokinase [PMID:6260483 "Activation by light of spinach fructose-1,6-bisphosphatase is mimicked by dithiothreitol. This process of activation by dithiothreitol implies the specific reduction of two disulfide bridges and a conformation change"].

The type-f thioredoxins are the primary reductants for cpFBPase. In Arabidopsis trxf1f2 double mutants, FBPase showed "retarded and incomplete reduction... upon illumination" and carbon fixation activation was delayed [PMID:26842981 "fructose 1,6-bisphosphatase and Rubisco activase showed retarded and incomplete reduction in the double mutant upon illumination"].

The redox states of FBPase and SBPase are linearly correlated with photosynthetic electron transport rates [PMID:38305687 "the redox states of FBPase and SBPase were linearly correlated with electron transport rates"].

### S-nitrosylation

cpFBPase is also regulated by S-nitrosylation in pea, specifically at Cys153. This occurs during the light period and triggers formation of the regulatory disulfide, providing an additional layer of redox regulation [PMID:29059554 "cFBP1 S-nitrosylation only occurs during the light period and we have elucidated by activity assays with Cys-to-Ser mutants that this enzyme may be inactivated through the S-nitrosylation of Cys153"].

### 2-Cys peroxiredoxin modulation

Native 2-Cys peroxiredoxin stimulates cpFBPase activity through a non-reductive mechanism requiring both FBP and Ca2+, distinct from the thioredoxin-mediated activation [PMID:17307139 "the native and the recombinant forms of rapeseed leaves stimulate the activity of chloroplast fructose-1,6-bisphosphatase... The absence of reductants, the strict requirement of both fructose 1,6-bisphosphate and Ca2+... bring forward clear differences with the well-known stimulation mediated by reduced thioredoxin"].

### pH regulation

Illumination raises stromal pH from ~7 to ~8, which promotes cpFBPase activation through a conformational transition [PMID:6096140]. A recent study demonstrated that Cys95 mediates pH-driven structural changes: at pH 8.3 (illuminated stroma), cFBP1 is active as a dimer; at pH 7.0, it forms inactive tetramers [PMID:40485148 "active cFBP1 is strictly dimeric at pH values occurring in illuminated chloroplasts and Cys95 is an important determinant of the stromal pH-driven structure and activity"].

### Dark inactivation

CBSX2 participates in the oxidation (inactivation) of cpFBPase during dark transitions [PMID:38028645 "the redox states of the Calvin cycle enzymes FBPase and SBPase in cbsx2 were similar to those of CF-gamma during light/dark transitions"].

## 9. cpFBPase in C4 Plants

### C4 photosynthetic context

In C4 plants (NADP-ME subtype, including Miscanthus, maize, sugarcane, sorghum), the Calvin-Benson cycle operates primarily in the **bundle sheath cell chloroplasts**. CO2 is initially fixed in mesophyll cells by PEP carboxylase, transported as C4 acids to bundle sheath cells, decarboxylated to release CO2, and this concentrated CO2 is then fixed by Rubisco in the bundle sheath chloroplast CBB cycle.

In maize, chloroplastic FBPase is **primarily located in bundle sheath cells**, with large (5-fold) light activation observed in isolated bundle sheath strands versus little light activation in mesophyll protoplasts [PMID:16663806 "There was a large (5-fold) light activation of FBPase in isolated bundle sheath strands of maize, whereas there was little light activation of the enzyme in isolated mesophyll protoplasts... The results suggest the chloroplastic FBPase in maize is primarily located in the bundle sheath cells"]. In mesophyll protoplasts, FBPase was largely cytoplasmic (cytosolic isoform for sucrose synthesis).

### C4 models and Miscanthus

Miscanthus x giganteus and related species (including M. lutarioriparius) are NADP-malic enzyme subtype C4 grasses [PMID:20693355 "S. viridis uses an NADP-malic enzyme subtype C4 photosynthetic system to fix carbon"]. The C4 photosynthesis model has been parameterized for this group [PMID:34173821 "C4 crops such as maize and sorghum are major contributors to food production... the C4 grasses sugarcane, miscanthus, and switchgrass are major plant sources of bioenergy"].

Photosynthetic efficiency in Miscanthus has been studied in the context of chilling tolerance, light responses, and bundle sheath conductance [PMID:26714623, PMID:22812384], though these studies focused on PEPCase, Rubisco, and PPDK rather than cpFBPase specifically.

## 10. Publications on M. lutarioriparius cpFBPase

**No publications were found specifically about chloroplastic FBPase in M. lutarioriparius.** The protein A0A811M8A5 derives from the whole genome shotgun sequence of M. lutarioriparius submitted by Han et al. (2020) to EMBL/GenBank/DDBJ databases.

Transcriptomic studies of M. lutarioriparius exist but focus on rhizome development [PMID:28446913] and secondary cell wall biosynthesis [PMID:28831170], not on Calvin cycle enzymes.

Given the close phylogenetic relationship of Miscanthus to maize, sorghum, and sugarcane (all Andropogoneae), the functional properties of cpFBPase can be reasonably inferred from studies in these related C4 grasses.

## Summary of Annotation Issues for GO Review

### Annotations that are CORRECT:
- **GO:0042132** (fructose 1,6-bisphosphate 1-phosphatase activity) -- MF, correct
- **GO:0046872** (metal ion binding) -- MF, correct (Mg2+ cofactor)
- **GO:0019253** (reductive pentose-phosphate cycle) -- BP, correct (Calvin cycle)
- **GO:0009507** (chloroplast) -- CC, correct but could be more specific (GO:0009570 chloroplast stroma)
- **GO:0016791** (phosphatase activity) -- MF, correct but very general
- **GO:0042578** (phosphoric ester hydrolase activity) -- MF, correct but general

### Annotations that are INCORRECT (likely TreeGrafter isoform confusion):
- **GO:0005986** (sucrose biosynthetic process) -- INCORRECT: sucrose synthesis is cytosolic, mediated by cytosolic FBPase
- **GO:0006094** (gluconeogenesis) -- INCORRECT: gluconeogenesis is a cytosolic pathway using cytosolic FBPase
- **GO:0005829** (cytosol) -- INCORRECT: this is a chloroplastic protein, not cytosolic
- **GO:0005737** (cytoplasm) -- INCORRECT: TreeGrafter annotation, likely inherited from cytosolic isoform

### Annotations that are QUESTIONABLE/OVER-ANNOTATED:
- **GO:0006000** (fructose metabolic process) -- overly vague; the relevant process is the Calvin cycle
- **GO:0006002** (fructose 6-phosphate metabolic process) -- technically true but misleading without Calvin cycle context
- **GO:0030388** (fructose 1,6-bisphosphate metabolic process) -- acceptable as secondary annotation
- **GO:0005975** (carbohydrate metabolic process) -- very broad, not informative

### Proposed additions:
- **GO:0009570** (chloroplast stroma) -- more specific localization
- **GO:0019253** (reductive pentose-phosphate cycle) -- already present from UniProtKB-KW, should be primary BP annotation

## References

Based on articles retrieved from PubMed:

- PMID:6260483 [DOI](https://doi.org/10.1111/j.1432-1033.1981.tb05092.x) - Pradel et al. 1981. Activation of spinach chloroplast FBPase.
- PMID:6260484 [DOI](https://doi.org/10.1111/j.1432-1033.1981.tb05093.x) - Meunier et al. 1981. Substrate-binding isotherms of spinach cpFBPase.
- PMID:6096140 [DOI](https://doi.org/10.1111/j.1432-1033.1984.tb08582.x) - Gontero et al. 1984. pH-induced conformational transition of cpFBPase.
- PMID:16663806 [DOI](https://doi.org/10.1104/pp.76.1.238) - Usuda et al. 1984. FBPase activation in maize bundle sheath vs mesophyll.
- PMID:8980497 [DOI](https://doi.org/10.1007/BF00019100) - Martin et al. 1996. Evolution of chloroplast and cytosolic FBPase.
- PMID:24317825 [DOI](https://doi.org/10.1007/BF00015056) - Daie 1993. Cytosolic FBPase in sucrose biosynthesis.
- PMID:10581254 [DOI](https://doi.org/10.1093/emboj/18.23.6809) - Chiadmi et al. 1999. Crystal structure of oxidized pea cpFBPase.
- PMID:10467036 [DOI](https://doi.org/10.1007/s004250050611) - Muschak et al. 1999. cpFBPase antisense potato.
- PMID:11581664 [DOI](https://doi.org/10.1038/nbt1001-965) - Miyagawa et al. 2001. Cyanobacterial FBPase/SBPase in tobacco.
- PMID:11917127 [DOI](https://doi.org/10.1073/pnas.072137099) - Andralojc et al. 2002. cpFBPase and 2-carboxyarabinitol 1-phosphate.
- PMID:15448173 [DOI](https://doi.org/10.1093/jxb/erh257) - Sahrawy et al. 2004. cpFBPase antisense in Arabidopsis.
- PMID:16415064 [DOI](https://doi.org/10.1093/pcp/pcj004) - Tamoi et al. 2006. FBPase and SBPase in Calvin cycle flux.
- PMID:17307139 [DOI](https://doi.org/10.1016/j.bbrc.2007.02.013) - Caporaletti et al. 2007. 2-Cys Prx modulation of cpFBPase.
- PMID:18377232 [DOI](https://doi.org/10.1089/ars.2007.1931) - Schurmann & Buchanan 2008. Ferredoxin/thioredoxin system review.
- PMID:18811733 [DOI](https://doi.org/10.1111/j.1365-3040.2008.01890.x) - Lee et al. 2008. Cytosolic FBPase loss in rice.
- PMID:19220782 [DOI](https://doi.org/10.1111/j.1365-3040.2009.01960.x) - Serrato et al. 2009. cpFBPaseII, redox-independent isoform.
- PMID:19325167 [DOI](https://doi.org/10.1093/jxb/erp066) - Serrato et al. 2009. FBPase-manipulated plants review.
- PMID:20693355 [DOI](https://doi.org/10.1105/tpc.110.075309) - Brutnell et al. 2010. Setaria viridis as C4 model.
- PMID:22812384 [DOI](https://doi.org/10.1111/j.1365-3040.2012.02579.x) - Ubierna et al. 2012. C4 efficiency in Miscanthus x giganteus.
- PMID:26714623 [DOI](https://doi.org/10.1111/pce.12699) - Friesen & Sage 2016. Chilling effects on Miscanthus photosynthesis.
- PMID:26842981 [DOI](https://doi.org/10.1093/jxb/erw017) - Naranjo et al. 2016. Trx f mutants and FBPase activation.
- PMID:29059554 [DOI](https://doi.org/10.1016/j.redox.2017.10.008) - Serrato et al. 2017. S-nitrosylation of cpFBPase.
- PMID:28446913 [DOI](https://doi.org/10.3389/fpls.2017.00492) - Hu et al. 2017. M. lutarioriparius transcriptome.
- PMID:28831170 [DOI](https://doi.org/10.1038/s41598-017-08690-8) - Hu et al. 2017. M. lutarioriparius secondary cell wall transcriptome.
- PMID:34173821 [DOI](https://doi.org/10.1093/jxb/erab266) - von Caemmerer 2021. C4 photosynthesis model.
- PMID:36518499 [DOI](https://doi.org/10.3389/fpls.2022.1052019) - Garcia-Canas et al. 2022. TrxF-FBPase-SBPase in cyanobacteria.
- PMID:33664754 [DOI](https://doi.org/10.3389/fpls.2021.530376) - Murai et al. 2021. CBSX proteins and Trx system.
- PMID:38305687 [DOI](https://doi.org/10.1093/pcp/pcae013) - Yoshida & Hisabori 2024. FBPase redox and electron transport.
- PMID:38028645 [DOI](https://doi.org/10.1002/pld3.542) - Li et al. 2023. CBSX2 and dark oxidation of cpFBPase.
- PMID:40485148 [DOI](https://doi.org/10.1111/pce.15667) - Gamez-Arcas et al. 2025. Cys95 and pH-driven cpFBPase structure.
