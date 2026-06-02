---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-31T17:25:31.418312'
end_time: '2026-05-31T17:38:25.254113'
duration_seconds: 773.84
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: DANRE
  gene_id: uox
  gene_symbol: uox
  uniprot_accession: Q6DG85
  protein_description: 'RecName: Full=Uricase {ECO:0000255|PIRNR:PIRNR000241, ECO:0000255|RuleBase:RU004455,
    ECO:0000305}; EC=1.7.3.3 {ECO:0000255|PIRNR:PIRNR000241, ECO:0000255|RuleBase:RU004455,
    ECO:0000269|PubMed:27922051}; AltName: Full=Urate oxidase {ECO:0000255|PIRNR:PIRNR000241,
    ECO:0000303|PubMed:27922051};'
  gene_info: Name=uox {ECO:0000312|ZFIN:ZDB-GENE-030826-24};
  organism_full: Danio rerio (Zebrafish) (Brachydanio rerio).
  protein_family: Belongs to the uricase family.
  protein_domains: Uricase. (IPR002042); Uricase (PF01014)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 25
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 1
  edison_message_content: 1
artifacts:
- filename: artifact-00.md
  path: uox-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: image-1.png
  path: uox-deep-research-falcon_artifacts/image-1.png
  media_type: image/png
  source: edison_message_content
  data_storage_id: null
  description: '## Context ID: pqac-00000010 The kinetic parameters $K_m$ and $k_{cat}$
    for wild-type $DrUox$ and the F216S mutant are reported in Table 2 (found on page
    6). Th'
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q6DG85
- **Protein Description:** RecName: Full=Uricase {ECO:0000255|PIRNR:PIRNR000241, ECO:0000255|RuleBase:RU004455, ECO:0000305}; EC=1.7.3.3 {ECO:0000255|PIRNR:PIRNR000241, ECO:0000255|RuleBase:RU004455, ECO:0000269|PubMed:27922051}; AltName: Full=Urate oxidase {ECO:0000255|PIRNR:PIRNR000241, ECO:0000303|PubMed:27922051};
- **Gene Information:** Name=uox {ECO:0000312|ZFIN:ZDB-GENE-030826-24};
- **Organism (full):** Danio rerio (Zebrafish) (Brachydanio rerio).
- **Protein Family:** Belongs to the uricase family.
- **Key Domains:** Uricase. (IPR002042); Uricase (PF01014)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "uox" matches the protein description above**
2. **Verify the organism is correct:** Danio rerio (Zebrafish) (Brachydanio rerio).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'uox' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **uox** (gene ID: uox, UniProt: Q6DG85) in DANRE.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

Question: You are an expert researcher providing comprehensive, well-cited information.

Provide detailed information focusing on:
1. Key concepts and definitions with current understanding
2. Recent developments and latest research (prioritize 2023-2024 sources)
3. Current applications and real-world implementations
4. Expert opinions and analysis from authoritative sources
5. Relevant statistics and data from recent studies

Format as a comprehensive research report with proper citations. Include URLs and publication dates where available.
Always prioritize recent, authoritative sources and provide specific citations for all major claims.

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q6DG85
- **Protein Description:** RecName: Full=Uricase {ECO:0000255|PIRNR:PIRNR000241, ECO:0000255|RuleBase:RU004455, ECO:0000305}; EC=1.7.3.3 {ECO:0000255|PIRNR:PIRNR000241, ECO:0000255|RuleBase:RU004455, ECO:0000269|PubMed:27922051}; AltName: Full=Urate oxidase {ECO:0000255|PIRNR:PIRNR000241, ECO:0000303|PubMed:27922051};
- **Gene Information:** Name=uox {ECO:0000312|ZFIN:ZDB-GENE-030826-24};
- **Organism (full):** Danio rerio (Zebrafish) (Brachydanio rerio).
- **Protein Family:** Belongs to the uricase family.
- **Key Domains:** Uricase. (IPR002042); Uricase (PF01014)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "uox" matches the protein description above**
2. **Verify the organism is correct:** Danio rerio (Zebrafish) (Brachydanio rerio).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'uox' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **uox** (gene ID: uox, UniProt: Q6DG85) in DANRE.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Research report: **uox / urate oxidase (uricase)** in *Danio rerio* (UniProt **Q6DG85**)

## 0. Identity verification (critical disambiguation)
The target gene/protein is **uox** from **zebrafish (*Danio rerio*)**, encoding **urate oxidase/uricase (EC 1.7.3.3)** in the **uricase family**, and is mapped in the zebrafish peroxisomal inventory as **Uox (UniProt Q6DG85_DANRE)**. (kamoshita2022insightsintothe pages 12-14)

Primary zebrafish-focused literature explicitly characterizes **zebrafish urate oxidase (DrUox)** as a **298 aa enzyme** bearing a **C-terminal ARM tripeptide** (a **type 1 peroxisomal targeting signal, PTS1**), consistent with a peroxisomal uricolysis enzyme and matching the UniProt description you supplied. (marchetti2016catalysisandstructure pages 4-5)

## 1. Key concepts and current understanding

### 1.1 Definition and pathway context
**Urate oxidase (Uox; “uricase”)** catalyzes the **first (rate-limiting) step** of oxidative uricolysis/purine catabolism in many non-human vertebrates, initiating conversion of the relatively insoluble metabolite **urate (uric acid)** into downstream, more soluble products. In animals, the canonical uricolysis pathway is a **three-enzyme** sequence in which Uox generates **5-hydroxyisourate (HIU)**, followed by HIU hydrolase (Urah) and OHCU decarboxylase (Urad) to yield **(S)-allantoin**. (marchetti2016catalysisandstructure pages 1-2, marchetti2016catalysisandstructure pages 4-5, kamoshita2022insightsintothe pages 14-15)

### 1.2 Enzymatic reaction (substrate specificity and products)
Zebrafish Uox catalyzes **oxidation/hydroxylation of urate to HIU**, and is described as the **classical cofactorless Uox** (i.e., it does not require a tightly bound organic cofactor). (marchetti2016catalysisandstructure pages 1-2)

In the zebrafish peroxisomal context, Uox is grouped among peroxisomal oxidases that use **molecular oxygen (O₂)** as electron acceptor and generate **hydrogen peroxide (H₂O₂)** as a byproduct of oxidation chemistry (with catalase and related enzymes mitigating H₂O₂). (kamoshita2022insightsintothe pages 12-14, kamoshita2022insightsintothe pages 14-15)

**Substrate specificity (direct evidence):** The Marchetti et al. biochemical work quantifies kinetics using **urate as substrate** and discusses **xanthine as a competitive inhibitor** (reduced affinity in an engineered mutant), supporting urate as the physiologic substrate and xanthine as an inhibitory ligand for zebrafish Uox. (marchetti2016catalysisandstructure pages 4-5)

### 1.3 Protein architecture and catalytic site concepts
Zebrafish Uox forms a **tetramer** with the **T-fold** architecture typical of classical uricases; the functional active sites occur at subunit interfaces. (marchetti2016catalysisandstructure pages 1-2, marchetti2016catalysisandstructure media 5859e86c)

## 2. Localization: where uox functions in the cell and organism

### 2.1 Subcellular localization (peroxisome)
Two independent lines of evidence support **peroxisomal localization** of zebrafish Uox:

1) **Sequence targeting signal:** DrUox encodes a C-terminal **ARM** tripeptide corresponding to a **PTS1** motif, indicating peroxisomal matrix import. (marchetti2016catalysisandstructure pages 4-5)

2) **Peroxisomal inventory annotation:** A zebrafish peroxisomal proteome inventory lists Uox (Q6DG85_DANRE) as peroxisomal with PTS1 **ARM**. (kamoshita2022insightsintothe pages 12-14)

### 2.2 Redox environment considerations (expert mechanistic interpretation)
Marchetti et al. report that DrUox shows a propensity for non-native disulfide formation and that **reducing conditions increase functional stability**, arguing that the enzyme has been selected to function within peroxisomes and referencing that the **peroxisome lumen is more reducing than the cytosol**, which would help maintain free thiols and limit cysteine oxidation. (marchetti2016catalysisandstructure pages 7-9)

### 2.3 Tissue/developmental expression
Whole-mount in situ hybridization indicates **uox is expressed primarily in the developing liver** at **2 days post fertilization (dpf)**, with **strong liver expression persisting at 4 dpf** (and weaker extrahepatic signals). (linnerz2022uricasedeficientlarvalzebrafish pages 5-7)

## 3. Primary experimental evidence in zebrafish (genetics/phenotypes)

### 3.1 uox loss-of-function model and hyperuricemia-relevant phenotypes
A zebrafish **uox−/−** knockout line was generated using **CRISPR/Cas9** targeting **exon 2**, producing a **+7 bp insertion** leading to a premature stop codon predicted after ~aa 30. (linnerz2022uricasedeficientlarvalzebrafish pages 2-4)

In this model:
- Larvae have **elevated urate levels** (qualitatively stated in the retrieved evidence). (linnerz2022uricasedeficientlarvalzebrafish pages 2-4)
- After microinjection of **monosodium urate (MSU) crystals**, uox−/− larvae show **suppressed acute inflammatory response** and **prolonged in vivo MSU crystal persistence** (reported to persist at least to **4 days post-injection / 6 dpf**), with later-stage imaging showing macrophage-dominated **granuloma-like structures**. (linnerz2022uricasedeficientlarvalzebrafish pages 2-4)
- The persistence phenotype can be **rescued by uox mRNA injection**, supporting causal linkage between uox function and the observed MSU crystal handling. (linnerz2022uricasedeficientlarvalzebrafish pages 2-4)

These observations are consistent with the core molecular function of Uox: loss of urate catabolism increases urate availability and alters urate-crystal–driven inflammatory dynamics. (linnerz2022uricasedeficientlarvalzebrafish pages 2-4)

## 4. Quantitative functional data (recently used and citable)

### 4.1 Enzyme kinetics (recombinant zebrafish Uox)
Marchetti et al. report Michaelis–Menten kinetics for recombinant DrUox measured using a coupled assay that removes HIU absorbance interference by adding Urah. (marchetti2016catalysisandstructure pages 4-5)

Key parameters (Table 2):
- **Wild-type DrUox:** **Km = 11 ± 1 μM**, **kcat ≈ 4 s⁻¹**. (marchetti2016catalysisandstructure media 810c6d8a)
- **F216S DrUox mutant (hominoid-lineage mimicking substitution):** **Km = 284 ± 31 μM**, **kcat ≈ 4 s⁻¹** (i.e., ~25× lower affinity with preserved turnover). (marchetti2016catalysisandstructure media 810c6d8a)

These data support a functional annotation in which zebrafish Uox is a moderately efficient urate-oxidizing enzyme whose affinity can be markedly perturbed by active-site-proximal substitutions. (marchetti2016catalysisandstructure media 810c6d8a)

### 4.2 Quantitative assay-relevant partner-enzyme activity (Urah)
In the same coupled assay logic, recombinant **Urah** is described as highly active (specific activity **230 ± 6 μmol·min⁻¹·mg⁻¹**), and a **1:1 molar ratio (Urah:Uox)** sufficed to reach maximal initial velocity in the kinetic setup. (marchetti2016catalysisandstructure pages 4-5)

## 5. Recent developments (prioritizing 2023–2024 literature)

### 5.1 2023: Evolutionary repurposing of uricase in sauropsids (contextualizing zebrafish as a canonical peroxisomal reference)
A 2023 *Molecular Biology and Evolution* study reports that uricase has followed distinct evolutionary trajectories in vertebrates: in some lineages it is lost (pseudogenized), whereas in sauropsids it may be **repurposed (co-opted)**, including changes consistent with **non-canonical localization** and **cysteine enrichment**. The study highlights that in reptiles, the typical peroxisomal targeting context appears altered, implying Uox may be **not peroxisomal** in those taxa. (mori2023cysteineenrichmentmediates pages 3-4)

Critically, the paper contrasts these unusual properties with canonical vertebrate uricases like **zebrafish DrUox**, and reports single-turnover comparisons showing markedly less HIU formation for an avian cysteine-rich uricase vs DrUox (≈**20% HIU formed** relative to DrUox under comparable conditions), supporting a mechanistic shift away from straightforward degradative urate oxidation in that lineage. (mori2023cysteineenrichmentmediates pages 6-7)

### 5.2 2024: Biotechnology and production/diagnostics landscape for uricase
A 2024 review emphasizes that uricase has broad **diagnostic and biotechnological uses**, including **biosensors for uric acid**, and discusses production considerations favoring microbial sources (especially extracellular uricase to reduce purification costs). It also proposes forward-looking translational strategies such as **uricase gene–carrying recombinant probiotic microorganisms** as a potential gout-treatment concept. (elbanna2024microbialuricaseand pages 1-2)

### 5.3 2024: Clinical uricase therapy benchmarking (real-world implementation)
A 2024 randomized head-to-head phase 2 trial (COMPARE) in refractory gout compared a tolerance-inducing strategy **SEL-212 (ImmTOR + pegadricase; monthly)** to **pegloticase (biweekly)**.

Key quantitative endpoints reported:
- Primary endpoint (SU <6 mg/dL for ≥80% of the time during months 3 and 6): **53.0% (44/83)** for SEL-212 vs **46.0% (40/87)** for pegloticase (one-sided P=0.181). (baraf2024thecompareheadtohead pages 5-8)
- Percent SU reduction months 3+6: **73.79%** (SEL-212) vs **47.96%** (pegloticase), P=0.0161. (baraf2024thecompareheadtohead pages 1-2)
- Selected adverse events (SEL-212 vs pegloticase): gout flares **60.2% vs 50.6%**, infections **25.3% vs 18.4%**, infusion reactions **15.7% vs 11.5%**; stomatitis **9.6% vs 0%**. (baraf2024thecompareheadtohead pages 1-2)

Although this is human therapy rather than zebrafish biology, it is directly relevant to uricase as an enzyme class and motivates zebrafish uox models as platforms to study urate biology and inflammation. (baraf2024thecompareheadtohead pages 1-2)

## 6. Applications and real-world implementations relevant to zebrafish uox annotation

1) **Zebrafish uox−/− as an in vivo urate/MSU model:** uox knockout larvae enable prolonged MSU crystal persistence and granuloma-like responses, allowing imaging-accessible analysis of later-stage crystal–immune interactions that are otherwise difficult to model in vivo. (linnerz2022uricasedeficientlarvalzebrafish pages 2-4)

2) **Therapeutic uricases in medicine:** PEGylated uricase approaches (e.g., pegloticase, pegadricase) are clinically deployed/investigated for urate lowering, and 2024 head-to-head clinical trial data provide concrete performance and safety benchmarks. (baraf2024thecompareheadtohead pages 1-2)

3) **Diagnostics/industrial biotechnology:** microbial uricase is used/proposed for urate detection (biosensors) and various biotech applications; production strategies emphasize cost-effective microbial expression and extracellular enzyme recovery. (elbanna2024microbialuricaseand pages 1-2)

## 7. Expert synthesis (functional annotation statement)
Collectively, the most defensible functional annotation for zebrafish **uox/Q6DG85** is:

- **Molecular function:** peroxisomal **urate oxidase/uricase (EC 1.7.3.3)** catalyzing urate → HIU (first step of uricolysis), using O₂ and producing H₂O₂ as an oxidase byproduct. (marchetti2016catalysisandstructure pages 1-2, kamoshita2022insightsintothe pages 12-14)
- **Pathway:** peroxisomal purine catabolism/uricolysis followed by Urah and Urad to (S)-allantoin. (marchetti2016catalysisandstructure pages 1-2, kamoshita2022insightsintothe pages 14-15)
- **Localization:** peroxisomal matrix via C-terminal **PTS1 ARM**. (kamoshita2022insightsintothe pages 12-14, marchetti2016catalysisandstructure pages 4-5)
- **Physiological relevance:** modulation of larval urate levels and MSU-crystal inflammatory dynamics, as shown by uox−/− zebrafish phenotypes. (linnerz2022uricasedeficientlarvalzebrafish pages 2-4)

## 8. Evidence summary table
The following table consolidates the key evidence for annotation and is suitable for downstream functional annotation pipelines.

| Category | Summary | Key references |
|---|---|---|
| Protein / gene identifiers | **Danio rerio uox** encodes urate oxidase/uricase (**EC 1.7.3.3**), a **298 aa** uricase-family protein mapped in UniProt as **Q6DG85**; zebrafish Uox is described as a classical cofactorless Uox and is highly conserved among vertebrates. Zebrafish knockout work targeted **uox exon 2** and identified the protein as a ~303 aa product in vivo annotation context. (marchetti2016catalysisandstructure pages 4-5, marchetti2016catalysisandstructure pages 1-2, linnerz2022uricasedeficientlarvalzebrafish pages 5-7) | Marchetti et al., 2016, *Sci Rep*, doi:10.1038/srep38302, https://doi.org/10.1038/srep38302; Linnerz et al., 2022, *Genes*, doi:10.3390/genes13122179, https://doi.org/10.3390/genes13122179 |
| Enzymatic reaction | Uox catalyzes the **oxidation/hydroxylation of urate** to **5-hydroxyisourate (HIU)**, the first step of oxidative uricolysis/purine urate degradation. The reaction uses **molecular oxygen as electron acceptor** and is associated with **H2O2 formation** by peroxisomal oxidases. HIU is unstable and can interfere with direct spectrophotometric assays unless coupled to HIU hydrolase. (kamoshita2022insightsintothe pages 14-15, marchetti2016catalysisandstructure pages 4-5, marchetti2016catalysisandstructure pages 1-2) | Marchetti et al., 2016, https://doi.org/10.1038/srep38302; Kamoshita et al., 2022, https://doi.org/10.3389/fphys.2022.822509 |
| Pathway position / partner enzymes | Uox performs the **first, rate-limiting step** of the **three-step uricolysis pathway** in purine catabolism. In zebrafish/animals this is followed by **HIU hydrolase (Urah)** converting HIU to **OHCU**, then **OHCU decarboxylase (Urad)** forming **(S)-allantoin**. A 1:1 molar ratio of Urah:Uox was sufficient to achieve maximal initial velocity in the coupled assay, and recombinant Urah had a specific activity of **230 ± 6 μmol min−1 mg−1**. (kamoshita2022insightsintothe pages 14-15, marchetti2016catalysisandstructure pages 4-5, marchetti2016catalysisandstructure pages 1-2) | Marchetti et al., 2016, https://doi.org/10.1038/srep38302; Kamoshita et al., 2022, https://doi.org/10.3389/fphys.2022.822509 |
| Subcellular localization | Zebrafish Uox is placed in the **peroxisome**. Evidence includes a **C-terminal tripeptide ARM**, identified as a **type 1 peroxisomal targeting signal (PTS1)**, and review-level zebrafish peroxisomal inventory annotation listing Uox as peroxisomal with PTS1 **ARM**. (kamoshita2022insightsintothe pages 12-14, marchetti2016catalysisandstructure pages 4-5, marchetti2016catalysisandstructure media 810c6d8a) | Marchetti et al., 2016, https://doi.org/10.1038/srep38302; Kamoshita et al., 2022, https://doi.org/10.3389/fphys.2022.822509 |
| Kinetic parameters | For recombinant wild-type **DrUox**, **Km = 11 ± 1 μM** and **kcat ≈ 4 s−1**. The hominoid-like **F216S** variant retained similar turnover (**kcat ≈ 4 s−1**) but had markedly reduced substrate affinity with **Km = 284 ± 31 μM** (~25-fold increase). The F216S variant also showed reduced affinity for xanthine, consistent with failure to bind xanthine-agarose. (marchetti2016catalysisandstructure pages 4-5, marchetti2016catalysisandstructure pages 7-9, marchetti2016catalysisandstructure media 810c6d8a) | Marchetti et al., 2016, https://doi.org/10.1038/srep38302 |
| Zebrafish developmental expression | Whole-mount in situ hybridization showed **uox expression primarily in the developing liver at 2 dpf**, with **persistent strong liver expression at 4 dpf** and weaker extrahepatic signal. In **uox−/−** larvae, transcript signal was significantly reduced at 2 dpf, with some residual expression still detectable at 4 dpf. (linnerz2022uricasedeficientlarvalzebrafish pages 5-7) | Linnerz et al., 2022, https://doi.org/10.3390/genes13122179 |
| Zebrafish in vivo mutant evidence | **CRISPR/Cas9 uox knockout** was generated by targeting **exon 2**, producing a **+7 bp insertion** predicted to introduce a premature stop codon after **aa 30**. **uox−/−** larvae were viable/fertile with no embryonic mortality reported, had **elevated urate levels**, and showed a **reduced acute inflammatory response** to injected **monosodium urate (MSU) crystals**, **prolonged crystal persistence** (to at least **4 days post-injection / 6 dpf**), and **macrophage-dominated granuloma-like aggregates**; persistence phenotypes were rescued by **uox mRNA injection**. (linnerz2022uricasedeficientlarvalzebrafish pages 5-7, linnerz2022uricasedeficientlarvalzebrafish pages 2-4) | Linnerz et al., 2022, https://doi.org/10.3390/genes13122179 |


*Table: This table summarizes the core functional annotation for Danio rerio uox/urate oxidase (UniProt Q6DG85), including reaction chemistry, pathway role, peroxisomal localization, kinetic data, and zebrafish mutant evidence. It is designed as a compact evidence-backed reference for gene function and biological context.*

## 9. Evidence gaps and limitations (important for curation)
- The retrieved excerpts support that uox−/− larvae have **elevated urate**, but do **not** include a numeric urate concentration or effect size; extracting those would require additional targeted retrieval of the specific results section/figure from the 2022 zebrafish mutant study. (linnerz2022uricasedeficientlarvalzebrafish pages 2-4)
- Substrate specificity beyond urate (e.g., activity on urate analogs) is not quantitatively provided in the captured excerpts; however, inhibition/affinity effects involving xanthine are discussed for engineered variants and align with known uricase active-site ligand behavior. (marchetti2016catalysisandstructure pages 4-5)

## Key primary references (URLs; publication dates)
- Marchetti M. et al. **2016-12**. *Scientific Reports*: “Catalysis and Structure of Zebrafish Urate Oxidase…” https://doi.org/10.1038/srep38302 (marchetti2016catalysisandstructure pages 1-2)
- Linnerz T. et al. **2022-11**. *Genes*: “Uricase-Deficient Larval Zebrafish…” https://doi.org/10.3390/genes13122179 (linnerz2022uricasedeficientlarvalzebrafish pages 2-4)
- Mori G. et al. **2023-06**. *Molecular Biology and Evolution*: “Cysteine Enrichment Mediates Co-Option of Uricase…” https://doi.org/10.1093/molbev/msad200 (mori2023cysteineenrichmentmediates pages 3-4)
- Elbanna K. et al. **2024-06**. *Advancements of Microbiology*: “Microbial Uricase and its Unique Potential Applications” https://doi.org/10.2478/am-2024-0007 (elbanna2024microbialuricaseand pages 1-2)
- Baraf HSB et al. **2024-07**. *Rheumatology*: “COMPARE head-to-head RCT of SEL-212 vs pegloticase” https://doi.org/10.1093/rheumatology/kead333 (baraf2024thecompareheadtohead pages 1-2)


References

1. (kamoshita2022insightsintothe pages 12-14): Maki Kamoshita, Rechal Kumar, Marco Anteghini, Markus Kunze, Markus Islinger, Vítor Martins dos Santos, and Michael Schrader. Insights into the peroxisomal protein inventory of zebrafish. Frontiers in Physiology, Feb 2022. URL: https://doi.org/10.3389/fphys.2022.822509, doi:10.3389/fphys.2022.822509. This article has 17 citations.

2. (marchetti2016catalysisandstructure pages 4-5): Marialaura Marchetti, Anastasia Liuzzi, Beatrice Fermi, Romina Corsini, Claudia Folli, Valentina Speranzini, Francesco Gandolfi, Stefano Bettati, Luca Ronda, Laura Cendron, Rodolfo Berni, Giuseppe Zanotti, and Riccardo Percudani. Catalysis and structure of zebrafish urate oxidase provide insights into the origin of hyperuricemia in hominoids. Scientific Reports, Dec 2016. URL: https://doi.org/10.1038/srep38302, doi:10.1038/srep38302. This article has 30 citations and is from a peer-reviewed journal.

3. (marchetti2016catalysisandstructure pages 1-2): Marialaura Marchetti, Anastasia Liuzzi, Beatrice Fermi, Romina Corsini, Claudia Folli, Valentina Speranzini, Francesco Gandolfi, Stefano Bettati, Luca Ronda, Laura Cendron, Rodolfo Berni, Giuseppe Zanotti, and Riccardo Percudani. Catalysis and structure of zebrafish urate oxidase provide insights into the origin of hyperuricemia in hominoids. Scientific Reports, Dec 2016. URL: https://doi.org/10.1038/srep38302, doi:10.1038/srep38302. This article has 30 citations and is from a peer-reviewed journal.

4. (kamoshita2022insightsintothe pages 14-15): Maki Kamoshita, Rechal Kumar, Marco Anteghini, Markus Kunze, Markus Islinger, Vítor Martins dos Santos, and Michael Schrader. Insights into the peroxisomal protein inventory of zebrafish. Frontiers in Physiology, Feb 2022. URL: https://doi.org/10.3389/fphys.2022.822509, doi:10.3389/fphys.2022.822509. This article has 17 citations.

5. (marchetti2016catalysisandstructure media 5859e86c): Marialaura Marchetti, Anastasia Liuzzi, Beatrice Fermi, Romina Corsini, Claudia Folli, Valentina Speranzini, Francesco Gandolfi, Stefano Bettati, Luca Ronda, Laura Cendron, Rodolfo Berni, Giuseppe Zanotti, and Riccardo Percudani. Catalysis and structure of zebrafish urate oxidase provide insights into the origin of hyperuricemia in hominoids. Scientific Reports, Dec 2016. URL: https://doi.org/10.1038/srep38302, doi:10.1038/srep38302. This article has 30 citations and is from a peer-reviewed journal.

6. (marchetti2016catalysisandstructure pages 7-9): Marialaura Marchetti, Anastasia Liuzzi, Beatrice Fermi, Romina Corsini, Claudia Folli, Valentina Speranzini, Francesco Gandolfi, Stefano Bettati, Luca Ronda, Laura Cendron, Rodolfo Berni, Giuseppe Zanotti, and Riccardo Percudani. Catalysis and structure of zebrafish urate oxidase provide insights into the origin of hyperuricemia in hominoids. Scientific Reports, Dec 2016. URL: https://doi.org/10.1038/srep38302, doi:10.1038/srep38302. This article has 30 citations and is from a peer-reviewed journal.

7. (linnerz2022uricasedeficientlarvalzebrafish pages 5-7): Tanja Linnerz, Yih Jian Sung, Leah Rolland, Jonathan W. Astin, Nicola Dalbeth, and Christopher J. Hall. Uricase-deficient larval zebrafish with elevated urate levels demonstrate suppressed acute inflammatory response to monosodium urate crystals and prolonged crystal persistence. Genes, 13:2179, Nov 2022. URL: https://doi.org/10.3390/genes13122179, doi:10.3390/genes13122179. This article has 12 citations.

8. (linnerz2022uricasedeficientlarvalzebrafish pages 2-4): Tanja Linnerz, Yih Jian Sung, Leah Rolland, Jonathan W. Astin, Nicola Dalbeth, and Christopher J. Hall. Uricase-deficient larval zebrafish with elevated urate levels demonstrate suppressed acute inflammatory response to monosodium urate crystals and prolonged crystal persistence. Genes, 13:2179, Nov 2022. URL: https://doi.org/10.3390/genes13122179, doi:10.3390/genes13122179. This article has 12 citations.

9. (marchetti2016catalysisandstructure media 810c6d8a): Marialaura Marchetti, Anastasia Liuzzi, Beatrice Fermi, Romina Corsini, Claudia Folli, Valentina Speranzini, Francesco Gandolfi, Stefano Bettati, Luca Ronda, Laura Cendron, Rodolfo Berni, Giuseppe Zanotti, and Riccardo Percudani. Catalysis and structure of zebrafish urate oxidase provide insights into the origin of hyperuricemia in hominoids. Scientific Reports, Dec 2016. URL: https://doi.org/10.1038/srep38302, doi:10.1038/srep38302. This article has 30 citations and is from a peer-reviewed journal.

10. (mori2023cysteineenrichmentmediates pages 3-4): Giulia Mori, Anastasia Liuzzi, Luca Ronda, Michele Di Palma, Magda S. Chegkazi, Soi Bui, Mitla Garcia-Maya, Jasmine Ragazzini, Marco Malatesta, Emanuele Della Monica, Claudio Rivetti, Parker Antin, Stefano Bettati, Roberto A. Steiner, and Riccardo Percudani. Cysteine enrichment mediates co-option of uricase in reptilian skin and transition to uricotelism. Molecular Biology and Evolution, Jun 2023. URL: https://doi.org/10.1093/molbev/msad200, doi:10.1093/molbev/msad200. This article has 10 citations and is from a highest quality peer-reviewed journal.

11. (mori2023cysteineenrichmentmediates pages 6-7): Giulia Mori, Anastasia Liuzzi, Luca Ronda, Michele Di Palma, Magda S. Chegkazi, Soi Bui, Mitla Garcia-Maya, Jasmine Ragazzini, Marco Malatesta, Emanuele Della Monica, Claudio Rivetti, Parker Antin, Stefano Bettati, Roberto A. Steiner, and Riccardo Percudani. Cysteine enrichment mediates co-option of uricase in reptilian skin and transition to uricotelism. Molecular Biology and Evolution, Jun 2023. URL: https://doi.org/10.1093/molbev/msad200, doi:10.1093/molbev/msad200. This article has 10 citations and is from a highest quality peer-reviewed journal.

12. (elbanna2024microbialuricaseand pages 1-2): Khaled Elbanna, Atheer Alshareef, Leena A. Neyaz, Mahmoud Z. El-Readi, and Hussein H. Abulreesh. Microbial uricase and its unique potential applications. Advancements of Microbiology, 63:81-91, Jun 2024. URL: https://doi.org/10.2478/am-2024-0007, doi:10.2478/am-2024-0007. This article has 6 citations.

13. (baraf2024thecompareheadtohead pages 5-8): Herbert S B Baraf, Puja P Khanna, Alan J Kivitz, Vibeke Strand, Hyon K Choi, Robert Terkeltaub, Nicola Dalbeth, Wesley DeHaan, Rehan Azeem, Peter G Traber, and Robert T Keenan. The compare head-to-head, randomized controlled trial of sel-212 (pegadricase plus rapamycin-containing nanoparticle, immtor™) versus pegloticase for refractory gout. Rheumatology, 63:1058-1067, Jul 2024. URL: https://doi.org/10.1093/rheumatology/kead333, doi:10.1093/rheumatology/kead333. This article has 26 citations and is from a peer-reviewed journal.

14. (baraf2024thecompareheadtohead pages 1-2): Herbert S B Baraf, Puja P Khanna, Alan J Kivitz, Vibeke Strand, Hyon K Choi, Robert Terkeltaub, Nicola Dalbeth, Wesley DeHaan, Rehan Azeem, Peter G Traber, and Robert T Keenan. The compare head-to-head, randomized controlled trial of sel-212 (pegadricase plus rapamycin-containing nanoparticle, immtor™) versus pegloticase for refractory gout. Rheumatology, 63:1058-1067, Jul 2024. URL: https://doi.org/10.1093/rheumatology/kead333, doi:10.1093/rheumatology/kead333. This article has 26 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](uox-deep-research-falcon_artifacts/artifact-00.md)
![## Context ID: pqac-00000010 The kinetic parameters $K_m$ and $k_{cat}$ for wild-type $DrUox$ and the F216S mutant are reported in Table 2 (found on page 6). Th](uox-deep-research-falcon_artifacts/image-1.png)

## Citations

1. kamoshita2022insightsintothe pages 12-14
2. marchetti2016catalysisandstructure pages 4-5
3. marchetti2016catalysisandstructure pages 1-2
4. marchetti2016catalysisandstructure pages 7-9
5. linnerz2022uricasedeficientlarvalzebrafish pages 5-7
6. linnerz2022uricasedeficientlarvalzebrafish pages 2-4
7. mori2023cysteineenrichmentmediates pages 3-4
8. mori2023cysteineenrichmentmediates pages 6-7
9. elbanna2024microbialuricaseand pages 1-2
10. baraf2024thecompareheadtohead pages 5-8
11. baraf2024thecompareheadtohead pages 1-2
12. kamoshita2022insightsintothe pages 14-15
13. https://doi.org/10.1038/srep38302;
14. https://doi.org/10.3390/genes13122179
15. https://doi.org/10.3389/fphys.2022.822509
16. https://doi.org/10.1038/srep38302
17. https://doi.org/10.1093/molbev/msad200
18. https://doi.org/10.2478/am-2024-0007
19. https://doi.org/10.1093/rheumatology/kead333
20. https://doi.org/10.3389/fphys.2022.822509,
21. https://doi.org/10.1038/srep38302,
22. https://doi.org/10.3390/genes13122179,
23. https://doi.org/10.1093/molbev/msad200,
24. https://doi.org/10.2478/am-2024-0007,
25. https://doi.org/10.1093/rheumatology/kead333,