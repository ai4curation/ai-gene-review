---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-28T21:07:39.208352'
end_time: '2026-06-28T21:28:20.071122'
duration_seconds: 1240.86
template_file: templates/interpro_family_research.md
template_variables:
  interpro_id: PTHR24072
  interpro_name: RHO FAMILY GTPASE
  interpro_short_name: Not specified
  interpro_type: family
  interpro_integrated: IPR003578
  member_databases: Not specified
  n_proteins: '51615'
  n_taxa: '9604'
  n_subfamilies: '98'
  interpro2go_terms: None mapped (no InterPro2GO terms for this entry)
  interpro_description: Not specified in InterPro
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 37
artifact_count: 3
artifact_sources:
  edison_answer_artifacts: 3
artifacts:
- filename: artifact-00.md
  path: PTHR24072-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: PTHR24072-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
- filename: artifact-02.md
  path: PTHR24072-deep-research-falcon_artifacts/artifact-02.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-02
---

## Question

# InterPro Family Research for GO Annotation Review

## ⚠️ CRITICAL: Family Identification Context

**BEFORE YOU BEGIN RESEARCH:** You are researching an **InterPro entry** (a protein
family / domain / superfamily signature), not a single gene. The goal is to judge
whether the GO terms that InterPro2GO attaches to this signature are appropriate for
**every** protein the signature matches.

### Target InterPro Entry (from the InterPro API):
- **Accession:** PTHR24072
- **Name:** RHO FAMILY GTPASE
- **Short name:** Not specified
- **Entry type:** family
- **Integrated into / parent:** IPR003578
- **Member database signatures:** Not specified
- **Scale:** 51615 proteins across 9604 taxa, 98 subfamilies
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
**PTHR24072 (RHO FAMILY GTPASE)**, structured to support GO annotation review.

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
- **Accession:** PTHR24072
- **Name:** RHO FAMILY GTPASE
- **Short name:** Not specified
- **Entry type:** family
- **Integrated into / parent:** IPR003578
- **Member database signatures:** Not specified
- **Scale:** 51615 proteins across 9604 taxa, 98 subfamilies
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
**PTHR24072 (RHO FAMILY GTPASE)**, structured to support GO annotation review.

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


# InterPro Family Research Report: PTHR24072 — RHO FAMILY GTPASE

## 1. Family Definition and Biochemistry

### 1.1 Overview

PTHR24072 (RHO FAMILY GTPASE) is a PANTHER family-level InterPro entry (integrated into IPR003578) that encompasses the Rho family of small GTPases, a major subfamily of the Ras superfamily of small GTP-hydrolyzing enzymes. In humans, 20 canonical Rho GTPases are organized into eight subfamilies: RHO (RHOA, RHOB, RHOC), RAC (RAC1, RAC2, RAC3, RHOG), CDC42 (CDC42, RHOJ, RHOQ), RHODF (RHOD, RHOF/RIF), RHOUV (RHOU/WRCH1, RHOV/CHP), RND (RND1, RND2, RND3/RHOE), RHOH, and RHOBTB (RHOBTB1, RHOBTB2) (mosaddeghzadeh2021therhofamily pages 3-5, wang2022rhogtpasefamily pages 1-2, hairston2025rhosmallgtpase pages 1-2). The signature spans 51,615 proteins across 9,604 taxa and 98 subfamilies, reflecting the pan-eukaryotic distribution and extensive diversification of this family.

### 1.2 Structural Fold and Conserved Motifs

Rho GTPases share a conserved G domain based on a Rossmann-fold architecture that mediates guanine nucleotide binding and hydrolysis (stiegler2020thepseudogtpasegroup pages 1-2). The G domain contains five conserved sequence motifs (G1–G5): the G1 motif (P-loop) contains a conserved Gly-12 involved in phosphate binding; the G2 motif (switch I) contains Thr-37, which stabilizes the active GTP-bound conformation through hydrogen bonds with the γ-phosphate; and the G3 motif (switch II) contains the catalytic Gln-61, essential for GTP hydrolysis (mosaddeghzadeh2021therhofamily pages 3-5, mosaddeghzadeh2021therhofamily pages 5-6, lin2025structuraldynamicsof pages 3-4). Switch I and switch II undergo conformational changes during the GDP-to-GTP transition, enabling effector protein recognition.

A distinguishing structural feature of Rho GTPases relative to other Ras superfamily members is the **Rho insert helix**, an approximately 13-amino acid α-helix inserted between the G4 and G5 motifs. This helix plays a crucial role in binding and activating specific effector proteins including NADPH oxidase, IQGAP, ROCK, and mDia, and is a primary determinant of Rho-specific signaling pathways (hairston2025rhosmallgtpase pages 7-9, lin2025structuraldynamicsof pages 3-4). The C-terminal hypervariable region contains a CAAX consensus motif that undergoes posttranslational lipid modifications (prenylation) directing subcellular membrane localization (mosaddeghzadeh2021therhofamily pages 3-5, mosaddeghzadeh2021therhofamily pages 5-6).

### 1.3 Mechanism of Action

Classical Rho GTPases function as molecular switches cycling between an inactive GDP-bound state and an active GTP-bound state. This cycle is regulated by three classes of regulatory proteins: guanine nucleotide exchange factors (GEFs, ~85 in humans) that promote GDP-to-GTP exchange and activation; GTPase-activating proteins (GAPs, ~66) that accelerate intrinsic GTP hydrolysis and inactivation; and guanine nucleotide dissociation inhibitors (GDIs, 3) that sequester GDP-bound GTPases in the cytosol (mosaddeghzadeh2021therhofamily pages 3-5, mosaddeghzadeh2021therhofamily pages 1-3). In the active GTP-bound state, Rho GTPases bind and activate >70 downstream effector proteins including kinases (ROCK, PAK, PI5K) and scaffolding proteins (DIA, WASP, IRSp53, IQGAP) (mosaddeghzadeh2021therhofamily pages 12-14).

## 2. InterPro2GO Mapping Appropriateness

### 2.1 Current State

No InterPro2GO terms are currently mapped to PTHR24072. Given the exceptional functional, biochemical, and taxonomic heterogeneity of this family, this absence is appropriate.

### 2.2 Analysis of Candidate GO Terms

The following table summarizes the suitability of commonly considered GO terms for this family, assessed across all 8 mammalian subfamilies:

| Subfamily | Mammalian members | Activity status | Key biochemical feature | Primary biological function(s) | GO: GTP binding | GO: GTPase activity | GO: small GTPase mediated signal transduction | GO: actin cytoskeleton organization |
|---|---|---|---|---|---|---|---|---|
| RHO | RHOA, RHOB, RHOC | Classical | Canonical Rho G domain with conserved catalytic residues; GDP/GTP cycling controlled by GEFs, GAPs, GDIs | Contractility, stress fibers, focal adhesion dynamics, migration/invasion | Yes | Yes | Often yes, but still context-dependent at protein level | Often yes, but not guaranteed for every member in every taxon/context (mosaddeghzadeh2021therhofamily pages 3-5, mosaddeghzadeh2021therhofamily pages 5-6, mosaddeghzadeh2021therhofamily pages 12-14) |
| RAC | RAC1, RAC2, RAC3, RHOG | Classical | Canonical switch GTPases; strong effector coupling to lamellipodia/WAVE-Arp2/3 pathways | Membrane ruffling, lamellipodia, migration, ROS/NADPH oxidase signaling, immune-cell functions | Yes | Yes | Often yes | Often yes (mosaddeghzadeh2021therhofamily pages 3-5, mosaddeghzadeh2021therhofamily pages 12-14, bement2024patterningofthe pages 1-6) |
| CDC42 | CDC42, RHOJ/TCL, RHOQ/TC10 | Classical | Canonical switch GTPases with selective effector interfaces for WASP/PAK/polarity factors | Cell polarity, filopodia, vesicle trafficking, morphogenesis | Yes | Yes | Often yes | Often yes (wang2022rhogtpasefamily pages 1-2, mosaddeghzadeh2021therhofamily pages 12-14, bement2024patterningofthe pages 1-6) |
| RHODF | RHOD, RHOF/RIF | Fast-cycling atypical | Retain GTPase activity but have elevated intrinsic nucleotide exchange; tend to accumulate in active state | Endosome/membrane trafficking, filopodia or actin remodeling, migration-related processes | Yes | Yes, but atypical kinetics | Partly; too broad for all family members | Partly; true for some well-studied members, not safely universal (aspenstrom2022theroleof pages 2-4, mosaddeghzadeh2021therhofamily pages 5-6, mosaddeghzadeh2021therhofamily pages 18-19) |
| RHOUV | RHOU/WRCH1, RHOV/CHP | Fast-cycling atypical | High intrinsic exchange; atypical regulation, often less dependent on classic GEF/GDI control | Polarity, adhesion, migration, developmental signaling | Yes | Yes, but atypical kinetics | Partly; too broad for uniform annotation | Partly; many roles touch actin, but not a safe universal family-level term (aspenstrom2022theroleof pages 2-4, mosaddeghzadeh2021therhofamily pages 5-6, filic2021regulationofthe pages 2-4) |
| RND | RND1, RND2, RND3/RHOE | PseudoGTPase | Bind GTP but cannot hydrolyze it because key catalytic residues are missing/diverged; constitutively GTP-bound | Regulation of actin dynamics, cell shape, migration, proliferation; often antagonize classical Rho signaling | Yes | No | No; not classical nucleotide-switch signaling | Partly; many members regulate actin, but term is not safe as a universal family-level annotation (stiegler2020thepseudogtpasegroup pages 4-6, basbous2021pathophysiologicalfunctionsof pages 1-3, mosaddeghzadeh2021therhofamily pages 3-5) |
| RHOH | RHOH | PseudoGTPase | Hematopoiesis-specific atypical Rho protein; retains fold/GTP association but lacks catalytic activity | T-cell receptor/hematopoietic signaling, immune regulation rather than broad cytoskeletal control | Yes | No | No; too specific and non-classical | No as a general rule (stiegler2020thepseudogtpasegroup pages 4-6, mosaddeghzadeh2021therhofamily pages 5-6, mosaddeghzadeh2021therhofamily pages 18-19) |
| RHOBTB | RHOBTB1, RHOBTB2 | PseudoGTPase / nucleotide-nonbinding | Highly divergent GTPase-like domain; RhoBTB1/2 do not bind nucleotide; BTB domains act in Cullin3 ubiquitin-ligase adaptor functions | Protein ubiquitination/adaptor functions, trafficking/signaling scaffolding rather than classical Rho switching | No | No | No | No (stiegler2020thepseudogtpasegroup pages 6-7, stiegler2020thepseudogtpasegroup pages 1-2, hairston2025rhosmallgtpase pages 9-11) |


*Table: This table summarizes the eight mammalian Rho GTPase subfamilies, highlighting their biochemical differences and the suitability of common GO terms. It is useful for showing why broad family-level GO annotation can over-annotate atypical and pseudoGTPase members.*

**Key findings for candidate GO terms:**

- **GO:0005525 (GTP binding):** Would fail for RhoBTB1/2, which cannot bind nucleotide at all due to divergent G3, G4, and G5 motifs (stiegler2020thepseudogtpasegroup pages 6-7). Therefore, this term cannot be safely applied family-wide.

- **GO:0003924 (GTPase activity):** Would fail for all pseudoGTPase members—Rnd1/2/3 and RhoH lack the conserved Gly-12 and Gln-61 residues essential for GTP hydrolysis and are constitutively GTP-bound (stiegler2020thepseudogtpasegroup pages 4-6, mosaddeghzadeh2021therhofamily pages 5-6, basbous2021pathophysiologicalfunctionsof pages 1-3, mosaddeghzadeh2021therhofamily pages 3-5). RhoBTB1/2 also lack this activity.

- **GO:0007264 (small GTPase mediated signal transduction):** While broadly true for classical members, this term is inappropriate for pseudoGTPases that do not cycle between nucleotide states. RhoBTB proteins function primarily as Cullin3 ubiquitin ligase adaptors, a fundamentally different mechanism (stiegler2020thepseudogtpasegroup pages 6-7, hairston2025rhosmallgtpase pages 9-11).

- **GO:0032956 (regulation of actin cytoskeleton organization):** While many Rho GTPases regulate actin dynamics, this is not universal. RhoBTB functions center on ubiquitination pathways. RhoH primarily regulates T-cell receptor signaling and hematopoietic processes rather than direct actin remodeling (stiegler2020thepseudogtpasegroup pages 4-6, mosaddeghzadeh2021therhofamily pages 18-19).

- **GO:0005886 (plasma membrane):** Subcellular localization varies considerably. RhoBTB proteins localize to different compartments; various members show Golgi, endosomal, or nuclear localization depending on context (mosaddeghzadeh2021therhofamily pages 5-6).

## 3. Functional Divergence Across the Family

### 3.1 Classical vs. Atypical Members

The Rho GTPase family exhibits profound functional divergence that can be categorized into three regulatory classes:

**Classical GDP/GTP-switch GTPases (10 members):** RHOA, RHOB, RHOC, RAC1, RAC2, RAC3, RHOG, CDC42, RHOJ, RHOQ. These follow the canonical molecular switch paradigm and are regulated by GEFs, GAPs, and GDIs (mosaddeghzadeh2021therhofamily pages 5-6, aspenstrom2022theroleof pages 2-4).

**Fast-cycling atypical GTPases (4 members):** RHOD, RHOF, RHOU, RHOV. These retain intact GTPase activity but have greatly elevated intrinsic GDP/GTP exchange rates, allowing them to cycle rapidly between conformations without requiring GEFs. They predominantly reside in the active GTP-bound state (aspenstrom2022theroleof pages 2-4, mosaddeghzadeh2021therhofamily pages 5-6).

**PseudoGTPases (6 members):** RND1, RND2, RND3, RHOH, RHOBTB1, RHOBTB2. These represent catalytically dead members that retain the Rho GTPase fold but have lost enzymatic activity (stiegler2020thepseudogtpasegroup pages 4-6, stiegler2020thepseudogtpasegroup pages 1-2):

- **Rnd proteins** bind GTP constitutively but cannot hydrolyze it due to substitutions at positions Gly-12, Ala-59, and Gln-61. They are resistant to GAP-mediated inactivation and are instead regulated by phosphorylation and transcriptional control (aspenstrom2022theroleof pages 2-4, basbous2021pathophysiologicalfunctionsof pages 1-3).
- **RhoH** is a hematopoiesis-specific pseudoGTPase that retains GTP binding but lacks catalytic activity. It functions in T-cell receptor signaling (stiegler2020thepseudogtpasegroup pages 4-6, mosaddeghzadeh2021therhofamily pages 18-19).
- **RhoBTB1/2** are highly divergent multidomain proteins with pseudoGTPase domains that cannot bind nucleotide at all. Their GTPase-like domains instead serve as protein-protein interaction modules, functioning as substrate-binding domains for Cullin3/Roc1 ubiquitin ligase complexes (stiegler2020thepseudogtpasegroup pages 6-7). RhoBTB3 is also highly divergent and does not bind GTP but can bind and hydrolyze ATP (stiegler2020thepseudogtpasegroup pages 6-7).

### 3.2 Neo-functionalization

Several subfamilies demonstrate clear neo-functionalization:
- **RhoBTB** proteins have acquired BTB domains and serve as E3 ubiquitin ligase adaptors, a function entirely unrelated to the classical Rho GTPase switching mechanism (stiegler2020thepseudogtpasegroup pages 6-7, hairston2025rhosmallgtpase pages 9-11).
- **RhoH** has become restricted to hematopoietic lineages and functions in immune cell signaling rather than cytoskeletal regulation (stiegler2020thepseudogtpasegroup pages 4-6, mosaddeghzadeh2021therhofamily pages 18-19).
- **Rnd proteins** have evolved to antagonize classical Rho signaling, with Rnd3/RhoE inhibiting ROCK-mediated RhoA signaling—effectively having the opposite function of RhoA in some contexts (basbous2021pathophysiologicalfunctionsof pages 1-3).
- In plants, **ROP GTPases** have evolved plant-specific regulatory mechanisms including PRONE family RopGEFs not found in other organisms, and serve as the sole Rho-family branch, replacing the functions of Rac, Rho, and Cdc42 in a single versatile protein class (nielsen2020thesmallgtpase pages 15-16, nielsen2020thesmallgtpase pages 3-3).

## 4. Taxonomic Scope

The Rho GTPase family is present across all examined eukaryotic supergroups and was likely present in the last eukaryotic common ancestor (LECA) (filic2021regulationofthe pages 1-2, filic2021regulationofthe pages 2-4). The distribution of specific subfamilies varies dramatically across clades:

| Subfamily/type | Animals (Metazoa) | Fungi | Plants (Viridiplantae) | Amoebozoa | Other Protists |
|---|---|---|---|---|---|
| Classical Rho (RhoA/B/C-like) | Present; canonical animal Rho subfamily expanded in Metazoa (mosaddeghzadeh2021therhofamily pages 3-5, filic2021regulationofthe pages 2-4) | Present but limited repertoire; fungi retain Rho-type proteins such as Rho1-like members rather than the full metazoan expansion (dauttcastro2021thesmallgtpases pages 23-25) | Absent as a distinct subfamily; plants do not have separate RhoA/B/C-like class (liu2025genomewideidentificationand pages 1-2, nielsen2020thesmallgtpase pages 16-18) | No strict metazoan ortholog set; amoebozoans have independently diversified Rho-family members with partial functional analogies (filic2021regulationofthe pages 23-24, filic2021regulationofthe pages 4-5) | Variable/patchy across lineages; broad Rho-family presence predates major eukaryotic splits, but metazoan-style RhoA/B/C naming is not generally applicable (filic2021regulationofthe pages 1-2, filic2021regulationofthe pages 2-4) |
| Rac/ROP | Present; Rac subfamily widespread in animals (mosaddeghzadeh2021therhofamily pages 3-5, filic2021regulationofthe pages 2-4) | Present in some fungal lineages as Rac-like proteins, but repertoire is restricted relative to animals (dauttcastro2021thesmallgtpases pages 23-25) | Present as the only plant Rho-family branch: ROP/Rac-type GTPases; plants have a single ROP clade (liu2025genomewideidentificationand pages 1-2, nielsen2020thesmallgtpase pages 3-3) | Present; Rac-like proteins are prominent and amoebozoan repertoires independently expanded (filic2021regulationofthe pages 2-4, filic2021regulationofthe pages 23-24) | Present in many protists; Rac is inferred as an ancient/founding Rho-family form (filic2021regulationofthe pages 2-4) |
| Cdc42 | Present; canonical animal Cdc42 branch conserved and expanded (mosaddeghzadeh2021therhofamily pages 3-5, filic2021regulationofthe pages 2-4) | Present; fungi commonly retain Cdc42 with major roles in polarity (dauttcastro2021thesmallgtpases pages 23-25) | Absent as a separate subfamily; plant functions are instead handled within ROP/Rac-type proteins (liu2025genomewideidentificationand pages 1-2, nielsen2020thesmallgtpase pages 16-18) | Cdc42-like/related functions present in diversified amoebozoan repertoires, but not necessarily one-to-one orthologs (filic2021regulationofthe pages 23-24, filic2021regulationofthe pages 4-5) | Variable across protists; LECA likely already possessed Rho-family members, with later lineage-specific gain/loss (filic2021regulationofthe pages 1-2, filic2021regulationofthe pages 2-4) |
| RhoBTB | Present in animals (stiegler2020thepseudogtpasegroup pages 6-7) | Not established as a general fungal feature; no evidence here for broad fungal conservation (dauttcastro2021thesmallgtpases pages 23-25) | Absent/not reported in plants (liu2025genomewideidentificationand pages 1-2, nielsen2020thesmallgtpase pages 3-3) | Present; amoebozoan occurrence suggests ancient origin before opisthokont diversification (filic2021regulationofthe pages 4-5) | Likely patchy/uncertain outside animals and amoebozoa based on current evidence here (filic2021regulationofthe pages 4-5) |
| Rnd | Present in animals; metazoan atypical pseudoGTPase branch (stiegler2020thepseudogtpasegroup pages 4-6, basbous2021pathophysiologicalfunctionsof pages 1-3) | Not established as a conserved fungal subfamily in the evidence gathered (dauttcastro2021thesmallgtpases pages 23-25) | Absent as a plant subfamily (liu2025genomewideidentificationand pages 1-2) | No clear canonical Rnd branch established here; amoebozoa instead show independent diversification (filic2021regulationofthe pages 23-24) | Patchy/uncertain outside animals; not a universal pan-eukaryotic subfamily label despite ancient Rho-family origin (filic2021regulationofthe pages 1-2, filic2021regulationofthe pages 2-4) |
| RhoH | Present in animals, especially vertebrate/hematopoietic contexts (stiegler2020thepseudogtpasegroup pages 4-6, mosaddeghzadeh2021therhofamily pages 18-19) | Absent/not evidenced as a conserved fungal group (dauttcastro2021thesmallgtpases pages 23-25) | Absent in plants (liu2025genomewideidentificationand pages 1-2, nielsen2020thesmallgtpase pages 16-18) | Not established in amoebozoa by current evidence (filic2021regulationofthe pages 23-24, filic2021regulationofthe pages 4-5) | Likely absent or highly restricted outside animals; appears lineage-specific rather than universal (filic2021regulationofthe pages 1-2, filic2021regulationofthe pages 2-4) |
| RhoD/F | Present in animals as RHOD/RHOF atypical fast-cycling members (wang2022rhogtpasefamily pages 1-2, aspenstrom2022theroleof pages 2-4) | Not clearly established as conserved fungal subfamily in current evidence (dauttcastro2021thesmallgtpases pages 23-25) | Absent as distinct subfamily; plants instead have ROP-only branch (liu2025genomewideidentificationand pages 1-2) | No direct one-to-one ortholog assignment supported; amoebozoa contain independently diversified Rho-family proteins (filic2021regulationofthe pages 23-24, filic2021regulationofthe pages 4-5) | Patchy/uncertain outside animals; likely lineage-specific specializations rather than universal clades (filic2021regulationofthe pages 1-2, filic2021regulationofthe pages 2-4) |
| RhoU/V | Present in animals as RHOU/ RHOV atypical branch (wang2022rhogtpasefamily pages 1-2, aspenstrom2022theroleof pages 2-4) | Not established in fungi from current evidence (dauttcastro2021thesmallgtpases pages 23-25) | Absent as distinct subfamily; no separate plant RhoU/V branch (liu2025genomewideidentificationand pages 1-2, nielsen2020thesmallgtpase pages 16-18) | No clear canonical RhoU/V clade demonstrated; amoebozoan proteins are diversified independently (filic2021regulationofthe pages 23-24, filic2021regulationofthe pages 4-5) | Patchy/uncertain outside animals; not suitable as a universal family-wide label across protists (filic2021regulationofthe pages 1-2, filic2021regulationofthe pages 2-4) |


*Table: This table summarizes how major Rho GTPase subfamilies are distributed across eukaryotic clades. It is useful for GO review because it shows that PTHR24072 spans a pan-eukaryotic, evolutionarily heterogeneous family, so many subfamily/process annotations will not hold across all matched proteins.*

Key observations:

- **Animals (Metazoa):** The most expanded complement, with all 8 subfamilies present in mammals. The family underwent rapid expansion approximately 700 million years ago (filic2021regulationofthe pages 2-4). Mammals possess 20 canonical members.
- **Plants (Viridiplantae):** Plants lack Ras GTPases entirely and possess only a single Rho-family branch—the ROP/Rac-like GTPases—without separate Rho, Cdc42, Rnd, RhoH, or RhoBTB subfamilies (liu2025genomewideidentificationand pages 1-2, nielsen2020thesmallgtpase pages 3-3). Plant ROPs have evolved unique regulatory mechanisms including PRONE-family GEFs (nielsen2020thesmallgtpase pages 15-16).
- **Fungi:** Retain Rho1-type and Cdc42 proteins with major roles in polarity and morphogenesis, but have a more limited repertoire than animals (dauttcastro2021thesmallgtpases pages 23-25).
- **Amoebozoa:** Have independently diversified their Rho GTPase repertoire. *Dictyostelium discoideum* possesses approximately 20 Rho GTPases, but these arose through convergent evolution rather than shared ancestry with the mammalian complement (filic2021regulationofthe pages 1-2, filic2021regulationofthe pages 2-4, filic2021regulationofthe pages 23-24).
- **Other protists:** Variable numbers, e.g., 19 in *Entamoeba histolytica*, 5 in *Acanthamoeba castellanii*, reflecting lineage-specific gains and losses (filic2021regulationofthe pages 2-4).

The pan-eukaryotic distribution but highly variable subfamily architecture means that no single process or component GO term would hold across all 9,604 taxa matched by PTHR24072. Animal-specific processes (e.g., immune cell migration, neural crest cell polarity) do not apply to plants or fungi; plant-specific ROP functions do not apply to animals.

## 5. Over-Annotation Verdict

> Over-annotation verdict for **PTHR24072 (RHO FAMILY GTPASE)**: the current InterPro2GO state — **no mapped GO terms** — is **APPROPRIATE** and should be **ACCEPTED** as-is. This parent family is exceptionally heterogeneous, spanning **51,615 proteins across 9,604 taxa and 98 subfamilies**, and therefore does not support a single core molecular function, biological process, or cellular component term that is true for every match. Classical Rho-family members are bona fide GDP/GTP-switch GTPases with conserved catalytic machinery, but atypical members break that rule: **Rnd proteins and RhoH are pseudoGTPases lacking catalytic GTP hydrolysis**, while **RhoBTB proteins are so divergent that RhoBTB1/2 do not bind nucleotide and instead function mainly as BTB/Cullin3-associated adaptor proteins**. At the taxonomic level, the family is pan-eukaryotic, and plants contribute **ROP/Rac-like proteins** rather than the metazoan-style Rho/Cdc42 subfamily architecture, further arguing against parent-level process or component annotations. Because even apparently safe terms such as **GTP binding**, **GTPase activity**, **small GTPase mediated signal transduction**, or **actin cytoskeleton organization** fail for substantial parts of the family, adding GO terms at the parent level would risk systematic over-annotation. If future InterPro2GO mappings are desired, they should be assigned only to **functionally coherent child subfamilies** (for example, specific **PTHR24072:SF** entries), not to the broad parent family itself. (stiegler2020thepseudogtpasegroup pages 4-6, stiegler2020thepseudogtpasegroup pages 6-7, filic2021regulationofthe pages 1-2, liu2025genomewideidentificationand pages 1-2)


*Blockquote: This blockquote summarizes why the absence of InterPro2GO mappings for the broad RHO FAMILY GTPASE parent entry is currently the correct annotation state. It highlights the family’s biochemical and taxonomic heterogeneity and explains why any future GO mapping should be restricted to child subfamilies.*

### 5.1 Detailed Recommendation

**Recommended GO action pattern: ACCEPT (the current absence of mappings)**

The absence of InterPro2GO terms at the PTHR24072 parent family level is the correct annotation state. This assessment is based on three lines of evidence:

1. **Biochemical heterogeneity:** The family contains classical GTPases with full catalytic activity, pseudoGTPases that bind but cannot hydrolyze GTP (Rnd, RhoH), and members that cannot bind nucleotide at all (RhoBTB1/2) (stiegler2020thepseudogtpasegroup pages 4-6, stiegler2020thepseudogtpasegroup pages 6-7). Even the most fundamental molecular function term—GTP binding—would over-annotate RhoBTB proteins.

2. **Functional heterogeneity:** Downstream functions range from actin cytoskeleton regulation (classical Rho/Rac/Cdc42) to ubiquitin ligase adaptor activity (RhoBTB) to hematopoietic-specific immune signaling (RhoH) (stiegler2020thepseudogtpasegroup pages 6-7, mosaddeghzadeh2021therhofamily pages 18-19, hairston2025rhosmallgtpase pages 9-11, bement2024patterningofthe pages 1-6). Some members actively antagonize each other (Rnd3 inhibits RhoA signaling) (basbous2021pathophysiologicalfunctionsof pages 1-3).

3. **Taxonomic heterogeneity:** The family spans all eukaryotic supergroups, but subfamily composition varies radically. Plants have only ROP/Rac-type proteins with plant-specific regulators; animals have the full 8-subfamily complement; fungi have a restricted set (filic2021regulationofthe pages 1-2, filic2021regulationofthe pages 2-4, liu2025genomewideidentificationand pages 1-2). No biological process GO term is valid across all clades.

### 5.2 Recommendations for InterPro

- **Do not add GO terms to PTHR24072.** The parent family is too heterogeneous for any family-wide GO annotation.
- **GO terms should be pushed to child subfamily entries.** The 98 PTHR24072:SF subfamilies provide the appropriate granularity for GO annotation. For example:
  - Classical Rho subfamilies could receive GO:0003924 (GTPase activity), GO:0005525 (GTP binding), GO:0007264 (small GTPase mediated signal transduction)
  - Rnd subfamilies should receive GO:0005525 (GTP binding) but NOT GO:0003924 (GTPase activity)
  - RhoBTB subfamilies should receive terms related to ubiquitin ligase complex function rather than GTPase-related terms
  - Plant ROP subfamilies could receive appropriate plant-specific process terms
- **No InterPro structural change is needed.** The current family-type classification correctly groups these evolutionarily related proteins. The heterogeneity is appropriately managed by the 98 subfamilies.

This analysis is consistent with the broader principle that large, functionally divergent protein families—especially those containing pseudoenzyme members—require subfamily-level annotation rather than family-level GO mappings to avoid systematic over-annotation across databases.


References

1. (mosaddeghzadeh2021therhofamily pages 3-5): Niloufar Mosaddeghzadeh and Mohammad Reza Ahmadian. The rho family gtpases: mechanisms of regulation and signaling. Cells, 10:1831, Jul 2021. URL: https://doi.org/10.3390/cells10071831, doi:10.3390/cells10071831. This article has 449 citations.

2. (wang2022rhogtpasefamily pages 1-2): Tiantian Wang, Dean Rao, Chengpeng Yu, Jiaqi Sheng, Yiming Luo, Limin Xia, and Wenjie Huang. Rho gtpase family in hepatocellular carcinoma. Experimental Hematology & Oncology, Nov 2022. URL: https://doi.org/10.1186/s40164-022-00344-4, doi:10.1186/s40164-022-00344-4. This article has 74 citations and is from a peer-reviewed journal.

3. (hairston2025rhosmallgtpase pages 1-2): Dontrel William Spencer Hairston, Maria Mudryj, and Paramita Mitra Ghosh. Rho small gtpase family in androgen-regulated prostate cancer progression and metastasis. Cancers, 17:3680, Nov 2025. URL: https://doi.org/10.3390/cancers17223680, doi:10.3390/cancers17223680. This article has 1 citations.

4. (stiegler2020thepseudogtpasegroup pages 1-2): Amy L. Stiegler and Titus J. Boggon. The pseudogtpase group of pseudoenzymes. The FEBS Journal, 287:4232-4245, Sep 2020. URL: https://doi.org/10.1111/febs.15554, doi:10.1111/febs.15554. This article has 27 citations.

5. (mosaddeghzadeh2021therhofamily pages 5-6): Niloufar Mosaddeghzadeh and Mohammad Reza Ahmadian. The rho family gtpases: mechanisms of regulation and signaling. Cells, 10:1831, Jul 2021. URL: https://doi.org/10.3390/cells10071831, doi:10.3390/cells10071831. This article has 449 citations.

6. (lin2025structuraldynamicsof pages 3-4): Yuan Lin and Yi Zheng. Structural dynamics of rho gtpases. Feb 2025. URL: https://doi.org/10.1016/j.jmb.2024.168919, doi:10.1016/j.jmb.2024.168919. This article has 6 citations and is from a domain leading peer-reviewed journal.

7. (hairston2025rhosmallgtpase pages 7-9): Dontrel William Spencer Hairston, Maria Mudryj, and Paramita Mitra Ghosh. Rho small gtpase family in androgen-regulated prostate cancer progression and metastasis. Cancers, 17:3680, Nov 2025. URL: https://doi.org/10.3390/cancers17223680, doi:10.3390/cancers17223680. This article has 1 citations.

8. (mosaddeghzadeh2021therhofamily pages 1-3): Niloufar Mosaddeghzadeh and Mohammad Reza Ahmadian. The rho family gtpases: mechanisms of regulation and signaling. Cells, 10:1831, Jul 2021. URL: https://doi.org/10.3390/cells10071831, doi:10.3390/cells10071831. This article has 449 citations.

9. (mosaddeghzadeh2021therhofamily pages 12-14): Niloufar Mosaddeghzadeh and Mohammad Reza Ahmadian. The rho family gtpases: mechanisms of regulation and signaling. Cells, 10:1831, Jul 2021. URL: https://doi.org/10.3390/cells10071831, doi:10.3390/cells10071831. This article has 449 citations.

10. (bement2024patterningofthe pages 1-6): William M. Bement, Andrew B. Goryachev, Ann L. Miller, and George von Dassow. Patterning of the cell cortex by rho gtpases. Nature reviews. Molecular cell biology, 25:290-308, Jan 2024. URL: https://doi.org/10.1038/s41580-023-00682-z, doi:10.1038/s41580-023-00682-z. This article has 158 citations.

11. (aspenstrom2022theroleof pages 2-4): Pontus Aspenström. The role of fast-cycling atypical rho gtpases in cancer. Cancers, 14:1961, Apr 2022. URL: https://doi.org/10.3390/cancers14081961, doi:10.3390/cancers14081961. This article has 25 citations.

12. (mosaddeghzadeh2021therhofamily pages 18-19): Niloufar Mosaddeghzadeh and Mohammad Reza Ahmadian. The rho family gtpases: mechanisms of regulation and signaling. Cells, 10:1831, Jul 2021. URL: https://doi.org/10.3390/cells10071831, doi:10.3390/cells10071831. This article has 449 citations.

13. (filic2021regulationofthe pages 2-4): Vedrana Filić, Lucija Mijanović, Darija Putar, Antea Talajić, Helena Ćetković, and Igor Weber. Regulation of the actin cytoskeleton via rho gtpase signalling in dictyostelium and mammalian cells: a parallel slalom. Cells, 10:1592, Jun 2021. URL: https://doi.org/10.3390/cells10071592, doi:10.3390/cells10071592. This article has 46 citations.

14. (stiegler2020thepseudogtpasegroup pages 4-6): Amy L. Stiegler and Titus J. Boggon. The pseudogtpase group of pseudoenzymes. The FEBS Journal, 287:4232-4245, Sep 2020. URL: https://doi.org/10.1111/febs.15554, doi:10.1111/febs.15554. This article has 27 citations.

15. (basbous2021pathophysiologicalfunctionsof pages 1-3): Sara Basbous, Roberta Azzarelli, Emilie Pacary, and Violaine Moreau. Pathophysiological functions of rnd proteins. Small GTPases, 12:336-357, Oct 2021. URL: https://doi.org/10.1080/21541248.2020.1829914, doi:10.1080/21541248.2020.1829914. This article has 30 citations and is from a peer-reviewed journal.

16. (stiegler2020thepseudogtpasegroup pages 6-7): Amy L. Stiegler and Titus J. Boggon. The pseudogtpase group of pseudoenzymes. The FEBS Journal, 287:4232-4245, Sep 2020. URL: https://doi.org/10.1111/febs.15554, doi:10.1111/febs.15554. This article has 27 citations.

17. (hairston2025rhosmallgtpase pages 9-11): Dontrel William Spencer Hairston, Maria Mudryj, and Paramita Mitra Ghosh. Rho small gtpase family in androgen-regulated prostate cancer progression and metastasis. Cancers, 17:3680, Nov 2025. URL: https://doi.org/10.3390/cancers17223680, doi:10.3390/cancers17223680. This article has 1 citations.

18. (nielsen2020thesmallgtpase pages 15-16): Erik Nielsen. The small gtpase superfamily in plants: a conserved regulatory module with novel functions. Annual review of plant biology, 71:247-272, Apr 2020. URL: https://doi.org/10.1146/annurev-arplant-112619-025827, doi:10.1146/annurev-arplant-112619-025827. This article has 103 citations and is from a domain leading peer-reviewed journal.

19. (nielsen2020thesmallgtpase pages 3-3): Erik Nielsen. The small gtpase superfamily in plants: a conserved regulatory module with novel functions. Annual review of plant biology, 71:247-272, Apr 2020. URL: https://doi.org/10.1146/annurev-arplant-112619-025827, doi:10.1146/annurev-arplant-112619-025827. This article has 103 citations and is from a domain leading peer-reviewed journal.

20. (filic2021regulationofthe pages 1-2): Vedrana Filić, Lucija Mijanović, Darija Putar, Antea Talajić, Helena Ćetković, and Igor Weber. Regulation of the actin cytoskeleton via rho gtpase signalling in dictyostelium and mammalian cells: a parallel slalom. Cells, 10:1592, Jun 2021. URL: https://doi.org/10.3390/cells10071592, doi:10.3390/cells10071592. This article has 46 citations.

21. (dauttcastro2021thesmallgtpases pages 23-25): Mitzuko Dautt-Castro, Montserrat Rosendo-Vargas, and Sergio Casas-Flores. The small gtpases in fungal signaling conservation and function. Cells, 10:1039, Apr 2021. URL: https://doi.org/10.3390/cells10051039, doi:10.3390/cells10051039. This article has 52 citations.

22. (liu2025genomewideidentificationand pages 1-2): Zhida Liu, Guochao Xuanyuan, Shuqing Yang, Miru Du, Xiaoluo Zhang, Tingting Bao, Zhiwei Zhang, Wenbing Zhang, and Jun Zhao. Genome-wide identification and analysis of rop gtpase family members reveal their potential functions in biotic stress in potato (solanum tuberosum l.). BMC Plant Biology, Apr 2025. URL: https://doi.org/10.1186/s12870-025-06428-7, doi:10.1186/s12870-025-06428-7. This article has 3 citations and is from a peer-reviewed journal.

23. (nielsen2020thesmallgtpase pages 16-18): Erik Nielsen. The small gtpase superfamily in plants: a conserved regulatory module with novel functions. Annual review of plant biology, 71:247-272, Apr 2020. URL: https://doi.org/10.1146/annurev-arplant-112619-025827, doi:10.1146/annurev-arplant-112619-025827. This article has 103 citations and is from a domain leading peer-reviewed journal.

24. (filic2021regulationofthe pages 23-24): Vedrana Filić, Lucija Mijanović, Darija Putar, Antea Talajić, Helena Ćetković, and Igor Weber. Regulation of the actin cytoskeleton via rho gtpase signalling in dictyostelium and mammalian cells: a parallel slalom. Cells, 10:1592, Jun 2021. URL: https://doi.org/10.3390/cells10071592, doi:10.3390/cells10071592. This article has 46 citations.

25. (filic2021regulationofthe pages 4-5): Vedrana Filić, Lucija Mijanović, Darija Putar, Antea Talajić, Helena Ćetković, and Igor Weber. Regulation of the actin cytoskeleton via rho gtpase signalling in dictyostelium and mammalian cells: a parallel slalom. Cells, 10:1592, Jun 2021. URL: https://doi.org/10.3390/cells10071592, doi:10.3390/cells10071592. This article has 46 citations.

## Artifacts

- [Edison artifact artifact-00](PTHR24072-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](PTHR24072-deep-research-falcon_artifacts/artifact-01.md)
- [Edison artifact artifact-02](PTHR24072-deep-research-falcon_artifacts/artifact-02.md)

## Citations

1. stiegler2020thepseudogtpasegroup pages 1-2
2. mosaddeghzadeh2021therhofamily pages 12-14
3. stiegler2020thepseudogtpasegroup pages 6-7
4. mosaddeghzadeh2021therhofamily pages 5-6
5. basbous2021pathophysiologicalfunctionsof pages 1-3
6. dauttcastro2021thesmallgtpases pages 23-25
7. filic2021regulationofthe pages 2-4
8. filic2021regulationofthe pages 4-5
9. liu2025genomewideidentificationand pages 1-2
10. filic2021regulationofthe pages 23-24
11. nielsen2020thesmallgtpase pages 15-16
12. mosaddeghzadeh2021therhofamily pages 3-5
13. wang2022rhogtpasefamily pages 1-2
14. hairston2025rhosmallgtpase pages 1-2
15. lin2025structuraldynamicsof pages 3-4
16. hairston2025rhosmallgtpase pages 7-9
17. mosaddeghzadeh2021therhofamily pages 1-3
18. bement2024patterningofthe pages 1-6
19. aspenstrom2022theroleof pages 2-4
20. mosaddeghzadeh2021therhofamily pages 18-19
21. stiegler2020thepseudogtpasegroup pages 4-6
22. hairston2025rhosmallgtpase pages 9-11
23. nielsen2020thesmallgtpase pages 3-3
24. filic2021regulationofthe pages 1-2
25. nielsen2020thesmallgtpase pages 16-18
26. https://doi.org/10.3390/cells10071831,
27. https://doi.org/10.1186/s40164-022-00344-4,
28. https://doi.org/10.3390/cancers17223680,
29. https://doi.org/10.1111/febs.15554,
30. https://doi.org/10.1016/j.jmb.2024.168919,
31. https://doi.org/10.1038/s41580-023-00682-z,
32. https://doi.org/10.3390/cancers14081961,
33. https://doi.org/10.3390/cells10071592,
34. https://doi.org/10.1080/21541248.2020.1829914,
35. https://doi.org/10.1146/annurev-arplant-112619-025827,
36. https://doi.org/10.3390/cells10051039,
37. https://doi.org/10.1186/s12870-025-06428-7,