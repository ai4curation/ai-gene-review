# Uggt1 review notes

## 2026-09-05 — SFT binding concept versus annotation suitability

The GO:0051082 prediction remains CNN for the biological concept of binding non-native glycoprotein substrates. Recombinant rat UGGT retains the substrate preference of the liver enzyme [PMID:10764828, “The purified recombinant enzyme shows the same preference for unfolded polypeptides”]. The exact term has an IDA GOA row, and the current main review explicitly affirms the underlying recognition/binding while marking a standalone unfolded-protein-binding annotation over-annotated. Substrate binding is not disproved by preferring the glucosyltransferase activity as the curated molecular function, nor does the predicted binding term assert a separate folding-chaperone mechanism.

The benchmark policy separates ontology status from biological correctness. Its frozen ontology already treats release-specific identifiers separately from the underlying biological concept. An explicit supported-wrapper adjudication now preserves CNN for this gene/term when the reference action is `MARK_AS_OVER_ANNOTATED`; other rejection actions or accepted negations trigger renewed review. The main review, raw model identifier/label, and GOA snapshot are unchanged. Cached PMID:10764828 is abstract-only; the claim here is anchored to the explicit rat enzyme/substrate findings in that abstract and its existing IDA annotation, without inventing uninspected assay details.

LSP was considered but not used: the preferred glucosyltransferase activity is a different catalytic concept, rather than a refinement of the predicted binding specificity. The distinction concerns the usefulness of an annotation, not refutation of the experimentally supported binding concept.

## Re-review 2026-10-10

GOA changes since the original review:
- New rows (4): GO:0003980 EXP PMID:1533626; GO:0005788 ER lumen ISO and GO:0005793 ERGIC
  ISO (both from human UGGT1 Q9NYU2); GO:0006487 protein N-linked glycosylation IBA
  (PTN000132051).
- Retired rows (6): GO:0051082 IBA/ISO/IDA (QuickGO confirms GO:0051082 is obsolete),
  GO:0016740 and GO:0016757 (keyword IEA), GO:1901135 (ARBA IEA). Reviews kept; a
  retirement sentence added to each. The three GO:0051082 rows keep MARK_AS_OVER_ANNOTATED
  (recognition of non-native clients is the substrate-selection step of the
  glucosyltransferase, not a separate holdase/chaperone activity), so no
  proposed_new_terms entry is needed: the core MF has a GO term (GO:0003980).

PENDING resolutions:
- GO:0003980 EXP PMID:1533626 -> ACCEPT [PMID:1533626 "Denatured glycoproteins are
  glucosylated much more efficiently than native ones by the apparently homogeneous
  glucosyltransferase."]
- ER lumen ISO and ERGIC ISO -> ACCEPT, consistent with rat IDA rows [PMID:11535823
  "labeling intensity for GT was highest in pre-Golgi intermediates"].
- GO:0006487 IBA -> KEEP_AS_NON_CORE: UGGT acts on asparagine-linked glycans (N-glycan
  processing is part_of protein N-linked glycosylation), but the transient
  reglucosylation serves quality control rather than glycan biosynthesis.

Action changes:
- GO:0005515 IPI PMID:11278576 (with SELENOF Q923V8): MARK_AS_OVER_ANNOTATED -> REMOVE.
  The complex is real [PMID:11278576 "The native Sep15 isolated from rat prostate and
  mouse liver occurred in a complex with a 150-kDa protein"], but no specific MF follows;
  complex membership is captured by the GO:0032991 row.
- GO:0005515 IPI PMID:10764828 (with Q923V8): MARK_AS_OVER_ANNOTATED -> REMOVE (same
  reasoning; the cached abstract does not mention SELENOF).
- GO:0051084 'de novo' post-translational protein folding TAS: KEEP_AS_NON_CORE -> MODIFY
  to GO:0034975 protein folding in endoplasmic reticulum, matching the protein folding TAS row.
- 17 rows carrying boilerplate "Manual review ... Retained as supported or plausible"
  text were rewritten with specific summaries and verbatim supporting quotes; actions
  unchanged. Protein secretion ISO stays KEEP_AS_NON_CORE: QuickGO shows the mouse
  donor row (Q6P5E4) is IMP from PMID:20498017 [PMID:20498017 "A dramatic decrease in
  the secretion of prosaposin was observed in ugt1(-/-) cells"].

Open questions:
- Whether GO should have an activity term for glycoprotein folding-sensor recognition;
  for now it is treated as intrinsic to GO:0003980.
