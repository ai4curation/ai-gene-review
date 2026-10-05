---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-08T18:24:23.046191'
end_time: '2026-09-08T18:29:59.666341'
duration_seconds: 336.62
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: DROME
  gene_id: jumu
  gene_symbol: jumu
  uniprot_accession: Q9XTP7
  protein_description: 'SubName: Full=Jumeau {ECO:0000313|EMBL:AAF54525.1};'
  gene_info: Name=jumu {ECO:0000313|EMBL:AAF54525.1, ECO:0000313|FlyBase:FBgn0015396};
    Synonyms=5295 {ECO:0000313|EMBL:AAF54525.1}, Dmel\CG4029 {ECO:0000313|EMBL:AAF54525.1},
    Dmjumu {ECO:0000313|EMBL:AAF54525.1}, Dom {ECO:0000313|EMBL:AAF54525.1}, Dwhn
    {ECO:0000313|EMBL:AAF54525.1}, E(var)631 {ECO:0000313|EMBL:AAF54525.1}, FoxN14
    {ECO:0000313|EMBL:AAF54525.1}, Jumeau {ECO:0000313|EMBL:AAF54525.1}, jumeaux {ECO:0000313|EMBL:AAF54525.1},
    Jumu {ECO:0000313|EMBL:AAF54525.1}, jumu/Dom {ECO:0000313|EMBL:AAF54525.1}, l(3)06142
    {ECO:0000313|EMBL:AAF54525.1}, l(3)06439 {ECO:0000313|EMBL:AAF54525.1}, Scim31
    {ECO:0000313|EMBL:AAF54525.1}, Whn {ECO:0000313|EMBL:AAF54525.1}; ORFNames=CG4029
    {ECO:0000313|EMBL:AAF54525.1, ECO:0000313|FlyBase:FBgn0015396}, Dmel_CG4029 {ECO:0000313|EMBL:AAF54525.1};
  organism_full: Drosophila melanogaster (Fruit fly).
  protein_family: Not specified in UniProt
  protein_domains: Fork_head_dom. (IPR001766); FOXN1_4. (IPR049624); TF_fork_head_CS_2.
    (IPR030456); WH-like_DNA-bd_sf. (IPR036388); WH_DNA-bd_sf. (IPR036390)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 31
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: jumu-deep-research-falcon_artifacts/artifact-00.md
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
- **UniProt Accession:** Q9XTP7
- **Protein Description:** SubName: Full=Jumeau {ECO:0000313|EMBL:AAF54525.1};
- **Gene Information:** Name=jumu {ECO:0000313|EMBL:AAF54525.1, ECO:0000313|FlyBase:FBgn0015396}; Synonyms=5295 {ECO:0000313|EMBL:AAF54525.1}, Dmel\CG4029 {ECO:0000313|EMBL:AAF54525.1}, Dmjumu {ECO:0000313|EMBL:AAF54525.1}, Dom {ECO:0000313|EMBL:AAF54525.1}, Dwhn {ECO:0000313|EMBL:AAF54525.1}, E(var)631 {ECO:0000313|EMBL:AAF54525.1}, FoxN14 {ECO:0000313|EMBL:AAF54525.1}, Jumeau {ECO:0000313|EMBL:AAF54525.1}, jumeaux {ECO:0000313|EMBL:AAF54525.1}, Jumu {ECO:0000313|EMBL:AAF54525.1}, jumu/Dom {ECO:0000313|EMBL:AAF54525.1}, l(3)06142 {ECO:0000313|EMBL:AAF54525.1}, l(3)06439 {ECO:0000313|EMBL:AAF54525.1}, Scim31 {ECO:0000313|EMBL:AAF54525.1}, Whn {ECO:0000313|EMBL:AAF54525.1}; ORFNames=CG4029 {ECO:0000313|EMBL:AAF54525.1, ECO:0000313|FlyBase:FBgn0015396}, Dmel_CG4029 {ECO:0000313|EMBL:AAF54525.1};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** Fork_head_dom. (IPR001766); FOXN1_4. (IPR049624); TF_fork_head_CS_2. (IPR030456); WH-like_DNA-bd_sf. (IPR036388); WH_DNA-bd_sf. (IPR036390)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "jumu" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'jumu' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **jumu** (gene ID: jumu, UniProt: Q9XTP7) in DROME.

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
- **UniProt Accession:** Q9XTP7
- **Protein Description:** SubName: Full=Jumeau {ECO:0000313|EMBL:AAF54525.1};
- **Gene Information:** Name=jumu {ECO:0000313|EMBL:AAF54525.1, ECO:0000313|FlyBase:FBgn0015396}; Synonyms=5295 {ECO:0000313|EMBL:AAF54525.1}, Dmel\CG4029 {ECO:0000313|EMBL:AAF54525.1}, Dmjumu {ECO:0000313|EMBL:AAF54525.1}, Dom {ECO:0000313|EMBL:AAF54525.1}, Dwhn {ECO:0000313|EMBL:AAF54525.1}, E(var)631 {ECO:0000313|EMBL:AAF54525.1}, FoxN14 {ECO:0000313|EMBL:AAF54525.1}, Jumeau {ECO:0000313|EMBL:AAF54525.1}, jumeaux {ECO:0000313|EMBL:AAF54525.1}, Jumu {ECO:0000313|EMBL:AAF54525.1}, jumu/Dom {ECO:0000313|EMBL:AAF54525.1}, l(3)06142 {ECO:0000313|EMBL:AAF54525.1}, l(3)06439 {ECO:0000313|EMBL:AAF54525.1}, Scim31 {ECO:0000313|EMBL:AAF54525.1}, Whn {ECO:0000313|EMBL:AAF54525.1}; ORFNames=CG4029 {ECO:0000313|EMBL:AAF54525.1, ECO:0000313|FlyBase:FBgn0015396}, Dmel_CG4029 {ECO:0000313|EMBL:AAF54525.1};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** Fork_head_dom. (IPR001766); FOXN1_4. (IPR049624); TF_fork_head_CS_2. (IPR030456); WH-like_DNA-bd_sf. (IPR036388); WH_DNA-bd_sf. (IPR036390)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "jumu" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'jumu' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **jumu** (gene ID: jumu, UniProt: Q9XTP7) in DROME.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Functional annotation report: *Drosophila melanogaster jumu* (Q9XTP7)

## Executive conclusion

The requested target is correctly identified as *Drosophila melanogaster jumeau* (*jumu*, CG4029; UniProt Q9XTP7), not a similarly named gene from another organism. The literature describes Jumu as a 720-amino-acid **nuclear winged-helix/forkhead (Fox) transcription factor**. This agrees with the supplied Fork_head, FOXN1/4, and winged-helix DNA-binding annotations. It is therefore neither an enzyme nor a transporter: its primary biochemical function is sequence-specific DNA binding and context-dependent transcriptional regulation. The strongest functional evidence places Jumu in nuclei of embryonic mesoderm/cardiac progenitors and larval hematopoietic and imaginal-disc cells, where it controls receptor expression, mitotic machinery, cell-fate programs, and cytoskeletal/immune effectors. (wang2019drosophilajumumodulates pages 1-2, hao2018jumuisrequired pages 2-4)

Jumu’s best-resolved primary role is as a **developmental transcriptional hub coupling cell identity to cell division**. In cardiac mesoderm it supports FGF- and Wnt-receptor expression and controls a broad network of mitotic genes. In hematopoietic tissues it regulates progenitor differentiation, niche-cell proliferation, phagocytosis, and suppression of inappropriate Toll-dependent lamellocyte differentiation. Its actions are strongly cell-context dependent and include both transcriptional activation and repression. (hao2017dualrolefor pages 1-2, hasan2024genomewideexpressionprofiling pages 2-3, hasan2024genomewideexpressionprofiling pages 1-2)

## 1. Identity, molecular class, and localization

The symbol, organism, and molecular description are internally consistent across the supplied record and retrieved literature:

- **Gene:** *jumu* / Jumeau; literature also uses CG4029.
- **Organism:** *Drosophila melanogaster*.
- **Protein:** approximately 720 aa and nuclear.
- **Molecular class:** winged-helix/forkhead-box DNA-binding transcription factor.
- **Domain interpretation:** the supplied Fork_head_dom and WH-like DNA-binding superfamily annotations explain nuclear sequence-specific DNA recognition; the supplied FOXN1_4 annotation places it evolutionarily within the FoxN1/4 grouping. The retrieved experimental literature generally calls it a Fox or WH/FKH factor rather than relying on that narrower subfamily label. (wang2019drosophilajumumodulates pages 1-2, hao2018jumuisrequired pages 2-4)

Thus, its operational cellular location is the **nucleus**. Tissue expression is broader: reported sites include embryonic mesoderm and cardiac progenitors, larval lymph gland and circulating hemocytes, brain lobes, central nervous system, imaginal discs, salivary gland, hindgut, and fat body. Presence in a tissue should not be confused with proof of an equally important molecular function in every listed site. (hao2018jumuisrequired pages 1-2, hao2018jumuisrequired pages 2-4)

## 2. Primary molecular function

Jumu does not catalyze a chemical reaction and has no substrate in the enzymatic or transport sense. Its relevant “substrates” are **cis-regulatory DNA sequences associated with target genes**, recognized through its forkhead domain. Depending on enhancer context and partner factors, it can activate or repress transcription. This context dependence is illustrated by cardiac enhancer regulation and by its positive regulation of receptor and cell-division programs versus repression of inappropriate developmental or stress responses. (hasan2024genomewideexpressionprofiling pages 1-2, wang2019drosophilajumumodulates pages 1-2)

A useful mechanistic distinction is required:

1. **Functionally downstream genes** change expression or genetically rescue/interact with *jumu* but may be indirect.
2. **Likely direct targets** additionally have nearby Jumu ChIP-seq occupancy.
3. **Demonstrated direct cis-regulatory targets** require functional Jumu-site mutation or comparable enhancer assays; this highest standard remains unmet for many recently nominated targets.

## 3. Cardiac mesoderm specification and signaling

Jumu and the related Fox factor CHES-1-like act redundantly in embryonic cardiac-mesoderm specification. They transcriptionally promote **heartless (*htl*)**, encoding an FGF receptor, and **frizzled (*fz*)**, encoding a Wnt receptor. Synergistic genetic interactions place the Fox factors in the same specification pathways, while mesodermal overexpression of either receptor partially rescues the defective cardiac specification caused by combined Fox-factor loss. Jumu therefore modulates cardiac signaling chiefly by controlling the receiving cell’s competence to respond to FGF and Wnt signals, rather than by acting as an extracellular ligand or receptor itself. (hasan2024genomewideexpressionprofiling pages 1-2)

Direct Jumu occupancy at the functional *htl* and *fz* enhancers was not established in the retrieved excerpts. Accordingly, transcriptional activation is well supported at the genetic/expression level, but Jumu-specific direct binding should not be overclaimed.

## 4. Cardiac progenitor-cell division network

Earlier genetic work placed Jumu and CHES-1-like upstream of **Polo kinase activity**, controlling three categories of cardiac progenitor division: asymmetric divisions, symmetric divisions, and earlier divisions producing cardiac precursors. Regulation of Polo activity is robust pathway-level evidence, but it does not by itself prove that *polo* is directly bound or transcriptionally controlled by Jumu. (hasan2024genomewideexpressionprofiling pages 1-2)

A more specific downstream effector is **Nebbish (Neb)**, a kinesin. Mesodermal expression profiling identified *neb* as Jumu-activated, and genetic analysis showed that Neb is required for symmetric and earlier precursor-producing divisions, but not the asymmetric category. Synergistic interactions among *neb*, *jumu*, *Myb*, and *polo*, together with rescue by cardiac-mesoderm-specific *neb* expression, support Neb as an integral Jumu-network effector. Quantitative analyses examined at least 179 cardiac hemisegments per genotype, with blinded scoring and permutation tests using one million permutations. Direct functional binding of Jumu to a *neb* enhancer was not demonstrated in that study. (kump2021thedrosophilaforkheadfox pages 13-14)

## 5. Latest research: genome-wide cardiac network, 2024

The most recent target-specific publication located was Hasan et al., published in **December 2024**: [Genome-Wide Expression Profiling and Phenotypic Analysis of Downstream Targets Identify the Fox Transcription Factor Jumeau as a Master Regulator of Cardiac Progenitor Cell Division](https://doi.org/10.3390/ijms252312933). No comparably focused 2023 study was identified.

Using FACS-purified embryonic mesoderm from wild-type and *jumu*-null embryos, the study identified **1,271 dysregulated genes** under stringent thresholds—absolute log2 fold change greater than 1 and FDR below 0.1—and **2,496** under relaxed criteria. Jumu-activated genes were enriched for mitosis, cell cycle, and cell division. Every one of 21 activated candidates subjected to mutant phenotyping produced a cardiac progenitor-division defect, supporting the interpretation of Jumu as a network hub rather than a regulator of only one mitotic effector. (hasan2024genomewideexpressionprofiling pages 2-3)

Public embryonic ChIP-seq profiles nominated 13 of these 21 as **likely direct targets** because Jumu peaks occurred near peaks for cardiogenic regulators: *neb, sti, tum, SMC2, BubR1, barr, cmet, mei-S332, Cenp-C, Cdk2, scra, Incenp,* and *glu*. This list connects Jumu to spindle assembly, chromosome segregation, cytokinesis, and cell-cycle control. However, peak proximity is not equivalent to a validated functional enhancer; the authors explicitly proposed enhancer–reporter and binding-site mutation experiments as necessary follow-up. (hasan2024genomewideexpressionprofiling pages 10-12, hasan2024genomewideexpressionprofiling pages 13-15)

**Retinal Homeobox (*Rx*)** illustrates indirect network regulation. *Rx* lacked an analyzed embryonic Jumu ChIP peak but showed expression and genetic evidence for a shared pathway. *Rx/jumu* double heterozygotes had asymmetric-division defects exceeding an additive expectation with **p < 1 × 10⁻⁶**. This is strong evidence for pathway interaction but not direct Jumu binding to *Rx*. (hasan2024genomewideexpressionprofiling pages 10-12)

## 6. Hematopoietic progenitor regulation

Jumu is expressed throughout the larval lymph gland and performs separable cell-autonomous and non-cell-autonomous functions:

- In medullary-zone prohemocytes, it cell-autonomously maintains appropriate differentiation through regulation of **Collier (*col*)**.
- It non-cell-autonomously prevents excessive expansion of the posterior signaling center, the hematopoietic niche.
- Within posterior-signaling-center cells, it promotes proliferation through positive regulation of **dMyc**.
- Whole-gland deficiency activates **Toll signaling** and drives inappropriate lamellocyte differentiation; suppression of Toll-associated differentiation is linked to Jumu-dependent control of Col. (hao2017dualrolefor pages 1-2)

These experiments make Jumu a regulator of both progenitor-intrinsic state and niche architecture. Col and dMyc are mechanistically supported regulated genes, although direct binding to their cis-regulatory elements was not established in the retrieved evidence.

## 7. Circulating hemocytes, phagocytosis, and innate immunity

In circulating larval hemocytes, Jumu supports differentiation and phagocytic competence. It influences expression of the phagocytic receptor **NimC1** and cytoskeletal remodeling involving **Enabled (Ena)** and **Fascin**, which contribute to lamellipodia and filopodia. The evidence supports an indirect effect on phagocytosis rather than proving that these genes are direct DNA-binding targets. Severe *jumu* deficiency disrupts spindle formation, mitosis, and cytokinesis, producing enlarged multinucleate hemocytes; it also activates Toll signaling and induces lamellocytes. (hao2018jumuisrequired pages 1-2)

Evidence came from in-vivo phagocytosis, immunohistochemistry, qRT-PCR, immunoblotting, BrdU, phospho-histone-H3 and TUNEL assays, and MARCM mosaic analysis. Hemocyte counts used at least 50 larvae per experiment; phagocytosis assays scored 500–1,000 cells per genotype and were repeated at least three times. These sample sizes strengthen the cellular phenotype, although they do not resolve direct transcriptional occupancy. (hao2018jumuisrequired pages 2-4)

## 8. Wing development and stress signaling

In larval and pupal wing tissues, Jumu restrains apoptosis through a **JNK-dependent pathway**. Loss of *jumu* elevates *puckered* and phosphorylated JNK, and JNK RNAi rescues apoptosis. Jumu also supports **cut** expression during wing-margin development and regulates single-hair morphogenesis through a **Rho1-dependent planar-cell-polarity pathway**. The JNK, margin, and hair phenotypes are experimentally separable; *puckered* is a JNK activity readout rather than a demonstrated direct Jumu target, and direct Jumu binding to *cut* or Rho1-pathway loci remains unproven. (wang2019drosophilajumumodulates pages 1-2, wang2019drosophilajumumodulates pages 10-12)

## 9. Evidence summary

The following table separates established physiological functions from candidate direct targets and indirect pathway effects.

| Biological context / cell type | Precise role | Implicated targets / pathways | Evidence type and key quantitative detail | Confidence / limitations | Primary source |
|---|---|---|---|---|---|
| Protein identity and subcellular site | **jumu/CG4029 (Q9XTP7)** encodes a **720-aa nuclear winged-helix/forkhead (Fox) transcription factor**, rather than an enzyme, transporter, or structural protein. Its primary molecular activity is sequence-specific DNA binding and transcriptional regulation. | Conserved WH/FKH DNA-binding domain; consistent with the supplied InterPro Forkhead and FOXN1/4-family annotations. | Protein characterization and family/domain assignment; nuclear localization reported in the literature. (wang2019drosophilajumumodulates pages 1-2, hao2018jumuisrequired pages 2-4) | **High confidence** for nuclear Fox-transcription-factor identity. The cited studies do not independently map every InterPro boundary or experimentally validate the supplied UniProt accession. | Wang et al., 2019, [https://doi.org/10.1007/s10495-019-01527-x](https://doi.org/10.1007/s10495-019-01527-x) |
| Embryonic cardiac mesoderm specification | Jumu and CHES-1-like act redundantly to promote cardiac-mesoderm specification by transcriptionally activating receptors needed to receive FGF and Wnt signals. | **heartless (htl)**, encoding an FGF receptor, and **frizzled (fz)**, encoding a Wnt receptor. Mesodermal htl or fz expression partially rescues the double-Fox loss phenotype. | Genetic interactions, receptor-expression analysis, and tissue-specific rescue support transcriptional activation and pathway placement. (hasan2024genomewideexpressionprofiling pages 1-2) | **Strong functional evidence** that htl and fz are activated downstream of the two Fox factors; because of functional redundancy, the Jumu-specific contribution is context dependent. Direct Jumu occupancy is not established by the cited evidence. | Ahmad et al., 2016, [https://doi.org/10.1242/dev.122952](https://doi.org/10.1242/dev.122952) |
| Embryonic cardiac progenitor divisions | Jumu regulates asymmetric and symmetric cardiac progenitor divisions and earlier divisions that generate cardiac precursors. | **Polo kinase pathway**; Jumu and CHES-1-like regulate Polo activity. | Loss-of-function genetics and cardiac-cell phenotyping place Fox factors upstream of Polo-dependent division. (hasan2024genomewideexpressionprofiling pages 1-2) | **High confidence** in pathway-level function, but Polo activity regulation does not by itself prove that **polo** is a directly bound Jumu transcriptional target. | Ahmad et al., 2012, [https://doi.org/10.1016/j.devcel.2012.05.011](https://doi.org/10.1016/j.devcel.2012.05.011) |
| Subsets of embryonic cardiac progenitor divisions | Jumu activates the kinesin-encoding gene **nebbish (neb)**, which mediates symmetric and earlier precursor-producing divisions but is not required for the Jumu-controlled asymmetric category. | **neb**, with genetic interactions involving **jumu, Myb,** and **polo**. | Mesodermal expression profiling, loss-of-function phenotyping, synergistic genetics, and cardiac-mesoderm-specific rescue. Each quantitative genotype analysis included **at least 179 hemisegments**; permutation tests used **1,000,000 permutations**. (kump2021thedrosophilaforkheadfox pages 13-14) | **Strong functional evidence** that neb is a Jumu-regulated effector and that its expression can rescue jumu-associated defects. Direct Jumu binding to a functional neb enhancer was not demonstrated in that study. | Kump et al., 2021, [https://doi.org/10.1038/s41598-021-81894-1](https://doi.org/10.1038/s41598-021-81894-1) |
| Embryonic mesoderm and cardiac progenitor division network | Genome-wide analysis expands Jumu from a regulator of individual effectors to a hub controlling a broad mitotic gene network. | **21 functionally tested Jumu-activated genes** mediate cardiac progenitor division. Thirteen had Jumu ChIP-seq peaks near peaks for cardiac factors and were classified as **likely direct targets**: **neb, sti, tum, SMC2, BubR1, barr, cmet, mei-S332, Cenp-C, Cdk2, scra, Incenp,** and **glu**. | FACS-isolated stage 11–12 mesoderm, RNA-seq, RT-qPCR, mutant phenotyping, public embryonic ChIP-seq, and interaction-network analysis. **1,271 genes** were dysregulated at absolute log2 fold change >1 and FDR <0.1; relaxed criteria yielded **2,496** regulated genes. All **21** tested activated candidates produced division defects. (hasan2024genomewideexpressionprofiling pages 2-3, hasan2024genomewideexpressionprofiling pages 13-15, hasan2024genomewideexpressionprofiling pages 18-19) | **High confidence** that Jumu broadly controls cell-division gene expression; **moderate confidence** that the 13 candidates are direct targets. ChIP-peak proximity/colocalization is not equivalent to functional enhancer validation, which the authors identify as future work. | Hasan et al., 2024, [https://doi.org/10.3390/ijms252312933](https://doi.org/10.3390/ijms252312933) |
| Rx-dependent asymmetric cardiac progenitor division | Jumu positively regulates **Retinal Homeobox (Rx)** expression, and the two genes function in a shared pathway controlling asymmetric divisions. | **Rx**; no embryonic Jumu ChIP-seq peak was detected at the analyzed locus, favoring indirect regulation. | RNA profiling, RT-qPCR, mutant phenotyping, and genetic interaction. Double heterozygotes showed division defects significantly greater than the additive expectation (**p < 1 × 10⁻⁶**). (hasan2024genomewideexpressionprofiling pages 10-12, hasan2024genomewideexpressionprofiling pages 2-3) | **Strong genetic evidence** for a shared pathway, but **Rx is not a demonstrated direct Jumu target** and may be regulated indirectly. | Hasan et al., 2024, [https://doi.org/10.3390/ijms252312933](https://doi.org/10.3390/ijms252312933) |
| Larval lymph gland: medullary-zone prohemocytes and posterior signaling center | Jumu maintains appropriate progenitor differentiation cell-autonomously in the medullary zone, restricts posterior-signaling-center expansion non-cell-autonomously, and promotes posterior-signaling-center proliferation cell-autonomously. | Maintains **Collier (Col)** expression in medullary-zone progenitors; positively regulates **dMyc** in posterior-signaling-center cells; restrains **Toll signaling** and inappropriate lamellocyte differentiation. | Tissue-specific loss/overexpression and genetic/pathway analyses distinguish autonomous from non-autonomous actions. Whole-gland jumu deficiency activates Toll and induces lamellocytes. (hao2017dualrolefor pages 1-2) | **Strong context-specific genetic evidence**. Col and dMyc are mechanistically linked regulated genes, but direct Jumu occupancy of their cis-regulatory elements is not established by the cited evidence. | Hao & Jin, 2017, [https://doi.org/10.7554/eLife.25094](https://doi.org/10.7554/eLife.25094) |
| Larval circulating hemocytes | Jumu supports plasmatocyte differentiation and phagocytic competence by maintaining receptor expression and cytoskeletal remodeling; severe loss also disrupts mitosis and cytokinesis, producing enlarged multinucleate hemocytes. | **NimC1** phagocytic receptor; **Ena** and **Fascin** as downstream regulators of lamellipodia/filopodia; cytoskeletal organization; severe loss activates **Toll** and promotes lamellocytes. | In vivo phagocytosis, qRT-PCR, immunoblotting, immunohistochemistry, BrdU/PH3/TUNEL assays, and MARCM. Phagocytosis assays scored **500–1,000 cells per genotype** in at least three experiments; hemocyte counts used **≥50 larvae per experiment**. (hao2018jumuisrequired pages 1-2, hao2018jumuisrequired pages 2-4) | **Strong evidence** for physiological and cellular roles. Regulation of NimC1, Ena, and Fascin is reported, but direct binding/transcriptional activation by Jumu was not shown; phagocytosis control is therefore described as indirect. | Hao et al., 2018, [https://doi.org/10.1186/s12964-018-0305-3](https://doi.org/10.1186/s12964-018-0305-3) |
| Larval wing disc, pupal wing, and adult wing | Jumu restrains apoptosis through a JNK-dependent mechanism, supports wing-margin and anterior-cross-vein development, and regulates single-hair morphogenesis. | Loss increases **puckered (puc)** and phosphorylated JNK; **JNK RNAi rescues apoptosis**. Jumu positively regulates **cut** expression at the wing margin. Multiple wing hairs involve a **Rho1-dependent planar-cell-polarity** pathway. | GAL4/UAS knockdown and overexpression, mutant combinations, TUNEL, reporters, immunostaining, microscopy, and genetic rescue/epistasis. (wang2019drosophilajumumodulates pages 1-2, wang2019drosophilajumumodulates pages 10-12) | **Strong evidence** for JNK-dependent apoptosis and Rho1-associated morphogenesis. **puc** is a JNK readout, not a proven direct target; direct Jumu binding to **cut** or Rho1-pathway loci was not demonstrated. | Wang et al., 2019, [https://doi.org/10.1007/s10495-019-01527-x](https://doi.org/10.1007/s10495-019-01527-x) |


*Table: Evidence map for Drosophila melanogaster Jumu, separating established physiological and transcriptional roles from candidate direct targets and indirect pathway effects. Quantitative details and study limitations clarify the strength of each annotation.*

## 10. Current applications and expert interpretation

There is no clinical or industrial implementation of Jumu itself. Its current application is as a **genetically tractable in-vivo model** for conserved principles of:

- coupling transcriptional state to mitosis during organogenesis;
- robustness through redundant developmental transcription factors;
- cardiac progenitor specification through FGF/Wnt receptor control;
- hematopoietic progenitor–niche communication;
- innate immune-cell differentiation and phagocytosis; and
- transcriptional coordination of spindle, chromosome-segregation, and cytokinesis genes.

The 2024 investigators interpret Jumu as a “master regulator” or hub of cardiac progenitor division because numerous responsive cell-division genes yield relevant phenotypes and participate in an interaction network. That interpretation is persuasive at the systems-genetics level, but it should not be read as proof that Jumu directly binds every node. Thirteen targets are supported by ChIP-based nomination, while eight—including *Rx*—appear indirect under the available embryonic datasets. Some network edges were also inferred from ortholog interactions in other species, which requires experimental validation in flies. (hasan2024genomewideexpressionprofiling pages 10-12, hasan2024genomewideexpressionprofiling pages 2-3, hasan2024genomewideexpressionprofiling pages 13-15)

## 11. Recommended functional annotation

**Molecular function:** nuclear forkhead-box sequence-specific DNA-binding transcription regulator; context-dependent activator and repressor.

**Primary biological function:** coordinates developmental cell specification and cell division, especially in embryonic cardiac progenitors, by regulating signaling-receptor and mitotic-effector gene networks.

**Principal cellular location:** nucleus.

**Best-supported pathways and effectors:**

- FGF/Wnt cardiac specification: *htl*, *fz*;
- cardiac progenitor division: Polo activity, *neb*, and a broad mitotic network including *SMC2, BubR1, barr, Cenp-C, Cdk2,* and *Incenp*;
- lymph-gland homeostasis: *col*, *dMyc*, and Toll suppression;
- hemocyte phagocytosis/cytoskeleton: NimC1, Ena, and Fascin;
- wing survival and morphogenesis: JNK, *cut*, and Rho1-associated planar polarity.

Overall confidence is **high** for the protein’s identity as nuclear Fox transcription factor and for its roles in cardiac development and hematopoiesis; **moderate** for many specific direct-target assignments. The most important annotation gap is functional validation of Jumu-bound cis-regulatory elements by enhancer assays, binding-site mutation, and cell-type-resolved occupancy measurements.

References

1. (wang2019drosophilajumumodulates pages 1-2): Xiao Chun Wang, Ziguang Liu, and Li Hua Jin. Drosophila jumu modulates apoptosis via a jnk-dependent pathway and is required for other processes in wing development. Apoptosis, 24:465-477, Feb 2019. URL: https://doi.org/10.1007/s10495-019-01527-x, doi:10.1007/s10495-019-01527-x. This article has 6 citations and is from a peer-reviewed journal.

2. (hao2018jumuisrequired pages 2-4): Yangguang Hao, Shichao Yu, Fangzhou Luo, and Li Hua Jin. Jumu is required for circulating hemocyte differentiation and phagocytosis in drosophila. Cell Communication and Signaling : CCS, Dec 2018. URL: https://doi.org/10.1186/s12964-018-0305-3, doi:10.1186/s12964-018-0305-3. This article has 25 citations.

3. (hao2017dualrolefor pages 1-2): Yangguang Hao and Li Hua Jin. Dual role for jumu in the control of hematopoietic progenitors in the drosophila lymph gland. eLife, Mar 2017. URL: https://doi.org/10.7554/elife.25094, doi:10.7554/elife.25094. This article has 46 citations and is from a domain leading peer-reviewed journal.

4. (hasan2024genomewideexpressionprofiling pages 2-3): M. Rezaul Hasan, Andrew J. Kump, Evelyn C. Stepaniak, Manoj Panta, Kuncha Shashidhar, Rajnandani Katariya, Mofazzal K. Sabbir, Kristopher R. Schwab, Mark H. Inlow, Ye Chen, and Shaad M. Ahmad. Genome-wide expression profiling and phenotypic analysis of downstream targets identify the fox transcription factor jumeau as a master regulator of cardiac progenitor cell division. International Journal of Molecular Sciences, 25(23):12933, Dec 2024. URL: https://doi.org/10.3390/ijms252312933, doi:10.3390/ijms252312933. This article has 4 citations.

5. (hasan2024genomewideexpressionprofiling pages 1-2): M. Rezaul Hasan, Andrew J. Kump, Evelyn C. Stepaniak, Manoj Panta, Kuncha Shashidhar, Rajnandani Katariya, Mofazzal K. Sabbir, Kristopher R. Schwab, Mark H. Inlow, Ye Chen, and Shaad M. Ahmad. Genome-wide expression profiling and phenotypic analysis of downstream targets identify the fox transcription factor jumeau as a master regulator of cardiac progenitor cell division. International Journal of Molecular Sciences, 25(23):12933, Dec 2024. URL: https://doi.org/10.3390/ijms252312933, doi:10.3390/ijms252312933. This article has 4 citations.

6. (hao2018jumuisrequired pages 1-2): Yangguang Hao, Shichao Yu, Fangzhou Luo, and Li Hua Jin. Jumu is required for circulating hemocyte differentiation and phagocytosis in drosophila. Cell Communication and Signaling : CCS, Dec 2018. URL: https://doi.org/10.1186/s12964-018-0305-3, doi:10.1186/s12964-018-0305-3. This article has 25 citations.

7. (kump2021thedrosophilaforkheadfox pages 13-14): Andrew J. Kump, Manoj Panta, Kristopher R. Schwab, Mark H. Inlow, and Shaad M. Ahmad. The drosophila forkhead/fox transcription factor jumeau mediates specific cardiac progenitor cell divisions by regulating expression of the kinesin nebbish. Scientific Reports, Feb 2021. URL: https://doi.org/10.1038/s41598-021-81894-1, doi:10.1038/s41598-021-81894-1. This article has 8 citations and is from a peer-reviewed journal.

8. (hasan2024genomewideexpressionprofiling pages 10-12): M. Rezaul Hasan, Andrew J. Kump, Evelyn C. Stepaniak, Manoj Panta, Kuncha Shashidhar, Rajnandani Katariya, Mofazzal K. Sabbir, Kristopher R. Schwab, Mark H. Inlow, Ye Chen, and Shaad M. Ahmad. Genome-wide expression profiling and phenotypic analysis of downstream targets identify the fox transcription factor jumeau as a master regulator of cardiac progenitor cell division. International Journal of Molecular Sciences, 25(23):12933, Dec 2024. URL: https://doi.org/10.3390/ijms252312933, doi:10.3390/ijms252312933. This article has 4 citations.

9. (hasan2024genomewideexpressionprofiling pages 13-15): M. Rezaul Hasan, Andrew J. Kump, Evelyn C. Stepaniak, Manoj Panta, Kuncha Shashidhar, Rajnandani Katariya, Mofazzal K. Sabbir, Kristopher R. Schwab, Mark H. Inlow, Ye Chen, and Shaad M. Ahmad. Genome-wide expression profiling and phenotypic analysis of downstream targets identify the fox transcription factor jumeau as a master regulator of cardiac progenitor cell division. International Journal of Molecular Sciences, 25(23):12933, Dec 2024. URL: https://doi.org/10.3390/ijms252312933, doi:10.3390/ijms252312933. This article has 4 citations.

10. (wang2019drosophilajumumodulates pages 10-12): Xiao Chun Wang, Ziguang Liu, and Li Hua Jin. Drosophila jumu modulates apoptosis via a jnk-dependent pathway and is required for other processes in wing development. Apoptosis, 24:465-477, Feb 2019. URL: https://doi.org/10.1007/s10495-019-01527-x, doi:10.1007/s10495-019-01527-x. This article has 6 citations and is from a peer-reviewed journal.

11. (hasan2024genomewideexpressionprofiling pages 18-19): M. Rezaul Hasan, Andrew J. Kump, Evelyn C. Stepaniak, Manoj Panta, Kuncha Shashidhar, Rajnandani Katariya, Mofazzal K. Sabbir, Kristopher R. Schwab, Mark H. Inlow, Ye Chen, and Shaad M. Ahmad. Genome-wide expression profiling and phenotypic analysis of downstream targets identify the fox transcription factor jumeau as a master regulator of cardiac progenitor cell division. International Journal of Molecular Sciences, 25(23):12933, Dec 2024. URL: https://doi.org/10.3390/ijms252312933, doi:10.3390/ijms252312933. This article has 4 citations.

## Artifacts

- [Edison artifact artifact-00](jumu-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. hasan2024genomewideexpressionprofiling pages 1-2
2. kump2021thedrosophilaforkheadfox pages 13-14
3. hasan2024genomewideexpressionprofiling pages 2-3
4. hasan2024genomewideexpressionprofiling pages 10-12
5. hao2017dualrolefor pages 1-2
6. hao2018jumuisrequired pages 1-2
7. hao2018jumuisrequired pages 2-4
8. wang2019drosophilajumumodulates pages 1-2
9. hasan2024genomewideexpressionprofiling pages 13-15
10. wang2019drosophilajumumodulates pages 10-12
11. hasan2024genomewideexpressionprofiling pages 18-19
12. Genome-Wide Expression Profiling and Phenotypic Analysis of Downstream Targets Identify the Fox Transcription Factor Jumeau as a Master Regulator of Cardiac Progenitor Cell Division
13. https://doi.org/10.1007/s10495-019-01527-x
14. https://doi.org/10.1242/dev.122952
15. https://doi.org/10.1016/j.devcel.2012.05.011
16. https://doi.org/10.1038/s41598-021-81894-1
17. https://doi.org/10.3390/ijms252312933
18. https://doi.org/10.7554/eLife.25094
19. https://doi.org/10.1186/s12964-018-0305-3
20. https://doi.org/10.1007/s10495-019-01527-x](https://doi.org/10.1007/s10495-019-01527-x
21. https://doi.org/10.1242/dev.122952](https://doi.org/10.1242/dev.122952
22. https://doi.org/10.1016/j.devcel.2012.05.011](https://doi.org/10.1016/j.devcel.2012.05.011
23. https://doi.org/10.1038/s41598-021-81894-1](https://doi.org/10.1038/s41598-021-81894-1
24. https://doi.org/10.3390/ijms252312933](https://doi.org/10.3390/ijms252312933
25. https://doi.org/10.7554/eLife.25094](https://doi.org/10.7554/eLife.25094
26. https://doi.org/10.1186/s12964-018-0305-3](https://doi.org/10.1186/s12964-018-0305-3
27. https://doi.org/10.1007/s10495-019-01527-x,
28. https://doi.org/10.1186/s12964-018-0305-3,
29. https://doi.org/10.7554/elife.25094,
30. https://doi.org/10.3390/ijms252312933,
31. https://doi.org/10.1038/s41598-021-81894-1,