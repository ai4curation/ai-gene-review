---
provider: falcon
model: Edison Scientific Literature
cached: true
start_time: '2026-02-01T16:13:19.693015'
end_time: '2026-02-01T16:13:19.696347'
duration_seconds: 0.0
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: DROME
  gene_id: Lkb1
  gene_symbol: Lkb1
  uniprot_accession: Q8T9L5
  protein_description: 'RecName: Full=Serine/threonine-protein kinase STK11 {ECO:0000256|ARBA:ARBA00068788};
    EC=2.7.11.1 {ECO:0000256|ARBA:ARBA00012513};'
  gene_info: Name=Lkb1 {ECO:0000313|EMBL:AAF54972.2, ECO:0000313|FlyBase:FBgn0038167};
    Synonyms=anon-EST:Posey135 {ECO:0000313|EMBL:AAF54972.2}, dLKB1 {ECO:0000313|EMBL:AAF54972.2},
    dlkb1 {ECO:0000313|EMBL:AAF54972.2}, Dmel\CG9374 {ECO:0000313|EMBL:AAF54972.2},
    DmLKB1 {ECO:0000313|EMBL:AAF54972.2}, LKB1 {ECO:0000313|EMBL:AAF54972.2}, lkb1
    {ECO:0000313|EMBL:AAF54972.2}, LKB1/PEUTZ JEGHERS KINASE {ECO:0000313|EMBL:AAF54972.2},
    PAR-4 {ECO:0000313|EMBL:AAF54972.2}, par-4 {ECO:0000313|EMBL:AAF54972.2}, PAR4
    {ECO:0000313|EMBL:AAF54972.2}, Par4 {ECO:0000313|EMBL:AAF54972.2}, STK11 {ECO:0000313|EMBL:AAF54972.2};
    ORFNames=CG9374 {ECO:0000313|EMBL:AAL39386.1, ECO:0000313|FlyBase:FBgn0038167},
    Dmel_CG9374 {ECO:0000313|EMBL:AAF54972.2};
  organism_full: Drosophila melanogaster (Fruit fly).
  protein_family: Belongs to the protein kinase superfamily. CAMK Ser/Thr
  protein_domains: Kinase-like_dom_sf. (IPR011009); LKB1_c. (IPR039154); Prot_kinase_dom.
    (IPR000719); Protein_kinase_ATP_BS. (IPR017441); Ser/Thr_kinase_AS. (IPR008271)
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 19
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q8T9L5
- **Protein Description:** RecName: Full=Serine/threonine-protein kinase STK11 {ECO:0000256|ARBA:ARBA00068788}; EC=2.7.11.1 {ECO:0000256|ARBA:ARBA00012513};
- **Gene Information:** Name=Lkb1 {ECO:0000313|EMBL:AAF54972.2, ECO:0000313|FlyBase:FBgn0038167}; Synonyms=anon-EST:Posey135 {ECO:0000313|EMBL:AAF54972.2}, dLKB1 {ECO:0000313|EMBL:AAF54972.2}, dlkb1 {ECO:0000313|EMBL:AAF54972.2}, Dmel\CG9374 {ECO:0000313|EMBL:AAF54972.2}, DmLKB1 {ECO:0000313|EMBL:AAF54972.2}, LKB1 {ECO:0000313|EMBL:AAF54972.2}, lkb1 {ECO:0000313|EMBL:AAF54972.2}, LKB1/PEUTZ JEGHERS KINASE {ECO:0000313|EMBL:AAF54972.2}, PAR-4 {ECO:0000313|EMBL:AAF54972.2}, par-4 {ECO:0000313|EMBL:AAF54972.2}, PAR4 {ECO:0000313|EMBL:AAF54972.2}, Par4 {ECO:0000313|EMBL:AAF54972.2}, STK11 {ECO:0000313|EMBL:AAF54972.2}; ORFNames=CG9374 {ECO:0000313|EMBL:AAL39386.1, ECO:0000313|FlyBase:FBgn0038167}, Dmel_CG9374 {ECO:0000313|EMBL:AAF54972.2};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Belongs to the protein kinase superfamily. CAMK Ser/Thr
- **Key Domains:** Kinase-like_dom_sf. (IPR011009); LKB1_c. (IPR039154); Prot_kinase_dom. (IPR000719); Protein_kinase_ATP_BS. (IPR017441); Ser/Thr_kinase_AS. (IPR008271)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "Lkb1" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'Lkb1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **Lkb1** (gene ID: Lkb1, UniProt: Q8T9L5) in DROME.

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
- **UniProt Accession:** Q8T9L5
- **Protein Description:** RecName: Full=Serine/threonine-protein kinase STK11 {ECO:0000256|ARBA:ARBA00068788}; EC=2.7.11.1 {ECO:0000256|ARBA:ARBA00012513};
- **Gene Information:** Name=Lkb1 {ECO:0000313|EMBL:AAF54972.2, ECO:0000313|FlyBase:FBgn0038167}; Synonyms=anon-EST:Posey135 {ECO:0000313|EMBL:AAF54972.2}, dLKB1 {ECO:0000313|EMBL:AAF54972.2}, dlkb1 {ECO:0000313|EMBL:AAF54972.2}, Dmel\CG9374 {ECO:0000313|EMBL:AAF54972.2}, DmLKB1 {ECO:0000313|EMBL:AAF54972.2}, LKB1 {ECO:0000313|EMBL:AAF54972.2}, lkb1 {ECO:0000313|EMBL:AAF54972.2}, LKB1/PEUTZ JEGHERS KINASE {ECO:0000313|EMBL:AAF54972.2}, PAR-4 {ECO:0000313|EMBL:AAF54972.2}, par-4 {ECO:0000313|EMBL:AAF54972.2}, PAR4 {ECO:0000313|EMBL:AAF54972.2}, Par4 {ECO:0000313|EMBL:AAF54972.2}, STK11 {ECO:0000313|EMBL:AAF54972.2}; ORFNames=CG9374 {ECO:0000313|EMBL:AAL39386.1, ECO:0000313|FlyBase:FBgn0038167}, Dmel_CG9374 {ECO:0000313|EMBL:AAF54972.2};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Belongs to the protein kinase superfamily. CAMK Ser/Thr
- **Key Domains:** Kinase-like_dom_sf. (IPR011009); LKB1_c. (IPR039154); Prot_kinase_dom. (IPR000719); Protein_kinase_ATP_BS. (IPR017441); Ser/Thr_kinase_AS. (IPR008271)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "Lkb1" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'Lkb1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **Lkb1** (gene ID: Lkb1, UniProt: Q8T9L5) in DROME.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

Plan overview
We verified the target identity, searched and gathered recent and foundational literature, extracted mechanistic evidence on Drosophila Lkb1 (CG9374; STK11) function, localization, pathways, and recent regulatory updates (2023–2024), and synthesized a structured report with citations, URLs, and dates. Identity checks confirm Drosophila melanogaster Lkb1 (UniProt Q8T9L5) is a serine/threonine kinase in the CAMK-like kinase family with a canonical protein kinase domain, consistent with the literature cited below (2003–2024) (partanen2013breakingtheepithelial pages 4-4, amin2009lkb1regulatespolarity pages 1-1, thiele2016subcellularlocalizationof pages 14-18).

Verification of target identity (mandatory)
- Gene symbol and organism: The literature cited explicitly studies Drosophila melanogaster Lkb1 (also called dLKB1/PAR-4; CG9374), controlling oocyte anterior–posterior (AP) polarity, epithelial polarity, retina remodeling, and neuroblast division (e.g., Amin et al., PNAS, 2009, https://doi.org/10.1073/pnas.0812469106; Partanen et al., Phil. Trans. R. Soc. B, 2013, https://doi.org/10.1098/rstb.2013.0111) (amin2009lkb1regulatespolarity pages 1-1, partanen2013breakingtheepithelial pages 4-4).
- Domains/family: Ser/Thr protein kinase, activates AMPK-family kinases; activation by STRAD/MO25 is conserved; these are consistent with the UniProt domain annotations (Thiele 2016 dissertation, https://doi.org/10.5283/epub.31340; Trelford & Shepherd, Cell Commun. Signal., 2024, https://doi.org/10.1186/s12964-024-01689-5) (thiele2016subcellularlocalizationof pages 14-18, trelford2024lkb1biologyassessing pages 15-16, trelford2024lkb1biologyassessing pages 1-2, trelford2024lkb1biologyassessing pages 2-4).
- No cross-species confusion: Where human STK11 is discussed, it is framed as the ortholog; Drosophila-specific experiments and phenotypes are used throughout (amin2009lkb1regulatespolarity pages 1-1, thiele2016subcellularlocalizationof pages 14-18, partanen2013breakingtheepithelial pages 4-4).

Key concepts and definitions (current understanding)
- Biochemical identity and catalytic activity: Lkb1 is a serine/threonine “master kinase” that phosphorylates and activates AMPK and AMPK-related kinases (including MARK/Par-1, SIK, NUAK), coupling energy sensing to polarity, growth, and cell division (Partanen 2013 review; Amin 2009) (partanen2013breakingtheepithelial pages 4-4, amin2009lkb1regulatespolarity pages 1-1). Lkb1 directly phosphorylates Drosophila Par-1 (reported T408) and AMPK, placing it upstream of polarity and metabolic control modules (Thiele 2016; Amin 2009) (thiele2016subcellularlocalizationof pages 18-21, amin2009lkb1regulatespolarity pages 1-1). 
- Activation mechanism: The catalytically active unit is a 1:1:1 LKB1–STRAD–MO25 complex that allosterically activates LKB1 and promotes cytoplasmic/membrane localization; STRAD inhibits nuclear import and engages nuclear export, while MO25 stabilizes STRAD and the complex (Trelford & Shepherd 2024, https://doi.org/10.1186/s12964-024-01689-5; Thiele 2016, https://doi.org/10.5283/epub.31340) (trelford2024lkb1biologyassessing pages 4-5, trelford2024lkb1biologyassessing pages 1-2, trelford2024lkb1biologyassessing pages 2-4, thiele2016subcellularlocalizationof pages 14-18).
- Localization determinants: Lkb1 shuttles between nucleus and cytoplasm; active complexes are predominantly cytosolic/membrane-associated. A C-terminal basic/farnesylation region and phospholipid interactions (e.g., phosphatidic acid) promote membrane recruitment necessary in vivo; an N-terminal NLS mediates import (Thiele 2016; Borkowsky et al., Cells 2023, published Mar 6, 2023: https://doi.org/10.3390/cells12050812) (thiele2016subcellularlocalizationof pages 14-18, thiele2016subcellularlocalizationof pages 21-24, borkowsky2023phosphorylationoflkb1 pages 1-2).

Recent developments and latest research (priority 2023–2024)
- PDK1-dependent regulation (2023): In Drosophila, PDK1 binds Lkb1 via a conserved motif and phosphorylates Lkb1 at T353. This phosphorylation decreases Lkb1 catalytic activity, reduces AMPK activation, alters downstream pS6K, and modulates cell/organ growth. CRISPR knock-in flies expressing phospho-mutant Lkb1 (T353A, T353D) show distinct signaling and growth phenotypes, and molecular dynamics suggest phosphorylation remodels the ATP-binding pocket (Borkowsky et al., Cells, 2023-03-06, https://doi.org/10.3390/cells12050812) (borkowsky2023phosphorylationoflkb1 pages 1-2, borkowsky2023phosphorylationoflkb1 pages 4-5, borkowsky2023phosphorylationoflkb1 pages 7-8).
- Consolidated expert synthesis (2024): A comprehensive review underscores STRAD/MO25-dependent activation, nucleocytoplasmic shuttling, and the breadth of AMPK-family downstreams (including Par-1/MARK) in polarity and metabolism; it also discusses therapeutic implications of modulating LKB1 signaling (Trelford & Shepherd, Cell Commun. Signal., 2024-06, https://doi.org/10.1186/s12964-024-01689-5) (trelford2024lkb1biologyassessing pages 15-16, trelford2024lkb1biologyassessing pages 4-5, trelford2024lkb1biologyassessing pages 1-2, trelford2024lkb1biologyassessing pages 16-17, trelford2024lkb1biologyassessing pages 2-4).
- Hippo/Yorkie cross-talk: In conserved contexts, LKB1 has been identified as an upstream regulator influencing Hippo pathway output (Yorkie/YAP/TAZ), linking polarity/metabolism modules with growth control signaling; this connection is noted in recent synthesis accompanying the 2023 Drosophila study (Borkowsky et al., 2023, https://doi.org/10.3390/cells12050812) (borkowsky2023phosphorylationoflkb1 pages 1-2).

Primary function and substrates in Drosophila
- Enzymatic reaction: Lkb1 transfers phosphate from ATP to Ser/Thr residues on downstream kinases. Direct Drosophila substrates supported in the gathered evidence are AMPK and Par-1/MARK; genetic and biochemical data position Lkb1 upstream of these modules in polarity and metabolic responses (Thiele 2016; Amin 2009) (thiele2016subcellularlocalizationof pages 18-21, amin2009lkb1regulatespolarity pages 1-1). 
- Substrate specificity: Within the AMPK-related kinase subfamily, Lkb1 activates multiple kinases (MARK/Par-1, SIK, NUAK), with tissue-specific deployment; in photoreceptors, many remodeling phenotypes are AMPK-independent, implicating other AMPK-family substrates downstream of Lkb1 (Amin 2009) (amin2009lkb1regulatespolarity pages 1-1).

Cellular localization and sites of action
- Oocyte and follicle epithelium: Lkb1 is essential for oocyte AP axis formation and epithelial apico–basal polarity, ensuring proper localization of PAR proteins and adherens junctions (Partanen 2013; Amin 2009) (partanen2013breakingtheepithelial pages 4-4, amin2009lkb1regulatespolarity pages 1-1). 
- Pupal retina: During dramatic polarity remodeling, Lkb1 positions adherens junctions and restricts apical domain expansion; AMPK is not the primary mediator in this context (Amin 2009) (amin2009lkb1regulatespolarity pages 1-1). 
- Neuroblasts: Lkb1 is required for correct apical polarity complex localization, spindle assembly, and asymmetric division; mutants show spindle defects and polyploidy (Thiele 2016) (thiele2016subcellularlocalizationof pages 18-21).
- Subcellular: Active Lkb1–STRAD–MO25 complexes localize to cytoplasm and cortex/membrane; nuclear export is enhanced by STRAD, while C-terminal motifs that bind acidic lipids and undergo lipid modification promote membrane association (Thiele 2016; Borkowsky 2023) (thiele2016subcellularlocalizationof pages 14-18, thiele2016subcellularlocalizationof pages 21-24, borkowsky2023phosphorylationoflkb1 pages 1-2).

Roles in pathways: polarity, spindle assembly, and metabolism
- Polarity establishment and remodeling: Lkb1 orchestrates polarity in the oocyte (AP axis), follicle epithelium (apico–basal polarity), and pupal retina (AJ placement, apical domain restriction), engaging Par-1/MARK and other AMPK-related kinases in a context-dependent manner (Amin 2009; Partanen 2013) (amin2009lkb1regulatespolarity pages 1-1, partanen2013breakingtheepithelial pages 4-4). 
- Spindle assembly/asymmetric division: Lkb1 is necessary for proper spindle formation and neuroblast asymmetric division, acting upstream of Par-1/AMPK modules (Thiele 2016) (thiele2016subcellularlocalizationof pages 18-21). 
- Metabolic control: Lkb1→AMPK activation links energy status to mTOR antagonism and autophagy; in Drosophila, PDK1-mediated phosphorylation of Lkb1 reduces AMPK activation and shifts growth signaling (Borkowsky 2023; Trelford & Shepherd 2024) (borkowsky2023phosphorylationoflkb1 pages 7-8, borkowsky2023phosphorylationoflkb1 pages 1-2, trelford2024lkb1biologyassessing pages 4-5).

Interactions with STRAD/MO25 homologs
- STRAD (STE20-like pseudokinase) and MO25 form a heterotrimeric complex with Lkb1 that is essential for allosteric activation and cytoplasmic localization. In Drosophila neuroblasts, STRAD/MO25 co-immunoprecipitate with Lkb1; altering STRAD/MO25 interactions perturbs localization/activity, while PDK1 phosphorylation at T353 does not disrupt STRAD/MO25 binding (Thiele 2016; Borkowsky 2023) (thiele2016subcellularlocalizationof pages 14-18, borkowsky2023phosphorylationoflkb1 pages 7-8).

Current applications and real-world implementations
- Polarity and development models: Drosophila Lkb1 is a tractable in vivo system to dissect polarity establishment (oocyte AP axis, epithelial polarity) and remodeling (pupal retina), enabling genetic tests of AMPK-family downstreams and polarity networks (Amin 2009; Partanen 2013) (amin2009lkb1regulatespolarity pages 1-1, partanen2013breakingtheepithelial pages 4-4).
- Disease relevance and tool development: Human STK11/LKB1 is a tumor suppressor mutated in Peutz–Jeghers syndrome and cancers; the 2024 review outlines therapeutic strategies and the need for LKB1-pathway modulators, emphasizing challenges due to STRAD/MO25 dependency, isoforms, and PTMs (Trelford & Shepherd 2024, https://doi.org/10.1186/s12964-024-01689-5) (trelford2024lkb1biologyassessing pages 15-16, trelford2024lkb1biologyassessing pages 1-2). 
- Regulatory axis as a target: The 2023 Drosophila study highlights PDK1→Lkb1 phosphorylation as a conserved regulatory input connecting PI3K-PDK1 signals to LKB1–AMPK growth control, suggesting nodes for pharmacologic intervention or genetic manipulation (Borkowsky 2023, https://doi.org/10.3390/cells12050812) (borkowsky2023phosphorylationoflkb1 pages 1-2, borkowsky2023phosphorylationoflkb1 pages 7-8).

Expert opinions and analysis
- Polarity–metabolism integration: Authoritative reviews emphasize LKB1 as a central integrator of cell polarity and metabolic stress responses, acting through AMPK and AMPK-related kinases, with activation critically dependent on STRAD/MO25 and nucleocytoplasmic shuttling (Partanen 2013; Trelford & Shepherd 2024) (partanen2013breakingtheepithelial pages 4-4, trelford2024lkb1biologyassessing pages 4-5, trelford2024lkb1biologyassessing pages 1-2, trelford2024lkb1biologyassessing pages 2-4). 
- Context dependence of downstreams: Eye remodeling phenotypes that are largely AMPK-independent indicate that distinct AMPK-family effectors (e.g., Par-1/MARK, SIK, NUAK) mediate Lkb1 outputs in different tissues, aligning with the “master kinase” paradigm and arguing against single-effector models (Amin 2009) (amin2009lkb1regulatespolarity pages 1-1). 
- Upstream regulation: New data place PDK1 as a direct inhibitor of Lkb1 catalytic activity via kinase domain phosphorylation (T353 in fly), refining models of how growth factor/PI3K signals can tune LKB1–AMPK pathway output (Borkowsky 2023) (borkowsky2023phosphorylationoflkb1 pages 7-8, borkowsky2023phosphorylationoflkb1 pages 1-2).

Relevant statistics and data (recent studies)
- PDK1→Lkb1 knock-in phenotypes: MARCM mitotic index (pH3 S10) in wing disc clones: WT ≈1.2%, T353A ≈0.9%, T353D ≈1.4%; adult body-size differences measured (n≥35 per genotype); survival similar across genotypes (n≈100). Biochemical assays show reduced pAMPK and increased pS6K with phospho-mimetic T353D (Borkowsky 2023, 2023-03-06, https://doi.org/10.3390/cells12050812) (borkowsky2023phosphorylationoflkb1 pages 4-5, borkowsky2023phosphorylationoflkb1 pages 7-8). 
- Retina polarity remodeling: lkb1 mutant photoreceptors exhibit elongated rhabdomeres and expanded apical/junctional domains with AJ misplacement; AMPK mutants do not replicate these phenotypes under the same conditions, supporting AMPK-independent outputs (Amin 2009, 2009-06-02 online, https://doi.org/10.1073/pnas.0812469106) (amin2009lkb1regulatespolarity pages 1-1, amin2009lkb1regulatespolarity pages 6-6).

Concise evidence table
| Category | Finding (1–2 sentences) | Experimental context | Primary downstream target(s) | Source (year and URL) | Citation ID |
|---|---|---|---|---|---|
| Biochemical function | Lkb1 is a serine/threonine "master" kinase that activates the AMPK-family of kinases and couples energy sensing to polarity and growth control. | Genetic, biochemical, and review syntheses in Drosophila and conserved models. | AMPK-family kinases (AMPK, MARK/Par-1, NUAK, SIK, etc.) | Partanen et al., 2013 (review) https://doi.org/10.1098/rstb.2013.0111; Amin et al., 2009 (PNAS) https://doi.org/10.1073/pnas.0812469106 | (partanen2013breakingtheepithelial pages 4-4, amin2009lkb1regulatespolarity pages 1-1) |
| Direct substrates in flies | Lkb1 phosphorylates and activates AMPK and directly phosphorylates Par-1 (reported Par-1 phosphorylation at T408), linking metabolism to polarity. | In vitro kinase assays, mutant/rescue experiments and biochemical mapping in Drosophila models. | AMPK; PAR-1 (T408) | Thiele, 2016 (dissertation) https://doi.org/10.5283/epub.31340; Amin et al., 2009 https://doi.org/10.1073/pnas.0812469106 | (thiele2016subcellularlocalizationof pages 18-21, amin2009lkb1regulatespolarity pages 1-1) |
| STRAD/Mo25 complex & localization | STRAD and Mo25 binding stabilizes an active Lkb1 conformation and promotes cytoplasmic/membrane localization necessary for functional signaling. | Co-immunoprecipitation, overexpression and rescue assays in neuroblasts and epithelial cells. | STRAD (Strad homolog), Mo25 (adaptor complex) | Thiele, 2016 https://doi.org/10.5283/epub.31340; Partanen et al., 2013 https://doi.org/10.1098/rstb.2013.0111 | (thiele2016subcellularlocalizationof pages 14-18, partanen2013breakingtheepithelial pages 4-4) |
| Oocyte AP axis & epithelial polarity | Lkb1 is required for anterior–posterior axis establishment in the oocyte and for apical–basal polarity in follicle/epithelial cells; loss mislocalizes Par proteins and junctional markers. | Genetic loss-of-function and germline/clonal analyses during oogenesis and follicle/epithelium development. | Par proteins (including Par-1), AMPK (context-dependent) | Partanen et al., 2013 https://doi.org/10.1098/rstb.2013.0111; Amin et al., 2009 https://doi.org/10.1073/pnas.0812469106 | (partanen2013breakingtheepithelial pages 4-4, amin2009lkb1regulatespolarity pages 1-1) |
| Neuroblast spindle & asymmetric division | Lkb1 is necessary for proper spindle formation and asymmetric neuroblast division; mutants show spindle defects, polarity protein mislocalization, and polyploidy. | Larval neuroblast imaging, mutant phenotyping and biochemical assays. | Par-1 and AMPK-family effectors implicated in mediating division/spindle roles | Thiele, 2016 https://doi.org/10.5283/epub.31340; Amin et al., 2009 https://doi.org/10.1073/pnas.0812469106 | (thiele2016subcellularlocalizationof pages 18-21, amin2009lkb1regulatespolarity pages 1-1) |
| Eye/pupal retina polarity remodeling | Lkb1 controls polarity remodeling and adherens junction placement in the pupal retina; many retinal phenotypes are largely AMPK-independent, implying multiple downstream AMPK-like kinases. | MARCM clonal analysis, RNAi and genetic interaction studies in pupal retina. | Multiple AMPK-family kinases (Par-1, SIK, NUAK, etc.) | Amin et al., 2009 (PNAS) https://doi.org/10.1073/pnas.0812469106 | (amin2009lkb1regulatespolarity pages 1-1) |
| 2023: PDK1 phosphorylation regulates Lkb1 | PDK1 binds a conserved motif and phosphorylates Lkb1 at T353 in Drosophila; this phosphorylation reduces Lkb1 activity toward AMPK, altering pAMPK/pS6K and increasing cell/organ size. | In vitro kinase assays, CRISPR knock-in flies (WT, T353A, T353D), MD simulations, signaling blots. | AMPK signaling (reduced pAMPK) and downstream mTOR readouts | Borkowsky et al., 2023 https://doi.org/10.17879/90089628698 | (borkowsky2023phosphorylationoflkb1 pages 1-2, borkowsky2023phosphorylationoflkb1 pages 4-5, borkowsky2023phosphorylationoflkb1 pages 7-8) |
| Quantitative phenotypes / metrics | Reported metrics include MARCM mitotic index (pH3): WT ≈1.2%, T353A ≈0.9%, T353D ≈1.4%; body-size differences measured (n≥35), survival assays (n≈100); retina lkb1 clones show elongated rhabdomeres and AJ defects. | MARCM clone counts, adult body-size measurements, survival assays, pupal retina imaging. | Phenotypic readouts reflecting Lkb1 perturbation (mitotic index, body size, survival, retinal morphology) | Borkowsky et al., 2023 https://doi.org/10.17879/90089628698; Amin et al., 2009 https://doi.org/10.1073/pnas.0812469106 | (borkowsky2023phosphorylationoflkb1 pages 7-8, borkowsky2023phosphorylationoflkb1 pages 4-5, amin2009lkb1regulatespolarity pages 1-1) |


*Table: A concise evidence-linked table summarizing biochemical function, substrates, localization control, developmental roles, recent 2023 regulation by PDK1, and quantitative phenotypes for D. melanogaster Lkb1 (UniProt Q8T9L5), with source links and tool-evidence IDs for traceability.*

Gene product localization and compartments
- Predominantly cytosolic and membrane-associated when active; nuclear pools exist and are regulated by STRAD-dependent export and importin-dependent import. C-terminal lipidation/phospholipid binding promotes membrane targeting in epithelia and neuroblasts (Thiele 2016; Borkowsky 2023) (thiele2016subcellularlocalizationof pages 21-24, thiele2016subcellularlocalizationof pages 14-18, borkowsky2023phosphorylationoflkb1 pages 1-2).

Scope and limitations of evidence
- Direct phosphorylation of AMPK and Par-1 in Drosophila is supported by biochemical and genetic evidence; however, the relative contributions of other AMPK-related kinases (e.g., SIK, NUAK) remain incompletely quantified in each tissue and stage (Amin 2009; Thiele 2016) (amin2009lkb1regulatespolarity pages 1-1, thiele2016subcellularlocalizationof pages 18-21). 
- Hippo/Yorkie cross-talk is indicated in recent synthesis accompanying primary data; dedicated Drosophila in vivo dissection of this axis in 2023–2024 remains to be expanded (Borkowsky 2023) (borkowsky2023phosphorylationoflkb1 pages 1-2).

References with URLs and dates
- Amin et al., Lkb1 regulates polarity remodeling and adherens junction formation in the Drosophila eye. PNAS. Published online 2009-06-02. URL: https://doi.org/10.1073/pnas.0812469106 (amin2009lkb1regulatespolarity pages 1-1, amin2009lkb1regulatespolarity pages 6-6).
- Partanen et al., Breaking the epithelial polarity barrier in cancer: the strange case of LKB1/PAR-4. Phil. Trans. R. Soc. B. Published 2013-11-05. URL: https://doi.org/10.1098/rstb.2013.0111 (partanen2013breakingtheepithelial pages 4-4).
- Thiele, Subcellular localization of LKB1 and characterization of its interactions with the membrane skeleton in Drosophila melanogaster. Dissertation. 2016-01. URL: https://doi.org/10.5283/epub.31340 (thiele2016subcellularlocalizationof pages 14-18, thiele2016subcellularlocalizationof pages 18-21, thiele2016subcellularlocalizationof pages 21-24).
- Borkowsky et al., Phosphorylation of LKB1 by PDK1 inhibits cell proliferation and organ growth by decreased activation of AMPK. Cells. Published 2023-03-06. URL: https://doi.org/10.3390/cells12050812 (borkowsky2023phosphorylationoflkb1 pages 1-2, borkowsky2023phosphorylationoflkb1 pages 4-5, borkowsky2023phosphorylationoflkb1 pages 7-8).
- Trelford & Shepherd, LKB1 biology: assessing the therapeutic relevancy of LKB1 inhibitors. Cell Communication and Signaling. Published 2024-06-10. URL: https://doi.org/10.1186/s12964-024-01689-5 (trelford2024lkb1biologyassessing pages 15-16, trelford2024lkb1biologyassessing pages 4-5, trelford2024lkb1biologyassessing pages 1-2, trelford2024lkb1biologyassessing pages 16-17, trelford2024lkb1biologyassessing pages 2-4).

Conclusion
Drosophila Lkb1 (CG9374; STK11) is a conserved master serine/threonine kinase that activates AMPK-family kinases to coordinate polarity, division, and metabolic signaling. In flies, it directly activates AMPK and phosphorylates Par-1/MARK, and its active STRAD/MO25-bound complex localizes to cytoplasm and membranes to execute polarity programs in oocytes, epithelia, retina, and neuroblasts. Recent 2023 work identifies PDK1 as a direct inhibitory regulator of Lkb1 catalytic activity via T353 phosphorylation, linking PI3K–PDK1 cues to Lkb1–AMPK growth control in vivo. These mechanistic insights, together with 2024 synthesis on activation/localization, refine experimental strategies and therapeutic thinking about LKB1-pathway modulation across systems (amin2009lkb1regulatespolarity pages 1-1, thiele2016subcellularlocalizationof pages 18-21, thiele2016subcellularlocalizationof pages 14-18, borkowsky2023phosphorylationoflkb1 pages 1-2, trelford2024lkb1biologyassessing pages 4-5).

References

1. (partanen2013breakingtheepithelial pages 4-4): Johanna I. Partanen, Topi A. Tervonen, and Juha Klefström. Breaking the epithelial polarity barrier in cancer: the strange case of lkb1/par-4. Philosophical Transactions of the Royal Society B: Biological Sciences, 368:20130111, Nov 2013. URL: https://doi.org/10.1098/rstb.2013.0111, doi:10.1098/rstb.2013.0111. This article has 39 citations and is from a domain leading peer-reviewed journal.

2. (amin2009lkb1regulatespolarity pages 1-1): Nancy Amin, Afifa Khan, Daniel St. Johnston, Ian Tomlinson, Sophie Martin, Jay Brenman, and Helen McNeill. Lkb1 regulates polarity remodeling and adherens junction formation in the drosophila eye. Proceedings of the National Academy of Sciences, 106:8941-8946, Jun 2009. URL: https://doi.org/10.1073/pnas.0812469106, doi:10.1073/pnas.0812469106. This article has 76 citations and is from a highest quality peer-reviewed journal.

3. (thiele2016subcellularlocalizationof pages 14-18): Christian Volker Steffen Thiele. Subcellular localization of lkb1 and characterization of its interactions with the membrane skeleton in drosophila melanogaster. Text, Jan 2016. URL: https://doi.org/10.5283/epub.31340, doi:10.5283/epub.31340. This article has 0 citations and is from a peer-reviewed journal.

4. (trelford2024lkb1biologyassessing pages 15-16): Charles B. Trelford and Trevor G. Shepherd. Lkb1 biology: assessing the therapeutic relevancy of lkb1 inhibitors. Cell Communication and Signaling : CCS, Jun 2024. URL: https://doi.org/10.1186/s12964-024-01689-5, doi:10.1186/s12964-024-01689-5. This article has 22 citations.

5. (trelford2024lkb1biologyassessing pages 1-2): Charles B. Trelford and Trevor G. Shepherd. Lkb1 biology: assessing the therapeutic relevancy of lkb1 inhibitors. Cell Communication and Signaling : CCS, Jun 2024. URL: https://doi.org/10.1186/s12964-024-01689-5, doi:10.1186/s12964-024-01689-5. This article has 22 citations.

6. (trelford2024lkb1biologyassessing pages 2-4): Charles B. Trelford and Trevor G. Shepherd. Lkb1 biology: assessing the therapeutic relevancy of lkb1 inhibitors. Cell Communication and Signaling : CCS, Jun 2024. URL: https://doi.org/10.1186/s12964-024-01689-5, doi:10.1186/s12964-024-01689-5. This article has 22 citations.

7. (thiele2016subcellularlocalizationof pages 18-21): Christian Volker Steffen Thiele. Subcellular localization of lkb1 and characterization of its interactions with the membrane skeleton in drosophila melanogaster. Text, Jan 2016. URL: https://doi.org/10.5283/epub.31340, doi:10.5283/epub.31340. This article has 0 citations and is from a peer-reviewed journal.

8. (trelford2024lkb1biologyassessing pages 4-5): Charles B. Trelford and Trevor G. Shepherd. Lkb1 biology: assessing the therapeutic relevancy of lkb1 inhibitors. Cell Communication and Signaling : CCS, Jun 2024. URL: https://doi.org/10.1186/s12964-024-01689-5, doi:10.1186/s12964-024-01689-5. This article has 22 citations.

9. (thiele2016subcellularlocalizationof pages 21-24): Christian Volker Steffen Thiele. Subcellular localization of lkb1 and characterization of its interactions with the membrane skeleton in drosophila melanogaster. Text, Jan 2016. URL: https://doi.org/10.5283/epub.31340, doi:10.5283/epub.31340. This article has 0 citations and is from a peer-reviewed journal.

10. (borkowsky2023phosphorylationoflkb1 pages 1-2): S Borkowsky, M Gass, A Alavizargar, and J Hanewinkel. Phosphorylation of lkb1 by pdk1 inhibits cell proliferation and organ growth by decreased activation of ampk. cells 2023; 12: 812. Unknown journal, 2023.

11. (borkowsky2023phosphorylationoflkb1 pages 4-5): S Borkowsky, M Gass, A Alavizargar, and J Hanewinkel. Phosphorylation of lkb1 by pdk1 inhibits cell proliferation and organ growth by decreased activation of ampk. cells 2023; 12: 812. Unknown journal, 2023.

12. (borkowsky2023phosphorylationoflkb1 pages 7-8): S Borkowsky, M Gass, A Alavizargar, and J Hanewinkel. Phosphorylation of lkb1 by pdk1 inhibits cell proliferation and organ growth by decreased activation of ampk. cells 2023; 12: 812. Unknown journal, 2023.

13. (trelford2024lkb1biologyassessing pages 16-17): Charles B. Trelford and Trevor G. Shepherd. Lkb1 biology: assessing the therapeutic relevancy of lkb1 inhibitors. Cell Communication and Signaling : CCS, Jun 2024. URL: https://doi.org/10.1186/s12964-024-01689-5, doi:10.1186/s12964-024-01689-5. This article has 22 citations.

14. (amin2009lkb1regulatespolarity pages 6-6): Nancy Amin, Afifa Khan, Daniel St. Johnston, Ian Tomlinson, Sophie Martin, Jay Brenman, and Helen McNeill. Lkb1 regulates polarity remodeling and adherens junction formation in the drosophila eye. Proceedings of the National Academy of Sciences, 106:8941-8946, Jun 2009. URL: https://doi.org/10.1073/pnas.0812469106, doi:10.1073/pnas.0812469106. This article has 76 citations and is from a highest quality peer-reviewed journal.

## Citations

1. thiele2016subcellularlocalizationof pages 18-21
2. partanen2013breakingtheepithelial pages 4-4
3. thiele2016subcellularlocalizationof pages 14-18
4. thiele2016subcellularlocalizationof pages 21-24
5. https://doi.org/10.1073/pnas.0812469106;
6. https://doi.org/10.1098/rstb.2013.0111
7. https://doi.org/10.5283/epub.31340;
8. https://doi.org/10.1186/s12964-024-01689-5
9. https://doi.org/10.1186/s12964-024-01689-5;
10. https://doi.org/10.5283/epub.31340
11. https://doi.org/10.3390/cells12050812
12. https://doi.org/10.1073/pnas.0812469106
13. https://doi.org/10.1098/rstb.2013.0111;
14. https://doi.org/10.17879/90089628698
15. https://doi.org/10.17879/90089628698;
16. https://doi.org/10.1098/rstb.2013.0111,
17. https://doi.org/10.1073/pnas.0812469106,
18. https://doi.org/10.5283/epub.31340,
19. https://doi.org/10.1186/s12964-024-01689-5,