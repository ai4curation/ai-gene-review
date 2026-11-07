# benC (P07771, Acinetobacter baylyi ADP1) notes

## Provenance of this review

- Created as a cross-genus representative member of
  `modules/benzoate_upper_pathway.yaml`, so the module is grounded beyond
  Pseudomonas putida KT2440.
- Deep research: `just deep-research-falcon ACIAD benC` was attempted and failed with
  "Failed to authenticate" (provider credentials rejected), so there is no
  `-deep-research-*.md` file and none was written by hand. The review rests on
  the UniProt entry and the cached publications: PMID:12051836, PMID:12949084, PMID:9721284, PMID:2824437.
- Every quotation is verbatim from those cached sources; several are
  abstract-only, flagged with `full_text_unavailable` on the reference.

## This gene

- The only member of this module with a solved structure: PDB 1KRH at 1.5 A
  [PMID:12051836 "BenC contains three domains, each binding a redox cofactor:
  iron-sulfur, FAD and NADH, respectively."]. The cluster and the flavin sit
  about 9 A apart, which is what makes the intramolecular electron transfer fast.
  FAD binding (GO:0071949) is proposed as NEW on that basis.
- GO:0042203 toluene catabolic process is REMOVEd, and this overrules a *curated*
  Swiss-Prot line, not just an electronic mapping: P07771 carries
  `CC -!- PATHWAY: Xenobiotic degradation; toluene degradation.`, which is the
  source of the UniPathway UPA00273 cross-reference in that row. ADP1 is not a
  toluene degrader and the benzoate dioxygenase BenC serves has no detectable
  activity on 4-methylbenzoate. The defect is reported upstream in
  `review.source_defects` against UNIPROT, at PROBABLE confidence because the
  flat file does not state the line's own evidence.
- BenC is promiscuous in its choice of oxygenase partner: it substitutes for
  AntC in vivo [PMID:9721284 "In Acinetobacter mutants, benC substituted for
  antC during growth on anthranilate"]. This is one reason the module models it
  as a sibling annoton rather than a subunit of the BenAB complex.
