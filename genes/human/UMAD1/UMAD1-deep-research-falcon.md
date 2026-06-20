---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-20T05:28:57.705890'
end_time: '2026-06-20T05:37:15.345160'
duration_seconds: 497.64
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: UMAD1
  gene_symbol: UMAD1
  uniprot_accession: C9J7I0
  protein_description: 'RecName: Full=UBAP1-MVB12-associated (UMA)-domain containing
    protein 1 {ECO:0000312|HGNC:HGNC:48955}; AltName: Full=RPA3 antisense RNA 1 {ECO:0000312|HGNC:HGNC:48955};
    AltName: Full=RPA3 opposite strand {ECO:0000312|HGNC:HGNC:48955};'
  gene_info: Name=UMAD1 {ECO:0000312|HGNC:HGNC:48955}; Synonyms=RPA3-AS1 {ECO:0000312|HGNC:HGNC:48955},
    RPA3OS {ECO:0000312|HGNC:HGNC:48955};
  organism_full: Homo sapiens (Human).
  protein_family: Not specified in UniProt
  protein_domains: UBAP1-MVB12_assoc_domain. (IPR053292); UMA. (IPR023340)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 8
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: UMAD1-deep-research-falcon_artifacts/artifact-00.md
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
- **UniProt Accession:** C9J7I0
- **Protein Description:** RecName: Full=UBAP1-MVB12-associated (UMA)-domain containing protein 1 {ECO:0000312|HGNC:HGNC:48955}; AltName: Full=RPA3 antisense RNA 1 {ECO:0000312|HGNC:HGNC:48955}; AltName: Full=RPA3 opposite strand {ECO:0000312|HGNC:HGNC:48955};
- **Gene Information:** Name=UMAD1 {ECO:0000312|HGNC:HGNC:48955}; Synonyms=RPA3-AS1 {ECO:0000312|HGNC:HGNC:48955}, RPA3OS {ECO:0000312|HGNC:HGNC:48955};
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** UBAP1-MVB12_assoc_domain. (IPR053292); UMA. (IPR023340)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "UMAD1" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'UMAD1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **UMAD1** (gene ID: UMAD1, UniProt: C9J7I0) in human.

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
- **UniProt Accession:** C9J7I0
- **Protein Description:** RecName: Full=UBAP1-MVB12-associated (UMA)-domain containing protein 1 {ECO:0000312|HGNC:HGNC:48955}; AltName: Full=RPA3 antisense RNA 1 {ECO:0000312|HGNC:HGNC:48955}; AltName: Full=RPA3 opposite strand {ECO:0000312|HGNC:HGNC:48955};
- **Gene Information:** Name=UMAD1 {ECO:0000312|HGNC:HGNC:48955}; Synonyms=RPA3-AS1 {ECO:0000312|HGNC:HGNC:48955}, RPA3OS {ECO:0000312|HGNC:HGNC:48955};
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** UBAP1-MVB12_assoc_domain. (IPR053292); UMA. (IPR023340)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "UMAD1" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'UMAD1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **UMAD1** (gene ID: UMAD1, UniProt: C9J7I0) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Comprehensive Research Report: UMAD1 (UBAP1-MVB12-Associated Domain Containing Protein 1)

## Gene and Protein Identity

The human gene UMAD1 (UniProt: C9J7I0) encodes UBAP1-MVB12-associated domain containing protein 1, a recently characterized component of the endosomal sorting complex required for transport (ESCRT) machinery (glover2023umad1contributesto pages 1-3, glover2023umad1contributesto pages 3-6). UMAD1 is also known by alternative names RPA3-AS1 and RPA3OS in genomic annotations, though the functional literature focuses on its protein-coding capacity as an ESCRT-I subunit (glover2023umad1contributesto pages 1-3). The protein is conserved across vertebrates and shows ubiquitous expression in human tissues (glover2023umad1contributesto pages 3-6).

## Protein Structure and Domains

UMAD1 belongs to the MVB12-like protein family and contains a conserved N-terminal UMA (UBAP1-MVB12-associated) domain (glover2023umad1contributesto pages 3-6, flower2020ahelicalassembly pages 1-2). This domain defines a family of mammalian proteins that occupy equivalent positions to yeast Mvb12 in the ESCRT-I complex (flower2020ahelicalassembly pages 1-2, flower2020ahelicalassembly pages 2-3). The critical functional element within the UMA domain is a signature VPF motif at positions V89-P90-F91 (glover2023umad1contributesto pages 3-6). This motif is essential for ESCRT-I incorporation, as mutation of VPF to AAA completely abolishes binding to the ESCRT-I headpiece complex (glover2023umad1contributesto pages 3-6). Structural analysis reveals that the VPF motif makes direct contact with a hydrophobic pocket formed at the interface between TSG101 and VPS37 subunits within the ESCRT-I headpiece (glover2023umad1contributesto pages 3-6, flower2020ahelicalassembly pages 2-3). AlphaFold2 structural predictions support conserved interactions between the UMAD1 VPF motif and the TSG101-VPS37C heterodimer (glover2023umad1contributesto pages 3-6).

## Molecular Interactions and ESCRT-I Assembly

UMAD1 functions as a heterotetramer-forming subunit of ESCRT-I, where it selectively associates with the core ESCRT-I components TSG101 and VPS28, along with specific VPS37 isoforms (glover2023umad1contributesto pages 1-3, glover2023umad1contributesto pages 6-8, glover2023umad1contributesto pages 3-6). A defining feature of UMAD1 is its selective pairing preference for VPS37 subunits. UMAD1 shows the strongest association with VPS37C, followed by weaker but reproducible interaction with VPS37B (glover2023umad1contributesto pages 3-6). Under tested conditions, UMAD1 exhibits only marginal association with VPS37D and no detectable incorporation into complexes containing VPS37A (glover2023umad1contributesto pages 3-6). This selectivity distinguishes UMAD1 from other MVB12-like proteins; for example, UBAP1 preferentially pairs with VPS37A to form ubiquitin-binding ESCRT-I modules specialized for endosomal sorting (glover2023umad1contributesto pages 6-8).

The incorporation of MVB12-like subunits into ESCRT-I is mutually exclusive, as demonstrated by quantitative mass spectrometry showing that in UMAD1 knockout cells, the association of UBAP1 and MVB12A with TSG101 significantly increases, consistent with competition for the same binding site on the ESCRT-I headpiece (glover2023umad1contributesto pages 6-8). This mutually exclusive assembly pattern suggests that cells can form functionally distinct ESCRT-I complexes tailored to specific cellular processes based on which MVB12-like subunit and VPS37 isoform are incorporated.

## Primary Function: Role in Cytokinetic Abscission

The most thoroughly characterized function of UMAD1 is its essential role in cytokinetic abscission, the terminal membrane scission event that completes cell division by resolving the midbody between daughter cells (glover2023umad1contributesto pages 1-3, glover2023umad1contributesto pages 6-8). UMAD1 is recruited to the midbody during late stages of cytokinesis, where it colocalizes with TSG101 and persists until midbody resolution is complete (glover2023umad1contributesto pages 8-10). This recruitment is hierarchical: UMAD1 localization to the midbody requires both the midbody organizer CEP55 and the core ESCRT-I subunit TSG101 (glover2023umad1contributesto pages 8-10). Depletion of either CEP55 or TSG101 prevents UMAD1 recruitment to the midbody, and mutation of the VPF motif reduces UMAD1 midbody localization to background levels, confirming that ESCRT-I interaction is necessary for proper subcellular targeting (glover2023umad1contributesto pages 8-10).

UMAD1 plays a critical role in stabilizing the interaction between CEP55 and TSG101, thereby promoting formation of abscission-competent ESCRT-I assemblies at the midbody (glover2023umad1contributesto pages 6-8, glover2023umad1contributesto pages 3-6, glover2023umad1contributesto pages 10-13). The precise molecular mechanism by which UMAD1 stabilizes this interaction remains under investigation, but it may involve providing additional contact points between TSG101's proline-rich region and the ESCRT and ALIX-binding region (EABR) of CEP55, or inducing conformational changes in TSG101 that favor CEP55 engagement (glover2023umad1contributesto pages 8-10).

Loss of UMAD1 function produces several cellular phenotypes consistent with impaired cytokinesis. UMAD1 knockout cells show a 4-fold reduction in clonogenic growth compared to wild-type cells (glover2023umad1contributesto pages 6-8). At the cellular level, UMAD1-deficient cells exhibit modest increases in multinucleation at steady state and display delayed midbody resolution during live-cell imaging (glover2023umad1contributesto pages 6-8, glover2023umad1contributesto pages 8-10). These phenotypes are similar to those observed with TSG101 depletion, supporting the model that UMAD1 specifically functions within the ESCRT-I-mediated arm of the abscission pathway (glover2023umad1contributesto pages 6-8).

## Mechanism: ESCRT-III Dynamic Turnover

A particularly important mechanistic insight from recent research is that UMAD1's primary function is not simply recruiting ESCRT-III to the midbody, but rather facilitating the dynamic turnover and exchange of ESCRT-III subunits at this site (glover2023umad1contributesto pages 10-13, glover2023umad1contributesto pages 8-10). Fluorescence recovery after photobleaching (FRAP) experiments using CHMP4B-L-GFP as an ESCRT-III marker revealed that while ESCRT-III recruitment to the midbody is not significantly impaired in UMAD1-deficient cells, the dynamic exchange of ESCRT-III subunits with the cytoplasmic pool is substantially reduced (glover2023umad1contributesto pages 8-10). This dynamic turnover is essential for productive ESCRT-III filament growth and membrane scission activity. The UMAD1-dependent facilitation of ESCRT-III dynamics may involve ensuring proper midbody architecture for ESCRT-III nucleation, stabilizing interactions that promote VPS4-mediated ESCRT-III polymer remodeling, or coordinating with ALIX to scaffold ESCRT-III assembly (glover2023umad1contributesto pages 10-13).

## Functional Redundancy with ALIX

UMAD1 exhibits functional redundancy and synergy with ALIX, another major ESCRT-associated protein that recruits ESCRT-III to the midbody through a parallel pathway (glover2023umad1contributesto pages 6-8, glover2023umad1contributesto pages 8-10). While partial depletion of ALIX alone or UMAD1 loss alone produces modest cytokinesis defects, co-depletion of both factors causes synergistic increases in multinucleation and severe delays in abscission (glover2023umad1contributesto pages 6-8). This synergy occurs despite the fact that ESCRT-III recruitment to the midbody remains largely intact in doubly-depleted cells, reinforcing the conclusion that UMAD1 and ALIX cooperate primarily to support ESCRT-III dynamic exchange rather than initial recruitment (glover2023umad1contributesto pages 8-10). The existence of parallel UMAD1/ESCRT-I and ALIX-dependent pathways likely provides functional plasticity that allows cells to adapt cytokinesis to different tissue environments with varying expression levels of ESCRT components (glover2023umad1contributesto pages 10-13).

## Subcellular Localization

UMAD1 exhibits context-dependent subcellular localization. During cell division, UMAD1 localizes to the midbody during late cytokinesis, where it remains until abscission is completed (glover2023umad1contributesto pages 8-10). This midbody recruitment is entirely dependent on CEP55 and TSG101, positioning UMAD1 downstream of these factors in the abscission pathway (glover2023umad1contributesto pages 8-10). Outside of mitosis, as a component of the ESCRT-I machinery, UMAD1 is expected to function at endosomal membranes, consistent with the general role of ESCRT-I in endosomal sorting and multivesicular body (MVB) biogenesis (flower2020ahelicalassembly pages 1-2, gentili2023escrtdependentstingdegradation pages 1-2). While direct endosomal localization of UMAD1 has not been extensively documented in the available literature, the broader ESCRT framework and the identification of UMA-domain proteins in endosomal proteomics studies support this inference (gentili2023escrtdependentstingdegradation pages 3-4).

## Biological Pathways and Processes

UMAD1 participates in multiple ESCRT-mediated cellular processes:

**Cytokinetic abscission pathway**: UMAD1 forms cytokinesis-specific ESCRT-I assemblies containing VPS37B or VPS37C that are recruited by CEP55 to facilitate ESCRT-III-mediated membrane scission at the midbody (glover2023umad1contributesto pages 1-3, glover2023umad1contributesto pages 6-8, glover2023umad1contributesto pages 10-13).

**Endosomal sorting and protein degradation**: As a component of ESCRT-I, UMAD1 belongs to the cellular machinery responsible for sorting ubiquitinated cargo into multivesicular bodies for lysosomal degradation (flower2020ahelicalassembly pages 1-2). Recent work on ESCRT-mediated STING degradation identified VPS37A and UBAP1 as key ESCRT-I components required for STING trafficking to lysosomes (gentili2023escrtdependentstingdegradation pages 1-2, gentili2023escrtdependentstingdegradation pages 3-4). While this specific study focused on UBAP1 rather than UMAD1, both proteins are UMA-domain-containing ESCRT-I subunits that occupy equivalent structural positions, suggesting that UMAD1 likely participates in analogous endosomal sorting processes with different cargo or VPS37 partner preferences (gentili2023escrtdependentstingdegradation pages 3-4).

**ESCRT-mediated membrane remodeling**: The ESCRT machinery functions in diverse membrane remodeling events including autophagosome closure, membrane repair, and viral budding (flower2020ahelicalassembly pages 1-2, flower2020ahelicalassembly pages 5-6). As an ESCRT-I component, UMAD1 is positioned to contribute to these processes, though specific roles beyond cytokinesis remain to be experimentally demonstrated.

## Structural Context: UMA Domain Architecture

The UMA domain represents a mammalian innovation in ESCRT-I architecture. While yeast ESCRT-I contains a single Mvb12 subunit, mammalian cells have evolved a family of UMA-domain proteins (MVB12A, MVB12B, UBAP1, UBA1L, and UMAD1) that can occupy this position (flower2020ahelicalassembly pages 1-2). Structural studies of the human ESCRT-I headpiece containing MVB12A revealed that the UMA-N segment adopts an S-shaped conformation comprising two short 310 helices followed by an antiparallel β-sheet formed with TSG101 (flower2020ahelicalassembly pages 2-3). Although the precise conformation differs from yeast Mvb12, which adopts an α-helical structure, both bind to the same region of the ESCRT-I headpiece (flower2020ahelicalassembly pages 2-3). This structural versatility in UMA domain binding, combined with selective VPS37 pairing, allows mammalian cells to generate a diverse repertoire of ESCRT-I complexes with specialized functions.

## Current Understanding and Evidence Limitations

UMAD1 was first identified and functionally characterized in a 2023 study by Glover et al., making it one of the most recently described human ESCRT components (glover2023umad1contributesto pages 1-3). The strongest experimental evidence supports UMAD1's role in cytokinetic abscission, with comprehensive biochemical, cell biological, and functional rescue experiments establishing its mechanism of action at the midbody (glover2023umad1contributesto pages 1-3, glover2023umad1contributesto pages 6-8, glover2023umad1contributesto pages 8-10). The identification of UMAD1 in proteomic datasets and its structural classification as a UMA-domain protein provide strong inference for its participation in broader ESCRT-I functions at endosomes (flower2020ahelicalassembly pages 1-2, gentili2023escrtdependentstingdegradation pages 3-4), though direct experimental demonstration of UMAD1-specific roles in endosomal cargo sorting, autophagosome closure, or membrane repair remains an important area for future investigation.

| Feature | UMAD1 summary | Evidence |
|---|---|---|
| Verified identity | Human **UMAD1** encodes **UBAP1-MVB12-associated domain-containing protein 1**; literature also notes it as a genuinely expressed vertebrate protein and a novel **MVB12-like ESCRT-I subunit**. This matches the UniProt-provided identity for **Homo sapiens** C9J7I0. | (glover2023umad1contributesto pages 1-3, glover2023umad1contributesto pages 3-6) |
| Alternative names / symbol context | UniProt aliases include **RPA3-AS1** and **RPA3OS**, but the protein-focused literature specifically studies the **protein-coding UMAD1** product in human cells as an ESCRT-associated factor; care is needed not to confuse the locus with antisense-RNA nomenclature. | (glover2023umad1contributesto pages 1-3, glover2023umad1contributesto pages 3-6) |
| Protein family / class | **MVB12-like, UMA-domain-containing ESCRT-I accessory subunit**. UMAD1 is incorporated into a subset of mammalian ESCRT-I heterotetramers together with TSG101, VPS28, and selected VPS37 isoforms. | (glover2023umad1contributesto pages 1-3, glover2023umad1contributesto pages 3-6, flower2020ahelicalassembly pages 1-2) |
| Key domains | UMAD1 contains a conserved **UMA (UBAP1-MVB12-associated) domain** in its N-terminal region; UMA proteins occupy the MVB12-like position in human ESCRT-I headpieces. | (glover2023umad1contributesto pages 3-6, flower2020ahelicalassembly pages 1-2, flower2020ahelicalassembly pages 2-3) |
| Critical motif | The **VPF motif** in UMAD1’s UMA domain (**V89-P90-F91**) is essential for ESCRT-I binding. Mutation of this motif abolishes ESCRT-I association and eliminates UMAD1 rescue of cytokinesis defects. | (glover2023umad1contributesto pages 3-6, glover2023umad1contributesto pages 6-8) |
| Structural interpretation | By analogy to structural work on human ESCRT-I with MVB12A, UMA-containing proteins bind a conserved site on the **TSG101–VPS37–VPS28 headpiece**. Glover et al. further report AlphaFold2-supported conserved contacts between UMAD1’s VPF motif and **TSG101/VPS37C**. | (glover2023umad1contributesto pages 3-6, flower2020ahelicalassembly pages 1-2, flower2020ahelicalassembly pages 2-3) |
| Core binding partners | Directly or selectively associated partners include **TSG101**, **VPS28**, **VPS37C**, **VPS37B**, and **CEP55**; UMAD1 does **not** appreciably enrich ESCRT-II in the reported affinity purifications. | (glover2023umad1contributesto pages 6-8, glover2023umad1contributesto pages 3-6) |
| VPS37 subunit preference | UMAD1 shows strongest pairing with **VPS37C**, weaker but reproducible pairing with **VPS37B**, marginal association with **VPS37D**, and no clear incorporation with **VPS37A** under the tested conditions. | (glover2023umad1contributesto pages 3-6) |
| Relationship to other MVB12-like subunits | UMAD1 is **mutually exclusive** with other MVB12-like ESCRT-I subunits; in UMAD1-knockout cells, **UBAP1** and **MVB12A** incorporation into TSG101 complexes increases, consistent with competition for the same ESCRT-I position. | (glover2023umad1contributesto pages 6-8) |
| Primary molecular function | UMAD1 acts as a **cytokinesis-specialized ESCRT-I subunit/adaptor**, stabilizing the **CEP55–TSG101/ESCRT-I** interaction and thereby supporting abscission-competent ESCRT assembly at the midbody. | (glover2023umad1contributesto pages 1-3, glover2023umad1contributesto pages 6-8, glover2023umad1contributesto pages 8-10) |
| Primary biological process | The best-supported primary role is in **cytokinetic abscission**, the terminal step of cell division. UMAD1 depletion causes abscission delay, increased multinucleation, and reduced clonogenic growth. | (glover2023umad1contributesto pages 6-8, glover2023umad1contributesto pages 8-10) |
| Mechanistic role in abscission | UMAD1 is required not mainly for initial ESCRT-III recruitment, but for efficient **dynamic turnover/exchange of ESCRT-III subunits** at the midbody, a property needed for productive membrane scission. | (glover2023umad1contributesto pages 8-10, glover2023umad1contributesto pages 10-13) |
| Functional relationship with ALIX | UMAD1 function is **partially redundant/synergistic** with the **ALIX** arm of abscission. Co-depletion of UMAD1 and partial ALIX loss strongly worsens cytokinesis failure despite preserved CHMP4B recruitment. | (glover2023umad1contributesto pages 6-8, glover2023umad1contributesto pages 8-10, glover2023umad1contributesto pages 10-13) |
| Subcellular localization | UMAD1 **co-localizes with TSG101 at the midbody** during late cytokinesis and persists there until midbody resolution. Its recruitment requires **CEP55** and **TSG101/ESCRT-I** interaction. | (glover2023umad1contributesto pages 8-10) |
| Localization dependency | Depletion of **TSG101** or **CEP55** blocks UMAD1 recruitment to the midbody, and the VPF-mutant UMAD1 shows only background midbody localization, indicating ESCRT-I-dependent targeting downstream of CEP55. | (glover2023umad1contributesto pages 8-10) |
| Endosomal/lysosomal relevance | Broader ESCRT literature places UMA-containing ESCRT-I proteins in endosomal sorting. STING-trafficking datasets identify **UBAP1**-containing ESCRT-I as a key endosomal STING-degradation module and list **UMAD1** among human UMA-domain ESCRT-I options, supporting inference that UMAD1 belongs to the same ESCRT-I architectural class even though direct STING evidence is for UBAP1 rather than UMAD1. | (flower2020ahelicalassembly pages 1-2, gentili2023escrtdependentstingdegradation pages 1-2, gentili2023escrtdependentstingdegradation pages 3-4) |
| What UMAD1 is not | UMAD1 is **not an enzyme or transporter** in the current literature; no catalytic reaction or transported substrate has been established. Its role is best described as a **scaffolding/adaptor component** that specifies ESCRT-I composition and function in membrane-remodeling pathways. | (glover2023umad1contributesto pages 1-3, glover2023umad1contributesto pages 3-6, flower2020ahelicalassembly pages 1-2) |


*Table: This table summarizes the verified identity, domains, binding partners, localization, and best-supported functions of human UMAD1. It is useful for functional annotation because it separates directly demonstrated UMAD1 roles in cytokinetic ESCRT-I from broader ESCRT inferences about endosomal processes.*

## Summary

UMAD1 functions as a specialized scaffolding and adaptor protein rather than as an enzyme or transporter. Its primary role is to specify the composition and function of ESCRT-I complexes in cytokinetic abscission. Through its UMA domain and signature VPF motif, UMAD1 selectively incorporates into ESCRT-I assemblies containing VPS37C or VPS37B, stabilizes the CEP55-ESCRT-I interaction at the midbody, and facilitates the dynamic exchange of ESCRT-III subunits necessary for productive membrane scission during cell division (glover2023umad1contributesto pages 1-3, glover2023umad1contributesto pages 6-8, glover2023umad1contributesto pages 3-6, glover2023umad1contributesto pages 10-13, glover2023umad1contributesto pages 8-10). As a member of the UMA-domain protein family, UMAD1 likely contributes to additional ESCRT-mediated membrane remodeling processes at endosomal compartments, though these functions are less well characterized experimentally compared to its established role in cytokinesis.

References

1. (glover2023umad1contributesto pages 1-3): James Glover, Edward J. Scourfield, Leandro N. Ventimiglia, Xiaoping Yang, Steven Lynham, Monica Agromayor, and Juan Martin-Serrano. Umad1 contributes to escrt-iii dynamic subunit turnover during cytokinetic abscission. Journal of Cell Science, Aug 2023. URL: https://doi.org/10.1242/jcs.261097, doi:10.1242/jcs.261097. This article has 4 citations and is from a domain leading peer-reviewed journal.

2. (glover2023umad1contributesto pages 3-6): James Glover, Edward J. Scourfield, Leandro N. Ventimiglia, Xiaoping Yang, Steven Lynham, Monica Agromayor, and Juan Martin-Serrano. Umad1 contributes to escrt-iii dynamic subunit turnover during cytokinetic abscission. Journal of Cell Science, Aug 2023. URL: https://doi.org/10.1242/jcs.261097, doi:10.1242/jcs.261097. This article has 4 citations and is from a domain leading peer-reviewed journal.

3. (flower2020ahelicalassembly pages 1-2): Thomas G. Flower, Yoshinori Takahashi, Arpa Hudait, Kevin Rose, Nicholas Tjahjono, Alexander J. Pak, Adam L. Yokom, Xinwen Liang, Hong-Gang Wang, Fadila Bouamr, Gregory A. Voth, and James H. Hurley. A helical assembly of human escrt-i scaffolds reverse-topology membrane scission. Nature Structural & Molecular Biology, 27:570-580, May 2020. URL: https://doi.org/10.1038/s41594-020-0426-4, doi:10.1038/s41594-020-0426-4. This article has 75 citations and is from a highest quality peer-reviewed journal.

4. (flower2020ahelicalassembly pages 2-3): Thomas G. Flower, Yoshinori Takahashi, Arpa Hudait, Kevin Rose, Nicholas Tjahjono, Alexander J. Pak, Adam L. Yokom, Xinwen Liang, Hong-Gang Wang, Fadila Bouamr, Gregory A. Voth, and James H. Hurley. A helical assembly of human escrt-i scaffolds reverse-topology membrane scission. Nature Structural & Molecular Biology, 27:570-580, May 2020. URL: https://doi.org/10.1038/s41594-020-0426-4, doi:10.1038/s41594-020-0426-4. This article has 75 citations and is from a highest quality peer-reviewed journal.

5. (glover2023umad1contributesto pages 6-8): James Glover, Edward J. Scourfield, Leandro N. Ventimiglia, Xiaoping Yang, Steven Lynham, Monica Agromayor, and Juan Martin-Serrano. Umad1 contributes to escrt-iii dynamic subunit turnover during cytokinetic abscission. Journal of Cell Science, Aug 2023. URL: https://doi.org/10.1242/jcs.261097, doi:10.1242/jcs.261097. This article has 4 citations and is from a domain leading peer-reviewed journal.

6. (glover2023umad1contributesto pages 8-10): James Glover, Edward J. Scourfield, Leandro N. Ventimiglia, Xiaoping Yang, Steven Lynham, Monica Agromayor, and Juan Martin-Serrano. Umad1 contributes to escrt-iii dynamic subunit turnover during cytokinetic abscission. Journal of Cell Science, Aug 2023. URL: https://doi.org/10.1242/jcs.261097, doi:10.1242/jcs.261097. This article has 4 citations and is from a domain leading peer-reviewed journal.

7. (glover2023umad1contributesto pages 10-13): James Glover, Edward J. Scourfield, Leandro N. Ventimiglia, Xiaoping Yang, Steven Lynham, Monica Agromayor, and Juan Martin-Serrano. Umad1 contributes to escrt-iii dynamic subunit turnover during cytokinetic abscission. Journal of Cell Science, Aug 2023. URL: https://doi.org/10.1242/jcs.261097, doi:10.1242/jcs.261097. This article has 4 citations and is from a domain leading peer-reviewed journal.

8. (gentili2023escrtdependentstingdegradation pages 1-2): Matteo Gentili, Bingxu Liu, Malvina Papanastasiou, Deborah Dele-Oni, Marc A. Schwartz, Rebecca J. Carlson, Aziz M. Al’Khafaji, Karsten Krug, Adam Brown, John G. Doench, Steven A. Carr, and Nir Hacohen. Escrt-dependent sting degradation inhibits steady-state and cgamp-induced signalling. Nature Communications, Feb 2023. URL: https://doi.org/10.1038/s41467-023-36132-9, doi:10.1038/s41467-023-36132-9. This article has 138 citations and is from a highest quality peer-reviewed journal.

9. (gentili2023escrtdependentstingdegradation pages 3-4): Matteo Gentili, Bingxu Liu, Malvina Papanastasiou, Deborah Dele-Oni, Marc A. Schwartz, Rebecca J. Carlson, Aziz M. Al’Khafaji, Karsten Krug, Adam Brown, John G. Doench, Steven A. Carr, and Nir Hacohen. Escrt-dependent sting degradation inhibits steady-state and cgamp-induced signalling. Nature Communications, Feb 2023. URL: https://doi.org/10.1038/s41467-023-36132-9, doi:10.1038/s41467-023-36132-9. This article has 138 citations and is from a highest quality peer-reviewed journal.

10. (flower2020ahelicalassembly pages 5-6): Thomas G. Flower, Yoshinori Takahashi, Arpa Hudait, Kevin Rose, Nicholas Tjahjono, Alexander J. Pak, Adam L. Yokom, Xinwen Liang, Hong-Gang Wang, Fadila Bouamr, Gregory A. Voth, and James H. Hurley. A helical assembly of human escrt-i scaffolds reverse-topology membrane scission. Nature Structural & Molecular Biology, 27:570-580, May 2020. URL: https://doi.org/10.1038/s41594-020-0426-4, doi:10.1038/s41594-020-0426-4. This article has 75 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](UMAD1-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. gentili2023escrtdependentstingdegradation pages 3-4
2. flower2020ahelicalassembly pages 1-2
3. flower2020ahelicalassembly pages 2-3
4. gentili2023escrtdependentstingdegradation pages 1-2
5. flower2020ahelicalassembly pages 5-6
6. https://doi.org/10.1242/jcs.261097,
7. https://doi.org/10.1038/s41594-020-0426-4,
8. https://doi.org/10.1038/s41467-023-36132-9,