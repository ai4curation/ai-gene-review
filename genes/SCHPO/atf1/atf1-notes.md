# atf1 (P52890, SPBC29B5.01) review notes

S. pombe Atf1 (synonyms gad7, mts1, sss1). bZIP ATF/CREB-family transcription factor; principal nuclear substrate of the Sty1/Spc1 SAPK (p38) MAP kinase. Heterodimerizes with Pcr1 (mts2).

## Core identity / molecular function
- bZIP TF homologous to mammalian ATF-2/CRE-BP1; binds ATF/CRE recognition sites in vitro; ATF-like binding activity in pombe extracts entirely lost on atf1 deletion [PMID:8557039 "contains a bZIP domain at its C-terminus with strong homology to members of the ATF/CREB family of mammalian factors and in vitro binds specifically to ATF/CRE recognition sites. Furthermore the ATF-like binding activity detected in extracts from fission yeast cells is entirely lost upon deletion of the atf1+ gene"].
- gad7/Atf1 binds CRE in vitro; co-IP with Pcr1 => heterodimer in vivo [PMID:9135083 "could bind to the CRE (cAMP response element) sequence in vitro. ... Gad7 was co-immunoprecipitated with another bZIP protein Pcr1, suggesting that the two proteins form a heterodimer in vivo"].
- Atf1-Pcr1 heterodimer binds M26 site (5'-ATGACGT-3') with Kd ~1 nM [PMID:18375981 "The Atf1-Pcr1 heterodimer binds avidly (Kd ∼1 nM) to a DNA site called M26 (5′-ATGACGT-3′)"].
- Heterodimer Mts1(70 kD)/Mts2(28 kD) purified 40,000-fold, binds M26; binding in vitro correlates with hotspot activity in vivo [PMID:7958849 "purified 40,000-fold a heteromeric protein, containing polypeptides Mts1 (70 kD) and Mts2 (28 kD), that binds to the M26 site. Binding in vitro strictly correlates with hot spot activity in vivo"].
- Atf1 acts as both activator and repressor depending on context (M26-chromatin remodeling) [PMID:15448137 "Atf1-Pcr1 heterodimer can function differentially as either a transcriptional activator, or as a transcriptional repressor, or as an inducer of meiotic recombination"].

## Localization
- Nucleus (UniProt). Nuclear retention of Spc1 requires Atf1; nuclear localization of Atf1 requires Pcr1 [PMID:9585506 "Nuclear retention of Spc1 requires Atf1, a transcription factor that is the key nuclear substrate of Spc1. Nuclear localization of Atf1 requires Pcr1"].
- ORFeome global localization study: nuclear [PMID:16823372 - genome-wide localization].

## Stress response (core BP)
- Sty1-dependent target; deletion of atf1 phenocopies many sty1 defects (stress sensitivity, sterility); induces gpd1, ctt1(catalase), pyp2 directly [PMID:8824588 "Deletion of the atf1+ gene results in many, but not all, of the phenotypes associated with loss of Sty1, including sensitivity to environmental stress and inability to undergo sexual conjugation ... These genes include gpd1+ ... the catalase gene ... and pyp2+ ... Induction of Pyp2 by Atf1 is direct ... Atf1 associates stably and is phosphorylated by the Sty1 kinase in vitro"].
- Conjugation, meiosis, osmotic stress regulated by Spc1 through Atf1; Atf1 required for induction of meiotic and stress genes gpd1, pyp2 [PMID:8824587 "Atf1 is required for induction of meiotic genes and stress-response genes, such as gpd1+ and pyp2+, that are transcriptionally regulated by Spc1"].
- ~400-500 stress genes regulated [PMID:25122751 "the MAP kinase Sty1 and the basic leucine zipper (bZIP) transcription factor (TF) Atf1 regulate up to 400 genes in response to several stress conditions"].
- Catalase ctt1: Atf1 + its binding site needed for induction by osmotic stress, UV, heat shock (NOT oxidative/menadione, which is Pap1) [PMID:10731689 "A transcription factor, Atf1, and its binding site are necessary for the induction of ctt1(+) by osmotic stress, UV irradiation, and heat shock"].
- Neutral trehalase ntp1 heat induction via CRE-like element, Atf1-dependent [PMID:15164362 "a CRE-like element as the target for Atf1p-mediated expression under thermal stress"].
- Ecl1 (extender of chronological lifespan) directly activated by Atf1 on H2O2; Atf1 binds upstream of ecl1 [PMID:24696293 "the bZip transcription factor Atf1 is a direct activator of the induction of ... ecl1 (+) by H(2)O(2) stress. Based on ChIP analysis, we identified that Atf1 binds to the upstream DNA region of ecl1(+)"].
- Phosphorylation of Atf1 by Sty1 required for oxidative stress response via promoting transcription initiation, NOT DNA binding [PMID:28652406 "Sty1-mediated Atf1 phosphorylation does not stimulate binding of Atf1 to DNA but, rather, establishes a platform of interactions with the basal transcriptional machinery to facilitate transcription initiation"].
- Salt/cation stress: cta3 induction requires Sty1, Atf1, Prr1 (Tup-repressor controlled) [PMID:12221110 "relief from repression requires the Sty1, Atf1, and Prr1"].
- ecm33 target of Atf1 and Mbx1 (Pmk1 cell integrity pathway) [PMID:20032302 "ecm33(+), which encodes a glycosyl-phosphatidylinositol (GPI)-anchored cell surface protein as a transcriptional target of Pmk1 and Atf1"].
- agl1 (extracellular maltase) induced on glucose->maltose switch, dependent on Atf1+Pcr1; they recruit Mediator [PMID:24224056 "Transcription of agl1 was induced when the carbon source was changed from glucose to maltose. This was dependent on Atf1 and Pcr1 ... the association of Mediator with these genes was dependent on Atf1 and Pcr1"].
- Ish1/Bis1 (stationary-phase/nuclear envelope): ish1 expression regulated by Spc1 through Atf1 [PMID:11751918 "Expression of Ish1 is regulated by the Spc1 MAPK pathway through the Atf1 transcription factor"].
- Sro1 stress-responsive orphan regulated via Sty1/Atf1 [PMID:18410345 "the expression of the gene is regulated mainly through the stress activated protein kinase (SAPK) Sty1 and its downstream transcription factor Atf1"].

## Sexual development / stationary phase
- Required for sexual development and entry into stationary phase; activates ste11; G1 arrest under N starvation [PMID:8557039 "a transcription factor required for sexual development and entry into stationary phase ... the induction of ste11+ expression is lost"].
- gad7 required for proper G1 arrest and ste11 induction under N starvation [PMID:9135083 "required for proper G1 arrest and gene expression under nitrogen starvation ... Expression of ste11 ... was not inducible in the disruptant"].
- cgs2 chromatin remodeling links SAPK and PKA, affecting G0 checkpoint and sexual differentiation [PMID:15448137 "Spc1-dependent binding of Atf1-Pcr1 heterodimer to an M26 DNA site in the cgs2+ promoter, which remodels chromatin ... co-ordinates signals of nitrogen and carbon source depletion to affect a G0 cell-cycle checkpoint and sexual differentiation"]. This is the negative regulation of PKA/cAMP-activated GPCR signaling (GO:0110034).

## Meiotic recombination (M26 hotspot)
- Mts1/Mts2 (=Atf1/Pcr1) heterodimer essential for M26 hotspot activity; disruption abolishes hotspot [PMID:9391101 "Disruption of either gene, or both, abolishes M26 hotspot activity ... the Mts1/Mts2 heterodimer is essential for hotspot activity"].
- Hotspot activation not via increased transcription; separable from transcription [PMID:9391101 "ade6 mRNA levels are equivalent ... hotspot activation is not a consequence of elevated transcription levels"].
- Atf1 strictly required to activate ade6-M26 hotspot, not basal recombination; rate-limiting [PMID:19436749 "Atf1 is strictly required to activate the ade6-M26 meiotic recombination hotspot ... Atf1 is rate-limiting for hotspot recombination"]. Phosphorylation dispensable for hotspot [PMID:19436749 "a protein lacking all eleven MAPK phospho-acceptor sites ... was fully proficient for hotspot recombination"].
- HRA domain (activation) and HRR (repression) reside in Atf1; modular OSA/HRA/HRR/bZIP organization [PMID:18375981 "The HRA and HRR regions are necessary and sufficient to activate and repress recombination, respectively"]. => supports both activation (GO:0010846) and negative regulation (GO:0045128) of recombination.

## Heterochromatin / silencing at mating-type
- Atf1/Pcr1 nucleate heterochromatin at mat region in parallel to RNAi; target H3K9me and Swi6; RNAi-independent [PMID:15218150 "Atf1 and Pcr1 ... act in a parallel mechanism to the RNAi pathway for heterochromatin nucleation ... Atf1 and Pcr1 bind to the mating-type region and target histone H3 lysine-9 methylation and the Swi6 protein"]. NOTE: this is RNAi/siRNA-INDEPENDENT => supports the NEGATED GO:0141194 (siRNA-mediated heterochromatin formation) annotation and positive GO:0030466.
- Atf1/Pcr1 recruit HDAC Clr6, needed for H3/H4 deacetylation before H3K9me/Swi6 assembly [PMID:15292231 "Atf1 and Pcr1 ... are crucial for proper histone deacetylation of both H3 and H4 ... Atf1 and Pcr1 can form complexes with both a histone deacetylase, Clr6, and Swi6"].
- Clr3 HDAC recruited at mat through ATF/CREB proteins => chromatin-protein adaptor role [PMID:16246721 "Clr3 is recruited at a specific site through a mechanism involving ATF/CREB family proteins"]. Supports GO:0140463 chromatin-protein adaptor activity.

## Nucleosome organization / antisense barrier
- Atf1 basal binding creates wide NDRs; deletion -> disorganized nucleosomes, derepressed antisense transcription [PMID:25122751 "deletion of atf1 results in nucleosome disorganization specifically at stress coding regions and derepresses antisense transcription ... acts as an effective barrier"]. Supports GO:0031491 nucleosome binding & GO:0060195 negative regulation of antisense RNA transcription.

## Mitotic entry
- Atf1 directly controls Cdc13 (mitotic cyclin) expression; binds Cdc13 promoter; regulates G2/M independently of Wee1/Cdc25 [PMID:24728197 "Atf1 binds to the Cdc13 promoter, leading to activation of Cdc13 expression"].

## Protein interactions
- Heterodimer with Pcr1 (UniProt SUBUNIT). Interacts with Sty1/Spc1 (IntAct). Srk1 kinase target of Sty1 [PMID:12080074] - the GO:0005515 IPI with Q09892(sty1) refers to atf1-sty1 interaction. StressNet interactome [PMID:23695164].

## RNA binding (weak/dubious)
- ~210 nt RNAs copurified with Mts1/Mts2 but "likely copurified as a result of tight but nonspecific interactions" [PMID:7518718 "the RNAs copurified as a result of tight but nonspecific interactions with the heterodimeric protein"]. => GO:0003723 RNA binding is questionable/over-annotation (nonspecific).

## PMID:39747188 caveat
- This Nat Commun paper is about PhpC(NF-Y), not Atf1. Abstract does not mention atf1 DNA binding. The GO:0000978 EXP annotation attributed to atf1 from this paper cannot be supported from the abstract -> UNDECIDED (cannot verify atf1-specific claim from cached text).

## Core function summary
1. MF: sequence-specific RNA Pol II DNA-binding transcription activator (and repressor) binding ATF/CRE (M26, TGACGT) sites - core.
2. BP: master regulator of the core environmental stress response (osmotic, heat, oxidative, nutrient) downstream of Sty1 SAPK.
3. BP: sexual differentiation / stationary phase entry (ste11 induction, G1 arrest).
4. BP: activation of M26 meiotic recombination hotspots (separable, transcription-independent).
5. BP: RNAi-independent heterochromatin nucleation/silencing at the mating-type region (recruits Clr3/Clr6 HDACs, Swi6) - chromatin-protein adaptor.
