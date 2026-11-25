# TRAF3IP3 notes

## 2026-11-25 GO-CAM 65bc474400000029 review

The local `deep-research-falcon` recipe was attempted with a `perplexity-lite`
fallback, but neither `falcon` nor `perplexity` was available in this runtime.
These notes therefore summarize the cached publications and UniProt record used
for the manual review.

### Core biology

- In the 65bc GO-CAM mechanism, TRAF3IP3 accumulates at the mitochondrial MAVS
  platform after RNA-virus infection and bridges MAVS to TRAF3 for TBK1-IRF3
  activation [PMID:31390091, "TRAF3IP3 is accumulated on mitochondria and
  thereby facilitates the recruitment of TRAF3 to MAVS for TBK1-IRF3
  activation"].
- TRAF3IP3 has other compartment-specific immune adaptor roles: MEK recruitment
  to Golgi for BRAF-MEK-ERK signaling in thymocytes [PMID:26195727, "recruiting
  MEK to the Golgi"], TLR4 lipid-raft translocation in macrophages
  [PMID:30573680, "T3JAM associates with TLR4, promotes its translocation to
  lipid rafts"], and PP2Ac recruitment to lysosomes in regulatory T cells
  [PMID:30115741, "TRAF3IP3 recruits PP2Ac to the lysosome in T reg cells"].
- TRAF3IP3 can also dampen cytosolic RNA-induced antiviral signaling by
  promoting K48-linked TBK1 ubiquitination [PMID:32366851, "TRAF3IP3
  specifically increased K48-linked but not K63-linked polyubiquitination of
  TBK1"]. That is real biology, but the current seeded GOA rows around
  PMID:31390091 correctly capture the positive MAVS-to-TRAF3 adaptor role in
  the 65bc model.
- The many `GO:0005515` IPI rows from HuRI/BioPlex and other interactome
  screens were removed or refined under the generic protein-binding policy. The
  screen edges should not be read as false merely because the bare GO term is
  uninformative.

### GO-CAM consistency notes

- The 65bc GO-CAM's TRAF3IP3 activity is consistent with the gene review:
  `GO:0030674 protein-macromolecule adaptor activity` at the mitochondrial
  outer membrane in cytoplasmic pattern-recognition receptor signaling.
- The MGI `GO:0000139 Golgi membrane`, `GO:0005789 endoplasmic reticulum
  membrane`, and `GO:0031966 mitochondrial membrane` rows from PMID:31390091
  are co-dated, consistent with a compartment-localization experiment in the
  paper's uncached Results rather than with a one-off Golgi reference
  transposition. The gene review therefore does not record a source defect on
  the Golgi row.
- The MGI `GO:0044198 zf-TRAF domain binding` row cites PMID:31390091 but has
  MAVS in `With/From`; the gene review modifies that row to TRAF3IP3's
  demonstrated protein-macromolecule adaptor activity rather than proposing a
  precise With/From correction.
