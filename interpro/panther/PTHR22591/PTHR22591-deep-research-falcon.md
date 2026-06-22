---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-21T20:32:59.599683'
end_time: '2026-06-21T20:45:43.350370'
duration_seconds: 763.75
template_file: templates/interpro_family_research.md
template_variables:
  interpro_id: PTHR22591
  interpro_name: XIN
  interpro_short_name: Not specified
  interpro_type: family
  interpro_integrated: IPR030072
  member_databases: Not specified
  n_proteins: '1837'
  n_taxa: '2195'
  n_subfamilies: '3'
  interpro2go_terms: None mapped (no InterPro2GO terms for this entry)
  interpro_description: Not specified in InterPro
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 23
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: PTHR22591-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: PTHR22591-deep-research-falcon_artifacts/artifact-01.md
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
- **Accession:** PTHR22591
- **Name:** XIN
- **Short name:** Not specified
- **Entry type:** family
- **Integrated into / parent:** IPR030072
- **Member database signatures:** Not specified
- **Scale:** 1837 proteins across 2195 taxa, 3 subfamilies
- **Current InterPro2GO terms (the mappings under review):** None mapped (no InterPro2GO terms for this entry)
- **InterPro description:** Not specified in InterPro

### Why entry type matters:

An entry of type **domain**, **repeat**, or **homologous_superfamily** identifies a
structural/functional *module*, not a whole-protein function. GO terms describing a
whole-protein activity or process attached to such a module systematically over-annotate
every protein that merely *contains* the module. An entry of type **family** is more
likely to support whole-protein function terms, but only if the family is functionally
homogeneous.

## Research Target

Provide a comprehensive, citation-backed research report on the InterPro entry
**PTHR22591 (XIN)**, structured to support GO annotation review.

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
- **Accession:** PTHR22591
- **Name:** XIN
- **Short name:** Not specified
- **Entry type:** family
- **Integrated into / parent:** IPR030072
- **Member database signatures:** Not specified
- **Scale:** 1837 proteins across 2195 taxa, 3 subfamilies
- **Current InterPro2GO terms (the mappings under review):** None mapped (no InterPro2GO terms for this entry)
- **InterPro description:** Not specified in InterPro

### Why entry type matters:

An entry of type **domain**, **repeat**, or **homologous_superfamily** identifies a
structural/functional *module*, not a whole-protein function. GO terms describing a
whole-protein activity or process attached to such a module systematically over-annotate
every protein that merely *contains* the module. An entry of type **family** is more
likely to support whole-protein function terms, but only if the family is functionally
homogeneous.

## Research Target

Provide a comprehensive, citation-backed research report on the InterPro entry
**PTHR22591 (XIN)**, structured to support GO annotation review.

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


# InterPro Family Research Report: PTHR22591 (XIN)

## Executive Summary

InterPro entry PTHR22591 represents the XIN (Xin actin-binding repeat-containing protein) family, a well-characterized group of striated muscle structural proteins. This family is classified as "family" type in InterPro and currently has **no InterPro2GO mappings**. Based on comprehensive literature review of recent (2020-2024) authoritative sources, this absence of GO annotations is **inappropriate**. The family warrants core functional annotations, though care must be taken to avoid subfamily-specific over-annotation.

---

## 1. Family Definition and Biochemistry

> XIN/XIRP proteins are striated-muscle adaptor proteins of the Xin actin-binding repeat-containing family, with two principal vertebrate paralogs in mammals: XIRP1 (Xinα) and XIRP2 (Xinβ) (guo2020intercalateddiscprotein pages 1-2, long2015exomesequencingidentifies pages 1-2).
>
> Their defining conserved feature is the Xin repeat region, which mediates association with actin and underlies their classification as actin-binding structural proteins rather than enzymes; the literature describes them in the context of cytoskeletal organization, intercellular junctions, and sarcomeric architecture, not catalytic chemistry (guo2020intercalateddiscprotein pages 1-2, nguyen2023roleofactinbinding pages 1-3, noureddine2023structuralandsignaling pages 1-2).
>
> Experimentally and in reviews, XIN proteins are reported to interact with or associate closely with actin, N-cadherin, β-catenin, α-actinin, and filamin C, linking junctional complexes and myofibrillar structures to the actin cytoskeleton (guo2020intercalateddiscprotein pages 1-2, podyacheva2022sirt1activationand pages 1-2, noureddine2023structuralandsignaling pages 5-6).
>
> Subcellularly, family members localize to mechanically stressed attachment structures in muscle cells, especially Z-discs and intercalated discs, with Xinβ particularly emphasized as an intercalated-disc component in cardiomyocytes (guo2020intercalateddiscprotein pages 1-2, nielsen2023theintercalateddisc pages 2-4, noureddine2023structuralandsignaling pages 1-2).
>
> Functionally, the family supports structural integrity, actin filament stabilization/organization, and cell-cell adhesion in striated muscle; loss of Xinβ disrupts intercalated-disc organization and impairs cardiac signaling and function, reinforcing that these proteins act as scaffolds/adaptors in muscle architecture (guo2020intercalateddiscprotein pages 1-2, long2015exomesequencingidentifies pages 1-2, long2015exomesequencingidentifies pages 2-3).


*Blockquote: This blockquote summarizes the defining biochemical and structural features of the XIN/XIRP family, including conserved domains, major binding partners, localization, and core muscle-structural roles. It is useful for quickly assessing what family-level GO terms are supported by the literature.*

The XIN family comprises non-catalytic adapter proteins that stabilize and organize actin-based structures in striated muscle (guo2020intercalateddiscprotein pages 1-2, nguyen2023roleofactinbinding pages 1-3, noureddine2023structuralandsignaling pages 1-2). The family is defined by conserved **Xin actin-binding repeat domains** that mediate direct association with F-actin (guo2020intercalateddiscprotein pages 1-2). No enzymatic activity has been reported; these are **structural constituents** rather than enzymes (mao2020structureandfunction pages 1-3, noureddine2023structuralandsignaling pages 5-6).

### Conserved Molecular Features

The mammalian family contains two paralogous genes encoding **XIRP1 (Xinα)** and **XIRP2 (Xinβ)** (guo2020intercalateddiscprotein pages 1-2, long2015exomesequencingidentifies pages 1-2). Both proteins share:

- **Xin actin-binding repeats**: the signature domain responsible for actin filament association (guo2020intercalateddiscprotein pages 1-2, nguyen2023roleofactinbinding pages 1-3)
- **No catalytic residues or active sites**: function is purely structural/scaffolding (mao2020structureandfunction pages 1-3, noureddine2023structuralandsignaling pages 1-2)
- **Multi-protein interaction capacity**: bind N-cadherin, β-catenin, α-actinin, and filamin C to bridge junctional complexes with the actin cytoskeleton (guo2020intercalateddiscprotein pages 1-2, podyacheva2022sirt1activationand pages 1-2, noureddine2023structuralandsignaling pages 5-6)

Primary literature demonstrates that mouse Xin proteins directly bind to N-cadherin and that loss of Xinβ leads to misregistration and mislocalization of intercalated disc components including N-cadherin and β-catenin (podyacheva2022sirt1activationand pages 1-2, long2015exomesequencingidentifies pages 2-3). The interaction with filamin C is well-documented, with filamin C containing a unique 80-amino acid insertion in its Ig20 domain that mediates XIRP1/XIRP2 binding (noureddine2023structuralandsignaling pages 5-6).

### Structural Biology

While high-resolution structures of full-length XIN proteins are not yet available, the functional architecture places them as **adapter proteins** linking actin thin filaments to cell-cell and cell-matrix adhesion complexes at Z-discs and intercalated discs (guo2020intercalateddiscprotein pages 1-2, nielsen2023theintercalateddisc pages 2-4, noureddine2023structuralandsignaling pages 1-2). Electron microscopy of Xinβ-deficient hearts reveals shortened and misaligned intercalated discs, confirming the structural organizing role (long2015exomesequencingidentifies pages 1-2, long2015exomesequencingidentifies pages 2-3).

---

## 2. InterPro2GO Mapping Appropriateness

**Current status**: No GO terms are mapped to PTHR22591.

**Verdict**: This is **INAPPROPRIATE**. The XIN family has robust experimental characterization supporting multiple conserved GO annotations.

### Recommended Core Annotations (Appropriate for ALL Family Members)

| GO term with ID | Evidence type / appropriateness | Rationale with literature citations |
|---|---|---|
| actin binding (GO:0003779) | Appropriate for all members | XIN/XIRP proteins are consistently described as Xin actin-binding repeat-containing proteins, and the family is defined by conserved Xin repeats that mediate actin association; reviews and primary studies place both XIRP1 and XIRP2 in actin-linked muscle structures (guo2020intercalateddiscprotein pages 1-2, nguyen2023roleofactinbinding pages 1-3, noureddine2023structuralandsignaling pages 1-2). |
| structural constituent of muscle (GO:0008307) | Appropriate for all members | Family members are muscle-enriched structural proteins associated with sarcomeric/Z-disc and intercalated-disc architecture, supporting mechanical integrity in striated muscle rather than a catalytic role (mao2020structureandfunction pages 1-3, noureddine2023structuralandsignaling pages 5-6, noureddine2023structuralandsignaling pages 1-2). |
| cadherin binding (GO:0045296) | Appropriate for all members | Xinα/Xinβ are reported to bind adherens-junction proteins including N-cadherin and β-catenin, supporting cadherin-associated binding as a shared family property (guo2020intercalateddiscprotein pages 1-2, podyacheva2022sirt1activationand pages 1-2). |
| actin cytoskeleton organization (GO:0030036) | Appropriate for all members | XIN proteins connect actin filaments to junctional and Z-disc complexes and are implicated in stabilization/organization of actin-linked structures in muscle cells (guo2020intercalateddiscprotein pages 1-2, noureddine2023structuralandsignaling pages 5-6, noureddine2023structuralandsignaling pages 1-2). |
| muscle cell development (GO:0055001) | Appropriate for all members | The family is muscle-specific and linked to development and maturation of striated-muscle structures; Xinβ loss impairs heart development, while broader reviews place Xin proteins in skeletal/cardiac myogenic machinery (guo2020intercalateddiscprotein pages 1-2, nguyen2023roleofactinbinding pages 1-3, long2015exomesequencingidentifies pages 1-2). |
| intercalated disc assembly (GO:0086044) | Subfamily-specific; not appropriate for all members | Strongest evidence is for XIRP2/Xinβ, whose loss disrupts intercalated-disc maturation and organization in heart; this should not be generalized across the whole family without caution because XIRP1 also localizes to Z-disc/skeletal contexts (guo2020intercalateddiscprotein pages 1-2, long2015exomesequencingidentifies pages 1-2, long2015exomesequencingidentifies pages 2-3). |
| Z disc assembly (GO:0030239) | Appropriate for all members | XIN/XIRP proteins are repeatedly linked to Z-disc organization/assembly and interact with key Z-disc proteins such as filamin C; both family members participate in striated-muscle structural assembly programs (mao2020structureandfunction pages 1-3, noureddine2023structuralandsignaling pages 5-6, noureddine2023structuralandsignaling pages 1-2). |
| cell-cell adhesion (GO:0098609) | Appropriate for all members | Family members bind adherens-junction components and localize to load-bearing adhesive structures, indicating a general role in cell-cell adhesion in striated muscle (guo2020intercalateddiscprotein pages 1-2, nielsen2023theintercalateddisc pages 2-4, podyacheva2022sirt1activationand pages 1-2). |
| cardiac muscle tissue development (GO:0048738) | XIRP2-enriched / partially family-supported | Xinβ has strong experimental evidence in cardiac development and proliferation, while the broader family is clearly relevant to cardiac muscle but not exclusively or uniformly to the same degree across all members and tissues (guo2020intercalateddiscprotein pages 1-2, guo2020intercalateddiscprotein pages 3-4, guo2020intercalateddiscprotein pages 5-6). |
| regulation of Hippo signaling (GO:0035329) | XIRP2-specific; not appropriate for all members | Direct experimental evidence shows Xinβ recruits NF2 and is required for Hippo-YAP signaling in heart; this is a specific mechanistic finding for XIRP2 and should not be propagated to all family members (guo2020intercalateddiscprotein pages 1-2, guo2020intercalateddiscprotein pages 3-4). |
| intercalated disc (GO:0014704) | Subfamily-/context-enriched; not universal | XIN proteins are prominent at the intercalated disc in cardiomyocytes, especially XIRP2/Xinβ, but the family also includes proteins with major Z-disc/skeletal-muscle localization; thus the component term is not universally safe as a core family annotation (guo2020intercalateddiscprotein pages 1-2, nielsen2023theintercalateddisc pages 2-4, guo2020intercalateddiscprotein pages 5-6). |
| Z disc (GO:0030018) | Appropriate for all members | Reviews of muscle structural proteins place XIN/XIRP proteins at or associated with the Z-disc, and their interaction network includes canonical Z-disc proteins such as filamin C (mao2020structureandfunction pages 1-3, noureddine2023structuralandsignaling pages 5-6, noureddine2023structuralandsignaling pages 1-2). |
| sarcomere (GO:0030017) | Appropriate for all members | Because XIN proteins function in Z-disc/actin-linked contractile architecture, sarcomere localization is supported across the family as a broader component term (mao2020structureandfunction pages 1-3, noureddine2023structuralandsignaling pages 5-6, noureddine2023structuralandsignaling pages 1-2). |
| actin cytoskeleton (GO:0015629) | Appropriate for all members | Family members are actin-associated structural proteins embedded in actin-rich muscle cytoskeletal systems, making this a safe and general cellular-component assignment (guo2020intercalateddiscprotein pages 1-2, nguyen2023roleofactinbinding pages 1-3, noureddine2023structuralandsignaling pages 1-2). |
| adherens junction (GO:0005912) | Appropriate for all members | XIN proteins interact with adherens-junction proteins, especially N-cadherin/β-catenin complexes, and localize to adherens-junction-rich muscle attachment sites (guo2020intercalateddiscprotein pages 1-2, nielsen2023theintercalateddisc pages 2-4, podyacheva2022sirt1activationand pages 1-2). |


*Table: This table summarizes candidate GO annotations for the XIN/XIRP family and flags which terms appear safe for the full family versus those that are better restricted to XIRP2 or cardiac-specific contexts. It is useful for deciding whether new InterPro2GO mappings should be added conservatively.*

The following GO terms are supported by evidence across XIRP1 and XIRP2 in multiple species and should be added as **family-level InterPro2GO mappings**:

**Molecular Function:**
- **actin binding (GO:0003779)**: Direct experimental evidence from actin co-localization, pull-down assays, and the defining Xin actin-binding repeat signature (guo2020intercalateddiscprotein pages 1-2, nguyen2023roleofactinbinding pages 1-3, noureddine2023structuralandsignaling pages 1-2)
- **structural constituent of muscle (GO:0008307)**: XIN proteins are non-enzymatic structural components essential for sarcomere and intercalated disc integrity (mao2020structureandfunction pages 1-3, noureddine2023structuralandsignaling pages 5-6, noureddine2023structuralandsignaling pages 1-2)
- **cadherin binding (GO:0045296)**: Documented N-cadherin and β-catenin interactions at adherens junctions (guo2020intercalateddiscprotein pages 1-2, podyacheva2022sirt1activationand pages 1-2)

**Biological Process:**
- **actin cytoskeleton organization (GO:0030036)**: XIN proteins organize and stabilize actin filaments at muscle attachment sites (guo2020intercalateddiscprotein pages 1-2, noureddine2023structuralandsignaling pages 5-6, noureddine2023structuralandsignaling pages 1-2)
- **muscle cell development (GO:0055001)**: Loss-of-function studies demonstrate requirement for proper muscle maturation in both cardiac and skeletal contexts (guo2020intercalateddiscprotein pages 1-2, nguyen2023roleofactinbinding pages 1-3, long2015exomesequencingidentifies pages 1-2)
- **Z disc assembly (GO:0030239)**: Both XIRP1 and XIRP2 participate in Z-disc organization and interact with Z-disc proteins like filamin C (mao2020structureandfunction pages 1-3, noureddine2023structuralandsignaling pages 5-6, noureddine2023structuralandsignaling pages 1-2)
- **cell-cell adhesion (GO:0098609)**: Family members localize to and stabilize adherens junctions in muscle (guo2020intercalateddiscprotein pages 1-2, nielsen2023theintercalateddisc pages 2-4, podyacheva2022sirt1activationand pages 1-2)

**Cellular Component:**
- **Z disc (GO:0030018)**: Well-established localization for both XIRP1 and XIRP2 in striated muscle (mao2020structureandfunction pages 1-3, noureddine2023structuralandsignaling pages 5-6, noureddine2023structuralandsignaling pages 1-2)
- **sarcomere (GO:0030017)**: Broader localization encompassing Z-disc and myofibrillar structures (mao2020structureandfunction pages 1-3, noureddine2023structuralandsignaling pages 5-6, noureddine2023structuralandsignaling pages 1-2)
- **actin cytoskeleton (GO:0015629)**: Family members are integral components of actin-based cytoskeletal networks (guo2020intercalateddiscprotein pages 1-2, nguyen2023roleofactinbinding pages 1-3, noureddine2023structuralandsignaling pages 1-2)
- **adherens junction (GO:0005912)**: Interaction with N-cadherin/β-catenin complexes at junctional structures (guo2020intercalateddiscprotein pages 1-2, nielsen2023theintercalateddisc pages 2-4, podyacheva2022sirt1activationand pages 1-2)

### Subfamily-Specific Terms (NOT APPROPRIATE for Family-Level Annotation)

The following terms are **XIRP2-specific** and should **NOT** be applied to the entire PTHR22591 family:

- **intercalated disc assembly (GO:0086044)**: Strongest evidence is for Xinβ/XIRP2 in cardiac muscle; XIRP1 also localizes to skeletal Z-discs where intercalated discs are absent (guo2020intercalateddiscprotein pages 1-2, long2015exomesequencingidentifies pages 1-2, long2015exomesequencingidentifies pages 2-3)
- **intercalated disc (GO:0014704)**: While XIRP2 is prominently localized here, this is a cardiac-specific structure not present in all contexts where family members function (guo2020intercalateddiscprotein pages 1-2, nielsen2023theintercalateddisc pages 2-4, guo2020intercalateddiscprotein pages 5-6)
- **regulation of Hippo signaling (GO:0035329)**: Direct mechanistic evidence exists only for Xinβ recruiting NF2 to modulate Hippo-YAP signaling in heart; this should not be generalized to the entire family without experimental support for other members (guo2020intercalateddiscprotein pages 1-2, guo2020intercalateddiscprotein pages 3-4, guo2020intercalateddiscprotein pages 5-6)
- **cardiac muscle tissue development (GO:0048738)**: While XIRP2 has strong cardiac-specific roles, XIRP1 is broadly expressed in skeletal and cardiac muscle, making this too narrow for family-wide annotation (guo2020intercalateddiscprotein pages 1-2, guo2020intercalateddiscprotein pages 3-4, guo2020intercalateddiscprotein pages 5-6)

**Recommendation**: These subfamily-specific terms should ideally be mapped to child InterPro entries if subfamilies are distinguished, or annotated at the individual gene/protein level rather than at the family signature level.

---

## 3. Functional Divergence Across the Family

The XIN family shows **functional conservation with tissue-specific expression** rather than true neo-functionalization or opposing functions.

### Two Paralogs, Conserved Core Function

Mammals possess two XIN genes:
- **XIRP1 (Xinα)**: Expressed in both skeletal and cardiac muscle; localizes to Z-discs and myotendinous junctions (mao2020structureandfunction pages 1-3, noureddine2023structuralandsignaling pages 5-6)
- **XIRP2 (Xinβ)**: Predominantly cardiac-specific; enriched at intercalated discs of cardiomyocytes (guo2020intercalateddiscprotein pages 1-2, nielsen2023theintercalateddisc pages 2-4, guo2020intercalateddiscprotein pages 5-6)

Despite differential tissue expression, both proteins share the same **core molecular function**: actin-binding, structural scaffolding, and linkage to adherens junction proteins (guo2020intercalateddiscprotein pages 1-2, podyacheva2022sirt1activationand pages 1-2, noureddine2023structuralandsignaling pages 5-6). There is no evidence of opposing activities or catalytically inactive "pseudoenzyme" variants that retain the fold but lack function.

### Tissue Localization Differences, Not Functional Opposition

The key distinction is **subcellular localization**:
- XIRP1 localizes to Z-discs in skeletal and cardiac muscle sarcomeres
- XIRP2 localizes predominantly to intercalated discs in cardiac muscle (guo2020intercalateddiscprotein pages 1-2, nielsen2023theintercalateddisc pages 2-4)

Both structures are mechanically stressed, actin-rich, cell-cell or cell-matrix adhesion sites. The molecular mechanisms—actin binding, cadherin complex interaction, cytoskeletal organization—are conserved (guo2020intercalateddiscprotein pages 1-2, noureddine2023structuralandsignaling pages 5-6, noureddine2023structuralandsignaling pages 1-2).

### XIRP2-Specific Signaling Role

Recent work identifies a **signaling function unique to Xinβ (XIRP2)**: recruitment of NF2 (neurofibromin 2) to intercalated discs to modulate Hippo-YAP pathway activity, thereby regulating cardiomyocyte proliferation and heart development (guo2020intercalateddiscprotein pages 1-2, guo2020intercalateddiscprotein pages 3-4, guo2020intercalateddiscprotein pages 5-6). Overexpression of constitutively active YAP rescues Xinβ knockout cardiac defects, demonstrating that Xinβ acts upstream of YAP signaling (guo2020intercalateddiscprotein pages 3-4, guo2020intercalateddiscprotein pages 5-6). This signaling function has **not been demonstrated for XIRP1** and represents a tissue-specific elaboration rather than a fundamental family-level property.

### No Catalytically Dead Members

Unlike some protein families with enzymatic and pseudo-enzymatic members, the XIN family comprises only **non-catalytic structural proteins**. There is no evidence of family members that have lost a catalytic function while retaining the fold (mao2020structureandfunction pages 1-3, guo2020intercalateddiscprotein pages 1-2, noureddine2023structuralandsignaling pages 1-2).

**Conclusion on Divergence**: The family is functionally homogeneous at the molecular level (actin-binding structural adapter), with subfamily diversification primarily in tissue expression and secondary signaling roles (XIRP2/Hippo), not in opposing or neo-functionalized core activities.

---

## 4. Taxonomic Scope

### Phylogenetic Distribution

The XIN family is **vertebrate-specific** (and possibly present in invertebrate chordates):

- **Mammals**: Well-characterized XIRP1 and XIRP2 genes in mice, rats, and humans (guo2020intercalateddiscprotein pages 1-2, havlenova2021rightversusleft pages 1-2, wang2023comprehensivereviewon pages 1-2, long2015exomesequencingidentifies pages 1-2)
- **Fish**: Confirmed xirp genes in zebrafish (*Danio rerio*), with expression in developing muscle and tendons (based on vertebrate comparative genomics)
- **Invertebrate deuterostomes**: Possible orthologs in amphioxus and other chordates (inferred from evolutionary context)
- **Ecdysozoan invertebrates**: **NO XIN proteins** found in *Drosophila melanogaster* or *Caenorhabditis elegans* based on literature review and absence of functional studies in these model organisms

The InterPro entry reports **1837 proteins across 2195 taxa**, which likely reflects **homology detection at permissive thresholds** capturing divergent sequences. Functional XIN proteins with demonstrated actin-binding and muscle-structural roles appear **restricted to vertebrates**.

### Intercalated Discs Are Vertebrate-Specific

A critical taxon-specific structure is the **intercalated disc**, unique to vertebrate cardiac muscle (nielsen2023theintercalateddisc pages 2-4). This structure does not exist in invertebrate hearts or non-cardiac tissues. GO terms related to intercalated disc function (GO:0014704, GO:0086044) are therefore **inappropriate for application across the full 2195 taxa** and should be restricted to vertebrate-specific annotations.

### Conservation Across Vertebrate Taxa

Within vertebrates, the core function—**actin binding, Z-disc/sarcomere localization, and muscle structural integrity**—is conserved from fish to mammals (guo2020intercalateddiscprotein pages 1-2, havlenova2021rightversusleft pages 1-2, noureddine2023structuralandsignaling pages 1-2). Process and component terms relating to sarcomeres, Z-discs, actin cytoskeleton, and muscle development are appropriate across the vertebrate clade.

**Taxonomic Conclusion**: Family-level GO terms should reflect functions conserved across **all vertebrates**. Cardiac-specific terms (intercalated disc) should not be applied family-wide due to both subfamily restriction (XIRP2) and absence in non-cardiac contexts.

---

## 5. Over-Annotation Verdict and Recommendations

### Summary Verdict: CURRENTLY UNDER-ANNOTATED; RISK OF SUBFAMILY OVER-ANNOTATION IF NOT CAREFUL

**Current State**: InterPro entry PTHR22591 has **zero GO terms mapped**. This is **inappropriate** given the extensive experimental and structural characterization of the XIN family.

**Recommended Action Pattern**: **ADD core annotations (MODIFY-to-specific for some terms)**

### Specific Recommendations:

1. **ACCEPT and ADD** the following family-conserved GO terms to PTHR22591:
   - MF: actin binding (GO:0003779), structural constituent of muscle (GO:0008307), cadherin binding (GO:0045296)
   - BP: actin cytoskeleton organization (GO:0030036), muscle cell development (GO:0055001), Z disc assembly (GO:0030239), cell-cell adhesion (GO:0098609)
   - CC: Z disc (GO:0030018), sarcomere (GO:0030017), actin cytoskeleton (GO:0015629), adherens junction (GO:0005912)

2. **DO NOT ADD** the following subfamily-specific terms to the PTHR22591 family entry:
   - intercalated disc assembly (GO:0086044) — XIRP2-specific
   - intercalated disc (GO:0014704) — XIRP2-specific, vertebrate cardiac-specific
   - regulation of Hippo signaling (GO:0035329) — XIRP2-specific signaling function
   - cardiac muscle tissue development (GO:0048738) — XIRP2-enriched, not universal

3. **RECOMMENDED INTERP ACTION**: If InterPro defines child entries or subfamilies distinguishing XIRP1 from XIRP2, map the cardiac/intercalated disc-specific terms to the XIRP2 child entry only.

4. **KEEP AS NON-CORE** any hypothetical terms related to:
   - Generic "metal ion binding" or "ATP binding" (not applicable; XIN proteins are non-enzymatic with no reported nucleotide or metal cofactor requirements)
   - Process terms for pathways absent in non-vertebrate taxa where the signature may spuriously match

### Rationale for Verdict

This is a **family** entry (not a domain or repeat), and the family is functionally **homogeneous at the core molecular level** (actin-binding structural adapter). The risk of over-annotation comes from:

(a) **Subfamily specificity**: XIRP2 has cardiac-specific localization and Hippo signaling roles not shared by XIRP1.

(b) **Taxonomic leakage**: Intercalated disc structures exist only in vertebrate hearts; applying such terms family-wide would mis-annotate any non-vertebrate or non-cardiac matches.

(c) **Domain vs. whole-protein conflation**: PTHR22591 is classified as "family," implying whole-protein homology. The conserved Xin repeat domains mediate actin binding, which is appropriate to annotate. However, whole-protein localization (intercalated disc) or whole-cell processes (cardiac development) vary by subfamily and should not be uniformly applied.

**The solution is stratified annotation**: Core structural and molecular functions (actin binding, Z-disc assembly, muscle development) apply to all family members. Tissue-specific and signaling terms should be reserved for subfamily-specific child entries or individual gene annotations.

---

## References (Key Primary and Review Literature)

- Guo et al. (2020). Intercalated disc protein Xinβ is required for Hippo-YAP signaling in the heart. *Nature Communications* 11:4666. (guo2020intercalateddiscprotein pages 1-2, guo2020intercalateddiscprotein pages 3-4, guo2020intercalateddiscprotein pages 5-6)
- Nielsen et al. (2023). The intercalated disc: a unique organelle for electromechanical synchrony in cardiomyocytes. *Physiological Reviews* 103:2271-2319. (nielsen2023theintercalateddisc pages 2-4)
- Nguyen et al. (2023). Role of Actin-Binding Proteins in Skeletal Myogenesis. *Cells* 12:2523. (nguyen2023roleofactinbinding pages 1-3)
- Mao & Nakamura (2020). Structure and Function of Filamin C in the Muscle Z-Disc. *International Journal of Molecular Sciences* 21:2696. (mao2020structureandfunction pages 1-3, noureddine2023structuralandsignaling pages 5-6)
- Long et al. (2015). Exome Sequencing Identifies Pathogenic and Modifier Mutations in a Child With Sporadic Dilated Cardiomyopathy. *Journal of the American Heart Association* 4:e002443. (long2015exomesequencingidentifies pages 1-2, long2015exomesequencingidentifies pages 2-3)
- Havlenova et al. (2021). Right versus left ventricular remodeling in heart failure due to chronic volume overload. *Scientific Reports* 11:17136. (havlenova2021rightversusleft pages 1-2)
- Wang et al. (2023). Comprehensive review on gene mutations contributing to dilated cardiomyopathy. *Frontiers in Cardiovascular Medicine* 10:1296389. (wang2023comprehensivereviewon pages 1-2)
- Podyacheva & Toropova (2022). SIRT1 activation and its effect on intercalated disc proteins as a way to reduce doxorubicin cardiotoxicity. *Frontiers in Pharmacology* 13:1035387. (podyacheva2022sirt1activationand pages 1-2)
- Noureddine & Gehmlich (2023). Structural and signaling proteins in the Z-disk and their role in cardiomyopathies. *Frontiers in Physiology* 14:1143858. (noureddine2023structuralandsignaling pages 5-6, noureddine2023structuralandsignaling pages 1-2)
- Wadmore et al. (2021). The Role of Z-disc Proteins in Myopathy and Cardiomyopathy. *International Journal of Molecular Sciences* 22:3058. (wadmore2021theroleof pages 1-2)

---

## Conclusion

The XIN family (PTHR22591) is a well-defined, functionally conserved group of striated muscle structural proteins. The current absence of InterPro2GO mappings is **unjustified**. Core family-level GO annotations for actin binding, muscle structural roles, and cytoskeletal organization should be **added immediately**. However, subfamily-specific terms (intercalated disc, cardiac-specific processes, Hippo signaling) should be **excluded from the family-level entry** to prevent systematic over-annotation. If InterPro can distinguish XIRP1 vs. XIRP2 subfamilies, cardiac-specific terms should be mapped only to XIRP2.

**Final Recommendation**: **MODIFY-to-specific** — add core conserved annotations; reserve subfamily/tissue-specific terms for child entries or manual gene-level curation.

References

1. (guo2020intercalateddiscprotein pages 1-2): Haipeng Guo, Yao Wei Lu, Zhiqiang Lin, Zhan-Peng Huang, Jianming Liu, Yi Wang, Hee Young Seok, Xiaoyun Hu, Qing Ma, Kathryn Li, Jan Kyselovic, Qingchuan Wang, Jenny L.-C. Lin, Jim J.-C. Lin, Douglas B. Cowan, Francisco Naya, Yuguo Chen, William T. Pu, and Da-Zhi Wang. Intercalated disc protein xinβ is required for hippo-yap signaling in the heart. Nature Communications, Sep 2020. URL: https://doi.org/10.1038/s41467-020-18379-8, doi:10.1038/s41467-020-18379-8. This article has 30 citations and is from a highest quality peer-reviewed journal.

2. (long2015exomesequencingidentifies pages 1-2): Pamela A. Long, Brandon T. Larsen, Jared M. Evans, and Timothy M. Olson. Exome sequencing identifies pathogenic and modifier mutations in a child with sporadic dilated cardiomyopathy. Journal of the American Heart Association: Cardiovascular and Cerebrovascular Disease, Dec 2015. URL: https://doi.org/10.1161/jaha.115.002443, doi:10.1161/jaha.115.002443. This article has 35 citations and is from a domain leading peer-reviewed journal.

3. (nguyen2023roleofactinbinding pages 1-3): Mai Thi Nguyen, Raju Dash, Kyuho Jeong, and Wan Lee. Role of actin-binding proteins in skeletal myogenesis. Cells, 12:2523, Oct 2023. URL: https://doi.org/10.3390/cells12212523, doi:10.3390/cells12212523. This article has 26 citations.

4. (noureddine2023structuralandsignaling pages 1-2): Maya Noureddine and Katja Gehmlich. Structural and signaling proteins in the z-disk and their role in cardiomyopathies. Frontiers in Physiology, Mar 2023. URL: https://doi.org/10.3389/fphys.2023.1143858, doi:10.3389/fphys.2023.1143858. This article has 48 citations.

5. (podyacheva2022sirt1activationand pages 1-2): Ekaterina Podyacheva and Yana Toropova. Sirt1 activation and its effect on intercalated disc proteins as a way to reduce doxorubicin cardiotoxicity. Frontiers in Pharmacology, Nov 2022. URL: https://doi.org/10.3389/fphar.2022.1035387, doi:10.3389/fphar.2022.1035387. This article has 30 citations.

6. (noureddine2023structuralandsignaling pages 5-6): Maya Noureddine and Katja Gehmlich. Structural and signaling proteins in the z-disk and their role in cardiomyopathies. Frontiers in Physiology, Mar 2023. URL: https://doi.org/10.3389/fphys.2023.1143858, doi:10.3389/fphys.2023.1143858. This article has 48 citations.

7. (nielsen2023theintercalateddisc pages 2-4): Morten S. Nielsen, Chantal J. M. van Opbergen, Toon A. B. van Veen, and Mario Delmar. The intercalated disc: a unique organelle for electromechanical synchrony in cardiomyocytes. Jul 2023. URL: https://doi.org/10.1152/physrev.00021.2022, doi:10.1152/physrev.00021.2022. This article has 70 citations and is from a highest quality peer-reviewed journal.

8. (long2015exomesequencingidentifies pages 2-3): Pamela A. Long, Brandon T. Larsen, Jared M. Evans, and Timothy M. Olson. Exome sequencing identifies pathogenic and modifier mutations in a child with sporadic dilated cardiomyopathy. Journal of the American Heart Association: Cardiovascular and Cerebrovascular Disease, Dec 2015. URL: https://doi.org/10.1161/jaha.115.002443, doi:10.1161/jaha.115.002443. This article has 35 citations and is from a domain leading peer-reviewed journal.

9. (mao2020structureandfunction pages 1-3): Zhenfeng Mao and Fumihiko Nakamura. Structure and function of filamin c in the muscle z-disc. International Journal of Molecular Sciences, 21:2696, Apr 2020. URL: https://doi.org/10.3390/ijms21082696, doi:10.3390/ijms21082696. This article has 129 citations.

10. (guo2020intercalateddiscprotein pages 3-4): Haipeng Guo, Yao Wei Lu, Zhiqiang Lin, Zhan-Peng Huang, Jianming Liu, Yi Wang, Hee Young Seok, Xiaoyun Hu, Qing Ma, Kathryn Li, Jan Kyselovic, Qingchuan Wang, Jenny L.-C. Lin, Jim J.-C. Lin, Douglas B. Cowan, Francisco Naya, Yuguo Chen, William T. Pu, and Da-Zhi Wang. Intercalated disc protein xinβ is required for hippo-yap signaling in the heart. Nature Communications, Sep 2020. URL: https://doi.org/10.1038/s41467-020-18379-8, doi:10.1038/s41467-020-18379-8. This article has 30 citations and is from a highest quality peer-reviewed journal.

11. (guo2020intercalateddiscprotein pages 5-6): Haipeng Guo, Yao Wei Lu, Zhiqiang Lin, Zhan-Peng Huang, Jianming Liu, Yi Wang, Hee Young Seok, Xiaoyun Hu, Qing Ma, Kathryn Li, Jan Kyselovic, Qingchuan Wang, Jenny L.-C. Lin, Jim J.-C. Lin, Douglas B. Cowan, Francisco Naya, Yuguo Chen, William T. Pu, and Da-Zhi Wang. Intercalated disc protein xinβ is required for hippo-yap signaling in the heart. Nature Communications, Sep 2020. URL: https://doi.org/10.1038/s41467-020-18379-8, doi:10.1038/s41467-020-18379-8. This article has 30 citations and is from a highest quality peer-reviewed journal.

12. (havlenova2021rightversusleft pages 1-2): Tereza Havlenova, Petra Skaroupkova, Matus Miklovic, Matej Behounek, Martin Chmel, Dagmar Jarkovska, Jitka Sviglerova, Milan Stengl, Michal Kolar, Jiri Novotny, Jan Benes, Ludek Cervenka, Jiri Petrak, and Vojtech Melenovsky. Right versus left ventricular remodeling in heart failure due to chronic volume overload. Scientific Reports, Aug 2021. URL: https://doi.org/10.1038/s41598-021-96618-8, doi:10.1038/s41598-021-96618-8. This article has 56 citations and is from a peer-reviewed journal.

13. (wang2023comprehensivereviewon pages 1-2): Shipeng Wang, Zhiyu Zhang, Jiahuan He, Junqian Liu, Xia Guo, Haoxuan Chu, Hanchi Xu, and Yushi Wang. Comprehensive review on gene mutations contributing to dilated cardiomyopathy. Frontiers in Cardiovascular Medicine, Dec 2023. URL: https://doi.org/10.3389/fcvm.2023.1296389, doi:10.3389/fcvm.2023.1296389. This article has 27 citations and is from a peer-reviewed journal.

14. (wadmore2021theroleof pages 1-2): Kirsty Wadmore, Amar J. Azad, and Katja Gehmlich. The role of z-disc proteins in myopathy and cardiomyopathy. International Journal of Molecular Sciences, 22:3058, Mar 2021. URL: https://doi.org/10.3390/ijms22063058, doi:10.3390/ijms22063058. This article has 73 citations.

## Artifacts

- [Edison artifact artifact-00](PTHR22591-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](PTHR22591-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. guo2020intercalateddiscprotein pages 1-2
2. noureddine2023structuralandsignaling pages 5-6
3. nielsen2023theintercalateddisc pages 2-4
4. nguyen2023roleofactinbinding pages 1-3
5. havlenova2021rightversusleft pages 1-2
6. wang2023comprehensivereviewon pages 1-2
7. wadmore2021theroleof pages 1-2
8. long2015exomesequencingidentifies pages 1-2
9. noureddine2023structuralandsignaling pages 1-2
10. long2015exomesequencingidentifies pages 2-3
11. mao2020structureandfunction pages 1-3
12. guo2020intercalateddiscprotein pages 3-4
13. guo2020intercalateddiscprotein pages 5-6
14. https://doi.org/10.1038/s41467-020-18379-8,
15. https://doi.org/10.1161/jaha.115.002443,
16. https://doi.org/10.3390/cells12212523,
17. https://doi.org/10.3389/fphys.2023.1143858,
18. https://doi.org/10.3389/fphar.2022.1035387,
19. https://doi.org/10.1152/physrev.00021.2022,
20. https://doi.org/10.3390/ijms21082696,
21. https://doi.org/10.1038/s41598-021-96618-8,
22. https://doi.org/10.3389/fcvm.2023.1296389,
23. https://doi.org/10.3390/ijms22063058,