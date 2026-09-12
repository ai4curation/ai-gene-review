# UFSP1 (Q6NVU6) research notes

## Identity
- Ufm1-specific protease 1, peptidase C78 family (MEROPS C78.001), paralog of UFSP2.
- Long misannotated as catalytically inactive in humans because the canonical 445AUG-initiated protein lacks the catalytic cysteine/protease domain.

## Core function: active UFM1-specific cysteine protease
- Two 2022 papers established that the *endogenous* active UFSP1 is translated from an upstream non-canonical (near-cognate CUG/CTG ~217) start codon, producing a longer ~24 kDa isoform (A0A5F9ZGY7) that contains the catalytic Cys protease domain. [PMID:35926457 "the long-isoform UFSP1 we here identify is the correct endogenous UFSP1 that is catalytically competent via a cysteine-thiol-based mechanism, thus correcting the long-held misconception that human UFSP1 is an inactive protease"] [PMID:35525273 "translation of human UFSP1 initiates from an upstream near-cognate codon, 217CUG, via eukaryotic translation initiation factor eIF2A-mediated translational initiation rather than from the annotated 445AUG, revealing the presence of a catalytic protease domain containing a Cys active site"]
- UFSP1 is an active cysteine protease that matures pro-UFM1 (removes the C-terminal Ser-Cys dipeptide to expose the C-terminal Gly) AND de-UFMylates target proteins. [PMID:35525273 "both UFSP1 and UFSP2 mediate maturation of UFM1 and de-UFMylation of target proteins"]
- Catalytic residue: Cys (ACT_SITE 45 in the short-numbered entry; C->A abolishes activity). [UniProt MUTAGEN 45 "C->A: Abolished isopeptidase activity"]

## Distinct vs redundant roles (UFSP1 vs UFSP2)
- Both contribute redundantly to pro-UFM1 maturation; cells lacking both UFSPs show complete loss of UFMylation due to absence of mature UFM1. [PMID:35926457 "Cells lacking both UFSPs show complete loss of UFMylation resulting from an absence of mature UFM1"]
- UFSP2 (ER-localized via ODR4) removes UFM1 from ribosomal RPL26; UFSP1 does NOT reverse RPL26 UFMylation. UFSP1 acts earlier — matures UFM1 and removes a potentially autoinhibitory UFM1 modification on UFC1 (at K122). [PMID:35926457 "While UFSP2, but not UFSP1, removes UFM1 from the ribosomal subunit RPL26, UFSP1 acts earlier in the pathway to mature UFM1 and cleave a potential autoinhibitory modification on UFC1, thereby controlling activation of UFMylation"]
- UFSP1 is cytosolic. [UniProt "SUBCELLULAR LOCATION: Cytoplasm, cytosol"] [PMID:35926457 "Immunoblot analysis of cell fractions confirms that UFSP1 is cytosolic in localization"]
- In vitro UFSP1 cleaves UFM1 from diverse substrates (UBA5~UFM1, UFC1~UFM1) and disassembles K69-linked polyUFM1 chains. [PMID:35926457 "UFSP1 effectively cleaved UFM1 from these different substrates and catalyzed the disassembly of polyUFM1 chains in vitro"]

## Annotation assessment
- deUFMylase activity (GO:0071567), cysteine-type peptidase activity (GO:0008234): CORE MF, IDA-supported.
- protein maturation (GO:0051604), protein ufmylation (GO:0071569): correct BP context (pro-UFM1 maturation enables UFMylation). Process annotations; keep. ufmylation is the pathway it regulates/enables.
- cytosol (GO:0005829): correct localization, IDA + IEA.
- protein binding (GO:0005515, PMID:32296183): high-throughput IntAct interactome with ~40 partners (transcription factors etc.), uninformative; no specific functional partner. KEEP_AS_NON_CORE per guidelines.

## Pathway step (batch guidance)
UFSP1/UFSP2 = UFM1-specific proteases in the UFMylation cascade (UBA5 E1, UFC1 E2, UFL1 E3, DDRGK1/UFBP1 adaptor). Core MF here is the UFM1-specific/cysteine protease (deUFMylating) activity.
</content>
</invoke>
