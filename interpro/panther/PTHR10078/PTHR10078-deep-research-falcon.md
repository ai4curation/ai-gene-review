---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-28T19:39:34.292994'
end_time: '2026-06-28T19:55:51.358278'
duration_seconds: 977.07
template_file: templates/interpro_family_research.md
template_variables:
  interpro_id: PTHR10078
  interpro_name: INTERLEUKIN-1 FAMILY MEMBER
  interpro_short_name: Not specified
  interpro_type: family
  interpro_integrated: IPR000975
  member_databases: Not specified
  n_proteins: '4808'
  n_taxa: '2466'
  n_subfamilies: '12'
  interpro2go_terms: None mapped (no InterPro2GO terms for this entry)
  interpro_description: Not specified in InterPro
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 17
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: PTHR10078-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: PTHR10078-deep-research-falcon_artifacts/artifact-01.md
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
- **Accession:** PTHR10078
- **Name:** INTERLEUKIN-1 FAMILY MEMBER
- **Short name:** Not specified
- **Entry type:** family
- **Integrated into / parent:** IPR000975
- **Member database signatures:** Not specified
- **Scale:** 4808 proteins across 2466 taxa, 12 subfamilies
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
**PTHR10078 (INTERLEUKIN-1 FAMILY MEMBER)**, structured to support GO annotation review.

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
- **Accession:** PTHR10078
- **Name:** INTERLEUKIN-1 FAMILY MEMBER
- **Short name:** Not specified
- **Entry type:** family
- **Integrated into / parent:** IPR000975
- **Member database signatures:** Not specified
- **Scale:** 4808 proteins across 2466 taxa, 12 subfamilies
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
**PTHR10078 (INTERLEUKIN-1 FAMILY MEMBER)**, structured to support GO annotation review.

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


# Comprehensive Research Report: PTHR10078 — INTERLEUKIN-1 FAMILY MEMBER

## 1. Family Definition and Biochemistry

### 1.1 Structural Basis: The β-Trefoil Fold

The PANTHER entry PTHR10078 (INTERLEUKIN-1 FAMILY MEMBER) corresponds to the IL-1 cytokine superfamily, a group of 11 secreted immune-regulatory ligands that share a characteristic β-trefoil fold. This fold comprises 12 anti-parallel β-strands arranged into six β-hairpin motifs that assemble into a pyramidal barrel structure with a central hydrophobic core (wang2025il1superfamilyacross pages 1-3, zhukova2025structuralanddynamic pages 2-3). The mature proteins have molecular weights of approximately 17–18 kDa (wang2025il1superfamilyacross pages 1-3). This structural motif is evolutionarily ancient and is also found in fibroblast growth factors (FGFs) and certain carbohydrate-binding proteins, though distinct amino acid sequences can independently adopt this fold (wang2025il1superfamilyacross pages 1-3, lingel2009structureofil33 pages 1-2).

### 1.2 Conserved Residues and Motifs

A comprehensive evolutionary analysis across more than 400 animal species identified two ultraconserved motifs within the IL-1 β-trefoil domain: "F-F" and "FES-PG-WF" (wang2025il1superfamilyacross pages 11-12, wang2025il1superfamilyacross pages 12-14). These motifs maintain remarkable structural stability throughout evolution. Within these motifs, residue E113 has been identified as functionally critical, and the C-terminal region features a hyperconserved F157 flanked by semi-conserved residues D145, Y147, and E150 (wang2025il1superfamilyacross pages 12-14). The β-trefoil core maintains structural integrity and modulates receptor-binding activity, while N-terminal residues mediate receptor-binding specificity (wang2025il1superfamilyacross pages 12-14).

### 1.3 Receptor-Ligand Signaling Mechanism

IL-1 family cytokines signal through a conserved mechanism involving heterotrimeric receptor complex assembly. Agonist ligands bind a primary receptor (IL-1R1, ST2/IL-1R4, IL-18Rα/IL-1R5, or IL-36R/IL-1R6), which recruits a shared coreceptor, most commonly IL-1RAcP/IL-1R3 (frenay2022il1rapakey pages 6-8, frenay2022il1rapakey pages 4-6, lingel2009structureofil33 pages 1-2). Upon complex formation, intracellular TIR (Toll/IL-1 Receptor) domains juxtapose, creating a platform that recruits the adaptor protein MyD88, which oligomerizes into a "Myddosome" signaling hub (zhukova2025structuralanddynamic pages 7-8). This triggers a cascade involving IRAK4, IRAK1/2, and TRAF6, ultimately activating NF-κB and MAPK (p38, JNK, ERK1/2) pathways and inducing AP-1 transcription factor activity (frenay2022il1rapakey pages 6-8, wang2025blockadeofil1 pages 5-7, xie2020il38anew pages 4-6).

Critically, receptor antagonists such as IL-1Ra bind only to Site A of IL-1R1 (via Domains 1 and 2) but fail to engage Site B and Domain 3, thereby preventing productive coreceptor recruitment and maintaining the receptor in an "open" non-signaling conformation (zhukova2025structuralanddynamic pages 3-5). This mechanistic distinction between agonist and antagonist binding is central to understanding the functional heterogeneity of the family.

### 1.4 IL-1 Family Members and Classification

The following table comprehensively summarizes all 11 canonical IL-1 family ligands:

| Member name | Old nomenclature | Subfamily | Function | Primary receptor | Coreceptor | Taxonomic distribution | Evidence |
|---|---|---|---|---|---|---|---|
| IL-1α | IL-1F1 | IL-1 | Agonist | IL-1R1 | IL-1RAcP (IL-1R3) | Neo-IL-1; reported as mammalian-specific in recent broad evolutionary analysis | (wang2025blockadeofil1 pages 5-7, frenay2022il1rapakey pages 6-8, wang2025il1superfamilyacross pages 3-4, wang2025il1superfamilyacross pages 8-11) |
| IL-1β | IL-1F2 | IL-1 | Agonist | IL-1R1 | IL-1RAcP (IL-1R3) | Ancient IL-1; vertebrate-wide, including fish, birds, reptiles, mammals | (wang2025blockadeofil1 pages 5-7, zhukova2025structuralanddynamic pages 3-5, frenay2022il1rapakey pages 6-8, wang2025il1superfamilyacross pages 3-4, gibson2014thechickenil1 pages 9-11) |
| IL-1Ra | IL-1F3 | IL-1 | Antagonist | IL-1R1 | None for signaling; blocks productive IL-1RAcP recruitment | Paleo-IL-1; present from reptiles through mammals; identified in chicken and other non-mammalian vertebrates | (wang2025blockadeofil1 pages 5-7, zhukova2025structuralanddynamic pages 3-5, zhukova2025structuralanddynamic pages 1-2, wang2025il1superfamilyacross pages 6-8, gibson2014thechickenil1 pages 9-11) |
| IL-18 | IL-1F4 | IL-18 | Agonist | IL-18Rα (IL-1R5) | IL-18Rβ (IL-1R7) | Ancient IL-1; vertebrate-wide, including teleost fish | (wang2025blockadeofil1 pages 5-7, chauhan2020therapeuticmodulationof pages 4-6, garlanda2025il1familycytokines pages 1-2, wang2025il1superfamilyacross pages 3-4, wang2025il1superfamilyacross pages 6-8) |
| IL-36Ra | IL-1F5 | IL-36 | Antagonist | IL-36R (IL-1R6/IL-1RL2) | None for signaling; blocks productive IL-1RAcP recruitment | Neo-IL-1/IL-36 branch; generally treated as mammalian-specific in recent evolutionary synthesis | (wang2025blockadeofil1 pages 5-7, gao2024emergingfunctionsand pages 13-13, wang2025il1superfamilyacross pages 6-8, wang2025il1superfamilyacross pages 8-11) |
| IL-36α | IL-1F6 | IL-36 | Agonist | IL-36R (IL-1R6/IL-1RL2) | IL-1RAcP (IL-1R3) | Neo-IL-1/IL-36 branch; mammalian-specific | (wang2025blockadeofil1 pages 5-7, frenay2022il1rapakey pages 6-8, wang2025il1superfamilyacross pages 6-8, wang2025il1superfamilyacross pages 8-11) |
| IL-37 | IL-1F7 | IL-18 | Anti-inflammatory cytokine | IL-18Rα (IL-1R5) | SIGIRR/TIR8 (IL-1R8) | Neo-IL-1; mammalian-specific | (wang2025blockadeofil1 pages 5-7, xie2020il38anew pages 1-3, garlanda2025il1familycytokines pages 1-2, wang2025il1superfamilyacross pages 6-8) |
| IL-36β | IL-1F8 | IL-36 | Agonist | IL-36R (IL-1R6/IL-1RL2) | IL-1RAcP (IL-1R3) | Neo-IL-1/IL-36 branch; mammalian-specific | (wang2025blockadeofil1 pages 5-7, frenay2022il1rapakey pages 6-8, wang2025il1superfamilyacross pages 6-8, wang2025il1superfamilyacross pages 8-11) |
| IL-36γ | IL-1F9 | IL-36 | Agonist | IL-36R (IL-1R6/IL-1RL2) | IL-1RAcP (IL-1R3) | Neo-IL-1/IL-36 branch; mammalian-specific | (wang2025blockadeofil1 pages 5-7, frenay2022il1rapakey pages 6-8, wang2025il1superfamilyacross pages 6-8, wang2025il1superfamilyacross pages 8-11) |
| IL-38 | IL-1F10 | IL-36 | Antagonist / anti-inflammatory, context-dependent | IL-36R; also reported for IL-1RAPL1 and IL-1R1 | None clearly established as obligate signaling coreceptor for inhibitory function | Paleo-IL-1; present from reptiles through mammals | (xie2020il38anew pages 3-4, xie2020il38anew pages 1-3, xie2020il38anew pages 4-6, gao2024emergingfunctionsand pages 13-13, wang2025il1superfamilyacross pages 6-8) |
| IL-33 | IL-1F11 | IL-1 | Agonist with context-dependent dual biology | ST2 (IL-1R4/IL-1RL1) | IL-1RAcP (IL-1R3) | Often reported as mammalian-specific in recent evolutionary syntheses; earlier comparative work noted ST2 in birds but no confirmed avian IL-33 ligand | (wang2025blockadeofil1 pages 5-7, cayrol2021il33analarmin pages 3-5, lingel2009structureofil33 pages 1-2, gibson2014thechickenil1 pages 9-11, wang2025il1superfamilyacross pages 8-11) |


*Table: This table summarizes all 11 canonical IL-1 family ligands, their legacy IL-1F nomenclature, receptor usage, functional class, and evolutionary distribution. It is useful for GO review because it makes the family’s strong functional heterogeneity and lineage restriction explicit.*

The family comprises three subfamilies organized by receptor usage: the IL-1 subfamily (IL-1α, IL-1β, IL-1Ra, IL-33), the IL-36 subfamily (IL-36α/β/γ, IL-36Ra, IL-38), and the IL-18 subfamily (IL-18, IL-37) (wang2025blockadeofil1 pages 5-7, garlanda2025il1familycytokines pages 1-2). The IL-1 receptor family itself comprises 11 members (IL-1R1 through IL-1R10), forming five functional signaling complexes (garlanda2025il1familycytokines pages 1-2).

---

## 2. InterPro2GO Mapping Appropriateness

### 2.1 Current Status

PTHR10078 currently has **no InterPro2GO terms mapped**. This entry is integrated into the parent InterPro entry IPR000975 and represents a PANTHER family-level classification encompassing 4,808 proteins across 2,466 taxa with 12 subfamilies.

### 2.2 Assessment of Candidate GO Terms

Given the family's extreme functional heterogeneity, the absence of mapped GO terms is well-justified. The following table evaluates the most plausible candidate GO terms:

| GO ID | GO Term Name | Aspect | Appropriate for all PTHR10078 members? | Specific issues for this family | Recommendation |
|---|---|---|---|---|---|
| GO:0005125 | cytokine activity | F | No | Over-broad for the family. Several IL-1 family members are agonists, but IL-1Ra and IL-36Ra are receptor antagonists, and IL-37/IL-38 are primarily anti-inflammatory/regulatory rather than canonical pro-inflammatory cytokine agonists. A family-wide assignment would therefore conflate agonists with antagonists and suppressors. (wang2025blockadeofil1 pages 5-7, xie2020il38anew pages 1-3, zhukova2025structuralanddynamic pages 3-5, garlanda2025il1familycytokines pages 1-2) | REMOVE / do not add at this family level; if used, move to agonist-specific child entries |
| GO:0005149 | interleukin-1 receptor binding | F | No | Closer than most candidates, but still not uniformly true in a single specific sense across the family. Members bind different primary receptors: IL-1α/β and IL-1Ra bind IL-1R1, IL-33 binds ST2/IL-1R4, IL-36 agonists and IL-36Ra bind IL-36R/IL-1R6, IL-18 binds IL-18Rα/IL-1R5, and IL-37 signals via IL-18Rα plus IL-1R8. Thus one receptor-binding term risks collapsing distinct receptor specificities. (frenay2022il1rapakey pages 6-8, cayrol2021il33analarmin pages 3-5, lingel2009structureofil33 pages 1-2, garlanda2025il1familycytokines pages 1-2) | MODIFY-to-specific on child entries only; do not add to PTHR10078 |
| GO:0006954 | inflammatory response | P | No | Not valid for all members. Agonists such as IL-1α, IL-1β, IL-18, IL-33, and IL-36α/β/γ promote inflammatory programs, but IL-1Ra, IL-36Ra, IL-37, and IL-38 counteract or dampen inflammation. Family-wide process annotation would therefore encode opposite biological effects under one term. (xie2020il38anew pages 3-4, wang2025blockadeofil1 pages 5-7, xie2020il38anew pages 1-3, chauhan2020therapeuticmodulationof pages 4-6, garlanda2025il1familycytokines pages 1-2) | REMOVE / do not add at this family level; use positive or negative regulation terms on appropriate subfamilies |
| GO:0005576 | extracellular region | C | No | Many IL-1 family proteins are secreted or released extracellularly, but this is not sufficient to make the term safe for every member in every biological context. IL-33 has well-established nuclear residence and alarmin behavior, and IL-1α also has intracellular/nuclear roles; a blanket component term would miss this context dependence and could overstate constitutive extracellular localization. (wang2025blockadeofil1 pages 5-7, cayrol2021il33analarmin pages 3-5, lingel2009structureofil33 pages 1-2) | KEEP_AS_NON_CORE at most for more specific child groups; not recommended for the whole family |
| GO:0005615 | extracellular space | C | No | Same core problem as extracellular region, but even more specific. While many mature ligands act in extracellular space, some family members have important intracellular or nuclear localization/function before release, especially IL-33 and IL-1α. This makes the term unsafe as a universal family-level annotation. (wang2025blockadeofil1 pages 5-7, cayrol2021il33analarmin pages 3-5, lingel2009structureofil33 pages 1-2) | REMOVE / do not add at this family level; consider only for experimentally supported specific proteins or homogeneous child entries |


*Table: This table evaluates plausible GO terms that might be considered for the IL-1 family entry PTHR10078 and explains why none are reliably valid across the entire family. It is useful for showing that the current absence of InterPro2GO mappings is justified by strong functional and localization heterogeneity.*

### 2.3 Rationale for No Mapping

The fundamental challenge is that the IL-1 family includes both **agonists** (IL-1α, IL-1β, IL-18, IL-33, IL-36α/β/γ) that activate pro-inflammatory NF-κB/MAPK signaling and **antagonists** (IL-1Ra, IL-36Ra) that specifically block receptor activation and prevent signaling (wang2025blockadeofil1 pages 5-7, zhukova2025structuralanddynamic pages 3-5, garlanda2025il1familycytokines pages 1-2). Additionally, IL-37 functions as an anti-inflammatory cytokine suppressing iNOS, IL-6, and ROS while promoting IL-10 and Treg differentiation (wang2025blockadeofil1 pages 5-7), and IL-38 exhibits concentration-dependent dual behavior—anti-inflammatory at low concentrations but potentially pro-inflammatory at higher concentrations (xie2020il38anew pages 3-4, xie2020il38anew pages 4-6). IL-33 itself has context-dependent dual roles, acting as anti-inflammatory in acute phases by activating Tregs but shifting to pro-inflammatory dominance in chronic disease (wang2025blockadeofil1 pages 5-7).

No single Molecular Function, Biological Process, or Cellular Component GO term can accurately capture the biology of every protein matched by this signature. The only truly shared property is the β-trefoil fold structure, but there is no GO term for "β-trefoil fold" (this is a structural classification, not a functional annotation).

---

## 3. Functional Divergence Across the Family

### 3.1 Agonist–Antagonist Neo-functionalization

The most striking functional divergence within the IL-1 family is the evolution of receptor antagonists from agonist ancestors. IL-1Ra and IL-36Ra bind the same primary receptors as their corresponding agonists (IL-1R1 and IL-36R, respectively) but fail to recruit the coreceptor IL-1RAcP, thereby competitively blocking signaling without initiating it (zhukova2025structuralanddynamic pages 3-5, chauhan2020therapeuticmodulationof pages 4-6). This represents a clear case of neo-functionalization: proteins that retain the fold and receptor-binding capacity but have acquired diametrically opposite biological effects.

### 3.2 Anti-inflammatory Cytokines vs. Pro-inflammatory Agonists

IL-37 functions through a unique mechanism: it binds IL-18Rα (IL-1R5) but partners with SIGIRR/TIR8 (IL-1R8) rather than IL-18Rβ (IL-1R7), resulting in anti-inflammatory rather than pro-inflammatory signaling (garlanda2025il1familycytokines pages 1-2). This is functionally opposite to IL-18, which uses the same primary receptor but with a different coreceptor. Similarly, IL-38 predominantly acts as an anti-inflammatory agent by antagonizing IL-36R and IL-1R1, reducing IL-17A, IL-22, and IL-8 production analogously to IL-1Ra and IL-36Ra (xie2020il38anew pages 3-4, xie2020il38anew pages 1-3).

### 3.3 Alarmin vs. Classical Cytokine Function

IL-33 and IL-1α function as dual-function alarmins: they reside in the nucleus under homeostatic conditions and are passively released upon tissue damage or cell necrosis, acting as danger signals rather than conventionally secreted cytokines (cayrol2021il33analarmin pages 3-5). This contrasts sharply with IL-1β and IL-18, which require active processing by caspase-1 within the inflammasome pathway before secretion (chauhan2020therapeuticmodulationof pages 4-6). IL-33 possesses a unique domain architecture, containing an IL33_bt domain rather than the canonical IL1 domain found in most other family members (wang2025il1superfamilyacross pages 8-11).

### 3.4 Decoy Receptor Regulation

Beyond the ligands themselves, the IL-1 system includes decoy receptors (IL-1R2) that bind IL-1β without signaling, and soluble binding proteins (IL-18BP) that sequester IL-18 extracellularly (zhukova2025structuralanddynamic pages 3-5, chauhan2020therapeuticmodulationof pages 4-6). These negative regulators are structurally distinct from the ligand family but functionally integral to the system.

### 3.5 Concentration-Dependent Effects

IL-38 demonstrates particularly striking context-dependency. At low concentrations, truncated IL-38 exhibits anti-inflammatory properties by antagonizing IL-1R1 and IL-36R. However, at higher concentrations, IL-38 can promote pro-inflammatory cytokine production, potentially through dimerization-induced loss of antagonist activity (xie2020il38anew pages 3-4, xie2020il38anew pages 4-6).

---

## 4. Taxonomic Scope

### 4.1 Evolutionary Phases

A landmark 2025 analysis across 402 animal species representing 396 species identified three evolutionary phases of IL-1 family expansion (wang2025il1superfamilyacross pages 12-14, wang2025il1superfamilyacross pages 6-8):

- **Ancient IL-1s** (~420 Mya): IL-1β and IL-18 are the oldest family members, present in all vertebrates including teleost fish (wang2025il1superfamilyacross pages 3-4). These originated before the divergence of bony and cartilaginous fish.

- **Paleo-IL-1s** (~365–320 Mya): IL-1Ra and IL-38 emerged with terrestrial oviparous vertebrates and are present from reptiles through mammals. IL-1Ra homologs have been identified in chicken and rainbow trout (wang2025il1superfamilyacross pages 6-8, gibson2014thechickenil1 pages 9-11).

- **Neo-IL-1s** (~160 Mya): IL-1α, IL-37, IL-36 subfamily, and IL-33 are mammalian-specific innovations. IL-1α arose from IL-1β duplication between 320–160 Mya. IL-36α/β/γ also arose from IL-1β duplication events, generating the nine-gene IL-1 cluster on mammalian chromosome 2 (wang2025il1superfamilyacross pages 8-11, wang2025il1superfamilyacross pages 6-8, wang2025il1superfamilyacross pages 12-14).

### 4.2 Non-Mammalian Representation

The chicken genome possesses all IL-1 receptor genes found in mammals but only 4 of 11 IL-1 ligand genes, with just a single IL-1 gene (IL-1β) at the syntenic ligand cluster locus (gibson2014thechickenil1 pages 5-8). Notably, despite the presence of the ST2/IL-1R4 receptor in chickens, the IL-33 ligand has not been identified in birds (gibson2014thechickenil1 pages 9-11, gibson2014thechickenil1 pages 5-8). In teleost fish, IL-1β homologs are abundant but IL-18 is virtually absent from the immune system despite having homologs in the genome (wang2025il1superfamilyacross pages 6-8). Non-vertebrate IL-1R-like orthologs have been identified in Cnidaria, Protostomia, and Deuterostomia, though these are receptor homologs rather than ligand family members (wang2025il1superfamilyacross pages 12-14).

### 4.3 Implications for GO Annotation

The broad taxonomic distribution (4,808 proteins across 2,466 taxa) means this PANTHER family encompasses proteins from fish, birds, reptiles, and mammals. Many mammalian-specific GO process terms (e.g., those involving IL-33/ST2 signaling or IL-36 subfamily functions) would not apply to the fish and avian members of this signature. Conversely, the ancestral pro-inflammatory cytokine function of IL-1β is conserved across vertebrates but is not shared by the antagonist members (wang2025il1superfamilyacross pages 3-4, wang2025il1superfamilyacross pages 6-8).

---

## 5. Over-Annotation Verdict

### 5.1 Summary Assessment

The current InterPro2GO status of PTHR10078—**no mapped GO terms**—is **appropriate and sound**. This is one of the rare cases where the absence of annotation is the correct decision, driven by three converging factors:

1. **Extreme functional heterogeneity**: The family contains pro-inflammatory agonists, receptor antagonists, anti-inflammatory cytokines, and dual-function alarmins that exert diametrically opposite biological effects (wang2025blockadeofil1 pages 5-7, xie2020il38anew pages 1-3, garlanda2025il1familycytokines pages 1-2).

2. **Divergent receptor usage**: Members bind five different primary receptors (IL-1R1, ST2, IL-18Rα, IL-36R) with different coreceptors, making a single "receptor binding" GO term misleading (frenay2022il1rapakey pages 6-8, garlanda2025il1familycytokines pages 1-2).

3. **Wide taxonomic scope with lineage-specific members**: The 4,808 proteins span vertebrates from fish to mammals, but many family members (IL-33, IL-36, IL-37, IL-1α) are mammalian-specific innovations. Process terms that apply to mammalian agonists would be incorrect for non-mammalian or antagonist members (wang2025il1superfamilyacross pages 3-4, wang2025il1superfamilyacross pages 6-8, gibson2014thechickenil1 pages 5-8).

### 5.2 Recommended GO Action Pattern

| Recommendation | Action |
|---|---|
| **For PTHR10078 (family level)** | **ACCEPT** the current state of no InterPro2GO mappings. No GO term is universally valid across this functionally heterogeneous family. |
| **For subfamily-level child entries** | **MODIFY-to-specific**: GO annotations should be applied at the subfamily/child entry level where functional homogeneity is sufficient. For example, agonist-specific subfamilies could receive GO:0005125 (cytokine activity) and GO:0006954 (inflammatory response), while IL-1Ra/IL-36Ra subfamilies could receive GO:0004866 (endopeptidase inhibitor activity is incorrect; more appropriate would be a receptor antagonist term) or GO:0030292 (negative regulation of inflammatory response). |
| **For InterPro itself** | Consider ensuring that the 12 subfamilies within PTHR10078 are well-delineated to support subfamily-level GO annotation. The agonist/antagonist split is the most critical functional boundary. |

### 5.3 Specific Recommendations for Hypothetical GO Terms

- **GO:0005125 (cytokine activity)**: Do NOT add at family level. Only valid for agonist subfamilies. IL-1Ra and IL-36Ra are not cytokines in the agonist sense; they are competitive receptor antagonists (zhukova2025structuralanddynamic pages 3-5, zhukova2025structuralanddynamic pages 1-2).
- **GO:0006954 (inflammatory response)**: Do NOT add at family level. Would incorrectly annotate anti-inflammatory members (IL-37, IL-38, IL-1Ra) as pro-inflammatory (xie2020il38anew pages 3-4, wang2025blockadeofil1 pages 5-7).
- **GO:0005576 (extracellular region)**: Do NOT add at family level. IL-33 and IL-1α have critical nuclear/intracellular functions as alarmins (cayrol2021il33analarmin pages 3-5).
- **GO:0005149 (interleukin-1 receptor binding)**: Do NOT add at family level. Members bind distinct receptor types (IL-1R1, ST2, IL-18Rα, IL-36R) (frenay2022il1rapakey pages 6-8, garlanda2025il1familycytokines pages 1-2).

In conclusion, PTHR10078 represents a textbook example of a protein family where functional divergence through neo-functionalization (agonists evolving into antagonists), combined with lineage-restricted subfamily expansion, makes family-level GO annotation inappropriate. The current absence of InterPro2GO mappings should be maintained, with annotation efforts directed to child entries representing functionally homogeneous subfamilies.

References

1. (wang2025il1superfamilyacross pages 1-3): Weibin Wang, Dawei Li, Kai-yong Luo, Baozheng Chen, Tingting Hao, Xuzhen Li, Dazhong Guo, Yang Dong, and Ya Ning. Il-1 superfamily across 400+ species: therapeutic targets and disease implications. Biology, 14:561, May 2025. URL: https://doi.org/10.3390/biology14050561, doi:10.3390/biology14050561. This article has 2 citations.

2. (zhukova2025structuralanddynamic pages 2-3): J. Zhukova, J. Lopatnikova, S. Sennikov, R. C. Russo, Cecilia Garlanda, Bernhard Ryffel, and Gaby Palmer. Structural and dynamic properties of il1 receptors. Frontiers in Immunology, Dec 2025. URL: https://doi.org/10.3389/fimmu.2025.1714624, doi:10.3389/fimmu.2025.1714624. This article has 6 citations and is from a peer-reviewed journal.

3. (lingel2009structureofil33 pages 1-2): Andreas Lingel, Thomas M. Weiss, M. Niebuhr, B. Pan, B. Appleton, C. Wiesmann, J. Bazan, and Wayne J. Fairbrother. The structure of interleukin-33 and its interaction with the st2 and il-1racp receptors – insight into the arrangement of heterotrimeric interleukin-1 signaling complexes. Structure (London, England : 1993), 17:1398-1410, Oct 2009. URL: https://doi.org/10.1016/j.str.2009.08.009, doi:10.1016/j.str.2009.08.009. This article has 195 citations.

4. (wang2025il1superfamilyacross pages 11-12): Weibin Wang, Dawei Li, Kai-yong Luo, Baozheng Chen, Tingting Hao, Xuzhen Li, Dazhong Guo, Yang Dong, and Ya Ning. Il-1 superfamily across 400+ species: therapeutic targets and disease implications. Biology, 14:561, May 2025. URL: https://doi.org/10.3390/biology14050561, doi:10.3390/biology14050561. This article has 2 citations.

5. (wang2025il1superfamilyacross pages 12-14): Weibin Wang, Dawei Li, Kai-yong Luo, Baozheng Chen, Tingting Hao, Xuzhen Li, Dazhong Guo, Yang Dong, and Ya Ning. Il-1 superfamily across 400+ species: therapeutic targets and disease implications. Biology, 14:561, May 2025. URL: https://doi.org/10.3390/biology14050561, doi:10.3390/biology14050561. This article has 2 citations.

6. (frenay2022il1rapakey pages 6-8): Jame Frenay, Pierre-Simon Bellaye, Alexandra Oudot, Alex Helbling, Camille Petitot, Christophe Ferrand, Bertrand Collin, and Alexandre M. M. Dias. Il-1rap, a key therapeutic target in cancer. International Journal of Molecular Sciences, 23:14918, Nov 2022. URL: https://doi.org/10.3390/ijms232314918, doi:10.3390/ijms232314918. This article has 33 citations.

7. (frenay2022il1rapakey pages 4-6): Jame Frenay, Pierre-Simon Bellaye, Alexandra Oudot, Alex Helbling, Camille Petitot, Christophe Ferrand, Bertrand Collin, and Alexandre M. M. Dias. Il-1rap, a key therapeutic target in cancer. International Journal of Molecular Sciences, 23:14918, Nov 2022. URL: https://doi.org/10.3390/ijms232314918, doi:10.3390/ijms232314918. This article has 33 citations.

8. (zhukova2025structuralanddynamic pages 7-8): J. Zhukova, J. Lopatnikova, S. Sennikov, R. C. Russo, Cecilia Garlanda, Bernhard Ryffel, and Gaby Palmer. Structural and dynamic properties of il1 receptors. Frontiers in Immunology, Dec 2025. URL: https://doi.org/10.3389/fimmu.2025.1714624, doi:10.3389/fimmu.2025.1714624. This article has 6 citations and is from a peer-reviewed journal.

9. (wang2025blockadeofil1 pages 5-7): Kexin Wang, Haoge Luo, Liping Liu, Hang Gao, Yanyan Song, and Dong Li. Blockade of il-1 family cytokines in the treatment of rheumatoid arthritis. Frontiers in Pharmacology, May 2025. URL: https://doi.org/10.3389/fphar.2025.1577628, doi:10.3389/fphar.2025.1577628. This article has 29 citations.

10. (xie2020il38anew pages 4-6): Lihui Xie, Zhaohao Huang, He Li, Xiuxing Liu, Song Guo Zheng, and Wenru Su. Il-38: a new player in inflammatory autoimmune disorders. Biomolecules, 9:345, Aug 2020. URL: https://doi.org/10.3390/biom9080345, doi:10.3390/biom9080345. This article has 103 citations.

11. (zhukova2025structuralanddynamic pages 3-5): J. Zhukova, J. Lopatnikova, S. Sennikov, R. C. Russo, Cecilia Garlanda, Bernhard Ryffel, and Gaby Palmer. Structural and dynamic properties of il1 receptors. Frontiers in Immunology, Dec 2025. URL: https://doi.org/10.3389/fimmu.2025.1714624, doi:10.3389/fimmu.2025.1714624. This article has 6 citations and is from a peer-reviewed journal.

12. (wang2025il1superfamilyacross pages 3-4): Weibin Wang, Dawei Li, Kai-yong Luo, Baozheng Chen, Tingting Hao, Xuzhen Li, Dazhong Guo, Yang Dong, and Ya Ning. Il-1 superfamily across 400+ species: therapeutic targets and disease implications. Biology, 14:561, May 2025. URL: https://doi.org/10.3390/biology14050561, doi:10.3390/biology14050561. This article has 2 citations.

13. (wang2025il1superfamilyacross pages 8-11): Weibin Wang, Dawei Li, Kai-yong Luo, Baozheng Chen, Tingting Hao, Xuzhen Li, Dazhong Guo, Yang Dong, and Ya Ning. Il-1 superfamily across 400+ species: therapeutic targets and disease implications. Biology, 14:561, May 2025. URL: https://doi.org/10.3390/biology14050561, doi:10.3390/biology14050561. This article has 2 citations.

14. (gibson2014thechickenil1 pages 9-11): Mark S. Gibson, Pete Kaiser, and Mark Fife. The chicken il-1 family: evolution in the context of the studied vertebrate lineage. Immunogenetics, 66:427-438, May 2014. URL: https://doi.org/10.1007/s00251-014-0780-7, doi:10.1007/s00251-014-0780-7. This article has 37 citations and is from a peer-reviewed journal.

15. (zhukova2025structuralanddynamic pages 1-2): J. Zhukova, J. Lopatnikova, S. Sennikov, R. C. Russo, Cecilia Garlanda, Bernhard Ryffel, and Gaby Palmer. Structural and dynamic properties of il1 receptors. Frontiers in Immunology, Dec 2025. URL: https://doi.org/10.3389/fimmu.2025.1714624, doi:10.3389/fimmu.2025.1714624. This article has 6 citations and is from a peer-reviewed journal.

16. (wang2025il1superfamilyacross pages 6-8): Weibin Wang, Dawei Li, Kai-yong Luo, Baozheng Chen, Tingting Hao, Xuzhen Li, Dazhong Guo, Yang Dong, and Ya Ning. Il-1 superfamily across 400+ species: therapeutic targets and disease implications. Biology, 14:561, May 2025. URL: https://doi.org/10.3390/biology14050561, doi:10.3390/biology14050561. This article has 2 citations.

17. (chauhan2020therapeuticmodulationof pages 4-6): Dhruv Chauhan, Lieselotte Vande Walle, and Mohamed Lamkanfi. Therapeutic modulation of inflammasome pathways. Immunological Reviews, 297:123-138, Aug 2020. URL: https://doi.org/10.1111/imr.12908, doi:10.1111/imr.12908. This article has 224 citations and is from a domain leading peer-reviewed journal.

18. (garlanda2025il1familycytokines pages 1-2): Cecilia Garlanda, Irene Di Ceglie, and Sebastien Jaillon. Il-1 family cytokines in inflammation and immunity. Cellular &amp; Molecular Immunology, 22(11):1345-1362, Oct 2025. URL: https://doi.org/10.1038/s41423-025-01358-8, doi:10.1038/s41423-025-01358-8. This article has 80 citations and is from a peer-reviewed journal.

19. (gao2024emergingfunctionsand pages 13-13): Yuan Gao, Luwei Cai, Yulu Wu, Min Jiang, Yidan Zhang, Wenjing Ren, Yirui Song, Lili Li, Ziguang Lei, Youzhuang Wu, Luwen Zhu, Jing Li, Dongya Li, Guohong Li, Chengliang Luo, and Luyang Tao. Emerging functions and therapeutic targets of il‐38 in central nervous system diseases. CNS Neuroscience & Therapeutics, Feb 2024. URL: https://doi.org/10.1111/cns.14550, doi:10.1111/cns.14550. This article has 13 citations and is from a peer-reviewed journal.

20. (xie2020il38anew pages 1-3): Lihui Xie, Zhaohao Huang, He Li, Xiuxing Liu, Song Guo Zheng, and Wenru Su. Il-38: a new player in inflammatory autoimmune disorders. Biomolecules, 9:345, Aug 2020. URL: https://doi.org/10.3390/biom9080345, doi:10.3390/biom9080345. This article has 103 citations.

21. (xie2020il38anew pages 3-4): Lihui Xie, Zhaohao Huang, He Li, Xiuxing Liu, Song Guo Zheng, and Wenru Su. Il-38: a new player in inflammatory autoimmune disorders. Biomolecules, 9:345, Aug 2020. URL: https://doi.org/10.3390/biom9080345, doi:10.3390/biom9080345. This article has 103 citations.

22. (cayrol2021il33analarmin pages 3-5): Corinne Cayrol. Il-33, an alarmin of the il-1 family involved in allergic and non allergic inflammation: focus on the mechanisms of regulation of its activity. Cells, 11:107, Dec 2021. URL: https://doi.org/10.3390/cells11010107, doi:10.3390/cells11010107. This article has 114 citations.

23. (gibson2014thechickenil1 pages 5-8): Mark S. Gibson, Pete Kaiser, and Mark Fife. The chicken il-1 family: evolution in the context of the studied vertebrate lineage. Immunogenetics, 66:427-438, May 2014. URL: https://doi.org/10.1007/s00251-014-0780-7, doi:10.1007/s00251-014-0780-7. This article has 37 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](PTHR10078-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](PTHR10078-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. zhukova2025structuralanddynamic pages 7-8
2. zhukova2025structuralanddynamic pages 3-5
3. chauhan2020therapeuticmodulationof pages 4-6
4. zhukova2025structuralanddynamic pages 2-3
5. zhukova2025structuralanddynamic pages 1-2
6. gao2024emergingfunctionsand pages 13-13
7. https://doi.org/10.3390/biology14050561,
8. https://doi.org/10.3389/fimmu.2025.1714624,
9. https://doi.org/10.1016/j.str.2009.08.009,
10. https://doi.org/10.3390/ijms232314918,
11. https://doi.org/10.3389/fphar.2025.1577628,
12. https://doi.org/10.3390/biom9080345,
13. https://doi.org/10.1007/s00251-014-0780-7,
14. https://doi.org/10.1111/imr.12908,
15. https://doi.org/10.1038/s41423-025-01358-8,
16. https://doi.org/10.1111/cns.14550,
17. https://doi.org/10.3390/cells11010107,