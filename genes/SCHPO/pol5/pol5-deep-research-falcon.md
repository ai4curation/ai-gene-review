---
provider: falcon
model: Edison Scientific Literature
cached: true
start_time: '2026-05-30T19:20:19.821388'
end_time: '2026-05-30T19:20:19.823278'
duration_seconds: 0.0
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: SCHPO
  gene_id: pol5
  gene_symbol: pol5
  uniprot_accession: O60094
  protein_description: 'RecName: Full=rDNA transcriptional regulator pol5; AltName:
    Full=DNA polymerase V; Short=POL V; AltName: Full=DNA polymerase phi;'
  gene_info: Name=pol5; ORFNames=SPBC14C8.14c;
  organism_full: Schizosaccharomyces pombe (strain 972 / ATCC 24843) (Fission yeast).
  protein_family: Belongs to the MYBBP1A family. .
  protein_domains: ARM-type_fold. (IPR016024); DNA-dir_DNA_pol_B_CS. (IPR017964);
    DNA_pol_V/MYBBP1A. (IPR007015); DNA_pol_phi (PF04931)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 22
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 1
  edison_message_content: 1
artifacts:
- filename: artifact-00.md
  path: pol5-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: image-1.png
  path: pol5-deep-research-falcon_artifacts/image-1.png
  media_type: image/png
  source: edison_message_content
  data_storage_id: null
  description: '## Context ID: pqac-00000020 The entry for SPBC14C8.14c (clone TC48
    / DNA polymerase V) is located in Table 2 on page 9. It falls under the localization
    categor'
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** O60094
- **Protein Description:** RecName: Full=rDNA transcriptional regulator pol5; AltName: Full=DNA polymerase V; Short=POL V; AltName: Full=DNA polymerase phi;
- **Gene Information:** Name=pol5; ORFNames=SPBC14C8.14c;
- **Organism (full):** Schizosaccharomyces pombe (strain 972 / ATCC 24843) (Fission yeast).
- **Protein Family:** Belongs to the MYBBP1A family. .
- **Key Domains:** ARM-type_fold. (IPR016024); DNA-dir_DNA_pol_B_CS. (IPR017964); DNA_pol_V/MYBBP1A. (IPR007015); DNA_pol_phi (PF04931)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "pol5" matches the protein description above**
2. **Verify the organism is correct:** Schizosaccharomyces pombe (strain 972 / ATCC 24843) (Fission yeast).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'pol5' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **pol5** (gene ID: pol5, UniProt: O60094) in SCHPO.

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
- **UniProt Accession:** O60094
- **Protein Description:** RecName: Full=rDNA transcriptional regulator pol5; AltName: Full=DNA polymerase V; Short=POL V; AltName: Full=DNA polymerase phi;
- **Gene Information:** Name=pol5; ORFNames=SPBC14C8.14c;
- **Organism (full):** Schizosaccharomyces pombe (strain 972 / ATCC 24843) (Fission yeast).
- **Protein Family:** Belongs to the MYBBP1A family. .
- **Key Domains:** ARM-type_fold. (IPR016024); DNA-dir_DNA_pol_B_CS. (IPR017964); DNA_pol_V/MYBBP1A. (IPR007015); DNA_pol_phi (PF04931)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "pol5" matches the protein description above**
2. **Verify the organism is correct:** Schizosaccharomyces pombe (strain 972 / ATCC 24843) (Fission yeast).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'pol5' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **pol5** (gene ID: pol5, UniProt: O60094) in SCHPO.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Research report: *Schizosaccharomyces pombe* **pol5+** (UniProt **O60094**; ORF **SPBC14C8.14c**) — functional annotation

### Executive summary
The *S. pombe* gene **pol5+** (SPBC14C8.14c; UniProt O60094) encodes an essential, predominantly nuclear protein historically annotated as “DNA polymerase V/φ,” but experimental and comparative evidence supports its primary role in **ribosomal DNA (rDNA) / rRNA production and ribosome biogenesis**. In fission yeast, Pol5 is essential for viability, localizes to the nucleus in GFP-fusion studies, physically interacts with the cell-cycle transcription factor **Cdc10**, and is regulated by **Eso1-mediated lysine acetylation** at an essential conserved residue (**K47**). While direct mechanistic mapping of Pol5 to pre-ribosomal particles is currently strongest in budding yeast, these conserved functional data plus *S. pombe* genetics strongly support annotating fission-yeast Pol5 as a conserved ribosome biogenesis/rDNA transcription regulator rather than a replicative DNA polymerase. (nadeem2005pol5+apotential pages 199-202, nadeem2005pol5+apotential pages 1-9, chen2017dnapolymerase5 pages 3-6)

### 1) Key concepts and definitions (current understanding)

#### 1.1 What “Pol5” is (and is not)
- **Historical annotation ambiguity:** Pol5 has been historically classified with B-type DNA polymerases (“DNA polymerase V/phi”), including in early fission-yeast GFP-fusion screens, but later work in yeast indicates its dominant cellular function relates to **rRNA synthesis and ribosome assembly**, with any polymerase activity being weak/secondary. (nadeem2005pol5+apotential pages 116-121, ramossaenz2019pol5isan pages 1-2, ding2000large‐scalescreeningof media e191a246)
- **Functional framing:** In modern ribosome-biogenesis terminology, Pol5 is best conceptualized as a **trans-acting ribosome biogenesis factor** that couples rDNA transcription and/or co-transcriptional processing to productive ribosome assembly (strongest mechanistic support from *S. cerevisiae*). (braun2020pol5isrequired pages 1-2, ramossaenz2019pol5isan pages 1-2)

#### 1.2 rDNA transcription, ribosome biogenesis, and nucleolar organization
- **Division of labor among RNA polymerases:** In yeasts, rRNA production is distributed across polymerases: RNA Pol I produces the large rRNA precursor (18S/5.8S/25S-28S), Pol III transcribes 5S rRNA, and Pol II transcribes ribosomal protein genes. (hirai2023comparativeresearchregulatory pages 1-2)
- **Nucleolus/rDNA as a regulated hub:** rDNA transcription and nucleolar morphology respond rapidly to nutrient and stress signaling. In *S. pombe*, regulatory layers include **TOR signaling**, stress-responsive transcription factors, and **heterochromatin/RNAi-based repression** at rDNA repeats during starvation. (hirai2023comparativeresearchregulatory pages 2-4, hirai2023comparativeresearchregulatory pages 1-2)

### 2) Verified gene/protein identity and symbol disambiguation (mandatory verification)
Evidence from multiple *S. pombe* sources indicates that **pol5+** corresponds to **SPBC14C8.14c** and to the Pol5 protein described in the user’s UniProt context:
- A genome-scale GFP-fusion localization study lists **SPBC14C8.14c** (clone TC48) annotated as “DNA polymerase V” under a nuclear category, consistent with the historical Pol5 naming. (ding2000large‐scalescreeningof media e191a246, ding2000large‐scalescreeningof media b2dd5871)
- A *S. pombe* genetic/biochemical study of Pol5 acetylation by Eso1 explicitly studies “Pol5” in *S. pombe* and demonstrates essentiality of a conserved residue. (chen2017dnapolymerase5 pages 3-6, chen2017dnapolymerase5 pages 1-2)
- A fission-yeast thesis explicitly studies **pol5+**, reporting essentiality, nuclear localization, and interaction with **Cdc10**. (nadeem2005pol5+apotential pages 1-9)

### 3) Molecular function and biological processes for *S. pombe* Pol5

#### 3.1 Essential gene required for viability
- **Essentiality in *S. pombe*:** pol5+ disruption/analysis in the thesis work indicates **pol5+ is essential** for viability. (nadeem2005pol5+apotential pages 1-9)
- **Essential post-translational regulation:** Mutation of **Pol5 K47→R** is lethal in *S. pombe* (see §3.4). (chen2017dnapolymerase5 pages 3-6)

#### 3.2 Likely primary role: rRNA synthesis / ribosome biogenesis (supported by *S. pombe* phenotypes and cross-species mechanism)
- **Fission-yeast functional evidence:** In *S. pombe*, pol5+ expression is described as low-abundance/constitutive, and perturbation by overexpression correlates with impaired/delayed rRNA production, supporting involvement in rRNA production rather than DNA replication. (nadeem2005pol5+apotential pages 199-202, nadeem2005pol5+apotential pages 1-9)
- **Cross-species mechanistic anchor:** In *S. cerevisiae*, Pol5 is an **essential nucleolar ribosome biogenesis factor** for **60S** maturation; depletion/ts alleles cause 60S deficiency, half-mer polysomes, defective 27SB→25S processing, and impaired pre-60S release/export. (ramossaenz2019pol5isan pages 1-2)
- **Mechanistic inference relevant to *S. pombe*:** Additional *S. cerevisiae* data show Pol5 binds the **5′ ETS** and **domain III of 25S rRNA**, promotes recruitment of ribosomal proteins forming the peptide exit tunnel, and supports recycling of pre-40S factors—arguing Pol5 family proteins function as RNA-associated assembly factors. (braun2020pol5isrequired pages 1-2)

Taken together, the most evidence-consistent annotation for *S. pombe* Pol5 is: **essential nuclear (likely nucleolar) ribosome biogenesis/rDNA transcription-associated factor**, rather than a classical DNA polymerase. (nadeem2005pol5+apotential pages 1-9, ramossaenz2019pol5isan pages 1-2)

#### 3.3 Protein–protein interactions and pathway connections
- **Interaction with cell-cycle transcription factor Cdc10:** Two-hybrid and biochemical assays reported in the fission-yeast thesis support a physical interaction between SpPol5 and the **C-terminal region of Cdc10**, proposing a link between cell-cycle transcriptional control and growth/rRNA production. (nadeem2005pol5+apotential pages 116-121, nadeem2005pol5+apotential pages 1-9)
- **Interaction with acetyltransferase Eso1 (Eco1 ortholog):** In *S. pombe*, Pol5 is an Eso1-binding protein identified via TAP/IP-MS and confirmed by co-IP and GST pull-down mapping to Eso1’s C-terminal/Eco1-homology region. (chen2017dnapolymerase5 pages 3-6, chen2017dnapolymerase5 pages 2-3)

#### 3.4 Post-translational modification: Eso1-dependent acetylation at essential Lys47
Chen et al. (2017; publication date **Dec 2017**; International Journal of Molecular Medicine; https://doi.org/10.3892/ijmm.2017.3192) provide the most direct molecular mechanistic evidence for Pol5 regulation in *S. pombe*:
- **Pol5 is lysine-modified:** Mass spectrometry on Pol5 identified multiple lysine acetylation/trimethylation sites; **K47** had a reported **100% modification ratio** and is conserved with budding-yeast Pol5 (K53). (chen2017dnapolymerase5 pages 3-6)
- **Eso1/Eco1 can acetylate Pol5 in vitro:** Immunoprecipitated Pol5-HA incubated with recombinant Eco1 in HAT buffer plus acetyl-CoA yielded an anti–acetyl-lysine signal, consistent with direct acetylation. (chen2017dnapolymerase5 pages 2-3)
- **K47 is essential and linked to acetylation state:** A **K47R** non-acetylatable mutation is lethal (tetrad/selection-based evidence); a K47N acetyl-mimic supported normal growth, and plasmid-borne WT Pol5 rescued K47R dependence. (chen2017dnapolymerase5 pages 3-6)

### 4) Subcellular localization
- **Nuclear localization in *S. pombe*:** Early GFP-fusion localization screening lists SPBC14C8.14c under the category **Nucleus** (Table 2). (ding2000large‐scalescreeningof media e191a246, ding2000large‐scalescreeningof media b2dd5871)
- **Independent thesis GFP localization:** The *S. pombe* thesis reports GFP-tagged Pol5 localized to the **nucleus**, while nucleolar enrichment was proposed but not conclusively demonstrated in that work. (nadeem2005pol5+apotential pages 199-202, nadeem2005pol5+apotential pages 1-9)

### 5) Recent developments (2023–2024) and latest research context
Direct Pol5-focused primary research in 2023–2024 was not retrieved in the available corpus; however, several high-authority 2023–2024 studies and reviews sharpen the **systems-level context** for Pol5’s inferred role (rDNA transcription/ribosome biogenesis) in *S. pombe*.

#### 5.1 2023 review: Nutrient/stress regulation of ribosomal gene transcription in *S. pombe*
Hirai & Ohta (2023; publication date **Feb 2023**; Biomolecules; https://doi.org/10.3390/biom13020288) emphasize:
- **TOR-dependent control** of rRNA and ribosomal protein gene expression; rapamycin/TOR inhibition rapidly downregulates ribosome-related transcription, and *S. pombe* TORC1 (Tor2) is highlighted as a primary regulator of ribosome-related genes. (hirai2023comparativeresearchregulatory pages 2-4)
- **Heterochromatin/RNAi layers** that are prominent in fission yeast (Clr4-mediated H3K9 methylation and HP1 proteins) and can repress ribosomal genes/rDNA repeats during starvation; e.g., starvation-linked dissociation of activators (Atf1/Gcn5) and increased H3K9 methylation with FACT involvement. (hirai2023comparativeresearchregulatory pages 11-13, hirai2023comparativeresearchregulatory pages 9-11)
The review does not specifically place Pol5 into these pathways, but it defines the regulatory environment in which Pol5-dependent rRNA output would be controlled. (hirai2023comparativeresearchregulatory pages 2-4)

#### 5.2 2024 review: RNAPII transcription and chromatin remodeling at rDNA/tDNA loci
Yague-Sanz (2024; publication date **Dec 2024**; Yeast; https://doi.org/10.1002/yea.3921) proposes a model for *S. pombe* rDNA heterochromatinization in starvation in which:
- RNAPI dissociates from rDNA during starvation;
- pervasive local RNAPII transcription at rDNA (e.g., pausing near 5′ETS) may recruit factors (CCR4-NOT) and small-RNA pathways that promote Clr4-dependent H3K9 methylation and Clr3-dependent deacetylation. (yague‐sanz2024shapingthechromatin pages 9-9)
This suggests additional regulatory layers linking transcriptional activity at rDNA to chromatin state, relevant to any factor (including Pol5) proposed to couple transcription and processing. (yague‐sanz2024shapingthechromatin pages 9-9)

#### 5.3 2024 primary research: live-cell rDNA morphology as a readout of ribosome biogenesis regulation
Cockrell et al. (2024; publication date **Jul 2024**; PLOS Genetics; https://doi.org/10.1371/journal.pgen.1011331) provide quantitative tools and findings that are immediately relevant to Pol5’s functional neighborhood:
- **rDNA copy number context:** WT lab strains contain ~**80–120** rRNA genes across the two chromosome III rDNA arrays. (cockrell2024regulatorsofrdna pages 2-3)
- **Perturbations that change rDNA/nucleolus morphology:** RNA Pol I inhibition (actinomycin D) and glucose starvation drive rDNA condensation/nucleolar shrinkage, while TOR hyperactivation (tsc1Δ/tsc2Δ) expands rDNA volume and GapR-GFP intensity. (cockrell2024regulatorsofrdna pages 8-10)
- **Genome-scale implementation:** The authors screened the Bioneer haploid deletion collection (~**3,400** nonessential deletions) using a live imaging marker (GapR-GFP) for rDNA spatial organization phenotypes. (cockrell2024regulatorsofrdna pages 8-10)
- **Quantitative/statistical practice:** Example quantifications used n>**314** cells with Kruskal–Wallis testing across replicates; follow-up RPL mutant quantifications used >**50** cells per replicate. (cockrell2024regulatorsofrdna pages 8-10, cockrell2024regulatorsofrdna pages 12-15)
- **Signaling cross-talk:** RPL gene deletions (ribosomal protein insufficiency) produced strong nucleolar/rDNA phenotypes and correlated with resistance to TOR inhibition (Torin1 **10–12.5 μM**), with genetic analysis implicating the **Pmk1 MAPK** pathway as a modulator of compensatory ribosome biogenesis. (cockrell2024regulatorsofrdna pages 12-15, cockrell2024regulatorsofrdna pages 15-17)
Although Pol5 is not the direct subject, these methods are directly applicable to testing Pol5 conditional alleles for effects on rDNA morphology and TOR-linked adaptation. (cockrell2024regulatorsofrdna pages 8-10)

### 6) Current applications and real-world implementations
In yeast molecular/cell biology, Pol5-related knowledge is applied primarily as:

1. **Genetic essentiality/conditional alleles to probe ribosome biogenesis coupling to growth and cell cycle:** The *S. pombe* thesis uses overexpression/shut-off and interaction assays to connect Pol5 to growth-related rRNA production and cell-cycle transcription factor Cdc10. (nadeem2005pol5+apotential pages 1-9)
2. **PTM mapping and essential-residue genetics to define regulatory control points:** Chen et al. combine TAP/IP-MS, in vitro acetylation assays, and allele-specific viability tests to show a single conserved lysine (K47) is essential, likely via acetylation. (chen2017dnapolymerase5 pages 3-6, chen2017dnapolymerase5 pages 2-3)
3. **Live imaging readouts of rDNA function/nucleolar activity:** Nuclear and nucleolar phenotypes are now quantifiable at scale using GapR-GFP and other markers, enabling new ways to assay Pol5-linked rDNA activity indirectly via rDNA morphology. (cockrell2024regulatorsofrdna pages 8-10)

### 7) Expert opinions and authoritative analysis (within retrieved sources)
- **Authoritative synthesis for *S. pombe* ribosome gene transcription:** Hirai & Ohta (2023) emphasize that fission yeast differs from budding yeast by having mammal-like facultative heterochromatin machinery (Clr4/HP1), making chromatin-state control central to rDNA and ribosomal gene repression in starvation. (hirai2023comparativeresearchregulatory pages 1-2)
- **Interpretive model for rDNA chromatin remodeling:** Yague-Sanz (2024) frames local RNAPII transcription at rDNA as a potential mechanism to recruit chromatin remodelers and establish silent chromatin during starvation, offering a mechanistic hypothesis for how transcription and chromatin states are coupled at rDNA. (yague‐sanz2024shapingthechromatin pages 9-9)
- **Mechanistic consensus on Pol5 family function (cross-species):** Budding-yeast primary studies argue Pol5’s classification as a DNA polymerase is misleading and instead support its role as an rRNA-processing/ribosome-assembly factor binding pre-rRNA regions and influencing subunit maturation/export. (braun2020pol5isrequired pages 1-2, ramossaenz2019pol5isan pages 1-2)

### 8) Statistics and data highlights (recent and/or directly measured)
- rDNA arrays in *S. pombe* contain ~**80–120** rRNA genes (WT lab strains). (cockrell2024regulatorsofrdna pages 2-3)
- Genome-wide imaging screen scale: **3,400** nonessential deletion mutants screened for rDNA organization phenotypes. (cockrell2024regulatorsofrdna pages 8-10)
- Quantification practices: n>**314** cells for imaging comparisons with Kruskal–Wallis across replicates; >**50** cells/replicate for certain mutant validations. (cockrell2024regulatorsofrdna pages 8-10, cockrell2024regulatorsofrdna pages 12-15)
- TOR inhibitor concentrations used to phenotype ribosome-biogenesis compensation: Torin1 **10–12.5 μM**. (cockrell2024regulatorsofrdna pages 12-15)
- Pol5 PTM quantification: Pol5 **K47** reported with **100% modification ratio** in MS analysis in Chen et al. (2017). (chen2017dnapolymerase5 pages 3-6)

### 9) Evidence map for Pol5 functional annotation
The following table consolidates direct *S. pombe* evidence and cross-species mechanistic support.

| Evidence type | Key finding | Experimental approach/system | Species | Source (authors, year, journal) | URL/DOI |
|---|---|---|---|---|---|
| Identity / annotation | SPBC14C8.14c was recovered in a GFP-fusion localization screen and annotated there as “DNA polymerase V,” matching the historical Pol5 naming used for the fission-yeast gene; however, the screen excerpt does not unambiguously assign a localization category to this entry. (ding2000large‐scalescreeningof pages 7-10) | GFP-fusion genomic DNA library screen; clone TC48; fusion position 795/959 | *S. pombe* | Ding et al., 2000, *Genes to Cells* | https://doi.org/10.1046/j.1365-2443.2000.00317.x |
| Essentiality | *pol5+* is reported as essential for viability in fission yeast. (nadeem2005pol5+apotential pages 199-202, nadeem2005pol5+apotential pages 1-9) | Gene disruption and conditional-expression analyses summarized in thesis work | *S. pombe* | Nadeem, 2005, thesis | URL not available in retrieved context |
| Localization | GFP-tagged SpPol5p localized to the nucleus; nucleolar localization was proposed but not conclusively demonstrated in the thesis. (nadeem2005pol5+apotential pages 199-202, nadeem2005pol5+apotential pages 1-9) | GFP tagging / fluorescence localization | *S. pombe* | Nadeem, 2005, thesis | URL not available in retrieved context |
| Interaction / complex | SpPol5p physically interacts with the C-terminus of the cell-cycle transcription factor Cdc10p, suggesting a link between cell-cycle control and growth/rRNA production. (nadeem2005pol5+apotential pages 116-121, nadeem2005pol5+apotential pages 1-9) | Yeast two-hybrid, co-immunoprecipitation, GST pull-down | *S. pombe* | Nadeem, 2005, thesis | URL not available in retrieved context |
| Functional evidence | *pol5+* mRNA is constitutive and low abundance; overexpression perturbs rRNA production, supporting a role in rRNA synthesis/ribosome biogenesis rather than a conventional DNA polymerase role. (nadeem2005pol5+apotential pages 199-202, nadeem2005pol5+apotential pages 1-9) | Northern blot; overexpression and shut-off experiments; pulse-chase rRNA labeling | *S. pombe* | Nadeem, 2005, thesis | URL not available in retrieved context |
| PTM / essential residue | Pol5 is an Eso1 interaction partner and acetylation substrate; mutation of conserved Lys47 to Arg was lethal, indicating an essential role for this residue/modification state in viability. (chen2017dnapolymerase5 pages 1-2) | TAP purification, immunoprecipitation, LC-MS/MS, site-directed mutagenesis, tetrad analysis | *S. pombe* | Chen et al., 2017, *International Journal of Molecular Medicine* | https://doi.org/10.3892/ijmm.2017.3192 |
| Pathway context | Recent review of fission-yeast ribosomal gene regulation emphasizes TOR-responsive repression of ribosome-related transcription, starvation-induced chromatin remodeling, and rDNA heterochromatin/RNAi pathways; Pol5 is not specifically placed in these pathways in the review. (hirai2023comparativeresearchregulatory pages 2-4, hirai2023comparativeresearchregulatory pages 9-11, hirai2023comparativeresearchregulatory pages 1-2) | Comparative review of primary literature | *S. pombe* | Hirai & Ohta, 2023, *Biomolecules* | https://doi.org/10.3390/biom13020288 |
| Cross-species function inference | Budding-yeast Pol5 is an essential nucleolar trans-acting factor for 60S subunit maturation; depletion causes 60S deficiency, half-mer polysomes, defective 27SB→25S processing, and impaired pre-60S export. This strongly supports annotating *S. pombe* Pol5 as a ribosome-biogenesis factor. (ramossaenz2019pol5isan pages 8-9, ramossaenz2019pol5isan pages 1-2) | Depletion and temperature-sensitive mutants; polysome analysis; pre-rRNA processing assays; genetic suppression | *S. cerevisiae* | Ramos-Sáenz et al., 2019, *RNA* | https://doi.org/10.1261/rna.072116.119 |
| Cross-species mechanistic inference | Budding-yeast Pol5 binds the 5′ ETS and domain III of 25S rRNA, promotes peptide-exit-tunnel assembly in the LSU, and supports recycling of pre-40S factors; these data argue that Pol5 family proteins act in ribosome assembly, not replicative DNA synthesis. (braun2020pol5isrequired pages 1-2) | Pol5 depletion, RNA binding-site mapping, pre-rRNA processing analyses | *S. cerevisiae* | Braun et al., 2020, *Nucleic Acids Research* | https://doi.org/10.1093/nar/gkz1079 |


*Table: This table compiles the strongest directly supported evidence for functional annotation of *Schizosaccharomyces pombe* Pol5 (O60094/SPBC14C8.14c), separating organism-specific findings from cross-species inference. It is useful for distinguishing firm experimental evidence in fission yeast from broader pathway context and conserved Pol5-family function.*

### 10) Limitations and gaps in Pol5-specific knowledge (as of retrieved corpus)
- **Direct nucleolar localization and pre-ribosome binding in *S. pombe* remain incompletely defined** in the retrieved primary literature; existing *S. pombe* evidence supports nuclear localization and rRNA-production involvement, but detailed mapping to Pol I complexes or specific pre-rRNA intermediates is best established in *S. cerevisiae*. (nadeem2005pol5+apotential pages 199-202, braun2020pol5isrequired pages 1-2)
- **Pol5 domain/family claims** (e.g., MYBBP1A-family; ARM-like fold; polymerase-like motifs) are consistent with historical and comparative discussion but were not directly re-derived from a curated protein-domain database within this tool run; therefore, domain statements are presented here primarily as functional inferences from experimental literature rather than database recapitulation. (nadeem2005pol5+apotential pages 116-121)

### Key references (URLs and publication dates)
- Ding D-Q et al. “Large-scale screening of intracellular protein localization…” *Genes to Cells* (**Mar 2000**). https://doi.org/10.1046/j.1365-2443.2000.00317.x (ding2000large‐scalescreeningof media e191a246)
- Nadeem FK. “Pol5+, a potential link between cell cycle and cell growth in fission yeast” (thesis; **2005**). (nadeem2005pol5+apotential pages 1-9)
- Chen Z et al. “DNA polymerase 5 acetylation by Eso1 is essential for *S. pombe* viability.” *International Journal of Molecular Medicine* (**Dec 2017**). https://doi.org/10.3892/ijmm.2017.3192 (chen2017dnapolymerase5 pages 3-6)
- Ramos-Sáenz A et al. “Pol5 is an essential ribosome biogenesis factor…” *RNA* (**Aug 2019**). https://doi.org/10.1261/rna.072116.119 (ramossaenz2019pol5isan pages 1-2)
- Braun CM et al. “Pol5 is required for recycling of small subunit biogenesis factors…” *Nucleic Acids Research* (**Nov 2020**). https://doi.org/10.1093/nar/gkz1079 (braun2020pol5isrequired pages 1-2)
- Hirai H, Ohta K. “Regulatory mechanisms of ribosomal gene transcription…” *Biomolecules* (**Feb 2023**). https://doi.org/10.3390/biom13020288 (hirai2023comparativeresearchregulatory pages 2-4)
- Cockrell AJ et al. “Regulators of rDNA array morphology in fission yeast.” *PLOS Genetics* (**Jul 2024**). https://doi.org/10.1371/journal.pgen.1011331 (cockrell2024regulatorsofrdna pages 8-10)
- Yague-Sanz C. “Shaping the chromatin landscape at rRNA and tRNA genes…” *Yeast* (**Dec 2024**). https://doi.org/10.1002/yea.3921 (yague‐sanz2024shapingthechromatin pages 9-9)


References

1. (nadeem2005pol5+apotential pages 199-202): FK Nadeem. Pol5+, a potential link between cell cycle and cell growth in fission yeast. Unknown journal, 2005.

2. (nadeem2005pol5+apotential pages 1-9): FK Nadeem. Pol5+, a potential link between cell cycle and cell growth in fission yeast. Unknown journal, 2005.

3. (chen2017dnapolymerase5 pages 3-6): Zhiming Chen, Hongshi Cao, Yingqiang Lu, Qiang Ren, and Liankun Sun. Dna polymerase 5 acetylation by eso1 is essential for schizosaccharomyces pombe viability. International journal of molecular medicine, 40 6:1907-1913, Dec 2017. URL: https://doi.org/10.3892/ijmm.2017.3192, doi:10.3892/ijmm.2017.3192. This article has 2 citations and is from a peer-reviewed journal.

4. (nadeem2005pol5+apotential pages 116-121): FK Nadeem. Pol5+, a potential link between cell cycle and cell growth in fission yeast. Unknown journal, 2005.

5. (ramossaenz2019pol5isan pages 1-2): Ana Ramos-Sáenz, Daniel González-Álvarez, Olga Rodríguez-Galán, Alfonso Rodríguez-Gil, Sonia G. Gaspar, Eduardo Villalobo, Mercedes Dosil, and Jesús de la Cruz. Pol5 is an essential ribosome biogenesis factor required for 60s ribosomal subunit maturation in <i>saccharomyces cerevisiae</i>. RNA, 25:1561-1575, Aug 2019. URL: https://doi.org/10.1261/rna.072116.119, doi:10.1261/rna.072116.119. This article has 18 citations and is from a domain leading peer-reviewed journal.

6. (ding2000large‐scalescreeningof media e191a246): Da‐Qiao Ding, Yuki Tomita, Ayumu Yamamoto, Yuji Chikashige, Tokuko Haraguchi, and Yasushi Hiraoka. Large‐scale screening of intracellular protein localization in living fission yeast cells by the use of a gfp‐fusion genomic dna library. Genes to Cells, 5:169-190, Mar 2000. URL: https://doi.org/10.1046/j.1365-2443.2000.00317.x, doi:10.1046/j.1365-2443.2000.00317.x. This article has 171 citations and is from a peer-reviewed journal.

7. (braun2020pol5isrequired pages 1-2): Christina M. Braun, Philipp Hackert, Catharina E. Schmid, Markus T. Bohnsack, Katherine E. Bohnsack, and Jorge Perez-Fernandez. Pol5 is required for recycling of small subunit biogenesis factors and for formation of the peptide exit tunnel of the large ribosomal subunit. Nucleic Acids Research, 48:405-420, Nov 2020. URL: https://doi.org/10.1093/nar/gkz1079, doi:10.1093/nar/gkz1079. This article has 21 citations and is from a highest quality peer-reviewed journal.

8. (hirai2023comparativeresearchregulatory pages 1-2): Hayato Hirai and Kunihiro Ohta. Comparative research: regulatory mechanisms of ribosomal gene transcription in saccharomyces cerevisiae and schizosaccharomyces pombe. Biomolecules, 13:288, Feb 2023. URL: https://doi.org/10.3390/biom13020288, doi:10.3390/biom13020288. This article has 19 citations.

9. (hirai2023comparativeresearchregulatory pages 2-4): Hayato Hirai and Kunihiro Ohta. Comparative research: regulatory mechanisms of ribosomal gene transcription in saccharomyces cerevisiae and schizosaccharomyces pombe. Biomolecules, 13:288, Feb 2023. URL: https://doi.org/10.3390/biom13020288, doi:10.3390/biom13020288. This article has 19 citations.

10. (ding2000large‐scalescreeningof media b2dd5871): Da‐Qiao Ding, Yuki Tomita, Ayumu Yamamoto, Yuji Chikashige, Tokuko Haraguchi, and Yasushi Hiraoka. Large‐scale screening of intracellular protein localization in living fission yeast cells by the use of a gfp‐fusion genomic dna library. Genes to Cells, 5:169-190, Mar 2000. URL: https://doi.org/10.1046/j.1365-2443.2000.00317.x, doi:10.1046/j.1365-2443.2000.00317.x. This article has 171 citations and is from a peer-reviewed journal.

11. (chen2017dnapolymerase5 pages 1-2): Zhiming Chen, Hongshi Cao, Yingqiang Lu, Qiang Ren, and Liankun Sun. Dna polymerase 5 acetylation by eso1 is essential for schizosaccharomyces pombe viability. International journal of molecular medicine, 40 6:1907-1913, Dec 2017. URL: https://doi.org/10.3892/ijmm.2017.3192, doi:10.3892/ijmm.2017.3192. This article has 2 citations and is from a peer-reviewed journal.

12. (chen2017dnapolymerase5 pages 2-3): Zhiming Chen, Hongshi Cao, Yingqiang Lu, Qiang Ren, and Liankun Sun. Dna polymerase 5 acetylation by eso1 is essential for schizosaccharomyces pombe viability. International journal of molecular medicine, 40 6:1907-1913, Dec 2017. URL: https://doi.org/10.3892/ijmm.2017.3192, doi:10.3892/ijmm.2017.3192. This article has 2 citations and is from a peer-reviewed journal.

13. (hirai2023comparativeresearchregulatory pages 11-13): Hayato Hirai and Kunihiro Ohta. Comparative research: regulatory mechanisms of ribosomal gene transcription in saccharomyces cerevisiae and schizosaccharomyces pombe. Biomolecules, 13:288, Feb 2023. URL: https://doi.org/10.3390/biom13020288, doi:10.3390/biom13020288. This article has 19 citations.

14. (hirai2023comparativeresearchregulatory pages 9-11): Hayato Hirai and Kunihiro Ohta. Comparative research: regulatory mechanisms of ribosomal gene transcription in saccharomyces cerevisiae and schizosaccharomyces pombe. Biomolecules, 13:288, Feb 2023. URL: https://doi.org/10.3390/biom13020288, doi:10.3390/biom13020288. This article has 19 citations.

15. (yague‐sanz2024shapingthechromatin pages 9-9): Carlo Yague‐Sanz. Shaping the chromatin landscape at rrna and trna genes, an emerging new role for rna polymerase ii transcription? Yeast, 41:135-147, Dec 2024. URL: https://doi.org/10.1002/yea.3921, doi:10.1002/yea.3921. This article has 7 citations and is from a peer-reviewed journal.

16. (cockrell2024regulatorsofrdna pages 2-3): Alexandria J. Cockrell, Jeffrey J. Lange, Christopher Wood, Mark Mattingly, Scott M. McCroskey, William D. Bradford, Juliana Conkright-Fincham, Lauren Weems, Monica S. Guo, and Jennifer L. Gerton. Regulators of rdna array morphology in fission yeast. PLOS Genetics, 20:e1011331, Jul 2024. URL: https://doi.org/10.1371/journal.pgen.1011331, doi:10.1371/journal.pgen.1011331. This article has 4 citations and is from a domain leading peer-reviewed journal.

17. (cockrell2024regulatorsofrdna pages 8-10): Alexandria J. Cockrell, Jeffrey J. Lange, Christopher Wood, Mark Mattingly, Scott M. McCroskey, William D. Bradford, Juliana Conkright-Fincham, Lauren Weems, Monica S. Guo, and Jennifer L. Gerton. Regulators of rdna array morphology in fission yeast. PLOS Genetics, 20:e1011331, Jul 2024. URL: https://doi.org/10.1371/journal.pgen.1011331, doi:10.1371/journal.pgen.1011331. This article has 4 citations and is from a domain leading peer-reviewed journal.

18. (cockrell2024regulatorsofrdna pages 12-15): Alexandria J. Cockrell, Jeffrey J. Lange, Christopher Wood, Mark Mattingly, Scott M. McCroskey, William D. Bradford, Juliana Conkright-Fincham, Lauren Weems, Monica S. Guo, and Jennifer L. Gerton. Regulators of rdna array morphology in fission yeast. PLOS Genetics, 20:e1011331, Jul 2024. URL: https://doi.org/10.1371/journal.pgen.1011331, doi:10.1371/journal.pgen.1011331. This article has 4 citations and is from a domain leading peer-reviewed journal.

19. (cockrell2024regulatorsofrdna pages 15-17): Alexandria J. Cockrell, Jeffrey J. Lange, Christopher Wood, Mark Mattingly, Scott M. McCroskey, William D. Bradford, Juliana Conkright-Fincham, Lauren Weems, Monica S. Guo, and Jennifer L. Gerton. Regulators of rdna array morphology in fission yeast. PLOS Genetics, 20:e1011331, Jul 2024. URL: https://doi.org/10.1371/journal.pgen.1011331, doi:10.1371/journal.pgen.1011331. This article has 4 citations and is from a domain leading peer-reviewed journal.

20. (ding2000large‐scalescreeningof pages 7-10): Da‐Qiao Ding, Yuki Tomita, Ayumu Yamamoto, Yuji Chikashige, Tokuko Haraguchi, and Yasushi Hiraoka. Large‐scale screening of intracellular protein localization in living fission yeast cells by the use of a gfp‐fusion genomic dna library. Genes to Cells, 5:169-190, Mar 2000. URL: https://doi.org/10.1046/j.1365-2443.2000.00317.x, doi:10.1046/j.1365-2443.2000.00317.x. This article has 171 citations and is from a peer-reviewed journal.

21. (ramossaenz2019pol5isan pages 8-9): Ana Ramos-Sáenz, Daniel González-Álvarez, Olga Rodríguez-Galán, Alfonso Rodríguez-Gil, Sonia G. Gaspar, Eduardo Villalobo, Mercedes Dosil, and Jesús de la Cruz. Pol5 is an essential ribosome biogenesis factor required for 60s ribosomal subunit maturation in <i>saccharomyces cerevisiae</i>. RNA, 25:1561-1575, Aug 2019. URL: https://doi.org/10.1261/rna.072116.119, doi:10.1261/rna.072116.119. This article has 18 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](pol5-deep-research-falcon_artifacts/artifact-00.md)
![## Context ID: pqac-00000020 The entry for SPBC14C8.14c (clone TC48 / DNA polymerase V) is located in Table 2 on page 9. It falls under the localization categor](pol5-deep-research-falcon_artifacts/image-1.png)

## Citations

1. hirai2023comparativeresearchregulatory pages 1-2
2. hirai2023comparativeresearchregulatory pages 2-4
3. cockrell2024regulatorsofrdna pages 2-3
4. cockrell2024regulatorsofrdna pages 8-10
5. cockrell2024regulatorsofrdna pages 12-15
6. hirai2023comparativeresearchregulatory pages 11-13
7. hirai2023comparativeresearchregulatory pages 9-11
8. cockrell2024regulatorsofrdna pages 15-17
9. https://doi.org/10.3892/ijmm.2017.3192
10. https://doi.org/10.3390/biom13020288
11. https://doi.org/10.1002/yea.3921
12. https://doi.org/10.1371/journal.pgen.1011331
13. https://doi.org/10.1046/j.1365-2443.2000.00317.x
14. https://doi.org/10.1261/rna.072116.119
15. https://doi.org/10.1093/nar/gkz1079
16. https://doi.org/10.3892/ijmm.2017.3192,
17. https://doi.org/10.1261/rna.072116.119,
18. https://doi.org/10.1046/j.1365-2443.2000.00317.x,
19. https://doi.org/10.1093/nar/gkz1079,
20. https://doi.org/10.3390/biom13020288,
21. https://doi.org/10.1002/yea.3921,
22. https://doi.org/10.1371/journal.pgen.1011331,