# ste11 (S. pombe) review notes

UniProt P36631; PomBase SPBC32C12.02; 468 AA; HMG-box DNA-binding domain (residues 16-80).

## Core biology
Ste11 is the master HMG-box transcription factor controlling sexual differentiation (mating/conjugation and meiotic entry) in fission yeast.

- [PMID:1657709 "Schizosaccharomyces pombe ste11 encodes a member of the family of HMG-box proteins. Its transcript is induced in response to nitrogen starvation and a concomitant decrease of the intracellular cAMP level. Expression of ste11 is essential for induction of sexual development, and its ectopic expression stimulates uncontrolled mating and sporulation."]
- [PMID:1657709 "Ste11 protein regulates positively transcription of the following genes required for sexual development: the mating type genes, matP and matM, and the mei2 gene, which is essential for commitment to meiosis."]
- [PMID:1657709 "Ste11 protein synthesized in vitro binds specifically to a DNA fragment carrying a 10-base motif TTCTTTGTTY that is an essential cis-acting element for the induction of mei2 and is commonly seen in the upstream regions of the genes inducible by nitrogen starvation."] -- TR-box. Supports double-stranded DNA binding (GO:0003690) and RNA Pol II cis-reg DNA binding (GO:0000978), and activator activity.

## DNA binding mechanism / bending
- [PMID:10867006 "By site selection, we identify a highly specific 12-base pair motif for Ste11, AGAACAAAGAAA."]
- [PMID:10867006 "The sequence-specific interaction of Ste11 with these 3' base pairs contributes significantly to binding and bending of the DNA motif."] -- supports GO:0044377 (cis-reg DNA binding, bending).

## Recruitment / cooperativity with Mat1-Mc (M-cell specific genes)
- [PMID:9233811 "This regulation requires two HMG-box proteins: the ubiquitous Ste11 transcription factor and the M cell-controlling protein Mat1-Mc."]
- [PMID:9233811 "The Mat1-Mc protein caused a dramatic increase in the DNA-binding of Ste11 to this box"] -- WITH = PomBase:SPBC23G7.09 (mat1-Mc). Supports protein binding / RNA Pol II transcription regulator complex annotations from this paper.

## Target genes
- mat1-Pm / mat1-Pc: [PMID:7975894 "This region lies just upstream of a TATA-like box and contains a TR-box (TTCTTTGTTY) motif which is the recognition site of a putative transcription factor Ste11. ... Almost no expression of mat1-Pm was detected in a ste11 deletion mutant, whereas overproduction of Ste11 greatly increased the expression."]
- mfm M-factor genes: [PMID:8196631 "Their transcription is limited to M cells and requires the mat1-Mc and ste11 gene products."]
- rgs1: [PMID:11554925 "we describe rgs1, a member of the Regulator of G-protein Signalling (RGS) family, as a novel Ste11 target gene. rgs1 expression requires both an Ste11-mediated nitrogen starvation signal..."]
- dmc1/rad24 bicistronic meiotic transcript: [PMID:10908327 "Induction of the bicistronic transcript is under the control of a meiosis-specific transcription factor, Ste11."]
- ste8/STE11(Sc): [PMID:1435723] -- this paper is about S. pombe ste8 (=byr2) and S. cerevisiae STE11 kinase, NOT directly about the HMG TF ste11. However GOA cites it for "positive regulation of transcription by RNA Pol II" for ste11 P36631. The paper shows mat1-Pm induction requires the pheromone signal transduction. Annotation is borderline; ste11 (TF) is the activator of mat1-Pm. Keep but note the paper's primary subject is ste8.

## Regulation (negative)
- Pat1/Ran1 kinase phosphorylates Ste11 (inhibitory): [PMID:8945514 "the ste11 transcription factor is a substrate for ran1 in vitro and that this reaction is directly inhibited by mei3"].
- MAPK Spk1 phosphorylates and binds Ste11 (positive, pheromone pathway): [PMID:15713656 "we show that Spk1 can interact physically with Ste11 and also phosphorylate the transcription factor in vitro."] WITH = PomBase:SPAC31G5.09c (spk1). Also [PMID:15713656 "we demonstrate that ste11 is required for pheromone-induced G1 arrest."]
- PKA + TOR pathways block Ste11 nuclear accumulation: [PMID:20634885 "both the PKA and the Tor2 pathways inhibit sexual differentiation by preventing Ste11 nuclear accumulation."] and [PMID:20634885 "Exponentially growing wild-type cells showed a pancellular localization of Ste11-GFP ... In cells lacking PKA, Ste11-GFP accumulated in the nucleus"]. Supports both nucleus AND cytoplasm localization (shuttling).
- Tor2-Mei2-Ste11 complex: [PMID:17046992 "This newly revealed function of Tor2 appears to operate by interfering with the functions of the transcription factor Ste11 and the meiosis-promoting RNA-binding protein Mei2."] Supports GO:0034064 part_of Tor2-Mei2-Ste11 complex (IDA).
- Rad24 (14-3-3) binds phospho-Ste11: [PMID:37788281 "Ste11, the key transcription factor for sexual differentiation was expressed in sam3 mutants without starvation and it predominantly localized to the nucleus."] supports nucleoplasm activity.

## Upstream activation
- Rst2 (Zn-finger) activates ste11 transcription; ste11 autoregulates: [PMID:10982411 "A complete Ste11p-binding motif (TR box) found in the promoter region was necessary for the full expression of ste11, suggesting that Ste11p is involved in the activation of ste11."]

## Localization (CC)
- Nucleus + cytoplasm shuttling, nuclear accumulation on starvation/pheromone: [PMID:20634885 above]; high-throughput nucleus/cytosol [PMID:16823372 "we determined the localization of 4,431 proteins, corresponding to approximately 90% of the fission yeast proteome, by tagging each ORF with the yellow fluorescent protein."]; PKA mutants show nuclear Ste11 [PMID:21879336 "Rst2 and Ste11 proteins were induced and localized to the nucleus of sam5 and sam7 mutants even under rich glucose conditions"].

## Annotation decisions summary
- MF DNA-binding TF activity / activator / sequence-specific Pol II DNA binding / dsDNA binding / bending: ACCEPT (core).
- BP regulation/positive regulation of transcription by Pol II, positive regulation of conjugation with cellular fusion: ACCEPT (core).
- CC nucleus / nucleoplasm: ACCEPT (core action location). cytoplasm/cytosol: KEEP_AS_NON_CORE (shuttling reservoir; not where it acts as TF).
- GO:0005515 protein binding (x2): MODIFY/REMOVE-style. CLAUDE.md says avoid bare "protein binding". Mark for more informative term where possible. WITH mat1-Mc -> recruited into Pol II regulator complex (already captured by GO:0090575). WITH spk1 -> it is the kinase substrate relationship. Use MARK_AS_OVER_ANNOTATED / replace not feasible without good MF term; recommend NEW protein-binding-with-context not available -> mark as over-annotated bare protein binding.
- GO:0034064 Tor2-Mei2-Ste11 complex: ACCEPT (well documented).
- GO:0090575 Pol II transcription regulator complex: ACCEPT (Ste11 is a Pol II TF in a regulator complex with Mat1-Mc).
</content>
</invoke>
