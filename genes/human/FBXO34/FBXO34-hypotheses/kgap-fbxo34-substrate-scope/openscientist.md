# FBXO34 Substrate Scope and SCF Adaptor Function: Evidence Review

## Summary

FBXO34 (F-box only protein 34; UniProt Q9NWN3) is a confirmed SCF (SKP1-CUL1-F-box) E3 ubiquitin ligase substrate-recognition adaptor with one well-validated degradative substrate: **HNRNPU/hnRNP U**. Among 38 unique interaction partners catalogued in IntAct, only HNRNPU has direct evidence of FBXO34-dependent ubiquitination leading to proteasomal degradation with functional consequences (HIV-1 latency reactivation). The remaining ~35 interactors derive exclusively from high-throughput screens (Y2H, AP-MS, XL-MS, LUMIER) and lack any mechanistic validation as substrates. Current GO-style curation correctly assigns FBXO34 broad "ubiquitin-like protein ligase substrate adaptor activity" but should also support a specific HNRNPU substrate annotation. High-throughput interactors should remain classified as non-core interaction leads until independent substrate-level evidence is obtained.

---

## 1. Evidence for SCF-FBXO34 Complex Formation

### F-box Domain
FBXO34 contains a canonical F-box domain at residues 572-624 (UniProt annotation), which mediates binding to SKP1, the adaptor protein linking F-box proteins to the CUL1 scaffold.

### SKP1 Interaction
- **Method:** Yeast two-hybrid (Y2H) pooling approach
- **Source:** Stelzl et al. 2005 (PMID: 16169070) — a large-scale human interactome screen of 4,456 baits × 5,632 preys
- **Evidence level:** High-throughput detection; consistent with canonical F-box–SKP1 binding but not independently validated by targeted biochemistry

### CUL1 Interaction
- **Method:** Anti-tag co-immunoprecipitation (AP-MS)
- **Source:** BioPlex 2.0, Huttlin et al. 2017 (PMID: 28514442)
- **Evidence level:** Co-purification in a systematic AP-MS campaign; supports SCF complex assembly

### UniProt Curation
UniProt annotates the SUBUNIT field as "Directly interacts with SKP1 and CUL1" based on ECO:0000250 (sequence similarity evidence). The GO annotation GO:0031146 ("SCF-dependent proteasomal ubiquitin-dependent protein catabolic process") is assigned by NAS (Non-traceable Author Statement) via ComplexPortal, referencing Thompson et al. 2021 (PMID: 34445249), a review of SCF complex roles.

### Assessment
The combination of a canonical F-box domain, Y2H-detected SKP1 binding, and AP-MS-detected CUL1 co-purification provides strong but indirect support for a functional SCF-FBXO34 complex. **No crystal structure, targeted co-IP, or in vitro reconstitution of the trimeric SCF-FBXO34 complex has been published.** The current evidence is sufficient for annotation of SCF complex membership but would benefit from targeted validation.

---

## 2. HNRNPU as the Best-Supported Degradative Substrate

### Key Study: Yang et al. 2022 (PMID: 36285453)
*"FBXO34 promotes latent HIV-1 activation by post-transcriptional modulation"* — Emerging Microbes & Infections 11(1):2785-2799.

### Evidence Lines

| Evidence Type | Result |
|---|---|
| **Substrate identification** | HNRNPU identified by affinity purification mass spectrometry (AP-MS) as FBXO34-associated protein |
| **Ubiquitination** | FBXO34 overexpression promotes HNRNPU ubiquitination |
| **Degradation** | FBXO34-dependent ubiquitination leads to HNRNPU proteasomal degradation |
| **Functional consequence** | HNRNPU degradation abolishes HNRNPU–HIV-1 Rev mRNA interaction |
| **Phenocopy** | HNRNPU knockout phenocopies FBXO34 overexpression (both activate latent HIV-1) |
| **Multiple cell line validation** | Tested in multiple latent HIV-1 cell lines |
| **Primary cell validation** | Confirmed in primary CD4+ T lymphocyte model |
| **Clinical relevance** | Differential HNRNPU expression in ART-treated patients vs. healthy controls |
| **Domain mapping** | HNRNPU amino acids 1-339 interact with HIV-1 Rev mRNA region |

### Substrate Evidence Grade: **Strong (Tier 1)**
HNRNPU meets all standard criteria for a bona fide E3 ligase substrate:
- Direct physical interaction (AP-MS)
- Direct ubiquitination (ubiquitination assay)
- Consequent degradation
- Functional phenocopy (knockout = overexpression of E3)
- Biological pathway validation

### Important Mechanistic Context: HNRNPU's Dual Regulation by SCF Complexes

A remarkable finding from the literature is that HNRNPU has a **contrasting relationship with a different F-box protein, β-TrCP (FBXW1)**:

- **SCF-FBXO34** → HNRNPU is a **true degradative substrate** (ubiquitinated and degraded; PMID: 36285453)
- **SCF-β-TrCP** → HNRNPU is a **stable pseudosubstrate** (binds β-TrCP substrate pocket but is NOT degraded; PMID: 11850407, Davis et al. 2002)

In the β-TrCP context, HNRNPU occupies the substrate-binding WD domain of β-TrCP in a stoichiometric manner, stabilizes the E3, and determines its nuclear localization. This binding is competed by phospho-IκBα (a true substrate). The pseudosubstrate relationship serves as a regulatory mechanism controlling β-TrCP localization, stability, and substrate-binding threshold.

This dual regulation demonstrates that **F-box protein identity, not merely substrate binding, determines whether HNRNPU is degraded or stabilized**, providing a clear example of substrate fate determination by E3 ligase specificity.

Citation-gating note: the initial OpenScientist draft cited PMID: 42348677 for an HNRNPU NEDDylation/RNA-binding-repertoire claim. PubMed verification on 2026-07-06 shows that PMID resolves to a 2026 Science article titled "Ubiquitin-like proteins NEDD8 and SUMO2 control epithelial homeostasis, regeneration, and inflammation," not the stated "Winge et al. 2026, Cell" citation. Treat the HNRNPU NEDDylation claim as an unverified/miscited lead unless full text or another verified source confirms direct HNRNPU evidence. It should not be propagated into `FBXO34-ai-review.yaml` as fact from this report.

---

## 3. Other Reported FBXO34 Interactors: Detailed Assessment

### 3A. CCNB1/Cyclin B1 — Functional Target, Not Direct Substrate (PMID: 33842473)

**Study:** Zhao et al. 2021, "FBXO34 Regulates the G2/M Transition and Anaphase Entry in Meiotic Oocytes" (mouse oocyte system)

| Evidence | Present? |
|---|---|
| Physical interaction (co-IP/AP-MS) | **No** |
| Ubiquitination assay | **No** |
| Degradation assay | **No** |
| Half-life measurement | **No** |
| Functional rescue | **Yes** — CCNB1 overexpression rescues FBXO34-depletion phenotype |

**Assessment:** CCNB1 is a **functional pathway target** but not a validated direct substrate. The rescue experiment shows that FBXO34 depletion leads to low MPF activity (CDK1/Cyclin B1), and CCNB1 overexpression can compensate. However, this is consistent with FBXO34 targeting an upstream inhibitor of MPF (e.g., a CDK inhibitor or Cyclin B1 degradation regulator) rather than CCNB1 directly. This work was performed in mouse oocytes; human relevance is inferred by sequence similarity.

**Substrate evidence grade: Insufficient.** Should not be annotated as a substrate without ubiquitination or degradation evidence.

### 3B. High-Throughput Binary Interactors (Y2H-Only)

**Source 1: HuRI (PMID: 32296183)**
Luck et al. 2020, "A reference map of the human binary protein interactome" — Nature 580:402-408.

17 partners detected, including:
- **10 KRTAPs** (KRTAP4-5, 4-11, 4-12, 5-3, 9-2, 9-3, 9-8, 10-5, 10-8, 10-11, 12-4)
- ALPP, COL8A1, DISC1, FGF14, OIT3, VWC2L

Methods: Y2H array, two-hybrid prey pooling, validated two-hybrid (3 independent Y2H methods per pair in most cases)

**Source 2: Rolland et al. (PMID: 25416956)**
Rolland et al. 2014, "A proteome-scale map of the human interactome network" — Cell 159:1212-1226.

3 partners: MTUS2, KRT40, MDFI

**Assessment:** These are legitimate binary protein-protein interactions detected in well-controlled Y2H screens. However:
- **No ubiquitination, degradation, half-life, or functional evidence** for any of these partners
- The **KRTAP enrichment** (10/17 HuRI partners) is suspicious — KRTAPs are small, cysteine-rich proteins known to be promiscuous Y2H interactors. Their biological relevance to FBXO34 (a ubiquitin ligase adaptor) is unclear
- DISC1, FGF14, ALPP, COL8A1, OIT3 are biologically diverse proteins with no obvious connection to FBXO34's known ubiquitin ligase function

**Substrate evidence grade: None.** These should remain as non-core interaction leads in annotation databases.

### 3C. High-Throughput Co-complex Interactors (AP-MS)

**Source: BioPlex 2.0/3.0 (PMID: 28514442, 33961781)**
- Huttlin et al. 2017 and 2021

Partners: FBXO30, MYO6, YEATS4, NEXN, GSN, TMOD3, GAP43, ABRA, ERLEC1

**Assessment:** AP-MS co-purification indicates co-complex membership or proximity but does not distinguish direct binding from indirect association. CUL1 co-purification from the same studies is meaningful because it matches the expected SCF scaffold interaction. The other partners (cytoskeletal proteins MYO6/NEXN/GSN/TMOD3/GAP43/ABRA; ER lectin ERLEC1; chromatin factor YEATS4; another F-box protein FBXO30) lack any substrate-level evidence.

**Substrate evidence grade: None.**

### 3D. Other Detection Methods

| Partner | Method | Source | Assessment |
|---|---|---|---|
| HSP90AB1 | LUMIER | PMID: 22939624 | Chaperone; likely recognizes FBXO34 as client protein |
| COA7, ITGB1, NCBP1 | Cross-linking MS (XL-MS) | PMID: 30021884 | Nuclear proximity; could be indirect |
| DISC1 | Y2H fragment pooling | PMID: 31413325 | Alzheimer's-associated dataset; no functional validation |

**Substrate evidence grade: None.**

---

## 4. Summary Classification Table

| Interactor | Evidence Types | Substrate Grade | Recommended Annotation |
|---|---|---|---|
| **HNRNPU** | AP-MS + ubiquitination + degradation + phenocopy + primary cells | **Bona fide substrate** | Substrate of SCF-FBXO34 |
| SKP1 | Y2H | SCF component | Core SCF complex partner |
| CUL1 | AP-MS | SCF component | Core SCF complex partner |
| CCNB1 | Functional rescue (mouse) | Indirect/pathway target | Functional pathway link, not substrate |
| KRTAPs (×10) | Y2H only | No evidence | HTP interactor; likely promiscuous |
| ALPP, COL8A1, DISC1, FGF14, etc. | Y2H only | No evidence | HTP interactor |
| FBXO30, MYO6, YEATS4, etc. | AP-MS only | No evidence | HTP co-complex |
| HSP90AB1 | LUMIER only | No evidence | Chaperone-client |
| COA7, ITGB1, NCBP1 | XL-MS only | No evidence | Nuclear proximity |

---

## 5. Curation Recommendations

### Current GO Annotations (Adequate)
- **GO:0031146** — SCF-dependent proteasomal ubiquitin-dependent protein catabolic process (NAS): Correctly reflects FBXO34's role as an SCF adaptor

### Recommended Additional Annotations
1. **Substrate-specific annotation:** HNRNPU should be annotated as a specific substrate of FBXO34 in GO/UniProt with experimental evidence (ECO:0000269) from PMID: 36285453. This supports a pathway-specific annotation beyond the broad "ubiquitin-like ligase substrate adaptor activity."

2. **HIV-1 latency regulation:** FBXO34's role in HIV-1 latency through HNRNPU degradation should be captured as a microbial infection-specific function (already present in UniProt FUNCTION field).

3. **HTP interactors should NOT be converted** to substrate annotations without additional evidence. The threshold for substrate annotation should require, at minimum:
   - Direct ubiquitination evidence (in vivo or in vitro ubiquitination assay)
   - Evidence of FBXO34-dependent degradation or protein level change
   - Ideally: functional rescue or reconstitution

4. **Oocyte maturation function:** The CCNB1 functional rescue (PMID: 33842473) supports a GO annotation for meiotic cell cycle regulation but should be qualified as "by similarity" (mouse data) and should NOT annotate CCNB1 as a substrate.

### What Would Strengthen the FBXO34 Literature
- In vitro reconstitution of SCF-FBXO34 ubiquitination of HNRNPU
- Identification of the HNRNPU degron recognized by FBXO34
- Crystal or cryo-EM structure of FBXO34 alone or in complex with SKP1
- Cycloheximide chase experiments quantifying HNRNPU half-life ± FBXO34
- Identification of additional substrates beyond HNRNPU with full validation
- Confirmation of CCNB1 as direct or indirect target with mechanistic detail

---

## 6. Limitations

1. **PMID: 36285453** (Yang et al. 2022) — The abstract was available but the full text was not systematically reviewed in this analysis. Specific experimental details (e.g., whether in vitro ubiquitination was performed, whether a degron motif was mapped) require full-text verification.

2. **PMID: 33842473** (Zhao et al. 2021) — Mouse oocyte study; species extrapolation to human is annotated "by similarity" (ECO:0000250) in UniProt. The direct substrate in oocyte meiosis remains unidentified.

3. **PMID: 42348677** was PubMed-verified as a real 2026 Science paper, but the report's original "HNRNPU NEDDylation regulation" wording is not verified by the PubMed title/metadata and may be miscited. Keep this as an unverified lead unless a curator checks the full text.

4. **PMID: 40497153** was PubMed-verified as a 2025 Journal of Virus Eradication HIV-1 latency review. Treat it as background only unless full text is checked for a specific FBXO34 claim.

5. **The HuRI/BioPlex interactors** were assessed at the annotation level. Individual follow-up studies on any of these partners (beyond the original HTP screens) were not found in PubMed, suggesting they remain uncharacterized.

6. **FBXO34 remains a relatively understudied F-box protein** with only 5 primary PubMed entries as of this analysis, compared to dozens for well-characterized F-box proteins like β-TrCP, FBXW7, or SKP2.

---

## 7. Key Citations

| PMID | Reference | Contribution |
|---|---|---|
| **36285453** | Yang et al. 2022, Emerg Microbes Infect | **Primary FBXO34/HNRNPU substrate evidence** |
| **33842473** | Zhao et al. 2021, Front Cell Dev Biol | FBXO34 in oocyte meiosis |
| **11850407** | Davis et al. 2002, Genes Dev | HNRNPU as pseudosubstrate of β-TrCP (contrast) |
| **42348677** | PubMed-verified 2026 Science article, "Ubiquitin-like proteins NEDD8 and SUMO2 control epithelial homeostasis, regeneration, and inflammation" | **Citation-gating warning:** original HNRNPU NEDDylation claim is unverified/may be miscited |
| **20797629** | Tsuchiya et al. 2010, Mol Cell | Nuclear IKKβ–β-TrCP–hnRNP-U axis |
| **16169070** | Stelzl et al. 2005, Cell | Y2H: FBXO34–SKP1 interaction |
| **28514442** | Huttlin et al. 2017, Nature | BioPlex 2.0: FBXO34–CUL1 and other AP-MS |
| **33961781** | Huttlin et al. 2021, Cell | BioPlex 3.0: additional AP-MS interactors |
| **32296183** | Luck et al. 2020, Nature | HuRI: Y2H binary interactors |
| **25416956** | Rolland et al. 2014, Cell | Y2H interactome: MTUS2, KRT40, MDFI |
| **40497153** | Yang et al. 2025, J Virus Erad | PubMed-verified HIV-1 latency review; background only unless full text confirms specific FBXO34 support |
| **34445249** | Thompson et al. 2021, IJMS | SCF complex review (GO annotation source) |
| **22939624** | Taipale et al. 2012, Cell | HSP90–FBXO34 LUMIER interaction |
| **30021884** | Fasci et al. 2018, MCP | XL-MS in nuclei |
| **31413325** | Sügis et al. 2019, Sci Data | HENA Alzheimer's dataset (DISC1) |

---

*Report generated: Iteration 1 of 1. Analysis based on PubMed literature search, UniProt (Q9NWN3), IntAct (89 interaction records, 38 unique partners), and BioGRID (58 interactions) as of July 2026.*
