---
provider: falcon
model: Edison Scientific Literature
cached: true
start_time: '2026-09-26T20:36:01.472152'
end_time: '2026-09-26T20:36:01.475403'
duration_seconds: 0.0
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: yeast
  gene_id: MSI1
  gene_symbol: MSI1
  uniprot_accession: P13712
  protein_description: 'RecName: Full=Histone-binding protein MSI1 {ECO:0000305};
    AltName: Full=Chromatin assembly factor 1 subunit C {ECO:0000305}; Short=CAF-1
    subunit C {ECO:0000305}; AltName: Full=Chromatin assembly factor 1 subunit p50
    {ECO:0000305}; Short=CAF-1 p50 subunit {ECO:0000305}; AltName: Full=IRA1 multicopy
    suppressor;'
  gene_info: Name=MSI1; Synonyms=CAC3; OrderedLocusNames=YBR195C; ORFNames=YBR1405;
  organism_full: Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
  protein_family: Belongs to the WD repeat RBAP46/RBAP48/MSI1 family.
  protein_domains: Beta-prop_NOL10_N. (IPR056551); Histone-bd_RBBP4-like_N. (IPR022052);
    WD40/YVTN_repeat-like_dom_sf. (IPR015943); WD40_repeat_CS. (IPR019775); WD40_repeat_dom_sf.
    (IPR036322)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 23
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: MSI1-deep-research-falcon_artifacts/artifact-00.md
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
- **UniProt Accession:** P13712
- **Protein Description:** RecName: Full=Histone-binding protein MSI1 {ECO:0000305}; AltName: Full=Chromatin assembly factor 1 subunit C {ECO:0000305}; Short=CAF-1 subunit C {ECO:0000305}; AltName: Full=Chromatin assembly factor 1 subunit p50 {ECO:0000305}; Short=CAF-1 p50 subunit {ECO:0000305}; AltName: Full=IRA1 multicopy suppressor;
- **Gene Information:** Name=MSI1; Synonyms=CAC3; OrderedLocusNames=YBR195C; ORFNames=YBR1405;
- **Organism (full):** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
- **Protein Family:** Belongs to the WD repeat RBAP46/RBAP48/MSI1 family.
- **Key Domains:** Beta-prop_NOL10_N. (IPR056551); Histone-bd_RBBP4-like_N. (IPR022052); WD40/YVTN_repeat-like_dom_sf. (IPR015943); WD40_repeat_CS. (IPR019775); WD40_repeat_dom_sf. (IPR036322)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "MSI1" matches the protein description above**
2. **Verify the organism is correct:** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'MSI1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **MSI1** (gene ID: MSI1, UniProt: P13712) in yeast.

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
- **UniProt Accession:** P13712
- **Protein Description:** RecName: Full=Histone-binding protein MSI1 {ECO:0000305}; AltName: Full=Chromatin assembly factor 1 subunit C {ECO:0000305}; Short=CAF-1 subunit C {ECO:0000305}; AltName: Full=Chromatin assembly factor 1 subunit p50 {ECO:0000305}; Short=CAF-1 p50 subunit {ECO:0000305}; AltName: Full=IRA1 multicopy suppressor;
- **Gene Information:** Name=MSI1; Synonyms=CAC3; OrderedLocusNames=YBR195C; ORFNames=YBR1405;
- **Organism (full):** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
- **Protein Family:** Belongs to the WD repeat RBAP46/RBAP48/MSI1 family.
- **Key Domains:** Beta-prop_NOL10_N. (IPR056551); Histone-bd_RBBP4-like_N. (IPR022052); WD40/YVTN_repeat-like_dom_sf. (IPR015943); WD40_repeat_CS. (IPR019775); WD40_repeat_dom_sf. (IPR036322)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "MSI1" matches the protein description above**
2. **Verify the organism is correct:** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'MSI1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **MSI1** (gene ID: MSI1, UniProt: P13712) in yeast.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Functional annotation report: *Saccharomyces cerevisiae* MSI1/CAC3 (UniProt P13712)

## Executive conclusion

The requested protein is correctly identified as budding-yeast **Msi1/Cac3**, not a plant MSI1 protein, an RNA-binding Musashi protein, or the cancer abbreviation “MSI.” Primary literature maps **MSI1 to chromosome II ORF YBR195C** and identifies its product as the approximately p50/small subunit of the heterotrimeric **chromatin assembly factor 1 (CAF-1)** complex. The organism is *Saccharomyces cerevisiae*; the supplied S288c identifiers MSI1/CAC3/YBR195C and UniProt P13712 are mutually consistent with the literature. Kaufman and colleagues also placed Msi1 in the yeast p48/RbAp protein family, consistent with the supplied RBAP46/RBAP48/MSI1-family and WD40-domain annotations (published February 1997; https://doi.org/10.1101/gad.11.3.345). (kaufman1997ultravioletradiationsensitivity pages 5-6)

Functionally, Msi1 is **not an enzyme** and therefore has no catalytic reaction or conventional enzyme substrate specificity. Its best-supported primary role is as a WD40-type structural/accessory subunit of CAF-1, helping organize a complex that deposits histones H3–H4 onto newly synthesized or repaired DNA. Modern biochemistry substantially refines the older designation “histone-binding protein”: isolated Cac3 binds H3–H4, but weakly compared with intact CAF-1, and it cannot by itself productively assemble nucleosomes. The principal productive H3–H4 interface is instead formed by Cac1-bound Cac2 together with the acidic region of Cac1. (mattiroli2017thecac2subunit pages 2-3, mattiroli2017thecac2subunit pages 6-8, mattiroli2017thecac2subunit pages 1-2)

## Identity and ambiguity control

The gene symbol **MSI1 is highly ambiguous across biology**. Arabidopsis MSI1 participates in several plant chromatin complexes, while mammalian homologs are generally called RBBP4/RbAp48 or RBBP7/RbAp46. Those are homologous WD40 proteins, not UniProt P13712. Likewise, “MSI” in oncology usually means microsatellite instability, and mammalian Musashi-1 is an unrelated RNA-binding protein. None of those literatures was used as direct evidence for this yeast annotation.

For the exact yeast target, the verified nomenclature is:

- gene: **MSI1**, synonym **CAC3**;
- systematic locus: **YBR195C**, on chromosome II;
- product: CAF-1 p50/small subunit, Msi1/Cac3;
- organism: *S. cerevisiae*, matching the requested S288c context;
- family: p48/RbAp or RBAP46/RBAP48/MSI1 family;
- architecture: predicted WD40-repeat β-propeller, consistent with the supplied Beta-prop_NOL10_N, RBBP4-like histone-binding N-terminal, and WD40-domain InterPro assignments. (mattiroli2017thecac2subunit pages 1-2, kaufman1997ultravioletradiationsensitivity pages 5-6)

## Molecular function and mechanism

### CAF-1 architecture

Yeast CAF-1 contains one copy each of **Cac1, Cac2, and Cac3/Msi1**. Biophysical analysis describes it as an elongated heterotrimer, approximately 250–300 Å in maximum dimension, with Cac1 serving as the principal scaffold. Cac3 contacts the central portion of Cac1; hydrogen–deuterium exchange and mutagenesis implicated Cac1 regions around residues 280–286 and 344–349. Cac2 and Cac3 do not appear to interact directly. (mattiroli2017thecac2subunit pages 2-3, mattiroli2017thecac2subunit pages 6-8, mattiroli2017thecac2subunit pages 1-2)

Cac3’s WD40 propeller is therefore most plausibly a protein-interaction platform that stabilizes or organizes CAF-1 rather than a catalytic domain. Removal of Cac3 altered protection across roughly 115 Cac1 residues—about 19% of full-length Cac1—supporting a substantial architectural effect on the complex. (mattiroli2017thecac2subunit pages 6-8)

### Histone recognition and substrate specificity

Quantitative measurements are particularly informative. Isolated Cac3 bound H3–H4 with a reported dissociation constant of approximately **77 nM**, compared with approximately **0.3 nM** for intact CAF-1. A complex lacking Cac3 still bound H3–H4 at approximately **1.3 nM**. Moreover, isolated Cac3 did not detectably assemble tetrasomes or nucleosomes, whereas intact CAF-1 was active. These measurements show that H3–H4 is a legitimate interaction partner but that Cac3 is neither sufficient nor the dominant productive histone-binding module. (mattiroli2017thecac2subunit pages 2-3)

The physiologically relevant cargo of the complete complex is canonical **histone H3–H4**. Intact yeast CAF-1 binds one H3–H4 heterodimer in solution; cooperative association of two CAF-1–H3–H4 complexes on DNA permits deposition of an H3–H4 tetramer, the first histone core intermediate in nucleosome assembly. Histones can be transferred to CAF-1 from upstream chaperone assemblies involving Asf1 or Mcm2. These are whole-complex properties and should not be assigned specifically to Cac3’s WD40 surface. (sauer2017insightsintothe pages 16-17, sauer2017insightsintothe pages 17-18)

### Replication- and repair-coupled chromatin assembly

CAF-1 acts behind DNA synthesis to rebuild nucleosomes. Recruitment is coupled to proliferating-cell nuclear antigen (**PCNA**) at replication and repair sites, while the strongest DNA-binding and PCNA-associated determinants reside in Cac1 rather than Cac3. Accordingly, the most precise annotation is: **Msi1/Cac3 is a noncatalytic CAF-1 subunit that supports the architecture and efficiency of H3–H4 deposition during DNA-synthesis-coupled chromatin assembly**. (yang2013msi1like(msil)proteins pages 2-4, turner2011theanaphasepromotingcomplexa pages 26-30, sauer2017insightsintothe pages 17-18)

The distinction between direct and complex-level evidence is important. Early reports sometimes described all three CAF-1 subunits as histone binding. Later quantitative work showed that Cac3 makes only a moderate contribution to productive H3–H4 binding and assembly, whereas Cac2 and Cac1 form the essential composite interface. This later mechanistic evidence should be given greater weight. (turner2011theanaphasepromotingcomplex pages 26-30, mattiroli2017thecac2subunit pages 2-3, mattiroli2017thecac2subunit pages 1-2)

| Topic | Finding | Evidence type | Interpretation / caveat | Source, date, URL |
|---|---|---|---|---|
| Target identity | In *Saccharomyces cerevisiae*, **MSI1** is **CAC3**, chromosome II ORF **YBR195C**, and encodes the p50/small subunit of CAF-1. | Protein purification, peptide identification, gene mapping, and disruption genetics | Confirms the requested yeast protein; plant MSI1 and mammalian RBBP4/RBBP7 are homologs, not this target. | Kaufman et al., February 1997, [DOI](https://doi.org/10.1101/gad.11.3.345) (kaufman1997ultravioletradiationsensitivity pages 5-6) |
| Family and domains | Msi1/Cac3 belongs to the p48/RbAp family and is predicted to adopt a WD40-repeat β-propeller fold. | Sequence-family comparison and structural prediction | Consistent with the supplied RBAP46/RBAP48/MSI1-family and WD40 annotations. The fold supports protein-interaction/scaffolding functions; it does not imply catalytic activity. | Kaufman et al., February 1997, [DOI](https://doi.org/10.1101/gad.11.3.345); Mattiroli et al., April 2017, [DOI](https://doi.org/10.1038/srep46274) (mattiroli2017thecac2subunit pages 1-2, kaufman1997ultravioletradiationsensitivity pages 5-6) |
| CAF-1 architecture | Yeast CAF-1 is an elongated **1:1:1 Cac1–Cac2–Cac3 heterotrimer**. Cac1 scaffolds the two WD40 subunits; Cac2 and Cac3 do not directly interact detectably. Cac3 contacts the Cac1 central region, including segments around residues 280–286 and 344–349. | SEC-MALLS/SAXS, hydrogen–deuterium exchange mass spectrometry, mutagenesis, and pulldown assays | Establishes Msi1/Cac3 as an accessory structural subunit of CAF-1 rather than an enzyme. | Sauer et al., March 2017, [DOI](https://doi.org/10.7554/eLife.23474); Mattiroli et al., April 2017, [DOI](https://doi.org/10.1038/srep46274) (mattiroli2017thecac2subunit pages 2-3, sauer2017insightsintothe pages 16-17, mattiroli2017thecac2subunit pages 6-8, mattiroli2017thecac2subunit pages 1-2) |
| H3–H4 binding | Isolated Cac3 bound H3–H4 with **K~d~ ≈77 nM**, whereas intact CAF-1 bound at **≈0.3 nM** and CAF-1 lacking Cac3 at **≈1.3 nM**. Isolated Cac3 did not detectably assemble tetrasomes or nucleosomes. | Quantitative fluorescence binding and in-vitro chromatin-assembly assays | Cac3 contributes to complex organization and affinity but is **not the principal productive H3–H4-binding/deposition module**; the major composite interface is formed by Cac1-bound Cac2 plus the Cac1 acidic region. | Mattiroli et al., 18 April 2017, [DOI](https://doi.org/10.1038/srep46274) (mattiroli2017thecac2subunit pages 2-3, mattiroli2017thecac2subunit pages 6-8, mattiroli2017thecac2subunit pages 1-2) |
| Subcellular localization | Msi1/Cac3 was detected in both the **nucleus and cytoplasm**; Cac1 is predominantly nuclear. Cytoplasmic localization is consistent with Msi1’s interaction with Npr1. | Cell-fraction/localization observations and protein-interaction analysis | The nuclear pool supports CAF-1/chromatin functions, while the cytoplasmic pool supports a separable nutrient-signaling role. Localization is therefore not exclusively nuclear. | Johnston et al., March 2001, [DOI](https://doi.org/10.1128/MCB.21.5.1784-1794.2001); Yang et al., March 2013, [DOI](https://doi.org/10.5941/myco.2013.41.1.1) (johnston2001cac3(msi1)suppression pages 1-1, yang2013msi1like(msil)proteins pages 2-4) |
| Replication-coupled chromatin assembly | CAF-1 deposits H3–H4 on newly synthesized DNA and operates in the replication/repair-associated **PCNA** context. Biochemical work indicates that intact yeast CAF-1 binds one H3–H4 dimer and that two CAF-1–H3–H4 complexes can cooperate on sufficiently long DNA to produce an H3–H4 tetramer. | Purified-complex biochemistry, DNA/histone-binding assays, chromatin assembly, and prior PCNA genetics | This is primarily evidence for the **whole CAF-1 complex**. PCNA and DNA-binding determinants reside chiefly in Cac1; they should not be assigned directly to Cac3. | Sauer et al., March 2017, [DOI](https://doi.org/10.7554/eLife.23474); Yang et al., March 2013, [DOI](https://doi.org/10.5941/myco.2013.41.1.1) (yang2013msi1like(msil)proteins pages 2-4, turner2011theanaphasepromotingcomplexa pages 26-30, sauer2017insightsintothe pages 16-17, sauer2017insightsintothe pages 17-18) |
| UV response and telomeric silencing | Disruption of yeast CAF-1 subunits produced viable mutants with increased UV sensitivity and reduced telomere-position-effect silencing, assessed using a telomere-proximal **URA3/5-FOA** reporter. | Gene disruptions, UV-survival assays, and reporter-based silencing assays | Strong evidence that CAF-1 supports repair-coupled chromatin restoration and silent telomeric chromatin. These phenotypes reflect loss of CAF-1 and should not be interpreted as proof of a Cac3-specific catalytic reaction. | Kaufman et al., February 1997, [DOI](https://doi.org/10.1101/gad.11.3.345) (turner2011theanaphasepromotingcomplexa pages 26-30, kaufman1997ultravioletradiationsensitivity pages 5-6) |
| Separable Ras–PKA/Npr1 function | Increased MSI1 dosage suppresses activated **RAS2^G19V^** phenotypes independently of Cac1, Cac2, and intact CAF-1. Genetic and physical evidence implicates cytoplasmic **Npr1**: NPR1 deletion phenocopied MSI1 overexpression, whereas NPR1 overexpression opposed MSI1-mediated suppression. | Dosage suppression, epistasis, localization, and protein-association experiments | Supports a noncanonical function in nutrient-transporter/Ras–cAMP–PKA regulation, plausibly through Npr1 sequestration or modulation. This is distinct from Msi1’s CAF-1 role and does not establish kinase or enzymatic activity for Msi1. | Johnston et al., March 2001, [DOI](https://doi.org/10.1128/MCB.21.5.1784-1794.2001) (johnston2001cac3(msi1)suppression pages 1-1) |
| Recent literature, 2023–2024 | The targeted search found **no 2023–2024 primary publication centered on exact S. cerevisiae Msi1/Cac3**. A 2024 Hir-complex structure mentions CAF-1 as the Cac1/Cac2/Cac3 replication-associated complex but does not newly characterize Msi1. | Focused literature search and scope assessment | Recent papers on plant MSI1, human “MSI” cancer terminology, or other p48-family proteins cannot be transferred directly to P13712. Current mechanistic annotation therefore rests mainly on the 1997–2018 yeast literature. | Kim et al., July 2024, [DOI](https://doi.org/10.1016/j.molcel.2024.05.031); search assessment through 2024 (yang2013msi1like(msil)proteins pages 10-11) |


*Table: Evidence supporting the identity, architecture, localization, chromatin function, and separable signaling role of yeast Msi1/Cac3. The table distinguishes Cac3-specific results from findings that apply to the complete CAF-1 complex.*

## Cellular localization

Msi1/Cac3 has been detected in **both nucleus and cytoplasm**, whereas Cac1 is predominantly nuclear. The nuclear pool is consistent with CAF-1-mediated chromatin assembly at replication and repair sites. The cytoplasmic pool is mechanistically relevant to Msi1’s separable interaction with the nutrient-responsive kinase Npr1. Thus, “nuclear” is appropriate for its primary chromatin function, but “exclusively nuclear” would be inaccurate. (johnston2001cac3(msi1)suppression pages 1-1, yang2013msi1like(msil)proteins pages 2-4)

## Biological processes and pathways

### Chromatin inheritance, DNA repair, and silencing

Disruptions of yeast CAF-1 genes are viable, showing that CAF-1 is not the sole nucleosome-assembly route. Nevertheless, loss of CAF-1 causes increased ultraviolet sensitivity and reduced telomeric position-effect silencing. Kaufman et al. assayed telomeric repression with a telomere-proximal **URA3** reporter and 5-fluoroorotic-acid selection. These phenotypes support roles in chromatin restoration after DNA damage and in stable propagation of repressed telomeric chromatin. They are best interpreted as CAF-1-complex phenotypes rather than evidence for a Cac3-specific biochemical reaction. (turner2011theanaphasepromotingcomplexa pages 26-30, kaufman1997ultravioletradiationsensitivity pages 5-6)

CAF-1 overlaps functionally with other histone-chaperone systems, especially Asf1 and the HIR complex. Genetic combinations affecting CAF-1 and these alternative pathways intensify UV sensitivity, silencing defects, growth defects, or cell-cycle delay, explaining why single CAF-1 deletions can remain viable. (turner2011theanaphasepromotingcomplexa pages 30-34)

CAF-1-dependent assembly also contributes to broader heterochromatin behavior at telomeres and mating-type loci. Effects at rDNA and reported antagonism with Sin3–Rpd3 are genetically supported but mechanistically less direct for Msi1 than its established CAF-1 role. Proposed Msi1–Rpd3 coupling remains partly inferential, and it should not be treated as equivalent in confidence to purified-complex CAF-1 biochemistry. (yang2013msi1like(msil)proteins pages 2-4, turner2011theanaphasepromotingcomplexa pages 30-34)

### Mitotic chromatin and cell-cycle connections

Multicopy MSI1 can suppress temperature-sensitive growth and chromatin-assembly defects of the **apc5CA** anaphase-promoting-complex mutant. CAC1 and CAC2 dosage can do likewise, and histone H3/H4 coexpression also suppresses relevant defects. These genetic observations connect CAF-1 dosage to APC-associated mitotic chromatin assembly, but they do not demonstrate that Msi1 is an APC substrate or enzyme. (harkness2005contributionofcafi pages 1-2, harkness2005contributionofcafi pages 1-1)

### Ras–cAMP–PKA, Npr1, and Yak1 signaling

MSI1 was originally recovered as a multicopy suppressor of hyperactive Ras phenotypes, explaining the historical name “IRA1 multicopy suppressor.” Importantly, suppression of **RAS2^G19V** by increased MSI1 dosage persists without Cac1 or Cac2 and is therefore independent of intact CAF-1. NPR1 deletion phenocopied MSI1 overexpression, whereas NPR1 overexpression interfered with MSI1-mediated suppression; Msi1 also associates with cytoplasmic Npr1. The authors proposed that Msi1 modulates or sequesters Npr1, thereby affecting ubiquitin-dependent nutrient-transporter regulation and downstream Ras/cAMP–PKA physiology (published March 2001; https://doi.org/10.1128/MCB.21.5.1784-1794.2001). (johnston2001cac3(msi1)suppression pages 1-1)

MSI1 and the kinase **YAK1** also show genetic interdependence in growth-control phenotypes, placing Msi1 in a broader nutrient/stress-responsive network. However, the available evidence does not establish Msi1 as a kinase, phosphatase, or direct signal-transduction enzyme; it is more defensible to describe it as a regulatory interaction/scaffolding protein with a CAF-1-independent signaling function. (yang2013msi1like(msil)proteins pages 10-11, harkness2005contributionofcafi pages 7-8)

## Centromeric histone Cse4

CAF-1 can interact with the budding-yeast centromeric H3 variant **Cse4** and assemble Cse4-containing nucleosomes in vitro. Loss of CAF-1 markedly reduces ectopic, genome-wide Cse4 incorporation when Cse4 is overexpressed, and Cac1 plus Cac3 are required for the reported Cse4–CAF-1 interaction. This indicates that Cac3 contributes to CAF-1-dependent handling of a histone variant under Cse4-overexpression conditions. It should not be interpreted as making Msi1 the normal centromeric Cse4 chaperone or as superseding its principal canonical H3–H4/CAF-1 annotation. The study was published in May 2018 (https://doi.org/10.1093/nar/gky405).

## Structural and evolutionary interpretation

The supplied domain set is coherent with the experimental literature. WD40 β-propellers commonly expose multiple protein-binding surfaces, fitting Cac3’s contacts with Cac1 and its modest interaction with H3–H4. Conservation with Drosophila p55 and mammalian RbAp46/RbAp48 supports an ancestral function linking histones to multiprotein chromatin complexes. However, paralog-specific differences matter: yeast Hat2 is another p48-family member and was not detected in purified yeast CAF-1, whereas Msi1 was. Therefore, functional claims from plant MSI1 or mammalian RBBP4/7 should be treated as evolutionary support, not direct evidence for P13712. (mattiroli2017thecac2subunit pages 1-2, kaufman1997ultravioletradiationsensitivity pages 5-6)

## Recent research, 2023–2024

A focused search found **no 2023–2024 primary study centered on the exact S288c Msi1/Cac3 protein**. The 2024 structural analysis of the yeast HIR histone-chaperone complex refers to replication-associated CAF-1 as the Cac1/Cac2/Cac3 complex, but it does not newly define Msi1’s mechanism. Consequently, the strongest gene-specific mechanistic evidence remains the 1997–2018 literature, especially the quantitative 2017 CAF-1 studies. This is an evidence gap, not justification to substitute recent plant-MSI1, mammalian RBBP4/7, Musashi-1, or microsatellite-instability studies. (yang2013msi1like(msil)proteins pages 10-11, mattiroli2017thecac2subunit pages 2-3, sauer2017insightsintothe pages 16-17)

## Current applications and real-world relevance

There is no established clinical or industrial implementation targeting yeast Msi1 itself. Its present applications are predominantly as a **research model and experimental tool**:

1. **Replication-coupled epigenetic inheritance:** purified Cac1–Cac2–Cac3 complexes and subunit mutants define how new H3–H4 is transferred and deposited behind replication forks. (mattiroli2017thecac2subunit pages 2-3, sauer2017insightsintothe pages 16-17)
2. **DNA-damage chromatin restoration:** CAF-1 mutant UV phenotypes provide tractable assays for coupling DNA repair to nucleosome reassembly. (turner2011theanaphasepromotingcomplexa pages 26-30, kaufman1997ultravioletradiationsensitivity pages 5-6)
3. **Heterochromatin and epigenetic memory:** telomeric URA3/5-FOA reporters test how replication-coupled assembly stabilizes silent chromatin. (kaufman1997ultravioletradiationsensitivity pages 5-6)
4. **Centromere/chromosome-stability modeling:** CAF-1 manipulation is used to study inappropriate Cse4 deposition and its transcriptional or segregation consequences.
5. **Conserved chromatin-complex biology:** yeast Msi1 provides a genetically tractable model for the p48/RbAp WD40 family, although direct extrapolation to mammalian disease requires validation.
6. **Nutrient-signaling dissection:** MSI1 dosage and deletion constructs separate a CAF-1-independent Npr1/Ras–PKA function from its chromatin role. (johnston2001cac3(msi1)suppression pages 1-1)

## Confidence-ranked functional annotation

**High confidence:** Msi1/Cac3 is the nonenzymatic WD40 small subunit of yeast CAF-1; it binds Cac1, contributes to CAF-1 architecture, and supports H3–H4 deposition during DNA-synthesis-coupled nucleosome assembly. It acts principally in the nucleus but also has a cytoplasmic population. (mattiroli2017thecac2subunit pages 2-3, mattiroli2017thecac2subunit pages 6-8, kaufman1997ultravioletradiationsensitivity pages 5-6)

**High-to-moderate confidence:** Through CAF-1, it contributes to repair-coupled chromatin restoration, UV resistance, telomeric silencing, and genome stability. These are whole-complex functions, with redundancy from Asf1/HIR pathways. (yang2013msi1like(msil)proteins pages 2-4, turner2011theanaphasepromotingcomplexa pages 26-30, kaufman1997ultravioletradiationsensitivity pages 5-6)

**Moderate confidence:** Msi1 has a CAF-1-independent role in Ras/cAMP–PKA and nutrient-transporter regulation mediated by Npr1 and genetically connected to Yak1. The signaling phenotype is reproducible, but the precise molecular action remains less resolved than CAF-1 assembly. (johnston2001cac3(msi1)suppression pages 1-1, yang2013msi1like(msil)proteins pages 10-11)

**Lower or context-dependent confidence:** Msi1–Rpd3 coupling, APC-associated mitotic assembly, and Cse4 handling are biologically plausible and experimentally supported in particular settings, but they should be annotated as secondary/contextual functions rather than the protein’s primary molecular role. (turner2011theanaphasepromotingcomplexa pages 30-34, harkness2005contributionofcafi pages 1-2, harkness2005contributionofcafi pages 1-1)

Overall, the most precise concise annotation is: **Msi1/Cac3 (P13712) is a conserved WD40 interaction subunit of budding-yeast CAF-1 that structurally supports replication- and repair-coupled H3–H4 nucleosome assembly; it additionally participates in a separable cytoplasmic Npr1-dependent nutrient/Ras–PKA regulatory pathway.**

References

1. (kaufman1997ultravioletradiationsensitivity pages 5-6): P. Kaufman, R. Kobayashi, and B. Stillman. Ultraviolet radiation sensitivity and reduction of telomeric silencing in saccharomyces cerevisiae cells lacking chromatin assembly factor-i. Genes & development, 11 3:345-57, Feb 1997. URL: https://doi.org/10.1101/gad.11.3.345, doi:10.1101/gad.11.3.345. This article has 473 citations and is from a highest quality peer-reviewed journal.

2. (mattiroli2017thecac2subunit pages 2-3): Francesca Mattiroli, Yajie Gu, Jeremy L. Balsbaugh, Natalie G. Ahn, and Karolin Luger. The cac2 subunit is essential for productive histone binding and nucleosome assembly in caf-1. Scientific Reports, Apr 2017. URL: https://doi.org/10.1038/srep46274, doi:10.1038/srep46274. This article has 34 citations and is from a peer-reviewed journal.

3. (mattiroli2017thecac2subunit pages 6-8): Francesca Mattiroli, Yajie Gu, Jeremy L. Balsbaugh, Natalie G. Ahn, and Karolin Luger. The cac2 subunit is essential for productive histone binding and nucleosome assembly in caf-1. Scientific Reports, Apr 2017. URL: https://doi.org/10.1038/srep46274, doi:10.1038/srep46274. This article has 34 citations and is from a peer-reviewed journal.

4. (mattiroli2017thecac2subunit pages 1-2): Francesca Mattiroli, Yajie Gu, Jeremy L. Balsbaugh, Natalie G. Ahn, and Karolin Luger. The cac2 subunit is essential for productive histone binding and nucleosome assembly in caf-1. Scientific Reports, Apr 2017. URL: https://doi.org/10.1038/srep46274, doi:10.1038/srep46274. This article has 34 citations and is from a peer-reviewed journal.

5. (sauer2017insightsintothe pages 16-17): Paul Victor Sauer, Jennifer Timm, Danni Liu, David Sitbon, Elisabetta Boeri-Erba, Christophe Velours, Norbert Mücke, Jörg Langowski, Françoise Ochsenbein, Geneviève Almouzni, and Daniel Panne. Insights into the molecular architecture and histone h3-h4 deposition mechanism of yeast chromatin assembly factor 1. eLife, Mar 2017. URL: https://doi.org/10.7554/elife.23474, doi:10.7554/elife.23474. This article has 83 citations and is from a domain leading peer-reviewed journal.

6. (sauer2017insightsintothe pages 17-18): Paul Victor Sauer, Jennifer Timm, Danni Liu, David Sitbon, Elisabetta Boeri-Erba, Christophe Velours, Norbert Mücke, Jörg Langowski, Françoise Ochsenbein, Geneviève Almouzni, and Daniel Panne. Insights into the molecular architecture and histone h3-h4 deposition mechanism of yeast chromatin assembly factor 1. eLife, Mar 2017. URL: https://doi.org/10.7554/elife.23474, doi:10.7554/elife.23474. This article has 83 citations and is from a domain leading peer-reviewed journal.

7. (yang2013msi1like(msil)proteins pages 2-4): Dong-Hoon Yang, Shinae Maeng, and Yong-Sun Bahn. Msi1-like (msil) proteins in fungi. Mycobiology, 41:1-12, Mar 2013. URL: https://doi.org/10.5941/myco.2013.41.1.1, doi:10.5941/myco.2013.41.1.1. This article has 10 citations and is from a peer-reviewed journal.

8. (turner2011theanaphasepromotingcomplexa pages 26-30): E Turner. The anaphase-promoting complex interacts with histone modification proteins and chromatin assembly factors. Unknown journal, 2011.

9. (turner2011theanaphasepromotingcomplex pages 26-30): E Turner. The anaphase-promoting complex interacts with histone modification proteins and chromatin assembly factors. Unknown journal, 2011.

10. (johnston2001cac3(msi1)suppression pages 1-1): Stephen D. Johnston, Shinichiro Enomoto, Lisa Schneper, Mark C. McClellan, Florence Twu, Nathan D. Montgomery, Steven A. Haney, James R. Broach, and Judith Berman. Cac3 (msi1) suppression ofras2g19v is independent of chromatin assembly factor i and mediated by npr1. Molecular and Cellular Biology, 21:1784-1794, Mar 2001. URL: https://doi.org/10.1128/mcb.21.5.1784-1794.2001, doi:10.1128/mcb.21.5.1784-1794.2001. This article has 42 citations and is from a domain leading peer-reviewed journal.

11. (yang2013msi1like(msil)proteins pages 10-11): Dong-Hoon Yang, Shinae Maeng, and Yong-Sun Bahn. Msi1-like (msil) proteins in fungi. Mycobiology, 41:1-12, Mar 2013. URL: https://doi.org/10.5941/myco.2013.41.1.1, doi:10.5941/myco.2013.41.1.1. This article has 10 citations and is from a peer-reviewed journal.

12. (turner2011theanaphasepromotingcomplexa pages 30-34): E Turner. The anaphase-promoting complex interacts with histone modification proteins and chromatin assembly factors. Unknown journal, 2011.

13. (harkness2005contributionofcafi pages 1-2): Troy A. A. Harkness, Terra G. Arnason, Charmaine Legrand, Marnie G. Pisclevich, Gerald F. Davies, and Emma L. Turner. Contribution of caf-i to anaphase-promoting-complex-mediated mitotic chromatin assembly in saccharomyces cerevisiae. Eukaryotic Cell, 4:673-684, Apr 2005. URL: https://doi.org/10.1128/ec.4.4.673-684.2005, doi:10.1128/ec.4.4.673-684.2005. This article has 25 citations and is from a peer-reviewed journal.

14. (harkness2005contributionofcafi pages 1-1): Troy A. A. Harkness, Terra G. Arnason, Charmaine Legrand, Marnie G. Pisclevich, Gerald F. Davies, and Emma L. Turner. Contribution of caf-i to anaphase-promoting-complex-mediated mitotic chromatin assembly in saccharomyces cerevisiae. Eukaryotic Cell, 4:673-684, Apr 2005. URL: https://doi.org/10.1128/ec.4.4.673-684.2005, doi:10.1128/ec.4.4.673-684.2005. This article has 25 citations and is from a peer-reviewed journal.

15. (harkness2005contributionofcafi pages 7-8): Troy A. A. Harkness, Terra G. Arnason, Charmaine Legrand, Marnie G. Pisclevich, Gerald F. Davies, and Emma L. Turner. Contribution of caf-i to anaphase-promoting-complex-mediated mitotic chromatin assembly in saccharomyces cerevisiae. Eukaryotic Cell, 4:673-684, Apr 2005. URL: https://doi.org/10.1128/ec.4.4.673-684.2005, doi:10.1128/ec.4.4.673-684.2005. This article has 25 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](MSI1-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. kaufman1997ultravioletradiationsensitivity pages 5-6
2. turner2011theanaphasepromotingcomplexa pages 30-34
3. sauer2017insightsintothe pages 16-17
4. sauer2017insightsintothe pages 17-18
5. turner2011theanaphasepromotingcomplexa pages 26-30
6. turner2011theanaphasepromotingcomplex pages 26-30
7. harkness2005contributionofcafi pages 1-2
8. harkness2005contributionofcafi pages 1-1
9. harkness2005contributionofcafi pages 7-8
10. DOI
11. https://doi.org/10.1101/gad.11.3.345
12. https://doi.org/10.1038/srep46274
13. https://doi.org/10.7554/eLife.23474
14. https://doi.org/10.1128/MCB.21.5.1784-1794.2001
15. https://doi.org/10.5941/myco.2013.41.1.1
16. https://doi.org/10.1016/j.molcel.2024.05.031
17. https://doi.org/10.1093/nar/gky405
18. https://doi.org/10.1101/gad.11.3.345,
19. https://doi.org/10.1038/srep46274,
20. https://doi.org/10.7554/elife.23474,
21. https://doi.org/10.5941/myco.2013.41.1.1,
22. https://doi.org/10.1128/mcb.21.5.1784-1794.2001,
23. https://doi.org/10.1128/ec.4.4.673-684.2005,