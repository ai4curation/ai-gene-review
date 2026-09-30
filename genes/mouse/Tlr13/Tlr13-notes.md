# Tlr13 (mouse, UniProt Q6R5N8, MGI:3045213) — curation notes

Deep research (falcon) was requested by the batch harness but no
`Tlr13-deep-research-*.md` file had been produced when this review was written;
these notes come from the UniProt record, the GOA rows and the cached publications.
Unlike its Tlr11/Tlr12 neighbours, Tlr13 has no nomenclature ambiguity — the gene
symbol, the UniProt entry and the literature name all agree.

## Established biology

- Ligand. TLR13 recognises a short, conserved sequence of bacterial 23S ribosomal
  RNA: [PMID:22821982 "the orphan receptor TLR13 in mice recognizes a conserved 23S ribosomal RNA"]
  sequence that is the binding site of macrolide/lincosamide/streptogramin
  antibiotics. Methylation of that site, the mechanism of erythromycin resistance,
  abolishes recognition — 23S rRNA from resistant isolates and synthetic
  oligoribonucleotides carrying the modification [PMID:22821982 "failed"]
  [PMID:22821982 "to stimulate TLR13"]. Independently,
  [PMID:22896636 "Small interfering RNA against TLR13 reduced"] cytokine induction by
  bacterial RNA in dendritic cells, and the same study concludes that TLR13 is a
  receptor for bacterial RNA.
- Structure of recognition. The crystal structure of the ectodomain with a 13-nt
  single-stranded RNA shows sequence- and conformation-specific binding, and that
  [PMID:26323037 "The ssRNA induces TLR13 dimerization but assumes"] a stem-loop-like
  conformation quite unlike its conformation in the ribosome. The same work reports
  that [PMID:26323037 "a viral-derived 16-nt ssRNA"] predicted to adopt a similar
  fold also activates the receptor — which is the most concrete support for the
  earlier virus-related claim.
- Compartment and trafficking. It is an endosomal receptor. UniProt records
  "Endosome membrane" from PMID:22896636, and the UNC93B1 interaction was found by
  mass spectrometry of UNC93B immunoprecipitates:
  [PMID:17452530 "we identified TLR3, 7, 9, and 13 with extensive sequence coverage over the entire length of the proteins"].
- Signalling. [PMID:21131352 "MyD88- and TAK1-dependent TLR signaling pathway, inducing the activation of"]
  NF-kappa-B, with type I interferon induction through IRF7. The same paper reported
  a response to vesicular stomatitis virus; UniProt flags this as requiring further
  evidence, and the two 2012 papers plus the 2015 structure all converge on bacterial
  rRNA as the physiological ligand.
- Absence in human. UniProt notes that Tlr13 is not conserved in human and suggests
  a different human rRNA-sensing receptor may exist; chicken TLR21 is the
  phylogenetic neighbour that Keestra notes "displays similarity with mouse TLR13".

## Annotation decisions (summary)

- The ligand and pathway rows are the strongest part of the record and are accepted
  as-is: GO:0019843 rRNA binding (IDA, twice), GO:0034178 toll-like receptor 13
  signaling pathway (IDA, twice), GO:0045087 innate immune response (IDA, twice),
  GO:0002755 MyD88-dependent toll-like receptor signaling pathway (IGI with Myd88),
  GO:0005768 endosome and GO:0010008 endosome membrane.
- GO:0038023 (IBA) modified to GO:0038187 pattern recognition receptor activity: a
  defined PAMP is bound directly, with a structure of the complex.
- GO:0005886 plasma membrane (IBA) modified to GO:0010008 endosome membrane — the
  PAINT donors are surface TLRs and this receptor is endosomal.
- The two GO:0042802 identical protein binding rows are modified to GO:0042803
  protein homodimerization activity, which is what the structural and
  co-immunoprecipitation data show, and is informative.
- The two GO:0005515 protein binding rows record the UNC93B1 and MyD88 interactions.
  Both are modified rather than removed: UNC93B1 is a chaperone-like trafficking
  factor (GO:0051087 protein-folding chaperone binding), and the MyD88 interaction is
  TIR-domain-mediated (GO:0070976 TIR domain binding).
- GO:0009615 response to virus (IMP) is kept as non-core rather than accepted: the
  vesicular stomatitis virus result is the weakest claim in the record, is flagged by
  UniProt as needing further evidence, and the structural work supports only that a
  viral ssRNA of the right fold can activate the receptor.
- GO:0005737 cytoplasm (IDA) and GO:0043408 regulation of MAPK cascade (IGI with
  Map3k7) are kept as non-core: true but generic, and superseded by the endosome and
  MyD88-pathway annotations respectively.
