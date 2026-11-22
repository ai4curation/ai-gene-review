# serS (E. coli K-12, P0A8L1) review notes

## 2026-11-11 complete annotation review

Deep research could not be generated (`just deep-research ECOLI serS --provider perplexity`
failed: offline dependency resolution for deep-research-client). Review is based on the
curated UniProt record and cached abstracts.

### Function
- Class II seryl-tRNA synthetase, homodimer. [file:ECOLI/serS/serS-uniprot.txt "Catalyzes the attachment of serine to tRNA(Ser)"]
- Also serylates tRNA(Sec). [PMID:2963963 "This tRNA is aminoacylated with L-serine by the seryl-tRNA ligase which also charges cognate tRNASer"]
  [PMID:8065908 "charges specifically the five iso-acceptor tRNA(ser) as well as the tRNA(sec) (selC product) of E. coli"]
- tRNA(Sec) is a poorer substrate. [PMID:1939093 "seryl-tRNA synthetase displays 10-fold impaired Km and Kcat values for tRNA(Sec) in comparison to tRNA(Ser)"]
- Cross-dimer tRNA binding. [PMID:7537870 "provide functional evidence for the cross-dimer binding of tRNA in solution"]
  [PMID:8508916 "a tRNA molecule binds across the dimer"]
- E355Q abolishes serine activation (ATP site). [file:ECOLI/serS/serS-uniprot.txt "E->Q: Loss of serine activation activity."]

### Decisions
- GO:0006434 seryl-tRNA aminoacylation is obsolete in GOA's current labels; all four rows
  MODIFY -> GO:0006418, as in genes/PSEPK/serS.
- nucleotide binding -> ATP binding; aminoacyl-tRNA ligase -> serine-tRNA ligase; cytoplasm -> cytosol (MODIFY).
- GO:0000287 magnesium ion binding (IDA, PMID:17889423): MARK_AS_OVER_ANNOTATED. The abstract
  attributes the Mg2+ dependence of the equilibrium constant to Mg complexes of PPi/AMP/tRNA,
  not to a metal site on SerS [PMID:17889423 "Different bindings of the Mg(2+) ions to the substrate tRNA and product aminoacyl-tRNA can explain this observation."]. Abstract-only, so not REMOVE.
- GO:0042802 identical protein binding (IPI x2): KEEP_AS_NON_CORE; homodimer is functionally
  required (cross-dimer tRNA binding), but structural rather than a core activity.
- GO:0016260 L-selenocysteine biosynthetic process: ACCEPT. SerS catalyses Ser-tRNA(Sec)
  formation, step 1 of the tRNA-dependent route; participation, not just necessity. Consistent
  with the PSEPK serS review and the selenocysteine module (order 2 part).
- PMID:4906848 is cached as a citation only (no abstract); its IDA rows ACCEPTed on curator deference.
- `just paint-losses ECOLI serS`: no IRD/IKR losses on the lineage.
