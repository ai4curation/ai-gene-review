# DNAJC16/ERdj8: J-Domain and Thioredoxin-Like Domain Function in Autophagosome Size Regulation

## Summary

**No molecular function annotation for DNAJC16/ERdj8 is currently supported by direct biochemical evidence.** Despite bearing a conserved J-domain (with intact HPD motif) and a thioredoxin-like domain — hallmarks of HSP70 co-chaperone and redox enzyme activity, respectively — neither co-chaperone nor oxidoreductase function has been experimentally demonstrated for this protein. The critical barrier to the widely assumed "ER HSP70 co-chaperone" role is membrane topology: DNAJC16 is a type IV transmembrane protein whose J-domain and thioredoxin-like domain face the cytoplasm, not the ER lumen where BiP/HSPA5 resides. This topological arrangement makes direct J-domain–BiP interaction physically impossible across the ER membrane, and the "ERdj8" nomenclature is consequently misleading.

The sole primary research study on ERdj8 function (Yamamoto et al. 2020, [PMID: 32492081](https://pubmed.ncbi.nlm.nih.gov/32492081/)) demonstrated that overexpression of ERdj8 enlarges autophagosomes and that both the J-domain and thioredoxin-like domain are required for this phenotype. ERdj8 knockout causes defective engulfment of larger cargo, and *C. elegans* ortholog knockdown impairs autophagy of large somatic mitochondria but not smaller paternal mitochondria. However, no domain-specific rescue experiments have been performed in endogenous/knockout systems, and no biochemical assays — HSP70 binding, ATPase stimulation, redox activity, or substrate trapping — have been reported. The thioredoxin-like domain contains an atypical CFSC motif rather than the canonical CXXC active-site sequences found in enzymatically active PDI family members like ERdj5. Together, the evidence supports a model in which ERdj8 acts at the PIS-enriched ER subdomain where autophagosomes form, but the precise molecular mechanism — whether through cytoplasmic HSP70 recruitment, structural scaffolding, or an entirely different effector pathway — remains experimentally untested.

---

## Key Findings

### Finding 1: The J-Domain and TRX Domain Are Cytoplasmic, Not Luminal — Precluding Direct BiP Interaction

The most consequential finding of this investigation is topological. UniProt annotation of DNAJC16 (Q9Y2G8) identifies it as a **type IV membrane protein** with a single transmembrane helix (residues 536–556). The entire N-terminal region (residues 26–535), encompassing both the J-domain (residues 29–93) and the thioredoxin-like domain (residues 119–247), is **cytoplasmic**. Only the short C-terminal tail (residues 557–782) faces the ER lumen, confirmed by N-glycosylation at N631.

This topology has a decisive implication: **BiP/HSPA5, the ER-luminal HSP70 chaperone, cannot be the J-domain's functional partner.** The J-domain's conserved HPD motif (position 57) — which in other DnaJ proteins docks into the HSP70 ATPase domain to stimulate ATP hydrolysis — is on the wrong side of the membrane. Reviews of ER chaperone systems describe eight DnaJ-type proteins that regulate BiP, but all of these have their J-domains in the ER lumen. As noted in a review of BiP co-chaperones, "BiP, the ER HSP70 chaperone, interacts with unfolded client proteins in a nucleotide-dependent manner, which is tightly regulated by eight DnaJ-type proteins and two nucleotide exchange factors (NEFs), SIL1 and GRP170" ([PMID: 33557244](https://pubmed.ncbi.nlm.nih.gov/33557244/)). Similarly, another review states: "The chaperoning activity of BiP is assisted by ER-resident DnaJ (ERdj) proteins due to their ability to stimulate the low, intrinsic ATPase activity of BiP" ([PMID: 35628387](https://pubmed.ncbi.nlm.nih.gov/35628387/)). In both cases, the ERdj proteins must be co-resident in the ER lumen to access BiP's ATPase domain. DNAJC16's cytoplasmic J-domain cannot fulfill this requirement.

Instead, the cytoplasmic orientation suggests potential interaction with **cytoplasmic HSP70 family members** such as HSPA1A (HSP70) or HSPA8 (HSC70). However, no co-immunoprecipitation, pull-down, or ATPase stimulation assay has tested this hypothesis.

{{figure:domain_comparison.png|caption=Domain architecture comparison of DNAJC16 (cytoplasmic J-domain and TRX domain) versus ERdj5/DNAJC10 (luminal J-domain and six TRX domains). The membrane topology is opposite: DNAJC16's functional domains face the cytoplasm, whereas ERdj5's face the ER lumen where BiP resides.}}

### Finding 2: The Thioredoxin-Like Domain Has an Atypical Active-Site Motif and No Demonstrated Redox Activity

Sequence analysis reveals that DNAJC16's thioredoxin-like domain (residues 119–247) contains a single **CFSC motif** at positions 171–174. This differs substantially from the canonical active-site sequences found in enzymatically active PDI/thioredoxin family members:

| Protein | Active-Site Motif | Demonstrated Reductase Activity | Cellular Location |
|---------|------------------|-------------------------------|-------------------|
| **DNAJC16** | **CFSC** | **None** | **Cytoplasmic face of ER** |
| ERdj5/DNAJC10 | CSHC, CPPC (×2) | Yes — disulfide reductase | ER lumen |
| Thioredoxin (TXN) | CGPC | Yes | Cytoplasm |
| PDI/PDIA1 | CGHC (×2) | Yes — oxidoreductase | ER lumen |

Two additional Pfam thioredoxin-like domains (PF26973, PF26968) map to the cytoplasmic region (~248–535) but contain only **isolated cysteines** (C375, C387, C524) with no CXXC pairs. This arrangement parallels the non-catalytic Trxb1/Trxb2 domains of ERdj5, which was described as "composed of an N-terminal J domain followed by six thioredoxin-like domains" and functions "as an ER-localized disulfide reductase that enhances ER-associated degradation (ERAD)" ([PMID: 28479060](https://pubmed.ncbi.nlm.nih.gov/28479060/)). However, ERdj5's reductase activity resides in its *catalytically active* TRX domains with canonical CXXC motifs, not in its inactive Trxb domains — and DNAJC16's domains more closely resemble the inactive ones.

Structural studies of non-catalytic thioredoxin domains in other proteins demonstrate they can serve as **protein–protein interaction scaffolds** rather than catalytic sites. For example, the non-catalytic domain of PDIR "adopts a thioredoxin-like fold stabilized by a structural disulfide bridge with a positively charged binding surface for interactions with the ER chaperones, calreticulin and ERp72" ([PMID: 23614004](https://pubmed.ncbi.nlm.nih.gov/23614004/)).

Critically, **no redox assay** (insulin reduction, di-eosin-GSSG cleavage, or any other standard assay), **no substrate-trapping experiment** (CXXA mutant pulldown), and **no cysteine-to-serine mutant redox characterization** has been published for DNAJC16. Moreover, the cytoplasmic localization places the domain in a **reducing environment**, where disulfide reductase activity would be less functionally relevant than in the oxidizing ER lumen where ERdj5 operates.

### Finding 3: Domain Requirements Demonstrated Only in Overexpression — No Endogenous Rescue Data

Yamamoto et al. (2020) reported two complementary experimental paradigms. As stated in their paper: "ERdj8 overexpression extended the size of the autophagosome through its DnaJ and TRX domains. ERdj8 ablation resulted in a defect in engulfing larger targets" ([PMID: 32492081](https://pubmed.ncbi.nlm.nih.gov/32492081/)).

These two paradigms address fundamentally different questions:

1. **Overexpression (gain-of-function):** ERdj8 overexpression extended autophagosome size, and this phenotype required both the J-domain and TRX domain. Domain deletion or mutation constructs abolished the enlargement effect. This tells us which domains are sufficient for a gain-of-function phenotype — but gain-of-function can operate through non-physiological mechanisms (e.g., titrating binding partners, forming aggregates, or causing ER stress).

2. **Loss-of-function:** ERdj8 knockout resulted in defective engulfment of larger cargo. In *C. elegans*, *dnj-8* knockdown permitted autophagy of smaller paternal mitochondria but not larger somatic mitochondria. This tells us ERdj8 is necessary for large-cargo autophagy, but **no domain-specific rescue experiments** (e.g., J-domain HPD→AAA mutant rescue, TRX CFSC→SFSS mutant rescue in the knockout background) have been performed.

Therefore, **which domain is required at endogenous expression levels is unknown.** This gap is significant because overexpression artifacts are common in ER membrane protein studies. A TRX domain that acts as a structural scaffold at endogenous levels might appear "required" in overexpression simply because the scaffold is needed to maintain proper protein folding or localization, not because it has catalytic redox activity.

### Finding 4: ERdj8 Localizes to the PIS-Enriched ER Subdomain Where Autophagosomes Form

ERdj8 partially colocalizes with a specialized **ER subdomain enriched in phosphatidylinositol synthase (PIS/CDIPT)** and other phospholipid-synthesizing enzymes. As characterized by Yamamoto and Noda (2021): "Autophagosome formation occurs near the ER subdomain enriched with phospholipid synthesizing enzymes like phosphatidylinositol synthase (PIS)/CDP-diacylglycerol-inositol 3-phosphatidyltransferase (CDIPT) and choline/ethanolamine phosphotransferase 1 (CEPT1)" ([PMID: 33087127](https://pubmed.ncbi.nlm.nih.gov/33087127/)). The same review noted that "the localization of ERdj8/DNAJC16 partially overlaps with the PIS-enriched ER subdomain, thereby implying its association with autophagosome size determination."

This subdomain overlaps with **ER exit sites (ERES)** where Atg2-mediated lipid transfer fuels autophagosome membrane expansion. Valverde et al. established that "Atg2 transfers phospholipids from the ERES to the IM during the process of autophagosome formation, suggesting that lipid transfer proteins can mediate de novo organelle biogenesis" ([PMID: 30993752](https://pubmed.ncbi.nlm.nih.gov/30993752/)).

This localization is the strongest clue to ERdj8's biological role: it positions the protein precisely at the membrane site where autophagosomes grow. The cytoplasmic orientation of its J-domain and TRX domain would allow them to interact with cytoplasmic components of the autophagy machinery (e.g., Atg proteins, ULK1 complex components) or with cytoplasmic chaperones that regulate protein complex assembly at this site.

### Finding 5: No Molecular Function GO Annotation — Neither Co-Chaperone Nor Oxidoreductase Activity Is Experimentally Supported

As of 2026, UniProt Q9Y2G8 carries only two GO annotations:

| GO Term | Description | Evidence Code | Source |
|---------|-------------|---------------|--------|
| GO:0005789 | Endoplasmic reticulum membrane | IDA | [PMID: 32492081](https://pubmed.ncbi.nlm.nih.gov/32492081/) |
| GO:0016243 | Regulation of autophagosome size | IMP | [PMID: 32492081](https://pubmed.ncbi.nlm.nih.gov/32492081/) |
| **Molecular Function** | **NONE** | — | — |

There is **no molecular function annotation**. Neither GO:0051087 (chaperone binding), GO:0030544 (Hsp70 protein binding), GO:0015036 (disulfide oxidoreductase activity), nor any other molecular function term is assigned. This accurately reflects the state of experimental evidence: all published functional data derives from a single study providing cellular phenotypes but no biochemical mechanism.

{{figure:evidence_summary.png|caption=Comprehensive evidence summary for DNAJC16/ERdj8. Left: membrane topology showing cytoplasmic J-domain and TRX domains separated from luminal BiP by the ER membrane. Right: assessment of proposed molecular functions — all lack direct biochemical support.}}

---

## Mechanistic Model and Interpretation

Based on the available evidence, we propose the following working model for ERdj8 function, while emphasizing that it remains **hypothetical** and experimentally untested:

```
                        CYTOPLASM
                        ─────────
    ┌─────────┐  ┌──────────────┐  ┌──────────────────┐
    │ J-domain│──│  TRX domain  │──│  TRX-like folds   │
    │ (29-93) │  │  (119-247)   │  │  (248-535)        │
    │ HPD motif│  │  CFSC motif  │  │  No CXXC pairs   │
    └────┬────┘  └──────┬───────┘  └────────┬──────────┘
         │              │                    │
         ▼              ▼                    ▼
    Cytoplasmic    Protein-protein     Structural
    HSP70?         interaction         scaffold?
    (HSC70?)       scaffold?
                        │
    ════════════════════╪══════════════════════════
           ER MEMBRANE  │  (TM: 536-556)
    ════════════════════╪══════════════════════════
                        │
                        ▼
                  ER LUMEN
              ┌────────────┐
              │ C-terminal │  ← N-glycosylated (N631)
              │ (557-782)  │  ← Luminal; function unknown
              └────────────┘

              BiP/HSPA5 is HERE
              (Cannot reach J-domain)
```

**Proposed mechanism (speculative):**

1. ERdj8 is anchored in the ER membrane at the PIS-enriched subdomain via its single transmembrane helix.
2. The cytoplasmic J-domain may recruit **HSC70 (HSPA8)** or **HSP70 (HSPA1A)** to the ER surface, potentially facilitating protein complex assembly or remodeling at autophagosome formation sites.
3. The thioredoxin-like domains likely serve as **structural scaffolds** for protein–protein interactions rather than as catalytic redox enzymes, given their atypical active-site motifs and cytoplasmic (reducing) environment.
4. Together, the domains may organize a chaperone-scaffolding platform that influences the lipid or protein environment at the ER membrane, thereby determining the capacity and size of nascent autophagosomes.

**Alternative hypotheses that cannot be excluded:**
- The TRX domain could have non-canonical redox activity (e.g., glutaredoxin-like or S-nitrosylation-related chemistry)
- The J-domain could interact with non-HSP70 partners via its HPD motif
- The luminal C-terminal domain could have an independent signaling or regulatory function
- DNAJC16 could function through protein–protein interactions mediated by the large cytoplasmic region (~500 amino acids) that are independent of the J-domain's canonical HPD-HSP70 mechanism

---

## Supported and Refuted Hypotheses

| Hypothesis | Status | Key Evidence |
|---|---|---|
| ERdj8 J-domain stimulates BiP ATPase (luminal co-chaperone) | **Refuted by topology** | J-domain is cytoplasmic; BiP is luminal; separated by ER membrane |
| ERdj8 J-domain interacts with cytoplasmic HSP70 (HSC70/HSPA8) | **Plausible but untested** | HPD motif conserved; correct cytoplasmic orientation; no binding data exist |
| ERdj8 TRX domain has thioredoxin reductase/oxidoreductase activity | **Unlikely but untested** | Atypical CFSC motif; cytoplasmic reducing environment; no redox assay performed |
| ERdj8 TRX-like domains serve as protein-interaction scaffolds | **Plausible but untested** | 2 of 3 TRX folds lack CXXC motifs; precedent from PDIR ([PMID: 23614004](https://pubmed.ncbi.nlm.nih.gov/23614004/)) and ERdj5 inactive Trxb domains |
| Both domains independently essential at endogenous levels | **Unknown** | Only overexpression data available; no rescue experiments performed |
| ERdj8 regulates autophagosome size at ER subdomains | **Supported** | Overexpression, knockout, and *C. elegans* data ([PMID: 32492081](https://pubmed.ncbi.nlm.nih.gov/32492081/)) |

---

## Evidence Base

### Primary Research on ERdj8 Function

The entire functional characterization of DNAJC16/ERdj8 rests on a single primary paper:

- **Yamamoto et al. (2020)** — *ERdj8 governs the size of autophagosomes during the formation process.* [PMID: 32492081](https://pubmed.ncbi.nlm.nih.gov/32492081/). This study "characterized a novel ER membrane protein, ERdj8, in mammalian cells. ERdj8 localizes to a meshwork-like ER subdomain along with phosphatidylinositol synthase (PIS) and autophagy-related (Atg) proteins." It demonstrated that overexpression extends autophagosome size through both J and TRX domains, and that ablation impairs engulfment of larger targets. A correction notice was published ([PMID: 32968790](https://pubmed.ncbi.nlm.nih.gov/32968790/)) but did not alter the main conclusions.

- **Yamamoto & Noda (2021)** — *Autophagosome formation in relation to the endoplasmic reticulum.* [PMID: 33087127](https://pubmed.ncbi.nlm.nih.gov/33087127/)). Review placing ERdj8 in the context of the PIS-enriched ER subdomain involved in autophagosome biogenesis.

### Comparative Literature — ER J-Domain Proteins and BiP

| Study | Key Contribution | Relevance to DNAJC16 |
|-------|-----------------|---------------------|
| Behnke et al. 2015 ([PMID: 25698114](https://pubmed.ncbi.nlm.nih.gov/25698114/)) | Comprehensive review of BiP's ATPase cycle, regulation by DnaJ co-factors and NEFs | Establishes that BiP co-chaperones must be ER-luminal — topology excludes DNAJC16 |
| Ichhaporia & Bhatt 2021 ([PMID: 33557244](https://pubmed.ncbi.nlm.nih.gov/33557244/)) | Eight ER DnaJ proteins regulate BiP | DNAJC16 not among them due to cytoplasmic J-domain |
| Schwarz & Bhatt 2022 ([PMID: 35628387](https://pubmed.ncbi.nlm.nih.gov/35628387/)) | ERdj proteins stimulate BiP's intrinsic ATPase activity | Confirms luminal access is required for BiP stimulation |
| Clerico et al. 2015 ([PMID: 26097841](https://pubmed.ncbi.nlm.nih.gov/26097841/)) | HSP70/HSP110 family mechanisms | Cytoplasmic HSP70s (HSPA1A, HSPA8) are potential DNAJC16 partners |
| Ladiges et al. 2005 ([PMID: 16734427](https://pubmed.ncbi.nlm.nih.gov/16734427/)) | J-domain helix III contacts Hsc70 ATPase domain | Detailed mapping of J-domain/HSP70 interface — relevant to predicting DNAJC16 interactions |

### Comparative Literature — Thioredoxin Domains and ERdj5

| Study | Key Contribution | Relevance to DNAJC16 |
|-------|-----------------|---------------------|
| Hagiwara et al. 2011 ([PMID: 21329881](https://pubmed.ncbi.nlm.nih.gov/21329881/)) | Crystal structure of ERdj5; C-terminal TRX cluster reduces ERAD substrates | Defines what a functional TRX-domain J-protein looks like; DNAJC16 lacks these features |
| Maegawa et al. 2017 ([PMID: 28479060](https://pubmed.ncbi.nlm.nih.gov/28479060/)) | ERdj5 dynamics in ERAD | Multiple active CXXC motifs and demonstrated reductase activity — contrast with DNAJC16's single atypical motif |
| Kozlov et al. 2013 ([PMID: 23614004](https://pubmed.ncbi.nlm.nih.gov/23614004/)) | Non-catalytic TRX domain of PDIR functions in protein binding | Precedent for scaffolding role of TRX folds without catalytic activity |
| Selles et al. 2022 ([PMID: 36567215](https://pubmed.ncbi.nlm.nih.gov/36567215/)) | Redox proteomics of PDIs; non-catalytic thiol-disulfide motifs | Supports existence of non-catalytic cysteine motifs in TRX-domain proteins |
| Ushioda et al. 2009 ([PMID: 19788412](https://pubmed.ncbi.nlm.nih.gov/19788412/)) | ERdj5/JPDI role in ER quality control; TRX motifs required for stress mitigation | Demonstrates importance of TRX motifs in ERdj5 but in luminal, oxidizing context |

### Autophagosome Biogenesis at ER Subdomains

| Study | Key Contribution |
|-------|-----------------|
| Valverde et al. 2019 ([PMID: 30993752](https://pubmed.ncbi.nlm.nih.gov/30993752/)) | Atg2-mediated lipid transfer from ERES fuels autophagosome membrane expansion |
| Yamamoto & Noda 2021 ([PMID: 33087127](https://pubmed.ncbi.nlm.nih.gov/33087127/)) | PIS-enriched ER subdomain as site of autophagosome formation; ERdj8 partial colocalization |
| Gómez-Sánchez et al. 2022 ([PMID: 36354155](https://pubmed.ncbi.nlm.nih.gov/36354155/)) | Atg2-Atg9 interactions mediate ER-phagophore membrane contact sites |

### Disease Associations (Contextual)

DNAJC16 has been identified in several disease-related genetic and epigenetic studies, though none illuminate its molecular function:

- **Parkinson's disease:** Rare variants in DNAJC16 were enriched in PD patients in a burden analysis of the DNAJC family ([PMID: 41951985](https://pubmed.ncbi.nlm.nih.gov/41951985/)), representing the "first evidence that rare variants in DNAJC1, DNAJC11 and DNAJC16 were enriched in PD patients."
- **Tea consumption & DNA methylation:** CpG sites mapping to DNAJC16 were differentially methylated in relation to tea consumption in women ([PMID: 28535255](https://pubmed.ncbi.nlm.nih.gov/28535255/)).
- **Gout:** The variant rs7546668 in DNAJC16 showed significant association with gout ([PMID: 36221101](https://pubmed.ncbi.nlm.nih.gov/36221101/)).
- **Lung adenocarcinoma:** circDNAJC16 acts as a tumor suppressor via miR-93-5p sponging ([PMID: 41138842](https://pubmed.ncbi.nlm.nih.gov/41138842/)).
- **NAFLD/HCC:** DNAJC16 identified as a feature gene in a deep-learning screen for NASH-related HCC biomarkers ([PMID: 40206734](https://pubmed.ncbi.nlm.nih.gov/40206734/)).
- **Shrimp innate immunity:** *P. vannamei* DnaJC16 facilitates WSSV infection via hemocyte apoptosis ([PMID: 37105425](https://pubmed.ncbi.nlm.nih.gov/37105425/)).

These associations suggest DNAJC16 is biologically important across diverse contexts, but none provide molecular-function information.

---

## Limitations and Knowledge Gaps

### Critical Gaps in the Current Literature

1. **No biochemical characterization.** Not a single in vitro assay has been published for DNAJC16 — no HSP70 binding, no ATPase stimulation, no redox activity measurement. This is the most significant gap.

2. **Single primary study.** All functional conclusions derive from Yamamoto et al. 2020. No independent replication or extension has been published in six years.

3. **No domain-specific rescue in knockout cells.** The overexpression domain-deletion experiments cannot distinguish whether domains are needed for protein stability/localization versus catalytic function.

4. **Binding partners unknown.** No interactome study (BioID, AP-MS, crosslinking mass spectrometry, or yeast two-hybrid) has been performed for DNAJC16.

5. **Topology not experimentally validated by dedicated assay.** The cytoplasmic orientation of the J-domain and TRX domain is inferred from UniProt annotation algorithms and N-glycosylation data, but no protease protection or selective permeabilization assay has been published specifically for these domains.

### Limitations of This Investigation

- This analysis relied entirely on publicly available literature and sequence databases; no novel experimental data were generated.
- The topology inference, while well-supported by bioinformatic evidence and glycosylation data, would benefit from direct experimental validation.
- DNAJC16's potential interaction with cytoplasmic HSP70s is plausible but entirely hypothetical.
- Only 40 papers were reviewed, which, while comprehensive for this niche topic, may miss relevant structural or biochemical studies in adjacent fields.

---

## Proposed Follow-up Experiments

### Tier 1: Molecular Function Determination (Highest Priority)

1. **HSP70 binding assay.** Co-immunoprecipitation of endogenous DNAJC16 with cytoplasmic HSP70s (HSPA1A, HSPA8/HSC70) in mammalian cells. Test binding dependence on the HPD motif using HPD→AAA mutant. This is the single most informative experiment for establishing molecular function.

2. **ATPase stimulation assay.** Purify the DNAJC16 cytoplasmic region (residues 1–535 or the isolated J-domain, residues 29–93) and test stimulation of HSC70 ATPase activity in vitro, using HPD→AAA as negative control and a known J-domain (e.g., from DNAJA1) as positive control.

3. **Redox activity assay.** Test insulin disulfide reduction and/or di-eosin-GSSG cleavage by purified DNAJC16 TRX domain (residues 119–247). Include CFSC→SFSS (C171S/C174S) mutant as negative control and purified thioredoxin as positive control.

4. **Topology validation.** Protease protection assay (proteinase K digestion of microsomes) or selective digitonin permeabilization with domain-specific antibodies to confirm cytoplasmic exposure of J and TRX domains.

### Tier 2: Cellular Mechanism (Medium Priority)

5. **Domain-specific rescue.** Generate DNAJC16 knockout cells and rescue with constructs expressed at near-endogenous levels (e.g., weak promoter or inducible system):
   - Wild-type DNAJC16
   - HPD→AAA (J-domain dead)
   - C171S/C174S (TRX CXXC dead)
   - J-domain deletion (ΔJ)
   - TRX domain deletion (ΔTRX)
   Assess autophagosome size with each construct during starvation-induced autophagy.

6. **Proximity labeling (BioID/TurboID).** Fuse BioID2 or TurboID to the cytoplasmic N-terminus of DNAJC16 to identify proximal interactors at the ER membrane, especially autophagy-related proteins and HSP70 family members.

7. **Live imaging.** Track DNAJC16 dynamics relative to autophagosome formation markers (WIPI2, ATG13, LC3) and PIS at ER subdomains during starvation-induced autophagy using fluorescent protein fusions.

### Tier 3: Structural and Evolutionary (Lower Priority)

8. **Structural biology.** Determine the crystal or cryo-EM structure of the DNAJC16 cytoplasmic region to assess whether the TRX domain has a competent active site or is structurally adapted for protein–protein interactions.

9. **Cross-species comparison.** Biochemically characterize *C. elegans* DNJ-8 — does its J-domain stimulate nematode HSP70? Does topology differ in invertebrates?

10. **Luminal C-terminal domain characterization.** The function of the luminal region (residues 557–782) is entirely unknown. Deletion constructs and proximity labeling from the luminal side could reveal whether it contributes to autophagosome size regulation through a distinct mechanism.

---

## Molecular Function Annotation Assessment

**Current GO annotations for DNAJC16 (Q9Y2G8):**
- **Cellular Component:** GO:0005789 — endoplasmic reticulum membrane (IDA) ✓
- **Biological Process:** GO:0016243 — regulation of autophagosome size (IMP) ✓
- **Molecular Function:** NONE

**Assessment of candidate molecular function annotations:**

| Candidate GO Term | Annotation Warranted? | Rationale |
|---|---|---|
| GO:0051087 — chaperone binding | **No** | No binding data for any HSP70 |
| GO:0030544 — Hsp70 protein binding | **No** | No co-IP or pulldown data |
| GO:0015036 — disulfide oxidoreductase activity | **No** | No redox assay; atypical active site |
| GO:0051082 — unfolded protein binding | **No** | No substrate binding data |
| GO:0005515 — protein binding | **Premature** | No interaction partners identified |

**Conclusion:** No molecular function annotation should be added to DNAJC16 until direct biochemical evidence is obtained. The "ERdj8" name should not be interpreted as evidence for BiP co-chaperone function, and automated annotation pipelines should be cautious about transferring molecular function annotations from other J-domain proteins to DNAJC16 given its unique topology.

---

## Conclusion

DNAJC16/ERdj8 is an ER membrane protein that regulates autophagosome size at PIS-enriched ER subdomains where autophagosome biogenesis occurs. Despite its name and domain architecture suggesting dual co-chaperone and redox functions, **no molecular function — neither HSP70 co-chaperone activity nor thioredoxin-like redox activity — has been experimentally demonstrated.** The membrane topology places the J-domain and TRX domain in the cytoplasm, ruling out the ER-luminal chaperone BiP as the cognate HSP70 partner and raising the possibility of interaction with cytoplasmic HSP70 family members instead. The thioredoxin-like domain's atypical CFSC motif and cytoplasmic localization argue against canonical disulfide reductase activity, suggesting instead a structural or scaffolding role. Both domains are required for the overexpression-driven autophagosome enlargement phenotype, but their requirement at endogenous levels and the biochemical mechanism through which they act remain entirely open questions. Six years after the initial characterization, the field urgently needs in vitro reconstitution and interaction studies to establish the molecular function of this protein.

---

*Report generated: 2026-07-06. Based on systematic analysis of 40 publications, UniProt/Pfam sequence databases, and domain architecture comparison across the J-domain protein family.*
