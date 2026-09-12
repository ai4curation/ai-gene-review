---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-10T14:48:49.312546'
end_time: '2026-09-10T14:55:52.747425'
duration_seconds: 423.44
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: DROME
  gene_id: hbt
  gene_symbol: hbt
  uniprot_accession: Q9VK03
  protein_description: 'SubName: Full=Headbutt, isoform D {ECO:0000313|EMBL:AAF53281.2};'
  gene_info: Name=hbt {ECO:0000313|EMBL:AAF53281.2, ECO:0000313|FlyBase:FBgn0264308};
    Synonyms=CG15639 {ECO:0000313|EMBL:AAF53281.2}, CG16970 {ECO:0000313|EMBL:AAF53281.2},
    Dmel\CG43778 {ECO:0000313|EMBL:AAF53281.2}, FBgn 32504 {ECO:0000313|EMBL:AAF53281.2};
    ORFNames=CG43778 {ECO:0000313|EMBL:AAF53281.2, ECO:0000313|FlyBase:FBgn0264308},
    Dmel_CG43778 {ECO:0000313|EMBL:AAF53281.2};
  organism_full: Drosophila melanogaster (Fruit fly).
  protein_family: Not specified in UniProt
  protein_domains: Rost. (IPR049352); Rost (PF21534)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 9
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: hbt-deep-research-falcon_artifacts/artifact-00.md
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
- **UniProt Accession:** Q9VK03
- **Protein Description:** SubName: Full=Headbutt, isoform D {ECO:0000313|EMBL:AAF53281.2};
- **Gene Information:** Name=hbt {ECO:0000313|EMBL:AAF53281.2, ECO:0000313|FlyBase:FBgn0264308}; Synonyms=CG15639 {ECO:0000313|EMBL:AAF53281.2}, CG16970 {ECO:0000313|EMBL:AAF53281.2}, Dmel\CG43778 {ECO:0000313|EMBL:AAF53281.2}, FBgn 32504 {ECO:0000313|EMBL:AAF53281.2}; ORFNames=CG43778 {ECO:0000313|EMBL:AAF53281.2, ECO:0000313|FlyBase:FBgn0264308}, Dmel_CG43778 {ECO:0000313|EMBL:AAF53281.2};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** Rost. (IPR049352); Rost (PF21534)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "hbt" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'hbt' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **hbt** (gene ID: hbt, UniProt: Q9VK03) in DROME.

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
- **UniProt Accession:** Q9VK03
- **Protein Description:** SubName: Full=Headbutt, isoform D {ECO:0000313|EMBL:AAF53281.2};
- **Gene Information:** Name=hbt {ECO:0000313|EMBL:AAF53281.2, ECO:0000313|FlyBase:FBgn0264308}; Synonyms=CG15639 {ECO:0000313|EMBL:AAF53281.2}, CG16970 {ECO:0000313|EMBL:AAF53281.2}, Dmel\CG43778 {ECO:0000313|EMBL:AAF53281.2}, FBgn 32504 {ECO:0000313|EMBL:AAF53281.2}; ORFNames=CG43778 {ECO:0000313|EMBL:AAF53281.2, ECO:0000313|FlyBase:FBgn0264308}, Dmel_CG43778 {ECO:0000313|EMBL:AAF53281.2};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** Rost. (IPR049352); Rost (PF21534)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "hbt" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'hbt' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **hbt** (gene ID: hbt, UniProt: Q9VK03) in DROME.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Functional annotation report: *Drosophila melanogaster hbt* (Q9VK03)

## Executive conclusion

The target is correctly identified as *Drosophila melanogaster* **headbutt** (*hbt*; UniProt Q9VK03; FlyBase FBgn0264308), not an identically abbreviated gene from another organism. However, **the gene symbol “hbt” is ambiguous and literature is limited for this specific protein**. In particular, Arabidopsis *hbt/HOBBIT* encodes a CDC27-related anaphase-promoting-complex component and is unrelated to Q9VK03; papers about “head-butt” behavior are also irrelevant.

For Q9VK03 itself, the available annotation supports a Rost-domain-containing protein associated by a 2014 primary study with cell death and developmental pattern repair. Nevertheless, the retrieved evidence does **not** establish a biochemical activity, direct binding partner, substrate, precise signaling position, or subcellular localization. No gene-specific mechanistic developments from 2023–2024 were found. Therefore, the scientifically defensible primary annotation is: **a poorly characterized, non-enzymatically annotated Drosophila protein implicated genetically in cell-death-dependent developmental pattern repair, with its immediate molecular mechanism and site of action unresolved**.

## 1. Identity verification

The supplied UniProt record identifies Q9VK03 as Headbutt isoform D from *D. melanogaster*, encoded by *hbt*. Historical or merged identifiers include **CG15639, CG16970, CG43778/Dmel\CG43778**, and FlyBase **FBgn0264308**. These identifiers were used in exact literature searches.

The supplied domain calls—InterPro **IPR049352 (Rost.)** and Pfam **PF21534 (Rost)**—are internally consistent with one another. However, neither establishes a recognized enzyme class or broadly characterized protein family. A domain match should consequently be treated as a sequence-based structural/evolutionary annotation, not evidence of catalytic activity or a defined pathway role.

The most important symbol collision is Arabidopsis *hbt/HOBBIT*, a CDC27 homolog. It must not be used to annotate Drosophila Q9VK03. Likewise, search results in which “head butt” denotes an aggressive behavior do not concern the gene.

## 2. Literature base and evidence quality

The directly relevant primary publication identified was:

- Tanaka KM, Takahashi A, Fuse N, Takano-Shimizu-Kouno T. **“A novel cell death gene acts to repair patterning defects in *Drosophila melanogaster*.”** *Genetics* (2014). DOI: [10.1534/genetics.114.163337](https://doi.org/10.1534/genetics.114.163337). Published June 2014.

The article’s title associates the newly characterized gene with cell death and repair of developmental patterning defects. Unfortunately, its full text was unobtainable through the available retrieval system. Accordingly, allele-specific results, rescue experiments, expression patterns, epistasis, cell autonomy, penetrance, and quantitative phenotypes could not be audited and are not asserted here.

A later peer-reviewed modeling study examined apoptosis-mediated size control in the Drosophila embryonic epidermis. It showed that passive mechanics can reproduce much of posterior-compartment size robustness, but spatially asymmetric cell death requires patterned cellular properties or signaling. This provides relevant biological context, not direct proof that Hbt is a component of the modeled mechanism. (kursawe2015capabilitiesandlimitations pages 19-20, kursawe2015capabilitiesandlimitations pages 1-2)

| Annotation | Evidence level | Conclusion / limitation |
|---|---|---|
| **Identity** | **High — supplied UniProt record** | Q9VK03 is *Drosophila melanogaster* Headbutt isoform D, encoded by **hbt** (FBgn0264308); aliases include **CG15639, CG16970, and CG43778**. Arabidopsis **hbt/HOBBIT** (a CDC27 homolog) and behavioral uses of “head butt” are unrelated and excluded. |
| **Domain/family** | **Moderate — supplied computational annotations** | The protein contains a Rost-domain assignment (InterPro IPR049352; Pfam PF21534). No protein family, catalytic activity, ligand, or biochemical mechanism was established by the retrieved literature; the domain name alone is insufficient for functional inference. |
| **Molecular function** | **Low / unresolved** | No retrieved experiment demonstrated enzymatic, transporter, receptor, structural, or adaptor activity for Q9VK03. Tanaka et al. (2014; DOI: [10.1534/genetics.114.163337](https://doi.org/10.1534/genetics.114.163337)) is the directly relevant study identified, but its full text was unobtainable, preventing verification of detailed molecular claims. |
| **Biological process** | **Limited direct evidence** | The title of Tanaka et al. associates the gene with cell death and repair of developmental patterning defects, but exact experiments and conclusions could not be audited from full text. Separately, Drosophila embryonic epidermal size repair is known to depend substantially on regulated cell removal/apoptosis rather than proliferation, but this is pathway context—not proof of an **hbt** role (kursawe2015capabilitiesandlimitations pages 1-2, kursawe2015capabilitiesandlimitations pages 2-4). |
| **Localization** | **Unknown** | No validated subcellular localization, secretion, membrane topology, or tissue-specific site of protein action was retrieved. The developmental tissue examined in related pattern-repair work is embryonic epidermis, but it must not be assigned as Q9VK03 protein localization without direct evidence. |
| **Pathway** | **Contextual only** | EGFR/Spitz and Wingless/Wnt signaling antagonistically regulate apoptosis during Drosophila embryonic epidermal pattern repair; wild-type apoptosis was reported to differ by nearly **40-fold** between regions (kursawe2015capabilitiesandlimitations pages 2-4). No retrieved evidence places Hbt directly upstream, downstream, or within either pathway. |
| **Phenotype** | **Potentially direct but incompletely verifiable** | Tanaka et al.’s title supports an association with cell death-dependent repair of patterning defects, but allele, tissue, penetrance, rescue, and epistasis details remain unverified. Contextually, altered proliferation changed posterior-compartment cell number by **>30%** or **−25%** with relatively small size effects, while apoptosis blockade produced about **10% compartment shrinkage**; these values are not **hbt**-specific (kursawe2015capabilitiesandlimitations pages 2-4). |
| **Recent literature/applications** | **No gene-specific evidence found** | No 2023–2024 mechanistic study, validated application, clinical relevance, biotechnology implementation, or disease model specific to **hbt/Q9VK03** was retrieved. The 2015 mechanical model concerns general apoptosis-mediated tissue-size control and explicitly cannot resolve gene-specific biochemical mechanisms (kursawe2015capabilitiesandlimitations pages 19-20, kursawe2015capabilitiesandlimitations pages 20-22). |


*Table: Evidence-strength assessment for Drosophila hbt/Q9VK03, separating supplied database annotations, directly identifiable literature, and non-gene-specific pathway context. It highlights that the protein’s molecular function and localization remain unresolved.*

## 3. Primary function

### Best-supported functional description

The strongest cautious description is that *hbt* is **genetically implicated in regulated cell death used to correct developmental patterning defects**. This places its known phenotype in developmental tissue homeostasis rather than metabolism, transport, or extracellular structure.

There is no retrieved evidence that Q9VK03 is:

- an enzyme with a defined reaction or substrate;
- a transporter with a known cargo;
- a receptor or secreted ligand;
- a cytoskeletal or extracellular structural protein; or
- an adaptor with experimentally demonstrated partners.

Thus, assigning catalytic activity, substrate specificity, receptor status, or an adaptor mechanism would be speculative. The Rost/PF21534 annotation alone does not resolve these questions.

### Relationship to apoptosis and pattern repair

In the broader Drosophila embryonic epidermis system, changing proliferation does not lead to proportional changes in final compartment size: an extra division increased posterior-compartment cell number by more than 30%, while loss of one division reduced it by approximately 25%, yet compartment-size changes were comparatively small. These findings support compensation through regulated cell removal rather than simple proliferation matching. (kursawe2015capabilitiesandlimitations pages 2-4)

Cell death in this tissue is strongly spatially patterned. TUNEL-positive events were reported to be almost 40-fold more frequent in the anterior/front half than the posterior/back half of the compartment. Blocking apoptosis with p35 in a Cyclin-E perturbation produced nearly 10% compartment shrinkage. EGFR signaling through the Spitz ligand and Wingless/Wnt signaling were implicated as antagonistic regulators of this repair-associated apoptosis. (kursawe2015capabilitiesandlimitations pages 2-4)

These numerical findings explain the developmental process into which the 2014 *hbt* study may fit, but they are **not measurements of an *hbt* mutant** and should not be transferred to Q9VK03 as gene-specific statistics.

## 4. Biological processes and pathway placement

The plausible high-level process is **developmental pattern correction through regulated cell death**, potentially involving epithelial compartment-size homeostasis. The broader system integrates:

1. regional patterning information;
2. EGFR/Spitz and Wingless/Wnt survival–death signals;
3. apoptosis or cell extrusion;
4. epithelial tension, cell area, and actomyosin mechanics; and
5. preservation of tissue size despite altered cell number.

Mechanical modeling indicates that passive forces may explain much of final size robustness, but not the observed regional asymmetry of apoptosis. Spatially patterned cell growth, apical tension, contractility, or intercellular signaling is needed to reproduce that asymmetry. (kursawe2015capabilitiesandlimitations pages 19-20, kursawe2015capabilitiesandlimitations pages 4-5)

The model treats apoptosis and delamination as cell-removal events rather than resolving molecular execution. It therefore cannot identify Hbt’s biochemical action, and it cannot directly simulate apoptosis-deficient p35 conditions. (kursawe2015capabilitiesandlimitations pages 5-7, kursawe2015capabilitiesandlimitations pages 20-22)

No retrieved experiment establishes whether Hbt acts upstream or downstream of EGFR, Wingless, caspases, or mechanical stress sensing. Those pathway placements remain hypotheses requiring direct genetic epistasis and molecular interaction data.

## 5. Cellular and tissue localization

A validated **subcellular localization is presently unresolved**. No retrieved evidence demonstrates nuclear, cytosolic, plasma-membrane, organellar, extracellular, or junctional localization for Q9VK03. Likewise, no signal peptide, transmembrane topology, or secretion mechanism can be concluded from the evidence reviewed.

The embryonic epidermis is the developmental tissue relevant to the contextual pattern-repair literature, but this must not be conflated with direct localization of the Hbt protein. Establishing the functional site would require an endogenous tagged allele or a validated antibody, colocalization with apoptotic and junctional markers, and rescue by tissue-specific expression.

## 6. Recent developments, applications, and real-world implementation

No 2023–2024 publication providing a gene-specific biochemical mechanism, structure, localization, or validated interaction for *hbt/Q9VK03* was retrieved. The absence of recent papers is itself important: this remains a sparsely characterized Drosophila gene rather than a mature pathway component with a settled molecular model.

No clinical application, therapeutic program, diagnostic use, agricultural implementation, or biotechnology product specific to Hbt was identified. Its current value is principally as a **basic-research target** for studying how programmed cell death contributes to developmental robustness. Potential applications are experimental—genetic screens of apoptosis, epithelial mechanics, and pattern repair—not established real-world implementations.

## 7. Expert assessment and annotation confidence

The evidence supports three confidence tiers:

- **High confidence:** identity as Drosophila *hbt*/Headbutt Q9VK03 and exclusion of Arabidopsis HOBBIT and behavioral “head butt” literature.
- **Moderate-to-low confidence:** association with developmental cell death and pattern repair, based on the directly relevant 2014 publication’s bibliographic identity and title, without retrievable full-text verification.
- **Unresolved:** immediate molecular activity, protein partners, cell autonomy, pathway order, substrate or ligand, and subcellular localization.

The pathway-level literature supports apoptosis as an active size-control mechanism and shows that mechanics alone cannot explain spatially patterned death. However, authoritative interpretation requires keeping this general evidence separate from *hbt*-specific evidence. (kursawe2015capabilitiesandlimitations pages 1-2, kursawe2015capabilitiesandlimitations pages 20-22)

## 8. Recommended experiments for definitive annotation

The most informative next steps would be:

1. **Endogenous CRISPR tagging** of Q9VK03, followed by live imaging and immunostaining in embryos.
2. **Null-allele and isoform-specific rescue**, distinguishing isoform D from other transcripts.
3. **Tissue-specific mosaic analysis** to determine whether Hbt acts cell-autonomously in cells selected for death or non-autonomously in neighboring cells.
4. **Epistasis with EGFR/Spitz, Wingless/Wnt, and core apoptotic genes**, including caspase inhibition, to position Hbt in the pathway.
5. **Apoptosis measurements** using TUNEL and activated-caspase reporters, accompanied by compartment area, cell number, and spatial-distribution statistics.
6. **Affinity purification–mass spectrometry or proximity labeling** to identify interaction partners, followed by domain-deletion tests of the Rost/PF21534 region.
7. **Comparative sequence and structure prediction** across drosophilids to determine whether the Rost domain suggests conserved interfaces, while avoiding biochemical annotation from homology alone.

## Overall annotation

**Q9VK03/Hbt is a poorly characterized Rost-domain-containing Drosophila protein genetically associated with cell death-mediated repair of developmental patterning defects. Its precise biochemical function, direct pathway position, and subcellular localization remain unknown.** The quantitative apoptosis, EGFR/Wingless, and epithelial-mechanics literature supplies a plausible developmental framework, but it does not yet provide a direct molecular mechanism for Hbt.

References

1. (kursawe2015capabilitiesandlimitations pages 19-20): Jochen Kursawe, Pavel A. Brodskiy, Jeremiah J. Zartman, Ruth E. Baker, and Alexander G. Fletcher. Capabilities and limitations of tissue size control through passive mechanical forces. Dec 2015. URL: https://doi.org/10.1371/journal.pcbi.1004679, doi:10.1371/journal.pcbi.1004679. This article has 44 citations and is from a highest quality peer-reviewed journal.

2. (kursawe2015capabilitiesandlimitations pages 1-2): Jochen Kursawe, Pavel A. Brodskiy, Jeremiah J. Zartman, Ruth E. Baker, and Alexander G. Fletcher. Capabilities and limitations of tissue size control through passive mechanical forces. Dec 2015. URL: https://doi.org/10.1371/journal.pcbi.1004679, doi:10.1371/journal.pcbi.1004679. This article has 44 citations and is from a highest quality peer-reviewed journal.

3. (kursawe2015capabilitiesandlimitations pages 2-4): Jochen Kursawe, Pavel A. Brodskiy, Jeremiah J. Zartman, Ruth E. Baker, and Alexander G. Fletcher. Capabilities and limitations of tissue size control through passive mechanical forces. Dec 2015. URL: https://doi.org/10.1371/journal.pcbi.1004679, doi:10.1371/journal.pcbi.1004679. This article has 44 citations and is from a highest quality peer-reviewed journal.

4. (kursawe2015capabilitiesandlimitations pages 20-22): Jochen Kursawe, Pavel A. Brodskiy, Jeremiah J. Zartman, Ruth E. Baker, and Alexander G. Fletcher. Capabilities and limitations of tissue size control through passive mechanical forces. Dec 2015. URL: https://doi.org/10.1371/journal.pcbi.1004679, doi:10.1371/journal.pcbi.1004679. This article has 44 citations and is from a highest quality peer-reviewed journal.

5. (kursawe2015capabilitiesandlimitations pages 4-5): Jochen Kursawe, Pavel A. Brodskiy, Jeremiah J. Zartman, Ruth E. Baker, and Alexander G. Fletcher. Capabilities and limitations of tissue size control through passive mechanical forces. Dec 2015. URL: https://doi.org/10.1371/journal.pcbi.1004679, doi:10.1371/journal.pcbi.1004679. This article has 44 citations and is from a highest quality peer-reviewed journal.

6. (kursawe2015capabilitiesandlimitations pages 5-7): Jochen Kursawe, Pavel A. Brodskiy, Jeremiah J. Zartman, Ruth E. Baker, and Alexander G. Fletcher. Capabilities and limitations of tissue size control through passive mechanical forces. Dec 2015. URL: https://doi.org/10.1371/journal.pcbi.1004679, doi:10.1371/journal.pcbi.1004679. This article has 44 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](hbt-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. kursawe2015capabilitiesandlimitations pages 2-4
2. kursawe2015capabilitiesandlimitations pages 19-20
3. kursawe2015capabilitiesandlimitations pages 1-2
4. kursawe2015capabilitiesandlimitations pages 20-22
5. kursawe2015capabilitiesandlimitations pages 4-5
6. kursawe2015capabilitiesandlimitations pages 5-7
7. 10.1534/genetics.114.163337
8. https://doi.org/10.1534/genetics.114.163337
9. https://doi.org/10.1371/journal.pcbi.1004679,