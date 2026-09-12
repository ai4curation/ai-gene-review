---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-11T21:33:24.758819'
end_time: '2026-06-11T21:42:16.956326'
duration_seconds: 532.2
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: pheA
  gene_symbol: pheA
  uniprot_accession: Q88M06
  protein_description: 'RecName: Full=Bifunctional chorismate mutase/prephenate dehydratase
    {ECO:0000256|ARBA:ARBA00014401}; EC=4.2.1.51 {ECO:0000256|ARBA:ARBA00013147};
    EC=5.4.99.5 {ECO:0000256|ARBA:ARBA00012404}; AltName: Full=Chorismate mutase-prephenate
    dehydratase {ECO:0000256|ARBA:ARBA00031520}; AltName: Full=p-protein {ECO:0000256|ARBA:ARBA00031175};'
  gene_info: Name=pheA {ECO:0000313|EMBL:AAN67389.1}; OrderedLocusNames=PP_1769 {ECO:0000313|EMBL:AAN67389.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: ACT-like_dom_sf. (IPR045865); ACT_dom. (IPR002912); Chor_mutase/pphenate_deHydtase.
    (IPR008242); Chorismate_II_sf. (IPR036263); CM_dom_sf. (IPR036979)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 19
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: pheA-deep-research-falcon_artifacts/artifact-00.md
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
- **UniProt Accession:** Q88M06
- **Protein Description:** RecName: Full=Bifunctional chorismate mutase/prephenate dehydratase {ECO:0000256|ARBA:ARBA00014401}; EC=4.2.1.51 {ECO:0000256|ARBA:ARBA00013147}; EC=5.4.99.5 {ECO:0000256|ARBA:ARBA00012404}; AltName: Full=Chorismate mutase-prephenate dehydratase {ECO:0000256|ARBA:ARBA00031520}; AltName: Full=p-protein {ECO:0000256|ARBA:ARBA00031175};
- **Gene Information:** Name=pheA {ECO:0000313|EMBL:AAN67389.1}; OrderedLocusNames=PP_1769 {ECO:0000313|EMBL:AAN67389.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** ACT-like_dom_sf. (IPR045865); ACT_dom. (IPR002912); Chor_mutase/pphenate_deHydtase. (IPR008242); Chorismate_II_sf. (IPR036263); CM_dom_sf. (IPR036979)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "pheA" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'pheA' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **pheA** (gene ID: pheA, UniProt: Q88M06) in PSEPK.

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
- **UniProt Accession:** Q88M06
- **Protein Description:** RecName: Full=Bifunctional chorismate mutase/prephenate dehydratase {ECO:0000256|ARBA:ARBA00014401}; EC=4.2.1.51 {ECO:0000256|ARBA:ARBA00013147}; EC=5.4.99.5 {ECO:0000256|ARBA:ARBA00012404}; AltName: Full=Chorismate mutase-prephenate dehydratase {ECO:0000256|ARBA:ARBA00031520}; AltName: Full=p-protein {ECO:0000256|ARBA:ARBA00031175};
- **Gene Information:** Name=pheA {ECO:0000313|EMBL:AAN67389.1}; OrderedLocusNames=PP_1769 {ECO:0000313|EMBL:AAN67389.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** ACT-like_dom_sf. (IPR045865); ACT_dom. (IPR002912); Chor_mutase/pphenate_deHydtase. (IPR008242); Chorismate_II_sf. (IPR036263); CM_dom_sf. (IPR036979)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "pheA" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'pheA' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **pheA** (gene ID: pheA, UniProt: Q88M06) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Research report: **pheA (PP_1769; UniProt Q88M06)** in *Pseudomonas putida* KT2440

### 0) Mandatory identity verification (disambiguation)
The target protein **UniProt Q88M06** corresponds to *Pseudomonas putida* strain KT2440 **PP_1769**, annotated as **pheA**, encoding a **bifunctional chorismate mutase/prephenate dehydratase** (often termed the bacterial “P-protein”). This assignment is supported by direct genetic-functional analysis in KT2440 showing that insertions in **PP_1769** confer **phenylalanine auxotrophy** and by operon mapping placing PP_1769 with other aromatic biosynthesis genes (molinahenares2009functionalanalysisof pages 6-7, molinahenares2009functionalanalysisof pages 1-2). This confirms that the gene symbol **pheA** matches the protein description provided (bifunctional CM/PDT enzyme).

---

### 1) Key concepts and definitions (current understanding)

#### 1.1 The chorismate node and aromatic amino-acid branching
In bacteria, **chorismate** is a central branch-point metabolite of the shikimate pathway. One major fate is conversion into **prephenate** via **chorismate mutase** activity; prephenate is then processed toward **phenylalanine** and **tyrosine** (dosselaere2001ametabolicnode pages 3-5). The importance of this “chorismate node” is that multiple pathways compete for chorismate, making enzymes such as PheA key control points for flux partitioning (dosselaere2001ametabolicnode pages 3-5).

#### 1.2 PheA (bifunctional chorismate mutase/prephenate dehydratase)
Bacterial **PheA** proteins are **two-domain (bifunctional)** enzymes that couple:
- **Chorismate mutase (CM; EC 5.4.99.5):** catalyzes **chorismate → prephenate** (a Claisen rearrangement) (dosselaere2001ametabolicnode pages 3-5).
- **Prephenate dehydratase (PDT; EC 4.2.1.51):** converts **prephenate → phenylpyruvate** (the keto-acid precursor of L-phenylalanine) (dosselaere2001ametabolicnode pages 3-5).

This functional definition is consistent with *Pseudomonas* KT2440 genetics: disrupting PP_1769 blocks phenylalanine biosynthesis (molinahenares2009functionalanalysisof pages 6-7, molinahenares2009functionalanalysisof pages 1-2).

#### 1.3 Regulatory concept: phenylalanine feedback inhibition (ACT-like regulatory region)
A central property of many bacterial PheA enzymes is **allosteric feedback inhibition by L-phenylalanine**. Authoritative biochemical dissection of model bacterial PheA shows a **separable C-terminal regulatory region** required for full phenylalanine-mediated inhibition; truncation abolishes feedback inhibition and alters substrate affinity (zhang1998chorismatemutaseprephenatedehydratase pages 5-6). Reviews of chorismate-utilizing enzymes similarly describe PheA as allosterically inhibited by phenylalanine with conformational/oligomeric effects (dosselaere2001ametabolicnode pages 3-5).

---

### 2) Gene/protein function in *Pseudomonas putida* KT2440 (primary evidence)

#### 2.1 Essential role in phenylalanine biosynthesis (mutant phenotypes)
A functional genetic analysis in *P. putida* KT2440 found multiple independent mini-Tn5 insertions in **PP_1769 (pheA)** (insertions reported at codons 6, 37, 42, and 120) that produced mutants whose growth was restored by **phenylalanine** supplementation but **not by tyrosine**, demonstrating **phenylalanine auxotrophy** and arguing against a tyrosine→phenylalanine bypass in this organism (molinahenares2009functionalanalysisof pages 6-7). This provides organism-specific evidence that PP_1769 is required for endogenous phenylalanine synthesis.

#### 2.2 Operon/genomic context: linkage to aromatic biosynthesis genes
In KT2440, **PP_1769 (pheA)** is tightly linked to aromatic biosynthesis genes: PP_1769 overlaps **serC** by 6 nucleotides and lies 61 nucleotides from **PP_1770**, and RT-PCR supports that **pheA forms an operon with serC and also with PP_1770 (tyrA; prephenate dehydrogenase)** (molinahenares2009functionalanalysisof pages 6-7). This genomic organization strengthens the functional inference that PP_1769 is part of the aromatic amino-acid biosynthetic module in KT2440.

---

### 3) Regulation and substrate specificity (evidence and inference)

#### 3.1 Catalytic specificity at the pathway level
The KT2440 mutant phenotypes demonstrate that disrupting pheA blocks phenylalanine synthesis upstream of phenylalanine formation (molinahenares2009functionalanalysisof pages 6-7). While the KT2440 papers retrieved here do not report purified-enzyme kinetics, authoritative biochemical studies of PheA family proteins show that PheA catalyzes the two-step CM/PDT route committing carbon toward **phenylpyruvate** (and thus L-phenylalanine) (dosselaere2001ametabolicnode pages 3-5, zhang1998chorismatemutaseprephenatedehydratase pages 3-5). 

#### 3.2 Feedback inhibition by aromatic amino acids (expert biochemical characterization)
Detailed biochemical domain studies of bacterial PheA show that phenylalanine is a strong inhibitor of the dehydratase activity and that the C-terminal regulatory region is required for full feedback control (zhang1998chorismatemutaseprephenatedehydratase pages 5-6, zhang1998chorismatemutaseprephenatedehydratase pages 3-5). A chorismate-node review further describes phenylalanine binding as causing conformational changes and shifts in oligomeric state linked to decreased activity (dosselaere2001ametabolicnode pages 3-5).

#### 3.3 Pseudomonas-specific recent evidence: engineering feedback-insensitive PheA to increase phenylalanine supply (2024)
A 2024 study in *Pseudomonas putida* DOT-T1E (a different *P. putida* strain, but the same enzyme class and pathway role) identified intracellular **L-phenylalanine** as a limiting substrate for **2-phenylethanol (2-PE)** production and introduced a chorismate mutase/prephenate dehydratase variant described as **insensitive to feedback inhibition by aromatic amino acids**. This intervention increased phenylalanine availability and improved 2-PE titers (godoy2024biosynthesisoffragrance pages 1-2). This provides recent, experimentally supported *Pseudomonas* evidence that PheA-like feedback control materially constrains flux toward phenylalanine-derived products.

---

### 4) Subcellular localization and site of action

#### 4.1 Most likely localization of KT2440 PheA
No direct subcellular localization experiment for **KT2440 PP_1769/PheA** was found in the retrieved full texts. However, the biochemical role of PheA is within core cytosolic metabolism (shikimate pathway branch), and bifunctional PheA enzymes in bacteria are typically treated as cytosolic enzymes acting on intracellular chorismate and prephenate pools (supported indirectly by the genetic/physiological phenotypes in KT2440) (molinahenares2009functionalanalysisof pages 6-7, molinahenares2009functionalanalysisof pages 1-2).

#### 4.2 Distinguishing from periplasmic chorismate mutases in *Pseudomonas*
Importantly, *Pseudomonas* can also encode **periplasm-localized monofunctional AroQ chorismate mutases** (“*AroQ”), shown experimentally in *Pseudomonas aeruginosa* as periplasmic proteins (calhoun2001theemergingperiplasmlocalized pages 1-2). These are **not** the same as the KT2440 PP_1769 bifunctional PheA (which is genetically tied to cytosolic aromatic biosynthesis genes and is required for phenylalanine prototrophy). This distinction reduces risk of misannotation when interpreting chorismate mutase activity in Pseudomonads (molinahenares2009functionalanalysisof pages 6-7, calhoun2001theemergingperiplasmlocalized pages 1-2).

---

### 5) Recent developments and latest research (emphasis on 2023–2024)

#### 5.1 2024: phenylalanine supply as a bottleneck for phenylalanine-derived aromatics in *Pseudomonas*
Godoy et al. (published **April 2024**) engineered *P. putida* DOT‑T1E strains for fragrance **2‑phenylethanol** production via the Ehrlich pathway and found phenylalanine supply limiting. Introducing a feedback-insensitive CM/PDT (PheA-class) enzyme increased phenylalanine and improved 2‑PE production, and further random mutagenesis increased titers (godoy2024biosynthesisoffragrance pages 1-2). URL: https://doi.org/10.1186/s13068-024-02498-1 (godoy2024biosynthesisoffragrance pages 1-2).

Although this is not KT2440 specifically, it is a close-strain *P. putida* demonstration aligning with the known regulatory role of PheA and is directly relevant for functional annotation in the *Pseudomonas* context (godoy2024biosynthesisoffragrance pages 1-2).

#### 5.2 2023 gap note
Within the retrieved corpus, no 2023 primary paper directly characterizing **KT2440 PP_1769/PheA biochemistry** (e.g., kinetics/structure) was obtained. Therefore, KT2440-specific “latest research” in 2023 cannot be asserted here beyond engineering/physiology already cited.

---

### 6) Current applications and real-world implementations

#### 6.1 Redirecting chorismate away from phenylalanine/tyrosine toward product formation (KT2440; PHBA)
A clear implementation in *P. putida* KT2440 is metabolic engineering for **para-hydroxybenzoic acid (PHBA)** production from glucose. In this strategy, **pheA was deleted** (along with other edits) specifically to remove competition for chorismate and redirect flux toward PHBA formation (yu2016metabolicengineeringof pages 1-3, yu2016metabolicengineeringof pages 5-6). In fed-batch fermentation, the best engineered strain achieved **1.73 g/L PHBA** and **18.1% carbon yield (C-mol/C-mol)** (yu2016metabolicengineeringof pages 5-6). URL: https://doi.org/10.3389/fbioe.2016.00090 (published **Nov 2016**) (yu2016metabolicengineeringof pages 5-6).

#### 6.2 Increasing phenylalanine-derived product formation by relieving feedback inhibition (Pseudomonas; 2-PE)
Conversely, when the product goal is phenylalanine-derived aromatics (e.g., **2‑phenylethanol**), engineering strategies can increase flux through PheA by relieving feedback control. In *P. putida* DOT-T1E, introduction of a feedback-insensitive CM/PDT enzyme increased 2‑PE production and enabled use of agricultural waste-derived sugar mixtures as substrates (godoy2024biosynthesisoffragrance pages 1-2).

---

### 7) Expert opinions and authoritative analysis (interpretation)

#### 7.1 Why pheA is a “high-leverage” annotation target
Reviews of chorismate-utilizing enzymes emphasize that the chorismate node is a heavily competed metabolic branchpoint, and that enzymes like PheA combine catalytic commitment with tight allosteric regulation by end products such as phenylalanine (dosselaere2001ametabolicnode pages 3-5). This explains why pheA deletions can strongly redirect chorismate to alternative products (e.g., PHBA) and why feedback-insensitive variants can boost phenylalanine supply for downstream synthesis (yu2016metabolicengineeringof pages 5-6, godoy2024biosynthesisoffragrance pages 1-2).

#### 7.2 Regulatory domain modularity
Biochemical domain dissection of PheA shows that the regulatory region is separable from catalytic fragments, and removal can abolish phenylalanine feedback inhibition (zhang1998chorismatemutaseprephenatedehydratase pages 5-6). This modularity underlies a common metabolic engineering tactic: creating or importing **feedback-resistant** variants to increase flux (as reflected in the 2024 *Pseudomonas* work) (godoy2024biosynthesisoffragrance pages 1-2, zhang1998chorismatemutaseprephenatedehydratase pages 5-6).

---

### 8) Relevant statistics and data points (from recent and key studies)

Key quantitative outcomes directly tied to manipulating the PheA node include:
- **PHBA production (KT2440)**: **1.73 g/L** maximum titer; **18.1% C-mol/C-mol carbon yield** in a non-optimized fed-batch fermentation; engineering included deletion of **pheA** to reduce chorismate consumption by aromatic amino-acid biosynthesis (yu2016metabolicengineeringof pages 5-6, yu2016metabolicengineeringof pages 1-3).
- **2-phenylethanol production (P. putida DOT-T1E; 2024)**: baseline production with glucose about **50–60 ppm**, increasing to about **100 ppm** after introducing a feedback-insensitive CM/PDT variant, and up to **120 ppm** after additional random mutagenesis (godoy2024biosynthesisoffragrance pages 1-2).

---

### 9) Consolidated functional-annotation summary (table)
The following table consolidates direct KT2440 evidence, family-level biochemical understanding, and application-level data.

| Gene/locus | Protein name | EC numbers | Domains | Primary reactions | Pathway role | Key experimental evidence in *P. putida* KT2440 | Evidence of regulation | Applications | Key quantitative data | Primary source (year, URL) |
|---|---|---|---|---|---|---|---|---|---|---|
| **pheA / PP_1769 / UniProt Q88M06** | Bifunctional chorismate mutase/prephenate dehydratase (“P-protein”) | **EC 5.4.99.5** (chorismate mutase); **EC 4.2.1.51** (prephenate dehydratase) | N-terminal chorismate mutase (CM) catalytic region; prephenate dehydratase (PDT) catalytic region; C-terminal ACT-like regulatory domain inferred from family/domain architecture and bacterial PheA literature | **Chorismate → prephenate** (CM step); **prephenate → phenylpyruvate + H2O + CO2** (PDT step), committing flux toward phenylalanine biosynthesis (dosselaere2001ametabolicnode pages 3-5, zhang1998chorismatemutaseprephenatedehydratase pages 3-5) | Branch-point enzyme at the chorismate node directing carbon from the shikimate pathway into the phenylalanine branch; competes with other chorismate-consuming pathways | Mini-Tn5 insertions in **PP_1769** caused **phenylalanine auxotrophy**; growth restored by phenylalanine but not tyrosine. RT-PCR showed **serC–pheA–PP1770/tyrA** operon linkage; PP_1769 overlaps **serC** by 6 nt and lies 61 nt from **PP1770**. Deletion of **pheA** in KT2440 was also used to redirect chorismate flux in engineering studies (molinahenares2009functionalanalysisof pages 6-7, molinahenares2009functionalanalysisof pages 1-2, yu2016metabolicengineeringof pages 5-6) | Canonical bacterial PheA enzymes are allosterically **feedback-inhibited by L-phenylalanine**, mediated by a separable C-terminal regulatory region/ACT-like domain; Phe strongly inhibits PDT activity and alters oligomerization in model bacterial PheA proteins (dosselaere2001ametabolicnode pages 3-5, zhang1998chorismatemutaseprephenatedehydratase pages 5-6, zhang1998chorismatemutaseprephenatedehydratase pages 3-5). In *Pseudomonas*, engineered **feedback-insensitive CM/PDT (PheA) variants** were introduced to raise intracellular phenylalanine and downstream product formation (godoy2024biosynthesisoffragrance pages 1-2) | **PHBA production:** deleting **pheA** in KT2440 removes competition for chorismate, improving precursor availability for para-hydroxybenzoic acid production. **2-Phenylethanol (2-PE):** relieving CM/PDT feedback inhibition increased phenylalanine supply and improved 2-PE production in *Pseudomonas* strains (yu2016metabolicengineeringof pages 5-6, yu2016metabolicengineeringof pages 1-3, godoy2024biosynthesisoffragrance pages 1-2) | PHBA in engineered KT2440 reached **1.73 g/L** maximum titer and **18.1% C-mol/C-mol** carbon yield in fed-batch; strategy included **pheA deletion** (yu2016metabolicengineeringof pages 5-6, yu2016metabolicengineeringof pages 1-3). In *Pseudomonas putida* DOT-T1E derivatives, introducing a feedback-insensitive CM/PDT increased 2-PE to about **100 ppm**, with random mutagenesis pushing titers to **120 ppm** (godoy2024biosynthesisoffragrance pages 1-2) | Molina-Henares et al., **2009**, https://doi.org/10.1111/j.1751-7915.2008.00062.x ; Yu et al., **2016**, https://doi.org/10.3389/fbioe.2016.00090 ; Godoy et al., **2024**, https://doi.org/10.1186/s13068-024-02498-1 |


*Table: This table summarizes verified functional annotation evidence for *Pseudomonas putida* KT2440 pheA/PP_1769 (UniProt Q88M06), including catalytic role, operon/genetic evidence, regulation, and engineering applications. It is useful for quickly separating direct KT2440 evidence from broader family-level regulatory inference.*

---

### 10) Evidence gaps and confidence statement
- **High confidence (KT2440-specific):** PP_1769 (pheA) is required for phenylalanine biosynthesis; disruption causes phenylalanine auxotrophy; gene is operon-linked with serC and tyrA-region genes (molinahenares2009functionalanalysisof pages 6-7, molinahenares2009functionalanalysisof pages 1-2).
- **High confidence (family-level biochemistry):** PheA catalyzes chorismate→prephenate and prephenate→phenylpyruvate and is feedback inhibited by phenylalanine via a separable regulatory region (dosselaere2001ametabolicnode pages 3-5, zhang1998chorismatemutaseprephenatedehydratase pages 5-6, zhang1998chorismatemutaseprephenatedehydratase pages 3-5).
- **Moderate confidence (KT2440 localization):** No KT2440-specific localization assay was retrieved; by pathway context it is most consistent with **cytosolic** function. Distinct periplasmic chorismate mutases exist in Pseudomonads but represent a different enzyme class (calhoun2001theemergingperiplasmlocalized pages 1-2).

---

### Key references (publication dates and URLs)
- Molina-Henares MA et al. **Dec 2009**. *Functional analysis of aromatic biosynthetic pathways in Pseudomonas putida KT2440*. Microbial Biotechnology. https://doi.org/10.1111/j.1751-7915.2008.00062.x (molinahenares2009functionalanalysisof pages 6-7)
- Yu S et al. **Nov 2016**. *Metabolic engineering of Pseudomonas putida KT2440 for the production of para-hydroxy benzoic acid*. Frontiers in Bioengineering and Biotechnology. https://doi.org/10.3389/fbioe.2016.00090 (yu2016metabolicengineeringof pages 5-6)
- Godoy P et al. **Apr 2024**. *Biosynthesis of fragrance 2-phenylethanol from sugars by Pseudomonas putida*. Biotechnology for Biofuels and Bioproducts. https://doi.org/10.1186/s13068-024-02498-1 (godoy2024biosynthesisoffragrance pages 1-2)
- Dosselaere F, Vanderleyden J. **Jan 2001**. *A metabolic node in action: chorismate-utilizing enzymes in microorganisms*. Critical Reviews in Microbiology. https://doi.org/10.1080/20014091096710 (dosselaere2001ametabolicnode pages 3-5)
- Calhoun DH et al. **Jul 2001**. *The emerging periplasm-localized subclass of AroQ chorismate mutases…*. Genome Biology. https://doi.org/10.1186/gb-2001-2-8-research0030 (calhoun2001theemergingperiplasmlocalized pages 1-2)
- Zhang S et al. **1998**. *Chorismate mutase-prephenate dehydratase from E. coli: study of catalytic and regulatory domains…* (domain/feedback analysis) (zhang1998chorismatemutaseprephenatedehydratase pages 5-6)

References

1. (molinahenares2009functionalanalysisof pages 6-7): M. A. Molina-Henares, Adela García‐Salamanca, A. Molina-Henares, J. de la Torre, M. C. Herrera, J. Ramos, and E. Duque. Functional analysis of aromatic biosynthetic pathways in pseudomonas putida kt2440. Microbial biotechnology, 2:91-100, Dec 2009. URL: https://doi.org/10.1111/j.1751-7915.2008.00062.x, doi:10.1111/j.1751-7915.2008.00062.x. This article has 32 citations and is from a peer-reviewed journal.

2. (molinahenares2009functionalanalysisof pages 1-2): M. A. Molina-Henares, Adela García‐Salamanca, A. Molina-Henares, J. de la Torre, M. C. Herrera, J. Ramos, and E. Duque. Functional analysis of aromatic biosynthetic pathways in pseudomonas putida kt2440. Microbial biotechnology, 2:91-100, Dec 2009. URL: https://doi.org/10.1111/j.1751-7915.2008.00062.x, doi:10.1111/j.1751-7915.2008.00062.x. This article has 32 citations and is from a peer-reviewed journal.

3. (dosselaere2001ametabolicnode pages 3-5): Filip Dosselaere and J. Vanderleyden. A metabolic node in action: chorismate-utilizing enzymes in microorganisms. Critical Reviews in Microbiology, 27:131-75, Jan 2001. URL: https://doi.org/10.1080/20014091096710, doi:10.1080/20014091096710. This article has 254 citations and is from a peer-reviewed journal.

4. (zhang1998chorismatemutaseprephenatedehydratase pages 5-6): S Zhang, G Pohnert, P Kongsaeree, and DB Wilson. Chorismate mutase-prephenate dehydratase from escherichia coli: study of catalytic and regulatory domains using genetically engineered proteins. Unknown journal, 1998.

5. (zhang1998chorismatemutaseprephenatedehydratase pages 3-5): S Zhang, G Pohnert, P Kongsaeree, and DB Wilson. Chorismate mutase-prephenate dehydratase from escherichia coli: study of catalytic and regulatory domains using genetically engineered proteins. Unknown journal, 1998.

6. (godoy2024biosynthesisoffragrance pages 1-2): Patricia Godoy, Zulema Udaondo, Estrella Duque, and Juan L. Ramos. Biosynthesis of fragrance 2-phenylethanol from sugars by pseudomonas putida. Biotechnology for Biofuels and Bioproducts, Apr 2024. URL: https://doi.org/10.1186/s13068-024-02498-1, doi:10.1186/s13068-024-02498-1. This article has 11 citations and is from a domain leading peer-reviewed journal.

7. (calhoun2001theemergingperiplasmlocalized pages 1-2): David H Calhoun, Carol A Bonner, Wei Gu, Gary Xie, and Roy A Jensen. The emerging periplasm-localized subclass of aroq chorismate mutases, exemplified by those from salmonella typhimurium and pseudomonas aeruginosa. Genome Biology, 2:research0030.1-research0030.16, Jul 2001. URL: https://doi.org/10.1186/gb-2001-2-8-research0030, doi:10.1186/gb-2001-2-8-research0030. This article has 75 citations and is from a highest quality peer-reviewed journal.

8. (yu2016metabolicengineeringof pages 1-3): Shiqin Yu, Manuel R. Plan, Gal Winter, and Jens O. Krömer. Metabolic engineering of pseudomonas putida kt2440 for the production of para-hydroxy benzoic acid. Frontiers in Bioengineering and Biotechnology, Nov 2016. URL: https://doi.org/10.3389/fbioe.2016.00090, doi:10.3389/fbioe.2016.00090. This article has 76 citations.

9. (yu2016metabolicengineeringof pages 5-6): Shiqin Yu, Manuel R. Plan, Gal Winter, and Jens O. Krömer. Metabolic engineering of pseudomonas putida kt2440 for the production of para-hydroxy benzoic acid. Frontiers in Bioengineering and Biotechnology, Nov 2016. URL: https://doi.org/10.3389/fbioe.2016.00090, doi:10.3389/fbioe.2016.00090. This article has 76 citations.

## Artifacts

- [Edison artifact artifact-00](pheA-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. dosselaere2001ametabolicnode pages 3-5
2. zhang1998chorismatemutaseprephenatedehydratase pages 5-6
3. molinahenares2009functionalanalysisof pages 6-7
4. godoy2024biosynthesisoffragrance pages 1-2
5. calhoun2001theemergingperiplasmlocalized pages 1-2
6. yu2016metabolicengineeringof pages 5-6
7. molinahenares2009functionalanalysisof pages 1-2
8. zhang1998chorismatemutaseprephenatedehydratase pages 3-5
9. yu2016metabolicengineeringof pages 1-3
10. https://doi.org/10.1186/s13068-024-02498-1
11. https://doi.org/10.3389/fbioe.2016.00090
12. https://doi.org/10.1111/j.1751-7915.2008.00062.x
13. https://doi.org/10.1080/20014091096710
14. https://doi.org/10.1186/gb-2001-2-8-research0030
15. https://doi.org/10.1111/j.1751-7915.2008.00062.x,
16. https://doi.org/10.1080/20014091096710,
17. https://doi.org/10.1186/s13068-024-02498-1,
18. https://doi.org/10.1186/gb-2001-2-8-research0030,
19. https://doi.org/10.3389/fbioe.2016.00090,