---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-28T19:00:30.558105'
end_time: '2026-06-28T19:20:39.299601'
duration_seconds: 1208.74
template_file: templates/module_research.md.j2
template_variables:
  module_title: Glucocorticoid receptor signaling pathway module
  module_summary: Glucocorticoid receptor signaling couples steroid ligand binding,
    HSP90/co-chaperone regulation, nuclear translocation, and co-regulator exchange
    to anti-inflammatory and metabolic transcriptional programs.
  module_outline: "- Glucocorticoid receptor signaling pathway\n  - 1. glucocorticoid\
    \ receptor chaperone cycle\n  - Glucocorticoid receptor chaperone cycle\n    -\
    \ HSP90 chaperone (molecular player: HSP90 chaperone family/ortholog group)\n\
    \    - FKBP5 co-chaperone (molecular player: FKBP5 co-chaperone family/ortholog\
    \ group)\n    - Ligand-activated glucocorticoid receptor (molecular player: NR3C1)\n\
    \  - 2. glucocorticoid receptor activation\n  - Glucocorticoid receptor activation\n\
    \    - Glucocorticoid receptor (molecular player: NR3C1)\n    - Nuclear receptor\
    \ coactivator 1 (molecular player: NCOA1)\n  - 3. glucocorticoid transcriptional\
    \ output\n  - Glucocorticoid transcriptional output\n    - Nuclear receptor coactivator\
    \ 2 (molecular player: NCOA2)\n    - Nuclear receptor corepressor (molecular player:\
    \ NCOR1)\n    - NR3C1 transcriptional receptor (molecular player: NR3C1)"
  module_connections: '- Glucocorticoid receptor chaperone cycle causes Glucocorticoid
    receptor activation: The initiating event promotes glucocorticoid receptor activation.

    - Glucocorticoid receptor activation causes Glucocorticoid transcriptional output:
    Glucocorticoid receptor activation leads to glucocorticoid transcriptional output.'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 56
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: glucocorticoid_receptor_signaling-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: glucocorticoid_receptor_signaling-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
---

## Question

# Commissioned Review Brief

## Review Topic

Glucocorticoid receptor signaling pathway module

## Working Scope

Glucocorticoid receptor signaling couples steroid ligand binding, HSP90/co-chaperone regulation, nuclear translocation, and co-regulator exchange to anti-inflammatory and metabolic transcriptional programs.

## Provisional Biological Outline

- Glucocorticoid receptor signaling pathway
  - 1. glucocorticoid receptor chaperone cycle
  - Glucocorticoid receptor chaperone cycle
    - HSP90 chaperone (molecular player: HSP90 chaperone family/ortholog group)
    - FKBP5 co-chaperone (molecular player: FKBP5 co-chaperone family/ortholog group)
    - Ligand-activated glucocorticoid receptor (molecular player: NR3C1)
  - 2. glucocorticoid receptor activation
  - Glucocorticoid receptor activation
    - Glucocorticoid receptor (molecular player: NR3C1)
    - Nuclear receptor coactivator 1 (molecular player: NCOA1)
  - 3. glucocorticoid transcriptional output
  - Glucocorticoid transcriptional output
    - Nuclear receptor coactivator 2 (molecular player: NCOA2)
    - Nuclear receptor corepressor (molecular player: NCOR1)
    - NR3C1 transcriptional receptor (molecular player: NR3C1)

## Known Relationships Among Steps

- Glucocorticoid receptor chaperone cycle causes Glucocorticoid receptor activation: The initiating event promotes glucocorticoid receptor activation.
- Glucocorticoid receptor activation causes Glucocorticoid transcriptional output: Glucocorticoid receptor activation leads to glucocorticoid transcriptional output.

## Assignment

Write a rigorous, review-style synthesis suitable for a molecular biology
audience. Treat the topic as a biological system whose boundaries, core
mechanisms, variants, and unresolved points should be made clear to readers who
know the field but are not specialists in this specific process.

The review should be explanatory rather than encyclopedic. Anchor broad claims
in primary literature or authoritative reviews, but keep the focus on how the
system works and how its parts fit together.

## Questions To Address

1. **Scope and boundaries**
   - What exactly is included in this biological system?
   - Which neighboring pathways, organelle processes, complexes, or regulatory
     events are often confused with it but should be treated separately?
   - Are there competing definitions in the literature?

2. **Core mechanism**
   - What is the best current model for the sequence of events?
   - Which steps are obligatory, which are conditional, and which are accessory?
   - What molecular assemblies, enzymes, receptors, adaptors, transporters, or
     structural units carry out each major step?

3. **Variation**
   - How does the system vary across major evolutionary lineages?
   - Are there well-supported differences between cell types, tissues,
     developmental stages, physiological states, or compartments?
   - Where are there alternative routes that achieve a similar outcome by
     different molecular means?

4. **Conservation and origin**
   - What is the deepest plausible evolutionary origin of the system?
   - Which parts appear ancient and conserved, and which appear to be later
     elaborations, replacements, or lineage-specific losses?
   - When a protein family has expanded, which family members are the best
     representatives for understanding the ancestral role?

5. **Physical and biological constraints**
   - What steps must occur in a particular order?
   - Which events are mutually exclusive, compartment-specific, cell-type
     specific, substrate-specific, or stage-specific?
   - What evidence rules out otherwise plausible paths through the system?

6. **Evidence and controversy**
   - Which mechanistic claims are strongly supported by experiments?
   - Where does the literature disagree, rely on indirect evidence, or mix data
     from organisms that may not be comparable?
   - What are the most important open questions?

## Output Format

Use the style and structure of a concise review article:

1. Executive summary
2. Definition and biological boundaries
3. Mechanistic overview
4. Major molecular players and active assemblies
5. Evolutionary and cell-biological variation
6. Constraints, dependencies, and failure modes
7. Controversies and open questions
8. Key references

Include citations for major claims, preferably PMIDs or DOIs. Be explicit about
uncertainty and avoid overgeneralizing from one organism, cell type, or assay
system to all biology.

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

# Commissioned Review Brief

## Review Topic

Glucocorticoid receptor signaling pathway module

## Working Scope

Glucocorticoid receptor signaling couples steroid ligand binding, HSP90/co-chaperone regulation, nuclear translocation, and co-regulator exchange to anti-inflammatory and metabolic transcriptional programs.

## Provisional Biological Outline

- Glucocorticoid receptor signaling pathway
  - 1. glucocorticoid receptor chaperone cycle
  - Glucocorticoid receptor chaperone cycle
    - HSP90 chaperone (molecular player: HSP90 chaperone family/ortholog group)
    - FKBP5 co-chaperone (molecular player: FKBP5 co-chaperone family/ortholog group)
    - Ligand-activated glucocorticoid receptor (molecular player: NR3C1)
  - 2. glucocorticoid receptor activation
  - Glucocorticoid receptor activation
    - Glucocorticoid receptor (molecular player: NR3C1)
    - Nuclear receptor coactivator 1 (molecular player: NCOA1)
  - 3. glucocorticoid transcriptional output
  - Glucocorticoid transcriptional output
    - Nuclear receptor coactivator 2 (molecular player: NCOA2)
    - Nuclear receptor corepressor (molecular player: NCOR1)
    - NR3C1 transcriptional receptor (molecular player: NR3C1)

## Known Relationships Among Steps

- Glucocorticoid receptor chaperone cycle causes Glucocorticoid receptor activation: The initiating event promotes glucocorticoid receptor activation.
- Glucocorticoid receptor activation causes Glucocorticoid transcriptional output: Glucocorticoid receptor activation leads to glucocorticoid transcriptional output.

## Assignment

Write a rigorous, review-style synthesis suitable for a molecular biology
audience. Treat the topic as a biological system whose boundaries, core
mechanisms, variants, and unresolved points should be made clear to readers who
know the field but are not specialists in this specific process.

The review should be explanatory rather than encyclopedic. Anchor broad claims
in primary literature or authoritative reviews, but keep the focus on how the
system works and how its parts fit together.

## Questions To Address

1. **Scope and boundaries**
   - What exactly is included in this biological system?
   - Which neighboring pathways, organelle processes, complexes, or regulatory
     events are often confused with it but should be treated separately?
   - Are there competing definitions in the literature?

2. **Core mechanism**
   - What is the best current model for the sequence of events?
   - Which steps are obligatory, which are conditional, and which are accessory?
   - What molecular assemblies, enzymes, receptors, adaptors, transporters, or
     structural units carry out each major step?

3. **Variation**
   - How does the system vary across major evolutionary lineages?
   - Are there well-supported differences between cell types, tissues,
     developmental stages, physiological states, or compartments?
   - Where are there alternative routes that achieve a similar outcome by
     different molecular means?

4. **Conservation and origin**
   - What is the deepest plausible evolutionary origin of the system?
   - Which parts appear ancient and conserved, and which appear to be later
     elaborations, replacements, or lineage-specific losses?
   - When a protein family has expanded, which family members are the best
     representatives for understanding the ancestral role?

5. **Physical and biological constraints**
   - What steps must occur in a particular order?
   - Which events are mutually exclusive, compartment-specific, cell-type
     specific, substrate-specific, or stage-specific?
   - What evidence rules out otherwise plausible paths through the system?

6. **Evidence and controversy**
   - Which mechanistic claims are strongly supported by experiments?
   - Where does the literature disagree, rely on indirect evidence, or mix data
     from organisms that may not be comparable?
   - What are the most important open questions?

## Output Format

Use the style and structure of a concise review article:

1. Executive summary
2. Definition and biological boundaries
3. Mechanistic overview
4. Major molecular players and active assemblies
5. Evolutionary and cell-biological variation
6. Constraints, dependencies, and failure modes
7. Controversies and open questions
8. Key references

Include citations for major claims, preferably PMIDs or DOIs. Be explicit about
uncertainty and avoid overgeneralizing from one organism, cell type, or assay
system to all biology.

# Glucocorticoid Receptor Signaling Pathway Module: A Mechanistic Review

## 1. Executive Summary

The glucocorticoid receptor (GR, encoded by *NR3C1*) signaling pathway is a tripartite system connecting steroid hormone sensing in the cytoplasm to gene-regulatory programs in the nucleus. The pathway comprises three obligatory, sequentially linked steps: (i) an HSP90/HSP70-dependent chaperone cycle that maintains GR in a ligand-competent conformation and is gated by the antagonistic co-chaperones FKBP51 and FKBP52; (ii) ligand-driven receptor activation involving conformational change, hyperphosphorylation, nuclear localization signal exposure, and FKBP52/dynein-mediated nuclear translocation; and (iii) context-specific transcriptional output determined by GR interaction with glucocorticoid response elements (GREs), co-regulators (including NCOA1/SRC-1, NCOA2/GRIP1, NCOR1, p300/CBP), lineage-specific pioneer transcription factors, and chromatin accessibility landscapes. Emerging evidence implicates liquid–liquid phase separation (LLPS) as an additional organizational layer. Despite more than four decades of research, several central questions remain unresolved, including how GR achieves gene-level selectivity, why the transactivation/transrepression dissociation hypothesis has largely failed in clinical translation, and what the precise physiological contribution of GR condensates is.

## 2. Definition and Biological Boundaries

### 2.1 What is included

The GR signaling pathway module, as defined here, encompasses the molecular events from glucocorticoid ligand arrival at the cytoplasmic GR–chaperone complex through to transcriptional output at target genes. It includes the HSP90/HSP70 chaperone cycle and its co-chaperone regulators (FKBP51, FKBP52, p23, HOP), the ligand-induced activation and nuclear translocation machinery, and the nuclear co-regulator exchange that drives transactivation and transrepression of GR target genes (su2025glucocorticoidreceptorsignaling pages 2-3, noddings2023cryoemrevealshow pages 9-10, lockett2024theglucocorticoidreceptor pages 7-8).

### 2.2 What should be treated separately

Several neighboring systems are often conflated with GR signaling but should be considered distinct modules:

- **Mineralocorticoid receptor (MR, *NR3C2*) signaling.** MR and GR are close paralogs sharing chaperone machinery and some genomic binding sites, but MR has ~10-fold higher affinity for endogenous cortisol/corticosterone and serves a partially distinct physiological role in electrolyte homeostasis and neuronal function. MR/GR heterodimers represent a functionally distinct entity (grossmann2022structuralandmolecular pages 1-2).
- **Hypothalamic–pituitary–adrenal (HPA) axis regulation.** GR is a critical effector of the negative feedback loop in the HPA axis, but the neuroendocrine circuits governing ACTH and cortisol release operate at a different organizational level (gans2021glucocorticoidmediateddevelopmentalprogramming pages 10-11).
- **Non-genomic kinase cascades.** GR engages cytoplasmic kinase pathways (PI3K/Akt, JNK, LCK/FYN) within seconds to minutes of ligand binding, but these rapid nongenomic effects are mechanistically distinct from the canonical chaperone→nucleus→transcription module and are best treated as a parallel branch rather than a sequential step (lockett2024theglucocorticoidreceptor pages 9-10, lockett2024theglucocorticoidreceptor pages 8-9, vettorazzi2022aguideto pages 3-4).
- **11β-HSD1/2-mediated pre-receptor metabolism.** Tissue-specific interconversion of cortisone and cortisol occurs upstream of receptor binding and is a separate regulatory layer.

### 2.3 Competing definitions

There is no major definitional controversy about the core GR signaling pathway. However, the field has progressively expanded the concept from a simple "ligand-binds-receptor-activates-gene" model to include nongenomic signaling, GR condensate biology, and GR isoform-specific functions. Whether nongenomic GR effects are truly part of "GR signaling" or represent a distinct module remains a matter of scope (lockett2024theglucocorticoidreceptor pages 9-10, vettorazzi2022aguideto pages 3-4).

## 3. Mechanistic Overview

The following table summarizes the three sequential steps of the pathway module, their molecular requirements, and regulatory inputs:

| Step Name | Key Molecular Events | Required Components | Obligatory vs Conditional Status | Compartment | Key Regulatory Inputs |
|---|---|---|---|---|---|
| 1. Glucocorticoid receptor chaperone cycle | Newly synthesized or recycled GR is maintained in a ligand-responsive but transcriptionally inactive heterocomplex. Hsp70 first captures and partially unfolds GR, suppressing ligand binding; GR is then transferred to an Hsp90:Hop loading complex. ATP-driven Hsp90 remodeling releases Hsp70/Hop and permits p23 binding, generating the maturation complex in which GR is refolded and ligand binding competence is restored. Cryo-EM studies indicate that mature ligand-bound GR is stabilized on Hsp90 and protected from Hsp70 rebinding; FKBP51 or FKBP52 can then bind the GR:Hsp90 complex in a mutually exclusive manner, with similar overall architecture but functionally distinct FK1-domain contacts. FKBP52 promotes progression to a transport-competent state, whereas FKBP51 favors cytosolic retention/recycling through the chaperone cycle. A key structural determinant is FKBP52 Pro119 versus FKBP51 Leu119 in the proline-rich loop, which alters GR engagement and potentiation. (noddings2023cryoemrevealshow pages 9-10, noddings2023cryoemrevealshow pages 8-9, noddings2023cryoemrevealshow pages 1-2, noddings2023cryoemrevealshow pages 6-7, noddings2023cryoemrevealshow pages 7-8, noddings2023cryoemrevealshow pages 4-5) | NR3C1/GR, HSP70, HSP90, HOP/STIP1, PTGES3/p23, FKBP5/FKBP51 and/or FKBP4/FKBP52, ATP; classically Hsp40 and other co-chaperones contribute upstream. (noddings2023cryoemrevealshow pages 9-10, noddings2023cryoemrevealshow pages 8-9, noddings2023cryoemrevealshow pages 1-2, lockett2024theglucocorticoidreceptor pages 7-8) | Obligatory for canonical high-affinity GR signaling: Hsp70→Hsp90 loading/maturation and Hsp90-dependent ligand-competent GR. Conditional/accessory: exact co-chaperone composition, FKBP51↔FKBP52 exchange, rate of recycling, and dynein coupling vary by cell context. (noddings2023cryoemrevealshow pages 9-10, noddings2023cryoemrevealshow pages 1-2, lockett2024theglucocorticoidreceptor pages 7-8, su2025glucocorticoidreceptorsignaling pages 7-8) | Cytoplasm, with Hsp90-associated complexes persisting during transit and some components detectable in nucleus. (lockett2024theglucocorticoidreceptor pages 7-8, grossmann2022structuralandmolecular pages 6-7) | Glucocorticoid availability; Hsp90 ATPase cycle; relative FKBP51:FKBP52 abundance; FKBP5 induction as GR-dependent negative feedback; post-translational modification of GR and co-chaperones; proteostasis pressure and CHIP/proteasome routing when Hsp90 function fails. (noddings2023cryoemrevealshow pages 9-10, grossmann2022structuralandmolecular pages 6-7, lockett2024theglucocorticoidreceptor pages 15-15) |
| 2. Glucocorticoid receptor activation | Ligand binding to mature GR triggers conformational change, hyperphosphorylation, exposure of NLS motifs in the DBD/hinge and LBD, and remodeling of the heterocomplex. In many models, FKBP5/FKBP51 is replaced by FKBP4/FKBP52, which links the complex to dynein/dynactin for microtubule-based retrograde trafficking to the nucleus. Activated GR accumulates in the nucleus, where it can bind DNA as monomer/dimer/tetramer depending on context and may undergo further structural transitions. DNA binding itself can alter GR quaternary organization and transcriptional competence. In parallel, a subset of GR actions is rapid and non-genomic, involving cytoplasmic or membrane-associated GR modulation of kinase pathways such as PI3K/Akt, JNK, LCK/FYN, and calcium signaling. (su2025glucocorticoidreceptorsignaling pages 2-3, lockett2024theglucocorticoidreceptor pages 7-8, noddings2023cryoemrevealshow pages 9-10, su2025glucocorticoidreceptorsignaling pages 7-8, lockett2024theglucocorticoidreceptor pages 9-10, lockett2024theglucocorticoidreceptor pages 8-9, vettorazzi2022aguideto pages 2-3) | Ligand-bound GR, exposed NLSs, import machinery, FKBP52-dynein/dynactin axis for efficient canonical trafficking, intact microtubule transport, and permissive phosphorylation state of GR. (su2025glucocorticoidreceptorsignaling pages 2-3, lockett2024theglucocorticoidreceptor pages 7-8, su2025glucocorticoidreceptorsignaling pages 7-8) | Obligatory for canonical genomic signaling: ligand binding, activating conformational change, nuclear entry. Conditional/accessory: FKBP52-mediated accelerated trafficking, extent/pattern of phosphorylation, non-genomic kinase signaling, receptor oligomeric state, and isoform-specific behavior. (su2025glucocorticoidreceptorsignaling pages 2-3, noddings2023cryoemrevealshow pages 9-10, su2025glucocorticoidreceptorsignaling pages 7-8, lockett2024theglucocorticoidreceptor pages 9-10, lockett2024theglucocorticoidreceptor pages 8-9) | Cytoplasm → nucleus; non-genomic branch also at plasma membrane/cytoplasm. (su2025glucocorticoidreceptorsignaling pages 2-3, lockett2024theglucocorticoidreceptor pages 9-10, vettorazzi2022aguideto pages 3-4, vettorazzi2022aguideto pages 2-3) | Ligand identity and dose; GR isoform composition (GRα vs GRβ and translational isoforms); phosphorylation at sites such as S203/S211/S226; competition between FKBP51 and FKBP52; cell-state signals impinging through MAPKs and other kinases. (lockett2024theglucocorticoidreceptor pages 15-15, su2025glucocorticoidreceptorsignaling pages 2-3, lockett2024theglucocorticoidreceptor pages 11-12, lockett2024theglucocorticoidreceptor pages 13-13, noddings2023cryoemrevealshow pages 9-10, su2025glucocorticoidreceptorsignaling pages 7-8) |
| 3. Glucocorticoid transcriptional output | Nuclear GR engages a context-specific cistrome dominated by pre-accessible chromatin and lineage-defined enhancers. Canonical transactivation involves GR binding GREs and recruiting coactivators (for example NCOA1/SRC-1, NCOA2/GRIP1/SRC-2, p300/CBP, Mediator, chromatin remodelers) to remodel chromatin and promote Pol II transcription. Repression can occur through multiple mechanisms: direct binding at negative GREs with NCoR/SMRT-HDAC complexes, competition/composite binding at shared regulatory elements, and selective protein-protein interactions with inflammatory TFs such as NF-κB or AP-1; however, genome-wide evidence indicates that direct DNA binding and chromatin context are more prominent than a simple global “tethering-only” model. Recent work adds phase separation/condensate formation as a likely organizational layer: ligand-bound GR forms liquid-like nuclear condensates/foci via IDRs, recruits MED1/BRD4/NCOA-family factors, can partition activating versus repressive assemblies, and couples enhancer clusters/super-enhancers to long-range chromatin contacts and transcriptional output. (martinez2024glucocorticoidstheiruses pages 19-20, mechtidou2022involvementofchromatin pages 28-29, lockett2024theglucocorticoidreceptor pages 8-9, lockett2024theglucocorticoidreceptor pages 19-19, vettorazzi2022aguideto pages 6-7, fargason2025endocrineexamplesof pages 8-9, pinheiro2023phaseseparationapossible pages 3-5, pinheiro2023phaseseparationapossible pages 5-6, fargason2025endocrineexamplesof pages 2-4, mechtidou2022involvementofchromatin pages 22-23, borin2023emergingepigeneticand pages 10-11) | Nuclear GR, GRE-containing chromatin, cell-type-specific pioneer factors/open chromatin, coactivators (NCOA1, NCOA2, p300/CBP), corepressors (NCOR1/NCOR2/SMRT, HDAC2/HDAC3-associated complexes), Pol II machinery; for condensate-based organization, GR IDRs and multivalent co-regulator interactions are important. (martinez2024glucocorticoidstheiruses pages 19-20, mechtidou2022involvementofchromatin pages 28-29, lockett2024theglucocorticoidreceptor pages 19-19, fargason2025endocrineexamplesof pages 8-9, pinheiro2023phaseseparationapossible pages 3-5, vettorazzi2022aguideto pages 6-7) | Obligatory for genomic output: nuclear GR, chromatin engagement, and some form of co-regulator exchange. Conditional/accessory: whether a given locus is activated vs repressed, requirement for dimer/tetramer states, condensate formation, and dependence on specific pioneer factors/coregulators are highly gene- and cell-type-specific. Phase separation is increasingly supported but should still be treated as an emergent organizing principle rather than a universally required step at every GR target. (vettorazzi2022aguideto pages 6-7, fargason2025endocrineexamplesof pages 8-9, pinheiro2023phaseseparationapossible pages 5-6, fargason2025endocrineexamplesof pages 2-4, lockett2024theglucocorticoidreceptor pages 19-19, lockett2024theglucocorticoidreceptor pages 19-20) | Nucleus | Chromatin accessibility landscape; pioneer/lineage TFs (for example AP-1, PU.1, C/EBP, FoxA1/GATA in relevant tissues); availability of NCOA versus NCOR/SMRT complexes; histone acetylation/deacetylation status; DNA motif grammar (GRE vs nGRE vs composite sites); condensate biophysics and enhancer clustering; inflammatory signaling context. (martinez2024glucocorticoidstheiruses pages 19-20, lockett2024theglucocorticoidreceptor pages 19-19, vettorazzi2022aguideto pages 6-7, fargason2025endocrineexamplesof pages 8-9, fargason2025endocrineexamplesof pages 2-4, mechtidou2022involvementofchromatin pages 22-23, borin2023emergingepigeneticand pages 10-11, lockett2024theglucocorticoidreceptor pages 19-20) |


*Table: This table summarizes the three sequential steps of the glucocorticoid receptor signaling pathway module, integrating canonical chaperone-dependent activation with newer structural and condensate-based models. It is useful as a compact mechanistic map linking cytoplasmic maturation, nuclear entry, and context-specific transcriptional output.*

### 3.1 Step 1: The Chaperone Cycle

In the unliganded state, GRα resides in the cytoplasm bound to a multi-protein complex comprising HSP90, HSP70, co-chaperone p23, and immunophilins FKBP51 and FKBP52 (su2025glucocorticoidreceptorsignaling pages 2-3, lockett2024theglucocorticoidreceptor pages 7-8). The cycle proceeds through three defined intermediate complexes revealed by structural studies:

1. **GR-loading complex.** HSP70 (with HSP40) initially captures and partially unfolds GR, inactivating the ligand-binding domain. HSP70 then transfers GR to an HSP90:HOP loading complex, where GR remains partially unfolded and unable to bind cortisol (noddings2023cryoemrevealshow pages 8-9, noddings2023cryoemrevealshow pages 1-2).
2. **GR-maturation complex.** ATP hydrolysis by HSP90 drives release of HSP70 and HOP, and p23 binds to stabilize the closed HSP90 conformation. HSP90 refolds GR to its native, ligand-competent state, and cortisol can now bind (noddings2023cryoemrevealshow pages 9-10, noddings2023cryoemrevealshow pages 1-2).
3. **FKBP-engaged complex.** Either FKBP51 or FKBP52 replaces p23 on the mature GR:HSP90 complex in a mutually exclusive manner. Recent cryo-EM structures at 3.01 Å (GR:Hsp90:FKBP52) and 3.23 Å (GR:Hsp90:FKBP51) resolution reveal that the two complexes are architecturally near-identical, but functionally opposite (noddings2023cryoemrevealshow pages 6-7, noddings2023cryoemrevealshow pages 1-2, noddings2023cryoemrevealshow pages 2-3). The critical determinant is a single residue difference in the FK1-domain proline-rich loop: **FKBP52 contains Pro119, while FKBP51 contains Leu119**. Swapping this residue reverses the functional effects of each immunophilin both in vitro and in vivo (noddings2023cryoemrevealshow pages 6-7, noddings2023cryoemrevealshow pages 7-8, noddings2023cryoemrevealshow pages 8-9). FKBP52 Pro119 reduces loop dynamics, stabilizes the GR–FK1 interface, and enhances ligand-binding affinity. An adjacent phosphorylation site (S118) unique to FKBP52 further tunes potentiation, potentially through proline-directed kinase recruitment (noddings2023cryoemrevealshow pages 4-5).

Crucially, GR activation induces FKBP51 (but not FKBP52) gene expression, establishing a **negative feedback loop** that dampens chronic GR signaling by shifting the FKBP51:FKBP52 ratio toward cytosolic sequestration (noddings2023cryoemrevealshow pages 9-10).

### 3.2 Step 2: Receptor Activation and Nuclear Translocation

Upon glucocorticoid binding, GR undergoes conformational change and becomes hyperphosphorylated at key serine residues (S203, S211, S226) in the AF1 domain (su2025glucocorticoidreceptorsignaling pages 2-3). This exposes two nuclear localization signals—NLS1 at the DBD/hinge junction and NLS2 in the LBD—and triggers exchange of FKBP51 for FKBP52 within the heterocomplex (su2025glucocorticoidreceptorsignaling pages 2-3, lockett2024theglucocorticoidreceptor pages 7-8). FKBP52 then couples the activated GR:HSP90 complex to the **dynein/dynactin motor** for microtubule-dependent retrograde transport toward the nucleus (su2025glucocorticoidreceptorsignaling pages 7-8, li2025fk506‑bindingproteinsas pages 5-7). FKBP51 shows weaker dynein binding, consistent with its role in delaying nuclear import (su2025glucocorticoidreceptorsignaling pages 7-8).

HSP90 remains associated during nuclear translocation and is detectable in both cytoplasmic and nuclear compartments; its inhibition impairs not only translocation but also subsequent transcriptional activity (grossmann2022structuralandmolecular pages 6-7).

**Nongenomic branch.** In parallel, a fraction of ligand-activated GR mediates rapid, transcription-independent effects. These include PI3K/Akt activation, direct cytoplasmic sequestration of NF-κB subunit p65, inhibition of JNK-mediated AP-1 activation, and TCR signaling modulation through LCK/FYN kinases (lockett2024theglucocorticoidreceptor pages 9-10, lockett2024theglucocorticoidreceptor pages 8-9, vettorazzi2022aguideto pages 2-3). A membrane-bound GR (mGR) population has been identified on immune cells (monocytes, B cells, T cells), where it rapidly activates pro-apoptotic and immune-regulatory pathways upon exposure to membrane-impermeable glucocorticoids (lockett2024theglucocorticoidreceptor pages 9-10, vettorazzi2022aguideto pages 3-4, mitreaguilar2022theroleof pages 2-4).

### 3.3 Step 3: Transcriptional Output

Nuclear GR regulates gene expression through multiple mechanisms:

**Transactivation.** GR homodimers (and potentially tetramers) bind palindromic GRE consensus sequences (AGAACA) to activate transcription by recruiting coactivators including NCOA1/SRC-1, NCOA2/GRIP1, p300/CBP, and the Mediator complex (martinez2024glucocorticoidstheiruses pages 19-20, lockett2024theglucocorticoidreceptor pages 8-9, su2025glucocorticoidreceptorsignaling pages 2-3). These coactivators promote chromatin remodeling through histone acetyltransferase activity and assembly of the RNA Polymerase II machinery.

**Transrepression.** GR represses gene expression through several mechanisms: (a) direct binding to negative GREs (nGREs) with recruitment of corepressors NCOR1, NCOR2/SMRT, and associated HDACs (mechtidou2022involvementofchromatin pages 28-29, lockett2024theglucocorticoidreceptor pages 19-19); (b) protein–protein interactions with pro-inflammatory transcription factors NF-κB and AP-1 (lockett2024theglucocorticoidreceptor pages 8-9, su2025glucocorticoidreceptorsignaling pages 2-3, vettorazzi2022aguideto pages 6-7); and (c) composite binding at shared regulatory elements (lockett2024theglucocorticoidreceptor pages 7-8). Notably, genome-wide ChIP-seq studies have shown that "pure tethering" (GR binding DNA-bound TFs without contacting DNA itself) is not a prominent mechanism at the genomic scale; direct GR DNA binding predominates even at co-occupied sites (vettorazzi2022aguideto pages 6-7).

**Cell-type specificity.** The GR cistrome—its genome-wide binding pattern—is overwhelmingly shaped by pre-existing chromatin accessibility established by lineage-determining pioneer transcription factors such as PU.1 and C/EBP in macrophages, GATA factors in other lineages, and FoxA1 in epithelial contexts. Approximately 95% of GR binding occurs at constitutively accessible chromatin regions that were open before hormone treatment (mechtidou2022involvementofchromatin pages 22-23, lockett2024theglucocorticoidreceptor pages 19-19, vettorazzi2022aguideto pages 6-7, borin2023emergingepigeneticand pages 10-11). Cell-type differences in cofactor availability—including relative NCOA1 versus NCOR1 abundance—further tune transcriptional output (lockett2024theglucocorticoidreceptor pages 19-19, lockett2024theglucocorticoidreceptor pages 19-20).

## 4. Major Molecular Players and Active Assemblies

The following table provides a comprehensive reference for the key molecular components of the GR signaling module:

| Gene/Protein Name | Aliases | Category | Function in GR Signaling | Key Regulatory Role |
|---|---|---|---|---|
| **NR3C1 / GR** | Glucocorticoid receptor; GR; GRα, GRβ | Receptor | Central steroid-activated transcription factor of the module. In the cytoplasm, GR is assembled in an HSP90/HSP70/co-chaperone complex; after ligand binding it undergoes conformational change, exposes NLS elements, translocates to the nucleus, binds GREs or interacts with other TFs, and drives anti-inflammatory and metabolic programs. GRα is the canonical ligand-binding, transcriptionally active isoform; GRβ generally does not bind glucocorticoids conventionally and can antagonize GRα-dependent transcription. (su2025glucocorticoidreceptorsignaling pages 2-3, lockett2024theglucocorticoidreceptor pages 7-8, lockett2024theglucocorticoidreceptor pages 8-9, lockett2024theglucocorticoidreceptor pages 13-13) | Signal integration node for ligand availability, PTMs, chromatin context, and cofactor choice. Isoform usage, phosphorylation, SUMOylation, ubiquitination, acetylation, and cell-type-specific cistromes alter sensitivity, nuclear trafficking, and transcriptional output. (lockett2024theglucocorticoidreceptor pages 15-15, su2025glucocorticoidreceptorsignaling pages 2-3, lockett2024theglucocorticoidreceptor pages 19-19) |
| **HSP90AA1 / HSP90AB1** | HSP90; Hsp90α; Hsp90β | Chaperone | Core ATP-dependent chaperone that loads, refolds, and stabilizes GR during the chaperone cycle. HSP90 converts HSP70-inhibited GR into a mature ligand-binding conformation and remains associated with active GR complexes that can engage FKBP co-chaperones. (noddings2023cryoemrevealshow pages 9-10, noddings2023cryoemrevealshow pages 8-9, noddings2023cryoemrevealshow pages 1-2) | Governs the loading-to-maturation transition, protects ligand-bound GR from HSP70 rebinding, and couples ATP hydrolysis to receptor maturation; HSP90 inhibition destabilizes receptor signaling and can bias GR toward degradation. (noddings2023cryoemrevealshow pages 9-10, grossmann2022structuralandmolecular pages 6-7) |
| **HSPA1A / HSP70** | HSP70; Hsp70-1A | Chaperone | Early chaperone that binds GR and locally unfolds/inactivates the ligand-binding receptor before transfer to the HSP90:Hop loading complex. This creates the substrate state needed for HSP90-dependent re-maturation. (noddings2023cryoemrevealshow pages 8-9, noddings2023cryoemrevealshow pages 1-2) | Enforces ordering of the cycle by transiently suppressing ligand binding until handoff to HSP90; excessive or persistent HSP70 engagement would be expected to oppose maturation and signaling competence. (noddings2023cryoemrevealshow pages 8-9, noddings2023cryoemrevealshow pages 1-2) |
| **FKBP5 / FKBP51** | FKBP51 | Co-chaperone | HSP90-binding immunophilin that associates with mature GR:HSP90 complexes and generally suppresses GR signaling. FKBP51 competes with FKBP52 for complex occupancy, reduces efficient nuclear translocation, and favors cytosolic sequestration/recycling through the chaperone cycle. (noddings2023cryoemrevealshow pages 9-10, lockett2024theglucocorticoidreceptor pages 7-8, su2025glucocorticoidreceptorsignaling pages 7-8) | Major negative-feedback regulator because GR activation induces FKBP51 expression, which dampens chronic GR activity. Structurally, FKBP51 is similar to FKBP52 but differs at the functionally critical FK1 proline-rich loop residue L119, contributing to antagonism of FKBP52-like potentiation. (noddings2023cryoemrevealshow pages 9-10, noddings2023cryoemrevealshow pages 6-7, noddings2023cryoemrevealshow pages 7-8) |
| **FKBP4 / FKBP52** | FKBP52 | Co-chaperone | HSP90-binding immunophilin that promotes GR activity after ligand binding. FKBP52 associates with mature GR:HSP90 complexes, enhances ligand-binding competence, and promotes rapid nuclear import through coupling to the dynein motor machinery. (noddings2023cryoemrevealshow pages 9-10, noddings2023cryoemrevealshow pages 8-9, lockett2024theglucocorticoidreceptor pages 7-8, su2025glucocorticoidreceptorsignaling pages 7-8) | Positive trafficking and activation factor. Cryo-EM and functional studies identify the FK1-domain proline-rich loop, especially **P119** (and adjacent S118 context), as critical for GR potentiation; residue swapping between FKBP51/52 reverses function. (noddings2023cryoemrevealshow pages 6-7, noddings2023cryoemrevealshow pages 7-8, noddings2023cryoemrevealshow pages 8-9, noddings2023cryoemrevealshow pages 4-5) |
| **PTGES3 / p23** | p23 | Co-chaperone | Late HSP90 co-chaperone that stabilizes the ATP-bound HSP90 maturation complex containing folded, ligand-competent GR. p23 helps preserve the active state and shields GR from HSP70 rebinding. (noddings2023cryoemrevealshow pages 9-10, noddings2023cryoemrevealshow pages 1-2) | Stabilizes mature GR:HSP90 assemblies and sets the stage for subsequent FKBP51/FKBP52 exchange. Competition between p23 and FKBP immunophilins influences progression from maturation toward trafficking/activation. (noddings2023cryoemrevealshow pages 9-10) |
| **STIP1 / HOP** | HOP; STI1 | Co-chaperone | Adaptor that bridges HSP70 and HSP90 in the GR loading complex, facilitating transfer of partially unfolded GR from HSP70 into HSP90 for subsequent maturation. (noddings2023cryoemrevealshow pages 8-9, grossmann2022structuralandmolecular pages 5-6) | Organizes early assembly of the loading complex; release of Hop is a key transition step that permits ATP-driven remodeling, p23 recruitment, and productive receptor maturation. (noddings2023cryoemrevealshow pages 1-2, grossmann2022structuralandmolecular pages 5-6) |
| **NCOA1** | SRC-1; steroid receptor coactivator-1 | Co-activator | Canonical nuclear receptor coactivator recruited to activated GR, mainly through AF-2/LxxLL interactions and AF-1-supported assemblies. NCOA1 helps stimulate transcription by promoting chromatin opening and recruitment of the basal transcription apparatus. (martinez2024glucocorticoidstheiruses pages 19-20, mechtidou2022involvementofchromatin pages 28-29) | Functions as a chromatin-remodeling and transcription-amplifying coactivator; tissue-specific abundance contributes to cell-type differences in GR target-gene activation. (lockett2024theglucocorticoidreceptor pages 19-19, lockett2024theglucocorticoidreceptor pages 19-20) |
| **NCOA2** | GRIP1; SRC-2; TIF2 | Co-activator | Multifunctional GR co-regulator that can act prominently in GR-dependent transcriptional activation and, in some inflammatory contexts, in repression complexes. It supports assembly of transcriptional machinery and context-dependent regulation of inflammatory genes. (martinez2024glucocorticoidstheiruses pages 19-20, lockett2024theglucocorticoidreceptor pages 19-19) | Important determinant of promoter- and context-specific output; highlights that GR coactivators are not simple “on switches” but can shape both positive and negative regulatory programs depending on chromatin and TF context. (martinez2024glucocorticoidstheiruses pages 19-20, vettorazzi2022aguideto pages 6-7) |
| **NCOR1** | NCoR1; nuclear receptor corepressor 1 | Co-repressor | Corepressor recruited in GR-mediated repression, especially at negative GRE-linked or repressive assemblies. NCOR1 participates in chromatin compaction and transcriptional silencing, often through HDAC3/HDAC-containing complexes. (mechtidou2022involvementofchromatin pages 28-29, lockett2024theglucocorticoidreceptor pages 19-19) | Central factor for direct repression modules and for the older nGRE/corepressor model of GR-mediated silencing; availability of NCOR1 contributes to cell-specific glucocorticoid sensitivity and repression competence. (lockett2024theglucocorticoidreceptor pages 19-19, lockett2024theglucocorticoidreceptor pages 19-20) |
| **NCOR2** | SMRT; silencing mediator for retinoid and thyroid receptors | Co-repressor | Closely related corepressor that partners with GR in repressive transcriptional complexes, particularly at negative GRE or composite regulatory sites, helping recruit histone deacetylase activity and suppress transcription. (mechtidou2022involvementofchromatin pages 28-29, lockett2024theglucocorticoidreceptor pages 19-19) | Reinforces promoter- and context-dependent repression and supports the view that repression can require dedicated corepressor machinery rather than passive exclusion of coactivators. (lockett2024theglucocorticoidreceptor pages 7-8, lockett2024theglucocorticoidreceptor pages 19-19) |
| **HDAC2** | Histone deacetylase 2 | Co-repressor / chromatin enzyme | Histone deacetylase that contributes to GR-mediated repression of inflammatory transcription, including NF-κB-linked programs, by promoting deacetylation-dependent chromatin compaction and/or deacetylation of regulatory proteins. (martinez2024glucocorticoidstheiruses pages 19-20, lockett2024theglucocorticoidreceptor pages 15-15) | Particularly important for anti-inflammatory transrepression competence; reduced HDAC2 function is associated with impaired glucocorticoid responsiveness in inflammatory settings. (martinez2024glucocorticoidstheiruses pages 19-20, lockett2024theglucocorticoidreceptor pages 15-15) |
| **EP300** | p300 | Co-activator / chromatin enzyme | Histone acetyltransferase and scaffold coactivator recruited by activated GR to enhance transcription of permissive target genes. p300 supports enhancer/promoter acetylation and assembly of active transcription complexes. (su2025glucocorticoidreceptorsignaling pages 2-3, borin2023emergingepigeneticand pages 10-11) | Couples GR occupancy to active chromatin states, especially at accessible enhancers; helps explain why chromatin context and cofactor availability strongly influence target selectivity. (lockett2024theglucocorticoidreceptor pages 19-19, borin2023emergingepigeneticand pages 10-11) |
| **CREBBP** | CBP; CREB-binding protein | Co-activator / chromatin enzyme | p300-related histone acetyltransferase and scaffold that cooperates with GR at activated loci, aiding transcription complex assembly and local chromatin acetylation. (su2025glucocorticoidreceptorsignaling pages 2-3, borin2023emergingepigeneticand pages 10-11) | Serves as a major integrator of TF cooperation at GR-bound loci and participates in context-specific enhancer activation; its recruitment depends on chromatin accessibility and collaborating TF networks. (lockett2024theglucocorticoidreceptor pages 19-19, borin2023emergingepigeneticand pages 10-11) |
| **Dynein complex** | Cytoplasmic dynein; dynein/dynactin motor | Motor/trafficking factor | Microtubule-based motor apparatus that mediates rapid retrograde transport of ligand-activated GR complexes toward the nucleus, primarily through FKBP52-linked coupling. (grossmann2022structuralandmolecular pages 6-7, noddings2023cryoemrevealshow pages 9-10, su2025glucocorticoidreceptorsignaling pages 7-8, li2025fk506‑bindingproteinsas pages 5-7) | Provides the physical transport route that makes cytoplasmic maturation productive for nuclear signaling. Preferential association with FKBP52 over FKBP51 is a key determinant of fast versus delayed nuclear import. (noddings2023cryoemrevealshow pages 9-10, su2025glucocorticoidreceptorsignaling pages 7-8) |


*Table: This table summarizes the principal receptors, chaperones, co-chaperones, coactivators, corepressors, and trafficking factors that define the glucocorticoid receptor signaling module. It is useful as a compact map of how cytoplasmic receptor maturation is coupled to nuclear transcriptional regulation and context-specific output.*

### 4.1 GR Isoforms and Translational Variants

The *NR3C1* gene produces multiple isoforms through alternative splicing and translational initiation:

- **GRα** (94 kDa, full-length): The canonical ligand-binding, transcriptionally active isoform (su2025glucocorticoidreceptorsignaling pages 2-3).
- **GRβ** (742 aa, truncated LBD): Cannot conventionally bind glucocorticoids; acts as a dominant-negative inhibitor of GRα and retains corepressor-binding capability (su2025glucocorticoidreceptorsignaling pages 2-3, lockett2024theglucocorticoidreceptor pages 11-12).
- **GRγ**: Associated with mitochondrial function pathways (lockett2024theglucocorticoidreceptor pages 11-12).
- **GR-A**: Lacks portions of the LBD due to exon 5–7 splicing (lockett2024theglucocorticoidreceptor pages 11-12).
- **GR-P**: Fails to splice between exons 7–8, lacks the carboxy-terminal LBD half including dimerization signal and AF2; comprises 4–24% of total GR mRNA in lymphocytes (lockett2024theglucocorticoidreceptor pages 11-12).
- **Translational isoforms (GRα-A, -B, -C1-3, -D1-3)**: Generated through ribosomal leaky scanning from different AUG start codons, producing progressively shorter N-terminal domains (53–94 kDa) with altered cofactor interactions but preserved DNA-binding and ligand-binding capacity (lockett2024theglucocorticoidreceptor pages 13-13).

### 4.2 Post-translational Modifications

GR function is modulated by multiple PTMs: **Phosphorylation** at S203, S211, S226 (and additional sites including T524 by MINK1, S617 by ROCK1) regulates nuclear translocation, cofactor recruitment, and transcriptional activity (lockett2024theglucocorticoidreceptor pages 15-15, su2025glucocorticoidreceptorsignaling pages 2-3, martinez2024glucocorticoidstheiruses pages 17-19). **SUMOylation** at lysine residues can increase or decrease transcriptional activity depending on promoter and tissue context; GR SUMOylation participates in SUMO-SMRT/NCoR1-HDAC3 repressive complexes (mechtidou2022involvementofchromatin pages 28-29, lockett2024theglucocorticoidreceptor pages 15-15). **Ubiquitination** at K419 in the NTD reduces transcriptional activity and promotes nuclear export (lockett2024theglucocorticoidreceptor pages 15-15). **Acetylation** in the hinge region reduces GRE-dependent transcription, while deacetylation by HDAC2 is required for effective NF-κB transrepression (lockett2024theglucocorticoidreceptor pages 15-15).

## 5. Evolutionary and Cell-Biological Variation

### 5.1 Evolutionary Origin and Conservation

GR and MR evolved through gene duplication from a common ancestral corticosteroid receptor over 450 million years ago, with a distinct MR first appearing in cartilaginous fishes (grossmann2022structuralandmolecular pages 1-2). The *NR3C1* gene is absent from invertebrate genomes—corticosteroid receptor orthologs have not been found in invertebrates (gans2021glucocorticoidmediateddevelopmentalprogramming pages 10-11). Across vertebrates, the DNA- and ligand-binding regions of GR are highly conserved; the zebrafish MR DNA-binding domain shares 97% identity with human MR (grossmann2022structuralandmolecular pages 1-2, gans2021glucocorticoidmediateddevelopmentalprogramming pages 9-10).

Zebrafish retain a single copy of the *nr3c1* gene with highly conserved DNA- and ligand-binding regions. Alternative splicing produces a lowly expressed β isoform in both zebrafish and humans, and the gene contains multiple functional translational start codons similar to the human ortholog (gans2021glucocorticoidmediateddevelopmentalprogramming pages 10-11). The HPA (HPI in fish) axis tissues and core functions are essentially conserved from fish to humans (gans2021glucocorticoidmediateddevelopmentalprogramming pages 10-11).

### 5.2 Ancient versus Derived Components

The most ancient components of the system are the HSP90 and HSP70 chaperone families, which are deeply conserved across eukaryotes. The nuclear receptor superfamily itself is metazoan, with the 3-ketosteroid receptor family being vertebrate-specific. FKBP immunophilins are broadly conserved across eukaryotes, but the FKBP51/52 regulatory pair and their antagonistic regulation of nuclear receptor trafficking appear to be a vertebrate elaboration.

### 5.3 Tissue and Cell-Type Variation

GR signaling output varies profoundly between cell types. In macrophages, GR-dependent anti-inflammatory programs require myeloid-specific GR, and GR deletion in macrophages aggravates obesity-related insulin resistance by enhancing adipose tissue inflammation (mechtidou2022involvementofchromatin pages 22-23). Hippocampal neurons show cell-type-specific coregulator profiles, with *Ncoa1* (SRC-1) being minimally expressed while *Ncoa2* (GRIP1/SRC-2) is more prominent (lockett2024theglucocorticoidreceptor pages 19-19). These differences mean that GR target gene sets are substantially non-overlapping between cell types, reinforced by tissue-specific pioneer factor landscapes (vettorazzi2022aguideto pages 6-7).

## 6. Constraints, Dependencies, and Failure Modes

### 6.1 Ordered Steps

The chaperone cycle must precede activation: HSP70 binding → HSP90 loading → maturation → ligand binding → FKBP exchange → nuclear translocation is a strictly ordered sequence (noddings2023cryoemrevealshow pages 9-10, noddings2023cryoemrevealshow pages 8-9). Nuclear translocation must precede genomic transcriptional output. Nongenomic effects, by contrast, can occur in parallel with or independently of genomic signaling (lockett2024theglucocorticoidreceptor pages 9-10).

### 6.2 Mutually Exclusive Events

FKBP51 and FKBP52 bind the GR:HSP90 complex in a mutually exclusive manner; the cellular ratio of these co-chaperones therefore determines the net rate of nuclear import (noddings2023cryoemrevealshow pages 9-10). Activating and repressive GR condensates are physically separated and non-miscible, suggesting that a given GR molecule occupies one or the other type of condensate at a given time (fargason2025endocrineexamplesof pages 8-9).

### 6.3 Failure Modes

Loss of HSP90 function (by inhibition or proteostatic stress) routes GR to CHIP-mediated ubiquitination and proteasomal degradation rather than activation (grossmann2022structuralandmolecular pages 6-7). GR isoform dysregulation—particularly elevated GRβ expression—is associated with glucocorticoid resistance in diseases including asthma, rheumatoid arthritis, and hematological malignancies (OpenTargets Search: -NR3C1). Chronic glucocorticoid exposure can reprogram FKBP5 expression epigenetically, persistently altering the FKBP51:FKBP52 balance and GR sensitivity—a mechanism implicated in stress-related psychiatric disorders.

## 7. Controversies and Open Questions

### 7.1 The Dissociation Hypothesis and SEGRAMs

The long-standing hypothesis that GR-mediated anti-inflammatory effects arise predominantly from transrepression (monomeric tethering to NF-κB/AP-1) while metabolic side effects result from transactivation (dimeric GRE binding) has driven decades of drug development. Selective GR agonists/modulators (SEGRAMs) were designed to favor transrepression while minimizing transactivation. However, this approach has had **limited clinical success** (lesovaya2022thelongwinding pages 4-5, lesovaya2022thelongwinding pages 3-4, lesovaya2022thelongwinding pages 1-2). Analysis of glucocorticoid molecular signatures across tissues showed that both full therapeutic activity and side effects require both transactivation and transrepression functions (lesovaya2022thelongwinding pages 4-5). Key clinical-stage SEGRAMs include Fosdagrocorat (discontinued), Mapracorat (clinical trials unreported), and AZD compounds (variable results); critically, no SEGRAM has reached phase III trials or been marketed (lockett2024theglucocorticoidreceptor pages 19-20, lockett2024theglucocorticoidreceptor pages 20-21). The partial agonist vamorolone represents a first-in-class dissociative steroid that achieves partial GR agonism through disruption of a specific ligand–receptor hydrogen bond, weakening coactivator but not corepressor interactions (liu2020disruptionofa pages 7-8).

Studies using GRdim mice (dimerization-deficient) further challenged the dissociation model by demonstrating that GR dimerization is actually required for most anti-inflammatory responses; simple tethering-only signaling was insufficient for resolution of complex inflammatory challenges (mechtidou2022involvementofchromatin pages 23-24).

### 7.2 Phase Separation as a Regulatory Layer

An emerging paradigm proposes that ligand-activated GR forms ~4,500 nuclear foci via liquid–liquid phase separation (LLPS), often localized at super-enhancers (fargason2025endocrineexamplesof pages 2-4). These condensates exhibit hallmark liquid-like properties (roundness, fusion, rapid FRAP recovery) and recruit MED1, BRD4, and NCOA-family members through multivalent IDR interactions (fargason2025endocrineexamplesof pages 8-9). Single-molecule tracking studies reveal three distinct diffusive states for nuclear GR: tight chromatin binding (D < 0.1 μm²/s), condensate residence (D = 0.5–1 μm²/s), and free nucleoplasmic diffusion (D > 3 μm²/s) (fargason2025endocrineexamplesof pages 2-4). Tetrameric GR forms more robust condensates than monomeric or dimeric forms, and different DNA motifs (canonical GRE, nGRE, κBRE) differentially modulate condensate formation (fargason2025endocrineexamplesof pages 8-9, pinheiro2023phaseseparationapossible pages 5-6). While these findings are compelling, GR-LLPS should still be treated as an emergent organizing principle rather than a universally required mechanism at every GR target locus, as comprehensive experimental validation remains incomplete (pinheiro2023phaseseparationapossible pages 3-5, pinheiro2023phaseseparationapossible pages 2-3).

### 7.3 Key Open Questions

1. **Gene-level selectivity:** How does GR achieve locus-specific activation versus repression given that the same receptor binds thousands of genomic sites? The answer likely involves combinatorial logic of DNA motif grammar, pioneer factor context, and condensate organization, but a predictive framework is lacking.
2. **Quantitative contribution of nongenomic signaling:** The relative contribution of rapid kinase-based GR effects versus genomic transcriptional programs to anti-inflammatory efficacy remains poorly quantified in vivo.
3. **FKBP51/52 regulatory pharmacology:** Whether selective modulation of the FKBP51:FKBP52 balance can provide a new therapeutic axis for GR-related pathology is under active investigation but not yet clinically validated.
4. **Phase separation functionality:** Rigorous loss-of-function evidence distinguishing phase separation from simple clustering as a requirement for GR transcriptional output is still needed.
5. **Cross-organism generalizability:** Most mechanistic studies derive from mouse models and human cell lines. Whether the same regulatory logic applies across all vertebrates, and particularly in teleosts with duplicated genomes, remains incompletely characterized (gans2021glucocorticoidmediateddevelopmentalprogramming pages 10-11, gans2021glucocorticoidmediateddevelopmentalprogramming pages 9-10).

## 8. Key References

- Lockett J, Inder W, Clifton V. The Glucocorticoid Receptor: Isoforms, Functions, and Contribution to Glucocorticoid Sensitivity. *Endocrine Reviews*. 2024;45:593–624. doi:10.1210/endrev/bnae008
- Noddings CM, Johnson JL, Agard DA. Cryo-EM reveals how Hsp90 and FKBP immunophilins co-regulate the glucocorticoid receptor. *Nat Struct Mol Biol*. 2023;30:1867–1877. doi:10.1038/s41594-023-01128-y
- Martinez GJ et al. Glucocorticoids, their uses, sexual dimorphisms, and diseases: new concepts, mechanisms, and discoveries. *Physiol Rev*. 2024;104:473–532. doi:10.1152/physrev.00021.2023
- Vettorazzi S et al. A guide to changing paradigms of glucocorticoid receptor function. *FEBS J*. 2022;289:5718–5743. doi:10.1111/febs.16100
- Lesovaya EA et al. The long winding road to the safer glucocorticoid receptor (GR) targeting therapies. *Oncotarget*. 2022;13:408–424. doi:10.18632/oncotarget.28191
- da Silva Pinheiro E et al. Phase-separation: a possible new layer for transcriptional regulation by glucocorticoid receptor. *Front Endocrinol*. 2023;14:1160238. doi:10.3389/fendo.2023.1160238
- Su C et al. Glucocorticoid receptor signaling in the brain and its involvement in cognitive function. *Neural Regen Res*. 2025;20:2520–2537. doi:10.4103/nrr.nrr-d-24-00355
- Grossmann C et al. Structural and molecular determinants of mineralocorticoid receptor signalling. *Br J Pharmacol*. 2022;179:3103–3118. doi:10.1111/bph.15746
- Liu X et al. Disruption of a key ligand-H-bond network drives dissociative properties in vamorolone. *PNAS*. 2020;117:24285–24293. doi:10.1073/pnas.2006890117
- Gans IM, Coffman JA. Glucocorticoid-Mediated Developmental Programming of Vertebrate Stress Responsivity. *Front Physiol*. 2021;12:812195. doi:10.3389/fphys.2021.812195
- Hsu HT et al. Endocrine Examples of Phase Separation in Biology. *Endocrinology*. 2025;166(12). doi:10.1210/endocr/bqaf158

References

1. (su2025glucocorticoidreceptorsignaling pages 2-3): Chonglin Su, Taiqi Huang, Meiyu Zhang, Yanyu Zhang, Yan Zeng, and Xingxing Chen. Glucocorticoid receptor signaling in the brain and its involvement in cognitive function. Neural Regeneration Research, 20:2520-2537, Sep 2025. URL: https://doi.org/10.4103/nrr.nrr-d-24-00355, doi:10.4103/nrr.nrr-d-24-00355. This article has 39 citations and is from a peer-reviewed journal.

2. (noddings2023cryoemrevealshow pages 9-10): Chari M. Noddings, Jill L. Johnson, and David A. Agard. Cryo-em reveals how hsp90 and fkbp immunophilins co-regulate the glucocorticoid receptor. Nature Structural & Molecular Biology, 30:1867-1877, Nov 2023. URL: https://doi.org/10.1038/s41594-023-01128-y, doi:10.1038/s41594-023-01128-y. This article has 84 citations and is from a highest quality peer-reviewed journal.

3. (lockett2024theglucocorticoidreceptor pages 7-8): J. Lockett, W. Inder, and Vicki Clifton. The glucocorticoid receptor: isoforms, functions, and contribution to glucocorticoid sensitivity. Endocrine Reviews, 45:593-624, Mar 2024. URL: https://doi.org/10.1210/endrev/bnae008, doi:10.1210/endrev/bnae008. This article has 125 citations and is from a domain leading peer-reviewed journal.

4. (grossmann2022structuralandmolecular pages 1-2): Claudia Grossmann, Brian Almeida‐Prieto, Alexander Nolze, and Diego Alvarez de la Rosa. Structural and molecular determinants of mineralocorticoid receptor signalling. British Journal of Pharmacology, 179:3103-3118, Dec 2022. URL: https://doi.org/10.1111/bph.15746, doi:10.1111/bph.15746. This article has 61 citations and is from a highest quality peer-reviewed journal.

5. (gans2021glucocorticoidmediateddevelopmentalprogramming pages 10-11): Ian M. Gans and James A. Coffman. Glucocorticoid-mediated developmental programming of vertebrate stress responsivity. Frontiers in Physiology, Dec 2021. URL: https://doi.org/10.3389/fphys.2021.812195, doi:10.3389/fphys.2021.812195. This article has 31 citations.

6. (lockett2024theglucocorticoidreceptor pages 9-10): J. Lockett, W. Inder, and Vicki Clifton. The glucocorticoid receptor: isoforms, functions, and contribution to glucocorticoid sensitivity. Endocrine Reviews, 45:593-624, Mar 2024. URL: https://doi.org/10.1210/endrev/bnae008, doi:10.1210/endrev/bnae008. This article has 125 citations and is from a domain leading peer-reviewed journal.

7. (lockett2024theglucocorticoidreceptor pages 8-9): J. Lockett, W. Inder, and Vicki Clifton. The glucocorticoid receptor: isoforms, functions, and contribution to glucocorticoid sensitivity. Endocrine Reviews, 45:593-624, Mar 2024. URL: https://doi.org/10.1210/endrev/bnae008, doi:10.1210/endrev/bnae008. This article has 125 citations and is from a domain leading peer-reviewed journal.

8. (vettorazzi2022aguideto pages 3-4): Sabine Vettorazzi, Denis Nalbantoglu, J. Christof M. Gebhardt, and Jan Tuckermann. A guide to changing paradigms of glucocorticoid receptor function—a model system for genome regulation and physiology. The FEBS Journal, 289:5718-5743, Jul 2022. URL: https://doi.org/10.1111/febs.16100, doi:10.1111/febs.16100. This article has 72 citations.

9. (noddings2023cryoemrevealshow pages 8-9): Chari M. Noddings, Jill L. Johnson, and David A. Agard. Cryo-em reveals how hsp90 and fkbp immunophilins co-regulate the glucocorticoid receptor. Nature Structural & Molecular Biology, 30:1867-1877, Nov 2023. URL: https://doi.org/10.1038/s41594-023-01128-y, doi:10.1038/s41594-023-01128-y. This article has 84 citations and is from a highest quality peer-reviewed journal.

10. (noddings2023cryoemrevealshow pages 1-2): Chari M. Noddings, Jill L. Johnson, and David A. Agard. Cryo-em reveals how hsp90 and fkbp immunophilins co-regulate the glucocorticoid receptor. Nature Structural & Molecular Biology, 30:1867-1877, Nov 2023. URL: https://doi.org/10.1038/s41594-023-01128-y, doi:10.1038/s41594-023-01128-y. This article has 84 citations and is from a highest quality peer-reviewed journal.

11. (noddings2023cryoemrevealshow pages 6-7): Chari M. Noddings, Jill L. Johnson, and David A. Agard. Cryo-em reveals how hsp90 and fkbp immunophilins co-regulate the glucocorticoid receptor. Nature Structural & Molecular Biology, 30:1867-1877, Nov 2023. URL: https://doi.org/10.1038/s41594-023-01128-y, doi:10.1038/s41594-023-01128-y. This article has 84 citations and is from a highest quality peer-reviewed journal.

12. (noddings2023cryoemrevealshow pages 7-8): Chari M. Noddings, Jill L. Johnson, and David A. Agard. Cryo-em reveals how hsp90 and fkbp immunophilins co-regulate the glucocorticoid receptor. Nature Structural & Molecular Biology, 30:1867-1877, Nov 2023. URL: https://doi.org/10.1038/s41594-023-01128-y, doi:10.1038/s41594-023-01128-y. This article has 84 citations and is from a highest quality peer-reviewed journal.

13. (noddings2023cryoemrevealshow pages 4-5): Chari M. Noddings, Jill L. Johnson, and David A. Agard. Cryo-em reveals how hsp90 and fkbp immunophilins co-regulate the glucocorticoid receptor. Nature Structural & Molecular Biology, 30:1867-1877, Nov 2023. URL: https://doi.org/10.1038/s41594-023-01128-y, doi:10.1038/s41594-023-01128-y. This article has 84 citations and is from a highest quality peer-reviewed journal.

14. (su2025glucocorticoidreceptorsignaling pages 7-8): Chonglin Su, Taiqi Huang, Meiyu Zhang, Yanyu Zhang, Yan Zeng, and Xingxing Chen. Glucocorticoid receptor signaling in the brain and its involvement in cognitive function. Neural Regeneration Research, 20:2520-2537, Sep 2025. URL: https://doi.org/10.4103/nrr.nrr-d-24-00355, doi:10.4103/nrr.nrr-d-24-00355. This article has 39 citations and is from a peer-reviewed journal.

15. (grossmann2022structuralandmolecular pages 6-7): Claudia Grossmann, Brian Almeida‐Prieto, Alexander Nolze, and Diego Alvarez de la Rosa. Structural and molecular determinants of mineralocorticoid receptor signalling. British Journal of Pharmacology, 179:3103-3118, Dec 2022. URL: https://doi.org/10.1111/bph.15746, doi:10.1111/bph.15746. This article has 61 citations and is from a highest quality peer-reviewed journal.

16. (lockett2024theglucocorticoidreceptor pages 15-15): J. Lockett, W. Inder, and Vicki Clifton. The glucocorticoid receptor: isoforms, functions, and contribution to glucocorticoid sensitivity. Endocrine Reviews, 45:593-624, Mar 2024. URL: https://doi.org/10.1210/endrev/bnae008, doi:10.1210/endrev/bnae008. This article has 125 citations and is from a domain leading peer-reviewed journal.

17. (vettorazzi2022aguideto pages 2-3): Sabine Vettorazzi, Denis Nalbantoglu, J. Christof M. Gebhardt, and Jan Tuckermann. A guide to changing paradigms of glucocorticoid receptor function—a model system for genome regulation and physiology. The FEBS Journal, 289:5718-5743, Jul 2022. URL: https://doi.org/10.1111/febs.16100, doi:10.1111/febs.16100. This article has 72 citations.

18. (lockett2024theglucocorticoidreceptor pages 11-12): J. Lockett, W. Inder, and Vicki Clifton. The glucocorticoid receptor: isoforms, functions, and contribution to glucocorticoid sensitivity. Endocrine Reviews, 45:593-624, Mar 2024. URL: https://doi.org/10.1210/endrev/bnae008, doi:10.1210/endrev/bnae008. This article has 125 citations and is from a domain leading peer-reviewed journal.

19. (lockett2024theglucocorticoidreceptor pages 13-13): J. Lockett, W. Inder, and Vicki Clifton. The glucocorticoid receptor: isoforms, functions, and contribution to glucocorticoid sensitivity. Endocrine Reviews, 45:593-624, Mar 2024. URL: https://doi.org/10.1210/endrev/bnae008, doi:10.1210/endrev/bnae008. This article has 125 citations and is from a domain leading peer-reviewed journal.

20. (martinez2024glucocorticoidstheiruses pages 19-20): Genesee J. Martinez, Malik Appleton, Zachary A. Kipp, Analia S. Loria, Booki Min, and Terry D. Hinds. Glucocorticoids, their uses, sexual dimorphisms, and diseases: new concepts, mechanisms, and discoveries. Jan 2024. URL: https://doi.org/10.1152/physrev.00021.2023, doi:10.1152/physrev.00021.2023. This article has 92 citations and is from a highest quality peer-reviewed journal.

21. (mechtidou2022involvementofchromatin pages 28-29): Involvement of chromatin modifying enzymes in the regulation of inflammatory genes by the Glucocorticoid Receptor This article has 0 citations.

22. (lockett2024theglucocorticoidreceptor pages 19-19): J. Lockett, W. Inder, and Vicki Clifton. The glucocorticoid receptor: isoforms, functions, and contribution to glucocorticoid sensitivity. Endocrine Reviews, 45:593-624, Mar 2024. URL: https://doi.org/10.1210/endrev/bnae008, doi:10.1210/endrev/bnae008. This article has 125 citations and is from a domain leading peer-reviewed journal.

23. (vettorazzi2022aguideto pages 6-7): Sabine Vettorazzi, Denis Nalbantoglu, J. Christof M. Gebhardt, and Jan Tuckermann. A guide to changing paradigms of glucocorticoid receptor function—a model system for genome regulation and physiology. The FEBS Journal, 289:5718-5743, Jul 2022. URL: https://doi.org/10.1111/febs.16100, doi:10.1111/febs.16100. This article has 72 citations.

24. (fargason2025endocrineexamplesof pages 8-9): HT Hsu, CC Hsu, SC Tsai, JC Chen, HY Li, and YT Lin. Endocrine examples of phase separation in biology. Endocrinology, Oct 2025. URL: https://doi.org/10.1210/endocr/bqaf158, doi:10.1210/endocr/bqaf158. This article has 1 citations and is from a domain leading peer-reviewed journal.

25. (pinheiro2023phaseseparationapossible pages 3-5): Ester da Silva Pinheiro, André Maciel Preato, Tamirez Villas Boas Petrucci, Lucas Souza dos Santos, and Isaias Glezer. Phase-separation: a possible new layer for transcriptional regulation by glucocorticoid receptor. Frontiers in Endocrinology, Apr 2023. URL: https://doi.org/10.3389/fendo.2023.1160238, doi:10.3389/fendo.2023.1160238. This article has 14 citations.

26. (pinheiro2023phaseseparationapossible pages 5-6): Ester da Silva Pinheiro, André Maciel Preato, Tamirez Villas Boas Petrucci, Lucas Souza dos Santos, and Isaias Glezer. Phase-separation: a possible new layer for transcriptional regulation by glucocorticoid receptor. Frontiers in Endocrinology, Apr 2023. URL: https://doi.org/10.3389/fendo.2023.1160238, doi:10.3389/fendo.2023.1160238. This article has 14 citations.

27. (fargason2025endocrineexamplesof pages 2-4): HT Hsu, CC Hsu, SC Tsai, JC Chen, HY Li, and YT Lin. Endocrine examples of phase separation in biology. Endocrinology, Oct 2025. URL: https://doi.org/10.1210/endocr/bqaf158, doi:10.1210/endocr/bqaf158. This article has 1 citations and is from a domain leading peer-reviewed journal.

28. (mechtidou2022involvementofchromatin pages 22-23): Involvement of chromatin modifying enzymes in the regulation of inflammatory genes by the Glucocorticoid Receptor This article has 0 citations.

29. (borin2023emergingepigeneticand pages 10-11): Cristina Borin, Tim Pieters, Valentina Serafin, and Panagiotis Ntziachristos. Emerging epigenetic and posttranslational mechanisms controlling resistance to glucocorticoids in acute lymphoblastic leukemia. HemaSphere, 7:e916, Jun 2023. URL: https://doi.org/10.1097/hs9.0000000000000916, doi:10.1097/hs9.0000000000000916. This article has 12 citations and is from a peer-reviewed journal.

30. (lockett2024theglucocorticoidreceptor pages 19-20): J. Lockett, W. Inder, and Vicki Clifton. The glucocorticoid receptor: isoforms, functions, and contribution to glucocorticoid sensitivity. Endocrine Reviews, 45:593-624, Mar 2024. URL: https://doi.org/10.1210/endrev/bnae008, doi:10.1210/endrev/bnae008. This article has 125 citations and is from a domain leading peer-reviewed journal.

31. (noddings2023cryoemrevealshow pages 2-3): Chari M. Noddings, Jill L. Johnson, and David A. Agard. Cryo-em reveals how hsp90 and fkbp immunophilins co-regulate the glucocorticoid receptor. Nature Structural & Molecular Biology, 30:1867-1877, Nov 2023. URL: https://doi.org/10.1038/s41594-023-01128-y, doi:10.1038/s41594-023-01128-y. This article has 84 citations and is from a highest quality peer-reviewed journal.

32. (li2025fk506‑bindingproteinsas pages 5-7): Zhi Li, Xiaolei Liu, and Hesong Zeng. Fk506‑binding proteins as emerging bridges linking proteostasis to multi‑system pathogenesis and therapeutic strategies (review). International Journal of Molecular Medicine, 57:1-17, Nov 2025. URL: https://doi.org/10.3892/ijmm.2025.5701, doi:10.3892/ijmm.2025.5701. This article has 1 citations and is from a peer-reviewed journal.

33. (mitreaguilar2022theroleof pages 2-4): Irma B. Mitre-Aguilar, Daniel Moreno-Mitre, Jorge Melendez-Zajgla, Vilma Maldonado, Nadia J. Jacobo-Herrera, Victoria Ramirez-Gonzalez, and Gretel Mendoza-Almanza. The role of glucocorticoids in breast cancer therapy. Current Oncology, 30:298-314, Dec 2022. URL: https://doi.org/10.3390/curroncol30010024, doi:10.3390/curroncol30010024. This article has 48 citations.

34. (grossmann2022structuralandmolecular pages 5-6): Claudia Grossmann, Brian Almeida‐Prieto, Alexander Nolze, and Diego Alvarez de la Rosa. Structural and molecular determinants of mineralocorticoid receptor signalling. British Journal of Pharmacology, 179:3103-3118, Dec 2022. URL: https://doi.org/10.1111/bph.15746, doi:10.1111/bph.15746. This article has 61 citations and is from a highest quality peer-reviewed journal.

35. (martinez2024glucocorticoidstheiruses pages 17-19): Genesee J. Martinez, Malik Appleton, Zachary A. Kipp, Analia S. Loria, Booki Min, and Terry D. Hinds. Glucocorticoids, their uses, sexual dimorphisms, and diseases: new concepts, mechanisms, and discoveries. Jan 2024. URL: https://doi.org/10.1152/physrev.00021.2023, doi:10.1152/physrev.00021.2023. This article has 92 citations and is from a highest quality peer-reviewed journal.

36. (gans2021glucocorticoidmediateddevelopmentalprogramming pages 9-10): Ian M. Gans and James A. Coffman. Glucocorticoid-mediated developmental programming of vertebrate stress responsivity. Frontiers in Physiology, Dec 2021. URL: https://doi.org/10.3389/fphys.2021.812195, doi:10.3389/fphys.2021.812195. This article has 31 citations.

37. (OpenTargets Search: -NR3C1): Open Targets Query (-NR3C1, 5 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

38. (lesovaya2022thelongwinding pages 4-5): Ekaterina A. Lesovaya, Daria Chudakova, Gleb Baida, Ekaterina M. Zhidkova, Kirill I. Kirsanov, Marianna G. Yakubovskaya, and Irina V. Budunova. The long winding road to the safer glucocorticoid receptor (gr) targeting therapies. Oncotarget, 13:408-424, Feb 2022. URL: https://doi.org/10.18632/oncotarget.28191, doi:10.18632/oncotarget.28191. This article has 52 citations.

39. (lesovaya2022thelongwinding pages 3-4): Ekaterina A. Lesovaya, Daria Chudakova, Gleb Baida, Ekaterina M. Zhidkova, Kirill I. Kirsanov, Marianna G. Yakubovskaya, and Irina V. Budunova. The long winding road to the safer glucocorticoid receptor (gr) targeting therapies. Oncotarget, 13:408-424, Feb 2022. URL: https://doi.org/10.18632/oncotarget.28191, doi:10.18632/oncotarget.28191. This article has 52 citations.

40. (lesovaya2022thelongwinding pages 1-2): Ekaterina A. Lesovaya, Daria Chudakova, Gleb Baida, Ekaterina M. Zhidkova, Kirill I. Kirsanov, Marianna G. Yakubovskaya, and Irina V. Budunova. The long winding road to the safer glucocorticoid receptor (gr) targeting therapies. Oncotarget, 13:408-424, Feb 2022. URL: https://doi.org/10.18632/oncotarget.28191, doi:10.18632/oncotarget.28191. This article has 52 citations.

41. (lockett2024theglucocorticoidreceptor pages 20-21): J. Lockett, W. Inder, and Vicki Clifton. The glucocorticoid receptor: isoforms, functions, and contribution to glucocorticoid sensitivity. Endocrine Reviews, 45:593-624, Mar 2024. URL: https://doi.org/10.1210/endrev/bnae008, doi:10.1210/endrev/bnae008. This article has 125 citations and is from a domain leading peer-reviewed journal.

42. (liu2020disruptionofa pages 7-8): Xu Liu, Yashuo Wang, Jennifer S. Gutierrez, Jesse M. Damsker, Kanneboyina Nagaraju, Eric P. Hoffman, and Eric A. Ortlund. Disruption of a key ligand-h-bond network drives dissociative properties in vamorolone for duchenne muscular dystrophy treatment. Proceedings of the National Academy of Sciences, 117:24285-24293, Sep 2020. URL: https://doi.org/10.1073/pnas.2006890117, doi:10.1073/pnas.2006890117. This article has 99 citations and is from a highest quality peer-reviewed journal.

43. (mechtidou2022involvementofchromatin pages 23-24): Involvement of chromatin modifying enzymes in the regulation of inflammatory genes by the Glucocorticoid Receptor This article has 0 citations.

44. (pinheiro2023phaseseparationapossible pages 2-3): Ester da Silva Pinheiro, André Maciel Preato, Tamirez Villas Boas Petrucci, Lucas Souza dos Santos, and Isaias Glezer. Phase-separation: a possible new layer for transcriptional regulation by glucocorticoid receptor. Frontiers in Endocrinology, Apr 2023. URL: https://doi.org/10.3389/fendo.2023.1160238, doi:10.3389/fendo.2023.1160238. This article has 14 citations.

## Artifacts

- [Edison artifact artifact-00](glucocorticoid_receptor_signaling-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](glucocorticoid_receptor_signaling-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. grossmann2022structuralandmolecular pages 1-2
2. gans2021glucocorticoidmediateddevelopmentalprogramming pages 10-11
3. noddings2023cryoemrevealshow pages 4-5
4. noddings2023cryoemrevealshow pages 9-10
5. su2025glucocorticoidreceptorsignaling pages 2-3
6. su2025glucocorticoidreceptorsignaling pages 7-8
7. grossmann2022structuralandmolecular pages 6-7
8. lockett2024theglucocorticoidreceptor pages 7-8
9. vettorazzi2022aguideto pages 6-7
10. lockett2024theglucocorticoidreceptor pages 11-12
11. lockett2024theglucocorticoidreceptor pages 13-13
12. lockett2024theglucocorticoidreceptor pages 15-15
13. mechtidou2022involvementofchromatin pages 22-23
14. lockett2024theglucocorticoidreceptor pages 19-19
15. lockett2024theglucocorticoidreceptor pages 9-10
16. fargason2025endocrineexamplesof pages 8-9
17. lesovaya2022thelongwinding pages 4-5
18. liu2020disruptionofa pages 7-8
19. mechtidou2022involvementofchromatin pages 23-24
20. fargason2025endocrineexamplesof pages 2-4
21. lockett2024theglucocorticoidreceptor pages 8-9
22. vettorazzi2022aguideto pages 3-4
23. noddings2023cryoemrevealshow pages 8-9
24. noddings2023cryoemrevealshow pages 1-2
25. noddings2023cryoemrevealshow pages 6-7
26. noddings2023cryoemrevealshow pages 7-8
27. vettorazzi2022aguideto pages 2-3
28. martinez2024glucocorticoidstheiruses pages 19-20
29. mechtidou2022involvementofchromatin pages 28-29
30. pinheiro2023phaseseparationapossible pages 3-5
31. pinheiro2023phaseseparationapossible pages 5-6
32. borin2023emergingepigeneticand pages 10-11
33. lockett2024theglucocorticoidreceptor pages 19-20
34. noddings2023cryoemrevealshow pages 2-3
35. mitreaguilar2022theroleof pages 2-4
36. grossmann2022structuralandmolecular pages 5-6
37. martinez2024glucocorticoidstheiruses pages 17-19
38. gans2021glucocorticoidmediateddevelopmentalprogramming pages 9-10
39. lesovaya2022thelongwinding pages 3-4
40. lesovaya2022thelongwinding pages 1-2
41. lockett2024theglucocorticoidreceptor pages 20-21
42. pinheiro2023phaseseparationapossible pages 2-3
43. https://doi.org/10.4103/nrr.nrr-d-24-00355,
44. https://doi.org/10.1038/s41594-023-01128-y,
45. https://doi.org/10.1210/endrev/bnae008,
46. https://doi.org/10.1111/bph.15746,
47. https://doi.org/10.3389/fphys.2021.812195,
48. https://doi.org/10.1111/febs.16100,
49. https://doi.org/10.1152/physrev.00021.2023,
50. https://doi.org/10.1210/endocr/bqaf158,
51. https://doi.org/10.3389/fendo.2023.1160238,
52. https://doi.org/10.1097/hs9.0000000000000916,
53. https://doi.org/10.3892/ijmm.2025.5701,
54. https://doi.org/10.3390/curroncol30010024,
55. https://doi.org/10.18632/oncotarget.28191,
56. https://doi.org/10.1073/pnas.2006890117,