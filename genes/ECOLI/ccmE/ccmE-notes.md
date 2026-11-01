# ccmE (P69490, b2197) notes

## Deep research status

2026-10-23: `just deep-research-falcon ECOLI ccmE` was attempted and failed with
`Exception: Failed to authenticate`; no other provider credentials were available.
This review is therefore based on the cached publications and the UniProt record.

## Biology

- CcmE is the periplasmic heme chaperone of system I [PMID:9712585 "an Escherichia coli hemoprotein, CcmE, was shown to bind heme in the bacterial periplasm by way of a single covalent bond to a histidine"].
- Monotopic inner-membrane protein; the anchor matters for heme receipt but not delivery [PMID:16364305 "heme delivery from CcmE does not involve the membrane anchor"].
- Heme loading occurs in a CcmCDE ternary complex [PMID:15513913 "We demonstrate the formation of a ternary complex consisting of CcmCDE."]; CcmC His60/His184 ligate the heme and CcmE His130 forms the adduct [PMID:19629033 "contributions from which are shown to include CcmC His60 and His184 as iron axial ligands and the CcmE His130 as a covalent adduct"].
- Holo-CcmE heme is oxidized [PMID:19629033 "HoloCcmE is purified in the oxidized (Fe 3+ ) form"].
- CcmAB-dependent ATP hydrolysis releases holo-CcmE from CcmC [PMID:16824107 "In the absence of CcmA or CcmB, holo(haem)CcmE binds to CcmC in a stable dead-end complex"].
- The CcmABC heme-transporter model is disproven [PMID:24044352 "It was thought that CcmABC form a ATP-driven heme transporter,14 but this has since been disproven."].
- Holo-CcmE delivers heme to CcmF/CcmH [PMID:11744735 "CcmF interacts directly with the heme donor CcmE and with CcmH but not with apocytochrome c"].

## Curation decisions

- Five bare protein-binding IPI rows: REMOVE per protein-binding policy (interactions are real).
- Protein-heme linkage and cytochrome complex assembly: MODIFY to GO:0018063 cytochrome c-heme linkage (is_a descendant); NEW GO:0018063 row added.
- ABC transporter complex (NAS) and heme import across plasma membrane (NAS): REMOVE; CcmE is the client released by CcmABCD, and heme import into the cytosol is the wrong direction.
- Heme binding and cytochrome c biosynthetic process rows: ACCEPT.
