# KGD4 (YFR049W / YMR31) notes

UniProt P19955; module `tca_cycle` (Kgd4/MRPS36 adaptor annoton, GO:0030674).

## Evidence journal
- Kgd4 is a novel subunit of mitochondrial alpha-KGDH, previously assigned to the mitoribosome [PMID:25165143 "we identified a novel component, Kgd4 (Ymr31/MRPS36), which was previously assigned to be a subunit of the mitochondrial ribosome"].
- Adaptor mechanism: binds E1-E2 core and E3 [PMID:25165143 "By binding to both the E1-E2 core and the E3 subunit, Kgd4 acts as a molecular adaptor that is necessary to a form a stable α-KGDH enzyme complex"]; direct Lpd1 binding [PMID:25165143 "showed that Kgd4 directly binds to Lpd1"]; C-terminal domain contacts the core [PMID:25165143 "This demonstrates that the C-terminal domain of Kgd4 directly interacts with the assembled Kgd1-Kgd2 core"].
- Activity: [PMID:25165143 "KGDH activity was dramatically reduced in the absence of Kgd4 (Figure 2A)"].
- Ribosome assignment is contamination [PMID:25165143 "the highly abundant KGDH is therefore found to contaminate ribosomal preparations"]; UniProt CAUTION agrees [UniProt:P19955].
- Original ribosomal-protein claim: [PMID:2693936 "Two mitochondrial ribosomal proteins of yeast (Saccharomyces cerevisiae) were purified"].
- Isoforms Kgd4S/Kgd4L via alternative UUG initiation [UniProt:P19955].

## Curation decisions
- REMOVE structural constituent of ribosome (GO:0003735) and mitochondrial ribosome (GO:0005761): contradicted by full-text evidence.
- Protein binding: MODIFY low-throughput rows to GO:0030674; REMOVE HTP rows.
- YeastCyc: KGD4 is not attached to the 2-oxoglutarate dehydrogenase reaction in the cached YeastPathways export, yet SGD's RCA rows (TCA-EUK-PWY) do include KGD4 with correct mitochondrial compartment.
