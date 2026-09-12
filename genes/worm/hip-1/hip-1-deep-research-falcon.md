---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-03T21:19:17.716608'
end_time: '2026-07-03T21:37:11.439955'
duration_seconds: 1073.72
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: worm
  gene_id: hip-1
  gene_symbol: hip-1
  uniprot_accession: G5EE04
  protein_description: 'SubName: Full=STI1 domain-containing protein {ECO:0000313|EMBL:CAB03349.1};'
  gene_info: Name=hip-1 {ECO:0000313|EMBL:CAB03349.1, ECO:0000313|WormBase:T12D8.8};
    ORFNames=CELE_T12D8.8 {ECO:0000313|EMBL:CAB03349.1}, T12D8.8 {ECO:0000313|WormBase:T12D8.8};
  organism_full: Caenorhabditis elegans.
  protein_family: Belongs to the FAM10 family.
  protein_domains: Hip_N. (IPR034649); STI1/HOP_DP. (IPR041243); STI1_HS-bd. (IPR006636);
    TPR-like_helical_dom_sf. (IPR011990); TPR_rpt. (IPR019734)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 30
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: hip-1-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: hip-1-deep-research-falcon_artifacts/artifact-01.md
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
- **UniProt Accession:** G5EE04
- **Protein Description:** SubName: Full=STI1 domain-containing protein {ECO:0000313|EMBL:CAB03349.1};
- **Gene Information:** Name=hip-1 {ECO:0000313|EMBL:CAB03349.1, ECO:0000313|WormBase:T12D8.8}; ORFNames=CELE_T12D8.8 {ECO:0000313|EMBL:CAB03349.1}, T12D8.8 {ECO:0000313|WormBase:T12D8.8};
- **Organism (full):** Caenorhabditis elegans.
- **Protein Family:** Belongs to the FAM10 family.
- **Key Domains:** Hip_N. (IPR034649); STI1/HOP_DP. (IPR041243); STI1_HS-bd. (IPR006636); TPR-like_helical_dom_sf. (IPR011990); TPR_rpt. (IPR019734)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "hip-1" matches the protein description above**
2. **Verify the organism is correct:** Caenorhabditis elegans.
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'hip-1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **hip-1** (gene ID: hip-1, UniProt: G5EE04) in worm.

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
- **UniProt Accession:** G5EE04
- **Protein Description:** SubName: Full=STI1 domain-containing protein {ECO:0000313|EMBL:CAB03349.1};
- **Gene Information:** Name=hip-1 {ECO:0000313|EMBL:CAB03349.1, ECO:0000313|WormBase:T12D8.8}; ORFNames=CELE_T12D8.8 {ECO:0000313|EMBL:CAB03349.1}, T12D8.8 {ECO:0000313|WormBase:T12D8.8};
- **Organism (full):** Caenorhabditis elegans.
- **Protein Family:** Belongs to the FAM10 family.
- **Key Domains:** Hip_N. (IPR034649); STI1/HOP_DP. (IPR041243); STI1_HS-bd. (IPR006636); TPR-like_helical_dom_sf. (IPR011990); TPR_rpt. (IPR019734)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "hip-1" matches the protein description above**
2. **Verify the organism is correct:** Caenorhabditis elegans.
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'hip-1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **hip-1** (gene ID: hip-1, UniProt: G5EE04) in worm.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Comprehensive Research Report: *C. elegans* hip-1 (T12D8.8) — An Hsp70 Co-chaperone of the Hip/ST13 Family

## 1. Gene Identity and Nomenclature

The *C. elegans* gene **hip-1** (systematic name T12D8.8; UniProt accession G5EE04) encodes an STI1 domain-containing protein that is the nematode ortholog of mammalian **Hip** (Hsp70-interacting protein), also known as **ST13** (Suppressor of Tumorigenicity 13) or **p48** (shi2007whatweknow pages 1-2). It is important to distinguish this protein from the *C. elegans* **sti-1** gene, which encodes the ortholog of HOP (Hsp70–Hsp90 organizing protein) — a related but functionally distinct co-chaperone (song2009c.eleganssti1 pages 8-9). While both Hip and Hop share STI1-type domains, they occupy different positions in the Hsp70 chaperone network. HIP-1 belongs to the **FAM10 protein family**, which is the gene family designation for ST13/Hip orthologs across eukaryotes (shi2007whatweknow pages 1-2). The protein is conserved across animals, plants, and protozoa, though notably absent from *Saccharomyces cerevisiae* and other fungi (li2013structureandfunction pages 31-35).

## 2. Protein Function: Hsp70 Co-chaperone Activity

### 2.1 Primary Molecular Function

HIP-1 functions as a **co-chaperone of the Hsp70 family of molecular chaperones**. Its primary biochemical activity is to **stabilize the ADP-bound state of Hsp70**, thereby prolonging Hsp70–substrate complexes and preventing premature substrate release (leak2014heatshockproteins pages 4-5, shi2007whatweknow pages 2-4). In mammalian systems, Hip binds to the nucleotide-binding domain (NBD/ATPase domain) of Hsp70 specifically when Hsp70 is in the ADP-bound conformation, with a dissociation constant (K_D) of approximately 8–10 µM (li2013structureandfunction pages 82-86, li2013structureandfunction pages 121-125). One Hip dimer binds two Hsp70 molecules (li2013structureandfunction pages 82-86).

Structurally, Hip's TPR domain forms a **"bracket" over the nucleotide-binding cleft of Hsp70**, dampening dynamic movement of subdomain IIB and slowing ADP dissociation (li2013structureandfunction pages 121-125, karunanayake2021cytosolicproteinquality pages 8-10). This mechanism locks Hsp70 in its high-affinity substrate-binding state (the "closed lid" state), effectively **attenuating the Hsp70 chaperone cycle** and extending the dwell time of substrates on the chaperone (li2013structureandfunction pages 31-35, li2013structureandfunction pages 125-129).

Hip also possesses **intrinsic holdase activity**: it can bind unfolded proteins and prevent their aggregation independently of Hsp70, though it cannot fold substrates on its own and has no ATPase activity (li2013structureandfunction pages 31-35, velten2002domainstructureof pages 7-7, velten2002domainstructureof pages 5-7).

### 2.2 Role in Protein Folding vs. Degradation Decisions

Hip functions as a **pro-folding co-chaperone** that biases the Hsp70 system toward protein refolding rather than degradation. It competes with the nucleotide exchange factor **BAG-1** for binding to the Hsp70 ATPase domain (shi2007whatweknow pages 2-4, leak2014heatshockproteins pages 4-5, li2013structureandfunction pages 31-35). While Hip stabilizes Hsp70–substrate complexes to promote refolding, BAG-1 stimulates ADP release and substrate dissociation, which can route substrates toward proteasomal degradation. Under normal cellular conditions, Hip is typically 5–10 times more abundant than BAG-1 or BAG-2, favoring the folding pathway (arndt2007tobeor pages 6-8). Importantly, Hip is not found in complexes with CHIP (the E3 ubiquitin ligase that links Hsp70 to the proteasome), suggesting steric incompatibility between the pro-folding (Hip) and pro-degradation (CHIP) co-chaperone pathways on Hsp70 (arndt2007tobeor pages 6-8).

## 3. Domain Architecture

The conserved domain architecture of HIP-1 inferred from the UniProt annotation and detailed structural studies of mammalian Hip is summarized below:

| Domain name | InterPro ID | Approximate residue positions in mammalian Hip/ST13 | Known function |
|---|---|---:|---|
| Hip_N | IPR034649 | 1–44 | N-terminal dimerization domain; forms a stable Hip dimer that supports avid Hsp70 binding and co-chaperone function (li2013structureandfunction pages 31-35, li2013structureandfunction pages 35-39) |
| STI1_HS-bd | IPR006636 | ~113–214 | TPR-containing Hsp70-binding module; binds the Hsp70 nucleotide-binding/ATPase domain preferentially in the ADP-bound state and stabilizes Hsp70-substrate complexes by slowing ADP release (li2013structureandfunction pages 31-35, li2013structureandfunction pages 121-125, shi2007whatweknow pages 1-2) |
| TPR repeat | IPR019734 | within ~113–214 | Repeated tetratricopeptide motifs that build the Hsp70-binding scaffold; mediate protein–protein interaction with Hsp70 and contribute to attenuation of the Hsp70 chaperone cycle (li2013structureandfunction pages 35-39, li2013structureandfunction pages 121-125) |
| TPR-like helical domain superfamily | IPR011990 | within ~113–214 | Helical superstructure underlying the TPR region; provides the structural scaffold for docking onto Hsp70’s nucleotide-binding domain and forming the “bracket” that stabilizes the ADP-bound conformation (li2013structureandfunction pages 121-125, karunanayake2021cytosolicproteinquality pages 8-10) |
| GGMP repeat region | — | ~278–311 | Flexible repeat-rich region with seven imperfect GGMP tetrapeptide repeats; precise role remains unresolved, but it is part of the conserved C-terminal region associated with Hip function in substrate/chaperone complexes (li2013structureandfunction pages 35-39, velten2002domainstructureof pages 5-7) |
| STI1/HOP_DP | IPR041243 | ~312–368 | C-terminal DP domain; contains hydrophobic grooves implicated in binding non-native substrate segments and is important for substrate/client handling and conformational maturation in vivo (li2013structureandfunction pages 31-35, li2013structureandfunction pages 35-39, li2013structureandfunction pages 121-125) |


*Table: This table summarizes the conserved domain architecture of C. elegans HIP-1/T12D8.8 inferred from UniProt domain calls and mechanistic studies of mammalian Hip/ST13. It is useful for mapping sequence features to likely co-chaperone functions in Hsp70-dependent proteostasis.*

The multi-domain organization is connected by long, negatively charged, disordered linkers that provide conformational flexibility, allowing Hip to recognize diverse Hsp70–substrate complexes (li2013structureandfunction pages 121-125). The N-terminal dimerization domain forms a compact α-helical dimer with slow subunit exchange (half-time ~6 hours), which is essential for avidity-based binding to multiple Hsp70 molecules simultaneously (li2013structureandfunction pages 35-39, li2013structureandfunction pages 125-129). The two-domain structural organization (an elongated N-terminal dimeric domain and a globular C-terminal domain) was also confirmed by limited proteolysis and biophysical characterization (velten2002domainstructureof pages 7-7, velten2002domainstructureof pages 5-7).

## 4. Subcellular Localization

Hip/ST13 is predominantly a **cytosolic protein**. Studies in mammalian cells demonstrate that Hip shows a **uniform distribution throughout the cytoplasm**, with an estimated concentration in reticulocyte lysate of approximately 1 µM (shi2007whatweknow pages 1-2, wu2019acytosolicchaperone pages 2-3, li2013structureandfunction pages 31-35). Immunostaining confirms cytosolic localization distinct from ER-associated punctate patterns (wu2019acytosolicchaperone pages 2-3). This cytoplasmic localization is consistent with its function as a co-chaperone of the cytosolic Hsp70 machinery. By inference, *C. elegans* HIP-1 is predicted to similarly function in the cytosol, where it can engage the nematode Hsp70 homologs (such as HSP-1) in their chaperone cycles.

## 5. Biological Roles and Experimental Evidence in *C. elegans*

### 5.1 Proteostasis and α-Synuclein Aggregation

The most direct experimental evidence for *C. elegans* HIP-1 function comes from a landmark study by Roodveldt et al. (2009) using a transgenic worm model expressing α-synuclein-YFP in body wall muscle cells. Key findings include:

- **RNAi knockdown of hip-1 (T12D8.8) significantly increased the number of α-synuclein inclusions by 2.3-fold** (P < 0.0001), demonstrating that HIP-1 is required for suppression of α-synuclein aggregation in vivo (roodveldt2009chaperoneproteostasisin pages 6-8, roodveldt2009chaperoneproteostasisin pages 8-10).

- **Double knockdown of hsp-70 (C12C8.1) and hip-1 reduced inclusions by approximately 60%** compared to single hip-1 knockdown, reaching a level similar to hsp-70 knockdown alone (roodveldt2009chaperoneproteostasisin pages 8-10, roodveldt2009chaperoneproteostasisin pages 10-10). This provides strong genetic evidence that HIP-1 acts **through and with Hsp70** in an epistatic relationship, functioning upstream of Hsp70 to modulate its anti-aggregation activity.

- **In vitro reconstitution** showed that addition of Hip to Hsp70 in the presence of ATP **completely suppressed the conversion of α-synuclein into amyloid species**, maintaining both Hsp70 and α-synuclein in solution (roodveldt2009chaperoneproteostasisin pages 6-8). Hip alone did not inhibit fibril formation, confirming that its anti-amyloidogenic activity is mediated through Hsp70 (roodveldt2009chaperoneproteostasisin pages 6-8).

The mechanistic model posits that without Hip, the ADP-bound Hsp70/α-synuclein complex can co-aggregate, depleting functional Hsp70 from solution and allowing rapid α-synuclein fibril formation. Hip stabilizes the ADP-Hsp70 complex and maintains Hsp70 in solution, thereby sustaining chaperone-mediated inhibition of amyloid pathways (roodveldt2009chaperoneproteostasisin pages 8-10, roodveldt2009chaperoneproteostasisin pages 10-10).

### 5.2 Chaperone Network Context in *C. elegans*

The *C. elegans* chaperone network includes a separate co-chaperone, STI-1, which is the ortholog of mammalian HOP/Stip1 and mediates client transfer from Hsp70 to Hsp90 (song2009c.eleganssti1 pages 8-9). CeSTI-1 is involved in aging and thermotolerance, with loss of function shortening lifespan by 68–77% at different temperatures (song2009c.eleganssti1 pages 8-9). HIP-1 and STI-1 thus occupy complementary roles in the nematode proteostasis network: HIP-1 stabilizes Hsp70–substrate complexes to promote the holding/folding function, while STI-1 facilitates substrate transfer between the Hsp70 and Hsp90 systems.

## 6. Emerging Roles: Mitochondrial Precursor Import

A recent study (Juszkiewicz et al., 2025) has identified a previously unappreciated function for St13/Hip in **mitochondrial precursor protein import**. St13 directly engages **mitochondrial targeting signals (MTS)** through the hydrophobic groove of its STI1 domain, accommodating the hydrophobic face of amphipathic MTS helices (juszkiewicz2025mechanismofchaperone pages 9-10). Upon emergence of the precursor polypeptide from the ribosome, St13 recruits and facilitates loading of Hsc70 onto the precursor, stabilizing Hsc70's ADP-bound state and maintaining the precursor in an unfolded, import-competent state (juszkiewicz2025mechanismofchaperone pages 9-10, juszkiewicz2025mechanismofchaperone pages 7-9). St13 also facilitates recruitment of the Stip1-Hsp90 system to these precursors (juszkiewicz2025mechanismofchaperone pages 7-9). The authors propose that St13 is the long-sought "presequence binding factor" (PBF), a ~50 kDa protein previously identified in early studies as interacting with mitochondrial presequences (juszkiewicz2025mechanismofchaperone pages 9-10). During mitochondrial import stress, this interaction becomes particularly important for buffering precursor degradation and preserving import competence (juszkiewicz2025mechanismofchaperone pages 1-2). This finding suggests that *C. elegans* HIP-1, by domain conservation, may similarly participate in mitochondrial protein biogenesis.

## 7. Summary of Key Evidence

| Study/Reference | Experimental approach | Key finding | Functional implication |
|---|---|---|---|
| Roodveldt et al., 2009, *EMBO Journal* | RNAi knockdown of **hip-1/T12D8.8** in a transgenic *C. elegans* α-synuclein-YFP inclusion model; confocal quantification of inclusions in young adults | **hip-1 RNAi increased α-synuclein inclusions 2.3-fold** relative to control (**P**<0.0001) (roodveldt2009chaperoneproteostasisin pages 6-8, roodveldt2009chaperoneproteostasisin pages 8-10) | hip-1 is required in vivo to suppress proteotoxic α-synuclein aggregation and supports proteostasis in the worm cytosol (roodveldt2009chaperoneproteostasisin pages 6-8, roodveldt2009chaperoneproteostasisin pages 10-10) |
| Roodveldt et al., 2009, *EMBO Journal* | Double RNAi knockdown of **hsp70 (C12C8.1) + hip-1 (T12D8.8)** in the same *C. elegans* α-synuclein model | Double knockdown **reduced inclusions by ~60% compared with hip-1 knockdown alone**, approaching the hsp70-knockdown phenotype (roodveldt2009chaperoneproteostasisin pages 8-10, roodveldt2009chaperoneproteostasisin pages 10-10) | Provides genetic evidence that hip-1 acts **through/with Hsp70**, functioning upstream to modulate Hsp70-dependent anti-aggregation activity (roodveldt2009chaperoneproteostasisin pages 8-10) |
| Roodveldt et al., 2009, *EMBO Journal* | In vitro α-synuclein aggregation assay with purified proteins; ThT fluorescence, TEM, and solubility analysis in the presence of **Hip + Hsp70 + ATP** | Addition of **Hip to Hsp70 in the presence of ATP completely suppressed conversion of α-synuclein into amyloid species** and maintained Hsp70 and α-synuclein in soluble form (roodveldt2009chaperoneproteostasisin pages 6-8, roodveldt2009chaperoneproteostasisin pages 1-2) | hip-1/Hip is an **Hsp70 co-chaperone** that prevents Hsp70 co-aggregation and stabilizes anti-amyloid chaperone function under ATP-turnover conditions (roodveldt2009chaperoneproteostasisin pages 6-8, roodveldt2009chaperoneproteostasisin pages 8-10) |
| Li et al., 2013, *Nature Structural & Molecular Biology* | Structural and biochemical characterization of mammalian Hip/ST13, including domain mapping and Hsp70-binding analysis | Hip’s **TPR domain binds the Hsp70 nucleotide-binding domain (NBD)** and forms a **bracket over the nucleotide-binding cleft**, stabilizing the **ADP-bound** state; Hip preferentially binds ADP-Hsp70 (KD ~8–10 µM) (li2013structureandfunction pages 121-125, li2013structureandfunction pages 82-86) | Explains the likely molecular mechanism of worm hip-1: a conserved Hip-family co-chaperone that **slows ADP release, prolongs substrate holding, and prevents premature substrate release** (li2013structureandfunction pages 31-35, li2013structureandfunction pages 121-125) |
| Juszkiewicz et al., 2025, *Molecular Biology of the Cell* | Biochemical and mechanistic analysis of St13 on mitochondrial precursor proteins and mitochondrial targeting signals (MTSs) | **St13 directly engages mitochondrial targeting signals** via its STI1 domain hydrophobic groove and recruits/retains **Hsc70/Hsp90** on precursors to maintain import competence (juszkiewicz2025mechanismofchaperone pages 9-10, juszkiewicz2025mechanismofchaperone pages 7-9, juszkiewicz2025mechanismofchaperone pages 1-2) | Expands Hip-family function beyond generic proteostasis: hip-1-like proteins can act in **mitochondrial precursor triage/import competence**, suggesting additional conserved roles for worm hip-1 inferred from domain architecture (juszkiewicz2025mechanismofchaperone pages 9-10, juszkiewicz2025mechanismofchaperone pages 1-2) |


*Table: This table summarizes the main experimental findings supporting functional annotation of C. elegans hip-1 and its orthologous Hip/ST13 mechanism. It links worm genetic evidence to conserved biochemical and structural studies that explain how HIP-1 acts as an Hsp70 co-chaperone.*

## 8. Conclusions

*C. elegans* **hip-1** (T12D8.8, UniProt G5EE04) encodes a cytosolic co-chaperone of the Hip/ST13/FAM10 family that functions as a critical regulator of Hsp70 chaperone activity. Its primary molecular function is to **stabilize the ADP-bound state of Hsp70**, prolonging substrate engagement and promoting protein folding over degradation. The protein achieves this through a conserved multi-domain architecture comprising an N-terminal dimerization domain (Hip_N), a central TPR domain that binds the Hsp70 ATPase domain, and a C-terminal DP domain involved in substrate interactions. Direct experimental evidence in *C. elegans* demonstrates that HIP-1 is essential for suppressing α-synuclein aggregation in an Hsp70-dependent manner (roodveldt2009chaperoneproteostasisin pages 6-8, roodveldt2009chaperoneproteostasisin pages 8-10). The protein functions in the cytosol where it participates in general proteostasis and, based on recent evidence from the conserved mammalian ortholog, may also play a role in maintaining mitochondrial precursor import competence (juszkiewicz2025mechanismofchaperone pages 9-10, juszkiewicz2025mechanismofchaperone pages 7-9). HIP-1 represents a key node in the *C. elegans* cytosolic protein quality control network, operating alongside but distinct from other co-chaperones such as STI-1/HOP and CHIP in directing client protein fate decisions.

References

1. (shi2007whatweknow pages 1-2): Zheng-zheng Shi, Jia-wei Zhang, and Shu Zheng. What we know about st13, a co-factor of heat shock protein, or a tumor suppressor? Journal of Zhejiang University SCIENCE B, 8:170-176, Mar 2007. URL: https://doi.org/10.1631/jzus.2007.b0170, doi:10.1631/jzus.2007.b0170. This article has 59 citations.

2. (song2009c.eleganssti1 pages 8-9): Hyun-Ok Song, Wonhae Lee, Kiyoung An, Hye-suk Lee, Jeong Hoon Cho, Zee-Yong Park, and Joohong Ahnn. C. elegans sti-1, the homolog of sti1/hop, is involved in aging and stress response. Journal of molecular biology, 390 4:604-17, Jul 2009. URL: https://doi.org/10.1016/j.jmb.2009.05.035, doi:10.1016/j.jmb.2009.05.035. This article has 68 citations and is from a domain leading peer-reviewed journal.

3. (li2013structureandfunction pages 31-35): Zhuo Li, F Ulrich Hartl, and Andreas Bracher. Structure and function of hip, an attenuator of the hsp70 chaperone cycle. Nature Structural &Molecular Biology, 20:929-935, Jun 2013. URL: https://doi.org/10.1038/nsmb.2608, doi:10.1038/nsmb.2608. This article has 97 citations.

4. (leak2014heatshockproteins pages 4-5): Rehana K. Leak. Heat shock proteins in neurodegenerative disorders and aging. Journal of Cell Communication and Signaling, 8:293-310, Sep 2014. URL: https://doi.org/10.1007/s12079-014-0243-9, doi:10.1007/s12079-014-0243-9. This article has 226 citations and is from a peer-reviewed journal.

5. (shi2007whatweknow pages 2-4): Zheng-zheng Shi, Jia-wei Zhang, and Shu Zheng. What we know about st13, a co-factor of heat shock protein, or a tumor suppressor? Journal of Zhejiang University SCIENCE B, 8:170-176, Mar 2007. URL: https://doi.org/10.1631/jzus.2007.b0170, doi:10.1631/jzus.2007.b0170. This article has 59 citations.

6. (li2013structureandfunction pages 82-86): Zhuo Li, F Ulrich Hartl, and Andreas Bracher. Structure and function of hip, an attenuator of the hsp70 chaperone cycle. Nature Structural &Molecular Biology, 20:929-935, Jun 2013. URL: https://doi.org/10.1038/nsmb.2608, doi:10.1038/nsmb.2608. This article has 97 citations.

7. (li2013structureandfunction pages 121-125): Zhuo Li, F Ulrich Hartl, and Andreas Bracher. Structure and function of hip, an attenuator of the hsp70 chaperone cycle. Nature Structural &Molecular Biology, 20:929-935, Jun 2013. URL: https://doi.org/10.1038/nsmb.2608, doi:10.1038/nsmb.2608. This article has 97 citations.

8. (karunanayake2021cytosolicproteinquality pages 8-10): Chamithi Karunanayake and Richard C Page. Cytosolic protein quality control machinery: interactions of hsp70 with a network of co-chaperones and substrates. Experimental Biology and Medicine, 246:1419-1434, Mar 2021. URL: https://doi.org/10.1177/1535370221999812, doi:10.1177/1535370221999812. This article has 21 citations and is from a peer-reviewed journal.

9. (li2013structureandfunction pages 125-129): Zhuo Li, F Ulrich Hartl, and Andreas Bracher. Structure and function of hip, an attenuator of the hsp70 chaperone cycle. Nature Structural &Molecular Biology, 20:929-935, Jun 2013. URL: https://doi.org/10.1038/nsmb.2608, doi:10.1038/nsmb.2608. This article has 97 citations.

10. (velten2002domainstructureof pages 7-7): Marion Velten, Nathalie Gomez-Vrielynck, Alain Chaffotte, and Moncef M. Ladjimi. Domain structure of the hsc70 cochaperone, hip*. The Journal of Biological Chemistry, 277:259-266, Jan 2002. URL: https://doi.org/10.1074/jbc.m106881200, doi:10.1074/jbc.m106881200. This article has 30 citations.

11. (velten2002domainstructureof pages 5-7): Marion Velten, Nathalie Gomez-Vrielynck, Alain Chaffotte, and Moncef M. Ladjimi. Domain structure of the hsc70 cochaperone, hip*. The Journal of Biological Chemistry, 277:259-266, Jan 2002. URL: https://doi.org/10.1074/jbc.m106881200, doi:10.1074/jbc.m106881200. This article has 30 citations.

12. (arndt2007tobeor pages 6-8): V. Arndt, Christian Rogon, and J. Höhfeld. To be, or not to be — molecular chaperones in protein degradation. Cellular and Molecular Life Sciences, 64:2525-2541, Jun 2007. URL: https://doi.org/10.1007/s00018-007-7188-6, doi:10.1007/s00018-007-7188-6. This article has 248 citations and is from a domain leading peer-reviewed journal.

13. (li2013structureandfunction pages 35-39): Zhuo Li, F Ulrich Hartl, and Andreas Bracher. Structure and function of hip, an attenuator of the hsp70 chaperone cycle. Nature Structural &Molecular Biology, 20:929-935, Jun 2013. URL: https://doi.org/10.1038/nsmb.2608, doi:10.1038/nsmb.2608. This article has 97 citations.

14. (wu2019acytosolicchaperone pages 2-3): Yang Wu, Jingzi Zhang, Lei Fang, Hon Cheung Lee, and Yong Juan Zhao. A cytosolic chaperone complex controls folding and degradation of type iii cd38. Journal of Biological Chemistry, 294:4247-4258, Mar 2019. URL: https://doi.org/10.1074/jbc.ra118.005844, doi:10.1074/jbc.ra118.005844. This article has 15 citations and is from a domain leading peer-reviewed journal.

15. (roodveldt2009chaperoneproteostasisin pages 6-8): Cintia Roodveldt, Carlos W Bertoncini, August Andersson, Annemieke T van der Goot, Shang-Te Hsu, Rafael Fernández-Montesinos, Jannie de Jong, Tjakko J van Ham, Ellen A Nollen, David Pozo, John Christodoulou, and Christopher M Dobson. Chaperone proteostasis in parkinson's disease: stabilization of the hsp70/α‐synuclein complex by hip. The EMBO Journal, 28:3758-3770, Dec 2009. URL: https://doi.org/10.1038/emboj.2009.298, doi:10.1038/emboj.2009.298. This article has 151 citations.

16. (roodveldt2009chaperoneproteostasisin pages 8-10): Cintia Roodveldt, Carlos W Bertoncini, August Andersson, Annemieke T van der Goot, Shang-Te Hsu, Rafael Fernández-Montesinos, Jannie de Jong, Tjakko J van Ham, Ellen A Nollen, David Pozo, John Christodoulou, and Christopher M Dobson. Chaperone proteostasis in parkinson's disease: stabilization of the hsp70/α‐synuclein complex by hip. The EMBO Journal, 28:3758-3770, Dec 2009. URL: https://doi.org/10.1038/emboj.2009.298, doi:10.1038/emboj.2009.298. This article has 151 citations.

17. (roodveldt2009chaperoneproteostasisin pages 10-10): Cintia Roodveldt, Carlos W Bertoncini, August Andersson, Annemieke T van der Goot, Shang-Te Hsu, Rafael Fernández-Montesinos, Jannie de Jong, Tjakko J van Ham, Ellen A Nollen, David Pozo, John Christodoulou, and Christopher M Dobson. Chaperone proteostasis in parkinson's disease: stabilization of the hsp70/α‐synuclein complex by hip. The EMBO Journal, 28:3758-3770, Dec 2009. URL: https://doi.org/10.1038/emboj.2009.298, doi:10.1038/emboj.2009.298. This article has 151 citations.

18. (juszkiewicz2025mechanismofchaperone pages 9-10): Szymon Juszkiewicz, Sew-Yeu Peak-Chew, and Ramanujan S. Hegde. Mechanism of chaperone recruitment and retention on mitochondrial precursors. Molecular Biology of the Cell, Jan 2025. URL: https://doi.org/10.1091/mbc.e25-01-0035, doi:10.1091/mbc.e25-01-0035. This article has 21 citations and is from a domain leading peer-reviewed journal.

19. (juszkiewicz2025mechanismofchaperone pages 7-9): Szymon Juszkiewicz, Sew-Yeu Peak-Chew, and Ramanujan S. Hegde. Mechanism of chaperone recruitment and retention on mitochondrial precursors. Molecular Biology of the Cell, Jan 2025. URL: https://doi.org/10.1091/mbc.e25-01-0035, doi:10.1091/mbc.e25-01-0035. This article has 21 citations and is from a domain leading peer-reviewed journal.

20. (juszkiewicz2025mechanismofchaperone pages 1-2): Szymon Juszkiewicz, Sew-Yeu Peak-Chew, and Ramanujan S. Hegde. Mechanism of chaperone recruitment and retention on mitochondrial precursors. Molecular Biology of the Cell, Jan 2025. URL: https://doi.org/10.1091/mbc.e25-01-0035, doi:10.1091/mbc.e25-01-0035. This article has 21 citations and is from a domain leading peer-reviewed journal.

21. (roodveldt2009chaperoneproteostasisin pages 1-2): Cintia Roodveldt, Carlos W Bertoncini, August Andersson, Annemieke T van der Goot, Shang-Te Hsu, Rafael Fernández-Montesinos, Jannie de Jong, Tjakko J van Ham, Ellen A Nollen, David Pozo, John Christodoulou, and Christopher M Dobson. Chaperone proteostasis in parkinson's disease: stabilization of the hsp70/α‐synuclein complex by hip. The EMBO Journal, 28:3758-3770, Dec 2009. URL: https://doi.org/10.1038/emboj.2009.298, doi:10.1038/emboj.2009.298. This article has 151 citations.

## Artifacts

- [Edison artifact artifact-00](hip-1-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](hip-1-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. shi2007whatweknow pages 1-2
2. li2013structureandfunction pages 31-35
3. li2013structureandfunction pages 82-86
4. arndt2007tobeor pages 6-8
5. li2013structureandfunction pages 121-125
6. wu2019acytosolicchaperone pages 2-3
7. roodveldt2009chaperoneproteostasisin pages 6-8
8. juszkiewicz2025mechanismofchaperone pages 9-10
9. juszkiewicz2025mechanismofchaperone pages 7-9
10. juszkiewicz2025mechanismofchaperone pages 1-2
11. roodveldt2009chaperoneproteostasisin pages 8-10
12. leak2014heatshockproteins pages 4-5
13. shi2007whatweknow pages 2-4
14. karunanayake2021cytosolicproteinquality pages 8-10
15. li2013structureandfunction pages 125-129
16. velten2002domainstructureof pages 7-7
17. velten2002domainstructureof pages 5-7
18. li2013structureandfunction pages 35-39
19. roodveldt2009chaperoneproteostasisin pages 10-10
20. roodveldt2009chaperoneproteostasisin pages 1-2
21. https://doi.org/10.1631/jzus.2007.b0170,
22. https://doi.org/10.1016/j.jmb.2009.05.035,
23. https://doi.org/10.1038/nsmb.2608,
24. https://doi.org/10.1007/s12079-014-0243-9,
25. https://doi.org/10.1177/1535370221999812,
26. https://doi.org/10.1074/jbc.m106881200,
27. https://doi.org/10.1007/s00018-007-7188-6,
28. https://doi.org/10.1074/jbc.ra118.005844,
29. https://doi.org/10.1038/emboj.2009.298,
30. https://doi.org/10.1091/mbc.e25-01-0035,