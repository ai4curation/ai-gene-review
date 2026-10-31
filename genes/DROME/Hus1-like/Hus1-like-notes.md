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
- Deep research (falcon) initially hit rate limits (HTTP 429); completed on retry (see below).

## Deep research (falcon) update
- Completed after retry. It summarizes the 9-1-1 clamp model [file:DROME/Hus1-like/Hus1-like-deep-research-falcon.md "The ring acts as a DNA-associated platform for damage- and replication-stress signaling."] and reports that a Hus1-like insertion mutant increases sensory axon regrowth after injury (Li et al. 2021, Nat Commun). That finding is not in GOA and was not added as a NEW annotation; it is recorded as a suggested question.
- The report missed the Abdu-lab hus1 papers (PMID:17327271, PMID:19501158, PMID:22666434), which remain the primary basis of this review.
- Review follow-up: the core MF GO:0030674 is asserted with contributes_to_molecular_function, not molecular_function. Hus1-like is a PCNA-like ring subunit; the recruitment-platform (adaptor) activity belongs to the assembled 9-1-1 clamp, and no experiment shows this subunit bridging macromolecules on its own (unlike Rad9, whose C-terminal extension targets the complex). This matches how RnrS models its complex-level activity.
