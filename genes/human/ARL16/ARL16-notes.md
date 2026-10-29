# ARL16 notes

- RIG-I inhibitor [PMID:21233210], human cells:
  - GTP-bound ARL16 binds the RIG-I CTD and blocks RNA binding.
  - Knockdown potentiates virus-induced IFN-beta.
- Cilia [PMID:35196065]:
  - Endogenous ARL16 sits along the ciliary axoneme in human RPE1 cells, plus cytosol and mitochondria (HSP60).
  - In human retina it is in the photoreceptor ciliary region and inner segment.
  - Arl16 knockout MEFs: fewer but longer cilia; IFT140 and INPP5E stuck at the Golgi.
- Atypical G-3 motif [PMID:38606629].

## GOA calls
- **Protein binding (30 rows) → REMOVE.** These are Y2H screens (neurodegeneration map, HuRI, HI-II-14) plus RIG-I. The RIG-I biology moves to a NEW BP row.
- **ACCEPT:** GTP binding, axoneme, cytoplasm.
- **UNDECIDED:** GTPase activity (atypical G-3; no hydrolysis measured).
- **Non-core:** mitochondrion, photoreceptor inner segment.
- **NEW:**
  - Negative regulation of RIG-I signaling pathway (IMP, human).
  - Protein localization to cilium (ISO from mouse Arl16, MGI:1917567).

## Review round 1 (PR #4178)
- NEW ciliary basal body (IDA, PMID:35196065), from the photoreceptor centrin 3 co-staining; UniProt records this location but GOA lacks it. Added as a core-function location.
- GTP binding now quotes the radiolabelled-GTP binding assay and the T37N / delta45-54 GTP-free mutants (PMID:21233210).
- Cytoplasm rows now quote only the diffuse cytosolic staining.
- Mitochondrion row notes the authors' attribution to a longer ARL16 variant.
- ISO donor MGI:1917567 verified as mouse Arl16 (UniProt B1ATY8).

## 2026-10-24 ORGANELLES batch 2 (mitochondrion rows)

- Rows: GO:0005739 EXP (PMID:35196065) and IEA (GO_REF:0000044, SL-0173). Both stay KEEP_AS_NON_CORE; reasons now record the check.
- EXP is direct (rule 2). Endogenous ARL16 co-stains with HSP60 [PMID:35196065 "ARL16 also localized to both the cytosol and the mitochondria, as evidenced by its diffuse staining across the cell and colocalization with the mitochondrial protein HSP60, respectively (Supplemental Figure S2A)."]. The expressed long variant is mitochondrial [PMID:35196065 "In contrast, the 197 residue human variant displayed little evidence of diffuse, cytosolic localization."]. The assay resolves the organelle only.
- IEA: SL-0173 carries ECO:0000269 from PMID:35196065 in UniProt, so the mapping is sound.
- Rule 4: stays at the root because there is only one weak line. The canonical 173-residue chain has no presequence or TM. The mitochondrial signal is attributed to an N-terminally extended variant that UniProt lists only under a sequence caution ("Erroneous initiation; Note=Extended N-terminus"). Whether that extension is a presequence is untested, and there is no fractionation.
- Outcome: root.
