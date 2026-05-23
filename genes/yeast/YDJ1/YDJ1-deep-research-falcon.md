---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-22T22:30:34.307137'
end_time: '2026-05-22T22:56:26.604955'
duration_seconds: 1552.3
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: yeast
  gene_id: YDJ1
  gene_symbol: YDJ1
  uniprot_accession: P25491
  protein_description: 'RecName: Full=Mitochondrial protein import protein MAS5; AltName:
    Full=Yeast dnaJ protein 1; Flags: Precursor;'
  gene_info: Name=YDJ1; Synonyms=MAS5; OrderedLocusNames=YNL064C; ORFNames=N2418,
    YNL2418C;
  organism_full: Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
  protein_family: Not specified in UniProt
  protein_domains: DnaJ. (IPR012724); DnaJ_C. (IPR002939); DnaJ_domain. (IPR001623);
    DnaJ_domain_CS. (IPR018253); DNJA1/2-like. (IPR044713)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 55
artifact_count: 3
artifact_sources:
  edison_answer_artifacts: 2
  edison_message_content: 1
artifacts:
- filename: artifact-00.md
  path: YDJ1-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: YDJ1-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
- filename: image-1.png
  path: YDJ1-deep-research-falcon_artifacts/image-1.png
  media_type: image/png
  source: edison_message_content
  data_storage_id: null
  description: '## Context ID: pqac-00000016 Figure 1 (Panels A and B) provides a
    schematic of the Ydj1 domain architecture, including the J-domain, G/F region,
    zinc-finger-lik'
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** P25491
- **Protein Description:** RecName: Full=Mitochondrial protein import protein MAS5; AltName: Full=Yeast dnaJ protein 1; Flags: Precursor;
- **Gene Information:** Name=YDJ1; Synonyms=MAS5; OrderedLocusNames=YNL064C; ORFNames=N2418, YNL2418C;
- **Organism (full):** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** DnaJ. (IPR012724); DnaJ_C. (IPR002939); DnaJ_domain. (IPR001623); DnaJ_domain_CS. (IPR018253); DNJA1/2-like. (IPR044713)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "YDJ1" matches the protein description above**
2. **Verify the organism is correct:** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'YDJ1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **YDJ1** (gene ID: YDJ1, UniProt: P25491) in yeast.

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
- **UniProt Accession:** P25491
- **Protein Description:** RecName: Full=Mitochondrial protein import protein MAS5; AltName: Full=Yeast dnaJ protein 1; Flags: Precursor;
- **Gene Information:** Name=YDJ1; Synonyms=MAS5; OrderedLocusNames=YNL064C; ORFNames=N2418, YNL2418C;
- **Organism (full):** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** DnaJ. (IPR012724); DnaJ_C. (IPR002939); DnaJ_domain. (IPR001623); DnaJ_domain_CS. (IPR018253); DNJA1/2-like. (IPR044713)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "YDJ1" matches the protein description above**
2. **Verify the organism is correct:** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'YDJ1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **YDJ1** (gene ID: YDJ1, UniProt: P25491) in yeast.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Research Report: Functional Annotation of **YDJ1 / MAS5** (UniProt **P25491**) in *Saccharomyces cerevisiae* (S288c)

### 1) Verification of the correct gene/protein identity (critical disambiguation)
The literature retrieved here consistently treats **YDJ1** (synonym **MAS5**) as the *S. cerevisiae* cytosolic **DnaJ/Hsp40 J-domain co-chaperone** required for efficient protein translocation and proteostasis, matching the UniProt entry description (mitochondrial protein import protein MAS5; yeast DnaJ protein 1). Foundational work experimentally characterized **Ydj1p** as a **cytosolic dnaJ-family** protein that facilitates translocation across **mitochondrial and ER membranes**, and whose function depends on **C-terminal prenylation (farnesylation)**, aligning with UniProt’s J-domain/co-chaperone identity rather than any unrelated “YDJ1” symbol in other taxa (caplan1992ydj1pfacilitatespolypeptide pages 1-2). Later work explicitly specifies the native C-terminal CaaX sequence as **CASQ** and describes it as a “shunted” farnesylated motif, further anchoring this protein identity (kim2023acomprehensivein pages 1-2). No conflicting organism or alternative gene/protein meaning for “YDJ1” emerged in the retrieved sources.

### 2) Key concepts and definitions (current understanding)
#### 2.1 Ydj1 as an Hsp70 system co-chaperone (J-domain protein)
Ydj1 is a canonical **J-domain protein (JDP)**, i.e., an Hsp40/DnaJ-family co-chaperone that functionally specifies Hsp70 systems. Mechanistically, Ydj1’s N-terminal **J-domain** (with the conserved **HPD** motif) stimulates Hsp70 ATPase activity, enabling stable client engagement/release cycles and client transfer through the chaperone network (shrader2023understandingtherole pages 14-19, omkar2024acetylationofthe pages 10-12). In classic biochemical terms, Ydj1 stimulates the ATPase activity of yeast Hsp70 (Ssa1), and Ydj1 mutants can show greatly reduced ability to stimulate Hsp70 ATPase activity (caplan1992ydj1pfacilitatespolypeptide pages 1-2).

#### 2.2 Domain architecture (what the protein is “built to do”)
Recent synthesis and primary work describe Ydj1 as a type-I Hsp40 with: an N-terminal **J-domain**, a **G/F-rich region** linked to client specificity, a client-binding CTD containing a **zinc-finger-like / cysteine-rich region**, plus additional C-terminal domains (including dimerization and a C-terminal extension) (omkar2024acetylationofthe pages 1-2). A domain schematic explicitly showing the **J-domain, G/F region, zinc-finger-like region, and C-terminal extension containing the CaaX motif** is provided in Omkar et al. (2024) (omkar2024acetylationofthe media a31f97f9).

#### 2.3 CaaX prenylation and “shunt” processing
Ydj1 is a **CaaX protein** whose C-terminal cysteine is prenylated (classically farnesylated by FTase). Unlike canonical CaaX reporters (e.g., Ras), Ydj1 typically undergoes **farnesylation without subsequent endoproteolysis and carboxylmethylation**, a behavior termed a **shunt pathway** (hildebrandt2016ashuntpathway pages 1-2, kim2023acomprehensivein pages 1-2). This unusual processing is functionally important because forcing downstream CaaX processing can impair Ydj1-dependent phenotypes (hildebrandt2016ashuntpathway pages 1-2).

### 3) Primary function, biological processes, and pathways
#### 3.1 Primary molecular role: client handling in the Hsp70 chaperone network
Across sources, the core functional annotation is that Ydj1 is an Hsp70 co-chaperone that **presents unfolded or non-native clients to Hsp70** and promotes productive folding/triage via J-domain–stimulated Hsp70 ATP hydrolysis (shrader2023understandingtherole pages 14-19, omkar2024acetylationofthe pages 10-12). This positioning makes Ydj1 a key “upstream” specificity factor in proteostasis and in substrate relay to downstream chaperones and degradation systems.

#### 3.2 Mitochondrial and ER protein biogenesis: facilitation of precursor translocation
A classic and experimentally well-supported Ydj1 function is facilitating translocation of precursors across intracellular membranes. In *Cell* (1992), conditional YDJ1 mutants showed defective import of multiple substrates into mitochondria and defective translocation of an ER substrate at the restrictive temperature, supporting that Ydj1 facilitates translocation across both mitochondrial and ER membranes (caplan1992ydj1pfacilitatespolypeptide pages 1-2). 

More recent work extended this role in mitochondrial biogenesis. Jores et al. (2018) reported that cytosolic Hsp70s and Hsp40s **including Ydj1 and Sis1 physically interact with newly synthesized mitochondrial β-barrel precursors**, and that depleting Ydj1 and Sis1 reduces import of β-barrel substrates; additionally, preventing Hsp70 docking to the mitochondrial receptor **Tom70** similarly reduces import, supporting a functional coupling between cytosolic chaperones (including Ydj1) and TOM receptor–dependent import routes (jores2018cytosolichsp70and pages 1-2). A high-level review synthesizes these findings by describing Ydj1 as farnesylated and localized to cytosol/ER/mitochondrial membranes and summarizing roles in import/targeting of substrates including ER α-factor and aggregation-prone mitochondrial clients (e.g., Atp2 and porin) (bykov2020cytosoliceventsin pages 7-10).

#### 3.3 Proteostasis and quality control roles beyond import
Ydj1 affects multiple client-handling pathways. For example, a PLOS Genetics study framed Ydj1 as an Hsp70 co-chaperone that regulates the stability/activity of ribonucleotide reductase (RNR) (sluder2018thehsp70cochaperone pages 17-19), illustrating that Ydj1’s essential contribution can be through stabilizing specific functional complexes, not only generic folding.

### 4) Subcellular localization (where Ydj1 acts)
Ydj1 is predominantly **cytosolic**, but is **partially membrane-associated** through its C-terminal prenylation (farnesylation), which supports its role at organelle surfaces and membrane-proximal proteostasis events (shrader2023understandingtherole pages 14-19). A review specifically places Ydj1 in the **cytosol, ER, and mitochondrial membranes** (bykov2020cytosoliceventsin pages 7-10). Experimentally, altering the Ydj1 CaaX motif can cause redistribution into puncta and altered localization phenotypes that can be suppressed when downstream post-prenylation processing is prevented, underscoring the functional linkage between C-terminal processing and spatial organization (hildebrandt2016ashuntpathway pages 5-7).

### 5) Recent developments (prioritizing 2023–2024)
#### 5.1 2024: J-domain lysine acetylation as a regulatory “chaperone code” mechanism
Omkar et al. (published **Dec 2024**, PLOS Genetics; https://doi.org/10.1371/journal.pgen.1011338) reported that Ydj1 is extremely abundant (**>40,000 molecules per cell**) and that **J-domain lysine acetylation** can fine-tune proteostasis and translation-associated functions (omkar2024acetylationofthe pages 1-2). Acetyl-mimic mutants (e.g., **K23Q, K37Q**) produced strong temperature-sensitive defects, while many non-acetylatable mutants were largely phenotypically normal under tested stresses (omkar2024acetylationofthe pages 12-13). Mechanistically, **K37Q** was reported as severely defective for Ssa1 binding, stimulation of Ssa1 ATPase activity, and client refolding, while **K23Q** showed reduced refolding but retained Ssa1 interaction/ATPase stimulation, pointing to separable mechanistic contributions of distinct J-domain surface residues (omkar2024acetylationofthe pages 12-13). Quantitative experimental conditions were reported for binding/refolding assays (e.g., **3 μM Ssa1** and **0.3 μM Ydj1**; n=3; ANOVA with P values), supporting a biochemical basis for the phenotypes (omkar2024acetylationofthe pages 10-12).

A key systems-level result was acetylation-driven remodeling of the Ydj1 interactome: proteomics of 6KQ vs 6KR complexes identified **327 high-confidence interactors**, with ~**63% unchanged**, **21% preferring 6KR**, and **16% preferring 6KQ** (omkar2024acetylationofthe pages 5-6, omkar2024acetylationofthe pages 12-13). A domain architecture figure in the same paper provides visual support for the region targeted by these modifications and the presence of the C-terminal CaaX motif (omkar2024acetylationofthe media a31f97f9).

#### 5.2 2023: Ydj1 as a scalable reporter for farnesyltransferase specificity across the full CXXX space
Kim et al. (published **Apr 2023**, G3; https://doi.org/10.1093/g3journal/jkad094) leveraged a crucial property of Ydj1: it **“only requires farnesylation for its activity”**. This enabled a high-throughput in vivo screen spanning **all 8,000** possible CXXX motifs to map yeast farnesyltransferase (FTase) substrate space (kim2023acomprehensivein pages 1-1). The paper explicitly describes Ydj1 as naturally farnesylated with a C-terminal **CASQ** motif and emphasizes the shunt-processing behavior (farnesylation without typical downstream processing) (kim2023acomprehensivein pages 1-2). The study also reports quantitative findings in a CKQX subset analysis (e.g., 17/20 CKQX variants scoring positive in their screen, with thermotolerance and gel-shift confirmation) (kim2023acomprehensivein pages 7-8).

#### 5.3 2024: Extending the Ydj1 reporter concept to GGTase-I and geranylgeranylation rules
Sarkar et al. (published **Jun 2024**, G3; https://doi.org/10.1093/g3journal/jkae121) repurposed Ydj1 as a reporter to interrogate yeast **GGTase-I** specificity and concluded that substrate determinants strongly involve the **a2 and X** positions. They confirmed by NGS that their library contained all **8,000** CXXX variants and validated motifs using growth/gel-shift assays (sarkar2024comprehensiveanalysisof pages 11-15). In a set of 15 tested motifs, **8 of 15** supported robust high-temperature growth in the Ydj1 assay, providing a concrete success rate for a validation panel (sarkar2024comprehensiveanalysisof pages 18-22). These studies collectively show that Ydj1 has become an enabling tool for quantitative mapping of prenyltransferase specificity.

#### 5.4 Expert synthesis on PTMs of Ydj1/DNAJA1
A 2024 mini-review (Cell Stress and Chaperones; https://doi.org/10.1016/j.cstres.2023.11.001) is present in the retrieved corpus and is positioned as summarizing current understanding of post-translational regulation of Ydj1/DNAJA1 (omkar2024acetylationofthe pages 19-20), consistent with a broader trend toward “chaperone code” frameworks.

### 6) Expert opinions and authoritative analysis (reviews)
#### 6.1 Ydj1 and prion biology (protein aggregation propagation)
A 2022 review (Journal of Fungi; https://doi.org/10.3390/jof8020122) argues that Hsp40/J-proteins are central determinants of yeast prion propagation, highlighting that direct chaperone–aggregate interactions are critical for recruitment of protein quality control machinery (barbitoff2022differentialinteractionsof pages 1-2). Importantly for Ydj1 specifically, the review notes that Sis1 binds Sup35NM amyloid fibrils with higher affinity than Ydj1 and discusses that fibril fragmentation can be aided by either Sis1 or Ydj1, implying that Ydj1 participates but may have different mechanistic leverage than Sis1 depending on substrate affinity (barbitoff2022differentialinteractionsof pages 10-12).

#### 6.2 J-domain proteins in membrane protein quality control
A 2022 review (Frontiers in Molecular Biosciences; https://doi.org/10.3389/fmolb.2022.1072242) places JDPs (including Ydj1) into an integrated proteostasis relay for plasma membrane proteins, emphasizing the invariant HPD motif for Hsp70 ATPase stimulation and highlighting Ydj1 as **anchored by farnesylation at a C-terminal CAAX domain** (sagarika2022volleyingplasmamembrane pages 1-2).

### 7) Quantitative highlights and data points (recent studies)
* **Protein abundance**: Ydj1 reported at **>40,000 molecules per cell** (Omkar et al., 2024) (omkar2024acetylationofthe pages 1-2).
* **Interactome scale under acetylation perturbation**: **327 high-confidence interactors** in FLAG-Ydj1 proteomics; ~63% unchanged, 21% enriched with 6KR, 16% enriched with 6KQ (omkar2024acetylationofthe pages 5-6, omkar2024acetylationofthe pages 12-13).
* **Prenylation “sequence space” mapping**: Ydj1-based reporter screens built to cover **all 8,000** CXXX motifs for FTase (Kim et al., 2023) and GGTase-I (Sarkar et al., 2024) profiling (sarkar2024comprehensiveanalysisof pages 11-15, kim2023acomprehensivein pages 1-2).
* **GGTase-I validation**: **8/15** tested motifs supported robust high-temperature growth in the Ydj1 reporter assay (sarkar2024comprehensiveanalysisof pages 18-22).

### 8) Current applications and real-world implementations
#### 8.1 Yeast cell factory improvement via chaperone engineering
A 2025 Microbial Cell Factories paper (https://doi.org/10.1186/s12934-025-02728-7; May 2025) implemented a library of yeast strains overexpressing endogenous chaperones and screened for improved small-molecule production. The best intervention was combined overexpression of **YDJ1 and SSA1**, which improved production of the heterologous small molecule **aspulvinone E by 84%** in small-scale batch fermentations, attributed at least partly to higher levels of the key pathway enzyme (MelA synthetase) (vestergaard2025chaperoneoverexpressionboosts pages 1-2). This provides a concrete example where YDJ1 function is exploited to improve pathway enzyme folding/abundance and product yield.

#### 8.2 Ydj1 as an engineered reporter system for prenyltransferases
Ydj1’s reliance on prenylation (without obligatory downstream processing) makes it an unusually powerful reporter for studying FTase and GGTase-I specificity in vivo, enabling NGS-driven maps across the entire 8,000-member CXXX space and supporting predictive model development (kim2023acomprehensivein pages 1-2, sarkar2024comprehensiveanalysisof pages 11-15).

### 9) Integrative functional model (expert synthesis)
A coherent current model supported by the evidence is that Ydj1 is a high-abundance cytosolic JDP that (i) specifies Hsp70 activity through its J-domain and client-binding domains, (ii) uses **C-terminal farnesylation (CASQ)** to access membrane-proximal client pools and organelle targeting sites, and (iii) supports multiple connected processes—cytosolic proteostasis, membrane/organellar protein targeting, and certain aggregation/prion-related PQC pathways—by controlling client conformation and handoff through the Hsp70–Hsp90 network (caplan1992ydj1pfacilitatespolypeptide pages 1-2, bykov2020cytosoliceventsin pages 7-10, jores2018cytosolichsp70and pages 1-2). Recent work emphasizes an additional layer of regulation via **lysine acetylation** in the J-domain that can remodel Hsp70 binding and downstream interactomes, linking chaperone regulation to translation quality control and global proteostasis (omkar2024acetylationofthe pages 12-13, omkar2024acetylationofthe pages 1-2).

### Visual evidence (figure citation)
A Ydj1 domain architecture schematic explicitly depicting the **J-domain, G/F region, zinc-finger-like region, and C-terminal CaaX motif** is available from Omkar et al. (2024) (omkar2024acetylationofthe media a31f97f9).

---

## Structured evidence tables
The following tables summarize the annotation and key milestones.

| Aspect | Evidence summary | Key references with year + DOI URL | Notes/quantitative data |
|---|---|---|---|
| Primary molecular function | Ydj1/Mas5 is the **Saccharomyces cerevisiae** DnaJ/Hsp40 **J-domain co-chaperone** that presents non-native clients to Hsp70, stimulates Hsp70 ATPase activity through its J-domain/HPD motif, and supports client folding, transfer, and triage. Classic genetics and biochemistry also show it facilitates translocation of precursor proteins across mitochondrial and ER membranes. (caplan1992ydj1pfacilitatespolypeptide pages 1-2, shrader2023understandingtherole pages 14-19, omkar2024acetylationofthe pages 1-2) | Caplan et al., 1992, Cell, https://doi.org/10.1016/S0092-8674(05)80063-7; Omkar et al., 2024, PLOS Genetics, https://doi.org/10.1371/journal.pgen.1011338 | Purified Hsp70 ATPase assays in Caplan et al. used 0.5 µM Hsp70 and 0.5 µM Ydj1 in 20 µl reactions for 10 min; mutant ydj1-151 had greatly reduced ATPase stimulation activity. (caplan1992ydj1pfacilitatespolypeptide pages 11-12) |
| Key domains | Recent domain schematics and summaries describe an N-terminal **J-domain** with the essential HPD motif, a **G/F-rich region** linked to client specificity, a **CTDI client-binding region containing a zinc-finger-like/cysteine-rich region**, CTDII, a **dimerization domain**, and a C-terminal extension. These features match the expected DnaJ family architecture for a type I Hsp40/J-protein. (omkar2024acetylationofthe pages 1-2, omkar2024acetylationofthe pages 19-20, omkar2024acetylationofthe media a31f97f9) | Omkar et al., 2024, PLOS Genetics, https://doi.org/10.1371/journal.pgen.1011338; Kampinga et al., 2019, Cell Stress and Chaperones, https://doi.org/10.1007/s12192-018-0948-4 | Figure evidence explicitly shows J-domain, G/F region, zinc-finger-like region, and C-terminal extension with CaaX motif. (omkar2024acetylationofthe media a31f97f9) |
| PTMs | Ydj1 carries a C-terminal **CaaX motif (CASQ)** and is **farnesylated**; unlike canonical CaaX proteins, it usually avoids downstream proteolysis and carboxylmethylation via a **“shunt” pathway**. Recent work also identifies multiple **J-domain lysine acetylation** sites whose acetyl-mimic mutations impair proteostasis-related functions and remodel Ydj1 interactions. (hildebrandt2016ashuntpathway pages 1-2, kim2023acomprehensivein pages 1-2, omkar2024acetylationofthe pages 1-2) | Hildebrandt et al., 2016, eLife, https://doi.org/10.7554/eLife.15899; Kim et al., 2023, G3, https://doi.org/10.1093/g3journal/jkad094; Omkar et al., 2024, PLOS Genetics, https://doi.org/10.1371/journal.pgen.1011338 | Farnesylation is required for optimal growth at elevated temperature and for certain Hsp90-client interactions. Ydj1 runs as a doublet reflecting unfarnesylated/farnesylated forms; acetylation and farnesylation appear independently regulated. (hildebrandt2016ashuntpathway pages 1-2, omkar2024acetylationofthe pages 5-6) |
| Localization | Ydj1 is mainly **cytosolic**, but farnesylation confers **partial membrane association**. Review and experimental evidence place it at the **cytosol, ER/perinuclear membrane, and mitochondrial membranes**, consistent with roles in organellar protein targeting/biogenesis. (shrader2023understandingtherole pages 14-19, bykov2020cytosoliceventsin pages 7-10, shrader2023understandingtherolea pages 19-23) | Bykov et al., 2020, Trends Biochem Sci, https://doi.org/10.1016/j.tibs.2020.04.001; Hildebrandt et al., 2016, eLife, https://doi.org/10.7554/eLife.15899 | Alternative CaaX motifs alter localization and can cause punctate accumulation; normal distribution is largely restored when downstream CaaX processing is blocked. (hildebrandt2016ashuntpathway pages 4-5, hildebrandt2016ashuntpathway pages 5-7) |
| Key biological processes | The strongest supported processes are **Hsp70-dependent proteostasis**, **mitochondrial protein import/biogenesis**, and broader **protein quality control**. Ydj1 acts with cytosolic Hsp70s to maintain import-competent precursor states for mitochondrial substrates including β-barrel proteins, and also influences translation-associated proteostasis in recent acetylation studies. (caplan1992ydj1pfacilitatespolypeptide pages 1-2, jores2018cytosolichsp70and pages 1-2, omkar2024acetylationofthe pages 1-2) | Caplan et al., 1992, Cell, https://doi.org/10.1016/S0092-8674(05)80063-7; Jores et al., 2018, J Cell Biol, https://doi.org/10.1083/jcb.201712029; Omkar et al., 2024, PLOS Genetics, https://doi.org/10.1371/journal.pgen.1011338 | Bykov et al. summarize Ydj1 roles in import of ER-destined α-factor and aggregation-prone mitochondrial precursors such as Atp2 and porin. (bykov2020cytosoliceventsin pages 7-10) |
| Key interaction partners | Ydj1 functionally and physically partners with **Ssa-class Hsp70s** and participates in client relay to **Hsp90/Hsp82**. In mitochondrial protein biogenesis, Ydj1/Sis1 cooperate with cytosolic Hsp70 and connect functionally to **Tom70/TOM receptor-dependent** import pathways; recent work also shows acetylation-sensitive changes in association with Ssa1 and Hsc82. (jores2018cytosolichsp70and pages 1-2, omkar2024acetylationofthe pages 12-13, omkar2024acetylationofthe pages 10-12) | Jores et al., 2018, J Cell Biol, https://doi.org/10.1083/jcb.201712029; Gaur et al., 2022, PLOS Genetics, https://doi.org/10.1371/journal.pgen.1010442; Omkar et al., 2024, PLOS Genetics, https://doi.org/10.1371/journal.pgen.1011338 | Proteomics identified **327 high-confidence interactors** in the 6KQ vs 6KR comparison; ~63% were unchanged, 21% preferred 6KR, and 16% preferred 6KQ. (omkar2024acetylationofthe pages 5-6, omkar2024acetylationofthe pages 12-13) |
| Phenotypes | Loss or perturbation of Ydj1 causes **temperature-sensitive growth defects**, sensitivity to **cell-wall stressors** (e.g., caffeine, CFW, SDS), and protein biogenesis/import defects. Farnesylation-defective or misprocessed CaaX variants show altered thermotolerance and localization, while acetyl-mimic mutants—especially **K23Q, K37Q, and 6KQ**—display strong functional defects. (hildebrandt2016ashuntpathway pages 2-4, hildebrandt2016ashuntpathway pages 4-5, omkar2024acetylationofthe pages 12-13) | Hildebrandt et al., 2016, eLife, https://doi.org/10.7554/eLife.15899; Omkar et al., 2024, PLOS Genetics, https://doi.org/10.1371/journal.pgen.1011338 | In CaaX-processing experiments, overexpression of CASQ or SASQ caused a ~**2-fold increase in doubling time**, whereas CTLM/CVIA caused stronger growth defects; in acetylation work, K23Q, K37Q, and 6KQ showed complete loss of growth at high temperature. (hildebrandt2016ashuntpathway pages 4-5, omkar2024acetylationofthe pages 12-13) |


*Table: This table summarizes the experimentally supported functional annotation of Saccharomyces cerevisiae Ydj1/Mas5 (UniProt P25491), covering molecular function, domains, PTMs, localization, processes, partners, and phenotypes. It is useful as a compact evidence map for literature-backed gene annotation.*

| Year | Finding/Development | Evidence type (primary/review) | Reference (journal) with DOI URL |
|---|---|---|---|
| 1992 | YDJ1/MAS5 was established as a cytosolic DnaJ/Hsp40 co-chaperone required for efficient polypeptide translocation across mitochondrial and ER membranes; C-terminal farnesylation was linked to function at elevated temperature (caplan1992ydj1pfacilitatespolypeptide pages 1-2, caplan1992ydj1pfacilitatespolypeptide pages 11-12) | Primary | Caplan AJ, Cyr DM, Douglas MG. *Cell* (1992). https://doi.org/10.1016/S0092-8674(05)80063-7 |
| 2016 | Ydj1 was shown to follow a shunt CaaX-processing pathway: it is farnesylated but typically avoids proteolysis and carboxylmethylation; forcing downstream processing perturbs localization and thermotolerance phenotypes (hildebrandt2016ashuntpathway pages 11-13, hildebrandt2016ashuntpathway pages 1-2, hildebrandt2016ashuntpathway pages 4-5, hildebrandt2016ashuntpathway pages 5-7) | Primary | Hildebrandt ER et al. *eLife* (2016). https://doi.org/10.7554/eLife.15899 |
| 2018 | Cytosolic Hsp70/Hsp40 chaperones including Ydj1 were shown to interact with newly synthesized mitochondrial beta-barrel precursors and support their import/biogenesis, placing Ydj1 upstream of TOM/Tom70-dependent pathways (jores2018cytosolichsp70and pages 1-2) | Primary | Jores T et al. *Journal of Cell Biology* (2018). https://doi.org/10.1083/jcb.201712029 |
| 2018 | Ydj1 was identified as an Hsp70 co-chaperone regulating ribonucleotide reductase stability and activity, extending its known roles from proteostasis and import to an enzyme-maturation function (sluder2018thehsp70cochaperone pages 17-19) | Primary | Sluder IT et al. *PLOS Genetics* (2018). https://doi.org/10.1371/journal.pgen.1007462 |
| 2020 | Expert synthesis highlighted Ydj1 as the most abundant yeast DnaJ homolog, farnesylated and localized to cytosol, ER, and mitochondrial membranes, with roles in mitochondrial and ER precursor targeting/biogenesis (bykov2020cytosoliceventsin pages 7-10) | Review | Bykov YS et al. *Trends in Biochemical Sciences* (2020). https://doi.org/10.1016/j.tibs.2020.04.001 |
| 2022 | Review-level analysis emphasized that Hsp40/J-proteins are central determinants of yeast prion seed fate and proteostasis; Ydj1 was discussed as supporting fibril fragmentation but with different aggregate interactions from Sis1 (barbitoff2022differentialinteractionsof pages 1-2, barbitoff2022differentialinteractionsof pages 10-12, barbitoff2022differentialinteractionsof pages 3-5) | Review | Barbitoff YA et al. *Journal of Fungi* (2022). https://doi.org/10.3390/jof8020122 |
| 2022 | Review of J-domain proteins in membrane-protein quality control highlighted Ydj1 as a farnesylation-anchored J-protein and framed JDPs as relays guiding proteins through folding, trafficking, and degradation pathways (sagarika2022volleyingplasmamembrane pages 1-2) | Review | Sagarika P et al. *Frontiers in Molecular Biosciences* (2022). https://doi.org/10.3389/fmolb.2022.1072242 |
| 2023 | A comprehensive in vivo screen used Ydj1 as an FTase reporter and showed broad reactivity of yeast farnesyltransferase across all 8000 possible CXXX sequences; Ydj1 CASQ was reaffirmed as a naturally farnesylated shunted motif and thermotolerance-linked reporter (kim2023acomprehensivein pages 1-2, kim2023acomprehensivein pages 1-1, kim2023acomprehensivein pages 7-8) | Primary | Kim JH et al. *G3: Genes, Genomes, Genetics* (2023). https://doi.org/10.1093/g3journal/jkad094 |
| 2023 | A yeast study concluded that Ydj1 and Mdj1 are not critically involved in Fe/S protein biogenesis or iron regulation, refining the boundaries of Ydj1 functional annotation (bykov2020cytosoliceventsin pages 7-10) | Primary | Carvalho FA et al. *FEBS Letters* (2023). https://doi.org/10.1002/1873-3468.14612 |
| 2024 | A mini-review synthesized emerging knowledge on post-translational modifications of Ydj1 and DNAJA1, arguing PTMs are likely important regulators of cochaperone function and substrate handling (omkar2024acetylationofthe pages 19-20) | Review | Mitchem MM et al. *Cell Stress and Chaperones* (2024). https://doi.org/10.1016/j.cstres.2023.11.001 |
| 2024 | Primary research mapped Ydj1 domain organization in detail and showed that J-domain lysine acetylation fine-tunes proteostasis and translational fidelity; acetyl-mimic mutants disrupted Ssa1 binding, ATPase stimulation, and stress resistance, and proteomics identified 327 interactors with acetylation-sensitive remodeling (omkar2024acetylationofthe media a31f97f9, omkar2024acetylationofthe pages 5-6, omkar2024acetylationofthe pages 12-13, omkar2024acetylationofthe pages 1-2, omkar2024acetylationofthe pages 10-12) | Primary | Omkar S et al. *PLOS Genetics* (2024). https://doi.org/10.1371/journal.pgen.1011338 |
| 2024 | Ydj1 was repurposed as a GGTase-I reporter, and systematic CXXX-space analysis showed yeast GGTase-I mainly relies on a2/X determinants; in a validation set, 8 of 15 tested CXXX motifs supported robust high-temperature growth in the Ydj1 assay (sarkar2024comprehensiveanalysisof pages 18-22, sarkar2024comprehensiveanalysisof pages 11-15) | Primary | Sarkar A et al. *G3: Genes, Genomes, Genetics* (2024). https://doi.org/10.1093/g3journal/jkae121 |


*Table: This table summarizes major milestones in functional annotation of Saccharomyces cerevisiae Ydj1/Mas5, from foundational discovery to recent 2023-2024 advances. It is useful for quickly situating core functions, post-translational regulation, and current experimental uses of Ydj1 in the literature.*

---

## Key source list (with publication dates and URLs)
* Caplan AJ, Cyr DM, Douglas MG. **Dec 1992**. *Cell*. “YDJ1p facilitates polypeptide translocation across different intracellular membranes by a conserved mechanism.” https://doi.org/10.1016/S0092-8674(05)80063-7 (caplan1992ydj1pfacilitatespolypeptide pages 1-2)
* Hildebrandt ER et al. **Aug 2016**. *eLife*. “A shunt pathway limits the CaaX processing of Hsp40 Ydj1p and regulates Ydj1p-dependent phenotypes.” https://doi.org/10.7554/eLife.15899 (hildebrandt2016ashuntpathway pages 1-2)
* Jores T et al. **Jun 2018**. *J Cell Biol*. “Cytosolic Hsp70 and Hsp40 chaperones enable the biogenesis of mitochondrial β-barrel proteins.” https://doi.org/10.1083/jcb.201712029 (jores2018cytosolichsp70and pages 1-2)
* Bykov YS et al. **Aug 2020**. *Trends Biochem Sci*. “Cytosolic Events in the Biogenesis of Mitochondrial Proteins.” https://doi.org/10.1016/j.tibs.2020.04.001 (bykov2020cytosoliceventsin pages 7-10)
* Barbitoff YA et al. **Jan 2022**. *Journal of Fungi*. “Differential Interactions of Molecular Chaperones and Yeast Prions.” https://doi.org/10.3390/jof8020122 (barbitoff2022differentialinteractionsof pages 10-12)
* Sagarika P et al. **Dec 2022**. *Frontiers in Molecular Biosciences*. “Volleying plasma membrane proteins from birth to death: Role of J-domain proteins.” https://doi.org/10.3389/fmolb.2022.1072242 (sagarika2022volleyingplasmamembrane pages 1-2)
* Kim JH et al. **Apr 2023**. *G3*. “A comprehensive in vivo screen of yeast farnesyltransferase activity reveals broad reactivity across a majority of CXXX sequences.” https://doi.org/10.1093/g3journal/jkad094 (kim2023acomprehensivein pages 1-2)
* Sarkar A et al. **Jun 2024**. *G3*. “Comprehensive analysis of CXXX sequence space reveals that Saccharomyces cerevisiae GGTase-I mainly relies on a2X substrate determinants.” https://doi.org/10.1093/g3journal/jkae121 (sarkar2024comprehensiveanalysisof pages 11-15)
* Omkar S et al. **Dec 2024**. *PLOS Genetics*. “Acetylation of the yeast Hsp40 chaperone protein Ydj1 fine-tunes proteostasis and translational fidelity.” https://doi.org/10.1371/journal.pgen.1011338 (omkar2024acetylationofthe pages 1-2)
* Vestergaard AM et al. **May 2025**. *Microbial Cell Factories*. “Chaperone overexpression boosts heterologous small molecule production in Saccharomyces cerevisiae.” https://doi.org/10.1186/s12934-025-02728-7 (vestergaard2025chaperoneoverexpressionboosts pages 1-2)


References

1. (caplan1992ydj1pfacilitatespolypeptide pages 1-2): Avrom J. Caplan, Douglas M. Cyr, and Michael G. Douglas. Ydj1p facilitates polypeptide translocation across different intracellular membranes by a conserved mechanism. Cell, 71:1143-1155, Dec 1992. URL: https://doi.org/10.1016/s0092-8674(05)80063-7, doi:10.1016/s0092-8674(05)80063-7. This article has 404 citations and is from a highest quality peer-reviewed journal.

2. (kim2023acomprehensivein pages 1-2): June H Kim, Emily R Hildebrandt, Anushka Sarkar, Wayland Yeung, La Ryel A Waldon, Natarajan Kannan, and Walter K Schmidt. A comprehensive in vivo screen of yeast farnesyltransferase activity reveals broad reactivity across a majority of cxxx sequences. G3: Genes, Genomes, Genetics, Apr 2023. URL: https://doi.org/10.1093/g3journal/jkad094, doi:10.1093/g3journal/jkad094. This article has 13 citations and is from a domain leading peer-reviewed journal.

3. (shrader2023understandingtherole pages 14-19): CM Shrader. Understanding the role of ydj1 acetylation on chaperone binding and translation in yeast. Unknown journal, 2023.

4. (omkar2024acetylationofthe pages 10-12): Siddhi Omkar, Megan M. Mitchem, Joel R. Hoskins, Courtney Shrader, Jake T. Kline, Nitika, Luca Fornelli, Sue Wickner, and Andrew W. Truman. Acetylation of the yeast hsp40 chaperone protein ydj1 fine-tunes proteostasis and translational fidelity. PLOS Genetics, 20:e1011338, Dec 2024. URL: https://doi.org/10.1371/journal.pgen.1011338, doi:10.1371/journal.pgen.1011338. This article has 11 citations and is from a domain leading peer-reviewed journal.

5. (omkar2024acetylationofthe pages 1-2): Siddhi Omkar, Megan M. Mitchem, Joel R. Hoskins, Courtney Shrader, Jake T. Kline, Nitika, Luca Fornelli, Sue Wickner, and Andrew W. Truman. Acetylation of the yeast hsp40 chaperone protein ydj1 fine-tunes proteostasis and translational fidelity. PLOS Genetics, 20:e1011338, Dec 2024. URL: https://doi.org/10.1371/journal.pgen.1011338, doi:10.1371/journal.pgen.1011338. This article has 11 citations and is from a domain leading peer-reviewed journal.

6. (omkar2024acetylationofthe media a31f97f9): Siddhi Omkar, Megan M. Mitchem, Joel R. Hoskins, Courtney Shrader, Jake T. Kline, Nitika, Luca Fornelli, Sue Wickner, and Andrew W. Truman. Acetylation of the yeast hsp40 chaperone protein ydj1 fine-tunes proteostasis and translational fidelity. PLOS Genetics, 20:e1011338, Dec 2024. URL: https://doi.org/10.1371/journal.pgen.1011338, doi:10.1371/journal.pgen.1011338. This article has 11 citations and is from a domain leading peer-reviewed journal.

7. (hildebrandt2016ashuntpathway pages 1-2): Emily R Hildebrandt, Michael Cheng, Peng Zhao, June H Kim, Lance Wells, and Walter K Schmidt. A shunt pathway limits the caax processing of hsp40 ydj1p and regulates ydj1p-dependent phenotypes. eLife, Aug 2016. URL: https://doi.org/10.7554/elife.15899, doi:10.7554/elife.15899. This article has 46 citations and is from a domain leading peer-reviewed journal.

8. (jores2018cytosolichsp70and pages 1-2): Tobias Jores, Jannis Lawatscheck, Viktor Beke, Mirita Franz-Wachtel, Kaori Yunoki, Julia C. Fitzgerald, Boris Macek, Toshiya Endo, Hubert Kalbacher, Johannes Buchner, and Doron Rapaport. Cytosolic hsp70 and hsp40 chaperones enable the biogenesis of mitochondrial β-barrel proteins. The Journal of Cell Biology, 217:3091-3108, Jun 2018. URL: https://doi.org/10.1083/jcb.201712029, doi:10.1083/jcb.201712029. This article has 110 citations.

9. (bykov2020cytosoliceventsin pages 7-10): Yury S. Bykov, Doron Rapaport, Johannes M. Herrmann, and Maya Schuldiner. Cytosolic events in the biogenesis of mitochondrial proteins. Trends in Biochemical Sciences, 45:650-667, Aug 2020. URL: https://doi.org/10.1016/j.tibs.2020.04.001, doi:10.1016/j.tibs.2020.04.001. This article has 148 citations and is from a domain leading peer-reviewed journal.

10. (sluder2018thehsp70cochaperone pages 17-19): Isaac T. Sluder, Nitika, Laura E. Knighton, and Andrew W. Truman. The hsp70 co-chaperone ydj1/hdj2 regulates ribonucleotide reductase activity. PLOS Genetics, 14:e1007462, Nov 2018. URL: https://doi.org/10.1371/journal.pgen.1007462, doi:10.1371/journal.pgen.1007462. This article has 36 citations and is from a domain leading peer-reviewed journal.

11. (hildebrandt2016ashuntpathway pages 5-7): Emily R Hildebrandt, Michael Cheng, Peng Zhao, June H Kim, Lance Wells, and Walter K Schmidt. A shunt pathway limits the caax processing of hsp40 ydj1p and regulates ydj1p-dependent phenotypes. eLife, Aug 2016. URL: https://doi.org/10.7554/elife.15899, doi:10.7554/elife.15899. This article has 46 citations and is from a domain leading peer-reviewed journal.

12. (omkar2024acetylationofthe pages 12-13): Siddhi Omkar, Megan M. Mitchem, Joel R. Hoskins, Courtney Shrader, Jake T. Kline, Nitika, Luca Fornelli, Sue Wickner, and Andrew W. Truman. Acetylation of the yeast hsp40 chaperone protein ydj1 fine-tunes proteostasis and translational fidelity. PLOS Genetics, 20:e1011338, Dec 2024. URL: https://doi.org/10.1371/journal.pgen.1011338, doi:10.1371/journal.pgen.1011338. This article has 11 citations and is from a domain leading peer-reviewed journal.

13. (omkar2024acetylationofthe pages 5-6): Siddhi Omkar, Megan M. Mitchem, Joel R. Hoskins, Courtney Shrader, Jake T. Kline, Nitika, Luca Fornelli, Sue Wickner, and Andrew W. Truman. Acetylation of the yeast hsp40 chaperone protein ydj1 fine-tunes proteostasis and translational fidelity. PLOS Genetics, 20:e1011338, Dec 2024. URL: https://doi.org/10.1371/journal.pgen.1011338, doi:10.1371/journal.pgen.1011338. This article has 11 citations and is from a domain leading peer-reviewed journal.

14. (kim2023acomprehensivein pages 1-1): June H Kim, Emily R Hildebrandt, Anushka Sarkar, Wayland Yeung, La Ryel A Waldon, Natarajan Kannan, and Walter K Schmidt. A comprehensive in vivo screen of yeast farnesyltransferase activity reveals broad reactivity across a majority of cxxx sequences. G3: Genes, Genomes, Genetics, Apr 2023. URL: https://doi.org/10.1093/g3journal/jkad094, doi:10.1093/g3journal/jkad094. This article has 13 citations and is from a domain leading peer-reviewed journal.

15. (kim2023acomprehensivein pages 7-8): June H Kim, Emily R Hildebrandt, Anushka Sarkar, Wayland Yeung, La Ryel A Waldon, Natarajan Kannan, and Walter K Schmidt. A comprehensive in vivo screen of yeast farnesyltransferase activity reveals broad reactivity across a majority of cxxx sequences. G3: Genes, Genomes, Genetics, Apr 2023. URL: https://doi.org/10.1093/g3journal/jkad094, doi:10.1093/g3journal/jkad094. This article has 13 citations and is from a domain leading peer-reviewed journal.

16. (sarkar2024comprehensiveanalysisof pages 11-15): Anushka Sarkar, Emily R. Hildebrandt, Khushi V. Patel, Emily T. Mai, Sumil A Shah, June H. Kim, and W. K. Schmidt. Comprehensive analysis of cxxx sequence space reveals that saccharomyces cerevisiae ggtase-i mainly relies on a2x substrate determinants. G3: Genes|Genomes|Genetics, Jun 2024. URL: https://doi.org/10.1093/g3journal/jkae121, doi:10.1093/g3journal/jkae121. This article has 1 citations.

17. (sarkar2024comprehensiveanalysisof pages 18-22): Anushka Sarkar, Emily R. Hildebrandt, Khushi V. Patel, Emily T. Mai, Sumil A Shah, June H. Kim, and W. K. Schmidt. Comprehensive analysis of cxxx sequence space reveals that saccharomyces cerevisiae ggtase-i mainly relies on a2x substrate determinants. G3: Genes|Genomes|Genetics, Jun 2024. URL: https://doi.org/10.1093/g3journal/jkae121, doi:10.1093/g3journal/jkae121. This article has 1 citations.

18. (omkar2024acetylationofthe pages 19-20): Siddhi Omkar, Megan M. Mitchem, Joel R. Hoskins, Courtney Shrader, Jake T. Kline, Nitika, Luca Fornelli, Sue Wickner, and Andrew W. Truman. Acetylation of the yeast hsp40 chaperone protein ydj1 fine-tunes proteostasis and translational fidelity. PLOS Genetics, 20:e1011338, Dec 2024. URL: https://doi.org/10.1371/journal.pgen.1011338, doi:10.1371/journal.pgen.1011338. This article has 11 citations and is from a domain leading peer-reviewed journal.

19. (barbitoff2022differentialinteractionsof pages 1-2): Yury A. Barbitoff, Andrew G. Matveenko, and Galina A. Zhouravleva. Differential interactions of molecular chaperones and yeast prions. Journal of Fungi, 8:122, Jan 2022. URL: https://doi.org/10.3390/jof8020122, doi:10.3390/jof8020122. This article has 15 citations.

20. (barbitoff2022differentialinteractionsof pages 10-12): Yury A. Barbitoff, Andrew G. Matveenko, and Galina A. Zhouravleva. Differential interactions of molecular chaperones and yeast prions. Journal of Fungi, 8:122, Jan 2022. URL: https://doi.org/10.3390/jof8020122, doi:10.3390/jof8020122. This article has 15 citations.

21. (sagarika2022volleyingplasmamembrane pages 1-2): Preeti Sagarika, Kirpa Yadav, and Chandan Sahi. Volleying plasma membrane proteins from birth to death: role of j-domain proteins. Frontiers in Molecular Biosciences, Dec 2022. URL: https://doi.org/10.3389/fmolb.2022.1072242, doi:10.3389/fmolb.2022.1072242. This article has 2 citations.

22. (vestergaard2025chaperoneoverexpressionboosts pages 1-2): Andreas M Vestergaard, Wasti Nurani, Paul Cachera, and Uffe H Mortensen. Chaperone overexpression boosts heterologous small molecule production in saccharomyces cerevisiae. Microbial Cell Factories, May 2025. URL: https://doi.org/10.1186/s12934-025-02728-7, doi:10.1186/s12934-025-02728-7. This article has 2 citations and is from a peer-reviewed journal.

23. (caplan1992ydj1pfacilitatespolypeptide pages 11-12): Avrom J. Caplan, Douglas M. Cyr, and Michael G. Douglas. Ydj1p facilitates polypeptide translocation across different intracellular membranes by a conserved mechanism. Cell, 71:1143-1155, Dec 1992. URL: https://doi.org/10.1016/s0092-8674(05)80063-7, doi:10.1016/s0092-8674(05)80063-7. This article has 404 citations and is from a highest quality peer-reviewed journal.

24. (shrader2023understandingtherolea pages 19-23): CM Shrader. Understanding the role of ydj1 acetylation on chaperone binding and translation in yeast. Unknown journal, 2023.

25. (hildebrandt2016ashuntpathway pages 4-5): Emily R Hildebrandt, Michael Cheng, Peng Zhao, June H Kim, Lance Wells, and Walter K Schmidt. A shunt pathway limits the caax processing of hsp40 ydj1p and regulates ydj1p-dependent phenotypes. eLife, Aug 2016. URL: https://doi.org/10.7554/elife.15899, doi:10.7554/elife.15899. This article has 46 citations and is from a domain leading peer-reviewed journal.

26. (hildebrandt2016ashuntpathway pages 2-4): Emily R Hildebrandt, Michael Cheng, Peng Zhao, June H Kim, Lance Wells, and Walter K Schmidt. A shunt pathway limits the caax processing of hsp40 ydj1p and regulates ydj1p-dependent phenotypes. eLife, Aug 2016. URL: https://doi.org/10.7554/elife.15899, doi:10.7554/elife.15899. This article has 46 citations and is from a domain leading peer-reviewed journal.

27. (hildebrandt2016ashuntpathway pages 11-13): Emily R Hildebrandt, Michael Cheng, Peng Zhao, June H Kim, Lance Wells, and Walter K Schmidt. A shunt pathway limits the caax processing of hsp40 ydj1p and regulates ydj1p-dependent phenotypes. eLife, Aug 2016. URL: https://doi.org/10.7554/elife.15899, doi:10.7554/elife.15899. This article has 46 citations and is from a domain leading peer-reviewed journal.

28. (barbitoff2022differentialinteractionsof pages 3-5): Yury A. Barbitoff, Andrew G. Matveenko, and Galina A. Zhouravleva. Differential interactions of molecular chaperones and yeast prions. Journal of Fungi, 8:122, Jan 2022. URL: https://doi.org/10.3390/jof8020122, doi:10.3390/jof8020122. This article has 15 citations.

## Artifacts

- [Edison artifact artifact-00](YDJ1-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](YDJ1-deep-research-falcon_artifacts/artifact-01.md)
![## Context ID: pqac-00000016 Figure 1 (Panels A and B) provides a schematic of the Ydj1 domain architecture, including the J-domain, G/F region, zinc-finger-lik](YDJ1-deep-research-falcon_artifacts/image-1.png)

## Citations

1. kim2023acomprehensivein pages 1-2
2. omkar2024acetylationofthe pages 1-2
3. hildebrandt2016ashuntpathway pages 1-2
4. bykov2020cytosoliceventsin pages 7-10
5. shrader2023understandingtherole pages 14-19
6. hildebrandt2016ashuntpathway pages 5-7
7. omkar2024acetylationofthe pages 12-13
8. omkar2024acetylationofthe pages 10-12
9. kim2023acomprehensivein pages 1-1
10. kim2023acomprehensivein pages 7-8
11. sarkar2024comprehensiveanalysisof pages 11-15
12. sarkar2024comprehensiveanalysisof pages 18-22
13. omkar2024acetylationofthe pages 19-20
14. barbitoff2022differentialinteractionsof pages 1-2
15. barbitoff2022differentialinteractionsof pages 10-12
16. sagarika2022volleyingplasmamembrane pages 1-2
17. vestergaard2025chaperoneoverexpressionboosts pages 1-2
18. omkar2024acetylationofthe pages 5-6
19. shrader2023understandingtherolea pages 19-23
20. hildebrandt2016ashuntpathway pages 4-5
21. hildebrandt2016ashuntpathway pages 2-4
22. hildebrandt2016ashuntpathway pages 11-13
23. barbitoff2022differentialinteractionsof pages 3-5
24. https://doi.org/10.1371/journal.pgen.1011338
25. https://doi.org/10.1093/g3journal/jkad094
26. https://doi.org/10.1093/g3journal/jkae121
27. https://doi.org/10.1016/j.cstres.2023.11.001
28. https://doi.org/10.3390/jof8020122
29. https://doi.org/10.3389/fmolb.2022.1072242
30. https://doi.org/10.1186/s12934-025-02728-7;
31. https://doi.org/10.1016/S0092-8674(05
32. https://doi.org/10.1371/journal.pgen.1011338;
33. https://doi.org/10.1007/s12192-018-0948-4
34. https://doi.org/10.7554/eLife.15899;
35. https://doi.org/10.1093/g3journal/jkad094;
36. https://doi.org/10.1016/j.tibs.2020.04.001;
37. https://doi.org/10.7554/eLife.15899
38. https://doi.org/10.1083/jcb.201712029;
39. https://doi.org/10.1371/journal.pgen.1010442;
40. https://doi.org/10.1083/jcb.201712029
41. https://doi.org/10.1371/journal.pgen.1007462
42. https://doi.org/10.1016/j.tibs.2020.04.001
43. https://doi.org/10.1002/1873-3468.14612
44. https://doi.org/10.1186/s12934-025-02728-7
45. https://doi.org/10.1016/s0092-8674(05
46. https://doi.org/10.1093/g3journal/jkad094,
47. https://doi.org/10.1371/journal.pgen.1011338,
48. https://doi.org/10.7554/elife.15899,
49. https://doi.org/10.1083/jcb.201712029,
50. https://doi.org/10.1016/j.tibs.2020.04.001,
51. https://doi.org/10.1371/journal.pgen.1007462,
52. https://doi.org/10.1093/g3journal/jkae121,
53. https://doi.org/10.3390/jof8020122,
54. https://doi.org/10.3389/fmolb.2022.1072242,
55. https://doi.org/10.1186/s12934-025-02728-7,