---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-10-09T13:03:26.669278'
end_time: '2026-10-09T13:13:33.474597'
duration_seconds: 606.81
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: DROME
  gene_id: Kpc2
  gene_symbol: Kpc2
  uniprot_accession: A0A0B4KFW5
  protein_description: 'SubName: Full=Kip1 ubiquitination-promoting complex subunit
    2, isoform C {ECO:0000313|EMBL:AGB93630.1};'
  gene_info: Name=Kpc2 {ECO:0000313|EMBL:AGB93630.1, ECO:0000313|FlyBase:FBgn0028372};
    Synonyms=dKPC2 {ECO:0000313|EMBL:AGB93630.1}, Dmel\CG11025 {ECO:0000313|EMBL:AGB93630.1},
    Isopeptidase-T-3 {ECO:0000313|EMBL:AGB93630.1}, isopeptidase-T-3 {ECO:0000313|EMBL:AGB93630.1},
    ISOT-3 {ECO:0000313|EMBL:AGB93630.1}, IsoT-3 {ECO:0000313|EMBL:AGB93630.1}, ISOT-3A
    {ECO:0000313|EMBL:AGB93630.1}; ORFNames=CG11025 {ECO:0000313|EMBL:AGB93630.1,
    ECO:0000313|FlyBase:FBgn0028372}, Dmel_CG11025 {ECO:0000313|EMBL:AGB93630.1};
  organism_full: Drosophila melanogaster (Fruit fly).
  protein_family: Not specified in UniProt
  protein_domains: UBA. (IPR015940); UBA-like_sf. (IPR009060); UBA2_UBAC1. (IPR041927);
    UBAC1. (IPR052476); UBL_UBAC1. (IPR057650)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 28
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 1
  edison_message_content: 1
artifacts:
- filename: artifact-00.md
  path: Kpc2-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: image-1.png
  path: Kpc2-deep-research-falcon_artifacts/image-1.png
  media_type: image/png
  source: edison_message_content
  data_storage_id: null
  description: '## Context ID: pqac-00000027 As requested, I have extracted panel
    L from Figure 1, which illustrates the predicted domain structure shared by the
    Drosophila KPC'
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** A0A0B4KFW5
- **Protein Description:** SubName: Full=Kip1 ubiquitination-promoting complex subunit 2, isoform C {ECO:0000313|EMBL:AGB93630.1};
- **Gene Information:** Name=Kpc2 {ECO:0000313|EMBL:AGB93630.1, ECO:0000313|FlyBase:FBgn0028372}; Synonyms=dKPC2 {ECO:0000313|EMBL:AGB93630.1}, Dmel\CG11025 {ECO:0000313|EMBL:AGB93630.1}, Isopeptidase-T-3 {ECO:0000313|EMBL:AGB93630.1}, isopeptidase-T-3 {ECO:0000313|EMBL:AGB93630.1}, ISOT-3 {ECO:0000313|EMBL:AGB93630.1}, IsoT-3 {ECO:0000313|EMBL:AGB93630.1}, ISOT-3A {ECO:0000313|EMBL:AGB93630.1}; ORFNames=CG11025 {ECO:0000313|EMBL:AGB93630.1, ECO:0000313|FlyBase:FBgn0028372}, Dmel_CG11025 {ECO:0000313|EMBL:AGB93630.1};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** UBA. (IPR015940); UBA-like_sf. (IPR009060); UBA2_UBAC1. (IPR041927); UBAC1. (IPR052476); UBL_UBAC1. (IPR057650)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "Kpc2" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'Kpc2' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **Kpc2** (gene ID: Kpc2, UniProt: A0A0B4KFW5) in DROME.

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
- **UniProt Accession:** A0A0B4KFW5
- **Protein Description:** SubName: Full=Kip1 ubiquitination-promoting complex subunit 2, isoform C {ECO:0000313|EMBL:AGB93630.1};
- **Gene Information:** Name=Kpc2 {ECO:0000313|EMBL:AGB93630.1, ECO:0000313|FlyBase:FBgn0028372}; Synonyms=dKPC2 {ECO:0000313|EMBL:AGB93630.1}, Dmel\CG11025 {ECO:0000313|EMBL:AGB93630.1}, Isopeptidase-T-3 {ECO:0000313|EMBL:AGB93630.1}, isopeptidase-T-3 {ECO:0000313|EMBL:AGB93630.1}, ISOT-3 {ECO:0000313|EMBL:AGB93630.1}, IsoT-3 {ECO:0000313|EMBL:AGB93630.1}, ISOT-3A {ECO:0000313|EMBL:AGB93630.1}; ORFNames=CG11025 {ECO:0000313|EMBL:AGB93630.1, ECO:0000313|FlyBase:FBgn0028372}, Dmel_CG11025 {ECO:0000313|EMBL:AGB93630.1};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** UBA. (IPR015940); UBA-like_sf. (IPR009060); UBA2_UBAC1. (IPR041927); UBAC1. (IPR052476); UBL_UBAC1. (IPR057650)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "Kpc2" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'Kpc2' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **Kpc2** (gene ID: Kpc2, UniProt: A0A0B4KFW5) in DROME.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Functional annotation report: *Drosophila melanogaster* Kpc2

**Target verification.** The supplied UniProt accession **A0A0B4KFW5** identifies Kpc2 **isoform C** at the fly **CG11025** locus. This is the same locus called **dKPC2**, **UBAC1/KPC2 homolog**, or **IsoT-3/ISOT-3A** in the literature—not an unrelated KPC2-named cancer cell line. Genetic mapping, transcript sequencing, a second engineered mutant allele, and genomic rescue establish the CG11025 assignment. The predicted ubiquitin-like (**UBL**) and ubiquitin-associated (**UBA**) domains agree with the supplied domain annotations. Crucially, much of the direct functional evidence concerns the **locus or isoform B**, rather than isoform C specifically. (li2020ageneticscreen pages 4-5, li2020ageneticscreen pages 2-4, li2020ageneticscreen media ad9798f3)

## Primary molecular function and pathway

**Kpc2 is best annotated as a ubiquitin-system adaptor, not as a demonstrated enzyme or transporter.** In fly testes, dKPC2 physically associates with dKPC1/CG6752, the predicted RING-domain E3 ubiquitin-ligase component of the KIP1 ubiquitination-promoting complex (**KPC**). Reciprocal co-immunoprecipitation demonstrates their association; loss of either component greatly reduces the other’s detectable protein, and re-expression restores it. Thus, dKPC2 has an experimentally supported role in assembling or stabilizing the fly KPC complex. The UBA domains suggest ubiquitin recognition, but binding preferences and a direct biochemical substrate for fly dKPC2 have **not** been established. (li2020ageneticscreen pages 8-10, li2020ageneticscreen pages 10-12)

The clearest **fly-specific biological role** is in the sperm-flagellar localization pathway of **Amo**, the fly polycystin-2/TRPP2-family protein. Removing either dKPC2 or dKPC1 prevents Amo accumulation at the mature sperm-tail tip; sperm then fail to enter female sperm-storage organs after mating, causing male sterility. Genomic restoration of dKpc2, or testis-directed expression of **isoform B**, restores Amo localization, sperm storage, and fertility. This establishes a genetic requirement for KPC in Amo targeting, **not** that dKPC2 directly transports Amo or that Amo is its ubiquitination substrate. (li2020ageneticscreen pages 4-5, li2020ageneticscreen pages 2-4)

**What reaction and substrate can be assigned?** The fly complex contains a predicted E3 ligase, dKPC1; dKPC2 itself is an adaptor and no catalytic reaction is assigned to it. dKPC2 undergoes monoubiquitination, and an interaction-defective dKPC1 SPRY-domain mutant lacks detectable modified dKPC2, making dKPC1 a *likely* enzyme responsible. Direct reconstitution of that reaction, its modified residue, and its specificity have not been reported. The investigators could not convincingly detect Amo ubiquitination or direct binding of Amo to either KPC component; total Amo abundance remained similar in mutant and wild-type testes. They favor an **indirect** effect on final flagellar targeting, potentially involving unidentified partners or membrane organization. (li2020ageneticscreen pages 8-10, li2020ageneticscreen pages 12-14)

The principal findings and their limits are summarized below.

| Finding | Experimental evidence | Organism / isoform caveat |
|---|---|---|
| **Identity and architecture** | Genetic mapping, exon sequencing, transcript analysis, null mutagenesis, and genomic rescue identify **CG11025 as Drosophila Kpc2/dKPC2**, homologous to vertebrate UBAC1/KPC2. Transcript B encodes **435 aa**; transcript C encodes **561 aa** and is 126 aa longer at its N terminus. Both predicted proteins have an **N-terminal ubiquitin-like (UBL) domain and two C-terminal ubiquitin-associated (UBA) domains**. Isoform B is 30% identical and 48% similar to human KPC2 (BLAST E value 2 × 10^-35). [Li et al., 30 December 2020](https://doi.org/10.1371/journal.pgen.1009217) (li2020ageneticscreen pages 4-5, li2020ageneticscreen pages 2-4) | Confirms the locus and supports the supplied **A0A0B4KFW5 isoform-C** annotation. However, testis-specific expression of **isoform B**, not C, fully rescued the mutant phenotype; the study therefore inferred that B is the functional testis isoform. |
| **Association with dKPC1** | Reciprocal co-immunoprecipitation from testes demonstrated that dKPC2 and the RING E3-ligase component dKPC1 form a complex in vivo. Only the largest, fully modified dKPC2 band was recovered with dKPC1. Loss of either protein made the other nearly or completely undetectable, and re-expression restored it, demonstrating reciprocal stabilization. [Li et al., 30 December 2020](https://doi.org/10.1371/journal.pgen.1009217) (li2020ageneticscreen pages 8-10, li2020ageneticscreen pages 10-12) | Direct evidence applies to endogenous testis dKPC2 and the isoform-B rescue product. The precise domains mediating the fly interaction—and whether accession A0A0B4KFW5 isoform C participates—were not tested directly. |
| **Localization and biological role** | Antibody imaging localized dKPC2 to a restricted region at the **tip of the mature sperm flagellum**, partially overlapping the TRPP2-family polycystin **Amo**. dKpc2 null and splice-site mutants were viable but male sterile, lacked Amo at the flagellar tip, and failed to store sperm in the female seminal receptacle or spermathecae despite normal courtship, mating, sperm development, individualization, and gross tail ultrastructure. Genomic rescue or testis-specific isoform-B expression restored Amo localization, sperm storage, and fertility; reported fertility comparisons were significant at **p < 0.001**. [Li et al., 30 December 2020](https://doi.org/10.1371/journal.pgen.1009217) (li2020ageneticscreen pages 4-5, li2020ageneticscreen pages 2-4) | This establishes a specialized fly-sperm role in Amo targeting and fertility, but does not establish localization or function of isoform C specifically. “Trafficking” denotes a genetic requirement for correct final localization, not demonstrated direct transport of Amo by dKPC2. |
| **Post-translational modification** | Testis immunoblots detected an unmodified **approximately 49-kDa** species and an **approximately 58-kDa doublet**. Deubiquitinase shifted the doublet downward by approximately 8.5 kDa, whereas phosphatase collapsed its upper band, supporting unmodified, monoubiquitinated, and phosphorylated-monoubiquitinated forms. Mature seminal-vesicle sperm contained only the largest form. An interaction-defective dKpc1 SPRY-domain allele eliminated detectable dKPC2 monoubiquitination, making dKPC1 the likely E3 ligase for dKPC2. [Li et al., 30 December 2020](https://doi.org/10.1371/journal.pgen.1009217) (li2020ageneticscreen pages 4-5, li2020ageneticscreen pages 8-10, li2020ageneticscreen pages 10-12) | Modification assignments are based on enzymatic band shifts and genetics; the modified residues, ubiquitin linkage, responsible kinase, and functional consequences remain unknown. Direct reconstitution of dKPC1-catalyzed dKPC2 ubiquitination was not reported. |
| **Proteasome and p27 mechanism** | Mammalian KPC2/UBAC1 binds KPC1/RNF123, polyubiquitinated proteins, and the 26S proteasome; its UBL/UBA/STI1 architecture supports KPC1 stabilization and proteasome-linked degradation of KPC1-ubiquitinated p27 during G0-to-G1 progression. [Hara et al., November 2005](https://doi.org/10.1128/MCB.25.21.9292-9303.2005) (hara2005roleofthe pages 1-1, hara2005roleofthe pages 1-2, hara2005roleofthe pages 3-5, hara2005roleofthe pages 8-9) | This is **mammalian ortholog evidence**, not a demonstrated reaction of Drosophila dKPC2 or A0A0B4KFW5 isoform C. No fly experiment established p27 as a substrate, proteasome binding, or ubiquitinated-cargo shuttling by isoform C. |
| **Direct Amo ubiquitination or binding** | Amo abundance remained similar to wild type in dKpc1 and dKpc2 mutant testes. Co-immunoprecipitation did not demonstrate direct Amo binding to either KPC component, and the investigators could not convincingly detect Amo ubiquitination or cleavage. They therefore proposed an **indirect** mechanism involving unidentified proteins or modification of the sperm-tail membrane. [Li et al., 30 December 2020](https://doi.org/10.1371/journal.pgen.1009217) (li2020ageneticscreen pages 8-10, li2020ageneticscreen pages 12-14) | Amo is a genetically downstream localization-dependent cargo, **not an established direct dKPC1 substrate or dKPC2-bound cargo**. Substrate specificity of the fly KPC complex remains unresolved. |
| **Status of isoform C / A0A0B4KFW5** | Transcript C was detected in wild-type flies and is disrupted in the causal splice-site mutant; its predicted architecture is compatible with a UBL-UBA adaptor. Nevertheless, testis-specific isoform B alone produced all three observed modification states and fully rescued fertility, sperm storage, and Amo localization. [Li et al., 30 December 2020](https://doi.org/10.1371/journal.pgen.1009217) (li2020ageneticscreen pages 4-5, li2020ageneticscreen pages 2-4, li2020ageneticscreen pages 10-12) | **No isoform-C-specific molecular activity, localization, substrate, or phenotype has been demonstrated.** Functional annotation of A0A0B4KFW5 should distinguish locus-level dKPC2 evidence from isoform-C-specific evidence and treat UBA-mediated ubiquitin recognition as a domain-based inference. |


*Table: Evidence supporting the identity, architecture, localization, and function of Drosophila CG11025/dKPC2, with explicit separation of fly experiments from mammalian ortholog inference. The table highlights that the supplied UniProt isoform C lacks isoform-specific functional validation.*

## Cellular location and isoform resolution

Immunostaining places endogenous dKPC2 in a **restricted region at the tip of the mature sperm flagellum**, partly overlapping Amo. Immunoblots detect dKPC2 in testes and sperm, but not in the tested female or testis-depleted male samples. These observations identify the experimentally supported site of its specialized fly function; they do **not** establish that every Kpc2 splice isoform is sperm-specific or that isoform C individually occupies the flagellar tip. The flagellar-tip staining and Amo comparison are documented in [Li *et al.*, 2020, Figure 3](https://doi.org/10.1371/journal.pgen.1009217.g003). (li2020ageneticscreen pages 5-8, li2020ageneticscreen pages 8-10)

The distinction between **sequence isoforms** and **modified protein forms** matters. The study predicts transcript B to encode **435 amino acids** and transcript C **561 amino acids**, with C having a 126-residue N-terminal extension; both are predicted to contain a UBL and two UBA domains. Yet expression of **B alone** rescued the testis phenotype and yielded the three immunoblot bands attributed to dKPC2. The approximately **49-kDa** band is consistent with unmodified B; an approximately **58-kDa doublet** shifted by roughly **8.5 kDa** upon deubiquitinase treatment, and its upper band shifted upon phosphatase treatment. These experiments support unmodified, monoubiquitinated, and phosphorylated–monoubiquitinated forms, rather than proving that each band represents a different transcript. Only the largest modified form was detected in mature seminal-vesicle sperm and in the dKPC1-associated complex. Predicted isoform architecture is illustrated in [Li *et al.*, 2020, Figure 1L](https://doi.org/10.1371/journal.pgen.1009217.g001). (li2020ageneticscreen pages 4-5, li2020ageneticscreen pages 8-10, li2020ageneticscreen pages 10-12, li2020ageneticscreen media ad9798f3)

## Ortholog evidence versus demonstrated fly function

Mammalian **KPC2/UBAC1** provides a biochemical rationale for the adaptor annotation: its UBA regions bind polyubiquitinated proteins, it associates with proteasome components and KPC1/RNF123, and it promotes proteasome-dependent loss of the cell-cycle inhibitor **p27Kip1** during G0-to-G1 progression. Domain-deletion and depletion/rescue experiments implicate its UBL/UBA and STI1-containing regions in these activities; proteasome association should not be attributed to the UBL domain *alone*, because the reported interaction also depends on a broader N-terminal region. These are **mammalian experiments**, not proof of p27 degradation, proteasome binding, or the same substrate specificity by fly isoform C. [Hara *et al.*, *Molecular and Cellular Biology*, November 2005](https://doi.org/10.1128/MCB.25.21.9292-9303.2005). (hara2005roleofthe pages 1-1, hara2005roleofthe pages 9-10, hara2005roleofthe pages 3-5)

An older review described fly **ISOT-3A** as lacking a UBL domain and noted that it had not yet been experimentally investigated. The subsequent fly primary study predicts an N-terminal UBL in the **B and C isoforms** and supplies direct locus-level experiments. The difference illustrates why isoform choice and the newer primary work take precedence over transferring an older, unqualified domain description. The name “isopeptidase-T-3” should likewise **not** be taken as evidence that this protein is an experimentally validated deubiquitinating enzyme. [Jantrapirom *et al.*, *International Journal of Molecular Sciences*, April 2019](https://doi.org/10.3390/ijms20081893); [Li *et al.*, *PLOS Genetics*, 30 December 2020](https://doi.org/10.1371/journal.pgen.1009217). (jantrapirom2019nonproteasomalublubafamily pages 8-11, li2020ageneticscreen pages 4-5)

## Evidence scale, research status, and applications

The fly discovery arose from a screen of **60** male-sterile mutant stocks producing mature sperm. Isoform B showed **30% amino-acid identity and 48% similarity** to human KPC2 in the reported comparison. Fertility rescue comparisons were reported as **p < 0.001**; precise fertility percentages should not be inferred from the accessible narrative. The work supplies experimentally validated mutant, rescue, tagged-protein, and antibody reagents for investigating sperm-tail protein targeting. This is a **research-model application**, not a demonstrated therapeutic or clinical application of fly Kpc2. [Li *et al.*, *PLOS Genetics* **16**, e1009217, 30 December 2020](https://doi.org/10.1371/journal.pgen.1009217). (li2020ageneticscreen pages 4-5, li2020ageneticscreen pages 2-4, li2020ageneticscreen pages 12-14)

Targeted searches did **not identify a 2023–2024 primary study that newly establishes the molecular function of this specific fly locus or isoform C**. Consequently, the 2020 organism-specific experiments remain more informative for this annotation than newer work on other organisms or similarly named entities. The leading open questions are the direct fly KPC substrate, how dKPC2 modification affects complex activity, the mechanism coupling KPC to Amo localization, and whether **A0A0B4KFW5/isoform C** has a distinct location or function. (li2020ageneticscreen pages 4-5, li2020ageneticscreen pages 12-14)

**Annotation conclusion:** Assign *D. melanogaster* CG11025/Kpc2 a **demonstrated locus-level role as the dKPC1-associated adaptor required for Amo localization at the sperm flagellar tip and consequent sperm storage and male fertility**. Annotate ubiquitin binding, proteasomal cargo shuttling, and p27 turnover as **domain-based or mammalian-ortholog inferences**, not experimentally established activities of **isoform C**. (li2020ageneticscreen pages 2-4, li2020ageneticscreen pages 8-10, hara2005roleofthe pages 1-1)

References

1. (li2020ageneticscreen pages 4-5): Weizhe Li, Jinqing Liang, Patricia Outeda, Stacey Turner, Barbara T. Wakimoto, and Terry Watnick. A genetic screen in drosophila reveals an unexpected role for the kip1 ubiquitination-promoting complex in male fertility. PLOS Genetics, 16:e1009217, Dec 2020. URL: https://doi.org/10.1371/journal.pgen.1009217, doi:10.1371/journal.pgen.1009217. This article has 7 citations and is from a domain leading peer-reviewed journal.

2. (li2020ageneticscreen pages 2-4): Weizhe Li, Jinqing Liang, Patricia Outeda, Stacey Turner, Barbara T. Wakimoto, and Terry Watnick. A genetic screen in drosophila reveals an unexpected role for the kip1 ubiquitination-promoting complex in male fertility. PLOS Genetics, 16:e1009217, Dec 2020. URL: https://doi.org/10.1371/journal.pgen.1009217, doi:10.1371/journal.pgen.1009217. This article has 7 citations and is from a domain leading peer-reviewed journal.

3. (li2020ageneticscreen media ad9798f3): Weizhe Li, Jinqing Liang, Patricia Outeda, Stacey Turner, Barbara T. Wakimoto, and Terry Watnick. A genetic screen in drosophila reveals an unexpected role for the kip1 ubiquitination-promoting complex in male fertility. PLOS Genetics, 16:e1009217, Dec 2020. URL: https://doi.org/10.1371/journal.pgen.1009217, doi:10.1371/journal.pgen.1009217. This article has 7 citations and is from a domain leading peer-reviewed journal.

4. (li2020ageneticscreen pages 8-10): Weizhe Li, Jinqing Liang, Patricia Outeda, Stacey Turner, Barbara T. Wakimoto, and Terry Watnick. A genetic screen in drosophila reveals an unexpected role for the kip1 ubiquitination-promoting complex in male fertility. PLOS Genetics, 16:e1009217, Dec 2020. URL: https://doi.org/10.1371/journal.pgen.1009217, doi:10.1371/journal.pgen.1009217. This article has 7 citations and is from a domain leading peer-reviewed journal.

5. (li2020ageneticscreen pages 10-12): Weizhe Li, Jinqing Liang, Patricia Outeda, Stacey Turner, Barbara T. Wakimoto, and Terry Watnick. A genetic screen in drosophila reveals an unexpected role for the kip1 ubiquitination-promoting complex in male fertility. PLOS Genetics, 16:e1009217, Dec 2020. URL: https://doi.org/10.1371/journal.pgen.1009217, doi:10.1371/journal.pgen.1009217. This article has 7 citations and is from a domain leading peer-reviewed journal.

6. (li2020ageneticscreen pages 12-14): Weizhe Li, Jinqing Liang, Patricia Outeda, Stacey Turner, Barbara T. Wakimoto, and Terry Watnick. A genetic screen in drosophila reveals an unexpected role for the kip1 ubiquitination-promoting complex in male fertility. PLOS Genetics, 16:e1009217, Dec 2020. URL: https://doi.org/10.1371/journal.pgen.1009217, doi:10.1371/journal.pgen.1009217. This article has 7 citations and is from a domain leading peer-reviewed journal.

7. (hara2005roleofthe pages 1-1): Taichi Hara, Takumi Kamura, Shuhei Kotoshiba, Hidehisa Takahashi, Kenichiro Fujiwara, Ichiro Onoyama, Masahiro Shirakawa, Noboru Mizushima, and Keiichi I. Nakayama. Role of the ubl-uba protein kpc2 in degradation of p27 at g1 phase of the cell cycle. Molecular and Cellular Biology, 25:9292-9303, Nov 2005. URL: https://doi.org/10.1128/mcb.25.21.9292-9303.2005, doi:10.1128/mcb.25.21.9292-9303.2005. This article has 96 citations and is from a domain leading peer-reviewed journal.

8. (hara2005roleofthe pages 1-2): Taichi Hara, Takumi Kamura, Shuhei Kotoshiba, Hidehisa Takahashi, Kenichiro Fujiwara, Ichiro Onoyama, Masahiro Shirakawa, Noboru Mizushima, and Keiichi I. Nakayama. Role of the ubl-uba protein kpc2 in degradation of p27 at g1 phase of the cell cycle. Molecular and Cellular Biology, 25:9292-9303, Nov 2005. URL: https://doi.org/10.1128/mcb.25.21.9292-9303.2005, doi:10.1128/mcb.25.21.9292-9303.2005. This article has 96 citations and is from a domain leading peer-reviewed journal.

9. (hara2005roleofthe pages 3-5): Taichi Hara, Takumi Kamura, Shuhei Kotoshiba, Hidehisa Takahashi, Kenichiro Fujiwara, Ichiro Onoyama, Masahiro Shirakawa, Noboru Mizushima, and Keiichi I. Nakayama. Role of the ubl-uba protein kpc2 in degradation of p27 at g1 phase of the cell cycle. Molecular and Cellular Biology, 25:9292-9303, Nov 2005. URL: https://doi.org/10.1128/mcb.25.21.9292-9303.2005, doi:10.1128/mcb.25.21.9292-9303.2005. This article has 96 citations and is from a domain leading peer-reviewed journal.

10. (hara2005roleofthe pages 8-9): Taichi Hara, Takumi Kamura, Shuhei Kotoshiba, Hidehisa Takahashi, Kenichiro Fujiwara, Ichiro Onoyama, Masahiro Shirakawa, Noboru Mizushima, and Keiichi I. Nakayama. Role of the ubl-uba protein kpc2 in degradation of p27 at g1 phase of the cell cycle. Molecular and Cellular Biology, 25:9292-9303, Nov 2005. URL: https://doi.org/10.1128/mcb.25.21.9292-9303.2005, doi:10.1128/mcb.25.21.9292-9303.2005. This article has 96 citations and is from a domain leading peer-reviewed journal.

11. (li2020ageneticscreen pages 5-8): Weizhe Li, Jinqing Liang, Patricia Outeda, Stacey Turner, Barbara T. Wakimoto, and Terry Watnick. A genetic screen in drosophila reveals an unexpected role for the kip1 ubiquitination-promoting complex in male fertility. PLOS Genetics, 16:e1009217, Dec 2020. URL: https://doi.org/10.1371/journal.pgen.1009217, doi:10.1371/journal.pgen.1009217. This article has 7 citations and is from a domain leading peer-reviewed journal.

12. (hara2005roleofthe pages 9-10): Taichi Hara, Takumi Kamura, Shuhei Kotoshiba, Hidehisa Takahashi, Kenichiro Fujiwara, Ichiro Onoyama, Masahiro Shirakawa, Noboru Mizushima, and Keiichi I. Nakayama. Role of the ubl-uba protein kpc2 in degradation of p27 at g1 phase of the cell cycle. Molecular and Cellular Biology, 25:9292-9303, Nov 2005. URL: https://doi.org/10.1128/mcb.25.21.9292-9303.2005, doi:10.1128/mcb.25.21.9292-9303.2005. This article has 96 citations and is from a domain leading peer-reviewed journal.

13. (jantrapirom2019nonproteasomalublubafamily pages 8-11): Salinee Jantrapirom, Luca Lo Piccolo, and Masamitsu Yamaguchi. Non-proteasomal ubl-uba family of proteins in neurodegeneration. International Journal of Molecular Sciences, 20:1893, Apr 2019. URL: https://doi.org/10.3390/ijms20081893, doi:10.3390/ijms20081893. This article has 16 citations.

## Artifacts

- [Edison artifact artifact-00](Kpc2-deep-research-falcon_artifacts/artifact-00.md)
![## Context ID: pqac-00000027 As requested, I have extracted panel L from Figure 1, which illustrates the predicted domain structure shared by the Drosophila KPC](Kpc2-deep-research-falcon_artifacts/image-1.png)

## Citations

1. li2020ageneticscreen pages 4-5
2. li2020ageneticscreen pages 2-4
3. li2020ageneticscreen pages 8-10
4. li2020ageneticscreen pages 10-12
5. li2020ageneticscreen pages 12-14
6. hara2005roleofthe pages 1-1
7. hara2005roleofthe pages 1-2
8. hara2005roleofthe pages 3-5
9. hara2005roleofthe pages 8-9
10. li2020ageneticscreen pages 5-8
11. hara2005roleofthe pages 9-10
12. jantrapirom2019nonproteasomalublubafamily pages 8-11
13. Li et al., 30 December 2020
14. Hara et al., November 2005
15. Li *et al.*, 2020, Figure 3
16. Li *et al.*, 2020, Figure 1L
17. Hara *et al.*, *Molecular and Cellular Biology*, November 2005
18. Jantrapirom *et al.*, *International Journal of Molecular Sciences*, April 2019
19. Li *et al.*, *PLOS Genetics*, 30 December 2020
20. Li *et al.*, *PLOS Genetics* **16**, e1009217, 30 December 2020
21. https://doi.org/10.1371/journal.pgen.1009217
22. https://doi.org/10.1128/MCB.25.21.9292-9303.2005
23. https://doi.org/10.1371/journal.pgen.1009217.g003
24. https://doi.org/10.1371/journal.pgen.1009217.g001
25. https://doi.org/10.3390/ijms20081893
26. https://doi.org/10.1371/journal.pgen.1009217,
27. https://doi.org/10.1128/mcb.25.21.9292-9303.2005,
28. https://doi.org/10.3390/ijms20081893,