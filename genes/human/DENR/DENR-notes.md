# DENR (Density-regulated protein, DRP) — research notes

UniProt O43583. 198 aa. Contains a C-terminal SUI1 domain (eIF1-like). Member of the DENR family; homologous to the C-terminal region of Ligatin/eIF2D, while MCTS1 is homologous to the N-terminal region.

## Core function
DENR forms a heterodimer with MCTS1; the MCTS1–DENR complex is a non-canonical translation (re)initiation and 40S recycling factor. It is the functional equivalent of eIF2D split into two polypeptides.

- [PMID:20713520 "the oncogene MCT-1 and DENR, which are homologous to N-terminal and C-terminal regions of Ligatin, respectively) promote efficient eIF2-independent recruitment of Met-tRNA(Met)(i) to 40S/mRNA complexes, if attachment of 40S subunits to the mRNA places the initiation codon directly in the P site"]
- [PMID:20713520 "Ligatin and MCT-1/DENR can promote release of deacylated tRNA and mRNA from recycled 40S subunits after ABCE1-mediated dissociation of post-termination ribosomes"]
- UniProt FUNCTION: "Translation regulator forming a complex with MCTS1 to promote translation reinitiation ... Firstly, the dissociation of deacylated tRNAs from post-termination 40S ribosomal complexes during ribosome recycling. Secondly, the recruitment in an EIF2-independent manner of aminoacylated initiator tRNA to P site of 40S ribosomes for a new round of translation."
- DENR–MCTS1 heterodimerization and tRNA recruitment are required for translation reinitiation [PMID:29889857 title]. DENR contributes the SUI1 (PUA-interacting) module; MCTS1 PUA domain binds DENR.
- MCTS1-dependent reinitiation translates specific mRNAs incl. JAK2; essential for IFN-γ immunity [PMID:37875108 title].

## Interactions (IPI)
- MCTS1 (Q9ULC4): the physiological obligate partner — many entries (16169070, 21516116, 32296183, 33961781, 40205054, 16982740). Best captured as MCTS1 binding / heterodimerization, not bare protein binding.
- MAPT (P10636, tau), MARCHF5 (Q9NX47), NELFB/UBC: high-throughput, peripheral.

## Localization
Cytoplasm (IDA, PMID:16982740). Also reported in stress granules / nucleolus (CD-CODE) but cytoplasmic ribosome-associated is the functional site.

## Decisions
- Reinitiation, preinitiation complex formation, ribosome disassembly (recycling), eIF2-independent tRNA delivery = core.
- MF: translation initiation factor activity (GO:0003743) is supported (eIF2D-like). Core MF.
- protein binding IPI with MCTS1 → MODIFY to protein heterodimerization/MCTS1 binding context; non-MCTS1 ones KEEP_AS_NON_CORE or over-annotated.
- IRES-dependent viral translational initiation (GO:0075522) — supported by 20713520 (HCV-like IRES P-site delivery). KEEP_AS_NON_CORE.
