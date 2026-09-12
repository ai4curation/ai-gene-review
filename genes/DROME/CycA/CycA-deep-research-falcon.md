---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-08T18:30:46.506904'
end_time: '2026-09-08T18:40:07.282163'
duration_seconds: 560.78
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: DROME
  gene_id: CycA
  gene_symbol: CycA
  uniprot_accession: M9NFR3
  protein_description: 'SubName: Full=Cyclin A, isoform C {ECO:0000313|EMBL:AFH04395.1};'
  gene_info: Name=CycA {ECO:0000313|EMBL:AFH04395.1, ECO:0000313|FlyBase:FBgn0000404};
    Synonyms=0033/02 {ECO:0000313|EMBL:AFH04395.1}, 0040/24 {ECO:0000313|EMBL:AFH04395.1},
    0046/23 {ECO:0000313|EMBL:AFH04395.1}, 0104/07 {ECO:0000313|EMBL:AFH04395.1},
    0245/34 {ECO:0000313|EMBL:AFH04395.1}, 0521/06 {ECO:0000313|EMBL:AFH04395.1},
    0545/13 {ECO:0000313|EMBL:AFH04395.1}, 1329/16 {ECO:0000313|EMBL:AFH04395.1},
    1449/05 {ECO:0000313|EMBL:AFH04395.1}, anon-WO0140519.128 {ECO:0000313|EMBL:AFH04395.1},
    CLD3 {ECO:0000313|EMBL:AFH04395.1}, Cyc A {ECO:0000313|EMBL:AFH04395.1}, CYCA
    {ECO:0000313|EMBL:AFH04395.1}, cycA {ECO:0000313|EMBL:AFH04395.1}, CYCLIN A {ECO:0000313|EMBL:AFH04395.1},
    cyclin A {ECO:0000313|EMBL:AFH04395.1}, CyclinA {ECO:0000313|EMBL:AFH04395.1},
    dCycA {ECO:0000313|EMBL:AFH04395.1}, DmcycA {ECO:0000313|EMBL:AFH04395.1}, Dmel\CG5940
    {ECO:0000313|EMBL:AFH04395.1}, hari {ECO:0000313|EMBL:AFH04395.1}, l(3)03946 {ECO:0000313|EMBL:AFH04395.1},
    l(3)183 {ECO:0000313|EMBL:AFH04395.1}, l(3)68Ea {ECO:0000313|EMBL:AFH04395.1},
    l(3)j3C8 {ECO:0000313|EMBL:AFH04395.1}, l(3)neo114 {ECO:0000313|EMBL:AFH04395.1},
    l(3)rsg11 {ECO:0000313|EMBL:AFH04395.1}, rsg11 {ECO:0000313|EMBL:AFH04395.1},
    S(rux)3B {ECO:0000313|EMBL:AFH04395.1}; ORFNames=CG5940 {ECO:0000313|EMBL:AFH04395.1,
    ECO:0000313|FlyBase:FBgn0000404}, Dmel_CG5940 {ECO:0000313|EMBL:AFH04395.1};
  organism_full: Drosophila melanogaster (Fruit fly).
  protein_family: Belongs to the cyclin family.
  protein_domains: Cyclin. (IPR039361); Cyclin-like_dom. (IPR013763); Cyclin-like_sf.
    (IPR036915); Cyclin_C-dom. (IPR004367); Cyclin_N. (IPR006671)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 46
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: CycA-deep-research-falcon_artifacts/artifact-00.md
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
- **UniProt Accession:** M9NFR3
- **Protein Description:** SubName: Full=Cyclin A, isoform C {ECO:0000313|EMBL:AFH04395.1};
- **Gene Information:** Name=CycA {ECO:0000313|EMBL:AFH04395.1, ECO:0000313|FlyBase:FBgn0000404}; Synonyms=0033/02 {ECO:0000313|EMBL:AFH04395.1}, 0040/24 {ECO:0000313|EMBL:AFH04395.1}, 0046/23 {ECO:0000313|EMBL:AFH04395.1}, 0104/07 {ECO:0000313|EMBL:AFH04395.1}, 0245/34 {ECO:0000313|EMBL:AFH04395.1}, 0521/06 {ECO:0000313|EMBL:AFH04395.1}, 0545/13 {ECO:0000313|EMBL:AFH04395.1}, 1329/16 {ECO:0000313|EMBL:AFH04395.1}, 1449/05 {ECO:0000313|EMBL:AFH04395.1}, anon-WO0140519.128 {ECO:0000313|EMBL:AFH04395.1}, CLD3 {ECO:0000313|EMBL:AFH04395.1}, Cyc A {ECO:0000313|EMBL:AFH04395.1}, CYCA {ECO:0000313|EMBL:AFH04395.1}, cycA {ECO:0000313|EMBL:AFH04395.1}, CYCLIN A {ECO:0000313|EMBL:AFH04395.1}, cyclin A {ECO:0000313|EMBL:AFH04395.1}, CyclinA {ECO:0000313|EMBL:AFH04395.1}, dCycA {ECO:0000313|EMBL:AFH04395.1}, DmcycA {ECO:0000313|EMBL:AFH04395.1}, Dmel\CG5940 {ECO:0000313|EMBL:AFH04395.1}, hari {ECO:0000313|EMBL:AFH04395.1}, l(3)03946 {ECO:0000313|EMBL:AFH04395.1}, l(3)183 {ECO:0000313|EMBL:AFH04395.1}, l(3)68Ea {ECO:0000313|EMBL:AFH04395.1}, l(3)j3C8 {ECO:0000313|EMBL:AFH04395.1}, l(3)neo114 {ECO:0000313|EMBL:AFH04395.1}, l(3)rsg11 {ECO:0000313|EMBL:AFH04395.1}, rsg11 {ECO:0000313|EMBL:AFH04395.1}, S(rux)3B {ECO:0000313|EMBL:AFH04395.1}; ORFNames=CG5940 {ECO:0000313|EMBL:AFH04395.1, ECO:0000313|FlyBase:FBgn0000404}, Dmel_CG5940 {ECO:0000313|EMBL:AFH04395.1};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Belongs to the cyclin family.
- **Key Domains:** Cyclin. (IPR039361); Cyclin-like_dom. (IPR013763); Cyclin-like_sf. (IPR036915); Cyclin_C-dom. (IPR004367); Cyclin_N. (IPR006671)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "CycA" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'CycA' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **CycA** (gene ID: CycA, UniProt: M9NFR3) in DROME.

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
- **UniProt Accession:** M9NFR3
- **Protein Description:** SubName: Full=Cyclin A, isoform C {ECO:0000313|EMBL:AFH04395.1};
- **Gene Information:** Name=CycA {ECO:0000313|EMBL:AFH04395.1, ECO:0000313|FlyBase:FBgn0000404}; Synonyms=0033/02 {ECO:0000313|EMBL:AFH04395.1}, 0040/24 {ECO:0000313|EMBL:AFH04395.1}, 0046/23 {ECO:0000313|EMBL:AFH04395.1}, 0104/07 {ECO:0000313|EMBL:AFH04395.1}, 0245/34 {ECO:0000313|EMBL:AFH04395.1}, 0521/06 {ECO:0000313|EMBL:AFH04395.1}, 0545/13 {ECO:0000313|EMBL:AFH04395.1}, 1329/16 {ECO:0000313|EMBL:AFH04395.1}, 1449/05 {ECO:0000313|EMBL:AFH04395.1}, anon-WO0140519.128 {ECO:0000313|EMBL:AFH04395.1}, CLD3 {ECO:0000313|EMBL:AFH04395.1}, Cyc A {ECO:0000313|EMBL:AFH04395.1}, CYCA {ECO:0000313|EMBL:AFH04395.1}, cycA {ECO:0000313|EMBL:AFH04395.1}, CYCLIN A {ECO:0000313|EMBL:AFH04395.1}, cyclin A {ECO:0000313|EMBL:AFH04395.1}, CyclinA {ECO:0000313|EMBL:AFH04395.1}, dCycA {ECO:0000313|EMBL:AFH04395.1}, DmcycA {ECO:0000313|EMBL:AFH04395.1}, Dmel\CG5940 {ECO:0000313|EMBL:AFH04395.1}, hari {ECO:0000313|EMBL:AFH04395.1}, l(3)03946 {ECO:0000313|EMBL:AFH04395.1}, l(3)183 {ECO:0000313|EMBL:AFH04395.1}, l(3)68Ea {ECO:0000313|EMBL:AFH04395.1}, l(3)j3C8 {ECO:0000313|EMBL:AFH04395.1}, l(3)neo114 {ECO:0000313|EMBL:AFH04395.1}, l(3)rsg11 {ECO:0000313|EMBL:AFH04395.1}, rsg11 {ECO:0000313|EMBL:AFH04395.1}, S(rux)3B {ECO:0000313|EMBL:AFH04395.1}; ORFNames=CG5940 {ECO:0000313|EMBL:AFH04395.1, ECO:0000313|FlyBase:FBgn0000404}, Dmel_CG5940 {ECO:0000313|EMBL:AFH04395.1};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Belongs to the cyclin family.
- **Key Domains:** Cyclin. (IPR039361); Cyclin-like_dom. (IPR013763); Cyclin-like_sf. (IPR036915); Cyclin_C-dom. (IPR004367); Cyclin_N. (IPR006671)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "CycA" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'CycA' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **CycA** (gene ID: CycA, UniProt: M9NFR3) in DROME.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Functional annotation report: *Drosophila melanogaster* **CycA**

## Executive conclusion

The target is correctly identified as *Drosophila melanogaster* Cyclin A: **CycA/CG5940**, FlyBase **FBgn0000404**, UniProt **M9NFR3**. The retrieved fly literature consistently uses CycA or CYCA for this mitotic cyclin and does not indicate that the supplied accession represents a different namesake. Literature on bacterial **cycA** transporters and Cyclin A proteins from other organisms was excluded.

CycA is best annotated as a **regulatory cyclin subunit of cyclin-dependent kinase 1 (Cdk1/Cdc2)**. It is not itself a catalytic enzyme, transporter, or structural protein. Its primary biochemical function is to bind and activate Cdk1 and to confer temporal and spatial control on Cdk1-dependent phosphorylation during G2 and early mitosis. The resulting CycA–Cdk1 activity promotes mitotic entry, preserves the ordering of S and M phases, and coordinates chromosome, centrosome/spindle, centromere, and cytoplasmic-organelle events. CycA also has spatially specialized functions at centromeres and at the polarized cell cortex. Regulated APC/C-dependent destruction of CycA in prometaphase/metaphase is integral to its function. Direct, comprehensive substrate specificity has not been defined for fly CycA–Cdk1; therefore, annotation should not claim a single established protein substrate.

## 1. Identity, family, and domain verification

The identifiers supplied by the user—M9NFR3, CycA, CG5940, and FBgn0000404—are mutually consistent with *D. melanogaster* Cyclin A. An independent Drosophila RNAi screen explicitly identified CYCA as the fly Cyclin A protein, while older genetic work describes an approximately 59-kDa protein essential for embryonic cell cycles. No evidence retrieved suggested an identity conflict. (dhaliwal2011rolesofcyclin pages 20-25, erhardt2008genomewideanalysisreveals pages 1-2)

The supplied InterPro annotations—Cyclin (IPR039361), cyclin-like domain/superfamily (IPR013763/IPR036915), Cyclin N (IPR006671), and Cyclin C-terminal domain (IPR004367)—are internally consistent with a canonical cyclin fold. Functionally, this architecture provides the interaction surface that activates a CDK catalytic subunit; CycA itself does not catalyze a reaction. The literature establishes cyclin behavior and Cdk1 partnership, but the retrieved experimental papers did not independently map each InterPro boundary. Thus, **protein-family membership is strongly supported**, whereas exact domain boundaries should remain attributed to UniProt/InterPro rather than to the cited functional studies.

## 2. Primary molecular function

### CycA is the activating and targeting subunit of Cdk1

The central complex is **CycA–Cdk1**, historically termed Cyclin A–Cdc2. In Drosophila, its activation precedes CycB–Cdk1 during G2/M, placing it early in the mitotic kinase sequence. CycA abundance and localization therefore determine when and where Cdk1 phosphorylates cellular targets. Loss of CycA prevents normal mitotic entry in many embryonic and somatic contexts, whereas stabilized CycA delays progression around metaphase. (dhaliwal2011rolesofcyclin pages 25-30, darnat2021corticalcyclina pages 1-5)

For enzyme-style annotation, the catalytic reaction belongs to **Cdk1**, not CycA: transfer of phosphate from ATP to serine/threonine residues in compatible protein substrates. CycA acts as the regulatory subunit that activates Cdk1 and influences substrate access. The retrieved studies do not define a complete fly CycA–Cdk1 phosphoproteome or a unique sequence specificity distinct from other Cdk1–cyclin complexes.

### Prevention of inappropriate S phase

CycA–Cdc2 also prevents DNA rereplication and helps ensure that mitosis follows S phase. Co-expression of Cdc2 and CycA inhibited S phase in salivary glands and diploid abdominal histoblasts. Notably, kinase-defective Cdc2 retained substantial S-phase inhibition, and Cdc2 plus CycA inhibited E2F-dependent transcriptional activation. This supports a partly **kinase-independent regulatory mechanism involving E2F**, alongside possible CDK phosphorylation of replication machinery. Direct action at replication origins was proposed but not established as the sole mechanism. (hayashi1999kinase‐independentactivityof pages 1-2)

This dual role explains why CycA loss or inhibition by Roughex can convert mitotically proliferating cells into repeated G/S endocycles and polyploid states. CycA is consequently both a mitotic-entry regulator and a barrier to unscheduled endoreplication. (herriage2024prematureendocyclingof pages 1-6, herriage2024prematureendocyclingof pages 6-8, hayashi1999kinase‐independentactivityof pages 1-2)

## 3. Principal pathways and regulatory logic

### G2/M and APC/C–Fzr/Cdh1 pathway

During G2, CycA accumulates and helps inhibit **APC/C–Fzr/Cdh1**, preventing premature degradation of CycB, CycB3, and Cdc25/String. This positive-feedback-like arrangement permits mitotic cyclins and Cdc25 activity to rise sufficiently for mitotic entry. In CycA mutants, inappropriate APC/C–Fzr activity causes premature loss of these regulators and blocks mitosis. (vasavan2015tumoursuppressorrole pages 119-123, dhaliwal2011rolesofcyclin pages 20-25)

CycA is itself later targeted for ubiquitin-dependent proteasomal degradation. It peaks around prophase and is destroyed in prometaphase/metaphase, before the later mitotic cyclins. Its N-terminal 53 residues contain a compound degradation region involving D-box and KEN-box signals; individual motifs are insufficient to explain all targeting, whereas deleting this region stabilizes CycA. Nondegradable CycA produces a dose-dependent metaphase delay and meiotic spindle/chromosome defects. (dhaliwal2011rolesofcyclin pages 25-30, dhaliwal2011rolesofcyclin pages 124-129, dhaliwal2011rolesofcyclin pages 20-25)

A proposed consequence of persistent CycA–Cdk1 is inhibitory phosphorylation of Separase, but the retrieved evidence does not establish Separase as a direct fly CycA-specific substrate. This should remain mechanistic inference, not definitive annotation. (dhaliwal2011rolesofcyclin pages 25-30)

### Centromere inheritance

A genome-wide Drosophila RNAi screen identified CycA and the APC/C inhibitor Rca1/Emi1 as regulators of CENP-A/CID propagation. CycA was observed at centromeres, and CycA/Rca1 control of APC/C–Fzr linked centromere assembly to cell-cycle position. This is good evidence for a **regulatory role in centromere propagation**, but not for CycA being a constitutive structural centromere component. No direct centromeric phosphosubstrate was established. (erhardt2008genomewideanalysisreveals pages 1-2)

## 4. Subcellular localization and site of action

CycA localization is dynamic and cell-type dependent:

* During interphase it is substantially cytoplasmic; it accumulates in the nucleus during prophase and is released into the cytoplasm following nuclear-envelope breakdown. APC/C-dependent destruction follows near metaphase entry. Nuclear accumulation correlates with chromosome condensation and nuclear-envelope events but is not absolutely required for all mitotic functions. (bergman2015spatialreorganizationof pages 15-17, darnat2021corticalcyclina pages 1-5)
* CycA localizes to centromeres in cultured Drosophila cells, where it contributes to cell-cycle coupling of CID/CENP-A assembly. (erhardt2008genomewideanalysisreveals pages 1-2)
* In dividing sensory-organ precursor cells, Frizzled/Dishevelled recruits CycA into an **apical-posterior cortical crescent** during G2/prophase. Cortical CycA promotes recruitment of Mud, the fly NuMA homologue, and correct orientation of the mitotic spindle. This establishes an unusually direct connection between planar-cell-polarity signaling and a core cell-cycle regulator. Direct physical binding between CycA and Mud was not established in the gathered evidence. (darnat2021corticalcyclina pages 1-5)
* After nuclear-envelope breakdown in early embryos, cytoplasmic CycA contributes to ER redistribution toward spindle poles. Injection of CycA, but not CycB, restored mitotic ER clustering after cell-cycle blockade; combined depletion of CycA, CycB, and CycB3 blocked remodeling. CycA depletion alone had a weaker effect, indicating redundancy among mitotic cyclins. Relevant ER phosphosubstrates remain unknown. (bergman2015spatialreorganizationof pages 15-17, bergman2015spatialreorganizationof pages 1-2)

Thus, the most defensible localization annotation is **nucleus, cytoplasm, centromere, and—in polarized precursor cells—apical-posterior cell cortex**, with strong cell-cycle dependence.

## 5. Biological processes and phenotypic evidence

Maternal CycA supports rapid syncytial embryonic divisions, cellularization-associated cycles, and subsequent embryonic mitoses. CycA loss is embryonic lethal. Residual maternal protein allows some epidermal cells to reach mitosis 15, but CycA-deficient epidermal cells fail to enter mitosis 16; nervous-system divisions can be less dependent, demonstrating tissue-specific redundancy or regulation. (dhaliwal2011rolesofcyclin pages 20-25)

In sensory-organ lineages, CycA mutant progenitors divide incorrectly, causing cell loss and malformed terminal mechanosensory organs. This phenotype reflects both its canonical mitotic-entry role and its cortical spindle-orientation function. (darnat2021corticalcyclina pages 1-5)

In the female germline, CycA participates in germline-stem-cell and cyst divisions, meiosis, and subsequent embryogenesis. Its protein must be suppressed when nurse cells leave mitotic cycles and enter endoreplication. Stabilized or excessive CycA disrupts germline-stem-cell maintenance, can add a cystocyte division, drives inappropriate mitotic entry in nurse cells, and causes abnormal meiotic spindles and chromosome segregation. (dhaliwal2011rolesofcyclin pages 34-39, dhaliwal2011rolesofcyclin pages 124-129)

## 6. Recent developments, 2023–2024

The recent literature largely extends CycA into models of post-transcriptional control and experimentally induced polyploid cycles rather than revising its primary molecular function.

### Post-transcriptional control during oogenesis

An October 17, 2024 bioRxiv preprint used smFISH, immunofluorescence, STED microscopy, RNAi, and mRNP-overlap analyses to examine cycA mRNA. cycA transcript is continuously present and broadly distributed through egg chambers, although CycA protein is expressed during the four germline cyst mitoses and again from approximately stage 12. Bruno 1 binds the cycA 3′ UTR and recruits the eIF4E-binding translational repressor Cup. Depletion of Bru1 or Cup reduces cycA mRNA abundance, causes abnormal CycA protein expression from about stage 4, and permits inappropriate nurse-cell mitotic re-entry. Me31B-marked P bodies contain cycA mRNA, but Me31B depletion did not measurably derepress CycA, arguing that visible P-body localization is not itself required for the core repression mechanism. Because this is a preprint, these conclusions should be treated as provisional. [Bayer et al., posted October 17, 2024; DOI URL](https://doi.org/10.1101/2024.10.17.618951). (bayer2024posttranscriptionalregulationof pages 1-6, bayer2024posttranscriptionalregulationof pages 6-10, bayer2024posttranscriptionalregulationof pages 32-36)

### CycA depletion as a model of induced endocycles

A peer-reviewed PLOS Genetics study published September 3, 2024 used CycA RNAi-derived induced-endocycling cells in Drosophila wing discs to investigate the consequences of unscheduled polyploid cycles. Induced endocycling cells enlarged, accumulated DNA damage, activated JNK signaling, resisted apoptosis, and entered a reversible senescent-like arrest. They stimulated compensatory division of neighboring diploid cells, but this did not restore tissue growth. The work positions CycA perturbation as a model for wound-associated polyploidy and therapy-resistant polyploid cancer-cell states, not as evidence that fly CycA is itself a clinically validated drug target. [Huang et al., published September 3, 2024; DOI URL](https://doi.org/10.1371/journal.pgen.1011387). (huang2024anunscheduledswitch pages 1-2)

A separate 2024 preprint directly depleted CycA in ovarian follicle cells, inducing premature endocycles and producing enlarged, irregular cells, abnormal E-cadherin patterns, distorted epithelial interfaces, and defective oogenesis. Normally, follicle cells switch at stages 6/7 and complete three genome duplications over about 24 hours to reach approximately 16C DNA content. In a parallel Roughex-induced condition—not CycA RNAi alone—stage-10B egg chambers contained approximately 179 rather than 641 follicle cells and reached about 56C rather than 16C. Those numerical values must not be attributed uniquely to CycA depletion. [Herriage and Calvi, 2024 preprint; DOI URL](https://doi.org/10.1101/2023.10.10.561736). (herriage2024prematureendocyclingof pages 1-6, herriage2024prematureendocyclingof pages 6-8)

No retrieved 2023 paper supplied a comparably direct new molecular mechanism for the exact M9NFR3/CG5940 protein. Foundational studies therefore remain the strongest sources for primary function, while 2024 work provides current applications.

## 7. Current applications and translational relevance

CycA is widely useful as an **experimental switch between mitotic proliferation and endoreplication**. RNAi, Roughex-mediated inhibition, stabilized CycA, and tissue-specific expression permit investigators to model polyploidization, senescence, genome instability, epithelial architecture, organ growth, and reproductive defects. These models have relevance to wound healing and cancer biology because mammalian tissues and tumors can also undergo polyploid cycles. The current implementation is principally basic and preclinical model-organism research; there is no evidence in the retrieved literature for a CycA-directed clinical intervention. (herriage2024prematureendocyclingof pages 1-6, herriage2024prematureendocyclingof pages 6-8, huang2024anunscheduledswitch pages 1-2)

The cortical-CycA system is also an implementation of Drosophila sensory-organ precursors as a model for how planar polarity is coupled to spindle orientation. The ER-remodeling and centromere studies similarly use CycA perturbation to dissect how mitotic kinase timing is translated into spatially distinct cellular events. (darnat2021corticalcyclina pages 1-5, bergman2015spatialreorganizationof pages 1-2, erhardt2008genomewideanalysisreveals pages 1-2)

## 8. Expert interpretation and recommended annotation

The evidence supports the following concise functional annotation:

> **Cyclin A is a cell-cycle-regulated activating and targeting subunit of Cdk1 that promotes G2/M transition and early mitotic events, suppresses inappropriate S-phase re-entry, and coordinates APC/C-regulated cyclin stability, centromere inheritance, spindle orientation, and cytoplasmic remodeling. Its localization shifts among cytoplasm, nucleus, centromeres, and specialized cortical domains, and it is degraded by APC/C around prometaphase/metaphase.**

Recommended high-confidence biological-process terms include mitotic G2/M transition, positive regulation of Cdk1 activity, mitotic cell-cycle progression, negative regulation of DNA rereplication/endocycle entry, APC/C-regulated proteolysis, chromosome segregation, centromere propagation, spindle orientation, and female germline/meiotic cell-cycle control. “Protein serine/threonine kinase activity” should **not** be assigned to CycA itself; it belongs to the CycA–Cdk1 complex’s catalytic subunit.

The largest unresolved mechanistic issue is substrate identity. Phenotypes implicate nuclear-envelope, chromatin, centrosome/spindle, replication, and ER targets, but few have been demonstrated as direct, CycA-selective Cdk1 substrates in Drosophila. E2F inhibition includes a kinase-independent component, Mud recruitment is not proven to involve direct binding, and proposed Separase or ER-protein phosphorylation remains incomplete. These distinctions are important for avoiding overannotation. (dhaliwal2011rolesofcyclin pages 25-30, bergman2015spatialreorganizationof pages 15-17, darnat2021corticalcyclina pages 1-5, hayashi1999kinase‐independentactivityof pages 1-2)

The evidence and confidence assignments are summarized below.

| Functional aspect | Precise conclusion | Experimental evidence/model | Evidence strength and limitations | Key source and date/DOI |
|---|---|---|---|---|
| Identity and domains | The research target is *Drosophila melanogaster* CycA/CG5940 (UniProt M9NFR3; FlyBase FBgn0000404), the approximately 59-kDa Cyclin A—not a similarly named protein from another organism. The supplied UniProt/InterPro annotations identify N- and C-terminal cyclin-fold domains. | Identifier cross-references supplied for M9NFR3; fly studies consistently identify CYCA as *Drosophila* Cyclin A and as a mitotic cyclin. | **High identity confidence.** The retrieved papers did not independently map the InterPro domains, so detailed domain architecture is database-supported rather than directly demonstrated in these experiments. (dhaliwal2011rolesofcyclin pages 20-25, erhardt2008genomewideanalysisreveals pages 1-2) | UniProt M9NFR3; Erhardt et al., December 2008, [10.1083/jcb.200806038](https://doi.org/10.1083/jcb.200806038) |
| CDK1 activation and G2/M entry | CycA binds Cdk1/Cdc2 and activates it before CycB–Cdk1, making CycA–Cdk1 a principal trigger of the G2-to-M transition. CycA is a regulatory kinase subunit, not an enzyme with an independently catalyzed reaction. | Timing and genetic analyses in embryos; CycA/Cdc2 co-expression studies; synthesis in later cell-biological work. | **Strong, direct fly evidence** for the functional complex and mitotic-entry role. Individual downstream phosphoprotein substrates remain incompletely defined. (darnat2021corticalcyclina pages 1-5, hayashi1999kinase‐independentactivityof pages 1-2) | Hayashi & Yamaguchi, February 1999, [10.1046/j.1365-2443.1999.00243.x](https://doi.org/10.1046/j.1365-2443.1999.00243.x); Darnat et al., version of record May 17, 2022, [10.1038/s41467-022-30182-1](https://doi.org/10.1038/s41467-022-30182-1) |
| APC/C–Fzr feedback and CycA degradation | Accumulated CycA inhibits APC/C–Fzr/Cdh1 during G2, protecting CycB, CycB3, and Cdc25/String and enabling mitotic entry. APC/C later targets CycA for proteasomal destruction in prometaphase/metaphase. | CycA loss causes premature destruction of other mitotic regulators; stabilized CycA and N-terminal deletions test degradation; genetic interaction with Fzr/Rca1. | **Strong genetic and protein-stability evidence.** The first 53 residues contain D-box/KEN-box-associated degradation information, but no single motif fully accounts for targeting. (dhaliwal2011rolesofcyclin pages 25-30, vasavan2015tumoursuppressorrole pages 119-123, dhaliwal2011rolesofcyclin pages 20-25) | Foundational fly studies summarized in Dhaliwal, 2011; Erhardt et al., December 2008, [10.1083/jcb.200806038](https://doi.org/10.1083/jcb.200806038) |
| Suppression of S phase and rereplication | In G2, CycA–Cdc2 prevents inappropriate S-phase entry and helps maintain mitosis-before-replication ordering. It can repress E2F-dependent activation partly through a kinase-independent mechanism. | Co-expression in larval salivary glands and diploid abdominal histoblasts; kinase-defective Cdc2 retained S-phase inhibition; E2F interaction and epistasis assays. | **Direct experimental evidence.** The E2F mechanism explains part, not necessarily all, of rereplication control; direct replication-origin action remained a model. (hayashi1999kinase‐independentactivityof pages 1-2) | Hayashi & Yamaguchi, February 1999, [10.1046/j.1365-2443.1999.00243.x](https://doi.org/10.1046/j.1365-2443.1999.00243.x) |
| Cell-cycle localization | CycA is cytoplasmic during interphase, accumulates in nuclei during prophase, and is released into the cytoplasm after nuclear-envelope breakdown before APC/C-dependent destruction. | Live/fixed imaging in sensory-organ precursors and early embryos; temporal comparison with nuclear-envelope breakdown and ER remodeling. | **Strong imaging evidence**, although localization varies by cell type and stage and nuclear accumulation is not absolutely required for mitotic function. (bergman2015spatialreorganizationof pages 15-17, darnat2021corticalcyclina pages 1-5) | Bergman et al., February 17, 2015, [10.1371/journal.pone.0117859](https://doi.org/10.1371/journal.pone.0117859); Darnat et al., May 17, 2022, [10.1038/s41467-022-30182-1](https://doi.org/10.1038/s41467-022-30182-1) |
| Centromere localization and propagation | CycA localizes to centromeres and, with Rca1/Emi1, couples CENP-A/CID centromere assembly to the cell cycle through regulation of APC/C–Fzr. | Genome-wide RNAi screen for loss of centromeric CID followed by localization and pathway analyses in *Drosophila* cultured cells. | **Direct screening, imaging, and perturbation evidence.** The result supports a regulatory role; it does not establish CycA as a structural centromere component or identify a directly phosphorylated centromeric substrate. (erhardt2008genomewideanalysisreveals pages 1-2) | Erhardt et al., December 1, 2008, [10.1083/jcb.200806038](https://doi.org/10.1083/jcb.200806038) |
| Polarized cortex, Mud, and spindle orientation | During sensory-organ precursor prophase, Frizzled/Dishevelled recruits CycA to an apical-posterior cortical crescent; cortical CycA promotes Mud/NuMA recruitment and correct spindle orientation. | In-vivo CycA dynamics, loss-of-function, ectopic-localization, cortical-recruitment, and spindle-orientation assays in pI/SOP cells. | **Strong, direct cell-biological evidence** for a noncanonical spatial/adaptor-like role. “Recruitment” is functional and localization-based; direct CycA–Mud binding was not established in the gathered evidence. (darnat2021corticalcyclina pages 1-5) | Darnat et al., May 17, 2022, [10.1038/s41467-022-30182-1](https://doi.org/10.1038/s41467-022-30182-1) |
| Mitotic ER remodeling | Cytoplasmic CycA can initiate mitotic reorganization of the ER toward spindle poles in early embryos, linking nuclear-envelope breakdown to cytoplasmic mitotic remodeling. | CycA microinjection restored ER clustering after cell-cycle blockade; CycB injection did not; combined RNAi against CycA, CycB, and CycB3 blocked remodeling. | **Direct sufficiency evidence with redundancy.** CycA knockdown alone had a minor phenotype, and the relevant phosphorylated ER substrate remains unidentified. (bergman2015spatialreorganizationof pages 15-17, bergman2015spatialreorganizationof pages 1-2) | Bergman et al., February 17, 2015, [10.1371/journal.pone.0117859](https://doi.org/10.1371/journal.pone.0117859) |
| Germline and oogenesis regulation | CycA drives germline mitoses but must be suppressed as nurse cells leave mitotic cycles. cycA mRNA persists when protein is absent; Bru1 binds its 3′ UTR and recruits Cup to repress translation. CycA is re-expressed late in oogenesis. | Expression imaging, RNA perturbation, super-resolution microscopy, mRNA–protein association assays, and bru1/cup depletion in egg chambers. | **Mechanistically informative but the newest evidence is a 2024 preprint.** Bru1/Cup depletion reduces cycA mRNA and causes abnormal CycA expression and mitotic re-entry; Me31B depletion did not measurably derepress CycA. (bayer2024posttranscriptionalregulationof pages 1-6, bayer2024posttranscriptionalregulationof pages 6-10, bayer2024posttranscriptionalregulationof pages 32-36) | Bayer et al., bioRxiv, October 17, 2024, [10.1101/2024.10.17.618951](https://doi.org/10.1101/2024.10.17.618951) |
| 2024 induced-endocycle applications | CycA depletion is used experimentally to switch proliferating cells into G/S endocycles, enabling study of polyploidy, senescence, tissue growth, oogenesis, wound responses, and cancer-relevant genome instability. | CycA RNAi in wing discs and ovarian follicle cells; EdU, phospho-H3, ploidy, epithelial morphology, stress-pathway, and growth analyses. Follicle cells normally complete three endocycles in about 24 h to reach 16C; an induced-endocycle condition yielded about 179 versus 641 cells and about 56C versus 16C, although those numerical values were reported for Rux induction rather than CycA RNAi alone. | **Peer-reviewed contextual application in wing discs plus direct 2024 preprint evidence in follicle cells.** CycA is a genetic perturbation/modeling tool, not a validated therapeutic target; cross-species clinical extrapolation is premature. (herriage2024prematureendocyclingof pages 1-6, herriage2024prematureendocyclingof pages 6-8, huang2024anunscheduledswitch pages 1-2) | Huang et al., September 3, 2024, [10.1371/journal.pgen.1011387](https://doi.org/10.1371/journal.pgen.1011387); Herriage & Calvi, 2024 preprint, [10.1101/2023.10.10.561736](https://doi.org/10.1101/2023.10.10.561736) |


*Table: Evidence matrix separating firmly established functions of the exact Drosophila CycA protein from mechanistic inferences and recent preprint findings. It also identifies where quantitative results apply to induced-endocycle models rather than uniquely to CycA.*

## Key source list

1. Hayashi S, Yamaguchi M. “Kinase-independent activity of Cdc2/Cyclin A prevents the S phase in the Drosophila cell cycle.” *Genes to Cells* 4:111–122. Published February 1999. [https://doi.org/10.1046/j.1365-2443.1999.00243.x](https://doi.org/10.1046/j.1365-2443.1999.00243.x). (hayashi1999kinase‐independentactivityof pages 1-2)
2. Erhardt S et al. “Genome-wide analysis reveals a cell cycle-dependent mechanism controlling centromere propagation.” *Journal of Cell Biology* 183:805–818. Published December 2008. [https://doi.org/10.1083/jcb.200806038](https://doi.org/10.1083/jcb.200806038). (erhardt2008genomewideanalysisreveals pages 1-2)
3. Bergman ZJ et al. “Spatial Reorganization of the Endoplasmic Reticulum during Mitosis Relies on Mitotic Kinase Cyclin A in the Early Drosophila Embryo.” *PLOS ONE* 10:e0117859. Published February 17, 2015. [https://doi.org/10.1371/journal.pone.0117859](https://doi.org/10.1371/journal.pone.0117859). (bergman2015spatialreorganizationof pages 1-2)
4. Darnat P et al. “Cortical Cyclin A controls spindle orientation during asymmetric cell division.” *Nature Communications*. Version of record published May 17, 2022. [https://doi.org/10.1038/s41467-022-30182-1](https://doi.org/10.1038/s41467-022-30182-1). (darnat2021corticalcyclina pages 1-5)
5. Huang Y-T, Hesting LL, Calvi BR. “An unscheduled switch to endocycles induces a reversible senescent arrest that impairs growth of the Drosophila wing disc.” *PLOS Genetics* 20:e1011387. Published September 3, 2024. [https://doi.org/10.1371/journal.pgen.1011387](https://doi.org/10.1371/journal.pgen.1011387). (huang2024anunscheduledswitch pages 1-2)
6. Bayer LV et al. “Post-transcriptional regulation of cyclin A and cyclin B mRNAs is mediated by Bruno 1 and Cup, and further fine-tuned within P-bodies.” bioRxiv preprint, posted October 17, 2024. [https://doi.org/10.1101/2024.10.17.618951](https://doi.org/10.1101/2024.10.17.618951). (bayer2024posttranscriptionalregulationof pages 1-6)
7. Herriage HC, Calvi BR. “Premature endocycling of Drosophila follicle cells causes pleiotropic defects in oogenesis.” 2024 bioRxiv version. [https://doi.org/10.1101/2023.10.10.561736](https://doi.org/10.1101/2023.10.10.561736). (herriage2024prematureendocyclingof pages 1-6, herriage2024prematureendocyclingof pages 6-8)

References

1. (dhaliwal2011rolesofcyclin pages 20-25): R Dhaliwal. Roles of cyclin a and cyclin b in drosophila female meiosis. Unknown journal, 2011.

2. (erhardt2008genomewideanalysisreveals pages 1-2): Sylvia Erhardt, Barbara G. Mellone, Craig M. Betts, Weiguo Zhang, Gary H. Karpen, and Aaron F. Straight. Genome-wide analysis reveals a cell cycle–dependent mechanism controlling centromere propagation. The Journal of Cell Biology, 183:805-818, Dec 2008. URL: https://doi.org/10.1083/jcb.200806038, doi:10.1083/jcb.200806038. This article has 228 citations.

3. (dhaliwal2011rolesofcyclin pages 25-30): R Dhaliwal. Roles of cyclin a and cyclin b in drosophila female meiosis. Unknown journal, 2011.

4. (darnat2021corticalcyclina pages 1-5): Pénélope Darnat, Angelique Burg, Jérémy Sallé, Jérôme Lacoste, Sophie Louvet-Vallée, Michel Gho, and Agnes Audibert. Cortical cyclin a controls spindle orientation during asymmetric cell division. Apr 2021. URL: https://doi.org/10.21203/rs.3.rs-343397/v1, doi:10.21203/rs.3.rs-343397/v1.

5. (hayashi1999kinase‐independentactivityof pages 1-2): Shigeo Hayashi and Masamitsu Yamaguchi. Kinase‐independent activity of cdc2/cyclin a prevents the s phase in the drosophila cell cycle. Genes to Cells, 4:111-122, Feb 1999. URL: https://doi.org/10.1046/j.1365-2443.1999.00243.x, doi:10.1046/j.1365-2443.1999.00243.x. This article has 35 citations and is from a peer-reviewed journal.

6. (herriage2024prematureendocyclingof pages 1-6): Hunter C. Herriage and Brian R. Calvi. Premature endocycling of drosophila follicle cells causes pleiotropic defects in oogenesis. bioRxiv, Oct 2024. URL: https://doi.org/10.1101/2023.10.10.561736, doi:10.1101/2023.10.10.561736. This article has 10 citations.

7. (herriage2024prematureendocyclingof pages 6-8): Hunter C. Herriage and Brian R. Calvi. Premature endocycling of drosophila follicle cells causes pleiotropic defects in oogenesis. bioRxiv, Oct 2024. URL: https://doi.org/10.1101/2023.10.10.561736, doi:10.1101/2023.10.10.561736. This article has 10 citations.

8. (vasavan2015tumoursuppressorrole pages 119-123): B Vasavan. Tumour suppressor role of s-phase kinase associated protein 1-cullin-f box-s-phase kinase associated protein 2 (scfskp2). Unknown journal, 2015.

9. (dhaliwal2011rolesofcyclin pages 124-129): R Dhaliwal. Roles of cyclin a and cyclin b in drosophila female meiosis. Unknown journal, 2011.

10. (bergman2015spatialreorganizationof pages 15-17): Zane J. Bergman, Justin D. Mclaurin, Anthony S. Eritano, Brittany M. Johnson, Amanda Q. Sims, and Blake Riggs. Spatial reorganization of the endoplasmic reticulum during mitosis relies on mitotic kinase cyclin a in the early drosophila embryo. PLoS ONE, 10:e0117859, Feb 2015. URL: https://doi.org/10.1371/journal.pone.0117859, doi:10.1371/journal.pone.0117859. This article has 37 citations and is from a peer-reviewed journal.

11. (bergman2015spatialreorganizationof pages 1-2): Zane J. Bergman, Justin D. Mclaurin, Anthony S. Eritano, Brittany M. Johnson, Amanda Q. Sims, and Blake Riggs. Spatial reorganization of the endoplasmic reticulum during mitosis relies on mitotic kinase cyclin a in the early drosophila embryo. PLoS ONE, 10:e0117859, Feb 2015. URL: https://doi.org/10.1371/journal.pone.0117859, doi:10.1371/journal.pone.0117859. This article has 37 citations and is from a peer-reviewed journal.

12. (dhaliwal2011rolesofcyclin pages 34-39): R Dhaliwal. Roles of cyclin a and cyclin b in drosophila female meiosis. Unknown journal, 2011.

13. (bayer2024posttranscriptionalregulationof pages 1-6): Livia V. Bayer, Samantha N. Milano, Harpreet Kaur, and Diana P. Bratu. Post-transcriptional regulation of cyclin a and cyclin b mrnas is mediated by bruno 1 and cup, and further fine-tuned within p-bodies. bioRxiv, Oct 2024. URL: https://doi.org/10.1101/2024.10.17.618951, doi:10.1101/2024.10.17.618951. This article has 0 citations.

14. (bayer2024posttranscriptionalregulationof pages 6-10): Livia V. Bayer, Samantha N. Milano, Harpreet Kaur, and Diana P. Bratu. Post-transcriptional regulation of cyclin a and cyclin b mrnas is mediated by bruno 1 and cup, and further fine-tuned within p-bodies. bioRxiv, Oct 2024. URL: https://doi.org/10.1101/2024.10.17.618951, doi:10.1101/2024.10.17.618951. This article has 0 citations.

15. (bayer2024posttranscriptionalregulationof pages 32-36): Livia V. Bayer, Samantha N. Milano, Harpreet Kaur, and Diana P. Bratu. Post-transcriptional regulation of cyclin a and cyclin b mrnas is mediated by bruno 1 and cup, and further fine-tuned within p-bodies. bioRxiv, Oct 2024. URL: https://doi.org/10.1101/2024.10.17.618951, doi:10.1101/2024.10.17.618951. This article has 0 citations.

16. (huang2024anunscheduledswitch pages 1-2): Yi-Ting Huang, Lauren L. Hesting, and Brian R. Calvi. An unscheduled switch to endocycles induces a reversible senescent arrest that impairs growth of the drosophila wing disc. Sep 2024. URL: https://doi.org/10.1371/journal.pgen.1011387, doi:10.1371/journal.pgen.1011387. This article has 12 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](CycA-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. dhaliwal2011rolesofcyclin pages 25-30
2. erhardt2008genomewideanalysisreveals pages 1-2
3. darnat2021corticalcyclina pages 1-5
4. dhaliwal2011rolesofcyclin pages 20-25
5. huang2024anunscheduledswitch pages 1-2
6. bergman2015spatialreorganizationof pages 1-2
7. bayer2024posttranscriptionalregulationof pages 1-6
8. herriage2024prematureendocyclingof pages 1-6
9. herriage2024prematureendocyclingof pages 6-8
10. vasavan2015tumoursuppressorrole pages 119-123
11. dhaliwal2011rolesofcyclin pages 124-129
12. bergman2015spatialreorganizationof pages 15-17
13. dhaliwal2011rolesofcyclin pages 34-39
14. bayer2024posttranscriptionalregulationof pages 6-10
15. bayer2024posttranscriptionalregulationof pages 32-36
16. Bayer et al., posted October 17, 2024; DOI URL
17. Huang et al., published September 3, 2024; DOI URL
18. Herriage and Calvi, 2024 preprint; DOI URL
19. 10.1083/jcb.200806038
20. 10.1046/j.1365-2443.1999.00243.x
21. 10.1038/s41467-022-30182-1
22. 10.1371/journal.pone.0117859
23. 10.1101/2024.10.17.618951
24. 10.1371/journal.pgen.1011387
25. 10.1101/2023.10.10.561736
26. https://doi.org/10.1046/j.1365-2443.1999.00243.x
27. https://doi.org/10.1083/jcb.200806038
28. https://doi.org/10.1371/journal.pone.0117859
29. https://doi.org/10.1038/s41467-022-30182-1
30. https://doi.org/10.1371/journal.pgen.1011387
31. https://doi.org/10.1101/2024.10.17.618951
32. https://doi.org/10.1101/2023.10.10.561736
33. https://doi.org/10.1046/j.1365-2443.1999.00243.x](https://doi.org/10.1046/j.1365-2443.1999.00243.x
34. https://doi.org/10.1083/jcb.200806038](https://doi.org/10.1083/jcb.200806038
35. https://doi.org/10.1371/journal.pone.0117859](https://doi.org/10.1371/journal.pone.0117859
36. https://doi.org/10.1038/s41467-022-30182-1](https://doi.org/10.1038/s41467-022-30182-1
37. https://doi.org/10.1371/journal.pgen.1011387](https://doi.org/10.1371/journal.pgen.1011387
38. https://doi.org/10.1101/2024.10.17.618951](https://doi.org/10.1101/2024.10.17.618951
39. https://doi.org/10.1101/2023.10.10.561736](https://doi.org/10.1101/2023.10.10.561736
40. https://doi.org/10.1083/jcb.200806038,
41. https://doi.org/10.21203/rs.3.rs-343397/v1,
42. https://doi.org/10.1046/j.1365-2443.1999.00243.x,
43. https://doi.org/10.1101/2023.10.10.561736,
44. https://doi.org/10.1371/journal.pone.0117859,
45. https://doi.org/10.1101/2024.10.17.618951,
46. https://doi.org/10.1371/journal.pgen.1011387,