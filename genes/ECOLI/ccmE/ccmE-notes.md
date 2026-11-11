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


## 2026-11-06 system I comparative reassessment

Binds heme transiently and covalently as a membrane-anchored periplasmic chaperone and delivers it to the heme-ligation machinery. The E. coli evidence is distinguished from heterologous ortholog assays and engineered expression constructs.

Read the full 2023 E. coli structures (PMID:37626034), 2025 CcmB efflux work (PMID:40026579) and CcmCD crosslink mapping (PMID:40167305). The studies disagree about the heme conduit. ATP-dependent holo-CcmE release and covalent loading remain supported; heme contact, engineered overexpression, and proposed channel models are distinguished from purified vectorial transport. Broad intracellular heme handoff is not equivalent to membrane translocation. The 2025 review PMID:40460019 is abstract-only and is not used to settle this disagreement.

Specific reassessment: Binds heme transiently and covalently as a membrane-anchored periplasmic chaperone and delivers it to the heme-ligation machinery.

Default Falcon was genuinely attempted and failed with HTTP403 authentication; no provider report was created. Manual literature assessment is recorded here. Original seed rows (including inherited NEW), raw UniProt/GOA, and existing provider files are preserved against original-members-baseline.json. Focused validation and helper history are recorded in the original-panel audit ledger.


## PR6121 round-1 evidence correction (2026-11-06)

- GO:0017003 ACCEPT retained; clarify current definition and distinct own-adduct versus downstream-delivery claims. Historical redundant NEW retained.

Current GO definitions were checked against the official QuickGO API. All original annotation payloads, including authored NEW rows, are preserved. Primary scope and construct limits remain explicit; no raw UniProt/GOA, provider report or publication cache was edited. Scoped comparative proof is recorded in the round-1 audit.

The historical NEW GO:0018063 duplicates current MODIFY replacements. It is retained by explicit parent instruction to preserve the frozen assertion; archival withdrawal would require a separate exact-payload preservation change and aggregate-checker reconciliation. This is annotation redundancy, not a disputed molecular role.


## PR6121 reference-finding follow-up (2026-11-06)

Narrowed the top-level finding statements for PMID:40167305 to the claims established by their existing quoted passages. Annotation actions, core functions, quotes and source records are unchanged. The original 52-file handoff remains preserved and verified separately; this edit has a supplemental history and manifest.


## PR6121 provenance and redundancy follow-up (2026-11-06)

The redundant historical GO:0018063 NEW proposal is now retired in place using the schema's retired flag. Its row order, source payload, supporting quotations and historical action remain, with the exact prior row additionally recorded in analysis/module_audits/bacterial_cytochrome_c_maturation_system_i/retired-ccme-proposal.yaml. The true process remains asserted by the two GO:0017004 MODIFY replacements and by the core function; no REMOVE action is used for duplication. The core list omits the redundant GO:0017003 ancestor while retaining its distinct His130-adduct chemistry in prose and the accepted original annotation. GO:1903607 is retained: it is not in the current is_a/part_of ancestor closure of GO:0018063, so no unsupported hierarchy equivalence is asserted.

Standard record-section backfill derives the UniProt quote provenance; these metadata additions do not change the quoted source text or underlying functional assertions.
