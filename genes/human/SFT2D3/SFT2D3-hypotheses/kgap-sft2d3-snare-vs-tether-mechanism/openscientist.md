# SFT2D3: SNARE Binding Versus Tether/SNARE-Regulatory Mechanism

## Summary

**No direct SNARE binding has been demonstrated for human SFT2D3 -- or for any Sft2/Got1-family member in any organism.** Despite being annotated as involved in "fusion of retrograde transport vesicles derived from an endocytic compartment with the Golgi complex," the entire SFT2D3 functional annotation rests on sequence similarity to yeast Sft2p (evidence code ECO:0000250), with no direct experimental validation in human cells. The strongest molecular evidence linking SFT2D3 to SNARE machinery is a reciprocally validated co-immunoprecipitation with STX5 (human Sed5 ortholog) from the OpenCell high-throughput endogenous-tagging proteomics project ([PMID: 35271311](https://pubmed.ncbi.nlm.nih.gov/35271311/)). Additional co-IP partners include GOSR2, VAMP3, and members of the Golgi tethering/trafficking machinery (COG6, RAB1B, RAB2A), establishing that SFT2D3 resides in a SNARE-proximal protein environment but not proving it directly engages SNAREs.

The yeast literature shows that Sft2p and its paralog Got1p act at a post-tethering step in vesicle fusion, genetically suppress *sed5* (syntaxin) temperature-sensitive alleles, and influence ER-Golgi transport -- but the molecular mechanism has been variously proposed as SNARE facilitation, membrane property modulation, or an unspecified post-tethering role. In human cells, the paralog SFT2D2 -- not SFT2D3 -- has been experimentally validated as required for endosome-to-Golgi retrieval by a genome-wide RNAi screen ([PMID: 25464851](https://pubmed.ncbi.nlm.nih.gov/25464851/)). SFT2D3 was not identified as a hit in that screen, leaving its specific cellular role undefined.

The current evidence is therefore consistent with SFT2D3 functioning in the SNARE-proximal environment of Golgi membrane fusion, but the critical experiments to distinguish direct SNARE binding from SNARE-regulatory activity, tethering complex cooperation, membrane property modulation, or mere co-compartmentalization have never been performed. Resolving the molecular function of SFT2D3 requires in vitro reconstituted binding assays, crosslinking mass spectrometry, and SFT2D3-specific loss-of-function studies with SNARE redistribution readouts.

---

## Key Findings

### Finding 1: SFT2D3 Function Annotation Is Entirely Inferred From Yeast Orthology

All functional annotations for SFT2D3 (UniProt Q587I9) are derived from sequence similarity to yeast Sft2p (UniProt P38166) under evidence code ECO:0000250. The Gene Ontology annotations are uniformly IEA (Inferred from Electronic Annotation). No human study has directly tested SFT2D3 molecular function, subcellular localization by imaging, or knockout/knockdown phenotype. The UniProt function statement -- "May be involved in fusion of retrograde transport vesicles derived from an endocytic compartment with the Golgi complex" -- is a direct transfer from the yeast Sft2p literature, specifically from the seminal study by Conchon et al. (1999), which showed that "Sft2p is a non-essential tetra-spanning membrane protein, found mostly in the late Golgi, that can suppress some sed5 alleles" ([PMID: 10406798](https://pubmed.ncbi.nlm.nih.gov/10406798/)). This annotation transfer is reasonable given the conserved 4-TM topology and sequence identity, but it should not be confused with direct experimental evidence for SFT2D3 itself.

### Finding 2: SFT2D3 Co-Immunoprecipitates With STX5 Reciprocally in OpenCell

The strongest piece of molecular evidence for SFT2D3 comes from the OpenCell project at the CZ Biohub ([PMID: 35271311](https://pubmed.ncbi.nlm.nih.gov/35271311/)), which "combined genome engineering, confocal live-cell imaging, mass spectrometry, and data science to systematically map the localization and interactions of human proteins." In this dataset, SFT2D3 used as bait captures STX5 by anti-tag co-immunoprecipitation, and reciprocally, STX5 used as bait captures SFT2D3. The STRING combined score for SFT2D3-STX5 is 0.740 (experimental component = 0.553), the highest-scoring interaction for SFT2D3 in the database.

**Why this matters:** STX5 is the human ortholog of yeast Sed5p, the Golgi syntaxin whose temperature-sensitive alleles are suppressed by yeast Sft2p overexpression. The reciprocal co-IP therefore directly parallels the yeast genetic interaction at the protein level, making the SFT2D3-STX5 physical association the most evolutionarily consistent and proteomically robust link to SNARE machinery.

**Why it is insufficient:** Co-immunoprecipitation from detergent-solubilized membranes cannot distinguish between (a) direct protein-protein binding, (b) membership in a shared multi-protein complex (e.g., via a tethering factor), (c) co-compartmentalization in the same lipid microdomain, or (d) post-lysis artifactual association. No crosslinking, in vitro reconstitution, or domain-mapping experiments have been performed.

### Finding 3: SFT2D3 Co-IPs With Multiple Golgi SNAREs and Trafficking Machinery

Beyond STX5, the OpenCell and BioPlex datasets reveal a broader SFT2D3 interaction network:

| Interactor | Category | Source | STRING Score |
|:-----------|:---------|:-------|:-------------|
| **STX5** | Qa-SNARE (syntaxin) | OpenCell (reciprocal) | 0.740 |
| **GOSR2** (GS28) | Qb-SNARE | OpenCell | -- |
| **VAMP3** | R-SNARE (v-SNARE) | OpenCell | -- |
| **YKT6** | R-SNARE | STRING | 0.289 |
| **GOLT1B** | Got1 ortholog | STRING | 0.483 |
| **GOLT1A** | Got1 ortholog | STRING | 0.483 |
| **COG6** | COG tethering complex | STRING | 0.412 |
| **RAB1B** | Rab GTPase | OpenCell | -- |
| **RAB2A** | Rab GTPase | OpenCell | -- |
| **RABAC1** (PRA1) | Rab regulator | OpenCell | -- |
| **YIPF5** | Yip1-family | OpenCell | -- |
| **GORASP2** (GRASP55) | Golgi stacking | OpenCell | -- |
| **IFITM3** | Immune/membrane | BioPlex | -- |

This interaction profile is consistent with a protein embedded in the Golgi SNARE fusion environment, interacting with both Qa- and R-SNAREs, Rab GTPases that regulate vesicle targeting, and the COG tethering complex that facilitates retrograde intra-Golgi transport. Notably, the presence of COG6 (a component of the octameric COG complex) and GOLT1A/B (Got1 orthologs) suggests SFT2D3 may participate in a tethering-to-fusion handoff mechanism. However, all of these interactions derive from large-scale proteomics studies ([PMID: 35271311](https://pubmed.ncbi.nlm.nih.gov/35271311/); [PMID: 33961781](https://pubmed.ncbi.nlm.nih.gov/33961781/)) and have not been validated by targeted biochemistry.

{{figure:sft2d3_evidence_landscape.png|caption=SFT2D3 protein interaction landscape (left) and evidence hierarchy for molecular function (right). Red nodes are SNAREs, orange are Got1 orthologs, purple are tethering/Golgi matrix components, green are Rab GTPases. The evidence hierarchy shows that direct binding and targeted co-IP remain unperformed; all current data derive from high-throughput proteomics, yeast genetics, or sequence homology.}}

### Finding 4: Yeast Sft2/Got1 Act Post-Tethering but the Mechanism Is Unresolved

Three lines of yeast evidence define what Sft2p and Got1p do -- and, critically, what remains unknown:

1. **Post-tethering vesicle fusion defect:** Conchon et al. (1999) demonstrated that "got1 mutants, but not sft2 mutants, show a defect in an in vitro assay for ER-Golgi transport at a step after vesicle tethering to Golgi membranes" ([PMID: 10406798](https://pubmed.ncbi.nlm.nih.gov/10406798/)). The *got1 sft2* double mutant phenotype was ascribable to an endosome-Golgi traffic defect. This positions the family at the tethering-to-fusion transition, but the molecular mechanism -- whether through SNARE engagement, SNARE complex regulation, or membrane conditioning -- was not determined.

2. **Membrane property modulation hypothesis:** Losev et al. (2009) found that Got1p is efficiently packaged into COPII vesicles and cycles rapidly between ER and Golgi, and proposed "that Got1p has an unexpected role in vesicle formation from the ER by influencing membrane properties" ([PMID: 19383723](https://pubmed.ncbi.nlm.nih.gov/19383723/)). This alternative hypothesis suggests the Sft2/Got1 family may not directly engage SNAREs at all, but instead modulate the lipid environment to facilitate fusion.

3. **Genetic suppression of Sed5 extends to autophagy:** Ishihara et al. (2017) showed that "overexpression of SFT1 or SFT2 (suppressor of sed5 ts) rescued the autophagy defects in sed5-1 mutant cells" ([PMID: 28927260](https://pubmed.ncbi.nlm.nih.gov/28927260/)). This confirms the genetic interaction between Sft2p and Sed5p is robust and extends beyond canonical secretory trafficking, but again does not specify the molecular mechanism.

**Critically, no yeast study has demonstrated direct Sft2p-Sed5p protein binding by in vitro assays.** The comprehensive in vitro SNARE interaction studies by Tsui & Bhatt (1999; [PMID: 10591633](https://pubmed.ncbi.nlm.nih.gov/10591633/)) and Parlati et al. (2002; [PMID: 11959998](https://pubmed.ncbi.nlm.nih.gov/11959998/)) tested all SNARE-SNARE pairwise interactions but did not include Sft2p or Got1p, as these are not classified as SNAREs. The important distinction between Sft1p (a bona fide v-SNARE) and Sft2p (a tetra-spanning non-SNARE suppressor of sed5) is sometimes overlooked in the literature due to name similarity.

### Finding 5: SFT2D2 -- Not SFT2D3 -- Is Validated in Endosome-to-Golgi Retrieval

The closest functional data for a human SFT2D family member comes from SFT2D2, not SFT2D3. A genome-wide RNAi screen by Breusegem & Seaman (2014) identified ~90 genes required for endosome-to-Golgi retrieval of a CD8-CIMPR reporter, and the authors "further demonstrate a role for three multipass membrane proteins, SFT2D2, ZDHHC5, and GRINA, in endosome-to-Golgi retrieval" ([PMID: 25464851](https://pubmed.ncbi.nlm.nih.gov/25464851/)). **SFT2D3 was not reported as a hit in this screen**, suggesting either functional non-redundancy between the paralogs, expression-level differences in the cell line used, or that SFT2D3 operates in a distinct trafficking step.

SFT2D2 has additionally been implicated in diverse disease contexts including schizophrenia (autoantibodies against SFT2D2 in patients, with anti-SFT2D2 IgG causing neuroinflammation and psychosis-like behavior in mice; [PMID: 36619926](https://pubmed.ncbi.nlm.nih.gov/36619926/); [PMID: 39067681](https://pubmed.ncbi.nlm.nih.gov/39067681/); [PMID: 38262166](https://pubmed.ncbi.nlm.nih.gov/38262166/)), prostate cancer via a chimeric SFT2D2-TBX19 transcript ([PMID: 39540264](https://pubmed.ncbi.nlm.nih.gov/39540264/)), and multiple myeloma where SFT2D2 was validated as significantly upregulated and promoting tumor growth ([PMID: 40389878](https://pubmed.ncbi.nlm.nih.gov/40389878/)). These disease associations underscore the biological relevance of the SFT2D family but do not clarify the molecular function of SFT2D3 specifically.

---

## Mechanistic Model and Interpretation

### Where SFT2D3 Sits in the Trafficking Machinery

Based on the convergence of yeast genetics, human proteomics, and family-level analysis, SFT2D3 most likely operates at the **tethering-to-fusion transition** in Golgi and/or endosome-to-Golgi vesicle trafficking. The following schematic illustrates the proposed position:

```
  Vesicle                    Target Golgi membrane
  +--------+                 +-------------------------+
  |        |   Long-range    |                         |
  |  Cargo |   tethering     |   COG complex           |
  |        |<--------------->|   (COG6 interacts       |
  |        |   (Golgins,     |    with SFT2D3)         |
  |        |    COG)         |                         |
  +---+----+                 |   +--------------+      |
      |                      |   |   SFT2D3    |      |
      |   Close-range        |   |   (4-TM)    |      |
      |   tethering / SNARE  |   |             |      |
      |   priming            |   |  ?--> STX5  |      |
      |                      |   |  ?--> GOSR2 |      |
      |   v-SNARE            |   |  ?--> YKT6  |      |
      |   (VAMP3, YKT6)      |   +--------------+     |
      |         |             |         |              |
      +---------+-------------+---------+              |
                |   SNARE complex                      |
                |   assembly & fusion                  |
                v                                      |
          =====================                        |
             Membrane fusion                           |
                                                       |
  Key: ?--> = interaction observed by co-IP            |
       but mechanism unknown (direct binding,          |
       regulatory, or co-compartment)                  |
  +----------------------------------------------------+
```

### Three Competing Mechanistic Hypotheses

The available data cannot distinguish among three plausible models:

| Model | Prediction | Supporting Evidence | Against |
|:------|:-----------|:-------------------|:--------|
| **A. Direct SNARE binding** | SFT2D3 binds STX5 (and/or other SNAREs) through a specific interaction surface | Reciprocal co-IP with STX5; yeast Sft2p suppresses *sed5* alleles | No in vitro binding; Sft2/Got1 not structurally related to SNAREs; no SNARE-like domains |
| **B. SNARE-regulatory / tether handoff** | SFT2D3 facilitates SNARE complex assembly via tethering complex interaction (e.g., COG) | COG6 interaction; post-tethering fusion defect in yeast *got1*; recent Sly1 tethering-to-SNARE handoff mechanism ([PMID: 38478018](https://pubmed.ncbi.nlm.nih.gov/38478018/)) | No direct evidence SFT2D3 modulates tethering |
| **C. Membrane property modulation** | SFT2D3 alters lipid environment to facilitate fusion without directly contacting SNAREs | Got1p membrane property hypothesis ([PMID: 19383723](https://pubmed.ncbi.nlm.nih.gov/19383723/)); 4-TM topology typical of lipid-interacting proteins | No lipid binding data for any family member |

The recent discovery that the SM protein Sly1 mediates close-range vesicle tethering via an ALPS-like helix and hands off vesicles from long-range tethers (Golgins, COG) to initiate SNARE complex assembly ([PMID: 38478018](https://pubmed.ncbi.nlm.nih.gov/38478018/)) provides an important mechanistic framework. SFT2D3 could function analogously -- as an accessory factor in the tethering-to-SNARE transition -- without being a SNARE itself.

---

## Evidence Base

### Primary Literature Supporting SFT2D3 Investigation

| Reference | Key Contribution | Relevance to SFT2D3 |
|:----------|:-----------------|:--------------------|
| Conchon et al. (1999) [PMID: 10406798](https://pubmed.ncbi.nlm.nih.gov/10406798/) | Identified yeast Sft2p and Got1p; showed post-tethering fusion defect | Direct ortholog; source of all SFT2D3 annotations |
| Cho et al. (2022) [PMID: 35271311](https://pubmed.ncbi.nlm.nih.gov/35271311/) | OpenCell endogenous tagging proteomics | Source of reciprocal SFT2D3-STX5 co-IP |
| Huttlin et al. (2021) [PMID: 33961781](https://pubmed.ncbi.nlm.nih.gov/33961781/) | BioPlex 3.0 interactome | Additional SFT2D3 interaction data |
| Losev et al. (2009) [PMID: 19383723](https://pubmed.ncbi.nlm.nih.gov/19383723/) | Got1p membrane property hypothesis | Alternative mechanism for family |
| Ishihara et al. (2017) [PMID: 28927260](https://pubmed.ncbi.nlm.nih.gov/28927260/) | Sft2 suppresses sed5-1 in autophagy | Extended genetic interaction |
| Breusegem & Seaman (2014) [PMID: 25464851](https://pubmed.ncbi.nlm.nih.gov/25464851/) | SFT2D2 required for endosome-to-Golgi retrieval | Paralog evidence; SFT2D3 not a hit |
| Brune et al. (2024) [PMID: 38478018](https://pubmed.ncbi.nlm.nih.gov/38478018/) | Sly1 close-range tethering mechanism | Framework for tethering-to-SNARE handoff |

### SNARE Biology Context

| Reference | Relevance |
|:----------|:----------|
| Banfield et al. (1995) [PMID: 7596416](https://pubmed.ncbi.nlm.nih.gov/7596416/) | Identified Sft1p as SNARE-like protein in intra-Golgi traffic; distinct from Sft2p |
| Tsui & Bhatt (1999) [PMID: 10591633](https://pubmed.ncbi.nlm.nih.gov/10591633/) | Showed yeast Golgi SNARE interactions are promiscuous; did not test Sft2p |
| Parlati et al. (2002) [PMID: 11959998](https://pubmed.ncbi.nlm.nih.gov/11959998/) | Defined Sed5-based SNARE complexes; Sft1p (not Sft2p) is a v-SNARE |
| Laufman et al. (2019) [PMID: 31357511](https://pubmed.ncbi.nlm.nih.gov/31357511/) | Stx5-mediated ER-Golgi transport in mammals |
| Smits et al. (2021) [PMID: 34779586](https://pubmed.ncbi.nlm.nih.gov/34779586/) | BET1 SNARE complex (GOSR2, SEC22b, STX5) in disease |

### SFT2D2 Disease Associations (Paralog Context)

| Reference | Finding |
|:----------|:--------|
| Xu et al. (2023) [PMID: 36619926](https://pubmed.ncbi.nlm.nih.gov/36619926/) | SFT2D2 rare variant associated with schizophrenia; anti-SFT2D2 autoantibodies in patients |
| Bao et al. (2024) [PMID: 39067681](https://pubmed.ncbi.nlm.nih.gov/39067681/) | Anti-SFT2D2 IgG induces encephalitis and schizophrenia-like behavior in mice |
| Chen et al. (2024) [PMID: 38262166](https://pubmed.ncbi.nlm.nih.gov/38262166/) | Anti-SFT2D2 autoantibodies alter dendritic spines and cause psychotic behavior |
| Deng et al. (2024) [PMID: 39540264](https://pubmed.ncbi.nlm.nih.gov/39540264/) | Chimeric SFT2D2-TBX19 in prostate cancer |
| Li et al. (2025) [PMID: 40389878](https://pubmed.ncbi.nlm.nih.gov/40389878/) | SFT2D2 upregulated and promoting proliferation in multiple myeloma |

---

## Distinguishing Evidence Types: A Critical Assessment

A central theme of this investigation is the need to rigorously separate different categories of evidence. The table below classifies all available SFT2D3 evidence by type, status, and what it can and cannot demonstrate:

| Evidence Type | Status for SFT2D3 | Details |
|:-------------|:-------------------|:--------|
| **Direct binding (in vitro reconstitution)** | **NOT PERFORMED** | No purified-protein binding assay exists |
| **Targeted co-IP (endogenous antibodies)** | **NOT PERFORMED** | No SFT2D3-specific antibody co-IP published |
| **Reciprocal co-IP (high-throughput)** | **AVAILABLE** | STX5 <-> SFT2D3 reciprocal, OpenCell ([PMID: 35271311](https://pubmed.ncbi.nlm.nih.gov/35271311/)) |
| **High-throughput co-IP (single direction)** | **AVAILABLE** | STX5, GOSR2, VAMP3, RAB1B, etc. (OpenCell, BioPlex) |
| **Yeast genetic suppression** | **AVAILABLE** | Sft2p suppresses *sed5* alleles ([PMID: 10406798](https://pubmed.ncbi.nlm.nih.gov/10406798/); [PMID: 28927260](https://pubmed.ncbi.nlm.nih.gov/28927260/)) |
| **Trafficking phenotype (human)** | **AVAILABLE for SFT2D2 only** | SFT2D2 in endosome-to-Golgi retrieval ([PMID: 25464851](https://pubmed.ncbi.nlm.nih.gov/25464851/)); SFT2D3 not tested |
| **Sequence homology** | **AVAILABLE** | SFT2D3 and yeast Sft2p share conserved 4-TM topology |
| **GO/database annotation** | **INFERRED (ECO:0000250)** | All annotations transferred from yeast Sft2p |

This hierarchy demonstrates that SFT2D3 molecular function evidence reaches only to the level of high-throughput reciprocal co-IP. The gap between "co-immunoprecipitates with STX5" and "directly binds STX5" is substantial and cannot be bridged without dedicated biochemical experiments.

---

## Limitations and Knowledge Gaps

### Critical Gaps

1. **No direct binding assay exists.** The single most important missing experiment is an in vitro reconstituted binding assay between purified SFT2D3 and STX5 (or other Golgi SNAREs). Without this, the molecular function cannot be classified as "SNARE binding."

2. **No SFT2D3-specific loss-of-function study.** Neither knockout, knockdown, nor CRISPR interference experiments have been published for SFT2D3 in any human cell line. The SFT2D2 RNAi screen result ([PMID: 25464851](https://pubmed.ncbi.nlm.nih.gov/25464851/)) cannot be directly transferred to SFT2D3.

3. **No SFT2D3 subcellular localization by imaging.** While yeast Sft2p localizes to the late Golgi, human SFT2D3 subcellular localization has not been independently determined by targeted imaging studies.

4. **Yeast-to-human inference is uncertain.** The sequence identity between Sft2p and SFT2D3, while supporting orthology, is at the lower end for confident functional transfer. The human genome encodes three paralogs (SFT2D1, SFT2D2, SFT2D3), creating the possibility of subfunctionalization not present in yeast.

5. **Co-IP limitations.** All interaction data come from detergent-solubilized membrane protein co-IPs in high-throughput studies. Membrane protein complexes are notoriously prone to both false positives (detergent-mediated reassociation) and false negatives (loss of weak or lipid-dependent interactions).

### Methodological Considerations

- The OpenCell co-IP data use endogenous split-mNeonGreen tagging, which is a strength (endogenous expression levels), but the tag could theoretically alter protein folding or interactions for a small 4-TM protein.
- STRING scores aggregate multiple evidence types; the experimental component (0.553 for STX5) is moderate but not definitive.
- The absence of SFT2D3 from the endosome-to-Golgi retrieval screen could reflect cell-type-specific expression, functional redundancy with SFT2D1/SFT2D2, or genuine non-involvement in that specific trafficking step.
- The name similarity between Sft1p (a bona fide SNARE) and Sft2p (a non-SNARE tetra-spanning protein) has occasionally led to confusion in the literature. They are structurally and functionally distinct proteins.

---

## Proposed Follow-up Experiments

### Priority 1: Direct Binding (High Impact, Moderate Feasibility)

1. **In vitro pull-down with purified proteins.** Express and purify the cytoplasmic loops of SFT2D3 (or full-length in nanodiscs/liposomes) and test binding to purified STX5 cytoplasmic domain, full Golgi SNARE complexes (STX5/GOSR2/BET1/SEC22B), and the COG complex. Include SFT2D2 and SFT2D1 as controls.

2. **Crosslinking mass spectrometry (XL-MS).** Perform in-cell or in-membrane XL-MS using NHS-ester or photoactivatable crosslinkers on cells expressing tagged SFT2D3, followed by enrichment and MS identification of crosslinked peptide pairs. This would reveal direct contacts at amino-acid resolution and definitively distinguish direct from indirect interactions.

3. **BioID/TurboID proximity labeling.** While co-IP data exist, proximity labeling with SFT2D3-TurboID would provide orthogonal evidence and capture transient interactions that survive detergent lysis poorly.

### Priority 2: Loss-of-Function (High Impact, High Feasibility)

4. **CRISPR knockout/CRISPRi of SFT2D3.** Generate SFT2D3-null or knockdown cells and assess:
   - Golgi morphology (electron microscopy, GM130/TGN46 staining)
   - SNARE distribution (STX5, GOSR2, BET1 localization by immunofluorescence)
   - Cargo trafficking (VSVG-GFP transport assay, CD-MPR recycling assay as in [PMID: 25464851](https://pubmed.ncbi.nlm.nih.gov/25464851/))
   - Include SFT2D2 single and SFT2D2/SFT2D3 double knockouts to test redundancy

5. **Functional rescue with yeast Sft2p.** Test whether yeast Sft2p can rescue SFT2D3 knockout phenotypes, establishing functional conservation and confirming orthology.

### Priority 3: Mechanistic Dissection (Medium Impact, Moderate Feasibility)

6. **SNARE complex assembly assay.** Test whether SFT2D3 modulates the kinetics or efficiency of SNARE complex assembly (STX5/GOSR2/BET1/SEC22B) using a fluorescence-based liposome fusion reconstitution assay. This would directly test whether SFT2D3 acts as a SNARE chaperone or facilitator.

7. **Lipid binding assay.** Given the Got1p membrane property hypothesis, test SFT2D3 binding to lipid strips (PIP strips) or liposomes of varying composition. This would address whether the family modulates membranes rather than directly engaging proteins.

8. **Structure determination.** AlphaFold2 structure prediction for SFT2D3, followed by molecular docking with STX5 structures, could suggest binding interfaces and guide targeted mutagenesis experiments.

### Summary of Missing Experiments

| Priority | Experiment | What It Would Resolve |
|:---------|:----------|:---------------------|
| **1** | In vitro reconstituted binding (recombinant SFT2D3 + STX5/GOSR2/VAMP3) | Direct vs. indirect SNARE interaction |
| **2** | Crosslinking mass spectrometry (XL-MS) of SFT2D3 complexes | Identify direct contact surfaces |
| **3** | SFT2D3 knockout + SNARE redistribution assay | Whether SFT2D3 affects SNARE localization/recycling |
| **4** | Reconstituted liposome fusion with/without SFT2D3 | Whether SFT2D3 enhances SNARE-mediated fusion |
| **5** | SFT2D3 domain mutagenesis + co-IP | Map interaction surfaces |
| **6** | Endogenous co-IP with anti-SNARE antibodies | Validate interaction at endogenous levels |
| **7** | SFT2D3 sub-Golgi localization (super-resolution) | Determine cis- vs. trans-Golgi vs. TGN compartment |
| **8** | SFT2D3 vs. SFT2D2 knockout comparison | Determine paralog-specific vs. redundant roles |

---

## Conclusions

1. **SFT2D3 is physically proximal to Golgi SNARE fusion machinery** (STX5, GOSR2, VAMP3, YKT6), supported by reciprocally validated co-IP data from OpenCell ([PMID: 35271311](https://pubmed.ncbi.nlm.nih.gov/35271311/)).

2. **No direct SNARE binding has been demonstrated** for SFT2D3 or any member of the Sft2/Got1 family, in any organism. Even in yeast, the genetic interaction between Sft2p and Sed5p does not constitute evidence of direct physical binding.

3. **The molecular function is unresolved.** Current data cannot distinguish between: (a) direct SNARE binding, (b) SNARE-regulatory activity through tethering or SM proteins, (c) membrane property modulation, or (d) cargo/receptor handling that indirectly affects trafficking.

4. **Human SFT2D2 is the better-characterized paralog**, with direct evidence for a role in endosome-to-Golgi retrieval ([PMID: 25464851](https://pubmed.ncbi.nlm.nih.gov/25464851/)), but even SFT2D2 lacks mechanistic resolution regarding SNARE interactions. SFT2D3 was not identified as a hit in the same screen.

5. **All database annotations for SFT2D3** (UniProt, GO, InterPro) are inferred from yeast Sft2p orthology (ECO:0000250 or IEA), not from direct experimental evidence.

6. **The key bottleneck** is the absence of in vitro binding assays, crosslinking proteomics, and genetic perturbation studies specifically targeting SFT2D3. These experiments are technically feasible and would decisively classify SFT2D3's molecular function.
