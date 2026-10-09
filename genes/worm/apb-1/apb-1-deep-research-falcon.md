---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-27T15:28:44.135116'
end_time: '2026-09-27T15:34:40.358200'
duration_seconds: 356.22
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: worm
  gene_id: apb-1
  gene_symbol: apb-1
  uniprot_accession: Q9N4F3
  protein_description: 'RecName: Full=AP complex subunit beta {ECO:0000256|PIRNR:PIRNR002291};'
  gene_info: Name=apb-1 {ECO:0000313|EMBL:CCD72406.1, ECO:0000313|WormBase:Y71H2B.10};
    ORFNames=CELE_Y71H2B.10 {ECO:0000313|EMBL:CCD72406.1}, Y71H2B.10 {ECO:0000313|WormBase:Y71H2B.10};
  organism_full: Caenorhabditis elegans.
  protein_family: Belongs to the adaptor complexes large subunit family.
  protein_domains: AP_beta. (IPR026739); AP_complex_bsu_1_2_4. (IPR016342); ARM-like.
    (IPR011989); ARM-type_fold. (IPR016024); B-adaptin_app_sub_C. (IPR015151)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 13
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: apb-1-deep-research-falcon_artifacts/artifact-00.md
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
- **UniProt Accession:** Q9N4F3
- **Protein Description:** RecName: Full=AP complex subunit beta {ECO:0000256|PIRNR:PIRNR002291};
- **Gene Information:** Name=apb-1 {ECO:0000313|EMBL:CCD72406.1, ECO:0000313|WormBase:Y71H2B.10}; ORFNames=CELE_Y71H2B.10 {ECO:0000313|EMBL:CCD72406.1}, Y71H2B.10 {ECO:0000313|WormBase:Y71H2B.10};
- **Organism (full):** Caenorhabditis elegans.
- **Protein Family:** Belongs to the adaptor complexes large subunit family.
- **Key Domains:** AP_beta. (IPR026739); AP_complex_bsu_1_2_4. (IPR016342); ARM-like. (IPR011989); ARM-type_fold. (IPR016024); B-adaptin_app_sub_C. (IPR015151)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "apb-1" matches the protein description above**
2. **Verify the organism is correct:** Caenorhabditis elegans.
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'apb-1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **apb-1** (gene ID: apb-1, UniProt: Q9N4F3) in worm.

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
- **UniProt Accession:** Q9N4F3
- **Protein Description:** RecName: Full=AP complex subunit beta {ECO:0000256|PIRNR:PIRNR002291};
- **Gene Information:** Name=apb-1 {ECO:0000313|EMBL:CCD72406.1, ECO:0000313|WormBase:Y71H2B.10}; ORFNames=CELE_Y71H2B.10 {ECO:0000313|EMBL:CCD72406.1}, Y71H2B.10 {ECO:0000313|WormBase:Y71H2B.10};
- **Organism (full):** Caenorhabditis elegans.
- **Protein Family:** Belongs to the adaptor complexes large subunit family.
- **Key Domains:** AP_beta. (IPR026739); AP_complex_bsu_1_2_4. (IPR016342); ARM-like. (IPR011989); ARM-type_fold. (IPR016024); B-adaptin_app_sub_C. (IPR015151)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "apb-1" matches the protein description above**
2. **Verify the organism is correct:** Caenorhabditis elegans.
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'apb-1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **apb-1** (gene ID: apb-1, UniProt: Q9N4F3) in worm.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Functional annotation report: *C. elegans apb-1* (UniProt Q9N4F3)

## Executive conclusion

The identity is verified: *apb-1* in *Caenorhabditis elegans* encodes APB-1, a large β-adaptin subunit shared by the heterotetrameric AP-1 and AP-2 adaptor complexes. This agrees with the supplied UniProt description, “AP complex subunit beta,” and with its adaptor-complex large-subunit, AP_beta, ARM-like/ARM-fold, and C-terminal β-adaptin appendage annotations. Literature using “2-APB” for a small-molecule ion-channel modulator is unrelated and was excluded.

APB-1 is not an enzyme or transporter and has no catalytic reaction or transported substrate. Its primary function is structural and organizational: as part of adaptor coats, it helps connect selected membrane cargo and clathrin-associated trafficking machinery, enabling coated-carrier formation and cargo sorting. In AP-2 it belongs to the β–μ2 hemicomplex; in AP-1 it is the β1 large subunit. Because the same protein is used in both complexes, an *apb-1* phenotype cannot be assigned to AP-1 or AP-2 without compartment- or partner-specific evidence. (gu2013ap2hemicomplexescontribute pages 6-8, sato2014c.elegansas pages 4-6, nakatsu2014theroleof pages 4-6)

## 1. Identity, family, and domain consistency

The nematode AP-2 complex comprises APA-2/α, APS-2/σ2, APB-1/β, and APM-2/μ2. APB-1 is explicitly described as shared with AP-1. The AP-1 complex contains APG-1/γ1, APS-1/σ1, APB-1/β1, and one of the μ1 chains APM-1 or UNC-101. Thus, the gene symbol, organism, and supplied protein-family assignment all match the literature target. (sato2014c.elegansas pages 4-6, nakatsu2014theroleof pages 4-6)

The supplied ARM-like and ARM-type-fold annotations are structurally plausible for the elongated adaptor “trunk” characteristic of AP-complex large subunits. The supplied B-adaptin_app_sub_C annotation is consistent with a C-terminal appendage/platform used by β-adaptins to organize coat-associated proteins. These domain-based statements are evolutionary/structural inference; the retrieved literature did not report an atomic structure of *C. elegans* APB-1 itself.

## 2. Primary molecular function

### AP-2 role at the plasma membrane

AP-2 mediates clathrin-associated sorting and endocytosis at the plasma membrane. APB-1 pairs functionally with APM-2/μ2 as one hemicomplex, while APA-2/α and APS-2/σ2 form the other. GFP-tagged β-adaptin remained stable and localized at AP-2-associated sites when α-adaptin was absent, but it disappeared from the synapse-rich nerve ring when μ2 was absent; residual fluorescence remained in cell bodies. This is direct evidence that APB-1’s stable recruitment to neuronal AP-2 sites depends particularly on its μ2 partner. (gu2013ap2hemicomplexescontribute pages 6-8, gu2013ap2hemicomplexescontribute pages 4-6)

The best mechanistic interpretation is that APB-1 supplies part of the large structural scaffold that stabilizes AP-2, supports coat assembly, and positions cargo- and accessory-protein interactions. Cargo recognition is distributed across the adaptor rather than attributable solely to APB-1. For example, MIG-14/Wntless trafficking is especially sensitive to loss of μ2, whereas an artificial dileucine cargo is more sensitive to loss of α-adaptin; these are AP-2 hemicomplex experiments, not direct demonstrations that APB-1 alone recognizes either cargo. (gu2013ap2hemicomplexescontribute pages 4-6, sato2014c.elegansas pages 4-6)

### AP-1 role in intracellular and polarized sorting

AP-1 functions in clathrin-associated traffic at the trans-Golgi network (TGN) and related endosomal/recycling compartments, particularly in polarized epithelial sorting. In the *C. elegans* intestine, GFP–APB-1 labels punctate structures and colocalizes with SMAP-1, an Arf-family GAP implicated in TGN coat assembly and polarized secretion. APB-1 puncta accumulate in *smap-1* mutants, whereas clathrin-positive puncta decrease. These findings place APB-1 in an AP-1/clathrin pathway at intestinal intracellular membranes. (wang2021ap1recruitssmap1smaps pages 4-8)

GST pull-down experiments did not detect direct binding between SMAP-1 and APB-1; SMAP-1 bound APG-1/γ instead. Therefore, APB-1 and SMAP-1 colocalization should be interpreted as membership in the same TGN sorting machinery, not evidence of direct physical contact. Overexpressing all four AP-1 subunits, including APB-1, did not fully rescue the *smap-1* cargo-sorting defect, whereas clathrin overexpression did, supporting a model in which SMAP-1 helps couple intact AP-1 to productive clathrin assembly. (wang2021ap1recruitssmap1smaps pages 4-8)

## 3. Cellular and tissue localization

Direct imaging supports localization at several membrane-trafficking sites:

* **Neuronal synaptic regions:** GFP-tagged β-adaptin localizes to the nerve ring, and this signal depends on APM-2/μ2, identifying it principally as AP-2-associated at these sites. (gu2013ap2hemicomplexescontribute pages 6-8, gu2013ap2hemicomplexescontribute pages 14-15)
* **Oocyte plasma membrane:** β-adaptin is detected at the oocyte surface, consistent with AP-2-mediated endocytic traffic. (gu2013ap2hemicomplexescontribute pages 6-8)
* **Intestinal intracellular puncta/TGN-associated structures:** GFP–APB-1 colocalizes with SMAP-1 and participates in AP-1/clathrin-associated polarized sorting. (wang2021ap1recruitssmap1smaps pages 4-8)

Accordingly, APB-1 is a cytosolic coat protein recruited transiently to the cytoplasmic face of membranes; it is not a transmembrane, secreted, or extracellular protein.

## 4. Biological processes and pathways

### Clathrin-mediated endocytosis and synaptic-vesicle recycling

AP-2 is required for efficient synaptic-vesicle maintenance. Disrupting both AP-2 hemicomplexes reduced synaptic-vesicle number by approximately 70%, whereas loss of either α or μ2 alone caused reductions of about 30%. The α-adaptin mutant evoked current was 1,259.1 ± 274.9 pA compared with 2,159.6 ± 131.1 pA in wild type. These values establish the physiological importance and partial independence of AP-2 hemicomplexes, but they are not measurements from an *apb-1* null mutant and therefore constitute pathway-level rather than APB-1-specific quantitative evidence. (gu2013ap2hemicomplexescontribute pages 14-15)

APB-1’s μ2-dependent nerve-ring localization makes participation in this pathway highly credible. Nevertheless, because APB-1 is also part of AP-1, strong *apb-1* loss may combine endocytic and intracellular-sorting defects.

### TGN sorting, secretion, and epithelial polarity

The intestinal AP-1 pathway helps separate apical from basolateral cargo. Loss of AP-1 subunits or clathrin reduces clathrin-positive puncta and causes apical ERM-1 to accumulate basolaterally while basolateral SLCF-1 appears at the apical membrane. In *smap-1* mutants, GFP–APB-1 and GFP–APG-1 accumulate on puncta, while TGN-associated clathrin is reduced. Imaging analyses used 18 animals per condition for puncta/cargo measurements and 12 animals for colocalization measurements, with reported differences commonly reaching *p*<0.001. These results support APB-1’s role in AP-1-dependent polarized secretion, although most perturbations targeted SMAP-1 or the AP-1 complex rather than APB-1 alone. (wang2021ap1recruitssmap1smaps pages 3-4, wang2021ap1recruitssmap1smaps pages 4-8)

### Development and tubulogenesis

RNAi depletion of *apb-1*, like depletion of AP-1 γ or σ1 subunits, causes embryonic-stage growth arrest, showing that APB-1-dependent trafficking is essential for development. A characterized *apb-1(tm1369)* heterozygous strain was also used in the 2012 intestinal tubulogenesis study, consistent with severe loss-of-function consequences. Because APB-1 is shared with AP-2, lethality alone does not establish that AP-1 disruption is solely responsible. (nakatsu2014theroleof pages 4-6, zhang2012clathrinandap1 pages 1-1)

## 5. Evidence summary

| Finding | Evidence type | Experimental observation | Interpretation | Key source/date |
|---|---|---|---|---|
| APB-1 is the β-adaptin shared by AP-1 and AP-2 | Direct APB-1 identification | Curated review and experimental literature identify nematode APB-1 as the common β subunit of both heterotetrameric adaptor complexes. | Confirms that *apb-1* findings may reflect AP-1, AP-2, or both; they cannot be assigned to one complex without pathway-specific evidence. | Gu et al., March 2013; Sato et al., April 2014 (gu2013ap2hemicomplexescontribute pages 6-8, sato2014c.elegansas pages 4-6) |
| AP-1 complex composition | Direct APB-1 identification plus complex-level inference | APB-1/β1 is placed with APG-1/γ1, APS-1/σ1, and either APM-1 or UNC-101/μ1. | Supports APB-1 as a large structural subunit of the AP-1 clathrin-adaptor coat used in intracellular and polarized sorting. | Nakatsu et al., November 2014 (nakatsu2014theroleof pages 4-6) |
| AP-2 β–μ2 hemicomplex | Direct APB-1 observation plus complex-level inference | GFP-tagged β-adaptin remained stable when α-adaptin was absent but was lost from AP-2-associated sites when μ2/APM-2 was absent. | APB-1 partners with APM-2/μ2 as one AP-2 hemicomplex and contributes to adaptor assembly rather than catalysis. | Gu et al., March 2013; Sato et al., April 2014 (gu2013ap2hemicomplexescontribute pages 6-8, sato2014c.elegansas pages 4-6) |
| Synaptic and oocyte localization | Direct APB-1 localization | A single-copy GFP-tagged β-adaptin transgene localized to synapse-rich regions of the nerve ring and the oocyte plasma membrane; nerve-ring localization depended on μ2. | Places APB-1 at plasma-membrane/AP-2 trafficking sites, including neuronal synapses and oocytes. | Gu et al., March 2013 (gu2013ap2hemicomplexescontribute pages 6-8, gu2013ap2hemicomplexescontribute pages 14-15) |
| Intestinal TGN-associated puncta and SMAP-1 colocalization | Direct APB-1 localization | GFP–APB-1 labeled intestinal puncta, accumulated on punctate structures in *smap-1* mutants, and colocalized with SMAP-1–mCherry; SMAP-1 did not bind APB-1 detectably in GST pull-down assays. | Supports APB-1 participation in AP-1/clathrin sorting at the intestinal trans-Golgi network, while arguing against a demonstrated direct APB-1–SMAP-1 interaction. | Wang et al., November 2021 (wang2021ap1recruitssmap1smaps pages 4-8) |
| Embryonic growth arrest after *apb-1* knockdown | Direct *apb-1* perturbation | RNAi knockdown of *apb-1*, like depletion of other core AP-1 subunits, caused embryonic-stage growth arrest. | Shows that APB-1-dependent adaptor traffic is essential for development, although sharing with AP-2 limits attribution solely to AP-1. | Nakatsu et al., November 2014, reviewing nematode loss-of-function evidence (nakatsu2014theroleof pages 4-6) |
| AP-2-dependent synaptic-vesicle maintenance | Complex-level inference; not a direct *apb-1* loss-of-function result | Simultaneous disruption of the α- and μ2-associated halves of AP-2 reduced synaptic-vesicle number by about 70%; single α- or μ2-subunit mutations produced reductions of about 30%. | Quantifies the importance of AP-2 in synaptic-vesicle endocytosis and provides pathway context for APB-1, but does not measure the phenotype of *apb-1* loss itself. | Gu et al., March 2013 (gu2013ap2hemicomplexescontribute pages 14-15) |
| No gene-specific 2023–2024 annotation advance identified | Literature-gap assessment | Targeted searches yielded no 2023–2024 study providing new APB-1-specific localization, cargo, structure, or loss-of-function evidence; the newest directly informative retrieved study was published in 2021. | Current annotation still rests mainly on earlier mechanistic genetics, imaging, and adaptor-complex biology; unrelated “2-APB” chemical literature must not be conflated with *apb-1*. | Literature assessment through 2024; Wang et al., November 2021 is the latest directly informative retrieved source (wang2021ap1recruitssmap1smaps pages 4-8) |


*Table: Evidence-grade summary distinguishing direct APB-1 observations and *apb-1* perturbations from broader AP-1/AP-2 complex-level inference. This separation is essential because APB-1 is shared by both adaptor complexes.*

## 6. Recent developments and 2023–2024 status

Targeted searches did not identify a 2023–2024 publication that materially advances gene-specific annotation of *C. elegans apb-1* through a new structure, cargo-binding assay, conditional knockout, or APB-1-specific interactome. The newest directly informative retrieved study was Wang et al., published November 2021, which localized APB-1 within intestinal AP-1/TGN sorting machinery and clarified its relationship to SMAP-1 and clathrin. (wang2021ap1recruitssmap1smaps pages 4-8)

Recent AP-2 research in *C. elegans* continues to use endocytic regulators and AP-2 subunits to examine clathrin dynamics. For example, reducing AP-2 activity partially suppressed abnormal clathrin accumulation in NIMA-kinase mutants: one background showed a 1.5-fold reduction in mean apical GFP–CHC-1 intensity and a 1.4-fold reduction in positive pixels. Those measurements concern AP-2 pathway regulation, not direct APB-1 perturbation. (joseph2020controlofclathrinmediated pages 9-12)

The absence of a 2023–2024 gene-specific advance is itself important: current annotation remains based primarily on conserved adaptor-complex architecture, older nematode genetics, and direct localization studies. Claims of a defined APB-1-specific cargo, catalytic activity, or unique AP-1-versus-AP-2 phenotype would exceed the available evidence.

## 7. Current applications and expert assessment

APB-1 presently has no clinical or industrial implementation. Its practical value is as an in vivo research handle for:

1. dissecting clathrin-mediated endocytosis and AP-2 hemicomplex organization;
2. studying AP-1-dependent TGN sorting and epithelial polarity;
3. testing how membrane traffic shapes synapses, oocytes, intestinal epithelia, and developing tubes; and
4. modeling conserved β-adaptin function relevant to metazoan membrane trafficking.

Authoritative reviews describe AP complexes as cargo-sorting and vesicle-formation machinery and emphasize AP-1 as a regulator of polarized transport. For APB-1 specifically, the strongest conclusion is that it is an essential, shared coat scaffold rather than an enzyme, transporter, or independently acting signaling molecule. (sato2014c.elegansas pages 4-6, nakatsu2014theroleof pages 4-6)

## 8. Confidence and unresolved questions

**High confidence:** identity as *C. elegans* β-adaptin; membership in both AP-1 and AP-2; β–μ2 hemicomplex behavior; localization to AP-2-associated neuronal/oocyte membranes and AP-1-associated intestinal puncta; essential developmental role. (gu2013ap2hemicomplexescontribute pages 6-8, sato2014c.elegansas pages 4-6, nakatsu2014theroleof pages 4-6, wang2021ap1recruitssmap1smaps pages 4-8)

**Moderate confidence:** direct participation in synaptic-vesicle recycling and polarized intestinal cargo sorting. The pathway evidence is strong, but several decisive phenotypes were produced by partner-subunit or pathway perturbations rather than an APB-1-specific conditional allele. (gu2013ap2hemicomplexescontribute pages 14-15, wang2021ap1recruitssmap1smaps pages 4-8)

**Unresolved:** whether APB-1 itself directly binds particular endogenous cargoes in the worm; the relative fractions allocated to AP-1 versus AP-2 in each tissue; its complete interaction network; and the structure of the native nematode APB-1-containing complexes.

## Key sources

* Gu et al. **“AP2 hemicomplexes contribute independently to synaptic vesicle endocytosis.”** *eLife*, March 2013. https://doi.org/10.7554/eLife.00190 (gu2013ap2hemicomplexescontribute pages 6-8, gu2013ap2hemicomplexescontribute pages 14-15)
* Sato et al. **“C. elegans as a model for membrane traffic.”** *WormBook*, April 2014. https://doi.org/10.1895/wormbook.1.77.2 (sato2014c.elegansas pages 4-6)
* Nakatsu et al. **“The Role of the Clathrin Adaptor AP-1: Polarized Sorting and Beyond.”** *Membranes*, November 2014. https://doi.org/10.3390/membranes4040747 (nakatsu2014theroleof pages 4-6)
* Wang et al. **“AP-1 Recruits SMAP-1/SMAPs to the trans-Golgi Network to Promote Sorting in Polarized Epithelia.”** *Frontiers in Cell and Developmental Biology*, November 2021. https://doi.org/10.3389/fcell.2021.774401 (wang2021ap1recruitssmap1smaps pages 4-8)
* Joseph et al. **“Control of clathrin-mediated endocytosis by NIMA family kinases.”** *PLOS Genetics*, February 18, 2020. https://doi.org/10.1371/journal.pgen.1008633 (joseph2020controlofclathrinmediated pages 9-12)

References

1. (gu2013ap2hemicomplexescontribute pages 6-8): Mingyu Gu, Qiang Liu, Shigeki Watanabe, Lin Sun, Gunther Hollopeter, Barth D Grant, and Erik M Jorgensen. Ap2 hemicomplexes contribute independently to synaptic vesicle endocytosis. eLife, Mar 2013. URL: https://doi.org/10.7554/elife.00190, doi:10.7554/elife.00190. This article has 103 citations and is from a domain leading peer-reviewed journal.

2. (sato2014c.elegansas pages 4-6): Ken Sato, A. Norris, Miyuki Sato, and B. Grant. C. elegans as a model for membrane traffic. WormBook : the online review of C. elegans biology, pages 1-47, Apr 2014. URL: https://doi.org/10.1895/wormbook.1.77.2, doi:10.1895/wormbook.1.77.2. This article has 126 citations.

3. (nakatsu2014theroleof pages 4-6): Fubito Nakatsu, Koji Hase, and Hiroshi Ohno. The role of the clathrin adaptor ap-1: polarized sorting and beyond. Membranes, 4:747-763, Nov 2014. URL: https://doi.org/10.3390/membranes4040747, doi:10.3390/membranes4040747. This article has 96 citations.

4. (gu2013ap2hemicomplexescontribute pages 4-6): Mingyu Gu, Qiang Liu, Shigeki Watanabe, Lin Sun, Gunther Hollopeter, Barth D Grant, and Erik M Jorgensen. Ap2 hemicomplexes contribute independently to synaptic vesicle endocytosis. eLife, Mar 2013. URL: https://doi.org/10.7554/elife.00190, doi:10.7554/elife.00190. This article has 103 citations and is from a domain leading peer-reviewed journal.

5. (wang2021ap1recruitssmap1smaps pages 4-8): Shimin Wang, Longfeng Yao, Wenjuan Zhang, Zihang Cheng, Can Hu, Hang Liu, Yanling Yan, and Anbing Shi. Ap-1 recruits smap-1/smaps to the trans-golgi network to promote sorting in polarized epithelia. Frontiers in Cell and Developmental Biology, Nov 2021. URL: https://doi.org/10.3389/fcell.2021.774401, doi:10.3389/fcell.2021.774401. This article has 5 citations.

6. (gu2013ap2hemicomplexescontribute pages 14-15): Mingyu Gu, Qiang Liu, Shigeki Watanabe, Lin Sun, Gunther Hollopeter, Barth D Grant, and Erik M Jorgensen. Ap2 hemicomplexes contribute independently to synaptic vesicle endocytosis. eLife, Mar 2013. URL: https://doi.org/10.7554/elife.00190, doi:10.7554/elife.00190. This article has 103 citations and is from a domain leading peer-reviewed journal.

7. (wang2021ap1recruitssmap1smaps pages 3-4): Shimin Wang, Longfeng Yao, Wenjuan Zhang, Zihang Cheng, Can Hu, Hang Liu, Yanling Yan, and Anbing Shi. Ap-1 recruits smap-1/smaps to the trans-golgi network to promote sorting in polarized epithelia. Frontiers in Cell and Developmental Biology, Nov 2021. URL: https://doi.org/10.3389/fcell.2021.774401, doi:10.3389/fcell.2021.774401. This article has 5 citations.

8. (zhang2012clathrinandap1 pages 1-1): Hongjie Zhang, Ahlee Kim, Nessy Abraham, Liakot A. Khan, David H. Hall, John T. Fleming, and Verena Gobel. Clathrin and ap-1 regulate apical polarity and lumen formation during c. elegans tubulogenesis. Development, 139:2071-2083, Jun 2012. URL: https://doi.org/10.1242/dev.077347, doi:10.1242/dev.077347. This article has 89 citations and is from a domain leading peer-reviewed journal.

9. (joseph2020controlofclathrinmediated pages 9-12): Braveen B. Joseph, Yu Wang, Phil Edeen, Vladimir Lažetić, Barth D. Grant, and David S. Fay. Control of clathrin-mediated endocytosis by nima family kinases. PLOS Genetics, 16:e1008633, Feb 2020. URL: https://doi.org/10.1371/journal.pgen.1008633, doi:10.1371/journal.pgen.1008633. This article has 49 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](apb-1-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. nakatsu2014theroleof pages 4-6
2. joseph2020controlofclathrinmediated pages 9-12
3. https://doi.org/10.7554/eLife.00190
4. https://doi.org/10.1895/wormbook.1.77.2
5. https://doi.org/10.3390/membranes4040747
6. https://doi.org/10.3389/fcell.2021.774401
7. https://doi.org/10.1371/journal.pgen.1008633
8. https://doi.org/10.7554/elife.00190,
9. https://doi.org/10.1895/wormbook.1.77.2,
10. https://doi.org/10.3390/membranes4040747,
11. https://doi.org/10.3389/fcell.2021.774401,
12. https://doi.org/10.1242/dev.077347,
13. https://doi.org/10.1371/journal.pgen.1008633,