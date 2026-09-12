---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-28T21:39:50.684647'
end_time: '2026-06-28T21:57:01.778815'
duration_seconds: 1031.09
template_file: templates/interpro_family_research.md
template_variables:
  interpro_id: PTHR44329
  interpro_name: Serine/Threonine Kinases and Pseudokinases
  interpro_short_name: Ser/Thr_Kinases-Pseudokinases
  interpro_type: family
  interpro_integrated: IPR051681
  member_databases: Not specified
  n_proteins: '112156'
  n_taxa: '17548'
  n_subfamilies: '136'
  interpro2go_terms: None mapped (no InterPro2GO terms for this entry)
  interpro_description: This family of proteins includes both active serine/threonine
    kinases and pseudokinases. The active kinases are involved in various cellular
    processes such as signal transduction pathways, stress responses, and regulation
    of gene expression. They may function in defense mechanisms, potassium homeostasis,
    and viral egress. The pseudokinases, despite lacking catalytic activity, play
    crucial roles in programmed cell death processes like necroptosis. They are activated
    by phosphorylation and binding to specific inositol phosphates, leading to cellular
    events such as membrane localization and plasma membrane damage. Some family members
    are also involved in the regulation of nuclear envelope integrity in response
    to viral infection.
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 36
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: PTHR44329-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: PTHR44329-deep-research-falcon_artifacts/artifact-01.md
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
- **Accession:** PTHR44329
- **Name:** Serine/Threonine Kinases and Pseudokinases
- **Short name:** Ser/Thr_Kinases-Pseudokinases
- **Entry type:** family
- **Integrated into / parent:** IPR051681
- **Member database signatures:** Not specified
- **Scale:** 112156 proteins across 17548 taxa, 136 subfamilies
- **Current InterPro2GO terms (the mappings under review):** None mapped (no InterPro2GO terms for this entry)
- **InterPro description:** This family of proteins includes both active serine/threonine kinases and pseudokinases. The active kinases are involved in various cellular processes such as signal transduction pathways, stress responses, and regulation of gene expression. They may function in defense mechanisms, potassium homeostasis, and viral egress. The pseudokinases, despite lacking catalytic activity, play crucial roles in programmed cell death processes like necroptosis. They are activated by phosphorylation and binding to specific inositol phosphates, leading to cellular events such as membrane localization and plasma membrane damage. Some family members are also involved in the regulation of nuclear envelope integrity in response to viral infection.

### Why entry type matters:

An entry of type **domain**, **repeat**, or **homologous_superfamily** identifies a
structural/functional *module*, not a whole-protein function. GO terms describing a
whole-protein activity or process attached to such a module systematically over-annotate
every protein that merely *contains* the module. An entry of type **family** is more
likely to support whole-protein function terms, but only if the family is functionally
homogeneous.

## Research Target

Provide a comprehensive, citation-backed research report on the InterPro entry
**PTHR44329 (Serine/Threonine Kinases and Pseudokinases)**, structured to support GO annotation review.

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
- **Accession:** PTHR44329
- **Name:** Serine/Threonine Kinases and Pseudokinases
- **Short name:** Ser/Thr_Kinases-Pseudokinases
- **Entry type:** family
- **Integrated into / parent:** IPR051681
- **Member database signatures:** Not specified
- **Scale:** 112156 proteins across 17548 taxa, 136 subfamilies
- **Current InterPro2GO terms (the mappings under review):** None mapped (no InterPro2GO terms for this entry)
- **InterPro description:** This family of proteins includes both active serine/threonine kinases and pseudokinases. The active kinases are involved in various cellular processes such as signal transduction pathways, stress responses, and regulation of gene expression. They may function in defense mechanisms, potassium homeostasis, and viral egress. The pseudokinases, despite lacking catalytic activity, play crucial roles in programmed cell death processes like necroptosis. They are activated by phosphorylation and binding to specific inositol phosphates, leading to cellular events such as membrane localization and plasma membrane damage. Some family members are also involved in the regulation of nuclear envelope integrity in response to viral infection.

### Why entry type matters:

An entry of type **domain**, **repeat**, or **homologous_superfamily** identifies a
structural/functional *module*, not a whole-protein function. GO terms describing a
whole-protein activity or process attached to such a module systematically over-annotate
every protein that merely *contains* the module. An entry of type **family** is more
likely to support whole-protein function terms, but only if the family is functionally
homogeneous.

## Research Target

Provide a comprehensive, citation-backed research report on the InterPro entry
**PTHR44329 (Serine/Threonine Kinases and Pseudokinases)**, structured to support GO annotation review.

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


# Comprehensive Research Report: InterPro Entry PTHR44329 (Serine/Threonine Kinases and Pseudokinases) — GO Annotation Review

## 1. Family Definition and Biochemistry

### Structural Fold and Catalytic Architecture

PTHR44329 is a PANTHER family-level classification that encompasses both catalytically active serine/threonine protein kinases (STKs) and catalytically inactive pseudokinases. All members share the conserved bilobal protein kinase fold, consisting of an N-terminal lobe (predominantly β-sheets and the αC-helix) and a C-terminal lobe (predominantly α-helical), with the active site cleft positioned between the two lobes (oboyle2022computationaltoolsand pages 15-17, gizzio2024evolutionarysequenceand pages 12-15).

Three canonical catalytic motifs define the enzymatic active kinase members:

- **VAIK motif (β3 strand):** Contains a conserved lysine (K72 in PKA numbering) that forms a critical salt bridge with a glutamate in the αC-helix, positioning ATP for catalysis. This lysine stabilizes the γ-phosphate of ATP during phosphotransfer (goldberg2023emergingfunctionsof pages 3-4, gizzio2022evolutionarydivergencein pages 12-13).
- **HRD motif (catalytic loop):** Contains the catalytic aspartate (D166 in PKA) essential for proton abstraction from the substrate hydroxyl during phosphotransfer (oboyle2022computationaltoolsand pages 4-6, oboyle2022computationaltoolsand pages 15-17).
- **DFG motif (activation loop):** Contains a metal-binding aspartate (D184 in PKA) that coordinates Mg²⁺/Mn²⁺ ions required for ATP binding and catalysis. The DFG phenylalanine occupies distinct conformational positions (DFG-in for active, DFG-out for inactive) that regulate activation loop dynamics (oboyle2022computationaltoolsand pages 4-6, oboyle2022computationaltoolsand pages 15-17, gizzio2022evolutionarydivergencein pages 13-15).

Active STKs catalyze the transfer of the γ-phosphate from ATP to the hydroxyl group of serine or threonine residues on substrate proteins. The human genome alone encodes over 300 Ser/Thr kinases, comprising the majority of the human kinome (o’boyle2025atlasofthe pages 1-5).

### Pseudokinase Divergence from Active Kinases

Pseudokinases are defined bioinformatically by the absence of one or more of the three canonical catalytic residues (VAIK-Lys, HRD-Asp, DFG-Asp) (oboyle2022computationaltoolsand pages 1-3, goldberg2023emergingfunctionsof pages 1-2). Approximately 10% of human kinases are classified as pseudokinases (goldberg2023emergingfunctionsof pages 3-4, oboyle2022computationaltoolsand pages 1-3). Despite lacking catalytic activity, pseudokinases retain the conserved kinase fold structure but exhibit a "degraded catalytic site" (oboyle2022computationaltoolsand pages 15-17).

Specific examples of catalytic residue substitutions include: ULK4, where the DFG-Asp is replaced by asparagine and the conserved β3-Lys/αC-Glu salt bridge is absent (oboyle2022computationaltoolsand pages 6-7); VRK3, where DFG-Asp is replaced by glycine and HRD-Asp is only partially conserved (oboyle2022computationaltoolsand pages 4-6); and PSKH2, which carries a primate-specific asparagine substitution at the catalytic aspartate position (oboyle2022computationaltoolsand pages 4-6).

Pseudokinases are further subclassified into four types based on nucleotide-binding properties: Class I does not bind ATP or metal cations; Classes II–IV have varying abilities to bind nucleotides and/or metal ions (pon2023redefiningpseudokinasesa pages 1-3). This heterogeneity in ATP binding is critical for GO annotation considerations.

## 2. InterPro2GO Mapping Appropriateness

The current InterPro2GO status for PTHR44329 is **no mapped GO terms**. Given the family's extreme functional heterogeneity, this is the appropriate annotation strategy. The following analysis examines why commonly considered GO terms would be inappropriate if mapped to this parent entry:

| Candidate GO Term | GO ID | Applies to all members? | Risk of over-annotation | Recommended action |
|---|---|---|---|---|
| protein serine/threonine kinase activity | GO:0004674 | No | Very high: family explicitly includes pseudokinases that lack canonical phosphotransfer activity; some members are molecular switches, scaffolds, or alternative transferases rather than Ser/Thr kinases (goldberg2023emergingfunctionsof pages 3-4, oboyle2022computationaltoolsand pages 15-17, goldberg2023emergingfunctionsof pages 11-12) | REMOVE / do not map at this parent family |
| ATP binding | GO:0005524 | No | High: ATP binding is heterogeneous across pseudokinases; some classes do not bind ATP at all, while others bind ATP but use it for non-canonical chemistry or regulatory functions (goldberg2023emergingfunctionsof pages 6-8, pon2023redefiningpseudokinasesa pages 1-3, pon2023redefiningpseudokinasesa pages 3-4) | REMOVE / do not map |
| protein phosphorylation | GO:0006468 | No | Very high: only catalytically active kinase subfamilies perform protein phosphorylation; pseudokinases such as MLKL, KSR, and Tribbles do not universally catalyze phosphorylation (goldberg2023emergingfunctionsof pages 4-6, goldberg2023emergingfunctionsof pages 6-8, goldberg2023emergingfunctionsof pages 3-4) | REMOVE / do not map |
| protein binding | GO:0005515 | No safe universal support | Moderate to high: many members bind proteins, but this is too generic and often poorly informative; not demonstrated uniformly for every matched protein across 136 subfamilies and 17,548 taxa (goldberg2023emergingfunctionsof pages 6-8, riegel2022recentadvancesin pages 9-10, goldberg2023emergingfunctionsof pages 1-2) | KEEP_UNMAPPED / non-core generic term |
| signal transduction | GO:0007165 | No | High: many eukaryotic kinases participate in signaling, but bacterial STKs also regulate growth, virulence, metabolism, and antibiotic resistance, and some pseudokinases act in death execution or scaffolding instead (goldberg2023emergingfunctionsof pages 4-6, goldberg2023emergingfunctionsof pages 3-4, o’boyle2025atlasofthe pages 5-11, o’boyle2025anatlasof pages 1-5) | REMOVE from parent; map only to specific child families where appropriate |
| necroptotic process | GO:0070266 | No | Extreme: applies to MLKL/RIPK3-related subfamilies only, not to the vast majority of active Ser/Thr kinases across plants, bacteria, fungi, and animals (martinezosorio2023themanyfaces pages 4-6, martinezosorio2023themanyfaces pages 6-8, xu2025mixedlineagekinase pages 8-8, o’boyle2025atlasofthe pages 5-11) | MAP only to MLKL/RIPK3-specific child entries |
| programmed cell death | GO:0012501 | No | Very high: relevant to selected pseudokinase subfamilies such as MLKL, but not universal for canonical kinases involved in immunity, metabolism, development, or virulence (goldberg2023emergingfunctionsof pages 11-12, martinezosorio2023themanyfaces pages 4-6, goldberg2023emergingfunctionsof pages 4-6, o’boyle2025anatlasof pages 1-5) | MAP only to validated death-related child entries |
| defense response | GO:0006952 | No | Very high: some plant RLKs and immune-associated kinases participate in defense, but many family members are unrelated to host defense and occur in taxa lacking the relevant pathways (o’boyle2025atlasofthe pages 5-11, o’boyle2025anatlasof pages 1-5) | MAP only to defense-specific child families |
| intracellular signal transduction | GO:0035556 | No | High: many members are intracellular signaling enzymes, but this excludes membrane receptor kinases and non-signaling pseudokinase effectors; also not applicable across all bacterial and plant clades (goldberg2023emergingfunctionsof pages 4-6, riegel2022recentadvancesin pages 9-10, riegel2022recentadvancesin pages 10-11, o’boyle2025anatlasof pages 1-5) | MAP only to narrower, homogeneous child entries |
| Current InterPro2GO status: no mapped terms | N/A | Yes | Lowest risk: the family is functionally heterogeneous, taxonomically broad, and contains both active kinases and pseudokinases with divergent biochemistry, making parent-level GO mapping unsafe (goldberg2023emergingfunctionsof pages 3-4, oboyle2022computationaltoolsand pages 1-3, o’boyle2025atlasofthe pages 5-11, pon2023redefiningpseudokinasesa pages 1-3) | ACCEPT current absence of GO mappings |


*Table: This table summarizes why broad GO terms are not safe for the mixed Ser/Thr kinase and pseudokinase family PTHR44329. It supports accepting the current absence of InterPro2GO mappings because family-wide annotation would systematically over-annotate many matched proteins.*

### Detailed Assessment of Candidate Terms

**GO:0004674 (protein serine/threonine kinase activity):** This molecular function term applies only to the catalytically active kinase subfamilies. Pseudokinases such as MLKL, KSR1/2, Tribbles, and ILK explicitly lack canonical phosphotransfer activity (goldberg2023emergingfunctionsof pages 3-4, goldberg2023emergingfunctionsof pages 11-12). Some pseudokinases have evolved alternative enzymatic activities such as AMPylation (SelO) rather than phosphorylation (pon2023redefiningpseudokinasesa pages 3-4). Mapping this term at the family level would systematically over-annotate all pseudokinase members.

**GO:0005524 (ATP binding):** ATP binding is not universal even among pseudokinases: Class I pseudokinases do not bind ATP at all, while others bind it for non-canonical purposes (goldberg2023emergingfunctionsof pages 6-8, pon2023redefiningpseudokinasesa pages 1-3). This makes ATP binding inappropriate as a family-wide annotation.

**GO:0006468 (protein phosphorylation):** Only the catalytically active members catalyze protein phosphorylation. Pseudokinases acting as molecular switches (MLKL), scaffolds (Tribbles, KSR), or allosteric regulators (FAM20A, JAK-JH2) do not perform phosphorylation (goldberg2023emergingfunctionsof pages 4-6, goldberg2023emergingfunctionsof pages 6-8).

## 3. Functional Divergence Across the Family

The functional diversity within PTHR44329 is profound and represents a textbook case of neo-functionalization from a common structural scaffold.

| Member type | Example proteins / subfamily | Catalytic activity | Key biological processes | GO:0004674 protein serine/threonine kinase activity? | GO:0005524 ATP binding? | GO:0006468 protein phosphorylation? |
|---|---|---|---|---|---|---|
| Active kinase | MAPKs / ERK-type CMGC kinases | Canonical Ser/Thr kinase activity using conserved kinase motifs and bilobal fold (oboyle2022computationaltoolsand pages 15-17, gizzio2022evolutionarydivergencein pages 13-15, gizzio2022evolutionarydivergencein pages 12-13) | Signal transduction, gene-expression control, stress and growth responses (sujina2026emergenceofcatalytic pages 4-6) | Yes | Yes | Yes |
| Active kinase | RIPK3 | Active Ser/Thr kinase; phosphorylates MLKL during necroptosis signaling (martinezosorio2023themanyfaces pages 4-6, xu2025mixedlineagekinase pages 8-8) | Necroptosis pathway activation and inflammatory cell death signaling (martinezosorio2023themanyfaces pages 4-6, xu2025mixedlineagekinase pages 8-8) | Yes | Yes | Yes |
| Pseudokinase | MLKL | Pseudokinase; lacks canonical phosphotransfer role, functions as phosphorylation-activated molecular switch; RIPK3 phosphorylation triggers dimerization/oligomerization and membrane damage (goldberg2023emergingfunctionsof pages 11-12, martinezosorio2023themanyfaces pages 4-6, martinezosorio2023themanyfaces pages 6-8, xu2025mixedlineagekinase pages 8-8) | Necroptosis execution, membrane permeabilization, inflammatory cell death (martinezosorio2023themanyfaces pages 4-6, martinezosorio2023themanyfaces pages 6-8, xu2025mixedlineagekinase pages 8-8) | No | Variable / context-dependent; not safe as universal term (goldberg2023emergingfunctionsof pages 6-8, pon2023redefiningpseudokinasesa pages 1-3) | No |
| Pseudokinase | KSR1/2 | Pseudokinase acting mainly as allosteric regulator and scaffold in RAF/MEK/ERK signaling (riegel2022recentadvancesin pages 9-10, riegel2022recentadvancesin pages 10-11) | MAPK cascade scaffolding, pathway organization, signaling control (riegel2022recentadvancesin pages 9-10, riegel2022recentadvancesin pages 10-11) | No | Variable / not universal from family membership alone (goldberg2023emergingfunctionsof pages 6-8, pon2023redefiningpseudokinasesa pages 1-3) | No |
| Pseudokinase | Tribbles (TRIB1/2/3) | Catalytically impaired pseudokinases; scaffold/adaptor proteins that recruit ubiquitin ligases and substrates (goldberg2023emergingfunctionsof pages 6-8) | Ubiquitination control, signaling hub functions, pathway modulation (goldberg2023emergingfunctionsof pages 6-8) | No | Sometimes weak nucleotide binding reported, but not a safe universal annotation (goldberg2023emergingfunctionsof pages 6-8) | No |
| Pseudokinase with alternative chemistry | SelO / Selenoprotein O | Not a canonical protein kinase; ATP-dependent AMPylase using kinase-like fold (pon2023redefiningpseudokinasesa pages 3-4, goldberg2023emergingfunctionsof pages 4-6) | Mitochondrial redox regulation and stress-response protein modification (pon2023redefiningpseudokinasesa pages 3-4, goldberg2023emergingfunctionsof pages 4-6) | No | Yes | No |
| Pseudokinase domain | JAK JH2 pseudokinase domain | Low/atypical catalytic potential in some cases, but principal role is regulatory/allosteric inhibition of adjacent kinase domain (goldberg2023emergingfunctionsof pages 4-6, goldberg2023emergingfunctionsof pages 10-11, riegel2022recentadvancesin pages 10-11, goldberg2023emergingfunctionsof pages 3-4) | Cytokine signaling regulation, control of kinase activation state (goldberg2023emergingfunctionsof pages 4-6, goldberg2023emergingfunctionsof pages 10-11, riegel2022recentadvancesin pages 10-11) | No as a blanket family annotation | Variable; some bind nucleotide, others differ (pon2023redefiningpseudokinasesa pages 1-3) | No as a blanket family annotation |
| Active kinase | Plant receptor-like kinases (RLKs / RLCK-linked signaling modules) | Canonical Ser/Thr kinase activity in many members (o’boyle2025anatlasof pages 1-5) | Plant immunity, development, antiviral defense, pattern-triggered signaling (o’boyle2025anatlasof pages 1-5) | Yes for active members, but not for mixed active+pseudokinase family as a whole | Yes for active members | Yes for active members |
| Active kinase | Bacterial STKs (e.g., PknB-like families) | Canonical Ser/Thr kinase activity in many bacterial families; some related bacterial pseudokinase families also exist (o’boyle2025atlasofthe pages 5-11, o’boyle2025anatlasof pages 5-9, o’boyle2025anatlasof pages 1-5) | Cell growth, virulence, pathogenicity, metabolism, antibiotic resistance (o’boyle2025atlasofthe pages 5-11, o’boyle2025anatlasof pages 5-9, o’boyle2025anatlasof pages 1-5) | Yes for active bacterial STKs, not for all PTHR44329 matches | Yes for active members | Yes for active members |
| Mixed family verdict | PTHR44329 overall | Contains both active kinases and catalytically dead/repurposed pseudokinases, including ATP-nonbinding classes and alternative-activity enzymes (goldberg2023emergingfunctionsof pages 3-4, goldberg2023emergingfunctionsof pages 6-8, pon2023redefiningpseudokinasesa pages 1-3) | Extremely broad: signaling, stress, immunity, necroptosis, virulence, development, scaffolding, alternative transferase functions (goldberg2023emergingfunctionsof pages 4-6, goldberg2023emergingfunctionsof pages 3-4, o’boyle2025atlasofthe pages 5-11, o’boyle2025anatlasof pages 1-5) | No universal mapping | No universal mapping | No universal mapping |


*Table: This table summarizes why PTHR44329 is functionally heterogeneous: it contains both canonical serine/threonine kinases and pseudokinases with non-catalytic or alternative catalytic roles. It helps assess why broad GO terms such as kinase activity, ATP binding, or protein phosphorylation are not safe annotations for the whole family.*

### Active Kinase Subfamilies

Active STK members participate in vastly different biological processes depending on the organism and subfamily. In eukaryotes, CMGC kinases (CDK, MAPK, GSK families), CAMK, and Casein Kinase 1 regulate growth factor signaling, translation control, tumor suppression through the Hippo pathway, cardiac function, GPCR signaling, and ribosomal biogenesis (sujina2026emergenceofcatalytic pages 4-6). In bacteria, STKs classified into 42 families across multiple phyla regulate cell growth, virulence, pathogenicity, metabolism, and antibiotic resistance (o’boyle2025atlasofthe pages 5-11, o’boyle2025anatlasof pages 5-9, o’boyle2025anatlasof pages 1-5). In plants, receptor-like kinases function in immunity, development, and pathogen recognition.

### Pseudokinase Members — Divergent Non-Catalytic and Neo-Catalytic Roles

Pseudokinases have evolved multiple distinct functional mechanisms (goldberg2023emergingfunctionsof pages 4-6, pon2023redefiningpseudokinasesa pages 1-3, riegel2022recentadvancesin pages 9-10):

1. **Allosteric regulation:** FAM20A activates FAM20C kinase through heterodimerization; JAK-JH2 domains inhibit adjacent JH1 kinase domains through intramolecular interactions; HER3 stabilizes EGFR/HER2 heterodimer partners (goldberg2023emergingfunctionsof pages 4-6, riegel2022recentadvancesin pages 9-10, riegel2022recentadvancesin pages 10-11).

2. **Scaffolding:** KSR1/2 provide docking sites for MEK, ERK, and other MAPK cascade components; Tribbles (TRIB1/2/3) recruit E3 ubiquitin ligases and substrates for ubiquitination (goldberg2023emergingfunctionsof pages 6-8, riegel2022recentadvancesin pages 9-10, riegel2022recentadvancesin pages 10-11).

3. **Molecular switch:** MLKL is the premier example. Upon RIPK3-mediated phosphorylation of its activation loop, the MLKL pseudokinase domain undergoes conformational change, triggering pseudokinase domain dimerization, tetramerization, oligomerization, translocation to plasma membrane, and ultimately membrane permeabilization through pore formation (~4 nm diameter), causing necroptotic cell death (goldberg2023emergingfunctionsof pages 11-12, saha2026targetingmlkldrivennecroptosis pages 2-4, martinezosorio2023themanyfaces pages 4-6, martinezosorio2023themanyfaces pages 6-8, xu2025mixedlineagekinase pages 8-8, xu2025mixedlineagekinase pages 12-13, saha2026targetingmlkldrivennecroptosis pages 4-6).

4. **Alternative enzymatic activities (neo-functionalization):** SelO (Selenoprotein O) catalyzes AMPylation rather than phosphorylation, binding ATP in an inverted orientation and transferring AMP to substrate proteins involved in mitochondrial redox biology (pon2023redefiningpseudokinasesa pages 3-4). SidJ (a Legionella effector pseudokinase) catalyzes protein glutamylation (pon2023redefiningpseudokinasesa pages 1-3, goldberg2023emergingfunctionsof pages 10-11). SARS-CoV-2 nsp12 catalyzes RNAylation (pon2023redefiningpseudokinasesa pages 1-3).

5. **Competitive inhibition:** STYX pseudophosphatase sequesters ERK2 and competes with active phosphatases (goldberg2023emergingfunctionsof pages 6-8).

These dramatically divergent functions confirm that PTHR44329 is functionally polyphyletic at the process level—the kinase fold has been reused for fundamentally different purposes across subfamilies.

## 4. Taxonomic Scope

PTHR44329 matches 112,156 proteins across 17,548 taxa, indicating a pan-taxonomic distribution spanning all domains of life. STKs are present in:

- **Bacteria:** Classification of ~300,000 bacterial STK sequences revealed 42 distinct families (35 canonical + 7 pseudokinase). Actinobacteria harbor the most diversity (13 families, >100,000 sequences), followed by Proteobacteria (9 families, >19,000 sequences), Firmicutes (4 families, 7,000 sequences), Cyanobacteria (3 families, 27,000 sequences), and Myxococcota (2 families, 12,000 sequences). Many bacterial STK families are phylum-specific (o’boyle2025atlasofthe pages 5-11, o’boyle2025anatlasof pages 5-9, o’boyle2025atlasofthe pages 1-5).

- **Plants:** Extensive receptor-like kinase (RLK) families are major components of plant immune signaling and development.

- **Fungi:** TKL pseudokinase expansions are prominent in fungi (oboyle2022computationaltoolsand pages 1-3).

- **Animals:** The human genome encodes >300 Ser/Thr kinases plus ~50 pseudokinases. Approximately half of human pseudokinases have orthologs in model organisms (goldberg2023emergingfunctionsof pages 3-4).

This taxonomic breadth means that any process-specific GO term mapped at the family level would inevitably "leak" into taxa where the corresponding pathway or subcellular compartment is absent. For example, necroptosis (GO:0070266) is an animal-specific pathway mediated by MLKL—mapping it at the PTHR44329 level would incorrectly annotate bacterial, plant, and fungal kinase members (martinezosorio2023themanyfaces pages 4-6, o’boyle2025atlasofthe pages 5-11).

## 5. Over-Annotation Verdict

### Summary Assessment

The current InterPro2GO status for PTHR44329 — **no mapped GO terms** — is **correct and should be ACCEPTED**.

This family is one of the most functionally heterogeneous protein families in InterPro, combining:

1. **Catalytically active serine/threonine kinases** with canonical phosphotransfer chemistry across all major organismal lineages (gizzio2022evolutionarydivergencein pages 13-15, o’boyle2025atlasofthe pages 5-11, o’boyle2025anatlasof pages 1-5).
2. **Catalytically dead pseudokinases** that serve as allosteric regulators, scaffolds, molecular switches, and competitive inhibitors (goldberg2023emergingfunctionsof pages 4-6, riegel2022recentadvancesin pages 9-10, goldberg2023emergingfunctionsof pages 6-8).
3. **Neo-functionalized pseudokinases** with alternative enzymatic activities (AMPylation, glutamylation, RNAylation) distinct from phosphorylation (pon2023redefiningpseudokinasesa pages 3-4, pon2023redefiningpseudokinasesa pages 1-3).
4. **136 subfamilies** participating in processes as diverse as MAPK signaling, necroptosis, cytokine signaling regulation, plant immunity, bacterial virulence, and mitochondrial redox homeostasis (sujina2026emergenceofcatalytic pages 4-6, o’boyle2025anatlasof pages 1-5).

No single molecular function, biological process, or cellular component GO term can be truthfully applied to all 112,156 proteins matched by this signature.

### Recommended GO Action Pattern

| Action | Details |
|---|---|
| **Overall verdict** | **ACCEPT** — The current absence of InterPro2GO terms is correct |
| **Molecular Function terms** | Do not add GO:0004674 (Ser/Thr kinase activity) or GO:0005524 (ATP binding); these would over-annotate pseudokinase members |
| **Biological Process terms** | Do not add any process terms (signal transduction, necroptosis, defense response, etc.) at the parent level; all are subfamily-specific |
| **Cellular Component terms** | No component terms should be mapped; family members localize to diverse compartments depending on organism and subfamily |
| **InterPro recommendation** | GO terms should be pushed to the 136 child subfamily entries where functional homogeneity can be verified. For example, MLKL-specific subfamilies could appropriately receive GO:0070266 (necroptotic process), while active kinase subfamilies could receive GO:0004674 (protein serine/threonine kinase activity) |

The entry type (family) would normally support whole-protein function annotations, but only when the family is functionally homogeneous. PTHR44329 explicitly and intentionally groups active enzymes with catalytically dead pseudokinases, making it fundamentally incompatible with any uniform GO annotation. This is a sound design choice by PANTHER reflecting evolutionary relatedness, but GO mappings must be deferred to child entries that segregate active from inactive members and further distinguish the highly divergent biological roles of different subfamilies.

References

1. (oboyle2022computationaltoolsand pages 15-17): Brady O'Boyle, Safal Shrestha, Krzysztof Kochut, Patrick A. Eyers, and Natarajan Kannan. Computational tools and resources for pseudokinase research. Methods in enzymology, 667:403-426, Jan 2022. URL: https://doi.org/10.1016/bs.mie.2022.03.040, doi:10.1016/bs.mie.2022.03.040. This article has 8 citations and is from a peer-reviewed journal.

2. (gizzio2024evolutionarysequenceand pages 12-15): Joan Gizzio, Abhishek Thakur, Allan Haldane, Carol Beth Post, and Ronald M. Levy. Evolutionary sequence and structural basis for the distinct conformational landscapes of tyr and ser/thr kinases. bioRxiv, Mar 2024. URL: https://doi.org/10.1101/2024.03.08.584161, doi:10.1101/2024.03.08.584161. This article has 27 citations.

3. (goldberg2023emergingfunctionsof pages 3-4): Timea Goldberg and Anju Sreelatha. Emerging functions of pseudoenzymes. Biochemical Journal, 480:715-728, May 2023. URL: https://doi.org/10.1042/bcj20220373, doi:10.1042/bcj20220373. This article has 25 citations and is from a domain leading peer-reviewed journal.

4. (gizzio2022evolutionarydivergencein pages 12-13): Joan Gizzio, Abhishek Thakur, Allan Haldane, and Ronald M Levy. Evolutionary divergence in the conformational landscapes of tyrosine vs serine/threonine kinases. eLife, Dec 2022. URL: https://doi.org/10.7554/elife.83368, doi:10.7554/elife.83368. This article has 30 citations and is from a domain leading peer-reviewed journal.

5. (oboyle2022computationaltoolsand pages 4-6): Brady O'Boyle, Safal Shrestha, Krzysztof Kochut, Patrick A. Eyers, and Natarajan Kannan. Computational tools and resources for pseudokinase research. Methods in enzymology, 667:403-426, Jan 2022. URL: https://doi.org/10.1016/bs.mie.2022.03.040, doi:10.1016/bs.mie.2022.03.040. This article has 8 citations and is from a peer-reviewed journal.

6. (gizzio2022evolutionarydivergencein pages 13-15): Joan Gizzio, Abhishek Thakur, Allan Haldane, and Ronald M Levy. Evolutionary divergence in the conformational landscapes of tyrosine vs serine/threonine kinases. eLife, Dec 2022. URL: https://doi.org/10.7554/elife.83368, doi:10.7554/elife.83368. This article has 30 citations and is from a domain leading peer-reviewed journal.

7. (o’boyle2025atlasofthe pages 1-5): Brady O’Boyle, Wayland Yeung, Jason D. Lu, Samiksha Katiyar, Tomer M. Yaron-Barir, Jared L. Johnson, Lewis C. Cantley, and Natarajan Kannan. Atlas of the bacterial serine-threonine kinases expands the functional diversity of the kinome. bioRxiv, Jan 2025. URL: https://doi.org/10.1101/2025.01.12.632604, doi:10.1101/2025.01.12.632604. This article has 2 citations.

8. (oboyle2022computationaltoolsand pages 1-3): Brady O'Boyle, Safal Shrestha, Krzysztof Kochut, Patrick A. Eyers, and Natarajan Kannan. Computational tools and resources for pseudokinase research. Methods in enzymology, 667:403-426, Jan 2022. URL: https://doi.org/10.1016/bs.mie.2022.03.040, doi:10.1016/bs.mie.2022.03.040. This article has 8 citations and is from a peer-reviewed journal.

9. (goldberg2023emergingfunctionsof pages 1-2): Timea Goldberg and Anju Sreelatha. Emerging functions of pseudoenzymes. Biochemical Journal, 480:715-728, May 2023. URL: https://doi.org/10.1042/bcj20220373, doi:10.1042/bcj20220373. This article has 25 citations and is from a domain leading peer-reviewed journal.

10. (oboyle2022computationaltoolsand pages 6-7): Brady O'Boyle, Safal Shrestha, Krzysztof Kochut, Patrick A. Eyers, and Natarajan Kannan. Computational tools and resources for pseudokinase research. Methods in enzymology, 667:403-426, Jan 2022. URL: https://doi.org/10.1016/bs.mie.2022.03.040, doi:10.1016/bs.mie.2022.03.040. This article has 8 citations and is from a peer-reviewed journal.

11. (pon2023redefiningpseudokinasesa pages 1-3): Alex Pon, Adam Osinski, and Anju Sreelatha. Redefining pseudokinases: a look at the untapped enzymatic potential of pseudokinases. IUBMB Life, 75:370-376, Jan 2023. URL: https://doi.org/10.1002/iub.2698, doi:10.1002/iub.2698. This article has 12 citations and is from a peer-reviewed journal.

12. (goldberg2023emergingfunctionsof pages 11-12): Timea Goldberg and Anju Sreelatha. Emerging functions of pseudoenzymes. Biochemical Journal, 480:715-728, May 2023. URL: https://doi.org/10.1042/bcj20220373, doi:10.1042/bcj20220373. This article has 25 citations and is from a domain leading peer-reviewed journal.

13. (goldberg2023emergingfunctionsof pages 6-8): Timea Goldberg and Anju Sreelatha. Emerging functions of pseudoenzymes. Biochemical Journal, 480:715-728, May 2023. URL: https://doi.org/10.1042/bcj20220373, doi:10.1042/bcj20220373. This article has 25 citations and is from a domain leading peer-reviewed journal.

14. (pon2023redefiningpseudokinasesa pages 3-4): Alex Pon, Adam Osinski, and Anju Sreelatha. Redefining pseudokinases: a look at the untapped enzymatic potential of pseudokinases. IUBMB Life, 75:370-376, Jan 2023. URL: https://doi.org/10.1002/iub.2698, doi:10.1002/iub.2698. This article has 12 citations and is from a peer-reviewed journal.

15. (goldberg2023emergingfunctionsof pages 4-6): Timea Goldberg and Anju Sreelatha. Emerging functions of pseudoenzymes. Biochemical Journal, 480:715-728, May 2023. URL: https://doi.org/10.1042/bcj20220373, doi:10.1042/bcj20220373. This article has 25 citations and is from a domain leading peer-reviewed journal.

16. (riegel2022recentadvancesin pages 9-10): Kristina Riegel, Parthiban Vijayarangakannan, Petros Kechagioglou, Katarzyna Bogucka, and Krishnaraj Rajalingam. Recent advances in targeting protein kinases and pseudokinases in cancer biology. Frontiers in Cell and Developmental Biology, Jul 2022. URL: https://doi.org/10.3389/fcell.2022.942500, doi:10.3389/fcell.2022.942500. This article has 30 citations.

17. (o’boyle2025atlasofthe pages 5-11): Brady O’Boyle, Wayland Yeung, Jason D. Lu, Samiksha Katiyar, Tomer M. Yaron-Barir, Jared L. Johnson, Lewis C. Cantley, and Natarajan Kannan. Atlas of the bacterial serine-threonine kinases expands the functional diversity of the kinome. bioRxiv, Jan 2025. URL: https://doi.org/10.1101/2025.01.12.632604, doi:10.1101/2025.01.12.632604. This article has 2 citations.

18. (o’boyle2025anatlasof pages 1-5): Brady O’Boyle, Wayland Yeung, Jason D. Lu, Samiksha Katiyar, Tomer M. Yaron-Barir, Jared L. Johnson, Lewis C. Cantley, and Natarajan Kannan. An atlas of bacterial serine-threonine kinases reveals functional diversity and key distinctions from eukaryotic kinases. Science signaling, 18 885:eadt8686, May 2025. URL: https://doi.org/10.1126/scisignal.adt8686, doi:10.1126/scisignal.adt8686. This article has 7 citations and is from a domain leading peer-reviewed journal.

19. (martinezosorio2023themanyfaces pages 4-6): Veronica Martinez-Osorio, Yasmin Abdelwahab, and Uris Ros. The many faces of mlkl, the executor of necroptosis. International Journal of Molecular Sciences, 24:10108, Jun 2023. URL: https://doi.org/10.3390/ijms241210108, doi:10.3390/ijms241210108. This article has 75 citations.

20. (martinezosorio2023themanyfaces pages 6-8): Veronica Martinez-Osorio, Yasmin Abdelwahab, and Uris Ros. The many faces of mlkl, the executor of necroptosis. International Journal of Molecular Sciences, 24:10108, Jun 2023. URL: https://doi.org/10.3390/ijms241210108, doi:10.3390/ijms241210108. This article has 75 citations.

21. (xu2025mixedlineagekinase pages 8-8): Lijuan Xu and Chunlin Zhuang. Mixed lineage kinase domain-like protein (mlkl): from mechanisms to therapeutic opportunities. Advanced science, pages e09277, Aug 2025. URL: https://doi.org/10.1002/advs.202509277, doi:10.1002/advs.202509277. This article has 10 citations and is from a peer-reviewed journal.

22. (riegel2022recentadvancesin pages 10-11): Kristina Riegel, Parthiban Vijayarangakannan, Petros Kechagioglou, Katarzyna Bogucka, and Krishnaraj Rajalingam. Recent advances in targeting protein kinases and pseudokinases in cancer biology. Frontiers in Cell and Developmental Biology, Jul 2022. URL: https://doi.org/10.3389/fcell.2022.942500, doi:10.3389/fcell.2022.942500. This article has 30 citations.

23. (sujina2026emergenceofcatalytic pages 4-6): Ayadathil Sujina, Amal Fahma, Suhail Subair, Rajesh Raju, and Poornima Ramesh. Emergence of catalytic activity in vrk3: phosphoproteomic insights into the regulatory network of a former pseudokinase. Proteomes, 14:14, Mar 2026. URL: https://doi.org/10.3390/proteomes14010014, doi:10.3390/proteomes14010014. This article has 0 citations.

24. (goldberg2023emergingfunctionsof pages 10-11): Timea Goldberg and Anju Sreelatha. Emerging functions of pseudoenzymes. Biochemical Journal, 480:715-728, May 2023. URL: https://doi.org/10.1042/bcj20220373, doi:10.1042/bcj20220373. This article has 25 citations and is from a domain leading peer-reviewed journal.

25. (o’boyle2025anatlasof pages 5-9): Brady O’Boyle, Wayland Yeung, Jason D. Lu, Samiksha Katiyar, Tomer M. Yaron-Barir, Jared L. Johnson, Lewis C. Cantley, and Natarajan Kannan. An atlas of bacterial serine-threonine kinases reveals functional diversity and key distinctions from eukaryotic kinases. Science signaling, 18 885:eadt8686, May 2025. URL: https://doi.org/10.1126/scisignal.adt8686, doi:10.1126/scisignal.adt8686. This article has 7 citations and is from a domain leading peer-reviewed journal.

26. (saha2026targetingmlkldrivennecroptosis pages 2-4): Sarmistha Saha, Luciano Saso, and Brigitta Buttari. Targeting mlkl-driven necroptosis: a therapeutic target in inflammation and host defense. Biomolecules, 16:360, Feb 2026. URL: https://doi.org/10.3390/biom16030360, doi:10.3390/biom16030360. This article has 1 citations.

27. (xu2025mixedlineagekinase pages 12-13): Lijuan Xu and Chunlin Zhuang. Mixed lineage kinase domain-like protein (mlkl): from mechanisms to therapeutic opportunities. Advanced science, pages e09277, Aug 2025. URL: https://doi.org/10.1002/advs.202509277, doi:10.1002/advs.202509277. This article has 10 citations and is from a peer-reviewed journal.

28. (saha2026targetingmlkldrivennecroptosis pages 4-6): Sarmistha Saha, Luciano Saso, and Brigitta Buttari. Targeting mlkl-driven necroptosis: a therapeutic target in inflammation and host defense. Biomolecules, 16:360, Feb 2026. URL: https://doi.org/10.3390/biom16030360, doi:10.3390/biom16030360. This article has 1 citations.

## Artifacts

- [Edison artifact artifact-00](PTHR44329-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](PTHR44329-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. oboyle2022computationaltoolsand pages 15-17
2. oboyle2022computationaltoolsand pages 6-7
3. oboyle2022computationaltoolsand pages 4-6
4. pon2023redefiningpseudokinasesa pages 1-3
5. pon2023redefiningpseudokinasesa pages 3-4
6. sujina2026emergenceofcatalytic pages 4-6
7. goldberg2023emergingfunctionsof pages 6-8
8. oboyle2022computationaltoolsand pages 1-3
9. goldberg2023emergingfunctionsof pages 3-4
10. gizzio2024evolutionarysequenceand pages 12-15
11. gizzio2022evolutionarydivergencein pages 12-13
12. gizzio2022evolutionarydivergencein pages 13-15
13. goldberg2023emergingfunctionsof pages 1-2
14. goldberg2023emergingfunctionsof pages 11-12
15. goldberg2023emergingfunctionsof pages 4-6
16. riegel2022recentadvancesin pages 9-10
17. martinezosorio2023themanyfaces pages 4-6
18. martinezosorio2023themanyfaces pages 6-8
19. xu2025mixedlineagekinase pages 8-8
20. riegel2022recentadvancesin pages 10-11
21. goldberg2023emergingfunctionsof pages 10-11
22. saha2026targetingmlkldrivennecroptosis pages 2-4
23. xu2025mixedlineagekinase pages 12-13
24. saha2026targetingmlkldrivennecroptosis pages 4-6
25. https://doi.org/10.1016/bs.mie.2022.03.040,
26. https://doi.org/10.1101/2024.03.08.584161,
27. https://doi.org/10.1042/bcj20220373,
28. https://doi.org/10.7554/elife.83368,
29. https://doi.org/10.1101/2025.01.12.632604,
30. https://doi.org/10.1002/iub.2698,
31. https://doi.org/10.3389/fcell.2022.942500,
32. https://doi.org/10.1126/scisignal.adt8686,
33. https://doi.org/10.3390/ijms241210108,
34. https://doi.org/10.1002/advs.202509277,
35. https://doi.org/10.3390/proteomes14010014,
36. https://doi.org/10.3390/biom16030360,