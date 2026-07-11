---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-21T21:31:49.062498'
end_time: '2026-06-21T21:43:38.754535'
duration_seconds: 709.69
template_file: templates/interpro_family_research.md
template_variables:
  interpro_id: PTHR31458
  interpro_name: Polygalacturonase-associated BURP domain-containing protein
  interpro_short_name: PG-associated_BURP
  interpro_type: family
  interpro_integrated: IPR051897
  member_databases: Not specified
  n_proteins: '1738'
  n_taxa: '1244'
  n_subfamilies: '13'
  interpro2go_terms: None mapped (no InterPro2GO terms for this entry)
  interpro_description: This family of proteins includes non-catalytic subunits of
    polygalacturonase as well as proteins containing a BURP domain at the C-terminus.
    Members of this family are involved in the regulation of plant cell size and growth,
    with some acting as chaperones for other proteins through the secretory pathway.
    The BURP domain is unique to plant proteins and plays a critical role in the function
    of these proteins, although the exact mechanisms are not fully understood.
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 18
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: PTHR31458-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: PTHR31458-deep-research-falcon_artifacts/artifact-01.md
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
- **Accession:** PTHR31458
- **Name:** Polygalacturonase-associated BURP domain-containing protein
- **Short name:** PG-associated_BURP
- **Entry type:** family
- **Integrated into / parent:** IPR051897
- **Member database signatures:** Not specified
- **Scale:** 1738 proteins across 1244 taxa, 13 subfamilies
- **Current InterPro2GO terms (the mappings under review):** None mapped (no InterPro2GO terms for this entry)
- **InterPro description:** This family of proteins includes non-catalytic subunits of polygalacturonase as well as proteins containing a BURP domain at the C-terminus. Members of this family are involved in the regulation of plant cell size and growth, with some acting as chaperones for other proteins through the secretory pathway. The BURP domain is unique to plant proteins and plays a critical role in the function of these proteins, although the exact mechanisms are not fully understood.

### Why entry type matters:

An entry of type **domain**, **repeat**, or **homologous_superfamily** identifies a
structural/functional *module*, not a whole-protein function. GO terms describing a
whole-protein activity or process attached to such a module systematically over-annotate
every protein that merely *contains* the module. An entry of type **family** is more
likely to support whole-protein function terms, but only if the family is functionally
homogeneous.

## Research Target

Provide a comprehensive, citation-backed research report on the InterPro entry
**PTHR31458 (Polygalacturonase-associated BURP domain-containing protein)**, structured to support GO annotation review.

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
- **Accession:** PTHR31458
- **Name:** Polygalacturonase-associated BURP domain-containing protein
- **Short name:** PG-associated_BURP
- **Entry type:** family
- **Integrated into / parent:** IPR051897
- **Member database signatures:** Not specified
- **Scale:** 1738 proteins across 1244 taxa, 13 subfamilies
- **Current InterPro2GO terms (the mappings under review):** None mapped (no InterPro2GO terms for this entry)
- **InterPro description:** This family of proteins includes non-catalytic subunits of polygalacturonase as well as proteins containing a BURP domain at the C-terminus. Members of this family are involved in the regulation of plant cell size and growth, with some acting as chaperones for other proteins through the secretory pathway. The BURP domain is unique to plant proteins and plays a critical role in the function of these proteins, although the exact mechanisms are not fully understood.

### Why entry type matters:

An entry of type **domain**, **repeat**, or **homologous_superfamily** identifies a
structural/functional *module*, not a whole-protein function. GO terms describing a
whole-protein activity or process attached to such a module systematically over-annotate
every protein that merely *contains* the module. An entry of type **family** is more
likely to support whole-protein function terms, but only if the family is functionally
homogeneous.

## Research Target

Provide a comprehensive, citation-backed research report on the InterPro entry
**PTHR31458 (Polygalacturonase-associated BURP domain-containing protein)**, structured to support GO annotation review.

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


# Comprehensive Research Report: InterPro Entry PTHR31458
## Polygalacturonase-associated BURP domain-containing protein

**Report Date:** 2025  
**InterPro Accession:** PTHR31458  
**Entry Type:** Family  
**Current InterPro2GO Status:** No GO terms mapped

---

## Executive Summary

PTHR31458 represents a plant-specific protein family characterized by the conserved BURP domain (BNM2, USP, RD22, PG1β). This comprehensive analysis, based primarily on 2020-2025 literature, reveals that PTHR31458 is **functionally heterogeneous** with at least **seven distinct subfamilies** exhibiting divergent and sometimes opposing functions. The current absence of InterPro2GO mappings is **largely appropriate** given this extreme functional diversity. However, subfamily-specific child entries would be suitable targets for more precise GO annotation (ren2023genomewideidentificationand pages 1-2, chigumba2022discoveryandbiosynthesis pages 1-3, jin2020ethyleneinsensitive3like2(oseil2) pages 1-4, ren2023genomewideidentificationand pages 4-6).

**Key Finding:** Recent biochemical characterization (2022) revealed that a subset of BURP domains have undergone neo-functionalization to serve as **copper-dependent autocatalytic peptide cyclases** in specialized metabolism, representing a fundamental expansion of the family's known biochemical repertoire beyond structural and regulatory roles (chigumba2022discoveryandbiosynthesis pages 1-3, chigumba2022discoveryandbiosynthesis pages 7-7).

---

## 1. Family Definition and Biochemistry

### 1.1 BURP Domain Structure and Conserved Residues

The BURP domain is a **~230 amino acid** plant-specific module defined by highly conserved structural motifs (ren2023genomewideidentificationand pages 1-2, ren2023genomewideidentificationand pages 4-6). The canonical architecture comprises:

**N-terminal region:**
- Hydrophobic signal peptide sequence (~20 amino acids) directing secretory pathway trafficking (present in ~70% of family members) (ren2023genomewideidentificationand pages 1-2, ren2023genomewideidentificationand pages 4-6)
- Two conserved phenylalanine residues (FF motif) (ren2023genomewideidentificationand pages 1-2)

**Central variable region:**
- Short conserved sequences or tandemly repeated motifs
- Variable fragment composition distinguishes subfamilies (ren2023genomewideidentificationand pages 1-2)
- Some members harbor **multi-core precursor peptide repeats** embedded in this region (specialized for RiPP biosynthesis) (chigumba2022discoveryandbiosynthesis pages 1-3, wang2025largescaletranscriptomemining pages 2-3)

**C-terminal BURP domain (defining signature):**
- Conserved residues: valine (V), aspartic acid (D), threonine (T), proline (P), glycine (G) (ren2023genomewideidentificationand pages 1-2)
- **Fourfold cysteine-histidine (CH) motif:** CHX₁₀CHX₂₅₋₂₇CHX₂₅₋₂₆CHX₈-W  
  (where X = any amino acid, W = tryptophan) (ren2023genomewideidentificationand pages 1-2, ren2023genomewideidentificationand pages 4-6)

### 1.2 Fold and Mechanistic Functions

**Classical Model (Pre-2022):** BURP proteins were understood primarily as **non-catalytic structural or regulatory proteins** associated with cell walls, secretory vesicles, and developmental processes (ren2023genomewideidentificationand pages 1-2, ren2023genomewideidentificationand pages 2-4).

**Breakthrough Discovery (2022):** Chigumba et al. demonstrated experimentally that BURP domains in specialized precursor proteins function as **copper-dependent autocatalytic peptide cyclases** (chigumba2022discoveryandbiosynthesis pages 1-3, chigumba2022discoveryandbiosynthesis pages 7-7). Key biochemical findings include:

1. **Catalytic mechanism:** BURP domains catalyze C-N, C-O, and C-C crosslinks between aromatic amino acid side chains (tyrosine, tryptophan) and other residues within their own N-terminal core peptide sequences, generating mono- and bicyclic peptides (burpitides) (chigumba2022discoveryandbiosynthesis pages 1-3, chigumba2022discoveryandbiosynthesis pages 7-7, chigumba2022discoveryandbiosynthesis pages 6-6)

2. **Metal cofactor:** Requires **Cu(II)** for single-turnover autocatalytic cyclization; characterized BURP cyclases (SkrBURP, CcaBURP1/2, AhyBURP, KjaBURP) showed copper-dependent activity in vitro (chigumba2022discoveryandbiosynthesis pages 1-3, mydy2021plantcoppermetalloenzymes pages 3-4, chigumba2022discoveryandbiosynthesis pages 7-7)

3. **Oxygen tolerance:** BURP-mediated cyclization occurs under aerobic conditions, distinguishing it from some bacterial radical SAM cyclases (chigumba2022discoveryandbiosynthesis pages 7-7)

4. **Substrates:** Intrinsic core peptides (autocatalytic) with C-terminal aromatic residues; generates ribosomally synthesized and post-translationally modified peptides (RiPPs) including selanine, cercic acid, stephanotic acid, legumenin, and moroidin scaffolds (mydy2021plantcoppermetalloenzymes pages 2-3, chigumba2022discoveryandbiosynthesis pages 1-3, chigumba2022discoveryandbiosynthesis pages 5-6, wang2025largescaletranscriptomemining pages 2-3)

**Structural Context:** The conserved CH motifs likely coordinate copper ions, though high-resolution BURP domain structures have not been solved. The four CH residues are positioned with defined spacing suggesting a metal-binding architecture (ren2023genomewideidentificationand pages 1-2, ren2023genomewideidentificationand pages 4-6).

**Caveat:** This catalytic function is **not universal** across PTHR31458—it represents **neo-functionalization** in specialized BURP-domain precursor proteins rather than the ancestral family role (chigumba2022discoveryandbiosynthesis pages 1-3, chigumba2022discoveryandbiosynthesis pages 7-7).

---

## 2. InterPro2GO Mapping Appropriateness

**Current Status:** PTHR31458 has **zero GO terms** mapped via InterPro2GO.

**Verdict:** This absence is **largely sound and reflects appropriate caution** given the family's extreme functional heterogeneity. Specific analysis of potential GO terms:

| Potential GO term | GO ID | Evidence level | Recommendation | Rationale |
|---|---|---|---|---|
| extracellular region | GO:0005576 | Subfamily-specific | MODIFY | Many BURP proteins carry N-terminal signal peptides and are predicted/perceived as secretory-pathway or extracellular/apoplastic proteins, especially PG1β-like and many RD22/USP members; however several family members lack signal peptides or have incomplete BURP domains, so this is not true for every PTHR31458 match (ren2023genomewideidentificationand pages 1-2, ren2023genomewideidentificationand pages 2-4, ren2023genomewideidentificationand pages 4-6). |
| apoplast | GO:0048046 | Subset only | REJECT | Apoplastic localization is experimentally reported for some RD22-like proteins (e.g., soybean GmRD22 in cited literature within retrieved reviews) and is plausible for secreted cell-wall-associated members, but it is not demonstrated across the full family and would over-annotate intracellular/vesicular or precursor-peptide cyclase members (ren2023genomewideidentificationand pages 1-2, ren2023genomewideidentificationand pages 2-4). |
| copper ion binding | GO:0005507 | Subset only | REJECT | Copper dependence is experimentally established for BURP-domain peptide cyclases involved in RiPP biosynthesis, but this neo-functionalized catalytic role applies only to a specialized subset of BURP proteins rather than the whole family; adding this term to PTHR31458 would over-annotate classical PG1β, RD22, USP, and BNM2 proteins (mydy2021plantcoppermetalloenzymes pages 2-3, chigumba2022discoveryandbiosynthesis pages 1-3, mydy2021plantcoppermetalloenzymes pages 3-4, chigumba2022discoveryandbiosynthesis pages 7-7). |
| peptide cyclase activity | GO:0140101* | Subset only | CREATE_CHILD_TERM | Chigumba et al. showed that some BURP domains are copper-dependent autocatalytic peptide cyclases generating cyclic RiPP scaffolds, but these are specialized BURP-domain precursor proteins and not representative of the entire PTHR31458 family; if InterPro wants GO here, it belongs on a more specific child entry for RiPP-biosynthetic BURP proteins (chigumba2022discoveryandbiosynthesis pages 1-3, chigumba2022discoveryandbiosynthesis pages 7-7, wang2025largescaletranscriptomemining pages 2-3). |
| peptide macrocyclization involved in RiPP biosynthesis | no stable ID confirmed from context | Subset only | CREATE_CHILD_TERM | Strong experimental evidence supports BURP-mediated side-chain macrocyclization for selanine, cercic acid, stephanotic acid, legumenin, and related burpitides, but only in specialized precursor-peptide BURP proteins; not suitable for the full family-level signature (chigumba2022discoveryandbiosynthesis pages 1-3, chigumba2022discoveryandbiosynthesis pages 5-6, chigumba2022discoveryandbiosynthesis pages 7-7, wang2025largescaletranscriptomemining pages 2-3). |
| polygalacturonase regulator activity | no stable ID confirmed from context | Subfamily-specific | CREATE_CHILD_TERM | PG1β-like members are defined as non-catalytic β-subunits of polygalacturonase isozyme 1 and in rice OsBURP14/16 modulate PG activity and pectin content; this is specific to the PG1β-like clade and should not be propagated to RD22/USP/BNM2 or peptide-cyclase BURP proteins (ren2023genomewideidentificationand pages 1-2, jin2020ethyleneinsensitive3like2(oseil2) pages 1-4, jin2020ethyleneinsensitive3like2(oseil2) pages 7-10). |
| cell wall organization or biogenesis | GO:0071554 | Subfamily-specific | MODIFY | Experimental work on PG1β-like OsBURP16 links BURP proteins to pectin reduction, altered cell adhesion, and wall integrity; some RD22-like proteins also affect lignified/apoplastic wall properties under stress. However these functions are not universal across the family and should be restricted to validated child groups, especially PG1β-like members (jin2020ethyleneinsensitive3like2(oseil2) pages 1-4, jin2020ethyleneinsensitive3like2(oseil2) pages 10-13, jin2020ethyleneinsensitive3like2(oseil2) pages 7-10). |
| pectin catabolic process | GO:0045490 | Subfamily-specific | REJECT | OsBURP16 overexpression increases PG activity and lowers pectin content, but BURP proteins are not themselves demonstrated catalytic pectin hydrolases; the signal would be indirect/regulatory and limited to PG1β-like members, so this process term is too strong and too broad for PTHR31458 (jin2020ethyleneinsensitive3like2(oseil2) pages 1-4, jin2020ethyleneinsensitive3like2(oseil2) pages 10-13, jin2020ethyleneinsensitive3like2(oseil2) pages 7-10). |
| response to water deprivation | GO:0009414 | Subfamily-specific | REJECT | RD22-like proteins are classically induced by ABA/drought and some enhance drought tolerance, but other BURP subfamilies have opposite or unrelated functions; the family is too heterogeneous for this process term at top level (ren2023genomewideidentificationand pages 1-2, ren2023genomewideidentificationand pages 4-6). |
| response to salt stress | GO:0009651 | Subfamily-specific | REJECT | Multiple BURP genes respond transcriptionally to salt, yet direction and mechanism differ by subfamily: some RD22-like genes enhance tolerance, whereas PG1β-like OsBURP16 promotes salt sensitivity. Opposite phenotypic effects make this unsuitable as a universal family annotation (ren2023genomewideidentificationand pages 1-2, jin2020ethyleneinsensitive3like2(oseil2) pages 1-4, jin2020ethyleneinsensitive3like2(oseil2) pages 10-13, jin2020ethyleneinsensitive3like2(oseil2) pages 7-10). |
| response to abscisic acid | GO:0009737 | Subfamily-specific | REJECT | ABA induction is well documented for RD22-like genes and also for OsBURP16, but this is a stress-regulated expression pattern seen in subsets, not a defining function of all BURP proteins (ren2023genomewideidentificationand pages 1-2, jin2020ethyleneinsensitive3like2(oseil2) pages 7-10). |
| seed development | GO:0048316 | Subfamily-specific | REJECT | USP-, BNM2-, SCB1-, and related BURP proteins participate in seed/pollen/embryogenesis contexts, but these developmental roles are not shared by PG1β-like or RiPP-cyclase BURP proteins, so the term should remain limited to appropriate child entries or gene-level annotations (ren2023genomewideidentificationand pages 1-2, ren2023genomewideidentificationand pages 2-4). |
| pollen development / male gametophyte development | GO:0009555 / GO:0048229 | Subfamily-specific | REJECT | BNM2-like and RAFTIN-like BURP proteins show reproductive-tissue-specific functions, but these are clear subfamily specializations and cannot be generalized to all PTHR31458 matches (ren2023genomewideidentificationand pages 1-2, ren2023genomewideidentificationand pages 2-4). |
| extracellular matrix structural constituent / structural molecule activity | GO:0005201 | Subset only | REJECT | Although many BURP proteins are secreted and associated with wall or extracellular compartments, there is no evidence that the family as a whole serves a conserved structural-molecule role; functions range from non-catalytic PG subunits to stress proteins to peptide cyclases (ren2023genomewideidentificationand pages 1-2, chigumba2022discoveryandbiosynthesis pages 1-3, ren2023genomewideidentificationand pages 4-6). |
| no automatic GO term at this family level | n/a | All family members | ACCEPT | The strongest overall conclusion is that PTHR31458 is functionally heterogeneous: it spans developmental proteins, stress-responsive proteins, PG1β-like non-catalytic cell-wall regulators, and specialized copper-dependent RiPP cyclases. Therefore the current lack of InterPro2GO mappings is largely appropriate; any future GO should be moved to narrower child entries rather than attached to the whole family (ren2023genomewideidentificationand pages 1-2, chigumba2022discoveryandbiosynthesis pages 1-3, jin2020ethyleneinsensitive3like2(oseil2) pages 1-4, chigumba2022discoveryandbiosynthesis pages 7-7, ren2023genomewideidentificationand pages 4-6). |


*Table: This table summarizes which GO terms are or are not appropriate for the BURP family-level InterPro entry PTHR31458. It is useful for GO review because it separates family-wide inferences from subfamily- or subset-specific functions, highlighting where child-entry annotation would be safer.*

**Critical Issues Precluding Family-Level GO Annotation:**

1. **Opposing phenotypes:** Stress response terms are inappropriate because subfamilies exhibit **opposite effects**—RD22-like proteins can enhance salt/drought tolerance, whereas PG1β-like OsBURP16 *increases* stress sensitivity (ren2023genomewideidentificationand pages 1-2, jin2020ethyleneinsensitive3like2(oseil2) pages 10-13, jin2020ethyleneinsensitive3like2(oseil2) pages 7-10)

2. **Localization inconsistency:** ~70% carry signal peptides for extracellular/secretory targeting, but ~30% lack them and show incomplete BURP domains, precluding universal "extracellular region" annotation (ren2023genomewideidentificationand pages 4-6)

3. **Catalytic vs. non-catalytic divide:** Copper-dependent peptide cyclase activity is restricted to specialized RiPP-biosynthetic BURP proteins and does not apply to classical PG1β, RD22, USP, or BNM2 members (chigumba2022discoveryandbiosynthesis pages 1-3, chigumba2022discoveryandbiosynthesis pages 7-7)

4. **Developmental vs. metabolic specialization:** BNM2/USP members function in pollen/seed development, whereas PG1β members regulate cell wall pectin degradation during fruit ripening and stress—fundamentally different processes (ren2023genomewideidentificationand pages 1-2, jin2020ethyleneinsensitive3like2(oseil2) pages 1-4)

---

## 3. Functional Divergence Across Subfamilies

PTHR31458 comprises **seven recognized subfamilies** with distinct and sometimes non-overlapping functions:

| Subfamily | Representative members / genes | Cellular localization | Primary known functions | Expression patterns / tissues | Involvement in stress responses | Key references |
|---|---|---|---|---|---|---|
| BNM2-like | **BNM2** from *Brassica napus*; apple **MdBNM1**; BURP-domain RiPP precursors such as **SkrBURP**, **CcaBURP1/2**, **AhyBURP**, **KjaBURP** are evolutionarily linked to the classical BURP set and carry N-terminal core-peptide regions plus C-terminal BURP domain | Often secretory-pathway associated; reported in Golgi apparatus, provacuole region, or protein storage vesicles for BNM2-like/related proteins; many BURP proteins also possess N-terminal signal peptides for secretion (ren2023genomewideidentificationand pages 2-4, ren2023genomewideidentificationand pages 4-6, chigumba2022discoveryandbiosynthesis pages 1-3, wang2025largescaletranscriptomemining pages 2-3) | Originally defined by microspore-derived embryo protein; involved in pollen grain embryogenesis/seed developmental programs. In specialized-metabolism examples, BURP domains act as **copper-dependent autocatalytic peptide cyclases** generating cyclic RiPP scaffolds (ren2023genomewideidentificationand pages 1-2, chigumba2022discoveryandbiosynthesis pages 1-3, chigumba2022discoveryandbiosynthesis pages 7-7, mydy2021plantcoppermetalloenzymes pages 3-4) | BNM2 is specifically expressed during pollen grain embryogenesis in grape; classical BNM2 family members are developmentally regulated, especially reproductive tissues (ren2023genomewideidentificationand pages 1-2) | Direct abiotic-stress function is not established as a universal property of BNM2-like proteins; evidence points more to developmental specialization, with some BURP-domain descendants neo-functionalized into peptide-biosynthetic enzymes rather than stress regulators (ren2023genomewideidentificationand pages 1-2, chigumba2022discoveryandbiosynthesis pages 1-3, chigumba2022discoveryandbiosynthesis pages 7-7) | (ren2023genomewideidentificationand pages 1-2, chigumba2022discoveryandbiosynthesis pages 1-3, ren2023genomewideidentificationand pages 2-4, mydy2021plantcoppermetalloenzymes pages 3-4, chigumba2022discoveryandbiosynthesis pages 7-7, wang2025largescaletranscriptomemining pages 2-3, ren2023genomewideidentificationand pages 4-6) |
| USP-like | **USP** from *Vicia faba*; apple **MdUSP1-3**; Arabidopsis **AtUSPL1** | Intracellular vesicles; reported for VfUSP/AtUSPL1-related proteins in Golgi/provacuolar or storage-vesicle compartments; many members have signal peptides consistent with secretory trafficking, though some family members lack them (ren2023genomewideidentificationand pages 2-4, ren2023genomewideidentificationand pages 4-6) | Non-storage/seed-associated proteins; implicated in seed development and protein accumulation/processing. Overexpression of AtUSPL1 and BNM2 can alter accumulation of seed proteins related to synthesis/storage/development (ren2023genomewideidentificationand pages 1-2, ren2023genomewideidentificationand pages 2-4) | Specifically expressed during broad bean seed development; apple **MdUSP1** highly expressed in roots in one cultivar dataset (ren2023genomewideidentificationand pages 1-2, ren2023genomewideidentificationand pages 4-6) | Some BURP USP-like genes respond to ABA-mediated water stress; cited example **AtUSPL1** is up-regulated by ABA-mediated water stress and increases drought tolerance (reported in review of BURP family literature) (ren2023genomewideidentificationand pages 1-2) | (ren2023genomewideidentificationand pages 1-2, ren2023genomewideidentificationand pages 2-4, ren2023genomewideidentificationand pages 4-6) |
| RD22-like | **RD22** from *Arabidopsis thaliana*; soybean **GmRD22**; grape **VvRD22**; apple **MdRD1-9** | Frequently extracellular/apoplastic or periplasmic-secretory pathway proteins; soybean GmRD22 specifically described as apoplast-localized in cited literature list; most apple RD proteins predicted periplasmic/extracellular, though several lack full signal peptides or show incomplete domains (ren2023genomewideidentificationand pages 4-6) | Stress-responsive cell-wall/apoplastic proteins implicated in growth regulation, cell wall/lignin-associated adaptation, and developmental regulation; not known as catalytic polygalacturonase subunits. Some BURP proteins generally regulate plant cell size and growth (ren2023genomewideidentificationand pages 1-2) | RD22 is induced by ABA or drought in *Arabidopsis*; apple **MdRD7** is highly expressed in fruit/leaves depending on cultivar and is strongly induced by NaCl and PEG over time (ren2023genomewideidentificationand pages 1-2, ren2023genomewideidentificationand pages 4-6) | Strongest evidence among classical BURP subfamilies for abiotic stress involvement: many RD22-like genes are induced by drought, salt, PEG, or ABA; overexpression examples from grape and soybean enhance salt/drought tolerance, with soybean **GmRD22** linked to increased cell-wall lignin (ren2023genomewideidentificationand pages 1-2) | (ren2023genomewideidentificationand pages 1-2, ren2023genomewideidentificationand pages 4-6) |
| PG1β-like | Tomato **PG1β**; rice **OsBURP14** and **OsBURP16**; apple **MdPG1-4** | Secretory/extracellular or wall-associated proteins; apple PG1β-like proteins predicted outer membrane/extracellular and have signal peptides; family context is consistent with secretory pathway/cell wall localization (ren2023genomewideidentificationand pages 4-6, jin2020ethyleneinsensitive3like2(oseil2) pages 1-4) | **Non-catalytic β-subunits of polygalacturonase isozyme 1** and related PG1β-like proteins. These proteins are linked to **polygalacturonase activity, pectin degradation, cell adhesion, and cell wall modification** rather than having GH28 catalytic residues themselves. In rice, **OsBURP16 overexpression increased PG activity, decreased pectin content, reduced cell adhesion, and enhanced abiotic stress sensitivity**; **OsEIL2 directly activates OsBURP14/16**, causing elevated PG activity and lower pectin content (ren2023genomewideidentificationand pages 1-2, jin2020ethyleneinsensitive3like2(oseil2) pages 1-4, jin2020ethyleneinsensitive3like2(oseil2) pages 7-10, jin2020ethyleneinsensitive3like2(oseil2) pages 10-13, chigumba2022discoveryandbiosynthesis pages 4-5) | Originally defined by tomato fruit-ripening PG1β expressed at maturity; in rice, **OsBURP16** is strongly induced by ABA, ACC, NaCl, PEG, and dark, and OsBURP14/16 are transcriptionally activated by OsEIL2; apple **MdPG3/4** show tissue-specific expression (ren2023genomewideidentificationand pages 1-2, jin2020ethyleneinsensitive3like2(oseil2) pages 7-10, ren2023genomewideidentificationand pages 4-6) | Clear, experimentally supported stress linkage in at least a subset: **OsBURP16** promotes salt and drought sensitivity via pectin loss/cell-wall integrity effects; however this is not yet demonstrated for all PG1β-like proteins. Thus the subfamily is functionally connected to cell-wall remodeling and stress responsiveness, but stress-sign direction may vary by lineage and expression context (jin2020ethyleneinsensitive3like2(oseil2) pages 1-4, jin2020ethyleneinsensitive3like2(oseil2) pages 7-10, jin2020ethyleneinsensitive3like2(oseil2) pages 10-13) | (ren2023genomewideidentificationand pages 1-2, jin2020ethyleneinsensitive3like2(oseil2) pages 1-4, chigumba2022discoveryandbiosynthesis pages 4-5, ren2023genomewideidentificationand pages 4-6, jin2020ethyleneinsensitive3like2(oseil2) pages 10-13, jin2020ethyleneinsensitive3like2(oseil2) pages 7-10) |
| BURP V | Rice-specific/monocot-enriched clade reported in rice genome-wide classification; specific representatives not detailed in retrieved passages | Not resolved from retrieved evidence; likely secretory-pathway biased like many BURP proteins but not experimentally established here (jin2020ethyleneinsensitive3like2(oseil2) pages 1-4, ren2023genomewideidentificationand pages 4-6) | Function currently unclear; appears to represent lineage-specific expansion outside the four founding subfamilies (jin2020ethyleneinsensitive3like2(oseil2) pages 1-4) | Not enough direct evidence in retrieved texts; classification recognized in rice BURP family analyses (jin2020ethyleneinsensitive3like2(oseil2) pages 1-4) | Some rice BURP family members broadly respond to salt stress, but retrieved evidence does not assign a specific abiotic-stress role uniquely to BURP V members (jin2020ethyleneinsensitive3like2(oseil2) pages 1-4, jin2020ethyleneinsensitive3like2(oseil2) pages 10-13) | (jin2020ethyleneinsensitive3like2(oseil2) pages 1-4, ren2023genomewideidentificationand pages 4-6, jin2020ethyleneinsensitive3like2(oseil2) pages 10-13) |
| BURP VI | Rice/monocot-dominated clade in phylogenetic analyses; apple also contains one BURPVI member according to recent apple family study | Not resolved experimentally in retrieved passages; many BURP proteins in apple/rice are predicted periplasmic or extracellular, but subfamily-specific localization is not shown (ren2023genomewideidentificationand pages 4-6) | Function unknown; likely represents monocot-heavy expansion with no universal biochemical role yet established from the gathered evidence (ren2023genomewideidentificationand pages 4-6) | Mostly monocot members; present in rice-dominated phylogeny and one apple member in recent survey (ren2023genomewideidentificationand pages 4-6) | No subfamily-specific stress mechanism established in the retrieved evidence, though BURP families in rice/apple often show abiotic-stress-responsive transcription (ren2023genomewideidentificationand pages 4-6) | (ren2023genomewideidentificationand pages 4-6) |
| BURP VII | Rice/monocot-dominated clade recognized in rice classification | Not resolved from retrieved evidence (jin2020ethyleneinsensitive3like2(oseil2) pages 1-4, ren2023genomewideidentificationand pages 4-6) | Function unknown; likely lineage-specific BURP diversification without a demonstrated shared mechanistic role from current evidence (jin2020ethyleneinsensitive3like2(oseil2) pages 1-4, ren2023genomewideidentificationand pages 4-6) | Mostly monocot members in phylogenetic analyses (ren2023genomewideidentificationand pages 4-6) | No direct experimental stress function recovered in the retrieved evidence for this subfamily specifically (jin2020ethyleneinsensitive3like2(oseil2) pages 1-4, ren2023genomewideidentificationand pages 4-6) | (jin2020ethyleneinsensitive3like2(oseil2) pages 1-4, ren2023genomewideidentificationand pages 4-6) |


*Table: This table summarizes the major BURP domain subfamilies, highlighting their representative genes, localization, functions, expression patterns, and stress associations. It is especially useful for distinguishing the experimentally supported PG1β-like cell-wall/polygalacturonase-linked roles from the more weakly characterized or lineage-specific BURP clades.*

### 3.1 Major Functional Partitions

**Group 1: Developmental/Reproductive Proteins**
- **BNM2-like:** Microspore-derived embryogenesis, pollen grain development (ren2023genomewideidentificationand pages 1-2)
- **USP-like:** Seed development, protein storage/accumulation in vesicles (ren2023genomewideidentificationand pages 1-2, ren2023genomewideidentificationand pages 2-4)
- Localization: Golgi apparatus, provacuolar regions, protein storage vesicles (ren2023genomewideidentificationand pages 2-4)

**Group 2: Stress-Responsive Apoplastic Proteins**
- **RD22-like:** ABA/drought inducible, apoplast-localized, enhance abiotic stress tolerance, linked to cell wall lignification (GmRD22 increases lignin in soybean) (ren2023genomewideidentificationand pages 1-2)
- Evidence: VvRD22 (grape) and GmRD22 (soybean) overexpression enhances salt/drought tolerance (ren2023genomewideidentificationand pages 1-2)

**Group 3: Cell Wall Modifiers (Non-Catalytic PG Subunits)**
- **PG1β-like:** Non-catalytic **β-subunits of polygalacturonase isozyme 1** (ren2023genomewideidentificationand pages 1-2, jin2020ethyleneinsensitive3like2(oseil2) pages 1-4)
- Mechanism: Modulate PG enzymatic activity → increased pectin degradation → reduced cell adhesion and wall integrity (jin2020ethyleneinsensitive3like2(oseil2) pages 1-4, jin2020ethyleneinsensitive3like2(oseil2) pages 10-13, jin2020ethyleneinsensitive3like2(oseil2) pages 7-10)
- Expression: Tomato PG1β expressed during fruit ripening; rice OsBURP14/16 induced by ethylene signaling (OsEIL2), ABA, ACC, salt, drought, and darkness (jin2020ethyleneinsensitive3like2(oseil2) pages 7-10)
- **Experimental phenotype (rice OsBURP16):** Overexpression → ↑ PG activity, ↓ pectin content, ↓ cell adhesion, **↑ salt/drought sensitivity** (opposite effect from RD22 subfamily) (jin2020ethyleneinsensitive3like2(oseil2) pages 1-4, jin2020ethyleneinsensitive3like2(oseil2) pages 10-13, jin2020ethyleneinsensitive3like2(oseil2) pages 7-10)
- Regulatory linkage: OsEIL2 transcription factor directly binds OsBURP14/16 promoters at EIN3-binding sites (TTCAAA, ATGTA), activating transcription during stress and senescence (jin2020ethyleneinsensitive3like2(oseil2) pages 7-10)

**Group 4: Specialized Metabolic Enzymes (Neo-Functionalized)**
- **BURP-domain RiPP cyclases:** Copper-dependent autocatalytic peptide cyclases generating cyclic plant natural products (burpitides) (chigumba2022discoveryandbiosynthesis pages 1-3, chigumba2022discoveryandbiosynthesis pages 7-7, wang2025largescaletranscriptomemining pages 2-3)
- Representative members: SkrBURP (selanine A/B from *Selaginella kraussiana*), CcaBURP1 (cercic acid), CcaBURP2 (stephanotic acid-LV), AhyBURP (legumenin from peanut), KjaBURP (moroidin from *Kerria japonica*) (chigumba2022discoveryandbiosynthesis pages 1-3, chigumba2022discoveryandbiosynthesis pages 5-6, wang2025largescaletranscriptomemining pages 2-3)
- Substrate specificity: Intrinsic N-terminal core peptides with tyrosine/tryptophan for macrocyclization (chigumba2022discoveryandbiosynthesis pages 1-3)
- Distribution: Identified across lycophytes, ferns, gymnosperms, and angiosperms; genome mining predicts ~12% of BURP-domain loci encode cyclic peptides (chigumba2022discoveryandbiosynthesis pages 7-7)

**Group 5: Lineage-Specific Expansions (Unknown Function)**
- **BURP V, VI, VII:** Monocot-dominated clades (especially rice) with no experimentally established biochemical roles (jin2020ethyleneinsensitive3like2(oseil2) pages 1-4, ren2023genomewideidentificationand pages 4-6)

### 3.2 Pseudo-Enzymes and Incomplete Domains

Several apple BURP proteins (**MdRD2, MdRD3, MdRD5, MdBNM1**) lack complete BURP domains or signal peptides, suggesting potential non-functional or regulatory-only variants (ren2023genomewideidentificationand pages 4-6). However, explicit characterization of catalytically-dead or dominant-negative BURP proteins has not been experimentally demonstrated in retrieved literature.

---

## 4. Taxonomic Scope

**Distribution:** PTHR31458 is **strictly plant-specific** and appears at the evolutionary origin of **land plants (Embryophyta)** (wang2025largescaletranscriptomemining pages 2-3).

**Presence confirmed:**
- **Lycophytes:** *Selaginella kraussiana* (African clubmoss) (chigumba2022discoveryandbiosynthesis pages 1-3)
- **Ferns:** Cycad-related gymnosperms  
- **Gymnosperms:** *Encephalartos altensteinii* (Eastern Cape giant cycad), cycads (chigumba2022discoveryandbiosynthesis pages 3-4)
- **Angiosperms (Monocots):** *Oryza sativa* (rice), *Zea mays* (maize), grasses (jin2020ethyleneinsensitive3like2(oseil2) pages 1-4, ren2023genomewideidentificationand pages 4-6)
- **Angiosperms (Dicots):** *Arabidopsis thaliana*, *Glycine max* (soybean), *Vitis vinifera* (grape), *Malus domestica* (apple, 18 genes), *Cercis canadensis* (Eastern redbud), legumes, Brassicaceae, Rosaceae, etc. (ren2023genomewideidentificationand pages 1-2, chigumba2022discoveryandbiosynthesis pages 1-3, ren2023genomewideidentificationand pages 4-6)

**Absence confirmed:**
- **Green algae (Chlorophyta):** Analysis of 6 green algal genomes found **zero BURP-domain genes** (wang2025largescaletranscriptomemining pages 2-3)

**Gene copy number:** Plant genomes average **~9 BURP genes**, with documented range of 17-18 in rice and apple (jin2020ethyleneinsensitive3like2(oseil2) pages 1-4, ren2023genomewideidentificationand pages 4-6). InterPro entry PTHR31458 encompasses **1738 proteins across 1244 taxa**, consistent with broad land plant distribution (user-provided metadata).

**Taxonomic constraint for GO terms:** Because BURP domains are absent from algae and specific to land plants, any assigned GO terms must reflect plant-specific biology (cell wall composition, land-plant-specific stress adaptations, etc.). No marine/aquatic-specific process terms are appropriate despite presence in the marine angiosperm *Zostera marina* (chigumba2022discoveryandbiosynthesis pages 7-7).

---

## 5. Over-Annotation Verdict and GO Action Recommendations

### 5.1 Overall Assessment

**InterPro2GO for PTHR31458 is currently sound in its ABSENCE of mapped terms.** The family exhibits:

1. **Functional heterogeneity** spanning development, stress response, cell wall modification, and specialized metabolism  
2. **Opposing phenotypes** (stress tolerance vs. sensitivity) across subfamilies  
3. **Neo-functionalization events** (catalytic peptide cyclases) not shared by all members  
4. **Localization diversity** (extracellular, vesicular, incomplete signal peptides)  

These characteristics make **family-level GO annotation inappropriate** and prone to systematic over-annotation.

### 5.2 Recommended GO Action Pattern

**For PTHR31458 (family level):**  
**ACCEPT** — Maintain current absence of GO terms. Do not add broad molecular function, biological process, or cellular component terms to this entry.

**For subfamily-specific child entries (if created):**  
Recommend **CREATE_CHILD_TERM** strategy with the following subfamily-specific mappings:

1. **PG1β-like subfamily child entry:**
   - **MODIFY-to-specific:** GO terms related to "regulation of polygalacturonase activity" or "pectin catabolic process regulation" (not direct catalysis)
   - **MODIFY-to-specific:** "cell wall organization" (GO:0071554) restricted to this clade
   - **MODIFY-to-specific:** "extracellular region" (GO:0005576) for signal-peptide-containing members
   - Experimental support: Rice OsBURP14/16 (jin2020ethyleneinsensitive3like2(oseil2) pages 1-4, jin2020ethyleneinsensitive3like2(oseil2) pages 10-13, jin2020ethyleneinsensitive3like2(oseil2) pages 7-10)

2. **BURP-domain RiPP cyclase child entry:**
   - **CREATE_CHILD_TERM:** "copper ion binding" (GO:0005507)
   - **CREATE_CHILD_TERM:** "peptide cyclase activity" or "peptide macrocyclization involved in RiPP biosynthesis"
   - **KEEP_AS_NON_CORE:** Highly specialized function, not representative of family
   - Experimental support: SkrBURP, CcaBURP1/2, AhyBURP, KjaBURP (chigumba2022discoveryandbiosynthesis pages 1-3, chigumba2022discoveryandbiosynthesis pages 7-7)

3. **RD22-like subfamily child entry:**
   - **MODIFY-to-specific:** "response to abscisic acid" (GO:0009737) or "response to water deprivation" (GO:0009414) with qualifier noting stress tolerance enhancement
   - **MODIFY-to-specific:** "apoplast" (GO:0048046) for experimentally verified members
   - Experimental support: GmRD22, VvRD22 (ren2023genomewideidentificationand pages 1-2)

4. **BNM2-like and USP-like subfamily child entries:**
   - **MODIFY-to-specific:** Developmental process terms ("pollen development," "seed development") restricted to these clades
   - **KEEP_AS_NON_CORE:** Tissue-specific expression, not universal
   - Experimental support: BNM2, VfUSP, AtUSPL1, SCB1 (ren2023genomewideidentificationand pages 1-2, ren2023genomewideidentificationand pages 2-4)

### 5.3 InterPro Recommendation

**Demote whole-protein function terms** from PTHR31458 and **move to child entries** corresponding to phylogenetically coherent and functionally validated subfamilies. If InterPro maintains PTHR31458 as a family-level signature without subdivision, then **MARK_AS_OVER_ANNOTATED** would apply to any broad GO assignments, and we recommend **REMOVE** any future terms erroneously added at this level.

---

## 6. Distinction of Experimental vs. Inferred Evidence

### Experimental Findings (Direct Evidence)

1. **BURP-domain peptide cyclase activity:** Demonstrated via in vitro incubation of recombinant BURP domains (MBP-SkrBURP, MBP-CcaBURP1/2) with Cu(II), detection of modified core peptides by LC-MS/MS, NMR structure elucidation of cyclic products, and exopeptidase-based confirmation (chigumba2022discoveryandbiosynthesis pages 1-3, chigumba2022discoveryandbiosynthesis pages 7-7, chigumba2022discoveryandbiosynthesis pages 6-6)

2. **OsBURP16 cell wall function:** Rice transgenic overexpression lines showed increased PG activity (enzymatic assay), decreased pectin content (biochemical quantification), reduced cell adhesion (microscopy), and enhanced salt/drought sensitivity (survival assays, chlorophyll retention, water loss rates) (jin2020ethyleneinsensitive3like2(oseil2) pages 1-4, jin2020ethyleneinsensitive3like2(oseil2) pages 10-13, jin2020ethyleneinsensitive3like2(oseil2) pages 7-10)

3. **OsEIL2-BURP regulatory axis:** ChIP-qPCR confirmed OsEIL2 binding to OsBURP14/16 promoters in vivo; EMSA validated direct DNA binding in vitro (jin2020ethyleneinsensitive3like2(oseil2) pages 7-10)

4. **GmRD22/VvRD22 stress tolerance:** Transgenic tobacco/Arabidopsis overexpressing soybean or grape RD22 showed enhanced salt/drought survival; GmRD22 linked to elevated lignin content (biochemical assay) (ren2023genomewideidentificationand pages 1-2)

### Inferred Evidence (Computational/Structural)

1. **BURP domain conserved motifs:** Predicted from sequence alignments and phylogenetic analyses across multiple species; no crystal structure available (ren2023genomewideidentificationand pages 1-2, ren2023genomewideidentificationand pages 4-6)

2. **Subcellular localization:** Primarily inferred from signal peptide prediction algorithms (SignalP) and homology to experimentally localized orthologs (ren2023genomewideidentificationand pages 4-6)

3. **Subfamilies BURP V/VI/VII:** Defined by phylogenetic clustering without experimental functional validation (jin2020ethyleneinsensitive3like2(oseil2) pages 1-4, ren2023genomewideidentificationand pages 4-6)

4. **Copper coordination by CH motifs:** Inferred from spacing pattern and requirement for Cu(II) in cyclase assays; direct structural evidence for metal binding is lacking (chigumba2022discoveryandbiosynthesis pages 1-3, chigumba2022discoveryandbiosynthesis pages 7-7)

---

## 7. Key Literature Citations

**Foundational Reviews and Methods (2024-2025):**
- Chekan et al. (2024) *Natural Product Reports* — Comprehensive plant RiPP biosynthesis review including BURP-domain burpitides (chekan2024plantpeptides– pages 3-4, chekan2024plantpeptides– pages 7-8)
- Mydy et al. (2021) *Frontiers in Plant Science* — Plant copper metalloenzymes including BURP cyclases (mydy2021plantcoppermetalloenzymes pages 2-3, mydy2021plantcoppermetalloenzymes pages 3-4)
- Wang et al. (2025) *Nature Communications* — Large-scale transcriptome mining for stephanotic acid-type burpitides (wang2025largescaletranscriptomemining pages 2-3)

**Primary Experimental Studies (2020-2022):**
- Chigumba et al. (2022) *Nature Chemical Biology* — Discovery and biochemical characterization of BURP-domain autocatalytic peptide cyclases (chigumba2022discoveryandbiosynthesis pages 1-3, chigumba2022discoveryandbiosynthesis pages 5-6, chigumba2022discoveryandbiosynthesis pages 4-5, chigumba2022discoveryandbiosynthesis pages 3-4, chigumba2022discoveryandbiosynthesis pages 7-7, chigumba2022discoveryandbiosynthesis pages 6-6)
- Jin et al. (2020) *Plant Science* — OsEIL2-OsBURP16 regulatory axis in rice salt/drought stress via pectin modification (jin2020ethyleneinsensitive3like2(oseil2) pages 1-4, jin2020ethyleneinsensitive3like2(oseil2) pages 4-7, jin2020ethyleneinsensitive3like2(oseil2) pages 10-13, jin2020ethyleneinsensitive3like2(oseil2) pages 7-10)

**Genome-Wide Family Analyses (2023):**
- Ren et al. (2023) *Physiology and Molecular Biology of Plants* — Apple BURP family identification and abiotic stress expression profiling (ren2023genomewideidentificationand pages 1-2, ren2023genomewideidentificationand pages 2-4, ren2023genomewideidentificationand pages 4-6)

---

## 8. Conclusions

PTHR31458 (Polygalacturonase-associated BURP domain-containing protein) represents a **functionally heterogeneous plant-specific protein family** that has undergone extensive subfamily-specific specialization and neo-functionalization. The family encompasses:

1. **Structural/developmental proteins** (BNM2, USP subfamilies) with roles in pollen, seed, and vesicular processes  
2. **Stress-responsive apoplastic proteins** (RD22 subfamily) enhancing abiotic stress tolerance  
3. **Cell wall modifiers** (PG1β subfamily) acting as non-catalytic polygalacturonase regulators with negative effects on stress tolerance  
4. **Copper-dependent peptide cyclases** (specialized BURP-domain RiPP biosynthetic enzymes) generating bioactive cyclic peptides  

The **absence of InterPro2GO mappings is appropriate** at the family level due to incompatible and sometimes opposing functions across subfamilies. Future GO annotation efforts should focus on **creating subfamily-specific child entries** rather than applying broad terms to PTHR31458 itself. This approach will prevent systematic over-annotation while enabling accurate functional description of phylogenetically coherent BURP protein clades.

**Final Recommendation:** **ACCEPT** current InterPro2GO status (no terms); recommend **CREATE_CHILD_TERM** strategy for subfamily-level annotations when/if InterPro subdivides this entry (ren2023genomewideidentificationand pages 1-2, chigumba2022discoveryandbiosynthesis pages 1-3, jin2020ethyleneinsensitive3like2(oseil2) pages 1-4, chigumba2022discoveryandbiosynthesis pages 7-7, ren2023genomewideidentificationand pages 4-6, jin2020ethyleneinsensitive3like2(oseil2) pages 10-13, jin2020ethyleneinsensitive3like2(oseil2) pages 7-10).

References

1. (ren2023genomewideidentificationand pages 1-2): Jiaxuan Ren, Li Feng, Lili Guo, Huimin Gou, Shixiong Lu, and Juan Mao. Genome-wide identification and expression analysis of the burp domain-containing genes in malus domestica. Physiology and Molecular Biology of Plants, 29:1717-1731, Nov 2023. URL: https://doi.org/10.1007/s12298-023-01393-7, doi:10.1007/s12298-023-01393-7. This article has 4 citations and is from a peer-reviewed journal.

2. (chigumba2022discoveryandbiosynthesis pages 1-3): Desnor N. Chigumba, L. S. Mydy, F. de Waal, Wenjie Li, Khadija Shafiq, Jesse W. Wotring, Osama G. Mohamed, Tim Mladenovic, A. Tripathi, J. Sexton, S. Kautsar, M. Medema, and R. Kersten. Discovery and biosynthesis of cyclic plant peptides via autocatalytic cyclases. JournalArticle, Jan 2022. URL: https://doi.org/10.7302/24583, doi:10.7302/24583. This article has 84 citations.

3. (jin2020ethyleneinsensitive3like2(oseil2) pages 1-4): Jing Jin, Jianli Duan, Chi Shan, Zhiling Mei, Haiying Chen, Huafeng Feng, Jian Zhu, and Weiming Cai. Ethylene insensitive3-like2 (oseil2) confers stress sensitivity by regulating osburp16, the β subunit of polygalacturonase (pg1β-like) subfamily gene in rice. Plant science : an international journal of experimental plant biology, 292:110353, Mar 2020. URL: https://doi.org/10.1016/j.plantsci.2019.110353, doi:10.1016/j.plantsci.2019.110353. This article has 44 citations.

4. (ren2023genomewideidentificationand pages 4-6): Jiaxuan Ren, Li Feng, Lili Guo, Huimin Gou, Shixiong Lu, and Juan Mao. Genome-wide identification and expression analysis of the burp domain-containing genes in malus domestica. Physiology and Molecular Biology of Plants, 29:1717-1731, Nov 2023. URL: https://doi.org/10.1007/s12298-023-01393-7, doi:10.1007/s12298-023-01393-7. This article has 4 citations and is from a peer-reviewed journal.

5. (chigumba2022discoveryandbiosynthesis pages 7-7): Desnor N. Chigumba, L. S. Mydy, F. de Waal, Wenjie Li, Khadija Shafiq, Jesse W. Wotring, Osama G. Mohamed, Tim Mladenovic, A. Tripathi, J. Sexton, S. Kautsar, M. Medema, and R. Kersten. Discovery and biosynthesis of cyclic plant peptides via autocatalytic cyclases. JournalArticle, Jan 2022. URL: https://doi.org/10.7302/24583, doi:10.7302/24583. This article has 84 citations.

6. (wang2025largescaletranscriptomemining pages 2-3): Xiaofeng Wang, Khadija Shafiq, Derrick A. Ousley, Desnor N. Chigumba, Dulciana Davis, Kali M. McDonough, Lisa S. Mydy, Jonathan Z. Sexton, and Roland D. Kersten. Large-scale transcriptome mining enables macrocyclic diversification and improved bioactivity of the stephanotic acid scaffold. Nature Communications, May 2025. URL: https://doi.org/10.1038/s41467-025-59428-4, doi:10.1038/s41467-025-59428-4. This article has 4 citations and is from a highest quality peer-reviewed journal.

7. (ren2023genomewideidentificationand pages 2-4): Jiaxuan Ren, Li Feng, Lili Guo, Huimin Gou, Shixiong Lu, and Juan Mao. Genome-wide identification and expression analysis of the burp domain-containing genes in malus domestica. Physiology and Molecular Biology of Plants, 29:1717-1731, Nov 2023. URL: https://doi.org/10.1007/s12298-023-01393-7, doi:10.1007/s12298-023-01393-7. This article has 4 citations and is from a peer-reviewed journal.

8. (chigumba2022discoveryandbiosynthesis pages 6-6): Desnor N. Chigumba, L. S. Mydy, F. de Waal, Wenjie Li, Khadija Shafiq, Jesse W. Wotring, Osama G. Mohamed, Tim Mladenovic, A. Tripathi, J. Sexton, S. Kautsar, M. Medema, and R. Kersten. Discovery and biosynthesis of cyclic plant peptides via autocatalytic cyclases. JournalArticle, Jan 2022. URL: https://doi.org/10.7302/24583, doi:10.7302/24583. This article has 84 citations.

9. (mydy2021plantcoppermetalloenzymes pages 3-4): Lisa S. Mydy, Desnor N. Chigumba, and Roland D. Kersten. Plant copper metalloenzymes as prospects for new metabolism involving aromatic compounds. Frontiers in Plant Science, Nov 2021. URL: https://doi.org/10.3389/fpls.2021.692108, doi:10.3389/fpls.2021.692108. This article has 46 citations.

10. (mydy2021plantcoppermetalloenzymes pages 2-3): Lisa S. Mydy, Desnor N. Chigumba, and Roland D. Kersten. Plant copper metalloenzymes as prospects for new metabolism involving aromatic compounds. Frontiers in Plant Science, Nov 2021. URL: https://doi.org/10.3389/fpls.2021.692108, doi:10.3389/fpls.2021.692108. This article has 46 citations.

11. (chigumba2022discoveryandbiosynthesis pages 5-6): Desnor N. Chigumba, L. S. Mydy, F. de Waal, Wenjie Li, Khadija Shafiq, Jesse W. Wotring, Osama G. Mohamed, Tim Mladenovic, A. Tripathi, J. Sexton, S. Kautsar, M. Medema, and R. Kersten. Discovery and biosynthesis of cyclic plant peptides via autocatalytic cyclases. JournalArticle, Jan 2022. URL: https://doi.org/10.7302/24583, doi:10.7302/24583. This article has 84 citations.

12. (jin2020ethyleneinsensitive3like2(oseil2) pages 7-10): Jing Jin, Jianli Duan, Chi Shan, Zhiling Mei, Haiying Chen, Huafeng Feng, Jian Zhu, and Weiming Cai. Ethylene insensitive3-like2 (oseil2) confers stress sensitivity by regulating osburp16, the β subunit of polygalacturonase (pg1β-like) subfamily gene in rice. Plant science : an international journal of experimental plant biology, 292:110353, Mar 2020. URL: https://doi.org/10.1016/j.plantsci.2019.110353, doi:10.1016/j.plantsci.2019.110353. This article has 44 citations.

13. (jin2020ethyleneinsensitive3like2(oseil2) pages 10-13): Jing Jin, Jianli Duan, Chi Shan, Zhiling Mei, Haiying Chen, Huafeng Feng, Jian Zhu, and Weiming Cai. Ethylene insensitive3-like2 (oseil2) confers stress sensitivity by regulating osburp16, the β subunit of polygalacturonase (pg1β-like) subfamily gene in rice. Plant science : an international journal of experimental plant biology, 292:110353, Mar 2020. URL: https://doi.org/10.1016/j.plantsci.2019.110353, doi:10.1016/j.plantsci.2019.110353. This article has 44 citations.

14. (chigumba2022discoveryandbiosynthesis pages 4-5): Desnor N. Chigumba, L. S. Mydy, F. de Waal, Wenjie Li, Khadija Shafiq, Jesse W. Wotring, Osama G. Mohamed, Tim Mladenovic, A. Tripathi, J. Sexton, S. Kautsar, M. Medema, and R. Kersten. Discovery and biosynthesis of cyclic plant peptides via autocatalytic cyclases. JournalArticle, Jan 2022. URL: https://doi.org/10.7302/24583, doi:10.7302/24583. This article has 84 citations.

15. (chigumba2022discoveryandbiosynthesis pages 3-4): Desnor N. Chigumba, L. S. Mydy, F. de Waal, Wenjie Li, Khadija Shafiq, Jesse W. Wotring, Osama G. Mohamed, Tim Mladenovic, A. Tripathi, J. Sexton, S. Kautsar, M. Medema, and R. Kersten. Discovery and biosynthesis of cyclic plant peptides via autocatalytic cyclases. JournalArticle, Jan 2022. URL: https://doi.org/10.7302/24583, doi:10.7302/24583. This article has 84 citations.

16. (chekan2024plantpeptides– pages 3-4): Jonathan R. Chekan, Lisa S. Mydy, Michael A. Pasquale, and Roland D. Kersten. Plant peptides – redefining an area of ribosomally synthesized and post-translationally modified peptides. Natural product reports, 41:1020-1059, Feb 2024. URL: https://doi.org/10.1039/d3np00042g, doi:10.1039/d3np00042g. This article has 62 citations and is from a peer-reviewed journal.

17. (chekan2024plantpeptides– pages 7-8): Jonathan R. Chekan, Lisa S. Mydy, Michael A. Pasquale, and Roland D. Kersten. Plant peptides – redefining an area of ribosomally synthesized and post-translationally modified peptides. Natural product reports, 41:1020-1059, Feb 2024. URL: https://doi.org/10.1039/d3np00042g, doi:10.1039/d3np00042g. This article has 62 citations and is from a peer-reviewed journal.

18. (jin2020ethyleneinsensitive3like2(oseil2) pages 4-7): Jing Jin, Jianli Duan, Chi Shan, Zhiling Mei, Haiying Chen, Huafeng Feng, Jian Zhu, and Weiming Cai. Ethylene insensitive3-like2 (oseil2) confers stress sensitivity by regulating osburp16, the β subunit of polygalacturonase (pg1β-like) subfamily gene in rice. Plant science : an international journal of experimental plant biology, 292:110353, Mar 2020. URL: https://doi.org/10.1016/j.plantsci.2019.110353, doi:10.1016/j.plantsci.2019.110353. This article has 44 citations.

## Artifacts

- [Edison artifact artifact-00](PTHR31458-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](PTHR31458-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. ren2023genomewideidentificationand pages 1-2
2. chigumba2022discoveryandbiosynthesis pages 7-7
3. ren2023genomewideidentificationand pages 4-6
4. ren2023genomewideidentificationand pages 2-4
5. chigumba2022discoveryandbiosynthesis pages 1-3
6. wang2025largescaletranscriptomemining pages 2-3
7. chigumba2022discoveryandbiosynthesis pages 3-4
8. chigumba2022discoveryandbiosynthesis pages 6-6
9. mydy2021plantcoppermetalloenzymes pages 3-4
10. mydy2021plantcoppermetalloenzymes pages 2-3
11. chigumba2022discoveryandbiosynthesis pages 5-6
12. chigumba2022discoveryandbiosynthesis pages 4-5
13. https://doi.org/10.1007/s12298-023-01393-7,
14. https://doi.org/10.7302/24583,
15. https://doi.org/10.1016/j.plantsci.2019.110353,
16. https://doi.org/10.1038/s41467-025-59428-4,
17. https://doi.org/10.3389/fpls.2021.692108,
18. https://doi.org/10.1039/d3np00042g,