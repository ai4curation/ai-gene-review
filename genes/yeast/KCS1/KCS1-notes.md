# KCS1 (YDR017C, Q12494) notes

- Yeast IP6 kinase [PMID:10574768 "we report the cloning of two mammalian InsP(6) kinases and a yeast InsP(6) kinase"]; 5-position [UniProt:Q12494 "Reaction=1D-myo-inositol hexakisphosphate + ATP = 5-diphospho-1D-myo-inositol 1,2,3,4,6-pentakisphosphate + ADP"].
- Also IP5 -> PP-IP4 [PMID:10827188 "inositol pentakisphosphate (InsP(5)) was phosphorylated to diphosphoinositol tetrakisphosphate (PP-InsP(4))"], but yeast kinase specialised for IP6 [PMID:10827188 "the yeast kinase are more specialized for the phosphorylation of InsP(6)"].
- Kinase-dead allele abolishes PP-InsPs; leucine heptad domain needed for vacuole biogenesis [PMID:11956213 "kinase-dead" ... "two leucine heptad repeats"]; broader substrate range when overexpressed [PMID:11956213 "the ability of Kcs1p to phosphorylate a wider range of substrates than previously appreciated"].
- INO1 transcription/inositol auxotrophy [PMID:23824185 "Deletion of KCS1 ... causes inositol auxotrophy and decreased intracellular inositol and phosphatidylinositol"].
- PHO / polyP [PMID:15866881 "constitutively express PHO5"].
- Cytoplasmic (GFP) [UniProt:Q12494 "SUBCELLULAR LOCATION: Cytoplasm"].

## Curation decisions
- IBA 3-kinase activities (GO:0000824, GO:0008440) from PTN000963723 seeded only by ARG82 marked over-annotated (IPMK-specific; arg82 cells accumulate IP3 despite Kcs1) [PMID:10683435 "increased cellular [InsP(3)] 170-fold"].
- IBA lipid process GO:0046854 over-annotated (IPMK-specific).
- GO:0120517 RCA mis-mapped (IP5 -> IP6 is Ipk1): MODIFY to GO:0000827.
- GO:0010919 IMP MODIFY to GO:1900088 regulation of inositol biosynthetic process (paper is about INO1/inositol, not InsP synthesis).
- Nucleus IBA UNDECIDED (no direct yeast evidence either way).
