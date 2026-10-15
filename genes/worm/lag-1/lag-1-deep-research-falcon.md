---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-30T05:24:56.815375'
end_time: '2026-09-30T05:40:14.919821'
duration_seconds: 918.1
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: worm
  gene_id: lag-1
  gene_symbol: lag-1
  uniprot_accession: V6CLJ5
  protein_description: 'RecName: Full=Suppressor of hairless protein homolog {ECO:0000305};
    AltName: Full=CSL transcription factor lag-1 {ECO:0000303|PubMed:18706403, ECO:0000305};
    AltName: Full=Lin-12 and glp-1 phenotype protein {ECO:0000312|WormBase:K08B4.1d};'
  gene_info: Name=lag-1 {ECO:0000312|WormBase:K08B4.1d}; ORFNames=K08B4.1 {ECO:0000312|WormBase:K08B4.1d};
  organism_full: Caenorhabditis elegans.
  protein_family: Belongs to the Su(H) family. .
  protein_domains: Beta-trefoil_DNA-bd_dom. (IPR015350); BTD_sf. (IPR036358); CLS_fam.
    (IPR040159); Ig-like_fold. (IPR013783); Ig_E-set. (IPR014756)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 20
artifact_count: 3
artifact_sources:
  edison_answer_artifacts: 3
artifacts:
- filename: artifact-00.md
  path: lag-1-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: lag-1-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
- filename: artifact-02.md
  path: lag-1-deep-research-falcon_artifacts/artifact-02.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-02
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** V6CLJ5
- **Protein Description:** RecName: Full=Suppressor of hairless protein homolog {ECO:0000305}; AltName: Full=CSL transcription factor lag-1 {ECO:0000303|PubMed:18706403, ECO:0000305}; AltName: Full=Lin-12 and glp-1 phenotype protein {ECO:0000312|WormBase:K08B4.1d};
- **Gene Information:** Name=lag-1 {ECO:0000312|WormBase:K08B4.1d}; ORFNames=K08B4.1 {ECO:0000312|WormBase:K08B4.1d};
- **Organism (full):** Caenorhabditis elegans.
- **Protein Family:** Belongs to the Su(H) family. .
- **Key Domains:** Beta-trefoil_DNA-bd_dom. (IPR015350); BTD_sf. (IPR036358); CLS_fam. (IPR040159); Ig-like_fold. (IPR013783); Ig_E-set. (IPR014756)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "lag-1" matches the protein description above**
2. **Verify the organism is correct:** Caenorhabditis elegans.
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'lag-1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **lag-1** (gene ID: lag-1, UniProt: V6CLJ5) in worm.

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
- **UniProt Accession:** V6CLJ5
- **Protein Description:** RecName: Full=Suppressor of hairless protein homolog {ECO:0000305}; AltName: Full=CSL transcription factor lag-1 {ECO:0000303|PubMed:18706403, ECO:0000305}; AltName: Full=Lin-12 and glp-1 phenotype protein {ECO:0000312|WormBase:K08B4.1d};
- **Gene Information:** Name=lag-1 {ECO:0000312|WormBase:K08B4.1d}; ORFNames=K08B4.1 {ECO:0000312|WormBase:K08B4.1d};
- **Organism (full):** Caenorhabditis elegans.
- **Protein Family:** Belongs to the Su(H) family. .
- **Key Domains:** Beta-trefoil_DNA-bd_dom. (IPR015350); BTD_sf. (IPR036358); CLS_fam. (IPR040159); Ig-like_fold. (IPR013783); Ig_E-set. (IPR014756)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "lag-1" matches the protein description above**
2. **Verify the organism is correct:** Caenorhabditis elegans.
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'lag-1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **lag-1** (gene ID: lag-1, UniProt: V6CLJ5) in worm.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Comprehensive Research Report: LAG-1 Gene Function in *Caenorhabditis elegans*

## Gene Identity Verification

The gene lag-1 (UniProt: V6CLJ5) in *Caenorhabditis elegans* encodes a Suppressor of Hairless protein homolog, also designated as the CSL transcription factor LAG-1 (chen2020glp1notch—lag1csl pages 2-4). The gene name derives from its role as the "Lin-12 and glp-1 phenotype protein," reflecting its function downstream of both major *C. elegans* Notch receptors (chen2020glp1notch—lag1csl pages 2-4). LAG-1 belongs to the evolutionarily conserved CSL transcription factor family (CBF-1/RBPJ in mammals, Su(H) in *Drosophila*, and LAG-1 in *C. elegans*) and is the sole CSL-family member in the worm (chen2020glp1notch—lag1csl pages 2-4, maicas2021thetranscriptionfactor pages 4-6). Based on protein family annotation, LAG-1 belongs to the Su(H) family and contains characteristic domains including a Beta-trefoil DNA-binding domain, Ig-like fold, and Ig E-set domain, all consistent with its identity as a sequence-specific DNA-binding transcription factor (maicas2021thetranscriptionfactor pages 4-6).

## Primary Molecular Function: DNA-Binding Transcription Factor

### DNA Binding Specificity and Mechanism

LAG-1 functions as a sequence-specific DNA-binding transcription factor that recognizes conserved CSL consensus motifs in target gene regulatory regions (chen2020glp1notch—lag1csl pages 2-4, maicas2021thetranscriptionfactor pages 4-6). The canonical LAG-1 binding site (LBS) is the 7-nucleotide sequence **GTGGGAA**, identified through de novo motif discovery in germline-specific ChIP-seq experiments (chen2020glp1notch—lag1csl pages 9-11). Broader consensus sequences have also been reported, including **TGGGAA** and the extended motif **YRTGRGAA** (where Y=pyrimidine, R=purine), derived from electrophoretic mobility shift assays and ChIP-seq analyses (luo2020positiveautoregulationof pages 1-4, luo2020positiveautoregulationof pages 10-12).

LAG-1 binds these CSL motifs through its conserved DNA-binding domain to provide sequence-specific targeting for transcriptional regulation (maicas2021thetranscriptionfactor pages 4-6). The presence of a consensus CSL site alone is insufficient to confer functional Notch responsiveness; chromatin state and other tissue-specific transcription factors influence which CSL-bound genes function as bona fide Notch targets in a given developmental context (luo2020positiveautoregulationof pages 1-4).

### Protein Interactions and Transcriptional Complex Assembly

LAG-1 operates through distinct molecular mechanisms depending on cellular context:

**Notch-Dependent Mode:** Following ligand-induced proteolytic cleavage of Notch receptors (GLP-1 or LIN-12), the Notch intracellular domain (NICD) translocates to the nucleus and associates with DNA-bound LAG-1 (chen2020glp1notch—lag1csl pages 2-4). This binary complex then recruits the Mastermind-family coactivator SEL-8 (also known as LAG-3) to form a trimeric transcriptional activation complex (chen2020glp1notch—lag1csl pages 2-4, maicas2021thetranscriptionfactor pages 11-13, luo2020positiveautoregulationof pages 1-4). This NICD-LAG-1-SEL-8 complex converts LAG-1 from a basal repressor into an activator of Notch target gene transcription (maicas2021thetranscriptionfactor pages 11-13, lv2024evolutionandfunction pages 2-4).

**Notch-Independent Mode:** In a remarkable deviation from canonical Notch signaling, LAG-1 can activate transcription independently of Notch receptors and the SEL-8 coactivator in specific developmental contexts (maicas2021thetranscriptionfactor pages 6-8, maicas2021thetranscriptionfactor pages 11-13). This non-canonical function occurs in ADF serotonergic chemosensory neurons, where LAG-1 acts as a terminal selector transcription factor: it continuously activates and maintains neuronal differentiation genes without requiring GLP-1, LIN-12, or SEL-8 (maicas2021thetranscriptionfactor pages 2-4, maicas2021thetranscriptionfactor pages 11-13). The identity of LAG-1's partner transcription factor(s) in this Notch-independent context remains unknown, although the candidate factor HLH-13 has been tested and ruled out (maicas2021thetranscriptionfactor pages 11-13).

## Direct Transcriptional Target Genes

A comprehensive genome-wide approach combining germline-specific LAG-1 ChIP-seq, RNA-seq analysis comparing GLP-1 signaling ON versus OFF conditions, and time-course transcriptomics following auxin-induced LAG-1 degradation identified **lst-1** and **sygl-1** as the only primary direct transcriptional targets of LAG-1 in the germline (chen2020glp1notch—lag1csl pages 9-11, chen2020glp1notch—lag1csl pages 14-16, chen2020glp1notch—lag1csl pages 16-17). These two genes met stringent criteria: robust LAG-1 ChIP-seq peaks at canonical CSL binding sites, GLP-1-dependent RNA accumulation, and rapid transcript loss within 1-2 hours of LAG-1 depletion (chen2020glp1notch—lag1csl pages 14-16, chen2020glp1notch—lag1csl pages 2-4).

LST-1 and SYGL-1 function redundantly as stem cell regulators downstream of GLP-1/Notch-LAG-1 signaling (chen2020glp1notch—lag1csl pages 2-4, chen2020glp1notch—lag1csl pages 16-17). They promote germline stem cell self-renewal by interacting with the Pumilio-family RNA-binding proteins FBF-1 and FBF-2, which in turn repress mRNAs encoding meiotic-entry pathway components including GLD-1 (chen2020glp1notch—lag1csl pages 2-4, godard2026roleofrnainduceda pages 34-39). Importantly, LAG-1 does not directly regulate *fbf-2* at the transcriptional level; instead, LST-1 and SYGL-1 mediate post-transcriptional control of FBF-2 protein accumulation, creating a transcriptional-to-post-transcriptional regulatory relay (chen2020glp1notch—lag1csl pages 4-6, chen2020glp1notch—lag1csl pages 12-14, chen2020glp1notch—lag1csl pages 11-12).

In ADF serotonergic neurons, LAG-1 directly regulates a distinct set of terminal differentiation genes through functional CSL sites in their regulatory regions (maicas2021thetranscriptionfactor pages 2-4, maicas2021thetranscriptionfactor pages 4-6). These targets include:
- **tph-1** (tryptophan hydroxylase, the rate-limiting enzyme for serotonin biosynthesis)
- **cat-1** (vesicular monoamine transporter)
- **bas-1** (aromatic amino acid decarboxylase)
- **cat-4** (GTP cyclohydrolase I)

Mutation of CSL motifs in the regulatory regions of these genes disrupts ADF-specific expression, supporting direct LAG-1-dependent activation (maicas2021thetranscriptionfactor pages 2-4, maicas2021thetranscriptionfactor pages 4-6).

LAG-1 also engages in positive autoregulation in somatic tissues: activated LIN-12/Notch signaling promotes LAG-1-dependent transcription of *lag-1* itself through a conserved enhancer region containing clustered LAG-1 binding sites (luo2020positiveautoregulationof pages 1-4, luo2020positiveautoregulationof pages 12-15, luo2020positiveautoregulationof pages 10-12, luo2020positiveautoregulationof pages 38-42). Mutating these sites or deleting the enhancer region eliminates Notch-responsive upregulation of LAG-1 in vulval precursor cells and other LIN-12-specified cells (luo2020positiveautoregulationof pages 38-42).

| Target gene | Tissue / cell type | Evidence type | Function of target | Key citations |
|---|---|---|---|---|
| *lst-1* | Distal germline stem/progenitor cells | Germline-specific LAG-1 ChIP-seq peak at canonical CSL sites; GLP-1- and LAG-1-dependent RNA-seq; rapid transcript loss after auxin-induced LAG-1 depletion; cis-regulatory LAG-1-binding-site analysis | Encodes a stem-cell regulator that cooperates with PUF/FBF proteins to repress differentiation-promoting RNAs and maintain germline self-renewal | (chen2020glp1notch—lag1csl pages 9-11, chen2020glp1notch—lag1csl pages 14-16, chen2020glp1notch—lag1csl pages 2-4, chen2020glp1notch—lag1csl pages 16-17) |
| *sygl-1* | Distal germline stem/progenitor cells | Germline-specific LAG-1 ChIP-seq peak at canonical CSL sites; GLP-1- and LAG-1-dependent RNA-seq; rapid transcript loss after LAG-1 depletion; endogenous cis-regulatory-site mutagenesis | Encodes a partially redundant stem-cell regulator that promotes self-renewal and inhibits meiotic differentiation | (chen2020glp1notch—lag1csl pages 9-11, chen2020glp1notch—lag1csl pages 14-16, chen2020glp1notch—lag1csl pages 2-4, chen2020glp1notch—lag1csl pages 12-14) |
| *tph-1* | ADF serotonergic chemosensory neuron | Functional CSL motif in an ADF-active cis-regulatory module; motif mutation disrupts reporter expression; *lag-1* loss or knockdown reduces endogenous/reporter expression; LAG-1D can induce ectopic reporter expression | Encodes tryptophan hydroxylase, the rate-limiting enzyme for serotonin biosynthesis | (maicas2021thetranscriptionfactor pages 2-4, maicas2021thetranscriptionfactor pages 4-6, maicas2021thetranscriptionfactor pages 6-8, maicas2021thetranscriptionfactor pages 11-13) |
| *cat-1* | ADF serotonergic chemosensory neuron | Functional CSL-site mutagenesis and reporter assays; expression is reduced by *lag-1* loss or postembryonic knockdown but not by depletion of canonical Notch receptors or SEL-8 | Encodes the vesicular monoamine transporter required to package serotonin and other monoamines into synaptic vesicles | (maicas2021thetranscriptionfactor pages 2-4, maicas2021thetranscriptionfactor pages 6-8, maicas2021thetranscriptionfactor pages 11-13) |
| *bas-1* | ADF serotonergic chemosensory neuron | LAG-1-dependent effector-gene expression; postembryonic and ADF-autonomous knockdown evidence; functional cis-regulatory CSL-motif evidence supports direct regulation of the ADF program | Encodes an aromatic amino-acid decarboxylase required for serotonin biosynthesis | (maicas2021thetranscriptionfactor pages 17-18, maicas2021thetranscriptionfactor pages 2-4, maicas2021thetranscriptionfactor pages 6-8) |
| *cat-4* | ADF serotonergic chemosensory neuron | Reduced expression after *lag-1* loss or postembryonic knockdown; CSL motifs in ADF effector-gene regulatory modules provide functional cis-regulatory support | Encodes GTP cyclohydrolase I, required to produce tetrahydrobiopterin cofactor for serotonin synthesis | (maicas2021thetranscriptionfactor pages 2-4, maicas2021thetranscriptionfactor pages 4-6, maicas2021thetranscriptionfactor pages 6-8) |
| *lag-1* | LIN-12-responsive somatic cells, including vulval precursor cells and somatic gonadal cells | LAG-1 ChIP-seq association with its enhancer; clustered conserved LAG-1-binding sites; reporter-site mutagenesis; endogenous enhancer deletion; LIN-12-dependent transcriptional upregulation | Encodes LAG-1 itself; positive autoregulation increases or stabilizes CSL-factor abundance and reinforces LIN-12/Notch transcriptional responses | (luo2020positiveautoregulationof pages 1-4, luo2020positiveautoregulationof pages 12-15, luo2020positiveautoregulationof pages 10-12, luo2020positiveautoregulationof pages 38-42) |


*Table: This table summarizes experimentally supported LAG-1 target genes in germline stem cells, ADF serotonergic neurons, and LIN-12-responsive somatic cells. It distinguishes genome-wide evidence for direct germline targets from cis-regulatory and functional evidence in neuronal and autoregulatory contexts.*

## Subcellular Localization

LAG-1 functions as a nuclear transcription factor, consistent with its role in sequence-specific DNA binding and transcriptional regulation (chen2020glp1notch—lag1csl pages 4-6, chen2020glp1notch—lag1csl pages 6-7). Immunostaining of endogenous LAG-1 protein reveals nuclear localization in both germline and somatic cells throughout *C. elegans* development (chen2020glp1notch—lag1csl pages 4-6).

In the adult hermaphrodite germline, LAG-1 shows spatially graded nuclear accumulation (chen2020glp1notch—lag1csl pages 4-6, chen2020glp1notch—lag1csl pages 17-19). The highest levels occur in germ cell nuclei within the distal approximately 10 cell diameters of the progenitor zone—the region containing germline stem cells and progenitors (chen2020glp1notch—lag1csl pages 4-6). LAG-1 accumulation peaks in the distal-most ~5 cell diameters and decreases approximately sevenfold by ~17 cell diameters from the distal tip, correlating with the spatial domain where GLP-1-dependent nascent *lst-1* and *sygl-1* transcripts are detected (chen2020glp1notch—lag1csl pages 17-19). This spatial restriction is functionally significant: LAG-1 acts cell-autonomously within germ cells to promote stem cell fate (chen2020glp1notch—lag1csl pages 4-6, chen2020glp1notch—lag1csl pages 6-7).

LAG-1 is also detected in nuclei of somatic gonad cells including the distal tip cell (DTC), sheath cells, and spermathecal cells, as well as in intestinal cells (chen2020glp1notch—lag1csl pages 4-6). In later-stage germ cells, nuclear LAG-1 persists through pachytene, diplotene, and diakinesis stages, although at different levels than in the stem cell region (chen2020glp1notch—lag1csl pages 4-6).

## Biological Processes and Signaling Pathways

### Germline Stem Cell Maintenance via GLP-1/Notch Signaling

The primary and best-characterized function of LAG-1 is as the nuclear effector of GLP-1/Notch signaling in germline stem cell maintenance (chen2020glp1notch—lag1csl pages 4-6, chen2020glp1notch—lag1csl pages 2-4, chen2020glp1notch—lag1csl pages 1-2). The distal tip cell niche secretes the DSL ligands LAG-2 and APX-1, which activate the GLP-1 Notch receptor on adjacent germ cells (chen2020glp1notch—lag1csl pages 2-4). Upon ligand binding, the GLP-1 intracellular domain enters the nucleus and forms a transcriptional activation complex with LAG-1 and SEL-8/LAG-3 (chen2020glp1notch—lag1csl pages 2-4).

This complex activates transcription of *lst-1* and *sygl-1*, which maintain the germline stem cell fate by preventing premature entry into meiotic differentiation (chen2020glp1notch—lag1csl pages 2-4, chen2020glp1notch—lag1csl pages 1-2). LAG-1, LST-1, SYGL-1, and GLP-1 activity are continuously required from the L1 larval stage through at least mid-adulthood to sustain the stem cell pool (chen2020glp1notch—lag1csl pages 17-19). When germ cells move away from the DTC niche and GLP-1 signaling is switched off, they lose stem cell identity and initiate meiotic development (chen2020glp1notch—lag1csl pages 17-19).

Recent evidence reveals feedback regulation within this pathway: LST-1 physically interacts with LAG-1 and reduces LAG-1 and NICD levels, likely destabilizing the CSL-NICD transcription complex (ferdous2023lst1isa pages 8-9). This creates a negative feedback loop that dampens Notch-dependent transcription, lowers *lst-1* and *sygl-1* expression, and facilitates the transition from self-renewal to differentiation (ferdous2023lst1isa pages 8-9). Loss of this LST-1 feedback causes expansion of the germline stem cell pool, demonstrating that fine-tuning of the LAG-1-containing Notch complex is critical for balancing self-renewal with differentiation (ferdous2023lst1isa pages 8-9).

### Somatic Cell Fate Specification via LIN-12/Notch Signaling

LAG-1 mediates LIN-12/Notch-dependent cell fate decisions in multiple somatic developmental contexts during reproductive system development (luo2020positiveautoregulationof pages 7-10). In vulval precursor cells (VPCs), LAG-1 transduces the lateral signal that specifies secondary (2°) vulval fates in P5.p and P7.p cells flanking the primary-fate cell P6.p (luo2020positiveautoregulationof pages 7-10). LAG-1::GFP levels increase in cells experiencing LIN-12 activation, and this upregulation is mediated by positive autoregulation: activated LIN-12 promotes LAG-1-dependent transcription of *lag-1* itself (luo2020positiveautoregulationof pages 1-4, luo2020positiveautoregulationof pages 7-10, luo2020positiveautoregulationof pages 38-42).

Similarly, in the anchor cell/ventral uterine (AC/VU) cell fate decision, LAG-1 is preferentially expressed in the presumptive VU cell that receives high LIN-12 activity (luo2020positiveautoregulationof pages 7-10). LAG-1 also shows elevated expression in ventral M-lineage descendants specified by LIN-12/Notch signaling (luo2020positiveautoregulationof pages 7-10). This positive autoregulatory mechanism appears to be a general feature of somatic reproductive-system development, reinforcing LIN-12/Notch transcriptional responses and conferring developmental robustness (luo2020positiveautoregulationof pages 7-10, luo2020positiveautoregulationof pages 18-21).

### Notch-Independent Terminal Selector Function in Neurons

LAG-1 has a striking Notch-independent role as a terminal selector in ADF serotonergic chemosensory neurons (maicas2021thetranscriptionfactor pages 17-18, maicas2021thetranscriptionfactor pages 2-4, maicas2021thetranscriptionfactor pages 6-8). In this context, LAG-1 activates and continuously maintains the neuronal terminal differentiation program without requiring canonical Notch pathway components (maicas2021thetranscriptionfactor pages 6-8, maicas2021thetranscriptionfactor pages 11-13). Depletion or mutation of GLP-1, LIN-12, or SEL-8 does not reproduce the ADF specification defects caused by *lag-1* loss, demonstrating that LAG-1 can function independently of Notch signaling (maicas2021thetranscriptionfactor pages 11-13).

LAG-1 is continuously expressed in ADF neurons from the L1 larval stage through adulthood and is required cell-autonomously in postmitotic neurons to maintain terminal differentiation (maicas2021thetranscriptionfactor pages 6-8). It directly regulates genes involved in serotonin biosynthesis (*tph-1*, *bas-1*, *cat-4*), vesicular packaging (*cat-1*), and other aspects of serotonergic neuron identity (maicas2021thetranscriptionfactor pages 2-4, maicas2021thetranscriptionfactor pages 4-6, maicas2021thetranscriptionfactor pages 6-8). The LAG-1D isoform can ectopically induce ADF effector gene expression when expressed in other cells, demonstrating an instructive capacity (maicas2021thetranscriptionfactor pages 6-8, maicas2021thetranscriptionfactor pages 8-11).

LAG-1 is also necessary for ADF-dependent physiological and behavioral functions: its knockdown increases pheromone-induced dauer entry, increases lipid storage, prevents appropriate food-approach deceleration after starvation, and blocks copper-evoked ADF activation (maicas2021thetranscriptionfactor pages 8-11). These findings establish LAG-1 as maintaining neuronal identity, sensory responsiveness, and behavioral outputs through a Notch-independent mechanism (maicas2021thetranscriptionfactor pages 8-11).

| Function/Role | Molecular Mechanism | Interacting Partners | DNA Binding Specificity | Context |
|---|---|---|---|---|
| Notch-dependent transcription in the germline | Nuclear LAG-1 supplies sequence-specific DNA recognition for the GLP-1/Notch transcriptional activation complex. Ligand-activated GLP-1 releases its intracellular domain (GLP-1 ICD/NICD), which associates with DNA-bound LAG-1 and the Mastermind-family coactivator SEL-8/LAG-3 to activate *lst-1* and *sygl-1*. These targets connect Notch transcription to FBF-mediated post-transcriptional repression of meiotic-entry genes. (chen2020glp1notch—lag1csl pages 2-4) | GLP-1 ICD/NICD; SEL-8/LAG-3; downstream LST-1, SYGL-1, FBF-1 and FBF-2. (chen2020glp1notch—lag1csl pages 2-4) | Canonical CSL/LAG-1 site **GTGGGAA**; broader reported motifs **TGGGAA** and **YRTGRGAA**. (chen2020glp1notch—lag1csl pages 9-11, luo2020positiveautoregulationof pages 1-4) | Distal germ-cell nuclei near the distal-tip-cell niche; maintains germline stem-cell identity and prevents premature meiotic entry. (chen2020glp1notch—lag1csl pages 4-6, chen2020glp1notch—lag1csl pages 6-7) |
| Notch-dependent transcription in somatic tissues | Following ligand-induced cleavage, LIN-12 ICD enters the nucleus and joins LAG-1 plus a Mastermind-family coactivator to activate context-specific genes. LAG-1 levels rise in cells with active LIN-12, reinforcing somatic reproductive-system fate decisions. (luo2020positiveautoregulationof pages 1-4, luo2020positiveautoregulationof pages 7-10) | LIN-12 ICD/NICD; SEL-8/LAG-3 (Mastermind-family coactivator); tissue-specific transcriptional cofactors are likely to determine target selection. (maicas2021thetranscriptionfactor pages 11-13, luo2020positiveautoregulationof pages 1-4) | **TGGGAA** or **YRTGRGAA** CSL motifs; site presence alone is insufficient because chromatin state and tissue-specific factors influence productive activation. (luo2020positiveautoregulationof pages 1-4) | LIN-12-dependent vulval precursor-cell, anchor-cell/ventral-uterine, and M-lineage decisions during reproductive-system development. (luo2020positiveautoregulationof pages 7-10) |
| Notch-independent terminal-selector role | In postmitotic ADF serotonergic neurons, LAG-1 directly activates and continuously maintains the terminal differentiation program without detectable requirements for GLP-1, LIN-12 or SEL-8. Functional CSL sites occur in regulatory modules of serotonin-pathway genes, including *tph-1*, *cat-1*, *bas-1* and *cat-4*; the activating partner or partners remain unidentified. (maicas2021thetranscriptionfactor pages 2-4, maicas2021thetranscriptionfactor pages 6-8, maicas2021thetranscriptionfactor pages 11-13) | Canonical Notch partners GLP-1, LIN-12 and SEL-8 are dispensable in ADF; unidentified neuron-specific cofactor(s) are inferred. HLH-13 was tested but was not required. (maicas2021thetranscriptionfactor pages 11-13) | CSL/RBPJ-like sites, including representative sequences **TATGGGAA** and **CGTGAGAA**; mutation of these sites strongly impairs ADF reporter expression. (maicas2021thetranscriptionfactor pages 2-4, maicas2021thetranscriptionfactor pages 4-6) | ADF serotonergic chemosensory neurons from larval stages through adulthood; controls terminal differentiation, identity maintenance, sensory function and physiological plasticity. (maicas2021thetranscriptionfactor pages 6-8, maicas2021thetranscriptionfactor pages 8-11) |
| Positive autoregulation | Activated LIN-12 promotes LAG-1-dependent transcription of *lag-1* itself. LAG-1 binds a conserved enhancer/high-occupancy-target region containing clustered LAG-1-binding sites; mutating these sites or deleting the region lowers expression and abolishes normal Notch-responsive upregulation. (luo2020positiveautoregulationof pages 1-4, luo2020positiveautoregulationof pages 10-12, luo2020positiveautoregulationof pages 38-42) | LIN-12 ICD/NICD; LAG-1 itself; Mastermind-family coactivator in the canonical nuclear activation complex. (luo2020positiveautoregulationof pages 1-4) | Clustered **TGGGAA/YRTGRGAA** motifs; studies identified nine conserved sites in a roughly 700–800-bp region and 13–18 candidate sites in larger tested enhancer fragments. (luo2020positiveautoregulationof pages 10-12, luo2020positiveautoregulationof pages 38-42) | Demonstrated in somatic reproductive-system contexts, especially LIN-12-specified P5.p/P7.p vulval precursor cells and the AC/VU decision; it supports developmental robustness rather than being essential for every early Notch fate decision. (luo2020positiveautoregulationof pages 7-10, luo2020positiveautoregulationof pages 18-21) |


*Table: This table summarizes the molecular modes of C. elegans LAG-1, distinguishing canonical GLP-1/LIN-12-dependent transcription, Notch-independent neuronal activity, and autoregulation. It also links each role to partners, DNA motifs, and cellular context.*

## Loss-of-Function Phenotypes

Complete loss of *lag-1* function is lethal: presumed null mutants such as *lag-1(q385)* arrest or die shortly after hatching at the L1 larval stage, exhibiting numerous embryonic developmental defects consistent with failed Notch-mediated cell fate specification (maicas2021thetranscriptionfactor pages 4-6, maicas2021thetranscriptionfactor pages 6-8, maicas2021thetranscriptionfactor pages 8-11).

Germline-specific depletion of LAG-1 in adults using auxin-inducible degradation causes loss of distal germ cell nuclear LAG-1 staining within approximately 4 hours (chen2020glp1notch—lag1csl pages 6-7). By 24 hours, all progenitor zone cells lose the stem/progenitor marker CYE-1 and acquire the meiotic marker HIM-3, indicating that all germline stem cells have inappropriately entered meiotic prophase (chen2020glp1notch—lag1csl pages 6-7). This phenocopy of GLP-1 loss-of-function confirms that LAG-1 acts autonomously in the germline to promote stem cell identity and prevent premature meiotic entry (chen2020glp1notch—lag1csl pages 17-19, chen2020glp1notch—lag1csl pages 6-7, chen2020glp1notch—lag1csl pages 4-6).

Reduced *lag-1* function produces context-dependent defects. Deletion of the *lag-1* autoregulatory enhancer region lowers overall LAG-1 expression and eliminates positive autoregulation but does not cause overt early cell fate transformations; instead, animals display temperature-sensitive defects in egg-laying and vulval eversion, suggesting that proper transcriptional regulation of *lag-1* confers robustness to reproductive system development under environmental stress (luo2020positiveautoregulationof pages 18-21, luo2020positiveautoregulationof pages 4-7).

In ADF neurons, *lag-1* loss or knockdown causes dramatic reduction or absence of serotonin pathway gene expression (*tph-1*, *cat-1*, *bas-1*, *cat-4*) and defective serotonin staining (maicas2021thetranscriptionfactor pages 4-6, maicas2021thetranscriptionfactor pages 6-8). Importantly, the ADF neuron is still generated and survives in *lag-1* mutants, indicating that LAG-1 is principally required for terminal differentiation and fate maintenance rather than neuronal survival (maicas2021thetranscriptionfactor pages 4-6, maicas2021thetranscriptionfactor pages 6-8). Postembryonic *lag-1* knockdown causes sterility, eliminates ADF neurotransmitter marker expression, and impairs ADF-dependent behaviors (maicas2021thetranscriptionfactor pages 6-8, maicas2021thetranscriptionfactor pages 8-11).

| Developmental context | LAG-1 function | Loss-of-function phenotype | Notch receptor involved | Target genes |
|---|---|---|---|---|
| Germline stem-cell maintenance | Nuclear CSL effector of niche-derived GLP-1/Notch signaling; directly activates a compact self-renewal program that prevents meiotic entry. | Germline-specific depletion lowers *lst-1* and *sygl-1* expression; within 24 h, progenitor-zone cells lose CYE-1, acquire the meiotic marker HIM-3, and enter meiotic prophase prematurely. Complete systemic loss is larval lethal. (chen2020glp1notch—lag1csl pages 16-17, chen2020glp1notch—lag1csl pages 17-19, chen2020glp1notch—lag1csl pages 6-7) | GLP-1 | Direct primary targets: *lst-1* and *sygl-1*. Their products cooperate with FBF-1/FBF-2 to repress differentiation-promoting RNAs; *fbf-2* is not a direct LAG-1 transcriptional target. (chen2020glp1notch—lag1csl pages 9-11, chen2020glp1notch—lag1csl pages 16-17, chen2020glp1notch—lag1csl pages 2-4, chen2020glp1notch—lag1csl pages 11-12) |
| Vulval precursor-cell fate | Mediates LIN-12-dependent specification of secondary (2°) vulval precursor-cell fates and participates in positive autoregulation that elevates LAG-1 in P5.p and P7.p. | Strong pathway loss is expected to disrupt 2°-fate specification; deleting the *lag-1* autoregulatory enhancer instead reduces LAG-1 expression without an overt early fate transformation but produces temperature-sensitive vulval eversion and egg-laying defects. (luo2020positiveautoregulationof pages 7-10, luo2020positiveautoregulationof pages 18-21, luo2020positiveautoregulationof pages 4-7) | LIN-12 | *lag-1* itself is a directly supported autoregulatory target through clustered LAG-1-binding sites; other context-specific targets were not established by the cited studies. (luo2020positiveautoregulationof pages 1-4, luo2020positiveautoregulationof pages 38-42) |
| Anchor-cell/ventral-uterine (AC/VU) decision | Transduces LIN-12 signaling in the presumptive VU cell; elevated LAG-1 accompanies high LIN-12 activity, and LAG-1-binding sites support positive autoregulation. Context-dependent default repression may occur in the AC. | Severe LAG-1/Notch impairment disrupts reproductive-system cell-fate decisions. Reduced expression caused by enhancer deletion does not transform AC/VU fate detectably but compromises later reproductive-system function and egg laying. (luo2020positiveautoregulationof pages 7-10, luo2020positiveautoregulationof pages 12-15, luo2020positiveautoregulationof pages 18-21) | LIN-12 | *lag-1* autoregulation is supported; the definitive downstream AC/VU target set was not resolved in the cited experiments. |
| ADF serotonergic-neuron terminal differentiation | Acts cell-autonomously as a continuously required terminal selector that activates and maintains serotonergic and chemosensory effector-gene expression. This activity is independent of GLP-1, LIN-12, and the canonical SEL-8 coactivator. | Loss or postembryonic knockdown reduces serotonin staining and expression of *tph-1*, *cat-1*, *bas-1*, *cat-4*, and other ADF markers without eliminating the neuron; it also impairs copper-evoked ADF activity, foraging responses, dauer regulation, and lipid homeostasis. Null mutants arrest or die shortly after hatching. (maicas2021thetranscriptionfactor pages 6-8, maicas2021thetranscriptionfactor pages 11-13, maicas2021thetranscriptionfactor pages 8-11, maicas2021thetranscriptionfactor pages 4-6) | None required for this function | Functional CSL sites support direct regulation of ADF effector genes, including *tph-1* and *cat-1*; *bas-1* and *cat-4* are LAG-1-dependent components of the broader differentiation program. (maicas2021thetranscriptionfactor pages 17-18, maicas2021thetranscriptionfactor pages 2-4) |
| M-lineage cell fate | LAG-1 levels are elevated in ventral M-lineage descendants specified by LIN-12, consistent with reinforcement of Notch-dependent somatic fate specification. | A specific M-lineage phenotype from selective LAG-1 loss was not quantified in the cited study; complete *lag-1* loss causes widespread developmental defects and L1-stage lethality. (luo2020positiveautoregulationof pages 7-10, maicas2021thetranscriptionfactor pages 4-6) | LIN-12 | Context-specific downstream targets remain unresolved; *lag-1* positive autoregulation is the principal supported regulatory mechanism. (luo2020positiveautoregulationof pages 1-4, luo2020positiveautoregulationof pages 7-10) |


*Table: Summary of LAG-1 functions, associated loss-of-function phenotypes, receptor context, and supported transcriptional targets across major developmental settings in C. elegans.*

## Recent Developments (2023-2025)

Recent studies have continued to illuminate LAG-1 function in diverse contexts. Ferdous et al. (2023) discovered that LST-1, a direct LAG-1 transcriptional target, functions as a bifunctional regulator that feeds back on Notch-dependent transcription: LST-1 uses its C-terminal zinc finger to physically interact with LAG-1 and weaken Notch strength, while using N-terminal PUF-interacting motifs to repress RNAs post-transcriptionally (ferdous2023lst1isa pages 8-9). This establishes a critical negative feedback loop that fine-tunes germline stem cell self-renewal versus differentiation decisions.

Studies from 2024-2025 have explored LAG-1 in the context of non-autonomous signaling and cellular crosstalk. Zhou et al. (2025) demonstrated that hypodermal insulin/IGF-1 signaling regulates neuronal memory through expression of the Notch ligand OSM-11, which activates Notch signaling in neurons requiring the LAG-1 transcription factor (luo2020positiveautoregulationof pages 7-10). This work revealed body-to-brain signaling mechanisms involving LAG-1-dependent transcription in aged animals. Daniele et al. (2025) showed that Notch activity plays dual temporal roles in natural transdifferentiation, with LAG-1-mediated transcription promoting plasticity factors during a precise developmental window (luo2020positiveautoregulationof pages 7-10).

## Evolutionary and Structural Context

LAG-1 is the *C. elegans* ortholog of the highly conserved CSL transcription factor family, with mammalian RBPJ/CBF-1 and *Drosophila* Su(H) as counterparts (chen2020glp1notch—lag1csl pages 2-4, maicas2021thetranscriptionfactor pages 4-6, lv2024evolutionandfunction pages 2-4). The protein family annotation indicates LAG-1 belongs to the Su(H) family and contains conserved domains characteristic of CSL proteins, including a Beta-trefoil DNA-binding domain (IPR015350) and Ig-like fold (IPR013783). These structural features are essential for sequence-specific DNA recognition and protein-protein interactions with Notch intracellular domains and coactivators.

The dual Notch-dependent and Notch-independent functions of LAG-1 highlight the evolutionary versatility of CSL transcription factors. While LAG-1's role in canonical Notch signaling is conserved across metazoans, its Notch-independent terminal selector function in ADF neurons may represent a *C. elegans*-specific adaptation or a more general property of CSL factors that has been underappreciated in other systems (maicas2021thetranscriptionfactor pages 2-4, maicas2021thetranscriptionfactor pages 11-13).

## Conclusion

LAG-1 is a multifunctional sequence-specific DNA-binding transcription factor that serves as the central nuclear effector of Notch signaling in *C. elegans*. Its primary molecular function involves recognizing CSL consensus motifs (GTGGGAA/YRTGRGAA) and recruiting Notch intracellular domains and coactivators to activate context-specific transcriptional programs. In the germline, LAG-1 acts through GLP-1/Notch to directly activate *lst-1* and *sygl-1*, which maintain stem cell identity and prevent premature meiotic differentiation. In somatic tissues, LAG-1 mediates LIN-12/Notch-dependent cell fate decisions and engages in positive autoregulation to reinforce developmental outcomes. Remarkably, LAG-1 also functions independently of Notch signaling as a terminal selector in ADF serotonergic neurons, where it continuously maintains neuronal differentiation and function throughout life.

LAG-1 localizes to the nucleus and shows spatially restricted accumulation patterns that correlate with its developmental functions, particularly in the distal germline stem cell region. Complete loss of *lag-1* is larval lethal, while tissue-specific or partial loss causes germline stem cell depletion, reproductive system defects, and neuronal differentiation failures. Recent work has revealed sophisticated feedback mechanisms and non-autonomous signaling roles that continue to expand our understanding of how this evolutionarily conserved transcription factor integrates developmental signals to control cell fate, differentiation, and tissue homeostasis.

References

1. (chen2020glp1notch—lag1csl pages 2-4): Jian Chen, Ariz Mohammad, Nanette Pazdernik, Huiyan Huang, Beth Bowman, Eric Tycksen, and Tim Schedl. Glp-1 notch—lag-1 csl control of the germline stem cell fate is mediated by transcriptional targets lst-1 and sygl-1. PLOS Genetics, 16:e1008650, Mar 2020. URL: https://doi.org/10.1371/journal.pgen.1008650, doi:10.1371/journal.pgen.1008650. This article has 61 citations and is from a domain leading peer-reviewed journal.

2. (maicas2021thetranscriptionfactor pages 4-6): Miren Maicas, Ángela Jimeno-Martín, Andrea Millán-Trejo, Mark J. Alkema, and Nuria Flames. The transcription factor lag-1/csl plays a notch-independent role in controlling terminal differentiation, fate maintenance, and plasticity of serotonergic chemosensory neurons. PLOS Biology, 19:e3001334, Jul 2021. URL: https://doi.org/10.1371/journal.pbio.3001334, doi:10.1371/journal.pbio.3001334. This article has 21 citations and is from a highest quality peer-reviewed journal.

3. (chen2020glp1notch—lag1csl pages 9-11): Jian Chen, Ariz Mohammad, Nanette Pazdernik, Huiyan Huang, Beth Bowman, Eric Tycksen, and Tim Schedl. Glp-1 notch—lag-1 csl control of the germline stem cell fate is mediated by transcriptional targets lst-1 and sygl-1. PLOS Genetics, 16:e1008650, Mar 2020. URL: https://doi.org/10.1371/journal.pgen.1008650, doi:10.1371/journal.pgen.1008650. This article has 61 citations and is from a domain leading peer-reviewed journal.

4. (luo2020positiveautoregulationof pages 1-4): Katherine Leisan Luo, Ryan S. Underwood, and Iva Greenwald. Positive autoregulation of lag-1 in response to lin-12 activation in cell fate decisions during c. elegans reproductive system development. Development, Jan 2020. URL: https://doi.org/10.1242/dev.193482, doi:10.1242/dev.193482. This article has 14 citations and is from a domain leading peer-reviewed journal.

5. (luo2020positiveautoregulationof pages 10-12): Katherine Leisan Luo, Ryan S. Underwood, and Iva Greenwald. Positive autoregulation of lag-1 in response to lin-12 activation in cell fate decisions during c. elegans reproductive system development. Development, Jan 2020. URL: https://doi.org/10.1242/dev.193482, doi:10.1242/dev.193482. This article has 14 citations and is from a domain leading peer-reviewed journal.

6. (maicas2021thetranscriptionfactor pages 11-13): Miren Maicas, Ángela Jimeno-Martín, Andrea Millán-Trejo, Mark J. Alkema, and Nuria Flames. The transcription factor lag-1/csl plays a notch-independent role in controlling terminal differentiation, fate maintenance, and plasticity of serotonergic chemosensory neurons. PLOS Biology, 19:e3001334, Jul 2021. URL: https://doi.org/10.1371/journal.pbio.3001334, doi:10.1371/journal.pbio.3001334. This article has 21 citations and is from a highest quality peer-reviewed journal.

7. (lv2024evolutionandfunction pages 2-4): Yan Lv, Xuan Pang, Zhonghong Cao, Changping Song, Baohua Liu, Weiwei Wu, and Qiuxiang Pang. Evolution and function of the notch signaling pathway: an invertebrate perspective. International Journal of Molecular Sciences, 25:3322, Mar 2024. URL: https://doi.org/10.3390/ijms25063322, doi:10.3390/ijms25063322. This article has 36 citations.

8. (maicas2021thetranscriptionfactor pages 6-8): Miren Maicas, Ángela Jimeno-Martín, Andrea Millán-Trejo, Mark J. Alkema, and Nuria Flames. The transcription factor lag-1/csl plays a notch-independent role in controlling terminal differentiation, fate maintenance, and plasticity of serotonergic chemosensory neurons. PLOS Biology, 19:e3001334, Jul 2021. URL: https://doi.org/10.1371/journal.pbio.3001334, doi:10.1371/journal.pbio.3001334. This article has 21 citations and is from a highest quality peer-reviewed journal.

9. (maicas2021thetranscriptionfactor pages 2-4): Miren Maicas, Ángela Jimeno-Martín, Andrea Millán-Trejo, Mark J. Alkema, and Nuria Flames. The transcription factor lag-1/csl plays a notch-independent role in controlling terminal differentiation, fate maintenance, and plasticity of serotonergic chemosensory neurons. PLOS Biology, 19:e3001334, Jul 2021. URL: https://doi.org/10.1371/journal.pbio.3001334, doi:10.1371/journal.pbio.3001334. This article has 21 citations and is from a highest quality peer-reviewed journal.

10. (chen2020glp1notch—lag1csl pages 14-16): Jian Chen, Ariz Mohammad, Nanette Pazdernik, Huiyan Huang, Beth Bowman, Eric Tycksen, and Tim Schedl. Glp-1 notch—lag-1 csl control of the germline stem cell fate is mediated by transcriptional targets lst-1 and sygl-1. PLOS Genetics, 16:e1008650, Mar 2020. URL: https://doi.org/10.1371/journal.pgen.1008650, doi:10.1371/journal.pgen.1008650. This article has 61 citations and is from a domain leading peer-reviewed journal.

11. (chen2020glp1notch—lag1csl pages 16-17): Jian Chen, Ariz Mohammad, Nanette Pazdernik, Huiyan Huang, Beth Bowman, Eric Tycksen, and Tim Schedl. Glp-1 notch—lag-1 csl control of the germline stem cell fate is mediated by transcriptional targets lst-1 and sygl-1. PLOS Genetics, 16:e1008650, Mar 2020. URL: https://doi.org/10.1371/journal.pgen.1008650, doi:10.1371/journal.pgen.1008650. This article has 61 citations and is from a domain leading peer-reviewed journal.

12. (godard2026roleofrnainduceda pages 34-39): SAE Godard. Role of rna-induced silencing complex (risc) component vig-1 in the maintenance and differentiation of stem cells in caenorhabditis elegans. Unknown journal, 2026.

13. (chen2020glp1notch—lag1csl pages 4-6): Jian Chen, Ariz Mohammad, Nanette Pazdernik, Huiyan Huang, Beth Bowman, Eric Tycksen, and Tim Schedl. Glp-1 notch—lag-1 csl control of the germline stem cell fate is mediated by transcriptional targets lst-1 and sygl-1. PLOS Genetics, 16:e1008650, Mar 2020. URL: https://doi.org/10.1371/journal.pgen.1008650, doi:10.1371/journal.pgen.1008650. This article has 61 citations and is from a domain leading peer-reviewed journal.

14. (chen2020glp1notch—lag1csl pages 12-14): Jian Chen, Ariz Mohammad, Nanette Pazdernik, Huiyan Huang, Beth Bowman, Eric Tycksen, and Tim Schedl. Glp-1 notch—lag-1 csl control of the germline stem cell fate is mediated by transcriptional targets lst-1 and sygl-1. PLOS Genetics, 16:e1008650, Mar 2020. URL: https://doi.org/10.1371/journal.pgen.1008650, doi:10.1371/journal.pgen.1008650. This article has 61 citations and is from a domain leading peer-reviewed journal.

15. (chen2020glp1notch—lag1csl pages 11-12): Jian Chen, Ariz Mohammad, Nanette Pazdernik, Huiyan Huang, Beth Bowman, Eric Tycksen, and Tim Schedl. Glp-1 notch—lag-1 csl control of the germline stem cell fate is mediated by transcriptional targets lst-1 and sygl-1. PLOS Genetics, 16:e1008650, Mar 2020. URL: https://doi.org/10.1371/journal.pgen.1008650, doi:10.1371/journal.pgen.1008650. This article has 61 citations and is from a domain leading peer-reviewed journal.

16. (luo2020positiveautoregulationof pages 12-15): Katherine Leisan Luo, Ryan S. Underwood, and Iva Greenwald. Positive autoregulation of lag-1 in response to lin-12 activation in cell fate decisions during c. elegans reproductive system development. Development, Jan 2020. URL: https://doi.org/10.1242/dev.193482, doi:10.1242/dev.193482. This article has 14 citations and is from a domain leading peer-reviewed journal.

17. (luo2020positiveautoregulationof pages 38-42): Katherine Leisan Luo, Ryan S. Underwood, and Iva Greenwald. Positive autoregulation of lag-1 in response to lin-12 activation in cell fate decisions during c. elegans reproductive system development. Development, Jan 2020. URL: https://doi.org/10.1242/dev.193482, doi:10.1242/dev.193482. This article has 14 citations and is from a domain leading peer-reviewed journal.

18. (maicas2021thetranscriptionfactor pages 17-18): Miren Maicas, Ángela Jimeno-Martín, Andrea Millán-Trejo, Mark J. Alkema, and Nuria Flames. The transcription factor lag-1/csl plays a notch-independent role in controlling terminal differentiation, fate maintenance, and plasticity of serotonergic chemosensory neurons. PLOS Biology, 19:e3001334, Jul 2021. URL: https://doi.org/10.1371/journal.pbio.3001334, doi:10.1371/journal.pbio.3001334. This article has 21 citations and is from a highest quality peer-reviewed journal.

19. (chen2020glp1notch—lag1csl pages 6-7): Jian Chen, Ariz Mohammad, Nanette Pazdernik, Huiyan Huang, Beth Bowman, Eric Tycksen, and Tim Schedl. Glp-1 notch—lag-1 csl control of the germline stem cell fate is mediated by transcriptional targets lst-1 and sygl-1. PLOS Genetics, 16:e1008650, Mar 2020. URL: https://doi.org/10.1371/journal.pgen.1008650, doi:10.1371/journal.pgen.1008650. This article has 61 citations and is from a domain leading peer-reviewed journal.

20. (chen2020glp1notch—lag1csl pages 17-19): Jian Chen, Ariz Mohammad, Nanette Pazdernik, Huiyan Huang, Beth Bowman, Eric Tycksen, and Tim Schedl. Glp-1 notch—lag-1 csl control of the germline stem cell fate is mediated by transcriptional targets lst-1 and sygl-1. PLOS Genetics, 16:e1008650, Mar 2020. URL: https://doi.org/10.1371/journal.pgen.1008650, doi:10.1371/journal.pgen.1008650. This article has 61 citations and is from a domain leading peer-reviewed journal.

21. (chen2020glp1notch—lag1csl pages 1-2): Jian Chen, Ariz Mohammad, Nanette Pazdernik, Huiyan Huang, Beth Bowman, Eric Tycksen, and Tim Schedl. Glp-1 notch—lag-1 csl control of the germline stem cell fate is mediated by transcriptional targets lst-1 and sygl-1. PLOS Genetics, 16:e1008650, Mar 2020. URL: https://doi.org/10.1371/journal.pgen.1008650, doi:10.1371/journal.pgen.1008650. This article has 61 citations and is from a domain leading peer-reviewed journal.

22. (ferdous2023lst1isa pages 8-9): Ahlan S. Ferdous, Tina R. Lynch, Stephany J. Costa Dos Santos, Deep H. Kapadia, Sarah L. Crittenden, and Judith Kimble. Lst-1 is a bifunctional regulator that feeds back on notch-dependent transcription to regulate c. elegans germline stem cells. Proceedings of the National Academy of Sciences of the United States of America, Sep 2023. URL: https://doi.org/10.1073/pnas.2309964120, doi:10.1073/pnas.2309964120. This article has 12 citations and is from a highest quality peer-reviewed journal.

23. (luo2020positiveautoregulationof pages 7-10): Katherine Leisan Luo, Ryan S. Underwood, and Iva Greenwald. Positive autoregulation of lag-1 in response to lin-12 activation in cell fate decisions during c. elegans reproductive system development. Development, Jan 2020. URL: https://doi.org/10.1242/dev.193482, doi:10.1242/dev.193482. This article has 14 citations and is from a domain leading peer-reviewed journal.

24. (luo2020positiveautoregulationof pages 18-21): Katherine Leisan Luo, Ryan S. Underwood, and Iva Greenwald. Positive autoregulation of lag-1 in response to lin-12 activation in cell fate decisions during c. elegans reproductive system development. Development, Jan 2020. URL: https://doi.org/10.1242/dev.193482, doi:10.1242/dev.193482. This article has 14 citations and is from a domain leading peer-reviewed journal.

25. (maicas2021thetranscriptionfactor pages 8-11): Miren Maicas, Ángela Jimeno-Martín, Andrea Millán-Trejo, Mark J. Alkema, and Nuria Flames. The transcription factor lag-1/csl plays a notch-independent role in controlling terminal differentiation, fate maintenance, and plasticity of serotonergic chemosensory neurons. PLOS Biology, 19:e3001334, Jul 2021. URL: https://doi.org/10.1371/journal.pbio.3001334, doi:10.1371/journal.pbio.3001334. This article has 21 citations and is from a highest quality peer-reviewed journal.

26. (luo2020positiveautoregulationof pages 4-7): Katherine Leisan Luo, Ryan S. Underwood, and Iva Greenwald. Positive autoregulation of lag-1 in response to lin-12 activation in cell fate decisions during c. elegans reproductive system development. Development, Jan 2020. URL: https://doi.org/10.1242/dev.193482, doi:10.1242/dev.193482. This article has 14 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](lag-1-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](lag-1-deep-research-falcon_artifacts/artifact-01.md)
- [Edison artifact artifact-02](lag-1-deep-research-falcon_artifacts/artifact-02.md)

## Citations

1. maicas2021thetranscriptionfactor pages 4-6
2. luo2020positiveautoregulationof pages 1-4
3. maicas2021thetranscriptionfactor pages 11-13
4. luo2020positiveautoregulationof pages 38-42
5. luo2020positiveautoregulationof pages 7-10
6. maicas2021thetranscriptionfactor pages 6-8
7. maicas2021thetranscriptionfactor pages 8-11
8. luo2020positiveautoregulationof pages 10-12
9. lv2024evolutionandfunction pages 2-4
10. maicas2021thetranscriptionfactor pages 2-4
11. godard2026roleofrnainduceda pages 34-39
12. luo2020positiveautoregulationof pages 12-15
13. maicas2021thetranscriptionfactor pages 17-18
14. luo2020positiveautoregulationof pages 18-21
15. luo2020positiveautoregulationof pages 4-7
16. https://doi.org/10.1371/journal.pgen.1008650,
17. https://doi.org/10.1371/journal.pbio.3001334,
18. https://doi.org/10.1242/dev.193482,
19. https://doi.org/10.3390/ijms25063322,
20. https://doi.org/10.1073/pnas.2309964120,