# A0A5M3MJR8 (Coniophora puteana pyruvate carboxylase) notes

No deep-research provider was available. This file is a manual literature and record review.

## Identity
- UniProtKB A0A5M3MJR8_CONPW, TrEMBL, PE 4 (predicted). ORF CONPUDRAFT_91456 (EMBL EIW79180.1), proteome UP000053558, 1199 aa.
- It is the only protein named pyruvate carboxylase in the C. puteana RWD-64-598 SS2 proteome (UniProt REST query, 2026-10-28).
- Family: PANTHER PTHR43778:SF2, NCBIfam TIGR01235, PIRSF001594. Single-chain PC architecture: biotin carboxylation domain 45-495, ATP-grasp 165-362, carboxyltransferase 585-854, biotinyl domain 1120-1198, predicted biotinyl-Lys1164.
- Residues 1-30 form an N-terminal extension that MobiDB-lite predicts to be disordered; S. cerevisiae Pyc1p has no such extension. No transit peptide is annotated, and I did not run a targeting predictor. Localization of basidiomycete PC is untested.

## Literature
- No paper characterizes this protein or any Coniophora pyruvate carboxylase.
- Brown-rot oxalate biosynthesis (Fomitopsis palustris): oxalate comes mainly from oxaloacetate hydrolysis by oxaloacetase, fed by coupled TCA and glyoxylate cycles [PMID:11553780 "Thus, most oxalate is inferred to be produced from oxaloacetate and to be hydrolyzed by OXA involved in both recycling routes (C and D)."]. That model sources oxaloacetate from malate oxidation; it does not invoke pyruvate carboxylase, and PC activity was not reported.
- In Aspergillus niger, oxalate forms by cytoplasmic hydrolysis of oxaloacetate [PMID:3132096 "The results are consistent with a cytoplasmic pathway of oxalate formation which does not involve the tricarboxylic acid cycle."]. In a cytosolic route, oxaloacetate would come from PC.
- In brown-rot fungi, oxaloacetase expression goes up at hyphal fronts [PMID:27543342 "Near advancing hyphal fronts, oxaloacetase expression was up upregulated for both fungi"].
- Yeast PC is cytosolic, and that paper describes the cytosolic location as unusual for fungi [PMID:2665820 "In contrast to the general situation in fungi, plants and animals, pyruvate carboxylase was found to be a cytosolic enzyme in both yeasts."]. PAINT nevertheless asserts cytosol at the Fungi node PTN001050931, seeded by S. cerevisiae Pyc1p/Pyc2p and Aspergillus nidulans PycA.

## Review decisions (8 IEA rows)
- Pyruvate carboxylase activity: ACCEPT. Catalytic activity: MODIFY to that term.
- Biotin carboxylase activity: KEEP_AS_NON_CORE, as a partial reaction of the single-chain enzyme.
- ATP binding: KEEP_AS_NON_CORE. Metal ion binding: KEEP_AS_NON_CORE. Nucleotide binding: TOO_GENERAL.
- Cytoplasm: ACCEPT, with the caveat above. Gluconeogenesis: ACCEPT.
- No NEW rows. Source defects: none. UniProt's automatic annotation is consistent with the family.

## CMMMech cross-check (cerussite.yaml)
- CMMMech gives the locus as `CONPUDRAFT_164718`. The UniProt entry's ORF is CONPUDRAFT_91456, and a UniProt search for CONPUDRAFT_164718 returns nothing. The CMMMech locus field looks wrong; the accession itself is right, being the only PC in the proteome.
- CMMMech's functional_role ("converting pyruvate and bicarbonate into oxaloacetate, the immediate precursor for oxalic-acid biosynthesis in Coniophora puteana") is a family-level inference. Vlasov et al. 2023 (Crystals 13:432, doi:10.3390/cryst13030432) did mineralogy only, as CMMMech's own evidence note says. The F. palustris model routes oxaloacetate for oxalate through malate oxidation, not PC. PC as the oxalate oxaloacetate source in C. puteana is therefore plausible but unverified, and the record's "partial" support level is appropriate.
