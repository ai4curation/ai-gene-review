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
- Nuclear and plasma-membrane IBA localizations are unsafe Hsp70-family
  transfers. Cytoplasm/cytosol are consistent with the characterized site of
  action, with RAC positioned at the cytoplasmic ribosome.
