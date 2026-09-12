# MCTS1 (MCT-1, Malignant T-cell-amplified sequence 1) — research notes

UniProt Q9ULC4. Contains a PUA domain (RNA-binding). Partner of DENR; the MCTS1-DENR heterodimer is the eIF2D-like non-canonical reinitiation/recycling factor (MCTS1 = N-terminal half of Ligatin/eIF2D, DENR = C-terminal SUI1 half).

- [PMID:16982740 "MCT-1 protein interacts with the cap complex through its PUA domain and recruits the density-regulated protein (DENR/DRP), containing the SUI1 translation initiation domain"]
- [PMID:20713520 "the oncogene MCT-1 and DENR ... promote efficient eIF2-independent recruitment of Met-tRNA(Met)(i) to 40S/mRNA complexes ... can promote release of deacylated tRNA and mRNA from recycled 40S subunits after ABCE1-mediated dissociation of post-termination ribosomes"]
- [PMID:29889857 "DENR-MCTS1 heterodimerization and tRNA recruitment are required for translation reinitiation"]
- [PMID:37875108] MCTS1-dependent reinitiation translates JAK2; essential for IFN-γ immunity (IMP from patient cells).
- Originally identified as oncogene amplified in T-cell lymphoma (PMID:11709712, cytoplasmic).

## MF decisions
- translation initiation factor activity (GO:0003743, IDA 20713520) — core.
- ribosomal small subunit binding (GO:0043024, IDA 20713520) — core (binds 40S).
- RNA cap binding (GO:0000339, IDA 16982740) — supported by the cap-complex interaction via PUA; KEEP/ACCEPT but note it is in context of cap complex.
- RNA binding (GO:0003723, IEA) — PUA domain; KEEP_AS_NON_CORE.
- protein binding IPI with DENR (O43583) — the obligate partner; KEEP_AS_NON_CORE.
- reinitiation, ribosome disassembly, preinitiation complex formation, IRES init — core/non-core as for DENR.
