---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-21T19:49:59.139856'
end_time: '2026-06-21T20:02:02.182549'
duration_seconds: 723.04
template_file: templates/interpro_family_research.md
template_variables:
  interpro_id: PTHR10807
  interpro_name: MYOTUBULARIN-RELATED
  interpro_short_name: Not specified
  interpro_type: family
  interpro_integrated: IPR030564
  member_databases: Not specified
  n_proteins: '30741'
  n_taxa: '8904'
  n_subfamilies: '34'
  interpro2go_terms: None mapped (no InterPro2GO terms for this entry)
  interpro_description: Not specified in InterPro
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 32
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: PTHR10807-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: PTHR10807-deep-research-falcon_artifacts/artifact-01.md
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
- **Accession:** PTHR10807
- **Name:** MYOTUBULARIN-RELATED
- **Short name:** Not specified
- **Entry type:** family
- **Integrated into / parent:** IPR030564
- **Member database signatures:** Not specified
- **Scale:** 30741 proteins across 8904 taxa, 34 subfamilies
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
**PTHR10807 (MYOTUBULARIN-RELATED)**, structured to support GO annotation review.

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
- **Accession:** PTHR10807
- **Name:** MYOTUBULARIN-RELATED
- **Short name:** Not specified
- **Entry type:** family
- **Integrated into / parent:** IPR030564
- **Member database signatures:** Not specified
- **Scale:** 30741 proteins across 8904 taxa, 34 subfamilies
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
**PTHR10807 (MYOTUBULARIN-RELATED)**, structured to support GO annotation review.

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


# Comprehensive Research Report: InterPro Family PTHR10807 (MYOTUBULARIN-RELATED)

## Executive Summary

InterPro entry PTHR10807 represents the MYOTUBULARIN-RELATED protein family, encompassing 30,741 proteins across 8,904 taxa with 34 subfamilies. **Crucially, this entry currently has NO InterPro2GO mappings**. This report evaluates whether GO annotations should be added and, if so, which terms are appropriate for the entire family versus specific subfamilies.

**Key Finding**: The myotubularin family exhibits profound functional heterogeneity with approximately 40% of members being catalytically inactive pseudo-phosphatases. Any future GO annotation strategy MUST distinguish between active phosphatases and inactive regulatory subunits to avoid systematic over-annotation.

---

## 1. Family Definition and Biochemistry

### Catalytic Mechanism and Structure

The myotubularin family comprises lipid phosphatases belonging to the protein tyrosine phosphatase/dual-specificity phosphatase (PTP/DSP) superfamily (amoasii2012myotubularinphosphoinositidephosphatases pages 1-4, davies2012theptenand pages 1-3, amoasii2012myotubularinphosphoinositidephosphatases pages 4-8). The **catalytically active members** contain the conserved signature motif **C(X)₅R(T/S)** in their active site, which is essential for enzymatic activity (bong2016crystalstructureof pages 1-2, begley2003crystalstructureof pages 1-2, amoasii2012myotubularinphosphoinositidephosphatases pages 1-4, amoasii2012myotubularinphosphoinositidephosphatases pages 4-8).

The catalytic mechanism involves a two-step reaction (bong2016crystalstructureof pages 1-2, schaletzky2003phosphatidylinositol5phosphateactivationand pages 1-2, amoasii2012myotubularinphosphoinositidephosphatases pages 1-4):
1. The nucleophilic cysteine residue attacks the phosphate group of the substrate, forming a phosphocysteine intermediate
2. The conserved arginine stabilizes the transition state
3. A conserved aspartate residue protonates the leaving oxygen, completing hydrolysis

### Substrate Specificity

Active myotubularins preferentially dephosphorylate **phosphatidylinositol 3-phosphate [PtdIns(3)P]** and **phosphatidylinositol 3,5-bisphosphate [PtdIns(3,5)P₂]** at the D3 position of the inositol ring, generating **phosphatidylinositol (PtdIns)** and **phosphatidylinositol 5-phosphate [PtdIns(5)P]**, respectively (wang2024recentadvancesof pages 1-2, bong2016crystalstructureof pages 1-2, schaletzky2003phosphatidylinositol5phosphateactivationand pages 1-2, begley2003crystalstructureof pages 1-2, amoasii2012myotubularinphosphoinositidephosphatases pages 1-4, davies2012theptenand pages 1-3, amoasii2012myotubularinphosphoinositidephosphatases pages 4-8). This activity positions them as antagonists of Class II and Class III phosphatidylinositol 3-kinases (amoasii2012myotubularinphosphoinositidephosphatases pages 1-4, davies2012theptenand pages 1-3).

Structural studies of MTMR2 at 2.3 Å resolution revealed that two phosphate molecules coordinate with strictly conserved residues in the C(X)₅R motif (bong2016crystalstructureof pages 1-2, begley2003crystalstructureof pages 1-2). The substrate specificity for PtdIns(3)P and PtdIns(3,5)P₂ is conserved across active family members from yeast to humans (schaletzky2003phosphatidylinositol5phosphateactivationand pages 1-2, amoasii2012myotubularinphosphoinositidephosphatases pages 1-4).

### Domain Architecture

All myotubularins share a conserved domain architecture (begley2003crystalstructureof pages 1-2, saar2025themyotubularinrelated pages 1-2, amoasii2012myotubularinphosphoinositidephosphatases pages 1-4, amoasii2012myotubularinphosphoinositidephosphatases pages 4-8):

- **PH-GRAM domain** (~190 residues): Pleckstrin homology-glucosyltransferases, Rab-like GTPase activators and myotubularins domain. Structural studies revealed this domain unexpectedly adopts a PH domain fold (begley2003crystalstructureof pages 1-2). While initially predicted to bind phosphoinositides, recent studies show conflicting results on its lipid-binding capacity.

- **RID domain**: Rac-induced recruitment domain, also called the MTMR domain, functions as a membrane-targeting motif (amoasii2012myotubularinphosphoinositidephosphatases pages 4-8).

- **PTP/DSP domain** (~376 residues): The catalytic phosphatase domain containing the C(X)₅R motif (begley2003crystalstructureof pages 1-2).

- **SID domain**: SET-interacting domain unique to myotubularins, mediating protein-protein interactions (amoasii2012myotubularinphosphoinositidephosphatases pages 4-8).

- **Coiled-coil (CC) domain**: Essential for homo- and heterodimerization between myotubularins. Recent biophysical data shows that MTMR7-CC forms dimers while MTMR9-CC forms trimers (saar2025themyotubularinrelated pages 1-2, wang2024recentadvancesof pages 2-3).

- **PDZ-binding motif**: Present at the C-terminus of most members (amoasii2012myotubularinphosphoinositidephosphatases pages 4-8).

- **Additional domains in subfamilies**: MTMR3/4 contain FYVE domains, while MTMR5/13 possess DENN and additional PH domains (amoasii2012myotubularinphosphoinositidephosphatases pages 4-8).

Recent 2025 work identified extensive intrinsically disordered regions (IDRs) in the C-terminal domains (CTDs) of MTMRs containing short linear motifs (SLiMs) important for subcellular targeting, signaling, and phase separation (saar2025themyotubularinrelated pages 1-2).

### Allosteric Regulation

A remarkable feature is allosteric activation by the product PtdIns(5)P. Studies show that PtdIns(5)P causes MTM1 to form heptameric rings (12.5 nm diameter) and functions as a positive feedback activator for MTM1, MTMR3, and MTMR6 (schaletzky2003phosphatidylinositol5phosphateactivationand pages 1-2). Disease-causing mutation R69 in MTM1 reduces the enzyme's ability to respond to PtdIns(5)P activation (schaletzky2003phosphatidylinositol5phosphateactivationand pages 1-2).

---

## 2. InterPro2GO Mapping Appropriateness

### Current Status
**PTHR10807 currently has ZERO InterPro2GO mappings.** This presents an opportunity to establish appropriate annotations de novo rather than correcting existing over-annotation.

### Critical Issue: Functional Heterogeneity

The myotubularin family consists of **approximately 14 members in humans** distributed into **6 phylogenetic subgroups** (amoasii2012myotubularinphosphoinositidephosphatases pages 4-8):

**Catalytically ACTIVE members (9 members)**:
- MTM1
- MTMR1, MTMR2
- MTMR3, MTMR4
- MTMR6, MTMR7, MTMR8
- MTMR14 (JUMPY - often classified separately)

**Catalytically INACTIVE pseudo-phosphatases (6 members)**:
- MTMR5 (SBF1)
- MTMR9 (LIP-STYX)
- MTMR10, MTMR11 (CRA)
- MTMR12 (3-PAP)
- MTMR13 (SBF2)
- [MTMR15/FAN1 is no longer considered a myotubularin but a nuclease]

The inactive members contain naturally occurring substitutions in the catalytic cysteine and/or arginine residues of the C(X)₅R motif, rendering them enzymatically dead (begley2003crystalstructureof pages 1-2, wang2024recentadvancesof pages 2-3, zaru2020challengesinthe pages 1-2, amoasii2012myotubularinphosphoinositidephosphatases pages 4-8).

### Recommended GO Annotation Strategy

| GO term name | GO ID | Applicability | Evidence support level | Recommendation |
|---|---|---|---|---|
| phosphatidylinositol-3-phosphatase activity | GO:0004438 | All catalytically active myotubularins only (MTM1, MTMR1-4, MTMR6-8; MTMR14/JUMPY myotubularin-like but may sit outside the core Panther family boundary) | Strong: biochemical and structural evidence for PI(3)P dephosphorylation across active family members; inactive members lack catalytic residues (bong2016crystalstructureof pages 1-2, schaletzky2003phosphatidylinositol5phosphateactivationand pages 1-2, begley2003crystalstructureof pages 1-2, amoasii2012myotubularinphosphoinositidephosphatases pages 1-4, davies2012theptenand pages 1-3, amoasii2012myotubularinphosphoinositidephosphatases pages 4-8) | ADD ONLY TO SUBFAMILIES |
| phosphatidylinositol-3,5-bisphosphate 3-phosphatase activity | GO:0008968 | All catalytically active myotubularins only | Strong: multiple active MTMs hydrolyze PI(3,5)P2 to PI5P; not applicable to pseudo-phosphatases (schaletzky2003phosphatidylinositol5phosphateactivationand pages 1-2, amoasii2012myotubularinphosphoinositidephosphatases pages 1-4, davies2012theptenand pages 1-3, amoasii2012myotubularinphosphoinositidephosphatases pages 4-8) | ADD ONLY TO SUBFAMILIES |
| phosphoinositide phosphatase activity | GO:0042578 | All catalytically active myotubularins only | Strong but broader than the two terms above; accurate for active enzymes, inaccurate for inactive members (bong2016crystalstructureof pages 1-2, begley2003crystalstructureof pages 1-2, amoasii2012myotubularinphosphoinositidephosphatases pages 1-4, davies2012theptenand pages 1-3, amoasii2012myotubularinphosphoinositidephosphatases pages 4-8) | ADD ONLY TO SUBFAMILIES |
| phosphatidylinositol binding | GO:0035091 | Many, but not demonstrably all, family members; likely mediated variably by PH-GRAM/FYVE/PH domains | Moderate: lipid-binding domains are common, but binding specificity is domain- and member-dependent; not universal enough for whole family annotation (begley2003crystalstructureof pages 1-2, stdenis2015myotubularinrelatedproteins3 pages 1-7, saar2025themyotubularinrelated pages 1-2, amoasii2012myotubularinphosphoinositidephosphatases pages 4-8) | DO NOT ADD |
| endosome organization | GO:0007032 | Many active members, especially MTMR3/4 and endosome-associated subgroups; not all family members | Moderate: literature strongly links myotubularins to endosomal PI regulation and trafficking, but not uniformly for every matched protein across taxa/subfamilies (stdenis2015myotubularinrelatedproteins3 pages 1-7, amoasii2012myotubularinphosphoinositidephosphatases pages 1-4, davies2012theptenand pages 1-3, amoasii2012myotubularinphosphoinositidephosphatases pages 4-8) | ADD ONLY TO SUBFAMILIES |
| membrane trafficking | GO:0048193 | Broadly relevant to many active members; not universal to inactive/pseudo-phosphatases and not proven for every subfamily | Moderate: recurring family-level interpretation from PI(3)P/PI(3,5)P2 metabolism, but still too broad for all proteins in PTHR10807 (wang2024recentadvancesof pages 1-2, tronch�re2003implicationofphosphoinositide pages 1-2, amoasii2012myotubularinphosphoinositidephosphatases pages 1-4, davies2012theptenand pages 1-3, amoasii2012myotubularinphosphoinositidephosphatases pages 4-8) | ADD ONLY TO SUBFAMILIES |
| autophagy | GO:0006914 | Specific active members/subcomplexes only (e.g., MTMR3/4, MTMR6/7/8/9, MTMR14 in reviews), not all family proteins | Moderate: strong literature for selected members, including positive and negative regulatory roles; direction and presence vary by member, so family-wide annotation would overreach (wang2024recentadvancesof pages 1-2, wang2024recentadvancesof pages 2-3, wang2024recentadvancesof pages 3-4) | ADD ONLY TO SUBFAMILIES |
| regulation of autophagy | GO:0010506 | Specific active members or complexes only | Moderate: member-specific and sometimes opposite effects reported; not homogeneous across family (wang2024recentadvancesof pages 1-2, wang2024recentadvancesof pages 2-3, wang2024recentadvancesof pages 3-4) | ADD ONLY TO SUBFAMILIES |
| early endosome | GO:0005769 | Specific members with experimental localization, especially MTMR4 and several active MTMs; not all family members | Moderate: compatible with known localization for some proteins, but localization differs substantially across family and taxa (saar2025themyotubularinrelated pages 1-2, amoasii2012myotubularinphosphoinositidephosphatases pages 1-4, davies2012theptenand pages 1-3, amoasii2012myotubularinphosphoinositidephosphatases pages 4-8) | ADD ONLY TO SUBFAMILIES |
| endosome membrane | GO:0010008 | Specific members only | Moderate: many MTMs act on endosomal phosphoinositides, but not all proteins are stably endosome-membrane localized (saar2025themyotubularinrelated pages 1-2, amoasii2012myotubularinphosphoinositidephosphatases pages 1-4, davies2012theptenand pages 1-3, amoasii2012myotubularinphosphoinositidephosphatases pages 4-8) | ADD ONLY TO SUBFAMILIES |
| cytoplasm | GO:0005737 | Many members, including active-inactive complexes | Weak/informationally poor: true for many proteins but too generic to be useful and unlikely to aid GO review (wang2024recentadvancesof pages 2-3, amoasii2012myotubularinphosphoinositidephosphatases pages 4-8) | DO NOT ADD |
| membrane | GO:0016020 | Many family members associate with membranes, but localization is dynamic and non-uniform | Weak/informationally poor: too generic and risks low-value overannotation (saar2025themyotubularinrelated pages 1-2, amoasii2012myotubularinphosphoinositidephosphatases pages 1-4, amoasii2012myotubularinphosphoinositidephosphatases pages 4-8) | DO NOT ADD |
| protein heterodimerization activity | GO:0046982 | Many active-inactive and active-active MTMR pairs, but not necessarily every family member in every taxon | Moderate: dimerization is common via coiled-coil domains, yet not universal enough for whole-family propagation across all matches (wang2024recentadvancesof pages 1-2, stdenis2015myotubularinrelatedproteins3 pages 1-7, wang2024recentadvancesof pages 2-3, zaru2020challengesinthe pages 1-2, amoasii2012myotubularinphosphoinositidephosphatases pages 4-8) | ADD ONLY TO SUBFAMILIES |
| phosphatase activator activity | GO:0010923 | Inactive pseudo-phosphatases that stimulate active partners, especially MTMR9 and related dead phosphatases | Moderate: supported for selected inactive members as allosteric/targeting cofactors, not for all family proteins (zaru2020challengesinthe pages 1-2, amoasii2012myotubularinphosphoinositidephosphatases pages 4-8) | ADD ONLY TO SUBFAMILIES |
| cytokinesis / abscission-related process | GO:0000910 / GO:0000911 | MTMR3/MTMR4 subfamily only | Strong for MTMR3/4 specifically, not transferable to rest of family (stdenis2015myotubularinrelatedproteins3 pages 1-7) | ADD ONLY TO SUBFAMILIES |
| Ras protein signal transduction / KRAS plasma membrane localization support | N/A | MTMR2/3/4/7-like subset only, and currently based on 2024 preprint evidence | Emerging: mechanistic but preprint-stage and subset-specific (lange2024myotubularinrelatedproteinsregulate pages 1-5) | DO NOT ADD |


*Table: This table summarizes which GO terms are supported for the myotubularin family and whether they should be applied at whole-family level or only to specific subfamilies. It is useful for avoiding over-annotation of inactive pseudo-phosphatases and member-specific biological processes.*

**Key Recommendations**:

1. **DO NOT apply catalytic activity terms to the entire family**. Terms like "phosphatidylinositol-3-phosphatase activity" (GO:0004438) or "phosphatidylinositol-3,5-bisphosphate 3-phosphatase activity" (GO:0008968) should ONLY be mapped to child entries or subfamilies containing active members (bong2016crystalstructureof pages 1-2, schaletzky2003phosphatidylinositol5phosphateactivationand pages 1-2, begley2003crystalstructureof pages 1-2, amoasii2012myotubularinphosphoinositidephosphatases pages 1-4, davies2012theptenand pages 1-3).

2. **Inactive members have distinct functions**: Dead phosphatases heterodimerize with active partners and regulate their activity, substrate presentation, or subcellular localization (wang2024recentadvancesof pages 2-3, zaru2020challengesinthe pages 1-2, amoasii2012myotubularinphosphoinositidephosphatases pages 4-8). For example, MTMR9 allosterically activates MTMR6 lipid phosphatase activity (zaru2020challengesinthe pages 1-2). These could be annotated with "phosphatase activator activity" (GO:0010923) but NOT with phosphatase activity terms.

3. **Biological process terms vary by subfamily**:
   - Autophagy regulation: Documented for specific members (MTMR3/4, MTMR6/7/8/9, MTMR14) but with both positive and negative regulatory roles that differ between members (wang2024recentadvancesof pages 1-2, wang2024recentadvancesof pages 2-3, wang2024recentadvancesof pages 3-4)
   - Cytokinesis/abscission: Specific to MTMR3/MTMR4 heterodimer (stdenis2015myotubularinrelatedproteins3 pages 1-7)
   - Endosome organization: Many but not all active members (stdenis2015myotubularinrelatedproteins3 pages 1-7, amoasii2012myotubularinphosphoinositidephosphatases pages 1-4, amoasii2012myotubularinphosphoinositidephosphatases pages 4-8)

4. **Generic terms provide little value**: Terms like "membrane" (GO:0016020) or "cytoplasm" (GO:0005737) are technically true but informationally poor and should be avoided (wang2024recentadvancesof pages 2-3, amoasii2012myotubularinphosphoinositidephosphatases pages 4-8).

### Subfamily-Specific Annotations Are Essential

Given the 34 subfamilies reported in PTHR10807, InterPro2GO should **either**:
- Map specific GO terms only to child entries representing active phosphatases
- Add qualifier metadata indicating which subfamilies each term applies to
- Avoid family-level GO propagation entirely for this entry

---

## 3. Functional Divergence Across the Family

### Active vs. Inactive Member Dichotomy

The most striking functional divergence is the ~40% of family members that are catalytically inactive pseudo-phosphatases (zaru2020challengesinthe pages 1-2, amoasii2012myotubularinphosphoinositidephosphatases pages 4-8). Phylogenetic analysis reveals these are not recent pseudogene artifacts but evolutionarily conserved proteins with distinct biological functions (kennelly2001proteinphosphatasesaphylogenetic pages 1-2, amoasii2012myotubularinphosphoinositidephosphatases pages 4-8).

### Heterodimerization Networks

| Member | Catalytic status | C(X)5R motif status | Key domains noted | Substrate specificity if active | Known dimerization / interaction partners | Associated human diseases / traits | Evidence |
|---|---|---|---|---|---|---|---|
| MTM1 | Active | Canonical C(X)5R present | PH-GRAM, PTP/DSP, SID, CC, PDZ-binding motif | PI(3)P and PI(3,5)P2 → PI and PI(5)P | MTMR12; homodimerization reported | X-linked centronuclear/myotubular myopathy; cholestatic liver disease model relevance | (wang2024recentadvancesof pages 1-2, schaletzky2003phosphatidylinositol5phosphateactivationand pages 1-2, wang2024recentadvancesof pages 2-3, amoasii2012myotubularinphosphoinositidephosphatases pages 1-4, amoasii2012myotubularinphosphoinositidephosphatases pages 4-8) |
| MTMR1 | Active | Canonical C(X)5R present | PH-GRAM, PTP/DSP, SID, CC, PDZ-binding motif | PI(3)P and PI(3,5)P2 | MTMR12 | Linked to myotonic dystrophy in older literature; less well characterized functionally | (bong2016crystalstructureof pages 1-2, wang2024recentadvancesof pages 2-3, amoasii2012myotubularinphosphoinositidephosphatases pages 4-8) |
| MTMR2 | Active | Canonical C(X)5R present | PH-GRAM, PTP/DSP, SID, CC, PDZ-binding motif | PI(3)P and PI(3,5)P2 | MTMR5/SBF1, MTMR13/SBF2, MTMR12 | Charcot-Marie-Tooth disease type 4B | (begley2003crystalstructureof pages 1-2, wang2024recentadvancesof pages 2-3, amoasii2012myotubularinphosphoinositidephosphatases pages 1-4, amoasii2012myotubularinphosphoinositidephosphatases pages 4-8) |
| MTMR3 | Active | Canonical C(X)5R present | PH-GRAM, PTP/DSP, SID, CC, FYVE, PDZ-binding motif | PI(3)P and PI(3,5)P2 | MTMR4 | Cancer susceptibility/ progression associations; roles in autophagy and cytokinesis/abscission | (lange2024myotubularinrelatedproteinsregulate pages 1-5, stdenis2015myotubularinrelatedproteins3 pages 1-7, amoasii2012myotubularinphosphoinositidephosphatases pages 4-8) |
| MTMR4 | Active | Canonical C(X)5R present | PH-GRAM, PTP/DSP, SID, CC, FYVE, PDZ-binding motif | PI(3)P and PI(3,5)P2; also reported protein phosphatase activity on Smad2/3 in review literature | MTMR3 | LQT1/aortic aneurysm associations in review literature; roles in endosomes and cytokinesis/abscission | (stdenis2015myotubularinrelatedproteins3 pages 1-7, wang2024recentadvancesof pages 3-4, amoasii2012myotubularinphosphoinositidephosphatases pages 4-8) |
| MTMR6 | Active | Canonical C(X)5R present | PH-GRAM, PTP/DSP, SID, CC, PDZ-binding motif | PI(3)P and PI(3,5)P2 | MTMR9; homodimerization reported | Reported roles in KCa3.1 regulation, apoptosis, autophagy; no classic monogenic disease established here | (schaletzky2003phosphatidylinositol5phosphateactivationand pages 1-2, wang2024recentadvancesof pages 2-3, amoasii2012myotubularinphosphoinositidephosphatases pages 4-8) |
| MTMR7 | Active | Canonical C(X)5R present | PH-GRAM, PTP/DSP, SID, CC, PDZ-binding motif; long disordered CTD emphasized recently | Family substrate class is PI(3)P / PI(3,5)P2; specific activity retained in active group | MTMR9; coiled-coil oligomerization studied | Obesity/metabolic syndrome, epilepsy, colorectal cancer associations; KRAS/PM lipid regulation | (lange2024myotubularinrelatedproteinsregulate pages 1-5, saar2025themyotubularinrelated pages 1-2, stdenis2015myotubularinrelatedproteins3 pages 1-7, amoasii2012myotubularinphosphoinositidephosphatases pages 4-8) |
| MTMR8 | Active | Canonical C(X)5R present | PH-GRAM, PTP/DSP, SID, CC, PDZ-binding motif | PI(3)P and PI(3,5)P2; MTMR8-MTMR9 complex reported to prefer PI(3)P | MTMR9 | Reported signaling/developmental roles; no specific monogenic disease highlighted here | (wang2024recentadvancesof pages 2-3, amoasii2012myotubularinphosphoinositidephosphatases pages 4-8) |
| MTMR14 / JUMPY | Active (myotubularin-like, often treated separately) | Similar CX5R motif | Myotubularin-like phosphatase core; not placed in core 14-member MTMR phylogeny by some reviews | Shares myotubularin substrate specificity | Not specified here | Autosomal centronuclear myopathy | (amoasii2012myotubularinphosphoinositidephosphatases pages 1-4, amoasii2012myotubularinphosphoinositidephosphatases pages 4-8) |
| MTMR5 / SBF1 | Inactive / pseudo-phosphatase | Lacks catalytic Cys/Arg substitutions in motif | PH-GRAM, PTP-like inactive domain, SID, CC, DENN, PH | — | MTMR2 | Charcot-Marie-Tooth-related biology; disease-linked pseudophosphatase family member; oncogenic/growth-control associations | (begley2003crystalstructureof pages 1-2, wang2024recentadvancesof pages 2-3, zaru2020challengesinthe pages 1-2, amoasii2012myotubularinphosphoinositidephosphatases pages 4-8) |
| MTMR9 / LIP-STYX | Inactive / pseudo-phosphatase | Lacks catalytic Cys/Arg substitutions in motif | PH-GRAM, PTP-like inactive domain, SID, CC, PDZ-binding motif; short CTD | — | MTMR6, MTMR7, MTMR8; homodimerization reported | Obesity/metabolic syndrome and epilepsy associations; allosteric activator/localization partner for active MTMRs | (wang2024recentadvancesof pages 2-3, zaru2020challengesinthe pages 1-2, amoasii2012myotubularinphosphoinositidephosphatases pages 4-8) |
| MTMR10 | Inactive / pseudo-phosphatase | Lacks catalytic motif residues | PH-GRAM, PTP-like inactive domain, SID, CC, PDZ-binding motif | — | Not specified here | Reported in 15q13.3 neuropathological disorder region / neurologic associations in review literature | (wang2024recentadvancesof pages 2-3, wang2024recentadvancesof pages 3-4, amoasii2012myotubularinphosphoinositidephosphatases pages 4-8) |
| MTMR11 / CRA | Inactive / pseudo-phosphatase | Lacks catalytic motif residues | PH-GRAM, PTP-like inactive domain, SID, CC, PDZ-binding motif | — | Not specified here | Aberrant expression reported in AML, ALL, HER2+ breast cancer | (stdenis2015myotubularinrelatedproteins3 pages 1-7, amoasii2012myotubularinphosphoinositidephosphatases pages 4-8) |
| MTMR12 / 3-PAP | Inactive / pseudo-phosphatase | Lacks catalytic motif residues | PH-GRAM, PTP-like inactive domain, SID, CC, PDZ-binding motif | — | MTM1, MTMR1, MTMR2; homodimerization reported | Stabilizes functional complexes in skeletal muscle; relevant to X-linked myotubular myopathy biology | (wang2024recentadvancesof pages 2-3, amoasii2012myotubularinphosphoinositidephosphatases pages 4-8) |
| MTMR13 / SBF2 | Inactive / pseudo-phosphatase | Lacks catalytic motif residues | PH-GRAM, PTP-like inactive domain, SID, CC, DENN, PH | — | MTMR2; homodimerization reported | Charcot-Marie-Tooth disease type 4B | (begley2003crystalstructureof pages 1-2, wang2024recentadvancesof pages 2-3, zaru2020challengesinthe pages 1-2, amoasii2012myotubularinphosphoinositidephosphatases pages 4-8) |
| MTMR15 / FAN1 | Not a core myotubularin in newer reviews; nuclease rather than MTMR pseudo-phosphatase | Not applicable / reclassified | FAN1 nuclease architecture, not retained as canonical MTMR family member in later reviews | — | FANCD2 interaction noted | DNA repair disorders / neuropathological associations via 15q13.3 region in older review context | (wang2024recentadvancesof pages 2-3, amoasii2012myotubularinphosphoinositidephosphatases pages 4-8) |


*Table: This table summarizes active and inactive myotubularin-family members, their motifs, domains, substrates, interaction partners, and disease links. It is useful for assessing whether family-level GO annotations would apply uniformly across PTHR10807 matches.*

Inactive members regulate active partners through obligate or facultative heterodimer formation (wang2024recentadvancesof pages 2-3, zaru2020challengesinthe pages 1-2, amoasii2012myotubularinphosphoinositidephosphatases pages 4-8):

- **MTMR2-MTMR5/MTMR13**: MTMR2 forms heterodimers with inactive MTMR5 (SBF1) or MTMR13 (SBF2). Mutations in either MTMR2 or MTMR13 cause Charcot-Marie-Tooth disease type 4B, demonstrating that the inactive partner is functionally essential (begley2003crystalstructureof pages 1-2, wang2024recentadvancesof pages 2-3).

- **MTMR6/7/8-MTMR9 complexes**: MTMR6, MTMR7, and MTMR8 can each heterodimerize with MTMR9. The MTMR6-MTMR9 complex shows higher activity against PtdIns(3,5)P₂, while MTMR8-MTMR9 prefers PtdIns(3)P (wang2024recentadvancesof pages 2-3). The inactive MTMR9 modulates substrate specificity of its active partners.

- **MTMR3-MTMR4**: Both are catalytically active and form heterodimers. This complex regulates abscission during mitosis by interacting with PLK1 and CEP55 through distinct domains—MTMR3 binds PLK1 via its FYVE domain, while MTMR4 binds CEP55 via a GPPXXXY motif analogous to ESCRT-I components (stdenis2015myotubularinrelatedproteins3 pages 1-7).

- **MTM1-MTMR12**: MTMR12 (3-PAP) is inactive and regulates MTM1 localization and activity in skeletal muscle (wang2024recentadvancesof pages 2-3).

### Substrate Preference Divergence

While all active members dephosphorylate PtdIns(3)P and PtdIns(3,5)P₂, different heterodimeric complexes show distinct substrate preferences. This suggests functional specialization despite conserved catalytic machinery (wang2024recentadvancesof pages 2-3).

### Neo-functionalization Beyond Lipid Phosphatase Activity

MTMR4 has been reported to dephosphorylate protein substrates (Smad2/3) in addition to lipids, representing potential neo-functionalization (wang2024recentadvancesof pages 3-4). This remains controversial and requires further validation.

Recent 2024 work identified MTMR2/3/4/7 as regulators of KRAS plasma membrane localization through indirect control of PM PtdIns4P and phosphatidylserine levels, demonstrating a previously unrecognized signaling function (lange2024myotubularinrelatedproteinsregulate pages 1-5).

### Disease Associations Reflect Divergence

Different subfamily members cause distinct diseases (amoasii2012myotubularinphosphoinositidephosphatases pages 1-4, amoasii2012myotubularinphosphoinositidephosphatases pages 4-8):
- **MTM1**: X-linked centronuclear/myotubular myopathy
- **MTMR2, MTMR5, MTMR13**: Charcot-Marie-Tooth neuropathies
- **MTMR14**: Autosomal centronuclear myopathy
- **MTMR3, MTMR7**: Cancer susceptibility associations
- **MTMR7, MTMR9**: Metabolic syndrome and obesity associations

---

## 4. Taxonomic Scope

### Eukaryote-Specific Family

Myotubularins are **found only in eukaryotes** (amoasii2012myotubularinphosphoinositidephosphatases pages 1-4, davies2012theptenand pages 1-3, kennelly2001proteinphosphatasesaphylogenetic pages 1-2, amoasii2012myotubularinphosphoinositidephosphatases pages 4-8). They are **absent from bacteria and archaea**, distinguishing them from other phosphatase families that show prokaryotic representatives (brenchley2007thetritrypphosphatome pages 2-3, kennelly2001proteinphosphatasesaphylogenetic pages 1-2).

### Distribution Across Eukaryotic Kingdoms

The family is highly conserved from unicellular eukaryotes to mammals (amoasii2012myotubularinphosphoinositidephosphatases pages 4-8):

- **Fungi**: *Saccharomyces cerevisiae* has a single active member (Ymr1) and notably **lacks inactive pseudo-phosphatase members**, demonstrating that the active-inactive pairing is not universal across all eukaryotic clades (amoasii2012myotubularinphosphoinositidephosphatases pages 4-8).

- **Nematodes**: *Caenorhabditis elegans* has multiple myotubularins including both active and inactive members (zaru2020challengesinthe pages 1-2, amoasii2012myotubularinphosphoinositidephosphatases pages 4-8).

- **Arthropods**: *Drosophila melanogaster* possesses myotubularin orthologs (amoasii2012myotubularinphosphoinositidephosphatases pages 4-8).

- **Vertebrates**: Highly conserved across fish (*Danio rerio*), mammals, and other vertebrates with the full complement of 14-16 members in mammals (amoasii2012myotubularinphosphoinositidephosphatases pages 4-8).

### Implications for GO Term Applicability

Given the 8,904 taxa represented in PTHR10807, several considerations arise:

1. **Cellular compartment terms**: The endosomal system is present across all eukaryotes, so terms like "early endosome" could theoretically apply broadly. However, specific localization varies between orthologs.

2. **Autophagy terms**: Autophagy is a eukaryote-specific process, making such terms taxonomically appropriate. However, myotubularin roles in autophagy are member-specific and sometimes opposing (activation vs. inhibition), precluding family-wide annotation (wang2024recentadvancesof pages 1-2, wang2024recentadvancesof pages 3-4).

3. **Disease-related process terms**: Specific to vertebrate biology and should not be propagated to fungal or invertebrate orthologs.

4. **Core lipid metabolism terms**: PtdIns(3)P metabolism is conserved across eukaryotes, but the absence of inactive members in yeast suggests divergent regulatory strategies across clades.

### Recent Developments (2023-2024)

A 2024 review highlighted myotubularin roles in cardiovascular diseases including cardiomyocyte hypertrophy, vascular smooth muscle cell proliferation, LQT1, and aortic aneurysm (wang2024recentadvancesof pages 1-2). A 2023 review connected myotubularins to myotubular myopathies, neurodegenerative disorders, and carcinogenesis (derkaczew2023thegeneticbackground pages 1-3). These associations are mammalian/vertebrate-specific and demonstrate continued functional diversification in higher eukaryotes.

---

## 5. Over-Annotation Verdict and Recommendations

### Current Status Assessment

**PTHR10807 currently has NO InterPro2GO annotations**, which means:
- There is no existing over-annotation to correct
- There is an opportunity to establish a best-practice annotation strategy from the outset
- The absence of annotations may reflect recognition of the family's heterogeneity

### Verdict: HIGH RISK OF OVER-ANNOTATION IF APPLIED AT FAMILY LEVEL

The myotubularin family presents a **paradigmatic case** of why family-level GO annotation can be problematic:

1. **~40% of family members lack catalytic activity** - applying phosphatase activity terms would systematically misannotate thousands of proteins
2. **Subfamilies have distinct biological process roles** - some regulate autophagy positively, others negatively; some are involved in cytokinesis, others are not
3. **Inactive members have evolved alternative functions** - they act as cofactors, localizers, and allosteric activators
4. **Substrate preferences differ between subcomplexes** despite conserved catalytic machinery

### Recommended Action Pattern

**For InterPro2GO curators:**

**VERDICT: MARK_AS_REQUIRES_SUBFAMILY_SPECIFIC_ANNOTATION**

**Rationale**: The family is functionally heterogeneous with catalytically active and inactive subclades. GO terms should be applied at the subfamily or child-entry level, not propagated to all PTHR10807 matches.

**Specific Recommendations**:

1. **DO NOT add family-level MF terms** for phosphatase activity - these would systematically over-annotate inactive members

2. **CONSIDER adding subfamily-specific annotations** if InterPro can map them to appropriate child entries:
   - **For active-only subfamilies**: "phosphatidylinositol-3-phosphatase activity" (GO:0004438), "phosphatidylinositol-3,5-bisphosphate 3-phosphatase activity" (GO:0008968)
   - **For inactive-only subfamilies**: "phosphatase activator activity" (GO:0010923), "protein heterodimerization activity" (GO:0046982)

3. **Biological Process terms require even more caution**:
   - "endosome organization" (GO:0007032) - applicable to many but not all active members
   - "autophagy" (GO:0006914) or "regulation of autophagy" (GO:0010506) - member-specific and directionally inconsistent
   - "cytokinesis" (GO:0000910) - MTMR3/4 specific

4. **Alternative strategy**: Create a **KEEP_AS_NON_CORE** marker for this entry, indicating that InterPro2GO mappings exist only at child/subfamily level, never propagated from the parent PTHR10807 entry

5. **For database consumers**: Flag that proteins matching PTHR10807 require ortholog-specific or subfamily-specific functional assignment, not inheritance from the family signature

### Recommendations for InterPro Itself

**Consider restructuring PTHR10807** if technically feasible:
- Split into two parent entries: PTHR10807-ACTIVE and PTHR10807-INACTIVE
- Or ensure the 34 subfamilies are represented as distinct child entries that can receive subfamily-appropriate GO annotations
- Document in the entry description that ~40% of matches are catalytically inactive and perform regulatory rather than catalytic functions

### Precedent and Best Practices

This situation parallels other pseudo-enzyme families where UniProtKB and other databases have developed special annotation practices (zaru2020challengesinthe pages 1-2):
- Pseudokinases (e.g., KSR1)
- Inactive phosphatases in other families
- Catalytically dead proteases

The pseudoenzyme community has established that **demonstrating lack of catalytic activity is as important as demonstrating activity** (zaru2020challengesinthe pages 1-2). InterPro2GO should adopt similar rigor: absence of GO terms for inactive members is informative, not a gap to be filled.

### Summary Table of Recommendations

| GO Annotation Scenario | Recommendation | Rationale |
|---|---|---|
| Phosphatase activity (MF) to whole PTHR10807 | **REJECT / DO NOT ADD** | Would misannotate ~40% of family (inactive members) |
| Phosphatase activity to active-only subfamilies | **ACCEPT / ADD ONLY TO SUBFAMILIES** | Supported by extensive biochemical evidence |
| Endosome organization (BP) to whole family | **REJECT** | Not universal; member- and taxon-dependent |
| Autophagy regulation (BP) to whole family | **REJECT** | Member-specific and directionally inconsistent |
| Generic terms (membrane, cytoplasm) | **REJECT** | Low information value |
| Heterodimerization (MF) to inactive subfamilies | **CONSIDER / ADD ONLY TO SUBFAMILIES** | Well-supported for regulatory function |

---

## Conclusion

InterPro entry PTHR10807 represents a functionally diverse protein family where **subfamily identity, not family membership, determines function**. The profound split between catalytically active phosphatases and inactive regulatory subunits makes this entry **unsuitable for family-level GO propagation**. 

Any GO annotation strategy must leverage InterPro's hierarchical structure to apply specific terms only to appropriate child entries/subfamilies. The current absence of InterPro2GO mappings is preferable to over-annotation that would systematically mischaracterize thousands of proteins across 8,904 taxa.

**Final Verdict**: **This entry should remain WITHOUT family-level InterPro2GO mappings** and serve as a model for how to handle functionally heterogeneous protein families through subfamily-specific annotation strategies.

---

## References

All citations follow the format () corresponding to evidence context IDs from:

- **Recent 2023-2024 reviews**: Wang et al. 2024 (cardiovascular) (wang2024recentadvancesof pages 1-2), Derkaczew et al. 2023 (genetic background) (derkaczew2023thegeneticbackground pages 1-3), Lange et al. 2024 preprint (KRAS regulation) (lange2024myotubularinrelatedproteinsregulate pages 1-5), Saar et al. 2025 (disordered regions) (saar2025themyotubularinrelated pages 1-2)

- **Structural studies**: Begley et al. 2003 (MTMR2 structure) (begley2003crystalstructureof pages 1-2), Bong et al. 2016 (MTMR1 structure) (bong2016crystalstructureof pages 1-2), Begley et al. 2006 (substrate recognition) (schaletzky2003phosphatidylinositol5phosphateactivationand pages 1-2), Schaletzky et al. 2003 (allosteric activation) (schaletzky2003phosphatidylinositol5phosphateactivationand pages 1-2)

- **Comprehensive reviews**: Amoasii et al. 2012 (diseases) (amoasii2012myotubularinphosphoinositidephosphatases pages 1-4), Davies et al. 2012 (PTEN and myotubularins) (davies2012theptenand pages 1-3), Tronchère et al. 2003 (myotubular myopathy) (tronch�re2003implicationofphosphoinositide pages 1-2)

- **Functional studies**: St-Denis et al. 2015 (MTMR3/4 in cytokinesis) (stdenis2015myotubularinrelatedproteins3 pages 1-7), Zaru et al. 2020 (pseudoenzyme annotation) (zaru2020challengesinthe pages 1-2)

- **Phylogenetic studies**: Kennelly 2001 (phylogenetic perspective) (kennelly2001proteinphosphatasesaphylogenetic pages 1-2), Brenchley et al. 2007 (TriTryp phosphatome) (brenchley2007thetritrypphosphatome pages 2-3)

References

1. (amoasii2012myotubularinphosphoinositidephosphatases pages 1-4): Leonela Amoasii, Karim Hnia, and Jocelyn Laporte. Myotubularin phosphoinositide phosphatases in human diseases. Current topics in microbiology and immunology, 362:209-33, Jan 2012. URL: https://doi.org/10.1007/978-94-007-5025-8\_10, doi:10.1007/978-94-007-5025-8\_10. This article has 58 citations and is from a peer-reviewed journal.

2. (davies2012theptenand pages 1-3): E. M. Davies, D. A. Sheffield, Priyanka Tibarewal, C. Fedele, C. Mitchell, and N. Leslie. The pten and myotubularin phosphoinositide 3-phosphatases: linking lipid signalling to human disease. Sub-cellular biochemistry, 58:281-336, 2012. URL: https://doi.org/10.1007/978-94-007-3012-0\_8, doi:10.1007/978-94-007-3012-0\_8. This article has 25 citations.

3. (amoasii2012myotubularinphosphoinositidephosphatases pages 4-8): Leonela Amoasii, Karim Hnia, and Jocelyn Laporte. Myotubularin phosphoinositide phosphatases in human diseases. Current topics in microbiology and immunology, 362:209-33, Jan 2012. URL: https://doi.org/10.1007/978-94-007-5025-8\_10, doi:10.1007/978-94-007-5025-8\_10. This article has 58 citations and is from a peer-reviewed journal.

4. (bong2016crystalstructureof pages 1-2): Seoung Min Bong, Kka-bi Son, Seung-Won Yang, Jae-Won Park, Jea-Won Cho, Kyung-Tae Kim, Hackyoung Kim, Seung Jun Kim, Young Jun Kim, and Byung Il Lee. Crystal structure of human myotubularin-related protein 1 provides insight into the structural basis of substrate specificity. PLoS ONE, 11:e0152611, Mar 2016. URL: https://doi.org/10.1371/journal.pone.0152611, doi:10.1371/journal.pone.0152611. This article has 12 citations and is from a peer-reviewed journal.

5. (begley2003crystalstructureof pages 1-2): Michael J Begley, Gregory S Taylor, Soo-A Kim, Donna M Veine, Jack E Dixon, and Jeanne A Stuckey. Crystal structure of a phosphoinositide phosphatase, mtmr2: insights into myotubular myopathy and charcot-marie-tooth syndrome. Molecular cell, 12 6:1391-402, Dec 2003. URL: https://doi.org/10.1016/s1097-2765(03)00486-6, doi:10.1016/s1097-2765(03)00486-6. This article has 189 citations and is from a highest quality peer-reviewed journal.

6. (schaletzky2003phosphatidylinositol5phosphateactivationand pages 1-2): Julia Schaletzky, Stephen K. Dove, Benjamin Short, Oscar Lorenzo, Michael J. Clague, and Francis A. Barr. Phosphatidylinositol-5-phosphate activation and conserved substrate specificity of the myotubularin phosphatidylinositol 3-phosphatases. Current Biology, 13:504-509, Mar 2003. URL: https://doi.org/10.1016/s0960-9822(03)00132-5, doi:10.1016/s0960-9822(03)00132-5. This article has 220 citations and is from a highest quality peer-reviewed journal.

7. (wang2024recentadvancesof pages 1-2): Jia Wang, Wei Guo, Qiang Wang, Yongjian Yang, and Xiongshan Sun. Recent advances of myotubularin-related (mtmr) protein family in cardiovascular diseases. Frontiers in Cardiovascular Medicine, Mar 2024. URL: https://doi.org/10.3389/fcvm.2024.1364604, doi:10.3389/fcvm.2024.1364604. This article has 16 citations and is from a peer-reviewed journal.

8. (saar2025themyotubularinrelated pages 1-2): Daniel Saar, Caroline L. E. Lennartsson, Philip Weidner, Elke Burgermeister, and Birthe B. Kragelund. The myotubularin related proteins and the untapped interaction potential of their disordered c‐terminal regions. Proteins, 93:831-854, Nov 2025. URL: https://doi.org/10.1002/prot.26774, doi:10.1002/prot.26774. This article has 5 citations.

9. (wang2024recentadvancesof pages 2-3): Jia Wang, Wei Guo, Qiang Wang, Yongjian Yang, and Xiongshan Sun. Recent advances of myotubularin-related (mtmr) protein family in cardiovascular diseases. Frontiers in Cardiovascular Medicine, Mar 2024. URL: https://doi.org/10.3389/fcvm.2024.1364604, doi:10.3389/fcvm.2024.1364604. This article has 16 citations and is from a peer-reviewed journal.

10. (zaru2020challengesinthe pages 1-2): Rossana Zaru, Michele Magrane, and Sandra Orchard. Challenges in the annotation of pseudoenzymes in databases: the uniprotkb approach. The FEBS Journal, 287:4114-4127, Nov 2020. URL: https://doi.org/10.1111/febs.15100, doi:10.1111/febs.15100. This article has 29 citations.

11. (stdenis2015myotubularinrelatedproteins3 pages 1-7): Nicole St-Denis, Gagan D. Gupta, Zhen Yuan Lin, Beatriz Gonzalez-Badillo, Laurence Pelletier, and Anne-Claude Gingras. Myotubularin-related proteins 3 and 4 interact with polo-like kinase 1 and centrosomal protein of 55 kda to ensure proper abscission. Molecular &amp; Cellular Proteomics, 14:946-960, Apr 2015. URL: https://doi.org/10.1074/mcp.m114.046086, doi:10.1074/mcp.m114.046086. This article has 54 citations and is from a domain leading peer-reviewed journal.

12. (tronch�re2003implicationofphosphoinositide pages 1-2): H. Tronch�re, A. Buj-Bello, J.-L. Mandel, and B. Payrastre. Implication of phosphoinositide phosphatases in genetic diseases: the case of myotubularin. Cellular and Molecular Life Sciences CMLS, 60:2084-2099, Oct 2003. URL: https://doi.org/10.1007/s00018-003-3062-3, doi:10.1007/s00018-003-3062-3. This article has 35 citations.

13. (wang2024recentadvancesof pages 3-4): Jia Wang, Wei Guo, Qiang Wang, Yongjian Yang, and Xiongshan Sun. Recent advances of myotubularin-related (mtmr) protein family in cardiovascular diseases. Frontiers in Cardiovascular Medicine, Mar 2024. URL: https://doi.org/10.3389/fcvm.2024.1364604, doi:10.3389/fcvm.2024.1364604. This article has 16 citations and is from a peer-reviewed journal.

14. (lange2024myotubularinrelatedproteinsregulate pages 1-5): Taylor E. Lange, Ali Naji, Ransome van der Hoeven, Hong Liang, Yong Zhou, Gerald R.V. Hammond, John F. Hancock, and Kwang-jin Cho. Myotubularin-related proteins regulate kras function by controlling plasma membrane levels of polyphosphoinositides and phosphatidylserine. bioRxiv, Jan 2024. URL: https://doi.org/10.1101/2024.01.22.576612, doi:10.1101/2024.01.22.576612. This article has 1 citations.

15. (kennelly2001proteinphosphatasesaphylogenetic pages 1-2): Peter J. Kennelly. Protein phosphatases–a phylogenetic perspective. Chemical reviews, 101 8:2291-312, Jun 2001. URL: https://doi.org/10.1021/cr0002543, doi:10.1021/cr0002543. This article has 114 citations and is from a highest quality peer-reviewed journal.

16. (brenchley2007thetritrypphosphatome pages 2-3): Rachel Brenchley, Humera Tariq, Helen McElhinney, Balázs Szöőr, Julie Huxley-Jones, Robert Stevens, Keith Matthews, and Lydia Tabernero. The tritryp phosphatome: analysis of the protein phosphatase catalytic domains. BMC Genomics, 8:434-434, Nov 2007. URL: https://doi.org/10.1186/1471-2164-8-434, doi:10.1186/1471-2164-8-434. This article has 115 citations and is from a peer-reviewed journal.

17. (derkaczew2023thegeneticbackground pages 1-3): Maria Derkaczew, Piotr Martyniuk, Robert Hofman, Krzysztof Rutkowski, Adam Osowski, and Joanna Wojtkiewicz. The genetic background of abnormalities in metabolic pathways of phosphoinositides and their linkage with the myotubular myopathies, neurodegenerative disorders, and carcinogenesis. Biomolecules, 13:1550, Oct 2023. URL: https://doi.org/10.3390/biom13101550, doi:10.3390/biom13101550. This article has 7 citations.

## Artifacts

- [Edison artifact artifact-00](PTHR10807-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](PTHR10807-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. begley2003crystalstructureof pages 1-2
2. amoasii2012myotubularinphosphoinositidephosphatases pages 4-8
3. saar2025themyotubularinrelated pages 1-2
4. lange2024myotubularinrelatedproteinsregulate pages 1-5
5. zaru2020challengesinthe pages 1-2
6. wang2024recentadvancesof pages 2-3
7. wang2024recentadvancesof pages 3-4
8. wang2024recentadvancesof pages 1-2
9. derkaczew2023thegeneticbackground pages 1-3
10. bong2016crystalstructureof pages 1-2
11. amoasii2012myotubularinphosphoinositidephosphatases pages 1-4
12. davies2012theptenand pages 1-3
13. kennelly2001proteinphosphatasesaphylogenetic pages 1-2
14. brenchley2007thetritrypphosphatome pages 2-3
15. PtdIns(3)P
16. PtdIns(3,5)P₂
17. PtdIns(5)P
18. MTMR15/FAN1 is no longer considered a myotubularin but a nuclease
19. https://doi.org/10.1007/978-94-007-5025-8\_10,
20. https://doi.org/10.1007/978-94-007-3012-0\_8,
21. https://doi.org/10.1371/journal.pone.0152611,
22. https://doi.org/10.1016/s1097-2765(03
23. https://doi.org/10.1016/s0960-9822(03
24. https://doi.org/10.3389/fcvm.2024.1364604,
25. https://doi.org/10.1002/prot.26774,
26. https://doi.org/10.1111/febs.15100,
27. https://doi.org/10.1074/mcp.m114.046086,
28. https://doi.org/10.1007/s00018-003-3062-3,
29. https://doi.org/10.1101/2024.01.22.576612,
30. https://doi.org/10.1021/cr0002543,
31. https://doi.org/10.1186/1471-2164-8-434,
32. https://doi.org/10.3390/biom13101550,