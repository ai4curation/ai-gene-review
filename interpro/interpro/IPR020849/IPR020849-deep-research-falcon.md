---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-20T05:52:29.317693'
end_time: '2026-06-20T06:10:11.636474'
duration_seconds: 1062.32
template_file: templates/interpro_family_research.md
template_variables:
  interpro_id: IPR020849
  interpro_name: Small GTPase, Ras-type
  interpro_short_name: Small_GTPase_Ras-type
  interpro_type: family
  interpro_integrated: None (top-level entry)
  member_databases: 'PTHR24070 (panther: RAS, DI-RAS, AND RHEB FAMILY MEMBERS OF SMALL
    GTPASE SUPERFAMILY)'
  n_proteins: '33550'
  n_taxa: '8233'
  n_subfamilies: '0'
  interpro2go_terms: GO:0005525 GTP binding [F]; GO:0007165 signal transduction [P];
    GO:0016020 membrane [C]
  interpro_description: "Ras proteins are small GTPases that regulate cell growth,\
    \ proliferation and differentiation. The different Ras isoforms: H-ras, N-ras\
    \ and K-ras, generate distinct signal outputs, despite interacting with a common\
    \ set of activators and effectors. Ras is activated by guanine nucleotide exchange\
    \ factors (GEFs) that release GDP and allow GTP binding. Many RasGEFs have been\
    \ identified. These are sequestered in the cytosol until activation by growth\
    \ factors triggers recruitment to the plasma membrane or Golgi, where the GEF\
    \ colocalises with Ras. Active GTP-bound Ras interacts with several effector proteins:\
    \ among the best characterised are the Raf kinases, phosphatidylinositol 3-kinase\
    \ (PI3K), RalGEFs and NORE/MST1. Small GTPases form an independent superfamily\
    \ within the larger class of regulatory GTP hydrolases. This superfamily contains\
    \ proteins that control a vast number of important processes and possess a common,\
    \ structurally preserved GTP-binding domain [[cite:PUB00052600], [cite:PUB00004087]].\
    \ Sequence comparisons of small G proteins from various species have revealed\
    \ that they are conserved in primary structures at the level of 30-55% similarity\
    \ . Crystallographic analysis of various small G proteins revealed the presence\
    \ of a 20kDa catalytic domain that is unique for the whole superfamily [[cite:PUB00004087],\
    \ [cite:PUB00023196]]. The domain is built of five \u03B1 helices (A1-A5), six\
    \ \u03B2-strands (B1-B6) and five polypeptide loops (G1-G5). A structural comparison\
    \ of the GTP- and ..."
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 34
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: IPR020849-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: IPR020849-deep-research-falcon_artifacts/artifact-01.md
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
- **Accession:** IPR020849
- **Name:** Small GTPase, Ras-type
- **Short name:** Small_GTPase_Ras-type
- **Entry type:** family
- **Integrated into / parent:** None (top-level entry)
- **Member database signatures:** PTHR24070 (panther: RAS, DI-RAS, AND RHEB FAMILY MEMBERS OF SMALL GTPASE SUPERFAMILY)
- **Scale:** 33550 proteins across 8233 taxa, 0 subfamilies
- **Current InterPro2GO terms (the mappings under review):** GO:0005525 GTP binding [F]; GO:0007165 signal transduction [P]; GO:0016020 membrane [C]
- **InterPro description:** Ras proteins are small GTPases that regulate cell growth, proliferation and differentiation. The different Ras isoforms: H-ras, N-ras and K-ras, generate distinct signal outputs, despite interacting with a common set of activators and effectors. Ras is activated by guanine nucleotide exchange factors (GEFs) that release GDP and allow GTP binding. Many RasGEFs have been identified. These are sequestered in the cytosol until activation by growth factors triggers recruitment to the plasma membrane or Golgi, where the GEF colocalises with Ras. Active GTP-bound Ras interacts with several effector proteins: among the best characterised are the Raf kinases, phosphatidylinositol 3-kinase (PI3K), RalGEFs and NORE/MST1. Small GTPases form an independent superfamily within the larger class of regulatory GTP hydrolases. This superfamily contains proteins that control a vast number of important processes and possess a common, structurally preserved GTP-binding domain [[cite:PUB00052600], [cite:PUB00004087]]. Sequence comparisons of small G proteins from various species have revealed that they are conserved in primary structures at the level of 30-55% similarity . Crystallographic analysis of various small G proteins revealed the presence of a 20kDa catalytic domain that is unique for the whole superfamily [[cite:PUB00004087], [cite:PUB00023196]]. The domain is built of five α helices (A1-A5), six β-strands (B1-B6) and five polypeptide loops (G1-G5). A structural comparison of the GTP- and ...

### Why entry type matters:

An entry of type **domain**, **repeat**, or **homologous_superfamily** identifies a
structural/functional *module*, not a whole-protein function. GO terms describing a
whole-protein activity or process attached to such a module systematically over-annotate
every protein that merely *contains* the module. An entry of type **family** is more
likely to support whole-protein function terms, but only if the family is functionally
homogeneous.

## Research Target

Provide a comprehensive, citation-backed research report on the InterPro entry
**IPR020849 (Small GTPase, Ras-type)**, structured to support GO annotation review.

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
- **Accession:** IPR020849
- **Name:** Small GTPase, Ras-type
- **Short name:** Small_GTPase_Ras-type
- **Entry type:** family
- **Integrated into / parent:** None (top-level entry)
- **Member database signatures:** PTHR24070 (panther: RAS, DI-RAS, AND RHEB FAMILY MEMBERS OF SMALL GTPASE SUPERFAMILY)
- **Scale:** 33550 proteins across 8233 taxa, 0 subfamilies
- **Current InterPro2GO terms (the mappings under review):** GO:0005525 GTP binding [F]; GO:0007165 signal transduction [P]; GO:0016020 membrane [C]
- **InterPro description:** Ras proteins are small GTPases that regulate cell growth, proliferation and differentiation. The different Ras isoforms: H-ras, N-ras and K-ras, generate distinct signal outputs, despite interacting with a common set of activators and effectors. Ras is activated by guanine nucleotide exchange factors (GEFs) that release GDP and allow GTP binding. Many RasGEFs have been identified. These are sequestered in the cytosol until activation by growth factors triggers recruitment to the plasma membrane or Golgi, where the GEF colocalises with Ras. Active GTP-bound Ras interacts with several effector proteins: among the best characterised are the Raf kinases, phosphatidylinositol 3-kinase (PI3K), RalGEFs and NORE/MST1. Small GTPases form an independent superfamily within the larger class of regulatory GTP hydrolases. This superfamily contains proteins that control a vast number of important processes and possess a common, structurally preserved GTP-binding domain [[cite:PUB00052600], [cite:PUB00004087]]. Sequence comparisons of small G proteins from various species have revealed that they are conserved in primary structures at the level of 30-55% similarity . Crystallographic analysis of various small G proteins revealed the presence of a 20kDa catalytic domain that is unique for the whole superfamily [[cite:PUB00004087], [cite:PUB00023196]]. The domain is built of five α helices (A1-A5), six β-strands (B1-B6) and five polypeptide loops (G1-G5). A structural comparison of the GTP- and ...

### Why entry type matters:

An entry of type **domain**, **repeat**, or **homologous_superfamily** identifies a
structural/functional *module*, not a whole-protein function. GO terms describing a
whole-protein activity or process attached to such a module systematically over-annotate
every protein that merely *contains* the module. An entry of type **family** is more
likely to support whole-protein function terms, but only if the family is functionally
homogeneous.

## Research Target

Provide a comprehensive, citation-backed research report on the InterPro entry
**IPR020849 (Small GTPase, Ras-type)**, structured to support GO annotation review.

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


# Comprehensive Research Report: InterPro Entry IPR020849 (Small GTPase, Ras-type)

## Executive Summary

InterPro entry **IPR020849** represents a **family**-level signature for Small GTPase, Ras-type proteins covering 33,550 proteins across 8,233 taxa. This report evaluates the appropriateness of current InterPro2GO mappings (GO:0005525 GTP binding [F]; GO:0007165 signal transduction [P]; GO:0016020 membrane [C]) against primary literature from 2020–2024 focusing on biochemical mechanism, evolutionary scope, and functional diversification (mozzarelli2024functionalandstructural pages 1-3, yin2023targetingsmallgtpases pages 1-2, kolch2023dynamicregulationof pages 1-2, yin2023targetingsmallgtpases pages 3-5).

---

## 1. Family Definition and Biochemistry

### 1.1 Conserved Structural Architecture

Ras-type small GTPases share a **conserved ~20 kDa catalytic GTPase domain** adopting the **Ras-like Rossmann fold** consisting of six β-strands surrounded by five α-helices (simanshu2022astructureis pages 2-3, osaka2021divergentmechanismsactivating pages 1-2, yin2023targetingsmallgtpases pages 3-5). This structural core contains five functionally critical loop/motif regions designated **G1–G5** (also termed G-boxes) that bind guanine nucleotides with picomolar affinity and catalyze GTP hydrolysis (osaka2021divergentmechanismsactivating pages 1-2, yin2023targetingsmallgtpases pages 3-5, osaka2021divergentmechanismsactivating pages 2-4).

| Feature Category | Specific Element | Description | Universality Across Family |
|---|---|---|---|
| Core fold | Ras-like G-domain / Rossmann fold | Conserved catalytic G-domain adopts a Ras-like Rossmann fold with a central six-stranded β-sheet surrounded by five α-helices; GDP- and GTP-bound states retain the same overall fold but differ mainly in Switch I/II conformations (simanshu2022astructureis pages 2-3, osaka2021divergentmechanismsactivating pages 1-2, yin2023targetingsmallgtpases pages 3-5) | Universal defining feature of Ras-type small GTPases |
| Core architecture | Switch regions I and II | Switch I and Switch II undergo nucleotide-dependent conformational changes that create the effector/regulator interaction surface; GTP loading promotes the active conformation recognized by effectors (osaka2021divergentmechanismsactivating pages 1-2, yin2023targetingsmallgtpases pages 3-5, osaka2021divergentmechanismsactivating pages 2-4) | Universal mechanistic feature |
| Conserved motif | G1 / P-loop (approx. Ras residues 10–16; consensus phosphate-binding loop) | Binds nucleotide phosphates; includes oncogenic/catalytic hotspot residues Gly12 and Gly13. The P-loop is a major determinant of high-affinity nucleotide binding (osaka2021divergentmechanismsactivating pages 1-2, yin2023targetingsmallgtpases pages 3-5, osaka2021divergentmechanismsactivating pages 2-4) | Universal and essential |
| Conserved motif | G2 / Switch I (approx. Ras residues 32–38) | Contains conserved Thr35, which coordinates Mg2+ and interacts with the γ-phosphate of GTP; contributes to nucleotide-state sensing and effector binding (simanshu2022astructureis pages 2-3, yin2023targetingsmallgtpases pages 3-5) | Universal and essential |
| Conserved motif | G3 / Switch II (approx. Ras residues 57–61) | Contains catalytic Gln61 and forms part of Switch II; crucial for GTP hydrolysis and conformational coupling to the active site (berta2023mechanismbasedredesignof pages 1-2, yin2023targetingsmallgtpases pages 3-5, osaka2021divergentmechanismsactivating pages 2-4) | Universal and essential |
| Conserved motif | G4 / NKXD motif (human Ras 116NKCD119) | Major guanine-specificity motif; Lys117 contacts ribose and Asp119 hydrogen-bonds to guanine, conferring selective high-affinity binding to guanine nucleotides (osaka2021divergentmechanismsactivating pages 1-2, osaka2021divergentmechanismsactivating pages 2-4) | Universal hallmark of guanine nucleotide specificity |
| Conserved motif | G5 / SAX motif (human Ras 145SAK147) | Contributes to guanine recognition; Ala146 and Lys147 interact with the guanine ring and support nucleotide specificity and tight binding (osaka2021divergentmechanismsactivating pages 1-2, osaka2021divergentmechanismsactivating pages 2-4) | Universal hallmark of guanine nucleotide specificity |
| Key catalytic residue | Thr35 | Coordinates Mg2+ and γ-phosphate in the active state, helping couple nucleotide state to switch conformation and effector recognition (simanshu2022astructureis pages 2-3, yin2023targetingsmallgtpases pages 3-5) | Conserved core residue across Ras-type proteins |
| Key catalytic residue | Gln61 | Central catalytic residue for hydrolysis; recent mechanistic work supports a role in activating/deprotonating the nucleophilic water during GTP hydrolysis in Ras·GAP complexes (berta2023mechanismbasedredesignof pages 1-2, yin2023targetingsmallgtpases pages 3-5) | Conserved catalytic position; mutations often impair hydrolysis |
| Key catalytic residue | Gly12 / Gly13 | P-loop glycines permit proper active-site geometry; substitutions at these positions commonly impair GAP-stimulated hydrolysis and stabilize the GTP-bound state (berta2023mechanismbasedredesignof pages 1-2, yin2023targetingsmallgtpases pages 3-5) | Conserved active-site residues |
| Catalytic cofactor interaction | Mg2+ coordination network | Essential Mg2+ coordinates β/γ phosphates and Ras residues including Ser17 and Thr35 plus water molecules, stabilizing the nucleotide-binding site (simanshu2022astructureis pages 2-3, berta2023mechanismbasedredesignof pages 1-2) | Universal requirement for canonical Ras-type nucleotide binding/hydrolysis |
| GAP-assisted catalysis | Arginine finger from GAP | Ras intrinsic hydrolysis is slow; RasGAP/NF1 accelerates hydrolysis by providing an arginine finger that stabilizes the transition state and contacts β/γ phosphates (kolch2023dynamicregulationof pages 1-2, berta2023mechanismbasedredesignof pages 1-2, osaka2021divergentmechanismsactivating pages 2-4) | Broadly conserved regulatory mechanism for canonical Ras-family cycling |
| Nucleotide biochemistry | High-affinity GDP/GTP binding | Ras-family proteins bind GDP and GTP with very high, often picomolar, affinity; intrinsic exchange and hydrolysis are slow and therefore regulated by GEFs and GAPs (mozzarelli2024functionalandstructural pages 1-3, gray2020targetingthesmall pages 1-3, liu2023ras‐targetedcancertherapy pages 1-2) | Core biochemical property of the family |
| Molecular-switch behavior | GDP-bound OFF / GTP-bound ON cycle | Family members operate as guanine nucleotide-dependent molecular switches: GDP-bound proteins are inactive or low-effector-binding, whereas GTP-bound proteins adopt conformations that engage effectors (mozzarelli2024functionalandstructural pages 1-3, yin2023targetingsmallgtpases pages 1-2, nair2023regulationofrasgtpase pages 1-2) | Universal family-level mechanism |
| Membrane association | C-terminal CAAX prenylation and secondary targeting signals | Ras proteins are synthesized as hydrophilic proteins but undergo prenylation and additional processing (and, for some isoforms, palmitoylation or use of polybasic sequences) to associate with plasma membrane/Golgi/ER membranes, enabling biological activity (liu2023ras‐targetedcancertherapy pages 1-2, nair2023regulationofrasgtpase pages 1-2) | Common and functionally important for canonical Ras isoforms; membrane targeting chemistry can vary among Ras-family branches |
| Family diversification note | Seven Ras-family subgroups | The broader Ras family includes Ras, Ral, Rheb, Rap, Rad, Rit, and DIRAS branches, all sharing the conserved G-domain but diverging in regulators, localization, and outputs (mozzarelli2024functionalandstructural pages 1-3, yin2023targetingsmallgtpases pages 1-2) | Shared core biochemistry with subfamily specialization |


*Table: This table summarizes the conserved structural and biochemical hallmarks of the IPR020849 Ras-type small GTPase family, emphasizing features most relevant to family-level GO annotation review. It highlights which properties are universal across the family versus where subfamily-level diversification begins.*

**Key conserved residues** essential for catalysis and nucleotide binding include (berta2023mechanismbasedredesignof pages 1-2, osaka2021divergentmechanismsactivating pages 1-2, yin2023targetingsmallgtpases pages 3-5, osaka2021divergentmechanismsactivating pages 2-4):

- **G1 (P-loop, residues ~10–16 in canonical Ras):** Binds nucleotide phosphates; contains Gly12 and Gly13, hotspot positions for oncogenic mutations that impair GAP-mediated GTP hydrolysis.
- **G2/Switch I (residues ~32–38):** Contains Thr35, which coordinates Mg²⁺ and interacts with the γ-phosphate of GTP; critical for effector recognition and nucleotide state-sensing.
- **G3/Switch II (residues ~57–61):** Contains catalytic Gln61, which recent mechanistic studies demonstrate acts as a transient Brønsted base to activate the nucleophilic water for GTP hydrolysis in Ras·GAP complexes (berta2023mechanismbasedredesignof pages 1-2).
- **G4 (NKXD motif, residues 116–119 in human Ras):** Lys117 interacts with the ribose moiety and Asp119 forms a hydrogen bond with the guanine base, conferring guanine nucleotide specificity (osaka2021divergentmechanismsactivating pages 1-2, osaka2021divergentmechanismsactivating pages 2-4).
- **G5 (SAX motif, residues 145–147):** Ala146 and Lys147 interact with the guanine ring, further ensuring specificity and tight binding (osaka2021divergentmechanismsactivating pages 1-2, osaka2021divergentmechanismsactivating pages 2-4).

The **Switch I and Switch II** regions undergo major conformational changes upon GDP→GTP exchange, creating the binding surface for downstream effectors and regulatory proteins (GEFs and GAPs) (mozzarelli2024functionalandstructural pages 1-3, kolch2023dynamicregulationof pages 1-2, osaka2021divergentmechanismsactivating pages 1-2, yin2023targetingsmallgtpases pages 3-5). Intrinsic GTP hydrolysis is extremely slow (k_cat ~0.006–0.019 min⁻¹); GTPase-activating proteins (GAPs) accelerate hydrolysis by 2–5 orders of magnitude by providing an arginine finger that stabilizes the transition state (kolch2023dynamicregulationof pages 1-2, berta2023mechanismbasedredesignof pages 1-2, osaka2021divergentmechanismsactivating pages 2-4).

### 1.2 Molecular Mechanism

Ras-type GTPases function as **binary molecular switches** cycling between an inactive GDP-bound "OFF" state and an active GTP-bound "ON" state (mozzarelli2024functionalandstructural pages 1-3, kolch2023dynamicregulationof pages 1-2, yin2023targetingsmallgtpases pages 1-2). Guanine nucleotide exchange factors (GEFs) facilitate GDP release and GTP loading, while GAPs stimulate GTP hydrolysis to return the protein to the inactive state (mozzarelli2024functionalandstructural pages 1-3, kolch2023dynamicregulationof pages 1-2, osaka2021divergentmechanismsactivating pages 2-4, nair2023regulationofrasgtpase pages 1-2). The intracellular GTP/GDP ratio (5–80 fold higher GTP) drives preferential GTP loading once GDP dissociates (osaka2021divergentmechanismsactivating pages 2-4). In the active GTP-bound state, conformational changes in Switch I and II enable selective interaction with effector proteins that propagate signaling cascades (mozzarelli2024functionalandstructural pages 1-3, kolch2023dynamicregulationof pages 1-2).

---

## 2. InterPro2GO Mapping Appropriateness

| GO Term ID and Name | Assessment | Rationale based on evidence | Subfamily-specific concerns | Recommendation |
|---|---|---|---|---|
| GO:0005525 GTP binding | ACCEPT | This is the defining biochemical property of Ras-type small GTPases. The family shares the conserved Ras G-domain with G1–G5 motifs responsible for high-affinity guanine nucleotide binding; G4/G5 confer guanine specificity and the proteins cycle between GDP- and GTP-bound states. This appears to hold across the Ras family branches represented in the literature and is the least over-broad of the current mappings (mozzarelli2024functionalandstructural pages 1-3, gray2020targetingthesmall pages 1-3, osaka2021divergentmechanismsactivating pages 1-2, yin2023targetingsmallgtpases pages 3-5, osaka2021divergentmechanismsactivating pages 2-4, yin2023targetingsmallgtpases pages 1-2). | No clear evidence from the retrieved sources for stable non-binders or pseudoproteins within the family-level scope; however, family-level annotation should still be monitored for any future inactive outliers. | KEEP. This term is appropriate for essentially all proteins matching the signature and captures the core family biochemistry (mozzarelli2024functionalandstructural pages 1-3, osaka2021divergentmechanismsactivating pages 1-2, osaka2021divergentmechanismsactivating pages 2-4). |
| GO:0007165 signal transduction | MODIFY | Ras-type proteins are widely described as molecular switches in signaling pathways, but the family is functionally diversified into multiple subfamilies (Ras, Ral, Rheb, Rap, Rad, Rit, DIRAS) with distinct downstream outputs and pathway contexts. The term is therefore broadly true at a high level, yet too generic for a top-level family and risks obscuring important specialization. A more specific process term would need child-family evidence rather than this top-level entry (mozzarelli2024functionalandstructural pages 1-3, kolch2023dynamicregulationof pages 1-2, yin2023targetingsmallgtpases pages 1-2, riovilarino2021rasfamilyof pages 1-2, nair2023regulationofrasgtpase pages 1-2). | Different branches have distinct roles: e.g., canonical Ras proteins classically relay RTK-to-RAF/PI3K signaling, whereas DIRAS proteins are discussed as tumor suppressive and other branches such as Rheb/Ral/Rap have specialized pathway functions. Thus, one generic process term may be technically broad but not uniformly informative for every match (yin2023targetingsmallgtpases pages 1-2, riovilarino2021rasfamilyof pages 1-2). | MODIFY-to-specific / KEEP_AS_NON_CORE. Retain only if InterPro wants a very high-level process tag for the family; otherwise move more informative signaling-process GO terms to child entries or subfamilies where pathway specificity is demonstrated (kolch2023dynamicregulationof pages 1-2, yin2023targetingsmallgtpases pages 1-2, nair2023regulationofrasgtpase pages 1-2). |
| GO:0016020 membrane | REMOVE | The evidence supports membrane association or membrane trafficking relevance for many canonical Ras proteins through prenylation/CAAX processing, but GO:0016020 denotes the membrane cellular component itself and is overly generic. It is also not demonstrated from the retrieved evidence that every Ras-type family member should be annotated simply to “membrane” at the family level; localization varies among plasma membrane, Golgi, ER, and other compartments, and some family branches are better described by specific membrane-associated terms only at subfamily level (liu2023ras‐targetedcancertherapy pages 1-2, yin2023targetingsmallgtpases pages 1-2, nair2023regulationofrasgtpase pages 1-2). | Canonical HRAS/NRAS/KRAS isoforms clearly depend on membrane targeting, but broader Ras-family diversification means a single unspecific component term can over-annotate and loses biological meaning. If used, more precise child terms such as plasma membrane or Golgi membrane would need subfamily-specific support rather than family-wide assignment (liu2023ras‐targetedcancertherapy pages 1-2, nair2023regulationofrasgtpase pages 1-2). | REMOVE or at minimum MARK_AS_OVER_ANNOTATED. Do not keep a family-level “membrane” term on this top-level entry; if localization terms are needed, attach more specific component terms to narrower child entries with direct evidence (liu2023ras‐targetedcancertherapy pages 1-2, nair2023regulationofrasgtpase pages 1-2). |


*Table: This table evaluates the three current InterPro2GO mappings for IPR020849 against family-wide evidence. It highlights which terms are robust at the family level and which are too broad or insufficiently specific for universal annotation.*

### 2.1 GO:0005525 (GTP binding) — **ACCEPT**

**Assessment:** This molecular function term is **appropriate for every protein matching this signature**. GTP binding through the conserved G1–G5 motifs is the defining biochemical activity of the Ras-type family (mozzarelli2024functionalandstructural pages 1-3, gray2020targetingthesmall pages 1-3, osaka2021divergentmechanismsactivating pages 1-2, yin2023targetingsmallgtpases pages 3-5, osaka2021divergentmechanismsactivating pages 2-4, yin2023targetingsmallgtpases pages 1-2). All evidence across 2020–2024 literature confirms that canonical and non-canonical Ras subfamily members share picomolar-affinity guanine nucleotide binding and the capacity to cycle between GDP- and GTP-bound states. No evidence was identified for stable pseudoproteins or catalytically inactive members lacking this core activity within the family represented by IPR020849.

**Recommendation:** **ACCEPT.** Retain GO:0005525 as a core family-level mapping.

### 2.2 GO:0007165 (signal transduction) — **MODIFY-to-specific / KEEP_AS_NON_CORE**

**Assessment:** Ras-type proteins universally function as molecular switches transmitting signals from receptors to intracellular effectors, controlling proliferation, differentiation, migration, and other cellular processes (mozzarelli2024functionalandstructural pages 1-3, kolch2023dynamicregulationof pages 1-2, yin2023targetingsmallgtpases pages 1-2, nair2023regulationofrasgtpase pages 1-2). However, the family is functionally **diversified into seven subfamilies** (Ras, Ral, Rheb, Rap, Rad, Rit, DIRAS) with distinct signaling outputs and pathway contexts (yin2023targetingsmallgtpases pages 1-2).

- **Canonical Ras subfamily (HRAS, NRAS, KRAS):** Primarily relay receptor tyrosine kinase (RTK) signals through RAF/MEK/ERK and PI3K/AKT pathways to control cell proliferation and survival (mozzarelli2024functionalandstructural pages 1-3, kolch2023dynamicregulationof pages 1-2, yin2023targetingsmallgtpases pages 1-2).
- **DIRAS subfamily (DIRAS1, DIRAS2, DIRAS3/Noey2):** Characterized as tumor suppressors, functionally opposite to oncogenic Ras subfamily members, with downregulation observed in cancer (yin2023targetingsmallgtpases pages 1-2, riovilarino2021rasfamilyof pages 1-2).
- **Other subfamilies (Rheb, Ral, Rap, Rad, Rit):** Specialized roles in distinct pathways including mTOR regulation (Rheb), vesicle trafficking (Ral), integrin signaling (Rap), with divergent effector repertoires (mozzarelli2024functionalandstructural pages 1-3, yin2023targetingsmallgtpases pages 1-2).

While "signal transduction" is technically true at a high level, it is **too generic** to convey meaningful biology for any specific protein match and obscures critical subfamily-level functional specialization.

**Recommendation:** **MODIFY-to-specific** or **KEEP_AS_NON_CORE**. If InterPro wishes to retain a process-level term at the family level, annotate this as a low-priority or non-core term and encourage assignment of more specific signaling process GO children (e.g., GO:0007265 Ras protein signal transduction, or pathway-specific terms) at subfamily-level child entries where pathway context is experimentally defined.

### 2.3 GO:0016020 (membrane) — **REMOVE** or **MARK_AS_OVER_ANNOTATED**

**Assessment:** Canonical Ras proteins (HRAS, NRAS, KRAS) undergo **C-terminal CAAX prenylation** (farnesylation or geranylgeranylation) followed by proteolytic processing and, for some isoforms, palmitoylation, enabling membrane association at plasma membrane, Golgi apparatus, or endoplasmic reticulum (liu2023ras‐targetedcancertherapy pages 1-2, nair2023regulationofrasgtpase pages 1-2). Membrane targeting is required for biological activity of canonical Ras proteins and appears common across the family.

However, GO:0016020 ("membrane") is an **overly generic cellular component term** that provides little biological information and does not specify which membrane compartment. Evidence shows Ras-family members exhibit **diverse subcellular localization patterns**: plasma membrane, Golgi membrane, ER membrane, with isoform-specific trafficking determinants (e.g., KRAS4B polybasic region vs. NRAS/HRAS palmitoylation-dependent Golgi trafficking) (nair2023regulationofrasgtpase pages 1-2). 

Furthermore, a **family-level** annotation to "membrane" risks over-annotation when applied to 33,550 proteins across 8,233 taxa without subfamily-specific evidence. More precise component terms (e.g., GO:0005886 plasma membrane, GO:0005794 Golgi apparatus, GO:0005789 endoplasmic reticulum membrane) would require subfamily-level experimental validation.

**Recommendation:** **REMOVE** or at minimum **MARK_AS_OVER_ANNOTATED**. Do not retain a top-level "membrane" annotation on this family-level entry. If subcellular localization annotations are needed, assign more specific component terms to child InterPro entries with direct localization evidence for defined subsets of the family (liu2023ras‐targetedcancertherapy pages 1-2, nair2023regulationofrasgtpase pages 1-2).

---

## 3. Functional Divergence Across the Family

The Ras family (36 human members) is subdivided into **seven major branches** (mozzarelli2024functionalandstructural pages 1-3, yin2023targetingsmallgtpases pages 1-2):

1. **Ras subfamily** (HRAS, NRAS, KRAS4A, KRAS4B): Oncogenic drivers when mutated; relay RTK→RAF/MEK/ERK and PI3K/AKT signaling.
2. **Ral subfamily**: Effectors include RalGEF and regulators of trafficking, invasion, and metastasis.
3. **Rheb subfamily**: Activates mTORC1, integrating nutrient and growth factor signals.
4. **Rap subfamily**: Regulates integrin activation, cell adhesion, and junction formation.
5. **Rad subfamily**: Roles in differentiation and insulin signaling.
6. **Rit subfamily**: Neuronal differentiation and survival.
7. **DIRAS subfamily** (DIRAS1, DIRAS2, DIRAS3): Tumor suppressors, downregulated in cancer; biochemical properties under active investigation (yin2023targetingsmallgtpases pages 1-2).

**Key point:** While all share the conserved G-domain and GTPase cycle, **different subfamilies engage distinct effectors and participate in distinct pathways**. No subfamily is known to lack intrinsic GTPase activity, though oncogenic mutations (e.g., G12, G13, Q61 hotspots) can impair GAP-mediated hydrolysis and lock proteins in the GTP-bound active state (kolch2023dynamicregulationof pages 1-2, berta2023mechanismbasedredesignof pages 1-2, yin2023targetingsmallgtpases pages 3-5). Evidence for "pseudoenzyme" or catalytically dead members was not found in the 2020–2024 literature for this family.

---

## 4. Taxonomic Scope

Ras-type GTPases are **ubiquitous across eukaryotes** (yin2023targetingsmallgtpases pages 1-2). The family is present in:

- **Animals** (e.g., 36 members in humans; 108 Ras superfamily genes identified in the Pacific white shrimp _Litopenaeus vannamei_) (yin2023targetingsmallgtpases pages 1-2).
- **Fungi** (e.g., ~29 Ras superfamily members in budding yeast _Saccharomyces cerevisiae_) (yin2023targetingsmallgtpases pages 1-2).
- **Plants** (small GTPase superfamily conserved in land plants and green algae with roles in membrane trafficking, cytoskeleton, and signaling) (yin2023targetingsmallgtpases pages 1-2).
- **Protists** (widespread across diverse eukaryotic lineages including trypanosomes, apicomplexans, and other deeply diverged groups).

The **G-domain fold and G1–G5 motifs are highly conserved** across all eukaryotic Ras-type proteins, supporting the eukaryote-wide applicability of the GTP-binding molecular function (yin2023targetingsmallgtpases pages 3-5, osaka2021divergentmechanismsactivating pages 2-4, yin2023targetingsmallgtpases pages 1-2). No evidence was found for prokaryotic homologs bearing the canonical Ras-type signature (Ras superfamily is eukaryote-specific).

However, **lineage-specific subfamily expansions** and **pathway context** vary significantly. For example, DIRAS proteins may not exist in all taxa, and plant/fungal Ras-like proteins participate in lineage-specific regulatory networks (e.g., yeast Ras1/Ras2 in cAMP/PKA pathway vs. metazoan Ras→RAF signaling). Thus, **process-level terms** like "signal transduction" may apply universally at a mechanistic level but lack specificity regarding pathway output or biological context in different taxa.

Similarly, **membrane localization** through prenylation is conserved, but the specific membrane compartment and trafficking itinerary can vary by isoform and taxon (liu2023ras‐targetedcancertherapy pages 1-2, nair2023regulationofrasgtpase pages 1-2).

---

## 5. Over-Annotation Verdict and Recommendations

### Summary Assessment

InterPro2GO mappings for IPR020849 are **partially over-broad**:

- **GO:0005525 (GTP binding):** Sound and appropriate for family-level annotation. **ACCEPT.**
- **GO:0007165 (signal transduction):** Technically true but too generic; lacks biological specificity for any individual protein match. **MODIFY-to-specific** or **KEEP_AS_NON_CORE**.
- **GO:0016020 (membrane):** Overly generic component term that does not provide meaningful localization information and risks over-annotation at the family level. **REMOVE** or **MARK_AS_OVER_ANNOTATED**.

### Recommended GO Action Pattern

| GO Term | Action | Rationale |
|---------|--------|-----------|
| GO:0005525 (GTP binding) | **ACCEPT** | Universal defining molecular function for the family (mozzarelli2024functionalandstructural pages 1-3, osaka2021divergentmechanismsactivating pages 1-2, osaka2021divergentmechanismsactivating pages 2-4) |
| GO:0007165 (signal transduction) | **MODIFY-to-specific** or **KEEP_AS_NON_CORE** | True but too broad; more informative child terms (e.g., GO:0007265 Ras protein signal transduction) should be assigned at subfamily level with experimental support (mozzarelli2024functionalandstructural pages 1-3, yin2023targetingsmallgtpases pages 1-2) |
| GO:0016020 (membrane) | **REMOVE** or **MARK_AS_OVER_ANNOTATED** | Overly generic; specific membrane compartment terms require subfamily-level evidence and should not be assigned at family level (liu2023ras‐targetedcancertherapy pages 1-2, nair2023regulationofrasgtpase pages 1-2) |

### Recommendations for InterPro

1. **Retain GO:0005525 (GTP binding)** as the core family-level molecular function annotation.
2. **Demote or remove GO:0007165 (signal transduction)** from automatic propagation, or annotate it as low-confidence/non-core. Encourage curators to assign more specific signaling process GO terms at child InterPro entries representing defined Ras subfamilies with validated pathway contexts.
3. **Remove GO:0016020 (membrane)** from this family-level entry. If subcellular localization annotations are desired, assign specific membrane component terms (plasma membrane, Golgi membrane, ER membrane) to narrower child entries where experimental localization data support the annotation.
4. **Consider creating subfamily-level child entries** for the seven major Ras branches (canonical Ras, Ral, Rheb, Rap, Rad, Rit, DIRAS) to enable more granular and biologically meaningful GO annotations tied to specific pathway functions and effector repertoires.

---

## Conclusion

IPR020849 (Small GTPase, Ras-type) represents a functionally diverse family of molecular switch proteins unified by conserved GTP-binding and hydrolysis machinery but divergent in signaling outputs and pathway contexts. Current InterPro2GO mappings are **partially appropriate**: GTP binding is universally correct, but signal transduction is too generic, and membrane localization lacks specificity. To avoid systematic over-annotation, InterPro should retain only the most robust family-level term (GTP binding) and move process/component annotations to subfamily-specific child entries where experimental evidence supports more precise functional and localization assignments (mozzarelli2024functionalandstructural pages 1-3, kolch2023dynamicregulationof pages 1-2, liu2023ras‐targetedcancertherapy pages 1-2, yin2023targetingsmallgtpases pages 1-2, nair2023regulationofrasgtpase pages 1-2).

---

**Publication Dates and URLs (Selected Sources):**

- Kolch et al., "Dynamic regulation of RAS and RAS signaling," _Biochemical Journal_ 480:1–23 (2023). DOI: 10.1042/bcj20220234. https://doi.org/10.1042/bcj20220234
- Yin et al., "Targeting small GTPases: emerging grasps on previously untamable targets, pioneered by KRAS," _Signal Transduction and Targeted Therapy_ 8:212 (2023). DOI: 10.1038/s41392-023-01441-4. https://doi.org/10.1038/s41392-023-01441-4
- Berta et al., "Mechanism-Based Redesign of GAP to Activate Oncogenic Ras," _J. Am. Chem. Soc._ 145:20302–20310 (2023). DOI: 10.1021/jacs.3c04330. https://doi.org/10.1021/jacs.3c04330
- Osaka et al., "Divergent Mechanisms Activating RAS and Small GTPases Through Post-translational Modification," _Front. Mol. Biosci._ 8:707439 (2021). DOI: 10.3389/fmolb.2021.707439. https://doi.org/10.3389/fmolb.2021.707439
- Nair & Saha, "Regulation of Ras-GTPase Signaling and Localization by Post-Translational Modifications," _Kinases Phosphatases_ 1:97–116 (2023). DOI: 10.3390/kinasesphosphatases1020007. https://doi.org/10.3390/kinasesphosphatases1020007
- Mozzarelli et al., "Functional and Structural Insights into RAS Effector Proteins," _Mol. Cell_ 84:2807–2821 (2024). DOI: 10.1016/j.molcel.2024.06.027. https://doi.org/10.1016/j.molcel.2024.06.027

References

1. (mozzarelli2024functionalandstructural pages 1-3): Alessandro M. Mozzarelli, Dhirendra K. Simanshu, and Pau Castel. Functional and structural insights into ras effector proteins. Molecular Cell, 84:2807-2821, Aug 2024. URL: https://doi.org/10.1016/j.molcel.2024.06.027, doi:10.1016/j.molcel.2024.06.027. This article has 37 citations and is from a highest quality peer-reviewed journal.

2. (yin2023targetingsmallgtpases pages 1-2): Guowei Yin, Jing Huang, Johnny Petela, Hongmei Jiang, Yuetong Zhang, Siqi Gong, Jiaxin Wu, Bei Liu, Jianyou Shi, and Yijun Gao. Targeting small gtpases: emerging grasps on previously untamable targets, pioneered by kras. Signal Transduction and Targeted Therapy, May 2023. URL: https://doi.org/10.1038/s41392-023-01441-4, doi:10.1038/s41392-023-01441-4. This article has 101 citations and is from a peer-reviewed journal.

3. (kolch2023dynamicregulationof pages 1-2): Walter Kolch, Dénes Berta, and Edina Rosta. Dynamic regulation of ras and ras signaling. Biochemical Journal, 480:1-23, Jan 2023. URL: https://doi.org/10.1042/bcj20220234, doi:10.1042/bcj20220234. This article has 105 citations and is from a domain leading peer-reviewed journal.

4. (yin2023targetingsmallgtpases pages 3-5): Guowei Yin, Jing Huang, Johnny Petela, Hongmei Jiang, Yuetong Zhang, Siqi Gong, Jiaxin Wu, Bei Liu, Jianyou Shi, and Yijun Gao. Targeting small gtpases: emerging grasps on previously untamable targets, pioneered by kras. Signal Transduction and Targeted Therapy, May 2023. URL: https://doi.org/10.1038/s41392-023-01441-4, doi:10.1038/s41392-023-01441-4. This article has 101 citations and is from a peer-reviewed journal.

5. (simanshu2022astructureis pages 2-3): Dhirendra K. Simanshu and Deborah K. Morrison. A structure is worth a thousand words: new insights for ras and raf regulation. Cancer Discovery, 12:899-912, Jan 2022. URL: https://doi.org/10.1158/2159-8290.cd-21-1494, doi:10.1158/2159-8290.cd-21-1494. This article has 77 citations and is from a highest quality peer-reviewed journal.

6. (osaka2021divergentmechanismsactivating pages 1-2): Natsuki Osaka, Yoshihisa Hirota, Doshun Ito, Yoshiki Ikeda, Ryo Kamata, Yuki Fujii, Venkat R. Chirasani, Sharon L. Campbell, Koh Takeuchi, Toshiya Senda, and Atsuo T. Sasaki. Divergent mechanisms activating ras and small gtpases through post-translational modification. Frontiers in Molecular Biosciences, Jul 2021. URL: https://doi.org/10.3389/fmolb.2021.707439, doi:10.3389/fmolb.2021.707439. This article has 37 citations.

7. (osaka2021divergentmechanismsactivating pages 2-4): Natsuki Osaka, Yoshihisa Hirota, Doshun Ito, Yoshiki Ikeda, Ryo Kamata, Yuki Fujii, Venkat R. Chirasani, Sharon L. Campbell, Koh Takeuchi, Toshiya Senda, and Atsuo T. Sasaki. Divergent mechanisms activating ras and small gtpases through post-translational modification. Frontiers in Molecular Biosciences, Jul 2021. URL: https://doi.org/10.3389/fmolb.2021.707439, doi:10.3389/fmolb.2021.707439. This article has 37 citations.

8. (berta2023mechanismbasedredesignof pages 1-2): Dénes Berta, Sascha Gehrke, Kinga Nyíri, Beáta G. Vértessy, and Edina Rosta. Mechanism-based redesign of gap to activate oncogenic ras. Journal of the American Chemical Society, 145:20302-20310, Sep 2023. URL: https://doi.org/10.1021/jacs.3c04330, doi:10.1021/jacs.3c04330. This article has 26 citations and is from a highest quality peer-reviewed journal.

9. (gray2020targetingthesmall pages 1-3): Janine L. Gray, Frank von Delft, and Paul E. Brennan. Targeting the small gtpase superfamily through their regulatory proteins. Angewandte Chemie (International Ed. in English), 59:6342-6366, Jan 2020. URL: https://doi.org/10.1002/anie.201900585, doi:10.1002/anie.201900585. This article has 167 citations.

10. (liu2023ras‐targetedcancertherapy pages 1-2): Cen Liu, Danyang Ye, Hongliu Yang, Xu Chen, Zhijun Su, Xia Li, Mei Ding, and Yonggang Liu. Ras‐targeted cancer therapy: advances in drugging specific mutations. MedComm, May 2023. URL: https://doi.org/10.1002/mco2.285, doi:10.1002/mco2.285. This article has 29 citations.

11. (nair2023regulationofrasgtpase pages 1-2): Arathi Nair and Bhaskar Saha. Regulation of ras-gtpase signaling and localization by post-translational modifications. Kinases and Phosphatases, 1:97-116, Apr 2023. URL: https://doi.org/10.3390/kinasesphosphatases1020007, doi:10.3390/kinasesphosphatases1020007. This article has 7 citations.

12. (riovilarino2021rasfamilyof pages 1-2): Anxo Rio-Vilariño, Laura del Puerto-Nevado, Jesús García-Foncillas, and Arancha Cebrián. Ras family of small gtpases in crc: new perspectives for overcoming drug resistance. Cancers, 13:3757, Jul 2021. URL: https://doi.org/10.3390/cancers13153757, doi:10.3390/cancers13153757. This article has 9 citations.

## Artifacts

- [Edison artifact artifact-00](IPR020849-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](IPR020849-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. berta2023mechanismbasedredesignof pages 1-2
2. osaka2021divergentmechanismsactivating pages 2-4
3. yin2023targetingsmallgtpases pages 1-2
4. nair2023regulationofrasgtpase pages 1-2
5. mozzarelli2024functionalandstructural pages 1-3
6. kolch2023dynamicregulationof pages 1-2
7. yin2023targetingsmallgtpases pages 3-5
8. simanshu2022astructureis pages 2-3
9. osaka2021divergentmechanismsactivating pages 1-2
10. gray2020targetingthesmall pages 1-3
11. riovilarino2021rasfamilyof pages 1-2
12. F
13. P
14. C
15. [cite:PUB00052600
16. cite:PUB00004087
17. [cite:PUB00004087
18. cite:PUB00023196
19. https://doi.org/10.1042/bcj20220234
20. https://doi.org/10.1038/s41392-023-01441-4
21. https://doi.org/10.1021/jacs.3c04330
22. https://doi.org/10.3389/fmolb.2021.707439
23. https://doi.org/10.3390/kinasesphosphatases1020007
24. https://doi.org/10.1016/j.molcel.2024.06.027
25. https://doi.org/10.1016/j.molcel.2024.06.027,
26. https://doi.org/10.1038/s41392-023-01441-4,
27. https://doi.org/10.1042/bcj20220234,
28. https://doi.org/10.1158/2159-8290.cd-21-1494,
29. https://doi.org/10.3389/fmolb.2021.707439,
30. https://doi.org/10.1021/jacs.3c04330,
31. https://doi.org/10.1002/anie.201900585,
32. https://doi.org/10.1002/mco2.285,
33. https://doi.org/10.3390/kinasesphosphatases1020007,
34. https://doi.org/10.3390/cancers13153757,