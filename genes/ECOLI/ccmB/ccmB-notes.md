# ccmB (P0ABL8, b2200) notes

## 2026-10-23

Deep research could not be run: `just deep-research-falcon ECOLI ccmB` was
attempted on 2026-10-23 and failed with `Exception: Failed to authenticate`, and
no other provider credentials were available. These notes are built from the
fetched UniProt record, the GOA-cited PubMed cache, and the system I module
literature (`modules/bacterial_cytochrome_c_maturation_system_i.yaml`).

### Biology

- CcmB is a six-TM integral inner-membrane protein (UniProt: "Cell inner
  membrane; Multi-pass membrane protein"), topology supported by the global
  E. coli inner-membrane study [PMID:15919996 "we established the periplasmic or cytoplasmic locations of the C termini for 601 inner membrane proteins"].
- CcmB recruits CcmA to the membrane
  [PMID:17419738 "is found in a membrane-bound complex only when CcmB is present in the membrane"].
- CcmB is required for release of holo-CcmE from CcmC
  [PMID:16824107 "In the absence of CcmA or CcmB, holo(haem)CcmE binds to CcmC in a stable dead-end complex"]
  and is thought to relay the CcmA conformational change
  [PMID:24044352 "An ATP-driven conformational change in CcmA, presumably via CcmB, is responsible for removing the heme from CcmC"].
- In-frame ccmB deletion blocks holocytochrome c formation even when holo-CcmE
  forms [PMID:10339610 "The ΔccmAand ΔccmBmutants, however, could not synthesize holocytochromec"].
- Heme export model not supported [PMID:10708391 "suggesting that the activity of neither the CydDC nor CcmAB transporters is essential for haem export to the periplasm"];
  [PMID:24044352 "It was thought that CcmABC form a ATP-driven heme transporter,14 but this has since been disproven."].
  The CcmB UniProt FUNCTION line still states the legacy export model; the
  paired CcmA entry has been revised.

### Curation decisions

- Core function: no MF (CcmB's own activity is undefined; complex-level energy
  coupling); BP GO:1903607; CC plasma membrane. Same approach as PSEPK ccmB.
- REMOVE: 2x bare protein binding (policy); GO:0015232 heme transmembrane
  transporter activity (IEA family-name inference, contradicted); GO:1904334 heme
  import NAS (contradicted by its own cited paper).
- MARK_AS_OVER_ANNOTATED: GO:0015886 heme transport (heme is moved as
  covalent holo-CcmE; CcmB does not transport free heme); GO:0043190 ABC
  transporter complex (as for ccmA).
- MODIFY: GO:0016020 membrane -> GO:0005886; GO:0017004 -> GO:1903607.


## 2026-11-06 system I comparative reassessment

Forms the membrane coupling subunit of CcmABCD, connecting CcmA ATP hydrolysis to heme-chaperone handling and release. The E. coli evidence is distinguished from heterologous ortholog assays and engineered expression constructs.

Read the full 2023 E. coli structures (PMID:37626034), 2025 CcmB efflux work (PMID:40026579) and CcmCD crosslink mapping (PMID:40167305). The studies disagree about the heme conduit. ATP-dependent holo-CcmE release and covalent loading remain supported; heme contact, engineered overexpression, and proposed channel models are distinguished from purified vectorial transport. Broad intracellular heme handoff is not equivalent to membrane translocation. The 2025 review PMID:40460019 is abstract-only and is not used to settle this disagreement.

Specific reassessment: Forms the membrane coupling subunit of CcmABCD, connecting CcmA ATP hydrolysis to heme-chaperone handling and release.

Default Falcon was genuinely attempted and failed with HTTP403 authentication; no provider report was created. Manual literature assessment is recorded here. Original seed rows (including inherited NEW), raw UniProt/GOA, and existing provider files are preserved against original-members-baseline.json. Focused validation and helper history are recorded in the original-panel audit ledger.

Panel source and strain evidence is catalogued in [ccmB-source-analysis/evidence.yaml](ccmB-source-analysis/evidence.yaml); run `.venv/bin/python genes/ECOLI/ccmB/ccmB-source-analysis/verify.py` for quote and source-hash checks. The full supplementary PDF remains in ignored cache.
