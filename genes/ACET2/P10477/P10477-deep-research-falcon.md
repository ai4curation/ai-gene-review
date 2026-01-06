---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-26T17:03:39.269155'
end_time: '2025-12-26T17:13:36.348106'
duration_seconds: 597.08
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: ACET2
  gene_id: P10477
  gene_symbol: celE
  uniprot_accession: P10477
  protein_description: 'RecName: Full=Cellulase/esterase CelE {ECO:0000305}; AltName:
    Full=CtCel5C-CE2 {ECO:0000303|PubMed:19338387}; Includes: RecName: Full=Cellulase
    E {ECO:0000303|PubMed:3066698}; EC=3.2.1.4 {ECO:0000269|PubMed:1991028, ECO:0000269|PubMed:3066698};
    AltName: Full=CtCel5C {ECO:0000303|PubMed:19338387}; AltName: Full=Endo-1,4-beta-glucanase
    E {ECO:0000303|PubMed:3066698}; Short=EGE {ECO:0000303|PubMed:3066698}; Short=Endoglucanase
    E {ECO:0000303|PubMed:3066698}; Includes: RecName: Full=Acetylxylan esterase /
    glucomannan deacetylase {ECO:0000305|PubMed:19338387}; EC=3.1.1.- {ECO:0000269|PubMed:19338387};
    EC=3.1.1.72 {ECO:0000269|PubMed:19338387}; AltName: Full=CtCE2 {ECO:0000303|PubMed:19338387};
    Flags: Precursor;'
  gene_info: Name=celE {ECO:0000303|PubMed:3066698}; OrderedLocusNames=Cthe_0797 {ECO:0000312|EMBL:ABN52032.1};
  organism_full: Acetivibrio thermocellus (strain ATCC 27405 / DSM 1237 / JCM 9322
    / NBRC 103400 / NCIMB 10682 / NRRL B-4536 / VPI 7372) (Clostridium thermocellum).
  protein_family: In the C-terminal section; belongs to the carbohydrate
  protein_domains: CE2_N. (IPR040794); CtCE2-like_dom. (IPR037461); Dockerin_1_rpt.
    (IPR002105); Dockerin_dom. (IPR016134); Dockerin_dom_sf. (IPR036439)
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 13
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** P10477
- **Protein Description:** RecName: Full=Cellulase/esterase CelE {ECO:0000305}; AltName: Full=CtCel5C-CE2 {ECO:0000303|PubMed:19338387}; Includes: RecName: Full=Cellulase E {ECO:0000303|PubMed:3066698}; EC=3.2.1.4 {ECO:0000269|PubMed:1991028, ECO:0000269|PubMed:3066698}; AltName: Full=CtCel5C {ECO:0000303|PubMed:19338387}; AltName: Full=Endo-1,4-beta-glucanase E {ECO:0000303|PubMed:3066698}; Short=EGE {ECO:0000303|PubMed:3066698}; Short=Endoglucanase E {ECO:0000303|PubMed:3066698}; Includes: RecName: Full=Acetylxylan esterase / glucomannan deacetylase {ECO:0000305|PubMed:19338387}; EC=3.1.1.- {ECO:0000269|PubMed:19338387}; EC=3.1.1.72 {ECO:0000269|PubMed:19338387}; AltName: Full=CtCE2 {ECO:0000303|PubMed:19338387}; Flags: Precursor;
- **Gene Information:** Name=celE {ECO:0000303|PubMed:3066698}; OrderedLocusNames=Cthe_0797 {ECO:0000312|EMBL:ABN52032.1};
- **Organism (full):** Acetivibrio thermocellus (strain ATCC 27405 / DSM 1237 / JCM 9322 / NBRC 103400 / NCIMB 10682 / NRRL B-4536 / VPI 7372) (Clostridium thermocellum).
- **Protein Family:** In the C-terminal section; belongs to the carbohydrate
- **Key Domains:** CE2_N. (IPR040794); CtCE2-like_dom. (IPR037461); Dockerin_1_rpt. (IPR002105); Dockerin_dom. (IPR016134); Dockerin_dom_sf. (IPR036439)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "celE" matches the protein description above**
2. **Verify the organism is correct:** Acetivibrio thermocellus (strain ATCC 27405 / DSM 1237 / JCM 9322 / NBRC 103400 / NCIMB 10682 / NRRL B-4536 / VPI 7372) (Clostridium thermocellum).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'celE' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **celE** (gene ID: P10477, UniProt: P10477) in ACET2.

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
- **UniProt Accession:** P10477
- **Protein Description:** RecName: Full=Cellulase/esterase CelE {ECO:0000305}; AltName: Full=CtCel5C-CE2 {ECO:0000303|PubMed:19338387}; Includes: RecName: Full=Cellulase E {ECO:0000303|PubMed:3066698}; EC=3.2.1.4 {ECO:0000269|PubMed:1991028, ECO:0000269|PubMed:3066698}; AltName: Full=CtCel5C {ECO:0000303|PubMed:19338387}; AltName: Full=Endo-1,4-beta-glucanase E {ECO:0000303|PubMed:3066698}; Short=EGE {ECO:0000303|PubMed:3066698}; Short=Endoglucanase E {ECO:0000303|PubMed:3066698}; Includes: RecName: Full=Acetylxylan esterase / glucomannan deacetylase {ECO:0000305|PubMed:19338387}; EC=3.1.1.- {ECO:0000269|PubMed:19338387}; EC=3.1.1.72 {ECO:0000269|PubMed:19338387}; AltName: Full=CtCE2 {ECO:0000303|PubMed:19338387}; Flags: Precursor;
- **Gene Information:** Name=celE {ECO:0000303|PubMed:3066698}; OrderedLocusNames=Cthe_0797 {ECO:0000312|EMBL:ABN52032.1};
- **Organism (full):** Acetivibrio thermocellus (strain ATCC 27405 / DSM 1237 / JCM 9322 / NBRC 103400 / NCIMB 10682 / NRRL B-4536 / VPI 7372) (Clostridium thermocellum).
- **Protein Family:** In the C-terminal section; belongs to the carbohydrate
- **Key Domains:** CE2_N. (IPR040794); CtCE2-like_dom. (IPR037461); Dockerin_1_rpt. (IPR002105); Dockerin_dom. (IPR016134); Dockerin_dom_sf. (IPR036439)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "celE" matches the protein description above**
2. **Verify the organism is correct:** Acetivibrio thermocellus (strain ATCC 27405 / DSM 1237 / JCM 9322 / NBRC 103400 / NCIMB 10682 / NRRL B-4536 / VPI 7372) (Clostridium thermocellum).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'celE' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **celE** (gene ID: P10477, UniProt: P10477) in ACET2.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

Plan and verification
- Identity check: The target is celE encoding Endoglucanase E (also known as CelE; CtCel5C-CE2) from Clostridium thermocellum (syn. Acetivibrio thermocellus). Primary literature on Endoglucanase E (CelE) from C. thermocellum confirms gene/protein naming and association with the extracellular cellulosome. Early biochemical work mapped the catalytic N‑terminus and a distinct C‑terminal cellulose-binding region for Endoglucanase E, consistent with a multimodular, cellulosomal enzyme. Later studies characterized the appended CE2 esterase module (CtCE2) within the same protein, establishing bifunctionality alongside GH5 endoglucanase activity (montanier2009; gold2007; durrant1991; hazlewood1993) (montanier2009theactivesite pages 8-9, gold2007globalviewof pages 8-8, durrant1991thenoncatalyticcterminal pages 1-2, hazlewood1993genesequenceand pages 10-10).

Comprehensive research report
1) Key concepts and definitions with current understanding
- Protein and primary function: CelE (Endoglucanase E; UniProt P10477) is a cellulosomal, multimodular enzyme from C. thermocellum that combines an N‑terminal GH5 endo‑1,4‑β‑glucanase with a C‑terminal carbohydrate esterase family 2 (CE2) module. The GH5 domain hydrolyzes internal β‑1,4‑glucan linkages of cellulose/β‑glucans, while the CE2 domain catalyzes deacetylation reactions on plant polysaccharides and also provides noncatalytic cellulose binding that augments cellulase action (PLoS Biol, 2009-03-24; URL: https://doi.org/10.1371/journal.pbio.1000071). Proteomic analysis of native cellulosomes identified CelE as a bifunctional subunit with GH5 and CE2 domains (J Bacteriol, 2007-10; URL: https://doi.org/10.1128/jb.00882-07) (montanier2009theactivesite pages 8-9, gold2007globalviewof pages 8-8).
- Modular architecture: Early mapping of Endoglucanase E showed the N‑terminal catalytic region and a separate C‑terminal cellulose-binding domain; truncation constructs retained catalysis but lost cellulose affinity, highlighting distinct modules. This is consistent with later, more detailed modular annotations of GH5 and CE2 appended to a cellulosomal dockerin-bearing enzyme (Biochem J, 1991-01; URL: https://doi.org/10.1042/bj2730289; J Gen Microbiol, 1993-02; URL: https://doi.org/10.1099/00221287-139-2-307) (durrant1991thenoncatalyticcterminal pages 1-2, hazlewood1993genesequenceand pages 10-10).
- Cellulosome localization: Endoglucanase E is part of the extracellular cellulosome, a surface-anchored multi‑enzyme complex specialized for plant cell-wall deconstruction in C. thermocellum. Proteomics detected CelE in purified cellulosome preparations, supporting extracellular, complex-associated localization (J Bacteriol, 2007-10; URL: https://doi.org/10.1128/jb.00882-07) (gold2007globalviewof pages 8-8, durrant1991thenoncatalyticcterminal pages 1-2).

2) Recent developments and latest research (priority to 2023–2024 sources)
- Direct 2023–2024 sources specifically on C. thermocellum CelE/CtCel5C‑CE2 were not captured in the accessible evidence corpus. However, the modern mechanistic understanding of CelE’s CE2 module as both an esterase and a cellulose-binding enhancer derives from PLoS Biology (2009), which remains a definitive source on CtCE2’s multifunctionality within CelE (montanier2009theactivesite pages 8-9). Proteomic placement of CelE within the cellulosome and its regulation under substrates such as cellobiose was established in 2007 and remains relevant (gold2007globalviewof pages 8-8). Where 2023–2024 review statements on cellulosomes and CE2/GH5 roles are desired, additional targeted retrieval would be needed beyond the current evidence set.

3) Current applications and real-world implementations
- Biomass deconstruction and enzyme engineering: CelE’s bifunctional architecture exemplifies cellulosomal design that synergizes glycoside hydrolase activity with accessory deacetylation and substrate-binding, informing synthetic cellulosome assembly and enzyme cocktail optimization for industrial lignocellulose saccharification. The CtCE2 module’s unusual combination of catalysis and cellulose binding demonstrates a design principle for improving activity on recalcitrant substrates by embedding noncatalytic binding within the catalytic module’s site, potentially transferable to engineered biocatalysts for biomass valorization (PLoS Biol, 2009-03-24; URL: https://doi.org/10.1371/journal.pbio.1000071). Proteomic observations of CelE abundance under cellobiose growth conditions also provide cues for fermentation strategies and substrate-induced enzyme expression profiles relevant to bioprocess development (J Bacteriol, 2007-10; URL: https://doi.org/10.1128/jb.00882-07) (montanier2009theactivesite pages 8-9, gold2007globalviewof pages 8-8).

4) Expert opinions and analysis from authoritative sources
- Multifunctionality in CE2: Montanier et al. argue that the CtCE2 domain within CelE is an example of “gene sharing,” where a catalytic esterase active site also mediates noncatalytic cellulose binding via aromatic residue presentation, thereby boosting the appended GH5’s function on insoluble substrates without compromising esterase activity (PLoS Biol, 2009-03-24; URL: https://doi.org/10.1371/journal.pbio.1000071) (montanier2009theactivesite pages 8-9).
- Cellulosomal context and regulation: Quantitative proteomics by Gold and Martin provides a systems view of the C. thermocellum cellulosome, listing CelE as a bifunctional GH5+CE2 component whose relative abundance varies with growth substrate (e.g., cellobiose), reflecting coordinated regulation within the complex (J Bacteriol, 2007-10; URL: https://doi.org/10.1128/jb.00882-07) (gold2007globalviewof pages 8-8).
- Foundational mapping of CelE modularity: Durrant et al. and Hazlewood et al. established that Endoglucanase E contains separable catalytic and cellulose-binding regions, supporting the broader concept that cellulosomal enzymes bear modular architectures suited for extracellular polysaccharide deconstruction (Biochem J, 1991-01; J Gen Microbiol, 1993-02) (durrant1991thenoncatalyticcterminal pages 1-2, hazlewood1993genesequenceand pages 10-10).

5) Relevant statistics and data from recent studies
- Effects of CE2 aromatic residue mutations in CelE: Mutation of Trp‑790, Tyr‑665, or Trp‑746 in the CE2 module reduced cellulase activity on insoluble substrates by approximately 3–5‑fold, demonstrating the contribution of CE2-mediated cellulose binding to overall activity (PLoS Biol, 2009-03-24; URL: https://doi.org/10.1371/journal.pbio.1000071) (montanier2009theactivesite pages 8-9).
- CE2 catalytic assays and conditions: CtCE2 activity was quantified by hydrolysis of para‑nitrophenyl acetate (4‑NPAc) in defined buffer (e.g., 50 mM sodium phosphate, pH 7.0) and by acetate-release assays upon deacetylation of polysaccharide substrates; additional biophysical binding measurements included ITC and pull‑down with phosphoric acid-swollen cellulose (PLoS Biol, 2009-03-24; URL: https://doi.org/10.1371/journal.pbio.1000071) (montanier2009theactivesite pages 8-9).
- Modular mapping and activity tradeoffs in early work: Truncation analyses showed that the N‑terminal catalytic construct (EGEa) had about fourfold higher specific activity than the full-length Endoglucanase E but with reduced β‑glucan affinity, quantifying functional contributions of the C‑terminal binding region (Biochem J, 1991-01; URL: https://doi.org/10.1042/bj2730289) (durrant1991thenoncatalyticcterminal pages 1-2).

Mechanistic and pathway role
- Pathway context: CelE participates in extracellular cellulose and hemicellulose deconstruction within the C. thermocellum cellulosome. The GH5 domain cleaves internal β‑1,4‑glucan linkages in amorphous cellulose/β‑glucans, generating soluble oligosaccharides for downstream metabolism, while the CE2 module deacetylates noncellulosic plant polysaccharides (e.g., acetylated hemicelluloses), facilitating access for glycoside hydrolases; CE2 also binds cellulose to position CelE on insoluble substrates, enhancing catalytic efficiency on complex biomass (PLoS Biol, 2009-03-24; J Bacteriol, 2007-10) (montanier2009theactivesite pages 8-9, gold2007globalviewof pages 8-8).

Subcellular localization and complex membership
- CelE is secreted and incorporated into the cellulosome, as inferred from its identification in isolated cellulosome fractions and early biochemical characterization showing extracellular, cellulose-binding behavior characteristic of cellulosomal endoglucanases (J Bacteriol, 2007-10; Biochem J, 1991-01) (gold2007globalviewof pages 8-8, durrant1991thenoncatalyticcterminal pages 1-2).

Limitations and notes on recent literature
- Despite an explicit search for 2023–2024 sources specifically discussing CelE/CtCel5C‑CE2 in C. thermocellum, the present evidence set did not surface directly citable recent reviews focused on this protein. The core functional and structural understanding remains grounded in the definitive 2007–2009 literature cited above; additional targeted retrieval would be needed to incorporate any newer syntheses or updates.

Embedded evidence table
| Aspect | Key finding (1–2 sentences) | Organism / Protein | Method / Assay | Quant / Stats (if any) | Source (citation ID) | URL | Year |
|---|---|---|---:|---|---|---|---|
| Bifunctional architecture (GH5 + CE2) and cellulosomal association | CelE/CtCel5C-CE2 is a multimodular, bifunctional enzyme combining a GH5 catalytic module with a CE2 esterase module and is described as a cellulosomal (extracellular) subunit. | Clostridium thermocellum — CelE (CtCel5C-CE2, UniProt P10477) | Sequence/domain annotation and proteomics | N/A (domain architecture reported; abundance assessed by proteomics) | (gold2007globalviewof pages 8-8, montanier2009theactivesite pages 8-9) | https://doi.org/10.1128/jb.00882-07 ; https://doi.org/10.1371/journal.pbio.1000071 | 2007, 2009 |
| CE2 domain: dual esterase and cellulose‑binding functions enhancing cellulase activity | The CE2 module displays classical esterase (deacetylase) activity and a noncatalytic cellulose‑binding function that enhances the appended cellulase activity; mutations in aromatic residues in CE2 reduce cellulase activity ~3–5×. | Clostridium thermocellum — CtCE2 (C‑terminal of CtCel5C-CE2) | Site-directed mutagenesis; hydrolytic assays (4‑NPAc), acetate-release assays, ITC/binding and pull‑down with PASC; stopped‑flow pre‑steady‑state | Mutations (Trp-790, Tyr-665, Trp-746) reduce activity on insoluble substrates by ~3–5×; esterase and binding assays quantified in vitro | (montanier2009theactivesite pages 8-9) | https://doi.org/10.1371/journal.pbio.1000071 | 2009 |
| Early mapping: catalytic region vs C‑terminal cellulose‑binding region in Endoglucanase E | Endoglucanase E (product of celE) is ~780 aa; N‑terminal region contains the catalytic activity while a distinct C‑terminal cellulose‑binding domain (CBD) spans ~residues 432–671; truncation of the C‑terminus alters activity/affinity. | Clostridium thermocellum — Endoglucanase E (CelE / EGE) | Truncation constructs; binding to Avicel/biochemical assays; sequence analysis | N‑terminal construct (EGEa) showed ~4× higher specific activity than full‑length but lower β‑glucan affinity | (durrant1991thenoncatalyticcterminal pages 1-2, hazlewood1993genesequenceand pages 10-10) | https://doi.org/10.1042/bj2730289 ; https://doi.org/10.1099/00221287-139-2-307 | 1991, 1993 |
| Proteomic identification and regulation under cellobiose | Quantitative proteomics detected CelE in the native cellulosome and reported increased CelE abundance under cellobiose growth conditions, indicating regulated expression linked to substrate. | Clostridium thermocellum — CelE | Quantitative proteomic analysis of isolated cellulosomes from different growth substrates | Increase in CelE abundance under cellobiose reported (fold‑change not specified in excerpt) | (gold2007globalviewof pages 8-8) | https://doi.org/10.1128/jb.00882-07 | 2007 |
| Evidence for extracellular / cellulosome localization of endoglucanases (including CelE family) | Endoglucanase E and related cellulases are secreted/extracellular and are components of the cellulosome (cell‑surface multi‑enzyme complex), with CBDs mediating tight binding to cellulose. | Clostridium thermocellum — Endoglucanases (CelE family) | Biochemical fractionation/isolation of cellulosome, binding assays, proteomics | Mature enzyme size and extracellular association reported; CBD mediates Avicel binding | (durrant1991thenoncatalyticcterminal pages 1-2, gold2007globalviewof pages 8-8) | https://doi.org/10.1042/bj2730289 ; https://doi.org/10.1128/jb.00882-07 | 1991, 2007 |
| Kinetic / activity assay details reported for CE2 | CE2 activity measured by hydrolysis of model esterase substrates (e.g., 4‑NPAc) and acetate‑release (deacetylation) assays; stopped‑flow and pre‑steady‑state experiments and binding assays were used to dissect catalytic vs binding roles. | Clostridium thermocellum — CtCE2 (part of CtCel5C-CE2) | 4‑NPAc hydrolysis assays, acetate release (Megazyme kit), stopped‑flow pre‑steady‑state with cellohexaose, ITC, pull‑down | Assay conditions and comparative activities reported; mutational effects on activity (3–5× reductions) documented | (montanier2009theactivesite pages 8-9) | https://doi.org/10.1371/journal.pbio.1000071 | 2009 |


*Table: Concise literature evidence for CelE (CtCel5C‑CE2, UniProt P10477) summarizing domain architecture, CE2 multifunctionality, localization to the cellulosome, proteomic detection, and key assay/quantitative findings from primary sources.*

References (with URLs and publication dates)
- Montanier C et al. The active site of a carbohydrate esterase displays divergent catalytic and noncatalytic binding functions. PLoS Biology. 2009-03-24. URL: https://doi.org/10.1371/journal.pbio.1000071 (montanier2009theactivesite pages 8-9)
- Gold ND, Martin VJJ. Global view of the Clostridium thermocellum cellulosome revealed by quantitative proteomic analysis. Journal of Bacteriology. 2007-10. URL: https://doi.org/10.1128/jb.00882-07 (gold2007globalviewof pages 8-8)
- Durrant AJ et al. The non‑catalytic C‑terminal region of endoglucanase E from Clostridium thermocellum contains a cellulose‑binding domain. Biochemical Journal. 1991-01. URL: https://doi.org/10.1042/bj2730289 (durrant1991thenoncatalyticcterminal pages 1-2)
- Hazlewood GP et al. Gene sequence and properties of CelI, a family E endoglucanase from Clostridium thermocellum. Journal of General Microbiology. 1993-02. URL: https://doi.org/10.1099/00221287-139-2-307 (hazlewood1993genesequenceand pages 10-10)

References

1. (montanier2009theactivesite pages 8-9): Cedric Montanier, Victoria A Money, Virginia M. R Pires, James E Flint, Benedita A Pinheiro, Arun Goyal, José A. M Prates, Atsushi Izumi, Henrik Stålbrand, Carl Morland, Alan Cartmell, Katarina Kolenova, Evangelos Topakas, Eleanor J Dodson, David N Bolam, Gideon J Davies, Carlos M. G. A Fontes, and Harry J Gilbert. The active site of a carbohydrate esterase displays divergent catalytic and noncatalytic binding functions. PLoS Biology, 7:e1000071, Mar 2009. URL: https://doi.org/10.1371/journal.pbio.1000071, doi:10.1371/journal.pbio.1000071. This article has 83 citations and is from a highest quality peer-reviewed journal.

2. (gold2007globalviewof pages 8-8): Nicholas D. Gold and Vincent J. J. Martin. Global view of the <i>clostridium thermocellum</i> cellulosome revealed by quantitative proteomic analysis. Journal of Bacteriology, 189:6787-6795, Oct 2007. URL: https://doi.org/10.1128/jb.00882-07, doi:10.1128/jb.00882-07. This article has 271 citations and is from a peer-reviewed journal.

3. (durrant1991thenoncatalyticcterminal pages 1-2): Alastair J. Durrant, Judith Hall, Geoffrey P. HAZLEWOODt, and H. Gilbert. The non-catalytic c-terminal region of endoglucanase e from clostridium thermocellum contains a cellulose-binding domain. The Biochemical journal, 273(Pt 2):289-93, Jan 1991. URL: https://doi.org/10.1042/bj2730289, doi:10.1042/bj2730289. This article has 63 citations.

4. (hazlewood1993genesequenceand pages 10-10): G. P. Hazlewood, K. Davidson, J. I. Laurie, N. S. Huskisson, and H. J. Gilbert. Gene sequence and properties of cell, a family e endoglucanase from clostridium thermocellum. Journal of General Microbiology, 139:307-316, Feb 1993. URL: https://doi.org/10.1099/00221287-139-2-307, doi:10.1099/00221287-139-2-307. This article has 52 citations.

## Citations

1. montanier2009theactivesite pages 8-9
2. gold2007globalviewof pages 8-8
3. durrant1991thenoncatalyticcterminal pages 1-2
4. hazlewood1993genesequenceand pages 10-10
5. https://doi.org/10.1371/journal.pbio.1000071
6. https://doi.org/10.1128/jb.00882-07
7. https://doi.org/10.1042/bj2730289;
8. https://doi.org/10.1099/00221287-139-2-307
9. https://doi.org/10.1042/bj2730289
10. https://doi.org/10.1371/journal.pbio.1000071,
11. https://doi.org/10.1128/jb.00882-07,
12. https://doi.org/10.1042/bj2730289,
13. https://doi.org/10.1099/00221287-139-2-307,