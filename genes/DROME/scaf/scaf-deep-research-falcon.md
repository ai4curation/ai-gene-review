---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-10T14:51:05.371164'
end_time: '2026-09-10T14:59:42.396641'
duration_seconds: 517.03
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: DROME
  gene_id: scaf
  gene_symbol: scaf
  uniprot_accession: Q7K5M0
  protein_description: 'RecName: Full=Inactive serine protease scarface {ECO:0000303|PubMed:15342518,
    ECO:0000303|PubMed:20379222}; Flags: Precursor;'
  gene_info: Name=scaf {ECO:0000303|PubMed:20530545, ECO:0000312|FlyBase:FBgn0033033};
    Synonyms=scarf {ECO:0000303|PubMed:20379222}; ORFNames=CG11066 {ECO:0000312|FlyBase:FBgn0033033};
  organism_full: Drosophila melanogaster (Fruit fly).
  protein_family: Belongs to the peptidase S1 family. {ECO:0000255|PROSITE-
  protein_domains: CLIP_SPH_Scar. (IPR040973); Peptidase_S1_PA. (IPR009003); Peptidase_S1A.
    (IPR001314); Trypsin_dom. (IPR001254); CLIP_SPH_Scar (PF18399)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 18
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: scaf-deep-research-falcon_artifacts/artifact-00.md
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
- **UniProt Accession:** Q7K5M0
- **Protein Description:** RecName: Full=Inactive serine protease scarface {ECO:0000303|PubMed:15342518, ECO:0000303|PubMed:20379222}; Flags: Precursor;
- **Gene Information:** Name=scaf {ECO:0000303|PubMed:20530545, ECO:0000312|FlyBase:FBgn0033033}; Synonyms=scarf {ECO:0000303|PubMed:20379222}; ORFNames=CG11066 {ECO:0000312|FlyBase:FBgn0033033};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Belongs to the peptidase S1 family. {ECO:0000255|PROSITE-
- **Key Domains:** CLIP_SPH_Scar. (IPR040973); Peptidase_S1_PA. (IPR009003); Peptidase_S1A. (IPR001314); Trypsin_dom. (IPR001254); CLIP_SPH_Scar (PF18399)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "scaf" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'scaf' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **scaf** (gene ID: scaf, UniProt: Q7K5M0) in DROME.

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
- **UniProt Accession:** Q7K5M0
- **Protein Description:** RecName: Full=Inactive serine protease scarface {ECO:0000303|PubMed:15342518, ECO:0000303|PubMed:20379222}; Flags: Precursor;
- **Gene Information:** Name=scaf {ECO:0000303|PubMed:20530545, ECO:0000312|FlyBase:FBgn0033033}; Synonyms=scarf {ECO:0000303|PubMed:20379222}; ORFNames=CG11066 {ECO:0000312|FlyBase:FBgn0033033};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Belongs to the peptidase S1 family. {ECO:0000255|PROSITE-
- **Key Domains:** CLIP_SPH_Scar. (IPR040973); Peptidase_S1_PA. (IPR009003); Peptidase_S1A. (IPR001314); Trypsin_dom. (IPR001254); CLIP_SPH_Scar (PF18399)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "scaf" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'scaf' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **scaf** (gene ID: scaf, UniProt: Q7K5M0) in DROME.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Functional annotation report: *Drosophila melanogaster scarface* (*scaf*)

## Executive conclusion

The requested target is correctly identified as *Drosophila melanogaster scarface*—gene symbol *scaf*, synonym *scarf*, ORF CG11066, UniProt Q7K5M0. The focused literature consistently describes this product as a secreted, catalytically inactive serine-protease homolog involved in epithelial morphogenesis; it is not one of the unrelated genes denoted “SCAF” in other organisms. Its peptidase-S1/trypsin-like and CLIP-serine-protease-homolog annotations therefore agree with the literature, but indicate a **pseudoenzyme scaffold/regulator**, not a demonstrated proteolytic enzyme (srivastava2015regulationofa pages 1-2, sorrosal2010scarfaceasecreted pages 1-2).

The strongest functional interpretation is that Scarface acts outside the cell to coordinate basement-membrane organization and attenuate JNK signaling. It helps maintain polarized Laminin A localization, participates in a JNK-induced negative-feedback loop, and mediates EGFR–JNK crosstalk during epithelial closure. No intrinsic catalytic reaction, substrate specificity, or direct molecular binding partner has been established.

| Annotation aspect | Current conclusion | Principal experimental evidence | Confidence / limitations |
|---|---|---|---|
| Identity | The target is *Drosophila melanogaster* **scarface** (*scaf*; synonym *scarf*; CG11066), corresponding to UniProt Q7K5M0—not an unrelated SCAF-named gene. | Focused fly studies consistently describe Scarface as the same secreted serine-protease homolog and use *scaf/scarf* alleles, RNAi, and tagged protein reagents (srivastava2015regulationofa pages 2-3, sorrosal2010scarfaceasecreted pages 1-2, kushnir2017novelinterplaybetween pages 1-2). | **High.** Organism, names, molecular class, and developmental phenotypes agree across independent studies. |
| Molecular class and catalytic status | Secreted **inactive serine-protease homolog** of the trypsin/peptidase-S1 fold; it is best regarded as a regulatory pseudoenzyme rather than an active protease. | Literature reports substitutions in the canonical catalytic triad and lack of expected catalytic activity (srivastava2015regulationofa pages 1-2, sorrosal2010scarfaceasecreted pages 1-2). | **High for inactivity; moderate for structural mechanism.** Retrieved evidence does not specify every substituted residue or include kinetic assays. |
| Secretion and localization | Scarface enters the secretory pathway and acts extracellularly or through extracellular-matrix organization. Tagged protein occurs in the imaginal-disc hinge, peripodial stalk, and peripodial membrane; intracellular pools occur in endosomal compartments. | Scarf–Myc was examined in S2-cell lysates and conditioned medium; membrane-tethered Scarf-CD2–Myc and Rab5/Rab7/Rab11 colocalization addressed secretion and trafficking. Protein-trap GFP localized Scarface in thorax-forming disc regions (srivastava2015regulationofa pages 2-3, sorrosal2010scarfaceasecreted pages 6-7). | **High for secretion and tissue distribution; moderate for exact extracellular binding site.** Stable binding to a specific basement-membrane component is not established. |
| Basement membrane and Laminin A | Scarface is required for polarized Laminin A distribution, preventing inappropriate apical Laminin accumulation and supporting epithelial basement-membrane organization. | *scarf* loss-of-function embryos accumulate Laminin A at the apical epithelial surface before detectable loss of epithelial polarity; mutant cells can form an apical basement-membrane-like cap (sorrosal2010scarfaceasecreted pages 1-2, sorrosal2010scarfaceasecreted pages 6-7). | **High for the Laminin-localization phenotype; moderate for mechanism.** Proposed roles in trafficking, transcytosis, or facilitation of another protease cascade remain unproven. |
| JNK feedback | *scaf* is induced by JNK, while its secreted product antagonizes JNK-pathway output, forming a negative-feedback loop during epithelial morphogenesis. | Reduced JNKK/Hemipterous activity lowers Scarface-reporter expression, whereas induced dTAK1/JNK activation drives expression. Scaf overexpression reduces *dpp* and pMad; loss of *scaf* expands both outputs (srivastava2015regulationofa pages 3-5, kushnir2017novelinterplaybetween pages 8-11, kushnir2017novelinterplaybetween pages 11-13). | **High for the pathway relationship.** The direct extracellular target through which Scaf attenuates JNK remains unidentified. |
| EGFR crosstalk | EGFR–Ras signaling in lateral epidermis represses *scaf*, preventing excessive secreted Scaf from suppressing JNK in neighboring leading-edge cells. | Reduced EGFR signaling through *rhomboid* or *spi* mutation, EgfrDN, or RasDN expands *scaf* expression; RasV12 reduces it. In *rhomboid; scaf* double mutants, pMad resembles the expanded *scaf*-mutant state, placing *scaf* downstream of EGFR in this assay (kushnir2017novelinterplaybetween pages 8-11, kushnir2017novelinterplaybetween pages 11-13, kushnir2017novelinterplaybetween pages 6-8). | **High for genetic ordering and non-cell-autonomous regulation.** The proposed Yan–Engrailed transcriptional relay and extracellular target are not fully resolved. |
| Embryonic dorsal closure | Scarface tunes JNK–Dpp signaling and matrix polarity required for coordinated epithelial-sheet migration and closure. Both deficiency and ectopic excess disturb pathway balance. | *scarf/scaf* mutants exhibit germ-band-retraction and dorsal-closure defects, abnormal Laminin A localization, expanded *dpp*/pMad, and phenotypes consistent with JNK overactivity; excessive Scaf suppresses *dpp*/pMad and can impede closure (sorrosal2010scarfaceasecreted pages 1-2, kushnir2017novelinterplaybetween pages 11-13, kushnir2017novelinterplaybetween pages 1-2). | **High for developmental requirement; moderate for a unified molecular mechanism.** Signaling feedback and matrix organization may be connected but have not been linked biochemically. |
| Thoracic closure | Scarface is a JNK-regulated effector required in imaginal-disc and peripodial tissues for adult thorax closure and normal bristle patterning. | Scarface RNAi driven by Ap-Gal4 causes a mild thoracic cleft and bristle loss; Pnr-Gal4 produces a stronger cleft. Ubiquitous knockdown causes pupal lethality and scarring; JNK activation induces Scarface in wing, leg, and haltere discs (srivastava2015regulationofa pages 3-5, srivastava2015regulationofa pages 2-3, srivastava2015regulationofa pages 5-7). | **Moderate to high.** Genetic evidence is strong, but no direct molecular substrate or quantitative biomechanical measurement was reported. |
| Substrate and reaction | **No catalyzed reaction or substrate specificity is established.** Scarface is catalytically inactive and should not be assigned trypsin-like hydrolysis solely from its S1 domain. | Catalytic-triad substitutions and pseudoenzyme classification argue against intrinsic proteolysis; models instead invoke protein interaction, extracellular signaling, trafficking, or regulation of another protease cascade (srivastava2015regulationofa pages 1-2, sorrosal2010scarfaceasecreted pages 6-7, kushnir2017novelinterplaybetween pages 11-13). | **High that no enzymatic reaction is demonstrated; low for the identity of its direct molecular partner.** |
| Recent 2023–2024 evidence | No focused 2023–2024 mechanistic study of Q7K5M0/*scaf* was identified in the retrieved literature. The latest direct study retrieved was published in 2017. | Available focused studies center on 2010 embryonic morphogenesis and Laminin polarity, 2015 thoracic development, and 2017 EGFR–JNK crosstalk (sorrosal2010scarfaceasecreted pages 1-2, srivastava2015regulationofa pages 1-2, kushnir2017novelinterplaybetween pages 8-11). | **Evidence gap.** Absence from this search does not prove that no expression-atlas or incidental dataset mentions *scaf*. |
| Applications | Current use is primarily as a **Drosophila research model** for epithelial closure, extracellular negative feedback, pseudoenzyme biology, basement-membrane polarity, and EGFR–JNK crosstalk; no clinical, diagnostic, agricultural, or biotechnology implementation is established. | Protein-trap, RNAi, mutant, overexpression, epistasis, secretion, and imaging reagents have been applied to developmental-signaling and tissue-morphogenesis experiments (srivastava2015regulationofa pages 3-5, kushnir2017novelinterplaybetween pages 8-11, sorrosal2010scarfaceasecreted pages 6-7). | **High for research utility; no evidence for deployed real-world applications.** Translational parallels to wound healing or tumor invasion remain conceptual. |


*Table: Evidence-weighted summary for Drosophila Scarface (scaf/scarf; CG11066; Q7K5M0), distinguishing demonstrated functions from mechanistic inference and unresolved questions.*

## 1. Identity and domain verification

### Required identity checks

1. **Symbol and description:** The literature uses *scarface*, *scaf*, or *scarf* for a secreted serine-protease-like protein. Genetic studies employ *scaf/scarf* mutants, RNAi, protein-trap alleles, and tagged Scarface constructs with mutually consistent developmental phenotypes (srivastava2015regulationofa pages 2-3, sorrosal2010scarfaceasecreted pages 1-2, sorrosal2010scarfaceasecreted pages 6-7).
2. **Organism:** All focused evidence summarized here concerns the fruit fly, *D. melanogaster*.
3. **Family/domain agreement:** The reported trypsin-like serine-protease-homolog character is consistent with UniProt Q7K5M0’s peptidase S1A/trypsin and CLIP-SPH domain assignments. Scarface has substitutions in the canonical catalytic triad and is described as catalytically inactive (srivastava2015regulationofa pages 1-2).
4. **Ambiguity exclusion:** No evidence concerning human SCAF RNA-processing factors or unrelated similarly named proteins was used.

Thus, the identification is secure. Nevertheless, the exact altered catalytic-triad residues were not specified in the retrieved full-text evidence and should not be inferred without direct sequence inspection.

## 2. Molecular function

### 2.1 Scarface is a protease homolog, not a validated enzyme

Although Scarface contains a peptidase-S1/trypsin-like fold, available evidence supports classification as an **inactive serine-protease homolog**. Consequently, no EC reaction should be assigned, and there is no demonstrated peptide substrate, cleavage-site preference, turnover number, or inhibitor profile. Calling Scarface a “protease” without the qualifier *inactive homolog* would overstate current knowledge (srivastava2015regulationofa pages 1-2, sorrosal2010scarfaceasecreted pages 1-2).

The most plausible pseudoenzyme functions proposed by investigators are protein–protein interaction, regulation of an extracellular protease cascade, control of extracellular signaling, or regulation of basement-membrane trafficking. One model proposes that Scarface facilitates another serine-protease activity that removes ectopic apical Laminin A; this has not been established biochemically and Laminin A should not be described as a direct Scarface substrate (sorrosal2010scarfaceasecreted pages 6-7, kushnir2017novelinterplaybetween pages 11-13).

### 2.2 Primary functional role: extracellular regulation of epithelial organization

Loss of *scarf* causes abnormal Laminin A accumulation at the apical epithelial surface before detectable loss of epithelial polarity. Mutant cells may develop an apical basement-membrane-like cap, supporting a role in polarized Laminin delivery, retention, or turnover rather than general epithelial destruction. The best-supported structural function is therefore maintenance of correct basement-membrane protein distribution and cell–matrix organization during morphogenetic movement (sorrosal2010scarfaceasecreted pages 1-2, sorrosal2010scarfaceasecreted pages 6-7).

Published May 2010, Sorrosal et al., “Scarface, a secreted serine protease-like protein, regulates polarized localization of laminin A at the basement membrane of the Drosophila embryo,” *EMBO Reports* 11:373–379, DOI/URL: https://doi.org/10.1038/embor.2010.43 (sorrosal2010scarfaceasecreted pages 1-2).

## 3. Localization and site of action

Scarface contains a signal sequence and was experimentally detected using tagged Scarf–Myc in S2-cell conditioned medium, supporting secretion. Experiments with membrane-tethered Scarf-CD2–Myc and comparison with Rab5-, Rab7-, and Rab11-associated compartments further indicate secretory/endosomal trafficking (srivastava2015regulationofa pages 1-2, sorrosal2010scarfaceasecreted pages 6-7).

In larval imaginal discs, Scarface protein-trap GFP occurs in the wing-disc hinge, peripodial stalk, and peripodial membrane. In peripodial cells, the reporter is predominantly cytoplasmic and excluded from nuclei, consistent with production and trafficking through the secretory system. These tissues contribute to adult thorax formation (srivastava2015regulationofa pages 3-5, srivastava2015regulationofa pages 2-3).

The functional site is consequently inferred to be the **extracellular epithelial environment and basement-membrane interface**. However, stable binding of Scarface to Laminin, a particular receptor, or another matrix component has not been demonstrated.

## 4. Signaling pathways

### 4.1 JNK negative feedback

Scarface is both a transcriptional output and an antagonist of JNK signaling. Impairing the Drosophila JNKK Hemipterous diminishes or eliminates Scarface-reporter expression in the peripodial stalk. Conversely, temporally activating the pathway with dTAK1 induces robust Scarface expression in wing, leg, and haltere imaginal discs. These experiments support necessity and sufficiency of JNK activity for *scaf* expression in the tested developmental contexts (srivastava2015regulationofa pages 3-5, srivastava2015regulationofa pages 5-7).

In embryonic epithelia, excess Scarface reduces transcription of the JNK target *decapentaplegic* (*dpp*) and decreases phosphorylated Mad, whereas *scaf* loss expands *dpp* expression and pMad. Scarface therefore limits JNK-dependent Dpp output, forming extracellular negative feedback rather than directly dephosphorylating JNK as the intracellular phosphatase Puckered does (kushnir2017novelinterplaybetween pages 8-11, kushnir2017novelinterplaybetween pages 11-13, kushnir2017novelinterplaybetween pages 1-2).

Rousset et al. described this relationship explicitly as a negative-feedback loop during epithelial morphogenesis: *Development* 137:2177–2186, July 2010, DOI/URL: https://doi.org/10.1242/dev.050781 (srivastava2015regulationofa pages 7-7).

### 4.2 EGFR–Scarface–JNK crosstalk

During embryonic dorsal closure, EGFR–Ras signaling in lateral epidermal cells represses *scaf*. Reduced EGFR activity through *rhomboid* or *spitz* mutation, dominant-negative EGFR, or dominant-negative Ras expands *scaf* expression ventrally. Constitutively active Ras has the converse effect and reduces *scaf* expression (kushnir2017novelinterplaybetween pages 8-11, kushnir2017novelinterplaybetween pages 6-8).

This regulation is functionally non-cell-autonomous: EGFR activity prevents lateral epidermal cells from producing excessive secreted Scarface, thereby allowing strong JNK activity in neighboring leading-edge cells. In *rhomboid; scaf* double mutants, pMad resembles the expanded domain of *scaf* single mutants, placing *scaf* genetically downstream of EGFR for this output. Evidence further suggests a Yan/Engrailed-dependent transcriptional relay, although its detailed molecular implementation remains incomplete (kushnir2017novelinterplaybetween pages 11-13, kushnir2017novelinterplaybetween pages 8-11).

Published June 19, 2017, Kushnir et al., “Novel interplay between JNK and EGFR signaling in Drosophila dorsal closure,” *PLOS Genetics* 13:e1006860, DOI/URL: https://doi.org/10.1371/journal.pgen.1006860 (kushnir2017novelinterplaybetween pages 8-11).

## 5. Biological processes and phenotypes

### Embryonic morphogenesis

*scarf* loss-of-function embryos display germ-band-retraction and dorsal-closure defects alongside mislocalized Laminin A. Signaling assays show excessive or spatially expanded JNK–Dpp output in *scaf* mutants, whereas ectopic Scarface suppresses *dpp* and pMad. Normal closure therefore requires an appropriate Scarface dosage: too little weakens negative feedback and matrix polarity, while too much suppresses JNK-dependent morphogenesis (sorrosal2010scarfaceasecreted pages 1-2, kushnir2017novelinterplaybetween pages 11-13).

### Adult thorax closure

In larval thorax-forming tissues, *scaf* knockdown driven by Ap-Gal4 causes a mild adult thoracic cleft and medio-lateral bristle loss; Pnr-Gal4 knockdown produces a more severe cleft. Ubiquitous RNAi causes pupal lethality and a scarring phenotype. These observations support a requirement for Scarface in epithelial movement and cell–matrix interactions during thoracic closure (srivastava2015regulationofa pages 2-3, srivastava2015regulationofa pages 5-7).

Published February 2015, Srivastava and Dong, “Regulation of a serine protease homolog by the JNK pathway during thoracic development of Drosophila melanogaster,” *FEBS Open Bio* 5:117–123, DOI/URL: https://doi.org/10.1016/j.fob.2015.01.008 (srivastava2015regulationofa pages 1-2, srivastava2015regulationofa pages 3-5).

## 6. Evidence quality and quantitative information

The functional annotation rests on complementary evidence: loss-of-function mutants, tissue-specific RNAi, overexpression, pathway activation/inhibition, genetic epistasis, protein traps, conditioned-medium secretion assays, immunostaining, and basement-membrane imaging. Agreement among these approaches makes the assignments of secretion, JNK feedback, matrix regulation, and epithelial-closure function relatively strong.

The focused papers are primarily qualitative or spatial. Reported comparative findings include mild versus severe thoracic clefts under different drivers, expansion or reduction of *scaf*, *dpp*, and pMad domains, pupal lethality after ubiquitous knockdown, and apical Laminin accumulation in mutants. The retrieved evidence did not supply reliable numerical penetrance, effect sizes, protein concentrations, binding constants, or enzymatic kinetic values; none should be fabricated or inferred (srivastava2015regulationofa pages 2-3, kushnir2017novelinterplaybetween pages 8-11, sorrosal2010scarfaceasecreted pages 6-7).

## 7. Recent research and applications

A targeted search did not identify a focused 2023–2024 mechanistic publication on Q7K5M0/*scaf*. The latest directly focused mechanistic study retrieved was the 2017 EGFR–JNK work; the core molecular literature dates from 2010–2017. This is an important evidence gap rather than evidence that the annotation has been superseded.

Scarface currently has no established clinical, diagnostic, agricultural, or biotechnology implementation. Its real-world use is as an experimental Drosophila model for:

- extracellular control of JNK signaling;
- EGFR–JNK pathway crosstalk;
- epithelial sheet closure and wound-healing-like morphogenesis;
- polarized basement-membrane assembly;
- regulatory functions acquired by catalytically inactive protease homologs.

Potential relevance to wound repair, tissue regeneration, and tumor invasion is conceptual because these processes share JNK signaling and matrix-remodeling principles. Direct conservation of Scarface’s mechanism or a translational intervention based on it has not been demonstrated.

## 8. Final annotation

**Recommended primary-function annotation:** *Scarface is a secreted, catalytically inactive CLIP-domain serine-protease homolog that regulates epithelial morphogenesis by maintaining polarized Laminin A/basement-membrane organization and by negatively modulating JNK–Dpp signaling. During dorsal closure, EGFR–Ras signaling restricts* scaf *expression in lateral epidermis, permitting appropriate JNK activity in leading-edge cells; Scarface is also a JNK-induced effector required for imaginal-disc-derived thoracic closure.*

**Reaction/substrate:** none established. Scarface should be annotated as a regulatory pseudoenzyme, not assigned a trypsin-like catalytic reaction. The identity of its direct extracellular target, receptor, binding partner, or regulated protease remains the principal unresolved mechanistic question.

References

1. (srivastava2015regulationofa pages 1-2): Ajay Srivastava and Qian Dong. Regulation of a serine protease homolog by the jnk pathway during thoracic development of drosophila melanogaster. FEBS Open Bio, 5:117-123, Feb 2015. URL: https://doi.org/10.1016/j.fob.2015.01.008, doi:10.1016/j.fob.2015.01.008. This article has 11 citations and is from a peer-reviewed journal.

2. (sorrosal2010scarfaceasecreted pages 1-2): Georgina Sorrosal, Lidia Pérez, Héctor Herranz, and Marco Milán. Scarface, a secreted serine protease‐like protein, regulates polarized localization of laminin a at the basement membrane of the drosophila embryo. EMBO reports, 11:373-379, May 2010. URL: https://doi.org/10.1038/embor.2010.43, doi:10.1038/embor.2010.43. This article has 31 citations and is from a highest quality peer-reviewed journal.

3. (srivastava2015regulationofa pages 2-3): Ajay Srivastava and Qian Dong. Regulation of a serine protease homolog by the jnk pathway during thoracic development of drosophila melanogaster. FEBS Open Bio, 5:117-123, Feb 2015. URL: https://doi.org/10.1016/j.fob.2015.01.008, doi:10.1016/j.fob.2015.01.008. This article has 11 citations and is from a peer-reviewed journal.

4. (kushnir2017novelinterplaybetween pages 1-2): Tatyana Kushnir, Sharon Mezuman, Shaked Bar-Cohen, Rotem Lange, Ze'ev Paroush, and Aharon Helman. Novel interplay between jnk and egfr signaling in drosophila dorsal closure. Jun 2017. URL: https://doi.org/10.1371/journal.pgen.1006860, doi:10.1371/journal.pgen.1006860. This article has 18 citations and is from a domain leading peer-reviewed journal.

5. (sorrosal2010scarfaceasecreted pages 6-7): Georgina Sorrosal, Lidia Pérez, Héctor Herranz, and Marco Milán. Scarface, a secreted serine protease‐like protein, regulates polarized localization of laminin a at the basement membrane of the drosophila embryo. EMBO reports, 11:373-379, May 2010. URL: https://doi.org/10.1038/embor.2010.43, doi:10.1038/embor.2010.43. This article has 31 citations and is from a highest quality peer-reviewed journal.

6. (srivastava2015regulationofa pages 3-5): Ajay Srivastava and Qian Dong. Regulation of a serine protease homolog by the jnk pathway during thoracic development of drosophila melanogaster. FEBS Open Bio, 5:117-123, Feb 2015. URL: https://doi.org/10.1016/j.fob.2015.01.008, doi:10.1016/j.fob.2015.01.008. This article has 11 citations and is from a peer-reviewed journal.

7. (kushnir2017novelinterplaybetween pages 8-11): Tatyana Kushnir, Sharon Mezuman, Shaked Bar-Cohen, Rotem Lange, Ze'ev Paroush, and Aharon Helman. Novel interplay between jnk and egfr signaling in drosophila dorsal closure. Jun 2017. URL: https://doi.org/10.1371/journal.pgen.1006860, doi:10.1371/journal.pgen.1006860. This article has 18 citations and is from a domain leading peer-reviewed journal.

8. (kushnir2017novelinterplaybetween pages 11-13): Tatyana Kushnir, Sharon Mezuman, Shaked Bar-Cohen, Rotem Lange, Ze'ev Paroush, and Aharon Helman. Novel interplay between jnk and egfr signaling in drosophila dorsal closure. Jun 2017. URL: https://doi.org/10.1371/journal.pgen.1006860, doi:10.1371/journal.pgen.1006860. This article has 18 citations and is from a domain leading peer-reviewed journal.

9. (kushnir2017novelinterplaybetween pages 6-8): Tatyana Kushnir, Sharon Mezuman, Shaked Bar-Cohen, Rotem Lange, Ze'ev Paroush, and Aharon Helman. Novel interplay between jnk and egfr signaling in drosophila dorsal closure. Jun 2017. URL: https://doi.org/10.1371/journal.pgen.1006860, doi:10.1371/journal.pgen.1006860. This article has 18 citations and is from a domain leading peer-reviewed journal.

10. (srivastava2015regulationofa pages 5-7): Ajay Srivastava and Qian Dong. Regulation of a serine protease homolog by the jnk pathway during thoracic development of drosophila melanogaster. FEBS Open Bio, 5:117-123, Feb 2015. URL: https://doi.org/10.1016/j.fob.2015.01.008, doi:10.1016/j.fob.2015.01.008. This article has 11 citations and is from a peer-reviewed journal.

11. (srivastava2015regulationofa pages 7-7): Ajay Srivastava and Qian Dong. Regulation of a serine protease homolog by the jnk pathway during thoracic development of drosophila melanogaster. FEBS Open Bio, 5:117-123, Feb 2015. URL: https://doi.org/10.1016/j.fob.2015.01.008, doi:10.1016/j.fob.2015.01.008. This article has 11 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](scaf-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. srivastava2015regulationofa pages 1-2
2. sorrosal2010scarfaceasecreted pages 1-2
3. srivastava2015regulationofa pages 7-7
4. kushnir2017novelinterplaybetween pages 8-11
5. srivastava2015regulationofa pages 2-3
6. kushnir2017novelinterplaybetween pages 1-2
7. sorrosal2010scarfaceasecreted pages 6-7
8. srivastava2015regulationofa pages 3-5
9. kushnir2017novelinterplaybetween pages 11-13
10. kushnir2017novelinterplaybetween pages 6-8
11. srivastava2015regulationofa pages 5-7
12. https://doi.org/10.1038/embor.2010.43
13. https://doi.org/10.1242/dev.050781
14. https://doi.org/10.1371/journal.pgen.1006860
15. https://doi.org/10.1016/j.fob.2015.01.008
16. https://doi.org/10.1016/j.fob.2015.01.008,
17. https://doi.org/10.1038/embor.2010.43,
18. https://doi.org/10.1371/journal.pgen.1006860,