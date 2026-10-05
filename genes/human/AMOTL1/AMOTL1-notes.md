# AMOTL1 (Q8IY63) review notes

## 2026-10-04: PAINT/affinage review

AMOTL1 is a tight-junction scaffold of the angiomotin family.
- **YAP1:** [PMID:21187284 "We demonstrate that AMOTL1 and AMOTL2 can regulate YAP1 cytoplasm-to-nucleus translocation through direct protein-protein interaction, which can occur independent of YAP1 phosphorylation status."]
- **PDZ motif:** the C-terminus is ...EVLI, a class II PDZ-binding motif.

Decisions:
- **22 protein-binding rows from the PDZ-PBM affinity screen, plus MPDZ (BioPlex) and NHERF2 (cell map): MODIFY to GO:0030165 PDZ domain binding.** This is the same treatment as AKIP1.
- **Two YAP1 protein-binding rows: MODIFY to GO:0050699 WW domain binding.**
- **PMID:16019084:** its abstract describes MASCOT, which is AMOTL2 (KIAA0989), but the title covers the family. The tight junction and identical-protein-binding IDA rows are ACCEPTed, deferring to the full-text curator.
- **Accepted:** tight junction, plasma membrane, apical membrane, cytosol and Hippo signaling rows.
- **Kept as non-core:**
  - angiogenesis, migration, polarity and actin rows (family IBAs);
  - lamellipodium and vesicle;
  - COP9 colocalization (a proteomic survey).

## Round 1 (PR #4036 review)

Evidence grounding is fixed; no actions changed.
- **TJ and apical rows** now rest on the AMOTL1-specific JEAP discovery paper (PMID:11733531) and the Amot/JEAP-MUPP1 study (PMID:17397395). The AMOTL2 abstract from PMID:16019084 no longer supports any row; it is cited only for the deferred IDA rows.
- **PDZ rows** now rest on the UniProt PDZ-binding motif (953-956) and on JEAP binding MUPP1 PDZ3 via its C-terminal motif (PMID:17397395).
  - The fragmentomics rows disclose that AMOTL1 appears only in that paper's supplementary data.
  - The BioPlex and cell-map rows are described as cellular co-purification, without the screen caveat.
- **Each non-core IBA** has its own node-aware reason:
  - Donors are mainly AMOT and AMOTL2 orthologs, with mouse Amotl1 on migration, vesicle and polarity.
  - Angiogenesis cites AMOTL1-specific endothelial evidence (HECW2 study, PMID:27498087).
- **Duplicate supported_by entries removed;** verified structurally from the rebuilt file.
