---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-30T05:14:41.081816'
end_time: '2026-09-30T05:29:36.984035'
duration_seconds: 895.9
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: worm
  gene_id: glp-1
  gene_symbol: glp-1
  uniprot_accession: P13508
  protein_description: 'RecName: Full=Protein glp-1; Contains: RecName: Full=glp-1/Notch
    intracellular domain {ECO:0000305|PubMed:9003776}; Flags: Precursor;'
  gene_info: Name=glp-1 {ECO:0000312|WormBase:F02A9.6}; Synonyms=emb-33 {ECO:0000312|WormBase:F02A9.6};
    ORFNames=F02A9.6 {ECO:0000312|WormBase:F02A9.6};
  organism_full: Caenorhabditis elegans.
  protein_family: Not specified in UniProt
  protein_domains: Ankyrin_rpt. (IPR002110); Ankyrin_rpt-contain_sf. (IPR036770);
    EGF. (IPR000742); EGF-like_Ca-bd_dom. (IPR001881); EGF-type_Asp/Asn_hydroxyl_site.
    (IPR000152)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 30
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: glp-1-deep-research-falcon_artifacts/artifact-00.md
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
- **UniProt Accession:** P13508
- **Protein Description:** RecName: Full=Protein glp-1; Contains: RecName: Full=glp-1/Notch intracellular domain {ECO:0000305|PubMed:9003776}; Flags: Precursor;
- **Gene Information:** Name=glp-1 {ECO:0000312|WormBase:F02A9.6}; Synonyms=emb-33 {ECO:0000312|WormBase:F02A9.6}; ORFNames=F02A9.6 {ECO:0000312|WormBase:F02A9.6};
- **Organism (full):** Caenorhabditis elegans.
- **Protein Family:** Not specified in UniProt
- **Key Domains:** Ankyrin_rpt. (IPR002110); Ankyrin_rpt-contain_sf. (IPR036770); EGF. (IPR000742); EGF-like_Ca-bd_dom. (IPR001881); EGF-type_Asp/Asn_hydroxyl_site. (IPR000152)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "glp-1" matches the protein description above**
2. **Verify the organism is correct:** Caenorhabditis elegans.
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'glp-1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **glp-1** (gene ID: glp-1, UniProt: P13508) in worm.

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
- **UniProt Accession:** P13508
- **Protein Description:** RecName: Full=Protein glp-1; Contains: RecName: Full=glp-1/Notch intracellular domain {ECO:0000305|PubMed:9003776}; Flags: Precursor;
- **Gene Information:** Name=glp-1 {ECO:0000312|WormBase:F02A9.6}; Synonyms=emb-33 {ECO:0000312|WormBase:F02A9.6}; ORFNames=F02A9.6 {ECO:0000312|WormBase:F02A9.6};
- **Organism (full):** Caenorhabditis elegans.
- **Protein Family:** Not specified in UniProt
- **Key Domains:** Ankyrin_rpt. (IPR002110); Ankyrin_rpt-contain_sf. (IPR036770); EGF. (IPR000742); EGF-like_Ca-bd_dom. (IPR001881); EGF-type_Asp/Asn_hydroxyl_site. (IPR000152)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "glp-1" matches the protein description above**
2. **Verify the organism is correct:** Caenorhabditis elegans.
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'glp-1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **glp-1** (gene ID: glp-1, UniProt: P13508) in worm.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Comprehensive Research Report: glp-1 Gene in *Caenorhabditis elegans*

## Gene Identity Verification

The gene glp-1 (UniProt: P13508; synonyms: emb-33; ORF: F02A9.6) from *Caenorhabditis elegans* encodes the protein GLP-1, a Notch-family receptor (rudel2001conservationofglp1 pages 2-3, rudel2001conservationofglp1 pages 1-2). **It is critical to note that this gene is unrelated to the mammalian glucagon-like peptide-1 (GLP-1) or its receptor.** The *C. elegans* GLP-1 is a transmembrane signaling receptor belonging to the evolutionarily conserved Notch family, which mediates cell-cell communication and developmental cell-fate decisions (rudel2001conservationofglp1 pages 2-3).

| Feature Category | Details | Key Citations |
|---|---|---|
| Identity | *C. elegans* **glp-1** (synonym **emb-33**; ORF **F02A9.6**) encodes GLP-1, a Notch-family receptor. It is unrelated to mammalian glucagon-like peptide-1 and GLP-1R. | (rudel2001conservationofglp1 pages 2-3, rudel2001conservationofglp1 pages 1-2) |
| Molecular architecture | GLP-1 is a precursor, single-pass transmembrane receptor. Its extracellular region contains **10 EGF-like repeats** and **three LNR repeats**; its intracellular region includes a **RAM motif**, **six ankyrin repeats**, and a C-terminal **PEST sequence**. This architecture agrees with the supplied UniProt/InterPro EGF, calcium-binding EGF, and ankyrin-repeat annotations. | (rudel2001conservationofglp1 pages 1-2, rudel2001conservationofglp1 pages 7-8, rudel2001conservationofglp1 pages 6-7) |
| Primary molecular function | GLP-1 is a ligand-activated cell–cell signaling receptor, not an enzyme or transporter. It converts contact-dependent extracellular signals into a nuclear transcriptional response controlling developmental cell fate. Thus, substrate specificity is not applicable; ligand specificity is the relevant property. | (rudel2001conservationofglp1 pages 2-3) |
| Receptor activation | Ligand engagement exposes an extracellular protease site, leading to receptor cleavage followed by intramembrane cleavage by **γ-secretase**. The released GLP-1 intracellular domain, GLP-1(ICD/NICD), enters the nucleus. GLP-1’s negative regulatory region has a lower mechanical-force threshold for activation than *Drosophila* Notch. | (post2025notchactivityis pages 2-3, langridge2021thec.elegans pages 5-8) |
| Ligands | The cognate DSL-family ligands are **LAG-2** and **APX-1**. In the adult germline niche, they are presented by the somatic distal tip cell to GLP-1 on neighboring germ cells; APX-1 also has prominent embryonic signaling roles. | (rudel2001conservationofglp1 pages 2-3, post2025notchactivityis pages 2-3, chen2020glp1notch—lag1csl pages 2-4) |
| Subcellular localization | In its receiving state, GLP-1 is a **plasma-membrane receptor**, especially at interfaces between germ cells and the distal tip cell niche. After activation, GLP-1(ICD) accumulates in germ-cell **nuclei** and participates in transcriptional activation. | (rudel2001conservationofglp1 pages 2-3, rudel2001conservationofglp1 pages 9-10, post2025notchactivityis pages 2-3) |
| Tissue and developmental localization | GLP-1 protein is enriched in the **distal mitotic/progenitor region of the gonad**. In early embryos, it appears from the two-cell stage in the anterior **AB blastomere** and later in AB descendants. Protein distribution is more restricted than *glp-1* mRNA, indicating post-transcriptional regulation. | (rudel2001conservationofglp1 pages 2-3, rudel2001conservationofglp1 pages 9-10, rudel2001conservationofglp1 pages 8-9) |
| Nuclear signaling complex | Nuclear GLP-1(ICD) associates with the CSL-family DNA-binding protein **LAG-1** and the Mastermind-like coactivator **SEL-8/LAG-3**. The RAM and ankyrin-repeat regions support assembly and activity of this transcriptional complex. | (rudel2001conservationofglp1 pages 12-13, chen2020glp1notch—lag1csl pages 2-4) |
| Direct transcriptional targets | Integrated LAG-1 ChIP-seq, GLP-1-dependent RNA-seq, and acute LAG-1-degradation experiments identified **lst-1** and **sygl-1** as the principal—and potentially only—direct protein-coding targets mediating germline stem-cell fate. Their transcripts decline within approximately **0.5–1 hour** after LAG-1 degradation. | (chen2020glp1notch—lag1csl pages 1-2, chen2020glp1notch—lag1csl pages 17-19, chen2020glp1notch—lag1csl pages 16-17) |
| Downstream post-transcriptional network | LST-1 and SYGL-1 cooperate with PUF-family RNA-binding proteins **FBF-1/FBF-2** to repress differentiation-promoting mRNAs. This network opposes the **GLD-1**, **GLD-2**, and **SCF^PROM-1** meiotic-entry pathways. | (chen2020glp1notch—lag1csl pages 2-4, chen2020glp1notch—lag1csl pages 12-14) |
| Primary germline function | GLP-1 transduces the distal tip cell’s niche signal to maintain germline stem/progenitor identity, sustain the mitotic population, and prevent premature meiotic entry. Evidence indicates that it primarily controls developmental fate rather than directly driving the core mitotic machinery. | (fox2010mitoticcellcycle pages 158-162, jones2024c.elegansgermline pages 3-4, chen2020glp1notch—lag1csl pages 2-4) |
| Loss-of-function evidence | Loss or conditional inactivation of *glp-1* causes proliferative germ cells to enter meiosis prematurely, depleting the stem/progenitor population. Combined *lst-1 sygl-1* loss phenocopies *glp-1* loss, supporting these genes as its major germline output. | (fox2010mitoticcellcycle pages 149-154, chen2020glp1notch—lag1csl pages 17-19) |
| Gain-of-function evidence | Constitutive or elevated GLP-1 activity prevents normal meiotic differentiation and causes ectopic proliferation or germline tumors. Overexpression of **LST-1** or **SYGL-1** can similarly produce tumor-like overproliferation. | (jones2024c.elegansgermline pages 3-4, jones2024c.elegansgermline pages 4-6) |
| Embryonic function | Maternally supplied GLP-1 mediates inductive cell–cell interactions that specify early blastomere fates. Its conserved roles include early embryonic fate specification and anterior pharyngeal development, distinct from its later germline function. | (rudel2001conservationofglp1 pages 2-3, rudel2001conservationofglp1 pages 8-9) |
| 2023 development—negative feedback | A 2023 study established that **LST-1 is bifunctional**: its N-terminal PUF-interacting motifs support post-transcriptional repression and self-renewal, while its C-terminal zinc finger weakens Notch-dependent transcription. LST-1 therefore provides negative feedback that helps balance self-renewal and differentiation. | (ferdous2023lst1isa pages 2-2) |
| 2024 synthesis—tumor model and regulation | A 2024 review consolidated GLP-1 gain-of-function germlines as a tumor model and summarized regulation by cell-cycle factors, DNA replication, proteostasis, metabolism, endocytosis, transcription, and RNA control. Insufficient and excessive signaling produce opposite stem-cell phenotypes. | (jones2024c.elegansgermline pages 4-6, jones2024c.elegansgermline pages 3-4) |
| 2024 preprint—extracellular matrix | A May 2024 preprint, subsequently peer reviewed in 2025, reported that niche-adjacent **EMB-9/type IV collagen** promotes GLP-1 activation. The DTC-secreted papilin homolog **MIG-6L** limits local collagen accumulation and thereby restricts signaling. | (narbonne2024nicheadjacenttypeiv pages 1-5, narbonne2024nicheadjacenttypeiv pages 13-15) |
| 2025 confirmation—type IV collagen | Selective depletion of DTC-derived **EMB-9/type IV collagen** reduced GLP-1 activity and progenitor-zone size. Conversely, altered germline state or reduced GLP-1 activity was associated with broad collagen accumulation, revealing a reciprocal relationship between Notch signaling and extracellular matrix. | (martel2025nicheassociatedtypeiv pages 6-7, martel2025nicheassociatedtypeiv pages 1-2, martel2025nicheassociatedtypeiv pages 5-6) |
| 2025 development—LAT-1/latrophilin | The adhesion GPCR **LAT-1** positively modulates signaling by binding LAG-2 **in cis** on the distal tip cell through extracellular RBL and GAIN domains. Its membrane-tethered N terminus is sufficient, making the effect independent of conventional G-protein signaling. Loss of *lat-1* reduces nuclear GLP-1(ICD), mitotic activity, germ-cell number, and progenitor-zone size. | (post2025notchactivityis pages 1-2, post2025notchactivityis pages 7-8, post2025notchactivityis pages 3-5, post2025notchactivityis pages 8-9) |
| Functional-annotation summary | **Notch-family single-pass transmembrane receptor that receives DTC-derived LAG-2/APX-1 signals and, through proteolytic release of its intracellular domain and LAG-1–SEL-8/LAG-3-dependent transcription of *lst-1* and *sygl-1*, maintains distal germline stem/progenitor fate and suppresses meiotic differentiation; it also specifies embryonic cell fates.** | (chen2020glp1notch—lag1csl pages 2-4, jones2024c.elegansgermline pages 3-4) |


*Table: This table summarizes the verified molecular architecture, localization, ligands, signaling mechanism, biological roles, genetic evidence, and recent regulatory findings for *C. elegans* GLP-1. It distinguishes the worm Notch receptor from mammalian glucagon-like peptide-1 terminology.*

## Molecular Structure and Primary Function

### Protein Architecture

GLP-1 is a single-pass transmembrane receptor with a modular domain structure consistent with the UniProt annotation (rudel2001conservationofglp1 pages 1-2). The extracellular region contains 10 EGF-like repeats and three LNR (Lin-12/Notch repeat) repeats, which mediate ligand binding and regulate receptor activation (rudel2001conservationofglp1 pages 1-2, rudel2001conservationofglp1 pages 9-10). The protein also possesses a conserved CC-linker region containing two conserved cysteine residues implicated in receptor dimerization and processing (rudel2001conservationofglp1 pages 9-10).

The intracellular signaling domain contains a RAM (RBP-Jκ-associated molecule) motif, six ankyrin (ANK) repeats, and a C-terminal PEST sequence (rudel2001conservationofglp1 pages 1-2, rudel2001conservationofglp1 pages 12-13). The RAM domain binds the DNA-binding transcription factor LAG-1, while the ankyrin repeats mediate protein-protein interactions essential for assembling the transcriptional activation complex (rudel2001conservationofglp1 pages 12-13, rudel2001conservationofglp1 pages 7-8).

### Primary Molecular Function: Signal Transduction Rather Than Enzymatic Activity

As a signaling receptor, GLP-1 does not possess enzymatic activity or function as a transporter. Instead, its primary molecular function is to transduce extracellular ligand-binding events into intracellular transcriptional responses (rudel2001conservationofglp1 pages 2-3). The relevant parameter is therefore **ligand specificity** rather than substrate specificity. GLP-1 specifically recognizes and responds to DSL (Delta/Serrate/LAG-2)-family ligands presented by adjacent cells (rudel2001conservationofglp1 pages 2-3, post2025notchactivityis pages 2-3).

## Ligand Interactions and Receptor Activation

### Cognate Ligands

The primary ligands for GLP-1 are LAG-2 and APX-1, both members of the DSL family of Notch ligands (rudel2001conservationofglp1 pages 2-3, post2025notchactivityis pages 2-3, langridge2021thec.elegans pages 5-8). In the adult germline, the distal tip cell (DTC) niche expresses LAG-2, which activates GLP-1 on neighboring germline stem cells (post2025notchactivityis pages 2-3, jones2024c.elegansgermline pages 3-4, chen2020glp1notch—lag1csl pages 2-4). APX-1 functions redundantly with LAG-2 in some contexts and plays prominent roles in embryonic signaling (rudel2001conservationofglp1 pages 2-3, langridge2021thec.elegans pages 5-8).

### Mechanism of Receptor Activation

GLP-1 activation follows the canonical Notch signaling mechanism (post2025notchactivityis pages 2-3, langridge2021thec.elegans pages 5-8). Ligand binding to the extracellular domain induces a conformational change that exposes an ADAM protease cleavage site in the negative regulatory region (NRR). Importantly, *C. elegans* GLP-1 and LIN-12 are tuned to lower mechanical-force thresholds for activation compared to *Drosophila* Notch, lacking the leucine "plug" that occludes the cleavage site in other organisms (langridge2021thec.elegans pages 5-8). This structural difference allows GLP-1 to be activated without the strong Epsin-mediated endocytic pulling force required in flies and vertebrates (langridge2021thec.elegans pages 5-8).

Following ADAM cleavage, γ-secretase performs intramembrane proteolysis, releasing the GLP-1 intracellular domain (GLP-1(ICD), also called NICD for Notch intracellular domain) (post2025notchactivityis pages 2-3, chen2020glp1notch—lag1csl pages 2-4). This liberated fragment translocates to the nucleus where it performs its signaling function (post2025notchactivityis pages 2-3, post2025notchactivityis pages 8-9).

## Subcellular Localization

### Plasma Membrane Localization

As a transmembrane receptor, GLP-1 localizes to the plasma membrane where it receives signals from adjacent ligand-expressing cells (rudel2001conservationofglp1 pages 2-3, rudel2001conservationofglp1 pages 9-10). In the germline, GLP-1 protein is concentrated in the distal mitotic/progenitor region, particularly at cell-cell contact sites with the distal tip cell niche (rudel2001conservationofglp1 pages 2-3).

### Nuclear Translocation of Cleaved Fragment

Upon activation, the cleaved GLP-1 intracellular domain accumulates in germ cell nuclei, where it forms a transcriptional activation complex (post2025notchactivityis pages 2-3, post2025notchactivityis pages 8-9). This dual localization—membrane-bound receptor and nuclear signaling fragment—is characteristic of Notch-family proteins.

### Tissue-Specific Expression

GLP-1 protein localization is more restricted than glp-1 mRNA distribution, indicating post-transcriptional regulation (rudel2001conservationofglp1 pages 2-3, rudel2001conservationofglp1 pages 8-9). In the adult germline, protein accumulates specifically in the distal proliferative zone (rudel2001conservationofglp1 pages 2-3). In early embryos, GLP-1 appears from the two-cell stage and is asymmetrically localized to the anterior AB blastomere and its descendants (rudel2001conservationofglp1 pages 9-10). The mRNA-binding protein GLD-1 represses glp-1 translation, contributing to restricted protein accumulation (kimble2007controlsofgermline pages 11-12, jones2024c.elegansgermline pages 6-8).

## Nuclear Signaling Pathway and Transcriptional Targets

### Nuclear Transcriptional Complex

In the nucleus, GLP-1(ICD) assembles with the CSL-family DNA-binding protein LAG-1 and the Mastermind-like coactivator SEL-8/LAG-3 to form a ternary transcriptional activation complex (rudel2001conservationofglp1 pages 12-13, chen2020glp1notch—lag1csl pages 2-4, chen2020glp1notch—lag1csl pages 17-19). LAG-1 recognizes the consensus CSL-binding sequence (GTGGGAA) in target gene promoters, directing the complex to specific genomic loci (chen2020glp1notch—lag1csl pages 2-4).

### Direct Transcriptional Targets: lst-1 and sygl-1

A comprehensive 2020 genome-wide study combining LAG-1 ChIP-seq, GLP-1-dependent RNA-seq, and time-course analysis following auxin-induced LAG-1 degradation identified **lst-1** and **sygl-1** as the principal—and likely only—direct protein-coding transcriptional targets of GLP-1/Notch signaling in the germline (chen2020glp1notch—lag1csl pages 1-2, chen2020glp1notch—lag1csl pages 17-19, chen2020glp1notch—lag1csl pages 11-12, chen2020glp1notch—lag1csl pages 16-17). These two genes are both necessary and sufficient to mediate GLP-1's role in maintaining germline stem cell fate: the lst-1 sygl-1 double mutant phenocopies glp-1 loss-of-function, while overexpression of either gene produces germline tumors resembling glp-1 gain-of-function (chen2020glp1notch—lag1csl pages 17-19, chen2020glp1notch—lag1csl pages 2-4).

LST-1 and SYGL-1 transcripts decline within 0.5-1 hour after LAG-1 degradation, confirming their status as primary response genes (chen2020glp1notch—lag1csl pages 16-17). Their expression is restricted to distal germ cells in contact with the DTC niche and requires continuous GLP-1 activity throughout larval development and adulthood (chen2020glp1notch—lag1csl pages 17-19, chen2020glp1notch—lag1csl pages 6-7).

### Downstream Post-Transcriptional Regulatory Network

LST-1 and SYGL-1 function as post-transcriptional regulators that maintain germline stem cell fate (ferdous2023lst1isa pages 2-2, chen2020glp1notch—lag1csl pages 2-4). They cooperate with PUF-family RNA-binding proteins FBF-1 and FBF-2 to repress or promote degradation of mRNAs encoding components of meiotic entry pathways (chen2020glp1notch—lag1csl pages 2-4, chen2020glp1notch—lag1csl pages 12-14). This network opposes three redundant pathways that promote meiotic differentiation: the GLD-1/NOS-3 pathway, the GLD-2/GLD-3 pathway, and the SCF^PROM-1 ubiquitin ligase pathway (chen2020glp1notch—lag1csl pages 2-4).

A 2023 study revealed that LST-1 is bifunctional: its N-terminal PUF-interacting motifs support RNA repression and self-renewal, while its C-terminal zinc finger domain feeds back negatively on GLP-1/Notch-dependent transcription, weakening signaling strength and limiting lst-1 and sygl-1 expression (ferdous2023lst1isa pages 2-2). This negative feedback loop helps balance stem cell self-renewal and differentiation.

## Biological Function and Pathway Context

### Germline Stem Cell Maintenance and the Mitosis-to-Meiosis Decision

The primary biological function of GLP-1 in adult *C. elegans* is to maintain germline stem cells (GSCs) and proliferative progenitor cells in the distal gonad (fox2010mitoticcellcycle pages 129-136, fox2010mitoticcellcycle pages 14-18, jones2024c.elegansgermline pages 3-4). The distal tip cell (DTC) functions as the somatic stem cell niche, expressing LAG-2 and APX-1 ligands that activate GLP-1 on adjacent germ cells (dalfo2020agenomewidernai pages 1-5, byrd2009scratchingtheniche pages 1-2, fox2010mitoticcellcycle pages 14-18, chen2020glp1notch—lag1csl pages 2-4). This signaling maintains cells in a mitotic, proliferative state and prevents premature entry into meiotic differentiation (fox2010mitoticcellcycle pages 129-136, fox2010mitoticcellcycle pages 14-18, kimble2007controlsofgermline pages 11-12).

As germ cells move proximally away from the DTC, they experience declining GLP-1 signaling. This reduction permits the meiotic entry pathways to become active, initiating the transition from mitotic proliferation to meiotic prophase (fox2010mitoticcellcycle pages 149-154, fox2010mitoticcellcycle pages 158-162, fox2010mitoticcellcycle pages 162-166). Temperature-sensitive glp-1 mutants demonstrate that GLP-1 activity is continuously required: inactivation at any life stage causes proliferative germ cells to enter meiosis within hours (fox2010mitoticcellcycle pages 149-154, kimble2007controlsofgermline pages 11-12).

GLP-1 primarily controls developmental fate decisions rather than directly regulating core cell cycle machinery (fox2010mitoticcellcycle pages 158-162, fox2010mitoticcellcycle pages 162-166). Cells generally complete their current mitotic division before entering meiosis when GLP-1 is inactivated, and meiotic entry can occur even when cells are arrested in the mitotic cell cycle (fox2010mitoticcellcycle pages 162-166).

### Loss-of-Function and Gain-of-Function Genetic Evidence

Loss-of-function glp-1 mutants fail to maintain germline stem cells, with germ cells entering meiosis prematurely and producing severely reduced or absent germlines (fox2010mitoticcellcycle pages 14-18, kimble2007controlsofgermline pages 11-12, jones2024c.elegansgermline pages 3-4). Conversely, gain-of-function or constitutively active glp-1 alleles prevent the normal mitosis-to-meiosis transition, causing germline tumors characterized by ectopic proliferation and accumulated undifferentiated cells (jones2024c.elegansgermline pages 3-4, jones2024c.elegansgermline pages 4-6). These tumor phenotypes demonstrate that precise regulation of GLP-1 activity is essential for balancing stem cell maintenance and differentiation.

### Embryonic Cell Fate Specification

In addition to its germline function, maternally supplied GLP-1 mediates essential cell-cell interactions during early embryogenesis (rudel2001conservationofglp1 pages 2-3, rudel2001conservationofglp1 pages 8-9). GLP-1 specifies blastomere fates, particularly in the AB lineage, and is required for proper anterior pharynx formation (rudel2001conservationofglp1 pages 2-3, rudel2001conservationofglp1 pages 8-9). Both LAG-2 and APX-1 activate GLP-1 during embryonic development (rudel2001conservationofglp1 pages 2-3).

## Recent Developments (2023-2025)

### 2023: LST-1 Negative Feedback Mechanism

A 2023 study published in *Proceedings of the National Academy of Sciences* by Ferdous et al. revealed that LST-1 provides negative feedback on Notch-dependent transcription (ferdous2023lst1isa pages 2-2). The C-terminal zinc finger domain of LST-1 weakens GLP-1/Notch signaling strength and lowers lst-1 and sygl-1 expression, while the N-terminal PUF-interacting motifs support RNA repression. This bifunctional regulation introduces a major feedback feature in the regulatory network controlling the balance between self-renewal and differentiation (ferdous2023lst1isa pages 2-2).

### 2024: Tumor Model and Multi-Level Regulation

A comprehensive 2024 review by Jones et al. in *Biology* consolidated GLP-1/Notch gain-of-function as one of three distinct germline tumor models in *C. elegans* (jones2024c.elegansgermline pages 4-6, jones2024c.elegansgermline pages 3-4). The review summarized multiple regulatory mechanisms controlling GLP-1 function, including:

- Cell-cycle regulation by CYE-1/CDK-2, DNA polymerase, and primase components (jones2024c.elegansgermline pages 4-6)
- Proteostasis control through HSP90, CUP-2, and DER-2 (ER-associated degradation factors) (jones2024c.elegansgermline pages 4-6)
- Metabolic regulation involving uridine/thymidine levels affecting glp-1 mRNA translation through the 3' UTR (jones2024c.elegansgermline pages 4-6)
- Somatic signaling by syndecan SDN-1 promoting glp-1 transcription via calcium-dependent APTF-2 transcription factor (jones2024c.elegansgermline pages 6-8)
- Negative regulation by RNA-binding proteins including NHL-2, PUF-8, and PRP-19 (jones2024c.elegansgermline pages 4-6)

### 2024-2025: Extracellular Matrix Regulation of GLP-1 Activation

A landmark finding reported in a May 2024 preprint (subsequently published in *Nature Communications* in October 2025) by Martel, Narbonne, and colleagues demonstrated that niche-associated type IV collagen promotes GLP-1/Notch receptor activation (narbonne2024nicheadjacenttypeiv pages 1-5, martel2025nicheassociatedtypeiv pages 6-7, martel2025nicheassociatedtypeiv pages 1-2). EMB-9/type IV collagen accumulates in the basement membrane adjacent to the DTC niche, and elevated local collagen levels—possibly through increased basement membrane stiffness—enhance GLP-1 activity in neighboring germline stem cells (martel2025nicheassociatedtypeiv pages 6-7, martel2025nicheassociatedtypeiv pages 1-2).

Selective reduction of DTC-derived EMB-9 using RNAi decreased GLP-1 activity and reduced progenitor zone size (martel2025nicheassociatedtypeiv pages 6-7, martel2025nicheassociatedtypeiv pages 5-6). The DTC-secreted papilin homolog MIG-6L limits collagen accumulation at the DTC-germline interface through its PLAC domain, thereby restricting GLP-1 signaling (narbonne2024nicheadjacenttypeiv pages 1-5).

Surprisingly, the relationship is bidirectional: reducing or eliminating GLP-1 activity causes a dramatic, generalized increase in type IV collagen throughout the animal (martel2025nicheassociatedtypeiv pages 1-2, martel2025nicheassociatedtypeiv pages 5-6). This suggests that elevated Notch activity can be a consequence of increased matrix stiffness, while reduced Notch signaling promotes fibrosis-like collagen accumulation (narbonne2024nicheadjacenttypeiv pages 1-5, martel2025nicheassociatedtypeiv pages 1-2). These findings have potential implications for understanding the co-occurrence of tissue fibrosis and elevated Notch signaling in aging and inflammation-associated diseases.

### 2025: Latrophilin LAT-1 as a Positive Modulator

A July 2025 *Nature Communications* study by Post et al. identified the adhesion G protein-coupled receptor latrophilin-1 (LAT-1) as a positive modulator of GLP-1/Notch signaling (post2025notchactivityis pages 1-2, post2025notchactivityis pages 7-8, post2025notchactivityis pages 2-3, post2025notchactivityis pages 3-5, post2025notchactivityis pages 8-9). LAT-1 directly binds the DSL ligand LAG-2 in cis (on the same DTC cell) through its extracellular RBL and GAIN domains (post2025notchactivityis pages 7-8, post2025notchactivityis pages 3-5). This interaction enhances GLP-1 activation in adjacent germ cells, increasing nuclear translocation of the Notch intracellular domain (post2025notchactivityis pages 1-2, post2025notchactivityis pages 8-9).

The effect is independent of conventional G protein signaling: a membrane-tethered LAT-1 N-terminal fragment is sufficient to restore normal Notch activity (post2025notchactivityis pages 2-3, post2025notchactivityis pages 8-9). Loss of lat-1 reduces the progenitor zone size, decreases mitotic activity, and causes more distal expression of the differentiation-promoting factor GLD-1 (post2025notchactivityis pages 2-3, post2025notchactivityis pages 3-5). LAT-1 must be expressed on the DTC rather than in germ cells to support GLP-1-dependent germ cell proliferation (post2025notchactivityis pages 7-8). These findings reveal a novel mechanism by which an adhesion GPCR fine-tunes canonical Notch signaling to balance stem cell self-renewal and differentiation.

## Summary

The *C. elegans* glp-1 gene encodes GLP-1, a Notch-family transmembrane receptor that serves as the central transducer of stem cell niche signals in the germline and mediates cell fate specification in early embryos. As a signaling receptor rather than an enzyme or transporter, GLP-1's molecular function centers on ligand recognition (LAG-2 and APX-1) and signal transduction through proteolytic activation, nuclear translocation of the intracellular domain, and assembly of a transcriptional complex with LAG-1 and SEL-8/LAG-3.

GLP-1 localizes to the plasma membrane of distal germline cells and early embryonic blastomeres, with the activated intracellular fragment translocating to the nucleus. In the germline, GLP-1 directly activates transcription of lst-1 and sygl-1, which form a post-transcriptional regulatory network with FBF proteins to repress meiotic entry pathways and maintain stem cell fate. The pathway operates within a complex regulatory environment involving the DTC niche, extracellular matrix composition, and modulatory receptors.

Recent discoveries (2023-2025) have revealed sophisticated regulatory mechanisms including LST-1-mediated negative feedback, extracellular matrix/type IV collagen-dependent modulation of receptor activation, and enhancement of ligand-receptor interactions by the adhesion GPCR latrophilin LAT-1. These findings expand our understanding of how stem cell niche signaling is regulated at multiple levels—from extracellular matrix mechanics to ligand presentation to transcriptional feedback—and establish *C. elegans* GLP-1 as a powerful model for studying Notch signaling regulation in stem cell biology.

## Key Citations and Dates

**Classical foundational studies:**
- Rudel & Kimble (2001, Genetics) - Conservation of glp-1 structure and function (rudel2001conservationofglp1 pages 2-3, rudel2001conservationofglp1 pages 1-2)
- Kimble & Crittenden (2007, Annual Review) - Comprehensive review of germline stem cell control (kimble2007controlsofgermline pages 11-12)

**Recent transcriptional target identification:**
- Chen et al. (2020, PLOS Genetics) - Identification of lst-1 and sygl-1 as primary targets (chen2020glp1notch—lag1csl pages 1-2, chen2020glp1notch—lag1csl pages 2-4)

**2023-2025 mechanistic advances:**
- Ferdous et al. (2023, PNAS) - LST-1 bifunctional regulation and feedback (ferdous2023lst1isa pages 2-2)
- Jones et al. (2024, Biology) - Tumor models and multi-level regulation (jones2024c.elegansgermline pages 4-6, jones2024c.elegansgermline pages 3-4)
- Martel/Narbonne et al. (2024 preprint/2025 Nature Communications) - Type IV collagen regulation (narbonne2024nicheadjacenttypeiv pages 1-5, martel2025nicheassociatedtypeiv pages 6-7, martel2025nicheassociatedtypeiv pages 1-2)
- Post et al. (2025, Nature Communications) - LAT-1 modulation of signaling (post2025notchactivityis pages 1-2, post2025notchactivityis pages 7-8, post2025notchactivityis pages 8-9)

References

1. (rudel2001conservationofglp1 pages 2-3): David Rudel and Judith Kimble. Conservation of <i>glp-1</i> regulation and function in nematodes. Genetics, 157(2):639-654, Feb 2001. URL: https://doi.org/10.1093/genetics/157.2.639, doi:10.1093/genetics/157.2.639. This article has 67 citations and is from a domain leading peer-reviewed journal.

2. (rudel2001conservationofglp1 pages 1-2): David Rudel and Judith Kimble. Conservation of <i>glp-1</i> regulation and function in nematodes. Genetics, 157(2):639-654, Feb 2001. URL: https://doi.org/10.1093/genetics/157.2.639, doi:10.1093/genetics/157.2.639. This article has 67 citations and is from a domain leading peer-reviewed journal.

3. (rudel2001conservationofglp1 pages 7-8): David Rudel and Judith Kimble. Conservation of <i>glp-1</i> regulation and function in nematodes. Genetics, 157(2):639-654, Feb 2001. URL: https://doi.org/10.1093/genetics/157.2.639, doi:10.1093/genetics/157.2.639. This article has 67 citations and is from a domain leading peer-reviewed journal.

4. (rudel2001conservationofglp1 pages 6-7): David Rudel and Judith Kimble. Conservation of <i>glp-1</i> regulation and function in nematodes. Genetics, 157(2):639-654, Feb 2001. URL: https://doi.org/10.1093/genetics/157.2.639, doi:10.1093/genetics/157.2.639. This article has 67 citations and is from a domain leading peer-reviewed journal.

5. (post2025notchactivityis pages 2-3): Willem Berend Post, Victoria Elisabeth Groß, Daniel Matúš, Iannis Charnay, Fabian Liessmann, Florian Seufert, Peter Hildebrand, Jens Meiler, Anette Kaiser, Torsten Schöneberg, and Simone Prömel. Notch activity is modulated by the agpcr latrophilin binding the dsl ligand in c. elegans. Nature Communications, Jul 2025. URL: https://doi.org/10.1038/s41467-025-61730-0, doi:10.1038/s41467-025-61730-0. This article has 4 citations and is from a highest quality peer-reviewed journal.

6. (langridge2021thec.elegans pages 5-8): Paul D. Langridge, Jessica Yu Chan, Alejandro Garcia-Diaz, Iva Greenwald, and Gary Struhl. The c. elegans notch proteins lin-12 and glp-1 are tuned to lower force thresholds for activation than drosophila notch. bioRxiv, Feb 2021. URL: https://doi.org/10.1101/2021.02.11.429991, doi:10.1101/2021.02.11.429991. This article has 1 citations.

7. (chen2020glp1notch—lag1csl pages 2-4): Jian Chen, Ariz Mohammad, Nanette Pazdernik, Huiyan Huang, Beth Bowman, Eric Tycksen, and Tim Schedl. Glp-1 notch—lag-1 csl control of the germline stem cell fate is mediated by transcriptional targets lst-1 and sygl-1. PLOS Genetics, 16:e1008650, Mar 2020. URL: https://doi.org/10.1371/journal.pgen.1008650, doi:10.1371/journal.pgen.1008650. This article has 61 citations and is from a domain leading peer-reviewed journal.

8. (rudel2001conservationofglp1 pages 9-10): David Rudel and Judith Kimble. Conservation of <i>glp-1</i> regulation and function in nematodes. Genetics, 157(2):639-654, Feb 2001. URL: https://doi.org/10.1093/genetics/157.2.639, doi:10.1093/genetics/157.2.639. This article has 67 citations and is from a domain leading peer-reviewed journal.

9. (rudel2001conservationofglp1 pages 8-9): David Rudel and Judith Kimble. Conservation of <i>glp-1</i> regulation and function in nematodes. Genetics, 157(2):639-654, Feb 2001. URL: https://doi.org/10.1093/genetics/157.2.639, doi:10.1093/genetics/157.2.639. This article has 67 citations and is from a domain leading peer-reviewed journal.

10. (rudel2001conservationofglp1 pages 12-13): David Rudel and Judith Kimble. Conservation of <i>glp-1</i> regulation and function in nematodes. Genetics, 157(2):639-654, Feb 2001. URL: https://doi.org/10.1093/genetics/157.2.639, doi:10.1093/genetics/157.2.639. This article has 67 citations and is from a domain leading peer-reviewed journal.

11. (chen2020glp1notch—lag1csl pages 1-2): Jian Chen, Ariz Mohammad, Nanette Pazdernik, Huiyan Huang, Beth Bowman, Eric Tycksen, and Tim Schedl. Glp-1 notch—lag-1 csl control of the germline stem cell fate is mediated by transcriptional targets lst-1 and sygl-1. PLOS Genetics, 16:e1008650, Mar 2020. URL: https://doi.org/10.1371/journal.pgen.1008650, doi:10.1371/journal.pgen.1008650. This article has 61 citations and is from a domain leading peer-reviewed journal.

12. (chen2020glp1notch—lag1csl pages 17-19): Jian Chen, Ariz Mohammad, Nanette Pazdernik, Huiyan Huang, Beth Bowman, Eric Tycksen, and Tim Schedl. Glp-1 notch—lag-1 csl control of the germline stem cell fate is mediated by transcriptional targets lst-1 and sygl-1. PLOS Genetics, 16:e1008650, Mar 2020. URL: https://doi.org/10.1371/journal.pgen.1008650, doi:10.1371/journal.pgen.1008650. This article has 61 citations and is from a domain leading peer-reviewed journal.

13. (chen2020glp1notch—lag1csl pages 16-17): Jian Chen, Ariz Mohammad, Nanette Pazdernik, Huiyan Huang, Beth Bowman, Eric Tycksen, and Tim Schedl. Glp-1 notch—lag-1 csl control of the germline stem cell fate is mediated by transcriptional targets lst-1 and sygl-1. PLOS Genetics, 16:e1008650, Mar 2020. URL: https://doi.org/10.1371/journal.pgen.1008650, doi:10.1371/journal.pgen.1008650. This article has 61 citations and is from a domain leading peer-reviewed journal.

14. (chen2020glp1notch—lag1csl pages 12-14): Jian Chen, Ariz Mohammad, Nanette Pazdernik, Huiyan Huang, Beth Bowman, Eric Tycksen, and Tim Schedl. Glp-1 notch—lag-1 csl control of the germline stem cell fate is mediated by transcriptional targets lst-1 and sygl-1. PLOS Genetics, 16:e1008650, Mar 2020. URL: https://doi.org/10.1371/journal.pgen.1008650, doi:10.1371/journal.pgen.1008650. This article has 61 citations and is from a domain leading peer-reviewed journal.

15. (fox2010mitoticcellcycle pages 158-162): Paul M. Fox. Mitotic cell cycle progression and differentiation of germline stem cells in caenorhabditis elegans. ArXiv, Jan 2010. URL: https://doi.org/10.7936/k7p26w4z, doi:10.7936/k7p26w4z. This article has 0 citations.

16. (jones2024c.elegansgermline pages 3-4): Mariah E. Jones, Mina Norman, Alex Minh Tiet, Jiwoo Lee, and Myon Hee Lee. C. elegans germline as three distinct tumor models. Biology, Jun 2024. URL: https://doi.org/10.3390/biology13060425, doi:10.3390/biology13060425. This article has 3 citations.

17. (fox2010mitoticcellcycle pages 149-154): Paul M. Fox. Mitotic cell cycle progression and differentiation of germline stem cells in caenorhabditis elegans. ArXiv, Jan 2010. URL: https://doi.org/10.7936/k7p26w4z, doi:10.7936/k7p26w4z. This article has 0 citations.

18. (jones2024c.elegansgermline pages 4-6): Mariah E. Jones, Mina Norman, Alex Minh Tiet, Jiwoo Lee, and Myon Hee Lee. C. elegans germline as three distinct tumor models. Biology, Jun 2024. URL: https://doi.org/10.3390/biology13060425, doi:10.3390/biology13060425. This article has 3 citations.

19. (ferdous2023lst1isa pages 2-2): Ahlan S. Ferdous, Tina R. Lynch, Stephany J. Costa Dos Santos, Deep H. Kapadia, Sarah L. Crittenden, and Judith Kimble. Lst-1 is a bifunctional regulator that feeds back on notch-dependent transcription to regulate c. elegans germline stem cells. Proceedings of the National Academy of Sciences of the United States of America, Sep 2023. URL: https://doi.org/10.1073/pnas.2309964120, doi:10.1073/pnas.2309964120. This article has 12 citations and is from a highest quality peer-reviewed journal.

20. (narbonne2024nicheadjacenttypeiv pages 1-5): Patrick Narbonne, Pier-Olivier Martel, Julia Degrémont, Sarah Turmel-Couture, Eden Dologuele, Lucie Beaulieu, and Alexandre Clouet. Niche-adjacent type iv collagen promotes glp-1/notch receptor activation in the c. elegans germline. May 2024. URL: https://doi.org/10.21203/rs.3.rs-4228526/v1, doi:10.21203/rs.3.rs-4228526/v1.

21. (narbonne2024nicheadjacenttypeiv pages 13-15): Patrick Narbonne, Pier-Olivier Martel, Julia Degrémont, Sarah Turmel-Couture, Eden Dologuele, Lucie Beaulieu, and Alexandre Clouet. Niche-adjacent type iv collagen promotes glp-1/notch receptor activation in the c. elegans germline. May 2024. URL: https://doi.org/10.21203/rs.3.rs-4228526/v1, doi:10.21203/rs.3.rs-4228526/v1.

22. (martel2025nicheassociatedtypeiv pages 6-7): Pier-Olivier Martel, Rustelle Janse van Vuuren, Julia Degrémont, Sarah Turmel-Couture, Armi M. Chaudhari, Eden Dologuele, Lucie Beaulieu, Alexandre Clouet, and Patrick Narbonne. Niche-associated type iv collagen promotes glp-1/notch receptor activation in the c. elegans germline. Nature Communications, Oct 2025. URL: https://doi.org/10.1038/s41467-025-64394-y, doi:10.1038/s41467-025-64394-y. This article has 2 citations and is from a highest quality peer-reviewed journal.

23. (martel2025nicheassociatedtypeiv pages 1-2): Pier-Olivier Martel, Rustelle Janse van Vuuren, Julia Degrémont, Sarah Turmel-Couture, Armi M. Chaudhari, Eden Dologuele, Lucie Beaulieu, Alexandre Clouet, and Patrick Narbonne. Niche-associated type iv collagen promotes glp-1/notch receptor activation in the c. elegans germline. Nature Communications, Oct 2025. URL: https://doi.org/10.1038/s41467-025-64394-y, doi:10.1038/s41467-025-64394-y. This article has 2 citations and is from a highest quality peer-reviewed journal.

24. (martel2025nicheassociatedtypeiv pages 5-6): Pier-Olivier Martel, Rustelle Janse van Vuuren, Julia Degrémont, Sarah Turmel-Couture, Armi M. Chaudhari, Eden Dologuele, Lucie Beaulieu, Alexandre Clouet, and Patrick Narbonne. Niche-associated type iv collagen promotes glp-1/notch receptor activation in the c. elegans germline. Nature Communications, Oct 2025. URL: https://doi.org/10.1038/s41467-025-64394-y, doi:10.1038/s41467-025-64394-y. This article has 2 citations and is from a highest quality peer-reviewed journal.

25. (post2025notchactivityis pages 1-2): Willem Berend Post, Victoria Elisabeth Groß, Daniel Matúš, Iannis Charnay, Fabian Liessmann, Florian Seufert, Peter Hildebrand, Jens Meiler, Anette Kaiser, Torsten Schöneberg, and Simone Prömel. Notch activity is modulated by the agpcr latrophilin binding the dsl ligand in c. elegans. Nature Communications, Jul 2025. URL: https://doi.org/10.1038/s41467-025-61730-0, doi:10.1038/s41467-025-61730-0. This article has 4 citations and is from a highest quality peer-reviewed journal.

26. (post2025notchactivityis pages 7-8): Willem Berend Post, Victoria Elisabeth Groß, Daniel Matúš, Iannis Charnay, Fabian Liessmann, Florian Seufert, Peter Hildebrand, Jens Meiler, Anette Kaiser, Torsten Schöneberg, and Simone Prömel. Notch activity is modulated by the agpcr latrophilin binding the dsl ligand in c. elegans. Nature Communications, Jul 2025. URL: https://doi.org/10.1038/s41467-025-61730-0, doi:10.1038/s41467-025-61730-0. This article has 4 citations and is from a highest quality peer-reviewed journal.

27. (post2025notchactivityis pages 3-5): Willem Berend Post, Victoria Elisabeth Groß, Daniel Matúš, Iannis Charnay, Fabian Liessmann, Florian Seufert, Peter Hildebrand, Jens Meiler, Anette Kaiser, Torsten Schöneberg, and Simone Prömel. Notch activity is modulated by the agpcr latrophilin binding the dsl ligand in c. elegans. Nature Communications, Jul 2025. URL: https://doi.org/10.1038/s41467-025-61730-0, doi:10.1038/s41467-025-61730-0. This article has 4 citations and is from a highest quality peer-reviewed journal.

28. (post2025notchactivityis pages 8-9): Willem Berend Post, Victoria Elisabeth Groß, Daniel Matúš, Iannis Charnay, Fabian Liessmann, Florian Seufert, Peter Hildebrand, Jens Meiler, Anette Kaiser, Torsten Schöneberg, and Simone Prömel. Notch activity is modulated by the agpcr latrophilin binding the dsl ligand in c. elegans. Nature Communications, Jul 2025. URL: https://doi.org/10.1038/s41467-025-61730-0, doi:10.1038/s41467-025-61730-0. This article has 4 citations and is from a highest quality peer-reviewed journal.

29. (kimble2007controlsofgermline pages 11-12): Judith Kimble and Sarah L. Crittenden. Controls of germline stem cells, entry into meiosis, and the sperm/oocyte decision in<i>caenorhabditis elegans</i>. Nov 2007. URL: https://doi.org/10.1146/annurev.cellbio.23.090506.123326, doi:10.1146/annurev.cellbio.23.090506.123326. This article has 476 citations and is from a domain leading peer-reviewed journal.

30. (jones2024c.elegansgermline pages 6-8): Mariah E. Jones, Mina Norman, Alex Minh Tiet, Jiwoo Lee, and Myon Hee Lee. C. elegans germline as three distinct tumor models. Biology, Jun 2024. URL: https://doi.org/10.3390/biology13060425, doi:10.3390/biology13060425. This article has 3 citations.

31. (chen2020glp1notch—lag1csl pages 11-12): Jian Chen, Ariz Mohammad, Nanette Pazdernik, Huiyan Huang, Beth Bowman, Eric Tycksen, and Tim Schedl. Glp-1 notch—lag-1 csl control of the germline stem cell fate is mediated by transcriptional targets lst-1 and sygl-1. PLOS Genetics, 16:e1008650, Mar 2020. URL: https://doi.org/10.1371/journal.pgen.1008650, doi:10.1371/journal.pgen.1008650. This article has 61 citations and is from a domain leading peer-reviewed journal.

32. (chen2020glp1notch—lag1csl pages 6-7): Jian Chen, Ariz Mohammad, Nanette Pazdernik, Huiyan Huang, Beth Bowman, Eric Tycksen, and Tim Schedl. Glp-1 notch—lag-1 csl control of the germline stem cell fate is mediated by transcriptional targets lst-1 and sygl-1. PLOS Genetics, 16:e1008650, Mar 2020. URL: https://doi.org/10.1371/journal.pgen.1008650, doi:10.1371/journal.pgen.1008650. This article has 61 citations and is from a domain leading peer-reviewed journal.

33. (fox2010mitoticcellcycle pages 129-136): Paul M. Fox. Mitotic cell cycle progression and differentiation of germline stem cells in caenorhabditis elegans. ArXiv, Jan 2010. URL: https://doi.org/10.7936/k7p26w4z, doi:10.7936/k7p26w4z. This article has 0 citations.

34. (fox2010mitoticcellcycle pages 14-18): Paul M. Fox. Mitotic cell cycle progression and differentiation of germline stem cells in caenorhabditis elegans. ArXiv, Jan 2010. URL: https://doi.org/10.7936/k7p26w4z, doi:10.7936/k7p26w4z. This article has 0 citations.

35. (dalfo2020agenomewidernai pages 1-5): Diana Dalfó, Yanhui Ding, Qifei Liang, Alex Fong, Patricia Giselle Cipriani, Fabio Piano, Jialin C Zheng, Zhao Qin, and E Jane Albert Hubbard. A genome-wide rnai screen for enhancers of a germline tumor phenotype caused by elevated glp-1/notch signaling in<i>caenorhabditis elegans</i>. Dec 2020. URL: https://doi.org/10.1534/g3.120.401632, doi:10.1534/g3.120.401632. This article has 3 citations.

36. (byrd2009scratchingtheniche pages 1-2): Dana T. Byrd and Judith Kimble. Scratching the niche that controls caenorhabditis elegans germline stem cells. Seminars in cell & developmental biology, 20 9:1107-13, Dec 2009. URL: https://doi.org/10.1016/j.semcdb.2009.09.005, doi:10.1016/j.semcdb.2009.09.005. This article has 106 citations and is from a peer-reviewed journal.

37. (fox2010mitoticcellcycle pages 162-166): Paul M. Fox. Mitotic cell cycle progression and differentiation of germline stem cells in caenorhabditis elegans. ArXiv, Jan 2010. URL: https://doi.org/10.7936/k7p26w4z, doi:10.7936/k7p26w4z. This article has 0 citations.

## Artifacts

- [Edison artifact artifact-00](glp-1-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. fox2010mitoticcellcycle pages 162-166
2. narbonne2024nicheadjacenttypeiv pages 1-5
3. post2025notchactivityis pages 7-8
4. kimble2007controlsofgermline pages 11-12
5. post2025notchactivityis pages 2-3
6. fox2010mitoticcellcycle pages 158-162
7. fox2010mitoticcellcycle pages 149-154
8. narbonne2024nicheadjacenttypeiv pages 13-15
9. martel2025nicheassociatedtypeiv pages 6-7
10. martel2025nicheassociatedtypeiv pages 1-2
11. martel2025nicheassociatedtypeiv pages 5-6
12. post2025notchactivityis pages 1-2
13. post2025notchactivityis pages 3-5
14. post2025notchactivityis pages 8-9
15. fox2010mitoticcellcycle pages 129-136
16. fox2010mitoticcellcycle pages 14-18
17. dalfo2020agenomewidernai pages 1-5
18. byrd2009scratchingtheniche pages 1-2
19. https://doi.org/10.1093/genetics/157.2.639,
20. https://doi.org/10.1038/s41467-025-61730-0,
21. https://doi.org/10.1101/2021.02.11.429991,
22. https://doi.org/10.1371/journal.pgen.1008650,
23. https://doi.org/10.7936/k7p26w4z,
24. https://doi.org/10.3390/biology13060425,
25. https://doi.org/10.1073/pnas.2309964120,
26. https://doi.org/10.21203/rs.3.rs-4228526/v1,
27. https://doi.org/10.1038/s41467-025-64394-y,
28. https://doi.org/10.1146/annurev.cellbio.23.090506.123326,
29. https://doi.org/10.1534/g3.120.401632,
30. https://doi.org/10.1016/j.semcdb.2009.09.005,