# rpoC (E. coli K-12) notes

## 2026-11-13 annotation review

Reviewed every GOA row against the UniProt record (experimental CC statements,
ECO:0000269) and the cached publications for each cited PMID. No deep-research
provider report was generated for this gene; claims rest on UniProt and the
cached papers.

Cross-subunit policy, applied identically to rpoA, rpoB, rpoC and rpoZ in
E. coli K-12 and P. putida KT2440 (see projects/PROTEIN_COMPLEX_FUNCTIONS.md):

- DNA-directed RNA polymerase activity (GO:0003899) is a core function only of
  the beta and beta-prime active-centre subunits, recorded with contribution
  semantics because neither is active alone. On alpha and omega the
  complex-level activity is MARK_AS_OVER_ANNOTATED. GO:0034062 on beta/beta' is
  MODIFY to the specific GO:0003899.
- Alpha's core function is protein dimerization (assembly platform); omega's is
  bacterial-type RNA polymerase core enzyme binding (latching beta-prime).
- ComplexPortal holoenzyme rows: complex membership (GO:0000345) and
  transcription initiation are accepted (omega initiation kept as non-core).
  Regulon-level physiology (iron homeostasis, heat response, nitrate
  assimilation, motility, flagellum assembly, biofilm, envelope stress) and
  regulation of initiation are MARK_AS_OVER_ANNOTATED: the specificity in each
  cited paper belongs to a sigma factor or regulator
  [PMID:28666008 "The promoter selectivity of Escherichia coli RNA polymerase (RNAP) is determined by the sigma subunit."].
  GO:0008023 (a factor complex that acts on RNAP) is over-annotated for an RNAP
  subunit. Antitermination is kept as non-core: RNAP is part of the processive
  antitermination complex [PMID:28452979 "render elongating RNA polymerase termination-resistant"].
- Bare protein binding rows are removed under the protein-binding policy.
- Membrane (HDA, blue-native complexome) is over-annotated; RNAP has no
  membrane anchor.
Regulation of elongation (GO:0032784) is kept as non-core for beta and
beta-prime because pausing is intrinsic to the active centre
[PMID:26132790 "Pausing is thus an intrinsic property of RNAP augmented by sequence context"].
