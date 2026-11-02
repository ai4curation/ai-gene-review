---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-10-09T20:34:53.119158'
end_time: '2026-10-09T20:46:47.685342'
duration_seconds: 714.57
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: DROME
  gene_id: Lsp2
  gene_symbol: Lsp2
  uniprot_accession: Q24388
  protein_description: 'RecName: Full=Larval serum protein 2; Short=LSP-2; AltName:
    Full=Hexamerin-2; Flags: Precursor;'
  gene_info: Name=Lsp2; ORFNames=CG6806;
  organism_full: Drosophila melanogaster (Fruit fly).
  protein_family: Belongs to the hemocyanin family. .
  protein_domains: Di-copper_centre_dom_sf. (IPR008922); Hemocyanin/hexamerin. (IPR013788);
    Hemocyanin/hexamerin_mid_dom. (IPR000896); Hemocyanin_C. (IPR005203); Hemocyanin_C_sf.
    (IPR037020)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 19
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 1
  edison_message_content: 1
artifacts:
- filename: artifact-00.md
  path: Lsp2-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: image-1.png
  path: Lsp2-deep-research-falcon_artifacts/image-1.png
  media_type: image/png
  source: edison_message_content
  data_storage_id: null
  description: '## Context ID: pqac-00000021 I have extracted the requested information
    from Table 2 on page 7. The first image shows the relevant column headings: ''after
    starv'
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q24388
- **Protein Description:** RecName: Full=Larval serum protein 2; Short=LSP-2; AltName: Full=Hexamerin-2; Flags: Precursor;
- **Gene Information:** Name=Lsp2; ORFNames=CG6806;
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Belongs to the hemocyanin family. .
- **Key Domains:** Di-copper_centre_dom_sf. (IPR008922); Hemocyanin/hexamerin. (IPR013788); Hemocyanin/hexamerin_mid_dom. (IPR000896); Hemocyanin_C. (IPR005203); Hemocyanin_C_sf. (IPR037020)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "Lsp2" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'Lsp2' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **Lsp2** (gene ID: Lsp2, UniProt: Q24388) in DROME.

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
- **UniProt Accession:** Q24388
- **Protein Description:** RecName: Full=Larval serum protein 2; Short=LSP-2; AltName: Full=Hexamerin-2; Flags: Precursor;
- **Gene Information:** Name=Lsp2; ORFNames=CG6806;
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Belongs to the hemocyanin family. .
- **Key Domains:** Di-copper_centre_dom_sf. (IPR008922); Hemocyanin/hexamerin. (IPR013788); Hemocyanin/hexamerin_mid_dom. (IPR000896); Hemocyanin_C. (IPR005203); Hemocyanin_C_sf. (IPR037020)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "Lsp2" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'Lsp2' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **Lsp2** (gene ID: Lsp2, UniProt: Q24388) in DROME.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Functional annotation report: *Drosophila melanogaster* Lsp2

## Identity and principal function

**Identity verified:** The target is *Drosophila melanogaster* **Lsp2/CG6806**, encoding larval serum protein 2 (LSP-2; hexamerin-2), corresponding to the supplied UniProt accession **Q24388**. A primary proteomic study explicitly identifies *Drosophila* Lsp2 as a **hexamerin**, consistent with the hemocyanin/hexamerin domains supplied in the question. The specific UniProt accession and individual domain assignments were supplied by the requester rather than independently established by the retrieved articles. Findings about similarly named proteins in other insects are not used as evidence of this gene’s function. (handke2013thehemolymphproteome pages 4-5, handke2013thehemolymphproteome pages 7-8)

**Primary function:** LSP-2 is a highly abundant **circulating protein and amino-acid reserve**, produced principally by the larval fat body and accumulated in the **extracellular hemolymph** ahead of the nonfeeding wandering and pupal periods. Its broader role is to retain nutritional resources for developmental protein synthesis, not to catalyze a defined reaction or transport a specific small-molecule substrate across a membrane. Hexamerins are related evolutionarily to hemocyanins and assemble as storage-protein complexes; a hemocyanin-related domain annotation alone does **not** establish oxygen transport or copper-dependent enzymatic activity for LSP-2. (short2020proteinstoresregulate pages 2-3, handke2013thehemolymphproteome pages 5-7)

The **site of synthesis** and the **principal site of action** should be distinguished: fat-body cells make Lsp proteins, but their major larval reservoir is the hemolymph. Subsequent uptake and intracellular amino-acid reuse are relevant to metamorphosis; neither localization in hemolymph nor a proposed uptake route implies that LSP-2 is a membrane transporter. (short2020proteinstoresregulate pages 2-3, handke2013thehemolymphproteome pages 5-7, kosakamoto2026lsp2linksearlylife pages 10-11)

## Experimental evidence, quantitative results and limits

In fed, wandering third-instar larvae, **Lsp1a, Lsp1b, Lsp1c and Lsp2 together** may account for **up to 70% of total hemolymph protein**—a figure for the group, **not** LSP-2 alone. Handke and colleagues directly detected Lsp2 in larval hemolymph by mass spectrometry and observed strong late-larval accumulation of the major serum proteins. Their Table 2 reports **1,827 total spectral counts** for Lsp2 and a **log₂(starved/fed) change of −4.67** after starvation (**p = 0.006818**). The authors caution that starvation delays development, so this difference cannot be interpreted solely as consumption of an existing LSP-2 reserve or as direct nutrient-dependent transcriptional control. (handke2013thehemolymphproteome pages 4-5, handke2013thehemolymphproteome pages 5-7, handke2013thehemolymphproteome media 7a89bf3a, handke2013thehemolymphproteome media b4f21f47)

The strongest retrieved **Lsp2-specific causal evidence** is the peer-reviewed 2026 study by Kosakamoto and colleagues. Stable-isotope feeding showed that larval dietary amino acids persist in adult proteins: larva-derived label represented **56.1% of the day-6 adult-head proteome** in the reported comparison and remained detectable at day 16. The isotope result alone cannot assign every retained amino acid to LSP-2—some label may reside in long-lived proteins. Crucially, Lsp2 knockdown additionally reduced larva-derived cytoplasmic ribosomal proteins and early-adult translation, and developmental or adult Lsp2 knockdown extended lifespan. These interventions support a functional link between the storage protein, protein synthesis and adult physiology rather than merely a correlation with larval diet. (kosakamoto2026lsp2linksearlylife pages 7-8, kosakamoto2026lsp2linksearlylife pages 8-9, kosakamoto2025storageproteinmediatedtranslation pages 5-8)

LSP-2’s **amino-acid composition** may matter to this role: the 2026 study reports **1.97-fold enrichment in phenylalanine** and **2.66-fold enrichment in tyrosine**, relative to the average protein encoded by the fly exome. Fat-body Lsp2 knockdown lowered these amino acids in young adults; larval tyrosine restriction lowered Lsp2 expression and early-adult translation. Dietary phenylalanine or histidine restriction also extended lifespan in the tested conditions. These results are consistent with nutritional buffering, but amino-acid enrichment within a protein sequence is **not** evidence that purified LSP-2 selectively binds free phenylalanine or tyrosine. (kosakamoto2026lsp2linksearlylife pages 9-10, kosakamoto2026lsp2linksearlylife pages 9-9)

The table separates observations from interpretations; its starvation values were checked against the cropped Lsp2 row and column headings of Handke and colleagues’ Table 2. (handke2013thehemolymphproteome media 7a89bf3a, handke2013thehemolymphproteome media b4f21f47)

| Biological question | Experimental evidence and date | Interpretation | Important limitation |
|---|---|---|---|
| Is *D. melanogaster* Lsp2/CG6806 an extracellular storage hexamerin produced by the fat body? | Handke *et al.* (June 2013) identified Lsp2/CG6806 by mass spectrometry in larval hemolymph and classified it as a hexamerin. The Lsp family is strongly induced in the fat body during mid-third instar. In well-fed wandering larvae, **Lsp1a, Lsp1b, Lsp1c and Lsp2 together** can constitute up to **70% of total hemolymph protein**. (handke2013thehemolymphproteome pages 4-5, handke2013thehemolymphproteome pages 5-7) | Supports fat-body synthesis followed by secretion into hemolymph, where Lsp2 contributes to a large circulating protein and amino-acid reserve before non-feeding wandering and pupal stages. | The 70% figure is the combined abundance of four larval serum proteins, **not Lsp2 alone**. Proteomics establishes extracellular abundance but does not directly measure secretion kinetics or amino-acid release from purified Lsp2. |
| How does starvation affect circulating Lsp2? | Handke *et al.* (2013), Table 2, reported that hemolymph Lsp2 decreased after starvation: **1,827 total spectral counts, log₂(starved/fed) = −4.67, p = 0.006818**. Total hemolymph protein in starved larvae was approximately twofold lower, principally because larval serum proteins were depleted. (handke2013thehemolymphproteome pages 5-7, handke2013thehemolymphproteome media 7a89bf3a, handke2013thehemolymphproteome media b4f21f47) | Lsp2 abundance is strongly associated with nutritional state and developmental progression, consistent with a nutrient-storage role. | Spectral counting is approximate. Starvation delayed development, so the reduction could reflect both direct nutrient regulation and failure to reach the late-L3 expression peak; it is not a direct measurement of Lsp2 consumption. |
| Do larval dietary amino acids persist into adulthood? | Kosakamoto *et al.* (September 2026, peer-reviewed *Nature*) used pulse-SILAC with heavy lysine and arginine during larval development. In the day-6 adult-head proteome, larva-derived heavy isotope represented **56.1%**, compared with **32.3%** medium isotope acquired during adulthood. At day 16, heavy-labelled protein still represented **41.0%** of the head proteome and **19.5%** of the abdominal proteome. Chimeric RpL22 peptides containing larval- and adult-derived labels supported amino-acid recycling. (kosakamoto2026lsp2linksearlylife pages 7-8, kosakamoto2025storageproteinmediatedtranslation pages 5-8) | Demonstrates substantial carryover of larval nutritional resources across metamorphosis. Combined with Lsp2-specific perturbation, the results support Lsp2 as an amino-acid reservoir linking juvenile diet to the early-adult proteome. | Isotope persistence includes all labelled proteins and cannot by itself assign every retained amino acid to Lsp2. Some signal represents intact long-lived proteins rather than recycled Lsp2-derived amino acids. |
| Does Lsp2 affect translation and lifespan? | In the 2026 *Nature* study, developmental fat-body Lsp2 knockdown reduced larva-derived cytoplasmic ribosomal proteins and early-adult protein synthesis and extended lifespan. Adult-specific knockdown also reduced translation and extended lifespan; lifelong and first-week adult knockdown yielded median lifespans of **67 and 63 days**, respectively. Stable-isotope and proteomic analyses included **8,115 proteins, 83 cytoplasmic ribosomal proteins and 72 mitochondrial ribosomal proteins** in one adult-head comparison. (kosakamoto2026lsp2linksearlylife pages 7-8, kosakamoto2026lsp2linksearlylife pages 8-8, kosakamoto2026lsp2linksearlylife pages 8-9) | Provides causal genetic evidence that Lsp2 availability supports translational capacity and that lowering Lsp2 can promote longevity. Developmental and adult manipulations indicate that Lsp2 is not merely a passive larval marker. | RNAi does not reveal whether Lsp2 acts solely by supplying amino acids or also through nutrient signalling. Several analyses emphasized female heads, and reduced translation is a downstream phenotype rather than a direct molecular interaction. |
| Is Lsp2 composition specialized for particular amino acids? | Kosakamoto *et al.* (2026) reported that Lsp2 contains **1.97-fold more phenylalanine** and **2.66-fold more tyrosine** than the average protein encoded by the *Drosophila* exome. Fat-body Lsp2 knockdown reduced young-adult Phe and Tyr content. Larval Tyr deprivation suppressed Lsp2 and early-adult translation, while reducing dietary Phe or histidine to **25%** of control extended lifespan in both sexes; equivalent isoleucine restriction did not. (kosakamoto2026lsp2linksearlylife pages 9-10, kosakamoto2026lsp2linksearlylife pages 9-9) | Suggests that Lsp2 preferentially buffers aromatic amino-acid resources and connects their juvenile availability to adult translation and longevity. | Enrichment and dietary phenotypes do not prove that Lsp2 has selective amino-acid-binding sites; the enriched residues are incorporated into the protein sequence. Dietary restriction can also affect pathways independent of Lsp2. |
| How might circulating Lsp2 be recovered and mobilized? | The 2026 *Nature* discussion places Lsp2 in a model in which Lsp proteins are retrieved into the fat body before pupariation through **Fbp1**, then made available for amino-acid utilization during non-feeding development. (kosakamoto2026lsp2linksearlylife pages 10-11) | Fbp1-mediated retrieval supplies a plausible route from circulating hemolymph storage to intracellular degradation and amino-acid reuse during metamorphosis. | This is contextual evidence and a working model, **not a direct Lsp2–Fbp1 receptor-binding or uptake experiment in the cited study**. Endosomal–lysosomal degradation and coupling to mTORC1 remain incompletely demonstrated. |
| Could Lsp2 also regulate adult protein appetite? | Waldron *et al.* (June 2026 **bioRxiv preprint**) found that protein deprivation lowered head Lsp2; peptidergic-neuron Lsp2 RNAi increased yeast consumption under protein deprivation. In Mip-positive neurons, knockdown increased protein intake, whereas overexpression reduced it. Fbp1 knockdown and perturbation of tested autophagy or proteasome components did not reproduce the feeding effect. (waldron2026intracellularaminoacid pages 10-13, waldron2026intracellularaminoacid pages 13-17) | Preliminary evidence suggests that intracellular neuronal Lsp2 may act as a protein-demand gauge independently of imported circulating Lsp2, extending its possible role beyond systemic storage. | This work is a non-peer-reviewed preprint and describes a cell-type-specific adult neural phenotype. The sensing mechanism remains unresolved and should not replace the established annotation of Lsp2 as a circulating storage hexamerin. |


*Table: Evidence table for *Drosophila melanogaster* Lsp2/CG6806, separating direct experimental findings from mechanistic interpretation. It highlights localization, nutritional regulation, amino-acid storage, translation, lifespan, and emerging preprint evidence.*

## Biological processes and pathway interpretation

**Developmental resource allocation.** Fat-body Lsp expression rises during the third instar before feeding ceases, and circulating Lsp proteins are associated with nutrient provision through wandering and pupation. The reported involvement of **Fbp1** in Lsp re-uptake into the fat body offers a route for resource recovery before pupariation. However, the retrieved 2026 Lsp2 study does not itself demonstrate a purified **LSP-2–Fbp1 binding interaction** or directly resolve each step of LSP-2 degradation and amino-acid transfer into new proteins. The appropriate annotation is **storage and subsequent mobilization of proteinaceous nutritional resources**, with receptor-level details qualified. (handke2013thehemolymphproteome pages 5-7, kosakamoto2026lsp2linksearlylife pages 10-11)

**Nutrition and translation.** Lsp2 expression and abundance respond to developmental nutritional history. Isotope tracing, stage-restricted fat-body RNAi, adult protein-synthesis assays and lifespan experiments place Lsp2 upstream of changes in translational capacity. A contribution from nutrient-sensing mechanisms such as **mTORC1/4E-BP** is discussed, but an endosomal–lysosomal recycling mechanism and a complete direct signaling chain from LSP-2 to mTORC1 remain incompletely established. Early-life protein restriction also changes insulin signaling; **those broader insulin-related effects should not be attributed automatically to Lsp2**, because Lsp2 knockdown does not reproduce all effects of the dietary intervention. Likewise, reported ecdysone-associated developmental regulation of Lsp expression does not by itself demonstrate direct ecdysone-receptor control of this particular gene. (kosakamoto2025storageproteinmediatedtranslation pages 14-18, handke2013thehemolymphproteome pages 7-8, kosakamoto2026lsp2linksearlylife pages 7-8, kosakamoto2026lsp2linksearlylife pages 10-11, kosakamoto2026lsp2linksearlylife pages 9-10)

**Possible additional adult activity.** A **June 2026 bioRxiv preprint**, not yet peer-reviewed in the retrieved record, reports Lsp2 expression in adult peptidergic neurons and opposite effects of Lsp2 knockdown and overexpression in Mip-positive neurons on protein-food intake. This suggests a possible intracellular nutrient-demand role outside its established circulating larval reservoir. The molecular sensing mechanism remains unresolved, so this proposed neuronal activity should be treated as **emerging**, not as a replacement for the well-supported storage annotation. (waldron2026intracellularaminoacid pages 10-13, waldron2026intracellularaminoacid pages 13-17)

## Research applications and evidence gaps

In practice, Lsp2 is used as a **measurable model of developmental nutrient storage and nutritional carryover** in flies. Published experimental implementations include hemolymph proteomics, fat-body-specific and stage-restricted RNAi, an endogenous **Lsp2–muGFP** reporter, isotope tracing and adult translation assays. These are research tools and physiological models, not evidence of a clinical application. The main remaining mechanistic questions are how much of the amino acids mobilized during metamorphosis can be assigned specifically to LSP-2, how LSP-2 is taken up and degraded, and whether it directly participates in nutrient-sensing signaling. (kosakamoto2025storageproteinmediatedtranslation pages 37-38, kosakamoto2026lsp2linksearlylife pages 7-8, handke2013thehemolymphproteome pages 5-7, kosakamoto2025storageproteinmediatedtranslation pages 14-18)

**Recency and source limitation:** A potentially pertinent **2024 *Developmental Cell*** article on temporal allocation of amino-acid resources was located, but its full study was not available in the retrieved material; no Lsp2-specific result is attributed to it here. The directly verifiable, recent peer-reviewed mechanistic evidence above is from **2026**, supplemented by the foundational **2013** localization and proteomics study. (kosakamoto2026lsp2linksearlylife pages 10-11, waldron2026intracellularaminoacid pages 35-37)

### Key sources and links

- Handke B. *et al.* “The Hemolymph Proteome of Fed and Starved *Drosophila* Larvae.” *PLOS ONE*, **June 2013**. https://doi.org/10.1371/journal.pone.0067208. (handke2013thehemolymphproteome pages 4-5, handke2013thehemolymphproteome pages 5-7)
- Kosakamoto H. *et al.* “Lsp2 links early-life diet to adult translation and lifespan in *Drosophila*.” *Nature*, **September 2026**. https://doi.org/10.1038/s41586-026-11031-3. (kosakamoto2026lsp2linksearlylife pages 7-8, kosakamoto2026lsp2linksearlylife pages 9-10)
- Valzania L., Alami A. and Léopold P. “A temporal allocation of amino acid resources ensures fitness and body allometry in *Drosophila*.” *Developmental Cell*, **2024**; identified as potentially relevant, but **gene-specific findings were not independently checked** here. https://doi.org/10.1016/j.devcel.2024.05.018. (waldron2026intracellularaminoacid pages 35-37)
- Waldron S., Liu Y. and Croset V. “Intracellular amino acid scarcity sensing tunes protein hunger.” **bioRxiv preprint, June 2026**. https://doi.org/10.64898/2026.06.20.732459. (waldron2026intracellularaminoacid pages 10-13, waldron2026intracellularaminoacid pages 13-17)

References

1. (handke2013thehemolymphproteome pages 4-5): Björn Handke, Ingrid Poernbacher, Sandra Goetze, Christian H. Ahrens, Ulrich Omasits, Florian Marty, Nikiana Simigdala, Imke Meyer, Bernd Wollscheid, Erich Brunner, Ernst Hafen, and Christian F. Lehner. The hemolymph proteome of fed and starved drosophila larvae. PLoS ONE, 8:e67208, Jun 2013. URL: https://doi.org/10.1371/journal.pone.0067208, doi:10.1371/journal.pone.0067208. This article has 86 citations and is from a peer-reviewed journal.

2. (handke2013thehemolymphproteome pages 7-8): Björn Handke, Ingrid Poernbacher, Sandra Goetze, Christian H. Ahrens, Ulrich Omasits, Florian Marty, Nikiana Simigdala, Imke Meyer, Bernd Wollscheid, Erich Brunner, Ernst Hafen, and Christian F. Lehner. The hemolymph proteome of fed and starved drosophila larvae. PLoS ONE, 8:e67208, Jun 2013. URL: https://doi.org/10.1371/journal.pone.0067208, doi:10.1371/journal.pone.0067208. This article has 86 citations and is from a peer-reviewed journal.

3. (short2020proteinstoresregulate pages 2-3): Clancy A. Short, John D. Hatle, and Daniel A. Hahn. Protein stores regulate when reproductive displays begin in the male caribbean fruit fly. Frontiers in Physiology, Aug 2020. URL: https://doi.org/10.3389/fphys.2020.00991, doi:10.3389/fphys.2020.00991. This article has 9 citations.

4. (handke2013thehemolymphproteome pages 5-7): Björn Handke, Ingrid Poernbacher, Sandra Goetze, Christian H. Ahrens, Ulrich Omasits, Florian Marty, Nikiana Simigdala, Imke Meyer, Bernd Wollscheid, Erich Brunner, Ernst Hafen, and Christian F. Lehner. The hemolymph proteome of fed and starved drosophila larvae. PLoS ONE, 8:e67208, Jun 2013. URL: https://doi.org/10.1371/journal.pone.0067208, doi:10.1371/journal.pone.0067208. This article has 86 citations and is from a peer-reviewed journal.

5. (kosakamoto2026lsp2linksearlylife pages 10-11): Hina Kosakamoto, Rina Okada, Clive S. Barker, Ayako Isomura-Matoba, Jun Seita, Naoshi Dohmae, Koshi Imami, and Fumiaki Obata. Lsp2 links early-life diet to adult translation and lifespan in drosophila. Nature, 658:474-484, Sep 2026. URL: https://doi.org/10.1038/s41586-026-11031-3, doi:10.1038/s41586-026-11031-3. This article has 2 citations and is from a highest quality peer-reviewed journal.

6. (handke2013thehemolymphproteome media 7a89bf3a): Björn Handke, Ingrid Poernbacher, Sandra Goetze, Christian H. Ahrens, Ulrich Omasits, Florian Marty, Nikiana Simigdala, Imke Meyer, Bernd Wollscheid, Erich Brunner, Ernst Hafen, and Christian F. Lehner. The hemolymph proteome of fed and starved drosophila larvae. PLoS ONE, 8:e67208, Jun 2013. URL: https://doi.org/10.1371/journal.pone.0067208, doi:10.1371/journal.pone.0067208. This article has 86 citations and is from a peer-reviewed journal.

7. (handke2013thehemolymphproteome media b4f21f47): Björn Handke, Ingrid Poernbacher, Sandra Goetze, Christian H. Ahrens, Ulrich Omasits, Florian Marty, Nikiana Simigdala, Imke Meyer, Bernd Wollscheid, Erich Brunner, Ernst Hafen, and Christian F. Lehner. The hemolymph proteome of fed and starved drosophila larvae. PLoS ONE, 8:e67208, Jun 2013. URL: https://doi.org/10.1371/journal.pone.0067208, doi:10.1371/journal.pone.0067208. This article has 86 citations and is from a peer-reviewed journal.

8. (kosakamoto2026lsp2linksearlylife pages 7-8): Hina Kosakamoto, Rina Okada, Clive S. Barker, Ayako Isomura-Matoba, Jun Seita, Naoshi Dohmae, Koshi Imami, and Fumiaki Obata. Lsp2 links early-life diet to adult translation and lifespan in drosophila. Nature, 658:474-484, Sep 2026. URL: https://doi.org/10.1038/s41586-026-11031-3, doi:10.1038/s41586-026-11031-3. This article has 2 citations and is from a highest quality peer-reviewed journal.

9. (kosakamoto2026lsp2linksearlylife pages 8-9): Hina Kosakamoto, Rina Okada, Clive S. Barker, Ayako Isomura-Matoba, Jun Seita, Naoshi Dohmae, Koshi Imami, and Fumiaki Obata. Lsp2 links early-life diet to adult translation and lifespan in drosophila. Nature, 658:474-484, Sep 2026. URL: https://doi.org/10.1038/s41586-026-11031-3, doi:10.1038/s41586-026-11031-3. This article has 2 citations and is from a highest quality peer-reviewed journal.

10. (kosakamoto2025storageproteinmediatedtranslation pages 5-8): Hina Kosakamoto, Rina Okada, Clive Barker, Jun Seita, Naoshi Dohmae, Koshi Imami, and Fumiaki Obata. Storage protein-mediated translation control links juvenile diet to longevity in drosophila. bioRxiv, May 2025. URL: https://doi.org/10.1101/2025.05.18.654697, doi:10.1101/2025.05.18.654697. This article has 3 citations.

11. (kosakamoto2026lsp2linksearlylife pages 9-10): Hina Kosakamoto, Rina Okada, Clive S. Barker, Ayako Isomura-Matoba, Jun Seita, Naoshi Dohmae, Koshi Imami, and Fumiaki Obata. Lsp2 links early-life diet to adult translation and lifespan in drosophila. Nature, 658:474-484, Sep 2026. URL: https://doi.org/10.1038/s41586-026-11031-3, doi:10.1038/s41586-026-11031-3. This article has 2 citations and is from a highest quality peer-reviewed journal.

12. (kosakamoto2026lsp2linksearlylife pages 9-9): Hina Kosakamoto, Rina Okada, Clive S. Barker, Ayako Isomura-Matoba, Jun Seita, Naoshi Dohmae, Koshi Imami, and Fumiaki Obata. Lsp2 links early-life diet to adult translation and lifespan in drosophila. Nature, 658:474-484, Sep 2026. URL: https://doi.org/10.1038/s41586-026-11031-3, doi:10.1038/s41586-026-11031-3. This article has 2 citations and is from a highest quality peer-reviewed journal.

13. (kosakamoto2026lsp2linksearlylife pages 8-8): Hina Kosakamoto, Rina Okada, Clive S. Barker, Ayako Isomura-Matoba, Jun Seita, Naoshi Dohmae, Koshi Imami, and Fumiaki Obata. Lsp2 links early-life diet to adult translation and lifespan in drosophila. Nature, 658:474-484, Sep 2026. URL: https://doi.org/10.1038/s41586-026-11031-3, doi:10.1038/s41586-026-11031-3. This article has 2 citations and is from a highest quality peer-reviewed journal.

14. (waldron2026intracellularaminoacid pages 10-13): Sophie Waldron, Yixin Liu, and Vincent Croset. Intracellular amino acid scarcity sensing tunes protein hunger. Jun 2026. URL: https://doi.org/10.64898/2026.06.20.732459, doi:10.64898/2026.06.20.732459. This article has 0 citations.

15. (waldron2026intracellularaminoacid pages 13-17): Sophie Waldron, Yixin Liu, and Vincent Croset. Intracellular amino acid scarcity sensing tunes protein hunger. Jun 2026. URL: https://doi.org/10.64898/2026.06.20.732459, doi:10.64898/2026.06.20.732459. This article has 0 citations.

16. (kosakamoto2025storageproteinmediatedtranslation pages 14-18): Hina Kosakamoto, Rina Okada, Clive Barker, Jun Seita, Naoshi Dohmae, Koshi Imami, and Fumiaki Obata. Storage protein-mediated translation control links juvenile diet to longevity in drosophila. bioRxiv, May 2025. URL: https://doi.org/10.1101/2025.05.18.654697, doi:10.1101/2025.05.18.654697. This article has 3 citations.

17. (kosakamoto2025storageproteinmediatedtranslation pages 37-38): Hina Kosakamoto, Rina Okada, Clive Barker, Jun Seita, Naoshi Dohmae, Koshi Imami, and Fumiaki Obata. Storage protein-mediated translation control links juvenile diet to longevity in drosophila. bioRxiv, May 2025. URL: https://doi.org/10.1101/2025.05.18.654697, doi:10.1101/2025.05.18.654697. This article has 3 citations.

18. (waldron2026intracellularaminoacid pages 35-37): Sophie Waldron, Yixin Liu, and Vincent Croset. Intracellular amino acid scarcity sensing tunes protein hunger. Jun 2026. URL: https://doi.org/10.64898/2026.06.20.732459, doi:10.64898/2026.06.20.732459. This article has 0 citations.

## Artifacts

- [Edison artifact artifact-00](Lsp2-deep-research-falcon_artifacts/artifact-00.md)
![## Context ID: pqac-00000021 I have extracted the requested information from Table 2 on page 7. The first image shows the relevant column headings: 'after starv](Lsp2-deep-research-falcon_artifacts/image-1.png)

## Citations

1. waldron2026intracellularaminoacid pages 35-37
2. handke2013thehemolymphproteome pages 4-5
3. handke2013thehemolymphproteome pages 7-8
4. short2020proteinstoresregulate pages 2-3
5. handke2013thehemolymphproteome pages 5-7
6. kosakamoto2025storageproteinmediatedtranslation pages 5-8
7. waldron2026intracellularaminoacid pages 10-13
8. waldron2026intracellularaminoacid pages 13-17
9. kosakamoto2025storageproteinmediatedtranslation pages 14-18
10. kosakamoto2025storageproteinmediatedtranslation pages 37-38
11. https://doi.org/10.1371/journal.pone.0067208.
12. https://doi.org/10.1038/s41586-026-11031-3.
13. https://doi.org/10.1016/j.devcel.2024.05.018.
14. https://doi.org/10.64898/2026.06.20.732459.
15. https://doi.org/10.1371/journal.pone.0067208,
16. https://doi.org/10.3389/fphys.2020.00991,
17. https://doi.org/10.1038/s41586-026-11031-3,
18. https://doi.org/10.1101/2025.05.18.654697,
19. https://doi.org/10.64898/2026.06.20.732459,