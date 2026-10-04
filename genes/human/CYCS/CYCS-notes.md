# CYCS notes

## 2026-09-30 APOPTOSIS review

- Re-reviewed all 73 human CYCS GOA rows, including the 20 new Haenig et al.
  neurodegeneration interactome `GO:0005515 protein binding` rows seeded by
  the refreshed GOA import.
- Kept CYCS centered on two activities: heme-dependent electron transfer from
  Complex III to Complex IV in the mitochondrial intermembrane space, and
  cytochrome-c-dependent APAF1 apoptosome assembly after release into the
  cytosol during intrinsic apoptotic signaling.
- Tightened broad apoptosis rows from `GO:0006915 apoptotic process`,
  `GO:0097190 apoptotic signaling pathway`, and
  `GO:0097194 execution phase of apoptosis` to
  `GO:0097193 intrinsic apoptotic signaling pathway`.
- Removed the APAF1 `GO:0005515 protein binding` rows rather than assigning an
  ill-fitting molecular-function replacement; the curated representation is
  CYCS `part_of` the apoptosome and contributing to apoptotic
  procaspase-9-activator activity.
- Removed all high-throughput generic `GO:0005515` rows from IntAct/BioPlex or
  yeast two-hybrid interactome screens, including all 21
  PMID:32814053-derived partner edges, because the source edges do not establish
  a specific CYCS respiratory or apoptotic mechanism.
- Modified Reactome mitochondrial-inner-membrane projections to
  `GO:0005758 mitochondrial intermembrane space` because mature CYCS is the
  soluble IMS carrier that transiently contacts inner-membrane complexes rather
  than an inner-membrane component.
- Removed the Reactome cytosol localization from the CYCS expression event; that
  row described translation of the nuclear-encoded precursor, not a functional
  mature CYCS localization.
- Flagged PMID:10383829 as a wrong identifier for the `GO:0045333 cellular
  respiration` row and replaced that broad assertion with the two specific
  mitochondrial electron-transfer processes already represented by stronger
  pathway evidence.
