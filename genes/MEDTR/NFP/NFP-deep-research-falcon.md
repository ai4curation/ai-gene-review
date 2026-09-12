---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-21T13:53:29.756716'
end_time: '2026-05-21T14:05:14.699661'
duration_seconds: 704.94
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: MEDTR
  gene_id: Q0GXS4
  gene_symbol: NFP
  uniprot_accession: Q0GXS4
  protein_description: 'RecName: Full=Serine/threonine receptor-like kinase NFP {ECO:0000303|PubMed:16723404};
    Short=RLK NFP {ECO:0000303|PubMed:16723404}; AltName: Full=Nod factor perception
    protein {ECO:0000303|PubMed:12753588}; EC=2.7.10.- {ECO:0000255|PROSITE-ProRule:PRU00159};
    AltName: Full=Nod-factor receptor 5; Flags: Precursor;'
  gene_info: Name=NFP {ECO:0000303|PubMed:12753588}; OrderedLocusNames=MTR_5g019040
    {ECO:0000312|EMBL:AES94847.1};
  organism_full: Medicago truncatula (Barrel medic) (Medicago tribuloides).
  protein_family: Belongs to the protein kinase superfamily. Tyr protein
  protein_domains: Kinase-like_dom_sf. (IPR011009); NFP_LYK_LysM1. (IPR056561); NFP_LysM2.
    (IPR059143); NFP_LysM3. (IPR059144); Plant_RLK_LysM. (IPR052611)
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
  edison_answer_artifacts: 1
  edison_message_content: 1
artifacts:
- filename: artifact-00.md
  path: NFP-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: image-1.png
  path: NFP-deep-research-falcon_artifacts/image-1.png
  media_type: image/png
  source: edison_message_content
  data_storage_id: null
  description: '## Context ID: pqac-00000008 The document contains several figures
    that address your request. - **Figure 1** provides an amino acid alignment of
    NFP with orthol'
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q0GXS4
- **Protein Description:** RecName: Full=Serine/threonine receptor-like kinase NFP {ECO:0000303|PubMed:16723404}; Short=RLK NFP {ECO:0000303|PubMed:16723404}; AltName: Full=Nod factor perception protein {ECO:0000303|PubMed:12753588}; EC=2.7.10.- {ECO:0000255|PROSITE-ProRule:PRU00159}; AltName: Full=Nod-factor receptor 5; Flags: Precursor;
- **Gene Information:** Name=NFP {ECO:0000303|PubMed:12753588}; OrderedLocusNames=MTR_5g019040 {ECO:0000312|EMBL:AES94847.1};
- **Organism (full):** Medicago truncatula (Barrel medic) (Medicago tribuloides).
- **Protein Family:** Belongs to the protein kinase superfamily. Tyr protein
- **Key Domains:** Kinase-like_dom_sf. (IPR011009); NFP_LYK_LysM1. (IPR056561); NFP_LysM2. (IPR059143); NFP_LysM3. (IPR059144); Plant_RLK_LysM. (IPR052611)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "NFP" matches the protein description above**
2. **Verify the organism is correct:** Medicago truncatula (Barrel medic) (Medicago tribuloides).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'NFP' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **NFP** (gene ID: Q0GXS4, UniProt: Q0GXS4) in MEDTR.

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
- **UniProt Accession:** Q0GXS4
- **Protein Description:** RecName: Full=Serine/threonine receptor-like kinase NFP {ECO:0000303|PubMed:16723404}; Short=RLK NFP {ECO:0000303|PubMed:16723404}; AltName: Full=Nod factor perception protein {ECO:0000303|PubMed:12753588}; EC=2.7.10.- {ECO:0000255|PROSITE-ProRule:PRU00159}; AltName: Full=Nod-factor receptor 5; Flags: Precursor;
- **Gene Information:** Name=NFP {ECO:0000303|PubMed:12753588}; OrderedLocusNames=MTR_5g019040 {ECO:0000312|EMBL:AES94847.1};
- **Organism (full):** Medicago truncatula (Barrel medic) (Medicago tribuloides).
- **Protein Family:** Belongs to the protein kinase superfamily. Tyr protein
- **Key Domains:** Kinase-like_dom_sf. (IPR011009); NFP_LYK_LysM1. (IPR056561); NFP_LysM2. (IPR059143); NFP_LysM3. (IPR059144); Plant_RLK_LysM. (IPR052611)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "NFP" matches the protein description above**
2. **Verify the organism is correct:** Medicago truncatula (Barrel medic) (Medicago tribuloides).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'NFP' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **NFP** (gene ID: Q0GXS4, UniProt: Q0GXS4) in MEDTR.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Research Report: Functional Annotation of **NFP** (UniProt **Q0GXS4**) in *Medicago truncatula*

## 0. Target verification (critical disambiguation)
The *Medicago truncatula* gene **NFP** (Nod Factor Perception) corresponds to a plasma-membrane **LysM receptor-like kinase (LysM-RLK)** with an N-terminal signal peptide, **three extracellular LysM domains**, a single transmembrane helix, and a C-terminal intracellular kinase-like region (UniProt Q0GXS4), and is closely related to pea **SYM10** and *Lotus japonicus* **NFR5**. This identity is supported by cloning/genetic linkage to *nfp* mutant alleles, complementation, and protein/domain analyses in *M. truncatula* (Jemalong A17) (arrighi2006themedicagotruncatula pages 2-3, arrighi2006themedicagotruncatula pages 3-4). Visual evidence for domain architecture and kinase motif losses is shown in Arrighi et al. figures (arrighi2006themedicagotruncatula media 0385937d, arrighi2006themedicagotruncatula media eefcd0eb).

## 1. Key concepts and definitions (current understanding)

### 1.1 Nod factors (NFs) and Nod factor perception
**Nod factors** are rhizobial **lipo-chitooligosaccharides (LCOs)** that initiate legume–rhizobia symbiosis by triggering early root responses (e.g., root hair deformation/curling, infection thread initiation) and downstream developmental programs culminating in root nodule formation. In *M. truncatula*, **NFP is essential for the earliest NF responses**, consistent with its name and mutant phenotype (arrighi2006themedicagotruncatula pages 2-3, arrighi2006themedicagotruncatula pages 8-10).

### 1.2 LysM receptor-like kinases (LysM-RLKs)
Plant **LysM-RLKs** are cell-surface receptors with extracellular LysM domains (∼40 aa modules often associated with binding N-acetylglucosamine-containing ligands such as chitin-derived molecules) linked through a transmembrane segment to an intracellular kinase domain. A key conceptual point emerging from *M. truncatula* analyses is that many plant LysM-RLKs contain a **conserved “LysM triplet”** (three LysM domains), including NFP (arrighi2006themedicagotruncatula pages 10-11).

### 1.3 “Dead”/nonclassical kinase domains and receptor complexes
A central mechanistic concept for NFP (and NFR5-like receptors) is that the intracellular region resembles a kinase domain but lacks conserved motifs and can function as a **pseudokinase (“dead kinase”)** that participates in signaling through **heteromerization** with kinase-active partners (arrighi2006themedicagotruncatula pages 2-3, arrighi2006themedicagotruncatula pages 11-12). This resembles general receptor biology where one subunit can provide ligand-binding specificity and another provides catalytic output, or where signaling is mediated via trans-phosphorylation in receptor complexes (arrighi2006themedicagotruncatula pages 11-12).

## 2. Gene/protein function: what NFP does (primary function)

### 2.1 Primary functional role
**Primary function (experimentally supported):** NFP is an essential component of the **Nod factor receptor system** required for **Nod factor perception and early symbiotic signaling** that enables rhizobial infection and nodulation in *M. truncatula* (arrighi2006themedicagotruncatula pages 2-3, arrighi2006themedicagotruncatula pages 8-10).

**Genetic evidence:** *nfp* mutants fail to undergo hallmark early NF responses (root hair deformation/curling; infection thread formation) and are defective for nodulation; complementation with a genomic NFP fragment restores nodulation, confirming gene identity and essential function (arrighi2006themedicagotruncatula pages 2-3).

### 2.2 Ligand specificity and binding determinants (mechanistic inference + supporting evidence)
Direct biochemical binding measurements for NFP–NF are not established in the retrieved evidence; however, multiple lines support NFP’s role in NF recognition:

* **Domain logic:** the extracellular region comprises three LysM domains specialized for carbohydrate-derived ligands (mulder2006lysmdomainsof pages 1-2).
* **Mutant structure–function:** Arrighi et al. report a strong *nfp-2* allele mutated in the **first LysM domain**, consistent with a crucial role for LysM1 in recognition (arrighi2006themedicagotruncatula pages 11-12).
* **Computational structural modeling/docking (mechanistic hypothesis):** docking of Nod factors to modeled NFP LysM domains predicts binding modes in which the LCO tetrasaccharide backbone and substituents (sulfate, O-acetyl group, and lipid chain) interact with specific residues and surface features, supporting a plausible structural basis for NF recognition (mulder2006lysmdomainsof pages 4-5). Mulder et al. further propose each LysM domain could potentially bind one NF, and discuss how triplicated LysMs could broaden recognition or amplify signaling (mulder2006lysmdomainsof pages 5-6).

### 2.3 Kinase activity: enzymatic reaction and substrate specificity
NFP is annotated as a receptor-like kinase (EC 2.7.10.-), but the best-supported functional interpretation is **non-catalytic signaling** rather than active enzymatic phosphorylation:

* **Motif loss:** NFP lacks key conserved kinase motifs (e.g., missing activation loop segment; absent P-loop/DFG-related motifs described in Arrighi et al.), indicating a nonclassical kinase domain (arrighi2006themedicagotruncatula pages 2-3, arrighi2006themedicagotruncatula pages 11-12, arrighi2006themedicagotruncatula media 0385937d).
* **Biochemical assay:** NFP showed **no detectable autophosphorylation activity** under in vitro conditions where other receptor kinases (e.g., LYK3, BAK1) did autophosphorylate, supporting pseudokinase-like behavior (arrighi2006themedicagotruncatula pages 3-4, arrighi2006themedicagotruncatula media d64c86c9).

Thus, NFP’s “substrate specificity” is currently best described as **not established as an active kinase**; instead, NFP likely acts as a **signaling/scaffolding subunit** in receptor complexes that are phosphorylated by kinase-active partners (arrighi2006themedicagotruncatula pages 11-12).

## 3. Cellular localization and expression context (where NFP acts)

### 3.1 Subcellular localization
NFP is described as a **plasma-membrane** receptor-like protein (consistent with signal peptide + transmembrane topology and extracellular glycosylation) (mulder2006lysmdomainsof pages 6-7).

### 3.2 Cell- and tissue-level expression patterns
Arrighi et al. map NFP promoter activity and conclude NFP expression is tightly associated with infection:

* **Root hairs:** expression in growing and recently matured root hairs (arrighi2006themedicagotruncatula pages 2-3).
* **Cortex and primordia:** expression in inner/middle cortex at sites associated with curling and nodule primordium formation (arrighi2006themedicagotruncatula pages 3-4).
* **Nodule infection zone:** expression restricted to the infection zone in mature nodules and coincident with infection thread formation and bacterial release (arrighi2006themedicagotruncatula pages 3-4, arrighi2006themedicagotruncatula pages 10-11).
* **Not nitrogen fixation:** declining expression toward nitrogen-fixing zone and lack of expression in central tissue suggests NFP is unlikely to directly mediate nitrogen fixation/assimilation, but instead functions in NF signaling/infection processes (arrighi2006themedicagotruncatula pages 10-11).

### 3.3 Post-translational modification relevant to localization/function
Mulder et al. provide biochemical evidence that NFP is **extensively N-glycosylated** extracellularly (with multiple predicted N-glycosylation sites; glycosidase tests indicating multiple modified sites), supporting extracellular domain maturation consistent with surface receptor function (mulder2006lysmdomainsof pages 6-7).

## 4. Pathway placement: how NFP connects to symbiotic signaling

### 4.1 Upstream role in NF signaling cascade
Arrighi et al. place NFP genetically **upstream** of canonical downstream symbiotic signaling components such as **DMI1/DMI2/DMI3** (and downstream transcriptional regulators), based on known mutant pathway relationships and the null phenotype of *nfp* in early NF responses (arrighi2006themedicagotruncatula pages 10-11).

They further argue that because NFP has not been shown to control processes beyond NF perception, its expression and knockdown phenotypes suggest that **NF perception/signaling continues throughout infection**, not solely at the epidermis (arrighi2006themedicagotruncatula pages 10-11).

### 4.2 Infection vs organogenesis programs
Arrighi et al. interpret expression patterns and infection phenotypes as consistent with NFP controlling (directly or indirectly) **distinct NF signaling routes**: one supporting **symbiotic infection** (infection thread development) and one supporting **nodule organogenesis** (arrighi2006themedicagotruncatula pages 10-11).

## 5. Receptor complexes and partners (current models + new evidence)

### 5.1 Classical model: NFP/NFR5-like pseudokinase + kinase-active LysM-RLK partner
Both the aberrant kinase domain of NFP and general receptor logic support a model in which NFP functions with a kinase-active LysM-RLK partner (e.g., LYK3) in a heteromeric complex to transmit NF signals (mulder2006lysmdomainsof pages 6-7, arrighi2006themedicagotruncatula pages 11-12).

### 5.2 2023–2024 developments (prioritized)

#### (i) Expanded partner set and biochemical trans-phosphorylation (2024)
A 2024 preprint reports that *M. truncatula* **MtLYK2, MtLYK3, and MtLYK2bis** can associate functionally with MtNFP:

* **Heterologous co-expression phenotype:** co-overexpression of MtNFP with MtLYK2/3/2bis in *Nicotiana* triggers apparent cell death, consistent with strong receptor complex signaling and immune crosstalk (li2024nodulationtrioin pages 1-3).
* **Kinase activity + trans-phosphorylation:** cytoplasmic domains of MtLYK2/3/2bis display kinase activity, and kinase-active versions can induce mobility shifts/retardation consistent with **trans-phosphorylation of the MtNFP cytoplasmic domain** in co-expression assays; kinase-dead controls do not (li2024nodulationtrioin pages 3-9).
* **Genetic redundancy:** these receptors show overlapping contributions to nodulation, supporting a model where NFP can partner with multiple LysM-RLKs with partially redundant/specialized roles (li2024nodulationtrioin pages 3-9, li2024nodulationtrioin pages 1-3).

Interpretation: this expands the earlier “single partner” view (NFP–LYK3) toward a **multi-partner receptor complex landscape** in *M. truncatula* (li2024nodulationtrioin pages 3-9).

#### (ii) Connection to immune co-receptor modules via SOBIR1 (2023)
A 2023 preprint reports identification of **MtSOBIR1** as an interactor of the **MtNFP kinase domain**:

* **Yeast-two-hybrid (Y2H):** the MtNFP kinase domain (aa 273–595) was used as bait, and partial clones corresponding to a SOBIR1-like RLK were recovered as interactors (sarrette2023medicagotruncatulasobir1 pages 4-5).
* **Expert framing:** SOBIR1 is described as a known positive regulator of immunity and a common coreceptor for receptor-like proteins lacking intracellular signaling domains; it has an active kinase domain and can participate in complexes including BAK1, suggesting plausible mechanistic routes by which NFP-containing complexes could interface with immune signaling modules (sarrette2023medicagotruncatulasobir1 pages 4-5).

Interpretation: NFP may not act only within “symbiosis-only” receptor assemblies but may recruit (or be regulated by) **immunity-associated RLK modules**, potentially contributing to host specificity and defense suppression/activation balance (sarrette2023medicagotruncatulasobir1 pages 4-5).

#### (iii) Symbiosis–immunity interface emphasized by recent review (2023)
A 2023 review highlights that Nod factors can induce transient defense outputs but generally weaker than chitin, and that NFRs (including MtNFP) can trigger defense-like outcomes when expressed ectopically or outside their native context (grundy2023legumesregulatesymbiosis pages 8-9). Specifically, **ectopic expression of MtNFP in nodules** is reported to increase uninfected cell density and trigger premature death of infected cells, consistent with a tight requirement for correct spatial/temporal regulation of NFP signaling to maintain mutualism rather than defense (grundy2023legumesregulatesymbiosis pages 8-9).

## 6. Quantitative findings and statistics from the retrieved studies

### 6.1 RNAi phenotype penetrance (Arrighi et al., 2006)
RNAi knockdown targeting either LysM-region or kinase-region sequences caused a strong Nod2 phenotype in **79% and 90% of transformed roots** (two constructs), affecting **21/24** total roots examined; most roots were non-nodulated, and when infection structures occurred they frequently aborted with aberrant morphology (arrighi2006themedicagotruncatula pages 3-4).

### 6.2 Scale of MtNFP-partner discovery screen (Sarrette et al., 2023)
The Y2H screen using MtNFP kinase domain bait screened **62.5 million clones**, selected **355 His+** colonies, and identified **53 genes** meeting confidence criteria; **three partial clones** of the MtSOBIR1 locus were recovered as NFP-KD interactors (sarrette2023medicagotruncatulasobir1 pages 4-5).

### 6.3 Glycosylation site statistics (Mulder et al., 2006)
Mulder et al. report **10 predicted extracellular N-glycosylation sites** on NFP and provide biochemical evidence consistent with multiple sites being modified (mulder2006lysmdomainsof pages 6-7).

## 7. Current applications and real-world implementations
While NFP itself is not a deployed agricultural product, understanding NFP is practically relevant because it sits at the decision point between symbiosis initiation and defense responses. A concrete example of real-world-oriented implementation discussed in recent literature is **engineering immune perception into legumes without abolishing nodulation**:

* A 2023 review describes introduction of the Arabidopsis pattern-recognition receptor **EFR** into *M. truncatula* to enable elf18 perception and improve resistance to *Ralstonia solanacearum*, while still allowing nodulation with *S. meliloti*; this demonstrates that immune signaling can be added/modified while maintaining symbiosis, motivating careful engineering of receptor networks that include Nod-factor receptors and their crosstalk nodes (grundy2023legumesregulatesymbiosis pages 8-9).

More broadly, mechanistic knowledge of NFP partner selection, phosphorylation-dependent tuning, and immune crosstalk (e.g., via SOBIR1-like modules) provides conceptual entry points for:

* breeding/engineering for **rhizobial specificity** and stable infection,
* minimizing defense-triggered incompatibility,
* optimizing symbiosis under pathogen pressure,

all of which align with the “symbiosis–immunity interface” emphasized in 2023–2024 work (grundy2023legumesregulatesymbiosis pages 8-9, sarrette2023medicagotruncatulasobir1 pages 4-5, li2024nodulationtrioin pages 3-9).

## 8. Visual evidence (figures)
Arrighi et al. include figures that (i) depict NFP’s domain architecture and kinase motif losses and (ii) show autophosphorylation assays supporting kinase inactivity (arrighi2006themedicagotruncatula media 0385937d, arrighi2006themedicagotruncatula media d64c86c9, arrighi2006themedicagotruncatula media eefcd0eb).

## 9. Evidence map (summary table)
| Aspect | Key findings | Evidence type (genetics/biochemistry/modeling/review) | Primary sources with year and URL/DOI |
|---|---|---|---|
| identity/domains | UniProt Q0GXS4 matches **Medicago truncatula NFP**, a LysM receptor-like kinase of ~595 aa with an N-terminal signal peptide, **three extracellular LysM domains**, a transmembrane helix, and a C-terminal kinase-like domain; it is closely related to **Lotus japonicus NFR5** and pea **SYM10**. Figures in Arrighi et al. show the domain architecture and motif losses in the kinase region. (arrighi2006themedicagotruncatula pages 2-3, arrighi2006themedicagotruncatula media 0385937d) | Genetics, sequence/domain analysis, comparative analysis | Arrighi et al., 2006, *Plant Physiology* — https://doi.org/10.1104/pp.106.084657 |
| ligand/recognition | NFP is required for specific recognition of **Sinorhizobium meliloti Nod factors** (lipo-chitooligosaccharides). Structural modeling/docking suggested that each LysM domain can bind a Nod factor, with residues near LysM1/2/3 contributing to sulfate, O-acetyl, and acyl-chain recognition; N-glycosylation is not predicted to block binding. A strong nfp-2 allele affecting the first LysM domain supports a crucial role of LysM1 in recognition. (mulder2006lysmdomainsof pages 1-2, mulder2006lysmdomainsof pages 4-5, arrighi2006themedicagotruncatula pages 11-12, mulder2006lysmdomainsof pages 5-6) | Genetics, structural modeling, glycoprotein biochemistry | Mulder et al., 2006, *Glycobiology* — https://doi.org/10.1093/glycob/cwl006; Arrighi et al., 2006, *Plant Physiology* — https://doi.org/10.1104/pp.106.084657 |
| kinase activity | NFP has a **nonclassical/aberrant kinase domain** lacking key conserved motifs (including P-loop/DFG-related features and an activation-loop segment), and **no detectable autophosphorylation** was observed in vitro, supporting interpretation of NFP as a likely **pseudokinase** or signaling subunit that requires an active kinase partner. (arrighi2006themedicagotruncatula pages 2-3, arrighi2006themedicagotruncatula pages 3-4, arrighi2006themedicagotruncatula pages 11-12, arrighi2006themedicagotruncatula media 0385937d) | Biochemistry, motif analysis, comparative analysis | Arrighi et al., 2006, *Plant Physiology* — https://doi.org/10.1104/pp.106.084657 |
| localization/expression | NFP is described as a **plasma-membrane** LysM receptor-like protein. Expression is detected in **growing/root hairs**, **inner and middle cortex** at sites of curling and primordium formation, **nodule primordia**, and the **infection zone** of mature nodules; expression declines toward the nitrogen-fixing zone, arguing against a direct role in nitrogen fixation/assimilation. NFP protein is heavily **N-glycosylated** extracellularly. (arrighi2006themedicagotruncatula pages 2-3, arrighi2006themedicagotruncatula pages 3-4, mulder2006lysmdomainsof pages 6-7, arrighi2006themedicagotruncatula pages 10-11) | Promoter-reporter expression, transcript localization, glycoprotein biochemistry | Arrighi et al., 2006, *Plant Physiology* — https://doi.org/10.1104/pp.106.084657; Mulder et al., 2006, *Glycobiology* — https://doi.org/10.1093/glycob/cwl006 |
| pathway position | NFP acts at the **earliest stages of Nod factor signaling** and is genetically placed **upstream of DMI1/DMI2/DMI3 and NSP1/NSP2**. nfp mutants fail in Nod factor-induced root hair deformation/curling and infection thread formation, and NFP has been linked to early responses including calcium fluxes, calcium spiking, and inhibition of reactive oxygen efflux. Arrighi et al. further argue that NFP functions throughout infection and may control partly distinct pathways for **symbiotic infection** and **nodule organogenesis**. (arrighi2006themedicagotruncatula pages 2-3, arrighi2006themedicagotruncatula pages 8-10, arrighi2006themedicagotruncatula pages 10-11) | Genetics, expression analysis, pathway review | Arrighi et al., 2006, *Plant Physiology* — https://doi.org/10.1104/pp.106.084657; Shumilina et al., 2023, *IJMS* — https://doi.org/10.3390/ijms242417397 |
| receptor partners | Modeling and comparative genetics suggested NFP may function in a **heteromeric receptor complex** with active LysM-RLK partners such as **LYK3**. Recent Medicago work extends this: **MtLYK2, MtLYK3, and MtLYK2bis** can functionally associate with MtNFP, and their kinase-active cytoplasmic domains can **trans-phosphorylate NFP** in heterologous assays, supporting multi-receptor complex models with overlapping specificities. A 2023 screen also identified **MtSOBIR1** as a new interactor of the NFP kinase domain, linking NFP to additional receptor-coreceptor modules. (mulder2006lysmdomainsof pages 6-7, li2024nodulationtrioin pages 3-9, li2024nodulationtrioin pages 1-3, sarrette2023medicagotruncatulasobir1 pages 4-5) | Structural inference, biochemistry, genetics, protein-protein interaction | Mulder et al., 2006, *Glycobiology* — https://doi.org/10.1093/glycob/cwl006; Li et al., 2024, *bioRxiv* — https://doi.org/10.1101/2024.02.19.577609; Sarrette et al., 2023, *bioRxiv* — https://doi.org/10.1101/2023.10.15.561875 |
| immune crosstalk | NFP/NFR-type receptors lie at a **symbiosis–immunity interface**. Reviews summarize that NFs can induce transient defense outputs, but also suppress MTI by other mechanisms. Ectopic expression of **MtNFP** in nodule tissue increased uninfected cell density and caused premature death of infected cells, and NFRs from Medicago/Lotus can trigger cell death in tobacco. Recent work connects NFP to **SOBIR1**, a known immunity coreceptor, and co-expression of MtNFP with MtLYK2/3/2bis in *Nicotiana* induced apparent cell death, consistent with immune-like crosstalk. (grundy2023legumesregulatesymbiosis pages 8-9, sarrette2023medicagotruncatulasobir1 pages 4-5, li2024nodulationtrioin pages 1-3) | Review, ectopic-expression phenotyping, protein interaction, heterologous assays | Grundy et al., 2023, *IJMS* — https://doi.org/10.3390/ijms24032800; Sarrette et al., 2023, *bioRxiv* — https://doi.org/10.1101/2023.10.15.561875; Li et al., 2024, *bioRxiv* — https://doi.org/10.1101/2024.02.19.577609 |
| quantitative data | RNAi knockdown of NFP caused a strong **Nod2 phenotype in 79% and 90% of transformed roots** for two independent constructs (**21/24 total** roots affected), with most roots non-nodulated and rare infection threads abortive/aberrant. The 2023 MtNFP kinase-domain Y2H screen tested **62.5 million clones**, yielding **355 His+ colonies** and **53 candidate genes** with satisfactory confidence scores; **three partial clones** of the MtSOBIR1 gene were recovered as NFP-KD interactors. Mulder et al. reported **10 predicted extracellular N-glycosylation sites** on NFP, with biochemical evidence that multiple sites are glycosylated. (arrighi2006themedicagotruncatula pages 3-4, sarrette2023medicagotruncatulasobir1 pages 4-5, mulder2006lysmdomainsof pages 6-7) | Genetics, screening statistics, glycoprotein biochemistry | Arrighi et al., 2006, *Plant Physiology* — https://doi.org/10.1104/pp.106.084657; Sarrette et al., 2023, *bioRxiv* — https://doi.org/10.1101/2023.10.15.561875; Mulder et al., 2006, *Glycobiology* — https://doi.org/10.1093/glycob/cwl006 |


*Table: This table summarizes the experimentally supported functional annotation of Medicago truncatula NFP (UniProt Q0GXS4), including domain structure, ligand recognition, signaling role, receptor partnerships, immune crosstalk, and quantitative findings. It is useful as a compact evidence map for building the full research report.*

## 10. Limitations and open questions
* **Direct ligand-binding biochemistry/structures:** The retrieved evidence includes docking/modeling but not definitive binding constants or co-crystal structures for NFP–Nod factor interactions; such quantitative binding remains a key gap (mulder2006lysmdomainsof pages 4-5, mulder2006lysmdomainsof pages 5-6).
* **Catalytic mechanism:** NFP appears kinase-inactive by motif and assay, but its exact signaling mechanism (e.g., scaffolding, conformational gating, regulated phosphorylation by partners) remains unresolved; recent work strengthens trans-phosphorylation models but does not fully define in planta complex composition/dynamics (arrighi2006themedicagotruncatula pages 11-12, li2024nodulationtrioin pages 3-9).
* **PubMed ID cross-checking:** UniProt references specific PubMed IDs (12753588; 16723404). The tool-driven retrieval here captured the closely aligned 2006 primary literature that provides direct experimental evidence for NFP identity and function; however, the original PubMed-ID-matched papers were not individually retrieved through the current search results, so statements are anchored to the retrieved articles rather than those PubMed IDs.

## References (retrieved sources; publication dates and URLs)
* Arrighi J-F. et al. **July 2006**. *Plant Physiology*. “The Medicago truncatula Lysine Motif-Receptor-Like Kinase Gene Family Includes NFP and New Nodule-Expressed Genes.” https://doi.org/10.1104/pp.106.084657 (arrighi2006themedicagotruncatula pages 2-3, arrighi2006themedicagotruncatula pages 3-4)
* Mulder L. et al. **Sep 2006**. *Glycobiology*. “LysM domains of Medicago truncatula NFP protein involved in Nod factor perception…” https://doi.org/10.1093/glycob/cwl006 (mulder2006lysmdomainsof pages 4-5, mulder2006lysmdomainsof pages 6-7)
* Grundy E.B. et al. **Feb 2023**. *International Journal of Molecular Sciences*. “Legumes Regulate Symbiosis with Rhizobia via Their Innate Immune System.” https://doi.org/10.3390/ijms24032800 (grundy2023legumesregulatesymbiosis pages 8-9)
* Shumilina J. et al. **Dec 2023**. *International Journal of Molecular Sciences*. “Signaling in Legume–Rhizobia Symbiosis.” https://doi.org/10.3390/ijms242417397 (arrighi2006themedicagotruncatula pages 10-11)
* Sarrette B. et al. **Oct 2023 (posted Oct 17, 2023)**. *bioRxiv preprint*. “Medicago truncatula SOBIR1 controls specificity in the Rhizobium-legume symbiosis.” https://doi.org/10.1101/2023.10.15.561875 (sarrette2023medicagotruncatulasobir1 pages 4-5)
* Li Y. et al. **Feb 2024**. *bioRxiv preprint*. “Nodulation Trio in Medicago truncatula: Unveiling the Overlapping Roles of MtLYK2, MtLYK3, and MtLYK2bis.” https://doi.org/10.1101/2024.02.19.577609 (li2024nodulationtrioin pages 3-9, li2024nodulationtrioin pages 1-3)


References

1. (arrighi2006themedicagotruncatula pages 2-3): J. Arrighi, A. Barre, Besma Ben Amor, Anne Bersoult, Lidia Campos Soriano, R. Mirabella, Fernanda de Carvalho-Niebel, E. Journet, M. Ghérardi, T. Huguet, R. Geurts, J. Dénarié, P. Rougé, and C. Gough. The medicago truncatula lysine motif-receptor-like kinase gene family includes nfp and new nodule-expressed genes1[w]. Plant Physiology, 142:265-279, Jul 2006. URL: https://doi.org/10.1104/pp.106.084657, doi:10.1104/pp.106.084657. This article has 658 citations and is from a highest quality peer-reviewed journal.

2. (arrighi2006themedicagotruncatula pages 3-4): J. Arrighi, A. Barre, Besma Ben Amor, Anne Bersoult, Lidia Campos Soriano, R. Mirabella, Fernanda de Carvalho-Niebel, E. Journet, M. Ghérardi, T. Huguet, R. Geurts, J. Dénarié, P. Rougé, and C. Gough. The medicago truncatula lysine motif-receptor-like kinase gene family includes nfp and new nodule-expressed genes1[w]. Plant Physiology, 142:265-279, Jul 2006. URL: https://doi.org/10.1104/pp.106.084657, doi:10.1104/pp.106.084657. This article has 658 citations and is from a highest quality peer-reviewed journal.

3. (arrighi2006themedicagotruncatula media 0385937d): J. Arrighi, A. Barre, Besma Ben Amor, Anne Bersoult, Lidia Campos Soriano, R. Mirabella, Fernanda de Carvalho-Niebel, E. Journet, M. Ghérardi, T. Huguet, R. Geurts, J. Dénarié, P. Rougé, and C. Gough. The medicago truncatula lysine motif-receptor-like kinase gene family includes nfp and new nodule-expressed genes1[w]. Plant Physiology, 142:265-279, Jul 2006. URL: https://doi.org/10.1104/pp.106.084657, doi:10.1104/pp.106.084657. This article has 658 citations and is from a highest quality peer-reviewed journal.

4. (arrighi2006themedicagotruncatula media eefcd0eb): J. Arrighi, A. Barre, Besma Ben Amor, Anne Bersoult, Lidia Campos Soriano, R. Mirabella, Fernanda de Carvalho-Niebel, E. Journet, M. Ghérardi, T. Huguet, R. Geurts, J. Dénarié, P. Rougé, and C. Gough. The medicago truncatula lysine motif-receptor-like kinase gene family includes nfp and new nodule-expressed genes1[w]. Plant Physiology, 142:265-279, Jul 2006. URL: https://doi.org/10.1104/pp.106.084657, doi:10.1104/pp.106.084657. This article has 658 citations and is from a highest quality peer-reviewed journal.

5. (arrighi2006themedicagotruncatula pages 8-10): J. Arrighi, A. Barre, Besma Ben Amor, Anne Bersoult, Lidia Campos Soriano, R. Mirabella, Fernanda de Carvalho-Niebel, E. Journet, M. Ghérardi, T. Huguet, R. Geurts, J. Dénarié, P. Rougé, and C. Gough. The medicago truncatula lysine motif-receptor-like kinase gene family includes nfp and new nodule-expressed genes1[w]. Plant Physiology, 142:265-279, Jul 2006. URL: https://doi.org/10.1104/pp.106.084657, doi:10.1104/pp.106.084657. This article has 658 citations and is from a highest quality peer-reviewed journal.

6. (arrighi2006themedicagotruncatula pages 10-11): J. Arrighi, A. Barre, Besma Ben Amor, Anne Bersoult, Lidia Campos Soriano, R. Mirabella, Fernanda de Carvalho-Niebel, E. Journet, M. Ghérardi, T. Huguet, R. Geurts, J. Dénarié, P. Rougé, and C. Gough. The medicago truncatula lysine motif-receptor-like kinase gene family includes nfp and new nodule-expressed genes1[w]. Plant Physiology, 142:265-279, Jul 2006. URL: https://doi.org/10.1104/pp.106.084657, doi:10.1104/pp.106.084657. This article has 658 citations and is from a highest quality peer-reviewed journal.

7. (arrighi2006themedicagotruncatula pages 11-12): J. Arrighi, A. Barre, Besma Ben Amor, Anne Bersoult, Lidia Campos Soriano, R. Mirabella, Fernanda de Carvalho-Niebel, E. Journet, M. Ghérardi, T. Huguet, R. Geurts, J. Dénarié, P. Rougé, and C. Gough. The medicago truncatula lysine motif-receptor-like kinase gene family includes nfp and new nodule-expressed genes1[w]. Plant Physiology, 142:265-279, Jul 2006. URL: https://doi.org/10.1104/pp.106.084657, doi:10.1104/pp.106.084657. This article has 658 citations and is from a highest quality peer-reviewed journal.

8. (mulder2006lysmdomainsof pages 1-2): Lonneke Mulder, Benoit Lefebvre, Julie Cullimore, and Anne Imberty. Lysm domains of medicago truncatula nfp protein involved in nod factor perception. glycosylation state, molecular modeling and docking of chitooligosaccharides and nod factors. Glycobiology, 16 9:801-9, Sep 2006. URL: https://doi.org/10.1093/glycob/cwl006, doi:10.1093/glycob/cwl006. This article has 130 citations and is from a peer-reviewed journal.

9. (mulder2006lysmdomainsof pages 4-5): Lonneke Mulder, Benoit Lefebvre, Julie Cullimore, and Anne Imberty. Lysm domains of medicago truncatula nfp protein involved in nod factor perception. glycosylation state, molecular modeling and docking of chitooligosaccharides and nod factors. Glycobiology, 16 9:801-9, Sep 2006. URL: https://doi.org/10.1093/glycob/cwl006, doi:10.1093/glycob/cwl006. This article has 130 citations and is from a peer-reviewed journal.

10. (mulder2006lysmdomainsof pages 5-6): Lonneke Mulder, Benoit Lefebvre, Julie Cullimore, and Anne Imberty. Lysm domains of medicago truncatula nfp protein involved in nod factor perception. glycosylation state, molecular modeling and docking of chitooligosaccharides and nod factors. Glycobiology, 16 9:801-9, Sep 2006. URL: https://doi.org/10.1093/glycob/cwl006, doi:10.1093/glycob/cwl006. This article has 130 citations and is from a peer-reviewed journal.

11. (arrighi2006themedicagotruncatula media d64c86c9): J. Arrighi, A. Barre, Besma Ben Amor, Anne Bersoult, Lidia Campos Soriano, R. Mirabella, Fernanda de Carvalho-Niebel, E. Journet, M. Ghérardi, T. Huguet, R. Geurts, J. Dénarié, P. Rougé, and C. Gough. The medicago truncatula lysine motif-receptor-like kinase gene family includes nfp and new nodule-expressed genes1[w]. Plant Physiology, 142:265-279, Jul 2006. URL: https://doi.org/10.1104/pp.106.084657, doi:10.1104/pp.106.084657. This article has 658 citations and is from a highest quality peer-reviewed journal.

12. (mulder2006lysmdomainsof pages 6-7): Lonneke Mulder, Benoit Lefebvre, Julie Cullimore, and Anne Imberty. Lysm domains of medicago truncatula nfp protein involved in nod factor perception. glycosylation state, molecular modeling and docking of chitooligosaccharides and nod factors. Glycobiology, 16 9:801-9, Sep 2006. URL: https://doi.org/10.1093/glycob/cwl006, doi:10.1093/glycob/cwl006. This article has 130 citations and is from a peer-reviewed journal.

13. (li2024nodulationtrioin pages 1-3): Yaohua Li, Yanwen Zhao, Ziang Yan, Ru Dong, Haixiang Yu, Hui Zhu, and Yangrong Cao. Nodulation trio in medicago truncatula: unveiling the overlapping roles of mtlyk2, mtlyk3, and mtlyk2bis. bioRxiv, Feb 2024. URL: https://doi.org/10.1101/2024.02.19.577609, doi:10.1101/2024.02.19.577609. This article has 0 citations.

14. (li2024nodulationtrioin pages 3-9): Yaohua Li, Yanwen Zhao, Ziang Yan, Ru Dong, Haixiang Yu, Hui Zhu, and Yangrong Cao. Nodulation trio in medicago truncatula: unveiling the overlapping roles of mtlyk2, mtlyk3, and mtlyk2bis. bioRxiv, Feb 2024. URL: https://doi.org/10.1101/2024.02.19.577609, doi:10.1101/2024.02.19.577609. This article has 0 citations.

15. (sarrette2023medicagotruncatulasobir1 pages 4-5): Baptiste Sarrette, Thi-Bich Luu, Alexander Johansson, Judith Fliegmann, Cécile Pouzet, Aurélie Le Ru, Carole Pichereaux, Céline Remblière, Laurent Sauviac, Noémie Carles, Emilie Amblard, Valentin Guyot, Maxime Bonhomme, Julie Cullimore, Clare Gough, Christophe Jacquet, and Nicolas Pauly. Medicago truncatula sobir1 controls specificity in the rhizobium-legume symbiosis. bioRxiv, Oct 2023. URL: https://doi.org/10.1101/2023.10.15.561875, doi:10.1101/2023.10.15.561875. This article has 0 citations.

16. (grundy2023legumesregulatesymbiosis pages 8-9): Estelle B. Grundy, Peter M. Gresshoff, Huanan Su, and Brett J. Ferguson. Legumes regulate symbiosis with rhizobia via their innate immune system. International Journal of Molecular Sciences, 24:2800, Feb 2023. URL: https://doi.org/10.3390/ijms24032800, doi:10.3390/ijms24032800. This article has 41 citations.

## Artifacts

- [Edison artifact artifact-00](NFP-deep-research-falcon_artifacts/artifact-00.md)
![## Context ID: pqac-00000008 The document contains several figures that address your request. - **Figure 1** provides an amino acid alignment of NFP with orthol](NFP-deep-research-falcon_artifacts/image-1.png)

## Citations

1. arrighi2006themedicagotruncatula pages 10-11
2. arrighi2006themedicagotruncatula pages 11-12
3. arrighi2006themedicagotruncatula pages 2-3
4. mulder2006lysmdomainsof pages 1-2
5. mulder2006lysmdomainsof pages 4-5
6. mulder2006lysmdomainsof pages 5-6
7. mulder2006lysmdomainsof pages 6-7
8. arrighi2006themedicagotruncatula pages 3-4
9. li2024nodulationtrioin pages 1-3
10. li2024nodulationtrioin pages 3-9
11. grundy2023legumesregulatesymbiosis pages 8-9
12. arrighi2006themedicagotruncatula pages 8-10
13. w
14. https://doi.org/10.1104/pp.106.084657
15. https://doi.org/10.1093/glycob/cwl006;
16. https://doi.org/10.1104/pp.106.084657;
17. https://doi.org/10.1093/glycob/cwl006
18. https://doi.org/10.3390/ijms242417397
19. https://doi.org/10.1101/2024.02.19.577609;
20. https://doi.org/10.1101/2023.10.15.561875
21. https://doi.org/10.3390/ijms24032800;
22. https://doi.org/10.1101/2023.10.15.561875;
23. https://doi.org/10.1101/2024.02.19.577609
24. https://doi.org/10.3390/ijms24032800
25. https://doi.org/10.1104/pp.106.084657,
26. https://doi.org/10.1093/glycob/cwl006,
27. https://doi.org/10.1101/2024.02.19.577609,
28. https://doi.org/10.1101/2023.10.15.561875,
29. https://doi.org/10.3390/ijms24032800,