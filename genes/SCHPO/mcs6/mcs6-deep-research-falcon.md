---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-26T20:27:41.796818'
end_time: '2026-09-26T20:38:27.677210'
duration_seconds: 645.88
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: SCHPO
  gene_id: mcs6
  gene_symbol: crk1
  uniprot_accession: Q12126
  protein_description: 'RecName: Full=Serine/threonine-protein kinase crk1; EC=2.7.11.23
    {ECO:0000269|PubMed:8557036, ECO:0000269|PubMed:8557037, ECO:0000269|PubMed:9857180};
    AltName: Full=Mitotic catastrophe suppressor 6;'
  gene_info: Name=crk1; Synonyms=mcs6, mop1; ORFNames=SPBC19F8.07;
  organism_full: Schizosaccharomyces pombe (strain 972 / ATCC 24843) (Fission yeast).
  protein_family: Belongs to the protein kinase superfamily. CMGC Ser/Thr
  protein_domains: CDK. (IPR050108); CDK7. (IPR037770); Kinase-like_dom_sf. (IPR011009);
    Prot_kinase_dom. (IPR000719); Protein_kinase_ATP_BS. (IPR017441)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 38
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: mcs6-deep-research-falcon_artifacts/artifact-00.md
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
- **UniProt Accession:** Q12126
- **Protein Description:** RecName: Full=Serine/threonine-protein kinase crk1; EC=2.7.11.23 {ECO:0000269|PubMed:8557036, ECO:0000269|PubMed:8557037, ECO:0000269|PubMed:9857180}; AltName: Full=Mitotic catastrophe suppressor 6;
- **Gene Information:** Name=crk1; Synonyms=mcs6, mop1; ORFNames=SPBC19F8.07;
- **Organism (full):** Schizosaccharomyces pombe (strain 972 / ATCC 24843) (Fission yeast).
- **Protein Family:** Belongs to the protein kinase superfamily. CMGC Ser/Thr
- **Key Domains:** CDK. (IPR050108); CDK7. (IPR037770); Kinase-like_dom_sf. (IPR011009); Prot_kinase_dom. (IPR000719); Protein_kinase_ATP_BS. (IPR017441)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "crk1" matches the protein description above**
2. **Verify the organism is correct:** Schizosaccharomyces pombe (strain 972 / ATCC 24843) (Fission yeast).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'crk1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **crk1** (gene ID: mcs6, UniProt: Q12126) in SCHPO.

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
- **UniProt Accession:** Q12126
- **Protein Description:** RecName: Full=Serine/threonine-protein kinase crk1; EC=2.7.11.23 {ECO:0000269|PubMed:8557036, ECO:0000269|PubMed:8557037, ECO:0000269|PubMed:9857180}; AltName: Full=Mitotic catastrophe suppressor 6;
- **Gene Information:** Name=crk1; Synonyms=mcs6, mop1; ORFNames=SPBC19F8.07;
- **Organism (full):** Schizosaccharomyces pombe (strain 972 / ATCC 24843) (Fission yeast).
- **Protein Family:** Belongs to the protein kinase superfamily. CMGC Ser/Thr
- **Key Domains:** CDK. (IPR050108); CDK7. (IPR037770); Kinase-like_dom_sf. (IPR011009); Prot_kinase_dom. (IPR000719); Protein_kinase_ATP_BS. (IPR017441)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "crk1" matches the protein description above**
2. **Verify the organism is correct:** Schizosaccharomyces pombe (strain 972 / ATCC 24843) (Fission yeast).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'crk1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **crk1** (gene ID: mcs6, UniProt: Q12126) in SCHPO.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Functional annotation report: *Schizosaccharomyces pombe crk1/mcs6* (UniProt Q12126)

## Executive conclusion

The requested protein is correctly identified as the *Schizosaccharomyces pombe* CDK7-family kinase **Crk1/Mcs6**—not one of the unrelated fungal proteins also named CRK1. Its best-supported primary function is as the catalytic kinase of the **Mcs6–Mcs2–Pmh1 complex**, the fission-yeast counterpart of metazoan CDK7–cyclin H–MAT1. This complex has two experimentally separable outputs: it activates the principal cell-cycle CDK Cdc2 through T-loop phosphorylation and acts with TFIIH as an RNA-polymerase-II C-terminal-domain kinase, preferentially supporting CTD Ser5 phosphorylation. These activities connect cell-cycle progression with initiation-associated transcription, especially the expression of genes required for cytokinesis and cell separation. (hermand2001specificityofcdk pages 1-2, saiz2002acdkactivatingkinase pages 3-4, lee2005impairmentofthe pages 1-2)

## 1. Mandatory identity verification

The 1995 cloning study established that *crk1*—“CDK-related kinase 1”—is allelic to the mitotic-catastrophe-suppressor locus *mcs6*. It encodes a predicted 335-amino-acid serine/threonine kinase, associates with the cyclin-H-like protein Mcs2, and belongs phylogenetically to the MO15/CDK7/Kin28-related CDK group. The reported 46% identity to *Xenopus* MO15 and 48% identity to budding-yeast Kin28, together with complementation by MO15, support the CDK7-family assignment. This agrees with the supplied UniProt Q12126 CMGC kinase, CDK and CDK7 domain annotations. (buck1995identificationofa pages 2-3, buck1995identificationofa pages 1-2)

The target organism is specifically fission yeast, *S. pombe*, corresponding to the supplied strain context. Searches also recovered proteins called CRK1 from *Candida albicans* and *Ustilago maydis*, but these are different proteins with different biological roles and are excluded from this annotation. The alias **mop1** is accepted from the supplied UniProt record, although the retrieved primary passages most directly establish the *crk1–mcs6* equivalence rather than independently validating *mop1*.

Crk1/Mcs6 is essential. Deletion-bearing spores undergo several divisions and then arrest, commonly with septa and condensed or segregated chromatin; complementation by an intact *crk1* ORF confirms that lethality maps to this locus. (buck1995identificationofa pages 2-3, buck1995identificationofa pages 1-2)

## 2. Molecular function and catalytic reaction

Mcs6 is an ATP-dependent protein serine/threonine kinase. Its general reaction is:

**ATP + protein-OH → ADP + phosphoprotein**

Its physiologically supported substrate classes are substantially narrower than this generic reaction suggests:

1. **Cell-cycle CDKs**, most importantly Cdc2 at its activation-loop residue **Thr167**.
2. **RNA polymerase II CTD repeats**, with a strong functional association with **Ser5 phosphorylation**.

### 2.1 Cdc2-activating kinase activity

Mcs6 is a physiological CDK-activating kinase, or CAK, for Cdc2. Activating phosphorylation of Cdc2 Thr167 promotes Cdc2–cyclin activity required for both G1/S progression and mitotic entry. In the combined *csk1Δ mcs6-13* mutant, Cdc2–Cdc13 complexes assemble normally but fail to activate efficiently; isolated complexes are stimulated approximately four- to fivefold by added CAK, compared with less than twofold for wild-type or single-mutant complexes. This localizes the defect to activating phosphorylation rather than cyclin-complex assembly. (lee1999cdc2activationin pages 3-4, lee1999cdc2activationin pages 2-3)

The precise relationship between Mcs6 and the second fission-yeast CAK, Csk1, evolved across studies. One biochemical model placed them in a linear pathway—Csk1 phosphorylates Mcs6, which activates Cdc2—and showed that Csk1 did not bind or phosphorylate *S. pombe* Cdc2 under the tested conditions. (hermand2001specificityofcdk pages 4-5, hermand2001specificityofcdk pages 1-2) Later genetics and biochemical work favored a **branched, partially overlapping CAK network**: Csk1 can maintain Cdc2 Thr167 phosphorylation when Mcs6 CAK function is compromised, while Mcs6 retains a separate essential transcriptional function. The most balanced interpretation is therefore that Mcs6 is a direct physiological Cdc2 CAK, while Csk1 acts both upstream of Mcs6 and, in some experimental contexts, in parallel to support Cdc2 activation. (saiz2002acdkactivatingkinase pages 3-4, saiz2002acdkactivatingkinase pages 4-6)

### 2.2 RNA polymerase II CTD kinase activity

Crk1–Mcs2 complexes phosphorylate an RNAPII CTD substrate in vitro. Conditional Mcs6 impairment reduces CTD phosphorylation in vivo, especially Ser5, while Ser2 phosphorylation is relatively preserved. Mcs6 immunocomplexes also directly phosphorylate GST-CTD substrates. These results identify Mcs6 as an initiation-associated CTD kinase rather than a general kinase for every CTD phosphosite. (buck1995identificationofa pages 1-2, saiz2002acdkactivatingkinase pages 3-4, saiz2002acdkactivatingkinase pages 4-6)

The transcriptional output is separable from Cdc2 activation. Tight conditional *mcs6* mutants can lose CTD kinase activity and arrest while retaining Cdc2 T-loop phosphorylation; conversely, combined Mcs6/Csk1 CAK impairment can block the cell cycle while CTD phosphorylation remains near wild-type levels. (saiz2002acdkactivatingkinase pages 4-6, saiz2002acdkactivatingkinase pages 1-2)

## 3. Complex composition and upstream regulation

Mcs6 is the catalytic component of the **Mcs6–Mcs2–Pmh1** complex:

- **Mcs6:** CDK7-like catalytic kinase.
- **Mcs2:** cyclin-H-like regulatory subunit.
- **Pmh1:** MAT1/Tfb3-related assembly subunit connecting the kinase module to TFIIH.

Mcs6 specifically coprecipitates with Mcs2, and the ternary complex is evolutionarily and functionally analogous to CDK7–cyclin H–MAT1. Coexpression of Mcs6 and Mcs2, but not either alone, can provide CAK activity in a heterologous yeast complementation assay. (buck1995identificationofa pages 4-5, lee2005impairmentofthe pages 3-5, hermand2001specificityofcdk pages 2-3)

Csk1 directly phosphorylates Mcs6 at **Ser165**, the Mcs6 activation-loop site corresponding functionally to the canonical CDK7 activating site. Mutation of Ser165 eliminates this labeling, and deletion of *csk1* reduces Mcs2-associated kinase activity by approximately threefold. Pretreatment with Csk1 increases Mcs6-complex activity toward both CTD and CDK substrates. Nevertheless, Mcs6-S165A retains measurable activity and can support relevant genetic functions, showing that Ser165 phosphorylation enhances rather than absolutely licenses catalysis. (hermand1998fissionyeastcsk1 pages 3-5, hermand1998fissionyeastcsk1 pages 2-3, hermand1998fissionyeastcsk1 pages 6-7)

## 4. Biological pathways and processes

### Cell-cycle control

Mcs6-dependent Cdc2 activation contributes to the G1/S and G2/M transitions. Loss of both Mcs6 and Csk1 CAK capacity causes an early Cdc2-deficient arrest: cells elongate, do not divide after heat shift, and approximately 90–95% retain one DNA mass. By contrast, depletion of Mcs6 alone permits roughly five to seven divisions before a later, heterogeneous arrest dominated by septated binucleate cells. This difference reveals an Mcs6 function beyond Cdc2 activation. (saiz2002acdkactivatingkinase pages 1-2, lee1999cdc2activationin pages 2-3)

### Pol II transcription and cell separation

Conditional Mcs6 or Pmh1 impairment causes rapid CTD Ser5 hypophosphorylation but does not immediately abolish bulk transcription. Instead, transcriptional effects are selective. Prolonged severe impairment produces about a one-third decrease in overall expression, while approximately 5% of transcripts fall more than twofold; an alternative normalization identified about 500 changing transcripts, roughly 10% of the genome. These figures are method-dependent and should not be treated as contradictory estimates of one identical quantity. (lee2005impairmentofthe pages 1-2, lee2005impairmentofthe pages 3-5)

Sensitive genes are enriched for the Sep1/Ace2-regulated mitotic program and include *ace2, eng1, agn1, mid2, sou1* and *cdc15*. Their products support cytokinesis, septum digestion and daughter-cell separation. Accordingly, conditional mutants accumulate persistent or multiple septa, multinucleate cells, branching, chains of unseparated cells and abnormal morphology. Genetic interactions with *sep1* and synthetic lethality with *sep10* further connect the TFIIH-associated kinase to this transcriptional program. (lee2005impairmentofthe pages 8-9, lee2005impairmentofthe pages 5-8, lee2005impairmentofthe pages 9-10)

Thus, the “mitotic catastrophe suppressor” phenotype is not evidence that Mcs6 is merely a checkpoint protein. It reflects the intersection of direct Cdc2 activation and transcription of a cell-cycle-regulated gene set.

## 5. Cellular localization

The functional site of Mcs6 action is principally **nuclear**: it is associated with TFIIH-like transcription machinery and phosphorylates the CTD of nuclear RNAPII, while also acting on intracellular Cdc2. However, the retrieved studies establish this compartment mainly through complex association and substrate biology; they did not provide definitive endogenous fluorescence-microscopy localization in the examined passages. “Nuclear/TFIIH-associated” is therefore a strong functional localization, but direct imaging evidence should not be implied. (lee2005impairmentofthe pages 1-2, lee2005impairmentofthe pages 10-11, lee2005impairmentofthe pages 3-5)

## 6. Recent developments, 2023–2024

Direct 2023–2024 research focused specifically on *S. pombe* Mcs6 is sparse; the definitive functional literature remains the 1995–2005 primary work. A 2023 chemical-genetic study used analog-sensitive Mcs6 and four hours of 3-MB-PP1 treatment to test Pol II-dependent chromatin remodeling at selected Pol III loci. Mcs6 inhibition did not significantly increase histone H3 occupancy at those loci, whereas inhibition of the CTD Ser2 kinase Lsk1 did. This is a useful negative boundary: Mcs6-dependent initiation/Ser5 activity was not required for the tested nucleosome-depletion effect, but the result does not weaken Mcs6’s established role in Pol II transcription generally. (yaguesanz2023chromatinremodelingby pages 3-4)

A 2024 structure of **human** CDK7–cyclin H–MAT1 showed that phosphorylation of CDK7 S164 and T170 has substrate-selective effects: dual phosphorylation particularly enhances multisite phosphorylation of repetitive RNAPII-CTD and SPT5 substrates, whereas CAK activity toward CDK substrates is relatively insensitive. This updates the general CDK7-family model from a simple on/off activation switch to regulation of substrate recognition or processivity. It is relevant to Mcs6 as a hypothesis, not direct evidence: the human S164-centered interaction network is incompletely conserved in *S. pombe*, and no equivalent dual-phosphorylation structure or ordered mechanism has been demonstrated for Mcs6. (duster2024structuralbasisof pages 8-10, duster2024structuralbasisof pages 2-3, duster2024structuralbasisof pages 1-2)

## 7. Applications and expert interpretation

Mcs6 has no established clinical or industrial implementation. Its principal real-world application is as a **genetically tractable model of conserved CDK7 biology**. Fission yeast uniquely preserves both major CDK7-like outputs—cell-cycle-CDK activation and transcriptional CTD phosphorylation—allowing conditional alleles, suppressor genetics, biochemical reconstitution and analog-sensitive chemical genetics to separate functions that are intertwined in metazoan CDK7. Modern reviews use Mcs6 as an evolutionary reference for understanding transcriptional CDKs and why CDK7 inhibition can influence both transcription and cell-cycle control. (parua2020dissectingthepol pages 3-4)

The expert consensus supported by the primary evidence is that Mcs6 should be annotated neither solely as a CAK nor solely as a transcription kinase. It is a **dual-function CDK7 ortholog** whose essentiality probably reflects its TFIIH/Pol II role plus contributions to Cdc2 activation. Csk1 provides overlapping cell-cycle CAK capacity but cannot replace the essential transcription-associated Mcs6 complex. (lee1999cdc2activationin pages 3-4, saiz2002acdkactivatingkinase pages 4-6, lee1999cdc2activationin pages 4-4)

## 8. Evidence matrix

The following table distinguishes direct findings from qualified inference and includes the principal dates and DOI links.

| Claim/function | Direct evidence | Evidence strength/qualification | Key source/date/DOI URL |
|---|---|---|---|
| **Identity:** Crk1 is Mcs6 (also Mop1), UniProt Q12126, in *Schizosaccharomyces pombe* | Genetic allelism established that *crk1* and *mcs6* are the same locus; the product is a 335-aa serine/threonine kinase related to CDK7/MO15/Kin28. | **Strong, direct genetic and sequence evidence.** Unrelated proteins called CRK1 in other fungi are not this protein. The supplied UniProt aliases/domain assignment are concordant with the literature. | Buck, Russell & Millar, Dec 1995, *EMBO J.* [DOI](https://doi.org/10.1002/j.1460-2075.1995.tb00308.x) (buck1995identificationofa pages 2-3, buck1995identificationofa pages 1-2) |
| **Complex composition:** catalytic subunit of Mcs6–Mcs2–Pmh1 | Mcs6 specifically coprecipitated with cyclin-H-like Mcs2; later work identified Pmh1 as the MAT1-related third subunit, defining a complex analogous to metazoan CDK7–cyclin H–MAT1. | **Strong biochemical and evolutionary evidence.** Mcs2/Pmh1 association supports both CAK and TFIIH-linked functions. | Buck et al., Dec 1995, [DOI](https://doi.org/10.1002/j.1460-2075.1995.tb00308.x); Hermand et al., Jan 2001, [DOI](https://doi.org/10.1093/emboj/20.1.82); Lee et al., Jun 2005, [DOI](https://doi.org/10.1091/mbc.e04-11-0982) (buck1995identificationofa pages 4-5, hermand2001specificityofcdk pages 2-3, lee2005impairmentofthe pages 3-5) |
| **Enzymatic reaction:** ATP-dependent protein serine/threonine phosphorylation | Mcs6-containing complexes phosphorylate CDKs and the repetitive C-terminal domain (CTD) of RNA polymerase II. | **Strong direct kinase-assay evidence.** Physiologically important substrate classes are CDK activation loops and the Pol II CTD; broad proteome-wide specificity has not been defined. | Buck et al., Dec 1995, [DOI](https://doi.org/10.1002/j.1460-2075.1995.tb00308.x); Saiz & Fisher, Jul 2002, [DOI](https://doi.org/10.1016/S0960-9822(02)00903-X) (buck1995identificationofa pages 1-2, saiz2002acdkactivatingkinase pages 3-4) |
| **Cell-cycle substrate:** activating phosphorylation of Cdc2 at Thr167 | Mcs6 activates Cdc2 by T-loop phosphorylation; combined Mcs6/Csk1 impairment reduces Thr167 phosphorylation and Cdc2-associated kinase activity despite normal Cdc2–Cdc13 assembly. Isolated double-mutant complexes were stimulated about **4–5-fold** by added CAK, versus **<2-fold** for wild-type or single-mutant complexes. | **Strong biochemical and genetic evidence**, although studies differed on how directly Csk1 also contributes to Cdc2 activation. The consensus is that Mcs6 is a physiological Cdc2 CAK and that Mcs6/Csk1 form a partially overlapping or branched CAK network. | Lee et al., Apr 1999, *Current Biology*, [DOI](https://doi.org/10.1016/S0960-9822(99)80194-8); Hermand et al., Jan 2001, [DOI](https://doi.org/10.1093/emboj/20.1.82); Saiz & Fisher, Jul 2002, [DOI](https://doi.org/10.1016/S0960-9822(02)00903-X) (hermand2001specificityofcdk pages 1-2, lee1999cdc2activationin pages 3-4, saiz2002acdkactivatingkinase pages 4-6) |
| **Transcriptional substrate:** preferential phosphorylation of RNAPII CTD Ser5 | Mcs6 immunocomplexes phosphorylated GST-CTD in vitro; conditional Mcs6 or Pmh1 impairment rapidly reduced CTD Ser5 phosphorylation in vivo, while Ser2 phosphorylation was comparatively retained. | **Strong direct biochemical and conditional-genetic evidence.** Mcs6 is best classified as an initiation-associated CTD Ser5 kinase, but residual activity means conditional mutants do not necessarily reveal every essential transcriptional target. | Saiz & Fisher, Jul 2002, [DOI](https://doi.org/10.1016/S0960-9822(02)00903-X); Lee et al., Jun 2005, [DOI](https://doi.org/10.1091/mbc.e04-11-0982) (saiz2002acdkactivatingkinase pages 3-4, lee2005impairmentofthe pages 3-5, saiz2002acdkactivatingkinase pages 4-6) |
| **Upstream regulation:** Csk1 phosphorylates Mcs6 Ser165 | Recombinant Csk1 phosphorylated Mcs6 at Ser165; S165 mutation abolished that labeling. Deleting *csk1* reduced Mcs2-associated CTD kinase activity about **threefold**, and Csk1 pretreatment enhanced Mcs6-complex activity toward CTD and CDK substrates. | **Strong direct biochemical evidence for regulation.** Ser165 phosphorylation enhances activity but is not absolutely required: Mcs6-S165A retains activity and can support viability in tested contexts. | Hermand et al., Dec 1998, *EMBO J.*, [DOI](https://doi.org/10.1093/emboj/17.24.7230) (hermand1998fissionyeastcsk1 pages 3-5, hermand1998fissionyeastcsk1 pages 2-3, hermand1998fissionyeastcsk1 pages 6-7) |
| **Essentiality and terminal phenotypes** | *crk1/mcs6* deletion is lethal; spores carrying the disruption divide approximately **5–7 times** before arrest. About **50–70%** of depleted cells contain two nuclei and a septum, with a smaller four-nucleus/three-septum class. Conditional mutants show multinucleation, persistent septa, branching, and failed cell separation. | **Strong direct genetic evidence.** Delayed arrest reflects inherited maternal/parental protein and reveals an essential transcription/cell-division function beyond Cdc2 activation alone. | Buck et al., Dec 1995, [DOI](https://doi.org/10.1002/j.1460-2075.1995.tb00308.x); Saiz & Fisher, Jul 2002, [DOI](https://doi.org/10.1016/S0960-9822(02)00903-X) (buck1995identificationofa pages 2-3, saiz2002acdkactivatingkinase pages 1-2) |
| **Selective transcriptional program and quantitative transcriptomics** | Conditional Mcs6/Pmh1 impairment caused only about a **one-third** reduction in overall expression after prolonged severe impairment, while roughly **5%** of transcripts decreased more than twofold; another normalization identified approximately **500 genes (~10% of the genome)** changing by more than twofold. Sensitive genes included *ace2, eng1, agn1, mid2, sou1,* and *cdc15*. | **Strong transcriptomic evidence, with normalization-dependent percentages.** Effects are selective and enriched for Sep1/Ace2-regulated cytokinesis and cell-separation genes, rather than an immediate global Pol II shutdown. | Lee et al., Jun 2005, [DOI](https://doi.org/10.1091/mbc.e04-11-0982) (lee2005impairmentofthe pages 1-2, lee2005impairmentofthe pages 8-9, lee2005impairmentofthe pages 5-8, lee2005impairmentofthe pages 3-5) |
| **Functional localization:** nuclear TFIIH/Pol II transcription machinery | Mcs6 is biochemically associated with a TFIIH-like complex and acts on the nuclear RNAPII CTD; its Cdc2 substrate is also intracellular. | **Strong functional-compartment inference, but limited direct localization evidence.** Nuclear action is compelling from TFIIH/Pol II association, yet the retrieved studies did not provide definitive fluorescence-microscopy localization of endogenous Mcs6; “nuclear” should therefore not be presented as independently imaged here. | Lee et al., Jun 2005, [DOI](https://doi.org/10.1091/mbc.e04-11-0982) (lee2005impairmentofthe pages 1-2, lee2005impairmentofthe pages 10-11, lee2005impairmentofthe pages 3-5) |
| **2023 chemical-genetic result:** Mcs6 was not required for the tested Pol II-dependent chromatin effect at Pol III loci | An analog-sensitive Mcs6 strain was treated with 3-MB-PP1 for **4 h**; anti-H3 ChIP detected no significant histone-occupancy change at tested tDNA/Pol III loci. In contrast, inhibition of the CTD Ser2 kinase Lsk1 increased occupancy. | **Direct negative result with locus- and time-window limits.** It argues against Mcs6-dependent Ser5 phosphorylation maintaining nucleosome depletion at the tested Pol III loci, not against Mcs6’s established Pol II role generally. | Yague-Sanz et al., Jun 2023, *Nature Communications*, [DOI](https://doi.org/10.1038/s41467-023-39387-4) (yaguesanz2023chromatinremodelingby pages 3-4) |
| **2024 mechanistic inference from human CDK7:** T-loop phosphorylation can tune transcriptional-substrate recognition/processivity | A human CDK7–cyclin H–MAT1 structure showed that pT170 and pS164 have distinct roles; dual phosphorylation enhanced multisite RNAPII-CTD and SPT5-repeat phosphorylation, whereas CAK activity toward CDK substrates was comparatively insensitive. | **Non-direct orthology-based inference only.** The human S164-centered network is incompletely conserved in *S. pombe*; it suggests hypotheses about Mcs6 substrate selectivity but does not demonstrate a dual-phosphorylation mechanism in Mcs6. | Düster et al., Aug 2024, *Nature Communications*, [DOI](https://doi.org/10.1038/s41467-024-50891-z) (duster2024structuralbasisof pages 8-10, duster2024structuralbasisof pages 2-3, duster2024structuralbasisof pages 1-2) |


*Table: Evidence matrix for the verified S. pombe Crk1/Mcs6 protein, separating direct genetic and biochemical findings from localization inference and human-CDK7 extrapolation.*

## 9. Remaining uncertainties

Major unresolved issues include the complete physiological substrate repertoire, whether Mcs6 directly phosphorylates CTD sites beyond Ser5 under defined cellular conditions, the quantitative division of Cdc2 activation between Mcs6 and Csk1 across growth states, and direct high-resolution localization of endogenous Mcs6. No *S. pombe* Mcs6 structure was found, and the 2024 human CDK7 dual-phosphorylation mechanism cannot yet be transferred wholesale to fission yeast. The most defensible concise annotation is therefore: **essential nuclear CDK7-family serine/threonine kinase; catalytic subunit of the Mcs6–Mcs2–Pmh1/TFIIH-associated complex; activates Cdc2 by Thr167 phosphorylation and promotes RNAPII CTD Ser5 phosphorylation, thereby coupling cell-cycle progression to selective cell-cycle-regulated transcription and cell separation.**

References

1. (hermand2001specificityofcdk pages 1-2): D. Hermand, T. Westerling, A. Pihlak, J. Thuret, T. Vallenius, M. Tiainen, J. Vandenhaute, G. Cottarel, C. Mann, and T. Mäkelä. Specificity of cdk activation in vivo by the two caks mcs6 and csk1 in fission yeast. The EMBO Journal, 20:82-90, Jan 2001. URL: https://doi.org/10.1093/emboj/20.1.82, doi:10.1093/emboj/20.1.82. This article has 46 citations.

2. (saiz2002acdkactivatingkinase pages 3-4): Julia E. Saiz and Robert P. Fisher. A cdk-activating kinase network is required in cell cycle control and transcription in fission yeast. Current Biology, 12:1100-1105, Jul 2002. URL: https://doi.org/10.1016/s0960-9822(02)00903-x, doi:10.1016/s0960-9822(02)00903-x. This article has 60 citations and is from a highest quality peer-reviewed journal.

3. (lee2005impairmentofthe pages 1-2): Karen M. Lee, Ida Miklos, Hongyan Du, Stephen Watt, Zsolt Szilagyi, Julia E. Saiz, Ram Madabhushi, Christopher J. Penkett, Matthias Sipiczki, Jürg Bähler, and Robert P. Fisher. Impairment of the tfiih-associated cdk-activating kinase selectively affects cell cycle-regulated gene expression in fission yeast. Molecular biology of the cell, 16 6:2734-45, Jun 2005. URL: https://doi.org/10.1091/mbc.e04-11-0982, doi:10.1091/mbc.e04-11-0982. This article has 71 citations and is from a domain leading peer-reviewed journal.

4. (buck1995identificationofa pages 2-3): V. Buck, Paul Russell, and J. B. Millar. Identification of a cdk‐activating kinase in fission yeast. The EMBO Journal, 14:6173-6183, Dec 1995. URL: https://doi.org/10.1002/j.1460-2075.1995.tb00308.x, doi:10.1002/j.1460-2075.1995.tb00308.x. This article has 145 citations.

5. (buck1995identificationofa pages 1-2): V. Buck, Paul Russell, and J. B. Millar. Identification of a cdk‐activating kinase in fission yeast. The EMBO Journal, 14:6173-6183, Dec 1995. URL: https://doi.org/10.1002/j.1460-2075.1995.tb00308.x, doi:10.1002/j.1460-2075.1995.tb00308.x. This article has 145 citations.

6. (lee1999cdc2activationin pages 3-4): Karen M. Lee, Julia E. Saiz, William A. Barton, and Robert P. Fisher. Cdc2 activation in fission yeast depends on mcs6 and csk1, two partially redundant cdk-activating kinases (caks). Current Biology, 9:441-444, Apr 1999. URL: https://doi.org/10.1016/s0960-9822(99)80194-8, doi:10.1016/s0960-9822(99)80194-8. This article has 98 citations and is from a highest quality peer-reviewed journal.

7. (lee1999cdc2activationin pages 2-3): Karen M. Lee, Julia E. Saiz, William A. Barton, and Robert P. Fisher. Cdc2 activation in fission yeast depends on mcs6 and csk1, two partially redundant cdk-activating kinases (caks). Current Biology, 9:441-444, Apr 1999. URL: https://doi.org/10.1016/s0960-9822(99)80194-8, doi:10.1016/s0960-9822(99)80194-8. This article has 98 citations and is from a highest quality peer-reviewed journal.

8. (hermand2001specificityofcdk pages 4-5): D. Hermand, T. Westerling, A. Pihlak, J. Thuret, T. Vallenius, M. Tiainen, J. Vandenhaute, G. Cottarel, C. Mann, and T. Mäkelä. Specificity of cdk activation in vivo by the two caks mcs6 and csk1 in fission yeast. The EMBO Journal, 20:82-90, Jan 2001. URL: https://doi.org/10.1093/emboj/20.1.82, doi:10.1093/emboj/20.1.82. This article has 46 citations.

9. (saiz2002acdkactivatingkinase pages 4-6): Julia E. Saiz and Robert P. Fisher. A cdk-activating kinase network is required in cell cycle control and transcription in fission yeast. Current Biology, 12:1100-1105, Jul 2002. URL: https://doi.org/10.1016/s0960-9822(02)00903-x, doi:10.1016/s0960-9822(02)00903-x. This article has 60 citations and is from a highest quality peer-reviewed journal.

10. (saiz2002acdkactivatingkinase pages 1-2): Julia E. Saiz and Robert P. Fisher. A cdk-activating kinase network is required in cell cycle control and transcription in fission yeast. Current Biology, 12:1100-1105, Jul 2002. URL: https://doi.org/10.1016/s0960-9822(02)00903-x, doi:10.1016/s0960-9822(02)00903-x. This article has 60 citations and is from a highest quality peer-reviewed journal.

11. (buck1995identificationofa pages 4-5): V. Buck, Paul Russell, and J. B. Millar. Identification of a cdk‐activating kinase in fission yeast. The EMBO Journal, 14:6173-6183, Dec 1995. URL: https://doi.org/10.1002/j.1460-2075.1995.tb00308.x, doi:10.1002/j.1460-2075.1995.tb00308.x. This article has 145 citations.

12. (lee2005impairmentofthe pages 3-5): Karen M. Lee, Ida Miklos, Hongyan Du, Stephen Watt, Zsolt Szilagyi, Julia E. Saiz, Ram Madabhushi, Christopher J. Penkett, Matthias Sipiczki, Jürg Bähler, and Robert P. Fisher. Impairment of the tfiih-associated cdk-activating kinase selectively affects cell cycle-regulated gene expression in fission yeast. Molecular biology of the cell, 16 6:2734-45, Jun 2005. URL: https://doi.org/10.1091/mbc.e04-11-0982, doi:10.1091/mbc.e04-11-0982. This article has 71 citations and is from a domain leading peer-reviewed journal.

13. (hermand2001specificityofcdk pages 2-3): D. Hermand, T. Westerling, A. Pihlak, J. Thuret, T. Vallenius, M. Tiainen, J. Vandenhaute, G. Cottarel, C. Mann, and T. Mäkelä. Specificity of cdk activation in vivo by the two caks mcs6 and csk1 in fission yeast. The EMBO Journal, 20:82-90, Jan 2001. URL: https://doi.org/10.1093/emboj/20.1.82, doi:10.1093/emboj/20.1.82. This article has 46 citations.

14. (hermand1998fissionyeastcsk1 pages 3-5): D. Hermand, A. Pihlak, T. Westerling, V. Damagnez, J. Vandenhaute, G. Cottarel, and T. Mäkelä. Fission yeast csk1 is a cak‐activating kinase (cakak). The EMBO Journal, 17:7230-7238, Dec 1998. URL: https://doi.org/10.1093/emboj/17.24.7230, doi:10.1093/emboj/17.24.7230. This article has 90 citations.

15. (hermand1998fissionyeastcsk1 pages 2-3): D. Hermand, A. Pihlak, T. Westerling, V. Damagnez, J. Vandenhaute, G. Cottarel, and T. Mäkelä. Fission yeast csk1 is a cak‐activating kinase (cakak). The EMBO Journal, 17:7230-7238, Dec 1998. URL: https://doi.org/10.1093/emboj/17.24.7230, doi:10.1093/emboj/17.24.7230. This article has 90 citations.

16. (hermand1998fissionyeastcsk1 pages 6-7): D. Hermand, A. Pihlak, T. Westerling, V. Damagnez, J. Vandenhaute, G. Cottarel, and T. Mäkelä. Fission yeast csk1 is a cak‐activating kinase (cakak). The EMBO Journal, 17:7230-7238, Dec 1998. URL: https://doi.org/10.1093/emboj/17.24.7230, doi:10.1093/emboj/17.24.7230. This article has 90 citations.

17. (lee2005impairmentofthe pages 8-9): Karen M. Lee, Ida Miklos, Hongyan Du, Stephen Watt, Zsolt Szilagyi, Julia E. Saiz, Ram Madabhushi, Christopher J. Penkett, Matthias Sipiczki, Jürg Bähler, and Robert P. Fisher. Impairment of the tfiih-associated cdk-activating kinase selectively affects cell cycle-regulated gene expression in fission yeast. Molecular biology of the cell, 16 6:2734-45, Jun 2005. URL: https://doi.org/10.1091/mbc.e04-11-0982, doi:10.1091/mbc.e04-11-0982. This article has 71 citations and is from a domain leading peer-reviewed journal.

18. (lee2005impairmentofthe pages 5-8): Karen M. Lee, Ida Miklos, Hongyan Du, Stephen Watt, Zsolt Szilagyi, Julia E. Saiz, Ram Madabhushi, Christopher J. Penkett, Matthias Sipiczki, Jürg Bähler, and Robert P. Fisher. Impairment of the tfiih-associated cdk-activating kinase selectively affects cell cycle-regulated gene expression in fission yeast. Molecular biology of the cell, 16 6:2734-45, Jun 2005. URL: https://doi.org/10.1091/mbc.e04-11-0982, doi:10.1091/mbc.e04-11-0982. This article has 71 citations and is from a domain leading peer-reviewed journal.

19. (lee2005impairmentofthe pages 9-10): Karen M. Lee, Ida Miklos, Hongyan Du, Stephen Watt, Zsolt Szilagyi, Julia E. Saiz, Ram Madabhushi, Christopher J. Penkett, Matthias Sipiczki, Jürg Bähler, and Robert P. Fisher. Impairment of the tfiih-associated cdk-activating kinase selectively affects cell cycle-regulated gene expression in fission yeast. Molecular biology of the cell, 16 6:2734-45, Jun 2005. URL: https://doi.org/10.1091/mbc.e04-11-0982, doi:10.1091/mbc.e04-11-0982. This article has 71 citations and is from a domain leading peer-reviewed journal.

20. (lee2005impairmentofthe pages 10-11): Karen M. Lee, Ida Miklos, Hongyan Du, Stephen Watt, Zsolt Szilagyi, Julia E. Saiz, Ram Madabhushi, Christopher J. Penkett, Matthias Sipiczki, Jürg Bähler, and Robert P. Fisher. Impairment of the tfiih-associated cdk-activating kinase selectively affects cell cycle-regulated gene expression in fission yeast. Molecular biology of the cell, 16 6:2734-45, Jun 2005. URL: https://doi.org/10.1091/mbc.e04-11-0982, doi:10.1091/mbc.e04-11-0982. This article has 71 citations and is from a domain leading peer-reviewed journal.

21. (yaguesanz2023chromatinremodelingby pages 3-4): Carlo Yague-Sanz, Valérie Migeot, Marc Larochelle, François Bachand, Maxime Wéry, Antonin Morillon, and Damien Hermand. Chromatin remodeling by pol ii primes efficient pol iii transcription. Nature Communications, Jun 2023. URL: https://doi.org/10.1038/s41467-023-39387-4, doi:10.1038/s41467-023-39387-4. This article has 26 citations and is from a highest quality peer-reviewed journal.

22. (duster2024structuralbasisof pages 8-10): Robert Düster, Kanchan Anand, Sophie C. Binder, Maximilian Schmitz, Karl Gatterdam, Robert P. Fisher, and Matthias Geyer. Structural basis of cdk7 activation by dual t-loop phosphorylation. Aug 2024. URL: https://doi.org/10.1038/s41467-024-50891-z, doi:10.1038/s41467-024-50891-z. This article has 30 citations and is from a highest quality peer-reviewed journal.

23. (duster2024structuralbasisof pages 2-3): Robert Düster, Kanchan Anand, Sophie C. Binder, Maximilian Schmitz, Karl Gatterdam, Robert P. Fisher, and Matthias Geyer. Structural basis of cdk7 activation by dual t-loop phosphorylation. Aug 2024. URL: https://doi.org/10.1038/s41467-024-50891-z, doi:10.1038/s41467-024-50891-z. This article has 30 citations and is from a highest quality peer-reviewed journal.

24. (duster2024structuralbasisof pages 1-2): Robert Düster, Kanchan Anand, Sophie C. Binder, Maximilian Schmitz, Karl Gatterdam, Robert P. Fisher, and Matthias Geyer. Structural basis of cdk7 activation by dual t-loop phosphorylation. Aug 2024. URL: https://doi.org/10.1038/s41467-024-50891-z, doi:10.1038/s41467-024-50891-z. This article has 30 citations and is from a highest quality peer-reviewed journal.

25. (parua2020dissectingthepol pages 3-4): Pabitra K. Parua and Robert P. Fisher. Dissecting the pol ii transcription cycle and derailing cancer with cdk inhibitors. Nature Chemical Biology, 16:716-724, Jun 2020. URL: https://doi.org/10.1038/s41589-020-0563-4, doi:10.1038/s41589-020-0563-4. This article has 124 citations and is from a highest quality peer-reviewed journal.

26. (lee1999cdc2activationin pages 4-4): Karen M. Lee, Julia E. Saiz, William A. Barton, and Robert P. Fisher. Cdc2 activation in fission yeast depends on mcs6 and csk1, two partially redundant cdk-activating kinases (caks). Current Biology, 9:441-444, Apr 1999. URL: https://doi.org/10.1016/s0960-9822(99)80194-8, doi:10.1016/s0960-9822(99)80194-8. This article has 98 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](mcs6-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. yaguesanz2023chromatinremodelingby pages 3-4
2. parua2020dissectingthepol pages 3-4
3. hermand2001specificityofcdk pages 1-2
4. saiz2002acdkactivatingkinase pages 3-4
5. lee2005impairmentofthe pages 1-2
6. buck1995identificationofa pages 2-3
7. buck1995identificationofa pages 1-2
8. hermand2001specificityofcdk pages 4-5
9. saiz2002acdkactivatingkinase pages 4-6
10. saiz2002acdkactivatingkinase pages 1-2
11. buck1995identificationofa pages 4-5
12. lee2005impairmentofthe pages 3-5
13. hermand2001specificityofcdk pages 2-3
14. lee2005impairmentofthe pages 8-9
15. lee2005impairmentofthe pages 5-8
16. lee2005impairmentofthe pages 9-10
17. lee2005impairmentofthe pages 10-11
18. duster2024structuralbasisof pages 8-10
19. duster2024structuralbasisof pages 2-3
20. duster2024structuralbasisof pages 1-2
21. DOI
22. https://doi.org/10.1002/j.1460-2075.1995.tb00308.x
23. https://doi.org/10.1093/emboj/20.1.82
24. https://doi.org/10.1091/mbc.e04-11-0982
25. https://doi.org/10.1016/S0960-9822(02
26. https://doi.org/10.1016/S0960-9822(99
27. https://doi.org/10.1093/emboj/17.24.7230
28. https://doi.org/10.1038/s41467-023-39387-4
29. https://doi.org/10.1038/s41467-024-50891-z
30. https://doi.org/10.1093/emboj/20.1.82,
31. https://doi.org/10.1016/s0960-9822(02
32. https://doi.org/10.1091/mbc.e04-11-0982,
33. https://doi.org/10.1002/j.1460-2075.1995.tb00308.x,
34. https://doi.org/10.1016/s0960-9822(99
35. https://doi.org/10.1093/emboj/17.24.7230,
36. https://doi.org/10.1038/s41467-023-39387-4,
37. https://doi.org/10.1038/s41467-024-50891-z,
38. https://doi.org/10.1038/s41589-020-0563-4,