# imt1 (O14084, SPAC2F3.01) notes

## Evidence journal

- PTHR32385 PAINT places `GO:0000030 mannosyltransferase activity` and `GO:0051999 mannosyl-inositol phosphorylceramide biosynthetic process` on `PANTHER:PTN001285482`, the fungal IPC mannosyltransferase node seeded by CGD `CAL0000176496`, SGD `SUR1`/`CSH1`, S. pombe `imt1`/`imt2`/`imt3`, and A. fumigatus `Q4WDG6`.
- Nakase et al. 2010 showed that S. pombe has three SUR1 homologues, `imt1`, `imt2`, and `imt3`, and that the triple disruptant has no detectable MIPC and accumulates IPC [PMID:20388730 "MIPC was not detected and IPC levels were increased in the triple disruptant, indicating that the three SUR1 homologues are involved in the synthesis of MIPC."].
- The 2010 paper also localizes GFP-Imt1p, GFP-Imt2p, and GFP-Imt3p to Golgi apparatus membranes [PMID:20388730 "GFP-tagged Imt1p, Imt2p and Imt3p localized to Golgi apparatus membranes."].
- The exact catalytic term `GO:0103064 inositol phosphorylceramide mannosyltransferase activity` is sound for Imt1, but PomBase assigns it by ISO from S. cerevisiae Sur1 rather than by a direct imt1-only enzymatic assay.

## 2026-11 newer-literature scan

- Search hit PMID:37792890, a 2023 fission-yeast MIPC/cell-wall study, as newer S. pombe sphingolipid literature. Its full text explicitly places Imt1, Imt2, and Imt3 at the Golgi IPC-to-MIPC step and reports that `imt1D` and `imt2D`, unlike `imt3D`, do not suppress `css1-3`, consistent with distinct IPC-subspecies preferences. This refines the older interchangeability framing but does not justify new downstream `css1` phenotype/process annotations for Imt1.
- Search hit the 2026 inositol-starvation paper by Sanchez et al. as broader fission-yeast inositol-metabolism context. It does not appear to revise Imt1's direct IPC mannosyltransferase role.

## Decisions

- `GO:0000030` IBA is a sound PAINT transfer from `PTN001285482`, but it is too general now that `GO:0103064` exists and is already present on imt1 by ISO.
- `GO:0051999` IBA is ACCEPT: the PAINT node is seeded by S. pombe, SGD/CGD, and A. fumigatus MIPC-synthase evidence and lands on the same term supported by PomBase IMP/IGI rows from PMID:20388730.
- Retain the cis-Golgi/trans-Golgi rows from PomBase. The cached abstract supports Golgi membranes but not cis versus trans resolution; PomBase curators had full text, and UniProt records both specific Golgi network membrane locations.
