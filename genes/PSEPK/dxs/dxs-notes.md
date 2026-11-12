# dxs (Q88QG7, PP_0527) - Pseudomonas putida KT2440 - review notes

## 2026-11-12 completion pass (thiamine diphosphate biosynthesis batch)

Deep-research providers were not available in this session. The existing
`dxs-deep-research-openscientist.md` was used; none of the primary papers it cites
(PMID:30203647, 23072514, 17135236, 39268973, 28636325, 24767541, 20808315, 37567475,
31500633, 21366531, 40784416) is cached in `publications/`, so quotes are taken from
the UniProt record and the provider report only. No KT2440 experiment on Dxs itself is
known; all functional claims are family inference (HAMAP MF_00315, TIGR00204, PANTHER
PTHR43322:SF5).

### Evidence

- Function, cofactors (UniProt, HAMAP MF_00315): "Catalyzes the acyloin condensation reaction between C atoms 2 and 3 of pyruvate and glyceraldehyde 3-phosphate to yield 1-deoxy-D-xylulose-5-phosphate (DXP)"; "Binds 1 Mg(2+) ion per subunit."; "Binds 1 thiamine pyrophosphate per subunit."; "Belongs to the transketolase family. DXPS subfamily."
- Branch point [file:PSEPK/dxs/dxs-deep-research-openscientist.md, quoting PMID:30203647: "feeds into three separate essential pathways for bacterial central metabolism: ThDP synthesis, pyridoxal phosphate (PLP) synthesis, and the MEP pathway for isoprenoid synthesis"].
- KT2440 uses only the MEP route [same report, quoting PMID:31500633: "In P. putida and most other bacteria, these precursors are produced from pyruvate and glyceraldehyde 3-phosphate by the methylerythritol 4-phosphate (MEP) pathway"].

### Decisions

- GO:0000287 Mg binding, GO:0030976 ThDP binding: KEEP_AS_NON_CORE (cofactor context).
- GO:0005829 cytosol: KEEP_AS_NON_CORE (soluble, no signal or TM).
- GO:0008661 DXP synthase activity: ACCEPT (core MF).
- GO:0009228 thiamine biosynthesis: ACCEPT. Dxs catalyses formation of DXP, the substrate ThiG condenses into the thiazole; it does a step, not merely supply a requirement.
- GO:0016114 terpenoid biosynthesis: MARK_AS_OVER_ANNOTATED. The earlier reason (redundant parent of GO:0019288) was wrong: runoak on the local GO db shows GO:0016114 is not an ancestor of GO:0019288. The term describes a downstream process that Dxs does not perform. Consistent with KT2440 ispE/F/G/H.
- GO:0016744 transketolase or transaldolase activity: changed KEEP_AS_NON_CORE -> TOO_GENERAL (is_a ancestor of GO:0008661, which is asserted; runoak ancestors of GO:0008661 = GO:0016744 > GO:0016740 > GO:0003824).
- GO:0019288 MEP pathway IPP biosynthesis: ACCEPT (core BP).
- core_functions: dropped the UniProt keyword quote ("Thiamine biosynthesis"), which restates an annotation, in favour of the cofactor note and the branch-point quote.
