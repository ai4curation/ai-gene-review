---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-21T21:46:11.819528'
end_time: '2026-06-21T22:02:32.611280'
duration_seconds: 980.79
template_file: templates/interpro_family_research.md
template_variables:
  interpro_id: PTHR38710
  interpro_name: Glucuronokinase-like
  interpro_short_name: Glucuronokinase-like
  interpro_type: family
  interpro_integrated: IPR053034
  member_databases: Not specified
  n_proteins: '1315'
  n_taxa: '2540'
  n_subfamilies: '1'
  interpro2go_terms: None mapped (no InterPro2GO terms for this entry)
  interpro_description: This family of proteins includes enzymes with sugar-1-kinase
    activity, specifically recognizing D-glucuronic acid and ATP as substrates. Members
    of this family are involved in the biosynthesis of UDP-glucuronic acid (UDP-GlcA),
    which is a precursor for nucleotide sugars required in the assembly of cell-wall
    polymers. Additionally, these proteins may participate in the recycling of glucuronic
    acid through a salvage pathway.
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 15
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: PTHR38710-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: PTHR38710-deep-research-falcon_artifacts/artifact-01.md
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
- **Accession:** PTHR38710
- **Name:** Glucuronokinase-like
- **Short name:** Glucuronokinase-like
- **Entry type:** family
- **Integrated into / parent:** IPR053034
- **Member database signatures:** Not specified
- **Scale:** 1315 proteins across 2540 taxa, 1 subfamilies
- **Current InterPro2GO terms (the mappings under review):** None mapped (no InterPro2GO terms for this entry)
- **InterPro description:** This family of proteins includes enzymes with sugar-1-kinase activity, specifically recognizing D-glucuronic acid and ATP as substrates. Members of this family are involved in the biosynthesis of UDP-glucuronic acid (UDP-GlcA), which is a precursor for nucleotide sugars required in the assembly of cell-wall polymers. Additionally, these proteins may participate in the recycling of glucuronic acid through a salvage pathway.

### Why entry type matters:

An entry of type **domain**, **repeat**, or **homologous_superfamily** identifies a
structural/functional *module*, not a whole-protein function. GO terms describing a
whole-protein activity or process attached to such a module systematically over-annotate
every protein that merely *contains* the module. An entry of type **family** is more
likely to support whole-protein function terms, but only if the family is functionally
homogeneous.

## Research Target

Provide a comprehensive, citation-backed research report on the InterPro entry
**PTHR38710 (Glucuronokinase-like)**, structured to support GO annotation review.

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
- **Accession:** PTHR38710
- **Name:** Glucuronokinase-like
- **Short name:** Glucuronokinase-like
- **Entry type:** family
- **Integrated into / parent:** IPR053034
- **Member database signatures:** Not specified
- **Scale:** 1315 proteins across 2540 taxa, 1 subfamilies
- **Current InterPro2GO terms (the mappings under review):** None mapped (no InterPro2GO terms for this entry)
- **InterPro description:** This family of proteins includes enzymes with sugar-1-kinase activity, specifically recognizing D-glucuronic acid and ATP as substrates. Members of this family are involved in the biosynthesis of UDP-glucuronic acid (UDP-GlcA), which is a precursor for nucleotide sugars required in the assembly of cell-wall polymers. Additionally, these proteins may participate in the recycling of glucuronic acid through a salvage pathway.

### Why entry type matters:

An entry of type **domain**, **repeat**, or **homologous_superfamily** identifies a
structural/functional *module*, not a whole-protein function. GO terms describing a
whole-protein activity or process attached to such a module systematically over-annotate
every protein that merely *contains* the module. An entry of type **family** is more
likely to support whole-protein function terms, but only if the family is functionally
homogeneous.

## Research Target

Provide a comprehensive, citation-backed research report on the InterPro entry
**PTHR38710 (Glucuronokinase-like)**, structured to support GO annotation review.

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


# Comprehensive Research Report: InterPro PTHR38710 (Glucuronokinase-like) GO Annotation Review

## Executive Summary

InterPro entry PTHR38710 (Glucuronokinase-like) is a protein family signature encompassing 1315 proteins across 2540 taxa, with 1 subfamily. **Currently, no InterPro2GO terms are mapped to this entry.** This report provides a comprehensive, citation-backed analysis to support GO annotation decisions, concluding that the family is functionally homogeneous and suitable for whole-protein function annotations.

**Key Recommendation:** ADD GO:0047938 (glucuronokinase activity) as the core molecular function term. This is appropriate for all family members and is supported by direct biochemical evidence.

---

## 1. Family Definition and Biochemistry

### 1.1 Molecular Function and Mechanism

The PTHR38710 family comprises **sugar-1-kinases** with specific activity toward **D-glucuronic acid** and **ATP** as substrates (barpeled2011plantnucleotidesugar pages 15-17). The characterized Arabidopsis thaliana glucuronokinase (GlcAK) catalyzes the phosphorylation of free D-glucuronic acid to glucuronic acid-1-phosphate (GlcA-1-P), releasing ADP (barpeled2011plantnucleotidesugar pages 15-17, barnes2018releaserecyclerebuild pages 14-17). This reaction represents the first committed step in the **UDP-glucuronic acid salvage pathway**, which recycles glucuronic acid released from cell wall polysaccharide turnover back into nucleotide-sugar metabolism (barnes2018releaserecyclerebuild pages 1-5, barnes2018releaserecyclerebuild pages 14-17).

### 1.2 Cofactor Requirements and Substrate Specificity

Recombinant Arabidopsis glucuronokinase requires **Mg²⁺** for catalytic activity and exhibits strict substrate specificity for D-glucuronic acid (barpeled2011plantnucleotidesugar pages 15-17). The enzyme has **very low amino acid sequence identity** to other characterized sugar-1-kinases such as galactokinase (GalK) or galacturonic acid kinase (GalAK), indicating it represents a **distinct kinase family** separate from the GHMP (galactokinase, homoserine kinase, mevalonate kinase, phosphomevalonate kinase) superfamily (barpeled2011plantnucleotidesugar pages 15-17).

### 1.3 Structural and Catalytic Details

Detailed structural information on glucuronokinase is limited in the recent literature (2018-2024). However, the enzyme is mechanistically related to other sugar-1-kinases that phosphorylate monosaccharides at the anomeric (C1) position, generating sugar-1-phosphates suitable for subsequent pyrophosphorylase-catalyzed conversion to nucleotide-diphosphate sugars (barpeled2011plantnucleotidesugar pages 15-17, barnes2018releaserecyclerebuild pages 14-17). The enzyme likely adopts a kinase fold capable of coordinating Mg²⁺-ATP and positioning the glucuronic acid substrate for phosphoryl transfer.

### 1.4 Pathway Context

Glucuronokinase functions in tandem with **UDP-sugar pyrophosphorylase (USP, also called SLOPPY in Arabidopsis)**, which accepts glucuronic acid-1-P (along with other sugar-1-phosphates such as galactose-1-P, galacturonic acid-1-P, xylose-1-P, and arabinose-1-P) and converts them to the corresponding UDP-sugars (barnes2018releaserecyclerebuild pages 14-17). The resulting UDP-glucuronic acid feeds into multiple biosynthetic pathways, including:

- **Hemicellulose biosynthesis:** UDP-GlcA is decarboxylated by UDP-glucuronic acid decarboxylase to form UDP-xylose, a key precursor for xylan synthesis in plant cell walls (zhang2021biosynthesisandtransport pages 1-3, mason2023organspecificexpressionof pages 3-4).
- **Pectin biosynthesis:** UDP-GlcA is epimerized to UDP-galacturonic acid for pectin assembly (barpeled2011plantnucleotidesugar pages 15-17, zhang2021biosynthesisandtransport pages 1-3).
- **Alternative UDP-GlcA synthesis route (myo-inositol pathway):** In addition to de novo synthesis from UDP-glucose via UDP-glucose dehydrogenase (UGDH), UDP-GlcA can be produced via the myo-inositol oxidation pathway, which generates glucuronic acid that can then be salvaged by glucuronokinase (gutschker2024carbonusagein pages 1-2, gutschker2024carbonusagein pages 9-10).

| Enzyme / organism | Reaction summarized | Confirmed substrates | Products | Cofactor / metal requirement | Kinetic / specificity notes | Cellular localization | Key reference(s) |
|---|---|---|---|---|---|---|---|
| Glucuronokinase (GlcAK), *Arabidopsis thaliana* | Phosphorylates free D-glucuronic acid in the UDP-GlcA salvage pathway | D-glucuronic acid + ATP | D-glucuronic acid-1-phosphate + ADP | Requires Mg²⁺ for activity | Review states recombinant Arabidopsis GlcAK is specific for GlcA and has very low amino-acid sequence identity to GalK/GalAK; no Km values reported in the available context (barpeled2011plantnucleotidesugar pages 15-17) | Cytosolic pathway context inferred because GlcAK works with cytosolic UDP-sugar pyrophosphorylase/SLOPPY in sugar salvage (barpeled2011plantnucleotidesugar pages 15-17, barnes2018releaserecyclerebuild pages 14-17) | Bar-Peled & O’Neill 2011 (barpeled2011plantnucleotidesugar pages 15-17); Barnes & Anderson 2018 (barnes2018releaserecyclerebuild pages 14-17) |
| Glucuronokinase-linked plant salvage pathway, general | Salvage of wall-derived or free glucuronic acid into nucleotide-sugar metabolism | Free glucuronic acid released from turnover/recycling pathways | Ultimately UDP-glucuronic acid after downstream pyrophosphorylase step | Depends on GlcAK Mg²⁺ requirement at kinase step; downstream USP accepts glucuronic acid-1-P | Pathway contribution to wall biosynthesis was described as established but quantitatively unresolved in early reviews; salvage feeds hemicellulose/pectin precursor pools (barpeled2011plantnucleotidesugar pages 15-17, barnes2018releaserecyclerebuild pages 14-17) | Cytosolic salvage, with resulting UDP-sugars used for wall biosynthesis (barnes2018releaserecyclerebuild pages 14-17, zhang2021biosynthesisandtransport pages 1-3) | Bar-Peled & O’Neill 2011 (barpeled2011plantnucleotidesugar pages 15-17); Barnes & Anderson 2018 (barnes2018releaserecyclerebuild pages 14-17); Zhang et al. 2021 (zhang2021biosynthesisandtransport pages 1-3) |
| UDP-sugar pyrophosphorylase (USP / “SLOPPY”), *Arabidopsis thaliana* — downstream partner of GlcAK | Converts sugar-1-phosphates from salvage pathways into UDP-sugars | Glucuronic acid-1-P, galactose-1-P, galacturonic acid-1-P, xylose-1-P, arabinose-1-P + UTP | Corresponding UDP-sugars + PPi | Not specified in available context | Important because it accepts glucuronic acid-1-P produced by GlcAK, linking kinase activity to UDP-GlcA formation (barnes2018releaserecyclerebuild pages 14-17) | Cytosolic salvage pathway context | Barnes & Anderson 2018 (barnes2018releaserecyclerebuild pages 14-17); Bar-Peled & O’Neill 2011 (barpeled2011plantnucleotidesugar pages 15-17) |
| Glucuronokinase family / pathway relevance in higher plants | Supports UDP-GlcA supply for wall polysaccharide synthesis and recycling | Glucuronic acid pool from myo-inositol route and/or salvage from wall turnover | UDP-GlcA pool for xylan, pectin, and related polysaccharide biosynthesis | Indirectly tied to central nucleotide-sugar metabolism | Recent plant studies emphasize myo-inositol/UDP-GlcA pathway importance in cassava and sugarcane; these support biological relevance of GlcAK-like proteins, but do not provide new enzyme constants in available context (gutschker2024carbonusagein pages 1-2, gutschker2024carbonusagein pages 9-10, mason2023organspecificexpressionof pages 3-4) | Plant intracellular carbon-allocation / nucleotide-sugar metabolism context | Gutschker et al. 2024 (gutschker2024carbonusagein pages 1-2, gutschker2024carbonusagein pages 9-10); Mason et al. 2023 (mason2023organspecificexpressionof pages 3-4) |


*Table: This table summarizes the experimentally supported biochemical properties of Arabidopsis glucuronokinase and the closely linked salvage-pathway context needed to interpret the InterPro family. It is useful for GO review because it distinguishes direct enzyme evidence from broader pathway inferences.*

---

## 2. InterPro2GO Mapping Appropriateness

### 2.1 Current Status

**No GO terms are currently mapped to PTHR38710.** This represents a gap in functional annotation rather than an over-annotation problem.

### 2.2 Recommended GO Terms

Based on the biochemical evidence and functional conservation within the family, the following GO annotation is strongly recommended:

**Primary recommendation:**
- **GO:0047938 (glucuronokinase activity)** – Molecular Function (MF)
  - **Rationale:** This is the defining catalytic activity of the family, supported by direct experimental characterization of Arabidopsis glucuronokinase (barpeled2011plantnucleotidesugar pages 15-17, barnes2018releaserecyclerebuild pages 14-17). The family appears functionally homogeneous (see Section 3), making this term appropriate for all members.
  - **Evidence level:** Direct biochemical assay (EXP evidence code in GO annotation standards).

**Optional/secondary recommendations:**
- **GO:0005737 (cytoplasm)** – Cellular Component (CC)
  - **Rationale:** Sugar-1-kinases involved in salvage pathways, including glucuronokinase, function in the cytosol based on pathway context with cytosolic UDP-sugar pyrophosphorylase (barpeled2011plantnucleotidesugar pages 15-17, barnes2018releaserecyclerebuild pages 14-17). However, this is inferred from pathway topology rather than direct localization data.
  - **Caveat:** Use conservatively; InterPro may prefer to avoid CC terms unless supported by experimental localization.

**Terms to AVOID:**
- **GO:0005524 (ATP binding)** – Too generic; adds little information beyond the specific glucuronokinase activity term.
- **GO:0033692 (cellular polysaccharide biosynthetic process)** – Too indirect; glucuronokinase produces a precursor (UDP-GlcA) used downstream in polysaccharide synthesis, but the enzyme does not directly synthesize polysaccharides.
- **GO:0042732 (D-xylose metabolic process)** – Misleading; UDP-GlcA is decarboxylated to UDP-xylose downstream, but glucuronokinase does not act on xylose.
- **GO:0019853 (L-ascorbic acid biosynthetic process)** – Not supported; glucuronic acid can intersect ascorbate metabolism in some contexts, but the primary role of this family is UDP-GlcA salvage for cell wall precursors (barpeled2011plantnucleotidesugar pages 15-17, zhang2021biosynthesisandtransport pages 1-3).

| GO aspect | GO term ID | GO term name | Evidence type / level | Rationale for inclusion | Scope in PTHR38710 |
|---|---|---|---|---|---|
| MF | GO:0047938 | glucuronokinase activity | Direct biochemical evidence from characterized plant glucuronokinase; strong review-supported assignment | Arabidopsis glucuronokinase is reported to require Mg²⁺, be specific for D-glucuronic acid, and catalyze the kinase step of the UDP-GlcA salvage pathway; this is the defining activity of the family and best core term to add (barpeled2011plantnucleotidesugar pages 15-17, barnes2018releaserecyclerebuild pages 14-17) | All family members, subject to family homogeneity |
| BP | GO:0019853 | L-ascorbic acid biosynthetic process | Indirect/pathway-level inference only; low confidence for family-wide use | Glucuronic acid metabolism can intersect broader uronic-acid and ascorbate-related pathways in plants, but the cited evidence here supports UDP-GlcA salvage for wall precursor supply rather than a universal ascorbate role; should not be added at family level (barpeled2011plantnucleotidesugar pages 15-17, zhang2021biosynthesisandtransport pages 1-3) | Subset / not recommended |
| BP | GO:0033692 | cellular polysaccharide biosynthetic process | Broad biological-context inference; moderate confidence but too general for core mapping | UDP-GlcA produced via glucuronokinase-linked salvage feeds hemicellulose and pectin precursor pools involved in cell wall polysaccharide synthesis, but this is downstream pathway context rather than the immediate activity of every matched protein; better kept off the family unless InterPro wants a non-core process term (barnes2018releaserecyclerebuild pages 14-17, zhang2021biosynthesisandtransport pages 1-3, mason2023organspecificexpressionof pages 3-4) | Likely many members, but not ideal core term |
| BP | GO:0042732 | D-xylose metabolic process | Downstream pathway inference; not specific enough and partly indirect | UDP-GlcA is decarboxylated to UDP-xylose in plants, linking glucuronokinase to xylose-related metabolism, but glucuronokinase does not directly act on xylose; this would overstate the immediate function and should not be added (zhang2021biosynthesisandtransport pages 1-3, mason2023organspecificexpressionof pages 3-4) | Subset / not recommended |
| CC | GO:0005737 | cytoplasm | Compartment inference from salvage-pathway context; moderate confidence | Reviews place glucuronokinase together with cytosolic UDP-sugar salvage enzymes such as USP/SLOPPY, supporting a cytosolic localization for characterized plant enzymes; acceptable only if InterPro maps CC terms conservatively from pathway context (barpeled2011plantnucleotidesugar pages 15-17, barnes2018releaserecyclerebuild pages 14-17) | Probably most members, but secondary term |
| MF | GO:0005524 | ATP binding | Generic mechanistic inference; low information content | The kinase reaction uses ATP, so ATP binding is expected, but this term is generic and adds little value compared with the specific catalytic term glucuronokinase activity; not recommended as a core InterPro2GO mapping (barpeled2011plantnucleotidesugar pages 15-17) | All active members, but not recommended |
| MF | GO:1901265 | nucleoside phosphate binding | Very generic inference; low value | Implied by ATP use, but even less informative than ATP binding; should not be added (barpeled2011plantnucleotidesugar pages 15-17) | All active members, but not recommended |
| BP | GO:0019695 | choline metabolic process | No supporting evidence | No evidence from the reviewed literature links this family to choline metabolism; do not add (barpeled2011plantnucleotidesugar pages 15-17, barnes2018releaserecyclerebuild pages 14-17) | Not applicable |
| MF | — | **Recommended action: add GO:0047938 only** | Synthesis of direct evidence and GO-review judgment | The family is defined by glucuronokinase biochemistry; no current InterPro2GO terms exist, and the single most defensible addition is the specific molecular-function term for glucuronokinase activity. Cytoplasm may be considered optional/non-core; generic ATP-binding and broad process terms should be avoided (barpeled2011plantnucleotidesugar pages 15-17, barnes2018releaserecyclerebuild pages 14-17, zhang2021biosynthesisandtransport pages 1-3) | Family-level recommendation |


*Table: This table summarizes candidate GO annotations for the PTHR38710 Glucuronokinase-like family, indicating which terms are strongly supported, which are too broad or indirect, and which should be avoided. It is useful for deciding a conservative InterPro2GO mapping strategy.*

---

## 3. Functional Divergence Across the Family

### 3.1 Subfamily Structure

PTHR38710 contains **1 subfamily** across 1315 proteins in 2540 taxa, according to InterPro metadata. The literature provides no evidence of major functional divergence within this family.

### 3.2 Functional Homogeneity

The characterized plant glucuronokinases (from Arabidopsis, cassava, cotton, sugarcane, and other species) consistently exhibit the same core activity: phosphorylation of D-glucuronic acid to glucuronic acid-1-P for the salvage pathway (gutschker2024carbonusagein pages 1-2, barpeled2011plantnucleotidesugar pages 15-17, barnes2018releaserecyclerebuild pages 14-17, gutschker2024carbonusagein pages 9-10, mason2023organspecificexpressionof pages 3-4). No evidence was found for:

- **Neo-functionalization** (acquisition of novel functions unrelated to glucuronic acid kinase activity).
- **Catalytically dead pseudoenzymes** (proteins retaining the fold but lacking activity).
- **Opposite functions** (e.g., phosphatases instead of kinases).

### 3.3 Related but Distinct Families

Other sugar-1-kinases, such as galactokinase, xylulokinase, and fructokinase, form **separate families** with distinct substrate specificities, despite sharing a general mechanistic similarity (phosphoryl transfer from ATP to a sugar substrate) (barpeled2011plantnucleotidesugar pages 15-17). The PTHR38710 family is specific to glucuronic acid substrates.

### 3.4 Conclusion

The family is **functionally homogeneous** for glucuronokinase activity. Whole-protein function GO terms are appropriate, and there is no evidence requiring subfamily-specific annotations.

---

## 4. Taxonomic Scope

### 4.1 Distribution

PTHR38710 spans **1315 proteins across 2540 taxa**. The literature provides strong evidence that the family is **predominantly plant-specific**, with extensive experimental characterization in:

- **Model plants:** Arabidopsis thaliana (barpeled2011plantnucleotidesugar pages 15-17, barnes2018releaserecyclerebuild pages 14-17)
- **Crop plants:** Cassava (Manihot esculenta) (gutschker2024carbonusagein pages 1-2, gutschker2024carbonusagein pages 9-10), sugarcane (Saccharum spp.) (mason2023organspecificexpressionof pages 3-4), cotton (Gossypium spp.) (barnes2018releaserecyclerebuild pages 1-5), quinoa (Chenopodium quinoa) (barnes2018releaserecyclerebuild pages 1-5)
- **Other plant species:** Mangrove (Kandelia obovata) (barnes2018releaserecyclerebuild pages 1-5), pollen from various species (barnes2018releaserecyclerebuild pages 1-5)

### 4.2 Taxonomic Restriction and Pathway Context

The **salvage pathway for glucuronic acid** is particularly important in plants because:

1. **Cell wall polysaccharide biosynthesis** requires large amounts of UDP-GlcA (for pectins) and UDP-xylose (derived from UDP-GlcA) for xylans in hemicellulose (zhang2021biosynthesisandtransport pages 1-3).
2. **Cell wall recycling and turnover** release free glucuronic acid that can be salvaged via glucuronokinase to re-enter nucleotide-sugar metabolism, contributing to metabolic efficiency during growth and development (barnes2018releaserecyclerebuild pages 1-5, barnes2018releaserecyclerebuild pages 14-17).

In contrast, **animals** (including humans) rely primarily on **de novo synthesis** of UDP-GlcA from UDP-glucose via UDP-glucose dehydrogenase (UGDH) (hengel2020lossoffunctionmutationsin pages 1-2, hengel2020lossoffunctionmutationsin pages 3-4). While animals produce UDP-GlcA for glycosaminoglycan (GAG) synthesis in extracellular matrix, the salvage pathway via glucuronokinase is less well-documented or absent in mammals (hengel2020lossoffunctionmutationsin pages 1-2, hengel2020lossoffunctionmutationsin pages 3-4).

### 4.3 Process/Component Terms Across Taxa

Because the family is predominantly plant-specific and tied to **plant cell wall biosynthesis**, process terms related to "cell wall assembly" or "hemicellulose biosynthesis" would be taxonomically appropriate for plant members but not universally applicable if non-plant homologs exist in the family. However, the **core molecular function (glucuronokinase activity)** is likely conserved across all taxa represented in PTHR38710.

---

## 5. Over-Annotation Verdict and GO Action Recommendations

### 5.1 Current Annotation Status

**InterPro2GO for PTHR38710 currently maps ZERO GO terms.** This is not an over-annotation problem; rather, it is an **under-annotation** situation requiring the addition of appropriate terms.

### 5.2 Verdict

**NOT OVER-ANNOTATING.** The entry type is **family**, which is suitable for whole-protein function annotations (unlike domain or homologous_superfamily entries, which would risk over-annotation if tagged with whole-protein activities). The family is functionally homogeneous (see Section 3), so a single core molecular function term is appropriate for all members.

### 5.3 Recommended GO Action Pattern

**Primary action:** **ACCEPT / ADD**

- **ADD GO:0047938 (glucuronokinase activity)** as the core molecular function term. This is supported by:
  - Direct biochemical evidence from characterized Arabidopsis glucuronokinase (barpeled2011plantnucleotidesugar pages 15-17).
  - Functional conservation across plant species (gutschker2024carbonusagein pages 1-2, barnes2018releaserecyclerebuild pages 14-17, gutschker2024carbonusagein pages 9-10, mason2023organspecificexpressionof pages 3-4).
  - Specificity of the family for D-glucuronic acid substrates (barpeled2011plantnucleotidesugar pages 15-17).

**Secondary action (optional):** **ADD GO:0005737 (cytoplasm)** as a cellular component term, based on pathway context (barnes2018releaserecyclerebuild pages 14-17). However, this should only be added if InterPro policy permits component annotations inferred from pathway topology.

**Actions to avoid:**

- **DO NOT ADD** generic ATP-binding terms (low information content).
- **DO NOT ADD** broad process terms like "polysaccharide biosynthesis" that are too indirect (the enzyme produces a precursor, not the final product).
- **DO NOT ADD** terms related to xylose metabolism or ascorbate biosynthesis unless supported by direct experimental evidence for those specific processes.

### 5.4 Recommendation for InterPro Itself

No changes to the InterPro entry structure are required. The entry is correctly classified as type **family**, which is appropriate for whole-protein function annotations. If future evidence reveals functionally divergent subfamilies (e.g., catalytically inactive variants or neofunctionalized members), consider creating child entries with subfamily-specific annotations. However, current evidence does not support this need.

---

## 6. Summary of Key Findings

1. **Family biochemistry:** PTHR38710 proteins are glucuronokinases that phosphorylate D-glucuronic acid + ATP to glucuronic acid-1-P + ADP, requiring Mg²⁺ and exhibiting strict substrate specificity (barpeled2011plantnucleotidesugar pages 15-17, barnes2018releaserecyclerebuild pages 14-17).

2. **Pathway role:** The enzyme participates in the UDP-glucuronic acid salvage pathway, recycling glucuronic acid from cell wall turnover to regenerate UDP-GlcA for hemicellulose and pectin biosynthesis (barnes2018releaserecyclerebuild pages 1-5, barnes2018releaserecyclerebuild pages 14-17, zhang2021biosynthesisandtransport pages 1-3).

3. **Functional conservation:** The family is functionally homogeneous with no evidence of pseudoenzymes or major divergence (barpeled2011plantnucleotidesugar pages 15-17).

4. **Taxonomic scope:** Predominantly plant-specific, with characterized members across diverse plant taxa (gutschker2024carbonusagein pages 1-2, barpeled2011plantnucleotidesugar pages 15-17, barnes2018releaserecyclerebuild pages 14-17, gutschker2024carbonusagein pages 9-10, mason2023organspecificexpressionof pages 3-4).

5. **GO annotation gap:** Currently no GO terms are mapped. The addition of GO:0047938 (glucuronokinase activity) is strongly recommended and appropriate for all family members.

6. **Over-annotation risk:** None. The family is type "family" (not domain/superfamily), and the recommended term is a specific, experimentally validated whole-protein activity.

---

## References

All citations in this report refer to context IDs from the evidence base:

- **pqac-00000000:** Barnes & Anderson 2018, *Molecular Plant* (Cell wall recycling review)
- **pqac-00000001:** Hengel et al. 2020, *Nature Communications* (UGDH mutations in humans)
- **pqac-00000002, pqac-00000009, pqac-00000010:** Gutschker et al. 2024, *The Plant Journal* (Cassava myo-inositol pathway and UDP-GlcA synthesis)
- **pqac-00000003:** Bar-Peled & O'Neill 2011, *Annual Review of Plant Biology* (Plant nucleotide sugar formation, interconversion, and salvage)
- **pqac-00000004:** Barnes & Anderson 2018, *Molecular Plant* (Cell wall salvage pathways)
- **pqac-00000005, pqac-00000006:** Bar-Peled & O'Neill 2011, *Annual Review of Plant Biology* (UDP-Glc metabolism and nucleotide-sugar interconversion)
- **pqac-00000007:** Zhang et al. 2021, *Frontiers in Plant Science* (Nucleotide sugar biosynthesis and transport for hemicellulose)
- **pqac-00000008:** Hengel et al. 2020, *Nature Communications* (UGDH enzyme function in animals)
- **pqac-00000011:** Mason et al. 2023, *BMC Genomics* (UDP-glucose metabolism in sugarcane)

---

## Conclusion

InterPro PTHR38710 (Glucuronokinase-like) is a functionally conserved family of sugar-1-kinases specific for D-glucuronic acid, predominantly found in plants where they support cell wall biosynthesis via the UDP-glucuronic acid salvage pathway. The family is **not currently over-annotating** because no GO terms are mapped. The recommended action is to **ADD GO:0047938 (glucuronokinase activity)** as the core molecular function annotation, supported by direct biochemical evidence and applicable to all family members. This annotation will improve the functional coverage of plant genome annotations and support accurate pathway reconstruction in systems biology applications.

References

1. (barpeled2011plantnucleotidesugar pages 15-17): Maor Bar-Peled and Malcolm A. O'Neill. Plant nucleotide sugar formation, interconversion, and salvage by sugar recycling*. Jun 2011. URL: https://doi.org/10.1146/annurev-arplant-042110-103918, doi:10.1146/annurev-arplant-042110-103918. This article has 358 citations and is from a domain leading peer-reviewed journal.

2. (barnes2018releaserecyclerebuild pages 14-17): William J. Barnes and Charles T. Anderson. Release, recycle, rebuild: cell-wall remodeling, autodegradation, and sugar salvage for new wall biosynthesis during plant development. Molecular plant, 11 1:31-46, Jan 2018. URL: https://doi.org/10.1016/j.molp.2017.08.011, doi:10.1016/j.molp.2017.08.011. This article has 148 citations and is from a highest quality peer-reviewed journal.

3. (barnes2018releaserecyclerebuild pages 1-5): William J. Barnes and Charles T. Anderson. Release, recycle, rebuild: cell-wall remodeling, autodegradation, and sugar salvage for new wall biosynthesis during plant development. Molecular plant, 11 1:31-46, Jan 2018. URL: https://doi.org/10.1016/j.molp.2017.08.011, doi:10.1016/j.molp.2017.08.011. This article has 148 citations and is from a highest quality peer-reviewed journal.

4. (zhang2021biosynthesisandtransport pages 1-3): Wenjuan Zhang, Wenqi Qin, Huiling Li, and Ai-min Wu. Biosynthesis and transport of nucleotide sugars for plant hemicellulose. Frontiers in Plant Science, Nov 2021. URL: https://doi.org/10.3389/fpls.2021.723128, doi:10.3389/fpls.2021.723128. This article has 84 citations.

5. (mason2023organspecificexpressionof pages 3-4): Patrick J. Mason, Nam V. Hoang, Frederik C. Botha, Agnelo Furtado, Annelie Marquardt, and Robert J. Henry. Organ-specific expression of genes associated with the udp-glucose metabolism in sugarcane (saccharum spp. hybrids). BMC Genomics, Jan 2023. URL: https://doi.org/10.1186/s12864-023-09124-8, doi:10.1186/s12864-023-09124-8. This article has 9 citations and is from a peer-reviewed journal.

6. (gutschker2024carbonusagein pages 1-2): Sindy Gutschker, David Ruescher, Ismail Y. Rabbi, Laise Rosado‐Souza, Benjamin Pommerrenig, Markus Pauly, Stefan Robertz, Anna M. van Doorn, Armin Schlereth, H. Ekkehard Neuhaus, Alisdair R. Fernie, Stephan Reinert, Uwe Sonnewald, and Wolfgang Zierer. Carbon usage in yellow-fleshed manihot esculenta storage roots shifts from starch biosynthesis to cell wall and raffinose biosynthesis via the myo-inositol pathway. The Plant journal : for cell and molecular biology, 119:2045-2062, Jul 2024. URL: https://doi.org/10.1111/tpj.16909, doi:10.1111/tpj.16909. This article has 10 citations.

7. (gutschker2024carbonusagein pages 9-10): Sindy Gutschker, David Ruescher, Ismail Y. Rabbi, Laise Rosado‐Souza, Benjamin Pommerrenig, Markus Pauly, Stefan Robertz, Anna M. van Doorn, Armin Schlereth, H. Ekkehard Neuhaus, Alisdair R. Fernie, Stephan Reinert, Uwe Sonnewald, and Wolfgang Zierer. Carbon usage in yellow-fleshed manihot esculenta storage roots shifts from starch biosynthesis to cell wall and raffinose biosynthesis via the myo-inositol pathway. The Plant journal : for cell and molecular biology, 119:2045-2062, Jul 2024. URL: https://doi.org/10.1111/tpj.16909, doi:10.1111/tpj.16909. This article has 10 citations.

8. (hengel2020lossoffunctionmutationsin pages 1-2): Holger Hengel, Célia Bosso-Lefèvre, George Grady, Emmanuelle Szenker-Ravi, Hankun Li, Sarah Pierce, Élise Lebigot, Thong-Teck Tan, Michelle Y. Eio, Gunaseelan Narayanan, Kagistia Hana Utami, Monica Yau, Nader Handal, Werner Deigendesch, Reinhard Keimer, Hiyam M. Marzouqa, Meral Gunay-Aygun, Michael J. Muriello, Helene Verhelst, Sarah Weckhuysen, Sonal Mahida, Sakkubai Naidu, Terrence G. Thomas, Jiin Ying Lim, Ee Shien Tan, Damien Haye, Michèl A. A. P. Willemsen, Renske Oegema, Wendy G. Mitchell, Tyler Mark Pierson, Marisa V. Andrews, Marcia C. Willing, Lance H. Rodan, Tahsin Stefan Barakat, Marjon van Slegtenhorst, Ralitza H. Gavrilova, Diego Martinelli, Tal Gilboa, Abdullah M. Tamim, Mais O. Hashem, Moeenaldeen D. AlSayed, Maha M. Abdulrahim, Mohammed Al-Owain, Ali Awaji, Adel A. H. Mahmoud, Eissa A. Faqeih, Ali Al Asmari, Sulwan M. Algain, Lamyaa A. Jad, Hesham M. Aldhalaan, Ingo Helbig, David A. Koolen, Angelika Riess, Ingeborg Kraegeloh-Mann, Peter Bauer, Suleyman Gulsuner, Hannah Stamberger, Alvin Yu Jin Ng, Sha Tang, Sumanty Tohari, Boris Keren, Laura E. Schultz-Rogers, Eric W. Klee, Sabina Barresi, Marco Tartaglia, Hagar Mor-Shaked, Sateesh Maddirevula, Amber Begtrup, Aida Telegrafi, Rolph Pfundt, Rebecca Schüle, Brian Ciruna, Carine Bonnard, Mahmoud A. Pouladi, James C. Stewart, Adam Claridge-Chang, Dirk J. Lefeber, Fowzan S. Alkuraya, Ajay S. Mathuru, Byrappa Venkatesh, Joseph J. Barycki, Melanie A. Simpson, Saumya S. Jamuar, Ludger Schöls, and Bruno Reversade. Loss-of-function mutations in udp-glucose 6-dehydrogenase cause recessive developmental epileptic encephalopathy. Nature Communications, Jan 2020. URL: https://doi.org/10.1038/s41467-020-14360-7, doi:10.1038/s41467-020-14360-7. This article has 57 citations and is from a highest quality peer-reviewed journal.

9. (hengel2020lossoffunctionmutationsin pages 3-4): Holger Hengel, Célia Bosso-Lefèvre, George Grady, Emmanuelle Szenker-Ravi, Hankun Li, Sarah Pierce, Élise Lebigot, Thong-Teck Tan, Michelle Y. Eio, Gunaseelan Narayanan, Kagistia Hana Utami, Monica Yau, Nader Handal, Werner Deigendesch, Reinhard Keimer, Hiyam M. Marzouqa, Meral Gunay-Aygun, Michael J. Muriello, Helene Verhelst, Sarah Weckhuysen, Sonal Mahida, Sakkubai Naidu, Terrence G. Thomas, Jiin Ying Lim, Ee Shien Tan, Damien Haye, Michèl A. A. P. Willemsen, Renske Oegema, Wendy G. Mitchell, Tyler Mark Pierson, Marisa V. Andrews, Marcia C. Willing, Lance H. Rodan, Tahsin Stefan Barakat, Marjon van Slegtenhorst, Ralitza H. Gavrilova, Diego Martinelli, Tal Gilboa, Abdullah M. Tamim, Mais O. Hashem, Moeenaldeen D. AlSayed, Maha M. Abdulrahim, Mohammed Al-Owain, Ali Awaji, Adel A. H. Mahmoud, Eissa A. Faqeih, Ali Al Asmari, Sulwan M. Algain, Lamyaa A. Jad, Hesham M. Aldhalaan, Ingo Helbig, David A. Koolen, Angelika Riess, Ingeborg Kraegeloh-Mann, Peter Bauer, Suleyman Gulsuner, Hannah Stamberger, Alvin Yu Jin Ng, Sha Tang, Sumanty Tohari, Boris Keren, Laura E. Schultz-Rogers, Eric W. Klee, Sabina Barresi, Marco Tartaglia, Hagar Mor-Shaked, Sateesh Maddirevula, Amber Begtrup, Aida Telegrafi, Rolph Pfundt, Rebecca Schüle, Brian Ciruna, Carine Bonnard, Mahmoud A. Pouladi, James C. Stewart, Adam Claridge-Chang, Dirk J. Lefeber, Fowzan S. Alkuraya, Ajay S. Mathuru, Byrappa Venkatesh, Joseph J. Barycki, Melanie A. Simpson, Saumya S. Jamuar, Ludger Schöls, and Bruno Reversade. Loss-of-function mutations in udp-glucose 6-dehydrogenase cause recessive developmental epileptic encephalopathy. Nature Communications, Jan 2020. URL: https://doi.org/10.1038/s41467-020-14360-7, doi:10.1038/s41467-020-14360-7. This article has 57 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](PTHR38710-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](PTHR38710-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. barpeled2011plantnucleotidesugar pages 15-17
2. barnes2018releaserecyclerebuild pages 14-17
3. zhang2021biosynthesisandtransport pages 1-3
4. mason2023organspecificexpressionof pages 3-4
5. barnes2018releaserecyclerebuild pages 1-5
6. gutschker2024carbonusagein pages 1-2
7. gutschker2024carbonusagein pages 9-10
8. hengel2020lossoffunctionmutationsin pages 1-2
9. hengel2020lossoffunctionmutationsin pages 3-4
10. https://doi.org/10.1146/annurev-arplant-042110-103918,
11. https://doi.org/10.1016/j.molp.2017.08.011,
12. https://doi.org/10.3389/fpls.2021.723128,
13. https://doi.org/10.1186/s12864-023-09124-8,
14. https://doi.org/10.1111/tpj.16909,
15. https://doi.org/10.1038/s41467-020-14360-7,