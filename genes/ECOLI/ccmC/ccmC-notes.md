# ccmC (P0ABM1, b2199) notes

## Provenance / process

- 2026-10-23: Deep research could not be run. `just deep-research-falcon ECOLI ccmC`
  failed with `Exception: Failed to authenticate`, and no other provider credentials
  were available. This review is based on the cached publications cited in GOA and in
  the system I module (`modules/bacterial_cytochrome_c_maturation_system_i.yaml`), the
  UniProt record, and the reviewed P. putida ortholog (`genes/PSEPK/ccmC`).

## Biology

- Six-TM inner-membrane protein, CcmC/CycZ/HelC family (heme-handling protein
  superfamily with the WWD motif). [PMID:10998170 "CcmC, an integral membrane protein with six transmembrane helices, is necessary and sufficient to incorporate haem covalently into CcmE."]
- Only Ccm protein strictly required for holo-CcmE formation; works without CcmAB when
  overexpressed. [PMID:10339610 "it is the only Ccm protein that is strictly required for heme transfer and attachment to CcmE"]
- Binds heme directly. [PMID:11384983 "Here, we report that the CcmC protein directly interacts with heme."]
- His60/His184 are the heme axial ligands in the purified CcmCDE complex.
  [PMID:19629033 "Haem in this holoCcmCDE complex is bound using periplasmic axial ligands His60 and His184 of CcmC, establishing that CcmC binds haem"]
- WWD domain binds heme and orients the 2-vinyl for attachment to CcmE His130.
  [PMID:29518410 "For holoCcmE this trafficking culminates in the covalent attachment of the 2-vinyl of heme to the CcmE His130 residue."]
- Holo-CcmE stays trapped on CcmC without CcmAB; ATP-dependent release from CcmA2B1C1.
  [PMID:16824107 "In the absence of CcmA or CcmB, holo(haem)CcmE binds to CcmC in a stable dead-end complex, indicating high affinity binding of haem to CcmC."]
- Heme export by CcmABC is not established.
  [PMID:24044352 "It was thought that CcmABC form a ATP-driven heme transporter,14 but this has since been disproven."]
  [PMID:10708391 "suggesting that the activity of neither the CydDC nor CcmAB transporters is essential for haem export to the periplasm"]

## Curation decisions (summary)

- Core: heme binding (GO:0020037), protein-heme linkage (GO:0017003, heme onto CcmE),
  cytochrome c biosynthetic process (GO:1903607), plasma membrane.
- Catalase activity IBA (single P. aeruginosa CcmC IMP donor, Q9I3N5) and the derived
  oxidant-detoxification IEA removed: mutant phenotype, not CcmC catalysis.
- Heme transmembrane transporter / heme transport IEA marked over-annotated (not REMOVE:
  route of heme to the periplasmic WWD domain is unresolved). Heme import across plasma
  membrane NAS removed (wrong direction, contradicted by the cited paper).
- ABC transporter complex NAS kept as non-core (complex membership real, transport not shown).
- Nine bare protein-binding IPI rows removed per policy (interactions with CcmA, CcmD,
  CcmE are real).
