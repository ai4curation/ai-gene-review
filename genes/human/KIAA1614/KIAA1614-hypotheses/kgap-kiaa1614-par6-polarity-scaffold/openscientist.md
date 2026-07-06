# KIAA1614 Par6-like Polarity Scaffold Hypothesis: Investigation Report

## Summary Answer

**KIAA1614 should not be annotated as a Par6 polarity scaffold based on current evidence.** The protein lacks all three functional domains (PB1, pseudo-CRIB, PDZ) that define canonical Par6 function, shows negligible sequence similarity to Par6 proteins, is predicted to be almost entirely intrinsically disordered (AlphaFold mean pLDDT = 20.9), and has no experimentally validated binding partners in any polarity complex. The PANTHER family-level classification (PTHR14102) that groups KIAA1614 with Par6 appears to be a distant or erroneous homology call that should not be used to infer molecular function.

---

## 1. Domain Architecture: KIAA1614 vs Canonical Par6

### Canonical Par6 proteins (PARD6A/B/G)
- **Size:** 345-376 amino acids
- **PB1 domain** (residues ~15-95): Mediates heterodimerization with aPKC (PRKCI/PRKCZ) via head-to-tail PB1-PB1 interaction
- **Pseudo-CRIB domain** (~133-150): Binds GTP-loaded Cdc42 and Rac1, regulating aPKC activity
- **PDZ domain** (~157-250): Binds Par3 (PARD3) and PALS1/Crumbs complex, connecting polarity complexes
- **InterPro:** IPR000270 (PB1), IPR034868 (PB1_Par6), IPR001478 (PDZ), IPR036034 (PDZ_sf), IPR051741 (PAR6_homolog)

### KIAA1614 (Q5VZ46)
- **Size:** 1190 amino acids (3.4x larger than Par6)
- **DUF4685** (residues 354-478): Domain of unknown function, found in vertebrates, 106-131 aa, two conserved motifs (SGE, VRF). No known function, no solved structures.
- **NO PB1 domain** — cannot bind aPKC
- **NO pseudo-CRIB domain** — cannot bind Cdc42/Rac
- **NO PDZ domain** — cannot bind Par3 or PALS1
- **InterPro:** IPR032756 (DUF4685), IPR051741 (PAR6_homolog via PANTHER only)
- **Disorder:** 61.2% of residues in annotated disordered regions; AlphaFold mean pLDDT = 20.9 (87% of residues < 50)

### Sequence similarity
K-mer analysis (k=4) shows Jaccard similarity between KIAA1614 and Par6 proteins of 0.007-0.008, essentially random. For comparison, Par6-Par6 family members show Jaccard similarity of 0.087-0.172 (10-25x higher).

**Conclusion:** KIAA1614 shares no recognizable domain architecture or sequence similarity with Par6 proteins beyond the PANTHER family-level classification.

---

## 2. Binding Partners and Molecular Activity

### Experimentally detected interactions (IntAct)
Only two interactions are recorded, both from high-throughput studies:

1. **PTPRR** (Receptor-type tyrosine-protein phosphatase R): Detected by anti-tag co-IP in a large-scale KRAS-EGFR network study in CRC cells (PMID 31980649). PTPRR was overexpressed bait; KIAA1614 was prey at physiological level. IntAct MIscore = 0.35 (low). This is a high-throughput AP-MS detection, not a validated direct interaction.

2. **Histone H2B type 1-H (H2BC9):** Detected by crosslinking mass spectrometry in intact human nuclei (PMID 30021884). MIscore = 0.40. One of ~8,700 crosslinks identified in this global nuclear interactome study.

### STRING database interactions
STRING physical network shows KIAA1614 with weak experimental scores (0.35-0.38) connecting to mRNA 3' processing complex members (CPSF1, CPSF2, CPSF3, RBBP6). These have zero database support and low text-mining scores, suggesting they derive from co-detection in high-throughput AP-MS experiments (likely BioPlex or similar). For context, the CPSF complex members interact with each other at scores of 0.83-0.99.

### Critical negative result
**No interaction with any canonical polarity complex member has been detected in any database:**
- No interaction with Par3 (PARD3)
- No interaction with aPKC (PRKCI, PRKCZ)
- No interaction with Cdc42, Rac1, or any Rho-family GTPase
- No interaction with PALS1, Crumbs, PATJ, or any tight junction component
- No interaction with Lgl, Scribble, or Dlg

---

## 3. GO Annotations and Evidence Codes

All six GO annotations for KIAA1614 carry evidence code **IBA** (Inferred from Biological Aspect of Ancestor), assigned by GO_Central:

| GO Term | Description | Evidence |
|---------|-------------|----------|
| GO:0007098 | Centrosome cycle | IBA |
| GO:0007163 | Establishment or maintenance of cell polarity | IBA |
| GO:0060341 | Regulation of cellular localization | IBA |
| GO:0005634 | Nucleus | IBA |
| GO:0005938 | Cell cortex | IBA |
| GO:0016324 | Apical plasma membrane | IBA |

**These annotations are entirely derived from the PANTHER family classification grouping KIAA1614 with Par6.** They are NOT experimentally supported. No experimental evidence (EXP, IDA, IPI, IMP, IGI, IEP) exists for any cellular localization, molecular function, or biological process for KIAA1614.

---

## 4. AlphaFold Structural Prediction

The AlphaFold prediction (AF-Q5VZ46-F1, model v6) reveals KIAA1614 to be almost entirely intrinsically disordered:

- **Mean pLDDT:** 20.9 (extremely low confidence)
- **Median pLDDT:** 15.5
- **87.1%** of residues have pLDDT ≤ 50 (very low confidence / disordered)
- **0.0%** of residues have pLDDT > 90 (no high-confidence structured regions)
- **DUF4685 region** (354-478): Mean pLDDT = 21.9, max = 63.6

This is structurally incompatible with Par6 proteins, which have well-folded PB1, CRIB, and PDZ domains with high pLDDT scores in AlphaFold predictions. The extreme disorder of KIAA1614 suggests it may function through short linear motifs (SLiMs) rather than structured domain-domain interactions, but there is no evidence for what those motifs might bind.

---

## 5. DUF4685 Domain

The DUF4685 domain (Pfam PF15737, InterPro IPR032756):
- Found exclusively in vertebrates (1,312 taxa represented)
- Typically 106-131 amino acids
- Two conserved sequence motifs: SGE and VRF (both confirmed present in KIAA1614 at positions 432 and 450)
- **No known function, no solved structures, no known interactions**
- 832 proteins in database, 10 domain architectures
- Zero pathways associated
- The domain itself falls within a predicted disordered region in KIAA1614 (74.4% of DUF4685 residues overlap with annotated disorder)

DUF4685 shows no sequence or structural similarity to any Par6-related domain (PB1, PDZ, CRIB). It is not part of any characterized binding surface or enzymatic active site.

---

## 6. Published Literature

Comprehensive PubMed search yields 8 publications mentioning KIAA1614, **none** of which characterize protein function:

| PMID | Year | Study Type | KIAA1614 Context |
|------|------|-----------|------------------|
| 38996988 | 2024 | Multi-omics MR | sCJD drug target candidate |
| 38812741 | 2024 | Multi-omics | Glioma biomarker candidate |
| 36175575 | 2022 | Transcriptomics | DEG in T1DM complications |
| 34215268 | 2021 | Methylation array | Hypermethylated in ectopic pregnancy |
| 30545422 | 2018 | Methylation | Metformin-responsive CpG |
| 29293112 | 2018 | GWAS/ImmunoChip | Suggestive SNP in Crohn's |
| 27517910 | 2016 | Methylation | Hypermethylated & silenced in UC |
| 26883866 | 2016 | pQTL | Locus near adhesion protein QTL |

The epigenomic studies suggest KIAA1614 expression is regulated by DNA methylation (particularly in inflammatory conditions), but this does not inform protein molecular function.

---

## 7. Hypothesis Assessment

### Hypothesis: "KIAA1614 is functionally equivalent to canonical Par6 polarity scaffolds"

**REJECTED.** Multiple independent lines of evidence converge against this hypothesis:

| Evidence Type | Finding | Implication |
|--------------|---------|-------------|
| Domain architecture | Lacks PB1, PDZ, pseudo-CRIB | Cannot perform canonical Par6 functions |
| Sequence similarity | Jaccard ~0.007 (random) | Not a true homolog |
| Structural prediction | IDP (pLDDT 20.9) | Incompatible with folded Par6 domains |
| Interaction data | No polarity complex partners | No functional connection to polarity |
| GO evidence | All IBA (inferred), 0 experimental | Circular: annotations derive from the very classification being tested |
| Literature | 0 molecular function studies | No experimental basis for any function |

### Alternative hypothesis: "KIAA1614 is a novel vertebrate-specific IDP with unknown function"

**SUPPORTED.** The evidence is consistent with KIAA1614 being:
- A large, intrinsically disordered protein
- Vertebrate-specific (DUF4685 is vertebrate-restricted)
- Epigenetically regulated (methylation-responsive promoter)
- Possibly present in the nucleus (crosslinking MS to H2B, PMID 30021884)
- Possibly weakly associated with mRNA processing (STRING, low confidence)

---

## 8. What CAN Be Curated as Molecular Function Now?

**Nothing.** There is insufficient evidence to assign any molecular function to KIAA1614. Specifically:

- **No molecular function (MF)** can be curated — no enzymatic activity, binding partner, or catalytic mechanism is known
- **No biological process (BP)** can be curated experimentally — all current annotations are IBA (inferred)
- **No cellular component (CC)** can be curated experimentally — subcellular localization has not been determined by direct experiment

The PANTHER family classification should be flagged as potentially misleading, as it creates a false impression of Par6-like function through propagated IBA annotations.

---

## 9. Decisive Missing Experiments

To resolve KIAA1614 function, the following experiments are needed (prioritized):

### High priority
1. **Subcellular localization by immunofluorescence or GFP-tagging** — Determine if KIAA1614 localizes to cell junctions, cortex, centrosomes, or nucleus in epithelial cells
2. **AP-MS with KIAA1614 as bait** — Identify direct binding partners using KIAA1614 as bait (not prey) in a targeted experiment
3. **BioID/TurboID proximity labeling** — Map the proximal interactome in relevant cell types

### Medium priority
4. **Co-IP with Par6, Par3, aPKC, Cdc42** — Directly test the Par6 equivalence hypothesis with pull-downs
5. **CRISPR knockout in epithelial cells** — Test for effects on tight junction formation, polarity, or cell morphology
6. **DUF4685 domain deletion/mutation** — Test whether DUF4685 is required for any detectable phenotype

### Lower priority
7. **Cross-linking mass spectrometry of purified DUF4685** — Determine if DUF4685 adopts any folded structure in isolation
8. **Expression profiling across developmental stages** — Determine when/where KIAA1614 is expressed
9. **AlphaFold Multimer modeling** — Test if KIAA1614 is predicted to interact with polarity complex members

---

## 10. Limitations

- BioPlex database API was inaccessible; some interaction data may exist there that I could not access
- neXtProt API has migrated and could not be queried; additional protein-level evidence may be available
- GTEx expression data returned no results for the specific gene identifier used; tissue expression remains uncertain
- Human Protein Atlas data could not be retrieved due to API format issues
- The PANTHER family classification algorithm is opaque; the exact basis for grouping KIAA1614 with Par6 cannot be fully evaluated without the underlying HMM profile alignment

---

## Conclusion

KIAA1614 is a large (1190 aa), intrinsically disordered, vertebrate-specific protein with a single annotated domain of unknown function (DUF4685). Its classification in the PANTHER PAR6 homolog family (PTHR14102) is not supported by domain architecture, sequence similarity, structural prediction, interaction data, or any experimental evidence. All polarity-related GO annotations are computationally inferred from this questionable classification. No molecular function can be curated for KIAA1614 at this time, and the Par6 equivalence hypothesis should be considered refuted. Targeted experimental studies (localization, interactome, knockout) are needed before any function can be assigned.
