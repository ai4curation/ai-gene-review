---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-25T01:40:44.470217'
end_time: '2026-09-25T01:48:17.922155'
duration_seconds: 453.45
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: yeast
  gene_id: CDC28
  gene_symbol: CDC28
  uniprot_accession: P00546
  protein_description: 'RecName: Full=Cyclin-dependent kinase 1 {ECO:0000303|PubMed:14574415};
    Short=CDK1 {ECO:0000303|PubMed:14574415}; EC=2.7.11.22 {ECO:0000250|UniProtKB:P04551};
    AltName: Full=Cell division control protein 28; AltName: Full=Cell division protein
    kinase 1;'
  gene_info: Name=CDC28 {ECO:0000303|PubMed:6361575}; Synonyms=CDK1, HSL5, SRM5; OrderedLocusNames=YBR160W
    {ECO:0000312|SGD:S000000364}; ORFNames=YBR1211;
  organism_full: Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
  protein_family: Belongs to the protein kinase superfamily. CMGC Ser/Thr
  protein_domains: CDK. (IPR050108); Kinase-like_dom_sf. (IPR011009); Prot_kinase_dom.
    (IPR000719); Protein_kinase_ATP_BS. (IPR017441); Ser/Thr_kinase_AS. (IPR008271)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 27
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: CDC28-deep-research-falcon_artifacts/artifact-00.md
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
- **UniProt Accession:** P00546
- **Protein Description:** RecName: Full=Cyclin-dependent kinase 1 {ECO:0000303|PubMed:14574415}; Short=CDK1 {ECO:0000303|PubMed:14574415}; EC=2.7.11.22 {ECO:0000250|UniProtKB:P04551}; AltName: Full=Cell division control protein 28; AltName: Full=Cell division protein kinase 1;
- **Gene Information:** Name=CDC28 {ECO:0000303|PubMed:6361575}; Synonyms=CDK1, HSL5, SRM5; OrderedLocusNames=YBR160W {ECO:0000312|SGD:S000000364}; ORFNames=YBR1211;
- **Organism (full):** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
- **Protein Family:** Belongs to the protein kinase superfamily. CMGC Ser/Thr
- **Key Domains:** CDK. (IPR050108); Kinase-like_dom_sf. (IPR011009); Prot_kinase_dom. (IPR000719); Protein_kinase_ATP_BS. (IPR017441); Ser/Thr_kinase_AS. (IPR008271)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "CDC28" matches the protein description above**
2. **Verify the organism is correct:** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'CDC28' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **CDC28** (gene ID: CDC28, UniProt: P00546) in yeast.

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
- **UniProt Accession:** P00546
- **Protein Description:** RecName: Full=Cyclin-dependent kinase 1 {ECO:0000303|PubMed:14574415}; Short=CDK1 {ECO:0000303|PubMed:14574415}; EC=2.7.11.22 {ECO:0000250|UniProtKB:P04551}; AltName: Full=Cell division control protein 28; AltName: Full=Cell division protein kinase 1;
- **Gene Information:** Name=CDC28 {ECO:0000303|PubMed:6361575}; Synonyms=CDK1, HSL5, SRM5; OrderedLocusNames=YBR160W {ECO:0000312|SGD:S000000364}; ORFNames=YBR1211;
- **Organism (full):** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
- **Protein Family:** Belongs to the protein kinase superfamily. CMGC Ser/Thr
- **Key Domains:** CDK. (IPR050108); Kinase-like_dom_sf. (IPR011009); Prot_kinase_dom. (IPR000719); Protein_kinase_ATP_BS. (IPR017441); Ser/Thr_kinase_AS. (IPR008271)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "CDC28" matches the protein description above**
2. **Verify the organism is correct:** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'CDC28' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **CDC28** (gene ID: CDC28, UniProt: P00546) in yeast.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# CDC28/Cdk1 in *Saccharomyces cerevisiae*: Functional-annotation report

## Executive summary

**Identity was verified before interpretation.** The target is **CDC28 (YBR160W; UniProt P00546)** from *Saccharomyces cerevisiae* strain S288c, not a similarly named protein from another organism. The literature consistently identifies budding-yeast Cdc28 as the archetypal **Cdk1**, a cyclin-dependent, proline-directed serine/threonine protein kinase that partners sequentially with **nine cyclins—Cln1–3 and Clb1–6**. This agrees with the supplied CMGC protein-kinase/CDK domain annotation and EC 2.7.11.22 classification. No conflicting CDC28 identity was used. (robertson2020theroleand pages 34-38, pluta2024cyclin‐dependentkinasesmasters pages 5-6)

Cdc28 is the central catalytic engine of the budding-yeast division cycle. By changing cyclin partners and exploiting cyclin-docking motifs, Cks1-dependent phospho-priming, localization, and kinase/phosphatase feedback, the same catalytic subunit triggers Start, DNA replication, spindle assembly, chromosome segregation, and mitotic exit. Its best-supported molecular function is transfer of the terminal phosphate of ATP to serine or threonine residues in protein substrates; it preferentially recognizes **S/T-P-x-K/R**, also accepts minimal **S/T-P** sites, and can phosphorylate important non-proline-directed sites when distal docking supplies specificity. (ubersax2004cellcycleregulationby pages 14-19, valk2023cdksignalingvia pages 1-2)

## 1. Molecular function and substrate specificity

### Catalytic reaction

Cdc28 catalyzes the generic protein-kinase reaction:

**ATP + protein–Ser/Thr–OH → ADP + protein–Ser/Thr–OPO₃²⁻ + H⁺.**

It is not a kinase for one unique substrate. Rather, cyclin identity, substrate docking, prior phosphorylation, and intracellular context determine which proteins are modified. Cyclin binding both activates the kinase fold and contributes substrate-recognition surfaces. (ubersax2004cellcycleregulationby pages 14-19, robertson2020theroleand pages 34-38)

### A layered specificity code

1. **Active-site sequence preference:** the optimal motif is **S/T-P-x-K/R**, and the minimal motif is **S/T-P**. The proline at +1 is characteristic of CMGC-family, proline-directed kinases. (robertson2020theroleand pages 34-38, valk2023cdksignalingvia pages 1-2)
2. **Cyclin docking:** Cln1/2 recognize LP-rich motifs; Clb5/6 recognize RxL and the especially potent **NLxxxL** motif; Clb2 recognizes an **LxF** docking motif. These contacts increase phosphorylation efficiency and impose cell-cycle timing beyond that encoded by the phosphoacceptor sequence alone. (faustova2021anewlinear pages 1-2, ord2019cyclinspecificdockingmechanisms pages 1-3, bandyopadhyay2020comprehensiveanalysisof pages 1-4)
3. **Cks1-dependent multisite phosphorylation:** Cks1 binds phosphorylated priming sites and promotes ordered or semi-processive phosphorylation of additional sites. This mechanism is important for switch-like substrate responses such as Sic1 degradation and rapid Whi5 hyperphosphorylation. (xiao2024whi5hypoand pages 3-5, faustova2021anewlinear pages 1-2)
4. **Nonconventional sites:** a 2023 expert perspective emphasized that biologically important Cdc28 phosphorylation can occur at sites lacking +1 proline. Distal cyclin docking and Cks1-mediated priming compensate for weak active-site recognition; examples occur in Sic1 and Far1 phosphodegrons and in Swe1 regulation. Consequently, mutation only of canonical S/T-P sites can miss functional CDK signaling. (valk2023cdksignalingvia pages 1-2)

This layered model is now the most defensible description of Cdc28 substrate specificity: Cdc28 is intrinsically proline-directed, but biological specificity emerges from the complete **Cdc28–cyclin–Cks1–substrate** assembly rather than from a short consensus sequence alone.

## 2. Cell-cycle functions and pathways

The stage-resolved evidence is summarized below.

| Cell-cycle window / CDC28 complex | Principal mechanistic function | Representative direct substrates / evidence | Site of action / localization confidence |
|---|---|---|---|
| **Start / Cln3–Cdc28** | Executes Start control in G1 and promotes the cell-cycle transcriptional program that precedes DNA replication. Cln3 is one of the nine cyclins that bind Cdc28. | Available evidence supports Start control by Cdc28 but does not establish a specific direct Cln3–Cdc28 substrate in the gathered excerpts. (robertson2020theroleand pages 34-38, pluta2024cyclin‐dependentkinasesmasters pages 5-6) | **Inferred nuclear action:** Start transcription occurs in the nucleus, but the gathered evidence does not directly demonstrate localization of the Cln3–Cdc28 complex. |
| **Late G1 / Cln1/2–Cdc28** | Reinforces commitment to division by hyperphosphorylating and inactivating Whi5; phosphorylates mating-pathway regulators and the CDK inhibitor Sic1. LP docking motifs confer G1-cyclin selectivity. | **Whi5:** Cln1/2–Cdc28-dependent multisite hyperphosphorylation drives nuclear exclusion and full SBF-target transcription; Cks1 accelerates the process. **Sic1:** phosphorylation at six or more sites enables SCF–Cdc4-mediated destruction. **Ste5 and Ste20:** direct cyclin-selective phosphorylation is enhanced by Cln2-binding motifs. (xiao2024whi5hypoand pages 3-5, xiao2024whi5hypoand pages 1-3, ubersax2004cellcycleregulationby pages 14-19, bhaduri2011cyclinspecificdockingmotifs pages 1-2, bandyopadhyay2020comprehensiveanalysisof pages 1-4) | **Direct substrate localization:** Whi5 nuclear export after phosphorylation was experimentally observed. **Inferred kinase action:** nucleus for Whi5/Sic1 and cell cortex or mating-signaling assemblies for Ste5/Ste20; direct residence of Cdc28 at these sites was not established. |
| **S phase / Clb5/6–Cdc28** | Initiates DNA replication, prevents relicensing, and selects S-phase substrates through RxL and NLxxxL docking motifs. | **Sld2:** phosphorylation promotes Dpb11 binding and DNA synthesis. **Orc2/Orc6 and Cdc6:** phosphorylation contributes to once-per-cycle replication control. **Mcm10 S66:** 2024 IP–LC–MS/MS, phosphatase, co-IP, degron, and tethering experiments showed that phosphorylation strengthens Mcm10–MCM association; S66 became essential when the C-terminal MCM-binding region was removed. **Far1, Fin1, Lif1 and Slx4:** NLxxxL-dependent recognition by Clb5/6–Cdc28. (wang2024scdkregulatedbipartiteinteraction pages 2-3, wang2024scdkregulatedbipartiteinteraction pages 1-2, faustova2021anewlinear pages 1-2, ubersax2004cellcycleregulationby pages 19-24) | **Inferred replication-site action:** replication origins and MCM helicase assemblies are strongly supported by substrate function and interaction assays, but direct stable localization of Cdc28 at origins was not demonstrated in the gathered evidence. |
| **G2 / Clb3/4–Cdc28** | Couples completion of replication to spindle formation and the G2/M transition; Clb3/4 expression begins in early S phase and peaks in G2. | Affinity purification–mass spectrometry found **14 proteins** associated with Clb3–Protein A, including regulators connected to microtubules, septins and mitotic exit; these are interaction candidates rather than uniformly validated direct kinase substrates. (sopko2007explorationofgene pages 35-36) | **Functionally inferred:** spindle, spindle-pole-body and septin-associated sites. The gathered evidence does not directly demonstrate physical Cdc28 localization at these structures. |
| **Mitosis / Clb1/2–Cdc28** | Drives spindle elongation and mitotic morphology, inhibits spindle-pole-body reduplication, coordinates chromosome segregation, and restrains premature mitotic exit. Clb1/2-associated activity peaks about **10 min before anaphase**. | **Cdc6, Swe1 and Spo12:** LxF docking supports Clb2-selective regulation; Swe1 interactions participate in reciprocal inhibition, while Spo12 phosphorylation promotes Cdc14 release. **Pds1/securin:** phosphorylation regulates Esp1/separase binding and localization. **Cdh1:** Cdc28 phosphorylation prevents APC/C activation while mitotic CDK activity is high. (ubersax2004cellcycleregulationby pages 19-24, sopko2007explorationofgene pages 35-36, ord2019cyclinspecificdockingmechanisms pages 1-3, ubersax2004cellcycleregulationby pages 14-19) | **Mostly inferred sites of action:** nucleus/chromosomes, spindle and spindle-pole bodies from substrate functions. Cyclin localization can spatially direct Cdc28, but direct residence of Cdc28 at each site is not established here. |
| **Mitotic exit / Cdc14–APC/C–Cdh1–Sic1 antagonism of Cdc28** | Cdc14-dependent dephosphorylation and APC/C-mediated cyclin destruction lower Cdc28 activity; dephosphorylated Cdh1 activates APC/C, and reaccumulating Sic1 inhibits residual B-type cyclin–Cdc28, resetting cells to G1. | **Cdh1:** phosphorylation by Cdc28 inhibits APC/C activation; dephosphorylation at exit reverses this. **Sic1:** inhibits B-type cyclin–Cdc28 after its re-expression. Cdc28 decline also permits Swi5 nuclear entry, which supports the exit/G1 transcriptional state. (ubersax2004cellcycleregulationby pages 14-19, robertson2020theroleand pages 34-38) | **Direct substrate-localization evidence:** Cdh1 redistributes between the interphase nucleus and spindle-pole-body/centrosomal region in mitosis in a Cdc28-dependent manner; Swi5 nuclear entry follows Cdc28 inactivation. These observations localize regulatory consequences, not necessarily Cdc28 itself. |


*Table: Stage-resolved map of S. cerevisiae S288c Cdc28 complexes, mechanisms, representative substrates, and spatial evidence. It explicitly separates directly observed localization effects from sites inferred through substrate function.*

### Start and G1/S commitment

In early G1, low cyclin abundance and CDK inhibitors keep Cdc28 activity low. Cln3-associated activity promotes Start, after which Cln1/2–Cdc28 reinforces commitment through positive-feedback transcription and substrate phosphorylation. Cdc28 activity then remains elevated until anaphase before cyclin destruction and renewed CKI expression return cells to low-CDK G1. (robertson2020theroleand pages 34-38, pluta2024cyclin‐dependentkinasesmasters pages 5-6)

A particularly well-resolved substrate is **Whi5**, the inhibitor of SBF-dependent G1/S transcription. In 2024, Xiao and colleagues used synchronized cultures, Phos-tag immunoblotting, phosphatase treatment, and systematic phosphosite mutants to distinguish early-G1 hypophosphorylation from Cln1/2–Cdc28-driven hyperphosphorylation. They detected **19 appreciably phosphorylated sites**; seven sites account for early-G1 hypophosphorylation, while Cdk1-dependent multisite phosphorylation drives Whi5 nuclear export, full CLN2 expression, and timely progression through both G1/S and S/G2/M. Removing 12 Cdk sites—or all 19 sites—retained Whi5 in the nucleus and prolonged later cell-cycle phases. Cks1 was needed for rapid, complete late-G1 hyperphosphorylation. Published June 2024, DOI: https://doi.org/10.1016/j.cub.2024.04.052. (xiao2024whi5hypoand pages 3-5, xiao2024whi5hypoand pages 1-3)

Cln1/2–Cdc28 also phosphorylates the mating-pathway proteins Ste5 and Ste20 through Cln-selective docking, helping suppress pheromone signaling as cells commit to division. Far1 phosphorylation promotes its degradation and releases CDK inhibition. Direct docking experiments showed that substrate motifs could enhance phosphorylation in vivo, act at variable distances from phosphoacceptors, and be exchanged between substrates. Published October 2011, DOI: https://doi.org/10.1016/j.cub.2011.08.033. (ubersax2004cellcycleregulationby pages 14-19, bhaduri2011cyclinspecificdockingmotifs pages 1-2)

### DNA-replication initiation and prevention of rereplication

S-phase Clb5/6–Cdc28 phosphorylates replication factors to initiate DNA synthesis while preventing relicensing. Established targets include **Sld2**, whose phosphorylation enables Dpb11 association; **Cdc6**, whose phosphorylation promotes SCF–Cdc4-dependent destabilization; and Orc2/Orc6, whose modification contributes to once-per-cycle replication. Combined nonphosphorylatable mutations in licensing controls can produce rereplication, supporting a causal—not merely correlative—role. (ubersax2004cellcycleregulationby pages 19-24)

A 2024 study added **Mcm10 S66** to this mechanism. IP–LC–MS/MS identified eight candidate Mcm10 phosphosites, while phosphatase-sensitive mobility shifts and co-immunoprecipitation associated phosphorylation with stronger Mcm10–MCM binding. S66A alone caused only a mild phenotype when the major C-terminal MCM-binding domain was intact, but it became lethal and severely impaired S-phase entry when residues 463–571 were removed. Artificial tethering of the mutant Mcm10 to MCM rescued viability and S-phase progression, supporting a bipartite interaction in which S-CDK phosphorylation strengthens the lower-affinity N-terminal contact. Published September 2024, DOI: https://doi.org/10.3389/fcell.2024.1420033. (wang2024scdkregulatedbipartiteinteraction pages 2-3, wang2024scdkregulatedbipartiteinteraction pages 1-2)

Clb5/6 select additional substrates through **NLxxxL**, a motif reported to be more potent than conventional RxL docking. Far1 truncation/mutagenesis and quantitative time-lapse fluorescence established S-CDK-selective recognition; Fin1, Lif1, and Slx4 use the same mechanism, linking Cdc28 to spindle regulation and DNA repair as well as replication. Published November 2021, DOI: https://doi.org/10.15252/embj.2020105839. (faustova2021anewlinear pages 1-2)

### G2, mitosis, and chromosome segregation

Clb3/4-associated Cdc28 contributes to replication completion, spindle formation, and G2/M progression. Their expression begins in early S phase and peaks in G2. Clb1/2–Cdc28 activity peaks approximately **10 minutes before anaphase** and promotes spindle elongation and mitotic morphology while preventing spindle-pole-body reduplication. Affinity purification–mass spectrometry recovered **14 Clb3-associated** and **10 Clb2-associated** proteins, although association does not by itself establish direct phosphorylation. (sopko2007explorationofgene pages 35-36)

Mechanistically supported mitotic targets include Pds1/securin, Cdc6, Swe1, Cdh1, and Spo12. Clb2-dependent LxF docking and Cks1 interactions tune Cdc6 and Swe1 regulation; Spo12 phosphorylation promotes Cdc14 release. Cdc28 phosphorylation of Cdh1 keeps APC/C–Cdh1 inactive while mitotic CDK activity must remain high. (ubersax2004cellcycleregulationby pages 19-24, ord2019cyclinspecificdockingmechanisms pages 1-3, ubersax2004cellcycleregulationby pages 14-19)

### Mitotic exit and reset to G1

Mitotic exit requires reversal of the Cdc28 phosphorylation state. APC/C-mediated cyclin destruction lowers kinase activity; Cdc14-dependent dephosphorylation activates Cdh1 and promotes the low-CDK state; and reaccumulated Sic1 inhibits residual B-type cyclin–Cdc28. Cdc28 therefore participates in a bistable control system: it promotes the high-CDK mitotic state while APC/C, Cdc14, and Sic1 cooperate to terminate that state. (ubersax2004cellcycleregulationby pages 14-19, robertson2020theroleand pages 34-38)

### Additional precisely supported functions

Cdc28 phosphorylation couples morphogenesis to division: Gin4 phosphorylation promotes septin association, and Swe1-mediated checkpoint regulation links bud formation to mitotic entry. Cdc28 also regulates transcription directly and indirectly; a 2024 review describes roles in cell-cycle transcription factors, RNA-polymerase-II CTD phosphorylation, proteasome recruitment to selected promoters, and maintenance of selected highly expressed genes. These broader transcriptional assignments are credible but less central to the protein’s primary annotation than its cell-cycle kinase function. Published September 2024, DOI: https://doi.org/10.1002/wrna.1816. (pluta2024cyclin‐dependentkinasesmasters pages 5-6, ubersax2004cellcycleregulationby pages 14-19)

## 3. Regulation of Cdc28 activity

Cdc28 is controlled at several levels:

- **Cyclin binding:** sequential accumulation of Cln1–3 and Clb1–6 activates and retargets Cdc28. (robertson2020theroleand pages 34-38)
- **T-loop activation:** Cak1 phosphorylates the Cdc28 activation loop, stabilizing the active cyclin-bound conformation. The established residue is T169, although the retrieved excerpt supports T-loop phosphorylation rather than independently displaying its residue number. (robertson2020theroleand pages 34-38)
- **Inhibitory phosphorylation:** Swe1 phosphorylates **Y19**, restraining mitotic entry when morphogenesis is defective. Mih1 is the counteracting phosphatase in the canonical pathway; the retrieved evidence directly supports Swe1–Y19 but was not sufficient to document Mih1 mechanistically in detail. (ubersax2004cellcycleregulationby pages 19-24)
- **Stoichiometric inhibitors:** Sic1 inhibits B-type cyclin complexes, while Far1 couples mating signals to G1 arrest. Cdc28-dependent multisite phosphorylation targets these inhibitors for destruction when division resumes. (ubersax2004cellcycleregulationby pages 14-19, faustova2021anewlinear pages 1-2)
- **Proteolysis and phosphatase opposition:** SCF ubiquitin ligases remove selected phosphorylated inhibitors/substrates; APC/C removes mitotic cyclins; Cdc14 and other phosphatases reverse CDK phosphorylation at mitotic exit. (ubersax2004cellcycleregulationby pages 14-19)

## 4. Subcellular localization and site of action

Cdc28 should not be annotated as a protein with one invariant compartment. Its activity is spatially distributed by cyclins, docking interactions, and substrate localization. The evidence supports major action in the **nucleus**—on Whi5, replication factors, chromosome-segregation regulators, and transcriptional proteins—and functional action at **replication origins/MCM complexes, the mitotic spindle and spindle-pole bodies, and bud-neck/septin structures**. However, many of those locations are inferred from direct substrates and cyclin-associated functions rather than from proof that Cdc28 is stably resident there. (ubersax2004cellcycleregulationby pages 14-19, sopko2007explorationofgene pages 35-36)

The strongest spatial observations in the retrieved evidence concern substrates: Cdc28-dependent Whi5 phosphorylation causes nuclear exclusion; Swi5 enters the nucleus after Cdc28 inactivation; Cdh1 redistributes between the interphase nucleus and the spindle-pole-body/centrosomal region in a Cdc28-dependent manner; and Gin4 phosphorylation promotes association with bud-neck septins. Thus the conservative localization annotation is **nuclear and cytoplasmic, with cell-cycle-regulated activity at nuclear replication/chromosome structures and cortical division machinery**, while avoiding an unsupported claim of permanent Cdc28 residence at every site. (xiao2024whi5hypoand pages 3-5, ubersax2004cellcycleregulationby pages 14-19)

## 5. Experimental evidence, quantitative scope, and applications

A major enabling technology is **analog-sensitive Cdc28 (cdc28-as1)**. Replacing a bulky ATP-pocket residue enlarges the pocket so the mutant kinase accepts radiolabeled bulky ATP analogs and is selectively inhibited by 1-NM-PP1. This permits rapid, reversible perturbation and direct substrate labeling while largely retaining substrate-binding specificity. (ubersax2004cellcycleregulationby pages 60-65, ubersax2004cellcycleregulationby pages 8-14)

A proteome-scale GST-ORF screen found **181 efficiently phosphorylated proteins** among 500 candidates plus 200 random proteins and led to an estimate of roughly **500 potential Cdc28 substrates**. Of 169 candidates tested subsequently, about **30** showed mobility shifts and **14** underwent rapid inhibitor-dependent dephosphorylation in vivo. These figures demonstrate Cdc28’s broad reach but also show why an in-vitro hit must not automatically be called a physiological substrate. (ubersax2004cellcycleregulationby pages 8-14)

Current real-world implementations are primarily research and biotechnology tools rather than direct clinical uses of yeast CDC28:

- acute chemical-genetic synchronization and reversible cell-cycle arrest;
- direct kinase-substrate mapping with orthogonal ATP analogs;
- phosphoproteomic reconstruction of cell-cycle networks;
- synthetic tuning of Start, replication, and division timing through docking motifs or phosphosite engineering;
- a conserved model for human CDK1 regulation and CDK-inhibitor mechanism. The evolutionary value is substantial: one budding-yeast Cdc28 catalytic subunit performs tasks distributed among more specialized metazoan CDKs. (ubersax2004cellcycleregulationby pages 60-65, ubersax2004cellcycleregulationby pages 8-14, pluta2024cyclin‐dependentkinasesmasters pages 5-6)

## 6. Recent developments and expert assessment

The most important 2023–2024 conceptual advance is refinement of the old “consensus-site-only” model. The 2023 analysis argues that nonconventional sites, cyclin SLiMs, and Cks1-dependent priming create a much wider range of phosphorylation rates and CDK thresholds than S/T-P counting predicts. Published November 2023, DOI: https://doi.org/10.1091/mbc.e22-06-0196. (valk2023cdksignalingvia pages 1-2)

The 2024 Whi5 work shows experimentally that hypo- and hyperphosphorylation are distinct regulatory states: early phosphorylation can facilitate entry, whereas Cdc28/Cks1-dependent hyperphosphorylation controls nuclear export and progression beyond Start. The 2024 Mcm10 study similarly shows that a phosphorylation event may appear dispensable until redundant binding architecture is removed. Together, these studies support a modern view in which Cdc28 phosphorylation often adjusts multivalent interaction strength, localization, and kinetic thresholds rather than acting as a simple binary switch. (xiao2024whi5hypoand pages 3-5, wang2024scdkregulatedbipartiteinteraction pages 2-3)

## Functional annotation conclusion

**Primary function:** CDC28 encodes the essential canonical budding-yeast Cdk1 catalytic subunit, a cyclin-dependent Ser/Thr protein kinase that phosphorylates stage-specific protein substrates to order the cell cycle.

**Best-supported substrate rule:** preference for S/T-P-x-K/R and S/T-P, expanded by noncanonical sites when cyclin docking and Cks1-dependent priming provide specificity.

**Principal processes:** Start and G1/S transcription, suppression of mating arrest, replication initiation and licensing control, spindle and septin regulation, chromosome segregation, and control of mitotic exit.

**Site of function:** predominantly nuclear cell-cycle pathways, with dynamically targeted activity at replication complexes, spindle/SPB-associated machinery, and bud-neck/septin structures; several of these are inferred sites of action rather than constitutive physical localization.

**Confidence:** very high for identity, catalytic class, cyclin dependence, and central cell-cycle role; high for the named mechanistically validated substrates; moderate for comprehensive substrate inventories and for physical localization at every inferred cellular structure.

References

1. (robertson2020theroleand pages 34-38): CM Robertson. The role and regulation of rif1 as an anti-checkpoint protein in s. cerevisiae. Unknown journal, 2020.

2. (pluta2024cyclin‐dependentkinasesmasters pages 5-6): Aleksandra J. Pluta, Cécilia Studniarek, Shona Murphy, and Chris J. Norbury. Cyclin‐dependent kinases: masters of the eukaryotic universe. Wiley Interdisciplinary Reviews. RNA, Sep 2024. URL: https://doi.org/10.1002/wrna.1816, doi:10.1002/wrna.1816. This article has 66 citations and is from a peer-reviewed journal.

3. (ubersax2004cellcycleregulationby pages 14-19): JA Ubersax. Cell-cycle regulation by cdk1 in saccharomyces cerevisiae. Unknown journal, 2004.

4. (valk2023cdksignalingvia pages 1-2): Ervin Valk, Mihkel Örd, Ilona Faustova, and Mart Loog. Cdk signaling via nonconventional cdk phosphorylation sites. Molecular Biology of the Cell, Nov 2023. URL: https://doi.org/10.1091/mbc.e22-06-0196, doi:10.1091/mbc.e22-06-0196. This article has 26 citations and is from a domain leading peer-reviewed journal.

5. (faustova2021anewlinear pages 1-2): Ilona Faustova, Luka Bulatovic, Frida Matiyevskaya, Ervin Valk, Mihkel Örd, and Mart Loog. A new linear cyclin docking motif that mediates exclusively s‐phase cdk‐specific signaling. The EMBO Journal, Nov 2021. URL: https://doi.org/10.15252/embj.2020105839, doi:10.15252/embj.2020105839. This article has 40 citations.

6. (ord2019cyclinspecificdockingmechanisms pages 1-3): Mihkel Örd, Rainis Venta, Kaidi Möll, Ervin Valk, and Mart Loog. Cyclin-specific docking mechanisms reveal the complexity of m-cdk function in the cell cycle. Molecular Cell, 75:76-89.e3, Jul 2019. URL: https://doi.org/10.1016/j.molcel.2019.04.026, doi:10.1016/j.molcel.2019.04.026. This article has 94 citations and is from a highest quality peer-reviewed journal.

7. (bandyopadhyay2020comprehensiveanalysisof pages 1-4): Sushobhana Bandyopadhyay, Samyabrata Bhaduri, Mihkel Örd, Norman E. Davey, Mart Loog, and Peter M. Pryciak. Comprehensive analysis of fungal g1 cyclin docking motif sequences that control cdk regulatory potency in vivo. bioRxiv, Mar 2020. URL: https://doi.org/10.1101/2020.03.02.973354, doi:10.1101/2020.03.02.973354. This article has 0 citations.

8. (xiao2024whi5hypoand pages 3-5): Jordan Xiao, Jonathan J. Turner, Mardo Kõivomägi, and Jan M. Skotheim. Whi5 hypo- and hyper-phosphorylation dynamics control cell-cycle entry and progression. Jun 2024. URL: https://doi.org/10.1016/j.cub.2024.04.052, doi:10.1016/j.cub.2024.04.052. This article has 19 citations and is from a highest quality peer-reviewed journal.

9. (xiao2024whi5hypoand pages 1-3): Jordan Xiao, Jonathan J. Turner, Mardo Kõivomägi, and Jan M. Skotheim. Whi5 hypo- and hyper-phosphorylation dynamics control cell-cycle entry and progression. Jun 2024. URL: https://doi.org/10.1016/j.cub.2024.04.052, doi:10.1016/j.cub.2024.04.052. This article has 19 citations and is from a highest quality peer-reviewed journal.

10. (bhaduri2011cyclinspecificdockingmotifs pages 1-2): Samyabrata Bhaduri and Peter M. Pryciak. Cyclin-specific docking motifs promote phosphorylation of yeast signaling proteins by g1/s cdk complexes. Current Biology, 21:1615-1623, Oct 2011. URL: https://doi.org/10.1016/j.cub.2011.08.033, doi:10.1016/j.cub.2011.08.033. This article has 94 citations and is from a highest quality peer-reviewed journal.

11. (wang2024scdkregulatedbipartiteinteraction pages 2-3): Xueting Wang, Lu Liu, Mengke Chen, Yun Quan, Jiaxin Zhang, Huiqiang Lou, Yisui Xia, Hongxiang Chen, and Wenya Hou. S-cdk-regulated bipartite interaction of mcm10 with mcm is essential for dna replication. Frontiers in Cell and Developmental Biology, Sep 2024. URL: https://doi.org/10.3389/fcell.2024.1420033, doi:10.3389/fcell.2024.1420033. This article has 4 citations.

12. (wang2024scdkregulatedbipartiteinteraction pages 1-2): Xueting Wang, Lu Liu, Mengke Chen, Yun Quan, Jiaxin Zhang, Huiqiang Lou, Yisui Xia, Hongxiang Chen, and Wenya Hou. S-cdk-regulated bipartite interaction of mcm10 with mcm is essential for dna replication. Frontiers in Cell and Developmental Biology, Sep 2024. URL: https://doi.org/10.3389/fcell.2024.1420033, doi:10.3389/fcell.2024.1420033. This article has 4 citations.

13. (ubersax2004cellcycleregulationby pages 19-24): JA Ubersax. Cell-cycle regulation by cdk1 in saccharomyces cerevisiae. Unknown journal, 2004.

14. (sopko2007explorationofgene pages 35-36): R Sopko. Exploration of gene function and identification of kinase targets by systematic analysis of gene overexpression in saccharomyces cerevisiae. Unknown journal, 2007.

15. (ubersax2004cellcycleregulationby pages 60-65): JA Ubersax. Cell-cycle regulation by cdk1 in saccharomyces cerevisiae. Unknown journal, 2004.

16. (ubersax2004cellcycleregulationby pages 8-14): JA Ubersax. Cell-cycle regulation by cdk1 in saccharomyces cerevisiae. Unknown journal, 2004.

## Artifacts

- [Edison artifact artifact-00](CDC28-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. valk2023cdksignalingvia pages 1-2
2. sopko2007explorationofgene pages 35-36
3. ubersax2004cellcycleregulationby pages 19-24
4. faustova2021anewlinear pages 1-2
5. robertson2020theroleand pages 34-38
6. ubersax2004cellcycleregulationby pages 14-19
7. ubersax2004cellcycleregulationby pages 8-14
8. ord2019cyclinspecificdockingmechanisms pages 1-3
9. bandyopadhyay2020comprehensiveanalysisof pages 1-4
10. bhaduri2011cyclinspecificdockingmotifs pages 1-2
11. wang2024scdkregulatedbipartiteinteraction pages 2-3
12. wang2024scdkregulatedbipartiteinteraction pages 1-2
13. ubersax2004cellcycleregulationby pages 60-65
14. https://doi.org/10.1016/j.cub.2024.04.052.
15. https://doi.org/10.1016/j.cub.2011.08.033.
16. https://doi.org/10.3389/fcell.2024.1420033.
17. https://doi.org/10.15252/embj.2020105839.
18. https://doi.org/10.1002/wrna.1816.
19. https://doi.org/10.1091/mbc.e22-06-0196.
20. https://doi.org/10.1002/wrna.1816,
21. https://doi.org/10.1091/mbc.e22-06-0196,
22. https://doi.org/10.15252/embj.2020105839,
23. https://doi.org/10.1016/j.molcel.2019.04.026,
24. https://doi.org/10.1101/2020.03.02.973354,
25. https://doi.org/10.1016/j.cub.2024.04.052,
26. https://doi.org/10.1016/j.cub.2011.08.033,
27. https://doi.org/10.3389/fcell.2024.1420033,