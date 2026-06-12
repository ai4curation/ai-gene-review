---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-12T01:59:36.607564'
end_time: '2026-06-12T02:20:15.955086'
duration_seconds: 1239.35
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: GET1
  gene_symbol: GET1
  uniprot_accession: O00258
  protein_description: 'RecName: Full=Guided entry of tail-anchored proteins factor
    1 {ECO:0000312|HGNC:HGNC:12790}; AltName: Full=Congenital heart disease 5 protein;
    AltName: Full=Tail-anchored protein insertion receptor WRB; AltName: Full=Tryptophan-rich
    basic protein;'
  gene_info: Name=GET1 {ECO:0000312|HGNC:HGNC:12790}; Synonyms=CHD5 {ECO:0000312|HGNC:HGNC:12790},
    WRB {ECO:0000312|HGNC:HGNC:12790};
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the WRB/GET1 family. .
  protein_domains: Get1. (IPR028945); Helix_hairpin_bin_sf. (IPR029012); CHD5 (PF04420)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 49
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 1
  edison_message_content: 1
artifacts:
- filename: artifact-00.md
  path: GET1-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: image-1.png
  path: GET1-deep-research-falcon_artifacts/image-1.png
  media_type: image/png
  source: edison_message_content
  data_storage_id: null
  description: '## Context ID: pqac-00000017 Table 2 provides the binding affinities
    (KD) of TRC40 and the TRC40-RAMP4 (TRC40-R4) complex to the WRB coiled-coil domain
    (WRBcc) '
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** O00258
- **Protein Description:** RecName: Full=Guided entry of tail-anchored proteins factor 1 {ECO:0000312|HGNC:HGNC:12790}; AltName: Full=Congenital heart disease 5 protein; AltName: Full=Tail-anchored protein insertion receptor WRB; AltName: Full=Tryptophan-rich basic protein;
- **Gene Information:** Name=GET1 {ECO:0000312|HGNC:HGNC:12790}; Synonyms=CHD5 {ECO:0000312|HGNC:HGNC:12790}, WRB {ECO:0000312|HGNC:HGNC:12790};
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the WRB/GET1 family. .
- **Key Domains:** Get1. (IPR028945); Helix_hairpin_bin_sf. (IPR029012); CHD5 (PF04420)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "GET1" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'GET1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **GET1** (gene ID: GET1, UniProt: O00258) in human.

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
- **UniProt Accession:** O00258
- **Protein Description:** RecName: Full=Guided entry of tail-anchored proteins factor 1 {ECO:0000312|HGNC:HGNC:12790}; AltName: Full=Congenital heart disease 5 protein; AltName: Full=Tail-anchored protein insertion receptor WRB; AltName: Full=Tryptophan-rich basic protein;
- **Gene Information:** Name=GET1 {ECO:0000312|HGNC:HGNC:12790}; Synonyms=CHD5 {ECO:0000312|HGNC:HGNC:12790}, WRB {ECO:0000312|HGNC:HGNC:12790};
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the WRB/GET1 family. .
- **Key Domains:** Get1. (IPR028945); Helix_hairpin_bin_sf. (IPR029012); CHD5 (PF04420)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "GET1" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'GET1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **GET1** (gene ID: GET1, UniProt: O00258) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Research Report: Human GET1 / WRB (UniProt O00258) — Functional Annotation and Current Understanding

## 0) Target verification (critical disambiguation)
The target in this report is **human GET1** as defined by UniProt accession **O00258**, which corresponds to **WRB (tryptophan-rich basic protein)**, historically also called **congenital heart disease 5 protein (CHD5)**, and is the mammalian functional homolog of yeast **Get1** in the **GET/TRC pathway** for tail-anchored (TA) protein insertion into the endoplasmic reticulum (ER). This identity is explicitly stated in the original WRB receptor-identification work, including the UniProt accession mapping and Get1 homology. (vilardi2011wrbisthe pages 1-2, vilardi2011wrbisthe pages 5-6)

## 1) Key concepts and definitions (current understanding)

### 1.1 Tail-anchored (TA) proteins
TA proteins are **single-pass membrane proteins** with a **C-terminal transmembrane domain (TMD)** that necessitates **post-translational** targeting/insertion (the TMD emerges only at translation termination). This is the client class handled by the GET/TRC pathway. (farkas2021captureanddelivery pages 1-3)

### 1.2 The mammalian GET/TRC pathway (overview)
A widely used model for mammals is:
1) Nascent TA proteins are initially captured by **SGTA** and the **BAG6 complex** (BAG6–TRC35–UBL4A). (farkas2021captureanddelivery pages 1-3)
2) TA substrates are transferred to the ATPase **TRC40** (also called **ASNA1**), which shields the hydrophobic TA TMD. (farkas2021captureanddelivery pages 1-3)
3) TRC40 delivers the substrate to the **ER-resident receptor/insertase** comprised of **WRB (GET1)** and **CAML**; receptor engagement drives conformational changes enabling insertion and TRC40 recycling. (farkas2021captureanddelivery pages 1-3, riveramonroy2016micelackingwrb pages 1-2)

### 1.3 What “GET1/WRB” is (functional definition)
WRB/GET1 is best described as an **ER membrane insertase receptor subunit**: it binds TRC40 and (together with CAML) forms the minimal machinery needed to accept TA substrates and catalyze their insertion into the ER bilayer. (vilardi2014wrbandcaml pages 1-2, mcdowell2020structuralbasisof pages 1-3)

## 2) GET1/WRB: protein properties, localization, and topology

### 2.1 ER localization
WRB is experimentally described as an **ER-resident membrane protein**; tagged WRB exhibits a reticular ER-like distribution and colocalizes with ER luminal markers (e.g., calreticulin). (vilardi2011wrbisthe pages 1-2)

### 2.2 Predicted topology and domains relevant to function
WRB is a small (~**19 kDa**) integral membrane protein with **three predicted transmembrane helices**, and a **cytosol-exposed coiled-coil domain** positioned between the first two TMDs (predicted by topology analysis; tested functionally). (vilardi2011wrbisthe pages 2-3, vilardi2011wrbisthe pages 3-5)

This coiled-coil region is the key TRC40-binding interface and is conserved with yeast Get1. (vilardi2011wrbisthe pages 3-5, vilardi2011wrbisthe pages 1-2)

## 3) Molecular function and mechanism (with evidence)

### 3.1 WRB is the TRC40 receptor; the coiled-coil is a TRC40 binding site
The foundational evidence for WRB’s receptor role is:
- **Physical interaction** between WRB and TRC40 (co-immunoprecipitation and recruitment assays). (vilardi2011wrbisthe pages 2-3, vilardi2011wrbisthe pages 1-2)
- A soluble WRB **coiled-coil fragment** binds TRC40 and **inhibits TRC40-dependent TA insertion**, demonstrating functional competition for receptor binding. (vilardi2011wrbisthe pages 2-3, vilardi2011wrbisthe pages 3-5)

Quantitatively, adding WRB coiled-coil at **10 µM** (reported as ~**100-fold molar excess**) reduced insertion of a TRC40-dependent TA substrate by **up to 92%**, while not affecting TRC40-independent insertion controls. (vilardi2011wrbisthe pages 3-5)

### 3.2 WRB and CAML form the functional mammalian GET receptor
In yeast complementation experiments lacking the endogenous GET receptor (get1/get2 deletion), co-expression of **human WRB + CAML**:
- Rescues growth phenotypes,
- Recruits Get3 (TRC40 homolog) to the ER,
- Restores TA targeting/insertion.

This supports the conclusion that **WRB and CAML are necessary and sufficient** to form a functional receptor complex for TRC40-mediated TA insertion. (vilardi2014wrbandcaml pages 1-2)

### 3.3 Quantitative binding and kinetic parameters (recently curated experimental data)
Vilardi et al. determined quantitative binding affinities for TRC40 interactions with receptor components:
- TRC40 binding to rough microsomes: **KD ~251 ± 65 nM**
- TRC40 binding to WRB coiled-coil domain: **KD ~392 ± 30 nM**
- TRC40 binding to CAML cytosolic domain: **KD ~85 ± 29 nM**
- TRC40–RAMP4 complex binding to CAML cytosolic domain: **KD ~34 ± 6 nM**

These values support a model in which the receptor’s cytosolic domains provide measurable, specific binding sites for TRC40 and TRC40–substrate complexes. (vilardi2014wrbandcaml pages 6-7, vilardi2014wrbandcaml media 82f0f8c3)

### 3.4 Structural mechanism: WRB/CAML as an Oxa1/YidC/EMC-like insertase
High-resolution structural biology has clarified how WRB/GET1 participates in insertion:

**2020 Molecular Cell (McDowell et al.)**
- Demonstrates that the membrane insertase is a **lipid-stabilized heterotetramer** (2:2 stoichiometry) formed upon Get3/TRC40 binding. (mcdowell2020structuralbasisof pages 3-4)
- Identifies a conserved **membrane-embedded hydrophilic groove** in the insertase, related to other insertases (YidC/EMC), consistent with a conserved insertion principle. (mcdowell2020structuralbasisof pages 1-3)
- Highlights a **Get2/CAML cytoplasmic helix** acting as a gate that interacts with Get3/TRC40 and contributes to insertion. (mcdowell2020structuralbasisof pages 1-3)

**2023 Nature Communications (McDowell et al.)**
- Provides structures/simulations including **human Get1/Get2/Get3**, showing the **hydrophilic groove** contacts TA substrates and that the **Get1/Get2 heterodimer** is sufficient for in vitro insertion. (mcdowell2023thegetinsertase pages 1-2)
- Reports **local membrane thinning** near the hydrophilic groove, interpreted as lowering the energetic barrier for insertion, i.e., the insertase actively remodels the bilayer. (mcdowell2023thegetinsertase pages 1-2, mcdowell2023thegetinsertase pages 9-10)
- Reveals **conformational plasticity** of the heterotetramer and gating interactions that likely coordinate substrate handoff and membrane integration. (mcdowell2023thegetinsertase pages 1-2, mcdowell2023thegetinsertase pages 9-10)

### 3.5 WRB’s additional mechanistic role: ensuring CAML topogenesis
Beyond client insertion, WRB is required for correct membrane integration/topology of its partner **CAML**:
- Without sufficient WRB, CAML forms aberrant topoforms, accumulates in ER clusters, and undergoes proteasome-mediated degradation.
- This supports a model where WRB acts in an **insertase/chaperone-like catalytic role** in membrane biogenesis. (carvalho2019thewrbsubunit pages 1-2)

This is consistent with quantitative observations that **CAML is often 4–7× more abundant than WRB**, and that WRB may not need to be stoichiometric with CAML to influence CAML’s productive membrane insertion. (carvalho2019thewrbsubunit pages 8-9)

## 4) Recent developments (prioritizing 2023–2024)

### 4.1 2023: Conformational plasticity and membrane thinning as a core mechanism
The 2023 structural/simulation work suggests a mechanistic framework where the insertase is not merely a static docking site, but dynamically remodels both protein conformation and the lipid environment (membrane thinning) to facilitate TA integration. (mcdowell2023thegetinsertase pages 1-2, mcdowell2023thegetinsertase pages 9-10)

### 4.2 2023: “Channel” concept in GET insertase function
A 2023 Cell Reports study reconstituted yeast Get1/2 and reported a **dynamic aqueous channel (~2.5 nm diameter)** that opens/closes and can be sealed by Get3 binding, supporting mechanistic ideas for how a GET receptor can insert a TMD while managing the C-terminal tail. Although performed in yeast, the study informs mechanistic hypotheses for the mammalian WRB/CAML system. (heo2023theget12insertase pages 1-3)

### 4.3 2023: Expert synthesis — TA targeting fidelity and surveillance
Recent review synthesis emphasizes that TA targeting includes not only delivery to ER receptors (WRB/CAML) but also surveillance mechanisms to resolve mis-targeting and enforce organelle specificity. This positions WRB/GET1 within a broader proteostasis network rather than an isolated insertion machine. (farkas2021captureanddelivery pages 5-7)

### 4.4 2024: Insertases as potential lipid scramblases (conceptual expansion)
A 2024 PNAS study argues that lipid scrambling may be a general feature of protein insertases, expanding the conceptual scope of insertase biology relevant to complexes such as GET/WRB-CAML. (mcdowell2023thegetinsertase pages 9-10)

## 5) Current applications and real-world implementations

### 5.1 Using WRB/CAML as a functional module to study ER membrane insertion
A practical, widely used real-world implementation is **reconstitution/complementation**:
- WRB + CAML can replace yeast Get1/Get2 to restore TA targeting/insertion in vivo, enabling genetic dissection of receptor features and domain swaps. (vilardi2014wrbandcaml pages 1-2)

### 5.2 Interpreting organ phenotypes via TA-client specificity
Tissue-specific WRB knockout in mice demonstrates a real-world implication: disruption of WRB does not uniformly collapse all TA proteins; instead, specific clients are highly vulnerable. For example, the SNARE **syntaxin 5 (Stx5)** is repeatedly identified as exceptionally sensitive to TRC40/WRB pathway disruption and is poorly rescued by alternative insertion pathways. (riveramonroy2016micelackingwrb pages 1-2, riveramonroy2016micelackingwrb pages 8-9)

### 5.3 Quantitative metrics for receptor interactions
The availability of **KD values** for TRC40 binding to WRB and CAML domains provides experimentally grounded parameters usable in mechanistic modeling and in vitro reconstitution design. (vilardi2014wrbandcaml media 82f0f8c3)

## 6) Expert opinions and authoritative analysis (evidence-based)

### 6.1 “Membrane insertase” framing
Recent authoritative reviews categorize WRB/GET1 (with CAML) as part of ER **membrane insertase systems**, related to Oxa1/YidC-type insertase families, integrating WRB into a unifying framework of membrane protein biogenesis. (farkas2021captureanddelivery pages 5-7, mcdowell2020structuralbasisof pages 3-4)

### 6.2 Proteostasis linkage
In vivo WRB loss studies emphasize that the TRC/GET pathway is not solely a targeting route; it is tightly linked to **proteostasis and quality control**, where stalled/misinserted clients can be routed to degradation pathways (including autophagy for certain clients like Stx5). (riveramonroy2016micelackingwrb pages 7-8)

## 7) Disease relevance: what is known, what remains uncertain

### 7.1 Why WRB is called “congenital heart disease 5 (CHD5)”
The designation reflects **positional mapping**, not a confirmed monogenic disease mechanism. WRB was historically called “congenital heart disease 5 protein” because the gene maps to **chromosome 21q22.3** within a Down syndrome (DS) region proposed to harbor gene(s) contributing to DS-associated congenital heart defects. (vilardi2011wrbisthe pages 5-6)

A key human-genetic statistic supporting a DS-CHD candidate region is the partial trisomy mapping study:
- Duplications including the candidate region: **8/14 (57%)** with CHD
- Duplications outside the region: **0/5 (0%)** with CHD

This supports a locus effect within the region but does not isolate WRB as the causal gene, and penetrance is incomplete. (barlow2001downsyndromecongenital pages 6-8, barlow2001downsyndromecongenital pages 5-6)

### 7.2 Down syndrome expression dosage
In Down syndrome fibroblasts, WRB is reported to be upregulated by the expected **~1.5×**, consistent with gene dosage from trisomy 21; CAML levels were not similarly increased, implying variable CAML:WRB ratios in human cells. (carvalho2019thewrbsubunit pages 8-9)

### 7.3 Functional evidence from model organisms and mice
Model organism perturbations reported in the WRB literature include cardiac and ocular phenotypes (medaka, Xenopus), supporting developmental sensitivity to WRB perturbation, while mouse tissue-specific WRB knockouts demonstrate severe, client-specific membrane biogenesis defects and organ pathology (e.g., liver injury with fibrosis and elevated transaminases; emerin mislocalization in ~50% cardiomyocytes). (riveramonroy2016micelackingwrb pages 1-2, riveramonroy2016micelackingwrb pages 3-4)

### 7.4 Current state of direct human disease association
Current evidence directly tying **human WRB variants** to congenital heart disease as a single-gene cause appears limited in the retrieved corpus. Consistent with this, Open Targets shows only a **low association score** for GET1/WRB with congenital heart disease and **no supporting evidence rows** in the retrieved context. (OpenTargets Search: congenital heart disease,cardiomyopathy,heart disease-WRB,GET1,CAML,TRC40)

## 8) Evidence-focused summary table
The following table consolidates the key functional-annotation claims with supporting citations, publication dates, and URLs.

| Category | Finding | Supporting citations | Key references |
|---|---|---|---|
| Identity | Human **GET1** in this context is **WRB** (tryptophan-rich basic protein; also called **CHD5**), corresponding to **UniProt O00258**, and is the mammalian homolog of yeast **Get1** in the GET/TRC tail-anchored protein targeting pathway. | (vilardi2011wrbisthe pages 1-2, vilardi2011wrbisthe pages 5-6) | Vilardi F et al. **2011-04**. *WRB is the receptor for TRC40/Asna1-mediated insertion of tail-anchored proteins into the ER membrane*. J Cell Sci. https://doi.org/10.1242/jcs.084277 |
| Localization/Topology | WRB is an **ER-resident integral membrane protein** with **three predicted transmembrane domains** and a **cytosol-exposed coiled-coil domain** between TMD1 and TMD2; tagged WRB shows an ER-like reticular pattern and colocalizes with calreticulin. | (vilardi2011wrbisthe pages 2-3, vilardi2011wrbisthe pages 3-5, vilardi2011wrbisthe pages 1-2) | Vilardi F et al. **2011-04**. J Cell Sci. https://doi.org/10.1242/jcs.084277 |
| Complex/Partners | WRB forms the **ER receptor/insertase complex with CAML** (functional mammalian counterpart of yeast Get1/Get2) and receives substrates from **TRC40/ASNA1**; upstream cytosolic handoff involves **BAG6, TRC35, and UBL4A**. | (farkas2021captureanddelivery pages 1-3, riveramonroy2016micelackingwrb pages 1-2, carvalho2019thewrbsubunit pages 1-2, vilardi2014wrbandcaml pages 1-2) | Farkas Á, Bohnsack KE. **2021-07**. *Capture and delivery of tail-anchored proteins to the endoplasmic reticulum*. J Cell Biol. https://doi.org/10.1083/jcb.202105004; Vilardi F et al. **2014-01**. PLoS One. https://doi.org/10.1371/journal.pone.0085033 |
| Molecular function | WRB is the **membrane receptor/insertase subunit** that enables **post-translational insertion of tail-anchored (TA) proteins** into the ER membrane after TRC40 delivery; together with CAML it is **necessary and sufficient** for functional receptor activity. | (vilardi2014wrbandcaml pages 1-2, vilardi2014wrbandcaml pages 2-3) | Vilardi F et al. **2014-01**. *WRB and CAML Are Necessary and Sufficient to Mediate Tail-Anchored Protein Targeting to the ER Membrane*. PLoS One. https://doi.org/10.1371/journal.pone.0085033 |
| Mechanism | The **WRB coiled-coil** binds TRC40 directly, competing with TA insertion when supplied as a soluble fragment; mechanistically, CAML first tethers TRC40/Get3 and WRB then contributes to substrate release and insertion through the membrane complex. | (vilardi2011wrbisthe pages 2-3, vilardi2011wrbisthe pages 3-5, vilardi2014wrbandcaml pages 1-2) | Vilardi F et al. **2011-04**. J Cell Sci. https://doi.org/10.1242/jcs.084277; Vilardi F et al. **2014-01**. PLoS One. https://doi.org/10.1371/journal.pone.0085033 |
| Mechanism | Structural work supports a **Get1/WRB–Get2/CAML hydrophilic groove** related to **YidC/EMC/Oxa1-type insertases**; Get3/TRC40 binding promotes formation of a **heterotetrameric insertase**, and lipid interactions help stabilize the active state. | (mcdowell2020structuralbasisof pages 1-3, farkas2021captureanddelivery pages 5-7, mcdowell2020structuralbasisof pages 3-4) | McDowell MA et al. **2020-10**. *Structural Basis of Tail-Anchored Membrane Protein Biogenesis by the GET Insertase Complex*. Mol Cell. https://doi.org/10.1016/j.molcel.2020.08.012 |
| Localization/Topology | WRB not only inserts TA clients but also helps **topogenesis of CAML itself**: without sufficient WRB, CAML adopts **aberrant topoforms**, clusters in the ER, and is degraded by the proteasome. | (carvalho2019thewrbsubunit pages 8-9, carvalho2019thewrbsubunit pages 1-2) | Carvalho HJF et al. **2019-08**. *The WRB Subunit of the Get3 Receptor is Required for the Correct Integration of its Partner CAML into the ER*. Sci Rep. https://doi.org/10.1038/s41598-019-48363-2 |
| Recent 2023-2024 developments | **2023 cryo-EM/simulation studies** showed that the GET insertase is **conformationally plastic** and causes **local membrane thinning** near the hydrophilic groove, likely lowering the energetic barrier for TA insertion. | (mcdowell2023thegetinsertase pages 1-2, mcdowell2023thegetinsertase pages 9-10) | McDowell MA et al. **2023-11**. *The GET insertase exhibits conformational plasticity and induces membrane thinning*. Nat Commun. https://doi.org/10.1038/s41467-023-42867-2 |
| Recent 2023-2024 developments | A **2023 Cell Reports** study on yeast Get1/2 found the insertase can form a **dynamic aqueous channel (~2.5 nm diameter)**, supporting a model in which GET receptors can insert the TMD and translocate short C-terminal tails; this is mechanistically informative for the mammalian WRB/CAML system. | (heo2023theget12insertase pages 1-3) | Heo P et al. **2023-01**. *The Get1/2 insertase forms a channel to mediate the insertion of tail-anchored proteins into the ER*. Cell Rep. https://doi.org/10.1016/j.celrep.2022.111921 |
| Recent 2023-2024 developments | Recent reviews place WRB/CAML among **ER membrane insertases** and emphasize TA-protein targeting fidelity plus surveillance/quality-control cross-talk with mitochondrial proofreading and ER quality-control pathways. | (mcdowell2023thegetinsertase pages 1-2, heo2023theget12insertase pages 1-3, farkas2021captureanddelivery pages 5-7) | Qin Q et al. **2023-01**. *Targeting and surveillance mechanisms for tail-anchored proteins*. The Innovation Life. https://doi.org/10.59717/j.xinn-life.2023.100013; Kizmaz B, Herrmann JM. **2023-07**. *Membrane insertases at a glance*. J Cell Sci. https://doi.org/10.1242/jcs.261219 |
| Recent 2023-2024 developments | A **2024 PNAS** analysis generalized the idea that **protein insertases can scramble lipids**, extending mechanistic thinking about insertases such as **WRB-CAML/GET** beyond peptide insertion alone. | (mcdowell2023thegetinsertase pages 1-2, mcdowell2023thegetinsertase pages 9-10) | Li D et al. **2024-04**. *Lipid scrambling is a general feature of protein insertases*. PNAS. https://doi.org/10.1073/pnas.2319476121 |
| Quantitative data | Biophysical binding data for the mammalian receptor show: **TRC40–rough microsomes KD ~251 ± 65 nM**; **TRC40–WRB coiled-coil KD ~392 ± 30 nM**; **TRC40–CAML cytosolic domain KD ~85 ± 29 nM**; **TRC40-RAMP4 complex–CAML cytosolic domain KD ~34 ± 6 nM**. | (vilardi2014wrbandcaml pages 6-7, vilardi2014wrbandcaml media 82f0f8c3) | Vilardi F et al. **2014-01**. PLoS One. https://doi.org/10.1371/journal.pone.0085033 |
| Quantitative data | Soluble WRB coiled-coil inhibits TRC40-dependent TA insertion in vitro; at **10 µM WRBcc** (a **100-fold molar excess**), glycosylated inserted substrate was reduced by **up to 92%**. | (vilardi2011wrbisthe pages 3-5) | Vilardi F et al. **2011-04**. J Cell Sci. https://doi.org/10.1242/jcs.084277 |
| Quantitative data | WRB and CAML are not present at equal abundance in cells: **CAML is ~4–7-fold more abundant than WRB**, and WRB was reported to be **~1.5× upregulated in Down syndrome fibroblasts** without changing CAML levels. | (carvalho2019thewrbsubunit pages 8-9) | Carvalho HJF et al. **2019-08**. Sci Rep. https://doi.org/10.1038/s41598-019-48363-2 |
| In vivo phenotypes/applications | Tissue-specific **WRB knockout mice** revealed that TA-protein dependence on the pathway is **client-specific**: **syntaxin 5 (Stx5)** is especially sensitive, while **Sec61β** and **Stx8** can be relatively unaffected. | (riveramonroy2016micelackingwrb pages 1-2, riveramonroy2016micelackingwrb pages 2-3, riveramonroy2016micelackingwrb pages 4-5, riveramonroy2016micelackingwrb pages 3-4) | Rivera-Monroy J et al. **2016-12**. *Mice lacking WRB reveal differential biogenesis requirements of tail-anchored proteins in vivo*. Sci Rep. https://doi.org/10.1038/srep39464 |
| In vivo phenotypes/applications | In cardiomyocyte-specific WRB knockout, **TRC40 and CAML protein levels fell significantly** and some TA clients were reduced; in hepatocytes, only animals with **70–90% WRB mRNA loss** showed significantly reduced WRB/CAML protein, indicating a **threshold effect**. | (riveramonroy2016micelackingwrb pages 2-3, riveramonroy2016micelackingwrb pages 3-4) | Rivera-Monroy J et al. **2016-12**. Sci Rep. https://doi.org/10.1038/srep39464 |
| In vivo phenotypes/applications | Approximately **50% of cardiomyocytes** showed reduced/mislocalized **emerin** after WRB loss, and Cre-positive hepatocytes developed severe liver injury with fibrosis and elevated ALT/AST, underscoring the pathway’s physiological relevance for organ proteostasis. | (riveramonroy2016micelackingwrb pages 4-5, riveramonroy2016micelackingwrb pages 3-4) | Rivera-Monroy J et al. **2016-12**. Sci Rep. https://doi.org/10.1038/srep39464 |
| In vivo phenotypes/applications | WRB-dependent TA insertion is physiologically important in the auditory system: WRB is required for proper insertion of **otoferlin**, and WRB deficiency disrupts **hair-cell exocytosis and hearing**. | (riveramonroy2016micelackingwrb pages 8-9) | Vogl C et al. **2016-12**. *Tryptophan-rich basic protein (WRB) mediates insertion of the tail-anchored protein otoferlin and is required for hair cell exocytosis and hearing*. EMBO J. https://doi.org/10.15252/embj.201593565 |
| Disease/clinical relevance | The alternative name **“congenital heart disease 5” (CHD5)** reflects historical positional/candidate-gene annotation: WRB maps to **chromosome 21q22.3 / Down syndrome region-2**, a region implicated in congenital heart disease, but current literature more strongly supports a **membrane protein biogenesis** role than a directly established monogenic CHD mechanism. | (vilardi2011wrbisthe pages 5-6, riveramonroy2016micelackingwrb pages 1-2) | Barlow GM et al. **2001-03**. *Down syndrome congenital heart disease: A narrowed region and a candidate gene*. Genet Med. https://doi.org/10.1097/00125817-200103000-00002; Vilardi F et al. **2011-04**. J Cell Sci. https://doi.org/10.1242/jcs.084277 |
| Disease/clinical relevance | Open Targets shows only a **weak congenital heart disease association score (0.0138)** for GET1/WRB and **no supporting evidence rows**, indicating that direct clinical evidence remains limited at present. | (OpenTargets Search: congenital heart disease,cardiomyopathy,heart disease-WRB,GET1,CAML,TRC40) | Open Targets platform context for GET1 and congenital heart disease (context retrieval) |
| Disease/clinical relevance | The broader **TRC/GET pathway** has clear disease relevance even when direct WRB human genetics are sparse: **ASNA1/TRC40** biallelic variants cause rapidly progressive pediatric cardiomyopathy, reinforcing the importance of this pathway in human tissue function. | (farkas2021captureanddelivery pages 1-3) | Verhagen JMA et al. **2019-09**. *Biallelic Variants in ASNA1... Cause Rapidly Progressive Pediatric Cardiomyopathy*. Circ Genom Precis Med. https://doi.org/10.1161/CIRCGEN.119.002507 |
| Key references | Most authoritative primary sources for functional annotation are the **2011 receptor-identification paper**, the **2014 WRB/CAML sufficiency paper**, the **2020 structural paper**, and the **2023 conformational plasticity paper**. | (mcdowell2020structuralbasisof pages 1-3, vilardi2014wrbandcaml pages 1-2, mcdowell2023thegetinsertase pages 1-2, mcdowell2020structuralbasisof pages 3-4) | Vilardi F et al. **2011-04**. https://doi.org/10.1242/jcs.084277; Vilardi F et al. **2014-01**. https://doi.org/10.1371/journal.pone.0085033; McDowell MA et al. **2020-10**. https://doi.org/10.1016/j.molcel.2020.08.012; McDowell MA et al. **2023-11**. https://doi.org/10.1038/s41467-023-42867-2 |


*Table: This table summarizes the current functional annotation of human GET1/WRB (UniProt O00258), including identity, localization, molecular mechanism, recent structural advances, quantitative data, physiological phenotypes, and clinical relevance. It is designed as a compact evidence map with direct citation IDs and key source metadata.*

## 9) Key quantitative/statistical highlights (from cited evidence)
- TRC40 binding affinities (KD) to receptor components are in the **tens-to-hundreds of nM** range, including **TRC40–WRB coiled-coil KD ~392 ± 30 nM** and **TRC40–CAMLcyt KD ~85 ± 29 nM**. (vilardi2014wrbandcaml media 82f0f8c3)
- Soluble WRB coiled-coil inhibits TRC40-dependent insertion with **up to 92% inhibition** at **10 µM** WRBcc (~100-fold molar excess). (vilardi2011wrbisthe pages 3-5)
- Down syndrome partial trisomy mapping indicates a DS-CHD candidate region with **57% (8/14)** CHD penetrance when duplicated versus **0% (0/5)** when duplications fall outside the region. (barlow2001downsyndromecongenital pages 6-8)
- In WRB tissue-specific knockout, **emerin** mislocalization/reduction is observed in **~50% of cardiomyocytes** (reported proportion). (riveramonroy2016micelackingwrb pages 4-5)

## 10) Conclusions (functional annotation)
Human **GET1/WRB (UniProt O00258)** is best annotated as an **ER membrane insertase receptor subunit** of the **GET/TRC pathway**. Its primary molecular function is to cooperate with **CAML** to accept **TRC40/ASNA1-bound tail-anchored proteins**, promote their release from TRC40, and enable **C-terminal TMD insertion** into the ER membrane via a conserved **hydrophilic groove** architecture related to Oxa1/YidC/EMC insertases. (vilardi2014wrbandcaml pages 1-2, mcdowell2023thegetinsertase pages 1-2, mcdowell2020structuralbasisof pages 3-4)

Recent 2023–2024 developments strengthen a dynamic mechanistic picture: the insertase is conformationally flexible and can remodel the bilayer (membrane thinning), reinforcing the view that WRB-containing complexes are active catalysts of membrane protein integration rather than passive receptors. (mcdowell2023thegetinsertase pages 1-2, mcdowell2023thegetinsertase pages 9-10)

The “CHD5” naming reflects genomic mapping within a Down syndrome CHD candidate region; while regional genotype–phenotype statistics support a locus effect, direct causality of WRB in human congenital heart disease remains uncertain in the currently retrieved evidence, and current curated resources indicate weak direct association. (barlow2001downsyndromecongenital pages 6-8, riveramonroy2016micelackingwrb pages 1-2, OpenTargets Search: congenital heart disease,cardiomyopathy,heart disease-WRB,GET1,CAML,TRC40)


References

1. (vilardi2011wrbisthe pages 1-2): Fabio Vilardi, Holger Lorenz, and Bernhard Dobberstein. Wrb is the receptor for trc40/asna1-mediated insertion of tail-anchored proteins into the er membrane. Journal of Cell Science, 124:1301-1307, Apr 2011. URL: https://doi.org/10.1242/jcs.084277, doi:10.1242/jcs.084277. This article has 154 citations and is from a domain leading peer-reviewed journal.

2. (vilardi2011wrbisthe pages 5-6): Fabio Vilardi, Holger Lorenz, and Bernhard Dobberstein. Wrb is the receptor for trc40/asna1-mediated insertion of tail-anchored proteins into the er membrane. Journal of Cell Science, 124:1301-1307, Apr 2011. URL: https://doi.org/10.1242/jcs.084277, doi:10.1242/jcs.084277. This article has 154 citations and is from a domain leading peer-reviewed journal.

3. (farkas2021captureanddelivery pages 1-3): Ákos Farkas and Katherine E. Bohnsack. Capture and delivery of tail-anchored proteins to the endoplasmic reticulum. The Journal of Cell Biology, Jul 2021. URL: https://doi.org/10.1083/jcb.202105004, doi:10.1083/jcb.202105004. This article has 49 citations.

4. (riveramonroy2016micelackingwrb pages 1-2): Jhon Rivera-Monroy, Lena Musiol, Kirsten Unthan-Fechner, Ákos Farkas, Anne Clancy, Javier Coy-Vergara, Uri Weill, Sarah Gockel, Shuh-Yow Lin, David P. Corey, Tobias Kohl, Philipp Ströbel, Maya Schuldiner, Blanche Schwappach, and Fabio Vilardi. Mice lacking wrb reveal differential biogenesis requirements of tail-anchored proteins in vivo. Scientific Reports, Dec 2016. URL: https://doi.org/10.1038/srep39464, doi:10.1038/srep39464. This article has 50 citations and is from a peer-reviewed journal.

5. (vilardi2014wrbandcaml pages 1-2): Fabio Vilardi, Milena Stephan, Anne Clancy, Andreas Janshoff, and Blanche Schwappach. Wrb and caml are necessary and sufficient to mediate tail-anchored protein targeting to the er membrane. PLoS ONE, 9:e85033, Jan 2014. URL: https://doi.org/10.1371/journal.pone.0085033, doi:10.1371/journal.pone.0085033. This article has 87 citations and is from a peer-reviewed journal.

6. (mcdowell2020structuralbasisof pages 1-3): Melanie A. McDowell, Michael Heimes, Francesco Fiorentino, Shahid Mehmood, Ákos Farkas, Javier Coy-Vergara, Di Wu, Jani Reddy Bolla, Volker Schmid, Roger Heinze, Klemens Wild, Dirk Flemming, Stefan Pfeffer, Blanche Schwappach, Carol V. Robinson, and Irmgard Sinning. Structural basis of tail-anchored membrane protein biogenesis by the get insertase complex. Molecular Cell, 80:72-86.e7, Oct 2020. URL: https://doi.org/10.1016/j.molcel.2020.08.012, doi:10.1016/j.molcel.2020.08.012. This article has 115 citations and is from a highest quality peer-reviewed journal.

7. (vilardi2011wrbisthe pages 2-3): Fabio Vilardi, Holger Lorenz, and Bernhard Dobberstein. Wrb is the receptor for trc40/asna1-mediated insertion of tail-anchored proteins into the er membrane. Journal of Cell Science, 124:1301-1307, Apr 2011. URL: https://doi.org/10.1242/jcs.084277, doi:10.1242/jcs.084277. This article has 154 citations and is from a domain leading peer-reviewed journal.

8. (vilardi2011wrbisthe pages 3-5): Fabio Vilardi, Holger Lorenz, and Bernhard Dobberstein. Wrb is the receptor for trc40/asna1-mediated insertion of tail-anchored proteins into the er membrane. Journal of Cell Science, 124:1301-1307, Apr 2011. URL: https://doi.org/10.1242/jcs.084277, doi:10.1242/jcs.084277. This article has 154 citations and is from a domain leading peer-reviewed journal.

9. (vilardi2014wrbandcaml pages 6-7): Fabio Vilardi, Milena Stephan, Anne Clancy, Andreas Janshoff, and Blanche Schwappach. Wrb and caml are necessary and sufficient to mediate tail-anchored protein targeting to the er membrane. PLoS ONE, 9:e85033, Jan 2014. URL: https://doi.org/10.1371/journal.pone.0085033, doi:10.1371/journal.pone.0085033. This article has 87 citations and is from a peer-reviewed journal.

10. (vilardi2014wrbandcaml media 82f0f8c3): Fabio Vilardi, Milena Stephan, Anne Clancy, Andreas Janshoff, and Blanche Schwappach. Wrb and caml are necessary and sufficient to mediate tail-anchored protein targeting to the er membrane. PLoS ONE, 9:e85033, Jan 2014. URL: https://doi.org/10.1371/journal.pone.0085033, doi:10.1371/journal.pone.0085033. This article has 87 citations and is from a peer-reviewed journal.

11. (mcdowell2020structuralbasisof pages 3-4): Melanie A. McDowell, Michael Heimes, Francesco Fiorentino, Shahid Mehmood, Ákos Farkas, Javier Coy-Vergara, Di Wu, Jani Reddy Bolla, Volker Schmid, Roger Heinze, Klemens Wild, Dirk Flemming, Stefan Pfeffer, Blanche Schwappach, Carol V. Robinson, and Irmgard Sinning. Structural basis of tail-anchored membrane protein biogenesis by the get insertase complex. Molecular Cell, 80:72-86.e7, Oct 2020. URL: https://doi.org/10.1016/j.molcel.2020.08.012, doi:10.1016/j.molcel.2020.08.012. This article has 115 citations and is from a highest quality peer-reviewed journal.

12. (mcdowell2023thegetinsertase pages 1-2): Melanie A. McDowell, Michael Heimes, Giray Enkavi, Ákos Farkas, Daniel Saar, Klemens Wild, Blanche Schwappach, Ilpo Vattulainen, and Irmgard Sinning. The get insertase exhibits conformational plasticity and induces membrane thinning. Nature Communications, Nov 2023. URL: https://doi.org/10.1038/s41467-023-42867-2, doi:10.1038/s41467-023-42867-2. This article has 16 citations and is from a highest quality peer-reviewed journal.

13. (mcdowell2023thegetinsertase pages 9-10): Melanie A. McDowell, Michael Heimes, Giray Enkavi, Ákos Farkas, Daniel Saar, Klemens Wild, Blanche Schwappach, Ilpo Vattulainen, and Irmgard Sinning. The get insertase exhibits conformational plasticity and induces membrane thinning. Nature Communications, Nov 2023. URL: https://doi.org/10.1038/s41467-023-42867-2, doi:10.1038/s41467-023-42867-2. This article has 16 citations and is from a highest quality peer-reviewed journal.

14. (carvalho2019thewrbsubunit pages 1-2): Hugo J. F. Carvalho, Andrea Del Bondio, Francesca Maltecca, Sara F. Colombo, and Nica Borgese. The wrb subunit of the get3 receptor is required for the correct integration of its partner caml into the er. Scientific Reports, Aug 2019. URL: https://doi.org/10.1038/s41598-019-48363-2, doi:10.1038/s41598-019-48363-2. This article has 24 citations and is from a peer-reviewed journal.

15. (carvalho2019thewrbsubunit pages 8-9): Hugo J. F. Carvalho, Andrea Del Bondio, Francesca Maltecca, Sara F. Colombo, and Nica Borgese. The wrb subunit of the get3 receptor is required for the correct integration of its partner caml into the er. Scientific Reports, Aug 2019. URL: https://doi.org/10.1038/s41598-019-48363-2, doi:10.1038/s41598-019-48363-2. This article has 24 citations and is from a peer-reviewed journal.

16. (heo2023theget12insertase pages 1-3): Paul Heo, Jacob A. Culver, Jennifer Miao, Frederic Pincet, and Malaiyalam Mariappan. The get1/2 insertase forms a channel to mediate the insertion of tail-anchored proteins into the er. Cell Reports, 42:111921, Jan 2023. URL: https://doi.org/10.1016/j.celrep.2022.111921, doi:10.1016/j.celrep.2022.111921. This article has 8 citations and is from a highest quality peer-reviewed journal.

17. (farkas2021captureanddelivery pages 5-7): Ákos Farkas and Katherine E. Bohnsack. Capture and delivery of tail-anchored proteins to the endoplasmic reticulum. The Journal of Cell Biology, Jul 2021. URL: https://doi.org/10.1083/jcb.202105004, doi:10.1083/jcb.202105004. This article has 49 citations.

18. (riveramonroy2016micelackingwrb pages 8-9): Jhon Rivera-Monroy, Lena Musiol, Kirsten Unthan-Fechner, Ákos Farkas, Anne Clancy, Javier Coy-Vergara, Uri Weill, Sarah Gockel, Shuh-Yow Lin, David P. Corey, Tobias Kohl, Philipp Ströbel, Maya Schuldiner, Blanche Schwappach, and Fabio Vilardi. Mice lacking wrb reveal differential biogenesis requirements of tail-anchored proteins in vivo. Scientific Reports, Dec 2016. URL: https://doi.org/10.1038/srep39464, doi:10.1038/srep39464. This article has 50 citations and is from a peer-reviewed journal.

19. (riveramonroy2016micelackingwrb pages 7-8): Jhon Rivera-Monroy, Lena Musiol, Kirsten Unthan-Fechner, Ákos Farkas, Anne Clancy, Javier Coy-Vergara, Uri Weill, Sarah Gockel, Shuh-Yow Lin, David P. Corey, Tobias Kohl, Philipp Ströbel, Maya Schuldiner, Blanche Schwappach, and Fabio Vilardi. Mice lacking wrb reveal differential biogenesis requirements of tail-anchored proteins in vivo. Scientific Reports, Dec 2016. URL: https://doi.org/10.1038/srep39464, doi:10.1038/srep39464. This article has 50 citations and is from a peer-reviewed journal.

20. (barlow2001downsyndromecongenital pages 6-8): Gillian M Barlow, Xiao-Ning Chen, Zheng Y Shi, Gary E Lyons, David M Kurnit, Livija Celle, Nancy B Spinner, Elaine Zackai, Mark J Pettenati, Alexander J Van Riper, Michael J Vekemans, Corey H Mjaatvedt, and Julie R Korenberg. Down syndrome congenital heart disease: a narrowed region and a candidate gene. Genetics in Medicine, 3:91-101, Mar 2001. URL: https://doi.org/10.1097/00125817-200103000-00002, doi:10.1097/00125817-200103000-00002. This article has 283 citations and is from a highest quality peer-reviewed journal.

21. (barlow2001downsyndromecongenital pages 5-6): Gillian M Barlow, Xiao-Ning Chen, Zheng Y Shi, Gary E Lyons, David M Kurnit, Livija Celle, Nancy B Spinner, Elaine Zackai, Mark J Pettenati, Alexander J Van Riper, Michael J Vekemans, Corey H Mjaatvedt, and Julie R Korenberg. Down syndrome congenital heart disease: a narrowed region and a candidate gene. Genetics in Medicine, 3:91-101, Mar 2001. URL: https://doi.org/10.1097/00125817-200103000-00002, doi:10.1097/00125817-200103000-00002. This article has 283 citations and is from a highest quality peer-reviewed journal.

22. (riveramonroy2016micelackingwrb pages 3-4): Jhon Rivera-Monroy, Lena Musiol, Kirsten Unthan-Fechner, Ákos Farkas, Anne Clancy, Javier Coy-Vergara, Uri Weill, Sarah Gockel, Shuh-Yow Lin, David P. Corey, Tobias Kohl, Philipp Ströbel, Maya Schuldiner, Blanche Schwappach, and Fabio Vilardi. Mice lacking wrb reveal differential biogenesis requirements of tail-anchored proteins in vivo. Scientific Reports, Dec 2016. URL: https://doi.org/10.1038/srep39464, doi:10.1038/srep39464. This article has 50 citations and is from a peer-reviewed journal.

23. (OpenTargets Search: congenital heart disease,cardiomyopathy,heart disease-WRB,GET1,CAML,TRC40): Open Targets Query (congenital heart disease,cardiomyopathy,heart disease-WRB,GET1,CAML,TRC40, 3 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

24. (vilardi2014wrbandcaml pages 2-3): Fabio Vilardi, Milena Stephan, Anne Clancy, Andreas Janshoff, and Blanche Schwappach. Wrb and caml are necessary and sufficient to mediate tail-anchored protein targeting to the er membrane. PLoS ONE, 9:e85033, Jan 2014. URL: https://doi.org/10.1371/journal.pone.0085033, doi:10.1371/journal.pone.0085033. This article has 87 citations and is from a peer-reviewed journal.

25. (riveramonroy2016micelackingwrb pages 2-3): Jhon Rivera-Monroy, Lena Musiol, Kirsten Unthan-Fechner, Ákos Farkas, Anne Clancy, Javier Coy-Vergara, Uri Weill, Sarah Gockel, Shuh-Yow Lin, David P. Corey, Tobias Kohl, Philipp Ströbel, Maya Schuldiner, Blanche Schwappach, and Fabio Vilardi. Mice lacking wrb reveal differential biogenesis requirements of tail-anchored proteins in vivo. Scientific Reports, Dec 2016. URL: https://doi.org/10.1038/srep39464, doi:10.1038/srep39464. This article has 50 citations and is from a peer-reviewed journal.

26. (riveramonroy2016micelackingwrb pages 4-5): Jhon Rivera-Monroy, Lena Musiol, Kirsten Unthan-Fechner, Ákos Farkas, Anne Clancy, Javier Coy-Vergara, Uri Weill, Sarah Gockel, Shuh-Yow Lin, David P. Corey, Tobias Kohl, Philipp Ströbel, Maya Schuldiner, Blanche Schwappach, and Fabio Vilardi. Mice lacking wrb reveal differential biogenesis requirements of tail-anchored proteins in vivo. Scientific Reports, Dec 2016. URL: https://doi.org/10.1038/srep39464, doi:10.1038/srep39464. This article has 50 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](GET1-deep-research-falcon_artifacts/artifact-00.md)
![## Context ID: pqac-00000017 Table 2 provides the binding affinities (KD) of TRC40 and the TRC40-RAMP4 (TRC40-R4) complex to the WRB coiled-coil domain (WRBcc) ](GET1-deep-research-falcon_artifacts/image-1.png)

## Citations

1. farkas2021captureanddelivery pages 1-3
2. vilardi2011wrbisthe pages 1-2
3. vilardi2011wrbisthe pages 3-5
4. vilardi2014wrbandcaml pages 1-2
5. mcdowell2020structuralbasisof pages 3-4
6. mcdowell2020structuralbasisof pages 1-3
7. mcdowell2023thegetinsertase pages 1-2
8. carvalho2019thewrbsubunit pages 1-2
9. carvalho2019thewrbsubunit pages 8-9
10. farkas2021captureanddelivery pages 5-7
11. mcdowell2023thegetinsertase pages 9-10
12. riveramonroy2016micelackingwrb pages 7-8
13. vilardi2011wrbisthe pages 5-6
14. riveramonroy2016micelackingwrb pages 8-9
15. barlow2001downsyndromecongenital pages 6-8
16. riveramonroy2016micelackingwrb pages 4-5
17. riveramonroy2016micelackingwrb pages 1-2
18. vilardi2011wrbisthe pages 2-3
19. vilardi2014wrbandcaml pages 6-7
20. barlow2001downsyndromecongenital pages 5-6
21. riveramonroy2016micelackingwrb pages 3-4
22. vilardi2014wrbandcaml pages 2-3
23. riveramonroy2016micelackingwrb pages 2-3
24. https://doi.org/10.1242/jcs.084277
25. https://doi.org/10.1083/jcb.202105004;
26. https://doi.org/10.1371/journal.pone.0085033
27. https://doi.org/10.1242/jcs.084277;
28. https://doi.org/10.1016/j.molcel.2020.08.012
29. https://doi.org/10.1038/s41598-019-48363-2
30. https://doi.org/10.1038/s41467-023-42867-2
31. https://doi.org/10.1016/j.celrep.2022.111921
32. https://doi.org/10.59717/j.xinn-life.2023.100013;
33. https://doi.org/10.1242/jcs.261219
34. https://doi.org/10.1073/pnas.2319476121
35. https://doi.org/10.1038/srep39464
36. https://doi.org/10.15252/embj.201593565
37. https://doi.org/10.1097/00125817-200103000-00002;
38. https://doi.org/10.1161/CIRCGEN.119.002507
39. https://doi.org/10.1371/journal.pone.0085033;
40. https://doi.org/10.1016/j.molcel.2020.08.012;
41. https://doi.org/10.1242/jcs.084277,
42. https://doi.org/10.1083/jcb.202105004,
43. https://doi.org/10.1038/srep39464,
44. https://doi.org/10.1371/journal.pone.0085033,
45. https://doi.org/10.1016/j.molcel.2020.08.012,
46. https://doi.org/10.1038/s41467-023-42867-2,
47. https://doi.org/10.1038/s41598-019-48363-2,
48. https://doi.org/10.1016/j.celrep.2022.111921,
49. https://doi.org/10.1097/00125817-200103000-00002,