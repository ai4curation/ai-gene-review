---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-21T20:46:05.660858'
end_time: '2026-06-21T20:55:24.845046'
duration_seconds: 559.18
template_file: templates/interpro_family_research.md
template_variables:
  interpro_id: PTHR23065
  interpro_name: F-BAR domain-containing protein
  interpro_short_name: F-BAR_domain_protein
  interpro_type: family
  interpro_integrated: None (top-level entry)
  member_databases: Not specified
  n_proteins: '23423'
  n_taxa: '7646'
  n_subfamilies: '21'
  interpro2go_terms: None mapped (no InterPro2GO terms for this entry)
  interpro_description: This family of proteins is involved in various cellular processes
    related to membrane dynamics, including endocytosis and vesicle-mediated transport.
    Members of this family typically contain an F-BAR domain that mediates membrane
    binding and tubulation, playing a crucial role in the reorganization of the cytoskeleton
    and morphogenesis of neurons. They are also involved in synaptic vesicle endocytosis,
    which is essential for neurotransmission. Some family members regulate the activity
    of enzymes and receptors by affecting their cellular localization, and they may
    also participate in cytokinesis and cell cycle regulation. Additionally, these
    proteins can interact with actin and microtubule cytoskeletons, influencing cell
    shape, migration, and signaling pathways.
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
  path: PTHR23065-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: PTHR23065-deep-research-falcon_artifacts/artifact-01.md
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
- **Accession:** PTHR23065
- **Name:** F-BAR domain-containing protein
- **Short name:** F-BAR_domain_protein
- **Entry type:** family
- **Integrated into / parent:** None (top-level entry)
- **Member database signatures:** Not specified
- **Scale:** 23423 proteins across 7646 taxa, 21 subfamilies
- **Current InterPro2GO terms (the mappings under review):** None mapped (no InterPro2GO terms for this entry)
- **InterPro description:** This family of proteins is involved in various cellular processes related to membrane dynamics, including endocytosis and vesicle-mediated transport. Members of this family typically contain an F-BAR domain that mediates membrane binding and tubulation, playing a crucial role in the reorganization of the cytoskeleton and morphogenesis of neurons. They are also involved in synaptic vesicle endocytosis, which is essential for neurotransmission. Some family members regulate the activity of enzymes and receptors by affecting their cellular localization, and they may also participate in cytokinesis and cell cycle regulation. Additionally, these proteins can interact with actin and microtubule cytoskeletons, influencing cell shape, migration, and signaling pathways.

### Why entry type matters:

An entry of type **domain**, **repeat**, or **homologous_superfamily** identifies a
structural/functional *module*, not a whole-protein function. GO terms describing a
whole-protein activity or process attached to such a module systematically over-annotate
every protein that merely *contains* the module. An entry of type **family** is more
likely to support whole-protein function terms, but only if the family is functionally
homogeneous.

## Research Target

Provide a comprehensive, citation-backed research report on the InterPro entry
**PTHR23065 (F-BAR domain-containing protein)**, structured to support GO annotation review.

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
- **Accession:** PTHR23065
- **Name:** F-BAR domain-containing protein
- **Short name:** F-BAR_domain_protein
- **Entry type:** family
- **Integrated into / parent:** None (top-level entry)
- **Member database signatures:** Not specified
- **Scale:** 23423 proteins across 7646 taxa, 21 subfamilies
- **Current InterPro2GO terms (the mappings under review):** None mapped (no InterPro2GO terms for this entry)
- **InterPro description:** This family of proteins is involved in various cellular processes related to membrane dynamics, including endocytosis and vesicle-mediated transport. Members of this family typically contain an F-BAR domain that mediates membrane binding and tubulation, playing a crucial role in the reorganization of the cytoskeleton and morphogenesis of neurons. They are also involved in synaptic vesicle endocytosis, which is essential for neurotransmission. Some family members regulate the activity of enzymes and receptors by affecting their cellular localization, and they may also participate in cytokinesis and cell cycle regulation. Additionally, these proteins can interact with actin and microtubule cytoskeletons, influencing cell shape, migration, and signaling pathways.

### Why entry type matters:

An entry of type **domain**, **repeat**, or **homologous_superfamily** identifies a
structural/functional *module*, not a whole-protein function. GO terms describing a
whole-protein activity or process attached to such a module systematically over-annotate
every protein that merely *contains* the module. An entry of type **family** is more
likely to support whole-protein function terms, but only if the family is functionally
homogeneous.

## Research Target

Provide a comprehensive, citation-backed research report on the InterPro entry
**PTHR23065 (F-BAR domain-containing protein)**, structured to support GO annotation review.

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


# Comprehensive Research Report: InterPro Entry PTHR23065 (F-BAR Domain-Containing Protein)

## Executive Summary

PTHR23065 represents the F-BAR domain-containing protein family, a top-level PANTHER family entry spanning 23,423 proteins across 7,646 taxa with 21 subfamilies. Currently, **no InterPro2GO terms are mapped** to this entry. This report evaluates whether this absence is appropriate or whether specific GO terms should be recommended, based on extensive structural, functional, and evolutionary evidence.

**Verdict**: The absence of GO terms is **partially appropriate but incomplete**. The family exhibits substantial functional heterogeneity that precludes most biological process and cellular component terms. However, conserved domain-level molecular function terms describing membrane binding and curvature sensing are warranted. **Recommendation: MODIFY—add minimal conserved molecular function terms only; avoid process/component over-annotation.**

---

## 1. Family Definition and Biochemistry

### 1.1 Structural Architecture

The F-BAR domain (also termed EFC/extended FCH domain or FCH-BAR) is an ~200-280 amino acid module that forms an antiparallel homodimer with a characteristic crescent or "banana" shape (wang2009molecularmechanismof pages 1-2, rao2011membraneshapingby pages 1-3, ahmed2010fbardomainproteins pages 1-2). Crystal structures of multiple F-BAR proteins—including CIP4, FBP17, syndapin/Pacsin, and FCHo2—reveal a conserved fold consisting of three antiparallel α-helices per monomer that dimerize into an elongated structure approximately 200 Å long (wang2009molecularmechanismof pages 1-2, rao2011membraneshapingby pages 1-3, safari2012thebardomain pages 7-10).

The concave membrane-binding surface displays **conserved clusters of positively charged residues (lysine and arginine)** that electrostatically interact with negatively charged phospholipids, particularly phosphatidylserine and phosphatidylinositol 4,5-bisphosphate [PI(4,5)P2] (rao2011membraneshapingby pages 1-3, ahmed2010fbardomainproteins pages 1-2, stanishnevakonovalova2016theroleof pages 1-2). Specific basic patches documented in structural studies include conserved residues such as K127, K130, K145, K146, and K148 in syndapin 1 F-BAR (rao2010molecularbasisfor pages 1-2), and equivalent positions in CIP4 and FBP17 (rao2011membraneshapingby pages 1-3, ahmed2010fbardomainproteins pages 1-2).

### 1.2 Mechanistic Basis of Membrane Binding and Tubulation

F-BAR domains bind membranes through a two-step mechanism: (1) electrostatic attraction between the positively charged concave surface and acidic membrane lipids, and (2) scaffolding of membrane curvature matching the intrinsic curvature of the dimeric structure (rao2011membraneshapingby pages 1-3, stanishnevakonovalova2016theroleof pages 1-2). The F-BAR domain curvature is shallower (larger tubule diameter ~50-100 nm) compared to classical N-BAR domains, corresponding to early-stage membrane invaginations such as clathrin-coated pit initiation (wang2009molecularmechanismof pages 1-2, safari2012thebardomain pages 7-10).

Some F-BAR proteins, notably the Pacsin/syndapin subfamily, possess a unique **amphipathic wedge loop** (e.g., residues 119-126 in syndapin 1) protruding from the membrane-binding surface that inserts into the lipid bilayer, enhancing membrane deformation and enabling generation of both wide tubules and narrower constrictions (wang2009molecularmechanismof pages 1-2, rao2010molecularbasisfor pages 1-2). Mutation of hydrophobic residues in this wedge (I122, M123) abolishes tubulation activity *in vivo* (rao2010molecularbasisfor pages 1-2).

Many F-BAR proteins undergo **autoinhibition** in full-length form: for example, full-length syndapin 1 does not tubulate membranes in cells, while its isolated F-BAR domain is highly active, suggesting that the C-terminal SH3 domain clamps onto the F-BAR domain until released by binding partners or membrane recruitment (rao2010molecularbasisfor pages 1-2, stanishnevakonovalova2016theroleof pages 1-2).

### 1.3 Conserved Features vs. Subfamily Divergence

**Conserved across the family:**
- Homodimeric F-BAR domain fold (rao2011membraneshapingby pages 1-3, ahmed2010fbardomainproteins pages 1-2, safari2012thebardomain pages 1-5)
- Positively charged concave membrane-binding surface (rao2011membraneshapingby pages 1-3, stanishnevakonovalova2016theroleof pages 1-2)
- Membrane curvature sensing/induction capability (rao2011membraneshapingby pages 1-3, stanishnevakonovalova2016theroleof pages 1-2, carman2018bardomainproteins—a pages 1-2)
- Binding preference for acidic phospholipids (ahmed2010fbardomainproteins pages 1-2, liu2015fbarfamilyproteins pages 2-4, safari2012thebardomain pages 5-7)

**Variable/subfamily-specific:**
- Exact lipid selectivity (e.g., PI(4,5)P2 vs. PI(3)P vs. phosphatidylserine preference differs) (ahmed2010fbardomainproteins pages 1-2, liu2015fbarfamilyproteins pages 2-4)
- Presence/absence of amphipathic insertion elements (wang2009molecularmechanismof pages 1-2, rao2010molecularbasisfor pages 1-2)
- Additional functional domains defining subfamily identity (see Section 3)

---

## 2. InterPro2GO Mapping Appropriateness

### 2.1 Current Status

**Zero GO terms are currently mapped to PTHR23065.** This contrasts with many protein families where at least generic molecular function or component terms are assigned.

### 2.2 Evaluation of Potential Terms

| Potential GO term | Universality assessment | Specificity level | Recommendation |
|---|---|---|---|
| **lipid binding** (MF) | Broadly supported for F-BAR domains because the conserved positively charged concave surface binds negatively charged membrane phospholipids, but lipid preferences vary and some members use auxiliary regions/domains for specificity; safe only as a high-level biochemical property, not as a precise family function (rao2011membraneshapingby pages 1-3, ahmed2010fbardomainproteins pages 1-2, safari2012thebardomain pages 1-5, safari2012thebardomain pages 5-7) | Too generic | KEEP_AS_NON_CORE |
| **phospholipid binding** (MF) | Better supported than generic lipid binding: F-BAR domains are defined by binding acidic phospholipids such as PI(4,5)P2 / phosphatidylserine through conserved basic residues on the concave face; however exact lipid selectivity differs among subfamilies (rao2011membraneshapingby pages 1-3, ahmed2010fbardomainproteins pages 1-2, liu2015fbarfamilyproteins pages 2-4, safari2012thebardomain pages 5-7) | Appropriate but still broad | MODIFY |
| **membrane binding** (MF) | Mechanistically near-universal at the domain level across F-BAR proteins: membrane association is the defining shared property of the fold, mediated by dimeric crescent surfaces and conserved basic patches; this is one of the few terms likely to hold across the family (wang2009molecularmechanismof pages 1-2, rao2011membraneshapingby pages 1-3, ahmed2010fbardomainproteins pages 1-2, liu2015fbarfamilyproteins pages 1-2) | Appropriate | ACCEPT |
| **membrane curvature sensing** (MF) | Strongly supported as a BAR/F-BAR family property in structural and review literature, but degree and geometry of curvature preference vary; still more universal than specific trafficking processes (rao2011membraneshapingby pages 1-3, stanishnevakonovalova2016theroleof pages 1-2, carman2018bardomainproteins—a pages 1-2) | Appropriate | ACCEPT |
| **membrane tubulation** / **membrane bending** (MF/BP-like functional description) | Many F-BAR proteins tubulate membranes in vitro, but tubule diameter and strength differ, some full-length proteins are autoinhibited, and some subfamilies specialize in protrusions or signaling rather than generic tubulation; not guaranteed for every matched protein in vivo (wang2009molecularmechanismof pages 1-2, rao2010molecularbasisfor pages 1-2, ahmed2010fbardomainproteins pages 2-4, safari2012thebardomain pages 7-10) | Subfamily-specific / assay-dependent | MODIFY |
| **endomembrane system / membrane** (CC) | True for many members but far too generic to be informative, and localization differs widely among plasma membrane, endosomes, caveolae, podosomes, growth cones, bud necks, etc. (liu2015fbarfamilyproteins pages 1-2, safari2012thebardomain pages 1-5, liu2015fbarfamilyproteins pages 5-6, liu2015fbarfamilyproteins pages 6-7) | Too generic | KEEP_AS_NON_CORE |
| **plasma membrane** (CC) | Common but not universal; many family members act at plasma membrane-associated structures, yet others localize to endosomes, T-tubules, neuronal structures, or cytokinetic sites, so this overstates uniformity (liu2015fbarfamilyproteins pages 1-2, safari2012thebardomain pages 1-5, liu2015fbarfamilyproteins pages 6-7, safari2012thebardomain pages 5-7) | Too generic / not universal | MODIFY |
| **clathrin-mediated endocytosis** (BP) | Not universal: strongly supported for FCHO1/2, CIP4/FBP17/TOCA proteins, PACSINs, and some others, but not for kinase-like FES/FER, many srGAPs, GAS7, or all fungal homologs; should not be applied to the whole family (liu2015fbarfamilyproteins pages 2-4, liu2015fbarfamilyproteins pages 5-6, liu2015fbarfamilyproteins pages 4-5, safari2012thebardomain pages 7-10) | Subfamily-specific | REMOVE |
| **endocytosis** (BP) | Over-broad for the whole family: many but not all F-BAR proteins participate in endocytosis, while others function mainly in protrusions, adhesion, cytokinesis, neuronal morphogenesis, or signaling (liu2015fbarfamilyproteins pages 1-2, liu2015fbarfamilyproteins pages 5-6, liu2015fbarfamilyproteins pages 6-7, safari2012thebardomain pages 7-10) | Subfamily-specific | REMOVE |
| **vesicle-mediated transport** (BP) | Present for subsets involved in endocytic/caveolar traffic, but not universally true across srGAP, FES/FER, GAS7, or other signaling/morphogenesis-biased members (liu2015fbarfamilyproteins pages 1-2, liu2015fbarfamilyproteins pages 5-6, liu2015fbarfamilyproteins pages 6-7) | Subfamily-specific | REMOVE |
| **actin cytoskeleton organization** (BP) | Widespread but still not universal as a core family term: many F-BAR proteins recruit WASP/N-WASP/WAVE or dynamin-linked actin regulators, yet the exact output varies and some members are primarily membrane/kinase scaffolds (liu2015fbarfamilyproteins pages 1-2, liu2015fbarfamilyproteins pages 2-4, stanishnevakonovalova2016theroleof pages 1-2, carman2018bardomainproteins—a pages 1-2) | Broad but not universal | KEEP_AS_NON_CORE |
| **regulation of actin polymerization** (BP) | Supported for many SH3-containing subfamilies through WASP/N-WASP/WAVE interactions, but not all F-BAR proteins share the same downstream actin effectors or outputs (liu2015fbarfamilyproteins pages 2-4, liu2015fbarfamilyproteins pages 4-5, safari2012thebardomain pages 5-7) | Subfamily-specific | MODIFY |
| **filopodium assembly / membrane protrusion** (BP) | Limited to subsets such as TOCA-1, srGAPs, PSTPIP2, PACSIN2, GAS7, and some FCHSD-related functions; opposite geometry/protrusive behavior in some members highlights family divergence (liu2015fbarfamilyproteins pages 4-5, liu2015fbarfamilyproteins pages 6-7) | Subfamily-specific | REMOVE |
| **lamellipodium organization** (BP) | Restricted to certain subfamilies such as CIP4, FES/FER, PSTPIP1; not a universal family property (liu2015fbarfamilyproteins pages 5-6, liu2015fbarfamilyproteins pages 6-7) | Subfamily-specific | REMOVE |
| **phagocytosis** (BP) | Demonstrated for specific members such as FBP17/PSTPIP-related macrophage functions, but clearly not family-wide across taxa and subfamilies (liu2015fbarfamilyproteins pages 1-2, liu2015fbarfamilyproteins pages 5-6, safari2012thebardomain pages 7-10) | Subfamily-specific | REMOVE |
| **podosome assembly** (BP) | Specific to subsets including FBP17, PSTPIP2, CIP4-related macrophage/invadopodia pathways; unsuitable for all matches (liu2015fbarfamilyproteins pages 5-6, liu2015fbarfamilyproteins pages 6-7, safari2012thebardomain pages 7-10) | Subfamily-specific | REMOVE |
| **cytokinesis** (BP) | Valid for some fungal and metazoan PCH/F-BAR proteins, but not a universal function of the entire family (liu2015fbarfamilyproteins pages 1-2, liu2015fbarfamilyproteins pages 6-7) | Subfamily-specific | REMOVE |
| **cell adhesion / cell migration** (BP) | Relevant especially to FES/FER, lamellipodial and protrusion-associated subfamilies, but too divergent and context-dependent for a family-wide mapping (liu2015fbarfamilyproteins pages 1-2, liu2015fbarfamilyproteins pages 6-7) | Subfamily-specific | REMOVE |
| **synaptic vesicle endocytosis / neuronal morphogenesis** (BP) | True for specialized neuronal subfamilies such as PACSINs and GAS7-related proteins, but would leak into non-neural taxa and many non-neuronal family members (wang2009molecularmechanismof pages 1-2, liu2015fbarfamilyproteins pages 6-7) | Taxon- and subfamily-specific | REMOVE |
| **caveola / caveolin-dependent endocytosis** (CC/BP) | NOSTRIN-centered and endothelial-context specific; clearly not universal across the family or across taxa (liu2015fbarfamilyproteins pages 5-6, liu2015fbarfamilyproteins pages 6-7) | Subfamily-specific | REMOVE |


*Table: This table evaluates candidate GO terms for the PTHR23065 F-BAR domain-containing protein family, emphasizing whether each term is truly universal across the family or only valid for particular subfamilies. It is useful for deciding whether InterPro2GO should remain empty, accept only core membrane-binding terms, or avoid over-annotation with pathway- and lineage-specific functions.*

### 2.3 Recommended GO Mappings

**ACCEPT (appropriate for family-wide annotation):**
- **GO:0016020 | membrane** (CC) — but only as a non-core/broad localization term
- **GO:0005488 | binding** > **GO:0005543 | phospholipid binding** (MF) — the most defensible molecular function; all F-BAR domains bind acidic membrane phospholipids via conserved basic residues (rao2011membraneshapingby pages 1-3, ahmed2010fbardomainproteins pages 1-2, liu2015fbarfamilyproteins pages 2-4)

**MODIFY (narrow to more specific or mark as non-core):**
- Membrane curvature sensing/generation: No exact GO term exists, but this is the closest to a universal F-BAR activity. Consider petitioning GO for a more precise "membrane curvature sensing" molecular function term.
- Membrane tubulation: Only in vitro or for subsets; many full-length proteins are autoinhibited (rao2010molecularbasisfor pages 1-2, stanishnevakonovalova2016theroleof pages 1-2).

**REMOVE / DO NOT ADD (subfamily-specific, would over-annotate):**
- Clathrin-mediated endocytosis (BP): Valid for FCHO, CIP4/FBP17/TOCA, PACSIN subfamilies but not for FES/FER tyrosine kinases, srGAPs, GAS7, or fungal homologs (liu2015fbarfamilyproteins pages 2-4, liu2015fbarfamilyproteins pages 4-5, safari2012thebardomain pages 7-10)
- Endocytosis (BP): Overly broad; not universal (liu2015fbarfamilyproteins pages 5-6, liu2015fbarfamilyproteins pages 6-7)
- Actin cytoskeleton organization (BP): Many but not all members recruit WASP/WAVE; subfamily-dependent (liu2015fbarfamilyproteins pages 1-2, liu2015fbarfamilyproteins pages 2-4)
- Filopodium, lamellipodium, phagocytosis, podosome, cytokinesis, adhesion (BP): All subfamily-specific (liu2015fbarfamilyproteins pages 5-6, liu2015fbarfamilyproteins pages 4-5, liu2015fbarfamilyproteins pages 6-7)
- Synaptic vesicle endocytosis, neuronal morphogenesis (BP): Taxon- and cell type-restricted (wang2009molecularmechanismof pages 1-2, liu2015fbarfamilyproteins pages 6-7)
- Caveola-related terms (CC/BP): NOSTRIN-specific, endothelial context (liu2015fbarfamilyproteins pages 5-6, liu2015fbarfamilyproteins pages 6-7)
- Plasma membrane (CC): Common but not universal; many act on endosomes, T-tubules, or other compartments (safari2012thebardomain pages 1-5, safari2012thebardomain pages 5-7)

### 2.4 Rationale for Minimal Annotation

PTHR23065 is a **family-level entry**, meaning it groups proteins by shared F-BAR domain architecture but encompasses significant functional divergence (see Section 3). Applying whole-protein biological process or pathway terms systematically over-annotates proteins that contain the F-BAR domain as a membrane-targeting module but perform distinct downstream functions dictated by auxiliary domains and interaction partners.

---

## 3. Functional Divergence Across the Family

### 3.1 Subfamily Classification

The F-BAR family is classified into **nine major subfamilies** based on domain architecture and phylogenetic analysis (ahmed2010fbardomainproteins pages 1-2, liu2015fbarfamilyproteins pages 1-2, liu2015fbarfamilyproteins pages 2-4, safari2012thebardomain pages 1-5):

| Subfamily | Representative members | Domain architecture (besides F-BAR) | Primary cellular functions | Key binding partners |
|---|---|---|---|---|
| CIP4 | CIP4/TRIP10, FBP17/FNBP1, TOCA-1/FNBP1L | HR1/Cdc42-binding region; C-terminal SH3 | Clathrin-mediated endocytosis; vesicle initiation/scission; phagocytosis and podosome formation (especially FBP17); filopodium formation (especially TOCA-1); actin-coupled membrane remodeling (ahmed2010fbardomainproteins pages 2-4, liu2015fbarfamilyproteins pages 2-4, liu2015fbarfamilyproteins pages 4-5, safari2012thebardomain pages 7-10) | Cdc42; WASP/N-WASP; dynamin/dynamin-2; WASP-WIP complex; phospholipids including PI(4,5)P2-rich membranes (liu2015fbarfamilyproteins pages 2-4, liu2015fbarfamilyproteins pages 4-5, safari2012thebardomain pages 7-10) |
| FCHO | FCHO1, FCHO2 | C-terminal μ-homology domain (μHD) | Early initiation of clathrin-coated pits; recruitment of endocytic scaffold machinery; curvature initiation at plasma membrane (liu2015fbarfamilyproteins pages 2-4, liu2015fbarfamilyproteins pages 4-5, safari2012thebardomain pages 7-10) | Eps15; intersectin; AP2/clathrin-associated machinery; phospholipids (liu2015fbarfamilyproteins pages 4-5, safari2012thebardomain pages 7-10) |
| srGAP | srGAP1, srGAP2, srGAP3, srGAP4 | Central RhoGAP domain; C-terminal SH3 | Membrane protrusion/filopodium formation; neuronal morphogenesis and migration; regulation of Rho-family GTPase signaling; some members behave as inverse-F-BAR-like membrane protrusion factors (liu2015fbarfamilyproteins pages 2-4, liu2015fbarfamilyproteins pages 4-5) | Cdc42, Rac1, RhoA; WASP (srGAP1), N-WASP (srGAP2), WAVE1 (srGAP3); phospholipids (liu2015fbarfamilyproteins pages 2-4, liu2015fbarfamilyproteins pages 4-5) |
| PACSIN / Syndapin | PACSIN1, PACSIN2, PACSIN3; syndapins | C-terminal SH3; NPF motifs; some have hydrophobic insertion/wedge loop features in F-BAR region | Endocytosis; vesicle constriction/scission; coupling membrane remodeling to actin regulation; microspikes/lamellipodia-like structures; isoform-specific roles in synaptic and general membrane trafficking (wang2009molecularmechanismof pages 1-2, rao2010molecularbasisfor pages 1-2, ahmed2010fbardomainproteins pages 2-4, liu2015fbarfamilyproteins pages 4-5) | Dynamin; N-WASP/WASP; EHD proteins; synaptojanin; SOS; phospholipids (rao2010molecularbasisfor pages 1-2, ahmed2010fbardomainproteins pages 2-4, liu2015fbarfamilyproteins pages 4-5) |
| PSTPIP | PSTPIP1, PSTPIP2 | PSTPIP1: PEST motifs + C-terminal SH3; PSTPIP2: lacks SH3/PEST | Endocytosis; phagocytosis/podosome regulation; cytokinesis and adhesion (PSTPIP1); filopodium/motility regulation in macrophage-related contexts (PSTPIP2) (liu2015fbarfamilyproteins pages 5-6, liu2015fbarfamilyproteins pages 6-7) | N-WASP; dynamin-2; FBP17 antagonistically in podosome regulation; phospholipids (liu2015fbarfamilyproteins pages 5-6) |
| FCHSD | FCHSD1, FCHSD2/Carom | Two SH3 domains | Endocytosis; membrane protrusion structures; possible regulation of cell growth/migration/adhesion through scaffolding interactions (liu2015fbarfamilyproteins pages 5-6, liu2015fbarfamilyproteins pages 6-7) | WASP; TOCA-1; MAGI-1; CASK; phospholipids (liu2015fbarfamilyproteins pages 5-6, liu2015fbarfamilyproteins pages 6-7) |
| FES/FER | FES, FER | Central SH2 domain; C-terminal tyrosine kinase domain; adjacent F-BAR extension (FX) membrane-binding region | Lamellipodium formation; cell motility; adhesion signaling; cytoskeletal regulation linked to kinase signaling rather than canonical endocytic scaffolding (liu2015fbarfamilyproteins pages 2-4, liu2015fbarfamilyproteins pages 6-7) | Phospholipids; cortactin; adhesion-associated partners such as PECAM-1 are reported for FER/FES-family signaling contexts (ahmed2010fbardomainproteins pages 2-4, liu2015fbarfamilyproteins pages 6-7) |
| NOSTRIN | NOSTRIN | C-terminal SH3; central region mediating additional interactions | Caveolin-dependent endocytosis in endothelial contexts; trafficking/translocation of eNOS; membrane scission-related remodeling (liu2015fbarfamilyproteins pages 5-6, liu2015fbarfamilyproteins pages 6-7) | N-WASP; dynamin-2; caveolin-1; eNOS; phospholipids (liu2015fbarfamilyproteins pages 5-6, liu2015fbarfamilyproteins pages 6-7) |
| GAS7 | GAS7 | SH3 and WW domains (human GAS7); mouse GAS7 retains WW-like interaction capacity | Filopodium formation; neurite outgrowth and neuronal morphogenesis; higher-order F-BAR assembly in actin-linked membrane remodeling (liu2015fbarfamilyproteins pages 5-6, liu2015fbarfamilyproteins pages 6-7) | N-WASP; phospholipids; WASP-associated scaffolds/Cdc42-dependent assembly factors in recent reconstitution work (liu2015fbarfamilyproteins pages 5-6) |


*Table: This table summarizes the nine major F-BAR protein subfamilies, their distinguishing domain architectures, representative members, core cellular functions, and major binding partners. It is useful for assessing functional heterogeneity across PTHR23065 and for judging whether any GO term could apply uniformly across the full family.*

### 3.2 Functional Neofunctionalization and Specialization

The F-BAR domain serves as a **membrane-targeting and curvature-sensing module**, but the *biological function* of each protein is determined by:

1. **Auxiliary domains** (SH3, RhoGAP, tyrosine kinase, HR1/Cdc42-binding, μHD) that dictate binding partners and signaling context (liu2015fbarfamilyproteins pages 1-2, liu2015fbarfamilyproteins pages 2-4, carman2018bardomainproteins—a pages 1-2).
2. **Tissue/cell-type expression patterns** (e.g., neuronal PACSINs vs. macrophage FBP17 vs. endothelial NOSTRIN) (ahmed2010fbardomainproteins pages 2-4, liu2015fbarfamilyproteins pages 5-6, liu2015fbarfamilyproteins pages 6-7).
3. **Evolutionary lineage** (metazoan-specific neuronal functions, fungal cytokinesis roles, etc.).

**Key examples of functional divergence:**

- **CIP4/FBP17/TOCA-1 subfamily**: Endocytosis, phagocytosis, podosome formation in macrophages, filopodium formation; recruits WASP/N-WASP and dynamin via SH3 domain and Cdc42 via HR1 domain (liu2015fbarfamilyproteins pages 2-4, liu2015fbarfamilyproteins pages 4-5, safari2012thebardomain pages 7-10).
  
- **FCHO1/2 subfamily**: Specialized for *initiating* clathrin-coated pit assembly, acting upstream of classical endocytic machinery; recruits Eps15 and intersectin via μHD domain but lacks direct WASP binding (liu2015fbarfamilyproteins pages 4-5, safari2012thebardomain pages 7-10).

- **srGAP subfamily**: RhoGAP domain inactivates Rho-family GTPases; induces *outward* membrane protrusions (filopodia) rather than invaginations, behaving as "inverse F-BAR" proteins; involved in neuronal morphogenesis and migration (liu2015fbarfamilyproteins pages 2-4, liu2015fbarfamilyproteins pages 4-5).

- **FES/FER subfamily**: Non-receptor tyrosine kinases; F-BAR domain targets signaling complexes to membranes, with FX extension enhancing lipid binding; function primarily in adhesion signaling, lamellipodium formation, and cytoskeletal regulation, *not* canonical endocytosis (ahmed2010fbardomainproteins pages 2-4, liu2015fbarfamilyproteins pages 2-4, liu2015fbarfamilyproteins pages 6-7).

- **NOSTRIN**: Specialized for caveolin-dependent endocytosis in endothelial cells; regulates eNOS (endothelial nitric oxide synthase) trafficking; not generalizable to other taxa or cell types (liu2015fbarfamilyproteins pages 5-6, liu2015fbarfamilyproteins pages 6-7).

- **Pacsin/Syndapin subfamily**: Neuron-enriched isoforms (Pacsin1) mediate synaptic vesicle recycling; possess unique wedge loop for membrane constriction; isoform 2 generates microspikes/lamellipodia-like structures (wang2009molecularmechanismof pages 1-2, rao2010molecularbasisfor pages 1-2, ahmed2010fbardomainproteins pages 2-4, liu2015fbarfamilyproteins pages 4-5).

- **GAS7**: Neuronal differentiation; regulates neurite outgrowth via N-WASP binding through SH3/WW domains; involved in higher-order F-BAR assembly dynamics (liu2015fbarfamilyproteins pages 5-6, liu2015fbarfamilyproteins pages 6-7).

### 3.3 Absence of Pseudo-enzymes

F-BAR domains are **structural scaffolds, not enzymes**; thus, the concept of catalytically dead or pseudo-enzyme members does not apply. However, there is evidence of **autoinhibited states** (e.g., full-length syndapin 1, PICK1) where the membrane-binding activity is suppressed until release by specific activators (rao2010molecularbasisfor pages 1-2, stanishnevakonovalova2016theroleof pages 1-2, safari2012thebardomain pages 5-7).

### 3.4 Opposite Functional Outputs

The srGAP subfamily exhibits a functionally opposite membrane geometry preference compared to most F-BAR proteins: while CIP4, FCHO, and PACSIN induce *inward* membrane curvature (invaginations), srGAP proteins generate *outward* protrusions (filopodia), earning the designation "inverse F-BAR" or "IF-BAR" (liu2015fbarfamilyproteins pages 2-4, liu2015fbarfamilyproteins pages 4-5). This polarity reversal is determined by the combination of F-BAR geometry and RhoGAP-mediated signaling, highlighting that the F-BAR domain output is modulated by protein context.

---

## 4. Taxonomic Scope

### 4.1 Phylogenetic Distribution

F-BAR domain-containing proteins are found in **all eukaryotes except plants** (ahmed2010fbardomainproteins pages 1-2, safari2012thebardomain pages 1-5, safari2012thebardomain pages 5-7). The InterPro entry PTHR23065 spans 7,646 taxa, confirming broad eukaryotic conservation.

**Presence in:**
- **Fungi**: Fission yeast Cdc15 and budding yeast Hof1/Syp1 (cytokinesis and bud neck septation) (safari2012thebardomain pages 1-5, safari2012thebardomain pages 5-7)
- **Metazoa**: Extensive diversification into nine subfamilies in mammals; neuronal-specific isoforms (PACSINs, GAS7), immune cell-specific (FBP17, PSTPIP), endothelial-specific (NOSTRIN) (liu2015fbarfamilyproteins pages 1-2, liu2015fbarfamilyproteins pages 2-4, liu2015fbarfamilyproteins pages 5-6, liu2015fbarfamilyproteins pages 6-7)
- **Protists/non-metazoan eukaryotes**: Documented in *Dictyostelium*, choanoflagellates, and other unicellular eukaryotes (safari2012thebardomain pages 1-5)

**Absence in:**
- **Plants**: F-BAR proteins are conspicuously absent from plant genomes, likely due to distinct membrane remodeling machinery (safari2012thebardomain pages 1-5, safari2012thebardomain pages 5-7)
- **Prokaryotes**: BAR domain superfamily is eukaryote-specific

### 4.2 Taxon-Specific Functions That Should Not Propagate

Many mapped process terms in other databases are **metazoan- or cell-type-specific** and would leak inappropriately into fungi, protists, or even between metazoan tissues:

- **Synaptic vesicle endocytosis**: Only applies to neuronal PACSINs in animals with nervous systems (wang2009molecularmechanismof pages 1-2, liu2015fbarfamilyproteins pages 6-7)
- **Phagocytosis**: Macrophage/immune cell-specific (FBP17, PSTPIP) (liu2015fbarfamilyproteins pages 5-6, safari2012thebardomain pages 7-10)
- **Caveolin-dependent endocytosis**: NOSTRIN-specific, endothelial context (liu2015fbarfamilyproteins pages 5-6, liu2015fbarfamilyproteins pages 6-7)
- **Neurite outgrowth/neuronal morphogenesis**: srGAPs, GAS7, TOCA-1 in neural contexts (liu2015fbarfamilyproteins pages 4-5, liu2015fbarfamilyproteins pages 6-7)

Applying these to the family entry would over-annotate fungal Cdc15 homologs, protist F-BAR proteins, and even mammalian non-neuronal subfamily members.

---

## 5. Over-Annotation Verdict and Recommendations

### 5.1 Summary Assessment

**InterPro2GO for PTHR23065 is currently sound in avoiding over-annotation**, given the family's high functional heterogeneity. However, it is **overly conservative** in omitting even conserved domain-level molecular function terms.

### 5.2 Recommended GO Action Pattern

**For PTHR23065 (top-level family entry):**

| GO Term Category | Recommendation | Specific Action |
|---|---|---|
| **Conserved molecular functions** (membrane binding, phospholipid binding) | **ACCEPT** with "contributes_to" or "enables" evidence | Add GO:0005543 (phospholipid binding), possibly GO:0044877 (protein-containing complex binding for dimerization). Mark as IEA (inferred from electronic annotation) or IDA (direct assay from structural studies). |
| **Membrane curvature sensing** | **MODIFY** | Petition GO for a new term or use existing related terms with caution; this is the core conserved biochemical property but lacks a precise GO term. |
| **Biological processes** (endocytosis, actin organization, etc.) | **REMOVE / DO NOT ADD** | These are subfamily-specific; if added, they should be mapped to child entries (subfamilies) in InterPro or to individual UniProt entries, not to PTHR23065. |
| **Cellular components** (plasma membrane, endosome, etc.) | **KEEP_AS_NON_CORE** or remove | Too variable and localization-dependent; minimally useful for a family entry. |

**For child entries (if InterPro splits into subfamilies):**

- CIP4/FBP17/TOCA-1 subfamily → clathrin-mediated endocytosis, Cdc42 binding, WASP/dynamin recruitment
- FCHO subfamily → clathrin coat assembly initiation, Eps15/intersectin binding
- srGAP subfamily → Rho GTPase activator activity, filopodium assembly, neuronal morphogenesis
- PACSIN/Syndapin subfamily → synaptic vesicle endocytosis (isoform 1), membrane tubule constriction
- FES/FER subfamily → non-receptor tyrosine kinase activity, cell adhesion, lamellipodium formation
- NOSTRIN → caveolin-dependent endocytosis, eNOS regulation
- etc.

### 5.3 Recommendation to InterPro

**InterPro should consider:**

1. **Retaining no GO terms at the PTHR23065 family level** for biological processes and cellular components, given functional heterogeneity.
2. **Adding minimal molecular function terms**: phospholipid binding (GO:0005543), membrane binding (GO:0016020 as enabling term), and potentially protein homodimerization (GO:0042803).
3. **If subfamilies are defined as separate InterPro entries**, map process-specific terms to those child entries rather than the parent.
4. **Flagging PTHR23065 in InterPro2GO documentation** as a case where domain-level vs. whole-protein function distinction is critical.

### 5.4 Recommended Action Pattern

**For gene products matching PTHR23065:**

- **ACCEPT**: Molecular function terms related to membrane binding and curvature sensing (domain-level properties).
- **MODIFY**: Avoid propagating subfamily-specific process terms (endocytosis, actin organization, etc.) unless additional evidence from auxiliary domains or taxon context supports them.
- **MARK_AS_OVER_ANNOTATED**: Any existing annotations claiming universal endocytosis, phagocytosis, filopodium, or other pathway-specific functions for all F-BAR proteins.
- **KEEP_AS_NON_CORE**: Generic membrane/cellular component terms if present, but deprioritize.

---

## 6. Conclusions

PTHR23065 (F-BAR domain-containing protein) represents a **functionally heterogeneous family** unified by a shared membrane-binding and curvature-sensing domain fold but diversified into at least nine subfamilies with distinct biological roles. The **current absence of InterPro2GO mappings is partially justified** to avoid over-annotation but is overly conservative regarding conserved molecular functions.

**Key findings:**
1. **Conserved biochemistry**: F-BAR domains universally bind acidic phospholipids via conserved basic residues and sense/induce membrane curvature.
2. **Functional divergence**: Subfamilies perform non-overlapping roles—endocytosis (FCHO, CIP4, PACSIN), filopodium formation (srGAP, TOCA-1), signaling (FES/FER), cytokinesis (fungal Cdc15), etc.
3. **Taxonomic breadth**: Eukaryote-wide (except plants) across 7,646 taxa, but many functions are metazoan- or tissue-specific.
4. **No pseudo-enzymes**: F-BAR is a scaffold, not enzymatic; autoinhibition exists but is regulatory, not loss-of-function.

**Recommended actions:**
- Add GO:0005543 (phospholipid binding) and GO:0044877 (protein-containing complex binding) as conserved molecular functions at the family level.
- Do not add biological process or cellular component terms to PTHR23065; reserve these for subfamily-level or gene-level annotation.
- Flag for GO Consortium consideration: need for a precise "membrane curvature sensing" molecular function term.

This report provides a comprehensive, evidence-based framework for InterPro2GO curation decisions regarding PTHR23065.

References

1. (wang2009molecularmechanismof pages 1-2): Qi Wang, Marcos V. A. S. Navarro, Gary Peng, Evan Molinelli, Shih Lin Goh, Bret L. Judson, Kanagalaghatta R. Rajashankar, and Holger Sondermann. Molecular mechanism of membrane constriction and tubulation mediated by the f-bar protein pacsin/syndapin. Proceedings of the National Academy of Sciences, 106:12700-12705, Aug 2009. URL: https://doi.org/10.1073/pnas.0902974106, doi:10.1073/pnas.0902974106. This article has 245 citations and is from a highest quality peer-reviewed journal.

2. (rao2011membraneshapingby pages 1-3): Yijian Rao and Volker Haucke. Membrane shaping by the bin/amphiphysin/rvs (bar) domain protein superfamily. Cellular and Molecular Life Sciences, 68:3983-3993, Jul 2011. URL: https://doi.org/10.1007/s00018-011-0768-5, doi:10.1007/s00018-011-0768-5. This article has 168 citations and is from a domain leading peer-reviewed journal.

3. (ahmed2010fbardomainproteins pages 1-2): Sohail Ahmed, Wenyu Bu, Raphael Tze Chuen Lee, Sebastian Maurer-Stroh, and Wah Ing Goh. F-bar domain proteins. Communicative & Integrative Biology, 3:116-121, Mar 2010. URL: https://doi.org/10.4161/cib.3.2.10808, doi:10.4161/cib.3.2.10808. This article has 57 citations and is from a peer-reviewed journal.

4. (safari2012thebardomain pages 7-10): Fatemeh Safari and Shiro Suetsugu. The bar domain superfamily proteins from subcellular structures to human diseases. Membranes, 2:91-117, Feb 2012. URL: https://doi.org/10.3390/membranes2010091, doi:10.3390/membranes2010091. This article has 63 citations.

5. (stanishnevakonovalova2016theroleof pages 1-2): T. B. Stanishneva-Konovalova, N. I Derkacheva, S. V. Polevova, and O. S. Sokolova. The role of bar domain proteins in the regulation of membrane dynamics. Acta Naturae, 8:60-69, Dec 2016. URL: https://doi.org/10.32607/20758251-2016-8-4-60-69, doi:10.32607/20758251-2016-8-4-60-69. This article has 63 citations and is from a peer-reviewed journal.

6. (rao2010molecularbasisfor pages 1-2): Yijian Rao, Qingjun Ma, Ardeschir Vahedi-Faridi, Anna Sundborger, Arndt Pechstein, Dmytro Puchkov, Lin Luo, Oleg Shupliakov, Wolfram Saenger, and Volker Haucke. Molecular basis for sh3 domain regulation of f-bar–mediated membrane deformation. Proceedings of the National Academy of Sciences, 107:8213-8218, Apr 2010. URL: https://doi.org/10.1073/pnas.1003478107, doi:10.1073/pnas.1003478107. This article has 193 citations and is from a highest quality peer-reviewed journal.

7. (safari2012thebardomain pages 1-5): Fatemeh Safari and Shiro Suetsugu. The bar domain superfamily proteins from subcellular structures to human diseases. Membranes, 2:91-117, Feb 2012. URL: https://doi.org/10.3390/membranes2010091, doi:10.3390/membranes2010091. This article has 63 citations.

8. (carman2018bardomainproteins—a pages 1-2): Peter J. Carman and Roberto Dominguez. Bar domain proteins—a linkage between cellular membranes, signaling pathways, and the actin cytoskeleton. Biophysical Reviews, 10:1587-1604, Nov 2018. URL: https://doi.org/10.1007/s12551-018-0467-7, doi:10.1007/s12551-018-0467-7. This article has 192 citations and is from a peer-reviewed journal.

9. (liu2015fbarfamilyproteins pages 2-4): Suxuan Liu, Xinyu Xiong, Xianxian Zhao, Xiaofeng Yang, and Hong Wang. F-bar family proteins, emerging regulators for cell membrane dynamic changes—from structure to human diseases. Journal of Hematology & Oncology, May 2015. URL: https://doi.org/10.1186/s13045-015-0144-2, doi:10.1186/s13045-015-0144-2. This article has 109 citations and is from a domain leading peer-reviewed journal.

10. (safari2012thebardomain pages 5-7): Fatemeh Safari and Shiro Suetsugu. The bar domain superfamily proteins from subcellular structures to human diseases. Membranes, 2:91-117, Feb 2012. URL: https://doi.org/10.3390/membranes2010091, doi:10.3390/membranes2010091. This article has 63 citations.

11. (liu2015fbarfamilyproteins pages 1-2): Suxuan Liu, Xinyu Xiong, Xianxian Zhao, Xiaofeng Yang, and Hong Wang. F-bar family proteins, emerging regulators for cell membrane dynamic changes—from structure to human diseases. Journal of Hematology & Oncology, May 2015. URL: https://doi.org/10.1186/s13045-015-0144-2, doi:10.1186/s13045-015-0144-2. This article has 109 citations and is from a domain leading peer-reviewed journal.

12. (ahmed2010fbardomainproteins pages 2-4): Sohail Ahmed, Wenyu Bu, Raphael Tze Chuen Lee, Sebastian Maurer-Stroh, and Wah Ing Goh. F-bar domain proteins. Communicative & Integrative Biology, 3:116-121, Mar 2010. URL: https://doi.org/10.4161/cib.3.2.10808, doi:10.4161/cib.3.2.10808. This article has 57 citations and is from a peer-reviewed journal.

13. (liu2015fbarfamilyproteins pages 5-6): Suxuan Liu, Xinyu Xiong, Xianxian Zhao, Xiaofeng Yang, and Hong Wang. F-bar family proteins, emerging regulators for cell membrane dynamic changes—from structure to human diseases. Journal of Hematology & Oncology, May 2015. URL: https://doi.org/10.1186/s13045-015-0144-2, doi:10.1186/s13045-015-0144-2. This article has 109 citations and is from a domain leading peer-reviewed journal.

14. (liu2015fbarfamilyproteins pages 6-7): Suxuan Liu, Xinyu Xiong, Xianxian Zhao, Xiaofeng Yang, and Hong Wang. F-bar family proteins, emerging regulators for cell membrane dynamic changes—from structure to human diseases. Journal of Hematology & Oncology, May 2015. URL: https://doi.org/10.1186/s13045-015-0144-2, doi:10.1186/s13045-015-0144-2. This article has 109 citations and is from a domain leading peer-reviewed journal.

15. (liu2015fbarfamilyproteins pages 4-5): Suxuan Liu, Xinyu Xiong, Xianxian Zhao, Xiaofeng Yang, and Hong Wang. F-bar family proteins, emerging regulators for cell membrane dynamic changes—from structure to human diseases. Journal of Hematology & Oncology, May 2015. URL: https://doi.org/10.1186/s13045-015-0144-2, doi:10.1186/s13045-015-0144-2. This article has 109 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](PTHR23065-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](PTHR23065-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. rao2010molecularbasisfor pages 1-2
2. liu2015fbarfamilyproteins pages 5-6
3. safari2012thebardomain pages 1-5
4. wang2009molecularmechanismof pages 1-2
5. rao2011membraneshapingby pages 1-3
6. ahmed2010fbardomainproteins pages 1-2
7. safari2012thebardomain pages 7-10
8. stanishnevakonovalova2016theroleof pages 1-2
9. liu2015fbarfamilyproteins pages 2-4
10. safari2012thebardomain pages 5-7
11. liu2015fbarfamilyproteins pages 1-2
12. ahmed2010fbardomainproteins pages 2-4
13. liu2015fbarfamilyproteins pages 6-7
14. liu2015fbarfamilyproteins pages 4-5
15. PI(4,5)P2
16. https://doi.org/10.1073/pnas.0902974106,
17. https://doi.org/10.1007/s00018-011-0768-5,
18. https://doi.org/10.4161/cib.3.2.10808,
19. https://doi.org/10.3390/membranes2010091,
20. https://doi.org/10.32607/20758251-2016-8-4-60-69,
21. https://doi.org/10.1073/pnas.1003478107,
22. https://doi.org/10.1007/s12551-018-0467-7,
23. https://doi.org/10.1186/s13045-015-0144-2,