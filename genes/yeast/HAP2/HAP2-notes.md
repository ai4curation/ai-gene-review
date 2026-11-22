# HAP2 (P06774, YGL237C) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: HAP2 is reviewed as the experimentally characterised reference for transfer to
N. crassa NCU03033 (Q7SGY4). ProtNLM2 outputs were not consulted.

### Deep research
`just deep-research-falcon yeast HAP2 --fallback perplexity-lite` failed: the Edison (falcon)
API returned "Failed to authenticate" (HTTP 403), and the perplexity-lite fallback also
failed. No deep-research file exists. The review is based on the cached abstracts
(all abstract-only) and the curated UniProt record.

### Evolutionary grounding
- PANTHER 19 places P06774, Q7SGY4 and human NFYA (P23511) in the same subfamily,
  PTHR12632:SF6 (see HAP2-bioinformatics/RESULTS.md). UniProt/InterPro cross-references show
  only the family PTHR12632 for both proteins.
- PAINT: the IBA rows come from PTN000290575 (MF/BP: GO:0000981, GO:0006357) and
  PTN000290576 (CC: GO:0016602). SGD:S000003206 (HAP2) is a donor to both nodes.
- PAINT propagated only the generic family-level terms (TF activity, regulation of transcription
  by Pol II, CCAAT-binding factor complex). It did NOT propagate the yeast-specific "positive
  regulation" / respiration terms. I treat that omission as deliberate: NF-Y can activate or
  repress, and the respiratory regulon depends on the HAP4 activation subunit.

### Experimentally established in S. cerevisiae
- Nuclear localisation of HAP2-lacZ fusion; lexA-HAP2 activates transcription
  [PMID:3547076 "a bifunctional HAP2-beta-galactosidase fusion gene was localized to the yeast nucleus"].
- HAP2 and HAP3 associate without DNA to form an activation complex at CYC1 UAS2
  [PMID:2832951 "HAP2 and HAP3 associate in the absence of DNA to form a multisubunit activation complex"].
- HAP2/3/5 heterotrimer is required and sufficient for CCAAT binding
  [PMID:7828851 "purified recombinant HAP2, HAP3, and HAP5 are able to reconstitute CCAAT-binding activity in mobility shift analysis"].
- HAP2 DNA-binding domain: 21 residues; R199L changes specificity; it forms a hybrid DNA-binding domain
  with HAP3 [PMID:8223474].
- One-step assembly of Hap2/3/5; Hap4 joins only after DNA binding; Hap4 supplies the activation domain
  [PMID:16278450].
- hap2 mutants: cytochromes about 40-50% of wild type, slow growth on glycerol [PMID:2182199].

### Inferred only (not shown in yeast)
- The generic NF-Y activator/repressor duality; the yeast complex is only shown as an activator.

### Protein binding
The five GO:0005515 IPI rows (all with HAP5, Q02516) come from high-throughput two-hybrid/MS screens.
They are removed under the protein-binding policy. The interaction is real, and the
CCAAT-binding factor complex CC term captures it.
