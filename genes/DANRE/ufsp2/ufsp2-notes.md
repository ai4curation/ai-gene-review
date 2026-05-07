# ufsp2 (Danio rerio) Research Notes

## Overview

ufsp2 encodes UFM1-specific protease 2, a thiol-dependent cysteine protease belonging to the peptidase C78 family. The enzyme specifically cleaves UFM1 (ubiquitin-fold modifier 1) from conjugated proteins and also processes UFM1 precursors to their mature form by removing C-terminal residues. This gene is the zebrafish ortholog of human UFSP2 (UniProt Q9NUQ7).

## Discovery of the UFM1 Pathway

The UFM1 conjugation system was first described by Komatsu et al. [PMID:15071506 "E1 (activating), E2 (conjugating), and E3 (ligating) enzymes"]. UFM1 is a 9.1 kDa ubiquitin-fold modifier that "lacks obvious sequence identity" to ubiquitin but shares a similar tertiary structure. The pathway is conserved in metazoa and plants but absent from yeast [PMID:15071506 "Ufm1, Uba5, and Ufc1 are all conserved in metazoa and plants but not in yeast"].

## UFSP2 as a DeUFMylase

Two UFM1-specific proteases, UfSP1 and UfSP2, were identified by Kang et al. [PMID:17182609 "UfSP2 is present in most, if not all, of multicellular organisms"]. These enzymes "cleaved the C-terminal extension of Ufm1 but not that of ubiquitin" or related modifiers like SUMO-1 and ISG15, demonstrating strict substrate specificity [PMID:17182609]. The catalytic mechanism is cysteine-dependent: "replacement of the conserved Cys residue by Ser resulted in a complete loss of the UfSP1 and UfSP2 activities" [PMID:17182609].

## Structural Biology

The crystal structure of mouse UfSP2 was determined at 2.6 angstrom resolution [PMID:21228277]. UfSP2 comprises two domains: an N-terminal domain (approximately 240 residues) with a novel fold, and a C-terminal catalytic domain (approximately 200 residues) resembling papain-like proteases. The active site employs an unconventional catalytic triad: "Cys294, Asp418, and His420 form the catalytic machinery" [PMID:21228277]. The N-terminal domain plays a critical role in substrate recognition: "the N-terminal domain of UfSP2 plays a key role in the recognition of C20orf116 and thus in the recruitment of UfSP2 to the ER" [PMID:21228277].

## RPL26 UFMylation and ER Quality Control

The ribosomal protein RPL26 was identified as the principal substrate of UFMylation [PMID:30626644 "RPL26/L1 is the principal target of UFMylation in HEK293 cells"]. UFMylation occurs at lysines K132 and K134 specifically on 60S ribosomal subunits docked at the ER membrane. The UFMylation machinery (UFL1/CDK5RAP3/DDRGK1 E3 complex) is localized to the ER, ensuring "RPL26 UFMylation occurs exclusively at the ER surface" [PMID:30626644]. UFSP2 reverses this modification: "UFMylated RPL26 increased in abundance upon disruption of UFSP2" [PMID:30626644].

RPL26 UFMylation is essential for ribosome-associated quality control (RQC) at the ER [PMID:37036982]. When ribosomes stall during cotranslational translocation, "UFMylation of translocon-bound 60S subunits modulates the RTJ to promote access of proteasomes and RQC machinery to ER-APs" [PMID:37036982]. UFSP2-mediated deUFMylation is required to recycle the modified ribosomal subunits after quality control is completed.

## Ribosome Disassembly

UFSP2 participates in ribosome disassembly at the ER. The UFM1 E3 ligase complex promotes recycling of 60S ribosomal subunits from the ER by UFMylating RPL26, and UFSP2-mediated removal of UFM1 from RPL26 is a required step in the recycling cycle. This connects UFSP2 directly to the GO:0032790 (ribosome disassembly) annotation.

## Human Disease Relevance

Heterozygous pathogenic variants in the C-terminal catalytic domain of human UFSP2 cause skeletal dysplasias. A Y290H (equivalent to mouse Y282H) variant was identified in Beukes hip dysplasia (BHD), an autosomal dominant disorder causing "bilateral dysmorphism of the proximal femur, which results in severe degenerative osteoarthropathy" [PMID:26428751]. This mutation "abolishes UFSP2-mediated C-terminal cleavage of its substrate, Ufm1" [PMID:26428751].

A separate autosomal recessive variant (V115E, in the N-terminal domain) causes severe neurodevelopmental disease with epilepsy [PMID:33473208]. Patient fibroblasts showed that "the variant more prominently affects de-UFMylation rather than UFMylation," with reduced UFSP2 protein stability [PMID:33473208].

## Subcellular Localization

Based on studies of mammalian orthologs, UFSP2 localizes to the ER, cytoplasm, and nucleus. The ER localization is functionally significant given the role in ER-associated ribosome quality control and the recruitment via the N-terminal domain interacting with DDRGK1 (C20orf116) at the ER membrane [PMID:21228277]. Cytoplasmic and nuclear localizations are also reported, consistent with additional roles including at DNA double-strand breaks.

## Zebrafish-Specific Considerations

All annotations for zebrafish ufsp2 are transferred from mammalian orthologs (human UFSP2 Q9NUQ7 and mouse Ufsp2 Q99K23) by sequence similarity (ISS, IBA, IEA). No direct experimental evidence exists for zebrafish ufsp2 itself. The protein is highly conserved across vertebrates, so the transferred annotations are expected to be reliable.
