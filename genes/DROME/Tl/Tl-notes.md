# Tl (Toll, P08953) — review notes

Batch 1 (Toll/TLR axis) of the INNATE_IMMUNITY project. Falcon deep research had
not started for DROME genes when this review was drafted; notes below are built from
the cached GOA publications and the UniProt record.

## Identity and architecture

- Type I transmembrane receptor, 1097 aa; extracellular LRR ectodomain with
  cysteine-rich caps, single TM, cytoplasmic TIR domain (UniProt P08953; InterPro
  IPR000157 TIR).
- Cloned as the maternal dorsal-group gene [PMID:2449285 "The sequence of cDNAs suggests that the Toll protein is an integral membrane protein with a cytoplasmic domain and a large extracytoplasmic domain."]

## Ligand: the endogenous cytokine Spätzle, not a microbial molecule

- Mature Spätzle (C-106) binds Toll directly [PMID:12872120 "in vitro experiments showed that the mature form of Spätzle bound to the Toll ectodomain with high affinity and with a stoichiometry of one Spätzle dimer to two receptors"].
- Crystal structures: [PMID:24282309 "Drosophila Toll functions in embryonic development and innate immunity and is activated by an endogenous ligand, Spätzle (Spz). The related Toll-like receptors in vertebrates also function in immunity but are activated directly by pathogen-associated molecules such as bacterial endotoxin."]; [PMID:24733933 "Spätzle binds to the concave surface of the membrane-distal LRR domain, in contrast to the flanking ligand interactions observed for mammalian Toll-like receptors"].
- Microbial sensing is done upstream by circulating PRRs (PGRP-SA, GNBP1, GNBP3) and the Persephone protease, which converge on Spätzle processing [PMID:17190605 "The sensing of Gram-positive bacteria is mediated by the pattern recognition receptors PGRP-SA and GNBP1 that cooperate to detect the presence of infections in the host. Here, we report that GNBP3 is a pattern recognition receptor that is required for the detection of fungal cell wall components."].
- Toll pathway does not mediate LPS responses in S2 cells [PMID:10973475 "indicating that the Toll pathway selectively controls the antifungal response in Drosophila cell lines and is not involved in LPS response"].
- Conclusion for project question 1: Tl is a cytokine receptor; no GO:0038187 (PRR activity) or GO:0002224 (toll-like receptor signaling pathway) annotation is present, and none should be added. The pathway term used throughout is GO:0008063 Toll signaling pathway, which is correct.

## Signalling

- TIR-mediated recruitment of MyD88 [PMID:11743586 "DmMyD88 interacted with Toll through its TIR domain and required the death domain proteins Tube and Pelle to activate expression of Drs"]; [PMID:11606776 "dMyD88 potently activates a Drosomycin reporter gene and associates with the Toll receptor via TIR domains"].
- Weckle adaptor [PMID:16782008 "Wek homodimerizes and associates with Toll. Moreover, Wek binds to and localizes DmMyD88 to the plasma membrane."].
- Multimerization [PMID:15197269 "constitutively active mutants of Toll form multimers that contain intermolecular disulfide linkages"].
- Endocytosis to Rab5 early endosomes required for signalling [PMID:20921412 "we find that Toll is recruited from the plasma membrane to Rab5(+) early endosomes"]; [PMID:20404143 "Mop and Hrs, which are critical components of the ESCRT-0 endocytosis complex, colocalize with the Toll receptor in endosomes"].

## Two core roles

1. Embryonic dorsoventral patterning (maternal) [PMID:3931919 "the function of the Toll product is to provide the source for a morphogen gradient in the dorsal-ventral axis of the wild-type embryo"]; [PMID:3931918 "Lack of function alleles produce dorsalized embryos as a recessive maternal effect. Dominant gain of function alleles result in ventralized embryos."].
2. Systemic humoral immunity against fungi and Gram-positive bacteria [PMID:8808632 "the intracellular components of the dorsoventral signaling pathway (except for dorsal) and the extracellular Toll ligand, spätzle, control expression of the antifungal peptide gene drosomycin in adults"]; [PMID:10369678 "a linear activation cascade Spaetzle--> Toll-->Cactus-->Dorsal/DIF leads to the induction of the drosomycin gene in larval fat body cells"].

Both are the same molecular function (Spätzle receptor signalling via MyD88/Tube/Pelle
to Cactus degradation and Dorsal/Dif nuclear import). Neither is "non-core": the
developmental patterning role is the historically defining one and the immune role is
the conserved defence role. Other developmental roles (heart, muscle, synaptic target
choice, cell competition, wound gene induction, fat-body growth control) are
context-specific reuse and are kept as non-core.

## Other roles (non-core)

- Synaptic target repulsion [PMID:20504957 "Toll functions in M13 to prevent synapse formation by MN12s"].
- Heart [PMID:15870289 "Toll mutations result in defects in dorsal vessel structure"].
- Muscle patterning [PMID:9676200 "this pathway is required in the epidermis for proper muscle development"].
- Cell competition [PMID:30146479 "loser cells were no longer eliminated in the Tl null background, indicating cell competition is prevented by loss of Tl"].
- Wound-induced barrier-repair genes [PMID:28289197 "Robust activation of wound-induced transcription from ple and Ddc requires Toll pathway components ranging from the extracellular ligand Spätzle to the Dif transcription factor."].
- Fat body growth/insulin crosstalk [PMID:29514084 "We find that Toll acts cell autonomously to block growth but not PI(3,4,5)P3 production in fat body cells expressing constitutively active PI3K."].
- Tumour response via fat body [PMID:24582964 "Toll elicits a non-tissue-autonomous program in adipocytes, which drives tumor cell death"].

## Virus binding: conflicting data

- Chowdhury et al. 2019 report Toll-1 ectodomain co-precipitates VSV virions [PMID:31088910 "our results corroborate that Toll-7 binds VSV while showing that Toll-1 also binds this virus"].
- Nakamoto et al. 2012 used Toll as the negative control [PMID:22464169 "while Toll-7 precipitated with VSV, the plasma membrane protein Toll and the intracellular protein tubulin did not precipitate"]; and "flies lacking core Toll pathway components did not demonstrate increased susceptibility to VSV".
- Moy et al. 2014 likewise [PMID:24374193 "biotinylated RVFV did not precipitate Toll, demonstrating specificity"].
- Decision: GO:0046790 virion binding and GO:0009597 detection of virus on Tl -> UNDECIDED.

## Annotation decisions summary

- Accept core MF: cytokine receptor activity (GO:0004896), cytokine binding (GO:0019955), transmembrane signaling receptor activity, TIR domain binding.
- protein binding rows: MyD88 rows -> MODIFY to GO:0070976 TIR domain binding; Spätzle row -> MODIFY to GO:0019955 cytokine binding; Tehao and Weckle rows -> REMOVE (uninformative).
- positive regulation of transcription by RNA polymerase II (Akirin paper, IMP) -> MARK_AS_OVER_ANNOTATED (the receptor is several steps upstream of transcription).

## Falcon deep research (added after it completed)

The Falcon report (file:DROME/Tl/Tl-deep-research-falcon.md) agrees with the curation: ["Toll does not directly bind microbial components; instead, upstream pattern-recognition proteins detect PAMPs"]. It raises no evidence for PRR activity or for vertebrate TLR-pathway terms on Tl. No annotation decisions changed.
