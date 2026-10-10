# hrde-1 (Q09249) review notes

Deep research: `just deep-research-falcon worm hrde-1 --fallback perplexity-lite` failed
(falcon killed at the 600 s timeout, exit 137; the perplexity fallback is unavailable in
this environment). No deep-research file was generated. The review is based on cached
publications and the UniProt record.

## Key facts with provenance
- HRDE-1/WAGO-9 is a germline nuclear WAGO Argonaute required for RNAi inheritance
  [PMID:22810588 "hrde-1 encodes an Argonaute protein that associates with small interfering RNAs in the germ cells of progeny of animals exposed to double-stranded RNA"].
- It binds 22G endo-siRNAs [PMID:22810588 "HRDE-1 bound 22G endogenous (endo) siRNAs, which were expressed in germ cells"].
- It recruits NRDE-2 to pre-mRNA [PMID:22810588 "HRDE-1 was required for RNAi-mediated recruitment of NRDE-2 to a germline pre-mRNA"].
- Silencing is co-transcriptional [PMID:22810588 "indicating that the RNAi inheritance machinery silences germline target genes co-transcriptionally during the normal course of reproduction"].
- It is nuclear, and also visits nuage [PMID:37083324 "HRDE-1, while predominantly nuclear, also localizes to peri-nuclear nuage domains, where amplification is thought to occur."].
- WAGOs are not slicers [PMID:22738726 "whereas the all WAGOs lack key catalytic residues"].
  Our own check (hrde-1-bioinformatics/RESULTS.md) found no DEDH tetrad residue
  conserved against human AGO2.
- It is needed for piRNA-initiated multigenerational silencing [PMID:22738725].

## Decisions
- RNA endonuclease IBA: REMOVE (slicer loss in the WAGO clade).
- miRNA binding IBA: MODIFY to siRNA binding. RISC IBA: MODIFY to RNAi effector complex.
- Post-transcriptional silencing (IBA and IMP): MODIFY to GO:0031048 (matches the module
  and the NRDE-2 annotation).
- Germ cell development IMP: non-core (transgenerational Mrt phenotype).
