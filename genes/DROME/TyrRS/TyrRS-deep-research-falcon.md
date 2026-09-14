---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-08T17:51:04.052952'
end_time: '2026-09-08T18:01:28.978211'
duration_seconds: 624.93
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: DROME
  gene_id: TyrRS
  gene_symbol: TyrRS
  uniprot_accession: Q9VV60
  protein_description: 'RecName: Full=Tyrosine--tRNA ligase {ECO:0000256|RuleBase:RU361234};
    EC=6.1.1.1 {ECO:0000256|RuleBase:RU361234}; AltName: Full=Tyrosyl-tRNA synthetase
    {ECO:0000256|RuleBase:RU361234};'
  gene_info: Name=TyrRS {ECO:0000313|EMBL:AAF49462.1, ECO:0000313|FlyBase:FBgn0027080};
    Synonyms=Aats-tyr {ECO:0000313|EMBL:AAF49462.1}, anon-EST:Posey261 {ECO:0000313|EMBL:AAF49462.1},
    Dmel\CG4561 {ECO:0000313|EMBL:AAF49462.1}, dTyrRS {ECO:0000313|EMBL:AAF49462.1},
    dYARS {ECO:0000313|EMBL:AAF49462.1}, dYARS1 {ECO:0000313|EMBL:AAF49462.1}, EMAP
    {ECO:0000313|EMBL:AAF49462.1}, YARS {ECO:0000313|EMBL:AAF49462.1}, YRS {ECO:0000313|EMBL:AAF49462.1};
    ORFNames=CG4561 {ECO:0000313|EMBL:AAF49462.1, ECO:0000313|FlyBase:FBgn0027080},
    Dmel_CG4561 {ECO:0000313|EMBL:AAF49462.1};
  organism_full: Drosophila melanogaster (Fruit fly).
  protein_family: Belongs to the class-I aminoacyl-tRNA synthetase family.
  protein_domains: aa-tRNA-synth_Ic. (IPR002305); NA-bd_OB-fold. (IPR012340); Rossmann-like_a/b/a_fold.
    (IPR014729); tRNA-bd_dom. (IPR002547); Tyr-tRNA-ligase. (IPR002307)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 25
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: TyrRS-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q9VV60
- **Protein Description:** RecName: Full=Tyrosine--tRNA ligase {ECO:0000256|RuleBase:RU361234}; EC=6.1.1.1 {ECO:0000256|RuleBase:RU361234}; AltName: Full=Tyrosyl-tRNA synthetase {ECO:0000256|RuleBase:RU361234};
- **Gene Information:** Name=TyrRS {ECO:0000313|EMBL:AAF49462.1, ECO:0000313|FlyBase:FBgn0027080}; Synonyms=Aats-tyr {ECO:0000313|EMBL:AAF49462.1}, anon-EST:Posey261 {ECO:0000313|EMBL:AAF49462.1}, Dmel\CG4561 {ECO:0000313|EMBL:AAF49462.1}, dTyrRS {ECO:0000313|EMBL:AAF49462.1}, dYARS {ECO:0000313|EMBL:AAF49462.1}, dYARS1 {ECO:0000313|EMBL:AAF49462.1}, EMAP {ECO:0000313|EMBL:AAF49462.1}, YARS {ECO:0000313|EMBL:AAF49462.1}, YRS {ECO:0000313|EMBL:AAF49462.1}; ORFNames=CG4561 {ECO:0000313|EMBL:AAF49462.1, ECO:0000313|FlyBase:FBgn0027080}, Dmel_CG4561 {ECO:0000313|EMBL:AAF49462.1};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Belongs to the class-I aminoacyl-tRNA synthetase family.
- **Key Domains:** aa-tRNA-synth_Ic. (IPR002305); NA-bd_OB-fold. (IPR012340); Rossmann-like_a/b/a_fold. (IPR014729); tRNA-bd_dom. (IPR002547); Tyr-tRNA-ligase. (IPR002307)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "TyrRS" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'TyrRS' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **TyrRS** (gene ID: TyrRS, UniProt: Q9VV60) in DROME.

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
- **UniProt Accession:** Q9VV60
- **Protein Description:** RecName: Full=Tyrosine--tRNA ligase {ECO:0000256|RuleBase:RU361234}; EC=6.1.1.1 {ECO:0000256|RuleBase:RU361234}; AltName: Full=Tyrosyl-tRNA synthetase {ECO:0000256|RuleBase:RU361234};
- **Gene Information:** Name=TyrRS {ECO:0000313|EMBL:AAF49462.1, ECO:0000313|FlyBase:FBgn0027080}; Synonyms=Aats-tyr {ECO:0000313|EMBL:AAF49462.1}, anon-EST:Posey261 {ECO:0000313|EMBL:AAF49462.1}, Dmel\CG4561 {ECO:0000313|EMBL:AAF49462.1}, dTyrRS {ECO:0000313|EMBL:AAF49462.1}, dYARS {ECO:0000313|EMBL:AAF49462.1}, dYARS1 {ECO:0000313|EMBL:AAF49462.1}, EMAP {ECO:0000313|EMBL:AAF49462.1}, YARS {ECO:0000313|EMBL:AAF49462.1}, YRS {ECO:0000313|EMBL:AAF49462.1}; ORFNames=CG4561 {ECO:0000313|EMBL:AAF49462.1, ECO:0000313|FlyBase:FBgn0027080}, Dmel_CG4561 {ECO:0000313|EMBL:AAF49462.1};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Belongs to the class-I aminoacyl-tRNA synthetase family.
- **Key Domains:** aa-tRNA-synth_Ic. (IPR002305); NA-bd_OB-fold. (IPR012340); Rossmann-like_a/b/a_fold. (IPR014729); tRNA-bd_dom. (IPR002547); Tyr-tRNA-ligase. (IPR002307)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "TyrRS" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'TyrRS' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **TyrRS** (gene ID: TyrRS, UniProt: Q9VV60) in DROME.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Functional annotation report: *Drosophila melanogaster* TyrRS (Q9VV60; CG4561)

## Executive conclusion

The requested protein is correctly identified as the **cytosolic tyrosyl-tRNA synthetase** of *Drosophila melanogaster*: TyrRS, historically called **Aats-tyr**, dTyrRS, or dYARS and encoded by **CG4561**. It should not be confused with the separate mitochondrial enzyme **TyrRS-m**, or with the unrelated *Drosophila* **yar** long noncoding RNA. The fly aaRS nomenclature explicitly reserves TyrRS for the cytosolic enzyme and TyrRS-m for the mitochondrial enzyme; a primary study independently identifies endogenous CG4561 as *Drosophila* TyrRS. Thus, the literature reviewed here matches UniProt Q9VV60 and the specified organism and protein class. (lu2015theaminoacyltrnasynthetases pages 4-5, casastinto2015activejnkdependentsecretion pages 1-2)

Its primary function is the ATP-dependent attachment of **L-tyrosine to cytosolic tRNA^Tyr**, generating Tyr-tRNA^Tyr for ribosomal protein synthesis. The strongest additional functions are: (i) conditional secretion from apoptotic “loser” cells and extracellular recruitment of haemocytes during cell competition; and (ii) a conserved capacity to bind and bundle F-actin. Nuclear transcriptional effects and neuropathy mechanisms are well supported in *Drosophila* disease models, but mostly involve transgenic human YARS1 rather than endogenous Q9VV60 and therefore should not automatically be treated as fully established physiological functions of the native fly protein. (storkebaum2009dominantmutationsin pages 1-2, casastinto2015activejnkdependentsecretion pages 1-2, bervoets2019transcriptionaldysregulationby pages 1-2, ermanoska2023tyrosyltrnasynthetasehas pages 3-4)

## 1. Identity, nomenclature, and domain consistency

### Identity verification

* **Accession and gene:** UniProt Q9VV60; CG4561; TyrRS/Aats-tyr/dYARS/dTyrRS.
* **Organism:** *Drosophila melanogaster*.
* **Compartmental identity:** cytosolic TyrRS, not mitochondrial TyrRS-m.
* **Ambiguous-name exclusion:** the lowercase *yar* gene encountered in fly literature is a cytoplasmic long noncoding RNA affecting sleep and is unrelated to tyrosyl-tRNA synthetase. It was excluded from this annotation.

A functional-complementation study found that the fly protein is approximately **68% identical and 80% similar** to human TyrRS; wild-type human YARS1 rescued a dYARS-RNAi bristle phenotype. This establishes functional orthology as well as sequence similarity. (storkebaum2009dominantmutationsin pages 2-2)

### Family and architecture

The supplied UniProt annotation—class-I aminoacyl-tRNA synthetase, aa-tRNA-synth_Ic/Rossmann-like catalytic fold, anticodon/tRNA-binding domain, OB-fold-related nucleic-acid-binding region, and Tyr-tRNA-ligase signature—is internally consistent with published TyrRS architecture. TyrRS functions as a **homodimer**, and each subunit contains an N-terminal catalytic region, central anticodon-recognition region, and metazoan C-terminal EMAP-II-like domain. (storkebaum2009dominantmutationsin pages 1-2)

The C-terminal EMAP-like extension is particularly important for interpreting noncanonical extracellular activity. Its presence does not change the central annotation: Q9VV60 remains first and foremost a cytosolic aminoacyl-tRNA synthetase.

## 2. Canonical biochemical function

### Reaction

TyrRS catalyzes EC 6.1.1.1:

**L-tyrosine + ATP + tRNA^Tyr → L-tyrosyl-tRNA^Tyr + AMP + PPi**

The reaction proceeds in two steps:

1. **Activation:** L-tyrosine + ATP → Tyr-AMP + PPi.
2. **Transfer:** Tyr-AMP + tRNA^Tyr → Tyr-tRNA^Tyr + AMP.

The charged tRNA delivers tyrosine to ribosomes decoding tyrosine codons during cytosolic translation. Published fly-model work explicitly describes TyrRS as an essential, ubiquitously expressed protein-biosynthesis enzyme and assays Tyr-tRNA^Tyr production and tyrosine-dependent ATP–PPi exchange. (storkebaum2009dominantmutationsin pages 1-2, storkebaum2009dominantmutationsin pages 2-2)

### Substrate specificity

The physiological substrates are **L-tyrosine, ATP, and cognate cytosolic tRNA^Tyr**. The literature retrieved did not report purified-Q9VV60 kinetic constants or a comprehensive specificity panel against alternative amino acids or noncognate fly tRNAs. Consequently, tyrosine/tRNA^Tyr specificity is strongly established by enzyme-family assignment, biochemical assays, and functional orthology, but numerical Km or kcat values should not be assigned to Q9VV60 without a protein-specific assay.

Human disease variants modeled in flies illustrate that catalytic impairment and organismal toxicity can be separated. G41R and Δ153–156VKQV substantially compromise aminoacylation, whereas E196K remains catalytically active but still produces neuropathic phenotypes. Therefore, mutant toxicity is not adequately explained by loss of tyrosine charging alone. (morant2021drosophilamodelsfor pages 9-10)

## 3. Cellular and extracellular localization

### Basal localization

The enzyme’s canonical site of action is the **cytosol**, where it supplies Tyr-tRNA^Tyr to cytoplasmic ribosomes. It is not the enzyme responsible for charging mitochondrial tRNA^Tyr; that function belongs to TyrRS-m. (lu2015theaminoacyltrnasynthetases pages 4-5, lu2015theaminoacyltrnasynthetases pages 3-4)

In fly neurons overexpressing human YARS1, wild-type and mutant proteins were distributed through cell bodies, axons, neuromuscular junctions, and major sensory-neuron dendrites. These experiments demonstrate access to neuronal compartments but do not resolve the endogenous distribution of Q9VV60 because overexpression can conceal subtle localization differences. The authoritative fly-model review recommends endogenous-level approaches such as CRISPR tagging for this reason. (morant2021drosophilamodelsfor pages 10-12)

### Conditional extracellular localization

A direct endogenous-fly study showed that apoptotic loser cells in imaginal-disc cell competition transcriptionally upregulate CG4561/TyrRS, with expression peaking approximately **24 hours after clone induction**. TyrRS was detected within loser cells and extracellularly adjacent to them. Its release requires **JNK signaling** and the secretory-pathway component **Kish**, with gryzun also implicated, indicating regulated secretion rather than nonspecific leakage alone. (casastinto2015activejnkdependentsecretion pages 1-2)

Extracellular TyrRS is cleaved by matrix metalloproteinases, particularly the Mmp1/2 system, into an N-terminal **MiniTyr** portion and C-terminal **EMAP** fragment. EMAP acts as the principal haemocyte-guidance cue, activating PI3K-associated migration and promoting recruitment of macrophage-like haemocytes to apoptotic loser cells for corpse clearance. Full-length secreted TyrRS and MiniTyr can promote apoptosis, whereas secreted EMAP does not, indicating functional partitioning after cleavage. The haemocyte receptor remains unidentified, and the generality of this pathway outside cell competition is unresolved. (casastinto2015activejnkdependentsecretion pages 10-11, casastinto2015activejnkdependentsecretion pages 1-2)

## 4. Biological processes and pathways

### 4.1 Cytosolic translation

The core pathway is aminoacyl-tRNA synthesis and genetic-code translation. TyrRS supplies charged tRNA^Tyr, making it directly responsible for maintaining tyrosine incorporation into newly synthesized proteins. Because aminoacylation is required in every translating cell, the enzyme is expected to be broadly required, although the retrieved studies did not provide a clean endogenous-null viability analysis for Q9VV60. A 50% reduction in dYARS dosage did not impair climbing, showing that this behavioral assay tolerates partial dosage reduction and arguing against simple haploinsufficiency as the cause of dominant YARS1 neuropathy-model phenotypes. (storkebaum2009dominantmutationsin pages 1-2, storkebaum2009dominantmutationsin pages 2-2)

### 4.2 Cell competition, apoptosis, and innate-cell recruitment

The endogenous pathway supported by direct fly evidence is:

**loser-cell stress/apoptosis → JNK activation → Kish-dependent TyrRS secretion → extracellular MMP cleavage → EMAP-mediated PI3K activation in haemocytes → haemocyte chemotaxis and corpse clearance.**

This is a precise noncanonical role connecting a translation enzyme to tissue-quality control and macrophage-like surveillance. It is currently the strongest evidence that native Q9VV60 acts outside the cytosol. (casastinto2015activejnkdependentsecretion pages 1-2, casastinto2015activejnkdependentsecretion pages 10-11)

### 4.3 F-actin organization—the major 2023 development

Ermanoska and colleagues reported in March 2023 that TyrRS is a direct F-actin-binding and bundling protein. High-speed co-sedimentation measured apparent dissociation constants of **0.75 μM for wild-type YARS1 and 0.80 μM for E196K**, indicating that E196K does not materially alter simple filament affinity. Low-speed sedimentation and cellular analyses instead showed altered/enhanced bundling behavior. Assays titrated 0.25–4 μM YARS1 against 2 μM F-actin. (ermanoska2023tyrosyltrnasynthetasehas pages 3-4)

An unbiased fly genetic screen identified **Fimbrin (Fim/CG8649)**, itself an actin-bundling factor, as a modifier of YARS1-E196K toxicity. Mutant YARS1 was associated with actin disorganization in fly nervous tissue, human neuroblastoma cells, and patient fibroblasts; genetic modulation of F-actin organization improved electrophysiological and morphological neuronal defects. This supports an evolutionarily conserved cytoskeletal function and a disease mechanism involving excessive or dysregulated actin organization. However, much of the in-vivo fly evidence used human YARS1 transgenes. Direct biochemical conservation strongly supports relevance to TyrRS proteins, but the quantitative physiological contribution of endogenous Q9VV60 to fly actin architecture remains to be established. (ermanoska2023tyrosyltrnasynthetasehas pages 1-2)

### 4.4 Nuclear transcriptional regulation

TyrRS can enter the nucleus, and CMT-associated conformational changes expose interaction surfaces that permit aberrant association with transcriptional regulators. In a *Drosophila* CMT model, mutant TyrRS altered E2F1-related signaling and a broader neuronal transcriptional network. Transcriptomic analysis identified **14 predicted transcription factors shared** between wild-type and E196K conditions and **39 additional E196K-specific factors**, associated with dendrite morphogenesis, neuronal development, and glucose metabolism. Manipulating E2F1/Dp alone did not rescue the fly phenotypes, indicating that the mechanism is broader than one transcription factor. (bervoets2019transcriptionaldysregulationby pages 5-6)

Genetic exclusion of mutant TyrRS from the nucleus prevented hallmark fly CMT phenotypes, while the nuclear-entry inhibitor embelin reduced neurotoxicity. This provides causal evidence for nuclear localization in the disease model. Nevertheless, these experiments chiefly concern transgenic human YARS1; they demonstrate a conserved cellular capability rather than proving that native Q9VV60 normally executes the same transcriptional program at endogenous abundance. (bervoets2019transcriptionaldysregulationby pages 1-2)

## 5. Applications and real-world implementations

### Disease modeling and variant interpretation

The principal application is modeling **YARS1-associated dominant-intermediate Charcot–Marie–Tooth neuropathy**. Human wild-type YARS1 complements dYARS depletion, and corresponding mutant fly and human proteins cause similar phenotypes, making *Drosophila* useful for testing pathogenicity and mechanism. Mutant expression produces dosage-dependent developmental lethality, progressive locomotor impairment, neuronal dysfunction, and terminal axonal degeneration; wild-type overexpression is comparatively benign. (storkebaum2009dominantmutationsin pages 2-2, storkebaum2009dominantmutationsin pages 4-5)

Useful quantitative benchmarks include:

* E196K increased climbing time by **65%**; in aged flies, **92% failed to fly** and **30% failed to jump**.
* Pan-neuronal E196K expression impaired motor performance by **74%**.
* G41R and Δ153–156VKQV produced flight-failure rates of **45% and 12%**, respectively.
* Presynaptic Δ153–156VKQV expression caused circuit defects in **38% of eight-day-old flies (n=16)**, while postsynaptic expression produced no detectable effect in the corresponding sample, localizing dysfunction primarily to the presynaptic neuron. (storkebaum2009dominantmutationsin pages 2-2, storkebaum2009dominantmutationsin pages 4-5)

Mutant human YARS1 also reduced new protein synthesis by approximately **50–80% in motor neurons** and **60–80% in class-IV multidendritic sensory neurons**. Since E196K remains catalytically competent and a 50% endogenous dYARS dosage reduction did not impair climbing, experts interpret these models as supporting toxic gain-of-function/neomorphic mechanisms, potentially combining translational inhibition, nuclear dysregulation, and altered actin organization rather than simple enzyme insufficiency. (storkebaum2009dominantmutationsin pages 2-2, morant2021drosophilamodelsfor pages 9-10, ermanoska2023tyrosyltrnasynthetasehas pages 1-2)

### Therapeutic-target discovery

The fly system has nominated several intervention points:

1. **Preventing pathological nuclear entry**, supported by genetic nuclear exclusion and embelin treatment.
2. **Normalizing F-actin organization**, which rescued neuronal electrophysiological and morphological defects.
3. **Restoring translational homeostasis**, although the exact causal chain for mutant YARS1 remains under active investigation.

These are preclinical disease-model applications, not established treatments. The endogenous extracellular EMAP pathway additionally offers a tractable system for studying macrophage recruitment and tissue surveillance, but no clinical implementation follows directly from the fly findings. (bervoets2019transcriptionaldysregulationby pages 1-2, ermanoska2023tyrosyltrnasynthetasehas pages 1-2)

## 6. Evidence hierarchy

The following table distinguishes direct endogenous-Q9VV60 evidence from findings obtained with transgenic human YARS1.

| Functional claim | Molecular/cellular location | Evidence type and experimental system | Key quantitative result | Confidence / limitation |
|---|---|---|---|---|
| TyrRS catalyzes ATP-dependent charging of tRNA^Tyr with L-tyrosine via tyrosyl-AMP, producing Tyr-tRNA^Tyr for translation. | Predominantly cytosolic translation machinery | Biochemical assays and cross-species complementation involving fly dYARS and human YARS1 (storkebaum2009dominantmutationsin pages 1-2, storkebaum2009dominantmutationsin pages 2-2) | Fly protein is 68% identical and 80% similar to human TyrRS; human WT YARS1 rescues a dYARS-RNAi bristle phenotype (storkebaum2009dominantmutationsin pages 2-2) | **High.** Canonical family function and functional orthology are well supported; detailed kinetic constants for purified Q9VV60 were not reported in the retrieved evidence. |
| Q9VV60/CG4561 is the cytosolic TyrRS, distinct from mitochondrial TyrRS-m. | Cytosol; not the mitochondrial matrix enzyme | Fly aaRS nomenclature analysis plus primary identification of endogenous CG4561; TyrRS and TyrRS-m are separate genes (lu2015theaminoacyltrnasynthetases pages 4-5, casastinto2015activejnkdependentsecretion pages 1-2) | One Drosophila gene encodes cytoplasmic TyrRS (storkebaum2009dominantmutationsin pages 2-2) | **High.** Identity is explicit; it must also not be confused with the unrelated *yar* lncRNA. |
| During cell competition, loser cells actively secrete TyrRS through a JNK- and Kish-dependent pathway; extracellular MMP cleavage yields MiniTyr and EMAP, and EMAP recruits haemocytes through PI3K-associated signaling. | Loser-cell cytoplasm → extracellular space; action on haemocytes | Endogenous fly CG4561 expression/localization, RNAi, tagged-protein immunoblotting, engineered secretion, and migration assays (casastinto2015activejnkdependentsecretion pages 1-2, casastinto2015activejnkdependentsecretion pages 10-11) | TyrRS expression peaks 24 h after clone induction; retrieved evidence gives no exact migration or secretion effect size (casastinto2015activejnkdependentsecretion pages 1-2) | **Moderate–high.** Strong fly-specific genetic evidence; haemocyte receptor is unknown, exact quantitative effect sizes were unavailable, and generality beyond cell competition is unresolved. |
| TyrRS can participate in nuclear transcriptional regulation; CMT mutants cause aberrant regulator interactions and broad neuronal transcriptional dysregulation. | Nucleus of fly neurons in CMT models | Primarily transgenic human YARS1 WT/E196K in flies, transcriptomics, genetic nuclear exclusion, and pharmacological inhibition with embelin (bervoets2019transcriptionaldysregulationby pages 5-6, bervoets2019transcriptionaldysregulationby pages 1-2) | 14 predicted transcription factors were shared by WT and E196K conditions; 39 additional factors were E196K-specific (bervoets2019transcriptionaldysregulationby pages 5-6) | **Moderate for endogenous Q9VV60; high for the disease model.** Nuclear exclusion suppresses CMT phenotypes, but most evidence concerns overexpressed human YARS1 rather than native fly TyrRS; manipulating E2F1 alone did not rescue disease. |
| TyrRS directly binds and bundles F-actin; E196K enhances bundling without materially changing measured binding affinity. | Cytoplasm and neuronal actin cytoskeleton | Purified YARS1 high-speed F-actin co-sedimentation and low-speed bundling assays, plus transgenic human YARS1 Drosophila genetics (ermanoska2023tyrosyltrnasynthetasehas pages 3-4, ermanoska2023tyrosyltrnasynthetasehas pages 1-2) | Apparent Kd: WT 0.75 μM; E196K 0.80 μM; assays titrated 0.25–4 μM YARS1 against 2 μM F-actin (ermanoska2023tyrosyltrnasynthetasehas pages 3-4) | **High for direct human YARS1–actin binding; moderate for native Q9VV60 physiology.** In-vivo fly work largely used human transgenes; retrieved evidence did not provide complete domain mapping or endogenous-protein measurements. |
| Dominant CMT-associated TyrRS variants cause dosage- and age-dependent, neuron-autonomous toxicity rather than simple haploinsufficiency. | Fly nervous system, including presynaptic axons and terminals | Transgenic human YARS1 and mutant fly dYARS expression; behavioral, electrophysiological, morphological, RNAi, and rescue assays (storkebaum2009dominantmutationsin pages 2-2, storkebaum2009dominantmutationsin pages 4-5) | E196K increased climbing time 65%; 92% of aged flies failed to fly and 30% failed to jump; pan-neuronal E196K impaired performance 74%. Presynaptic 153–156delVKQV caused defects in 38% of 8-day-old flies (n=16), whereas postsynaptic expression had no effect (storkebaum2009dominantmutationsin pages 2-2, storkebaum2009dominantmutationsin pages 4-5) | **High for model phenotypes.** A 50% reduction in endogenous dYARS dosage did not impair climbing, and catalytically active E196K remained toxic, supporting toxic gain of function; overexpression may not reproduce endogenous dosage. |
| CMT-mutant YARS1 suppresses neuronal protein synthesis independently of simple loss of aminoacylation. | Motor and multidendritic sensory neurons | Transgenic human YARS1 mutants in Drosophila; FUNCAT/BONCAT-type protein-synthesis measurements and aminoacylation comparisons (morant2021drosophilamodelsfor pages 9-10) | Translation decreased approximately 50–80% in motor neurons and 60–80% in class-IV sensory neurons (morant2021drosophilamodelsfor pages 9-10) | **Moderate–high for the disease model.** Variant-specific values and a corresponding endogenous-Q9VV60 assay were not supplied; impaired translation may coexist with nuclear and actin-mediated mechanisms. |


*Table: Evidence-ranked summary of canonical and noncanonical functions attributed to cytosolic Drosophila TyrRS, explicitly separating endogenous-fly evidence from transgenic human YARS1 disease-model results.*

## 7. Current interpretation and important limitations

The most defensible functional annotation is:

> **Q9VV60/CG4561 is the cytosolic, class-I tyrosyl-tRNA synthetase that specifically uses ATP and L-tyrosine to aminoacylate cytosolic tRNA^Tyr for translation. Under cell-competition conditions, endogenous fly TyrRS can be secreted and proteolytically converted into an EMAP chemoattractant that recruits haemocytes. TyrRS proteins also directly organize F-actin, while nuclear transcriptional effects are established mainly in human-YARS1 transgenic fly disease models.**

Several boundaries should be retained in database annotation:

* **Do not assign mitochondrial tyrosine charging to Q9VV60**; that belongs to TyrRS-m.
* **Do not conflate TyrRS with the *yar* lncRNA.**
* “Cytosolic” describes the canonical steady-state role, not exclusive localization: conditional extracellular and nuclear pools exist.
* The extracellular cell-competition function is directly demonstrated for endogenous CG4561 and can be annotated with relatively high confidence.
* Actin binding/bundling is biochemically strong and was reported in 2023, but the quantitative normal role of endogenous Q9VV60 in fly tissues needs endogenous tagging or allelic separation-of-function experiments.
* Nuclear transcriptional dysregulation, translational suppression, and most neuropathy phenotypes derive from overexpressed human YARS1 or engineered mutant dYARS. They are highly informative mechanistically but should not be recorded unqualified as basal native-Q9VV60 functions.
* No direct 2024 study substantially refining endogenous Q9VV60 function was identified in the retrieved literature. The latest high-impact target-relevant advance was the 2023 demonstration of F-actin bundling.

## Key references and publication dates

1. **Storkebaum et al.** “Dominant mutations in the tyrosyl-tRNA synthetase gene recapitulate in Drosophila features of human Charcot–Marie–Tooth neuropathy.” *PNAS* 106, 11782–11787. Published July 2009. https://doi.org/10.1073/pnas.0905339106. (storkebaum2009dominantmutationsin pages 1-2, storkebaum2009dominantmutationsin pages 2-2)
2. **Lu et al.** “The aminoacyl-tRNA synthetases of Drosophila melanogaster.” *Fly* 9, 53–61. Published April 2015. https://doi.org/10.1080/19336934.2015.1101196. (lu2015theaminoacyltrnasynthetases pages 4-5)
3. **Casas-Tintó et al.** “Active JNK-dependent secretion of Drosophila Tyrosyl-tRNA synthetase by loser cells recruits haemocytes during cell competition.” *Nature Communications* 6. Published December 2015. https://doi.org/10.1038/ncomms10022. (casastinto2015activejnkdependentsecretion pages 1-2, casastinto2015activejnkdependentsecretion pages 10-11)
4. **Bervoets et al.** “Transcriptional dysregulation by a nucleus-localized aminoacyl-tRNA synthetase associated with Charcot-Marie-Tooth neuropathy.” *Nature Communications* 10. Published November 2019. https://doi.org/10.1038/s41467-019-12909-9. (bervoets2019transcriptionaldysregulationby pages 5-6, bervoets2019transcriptionaldysregulationby pages 1-2)
5. **Morant et al.** “Drosophila Models for Charcot–Marie–Tooth Neuropathy Related to Aminoacyl-tRNA Synthetases.” *Genes* 12, 1519. Published September 2021. https://doi.org/10.3390/genes12101519. (morant2021drosophilamodelsfor pages 10-12, morant2021drosophilamodelsfor pages 9-10)
6. **Ermanoska et al.** “Tyrosyl-tRNA synthetase has a noncanonical function in actin bundling.” *Nature Communications* 14. Published March 2023. https://doi.org/10.1038/s41467-023-35908-3. (ermanoska2023tyrosyltrnasynthetasehas pages 3-4, ermanoska2023tyrosyltrnasynthetasehas pages 1-2)

References

1. (lu2015theaminoacyltrnasynthetases pages 4-5): Jiongming Lu, Steven J Marygold, Walid H Gharib, and Beat Suter. The aminoacyl-trna synthetases of drosophila melanogaster. Fly, 9:53-61, Apr 2015. URL: https://doi.org/10.1080/19336934.2015.1101196, doi:10.1080/19336934.2015.1101196. This article has 15 citations and is from a peer-reviewed journal.

2. (casastinto2015activejnkdependentsecretion pages 1-2): Sergio Casas-Tintó, Fidel-Nicolás Lolo, and Eduardo Moreno. Active jnk-dependent secretion of drosophila tyrosyl-trna synthetase by loser cells recruits haemocytes during cell competition. Nature Communications, Dec 2015. URL: https://doi.org/10.1038/ncomms10022, doi:10.1038/ncomms10022. This article has 54 citations and is from a highest quality peer-reviewed journal.

3. (storkebaum2009dominantmutationsin pages 1-2): Erik Storkebaum, Ricardo Leitão-Gonçalves, Tanja Godenschwege, Leslie Nangle, Monica Mejia, Inge Bosmans, Tinne Ooms, An Jacobs, Patrick Van Dijck, Xiang-Lei Yang, Paul Schimmel, Koen Norga, Vincent Timmerman, Patrick Callaerts, and Albena Jordanova. Dominant mutations in the tyrosyl-trna synthetase gene recapitulate in drosophila features of human charcot–marie–tooth neuropathy. Proceedings of the National Academy of Sciences, 106:11782-11787, Jul 2009. URL: https://doi.org/10.1073/pnas.0905339106, doi:10.1073/pnas.0905339106. This article has 147 citations and is from a highest quality peer-reviewed journal.

4. (bervoets2019transcriptionaldysregulationby pages 1-2): Sven Bervoets, Na Wei, Maria-Luise Erfurth, Shazie Yusein-Myashkova, Biljana Ermanoska, Ligia Mateiu, Bob Asselbergh, David Blocquel, Priyanka Kakad, Tyrone Penserga, Florian P Thomas, Velina Guergueltcheva, Ivailo Tournev, Tanja Godenschwege, Albena Jordanova, and Xiang-Lei Yang. Transcriptional dysregulation by a nucleus-localized aminoacyl-trna synthetase associated with charcot-marie-tooth neuropathy. Nature Communications, Nov 2019. URL: https://doi.org/10.1038/s41467-019-12909-9, doi:10.1038/s41467-019-12909-9. This article has 47 citations and is from a highest quality peer-reviewed journal.

5. (ermanoska2023tyrosyltrnasynthetasehas pages 3-4): Biljana Ermanoska, Bob Asselbergh, Laura Morant, Maria-Luise Petrovic-Erfurth, Seyyedmohsen Hosseinibarkooie, Ricardo Leitão-Gonçalves, Leonardo Almeida-Souza, Sven Bervoets, Litao Sun, LaTasha Lee, Derek Atkinson, Akram Khanghahi, Ivaylo Tournev, Patrick Callaerts, Patrik Verstreken, Xiang-Lei Yang, Brunhilde Wirth, Avital A. Rodal, Vincent Timmerman, Bruce L. Goode, Tanja A. Godenschwege, and Albena Jordanova. Tyrosyl-trna synthetase has a noncanonical function in actin bundling. Nature Communications, Mar 2023. URL: https://doi.org/10.1038/s41467-023-35908-3, doi:10.1038/s41467-023-35908-3. This article has 22 citations and is from a highest quality peer-reviewed journal.

6. (storkebaum2009dominantmutationsin pages 2-2): Erik Storkebaum, Ricardo Leitão-Gonçalves, Tanja Godenschwege, Leslie Nangle, Monica Mejia, Inge Bosmans, Tinne Ooms, An Jacobs, Patrick Van Dijck, Xiang-Lei Yang, Paul Schimmel, Koen Norga, Vincent Timmerman, Patrick Callaerts, and Albena Jordanova. Dominant mutations in the tyrosyl-trna synthetase gene recapitulate in drosophila features of human charcot–marie–tooth neuropathy. Proceedings of the National Academy of Sciences, 106:11782-11787, Jul 2009. URL: https://doi.org/10.1073/pnas.0905339106, doi:10.1073/pnas.0905339106. This article has 147 citations and is from a highest quality peer-reviewed journal.

7. (morant2021drosophilamodelsfor pages 9-10): Laura Morant, Maria-Luise Erfurth, and Albena Jordanova. Drosophila models for charcot–marie–tooth neuropathy related to aminoacyl-trna synthetases. Genes, 12:1519, Sep 2021. URL: https://doi.org/10.3390/genes12101519, doi:10.3390/genes12101519. This article has 10 citations.

8. (lu2015theaminoacyltrnasynthetases pages 3-4): Jiongming Lu, Steven J Marygold, Walid H Gharib, and Beat Suter. The aminoacyl-trna synthetases of drosophila melanogaster. Fly, 9:53-61, Apr 2015. URL: https://doi.org/10.1080/19336934.2015.1101196, doi:10.1080/19336934.2015.1101196. This article has 15 citations and is from a peer-reviewed journal.

9. (morant2021drosophilamodelsfor pages 10-12): Laura Morant, Maria-Luise Erfurth, and Albena Jordanova. Drosophila models for charcot–marie–tooth neuropathy related to aminoacyl-trna synthetases. Genes, 12:1519, Sep 2021. URL: https://doi.org/10.3390/genes12101519, doi:10.3390/genes12101519. This article has 10 citations.

10. (casastinto2015activejnkdependentsecretion pages 10-11): Sergio Casas-Tintó, Fidel-Nicolás Lolo, and Eduardo Moreno. Active jnk-dependent secretion of drosophila tyrosyl-trna synthetase by loser cells recruits haemocytes during cell competition. Nature Communications, Dec 2015. URL: https://doi.org/10.1038/ncomms10022, doi:10.1038/ncomms10022. This article has 54 citations and is from a highest quality peer-reviewed journal.

11. (ermanoska2023tyrosyltrnasynthetasehas pages 1-2): Biljana Ermanoska, Bob Asselbergh, Laura Morant, Maria-Luise Petrovic-Erfurth, Seyyedmohsen Hosseinibarkooie, Ricardo Leitão-Gonçalves, Leonardo Almeida-Souza, Sven Bervoets, Litao Sun, LaTasha Lee, Derek Atkinson, Akram Khanghahi, Ivaylo Tournev, Patrick Callaerts, Patrik Verstreken, Xiang-Lei Yang, Brunhilde Wirth, Avital A. Rodal, Vincent Timmerman, Bruce L. Goode, Tanja A. Godenschwege, and Albena Jordanova. Tyrosyl-trna synthetase has a noncanonical function in actin bundling. Nature Communications, Mar 2023. URL: https://doi.org/10.1038/s41467-023-35908-3, doi:10.1038/s41467-023-35908-3. This article has 22 citations and is from a highest quality peer-reviewed journal.

12. (bervoets2019transcriptionaldysregulationby pages 5-6): Sven Bervoets, Na Wei, Maria-Luise Erfurth, Shazie Yusein-Myashkova, Biljana Ermanoska, Ligia Mateiu, Bob Asselbergh, David Blocquel, Priyanka Kakad, Tyrone Penserga, Florian P Thomas, Velina Guergueltcheva, Ivailo Tournev, Tanja Godenschwege, Albena Jordanova, and Xiang-Lei Yang. Transcriptional dysregulation by a nucleus-localized aminoacyl-trna synthetase associated with charcot-marie-tooth neuropathy. Nature Communications, Nov 2019. URL: https://doi.org/10.1038/s41467-019-12909-9, doi:10.1038/s41467-019-12909-9. This article has 47 citations and is from a highest quality peer-reviewed journal.

13. (storkebaum2009dominantmutationsin pages 4-5): Erik Storkebaum, Ricardo Leitão-Gonçalves, Tanja Godenschwege, Leslie Nangle, Monica Mejia, Inge Bosmans, Tinne Ooms, An Jacobs, Patrick Van Dijck, Xiang-Lei Yang, Paul Schimmel, Koen Norga, Vincent Timmerman, Patrick Callaerts, and Albena Jordanova. Dominant mutations in the tyrosyl-trna synthetase gene recapitulate in drosophila features of human charcot–marie–tooth neuropathy. Proceedings of the National Academy of Sciences, 106:11782-11787, Jul 2009. URL: https://doi.org/10.1073/pnas.0905339106, doi:10.1073/pnas.0905339106. This article has 147 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](TyrRS-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. storkebaum2009dominantmutationsin pages 2-2
2. storkebaum2009dominantmutationsin pages 1-2
3. morant2021drosophilamodelsfor pages 9-10
4. morant2021drosophilamodelsfor pages 10-12
5. casastinto2015activejnkdependentsecretion pages 1-2
6. ermanoska2023tyrosyltrnasynthetasehas pages 3-4
7. ermanoska2023tyrosyltrnasynthetasehas pages 1-2
8. bervoets2019transcriptionaldysregulationby pages 5-6
9. bervoets2019transcriptionaldysregulationby pages 1-2
10. lu2015theaminoacyltrnasynthetases pages 4-5
11. lu2015theaminoacyltrnasynthetases pages 3-4
12. casastinto2015activejnkdependentsecretion pages 10-11
13. storkebaum2009dominantmutationsin pages 4-5
14. https://doi.org/10.1073/pnas.0905339106.
15. https://doi.org/10.1080/19336934.2015.1101196.
16. https://doi.org/10.1038/ncomms10022.
17. https://doi.org/10.1038/s41467-019-12909-9.
18. https://doi.org/10.3390/genes12101519.
19. https://doi.org/10.1038/s41467-023-35908-3.
20. https://doi.org/10.1080/19336934.2015.1101196,
21. https://doi.org/10.1038/ncomms10022,
22. https://doi.org/10.1073/pnas.0905339106,
23. https://doi.org/10.1038/s41467-019-12909-9,
24. https://doi.org/10.1038/s41467-023-35908-3,
25. https://doi.org/10.3390/genes12101519,