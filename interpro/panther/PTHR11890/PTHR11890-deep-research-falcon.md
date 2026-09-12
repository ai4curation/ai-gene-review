---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-28T20:28:44.766242'
end_time: '2026-06-28T20:49:52.628488'
duration_seconds: 1267.86
template_file: templates/interpro_family_research.md
template_variables:
  interpro_id: PTHR11890
  interpro_name: INTERLEUKIN-1 RECEPTOR FAMILY MEMBER
  interpro_short_name: Not specified
  interpro_type: family
  interpro_integrated: IPR015621
  member_databases: Not specified
  n_proteins: '11681'
  n_taxa: '3500'
  n_subfamilies: '13'
  interpro2go_terms: None mapped (no InterPro2GO terms for this entry)
  interpro_description: Not specified in InterPro
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 11
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: PTHR11890-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: PTHR11890-deep-research-falcon_artifacts/artifact-01.md
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
- **Accession:** PTHR11890
- **Name:** INTERLEUKIN-1 RECEPTOR FAMILY MEMBER
- **Short name:** Not specified
- **Entry type:** family
- **Integrated into / parent:** IPR015621
- **Member database signatures:** Not specified
- **Scale:** 11681 proteins across 3500 taxa, 13 subfamilies
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
**PTHR11890 (INTERLEUKIN-1 RECEPTOR FAMILY MEMBER)**, structured to support GO annotation review.

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
- **Accession:** PTHR11890
- **Name:** INTERLEUKIN-1 RECEPTOR FAMILY MEMBER
- **Short name:** Not specified
- **Entry type:** family
- **Integrated into / parent:** IPR015621
- **Member database signatures:** Not specified
- **Scale:** 11681 proteins across 3500 taxa, 13 subfamilies
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
**PTHR11890 (INTERLEUKIN-1 RECEPTOR FAMILY MEMBER)**, structured to support GO annotation review.

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


# Comprehensive Research Report: PTHR11890 — INTERLEUKIN-1 RECEPTOR FAMILY MEMBER

## 1. Family Definition and Biochemistry

### 1.1 Overview

PTHR11890 (INTERLEUKIN-1 RECEPTOR FAMILY MEMBER) is a PANTHER protein family entry integrated into InterPro entry IPR015621. It encompasses 11,681 proteins across approximately 3,500 taxa, organized into 13 subfamilies. The family corresponds to the interleukin-1 receptor (IL-1R) superfamily, which in humans comprises 10 canonical receptors (IL-1R1 through IL-1R10) plus the related IL1RAPL1 and IL1RAPL2 proteins (boraschi2022whatisil1 pages 3-5, garlanda2025il1familycytokines pages 1-2).

### 1.2 Domain Architecture and Fold

The canonical IL-1R family architecture consists of: (i) an extracellular portion containing up to three immunoglobulin (Ig)-like domains (D1, D2, D3); (ii) a single-pass transmembrane segment; and (iii) an intracellular Toll/IL-1 receptor (TIR) domain (boraschi2022whatisil1 pages 2-3, zhukova2025structuralanddynamic pages 6-7, zhukova2025structuralanddynamic pages 2-3). The three extracellular Ig-like domains are arranged in a distinctive curved, question-mark-like shape, where D1 and D2 form a rigid, integrated module stabilized by a conserved disulfide bond, while D3 connects to D2 via a long flexible linker permitting conformational movement (zhukova2025structuralanddynamic pages 2-3). This interdomain flexibility, centered on residues such as Glu202–204 in IL-1R1, is critical for ligand binding (zhukova2025structuralanddynamic pages 6-7).

The intracellular TIR domain is a conserved ~160 amino acid module adopting a characteristic α/β fold with a central parallel five-stranded β-sheet (βA–βE) surrounded by five α-helices (αA–αE) (zhukova2025structuralanddynamic pages 6-7, zhukova2025structuralanddynamic pages 7-8). Key functional surfaces include the BB loop and αB helix, which form the canonical dimerization interface essential for heterodimeric interactions between receptor TIR domains and recruitment of downstream adaptors such as MyD88 (zhukova2025structuralanddynamic pages 7-8). TIR domain sequence identity between different IL-1R family members is relatively low (25–37%), indicating important structural differences that determine functional specificity (zhukova2025structuralanddynamic pages 7-8).

### 1.3 Signaling Mechanism

Signal activation occurs through a stepwise process: an agonist cytokine binds its cognate primary receptor, and together this cytokine–receptor complex recruits a secondary/accessory receptor (most commonly IL-1R3/IL-1RAcP). The intracellular TIR domains of the two receptor chains are then brought into close proximity, initiating NF-κB signal transduction cascades through recruitment of the adaptor MyD88 and IRAK kinases (boraschi2022whatisil1 pages 2-3, fields2019structuralbasisof pages 3-6). This signaling paradigm is shared with Toll-like receptors (TLRs), indicating a deep evolutionary connection in innate immune signaling (boraschi2022whatisil1 pages 2-3, boraschi2022whatisil1 pages 3-5).

However, critically, **not all family members participate in this signaling paradigm**. IL-1R2 lacks a TIR domain and functions as a non-signaling decoy receptor (boraschi2022whatisil1 pages 2-3, zhukova2025structuralanddynamic pages 2-3). IL-1R8/SIGIRR has only a single Ig-like extracellular domain and actively suppresses signaling (boraschi2022whatisil1 pages 2-3, garlanda2025il1familycytokines pages 5-6). IL-1R9 and IL-1R10 are orphan receptors with no established immune signaling ligands, expressed primarily in the brain (boraschi2022whatisil1 pages 2-3, boraschi2022whatisil1 pages 5-6).

## 2. InterPro2GO Mapping Appropriateness

The entry currently has **no InterPro2GO terms mapped**. This is the appropriate status. The following analysis evaluates whether any GO terms could reasonably be applied to every protein matched by PTHR11890.

The comprehensive table below evaluates hypothetical GO terms that could be considered for this family:

| Hypothetical GO Term | GO ID (approximate) | Aspect (MF/BP/CC) | Would Apply to All Family Members? | Problem if Mapped at Family Level | Recommendation |
|---|---|---|---|---|---|
| cytokine receptor activity | GO:0004896 | MF | No | Over-broad for the family: IL1R2 is a decoy lacking signaling capacity, IL1R3/IL1R7 are accessory chains rather than stand-alone cytokine receptors, and IL1RAPL1/2 are neuronal/orphan IL-1R-related proteins with non-canonical functions rather than established cytokine receptors (boraschi2022whatisil1 pages 2-3, fields2019structuralbasisof pages 2-3, boraschi2022whatisil1 pages 3-5) | DO NOT MAP |
| interleukin-1 receptor activity | GO:0004908 | MF | No | True for IL1R1 and perhaps closely related ligand-binding IL-1 receptors only; false for IL1R2 decoy, IL1R3 accessory chain, IL1R8 negative regulator, IL1R9/10 orphan receptors, and IL1RAPL1/2 neuronal proteins. Family contains receptors for IL-33, IL-18, and IL-36 as well, not only IL-1 (boraschi2022whatisil1 pages 3-5, boraschi2022whatisil1 pages 2-3) | subfamily-only |
| signal transduction | GO:0007165 | BP | No | Many members do not positively transduce signals in the canonical sense: IL1R2 is a decoy that lacks a TIR signaling output, IL1R8 is inhibitory, and IL1RAPL1/2 are specialized neuronal proteins with divergent functions. A family-level BP term would collapse opposite functions into one annotation (boraschi2022whatisil1 pages 2-3, garlanda2025il1familycytokines pages 5-6, zhukova2025structuralanddynamic pages 2-3) | DO NOT MAP |
| inflammatory response | GO:0006954 | BP | No | Valid for many immune IL-1R members, but not for neuronal/orphan branches such as IL1RAPL1/2 and probably not uniformly across all taxa or all subfamilies. Also misses anti-inflammatory and inhibitory members such as IL1R2 and IL1R8, which suppress rather than promote inflammatory signaling (garlanda2025il1familycytokines pages 5-6, boraschi2022whatisil1 pages 2-3, boraschi2022whatisil1 pages 5-6) | subfamily-only |
| immune response | GO:0006955 | BP | No | Too broad and not universal: several family members are expressed mainly in brain and have non-immune functions, while IL1RAPL1/2 are neo-functionalized neuronal proteins. Mapping this to the whole family would clearly over-annotate non-immune members (boraschi2022whatisil1 pages 2-3, boraschi2022whatisil1 pages 5-6, boraschi2022whatisil1 pages 3-5) | DO NOT MAP |
| plasma membrane | GO:0005886 | CC | Partial | Many IL-1R proteins are membrane receptors, but not all biologically relevant products are strictly plasma-membrane localized in all contexts; soluble decoy forms exist for IL1R2, and this CC term is too generic to be useful for family-level functional review. It also adds little information and risks propagating low-value annotations (boraschi2022whatisil1 pages 2-3, zhukova2025structuralanddynamic pages 2-3, boraschi2022whatisil1 pages 3-5) | DO NOT MAP |
| interleukin-1-mediated signaling pathway | GO:0070498 | BP | No | Restricted mainly to the IL1R1 branch and closely related IL-1 signaling components; inappropriate for IL-33, IL-18, IL-36 receptors, accessory chains, inhibitory receptors, orphan receptors, and neuronal IL1RAPL proteins (boraschi2022whatisil1 pages 3-5, boraschi2022whatisil1 pages 2-3, fields2019structuralbasisof pages 2-3) | subfamily-only |
| negative regulation of interleukin-1-mediated signaling pathway | GO:approx.  regulation term | BP | No | True for IL1R2 and IL1R8/SIGIRR, but opposite of the function of canonical signaling receptors such as IL1R1, IL1R4, IL1R5, and IL1R6. This is a classic case of subfamily-specific and even opposite-function divergence within the family (boraschi2022whatisil1 pages 2-3, garlanda2025il1familycytokines pages 5-6) | subfamily-only |
| toll-like receptor signaling pathway via TIR-domain interactions | GO:approx. related innate immune signaling term | BP | No | The shared TIR domain does not justify assigning a common pathway term: receptor TIR domains are structural/signaling modules, but family members participate in distinct ligand systems and some lack signaling activity altogether. Family-level mapping would confuse architecture with conserved whole-protein biology (boraschi2022whatisil1 pages 2-3, zhukova2025structuralanddynamic pages 6-7, zhukova2025structuralanddynamic pages 7-8) | DO NOT MAP |
| synapse organization / neuronal signaling | GO:approx. synapse organization term | BP | No | Relevant to IL1RAPL1/2 and perhaps orphan brain-expressed IL-1R-related members, but not to canonical immune receptors. This illustrates strong neo-functionalization within the family and argues against any single BP term spanning all matched proteins (boraschi2022whatisil1 pages 5-6, boraschi2022whatisil1 pages 3-5) | subfamily-only |


*Table: This table evaluates plausible GO terms for the InterPro family PTHR11890 and shows why none are suitable as universal family-level annotations. It is useful for review because it highlights subfamily-specific, opposite, and non-immune functions that would cause over-annotation.*

**Key finding:** No single GO term in any aspect (Molecular Function, Biological Process, or Cellular Component) is universally true across all members of PTHR11890. The family encompasses signaling receptors, decoy receptors, negative regulators, accessory chains, orphan receptors, and neo-functionalized neuronal proteins. Even the most generic terms such as "cytokine receptor activity" (GO:0004896) would be incorrect for IL-1R2 (which cannot signal), IL1RAPL1/2 (which are neuronal synapse organizers), and IL-1R8/SIGIRR (which is an inhibitory receptor) (boraschi2022whatisil1 pages 2-3, garlanda2025il1familycytokines pages 5-6).

## 3. Functional Divergence Across the Family

The IL-1R family exhibits extreme functional heterogeneity, summarized in the following table:

| Receptor Name (standardized) | Alternative Names / Gene Symbol | Functional Class | Primary Ligand(s) | Key Structural Feature | Taxonomic Scope |
|---|---|---|---|---|---|
| IL-1R1 | IL1R1; IL-1RI; CD121a | Signaling receptor | IL-1α, IL-1β | Typical IL-1R architecture with 3 extracellular Ig-like domains, TM region, intracellular TIR domain; forms signaling complex with IL-1R3 | Broad vertebrate distribution; reported as present in many vertebrates, though some analyses place clear homologs from later vertebrate clades onward (fields2019structuralbasisof pages 3-6, boraschi2022whatisil1 pages 2-3, wang2025il1superfamilyacross pages 6-8, boraschi2022whatisil1 pages 3-5) |
| IL-1R2 | IL1R2; IL-1RII; CD121b | Decoy receptor | IL-1α, IL-1β | Extracellular IL-1-binding receptor architecture but lacks intracellular TIR signaling capacity; membrane and soluble decoy forms reported | Likely mammal-enriched / possibly mammal-specific in recent evolutionary analyses (boraschi2022whatisil1 pages 2-3, zhukova2025structuralanddynamic pages 2-3, wang2025il1superfamilyacross pages 8-11, boraschi2022whatisil1 pages 3-5) |
| IL-1R3 | IL1RAP; IL-1RAcP | Co-receptor / accessory chain | Co-receptor for IL-1R1, IL-1R4, IL-1R6 complexes; also part of other IL-1 family receptor complexes | Typical IL-1R architecture with 3 Ig-like domains and intracellular TIR; promiscuous accessory chain | Ancient within vertebrates; widely distributed, with ancestry traced deep in vertebrates and broad conservation across vertebrate taxa (boraschi2022whatisil1 pages 2-3, fields2019structuralbasisof pages 2-3, wang2025il1superfamilyacross pages 8-11, boraschi2022whatisil1 pages 3-5) |
| IL-1R4 | IL1RL1; ST2; IL-33R | Signaling receptor | IL-33 | Typical IL-1R-like transmembrane receptor with extracellular Ig-like region and intracellular TIR; signals with IL-1R3 | More recent than several core IL-1Rs; recent analysis places emergence after amphibians (boraschi2022whatisil1 pages 2-3, wang2025il1superfamilyacross pages 8-11, boraschi2022whatisil1 pages 3-5, garlanda2025il1familycytokines pages 1-2) |
| IL-1R5 | IL18R1; IL-18Rα | Signaling receptor | IL-18 | Typical IL-1R architecture with 3 Ig-like domains and TIR; primary ligand-binding chain of IL-18 receptor complex | Present across vertebrates; homologs reported from cartilaginous fish onward (boraschi2022whatisil1 pages 3-5, wang2025il1superfamilyacross pages 6-8, wang2025il1superfamilyacross pages 3-4) |
| IL-1R6 | IL1RL2; IL-36R; IL-1Rrp2 | Signaling receptor | IL-36α, IL-36β, IL-36γ | Typical IL-1R architecture with extracellular Ig-like domains and intracellular TIR; signals with IL-1R3 | Vertebrate receptor; some analyses place clear homologs from later vertebrate clades, while functional class is conserved in mammals (boraschi2022whatisil1 pages 2-3, wang2025il1superfamilyacross pages 6-8, boraschi2022whatisil1 pages 3-5, garlanda2025il1familycytokines pages 1-2) |
| IL-1R7 | IL18RAP; IL-18Rβ | Co-receptor / accessory chain | Co-receptor for IL-18 receptor signaling with IL-1R5 | IL-1R-like accessory chain with extracellular Ig-like domains and intracellular TIR | Present across vertebrates; homologs reported from cartilaginous fish onward (boraschi2022whatisil1 pages 3-5, wang2025il1superfamilyacross pages 6-8, wang2025il1superfamilyacross pages 3-4) |
| IL-1R8 | SIGIRR; TIR8 | Negative regulator | No single canonical agonist ligand; also serves as co-receptor for IL-37 with IL-18Rα | Distinctive single extracellular Ig-like domain plus intracellular TIR; inhibitory rather than canonical activating receptor | One of the most ancient IL-1R family members; found in basal vertebrates including jawless fish, broadly distributed in vertebrates (boraschi2022whatisil1 pages 2-3, garlanda2025il1familycytokines pages 5-6, wang2025il1superfamilyacross pages 8-11, wang2025il1superfamilyacross pages 6-8, boraschi2022whatisil1 pages 3-5) |
| IL-1R9 | IL1RAPL1; TIGIRR-2 | Orphan / neuronal receptor | No firmly established canonical IL-1-family ligand; reported brain-associated/orphan | IL-1R family member with neuronal specialization; not a canonical immune signaling receptor in current understanding | Tetrapod/brain-associated branch in some schemes; orphan receptor with non-immune neuronal role (boraschi2022whatisil1 pages 5-6, boraschi2022whatisil1 pages 3-5, garlanda2025il1familycytokines pages 1-2) |
| IL-1R10 | IL1RAPL2; TIGIRR / TIGIRR-1 | Orphan / neuronal receptor | No known canonical ligand | IL-1R family member with neuronal/orphan specialization; not well supported as canonical immune receptor | Vertebrate neuronal/orphan branch; function remains poorly defined and non-canonical (boraschi2022whatisil1 pages 3-5, boraschi2022whatisil1 pages 2-3, garlanda2025il1familycytokines pages 1-2) |
| IL1RAPL1 | Interleukin-1 receptor accessory protein-like 1; gene symbol IL1RAPL1 | Neuronal / synapse organizer | No canonical IL-1-family ligand established | IL-1R-related protein with strong neo-functionalization toward neuronal function | Tetrapoda only; absent in fish, emerged later in vertebrate evolution (~365 Mya) (boraschi2022whatisil1 pages 5-6) |
| IL1RAPL2 | Interleukin-1 receptor accessory protein-like 2; gene symbol IL1RAPL2 | Neuronal / synapse-associated orphan | No canonical IL-1-family ligand established | IL-1R-related protein specialized toward neuronal function rather than core cytokine signaling | Vertebrate neuronal lineage; exact deep taxonomic distribution less clear than IL1RAPL1, but treated as brain-associated orphan receptor family member (boraschi2022whatisil1 pages 3-5, boraschi2022whatisil1 pages 2-3) |


*Table: This table summarizes the major IL-1 receptor family members relevant to PTHR11890, highlighting their functional divergence, structural differences, ligands, and taxonomic scope. It is useful for GO review because it shows that the family includes signaling receptors, decoys, inhibitory receptors, and neuronal proteins, arguing against broad family-level GO mappings.*

### 3.1 Functional Classes

The family can be divided into at least six distinct functional categories:

**Signaling receptors** — IL-1R1 (binds IL-1α/β), IL-1R4/ST2 (binds IL-33), IL-1R5/IL-18Rα (binds IL-18), and IL-1R6/IL-36R (binds IL-36α/β/γ). These are the canonical pro-inflammatory signaling receptors that form ternary complexes with accessory chains and activate NF-κB downstream signaling (fields2019structuralbasisof pages 3-6, boraschi2022whatisil1 pages 3-5, garlanda2025il1familycytokines pages 1-2).

**Accessory/co-receptors** — IL-1R3/IL-1RAcP and IL-1R7/IL-18Rβ function as secondary receptors that do not independently bind ligands but are recruited to binary ligand–primary receptor complexes to enable signaling (fields2019structuralbasisof pages 2-3, fields2019structuralbasisof pages 14-17).

**Decoy receptor** — IL-1R2 retains extracellular Ig-like domains for high-affinity ligand binding but completely lacks the intracellular TIR domain, making it unable to transduce signals. It functions as a negative regulator by sequestering IL-1α and IL-1β into inactive complexes. IL-1R2 exists in both membrane-bound and soluble forms (boraschi2022whatisil1 pages 2-3, zhukova2025structuralanddynamic pages 2-3).

**Negative regulator** — IL-1R8/SIGIRR possesses a unique architecture with only a single extracellular Ig-like domain and suppresses signaling by multiple IL-1R family members and TLRs. It also serves as a co-receptor for the anti-inflammatory cytokine IL-37 (boraschi2022whatisil1 pages 2-3, garlanda2025il1familycytokines pages 5-6).

**Orphan receptors** — IL-1R9/TIGIRR-2 and IL-1R10/TIGIRR have no established canonical ligands and are primarily expressed in the brain. Their functions remain poorly characterized but are likely non-immune (boraschi2022whatisil1 pages 2-3, boraschi2022whatisil1 pages 5-6).

**Neo-functionalized neuronal proteins** — IL1RAPL1 and IL1RAPL2, while structurally related to the IL-1R family, have diverged to function as neuronal synapse organizers. IL1RAPL1 mutations are associated with X-linked intellectual disability, and IL1RAPL2 is expressed in retinal ganglion cells and other neuronal populations (boraschi2022whatisil1 pages 5-6, boraschi2022whatisil1 pages 3-5). These proteins represent a clear case of neo-functionalization where the ancestral immune receptor fold has been repurposed for a completely different biological role.

### 3.2 Opposing Functions

A critical consideration for GO annotation is that some family members have directly **opposing functions**: IL-1R1 promotes inflammatory signaling, while IL-1R2 and IL-1R8/SIGIRR actively suppress it. Assigning "inflammatory response" or "signal transduction" to the family would simultaneously over-annotate the decoy receptor and negative regulator (boraschi2022whatisil1 pages 2-3, garlanda2025il1familycytokines pages 5-6, zhukova2025structuralanddynamic pages 2-3).

## 4. Taxonomic Scope

### 4.1 Evolutionary Origin

The IL-1R family is primarily a vertebrate protein family. Most IL-1R genes originated approximately 420 million years ago, coinciding with early vertebrate evolution, possibly associated with whole-genome duplication events (535–485 Mya) (boraschi2022whatisil1 pages 3-5, wang2025il1superfamilyacross pages 12-14, wang2025il1superfamilyacross pages 3-4). All IL-1R superfamily members except TIGIRR-2 are reported to be present across all vertebrates, having diverged before the separation of bony and cartilaginous fish (wang2025il1superfamilyacross pages 3-4).

### 4.2 Member-Specific Distribution

IL-1R8/SIGIRR is among the most ancient family members, with homologs identified in jawless fish (Myxini) showing 39.70% identity to human SIGIRR (wang2025il1superfamilyacross pages 8-11, wang2025il1superfamilyacross pages 12-14). IL-1R3/IL-1RAcP is also widely distributed across vertebrates (wang2025il1superfamilyacross pages 8-11). In contrast, IL-1R4/ST2 emerged after amphibians (wang2025il1superfamilyacross pages 8-11, wang2025il1superfamilyacross pages 6-8), while IL-1R2 may be unique to mammals with no homologs confirmed in birds or other lineages (wang2025il1superfamilyacross pages 8-11). IL1RAPL1 appeared only in Tetrapoda (~365 Mya) and is absent in fish (boraschi2022whatisil1 pages 3-5, boraschi2022whatisil1 pages 5-6). Teleost fish possess unique IL-1R family variants such as DIGIRR (a truncated receptor with two Ig-like domains) (boraschi2022whatisil1 pages 2-3). The PTHR11890 signature matching 3,500 taxa likely includes IL-1R-like sequences from invertebrate genomes that share the TIR domain and/or Ig-like domains but may not be true functional orthologs of vertebrate IL-1R proteins (boraschi2022whatisil1 pages 2-3, wang2025il1superfamilyacross pages 12-14).

### 4.3 Cross-Taxon Functional Conservation

The extensive study by Wang et al. (2025) across 400+ animal species (2,700 IL-1R sequences from 407 species) demonstrated that domain architecture varies significantly across taxonomic groups. Different receptor groups show taxon-specific domain distributions: for example, the TIR domain is extraordinarily conserved from plants to mammals, but the extracellular Ig-like domain composition varies, with some groups lacking TIR domains in most species (wang2025il1superfamilyacross pages 11-12, wang2025il1superfamilyacross pages 4-6). Critically, no single immune function or signaling activity can be assumed to hold across all taxa matched by PTHR11890, given that some matched proteins may be invertebrate TIR-domain-containing proteins with distinct functional roles.

## 5. Over-Annotation Verdict

### 5.1 Summary Assessment

The current status of PTHR11890 — **no InterPro2GO terms mapped** — is **sound and appropriate**. This family-level PANTHER entry is too functionally heterogeneous for any GO term to apply universally across all 11,681 matched proteins and 13 subfamilies. The family includes:

- Pro-inflammatory signaling receptors (IL-1R1, IL-1R4, IL-1R5, IL-1R6)
- A decoy/anti-inflammatory receptor (IL-1R2, lacking TIR domain)
- Accessory/co-receptors (IL-1R3, IL-1R7)
- A negative regulatory receptor (IL-1R8/SIGIRR)
- Orphan receptors with neuronal expression (IL-1R9, IL-1R10)
- Neo-functionalized neuronal proteins (IL1RAPL1, IL1RAPL2)

### 5.2 Recommended GO Action Pattern

**For the PTHR11890 family-level entry: ACCEPT (the current null mapping is correct)**

No InterPro2GO terms should be added at this family level. The absence of mapped GO terms correctly reflects the biological reality that no molecular function, biological process, or cellular component term applies universally to all members.

### 5.3 Recommendations for InterPro

If GO annotations are desired for this protein family, they should be applied at the **subfamily level** only:

- **IL-1/IL-33/IL-36 signaling receptor subfamilies**: Could receive "interleukin-1 receptor activity" or related MF terms, and process terms like "inflammatory response" or specific interleukin-mediated signaling pathway terms.
- **IL-1R2 subfamily**: Could receive "negative regulation of interleukin-1-mediated signaling pathway" or similar decoy-specific terms.
- **IL-1R8/SIGIRR subfamily**: Could receive terms related to negative regulation of innate immune signaling.
- **IL1RAPL1/2 subfamilies**: Could receive neuronal-specific terms such as "synapse organization" where supported by experimental evidence.
- **IL-1R3/IL-1RAcP subfamily**: Could receive co-receptor-specific terms.

Any GO term proposed for addition to the family-level entry should be rejected (**MARK_AS_OVER_ANNOTATED**) because the functional divergence within this family, including directly opposing activities (pro-inflammatory vs. anti-inflammatory), immune vs. non-immune roles, and the presence of catalytically/signaling-dead members, makes family-level annotation inherently misleading.

References

1. (boraschi2022whatisil1 pages 3-5): Diana Boraschi. What is il-1 for? the functions of interleukin-1 across evolution. Frontiers in Immunology, Apr 2022. URL: https://doi.org/10.3389/fimmu.2022.872155, doi:10.3389/fimmu.2022.872155. This article has 145 citations and is from a peer-reviewed journal.

2. (garlanda2025il1familycytokines pages 1-2): Cecilia Garlanda, Irene Di Ceglie, and Sebastien Jaillon. Il-1 family cytokines in inflammation and immunity. Cellular &amp; Molecular Immunology, 22(11):1345-1362, Oct 2025. URL: https://doi.org/10.1038/s41423-025-01358-8, doi:10.1038/s41423-025-01358-8. This article has 80 citations and is from a peer-reviewed journal.

3. (boraschi2022whatisil1 pages 2-3): Diana Boraschi. What is il-1 for? the functions of interleukin-1 across evolution. Frontiers in Immunology, Apr 2022. URL: https://doi.org/10.3389/fimmu.2022.872155, doi:10.3389/fimmu.2022.872155. This article has 145 citations and is from a peer-reviewed journal.

4. (zhukova2025structuralanddynamic pages 6-7): J. Zhukova, J. Lopatnikova, S. Sennikov, R. C. Russo, Cecilia Garlanda, Bernhard Ryffel, and Gaby Palmer. Structural and dynamic properties of il1 receptors. Frontiers in Immunology, Dec 2025. URL: https://doi.org/10.3389/fimmu.2025.1714624, doi:10.3389/fimmu.2025.1714624. This article has 6 citations and is from a peer-reviewed journal.

5. (zhukova2025structuralanddynamic pages 2-3): J. Zhukova, J. Lopatnikova, S. Sennikov, R. C. Russo, Cecilia Garlanda, Bernhard Ryffel, and Gaby Palmer. Structural and dynamic properties of il1 receptors. Frontiers in Immunology, Dec 2025. URL: https://doi.org/10.3389/fimmu.2025.1714624, doi:10.3389/fimmu.2025.1714624. This article has 6 citations and is from a peer-reviewed journal.

6. (zhukova2025structuralanddynamic pages 7-8): J. Zhukova, J. Lopatnikova, S. Sennikov, R. C. Russo, Cecilia Garlanda, Bernhard Ryffel, and Gaby Palmer. Structural and dynamic properties of il1 receptors. Frontiers in Immunology, Dec 2025. URL: https://doi.org/10.3389/fimmu.2025.1714624, doi:10.3389/fimmu.2025.1714624. This article has 6 citations and is from a peer-reviewed journal.

7. (fields2019structuralbasisof pages 3-6): James K. Fields, Sebastian Günther, and Eric J. Sundberg. Structural basis of il-1 family cytokine signaling. Frontiers in Immunology, Jun 2019. URL: https://doi.org/10.3389/fimmu.2019.01412, doi:10.3389/fimmu.2019.01412. This article has 388 citations and is from a peer-reviewed journal.

8. (garlanda2025il1familycytokines pages 5-6): Cecilia Garlanda, Irene Di Ceglie, and Sebastien Jaillon. Il-1 family cytokines in inflammation and immunity. Cellular &amp; Molecular Immunology, 22(11):1345-1362, Oct 2025. URL: https://doi.org/10.1038/s41423-025-01358-8, doi:10.1038/s41423-025-01358-8. This article has 80 citations and is from a peer-reviewed journal.

9. (boraschi2022whatisil1 pages 5-6): Diana Boraschi. What is il-1 for? the functions of interleukin-1 across evolution. Frontiers in Immunology, Apr 2022. URL: https://doi.org/10.3389/fimmu.2022.872155, doi:10.3389/fimmu.2022.872155. This article has 145 citations and is from a peer-reviewed journal.

10. (fields2019structuralbasisof pages 2-3): James K. Fields, Sebastian Günther, and Eric J. Sundberg. Structural basis of il-1 family cytokine signaling. Frontiers in Immunology, Jun 2019. URL: https://doi.org/10.3389/fimmu.2019.01412, doi:10.3389/fimmu.2019.01412. This article has 388 citations and is from a peer-reviewed journal.

11. (wang2025il1superfamilyacross pages 6-8): Weibin Wang, Dawei Li, Kai-yong Luo, Baozheng Chen, Tingting Hao, Xuzhen Li, Dazhong Guo, Yang Dong, and Ya Ning. Il-1 superfamily across 400+ species: therapeutic targets and disease implications. Biology, 14:561, May 2025. URL: https://doi.org/10.3390/biology14050561, doi:10.3390/biology14050561. This article has 2 citations.

12. (wang2025il1superfamilyacross pages 8-11): Weibin Wang, Dawei Li, Kai-yong Luo, Baozheng Chen, Tingting Hao, Xuzhen Li, Dazhong Guo, Yang Dong, and Ya Ning. Il-1 superfamily across 400+ species: therapeutic targets and disease implications. Biology, 14:561, May 2025. URL: https://doi.org/10.3390/biology14050561, doi:10.3390/biology14050561. This article has 2 citations.

13. (wang2025il1superfamilyacross pages 3-4): Weibin Wang, Dawei Li, Kai-yong Luo, Baozheng Chen, Tingting Hao, Xuzhen Li, Dazhong Guo, Yang Dong, and Ya Ning. Il-1 superfamily across 400+ species: therapeutic targets and disease implications. Biology, 14:561, May 2025. URL: https://doi.org/10.3390/biology14050561, doi:10.3390/biology14050561. This article has 2 citations.

14. (fields2019structuralbasisof pages 14-17): James K. Fields, Sebastian Günther, and Eric J. Sundberg. Structural basis of il-1 family cytokine signaling. Frontiers in Immunology, Jun 2019. URL: https://doi.org/10.3389/fimmu.2019.01412, doi:10.3389/fimmu.2019.01412. This article has 388 citations and is from a peer-reviewed journal.

15. (wang2025il1superfamilyacross pages 12-14): Weibin Wang, Dawei Li, Kai-yong Luo, Baozheng Chen, Tingting Hao, Xuzhen Li, Dazhong Guo, Yang Dong, and Ya Ning. Il-1 superfamily across 400+ species: therapeutic targets and disease implications. Biology, 14:561, May 2025. URL: https://doi.org/10.3390/biology14050561, doi:10.3390/biology14050561. This article has 2 citations.

16. (wang2025il1superfamilyacross pages 11-12): Weibin Wang, Dawei Li, Kai-yong Luo, Baozheng Chen, Tingting Hao, Xuzhen Li, Dazhong Guo, Yang Dong, and Ya Ning. Il-1 superfamily across 400+ species: therapeutic targets and disease implications. Biology, 14:561, May 2025. URL: https://doi.org/10.3390/biology14050561, doi:10.3390/biology14050561. This article has 2 citations.

17. (wang2025il1superfamilyacross pages 4-6): Weibin Wang, Dawei Li, Kai-yong Luo, Baozheng Chen, Tingting Hao, Xuzhen Li, Dazhong Guo, Yang Dong, and Ya Ning. Il-1 superfamily across 400+ species: therapeutic targets and disease implications. Biology, 14:561, May 2025. URL: https://doi.org/10.3390/biology14050561, doi:10.3390/biology14050561. This article has 2 citations.

## Artifacts

- [Edison artifact artifact-00](PTHR11890-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](PTHR11890-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. zhukova2025structuralanddynamic pages 2-3
2. zhukova2025structuralanddynamic pages 6-7
3. zhukova2025structuralanddynamic pages 7-8
4. fields2019structuralbasisof pages 3-6
5. fields2019structuralbasisof pages 2-3
6. fields2019structuralbasisof pages 14-17
7. https://doi.org/10.3389/fimmu.2022.872155,
8. https://doi.org/10.1038/s41423-025-01358-8,
9. https://doi.org/10.3389/fimmu.2025.1714624,
10. https://doi.org/10.3389/fimmu.2019.01412,
11. https://doi.org/10.3390/biology14050561,