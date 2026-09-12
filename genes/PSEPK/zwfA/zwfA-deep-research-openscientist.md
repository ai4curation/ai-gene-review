---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-15T08:08:43.660344'
end_time: '2026-07-15T08:34:09.455214'
duration_seconds: 1525.8
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: zwfA
  gene_symbol: zwfA
  uniprot_accession: Q88P31
  protein_description: 'RecName: Full=Glucose-6-phosphate 1-dehydrogenase {ECO:0000256|HAMAP-Rule:MF_00966};
    Short=G6PD {ECO:0000256|HAMAP-Rule:MF_00966}; EC=1.1.1.49 {ECO:0000256|HAMAP-Rule:MF_00966};'
  gene_info: Name=zwfA {ECO:0000313|EMBL:AAN66647.1}; Synonyms=zwf {ECO:0000256|HAMAP-Rule:MF_00966};
    OrderedLocusNames=PP_1022 {ECO:0000313|EMBL:AAN66647.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the glucose-6-phosphate dehydrogenase family.
  protein_domains: G6P_DH. (IPR001282); G6P_DH_AS. (IPR019796); G6P_DH_C. (IPR022675);
    G6P_DH_NAD-bd. (IPR022674); NAD(P)-bd_dom_sf. (IPR036291)
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 8
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: zwfA-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: zwfA-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q88P31
- **Protein Description:** RecName: Full=Glucose-6-phosphate 1-dehydrogenase {ECO:0000256|HAMAP-Rule:MF_00966}; Short=G6PD {ECO:0000256|HAMAP-Rule:MF_00966}; EC=1.1.1.49 {ECO:0000256|HAMAP-Rule:MF_00966};
- **Gene Information:** Name=zwfA {ECO:0000313|EMBL:AAN66647.1}; Synonyms=zwf {ECO:0000256|HAMAP-Rule:MF_00966}; OrderedLocusNames=PP_1022 {ECO:0000313|EMBL:AAN66647.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the glucose-6-phosphate dehydrogenase family.
- **Key Domains:** G6P_DH. (IPR001282); G6P_DH_AS. (IPR019796); G6P_DH_C. (IPR022675); G6P_DH_NAD-bd. (IPR022674); NAD(P)-bd_dom_sf. (IPR036291)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "zwfA" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'zwfA' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **zwfA** (gene ID: zwfA, UniProt: Q88P31) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *zwfA* (PP_1022, UniProt Q88P31) in *Pseudomonas putida* KT2440

## Summary

**zwfA** (locus tag **PP_1022**, UniProt **Q88P31**) encodes **glucose-6-phosphate 1-dehydrogenase (G6PDH-A / ZwfA / PputG6PDH-1; EC 1.1.1.49)**, a cytoplasmic oxidoreductase that catalyzes the **first committed step of glucose catabolism** in *Pseudomonas putida* KT2440. The enzyme oxidizes D-glucose-6-phosphate (G6P) to 6-phospho-D-glucono-1,5-lactone with concomitant reduction of a nicotinamide dinucleotide cofactor, thereby feeding the intracellular **Entner–Doudoroff (ED) pathway**—the sole route for glycolytic breakdown of hexose in this organism—and the oxidative pentose-phosphate (PP) pathway. The gene symbol *zwfA* and the organism (*P. putida* KT2440) are unambiguously confirmed against the UniProt record, and the biochemical literature discussed below characterizes precisely this protein and its two paralogs (*zwfB*, *zwfC*).

The distinguishing feature of ZwfA is that it is a **genuine dual-cofactor enzyme**. Contrary to the textbook assumption that G6PDH is strictly NADP⁺-specific, purified ZwfA uses both NADP⁺ and NAD⁺ at physiologically comparable rates. Its cofactor-specificity constant (φ ≈ 3.3) is modest, and kinetic modeling indicates that in vivo it produces roughly **two-thirds NADH and one-third NADPH** per mole of G6P oxidized. ZwfA is the **predominant of three G6PDH isozymes** during glucose growth: markerless deletion of *zwfA* alone lowers the glucose growth rate by ~84%, whereas single deletions of *zwfB* or *zwfC* are nearly silent. This positions ZwfA as the physiological "gatekeeper" of glucose flux and the principal cellular source of reducing power.

Physiologically, ZwfA-generated NADPH is the redox currency that underpins *P. putida*'s notable oxidative-stress tolerance, and the enzyme operates within the **EDEMP cycle**—a cyclic metabolic architecture that recycles triose phosphates back to hexose phosphates to boost NADPH output. Transcriptionally, *zwfA* heads the **HexR-repressed *zwfA–pgl–eda* operon**, which is derepressed by the ED-pathway intermediate 2-keto-3-deoxy-6-phosphogluconate (KDPG) during growth on glucose or gluconate, and is further induced by oxidative stress. Together these data define ZwfA as the metabolic entry point coupling carbon catabolism to redox homeostasis in a biotechnologically important soil bacterium.

---

## Gene / Protein Identity (verified)

| Attribute | Value |
|---|---|
| UniProt accession | Q88P31 |
| Gene name / synonyms | *zwfA* / *zwf* |
| Ordered locus name | PP_1022 |
| Protein | Glucose-6-phosphate 1-dehydrogenase (G6PD) |
| EC number | 1.1.1.49 |
| Organism | *Pseudomonas putida* KT2440 (ATCC 47054 / DSM 6125) |
| Family | Glucose-6-phosphate dehydrogenase family |
| Key InterPro domains | G6P_DH (IPR001282), G6P_DH_AS (IPR019796), G6P_DH_C (IPR022675), G6P_DH_NAD-bd (IPR022674), NAD(P)-bd_dom_sf (IPR036291) |

**Identity verification:** The gene symbol *zwfA*, organism (*P. putida* KT2440), EC number, and G6PDH family/domain annotations are all mutually consistent, and the primary literature discussed below studies this exact protein (variously named ZwfA, *zwf-1*, PputG6PDH-1, or G6PDH-A; locus PP_1022). No ambiguity or cross-organism symbol confusion was encountered.

---

## Key Findings

### 1. ZwfA catalyzes the first committed step of glucose oxidation (EC 1.1.1.49)

ZwfA is **glucose-6-phosphate 1-dehydrogenase (G6PDH)**, EC 1.1.1.49. It catalyzes the oxidation of glucose-6-phosphate to 6-phospho-D-glucono-1,5-lactone with concomitant reduction of NAD(P)⁺ to NAD(P)H—the first committing step of the oxidative branch that feeds both the Entner–Doudoroff and pentose-phosphate pathways. The substrate is G6P, and Pseudomonas Zwf isozymes have been reported to show positive cooperativity toward this substrate. The protein belongs to the glucose-6-phosphate dehydrogenase family and carries the diagnostic InterPro domains G6P_DH (IPR001282), G6P_DH_C (IPR022675), G6P_DH_NAD-bd (IPR022674), and the NAD(P)-binding domain superfold (IPR036291), fully consistent with the UniProt annotation.

The reaction and its cofactor output are documented directly: G6PDH "generates NAD(P)H during the conversion of glucose-6-phosphate (G6P) to 6-phosphogluconolactone, thus aiding in anabolic processes, energy yield, and oxidative stress responses" ([PMID: 36354357](https://pubmed.ncbi.nlm.nih.gov/36354357/)). Its position as the pathway entry point is established by the observation that G6PDH "catalyzes the first committing step in the oxidative branch of the pentose phosphate (PP) pathway, feeding either the reductive PP or the Entner-Doudoroff pathway" ([PMID: 33727391](https://pubmed.ncbi.nlm.nih.gov/33727391/)).

### 2. ZwfA is the predominant G6PDH isoform on glucose and a dual-cofactor (NADP⁺/NAD⁺) enzyme producing more NADH than NADPH in vivo

*P. putida* KT2440 encodes **three G6PDH isozymes**: *zwfA* (PP_1022), *zwfB*, and *zwfC*. ZwfA (also named *zwf-1* / PputG6PDH-1) is the major isoform expressed during growth on glucose. Olavarría et al. (2015) purified this protein and studied its kinetics, stating explicitly that they set out "to determine the actual cofactor preference of the glucose-6-phosphate dehydrogenase encoded by the zwf-1 gene (PputG6PDH-1), the major isoform during growth on glucose" ([PMID: 26702395](https://pubmed.ncbi.nlm.nih.gov/26702395/)).

The central biochemical surprise is that ZwfA is **not strictly NADP⁺-specific**. Kinetic modeling showed that "the reaction catalyzed by PputG6PDH-1 yields around 1/3 mol of NADPH and 2/3 mol of NADH per mol of oxidized G6P" ([PMID: 26702395](https://pubmed.ncbi.nlm.nih.gov/26702395/)). Systematic characterization of all three isozymes confirmed that they carry different cofactor specificities and that some variants accept NAD⁺ similarly or even preferentially ([PMID: 33727391](https://pubmed.ncbi.nlm.nih.gov/33727391/)). Comparative work across Pseudomonas species shows the general pattern that ZwfA has the highest catalytic efficiency, positive cooperativity toward G6P, and dual cofactor specificity, whereas ZwfB is NADP⁺-preferring and ZwfC is strongly NADP⁺-specific ([PMID: 36354357](https://pubmed.ncbi.nlm.nih.gov/36354357/)).

### 3. ZwfA operates in the cytoplasm within the EDEMP cycle, the hub of glucose catabolism

Because G6PDH acts on the phosphorylated, intracellular metabolite glucose-6-phosphate, ZwfA activity is **cytoplasmic**. In *P. putida* KT2440, glucose can be partially oxidized in the periplasm to gluconate and 2-ketogluconate, but the phosphorylative branch (glucose → G6P via glucokinase → ZwfA → 6-P-gluconolactone → Pgl → 6-P-gluconate) operates inside the cell; in a related Pseudomonas, glucose "was metabolized via the intracellular phosphorylative route only" ([PMID: 36354357](https://pubmed.ncbi.nlm.nih.gov/36354357/)).

Nikel et al. (2015) showed that KT2440 metabolizes glucose through a cyclic architecture, the **EDEMP cycle**: "This set of reactions merges activities belonging to the ED, the EMP (operating in a gluconeogenic fashion), and the pentose phosphate pathways to form an unforeseen metabolic architecture (EDEMP cycle)" ([PMID: 26350459](https://pubmed.ncbi.nlm.nih.gov/26350459/)). In this cycle, ~10% of triose phosphates are recycled to hexose phosphates and re-oxidized by G6PDH, and as a result "cells growing on glucose thus run a biochemical cycle that favors NADPH formation" ([PMID: 26350459](https://pubmed.ncbi.nlm.nih.gov/26350459/)). ZwfA is the enzymatic entry point of this NADPH-favoring cycle.

### 4. The ZwfA-initiated ED/oxidative-PP route supplies the NADPH underpinning oxidative-stress tolerance

*P. putida* **lacks 6-phosphofructokinase**, so glucose catabolism cannot proceed by classical EMP glycolysis and instead runs exclusively through the ED pathway, which is initiated by ZwfA. Chavarría et al. (2013) established that "glucose catabolism of Pseudomonas putida is carried out exclusively through the Entner-Doudoroff (ED) pathway due to the absence of 6-phosphofructokinase" ([PMID: 23301697](https://pubmed.ncbi.nlm.nih.gov/23301697/)).

Forcing flux away from the ED route (by heterologously expressing *E. coli* PfkA) collapsed ATP and NAD(P)H pools, altered the NAD(P)H/NADP⁺ ratio, and rendered cells hypersensitive to the oxidants diamide and H₂O₂. The authors concluded that "these results expose the role of the ED pathway for generating the redox currency (NADPH) that is required for counteracting oxidative stress" ([PMID: 23301697](https://pubmed.ncbi.nlm.nih.gov/23301697/)). Because ZwfA is the committing enzyme of this route, it is the proximal generator of the NADPH used for antioxidant defense.

### 5. *zwfA* forms the HexR-regulated *zwfA–pgl–eda* operon, induced by KDPG and oxidative stress

*zwfA* is co-transcribed with *pgl* (6-phosphogluconolactonase) and *eda* (KDPG aldolase) as the **zwfA–pgl–eda operon**, physically coupling the first ED-pathway steps ([PMID: 33727391](https://pubmed.ncbi.nlm.nih.gov/33727391/)). Its expression is controlled by the repressor **HexR**. Kim et al. (2008) showed that "zwf-1, which encodes glucose-6-phosphate dehydrogenase, was highly induced when Pseudomonas putida KT2440 was cultured in minimal medium containing glucose or gluconate" ([PMID: 19047757](https://pubmed.ncbi.nlm.nih.gov/19047757/)), but was silent on pyruvate or succinate.

The mechanism of induction is derepression by an ED intermediate: "an electrophoretic mobility shift assay showed that HexR protein binds to the zwf-1 promoter region and that HexR binding is inhibited by 2-keto-3-deoxy-6-phosphogluconate (KDPG)" ([PMID: 19047757](https://pubmed.ncbi.nlm.nih.gov/19047757/)). Genetic evidence supports KDPG as the true inducer: *edd* mutants unable to make KDPG fail to induce, while *eda* mutants that overaccumulate KDPG are constitutively high. Additionally, "zwf-1 was also highly expressed in the presence of oxidative stress-inducing reagents" ([PMID: 19047757](https://pubmed.ncbi.nlm.nih.gov/19047757/)) such as menadione and cumene hydroperoxide, which also diminish HexR–DNA binding independently of KDPG—consistent with ZwfA's role in supplying antioxidant NADPH.

### 6. ZwfA is the physiologically dominant isozyme; structural basis of dual NADP⁺/NAD⁺ use

Systematic markerless deletion of all combinations of *zwfA/zwfB/zwfC* (Volke et al. 2021) demonstrated that ZwfA carries the bulk of cellular G6PDH activity. The single Δ*zwfA* strain had a specific growth rate **84% lower than wild type on glucose** and a significant defect on fructose (both routed heavily through G6PDH), plus a milder defect on gluconate; Δ*zwfB* and Δ*zwfC* single mutants grew nearly normally. There is redundancy for the PP-pathway role: only the double Δ*zwfAB* (and triple) mutants failed to grow on ribose, showing ZwfA and ZwfB can mutually supply PP-pathway flux, while ZwfC (near-zero turnover) is dispensable. This deletion study confirmed that the isozymes "catalyze the first committing step in the oxidative branch of the pentose phosphate (PP) pathway, feeding either the reductive PP or the Entner-Doudoroff pathway" ([PMID: 33727391](https://pubmed.ncbi.nlm.nih.gov/33727391/)), and the independent identification of ZwfA as "the major isoform during growth on glucose" ([PMID: 26702395](https://pubmed.ncbi.nlm.nih.gov/26702395/)) corroborates the severe deletion phenotype.

Kinetically, cofactor-specificity constants φ = (kcat/Km)NADP⁺ / (kcat/Km)NAD⁺ were: **G6PDH-A φ ≈ 3.34 ± 0.52** (uses NADP⁺ and NAD⁺ at similar proportions), G6PDH-B φ ≈ 0.86 ± 0.07 (NAD⁺-preferring), and G6PDH-C φ ≈ 2082 ± 532 (strongly NADP⁺-specific). Mechanistically, ZwfA follows a rapid-equilibrium random-ordered mechanism and belongs to G6PDH family I, carrying an arginine (R49, equivalent to *E. coli* R50) in the β2-α2 cofactor-discriminating loop; despite this arginine it retains substantial NAD⁺ usage, whereas G6PDH-B has a histidine (H68) at that position.

### 7. Direct kinetic parameters of purified ZwfA

Olavarría et al. (2015) cloned, expressed, and purified recombinant His-tagged ZwfA (PputG6PDH-1) and determined its steady-state kinetics, with a rapid-equilibrium random-ordered bisubstrate mechanism fitting best. They "estimated the in vivo relative production of NADH and NADPH during the oxidation of glucose-6-phosphate (G6P)" based on these constants ([PMID: 26702395](https://pubmed.ncbi.nlm.nih.gov/26702395/)). The measured constants were:

| Parameter | With NADP⁺ | With NAD⁺ |
|---|---|---|
| Km (cofactor) | 14 ± 2 µM | 127 ± 8 µM |
| Km (G6P) | 946 ± 49 µM | 1137 ± 37 µM |
| kcat | 102 ± 1 s⁻¹ | 277 ± 2 s⁻¹ |
| Ki (cofactor) | 111 ± 12 µM | 1148 ± 67 µM |

Thus NADP⁺ is bound ~9× more tightly (lower Km), but NAD⁺ supports ~2.7× faster turnover (higher kcat); the catalytic-efficiency ratio (kcat/Km)NADP⁺ / (kcat/Km)NAD⁺ ≈ 3.4, confirming only a **modest NADP⁺ preference**. Reduced-cofactor products inhibit the enzyme (NADPH mixed-type, Kic ≈ 35 µM; NADH competitive, Kic ≈ 480 µM), providing redox feedback. During growth on glucose as sole carbon source, ¹³C-flux estimates indicate **3–6 mmol gDW⁻¹ h⁻¹** passes through the ZwfA reaction (versus ~2 in *E. coli*). Control experiments confirmed that His-tag removal did not alter kinetics and that no host G6PDH co-purified, tying the measured constants directly to the physiological dual-cofactor output "of around 1/3 mol of NADPH and 2/3 mol of NADH per mol of oxidized G6P" ([PMID: 26702395](https://pubmed.ncbi.nlm.nih.gov/26702395/)).

---

## Mechanistic Model / Interpretation

ZwfA sits at the metabolic branch point where carbon catabolism and redox metabolism converge in *P. putida* KT2440. The following schematic places it in context:

```
   Glucose (extracellular)
        |
   [periplasm] -- partial oxidation --> gluconate --> 2-ketogluconate
        |                                   |
   glucose transport                    (re-import + phosphorylation)
        |                                   |
   [cytoplasm]                              v
   Glucose --glucokinase--> Glucose-6-P (G6P)
                                 |
                    +------------+-------------+
                    |  ZwfA / G6PDH-A (PP_1022)|  <== FIRST COMMITTED STEP
                    |  G6P + NAD(P)+  ->        |      phi ~ 3.3 (dual cofactor)
                    |  6-P-glucono-1,5-lactone  |      in vivo: ~2/3 NADH, 1/3 NADPH
                    |  + NAD(P)H                |
                    +------------+-------------+
                                 v
                          6-P-gluconolactone
                                 | Pgl
                                 v
                          6-phosphogluconate
                          /                \
                    (Edd) ED pathway     oxidative PP pathway
                         |                     |
                       KDPG  --> (relieves HexR repression of zwfA-pgl-eda operon)
                         | Eda
                    pyruvate + G3P --> EDEMP cycle (recycles ~10% triose-P to hexose-P)
                                              |
                                     favors NADPH formation
                                              |
                                     oxidative-stress defense (diamide, H2O2)
```

Three interlocking themes emerge:

**(1) A single dominant gatekeeper with paralog backup.** ZwfA carries most cellular G6PDH flux (Δ*zwfA* cuts glucose growth ~84%), while ZwfB provides redundancy specifically for pentose-phosphate flux (only Δ*zwfAB* fails on ribose) and ZwfC is functionally near-silent. The three-isozyme system lets the cell tune cofactor output: ZwfA (φ ≈ 3.3, balanced) and ZwfB (φ ≈ 0.86, NAD⁺-preferring) versus ZwfC (φ ≈ 2082, NADP⁺-specific).

**(2) Dual-cofactor output rewrites the textbook.** Unlike the canonical strictly NADP⁺-linked G6PDH, ZwfA binds NADP⁺ tightly (Km 14 µM) but turns NAD⁺ over faster (kcat 277 vs 102 s⁻¹), giving a net in vivo output biased toward NADH (~2/3). This blurs the classic catabolic/anabolic cofactor division and provides *P. putida* with a flexible source of both catabolic (NADH) and biosynthetic/antioxidant (NADPH) reducing equivalents from a single node.

**(3) Redox-linked regulation.** Expression is gated by the HexR–KDPG axis, coupling *zwfA* transcription to actual ED-pathway flux (KDPG is a proxy for pathway throughput), and layered with oxidative-stress induction. This ensures ZwfA is upregulated precisely when its NADPH product is needed—both for growth on glucose/gluconate and for antioxidant defense. The EDEMP cycle then amplifies NADPH yield by re-routing triose phosphates back through ZwfA.

---

## Evidence Base

| PMID | Study focus | Contribution |
|---|---|---|
| [26702395](https://pubmed.ncbi.nlm.nih.gov/26702395/) | *Quantifying NAD(P)H production in the upper ED pathway from P. putida KT2440* | **Primary biochemical characterization** of purified ZwfA (PputG6PDH-1): full kinetic constants, dual-cofactor mechanism, in vivo ~2/3 NADH : 1/3 NADPH, flux 3–6 mmol gDW⁻¹ h⁻¹. Supports Findings 1, 2, 7. |
| [33727391](https://pubmed.ncbi.nlm.nih.gov/33727391/) | *Cofactor Specificity of G6PDH Isozymes in P. putida* | **Systematic deletion + kinetics** of all three isozymes: φ values, Δ*zwfA* 84% growth defect, *zwfA–pgl–eda* operon, structural determinants (R49). Supports Findings 1, 2, 5, 6. |
| [19047757](https://pubmed.ncbi.nlm.nih.gov/19047757/) | *Dual regulation of zwf-1 by KDPG and oxidative stress* | **Transcriptional regulation**: HexR represses *zwf-1*/*zwfA*, relieved by KDPG (EMSA), plus oxidative-stress induction. Supports Finding 5. |
| [23301697](https://pubmed.ncbi.nlm.nih.gov/23301697/) | *ED pathway empowers P. putida with high oxidative-stress tolerance* | **Physiological role of the pathway**: ED is the sole glycolytic route (no PFK); it supplies NADPH redox currency for oxidative-stress defense. Supports Finding 4. |
| [26350459](https://pubmed.ncbi.nlm.nih.gov/26350459/) | *P. putida metabolizes glucose through the EDEMP cycle* | **Metabolic architecture**: defines the cytoplasmic EDEMP cycle that recycles triose-P and favors NADPH; places ZwfA in context. Supports Finding 3. |
| [36354357](https://pubmed.ncbi.nlm.nih.gov/36354357/) | *G6PDH ZwfA, a dual cofactor-specific isozyme in P. bharatica CSV86* | **Comparative Pseudomonas evidence**: reaction defined; ZwfA is the dominant, dual-cofactor, high-efficiency isoform; phosphorylative route is intracellular. Supports Findings 1, 2, 3. |

**Supporting context (family-level, not P. putida-specific):**
- [PMID: 27010804](https://pubmed.ncbi.nlm.nih.gov/27010804/) — *E. coli* G6PDH cofactor-specificity determinants (K18, R50), the structural framework used to interpret ZwfA's β2-α2 loop arginine.
- [PMID: 26856851](https://pubmed.ncbi.nlm.nih.gov/26856851/) — dual coenzyme-specific G6PDH from *Thermoanaerobacter*, an independent example of NADP⁺/NAD⁺ dual specificity in the family.

**Peripheral / lower-relevance** literature retrieved during the investigation (PMIDs 38470347, 33413621, 31657440, 34311585) concerns downstream biotechnology (dipicolinic acid, polyhydroxyalkanoate production), NAD(P)H repair, or mycofactocin, and does not bear directly on ZwfA's primary function.

All P. putida-specific claims trace to studies of the correct protein (ZwfA / *zwf-1* / PputG6PDH-1 / PP_1022 in *P. putida* KT2440), satisfying the mandatory identity verification. No conflicting-gene literature was mistakenly incorporated.

---

## Limitations and Knowledge Gaps

1. **No experimental 3D structure of ZwfA.** Cofactor-discriminating residues (R49) are inferred by homology to *E. coli* G6PDH ([PMID: 27010804](https://pubmed.ncbi.nlm.nih.gov/27010804/)). A crystal or cryo-EM structure of ZwfA with bound NADP⁺ vs NAD⁺ would confirm the structural basis of its unusual dual specificity.

2. **In vivo cofactor split is model-derived.** The "~2/3 NADH, 1/3 NADPH" figure comes from kinetic modeling using in vitro constants and estimated intracellular cofactor concentrations ([PMID: 26702395](https://pubmed.ncbi.nlm.nih.gov/26702395/)), not direct in vivo measurement. Real-time cofactor-specific flux measurement would strengthen this claim.

3. **Positive cooperativity toward G6P** is reported for Pseudomonas Zwf isozymes generally ([PMID: 36354357](https://pubmed.ncbi.nlm.nih.gov/36354357/)), but the Olavarría kinetic model for ZwfA used random-ordered Michaelis–Menten fitting; the degree and physiological relevance of cooperativity for KT2440 ZwfA specifically is not fully resolved.

4. **Quaternary structure and integrated allosteric regulation** (e.g., oligomeric state, NADPH/NADH feedback in the cellular context) are only partially characterized. Product inhibition constants exist, but a complete allosteric map does not.

5. **Localization is inferred, not directly imaged.** Cytoplasmic localization follows logically from the intracellular substrate (G6P) and pathway context but has not been demonstrated by fractionation or microscopy for ZwfA specifically.

6. **Regulatory detail of oxidative-stress induction.** How oxidative stress diminishes HexR–DNA binding independently of KDPG ([PMID: 19047757](https://pubmed.ncbi.nlm.nih.gov/19047757/)) at the molecular level (e.g., thiol modification of HexR) remains unresolved.

---

## Proposed Follow-up Experiments / Actions

1. **Structural determination** of ZwfA (X-ray/cryo-EM) in complex with G6P plus NADP⁺ and separately NAD⁺, to visualize the β2-α2 loop (R49) and explain why the arginine does not enforce strict NADP⁺ specificity as it does in *E. coli*.

2. **Site-directed mutagenesis** of R49 and neighboring β1-α1 loop residues, with kinetic re-measurement of φ, to test whether ZwfA's dual specificity can be rationally converted to strict NADP⁺- or NAD⁺-specificity—useful for engineering cofactor balance in *P. putida* cell factories.

3. **Direct in vivo cofactor-flux measurement** (e.g., ¹³C-metabolic flux analysis coupled with cofactor-specific biosensors) to validate the modeled 2/3 NADH : 1/3 NADPH split under different growth and stress conditions.

4. **HexR–DNA interaction under oxidative stress**: biochemical dissection (mutagenesis of HexR cysteines, redox titration) to determine the KDPG-independent mechanism of stress-induced derepression.

5. **Quantitative fitness/flux mapping of the isozyme trio** under gradients of carbon source and oxidant, combining Δ*zwfA*/Δ*zwfB*/Δ*zwfC* single and combinatorial mutants with proteomics, to define how the cell dynamically partitions G6PDH flux and cofactor output.

6. **Localization confirmation** via subcellular fractionation or fluorescent tagging to formally establish cytoplasmic residence and rule out membrane association.

---

## Supported and Refuted Hypotheses

**Supported:**
- ZwfA is a bona fide glucose-6-phosphate 1-dehydrogenase (EC 1.1.1.49) — confirmed by direct enzymology (Findings 1, 7).
- ZwfA is the physiologically dominant of three G6PDH isozymes on glucose — confirmed by deletion phenotype (Finding 6) and expression data (Finding 2).
- ZwfA is a genuine dual-cofactor enzyme, not strictly NADP⁺-specific — confirmed kinetically (Findings 2, 6, 7).
- ZwfA-derived NADPH supports oxidative-stress tolerance — supported by ED-pathway perturbation experiments (Finding 4).
- *zwfA* is HexR/KDPG-regulated within the *zwfA–pgl–eda* operon — confirmed genetically and by EMSA (Finding 5).

**Refuted:**
- The textbook assumption that this G6PDH is strictly NADP⁺-specific — explicitly refuted; in vivo it produces more NADH than NADPH (Findings 2, 7).

---

### Conclusion

ZwfA (PP_1022, Q88P31) is glucose-6-phosphate 1-dehydrogenase (EC 1.1.1.49), the predominant cytoplasmic G6PDH isozyme of *P. putida* KT2440. It catalyzes the first committed, NAD(P)⁺-reducing oxidation of glucose-6-phosphate that launches glucose into the Entner–Doudoroff pathway (the organism's only glycolytic route) and the pentose-phosphate pathway. Uniquely among canonical G6PDHs, it is a genuine dual-cofactor enzyme producing predominantly NADH but also the NADPH that fuels anabolism and oxidative-stress defense, and its expression is gated by the HexR–KDPG regulatory axis. It is the physiological gatekeeper of central carbon and redox metabolism in this bacterium.


## Artifacts

- [OpenScientist final report](zwfA-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](zwfA-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:36354357
2. PMID:33727391
3. PMID:26702395
4. PMID:26350459
5. PMID:23301697
6. PMID:19047757
7. PMID:27010804
8. PMID:26856851