---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-28T21:28:22.440651'
end_time: '2026-06-28T21:43:17.710262'
duration_seconds: 895.27
template_file: templates/interpro_family_research.md
template_variables:
  interpro_id: PTHR24418
  interpro_name: Non-receptor tyrosine kinases involved in cell signaling
  interpro_short_name: Non-receptor_tyrosine_kinases
  interpro_type: family
  interpro_integrated: IPR050198
  member_databases: Not specified
  n_proteins: '45131'
  n_taxa: '5684'
  n_subfamilies: '76'
  interpro2go_terms: None mapped (no InterPro2GO terms for this entry)
  interpro_description: This family of proteins includes non-receptor tyrosine kinases
    that play crucial roles in various cellular processes. They are involved in signal
    transduction pathways that regulate immune responses, cell growth, survival, differentiation,
    cytoskeletal remodeling, cell adhesion, and migration. These proteins are activated
    by cell surface receptors and are essential for both innate and adaptive immunity.
    They also participate in the regulation of B-cell and T-cell receptor signaling,
    contributing to the development and function of lymphocytes. Additionally, they
    mediate responses to growth factors, cytokines, and environmental stresses, influencing
    processes like platelet activation, vascular development, and osteoclast maturation.
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 22
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: PTHR24418-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: PTHR24418-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
---

## Question

# InterPro Family Research for GO Annotation Review

## ⚠️ CRITICAL: Family Identification Context

**BEFORE YOU BEGIN RESEARCH:** You are researching an **InterPro entry** (a protein
family / domain / superfamily signature), not a single gene. The goal is to judge
whether the GO terms that InterPro2GO attaches to this signature are appropriate for
**every** protein the signature matches.

### Target InterPro Entry (from the InterPro API):
- **Accession:** PTHR24418
- **Name:** Non-receptor tyrosine kinases involved in cell signaling
- **Short name:** Non-receptor_tyrosine_kinases
- **Entry type:** family
- **Integrated into / parent:** IPR050198
- **Member database signatures:** Not specified
- **Scale:** 45131 proteins across 5684 taxa, 76 subfamilies
- **Current InterPro2GO terms (the mappings under review):** None mapped (no InterPro2GO terms for this entry)
- **InterPro description:** This family of proteins includes non-receptor tyrosine kinases that play crucial roles in various cellular processes. They are involved in signal transduction pathways that regulate immune responses, cell growth, survival, differentiation, cytoskeletal remodeling, cell adhesion, and migration. These proteins are activated by cell surface receptors and are essential for both innate and adaptive immunity. They also participate in the regulation of B-cell and T-cell receptor signaling, contributing to the development and function of lymphocytes. Additionally, they mediate responses to growth factors, cytokines, and environmental stresses, influencing processes like platelet activation, vascular development, and osteoclast maturation.

### Why entry type matters:

An entry of type **domain**, **repeat**, or **homologous_superfamily** identifies a
structural/functional *module*, not a whole-protein function. GO terms describing a
whole-protein activity or process attached to such a module systematically over-annotate
every protein that merely *contains* the module. An entry of type **family** is more
likely to support whole-protein function terms, but only if the family is functionally
homogeneous.

## Research Target

Provide a comprehensive, citation-backed research report on the InterPro entry
**PTHR24418 (Non-receptor tyrosine kinases involved in cell signaling)**, structured to support GO annotation review.

Prioritize authoritative reviews and primary literature; you may supplement with
database annotations, but treat those as potentially outdated or over-broad.

Address each of the following:

1. **Family definition and biochemistry.** What does this family/domain do
   mechanistically? What fold is it? What are the conserved catalytic or binding
   residues? Cite primary/structural literature for all claims.

2. **InterPro2GO mapping appropriateness.** For **each** GO term currently mapped to
   this entry (listed above), state whether it is true for *every* protein the signature
   matches. Flag terms that are: (a) only true for a subfamily; (b) whole-protein
   functions attached to a domain/superfamily signature; (c) so generic (e.g. "ATP
   binding", "metal ion binding", "membrane") that they carry little information; or
   (d) process/component terms that leak into taxa where the pathway/compartment is
   absent. Where a more specific GO term would be correct, name it.

3. **Functional divergence across the family.** Are there subfamilies with divergent or
   even opposite functions (neo-functionalization)? Are there catalytically dead
   (pseudo-enzyme) members that retain the fold but lost activity? Identify the
   subfamilies and what distinguishes them.

4. **Taxonomic scope.** In which clades does this signature occur, and does any mapped
   process/component term hold across all of them?

5. **Over-annotation verdict.** Summarize whether InterPro2GO for this entry is sound,
   partially over-broad, or over-annotating, and give the recommended GO action pattern
   (ACCEPT / MODIFY-to-specific / KEEP_AS_NON_CORE / MARK_AS_OVER_ANNOTATED / REMOVE)
   for genes matching it. Note any recommendation for InterPro itself (e.g. demote a
   whole-protein term on a domain entry, or move it to a child entry).

Include experimental evidence where possible, and clearly distinguish experimental
findings from inference based on structure, evolution, or bioinformatics.


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

# InterPro Family Research for GO Annotation Review

## ⚠️ CRITICAL: Family Identification Context

**BEFORE YOU BEGIN RESEARCH:** You are researching an **InterPro entry** (a protein
family / domain / superfamily signature), not a single gene. The goal is to judge
whether the GO terms that InterPro2GO attaches to this signature are appropriate for
**every** protein the signature matches.

### Target InterPro Entry (from the InterPro API):
- **Accession:** PTHR24418
- **Name:** Non-receptor tyrosine kinases involved in cell signaling
- **Short name:** Non-receptor_tyrosine_kinases
- **Entry type:** family
- **Integrated into / parent:** IPR050198
- **Member database signatures:** Not specified
- **Scale:** 45131 proteins across 5684 taxa, 76 subfamilies
- **Current InterPro2GO terms (the mappings under review):** None mapped (no InterPro2GO terms for this entry)
- **InterPro description:** This family of proteins includes non-receptor tyrosine kinases that play crucial roles in various cellular processes. They are involved in signal transduction pathways that regulate immune responses, cell growth, survival, differentiation, cytoskeletal remodeling, cell adhesion, and migration. These proteins are activated by cell surface receptors and are essential for both innate and adaptive immunity. They also participate in the regulation of B-cell and T-cell receptor signaling, contributing to the development and function of lymphocytes. Additionally, they mediate responses to growth factors, cytokines, and environmental stresses, influencing processes like platelet activation, vascular development, and osteoclast maturation.

### Why entry type matters:

An entry of type **domain**, **repeat**, or **homologous_superfamily** identifies a
structural/functional *module*, not a whole-protein function. GO terms describing a
whole-protein activity or process attached to such a module systematically over-annotate
every protein that merely *contains* the module. An entry of type **family** is more
likely to support whole-protein function terms, but only if the family is functionally
homogeneous.

## Research Target

Provide a comprehensive, citation-backed research report on the InterPro entry
**PTHR24418 (Non-receptor tyrosine kinases involved in cell signaling)**, structured to support GO annotation review.

Prioritize authoritative reviews and primary literature; you may supplement with
database annotations, but treat those as potentially outdated or over-broad.

Address each of the following:

1. **Family definition and biochemistry.** What does this family/domain do
   mechanistically? What fold is it? What are the conserved catalytic or binding
   residues? Cite primary/structural literature for all claims.

2. **InterPro2GO mapping appropriateness.** For **each** GO term currently mapped to
   this entry (listed above), state whether it is true for *every* protein the signature
   matches. Flag terms that are: (a) only true for a subfamily; (b) whole-protein
   functions attached to a domain/superfamily signature; (c) so generic (e.g. "ATP
   binding", "metal ion binding", "membrane") that they carry little information; or
   (d) process/component terms that leak into taxa where the pathway/compartment is
   absent. Where a more specific GO term would be correct, name it.

3. **Functional divergence across the family.** Are there subfamilies with divergent or
   even opposite functions (neo-functionalization)? Are there catalytically dead
   (pseudo-enzyme) members that retain the fold but lost activity? Identify the
   subfamilies and what distinguishes them.

4. **Taxonomic scope.** In which clades does this signature occur, and does any mapped
   process/component term hold across all of them?

5. **Over-annotation verdict.** Summarize whether InterPro2GO for this entry is sound,
   partially over-broad, or over-annotating, and give the recommended GO action pattern
   (ACCEPT / MODIFY-to-specific / KEEP_AS_NON_CORE / MARK_AS_OVER_ANNOTATED / REMOVE)
   for genes matching it. Note any recommendation for InterPro itself (e.g. demote a
   whole-protein term on a domain entry, or move it to a child entry).

Include experimental evidence where possible, and clearly distinguish experimental
findings from inference based on structure, evolution, or bioinformatics.


# Comprehensive Research Report: PTHR24418 — Non-Receptor Tyrosine Kinases Involved in Cell Signaling

## InterPro2GO Annotation Review for PTHR24418

---

## 1. Family Definition and Biochemistry

### 1.1 Scope of PTHR24418

PTHR24418 is a PANTHER family-level entry corresponding to the broad grouping of non-receptor tyrosine kinases (NRTKs) involved in cell signaling. It encompasses 45,131 proteins across 5,684 taxa, organized into 76 subfamilies. This entry is integrated into IPR050198 and is specifically referenced by name in the recent Feuermann et al. (2025) *Nature* publication describing PAN-GO evolutionary models of human gene functions, where it is cited as an example of a large, complex family requiring careful functional annotation (feuermann2025acompendiumof pages 4-5, feuermann2025acompendiumof pages 3-4).

In humans, PTHR24418 encompasses approximately 32 NRTKs distributed across at least 9–10 major subfamilies: **Src, JAK, Tec/BTK, Syk/ZAP70, FAK, Abl, CSK, Ack, Fes/Fer, and BRK/Frk** (eshaq2024nonreceptortyrosinekinases pages 2-4).

### 1.2 Kinase Domain Fold and Conserved Residues

All NRTKs share the canonical eukaryotic protein kinase (ePK) catalytic domain fold, consisting of a smaller N-terminal lobe (primarily β-sheets) responsible for ATP binding, and a larger C-terminal lobe (primarily α-helices) that serves as the substrate-binding platform (eshaq2024nonreceptortyrosinekinases pages 2-4). The activation loop, containing Tyr, Ser, or Thr residues, undergoes phosphorylation via autophosphorylation or trans-phosphorylation by other kinases, correlating with catalytic activation (eshaq2024nonreceptortyrosinekinases pages 2-4).

Conserved catalytic residues include: the invariant lysine contacting ATP phosphate groups (e.g., Lys295 in c-Src, Lys262 in FRK, Lys219 in BRK), the DFG motif aspartate coordinating Mg²⁺ for phosphotransfer, and the catalytic loop aspartate serving as the catalytic base (eshaq2024nonreceptortyrosinekinases pages 12-14, eshaq2024nonreceptortyrosinekinases pages 2-4). Regulatory tyrosines in the activation loop (e.g., Tyr419 in c-Src, Tyr342 in BRK, Tyr387 in FRK) are critical for modulating kinase activity (eshaq2024nonreceptortyrosinekinases pages 12-14).

### 1.3 Domain Architecture Diversity

Despite sharing the kinase catalytic domain, the NRTKs within PTHR24418 exhibit strikingly divergent domain architectures:

- **Src family**: SH4–unique–SH3–SH2–SH1(kinase)–C-terminal regulatory tail (eshaq2024nonreceptortyrosinekinases pages 9-12)
- **JAK family**: FERM(JH5-JH7)–SH2-like(JH3-JH4)–pseudokinase(JH2)–kinase(JH1) (eshaq2024nonreceptortyrosinekinases pages 7-9, eshaq2024nonreceptortyrosinekinases pages 5-7)
- **Tec/BTK**: PH–TH–SH3–SH2–kinase (eshaq2024nonreceptortyrosinekinases pages 9-12)
- **Syk/ZAP70**: tandem SH2–kinase (eshaq2024nonreceptortyrosinekinases pages 14-16)
- **FAK**: FERM–kinase–FAT (eshaq2024nonreceptortyrosinekinases pages 7-9)
- **Abl**: SH3–SH2–kinase–actin-binding/DNA-binding C-terminus (eshaq2024nonreceptortyrosinekinases pages 12-14, eshaq2024nonreceptortyrosinekinases pages 14-16)
- **Ack**: SAM–kinase–SH3–CRIB–UBA (eshaq2024nonreceptortyrosinekinases pages 2-4)
- **Fes/Fer**: F-BAR–coiled-coil–SH2–kinase (eshaq2024nonreceptortyrosinekinases pages 7-9)
- **BRK/Frk**: SH3–SH2–kinase with nuclear localization signals (eshaq2024nonreceptortyrosinekinases pages 12-14)

---

## 2. InterPro2GO Mapping Appropriateness

PTHR24418 currently has **no InterPro2GO terms mapped**, which is the configuration under review. The following table evaluates candidate GO terms that could theoretically be applied and assesses their appropriateness for universal application across all 45,131 matched proteins:

| GO Term | GO ID | Applies to all members? | Issues/Exceptions | Recommendation |
|---|---|---|---|---|
| protein tyrosine kinase activity | GO:0004713 | No | Most NRTK subfamilies share a conserved catalytic tyrosine kinase domain, but the family is highly diverse and JAK proteins contain a catalytically inactive regulatory pseudokinase domain (JH2); family-wide mapping risks conflating active kinase domains with regulatory kinase-like regions and may not be safe for every protein matched by this broad family signature (eshaq2024nonreceptortyrosinekinases pages 2-4, moncivais2023structuralanalysisof pages 16-17, eshaq2024nonreceptortyrosinekinases pages 5-7) | **Do not map at this parent family level**; if used, move to more specific catalytic child families only |
| ATP binding | GO:0005524 | No / not safely | ATP binding is expected for many active kinase domains, but it is a very generic term with limited informational value; some kinase-like/pseudokinase regions can retain or alter nucleotide binding without canonical catalysis, so universal family-level assignment is not robust (paul2020genome‐wideandstructural pages 9-10, eshaq2024nonreceptortyrosinekinases pages 2-4) | **Do not map**; too generic and potentially misleading |
| protein phosphorylation | GO:0006468 | No | This is a biological process term describing a downstream process rather than a molecular activity; broad family membership does not guarantee all matched proteins participate in the same process in the same way across taxa, and some NRTKs also act through kinase-independent mechanisms (eshaq2024nonreceptortyrosinekinases pages 1-2) | **Do not map** at this family level |
| signal transduction | GO:0007165 | Broadly yes, but too unspecific for GO family mapping | Nearly all NRTKs participate in signaling, but this term is extremely broad and not informative; the family spans many distinct pathways, receptors, and cellular contexts, so the term adds little value and obscures functional divergence (eshaq2024nonreceptortyrosinekinases pages 2-4, feuermann2025acompendiumof pages 4-5) | **KEEP_AS_NON_CORE / generally avoid mapping** |
| cytoplasm | GO:0005737 | No | Many NRTKs are cytoplasmic, but several shuttle to the nucleus or localize to membranes, adhesion complexes, receptor-associated compartments, or other subcellular structures depending on subfamily and state; broad family-level CC mapping would overgeneralize localization (eshaq2024nonreceptortyrosinekinases pages 2-4, eshaq2024nonreceptortyrosinekinases pages 12-14, eshaq2024nonreceptortyrosinekinases pages 14-16) | **Do not map** |
| intracellular signal transduction | GO:0035556 | Broadly yes, but not ideal for all members | NRTKs are intracellular signaling enzymes or scaffolds, yet the family includes strong pathway and localization divergence and some members have specialized functions in adhesion, cytoskeletal remodeling, or cytokine receptor complexes; term remains broad and non-discriminating (eshaq2024nonreceptortyrosinekinases pages 2-4, eshaq2024nonreceptortyrosinekinases pages 9-12) | **KEEP_AS_NON_CORE / avoid at parent family** |
| immune system process | GO:0002376 | No | Immune roles are prominent for JAK, Tec/BTK, Syk/ZAP70, and some Src-family members, but many other subfamilies such as FAK, Abl, Ack, CSK, BRK/Frk, and Fes/Fer also function outside immunity; not universal across the family or taxa (eshaq2024nonreceptortyrosinekinases pages 7-9, eshaq2024nonreceptortyrosinekinases pages 14-16, eshaq2024nonreceptortyrosinekinases pages 9-12) | **REMOVE / map only to immune-specialized child families** |
| T cell receptor signaling pathway | GO:0050852 | No | Restricted to specialized lymphocyte signaling kinases such as LCK, ITK, and ZAP70-related modules; not applicable to most NRTK subfamilies and absent outside taxa with adaptive immunity (eshaq2024nonreceptortyrosinekinases pages 14-16, eshaq2024nonreceptortyrosinekinases pages 9-12) | **REMOVE / move to specific child families or subfamilies** |
| B cell receptor signaling pathway | GO:0050853 | No | Restricted mainly to BTK, SYK, BLK, LYN, and related B-cell signaling proteins; not universal for the broader NRTK family and taxonomically limited to vertebrate/adaptive immune contexts (eshaq2024nonreceptortyrosinekinases pages 14-16, eshaq2024nonreceptortyrosinekinases pages 9-12) | **REMOVE / move to specific child families or subfamilies** |
| cell adhesion | GO:0007155 | No | Strongly relevant to FAK/PYK2 and some Src/Abl signaling contexts, but not a universal function of JAK, Tec, Syk, Csk, Ack, or BRK/Frk families; this would over-annotate the majority of matches (eshaq2024nonreceptortyrosinekinases pages 7-9, eshaq2024nonreceptortyrosinekinases pages 9-12) | **REMOVE / map to FAK-related child entries only** |
| cytokine-mediated signaling pathway | GO:0019221 | No | Characteristic of JAK-family kinases associated with cytokine receptors, but not of Src, Abl, FAK, Csk, Ack, Syk, Tec, or BRK/Frk as a whole; would be a classic subfamily-specific over-annotation (eshaq2024nonreceptortyrosinekinases pages 7-9, eshaq2024nonreceptortyrosinekinases pages 5-7) | **REMOVE / map to JAK-specific child entries only** |


*Table: This table evaluates whether plausible GO terms are appropriate for the broad PTHR24418 non-receptor tyrosine kinase family. It highlights where terms are too generic, subfamily-specific, or likely to cause over-annotation across this diverse family.*

**Summary of mapping assessment**: No candidate GO term—whether molecular function, biological process, or cellular component—can be safely applied to every protein matched by PTHR24418 without risk of systematic over-annotation. Even the most plausible candidate, "protein tyrosine kinase activity" (GO:0004713), fails because the JAK family members contain catalytically inactive pseudokinase domains (JH2) that retain the kinase fold but lack phosphotransfer activity (moncivais2023structuralanalysisof pages 16-17, eshaq2024nonreceptortyrosinekinases pages 5-7), and some NRTKs also function through kinase-independent mechanisms (eshaq2024nonreceptortyrosinekinases pages 1-2).

---

## 3. Functional Divergence Across the Family

### 3.1 Major Subfamilies and Their Distinct Functions

The following table provides a detailed comparison of all major NRTK subfamilies within PTHR24418:

| Subfamily | Members (human) | Domain Architecture | Primary Functions | Taxonomic Scope | GO Annotation Suitability for whole-family mapping |
|---|---|---|---|---|---|
| Src | SRC, FYN, YES1, LYN, LCK, HCK, FGR, BLK | SH4 lipid-modified N-terminus, unique region, SH3, SH2, SH1/TK catalytic domain, C-terminal regulatory tail Tyr (eshaq2024nonreceptortyrosinekinases pages 12-14, eshaq2024nonreceptortyrosinekinases pages 9-12) | Broad intracellular signaling downstream of adhesion receptors, immune receptors, growth factor pathways; regulates proliferation, migration, cytoskeletal remodeling, survival (eshaq2024nonreceptortyrosinekinases pages 9-12) | Ancient SrcM subgroup; premetazoan origin and conserved across choanoflagellates/filastereans and Metazoa (yeung2021evolutionoffunctional pages 3-6, yeung2021evolutionoffunctional pages 9-10) | Catalytic activity terms may fit most members, but process terms such as immune signaling, adhesion, migration, or oncogenic signaling are too broad for the whole subfamily; map only conservative kinase-function terms at child entries, not PTHR24418-wide |
| JAK | JAK1, JAK2, JAK3, TYK2 | FERM (JH5-JH7), SH2-like region (JH3-JH4), pseudokinase JH2, catalytic kinase JH1 (eshaq2024nonreceptortyrosinekinases pages 7-9) | Cytokine receptor-associated signaling; JAK-STAT activation; immune regulation, inflammation, hematopoiesis (eshaq2024nonreceptortyrosinekinases pages 7-9, moncivais2023structuralanalysisof pages 16-17, eshaq2024nonreceptortyrosinekinases pages 5-7) | Metazoan NRTKs; not a universal feature of all holozoan NRTKs; cytokine signaling role especially relevant in vertebrates (yeung2021evolutionoffunctional pages 3-6, yeung2021evolutionoffunctional pages 9-10) | Cytokine-mediated signaling and JAK-STAT terms are JAK-specific and must not be mapped to PTHR24418; pseudokinase domains also warn against naive catalytic generalization across all family architecture |
| Tec/BTK | BTK, ITK, TEC, BMX, TXK | PH, TH, SH3, SH2, SH1/TK catalytic domain (eshaq2024nonreceptortyrosinekinases pages 9-12) | Antigen receptor and phosphoinositide-dependent signaling, especially in lymphocytes; some broader cardiovascular and inflammatory roles (eshaq2024nonreceptortyrosinekinases pages 9-12) | Ancient architecture with premetazoan roots; expanded and specialized in metazoans, especially vertebrate immune systems (yeung2021evolutionoffunctional pages 3-6, yeung2021evolutionoffunctional pages 9-10) | B-cell/T-cell receptor signaling and immune system process are not suitable for PTHR24418-wide mapping; even within Tec, some roles are lineage- and tissue-specific |
| Syk/ZAP70 | SYK, ZAP70 | Tandem SH2 domains followed by catalytic kinase domain; cytosolic, lacking N-terminal acylation motifs (eshaq2024nonreceptortyrosinekinases pages 14-16) | ITAM-based immune receptor signaling, especially BCR/TCR and Fc receptor pathways (eshaq2024nonreceptortyrosinekinases pages 14-16) | Metazoan/vertebrate immune-specialized branch rather than pan-holozoan universal function (eshaq2024nonreceptortyrosinekinases pages 14-16, yeung2021evolutionoffunctional pages 9-10) | T-cell receptor signaling and B-cell receptor signaling are clearly child/subfamily-specific and inappropriate for PTHR24418 |
| FAK | PTK2/FAK, PTK2B/PYK2 | N-terminal FERM domain, kinase domain, C-terminal FAT region (eshaq2024nonreceptortyrosinekinases pages 7-9) | Integrin and adhesion signaling; focal adhesion dynamics, proliferation, survival, migration (eshaq2024nonreceptortyrosinekinases pages 7-9, eshaq2024nonreceptortyrosinekinases pages 9-12) | Metazoan cell-adhesion associated NRTKs; not universal to all NRTKs (eshaq2024nonreceptortyrosinekinases pages 7-9, yeung2021evolutionoffunctional pages 9-10) | Cell adhesion, focal adhesion, and integrin-related process terms are too specific for PTHR24418 and should stay on child entries only |
| Abl | ABL1, ABL2/ARG | SH3, SH2, kinase domain at N-terminus; C-terminal actin-binding/DNA-binding regions; differs from Src in C-terminal organization (eshaq2024nonreceptortyrosinekinases pages 12-14, eshaq2024nonreceptortyrosinekinases pages 14-16) | Cytoskeletal regulation, adhesion, migration, stress responses, DNA-damage-related signaling (eshaq2024nonreceptortyrosinekinases pages 12-14, eshaq2024nonreceptortyrosinekinases pages 14-16) | Abl architecture arose later than ancient premetazoan SrcM/Tec/Csk core, in metazoan evolution (yeung2021evolutionoffunctional pages 3-6) | DNA damage, actin organization, or adhesion-related GO terms would over-annotate PTHR24418; only conservative kinase-level terms might apply at Abl child level |
| CSK | CSK, CHK/MATK | SH3, SH2, kinase domain; lacks Src-family N-terminal unique region and C-terminal regulatory tail (eshaq2024nonreceptortyrosinekinases pages 9-12) | Negative regulation of Src-family kinases by inhibitory tail phosphorylation; regulatory rather than broad downstream signaling output (eshaq2024nonreceptortyrosinekinases pages 9-12) | Ancient Csk lineage conserved from premetazoans into Metazoa (yeung2021evolutionoffunctional pages 3-6, yeung2021evolutionoffunctional pages 9-10) | Illustrates opposite functional polarity inside PTHR24418: CSK inhibits Src-family signaling rather than acting like receptor-proximal effector kinases; therefore generic signaling-process GO terms are unsafe family-wide |
| Ack | TNK2/ACK1 (plus related ACK-family architecture in broader taxa) | Distinct NRTK architecture; kinase domain with C-terminal SH3, plus SAM, CRIB, UBA and other regulatory modules (eshaq2024nonreceptortyrosinekinases pages 2-4) | RTK/integrin downstream signaling, EGFR regulation, trafficking, growth control, epigenetic and scaffold-like roles (eshaq2024nonreceptortyrosinekinases pages 2-4) | Distinct but evolutionarily ancient NRTK architecture relative to other holozoan kinases; not representative of all NRTKs (eshaq2024nonreceptortyrosinekinases pages 2-4, yeung2021evolutionoffunctional pages 3-6) | Ack-specific trafficking/EGFR/efferocytosis-related annotations would be over-broad on PTHR24418; unusual domain architecture also argues against single whole-family process mapping |
| Fes/Fer | FES, FER | F-BAR domain, coiled-coils, SH2, C-terminal kinase domain (eshaq2024nonreceptortyrosinekinases pages 7-9) | Cytokine and cytoskeletal signaling, vesicle/membrane-associated regulation, differentiation and migration-related outputs (eshaq2024nonreceptortyrosinekinases pages 7-9) | Metazoan NRTK branch; not universal across all PTHR24418 matches (eshaq2024nonreceptortyrosinekinases pages 7-9, yeung2021evolutionoffunctional pages 9-10) | Membrane remodeling, cytokine-response, or migration terms are not safe for whole-family mapping; subfamily-specific annotation only |
| BRK/Frk | PTK6/BRK, FRK, SRMS | SH3, SH2, kinase domain; most lack N-myristoylation; NLS within SH2 enables nuclear localization (eshaq2024nonreceptortyrosinekinases pages 12-14) | Epithelial and nuclear signaling, proliferation/differentiation control; some scaffold and noncanonical localization-dependent roles (eshaq2024nonreceptortyrosinekinases pages 12-14) | Specialized metazoan branch, not ancient universal NRTK core (eshaq2024nonreceptortyrosinekinases pages 12-14, yeung2021evolutionoffunctional pages 9-10) | Nuclear localization, epithelial signaling, or cancer-associated process terms are not appropriate for PTHR24418-wide mapping |
| Family-wide implication for PTHR24418 | 32 human NRTKs in ~9-10 groups; InterPro entry spans 45,131 proteins, 5,684 taxa, 76 subfamilies | Shared eukaryotic tyrosine kinase catalytic core, but major divergence in accessory domains and regulation; some families include pseudokinase modules (JAK JH2) and kinase-independent signaling roles (eshaq2024nonreceptortyrosinekinases pages 2-4, moncivais2023structuralanalysisof pages 16-17, eshaq2024nonreceptortyrosinekinases pages 1-2) | Collective label “cell signaling” is accurate only at very high level; concrete pathways differ sharply among subfamilies (immune, adhesion, cytokine, cytoskeleton, nuclear, negative regulation) (eshaq2024nonreceptortyrosinekinases pages 9-12, eshaq2024nonreceptortyrosinekinases pages 2-4) | Core tyrosine kinase machinery predates animals for SrcM/Tec/Csk/IRKL, whereas many specific pathway functions emerged later in metazoans/vertebrates (yeung2021evolutionoffunctional pages 3-6, yeung2021evolutionoffunctional pages 9-10, feuermann2025acompendiumof pages 4-5, feuermann2025acompendiumof pages 5-6) | Best practice is no broad process/component InterPro2GO mapping at this parent family; if any GO is added, it should be extremely conservative and preferably moved to child families with demonstrated functional homogeneity |


*Table: This table summarizes the main non-receptor tyrosine kinase subfamilies contained within PTHR24418, highlighting their divergent architectures, functions, and evolutionary scope. It is useful for judging whether any GO term could safely be applied across the entire InterPro family without over-annotation.*

### 3.2 Key Examples of Functional Divergence

The functional divergence across PTHR24418 subfamilies is extreme and well-documented:

- **JAK family** (JAK1, JAK2, JAK3, TYK2) specializes in cytokine receptor-associated signaling via the JAK-STAT pathway, regulating immune responses, hematopoiesis, and inflammation. JAK family members are unique among NRTKs in possessing a catalytically inactive pseudokinase domain (JH2) that serves as a regulatory module suppressing basal kinase activity and enabling cytokine-inducible activation (moncivais2023structuralanalysisof pages 16-17, eshaq2024nonreceptortyrosinekinases pages 5-7, riegel2022recentadvancesin pages 15-15).

- **CSK family** performs the functionally *opposite* role to Src-family kinases: CSK phosphorylates the inhibitory C-terminal tyrosine of Src-family members, thereby *negatively* regulating their activity (eshaq2024nonreceptortyrosinekinases pages 9-12). This represents a clear case where even within the same parent family, members can have antagonistic signaling functions.

- **FAK family** is specialized for integrin-mediated cell adhesion and focal adhesion signaling, promoting cell proliferation, angiogenesis, and survival through Grb2/Ras/MAPK and PI3K/Akt pathways (eshaq2024nonreceptortyrosinekinases pages 7-9, eshaq2024nonreceptortyrosinekinases pages 9-12). These adhesion-specific functions are not shared by immune-specialized NRTKs.

- **BRK/Frk family** members uniquely possess nuclear localization signals (NLS) within their SH2 domains and can shuttle to the nucleus, enabling nuclear signaling functions distinct from the cytoplasmic roles of most other NRTKs (eshaq2024nonreceptortyrosinekinases pages 12-14).

### 3.3 Pseudokinase and Catalytically Dead Members

The JAK family is the most prominent example of pseudokinase domains within PTHR24418. All four JAK members (JAK1, JAK2, JAK3, TYK2) contain a JH2 pseudokinase domain that retains the kinase fold but lacks full catalytic activity (paul2020genome‐wideandstructural pages 9-10, moncivais2023structuralanalysisof pages 16-17, eshaq2024nonreceptortyrosinekinases pages 5-7). This pseudokinase domain is essential for regulatory functions: it is required for suppressing basal catalytic activity and for proper cytokine-inducible signal transduction activation (moncivais2023structuralanalysisof pages 16-17, riegel2022recentadvancesin pages 15-15). ATP binding to the JH2 domain of JAK2 is critical for pathogenic activation, demonstrating that these domains retain nucleotide-binding capacity without conventional catalysis (moncivais2023structuralanalysisof pages 16-17, grant2023jak1pseudokinasev666g pages 53-57).

Additionally, broader studies of the kinome have identified pseudokinases such as MLKL, ILK, EphA10, and EphB6 as examples of kinase-fold proteins that have lost catalytic activity (paul2020genome‐wideandstructural pages 9-10), though not all of these fall within PTHR24418.

---

## 4. Taxonomic Scope

### 4.1 Evolutionary Origin

PTHR24418 spans 5,684 taxa, indicating broad distribution across Metazoa and potentially extending to unicellular holozoans. Evolutionary analysis by Yeung et al. (2021) demonstrated that tyrosine kinase expansion is strongly correlated with the emergence of multicellularity (yeung2021evolutionoffunctional pages 3-6, yeung2021evolutionoffunctional pages 9-10). The oldest NRTK families—SrcM (including Src-related kinases), Tec, Csk, and IRKL—originated in pre-metazoan unicellular organisms, with representatives detectable in choanoflagellates and filastereans (yeung2021evolutionoffunctional pages 3-6, yeung2021evolutionoffunctional pages 9-10). These ancient NRTKs share the SH3-SH2-kinase domain architecture and were likely co-opted for complex multicellular functions during animal evolution (yeung2021evolutionoffunctional pages 3-6).

### 4.2 Lineage-Specific Expansion

While the core tyrosine kinase machinery predates animals, many specific signaling functions evolved later through lineage-specific duplications and neofunctionalization (yeung2021evolutionoffunctional pages 9-10, yeung2021evolutionoffunctional pages 14-15). Additional tyrosine kinase families emerged during metazoan diversification, coinciding with the evolution of the nervous system, circulatory system, and adaptive immunity (yeung2021evolutionoffunctional pages 9-10). The Feuermann et al. (2025) PAN-GO study provides evidence that more than half of human protein-coding genes have inherited functional characteristics from distant single-celled ancestors, but many functions underwent subsequent modification (feuermann2025acompendiumof pages 4-5, feuermann2025acompendiumof pages 5-6).

### 4.3 Implications for GO Term Taxonomic Validity

Process-level GO terms related to adaptive immunity (T cell receptor signaling, B cell receptor signaling) are only meaningful in jawed vertebrates possessing adaptive immune systems. Cytokine-mediated signaling pathway terms are primarily relevant in metazoans with organized cytokine networks. Cell adhesion signaling via FAK-type kinases is metazoan-specific. Thus, any process GO term mapped to PTHR24418 would inevitably "leak" into taxa where the corresponding pathway or cellular compartment is absent (yeung2021evolutionoffunctional pages 3-6, yeung2021evolutionoffunctional pages 9-10).

---

## 5. Over-Annotation Verdict

### 5.1 Assessment of Current Status

The current state of PTHR24418—**no InterPro2GO terms mapped**—is **appropriate and should be maintained**. This is a well-justified decision for a family of this scale and diversity, consistent with best practices for GO annotation quality.

### 5.2 Rationale

1. **Extreme functional heterogeneity**: The family encompasses 9–10 major subfamilies with fundamentally different biological roles spanning immune signaling, cell adhesion, cytoskeletal remodeling, cytokine responses, transcriptional regulation, and negative regulation of kinase activity (eshaq2024nonreceptortyrosinekinases pages 2-4, eshaq2024nonreceptortyrosinekinases pages 9-12).

2. **Pseudokinase members**: The presence of catalytically inactive pseudokinase domains (JAK JH2) within the family means that even "protein tyrosine kinase activity" (GO:0004713) cannot be safely universalized (moncivais2023structuralanalysisof pages 16-17, eshaq2024nonreceptortyrosinekinases pages 5-7).

3. **Taxonomic breadth**: Spanning 5,684 taxa from unicellular holozoans to vertebrates, process-level terms that are vertebrate-specific (e.g., adaptive immunity) would systematically over-annotate non-vertebrate members (yeung2021evolutionoffunctional pages 3-6, yeung2021evolutionoffunctional pages 9-10).

4. **Functional opposition within the family**: CSK negatively regulates Src-family kinases, meaning that generic "signal transduction" or "positive regulation" terms would misrepresent the function of a significant subfamily (eshaq2024nonreceptortyrosinekinases pages 9-12).

5. **Kinase-independent functions**: NRTKs also operate through kinase-independent scaffolding and regulatory mechanisms, further complicating catalytic-activity-based GO term assignments (eshaq2024nonreceptortyrosinekinases pages 1-2).

### 5.3 Recommended GO Action Pattern

| Recommendation | Details |
|---|---|
| **Overall verdict** | Current no-mapping status is **SOUND** — **ACCEPT (no change needed)** |
| **Molecular Function terms** | Do NOT add GO:0004713 (protein tyrosine kinase activity) or GO:0005524 (ATP binding) at this parent level; these should be mapped at more specific child family entries where catalytic activity is universal |
| **Biological Process terms** | Do NOT add any process terms (signal transduction, immune system process, etc.) at this level; all are subfamily-specific |
| **Cellular Component terms** | Do NOT add any component terms; localization varies across subfamilies |
| **InterPro recommendation** | GO annotations should be pushed to the 76 child subfamilies of PTHR24418 where functional homogeneity can be verified. The PANTHER/InterPro architecture of this entry already recognizes this diversity through its subfamily structure |
| **For individual genes** | Genes matching PTHR24418 should receive GO annotations only through subfamily-level InterPro entries or through direct experimental annotation, not through this parent family |

### 5.4 Conclusion

PTHR24418 represents a textbook case of a functionally heterogeneous protein family where the absence of InterPro2GO mappings is the correct approach. The family's 76 subfamilies with radically different domain architectures, biological pathways, and taxonomic distributions make it impossible to assign any GO term—even the most generic—without risk of systematic over-annotation. The Feuermann et al. (2025) PAN-GO initiative explicitly recognized this family as requiring careful subfamily-level functional modeling rather than whole-family GO term propagation (feuermann2025acompendiumof pages 4-5, feuermann2025acompendiumof pages 3-4). All GO annotations for members of this family should be handled at the subfamily level or through direct experimental evidence.

References

1. (feuermann2025acompendiumof pages 4-5): Marc Feuermann, Huaiyu Mi, Pascale Gaudet, Anushya Muruganujan, Suzanna E. Lewis, Dustin Ebert, Tremayne Mushayahama, Suzanne A. Aleksander, James Balhoff, Seth Carbon, J. Michael Cherry, Harold J. Drabkin, Nomi L. Harris, David P. Hill, Raymond Lee, Colin Logie, Sierra Moxon, Christopher J. Mungall, Paul W. Sternberg, Kimberly Van Auken, Jolene Ramsey, Deborah A. Siegele, Rex L. Chisholm, Petra Fey, Michelle Giglio, Suvarna Nadendla, Giulia Antonazzo, Helen Attrill, Nicholas H. Brown, Phani V. Garapati, Steven Marygold, Saadullah H. Ahmed, Praoparn Asanitthong, Diana Luna Buitrago, Meltem N. Erdol, Matthew C. Gage, Siyao Huang, Mohamed Ali Kadhum, Kan Yan Chloe Li, Miao Long, Aleksandra Michalak, Angeline Pesala, Armalya Pritazahra, Shirin C. C. Saverimuttu, Renzhi Su, Qianhan Xu, Ruth C. Lovering, Judith Blake, Karen Christie, Lori Corbani, Mary E. Dolan, Li Ni, Dmitry Sitnikov, Cynthia Smith, Manuel Lera-Ramirez, Kim Rutherford, Valerie Wood, Peter D’Eustachio, Wendy M. Demos, Jeffrey L. De Pons, Melinda R. Dwinell, G. Thomas Hayman, Mary L. Kaldunski, Anne E. Kwitek, Stanley J. F. Laulederkind, Jennifer R. Smith, Marek A. Tutaj, Mahima Vedi, Shur-Jen Wang, Stacia R. Engel, Kalpana Karra, Stuart R. Miyasato, Robert S. Nash, Marek S. Skrzypek, Shuai Weng, Edith D. Wong, Tilmann Achsel, Maria Andres-Alonso, Claudia Bagni, Àlex Bayés, Thomas Biederer, Nils Brose, John Jia En Chua, Marcelo P. Coba, L. Niels Cornelisse, Jaime de Juan-Sanz, Hana L. Goldschmidt, Eckart D. Gundelfinger, Richard L. Huganir, Cordelia Imig, Reinhard Jahn, Hwajin Jung, Pascal S. Kaeser, Eunjoon Kim, Frank Koopmans, Michael R. Kreutz, Noa Lipstein, Harold D. MacGillavry, Peter S. McPherson, Vincent O’Connor, Rainer Pielot, Timothy A. Ryan, Carlo Sala, Morgan Sheng, Karl-Heinz Smalla, A. B. Smit, Ruud F. Toonen, Jan R. T. van Weering, Matthijs Verhage, Chiara Verpelli, Erika Bakker, Tanya Z. Berardini, Leonore Reiser, Andrea Auchincloss, Kristian Axelsen, Ghislaine Argoud-Puy, Marie-Claude Blatter, Emmanuel Boutet, Lionel Breuza, Alan Bridge, Cristina Casals-Casas, Elisabeth Coudert, Anne Estreicher, Maria Livia Famiglietti, Arnaud Gos, Nadine Gruaz-Gumowski, Chantal Hulo, Nevila Hyka-Nouspikel, Florence Jungo, Philippe Le Mercier, Damien Lieberherr, Patrick Masson, Anne Morgat, Ivo Pedruzzi, Lucille Pourcel, Sylvain Poux, Catherine Rivoire, Shyamala Sundaram, Emily Bowler-Barnett, Hema Bye-A-Jee, Paul Denny, Alexandr Ignatchenko, Rizwan Ishtiaq, Antonia Lock, Yvonne Lussi, Michele Magrane, Maria J. Martin, Sandra Orchard, Pedro Raposo, Elena Speretta, Nidhi Tyagi, Kate Warner, Rossana Zaru, Juancarlos Chan, Stavros Diamantakis, Daniela Raciti, Malcolm Fisher, Christina James-Zorn, Virgilio Ponferrada, Aaron Zorn, Sridhar Ramachandran, Leyla Ruzicka, Monte Westerfield, and Paul D. Thomas. A compendium of human gene functions derived from evolutionary modelling. Nature, 640:146-154, Feb 2025. URL: https://doi.org/10.1038/s41586-025-08592-0, doi:10.1038/s41586-025-08592-0. This article has 40 citations and is from a highest quality peer-reviewed journal.

2. (feuermann2025acompendiumof pages 3-4): Marc Feuermann, Huaiyu Mi, Pascale Gaudet, Anushya Muruganujan, Suzanna E. Lewis, Dustin Ebert, Tremayne Mushayahama, Suzanne A. Aleksander, James Balhoff, Seth Carbon, J. Michael Cherry, Harold J. Drabkin, Nomi L. Harris, David P. Hill, Raymond Lee, Colin Logie, Sierra Moxon, Christopher J. Mungall, Paul W. Sternberg, Kimberly Van Auken, Jolene Ramsey, Deborah A. Siegele, Rex L. Chisholm, Petra Fey, Michelle Giglio, Suvarna Nadendla, Giulia Antonazzo, Helen Attrill, Nicholas H. Brown, Phani V. Garapati, Steven Marygold, Saadullah H. Ahmed, Praoparn Asanitthong, Diana Luna Buitrago, Meltem N. Erdol, Matthew C. Gage, Siyao Huang, Mohamed Ali Kadhum, Kan Yan Chloe Li, Miao Long, Aleksandra Michalak, Angeline Pesala, Armalya Pritazahra, Shirin C. C. Saverimuttu, Renzhi Su, Qianhan Xu, Ruth C. Lovering, Judith Blake, Karen Christie, Lori Corbani, Mary E. Dolan, Li Ni, Dmitry Sitnikov, Cynthia Smith, Manuel Lera-Ramirez, Kim Rutherford, Valerie Wood, Peter D’Eustachio, Wendy M. Demos, Jeffrey L. De Pons, Melinda R. Dwinell, G. Thomas Hayman, Mary L. Kaldunski, Anne E. Kwitek, Stanley J. F. Laulederkind, Jennifer R. Smith, Marek A. Tutaj, Mahima Vedi, Shur-Jen Wang, Stacia R. Engel, Kalpana Karra, Stuart R. Miyasato, Robert S. Nash, Marek S. Skrzypek, Shuai Weng, Edith D. Wong, Tilmann Achsel, Maria Andres-Alonso, Claudia Bagni, Àlex Bayés, Thomas Biederer, Nils Brose, John Jia En Chua, Marcelo P. Coba, L. Niels Cornelisse, Jaime de Juan-Sanz, Hana L. Goldschmidt, Eckart D. Gundelfinger, Richard L. Huganir, Cordelia Imig, Reinhard Jahn, Hwajin Jung, Pascal S. Kaeser, Eunjoon Kim, Frank Koopmans, Michael R. Kreutz, Noa Lipstein, Harold D. MacGillavry, Peter S. McPherson, Vincent O’Connor, Rainer Pielot, Timothy A. Ryan, Carlo Sala, Morgan Sheng, Karl-Heinz Smalla, A. B. Smit, Ruud F. Toonen, Jan R. T. van Weering, Matthijs Verhage, Chiara Verpelli, Erika Bakker, Tanya Z. Berardini, Leonore Reiser, Andrea Auchincloss, Kristian Axelsen, Ghislaine Argoud-Puy, Marie-Claude Blatter, Emmanuel Boutet, Lionel Breuza, Alan Bridge, Cristina Casals-Casas, Elisabeth Coudert, Anne Estreicher, Maria Livia Famiglietti, Arnaud Gos, Nadine Gruaz-Gumowski, Chantal Hulo, Nevila Hyka-Nouspikel, Florence Jungo, Philippe Le Mercier, Damien Lieberherr, Patrick Masson, Anne Morgat, Ivo Pedruzzi, Lucille Pourcel, Sylvain Poux, Catherine Rivoire, Shyamala Sundaram, Emily Bowler-Barnett, Hema Bye-A-Jee, Paul Denny, Alexandr Ignatchenko, Rizwan Ishtiaq, Antonia Lock, Yvonne Lussi, Michele Magrane, Maria J. Martin, Sandra Orchard, Pedro Raposo, Elena Speretta, Nidhi Tyagi, Kate Warner, Rossana Zaru, Juancarlos Chan, Stavros Diamantakis, Daniela Raciti, Malcolm Fisher, Christina James-Zorn, Virgilio Ponferrada, Aaron Zorn, Sridhar Ramachandran, Leyla Ruzicka, Monte Westerfield, and Paul D. Thomas. A compendium of human gene functions derived from evolutionary modelling. Nature, 640:146-154, Feb 2025. URL: https://doi.org/10.1038/s41586-025-08592-0, doi:10.1038/s41586-025-08592-0. This article has 40 citations and is from a highest quality peer-reviewed journal.

3. (eshaq2024nonreceptortyrosinekinases pages 2-4): Abdulaziz M. Eshaq, Thomas W. Flanagan, Sofie-Yasmin Hassan, Sara A. Al Asheikh, Waleed A. Al-Amoudi, Simeon Santourlidis, Sarah-Lilly Hassan, Maryam O. Alamodi, Marcelo L. Bendhack, Mohammed O. Alamodi, Youssef Haikel, Mossad Megahed, and Mohamed Hassan. Non-receptor tyrosine kinases: their structure and mechanistic role in tumor progression and resistance. Cancers, 16:2754, Aug 2024. URL: https://doi.org/10.3390/cancers16152754, doi:10.3390/cancers16152754. This article has 30 citations.

4. (eshaq2024nonreceptortyrosinekinases pages 12-14): Abdulaziz M. Eshaq, Thomas W. Flanagan, Sofie-Yasmin Hassan, Sara A. Al Asheikh, Waleed A. Al-Amoudi, Simeon Santourlidis, Sarah-Lilly Hassan, Maryam O. Alamodi, Marcelo L. Bendhack, Mohammed O. Alamodi, Youssef Haikel, Mossad Megahed, and Mohamed Hassan. Non-receptor tyrosine kinases: their structure and mechanistic role in tumor progression and resistance. Cancers, 16:2754, Aug 2024. URL: https://doi.org/10.3390/cancers16152754, doi:10.3390/cancers16152754. This article has 30 citations.

5. (eshaq2024nonreceptortyrosinekinases pages 9-12): Abdulaziz M. Eshaq, Thomas W. Flanagan, Sofie-Yasmin Hassan, Sara A. Al Asheikh, Waleed A. Al-Amoudi, Simeon Santourlidis, Sarah-Lilly Hassan, Maryam O. Alamodi, Marcelo L. Bendhack, Mohammed O. Alamodi, Youssef Haikel, Mossad Megahed, and Mohamed Hassan. Non-receptor tyrosine kinases: their structure and mechanistic role in tumor progression and resistance. Cancers, 16:2754, Aug 2024. URL: https://doi.org/10.3390/cancers16152754, doi:10.3390/cancers16152754. This article has 30 citations.

6. (eshaq2024nonreceptortyrosinekinases pages 7-9): Abdulaziz M. Eshaq, Thomas W. Flanagan, Sofie-Yasmin Hassan, Sara A. Al Asheikh, Waleed A. Al-Amoudi, Simeon Santourlidis, Sarah-Lilly Hassan, Maryam O. Alamodi, Marcelo L. Bendhack, Mohammed O. Alamodi, Youssef Haikel, Mossad Megahed, and Mohamed Hassan. Non-receptor tyrosine kinases: their structure and mechanistic role in tumor progression and resistance. Cancers, 16:2754, Aug 2024. URL: https://doi.org/10.3390/cancers16152754, doi:10.3390/cancers16152754. This article has 30 citations.

7. (eshaq2024nonreceptortyrosinekinases pages 5-7): Abdulaziz M. Eshaq, Thomas W. Flanagan, Sofie-Yasmin Hassan, Sara A. Al Asheikh, Waleed A. Al-Amoudi, Simeon Santourlidis, Sarah-Lilly Hassan, Maryam O. Alamodi, Marcelo L. Bendhack, Mohammed O. Alamodi, Youssef Haikel, Mossad Megahed, and Mohamed Hassan. Non-receptor tyrosine kinases: their structure and mechanistic role in tumor progression and resistance. Cancers, 16:2754, Aug 2024. URL: https://doi.org/10.3390/cancers16152754, doi:10.3390/cancers16152754. This article has 30 citations.

8. (eshaq2024nonreceptortyrosinekinases pages 14-16): Abdulaziz M. Eshaq, Thomas W. Flanagan, Sofie-Yasmin Hassan, Sara A. Al Asheikh, Waleed A. Al-Amoudi, Simeon Santourlidis, Sarah-Lilly Hassan, Maryam O. Alamodi, Marcelo L. Bendhack, Mohammed O. Alamodi, Youssef Haikel, Mossad Megahed, and Mohamed Hassan. Non-receptor tyrosine kinases: their structure and mechanistic role in tumor progression and resistance. Cancers, 16:2754, Aug 2024. URL: https://doi.org/10.3390/cancers16152754, doi:10.3390/cancers16152754. This article has 30 citations.

9. (moncivais2023structuralanalysisof pages 16-17): Omar J. Rodriguez Moncivais, Stephanie A. Chavez, Victor H. Estrada Jimenez, Shengjie Sun, Lin Li, Robert A. Kirken, and Georgialina Rodriguez. Structural analysis of janus tyrosine kinase variants in hematological malignancies: implications for drug development and opportunities for novel therapeutic strategies. International Journal of Molecular Sciences, 24:14573, Sep 2023. URL: https://doi.org/10.3390/ijms241914573, doi:10.3390/ijms241914573. This article has 8 citations.

10. (paul2020genome‐wideandstructural pages 9-10): Anindita Paul and Narayanaswamy Srinivasan. Genome‐wide and structural analyses of pseudokinases encoded in the genome of <scp><i>arabidopsis thaliana</i></scp> provide functional insights. Aug 2020. URL: https://doi.org/10.1002/prot.25981, doi:10.1002/prot.25981. This article has 16 citations.

11. (eshaq2024nonreceptortyrosinekinases pages 1-2): Abdulaziz M. Eshaq, Thomas W. Flanagan, Sofie-Yasmin Hassan, Sara A. Al Asheikh, Waleed A. Al-Amoudi, Simeon Santourlidis, Sarah-Lilly Hassan, Maryam O. Alamodi, Marcelo L. Bendhack, Mohammed O. Alamodi, Youssef Haikel, Mossad Megahed, and Mohamed Hassan. Non-receptor tyrosine kinases: their structure and mechanistic role in tumor progression and resistance. Cancers, 16:2754, Aug 2024. URL: https://doi.org/10.3390/cancers16152754, doi:10.3390/cancers16152754. This article has 30 citations.

12. (yeung2021evolutionoffunctional pages 3-6): Wayland Yeung, Annie Kwon, Rahil Taujale, Claire Bunn, Aarya Venkat, and Natarajan Kannan. Evolution of functional diversity in the holozoan tyrosine kinome. Molecular Biology and Evolution, 38:5625-5639, Aug 2021. URL: https://doi.org/10.1093/molbev/msab272, doi:10.1093/molbev/msab272. This article has 21 citations and is from a highest quality peer-reviewed journal.

13. (yeung2021evolutionoffunctional pages 9-10): Wayland Yeung, Annie Kwon, Rahil Taujale, Claire Bunn, Aarya Venkat, and Natarajan Kannan. Evolution of functional diversity in the holozoan tyrosine kinome. Molecular Biology and Evolution, 38:5625-5639, Aug 2021. URL: https://doi.org/10.1093/molbev/msab272, doi:10.1093/molbev/msab272. This article has 21 citations and is from a highest quality peer-reviewed journal.

14. (feuermann2025acompendiumof pages 5-6): Marc Feuermann, Huaiyu Mi, Pascale Gaudet, Anushya Muruganujan, Suzanna E. Lewis, Dustin Ebert, Tremayne Mushayahama, Suzanne A. Aleksander, James Balhoff, Seth Carbon, J. Michael Cherry, Harold J. Drabkin, Nomi L. Harris, David P. Hill, Raymond Lee, Colin Logie, Sierra Moxon, Christopher J. Mungall, Paul W. Sternberg, Kimberly Van Auken, Jolene Ramsey, Deborah A. Siegele, Rex L. Chisholm, Petra Fey, Michelle Giglio, Suvarna Nadendla, Giulia Antonazzo, Helen Attrill, Nicholas H. Brown, Phani V. Garapati, Steven Marygold, Saadullah H. Ahmed, Praoparn Asanitthong, Diana Luna Buitrago, Meltem N. Erdol, Matthew C. Gage, Siyao Huang, Mohamed Ali Kadhum, Kan Yan Chloe Li, Miao Long, Aleksandra Michalak, Angeline Pesala, Armalya Pritazahra, Shirin C. C. Saverimuttu, Renzhi Su, Qianhan Xu, Ruth C. Lovering, Judith Blake, Karen Christie, Lori Corbani, Mary E. Dolan, Li Ni, Dmitry Sitnikov, Cynthia Smith, Manuel Lera-Ramirez, Kim Rutherford, Valerie Wood, Peter D’Eustachio, Wendy M. Demos, Jeffrey L. De Pons, Melinda R. Dwinell, G. Thomas Hayman, Mary L. Kaldunski, Anne E. Kwitek, Stanley J. F. Laulederkind, Jennifer R. Smith, Marek A. Tutaj, Mahima Vedi, Shur-Jen Wang, Stacia R. Engel, Kalpana Karra, Stuart R. Miyasato, Robert S. Nash, Marek S. Skrzypek, Shuai Weng, Edith D. Wong, Tilmann Achsel, Maria Andres-Alonso, Claudia Bagni, Àlex Bayés, Thomas Biederer, Nils Brose, John Jia En Chua, Marcelo P. Coba, L. Niels Cornelisse, Jaime de Juan-Sanz, Hana L. Goldschmidt, Eckart D. Gundelfinger, Richard L. Huganir, Cordelia Imig, Reinhard Jahn, Hwajin Jung, Pascal S. Kaeser, Eunjoon Kim, Frank Koopmans, Michael R. Kreutz, Noa Lipstein, Harold D. MacGillavry, Peter S. McPherson, Vincent O’Connor, Rainer Pielot, Timothy A. Ryan, Carlo Sala, Morgan Sheng, Karl-Heinz Smalla, A. B. Smit, Ruud F. Toonen, Jan R. T. van Weering, Matthijs Verhage, Chiara Verpelli, Erika Bakker, Tanya Z. Berardini, Leonore Reiser, Andrea Auchincloss, Kristian Axelsen, Ghislaine Argoud-Puy, Marie-Claude Blatter, Emmanuel Boutet, Lionel Breuza, Alan Bridge, Cristina Casals-Casas, Elisabeth Coudert, Anne Estreicher, Maria Livia Famiglietti, Arnaud Gos, Nadine Gruaz-Gumowski, Chantal Hulo, Nevila Hyka-Nouspikel, Florence Jungo, Philippe Le Mercier, Damien Lieberherr, Patrick Masson, Anne Morgat, Ivo Pedruzzi, Lucille Pourcel, Sylvain Poux, Catherine Rivoire, Shyamala Sundaram, Emily Bowler-Barnett, Hema Bye-A-Jee, Paul Denny, Alexandr Ignatchenko, Rizwan Ishtiaq, Antonia Lock, Yvonne Lussi, Michele Magrane, Maria J. Martin, Sandra Orchard, Pedro Raposo, Elena Speretta, Nidhi Tyagi, Kate Warner, Rossana Zaru, Juancarlos Chan, Stavros Diamantakis, Daniela Raciti, Malcolm Fisher, Christina James-Zorn, Virgilio Ponferrada, Aaron Zorn, Sridhar Ramachandran, Leyla Ruzicka, Monte Westerfield, and Paul D. Thomas. A compendium of human gene functions derived from evolutionary modelling. Nature, 640:146-154, Feb 2025. URL: https://doi.org/10.1038/s41586-025-08592-0, doi:10.1038/s41586-025-08592-0. This article has 40 citations and is from a highest quality peer-reviewed journal.

15. (riegel2022recentadvancesin pages 15-15): Kristina Riegel, Parthiban Vijayarangakannan, Petros Kechagioglou, Katarzyna Bogucka, and Krishnaraj Rajalingam. Recent advances in targeting protein kinases and pseudokinases in cancer biology. Frontiers in Cell and Developmental Biology, Jul 2022. URL: https://doi.org/10.3389/fcell.2022.942500, doi:10.3389/fcell.2022.942500. This article has 30 citations.

16. (grant2023jak1pseudokinasev666g pages 53-57): Alice H. Grant, Alejandro C. Rodriguez, Omar J. Rodriguez Moncivais, Shengjie Sun, Lin Li, Jonathon E. Mohl, Ming-Ying Leung, Robert A. Kirken, and Georgialina Rodriguez. Jak1 pseudokinase v666g mutant dominantly impairs jak3 phosphorylation and il-2 signaling. International Journal of Molecular Sciences, 24:6805, Apr 2023. URL: https://doi.org/10.3390/ijms24076805, doi:10.3390/ijms24076805. This article has 10 citations.

17. (yeung2021evolutionoffunctional pages 14-15): Wayland Yeung, Annie Kwon, Rahil Taujale, Claire Bunn, Aarya Venkat, and Natarajan Kannan. Evolution of functional diversity in the holozoan tyrosine kinome. Molecular Biology and Evolution, 38:5625-5639, Aug 2021. URL: https://doi.org/10.1093/molbev/msab272, doi:10.1093/molbev/msab272. This article has 21 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](PTHR24418-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](PTHR24418-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. eshaq2024nonreceptortyrosinekinases pages 2-4
2. eshaq2024nonreceptortyrosinekinases pages 12-14
3. eshaq2024nonreceptortyrosinekinases pages 9-12
4. eshaq2024nonreceptortyrosinekinases pages 14-16
5. eshaq2024nonreceptortyrosinekinases pages 7-9
6. eshaq2024nonreceptortyrosinekinases pages 1-2
7. yeung2021evolutionoffunctional pages 3-6
8. yeung2021evolutionoffunctional pages 9-10
9. feuermann2025acompendiumof pages 4-5
10. feuermann2025acompendiumof pages 3-4
11. eshaq2024nonreceptortyrosinekinases pages 5-7
12. moncivais2023structuralanalysisof pages 16-17
13. feuermann2025acompendiumof pages 5-6
14. riegel2022recentadvancesin pages 15-15
15. yeung2021evolutionoffunctional pages 14-15
16. https://doi.org/10.1038/s41586-025-08592-0,
17. https://doi.org/10.3390/cancers16152754,
18. https://doi.org/10.3390/ijms241914573,
19. https://doi.org/10.1002/prot.25981,
20. https://doi.org/10.1093/molbev/msab272,
21. https://doi.org/10.3389/fcell.2022.942500,
22. https://doi.org/10.3390/ijms24076805,