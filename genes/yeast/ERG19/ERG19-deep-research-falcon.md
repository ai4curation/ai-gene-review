---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-11T16:21:13.270446'
end_time: '2026-06-11T16:36:58.955863'
duration_seconds: 945.69
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: yeast
  gene_id: ERG19
  gene_symbol: MVD1
  uniprot_accession: P32377
  protein_description: 'RecName: Full=Diphosphomevalonate decarboxylase {ECO:0000303|PubMed:9244250};
    EC=4.1.1.33 {ECO:0000269|PubMed:8626466}; AltName: Full=Ergosterol biosynthesis
    protein 19 {ECO:0000303|PubMed:9244250}; AltName: Full=Mevalonate pyrophosphate
    decarboxylase {ECO:0000303|PubMed:8626466}; Short=MPD {ECO:0000303|PubMed:8626466};
    AltName: Full=Mevalonate-5-diphosphate decarboxylase {ECO:0000303|PubMed:11698677};
    Short=MDD {ECO:0000303|PubMed:11698677}; Short=MDDase {ECO:0000303|PubMed:11698677};'
  gene_info: Name=MVD1 {ECO:0000303|PubMed:11698677}; Synonyms=ERG19 {ECO:0000303|PubMed:9244250},
    MPD {ECO:0000303|PubMed:8626466}; OrderedLocusNames=YNR043W; ORFNames=N3427;
  organism_full: Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
  protein_family: Belongs to the diphosphomevalonate decarboxylase family.
  protein_domains: GHMP_kinase_C_sf. (IPR036554); Mev_decarb. (IPR005935); Mev_diP_decarb.
    (IPR029765); MVD-like_N. (IPR053859); Mvd1_C. (IPR041431)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 36
artifact_count: 3
artifact_sources:
  edison_answer_artifacts: 2
  edison_message_content: 1
artifacts:
- filename: artifact-00.md
  path: ERG19-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: ERG19-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
- filename: image-1.png
  path: ERG19-deep-research-falcon_artifacts/image-1.png
  media_type: image/png
  source: edison_message_content
  data_storage_id: null
  description: '## Context ID: pqac-00000017 Figure 1 from the document depicts the
    ergosterol biosynthetic pathway in *S. cerevisiae*, organized into color-coded
    modules repre'
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** P32377
- **Protein Description:** RecName: Full=Diphosphomevalonate decarboxylase {ECO:0000303|PubMed:9244250}; EC=4.1.1.33 {ECO:0000269|PubMed:8626466}; AltName: Full=Ergosterol biosynthesis protein 19 {ECO:0000303|PubMed:9244250}; AltName: Full=Mevalonate pyrophosphate decarboxylase {ECO:0000303|PubMed:8626466}; Short=MPD {ECO:0000303|PubMed:8626466}; AltName: Full=Mevalonate-5-diphosphate decarboxylase {ECO:0000303|PubMed:11698677}; Short=MDD {ECO:0000303|PubMed:11698677}; Short=MDDase {ECO:0000303|PubMed:11698677};
- **Gene Information:** Name=MVD1 {ECO:0000303|PubMed:11698677}; Synonyms=ERG19 {ECO:0000303|PubMed:9244250}, MPD {ECO:0000303|PubMed:8626466}; OrderedLocusNames=YNR043W; ORFNames=N3427;
- **Organism (full):** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
- **Protein Family:** Belongs to the diphosphomevalonate decarboxylase family.
- **Key Domains:** GHMP_kinase_C_sf. (IPR036554); Mev_decarb. (IPR005935); Mev_diP_decarb. (IPR029765); MVD-like_N. (IPR053859); Mvd1_C. (IPR041431)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "MVD1" matches the protein description above**
2. **Verify the organism is correct:** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'MVD1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **MVD1** (gene ID: ERG19, UniProt: P32377) in yeast.

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
- **UniProt Accession:** P32377
- **Protein Description:** RecName: Full=Diphosphomevalonate decarboxylase {ECO:0000303|PubMed:9244250}; EC=4.1.1.33 {ECO:0000269|PubMed:8626466}; AltName: Full=Ergosterol biosynthesis protein 19 {ECO:0000303|PubMed:9244250}; AltName: Full=Mevalonate pyrophosphate decarboxylase {ECO:0000303|PubMed:8626466}; Short=MPD {ECO:0000303|PubMed:8626466}; AltName: Full=Mevalonate-5-diphosphate decarboxylase {ECO:0000303|PubMed:11698677}; Short=MDD {ECO:0000303|PubMed:11698677}; Short=MDDase {ECO:0000303|PubMed:11698677};
- **Gene Information:** Name=MVD1 {ECO:0000303|PubMed:11698677}; Synonyms=ERG19 {ECO:0000303|PubMed:9244250}, MPD {ECO:0000303|PubMed:8626466}; OrderedLocusNames=YNR043W; ORFNames=N3427;
- **Organism (full):** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
- **Protein Family:** Belongs to the diphosphomevalonate decarboxylase family.
- **Key Domains:** GHMP_kinase_C_sf. (IPR036554); Mev_decarb. (IPR005935); Mev_diP_decarb. (IPR029765); MVD-like_N. (IPR053859); Mvd1_C. (IPR041431)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "MVD1" matches the protein description above**
2. **Verify the organism is correct:** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'MVD1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **MVD1** (gene ID: ERG19, UniProt: P32377) in yeast.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Comprehensive research report: *Saccharomyces cerevisiae* **MVD1/ERG19** (UniProt **P32377**, locus **YNR043W**)—functional annotation, pathway context, and applications

## 0. Target verification (mandatory)
The UniProt accession **P32377** corresponds to *Saccharomyces cerevisiae* (S288c) **ERG19**, also called **MVD1/Mvd1**, annotated as **diphosphomevalonate (mevalonate diphosphate) decarboxylase** (**EC 4.1.1.33**) in the mevalonate/ergosterol pathway. Multiple independent sources explicitly identify **ERG19** as the yeast gene encoding **mevalonate diphosphate (pyrophosphate) decarboxylase**, matching the UniProt description and enzyme classification. (benveniste2002sterolmetabolism pages 4-7, maury2005microbialisoprenoidproduction pages 9-12, jorda2020regulationofergosterol pages 3-4)

## 1. Key concepts, definitions, and current understanding

### 1.1. What enzyme ERG19 encodes
**ERG19/Mvd1** encodes **mevalonate diphosphate decarboxylase** (also called **diphosphomevalonate decarboxylase**). This enzyme produces the universal C5 isoprenoid building block **isopentenyl diphosphate (IPP)** from **mevalonate 5-diphosphate (mevalonate pyrophosphate; MVAPP)**. (benveniste2002sterolmetabolism pages 4-7, maury2005microbialisoprenoidproduction pages 9-12, maury2005microbialisoprenoidproduction pages 7-9)

### 1.2. Catalyzed reaction (substrates/products)
The enzyme catalyzes an **ATP-dependent** decarboxylation that converts **MVAPP → IPP**, releasing **CO2**; this step is a key conversion that channels carbon into downstream **isoprenoid** and **ergosterol** biosynthesis. (benveniste2002sterolmetabolism pages 4-7, maury2005microbialisoprenoidproduction pages 9-12, sun2019mevalonatediphosphatedecarboxylase pages 1-2)

### 1.3. Cofactors and mechanistic summary
Mechanistic descriptions in the retrieved literature indicate that the reaction is **ATP-dependent** and **Mg2+-requiring**. A mechanistic model describes initial phosphorylation (transfer of ATP γ-phosphate to the C3-hydroxyl of MVAPP), followed by **decarboxylation** and **elimination**, proceeding via a transient **3-phospho-mevalonate-5-diphosphate** intermediate; ERG19/Mvd1 is classified within the **GHMP kinase superfamily** context in this mechanistic framing. (garay2026themevalonatepathway pages 12-13, sun2019mevalonatediphosphatedecarboxylase pages 1-2)

### 1.4. Pathway context (mevalonate → isoprenoid → ergosterol)
In yeast, ERG19 functions in the early mevalonate pathway that supplies **IPP**, which is then converted through **IDI1** and prenyltransferases (e.g., **ERG20**) to longer prenyl diphosphates feeding sterol synthesis (ergosterol) and also other essential isoprenoid-derived metabolites (e.g., ubiquinone, dolichol, heme, prenylated proteins). (maury2005microbialisoprenoidproduction pages 9-12, jorda2020regulationofergosterol pages 3-4, jorda2020regulationofergosterol media b5666840)

**Figure-based pathway evidence.** Jordá & Puig’s 2020 review depicts ERG19/Mvd1 (“mevalonate pyrophosphate decarboxylase”) in the ergosterol biosynthetic map and assigns pathway modules to distinct cellular locations (vacuole/mitochondria for earlier modules; ER for late sterol steps). (jorda2020regulationofergosterol media b5666840)

### 1.5. Cellular localization: current evidence and uncertainty
The retrieved corpus contains **partly inconsistent** localization statements:

* Reviews focused on yeast cell-factory engineering describe the “second module” including ERG19 as **predominantly cytoplasmic**. (johnston2020thewide‐rangingphenotypes pages 1-5)
* A review on compartmentalized isoprenoid engineering notes that localization databases suggest **MVA pathway proteins are mostly cytosolic** (without providing ERG19-specific imaging in the excerpted text). (cao2020harnessingsuborganellemetabolism pages 1-2)
* Conversely, Jordá & Puig’s pathway figure annotates earlier modules of the pathway as occurring in **vacuole/mitochondria** (and a later module in ER), implying a more complex compartment map in yeast regulatory thinking. (jorda2020regulationofergosterol media b5666840)

**Conclusion:** a direct ERG19/Mvd1 localization experiment in *S. cerevisiae* (e.g., ERG19-GFP microscopy) was **not found in the retrieved texts**, so localization is best stated as **primarily cytosolic by inference from pathway/module descriptions and localization database summaries**, with awareness that some reviews present alternative compartment assignments. (johnston2020thewide‐rangingphenotypes pages 1-5, cao2020harnessingsuborganellemetabolism pages 1-2, jorda2020regulationofergosterol media b5666840)

### 1.6. Oligomerization / protein-protein interaction evidence
A reviewed line of evidence indicates that yeast mevalonate diphosphate decarboxylase forms **homodimers in vivo**; dimerization defects can be caused by single amino-acid substitutions (as summarized), and cross-species dimer interactions are reported in complementation/two-hybrid contexts. (benveniste2002sterolmetabolism pages 4-7)

## 2. Essentiality and phenotypic consequences (what is known from retrieved evidence)
Within the retrieved evidence set, ERG19/Mvd1 is described as **essential for viability** (stated in yeast-related literature cited by a filamentous-fungus paper’s reference context). However, primary *S. cerevisiae erg19* mutant phenotype experiments were not directly retrieved here, so the evidence is best treated as **authoritative secondary reporting**, not a direct phenotype dataset in this run. (hu2019effectsongene pages 12-13)

More broadly, disruption of ergosterol synthesis causes pleiotropic defects in growth and stress adaptation (and ergosterol inhibition can lead to mitochondrial DNA loss unless ergosterol is supplied), emphasizing that upstream supply of sterol precursors is physiologically critical. (jorda2020regulationofergosterol pages 1-3)

## 3. Regulation and expert synthesis

### 3.1. Pathway-level transcriptional regulation context
A major yeast ergosterol-regulation review states that sterol regulatory element-binding transcription factors **Upc2** and **Ecm22**, the heme-binding protein **Hap1**, and repressors **Rox1** and **Mot3** coordinate **ERG gene expression** in *S. cerevisiae* under changing oxygen/iron/sterol conditions. This is pathway-level regulation context relevant to ERG19, though ERG19-specific promoter analyses were not extracted from the available text. (jorda2020regulationofergosterol pages 1-3)

A mechanistic review/preprint further states that fungal ERG19/MDD expression is regulated by **Upc2p/Ecm22p** and is **upregulated under sterol-depleted conditions**, again providing pathway-level regulation context rather than a gene-specific promoter dissection in the retrieved excerpts. (garay2026themevalonatepathway pages 12-13)

### 3.2. Expert interpretation (authoritative sources)
Authoritative reviews frame ergosterol biosynthesis as a high-energy, high-reducing-power pathway. Jordá & Puig report an estimated requirement of **24 ATP and 16 NADPH per ergosterol** molecule (reviewed), underscoring why flux through early steps (including ERG19) is tightly regulated and why engineering often targets upstream mevalonate reactions. (jorda2020regulationofergosterol pages 3-4, jorda2020regulationofergosterol pages 4-6)

## 4. Recent developments (prioritizing 2023–2024)

### 4.1. 2024: replacing the mevalonate pathway (modeling + growth-coupled strain design)
A 2024 **Nature Communications** study (Li et al.; accepted 6 Nov 2024; URL below) uses genome-scale modeling and experiments to replace the native mevalonate pathway with a two-step **isopentenol utilization (IU)** pathway relying on ATP as the only cofactor.

Key ERG19-relevant findings:
* Flux balance analysis predicts that knockout of **ERG19** (along with other MVA genes) **inactivates the MVA pathway** and prevents growth without an alternative supply route. (li2024yeastmetabolismadaptation pages 1-2)
* Introducing the IU pathway and supplying isopentenol restored growth; at **0.0186 mmol/gDCW/h**, growth matched wild-type level (quantitative modeling result). (li2024yeastmetabolismadaptation pages 1-2)

**Publication details:** Li et al., *Nature Communications* (2024), https://doi.org/10.1038/s41467-024-54298-8 (li2024yeastmetabolismadaptation pages 1-2)

### 4.2. 2023–2024: limitations in ERG19-specific literature in retrieved set
Within the retrieved 2023–2024 documents accessible here, ERG19 is not extensively re-characterized biochemically; rather, ERG19 appears in systems-level modeling, pathway replacement, and as a standard node in terpenoid precursor supply logic. (li2024yeastmetabolismadaptation pages 1-2)

## 5. Current applications and real-world implementations

### 5.1. ERG19 as an engineering node in yeast terpenoid/sterol production
A 2022 metabolic engineering study demonstrates a high-flux mevalonate/sterol precursor chassis where ERG19 is among multiple overexpressed genes (ERG10, ERG13, tHMG1, ERG12, ERG8, ERG19, IDI1, ERG20, ERG9). Quantitative outcomes reported include:

* **408.88 ± 0.09 mg/L squalene** in shake flasks (engineered strain SQ3-5). (lu2022enhancingfluxesthrough pages 1-2)
* **4.94 g/L squalene** in fed-batch fermentation (cane molasses medium). (lu2022enhancingfluxesthrough pages 1-2)
* **11.86 ± 0.09 mg/L β-caryophyllene** in a derived strain expressing β-caryophyllene synthase. (lu2022enhancingfluxesthrough pages 1-2)

**Publication details:** Lu et al., *Microbial Biotechnology* (May 2022), https://doi.org/10.1111/1751-7915.14072 (lu2022enhancingfluxesthrough pages 1-2, lu2022enhancingfluxesthrough pages 10-12)

### 5.2. ERG19 in in vitro synthetic biochemistry (cell-free isoprene production)
A 2017 *Microbial Cell Factories* study used **ERG19 cloned from *S. cerevisiae*** as the mevalonate diphosphate decarboxylase component of a five-enzyme lower-mevalonate module to produce **isoprene** from mevalonate in vitro.

Quantitative outcomes:
* Optimized small-scale system produced **6323.5 µmol/L/h (430 mg/L/h) isoprene**, using **5.0 µM** MVD (ERG19 product) along with MVK, PMK, IDI, and isoprene synthase. (sun2019mevalonatediphosphatedecarboxylase pages 1-2)
* Scale-up (50 mL) produced **302 mg/L isoprene in 40 h**, using **0.5 µM** MVD. (sun2019mevalonatediphosphatedecarboxylase pages 1-2)

**Publication details:** Cheng et al., *Microbial Cell Factories* (Jan 2017), https://doi.org/10.1186/s12934-016-0622-4 (sun2019mevalonatediphosphatedecarboxylase pages 1-2)

### 5.3. Synthetic pathway rewiring using ERG19 deletion background
A 2019 ACS Chemical Biology study on an alternative mevalonate pathway (altMVA) reports constructing a viable engineered *S. cerevisiae* platform in which the classical pathway is replaced; the excerpt shows ERG19 deletion/counterselection in strain construction (ERG19 appears explicitly in the strain engineering logic), supporting ERG19’s centrality as a control point in pathway replacement strategies. (sun2019mevalonatediphosphatedecarboxylase pages 1-2)

## 6. Statistics and quantitative data (from retrieved studies)
Key quantitative data points directly tied to ERG19-containing systems in the retrieved set:

* **Squalene titers (engineered yeast; ERG19 included in overexpression set):** 408.88 ± 0.09 mg/L (shake flask); 4.94 g/L (fed-batch). (lu2022enhancingfluxesthrough pages 1-2)
* **β-caryophyllene (engineered yeast chassis; ERG19 included in precursor pathway optimization framework):** 11.86 ± 0.09 mg/L. (lu2022enhancingfluxesthrough pages 1-2)
* **Cell-free isoprene production using *S. cerevisiae* ERG19 enzyme:** 430 mg/L/h in optimized small-scale; 302 mg/L in 40 h at 50 mL scale. (sun2019mevalonatediphosphatedecarboxylase pages 1-2)
* **2024 modeling/growth restoration value in pathway replacement context:** growth matched wild-type at IU pathway flux **0.0186 mmol/gDCW/h**; ERG19 knockout predicted to inactivate MVA pathway. (li2024yeastmetabolismadaptation pages 1-2)

## 7. Evidence summary tables
The following evidence-map artifacts consolidate the main findings with publication dates and URLs.

| Topic | Key findings | Evidence type | Representative source (author year) | Publication date | URL | Citation ID |
|---|---|---|---|---|---|---|
| Identity | Target identity is verified: *S. cerevisiae* ERG19 (alias MVD1/Mvd1; YNR043W) encodes mevalonate/diphosphomevalonate pyrophosphate decarboxylase, EC 4.1.1.33, matching UniProt P32377; no conflicting yeast gene identity was found in retrieved texts. | Review | Benveniste 2002; Jordá & Puig 2020 | 2002-01; 2020-07-15 | https://doi.org/10.1199/tab.0004 ; https://doi.org/10.3390/genes11070795 | (benveniste2002sterolmetabolism pages 4-7, jorda2020regulationofergosterol pages 3-4, jorda2020regulationofergosterol pages 1-3) |
| Reaction | ERG19/Mvd1 catalyzes ATP-dependent conversion of mevalonate 5-diphosphate (mevalonate pyrophosphate; MVAPP) to isopentenyl diphosphate (IPP), with CO2 release. | Review | Benveniste 2002; Maury et al. 2005 | 2002-01; 2005-07 | https://doi.org/10.1199/tab.0004 ; https://doi.org/10.1007/b136410 | (benveniste2002sterolmetabolism pages 4-7, maury2005microbialisoprenoidproduction pages 9-12, sun2019mevalonatediphosphatedecarboxylase pages 1-2) |
| Cofactors/mechanism | Reaction requires ATP and Mg2+; mechanistic summary in retrieved texts describes phosphorylation of the C3-hydroxyl of MVAPP by ATP, followed by decarboxylation/elimination via a transient 3-phospho-mevalonate-5-diphosphate intermediate; enzyme belongs to the GHMP kinase superfamily. | Review | Garay et al. 2026 preprint; Sun et al. 2019 | 2026-05; 2019-05 | https://doi.org/10.20944/preprints202605.0182.v1 ; https://doi.org/10.3389/fmicb.2019.01074 | (garay2026themevalonatepathway pages 12-13, sun2019mevalonatediphosphatedecarboxylase pages 1-2) |
| Pathway role | Mvd1/Erg19 supplies IPP, the universal C5 isoprenoid building block, placing it in the early mevalonate/ergosterol pathway upstream of IDI1 and ERG20 and therefore upstream of sterol, ubiquinone, dolichol, heme, and prenylated-protein biosynthesis. | Review | Maury et al. 2005; Jordá & Puig 2020 | 2005-07; 2020-07-15 | https://doi.org/10.1007/b136410 ; https://doi.org/10.3390/genes11070795 | (maury2005microbialisoprenoidproduction pages 9-12, maury2005microbialisoprenoidproduction pages 7-9, jorda2020regulationofergosterol pages 3-4, jorda2020regulationofergosterol pages 1-3, jorda2020regulationofergosterol media b5666840) |
| Localization | Retrieved sources are partly inconsistent. One review/preprint describes MDD/Mvd1 as a cytosolic homodimer and a 2020 cell-factory review states the MVA-pathway proteins are mostly cytosolic. By contrast, Jordá & Puig’s pathway figure places the first/second pathway modules in vacuole/mitochondria or vacuole; direct ERG19-specific localization experiment in *S. cerevisiae* was not found in retrieved texts. | Review | Johnston et al. 2020; Cao et al. 2020; Jordá & Puig 2020 | 2020-01; 2020-09; 2020-07-15 | https://doi.org/10.1002/yea.3452 ; https://doi.org/10.1016/j.synbio.2020.06.005 ; https://doi.org/10.3390/genes11070795 | (johnston2020thewide‐rangingphenotypes pages 1-5, garay2026themevalonatepathway pages 12-13, cao2020harnessingsuborganellemetabolism pages 1-2, jorda2020regulationofergosterol media b5666840) |
| Essentiality/phenotypes | ERG19 is described as essential for viability in yeast-related literature cited in retrieved texts; pathway defects in ergosterol synthesis broadly impair proliferation/stress adaptation, and pharmacological or genetic inhibition of ergosterol synthesis can cause mitochondrial-DNA loss unless ergosterol is supplied. Specific *S. cerevisiae erg19* mutant phenotype details were otherwise not found in retrieved texts. | Review | Hu et al. 2019; Jordá & Puig 2020 | 2019-09; 2020-07-15 | https://doi.org/10.3390/microorganisms7090342 ; https://doi.org/10.3390/genes11070795 | (hu2019effectsongene pages 12-13, jorda2020regulationofergosterol pages 1-3) |
| Regulation | Retrieved texts indicate fungal MDD/ERG19 expression is controlled at the pathway level by sterol-responsive transcription factors Upc2p and Ecm22p and is induced under sterol-depleted conditions; Jordá & Puig review identifies Upc2/Ecm22, Hap1, Rox1 and Mot3 as central coordinators of ERG gene expression in *S. cerevisiae*, but ERG19-specific promoter-level details were not found in retrieved texts. | Review | Garay et al. 2026 preprint; Jordá & Puig 2020 | 2026-05; 2020-07-15 | https://doi.org/10.20944/preprints202605.0182.v1 ; https://doi.org/10.3390/genes11070795 | (garay2026themevalonatepathway pages 12-13, jorda2020regulationofergosterol pages 1-3) |
| Protein-protein interactions / oligomerization | MVDPD/Mvd1 forms homodimers in vivo; Arabidopsis MVDPD can heterodimerize with the yeast enzyme in complementation/two-hybrid evidence summarized in review literature. | Review summarizing primary evidence | Benveniste 2002 | 2002-01 | https://doi.org/10.1199/tab.0004 | (benveniste2002sterolmetabolism pages 4-7) |
| Metabolic engineering / applications | ERG19 is a standard engineering node in yeast mevalonate-pathway optimization. In strain SQ-3, overexpression of ERG10, ERG13, tHMG1, ERG12, ERG8, ERG19, IDI1, ERG20 and ERG9 supported high-flux terpene production; downstream tuning enabled 408.88 ± 0.09 mg/L squalene in shake flasks and 4.94 g/L in fed-batch, and a derived strain produced 11.86 ± 0.09 mg/L β-caryophyllene. In an alternative-pathway study, ERG19 deletion was used as part of replacing the classical MVA pathway in yeast; in 2024 FBA, ERG19 knockout was predicted to inactivate the MVA pathway. | Engineering | Lu et al. 2022; Thomas et al. 2019; Li et al. 2024 | 2022-05; 2019-07; 2024-11-06 accepted | https://doi.org/10.1111/1751-7915.14072 ; https://doi.org/10.1021/acschembio.9b00322 ; https://doi.org/10.1038/s41467-024-54298-8 | (lu2022enhancingfluxesthrough pages 1-2, lu2022enhancingfluxesthrough pages 10-12, li2024yeastmetabolismadaptation pages 1-2) |


*Table: This table summarizes the key verified facts for *Saccharomyces cerevisiae* MVD1/ERG19 (UniProt P32377), including biochemical function, pathway role, localization evidence, regulation, and engineering relevance. It is designed as a compact evidence map with dates, URLs, and context citations for rapid use in functional annotation.*

| Use case | What was done with ERG19 | Product/Outcome | Quantitative metrics | Host/Context | Publication date | URL | Citation ID |
|---|---|---|---|---|---|---|---|
| Metabolic engineering of native mevalonate pathway | ERG19 was one of the overexpressed pathway genes in strain SQ-3 together with ERG10, ERG13, tHMG1, ERG12, ERG8, IDI1, ERG20, and ERG9 | High-flux chassis for terpene/sterol production; downstream strains produced squalene and β-caryophyllene | Derived strain SQ3-5 produced **408.88 ± 0.09 mg/L squalene** in shake flasks and **4.94 g/L squalene** in fed-batch cane molasses medium; derived strain SQ3-4-CPS produced **11.86 ± 0.09 mg/L β-caryophyllene**; HMGR optimization in the same study gave **431-fold** and **9-fold** squalene increases in haploid and industrial strains, respectively (lu2022enhancingfluxesthrough pages 1-2, lu2022enhancingfluxesthrough pages 10-12) | *Saccharomyces cerevisiae* industrial and laboratory engineering platform | 2022-05 | https://doi.org/10.1111/1751-7915.14072 | (lu2022enhancingfluxesthrough pages 1-2, lu2022enhancingfluxesthrough pages 10-12) |
| Pathway replacement / modeling | ERG19 knockout was evaluated **in silico** as one of several deletions that inactivate the native MVA pathway; ERG19 was not the practical deletion used experimentally, but its loss was explicitly modeled | Demonstrated that ERG19 is indispensable for native MVA-pathway-supported growth; informed design of an isopentenol utilization (IU) pathway-dependent strain | Flux balance analysis predicted no growth without the MVA pathway; introduction of the IU pathway plus isopentenol restored growth, with wild-type-level growth at **0.0186 mmol/gDCW/h** isopentenol flux; PRM10L156Q reduced prenol uptake by **30.88%** while isoprenol uptake was unaffected (li2024yeastmetabolismadaptation pages 1-2) | *Saccharomyces cerevisiae* growth-coupled terpenoid platform using alternative precursor assimilation | 2024-11-06 accepted / 2024 | https://doi.org/10.1038/s41467-024-54298-8 | (li2024yeastmetabolismadaptation pages 1-2) |
| In vitro biocatalysis / synthetic biochemistry | ERG19 from *S. cerevisiae* was cloned and used as the MVD enzyme in a five-enzyme lower mevalonate pathway module (with MVK, PMK, IDI, ISPS) | Cell-free conversion of mevalonate to isoprene | Optimized 2 mL system produced **6323.5 µmol/L/h (430 mg/L/h) isoprene** using balanced enzyme levels including **5.0 µM MVD**; 50 mL scale-up produced **302 mg/L isoprene in 40 h** using **0.5 µM MVD** (sun2019mevalonatediphosphatedecarboxylase pages 1-2) | In vitro enzyme system using yeast ERG19 as one component of the lower MVA pathway | 2017-01 | https://doi.org/10.1186/s12934-016-0622-4 | (sun2019mevalonatediphosphatedecarboxylase pages 1-2) |
| Synthetic pathway rewiring / altMVA platform | Native ERG19 was functionally bypassed in a yeast platform where the classical MVA pathway was replaced with an alternative mevalonate pathway; ERG19 deletion/background dependence was part of strain construction | Viable *S. cerevisiae* platform for enzyme engineering and terpene biosynthesis using an alternative route to IPP | Study reported creation of a viable engineered yeast platform replacing the classical pathway with altMVA, but no ERG19-specific production titer was provided in the retrieved excerpt (sun2019mevalonatediphosphatedecarboxylase pages 1-2) | *Saccharomyces cerevisiae* synthetic biology chassis for alternative mevalonate-pathway engineering | 2019-07 | https://doi.org/10.1021/acschembio.9b00322 | (sun2019mevalonatediphosphatedecarboxylase pages 1-2) |
| Expert pathway analysis / engineering target context | ERG19 was identified as the mevalonate diphosphate decarboxylase step that can affect sterol flux; overexpression was discussed as potentially reducing sterol content through diphosphate accumulation/feedback effects | Conceptual basis for choosing ERG19 as a control point in isoprenoid and sterol engineering | No standalone numeric ERG19 engineering metric reported in the retrieved excerpt; expert review highlighted ERG19 as a pathway node with possible flux-control consequences (maury2005microbialisoprenoidproduction pages 9-12, maury2005microbialisoprenoidproduction pages 13-14) | Review perspective on microbial isoprenoid production in yeast | 2005-07 | https://doi.org/10.1007/b136410 | (maury2005microbialisoprenoidproduction pages 9-12, maury2005microbialisoprenoidproduction pages 13-14) |


*Table: This table summarizes how S. cerevisiae ERG19/MVD1 has been used or implicated in metabolic engineering, pathway replacement, and in vitro biocatalysis studies. It prioritizes 2022-2024 evidence where available and includes quantitative outcomes to support functional annotation and application-focused interpretation.*

## 8. Limitations of this evidence set (important for functional annotation)
* **Subcellular localization in *S. cerevisiae*:** No direct ERG19-GFP (or equivalent) localization experiment was retrieved; available sources provide a mix of cytosolic inference and compartmentalized pathway schematics. This report therefore flags localization as **inferred/partly uncertain** rather than experimentally resolved here. (cao2020harnessingsuborganellemetabolism pages 1-2, jorda2020regulationofergosterol media b5666840)
* **ERG19-specific mutant phenotypes in budding yeast:** Essentiality is stated in secondary contexts, but direct primary phenotype experiments for *S. cerevisiae erg19* were not retrieved in this run. (hu2019effectsongene pages 12-13)

## 9. Practical functional annotation statement (for databases / pipelines)
**MVD1/ERG19 (UniProt P32377)** encodes **mevalonate 5-diphosphate decarboxylase** (EC 4.1.1.33), catalyzing an **ATP- and Mg2+-dependent decarboxylation** converting **mevalonate-5-diphosphate (MVAPP)** to **isopentenyl diphosphate (IPP)**, thereby supplying the universal C5 precursor for **ergosterol and other isoprenoid-derived metabolites**. Evidence supports **in vivo homodimerization**; localization is most commonly treated as **cytosolic** in engineering-focused literature, though some pathway schematics assign early modules to vacuole/mitochondria and the late steps to ER, indicating that compartmental context remains nuanced in the retrieved evidence. (benveniste2002sterolmetabolism pages 4-7, maury2005microbialisoprenoidproduction pages 9-12, sun2019mevalonatediphosphatedecarboxylase pages 1-2, johnston2020thewide‐rangingphenotypes pages 1-5, cao2020harnessingsuborganellemetabolism pages 1-2, jorda2020regulationofergosterol media b5666840)


References

1. (benveniste2002sterolmetabolism pages 4-7): Pierre Benveniste. Sterol metabolism. The arabidopsis book, 1:e0004, Jan 2002. URL: https://doi.org/10.1199/tab.0004, doi:10.1199/tab.0004. This article has 104 citations and is from a peer-reviewed journal.

2. (maury2005microbialisoprenoidproduction pages 9-12): Jérôme Maury, Mohammad A. Asadollahi, Kasper Møller, Anthony Clark, and Jens Nielsen. Microbial isoprenoid production: an example of green chemistry through metabolic engineering. Advances in biochemical engineering/biotechnology, 100:19-51, Jul 2005. URL: https://doi.org/10.1007/b136410, doi:10.1007/b136410. This article has 174 citations.

3. (jorda2020regulationofergosterol pages 3-4): Tania Jordá and Sergi Puig. Regulation of ergosterol biosynthesis in saccharomyces cerevisiae. Genes, 11:795, Jul 2020. URL: https://doi.org/10.3390/genes11070795, doi:10.3390/genes11070795. This article has 547 citations.

4. (maury2005microbialisoprenoidproduction pages 7-9): Jérôme Maury, Mohammad A. Asadollahi, Kasper Møller, Anthony Clark, and Jens Nielsen. Microbial isoprenoid production: an example of green chemistry through metabolic engineering. Advances in biochemical engineering/biotechnology, 100:19-51, Jul 2005. URL: https://doi.org/10.1007/b136410, doi:10.1007/b136410. This article has 174 citations.

5. (sun2019mevalonatediphosphatedecarboxylase pages 1-2): Yunlong Sun, Yali Niu, Hui Huang, Bin He, Long Ma, Yayi Tu, Van-Tuan Tran, Bin Zeng, and Zhihong Hu. Mevalonate diphosphate decarboxylase mvd/erg19 is required for ergosterol biosynthesis, growth, sporulation and stress tolerance in aspergillus oryzae. Frontiers in Microbiology, May 2019. URL: https://doi.org/10.3389/fmicb.2019.01074, doi:10.3389/fmicb.2019.01074. This article has 22 citations and is from a peer-reviewed journal.

6. (garay2026themevalonatepathway pages 12-13): Aisel Valle Garay, Cíntia Marques Coelho, Napoleão Fonseca Valadares, Leonardo Ferreira da Silva, Letícia Sousa Cabral, Matheus Castro Leitão, Luiza Cesca Piva, Janice Lisboa De Marco, Brenda Rabello de Camargo, Amanda Araújo Souza, Izadora Cristina Moreira de Oliveira, Matheus Ferroni Schwartz, Túlio Marcos Godoy de Andrade, Talita Souza Carmo, João Ricardo Moreira de Almeida, Fernando Araripe Gonçalves Torres, and Sonia Maria de Freitas. The mevalonate pathway: characteristics, innovations, applications, and challenges in biotechnology. Unknown journal, May 2026. URL: https://doi.org/10.20944/preprints202605.0182.v1, doi:10.20944/preprints202605.0182.v1.

7. (jorda2020regulationofergosterol media b5666840): Tania Jordá and Sergi Puig. Regulation of ergosterol biosynthesis in saccharomyces cerevisiae. Genes, 11:795, Jul 2020. URL: https://doi.org/10.3390/genes11070795, doi:10.3390/genes11070795. This article has 547 citations.

8. (johnston2020thewide‐rangingphenotypes pages 1-5): Emily J. Johnston, Tessa Moses, and Susan J. Rosser. The wide‐ranging phenotypes of ergosterol biosynthesis mutants, and implications for microbial cell factories. Yeast, 37:27-44, Jan 2020. URL: https://doi.org/10.1002/yea.3452, doi:10.1002/yea.3452. This article has 85 citations and is from a peer-reviewed journal.

9. (cao2020harnessingsuborganellemetabolism pages 1-2): Xuan H Cao, Shan Yang, Chunyang Cao, and Yongjin J. Zhou. Harnessing sub-organelle metabolism for biosynthesis of isoprenoids in yeast. Sep 2020. URL: https://doi.org/10.1016/j.synbio.2020.06.005, doi:10.1016/j.synbio.2020.06.005. This article has 75 citations.

10. (hu2019effectsongene pages 12-13): Zhihong Hu, Hui Huang, Yunlong Sun, Yali Niu, Wangzishuai Xu, Qicong Liu, Zhe Zhang, Chunmiao Jiang, Yongkai Li, and Bin Zeng. Effects on gene transcription profile and fatty acid composition by genetic modification of mevalonate diphosphate decarboxylase mvd/erg19 in aspergillus oryzae. Microorganisms, 7:342, Sep 2019. URL: https://doi.org/10.3390/microorganisms7090342, doi:10.3390/microorganisms7090342. This article has 10 citations.

11. (jorda2020regulationofergosterol pages 1-3): Tania Jordá and Sergi Puig. Regulation of ergosterol biosynthesis in saccharomyces cerevisiae. Genes, 11:795, Jul 2020. URL: https://doi.org/10.3390/genes11070795, doi:10.3390/genes11070795. This article has 547 citations.

12. (jorda2020regulationofergosterol pages 4-6): Tania Jordá and Sergi Puig. Regulation of ergosterol biosynthesis in saccharomyces cerevisiae. Genes, 11:795, Jul 2020. URL: https://doi.org/10.3390/genes11070795, doi:10.3390/genes11070795. This article has 547 citations.

13. (li2024yeastmetabolismadaptation pages 1-2): Guangjian Li, Hui Liang, Ruichen Gao, Ling Qin, Pei Xu, Mingtao Huang, Min-Hua Zong, Yufei Cao, and Wen-Yong Lou. Yeast metabolism adaptation for efficient terpenoids synthesis via isopentenol utilization. Nature Communications, Nov 2024. URL: https://doi.org/10.1038/s41467-024-54298-8, doi:10.1038/s41467-024-54298-8. This article has 44 citations and is from a highest quality peer-reviewed journal.

14. (lu2022enhancingfluxesthrough pages 1-2): Surui Lu, Chenyao Zhou, Xue-na Guo, Zhengda Du, Yanfei Cheng, Zhaoyue Wang, and Xiuping He. Enhancing fluxes through the mevalonate pathway in saccharomyces cerevisiae by engineering the hmgr and β‐alanine metabolism. Microbial Biotechnology, 15:2292-2306, May 2022. URL: https://doi.org/10.1111/1751-7915.14072, doi:10.1111/1751-7915.14072. This article has 56 citations and is from a peer-reviewed journal.

15. (lu2022enhancingfluxesthrough pages 10-12): Surui Lu, Chenyao Zhou, Xue-na Guo, Zhengda Du, Yanfei Cheng, Zhaoyue Wang, and Xiuping He. Enhancing fluxes through the mevalonate pathway in saccharomyces cerevisiae by engineering the hmgr and β‐alanine metabolism. Microbial Biotechnology, 15:2292-2306, May 2022. URL: https://doi.org/10.1111/1751-7915.14072, doi:10.1111/1751-7915.14072. This article has 56 citations and is from a peer-reviewed journal.

16. (maury2005microbialisoprenoidproduction pages 13-14): Jérôme Maury, Mohammad A. Asadollahi, Kasper Møller, Anthony Clark, and Jens Nielsen. Microbial isoprenoid production: an example of green chemistry through metabolic engineering. Advances in biochemical engineering/biotechnology, 100:19-51, Jul 2005. URL: https://doi.org/10.1007/b136410, doi:10.1007/b136410. This article has 174 citations.

## Artifacts

- [Edison artifact artifact-00](ERG19-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](ERG19-deep-research-falcon_artifacts/artifact-01.md)
![## Context ID: pqac-00000017 Figure 1 from the document depicts the ergosterol biosynthetic pathway in *S. cerevisiae*, organized into color-coded modules repre](ERG19-deep-research-falcon_artifacts/image-1.png)

## Citations

1. cao2020harnessingsuborganellemetabolism pages 1-2
2. benveniste2002sterolmetabolism pages 4-7
3. hu2019effectsongene pages 12-13
4. jorda2020regulationofergosterol pages 1-3
5. garay2026themevalonatepathway pages 12-13
6. li2024yeastmetabolismadaptation pages 1-2
7. lu2022enhancingfluxesthrough pages 1-2
8. sun2019mevalonatediphosphatedecarboxylase pages 1-2
9. maury2005microbialisoprenoidproduction pages 9-12
10. jorda2020regulationofergosterol pages 3-4
11. maury2005microbialisoprenoidproduction pages 7-9
12. jorda2020regulationofergosterol pages 4-6
13. lu2022enhancingfluxesthrough pages 10-12
14. maury2005microbialisoprenoidproduction pages 13-14
15. https://doi.org/10.1038/s41467-024-54298-8
16. https://doi.org/10.1111/1751-7915.14072
17. https://doi.org/10.1186/s12934-016-0622-4
18. https://doi.org/10.1199/tab.0004
19. https://doi.org/10.3390/genes11070795
20. https://doi.org/10.1007/b136410
21. https://doi.org/10.20944/preprints202605.0182.v1
22. https://doi.org/10.3389/fmicb.2019.01074
23. https://doi.org/10.1002/yea.3452
24. https://doi.org/10.1016/j.synbio.2020.06.005
25. https://doi.org/10.3390/microorganisms7090342
26. https://doi.org/10.1021/acschembio.9b00322
27. https://doi.org/10.1199/tab.0004,
28. https://doi.org/10.1007/b136410,
29. https://doi.org/10.3390/genes11070795,
30. https://doi.org/10.3389/fmicb.2019.01074,
31. https://doi.org/10.20944/preprints202605.0182.v1,
32. https://doi.org/10.1002/yea.3452,
33. https://doi.org/10.1016/j.synbio.2020.06.005,
34. https://doi.org/10.3390/microorganisms7090342,
35. https://doi.org/10.1038/s41467-024-54298-8,
36. https://doi.org/10.1111/1751-7915.14072,