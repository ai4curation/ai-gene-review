---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-25T04:19:49.975548'
end_time: '2026-09-25T04:30:23.879227'
duration_seconds: 633.9
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: yeast
  gene_id: MPS1
  gene_symbol: MPS1
  uniprot_accession: P54199
  protein_description: 'RecName: Full=Serine/threonine-protein kinase MPS1; EC=2.7.12.2
    {ECO:0000269|PubMed:11278681, ECO:0000269|PubMed:19269975, ECO:0000269|PubMed:22521787,
    ECO:0000269|PubMed:22561345}; AltName: Full=Monopolar spindle protein 1; AltName:
    Full=Regulatory cell proliferation kinase 1;'
  gene_info: Name=MPS1; Synonyms=RPK1; OrderedLocusNames=YDL028C; ORFNames=D2785;
  organism_full: Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
  protein_family: Belongs to the protein kinase superfamily. Ser/Thr protein
  protein_domains: Kinase-like_dom_sf. (IPR011009); Mps1. (IPR016242); Mps1_cat. (IPR027084);
    Prot_kinase_dom. (IPR000719); Protein_kinase_ATP_BS. (IPR017441)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 49
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: MPS1-deep-research-falcon_artifacts/artifact-00.md
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
- **UniProt Accession:** P54199
- **Protein Description:** RecName: Full=Serine/threonine-protein kinase MPS1; EC=2.7.12.2 {ECO:0000269|PubMed:11278681, ECO:0000269|PubMed:19269975, ECO:0000269|PubMed:22521787, ECO:0000269|PubMed:22561345}; AltName: Full=Monopolar spindle protein 1; AltName: Full=Regulatory cell proliferation kinase 1;
- **Gene Information:** Name=MPS1; Synonyms=RPK1; OrderedLocusNames=YDL028C; ORFNames=D2785;
- **Organism (full):** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
- **Protein Family:** Belongs to the protein kinase superfamily. Ser/Thr protein
- **Key Domains:** Kinase-like_dom_sf. (IPR011009); Mps1. (IPR016242); Mps1_cat. (IPR027084); Prot_kinase_dom. (IPR000719); Protein_kinase_ATP_BS. (IPR017441)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "MPS1" matches the protein description above**
2. **Verify the organism is correct:** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'MPS1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **MPS1** (gene ID: MPS1, UniProt: P54199) in yeast.

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
- **UniProt Accession:** P54199
- **Protein Description:** RecName: Full=Serine/threonine-protein kinase MPS1; EC=2.7.12.2 {ECO:0000269|PubMed:11278681, ECO:0000269|PubMed:19269975, ECO:0000269|PubMed:22521787, ECO:0000269|PubMed:22561345}; AltName: Full=Monopolar spindle protein 1; AltName: Full=Regulatory cell proliferation kinase 1;
- **Gene Information:** Name=MPS1; Synonyms=RPK1; OrderedLocusNames=YDL028C; ORFNames=D2785;
- **Organism (full):** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
- **Protein Family:** Belongs to the protein kinase superfamily. Ser/Thr protein
- **Key Domains:** Kinase-like_dom_sf. (IPR011009); Mps1. (IPR016242); Mps1_cat. (IPR027084); Prot_kinase_dom. (IPR000719); Protein_kinase_ATP_BS. (IPR017441)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "MPS1" matches the protein description above**
2. **Verify the organism is correct:** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'MPS1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **MPS1** (gene ID: MPS1, UniProt: P54199) in yeast.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Functional annotation report: *Saccharomyces cerevisiae* MPS1 (UniProt P54199)

## Executive summary

The requested protein is correctly identified as budding-yeast Mps1: **MPS1/YDL028C** (aliases **RPK1** and **D2785**) from *Saccharomyces cerevisiae* S288c, UniProt **P54199**. It is the essential Mps1-family protein kinase originally named for the **monopolar-spindle** phenotype. This identity is consistent with the supplied protein-kinase, Mps1 and Mps1-catalytic domain annotations and with yeast literature describing an essential kinase required for spindle-pole-body (SPB) duplication. It must not be confused with human MPS1/TTK or similarly named proteins in other organisms.

Mps1’s primary biochemical function is ATP-dependent protein phosphorylation. Its defining cellular role is best described as **spatially controlled phosphorylation at SPBs and kinetochores**. At SPBs, it drives organelle duplication and assembly. At unattached or immature kinetochores, it initiates the spindle-assembly checkpoint (SAC) and promotes accurate sister-kinetochore biorientation. These functions explain why loss of Mps1 causes both monopolar spindles and catastrophic chromosome segregation, whereas excessive Mps1 activates checkpoint-dependent mitotic arrest. Foundational experiments showed that the checkpoint defect persists even when SPB duplication has already occurred, establishing that SPB assembly and checkpoint signaling are separable Mps1 functions (weiss1996thesaccharomycescerevisiae pages 1-2, weiss1996thesaccharomycescerevisiae pages 10-12).

## 1. Identity verification and scope

The supplied record—P54199, MPS1/YDL028C, *S. cerevisiae* S288c—matches the protein described in the yeast literature as an essential protein kinase required for SPB duplication and spindle-integrity checkpoint signaling. Kinase-domain mutants fail to arrest after spindle damage, and recombinant yeast Mps1 exhibits autophosphorylation and substrate phosphorylation. The kinase can autophosphorylate serine, threonine and tyrosine in biochemical assays, although its physiological substrates are predominantly discussed as Ser/Thr phosphorylation targets (winey2002centrosomesandcheckpoints pages 5-6, weiss1996thesaccharomycescerevisiae pages 10-12, winey2002centrosomesandcheckpoints pages 6-7).

The **human protein MPS1/TTK is not the target**. Modern general SAC reviews frequently use “MPS1” to mean mammalian TTK; such findings were not treated here as direct evidence for P54199. Likewise, pathogenic-fungal Mps1 orthologs are considered only in the applications section and are explicitly separated from direct *S. cerevisiae* annotation.

## 2. Catalytic activity and substrate specificity

### 2.1 Reaction

Mps1 catalyzes transfer of the γ-phosphate of ATP to hydroxyl groups on protein substrates:

**ATP + protein Ser/Thr–OH → ADP + protein Ser/Thr–O-phosphate.**

The protein is therefore a regulatory protein kinase rather than a metabolic enzyme. Its effective specificity is determined not only by local phosphosite sequence but also by recruitment to SPBs or the outer kinetochore. Early biochemical work found that recombinant Mps1 could autophosphorylate and phosphorylate multiple substrates but did not support a rigid, uniquely predictive consensus sequence (weiss1996thesaccharomycescerevisiae pages 10-12, winey2002centrosomesandcheckpoints pages 6-7). More recent phosphoproteomic work suggests a relatively permissive preference, including acidic or related residues near a target threonine, but this 2025 evidence should be regarded as refinement beyond the user’s requested 2023–2024 priority window rather than the basis of the core annotation (nelson2025spindleintegrityis pages 3-5).

### 2.2 Experimentally supported substrate classes

**SPB substrates.** Spc42, Spc98 and Spc110 are phosphorylated by Mps1 in vitro, and their phosphorylation depends on Mps1 activity in vivo. Spc42 is especially important because Mps1 promotes its normal assembly into the SPB. Spc110 phosphosites can show conditional rather than stand-alone phenotypes, suggesting redundancy or combinatorial control with other kinases (winey2002centrosomesandcheckpoints pages 4-5, winey2002centrosomesandcheckpoints pages 3-4).

**Spc105/Knl1 MELT motifs.** At kinetochores, the best-supported signaling substrate is the outer-kinetochore scaffold Spc105, the budding-yeast KNL1 ortholog. Mps1 phosphorylation of its MELT motifs creates binding sites for Bub3–Bub1, establishing the kinetochore platform for SAC signaling. PP1/Glc7 bound to Spc105 opposes this modification, releases Bub1 and helps silence the checkpoint (benzi2020acommonmolecular pages 1-2, benzi2020acommonmolecular pages 5-6, benzi2020acommonmolecular pages 9-10).

**Bub1 and Mad1.** Bub1 recruitment depends on phosphorylated Spc105 and Bub1 itself is directly phosphorylated by Mps1, supporting subsequent Mad1-dependent signaling. Mad1 is phosphorylated by Mps1 in vitro; its hyperphosphorylation tracks with Mps1 overexpression, while Mps1 inhibition reduces Mad1 phosphorylation. Mad1 is consequently a strong biochemical candidate/target, although the physiological case in budding yeast is less complete than that for Spc105 (winey2002centrosomesandcheckpoints pages 4-5, benzi2020acommonmolecular pages 9-10).

**Ndc80 and Dam1-related control.** Mps1 phosphorylates kinetochore proteins involved in microtubule coupling, including Ndc80, and older work also supports Dam1 as an Mps1 target. These modifications contribute to attachment regulation, but they should not be conflated with Ipl1/Aurora-B phosphorylation, which is also central to error correction. The strongest unifying evidence for Mps1’s biorientation function remains the Spc105–Bub1 module (benzi2020acommonmolecular pages 9-10, nelson2025spindleintegrityis pages 27-28, nelson2025spindleintegrityis pages 17-18).

| Functional module | Cellular location | Direct/strongly supported substrate or interaction | Mechanistic output | Key evidence and evidence strength |
|---|---|---|---|---|
| Spindle-pole-body (SPB) duplication | SPB, the budding-yeast centrosome equivalent | Spc42, Spc98 and Spc110 are in-vitro substrates whose phosphorylation depends on Mps1 activity in vivo | Promotes multiple stages of SPB duplication and assembly, including normal Spc42 incorporation; loss of Mps1 produces a single SPB and monopolar spindle | Biochemical, localization and conditional-mutant evidence; **strong**, although the functional importance of individual phosphosites varies (weiss1996thesaccharomycescerevisiae pages 1-2, winey2002centrosomesandcheckpoints pages 4-5, winey2002centrosomesandcheckpoints pages 3-4) |
| Spindle-assembly checkpoint (SAC) initiation | Unattached kinetochores; checkpoint signal then acts in the nucleus | Mps1 phosphorylates Spc105/Knl1 MELT motifs, recruiting Bub1–Bub3; Mad1 is phosphorylated by Mps1 in vitro and becomes hyperphosphorylated when Mps1 is overexpressed | Builds the kinetochore checkpoint platform and promotes the Mad1–Mad2/Cdc20 pathway that restrains APC/C and anaphase | Genetic, biochemical, localization and overexpression evidence; **strongest for Spc105–Bub1/Bub3**, supportive for Mad1 as a direct physiological yeast substrate (winey2002centrosomesandcheckpoints pages 4-5, winey2002centrosomesandcheckpoints pages 5-6, benzi2020acommonmolecular pages 1-2, benzi2020acommonmolecular pages 9-10) |
| SAC silencing after attachment | Outer kinetochore | Spc105-bound PP1/Glc7 antagonizes Mps1-dependent MELT phosphorylation and removes Bub1 | Converts the kinetochore from a checkpoint-active to checkpoint-silent state after proper attachment | Suppressor genetics and localization evidence; **strong** (benzi2020acommonmolecular pages 1-2, benzi2020acommonmolecular pages 5-6, benzi2020acommonmolecular pages 9-10) |
| Chromosome biorientation and error correction | Outer kinetochore | Spc105 MELT motifs, PP1/Glc7 and recruited Bub1 form a shared regulatory module | Promotes correction/maturation of improper attachments and sister-kinetochore biorientation, partly independently of downstream Mad2 checkpoint arrest | In `mps1-3`, chromosome-loss-associated mating rose **1,000–2,000-fold**; only **42%** correctly segregated chromosome V and **41%** cosegregated both chromatids. Reducing PP1 action or tethering Bub1 to Spc105 rescued segregation; **strong genetic and cell-biological evidence** (benzi2020acommonmolecular pages 9-10, benzi2020acommonmolecular pages 2-3, benzi2020acommonmolecular pages 3-4) |
| Dynamic kinetochore recruitment | Ndc80 complex at the outer kinetochore | An N-terminal region of Mps1 binds a conserved Nuf2/Ndc80 calponin-homology-domain interaction hub; Dam1 complex can occupy the same or overlapping hub | Concentrates Mps1 near kinetochore substrates during attachment surveillance; mature Dam1-associated attachments disfavor Mps1 binding and help terminate checkpoint/error-correction signaling | Mutational, tethering, biochemical and cellular evidence; **strong**, with details of the open/closed-hub and competition sequence remaining partly model-based (parnell2024aconservedsite pages 11-12, parnell2023aninteractionhub pages 12-15, parnell2023aninteractionhub pages 33-37, pleuger2023ipl1controlledattachmentmaturation pages 22-25) |
| Meiosis | Meiotic SPBs, kinetochores and spindle–chromosome interface | No single substrate fully accounts for the phenotype; Mps1-dependent SPB duplication and kinetochore-attachment functions are implicated | Required for both meiotic SPB-duplication cycles, force-bearing end-on kinetochore–microtubule attachments, chromosome segregation in meiosis I and II, and meiosis-II cohesin protection | Conditional/hypomorphic genetics and live-cell imaging; **strong for requirement**, moderate for precise substrate-level mechanism (marston2017multipledutiesfor pages 7-8, winey2002centrosomesandcheckpoints pages 5-6, winey2002centrosomesandcheckpoints pages 3-4, winey2002centrosomesandcheckpoints pages 6-7) |
| Antifungal screening application | Engineered *S. cerevisiae* whole-cell assay | Overexpressed Mps1 orthologs from pathogenic fungi; this is **not direct P54199 biology**, although the host and reference response use *S. cerevisiae* Mps1 | Converts ortholog activity into growth inhibition, large-budded G2/M arrest and short bipolar spindles, providing a proposed screen for fungal-selective Mps1 inhibitors | Seven pathogenic-fungal orthologs were tested and two reproduced the arrest phenotype; **proof-of-concept platform evidence**, not a validated drug or clinical application (fabritius2024spindlecheckpointactivation pages 5-6, fabritius2024spindlecheckpointactivation pages 1-2) |


*Table: Evidence map for S. cerevisiae S288c Mps1/P54199, separating established SPB, kinetochore, checkpoint and meiotic functions from mechanistic models. The antifungal row is explicitly identified as an ortholog-screening application rather than direct P54199 biology.*

## 3. Spindle-pole-body duplication

The SPB is the budding-yeast centrosome equivalent and is embedded in the nuclear envelope. Mps1 localizes to SPBs and is required at multiple stages of their duplication and assembly. Conditional **mps1-1** cells fail to duplicate the SPB at restrictive temperature, producing one SPB and a monopolar spindle. Other alleles separate early and later assembly functions, demonstrating that Mps1 is not merely a checkpoint responder to a malformed spindle; it directly participates in SPB biogenesis (weiss1996thesaccharomycescerevisiae pages 1-2, winey2002centrosomesandcheckpoints pages 3-4).

The biochemical evidence aligns with this localization. Mps1 phosphorylates Spc42, Spc98 and Spc110, all structural or microtubule-nucleation-associated SPB components, and promotes normal Spc42 assembly. Thus, its broader structural role is to regulate construction of a duplication-competent SPB through phosphorylation of multiple components rather than to serve as a permanent architectural element itself (winey2002centrosomesandcheckpoints pages 4-5, winey2002centrosomesandcheckpoints pages 3-4).

This function is essential. When Mps1 fails, cells form monopolar spindles yet can inappropriately continue budding, DNA replication, mitotic progression and cytokinesis because the same mutant can also disable the checkpoint that should detect the defect. This coupled structural and surveillance failure explains the severe lethality and abnormal DNA content of mps1 mutants (weiss1996thesaccharomycescerevisiae pages 1-2, weiss1996thesaccharomycescerevisiae pages 10-12).

## 4. Spindle-assembly checkpoint signaling

### 4.1 Position in the pathway

Mps1 acts near the top of the SAC pathway. Unattached or immature kinetochores recruit Mps1, which phosphorylates Spc105 MELT motifs. Phosphorylated MELTs recruit Bub3–Bub1, enabling assembly of downstream Mad1–Mad2/Cdc20 signaling and ultimately an inhibitory mitotic checkpoint complex. This restrains APC/C-dependent destruction of securin/Pds1 and mitotic cyclins, delaying anaphase until kinetochore–microtubule attachment is satisfactory (hayward2019orchestrationofthe pages 1-2, benzi2020acommonmolecular pages 1-2, benzi2020acommonmolecular pages 9-10).

Overexpression of yeast Mps1 causes metaphase arrest even without obvious spindle damage; the arrest requires MAD1, MAD2, MAD3, BUB1 and BUB3, placing these factors downstream. Conversely, kinase-domain mutants fail to arrest after nocodazole-mediated microtubule depolymerization or SPB-duplication failure. The checkpoint defect remains when cells are synchronized after SPB duplication, proving it is not a secondary consequence of monopolar-spindle formation (weiss1996thesaccharomycescerevisiae pages 1-2, winey2002centrosomesandcheckpoints pages 5-6, weiss1996thesaccharomycescerevisiae pages 10-12).

### 4.2 Kinase–phosphatase switch

The SAC is controlled by an antagonistic Mps1–PP1 switch at Spc105. Mps1 creates phosphorylated MELT docking sites; Spc105-bound PP1/Glc7 removes these marks and promotes Bub1 release. Genetic suppressors of defective Mps1 that weaken PP1 action at Spc105 restore Bub1 localization, SAC proficiency and chromosome segregation, providing unusually direct evidence that the phosphorylation state of one scaffold coordinates checkpoint output with attachment control (benzi2020acommonmolecular pages 1-2, benzi2020acommonmolecular pages 5-6, benzi2020acommonmolecular pages 9-10).

## 5. Chromosome biorientation and attachment error correction

Mps1 does more than delay anaphase. It promotes formation or maturation of force-bearing kinetochore–microtubule attachments and sister-kinetochore biorientation. The **mps1-3 S635F** allele is particularly informative: these cells duplicate SPBs and make bipolar spindles, separating the chromosome phenotype from the classic SPB defect, yet they fail biorientation and SAC signaling (benzi2020acommonmolecular pages 1-2, benzi2020acommonmolecular pages 2-3, benzi2020acommonmolecular pages 3-4).

The quantitative defects are severe. Chromosome-loss-associated mating competence was **1,000–2,000-fold** above wild type. After release at 34°C, only **42%** of cells segregated chromosome V correctly, whereas **41%** retained both chromatids at one pole. Pericentromeric cohesion remained intact, arguing against premature cohesion loss and favoring defective attachment correction or biorientation (benzi2020acommonmolecular pages 2-3, benzi2020acommonmolecular pages 3-4).

Bub1 localization provides a molecular readout: at 34°C it was detected at kinetochores in **100% of wild-type cells** but at low levels in only **20% of mps1-3 cells** (wild type n=260; mutant n=170). Mutations reducing PP1 action at Spc105 restored Bub1 localization. Artificially tethering Bub1 or Bub3 to Spc105 rescued chromosome segregation and partially restored checkpoint signaling; importantly, segregation rescue persisted after MAD2 deletion. Therefore, the Spc105–Bub1 apparatus contributes directly to biorientation, not simply by prolonging mitosis through the downstream checkpoint (benzi2020acommonmolecular pages 9-10).

The most defensible current interpretation is that **Mps1 phosphorylation of Spc105 creates one sensory platform with two outputs**: checkpoint signaling and promotion of correct kinetochore attachment. Other Mps1 substrates almost certainly contribute, but the suppressor and tethering experiments make Spc105–Bub1 the best-supported shared mechanism (benzi2020acommonmolecular pages 1-2, benzi2020acommonmolecular pages 9-10, benzi2020acommonmolecular pages 2-3).

## 6. Localization and spatial regulation

Mps1 carries out its major functions at two nuclear structures:

1. **Spindle pole bodies**, where it phosphorylates assembly components and drives duplication.
2. **Outer kinetochores**, especially unattached or immature ones, where it is positioned near Spc105, Bub1/Mad1 and microtubule-coupling machinery (winey2002centrosomesandcheckpoints pages 4-5, winey2002centrosomesandcheckpoints pages 5-6, winey2002centrosomesandcheckpoints pages 3-4).

### Recent 2023–2024 mechanistic advance

Two 2023 preprints, subsequently represented by peer-reviewed 2024 work, refined how Mps1 is recruited and removed. An N-terminal region of Mps1 binds a conserved interaction hub in the Nuf2/Ndc80 calponin-homology-domain region. Mutating this hub disrupts Mps1 localization, checkpoint function and chromosome segregation; restoring Mps1–Ndc80 association by overexpression or engineered tethering rescues defects. This supports direct recruitment rather than nonspecific kinetochore proximity (parnell2023aninteractionhub pages 12-15, parnell2023aninteractionhub pages 33-37).

Parnell, Jenson and Miller’s peer-reviewed study was published in *Current Biology* on **June 3, 2024**, DOI [10.1016/j.cub.2024.04.054](https://doi.org/10.1016/j.cub.2024.04.054). It identified the Nuf2 interaction hub and showed graded effects of hub mutations while preserving Ndc80-complex assembly and microtubule binding, strengthening the conclusion that recruitment of Mps1 is a specific kinetochore function (parnell2024aconservedsite pages 11-12).

The leading attachment-maturation model proposes that movement or phosphorylation of the Ndc80 N-terminal tail exposes the hub, allowing Mps1 binding during error correction and checkpoint activation. As attachments mature, Dam1 complex occupies an overlapping site and displaces Mps1, separating the kinase from Spc105 and silencing the checkpoint. Ipl1/Aurora-B-dependent regulation contributes to this competition. Parts of this sequence—particularly the exact “open/closed” conformational transition—remain mechanistic interpretation rather than fully demonstrated chronology (parnell2024aconservedsite pages 11-12, parnell2023aninteractionhub pages 33-37, nelson2025spindleintegrityis pages 27-28, pleuger2023ipl1controlledattachmentmaturation pages 22-25).

An independent localization result from Benzi et al. showed wild-type Mps1 enrichment at centromeres of all **16 chromosomes**, whereas Mps1-3 lacked this enrichment. Artificial kinetochore tethering of Mps1-3 partially restored chromosome segregation, directly linking kinetochore residence to function (benzi2020acommonmolecular pages 5-6).

## 7. Meiosis

Mps1 is required during both meiotic divisions. It supports both rounds of SPB duplication, accurate chromosome segregation in meiosis I and II, and formation of force-bearing kinetochore–microtubule attachments. Hypomorphic alleles compatible with vegetative growth can nevertheless produce catastrophic meiotic segregation defects, showing that meiosis is especially sensitive to reduced Mps1 function (marston2017multipledutiesfor pages 7-8, winey2002centrosomesandcheckpoints pages 3-4, winey2002centrosomesandcheckpoints pages 6-7).

Live-cell work supports a role in converting lateral kinetochore contacts into stable end-on attachments. Mps1 is not required for pericentromeric cohesin protection in meiosis I but contributes to this process in meiosis II. A spore-wall-formation phenotype has also been reported, although its substrate-level mechanism appears distinct from the principal SPB/kinetochore pathway and is less precisely defined (marston2017multipledutiesfor pages 7-8, winey2002centrosomesandcheckpoints pages 6-7).

## 8. Recent applications and real-world relevance

The direct applications of *S. cerevisiae* P54199 are primarily experimental rather than clinical. Mps1 alleles, overexpression systems and engineered kinetochore tethering provide powerful tools for dissecting organelle duplication, checkpoint activation, phosphatase opposition and attachment maturation.

A 2024 study developed a possible antifungal-discovery application. Fabritius et al., published in *PLOS ONE* in **March 2024**, DOI [10.1371/journal.pone.0301084](https://doi.org/10.1371/journal.pone.0301084), expressed Mps1 orthologs from seven pathogenic fungi in budding yeast. Two—those from *Candida auris* and *C. albicans*—reproduced Mps1-overexpression phenotypes: growth inhibition, large-budded arrest, post-replication G2/M DNA content and short bipolar spindles. The proposed use is a whole-cell platform for identifying inhibitors of pathogenic-fungal Mps1 activity (fabritius2024spindlecheckpointactivation pages 5-6, fabritius2024spindlecheckpointactivation pages 1-2).

This is a **proof-of-concept screening platform**, not an approved antifungal strategy. Failure of most orthologs to produce a phenotype may reflect insufficient expression or poor recognition of *S. cerevisiae* substrates. The pathogenic-fungal proteins are not P54199; P54199 supplies the host-system benchmark and mechanistic rationale (fabritius2024spindlecheckpointactivation pages 5-6).

## 9. Evidence assessment and unresolved questions

The highest-confidence annotation is that Mps1 is an essential, spatially recruited protein kinase with three tightly related outputs: **SPB duplication, kinetochore attachment/biorientation, and SAC activation**. SPB substrates and the Spc105–Bub1 checkpoint module are supported by complementary genetics, biochemistry, localization and rescue experiments.

Important open questions remain. No short peptide consensus fully explains physiological substrate choice; localization and scaffold binding appear at least as important as primary sequence. The complete substrate set responsible for SPB duplication is unresolved, and individual SPB phosphosite mutants can be weak unless sensitized genetically. At kinetochores, Spc105 is the best-supported common target for SAC and biorientation, but Ndc80, Dam1, Bub1, Mad1 and potentially other substrates distribute Mps1’s effects across attachment formation, checkpoint amplification and spindle organization. Finally, the detailed order by which Ndc80-tail movement, Ipl1 activity, Dam1 binding and Mps1 autophosphorylation remove Mps1 from mature attachments remains an active mechanistic problem (winey2002centrosomesandcheckpoints pages 4-5, winey2002centrosomesandcheckpoints pages 6-7, parnell2024aconservedsite pages 11-12, parnell2023aninteractionhub pages 33-37).

## Key references

- Weiss EL, Winey M. **The *Saccharomyces cerevisiae* spindle pole body duplication gene MPS1 is part of a mitotic checkpoint.** *Journal of Cell Biology*. January 1996. [https://doi.org/10.1083/jcb.132.1.111](https://doi.org/10.1083/jcb.132.1.111) (weiss1996thesaccharomycescerevisiae pages 1-2, weiss1996thesaccharomycescerevisiae pages 10-12)
- Winey M, Huneycutt BJ. **Centrosomes and checkpoints: the MPS1 family of kinases.** *Oncogene*. September 2002. [https://doi.org/10.1038/sj.onc.1205712](https://doi.org/10.1038/sj.onc.1205712) (winey2002centrosomesandcheckpoints pages 4-5, winey2002centrosomesandcheckpoints pages 3-4)
- Marston AL, Wassmann K. **Multiple Duties for Spindle Assembly Checkpoint Kinases in Meiosis.** *Frontiers in Cell and Developmental Biology*. December 2017. [https://doi.org/10.3389/fcell.2017.00109](https://doi.org/10.3389/fcell.2017.00109) (marston2017multipledutiesfor pages 7-8)
- Benzi G et al. **A common molecular mechanism underlies the role of Mps1 in chromosome biorientation and the spindle assembly checkpoint.** *EMBO Reports*. April 2020. [https://doi.org/10.15252/embr.202050257](https://doi.org/10.15252/embr.202050257) (benzi2020acommonmolecular pages 1-2, benzi2020acommonmolecular pages 9-10, benzi2020acommonmolecular pages 2-3)
- McAinsh AD, Kops GJPL. **Principles and dynamics of spindle assembly checkpoint signalling.** *Nature Reviews Molecular Cell Biology*. Published online March 2023. [https://doi.org/10.1038/s41580-023-00593-z](https://doi.org/10.1038/s41580-023-00593-z)
- Parnell EJ, Jenson EE, Miller MP. **A conserved site on Ndc80 complex facilitates dynamic recruitment of Mps1 to yeast kinetochores to promote accurate chromosome segregation.** *Current Biology*. June 2024. [https://doi.org/10.1016/j.cub.2024.04.054](https://doi.org/10.1016/j.cub.2024.04.054) (parnell2024aconservedsite pages 11-12)
- Pleuger R et al. **Microtubule end-on attachment maturation regulates Mps1 association with its kinetochore receptor.** *Current Biology*. 2024. [https://doi.org/10.1016/j.cub.2024.03.062](https://doi.org/10.1016/j.cub.2024.03.062) (nelson2025spindleintegrityis pages 27-28)
- Fabritius AS et al. **Spindle checkpoint activation by fungal orthologs of the *S. cerevisiae* Mps1 kinase.** *PLOS ONE*. March 2024. [https://doi.org/10.1371/journal.pone.0301084](https://doi.org/10.1371/journal.pone.0301084) (fabritius2024spindlecheckpointactivation pages 5-6, fabritius2024spindlecheckpointactivation pages 1-2)

References

1. (weiss1996thesaccharomycescerevisiae pages 1-2): Eric L. Weiss and M. Winey. The saccharomyces cerevisiae spindle pole body duplication gene mps1 is part of a mitotic checkpoint. The Journal of Cell Biology, 132:111-123, Jan 1996. URL: https://doi.org/10.1083/jcb.132.1.111, doi:10.1083/jcb.132.1.111. This article has 633 citations.

2. (weiss1996thesaccharomycescerevisiae pages 10-12): Eric L. Weiss and M. Winey. The saccharomyces cerevisiae spindle pole body duplication gene mps1 is part of a mitotic checkpoint. The Journal of Cell Biology, 132:111-123, Jan 1996. URL: https://doi.org/10.1083/jcb.132.1.111, doi:10.1083/jcb.132.1.111. This article has 633 citations.

3. (winey2002centrosomesandcheckpoints pages 5-6): Mark Winey and Brenda J Huneycutt. Centrosomes and checkpoints: the mps1 family of kinases. Oncogene, 21:6161-6169, Sep 2002. URL: https://doi.org/10.1038/sj.onc.1205712, doi:10.1038/sj.onc.1205712. This article has 81 citations and is from a domain leading peer-reviewed journal.

4. (winey2002centrosomesandcheckpoints pages 6-7): Mark Winey and Brenda J Huneycutt. Centrosomes and checkpoints: the mps1 family of kinases. Oncogene, 21:6161-6169, Sep 2002. URL: https://doi.org/10.1038/sj.onc.1205712, doi:10.1038/sj.onc.1205712. This article has 81 citations and is from a domain leading peer-reviewed journal.

5. (nelson2025spindleintegrityis pages 3-5): Christian R. Nelson, Darren R. Mallett, and Sue Biggins. Spindle integrity is regulated by a phospho-dependent interaction between the ndc80 and dam1 kinetochore complexes. Apr 2025. URL: https://doi.org/10.1371/journal.pgen.1011645, doi:10.1371/journal.pgen.1011645. This article has 5 citations and is from a domain leading peer-reviewed journal.

6. (winey2002centrosomesandcheckpoints pages 4-5): Mark Winey and Brenda J Huneycutt. Centrosomes and checkpoints: the mps1 family of kinases. Oncogene, 21:6161-6169, Sep 2002. URL: https://doi.org/10.1038/sj.onc.1205712, doi:10.1038/sj.onc.1205712. This article has 81 citations and is from a domain leading peer-reviewed journal.

7. (winey2002centrosomesandcheckpoints pages 3-4): Mark Winey and Brenda J Huneycutt. Centrosomes and checkpoints: the mps1 family of kinases. Oncogene, 21:6161-6169, Sep 2002. URL: https://doi.org/10.1038/sj.onc.1205712, doi:10.1038/sj.onc.1205712. This article has 81 citations and is from a domain leading peer-reviewed journal.

8. (benzi2020acommonmolecular pages 1-2): Giorgia Benzi, Alain Camasses, Yoshimura Atsunori, Yuki Katou, Katsuhiko Shirahige, and Simonetta Piatti. A common molecular mechanism underlies the role of mps1 in chromosome biorientation and the spindle assembly checkpoint. EMBO reports, Apr 2020. URL: https://doi.org/10.15252/embr.202050257, doi:10.15252/embr.202050257. This article has 32 citations and is from a highest quality peer-reviewed journal.

9. (benzi2020acommonmolecular pages 5-6): Giorgia Benzi, Alain Camasses, Yoshimura Atsunori, Yuki Katou, Katsuhiko Shirahige, and Simonetta Piatti. A common molecular mechanism underlies the role of mps1 in chromosome biorientation and the spindle assembly checkpoint. EMBO reports, Apr 2020. URL: https://doi.org/10.15252/embr.202050257, doi:10.15252/embr.202050257. This article has 32 citations and is from a highest quality peer-reviewed journal.

10. (benzi2020acommonmolecular pages 9-10): Giorgia Benzi, Alain Camasses, Yoshimura Atsunori, Yuki Katou, Katsuhiko Shirahige, and Simonetta Piatti. A common molecular mechanism underlies the role of mps1 in chromosome biorientation and the spindle assembly checkpoint. EMBO reports, Apr 2020. URL: https://doi.org/10.15252/embr.202050257, doi:10.15252/embr.202050257. This article has 32 citations and is from a highest quality peer-reviewed journal.

11. (nelson2025spindleintegrityis pages 27-28): Christian R. Nelson, Darren R. Mallett, and Sue Biggins. Spindle integrity is regulated by a phospho-dependent interaction between the ndc80 and dam1 kinetochore complexes. Apr 2025. URL: https://doi.org/10.1371/journal.pgen.1011645, doi:10.1371/journal.pgen.1011645. This article has 5 citations and is from a domain leading peer-reviewed journal.

12. (nelson2025spindleintegrityis pages 17-18): Christian R. Nelson, Darren R. Mallett, and Sue Biggins. Spindle integrity is regulated by a phospho-dependent interaction between the ndc80 and dam1 kinetochore complexes. Apr 2025. URL: https://doi.org/10.1371/journal.pgen.1011645, doi:10.1371/journal.pgen.1011645. This article has 5 citations and is from a domain leading peer-reviewed journal.

13. (benzi2020acommonmolecular pages 2-3): Giorgia Benzi, Alain Camasses, Yoshimura Atsunori, Yuki Katou, Katsuhiko Shirahige, and Simonetta Piatti. A common molecular mechanism underlies the role of mps1 in chromosome biorientation and the spindle assembly checkpoint. EMBO reports, Apr 2020. URL: https://doi.org/10.15252/embr.202050257, doi:10.15252/embr.202050257. This article has 32 citations and is from a highest quality peer-reviewed journal.

14. (benzi2020acommonmolecular pages 3-4): Giorgia Benzi, Alain Camasses, Yoshimura Atsunori, Yuki Katou, Katsuhiko Shirahige, and Simonetta Piatti. A common molecular mechanism underlies the role of mps1 in chromosome biorientation and the spindle assembly checkpoint. EMBO reports, Apr 2020. URL: https://doi.org/10.15252/embr.202050257, doi:10.15252/embr.202050257. This article has 32 citations and is from a highest quality peer-reviewed journal.

15. (parnell2024aconservedsite pages 11-12): Emily J. Parnell, Erin E. Jenson, and Matthew P. Miller. A conserved site on ndc80 complex facilitates dynamic recruitment of mps1 to yeast kinetochores to promote accurate chromosome segregation. Current Biology, 34:2294-2307.e4, Jun 2024. URL: https://doi.org/10.1016/j.cub.2024.04.054, doi:10.1016/j.cub.2024.04.054. This article has 21 citations and is from a highest quality peer-reviewed journal.

16. (parnell2023aninteractionhub pages 12-15): Emily J. Parnell, Erin Jenson, and Matthew P. Miller. An interaction hub on ndc80 complex facilitates dynamic recruitment of mps1 to yeast kinetochores to promote accurate chromosome segregation. bioRxiv, Nov 2023. URL: https://doi.org/10.1101/2023.11.07.566082, doi:10.1101/2023.11.07.566082. This article has 5 citations.

17. (parnell2023aninteractionhub pages 33-37): Emily J. Parnell, Erin Jenson, and Matthew P. Miller. An interaction hub on ndc80 complex facilitates dynamic recruitment of mps1 to yeast kinetochores to promote accurate chromosome segregation. bioRxiv, Nov 2023. URL: https://doi.org/10.1101/2023.11.07.566082, doi:10.1101/2023.11.07.566082. This article has 5 citations.

18. (pleuger2023ipl1controlledattachmentmaturation pages 22-25): Richard Pleuger, Christian Cozma, Simone Hohoff, Christian Denkhaus, Alexander Dudziak, Farnusch Kaschani, Andrea Musacchio, Ingrid R. Vetter, and Stefan Westermann. Ipl1-controlled attachment maturation regulates mps1 association with its kinetochore receptor. bioRxiv, Nov 2023. URL: https://doi.org/10.1101/2023.10.30.564738, doi:10.1101/2023.10.30.564738. This article has 5 citations.

19. (marston2017multipledutiesfor pages 7-8): Adele L. Marston and Katja Wassmann. Multiple duties for spindle assembly checkpoint kinases in meiosis. Frontiers in Cell and Developmental Biology, Dec 2017. URL: https://doi.org/10.3389/fcell.2017.00109, doi:10.3389/fcell.2017.00109. This article has 109 citations.

20. (fabritius2024spindlecheckpointactivation pages 5-6): Amy S. Fabritius, Anabel Alonso, Andrew Wood, S. Sulthana, and Mark E. Winey. Spindle checkpoint activation by fungal orthologs of the s. cerevisiae mps1 kinase. PLOS ONE, 19:e0301084, Mar 2024. URL: https://doi.org/10.1371/journal.pone.0301084, doi:10.1371/journal.pone.0301084. This article has 0 citations and is from a peer-reviewed journal.

21. (fabritius2024spindlecheckpointactivation pages 1-2): Amy S. Fabritius, Anabel Alonso, Andrew Wood, S. Sulthana, and Mark E. Winey. Spindle checkpoint activation by fungal orthologs of the s. cerevisiae mps1 kinase. PLOS ONE, 19:e0301084, Mar 2024. URL: https://doi.org/10.1371/journal.pone.0301084, doi:10.1371/journal.pone.0301084. This article has 0 citations and is from a peer-reviewed journal.

22. (hayward2019orchestrationofthe pages 1-2): Daniel Hayward, Tatiana Alfonso‐Pérez, and Ulrike Gruneberg. Orchestration of the spindle assembly checkpoint by cdk1‐cyclin b1. FEBS Letters, 593:2889-2907, Sep 2019. URL: https://doi.org/10.1002/1873-3468.13591, doi:10.1002/1873-3468.13591. This article has 103 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](MPS1-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. nelson2025spindleintegrityis pages 3-5
2. benzi2020acommonmolecular pages 9-10
3. parnell2024aconservedsite pages 11-12
4. benzi2020acommonmolecular pages 5-6
5. fabritius2024spindlecheckpointactivation pages 5-6
6. marston2017multipledutiesfor pages 7-8
7. nelson2025spindleintegrityis pages 27-28
8. weiss1996thesaccharomycescerevisiae pages 1-2
9. weiss1996thesaccharomycescerevisiae pages 10-12
10. winey2002centrosomesandcheckpoints pages 5-6
11. winey2002centrosomesandcheckpoints pages 6-7
12. winey2002centrosomesandcheckpoints pages 4-5
13. winey2002centrosomesandcheckpoints pages 3-4
14. benzi2020acommonmolecular pages 1-2
15. nelson2025spindleintegrityis pages 17-18
16. benzi2020acommonmolecular pages 2-3
17. benzi2020acommonmolecular pages 3-4
18. parnell2023aninteractionhub pages 12-15
19. parnell2023aninteractionhub pages 33-37
20. fabritius2024spindlecheckpointactivation pages 1-2
21. hayward2019orchestrationofthe pages 1-2
22. 10.1016/j.cub.2024.04.054
23. 10.1371/journal.pone.0301084
24. https://doi.org/10.1083/jcb.132.1.111
25. https://doi.org/10.1038/sj.onc.1205712
26. https://doi.org/10.3389/fcell.2017.00109
27. https://doi.org/10.15252/embr.202050257
28. https://doi.org/10.1038/s41580-023-00593-z
29. https://doi.org/10.1016/j.cub.2024.04.054
30. https://doi.org/10.1016/j.cub.2024.03.062
31. https://doi.org/10.1371/journal.pone.0301084
32. https://doi.org/10.1083/jcb.132.1.111](https://doi.org/10.1083/jcb.132.1.111
33. https://doi.org/10.1038/sj.onc.1205712](https://doi.org/10.1038/sj.onc.1205712
34. https://doi.org/10.3389/fcell.2017.00109](https://doi.org/10.3389/fcell.2017.00109
35. https://doi.org/10.15252/embr.202050257](https://doi.org/10.15252/embr.202050257
36. https://doi.org/10.1038/s41580-023-00593-z](https://doi.org/10.1038/s41580-023-00593-z
37. https://doi.org/10.1016/j.cub.2024.04.054](https://doi.org/10.1016/j.cub.2024.04.054
38. https://doi.org/10.1016/j.cub.2024.03.062](https://doi.org/10.1016/j.cub.2024.03.062
39. https://doi.org/10.1371/journal.pone.0301084](https://doi.org/10.1371/journal.pone.0301084
40. https://doi.org/10.1083/jcb.132.1.111,
41. https://doi.org/10.1038/sj.onc.1205712,
42. https://doi.org/10.1371/journal.pgen.1011645,
43. https://doi.org/10.15252/embr.202050257,
44. https://doi.org/10.1016/j.cub.2024.04.054,
45. https://doi.org/10.1101/2023.11.07.566082,
46. https://doi.org/10.1101/2023.10.30.564738,
47. https://doi.org/10.3389/fcell.2017.00109,
48. https://doi.org/10.1371/journal.pone.0301084,
49. https://doi.org/10.1002/1873-3468.13591,