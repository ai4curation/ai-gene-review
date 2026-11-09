# HADHB Review Notes

## 2026-02-05: Initial Review

### Context
HADHB was identified during analysis of human Recon3D metabolic model as having a gene-reaction misassignment error. This prompted a full GO annotation review.

### Recon3D Model Error

**Finding**: HADHB (Entrez ID 3034) is incorrectly assigned to histidase reaction (HISDr, EC 4.3.1.3) in Recon3D instead of fatty acid beta-oxidation thiolase reactions.

| Source | Reaction | EC | Subsystem |
|--------|----------|-----|-----------|
| Recon3D | HISDr (Histidase) | 4.3.1.3 | Histidine metabolism |
| Correct | ACACT*, KAT* (Thiolases) | 2.3.1.155, 2.3.1.16 | Fatty acid oxidation |

**Impact**: The correct thiolase reactions exist in Recon3D with GPRs containing 3030 (HADH), 3032 (HADH), 10449 (ACAA2) but are missing 3034 (HADHB). This means:
1. HADHB knockout simulations would incorrectly predict no effect on fatty acid oxidation
2. Histidine metabolism simulations would incorrectly include HADHB

**Root cause**: Likely a gene ID mapping error during model construction.

### GO Annotation Errors Found

Two TAS annotations from 2003 (PMID:1550553) incorrectly assign HADHA activities to HADHB:

| GO Term | Activity | Correct Gene |
|---------|----------|--------------|
| GO:0003857 | 3-hydroxyacyl-CoA dehydrogenase | HADHA (alpha) |
| GO:0004300 | enoyl-CoA hydratase | HADHA (alpha) |

**Reason**: PMID:1550553 (1992) characterized the whole MTP complex before subunit-specific activities were known. PMID:8135828 (1994) later showed:
- Alpha subunit (HADHA): hydratase + dehydrogenase activities
- Beta subunit (HADHB): thiolase activity ONLY

### Key Literature

1. **PMID:1550553** (Carpenter 1992) - First purification of MTP from human liver, identified as trifunctional
2. **PMID:8135828** (Kamijo 1994) - Cloned both subunits, showed subunit-specific activities via expression
3. **PMID:29915090** (Liang 2018) - Cryo-EM structure of MTP at 4.2Å
4. **PMID:30850536** (Xia 2019) - Crystal structure at 3.6Å, detailed active site analysis

### Disease Association

Mutations in HADHB cause **Mitochondrial Trifunctional Protein Deficiency Type 2 (MTPD2)** [MIM:620300]:
- Autosomal recessive
- Phenotype ranges from fatal early-onset cardiomyopathy to late-onset myopathy with peripheral neuropathy
- Loss of all three MTP activities due to complex destabilization

### Alzheimer's Disease Relevance

HADHB is relevant to AD metabolic dysfunction through:
1. **Mitochondrial fatty acid oxidation** - Major energy source, impaired in AD
2. **Ketone body production** - Thiolase produces acetyl-CoA for ketogenesis
3. **Lipid metabolism** - Dysregulated in AD brains

The Recon3D error could affect metabolic modeling of AD brain metabolism.

## 2026-11-05 ORGANELLES ER batch 2 (endoplasmic reticulum rows)

Rows: GO:0005783 IEA (GO_REF:0000044, SL-0095) and IDA (PMID:21527675); no qualifier recorded in the review; no ER sub-compartment rows.

- UniProt: "Mitochondrion outer membrane {ECO:0000269|PubMed:21527675}. Endoplasmic reticulum {ECO:0000269|PubMed:21527675}." Both rows trace to the viperin/HCMV paper.
- PMID:21527675 (Science 2011; abstract only, no PMC id): the abstract describes viperin relocalizing from the ER to mitochondria and binding the trifunctional protein there; it says nothing about an ER pool of HADHB itself, or about an ER marker. The existing reasons' "viral-induced localization" reading is therefore not established; noted in both reasons.
- Topology: FT TRANSIT 1..33 (mitochondrion); no ER signal, TM or retention motif; any ER pool would be cytosolic-face; stays at root.
- Outcome: both rows stay KEEP_AS_NON_CORE, deferring to the curator's full-text reading; UniProt curated location quote added. Close call with MARK_AS_OVER_ANNOTATED if the ER signal is fractionation cross-contamination (MAM), stated in the reasons.
