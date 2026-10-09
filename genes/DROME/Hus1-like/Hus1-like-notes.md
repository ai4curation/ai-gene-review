# Hus1-like (Drosophila HUS1) review notes

## Literature journal
- 9-1-1 complex in fly cells: [PMID:22666434 "Our results demonstrate for the first time that it is possible to co-precipitate DmRad9 with DmRad1 (Figure 3) and Hus1, indicating that DmRad9 forms a complex with DmRad1 and DmHus1."]
- Localization: [PMID:22666434 "In both S2R+ and follicle cells, DmHus1 is found in the cytoplasm, DmRad1 is found throughout the cell and Dm DmRad9A is localized to the nuclear membrane."]
- Null phenotype: [PMID:17327271 "hus1 mutant flies are sensitive to hydroxyurea and methyl methanesulfonate but not to X-rays"]; [PMID:17327271 "We also found that hus1 is not required for the G2-M checkpoint and for post-irradiation induction of apoptosis."]; [PMID:17327271 "These results demonstrate that hus1 is essential for the activation of the meiotic checkpoint"].
- Meiotic repair: [PMID:19501158 "Together, our results imply that hus1 is required for repair of DSBs during meiotic recombination."]; SC/karyosome defects depend on DSBs and Chk2 [PMID:19501158 "suggesting that these processes are dependent upon DmChk2 checkpoint activity"].

## Curation decisions
- Core: structural subunit of the 9-1-1 checkpoint clamp (MF approximated by GO:0030674) in intra-S and meiotic DNA integrity checkpoints; HR repair of meiotic DSBs.
- Oogenesis phenotypes (karyosome, SC disassembly, oocyte localization, pronucleus) kept as non-core: DSB/Chk2-dependent secondary effects.
- Nucleolus (InterPro mapping) over-annotated; cytoplasm/cytosol kept as non-core (unassembled overexpressed subunit).
- Deep research (falcon) hit rate limits (HTTP 429); retried later.
