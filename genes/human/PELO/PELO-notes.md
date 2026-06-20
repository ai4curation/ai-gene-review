# PELO (Pelota homolog / Dom34) — research notes

UniProt: Q9BRX2. Member of the eukaryotic release factor 1 (eRF1) family, Pelota subfamily. 385 aa, cytoplasmic.

## Core function
PELO is the eRF1-like component of the **Pelota-HBS1L (Dom34-Hbs1) complex**, a ribosome-rescue
machine. Unlike eRF1, it has no peptidyl-tRNA hydrolase (peptide release) activity; it instead
recognizes ribosomes stalled at the 3' end of an mRNA (truncated/non-stop, no-go) and, together
with the GTPase HBS1L and the recycling ATPase ABCE1, drives subunit dissociation (ribosome
disassembly), initiating No-Go Decay (NGD) and Non-Stop Decay (NSD).

- [file:human/PELO/PELO-uniprot.txt "Component of the Pelota-HBS1L complex, a complex that recognizes stalled ribosomes and triggers the No-Go Decay (NGD) pathway"]
- [file:human/PELO/PELO-uniprot.txt "In the Pelota-HBS1L complex, PELO recognizes ribosomes stalled at the 3' end of an mRNA and engages stalled ribosomes by destabilizing mRNA in the mRNA channel"]
- [file:human/PELO/PELO-uniprot.txt "Belongs to the eukaryotic release factor 1 family. Pelota subfamily."]
- [PMID:21448132 "Dissociation by Pelota, Hbs1 and ABCE1 of mammalian vacant 80S ribosomes and stalled elongation complexes"] — biochemical reconstitution of subunit dissociation (ribosome disassembly).
- [PMID:27863242 "Decoding Mammalian Ribosome-mRNA States by Translational GTPase Complexes"] — cryo-EM of the PELO-HBS1L complex on stalled ribosomes; defines stalled-ribosome sensor activity, ribosome binding, Dom34-Hbs1 complex.
- [PMID:23667253 "The Hbs1-Dom34 protein complex functions in non-stop mRNA decay in mammalian cells"] — NSD/no-go decay role.
- [PMID:27543824 "Conserved functions of human Pelota in mRNA quality control of nonstop mRNA"] — K2A/R45A mutants abolish rescue of stalled ribosomes (UniProt MUTAGEN).

## Other / non-core
- PINK1-regulated mitophagy: upon mitochondrial damage PELO is recruited to mito-OM-associated ribosome/mRNP, enabling autophagy receptor recruitment [PMID:29861391]. Peripheral, context-specific.
- Many IntAct `protein binding` IPI rows are high-throughput interactors (HSPB1, HTT, FLNA, etc.); HBS1L (Q9Y450) and EIF3G/ABCE1 are the biologically meaningful ones. Bare GO:0005515 is uninformative.
- Ensembl IEA developmental terms (endoderm development, inner cell mass proliferation, BMP signaling, stem cell maintenance) reflect mouse Pelo knockout phenotypes (embryonic lethality) — downstream/pleiotropic, not in GOA TSV here.

## Action plan
- Core MF: GO:0170011 stalled ribosome sensor activity; GO:0043022 ribosome binding. Core BP: GO:0072344 rescue of stalled cytosolic ribosome; GO:0032790 ribosome disassembly. Core CC: GO:1990533 Dom34-Hbs1 complex.
- NGD/NSD BP (GO:0070966, GO:0070481) accept/keep.
- Bare protein binding IPI → KEEP_AS_NON_CORE (HBS1L) or MARK_AS_OVER_ANNOTATED (random HT hits).
