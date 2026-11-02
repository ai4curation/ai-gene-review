---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-30T06:38:54.834477'
end_time: '2026-09-30T07:00:41.462880'
duration_seconds: 1306.63
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: DROME
  gene_id: 18w
  gene_symbol: 18w
  uniprot_accession: A1ZBR2
  protein_description: 'SubName: Full=18 wheeler {ECO:0000313|EMBL:AAF57509.1};'
  gene_info: Name=18w {ECO:0000313|EMBL:AAF57509.1, ECO:0000313|FlyBase:FBgn0287775};
    Synonyms=18-w {ECO:0000313|EMBL:AAF57509.1}, 18-wheeler {ECO:0000313|EMBL:AAF57509.1},
    18W {ECO:0000313|EMBL:AAF57509.1}, CT25100 {ECO:0000313|EMBL:AAF57509.1}, Dmel\CG8896
    {ECO:0000313|EMBL:AAF57509.1}, EP-709 {ECO:0000313|EMBL:AAF57509.1}, l(2)00053
    {ECO:0000313|EMBL:AAF57509.1}, tlr {ECO:0000313|EMBL:AAF57509.1}, toll {ECO:0000313|EMBL:AAF57509.1},
    Toll-2 {ECO:0000313|EMBL:AAF57509.1}, toll-2 {ECO:0000313|EMBL:AAF57509.1}, Toll2
    {ECO:0000313|EMBL:AAF57509.1}; ORFNames=CG8896 {ECO:0000313|EMBL:AAF57509.1, ECO:0000313|FlyBase:FBgn0287775},
    Dmel_CG8896 {ECO:0000313|EMBL:AAF57509.1};
  organism_full: Drosophila melanogaster (Fruit fly).
  protein_family: Belongs to the Toll-like receptor family.
  protein_domains: Cys-rich_flank_reg_C. (IPR000483); Leu-rich_rpt. (IPR001611); Leu-rich_rpt_typical-subtyp.
    (IPR003591); LRR_5. (IPR026906); LRR_dom_sf. (IPR032675)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 62
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: 18w-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: 18w-deep-research-falcon_artifacts/artifact-01.md
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
- **UniProt Accession:** A1ZBR2
- **Protein Description:** SubName: Full=18 wheeler {ECO:0000313|EMBL:AAF57509.1};
- **Gene Information:** Name=18w {ECO:0000313|EMBL:AAF57509.1, ECO:0000313|FlyBase:FBgn0287775}; Synonyms=18-w {ECO:0000313|EMBL:AAF57509.1}, 18-wheeler {ECO:0000313|EMBL:AAF57509.1}, 18W {ECO:0000313|EMBL:AAF57509.1}, CT25100 {ECO:0000313|EMBL:AAF57509.1}, Dmel\CG8896 {ECO:0000313|EMBL:AAF57509.1}, EP-709 {ECO:0000313|EMBL:AAF57509.1}, l(2)00053 {ECO:0000313|EMBL:AAF57509.1}, tlr {ECO:0000313|EMBL:AAF57509.1}, toll {ECO:0000313|EMBL:AAF57509.1}, Toll-2 {ECO:0000313|EMBL:AAF57509.1}, toll-2 {ECO:0000313|EMBL:AAF57509.1}, Toll2 {ECO:0000313|EMBL:AAF57509.1}; ORFNames=CG8896 {ECO:0000313|EMBL:AAF57509.1, ECO:0000313|FlyBase:FBgn0287775}, Dmel_CG8896 {ECO:0000313|EMBL:AAF57509.1};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Belongs to the Toll-like receptor family.
- **Key Domains:** Cys-rich_flank_reg_C. (IPR000483); Leu-rich_rpt. (IPR001611); Leu-rich_rpt_typical-subtyp. (IPR003591); LRR_5. (IPR026906); LRR_dom_sf. (IPR032675)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "18w" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol '18w' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **18w** (gene ID: 18w, UniProt: A1ZBR2) in DROME.

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
- **UniProt Accession:** A1ZBR2
- **Protein Description:** SubName: Full=18 wheeler {ECO:0000313|EMBL:AAF57509.1};
- **Gene Information:** Name=18w {ECO:0000313|EMBL:AAF57509.1, ECO:0000313|FlyBase:FBgn0287775}; Synonyms=18-w {ECO:0000313|EMBL:AAF57509.1}, 18-wheeler {ECO:0000313|EMBL:AAF57509.1}, 18W {ECO:0000313|EMBL:AAF57509.1}, CT25100 {ECO:0000313|EMBL:AAF57509.1}, Dmel\CG8896 {ECO:0000313|EMBL:AAF57509.1}, EP-709 {ECO:0000313|EMBL:AAF57509.1}, l(2)00053 {ECO:0000313|EMBL:AAF57509.1}, tlr {ECO:0000313|EMBL:AAF57509.1}, toll {ECO:0000313|EMBL:AAF57509.1}, Toll-2 {ECO:0000313|EMBL:AAF57509.1}, toll-2 {ECO:0000313|EMBL:AAF57509.1}, Toll2 {ECO:0000313|EMBL:AAF57509.1}; ORFNames=CG8896 {ECO:0000313|EMBL:AAF57509.1, ECO:0000313|FlyBase:FBgn0287775}, Dmel_CG8896 {ECO:0000313|EMBL:AAF57509.1};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Belongs to the Toll-like receptor family.
- **Key Domains:** Cys-rich_flank_reg_C. (IPR000483); Leu-rich_rpt. (IPR001611); Leu-rich_rpt_typical-subtyp. (IPR003591); LRR_5. (IPR026906); LRR_dom_sf. (IPR032675)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "18w" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol '18w' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **18w** (gene ID: 18w, UniProt: A1ZBR2) in DROME.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Comprehensive Research Report: Gene 18w (18-wheeler/Toll-2) in Drosophila melanogaster

## Gene Identity Verification

The gene 18w (UniProt: A1ZBR2) encodes the protein 18-wheeler, also known as Toll-2, a member of the Toll-like receptor family in *Drosophila melanogaster*. This identification is confirmed across the literature, with consistent use of the synonyms 18w, 18-wheeler, and Toll-2 to refer to the same gene product (umetsu2022cellmechanicsand pages 7-8, pare2014apositionaltoll pages 1-2, kambris2002tissueandstagespecific pages 4-6).

## Protein Structure and Subcellular Localization

> **Identity and architecture:** *Drosophila melanogaster* 18-wheeler (18w), also called Toll-2, is a single-pass Toll-family receptor. Its inferred topology comprises an extracellular leucine-rich-repeat (LRR) recognition/interaction region with cysteine-rich flanks, one transmembrane helix, and a cytoplasmic Toll/interleukin-1 receptor (TIR) domain. The intact receptor is therefore expected at the plasma membrane, whereas an experimentally studied truncation lacking its extracellular and transmembrane regions becomes cytoplasmic. (ligoxygakis2002criticalevaluationof pages 3-4, amanda2016drosophilamidlinedevelopment pages 19-25)
>
> **Src-responsive signaling platform:** Toll-2 has two C-terminal tyrosine clusters outside the conserved TIR core. Src42A and Src64B phosphorylate these sites, producing phosphotyrosine docking sites recognized by the SH2 domains of the PI3K regulatory subunit. The resulting spatially restricted Toll-2–PI3K complex controls Myosin-II and Par-3 planar polarity, cell intercalation, and convergent extension; Toll-2 is therefore not itself a kinase. (tamada2021tollreceptorsremodel pages 7-9, tamada2021tollreceptorsremodel pages 2-4, tamada2021tollreceptorsremodel pages 9-10, tamada2021tollreceptorsremodel pages 6-7)
>
> **Ligand evidence:** DNT-2, also called Spätzle-5, is a secreted, proteolytically processed neurotrophin-like ligand that functions genetically through Toll-2 in the developing visual system. DNT-2 overexpression reduces neuronal apoptosis, but this rescue is blocked by Toll-2 knockdown; DNT-2 loss eliminates Toll-2-positive neurons and disrupts connectivity. This is strong functional evidence for a DNT-2→Toll-2 pathway, although direct biochemical binding has not yet been demonstrated and the key report is a 2025 preprint. (alshamsi2025theneurotrophindnt2 pages 8-11, alshamsi2025theneurotrophindnt2 pages 1-4, alshamsi2025theneurotrophindnt2 pages 14-17)
>
> **Context-dependent signaling modes:** Toll-2 can engage distinct outputs rather than one universal linear pathway. MyD88-associated signaling supports neuronal survival and can maintain adult progenitor quiescence; an alternative Weckle-dependent branch activates Yorkie and cell-cycle entry; and, during epithelial morphogenesis, the Src→phospho-Toll-2→PI3K branch polarizes cortical mechanics. The canonical MyD88–Tube–Pelle–Cactus–Dif/Dorsal cascade is well established for *Drosophila* Toll signaling generally, but should not automatically be assigned to every Toll-2 function without tissue-specific evidence. (lindsay2014conventionalandnonconventional pages 15-19, li2020atollreceptormap pages 20-22, li2020atollreceptormap pages 16-18, tamada2021tollreceptorsremodel pages 4-6)


*Blockquote: Key structural features, localization, candidate ligand, and context-dependent signaling mechanisms of Drosophila 18-wheeler/Toll-2, with distinctions between direct evidence and pathway-level inference.*

18-wheeler is a single-pass transmembrane receptor with a domain architecture characteristic of the Toll-like receptor family (amanda2016drosophilamidlinedevelopment pages 19-25). The protein comprises an extracellular leucine-rich repeat (LRR) domain flanked by cysteine-rich regions, a single transmembrane helix, and a cytoplasmic Toll/interleukin-1 receptor (TIR) domain (ligoxygakis2002criticalevaluationof pages 3-4, amanda2016drosophilamidlinedevelopment pages 19-25). This architecture positions the receptor at the plasma membrane, where the LRR domain mediates extracellular recognition or adhesion events, and the TIR domain transduces signals intracellularly (amanda2016drosophilamidlinedevelopment pages 19-25).

Critical evidence for membrane localization comes from studies of the 18w7-35 mutant allele, which produces an N-terminally truncated protein lacking the extracellular and transmembrane domains. This truncated product, consisting primarily of the TIR domain, localizes to the cytoplasm rather than the membrane, demonstrating that the full-length wild-type receptor requires its transmembrane domain for proper membrane targeting (ligoxygakis2002criticalevaluationof pages 3-4).

Notably, Toll-2 contains two C-terminal tyrosine clusters (C1 and C2) located outside the conserved TIR core domain. These clusters serve as Src-dependent phosphorylation sites essential for recruiting downstream signaling effectors, particularly the PI3K regulatory subunit (tamada2021tollreceptorsremodel pages 7-9, tamada2021tollreceptorsremodel pages 2-4).

## Primary Molecular Function

Unlike enzymes with defined substrate specificity, 18-wheeler functions as a transmembrane receptor involved in cell recognition, adhesion, and signal transduction. The protein does not possess intrinsic catalytic activity; rather, it acts as a platform for assembling context-dependent signaling complexes (tamada2021tollreceptorsremodel pages 4-6, tamada2021tollreceptorsremodel pages 7-9).

### Receptor-Ligand Interaction

Recent work has identified DNT-2 (also called Spätzle-5 or spz-5) as a neurotrophin-like ligand that functions genetically through Toll-2 during visual-system development (alshamsi2025theneurotrophindnt2 pages 8-11, alshamsi2025theneurotrophindnt2 pages 4-8, alshamsi2025theneurotrophindnt2 pages 1-4). DNT-2 is a secreted protein processed into an active form through proteolytic cleavage, similar to other Spätzle-family ligands (alshamsi2025theneurotrophindnt2 pages 14-17, lindsay2014conventionalandnonconventional pages 1-2). In the developing optic lobe, DNT-2 is expressed in Mi1 medulla neurons, while Toll-2 is expressed in connecting L1 lamina neurons (alshamsi2025theneurotrophindnt2 pages 4-8, alshamsi2025theneurotrophindnt2 pages 11-14). Genetic evidence strongly supports this ligand-receptor relationship: DNT-2 overexpression rescues naturally occurring cell death, but this rescue is completely blocked by Toll-2 knockdown; conversely, DNT-2 mutants lose Toll-2-positive neurons (alshamsi2025theneurotrophindnt2 pages 8-11, alshamsi2025theneurotrophindnt2 pages 1-4). While this genetic evidence is compelling, direct biochemical demonstration of DNT-2 binding to Toll-2 has not yet been reported, and the key study is a 2025 preprint (alshamsi2025theneurotrophindnt2 pages 14-17).

Earlier work proposed that 18-wheeler might function as a pattern-recognition receptor for Gram-negative bacteria, but this hypothesis has been thoroughly refuted. Careful genetic analysis demonstrated that 18-wheeler is not required for adult antimicrobial responses and does not function as a selective bacterial sensor (ligoxygakis2002criticalevaluationof pages 1-3).

## Signaling Pathways

18-wheeler engages multiple, context-dependent signaling mechanisms rather than a single linear pathway. The choice of pathway appears to depend on tissue type, developmental stage, and cellular context.

### Embryonic Morphogenesis: Src/PI3K Pathway

During embryonic germband elongation and convergent extension, Toll-2 functions as part of a striped positional code together with Toll-6 and Toll-8 (pare2014apositionaltoll pages 1-2, pare2014apositionaltoll pages 2-2, umetsu2022cellmechanicsand pages 5-7). In this context, Toll-2 activates a non-canonical, kinase-dependent pathway independent of traditional Toll/NF-κB signaling:

1. **Src kinase recruitment and phosphorylation**: Src-family kinases Src42A and Src64B associate with Toll-2 at cell-cell contacts and phosphorylate the C-terminal tyrosine clusters (tamada2021tollreceptorsremodel pages 7-9, tamada2021tollreceptorsremodel pages 4-6, tamada2021tollreceptorsremodel pages 2-4). This phosphorylation is functionally critical—mutations preventing phosphorylation of these tyrosines abolish Toll-2 function in convergent extension (tamada2021tollreceptorsremodel pages 7-9).

2. **PI3K recruitment**: The phosphorylated tyrosines create docking sites recognized by the SH2 domains of the PI3K regulatory subunit (PI3K-reg), concentrating PI3K activity at specific membrane domains (tamada2021tollreceptorsremodel pages 7-9, tamada2021tollreceptorsremodel pages 9-10, tamada2021tollreceptorsremodel pages 6-7). The TIR domain is dispensable for this interaction; only the C-terminal phosphotyrosines are required (tamada2021tollreceptorsremodel pages 6-7).

3. **Planar polarity establishment**: The localized Toll-2/PI3K complex promotes planar-polarized accumulation of Myosin-II at anterior-posterior cell interfaces and Par-3 redistribution, driving oriented cell intercalation and tissue elongation (tamada2021tollreceptorsremodel pages 4-6, tamada2021tollreceptorsremodel pages 7-9, kuebler2023stripedexpressionof pages 7-10).

Loss of Src42A and Src64B together severely disrupts planar polarity, Myosin-II localization, cell intercalation, and axis elongation, phenocopying Toll receptor defects (tamada2021tollreceptorsremodel pages 4-6, kuebler2023stripedexpressionof pages 6-7).

### Brain Development and Plasticity: MyD88 vs. Weckle/Yorkie Pathways

In the nervous system, Toll-2 regulates neuronal survival, progenitor proliferation, and experience-dependent structural plasticity through alternative downstream adaptors (li2020atollreceptormap pages 18-20, li2021thetollroute pages 6-7, li2020atollreceptormap pages 20-22).

**MyD88-dependent pathway**: MyD88 signaling maintains adult neural progenitor cells in a quiescent state, preventing inappropriate proliferation (li2020atollreceptormap pages 16-18, li2020atollreceptormap pages 14-16). Toll-2 is required for neuronal survival during development, as Toll-2 loss causes apoptosis, neurite atrophy, and behavioral impairment (li2020atollreceptormap pages 20-22, li2020atollreceptormap pages 7-10).

**Weckle/Yorkie pathway**: Toll-2 can antagonize MyD88-mediated quiescence by signaling through the adaptor Weckle (Wek), which promotes nuclear translocation of Yorkie (Yki), a transcriptional coactivator that drives cell-cycle gene expression (li2020atollreceptormap pages 16-18, li2020atollreceptormap pages 14-16). Toll-2 overexpression increases cell numbers in G1, S, and G2/M phases, and this effect requires both Wek and Yki—knockdown of either blocks the Toll-2-induced proliferation (li2020atollreceptormap pages 16-18). Neuronal activity during an early-adult critical period increases optic-lobe cell number in a Toll-2-dependent manner, linking experience to structural brain changes (li2020atollreceptormap pages 18-20, li2020atollreceptormap pages 7-10, li2020atollreceptormap pages 1-2).

### Visual System Development: Neurotrophic Signaling

As described above, DNT-2 functions through Toll-2 to promote survival of lamina neurons during the wave of naturally occurring cell death in pupal optic-lobe development (alshamsi2025theneurotrophindnt2 pages 8-11, alshamsi2025theneurotrophindnt2 pages 1-4). Beyond survival, the DNT-2/Toll-2 pathway regulates L1 axon targeting to the M1 medulla layer and controls dendritic complexity and morphology (alshamsi2025theneurotrophindnt2 pages 11-14, alshamsi2025theneurotrophindnt2 pages 14-17, alshamsi2025theneurotrophindnt2 pages 17-20). Altering either DNT-2 or Toll-2 levels disrupts connectivity, suggesting that appropriately scaled neurotrophic signaling is required for circuit assembly (alshamsi2025theneurotrophindnt2 pages 11-14).

### Canonical Toll/NF-κB Pathway

While canonical Toll signaling through MyD88, Tube, Pelle, Cactus, and the NF-κB-like factors Dif/Dorsal is well established for *Drosophila* Toll-1 in immunity and dorsoventral patterning (sisquella2022decipheringtherole pages 33-36, amanda2016drosophilamidlinedevelopment pages 15-19, lindsay2014conventionalandnonconventional pages 15-19, lindsay2014conventionalandnonconventional pages 1-2), the extent to which Toll-2 uses this pathway varies by tissue and context. Adult 18w mutants show normal DIF nuclear translocation and antimicrobial peptide expression after bacterial challenge, indicating that this canonical pathway can function without Toll-2 in adults (ligoxygakis2002criticalevaluationof pages 3-4, ligoxygakis2002criticalevaluationof pages 1-3).

## Biological Processes and Tissue-Specific Functions

| Biological Process | Molecular Function | Tissue/Cell Type | Developmental Stage/Context | Key References |
|---|---|---|---|---|
| Embryonic convergent extension and morphogenesis | Toll-2 acts with Toll-6 and Toll-8 as a striped positional code specifying heterotypic cell interfaces and planar polarity. Src42A/Src64B phosphorylate C-terminal tyrosines in Toll-2, creating docking sites for PI3K-reg; localized PI3K signaling promotes polarized Myosin-II accumulation, Par-3 redistribution, junction contraction, cell intercalation, and axis elongation. | Germband neuroectoderm and epidermal epithelial cells, especially boundaries between Toll-expression stripes | Early embryogenesis during germband extension and convergent extension | Paré et al., *Nature* (2014), [DOI](https://doi.org/10.1038/nature13953); Tamada et al., *Developmental Cell* (2021), [DOI](https://doi.org/10.1016/j.devcel.2021.04.012); Umetsu, *Fly* (2022), [DOI](https://doi.org/10.1080/19336934.2022.2074783) (umetsu2022cellmechanicsand pages 7-8, pare2014apositionaltoll pages 1-2, umetsu2022cellmechanicsand pages 5-7, tamada2021tollreceptorsremodel pages 7-9, tamada2021tollreceptorsremodel pages 6-7) |
| Brain development and structural plasticity | Toll-2 supports neuronal survival and neurite integrity and regulates progenitor state through alternative adaptor branches. MyD88 favors progenitor quiescence, whereas Toll-2–Weckle signaling promotes Yorkie-dependent cell-cycle entry. Neural activity during an early-adult critical period increases cell number in a Toll-2-dependent manner. | Predominantly neurons and adult progenitor cells in optic lobes, mushroom bodies, antennal lobes, central complex, subesophageal ganglion, and central brain | Embryonic through pupal nervous-system development; early-adult critical period and adult structural plasticity | Li et al., *eLife* (2020), [DOI](https://doi.org/10.7554/eLife.52743); Li and Hidalgo, *Frontiers in Physiology* (2021), [DOI](https://doi.org/10.3389/fphys.2021.679766) (li2020atollreceptormap pages 18-20, li2021thetollroute pages 6-7, li2020atollreceptormap pages 20-22, li2020atollreceptormap pages 7-10, li2020atollreceptormap pages 16-18, li2020atollreceptormap pages 14-16) |
| Visual-system development | Secreted DNT-2/Spätzle-5 functions genetically with Toll-2 as a neurotrophic ligand–receptor pathway. DNT-2 promotes survival of Toll-2-positive neurons and regulates L1 axon targeting, dendritic morphology, and connectivity. Toll-2 knockdown blocks rescue by DNT-2 overexpression, although direct biochemical binding remains unproven. | DNT-2-producing Mi1 and other medulla neurons; Toll-2-positive L1/L3 lamina neurons and medulla neurons | Pupal optic-lobe development during naturally occurring neuronal death and circuit assembly | Alshamsi et al., bioRxiv (18 July 2025), [DOI](https://doi.org/10.1101/2025.07.18.665476) (alshamsi2025theneurotrophindnt2 pages 8-11, alshamsi2025theneurotrophindnt2 pages 4-8, alshamsi2025theneurotrophindnt2 pages 1-4, alshamsi2025theneurotrophindnt2 pages 11-14, alshamsi2025theneurotrophindnt2 pages 14-17) |
| Follicle-cell migration during oogenesis | Toll-2 has a proposed adhesion and/or signaling role in coordinated epithelial-sheet migration. Loss of function delays posterior and centripetal follicle-cell movement and alters egg shape and dorsal-appendage morphology; the immediate intracellular pathway remains unresolved. | Somatic follicle-cell epithelium, including posteriorly and centripetally migrating cells, stalk cells, and eggshell-secreting populations | Oogenesis, principally egg-chamber stages 8–13 | Kleve et al., *Developmental Dynamics* (2006), [DOI](https://doi.org/10.1002/dvdy.20820) (kleve2006expressionof18‐wheeler pages 1-3, kleve2006expressionof18‐wheeler pages 4-5) |
| Salivary-gland development | Toll-2 regulates Rho-GTPase-dependent apical constriction, affecting phosphorylated Spaghetti squash, invagination timing, gland positioning, and coordinated cell migration. Its upstream ligand and receptor-coupling mechanism in this tissue remain unknown. | Embryonic salivary-gland placode and invaginating epithelial cells | Embryonic salivary-gland tubulogenesis | Kolesnikov and Beckendorf, *Developmental Biology* (2007), [DOI](https://doi.org/10.1016/j.ydbio.2007.04.014); summarized by Moawad (2016), [DOI](https://doi.org/10.17615/qzh4-et78) (amanda2016drosophilamidlinedevelopment pages 19-25, amanda2016drosophilamidlinedevelopment pages 39-43) |
| Larval fat-body maturation | Toll-2 is required for normal fat-body maturation and full antimicrobial-peptide inducibility. Mutants show reduced *attacin*, *diptericin*, and *Drosomycin* expression and loss of the maturation marker *Fbp1*, while retaining immune-induced DIF nuclear translocation. The immune phenotype is therefore best interpreted as secondary to defective tissue development rather than direct microbial recognition. | Larval fat body; transcripts are also detected in larval blood cells and lymph gland | Late larval development and systemic immune challenge; adult systemic immunity is largely Toll-2-independent | Ligoxygakis et al., *EMBO Reports* (2002), [DOI](https://doi.org/10.1093/embo-reports/kvf130); Kambris et al., *Gene Expression Patterns* (2002), [DOI](https://doi.org/10.1016/S1567-133X(02)00020-0) (ligoxygakis2002criticalevaluationof pages 1-3, ligoxygakis2002criticalevaluationof pages 4-6, ligoxygakis2002criticalevaluationof pages 3-4, kambris2002tissueandstagespecific pages 4-6) |
| Tracheal/airway epithelium development | Toll-2 is highly expressed in tracheal epithelium, but no Toll-2-specific developmental or immune mechanism has been established. Canonical Toll signaling appears incomplete or inoperative there, and inducible antimicrobial defense primarily uses IMD–Relish signaling; Toll-8 findings must not be assigned to Toll-2. | Tracheal airway epithelial cells | Larval or adult airway epithelium and epithelial immune-response contexts | Wagner et al., *BMC Genomics* (2008), [DOI](https://doi.org/10.1186/1471-2164-9-446); Ehrhardt et al., *Frontiers in Allergy* (2022), [DOI](https://doi.org/10.3389/falgy.2022.876673) (ehrhardt2022airwayremodelingthe pages 5-6) |


*Table: This table summarizes the tissue-specific functions, molecular mechanisms, and developmental contexts of Drosophila 18-wheeler/Toll-2. It distinguishes experimentally supported pathways from proposed or unresolved roles.*

18-wheeler participates in a remarkably diverse array of developmental processes, with tissue-specific roles spanning embryogenesis through adult life:

### Embryonic Convergent Extension

During early embryogenesis, 18w is expressed in transverse stripes regulated by pair-rule transcription factors Eve and Runt (pare2014apositionaltoll pages 1-2, kambris2002tissueandstagespecific pages 2-3). Together with Toll-6 and Toll-8, these striped expression patterns form a "Toll code" that specifies planar polarity and directs convergent extension—a process involving coordinated cell intercalation that narrows tissue along one axis and elongates it perpendicular to that axis (umetsu2022cellmechanicsand pages 7-8, pare2014apositionaltoll pages 2-2, umetsu2022cellmechanicsand pages 5-7). Loss of all three receptors reduces germband elongation by approximately 40%, while loss of Toll-2 alone produces intermediate defects (pare2014apositionaltoll pages 2-2).

### Midline Development

18w is expressed in the posterior portion of each embryonic segment within the ventral midline, particularly in the median neuroblast (MNB), where it may guide cell migration and positioning (amanda2016drosophilamidlinedevelopment pages 25-29). Expression persists from early through late embryogenesis, with higher levels during earlier stages when midline neurons are differentiating (amanda2016drosophilamidlinedevelopment pages 25-29).

### Salivary Gland Morphogenesis

In the embryonic salivary gland, 18-wheeler regulates apical constriction and invagination timing through activation of the Rho-GTPase pathway, including increased phosphorylation of the myosin regulatory light chain Spaghetti squash (amanda2016drosophilamidlinedevelopment pages 19-25). Loss of 18w disrupts coordinated cell migration and gland positioning (amanda2016drosophilamidlinedevelopment pages 39-43).

### Follicle Cell Migration and Oogenesis

During oogenesis, 18w is expressed in specific follicle-cell subpopulations undergoing posterior and centripetal migration (kleve2006expressionof18‐wheeler pages 1-3). Loss-of-function clones delay migration and produce eggs with abnormal shape, posteriorly shifted dorsal appendages, and reduced or absent dorsal-appendage paddles (kleve2006expressionof18‐wheeler pages 1-3, kleve2006expressionof18‐wheeler pages 4-5). This suggests roles in both epithelial migration and eggshell patterning (kleve2006expressionof18‐wheeler pages 9-9).

### Larval Fat Body Maturation

In larvae, 18-wheeler is required for normal fat-body development and maturation (ligoxygakis2002criticalevaluationof pages 1-3, ligoxygakis2002criticalevaluationof pages 4-6). Mutant larvae show developmental delay, reduced expression of the maturation marker Fbp1, and broadly compromised antimicrobial peptide induction after immune challenge (ligoxygakis2002criticalevaluationof pages 4-6, ligoxygakis2002criticalevaluationof pages 3-4). Importantly, this immune defect appears secondary to impaired tissue development rather than reflecting a direct role in pathogen recognition (ligoxygakis2002criticalevaluationof pages 1-3).

### Tracheal Expression

18-wheeler transcripts are highly expressed in the tracheal airway epithelium (ehrhardt2022airwayremodelingthe pages 5-6, kambris2002tissueandstagespecific pages 4-6), although its specific function there remains undefined. Canonical Toll signaling appears incomplete or inoperative in the trachea, where epithelial immunity primarily depends on the IMD pathway (ehrhardt2022airwayremodelingthe pages 5-6).

## Evolutionary and Structural Context

18-wheeler belongs to the Toll-like receptor family, which is conserved across metazoans and plays critical roles in both immunity and development (ligoxygakis2002criticalevaluationof pages 1-3). *Drosophila* has nine Toll-family genes; 18-wheeler is one of the "long" Tolls with extensive LRR regions (kambris2002tissueandstagespecific pages 4-6, kambris2002tissueandstagespecific pages 1-2). Phylogenetic analyses place 18w/Toll-2 in a clade with Toll-7, and the two genes show overlapping expression patterns despite differential regulation (kambris2002tissueandstagespecific pages 4-6).

The leucine-rich repeat domain is a widespread protein-interaction motif that provides a framework for specific protein-protein recognition (amanda2016drosophilamidlinedevelopment pages 19-25). In the case of 18-wheeler, LRRs likely mediate heterophilic interactions with other Toll receptors (such as Toll-6 and Toll-8) at cell boundaries, creating recognition codes that specify interface identity and polarity (umetsu2022cellmechanicsand pages 7-8, umetsu2022cellmechanicsand pages 5-7).

## Expression Patterns

18-wheeler expression is dynamic and tissue-specific:

- **Early embryo**: Expressed in eight circular bands at the cellular blastoderm stage, positioned posterior to even-skipped stripes (kambris2002tissueandstagespecific pages 2-3, kambris2002tissueandstagespecific pages 3-4). Expression begins zygotically with no maternal contribution (kambris2002tissueandstagespecific pages 3-4).

- **Germband extension**: Expression overlaps wingless stripes and extends posteriorly (kambris2002tissueandstagespecific pages 2-3).

- **Brain**: Broadly expressed in optic lobes, mushroom body Kenyon cells, antennal lobes, central complex (fan-shaped body and ellipsoid body), and subesophageal ganglion (li2020atollreceptormap pages 3-5, li2020atollreceptormap pages 2-3). Expression is predominantly neuronal rather than glial (li2020atollreceptormap pages 3-5).

- **Larval immune tissues**: Detected by RT-PCR in blood cells, fat body, and lymph gland (kambris2002tissueandstagespecific pages 4-6).

- **Ovary**: Restricted to specific follicle-cell populations, including migrating cells and stalk cells (kleve2006expressionof18‐wheeler pages 1-3, amanda2016drosophilamidlinedevelopment pages 19-25).

## Recent Developments (2020-2025)

The most significant recent advances in understanding 18-wheeler function have come from three lines of investigation:

1. **Non-canonical Src/PI3K signaling** (2021): Tamada et al. demonstrated that Toll-2 recruits PI3K through Src-dependent tyrosine phosphorylation, revealing a kinase-based mechanism independent of traditional Toll/NF-κB signaling (tamada2021tollreceptorsremodel pages 7-9). This work established how Toll receptors can directly control cytoskeletal mechanics.

2. **Brain structural plasticity** (2020-2021): Li, Hidalgo, and colleagues showed that Toll-2 regulates experience-dependent neurogenesis in the adult brain through Weckle/Yorkie signaling, linking neuronal activity to lasting anatomical changes (li2020atollreceptormap pages 18-20, li2021thetollroute pages 6-7). This revealed an unexpected role for Toll receptors in neural circuit remodeling.

3. **Neurotrophic ligand identification** (2025): Alshamsi et al. identified DNT-2/Spätzle-5 as a functional ligand for Toll-2 during visual-system development, providing the first clear ligand-receptor pairing for 18-wheeler in a specific developmental context (alshamsi2025theneurotrophindnt2 pages 8-11, alshamsi2025theneurotrophindnt2 pages 1-4). This preprint establishes a neurotrophic function analogous to vertebrate neurotrophin signaling.

## Experimental Evidence

Understanding of 18-wheeler function derives from multiple experimental approaches:

- **Genetic loss-of-function**: Studies using the 18w7-35 deletion allele and deficiency chromosomes established developmental requirements and tissue-specific phenotypes (ligoxygakis2002criticalevaluationof pages 1-3, ligoxygakis2002criticalevaluationof pages 3-4).

- **Gain-of-function**: Overexpression experiments demonstrated increased cell proliferation, altered tissue size, and effects on migration and morphology (li2020atollreceptormap pages 18-20, kleve2006expressionof18‐wheeler pages 1-3).

- **RNAi knockdown**: Tissue-specific and temporal knockdown experiments dissected stage-specific requirements and identified genetic interactions (li2020atollreceptormap pages 7-10, alshamsi2025theneurotrophindnt2 pages 1-4).

- **Phosphorylation analysis**: Mass spectrometry and phospho-specific antibodies identified Src-dependent tyrosine phosphorylation sites (tamada2021tollreceptorsremodel pages 7-9, tamada2021tollreceptorsremodel pages 2-4).

- **Rescue experiments**: Epistasis tests with downstream pathway components (Src kinases, PI3K, Wek, Yki) established signaling hierarchies (li2020atollreceptormap pages 16-18, tamada2021tollreceptorsremodel pages 7-9).

- **Protein truncation**: Analysis of the 18w7-35 truncation product established membrane localization requirements and TIR domain function (ligoxygakis2002criticalevaluationof pages 3-4).

## Summary

18-wheeler/Toll-2 is a multifunctional transmembrane receptor that serves as a versatile signaling platform in *Drosophila melanogaster*. Rather than functioning as an enzyme with defined substrate specificity, it acts as a cell-surface receptor that coordinates diverse developmental processes through context-dependent signaling mechanisms. Its primary molecular functions include: (1) establishing spatial positional codes during embryonic morphogenesis via Src/PI3K-dependent planar polarity signaling; (2) regulating neuronal survival, proliferation, and experience-dependent plasticity through alternative MyD88 and Weckle/Yorkie pathways; and (3) mediating neurotrophic signaling in response to the secreted ligand DNT-2/Spätzle-5 during visual-system development.

The protein localizes to the plasma membrane, where its extracellular LRR domain mediates recognition and adhesion, while its cytoplasmic TIR and C-terminal domains recruit different adaptor proteins and signaling effectors depending on cellular context. This remarkable versatility—using the same receptor architecture to control morphogenesis, neurogenesis, and neural circuit assembly—illustrates how evolution has repurposed Toll-family receptors beyond their ancestral roles in immunity to orchestrate complex developmental programs.

References

1. (umetsu2022cellmechanicsand pages 7-8): Daiki Umetsu. Cell mechanics and cell-cell recognition controls by toll-like receptors in tissue morphogenesis and homeostasis. Fly, 16:233-247, May 2022. URL: https://doi.org/10.1080/19336934.2022.2074783, doi:10.1080/19336934.2022.2074783. This article has 23 citations and is from a peer-reviewed journal.

2. (pare2014apositionaltoll pages 1-2): Adam C. Paré, Athea Vichas, Christopher T. Fincher, Zachary Mirman, Dene L. Farrell, Avantika Mainieri, and Jennifer A. Zallen. A positional toll receptor code directs convergent extension in drosophila. Nature, 515:523-527, Nov 2014. URL: https://doi.org/10.1038/nature13953, doi:10.1038/nature13953. This article has 310 citations and is from a highest quality peer-reviewed journal.

3. (kambris2002tissueandstagespecific pages 4-6): Zakaria Kambris, Jules A. Hoffmann, Jean-Luc Imler, and Maria Capovilla. Tissue and stage-specific expression of the tolls in drosophila embryos. Gene expression patterns : GEP, 2 3-4:311-7, Dec 2002. URL: https://doi.org/10.1016/s1567-133x(02)00020-0, doi:10.1016/s1567-133x(02)00020-0. This article has 118 citations.

4. (ligoxygakis2002criticalevaluationof pages 3-4): Petros Ligoxygakis, Philippe Bulet, and Jean‐Marc Reichhart. Critical evaluation of the role of the toll‐like receptor 18‐wheeler in the host defense of drosophila. EMBO reports, 3:666-673, Jul 2002. URL: https://doi.org/10.1093/embo-reports/kvf130, doi:10.1093/embo-reports/kvf130. This article has 95 citations and is from a highest quality peer-reviewed journal.

5. (amanda2016drosophilamidlinedevelopment pages 19-25): Amanda Moawad. Drosophila midline development: the role of 18-wheeler and an optimized protocol for transcriptome analysis. Text, 2016. URL: https://doi.org/10.17615/qzh4-et78, doi:10.17615/qzh4-et78. This article has 0 citations and is from a peer-reviewed journal.

6. (tamada2021tollreceptorsremodel pages 7-9): Masako Tamada, Jay Shi, Kia S. Bourdot, Sara Supriyatno, Karl H. Palmquist, Omar L. Gutierrez-Ruiz, and Jennifer A. Zallen. Toll receptors remodel epithelia by directing planar-polarized src and pi3k activity. Developmental Cell, 56:1589-1602.e9, Jun 2021. URL: https://doi.org/10.1016/j.devcel.2021.04.012, doi:10.1016/j.devcel.2021.04.012. This article has 44 citations and is from a highest quality peer-reviewed journal.

7. (tamada2021tollreceptorsremodel pages 2-4): Masako Tamada, Jay Shi, Kia S. Bourdot, Sara Supriyatno, Karl H. Palmquist, Omar L. Gutierrez-Ruiz, and Jennifer A. Zallen. Toll receptors remodel epithelia by directing planar-polarized src and pi3k activity. Developmental Cell, 56:1589-1602.e9, Jun 2021. URL: https://doi.org/10.1016/j.devcel.2021.04.012, doi:10.1016/j.devcel.2021.04.012. This article has 44 citations and is from a highest quality peer-reviewed journal.

8. (tamada2021tollreceptorsremodel pages 9-10): Masako Tamada, Jay Shi, Kia S. Bourdot, Sara Supriyatno, Karl H. Palmquist, Omar L. Gutierrez-Ruiz, and Jennifer A. Zallen. Toll receptors remodel epithelia by directing planar-polarized src and pi3k activity. Developmental Cell, 56:1589-1602.e9, Jun 2021. URL: https://doi.org/10.1016/j.devcel.2021.04.012, doi:10.1016/j.devcel.2021.04.012. This article has 44 citations and is from a highest quality peer-reviewed journal.

9. (tamada2021tollreceptorsremodel pages 6-7): Masako Tamada, Jay Shi, Kia S. Bourdot, Sara Supriyatno, Karl H. Palmquist, Omar L. Gutierrez-Ruiz, and Jennifer A. Zallen. Toll receptors remodel epithelia by directing planar-polarized src and pi3k activity. Developmental Cell, 56:1589-1602.e9, Jun 2021. URL: https://doi.org/10.1016/j.devcel.2021.04.012, doi:10.1016/j.devcel.2021.04.012. This article has 44 citations and is from a highest quality peer-reviewed journal.

10. (alshamsi2025theneurotrophindnt2 pages 8-11): Naser Alshamsi, Francisca Rojo-Cortés, Bangfu Zhu, Samaher Fahy, Guiyi Li, Anna Lassota, Marta Moreira, and Alicia Hidalgo. The neurotrophin dnt-2 regulates cell survival and connectivity via the toll-2 receptor during visual system development of <i>drosophila</i>. BioRxiv, Jul 2025. URL: https://doi.org/10.1101/2025.07.18.665476, doi:10.1101/2025.07.18.665476. This article has 0 citations.

11. (alshamsi2025theneurotrophindnt2 pages 1-4): Naser Alshamsi, Francisca Rojo-Cortés, Bangfu Zhu, Samaher Fahy, Guiyi Li, Anna Lassota, Marta Moreira, and Alicia Hidalgo. The neurotrophin dnt-2 regulates cell survival and connectivity via the toll-2 receptor during visual system development of <i>drosophila</i>. BioRxiv, Jul 2025. URL: https://doi.org/10.1101/2025.07.18.665476, doi:10.1101/2025.07.18.665476. This article has 0 citations.

12. (alshamsi2025theneurotrophindnt2 pages 14-17): Naser Alshamsi, Francisca Rojo-Cortés, Bangfu Zhu, Samaher Fahy, Guiyi Li, Anna Lassota, Marta Moreira, and Alicia Hidalgo. The neurotrophin dnt-2 regulates cell survival and connectivity via the toll-2 receptor during visual system development of <i>drosophila</i>. BioRxiv, Jul 2025. URL: https://doi.org/10.1101/2025.07.18.665476, doi:10.1101/2025.07.18.665476. This article has 0 citations.

13. (lindsay2014conventionalandnonconventional pages 15-19): Scott A. Lindsay and Steven A. Wasserman. Conventional and non-conventional drosophila toll signaling. Developmental and comparative immunology, 42 1:16-24, Jan 2014. URL: https://doi.org/10.1016/j.dci.2013.04.011, doi:10.1016/j.dci.2013.04.011. This article has 201 citations and is from a peer-reviewed journal.

14. (li2020atollreceptormap pages 20-22): Guiyi Li, Manuel G Forero, Jill S Wentzell, Ilgim Durmus, Reinhard Wolf, Niki C Anthoney, Mieczyslaw Parker, Ruiying Jiang, Jacob Hasenauer, Nicholas James Strausfeld, Martin Heisenberg, and Alicia Hidalgo. A toll-receptor map underlies structural brain plasticity. eLife, Feb 2020. URL: https://doi.org/10.7554/elife.52743, doi:10.7554/elife.52743. This article has 65 citations and is from a domain leading peer-reviewed journal.

15. (li2020atollreceptormap pages 16-18): Guiyi Li, Manuel G Forero, Jill S Wentzell, Ilgim Durmus, Reinhard Wolf, Niki C Anthoney, Mieczyslaw Parker, Ruiying Jiang, Jacob Hasenauer, Nicholas James Strausfeld, Martin Heisenberg, and Alicia Hidalgo. A toll-receptor map underlies structural brain plasticity. eLife, Feb 2020. URL: https://doi.org/10.7554/elife.52743, doi:10.7554/elife.52743. This article has 65 citations and is from a domain leading peer-reviewed journal.

16. (tamada2021tollreceptorsremodel pages 4-6): Masako Tamada, Jay Shi, Kia S. Bourdot, Sara Supriyatno, Karl H. Palmquist, Omar L. Gutierrez-Ruiz, and Jennifer A. Zallen. Toll receptors remodel epithelia by directing planar-polarized src and pi3k activity. Developmental Cell, 56:1589-1602.e9, Jun 2021. URL: https://doi.org/10.1016/j.devcel.2021.04.012, doi:10.1016/j.devcel.2021.04.012. This article has 44 citations and is from a highest quality peer-reviewed journal.

17. (alshamsi2025theneurotrophindnt2 pages 4-8): Naser Alshamsi, Francisca Rojo-Cortés, Bangfu Zhu, Samaher Fahy, Guiyi Li, Anna Lassota, Marta Moreira, and Alicia Hidalgo. The neurotrophin dnt-2 regulates cell survival and connectivity via the toll-2 receptor during visual system development of <i>drosophila</i>. BioRxiv, Jul 2025. URL: https://doi.org/10.1101/2025.07.18.665476, doi:10.1101/2025.07.18.665476. This article has 0 citations.

18. (lindsay2014conventionalandnonconventional pages 1-2): Scott A. Lindsay and Steven A. Wasserman. Conventional and non-conventional drosophila toll signaling. Developmental and comparative immunology, 42 1:16-24, Jan 2014. URL: https://doi.org/10.1016/j.dci.2013.04.011, doi:10.1016/j.dci.2013.04.011. This article has 201 citations and is from a peer-reviewed journal.

19. (alshamsi2025theneurotrophindnt2 pages 11-14): Naser Alshamsi, Francisca Rojo-Cortés, Bangfu Zhu, Samaher Fahy, Guiyi Li, Anna Lassota, Marta Moreira, and Alicia Hidalgo. The neurotrophin dnt-2 regulates cell survival and connectivity via the toll-2 receptor during visual system development of <i>drosophila</i>. BioRxiv, Jul 2025. URL: https://doi.org/10.1101/2025.07.18.665476, doi:10.1101/2025.07.18.665476. This article has 0 citations.

20. (ligoxygakis2002criticalevaluationof pages 1-3): Petros Ligoxygakis, Philippe Bulet, and Jean‐Marc Reichhart. Critical evaluation of the role of the toll‐like receptor 18‐wheeler in the host defense of drosophila. EMBO reports, 3:666-673, Jul 2002. URL: https://doi.org/10.1093/embo-reports/kvf130, doi:10.1093/embo-reports/kvf130. This article has 95 citations and is from a highest quality peer-reviewed journal.

21. (pare2014apositionaltoll pages 2-2): Adam C. Paré, Athea Vichas, Christopher T. Fincher, Zachary Mirman, Dene L. Farrell, Avantika Mainieri, and Jennifer A. Zallen. A positional toll receptor code directs convergent extension in drosophila. Nature, 515:523-527, Nov 2014. URL: https://doi.org/10.1038/nature13953, doi:10.1038/nature13953. This article has 310 citations and is from a highest quality peer-reviewed journal.

22. (umetsu2022cellmechanicsand pages 5-7): Daiki Umetsu. Cell mechanics and cell-cell recognition controls by toll-like receptors in tissue morphogenesis and homeostasis. Fly, 16:233-247, May 2022. URL: https://doi.org/10.1080/19336934.2022.2074783, doi:10.1080/19336934.2022.2074783. This article has 23 citations and is from a peer-reviewed journal.

23. (kuebler2023stripedexpressionof pages 7-10): Chloe A. Kuebler and Adam C. Paré. Striped expression of leucine-rich repeat proteins coordinates cell intercalation and compartment boundary formation in the early drosophila embryo. Symmetry, 15:1490, Jul 2023. URL: https://doi.org/10.3390/sym15081490, doi:10.3390/sym15081490. This article has 2 citations.

24. (kuebler2023stripedexpressionof pages 6-7): Chloe A. Kuebler and Adam C. Paré. Striped expression of leucine-rich repeat proteins coordinates cell intercalation and compartment boundary formation in the early drosophila embryo. Symmetry, 15:1490, Jul 2023. URL: https://doi.org/10.3390/sym15081490, doi:10.3390/sym15081490. This article has 2 citations.

25. (li2020atollreceptormap pages 18-20): Guiyi Li, Manuel G Forero, Jill S Wentzell, Ilgim Durmus, Reinhard Wolf, Niki C Anthoney, Mieczyslaw Parker, Ruiying Jiang, Jacob Hasenauer, Nicholas James Strausfeld, Martin Heisenberg, and Alicia Hidalgo. A toll-receptor map underlies structural brain plasticity. eLife, Feb 2020. URL: https://doi.org/10.7554/elife.52743, doi:10.7554/elife.52743. This article has 65 citations and is from a domain leading peer-reviewed journal.

26. (li2021thetollroute pages 6-7): Guiyi Li and Alicia Hidalgo. The toll route to structural brain plasticity. Frontiers in Physiology, Jul 2021. URL: https://doi.org/10.3389/fphys.2021.679766, doi:10.3389/fphys.2021.679766. This article has 24 citations.

27. (li2020atollreceptormap pages 14-16): Guiyi Li, Manuel G Forero, Jill S Wentzell, Ilgim Durmus, Reinhard Wolf, Niki C Anthoney, Mieczyslaw Parker, Ruiying Jiang, Jacob Hasenauer, Nicholas James Strausfeld, Martin Heisenberg, and Alicia Hidalgo. A toll-receptor map underlies structural brain plasticity. eLife, Feb 2020. URL: https://doi.org/10.7554/elife.52743, doi:10.7554/elife.52743. This article has 65 citations and is from a domain leading peer-reviewed journal.

28. (li2020atollreceptormap pages 7-10): Guiyi Li, Manuel G Forero, Jill S Wentzell, Ilgim Durmus, Reinhard Wolf, Niki C Anthoney, Mieczyslaw Parker, Ruiying Jiang, Jacob Hasenauer, Nicholas James Strausfeld, Martin Heisenberg, and Alicia Hidalgo. A toll-receptor map underlies structural brain plasticity. eLife, Feb 2020. URL: https://doi.org/10.7554/elife.52743, doi:10.7554/elife.52743. This article has 65 citations and is from a domain leading peer-reviewed journal.

29. (li2020atollreceptormap pages 1-2): Guiyi Li, Manuel G Forero, Jill S Wentzell, Ilgim Durmus, Reinhard Wolf, Niki C Anthoney, Mieczyslaw Parker, Ruiying Jiang, Jacob Hasenauer, Nicholas James Strausfeld, Martin Heisenberg, and Alicia Hidalgo. A toll-receptor map underlies structural brain plasticity. eLife, Feb 2020. URL: https://doi.org/10.7554/elife.52743, doi:10.7554/elife.52743. This article has 65 citations and is from a domain leading peer-reviewed journal.

30. (alshamsi2025theneurotrophindnt2 pages 17-20): Naser Alshamsi, Francisca Rojo-Cortés, Bangfu Zhu, Samaher Fahy, Guiyi Li, Anna Lassota, Marta Moreira, and Alicia Hidalgo. The neurotrophin dnt-2 regulates cell survival and connectivity via the toll-2 receptor during visual system development of <i>drosophila</i>. BioRxiv, Jul 2025. URL: https://doi.org/10.1101/2025.07.18.665476, doi:10.1101/2025.07.18.665476. This article has 0 citations.

31. (sisquella2022decipheringtherole pages 33-36): M Arch Sisquella. Deciphering the role of innate immune response in the model of tuberculosis in drosophila melanogaster. Unknown journal, 2022.

32. (amanda2016drosophilamidlinedevelopment pages 15-19): Amanda Moawad. Drosophila midline development: the role of 18-wheeler and an optimized protocol for transcriptome analysis. Text, 2016. URL: https://doi.org/10.17615/qzh4-et78, doi:10.17615/qzh4-et78. This article has 0 citations and is from a peer-reviewed journal.

33. (kleve2006expressionof18‐wheeler pages 1-3): Cassandra D. Kleve, Dominic A. Siler, Samreen K. Syed, and Elizabeth D. Eldon. Expression of 18‐wheeler in the follicle cell epithelium affects cell migration and egg morphology in drosophila. Developmental Dynamics, 235:1953-1961, Jul 2006. URL: https://doi.org/10.1002/dvdy.20820, doi:10.1002/dvdy.20820. This article has 38 citations and is from a peer-reviewed journal.

34. (kleve2006expressionof18‐wheeler pages 4-5): Cassandra D. Kleve, Dominic A. Siler, Samreen K. Syed, and Elizabeth D. Eldon. Expression of 18‐wheeler in the follicle cell epithelium affects cell migration and egg morphology in drosophila. Developmental Dynamics, 235:1953-1961, Jul 2006. URL: https://doi.org/10.1002/dvdy.20820, doi:10.1002/dvdy.20820. This article has 38 citations and is from a peer-reviewed journal.

35. (amanda2016drosophilamidlinedevelopment pages 39-43): Amanda Moawad. Drosophila midline development: the role of 18-wheeler and an optimized protocol for transcriptome analysis. Text, 2016. URL: https://doi.org/10.17615/qzh4-et78, doi:10.17615/qzh4-et78. This article has 0 citations and is from a peer-reviewed journal.

36. (ligoxygakis2002criticalevaluationof pages 4-6): Petros Ligoxygakis, Philippe Bulet, and Jean‐Marc Reichhart. Critical evaluation of the role of the toll‐like receptor 18‐wheeler in the host defense of drosophila. EMBO reports, 3:666-673, Jul 2002. URL: https://doi.org/10.1093/embo-reports/kvf130, doi:10.1093/embo-reports/kvf130. This article has 95 citations and is from a highest quality peer-reviewed journal.

37. (ehrhardt2022airwayremodelingthe pages 5-6): Birte Ehrhardt, Natalia El-Merhie, Draginja Kovacevic, Juliana Schramm, Judith Bossen, Thomas Roeder, and Susanne Krauss-Etschmann. Airway remodeling: the drosophila model permits a purely epithelial perspective. Frontiers in Allergy, Sep 2022. URL: https://doi.org/10.3389/falgy.2022.876673, doi:10.3389/falgy.2022.876673. This article has 20 citations and is from a peer-reviewed journal.

38. (kambris2002tissueandstagespecific pages 2-3): Zakaria Kambris, Jules A. Hoffmann, Jean-Luc Imler, and Maria Capovilla. Tissue and stage-specific expression of the tolls in drosophila embryos. Gene expression patterns : GEP, 2 3-4:311-7, Dec 2002. URL: https://doi.org/10.1016/s1567-133x(02)00020-0, doi:10.1016/s1567-133x(02)00020-0. This article has 118 citations.

39. (amanda2016drosophilamidlinedevelopment pages 25-29): Amanda Moawad. Drosophila midline development: the role of 18-wheeler and an optimized protocol for transcriptome analysis. Text, 2016. URL: https://doi.org/10.17615/qzh4-et78, doi:10.17615/qzh4-et78. This article has 0 citations and is from a peer-reviewed journal.

40. (kleve2006expressionof18‐wheeler pages 9-9): Cassandra D. Kleve, Dominic A. Siler, Samreen K. Syed, and Elizabeth D. Eldon. Expression of 18‐wheeler in the follicle cell epithelium affects cell migration and egg morphology in drosophila. Developmental Dynamics, 235:1953-1961, Jul 2006. URL: https://doi.org/10.1002/dvdy.20820, doi:10.1002/dvdy.20820. This article has 38 citations and is from a peer-reviewed journal.

41. (kambris2002tissueandstagespecific pages 1-2): Zakaria Kambris, Jules A. Hoffmann, Jean-Luc Imler, and Maria Capovilla. Tissue and stage-specific expression of the tolls in drosophila embryos. Gene expression patterns : GEP, 2 3-4:311-7, Dec 2002. URL: https://doi.org/10.1016/s1567-133x(02)00020-0, doi:10.1016/s1567-133x(02)00020-0. This article has 118 citations.

42. (kambris2002tissueandstagespecific pages 3-4): Zakaria Kambris, Jules A. Hoffmann, Jean-Luc Imler, and Maria Capovilla. Tissue and stage-specific expression of the tolls in drosophila embryos. Gene expression patterns : GEP, 2 3-4:311-7, Dec 2002. URL: https://doi.org/10.1016/s1567-133x(02)00020-0, doi:10.1016/s1567-133x(02)00020-0. This article has 118 citations.

43. (li2020atollreceptormap pages 3-5): Guiyi Li, Manuel G Forero, Jill S Wentzell, Ilgim Durmus, Reinhard Wolf, Niki C Anthoney, Mieczyslaw Parker, Ruiying Jiang, Jacob Hasenauer, Nicholas James Strausfeld, Martin Heisenberg, and Alicia Hidalgo. A toll-receptor map underlies structural brain plasticity. eLife, Feb 2020. URL: https://doi.org/10.7554/elife.52743, doi:10.7554/elife.52743. This article has 65 citations and is from a domain leading peer-reviewed journal.

44. (li2020atollreceptormap pages 2-3): Guiyi Li, Manuel G Forero, Jill S Wentzell, Ilgim Durmus, Reinhard Wolf, Niki C Anthoney, Mieczyslaw Parker, Ruiying Jiang, Jacob Hasenauer, Nicholas James Strausfeld, Martin Heisenberg, and Alicia Hidalgo. A toll-receptor map underlies structural brain plasticity. eLife, Feb 2020. URL: https://doi.org/10.7554/elife.52743, doi:10.7554/elife.52743. This article has 65 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](18w-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](18w-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. amanda2016drosophilamidlinedevelopment pages 19-25
2. ligoxygakis2002criticalevaluationof pages 3-4
3. ligoxygakis2002criticalevaluationof pages 1-3
4. tamada2021tollreceptorsremodel pages 7-9
5. tamada2021tollreceptorsremodel pages 6-7
6. li2020atollreceptormap pages 16-18
7. ehrhardt2022airwayremodelingthe pages 5-6
8. pare2014apositionaltoll pages 2-2
9. amanda2016drosophilamidlinedevelopment pages 25-29
10. amanda2016drosophilamidlinedevelopment pages 39-43
11. kambris2002tissueandstagespecific pages 4-6
12. kambris2002tissueandstagespecific pages 3-4
13. kambris2002tissueandstagespecific pages 2-3
14. li2020atollreceptormap pages 3-5
15. umetsu2022cellmechanicsand pages 7-8
16. pare2014apositionaltoll pages 1-2
17. tamada2021tollreceptorsremodel pages 2-4
18. tamada2021tollreceptorsremodel pages 9-10
19. lindsay2014conventionalandnonconventional pages 15-19
20. li2020atollreceptormap pages 20-22
21. tamada2021tollreceptorsremodel pages 4-6
22. lindsay2014conventionalandnonconventional pages 1-2
23. umetsu2022cellmechanicsand pages 5-7
24. kuebler2023stripedexpressionof pages 7-10
25. kuebler2023stripedexpressionof pages 6-7
26. li2020atollreceptormap pages 18-20
27. li2021thetollroute pages 6-7
28. li2020atollreceptormap pages 14-16
29. li2020atollreceptormap pages 7-10
30. li2020atollreceptormap pages 1-2
31. sisquella2022decipheringtherole pages 33-36
32. amanda2016drosophilamidlinedevelopment pages 15-19
33. ligoxygakis2002criticalevaluationof pages 4-6
34. kambris2002tissueandstagespecific pages 1-2
35. li2020atollreceptormap pages 2-3
36. DOI
37. https://doi.org/10.1038/nature13953
38. https://doi.org/10.1016/j.devcel.2021.04.012
39. https://doi.org/10.1080/19336934.2022.2074783
40. https://doi.org/10.7554/eLife.52743
41. https://doi.org/10.3389/fphys.2021.679766
42. https://doi.org/10.1101/2025.07.18.665476
43. https://doi.org/10.1002/dvdy.20820
44. https://doi.org/10.1016/j.ydbio.2007.04.014
45. https://doi.org/10.17615/qzh4-et78
46. https://doi.org/10.1093/embo-reports/kvf130
47. https://doi.org/10.1016/S1567-133X(02
48. https://doi.org/10.1186/1471-2164-9-446
49. https://doi.org/10.3389/falgy.2022.876673
50. https://doi.org/10.1080/19336934.2022.2074783,
51. https://doi.org/10.1038/nature13953,
52. https://doi.org/10.1016/s1567-133x(02
53. https://doi.org/10.1093/embo-reports/kvf130,
54. https://doi.org/10.17615/qzh4-et78,
55. https://doi.org/10.1016/j.devcel.2021.04.012,
56. https://doi.org/10.1101/2025.07.18.665476,
57. https://doi.org/10.1016/j.dci.2013.04.011,
58. https://doi.org/10.7554/elife.52743,
59. https://doi.org/10.3390/sym15081490,
60. https://doi.org/10.3389/fphys.2021.679766,
61. https://doi.org/10.1002/dvdy.20820,
62. https://doi.org/10.3389/falgy.2022.876673,