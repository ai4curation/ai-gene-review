# SSZ1 review notes

## 2026-08-12 re-review

- Identity verified as *Saccharomyces cerevisiae* SSZ1/YHR064C (PDR13),
  UniProt P38788, the atypical Hsp70-like subunit of the ribosome-associated
  complex (RAC), not the mitochondrial Fe-S chaperone Ssq1.
- Existing Falcon and targeted OpenScientist reports are correctly scoped. The
  OpenScientist report independently supports removing both family-derived
  GO:0016887 ATP hydrolysis annotations while retaining real ATP binding.
- Ssz1 forms stable RAC with Zuo1 at the cytoplasmic ribosomal tunnel exit. Its
  principal molecular contribution is to enable Zuo1 to stimulate the ATPase of
  the canonical nascent-chain Hsp70 Ssb1/2; neither Ssz1 ATP binding nor
  hydrolysis is required for this role.
- GO:0044183 is retained as the project's pragmatic co-chaperone MF for Ssz1's
  regulatory contribution to the RAC-Ssb folding system; unlike GO:0140662, it
  does not assert Ssz1 ATP hydrolysis. GO:0042026 remains an unsafe family-level
  transfer because classical post-translational refolding is not supported.
- The IMP unfolded-protein-binding annotation is marked over-annotated rather
  than removed: the peptide-binding domain is dispensable and classical Hsp70
  substrate binding is unsupported, but transient nascent-chain contacts within
  RAC cannot be excluded from the available evidence.
- Nuclear and plasma-membrane localizations are unsupported for Ssz1. Cytoplasm
  and cytosol remain consistent with RAC at the cytoplasmic ribosome.

## 2026-08-28 completion audit

- Reconciled the review against all 75 GOA rows, which collapse to 30 unique
  term/evidence/reference/qualifier signatures in the YAML; every non-NEW row now
  records its GOA qualifier explicitly.
- Audited all eight IBA rows against the current PTHR45639 PAINT snapshot. The
  active nodes are PTN002321897 (cytoplasm), PTN002500132 (nucleus/cytosol), and
  PTN000452648 (ATP hydrolysis, heat-shock-protein binding, protein-folding
  chaperone, and protein refolding).
- Corrected the localization interpretation. Plasma membrane remains REMOVE, but
  its root cause is `SOURCE_STALE_OR_MISSING`: the pinned GOA row points to
  PTN002500132, while the current PAINT snapshot has no plasma-membrane assertion
  at that node. Nucleus remains REMOVE with `PROPAGATION_BAD`: PMID:20368619
  directly localizes Jjj1/Zuo1 and discusses Ssb nuclear cycling, whereas its only
  Ssz1-specific result is 27S rRNA precursor accumulation in an SSZ1 deletion.
  That phenotype supports GO:0006364 rRNA processing, not `is_active_in nucleus`.
  [PMID:20368619 "When compared with WT cells, we observed a strong accumulation
  of the 27S rRNA precursor in Δjjj1 and Δzuo1 strains as well as in Δssz1 and
  Δssb1/2"]
- Retained the refolding IBA as `MARK_AS_OVER_ANNOTATED`. Its supported related
  biology is already represented by two accepted GO:0051083 de novo
  cotranslational-folding rows, so a redundant MODIFY replacement would weaken
  the explicit record of the canonical-Hsp70 transfer error.
- Added a NEW GO:0022626 `cytosolic ribosome` annotation and the same location to
  `core_functions`, directly supported by the original RAC study. [PMID:11274393
  "Zuotin and Ssz1p form a ribosome-associated complex (RAC) that is bound to the
  ribosome via the zuotin subunit."]
- RAC membership is captured explicitly in the core-function description and
  evidence, but no `in_complex` GO identifier was asserted: the review found no
  RAC-specific GO cellular-component term, and using generic `ribosome` as a
  complex would falsely imply that Ssz1 is a structural ribosomal subunit. The
  earlier protein-binding wording was corrected so it no longer claims a
  nonexistent RAC complex annotation.
- PAINT `source_label` values now use each exact bare machine identifier
  (`PANTHER:PTN...`) rather than an invented descriptive node label.
- The review is now COMPLETE: ATP binding is retained, ATP hydrolysis remains
  removed as a lost Hsp70 subactivity, generic protein-binding rows remain
  over-annotated, and the experimentally supported cotranslational-folding,
  translational-fidelity, frameshifting, and ribosome-biogenesis annotations are
  retained at core or non-core scope as appropriate. Cytosol is retained as the
  broad core compartment, while all still-broader cytoplasm rows are consistently
  non-core.
