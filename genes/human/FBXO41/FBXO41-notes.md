# FBXO41 review notes

## 2026-07-14 cerebellum-development audit

- Rechecked all 14 GOA-derived annotations and the two pre-existing proposed
  annotations against the reviewed UniProt record, the Falcon deep-research report,
  full-text PMID:31160656, full-text PMID:26063905, and FBXO41's role in
  `modules/cerebellum_development.yaml`.
- The module places FBXO41 in the post-specification granule-cell migration program.
  This is supported by the existing proposed GO:0001764 `neuron migration` annotation:
  cytoplasmic Fbxo41 rescue and gain-of-function experiments alter migration from the
  external granule layer toward the internal granule layer [PMID:26063905 "Collectively,
  these data indicate that the FBXO41 RNAi-induced phenotype is specific to FBXO41 and
  suggest that cytoplasmic FBXO41 is crucial to stimulate the migration of cerebellar
  granule neurons"].
- Kept the 10 Reactome cytosol rows as non-core pathway context. They are legitimate
  machine-sourced rows but do not constitute FBXO41-specific experimental localization;
  the general SCF core function therefore no longer asserts cytosol as its activity
  location.
- Accepted the centrosome annotation as a core functional location because the ortholog
  is experimentally localized to centrioles/centrosomes and this is the site from which
  increased Fbxo41 drives cilium shortening [PMID:31160656 "Super-resolution stochastic
  optical reconstruction microscopy (STORM) revealed that Fbxo41-EGFP resides adjacent
  to centrosomal protein 135 (Cep135), a centriole proximal-end protein"].
- Added a proposed GO:1990756 `ubiquitin-like ligase-substrate adaptor activity`
  annotation by orthology-supported inference. The study establishes F-box-dependent
  SKP1/CUL1 assembly, and UniProt describes human FBXO41 as the SCF substrate-recognition
  component. This does not imply that FBXO41 itself catalyzes ubiquitin transfer, and a
  physiological FBXO41 substrate remains unknown [PMID:31160656 "Indeed, Fbxo41
  associated with Skp1 and Cullin1, albeit less efficiently than Fbxo21 which was
  included as a positive control. Deleting (Fbxo41ΔF-box) or mutating (Fbxo41W577A)
  the F-box domain abolished these interactions"].
- Recorded GO:0019005 `SCF ubiquitin ligase complex` in `in_complex` for the synthesized
  core activities rather than treating the complex as a cellular location.
- The cilium-disassembly proposal remains deliberately qualified: increased Fbxo41 is
  sufficient to shorten/disassemble cilia, but knockdown did not alter basal cilium
  length and PDBU can drive disassembly without Fbxo41. The review therefore does not
  claim that FBXO41 is universally required for cilium disassembly or identify an
  unknown ciliary ubiquitination substrate [PMID:31160656 "PDBU induces cilia
  disassembly and increased Fbxo41 centrosomal expression in cultured neurons, but
  PDBU-dependent cilia disassembly is not dependent on Fbxo41"].

