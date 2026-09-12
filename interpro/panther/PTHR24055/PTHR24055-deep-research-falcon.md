---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-21T20:59:27.591105'
end_time: '2026-06-21T21:10:31.193795'
duration_seconds: 663.6
template_file: templates/interpro_family_research.md
template_variables:
  interpro_id: PTHR24055
  interpro_name: MITOGEN-ACTIVATED PROTEIN KINASE
  interpro_short_name: Not specified
  interpro_type: family
  interpro_integrated: IPR050117
  member_databases: Not specified
  n_proteins: '62692'
  n_taxa: '10279'
  n_subfamilies: '127'
  interpro2go_terms: None mapped (no InterPro2GO terms for this entry)
  interpro_description: Not specified in InterPro
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
  path: PTHR24055-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: PTHR24055-deep-research-falcon_artifacts/artifact-01.md
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
- **Accession:** PTHR24055
- **Name:** MITOGEN-ACTIVATED PROTEIN KINASE
- **Short name:** Not specified
- **Entry type:** family
- **Integrated into / parent:** IPR050117
- **Member database signatures:** Not specified
- **Scale:** 62692 proteins across 10279 taxa, 127 subfamilies
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
**PTHR24055 (MITOGEN-ACTIVATED PROTEIN KINASE)**, structured to support GO annotation review.

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
- **Accession:** PTHR24055
- **Name:** MITOGEN-ACTIVATED PROTEIN KINASE
- **Short name:** Not specified
- **Entry type:** family
- **Integrated into / parent:** IPR050117
- **Member database signatures:** Not specified
- **Scale:** 62692 proteins across 10279 taxa, 127 subfamilies
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
**PTHR24055 (MITOGEN-ACTIVATED PROTEIN KINASE)**, structured to support GO annotation review.

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


# Comprehensive Research Report: InterPro Entry PTHR24055 (MITOGEN-ACTIVATED PROTEIN KINASE)

## Executive Summary

**Entry context:** PTHR24055 is a PANTHER family-level InterPro entry spanning 62,692 proteins across 10,279 taxa with 127 subfamilies. Currently, **no InterPro2GO terms are mapped** to this entry. This report evaluates whether GO annotations should be added and, if so, which terms are appropriate for the entire family versus subfamily-specific.

**Verdict:** The current absence of GO terms is **inappropriate**. Core MAPK biochemical functions should be annotated at the family level, but process- and component-level terms would systematically over-annotate due to extensive functional divergence across 127 subfamilies spanning ERK, JNK, p38, ERK5, and atypical MAPK groups.

---

## 1. Family Definition and Biochemistry

### Conserved Molecular Architecture

> MAPKs are conserved eukaryotic protein kinases built on the canonical bilobal protein kinase fold, with an N-lobe and C-lobe surrounding the ATP-binding cleft; this structural framework is retained from yeast to humans and underlies the shared catalytic mechanism of the family (juyoux2023architectureofthe pages 1-3, canovas2021diversityandversatility pages 1-2).
>
> A universal defining feature of canonical MAPKs is an activation-loop Thr-x-Tyr (TXY) motif that is phosphorylated by upstream MAP2Ks; dual phosphorylation of both residues is the core activating event and triggers the conformational changes required for high kinase activity (juyoux2023architectureofthe pages 1-3, martinezlimon2020thep38pathway pages 1-3, canovas2021diversityandversatility pages 1-2).
>
> MAPKs function as serine/threonine protein kinases and are proline-directed, meaning they phosphorylate Ser/Thr residues in substrate sequence contexts characteristic of MAPK signaling; this is a family-level biochemical property, even though precise substrate preferences differ among subfamilies (kassouf2020impactofconventional pages 1-3, huang2024reconstructingthedeep pages 1-3, canovas2021diversityandversatility pages 1-2).
>
> MAPKs share a conserved common docking surface/domain used by activators, substrates, regulators, and scaffolds; MAP2Ks engage this region through kinase interaction motifs, and substrate/regulator docking at this site is a major determinant of signaling specificity beyond the catalytic pocket itself (poti2024targetingakey pages 1-2, juyoux2023architectureofthe pages 1-3, huang2024reconstructingthedeep pages 1-3).
>
> Activation-loop control is central to the common MAPK mechanism: phosphorylation of the TXY motif reorients residues around ATP and Mg2+, stabilizes an active conformation, and promotes substrate recognition, so the regulated inactive-to-active conformational switch is a family-wide mechanistic hallmark (juyoux2023architectureofthe pages 1-3, martinezlimon2020thep38pathway pages 1-3).


*Blockquote: This blockquote summarizes the conserved molecular mechanism shared across MAPKs, highlighting which biochemical features are family-wide and thus most defensible for broad annotation. It is useful for separating universal MAPK properties from subfamily- or pathway-specific functions.*

All mitogen-activated protein kinases (MAPKs) share a conserved bilobal protein kinase fold comprising N-terminal and C-terminal lobes that cradle the ATP-binding cleft (juyoux2023architectureofthe pages 1-3). This structural scaffold is universally conserved from yeast to humans and provides the catalytic framework for the family (majeed2023harnessingtherole pages 1-2, huang2024reconstructingthedeep pages 1-3, canovas2021diversityandversatility pages 1-2).

### Critical Catalytic Features

**Activation loop and dual phosphorylation mechanism:** The defining molecular feature of canonical MAPKs is the Thr-X-Tyr (TXY) motif located in the activation loop within kinase subdomain VIII (juyoux2023architectureofthe pages 1-3, martinezlimon2020thep38pathway pages 1-3). Dual phosphorylation of both the threonine and tyrosine residues by upstream MAP2K dual-specificity kinases is absolutely required for full catalytic activity (juyoux2023architectureofthe pages 1-3, canovas2021diversityandversatility pages 1-2). This phosphorylation event triggers conformational changes: the activation loop adopts a more open configuration, the two major lobes rotate relative to one another, residues surrounding ATP and Mg²⁺ are reoriented into catalytically competent positions, and substrate recognition is enhanced (juyoux2023architectureofthe pages 1-3, martinezlimon2020thep38pathway pages 1-3, canovas2021diversityandversatility pages 1-2).

**TXY motif variants define subfamilies:** While the TXY signature is conserved, the identity of the central "X" residue distinguishes major MAPK groups: ERK subfamily members have TEY, JNK subfamily members have TPY, and p38 subfamily members have TGY (liu2021identificationcharacterizationand pages 1-2, kassouf2020impactofconventional pages 1-3, huang2024reconstructingthedeep pages 1-3). These sequence variations contribute to specificity in MAP2K recognition and activation (juyoux2023architectureofthe pages 1-3).

**Catalytic mechanism:** MAPKs function as proline-directed serine/threonine protein kinases (majeed2023harnessingtherole pages 1-2, kassouf2020impactofconventional pages 1-3, huang2024reconstructingthedeep pages 1-3, canovas2021diversityandversatility pages 1-2). They phosphorylate serine or threonine residues in their substrate proteins, typically in contexts where proline occupies positions flanking the phospho-acceptor site (huang2024reconstructingthedeep pages 1-3, canovas2021diversityandversatility pages 1-2). This substrate sequence selectivity is a family-wide biochemical property, although the precise optimal motifs differ substantially among subfamilies (johnson2023anatlasof pages 1-2, canovas2021diversityandversatility pages 1-2).

**Common docking domain:** All MAPKs possess a conserved common docking (CD) domain—also called the D-groove—on the kinase surface distinct from the active site (nandi2023mitogenactivatedproteinkinases pages 1-2, poti2024targetingakey pages 1-2, juyoux2023architectureofthe pages 1-3, huang2024reconstructingthedeep pages 1-3). Upstream MAP2Ks, substrates, regulators, and scaffolds bind to this shallow surface groove through short linear kinase interaction motifs (KIMs or D-motifs), and these protein-protein interactions are critical for pathway specificity and signal fidelity (poti2024targetingakey pages 1-2, juyoux2023architectureofthe pages 1-3, huang2024reconstructingthedeep pages 1-3). The D-groove contains a conserved cysteine residue (Cys161 in ERK2, Cys162 in p38α, Cys163 in JNK1) that can be targeted covalently by certain inhibitors (poti2024targetingakey pages 1-2).

### Conserved Structural Residues

Recent cryo-EM and crystallographic studies have confirmed that key catalytic residues and ATP-coordinating motifs are structurally conserved across the MAPK family (juyoux2023architectureofthe pages 1-3). The activation loop phosphorylation sites, the DFG motif involved in coordinating the catalytic metal ions, and the hydrophobic spine elements that stabilize the active conformation are all family-wide features (juyoux2023architectureofthe pages 1-3).

---

## 2. InterPro2GO Mapping Appropriateness

**Current state:** PTHR24055 has **zero GO terms** mapped via InterPro2GO.

### Recommended Core Annotations (Appropriate for ALL Members)

The following GO terms describe biochemical functions that are **experimentally verified and universally conserved** across the MAPK family and should be added:

1. **GO:0004707 (MAP kinase activity)** — The signature molecular function of the family (huang2024reconstructingthedeep pages 1-3, canovas2021diversityandversatility pages 1-2).
2. **GO:0016301 (kinase activity)** — Parent term; all MAPKs are active protein kinases (kassouf2020impactofconventional pages 1-3).
3. **GO:0006468 (protein phosphorylation)** — The core catalytic process mediated by all MAPKs (majeed2023harnessingtherole pages 1-2, kassouf2020impactofconventional pages 1-3).
4. **GO:0035556 (intracellular signal transduction)** — MAPKs universally function as signal transduction components linking upstream signals to downstream effectors (majeed2023harnessingtherole pages 1-2, nandi2023mitogenactivatedproteinkinases pages 1-2, huang2024reconstructingthedeep pages 1-3).
5. **GO:0000186 (activation of MAPKK activity)** may apply depending on feedback mechanisms, but should be carefully evaluated.

### Terms That Would OVER-ANNOTATE (Subfamily-Specific)

| Subfamily name | TXY motif variant | Primary activation signals | Key substrates/functions | Tissue distribution | Representative members |
|---|---|---|---|---|---|
| ERK1/2 (conventional MAPKs) | TEY | Primarily growth factors, GPCR ligands, cytokines, insulin, osmotic stress, and microtubule disorganization via RAF→MEK1/2→ERK1/2 cascades (kassouf2020impactofconventional pages 1-3, nandi2023mitogenactivatedproteinkinases pages 1-2) | Phosphorylate RSK, MSK, MNK, Elk-1, c-Fos and cytoskeletal regulators; broadly linked to proliferation, differentiation, survival, metabolism, cell motility, and gene-expression programs (kassouf2020impactofconventional pages 1-3, nandi2023mitogenactivatedproteinkinases pages 1-2) | Expressed in all tissues; particularly high in brain, skeletal muscle, thymus, and heart in mammals (kassouf2020impactofconventional pages 1-3) | MAPK3/ERK1, MAPK1/ERK2 (kassouf2020impactofconventional pages 1-3) |
| JNKs / SAPKs (conventional MAPKs) | TPY | Environmental and genotoxic stresses including hypoxia, UV and ionizing radiation, cytokines, pathogens, toxins, drugs, and metabolic stress; activated mainly through MKK4/MKK7 (liu2021identificationcharacterizationand pages 1-2, kassouf2020impactofconventional pages 3-4, martinezlimon2020thep38pathway pages 1-3) | Phosphorylate c-Jun, ATF2, Elk-1, p53, BH3-only proteins and other transcriptional regulators; associated with stress responses, inflammation, apoptosis, differentiation, proliferation, and metabolic reprogramming (liu2021identificationcharacterizationand pages 1-2, kassouf2020impactofconventional pages 3-4, martinezlimon2020thep38pathway pages 1-3) | Family members show isoform- and tissue-specific expression; functional outputs depend strongly on cell type and context (martinezlimon2020thep38pathway pages 1-3) | JNK1/MAPK8, JNK2/MAPK9, JNK3/MAPK10 (kassouf2020impactofconventional pages 1-3, martinezlimon2020thep38pathway pages 1-3) |
| p38 MAPKs / SAPKs (conventional MAPKs) | TGY | Environmental and intracellular stress, inflammatory cytokines, osmotic shock, oxidative stress, DNA damage, ischemia, hypoxia, UV; activated mainly by MKK3/MKK6 and sometimes MKK4; noncanonical activation can occur via TAB1 binding or Tyr323-dependent autophosphorylation in T cells (juyoux2023architectureofthe pages 1-3, martinezlimon2020thep38pathway pages 1-3, canovas2021diversityandversatility pages 1-2) | Regulate inflammatory signaling, stress adaptation, differentiation, apoptosis, gene expression, nucleosome dynamics, mRNA translation, and immune responses; substrates include MSK1/2, MNK1/2, p53, ATF2, NF-κB-related outputs and many context-specific effectors (kassouf2020impactofconventional pages 3-4, martinezlimon2020thep38pathway pages 1-3, canovas2021diversityandversatility pages 1-2) | p38α and p38β are broadly expressed; p38α usually predominates. p38γ and p38δ are more tissue-restricted and have more specialized functions (martinezlimon2020thep38pathway pages 1-3, canovas2021diversityandversatility pages 1-2) | p38α/MAPK14, p38β/MAPK11, p38γ/MAPK12, p38δ/MAPK13 (martinezlimon2020thep38pathway pages 1-3, canovas2021diversityandversatility pages 1-2) |
| ERK5 (conventional MAPK) | TEY | Growth factors, inflammatory cytokines, oxidative stress, osmotic stress, ischemia, and hypoxia via MEK5→ERK5 (kassouf2020impactofconventional pages 1-3, nandi2023mitogenactivatedproteinkinases pages 1-2) | Linked to transcriptional regulation through MEF2, Elk-1 and Sap1a; implicated in proliferation, differentiation, mechanoreception, and stress-responsive signaling (nandi2023mitogenactivatedproteinkinases pages 1-2, huang2024reconstructingthedeep pages 1-3) | Broad eukaryotic MAPK family member, but less well characterized than ERK1/2, JNK, or p38 in the retrieved sources (nandi2023mitogenactivatedproteinkinases pages 1-2, huang2024reconstructingthedeep pages 1-3) | MAPK7/ERK5 (kassouf2020impactofconventional pages 1-3, huang2024reconstructingthedeep pages 1-3) |
| Atypical MAPKs | Variable/noncanonical; family members do not uniformly follow the classical three-tier cascade, though MAPKs generally retain a T-x-Y activation-loop signature | Often regulated by noncanonical mechanisms, including autophosphorylation or other signaling molecules rather than classical MAP2K cascades (kassouf2020impactofconventional pages 1-3, huang2024reconstructingthedeep pages 1-3) | Functional roles are diverse and less uniformly defined; contribute to specialized signaling outputs and expand MAPK network diversity rather than sharing one common canonical role (kassouf2020impactofconventional pages 1-3, huang2024reconstructingthedeep pages 1-3) | Distributed across eukaryotes with polyphyletic origin inferred for atypical MAPKs; regulation and functions are less conserved than for conventional groups (huang2024reconstructingthedeep pages 1-3) | ERK3/MAPK6, ERK4/MAPK4, ERK7/8/MAPK15, NLK (kassouf2020impactofconventional pages 1-3, huang2024reconstructingthedeep pages 1-3) |


*Table: This table summarizes the major MAPK subfamilies, their activation-loop motifs, upstream signals, core substrates and functions, tissue distribution, and representative members. It is useful for assessing whether broad GO annotations are appropriate across the full MAPK family or only for specific subfamilies.*

The MAPK family exhibits **profound functional divergence** across its 127 subfamilies. The following types of GO terms are NOT appropriate at the family level and would systematically over-annotate proteins:

**a) Stress response terms (JNK/p38-specific):**
- GO terms related to "response to oxidative stress," "response to UV," "response to osmotic stress," "response to inflammatory cytokines," etc., accurately describe p38 and JNK subfamily members but do NOT apply to ERK1/2, which primarily respond to growth factors and mitogens (kassouf2020impactofconventional pages 1-3, martinezlimon2020thep38pathway pages 1-3, canovas2021diversityandversatility pages 1-2).

**b) Growth factor response terms (ERK-specific):**
- Terms like "response to growth factor," "EGF receptor signaling pathway," "regulation of cell proliferation via ERK cascade" are specific to the ERK subfamily and do not apply to stress-activated kinases JNK and p38 (kassouf2020impactofconventional pages 1-3, martinezlimon2020thep38pathway pages 1-3).

**c) Specific substrate/effector terms:**
- GO annotations for phosphorylation of specific substrates such as "c-Jun phosphorylation" (JNK-specific), "p53 phosphorylation" (context-dependent), or "RSK activation" (ERK-specific) are subfamily-restricted and cannot be applied family-wide (kassouf2020impactofconventional pages 1-3, kassouf2020impactofconventional pages 3-4, martinezlimon2020thep38pathway pages 1-3, canovas2021diversityandversatility pages 1-2).

**d) Tissue- or cell-type-specific process terms:**
- p38γ and p38δ isoforms show restricted tissue expression and specialized functions (e.g., p38δ in glucose homeostasis, keratinocyte differentiation) that do not generalize to the ubiquitously expressed p38α, p38β, ERK1/2, or JNK proteins (martinezlimon2020thep38pathway pages 1-3, canovas2021diversityandversatility pages 1-2).

**e) Cellular compartment terms:**
- While activated MAPKs can translocate to the nucleus, not all subfamily members or all cell contexts involve nuclear translocation; compartment annotations should be applied cautiously or at the subfamily level.

### Recommendation

**ACTION: ADD CORE GO TERMS** for conserved MAPK molecular function and basic signal transduction role.  
**DO NOT ADD** pathway-specific, stimulus-specific, or substrate-specific terms at the PTHR24055 family level.  
**DELEGATE** such annotations to subfamily-specific child entries (if they exist within PANTHER's 127 subfamilies) or clearly flag them as context-dependent.

---

## 3. Functional Divergence Across the Family

### Major Subfamily Functional Specialization

The MAPK family is **not functionally homogeneous**. Instead, it comprises multiple subfamilies with **distinct and sometimes opposite** biological roles:

**ERK1/2 subfamily (MAPK3/MAPK1, TEY motif):**  
Activated primarily by growth factors, GPCR ligands, and mitogens via the RAF→MEK1/2→ERK1/2 cascade (kassouf2020impactofconventional pages 1-3, nandi2023mitogenactivatedproteinkinases pages 1-2). ERK1/2 promote cell proliferation, survival, differentiation, and metabolism (kassouf2020impactofconventional pages 1-3, kassouf2020impactofconventional pages 3-4, martinezlimon2020thep38pathway pages 1-3). They are generally considered pro-survival and proliferative kinases, and dysregulation leads to cancer (martinezlimon2020thep38pathway pages 1-3, canovas2021diversityandversatility pages 1-2).

**JNK subfamily (MAPK8/9/10, TPY motif):**  
Also called stress-activated protein kinases (SAPKs), JNKs respond to environmental and genotoxic stresses including UV irradiation, hypoxia, oxidative stress, inflammatory cytokines, and pathogen signals (liu2021identificationcharacterizationand pages 1-2, kassouf2020impactofconventional pages 1-3, kassouf2020impactofconventional pages 3-4, martinezlimon2020thep38pathway pages 1-3). JNKs phosphorylate c-Jun, ATF2, p53, and BH3-only proteins, driving stress responses, inflammation, and apoptosis (kassouf2020impactofconventional pages 3-4, martinezlimon2020thep38pathway pages 1-3). Functionally, JNKs often promote cell death or inflammatory signaling, contrasting with ERK's pro-survival role.

**p38 subfamily (MAPK14/11/12/13, TGY motif):**  
Like JNKs, p38 kinases are stress-activated and respond to osmotic shock, oxidative stress, inflammatory cytokines, DNA damage, ischemia, and infection (juyoux2023architectureofthe pages 1-3, martinezlimon2020thep38pathway pages 1-3, canovas2021diversityandversatility pages 1-2). The p38 isoforms (α, β, γ, δ) show differential tissue distribution: p38α and p38β are ubiquitously expressed (p38α predominating), whereas p38γ and p38δ have more restricted expression and specialized functions (martinezlimon2020thep38pathway pages 1-3, canovas2021diversityandversatility pages 1-2). p38α is essential for mouse placental development, whereas other isoforms are viable when knocked out (martinezlimon2020thep38pathway pages 1-3). p38 kinases regulate cytokine biosynthesis, immune responses, differentiation, and apoptosis (martinezlimon2020thep38pathway pages 1-3, canovas2021diversityandversatility pages 1-2).

**ERK5 (MAPK7, TEY motif):**  
Responds to growth factors and stresses via the MEK5→ERK5 pathway (kassouf2020impactofconventional pages 1-3, huang2024reconstructingthedeep pages 1-3). ERK5 is involved in proliferation, differentiation, and mechanoreception but is less well characterized than ERK1/2, JNK, or p38 (huang2024reconstructingthedeep pages 1-3).

**Atypical MAPKs (ERK3/4, ERK7, NLK):**  
These do not conform to the canonical three-tier MAP3K→MAP2K→MAPK activation cascade and are instead regulated by autophosphorylation or alternative mechanisms (kassouf2020impactofconventional pages 1-3, huang2024reconstructingthedeep pages 1-3). Phylogenetic analysis suggests a **polyphyletic origin** for atypical MAPKs, indicating they arose independently multiple times during evolution (huang2024reconstructingthedeep pages 1-3). Their biological roles are diverse and less uniformly defined than conventional MAPKs.

### Substrate Specificity Diversity

Recent kinome-wide profiling using positional scanning peptide arrays revealed that MAPK substrate specificity is **substantially more diverse than expected** and driven extensively by **negative selectivity** (johnson2023anatlasof pages 1-2). Different MAPK subfamilies recognize distinct optimal phosphorylation motifs: for example, ERK, JNK, and p38 subfamilies each have characteristic substrate preferences that extend beyond the proline-directed consensus (johnson2023anatlasof pages 1-2, canovas2021diversityandversatility pages 1-2). This substrate diversity ensures pathway specificity even when MAPKs share the same cellular compartment.

### Catalogued Pseudo-Kinases and Catalytically Inactive Variants

While atypical MAPKs exist with non-canonical regulation, **true catalytically dead MAPK pseudo-kinases appear to be rare or absent** in the PTHR24055 family (shrestha2020cataloguingthedead pages 1-2, huang2024reconstructingthedeep pages 1-3). Atypical MAPKs retain kinase activity but use alternative activation mechanisms rather than being pseudo-enzymes (kassouf2020impactofconventional pages 1-3, shrestha2020cataloguingthedead pages 1-2). Therefore, annotations of "protein kinase activity" and "protein phosphorylation" are broadly appropriate and unlikely to mislabel inactive pseudo-kinase members.

---

## 4. Taxonomic Scope

### Eukaryote-Wide Distribution

MAPKs are **ancient and universally conserved** across all major eukaryotic lineages (huang2024reconstructingthedeep pages 1-3). Phylogenetic reconstruction places the most recent common ancestor (MRCA) of the MAPK signaling network at approximately **2 billion years ago**, predating the divergence of animals, fungi, and plants (huang2024reconstructingthedeep pages 1-3).

### Evolutionary Expansion Pulses

Two major coevolutionary expansion events have been identified (huang2024reconstructingthedeep pages 1-3):
1. **Pre-animal/fungi divergence:** One expansion pulse occurred before the split between animal and fungal lineages.
2. **Pre-animal origin:** A second pulse predates the origin of animals, contributing to the functional diversity observed in extant metazoan MAPKs.

These expansions involved parallel radiation of all three tiers of the cascade (MAP3K, MAP2K, MAPK), showcasing a striking case of **multi-tier coevolution** (huang2024reconstructingthedeep pages 1-3).

### Functional Conservation Across Clades

The **core three-tier MAPK cascade architecture** (MAP3K→MAP2K→MAPK) is conserved from yeast (e.g., *Saccharomyces cerevisiae* HOG1 pathway) to humans (majeed2023harnessingtherole pages 1-2, liu2021identificationcharacterizationand pages 1-2, huang2024reconstructingthedeep pages 1-3). MAPKs are found in plants, fungi, and animals, with orthologs performing analogous signal transduction roles in stress response, development, and immunity (majeed2023harnessingtherole pages 1-2, huang2024reconstructingthedeep pages 1-3).

However, **functional outputs have diverged extensively** across taxa. For example, plant MAPKs participate in pathogen defense and abiotic stress responses distinct from animal immune or developmental programs (majeed2023harnessingtherole pages 1-2). Fungal MAPKs regulate mating, cell wall integrity, and osmotic stress responses (huang2024reconstructingthedeep pages 1-3). Thus, while the catalytic mechanism and cascade architecture are universally conserved, the **specific biological processes** regulated by MAPKs are **not conserved across all 10,279 taxa**.

### Implications for GO Annotations

Given this taxonomic breadth:
- **Molecular function terms** (e.g., MAP kinase activity, protein kinase activity) are appropriate across all taxa.
- **Biological process terms** tied to specific stimuli (e.g., "response to growth factor" in animals, "response to pathogen" in plants) or specific pathways (e.g., "MAPK cascade involved in osmotic stress response" in fungi vs. "JNK cascade" in animals) are **clade-specific** and would over-annotate when applied to a pan-eukaryotic family entry.

---

## 5. Over-Annotation Verdict and Recommendations

### Summary

**PTHR24055 represents a functionally divergent protein family spanning 127 subfamilies with distinct activation signals, substrates, and biological outcomes.** The entry type is **family**, meaning it groups proteins by homology but does NOT guarantee functional homogeneity.

### Verdict

**PARTIALLY SOUND WITH CRITICAL GAPS:**

1. **Current absence of GO terms is inappropriate.** Core MAPK molecular functions should be annotated.
2. **Adding subfamily-specific GO terms to PTHR24055 would systematically over-annotate** 62,692 proteins, many of which do not participate in the specific processes (e.g., annotating all MAPKs with "stress response" mislabels ERK1/2; annotating with "growth factor response" mislabels JNK/p38).
3. **PANTHER's 127 subfamilies likely correspond to functionally coherent groups** (e.g., ERK subfamily, JNK subfamily, p38 subfamily). Process-level and component-level annotations should be applied at the **subfamily level**, not the parent family level.

### Recommended GO Action Pattern

**For PTHR24055 (family level):**

| GO Term Category | Recommended Action | Rationale |
|---|---|---|
| **Core molecular function** (GO:0004707 MAP kinase activity, GO:0016301 kinase activity, GO:0006468 protein phosphorylation) | **ADD / ACCEPT** | Experimentally verified, universally conserved across all MAPKs |
| **Basic signaling process** (GO:0035556 intracellular signal transduction) | **ADD / ACCEPT** | All MAPKs mediate signal transduction |
| **ATP binding** (GO:0005524) | **ACCEPT (but generic)** | Universal for active kinases; carries little specific information |
| **Metal ion binding** (GO:0046872) | **ACCEPT (but generic)** | Mg²⁺ required for catalysis; universal but low information content |
| **Stress response terms** (e.g., GO:0006950, GO:0034599) | **REMOVE or MARK_AS_SUBFAMILY_SPECIFIC** | Only true for JNK/p38 subfamilies; false for ERK |
| **Growth factor response** (e.g., GO:0071363) | **REMOVE or MARK_AS_SUBFAMILY_SPECIFIC** | Only true for ERK subfamily; false for JNK/p38 |
| **Specific substrate phosphorylation** (e.g., c-Jun, p53, RSK) | **REMOVE or DELEGATE to subfamilies** | Substrate specificity is subfamily-dependent |
| **Nucleus** (GO:0005634) | **Context-dependent; prefer KEEP_AS_NON_CORE or subfamily-level** | Not all MAPKs translocate to nucleus in all contexts |

**For PTHR24055 subfamilies (if addressable in InterPro/PANTHER):**

- **DELEGATE** pathway-specific, stimulus-specific, and substrate-specific annotations to the appropriate subfamily entries.
- For example, if a "PTHR24055:SF###" corresponds to the p38α group, annotate it with stress-response and inflammatory GO terms. If another corresponds to ERK1/2, annotate with proliferation and growth-factor-response terms.

### Recommendation for InterPro Curators

**MODIFY-to-specific:**  
Do NOT apply whole-protein process terms (stress response, growth factor signaling, specific substrate interactions) to PTHR24055. Instead:
1. Add conserved molecular function and basic signal transduction terms.
2. Push process-specific annotations down to subfamily-level entries.
3. If InterPro does not currently integrate PANTHER subfamilies, consider flagging this family as requiring subfamily-level curation or issuing a cautionary note that functional annotations may not apply uniformly.

**Final Recommendation Code:** **MODIFY / SUBFAMILY_CURATION_REQUIRED**

---

## Conclusion

PTHR24055 (MITOGEN-ACTIVATED PROTEIN KINASE) is an ancient, eukaryote-wide protein family with a conserved catalytic core but extensive functional diversification across 127 subfamilies. The current lack of GO annotations is a gap that should be filled with conserved molecular function terms. However, applying process-level GO terms at the family level would systematically over-annotate due to the opposing biological roles of ERK (proliferation, growth), JNK (stress, apoptosis), and p38 (stress, inflammation) subfamilies. **InterPro2GO annotations should be restricted to universally conserved MAPK functions, with pathway-specific terms delegated to subfamily-level entries.**

---

**References:**  
All citations correspond to context IDs in the format () as provided during evidence gathering.

References

1. (juyoux2023architectureofthe pages 1-3): Pauline Juyoux, Ioannis Galdadas, Dorothea Gobbo, Jill von Velsen, Martin Pelosse, Mark Tully, Oscar Vadas, Francesco Luigi Gervasio, Erika Pellegrini, and Matthew W. Bowler. Architecture of the mkk6-p38α complex defines the basis of mapk specificity and activation. Science, 381:1217-1225, Sep 2023. URL: https://doi.org/10.1126/science.add7859, doi:10.1126/science.add7859. This article has 48 citations and is from a highest quality peer-reviewed journal.

2. (canovas2021diversityandversatility pages 1-2): Begoña Canovas and Angel R. Nebreda. Diversity and versatility of p38 kinase signalling in health and disease. Nature Reviews. Molecular Cell Biology, 22:346-366, Jan 2021. URL: https://doi.org/10.1038/s41580-020-00322-w, doi:10.1038/s41580-020-00322-w. This article has 727 citations.

3. (martinezlimon2020thep38pathway pages 1-3): Adrián Martínez-Limón, Manel Joaquin, María Caballero, Francesc Posas, and Eulàlia de Nadal. The p38 pathway: from biology to cancer therapy. International Journal of Molecular Sciences, 21:1913, Mar 2020. URL: https://doi.org/10.3390/ijms21061913, doi:10.3390/ijms21061913. This article has 507 citations.

4. (kassouf2020impactofconventional pages 1-3): Toufic Kassouf and Grzegorz Sumara. Impact of conventional and atypical mapks on the development of metabolic diseases. Biomolecules, 10:1256, Aug 2020. URL: https://doi.org/10.3390/biom10091256, doi:10.3390/biom10091256. This article has 114 citations.

5. (huang2024reconstructingthedeep pages 1-3): EJ Huang, Jeeun Parksong, Amy F. Peterson, Fernando Torres, Sergi Regot, and Gabriel S. Bever. Reconstructing the deep phylogeny of the mapk signaling network: functional specialization via multi-tier coevolutionary expansion. bioRxiv, Oct 2024. URL: https://doi.org/10.1101/2024.10.01.616093, doi:10.1101/2024.10.01.616093. This article has 0 citations.

6. (poti2024targetingakey pages 1-2): Ádám Levente Póti, Dániel Bálint, Anita Alexa, Péter Sok, Kristóf Ozsváth, Krisztián Albert, Gábor Turczel, Sarolt Magyari, Orsolya Ember, Kinga Papp, Sándor Balázs Király, Tímea Imre, Krisztina Németh, Tibor Kurtán, Gergő Gógl, Szilárd Varga, Tibor Soós, and Attila Reményi. Targeting a key protein-protein interaction surface on mitogen-activated protein kinases by a precision-guided warhead scaffold. Nature Communications, Oct 2024. URL: https://doi.org/10.1038/s41467-024-52574-1, doi:10.1038/s41467-024-52574-1. This article has 7 citations and is from a highest quality peer-reviewed journal.

7. (majeed2023harnessingtherole pages 1-2): Yasir Majeed, Xi Zhu, Ning Zhang, Noor ul-Ain, Ali Raza, Fasih Ullah Haider, and Huaijun Si. Harnessing the role of mitogen-activated protein kinases against abiotic stresses in plants. Frontiers in Plant Science, Feb 2023. URL: https://doi.org/10.3389/fpls.2023.932923, doi:10.3389/fpls.2023.932923. This article has 72 citations.

8. (liu2021identificationcharacterizationand pages 1-2): Zhi Liu, Xiaoting Huang, Zujing Yang, Cheng Peng, Haitao Yu, Chang Cui, Yuqing Hu, Xuefeng Wang, Qiang Xing, Jingjie Hu, and Zhenmin Bao. Identification, characterization, and expression analysis reveal diverse regulated roles of three mapk genes in chlamys farreri under heat stress. Frontiers in Physiology, Jul 2021. URL: https://doi.org/10.3389/fphys.2021.688626, doi:10.3389/fphys.2021.688626. This article has 20 citations.

9. (johnson2023anatlasof pages 1-2): Jared L. Johnson, Tomer M. Yaron, Emily M. Huntsman, Alexander Kerelsky, Junho Song, Amit Regev, Ting-Yu Lin, Katarina Liberatore, Daniel M. Cizin, Benjamin M. Cohen, Neil Vasan, Yilun Ma, Konstantin Krismer, Jaylissa Torres Robles, Bert van de Kooij, Anne E. van Vlimmeren, Nicole Andrée-Busch, Norbert F. Käufer, Maxim V. Dorovkov, Alexey G. Ryazanov, Yuichiro Takagi, Edward R. Kastenhuber, Marcus D. Goncalves, Benjamin D. Hopkins, Olivier Elemento, Dylan J. Taatjes, Alexandre Maucuer, Akio Yamashita, Alexei Degterev, Mohamed Uduman, Jingyi Lu, Sean D. Landry, Bin Zhang, Ian Cossentino, Rune Linding, John Blenis, Peter V. Hornbeck, Benjamin E. Turk, Michael B. Yaffe, and Lewis C. Cantley. An atlas of substrate specificities for the human serine/threonine kinome. Nature, 613:759-766, Jan 2023. URL: https://doi.org/10.1038/s41586-022-05575-3, doi:10.1038/s41586-022-05575-3. This article has 764 citations and is from a highest quality peer-reviewed journal.

10. (nandi2023mitogenactivatedproteinkinases pages 1-2): Ipsita Nandi and Benjamin Aroeti. Mitogen-activated protein kinases (mapks) and enteric bacterial pathogens: a complex interplay. International Journal of Molecular Sciences, 24:11905, Jul 2023. URL: https://doi.org/10.3390/ijms241511905, doi:10.3390/ijms241511905. This article has 31 citations.

11. (kassouf2020impactofconventional pages 3-4): Toufic Kassouf and Grzegorz Sumara. Impact of conventional and atypical mapks on the development of metabolic diseases. Biomolecules, 10:1256, Aug 2020. URL: https://doi.org/10.3390/biom10091256, doi:10.3390/biom10091256. This article has 114 citations.

12. (shrestha2020cataloguingthedead pages 1-2): Safal Shrestha, Dominic P. Byrne, John A. Harris, Natarajan Kannan, and Patrick A. Eyers. Cataloguing the dead: breathing new life into pseudokinase research. Mar 2020. URL: https://doi.org/10.1111/febs.15246, doi:10.1111/febs.15246. This article has 54 citations.

## Artifacts

- [Edison artifact artifact-00](PTHR24055-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](PTHR24055-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. juyoux2023architectureofthe pages 1-3
2. poti2024targetingakey pages 1-2
3. kassouf2020impactofconventional pages 1-3
4. huang2024reconstructingthedeep pages 1-3
5. johnson2023anatlasof pages 1-2
6. majeed2023harnessingtherole pages 1-2
7. canovas2021diversityandversatility pages 1-2
8. liu2021identificationcharacterizationand pages 1-2
9. nandi2023mitogenactivatedproteinkinases pages 1-2
10. kassouf2020impactofconventional pages 3-4
11. shrestha2020cataloguingthedead pages 1-2
12. https://doi.org/10.1126/science.add7859,
13. https://doi.org/10.1038/s41580-020-00322-w,
14. https://doi.org/10.3390/ijms21061913,
15. https://doi.org/10.3390/biom10091256,
16. https://doi.org/10.1101/2024.10.01.616093,
17. https://doi.org/10.1038/s41467-024-52574-1,
18. https://doi.org/10.3389/fpls.2023.932923,
19. https://doi.org/10.3389/fphys.2021.688626,
20. https://doi.org/10.1038/s41586-022-05575-3,
21. https://doi.org/10.3390/ijms241511905,
22. https://doi.org/10.1111/febs.15246,