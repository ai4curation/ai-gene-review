# STR (Medicago truncatula, D3GE74) – curation notes

## 2026-10-02 research journal

Sources: UniProt D3GE74, Falcon deep research (STR-deep-research-falcon.md), cached abstracts
(PMID:20453115, 26511916, 22077667, 30292683, 28380681 abstract-only; PMID:34618047, 37717076 full text).

### Identity and architecture
- Half-size ABCG transporter, positionally cloned from the str mutant [PMID:20453115 "STR was identified by positional cloning and encodes a half-size ATP binding cassette (ABC) transporter of a subfamily (ABCG)"].
- Conserved clade restricted to AM hosts [PMID:20453115 "its orthologs are highly conserved throughout the vascular plants but absent from Arabidopsis thaliana"].
- Do not confuse with MtABCG59 (full-size, strigolactone secretion) [file:MEDTR/STR/STR-deep-research-falcon.md].

### Complex and location
- Heterodimer with STR2 (A9YWR6) at the periarbuscular membrane [PMID:20453115 "STR heterodimerizes with STR2, and the resulting transporter is located in the peri-arbuscular membrane"]. BiFC STR–STR negative (basis of the NOT homodimerization row).
- GO note: GO:0085042 periarbuscular membrane has ancestors host cell membrane / host cellular component, NOT plasma membrane (checked QuickGO). So the plasma membrane rows are not redundant in the graph.

### Process
- str: arbuscules stunted, AM fails; nodulation normal [PMID:20453115 "In contrast with legume symbiosis mutants reported previously, str shows a wild-type nodulation phenotype."].
- Rice STR1/STR2 phenocopy; strigolactones unlikely substrates [PMID:22077667 "Mutation of either of the Oryza sativa (rice) ABCG transporters blocked arbuscule growth of different AM fungi at a small and stunted stage"].

### Substrate (unresolved)
- FatM/RAM2 make 16:0 beta-MAG; model is export across the PAM [PMID:28380681 "We propose a model in which β-monoacylglycerols, or a derivative thereof, are exported out of the root cell across the periarbuscular membrane for ultimate use by the fungus."].
- Expert review: no direct proof [PMID:34618047 "It is tempting to speculate that sn2-MAG compounds or MAG derivatives are STR/STR2 substrates; however, direct proof has not yet been provided"].
- STR–STR2 co-overexpression in Arabidopsis atwbc11-4 increased cutin [PMID:37717076 "co-overexpression of STR-STR2 in Arabidopsis atwbc11-4 plants significantly increased cuticular cutin content"] – heterologous, indirect.
- Decision: keep MF at ABC-type transporter activity; no lipid-transporter MF or lipid export BP proposed (NEW count 0).

### Regulation
- RAM1-dependent [PMID:26511916 "RAM1 regulates expression of EXO70I and Stunted Arbuscule"]; WRI5a binds STR AW-boxes [PMID:30292683 "WRI5a binds AW-box cis-regulatory elements in the promoters of M. truncatula STR"]; ERM1 binds STR/STR2 promoters, ERF12 feedback [PMID:37717076].

### Curation decisions
- protein binding (IPI, STR2) -> MODIFY to protein heterodimerization activity GO:0046982.
- ATP binding, ATP hydrolysis, membrane, response to symbiotic fungus (x2) -> KEEP_AS_NON_CORE.
- All others ACCEPT, including NOT nodulation and NOT homodimerization.
