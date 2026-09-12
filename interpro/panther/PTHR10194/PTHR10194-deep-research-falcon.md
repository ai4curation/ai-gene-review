---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-21T19:47:37.516235'
end_time: '2026-06-21T19:58:31.427868'
duration_seconds: 653.91
template_file: templates/interpro_family_research.md
template_variables:
  interpro_id: PTHR10194
  interpro_name: RAS GTPASE-ACTIVATING PROTEINS
  interpro_short_name: Not specified
  interpro_type: family
  interpro_integrated: IPR039360
  member_databases: Not specified
  n_proteins: '24424'
  n_taxa: '7495'
  n_subfamilies: '20'
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
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: PTHR10194-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# InterPro Family Research for GO Annotation Review

## ⚠️ CRITICAL: Family Identification Context

**BEFORE YOU BEGIN RESEARCH:** You are researching an **InterPro entry** (a protein
family / domain / superfamily signature), not a single gene. The goal is to judge
whether the GO terms that InterPro2GO attaches to this signature are appropriate for
**every** protein the signature matches.

### Target InterPro Entry (from the InterPro API):
- **Accession:** PTHR10194
- **Name:** RAS GTPASE-ACTIVATING PROTEINS
- **Short name:** Not specified
- **Entry type:** family
- **Integrated into / parent:** IPR039360
- **Member database signatures:** Not specified
- **Scale:** 24424 proteins across 7495 taxa, 20 subfamilies
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
**PTHR10194 (RAS GTPASE-ACTIVATING PROTEINS)**, structured to support GO annotation review.

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
- **Accession:** PTHR10194
- **Name:** RAS GTPASE-ACTIVATING PROTEINS
- **Short name:** Not specified
- **Entry type:** family
- **Integrated into / parent:** IPR039360
- **Member database signatures:** Not specified
- **Scale:** 24424 proteins across 7495 taxa, 20 subfamilies
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
**PTHR10194 (RAS GTPASE-ACTIVATING PROTEINS)**, structured to support GO annotation review.

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


# Comprehensive Research Report: PTHR10194 (RAS GTPASE-ACTIVATING PROTEINS)

## Executive Summary

InterPro entry PTHR10194 represents the RAS GTPase-activating protein (RasGAP) family, spanning 24,424 proteins across 7,495 taxa with 20 subfamilies. This entry is designated as type "family" (not domain or superfamily), which has important implications for GO annotation. **Critically, this entry currently has NO InterPro2GO mappings, which is actually appropriate given the substantial functional heterogeneity within this family.** The family includes both catalytically active RasGAPs and catalytically inactive pseudoGAPs, with substrate specificities ranging from Ras-selective to dual Ras/Rap to Rap-selective, making broad functional annotation problematic.

---

## 1. Family Definition and Biochemistry

### Structural Architecture

The canonical RasGAP catalytic module is a ~35 kDa largely helical protein comprising two structural subdomains: a central catalytic domain (GAPc) that contains the enzymatic machinery and an extra domain (GAPex) that is structurally conserved but dispensable for catalytic activity (scheffzek2019rasspecificgtpaseactivatingproteinsstructures pages 1-3, scheffzek2019rasspecificgtpaseactivatingproteinsstructures pages 3-4). The structure was first determined for the catalytic domain of p120GAP/RASA1 and has since been confirmed across multiple RasGAP family members (scheffzek2019rasspecificgtpaseactivatingproteinsstructures pages 1-3).

### Catalytic Mechanism

RasGAPs accelerate GTP hydrolysis on Ras family small GTPases through a transition state-stabilizing mechanism (scheffzek2019rasspecificgtpaseactivatingproteinsstructures pages 1-3, scheffzek2019rasspecificgtpaseactivatingproteinsstructures pages 3-4). The critical mechanistic features include:

1. **Arginine finger motif**: The catalytic core contains a conserved arginine residue (Arg789 in p120GAP/RASA1, Arg1276 in neurofibromin) that inserts into the GTPase active site to contact the β/γ phosphate region and stabilize the transition state of the phosphoryl transfer reaction (scheffzek2019rasspecificgtpaseactivatingproteinsstructures pages 4-6, scheffzek2019rasspecificgtpaseactivatingproteinsstructures pages 3-4). Even conservative substitution to lysine reduces GAP activity by three orders of magnitude (scheffzek2019rasspecificgtpaseactivatingproteinsstructures pages 3-4).

2. **FLRV motif**: The arginine-containing finger loop is stabilized by residues from the conserved FLRV (Phe-Leu-Arg-Val) motif (scheffzek2019rasspecificgtpaseactivatingproteinsstructures pages 3-4).

3. **Switch region stabilization**: RasGAPs stabilize the switch I and switch II regions of Ras, which are frequently flexible in isolated Ras structures, and correctly orient the critical Gln61 residue to position a water molecule for nucleophilic attack (scheffzek2019rasspecificgtpaseactivatingproteinsstructures pages 4-6, scheffzek2019rasspecificgtpaseactivatingproteinsstructures pages 3-4).

### Recent Structural Insights: The C2 Domain Contribution

A major recent discovery (2025) is that nine of the ten GAPs for Ras contain a C2 domain immediately N-terminal to the GAP domain, and this C2 domain directly augments catalytic activity (paul2025thec2domain pages 3-4, paul2025thec2domain pages 2-3). Structural studies revealed:

- The C2-GAP construct exhibits significantly increased catalytic efficiency (primarily driven by increased kcat) compared to the GAP domain alone (paul2025thec2domain pages 2-3).
- Crystal structures show the C2 domain can approach within 7 Å of Ras, and AlphaFold models predict direct contact between the C2 domain and the Ras allosteric lobe (paul2025thec2domain pages 3-4, paul2025thec2domain pages 2-3).
- Sequence alignment of 209 RasGAP sequences from humans to sponges reveals a completely conserved surface patch in the C2 domain (centered on residue R707 in human RASA1, equivalent to R698 in mouse) that is predicted to interact with Ras (paul2025thec2domain pages 3-4, paul2025thec2domain pages 2-3).
- Mutation of R707 (R707S or R707D) abrogates the catalytic advantage conferred by the C2 domain (paul2025thec2domain pages 2-3).
- Mouse models with the R698C mutation (equivalent to human pathogenic R707C) are embryonic lethal with vascular defects phenocopying loss of RasGAP, demonstrating the essential in vivo role of this C2 domain surface (paul2025thec2domain pages 2-3).

This C2 domain augmentation appears conserved across the RasGAP family, with functional importance confirmed for SynGAP as well (paul2025thec2domain pages 2-3).

### Conserved Residues and Fold

The G domain of target GTPases contains five conserved motifs (G1-G5) critical for nucleotide binding (mishra2016invitedreviewsmall pages 1-2). The RasGAP domain recognizes primarily the Switch regions (coinciding with G2 and G3 motifs) and the P-loop region of Ras (scheffzek2019rasspecificgtpaseactivatingproteinsstructures pages 4-6, scheffzek2019rasspecificgtpaseactivatingproteinsstructures pages 3-4). The catalytic mechanism involves a multi-step process: adoption of the GTP-bound ON-state, movement of the catalytic arginine into the active site, simultaneous GTP hydrolysis forming a protein-bound Pi intermediate, and finally Pi release with switch regions returning to the OFF-state (scheffzek2019rasspecificgtpaseactivatingproteinsstructures pages 6-7).

---

## 2. InterPro2GO Mapping Appropriateness

**Current status: PTHR10194 has NO InterPro2GO terms mapped.**

### Assessment

This absence of GO mappings is **appropriate and should be maintained** for the following reasons:

#### Problem 1: Subfamily-specific substrate preferences

The RasGAP family exhibits substantial substrate divergence:

- **Ras-selective**: p120GAP/RASA1 and NF1 are primarily Ras-specific (scheffzek2019rasspecificgtpaseactivatingproteinsstructures pages 1-3, scheffzek2019rasspecificgtpaseactivatingproteinsstructures pages 3-4).
- **Dual Ras/Rap specificity**: Within the GAP1 family, RASA3 (GAPIP4BP), RASA4 (CAPRI), and RASAL1 have been experimentally demonstrated to inactivate both Ras and Rap family members (scheffzek2019rasspecificgtpaseactivatingproteinsstructures pages 3-4, scheffzek2019rasspecificgtpaseactivatingproteinsstructures pages 6-7). These dual-target RasGAPs use a canonical arginine finger mechanism but can accommodate both Ras (with Gln61) and Rap (with Thr61 replacing the catalytic glutamine) (scheffzek2019rasspecificgtpaseactivatingproteinsstructures pages 4-6).
- **Rap-selective**: Plexins contain an intracellular RasGAP-like domain that functions on Rap1/2 rather than classical Ras (scheffzek2019rasspecificgtpaseactivatingproteinsstructures pages 4-6, scheffzek2019rasspecificgtpaseactivatingproteinsstructures pages 3-4).
- **Catalytically inactive pseudoGAPs**: IQGAPs (IQGAP1/2/3) retain the RasGAP fold but are devoid of RasGAP activity and instead bind Rho family GTPases (scheffzek2019rasspecificgtpaseactivatingproteinsstructures pages 3-4, liao2023therasgtpase‐activating‐like pages 1-2). These represent class i pseudoGTPases with loss of catalytic competence (stiegler2020thepseudogtpasegroup pages 1-2, stiegler2020thepseudogtpasegroup pages 2-4).

Annotating this family-level entry with "Ras GTPase activator activity" (GO:0005099) would be **over-annotating** because:
- Plexin subfamily members target Rap, not Ras
- IQGAP subfamily members are catalytically inactive for any small GTPase
- Some active members have dual Ras/Rap specificity

#### Problem 2: Entry type is "family" not "domain"

PTHR10194 is designated as type "family," implying it describes whole-protein function. However, the functional modules (C2 domain, GAP domain, accessory domains) have distinct roles. The GAP domain itself could potentially support a molecular function annotation, but the whole-protein families have divergent biology:

- p120GAP/RASA1: vascular development, growth control (scheffzek2019rasspecificgtpaseactivatingproteinsstructures pages 1-3, bellazzo2020cuttingthebrakes pages 1-3)
- NF1: tumor suppressor, neuronal function, neurofibromatosis syndrome (scheffzek2019rasspecificgtpaseactivatingproteinsstructures pages 1-3, bellazzo2020cuttingthebrakes pages 1-3, fernandezmedarde202140yearsof pages 3-5)
- SynGAP: neuron-specific, synaptic function, intellectual disability/autism (scheffzek2019rasspecificgtpaseactivatingproteinsstructures pages 3-4, fernandezmedarde202140yearsof pages 3-5)
- Plexins: transmembrane semaphorin receptors, axon guidance (scheffzek2019rasspecificgtpaseactivatingproteinsstructures pages 3-4, alves2019originandevolution pages 1-2)
- IQGAPs: cytoskeletal scaffolds, no GAP activity (scheffzek2019rasspecificgtpaseactivatingproteinsstructures pages 3-4, liao2023therasgtpase‐activating‐like pages 1-2)

Process-level GO terms describing any single biological role would only apply to a subset of proteins matched by this signature.

#### Problem 3: Taxonomic breadth

The PTHR10194 entry spans 7,495 taxa across eukaryotes, from unicellular organisms to mammals. RasGAPs are present in choanoflagellates (unicellular relatives of metazoans), Dictyostelium (Amoebozoa), fungi, and throughout Metazoa (filic2021regulationofthe pages 1-2, filic2021regulationofthe pages 2-4, alves2019originandevolution pages 1-2). The C2-GAP architecture is conserved from sponges to humans (paul2025thec2domain pages 3-4). 

Any process or component term tied to specific metazoan-only pathways (e.g., "nervous system development") or compartments (e.g., "neuron projection") would fail in unicellular eukaryotes or fungi.

### Recommendations

**For PTHR10194 (family-level entry):**

1. **ACCEPT the current absence of InterPro2GO mappings.** Do not add Ras-specific or process-specific terms.

2. **If any family-level annotation is desired, use only the most general terms that hold for the catalytically active subfamilies:**
   - Molecular Function: "GTPase activator activity" (GO:0005096) – broad enough to cover Ras, Rap, and related substrates for the active subfamilies
   - Biological Process: "small GTPase mediated signal transduction" (GO:0007264) – general pathway involvement
   - **However, even these would be PARTIALLY over-annotating because IQGAP subfamily members lack catalytic activity.**

3. **BETTER APPROACH: Recommend that InterPro/PANTHER add subfamily-specific entries** (e.g., separate entries for RASA1-like, NF1-like, GAP1 family, SynGAP family, Plexin, IQGAP) and attach GO terms at the subfamily level where they are uniformly true. This would allow:
   - RASA1-like subfamily → "Ras GTPase activator activity" (GO:0005099)
   - Plexin subfamily → "Rap GTPase activator activity" (GO:0097100, if exists) or more accurately "regulation of Rap protein signal transduction" (GO:0032487)
   - IQGAP subfamily → "Rho protein binding" (GO:0017048), "cytoskeletal protein binding" (GO:0008092), but NOT any GTPase activator activity
   - GAP1 subfamily with dual-specificity → both Ras and Rap activator activities

4. **Mark PTHR10194 as KEEP_AS_NON_CORE** for GO annotation purposes given the heterogeneity, or alternatively **flag for subdivision before GO mapping**.

---

## 3. Functional Divergence Across the Family

The RasGAP family exhibits extensive functional diversification into six major subfamilies with distinct domain architectures, regulatory mechanisms, and substrate specificities. A comprehensive comparison is provided in the following table:

| Subfamily | Representative members | Domain architecture | Catalytic activity status | Substrate specificity | Key distinguishing features | Relevant citations |
|---|---|---|---|---|---|---|
| p120GAP / RASA1 | RASA1 (p120GAP) | N-terminal CH domain; SH2-SH3-SH2 module; PH domain; C2 domain; C-terminal RasGAP module | Active RasGAP | Primarily Ras-specific | First RasGAP discovered; ubiquitously expressed; essential for embryonic vascular development; catalytic RasGAP module contains the conserved arginine finger (Arg789 in p120GAP); recent structural work shows the adjacent C2 domain augments catalytic efficiency and is conserved across many RasGAPs | (scheffzek2019rasspecificgtpaseactivatingproteinsstructures pages 1-3, scheffzek2019rasspecificgtpaseactivatingproteinsstructures pages 3-4, paul2025thec2domain pages 2-3, paul2025thec2domain pages 3-4) |
| NF1 / neurofibromin | NF1 (neurofibromin) | Large multidomain protein with central GAP-related domain (GRD) followed by bipartite Sec14-PH-like module | Active RasGAP | Primarily Ras-specific | Major tumor suppressor; highest adult expression in neurons; essential for embryonic development; catalytic arginine finger conserved (Arg1276 in neurofibromin); membrane recruitment can be mediated by SPRED1 | (scheffzek2019rasspecificgtpaseactivatingproteinsstructures pages 1-3, scheffzek2019rasspecificgtpaseactivatingproteinsstructures pages 3-4, scheffzek2019rasspecificgtpaseactivatingproteinsstructures pages 6-7) |
| GAP1 family | RASA2 (GAP1m), RASA3 (GAP1IP4BP), RASA4 (CAPRI), RASAL1 | Two C2 domains, followed by RasGAP module, then PH domain | Active RasGAPs | Mixed: some dual Ras/Rap specificity; GAPIP4BP/RASA3, CAPRI/RASA4, and RASAL1 reported as dual-specificity | Characterized by tandem C2 domains and regulated membrane translocation; CAPRI and RASAL1 show Ca2+-dependent membrane association; several members can inactivate both Ras and Rap, so family is functionally broader than Ras-only nomenclature suggests | (scheffzek2019rasspecificgtpaseactivatingproteinsstructures pages 3-4, scheffzek2019rasspecificgtpaseactivatingproteinsstructures pages 6-7, bellazzo2020cuttingthebrakes pages 1-3) |
| SynGAP family | SynGAP, DAB2IP, RASAL2, RASAL3 | PH domain, C2 domain, RasGAP module | Active RasGAPs | Mixed: Ras-directed, with subfamily-level functional divergence; some members discussed with Ras/Rap pathway cross-talk | SynGAP is neuron-enriched and linked to intellectual disability/autism; architecture places PH-C2-GAP module near N-terminus; recent work supports a conserved catalytic contribution of the C2 domain across RasGAPs, including SynGAP-like proteins | (scheffzek2019rasspecificgtpaseactivatingproteinsstructures pages 3-4, paul2025thec2domain pages 2-3, fernandezmedarde202140yearsof pages 3-5) |
| Plexins | Plexin family receptors (e.g., Plexin-C1) | Extracellular Sema-containing receptor region, transmembrane helix, intracellular RasGAP-like domain | Active GAP-like enzymes | Rap-specific (Rap1/2) rather than classical Ras | Transmembrane semaphorin receptors; intracellular RasGAP-like domain mechanistically resembles canonical RasGAP fold but functions on Rap family GTPases; domain structure highly conserved through evolution and detected as early as choanoflagellates/Metazoa ancestor | (scheffzek2019rasspecificgtpaseactivatingproteinsstructures pages 3-4, scheffzek2019rasspecificgtpaseactivatingproteinsstructures pages 4-6, alves2019originandevolution pages 1-2) |
| IQGAPs | IQGAP1, IQGAP2, IQGAP3 | N-terminal CH domain, WW domain, multiple IQ motifs, C-terminal RasGAP-like domain | PseudoGAP / catalytically inactive as RasGAP | Not catalytic for Ras; binds Rho-family GTPases and acts as scaffold/adaptor | Retain RasGAP-like fold but lack detectable RasGAP activity; function as scaffolds coordinating cytoskeletal and signaling pathways; IQGAP1 can bridge signaling assemblies such as GSDMD to ESCRT machinery; represents clear pseudoenzyme divergence within the broader RasGAP-like fold family | (scheffzek2019rasspecificgtpaseactivatingproteinsstructures pages 3-4, liao2023therasgtpase‐activating‐like pages 1-2, stiegler2020thepseudogtpasegroup pages 1-2) |


*Table: This table compares the six major RasGAP-related subfamilies by architecture, catalytic status, substrate preference, and distinguishing biology. It is useful for assessing whether a broad family-level annotation is likely to be uniformly true across all members matched by the InterPro/PANTHER family.*

### Key Divergences

#### Catalytically Active vs. PseudoGAPs

The most dramatic functional divergence is the presence of catalytically inactive pseudoGAPs (IQGAPs) alongside active RasGAPs (stiegler2020thepseudogtpasegroup pages 1-2, stiegler2020thepseudogtpasegroup pages 2-4). IQGAPs retain the RasGAP-like fold but have degenerated conserved catalytic motifs and do not accelerate GTP hydrolysis. Instead, they function as scaffolding proteins coordinating cytoskeletal and signaling pathways (scheffzek2019rasspecificgtpaseactivatingproteinsstructures pages 3-4, liao2023therasgtpase‐activating‐like pages 1-2). For example, IQGAP1 bridges Gasdermin D to the ESCRT system to promote IL-1β release via exosomes in a GTP-bound CDC42-dependent manner (liao2023therasgtpase‐activating‐like pages 1-2). This represents a clear example of pseudoenzyme evolution within the RasGAP fold family (stiegler2020thepseudogtpasegroup pages 1-2, stiegler2020thepseudogtpasegroup pages 2-4).

#### Substrate Specificity Divergence

- **Strict Ras specificity**: p120GAP/RASA1 and NF1 show primary activity toward Ras family GTPases (scheffzek2019rasspecificgtpaseactivatingproteinsstructures pages 1-3, fernandezmedarde202140yearsof pages 3-5).
  
- **Dual Ras/Rap specificity**: Within the GAP1 family, several members (RASA3/GAPIP4BP, RASA4/CAPRI, RASAL1) have been shown to inactivate both Ras and Rap family proteins using a conserved arginine finger mechanism (scheffzek2019rasspecificgtpaseactivatingproteinsstructures pages 3-4, scheffzek2019rasspecificgtpaseactivatingproteinsstructures pages 6-7). The mechanism involves the catalytic arginine plus a glutamine finger (Gln63 in Rap) in a dual in trans mechanism (scheffzek2019rasspecificgtpaseactivatingproteinsstructures pages 4-6, scheffzek2019rasspecificgtpaseactivatingproteinsstructures pages 3-4).

- **Rap specificity**: Plexins are transmembrane receptors whose intracellular RasGAP-like domain inactivates Rap1/2 proteins (scheffzek2019rasspecificgtpaseactivatingproteinsstructures pages 3-4). Unlike canonical RasGAPs, plexins lack some PSI and IPT domains in their extracellular portion and may use slightly different catalytic arrangements (alves2019originandevolution pages 1-2).

#### Regulatory Mechanism Divergence

Different subfamilies employ distinct regulatory strategies:

1. **Membrane recruitment mechanisms:**
   - p120GAP/RASA1: SH2 domain-mediated recruitment to phosphorylated receptor tyrosine kinases (scheffzek2019rasspecificgtpaseactivatingproteinsstructures pages 6-7, fernandezmedarde202140yearsof pages 3-5)
   - NF1: Membrane targeting mediated by SPRED1 binding to the GAP-related domain (scheffzek2019rasspecificgtpaseactivatingproteinsstructures pages 6-7)
   - GAP1 family: Ca²⁺-dependent C2 domain-mediated membrane translocation; CAPRI/RASA4 and RASAL1 sense calcium oscillations (scheffzek2019rasspecificgtpaseactivatingproteinsstructures pages 6-7)
   - SynGAP: PH-C2-GAP module at N-terminus

2. **Tissue-specific expression:**
   - NF1: Highest expression in neuronal tissues (scheffzek2019rasspecificgtpaseactivatingproteinsstructures pages 1-3)
   - SynGAP: Neuron-enriched, particularly at synapses (scheffzek2019rasspecificgtpaseactivatingproteinsstructures pages 3-4, fernandezmedarde202140yearsof pages 3-5)
   - p120GAP/RASA1: Ubiquitously expressed (scheffzek2019rasspecificgtpaseactivatingproteinsstructures pages 1-3)

3. **Disease associations indicating divergent biological roles:**
   - NF1: Neurofibromatosis type 1, tumor predisposition (bellazzo2020cuttingthebrakes pages 1-3, fernandezmedarde202140yearsof pages 3-5)
   - RASA1: Vascular malformations (capillary malformation-arteriovenous malformation, CM-AVM) (scheffzek2019rasspecificgtpaseactivatingproteinsstructures pages 1-3, bellazzo2020cuttingthebrakes pages 1-3)
   - RASA3: RASopathy-like phenotype and bone marrow failure (fernandezmedarde202140yearsof pages 3-5)
   - SynGAP: Intellectual disability and autism spectrum disorders (scheffzek2019rasspecificgtpaseactivatingproteinsstructures pages 3-4, fernandezmedarde202140yearsof pages 3-5)

#### No Evidence of Catalytically Dead Active-Site Mutants

Unlike some enzyme families, there is no evidence within the canonical RasGAP subfamilies (excluding IQGAPs) of proteins that retain the fold and substrate binding but have lost catalytic activity through active-site mutations while maintaining other functions. The oncogenic Ras mutations (G12, G13, Q61) render Ras insensitive to RasGAPs by interfering with transition state geometry, but this is a substrate-side escape mechanism, not a GAP-side pseudo-enzyme phenomenon (scheffzek2019rasspecificgtpaseactivatingproteinsstructures pages 4-6, scheffzek2019rasspecificgtpaseactivatingproteinsstructures pages 3-4). IQGAPs represent the only clear pseudoenzyme branch, and they have diverged so extensively that they no longer bind Ras-family proteins at all, instead interacting with Rho family members (scheffzek2019rasspecificgtpaseactivatingproteinsstructures pages 3-4).

---

## 4. Taxonomic Scope

### Evolutionary Origin

RasGAPs have an ancient eukaryotic origin. Phylogenetic and genomic analyses indicate:

- **Presence in the Last Eukaryotic Common Ancestor (LECA)**: Small GTPases and their regulatory proteins (GEFs and GAPs) are found across all eukaryotic supergroups, indicating their presence in LECA (filic2021regulationofthe pages 2-4, wuichet2015evolutionanddiversity pages 1-2).

- **Unicellular eukaryotes**: Plexins and semaphorins (semaphorins being ligands for plexins) have been detected in choanoflagellates, unicellular eukaryotes that are close relatives of Metazoa, indicating their origin in a common ancestor of Choanoflagellida and Metazoa (alves2019originandevolution pages 1-2). RasGAPs are also well-characterized in Dictyostelium discoideum (Amoebozoa), where they regulate actin cytoskeleton dynamics (filic2021regulationofthe pages 1-2, filic2021regulationofthe pages 2-4).

- **Conservation of C2-GAP architecture**: Alignment of 209 RasGAP sequences from humans to sponges shows complete conservation of the catalytic surface in the GAP domain and a highly conserved interaction surface in the C2 domain, demonstrating this architectural feature is at least as old as Porifera (paul2025thec2domain pages 3-4, paul2025thec2domain pages 2-3).

### Distribution Across Clades

The PTHR10194 entry itself reports 24,424 proteins across 7,495 taxa, indicating very broad taxonomic distribution. Specific distributions include:

- **Metazoa**: All major RasGAP subfamilies are present in bilaterian animals. Plexins and semaphorins are found in non-bilaterian metazoans including Cnidaria, Ctenophora, and Porifera (alves2019originandevolution pages 1-2).

- **Fungi**: RasGAPs are present in yeasts (Saccharomyces cerevisiae, Schizosaccharomyces pombe) (fernandezmedarde202140yearsof pages 3-5).

- **Amoebozoa**: Dictyostelium and related amoebae possess RasGAPs. Phylogenetic analysis of Rho GTPases in Amoebozoa shows variability in Rho inventories across different amoebozoan clades, and correspondingly variable RasGAP complements (filic2021regulationofthe pages 2-4).

- **Other eukaryotic lineages**: The Ras superfamily and regulatory proteins are distributed broadly across SAR (Stramenopiles, Alveolates, Rhizaria), Excavata, and Archaeplastida (plants), though specific RasGAP subfamily representation varies (fernandezmedarde202140yearsof pages 3-5).

- **Absence in prokaryotes**: While prokaryotes possess small GTPases of the Ras superfamily (MglA and Rup families), the eukaryotic RasGAP architecture (with C2 domains, SH2/SH3 domains, etc.) is not found in bacteria or archaea (wuichet2015evolutionanddiversity pages 3-3, wuichet2015evolutionanddiversity pages 1-2). Prokaryotic GTPase regulation uses distinct GAPs such as MglB (wuichet2015evolutionanddiversity pages 1-2).

### Implications for GO Term Scope

Given this broad taxonomic distribution:

- **Component terms**: Any GO component term referring to metazoan-specific organelles or structures (e.g., "neuron projection," "blood vessel development") would be inappropriate for PTHR10194 as these pathways/structures do not exist in fungi, Dictyostelium, or choanoflagellates.

- **Process terms**: Similarly, process terms tied to multicellularity, immune function, or nervous system development would be metazoan-specific and not hold across the 7,495 taxa.

- **Molecular function terms**: Broad molecular function terms like "GTPase activator activity" could in principle hold across eukaryotes, BUT the substrate specificity variation (Ras vs. Rap vs. Rho vs. catalytically inactive) means even molecular function terms must be carefully chosen to avoid over-annotation.

---

## 5. Over-Annotation Verdict and Recommendations

### Summary Verdict: Current Absence of GO Mappings is APPROPRIATE

**Status**: PTHR10194 currently has **no InterPro2GO terms** assigned.

**Verdict**: **This is correct and should be maintained.**

### Rationale

1. **Functional heterogeneity**: The family includes:
   - Catalytically active Ras-specific GAPs
   - Catalytically active dual Ras/Rap GAPs
   - Catalytically active Rap-specific GAPs (Plexins)
   - Catalytically inactive pseudoGAPs (IQGAPs)
   
   No single substrate-specific molecular function term (e.g., "Ras GTPase activator activity" GO:0005099) is true for all members.

2. **Entry type mismatch**: PTHR10194 is type "family" (whole-protein classification), yet the functional heterogeneity resides both within the catalytic domain (substrate specificity) and in accessory domains that confer tissue-specific regulation and biological roles. Family-level GO terms describing biological processes or cellular components would systematically over-annotate.

3. **Taxonomic breadth**: The entry spans 7,495 taxa from unicellular eukaryotes to mammals. Metazoan-specific process or component terms would be inappropriate for unicellular members.

### Recommended Action Pattern

**For PTHR10194 (the family-level entry):**

- **Action**: **ACCEPT** the current state (no GO mappings) OR **MARK_AS_NON_CORE** for GO annotation.
  
- **Alternative (preferred)**: **Request subdivision of PTHR10194 into subfamily-specific entries** corresponding to the six major subfamilies (p120GAP-like, NF1-like, GAP1 family, SynGAP family, Plexins, IQGAPs). Each subfamily could then receive appropriate GO annotations:
  - **p120GAP/RASA1 subfamily**: GO:0005099 (Ras GTPase activator activity), possibly GO:0001945 (blood vessel development) if taxonomically restricted to vertebrates
  - **NF1 subfamily**: GO:0005099 (Ras GTPase activator activity), GO:0008285 (negative regulation of cell proliferation), GO:0051056 (regulation of small GTPase mediated signal transduction)
  - **GAP1 family (RASA2/3/4, RASAL1)**: GO:0005099 (Ras GTPase activator activity) AND GO:0097100 (Rap GTPase activator activity, if it exists) to reflect dual specificity for subset; possibly Ca²⁺-dependent terms
  - **SynGAP family**: GO:0005099 (Ras GTPase activator activity), neuron-specific process terms if taxonomically restricted
  - **Plexin subfamily**: GO:0097100 (Rap GTPase activator activity) or GO:0032487 (regulation of Rap protein signal transduction), NOT Ras activator activity
  - **IQGAP subfamily**: GO:0017048 (Rho protein binding), GO:0008092 (cytoskeletal protein binding), scaffolding activity terms, but **explicitly NOT** any GTPase activator activity

**For genes annotated by PTHR10194:**

- **Do NOT propagate broad "Ras GTPase activator activity" to all genes** matching this family.
- Use subfamily assignment (from PTHR10194 subfamilies or from InterPro child entries like IPR039360 if it has more granular classifications) to assign appropriate GO terms.
- For genes where subfamily cannot be determined, use only the most conservative terms or omit automated GO annotation pending manual curation.

### Recommendation to InterPro

Since PTHR10194 is integrated into/parent of IPR039360, check whether IPR039360 or other child InterPro entries provide subfamily-level granularity. If so, GO mappings should be attached to those child entries, not to PTHR10194. If child entries do not exist or are insufficient, recommend creating them.

---

## Conclusion

PTHR10194 represents a functionally diverse superfamily of proteins sharing the RasGAP fold but with divergent substrate specificities (Ras, Rap, Rho, or none), catalytic statuses (active vs. pseudoenzyme), regulatory mechanisms, tissue distributions, and biological roles. The family-level entry, spanning 24,424 proteins across 7,495 taxa and 20 subfamilies, cannot be uniformly annotated with any specific molecular function, biological process, or cellular component GO term without systematic over-annotation of substantial subsets of its members.

The current absence of InterPro2GO mappings for PTHR10194 is **scientifically sound and should be maintained**. If GO annotation is desired, it should be implemented at the subfamily level (ideally through subdivision of PTHR10194 or through child InterPro entries) where functional predictions hold uniformly across all matched proteins.

### Key Citations

- Structural mechanism and C2 domain function: (paul2025thec2domain pages 3-4, paul2025thec2domain pages 2-3, scheffzek2019rasspecificgtpaseactivatingproteinsstructures pages 4-6, scheffzek2019rasspecificgtpaseactivatingproteinsstructures pages 1-3, scheffzek2019rasspecificgtpaseactivatingproteinsstructures pages 3-4)
- Subfamily classification and functional diversity: (scheffzek2019rasspecificgtpaseactivatingproteinsstructures pages 1-3, scheffzek2019rasspecificgtpaseactivatingproteinsstructures pages 3-4, bellazzo2020cuttingthebrakes pages 1-3, fernandezmedarde202140yearsof pages 3-5)
- PseudoGAPs and catalytic divergence: (liao2023therasgtpase‐activating‐like pages 1-2, stiegler2020thepseudogtpasegroup pages 1-2, stiegler2020thepseudogtpasegroup pages 2-4)
- Evolutionary and taxonomic distribution: (filic2021regulationofthe pages 1-2, filic2021regulationofthe pages 2-4, alves2019originandevolution pages 1-2, wuichet2015evolutionanddiversity pages 3-3, wuichet2015evolutionanddiversity pages 1-2)
- Dual substrate specificity and mechanistic variations: (scheffzek2019rasspecificgtpaseactivatingproteinsstructures pages 4-6, scheffzek2019rasspecificgtpaseactivatingproteinsstructures pages 3-4, scheffzek2019rasspecificgtpaseactivatingproteinsstructures pages 6-7)

References

1. (scheffzek2019rasspecificgtpaseactivatingproteinsstructures pages 1-3): Klaus Scheffzek and Giridhar Shivalingaiah. Ras-specific gtpase-activating proteins-structures, mechanisms, and interactions. Cold Spring Harbor perspectives in medicine, 9 3:a031500, Aug 2019. URL: https://doi.org/10.1101/cshperspect.a031500, doi:10.1101/cshperspect.a031500. This article has 117 citations and is from a peer-reviewed journal.

2. (scheffzek2019rasspecificgtpaseactivatingproteinsstructures pages 3-4): Klaus Scheffzek and Giridhar Shivalingaiah. Ras-specific gtpase-activating proteins-structures, mechanisms, and interactions. Cold Spring Harbor perspectives in medicine, 9 3:a031500, Aug 2019. URL: https://doi.org/10.1101/cshperspect.a031500, doi:10.1101/cshperspect.a031500. This article has 117 citations and is from a peer-reviewed journal.

3. (scheffzek2019rasspecificgtpaseactivatingproteinsstructures pages 4-6): Klaus Scheffzek and Giridhar Shivalingaiah. Ras-specific gtpase-activating proteins-structures, mechanisms, and interactions. Cold Spring Harbor perspectives in medicine, 9 3:a031500, Aug 2019. URL: https://doi.org/10.1101/cshperspect.a031500, doi:10.1101/cshperspect.a031500. This article has 117 citations and is from a peer-reviewed journal.

4. (paul2025thec2domain pages 3-4): Maxum E. Paul, Di Chen, Kimberly J. Vish, Nathaniel L. Lartey, Elizabeth Hughes, Zachary T. Freeman, Thomas L. Saunders, Amy L. Stiegler, Philip D. King, and Titus J. Boggon. The c2 domain augments ras gtpase-activating protein catalytic activity. Proceedings of the National Academy of Sciences of the United States of America, Feb 2025. URL: https://doi.org/10.1073/pnas.2418433122, doi:10.1073/pnas.2418433122. This article has 7 citations and is from a highest quality peer-reviewed journal.

5. (paul2025thec2domain pages 2-3): Maxum E. Paul, Di Chen, Kimberly J. Vish, Nathaniel L. Lartey, Elizabeth Hughes, Zachary T. Freeman, Thomas L. Saunders, Amy L. Stiegler, Philip D. King, and Titus J. Boggon. The c2 domain augments ras gtpase-activating protein catalytic activity. Proceedings of the National Academy of Sciences of the United States of America, Feb 2025. URL: https://doi.org/10.1073/pnas.2418433122, doi:10.1073/pnas.2418433122. This article has 7 citations and is from a highest quality peer-reviewed journal.

6. (mishra2016invitedreviewsmall pages 1-2): Ashwini K. Mishra and David G. Lambright. Invited review: small gtpases and their gaps. May 2016. URL: https://doi.org/10.1002/bip.22833, doi:10.1002/bip.22833. This article has 102 citations and is from a peer-reviewed journal.

7. (scheffzek2019rasspecificgtpaseactivatingproteinsstructures pages 6-7): Klaus Scheffzek and Giridhar Shivalingaiah. Ras-specific gtpase-activating proteins-structures, mechanisms, and interactions. Cold Spring Harbor perspectives in medicine, 9 3:a031500, Aug 2019. URL: https://doi.org/10.1101/cshperspect.a031500, doi:10.1101/cshperspect.a031500. This article has 117 citations and is from a peer-reviewed journal.

8. (liao2023therasgtpase‐activating‐like pages 1-2): Yun Liao, Xing Chen, William Miller‐Little, Han Wang, Belinda Willard, Katarzyna Bulek, Junjie Zhao, and Xiaoxia Li. The ras gtpase‐activating‐like protein iqgap1 bridges gasdermin d to the escrt system to promote il‐1β release via exosomes. The EMBO Journal, Nov 2023. URL: https://doi.org/10.15252/embj.2022110780, doi:10.15252/embj.2022110780. This article has 44 citations.

9. (stiegler2020thepseudogtpasegroup pages 1-2): Amy L. Stiegler and Titus J. Boggon. The pseudogtpase group of pseudoenzymes. The FEBS Journal, 287:4232-4245, Sep 2020. URL: https://doi.org/10.1111/febs.15554, doi:10.1111/febs.15554. This article has 27 citations.

10. (stiegler2020thepseudogtpasegroup pages 2-4): Amy L. Stiegler and Titus J. Boggon. The pseudogtpase group of pseudoenzymes. The FEBS Journal, 287:4232-4245, Sep 2020. URL: https://doi.org/10.1111/febs.15554, doi:10.1111/febs.15554. This article has 27 citations.

11. (bellazzo2020cuttingthebrakes pages 1-3): Arianna Bellazzo and Licio Collavin. Cutting the brakes on ras—cytoplasmic gaps as targets of inactivation in cancer. Cancers, 12:3066, Oct 2020. URL: https://doi.org/10.3390/cancers12103066, doi:10.3390/cancers12103066. This article has 20 citations.

12. (fernandezmedarde202140yearsof pages 3-5): Alberto Fernández-Medarde, Javier De Las Rivas, and Eugenio Santos. 40 years of ras—a historic overview. Genes, 12:681, May 2021. URL: https://doi.org/10.3390/genes12050681, doi:10.3390/genes12050681. This article has 67 citations.

13. (alves2019originandevolution pages 1-2): Chrystian Junqueira Alves, Karla Yotoko, Hongyan Zou, and Roland H. Friedel. Origin and evolution of plexins, semaphorins, and met receptor tyrosine kinases. Scientific Reports, Feb 2019. URL: https://doi.org/10.1038/s41598-019-38512-y, doi:10.1038/s41598-019-38512-y. This article has 64 citations and is from a peer-reviewed journal.

14. (filic2021regulationofthe pages 1-2): Vedrana Filić, Lucija Mijanović, Darija Putar, Antea Talajić, Helena Ćetković, and Igor Weber. Regulation of the actin cytoskeleton via rho gtpase signalling in dictyostelium and mammalian cells: a parallel slalom. Cells, 10:1592, Jun 2021. URL: https://doi.org/10.3390/cells10071592, doi:10.3390/cells10071592. This article has 46 citations.

15. (filic2021regulationofthe pages 2-4): Vedrana Filić, Lucija Mijanović, Darija Putar, Antea Talajić, Helena Ćetković, and Igor Weber. Regulation of the actin cytoskeleton via rho gtpase signalling in dictyostelium and mammalian cells: a parallel slalom. Cells, 10:1592, Jun 2021. URL: https://doi.org/10.3390/cells10071592, doi:10.3390/cells10071592. This article has 46 citations.

16. (wuichet2015evolutionanddiversity pages 1-2): Kristin Wuichet and Lotte Søgaard-Andersen. Evolution and diversity of the ras superfamily of small gtpases in prokaryotes. Genome Biology and Evolution, 7:57-70, Dec 2015. URL: https://doi.org/10.1093/gbe/evu264, doi:10.1093/gbe/evu264. This article has 74 citations and is from a domain leading peer-reviewed journal.

17. (wuichet2015evolutionanddiversity pages 3-3): Kristin Wuichet and Lotte Søgaard-Andersen. Evolution and diversity of the ras superfamily of small gtpases in prokaryotes. Genome Biology and Evolution, 7:57-70, Dec 2015. URL: https://doi.org/10.1093/gbe/evu264, doi:10.1093/gbe/evu264. This article has 74 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](PTHR10194-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. scheffzek2019rasspecificgtpaseactivatingproteinsstructures pages 1-3
2. scheffzek2019rasspecificgtpaseactivatingproteinsstructures pages 3-4
3. mishra2016invitedreviewsmall pages 1-2
4. scheffzek2019rasspecificgtpaseactivatingproteinsstructures pages 6-7
5. scheffzek2019rasspecificgtpaseactivatingproteinsstructures pages 4-6
6. alves2019originandevolution pages 1-2
7. filic2021regulationofthe pages 2-4
8. wuichet2015evolutionanddiversity pages 1-2
9. stiegler2020thepseudogtpasegroup pages 1-2
10. stiegler2020thepseudogtpasegroup pages 2-4
11. bellazzo2020cuttingthebrakes pages 1-3
12. filic2021regulationofthe pages 1-2
13. wuichet2015evolutionanddiversity pages 3-3
14. https://doi.org/10.1101/cshperspect.a031500,
15. https://doi.org/10.1073/pnas.2418433122,
16. https://doi.org/10.1002/bip.22833,
17. https://doi.org/10.15252/embj.2022110780,
18. https://doi.org/10.1111/febs.15554,
19. https://doi.org/10.3390/cancers12103066,
20. https://doi.org/10.3390/genes12050681,
21. https://doi.org/10.1038/s41598-019-38512-y,
22. https://doi.org/10.3390/cells10071592,
23. https://doi.org/10.1093/gbe/evu264,