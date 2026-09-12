# cdc25 (S. pombe) review notes

UniProt: P06652 (MPIP_SCHPO), gene SPAC24H6.05. "M-phase inducer phosphatase" / p80cdc25.
596 aa, Rhodanese-like catalytic domain (429-533), active-site phosphocysteine intermediate at Cys480.

## Core function

cdc25 is the protein-tyrosine phosphatase that dephosphorylates Cdc2 (CDK1) on Tyr15, the rate-limiting
step triggering mitotic entry. It is the positive counterpart of the Wee1/Mik1 tyrosine kinases.

- [PMID:3955656 "cdc25+ gene function is required to initiate mitosis ... increased cdc25+ expression causes mitosis to initiate at a reduced cell size. This shows that cdc25+ functions as a dosage-dependent inducer in mitotic control"] — also notes it "functions to counteract the activity of the mitotic inhibitor wee1+".
- [PMID:1756737 "cdc25 proteins directly dephosphorylate and activate p34cdc2 kinase to induce M-phase"]. C-terminal 23 kDa is the active domain; GST-cdc25 dephosphorylates pNPP and phospho-casein; "Reaction requirements and inhibitor sensitivities were the same as those of phosphotyrosine phosphatases (PTPases)"; "Mutation of the cdc25 Cys480 codon ... abolished the phosphatase activity". → catalytic, active-site cysteine confirmed.
- [PMID:1703321 "dephosphorylation of Tyr15 triggered activation of the pp34-cyclin complex ... a human protein-tyrosine phosphatase can catalyze this event both in vitro and in vivo"] — human PTPase complements p80cdc25.
- [PMID:1819507 "p80cdc25 encodes a phosphate that acts by directly dephosphorylating the Tyr-15 residue of p34cdc2"] (note: "phosphate" is a typo for phosphatase in source). Level of p80cdc25 rises as cells approach mitosis; timing of mitosis sensitive to cdc25+ dosage.
- [PMID:2665944 "The cell-cycle timing of mitosis in fission yeast is determined by the cdc25+ gene product activating the p34cdc2 protein kinase leading to mitotic initiation"].

EC 3.1.3.48 (protein-tyrosine-phosphatase). MF: protein tyrosine phosphatase activity (GO:0004725) — core, strongly supported.
GO:0004721 phosphoprotein phosphatase activity (IDA, PMID:22665807) is a broader parent; the IDA in that paper is about Cdk1/Clp1 phosphoregulation of Cdc25 — keep but the tyrosine-specific term is more informative.

## Cell size control / positive regulation of G2/M

- [PMID:28479325 "Cdc25—the tyrosine phosphatase that dephosphorylates tyrosine 15 (Y15) of Cdc2 ... Y15 dephosphorylation of Cdc2 is the rate-limiting step for entry into mitosis"] and "smaller cells express less Cdc25 and larger cells express more Cdc25, creating an increasing concentration of Cdc25 as cells grow and providing a mechanism for cells to trigger cell division when they reach a threshold concentration of Cdc25." This is mitotic G2 cell size control checkpoint (GO:0031569, IMP). Cell-size regulation (GO:0008361, NAS) is the older keyword-based statement.
- [PMID:22665807 "Cdc25 hyperphosphorylation by Cdk1 governs Cdc25 catalytic activation, the precision of mitotic entry, and unvarying cell length"] — Cdk1-Cdc25 positive feedback; Clp1/Cdc14 reverses it at mitotic exit.

## Checkpoint regulation (Cdc25 is the TARGET, inhibited by checkpoint kinases)

- [PMID:9278510 "These findings identify Cdc25, but not Wee1, as a target of the DNA damage checkpoint"]; "Cdc25 associated with Chk1 in vivo and was phosphorylated when copurified in Chk1 complexes." → response to mitotic G2 DNA damage checkpoint signaling (GO:0072435, IMP); protein binding with chk1 (SPCC1259.13).
- [PMID:9774107 "The Chk1 kinase ... phosphorylates Cdc25 ... Phosphorylation of Cdc25 promotes its binding to 14-3-3 proteins, preventing it from activating Cdc2"]; "Chk1 functions redundantly with the kinase Cds1 at the replication checkpoint and ... both kinases phosphorylate Cdc25 on the same sites, which include serine residues at positions 99, 192 and 359." IPI partners: cds1 (SPAC17A2.13c) and rad24 14-3-3 (SPAC8E11.02c).
- [PMID:10523629 "14-3-3 binding keeps Cdc25 out of the nucleus, away from its substrate"]; wild-type Cdc25 shuttles (nuclear accumulation with leptomycin B); Rad24 (14-3-3) overproduction → cytoplasmic. IPI partner rad24 (SPAC8E11.02c).
- [PMID:9042863 "regulation of Cdc2 tyrosine dephosphorylation, mainly carried out by the Cdc25 tyrosine phosphatase, as an important part of the mechanism by which the DNA damage checkpoint induces Cdc2 inhibition"] — PomBase used this for PTP activity IMP.
- [PMID:15297457] intra-S DNA damage checkpoint: Rad3-Cds1 pathway targets Cdc2; Cdc25 IMP for GO:0031573.
- [PMID:15629716 "Srk1 kinase ... regulates the onset of mitosis by inhibiting the Cdc25 phosphatase ... Srk1 interacts with and phosphorylates Cdc25 at the same sites phosphorylated by the Chk1 and Cds1 ... Phosphorylation by Srk1 causes Cdc25 to bind to Rad24 ... and accumulation of Cdc25 in the cytoplasm."] Localization: cytoplasm + nucleus (IDA).
- [PMID:18272791 "Srk1 ... negatively regulates cell cycle progression by inhibiting Cdc25 ... translocating Cdc25 from the nucleus to the cytoplasm"]. IDA nucleus + cytosol.

## Localization

- Cytoplasm + nucleus, shuttling; highest nuclear in G2. [PMID:15629716], [PMID:10523629], [PMID:28479325 "Cdc25 is predominantly nuclear in G2"].
- HDA cytosol (PMID:16823372 ORFeome global localization).
- PMID:1500423 is the MAMMALIAN cdc25 (nuclear), not S. pombe — annotated to P06652 by PomBase as orthologous support for nucleus. Keep but note it is heterologous evidence.

## Meiosis (non-core, but genuine)

cdc25 is also required for meiotic nuclear divisions (meiosis I onset), via the same Cdc2-Tyr15 dephosphorylation, downstream of the meiotic transcription factor Mei4.
- [PMID:17804800 "cdc25 + is an important target of Mei4p in control of entry into meiosis I. Forced dephosphorylation of Cdc2p on tyrosine-15 thus induced meiosis I in mei4 mutant cells"]. Mei4 activates cdc25+ transcription. → GO:0110044 regulation of cell cycle switching, mitotic to meiotic (IMP) and GO:0110032 positive regulation of G2/MI transition of meiotic cell cycle.
- [PMID:25492408 "Mei4 is also required for the expression of phosphatase Cdc25, which activates cyclin-dependent kinase (CDK), and is thereby essential for triggering meiotic nuclear divisions"]; "Cdc25 triggers entry to nuclear divisions downstream of the replication checkpoint independently of Mei4." → GO:0110032 (IMP).

These meiotic roles are the SAME biochemical activity (Cdc2-Y15 dephosphorylation) deployed in the meiotic cell cycle; they are real (not SPKW keyword artifacts) but are not the single core function — keep as non-core.

## Protein binding (IPI) — replace bare protein binding where possible

- PMID:9278510 with chk1 (SPCC1259.13): Cdc25 is a substrate/binding partner of the Chk1 checkpoint kinase. Could be modeled as kinase binding, but the experimental finding is being a checkpoint-kinase target.
- PMID:9774107 with cds1 (SPAC17A2.13c) AND rad24 14-3-3 (SPAC8E11.02c): substrate of Cds1; binds 14-3-3.
- PMID:10523629 with rad24 (SPAC8E11.02c): 14-3-3 binding.
- PMID:11812792 with suc1/p13suc1 (SPBC1734.14c): this NMR paper is about p13suc1/CKS; the cdc25 IPI here is weak/peripheral. The paper does not actually characterize a Cdc25-Suc1 interaction in detail — mark as over-annotated / undecided (paper is about suc1 structure, not cdc25).

GO curation guideline: avoid bare "protein binding" (GO:0005515). For the 14-3-3 interactions, GO:0071889 (14-3-3 protein binding) is the informative term. For chk1/cds1 (these kinases act ON cdc25), the relationship is best captured by the BP checkpoint terms rather than a generic MF; suggest MODIFY rad24 IPIs to 14-3-3 protein binding, and mark the others as over-annotated (uninformative protein binding).
