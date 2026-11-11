# AZIN2 notes

## 2026-10-24 ORGANELLES batch 2 (mitochondrion rows)

- Row: GO:0005739 mitochondrion, IEA, GO_REF:0000107 (Ensembl Compara projection from mouse Azin2 Q8BVM4 / ENSMUSP00000030581). Previously KEEP_AS_NON_CORE with a generic reason. No sub-compartment rows.
- Source check (QuickGO, GO:0005739 on Q8BVM4): two mouse rows, an MGI IDA located_in on PMID:16916800 and a UniProt IDA NOT|located_in on PMID:19449338. The projection carried the positive row only.
- PMID:16916800 (abstract only) gives a crude fraction: [PMID:16916800 "ODCp protein was mainly localized in the mitochondrial/membrane fraction"]. A mitochondrial/membrane pellet without organelle markers cannot separate mitochondria from ER/Golgi/vesicle membranes.
- PMID:19449338 (same group, abstract only) localizes transfected AZIN2 to the early secretory pathway: [PMID:19449338 "AZIN2 was located in the ER-Golgi intermediate compartment (ERGIC) and in the cis-Golgi network"].
- Human UniProt SUBCELLULAR LOCATION lists nucleus, cytoplasm, perinuclear region, membrane, cytoplasmic vesicle, ERGIC, cis- and trans-Golgi network, granules, axon, dendrite and perikaryon; no mitochondrion.
- Outcome: organelle claim not supported -> MARK_AS_OVER_ANNOTATED (not REMOVE, since the projection faithfully copies a real, if superseded, experimental row). No sub-compartment considered. Added PMID:16916800 and PMID:19449338 to references.
