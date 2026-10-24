# mek-1 research notes

Review date: 2026-09-09T03:17:51.839101+00:00. Target: Q7RYZ6, NEUCR, 518 residues. Identity is anchored to the frozen current UniProt accession and gene record. The accession-specific fetch seeded all 16 current GOA rows.

## Evidence basis

MEK-1 is the MAP kinase kinase of the Neurospora crassa MIK-1–MEK-1–MAK-1 signaling module. It is required for MAK-1 phosphorylation and helps control cell wall integrity, vegetative growth, asexual development and sexual differentiation. MEK-1 also accumulates at the contact sites of fusing germlings, linking this signaling module to local remodeling during cell fusion.

- PMID:18849472: “The MAK-1 MAPK was not phosphorylated in Δ mik-1 and Δ mek-1 mutants, consistent with the involvement of MIK-1, MEK-1, and MAK-1 in the same signaling cascade.”
- PMID:41071819: “In a first step, we confirmed the accumulation of the kinase MAK-1 at the contact sites and showed the same localization pattern for both its upstream kinases (Fig 7).”

## Source claim provenance

The full API prediction JSON is preserved without deleting any fields. Function and location reports retain original words, SL identifiers and entire evidence objects. GO sidecars preserve all emitted GO IDs and labels; main reviews assess the independent current GOA rows.


## Research execution

The original Falcon report returned and was inspected. Publication caching ran concurrently. The report is retained as received; consequential claims are checked against primary sources and sequence evidence below.

## Falcon report appraisal

The 342.39-second original Falcon report correctly distinguishes NCU06419/mek-1 from mek-2 and identifies the middle kinase of the cell-integrity cascade. Its principal primary source, PMID:22900028 (DOI:10.1371/journal.pone.0042565), was cached and inspected: Table 1 maps Δmek-1 to NCU06419 and the developmental analysis distinguishes the CWI module. The report’s claim that no direct MEK-1 localization was found is a search limitation. Independently recovered PMID:41071819 contains direct MEK-1-GFP microscopy at germling contacts (Figure 7B); the whole cached results section was inspected. This supports cytoplasmic/cortical localization, not division septum or diffuse uniform cytosol. PMID:18849472 directly shows dependence of MAK-1 phosphorylation on mek-1. The report’s serine/threonine-only substrate shorthand is not used to displace the established MAPKK functional class; specific target biochemical kinetics remain unmeasured. QuickGO definitions of MAP kinase and MAP kinase kinase were checked before modifying the EC-derived MAPK row.

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 output was not opened or used. All 16 GOA rows were re-examined against the cached full texts (PMID:18849472, PMID:22900028, PMID:21666072, PMID:41071819), the UniProt record, and the PANTHER family review.

### Identity
- Q7RYZ6 is the only UniProt entry for NCU06419 (TrEMBL, 518 aa, sequence version 3). It is the canonical product, not a fragment or isoform.
- Park et al. 2008 (PMID:18849472) describe MEK-1 as 485 aa: "mik-1, mek-1 , and mak-1 encode proteins of 1779, 485, and 455 amino acids, respectively." That length comes from an earlier gene model. The current 518-aa model differs in the disordered N-terminal region (residues 1-142, MobiDB-lite). The kinase domain (221-491) is intact, with the ATP-binding K250 and catalytic HRD D348 (PROSITE PRU10141/PRU10027). No catalytic residue or domain is missing.

### Evolutionary placement
- UniProt cross-references: PTHR47448:SF5 ("MITOGEN-ACTIVATED PROTEIN KINASE KINAE MKK2"). S. pombe Pek1/Skh1 (Q9Y884) has the same placement.
- PANTHER's per-organism classification, as recorded in interpro/panther/PTHR47448/PTHR47448-review.yaml, places Q7RYZ6 and Q9Y884 in PTHR48013:SF6 instead. UniProt also gives S. cerevisiae Mkk1 (P32490) and Mkk2 (P32491) as PTHR48013:SF6 ("MAP KINASE KINASE MKK1_SSP32-RELATED"), checked by UniProt REST on 2026-10-21.
- The two sources disagree on the parent family, PTHR47448 vs PTHR48013 (this disagreement is already logged in the family review, which is IN_PROGRESS). Both sources still put MEK-1 in the same subfamily as Pek1, and PANTHER's own files also group it with Mkk1/Mkk2. The donors of PAINT node PTN001220604 (Pek1, Mkk1, Mkk2) sit in that same clade, so the CWI-cascade IBAs are phylogenetically sound.

### Changes made
- GO:0004707 MAP kinase activity (IEA, EC 2.7.11.24 via ARBA): changed from MODIFY to REMOVE. The EC mapping is demonstrably wrong. MEK-1 is the MAPKK, not a MAPK, and GO:0004708 is not a descendant of GO:0004707, so a replacement is not a refinement. The correct activity is already present on independent rows.
- Added a note on the PANTHER source disagreement to the IBA GO:0004708 row.
- Added the missing `title` to the UniProt file reference. Its absence caused a schema error.
- All other actions were re-checked and kept. GO:0004708 is_a GO:0004712 (Ser/Thr/Tyr kinase), not GO:0004674, checked against OLS4 ancestors, so the MODIFY of the Ser/Thr row stands. GO:0000196 is_a GO:0000165, so the MODIFY of the MAPK cascade row stands. Division septum and positive regulation of calcium-mediated signaling (Compara transfers of Pek1-specific data) stay UNDECIDED.

### Relative to review next
S. pombe pek1 (Q9Y884, SPBC543.07). It is co-placed with MEK-1 under both PANTHER sources and is a donor to PTN001220604 and to the Compara rows. The repo has no review of it. The S. cerevisiae Mkk1/Mkk2 (P32490/P32491) are not reviewed either.

### Modules
No module in modules/ covers the fungal CWI MAPK cascade or MEK-1.
