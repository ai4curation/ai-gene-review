# Dhps (Q9VSF4, CG8005) review notes

Module context: dmel_hypusine_biosynthesis (Dhps then nero on eIF5A).

Note: `just fetch-gene DROME Dhps` resolved to the 76-aa unreviewed fragment M9PEZ0; the
review uses the expected accession Q9VSF4 (`just fetch-gene DROME Q9VSF4 --alias Dhps`).
UniProt Q9VSF4 carries only the ORF name CG8005; the FlyBase symbol Dhps is used.

Deep research: `Dhps-deep-research-falcon.md` (falcon).

- Reaction (UniProt, by similarity): "Catalyzes the NAD-dependent oxidative cleavage of spermidine and the subsequent transfer of the butylamine moiety of spermidine to the epsilon-amino group of a specific lysine residue of the eIF-5A precursor protein"
- Two-step pathway: [PMID:19546244 "In the first step, deoxyhypusine synthase (DHS) cleaves spermidine and transfers the 4-amino butyl moiety to a specific lysine residue of eIF5A"]
- Fly evidence (Liang 2021, abstract only in cache): [PMID:33852845 "Several genetic regimes of attenuating eIF5A hypusination all similarly affect brain mitochondrial respiration"]; deep research adds that a CG8005 null is late-larval lethal and neuronal CG8005 RNAi "also lowered brain hypusination and respiration".

Decisions: activity, hypusine biosynthesis and cytoplasm accepted; spermidine metabolic
process (IBA) kept as non-core (Dhps does cleave spermidine, but as donor for eIF5A
modification, not in polyamine homeostasis). Brain-aging and mitochondrial phenotypes are
downstream and were not proposed as NEW terms.
