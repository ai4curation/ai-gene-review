# HBS1L — research notes

UniProt: Q9Y450. TRAFAC-class translation-factor GTPase, eEF1A/eRF3/Hbs1 group. Cytoplasmic.

## Core function
HBS1L is the **GTPase subunit of the Pelota-HBS1L (Dom34-Hbs1) complex**. It delivers PELO
(eRF1-like) to the A site of stalled ribosomes and, via GTP hydrolysis, licenses PELO/ABCE1-driven
subunit dissociation (ribosome disassembly) in no-go and non-stop decay.

- [file:human/HBS1L/HBS1L-uniprot.txt "GTPase component of the Pelota-HBS1L complex, a complex that recognizes stalled ribosomes and triggers the No-Go Decay (NGD) pathway"]
- [file:human/HBS1L/HBS1L-uniprot.txt "Component of the Pelota-HBS1L complex, also named Dom34-Hbs1 complex, composed of PELO and HBS1L"]
- [PMID:21448132] dissociation of stalled complexes by Pelota/Hbs1/ABCE1.
- [PMID:27863242] cryo-EM defines the complex on stalled ribosomes.
- [PMID:23667253] Hbs1-Dom34 in non-stop mRNA decay.
- [PMID:9872408 "The product of the mammalian orthologue of the Saccharomyces cerevisiae HBS1 gene is phylogenetically related to eukaryotic release factor 3 (eRF3) but does not carry eRF3-like activity"] — original characterization: GTP-binding, translation-related, eRF3-like but NO eRF3 (release) activity. NOTE: this paper's TAS annotations for GTP binding / translation / signal transduction are coarse.

## Isoforms
- Isoform 2 (Q9Y450-2, "HBS1LV3", short splice form) links the **SKI complex and the cytoplasmic exosome** (direct SKIC2 and EXOSC3 binding) [PMID:28204585; PMID:20531386 (human exosome interactions)]. This is a distinct, isoform-specific scaffolding role.

## Other / non-core
- Bare protein binding IPI rows: PELO (Q9BRX2) is the meaningful partner; others are HT noise.
- HDA membrane (PMID:19946888 NK-cell membrane proteome) and extracellular exosome (PMID:19056867) localizations are mass-spec catalog hits, not the functional site.
- GO:0010629 negative regulation of gene expression (IEA, GO_REF:0000117) and GO:0007165 signal transduction (TAS, PMID:9872408) are overly broad / weakly supported.

## Action plan
- Core MF: GO:0003924 GTPase activity (with GTP binding). Core BP: GO:0072344 rescue; GO:0032790 disassembly; no-go/non-stop decay. Core CC: GO:1990533 Dom34-Hbs1 complex.
- GO:0006412 translation: KEEP_AS_NON_CORE (broad; specific role is rescue).
- signal transduction, neg reg gene expression, membrane, exosome localization: MARK_AS_OVER_ANNOTATED or KEEP_AS_NON_CORE.
