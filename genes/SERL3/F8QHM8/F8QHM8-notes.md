# F8QHM8 (Serpula lacrymans var. lacrymans S7.3 pyruvate carboxylase) notes

No deep-research provider was available. This file is a manual literature and record review.

## Identity
- UniProtKB F8QHM8_SERL3, TrEMBL, PE 4 (predicted). ORF SERLA73DRAFT_173059 (EMBL EGN92205.1), proteome UP000008063, 1198 aa.
- It is the only protein named pyruvate carboxylase in the S. lacrymans S7.3 proteome (UniProt REST query, 2026-10-28).
- Family: PANTHER PTHR43778:SF2, NCBIfam TIGR01235, PIRSF001594. Single-chain PC architecture: biotin carboxylation domain 44-494, ATP-grasp 164-361, carboxyltransferase 584-853, biotinyl domain 1119-1197, predicted biotinyl-Lys1163.
- Residues 1-29 form an N-terminal extension that MobiDB-lite predicts to be disordered; S. cerevisiae Pyc1p has no such extension. No transit peptide is annotated, and I did not run a targeting predictor. Localization of basidiomycete PC is untested.

## Literature
- No paper characterizes this protein or any Serpula pyruvate carboxylase.
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
- CMMMech gives the locus as `SERLA73DRAFT_189440`. The UniProt entry's ORF is SERLA73DRAFT_173059, and a UniProt search for SERLA73DRAFT_189440 returns nothing. The CMMMech locus field looks wrong; the accession is right, being the only PC in the S7.3 proteome.
- In the Vlasov et al. 2023 cerussite study (Crystals 13:432), S. lacrymans (LE-BIN 1192) was a comparator strain, not strain S7.3, and no gene-level work was done. CMMMech's role statement ("generating oxaloacetate for organic-acid and oxalate production") is a family-level inference; PC's contribution to oxalate in Serpula is untested.
