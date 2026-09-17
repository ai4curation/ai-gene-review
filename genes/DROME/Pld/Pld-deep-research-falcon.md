---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-08T17:50:55.899923'
end_time: '2026-09-08T18:00:34.298399'
duration_seconds: 578.4
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: DROME
  gene_id: Pld
  gene_symbol: Pld
  uniprot_accession: A4UZ54
  protein_description: 'RecName: Full=Phospholipase {ECO:0000256|PIRNR:PIRNR009376};
    EC=3.1.4.4 {ECO:0000256|PIRNR:PIRNR009376};'
  gene_info: Name=Pld {ECO:0000313|EMBL:AAM68352.3, ECO:0000313|FlyBase:FBgn0286511};
    Synonyms=Dmel\CG12110 {ECO:0000313|EMBL:AAM68352.3}, dPLD {ECO:0000313|EMBL:AAM68352.3},
    dPld {ECO:0000313|EMBL:AAM68352.3}, MitoPLD {ECO:0000313|EMBL:AAM68352.3}, PC-Pld
    {ECO:0000313|EMBL:AAM68352.3}, phospholipase D {ECO:0000313|EMBL:AAM68352.3},
    PLD {ECO:0000313|EMBL:AAM68352.3}, pld {ECO:0000313|EMBL:AAM68352.3}, pld1 {ECO:0000313|EMBL:AAM68352.3};
    ORFNames=CG12110 {ECO:0000313|EMBL:AAM68352.3, ECO:0000313|FlyBase:FBgn0286511},
    Dmel_CG12110 {ECO:0000313|EMBL:AAM68352.3};
  organism_full: Drosophila melanogaster (Fruit fly).
  protein_family: Belongs to the phospholipase D family.
  protein_domains: PH-like_dom_sf. (IPR011993); PLipase_D/transphosphatidylase. (IPR001736);
    PLipase_D_euk. (IPR016555); PLipase_D_fam. (IPR015679); PX_dom. (IPR001683)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 26
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Pld-deep-research-falcon_artifacts/artifact-00.md
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
- **UniProt Accession:** A4UZ54
- **Protein Description:** RecName: Full=Phospholipase {ECO:0000256|PIRNR:PIRNR009376}; EC=3.1.4.4 {ECO:0000256|PIRNR:PIRNR009376};
- **Gene Information:** Name=Pld {ECO:0000313|EMBL:AAM68352.3, ECO:0000313|FlyBase:FBgn0286511}; Synonyms=Dmel\CG12110 {ECO:0000313|EMBL:AAM68352.3}, dPLD {ECO:0000313|EMBL:AAM68352.3}, dPld {ECO:0000313|EMBL:AAM68352.3}, MitoPLD {ECO:0000313|EMBL:AAM68352.3}, PC-Pld {ECO:0000313|EMBL:AAM68352.3}, phospholipase D {ECO:0000313|EMBL:AAM68352.3}, PLD {ECO:0000313|EMBL:AAM68352.3}, pld {ECO:0000313|EMBL:AAM68352.3}, pld1 {ECO:0000313|EMBL:AAM68352.3}; ORFNames=CG12110 {ECO:0000313|EMBL:AAM68352.3, ECO:0000313|FlyBase:FBgn0286511}, Dmel_CG12110 {ECO:0000313|EMBL:AAM68352.3};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Belongs to the phospholipase D family.
- **Key Domains:** PH-like_dom_sf. (IPR011993); PLipase_D/transphosphatidylase. (IPR001736); PLipase_D_euk. (IPR016555); PLipase_D_fam. (IPR015679); PX_dom. (IPR001683)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "Pld" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'Pld' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **Pld** (gene ID: Pld, UniProt: A4UZ54) in DROME.

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
- **UniProt Accession:** A4UZ54
- **Protein Description:** RecName: Full=Phospholipase {ECO:0000256|PIRNR:PIRNR009376}; EC=3.1.4.4 {ECO:0000256|PIRNR:PIRNR009376};
- **Gene Information:** Name=Pld {ECO:0000313|EMBL:AAM68352.3, ECO:0000313|FlyBase:FBgn0286511}; Synonyms=Dmel\CG12110 {ECO:0000313|EMBL:AAM68352.3}, dPLD {ECO:0000313|EMBL:AAM68352.3}, dPld {ECO:0000313|EMBL:AAM68352.3}, MitoPLD {ECO:0000313|EMBL:AAM68352.3}, PC-Pld {ECO:0000313|EMBL:AAM68352.3}, phospholipase D {ECO:0000313|EMBL:AAM68352.3}, PLD {ECO:0000313|EMBL:AAM68352.3}, pld {ECO:0000313|EMBL:AAM68352.3}, pld1 {ECO:0000313|EMBL:AAM68352.3}; ORFNames=CG12110 {ECO:0000313|EMBL:AAM68352.3, ECO:0000313|FlyBase:FBgn0286511}, Dmel_CG12110 {ECO:0000313|EMBL:AAM68352.3};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Belongs to the phospholipase D family.
- **Key Domains:** PH-like_dom_sf. (IPR011993); PLipase_D/transphosphatidylase. (IPR001736); PLipase_D_euk. (IPR016555); PLipase_D_fam. (IPR015679); PX_dom. (IPR001683)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "Pld" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'Pld' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **Pld** (gene ID: Pld, UniProt: A4UZ54) in DROME.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Functional annotation report: *Drosophila melanogaster Pld* (UniProt A4UZ54)

## Executive summary

The requested protein is the single **conventional phosphatidylcholine-specific phospholipase D** of *Drosophila melanogaster*, generally called **Pld** or **dPLD** and corresponding to the supplied **CG12110/UniProt A4UZ54** record. It is a 1,278-amino-acid PX–PH–HKD-family enzyme, not mammalian PLD1 or PLD2. Its principal reaction is:

**phosphatidylcholine + H₂O → phosphatidic acid + choline**.

The strongest physiological evidence places dPLD at the base of photoreceptor rhabdomeral microvilli, near the sub-microvillar cisternae, and in endomembrane vesicles. During illumination, dPLD-derived phosphatidic acid supports Arf1- and retromer-dependent recycling of internalized Rhodopsin-1 from Rab7-positive late endosomes back toward the light-sensitive membrane. Loss of dPLD therefore causes rhodopsin-vesicle accumulation, loss of Rh1 and rhabdomere membrane, reduced photosensitivity, and progressive light-dependent retinal degeneration. A second experimentally supported role is promotion of Golgi-derived secretory-vesicle delivery during embryonic cellularization. The latest target-specific study, published as a September 2024 preprint, assigns localization to the PH domain and proposes that the PI3P-binding PX domain restrains enzyme activity. (naik2024theaccessorydomains pages 1-5, lalonde2006arolefor pages 1-2, thakur2016phospholipasedactivity pages 1-2)

## 1. Mandatory identity verification

### Identity match

The literature describes one conventional PLD gene in *D. melanogaster*, encoding a 1,278-aa protein with an N-terminal PX domain, PH domain, four conserved PLD regions, two catalytic HKD motifs, a polybasic PI(4,5)P₂-binding region, and a conserved C terminus. These properties agree with the supplied A4UZ54 annotation and InterPro assignments—PX, PH-like, and eukaryotic PLD/transphosphatidylase domains—and therefore support the identification of the target as **Pld/dPLD/CG12110**. The catalytically inactive H1095N substitution lies in the second HKD motif, experimentally connecting this architecture to PLD catalysis. (lalonde2006arolefor pages 1-2, lalonde2006arolefor pages 2-4)

Most insect genomes contain a single conventional PLD-like gene. Phylogenetic analysis places insect PLDs closer to chordate PLD1 than PLD2, and human PLD1 is correspondingly more effective than PLD2 in rescuing the fly mutant. These comparisons do **not** make the fly protein human PLD1; they establish evolutionary and functional relatedness. (panda2018functionalanalysisof pages 16-19, panda2018functionalanalysisof pages 8-12)

### Critical ambiguity: “MitoPLD”

The supplied synonym **MitoPLD** is potentially misleading. None of the retrieved target-specific studies supports mitochondrial localization or cardiolipin hydrolysis for A4UZ54/CG12110. Instead, they consistently characterize a conventional PX–PH PLD that hydrolyzes phosphatidylcholine and localizes near the photoreceptor plasma-membrane/ER contact region and on endomembranes. The record should therefore **not** be functionally annotated as a mitochondrial PLD6-like cardiolipin hydrolase without direct A4UZ54-specific evidence. (lalonde2006arolefor pages 2-4, panda2018functionalanalysisof pages 16-19, naik2024theaccessorydomains pages 1-5)

## 2. Primary biochemical function and substrate specificity

Drosophila dPLD is a conventional phosphatidylcholine-specific phospholipase D, EC 3.1.4.4. It cleaves the terminal phosphodiester bond of membrane phosphatidylcholine, yielding membrane-retained phosphatidic acid (PA) and soluble choline. Its paired HKD motifs form the characteristic catalytic apparatus of this PLD family, while PX, PH, and polybasic lipid-binding elements regulate membrane recruitment and activity. (naik2024theaccessorydomains pages 1-5, panda2018functionalanalysisof pages 1-5, lalonde2006arolefor pages 2-4)

Several in-vivo findings substantiate this assignment:

* The *dPLD3.1* loss-of-function mutant has reduced PA and no detectable PLD-dependent phosphatidylethanol production in an ethanol-feeding transphosphatidylation assay. Wild-type flies produced phosphatidylethanol, whereas *dPLD3.1* flies did not. (thakur2016phospholipasedactivity pages 2-3)
* Reconstitution with catalytically active dPLD restores PA and retinal integrity; catalytically inactive protein does not reproduce the functional rescue. (thakur2016phospholipasedactivity pages 12-13, thakur2016phospholipasedactivity pages 1-2)
* Expression of the independent PA-producing enzyme RdgA rescues both PA levels and retinal degeneration in *dPLD3.1*, demonstrating that insufficient PA—not merely absence of a PLD scaffold—is central to the phenotype. (thakur2016phospholipasedactivity pages 6-7)

The available studies did not report steady-state kinetic constants, a systematic panel of alternative head-group substrates, or direct evidence for cardiolipin hydrolysis. Accordingly, the defensible specificity annotation is **conventional PC-preferring PLD**, with transphosphatidylation in the presence of a primary alcohol, rather than an unrestricted phospholipase or mitochondrial cardiolipin enzyme.

## 3. Cellular localization

### Adult photoreceptors

Endogenous or reconstituted dPLD concentrates at the **base of the rhabdomeral microvilli**, near or on the **sub-microvillar cisternae (SMC)**. The SMC is a specialized smooth-ER compartment forming a close membrane-contact region with the light-sensitive apical plasma membrane. A second dPLD pool occurs on intracellular vesicles, including vesicles overlapping with PI3P reporters; in S2R+ cells dPLD is found on Rab5/Rab7-associated compartments and partly near sub-plasma-membrane actin. (panda2018functionalanalysisof pages 16-19, panda2018functionalanalysisof pages 12-16, naik2024theaccessorydomains pages 1-5)

This spatial distribution is functionally important. The 2024 Naik–Raghu preprint reports that deletion of the PH domain displaces dPLD from the rhabdomere base and prevents rescue of *dPLD3.1* retinal degeneration. In contrast, PX deletion does not abolish this localization, although the PX domain binds PI3P and affects activity. Thus, the PH domain appears to be the dominant localization determinant in photoreceptors. (naik2024theaccessorydomains pages 5-8)

### Embryos

During embryonic cellularization, Pld was detected on small cytoplasmic vesicles. Together with abnormal Golgi morphology and secretory trafficking in Pld-deficient embryos, this localization supports operation on Golgi-derived or post-Golgi membrane carriers rather than a purely plasma-membrane role. (lalonde2006arolefor pages 1-2, lalonde2006arolefor pages 2-4)

## 4. Principal pathways and physiological mechanisms

### 4.1 Light-dependent Rh1 recycling and membrane homeostasis

A fly rhabdomere contains approximately 40,000 light-sensitive microvillar projections and undergoes substantial membrane turnover during illumination. Light stimulates dPLD activity. Loss of dPLD does not primarily block Rh1 internalization: *dPLD3.1* photoreceptors do not show a selective increase in Rab5-positive vesicles or a primary clathrin-endocytosis defect. Instead, they clear internalized Rh1-containing vesicles slowly and accumulate Rh1 in **Rab7-positive late endosomes**. (thakur2016phospholipasedactivity pages 2-3, thakur2016phospholipasedactivity pages 13-15, thakur2016phospholipasedactivity pages 1-2)

The resulting sequence is:

1. Illumination activates rhodopsin and drives Rh1-containing membrane internalization.
2. dPLD generates a spatially restricted PA pool near the SMC and/or endosomal pathway.
3. PA supports removal of Rh1 cargo from Rab7-positive late endosomes.
4. Arf1-GTP and retromer direct recycling toward the rhabdomere membrane.
5. Recycling preserves Rh1 abundance, rhabdomere size, and sustained light sensitivity.

In *dPLD3.1*, illumination instead causes exaggerated rhabdomere-volume loss, accumulation of Rab7-positive Rh1 vesicles, progressive reduction of total Rh1, diminished light sensitivity, and retinal degeneration. Catalytically active dPLD reverses these defects. (thakur2016phospholipasedactivity pages 11-12, thakur2016phospholipasedactivity pages 6-7, thakur2016phospholipasedactivity pages 1-2)

Genetic epistasis places dPLD in an **Arf1–retromer recycling module**. Increasing the activity of Garz, an Arf1 regulator, clears Rh1 vesicles and suppresses dPLD-mutant degeneration; Garz depletion causes light-dependent degeneration. Increasing retromer activity also suppresses dPLD-loss phenotypes, whereas dPLD-driven vesicle clearance requires intact Garz/Arf1 and retromer function. These are strong pathway-level data, although they do not establish direct physical binding among dPLD, Arf1, and retromer. (thakur2016phospholipasedactivity pages 11-12, thakur2016phospholipasedactivity pages 13-15)

### 4.2 Phototransduction and phosphoinositide homeostasis

The foundational 2005 study found that Pld-null flies have reduced light sensitivity and increased susceptibility to retinal degeneration. Conversely, Pld overexpression rescued aspects of degeneration in PLC-deficient flies and restored visual signaling in flies lacking a phosphatidylinositol-transfer protein. The authors proposed that PLD-derived PA helps replenish phosphoinositide pools, including the PI(4,5)P₂ substrate consumed by PLC during phototransduction. Later work sharpened this interpretation: dPLD’s best-established direct role is not initiation of the electrical light response but maintenance and recycling of the activated rhabdomeral membrane under sustained illumination. (thakur2016phospholipasedactivity pages 6-7, naik2024theaccessorydomains pages 1-5)

PA could facilitate phosphoinositide synthesis, membrane curvature, coat recruitment, vesicle budding, or fusion. However, the immediate PA-binding effector responsible for Rh1 recycling remains unidentified. Therefore, “PA-dependent Arf1/retromer recycling” is well supported, whereas a specific direct biochemical connection from PA to an individual retromer component is still inferential.

### 4.3 Embryonic cellularization

Drosophila cellularization encloses approximately 6,000 syncytial nuclei and requires an estimated 25-fold increase in plasma-membrane area. Pld loss hinders this process and frequently produces early embryonic arrest. Pld-deficient embryos display abnormal Golgi structure and defective secretory-vesicle traffic, supporting a model in which dPLD-generated PA promotes production, movement, or fusion competence of Golgi-derived vesicles delivered to the growing embryonic cortex. (lalonde2006arolefor pages 1-2)

This developmental role is biologically coherent with the photoreceptor findings: both require PA-dependent handling of large membrane fluxes. Nevertheless, the embryonic study did not provide the same catalytic-rescue and lipidomic depth as the photoreceptor work, so the precise step—Golgi budding, carrier transport, cortical tethering, or fusion—remains less firmly resolved.

## 5. Quantitative evidence

Targeted mass spectrometry in fly heads quantified **39 PA molecular species**. Of these, **30 were reduced** in *dPLD3.1*. Re-expression of fly dPLD restored **26 species** to wild-type levels; human PLD1 restored 16 and human PLD2 only one, PA 16:2/18:0. dPLD significantly elevated every measured species above the mutant baseline, whereas human PLD1 and PLD2 failed to elevate two and five species, respectively. These data show that dPLD controls a broad but spatially and molecularly distinctive PA pool. (panda2018functionalanalysisof pages 16-19)

Human PLD1 completely rescued *dPLD3.1* retinal degeneration, while PLD2 was only partly effective. dPLD and human PLD1 both localized near the rhabdomere-base/SMC region, whereas human PLD2 was more diffuse. Thus, physiological rescue correlates better with correct localization and restoration of appropriate PA species than with bulk PA production alone. It remains unknown which individual acyl-chain species are causal. (panda2018functionalanalysisof pages 12-16, panda2018functionalanalysisof pages 19-23)

The 2016 trafficking experiments commonly quantified Rh1-containing vesicles in 10 ommatidia from three preparations and rhabdomere integrity in 50 ommatidia from at least two flies. The 2024 domain study generally analyzed 50 ommatidia from at least five flies. These sample designs support reproducible cell-level phenotyping, although ommatidia are nested within animals and should not always be interpreted as wholly independent biological replicates. (naik2024theaccessorydomains pages 14-17, thakur2016phospholipasedactivity pages 12-13)

## 6. Recent development: accessory-domain regulation (2024)

The most recent target-specific work located in this search is Naik and Raghu’s preprint, posted **23 September 2024**, DOI: https://doi.org/10.1101/2024.09.22.614390. It advances two mechanistic conclusions:

* **PH domain:** required for localization at the rhabdomere base and for rescue of dPLD deficiency.
* **PX domain:** binds PI3P but is not necessary for rhabdomere-base localization; its removal accelerates light-dependent degeneration caused by dPLD overexpression, suggesting that it negatively regulates activity.

Depletion of Vps34 or Vps15, which reduces PI3P synthesis, similarly enhanced dPLD-overexpression degeneration. Manipulating UVRAG- versus ATG14-associated PI3P pathways produced different effects, suggesting that early-endosomal and autophagic PI3P pools may regulate dPLD differently. These results provide a spatial-regulation model in which the PH domain positions dPLD while PX–PI3P interactions constrain its activity or partition its vesicular pool. Because the paper is a preprint and degeneration after overexpression is an indirect activity proxy, these assignments remain provisional pending peer review and direct enzymatic measurements. (naik2024theaccessorydomains pages 1-5, naik2024theaccessorydomains pages 5-8, naik2024theaccessorydomains pages 14-17)

No peer-reviewed 2023–2024 paper offering a comparably direct functional analysis of A4UZ54/CG12110 was identified in the retrieved literature.

## 7. Applications and real-world relevance

Pld is used primarily as a **model-system tool**, not as a current clinical or industrial target:

* **Membrane-trafficking model:** The fly photoreceptor provides an in-vivo system for studying how a signal-generated PA pool couples receptor endocytosis to retromer recycling and membrane-domain maintenance.
* **Lipidomics platform:** The *dPLD3.1* mutant and rescue transgenes enable causal comparison of total PA with specific PA molecular species. The finding that 30 of 39 species fall in the mutant, but different PLD orthologs restore different subsets, demonstrates why spatially resolved lipid output is more informative than bulk lipid measurements. (panda2018functionalanalysisof pages 16-19, panda2018functionalanalysisof pages 19-23)
* **Ortholog functional testing:** Human PLD1 and PLD2 can be compared in the same fly tissue; PLD1’s superior rescue supports conserved ancestral function and exposes PLD2 neofunctionalization. (panda2018functionalanalysisof pages 16-19)
* **Disease-model modifier screens:** PLD-pathway genes have emerged as modifiers in Drosophila ALS models, suggesting translational hypotheses about lipid signaling and membrane traffic. Such screens identify pathway interactions, however, and should not be interpreted as proof that fly Pld inhibition or activation will treat human ALS.

## 8. Evidence assessment and expert interpretation

The evidence is strongest for four conclusions:

1. **A4UZ54/CG12110 is a conventional PX–PH, two-HKD PLD.**
2. **Its primary catalytic output is PA generated from phosphatidylcholine.**
3. **In illuminated photoreceptors it preserves the rhabdomeral membrane by promoting Arf1/retromer-dependent post-endocytic Rh1 recycling.**
4. **During embryogenesis it supports Golgi-derived membrane delivery during cellularization.**

The central expert interpretation emerging from the 2016–2024 work is that dPLD does not merely raise whole-cell PA. It generates a **localized and compositionally specific PA pool** whose function depends on correct membrane targeting. This explains why human PLD1, which reaches the rhabdomere-base region, rescues more effectively than PLD2 despite both enzymes being able to produce PA. (panda2018functionalanalysisof pages 16-19, panda2018functionalanalysisof pages 19-23)

Important unresolved questions include the identity of the immediate PA effector, whether catalysis occurs predominantly on SMC, plasma-membrane, or endosomal PC, which PA acyl species are functionally decisive, and how light activates dPLD. Mitochondrial localization and cardiolipin specificity are not supported for this target.

The evidence matrix below summarizes the annotation and its limitations.

| Question / feature | Best-supported finding | Direct evidence and system | Key source / date | Confidence / limitations |
|---|---|---|---|---|
| Identity and architecture | The target is the single conventional *Drosophila melanogaster* phospholipase D, Pld/dPLD: a 1,278-aa protein with N-terminal PX and PH domains, two catalytic HKD motifs, a PI(4,5)P₂-binding region, and a conserved C terminus, consistent with UniProt A4UZ54/CG12110. | cDNA/RACE, genomic searches, Southern blotting, sequence/domain analysis, and the catalytic-inactivating H1095N substitution in the second HKD motif. | LaLonde et al., *BMC Developmental Biology*, 14 Dec 2006 (lalonde2006arolefor pages 1-2, lalonde2006arolefor pages 2-4) | **High** for conventional dPLD identity and architecture. Retrieved papers use Pld/dPLD but do not independently verify every database alias. |
| Primary catalytic function | Conventional dPLD hydrolyzes phosphatidylcholine to phosphatidic acid and choline: PC + H₂O → PA + choline. PA functions as both a membrane intermediate and signaling lipid. | Conserved HKD-family chemistry; loss of dPLD lowers PA; catalytically active dPLD and an independent PA-generating enzyme rescue mutant phenotypes. PLD-dependent phosphatidylethanol formation in ethanol-fed flies provides an in-vivo activity readout. | LaLonde et al., 2006; Thakur et al., *eLife*, 22 Nov 2016 (lalonde2006arolefor pages 1-2, thakur2016phospholipasedactivity pages 2-3, thakur2016phospholipasedactivity pages 6-7, thakur2016phospholipasedactivity pages 1-2) | **High** for PC-selective conventional PLD activity and PA production. No kinetic constants or exhaustive substrate-specificity profile were identified. |
| Photoreceptor localization | dPLD concentrates at the base of rhabdomeral microvilli, near or on the sub-microvillar cisternae, a specialized smooth-ER/plasma-membrane contact region; a vesicular pool also occurs. | Immunolocalization in adult photoreceptors; comparative localization in S2R+ cells and with human PLD isoforms; partial vesicular overlap with a PI3P reporter. | Panda et al., *Bioscience Reports*, 21 Dec 2018; Naik and Raghu, *bioRxiv*, 23 Sep 2024 (panda2018functionalanalysisof pages 16-19, panda2018functionalanalysisof pages 12-16, naik2024theaccessorydomains pages 1-5, naik2024theaccessorydomains pages 5-8) | **Moderate–high**. Localization at or near the SMC is well supported, but exact membrane topology and the relative contributions of SMC and endosomal pools remain unresolved. |
| Light-dependent Rh1 trafficking | During illumination, dPLD-derived PA couples endocytosis of Rh1-containing vesicles to their clearance or recycling from Rab7-positive late endosomes toward the rhabdomere, maintaining Rh1 abundance and apical membrane size. | The dPLD3.1 mutant accumulates Rh1-labeled, Rab7-positive vesicles, loses Rh1, and exhibits enhanced rhabdomere shrinkage; catalytically active dPLD rescues these defects. Rab5-positive vesicles and primary clathrin-dependent uptake were not selectively increased, placing dPLD after internalization. | Thakur et al., *eLife*, 22 Nov 2016 (thakur2016phospholipasedactivity pages 2-3, thakur2016phospholipasedactivity pages 13-15, thakur2016phospholipasedactivity pages 12-13, thakur2016phospholipasedactivity pages 1-2) | **High** for a post-endocytic recycling role. The PA-binding effector that executes vesicle sorting or fusion is unknown. |
| Arf1–retromer pathway | dPLD functions with Arf1-GTP and retromer: increasing Arf1 activation or retromer activity suppresses dPLD-loss phenotypes, whereas dPLD-driven vesicle clearance requires the Arf1 regulator Garz and intact retromer. | Photoreceptor genetic epistasis using garz/Arf1 and retromer manipulations, Rh1-vesicle counts, and retinal-degeneration assays. | Thakur et al., *eLife*, 22 Nov 2016 (thakur2016phospholipasedactivity pages 11-12, thakur2016phospholipasedactivity pages 13-15, thakur2016phospholipasedactivity pages 1-2) | **High** for pathway dependence; **moderate** for the exact molecular ordering because genetic interactions do not establish direct physical binding. |
| Embryonic cellularization | Pld promotes Golgi-derived secretory-vesicle trafficking and membrane delivery during cellularization; deficiency disrupts Golgi morphology, hinders cellularization, and frequently causes early embryonic arrest. | Targeted Pld loss and embryonic imaging. Cellularization encloses approximately 6,000 nuclei and entails an estimated 25-fold plasma-membrane expansion. | LaLonde et al., *BMC Developmental Biology*, 14 Dec 2006 (lalonde2006arolefor pages 1-2) | **Moderate–high** for a developmental trafficking role. Direct lipidomics and catalytic-mutant rescue during cellularization were not reported in the retrieved evidence. |
| PA molecular-species output | Of 39 PA species quantified in fly heads, 30 were reduced in dPLD3.1; dPLD re-expression restored 26. Human PLD1 restored 16 and PLD2 only one, indicating that localization and molecular-species output, rather than merely bulk PA, correlate with functional rescue. | Targeted ESI-MRM-MS/MS lipidomics in dPLD3.1 and transgenic rescue flies, accompanied by retinal phenotyping and localization comparisons. | Panda et al., *Bioscience Reports*, 21 Dec 2018 (panda2018functionalanalysisof pages 16-19, panda2018functionalanalysisof pages 19-23) | **High** for the measured species counts. Which individual PA species are causal for membrane maintenance remains untested. |
| PX and PH accessory domains | The PH domain is required for rhabdomere-base localization and physiological rescue. The PX domain binds PI3P but is dispensable for this localization and appears to restrain activity; deleting PX or perturbing selected PI3P pools enhances light-dependent degeneration caused by dPLD overexpression. | Domain-deletion transgenes, dPLD3.1 rescue, immunofluorescence, PI3P lipid-overlay assays, and RNAi against Vps34/Vps15, UVRAG, or ATG14; typical morphology quantification used 50 ommatidia from at least five flies. | Naik and Raghu, *bioRxiv* preprint, 23 Sep 2024 (naik2024theaccessorydomains pages 1-5, naik2024theaccessorydomains pages 5-8, naik2024theaccessorydomains pages 14-17) | **Provisional/moderate** because this is the newest target-specific study but is not peer reviewed. Overexpression-associated degeneration is an activity proxy, not a direct enzymatic-rate measurement. |
| “MitoPLD” alias warning | The supplied “MitoPLD” alias must not be treated as evidence that A4UZ54 is a mitochondrial PLD6-like cardiolipin hydrolase. The experimentally studied target is a PX–PH conventional, PC-hydrolyzing dPLD associated with photoreceptor SMC/sub-plasma-membrane and endomembrane compartments. | Target-specific literature consistently describes conventional dPLD and compares it with PLD1/PLD2; the retrieved studies provide no direct support for mitochondrial localization or cardiolipin substrate specificity. | LaLonde et al., 2006; Panda et al., 2018; Naik and Raghu, 2024 (lalonde2006arolefor pages 2-4, panda2018functionalanalysisof pages 16-19, panda2018functionalanalysisof pages 8-12, naik2024theaccessorydomains pages 1-5) | **High-confidence caution**. Mitochondrial localization and cardiolipin hydrolysis should remain unannotated unless demonstrated specifically for A4UZ54/CG12110. |


*Table: Compact evidence assessment for the identity, catalytic function, localization, pathways, and experimentally established roles of A4UZ54/CG12110. It also flags the unsupported and potentially misleading “MitoPLD” alias.*

## Key publications

* LaLonde MM et al. **“Regulation of phototransduction responsiveness and retinal degeneration by a phospholipase D-generated signaling lipid.”** *Journal of Cell Biology*, May 2005. DOI: https://doi.org/10.1083/jcb.200502122.
* LaLonde M et al. **“A role for Phospholipase D in Drosophila embryonic cellularization.”** *BMC Developmental Biology*, 14 December 2006. DOI: https://doi.org/10.1186/1471-213X-6-60. (lalonde2006arolefor pages 1-2)
* Thakur R et al. **“Phospholipase D activity couples plasma membrane endocytosis with retromer dependent recycling.”** *eLife*, 22 November 2016. DOI: https://doi.org/10.7554/eLife.18515. (thakur2016phospholipasedactivity pages 1-2)
* Panda A et al. **“Functional analysis of mammalian phospholipase D enzymes.”** *Bioscience Reports*, 21 December 2018. DOI: https://doi.org/10.1042/BSR20181690. (panda2018functionalanalysisof pages 1-5)
* Thakur R et al. **“Regulation of Membrane Turnover by Phosphatidic Acid: Cellular Functions and Disease Implications.”** *Frontiers in Cell and Developmental Biology*, June 2019. DOI: https://doi.org/10.3389/fcell.2019.00083.
* Naik A, Raghu P. **“The accessory domains of Phospholipase D regulate its localization and activity in Drosophila photoreceptors.”** *bioRxiv*, 23 September 2024. DOI: https://doi.org/10.1101/2024.09.22.614390. Preprint, not peer reviewed. (naik2024theaccessorydomains pages 1-5)

References

1. (naik2024theaccessorydomains pages 1-5): Amruta Naik and Padinjat Raghu. The accessory domains of phospholipase d regulate its localization and activity in drosophila photoreceptors. bioRxiv, Sep 2024. URL: https://doi.org/10.1101/2024.09.22.614390, doi:10.1101/2024.09.22.614390. This article has 0 citations.

2. (lalonde2006arolefor pages 1-2): Mary LaLonde, Hilde Janssens, Suyong Yun, Juan Crosby, Olga Redina, Virginie Olive, Yelena M Altshuller, Seok-Yong Choi, Guangwei Du, J Peter Gergen, and Michael A Frohman. A role for phospholipase d in drosophila embryonic cellularization. BMC Developmental Biology, 6:60-60, Dec 2006. URL: https://doi.org/10.1186/1471-213x-6-60, doi:10.1186/1471-213x-6-60. This article has 40 citations and is from a peer-reviewed journal.

3. (thakur2016phospholipasedactivity pages 1-2): Rajan Thakur, Aniruddha Panda, Elise Coessens, Nikita Raj, Shweta Yadav, Sruthi Balakrishnan, Qifeng Zhang, Plamen Georgiev, Bishal Basak, Renu Pasricha, Michael JO Wakelam, Nicholas T Ktistakis, and Padinjat Raghu. Phospholipase d activity couples plasma membrane endocytosis with retromer dependent recycling. eLife, Nov 2016. URL: https://doi.org/10.7554/elife.18515, doi:10.7554/elife.18515. This article has 44 citations and is from a domain leading peer-reviewed journal.

4. (lalonde2006arolefor pages 2-4): Mary LaLonde, Hilde Janssens, Suyong Yun, Juan Crosby, Olga Redina, Virginie Olive, Yelena M Altshuller, Seok-Yong Choi, Guangwei Du, J Peter Gergen, and Michael A Frohman. A role for phospholipase d in drosophila embryonic cellularization. BMC Developmental Biology, 6:60-60, Dec 2006. URL: https://doi.org/10.1186/1471-213x-6-60, doi:10.1186/1471-213x-6-60. This article has 40 citations and is from a peer-reviewed journal.

5. (panda2018functionalanalysisof pages 16-19): Aniruddha Panda, Rajan Thakur, Harini Krishnan, Amruta Naik, Dhananjay Shinde, and Padinjat Raghu. Functional analysis of mammalian phospholipase d enzymes. Bioscience Reports, Dec 2018. URL: https://doi.org/10.1042/bsr20181690, doi:10.1042/bsr20181690. This article has 21 citations and is from a peer-reviewed journal.

6. (panda2018functionalanalysisof pages 8-12): Aniruddha Panda, Rajan Thakur, Harini Krishnan, Amruta Naik, Dhananjay Shinde, and Padinjat Raghu. Functional analysis of mammalian phospholipase d enzymes. Bioscience Reports, Dec 2018. URL: https://doi.org/10.1042/bsr20181690, doi:10.1042/bsr20181690. This article has 21 citations and is from a peer-reviewed journal.

7. (panda2018functionalanalysisof pages 1-5): Aniruddha Panda, Rajan Thakur, Harini Krishnan, Amruta Naik, Dhananjay Shinde, and Padinjat Raghu. Functional analysis of mammalian phospholipase d enzymes. Bioscience Reports, Dec 2018. URL: https://doi.org/10.1042/bsr20181690, doi:10.1042/bsr20181690. This article has 21 citations and is from a peer-reviewed journal.

8. (thakur2016phospholipasedactivity pages 2-3): Rajan Thakur, Aniruddha Panda, Elise Coessens, Nikita Raj, Shweta Yadav, Sruthi Balakrishnan, Qifeng Zhang, Plamen Georgiev, Bishal Basak, Renu Pasricha, Michael JO Wakelam, Nicholas T Ktistakis, and Padinjat Raghu. Phospholipase d activity couples plasma membrane endocytosis with retromer dependent recycling. eLife, Nov 2016. URL: https://doi.org/10.7554/elife.18515, doi:10.7554/elife.18515. This article has 44 citations and is from a domain leading peer-reviewed journal.

9. (thakur2016phospholipasedactivity pages 12-13): Rajan Thakur, Aniruddha Panda, Elise Coessens, Nikita Raj, Shweta Yadav, Sruthi Balakrishnan, Qifeng Zhang, Plamen Georgiev, Bishal Basak, Renu Pasricha, Michael JO Wakelam, Nicholas T Ktistakis, and Padinjat Raghu. Phospholipase d activity couples plasma membrane endocytosis with retromer dependent recycling. eLife, Nov 2016. URL: https://doi.org/10.7554/elife.18515, doi:10.7554/elife.18515. This article has 44 citations and is from a domain leading peer-reviewed journal.

10. (thakur2016phospholipasedactivity pages 6-7): Rajan Thakur, Aniruddha Panda, Elise Coessens, Nikita Raj, Shweta Yadav, Sruthi Balakrishnan, Qifeng Zhang, Plamen Georgiev, Bishal Basak, Renu Pasricha, Michael JO Wakelam, Nicholas T Ktistakis, and Padinjat Raghu. Phospholipase d activity couples plasma membrane endocytosis with retromer dependent recycling. eLife, Nov 2016. URL: https://doi.org/10.7554/elife.18515, doi:10.7554/elife.18515. This article has 44 citations and is from a domain leading peer-reviewed journal.

11. (panda2018functionalanalysisof pages 12-16): Aniruddha Panda, Rajan Thakur, Harini Krishnan, Amruta Naik, Dhananjay Shinde, and Padinjat Raghu. Functional analysis of mammalian phospholipase d enzymes. Bioscience Reports, Dec 2018. URL: https://doi.org/10.1042/bsr20181690, doi:10.1042/bsr20181690. This article has 21 citations and is from a peer-reviewed journal.

12. (naik2024theaccessorydomains pages 5-8): Amruta Naik and Padinjat Raghu. The accessory domains of phospholipase d regulate its localization and activity in drosophila photoreceptors. bioRxiv, Sep 2024. URL: https://doi.org/10.1101/2024.09.22.614390, doi:10.1101/2024.09.22.614390. This article has 0 citations.

13. (thakur2016phospholipasedactivity pages 13-15): Rajan Thakur, Aniruddha Panda, Elise Coessens, Nikita Raj, Shweta Yadav, Sruthi Balakrishnan, Qifeng Zhang, Plamen Georgiev, Bishal Basak, Renu Pasricha, Michael JO Wakelam, Nicholas T Ktistakis, and Padinjat Raghu. Phospholipase d activity couples plasma membrane endocytosis with retromer dependent recycling. eLife, Nov 2016. URL: https://doi.org/10.7554/elife.18515, doi:10.7554/elife.18515. This article has 44 citations and is from a domain leading peer-reviewed journal.

14. (thakur2016phospholipasedactivity pages 11-12): Rajan Thakur, Aniruddha Panda, Elise Coessens, Nikita Raj, Shweta Yadav, Sruthi Balakrishnan, Qifeng Zhang, Plamen Georgiev, Bishal Basak, Renu Pasricha, Michael JO Wakelam, Nicholas T Ktistakis, and Padinjat Raghu. Phospholipase d activity couples plasma membrane endocytosis with retromer dependent recycling. eLife, Nov 2016. URL: https://doi.org/10.7554/elife.18515, doi:10.7554/elife.18515. This article has 44 citations and is from a domain leading peer-reviewed journal.

15. (panda2018functionalanalysisof pages 19-23): Aniruddha Panda, Rajan Thakur, Harini Krishnan, Amruta Naik, Dhananjay Shinde, and Padinjat Raghu. Functional analysis of mammalian phospholipase d enzymes. Bioscience Reports, Dec 2018. URL: https://doi.org/10.1042/bsr20181690, doi:10.1042/bsr20181690. This article has 21 citations and is from a peer-reviewed journal.

16. (naik2024theaccessorydomains pages 14-17): Amruta Naik and Padinjat Raghu. The accessory domains of phospholipase d regulate its localization and activity in drosophila photoreceptors. bioRxiv, Sep 2024. URL: https://doi.org/10.1101/2024.09.22.614390, doi:10.1101/2024.09.22.614390. This article has 0 citations.

## Artifacts

- [Edison artifact artifact-00](Pld-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. thakur2016phospholipasedactivity pages 2-3
2. thakur2016phospholipasedactivity pages 6-7
3. naik2024theaccessorydomains pages 5-8
4. lalonde2006arolefor pages 1-2
5. panda2018functionalanalysisof pages 16-19
6. thakur2016phospholipasedactivity pages 1-2
7. panda2018functionalanalysisof pages 1-5
8. naik2024theaccessorydomains pages 1-5
9. lalonde2006arolefor pages 2-4
10. panda2018functionalanalysisof pages 8-12
11. thakur2016phospholipasedactivity pages 12-13
12. panda2018functionalanalysisof pages 12-16
13. thakur2016phospholipasedactivity pages 13-15
14. thakur2016phospholipasedactivity pages 11-12
15. panda2018functionalanalysisof pages 19-23
16. naik2024theaccessorydomains pages 14-17
17. https://doi.org/10.1101/2024.09.22.614390.
18. https://doi.org/10.1083/jcb.200502122.
19. https://doi.org/10.1186/1471-213X-6-60.
20. https://doi.org/10.7554/eLife.18515.
21. https://doi.org/10.1042/BSR20181690.
22. https://doi.org/10.3389/fcell.2019.00083.
23. https://doi.org/10.1101/2024.09.22.614390,
24. https://doi.org/10.1186/1471-213x-6-60,
25. https://doi.org/10.7554/elife.18515,
26. https://doi.org/10.1042/bsr20181690,