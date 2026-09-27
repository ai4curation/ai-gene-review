# nudE (Aspergillus nidulans, O74689) review notes

## 2026-09-27 initial review (claude-code)

Context: comparative NudE-family member of `modules/nucleokinesis.yaml` (human NDE1/NDEL1 reviewed).

Key evidence
- Isolated as multicopy suppressor of nudF7; null viable with nuclear migration, growth and conidiation defects [PMID:10931877 "The nudE null mutant was viable, but displayed impaired nuclear migration, reduced colony growth, and a conidiation defect."].
- Coiled coil binds NudF and alone complements the deletion [PMID:10931877 "the NUDE construct containing the coiled-coil region alone complemented the nudE deletion and suppressed the nudF7 mutation"].
- C-terminal domain targets NudE to plus-end comets but is dispensable; NudF overproduction fully suppresses nudE deletion [PMID:12631710 "Furthermore, NUDF overproduction totally suppressed deletion of the nudE gene."].
- ClipA and NudE redundantly recruit NudF to plus ends [PMID:16467375].
- NudE required for HookA-mediated dynein activation; phi-opening dynein mutations partially bypass [PMID:31562232 "Thus, just like NudF/LIS1, NudE is also required for cargo-adapter–mediated dynein activation."]; early endosomes accumulate at tip in DeltanudE [PMID:31562232].
- PMID:11509576 (claimed direct NudE binding to NudK/Arp1, LC8 and tubulins) is RETRACTED; not used.

Decisions
- NEW MF GO:0140659 cytoskeletal motor regulator activity (module/human NDEL1 term); NEW CC GO:0035371 microtubule plus-end.
- Accept nuclear migration (IMP) and vesicle transport along microtubule (IBA, supported by EE data).
- Animal-specific IBA terms (kinetochore, chromosome segregation/localization, centrosome localization, MT nucleation) marked over-annotated: animal mechanism via CENP-F/centrosome, not documented in fungi; A. nidulans NudE function resides in the coiled coil and is fully bypassed by NudF overexpression.
- Kinesin complex IBA removed (source is rat Ndel1 as kinesin-1 cargo; consistent with human NDE1/NDEL1 reviews).
- Protein binding (NudF) removed as uninformative.

Deep research: no falcon report present at time of review.

## 2026-09-27 falcon deep research incorporated (claude-code)

- Read nudE-deep-research-falcon.md. It agrees that NudE is a NudF-binding coiled-coil accessory regulator, secondary to NudF; no action changed.
- Verified in cached PMID:10931877 and added: extra nudE copies also partially suppress the nudA1 dynein heavy-chain conidiation defect (supports pathway membership; added to the nuclear migration IMP row).
- The report's mention of NudE/NudF binding dynein/dynactin subunits and tubulins derives from the RETRACTED PMID:11509576; excluded.
- The report calls NudE's early-endosome role unproven; this is incomplete retrieval - PMID:31562232 shows early endosomes accumulate at the hyphal tip in DeltanudE, so the IBA GO:0047496 ACCEPT stands.
- Deep-research quote added to the core function.
