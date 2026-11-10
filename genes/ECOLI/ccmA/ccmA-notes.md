# ccmA (P33931, b2201) notes

## 2026-10-23

Deep research could not be run: `just deep-research-falcon ECOLI ccmA` was
attempted on 2026-10-23 and failed with `Exception: Failed to authenticate`, and
no other provider credentials were available. These notes are built from the
fetched UniProt record, the GOA-cited PubMed cache, and the system I module
literature (`modules/bacterial_cytochrome_c_maturation_system_i.yaml`).

### Biology

- The E. coli ccmABCDEFGH cluster is required for maturation of all c-type
  cytochromes [PMID:7635817 "the E. coli ccm gene cluster present in the aeg-46.5 region is required for a general pathway involved in cytochrome c maturation"].
- CcmA is the ATPase subunit; purified CcmAB hydrolyses ATP and the Walker A
  K40D mutation kills both ATPase and cytochrome c biogenesis
  [PMID:17419738 "Mutation of the Walker A motif in CcmA(K40D) results in loss of the in vitro ATPase activity and in loss of cytochrome c biogenesis in vivo"].
- CcmA is membrane-associated only via CcmB
  [PMID:17419738 "is found in a membrane-bound complex only when CcmB is present in the membrane"].
- Function: ATP-dependent release of holo-CcmE from CcmC
  [PMID:16824107 "In the absence of CcmA or CcmB, holo(haem)CcmE binds to CcmC in a stable dead-end complex"];
  [PMID:24044352 "An ATP-driven conformational change in CcmA, presumably via CcmB, is responsible for removing the heme from CcmC"].
- Heme export model not supported:
  [PMID:10708391 "suggesting that the activity of neither the CydDC nor CcmAB transporters is essential for haem export to the periplasm"];
  [PMID:10339610 "We also present evidence that questions the role of CcmAB as a heme exporter; yet, the transported substrate remains unknown."];
  [PMID:24044352 "It was thought that CcmABC form a ATP-driven heme transporter,14 but this has since been disproven."].
  The UniProt FUNCTION text agrees ("once thought to export heme, this does not
  seem to be the case"), but the HAMAP EC 7.6.2.5 / RHEA:19261 mapping still
  drives the IEA GO:0015439 row.
- Cryo-EM structures of the E. coli CcmABCD complex exist (PDB 7F02-7F04,
  7VFJ, 7VFP, 8CE1-8CEA), but the corresponding papers are not in the
  publication cache and were not used.

### Curation decisions

- Core MF: GO:0016887 ATP hydrolysis activity (IDA); BP GO:1903607; CC plasma membrane.
- REMOVE: 4x bare protein binding (policy); GO:0015439 and GO:0022857 transporter
  MFs (EC/family-name inference, contradicted); GO:1904334 heme import NAS
  (contradicted by its own cited paper).
- MODIFY GO:0017004 -> GO:1903607 (IEA and NAS).
- MARK_AS_OVER_ANNOTATED GO:0043190 ABC transporter complex (ABC architecture is
  real but transport is not; no GO term for the CcmABCD release complex,
  ComplexPortal CPX-3568).
- Consistent with the PSEPK ccmA review.


## 2026-11-06 system I comparative reassessment

Hydrolyzes ATP as the nucleotide-binding subunit of CcmABCD, coupling energy to release of heme-loaded CcmE during cytochrome c maturation. The E. coli evidence is distinguished from heterologous ortholog assays and engineered expression constructs.

Read the full 2023 E. coli structures (PMID:37626034), 2025 CcmB efflux work (PMID:40026579) and CcmCD crosslink mapping (PMID:40167305). The studies disagree about the heme conduit. ATP-dependent holo-CcmE release and covalent loading remain supported; heme contact, engineered overexpression, and proposed channel models are distinguished from purified vectorial transport. Broad intracellular heme handoff is not equivalent to membrane translocation. The 2025 review PMID:40460019 is abstract-only and is not used to settle this disagreement.

Specific reassessment: Hydrolyzes ATP as the nucleotide-binding subunit of CcmABCD, coupling energy to release of heme-loaded CcmE during cytochrome c maturation.

Default Falcon was genuinely attempted and failed with HTTP403 authentication; no provider report was created. Manual literature assessment is recorded here. Original seed rows (including inherited NEW), raw UniProt/GOA, and existing provider files are preserved against original-members-baseline.json. Focused validation and helper history are recorded in the original-panel audit ledger.
