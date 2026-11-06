# ccmD (P0ABM5, b2198) notes

## Provenance / process

- 2026-10-23: Deep research could not be run. `just deep-research-falcon ECOLI ccmD`
  failed with `Exception: Failed to authenticate`, and no other provider credentials
  were available. This review is based on the cached publications cited in GOA and in
  the system I module, the UniProt record, and the reviewed P. putida ortholog
  (`genes/PSEPK/ccmD`).

## Biology

- 69-residue single-pass inner-membrane protein, N terminus periplasmic, C terminus cytoplasmic.
  [PMID:18326572 "Evidence is presented that the topology of CcmD in the cytoplasmic membrane is the N terminus outside and the C terminus inside with one transmembrane domain."]
- Interacts with CcmC and CcmE; ternary CcmCDE complex; no detectable heme binding.
  [PMID:15513913 "We demonstrate the formation of a ternary complex consisting of CcmCDE."]
  [PMID:15513913 "Interactions of CcmD with either ferrochelatase, the last heme biosynthetic enzyme, or directly with heme were not detectable."]
- Subunit of CcmABCD; essential for holo-CcmE release, not for heme transfer.
  [PMID:18326572 "CcmD is absolutely required for the release of holo-CcmE from the CcmABCD complex."]
  [PMID:18326572 "CcmD is not necessary for the CcmC-dependent transfer of heme to CcmE in the periplasm or for interaction of CcmE with CcmABC."]
- Conflict: Schulz et al. proposed CcmE stabilisation
  [PMID:10339610 "CcmD was found to be involved in stabilizing the heme chaperone CcmE in the membrane."]
  but Richard-Fogal et al. saw equal CcmE levels with or without CcmD
  [PMID:18326572 "we conclude that CcmD is not essential for heme transfer to CcmE or for the stability or membrane insertion of CcmE"].
  Recorded as a DISPUTED finding_review on PMID:10339610. The module currently phrases
  CcmD's role as stabilising CcmE; the E. coli evidence favours a holo-CcmE release role.
  Flag this for the module curator.

## Curation decisions (summary)

- Core: cytochrome c biosynthetic process (GO:1903607) at the plasma membrane; no defined MF
  (core function omits molecular_function, as in the PSEPK ccmD review).
- ABC transporter complex NAS accepted (membership experimentally shown; CcmD's essential
  role is exerted within this complex).
- Heme transport IEA marked over-annotated; heme import across plasma membrane NAS removed.
- Cytochrome complex assembly (IEA, NAS) modified to GO:1903607; membrane modified to plasma membrane.
- Four bare protein-binding IPI rows removed per policy.
