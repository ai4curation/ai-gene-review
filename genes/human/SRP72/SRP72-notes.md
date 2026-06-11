# SRP72 (O76094) review notes

## Identity and overview
SRP72 is the largest subunit of the mammalian signal recognition particle (SRP), a ribonucleoprotein composed of a 300-nt 7SL RNA and six proteins (SRP9, SRP14, SRP19, SRP54, SRP68, SRP72). SRP72 and SRP68 form a heterodimer that binds a regulatory site on the 7SL RNA and constitutes part of the S-domain.

[file:human/SRP72/SRP72-uniprot.txt "Component of a signal recognition particle (SRP) complex that consists of a 7SL RNA molecule of 300 nucleotides and six protein subunits: SRP72, SRP68, SRP54,"]

[file:human/SRP72/SRP72-uniprot.txt "Heterodimer with SRP68"]

## Molecular function
- SRP72 is an RNA-binding scaffold subunit, NOT a GTPase (the GTPase activity of SRP resides in SRP54 and the SRP receptor).
- The N-terminal region (~9-163) contains TPR-like repeats and mediates the interaction with SRP68; the C-terminal region (RNA-binding, residues 545-617) binds the 7SL RNA 5e/5f loops.

[file:human/SRP72/SRP72-uniprot.txt "Within the SRP complex,\nCC       interacts (via N-terminus) with SRP68 (via C-terminus)"]

[file:human/SRP72/SRP72-uniprot.txt "Binds the signal recognition particle RNA (7SL RNA) in presence of"]

- The SRP72 RNA-binding domain is "a flexible peptide crawling along the 5e- and 5f-loops of SRP RNA. A conserved tryptophan inserts into the 5e-loop forming a novel type of RNA kink-turn" [PMID:27899666 "The SRP72-RBD is a \nflexible peptide crawling along the 5e- and 5f-loops of SRP RNA."].
- RNA-binding residues mapped by mutagenesis (source PMID:21073748): e.g. 553-558 (KKKKKK->AAAAAA) "Loss of RNA binding"; W577-L578 "Loss of RNA binding" [file:human/SRP72/SRP72-uniprot.txt "KKKKKK->AAAAAA: Loss of RNA binding."].
- SRP72-PBD is a tetratricopeptide repeat that binds an extended linear motif of SRP68 [PMID:27899666 "The SRP72-PBD is a tetratricopeptide repeat, which binds an \nextended linear motif of SRP68 with high affinity."]. This TPR-mediated SRP68 binding is the experimental basis for the GO:0030911 "TPR domain binding" IPI annotation.

## Cellular component / localization
- SRP72 acts within the cytosolic SRP and at the ER membrane during co-translational targeting.

[file:human/SRP72/SRP72-uniprot.txt "SUBCELLULAR LOCATION: Cytoplasm"]
[file:human/SRP72/SRP72-uniprot.txt "Endoplasmic reticulum {ECO:0000269|PubMed:22541560,"]

- ComplexPortal SRP complex: CPX-2652. Nucleolus / stress granule associations (CD-CODE) reflect SRP RNA assembly/trafficking; not core function.

## Biological process
- Core process: SRP-dependent cotranslational protein targeting to the ER membrane.

[file:human/SRP72/SRP72-uniprot.txt "mediates the cotranslational targeting\nCC       of secretory and membrane proteins to the endoplasmic reticulum (ER)"]

[file:human/SRP72/SRP72-uniprot.txt "The SRP complex targets the\nCC       ribosome-nascent chain complex to the SRP receptor (SR), which is\nCC       anchored in the ER, where SR compaction and GTPase rearrangement drive\nCC       cotranslational protein translocation into the ER"]

- SRP72/68 binding remodels 7SL RNA into an SRP54 binding competent state [PMID:17254600 "SRP68/72, together with SRP19, rearranges the 7SL RNA in an SRP54 binding \ncompetent state."].

## Disease
- Heterozygous SRP72 mutations cause autosomal-dominant bone marrow failure syndrome 1 (BMFS1; aplastic anemia / myelodysplasia). The BMFS1 variant R207H affects localization to the ER. This is a disease association, not a clean GO biological process.

[PMID:22541560 "We identified a heterozygous \nmutation in SRP72, a component of the signal recognition particle (SRP) that is \nresponsible for the translocation of nascent membrane-bound and excreted \nproteins to the endoplasmic reticulum."]

[file:human/SRP72/SRP72-uniprot.txt "Bone marrow failure syndrome 1 (BMFS1)"]

## Notes on specific references
- PMID:18089836 (TAS-103): abstract foregrounds SRP54 as the drug target, but the paper assays the intact SRP complex; the SRP72 IDA "signal recognition particle, ER targeting" CC annotation is valid for SRP72 as an SRP subunit. Do not REMOVE on subunit-naming grounds.
- PMID:24965446: pestivirus Npro interactome — SRP72 co-purified in an RNP/ribosome-associated complex (WITH/FROM is the Npro protease P19712-PRO). Bare protein binding, non-core.
- PMID:32296183 (HuRI; WITH/FROM SULT2B1 O00204), PMID:33961781 (BioPlex; SRP68 Q9UHB9), PMID:35271311 (OpenCell; SRP68 Q9UHB9): high-throughput interactome captures. Bare protein binding, non-core.
- PMID:16672232 IPI partner is SRP68 (Q9UHB9) — the physiological heterodimer partner; bare protein binding, kept non-core because GO:0005047 SRP binding captures the informative version.
- PMID:22658674, PMID:22681889: HeLa mRNA-interactome capture (HDA RNA binding); supports general RNA binding.

## Core function summary
1. 7S/7SL RNA binding scaffold subunit of SRP (heterodimer with SRP68), enabling SRP assembly and ribosome interaction.
2. Structural/RNA-binding S-domain component participating in SRP-dependent cotranslational protein targeting to the ER membrane.
</content>
