---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-28T17:27:55.848241'
end_time: '2026-06-28T17:52:53.934282'
duration_seconds: 1498.09
template_file: templates/module_research.md.j2
template_variables:
  module_title: TNF-mediated signaling pathway module
  module_summary: TNF binding to TNF receptor complexes nucleates TRADD, RIPK, and
    TRAF signaling assemblies that balance NF-kappaB activation, inflammatory gene
    expression, survival, and death decisions.
  module_outline: "- TNF-mediated signaling pathway\n  - 1. tnf receptor ligation\n\
    \  - TNF engages TNFR1\n    - TNF ligand (molecular player: TNF)\n    - TNFR1\
    \ receptor (molecular player: TNFR1 receptor family/ortholog group)\n  - 2. tnfr\
    \ adaptor complex\n  - TNFR adaptor complex assembly\n    - TRADD adaptor (molecular\
    \ player: TRADD)\n    - RIPK1 kinase/scaffold (molecular player: RIPK1 kinase/scaffold\
    \ family/ortholog group)\n    - TRAF2 adaptor (molecular player: TRAF2 adaptor\
    \ family/ortholog group)\n  - 3. tnf inflammatory output\n  - NF-kappaB and inflammatory\
    \ output\n    - TRAF2 signal relay (molecular player: TRAF2 signal relay family/ortholog\
    \ group)\n    - TNFR1 pathway context (molecular player: TNFR1 pathway context\
    \ family/ortholog group)"
  module_connections: '- TNF engages TNFR1 causes TNFR adaptor complex assembly: The
    initiating event promotes tnfr adaptor complex.

    - TNFR adaptor complex assembly causes NF-kappaB and inflammatory output: TNFR
    adaptor complex assembly leads to tnf inflammatory output.'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 41
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: tnf_signaling-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: tnf_signaling-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
---

## Question

# Commissioned Review Brief

## Review Topic

TNF-mediated signaling pathway module

## Working Scope

TNF binding to TNF receptor complexes nucleates TRADD, RIPK, and TRAF signaling assemblies that balance NF-kappaB activation, inflammatory gene expression, survival, and death decisions.

## Provisional Biological Outline

- TNF-mediated signaling pathway
  - 1. tnf receptor ligation
  - TNF engages TNFR1
    - TNF ligand (molecular player: TNF)
    - TNFR1 receptor (molecular player: TNFR1 receptor family/ortholog group)
  - 2. tnfr adaptor complex
  - TNFR adaptor complex assembly
    - TRADD adaptor (molecular player: TRADD)
    - RIPK1 kinase/scaffold (molecular player: RIPK1 kinase/scaffold family/ortholog group)
    - TRAF2 adaptor (molecular player: TRAF2 adaptor family/ortholog group)
  - 3. tnf inflammatory output
  - NF-kappaB and inflammatory output
    - TRAF2 signal relay (molecular player: TRAF2 signal relay family/ortholog group)
    - TNFR1 pathway context (molecular player: TNFR1 pathway context family/ortholog group)

## Known Relationships Among Steps

- TNF engages TNFR1 causes TNFR adaptor complex assembly: The initiating event promotes tnfr adaptor complex.
- TNFR adaptor complex assembly causes NF-kappaB and inflammatory output: TNFR adaptor complex assembly leads to tnf inflammatory output.

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

TNF-mediated signaling pathway module

## Working Scope

TNF binding to TNF receptor complexes nucleates TRADD, RIPK, and TRAF signaling assemblies that balance NF-kappaB activation, inflammatory gene expression, survival, and death decisions.

## Provisional Biological Outline

- TNF-mediated signaling pathway
  - 1. tnf receptor ligation
  - TNF engages TNFR1
    - TNF ligand (molecular player: TNF)
    - TNFR1 receptor (molecular player: TNFR1 receptor family/ortholog group)
  - 2. tnfr adaptor complex
  - TNFR adaptor complex assembly
    - TRADD adaptor (molecular player: TRADD)
    - RIPK1 kinase/scaffold (molecular player: RIPK1 kinase/scaffold family/ortholog group)
    - TRAF2 adaptor (molecular player: TRAF2 adaptor family/ortholog group)
  - 3. tnf inflammatory output
  - NF-kappaB and inflammatory output
    - TRAF2 signal relay (molecular player: TRAF2 signal relay family/ortholog group)
    - TNFR1 pathway context (molecular player: TNFR1 pathway context family/ortholog group)

## Known Relationships Among Steps

- TNF engages TNFR1 causes TNFR adaptor complex assembly: The initiating event promotes tnfr adaptor complex.
- TNFR adaptor complex assembly causes NF-kappaB and inflammatory output: TNFR adaptor complex assembly leads to tnf inflammatory output.

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

# TNF-Mediated Signaling Pathway Module: A Mechanistic Review

## 1. Executive Summary

Tumor necrosis factor (TNF) signaling through TNF receptor 1 (TNFR1) constitutes one of the most intensively studied cytokine signaling systems in mammalian biology. Upon TNF binding to TNFR1, a membrane-proximal signaling complex (Complex I) assembles within seconds, nucleated by the adaptors TRADD and RIPK1, which recruit the scaffold/E3 ligase module TRAF2–cIAP1/2 and the linear ubiquitin assembly complex LUBAC (loo2023deathbytnf pages 2-3). The resulting ubiquitin scaffold activates the canonical NF-κB and MAPK pathways, driving inflammatory gene expression and cell survival (li2025exploringtnfr1from pages 4-6, so2022theimmunologicalsignificance pages 2-3). However, the same pathway harbors latent death-inducing potential: when specific ubiquitin or phosphorylation checkpoints fail, Complex I components dissociate and form cytosolic death-inducing assemblies (Complex IIa and IIb) that drive apoptosis, necroptosis, or pyroptosis (loo2023deathbytnf pages 3-5, loo2023deathbytnf pages 5-6). This review synthesizes current mechanistic understanding of the TNF–TNFR1 signaling module, covering its molecular architecture, regulatory checkpoints, evolutionary origins, cell-type variation, and major unresolved questions.

---

## 2. Definition and Biological Boundaries

### 2.1 What Is Included

The TNF–TNFR1 signaling module encompasses the events from extracellular TNF ligand engagement of the TNFR1 death receptor through the assembly of receptor-proximal Complex I (TRADD, RIPK1, TRAF2/5, cIAP1/2, LUBAC), activation of the canonical NF-κB and MAPK cascades, and the conditional formation of cytosolic death complexes (Complex IIa, IIb, necrosome) (loo2023deathbytnf pages 2-3, loo2023deathbytnf pages 3-5). The system's outputs span inflammatory gene expression, pro-survival programs, apoptosis, necroptosis, and in some contexts pyroptosis (loo2023deathbytnf pages 3-5, smulski2024editorialreviewsand pages 1-2).

### 2.2 What Should Be Treated Separately

Several neighboring processes are often conflated with but are mechanistically distinct from the core TNFR1 pathway:

- **TNFR2 signaling**: TNFR2 lacks a death domain and signals primarily through TRAF2 and TRAF1 to activate the alternative NF-κB pathway and promote T regulatory cell functions. TNFR2 preferentially responds to membrane-bound TNF and modulates TNFR1 cytotoxicity by depleting cytosolic TRAF2/cIAP pools (siegmund2022tnfreceptorassociated pages 7-9, loo2023deathbytnf pages 7-8, smulski2024editorialreviewsand pages 1-2).
- **Other death receptor pathways**: CD95/Fas and TRAIL receptors (DR4/DR5) form plasma membrane-associated death-inducing signaling complexes (DISCs) that directly activate caspase-8 at the receptor, whereas TNFR1 empowers TRADD and RIPK1 to trigger cell death via cytosolic complexes after receptor dissociation (siegmund2023fn14andtnfr2 pages 4-5).
- **Non-canonical NF-κB signaling**: Although TRAF2 inhibits the alternative (non-canonical) NF-κB pathway by promoting NIK degradation, this pathway is primarily regulated through TRAF3–cIAP–NIK dynamics and is engaged by distinct TNFRSF receptors such as BAFFR, CD40, and LTβR (siegmund2022tnfreceptorassociated pages 7-9).
- **TLR/IL-1R–NF-κB signaling**: While converging on IKK/NF-κB activation, these pathways use MyD88/IRAK rather than TRADD/RIPK1 adaptors.

---

## 3. Mechanistic Overview

### 3.1 Step 1: TNF–TNFR1 Ligation

TNF exists as a homotrimeric type II transmembrane protein (tmTNF) that can be proteolytically shed to generate soluble TNF (sTNF). Both forms bind the extracellular cysteine-rich domains (CRDs) of TNFR1, inducing receptor trimerization and release of the silencer of death domains (SODD) from the intracellular death domain (manohar2024atthecrossroads pages 2-4). Membrane-bound TNF forms high-affinity multivalent interactions with TNFR1 and generates stronger, more sustained signals than sTNF, which promotes only transient receptor engagement (rafeeq2025targetingtnfr1drivennecroptosis pages 4-6). This ligand-form distinction has important implications for in vitro versus in vivo signaling outcomes (loo2023deathbytnf pages 7-8).

### 3.2 Step 2: Complex I Assembly

Complex I assembly is an obligatory step that occurs within seconds of receptor ligation (loo2023deathbytnf pages 2-3). The sequence proceeds as follows:

1. **TRADD and RIPK1 recruitment**: TRADD binds the cytoplasmic death domain of TNFR1 via its own C-terminal DD. RIPK1 is co-recruited through DD–DD interactions with both TNFR1 and TRADD. TRADD undergoes a conformational transition to an open state, serving as a scaffold for downstream factor recruitment (li2025exploringtnfr1from pages 4-6, wang2025thedualrole pages 2-4).

2. **TRAF2/5 and cIAP1/2 recruitment**: TRADD recruits TRAF2 homotrimers (or TRAF1–TRAF2 heterotrimers) through its N-terminal region. TRAF2 in turn brings cIAP1 and cIAP2 to the complex via its coiled-coil domain (so2022theimmunologicalsignificance pages 2-3).

3. **K63-linked ubiquitination**: cIAP1/2 rapidly polyubiquitinate RIPK1 with K63-linked chains, notably at lysine 377 (K376 in mice). This creates docking sites for the TAB2/TAB3 adaptor proteins and the LUBAC complex (li2025exploringtnfr1from pages 4-6, xiao2025theroleof pages 9-12).

4. **LUBAC recruitment and linear ubiquitination**: LUBAC (composed of HOIP, HOIL-1L, and SHARPIN) adds M1-linked (linear) ubiquitin chains to RIPK1 and other Complex I components. These linear chains are specifically recognized by NEMO, the regulatory subunit of the IKK complex (loo2023deathbytnf pages 2-3, xiao2025theroleof pages 9-12, li2025exploringtnfr1from pages 4-6).

5. **TAK1 and IKK complex recruitment**: K63-linked ubiquitin chains recruit the TAK1–TAB2/TAB3 complex, while M1-linked chains recruit the IKK complex (IKKα, IKKβ, NEMO) along with TBK1 and IKKε (so2022theimmunologicalsignificance pages 4-5, loo2023deathbytnf pages 2-3).

### 3.3 Step 3: NF-κB and MAPK Activation

TAK1 phosphorylates IKKβ at activation loop residues S177/S181, activating the IKK complex. Activated IKKβ then phosphorylates IκBα, marking it for K48-linked ubiquitination and proteasomal degradation (li2025exploringtnfr1from pages 4-6, so2022theimmunologicalsignificance pages 4-5). This liberates the NF-κB p65/p50 dimer, which translocates to the nucleus and activates transcription of hundreds of target genes, including pro-inflammatory cytokines (TNF, IL-6, IL-8), anti-apoptotic factors (FLIP, cIAP1/2, A20, TRAF1), and immunoregulatory molecules (so2022theimmunologicalsignificance pages 4-5, preedy2024cellularheterogeneityin pages 2-3). Simultaneously, TAK1 activates MAPK cascades (JNK, p38, ERK), leading to AP-1 transcription factor activation (so2022theimmunologicalsignificance pages 4-5, loo2023deathbytnf pages 2-3).

### 3.4 Step 4: Cell Death Checkpoint Control and Complex II Formation

The transition from survival signaling to cell death is governed by three hierarchically arranged checkpoints (loo2023deathbytnf pages 3-5, loo2023deathbytnf pages 5-6):

**Checkpoint 1 (IKK checkpoint)**: At the receptor level, IKKα/IKKβ and TBK1/IKKε phosphorylate RIPK1 within Complex I, directly inhibiting its kinase activity and preventing Complex IIb assembly (loo2023deathbytnf pages 3-5, loo2023deathbytnf pages 5-6).

**Checkpoint 2 (NF-κB checkpoint)**: The NF-κB transcriptional program induces FLIP expression. FLIP heterodimerizes with procaspase-8 and modulates its activity, preventing full caspase-8 activation and protecting cells from Complex IIa-mediated apoptosis (preedy2024cellularheterogeneityin pages 3-4, loo2023deathbytnf pages 5-6).

**Checkpoint 3 (Caspase-8 checkpoint)**: Active caspase-8 cleaves RIPK1 and RIPK3, preventing necrosome assembly. This checkpoint is the final barrier against necroptosis (loo2023deathbytnf pages 5-6, siegmund2023fn14andtnfr2 pages 4-5).

When these checkpoints fail, dissociated TRADD and/or RIPK1 associate with FADD and procaspase-8 in the cytosol to form **Complex IIa** (TRADD-dependent, RIPK1 kinase-independent apoptosis) or **Complex IIb** (RIPK1 kinase-dependent apoptosis) (loo2023deathbytnf pages 3-5, siegmund2023fn14andtnfr2 pages 4-5). If caspase-8 is additionally compromised, RIPK1 engages RIPK3 through RHIM domain interactions, and RIPK3 phosphorylates MLKL, which oligomerizes and translocates to the plasma membrane to execute necroptosis (rafeeq2025targetingtnfr1drivennecroptosis pages 4-6, siegmund2023fn14andtnfr2 pages 4-5).

---

## 4. Major Molecular Players and Active Assemblies

The following table provides a comprehensive summary of the principal proteins and complexes organizing TNF–TNFR1 signaling:

| Molecule | Type/Function | Domain(s) | Role in Complex I | Role in Complex II/Death | Key Regulatory Modifications |
|---|---|---|---|---|---|
| TNF | Trimeric TNFSF cytokine ligand | TNF homology domain; transmembrane precursor for tmTNF and cleaved sTNF | Initiates TNFR1 trimerization and membrane-proximal signaling complex assembly | Sustained or poorly checkpointed signaling can drive downstream apoptotic/necroptotic outputs; tmTNF generally gives stronger receptor engagement than sTNF | Proteolytic shedding to soluble TNF; ligand valency/form affects receptor residency and signaling strength (manohar2024atthecrossroads pages 2-4, rafeeq2025targetingtnfr1drivennecroptosis pages 4-6, loo2023deathbytnf pages 7-8, smulski2024editorialreviewsand pages 1-2) |
| TNFR1 | Death receptor; primary TNF receptor for canonical inflammatory and death signaling | Extracellular cysteine-rich domains; transmembrane helix; intracellular death domain (DD) | Binds TNF and recruits TRADD and RIPK1 through DD interactions to nucleate Complex I | Source platform for release of TRADD/RIPK1 into cytosolic Complex II assemblies; can ultimately support apoptosis, pyroptosis, or necroptosis when checkpoints fail | Receptor trimerization/cluster formation; occupancy differs with soluble versus membrane TNF (li2025exploringtnfr1from pages 4-6, preedy2024cellularheterogeneityin pages 2-3, loo2023deathbytnf pages 2-3, loo2023deathbytnf pages 3-5) |
| TRADD | Adaptor/scaffold | C-terminal DD; N-terminal region for partner recruitment | Early adaptor recruited to TNFR1; scaffolds TRAF2/5, RIPK1, and downstream signaling factors | Participates in Complex IIa with FADD/caspase-8; receptor-dissociated TRADD can seed cytosolic death complexes | Conformational opening reported during activation; scaffold function regulated by interaction state rather than intrinsic catalysis (li2025exploringtnfr1from pages 4-6, wang2025thedualrole pages 2-4, siegmund2023fn14andtnfr2 pages 4-5) |
| RIPK1 | Kinase/scaffold controlling survival-death decisions | N-terminal kinase domain; intermediate RHIM-containing region; C-terminal DD | Recruited to TNFR1; major ubiquitin scaffold in Complex I; helps recruit TAK1/IKK/LUBAC-dependent signaling | Central component of Complex IIb and necrosome initiation; kinase activity promotes apoptosis/necroptosis when inhibitory checkpoints fail | K63 ubiquitination by cIAP1/2; M1-linked ubiquitination via LUBAC on Complex I components; inhibitory phosphorylation by IKKα/β, TBK1, IKKε, TAK1/MK2; activating autophosphorylation including S166 (li2025exploringtnfr1from pages 4-6, wagner2025traf2andripk1 pages 1-2, loo2023deathbytnf pages 3-5, preedy2024cellularheterogeneityin pages 3-4, loo2023deathbytnf pages 5-6) |
| TRAF2 | Adaptor/E3-associated scaffold linking TNFR1 to cIAPs and NF-κB/MAPK | N-terminal RING; 5 zinc fingers; coiled-coil TRAF-N; C-terminal TRAF-C | Recruited via TRADD; brings cIAP1/2 to Complex I; promotes RIPK1 ubiquitination and downstream TAK1/IKK recruitment | Limits cytotoxic TNFR1 signaling by sustaining ubiquitin scaffolds; loss can sensitize to apoptosis/necroptosis in some contexts | RING-dependent ubiquitin ligase/scaffold activity; can be ubiquitinated itself; functional redundancy with RIPK1 in some cell lines; regulates canonical positively and alternative NF-κB negatively in many contexts (albini2025inflammationandcancer pages 2-3, siegmund2022tnfreceptorassociated pages 5-7, siegmund2022tnfreceptorassociated pages 1-2, siegmund2022tnfreceptorassociated pages 7-9, so2022theimmunologicalsignificance pages 2-3, wagner2025traf2andripk1 pages 5-8, wagner2025traf2andripk1 pages 4-5) |
| cIAP1/2 | RING E3 ubiquitin ligases; key TNFR1 checkpoint factors | BIR domains; UBA; CARD; C-terminal RING | Recruited by TRAF2; install K63-linked ubiquitin chains on RIPK1 and other Complex I proteins, enabling LUBAC/TAK1/IKK recruitment | Their loss or catalytic impairment destabilizes Complex I and licenses RIPK1-dependent apoptosis/necroptosis and inflammation | Auto-ubiquitination; ubiquitination of RIPK1; pharmacologic depletion by Smac mimetics; catalytic inactivity causes TNFR1-driven pathology in vivo (wagner2025traf2andripk1 pages 1-2, albini2025inflammationandcancer pages 2-3, siegmund2022tnfreceptorassociated pages 2-4, loo2023deathbytnf pages 3-5, xiao2025theroleof pages 9-12, li2025exploringtnfr1from pages 4-6) |
| LUBAC (HOIP/HOIL-1L/SHARPIN) | Linear ubiquitin assembly complex | HOIP catalytic RBR ligase; HOIL-1L and SHARPIN accessory subunits | Adds M1-linked ubiquitin to Complex I components including RIPK1/TNFR1-associated substrates; stabilizes receptor complex and recruits NEMO-containing IKK modules | Suppresses transition to death signaling by reinforcing receptor-proximal checkpoints; LUBAC deficiency predisposes to RIPK1-driven death and autoinflammation | M1-linked linear ubiquitination; function opposed/edited by OTULIN, CYLD, and contextually A20; PP6 can restrain linear ubiquitination (so2022theimmunologicalsignificance pages 2-3, loo2023deathbytnf pages 2-3, loo2023deathbytnf pages 3-5, xiao2025theroleof pages 9-12, loo2023deathbytnf pages 9-11, li2025exploringtnfr1from pages 4-6) |
| TAK1 | MAP3K activating IKK and MAPK pathways | Ser/Thr kinase (TAB-binding complex with TAB2/3) | Recruited to K63-ubiquitin scaffolds via TAB2/3; activates IKKβ and MAPK outputs | Loss of TAK1 activity weakens the receptor-level checkpoint and can permit RIPK1-dependent death | Activating phosphorylation; recruitment depends on ubiquitin scaffolds (li2025exploringtnfr1from pages 4-6, so2022theimmunologicalsignificance pages 4-5, preedy2024cellularheterogeneityin pages 2-3, wang2025thedualrole pages 2-4) |
| IKK complex (IKKα/IKKβ/NEMO) | Core canonical NF-κB kinase complex | IKKα and IKKβ kinases; NEMO ubiquitin-binding regulatory subunit | NEMO binds M1/K63 ubiquitin scaffolds; TAK1 activates IKKβ, leading to IκBα phosphorylation and canonical NF-κB activation | IKKs also impose a death checkpoint by inhibitory phosphorylation of RIPK1, limiting Complex IIb formation | IKKβ phosphorylation at activation loop residues; NEMO docking on linear ubiquitin chains; direct/indirect inhibitory phosphorylation of RIPK1 (li2025exploringtnfr1from pages 4-6, so2022theimmunologicalsignificance pages 4-5, loo2023deathbytnf pages 2-3, loo2023deathbytnf pages 3-5, loo2023deathbytnf pages 5-6) |
| NF-κB (p65/RelA-p50) | Canonical transcription factor dimer | Rel homology domains; p65 transactivation domain | Activated downstream of IKK-mediated IκBα degradation; drives inflammatory and pro-survival gene programs including FLIP, A20, cIAPs, TRAF1 | Failure of this transcriptional checkpoint lowers prosurvival proteins and permits Complex II-mediated apoptosis | Nuclear translocation after IκBα degradation; oscillatory/single-pulse dynamics vary between cells (li2025exploringtnfr1from pages 4-6, so2022theimmunologicalsignificance pages 4-5, preedy2024cellularheterogeneityin pages 2-3, preedy2024cellularheterogeneityin pages 3-4) |
| IκBα | NF-κB inhibitor | Ankyrin-repeat inhibitor protein | Binds NF-κB in resting cells; phosphorylated by activated IKK then degraded to release NF-κB | Not a core Complex II component, but failure to degrade it blocks the pro-survival NF-κB checkpoint and biases toward death | Phosphorylation by IKK; ubiquitin-mediated proteasomal degradation (li2025exploringtnfr1from pages 4-6, so2022theimmunologicalsignificance pages 4-5, preedy2024cellularheterogeneityin pages 2-3) |
| FADD | Death-domain adaptor for caspase-8 recruitment | C-terminal DD; N-terminal DED | Not a stable core member of TNFR1 Complex I in the prevailing model | Central adaptor in Complex IIa/IIb; links TRADD and/or RIPK1 to procaspase-8 | Assembly-dependent oligomerization; mechanistic dual role in promoting yet constraining caspase-8 remains incompletely resolved (loo2023deathbytnf pages 3-5, loo2023deathbytnf pages 5-6, siegmund2023fn14andtnfr2 pages 4-5, loo2023deathbytnf pages 7-8) |
| Caspase-8 | Initiator caspase and checkpoint enzyme | Tandem DEDs; catalytic caspase domain | Not a principal Complex I effector; indirectly protected by NF-κB-dependent FLIP expression and receptor-proximal checkpoints | Activated in Complex II to drive apoptosis; when active, also suppresses necroptosis by cleaving RIPK pathway components | Proximity-induced dimerization/cleavage; cleavage of RIPK1/RIPK3 limits necroptosis; can contribute to pyroptotic outputs in some contexts (loo2023deathbytnf pages 3-5, loo2023deathbytnf pages 5-6, siegmund2023fn14andtnfr2 pages 4-5, li2025exploringtnfr1from pages 4-6) |
| FLIP (c-FLIP) | Caspase-8 regulator; pro-survival checkpoint factor | Tandem DEDs; long isoform has caspase-like pseudoenzyme domain | Induced by NF-κB downstream of Complex I | Modulates caspase-8 activity in Complex II; abundance/isoform balance influences apoptosis versus necroptosis | Transcriptional induction by NF-κB; stoichiometric heterodimerization with caspase-8 (loo2023deathbytnf pages 3-5, preedy2024cellularheterogeneityin pages 3-4, rafeeq2025targetingtnfr1drivennecroptosis pages 4-6) |
| RIPK3 | Necroptosis kinase | Kinase domain; RHIM | Not a main Complex I component | Recruited downstream of activated RIPK1 into necrosome; phosphorylates MLKL to execute necroptosis when caspase-8 checkpoint is lost | Phosphorylation; RHIM-mediated assembly; can be cleaved/inhibited by caspase-8 activity (preedy2024cellularheterogeneityin pages 3-4, siegmund2023fn14andtnfr2 pages 4-5, manohar2024atthecrossroads pages 7-8, li2025exploringtnfr1from pages 4-6) |
| MLKL | Terminal necroptosis executioner | Pseudokinase domain; N-terminal membrane-disrupting region | No established role in Complex I | Phosphorylated by RIPK3, oligomerizes, translocates to membranes, and disrupts integrity to cause lytic death | RIPK3-dependent phosphorylation and oligomerization (rafeeq2025targetingtnfr1drivennecroptosis pages 4-6, siegmund2023fn14andtnfr2 pages 4-5) |
| A20 (TNFAIP3) | Ubiquitin-editing/checkpoint regulator; anti-inflammatory protein | OTU DUB domain; C-terminal zinc fingers/ubiquitin-binding motifs | Restrains and stabilizes Complex I signaling in a context-dependent manner; protects M1-ubiquitin architecture and suppresses pathological RIPK1 activation | Prevents RIPK1 kinase-dependent and -independent death; deficiency promotes TNF-driven cytotoxicity and autoinflammation | Deubiquitinase and ubiquitin-binding/editing functions; prominent NF-κB target gene; protects against TNF-induced apoptosis beyond simple NF-κB suppression (loo2023deathbytnf pages 3-5, xiao2025theroleof pages 33-34, loo2023deathbytnf pages 9-11) |
| CYLD | Deubiquitinase favoring death pathway access when unchecked | USP-family DUB with CAP-Gly domains | Removes K63/M1-linked ubiquitin from Complex I components, counteracting scaffold stability | Promotes Complex I destabilization and can facilitate RIPK1-dependent apoptosis/necroptosis when dominant or insufficiently restrained | Deubiquitination of RIPK1-associated chains; recruited to TNFR1 signaling machinery (loo2023deathbytnf pages 3-5, xiao2025theroleof pages 9-12, xiao2025theroleof pages 33-34, so2022theimmunologicalsignificance pages 2-3) |
| OTULIN | Met1-specific deubiquitinase controlling linear ubiquitin homeostasis | OTU DUB selective for M1-linked chains | Edits LUBAC-generated linear ubiquitin, preventing aberrant Complex I ubiquitin accumulation while preserving homeostasis | Loss perturbs checkpoints and causes TNF/RIPK1-driven inflammatory cell death syndromes | M1-specific deubiquitination; functional coupling to LUBAC (loo2023deathbytnf pages 3-5, loo2023deathbytnf pages 9-11) |
| TBK1/IKKε | Noncanonical IKK-family kinases acting in receptor-proximal checkpoint control | Ser/Thr kinase domains | Recruited via NEMO/ubiquitin-rich Complex I; help enforce receptor-level checkpoint alongside canonical IKKs | Inhibit RIPK1 activation and Complex IIb assembly; loss sensitizes to RIPK1-dependent death | Inhibitory phosphorylation of RIPK1; activation depends on ubiquitin scaffold assembly (loo2023deathbytnf pages 2-3, loo2023deathbytnf pages 3-5, loo2023deathbytnf pages 5-6, li2025exploringtnfr1from pages 4-6) |


*Table: This table summarizes the principal proteins and complexes that organize TNF-TNFR1 signaling, from receptor-proximal Complex I assembly to Complex II-mediated cell death. It highlights each factor’s structural features, signaling role, and the post-translational modifications that bias the pathway toward NF-κB activation, survival, apoptosis, or necroptosis.*

The cell death checkpoints that govern the survival-death decision are summarized below:

| Checkpoint Name | Location/Level | Key Molecules | Normal Function | Consequence of Disruption | Type of Cell Death Triggered |
|---|---|---|---|---|---|
| IKK checkpoint | Receptor-proximal Complex I; membrane-associated TNFR1 signalosome | IKKα, IKKβ, TBK1, IKKε, NEMO, RIPK1, LUBAC-dependent ubiquitin scaffold | Phosphorylates and inhibits RIPK1 kinase activity at the receptor complex, preventing Complex IIb assembly and maintaining inflammatory/survival signaling downstream of TNFR1 (loo2023deathbytnf pages 3-5, loo2023deathbytnf pages 5-6) | Loss of receptor-level inhibitory phosphorylation permits RIPK1 enzymatic activation, destabilizes the survival bias of Complex I, and promotes formation of cytosolic death complexes (loo2023deathbytnf pages 3-5, loo2023deathbytnf pages 5-6, preedy2024cellularheterogeneityin pages 3-4) | Primarily RIPK1-dependent apoptosis; can also permit pyroptotic outputs in some contexts and facilitate progression toward necroptotic signaling if additional checkpoints fail (loo2023deathbytnf pages 3-5, loo2023deathbytnf pages 5-6) |
| NF-κB checkpoint | Nuclear/transcriptional level downstream of Complex I | NF-κB (p65/p50), IκBα, FLIP/c-FLIP, prosurvival gene products | Induces a delayed prosurvival transcriptional program, especially FLIP and related anti-death factors, that suppresses caspase-8-mediated apoptosis after TNF sensing (loo2023deathbytnf pages 3-5, preedy2024cellularheterogeneityin pages 3-4, loo2023deathbytnf pages 5-6) | Failure of NF-κB activation leaves FLIP and other survival proteins insufficient, allowing TNF signaling to switch from survival/inflammation to cytosolic death-complex formation even when receptor-proximal signaling has occurred (preedy2024cellularheterogeneityin pages 3-4, loo2023deathbytnf pages 5-6) | RIPK1 kinase-independent apoptosis, classically associated with Complex IIa-like signaling (loo2023deathbytnf pages 5-6) |
| Caspase-8 checkpoint | Cytosolic Complex II level | Caspase-8, FADD, RIPK1, RIPK3, FLIP | Active caspase-8 promotes apoptotic processing when appropriate but also restrains necroptosis by cleaving RIPK1/RIPK3 and preventing stable necrosome formation (loo2023deathbytnf pages 5-6, siegmund2023fn14andtnfr2 pages 4-5, li2025exploringtnfr1from pages 4-6) | Inhibition or loss of caspase-8 disables this brake on RIPK1/RIPK3, allowing Complex IIb/ripoptosome maturation into necrosome and unleashing lytic death signaling (loo2023deathbytnf pages 5-6, siegmund2023fn14andtnfr2 pages 4-5, xiao2025theroleof pages 5-5) | Necroptosis, mediated by RIPK1-RIPK3-MLKL signaling (loo2023deathbytnf pages 5-6, siegmund2023fn14andtnfr2 pages 4-5, xiao2025theroleof pages 5-5) |


*Table: This table summarizes the three major checkpoints that keep TNF-TNFR1 signaling biased toward survival or controlled apoptosis rather than runaway inflammatory cell death. It is useful for distinguishing where in the pathway each checkpoint acts and what form of death emerges when that checkpoint fails.*

### 4.1 The Ubiquitin Code as a Signaling Language

The ubiquitin modifications within Complex I function as a sophisticated signaling language. K63-linked chains installed by cIAP1/2 serve as recruitment platforms for TAB2/TAB3 and subsequently TAK1, while M1-linked linear chains generated by LUBAC recruit NEMO and the IKK complex (so2022theimmunologicalsignificance pages 2-3, loo2023deathbytnf pages 2-3). This dual ubiquitin code is counterbalanced by deubiquitinases: CYLD removes K63- and M1-linked chains to destabilize the complex; OTULIN specifically edits M1-linked chains; and A20 stabilizes M1-linked ubiquitin architectures while preventing pathological RIPK1 activation (loo2023deathbytnf pages 3-5, xiao2025theroleof pages 9-12, xiao2025theroleof pages 33-34, loo2023deathbytnf pages 9-11). Deficiency in any of these regulators produces distinct inflammatory pathologies, underscoring the precision required in ubiquitin chain editing (loo2023deathbytnf pages 9-11).

### 4.2 TRAF2: Scaffold and E3 Ligase

TRAF2 is a 56 kDa trimeric adaptor protein with an N-terminal RING domain (E3 ligase activity), five zinc finger motifs, a coiled-coil TRAF-N domain, and a C-terminal TRAF-C domain mediating receptor interactions (albini2025inflammationandcancer pages 2-3, siegmund2022tnfreceptorassociated pages 1-2). It functions primarily as a scaffold, bringing cIAP1/2 E3 ligases together with their substrates (siegmund2022tnfreceptorassociated pages 2-4). TRAF2 can form homotrimers or TRAF1(TRAF2)₂ heterotrimers; the latter more efficiently recruit cIAP2 (so2022theimmunologicalsignificance pages 3-4). Beyond its scaffolding role, TRAF2 inhibits the alternative NF-κB pathway by cooperating with TRAF3 and cIAPs to maintain constitutive NIK degradation (siegmund2022tnfreceptorassociated pages 7-9). This creates an elegant regulatory circuit: ligand-induced recruitment of TRAF2/cIAPs to plasma membrane receptors depletes these molecules from the cytosol, simultaneously activating canonical and de-repressing alternative NF-κB signaling (siegmund2022tnfreceptorassociated pages 7-9).

---

## 5. Evolutionary and Cell-Biological Variation

### 5.1 Deep Evolutionary Origins

The TNF–TNFR signaling system has ancient metazoan origins. Comparative genomic analysis across 148 species spanning all metazoan phyla indicates that TNF superfamily (TNFSF) ligand homologs (Eiger-type) first appear after Ctenophora, while receptor homologs (Grindelwald-type) originate after Porifera but before Cnidaria, placing the earliest ligand–receptor system at approximately 700 million years ago (menon2024caughtinthe pages 1-4, menon2024caughtinthe pages 4-8). The Drosophila melanogaster system, featuring the single TNF ligand Eiger and its receptors Wengen and Grindelwald, signals primarily through the JNK pathway rather than a direct NF-κB counterpart (menon2024caughtinthe pages 1-4). Structural comparison of the DmEiger–DmGrnd complex with the human TNF–TNFR1 complex reveals conservation of the trimeric ligand–receptor binding configuration (menon2024caughtinthe pages 1-4, menon2024caughtinthe pages 11-13). Conserved sequence signatures include the TNF Homology Domain (THD) with GLY and FFG motifs in ligands, and cysteine-rich domains (CXXCXXC/CXXCXXXC) connected by disulfide bridges in receptors (menon2024caughtinthe pages 11-13).

Notably, the TNF–TNFR system has been independently lost in Nematoda (including C. elegans), Tardigrada, Chelicerata, and certain parasitic Platyhelminthes (menon2024caughtinthe pages 8-11, menon2024caughtinthe pages 4-8). The expansion from a single ancestral ligand–receptor pair to 29 TNFSF ligands and 19 TNFRSF receptors in humans reflects extensive mammalian-lineage elaboration (menon2024caughtinthe pages 1-4). Cross-reactivity between Cnidarian Grnd homologs and human TNF-α has been demonstrated experimentally, supporting deep structural conservation of the binding interface (menon2024caughtinthe pages 8-11).

### 5.2 Cell-Type and Tissue Variation

Cellular responses to TNF are inherently heterogeneous, both within isogenic populations and across cell types (preedy2024cellularheterogeneityin pages 2-3). Key sources of variation include:

- **Receptor density and expression patterns**: TNFR1 is ubiquitously expressed, while TNFR2 is preferentially expressed on leukocytes and endothelial cells (smulski2024editorialreviewsand pages 1-2).
- **Cell-type-specific outcomes**: Tissue-specific knockout studies reveal distinct phenotypes in intestinal epithelial cells, endothelial cells, and keratinocytes, reflecting different baseline expression levels of checkpoint components (loo2023deathbytnf pages 7-8).
- **TRAF2/RIPK1 contribution varies across cell lines**: In HCT116 and HT29 cells, TRAF2 deficiency reduces but does not abolish TNF-induced NF-κB signaling, while in HeLa-RIPK3 cells TRAF2 loss has minimal effect on IκBα dynamics (wagner2025traf2andripk1 pages 4-5). This cell-type dependence reflects compensatory mechanisms and variable expression of parallel signaling arms.
- **Stochastic single-cell variation**: NF-κB nuclear translocation patterns vary from single pulses to sustained oscillations among individual cells within a population, contributing to heterogeneous gene expression outputs (preedy2024cellularheterogeneityin pages 2-3).
- **Membrane microdomain context**: Cholesterol-rich membrane microdomains, N-glycosylation of receptors, and receptor clustering differentially regulate Complex I assembly and signaling strength (rafeeq2025targetingtnfr1drivennecroptosis pages 4-6).

### 5.3 Soluble Versus Membrane-Bound TNF

Membrane-bound TNF (tmTNF) forms high-affinity, multivalent contacts with TNFR1 resulting in stronger and more sustained signaling, whereas sTNF promotes only transient interactions with shorter residency times (rafeeq2025targetingtnfr1drivennecroptosis pages 4-6). sTNF is relatively poor at activating TNFR2 compared with tmTNF, which may partly explain discrepancies between in vitro (typically sTNF) and in vivo (both forms) experimental outcomes (loo2023deathbytnf pages 7-8). This distinction is therapeutically relevant: selective sTNF blockade may preserve beneficial tmTNF/TNFR2 signaling while reducing pathological inflammation.

---

## 6. Constraints, Dependencies, and Failure Modes

### 6.1 Obligatory Ordering

Several steps in the pathway follow a strict temporal order:

1. TNF–TNFR1 ligation must precede all downstream events.
2. TRADD and RIPK1 recruitment to the receptor DD is a prerequisite for Complex I assembly (li2025exploringtnfr1from pages 4-6, loo2023deathbytnf pages 2-3).
3. K63-linked ubiquitination by cIAP1/2 must occur before LUBAC recruitment and linear ubiquitination (so2022theimmunologicalsignificance pages 2-3, xiao2025theroleof pages 9-12).
4. TAK1 activation must precede IKKβ phosphorylation and NF-κB release (so2022theimmunologicalsignificance pages 4-5).
5. Complex II formation is kinetically delayed relative to Complex I, typically requiring hours rather than the seconds-to-minutes timescale of Complex I assembly (siegmund2023fn14andtnfr2 pages 4-5).

### 6.2 Mutually Exclusive Outcomes

- Apoptosis and necroptosis are mutually exclusive at the caspase-8 checkpoint: active caspase-8 cleaves RIPK1/RIPK3 to prevent necroptosis, while caspase-8 inhibition enables necrosome formation (loo2023deathbytnf pages 5-6, siegmund2023fn14andtnfr2 pages 4-5).
- The maintenance of RIPK1 in a ubiquitinated, scaffold-stabilized state within Complex I is mutually exclusive with its kinase-active, death-signaling form in Complex IIb (manohar2024atthecrossroads pages 7-8, rafeeq2025targetingtnfr1drivennecroptosis pages 4-6).

### 6.3 Genetic Failure Modes

Loss of cIAP1/2 E3 ligase activity is embryonically lethal in mice due to unrestrained RIPK1-mediated apoptosis, demonstrating the essential nature of the ubiquitin checkpoint (wagner2025traf2andripk1 pages 1-2). Expression of kinase-inactive RIPK1^D138N rescues embryonic development in cIAP1/2 mutant mice, but these animals develop systemic TNF-driven inflammation and die post-weaning, indicating additional RIPK1 kinase-independent death pathways controlled by cIAPs (wagner2025traf2andripk1 pages 1-2). Loss-of-function mutations in LUBAC components (HOIP, HOIL-1L, SHARPIN) or OTULIN cause human autoinflammatory diseases driven by TNF- and RIPK1-mediated cell death (loo2023deathbytnf pages 9-11).

---

## 7. Controversies and Open Questions

### 7.1 TRAF2 and RIPK1: Linear Pathway or Redundant Arms?

The conventional model positions RIPK1 downstream of TRAF2 as a substrate for cIAP-mediated K63 ubiquitination. However, Wagner et al. (2025) demonstrated that TRAF2 and RIPK1 act redundantly in classical NF-κB signaling: single knockouts of either protein leave TNF-induced IL-8 production and IκBα degradation largely intact across multiple cell lines, whereas combined TRAF2/RIPK1 deficiency completely abolishes NF-κB signaling (wagner2025traf2andripk1 pages 5-8, wagner2025traf2andripk1 pages 1-2). This has led to a revised model proposing two distinguishable Complex I subtypes: Complex Ia (TRADD–TRAF2/cIAP-dependent) and Complex Ib (non-modified RIPK1-dependent), which may cooperate and interact (wagner2025traf2andripk1 pages 1-2). This represents a significant departure from the strictly linear sequence traditionally assumed.

### 7.2 The Dual Role of FADD and Caspase-8

The mechanism by which FADD simultaneously promotes and inhibits caspase-8 activation within Complex II remains unclear (loo2023deathbytnf pages 7-8). Similarly, there are competing views on caspase-8-mediated RIPK1 cleavage: some studies suggest it promotes apoptosis by inhibiting pro-survival gene expression, while others propose it limits cell death (preedy2024cellularheterogeneityin pages 3-4). Whether the outcome depends on the stoichiometry of caspase-8 and FLIP isoforms, or on additional contextual factors, is an active area of investigation.

### 7.3 In Vitro Versus In Vivo Discrepancies

Most mechanistic studies of TNF signaling use supraphysiological concentrations of recombinant sTNF, which may not recapitulate the biology of tmTNF. The weaker TNFR2 activation by sTNF and the different receptor residency times may explain why certain cell death phenotypes are more prominent in vitro than in vivo (rafeeq2025targetingtnfr1drivennecroptosis pages 4-6, loo2023deathbytnf pages 7-8).

### 7.4 Cell-Type Specificity of Pathway Architecture

The degree to which each checkpoint component is expressed, and therefore the dominant mode of cell death upon checkpoint failure, varies dramatically between cell types (wagner2025traf2andripk1 pages 4-5, loo2023deathbytnf pages 7-8). Whether this variation reflects genuine alternative pathway wiring or quantitative differences in the same core architecture remains debated.

### 7.5 Interferon-γ Co-Sensing

How co-sensing of TNF and interferon-γ affects downstream TNFR1 cell death checkpoints is still poorly understood, despite the well-known synergy between these cytokines in driving inflammatory cell death (loo2023deathbytnf pages 7-8).

### 7.6 A20 Mechanism

A20 was long considered primarily an NF-κB inhibitor via deubiquitinase activity, but recent evidence indicates its primary anti-inflammatory mechanism is preventing cell death rather than suppressing NF-κB signaling per se (loo2023deathbytnf pages 9-11). The precise molecular mechanism by which A20 stabilizes M1-linked ubiquitin chains and prevents RIPK1 activation requires further elucidation.

---

## 8. Key References

The major sources informing this review include:

- van Loo G & Bertrand MJM. Death by TNF: a road to inflammation. *Nature Reviews Immunology* 23:289–303, 2023. DOI: 10.1038/s41577-022-00792-3 (loo2023deathbytnf pages 2-3, loo2023deathbytnf pages 3-5, loo2023deathbytnf pages 5-6, loo2023deathbytnf pages 7-8, loo2023deathbytnf pages 9-11)
- Wagner J et al. TRAF2 and RIPK1 redundantly mediate classical NFκB signaling by TNFR1 and CD95-type death receptors. *Cell Death & Disease* 16, 2025. DOI: 10.1038/s41419-024-07325-x (wagner2025traf2andripk1 pages 1-2, wagner2025traf2andripk1 pages 5-8, wagner2025traf2andripk1 pages 4-5)
- Preedy MK, White MRH, Tergaonkar V. Cellular heterogeneity in TNF/TNFR1 signalling. *Cell Death & Disease* 15, 2024. DOI: 10.1038/s41419-024-06559-z (preedy2024cellularheterogeneityin pages 2-3, preedy2024cellularheterogeneityin pages 3-4)
- Li Y et al. Exploring TNFR1: from discovery to targeted therapy development. *Journal of Translational Medicine* 23, 2025. DOI: 10.1186/s12967-025-06122-0 (li2025exploringtnfr1from pages 4-6)
- Siegmund D, Zaitseva O, Wajant H. Fn14 and TNFR2 as regulators of cytotoxic TNFR1 signaling. *Frontiers in Cell and Developmental Biology* 11, 2023. DOI: 10.3389/fcell.2023.1267837 (siegmund2023fn14andtnfr2 pages 4-5)
- Siegmund D, Wagner J, Wajant H. TNF Receptor Associated Factor 2 (TRAF2) Signaling in Cancer. *Cancers* 14:4055, 2022. DOI: 10.3390/cancers14164055 (siegmund2022tnfreceptorassociated pages 5-7, siegmund2022tnfreceptorassociated pages 1-2, siegmund2022tnfreceptorassociated pages 2-4, siegmund2022tnfreceptorassociated pages 7-9)
- Albini A et al. Inflammation and cancer cell survival: TRAF2 as a key player. *Cell Death & Disease* 16, 2025. DOI: 10.1038/s41419-025-07609-w (albini2025inflammationandcancer pages 2-3, albini2025inflammationandcancer pages 3-4)
- So T. The immunological significance of tumor necrosis factor receptor-associated factors (TRAFs). *International Immunology* 34:7–20, 2022. DOI: 10.1093/intimm/dxab058 (so2022theimmunologicalsignificance pages 2-3, so2022theimmunologicalsignificance pages 4-5, so2022theimmunologicalsignificance pages 3-4)
- Wang X et al. The Dual Role of TRADD in Liver Disease. *International Journal of Molecular Sciences* 26:5860, 2025. DOI: 10.3390/ijms26125860 (wang2025thedualrole pages 2-4)
- Manohar SM. At the Crossroads of TNFα Signaling and Cancer. *Current Molecular Pharmacology* 17, 2024. DOI: 10.2174/1874467217666230908111754 (manohar2024atthecrossroads pages 2-4, manohar2024atthecrossroads pages 7-8)
- Xiao H et al. The Role of Post-Translational Modifications in Necroptosis. *Biomolecules* 15:549, 2025. DOI: 10.3390/biom15040549 (xiao2025theroleof pages 5-5, xiao2025theroleof pages 9-12, xiao2025theroleof pages 33-34)
- Rafeeq MM et al. Targeting TNFR1-driven necroptosis in breast cancer. *EXCLI Journal* 24:1690–1712, 2025. DOI: 10.17179/excli2025-8873 (rafeeq2025targetingtnfr1drivennecroptosis pages 4-6)
- Menon N et al. Caught in the act of triplication: TNF superfamily. *bioRxiv* 2024. DOI: 10.1101/2024.07.27.603686 (menon2024caughtinthe pages 1-4, menon2024caughtinthe pages 8-11, menon2024caughtinthe pages 11-13, menon2024caughtinthe pages 4-8)
- Schorn F et al. cIAPs control RIPK1 kinase activity-dependent and -independent cell death and tissue inflammation. *EMBO Journal* 42, 2023. DOI: 10.15252/embj.2023113614
- Smulski CR. Editorial: Reviews and advances in inflammatory diseases and TNF. *Frontiers in Cell and Developmental Biology* 12, 2024. DOI: 10.3389/fcell.2024.1399804 (smulski2024editorialreviewsand pages 1-2)

References

1. (loo2023deathbytnf pages 2-3): Geert van Loo and Mathieu J. M. Bertrand. Death by tnf: a road to inflammation. Nature Reviews. Immunology, 23:289-303, Nov 2023. URL: https://doi.org/10.1038/s41577-022-00792-3, doi:10.1038/s41577-022-00792-3. This article has 1102 citations.

2. (li2025exploringtnfr1from pages 4-6): Yingying Li, Ruiwei Ye, Haorui Dai, Jiayi Lin, Yue Cheng, Yonghong Zhou, and Yiming Lu. Exploring tnfr1: from discovery to targeted therapy development. Journal of Translational Medicine, Jan 2025. URL: https://doi.org/10.1186/s12967-025-06122-0, doi:10.1186/s12967-025-06122-0. This article has 74 citations and is from a peer-reviewed journal.

3. (so2022theimmunologicalsignificance pages 2-3): Takanori So. The immunological significance of tumor necrosis factor receptor-associated factors (trafs). International immunology, 34:7-20, Aug 2022. URL: https://doi.org/10.1093/intimm/dxab058, doi:10.1093/intimm/dxab058. This article has 54 citations and is from a peer-reviewed journal.

4. (loo2023deathbytnf pages 3-5): Geert van Loo and Mathieu J. M. Bertrand. Death by tnf: a road to inflammation. Nature Reviews. Immunology, 23:289-303, Nov 2023. URL: https://doi.org/10.1038/s41577-022-00792-3, doi:10.1038/s41577-022-00792-3. This article has 1102 citations.

5. (loo2023deathbytnf pages 5-6): Geert van Loo and Mathieu J. M. Bertrand. Death by tnf: a road to inflammation. Nature Reviews. Immunology, 23:289-303, Nov 2023. URL: https://doi.org/10.1038/s41577-022-00792-3, doi:10.1038/s41577-022-00792-3. This article has 1102 citations.

6. (smulski2024editorialreviewsand pages 1-2): Cristian R. Smulski. Editorial: reviews and advances in inflammatory diseases and the tumor necrosis factor. Frontiers in Cell and Developmental Biology, Apr 2024. URL: https://doi.org/10.3389/fcell.2024.1399804, doi:10.3389/fcell.2024.1399804. This article has 1 citations.

7. (siegmund2022tnfreceptorassociated pages 7-9): Daniela Siegmund, Jennifer Wagner, and Harald Wajant. Tnf receptor associated factor 2 (traf2) signaling in cancer. Cancers, 14:4055, Aug 2022. URL: https://doi.org/10.3390/cancers14164055, doi:10.3390/cancers14164055. This article has 89 citations.

8. (loo2023deathbytnf pages 7-8): Geert van Loo and Mathieu J. M. Bertrand. Death by tnf: a road to inflammation. Nature Reviews. Immunology, 23:289-303, Nov 2023. URL: https://doi.org/10.1038/s41577-022-00792-3, doi:10.1038/s41577-022-00792-3. This article has 1102 citations.

9. (siegmund2023fn14andtnfr2 pages 4-5): Daniela Siegmund, Olena Zaitseva, and Harald Wajant. Fn14 and tnfr2 as regulators of cytotoxic tnfr1 signaling. Frontiers in Cell and Developmental Biology, Nov 2023. URL: https://doi.org/10.3389/fcell.2023.1267837, doi:10.3389/fcell.2023.1267837. This article has 18 citations.

10. (manohar2024atthecrossroads pages 2-4): Sonal M. Manohar. At the crossroads of tnf α signaling and cancer. Oct 2024. URL: https://doi.org/10.2174/1874467217666230908111754, doi:10.2174/1874467217666230908111754. This article has 108 citations and is from a peer-reviewed journal.

11. (rafeeq2025targetingtnfr1drivennecroptosis pages 4-6): Misbahuddin M. Rafeeq, Muhammad Afzal, Muhammad Shahid Nadeem, A. H. Habib, H. Alsufyani, Sami I. Alzarea, O. Alsaidan, and I. Kazmi. Targeting tnfr1-driven necroptosis in breast cancer. EXCLI Journal, 24:1690-1712, Dec 2025. URL: https://doi.org/10.17179/excli2025-8873, doi:10.17179/excli2025-8873. This article has 1 citations and is from a peer-reviewed journal.

12. (wang2025thedualrole pages 2-4): Xueling Wang, Qiwen Tan, Di Zhang, Huan Cao, Shenghe Deng, and Yu Zhang. The dual role of tradd in liver disease: from cell death regulation to inflammatory microenvironment remodeling. International Journal of Molecular Sciences, 26:5860, Jun 2025. URL: https://doi.org/10.3390/ijms26125860, doi:10.3390/ijms26125860. This article has 6 citations.

13. (xiao2025theroleof pages 9-12): Hao Xiao, Zeping Han, Min Xu, Xukang Gao, Shuangjian Qiu, Ning Ren, Yong Yi, and Chenhao Zhou. The role of post-translational modifications in necroptosis. Biomolecules, 15:549, Apr 2025. URL: https://doi.org/10.3390/biom15040549, doi:10.3390/biom15040549. This article has 7 citations.

14. (so2022theimmunologicalsignificance pages 4-5): Takanori So. The immunological significance of tumor necrosis factor receptor-associated factors (trafs). International immunology, 34:7-20, Aug 2022. URL: https://doi.org/10.1093/intimm/dxab058, doi:10.1093/intimm/dxab058. This article has 54 citations and is from a peer-reviewed journal.

15. (preedy2024cellularheterogeneityin pages 2-3): Marcus K. Preedy, Michael R. H. White, and Vinay Tergaonkar. Cellular heterogeneity in tnf/tnfr1 signalling: live cell imaging of cell fate decisions in single cells. Cell Death &amp; Disease, Mar 2024. URL: https://doi.org/10.1038/s41419-024-06559-z, doi:10.1038/s41419-024-06559-z. This article has 63 citations and is from a peer-reviewed journal.

16. (preedy2024cellularheterogeneityin pages 3-4): Marcus K. Preedy, Michael R. H. White, and Vinay Tergaonkar. Cellular heterogeneity in tnf/tnfr1 signalling: live cell imaging of cell fate decisions in single cells. Cell Death &amp; Disease, Mar 2024. URL: https://doi.org/10.1038/s41419-024-06559-z, doi:10.1038/s41419-024-06559-z. This article has 63 citations and is from a peer-reviewed journal.

17. (wagner2025traf2andripk1 pages 1-2): Jennifer Wagner, David Vredevoogd, Xin Yu, Dong Lu, Daniel S. Peeper, Heike M. Hermanns, Jin Wang, Harald Wajant, and Daniela Siegmund. Traf2 and ripk1 redundantly mediate classical nfκb signaling by tnfr1 and cd95-type death receptors. Cell Death & Disease, Jan 2025. URL: https://doi.org/10.1038/s41419-024-07325-x, doi:10.1038/s41419-024-07325-x. This article has 15 citations and is from a peer-reviewed journal.

18. (albini2025inflammationandcancer pages 2-3): Adriana Albini, Luisa Di Paola, Giampiero Mei, Denisa Baci, Nicola Fusco, Giovanni Corso, and Douglas Noonan. Inflammation and cancer cell survival: traf2 as a key player. Cell Death & Disease, Apr 2025. URL: https://doi.org/10.1038/s41419-025-07609-w, doi:10.1038/s41419-025-07609-w. This article has 28 citations and is from a peer-reviewed journal.

19. (siegmund2022tnfreceptorassociated pages 5-7): Daniela Siegmund, Jennifer Wagner, and Harald Wajant. Tnf receptor associated factor 2 (traf2) signaling in cancer. Cancers, 14:4055, Aug 2022. URL: https://doi.org/10.3390/cancers14164055, doi:10.3390/cancers14164055. This article has 89 citations.

20. (siegmund2022tnfreceptorassociated pages 1-2): Daniela Siegmund, Jennifer Wagner, and Harald Wajant. Tnf receptor associated factor 2 (traf2) signaling in cancer. Cancers, 14:4055, Aug 2022. URL: https://doi.org/10.3390/cancers14164055, doi:10.3390/cancers14164055. This article has 89 citations.

21. (wagner2025traf2andripk1 pages 5-8): Jennifer Wagner, David Vredevoogd, Xin Yu, Dong Lu, Daniel S. Peeper, Heike M. Hermanns, Jin Wang, Harald Wajant, and Daniela Siegmund. Traf2 and ripk1 redundantly mediate classical nfκb signaling by tnfr1 and cd95-type death receptors. Cell Death & Disease, Jan 2025. URL: https://doi.org/10.1038/s41419-024-07325-x, doi:10.1038/s41419-024-07325-x. This article has 15 citations and is from a peer-reviewed journal.

22. (wagner2025traf2andripk1 pages 4-5): Jennifer Wagner, David Vredevoogd, Xin Yu, Dong Lu, Daniel S. Peeper, Heike M. Hermanns, Jin Wang, Harald Wajant, and Daniela Siegmund. Traf2 and ripk1 redundantly mediate classical nfκb signaling by tnfr1 and cd95-type death receptors. Cell Death & Disease, Jan 2025. URL: https://doi.org/10.1038/s41419-024-07325-x, doi:10.1038/s41419-024-07325-x. This article has 15 citations and is from a peer-reviewed journal.

23. (siegmund2022tnfreceptorassociated pages 2-4): Daniela Siegmund, Jennifer Wagner, and Harald Wajant. Tnf receptor associated factor 2 (traf2) signaling in cancer. Cancers, 14:4055, Aug 2022. URL: https://doi.org/10.3390/cancers14164055, doi:10.3390/cancers14164055. This article has 89 citations.

24. (loo2023deathbytnf pages 9-11): Geert van Loo and Mathieu J. M. Bertrand. Death by tnf: a road to inflammation. Nature Reviews. Immunology, 23:289-303, Nov 2023. URL: https://doi.org/10.1038/s41577-022-00792-3, doi:10.1038/s41577-022-00792-3. This article has 1102 citations.

25. (manohar2024atthecrossroads pages 7-8): Sonal M. Manohar. At the crossroads of tnf α signaling and cancer. Oct 2024. URL: https://doi.org/10.2174/1874467217666230908111754, doi:10.2174/1874467217666230908111754. This article has 108 citations and is from a peer-reviewed journal.

26. (xiao2025theroleof pages 33-34): Hao Xiao, Zeping Han, Min Xu, Xukang Gao, Shuangjian Qiu, Ning Ren, Yong Yi, and Chenhao Zhou. The role of post-translational modifications in necroptosis. Biomolecules, 15:549, Apr 2025. URL: https://doi.org/10.3390/biom15040549, doi:10.3390/biom15040549. This article has 7 citations.

27. (xiao2025theroleof pages 5-5): Hao Xiao, Zeping Han, Min Xu, Xukang Gao, Shuangjian Qiu, Ning Ren, Yong Yi, and Chenhao Zhou. The role of post-translational modifications in necroptosis. Biomolecules, 15:549, Apr 2025. URL: https://doi.org/10.3390/biom15040549, doi:10.3390/biom15040549. This article has 7 citations.

28. (so2022theimmunologicalsignificance pages 3-4): Takanori So. The immunological significance of tumor necrosis factor receptor-associated factors (trafs). International immunology, 34:7-20, Aug 2022. URL: https://doi.org/10.1093/intimm/dxab058, doi:10.1093/intimm/dxab058. This article has 54 citations and is from a peer-reviewed journal.

29. (menon2024caughtinthe pages 1-4): Namita Menon, Kaushiki K, Moushmi Goswami, Anmol Singh, and Subhashini Srinivasan. Caught in the act of triplication: tnf superfamily. bioRxiv, Jul 2024. URL: https://doi.org/10.1101/2024.07.27.603686, doi:10.1101/2024.07.27.603686. This article has 0 citations.

30. (menon2024caughtinthe pages 4-8): Namita Menon, Kaushiki K, Moushmi Goswami, Anmol Singh, and Subhashini Srinivasan. Caught in the act of triplication: tnf superfamily. bioRxiv, Jul 2024. URL: https://doi.org/10.1101/2024.07.27.603686, doi:10.1101/2024.07.27.603686. This article has 0 citations.

31. (menon2024caughtinthe pages 11-13): Namita Menon, Kaushiki K, Moushmi Goswami, Anmol Singh, and Subhashini Srinivasan. Caught in the act of triplication: tnf superfamily. bioRxiv, Jul 2024. URL: https://doi.org/10.1101/2024.07.27.603686, doi:10.1101/2024.07.27.603686. This article has 0 citations.

32. (menon2024caughtinthe pages 8-11): Namita Menon, Kaushiki K, Moushmi Goswami, Anmol Singh, and Subhashini Srinivasan. Caught in the act of triplication: tnf superfamily. bioRxiv, Jul 2024. URL: https://doi.org/10.1101/2024.07.27.603686, doi:10.1101/2024.07.27.603686. This article has 0 citations.

33. (albini2025inflammationandcancer pages 3-4): Adriana Albini, Luisa Di Paola, Giampiero Mei, Denisa Baci, Nicola Fusco, Giovanni Corso, and Douglas Noonan. Inflammation and cancer cell survival: traf2 as a key player. Cell Death & Disease, Apr 2025. URL: https://doi.org/10.1038/s41419-025-07609-w, doi:10.1038/s41419-025-07609-w. This article has 28 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](tnf_signaling-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](tnf_signaling-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. loo2023deathbytnf pages 2-3
2. siegmund2022tnfreceptorassociated pages 7-9
3. manohar2024atthecrossroads pages 2-4
4. loo2023deathbytnf pages 7-8
5. so2022theimmunologicalsignificance pages 2-3
6. loo2023deathbytnf pages 5-6
7. loo2023deathbytnf pages 9-11
8. siegmund2022tnfreceptorassociated pages 2-4
9. so2022theimmunologicalsignificance pages 3-4
10. menon2024caughtinthe pages 1-4
11. menon2024caughtinthe pages 11-13
12. menon2024caughtinthe pages 8-11
13. preedy2024cellularheterogeneityin pages 2-3
14. smulski2024editorialreviewsand pages 1-2
15. so2022theimmunologicalsignificance pages 4-5
16. preedy2024cellularheterogeneityin pages 3-4
17. wang2025thedualrole pages 2-4
18. loo2023deathbytnf pages 3-5
19. xiao2025theroleof pages 9-12
20. albini2025inflammationandcancer pages 2-3
21. siegmund2022tnfreceptorassociated pages 5-7
22. siegmund2022tnfreceptorassociated pages 1-2
23. manohar2024atthecrossroads pages 7-8
24. xiao2025theroleof pages 33-34
25. xiao2025theroleof pages 5-5
26. menon2024caughtinthe pages 4-8
27. albini2025inflammationandcancer pages 3-4
28. https://doi.org/10.1038/s41577-022-00792-3,
29. https://doi.org/10.1186/s12967-025-06122-0,
30. https://doi.org/10.1093/intimm/dxab058,
31. https://doi.org/10.3389/fcell.2024.1399804,
32. https://doi.org/10.3390/cancers14164055,
33. https://doi.org/10.3389/fcell.2023.1267837,
34. https://doi.org/10.2174/1874467217666230908111754,
35. https://doi.org/10.17179/excli2025-8873,
36. https://doi.org/10.3390/ijms26125860,
37. https://doi.org/10.3390/biom15040549,
38. https://doi.org/10.1038/s41419-024-06559-z,
39. https://doi.org/10.1038/s41419-024-07325-x,
40. https://doi.org/10.1038/s41419-025-07609-w,
41. https://doi.org/10.1101/2024.07.27.603686,