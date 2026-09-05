# Uggt1 review notes

## 2026-09-05 — SFT binding concept versus annotation suitability

The GO:0051082 prediction remains CNN for the biological concept of binding non-native glycoprotein substrates. Recombinant rat UGGT retains the substrate preference of the liver enzyme [PMID:10764828, “The purified recombinant enzyme shows the same preference for unfolded polypeptides”]. The exact term has an IDA GOA row, and the current main review explicitly affirms the underlying recognition/binding while marking a standalone unfolded-protein-binding annotation over-annotated. Substrate binding is not disproved by preferring the glucosyltransferase activity as the curated molecular function, nor does the predicted binding term assert a separate folding-chaperone mechanism.

The benchmark policy separates ontology status from biological correctness. Its frozen ontology already treats release-specific identifiers separately from the underlying biological concept. An explicit supported-wrapper adjudication now preserves CNN for this gene/term when the reference action is `MARK_AS_OVER_ANNOTATED`; other rejection actions or accepted negations trigger renewed review. The main review, raw model identifier/label, and GOA snapshot are unchanged. Cached PMID:10764828 is abstract-only; the claim here is anchored to the explicit rat enzyme/substrate findings in that abstract and its existing IDA annotation, without inventing uninspected assay details.

LSP was considered but not used: the preferred glucosyltransferase activity is a different catalytic concept, rather than a refinement of the predicted binding specificity. The distinction concerns the usefulness of an annotation, not refutation of the experimentally supported binding concept.
