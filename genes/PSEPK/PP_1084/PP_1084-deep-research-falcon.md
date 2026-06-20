---
provider: falcon
model: Edison Scientific Literature
cached: true
start_time: '2026-06-02T23:56:18.705616'
end_time: '2026-06-02T23:56:18.706801'
duration_seconds: 0.0
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: PP_1084
  gene_symbol: tsaA
  uniprot_accession: Q88NW9
  protein_description: 'RecName: Full=Thioredoxin peroxidase {ECO:0000256|ARBA:ARBA00032824};'
  gene_info: Name=tsaA {ECO:0000313|EMBL:AAN66709.1}; OrderedLocusNames=PP_1084 {ECO:0000313|EMBL:AAN66709.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the peroxiredoxin family. AhpC/Prx1 subfamily.
  protein_domains: AhpC/TSA. (IPR000866); Peroxiredoxin. (IPR050217); Peroxiredoxin_AhpC-typ.
    (IPR024706); Peroxiredoxin_C. (IPR019479); Thioredoxin-like_sf. (IPR036249)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 24
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: PP_1084-deep-research-falcon_artifacts/artifact-00.md
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
- **UniProt Accession:** Q88NW9
- **Protein Description:** RecName: Full=Thioredoxin peroxidase {ECO:0000256|ARBA:ARBA00032824};
- **Gene Information:** Name=tsaA {ECO:0000313|EMBL:AAN66709.1}; OrderedLocusNames=PP_1084 {ECO:0000313|EMBL:AAN66709.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the peroxiredoxin family. AhpC/Prx1 subfamily.
- **Key Domains:** AhpC/TSA. (IPR000866); Peroxiredoxin. (IPR050217); Peroxiredoxin_AhpC-typ. (IPR024706); Peroxiredoxin_C. (IPR019479); Thioredoxin-like_sf. (IPR036249)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "tsaA" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'tsaA' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **tsaA** (gene ID: PP_1084, UniProt: Q88NW9) in PSEPK.

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
- **UniProt Accession:** Q88NW9
- **Protein Description:** RecName: Full=Thioredoxin peroxidase {ECO:0000256|ARBA:ARBA00032824};
- **Gene Information:** Name=tsaA {ECO:0000313|EMBL:AAN66709.1}; OrderedLocusNames=PP_1084 {ECO:0000313|EMBL:AAN66709.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the peroxiredoxin family. AhpC/Prx1 subfamily.
- **Key Domains:** AhpC/TSA. (IPR000866); Peroxiredoxin. (IPR050217); Peroxiredoxin_AhpC-typ. (IPR024706); Peroxiredoxin_C. (IPR019479); Thioredoxin-like_sf. (IPR036249)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "tsaA" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'tsaA' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **tsaA** (gene ID: PP_1084, UniProt: Q88NW9) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Comprehensive research report: **tsaA (PP_1084; UniProt Q88NW9)** in *Pseudomonas putida* KT2440

### 0) Executive summary (functional annotation)
*Pseudomonas putida* KT2440 locus **PP_1084** encodes a cytosolic **AhpC/Prx1-family (typical 2-Cys) peroxiredoxin**, experimentally characterized as a **thioredoxin-dependent peroxidase** that can also act as a **stress-responsive molecular chaperone** via oligomerization-dependent functional switching. The best-supported primary substrate in KT2440 experiments is **H2O2**, with broader substrate scope (e.g., organic hydroperoxides, peroxynitrite) supported by strong family-level evidence for typical 2-Cys peroxiredoxins. In KT2440, peroxide exposure promotes conversion of high-molecular-weight chaperone assemblies into low-molecular-weight forms with higher peroxidase activity, consistent with a redox-controlled homeostatic role in intracellular peroxide detoxification. (an2011functionalswitchingof pages 1-2, an2011functionalswitchingof pages 4-6, an2011functionalswitchingof pages 6-8, an2011functionalswitchingof pages 10-11)

### 1) Critical verification: gene/protein identity and context
#### 1.1 Verification against the user-supplied UniProt identity
The UniProt target (**Q88NW9**) is annotated as **Thioredoxin peroxidase**, gene name **tsaA**, ordered locus **PP_1084**, in *P. putida* KT2440, belonging to the **peroxiredoxin family (AhpC/Prx1 subfamily)**.

A KT2440-focused biochemical study directly investigated **PP1084** (noted as “PP1084 of *P. putida* KT2440”), identifying it as a **21 kDa AhpC/Tsa family peroxiredoxin** (typical 2-Cys), which aligns with the UniProt description and subfamily assignment. (an2011functionalswitchingof pages 1-2, an2011functionalswitchingof pages 4-6, an2011functionalswitchingof pages 6-8)

#### 1.2 Ambiguity check for “tsaA”
Within the retrieved literature, PP1084 is consistently discussed as an AhpC/Tsa-family peroxiredoxin from *P. putida* KT2440, and no conflicting “tsaA” assignments (to unrelated proteins or different organisms) were encountered in the evidence base assembled here. (an2011functionalswitchingof pages 1-2, an2011functionalswitchingof pages 4-6)

### 2) Key concepts and definitions (current understanding)
#### 2.1 What is a peroxiredoxin (Prx) and what does “AhpC/Prx1 subfamily” mean?
**Peroxiredoxins (Prxs)** are widespread thiol-dependent peroxidases that reduce peroxides using **redox-active cysteines**, protecting cells from oxidative stress and—depending on context—participating in redox regulation. In bacteria, AhpC-type Prxs are major peroxide-detoxifying enzymes and are often called **thioredoxin-dependent peroxidases**. (an2011functionalswitchingof pages 1-2, thapa2023theroleof pages 1-2)

The **AhpC/Prx1 (typical 2-Cys)** group is defined by a canonical two-cysteine catalytic cycle in which a **peroxidatic cysteine (CP)** forms a sulfenic acid intermediate and then resolves via a **resolving cysteine (CR)** to form a (typically **intersubunit**) disulfide bond. (sadowskabartosz2023peroxiredoxin2an pages 2-4, sadowskabartosz2023peroxiredoxin2an pages 8-10, thapa2023theroleof pages 2-4)

#### 2.2 Typical 2-Cys peroxiredoxin catalytic cycle (mechanistic definition)
Family-level (authoritative) synthesis describes the typical 2-Cys Prx mechanism as:
1) **CP-SH** reacts with peroxide (e.g., H2O2) → **CP-SOH** (sulfenic acid)
2) CP-SOH + CR-SH (often from the partner subunit) → **intersubunit disulfide**
3) The disulfide is reduced back to active thiols primarily by **thioredoxin (Trx)**, which is regenerated by **thioredoxin reductase (TrxR)** using **NADPH**.
This cycle is the central biochemical meaning of “thioredoxin peroxidase.” (sadowskabartosz2023peroxiredoxin2an pages 2-4, sadowskabartosz2023peroxiredoxin2an pages 8-10, thapa2023theroleof pages 2-4)

### 3) tsaA/PP_1084 product: molecular function, substrates, and mechanism
#### 3.1 Direct KT2440 experimental function: Trx-dependent peroxidase + chaperone
A KT2440 study (An et al., 2011; DOI https://doi.org/10.1007/s12192-010-0243-5; May 2011) characterized PP1084 (renamed **PpPrx**) as a **typical 2-Cys peroxiredoxin** that is **Trx-dependent** and shows **dual functionality**:
- **Peroxidase activity** detectable in a thioredoxin-coupled assay, with activity enriched in **low-molecular-weight (LMW)** forms. (an2011functionalswitchingof pages 6-8, an2011functionalswitchingof pages 10-11)
- **Chaperone activity** enriched in **high-molecular-weight (HMW)** oligomeric complexes, demonstrated by suppression of thermal aggregation of model substrates (e.g., malate dehydrogenase), consistent with a “holdase”-type stress chaperone function. (an2011functionalswitchingof pages 4-6, an2011functionalswitchingof pages 6-8)

#### 3.2 Substrate specificity
**Direct evidence in KT2440:** PP1084/PpPrx was assayed against **H2O2**, and H2O2 exposure is a central perturbation driving its structural/functional switching. (an2011functionalswitchingof pages 4-6, an2011functionalswitchingof pages 10-11, an2011functionalswitchingof pages 2-4)

**Family-supported substrate scope:** Typical 2-Cys peroxiredoxins (AhpC/Prx1-like) reduce **H2O2** and also **organic hydroperoxides (ROOH, including alkyl/lipid hydroperoxides)**; many also reduce **peroxynitrite**. This broader specificity is well supported in 2023 literature synthesizing peroxiredoxin chemistry and substrate range (even when the example protein is eukaryotic, the mechanistic and chemical principles apply to typical 2-Cys Prxs). (sadowskabartosz2023peroxiredoxin2an pages 2-4, sadowskabartosz2023peroxiredoxin2an pages 10-11, thapa2023theroleof pages 1-2, thapa2023theroleof pages 2-4)

**Important limitation:** In the retrieved KT2440 primary study excerpts, direct measurements of PP1084 activity toward *organic hydroperoxides* were not observed; thus, organic-hydroperoxide activity is currently best treated as a **high-confidence inference from subfamily membership**, rather than a KT2440-specific experimental fact in the evidence assembled here. (sadowskabartosz2023peroxiredoxin2an pages 2-4, thapa2023theroleof pages 1-2)

#### 3.3 Catalytic residues (evidence available)
For PP1084/PpPrx, sequence analysis reported **two highly conserved “VCP” tripeptides**, linked by the authors to catalytic function in typical 2-Cys peroxiredoxins, supporting the peroxiredoxin assignment and cysteine-based catalysis. (an2011functionalswitchingof pages 4-6, an2011functionalswitchingof pages 6-8)

**Important limitation:** The retrieved excerpts did not provide explicit residue numbers (e.g., “Cys47/Cys170”) for KT2440 PP1084; mechanistic residue positions are therefore presented as **typical-family features** rather than KT2440-specific numbering. (guevaraflores2024aphysiologicalapproach pages 1-2)

### 4) Biological processes, pathways, and cellular role in *P. putida* KT2440
#### 4.1 Oxidative stress defense and redox homeostasis
PP1084/PpPrx was discovered among **disulfide-bonded proteins** enriched after **oxidative treatments (H2O2, gamma rays)** in KT2440, consistent with involvement in oxidative-stress response and thiol redox homeostasis. (an2011functionalswitchingof pages 4-6, an2011functionalswitchingof pages 1-2)

#### 4.2 Oligomerization-linked functional switching (stress adaptation logic)
A key KT2440-specific mechanistic insight is that PP1084 undergoes stress-dependent transitions between:
- **HMW complexes** with strong **chaperone** activity, and
- **LMW species** with increased **peroxidase** activity.

Exposure to **H2O2** drives structural changes and a corresponding functional switch, and the thioredoxin system is described as a primary guide of this switching behavior. This supports a model in which PP1084 contributes both to (i) detoxification of peroxides and (ii) protection of other proteins from oxidative/heat stress via chaperone-like oligomeric assemblies. (an2011functionalswitchingof pages 1-2, an2011functionalswitchingof pages 6-8, an2011functionalswitchingof pages 10-11)

#### 4.3 Subcellular localization
PSORTb-based prediction placed PP1084/PpPrx in the **cytoplasm**, aligning with expected localization for a thioredoxin-coupled peroxide detox enzyme operating on intracellular peroxides and protein thiol redox balance. (an2011functionalswitchingof pages 4-6)

### 5) Recent developments (prioritizing 2023–2024 sources)
Because KT2440-specific publications in 2023–2024 mentioning PP_1084/tsaA directly were not retrieved here, “recent developments” are summarized as **state-of-the-art insights in typical 2-Cys peroxiredoxin biology** that sharpen functional interpretation of bacterial AhpC/Prx1 enzymes.

#### 5.1 Quantitative kinetic context (2023)
A 2023 synthesis reports that typical 2-Cys peroxiredoxins show high reactivity with H2O2, with second-order rate constants spanning approximately **10^5–10^8 M−1 s−1** (method-dependent), and describes competition between productive disulfide formation versus hyperoxidation using parameters around **kd ~2 s−1** and **kh ~1×10^4 M−1 s−1**. It also reports thioredoxin-based recycling parameters on the order of **~2.1×10^5 M−1 s−1** with **Km ~2–2.7 µM** for thioredoxin in a typical 2-Cys context. These quantitative ranges provide modern benchmarks for interpreting the efficiency and redox-control logic of bacterial AhpC/Prx1 enzymes such as KT2440 TsaA. (sadowskabartosz2023peroxiredoxin2an pages 8-10)

#### 5.2 Robustness vs hyperoxidation sensitivity motifs (2024)
A 2024 source highlights that many Prxs are sensitive to overoxidation under micromolar H2O2 and discusses motifs (e.g., “GGLG” and “YP”) associated with hyperoxidation sensitivity, while noting “robust” bacterial Prxs (e.g., *E. coli*, *Salmonella*) that lack those motifs and instead possess alternative motifs associated with resistance. It also frames how modest catalytic efficiencies (reported as **kcat/Km ~10^4–10^5 M−1 s−1** in that source) can still yield effective peroxide control if intracellular concentrations are high (cited typical Prx concentrations around **~15–60 µM**). This is relevant to functional annotation of KT2440 TsaA because it emphasizes that cellular abundance and recycling can be as important as intrinsic catalytic parameters. (guevaraflores2024aphysiologicalapproach pages 1-2)

#### 5.3 Omics-supported role of Ahp/Prx systems in oxidative stress during aromatic catabolism (2024)
A 2024 bioremediation-focused study in *Paraburkholderia xenovorans* reports that aromatic compound catabolism (hydroxyphenylacetates) induces oxidative stress and upregulates multiple peroxide detox enzymes including **Ahp components and peroxiredoxins** (e.g., AhpC2/AhpF/AhpD3, Prx1/Prx2, catalase). This supports a current applied research theme: successful aromatic degradation in soil-relevant bacteria requires active peroxide control programs, of which AhpC/Prx systems are prominent members. While not KT2440-specific, it supports the rationale that KT2440 peroxiredoxins likely contribute to its frequent use as an oxidative-stress-tolerant chassis for xenobiotic metabolism. (rodriguezcastro2024thelongchainflavodoxin pages 1-2, rodriguezcastro2024thelongchainflavodoxin pages 13-15)

### 6) Current applications and real-world implementations
#### 6.1 Direct KT2440 PP_1084/tsaA applications
Within the retrieved corpus, **no direct industrial or field deployment** specifically manipulating KT2440 **PP_1084/tsaA** was found. The best KT2440-specific contribution is mechanistic: PP1084 responds to peroxide stress and can act as a peroxide-reductase and chaperone—properties that are plausibly beneficial for industrial robustness, but this is not demonstrated here as an applied implementation. (an2011functionalswitchingof pages 4-6, an2011functionalswitchingof pages 1-2)

#### 6.2 Concrete bioremediation implementation involving oxidative-stress programs that include Ahp/Prx enzymes (2024)
Rodríguez-Castro et al. (Apr 2024; DOI https://doi.org/10.1186/s40659-024-00491-4) tested engineered redox protection in **soil microcosms**, showing improved biodegradation of an aromatic pollutant (4-HPA) by a strain overexpressing a protective flavodoxin. The study concurrently reports that antioxidant/peroxide-control systems including **Ahp/peroxiredoxin-related enzymes** are upregulated during aromatic catabolism. The microcosm result constitutes a real-world implementation relevant to peroxiredoxin-mediated oxidative defense: oxidative-stress detox capacity (including Ahp/Prx systems) is a key determinant of biodegradation performance and strain fitness in soil-like environments. (rodriguezcastro2024thelongchainflavodoxin pages 10-11, rodriguezcastro2024thelongchainflavodoxin pages 1-2)

### 7) Expert opinions and authoritative synthesis (what experts emphasize)
Recent authoritative syntheses emphasize the following themes relevant to bacterial AhpC/Prx1 (and thus to KT2440 TsaA):
1) **Peroxiredoxins are among the earliest and most sensitive peroxide defenses**, reacting rapidly with H2O2 via a specialized cysteine chemistry (peroxidatic cysteine) and being recycled mainly by thioredoxin systems. (sadowskabartosz2023peroxiredoxin2an pages 2-4, sadowskabartosz2023peroxiredoxin2an pages 8-10)
2) **Oligomerization can be functional**, linking redox state to peroxidase vs chaperone behavior; this is not purely an in vitro curiosity but a plausible stress-adaptation strategy. (thapa2023theroleof pages 1-2, an2011functionalswitchingof pages 10-11)
3) **Hyperoxidation and robustness** are important design/selection principles, especially in microbes experiencing recurring oxidative stress; sequence motifs and recycling capacity shape functional regimes. (guevaraflores2024aphysiologicalapproach pages 1-2, sadowskabartosz2023peroxiredoxin2an pages 2-4)

### 8) Relevant statistics and data (recent)
Key quantitative values from recent (2023–2024) sources relevant to interpreting KT2440 TsaA-type enzymes include:
- Typical 2-Cys Prx reaction with H2O2: **~10^5–10^8 M−1 s−1** (range across methods/contexts). (sadowskabartosz2023peroxiredoxin2an pages 8-10)
- Competition of disulfide formation vs hyperoxidation (example parameterization): **kd ~2 s−1**, **kh ~1×10^4 M−1 s−1**. (sadowskabartosz2023peroxiredoxin2an pages 8-10)
- Thioredoxin reduction parameters (example typical 2-Cys context): **~2.1×10^5 M−1 s−1**, **Km ~2–2.7 µM**. (sadowskabartosz2023peroxiredoxin2an pages 8-10)
- Typical intracellular Prx concentrations cited: **~15–60 µM**, supporting the idea that abundance can compensate for moderate kcat/Km in vivo. (guevaraflores2024aphysiologicalapproach pages 1-2)

**KT2440-specific quantitative limitation:** The KT2440 PP1084 study excerpts available here provide qualitative/relative activity statements (e.g., lower peroxidase activity relative to a yeast Prx control, higher chaperone activity) but do not provide a full kinetic parameter table in the extracted evidence; therefore, the numeric “statistics” above are best treated as **current family-level reference values**, not direct measurements of Q88NW9. (an2011functionalswitchingof pages 10-11, sadowskabartosz2023peroxiredoxin2an pages 8-10)

### 9) Evidence summary table
The following table links each major functional-annotation claim to its strongest supporting sources, with publication metadata.

| Item | Key finding | Organism context (KT2440 vs general) | Best supporting citation IDs | Publication info (authors, year, title, DOI/URL, month/year) |
|---|---|---|---|---|
| Identity | PP_1084 from *Pseudomonas putida* KT2440 is a 21 kDa AhpC/Tsa-family peroxiredoxin (typical 2-Cys Prx); this matches the UniProt Q88NW9 annotation as TsaA/thioredoxin peroxidase rather than an unrelated protein family. | KT2440-specific | (an2011functionalswitchingof pages 1-2, an2011functionalswitchingof pages 4-6, an2011functionalswitchingof pages 6-8) | An BC et al., 2011, *Functional switching of a novel prokaryotic 2-Cys peroxiredoxin (PpPrx) under oxidative stress*, Cell Stress and Chaperones, DOI: https://doi.org/10.1007/s12192-010-0243-5, May 2011 |
| Primary function | PP_1084/PpPrx is a thioredoxin-dependent peroxide-detoxifying enzyme with dual behavior: peroxidase activity plus stress-associated molecular chaperone activity. | KT2440-specific | (an2011functionalswitchingof pages 1-2, an2011functionalswitchingof pages 6-8, an2011functionalswitchingof pages 10-11) | An BC et al., 2011, *Functional switching of a novel prokaryotic 2-Cys peroxiredoxin (PpPrx) under oxidative stress*, https://doi.org/10.1007/s12192-010-0243-5, May 2011 |
| Mechanism | As an AhpC/Prx1 typical 2-Cys peroxiredoxin, the catalytic cycle is inferred to use a peroxidatic cysteine oxidized to sulfenic acid, then an intersubunit disulfide with a resolving cysteine, followed by thioredoxin-dependent reduction. | General AhpC/Prx1 mechanism, applied to PP_1084 family assignment | (sadowskabartosz2023peroxiredoxin2an pages 2-4, sadowskabartosz2023peroxiredoxin2an pages 8-10, guevaraflores2024aphysiologicalapproach pages 1-2, thapa2023theroleof pages 2-4) | Sadowska-Bartosz I & Bartosz G, 2023, *Peroxiredoxin 2: An Important Element of the Antioxidant Defense of the Erythrocyte*, https://doi.org/10.3390/antiox12051012, Apr 2023; Guevara-Flores A et al., 2024, *A Physiological Approach to Explore How Thioredoxin–Glutathione Reductase (TGR) and Peroxiredoxin (Prx) Eliminate H2O2 in Cysticerci of Taenia*, https://doi.org/10.3390/antiox13040444, Apr 2024; Thapa P et al., 2023, *The Role of Peroxiredoxins in Cancer Development*, https://doi.org/10.3390/biology12050666, Apr 2023 |
| Catalytic residue clues | Sequence analysis of PpPrx found two highly conserved VCP tripeptides associated with catalytic cysteines, supporting classification as a typical 2-Cys peroxiredoxin, although exact PP_1084 residue numbers were not given in the retrieved excerpts. | KT2440-specific sequence feature | (an2011functionalswitchingof pages 4-6, an2011functionalswitchingof pages 6-8) | An BC et al., 2011, *Functional switching of a novel prokaryotic 2-Cys peroxiredoxin (PpPrx) under oxidative stress*, https://doi.org/10.1007/s12192-010-0243-5, May 2011 |
| Substrates | Direct KT2440 evidence supports activity toward H2O2; by subfamily inference, AhpC/Prx1 enzymes also reduce organic hydroperoxides and can act on peroxynitrite. | H2O2: KT2440-specific; broader substrate range: general AhpC/Prx1 | (an2011functionalswitchingof pages 4-6, sadowskabartosz2023peroxiredoxin2an pages 2-4, sadowskabartosz2023peroxiredoxin2an pages 10-11, thapa2023theroleof pages 1-2, thapa2023theroleof pages 2-4) | An BC et al., 2011, *Functional switching of a novel prokaryotic 2-Cys peroxiredoxin (PpPrx) under oxidative stress*, https://doi.org/10.1007/s12192-010-0243-5, May 2011; Sadowska-Bartosz I & Bartosz G, 2023, *Peroxiredoxin 2...*, https://doi.org/10.3390/antiox12051012, Apr 2023; Thapa P et al., 2023, *The Role of Peroxiredoxins in Cancer Development*, https://doi.org/10.3390/biology12050666, Apr 2023 |
| Reductant / partner system | Peroxidase activity for PP_1084 was measured with a yeast thioredoxin system, and the authors conclude structural/functional switching is primarily guided by the thioredoxin system; this fits canonical Trx/TrxR/NADPH recycling of AhpC/Prx1 enzymes. | KT2440-specific experimental dependence plus general family mechanism | (an2011functionalswitchingof pages 1-2, an2011functionalswitchingof pages 6-8, an2011functionalswitchingof pages 10-11, sadowskabartosz2023peroxiredoxin2an pages 2-4, sadowskabartosz2023peroxiredoxin2an pages 8-10) | An BC et al., 2011, *Functional switching of a novel prokaryotic 2-Cys peroxiredoxin (PpPrx) under oxidative stress*, https://doi.org/10.1007/s12192-010-0243-5, May 2011; Sadowska-Bartosz I & Bartosz G, 2023, *Peroxiredoxin 2...*, https://doi.org/10.3390/antiox12051012, Apr 2023 |
| Oligomerization | PP_1084/PpPrx self-associates into high-molecular-weight (HMW) complexes and lower-molecular-weight (LMW) species; typical 2-Cys Prxs generally exist as dimers and larger toroid/decamer-like assemblies. | KT2440-specific plus general family context | (an2011functionalswitchingof pages 1-2, an2011functionalswitchingof pages 6-8, thapa2023theroleof pages 1-2) | An BC et al., 2011, *Functional switching of a novel prokaryotic 2-Cys peroxiredoxin (PpPrx) under oxidative stress*, https://doi.org/10.1007/s12192-010-0243-5, May 2011; Thapa P et al., 2023, *The Role of Peroxiredoxins in Cancer Development*, https://doi.org/10.3390/biology12050666, Apr 2023 |
| Chaperone role | In KT2440, HMW PP_1084 complexes have strong molecular chaperone activity, suppressing thermal aggregation of model substrates; oxidative conditions shift the balance toward LMW forms with greater peroxidase activity. | KT2440-specific | (an2011functionalswitchingof pages 4-6, an2011functionalswitchingof pages 6-8, an2011functionalswitchingof pages 10-11, an2011functionalswitchingof pages 1-2) | An BC et al., 2011, *Functional switching of a novel prokaryotic 2-Cys peroxiredoxin (PpPrx) under oxidative stress*, https://doi.org/10.1007/s12192-010-0243-5, May 2011 |
| Localization | PSORTb prediction places PP_1084/PpPrx in the cytoplasm, consistent with a role in intracellular peroxide detoxification and thioredoxin-linked redox homeostasis. | KT2440-specific prediction | (an2011functionalswitchingof pages 4-6) | An BC et al., 2011, *Functional switching of a novel prokaryotic 2-Cys peroxiredoxin (PpPrx) under oxidative stress*, https://doi.org/10.1007/s12192-010-0243-5, May 2011 |
| Biological process / pathway | The protein functions in oxidative-stress defense/redox homeostasis, especially detoxification of intracellular peroxides generated during stress; in KT2440 it was isolated among disulfide-bonded proteins after H2O2 or gamma-ray exposure. | KT2440-specific, with family-level redox-homeostasis context | (an2011functionalswitchingof pages 4-6, an2011functionalswitchingof pages 2-4, an2011functionalswitchingof pages 1-2) | An BC et al., 2011, *Functional switching of a novel prokaryotic 2-Cys peroxiredoxin (PpPrx) under oxidative stress*, https://doi.org/10.1007/s12192-010-0243-5, May 2011 |
| Activity level nuance | The recombinant KT2440 protein showed detectable but comparatively low H2O2 peroxidase activity versus a yeast thioredoxin peroxidase control, while exhibiting comparatively stronger chaperone activity. | KT2440-specific | (an2011functionalswitchingof pages 4-6, an2011functionalswitchingof pages 10-11) | An BC et al., 2011, *Functional switching of a novel prokaryotic 2-Cys peroxiredoxin (PpPrx) under oxidative stress*, https://doi.org/10.1007/s12192-010-0243-5, May 2011 |
| Recent kinetics/statistics | Recent reviews report typical 2-Cys Prx reaction rates with H2O2 in the ~10^5–10^8 M−1 s−1 range; competing condensation vs hyperoxidation parameters around kd ~2 s−1 and kh ~1×10^4 M−1 s−1; thioredoxin reduction second-order rate ~2.1×10^5 M−1 s−1 with Km ~2–2.7 µM; intracellular concentrations can be ~15–60 µM. These are family-level values, not KT2440-specific measurements. | General current understanding (2023–2024) | (sadowskabartosz2023peroxiredoxin2an pages 8-10, guevaraflores2024aphysiologicalapproach pages 1-2) | Sadowska-Bartosz I & Bartosz G, 2023, *Peroxiredoxin 2...*, https://doi.org/10.3390/antiox12051012, Apr 2023; Guevara-Flores A et al., 2024, *A Physiological Approach to Explore How Thioredoxin–Glutathione Reductase (TGR) and Peroxiredoxin (Prx) Eliminate H2O2 in Cysticerci of Taenia*, https://doi.org/10.3390/antiox13040444, Apr 2024 |
| Hyperoxidation / robustness context | Recent literature distinguishes hyperoxidation-sensitive versus robust typical 2-Cys Prxs by conserved motifs; bacterial AhpC-like enzymes are often more resistant to hyperoxidation than many eukaryotic homologs, supporting durable antioxidant function during repeated oxidative challenge. | General bacterial AhpC/Prx1 context | (sadowskabartosz2023peroxiredoxin2an pages 2-4, guevaraflores2024aphysiologicalapproach pages 1-2) | Sadowska-Bartosz I & Bartosz G, 2023, *Peroxiredoxin 2...*, https://doi.org/10.3390/antiox12051012, Apr 2023; Guevara-Flores A et al., 2024, *A Physiological Approach to Explore How Thioredoxin–Glutathione Reductase (TGR) and Peroxiredoxin (Prx) Eliminate H2O2 in Cysticerci of Taenia*, https://doi.org/10.3390/antiox13040444, Apr 2024 |
| Applications / implementations | No direct applied implementation of PP_1084 itself was found in the retrieved KT2440 literature. However, 2024 bioremediation work in another soil bacterium shows that oxidative-stress programs involving Ahp/peroxiredoxin enzymes are upregulated during aromatic-compound degradation and are relevant to strain robustness and soil-microcosm biodegradation performance; thus PP_1084 likely contributes to the oxidative-stress tolerance valued in *P. putida* as a biotechnological chassis. | KT2440 evidence indirect; application evidence from related bacteria/general Pseudomonas biotechnology context | (rodriguezcastro2024thelongchainflavodoxin pages 13-15, rodriguezcastro2024thelongchainflavodoxin pages 10-11, rodriguezcastro2024thelongchainflavodoxin pages 1-2, nies2022engineeringpseudomonasfora pages 171-174, nies2022engineeringpseudomonasfor pages 171-174) | Rodríguez-Castro L et al., 2024, *The long-chain flavodoxin FldX1 improves the biodegradation of 4-hydroxyphenylacetate and 3-hydroxyphenylacetate and counteracts the oxidative stress associated to aromatic catabolism in Paraburkholderia xenovorans*, https://doi.org/10.1186/s40659-024-00491-4, Apr 2024; Nies SC, 2022, *Engineering Pseudomonas for the production of reduced compounds*, journal/DOI not fully resolved in retrieved metadata, 2022 |


*Table: This table summarizes the main functional annotation evidence for Pseudomonas putida KT2440 tsaA/PP_1084 (UniProt Q88NW9), distinguishing direct KT2440 data from broader AhpC/Prx1 family inference. It is useful for tracing each annotation claim to specific supporting citations and recent mechanistic context.*

### 10) Recommended concise functional annotation statement (for databases)
**Gene/protein:** tsaA / PP_1084 (UniProt Q88NW9) — Thioredoxin peroxidase / typical 2-Cys peroxiredoxin (AhpC/Prx1 family)

**Molecular function:** Thioredoxin-dependent peroxidase reducing H2O2 (direct evidence) and likely organic hydroperoxides (subfamily inference); can form HMW oligomers with chaperone-like activity and LMW peroxidase-active forms; redox-dependent oligomerization mediates functional switching under oxidative stress. (an2011functionalswitchingof pages 4-6, an2011functionalswitchingof pages 6-8, an2011functionalswitchingof pages 10-11, sadowskabartosz2023peroxiredoxin2an pages 2-4, thapa2023theroleof pages 1-2)

**Cellular component:** Cytosol (prediction). (an2011functionalswitchingof pages 4-6)

**Biological process:** Oxidative stress response / peroxide detoxification; protein protection under oxidative/heat stress via chaperone-like assemblies. (an2011functionalswitchingof pages 4-6, an2011functionalswitchingof pages 1-2)

### References (URLs and publication dates)
- An BC et al. **May 2011**. *Functional switching of a novel prokaryotic 2-Cys peroxiredoxin (PpPrx) under oxidative stress*. **Cell Stress and Chaperones**. https://doi.org/10.1007/s12192-010-0243-5 (an2011functionalswitchingof pages 1-2)
- Sadowska-Bartosz I, Bartosz G. **Apr 2023**. *Peroxiredoxin 2: An Important Element of the Antioxidant Defense of the Erythrocyte*. **Antioxidants**. https://doi.org/10.3390/antiox12051012 (sadowskabartosz2023peroxiredoxin2an pages 8-10)
- Thapa P et al. **Apr 2023**. *The Role of Peroxiredoxins in Cancer Development*. **Biology (Basel)**. https://doi.org/10.3390/biology12050666 (thapa2023theroleof pages 1-2)
- Guevara-Flores A et al. **Apr 2024**. *A Physiological Approach to Explore How Thioredoxin–Glutathione Reductase (TGR) and Peroxiredoxin (Prx) Eliminate H2O2 in Cysticerci of Taenia*. **Antioxidants**. https://doi.org/10.3390/antiox13040444 (guevaraflores2024aphysiologicalapproach pages 1-2)
- Rodríguez-Castro L et al. **Apr 2024**. *The long-chain flavodoxin FldX1 improves the biodegradation of 4-hydroxyphenylacetate and 3-hydroxyphenylacetate and counteracts the oxidative stress associated to aromatic catabolism in Paraburkholderia xenovorans*. **Biological Research**. https://doi.org/10.1186/s40659-024-00491-4 (rodriguezcastro2024thelongchainflavodoxin pages 1-2)


References

1. (an2011functionalswitchingof pages 1-2): Byung Chull An, Seung Sik Lee, Eun Mi Lee, Jae Taek Lee, Seung Gon Wi, Hyun Suk Jung, Woojun Park, Sang Yeol Lee, and Byung Yeoup Chung. Functional switching of a novel prokaryotic 2-cys peroxiredoxin (ppprx) under oxidative stress. Cell Stress and Chaperones, 16:317-328, May 2011. URL: https://doi.org/10.1007/s12192-010-0243-5, doi:10.1007/s12192-010-0243-5. This article has 23 citations and is from a peer-reviewed journal.

2. (an2011functionalswitchingof pages 4-6): Byung Chull An, Seung Sik Lee, Eun Mi Lee, Jae Taek Lee, Seung Gon Wi, Hyun Suk Jung, Woojun Park, Sang Yeol Lee, and Byung Yeoup Chung. Functional switching of a novel prokaryotic 2-cys peroxiredoxin (ppprx) under oxidative stress. Cell Stress and Chaperones, 16:317-328, May 2011. URL: https://doi.org/10.1007/s12192-010-0243-5, doi:10.1007/s12192-010-0243-5. This article has 23 citations and is from a peer-reviewed journal.

3. (an2011functionalswitchingof pages 6-8): Byung Chull An, Seung Sik Lee, Eun Mi Lee, Jae Taek Lee, Seung Gon Wi, Hyun Suk Jung, Woojun Park, Sang Yeol Lee, and Byung Yeoup Chung. Functional switching of a novel prokaryotic 2-cys peroxiredoxin (ppprx) under oxidative stress. Cell Stress and Chaperones, 16:317-328, May 2011. URL: https://doi.org/10.1007/s12192-010-0243-5, doi:10.1007/s12192-010-0243-5. This article has 23 citations and is from a peer-reviewed journal.

4. (an2011functionalswitchingof pages 10-11): Byung Chull An, Seung Sik Lee, Eun Mi Lee, Jae Taek Lee, Seung Gon Wi, Hyun Suk Jung, Woojun Park, Sang Yeol Lee, and Byung Yeoup Chung. Functional switching of a novel prokaryotic 2-cys peroxiredoxin (ppprx) under oxidative stress. Cell Stress and Chaperones, 16:317-328, May 2011. URL: https://doi.org/10.1007/s12192-010-0243-5, doi:10.1007/s12192-010-0243-5. This article has 23 citations and is from a peer-reviewed journal.

5. (thapa2023theroleof pages 1-2): Pratik Thapa, Hong Jiang, Na Ding, Yanning Hao, Aziza Alshahrani, and Qiou Wei. The role of peroxiredoxins in cancer development. Biology, 12:666, Apr 2023. URL: https://doi.org/10.3390/biology12050666, doi:10.3390/biology12050666. This article has 26 citations.

6. (sadowskabartosz2023peroxiredoxin2an pages 2-4): Izabela Sadowska-Bartosz and Grzegorz Bartosz. Peroxiredoxin 2: an important element of the antioxidant defense of the erythrocyte. Antioxidants, 12:1012, Apr 2023. URL: https://doi.org/10.3390/antiox12051012, doi:10.3390/antiox12051012. This article has 48 citations.

7. (sadowskabartosz2023peroxiredoxin2an pages 8-10): Izabela Sadowska-Bartosz and Grzegorz Bartosz. Peroxiredoxin 2: an important element of the antioxidant defense of the erythrocyte. Antioxidants, 12:1012, Apr 2023. URL: https://doi.org/10.3390/antiox12051012, doi:10.3390/antiox12051012. This article has 48 citations.

8. (thapa2023theroleof pages 2-4): Pratik Thapa, Hong Jiang, Na Ding, Yanning Hao, Aziza Alshahrani, and Qiou Wei. The role of peroxiredoxins in cancer development. Biology, 12:666, Apr 2023. URL: https://doi.org/10.3390/biology12050666, doi:10.3390/biology12050666. This article has 26 citations.

9. (an2011functionalswitchingof pages 2-4): Byung Chull An, Seung Sik Lee, Eun Mi Lee, Jae Taek Lee, Seung Gon Wi, Hyun Suk Jung, Woojun Park, Sang Yeol Lee, and Byung Yeoup Chung. Functional switching of a novel prokaryotic 2-cys peroxiredoxin (ppprx) under oxidative stress. Cell Stress and Chaperones, 16:317-328, May 2011. URL: https://doi.org/10.1007/s12192-010-0243-5, doi:10.1007/s12192-010-0243-5. This article has 23 citations and is from a peer-reviewed journal.

10. (sadowskabartosz2023peroxiredoxin2an pages 10-11): Izabela Sadowska-Bartosz and Grzegorz Bartosz. Peroxiredoxin 2: an important element of the antioxidant defense of the erythrocyte. Antioxidants, 12:1012, Apr 2023. URL: https://doi.org/10.3390/antiox12051012, doi:10.3390/antiox12051012. This article has 48 citations.

11. (guevaraflores2024aphysiologicalapproach pages 1-2): Alberto Guevara-Flores, Gabriela Nava-Balderas, José de Jesús Martínez-González, César Vásquez-Lima, Juan Luis Rendón, and Irene Patricia del Arenal Mena. A physiological approach to explore how thioredoxin–glutathione reductase (tgr) and peroxiredoxin (prx) eliminate h2o2 in cysticerci of taenia. Antioxidants, 13:444, Apr 2024. URL: https://doi.org/10.3390/antiox13040444, doi:10.3390/antiox13040444. This article has 5 citations.

12. (rodriguezcastro2024thelongchainflavodoxin pages 1-2): Laura Rodríguez-Castro, Roberto E. Durán, Valentina Méndez, Flavia Dorochesi, Daniela Zühlke, Katharina Riedel, and Michael Seeger. The long-chain flavodoxin fldx1 improves the biodegradation of 4-hydroxyphenylacetate and 3-hydroxyphenylacetate and counteracts the oxidative stress associated to aromatic catabolism in paraburkholderia xenovorans. Biological Research, Apr 2024. URL: https://doi.org/10.1186/s40659-024-00491-4, doi:10.1186/s40659-024-00491-4. This article has 10 citations and is from a peer-reviewed journal.

13. (rodriguezcastro2024thelongchainflavodoxin pages 13-15): Laura Rodríguez-Castro, Roberto E. Durán, Valentina Méndez, Flavia Dorochesi, Daniela Zühlke, Katharina Riedel, and Michael Seeger. The long-chain flavodoxin fldx1 improves the biodegradation of 4-hydroxyphenylacetate and 3-hydroxyphenylacetate and counteracts the oxidative stress associated to aromatic catabolism in paraburkholderia xenovorans. Biological Research, Apr 2024. URL: https://doi.org/10.1186/s40659-024-00491-4, doi:10.1186/s40659-024-00491-4. This article has 10 citations and is from a peer-reviewed journal.

14. (rodriguezcastro2024thelongchainflavodoxin pages 10-11): Laura Rodríguez-Castro, Roberto E. Durán, Valentina Méndez, Flavia Dorochesi, Daniela Zühlke, Katharina Riedel, and Michael Seeger. The long-chain flavodoxin fldx1 improves the biodegradation of 4-hydroxyphenylacetate and 3-hydroxyphenylacetate and counteracts the oxidative stress associated to aromatic catabolism in paraburkholderia xenovorans. Biological Research, Apr 2024. URL: https://doi.org/10.1186/s40659-024-00491-4, doi:10.1186/s40659-024-00491-4. This article has 10 citations and is from a peer-reviewed journal.

15. (nies2022engineeringpseudomonasfora pages 171-174): SC Nies. Engineering pseudomonas for the production of reduced compounds. Unknown journal, 2022.

16. (nies2022engineeringpseudomonasfor pages 171-174): SC Nies. Engineering pseudomonas for the production of reduced compounds. Unknown journal, 2022.

## Artifacts

- [Edison artifact artifact-00](PP_1084-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. guevaraflores2024aphysiologicalapproach pages 1-2
2. an2011functionalswitchingof pages 4-6
3. an2011functionalswitchingof pages 1-2
4. thapa2023theroleof pages 1-2
5. rodriguezcastro2024thelongchainflavodoxin pages 1-2
6. an2011functionalswitchingof pages 6-8
7. an2011functionalswitchingof pages 10-11
8. thapa2023theroleof pages 2-4
9. an2011functionalswitchingof pages 2-4
10. rodriguezcastro2024thelongchainflavodoxin pages 13-15
11. rodriguezcastro2024thelongchainflavodoxin pages 10-11
12. nies2022engineeringpseudomonasfora pages 171-174
13. nies2022engineeringpseudomonasfor pages 171-174
14. https://doi.org/10.1007/s12192-010-0243-5;
15. https://doi.org/10.1186/s40659-024-00491-4
16. https://doi.org/10.1007/s12192-010-0243-5,
17. https://doi.org/10.3390/antiox12051012,
18. https://doi.org/10.3390/antiox13040444,
19. https://doi.org/10.3390/biology12050666,
20. https://doi.org/10.1186/s40659-024-00491-4,
21. https://doi.org/10.1007/s12192-010-0243-5
22. https://doi.org/10.3390/antiox12051012
23. https://doi.org/10.3390/biology12050666
24. https://doi.org/10.3390/antiox13040444