---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-04T14:31:36.265237'
end_time: '2026-07-04T14:59:37.545911'
duration_seconds: 1681.28
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: worm
  gene_id: wago-4
  gene_symbol: wago-4
  uniprot_accession: O62275
  protein_description: 'RecName: Full=Argonaute protein wago-4 {ECO:0000305}; AltName:
    Full=Worm-specific argonaute protein 4 {ECO:0000312|WormBase:F58G1.1};'
  gene_info: Name=wago-4 {ECO:0000312|WormBase:F58G1.1}; ORFNames=F58G1.1 {ECO:0000312|WormBase:F58G1.1};
  organism_full: Caenorhabditis elegans.
  protein_family: Belongs to the argonaute family. WAGO subfamily.
  protein_domains: PAZ_dom. (IPR003100); PAZ_dom_sf. (IPR036085); Piwi. (IPR003165);
    RNaseH-like_sf. (IPR012337); RNaseH_sf. (IPR036397)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 34
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: wago-4-deep-research-falcon_artifacts/artifact-00.md
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
- **UniProt Accession:** O62275
- **Protein Description:** RecName: Full=Argonaute protein wago-4 {ECO:0000305}; AltName: Full=Worm-specific argonaute protein 4 {ECO:0000312|WormBase:F58G1.1};
- **Gene Information:** Name=wago-4 {ECO:0000312|WormBase:F58G1.1}; ORFNames=F58G1.1 {ECO:0000312|WormBase:F58G1.1};
- **Organism (full):** Caenorhabditis elegans.
- **Protein Family:** Belongs to the argonaute family. WAGO subfamily.
- **Key Domains:** PAZ_dom. (IPR003100); PAZ_dom_sf. (IPR036085); Piwi. (IPR003165); RNaseH-like_sf. (IPR012337); RNaseH_sf. (IPR036397)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "wago-4" matches the protein description above**
2. **Verify the organism is correct:** Caenorhabditis elegans.
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'wago-4' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **wago-4** (gene ID: wago-4, UniProt: O62275) in worm.

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
- **UniProt Accession:** O62275
- **Protein Description:** RecName: Full=Argonaute protein wago-4 {ECO:0000305}; AltName: Full=Worm-specific argonaute protein 4 {ECO:0000312|WormBase:F58G1.1};
- **Gene Information:** Name=wago-4 {ECO:0000312|WormBase:F58G1.1}; ORFNames=F58G1.1 {ECO:0000312|WormBase:F58G1.1};
- **Organism (full):** Caenorhabditis elegans.
- **Protein Family:** Belongs to the argonaute family. WAGO subfamily.
- **Key Domains:** PAZ_dom. (IPR003100); PAZ_dom_sf. (IPR036085); Piwi. (IPR003165); RNaseH-like_sf. (IPR012337); RNaseH_sf. (IPR036397)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "wago-4" matches the protein description above**
2. **Verify the organism is correct:** Caenorhabditis elegans.
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'wago-4' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **wago-4** (gene ID: wago-4, UniProt: O62275) in worm.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Comprehensive Research Report: WAGO-4 (F58G1.1) — A Z-Granule Argonaute Protein Essential for Transgenerational Epigenetic Inheritance in *Caenorhabditis elegans*

## 1. Gene and Protein Identity

WAGO-4 (UniProt: O62275; ORF: F58G1.1) is a worm-specific Argonaute (AGO) protein encoded in the genome of *Caenorhabditis elegans*. It belongs to the WAGO (Worm-specific AGO) subfamily of the Argonaute protein family, which has undergone significant expansion in nematodes (seroussi2023acomprehensivesurvey pages 2-3, rees2020investigatingtherole pages 35-38). The *C. elegans* genome encodes 19 functional Argonaute proteins, of which approximately 11 belong to the WAGO clade (chen2026decodingargonautespecificity pages 47-49, seistrup2026crosstalkbetweenand pages 1-5). WAGO-4 contains the canonical Argonaute domain architecture, including PAZ and PIWI domains, and carries a divergent HKQK motif in its small RNA binding pocket that is characteristic of nematode WAGO proteins and determines preference for 22G-RNAs bearing 5′ triphosphate modifications (chen2026decodingargonautespecificity pages 15-18).

The following table summarizes the key properties of WAGO-4:

| Property | Summary |
|---|---|
| Gene name | **wago-4**; ORF **F58G1.1**; encodes worm-specific Argonaute protein 4 in *Caenorhabditis elegans* (seroussi2023acomprehensivesurvey pages 2-3, sendoel2019mina1andwago4 pages 2-4) |
| UniProt ID | **O62275** (user-supplied target identifier; matches *C. elegans* WAGO-4 Argonaute context summarized in the cited literature) |
| Organism | **Caenorhabditis elegans** (wan2017transgenerationalepigeneticinheritance pages 1-5, seroussi2023acomprehensivesurvey pages 2-3) |
| Protein family | Argonaute family, **WAGO subfamily**; one of the expanded nematode worm-specific Argonautes involved in endogenous and heritable RNA silencing (chen2026decodingargonautespecificity pages 47-49, seroussi2023acomprehensivesurvey pages 2-3, rees2020investigatingtherole pages 35-38) |
| Domain architecture | Canonical Argonaute architecture with **PAZ** and **PIWI** domains; WAGO proteins also show a divergent **HKQK** motif associated with 22G-RNA loading specificity rather than the canonical Argonaute catalytic configuration (chen2026decodingargonautespecificity pages 15-18) |
| Subcellular localization | Germline **perinuclear granules**; localizes with **P granules** in early embryonic germline blastomeres, then demixes with ZNFX-1 into **Z granules**; in adults participates in ordered **PZM** assemblages with P granules and Mutator foci; loss of GLH FG repeats shifts WAGO-4 toward the **cytoplasm** (wan2017transgenerationalepigeneticinheritance pages 1-5, wan2017transgenerationalepigeneticinheritance pages 8-11, jelenic2025germgranulelocalization pages 5-6, jelenic2025germgranulelocalization pages 1-2, jelenic2025germgranulelocalization pages 10-11) |
| Small RNA binding specificity | Binds **22G-RNAs**; literature supports association with **CSR-class 22G-RNAs** and also cross-loading/binding of **both CSR-class and WAGO-class 22G-RNAs** under wild-type conditions; proper granule localization helps preserve correct loading specificity (sundby2021connectingthedots pages 7-9, chen2026decodingargonautespecificity pages 47-49, chen2026decodingargonautespecificity pages 12-15, jelenic2025germgranulelocalization pages 10-11, jelenic2025germgranulelocalization pages 12-13) |
| Primary function | Cytoplasmic/heritable silencing Argonaute required for **RNAi inheritance** and **transgenerational epigenetic inheritance (TEI)**; acts with ZNFX-1 to mark target mRNAs and maintain heritable siRNA expression across generations (xu2018distinctnuclearand pages 2-4, wan2017transgenerationalepigeneticinheritance pages 1-5, quarato2022inheritanceandmaintenance pages 3-3) |
| Functional pathway context | Part of the germline 22G-RNA network and a **CSR-1/WAGO-4 regulatory hub**; helps coordinate post-transcriptional silencing and inherited small-RNA responses in germ granules/Z granules (seroussi2023acomprehensivesurvey pages 16-17, sundby2021connectingthedots pages 7-9) |
| Key interaction partners | **ZNFX-1** (co-localized and cooperative factor in Z granules/TEI), **MINA-1** (physical and regulatory interactor that represses WAGO-4 expression), **CDE-1** (3' uridylation promotes WAGO-4 association with heritable small RNAs per review evidence), **GLH proteins** including GLH-1/4 FG repeats (promote granule partitioning), and **EGO-1** (proposed RdRP recruited in the inheritance pathway) (xu2018distinctnuclearand pages 2-4, wan2017transgenerationalepigeneticinheritance pages 1-5, sundby2021connectingthedots pages 7-9, jelenic2025germgranulelocalization pages 5-6, jelenic2025germgranulelocalization pages 10-11, sendoel2019mina1andwago4 pages 1-2, sendoel2019mina1andwago4 pages 11-13, sendoel2019mina1andwago4 pages 13-16) |
| Phenotypes of loss-of-function | **Heritable RNAi defective** phenotype; impaired transgenerational silencing/RNAi inheritance; altered endogenous target regulation; fertility defects and **Mortal Germline (Mrt)** phenotype are observed when WAGO-4 function or granule localization is compromised, especially at elevated temperature (sundby2021connectingthedots pages 7-9, xu2018distinctnuclearand pages 2-4, jelenic2025germgranulelocalization pages 1-2, jelenic2025germgranulelocalization pages 6-7, jelenic2025germgranulelocalization pages 7-8) |
| Phenotypes of mislocalization | Reduced enrichment in germ granules causes altered 22G-RNA loading, increased reliance on CSR-1-like targets, reduced regulation of WAGO-4-specific/piRNA- and MUT-16-dependent targets, and defective fertility/gene silencing fidelity (jelenic2025germgranulelocalization pages 1-2, jelenic2025germgranulelocalization pages 10-11, jelenic2025germgranulelocalization pages 12-13, jelenic2025germgranulelocalization pages 8-10) |
| Germline/apoptosis role | WAGO-4 also participates in a regulatory network with **MINA-1** that links RNAi machinery to **germ cell apoptosis**; elevated WAGO-4 in *mina-1* mutants increases RNAi sensitivity and germ cell death, while *wago-4* loss suppresses these phenotypes (sendoel2019mina1andwago4 pages 1-2, sendoel2019mina1andwago4 pages 11-13, sendoel2019mina1andwago4 pages 9-11, sendoel2019mina1andwago4 pages 13-16) |


*Table: This table summarizes the identity, localization, molecular associations, small-RNA specificity, and phenotypes of the *C. elegans* Argonaute WAGO-4. It is useful as a compact reference for functional annotation of UniProt O62275.*

## 2. Primary Function: Effector of RNA-Mediated Transgenerational Epigenetic Inheritance

WAGO-4 is a cytoplasmic Argonaute protein whose primary function is to mediate **transgenerational epigenetic inheritance (TEI)** of RNA interference (RNAi) responses. It was identified in a genetic screen for factors required for RNAi inheritance in *C. elegans* (wan2017transgenerationalepigeneticinheritance pages 1-5). WAGO-4 acts cooperatively with ZNFX-1, a conserved RNA helicase/zinc finger protein, to mark mRNAs of genes undergoing heritable silencing and to maintain small interfering RNA (siRNA) expression across multiple generations (xu2018distinctnuclearand pages 2-4, wan2017transgenerationalepigeneticinheritance pages 1-5). Specifically, WAGO-4 associates with heritable siRNAs to target mRNAs and recruit the RNA-dependent RNA polymerase EGO-1, which synthesizes a pool of heritable siRNAs that propagate the silencing signal to progeny (xu2018distinctnuclearand pages 2-4).

Importantly, WAGO-4 is not required for the initiation of RNAi in the parental generation but is essential for the transmission of silencing signals to offspring, a phenotype described as **Heritable RNAi Defective (Hrde)** (sundby2021connectingthedots pages 7-9). Loss of WAGO-4 results in failure to propagate RNAi-mediated gene silencing across generations, while within-generation silencing remains largely intact (sundby2021connectingthedots pages 7-9, wan2017transgenerationalepigeneticinheritance pages 1-5).

## 3. Small RNA Binding Specificity

WAGO-4 binds **22G-RNAs**, which are 22-nucleotide small RNAs with a 5′ guanine bias and 5′ triphosphate groups, synthesized by RNA-dependent RNA polymerases (RdRPs) (quarato2022inheritanceandmaintenance pages 2-3, chen2026decodingargonautespecificity pages 12-15). These secondary siRNAs are the major effector molecules of heritable silencing pathways in *C. elegans* (frolows2021smallrnasand pages 2-3).

A distinctive feature of WAGO-4 is its broader small RNA binding specificity compared to other WAGO proteins. Under wild-type conditions, WAGO-4 binds both **WAGO-class and CSR-class 22G-RNAs**, demonstrating a degree of cross-loading capability that is unusual among WAGO proteins (chen2026decodingargonautespecificity pages 12-15). In contrast, WAGO-1 and HRDE-1 specifically associate with WAGO-class 22G-RNAs, and CSR-1 binds CSR-class 22G-RNAs (chen2026decodingargonautespecificity pages 47-49, chen2026decodingargonautespecificity pages 12-15). This dual specificity positions WAGO-4 at the interface between the silencing (WAGO) and licensing (CSR-1) branches of the 22G-RNA pathway. The 3′ uridylation of 22G-RNAs by the terminal uridyltransferase CDE-1/CID-1 promotes their association with WAGO-4 and appears to drive its role in TEI (sundby2021connectingthedots pages 7-9).

The structural basis for 22G-RNA recognition involves the divergent **HKQK motif** in the small RNA binding pocket, which is critical for small RNA loading and silencing function—mutations disrupting this motif abolish binding and proper localization (chen2026decodingargonautespecificity pages 15-18).

## 4. Subcellular Localization: Z Granules and PZM Assemblages

WAGO-4 expression is specific to the germline in adult worms, where it localizes to **perinuclear germ granules** (sendoel2019mina1andwago4 pages 2-4). Its subcellular localization undergoes a developmentally regulated transition:

- **Early embryogenesis:** WAGO-4 co-localizes with ZNFX-1 within **P granules** in germline blastomeres (wan2017transgenerationalepigeneticinheritance pages 1-5).
- **Later development:** WAGO-4 and ZNFX-1 undergo a demixing process, separating from P granule components to form an independent liquid-like condensate termed the **Z granule** (wan2017transgenerationalepigeneticinheritance pages 8-11, wan2017transgenerationalepigeneticinheritance pages 1-5). This demixing correlates temporally with P granule association with nuclear pores and the onset of germline transcription.
- **Adult germline:** Z granules containing WAGO-4 assemble into spatially ordered tri-condensate structures called **PZM (P granule–Z granule–Mutator foci) assemblages**, in which Z granules spatially bridge P granules and Mutator foci (wan2017transgenerationalepigeneticinheritance pages 8-11, wan2017transgenerationalepigeneticinheritance pages 1-5).

The partitioning of WAGO-4 into germ granules is determined by **FG dipeptide repeats** in the Vasa-like GLH proteins (GLH-1, GLH-2, and GLH-4). Mutations converting phenylalanine to alanine in these FG motifs significantly reduce WAGO-4 enrichment in perinuclear puncta, causing it to redistribute to the cytoplasm (jelenic2025germgranulelocalization pages 5-6, jelenic2025germgranulelocalization pages 1-2, jelenic2025germgranulelocalization pages 10-11). In vitro phase separation experiments confirmed that FG dipeptides contribute to WAGO-4 recruitment into phase-separated granules, though their loss alone does not completely prevent recruitment, indicating additional mechanisms are also involved (jelenic2025germgranulelocalization pages 10-11).

## 5. Functional Significance of Germ Granule Localization

A landmark study by Jelenic et al. (2025) demonstrated that WAGO-4's localization within germ granules is essential for maintaining **fidelity in small RNA loading** (jelenic2025germgranulelocalization pages 1-2, jelenic2025germgranulelocalization pages 10-11, jelenic2025germgranulelocalization pages 12-13). When WAGO-4 is mislocalized to the cytoplasm (in FG-repeat mutants):

- WAGO-4 loses preferential binding to its specific targets, particularly genes not co-regulated by CSR-1 (jelenic2025germgranulelocalization pages 1-2, jelenic2025germgranulelocalization pages 10-11).
- The small RNA profile bound by WAGO-4 shifts to more closely resemble CSR-1's targeting pattern, with increased association with CSR-1-class targets (jelenic2025germgranulelocalization pages 10-11, jelenic2025germgranulelocalization pages 12-13).
- Targets dependent on germ granule-based small RNA biogenesis pathways (piRNA-dependent and MUT-16-dependent targets) show reduced WAGO-4 association (jelenic2025germgranulelocalization pages 10-11).
- Mislocalized WAGO-4 predominantly downregulates its targets, with 94% of downregulated targets also being CSR-1 targets, suggesting aberrant silencing of genes that CSR-1 normally licenses for expression (jelenic2025germgranulelocalization pages 12-13).
- WAGO-4 dysfunction is associated with downregulation of histone genes, which has been linked to chromatin instability and fertility defects (jelenic2025germgranulelocalization pages 8-10).

Similarly, when the P body component CGH-1 is absent, WAGO-4 is displaced from Z granules, leading to disturbed 22G-RNA loading, WAGO-4 instability, and defective RNAi inheritance (du2022pbodiescoat pages 54-56).

## 6. Role in Germ Cell Death and the MINA-1 Regulatory Network

Beyond its role in TEI, WAGO-4 participates in a regulatory network coordinating **germ cell apoptosis** with RNAi. Sendoel et al. (2019) showed that MINA-1, an RNA-binding protein, physically interacts with WAGO-4 and negatively regulates its expression by binding to the *wago-4* 3′-UTR to repress translation (sendoel2019mina1andwago4 pages 13-16, sendoel2019mina1andwago4 pages 7-9). In *mina-1* mutants:

- WAGO-4 protein levels increase up to fourfold (sendoel2019mina1andwago4 pages 11-13, sendoel2019mina1andwago4 pages 7-9).
- This overexpression leads to elevated germ cell apoptosis and RNAi hypersensitivity (sendoel2019mina1andwago4 pages 1-2, sendoel2019mina1andwago4 pages 11-13).
- Loss of WAGO-4 function suppresses the increased apoptosis and P granule defects in *mina-1* mutants (sendoel2019mina1andwago4 pages 11-13, sendoel2019mina1andwago4 pages 9-11).

MINA-1 and WAGO-4 are part of a broader RNA regulon including FBF-1, FBF-2, GLD-1, and PPW-2 that coordinately regulates stem cell proliferation, gene silencing, meiotic entry, and apoptosis (sendoel2019mina1andwago4 pages 7-9). This demonstrates that WAGO-4 protein levels must be tightly controlled for proper germline homeostasis.

## 7. WAGO-4 in the Context of the WAGO Argonaute Family

Within the expanded family of *C. elegans* Argonautes, WAGO-4 occupies a unique niche. Seroussi et al. (2023) showed that **CSR-1 and WAGO-4 form a regulatory hub** that targets most constitutively expressed germline Argonautes, distinguishing them from other WAGO proteins (seroussi2023acomprehensivesurvey pages 16-17). Other WAGO family members serve distinct functions: WAGO-1 and WAGO-3 mediate post-transcriptional gene silencing by binding WAGO-class 22G-RNAs; HRDE-1 (WAGO-9) operates in the nucleus for co-transcriptional silencing; and NRDE-3 (WAGO-12) functions in somatic nuclear RNAi (chen2026decodingargonautespecificity pages 47-49). WAGO-4's primary distinction is its dedicated role in **cytoplasmic RNAi inheritance** and its localization to Z granules (chen2026decodingargonautespecificity pages 47-49).

## 8. Nucleus-Independent Inheritance

Recent work by Rieger et al. (2023) demonstrated that RNAi can be inherited independently of nuclear factors via the ooplasm, relying on cytoplasmic components including germ granule-resident proteins. WAGO-4, which colocalizes with ZNFX-1 in germ granules, is implicated in this **nucleus-independent transgenerational inheritance** mechanism, supporting the model that small RNA-loaded Argonaute complexes within cytoplasmic granules serve as vehicles for transmitting epigenetic information from parents to embryos (quarato2022inheritanceandmaintenance pages 3-3).

## 9. Fertility and Mortal Germline Phenotype

Loss of WAGO-4 function or its mislocalization from germ granules is associated with **Mortal Germline (Mrt)** phenotypes, in which worms become progressively sterile over multiple generations, particularly at elevated temperatures (jelenic2025germgranulelocalization pages 7-8). Reduced WAGO-4 partitioning in germ granules leads to fertility defects including reduced progeny numbers and unfertilized oocytes (jelenic2025germgranulelocalization pages 6-7). These phenotypes underscore the importance of WAGO-4-mediated small RNA pathways for long-term germline maintenance and transgenerational genome integrity.

## 10. Summary

WAGO-4 is a germline-specific, Z granule-localized Argonaute protein that serves as a critical effector of transgenerational epigenetic inheritance in *C. elegans*. It binds 22G-RNAs (both CSR-class and WAGO-class), cooperates with ZNFX-1 within Z granules to propagate heritable gene silencing signals across generations, and requires proper germ granule localization for faithful small RNA loading. Its protein levels are post-transcriptionally regulated by MINA-1, linking RNAi machinery to germ cell apoptosis control. WAGO-4 occupies a unique position at the intersection of the CSR-1 licensing and WAGO silencing pathways, and its dysfunction leads to heritable RNAi defects, mortal germline phenotypes, and compromised germline integrity.

References

1. (seroussi2023acomprehensivesurvey pages 2-3): Uri Seroussi, Andrew Lugowski, Lina Wadi, Robert X Lao, Alexandra R Willis, Winnie Zhao, Adam E Sundby, Amanda G Charlesworth, Aaron W Reinke, and Julie M Claycomb. A comprehensive survey of c. elegans argonaute proteins reveals organism-wide gene regulatory networks and functions. Feb 2023. URL: https://doi.org/10.7554/elife.83853, doi:10.7554/elife.83853. This article has 129 citations and is from a domain leading peer-reviewed journal.

2. (rees2020investigatingtherole pages 35-38): Alice Rees. Investigating the role of the ip3 signalling pathway in rna interference in c. elegans. ArXiv, Jul 2020. URL: https://doi.org/10.17863/cam.55509, doi:10.17863/cam.55509. This article has 0 citations.

3. (chen2026decodingargonautespecificity pages 47-49): Shihui Chen and C. Phillips. Decoding argonaute specificity: insights from c. elegans and beyond. RNA, 32:290-310, Dec 2026. URL: https://doi.org/10.1261/rna.080816.125, doi:10.1261/rna.080816.125. This article has 2 citations and is from a domain leading peer-reviewed journal.

4. (seistrup2026crosstalkbetweenand pages 1-5): Ann-Sophie Seistrup, Emily Nischwitz, Falk Butter, and René F. Ketting. Crosstalk between and developmental dynamics of <i>c. elegans</i> argonaute proteins. bioRxiv, Dec 2025. URL: https://doi.org/10.64898/2025.12.17.694999, doi:10.64898/2025.12.17.694999. This article has 1 citations.

5. (chen2026decodingargonautespecificity pages 15-18): Shihui Chen and C. Phillips. Decoding argonaute specificity: insights from c. elegans and beyond. RNA, 32:290-310, Dec 2026. URL: https://doi.org/10.1261/rna.080816.125, doi:10.1261/rna.080816.125. This article has 2 citations and is from a domain leading peer-reviewed journal.

6. (sendoel2019mina1andwago4 pages 2-4): Ataman Sendoel, Deni Subasic, Luca Ducoli, Martin Keller, Erich Michel, Ines Kohler, Kapil Dev Singh, Xue Zheng, Anneke Brümmer, Jochen Imig, Shivendra Kishore, Yibo Wu, Alexander Kanitz, Andres Kaech, Nitish Mittal, Ana M. Matia-González, André P. Gerber, Mihaela Zavolan, Ruedi Aebersold, Jonathan Hall, Frédéric H.-T. Allain, and Michael O. Hengartner. Mina-1 and wago-4 are part of regulatory network coordinating germ cell death and rnai in c. elegans. Cell Death & Differentiation, 26:2157-2178, Feb 2019. URL: https://doi.org/10.1038/s41418-019-0291-z, doi:10.1038/s41418-019-0291-z. This article has 6 citations and is from a domain leading peer-reviewed journal.

7. (wan2017transgenerationalepigeneticinheritance pages 1-5): Gang Wan, Brandon D. Fields, George Spracklin, Carolyn Phillips, and Scott Kennedy. Transgenerational epigenetic inheritance factors localize to spatially and temporally ordered liquid droplet assemblages. bioRxiv, Nov 2017. URL: https://doi.org/10.1101/220111, doi:10.1101/220111. This article has 4 citations.

8. (wan2017transgenerationalepigeneticinheritance pages 8-11): Gang Wan, Brandon D. Fields, George Spracklin, Carolyn Phillips, and Scott Kennedy. Transgenerational epigenetic inheritance factors localize to spatially and temporally ordered liquid droplet assemblages. bioRxiv, Nov 2017. URL: https://doi.org/10.1101/220111, doi:10.1101/220111. This article has 4 citations.

9. (jelenic2025germgranulelocalization pages 5-6): Stela Jelenic, Mathias S Renaud, Samantha Del Borrello, Joseph Gokcezade, Janos Bindics, Lisa Frasz, Philipp Czermak, Peter Duchek, and Julie M Claycomb. Germ granule localization of nematode argonaute wago-4 ensures fidelity in small rna loading. The EMBO Journal, 44:7211-7241, Oct 2025. URL: https://doi.org/10.1038/s44318-025-00606-x, doi:10.1038/s44318-025-00606-x. This article has 3 citations.

10. (jelenic2025germgranulelocalization pages 1-2): Stela Jelenic, Mathias S Renaud, Samantha Del Borrello, Joseph Gokcezade, Janos Bindics, Lisa Frasz, Philipp Czermak, Peter Duchek, and Julie M Claycomb. Germ granule localization of nematode argonaute wago-4 ensures fidelity in small rna loading. The EMBO Journal, 44:7211-7241, Oct 2025. URL: https://doi.org/10.1038/s44318-025-00606-x, doi:10.1038/s44318-025-00606-x. This article has 3 citations.

11. (jelenic2025germgranulelocalization pages 10-11): Stela Jelenic, Mathias S Renaud, Samantha Del Borrello, Joseph Gokcezade, Janos Bindics, Lisa Frasz, Philipp Czermak, Peter Duchek, and Julie M Claycomb. Germ granule localization of nematode argonaute wago-4 ensures fidelity in small rna loading. The EMBO Journal, 44:7211-7241, Oct 2025. URL: https://doi.org/10.1038/s44318-025-00606-x, doi:10.1038/s44318-025-00606-x. This article has 3 citations.

12. (sundby2021connectingthedots pages 7-9): Adam E. Sundby, Ruxandra I. Molnar, and Julie M. Claycomb. Connecting the dots: linking caenorhabditis elegans small rna pathways and germ granules. May 2021. URL: https://doi.org/10.1016/j.tcb.2020.12.012, doi:10.1016/j.tcb.2020.12.012. This article has 74 citations and is from a domain leading peer-reviewed journal.

13. (chen2026decodingargonautespecificity pages 12-15): Shihui Chen and C. Phillips. Decoding argonaute specificity: insights from c. elegans and beyond. RNA, 32:290-310, Dec 2026. URL: https://doi.org/10.1261/rna.080816.125, doi:10.1261/rna.080816.125. This article has 2 citations and is from a domain leading peer-reviewed journal.

14. (jelenic2025germgranulelocalization pages 12-13): Stela Jelenic, Mathias S Renaud, Samantha Del Borrello, Joseph Gokcezade, Janos Bindics, Lisa Frasz, Philipp Czermak, Peter Duchek, and Julie M Claycomb. Germ granule localization of nematode argonaute wago-4 ensures fidelity in small rna loading. The EMBO Journal, 44:7211-7241, Oct 2025. URL: https://doi.org/10.1038/s44318-025-00606-x, doi:10.1038/s44318-025-00606-x. This article has 3 citations.

15. (xu2018distinctnuclearand pages 2-4): Fei Xu, Shouhong Guang, and Xuezhu Feng. Distinct nuclear and cytoplasmic machineries cooperatively promote the inheritance of rnai in caenorhabditis elegans. Biology of the Cell, 110:217-224, Sep 2018. URL: https://doi.org/10.1111/boc.201800031, doi:10.1111/boc.201800031. This article has 9 citations and is from a peer-reviewed journal.

16. (quarato2022inheritanceandmaintenance pages 3-3): Piergiuseppe Quarato, Meetali Singh, Loan Bourdon, and Germano Cecere. Inheritance and maintenance of small rna‐mediated epigenetic effects. BioEssays, Mar 2022. URL: https://doi.org/10.1002/bies.202100284, doi:10.1002/bies.202100284. This article has 24 citations and is from a peer-reviewed journal.

17. (seroussi2023acomprehensivesurvey pages 16-17): Uri Seroussi, Andrew Lugowski, Lina Wadi, Robert X Lao, Alexandra R Willis, Winnie Zhao, Adam E Sundby, Amanda G Charlesworth, Aaron W Reinke, and Julie M Claycomb. A comprehensive survey of c. elegans argonaute proteins reveals organism-wide gene regulatory networks and functions. Feb 2023. URL: https://doi.org/10.7554/elife.83853, doi:10.7554/elife.83853. This article has 129 citations and is from a domain leading peer-reviewed journal.

18. (sendoel2019mina1andwago4 pages 1-2): Ataman Sendoel, Deni Subasic, Luca Ducoli, Martin Keller, Erich Michel, Ines Kohler, Kapil Dev Singh, Xue Zheng, Anneke Brümmer, Jochen Imig, Shivendra Kishore, Yibo Wu, Alexander Kanitz, Andres Kaech, Nitish Mittal, Ana M. Matia-González, André P. Gerber, Mihaela Zavolan, Ruedi Aebersold, Jonathan Hall, Frédéric H.-T. Allain, and Michael O. Hengartner. Mina-1 and wago-4 are part of regulatory network coordinating germ cell death and rnai in c. elegans. Cell Death & Differentiation, 26:2157-2178, Feb 2019. URL: https://doi.org/10.1038/s41418-019-0291-z, doi:10.1038/s41418-019-0291-z. This article has 6 citations and is from a domain leading peer-reviewed journal.

19. (sendoel2019mina1andwago4 pages 11-13): Ataman Sendoel, Deni Subasic, Luca Ducoli, Martin Keller, Erich Michel, Ines Kohler, Kapil Dev Singh, Xue Zheng, Anneke Brümmer, Jochen Imig, Shivendra Kishore, Yibo Wu, Alexander Kanitz, Andres Kaech, Nitish Mittal, Ana M. Matia-González, André P. Gerber, Mihaela Zavolan, Ruedi Aebersold, Jonathan Hall, Frédéric H.-T. Allain, and Michael O. Hengartner. Mina-1 and wago-4 are part of regulatory network coordinating germ cell death and rnai in c. elegans. Cell Death & Differentiation, 26:2157-2178, Feb 2019. URL: https://doi.org/10.1038/s41418-019-0291-z, doi:10.1038/s41418-019-0291-z. This article has 6 citations and is from a domain leading peer-reviewed journal.

20. (sendoel2019mina1andwago4 pages 13-16): Ataman Sendoel, Deni Subasic, Luca Ducoli, Martin Keller, Erich Michel, Ines Kohler, Kapil Dev Singh, Xue Zheng, Anneke Brümmer, Jochen Imig, Shivendra Kishore, Yibo Wu, Alexander Kanitz, Andres Kaech, Nitish Mittal, Ana M. Matia-González, André P. Gerber, Mihaela Zavolan, Ruedi Aebersold, Jonathan Hall, Frédéric H.-T. Allain, and Michael O. Hengartner. Mina-1 and wago-4 are part of regulatory network coordinating germ cell death and rnai in c. elegans. Cell Death & Differentiation, 26:2157-2178, Feb 2019. URL: https://doi.org/10.1038/s41418-019-0291-z, doi:10.1038/s41418-019-0291-z. This article has 6 citations and is from a domain leading peer-reviewed journal.

21. (jelenic2025germgranulelocalization pages 6-7): Stela Jelenic, Mathias S Renaud, Samantha Del Borrello, Joseph Gokcezade, Janos Bindics, Lisa Frasz, Philipp Czermak, Peter Duchek, and Julie M Claycomb. Germ granule localization of nematode argonaute wago-4 ensures fidelity in small rna loading. The EMBO Journal, 44:7211-7241, Oct 2025. URL: https://doi.org/10.1038/s44318-025-00606-x, doi:10.1038/s44318-025-00606-x. This article has 3 citations.

22. (jelenic2025germgranulelocalization pages 7-8): Stela Jelenic, Mathias S Renaud, Samantha Del Borrello, Joseph Gokcezade, Janos Bindics, Lisa Frasz, Philipp Czermak, Peter Duchek, and Julie M Claycomb. Germ granule localization of nematode argonaute wago-4 ensures fidelity in small rna loading. The EMBO Journal, 44:7211-7241, Oct 2025. URL: https://doi.org/10.1038/s44318-025-00606-x, doi:10.1038/s44318-025-00606-x. This article has 3 citations.

23. (jelenic2025germgranulelocalization pages 8-10): Stela Jelenic, Mathias S Renaud, Samantha Del Borrello, Joseph Gokcezade, Janos Bindics, Lisa Frasz, Philipp Czermak, Peter Duchek, and Julie M Claycomb. Germ granule localization of nematode argonaute wago-4 ensures fidelity in small rna loading. The EMBO Journal, 44:7211-7241, Oct 2025. URL: https://doi.org/10.1038/s44318-025-00606-x, doi:10.1038/s44318-025-00606-x. This article has 3 citations.

24. (sendoel2019mina1andwago4 pages 9-11): Ataman Sendoel, Deni Subasic, Luca Ducoli, Martin Keller, Erich Michel, Ines Kohler, Kapil Dev Singh, Xue Zheng, Anneke Brümmer, Jochen Imig, Shivendra Kishore, Yibo Wu, Alexander Kanitz, Andres Kaech, Nitish Mittal, Ana M. Matia-González, André P. Gerber, Mihaela Zavolan, Ruedi Aebersold, Jonathan Hall, Frédéric H.-T. Allain, and Michael O. Hengartner. Mina-1 and wago-4 are part of regulatory network coordinating germ cell death and rnai in c. elegans. Cell Death & Differentiation, 26:2157-2178, Feb 2019. URL: https://doi.org/10.1038/s41418-019-0291-z, doi:10.1038/s41418-019-0291-z. This article has 6 citations and is from a domain leading peer-reviewed journal.

25. (quarato2022inheritanceandmaintenance pages 2-3): Piergiuseppe Quarato, Meetali Singh, Loan Bourdon, and Germano Cecere. Inheritance and maintenance of small rna‐mediated epigenetic effects. BioEssays, Mar 2022. URL: https://doi.org/10.1002/bies.202100284, doi:10.1002/bies.202100284. This article has 24 citations and is from a peer-reviewed journal.

26. (frolows2021smallrnasand pages 2-3): Natalya Frolows and Alyson Ashe. Small rnas and chromatin in the multigenerational epigenetic landscape of caenorhabditis elegans. Philosophical Transactions of the Royal Society B, 376:20200112, Apr 2021. URL: https://doi.org/10.1098/rstb.2020.0112, doi:10.1098/rstb.2020.0112. This article has 61 citations.

27. (du2022pbodiescoat pages 54-56): Zhenzhen Du, Kun Shi, Jordan S. Brown, Tao He, Wei-Sheng Wu, Ying Zhang, Heng-Chi Lee, and Donglei Zhang. P bodies coat germ granules to promote transgenerational gene silencing in c. elegans. bioRxiv, Nov 2022. URL: https://doi.org/10.1101/2022.11.01.514641, doi:10.1101/2022.11.01.514641. This article has 1 citations.

28. (sendoel2019mina1andwago4 pages 7-9): Ataman Sendoel, Deni Subasic, Luca Ducoli, Martin Keller, Erich Michel, Ines Kohler, Kapil Dev Singh, Xue Zheng, Anneke Brümmer, Jochen Imig, Shivendra Kishore, Yibo Wu, Alexander Kanitz, Andres Kaech, Nitish Mittal, Ana M. Matia-González, André P. Gerber, Mihaela Zavolan, Ruedi Aebersold, Jonathan Hall, Frédéric H.-T. Allain, and Michael O. Hengartner. Mina-1 and wago-4 are part of regulatory network coordinating germ cell death and rnai in c. elegans. Cell Death & Differentiation, 26:2157-2178, Feb 2019. URL: https://doi.org/10.1038/s41418-019-0291-z, doi:10.1038/s41418-019-0291-z. This article has 6 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](wago-4-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. chen2026decodingargonautespecificity pages 15-18
2. wan2017transgenerationalepigeneticinheritance pages 1-5
3. xu2018distinctnuclearand pages 2-4
4. sundby2021connectingthedots pages 7-9
5. frolows2021smallrnasand pages 2-3
6. chen2026decodingargonautespecificity pages 12-15
7. jelenic2025germgranulelocalization pages 10-11
8. jelenic2025germgranulelocalization pages 12-13
9. jelenic2025germgranulelocalization pages 8-10
10. du2022pbodiescoat pages 54-56
11. seroussi2023acomprehensivesurvey pages 16-17
12. chen2026decodingargonautespecificity pages 47-49
13. quarato2022inheritanceandmaintenance pages 3-3
14. jelenic2025germgranulelocalization pages 7-8
15. jelenic2025germgranulelocalization pages 6-7
16. seroussi2023acomprehensivesurvey pages 2-3
17. rees2020investigatingtherole pages 35-38
18. seistrup2026crosstalkbetweenand pages 1-5
19. wan2017transgenerationalepigeneticinheritance pages 8-11
20. jelenic2025germgranulelocalization pages 5-6
21. jelenic2025germgranulelocalization pages 1-2
22. quarato2022inheritanceandmaintenance pages 2-3
23. https://doi.org/10.7554/elife.83853,
24. https://doi.org/10.17863/cam.55509,
25. https://doi.org/10.1261/rna.080816.125,
26. https://doi.org/10.64898/2025.12.17.694999,
27. https://doi.org/10.1038/s41418-019-0291-z,
28. https://doi.org/10.1101/220111,
29. https://doi.org/10.1038/s44318-025-00606-x,
30. https://doi.org/10.1016/j.tcb.2020.12.012,
31. https://doi.org/10.1111/boc.201800031,
32. https://doi.org/10.1002/bies.202100284,
33. https://doi.org/10.1098/rstb.2020.0112,
34. https://doi.org/10.1101/2022.11.01.514641,