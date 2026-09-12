---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-28T21:53:57.678745'
end_time: '2026-06-28T22:14:44.633010'
duration_seconds: 1246.95
template_file: templates/interpro_family_research.md
template_variables:
  interpro_id: PTHR46861
  interpro_name: Tumor necrosis factor receptor superfamily member 1A
  interpro_short_name: TNFRSF1A
  interpro_type: family
  interpro_integrated: IPR052493
  member_databases: Not specified
  n_proteins: '1171'
  n_taxa: '2199'
  n_subfamilies: '1'
  interpro2go_terms: None mapped (no InterPro2GO terms for this entry)
  interpro_description: This family of proteins includes receptors that bind to tumor
    necrosis factors such as TNFSF2/TNF-alpha and homotrimeric TNFSF1/lymphotoxin-alpha.
    Upon ligand binding, these receptors recruit the adapter molecule FADD, which
    in turn recruits caspase-8 to form the death-inducing signaling complex (DISC).
    Activation of caspase-8 initiates a cascade of caspases that leads to apoptosis.
    Additionally, these receptors are involved in non-apoptotic signaling pathways,
    including the induction of an anti-viral state and the activation of acid sphingomyelinase,
    contributing to various TNF-mediated effects.
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 30
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: PTHR46861-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: PTHR46861-deep-research-falcon_artifacts/artifact-01.md
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
- **Accession:** PTHR46861
- **Name:** Tumor necrosis factor receptor superfamily member 1A
- **Short name:** TNFRSF1A
- **Entry type:** family
- **Integrated into / parent:** IPR052493
- **Member database signatures:** Not specified
- **Scale:** 1171 proteins across 2199 taxa, 1 subfamilies
- **Current InterPro2GO terms (the mappings under review):** None mapped (no InterPro2GO terms for this entry)
- **InterPro description:** This family of proteins includes receptors that bind to tumor necrosis factors such as TNFSF2/TNF-alpha and homotrimeric TNFSF1/lymphotoxin-alpha. Upon ligand binding, these receptors recruit the adapter molecule FADD, which in turn recruits caspase-8 to form the death-inducing signaling complex (DISC). Activation of caspase-8 initiates a cascade of caspases that leads to apoptosis. Additionally, these receptors are involved in non-apoptotic signaling pathways, including the induction of an anti-viral state and the activation of acid sphingomyelinase, contributing to various TNF-mediated effects.

### Why entry type matters:

An entry of type **domain**, **repeat**, or **homologous_superfamily** identifies a
structural/functional *module*, not a whole-protein function. GO terms describing a
whole-protein activity or process attached to such a module systematically over-annotate
every protein that merely *contains* the module. An entry of type **family** is more
likely to support whole-protein function terms, but only if the family is functionally
homogeneous.

## Research Target

Provide a comprehensive, citation-backed research report on the InterPro entry
**PTHR46861 (Tumor necrosis factor receptor superfamily member 1A)**, structured to support GO annotation review.

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
- **Accession:** PTHR46861
- **Name:** Tumor necrosis factor receptor superfamily member 1A
- **Short name:** TNFRSF1A
- **Entry type:** family
- **Integrated into / parent:** IPR052493
- **Member database signatures:** Not specified
- **Scale:** 1171 proteins across 2199 taxa, 1 subfamilies
- **Current InterPro2GO terms (the mappings under review):** None mapped (no InterPro2GO terms for this entry)
- **InterPro description:** This family of proteins includes receptors that bind to tumor necrosis factors such as TNFSF2/TNF-alpha and homotrimeric TNFSF1/lymphotoxin-alpha. Upon ligand binding, these receptors recruit the adapter molecule FADD, which in turn recruits caspase-8 to form the death-inducing signaling complex (DISC). Activation of caspase-8 initiates a cascade of caspases that leads to apoptosis. Additionally, these receptors are involved in non-apoptotic signaling pathways, including the induction of an anti-viral state and the activation of acid sphingomyelinase, contributing to various TNF-mediated effects.

### Why entry type matters:

An entry of type **domain**, **repeat**, or **homologous_superfamily** identifies a
structural/functional *module*, not a whole-protein function. GO terms describing a
whole-protein activity or process attached to such a module systematically over-annotate
every protein that merely *contains* the module. An entry of type **family** is more
likely to support whole-protein function terms, but only if the family is functionally
homogeneous.

## Research Target

Provide a comprehensive, citation-backed research report on the InterPro entry
**PTHR46861 (Tumor necrosis factor receptor superfamily member 1A)**, structured to support GO annotation review.

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


# Comprehensive Research Report: InterPro Entry PTHR46861 — Tumor Necrosis Factor Receptor Superfamily Member 1A (TNFRSF1A)

## 1. Family Definition and Biochemistry

### 1.1 Overview and Classification

PTHR46861 is a PANTHER **family-level** InterPro entry encompassing orthologs of tumor necrosis factor receptor superfamily member 1A (TNFRSF1A, also known as TNFR1, CD120a, or p55). The entry covers 1,171 proteins across 2,199 taxa, with 1 subfamily. TNFRSF1A is a 55 kDa type I single-pass transmembrane glycoprotein that serves as the primary receptor for both soluble and membrane-bound TNF-α (TNFSF2) and homotrimeric lymphotoxin-α (TNFSF1) (li2025exploringtnfr1from pages 2-4, li2025exploringtnfr1from pages 1-2). TNFR1 is ubiquitously expressed across cell lineages, functioning as a constitutive housekeeping gene in most tissues, enabling rapid immune response (li2025exploringtnfr1from pages 2-4). The gene is located on human chromosome 12 (12p13.31), spanning 12 kb with 10 exons (li2025exploringtnfr1from pages 2-4).

### 1.2 Structural Architecture

TNFRSF1A is a modular 455-residue protein organized into three major structural regions (li2025exploringtnfr1from pages 2-4, uversky2017functionalityofintrinsic pages 21-24):

The following table details the major structural domains of TNFR1:

| Domain / region | Approx. residues | Principal function | Conserved features / structural characteristics | Key support |
|---|---|---|---|---|
| Signal peptide | aa 1-21 | Directs TNFR1 into the secretory pathway for cell-surface expression | N-terminal signal sequence characteristic of type I membrane proteins; cleaved during maturation (uversky2017functionalityofintrinsic pages 21-24, li2025exploringtnfr1from pages 2-4) | (uversky2017functionalityofintrinsic pages 21-24, li2025exploringtnfr1from pages 2-4) |
| CRD1 / PLAD | aa ~43-82; PLAD within N-terminus, often described around aa 1-54 / CRD1 | Mediates ligand-independent receptor preassembly/oligomerization and promotes TNFR1 trimerization before TNF binding | Cysteine-rich domain with disulfide-bonded TNFR fold; part of the elongated extracellular region; PLAD is a defining conserved feature of TNFR1 family architecture (uversky2017functionalityofintrinsic pages 24-27, li2025exploringtnfr1from pages 2-4, lo2025tnfreceptorsstructurefunction pages 1-3) | (uversky2017functionalityofintrinsic pages 24-27, li2025exploringtnfr1from pages 2-4, lo2025tnfreceptorsstructurefunction pages 1-3) |
| CRD2 | aa ~83-125 | Primary TNF-binding determinant | Cysteine-rich, disulfide-bonded ectodomain module; CRD2 and nearby residues are experimentally implicated in ligand binding; preserved native fold binds TNF with nanomolar affinity in structural/biochemical work (li2025exploringtnfr1from pages 2-4, bastos2024theroleof pages 1-2) | (li2025exploringtnfr1from pages 2-4, bastos2024theroleof pages 1-2) |
| CRD3 | aa ~126-166 | Contributes to TNF binding and receptor-ligand complex formation | Cysteine-rich domain with conserved TNFR disulfide architecture; functions together with CRD2 in ligand engagement within the elongated ectodomain (uversky2017functionalityofintrinsic pages 24-27, li2025exploringtnfr1from pages 2-4, lo2025tnfreceptorsstructurefunction pages 1-3) | (uversky2017functionalityofintrinsic pages 24-27, li2025exploringtnfr1from pages 2-4, lo2025tnfreceptorsstructurefunction pages 1-3) |
| CRD4 | aa ~167-196 | Distal extracellular module; specific role less well defined than CRD1-3 | Cysteine-rich, disulfide-stabilized TNFR module; retained as part of the four-CRD ectodomain organization, but functional assignment is less certain in current summaries (uversky2017functionalityofintrinsic pages 24-27, uversky2017functionalityofintrinsic pages 21-24) | (uversky2017functionalityofintrinsic pages 24-27, uversky2017functionalityofintrinsic pages 21-24) |
| Transmembrane domain | aa ~212-234 | Anchors receptor in plasma membrane and connects ectodomain to cytoplasmic signaling region | Single-pass α-helical transmembrane segment typical of type I receptors; structural studies support a helical TMD and membrane-embedded topology (li2025exploringtnfr1from pages 2-4, uversky2017functionalityofintrinsic pages 21-24, lo2025tnfreceptorsstructurefunction pages 1-3) | (li2025exploringtnfr1from pages 2-4, uversky2017functionalityofintrinsic pages 21-24, lo2025tnfreceptorsstructurefunction pages 1-3) |
| Neutral sphingomyelinase domain (NSD) | Juxtamembrane cytoplasmic region | Promotes ceramide generation / neutral sphingomyelinase-linked death signaling independently of the canonical death domain pathway | Functional signaling element in the membrane-proximal cytoplasmic tail; linked to increased intracellular ceramide and mitochondrial dysfunction (li2025exploringtnfr1from pages 2-4) | (li2025exploringtnfr1from pages 2-4) |
| TNFR1 internalization domain (TRID) | Juxtamembrane / proximal cytoplasmic region | Supports receptor internalization, a step important for transition from membrane complex I to cytosolic death-signaling complexes | Defined as a functional domain in TNFR1 architecture; mechanistically related to TNFR1 endocytosis and subsequent apoptotic signaling competence (li2025exploringtnfr1from pages 2-4, siegmund2023fn14andtnfr2 pages 4-5, li2025exploringtnfr1from pages 6-8) | (li2025exploringtnfr1from pages 2-4, siegmund2023fn14andtnfr2 pages 4-5, li2025exploringtnfr1from pages 6-8) |
| Death domain (DD) | aa ~356-441 (review summaries also place core helical segments within this interval) | Recruits TRADD by homotypic DD interaction and initiates downstream complex I / complex II signaling leading to NF-κB activation, apoptosis, or necroptosis | Canonical death-domain fold of six antiparallel α-helices; conserved charged/polar interaction surfaces; hallmark of TNFR1 versus TNFR2; enables TRADD recruitment rather than direct FADD binding at the receptor (uversky2017functionalityofintrinsic pages 24-27, li2025exploringtnfr1from pages 2-4, green2022thedeathreceptor pages 6-8, siegmund2023fn14andtnfr2 pages 4-5) | (uversky2017functionalityofintrinsic pages 24-27, li2025exploringtnfr1from pages 2-4, green2022thedeathreceptor pages 6-8, siegmund2023fn14andtnfr2 pages 4-5) |


*Table: This table summarizes the major structural regions of TNFR1/TNFRSF1A, their approximate residue ranges, and the best-supported functional assignments. It is useful for assessing which functions are conserved enough across the family to justify GO annotation.*

**Extracellular domain (28 kDa, 182 amino acids):** The ectodomain contains four cysteine-rich domains (CRD1–CRD4) with conserved six-cysteine repeat motifs forming an elongated structure (li2025exploringtnfr1from pages 2-4, uversky2017functionalityofintrinsic pages 24-27). The extracellular domain contains 30 cysteine residues forming 12 disulfide bonds, yielding a highly stable, well-resolved 3D structure (uversky2017functionalityofintrinsic pages 24-27). The conserved CXXCXXC or CXXCXXXC sequence motif in the CRDs is a defining feature of the TNFR superfamily (menon2024caughtinthe pages 11-13). CRD1 contains the pre-ligand assembly domain (PLAD, aa 1–54), which drives TNFR1 trimerization even in the resting (unliganded) state (li2025exploringtnfr1from pages 2-4, lo2025tnfreceptorsstructurefunction pages 1-3). CRD2 (aa 56–73) and residues around aa 107–114 constitute the critical ligand-binding sites, with CRD2 and CRD3 cooperating for TNF engagement (li2025exploringtnfr1from pages 2-4). Chemically synthesized CRD2 retains native conformation and binds TNF-α with KD ≈ 7 nM, confirming the structural integrity of this domain (from Lander et al. 2023).

**Transmembrane domain (22 amino acids):** An α-helical segment connecting the ectodomain to the intracellular signaling region (li2025exploringtnfr1from pages 2-4, lo2025tnfreceptorsstructurefunction pages 1-3).

**Intracellular domain:** Contains the death domain (DD) at the C-terminus (residues ~356–441), a ~80-residue module composed of six antiparallel α-helices (uversky2017functionalityofintrinsic pages 24-27, li2025exploringtnfr1from pages 2-4, bastos2024theroleof pages 2-5). The DD is the defining structural feature of death receptor signaling and is essential for recruiting the adaptor protein TRADD through homotypic DD-DD interactions (green2022thedeathreceptor pages 6-8, siegmund2023fn14andtnfr2 pages 4-5). The juxtamembrane region also contains the neutral sphingomyelinase domain (NSD), which independently activates ceramide generation and mitochondrial dysfunction (li2025exploringtnfr1from pages 2-4), and the TNFR1 internalization domain (TRID) required for receptor endocytosis (li2025exploringtnfr1from pages 2-4).

### 1.3 Signaling Mechanism

TNFR1 signals through two sequential multiprotein complexes (green2022thedeathreceptor pages 6-8, siegmund2023fn14andtnfr2 pages 4-5, li2025exploringtnfr1from pages 4-6):

**Complex I (pro-survival/pro-inflammatory):** Upon TNF-α binding, the exposed DD recruits TRADD, which in turn recruits RIPK1 and TRAF2/5. The E3 ligases cIAP1/2 polyubiquitylate RIPK1 (K63-linked), recruiting LUBAC for linear ubiquitylation and NEMO/IKKγ. This activates TAK1 and the IKK complex, leading to NF-κB nuclear translocation and MAPK pathway activation, driving transcription of pro-survival and pro-inflammatory genes (green2022thedeathreceptor pages 6-8, li2025exploringtnfr1from pages 4-6).

**Complex II (cell death):** When the deubiquitinase CYLD removes ubiquitin from RIPK1, TRADD-RIPK1 dissociate from the receptor and become cytosolic (green2022thedeathreceptor pages 6-8). In Complex IIa, TRADD recruits FADD, which binds and activates procaspase-8, triggering apoptosis. In Complex IIb, RIPK1 associates with FADD/caspase-8. When caspase-8 is inhibited, RIPK1 and RIPK3 form the necrosome, phosphorylating MLKL to cause necroptosis (siegmund2023fn14andtnfr2 pages 4-5, li2025exploringtnfr1from pages 6-8).

A critical distinction from other death receptors (CD95/Fas, TRAIL-R1/R2) is that TNFR1 does **not** form a membrane-proximal DISC that directly activates caspase-8; instead, it relies on the TRADD intermediary and cytosolic complex assembly, resulting in slower kinetics (hours rather than minutes) (siegmund2023fn14andtnfr2 pages 4-5, siegmund2023fn14andtnfr2 pages 1-2).

## 2. InterPro2GO Mapping Appropriateness

### 2.1 Current Status

PTHR46861 currently has **no InterPro2GO terms mapped**. This represents a case of **under-annotation** rather than appropriate restraint, given that this is a family-type entry for a functionally well-characterized and homogeneous protein family.

### 2.2 Recommended GO Terms

Based on the extensive evidence for conserved TNFRSF1A function across all characterized orthologs, several GO terms are strongly supported for addition. The following table summarizes the recommended mappings:

| Current status | GO ID | GO term name | Aspect | Evidence basis | Applies to all PTHR46861 family members? | Recommended action |
|---|---|---|---|---|---|---|
| None mapped | GO:0005031 | tumor necrosis factor-activated receptor activity | MF | TNFR1/TNFRSF1A is the cognate cell-surface receptor for TNF and lymphotoxin-α; conserved extracellular CRDs mediate ligand recognition and receptor activation (li2025exploringtnfr1from pages 2-4, lo2025tnfreceptorsstructurefunction pages 1-3, li2025exploringtnfr1from pages 1-2) | Yes, for bona fide TNFRSF1A orthologs in this family | ADD |
| None mapped | GO:0005164 | tumor necrosis factor receptor binding | MF | Appropriate because TNF is the ligand for TNFR1, but less precise for a receptor family than receptor activity; use only if InterPro2GO allows ligand-binding MF on whole receptor families (li2025exploringtnfr1from pages 2-4, li2025exploringtnfr1from pages 1-2) | Yes, likely for bona fide orthologs, but less specific than receptor activity | ADD (lower priority than GO:0005031) |
| None mapped | GO:0008625 | extrinsic apoptotic signaling pathway via death domain receptors | BP | TNFR1 contains a conserved intracellular death domain and signals through TRADD→FADD→caspase-8 via Complex II/cytosolic death complexes (green2022thedeathreceptor pages 6-8, siegmund2023fn14andtnfr2 pages 4-5, li2025exploringtnfr1from pages 4-6, alim2024molecularmechanismsof pages 1-3) | Yes, as a core conserved signaling capability of TNFR1 orthologs | ADD |
| None mapped | GO:0033209 | tumor necrosis factor-mediated signaling pathway | BP | Core pathway assignment is well supported by conserved TNF-induced Complex I/II signaling, including TRADD, RIPK1, NF-κB, apoptosis, and necroptosis outputs (green2022thedeathreceptor pages 6-8, li2025exploringtnfr1from pages 4-6, li2025exploringtnfr1from pages 6-8) | Yes | ADD |
| None mapped | GO:0007249 | I-kappaB kinase/NF-kappaB signaling | BP | TNFR1 Complex I recruits RIPK1/cIAP/LUBAC/NEMO and activates TAK1/IKK, leading to NF-κB activation; a conserved non-apoptotic output of TNFR1 signaling (green2022thedeathreceptor pages 6-8, li2025exploringtnfr1from pages 4-6, dong2022alterationsinbone pages 1-2) | Yes | ADD |
| None mapped | GO:0005886 | plasma membrane | CC | TNFR1 is a type I single-pass transmembrane cell-surface receptor; this location is fundamental to ligand reception and signaling (li2025exploringtnfr1from pages 2-4, uversky2017functionalityofintrinsic pages 21-24, lo2025tnfreceptorsstructurefunction pages 1-3) | Yes | ADD |
| None mapped | GO:0009897 | external side of plasma membrane | CC | The ligand-binding CRD ectodomain is exposed extracellularly on the cell surface, supporting annotation to the external side of the plasma membrane (li2025exploringtnfr1from pages 2-4, lo2025tnfreceptorsstructurefunction pages 1-3, li2025exploringtnfr1from pages 1-2) | Yes | ADD |


*Table: This table summarizes candidate GO terms for the PTHR46861/TNFRSF1A family, which currently has no InterPro2GO mappings. It highlights which terms are well supported across the family and should be considered for addition during GO annotation review.*

**Molecular Function:** The most appropriate term is *tumor necrosis factor-activated receptor activity* (GO:0005031), which precisely captures the core molecular function of TNFR1 as the receptor for TNF-α and lymphotoxin-α (li2025exploringtnfr1from pages 2-4, lo2025tnfreceptorsstructurefunction pages 1-3, li2025exploringtnfr1from pages 1-2).

**Biological Process:** Three process terms are well supported across the family: (i) *tumor necrosis factor-mediated signaling pathway* (GO:0033209), which captures the core Complex I/Complex II signaling cascade (green2022thedeathreceptor pages 6-8, li2025exploringtnfr1from pages 4-6, li2025exploringtnfr1from pages 6-8); (ii) *extrinsic apoptotic signaling pathway via death domain receptors* (GO:0008625), reflecting the conserved DD→TRADD→FADD→caspase-8 cascade (green2022thedeathreceptor pages 6-8, siegmund2023fn14andtnfr2 pages 4-5, alim2024molecularmechanismsof pages 1-3); and (iii) *I-kappaB kinase/NF-kappaB signaling* (GO:0007249), reflecting the conserved Complex I → NF-κB activation output (green2022thedeathreceptor pages 6-8, dong2022alterationsinbone pages 1-2, li2025exploringtnfr1from pages 4-6).

**Cellular Component:** *Plasma membrane* (GO:0005886) and *external side of plasma membrane* (GO:0009897) are appropriate, as TNFR1 is universally a cell-surface receptor (li2025exploringtnfr1from pages 2-4, lo2025tnfreceptorsstructurefunction pages 1-3).

### 2.3 Terms to Avoid

Certain terms warrant caution at this family level:

- **Necroptosis-specific terms** (e.g., *necroptotic process*): While TNFR1 can trigger necroptosis, this outcome depends on cellular context (caspase-8 inhibition) rather than being a constitutive activity of the receptor, and the necroptotic pathway may not be fully conserved in all taxa within the family.
- **Acid sphingomyelinase activation / ceramide signaling**: While documented for mammalian TNFR1 via the NSD domain (li2025exploringtnfr1from pages 2-4), conservation of this specific signaling arm in all PTHR46861 members (especially non-mammalian orthologs) is less well established.

## 3. Functional Divergence Across the Family

### 3.1 Dual Signaling: A Feature, Not Divergence

TNFR1's ability to activate both pro-survival (NF-κB/MAPK) and pro-death (apoptosis/necroptosis) signaling is not functional divergence but rather an intrinsic feature of the receptor, regulated by post-translational modifications and the availability of checkpoint proteins (cIAP1/2, FLIP, caspase-8) (green2022thedeathreceptor pages 6-8, li2025exploringtnfr1from pages 6-8). Under normal conditions, TNFR1 preferentially transmits pro-survival signals; cell death signaling is activated when specific checkpoints are inactivated (li2025exploringtnfr1from pages 6-8).

### 3.2 Distinction from TNFR2

TNFRSF1A (TNFR1) and TNFRSF1B (TNFR2) are encoded by different genes and represent distinct PANTHER families. Despite sharing 31.6% sequence identity in their extracellular CRDs and both binding TNF-α, they diverge fundamentally: TNFR2 lacks a death domain, does not recruit TRADD, and primarily signals through TRAF2 for NF-κB-mediated survival and immune regulation (uversky2017functionalityofintrinsic pages 24-27, xu2025theroleof pages 2-3, shi2023tnfr1andtnfr2 pages 1-2). TNFR1 is ubiquitously expressed, while TNFR2 is preferentially expressed in leukocytes (shi2023tnfr1andtnfr2 pages 1-2). Importantly, PTHR46861 specifically captures TNFRSF1A orthologs and does not include TNFR2, so this divergence is not a concern for annotation.

### 3.3 No Evidence of Pseudo-receptors or Neo-functionalization

Within the TNFRSF1A ortholog family captured by PTHR46861, there is no published evidence of catalytically dead or pseudo-receptor members. All characterized orthologs retain the hallmark CRD ectodomain, transmembrane anchor, and intracellular death domain. The receptor is mechanistically related to DR3 (TNFRSF25), which also signals through TRADD/RIPK1 rather than directly binding FADD, suggesting this signaling architecture is ancestral to the TNFR1/DR3 clade (siegmund2023fn14andtnfr2 pages 2-4). TNFRSF members that lack functional death domains (decoy receptors) are classified in separate families (dong2022alterationsinbone pages 2-4).

### 3.4 Disease-Associated Variants

Germline and mosaic mutations in TNFRSF1A cause TNF Receptor-Associated Periodic Syndrome (TRAPS), an autoinflammatory disorder (OpenTargets Search: -TNFRSF1A). Pathogenic variants often affect conserved cysteine residues in CRD1 or CRD2, disrupting disulfide bridges and CRD structure. These disease mutations reduce cell-surface expression of TNFR1 and impair TNF-α responsiveness, but they do not represent functional divergence of the family—they are loss-of-function variants within the same protein (from Assrawi et al. 2023; Akagi et al. 2022).

## 4. Taxonomic Scope

### 4.1 Distribution

The TNF-TNFR signaling system is ancient, dating to approximately 700 million years ago based on comparative analysis of invertebrate and vertebrate homologs (menon2024caughtinthe pages 1-4). The broader TNFSF-TNFRSF system is present across Metazoa, including Cnidaria (corals, sea anemones), Porifera (sponges), Mollusca, Arthropoda (Drosophila Eiger/Wengen/Grindelwald), but is notably absent from Nematoda (including C. elegans), Tardigrada, Chelicerates (spiders), and parasitic Platyhelminthes (menon2024caughtinthe pages 8-11, menon2024caughtinthe pages 1-4).

However, the specific PTHR46861 family representing **TNFRSF1A orthologs** is expected to be restricted primarily to **vertebrates** (mammals, birds, reptiles, amphibians, and fish), where the gene-specific orthology to mammalian TNFR1 can be established. The scale of 1,171 proteins across 2,199 taxa is consistent with a vertebrate-wide distribution with some gene duplications in teleost fish.

### 4.2 Conservation Evidence

Comparative genomic studies in the Chinese tree shrew (Tupaia belangeri chinensis) identified 24 TNFRSF genes, with tree shrew TNFRSF1A being phylogenetically closer to human than mouse (divergence ~18.2 mya vs. ~32.4 mya) (huang2025identificationandcharacterization pages 4-6). Importantly, tree shrew TNFRSF1A retains conserved death domain motifs similar to the human version, and functionally shows significant correlation with NF-κB signaling pathway activation (huang2025identificationandcharacterization pages 10-14, huang2025identificationandcharacterization pages 14-15). Ka/Ks ratio analysis across species demonstrates strong purifying selection on TNFRSF genes, indicating high functional conservation (huang2025identificationandcharacterization pages 6-10).

In zebrafish, TNFRSF1A expression is upregulated in disease models (e.g., diabetic kidney disease model with pdx1 knockdown, p = 0.0025), confirming functional conservation of the TNF signaling axis in teleost fish (from Xie et al. 2025).

### 4.3 Applicability of GO Terms Across Taxa

The core functions—TNF-activated receptor activity, death domain-mediated apoptotic signaling, and NF-κB pathway activation—appear conserved across all vertebrate taxa where TNFRSF1A orthologs are found. The TNF signaling pathway and apoptotic machinery are ancient features of vertebrate immunity (huang2025identificationandcharacterization pages 1-2). If any PTHR46861 members extend into invertebrate lineages, the specific receptor-ligand (TNF-TNFR1) designation and TRADD-dependent signaling architecture would need individual verification, but the structural features (CRDs, death domain) are expected to be present by definition of family membership.

## 5. Over-Annotation Verdict

### 5.1 Summary Assessment

PTHR46861 is a **family-type** entry specifically targeting TNFRSF1A orthologs. This is a **functionally homogeneous** family: all characterized members are type I transmembrane receptors with four extracellular CRDs, a transmembrane helix, and an intracellular death domain, all of which bind TNF-α/lymphotoxin-α and signal through the conserved TRADD→Complex I (NF-κB)/Complex II (apoptosis) cascade (li2025exploringtnfr1from pages 2-4, green2022thedeathreceptor pages 6-8, siegmund2023fn14andtnfr2 pages 4-5). There is no evidence of pseudo-receptors, catalytically dead members, or neo-functionalized orthologs within the family.

### 5.2 Current State: Under-Annotated

The current status of **no InterPro2GO terms** represents clear **under-annotation**. For a family entry of this functional homogeneity and biochemical characterization, this is a missed opportunity to provide useful automated annotations to the 1,171 proteins matched by the signature.

### 5.3 Recommended GO Action Pattern

**Overall verdict: UNDER-ANNOTATED → ADD new terms**

| Recommendation | Action |
|---|---|
| GO:0005031 (tumor necrosis factor-activated receptor activity) | **ADD** — core MF of the family |
| GO:0033209 (tumor necrosis factor-mediated signaling pathway) | **ADD** — universal BP for all members |
| GO:0008625 (extrinsic apoptotic signaling pathway via death domain receptors) | **ADD** — conserved DD-mediated apoptotic output |
| GO:0007249 (I-kappaB kinase/NF-kappaB signaling) | **ADD** — conserved Complex I output |
| GO:0005886 (plasma membrane) | **ADD** — universal CC for transmembrane receptors |
| GO:0009897 (external side of plasma membrane) | **ADD** — supported by ectodomain exposure |

### 5.4 Recommendations for InterPro

- The current entry with no InterPro2GO mappings should be updated to include the conserved, family-wide GO terms listed above.
- No demotion of terms is needed, as this is a family (not domain/superfamily) entry and no terms are currently mapped.
- If the 1 subfamily within PTHR46861 represents a specific clade with additional specialized functions (e.g., mammalian-specific ceramide/sphingomyelinase signaling via NSD), more specific process terms could be attached at the subfamily level rather than the family level.
- The parent entry IPR052493 should be examined to ensure that GO terms are not duplicated at both family and parent levels, following InterPro best practices for annotation hierarchy.

References

1. (li2025exploringtnfr1from pages 2-4): Yingying Li, Ruiwei Ye, Haorui Dai, Jiayi Lin, Yue Cheng, Yonghong Zhou, and Yiming Lu. Exploring tnfr1: from discovery to targeted therapy development. Journal of Translational Medicine, Jan 2025. URL: https://doi.org/10.1186/s12967-025-06122-0, doi:10.1186/s12967-025-06122-0. This article has 74 citations and is from a peer-reviewed journal.

2. (li2025exploringtnfr1from pages 1-2): Yingying Li, Ruiwei Ye, Haorui Dai, Jiayi Lin, Yue Cheng, Yonghong Zhou, and Yiming Lu. Exploring tnfr1: from discovery to targeted therapy development. Journal of Translational Medicine, Jan 2025. URL: https://doi.org/10.1186/s12967-025-06122-0, doi:10.1186/s12967-025-06122-0. This article has 74 citations and is from a peer-reviewed journal.

3. (uversky2017functionalityofintrinsic pages 21-24): Vladimir N. Uversky, Nawal Abd El‐Baky, Esmail M. El‐Fakharany, Amira Sabry, Ehab H. Mattar, Alexey V. Uversky, and Elrashdy M. Redwan. Functionality of intrinsic disorder in tumor necrosis factor‐α and its receptors. The FEBS Journal, Nov 2017. URL: https://doi.org/10.1111/febs.14182, doi:10.1111/febs.14182. This article has 18 citations.

4. (uversky2017functionalityofintrinsic pages 24-27): Vladimir N. Uversky, Nawal Abd El‐Baky, Esmail M. El‐Fakharany, Amira Sabry, Ehab H. Mattar, Alexey V. Uversky, and Elrashdy M. Redwan. Functionality of intrinsic disorder in tumor necrosis factor‐α and its receptors. The FEBS Journal, Nov 2017. URL: https://doi.org/10.1111/febs.14182, doi:10.1111/febs.14182. This article has 18 citations.

5. (lo2025tnfreceptorsstructurefunction pages 1-3): Chih Hung Lo. Tnf receptors: structure-function relationships and therapeutic targeting strategies. Jan 2025. URL: https://doi.org/10.1016/j.bbamem.2024.184394, doi:10.1016/j.bbamem.2024.184394. This article has 36 citations and is from a peer-reviewed journal.

6. (bastos2024theroleof pages 1-2): Luana Luiza Bastos, Diego Mariano, Rafael Pereira Lemos, Tatiane Senna Bialves, Carlo Jose Freire Oliveira, and Raquel C. de Melo-Minardi. The role of structural bioinformatics in understanding tumor necrosis factor α-interacting protein mechanisms in chronic inflammatory diseases: a review. Immuno, 4:14-42, Jan 2024. URL: https://doi.org/10.3390/immuno4010002, doi:10.3390/immuno4010002. This article has 15 citations.

7. (siegmund2023fn14andtnfr2 pages 4-5): Daniela Siegmund, Olena Zaitseva, and Harald Wajant. Fn14 and tnfr2 as regulators of cytotoxic tnfr1 signaling. Frontiers in Cell and Developmental Biology, Nov 2023. URL: https://doi.org/10.3389/fcell.2023.1267837, doi:10.3389/fcell.2023.1267837. This article has 18 citations.

8. (li2025exploringtnfr1from pages 6-8): Yingying Li, Ruiwei Ye, Haorui Dai, Jiayi Lin, Yue Cheng, Yonghong Zhou, and Yiming Lu. Exploring tnfr1: from discovery to targeted therapy development. Journal of Translational Medicine, Jan 2025. URL: https://doi.org/10.1186/s12967-025-06122-0, doi:10.1186/s12967-025-06122-0. This article has 74 citations and is from a peer-reviewed journal.

9. (green2022thedeathreceptor pages 6-8): Douglas R. Green. The death receptor pathway of apoptosis. Cold Spring Harbor perspectives in biology, 14 2:a041053, Feb 2022. URL: https://doi.org/10.1101/cshperspect.a041053, doi:10.1101/cshperspect.a041053. This article has 153 citations and is from a peer-reviewed journal.

10. (menon2024caughtinthe pages 11-13): Namita Menon, Kaushiki K, Moushmi Goswami, Anmol Singh, and Subhashini Srinivasan. Caught in the act of triplication: tnf superfamily. bioRxiv, Jul 2024. URL: https://doi.org/10.1101/2024.07.27.603686, doi:10.1101/2024.07.27.603686. This article has 0 citations.

11. (bastos2024theroleof pages 2-5): Luana Luiza Bastos, Diego Mariano, Rafael Pereira Lemos, Tatiane Senna Bialves, Carlo Jose Freire Oliveira, and Raquel C. de Melo-Minardi. The role of structural bioinformatics in understanding tumor necrosis factor α-interacting protein mechanisms in chronic inflammatory diseases: a review. Immuno, 4:14-42, Jan 2024. URL: https://doi.org/10.3390/immuno4010002, doi:10.3390/immuno4010002. This article has 15 citations.

12. (li2025exploringtnfr1from pages 4-6): Yingying Li, Ruiwei Ye, Haorui Dai, Jiayi Lin, Yue Cheng, Yonghong Zhou, and Yiming Lu. Exploring tnfr1: from discovery to targeted therapy development. Journal of Translational Medicine, Jan 2025. URL: https://doi.org/10.1186/s12967-025-06122-0, doi:10.1186/s12967-025-06122-0. This article has 74 citations and is from a peer-reviewed journal.

13. (siegmund2023fn14andtnfr2 pages 1-2): Daniela Siegmund, Olena Zaitseva, and Harald Wajant. Fn14 and tnfr2 as regulators of cytotoxic tnfr1 signaling. Frontiers in Cell and Developmental Biology, Nov 2023. URL: https://doi.org/10.3389/fcell.2023.1267837, doi:10.3389/fcell.2023.1267837. This article has 18 citations.

14. (alim2024molecularmechanismsof pages 1-3): Louisa F Alim, Colm Keane, and Fernando Souza-Fonseca-Guimaraes. Molecular mechanisms of tumour necrosis factor signalling via tnf receptor 1 and tnf receptor 2 in the tumour microenvironment. Current Opinion in Immunology, 86:102409, Feb 2024. URL: https://doi.org/10.1016/j.coi.2023.102409, doi:10.1016/j.coi.2023.102409. This article has 72 citations and is from a peer-reviewed journal.

15. (dong2022alterationsinbone pages 1-2): Yanzhao Dong, Haiying Zhou, Ahmad Alhaskawi, Zewei Wang, Jingtian Lai, Sohaib Hasan Abdullah Ezzi, Vishnu Goutham Kota, Mohamed Hasan Abdulla Hasan Abdulla, Zhenyu Sun, and Hui Lu. Alterations in bone fracture healing associated with tnfrsf signaling pathways. Frontiers in Pharmacology, Oct 2022. URL: https://doi.org/10.3389/fphar.2022.905535, doi:10.3389/fphar.2022.905535. This article has 10 citations.

16. (xu2025theroleof pages 2-3): Jiayi Xu. The role of tumor necrosis factor receptor superfamily in cancer: insights into oncogenesis, progression, and therapeutic strategies. NPJ Precision Oncology, Aug 2025. URL: https://doi.org/10.1038/s41698-025-00990-x, doi:10.1038/s41698-025-00990-x. This article has 20 citations and is from a peer-reviewed journal.

17. (shi2023tnfr1andtnfr2 pages 1-2): Gongping Shi and Yinling Hu. Tnfr1 and tnfr2, which link nf-κb activation, drive lung cancer progression, cell dedifferentiation, and metastasis. Cancers, 15:4299, Aug 2023. URL: https://doi.org/10.3390/cancers15174299, doi:10.3390/cancers15174299. This article has 26 citations.

18. (siegmund2023fn14andtnfr2 pages 2-4): Daniela Siegmund, Olena Zaitseva, and Harald Wajant. Fn14 and tnfr2 as regulators of cytotoxic tnfr1 signaling. Frontiers in Cell and Developmental Biology, Nov 2023. URL: https://doi.org/10.3389/fcell.2023.1267837, doi:10.3389/fcell.2023.1267837. This article has 18 citations.

19. (dong2022alterationsinbone pages 2-4): Yanzhao Dong, Haiying Zhou, Ahmad Alhaskawi, Zewei Wang, Jingtian Lai, Sohaib Hasan Abdullah Ezzi, Vishnu Goutham Kota, Mohamed Hasan Abdulla Hasan Abdulla, Zhenyu Sun, and Hui Lu. Alterations in bone fracture healing associated with tnfrsf signaling pathways. Frontiers in Pharmacology, Oct 2022. URL: https://doi.org/10.3389/fphar.2022.905535, doi:10.3389/fphar.2022.905535. This article has 10 citations.

20. (OpenTargets Search: -TNFRSF1A): Open Targets Query (-TNFRSF1A, 6 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

21. (menon2024caughtinthe pages 1-4): Namita Menon, Kaushiki K, Moushmi Goswami, Anmol Singh, and Subhashini Srinivasan. Caught in the act of triplication: tnf superfamily. bioRxiv, Jul 2024. URL: https://doi.org/10.1101/2024.07.27.603686, doi:10.1101/2024.07.27.603686. This article has 0 citations.

22. (menon2024caughtinthe pages 8-11): Namita Menon, Kaushiki K, Moushmi Goswami, Anmol Singh, and Subhashini Srinivasan. Caught in the act of triplication: tnf superfamily. bioRxiv, Jul 2024. URL: https://doi.org/10.1101/2024.07.27.603686, doi:10.1101/2024.07.27.603686. This article has 0 citations.

23. (huang2025identificationandcharacterization pages 4-6): Zongjian Huang, Nan Shi, Zhenqiu Luo, Fangfang Chen, Xunwei Feng, Yongjing Lai, Jian Li, Xiang Yi, Wei Xia, and Anzhou Tang. Identification and characterization of the tumor necrosis factor receptor superfamily in the chinese tree shrew (tupaia belangeri chinensis). BMC Genomics, Apr 2025. URL: https://doi.org/10.1186/s12864-025-11451-x, doi:10.1186/s12864-025-11451-x. This article has 1 citations and is from a peer-reviewed journal.

24. (huang2025identificationandcharacterization pages 10-14): Zongjian Huang, Nan Shi, Zhenqiu Luo, Fangfang Chen, Xunwei Feng, Yongjing Lai, Jian Li, Xiang Yi, Wei Xia, and Anzhou Tang. Identification and characterization of the tumor necrosis factor receptor superfamily in the chinese tree shrew (tupaia belangeri chinensis). BMC Genomics, Apr 2025. URL: https://doi.org/10.1186/s12864-025-11451-x, doi:10.1186/s12864-025-11451-x. This article has 1 citations and is from a peer-reviewed journal.

25. (huang2025identificationandcharacterization pages 14-15): Zongjian Huang, Nan Shi, Zhenqiu Luo, Fangfang Chen, Xunwei Feng, Yongjing Lai, Jian Li, Xiang Yi, Wei Xia, and Anzhou Tang. Identification and characterization of the tumor necrosis factor receptor superfamily in the chinese tree shrew (tupaia belangeri chinensis). BMC Genomics, Apr 2025. URL: https://doi.org/10.1186/s12864-025-11451-x, doi:10.1186/s12864-025-11451-x. This article has 1 citations and is from a peer-reviewed journal.

26. (huang2025identificationandcharacterization pages 6-10): Zongjian Huang, Nan Shi, Zhenqiu Luo, Fangfang Chen, Xunwei Feng, Yongjing Lai, Jian Li, Xiang Yi, Wei Xia, and Anzhou Tang. Identification and characterization of the tumor necrosis factor receptor superfamily in the chinese tree shrew (tupaia belangeri chinensis). BMC Genomics, Apr 2025. URL: https://doi.org/10.1186/s12864-025-11451-x, doi:10.1186/s12864-025-11451-x. This article has 1 citations and is from a peer-reviewed journal.

27. (huang2025identificationandcharacterization pages 1-2): Zongjian Huang, Nan Shi, Zhenqiu Luo, Fangfang Chen, Xunwei Feng, Yongjing Lai, Jian Li, Xiang Yi, Wei Xia, and Anzhou Tang. Identification and characterization of the tumor necrosis factor receptor superfamily in the chinese tree shrew (tupaia belangeri chinensis). BMC Genomics, Apr 2025. URL: https://doi.org/10.1186/s12864-025-11451-x, doi:10.1186/s12864-025-11451-x. This article has 1 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](PTHR46861-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](PTHR46861-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. uversky2017functionalityofintrinsic pages 24-27
2. menon2024caughtinthe pages 11-13
3. green2022thedeathreceptor pages 6-8
4. dong2022alterationsinbone pages 2-4
5. menon2024caughtinthe pages 1-4
6. huang2025identificationandcharacterization pages 4-6
7. huang2025identificationandcharacterization pages 6-10
8. huang2025identificationandcharacterization pages 1-2
9. uversky2017functionalityofintrinsic pages 21-24
10. lo2025tnfreceptorsstructurefunction pages 1-3
11. bastos2024theroleof pages 1-2
12. bastos2024theroleof pages 2-5
13. alim2024molecularmechanismsof pages 1-3
14. dong2022alterationsinbone pages 1-2
15. xu2025theroleof pages 2-3
16. menon2024caughtinthe pages 8-11
17. huang2025identificationandcharacterization pages 10-14
18. huang2025identificationandcharacterization pages 14-15
19. https://doi.org/10.1186/s12967-025-06122-0,
20. https://doi.org/10.1111/febs.14182,
21. https://doi.org/10.1016/j.bbamem.2024.184394,
22. https://doi.org/10.3390/immuno4010002,
23. https://doi.org/10.3389/fcell.2023.1267837,
24. https://doi.org/10.1101/cshperspect.a041053,
25. https://doi.org/10.1101/2024.07.27.603686,
26. https://doi.org/10.1016/j.coi.2023.102409,
27. https://doi.org/10.3389/fphar.2022.905535,
28. https://doi.org/10.1038/s41698-025-00990-x,
29. https://doi.org/10.3390/cancers15174299,
30. https://doi.org/10.1186/s12864-025-11451-x,