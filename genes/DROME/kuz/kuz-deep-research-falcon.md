---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-30T05:16:21.784407'
end_time: '2026-09-30T05:31:22.963240'
duration_seconds: 901.18
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: DROME
  gene_id: kuz
  gene_symbol: kuz
  uniprot_accession: A8DZ02
  protein_description: 'RecName: Full=ADAM10 endopeptidase {ECO:0000256|ARBA:ARBA00012332};
    EC=3.4.24.81 {ECO:0000256|ARBA:ARBA00012332};'
  gene_info: Name=kuz {ECO:0000313|EMBL:ABV53680.2, ECO:0000313|FlyBase:FBgn0259984};
    Synonyms=11410 {ECO:0000313|EMBL:ABV53680.2}, 34Da {ECO:0000313|EMBL:ABV53680.2},
    ADAM10 {ECO:0000313|EMBL:ABV53680.2}, BG:DS07660.3 {ECO:0000313|EMBL:ABV53680.2},
    br38 {ECO:0000313|EMBL:ABV53680.2}, CT22079 {ECO:0000313|EMBL:ABV53680.2}, Dmel\CG7147
    {ECO:0000313|EMBL:ABV53680.2}, GS11410 {ECO:0000313|EMBL:ABV53680.2}, KUZ {ECO:0000313|EMBL:ABV53680.2},
    Kuz {ECO:0000313|EMBL:ABV53680.2}, l(2)03782 {ECO:0000313|EMBL:ABV53680.2}, l(2)34Da
    {ECO:0000313|EMBL:ABV53680.2}, l(2)br38 {ECO:0000313|EMBL:ABV53680.2}, l(2)c00136
    {ECO:0000313|EMBL:ABV53680.2}, l(2)k01403 {ECO:0000313|EMBL:ABV53680.2}, l34Da
    {ECO:0000313|EMBL:ABV53680.2}, soy nut {ECO:0000313|EMBL:ABV53680.2}; ORFNames=CG7147
    {ECO:0000313|EMBL:ABV53680.2, ECO:0000313|FlyBase:FBgn0259984}, Dmel_CG7147 {ECO:0000313|EMBL:ABV53680.2};
  organism_full: Drosophila melanogaster (Fruit fly).
  protein_family: Not specified in UniProt
  protein_domains: ADAM10_ADAM17. (IPR034025); ADAM10_Cys-rich. (IPR049038); ADAM_Metalloproteinase.
    (IPR051489); Disintegrin_dom. (IPR001762); Disintegrin_dom_sf. (IPR036436)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 29
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: kuz-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: kuz-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** A8DZ02
- **Protein Description:** RecName: Full=ADAM10 endopeptidase {ECO:0000256|ARBA:ARBA00012332}; EC=3.4.24.81 {ECO:0000256|ARBA:ARBA00012332};
- **Gene Information:** Name=kuz {ECO:0000313|EMBL:ABV53680.2, ECO:0000313|FlyBase:FBgn0259984}; Synonyms=11410 {ECO:0000313|EMBL:ABV53680.2}, 34Da {ECO:0000313|EMBL:ABV53680.2}, ADAM10 {ECO:0000313|EMBL:ABV53680.2}, BG:DS07660.3 {ECO:0000313|EMBL:ABV53680.2}, br38 {ECO:0000313|EMBL:ABV53680.2}, CT22079 {ECO:0000313|EMBL:ABV53680.2}, Dmel\CG7147 {ECO:0000313|EMBL:ABV53680.2}, GS11410 {ECO:0000313|EMBL:ABV53680.2}, KUZ {ECO:0000313|EMBL:ABV53680.2}, Kuz {ECO:0000313|EMBL:ABV53680.2}, l(2)03782 {ECO:0000313|EMBL:ABV53680.2}, l(2)34Da {ECO:0000313|EMBL:ABV53680.2}, l(2)br38 {ECO:0000313|EMBL:ABV53680.2}, l(2)c00136 {ECO:0000313|EMBL:ABV53680.2}, l(2)k01403 {ECO:0000313|EMBL:ABV53680.2}, l34Da {ECO:0000313|EMBL:ABV53680.2}, soy nut {ECO:0000313|EMBL:ABV53680.2}; ORFNames=CG7147 {ECO:0000313|EMBL:ABV53680.2, ECO:0000313|FlyBase:FBgn0259984}, Dmel_CG7147 {ECO:0000313|EMBL:ABV53680.2};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** ADAM10_ADAM17. (IPR034025); ADAM10_Cys-rich. (IPR049038); ADAM_Metalloproteinase. (IPR051489); Disintegrin_dom. (IPR001762); Disintegrin_dom_sf. (IPR036436)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "kuz" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'kuz' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **kuz** (gene ID: kuz, UniProt: A8DZ02) in DROME.

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
- **UniProt Accession:** A8DZ02
- **Protein Description:** RecName: Full=ADAM10 endopeptidase {ECO:0000256|ARBA:ARBA00012332}; EC=3.4.24.81 {ECO:0000256|ARBA:ARBA00012332};
- **Gene Information:** Name=kuz {ECO:0000313|EMBL:ABV53680.2, ECO:0000313|FlyBase:FBgn0259984}; Synonyms=11410 {ECO:0000313|EMBL:ABV53680.2}, 34Da {ECO:0000313|EMBL:ABV53680.2}, ADAM10 {ECO:0000313|EMBL:ABV53680.2}, BG:DS07660.3 {ECO:0000313|EMBL:ABV53680.2}, br38 {ECO:0000313|EMBL:ABV53680.2}, CT22079 {ECO:0000313|EMBL:ABV53680.2}, Dmel\CG7147 {ECO:0000313|EMBL:ABV53680.2}, GS11410 {ECO:0000313|EMBL:ABV53680.2}, KUZ {ECO:0000313|EMBL:ABV53680.2}, Kuz {ECO:0000313|EMBL:ABV53680.2}, l(2)03782 {ECO:0000313|EMBL:ABV53680.2}, l(2)34Da {ECO:0000313|EMBL:ABV53680.2}, l(2)br38 {ECO:0000313|EMBL:ABV53680.2}, l(2)c00136 {ECO:0000313|EMBL:ABV53680.2}, l(2)k01403 {ECO:0000313|EMBL:ABV53680.2}, l34Da {ECO:0000313|EMBL:ABV53680.2}, soy nut {ECO:0000313|EMBL:ABV53680.2}; ORFNames=CG7147 {ECO:0000313|EMBL:ABV53680.2, ECO:0000313|FlyBase:FBgn0259984}, Dmel_CG7147 {ECO:0000313|EMBL:ABV53680.2};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** ADAM10_ADAM17. (IPR034025); ADAM10_Cys-rich. (IPR049038); ADAM_Metalloproteinase. (IPR051489); Disintegrin_dom. (IPR001762); Disintegrin_dom_sf. (IPR036436)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "kuz" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'kuz' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **kuz** (gene ID: kuz, UniProt: A8DZ02) in DROME.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Comprehensive Research Report: Kuzbanian (kuz) Gene in Drosophila melanogaster

## Gene Identity and Overview

The *kuzbanian* (*kuz*) gene in *Drosophila melanogaster* (UniProt: A8DZ02) encodes an ADAM10 metalloproteinase, representing the sole Drosophila ortholog of mammalian ADAM10 (baker2024aninvivo pages 13-17, wang2023aconservedmechanism pages 5-7). This gene was historically named after its loss-of-function phenotype and has multiple synonyms including ADAM10, CG7147, and several lethal allele designations reflecting its essential developmental functions. The protein belongs to the ADAM (A Disintegrin And Metalloproteinase) family and contains characteristic domains including the metalloproteinase domain, disintegrin domain, and cysteine-rich region (hunter2020phosphorylationandproteolytic pages 63-65, sanhueza2025theslit–robosignalling pages 3-4).

## Molecular Function and Enzymatic Activity

### Catalytic Activity

Kuzbanian functions as a zinc-dependent metalloproteinase that catalyzes the proteolytic cleavage of transmembrane proteins through peptide bond hydrolysis (hunter2020phosphorylationandproteolytic pages 63-65, wang2023aconservedmechanism pages 5-7). As an ADAM-family enzyme, Kuz performs regulated ectodomain shedding, a process whereby it cleaves the extracellular domains of substrate proteins near the plasma membrane, releasing soluble ectodomains and leaving membrane-bound C-terminal fragments (baker2024aninvivo pages 13-17, puschmann2026scube2primesdispatched pages 6-10). The enzyme is classified within the matrix metalloproteinase (MMP) superfamily and requires zinc coordination in its catalytic active site for proteolytic activity (sanhueza2025theslit–robosignalling pages 3-4, wang2023aconservedmechanism pages 5-7).

### Substrate Specificity

Recent evidence from 2024 suggests that Kuzbanian exhibits relatively broad substrate tolerance, with specificity determined primarily by mechanical accessibility and contextual factors rather than strict sequence requirements (baker2024aninvivo pages 13-17, baker2024aninvivo pages 10-13). A comprehensive in vivo screen demonstrated that Kuz can cleave structurally diverse proteolytic switch domains when they are mechanically exposed, suggesting that substrate recognition depends on force-induced conformational changes that expose otherwise occluded cleavage sites (baker2024aninvivo pages 13-17). This mechanism is analogous to ADAM10-mediated cleavage of von Willebrand factor, where torsional strain exposes the cleavage site (baker2024aninvivo pages 13-17).

### Major Substrates

| Substrate Name | Cleavage Site/Type | Biological Function | Key Citations |
|---|---|---|---|
| **Notch receptor** | Kuz cleaves the membrane-proximal extracellular **S2 site** after ligand-generated force exposes it, shedding the Notch extracellular domain and producing membrane-bound NEXT. | This is Kuz’s best-established primary function. S2 cleavage permits subsequent γ-secretase cleavage, release of NICD, and Notch-dependent transcription; it supports lateral inhibition, neurogenesis, axon patterning, and wing dorsoventral-boundary development. | (wang2023aconservedmechanism pages 1-4, baker2024aninvivo pages 30-35, hunter2020phosphorylationandproteolytic pages 63-65, hunter2020phosphorylationandproteolytic pages 113-114) |
| **Roundabout/Robo1 receptor** | Proteolytic processing of the **extracellular domain**; the precise Kuz cleavage bond has not been mapped in the cited sources. | Robo processing enables appropriate Slit–Robo signaling and repulsive responses during embryonic CNS midline guidance; Kuz loss therefore disrupts axon repulsion and axonal patterning. | (sanhueza2025theslit–robosignalling pages 3-4, kannan2018tyrosinephosphorylationand pages 30-33) |
| **Delta Notch ligand** | Kuz-dependent **juxtamembrane ligand processing/ectodomain shedding** is reported in the Drosophila literature; the exact cleavage residue is not established by the available excerpts. | Delta processing can regulate ligand abundance and activity and releases its extracellular domain. Evidence is direct for Delta, whereas equivalent Kuz-dependent cleavage of Serrate is not established by the sources reviewed. | (hunter2020phosphorylationandproteolytic pages 59-60, hunter2020phosphorylationandproteolytic pages 58-59) |
| **APPL (Drosophila amyloid precursor protein-like protein)** | **α-secretase-like ectodomain shedding**, generating a soluble N-terminal APPL fragment and leaving a membrane-associated C-terminal fragment; no exact residue-level site is given. | Kuz-mediated APPL processing is considered non-amyloidogenic relative to dBACE cleavage and regulates the balance between full-length and soluble APPL. Genetic manipulation of Kuz/APPL processing affects visual working memory and age-related memory decline. | (rieche2018drosophilafulllengthamyloid pages 1-3, rieche2018drosophilafulllengthamyloid pages 7-8, rieche2018drosophilafulllengthamyloid pages 3-4) |
| **Sonic Hedgehog (Shh; mammalian ADAM10 evidence)** | Mammalian ADAM10 removes lipid-bearing terminal peptide regions from membrane-associated, dually lipidated Shh, generating soluble, truncated Shh. **This is ortholog-based evidence, not direct demonstration that Drosophila Kuz cleaves Hedgehog.** | ADAM10 cooperates with Dispatched and SCUBE2 to promote Shh release from the plasma membrane; activity depends strongly on substrate lipidation and membrane context. This supports a plausible conserved sheddase capability but should not be annotated as a confirmed endogenous Kuz substrate without Drosophila-specific validation. | (puschmann2026scube2primesdispatched pages 6-10) |


*Table: This table summarizes experimentally supported and ortholog-inferred Kuzbanian/ADAM10 substrates, their cleavage modes, and their biological consequences. It distinguishes confirmed Drosophila substrates from mammalian ADAM10 evidence requiring fly-specific validation.*

The primary and most extensively characterized substrate of Kuzbanian is the Notch receptor, where Kuz performs the critical S2 cleavage (wang2023aconservedmechanism pages 1-4, baker2024aninvivo pages 30-35, hunter2020phosphorylationandproteolytic pages 63-65). Following ligand binding and force generation through ligand endocytosis, Kuz cleaves Notch at the membrane-proximal extracellular S2 site, shedding the Notch extracellular domain and producing a membrane-bound intermediate called NEXT (Notch External Truncation) (hunter2020phosphorylationandproteolytic pages 63-65). This cleavage is essential for subsequent γ-secretase processing and release of the Notch intracellular domain (NICD) for transcriptional activation.

Beyond Notch, Kuzbanian cleaves the Roundabout (Robo) axon guidance receptor, processing its extracellular domain to enable proper Slit–Robo signaling during midline axon guidance (sanhueza2025theslit–robosignalling pages 3-4, kannan2018tyrosinephosphorylationand pages 30-33). The Delta Notch ligand is also reported to undergo Kuz-dependent proteolytic processing, as documented in the literature (hunter2020phosphorylationandproteolytic pages 59-60), though the precise biological consequences require further investigation.

Recent work from 2018 established that Kuzbanian processes APPL, the Drosophila amyloid precursor protein-like protein, through α-secretase-like ectodomain shedding (rieche2018drosophilafulllengthamyloid pages 1-3, rieche2018drosophilafulllengthamyloid pages 7-8, rieche2018drosophilafulllengthamyloid pages 3-4). This cleavage generates soluble N-terminal APPL fragments and represents a non-amyloidogenic processing pathway, in contrast to the β-secretase dBACE pathway that produces neurotoxic amyloid-like peptides (rieche2018drosophilafulllengthamyloid pages 1-3).

Evidence from mammalian ADAM10 studies published in 2026 suggests that the ortholog can cleave lipidated Sonic Hedgehog (Shh), removing lipid-bearing terminal peptides to generate soluble Shh (puschmann2026scube2primesdispatched pages 6-10). While this function has been examined in the Drosophila eye where Kuz depletion affects Hedgehog-dependent development (puschmann2026scube2primesdispatched pages 6-10), direct demonstration of endogenous Drosophila Hedgehog cleavage by Kuz requires further validation.

## Subcellular Localization

Kuzbanian is characterized as a cell-surface and plasma membrane-associated metalloproteinase (puschmann2026scube2primesdispatched pages 6-10, schnute2022ubiquitylationisrequired pages 1-2). The enzyme functions at the membrane-bound stage of substrate processing, acting during ligand-receptor interactions at the plasma membrane (seib2021theroleof pages 6-8). Recent evidence suggests that Notch processing may occur in endosomal compartments following receptor internalization, with Kuz-dependent cleavage potentially taking place in Rab5-positive early endocytic vesicles (steinbuck2018areviewof pages 4-5). However, the precise subcellular compartmentalization of Kuz itself—whether it functions exclusively at the plasma membrane or also traffics through endosomal compartments—remains incompletely resolved in the literature (steinbuck2018areviewof pages 4-5, hunter2020phosphorylationandproteolytic pages 63-65). The current evidence consistently supports a membrane-associated localization where Kuz accesses its transmembrane protein substrates.

## Signaling Pathways and Biological Functions

| Pathway/Process Name | Kuz Role/Function | Developmental Context | Key Evidence |
|---|---|---|---|
| Canonical Notch signaling | Kuz acts as the ADAM-family S2 protease. Ligand-generated force exposes the membrane-proximal S2 site; Kuz sheds the Notch extracellular domain and generates NEXT, enabling γ-secretase cleavage, NICD release, and target-gene transcription. | Contact-dependent cell-fate decisions across developing tissues | Kuz depletion prevents ligand-induced Notch activation, while reduced *kuz* expression causes uncleaved, inactive Notch to accumulate. Accessibility and mechanical exposure, rather than a strict sequence motif, appear to govern cleavage. (baker2024aninvivo pages 13-17, wang2023aconservedmechanism pages 1-4, baker2024aninvivo pages 30-35, wang2023aconservedmechanism pages 5-7) |
| Slit–Robo axon guidance | Kuz proteolytically processes the extracellular domain of Robo1, enabling an appropriate repulsive response to Slit; the exact cleavage bond remains unmapped. | Embryonic ventral nerve cord, CNS midline crossing, axon extension, and tract patterning | Studies identify Robo1 as a Kuz substrate and associate Kuz loss with defective midline repulsion, longitudinal tracts, and axonal extension. (sanhueza2025theslit–robosignalling pages 3-4, kannan2018tyrosinephosphorylationand pages 30-33) |
| Neurogenesis and lateral inhibition | By activating Notch through S2 cleavage, Kuz enables selected cells to suppress neural fate in neighboring cells and supports orderly neural cell-fate specification. | Embryonic nervous-system development | Genetic evidence links Kuz-dependent Notch proteolysis to lateral inhibition. Kuz loss produces neurogenic and axon-patterning defects, although some phenotypes may reflect cleavage of non-Notch substrates. (hunter2020phosphorylationandproteolytic pages 63-65, hunter2020phosphorylationandproteolytic pages 113-114, kannan2018tyrosinephosphorylationand pages 4-6) |
| Wing-disc dorsoventral patterning | Kuz is required in Notch signal-receiving cells for receptor cleavage and activation at the dorsoventral boundary. | Larval wing imaginal disc and prospective wing margin | Kuz knockdown abolishes endogenous Cut expression at the dorsoventral boundary and blocks engineered Notch-receptor responses to neighboring ligand-producing cells. (baker2024aninvivo pages 30-35) |
| Eye development | Kuz supports proteolytic signaling needed for eye-disc patterning. Notch is an established fly substrate; a proposed Hedgehog-release role relies partly on mammalian ADAM10 evidence and is not confirmed direct cleavage of Drosophila Hh. | Eye-disc morphogenetic-furrow progression, photoreceptor differentiation, and adult ommatidium formation | Eye-specific dominant-negative Kuz perturbs eye development. Mammalian ADAM10 releases lipidated Shh at the plasma membrane, but direct endogenous Kuz–Hh cleavage in flies requires validation. (puschmann2026scube2primesdispatched pages 6-10) |
| Memory and APPL processing | Kuz performs α-secretase-like ectodomain shedding of APPL, shifting APPL from its full-length membrane form toward soluble N-terminal products and away from the dBACE-associated amyloidogenic route. | Adult neural circuits controlling visual working memory and age-related memory maintenance | Genetic reduction of *kuz* increases full-length APPL and prevents age-related visual-memory decline, whereas neuronal Kuz overexpression impairs working memory; the exact cleavage residue remains unmapped. (rieche2018drosophilafulllengthamyloid pages 1-3, rieche2018drosophilafulllengthamyloid pages 7-8, rieche2018drosophilafulllengthamyloid pages 3-4, rieche2018drosophilafulllengthamyloid pages 5-6) |


*Table: This table summarizes the best-supported signaling and developmental roles of Drosophila Kuzbanian, distinguishing direct fly evidence from ortholog-based inference. It highlights Kuz’s primary function as the Notch S2 sheddase and its additional roles in axon guidance and APPL processing.*

### Canonical Notch Signaling Pathway

The primary and best-characterized function of Kuzbanian is its essential role in canonical Notch signaling (wang2023aconservedmechanism pages 1-4, wang2023aconservedmechanism pages 5-7, hunter2020phosphorylationandproteolytic pages 63-65). In this pathway, Kuz acts as the critical S2 protease that initiates receptor activation following ligand engagement. The current model, supported by research through 2024, indicates that ligand binding generates mechanical force through endocytosis, exposing the normally protected S2 cleavage site in the Notch Negative Regulatory Region (NRR) (wang2023aconservedmechanism pages 1-4, baker2024aninvivo pages 30-35). Kuz then sheds the extracellular domain, producing the NEXT intermediate that serves as the substrate for γ-secretase-mediated S3 cleavage (wang2023aconservedmechanism pages 1-4, wang2023aconservedmechanism pages 5-7). This sequential proteolysis releases NICD, which translocates to the nucleus and activates transcription of Notch target genes through the CSL/Suppressor of Hairless transcription factor complex (wang2023aconservedmechanism pages 1-4).

Studies from 2023 demonstrated that reduced *kuz* expression in tumor models leads to accumulation of uncleaved, inactive Notch, confirming that Kuz activity is rate-limiting for Notch pathway activation (wang2023aconservedmechanism pages 5-7). Loss of Kuz prevents ligand-induced receptor activation, as shown in 2024 experiments where Kuz knockdown abolished Notch-dependent gene expression at the wing disc dorsoventral boundary (baker2024aninvivo pages 30-35).

### Axon Guidance and Slit–Robo Signaling

Beyond Notch, Kuzbanian plays critical roles in nervous system development through its processing of the Robo receptor (kannan2018tyrosinephosphorylationand pages 30-33). Kuz-mediated cleavage of Robo1's extracellular domain is required for appropriate repulsive responses to the Slit guidance cue during embryonic CNS midline crossing (sanhueza2025theslit–robosignalling pages 3-4). Loss of Kuzbanian function produces defects in longitudinal axon tracts and midline repulsion, phenotypes consistent with disrupted Robo signaling (kannan2018tyrosinephosphorylationand pages 4-6). Work published in 2018 established that Kuz is required for axonal extension and proper patterning of motor axon trajectories, including the ISNb motor nerve pathway (kannan2018tyrosinephosphorylationand pages 30-33).

These axon guidance functions appear to be at least partially independent of Kuz's role in Notch processing, as Kuz cleaves multiple cell-surface receptors involved in axon patterning decisions (hunter2020phosphorylationandproteolytic pages 65-67, kannan2018tyrosinephosphorylationand pages 30-33). The enzyme has been implicated in processing ephrins and potentially other guidance receptors, although detailed characterization of these substrates remains incomplete (hunter2020phosphorylationandproteolytic pages 65-67).

### Neurogenesis and Lateral Inhibition

During Drosophila embryonic development, Kuzbanian-dependent Notch activation mediates lateral inhibition, the process whereby developing neural cells prevent neighboring cells from adopting the same neural fate (hunter2020phosphorylationandproteolytic pages 113-114). This function is essential for proper nervous system patterning, as loss of Kuz produces neurogenic phenotypes characteristic of disrupted Notch signaling (hunter2020phosphorylationandproteolytic pages 113-114). The requirement for Kuz in neurogenesis reflects its role in processing Notch during cell fate specification rather than representing an independent pathway.

### Imaginal Disc Development

In larval development, Kuzbanian is required for Notch-dependent patterning in multiple imaginal discs. Studies from 2024 demonstrated that Kuz function in the wing disc is essential for dorsoventral boundary formation and expression of the boundary marker Cut (baker2024aninvivo pages 30-35). Signal-receiving cells require Kuz activity for ligand-induced Notch activation, and Kuz knockdown eliminates endogenous Notch signaling at the wing margin (baker2024aninvivo pages 30-35).

In the eye disc, Kuz supports proper progression of the morphogenetic furrow and photoreceptor differentiation (puschmann2026scube2primesdispatched pages 6-10). Recent work using eye-specific dominant-negative Kuz demonstrated developmental defects affecting ommatidium formation, consistent with impaired Hedgehog and/or Notch signaling during eye development (puschmann2026scube2primesdispatched pages 6-10).

### Memory and APPL Processing

An emerging area of Kuzbanian research involves its role in adult brain function through APPL processing. Work published in 2018 established that Kuz performs α-secretase-like cleavage of APPL, the Drosophila APP ortholog, generating soluble N-terminal fragments (rieche2018drosophilafulllengthamyloid pages 1-3, rieche2018drosophilafulllengthamyloid pages 7-8). Genetic studies revealed that heterozygous *kuz* mutants show increased full-length APPL levels and are protected against age-related visual working memory decline (rieche2018drosophilafulllengthamyloid pages 3-4). Conversely, neuronal overexpression of Kuz impairs visual working memory in young flies, suggesting that the balance of APPL processing critically regulates memory function (rieche2018drosophilafulllengthamyloid pages 3-4, rieche2018drosophilafulllengthamyloid pages 5-6). These findings connect Kuzbanian to circuits controlling cognitive function and potentially to mechanisms relevant for understanding Alzheimer's disease, given the evolutionary conservation of APP processing pathways.

## Developmental Contexts and Tissue Requirements

Kuzbanian function is required across multiple developmental contexts in Drosophila. In embryonic development, Kuz is essential for neurogenesis, axon guidance, and CNS tract formation (kannan2018tyrosinephosphorylationand pages 4-6, kannan2018tyrosinephosphorylationand pages 30-33, hunter2020phosphorylationandproteolytic pages 113-114). During larval stages, Kuz activity is critical in imaginal discs including the wing disc (dorsoventral patterning) and eye disc (morphogenetic furrow progression and photoreceptor development) (puschmann2026scube2primesdispatched pages 6-10, baker2024aninvivo pages 30-35). In adult flies, Kuz expression in specific neural circuits affects memory formation and maintenance (rieche2018drosophilafulllengthamyloid pages 1-3, rieche2018drosophilafulllengthamyloid pages 5-6).

The pleiotropic requirements for Kuz across development reflect both its primary role in Notch signaling—a pathway used repeatedly in diverse developmental contexts—and its additional functions in processing other cell-surface receptors including Robo, APPL, and potentially other guidance molecules (hunter2020phosphorylationandproteolytic pages 65-67).

## Recent Developments and Current Understanding (2023-2025)

Several significant advances have refined our understanding of Kuzbanian function in recent years. A 2023 study identified JNK pathway-mediated transcriptional repression of *kuz* as a conserved mechanism linking inflammation to Notch inactivation in cancer models, demonstrating how pathway crosstalk can regulate Kuz expression (wang2023aconservedmechanism pages 5-7). Work published in 2024 provided mechanistic insights into force-dependent proteolysis, showing that Kuz can cleave diverse structural domains when mechanically exposed, fundamentally revising our understanding of its substrate specificity from sequence-based to accessibility-based recognition (baker2024aninvivo pages 13-17, baker2024aninvivo pages 10-13).

A comprehensive 2025 review of Slit–Robo signaling synthesized evidence for Kuz-mediated Robo processing across species, highlighting the evolutionary conservation of ADAM10-dependent receptor cleavage in axon guidance (sanhueza2025theslit–robosignalling pages 3-4). Additionally, 2025-2026 work on Hedgehog signaling uncovered ADAM10-dependent Shh release mechanisms, suggesting potential conservation in Drosophila though direct validation remains needed (puschmann2026scube2primesdispatched pages 6-10).

## Experimental Evidence and Methodological Approaches

The evidence base for Kuzbanian function derives from multiple complementary approaches. Classical genetic studies using loss-of-function alleles, dominant-negative constructs, and RNAi knockdown have established developmental requirements (baker2024aninvivo pages 30-35, kannan2018tyrosinephosphorylationand pages 4-6). Cell-based assays examining proteolytic processing, including detection of cleavage products and substrate accumulation in Kuz-deficient backgrounds, have defined substrate relationships (rieche2018drosophilafulllengthamyloid pages 1-3, wang2023aconservedmechanism pages 5-7). Recent structure-function studies using engineered receptors with candidate proteolytic switch domains have illuminated substrate recognition mechanisms (baker2024aninvivo pages 13-17, baker2024aninvivo pages 10-13). Behavioral analyses have revealed post-developmental functions in adult memory circuits (rieche2018drosophilafulllengthamyloid pages 3-4, rieche2018drosophilafulllengthamyloid pages 5-6).

## Summary

Kuzbanian represents a critical regulatory protease in Drosophila development and physiology. Its primary function as the Notch S2 sheddase makes it essential for canonical Notch signaling across multiple developmental contexts, including neurogenesis, lateral inhibition, imaginal disc patterning, and boundary formation. Beyond Notch, Kuz processes additional substrates including the Robo axon guidance receptor, the Delta Notch ligand, and APPL, linking it to axon pathfinding, memory function, and potentially neurodegenerative disease mechanisms. Recent evidence indicates that Kuz substrate recognition depends on mechanical accessibility and contextual factors rather than strict sequence specificity, suggesting a sophisticated regulatory mechanism whereby force-induced conformational changes control proteolytic activation. As a membrane-associated metalloproteinase functioning at the cell surface and potentially in endosomal compartments, Kuzbanian integrates mechanical signals with biochemical processing to control cell fate, neural connectivity, and cognitive function throughout the Drosophila lifecycle.

References

1. (baker2024aninvivo pages 13-17): Frederick C. Baker, Jacob Harman, Trevor Jordan, Breana Walton, Amber Ajamu-Johnson, Rama F. Alashqar, Simran Bhikot, Gary Struhl, and Paul D. Langridge. An in vivo screen for proteolytic switch domains that can mediate notch activation by force. bioRxiv, Jul 2024. URL: https://doi.org/10.1101/2024.07.10.602225, doi:10.1101/2024.07.10.602225. This article has 1 citations.

2. (wang2023aconservedmechanism pages 5-7): Cheng-Wei Wang, Marie Clémot, Takao Hashimoto, Johnny A. Diaz, Lauren M. Goins, Andrew S. Goldstein, Raghavendra Nagaraj, and Utpal Banerjee. A conserved mechanism for jnk-mediated loss of notch function in advanced prostate cancer. Science Signaling, Nov 2023. URL: https://doi.org/10.1126/scisignal.abo5213, doi:10.1126/scisignal.abo5213. This article has 3 citations and is from a domain leading peer-reviewed journal.

3. (hunter2020phosphorylationandproteolytic pages 63-65): Ginger L. Hunter and Edward Giniger. Phosphorylation and proteolytic cleavage of notch in canonical and noncanonical notch signaling. Advances in experimental medicine and biology, 1227:51-68, Feb 2020. URL: https://doi.org/10.1007/978-3-030-36422-9\_4, doi:10.1007/978-3-030-36422-9\_4. This article has 13 citations and is from a peer-reviewed journal.

4. (sanhueza2025theslit–robosignalling pages 3-4): Nicole Sanhueza, Evelyn C. Avilés, and Carlos Oliva. The slit–robo signalling pathway in nervous system development: a comparative perspective from vertebrates and invertebrates. Open Biology, Jul 2025. URL: https://doi.org/10.1098/rsob.250026, doi:10.1098/rsob.250026. This article has 8 citations and is from a peer-reviewed journal.

5. (puschmann2026scube2primesdispatched pages 6-10): J. Puschmann, G. Steffes, J. Froese, D. Manikowski, K. Ehring, J. Wittke, C. Garbers, S.V. Wegner, and K. Grobe. Scube2 primes dispatched and adam10-mediated shh release by recruiting hdl acceptors to the plasma membrane. bioRxiv, Jan 2026. URL: https://doi.org/10.1101/2025.01.20.633902, doi:10.1101/2025.01.20.633902. This article has 2 citations.

6. (baker2024aninvivo pages 10-13): Frederick C. Baker, Jacob Harman, Trevor Jordan, Breana Walton, Amber Ajamu-Johnson, Rama F. Alashqar, Simran Bhikot, Gary Struhl, and Paul D. Langridge. An in vivo screen for proteolytic switch domains that can mediate notch activation by force. bioRxiv, Jul 2024. URL: https://doi.org/10.1101/2024.07.10.602225, doi:10.1101/2024.07.10.602225. This article has 1 citations.

7. (wang2023aconservedmechanism pages 1-4): Cheng-Wei Wang, Marie Clémot, Takao Hashimoto, Johnny A. Diaz, Lauren M. Goins, Andrew S. Goldstein, Raghavendra Nagaraj, and Utpal Banerjee. A conserved mechanism for jnk-mediated loss of notch function in advanced prostate cancer. Science Signaling, Nov 2023. URL: https://doi.org/10.1126/scisignal.abo5213, doi:10.1126/scisignal.abo5213. This article has 3 citations and is from a domain leading peer-reviewed journal.

8. (baker2024aninvivo pages 30-35): Frederick C. Baker, Jacob Harman, Trevor Jordan, Breana Walton, Amber Ajamu-Johnson, Rama F. Alashqar, Simran Bhikot, Gary Struhl, and Paul D. Langridge. An in vivo screen for proteolytic switch domains that can mediate notch activation by force. bioRxiv, Jul 2024. URL: https://doi.org/10.1101/2024.07.10.602225, doi:10.1101/2024.07.10.602225. This article has 1 citations.

9. (hunter2020phosphorylationandproteolytic pages 113-114): Ginger L. Hunter and Edward Giniger. Phosphorylation and proteolytic cleavage of notch in canonical and noncanonical notch signaling. Advances in experimental medicine and biology, 1227:51-68, Feb 2020. URL: https://doi.org/10.1007/978-3-030-36422-9\_4, doi:10.1007/978-3-030-36422-9\_4. This article has 13 citations and is from a peer-reviewed journal.

10. (kannan2018tyrosinephosphorylationand pages 30-33): Ramakrishnan Kannan, Eric Cox, Lei Wang, Irina Kuzina, Qun Gu, and Edward Giniger. Tyrosine phosphorylation and proteolytic cleavage of notch are required for non-canonical notch/abl signaling in drosophila axon guidance. Development, Jan 2018. URL: https://doi.org/10.1242/dev.151548, doi:10.1242/dev.151548. This article has 18 citations and is from a domain leading peer-reviewed journal.

11. (hunter2020phosphorylationandproteolytic pages 59-60): Ginger L. Hunter and Edward Giniger. Phosphorylation and proteolytic cleavage of notch in canonical and noncanonical notch signaling. Advances in experimental medicine and biology, 1227:51-68, Feb 2020. URL: https://doi.org/10.1007/978-3-030-36422-9\_4, doi:10.1007/978-3-030-36422-9\_4. This article has 13 citations and is from a peer-reviewed journal.

12. (hunter2020phosphorylationandproteolytic pages 58-59): Ginger L. Hunter and Edward Giniger. Phosphorylation and proteolytic cleavage of notch in canonical and noncanonical notch signaling. Advances in experimental medicine and biology, 1227:51-68, Feb 2020. URL: https://doi.org/10.1007/978-3-030-36422-9\_4, doi:10.1007/978-3-030-36422-9\_4. This article has 13 citations and is from a peer-reviewed journal.

13. (rieche2018drosophilafulllengthamyloid pages 1-3): Franziska Rieche, Katia Carmine-Simmen, Burkhard Poeck, Doris Kretzschmar, and Roland Strauss. Drosophila full-length amyloid precursor protein is required for visual working memory and prevents age-related memory impairment. Current Biology, 28:817-823.e3, Mar 2018. URL: https://doi.org/10.1016/j.cub.2018.01.077, doi:10.1016/j.cub.2018.01.077. This article has 29 citations and is from a highest quality peer-reviewed journal.

14. (rieche2018drosophilafulllengthamyloid pages 7-8): Franziska Rieche, Katia Carmine-Simmen, Burkhard Poeck, Doris Kretzschmar, and Roland Strauss. Drosophila full-length amyloid precursor protein is required for visual working memory and prevents age-related memory impairment. Current Biology, 28:817-823.e3, Mar 2018. URL: https://doi.org/10.1016/j.cub.2018.01.077, doi:10.1016/j.cub.2018.01.077. This article has 29 citations and is from a highest quality peer-reviewed journal.

15. (rieche2018drosophilafulllengthamyloid pages 3-4): Franziska Rieche, Katia Carmine-Simmen, Burkhard Poeck, Doris Kretzschmar, and Roland Strauss. Drosophila full-length amyloid precursor protein is required for visual working memory and prevents age-related memory impairment. Current Biology, 28:817-823.e3, Mar 2018. URL: https://doi.org/10.1016/j.cub.2018.01.077, doi:10.1016/j.cub.2018.01.077. This article has 29 citations and is from a highest quality peer-reviewed journal.

16. (schnute2022ubiquitylationisrequired pages 1-2): Björn Schnute, Hideyuki Shimizu, Marvin Lyga, Martin Baron, and Thomas Klein. Ubiquitylation is required for the incorporation of the notch receptor into intraluminal vesicles to prevent prolonged and ligand-independent activation of the pathway. BMC Biology, Mar 2022. URL: https://doi.org/10.1186/s12915-022-01245-y, doi:10.1186/s12915-022-01245-y. This article has 6 citations and is from a domain leading peer-reviewed journal.

17. (seib2021theroleof pages 6-8): Ekaterina Seib and Thomas Klein. The role of ligand endocytosis in notch signalling. Biology of the Cell, 113:401-418, Jun 2021. URL: https://doi.org/10.1111/boc.202100009, doi:10.1111/boc.202100009. This article has 44 citations and is from a peer-reviewed journal.

18. (steinbuck2018areviewof pages 4-5): Martin Peter Steinbuck and Susan Winandy. A review of notch processing with new insights into ligand-independent notch signaling in t-cells. Frontiers in Immunology, Jun 2018. URL: https://doi.org/10.3389/fimmu.2018.01230, doi:10.3389/fimmu.2018.01230. This article has 148 citations and is from a peer-reviewed journal.

19. (kannan2018tyrosinephosphorylationand pages 4-6): Ramakrishnan Kannan, Eric Cox, Lei Wang, Irina Kuzina, Qun Gu, and Edward Giniger. Tyrosine phosphorylation and proteolytic cleavage of notch are required for non-canonical notch/abl signaling in drosophila axon guidance. Development, Jan 2018. URL: https://doi.org/10.1242/dev.151548, doi:10.1242/dev.151548. This article has 18 citations and is from a domain leading peer-reviewed journal.

20. (rieche2018drosophilafulllengthamyloid pages 5-6): Franziska Rieche, Katia Carmine-Simmen, Burkhard Poeck, Doris Kretzschmar, and Roland Strauss. Drosophila full-length amyloid precursor protein is required for visual working memory and prevents age-related memory impairment. Current Biology, 28:817-823.e3, Mar 2018. URL: https://doi.org/10.1016/j.cub.2018.01.077, doi:10.1016/j.cub.2018.01.077. This article has 29 citations and is from a highest quality peer-reviewed journal.

21. (hunter2020phosphorylationandproteolytic pages 65-67): Ginger L. Hunter and Edward Giniger. Phosphorylation and proteolytic cleavage of notch in canonical and noncanonical notch signaling. Advances in experimental medicine and biology, 1227:51-68, Feb 2020. URL: https://doi.org/10.1007/978-3-030-36422-9\_4, doi:10.1007/978-3-030-36422-9\_4. This article has 13 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](kuz-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](kuz-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. baker2024aninvivo pages 13-17
2. hunter2020phosphorylationandproteolytic pages 63-65
3. hunter2020phosphorylationandproteolytic pages 59-60
4. rieche2018drosophilafulllengthamyloid pages 1-3
5. seib2021theroleof pages 6-8
6. steinbuck2018areviewof pages 4-5
7. baker2024aninvivo pages 30-35
8. wang2023aconservedmechanism pages 1-4
9. wang2023aconservedmechanism pages 5-7
10. kannan2018tyrosinephosphorylationand pages 30-33
11. kannan2018tyrosinephosphorylationand pages 4-6
12. hunter2020phosphorylationandproteolytic pages 65-67
13. hunter2020phosphorylationandproteolytic pages 113-114
14. rieche2018drosophilafulllengthamyloid pages 3-4
15. baker2024aninvivo pages 10-13
16. hunter2020phosphorylationandproteolytic pages 58-59
17. rieche2018drosophilafulllengthamyloid pages 7-8
18. schnute2022ubiquitylationisrequired pages 1-2
19. rieche2018drosophilafulllengthamyloid pages 5-6
20. https://doi.org/10.1101/2024.07.10.602225,
21. https://doi.org/10.1126/scisignal.abo5213,
22. https://doi.org/10.1007/978-3-030-36422-9\_4,
23. https://doi.org/10.1098/rsob.250026,
24. https://doi.org/10.1101/2025.01.20.633902,
25. https://doi.org/10.1242/dev.151548,
26. https://doi.org/10.1016/j.cub.2018.01.077,
27. https://doi.org/10.1186/s12915-022-01245-y,
28. https://doi.org/10.1111/boc.202100009,
29. https://doi.org/10.3389/fimmu.2018.01230,