---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-10-09T18:44:02.017818'
end_time: '2026-10-09T18:59:43.462705'
duration_seconds: 941.44
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: DROME
  gene_id: Det
  gene_symbol: Det
  uniprot_accession: Q9VEM2
  protein_description: 'SubName: Full=Deterin {ECO:0000313|EMBL:AAF55399.1};'
  gene_info: Name=Det {ECO:0000313|EMBL:AAF55399.1, ECO:0000313|FlyBase:FBgn0264291};
    Synonyms=det {ECO:0000313|EMBL:AAF55399.1}, Dmel\CG12265 {ECO:0000313|EMBL:AAF55399.1},
    scpo {ECO:0000313|EMBL:AAF55399.1}, svn {ECO:0000313|EMBL:AAF55399.1}; ORFNames=CG12265
    {ECO:0000313|EMBL:AAF55399.1, ECO:0000313|FlyBase:FBgn0264291}, Dmel_CG12265 {ECO:0000313|EMBL:AAF55399.1};
  organism_full: Drosophila melanogaster (Fruit fly).
  protein_family: Belongs to the IAP family. .
  protein_domains: Baculoviral_IAP. (IPR051190); BIR_rpt. (IPR001370); BIR (PF00653)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 40
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Det-deep-research-falcon_artifacts/artifact-00.md
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
- **UniProt Accession:** Q9VEM2
- **Protein Description:** SubName: Full=Deterin {ECO:0000313|EMBL:AAF55399.1};
- **Gene Information:** Name=Det {ECO:0000313|EMBL:AAF55399.1, ECO:0000313|FlyBase:FBgn0264291}; Synonyms=det {ECO:0000313|EMBL:AAF55399.1}, Dmel\CG12265 {ECO:0000313|EMBL:AAF55399.1}, scpo {ECO:0000313|EMBL:AAF55399.1}, svn {ECO:0000313|EMBL:AAF55399.1}; ORFNames=CG12265 {ECO:0000313|EMBL:AAF55399.1, ECO:0000313|FlyBase:FBgn0264291}, Dmel_CG12265 {ECO:0000313|EMBL:AAF55399.1};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Belongs to the IAP family. .
- **Key Domains:** Baculoviral_IAP. (IPR051190); BIR_rpt. (IPR001370); BIR (PF00653)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "Det" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'Det' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **Det** (gene ID: Det, UniProt: Q9VEM2) in DROME.

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
- **UniProt Accession:** Q9VEM2
- **Protein Description:** SubName: Full=Deterin {ECO:0000313|EMBL:AAF55399.1};
- **Gene Information:** Name=Det {ECO:0000313|EMBL:AAF55399.1, ECO:0000313|FlyBase:FBgn0264291}; Synonyms=det {ECO:0000313|EMBL:AAF55399.1}, Dmel\CG12265 {ECO:0000313|EMBL:AAF55399.1}, scpo {ECO:0000313|EMBL:AAF55399.1}, svn {ECO:0000313|EMBL:AAF55399.1}; ORFNames=CG12265 {ECO:0000313|EMBL:AAF55399.1, ECO:0000313|FlyBase:FBgn0264291}, Dmel_CG12265 {ECO:0000313|EMBL:AAF55399.1};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Belongs to the IAP family. .
- **Key Domains:** Baculoviral_IAP. (IPR051190); BIR_rpt. (IPR001370); BIR (PF00653)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "Det" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'Det' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **Det** (gene ID: Det, UniProt: Q9VEM2) in DROME.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Functional annotation of *Drosophila melanogaster* Det (Deterin; UniProt Q9VEM2)

## Identity and principal function

**Det is the fruit-fly gene encoding Deterin, also called Drosophila Survivin.** The supplied UniProt identity links Det to **CG12265** and the aliases *scpo* and *svn*; fly-specific studies independently identify *scapolo* (*scpo*) as a *deterin* allele and describe Deterin as the fly Survivin protein. Its baculoviral inhibitor-of-apoptosis repeat (**BIR**) is consistent with its IAP-family classification. Human Survivin/BIRC5 is a related protein, **not** the gene annotated here. (frappaolo2022microtubuleandactin pages 11-12, wang2020oocytespindleassembly pages 1-5, wang2020oocytespindleassembly pages 5-8)

The strongest physiological annotation is **nonenzymatic regulation of chromosome segregation and cell division as a targeting component of the chromosomal passenger complex (CPC)**. Deterin participates with INCENP, Borealin (or the male-meiotic Borealin paralog Australin), and **Aurora B**, the complex’s catalytic kinase. The CPC changes position during division to coordinate chromosome-associated events, spindle organization, and cytokinesis. Deterin is therefore not itself an enzyme, transporter, or demonstrated kinase substrate-processing protein; its best-supported role is to help position a signaling complex so that Aurora B can act at the appropriate cellular site. (frappaolo2022microtubuleandactin pages 11-12, wang2020oocytespindleassembly pages 1-5)

The evidence below separates experiments on fly Deterin from results obtained by altering other CPC members or by studying human Survivin.

| System/date and source | Direct perturbation or measurement | Biological conclusion | Important limitation |
|---|---|---|---|
| Male spermatocytes and larval neuroblasts; **scapolo (scpo), 2011**, summarized in 2012 and 2022 reviews ([DOI](https://doi.org/10.1091/mbc.e11-06-0569)) | Endogenous **Det/Deterin P86S** substitution in its BIR domain; CPC function persisted until anaphase onset, but Det/CPC and Pavarotti failed to concentrate at the central spindle and equatorial cortex. Spermatocytes also failed to recruit Polo and Rho1 correctly. | Det is a **noncatalytic CPC targeting adaptor** required during anaphase and cytokinesis for central-spindle assembly, centralspindlin positioning, and Rho1-dependent contractile-ring organization. **Aurora B**, not Det, is the CPC kinase; **Polo** is a separate kinase. | Separation-of-function allele rather than a null; downstream defects do not prove direct Det binding to Polo, Rho1, or Pavarotti. Review summaries support the unavailable primary text. (frappaolo2022microtubuleandactin pages 11-12, giansanti2012cytokinesisindrosophila pages 7-8) |
| Asymmetrically dividing larval neuroblasts; **2015** ([DOI](https://doi.org/10.1038/ncomms7551)) | Live imaging and photoconversion showed that kinetochore Det supplied later central-spindle and furrow pools (**20/20 cells**). Det appeared at the spindle center at mean **172 s** after anaphase onset (*n*=9) and shifted basally at mean **297 s** (*n*=9). Following spindle disruption, Det remained on chromatin and failed to reach the poles, central spindle, cortex, or furrow in **25/25 cells**. | Det is a microtubule-dependent chromosomal passenger that relocates from chromosomes or kinetochores to central-spindle microtubules and the ingressing furrow, where the Det-dependent pathway stabilizes furrow position and supports completion of constriction. | Localization establishes pathway dependence, not enzymatic activity; the experiments do not demonstrate direct Det binding to microtubules or contractile-ring proteins. (roth2015asymmetricallydividingdrosophila pages 4-4) |
| Stage-14 oocytes; **2021 preprint version** ([DOI](https://doi.org/10.1101/2020.06.03.132142)) | Oocyte-specific Det shRNA reduced Det transcript to **5% of control**. Depleted oocytes phenocopied *Incenp* or *aurB* RNAi with defective spindle and kinetochore assembly; an INCENP N-terminal deletion failed to recruit Det or promote spindle assembly. | Det helps target or stabilize the INCENP–Aurora B CPC on oocyte chromosomes, enabling kinetochore recruitment and chromosome-directed acentrosomal spindle assembly. | Preprint evidence; residual Det protein was not quantified. Some mechanistic conclusions derive from INCENP constructs or other CPC perturbations rather than Det depletion alone. Det is a targeting subunit, not the Aurora B catalyst. (wang2020oocytespindleassembly pages 1-5, wang2020oocytespindleassembly pages 28-31, wang2020oocytespindleassembly pages 5-8) |
| *Drosophila* Kc cells; **2001** ([DOI](https://doi.org/10.1002/jcb.1228)) | Human caspase-7 expression induced death; coexpression of full-length Det reduced apoptotic death by approximately **one-half**. A Det-BIR/human-Survivin-C-terminal chimera produced a similar reduction. Det also partially rescued human Survivin-depleted HeLa cells. | Overexpressed Det can suppress caspase-dependent apoptosis in cultured cells, and its BIR-containing region contributes to this activity. | Heterologous overexpression assay using **human caspase-7**; no purified-enzyme, direct-binding, or endogenous fly loss-of-function evidence establishes Det as a direct caspase inhibitor. (jiang2001participationofsurvivin pages 7-10, jiang2001participationofsurvivin pages 1-2) |
| *Drosophila* S2 cells; **2016** ([DOI](https://doi.org/10.1091/mbc.e15-07-0467)) | Genome-scale RNAi and genetic-interaction profiling based on nuclear area placed **Det** with Rho1 and established cytokinesis genes, including *tum*, *ial*, *lin19*, and *zip*. | Systems-level evidence assigns Det to the cytokinesis network and is consistent with its CPC-dependent role upstream of equatorial Rho1 and actomyosin organization. | High-throughput functional association rather than a direct physical interaction or detailed Det-specific mechanism; lower evidentiary weight than scpo genetics and live imaging. (billmann2016ageneticinteraction pages 7-9) |


*Table: Direct and supporting evidence for Drosophila melanogaster Det/Deterin (Q9VEM2), emphasizing its noncatalytic CPC-targeting role and the more limited evidence for anti-apoptotic activity. No verified Det-specific 2023–2024 study was identified.*

## Mechanism and biological pathways

**Anaphase and cytokinesis.** The particularly informative fly allele *scpo* changes **Pro86 to Ser within Deterin’s BIR domain**. It is a separation-of-function allele: CPC recruitment and activity persist until anaphase onset, whereas later CPC and Pavarotti (**Pav**, a centralspindlin component) fail to concentrate properly at the central spindle and equatorial cortex. The resulting defects implicate Deterin in central-spindle assembly, placement of cytokinetic machinery, and completion of cell cleavage rather than solely in earlier chromosome events. Because this is a missense allele, its phenotype should not be equated with complete absence of Deterin. The 2011 primary report is [Szafer-Glusman, Fuller and Giansanti, *Molecular Biology of the Cell*, October 2011](https://doi.org/10.1091/mbc.e11-06-0569); the allele findings cited here are corroborated by accessible [2012](https://doi.org/10.4161/spmg.21711) and [2022](https://doi.org/10.3390/cells11040695) fly-meiosis reviews. (giansanti2012cytokinesisindrosophila pages 6-7, frappaolo2022microtubuleandactin pages 11-12, giansanti2012cytokinesisindrosophila pages 7-8)

The downstream consequences differ by cell type. In *scpo* spermatocytes, Polo kinase and the small GTPase Rho1 fail to localize correctly to the equator. In mutant larval neuroblasts, Polo, Rho1, and myosin II can initially form a **broad** equatorial band, but that band fails to narrow into a functional contractile ring. This distinction supports a Deterin/CPC-dependent, spindle-coupled pathway for robust furrow positioning and constriction while allowing an additional, polarity-associated early positioning pathway in neuroblasts. A proposed route from Polo-dependent centralspindlin regulation through Pebble/RhoGEF to Rho1 activation is mechanistically plausible, **not** proof that Deterin binds Polo, Pebble, or Rho1 directly. (frappaolo2022microtubuleandactin pages 11-12, frappaolo2022microtubuleandactin pages 10-11, giansanti2012cytokinesisindrosophila pages 7-8)

**Oocyte meiosis.** Deterin also contributes to chromosome-directed assembly of the **acentrosomal** meiotic spindle. In an oocyte RNAi experiment, Deterin transcript fell to approximately **5% of control**, and spindle and kinetochore assembly were defective, resembling *Incenp* or *aurB* depletion. Altering INCENP’s N-terminal region prevented Deterin recruitment and spindle assembly, consistent with a Deterin–INCENP targeting function. This evidence comes from Wang and colleagues’ [preprint, initially posted 2020 and revised January 17, 2021](https://doi.org/10.1101/2020.06.03.132142); the 5% figure measures **RNA**, not residual Deterin protein. Results obtained by modifying Borealin, INCENP, HP1, or Subito provide CPC-pathway context but must not be mistaken for independent Det-specific perturbations. (wang2020oocytespindleassembly pages 1-5, wang2020oocytespindleassembly pages 28-31, wang2020oocytespindleassembly pages 5-8)

**Apoptosis: demonstrated capacity, less-established physiological mechanism.** Deterin was originally described as an apoptosis inhibitor by [Jones and colleagues, *Journal of Biological Chemistry*, July 2000](https://doi.org/10.1074/jbc.m000369200). An independently accessible [2001 primary study](https://doi.org/10.1002/jcb.1228) expressed **human caspase-7 in fly Kc cells**: coexpressed Deterin reduced apoptotic death by approximately **one-half**, as did a construct containing Deterin’s BIR region joined to the human Survivin C terminus. Deterin also partially protected human HeLa cells following depletion of human Survivin. These are functional, partly cross-species **overexpression** assays. They do **not** establish direct binding to, or direct enzymatic inhibition of, a fly caspase; nor do they establish that apoptosis suppression is Deterin’s dominant endogenous function. An authoritative [2009 review](https://doi.org/10.4161/fly.3.1.7800) accordingly noted that its endogenous apoptotic role had not then been resolved by mutant analysis. (xu2009geneticcontrolof pages 12-13, jiang2001participationofsurvivin pages 1-2, jiang2001participationofsurvivin pages 7-10)

## Where Deterin acts

Deterin’s localization is **cell-cycle dependent**, not a single fixed compartment. In dividing fly neuroblasts, chromosome/kinetochore-associated Deterin supplies later **central-spindle microtubule** and **equatorial cortical/cleavage-furrow** pools. Photoconversion tracked this redistribution in **20 of 20 cells**. Deterin appeared near the spindle center a mean **172 seconds** after anaphase onset (*n* = 9), then shifted toward the basal furrow region at a mean **297 seconds** (*n* = 9). When microtubules were disrupted, it remained chromosome-associated and failed to reach the spindle or furrow in **25 of 25** examined cells. These observations place its experimentally demonstrated cytokinetic action **inside the cell**, at chromosomes and the spindle–furrow interface, and show that redistribution depends on the spindle. They do not, alone, demonstrate direct microtubule binding. [Roth and colleagues, *Nature Communications*, March 2015](https://doi.org/10.1038/ncomms7551). (roth2015asymmetricallydividingdrosophila pages 4-4)

Localization in oocytes requires an additional qualification: the CPC is often most prominent on the **meiotic central spindle** during prometaphase I, rather than displaying an unqualified somatic-cell centromere pattern. Its recruitment to oocyte chromosomes and subsequent movement onto spindle microtubules underlie the proposed spindle-assembly mechanism. Human-cell images of Survivin at centrosomes or midbodies are **not** direct localization measurements of fly Deterin. (wang2020oocytespindleassembly pages 1-5, wang2020oocytespindleassembly pages 5-8, jiang2001participationofsurvivin pages 4-7)

## Current research and use

The clearest later Det-specific work located in this search comprises fly **neuroblast live imaging**, **oocyte-specific knockdown**, and **genetic-interaction profiling**. The latter placed Det alongside Rho1 and established cytokinesis regulators in a Drosophila S2-cell nuclear-area interaction network—useful independent support for pathway assignment, but weaker mechanistic evidence than the *scpo* allele and imaging experiments. [Billmann and colleagues, *Molecular Biology of the Cell*, April 2016](https://doi.org/10.1091/mbc.e15-07-0467). These studies are real-world research implementations of Det genetics and microscopy, **not** evidence of an approved Det-directed therapy or industrial application. (roth2015asymmetricallydividingdrosophila pages 4-4, billmann2016ageneticinteraction pages 7-9, wang2020oocytespindleassembly pages 5-8)

A targeted search **did not identify a verifiable 2023–2024 primary study specifically resolving Drosophila Det mechanism**. The most recent directly applicable synthesis retrieved was [Frappaolo, Piergentili and Giansanti, *Cells*, February 2022](https://doi.org/10.3390/cells11040695); the oocyte result above remains identified here by its accessible preprint version. Thus, a 2023–2024 claim about this particular gene would be less reliable than the older, experimentally specific fly literature. (frappaolo2022microtubuleandactin pages 11-12, wang2020oocytespindleassembly pages 1-5)

**Annotation conclusion.** For Q9VEM2, the high-confidence functional description is *intracellular BIR-domain CPC targeting/organizing protein required for chromosome-associated spindle processes and, especially, anaphase central-spindle and cleavage-furrow organization*. Antiapoptotic activity is experimentally observable in cultured-cell expression assays, but **direct caspase inhibition, its endogenous substrate specificity, and the relative importance of this activity in vivo remain unestablished by the cited evidence**. (roth2015asymmetricallydividingdrosophila pages 4-4, frappaolo2022microtubuleandactin pages 11-12, jiang2001participationofsurvivin pages 7-10, wang2020oocytespindleassembly pages 5-8)

References

1. (frappaolo2022microtubuleandactin pages 11-12): Anna Frappaolo, Roberto Piergentili, and Maria Grazia Giansanti. Microtubule and actin cytoskeletal dynamics in male meiotic cells of drosophila melanogaster. Cells, 11:695, Feb 2022. URL: https://doi.org/10.3390/cells11040695, doi:10.3390/cells11040695. This article has 16 citations.

2. (wang2020oocytespindleassembly pages 1-5): Lin-Ing Wang, Tyler DeFosse, Janet K. Jang, Rachel A. Battaglia, Victoria F. Wagner, and Kim S. McKim. Oocyte spindle assembly depends on multiple interactions between hp1 and the cpc. bioRxiv, Jun 2020. URL: https://doi.org/10.1101/2020.06.03.132142, doi:10.1101/2020.06.03.132142. This article has 1 citations.

3. (wang2020oocytespindleassembly pages 5-8): Lin-Ing Wang, Tyler DeFosse, Janet K. Jang, Rachel A. Battaglia, Victoria F. Wagner, and Kim S. McKim. Oocyte spindle assembly depends on multiple interactions between hp1 and the cpc. bioRxiv, Jun 2020. URL: https://doi.org/10.1101/2020.06.03.132142, doi:10.1101/2020.06.03.132142. This article has 1 citations.

4. (giansanti2012cytokinesisindrosophila pages 7-8): Maria Grazia Giansanti, Stefano Sechi, Anna Frappaolo, Giorgio Belloni, and Roberto Piergentili. Cytokinesis in drosophila male meiosis. Spermatogenesis, 2:185-196, Jul 2012. URL: https://doi.org/10.4161/spmg.21711, doi:10.4161/spmg.21711. This article has 30 citations and is from a peer-reviewed journal.

5. (roth2015asymmetricallydividingdrosophila pages 4-4): Michaela Roth, Chantal Roubinet, Niklas Iffländer, Alexia Ferrand, and Clemens Cabernard. Asymmetrically dividing drosophila neuroblasts utilize two spatially and temporally independent cytokinesis pathways. Nature Communications, Mar 2015. URL: https://doi.org/10.1038/ncomms7551, doi:10.1038/ncomms7551. This article has 42 citations and is from a highest quality peer-reviewed journal.

6. (wang2020oocytespindleassembly pages 28-31): Lin-Ing Wang, Tyler DeFosse, Janet K. Jang, Rachel A. Battaglia, Victoria F. Wagner, and Kim S. McKim. Oocyte spindle assembly depends on multiple interactions between hp1 and the cpc. bioRxiv, Jun 2020. URL: https://doi.org/10.1101/2020.06.03.132142, doi:10.1101/2020.06.03.132142. This article has 1 citations.

7. (jiang2001participationofsurvivin pages 7-10): Xiuyun Jiang, Casey Wilford, Stephan Duensing, Karl Munger, Grace Jones, and Davy Jones. Participation of survivin in mitotic and apoptotic activities of normal and tumor‐derived cells *. Journal of Cellular Biochemistry, 83:342-354, Jan 2001. URL: https://doi.org/10.1002/jcb.1228, doi:10.1002/jcb.1228. This article has 121 citations and is from a peer-reviewed journal.

8. (jiang2001participationofsurvivin pages 1-2): Xiuyun Jiang, Casey Wilford, Stephan Duensing, Karl Munger, Grace Jones, and Davy Jones. Participation of survivin in mitotic and apoptotic activities of normal and tumor‐derived cells *. Journal of Cellular Biochemistry, 83:342-354, Jan 2001. URL: https://doi.org/10.1002/jcb.1228, doi:10.1002/jcb.1228. This article has 121 citations and is from a peer-reviewed journal.

9. (billmann2016ageneticinteraction pages 7-9): Maximilian Billmann, Thomas Horn, Bernd Fischer, Thomas Sandmann, Wolfgang Huber, and Michael Boutros. A genetic interaction map of cell cycle regulators. Molecular Biology of the Cell, 27:1397-1407, Apr 2016. URL: https://doi.org/10.1091/mbc.e15-07-0467, doi:10.1091/mbc.e15-07-0467. This article has 34 citations and is from a domain leading peer-reviewed journal.

10. (giansanti2012cytokinesisindrosophila pages 6-7): Maria Grazia Giansanti, Stefano Sechi, Anna Frappaolo, Giorgio Belloni, and Roberto Piergentili. Cytokinesis in drosophila male meiosis. Spermatogenesis, 2:185-196, Jul 2012. URL: https://doi.org/10.4161/spmg.21711, doi:10.4161/spmg.21711. This article has 30 citations and is from a peer-reviewed journal.

11. (frappaolo2022microtubuleandactin pages 10-11): Anna Frappaolo, Roberto Piergentili, and Maria Grazia Giansanti. Microtubule and actin cytoskeletal dynamics in male meiotic cells of drosophila melanogaster. Cells, 11:695, Feb 2022. URL: https://doi.org/10.3390/cells11040695, doi:10.3390/cells11040695. This article has 16 citations.

12. (xu2009geneticcontrolof pages 12-13): Dongbin Xu, Sarah E. Woodfield, Tom V. Lee, Yun Fan, Christian Antonio, and Andreas Bergmann. Genetic control of programmed cell death (apoptosis) in drosophila. Fly, 3:78-90, Jan 2009. URL: https://doi.org/10.4161/fly.3.1.7800, doi:10.4161/fly.3.1.7800. This article has 167 citations and is from a peer-reviewed journal.

13. (jiang2001participationofsurvivin pages 4-7): Xiuyun Jiang, Casey Wilford, Stephan Duensing, Karl Munger, Grace Jones, and Davy Jones. Participation of survivin in mitotic and apoptotic activities of normal and tumor‐derived cells *. Journal of Cellular Biochemistry, 83:342-354, Jan 2001. URL: https://doi.org/10.1002/jcb.1228, doi:10.1002/jcb.1228. This article has 121 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Det-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. roth2015asymmetricallydividingdrosophila pages 4-4
2. billmann2016ageneticinteraction pages 7-9
3. frappaolo2022microtubuleandactin pages 11-12
4. wang2020oocytespindleassembly pages 1-5
5. wang2020oocytespindleassembly pages 5-8
6. giansanti2012cytokinesisindrosophila pages 7-8
7. wang2020oocytespindleassembly pages 28-31
8. jiang2001participationofsurvivin pages 7-10
9. jiang2001participationofsurvivin pages 1-2
10. giansanti2012cytokinesisindrosophila pages 6-7
11. frappaolo2022microtubuleandactin pages 10-11
12. xu2009geneticcontrolof pages 12-13
13. jiang2001participationofsurvivin pages 4-7
14. DOI
15. Szafer-Glusman, Fuller and Giansanti, *Molecular Biology of the Cell*, October 2011
16. 2012
17. 2022
18. preprint, initially posted 2020 and revised January 17, 2021
19. Jones and colleagues, *Journal of Biological Chemistry*, July 2000
20. 2001 primary study
21. 2009 review
22. Roth and colleagues, *Nature Communications*, March 2015
23. Billmann and colleagues, *Molecular Biology of the Cell*, April 2016
24. Frappaolo, Piergentili and Giansanti, *Cells*, February 2022
25. https://doi.org/10.1091/mbc.e11-06-0569
26. https://doi.org/10.1038/ncomms7551
27. https://doi.org/10.1101/2020.06.03.132142
28. https://doi.org/10.1002/jcb.1228
29. https://doi.org/10.1091/mbc.e15-07-0467
30. https://doi.org/10.4161/spmg.21711
31. https://doi.org/10.3390/cells11040695
32. https://doi.org/10.1074/jbc.m000369200
33. https://doi.org/10.4161/fly.3.1.7800
34. https://doi.org/10.3390/cells11040695,
35. https://doi.org/10.1101/2020.06.03.132142,
36. https://doi.org/10.4161/spmg.21711,
37. https://doi.org/10.1038/ncomms7551,
38. https://doi.org/10.1002/jcb.1228,
39. https://doi.org/10.1091/mbc.e15-07-0467,
40. https://doi.org/10.4161/fly.3.1.7800,