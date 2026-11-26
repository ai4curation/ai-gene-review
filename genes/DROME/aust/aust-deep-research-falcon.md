---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-10-09T18:54:08.801211'
end_time: '2026-10-09T19:09:39.312526'
duration_seconds: 930.51
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: DROME
  gene_id: aust
  gene_symbol: aust
  uniprot_accession: Q9VLD7
  protein_description: 'SubName: Full=Australin, isoform A {ECO:0000313|EMBL:AAF52756.1};
    SubName: Full=Australin, isoform B {ECO:0000313|EMBL:AHN54289.1};'
  gene_info: Name=aust {ECO:0000313|EMBL:AAF52756.1, ECO:0000313|FlyBase:FBgn0032104};
    Synonyms=Aust {ECO:0000313|EMBL:AAF52756.1}, Dmel\CG17009 {ECO:0000313|EMBL:AAF52756.1};
    ORFNames=CG17009 {ECO:0000313|EMBL:AAF52756.1, ECO:0000313|FlyBase:FBgn0032104},
    Dmel_CG17009 {ECO:0000313|EMBL:AAF52756.1};
  organism_full: Drosophila melanogaster (Fruit fly).
  protein_family: Belongs to the borealin family.
  protein_domains: Borealin_C. (IPR046466); Cell_div_borealin. (IPR018867); Borealin
    (PF10512)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 32
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 1
  edison_message_content: 1
artifacts:
- filename: artifact-00.md
  path: aust-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: image-1.png
  path: aust-deep-research-falcon_artifacts/image-1.png
  media_type: image/png
  source: edison_message_content
  data_storage_id: null
  description: '## Context ID: pqac-00000019 I have extracted the header row and the
    ''Australin'' row from Table 1 on page 189 (page 5 of the document). These images
    include the'
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q9VLD7
- **Protein Description:** SubName: Full=Australin, isoform A {ECO:0000313|EMBL:AAF52756.1}; SubName: Full=Australin, isoform B {ECO:0000313|EMBL:AHN54289.1};
- **Gene Information:** Name=aust {ECO:0000313|EMBL:AAF52756.1, ECO:0000313|FlyBase:FBgn0032104}; Synonyms=Aust {ECO:0000313|EMBL:AAF52756.1}, Dmel\CG17009 {ECO:0000313|EMBL:AAF52756.1}; ORFNames=CG17009 {ECO:0000313|EMBL:AAF52756.1, ECO:0000313|FlyBase:FBgn0032104}, Dmel_CG17009 {ECO:0000313|EMBL:AAF52756.1};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Belongs to the borealin family.
- **Key Domains:** Borealin_C. (IPR046466); Cell_div_borealin. (IPR018867); Borealin (PF10512)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "aust" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'aust' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **aust** (gene ID: aust, UniProt: Q9VLD7) in DROME.

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
- **UniProt Accession:** Q9VLD7
- **Protein Description:** SubName: Full=Australin, isoform A {ECO:0000313|EMBL:AAF52756.1}; SubName: Full=Australin, isoform B {ECO:0000313|EMBL:AHN54289.1};
- **Gene Information:** Name=aust {ECO:0000313|EMBL:AAF52756.1, ECO:0000313|FlyBase:FBgn0032104}; Synonyms=Aust {ECO:0000313|EMBL:AAF52756.1}, Dmel\CG17009 {ECO:0000313|EMBL:AAF52756.1}; ORFNames=CG17009 {ECO:0000313|EMBL:AAF52756.1, ECO:0000313|FlyBase:FBgn0032104}, Dmel_CG17009 {ECO:0000313|EMBL:AAF52756.1};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Belongs to the borealin family.
- **Key Domains:** Borealin_C. (IPR046466); Cell_div_borealin. (IPR018867); Borealin (PF10512)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "aust" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'aust' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **aust** (gene ID: aust, UniProt: Q9VLD7) in DROME.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Functional annotation of *Drosophila melanogaster* **aust** (Australin; UniProt Q9VLD7)

## Identity and principal function

The specified accession Q9VLD7 corresponds to *D. melanogaster* **aust/CG17009**, encoding **Australin (Aust)**. The supplied UniProt description assigns Borealin-family domains to the protein; fly-specific literature independently identifies Aust as a paralog of **Borealin-related (Borr)**, the fly’s canonical Borealin. **Aust and Borr are different proteins**, not interchangeable gene names. The gene symbol “aust” is therefore identifiable in this context, although literature specifically characterizing Aust is limited. (giansanti2012cytokinesisindrosophila pages 7-8, frappaolo2022microtubuleandactin pages 11-12)

**Primary functional annotation:** Aust is a **nonenzymatic, male-meiotic subunit of the chromosomal passenger complex (CPC)**. In dividing spermatocytes it replaces Borr in a complex whose other components are **Aurora B kinase, INCENP and Survivin/Deterin**. Its broader role is to support the CPC’s appropriately positioned activity during chromosome segregation and the transition to cytokinesis; **Aurora B, not Aust, is the kinase**. No catalytic reaction, transported substrate or ligand specificity should be assigned to Aust. The underlying Aust-specific genetics are principally attributed by subsequent reviews to Gao and colleagues’ 2008 study. (giansanti2012cytokinesisindrosophila pages 7-8, frappaolo2022microtubuleandactin pages 11-12, frappaolo2022microtubuleandactin pages 10-11)

| Finding | Supporting experiment/source, date, DOI | Evidence status |
|---|---|---|
| **Identity and family:** *D. melanogaster* **aust/CG17009** encodes Australin (UniProt Q9VLD7), a paralog of canonical fly Borealin-related (**Borr**) with Borealin-family domains. | The supplied UniProt record establishes the accession, gene and organism mapping. Drosophila reviews independently identify Aust as the Borr/Borealin paralog. Giansanti et al., August 2, 2012, [DOI 10.4161/spmg.21711](https://doi.org/10.4161/spmg.21711); Frappaolo et al., February 18, 2022, [DOI 10.3390/cells11040695](https://doi.org/10.3390/cells11040695) (giansanti2012cytokinesisindrosophila pages 7-8, frappaolo2022microtubuleandactin pages 11-12) | **High-confidence identity.** Database identity agrees with organism-specific literature. Aust must not be confused with Borr or similarly named genes in other organisms. |
| **Male-meiotic CPC role and localization:** Aust replaces Borr in the spermatocyte chromosomal passenger complex (CPC), whose other subunits are Aurora B, INCENP and Survivin/Deterin. Aust is reported at the central-spindle midzone during cytokinesis. | Drosophila-focused reviews summarize genetic and cytological work from Gao et al. Giansanti et al., August 2, 2012, [DOI 10.4161/spmg.21711](https://doi.org/10.4161/spmg.21711); Frappaolo et al., February 18, 2022, [DOI 10.3390/cells11040695](https://doi.org/10.3390/cells11040695) (giansanti2012cytokinesisindrosophila pages 4-6, frappaolo2022microtubuleandactin pages 11-12, sechi2013geneticdissectionof pages 25-36) | **Aust-specific finding reported in authoritative secondary sources.** Male-meiotic replacement and midzone localization are well supported, but generic CPC localization should not automatically be assigned to Aust without Aust-specific imaging. |
| **Chromosome functions:** *aust*-null spermatocytes show defects in sister-chromatid cohesion, chromosome alignment and segregation, whereas histone-H3 phosphorylation is reported to remain intact. | Findings are attributed to Gao et al., February 11, 2008, [DOI 10.1083/jcb.200708072](https://doi.org/10.1083/jcb.200708072), and summarized in later analyses (volpi2010…ofspermatogenesis pages 29-32) | **Aust-specific genetics and cytology reported in secondary sources.** The Gao et al. primary article was identified, but its full text was inaccessible through the research tool; therefore no numerical penetrance, sample size or unverified figure statistic is stated. |
| **Early cytokinesis:** Aust is required for central-spindle assembly and CPC positioning and for recruitment or maintenance of Pavarotti/MKLP1 (**Pav**), Fascetto/PRC1 (**Feo**) and anillin at the cell equator. *aust*-null spermatocytes consequently fail to assemble normal central spindles and actomyosin contractile rings. | Giansanti et al. list central-spindle-midzone localization, defective CPC localization and failed Pav, Feo and anillin recruitment; Frappaolo et al. confirm early arrest, defective central spindles and failure to recruit Pav. August 2, 2012, [DOI 10.4161/spmg.21711](https://doi.org/10.4161/spmg.21711); February 18, 2022, [DOI 10.3390/cells11040695](https://doi.org/10.3390/cells11040695) (giansanti2012cytokinesisindrosophila pages 4-6, frappaolo2022microtubuleandactin pages 11-12, giansanti2012cytokinesisindrosophila media d025ab38) | **Aust-specific loss-of-function phenotype reported in secondary reviews.** This supports a nonenzymatic CPC targeting or scaffolding role upstream of centralspindlin and contractile-ring assembly. Gao et al. penetrance values are not reproduced because the primary text was inaccessible. |
| **Aust–Borr/ESCRT-III hypothesis:** Aust lacks an approximately 140-residue central segment found in Borr. Canonical Borr directly binds the ESCRT-III Snf7 protein Shrub through a central region; Aust substitution may therefore prevent CPC–ESCRT-III coupling and help preserve incomplete male-germ-cell cytokinesis. | Capalbo et al., May 2012, used reciprocal affinity purification, mass spectrometry and GST pull-down to show direct Borr–Shrub association; Borr residues 118–249 were necessary but not sufficient for binding. [DOI 10.1098/rsob.120070](https://doi.org/10.1098/rsob.120070) (capalbo2012thechromosomalpassenger pages 3-4, capalbo2012thechromosomalpassenger pages 2-3). The Aust interpretation is proposed in Drosophila reviews (giansanti2012cytokinesisindrosophila pages 7-8, frappaolo2022microtubuleandactin pages 11-12) | **Borr–Shrub biochemistry is direct; the Aust mechanism is inferred.** Aust–Shrub nonbinding and causal control of incomplete male cytokinesis were not demonstrated directly. Human Borealin–CHMP4 and Aurora-B–CHMP4C results are not direct evidence about fly Aust (capalbo2012thechromosomalpassenger pages 1-2, capalbo2012thechromosomalpassenger pages 8-9, capalbo2012thechromosomalpassenger pages 4-5). |


*Table: Five-row evidence assessment for Drosophila melanogaster Australin (aust/CG17009; Q9VLD7), separating Aust-specific observations from general CPC biology and Borr- or human-based inference. It also flags the absence of verified quantitative data from the inaccessible Gao et al. primary text.*

## Biological processes and where Aust acts

**Chromosomes and spindle, before anaphase.** The CPC associates with chromatin before division and concentrates at chromosomes/inner centromeres as cells enter metaphase, where CPC-dependent regulation promotes chromosome alignment and appropriate kinetochore–microtubule interactions. Aust-deficient spermatocytes have reported defects in **sister-chromatid cohesion, chromosome alignment and segregation**. These findings support Aust’s importance for the meiotic chromosome functions of the CPC; they do **not** establish that Aust itself phosphorylates chromatin or directly recognizes a particular kinetochore substrate. A secondary account specifically notes that histone-H3 phosphorylation persists without Aust, cautioning against treating every Aurora-B-dependent output as Aust-dependent. The detailed chromatin-localization sequence is described for the **complex** and should not, without Aust-specific imaging, be interpreted as a map of every Aust molecule. (giansanti2012cytokinesisindrosophila pages 7-8, volpi2010…ofspermatogenesis pages 29-32, frappaolo2022microtubuleandactin pages 11-12)

**Central spindle and cell equator, from anaphase into cytokinesis.** The most clearly documented functional site for Australin is the **central-spindle midzone of male meiotic cells**, with CPC activity also associated with the equatorial cortex. The Aust entry in a Drosophila-specific cytokinesis review explicitly lists midzone localization, disrupted CPC positioning and failure to recruit **Pavarotti (Pav; the MKLP1 kinesin of centralspindlin)**, **Fascetto (Feo; a PRC1-related spindle protein)** and **anillin** in mutants. A later review likewise describes *aust*-null spermatocytes with defective central spindles, failure of Pav recruitment to the equator and early cytokinesis arrest. These are cellular, not extracellular, activities; the evidence does not support assigning Aust to a secretory compartment or describing it as a membrane-fission enzyme. (giansanti2012cytokinesisindrosophila pages 4-6, frappaolo2022microtubuleandactin pages 11-12, giansanti2012cytokinesisindrosophila media d025ab38)

A mechanistic interpretation connects these observations to the **CPC–centralspindlin–Rho1–actomyosin pathway**. Aurora-B-dependent CPC activity supports central-spindle organization and Pav/centralspindlin positioning; centralspindlin helps position the RhoGEF Pebble and local Rho1 activation, which organize the contractile ring. Aust loss disrupts the upstream CPC-associated organization, so both central-spindle formation and contractile-ring assembly fail. The complete chain includes interactions established for the wider cytokinesis machinery: it should **not** be read as proof that Aust binds Pav, Pebble, Rho1 or anillin directly. (giansanti2012cytokinesisindrosophila pages 7-8, giansanti2012cytokinesisindrosophila pages 4-6, frappaolo2022microtubuleandactin pages 11-12, frappaolo2022microtubuleandactin pages 10-11)

## What makes the male-meiotic protein distinctive?

Aust lacks a central segment corresponding to **approximately 140 amino acids of Borr**. Yet the 2012 Drosophila review reports that ectopically expressed Aust can substitute for Borr in cultured **S2 cells**, rescuing chromosome-alignment and cytokinesis defects. This supports conservation of core CPC function despite the structural difference; physiological replacement is described for **male meiosis**, not as a general claim that Aust performs Borr’s functions in every tissue. (giansanti2012cytokinesisindrosophila pages 7-8, frappaolo2022microtubuleandactin pages 11-12)

One proposed reason for the substitution concerns **ESCRT-III-dependent abscission**. In primary biochemical work on **Borr—not Aust**—Capalbo and colleagues found Borr and the ESCRT-III protein **Shrub (Shrb)** together by affinity purification and showed direct interaction using protein pull-downs. Their fragment tests found that **Borr residues 118–249 were necessary but not sufficient** for Shrb binding. Because Aust lacks the corresponding central region, reviews propose that an Aust-containing CPC might avoid this interaction, helping male germ cells complete furrow ingression **without abscission**, thereby retaining intercellular bridges. This explanation remains a **hypothesis about Aust**: Borr–Shrb binding was demonstrated, but the cited evidence does not demonstrate Aust–Shrb nonbinding or show that replacing Aust’s missing sequence changes male-meiotic abscission. Subsequent Shrub work in **female** germ cells informs abscission biology, but is not an Aust experiment. (giansanti2012cytokinesisindrosophila pages 7-8, frappaolo2022microtubuleandactin pages 11-12, capalbo2012thechromosomalpassenger pages 3-4, capalbo2012thechromosomalpassenger pages 2-3, matias2015abscissionisregulated pages 14-15)

The distinction matters because **normal incomplete cytokinesis is not the *aust*-null phenotype**. Normal fly male germ cells form persistent ring canals after furrowing; by contrast, Aust loss arrests cytokinesis early and prevents normal central-spindle and ring assembly. A contemporary review gives **64 interconnected spermatids per normal postmeiotic cyst**, a useful description of the biological setting—not a measured Aust-mutant penetrance. (frappaolo2022microtubuleandactin pages 14-16, frappaolo2022microtubuleandactin pages 11-12, frappaolo2022microtubuleandactin pages 8-10)

## Evidence strength, developments and applications

The most informative Aust-specific evidence is **fly mutant cytology and rescue**, summarized by the reviews above. Independent CPC biochemistry supports the broader interpretation of a Borealin-family positioning subunit: work on **canonical Borealin** identified a Borealin–Survivin–INCENP targeting module. That structural result helps explain the proposed role of Aust by homology but is **not** a direct demonstration of an Aust-specific binding interface. Likewise, human Borealin–CHMP4 experiments cannot be reported as fly Aust interactions. (giansanti2012cytokinesisindrosophila pages 7-8, frappaolo2022microtubuleandactin pages 11-12, klein2006centromeretargetingof pages 1-2, capalbo2012thechromosomalpassenger pages 1-2, capalbo2012thechromosomalpassenger pages 4-5)

**Recent-literature assessment:** Targeted searches did not retrieve a clearly Aust-specific **2023–2024** mechanistic paper. The relatively recent, directly pertinent synthesis is the **2022** review by Frappaolo and colleagues; the central Aust discovery remains the **2008** Gao study. The latter paper was identified but its full text was unavailable through the retrieval tools, so **Aust-mutant sample sizes, penetrance percentages and figure-specific effect estimates cannot be verified here**. The approximately 140-residue comparison above is a reported sequence difference, **not** a recent phenotype statistic. Present-day use is primarily **Drosophila male-meiosis research**: Aust mutants and spermatocyte imaging provide a way to interrogate CPC-dependent chromosome segregation, central-spindle organization and cytokinesis in a cell type where defects can be followed into anaphase. No Aust-specific clinical implementation is established by the sources examined. (giansanti2012cytokinesisindrosophila pages 7-8, frappaolo2022microtubuleandactin pages 11-12, frappaolo2022microtubuleandactin pages 8-10)

### Selected sources and dates

- **Gao S, et al.** “Australin: a chromosomal passenger protein required specifically for *Drosophila melanogaster* male meiosis.” *Journal of Cell Biology* **2008**, 180:521–535. **Primary Aust study**, identified but not available for full-text verification in this search. https://doi.org/10.1083/jcb.200708072. Its findings are discussed in the retrieved fly-specific reviews. (giansanti2012cytokinesisindrosophila pages 7-8, frappaolo2022microtubuleandactin pages 11-12)
- **Frappaolo A, Piergentili R, Giansanti MG.** “Microtubule and Actin Cytoskeletal Dynamics in Male Meiotic Cells of *Drosophila melanogaster*.” *Cells* **February 2022**, 11:695. **Recent fly-specific review.** https://doi.org/10.3390/cells11040695. (frappaolo2022microtubuleandactin pages 11-12, frappaolo2022microtubuleandactin pages 10-11)
- **Giansanti MG, et al.** “Cytokinesis in *Drosophila* male meiosis.” *Spermatogenesis* **July–September 2012**, 2:185–196. **Fly-specific review with an Australin localization/mutant-phenotype table.** https://doi.org/10.4161/spmg.21711. (giansanti2012cytokinesisindrosophila pages 7-8, giansanti2012cytokinesisindrosophila pages 4-6, giansanti2012cytokinesisindrosophila media d025ab38)
- **Capalbo L, et al.** “The chromosomal passenger complex controls the function of endosomal sorting complex required for transport-III Snf7 proteins during cytokinesis.” *Open Biology* **May 2012**, 2:120070. **Primary Borr–Shrub biochemistry; not an Aust binding experiment.** https://doi.org/10.1098/rsob.120070. (capalbo2012thechromosomalpassenger pages 1-2, capalbo2012thechromosomalpassenger pages 3-4, capalbo2012thechromosomalpassenger pages 2-3)
- **Klein UR, Nigg EA, Gruneberg U.** “Centromere targeting of the chromosomal passenger complex requires a ternary subcomplex of Borealin, Survivin, and the N-terminal domain of INCENP.” *Molecular Biology of the Cell* **June 2006**, 17:2547–2558. **CPC mechanism from non-Aust experiments.** https://doi.org/10.1091/mbc.e05-12-1133. (klein2006centromeretargetingof pages 1-2)

References

1. (giansanti2012cytokinesisindrosophila pages 7-8): Maria Grazia Giansanti, Stefano Sechi, Anna Frappaolo, Giorgio Belloni, and Roberto Piergentili. Cytokinesis in drosophila male meiosis. Spermatogenesis, 2:185-196, Jul 2012. URL: https://doi.org/10.4161/spmg.21711, doi:10.4161/spmg.21711. This article has 30 citations and is from a peer-reviewed journal.

2. (frappaolo2022microtubuleandactin pages 11-12): Anna Frappaolo, Roberto Piergentili, and Maria Grazia Giansanti. Microtubule and actin cytoskeletal dynamics in male meiotic cells of drosophila melanogaster. Cells, 11:695, Feb 2022. URL: https://doi.org/10.3390/cells11040695, doi:10.3390/cells11040695. This article has 16 citations.

3. (frappaolo2022microtubuleandactin pages 10-11): Anna Frappaolo, Roberto Piergentili, and Maria Grazia Giansanti. Microtubule and actin cytoskeletal dynamics in male meiotic cells of drosophila melanogaster. Cells, 11:695, Feb 2022. URL: https://doi.org/10.3390/cells11040695, doi:10.3390/cells11040695. This article has 16 citations.

4. (giansanti2012cytokinesisindrosophila pages 4-6): Maria Grazia Giansanti, Stefano Sechi, Anna Frappaolo, Giorgio Belloni, and Roberto Piergentili. Cytokinesis in drosophila male meiosis. Spermatogenesis, 2:185-196, Jul 2012. URL: https://doi.org/10.4161/spmg.21711, doi:10.4161/spmg.21711. This article has 30 citations and is from a peer-reviewed journal.

5. (sechi2013geneticdissectionof pages 25-36): S Sechi. Genetic dissection of meiotic cytokinesis in drosophila melanogaster males. Unknown journal, 2013.

6. (volpi2010…ofspermatogenesis pages 29-32): S Volpi. … of spermatogenesis in drosophila melanogaster: genetic, cytological and molecular characterization of a set of male-sterile mutants involved in meiotic cell …. Unknown journal, 2010.

7. (giansanti2012cytokinesisindrosophila media d025ab38): Maria Grazia Giansanti, Stefano Sechi, Anna Frappaolo, Giorgio Belloni, and Roberto Piergentili. Cytokinesis in drosophila male meiosis. Spermatogenesis, 2:185-196, Jul 2012. URL: https://doi.org/10.4161/spmg.21711, doi:10.4161/spmg.21711. This article has 30 citations and is from a peer-reviewed journal.

8. (capalbo2012thechromosomalpassenger pages 3-4): Luisa Capalbo, Emilie Montembault, Tetsuya Takeda, Zuni I. Bassi, David M. Glover, and Pier Paolo D'Avino. The chromosomal passenger complex controls the function of endosomal sorting complex required for transport-iii snf7 proteins during cytokinesis. Open Biology, 2:120070, May 2012. URL: https://doi.org/10.1098/rsob.120070, doi:10.1098/rsob.120070. This article has 155 citations and is from a peer-reviewed journal.

9. (capalbo2012thechromosomalpassenger pages 2-3): Luisa Capalbo, Emilie Montembault, Tetsuya Takeda, Zuni I. Bassi, David M. Glover, and Pier Paolo D'Avino. The chromosomal passenger complex controls the function of endosomal sorting complex required for transport-iii snf7 proteins during cytokinesis. Open Biology, 2:120070, May 2012. URL: https://doi.org/10.1098/rsob.120070, doi:10.1098/rsob.120070. This article has 155 citations and is from a peer-reviewed journal.

10. (capalbo2012thechromosomalpassenger pages 1-2): Luisa Capalbo, Emilie Montembault, Tetsuya Takeda, Zuni I. Bassi, David M. Glover, and Pier Paolo D'Avino. The chromosomal passenger complex controls the function of endosomal sorting complex required for transport-iii snf7 proteins during cytokinesis. Open Biology, 2:120070, May 2012. URL: https://doi.org/10.1098/rsob.120070, doi:10.1098/rsob.120070. This article has 155 citations and is from a peer-reviewed journal.

11. (capalbo2012thechromosomalpassenger pages 8-9): Luisa Capalbo, Emilie Montembault, Tetsuya Takeda, Zuni I. Bassi, David M. Glover, and Pier Paolo D'Avino. The chromosomal passenger complex controls the function of endosomal sorting complex required for transport-iii snf7 proteins during cytokinesis. Open Biology, 2:120070, May 2012. URL: https://doi.org/10.1098/rsob.120070, doi:10.1098/rsob.120070. This article has 155 citations and is from a peer-reviewed journal.

12. (capalbo2012thechromosomalpassenger pages 4-5): Luisa Capalbo, Emilie Montembault, Tetsuya Takeda, Zuni I. Bassi, David M. Glover, and Pier Paolo D'Avino. The chromosomal passenger complex controls the function of endosomal sorting complex required for transport-iii snf7 proteins during cytokinesis. Open Biology, 2:120070, May 2012. URL: https://doi.org/10.1098/rsob.120070, doi:10.1098/rsob.120070. This article has 155 citations and is from a peer-reviewed journal.

13. (matias2015abscissionisregulated pages 14-15): Neuza Reis Matias, Juliette Mathieu, and Jean-René Huynh. Abscission is regulated by the escrt-iii protein shrub in drosophila germline stem cells. PLOS Genetics, 11:e1004653, Feb 2015. URL: https://doi.org/10.1371/journal.pgen.1004653, doi:10.1371/journal.pgen.1004653. This article has 86 citations and is from a domain leading peer-reviewed journal.

14. (frappaolo2022microtubuleandactin pages 14-16): Anna Frappaolo, Roberto Piergentili, and Maria Grazia Giansanti. Microtubule and actin cytoskeletal dynamics in male meiotic cells of drosophila melanogaster. Cells, 11:695, Feb 2022. URL: https://doi.org/10.3390/cells11040695, doi:10.3390/cells11040695. This article has 16 citations.

15. (frappaolo2022microtubuleandactin pages 8-10): Anna Frappaolo, Roberto Piergentili, and Maria Grazia Giansanti. Microtubule and actin cytoskeletal dynamics in male meiotic cells of drosophila melanogaster. Cells, 11:695, Feb 2022. URL: https://doi.org/10.3390/cells11040695, doi:10.3390/cells11040695. This article has 16 citations.

16. (klein2006centromeretargetingof pages 1-2): Ulf R. Klein, Erich A. Nigg, and Ulrike Gruneberg. Centromere targeting of the chromosomal passenger complex requires a ternary subcomplex of borealin, survivin, and the n-terminal domain of incenp. Molecular biology of the cell, 17 6:2547-58, Jun 2006. URL: https://doi.org/10.1091/mbc.e05-12-1133, doi:10.1091/mbc.e05-12-1133. This article has 239 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](aust-deep-research-falcon_artifacts/artifact-00.md)
![## Context ID: pqac-00000019 I have extracted the header row and the 'Australin' row from Table 1 on page 189 (page 5 of the document). These images include the](aust-deep-research-falcon_artifacts/image-1.png)

## Citations

1. klein2006centromeretargetingof pages 1-2
2. giansanti2012cytokinesisindrosophila pages 7-8
3. frappaolo2022microtubuleandactin pages 11-12
4. frappaolo2022microtubuleandactin pages 10-11
5. giansanti2012cytokinesisindrosophila pages 4-6
6. sechi2013geneticdissectionof pages 25-36
7. capalbo2012thechromosomalpassenger pages 3-4
8. capalbo2012thechromosomalpassenger pages 2-3
9. capalbo2012thechromosomalpassenger pages 1-2
10. capalbo2012thechromosomalpassenger pages 8-9
11. capalbo2012thechromosomalpassenger pages 4-5
12. matias2015abscissionisregulated pages 14-15
13. frappaolo2022microtubuleandactin pages 14-16
14. frappaolo2022microtubuleandactin pages 8-10
15. DOI 10.4161/spmg.21711
16. DOI 10.3390/cells11040695
17. DOI 10.1083/jcb.200708072
18. DOI 10.1098/rsob.120070
19. https://doi.org/10.4161/spmg.21711
20. https://doi.org/10.3390/cells11040695
21. https://doi.org/10.1083/jcb.200708072
22. https://doi.org/10.1098/rsob.120070
23. https://doi.org/10.1083/jcb.200708072.
24. https://doi.org/10.3390/cells11040695.
25. https://doi.org/10.4161/spmg.21711.
26. https://doi.org/10.1098/rsob.120070.
27. https://doi.org/10.1091/mbc.e05-12-1133.
28. https://doi.org/10.4161/spmg.21711,
29. https://doi.org/10.3390/cells11040695,
30. https://doi.org/10.1098/rsob.120070,
31. https://doi.org/10.1371/journal.pgen.1004653,
32. https://doi.org/10.1091/mbc.e05-12-1133,