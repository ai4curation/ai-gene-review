---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-21T20:18:32.484513'
end_time: '2026-06-21T20:31:08.054061'
duration_seconds: 755.57
template_file: templates/interpro_family_research.md
template_variables:
  interpro_id: PTHR12480
  interpro_name: JMJD6 family arginine demethylases/lysyl-hydroxylases
  interpro_short_name: JMJD6_ArgDemeth/LysHydrox
  interpro_type: family
  interpro_integrated: IPR050910
  member_databases: Not specified
  n_proteins: '10081'
  n_taxa: '8924'
  n_subfamilies: '10'
  interpro2go_terms: None mapped (no InterPro2GO terms for this entry)
  interpro_description: The JMJD6 family proteins are multifunctional dioxygenases
    with roles in RNA splicing, gene expression regulation, and embryonic development.
    They exhibit bifunctional activity, acting as both arginine demethylases and lysyl-hydroxylases.
    Members of this family are involved in the hydroxylation of specific lysine residues
    on target proteins, which is crucial for processes such as RNA splicing and nucleolar
    organization. Additionally, they demethylate arginine residues on histones and
    other proteins, influencing the histone code and transcriptional regulation. These
    proteins are implicated in hematopoietic differentiation, angiogenic sprouting,
    and macrophage cytokine responses. Some family members also interact with transcriptional
    machinery to modulate polymerase II promoter-proximal pause release and transcriptional
    activation. The nuclear localization signal motifs within these proteins are key
    for their nuclear targeting.
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 20
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: PTHR12480-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: PTHR12480-deep-research-falcon_artifacts/artifact-01.md
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
- **Accession:** PTHR12480
- **Name:** JMJD6 family arginine demethylases/lysyl-hydroxylases
- **Short name:** JMJD6_ArgDemeth/LysHydrox
- **Entry type:** family
- **Integrated into / parent:** IPR050910
- **Member database signatures:** Not specified
- **Scale:** 10081 proteins across 8924 taxa, 10 subfamilies
- **Current InterPro2GO terms (the mappings under review):** None mapped (no InterPro2GO terms for this entry)
- **InterPro description:** The JMJD6 family proteins are multifunctional dioxygenases with roles in RNA splicing, gene expression regulation, and embryonic development. They exhibit bifunctional activity, acting as both arginine demethylases and lysyl-hydroxylases. Members of this family are involved in the hydroxylation of specific lysine residues on target proteins, which is crucial for processes such as RNA splicing and nucleolar organization. Additionally, they demethylate arginine residues on histones and other proteins, influencing the histone code and transcriptional regulation. These proteins are implicated in hematopoietic differentiation, angiogenic sprouting, and macrophage cytokine responses. Some family members also interact with transcriptional machinery to modulate polymerase II promoter-proximal pause release and transcriptional activation. The nuclear localization signal motifs within these proteins are key for their nuclear targeting.

### Why entry type matters:

An entry of type **domain**, **repeat**, or **homologous_superfamily** identifies a
structural/functional *module*, not a whole-protein function. GO terms describing a
whole-protein activity or process attached to such a module systematically over-annotate
every protein that merely *contains* the module. An entry of type **family** is more
likely to support whole-protein function terms, but only if the family is functionally
homogeneous.

## Research Target

Provide a comprehensive, citation-backed research report on the InterPro entry
**PTHR12480 (JMJD6 family arginine demethylases/lysyl-hydroxylases)**, structured to support GO annotation review.

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
- **Accession:** PTHR12480
- **Name:** JMJD6 family arginine demethylases/lysyl-hydroxylases
- **Short name:** JMJD6_ArgDemeth/LysHydrox
- **Entry type:** family
- **Integrated into / parent:** IPR050910
- **Member database signatures:** Not specified
- **Scale:** 10081 proteins across 8924 taxa, 10 subfamilies
- **Current InterPro2GO terms (the mappings under review):** None mapped (no InterPro2GO terms for this entry)
- **InterPro description:** The JMJD6 family proteins are multifunctional dioxygenases with roles in RNA splicing, gene expression regulation, and embryonic development. They exhibit bifunctional activity, acting as both arginine demethylases and lysyl-hydroxylases. Members of this family are involved in the hydroxylation of specific lysine residues on target proteins, which is crucial for processes such as RNA splicing and nucleolar organization. Additionally, they demethylate arginine residues on histones and other proteins, influencing the histone code and transcriptional regulation. These proteins are implicated in hematopoietic differentiation, angiogenic sprouting, and macrophage cytokine responses. Some family members also interact with transcriptional machinery to modulate polymerase II promoter-proximal pause release and transcriptional activation. The nuclear localization signal motifs within these proteins are key for their nuclear targeting.

### Why entry type matters:

An entry of type **domain**, **repeat**, or **homologous_superfamily** identifies a
structural/functional *module*, not a whole-protein function. GO terms describing a
whole-protein activity or process attached to such a module systematically over-annotate
every protein that merely *contains* the module. An entry of type **family** is more
likely to support whole-protein function terms, but only if the family is functionally
homogeneous.

## Research Target

Provide a comprehensive, citation-backed research report on the InterPro entry
**PTHR12480 (JMJD6 family arginine demethylases/lysyl-hydroxylases)**, structured to support GO annotation review.

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


# InterPro2GO Annotation Review: PTHR12480 (JMJD6 Family Arginine Demethylases/Lysyl-Hydroxylases)

## Executive Summary

InterPro entry PTHR12480 currently has **NO** InterPro2GO mappings. This analysis finds this absence **inappropriate** and recommends **adding conserved core biochemical GO terms** while **avoiding controversial or taxon-specific annotations**. The family represents Fe(II)/2-oxoglutarate-dependent dioxygenases with well-supported lysyl hydroxylase activity but controversial arginine demethylase activity.

---

## 1. Family Definition and Biochemistry

### Structural Architecture

PTHR12480 members are **Jumonji C (JmjC) domain-containing Fe(II)- and 2-oxoglutarate (2OG)-dependent dioxygenases** (manni2022jmjdfamilyproteins pages 1-2, yang2020jumonjidomain‐containingprotein pages 1-2). The core catalytic domain adopts a **double-stranded β-helix (DSBH) fold**, also termed a cupin fold, characteristic of 2OG oxygenases (cockman2022widespreadhydroxylationof pages 1-2, yang2020jumonjidomain‐containingprotein pages 1-2, yang2020jumonjidomain‐containingprotein pages 2-4). This barrel-like structure comprises eight β-strands forming two β-sheets, with the Fe(II)-binding site positioned at the opening of the barrel (yang2020jumonjidomain‐containingprotein pages 1-2, yang2020jumonjidomain‐containingprotein pages 2-4).

### Conserved Catalytic Residues

The **active site metal center** is coordinated by the canonical **HXD/E(X)nH motif**: in human JMJD6, His187, Asp189, and His273 bind the catalytic Fe(II) (yang2020jumonjidomain‐containingprotein pages 1-2, yang2020jumonjidomain‐containingprotein pages 2-4). Crystal structures confirm these residues are essential for enzymatic activity; mutagenesis of His187 to alanine significantly reduces 2OG turnover (paschalis2022jmjd6isa pages 1-2, wilkins2018jmjd5isa pages 1-2). The active site also accommodates **2-oxoglutarate** as a cosubstrate adjacent to the Fe(II), with catalysis requiring molecular oxygen and being enhanced by ascorbate (cockman2022widespreadhydroxylationof pages 1-2, corner2025biochemicalinvestigationsusing pages 1-3).

### Enzymatic Mechanism: The Lysyl Hydroxylase vs. Arginine Demethylase Controversy

**Well-Supported Activity: Lysyl Hydroxylase**

The **strongest biochemical evidence** supports JMJD6 as a **peptidyl-lysine C-5 hydroxylase** (cockman2022widespreadhydroxylationof pages 1-2, corner2025biochemicalinvestigationsusing pages 1-3, yang2020jumonjidomain‐containingprotein pages 2-4). Mass spectrometry-based studies have identified >100 sites of JMJD6-catalyzed lysine hydroxylation across 48 proteins, including 19 sites on BRD4 alone (cockman2022widespreadhydroxylationof pages 1-2). JMJD6 preferentially targets **unstructured, lysine-rich regions** in substrates such as bromodomain-containing proteins (BRD2/3/4), splicing factors (U2AF65, LUC7L2, RBM39), p53, and pVHL (cockman2022widespreadhydroxylationof pages 1-2, corner2025biochemicalinvestigationsusing pages 1-3). Kinetic studies using solid-phase extraction coupled to mass spectrometry confirm robust lysyl hydroxylase activity with defined Km values for 2OG, Fe(II), ascorbate, and O₂ (corner2025biochemicalinvestigationsusing pages 1-3).

**Controversial Activity: Arginine Demethylase**

JMJD6 was originally reported as an **arginine demethylase** for histones H3/H4 and non-histone proteins (yang2020jumonjidomain‐containingprotein pages 1-2, konuma2017structuralmechanismof pages 1-2, yang2020jumonjidomain‐containingprotein pages 2-4). However, **multiple subsequent studies failed to confirm direct demethylase activity** with isolated recombinant enzyme (yang2020jumonjidomain‐containingprotein pages 1-2, konuma2017structuralmechanismof pages 1-2, corner2025biochemicalinvestigationsusing pages 1-3, wang2023effectorsandeffects pages 1-2, yang2020jumonjidomain‐containingprotein pages 2-4). JMJD6 incubation with arginine-methylated histone peptides showed no demethylation by MALDI-MS (yang2020jumonjidomain‐containingprotein pages 2-4), and JMJD6 deletion in cells did not affect H4R3 arginine methylation levels (konuma2017structuralmechanismof pages 1-2). Recent reviews treat arginine demethylase assignment as **unresolved or controversial** and emphasize that JMJD6 is "most likely a lysine hydroxylase" (wang2023effectorsandeffects pages 1-2, yang2020jumonjidomain‐containingprotein pages 2-4). The consensus in the 2020s literature is that **lysyl hydroxylation, not arginine demethylation, is the validated core biochemical function** (cockman2022widespreadhydroxylationof pages 1-2, corner2025biochemicalinvestigationsusing pages 1-3).

| Feature | Description | Key Residues/Motifs | Catalytic Activity | Substrates | Evidence Level |
|---|---|---|---|---|---|
| Core fold / domain architecture | JMJD6 family proteins are JmjC-domain Fe(II)/2-oxoglutarate oxygenases with a conserved double-stranded beta-helix (DSBH/cupin) catalytic core; JMJD6 also has N- and C-terminal extensions and a distinctive surface architecture compared with some other JmjC oxygenases. | JmjC domain; DSBH/cupin fold; β-strand core; surrounding short helices | Supports oxygenase chemistry rather than directly defining substrate class | Whole protein scaffold for binding cofactors and protein/RNA partners | Strong: structural and crystallographic support (yang2020jumonjidomain‐containingprotein pages 1-2, konuma2017structuralmechanismof pages 1-2, corner2025biochemicalinvestigationsusing pages 1-3) |
| Metal-binding active site | The catalytic metal center is coordinated by the canonical JmjC HXD/E…H motif; in JMJD6 the Fe(II)-binding residues are reported as His187, Asp189, and His273. | His187-Asp189-…-His273; HXD/E(X)nH motif | Required for oxygen activation and substrate oxidation | All enzymatic substrates depend on intact metal center | Strong: crystal structure and mutagenesis-supported (yang2020jumonjidomain‐containingprotein pages 1-2, yang2020jumonjidomain‐containingprotein pages 2-4, corner2025biochemicalinvestigationsusing pages 1-3) |
| Cosubstrate binding | JMJD6 is a 2-oxoglutarate/Fe(II)-dependent dioxygenase; 2OG binds in the active site adjacent to Fe(II), and catalysis also depends on O2 and is promoted by ascorbate. | 2OG-binding pocket adjacent to Fe(II); catalytic requirement for O2 and ascorbate | Oxidative hydroxylation / demethylation chemistry coupled to 2OG decarboxylation | Broad peptide/protein substrates | Strong for 2OG oxygenase biochemistry; kinetic support available (cockman2022widespreadhydroxylationof pages 1-2, corner2025biochemicalinvestigationsusing pages 1-3, manni2022jmjdfamilyproteins pages 1-2) |
| Primary enzymatic activity: lysyl hydroxylase | Current strongest biochemical support is for post-translational lysyl C5 hydroxylation, including multiple sites in lysine-rich, largely disordered protein regions. Recent work emphasizes widespread hydroxylation of unstructured lysine-rich domains. | Same catalytic HXD…H center; substrate preference for lysine-rich regions | Lysyl C5 hydroxylation | BRD2, BRD3, BRD4; U2AF65; LUC7L2; RBM39; p53; pVHL; histones H3/H4 reported in some studies | Strong overall, especially for BRD proteins and broad lysine-rich substrates by MS-based biochemical/cellular studies (cockman2022widespreadhydroxylationof pages 1-2, corner2025biochemicalinvestigationsusing pages 1-3, yang2020jumonjidomain‐containingprotein pages 2-4) |
| Arginine demethylase activity | JMJD6 was originally reported as an arginine demethylase for histone and non-histone proteins, but multiple later studies could not robustly confirm direct demethylase activity with isolated recombinant enzyme; recent reviews treat this assignment as unresolved or controversial. | No unique alternative catalytic motif established beyond JmjC active site | Proposed N-methyl arginine demethylation | Reported targets include histone H3/H4 arginine marks and some non-histone proteins, but direct catalytic evidence is disputed | Controversial / mixed evidence; not suitable as a universal core family function without caution (yang2020jumonjidomain‐containingprotein pages 1-2, konuma2017structuralmechanismof pages 1-2, corner2025biochemicalinvestigationsusing pages 1-3, wang2023effectorsandeffects pages 1-2, yang2020jumonjidomain‐containingprotein pages 2-4) |
| Substrate spectrum / sequence context | JMJD6 appears relatively substrate-promiscuous compared with some other JmjC enzymes, favoring positively charged, lysine-rich, low-complexity or unstructured regions; many targets are involved in gene expression and biomolecular condensates. | Lysine-rich basic interaction domains; low-complexity/unstructured regions | Predominantly lysyl hydroxylation | >100 hydroxylation sites reported on 48 proteins; 19 sites on BRD4 alone in one study | Strong for broad lysyl-hydroxylase substrate scope in proteomic studies (cockman2022widespreadhydroxylationof pages 1-2, corner2025biochemicalinvestigationsusing pages 1-3) |
| Splicing-associated substrates | JMJD6 modifies or interacts with spliceosome-associated proteins and has been linked to regulation of alternative splicing, especially through U2AF65 and RBM39-associated pathways. | Interaction surfaces outside the catalytic core also likely contribute; lysine-rich target segments | Lysyl hydroxylation; broader splicing regulation may also involve scaffolding/noncatalytic roles | U2AF65, LUC7L2, RBM39; pathways affecting AR-V7, GLS isoforms, Aire-related splicing contexts | Moderate to strong for association and functional effects; catalytic linkage strongest for selected proteins such as U2AF65 (corner2025biochemicalinvestigationsusing pages 1-3, muro2024transcriptsplicingoptimizes pages 1-2, jablonowski2024metabolicreprogrammingof pages 1-2, paschalis2022jmjd6isa pages 1-2) |
| Histone substrates | Histone H3/H4 arginine demethylation was proposed early; later studies instead emphasized lysyl hydroxylation and questioned direct histone arginine demethylation. Histone targeting may be context-dependent and is not uniformly settled. | Reported histone targets include H3R2/H4R3 for demethylation claims; multiple lysines in H3/H4 for hydroxylation claims | Proposed arginine demethylation and/or lysyl hydroxylation | Histones H3 and H4 | Mixed/controversial; not robust enough for universal family-level GO molecular function assignment (konuma2017structuralmechanismof pages 1-2, yang2020jumonjidomain‐containingprotein pages 2-4, corner2025biochemicalinvestigationsusing pages 1-3) |
| Cellular localization signals | JMJD6 contains multiple nuclear localization signals, a nuclear export signal, an AT-hook-like region, a putative SUMOylation site, and a C-terminal polyserine region implicated in subnuclear trafficking and oligomeric behavior. | Five NLSs; NES; AT-hook-like region (around Lys300-Ser309); putative SUMOylation motif (Leu316-Glu319); C-terminal polyserine region | Not catalytic per se, but important for nuclear targeting and function | Localization to nucleus/nucleolus; interaction with nucleic acids and nuclear machinery | Strong for sequence/functional cell-biology evidence, but not universal catalytic annotation evidence (yang2020jumonjidomain‐containingprotein pages 1-2, yang2020jumonjidomain‐containingprotein pages 2-4) |
| RNA/protein interaction properties | JMJD6 binds single-stranded RNA and interacts with transcription/splicing regulators such as BRD4; these interactions likely help recruit the enzyme to specific nuclear complexes and chromatin-associated functions. | BRD4-binding segment around Lys84-Asn96; RNA-binding capability; AT-hook-like region | Recruitment/regulatory role rather than a separate catalytic class | BRD4 ET domain; spliceosome-associated proteins; ssRNA | Moderate to strong for interaction evidence; catalytic consequences vary by context (konuma2017structuralmechanismof pages 1-2, jablonowski2024metabolicreprogrammingof pages 1-2) |
| Developmental essentiality | Loss of JMJD6 causes severe developmental defects and perinatal/neonatal lethality in mice, indicating conserved organism-level importance; however, these phenotypes are too organism- and context-specific to infer a single universal GO biological process across all family members/taxa. | Not residue-specific; whole-protein loss-of-function phenotype | Indirect evidence of essential biochemical function in development | Embryonic lineage and organogenesis programs | Strong phenotype evidence, but weak for broad family-wide GO process transfer (yang2020jumonjidomain‐containingprotein pages 2-4, ren2024studiesofjmjd6 pages 1-7) |


*Table: This table summarizes the main structural, catalytic, substrate, and localization features currently supported for the JMJD6 family, highlighting where evidence is strong versus controversial. It is useful for judging which family-level functions are safe to transfer in GO annotation review.*

---

## 2. InterPro2GO Mapping Appropriateness

### Current Status: No GO Terms Mapped

PTHR12480 currently has **zero InterPro2GO annotations**. This absence is **inappropriate** given the strong experimental evidence for conserved biochemical activities across the family.

### Recommended Core GO Terms to ADD

**Molecular Function (MF):**
- **GO:0035523 (peptidyl-lysine 5-dioxygenase activity)**: STRONGLY RECOMMENDED. This term accurately reflects the best-supported catalytic function with extensive biochemical validation (cockman2022widespreadhydroxylationof pages 1-2, corner2025biochemicalinvestigationsusing pages 1-3, yang2020jumonjidomain‐containingprotein pages 2-4).
- **GO:0016706 (oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, 2-oxoglutarate as one donor)**: RECOMMENDED. Captures the conserved Fe(II)/2OG-dependent dioxygenase mechanism (cockman2022widespreadhydroxylationof pages 1-2, yang2020jumonjidomain‐containingprotein pages 1-2, corner2025biochemicalinvestigationsusing pages 1-3).
- **GO:0005506 (iron ion binding)**: RECOMMENDED. Structurally validated Fe(II) coordination by the HXD...H motif (yang2020jumonjidomain‐containingprotein pages 1-2, yang2020jumonjidomain‐containingprotein pages 2-4).

**Biological Process (BP):**
- **GO:0018126 (protein hydroxylation)**: RECOMMENDED. Accurately describes the well-supported enzymatic role without overcommitting to specific substrates (cockman2022widespreadhydroxylationof pages 1-2, corner2025biochemicalinvestigationsusing pages 1-3).

**Cellular Component (CC):**
- **GO:0005634 (nucleus)**: RECOMMENDED. JMJD6 contains multiple nuclear localization signals (NLS) and is consistently localized to the nucleus across studies (yang2020jumonjidomain‐containingprotein pages 1-2, yang2020jumonjidomain‐containingprotein pages 2-4, konuma2017structuralmechanismof pages 1-2).

### GO Terms to AVOID

**NOT Recommended - Controversial/Disputed:**
- **GO:0035515 (histone arginine demethylase activity)**: The arginine demethylase assignment is **not robustly supported** by recent biochemical studies and should not be applied at the family level (konuma2017structuralmechanismof pages 1-2, corner2025biochemicalinvestigationsusing pages 1-3, wang2023effectorsandeffects pages 1-2, yang2020jumonjidomain‐containingprotein pages 2-4).

**NOT Recommended - Taxon-Specific:**
- **GO:0007507 (heart development)**, **GO:0009790 (embryo development)**: While JMJD6 deletion causes severe developmental phenotypes in mice (yang2020jumonjidomain‐containingprotein pages 2-4, ren2024studiesofjmjd6 pages 1-7), these are organism-level consequences inappropriate for universal family annotation across 8,924 taxa.

**CAUTION - Context-Dependent:**
- **GO:0008380 (RNA splicing)**, **GO:0000398 (mRNA splicing, via spliceosome)**: JMJD6 regulates alternative splicing in mammalian systems through interactions with U2AF65, RBM39, and effects on AR-V7, Aire, and GLS isoforms (corner2025biochemicalinvestigationsusing pages 1-3, muro2024transcriptsplicingoptimizes pages 1-2, jablonowski2024metabolicreprogrammingof pages 1-2). However, these roles are **strongly documented in vertebrates** but may not be universal across all metazoan clades. Consider for **taxon-restricted child annotations** rather than family-level mapping.

| GO term ID | GO term name | GO aspect | Evidence strength | Rationale for inclusion or exclusion | Recommendation |
|---|---|---|---|---|---|
| GO:0035523 | peptidyl-lysine 5-dioxygenase activity | MF | Strong | Best-supported catalytic activity for JMJD6-family proteins; biochemical and structural work supports Fe(II)/2OG-dependent C5 lysyl hydroxylation, including broad substrate mapping in lysine-rich regions and kinetic assays on BRD-derived substrates. This is the safest family-level catalytic term. (cockman2022widespreadhydroxylationof pages 1-2, corner2025biochemicalinvestigationsusing pages 1-3, yang2020jumonjidomain‐containingprotein pages 2-4) | ADD |
| GO:0016706 | oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, 2-oxoglutarate as one donor, and incorporation of one atom each of oxygen into both donors | MF | Strong | Conserved chemistry of JmjC oxygenases is well supported for JMJD6: Fe(II)- and 2-oxoglutarate-dependent dioxygenase mechanism with O2/ascorbate dependence. Broader than the lysyl hydroxylase term but still mechanistically accurate. (cockman2022widespreadhydroxylationof pages 1-2, yang2020jumonjidomain‐containingprotein pages 1-2, corner2025biochemicalinvestigationsusing pages 1-3) | ADD |
| GO:0005506 | iron ion binding | MF | Strong | Active-site Fe(II) coordination by the conserved HXD...H motif (His187, Asp189, His273 in human JMJD6) is structurally established and required for catalysis. Informative but generic. (yang2020jumonjidomain‐containingprotein pages 1-2, yang2020jumonjidomain‐containingprotein pages 2-4, corner2025biochemicalinvestigationsusing pages 1-3) | ADD |
| GO:0019829 | cation binding | MF | Strong | Technically true but overly generic compared with iron ion binding; adds little information beyond a more specific metal-binding term. (yang2020jumonjidomain‐containingprotein pages 1-2, yang2020jumonjidomain‐containingprotein pages 2-4) | DO_NOT_ADD |
| GO:0016491 | oxidoreductase activity | MF | Strong | True but too generic; the more specific 2-oxoglutarate-dependent dioxygenase term is preferable and more informative for InterPro2GO. (cockman2022widespreadhydroxylationof pages 1-2, corner2025biochemicalinvestigationsusing pages 1-3) | DO_NOT_ADD |
| GO:0035515 | histone arginine demethylase activity | MF | Weak | Early literature proposed JMJD6 as an arginine demethylase, but multiple later biochemical studies failed to robustly confirm direct demethylation by isolated enzyme; recent reviews treat this assignment as controversial. Not safe for all family members. (konuma2017structuralmechanismof pages 1-2, corner2025biochemicalinvestigationsusing pages 1-3, wang2023effectorsandeffects pages 1-2, yang2020jumonjidomain‐containingprotein pages 2-4) | DO_NOT_ADD |
| GO:0016602 | CCAAT-binding factor complex | CC | Weak | Not supported for JMJD6 family; included here as an example of a clearly inappropriate component term unrelated to the family. (yang2020jumonjidomain‐containingprotein pages 1-2, konuma2017structuralmechanismof pages 1-2) | DO_NOT_ADD |
| GO:0042802 | identical protein binding | MF | Moderate | JMJD6 can oligomerize, but this is not a distinctive or useful family annotation and may not be universal across all homologs. Too generic for InterPro2GO. (yang2020jumonjidomain‐containingprotein pages 2-4) | DO_NOT_ADD |
| GO:0018126 | protein hydroxylation | BP | Strong | Fits the well-supported enzymatic role of the family and is broad enough to avoid overcommitting to specific substrates or pathways. Strongly supported by widespread lysyl hydroxylation data. (cockman2022widespreadhydroxylationof pages 1-2, corner2025biochemicalinvestigationsusing pages 1-3) | ADD |
| GO:0006397 | mRNA processing | BP | Moderate | JMJD6 is repeatedly implicated in mRNA splicing/processing through interactions with splicing factors and effects on alternative splicing, but evidence mixes direct catalysis, scaffolding, and context-specific roles. May hold for many animal orthologs but is less certain as a universal family-wide process term across 8924 taxa. (konuma2017structuralmechanismof pages 1-2, muro2024transcriptsplicingoptimizes pages 1-2, jablonowski2024metabolicreprogrammingof pages 1-2) | CAUTION |
| GO:0008380 | RNA splicing | BP | Moderate | Supported in mammalian JMJD6 by functional studies involving U2AF65, RBM39, AR-V7, Aire-related splicing, and GLS isoform control, but these are organism- and context-specific phenotypes rather than a universally demonstrated activity for every family member. (corner2025biochemicalinvestigationsusing pages 1-3, muro2024transcriptsplicingoptimizes pages 1-2, jablonowski2024metabolicreprogrammingof pages 1-2) | CAUTION |
| GO:0000398 | mRNA splicing, via spliceosome | BP | Moderate | Similar issue as RNA splicing: strong evidence in specific vertebrate systems, but likely too specific for all family matches across broad metazoan diversity. Better handled at narrower child entries or gene-level annotation. (corner2025biochemicalinvestigationsusing pages 1-3, jablonowski2024metabolicreprogrammingof pages 1-2) | CAUTION |
| GO:0007507 | heart development | BP | Weak | JMJD6 loss affects embryogenesis and cardiogenesis in mouse studies, but this is highly lineage- and taxon-specific and cannot be generalized to all proteins matched by the family. (ren2024studiesofjmjd6 pages 1-7, yang2020jumonjidomain‐containingprotein pages 2-4) | DO_NOT_ADD |
| GO:0009790 | embryo development | BP | Weak | Developmental phenotypes are strong in mouse knockouts, but they reflect organism-level consequences and are not appropriate as universal family-level GO process terms across all taxa. (yang2020jumonjidomain‐containingprotein pages 2-4, ren2024studiesofjmjd6 pages 1-7) | DO_NOT_ADD |
| GO:0005634 | nucleus | CC | Strong | Nuclear localization is consistently supported for JMJD6, including multiple NLS motifs and nuclear functions in transcription/splicing. Likely appropriate for canonical JMJD6 family proteins. (yang2020jumonjidomain‐containingprotein pages 1-2, yang2020jumonjidomain‐containingprotein pages 2-4, konuma2017structuralmechanismof pages 1-2) | ADD |
| GO:0005730 | nucleolus | CC | Moderate | JMJD6 can shuttle to the nucleolus and the polyserine region influences subnuclear localization, but nucleolar residency appears context-dependent rather than universal. (yang2020jumonjidomain‐containingprotein pages 2-4) | CAUTION |
| GO:0005654 | nucleoplasm | CC | Moderate | Reasonable for canonical JMJD6 proteins, but evidence is less direct than for nucleus and may not improve on the broader nuclear term. (yang2020jumonjidomain‐containingprotein pages 1-2, yang2020jumonjidomain‐containingprotein pages 2-4) | CAUTION |


*Table: This table summarizes candidate GO terms for InterPro family PTHR12480 and evaluates whether each is appropriate at the family level. It distinguishes strong core annotations from controversial or over-specific terms that should be avoided or used only with caution.*

---

## 3. Functional Divergence Across the Family

### Subfamily Structure

PTHR12480 comprises **10 subfamilies** spanning 10,081 proteins across 8,924 taxa (InterPro metadata). The literature on JMJD6 per se does not extensively characterize all 10 subfamilies at the molecular level, but related JmjC proteins reveal functional diversification:

- **JMJD5**: Catalyzes **arginyl C-3 hydroxylation** (not demethylation) on substrates like RCCD1 and ribosomal protein S6 (wilkins2018jmjd5isa pages 1-2). This is a **distinct chemistry** from JMJD6's lysyl C-5 hydroxylation.
- **JMJD7**: A **lysyl hydroxylase** with an unusual **dimeric JmjC fold** structure conserved from Drosophila to humans, targeting DRG1/2 proteins (wilkins2018jmjd5isa pages 1-2).

These observations indicate that while the **core 2OG-dependent oxygenase mechanism is conserved**, the **substrate specificity and modification site** (arginine C-3 vs. lysine C-5) differ among closely related family members (wilkins2018jmjd5isa pages 1-2, liu2022thenovelprotease pages 1-2).

### Catalytically Inactive (Pseudo-Enzyme) Members

No **definitively catalytically dead JMJD6 variants** retaining the fold but lacking activity were identified in the literature. However, some studies note that JMJD6 may have **scaffolding or non-catalytic roles** in addition to enzymatic functions, such as recruiting splicing machinery or transcriptional regulators (konuma2017structuralmechanismof pages 1-2, jablonowski2024metabolicreprogrammingof pages 1-2). The literature does not provide evidence for widespread pseudo-enzyme evolution within PTHR12480 specifically.

### Neo-Functionalization

The **bifunctional activity controversy** (lysyl hydroxylase vs. arginine demethylase) may reflect either: (a) true dual functionality under specific conditions (yang2020jumonjidomain‐containingprotein pages 2-4), or (b) historical misattribution with lysyl hydroxylation being the primary conserved function (cockman2022widespreadhydroxylationof pages 1-2, corner2025biochemicalinvestigationsusing pages 1-3). The current evidence favors the latter. There is no strong evidence for **opposite-function paralogs** (e.g., a demethylase vs. a methylase) within PTHR12480.

---

## 4. Taxonomic Scope

### Distribution Across Clades

PTHR12480 spans **10,081 proteins in 8,924 taxa** (InterPro metadata). The literature confirms JMJD6 homologs in:

- **Mammals** (mice, humans): Extensively studied; essential for embryogenesis with severe neonatal lethality in knockouts (yang2020jumonjidomain‐containingprotein pages 2-4, ren2024studiesofjmjd6 pages 1-7).
- **Invertebrates**: Detected in annelids (Owenia fusiformis, Capitella teleta) and Drosophila melanogaster, where histone-modifying enzyme complements including JMJD6-like proteins are conserved (wilkins2018jmjd5isa pages 1-2).
- **Vertebrates**: Broadly present across fish, birds, and mammals based on phylogenetic studies of 2OG oxygenases in Metazoa (wilkins2018jmjd5isa pages 1-2).

**Not well-represented in plants**: JmjC domain proteins in plants (e.g., Chinese cabbage, Arabidopsis) are primarily **histone lysine demethylases (KDMs)**, not JMJD6-type lysyl hydroxylases (wilkins2018jmjd5isa pages 1-2).

### Taxonomic Validity of Mapped Processes/Components

- **Core oxygenase mechanism (Fe(II)/2OG-dependent)**: Conserved across all metazoan clades represented in PTHR12480.
- **Nuclear localization**: Likely conserved in canonical JMJD6 orthologs across animals (yang2020jumonjidomain‐containingprotein pages 1-2, yang2020jumonjidomain‐containingprotein pages 2-4).
- **Developmental roles**: **Not universal**. While essential in mammals (yang2020jumonjidomain‐containingprotein pages 2-4, ren2024studiesofjmjd6 pages 1-7), specific developmental pathways (e.g., mammalian heart development, thymic T cell selection) are taxon-specific and should not be annotated at the family level.
- **RNA splicing regulation**: Strong in vertebrates (corner2025biochemicalinvestigationsusing pages 1-3, muro2024transcriptsplicingoptimizes pages 1-2, jablonowski2024metabolicreprogrammingof pages 1-2), but whether this holds across invertebrates and all 8,924 taxa is **uncertain**. Splicing-related GO terms require caution for family-level annotation.

---

## 5. Over-Annotation Verdict and GO Action Recommendations

### Verdict: Currently UNDER-ANNOTATED

PTHR12480 has **zero InterPro2GO mappings**, which is **inappropriate** given the robust experimental evidence for conserved biochemical activities. The family is not over-annotating but rather **failing to annotate well-supported core functions**.

### Recommended GO Action Pattern

**Action: ADD Core Annotations**

Apply the following GO terms to PTHR12480:

**Molecular Function:**
- GO:0035523 (peptidyl-lysine 5-dioxygenase activity) – **ADD**
- GO:0016706 (oxidoreductase activity, 2-oxoglutarate-dependent) – **ADD**
- GO:0005506 (iron ion binding) – **ADD**

**Biological Process:**
- GO:0018126 (protein hydroxylation) – **ADD**

**Cellular Component:**
- GO:0005634 (nucleus) – **ADD**

**Action: DO NOT ADD Controversial/Taxon-Specific Terms**

- GO:0035515 (histone arginine demethylase activity) – **DO NOT ADD** (controversial)
- GO:0007507 (heart development), GO:0009790 (embryo development) – **DO NOT ADD** (taxon-specific)
- GO:0008380 (RNA splicing) – **CAUTION / Consider taxon-restricted annotation** (strong in vertebrates, unclear family-wide)

### Recommendations for InterPro

1. **Add the core GO terms** listed above to PTHR12480 to reflect the conserved lysyl hydroxylase and 2OG oxygenase activities.
2. **Consider creating taxon-restricted child entries** for vertebrate-specific JMJD6 orthologs if splicing-related functions are to be annotated, given the strong evidence in mammals but uncertainty across broader taxonomic scope.
3. **Avoid promoting arginine demethylase activity** to the family level until the biochemical controversy is resolved with definitive structural/enzymatic evidence across multiple family members.

### Summary Table

| GO Term | Recommendation | Rationale |
|---------|----------------|-----------|
| GO:0035523 (peptidyl-lysine 5-dioxygenase activity) | **ADD** | Well-supported core catalytic function (cockman2022widespreadhydroxylationof pages 1-2, corner2025biochemicalinvestigationsusing pages 1-3) |
| GO:0016706 (2-oxoglutarate-dependent dioxygenase) | **ADD** | Conserved catalytic mechanism (cockman2022widespreadhydroxylationof pages 1-2, yang2020jumonjidomain‐containingprotein pages 1-2, corner2025biochemicalinvestigationsusing pages 1-3) |
| GO:0005506 (iron ion binding) | **ADD** | Structurally validated (yang2020jumonjidomain‐containingprotein pages 1-2, yang2020jumonjidomain‐containingprotein pages 2-4) |
| GO:0018126 (protein hydroxylation) | **ADD** | Accurate biological process term (cockman2022widespreadhydroxylationof pages 1-2, corner2025biochemicalinvestigationsusing pages 1-3) |
| GO:0005634 (nucleus) | **ADD** | Conserved nuclear localization (yang2020jumonjidomain‐containingprotein pages 1-2, yang2020jumonjidomain‐containingprotein pages 2-4) |
| GO:0035515 (histone arginine demethylase activity) | **REMOVE / DO NOT ADD** | Disputed by multiple studies (konuma2017structuralmechanismof pages 1-2, corner2025biochemicalinvestigationsusing pages 1-3, wang2023effectorsandeffects pages 1-2) |
| GO:0008380 (RNA splicing) | **CAUTION** | Strong in vertebrates, unclear family-wide (corner2025biochemicalinvestigationsusing pages 1-3, muro2024transcriptsplicingoptimizes pages 1-2) |
| GO:0007507 (heart development) | **DO NOT ADD** | Taxon-specific (yang2020jumonjidomain‐containingprotein pages 2-4, ren2024studiesofjmjd6 pages 1-7) |

---

## Experimental Evidence Summary

- **Structural data**: Crystal structures confirm DSBH fold, Fe(II)-binding residues, 2OG-binding pocket (yang2020jumonjidomain‐containingprotein pages 1-2, konuma2017structuralmechanismof pages 1-2, wilkins2018jmjd5isa pages 1-2).
- **Biochemical assays**: Mass spectrometry, kinetic studies, mutagenesis support lysyl hydroxylase activity (cockman2022widespreadhydroxylationof pages 1-2, corner2025biochemicalinvestigationsusing pages 1-3, wilkins2018jmjd5isa pages 1-2).
- **Cellular studies**: JMJD6 knockdown/knockout affects splicing, development, but many phenotypes are context-dependent (muro2024transcriptsplicingoptimizes pages 1-2, yang2020jumonjidomain‐containingprotein pages 2-4, ren2024studiesofjmjd6 pages 1-7, jablonowski2024metabolicreprogrammingof pages 1-2).
- **Disputed claims**: Multiple independent groups failed to confirm arginine demethylase activity with recombinant enzyme (yang2020jumonjidomain‐containingprotein pages 1-2, konuma2017structuralmechanismof pages 1-2, corner2025biochemicalinvestigationsusing pages 1-3, wang2023effectorsandeffects pages 1-2, yang2020jumonjidomain‐containingprotein pages 2-4).

---

## Conclusion

PTHR12480 (JMJD6 family) is a **protein family** with conserved Fe(II)/2OG-dependent dioxygenase activity, specifically **lysyl C-5 hydroxylation**. The current absence of InterPro2GO mappings is inappropriate. **Core molecular function and component terms should be added** based on strong structural and biochemical evidence. However, **arginine demethylase activity** should be excluded due to ongoing controversy, and **developmental/splicing process terms** should be applied with caution or limited to taxon-specific child entries to avoid over-annotation across the family's broad metazoan distribution.

**Final Recommendation:** **ADD core biochemical GO terms** (lysyl hydroxylase, 2OG oxygenase, iron binding, nucleus) while **avoiding controversial demethylase annotations and taxon-specific developmental processes**.

References

1. (manni2022jmjdfamilyproteins pages 1-2): Wang Manni, J. Xue, Hong Weiqi, Siyuan Chen, and Huashan Shi. Jmjd family proteins in cancer and inflammation. Signal Transduction and Targeted Therapy, Sep 2022. URL: https://doi.org/10.1038/s41392-022-01145-1, doi:10.1038/s41392-022-01145-1. This article has 103 citations and is from a peer-reviewed journal.

2. (yang2020jumonjidomain‐containingprotein pages 1-2): Jing Yang, Siyuan Chen, Yanfei Yang, Xuelei Ma, Bin Shao, Shengyong Yang, Yuquan Wei, and Xiawei Wei. Jumonji domain‐containing protein 6 protein and its role in cancer. Cell Proliferation, Jan 2020. URL: https://doi.org/10.1111/cpr.12747, doi:10.1111/cpr.12747. This article has 47 citations and is from a peer-reviewed journal.

3. (cockman2022widespreadhydroxylationof pages 1-2): Matthew E. Cockman, Yoichiro Sugimoto, Hamish B. Pegg, Norma Masson, Eidarus Salah, Anthony Tumber, Helen R. Flynn, Joanna M. Kirkpatrick, Christopher J. Schofield, and Peter J. Ratcliffe. Widespread hydroxylation of unstructured lysine-rich protein domains by jmjd6. Proceedings of the National Academy of Sciences of the United States of America, Aug 2022. URL: https://doi.org/10.1073/pnas.2201483119, doi:10.1073/pnas.2201483119. This article has 33 citations and is from a highest quality peer-reviewed journal.

4. (yang2020jumonjidomain‐containingprotein pages 2-4): Jing Yang, Siyuan Chen, Yanfei Yang, Xuelei Ma, Bin Shao, Shengyong Yang, Yuquan Wei, and Xiawei Wei. Jumonji domain‐containing protein 6 protein and its role in cancer. Cell Proliferation, Jan 2020. URL: https://doi.org/10.1111/cpr.12747, doi:10.1111/cpr.12747. This article has 47 citations and is from a peer-reviewed journal.

5. (paschalis2022jmjd6isa pages 1-2): Alec Paschalis, Jonathan Welti, Antje J. Neeb, Wei Yuan, Ines Figueiredo, Rita Pereira, Ana Ferreira, Ruth Riisnaes, Daniel Nava Rodrigues, Juan M. Jiménez-Vacas, Soojin Kim, Takuma Uo, Patrizio Di Micco, Anthony Tumber, Md. Saiful Islam, Marc A. Moesser, Martine Abboud, Akane Kawamura, Bora Gurel, Rossitza Christova, Veronica S. Gil, Lorenzo Buroni, Mateus Crespo, Susana Miranda, Maryou B. Lambros, Suzanne Carreira, Nina Tunariu, Andrea Alimonti, Bissan Al-Lazikani, Christopher J. Schofield, Stephen R. Plymate, Adam Sharp, and Johann S. de Bono. Jmjd6 is a druggable oxygenase that regulates ar-v7 expression in prostate cancer. Cancer Research, 81:1087-1100, Feb 2022. URL: https://doi.org/10.1158/0008-5472.can-20-1807, doi:10.1158/0008-5472.can-20-1807. This article has 56 citations and is from a highest quality peer-reviewed journal.

6. (wilkins2018jmjd5isa pages 1-2): Sarah E Wilkins, Md Saiful Islam, Joan M Gannon, Suzana Markolovic, Richard J Hopkinson, Wei Ge, Christopher J Schofield, and Rasheduzzaman Chowdhury. Jmjd5 is a human arginyl c-3 hydroxylase. JournalArticle, Jun 2018. URL: https://doi.org/10.17863/cam.54423, doi:10.17863/cam.54423. This article has 66 citations.

7. (corner2025biochemicalinvestigationsusing pages 1-3): Thomas Corner, Eidarus Saleh, Anthony Tumber, Lennart Brewitz, and Christopher J Schofield. Biochemical investigations using mass spectrometry to monitor jmjd6-catalysed hydroxylation of multi-lysine containing bromodomain-derived substrates. RSC Chemical Biology, 6:642-656, Feb 2025. URL: https://doi.org/10.1039/d4cb00311j, doi:10.1039/d4cb00311j. This article has 2 citations and is from a peer-reviewed journal.

8. (konuma2017structuralmechanismof pages 1-2): Tsuyoshi Konuma, Di Yu, Chengcheng Zhao, Ying Ju, Rajal Sharma, Chunyan Ren, Qiang Zhang, Ming-Ming Zhou, and Lei Zeng. Structural mechanism of the oxygenase jmjd6 recognition by the extraterminal (et) domain of brd4. Scientific Reports, Nov 2017. URL: https://doi.org/10.1038/s41598-017-16588-8, doi:10.1038/s41598-017-16588-8. This article has 50 citations and is from a peer-reviewed journal.

9. (wang2023effectorsandeffects pages 1-2): Yalong Wang and Mark T. Bedford. Effectors and effects of arginine methylation. Biochemical Society Transactions, 51:725-734, Apr 2023. URL: https://doi.org/10.1042/bst20221147, doi:10.1042/bst20221147. This article has 33 citations and is from a peer-reviewed journal.

10. (muro2024transcriptsplicingoptimizes pages 1-2): Ryunosuke Muro, Takeshi Nitta, Sachiko Nitta, Masayuki Tsukasaki, Tatsuo Asano, Kenta Nakano, Tadashi Okamura, Tomoki Nakashima, Kazuo Okamoto, and Hiroshi Takayanagi. Transcript splicing optimizes the thymic self-antigen repertoire to suppress autoimmunity. The Journal of Clinical Investigation, Oct 2024. URL: https://doi.org/10.1172/jci179612, doi:10.1172/jci179612. This article has 9 citations.

11. (jablonowski2024metabolicreprogrammingof pages 1-2): Carolyn M Jablonowski, Waise Quarni, Shivendra Singh, Haiyan Tan, Dhanushka Hewa Bostanthirige, Hongjian Jin, Jie Fang, Ti-Cheng Chang, David Finkelstein, Ji-Hoon Cho, Dongli Hu, Vishwajeeth Pagala, Sadie Miki Sakurada, Shondra M Pruett-Miller, Ruoning Wang, Andrew Murphy, Kevin Freeman, Junmin Peng, Andrew M Davidoff, Gang Wu, and Jun Yang. Metabolic reprogramming of cancer cells by jmjd6-mediated pre-mrna splicing associated with therapeutic response to splicing inhibitor. eLife, Mar 2024. URL: https://doi.org/10.7554/elife.90993, doi:10.7554/elife.90993. This article has 17 citations and is from a domain leading peer-reviewed journal.

12. (ren2024studiesofjmjd6 pages 1-7): Yonggang Ren. Studies of jmjd6 in embryogenesis and isl1 phosphorylation in cardiac development. Text, Jan 2024. URL: https://doi.org/10.11588/heidok.00032389, doi:10.11588/heidok.00032389. This article has 0 citations and is from a peer-reviewed journal.

13. (liu2022thenovelprotease pages 1-2): Haolin Liu, Pengcheng Wei, Qianqian Zhang, Zhongzhou Chen, Junfeng Liu, and Gongyi Zhang. The novel protease activities of jmjd5–jmjd6–jmjd7 and arginine methylation activities of arginine methyltransferases are likely coupled. Biomolecules, 12:347, Feb 2022. URL: https://doi.org/10.3390/biom12030347, doi:10.3390/biom12030347. This article has 8 citations.

## Artifacts

- [Edison artifact artifact-00](PTHR12480-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](PTHR12480-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. cockman2022widespreadhydroxylationof pages 1-2
2. corner2025biochemicalinvestigationsusing pages 1-3
3. konuma2017structuralmechanismof pages 1-2
4. manni2022jmjdfamilyproteins pages 1-2
5. wang2023effectorsandeffects pages 1-2
6. muro2024transcriptsplicingoptimizes pages 1-2
7. jablonowski2024metabolicreprogrammingof pages 1-2
8. liu2022thenovelprotease pages 1-2
9. https://doi.org/10.1038/s41392-022-01145-1,
10. https://doi.org/10.1111/cpr.12747,
11. https://doi.org/10.1073/pnas.2201483119,
12. https://doi.org/10.1158/0008-5472.can-20-1807,
13. https://doi.org/10.17863/cam.54423,
14. https://doi.org/10.1039/d4cb00311j,
15. https://doi.org/10.1038/s41598-017-16588-8,
16. https://doi.org/10.1042/bst20221147,
17. https://doi.org/10.1172/jci179612,
18. https://doi.org/10.7554/elife.90993,
19. https://doi.org/10.11588/heidok.00032389,
20. https://doi.org/10.3390/biom12030347,