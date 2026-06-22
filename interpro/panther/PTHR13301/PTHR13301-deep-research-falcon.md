---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-21T20:31:59.745100'
end_time: '2026-06-21T20:41:56.379533'
duration_seconds: 596.63
template_file: templates/interpro_family_research.md
template_variables:
  interpro_id: PTHR13301
  interpro_name: Plant Cellulose Synthase/Glycosyltransferase
  interpro_short_name: Plant_Cellulose_Synth/GTase
  interpro_type: family
  interpro_integrated: None (top-level entry)
  member_databases: Not specified
  n_proteins: '18182'
  n_taxa: '1180'
  n_subfamilies: '82'
  interpro2go_terms: None mapped (no InterPro2GO terms for this entry)
  interpro_description: The glycosyltransferase 2 family, specifically the plant cellulose
    synthase and cellulose synthase-like subfamilies, are responsible for the biosynthesis
    of cell wall polysaccharides in plants. Members of this family catalyze the formation
    of beta-1,4-glucan microfibrils, which are crucial for cell wall formation and
    plant structural integrity. Some members also synthesize mixed-linked glucans,
    essential for the structure of grass and cereal cell walls. These enzymes are
    involved in primary and secondary cell wall formation, affecting cell expansion,
    elongation, and complex wall patterning in various plant tissues.
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
  path: PTHR13301-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: PTHR13301-deep-research-falcon_artifacts/artifact-01.md
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
- **Accession:** PTHR13301
- **Name:** Plant Cellulose Synthase/Glycosyltransferase
- **Short name:** Plant_Cellulose_Synth/GTase
- **Entry type:** family
- **Integrated into / parent:** None (top-level entry)
- **Member database signatures:** Not specified
- **Scale:** 18182 proteins across 1180 taxa, 82 subfamilies
- **Current InterPro2GO terms (the mappings under review):** None mapped (no InterPro2GO terms for this entry)
- **InterPro description:** The glycosyltransferase 2 family, specifically the plant cellulose synthase and cellulose synthase-like subfamilies, are responsible for the biosynthesis of cell wall polysaccharides in plants. Members of this family catalyze the formation of beta-1,4-glucan microfibrils, which are crucial for cell wall formation and plant structural integrity. Some members also synthesize mixed-linked glucans, essential for the structure of grass and cereal cell walls. These enzymes are involved in primary and secondary cell wall formation, affecting cell expansion, elongation, and complex wall patterning in various plant tissues.

### Why entry type matters:

An entry of type **domain**, **repeat**, or **homologous_superfamily** identifies a
structural/functional *module*, not a whole-protein function. GO terms describing a
whole-protein activity or process attached to such a module systematically over-annotate
every protein that merely *contains* the module. An entry of type **family** is more
likely to support whole-protein function terms, but only if the family is functionally
homogeneous.

## Research Target

Provide a comprehensive, citation-backed research report on the InterPro entry
**PTHR13301 (Plant Cellulose Synthase/Glycosyltransferase)**, structured to support GO annotation review.

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
- **Accession:** PTHR13301
- **Name:** Plant Cellulose Synthase/Glycosyltransferase
- **Short name:** Plant_Cellulose_Synth/GTase
- **Entry type:** family
- **Integrated into / parent:** None (top-level entry)
- **Member database signatures:** Not specified
- **Scale:** 18182 proteins across 1180 taxa, 82 subfamilies
- **Current InterPro2GO terms (the mappings under review):** None mapped (no InterPro2GO terms for this entry)
- **InterPro description:** The glycosyltransferase 2 family, specifically the plant cellulose synthase and cellulose synthase-like subfamilies, are responsible for the biosynthesis of cell wall polysaccharides in plants. Members of this family catalyze the formation of beta-1,4-glucan microfibrils, which are crucial for cell wall formation and plant structural integrity. Some members also synthesize mixed-linked glucans, essential for the structure of grass and cereal cell walls. These enzymes are involved in primary and secondary cell wall formation, affecting cell expansion, elongation, and complex wall patterning in various plant tissues.

### Why entry type matters:

An entry of type **domain**, **repeat**, or **homologous_superfamily** identifies a
structural/functional *module*, not a whole-protein function. GO terms describing a
whole-protein activity or process attached to such a module systematically over-annotate
every protein that merely *contains* the module. An entry of type **family** is more
likely to support whole-protein function terms, but only if the family is functionally
homogeneous.

## Research Target

Provide a comprehensive, citation-backed research report on the InterPro entry
**PTHR13301 (Plant Cellulose Synthase/Glycosyltransferase)**, structured to support GO annotation review.

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


# InterPro Family Research Report: PTHR13301 (Plant Cellulose Synthase/Glycosyltransferase)

## Executive Summary

**InterPro Entry:** PTHR13301  
**Entry Type:** Family (top-level PANTHER family)  
**Scale:** 18,182 proteins across 1,180 taxa, 82 subfamilies  
**Current InterPro2GO Mappings:** None  
**Overall Verdict:** The absence of InterPro2GO mappings is **APPROPRIATE AND SHOULD BE MAINTAINED**. This is a functionally heterogeneous superfamily that encompasses cellulose synthases and multiple distinct cellulose synthase-like (CSL) subfamilies with divergent polysaccharide products.

---

## 1. Family Definition and Biochemistry

### Structural Fold and Catalytic Domain Architecture

PTHR13301 represents the plant cellulose synthase superfamily, encompassing both cellulose synthase (CESA) and cellulose synthase-like (CSL) proteins. All members belong to the glycosyltransferase family GT2 and share a conserved catalytic core architecture (daras2021updatinginsightsinto pages 4-6, daras2021updatinginsightsinto pages 1-2, daras2021updatinginsightsinto pages 2-4).

**Core structural features:**

- **GT-A fold catalytic domain:** The catalytic domain consists of a 7-stranded β-sheet core flanked by α-helices, creating an active site pocket for substrate and acceptor binding (qiao2021structureofarabidopsis pages 1-1, daras2021updatinginsightsinto pages 6-8). This GT-A-like fold is sandwiched between plant-specific regions in CESA proteins (qiao2021structureofarabidopsis pages 1-1).

- **Conserved catalytic motifs:** The canonical D,D,D,QXXRW motif is conserved across the family (huang2023pointmutationsin pages 1-2, qiao2021structureofarabidopsis pages 1-1, zhang2021structuralinsightsinto pages 1-2, daras2021updatinginsightsinto pages 4-6). The first two aspartic acid (D) residues coordinate UDP of UDP-glucose and the essential divalent cation (Mn²⁺); the third D serves as the catalytic base. The QXXRW motif (particularly the arginine) coordinates UDP, while tryptophan (W) forms van der Waals interactions with terminal glucan residues of the acceptor chain (daras2021updatinginsightsinto pages 4-6, verma2023insightsintosubstrate pages 1-5).

- **Additional conserved motifs:** DDG, DXD, and TED motifs within the catalytic domain participate in donor and acceptor UDP-glucose binding, glucan chain polymerization, and chain elongation (huang2023pointmutationsin pages 1-2, daras2021updatinginsightsinto pages 4-6).

- **Transmembrane architecture:** CESA proteins contain seven transmembrane helices (TMs) that form a channel facilitating translocation of newly synthesized glucan chains across the membrane (zhang2021structuralinsightsinto pages 1-2, daras2021updatinginsightsinto pages 6-8). TMs 1-6 cluster around three cytosolic interface helices (IF1-3) (daras2021updatinginsightsinto pages 6-8).

- **Plant-specific domains:** 
  - **Plant-Conserved Region (PCR):** Two antiparallel α-helices essential for CESA homotrimerization and CSC assembly; located at the periphery of the GT domain and stabilizes trimeric assemblies (qiao2021structureofarabidopsis pages 1-1, zhang2021structuralinsightsinto pages 1-2, daras2021updatinginsightsinto pages 4-6, daras2021updatinginsightsinto pages 6-8).
  - **Class-Specific Region (CSR):** A highly variable, often disordered region involved in protein-protein interactions and potentially in interactions with non-CESA auxiliary proteins or between rosette units (zhang2021structuralinsightsinto pages 1-2, daras2021updatinginsightsinto pages 4-6, daras2021updatinginsightsinto pages 6-8).

- **N-terminal domain:** CESA and some CSL proteins (notably CSLD) possess an N-terminal RING-type zinc finger motif implicated in protein oligomerization (zhang2021structuralinsightsinto pages 1-2, daras2021updatinginsightsinto pages 4-6).

**Critical structural distinction:** While CESA proteins possess the full complement of PCR, CSR, and N-terminal zinc finger domains, the more divergent CSL subfamilies CSLA and CSLC **lack PCR and CSR** despite retaining the catalytic GT2 core (daras2021updatinginsightsinto pages 4-6, daras2021updatinginsightsinto pages 6-8). This structural divergence correlates with functional divergence.

### Mechanism

These enzymes catalyze glycosyl transfer from nucleotide-sugar donors (primarily UDP-glucose or GDP-mannose, depending on subfamily) to growing polysaccharide chains via an inverting mechanism. CESA couples cellulose synthesis with secretion: the catalytic GT domain packs against the channel-forming transmembrane region, and newly synthesized glucan chains are translocated through the transmembrane pore into the apoplast or cell wall (verma2023insightsintosubstrate pages 1-5). A conserved FxVTxK "gating loop" adjacent to interface helix 3 (IF3) functions in substrate positioning and access control (verma2023insightsintosubstrate pages 1-5, daras2021updatinginsightsinto pages 10-11).

---

## 2. InterPro2GO Mapping Appropriateness

**Current status:** PTHR13301 has **no InterPro2GO mappings**.

**Evaluation:** This is **CORRECT and should be maintained**. The family is **too functionally heterogeneous** to support subfamily-specific GO terms at the top family level.

### Why subfamily-specific terms would over-annotate:

The PTHR13301 family encompasses multiple biochemically distinct subfamilies that synthesize **different polysaccharide products**:

| Subfamily | Polysaccharide product(s) synthesized | Taxonomic distribution | Key distinguishing features | PCR/CSR domains |
|---|---|---|---|---|
| CESA | Cellulose; β-1,4-glucan chains assembled into cellulose microfibrils | Broadly across land plants; core primary-wall and secondary-wall isoforms in both monocots and dicots | GT2 cellulose synthases with canonical D,D,D,QXXRW motif; seven transmembrane helices; N-terminal RING-type zinc finger; catalytic GT-A-like core flanked by plant-conserved region (PCR) and class-specific region (CSR); forms trimeric units within rosette cellulose synthase complexes (qiao2021structureofarabidopsis pages 1-1, zhang2021structuralinsightsinto pages 1-2, daras2021updatinginsightsinto pages 4-6, daras2021updatinginsightsinto pages 6-8) | Yes / Yes (daras2021updatinginsightsinto pages 4-6, daras2021updatinginsightsinto pages 6-8) |
| CSLA | Mannan and glucomannan backbones (heteromannans) | Both monocots and dicots; broadly across plant kingdom | Experimentally supported mannan synthases; shorter and more diverged than CESA; catalytic core resembles CesA/BcsA-related GT2 enzymes but lacks the plant-specific full CesA architecture; structurally closer to primitive GT2 backbone synthases (daras2021updatinginsightsinto pages 4-6, daras2021updatinginsightsinto pages 2-4, griessosowski2023impactofcellulose pages 7-10, daras2021updatinginsightsinto pages 6-8) | No / No (daras2021updatinginsightsinto pages 4-6, daras2021updatinginsightsinto pages 6-8) |
| CSLB | Poorly characterized; specific polysaccharide product not firmly established | Dicot/eudicot-specific | Part of divergent CSL branch; predicted structural congruence with CesA-like GT2 catalytic core, but biochemical function remains unclear in the cited review literature (daras2021updatinginsightsinto pages 4-6, daras2021updatinginsightsinto pages 2-4, daras2021updatinginsightsinto pages 6-8) | Predicted Yes / Yes (daras2021updatinginsightsinto pages 6-8) |
| CSLC | β-1,4-glucan backbone of xyloglucan or related glucans | Both monocots and dicots | Includes enzymes involved in xyloglucan backbone synthesis; like CSLA, relatively short and divergent; lacks PCR and CSR despite catalytic similarity to CesA-like GT2 core (daras2021updatinginsightsinto pages 4-6, daras2021updatinginsightsinto pages 2-4, daras2021updatinginsightsinto pages 6-8) | No / No (daras2021updatinginsightsinto pages 4-6, daras2021updatinginsightsinto pages 6-8) |
| CSLD | Reported roles in synthesis associated with tip-growing cells; evidence cited for xylan and homogalacturonan involvement, and also β-1,4-glucan/cellulose-like activity in some contexts | Both monocots and dicots | Closest CSL clade to CESA; N-terminal RING-type zinc finger present; high structural similarity to CesA; implicated in tip growth and functionally distinct from canonical cellulose-synthesizing CESAs; evidence indicates subfamily-level functional complexity rather than a single universal product assignment (daras2021updatinginsightsinto pages 4-6, daras2021updatinginsightsinto pages 2-4, daras2021updatinginsightsinto pages 6-8) | Predicted Yes / Yes (daras2021updatinginsightsinto pages 4-6, daras2021updatinginsightsinto pages 6-8) |
| CSLE | Poorly characterized; specific polysaccharide product not firmly established | Both monocots and dicots | Present in both major angiosperm clades in Arabidopsis/rice comparison; function remains poorly characterized in the cited review literature; predicted CesA-like structural organization for catalytic region (daras2021updatinginsightsinto pages 4-6, daras2021updatinginsightsinto pages 2-4, daras2021updatinginsightsinto pages 6-8) | Predicted Yes / Yes (daras2021updatinginsightsinto pages 6-8) |
| CSLF | Mixed-linkage β-glucan (MLG; β-(1,3;1,4)-D-glucan) | Monocot-specific | Monocot-expanded subfamily associated with grass/cereal wall specializations; CesA-like GT2 architecture predicted; functionally distinct from cellulose synthases despite related catalytic core (daras2021updatinginsightsinto pages 4-6, daras2021updatinginsightsinto pages 2-4, liu2022genomewidebioinformaticsanalysis pages 1-2, daras2021updatinginsightsinto pages 6-8) | Predicted Yes / Yes (daras2021updatinginsightsinto pages 6-8) |
| CSLG | Poorly characterized; specific polysaccharide product not firmly established | Dicot/eudicot-specific | Dicot-specific CSL clade; function remains poorly characterized in cited sources; predicted to retain CesA-like catalytic/channel architecture more than CSLA/CSLC do (daras2021updatinginsightsinto pages 4-6, daras2021updatinginsightsinto pages 2-4, daras2021updatinginsightsinto pages 6-8) | Predicted Yes / Yes (daras2021updatinginsightsinto pages 6-8) |
| CSLH | Mixed-linkage β-glucan (MLG; β-(1,3;1,4)-D-glucan) | Monocot-specific | Monocot-specific subfamily involved in MLG synthesis; contributes to grass-type wall diversification; predicted CesA-like GT2 structural framework (daras2021updatinginsightsinto pages 4-6, daras2021updatinginsightsinto pages 2-4, liu2022genomewidebioinformaticsanalysis pages 1-2, daras2021updatinginsightsinto pages 6-8) | Predicted Yes / Yes (daras2021updatinginsightsinto pages 6-8) |


*Table: This table summarizes the major functional and structural differences across the plant cellulose synthase superfamily subfamilies relevant to GO review. It is useful for judging whether any whole-family GO term could apply uniformly across PTHR13301, which clearly spans multiple biochemically distinct subfamilies.*

**Problematic GO term scenarios (if they were mapped at family level):**

1. **"Cellulose synthase activity" (GO:0016759) or "cellulose biosynthetic process" (GO:0030244):** These terms are **only valid for CESA subfamily members**. Applying them to the entire family would falsely annotate CSLA (mannan/glucomannan synthases), CSLC (xyloglucan backbone synthases), CSLF/CSLH (mixed-linkage glucan synthases), and other CSL proteins that do **not** synthesize cellulose (daras2021updatinginsightsinto pages 4-6, daras2021updatinginsightsinto pages 2-4, griessosowski2023impactofcellulose pages 7-10, liu2022genomewidebioinformaticsanalysis pages 1-2, daras2021updatinginsightsinto pages 6-8).

2. **"Mannan synthase activity" or "glucomannan biosynthetic process":** Valid only for **CSLA subfamily**, not for CESA or other CSL clades (daras2021updatinginsightsinto pages 4-6, griessosowski2023impactofcellulose pages 7-10, griessosowski2023impactofcellulose pages 4-7).

3. **"Mixed-linkage glucan biosynthetic process":** Valid only for **CSLF and CSLH subfamilies**, which are **monocot-specific** (grasses and cereals). This would inappropriately annotate all dicot family members (daras2021updatinginsightsinto pages 4-6, daras2021updatinginsightsinto pages 2-4, liu2022genomewidebioinformaticsanalysis pages 1-2).

4. **"Plasma membrane" (GO:0005886):** CESA cellulose synthases function at the plasma membrane, assembling into rosette complexes that synthesize cellulose at the cell surface (huang2023pointmutationsin pages 1-2, qiao2021structureofarabidopsis pages 1-1, zhang2021structuralinsightsinto pages 1-2). However, many CSL hemicellulose synthases localize to and function in the **Golgi apparatus**, where non-cellulosic polysaccharides are assembled (daras2021updatinginsightsinto pages 1-2, daras2021updatinginsightsinto pages 13-14). A plasma membrane term at the family level would mis-annotate Golgi-localized CSLs.

5. **"UDP-glucose binding" (GO:0070052):** While strongly supported for CESA (qiao2021structureofarabidopsis pages 1-1, verma2023insightsintosubstrate pages 1-5), substrate usage diverges across CSL subfamilies. CSLA mannan synthases likely use GDP-mannose; mixed specificities exist across the family (daras2021updatinginsightsinto pages 4-6, daras2021updatinginsightsinto pages 2-4).

### Acceptable but low-information terms:

Only extremely **generic terms** would be true across all PTHR13301 members:

- **"Glycosyltransferase activity" (GO:0016757):** True, as all are GT2 enzymes, but this provides minimal functional information (daras2021updatinginsightsinto pages 4-6, daras2021updatinginsightsinto pages 1-2).
- **"Membrane" (GO:0016020) or "integral component of membrane":** Likely true for most members (zhang2021structuralinsightsinto pages 1-2, daras2021updatinginsightsinto pages 4-6), but again, too generic to be useful for GO annotation purposes.

These terms carry so little specificity that they do not justify InterPro2GO mapping.

| Potential GO term type | Appropriate for all PTHR13301 members? | Applies to which subfamilies | Assessment of scope | Recommendation |
|---|---|---|---|---|
| **UDP-glucose binding** | No | Strongly supported for **CESA** cellulose synthases; not uniformly supported across the wider CSL superfamily because substrate use diverges among CSL clades (e.g., mannan/glucomannan, xyloglucan, mixed-linkage glucan synthases) (qiao2021structureofarabidopsis pages 1-1, daras2021updatinginsightsinto pages 4-6, daras2021updatinginsightsinto pages 2-4, verma2023insightsintosubstrate pages 1-5) | Too specific to one donor/substrate class; overstates biochemical uniformity across the family | **RESTRICT to subfamily** |
| **Transferase activity / glycosyltransferase activity** | Yes, at a high level | CESA and CSL proteins are all GT2-family glycosyltransferases, although product specificity differs greatly (qiao2021structureofarabidopsis pages 1-1, daras2021updatinginsightsinto pages 4-6, daras2021updatinginsightsinto pages 1-2, daras2021updatinginsightsinto pages 6-8) | Broad but biologically true for the family; however, very generic and low-information for GO review | **TOO_GENERIC** |
| **Cellulose synthase activity** | No | **CESA** only; CSL subfamilies synthesize distinct non-cellulosic backbones such as mannan/glucomannan, xyloglucan backbone, or mixed-linkage glucan (daras2021updatinginsightsinto pages 4-6, daras2021updatinginsightsinto pages 2-4, griessosowski2023impactofcellulose pages 7-10, daras2021updatinginsightsinto pages 6-8) | Overly specific and false for much of the family | **RESTRICT to subfamily** |
| **Cellulose biosynthetic process** | No | **CESA** only; not valid for CSLA/CSLC/CSLF/CSLH and other divergent CSL clades (daras2021updatinginsightsinto pages 4-6, daras2021updatinginsightsinto pages 2-4, daras2021updatinginsightsinto pages 6-8) | Process term is over-broad if mapped to top-level family because many members synthesize other wall polysaccharides | **MARK_AS_OVER_ANNOTATED** |
| **Plant-type cell wall organization / biogenesis** | No | Broadly relevant to many CESA/CSL proteins, but not demonstrated as a direct conserved process role for every matched protein, especially poorly characterized CSLB/E/G members (daras2021updatinginsightsinto pages 1-2, daras2021updatinginsightsinto pages 2-4, daras2021updatinginsightsinto pages 6-8, yokoyama2020agenomicperspective pages 1-3) | Process term is too broad and indirect for a functionally heterogeneous family | **MARK_AS_OVER_ANNOTATED** |
| **Cell wall polysaccharide biosynthetic process** | No | Broadly relevant to many characterized subfamilies: CESA, CSLA, CSLC, CSLD, CSLF, CSLH; but product identity differs and some subfamilies remain poorly characterized (daras2021updatinginsightsinto pages 4-6, daras2021updatinginsightsinto pages 2-4, liu2022genomewidebioinformaticsanalysis pages 1-2, daras2021updatinginsightsinto pages 6-8) | Closer to truth than cellulose-specific terms, but still too broad for all members because of incomplete characterization and major biochemical divergence | **RESTRICT to subfamily** |
| **Membrane** | Probably yes for most or all | CESA and most CSLs are integral membrane GT2 enzymes with multiple transmembrane helices (zhang2021structuralinsightsinto pages 1-2, daras2021updatinginsightsinto pages 4-6, daras2021updatinginsightsinto pages 6-8) | Likely true but too generic to be useful as an InterPro2GO family mapping | **TOO_GENERIC** |
| **Plasma membrane** | No | Best supported for **CESA** cellulose synthases, which synthesize cellulose at the plasma membrane; many non-cellulosic CSL enzymes function in Golgi/endomembrane contexts instead (huang2023pointmutationsin pages 1-2, qiao2021structureofarabidopsis pages 1-1, daras2021updatinginsightsinto pages 1-2, daras2021updatinginsightsinto pages 13-14) | Subcellular localization differs across family; PM term would mis-annotate Golgi-localized CSLs | **MARK_AS_OVER_ANNOTATED** |
| **Golgi apparatus / Golgi membrane** | No | More applicable to several **CSL** hemicellulose synthases; not appropriate for plasma-membrane cellulose synthases (daras2021updatinginsightsinto pages 1-2, liu2022genomewidebioinformaticsanalysis pages 1-2, daras2021updatinginsightsinto pages 13-14) | Compartment term leaks across subfamilies with different trafficking and synthesis sites | **MARK_AS_OVER_ANNOTATED** |
| **Mixed-linkage glucan biosynthetic process** | No | **CSLF**, **CSLH** (and in some literature CSLJ) in monocot lineages (daras2021updatinginsightsinto pages 4-6, daras2021updatinginsightsinto pages 2-4, liu2022genomewidebioinformaticsanalysis pages 1-2) | Taxonomically restricted and subfamily-specific; invalid for dicot and non-MLG synthases | **RESTRICT to subfamily** |
| **Mannan / glucomannan biosynthetic process** | No | **CSLA** subfamily (daras2021updatinginsightsinto pages 4-6, daras2021updatinginsightsinto pages 2-4, griessosowski2023impactofcellulose pages 7-10) | Correct for a well-defined subfamily, not the whole PTHR13301 family | **RESTRICT to subfamily** |
| **Xyloglucan biosynthetic process / xyloglucan glucan synthase activity** | No | **CSLC** subfamily (daras2021updatinginsightsinto pages 4-6, daras2021updatinginsightsinto pages 2-4) | Correct only for one divergent CSL clade | **RESTRICT to subfamily** |
| **Cellulose synthase complex / rosette complex component** | No | **CESA** only; these trimeric/rosette assemblies are structurally characterized for plant cellulose synthases, not for the whole CSL family (huang2023pointmutationsin pages 1-2, qiao2021structureofarabidopsis pages 1-1, zhang2021structuralinsightsinto pages 1-2, daras2021updatinginsightsinto pages 6-8) | Whole-protein complex term specific to a subset of family members | **RESTRICT to subfamily** |


*Table: This table evaluates which commonly proposed GO term types would or would not be appropriate for the broad PTHR13301 family. It is useful for GO review because it highlights that the family is biochemically and taxonomically heterogeneous, so most specific terms should be restricted to child subfamilies rather than mapped at the top family level.*

---

## 3. Functional Divergence Across the Family

### Overview

PTHR13301 is **not a functionally homogeneous family**. It represents an ancient glycosyltransferase superfamily that has undergone **extensive neo-functionalization** to produce structurally and biochemically distinct polysaccharide products (daras2021updatinginsightsinto pages 4-6, daras2021updatinginsightsinto pages 2-4, yokoyama2020agenomicperspective pages 1-3).

### Major Subfamilies and Their Distinct Functions

**1. CESA (Cellulose Synthase):**
- **Product:** β-1,4-glucan chains assembled into crystalline cellulose microfibrils
- **Function:** Primary and secondary cell wall cellulose biosynthesis
- **Localization:** Plasma membrane, within rosette cellulose synthase complexes (CSCs)
- **Assembly:** Homotrimeric or heterotrimeric units forming six-lobed rosettes
- **Experimental evidence:** Extensive structural, genetic, and biochemical characterization (huang2023pointmutationsin pages 1-2, qiao2021structureofarabidopsis pages 1-1, zhang2021structuralinsightsinto pages 1-2, daras2021updatinginsightsinto pages 4-6, daras2021updatinginsightsinto pages 6-8, daras2021updatinginsightsinto pages 8-10)

**2. CSLA (Cellulose Synthase-Like A):**
- **Product:** Mannan and glucomannan backbones (heteromannans with β-1,4-linked mannose ± glucose)
- **Function:** Hemicellulose synthesis
- **Localization:** Golgi apparatus
- **Key distinction:** Lacks PCR and CSR domains; shorter and structurally divergent from CESA (daras2021updatinginsightsinto pages 4-6, daras2021updatinginsightsinto pages 2-4, griessosowski2023impactofcellulose pages 7-10, griessosowski2023impactofcellulose pages 4-7, daras2021updatinginsightsinto pages 6-8)
- **Experimental evidence:** In vitro and in vivo mannan/glucomannan synthesis demonstrated (daras2021updatinginsightsinto pages 4-6, griessosowski2023impactofcellulose pages 7-10)

**3. CSLC (Cellulose Synthase-Like C):**
- **Product:** β-1,4-glucan backbone of xyloglucan (or related glucans)
- **Function:** Xyloglucan backbone synthesis in hemicelluloses
- **Key distinction:** Like CSLA, lacks PCR and CSR; structurally divergent (daras2021updatinginsightsinto pages 4-6, daras2021updatinginsightsinto pages 2-4, daras2021updatinginsightsinto pages 6-8)

**4. CSLD (Cellulose Synthase-Like D):**
- **Product/Function:** Complex and potentially subfamily-diverse; reported roles include xylan, homogalacturonan, and possibly β-1,4-glucan synthesis in tip-growing cells
- **Key distinction:** Retains RING-type zinc finger; closest CSL clade to CESA phylogenetically; recent evidence suggests some CSLD proteins can complement CESA function and have β-1,4-glucan synthase activity (daras2021updatinginsightsinto pages 4-6, daras2021updatinginsightsinto pages 2-4)
- **Caveat:** Functional assignments within CSLD appear heterogeneous even at the subfamily level

**5. CSLF and CSLH (Cellulose Synthase-Like F/H):**
- **Product:** Mixed-linkage β-glucan (MLG; β-(1,3;1,4)-D-glucan)
- **Function:** Synthesis of MLG, a hemicellulose critical for grass and cereal cell walls
- **Taxonomic restriction:** **Monocot-specific** (grasses, cereals)
- **Experimental evidence:** Well-supported by genetic and biochemical studies (daras2021updatinginsightsinto pages 4-6, daras2021updatinginsightsinto pages 2-4, liu2022genomewidebioinformaticsanalysis pages 1-2)

**6. CSLB, CSLE, and CSLG:**
- **Status:** Poorly characterized to date; specific polysaccharide products not firmly established in the reviewed literature (daras2021updatinginsightsinto pages 4-6, daras2021updatinginsightsinto pages 2-4, daras2021updatinginsightsinto pages 6-8)
- **Taxonomic restriction:** CSLB and CSLG are **dicot-specific** (daras2021updatinginsightsinto pages 4-6, daras2021updatinginsightsinto pages 2-4)

### Evidence for Neo-Functionalization

Phylogenetic and structural analyses demonstrate that:

- **CSLA and CSLC** are highly diverged from CESA and other CSL clades, likely representing primitive forms that diverged from an ancestral bacterial cellulose synthase gene before the evolution of plant-specific PCR/CSR domains (daras2021updatinginsightsinto pages 4-6, daras2021updatinginsightsinto pages 2-4, daras2021updatinginsightsinto pages 6-8).

- The remaining CSL clades (CSLB/D/E/F/G/H) share higher sequence similarity to CESA and possess predicted PCR and CSR domains, but have evolved distinct substrate specificities and polysaccharide products (daras2021updatinginsightsinto pages 4-6, daras2021updatinginsightsinto pages 6-8).

### No Evidence for Catalytically Inactive (Pseudo-Enzyme) Members

The literature reviewed does not report catalytically dead members that retain the fold but have lost activity within PTHR13301. However, mutational studies show that point mutations in conserved catalytic residues (D,D,D, QXXRW) result in severe loss-of-function or dominant-negative phenotypes, confirming the essentiality of these residues for catalysis (huang2023pointmutationsin pages 1-2, daras2021updatinginsightsinto pages 8-10, daras2021updatinginsightsinto pages 10-11, daras2021updatinginsightsinto pages 11-13).

---

## 4. Taxonomic Scope

### Distribution Across Plant Clades

PTHR13301 is **broadly distributed across land plants**, with 18,182 proteins across 1,180 taxa (per InterPro metadata). The family is present in:

- **Bryophytes** (mosses, liverworts)
- **Angiosperms** (both monocots and dicots)
- Likely **pteridophytes** and **gymnosperms** (inferred from broad land plant distribution)

**Subfamily-specific taxonomic restrictions:**

- **CESA, CSLA, CSLC, CSLD, CSLE:** Present in **both monocots and dicots** (daras2021updatinginsightsinto pages 4-6, daras2021updatinginsightsinto pages 2-4, liu2022genomewidebioinformaticsanalysis pages 1-2).

- **CSLF and CSLH:** **Monocot-specific** (grasses and cereals); absent from dicots (daras2021updatinginsightsinto pages 4-6, daras2021updatinginsightsinto pages 2-4, liu2022genomewidebioinformaticsanalysis pages 1-2).

- **CSLB and CSLG:** **Dicot/eudicot-specific**; absent from monocots (daras2021updatinginsightsinto pages 4-6, daras2021updatinginsightsinto pages 2-4).

### Taxonomic Scope Implications for GO Terms

**Critical issue:** Subfamily-specific process and component GO terms **do not hold across all taxa** matched by PTHR13301:

1. **Mixed-linkage glucan biosynthetic process** terms are **invalid for all dicot proteins** matched by this family, as CSLF/CSLH are monocot-specific.

2. **Grass-specific cell wall components or processes** would leak into bryophyte, gymnosperm, and dicot proteins if mapped at the family level.

3. **Plasma membrane localization** (CESA) vs. **Golgi localization** (many CSLs) differs within the same family, meaning cellular component terms inappropriately leak across subfamilies with different synthesis sites.

**Evolutionary context:** The cellulose synthase superfamily predates the monocot/dicot split, but **lineage-specific expansions and neo-functionalization** have created clade-restricted subfamilies (daras2021updatinginsightsinto pages 4-6, daras2021updatinginsightsinto pages 2-4, yokoyama2020agenomicperspective pages 1-3). This phylogenetic pattern makes top-level family GO mappings prone to over-annotation.

---

## 5. Over-Annotation Verdict and GO Action Recommendations

### Summary Verdict

**PTHR13301 InterPro2GO status is SOUND AS-IS (no mappings).**

This top-level PANTHER family is **too functionally and taxonomically heterogeneous** to support meaningful subfamily-specific GO term mappings. The absence of InterPro2GO mappings is appropriate and should be maintained.

### Detailed Recommendations

#### For InterPro2GO:

**Recommendation: MAINTAIN NO MAPPINGS at the PTHR13301 family level.**

**Rationale:**

1. **Functional heterogeneity:** CESA synthesizes cellulose; CSLA synthesizes mannans; CSLC synthesizes xyloglucan backbone; CSLF/H synthesize mixed-linkage glucan. No single molecular function or biological process term accurately describes all members (daras2021updatinginsightsinto pages 4-6, daras2021updatinginsightsinto pages 2-4, griessosowski2023impactofcellulose pages 7-10, liu2022genomewidebioinformaticsanalysis pages 1-2, daras2021updatinginsightsinto pages 6-8).

2. **Taxonomic restrictions:** CSLF/H (monocot-specific) and CSLB/G (dicot-specific) mean that lineage-specific process terms would mis-annotate proteins in the opposite clade (daras2021updatinginsightsinto pages 4-6, daras2021updatinginsightsinto pages 2-4).

3. **Cellular component divergence:** CESA functions at the plasma membrane in rosette complexes; CSL proteins function in the Golgi. Component terms leak inappropriately across subfamilies (huang2023pointmutationsin pages 1-2, qiao2021structureofarabidopsis pages 1-1, daras2021updatinginsightsinto pages 1-2, daras2021updatinginsightsinto pages 13-14).

4. **Generic terms lack utility:** Only "glycosyltransferase activity" or "membrane" would be universally true, but these are too generic to provide useful annotation (daras2021updatinginsightsinto pages 4-6, daras2021updatinginsightsinto pages 1-2).

#### For Child Subfamilies (if InterPro were to create/annotate them):

If InterPro creates child entries for individual subfamilies (e.g., separate entries for CESA, CSLA, CSLC, CSLF, CSLH), then subfamily-specific GO mappings **would be appropriate**:

- **CESA subfamily:** 
  - Molecular Function: GO:0016759 (cellulose synthase activity)
  - Biological Process: GO:0030244 (cellulose biosynthetic process)
  - Cellular Component: GO:0005886 (plasma membrane); GO:0070762 (cellulose synthase complex)

- **CSLA subfamily:**
  - Molecular Function: mannan synthase activity / glucomannan synthase activity
  - Biological Process: mannan biosynthetic process / glucomannan biosynthetic process
  - Cellular Component: GO:0000139 (Golgi membrane)

- **CSLC subfamily:**
  - Molecular Function: xyloglucan 4-glucosyltransferase activity (or related)
  - Biological Process: xyloglucan biosynthetic process

- **CSLF/CSLH subfamilies:**
  - Molecular Function: 1,3-beta-glucan synthase activity (or mixed-linkage glucan synthase activity)
  - Biological Process: mixed-linkage glucan biosynthetic process
  - **Taxonomic restriction note:** These annotations should be flagged as monocot-specific

**Action pattern for genes matching PTHR13301:**

- **At the family level:** **KEEP_AS_NON_CORE** (do not propagate family-level GO terms, as there are none and should be none)
- **For subfamily-level matches:** **ACCEPT subfamily-specific annotations** (if and when InterPro creates child entries with appropriate GO mappings)

#### Recommendations for InterPro Entry Structure:

**Consider demoting or refining PTHR13301** to better reflect functional diversity:

1. **Option 1:** Maintain PTHR13301 as a top-level family signature **without GO mappings**, but encourage use of subfamily signatures (if available from PANTHER or other member databases) for GO annotation.

2. **Option 2:** If PTHR13301 is used for GO propagation in any downstream databases, add a **curation flag** noting that this family is functionally heterogeneous and that subfamily-level annotations should be preferred.

3. **Do not map whole-protein molecular function or biological process terms to this family-level entry.** Mapping "cellulose biosynthetic process" to PTHR13301 would systematically over-annotate thousands of CSL proteins that synthesize other polysaccharides.

---

## Conclusion

PTHR13301 (Plant Cellulose Synthase/Glycosyltransferase) is a large, ancient, and functionally diverse protein family encompassing cellulose synthases (CESA) and multiple cellulose synthase-like (CSL) subfamilies with distinct polysaccharide products, subcellular localizations, and taxonomic distributions. While all members share a conserved GT2 glycosyltransferase fold and catalytic motifs (D,D,D,QXXRW), they have undergone extensive neo-functionalization:

- **CESA** synthesizes cellulose at the plasma membrane.
- **CSLA** synthesizes mannans/glucomannans in the Golgi.
- **CSLC** synthesizes xyloglucan backbone.
- **CSLF/CSLH** synthesize mixed-linkage glucans (monocot-specific).
- **CSLD** has diverse, possibly subfamily-heterogeneous roles.
- **CSLB/E/G** remain poorly characterized.

The current absence of InterPro2GO mappings for PTHR13301 is **appropriate and should be maintained**. Mapping subfamily-specific GO terms (e.g., "cellulose synthase activity," "mixed-linkage glucan biosynthetic process," "plasma membrane") at the family level would result in systematic over-annotation. Only generic terms like "glycosyltransferase activity" would be universally true, but these lack the specificity to justify mapping.

**Final Recommendation:** **KEEP PTHR13301 WITHOUT InterPro2GO MAPPINGS.** Subfamily-specific GO annotations should be applied at child entry levels (if created) or via other orthogonal annotation methods that can distinguish CESA from CSL subfamilies.

References

1. (daras2021updatinginsightsinto pages 4-6): Gerasimos Daras, Dimitris Templalexis, Fengoula Avgeri, Dikran Tsitsekian, Konstantina Karamanou, and Stamatis Rigas. Updating insights into the catalytic domain properties of plant cellulose synthase (cesa) and cellulose synthase-like (csl) proteins. Molecules, 26:4335, Jul 2021. URL: https://doi.org/10.3390/molecules26144335, doi:10.3390/molecules26144335. This article has 56 citations.

2. (daras2021updatinginsightsinto pages 1-2): Gerasimos Daras, Dimitris Templalexis, Fengoula Avgeri, Dikran Tsitsekian, Konstantina Karamanou, and Stamatis Rigas. Updating insights into the catalytic domain properties of plant cellulose synthase (cesa) and cellulose synthase-like (csl) proteins. Molecules, 26:4335, Jul 2021. URL: https://doi.org/10.3390/molecules26144335, doi:10.3390/molecules26144335. This article has 56 citations.

3. (daras2021updatinginsightsinto pages 2-4): Gerasimos Daras, Dimitris Templalexis, Fengoula Avgeri, Dikran Tsitsekian, Konstantina Karamanou, and Stamatis Rigas. Updating insights into the catalytic domain properties of plant cellulose synthase (cesa) and cellulose synthase-like (csl) proteins. Molecules, 26:4335, Jul 2021. URL: https://doi.org/10.3390/molecules26144335, doi:10.3390/molecules26144335. This article has 56 citations.

4. (qiao2021structureofarabidopsis pages 1-1): Zhu Qiao, Edwin R. Lampugnani, Xin-Fu Yan, Ghazanfar Abbas Khan, Wuan Geok Saw, Patrick Hannah, Feng Qian, Jacob Calabria, Yansong Miao, Gerhard Grüber, Staffan Persson, and Yong-Gui Gao. Structure of arabidopsis cesa3 catalytic domain with its substrate udp-glucose provides insight into the mechanism of cellulose synthesis. Proceedings of the National Academy of Sciences, Mar 2021. URL: https://doi.org/10.1073/pnas.2024015118, doi:10.1073/pnas.2024015118. This article has 51 citations and is from a highest quality peer-reviewed journal.

5. (daras2021updatinginsightsinto pages 6-8): Gerasimos Daras, Dimitris Templalexis, Fengoula Avgeri, Dikran Tsitsekian, Konstantina Karamanou, and Stamatis Rigas. Updating insights into the catalytic domain properties of plant cellulose synthase (cesa) and cellulose synthase-like (csl) proteins. Molecules, 26:4335, Jul 2021. URL: https://doi.org/10.3390/molecules26144335, doi:10.3390/molecules26144335. This article has 56 citations.

6. (huang2023pointmutationsin pages 1-2): Lei Huang, Weiwei Zhang, Xiaohui Li, Christopher J Staiger, and Chunhua Zhang. Point mutations in the catalytic domain disrupt cellulose synthase (cesa6) vesicle trafficking and protein dynamics. The Plant Cell, 35:2654-2677, Apr 2023. URL: https://doi.org/10.1093/plcell/koad110, doi:10.1093/plcell/koad110. This article has 15 citations.

7. (zhang2021structuralinsightsinto pages 1-2): Xiangnan Zhang, Yuan Xue, Zeyuan Guan, Chen Zhou, Yangfan Nie, She Men, Qiang Wang, Cuicui Shen, Delin Zhang, Shuangxia Jin, Lili Tu, Ping Yin, and Xianlong Zhang. Structural insights into homotrimeric assembly of cellulose synthase cesa7 from <i>gossypium hirsutum</i>. Apr 2021. URL: https://doi.org/10.1111/pbi.13571, doi:10.1111/pbi.13571. This article has 77 citations and is from a highest quality peer-reviewed journal.

8. (verma2023insightsintosubstrate pages 1-5): Preeti Verma, Albert L. Kwansa, Ruoya Ho, Yaroslava G. Yingling, and Jochen Zimmer. Insights into substrate coordination and glycosyl transfer of poplar cellulose synthase-8. Structure (London, England : 1993), 31:1166-1173.e6, Aug 2023. URL: https://doi.org/10.1016/j.str.2023.07.010, doi:10.1016/j.str.2023.07.010. This article has 22 citations.

9. (daras2021updatinginsightsinto pages 10-11): Gerasimos Daras, Dimitris Templalexis, Fengoula Avgeri, Dikran Tsitsekian, Konstantina Karamanou, and Stamatis Rigas. Updating insights into the catalytic domain properties of plant cellulose synthase (cesa) and cellulose synthase-like (csl) proteins. Molecules, 26:4335, Jul 2021. URL: https://doi.org/10.3390/molecules26144335, doi:10.3390/molecules26144335. This article has 56 citations.

10. (griessosowski2023impactofcellulose pages 7-10): Impact of cellulose synthase-like enzymes on heteromannan biodiversity This article has 0 citations.

11. (liu2022genomewidebioinformaticsanalysis pages 1-2): Xiaoqing Liu, Hongmei Zhang, Wei Zhang, Wenjing Xu, Songsong Li, Xin Chen, and Huatao Chen. Genome-wide bioinformatics analysis of cellulose synthase gene family in common bean (phaseolus vulgaris l.) and the expression in the pod development. BMC Genomic Data, Jan 2022. URL: https://doi.org/10.1186/s12863-022-01026-0, doi:10.1186/s12863-022-01026-0. This article has 22 citations and is from a peer-reviewed journal.

12. (griessosowski2023impactofcellulose pages 4-7): Impact of cellulose synthase-like enzymes on heteromannan biodiversity This article has 0 citations.

13. (daras2021updatinginsightsinto pages 13-14): Gerasimos Daras, Dimitris Templalexis, Fengoula Avgeri, Dikran Tsitsekian, Konstantina Karamanou, and Stamatis Rigas. Updating insights into the catalytic domain properties of plant cellulose synthase (cesa) and cellulose synthase-like (csl) proteins. Molecules, 26:4335, Jul 2021. URL: https://doi.org/10.3390/molecules26144335, doi:10.3390/molecules26144335. This article has 56 citations.

14. (yokoyama2020agenomicperspective pages 1-3): Ryusuke Yokoyama. A genomic perspective on the evolutionary diversity of the plant cell wall. Plants, 9:1195, Sep 2020. URL: https://doi.org/10.3390/plants9091195, doi:10.3390/plants9091195. This article has 23 citations.

15. (daras2021updatinginsightsinto pages 8-10): Gerasimos Daras, Dimitris Templalexis, Fengoula Avgeri, Dikran Tsitsekian, Konstantina Karamanou, and Stamatis Rigas. Updating insights into the catalytic domain properties of plant cellulose synthase (cesa) and cellulose synthase-like (csl) proteins. Molecules, 26:4335, Jul 2021. URL: https://doi.org/10.3390/molecules26144335, doi:10.3390/molecules26144335. This article has 56 citations.

16. (daras2021updatinginsightsinto pages 11-13): Gerasimos Daras, Dimitris Templalexis, Fengoula Avgeri, Dikran Tsitsekian, Konstantina Karamanou, and Stamatis Rigas. Updating insights into the catalytic domain properties of plant cellulose synthase (cesa) and cellulose synthase-like (csl) proteins. Molecules, 26:4335, Jul 2021. URL: https://doi.org/10.3390/molecules26144335, doi:10.3390/molecules26144335. This article has 56 citations.

## Artifacts

- [Edison artifact artifact-00](PTHR13301-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](PTHR13301-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. qiao2021structureofarabidopsis pages 1-1
2. daras2021updatinginsightsinto pages 6-8
3. verma2023insightsintosubstrate pages 1-5
4. daras2021updatinginsightsinto pages 4-6
5. daras2021updatinginsightsinto pages 1-2
6. daras2021updatinginsightsinto pages 2-4
7. huang2023pointmutationsin pages 1-2
8. zhang2021structuralinsightsinto pages 1-2
9. daras2021updatinginsightsinto pages 10-11
10. griessosowski2023impactofcellulose pages 7-10
11. liu2022genomewidebioinformaticsanalysis pages 1-2
12. griessosowski2023impactofcellulose pages 4-7
13. daras2021updatinginsightsinto pages 13-14
14. yokoyama2020agenomicperspective pages 1-3
15. daras2021updatinginsightsinto pages 8-10
16. daras2021updatinginsightsinto pages 11-13
17. https://doi.org/10.3390/molecules26144335,
18. https://doi.org/10.1073/pnas.2024015118,
19. https://doi.org/10.1093/plcell/koad110,
20. https://doi.org/10.1111/pbi.13571,
21. https://doi.org/10.1016/j.str.2023.07.010,
22. https://doi.org/10.1186/s12863-022-01026-0,
23. https://doi.org/10.3390/plants9091195,