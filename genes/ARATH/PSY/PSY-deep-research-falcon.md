---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-26T22:03:14.255006'
end_time: '2026-09-26T22:11:04.791051'
duration_seconds: 470.54
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: ARATH
  gene_id: PSY
  gene_symbol: PSY1
  uniprot_accession: P37271
  protein_description: 'RecName: Full=Phytoene synthase 1, chloroplastic {ECO:0000303|PubMed:8016277,
    ECO:0000303|Ref.2}; EC=2.5.1.32 {ECO:0000269|PubMed:25675505}; Flags: Precursor;'
  gene_info: Name=PSY1 {ECO:0000303|PubMed:8016277}; Synonyms=PSY {ECO:0000303|Ref.2};
    OrderedLocusNames=At5g17230 {ECO:0000312|Araport:AT5G17230}; ORFNames=MKP11.8
    {ECO:0000312|EMBL:BAB10510.1};
  organism_full: Arabidopsis thaliana (Mouse-ear cress).
  protein_family: Belongs to the phytoene/squalene synthase family.
  protein_domains: Isoprenoid_synthase_dom_sf. (IPR008949); Squ/phyt_synthse. (IPR002060);
    Squalene/phytoene_synthase_CS. (IPR019845); Trans_IPPS_bact-type. (IPR044843);
    Trans_IPPS_HH. (IPR033904)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 27
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: PSY-deep-research-falcon_artifacts/artifact-00.md
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
- **UniProt Accession:** P37271
- **Protein Description:** RecName: Full=Phytoene synthase 1, chloroplastic {ECO:0000303|PubMed:8016277, ECO:0000303|Ref.2}; EC=2.5.1.32 {ECO:0000269|PubMed:25675505}; Flags: Precursor;
- **Gene Information:** Name=PSY1 {ECO:0000303|PubMed:8016277}; Synonyms=PSY {ECO:0000303|Ref.2}; OrderedLocusNames=At5g17230 {ECO:0000312|Araport:AT5G17230}; ORFNames=MKP11.8 {ECO:0000312|EMBL:BAB10510.1};
- **Organism (full):** Arabidopsis thaliana (Mouse-ear cress).
- **Protein Family:** Belongs to the phytoene/squalene synthase family.
- **Key Domains:** Isoprenoid_synthase_dom_sf. (IPR008949); Squ/phyt_synthse. (IPR002060); Squalene/phytoene_synthase_CS. (IPR019845); Trans_IPPS_bact-type. (IPR044843); Trans_IPPS_HH. (IPR033904)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PSY1" matches the protein description above**
2. **Verify the organism is correct:** Arabidopsis thaliana (Mouse-ear cress).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PSY1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PSY1** (gene ID: PSY, UniProt: P37271) in ARATH.

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
- **UniProt Accession:** P37271
- **Protein Description:** RecName: Full=Phytoene synthase 1, chloroplastic {ECO:0000303|PubMed:8016277, ECO:0000303|Ref.2}; EC=2.5.1.32 {ECO:0000269|PubMed:25675505}; Flags: Precursor;
- **Gene Information:** Name=PSY1 {ECO:0000303|PubMed:8016277}; Synonyms=PSY {ECO:0000303|Ref.2}; OrderedLocusNames=At5g17230 {ECO:0000312|Araport:AT5G17230}; ORFNames=MKP11.8 {ECO:0000312|EMBL:BAB10510.1};
- **Organism (full):** Arabidopsis thaliana (Mouse-ear cress).
- **Protein Family:** Belongs to the phytoene/squalene synthase family.
- **Key Domains:** Isoprenoid_synthase_dom_sf. (IPR008949); Squ/phyt_synthse. (IPR002060); Squalene/phytoene_synthase_CS. (IPR019845); Trans_IPPS_bact-type. (IPR044843); Trans_IPPS_HH. (IPR033904)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PSY1" matches the protein description above**
2. **Verify the organism is correct:** Arabidopsis thaliana (Mouse-ear cress).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PSY1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PSY1** (gene ID: PSY, UniProt: P37271) in ARATH.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Functional annotation report: *Arabidopsis thaliana* PSY

## Executive conclusion

The requested target is correctly identified as the *Arabidopsis thaliana* locus **At5g17230**, commonly called **PSY** and represented by UniProt **P37271**. Although the supplied UniProt record calls the protein “phytoene synthase 1,” *Arabidopsis* has a **single PSY gene**; “PSY1” should therefore not be confused with the distinct PSY1 paralogs of tomato, tobacco, algae, or other organisms. In particular, tomato has three PSY genes, whereas *Arabidopsis* has one. Findings about tomato PSY1 were not used as evidence for At5g17230. (navarrocarcelen2025experimentalvalidationof pages 1-3, meier2011atranscriptionalanalysis pages 4-6, ezquerro2023overlappingandspecialized pages 1-2)

AtPSY is a plastid-targeted phytoene synthase (EC 2.5.1.32) that catalyzes the head-to-head condensation of **two geranylgeranyl diphosphate molecules (2 GGPP) into 15-cis-phytoene**, initiating the first committed and usually major flux-controlling step of carotenoid biosynthesis. Its functional abundance is controlled at several levels—transcription, alternative 5′-UTR use, plastid import and localization, protein interaction, folding, membrane association, and degradation. (alvarez2016carotenogenesisisregulated pages 1-5, zhou2022phytoenesynthasethe pages 1-2)

| Topic | Current annotation/finding | Evidence type | Key source/date |
|---|---|---|---|
| Identity | **Arabidopsis thaliana** PSY, locus **At5g17230**, corresponds to chloroplast-targeted phytoene synthase **P37271**; Arabidopsis has a single PSY gene. | Locus annotation, gene-family analysis, experimental transcript/protein studies | Meier et al., May 2011; Álvarez et al., Oct. 2016; Navarro-Carcelen & Rodriguez-Concepcion, Apr. 2025 (alvarez2016carotenogenesisisregulated pages 1-5, navarrocarcelen2025experimentalvalidationof pages 1-3, meier2011atranscriptionalanalysis pages 4-6) |
| Ambiguity warning | Tomato, tobacco, algae, and other species also use **PSY1** for distinct homologs. Findings about tomato PSY1 or other non-Arabidopsis proteins must not be assigned to At5g17230/P37271. | Cross-species gene-family comparison | Ezquerro et al., July 2023: tomato has PSY1–PSY3, whereas Arabidopsis has one PSY (ezquerro2023overlappingandspecialized pages 1-2) |
| Primary reaction | Catalyzes head-to-head condensation of **2 geranylgeranyl diphosphate (GGPP)** molecules to form **15-cis-phytoene**, the first carotene produced in the pathway. | Biochemistry, heterologous activity assays, authoritative review | Zhou et al., Apr. 2022; Hou et al., July 2023 preprint (hou2023reducingpsyactivity pages 1-4, zhou2022phytoenesynthasethe pages 1-2) |
| Family/domain interpretation | The supplied UniProt assignment to the phytoene/squalene-synthase family and isoprenoid-synthase-related domains is consistent with the conserved catalytic architecture reported for P37271; exact domain boundaries are not asserted here. | Comparative sequence/structure inference | Zhou et al., Apr. 2022 (zhou2022phytoenesynthasethe pages 1-2) |
| Cellular localization | Synthesized as a precursor with an N-terminal plastid-targeting sequence and imported into plastids/chloroplasts. PSY has been detected in stromal and membrane-associated compartments; etioplast fractionation detected it in stroma and prolamellar-body/protothylakoid-associated fractions. | Targeting-sequence analysis, fluorescent proteins, chloroplast/etioplast fractionation and immunoblotting | Hou et al., July 2023 preprint; Navarro-Carcelen & Rodriguez-Concepcion, Apr. 2025 (hou2023reducingpsyactivity pages 1-4, navarrocarcelen2025experimentalvalidationof pages 1-3, hou2023reducingpsyactivity pages 39-42) |
| Pathway position | PSY commits plastidial MEP-pathway-derived GGPP to carotenoids. Phytoene is subsequently converted through phytofluene and ζ-carotene to lycopene, cyclic carotenes and xanthophylls; downstream carotenoids support photosynthesis and photoprotection and supply apocarotenoid and hormone precursors. | Pathway biochemistry and synthesis reviews | Álvarez et al., Oct. 2016; Zhou et al., Apr. 2022 (alvarez2016carotenogenesisisregulated pages 1-5, zhou2022phytoenesynthasethe pages 1-2) |
| 5′UTR/splicing regulation | Two experimentally studied transcripts differ mainly in their 5′UTRs: ASV1 has a **403-nt** 5′UTR with a translation-attenuating structure, whereas ASV2 has a **252-nt** 5′UTR lacking that element and supports rapid responses such as changing light or salt stress. | Transcript analysis and cell-free translation assays | Álvarez et al., Oct. 2016 (alvarez2016carotenogenesisisregulated pages 1-5, alvarez2016carotenogenesisisregulated pages 31-34, alvarez2016carotenogenesisisregulated pages 24-27) |
| OR regulation | AtOR and AtOR-like interact directly with PSY in plastids and regulate PSY chiefly post-transcriptionally. AtOR-overexpressing lines had **40–50×** more AtOR transcript, about **50% greater PSY activity**, and **>30% more phytoene** after norflurazon treatment, without a significant PSY-transcript increase. | Co-IP/MS, split-ubiquitin, BiFC, chloroplast enzyme assays and genetics | Zhou et al., Mar. 17, 2015 (zhou2015arabidopsisorproteins pages 1-2, zhou2015arabidopsisorproteins pages 2-2) |
| Clp proteostasis | OR acts as a holdase that preserves folded, active, membrane-associated PSY, whereas the plastid Clp system removes damaged or misfolded PSY; Clp deficiency can therefore accumulate both active and inactive enzyme. | Arabidopsis mutant genetics, co-IP and biochemical activity assays | Welsch et al., Jan. 2018 (welsch2018clpproteaseand pages 10-10) |
| FBN6—recent advance | FBN6 specifically binds and co-localizes with plant PSY in chloroplast membrane domains and increases catalytic output without measurably increasing PSY abundance. Arabidopsis **fbn6-1** shows reduced carotenoid production during de-etiolation and an attenuated carotenoid increase after **24 h at 600 µmol photons m⁻² s⁻¹** high light. | Co-IP, confocal co-localization, bacterial reconstitution, norflurazon-based activity assays and Arabidopsis mutant phenotyping | Iglesias-Sanchez et al., online Nov. 15, 2023; Plant Physiology 194, 2024 (iglesiassanchez2024arabidopsisfibrillin6influences pages 1-2, iglesiassanchez2024arabidopsisfibrillin6influences pages 2-3, iglesiassanchez2024arabidopsisfibrillin6influences pages 3-6, iglesiassanchez2024arabidopsisfibrillin6influences pages 7-9, iglesiassanchez2024arabidopsisfibrillin6influences pages 6-7) |
| Metabolic-engineering evidence | Constitutive AtPSY elevation had little effect on green seedling carotenoid concentration but increased carotenoids approximately **10× in callus** and **100× in roots**, reaching about **1,800** and **500 µg g⁻¹ dry weight**, respectively, with carotenoid crystal formation in non-green plastids. | Transgenic Arabidopsis, pigment quantification, immunoblotting and polarization microscopy | Maass et al., July 2009; quantitative values reported in the study abstract summarized in the literature search |
| Functional interpretation | PSY is the principal flux-control point at the entry to Arabidopsis carotenoid biosynthesis, but output depends on substrate supply, plastid context, downstream capacity, localization and proteostasis; increased PSY abundance alone therefore does not guarantee higher carotenoid concentration in green tissues. | Integrated biochemical, genetic and metabolic evidence | Álvarez et al., Oct. 2016; Zhou et al., Apr. 2022; Iglesias-Sanchez et al., 2024 (zhou2022phytoenesynthasethe pages 1-2, alvarez2016carotenogenesisisregulated pages 31-34, iglesiassanchez2024arabidopsisfibrillin6influences pages 3-6) |


*Table: Compact evidence map for the identity, catalytic function, localization, regulation, pathway role, and engineering potential of Arabidopsis thaliana PSY/At5g17230/P37271. It also separates this target from unrelated same-symbol PSY1 genes in other organisms.*

## 1. Identity verification and nomenclature

### Verified target

- **Organism:** *Arabidopsis thaliana* (mouse-ear cress).
- **Gene/locus:** **PSY; At5g17230**.
- **Protein:** phytoene synthase, UniProt **P37271**.
- **Enzyme class:** EC 2.5.1.32.
- **Biological context:** plastidial carotenoid biosynthesis.

Independent Arabidopsis literature identifies At5g17230 as PSY, and comparative work describes it as the sole PSY gene in this species. This matches the supplied UniProt identity and organism. (alvarez2016carotenogenesisisregulated pages 1-5, navarrocarcelen2025experimentalvalidationof pages 1-3, meier2011atranscriptionalanalysis pages 4-6)

### Symbol ambiguity

The label **PSY1 is intrinsically ambiguous across species**. For example, tomato PSY1 is one member of a three-gene family and is strongly associated with fruit chromoplast carotenogenesis; it is not the same gene as Arabidopsis At5g17230. Consequently, tomato, tobacco, watermelon, algal, and other PSY1 results can inform general enzyme biology but cannot establish the target’s annotation. (ezquerro2023overlappingandspecialized pages 1-2)

A recent transcript-model reassessment also found that database-predicted Arabidopsis protein isoforms require caution. At5g17230.1, .2, and .4 encode the common AtPSY protein, whereas the predicted At5g17230.3 “AtPSYextra” contains an additional 15 residues. The latter transcript could not be amplified from several Arabidopsis cDNA sources, and synthetic AtPSYextra showed little or no detectable carotenoid-producing activity relative to natural AtPSY in heterologous systems. Thus, the canonical enzyme—not the computationally predicted extended protein—is the experimentally supported functional product. This study was published in April 2025 and postdates the requested 2023–2024 priority window, but it is directly relevant to annotation accuracy: https://doi.org/10.1007/s00299-025-03482-1. (navarrocarcelen2025experimentalvalidationof pages 1-3)

## 2. Molecular function and substrate specificity

AtPSY catalyzes:

**2 GGPP → 15-cis-phytoene + diphosphate-derived leaving products**

The essential substrate specificity is therefore for **geranylgeranyl diphosphate**, a C20 prenyl diphosphate; two molecules are condensed head-to-head to make the C40 carotene skeleton. Phytoene is the first carotene produced and the first pathway-specific product of carotenogenesis. The reaction commits GGPP away from competing plastidial isoprenoid outputs and into carotenoids. (alvarez2016carotenogenesisisregulated pages 1-5, hou2023reducingpsyactivity pages 1-4, zhou2022phytoenesynthasethe pages 1-2)

The supplied InterPro assignments—phytoene/squalene synthase, isoprenoid-synthase-related, and conserved squalene/phytoene-synthase signatures—are consistent with this chemistry. An authoritative 2022 review specifically associates Arabidopsis P37271 with the conserved PSY catalytic architecture and active-site motifs. The family relationship to squalene synthases reflects a shared head-to-head prenyl-diphosphate condensation fold; it does **not** imply that AtPSY functions physiologically as a squalene synthase. https://doi.org/10.3389/fpls.2022.884720, published April 2022. (zhou2022phytoenesynthasethe pages 1-2)

Direct functional support includes plant and bacterial complementation systems, chloroplast-membrane activity assays, norflurazon-dependent phytoene accumulation, and the loss or reduction of activity caused by mutations affecting substrate-pocket or metal-binding regions. A 2023 Arabidopsis study associated P178S with possible metal-binding effects, A352T with substrate binding, and M266I with the substrate-pocket region. https://doi.org/10.1101/2023.06.29.546996, posted July 2023. (hou2023reducingpsyactivity pages 36-39)

No strong evidence was found that AtPSY uses an alternative physiological substrate in vivo. Its defensible primary annotation is therefore **GGPP-specific phytoene synthase**.

## 3. Cellular and suborganellar localization

AtPSY is synthesized as a **precursor carrying an N-terminal plastid-targeting sequence** and is imported into plastids. Its catalytic role is executed in chloroplasts of green tissues and in other plastid types—including etioplasts and non-green plastids—according to developmental context. The plastid assignment agrees with the localization of both precursor production and downstream carotenoid enzymes. (navarrocarcelen2025experimentalvalidationof pages 1-3, zhou2022phytoenesynthasethe pages 1-2)

At the suborganellar level, PSY is not adequately described as exclusively soluble or exclusively membrane-bound. Arabidopsis fractionation detected PSY in **stroma and prolamellar-body/protothylakoid-associated fractions of etioplasts**. Recent variant work similarly reported stromal and protothylakoid-membrane localization without gross relocalization of the tested hypomorphic variants. (hou2023reducingpsyactivity pages 1-4, hou2023reducingpsyactivity pages 39-42)

Interaction studies place functional PSY-containing assemblies in plastid membrane-associated domains. OR–PSY bimolecular fluorescence complementation localized the interaction to chloroplasts, while FBN6 and PSY fusion proteins co-localized in discrete chloroplast domains interpreted as envelope- or thylakoid-associated rather than plastoglobule cores. Thus, the best current model is a **dynamic plastid enzyme partitioned between stromal and membrane-associated states**, with membrane recruitment and local protein partners influencing activity. (zhou2015arabidopsisorproteins pages 2-2, iglesiassanchez2024arabidopsisfibrillin6influences pages 2-3)

## 4. Pathway position and biological processes

Plastidial GGPP is supplied principally from the methylerythritol-phosphate pathway. AtPSY channels two GGPP molecules into phytoene; desaturation and isomerization then produce phytofluene, ζ-carotene, and lycopene, followed by cyclization and hydroxylation to β-carotene, α-carotene, and xanthophylls. (alvarez2016carotenogenesisisregulated pages 1-5, zhou2022phytoenesynthasethe pages 1-2)

The direct role of PSY is **biosynthetic flux initiation**, not light harvesting or hormone signaling per se. Nevertheless, its downstream products have several precise functions:

1. Carotenoids are structural and photoprotective components of the photosynthetic apparatus.
2. Xanthophyll-cycle pigments dissipate excess excitation energy.
3. Carotenoid cleavage supplies precursors for abscisic acid, strigolactones, and other apocarotenoid signals.
4. Changes in PSY flux can consequently alter plastid development and retrograde signaling.

Arabidopsis expression-network analysis found PSY strongly co-expressed with carotenoid, chlorophyll, plastoquinone, phylloquinone, Calvin-cycle, and MEP-pathway genes. Approximately 1,000 genes had expression correlation *r* > 0.6 and approximately 600 had *r* > 0.7, consistent with coordinated assembly of photosynthetic and plastid-isoprenoid systems. https://doi.org/10.1186/1752-0509-5-77, published May 2011. (meier2011atranscriptionalanalysis pages 4-6)

The 2023 variant study adds a more specific signaling interpretation. Partial reductions in PSY activity altered selected acyclic cis-carotenes and the PIF3/HY5 regulatory balance in a *crtiso/ccr2* background without necessarily changing total xanthophyll or total cis-carotene pools. The authors infer a threshold-dependent, still-unidentified cis-carotene-derived apocarotenoid signal influencing etioplast and chloroplast development. Because the 2023 source was a preprint at retrieval, that mechanistic interpretation should be treated as emerging rather than settled. (hou2023reducingpsyactivity pages 1-4, hou2023reducingpsyactivity pages 39-42)

## 5. Regulation of functional PSY

### 5.1 Transcript and 5′-UTR control

Arabidopsis produces two experimentally studied PSY transcript variants with different 5′ untranslated regions. ASV1 has a **403-nucleotide 5′UTR** containing a predicted translation-attenuating hairpin or riboswitch-like structure. ASV2 has a **252-nucleotide 5′UTR** lacking that element and is favored when rapid increases in pathway flux are required, including sudden light changes and salt stress. The coding product is essentially the same; regulation occurs primarily through translation efficiency rather than altered catalytic specificity. https://doi.org/10.1104/pp.16.01262, published October 2016. (alvarez2016carotenogenesisisregulated pages 1-5, alvarez2016carotenogenesisisregulated pages 31-34, alvarez2016carotenogenesisisregulated pages 24-27)

This mechanism helps reconcile PSY transcript abundance with enzyme activity: transcript measurements alone can be a poor proxy for active plastidial PSY.

### 5.2 ORANGE proteins

AtOR and AtOR-like directly interact with PSY in plastids. Evidence includes co-immunoprecipitation/mass spectrometry, split-ubiquitin assays, transient co-IP, and chloroplast-localized bimolecular fluorescence complementation. Single *ator* mutants had limited effects, whereas the double mutant greatly reduced PSY protein, indicating partial redundancy. (zhou2015arabidopsisorproteins pages 1-2, zhou2015arabidopsisorproteins pages 2-2)

Quantitatively, AtOR-overexpressing lines had **40–50-fold more AtOR transcript** but no significant increase in PSY transcript. Nevertheless, chloroplast-membrane PSY activity rose by about **50%**, and norflurazon-treated leaves accumulated **more than 30% additional phytoene**. These results establish OR proteins as major **post-transcriptional/post-translational regulators of active PSY** rather than conventional transcriptional activators. Zhou et al., PNAS, published March 17, 2015: https://doi.org/10.1073/pnas.1420831112. (zhou2015arabidopsisorproteins pages 2-2)

### 5.3 Clp protease and protein quality control

The plastid Clp system and OR act as a proteostasis balance. OR has holdase/chaperone-like activity, stabilizes folded PSY, and promotes the membrane-associated active pool. Misfolded or aggregated PSY can be recognized through ClpC1, with possible ClpS1 participation, unfolded, and degraded by the Clp core. Clp impairment permits accumulation of both functional and nonfunctional PSY; therefore, increased PSY protein does not necessarily mean proportionally increased catalytic activity. Welsch et al., January 2018: https://doi.org/10.1016/j.molp.2017.11.003. (welsch2018clpproteaseand pages 10-10)

### 5.4 FIBRILLIN6: principal 2024 advance

The most important recent Arabidopsis-specific development is the identification of **FIBRILLIN6 (FBN6)** as a direct positive regulator of PSY activity. Arabidopsis FBN6 co-immunoprecipitated with PSY, whereas FBN4 did not, supporting specificity. FBN6 and PSY co-localized in chloroplast membrane domains. In a bacterial reconstitution system, FBN6 increased carotenoid output from plant PSY despite similar PSY protein levels, but did not stimulate bacterial CrtB. In *Nicotiana benthamiana*, FBN6 increased phytoene production, particularly when PSY was coexpressed. (iglesiassanchez2024arabidopsisfibrillin6influences pages 1-2, iglesiassanchez2024arabidopsisfibrillin6influences pages 2-3, iglesiassanchez2024arabidopsisfibrillin6influences pages 3-6)

FBN6 did not measurably alter PSY abundance, protease accessibility, degradation behavior, or carotenoid stability in the relevant assays. The evidence therefore favors **direct catalytic stimulation**, distinct from OR-mediated stabilization. The proposed possibility that FBN6 facilitates removal of hydrophobic phytoene from the active site is biologically plausible but remains speculative. (iglesiassanchez2024arabidopsisfibrillin6influences pages 3-6, iglesiassanchez2024arabidopsisfibrillin6influences pages 7-9)

Physiologically, Arabidopsis *fbn6-1* mutants showed reduced carotenoid production during the first 24 hours of seedling de-etiolation and delayed chlorophyll accumulation. In nine-day-old seedlings exposed for 24 hours to **600 µmol photons m⁻² s⁻¹**, the normal high-light increase in carotenoids was strongly attenuated in *fbn6-1*, even though FBN6 and PSY transcript levels were not substantially induced. This reinforces the conclusion that activity is regulated at the protein level. Iglesias-Sanchez et al., *Plant Physiology* 194:1662–1673, online November 15, 2023 and assigned to the 2024 volume: https://doi.org/10.1093/plphys/kiad613. (iglesiassanchez2024arabidopsisfibrillin6influences pages 3-6, iglesiassanchez2024arabidopsisfibrillin6influences pages 7-9, iglesiassanchez2024arabidopsisfibrillin6influences pages 6-7)

## 6. Phenotypes, quantitative evidence, and applications

PSY is an attractive metabolic-engineering target because it controls entry into the carotenoid pathway. However, its effects are highly tissue dependent.

Constitutive AtPSY overexpression left carotenoid concentration in green Arabidopsis seedlings largely unchanged despite increased PSY abundance and plastid import. In nonphotosynthetic tissues, by contrast, carotenoids increased approximately **10-fold in callus** and **100-fold in roots**, reaching approximately **1,800 and 500 µg g⁻¹ dry weight**, respectively. Carotenoids were deposited in crystals, demonstrating that increasing one entry-point enzyme can induce both biosynthesis and sequestration in non-green plastids. Maass et al., July 2009: https://doi.org/10.1371/journal.pone.0006373.

The contrast between leaves and roots is mechanistically informative. Photosynthetic tissues maintain tightly buffered pigment stoichiometry, downstream capacity, and photosystem assembly; excess PSY flux can therefore be compensated. Non-green tissues have lower baseline carotenoid production and can respond dramatically when increased synthesis is coupled to sequestration. Translational feedback was also observed: expression of heterologous PSY proteins reduced endogenous AtPSY protein without changing endogenous PSY transcripts. (alvarez2016carotenogenesisisregulated pages 31-34)

### Current and prospective implementations

1. **Carotenoid biofortification:** PSY overexpression is a standard strategy for increasing provitamin-A and total carotenoids in crop storage tissues. Arabidopsis demonstrates both its potential and the requirement for an adequate sink.
2. **Coengineering regulators:** OR can increase the stable active PSY pool, while FBN6 offers a conceptually different strategy—raising catalytic output without necessarily raising PSY abundance.
3. **Tissue-specific expression:** Because constitutive PSY elevation is buffered in green tissues but highly effective in roots and callus, storage-organ or fruit-specific promoters are generally preferable.
4. **Flux-and-sink engineering:** Combining PSY with precursor supply, downstream enzymes, plastid differentiation, or carotenoid sequestration is likely to be more robust than PSY overexpression alone.
5. **Stress acclimation:** FBN6-dependent stimulation under high light suggests that manipulating the PSY regulatory complex could strengthen rapid carotenoid deployment, although agronomic benefits require crop-specific validation. (zhou2015arabidopsisorproteins pages 2-2, iglesiassanchez2024arabidopsisfibrillin6influences pages 3-6, iglesiassanchez2024arabidopsisfibrillin6influences pages 6-7)

## 7. Expert assessment and remaining uncertainties

The field’s prevailing view is that PSY is the first committed and usually major rate-limiting enzyme of plant carotenogenesis, but “rate limiting” is conditional rather than absolute. Functional output depends on GGPP supply, plastid type, downstream conversion capacity, sequestration, and the fraction of PSY that is correctly folded and productively localized. The observation that Clp-deficient tissues can accumulate PSY without increased in-vitro activity, and that green leaves can buffer PSY overexpression, directly supports this more nuanced model. (zhou2022phytoenesynthasethe pages 1-2, alvarez2016carotenogenesisisregulated pages 31-34, welsch2018clpproteaseand pages 10-10)

Three uncertainties remain important:

- A high-resolution experimental structure of Arabidopsis PSY and a complete kinetic substrate profile remain less developed than pathway-level genetics and proteostasis studies.
- PSY’s exact distribution among plastid membrane microdomains is dynamic and condition dependent; “chloroplast-localized” is secure, but a single invariant subcompartment is not.
- The cis-carotene-derived developmental signal inferred from partial PSY variants remains chemically unidentified. (hou2023reducingpsyactivity pages 1-4, hou2023reducingpsyactivity pages 39-42)

## Final functional annotation

**At5g17230/P37271 encodes the single canonical Arabidopsis phytoene synthase, a plastid-imported phytoene/squalene-synthase-family enzyme that condenses two GGPP molecules to 15-cis-phytoene. It operates at the stromal–plastid-membrane interface and controls entry into carotenoid biosynthesis. Its biologically active pool is governed by transcript/5′UTR regulation, OR-dependent stabilization and membrane association, Clp-dependent quality control, and FBN6-dependent catalytic stimulation. Its primary consequences are carotenoid production for photosynthesis and photoprotection and provision of precursors for carotenoid-derived hormones and signals.**

References

1. (navarrocarcelen2025experimentalvalidationof pages 1-3): Juan Navarro-Carcelen and Manuel Rodriguez-Concepcion. Experimental validation of computationally predicted phytoene synthase isoforms encoded by the arabidopsis thaliana psy gene. Plant Cell Reports, Apr 2025. URL: https://doi.org/10.1007/s00299-025-03482-1, doi:10.1007/s00299-025-03482-1. This article has 2 citations and is from a peer-reviewed journal.

2. (meier2011atranscriptionalanalysis pages 4-6): Stuart Meier, Oren Tzfadia, Ratnakar Vallabhaneni, Chris Gehring, and Eleanore T Wurtzel. A transcriptional analysis of carotenoid, chlorophyll and plastidial isoprenoid biosynthesis genes during development and osmotic stress responses in arabidopsis thaliana. BMC Systems Biology, 5:77-77, May 2011. URL: https://doi.org/10.1186/1752-0509-5-77, doi:10.1186/1752-0509-5-77. This article has 197 citations and is from a peer-reviewed journal.

3. (ezquerro2023overlappingandspecialized pages 1-2): Miguel Ezquerro, Esteban Burbano-Erazo, and Manuel Rodriguez-Concepcion. Overlapping and specialized roles of tomato phytoene synthases in carotenoid and abscisic acid production. Plant Physiology, 193:2021-2036, Jul 2023. URL: https://doi.org/10.1093/plphys/kiad425, doi:10.1093/plphys/kiad425. This article has 57 citations and is from a highest quality peer-reviewed journal.

4. (alvarez2016carotenogenesisisregulated pages 1-5): Daniel Álvarez, Björn Voß, Dirk Maass, Florian Wüst, Patrick Schaub, Peter Beyer, and Ralf Welsch. Carotenogenesis is regulated by 5′utr-mediated translation of phytoene synthase splice variants. Plant Physiology, 172(4):2314-2326, Oct 2016. URL: https://doi.org/10.1104/pp.16.01262, doi:10.1104/pp.16.01262. This article has 99 citations and is from a highest quality peer-reviewed journal.

5. (zhou2022phytoenesynthasethe pages 1-2): Xuesong Zhou, Sombir Rao, Emalee Wrightstone, Tianhu Sun, Andy Cheuk Woon Lui, Ralf Welsch, and Li Li. Phytoene synthase: the key rate-limiting enzyme of carotenoid biosynthesis in plants. Frontiers in Plant Science, Apr 2022. URL: https://doi.org/10.3389/fpls.2022.884720, doi:10.3389/fpls.2022.884720. This article has 194 citations.

6. (hou2023reducingpsyactivity pages 1-4): Xin Hou, Yagiz Alagoz, Ralf Welsch, Matthew D Mortimer, Barry J. Pogson, and Christopher I. Cazzonelli. Reducing psy activity fine tunes threshold levels of a cis-carotene-derived signal that regulates the pif3/hy5 module and plastid biogenesis. bioRxiv, Jul 2023. URL: https://doi.org/10.1101/2023.06.29.546996, doi:10.1101/2023.06.29.546996. This article has 0 citations.

7. (hou2023reducingpsyactivity pages 39-42): Xin Hou, Yagiz Alagoz, Ralf Welsch, Matthew D Mortimer, Barry J. Pogson, and Christopher I. Cazzonelli. Reducing psy activity fine tunes threshold levels of a cis-carotene-derived signal that regulates the pif3/hy5 module and plastid biogenesis. bioRxiv, Jul 2023. URL: https://doi.org/10.1101/2023.06.29.546996, doi:10.1101/2023.06.29.546996. This article has 0 citations.

8. (alvarez2016carotenogenesisisregulated pages 31-34): Daniel Álvarez, Björn Voß, Dirk Maass, Florian Wüst, Patrick Schaub, Peter Beyer, and Ralf Welsch. Carotenogenesis is regulated by 5′utr-mediated translation of phytoene synthase splice variants. Plant Physiology, 172(4):2314-2326, Oct 2016. URL: https://doi.org/10.1104/pp.16.01262, doi:10.1104/pp.16.01262. This article has 99 citations and is from a highest quality peer-reviewed journal.

9. (alvarez2016carotenogenesisisregulated pages 24-27): Daniel Álvarez, Björn Voß, Dirk Maass, Florian Wüst, Patrick Schaub, Peter Beyer, and Ralf Welsch. Carotenogenesis is regulated by 5′utr-mediated translation of phytoene synthase splice variants. Plant Physiology, 172(4):2314-2326, Oct 2016. URL: https://doi.org/10.1104/pp.16.01262, doi:10.1104/pp.16.01262. This article has 99 citations and is from a highest quality peer-reviewed journal.

10. (zhou2015arabidopsisorproteins pages 1-2): Xiangjun Zhou, Ralf Welsch, Yong Yang, Daniel Álvarez, Matthias Riediger, Hui Yuan, Tara Fish, Jiping Liu, Theodore W. Thannhauser, and Li Li. Arabidopsis or proteins are the major posttranscriptional regulators of phytoene synthase in controlling carotenoid biosynthesis. Proceedings of the National Academy of Sciences, 112:3558-3563, Feb 2015. URL: https://doi.org/10.1073/pnas.1420831112, doi:10.1073/pnas.1420831112. This article has 350 citations and is from a highest quality peer-reviewed journal.

11. (zhou2015arabidopsisorproteins pages 2-2): Xiangjun Zhou, Ralf Welsch, Yong Yang, Daniel Álvarez, Matthias Riediger, Hui Yuan, Tara Fish, Jiping Liu, Theodore W. Thannhauser, and Li Li. Arabidopsis or proteins are the major posttranscriptional regulators of phytoene synthase in controlling carotenoid biosynthesis. Proceedings of the National Academy of Sciences, 112:3558-3563, Feb 2015. URL: https://doi.org/10.1073/pnas.1420831112, doi:10.1073/pnas.1420831112. This article has 350 citations and is from a highest quality peer-reviewed journal.

12. (welsch2018clpproteaseand pages 10-10): Ralf Welsch, Xiangjun Zhou, Hui Yuan, Daniel Álvarez, Tianhu Sun, Dennis Schlossarek, Yong Yang, Guoxin Shen, Hong Zhang, Manuel Rodriguez-Concepcion, Theodore W. Thannhauser, and Li Li. Clp protease and or directly control the proteostasis of phytoene synthase, the crucial enzyme for carotenoid biosynthesis in arabidopsis. Molecular plant, 11 1:149-162, Jan 2018. URL: https://doi.org/10.1016/j.molp.2017.11.003, doi:10.1016/j.molp.2017.11.003. This article has 161 citations and is from a highest quality peer-reviewed journal.

13. (iglesiassanchez2024arabidopsisfibrillin6influences pages 1-2): Ariadna Iglesias-Sanchez, Juan Navarro-Carcelen, Luca Morelli, and Manuel Rodriguez-Concepcion. Arabidopsis fibrillin6 influences carotenoid biosynthesis by directly promoting phytoene synthase activity. Plant Physiology, 194:1662-1673, Nov 2024. URL: https://doi.org/10.1093/plphys/kiad613, doi:10.1093/plphys/kiad613. This article has 23 citations and is from a highest quality peer-reviewed journal.

14. (iglesiassanchez2024arabidopsisfibrillin6influences pages 2-3): Ariadna Iglesias-Sanchez, Juan Navarro-Carcelen, Luca Morelli, and Manuel Rodriguez-Concepcion. Arabidopsis fibrillin6 influences carotenoid biosynthesis by directly promoting phytoene synthase activity. Plant Physiology, 194:1662-1673, Nov 2024. URL: https://doi.org/10.1093/plphys/kiad613, doi:10.1093/plphys/kiad613. This article has 23 citations and is from a highest quality peer-reviewed journal.

15. (iglesiassanchez2024arabidopsisfibrillin6influences pages 3-6): Ariadna Iglesias-Sanchez, Juan Navarro-Carcelen, Luca Morelli, and Manuel Rodriguez-Concepcion. Arabidopsis fibrillin6 influences carotenoid biosynthesis by directly promoting phytoene synthase activity. Plant Physiology, 194:1662-1673, Nov 2024. URL: https://doi.org/10.1093/plphys/kiad613, doi:10.1093/plphys/kiad613. This article has 23 citations and is from a highest quality peer-reviewed journal.

16. (iglesiassanchez2024arabidopsisfibrillin6influences pages 7-9): Ariadna Iglesias-Sanchez, Juan Navarro-Carcelen, Luca Morelli, and Manuel Rodriguez-Concepcion. Arabidopsis fibrillin6 influences carotenoid biosynthesis by directly promoting phytoene synthase activity. Plant Physiology, 194:1662-1673, Nov 2024. URL: https://doi.org/10.1093/plphys/kiad613, doi:10.1093/plphys/kiad613. This article has 23 citations and is from a highest quality peer-reviewed journal.

17. (iglesiassanchez2024arabidopsisfibrillin6influences pages 6-7): Ariadna Iglesias-Sanchez, Juan Navarro-Carcelen, Luca Morelli, and Manuel Rodriguez-Concepcion. Arabidopsis fibrillin6 influences carotenoid biosynthesis by directly promoting phytoene synthase activity. Plant Physiology, 194:1662-1673, Nov 2024. URL: https://doi.org/10.1093/plphys/kiad613, doi:10.1093/plphys/kiad613. This article has 23 citations and is from a highest quality peer-reviewed journal.

18. (hou2023reducingpsyactivity pages 36-39): Xin Hou, Yagiz Alagoz, Ralf Welsch, Matthew D Mortimer, Barry J. Pogson, and Christopher I. Cazzonelli. Reducing psy activity fine tunes threshold levels of a cis-carotene-derived signal that regulates the pif3/hy5 module and plastid biogenesis. bioRxiv, Jul 2023. URL: https://doi.org/10.1101/2023.06.29.546996, doi:10.1101/2023.06.29.546996. This article has 0 citations.

## Artifacts

- [Edison artifact artifact-00](PSY-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. ezquerro2023overlappingandspecialized pages 1-2
2. zhou2022phytoenesynthasethe pages 1-2
3. welsch2018clpproteaseand pages 10-10
4. navarrocarcelen2025experimentalvalidationof pages 1-3
5. hou2023reducingpsyactivity pages 36-39
6. meier2011atranscriptionalanalysis pages 4-6
7. zhou2015arabidopsisorproteins pages 2-2
8. alvarez2016carotenogenesisisregulated pages 31-34
9. alvarez2016carotenogenesisisregulated pages 1-5
10. hou2023reducingpsyactivity pages 1-4
11. hou2023reducingpsyactivity pages 39-42
12. alvarez2016carotenogenesisisregulated pages 24-27
13. zhou2015arabidopsisorproteins pages 1-2
14. https://doi.org/10.1007/s00299-025-03482-1.
15. https://doi.org/10.3389/fpls.2022.884720,
16. https://doi.org/10.1101/2023.06.29.546996,
17. https://doi.org/10.1186/1752-0509-5-77,
18. https://doi.org/10.1104/pp.16.01262,
19. https://doi.org/10.1073/pnas.1420831112.
20. https://doi.org/10.1016/j.molp.2017.11.003.
21. https://doi.org/10.1093/plphys/kiad613.
22. https://doi.org/10.1371/journal.pone.0006373.
23. https://doi.org/10.1007/s00299-025-03482-1,
24. https://doi.org/10.1093/plphys/kiad425,
25. https://doi.org/10.1073/pnas.1420831112,
26. https://doi.org/10.1016/j.molp.2017.11.003,
27. https://doi.org/10.1093/plphys/kiad613,