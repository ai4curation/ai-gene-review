---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-30T05:12:57.724040'
end_time: '2026-09-30T05:29:25.906119'
duration_seconds: 988.18
template_file: templates/module_research.md.j2
template_variables:
  module_title: Canonical Notch signaling pathway module
  module_summary: A compact metazoan Notch signaling module. Notch is a contact-dependent
    juxtacrine pathway in which a Delta/Serrate/LAG-2 family ligand on one cell binds
    a Notch receptor on a neighboring cell, triggers ADAM/gamma-secretase proteolysis,
    releases the Notch intracellular domain, and converts CSL/RBPJ transcription complexes
    from repressors to activators of targets such as HES and HEY family genes. The
    trunk is grounded in GO:0007219 and annotated with curated UniProt exemplars plus
    PAINT ancestral nodes where the local PANTHER cache supports a function-by-descent
    claim.
  module_outline: "- Canonical Notch signaling pathway\n  - 1. ligand-receptor contact\n\
    \  - DSL ligand binding to Notch receptor\n    - Delta/Jagged Notch ligand (molecular\
    \ player: Delta/Serrate/LAG-2 Notch ligands; activity or role: Notch receptor\
    \ binding)\n    - Notch receptor (molecular player: Notch receptor family)\n \
    \ - 2. receptor cleavage and NICD release\n  - Proteolytic release of Notch intracellular\
    \ domain\n    - ADAM/gamma-secretase cleavage of Notch (molecular player: Notch-cleaving\
    \ protease module)\n  - 3. CSL/RBPJ transcriptional switch\n  - NICD-CSL-MAML\
    \ transcriptional activation\n    - HES/HEY transcriptional output (molecular\
    \ player: HES/HEY bHLH transcriptional repressors)"
  module_connections: '- DSL ligand binding to Notch receptor causes Proteolytic release
    of Notch intracellular domain: Ligand-induced mechanical activation exposes the
    Notch cleavage site.

    - Proteolytic release of Notch intracellular domain causes NICD-CSL-MAML transcriptional
    activation: Released NICD enters the nucleus and activates CSL/RBPJ-bound targets.'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 58
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: notch_signaling-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: notch_signaling-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
---

## Question

# Commissioned Review Brief

## Review Topic

Canonical Notch signaling pathway module

## Working Scope

A compact metazoan Notch signaling module. Notch is a contact-dependent juxtacrine pathway in which a Delta/Serrate/LAG-2 family ligand on one cell binds a Notch receptor on a neighboring cell, triggers ADAM/gamma-secretase proteolysis, releases the Notch intracellular domain, and converts CSL/RBPJ transcription complexes from repressors to activators of targets such as HES and HEY family genes. The trunk is grounded in GO:0007219 and annotated with curated UniProt exemplars plus PAINT ancestral nodes where the local PANTHER cache supports a function-by-descent claim.

## Provisional Biological Outline

- Canonical Notch signaling pathway
  - 1. ligand-receptor contact
  - DSL ligand binding to Notch receptor
    - Delta/Jagged Notch ligand (molecular player: Delta/Serrate/LAG-2 Notch ligands; activity or role: Notch receptor binding)
    - Notch receptor (molecular player: Notch receptor family)
  - 2. receptor cleavage and NICD release
  - Proteolytic release of Notch intracellular domain
    - ADAM/gamma-secretase cleavage of Notch (molecular player: Notch-cleaving protease module)
  - 3. CSL/RBPJ transcriptional switch
  - NICD-CSL-MAML transcriptional activation
    - HES/HEY transcriptional output (molecular player: HES/HEY bHLH transcriptional repressors)

## Known Relationships Among Steps

- DSL ligand binding to Notch receptor causes Proteolytic release of Notch intracellular domain: Ligand-induced mechanical activation exposes the Notch cleavage site.
- Proteolytic release of Notch intracellular domain causes NICD-CSL-MAML transcriptional activation: Released NICD enters the nucleus and activates CSL/RBPJ-bound targets.

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

Canonical Notch signaling pathway module

## Working Scope

A compact metazoan Notch signaling module. Notch is a contact-dependent juxtacrine pathway in which a Delta/Serrate/LAG-2 family ligand on one cell binds a Notch receptor on a neighboring cell, triggers ADAM/gamma-secretase proteolysis, releases the Notch intracellular domain, and converts CSL/RBPJ transcription complexes from repressors to activators of targets such as HES and HEY family genes. The trunk is grounded in GO:0007219 and annotated with curated UniProt exemplars plus PAINT ancestral nodes where the local PANTHER cache supports a function-by-descent claim.

## Provisional Biological Outline

- Canonical Notch signaling pathway
  - 1. ligand-receptor contact
  - DSL ligand binding to Notch receptor
    - Delta/Jagged Notch ligand (molecular player: Delta/Serrate/LAG-2 Notch ligands; activity or role: Notch receptor binding)
    - Notch receptor (molecular player: Notch receptor family)
  - 2. receptor cleavage and NICD release
  - Proteolytic release of Notch intracellular domain
    - ADAM/gamma-secretase cleavage of Notch (molecular player: Notch-cleaving protease module)
  - 3. CSL/RBPJ transcriptional switch
  - NICD-CSL-MAML transcriptional activation
    - HES/HEY transcriptional output (molecular player: HES/HEY bHLH transcriptional repressors)

## Known Relationships Among Steps

- DSL ligand binding to Notch receptor causes Proteolytic release of Notch intracellular domain: Ligand-induced mechanical activation exposes the Notch cleavage site.
- Proteolytic release of Notch intracellular domain causes NICD-CSL-MAML transcriptional activation: Released NICD enters the nucleus and activates CSL/RBPJ-bound targets.

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

# The Canonical Notch Signaling Pathway: A Comprehensive Review

## Executive Summary

The canonical Notch signaling pathway represents one of the most evolutionarily conserved cell communication systems in metazoans, orchestrating cell fate decisions through direct contact-dependent signaling between neighboring cells (lv2024evolutionandfunction pages 1-2, he2021comparativeandevolutionary pages 1-2). This pathway couples ligand-receptor engagement at the cell surface to sequential proteolytic processing, culminating in nuclear translocation of the Notch intracellular domain (NICD) and transcriptional activation of target genes (sprinzak2021biophysicsofnotch pages 1-3, lv2024evolutionandfunction pages 2-4). The canonical pathway is distinguished from non-canonical Notch signaling by its obligate dependence on the NICD–RBPJ/CSL–MAML transcriptional complex and characteristic induction of HES and HEY family genes (zack2024anothernotchin pages 5-10, guo2023notchsignalinghypoxia pages 1-2). Despite remarkable conservation of core components from cnidarians through insects to vertebrates, the pathway exhibits context-dependent outputs and lineage-specific elaborations that remain areas of active investigation (he2021comparativeandevolutionary pages 9-10, zhou2022notchsignalingpathway pages 21-22, sachan2023notchsignallingmultifaceted pages 18-18).

## Definition and Biological Boundaries

### Scope of the Canonical Pathway

The canonical Notch pathway is grounded in Gene Ontology term GO:0007219 and constitutes a compact metazoan signaling module with three obligatory steps: (1) DSL ligand binding to Notch receptor on an adjacent cell, (2) ADAM/gamma-secretase proteolysis releasing NICD, and (3) conversion of CSL transcription complexes from repressors to activators (lv2024evolutionandfunction pages 2-4). This juxtacrine signaling mechanism requires direct cell-cell contact, distinguishing it from paracrine or endocrine pathways (sprinzak2021biophysicsofnotch pages 1-3).

### Boundaries and Distinctions from Related Processes

Canonical Notch signaling should be clearly distinguished from several related but mechanistically distinct phenomena. **Non-canonical Notch signaling** encompasses NICD activity independent of RBPJ/CSL or ligand-independent activation mechanisms that bypass the standard DSL-dependent receptor processing (zack2024anothernotchin pages 5-10, wang2024mechanismofnotch pages 3-5, gratton2020pleiotropicroleof pages 5-7). These alternative routes can involve interactions with NF-κB, PI3K/AKT, Wnt, TGF-β, and other pathways, sometimes using membrane-tethered Notch fragments prior to S3 cleavage or engaging non-DSL ligands such as DNER, NB3/Contactin6, or MAGP proteins (wang2024mechanismofnotch pages 3-5, sen2023theintricatenotch pages 4-5).

**Receptor maturation processes** include the constitutive S1 furin cleavage in the trans-Golgi network, which produces the mature heterodimeric receptor but does not activate signaling (sen2023theintricatenotch pages 2-4, sprinzak2021biophysicsofnotch pages 7-9). Similarly, **glycosylation modifications** by O-fucosyl-, O-glucose-, and O-GlcNAc-transferases, along with Fringe-family modifying enzymes, regulate ligand-receptor specificity and affinity but are modulatory rather than core pathway components (reichrath2020notchsignalingand pages 51-53).

**Ligand trafficking and cis-inhibition** represent regulatory mechanisms outside the canonical trans-activation trunk: ubiquitin ligases control ligand endocytosis, while same-cell cis interactions between receptors and ligands commonly inhibit rather than activate signaling (sprinzak2021biophysicsofnotch pages 11-13, sprinzak2021biophysicsofnotch pages 7-9, sprinzak2021biophysicsofnotch pages 9-11).

### Competing Definitions

The literature exhibits general consensus on the core pathway but some variation in terminology and emphasis. "Canonical" is consistently defined by NICD-mediated, CSL-dependent transcriptional activation following ligand-triggered proteolysis (zack2024anothernotchin pages 5-10, guo2023notchsignalinghypoxia pages 1-2, friedrich2023decipheringthenotch pages 23-27). However, boundaries blur regarding which regulatory proteins constitute the pathway versus its modulators: some treatments include MIB1/Neuralized ubiquitin ligases and force-generation machinery as pathway steps (sprinzak2021biophysicsofnotch pages 11-13, lv2024evolutionandfunction pages 2-4), while others classify them as accessory regulators (sprinzak2021biophysicsofnotch pages 1-3).

## Mechanistic Overview

> 1. **Ligand–receptor contact:** A membrane-bound Delta/Serrate/LAG-2 (DSL) ligand on the sender cell binds ligand-recognition EGF repeats in the extracellular domain of a Notch receptor on an adjacent receiver cell, imposing the pathway’s contact-dependent, juxtacrine geometry. (lv2024evolutionandfunction pages 2-4, sprinzak2021biophysicsofnotch pages 1-3)
> 2. **Force-dependent receptor opening:** MIB1 or Neuralized ubiquitylates the ligand and promotes epsin/clathrin-mediated endocytosis in the sender cell. Pulling on the bound receptor opens its autoinhibitory negative regulatory region (NRR), which normally masks the S2 cleavage site; the ligand-bound Notch extracellular domain is subsequently trans-endocytosed into the sender cell. (sprinzak2021biophysicsofnotch pages 11-13, sprinzak2021biophysicsofnotch pages 26-30, sprinzak2021biophysicsofnotch pages 7-9)
> 3. **S2 ectodomain shedding:** ADAM10—the principal physiological sheddase in ligand-dependent NOTCH1 activation—cleaves the exposed extracellular juxtamembrane S2 site. This removes the receptor ectodomain and leaves the membrane-tethered Notch extracellular truncation fragment, NEXT; ADAM17 is more strongly associated with experimentally induced or ligand-independent processing. (alabi2021analysisofthe pages 2-3, alabi2021analysisofthe pages 3-5, alabi2021analysisofthe pages 10-11)
> 4. **S3 cleavage and NICD release:** The presenilin-containing γ-secretase complex cleaves NEXT within its transmembrane segment at S3 and nearby sites, releasing the Notch intracellular domain (NICD) from the membrane. Depending on cellular context, this cleavage may occur at the plasma membrane or after NEXT enters an intracellular compartment. (lv2024evolutionandfunction pages 2-4, sprinzak2021biophysicsofnotch pages 7-9, hounjet2021theroleof pages 13-14)
> 5. **Nuclear entry and CSL engagement:** NICD enters the nucleus and binds DNA-associated CSL—RBPJ in mammals, Su(H) in flies, and LAG-1 in nematodes. The high-affinity interaction of NICD’s RAM domain with RBPJ helps replace or counteract the corepressor-bound, transcriptionally inactive state. (lv2024evolutionandfunction pages 2-4, hall2022thestructurebinding pages 1-2, sprinzak2021biophysicsofnotch pages 13-14)
> 6. **Assembly of the activation complex:** A Mastermind-family coactivator—MAML1–3 in mammals—binds the composite interface formed by the NICD ankyrin-repeat domain and RBPJ. The resulting NICD–RBPJ–MAML ternary complex stabilizes the active DNA-bound assembly and displaces or functionally overrides corepressors such as SHARP/SPEN. (hall2022thestructurebinding pages 1-2, sprinzak2021biophysicsofnotch pages 13-14, giaimo2021transcriptionfactorrbpj pages 3-5)
> 7. **Chromatin activation and transcriptional output:** The ternary complex recruits Mediator and histone acetyltransferases including p300/CBP and PCAF/GCN5, establishing transcriptionally permissive chromatin. Direct outputs prominently include HES/E(spl) and HEY-family genes, whose bHLH repressors execute context-dependent cell-fate, progenitor-maintenance, boundary, and oscillatory programs. (lv2024evolutionandfunction pages 2-4, hall2022thestructurebinding pages 1-2, friedrich2023decipheringthenotch pages 23-27)


*Blockquote: The seven-step canonical pathway couples trans-cellular DSL–Notch binding and force-dependent proteolysis to assembly of the nuclear NICD–RBPJ–MAML complex and HES/HEY transcription.*

The canonical pathway progresses through seven sequential steps coupling surface ligand-receptor engagement to nuclear transcription (lv2024evolutionandfunction pages 2-4, wang2024mechanismofnotch pages 3-5, gratton2020pleiotropicroleof pages 5-7). This sequence represents regulated intramembrane proteolysis (RIP), a mechanism that converts transmembrane proteins into soluble transcriptional effectors without conventional second messengers (sprinzak2021biophysicsofnotch pages 7-9).

### Obligatory Versus Conditional Steps

**Obligatory steps** include: (1) DSL ligand binding to Notch receptor EGF repeats in trans configuration, (2) exposure of the S2 cleavage site through NRR conformational change, (3) ADAM protease cleavage at S2, (4) γ-secretase cleavage at S3 releasing NICD, (5) NICD nuclear entry and RBPJ binding, (6) MAML recruitment forming the ternary complex, and (7) transcriptional activation (lv2024evolutionandfunction pages 2-4, wang2024mechanismofnotch pages 3-5, hall2022thestructurebinding pages 1-2).

**Conditional or context-dependent elements** include: the specific ligand (Delta-like versus Jagged/Serrate) and receptor paralog employed, which exhibit tissue-specific expression and non-equivalent signaling capacities (zhou2022notchsignalingpathway pages 21-22, sachan2023notchsignallingmultifaceted pages 18-18); the subcellular location of S3 cleavage (plasma membrane versus endosomal compartments) (hounjet2021theroleof pages 13-14); and the identity of downstream target genes beyond the canonical HES/HEY families, which vary substantially among cell types (friedrich2023decipheringthenotch pages 23-27, sachan2023notchsignallingmultifaceted pages 18-18).

**Accessory regulatory steps** encompass ligand ubiquitylation by MIB1/Neuralized, epsin-dependent endocytosis generating mechanical force, trans-endocytosis of the ligand-bound extracellular domain, and NICD phosphorylation-dependent degradation terminating the signal (sprinzak2021biophysicsofnotch pages 11-13, sprinzak2021biophysicsofnotch pages 16-18).

## Major Molecular Players and Active Assemblies

| Functional category | Mammals | *Drosophila melanogaster* | *Caenorhabditis elegans* | Canonical role and key features |
|---|---|---|---|---|
| Notch receptors | NOTCH1, NOTCH2, NOTCH3, NOTCH4 | Notch | LIN-12 and GLP-1 | Single-pass receptors bearing extracellular EGF-like repeats and an autoinhibitory negative regulatory region, followed intracellularly by RAM, ankyrin-repeat, and PEST-containing regions. Ligand-induced proteolysis releases NICD; receptor-family expansion in vertebrates enables paralog- and tissue-specific functions. (wang2024mechanismofnotch pages 3-5, sprinzak2021biophysicsofnotch pages 1-3, lv2024evolutionandfunction pages 1-2) |
| Canonical DSL ligands | DLL1, DLL4, JAG1, JAG2; DLL3 is DSL-family but principally cis-inhibitory rather than a conventional trans-activator | Delta and Serrate | LAG-2 and related DSL ligands | Membrane-tethered ligands use an N-terminal C2/MNNL region, DSL domain, and EGF-like repeats to engage receptors on an adjacent cell. Productive trans-activation generally requires ligand ubiquitylation and endocytosis; same-cell cis interactions commonly inhibit receptor responsiveness. (sprinzak2021biophysicsofnotch pages 1-3, shi2024notchsignalingpathway pages 1-2, sprinzak2021biophysicsofnotch pages 7-9) |
| Ligand-activation machinery | MIB1; epsin and clathrin-dependent endocytic machinery | Mind bomb, Neuralized, epsin | Orthologous endocytic regulators | Ligand ubiquitylation recruits endocytic machinery in the sender cell. Internalization supplies tensile force that opens the receptor negative regulatory region, exposes S2, and trans-endocytoses the ligand-bound Notch extracellular domain. This machinery is mechanistically essential but accessory to the minimal receptor-to-nucleus trunk. (reichrath2020notchsignalingand pages 51-53, sprinzak2021biophysicsofnotch pages 11-13, lv2024evolutionandfunction pages 2-4) |
| S1 maturation protease | Furin-like proprotein convertases | Furin-like convertase | Furin-like convertase | Constitutive cleavage in the trans-Golgi produces extracellular and transmembrane–intracellular subunits that usually remain noncovalently associated as the mature heterodimer. S1 is a receptor-maturation event, not the ligand-triggered activating cleavage. (sachan2023notchsignallingmultifaceted pages 2-2, sen2023theintricatenotch pages 2-4, sprinzak2021biophysicsofnotch pages 7-9) |
| S2 ectodomain sheddase | ADAM10 physiologically; ADAM17/TACE mainly under ligand-independent or experimentally destabilized conditions | Kuzbanian | SUP-17/ADM-4-related ADAM proteases | After force-dependent opening of the negative regulatory region, an ADAM protease cleaves the membrane-proximal S2 site. This removes the extracellular domain and creates the membrane-tethered NEXT substrate. Evidence with endogenous NOTCH1 supports ADAM10 as the principal ligand-dependent sheddase and cautions against treating ADAM17 as universally equivalent. (alabi2021analysisofthe pages 2-3, alabi2021analysisofthe pages 3-5, alabi2021analysisofthe pages 10-11) |
| Intramembrane protease | γ-Secretase complex: presenilin catalytic subunit, nicastrin, APH1, and PEN2 | Presenilin, Nicastrin, Aph-1, Pen-2 | SEL-12/HOP-1, APH-2, APH-1, PEN-2 | γ-Secretase cleaves NEXT within the transmembrane region at S3 and related sites, releasing NICD. This cleavage is obligatory for the conventional nuclear canonical pathway, although its precise subcellular location can vary between plasma-membrane and endosomal compartments. (lv2024evolutionandfunction pages 2-4, sprinzak2021biophysicsofnotch pages 7-9, hounjet2021theroleof pages 13-14) |
| Released intracellular effector | N1ICD–N4ICD | Notch intracellular domain | LIN-12 or GLP-1 intracellular domain | NICD carries the receptor signal to the nucleus without a conventional second-messenger cascade. Its RAM region binds CSL, ankyrin repeats help assemble the activation complex, and its PEST region supports phosphorylation-dependent turnover and signal termination. (wang2024mechanismofnotch pages 3-5, hall2022thestructurebinding pages 1-2, sprinzak2021biophysicsofnotch pages 16-18) |
| CSL-family DNA-binding factor | RBPJ, also called CBF1 or RBP-Jκ | Suppressor of Hairless, Su(H) | LAG-1 | CSL is the conserved DNA-binding platform. Without NICD it can recruit corepressors; NICD binding displaces or counteracts repression and creates an activation surface. “CSL” derives from CBF1/Su(H)/LAG-1 and should not be mistaken for three mammalian proteins. (lv2024evolutionandfunction pages 2-4, giaimo2021transcriptionfactorrbpj pages 1-3, giaimo2021transcriptionfactorrbpj pages 3-5) |
| Mastermind coactivator | MAML1, MAML2, MAML3 | Mastermind, Mam | LAG-3 | MAML binds a composite interface formed by NICD ankyrin repeats and CSL, stabilizing the ternary NICD–CSL–MAML complex. It supports recruitment of Mediator and histone acetyltransferases such as p300/CBP; it is obligatory for the standard canonical transcriptional switch. (hall2022thestructurebinding pages 1-2, sprinzak2021biophysicsofnotch pages 13-14, friedrich2023decipheringthenotch pages 23-27) |
| Basal corepressors and recruited coactivators | SHARP/SPEN, FHL1 and HDAC-associated repressors; p300/CBP, PCAF/GCN5 and Mediator as coactivators | Hairless and associated repressors; chromatin coactivators after NICD–Mam assembly | LAG-1-associated repressors and coactivators | These proteins establish the repressed versus activated chromatin states surrounding CSL. They shape response strength and target selection but are not pathway-specific signal carriers in the same sense as receptor, NICD, CSL, and MAML. (sprinzak2021biophysicsofnotch pages 1-3, hall2022thestructurebinding pages 1-2, giaimo2021transcriptionfactorrbpj pages 3-5) |
| Primary canonical targets | HES1, HES4, HES5, HES7 and context-dependent HEY1, HEY2, HEYL; additional direct targets vary by cell type | Enhancer of split complex, E(spl)-C, and related Hairy/E(spl) genes | *hes*-related targets, including *ref-1* family genes in defined contexts | The most conserved immediate outputs encode bHLH transcriptional repressors of the HES/E(spl) and HEY families. They repress lineage-promoting transcription factors and mediate lateral inhibition, progenitor maintenance, boundary formation, and oscillatory programs. HES/HEY induction is a canonical readout, but no single member is universal in every tissue. (reichrath2020notchsignalingand pages 51-53, lv2024evolutionandfunction pages 2-4, pan2021transcriptionfactorrbpjl pages 1-2) |


*Table: Core receptors, DSL ligands, proteases, nuclear effectors, and primary transcriptional targets are compared across mammals, Drosophila, and C. elegans. The table distinguishes obligatory pathway components from maturation and regulatory machinery.*

### Receptors and Ligands

Notch receptors are approximately 300 kDa type I transmembrane proteins with an extracellular region containing tandem EGF-like repeats (36 in mammalian NOTCH1) and three Lin-12/Notch repeats that form the negative regulatory region (NRR) (wang2024mechanismofnotch pages 3-5, sprinzak2021biophysicsofnotch pages 7-9). Mammals express four receptors (NOTCH1–4), Drosophila expresses a single Notch gene, and C. elegans has LIN-12 and GLP-1 paralogs (lv2024evolutionandfunction pages 1-2, he2021comparativeandevolutionary pages 1-2).

Canonical ligands belong to the DSL (Delta/Serrate/LAG-2) family, characterized by an N-terminal C2/MNNL domain, DSL domain, and EGF-like repeats (wang2024mechanismofnotch pages 3-5, sprinzak2021biophysicsofnotch pages 1-3). Mammals express five family members: DLL1, DLL4, JAG1, and JAG2 function as productive trans-activators, while DLL3 lacks a critical functional DSL domain and primarily exerts cis-inhibitory effects (sprinzak2021biophysicsofnotch pages 1-3, sen2023theintricatenotch pages 4-5). Drosophila utilizes Delta and Serrate, with functional distinctions linked to differential glycosylation and Fringe-dependent modulation (reichrath2020notchsignalingand pages 51-53).

### Proteolytic Processing Machinery

**Furin-like convertases** perform constitutive S1 cleavage during receptor maturation in the Golgi, generating the non-covalently associated heterodimer but leaving the receptor in an autoinhibited state (sen2023theintricatenotch pages 2-4, sprinzak2021biophysicsofnotch pages 7-9).

**ADAM metalloproteases** catalyze the activation-associated S2 cleavage. ADAM10 is the principal physiological sheddase for ligand-dependent NOTCH1 processing, while ADAM17/TACE contributes more prominently to ligand-independent or experimentally induced activation (alabi2021analysisofthe pages 2-3, alabi2021analysisofthe pages 3-5, zack2024anothernotchin pages 26-28). Evidence from Adam10-deficient cells demonstrates that physiological Delta-like 4-stimulated Notch1 processing requires ADAM10 and cannot be rescued by ADAM17 or other ADAMs (alabi2021analysisofthe pages 2-3, alabi2021analysisofthe pages 10-11).

**γ-Secretase complex** comprises presenilin (the catalytic subunit with two aspartate residues in the active site), nicastrin, APH1, and PEN2 (lv2024evolutionandfunction pages 2-4, sen2023theintricatenotch pages 8-9). This intramembrane protease cleaves NEXT at S3 and additional sites, releasing NICD (sprinzak2021biophysicsofnotch pages 7-9, hounjet2021theroleof pages 13-14).

### Nuclear Transcriptional Machinery

**RBPJ/CSL** (recombination signal binding protein for immunoglobulin kappa J region, also called CSL for CBF1/Su(H)/LAG-1) is the evolutionarily conserved DNA-binding transcription factor that serves as the central platform for both repression and activation (lv2024evolutionandfunction pages 2-4, giaimo2021transcriptionfactorrbpj pages 1-3, giaimo2021transcriptionfactorrbpj pages 3-5). It binds the consensus sequence GTGGGAA at Notch-responsive elements (pan2021transcriptionfactorrbpjl pages 1-2).

**MAML/Mastermind proteins** (MAML1–3 in mammals, Mastermind in flies, LAG-3 in worms) function as essential transcriptional coactivators. The N-terminal helix of MAML binds a composite interface formed by the NICD ankyrin-repeat domain and RBPJ, stabilizing the ternary complex and recruiting additional coactivators including p300/CBP histone acetyltransferases and Mediator (hall2022thestructurebinding pages 1-2, sprinzak2021biophysicsofnotch pages 13-14, friedrich2023decipheringthenotch pages 23-27).

**Corepressors and coactivators** establish context. In the absence of NICD, RBPJ recruits corepressors such as SHARP/SPEN (mammals) or Hairless (Drosophila) along with histone deacetylases, maintaining target genes in a repressed state (sprinzak2021biophysicsofnotch pages 1-3, sprinzak2021biophysicsofnotch pages 13-14). NICD-MAML assembly displaces these complexes and recruits p300/CBP, PCAF/GCN5, and chromatin remodelers, creating transcriptionally permissive chromatin (friedrich2023decipheringthenotch pages 23-27, giaimo2021transcriptionfactorrbpj pages 3-5).

### Primary Target Genes

The most conserved direct transcriptional outputs encode basic helix-loop-helix (bHLH) transcriptional repressors of the HES/E(spl) and HEY families (lv2024evolutionandfunction pages 2-4, reichrath2020notchsignalingand pages 134-138, pan2021transcriptionfactorrbpjl pages 1-2). In mammals, these include HES1, HES4, HES5, HES7, HEY1, HEY2, and HEYL; in Drosophila, the Enhancer of split complex [E(spl)-C] contains seven bHLH genes (reichrath2020notchsignalingand pages 51-53). These repressors mediate lateral inhibition by suppressing proneural and lineage-promoting transcription factors, thereby controlling binary cell-fate decisions, maintaining progenitor states, establishing boundaries, and generating oscillatory gene-expression patterns (lv2024evolutionandfunction pages 2-4, pan2021transcriptionfactorrbpjl pages 1-2).

Additional direct targets vary by cellular context and include c-MYC, cyclins, p21, NF-κB, SOX2, and negative feedback regulators such as NRARP and Deltex (wang2024mechanismofnotch pages 3-5, pan2021transcriptionfactorrbpjl pages 1-2, giaimo2021transcriptionfactorrbpj pages 1-3).

## Evolutionary and Cell-Biological Variation

### Conservation and Origin

The Notch pathway represents an ancient metazoan innovation, with core components present from sponges and cnidarians through bilaterians to vertebrates (he2021comparativeandevolutionary pages 9-10, he2021comparativeandevolutionary pages 1-2, stein2024anorthologicsstudy pages 6-9). The pathway likely originated before or at the base of Metazoa: choanoflagellates, the closest unicellular relatives of animals, possess EGF, LNR, and ankyrin-repeat domains along with presenilin, although Delta ligands have not been identified (lv2024evolutionandfunction pages 14-15). This suggests that Notch-related protein modules predated multicellularity and were co-opted for cell-cell communication in early animals.

**Sponges** (Porifera), which lack neurons and organized tissues, retain Notch receptors, Delta ligands, CSL/Su(H) transcription factors, and the ADAM/γ-secretase proteolytic machinery, indicating that the pathway evolved before nervous system emergence (lv2024evolutionandfunction pages 6-8, lv2024evolutionandfunction pages 14-15). In Amphimedon queenslandica, multiple Delta ligands (AmDelta1–5), Notch, and bHLH transcriptional regulators are expressed during embryonic and larval development (lv2024evolutionandfunction pages 14-15).

**Cnidarians** possess nearly complete Notch pathway repertoires including Jagged/Delta ligands, Notch receptors, Su(H), presenilin/pen-2, and Hes genes (lv2024evolutionandfunction pages 14-15, lv2024evolutionandfunction pages 15-16). In Hydra and Nematostella vectensis, Notch regulates head regeneration, boundary formation, gastrulation, tissue organization, cnidocyte development, and neurogenesis (lv2024evolutionandfunction pages 15-16). By the cnidarian stage, approximately half of the human Notch-system proteins had evolved (stein2024anorthologicsstudy pages 6-9).

**Conservation from invertebrates to vertebrates** is evident in both molecular architecture and functional logic. Drosophila and mammalian systems share the core receptor-cleavage-transcription sequence, although Drosophila typically employs a single Notch receptor and two ligands (Delta and Serrate) compared to four receptors and five ligands in mammals (lv2024evolutionandfunction pages 1-2, reichrath2020notchsignalingand pages 48-51). The pathway regulates lateral inhibition, neurogenesis, boundary formation, somitogenesis, and progenitor maintenance across phyla (he2021comparativeandevolutionary pages 9-10, reichrath2020notchsignalingand pages 48-51).

### Lineage-Specific Elaborations

Vertebrate evolution involved expansion of receptor and ligand families through gene duplication, enabling paralog-specific expression patterns and functional specialization (lv2024evolutionandfunction pages 1-2, he2021comparativeandevolutionary pages 1-2). Lophotrochozoans similarly exhibit duplications of Delta and Hes/Hey-related genes with divergent expression patterns (he2021comparativeandevolutionary pages 1-2). Even evolutionarily conservative components such as Notch, Presenilin, and Su(H) display functional diversification beyond simple retention of ancestral roles (he2021comparativeandevolutionary pages 9-10, he2021comparativeandevolutionary pages 1-2).

### Cell-Type and Tissue-Specific Variation

Notch signaling produces dramatically different outcomes depending on cellular context (zhou2022notchsignalingpathway pages 21-22, sachan2023notchsignallingmultifaceted pages 18-18). In neural progenitors, it maintains stem-like properties and prevents premature differentiation; in lymphocytes, it specifies T-cell versus B-cell fate; in vasculature, it regulates tip versus stalk endothelial cell identity; in skin, it controls differentiation of keratinocytes (reichrath2020notchsignalingand pages 48-51). These context-dependent outputs reflect differences in: (1) which receptor and ligand paralogs are expressed, (2) which cofactors and chromatin regulators are available, (3) which RBPJ binding sites are accessible, and (4) which target-gene promoters can respond to activation (friedrich2023decipheringthenotch pages 23-27, sachan2023notchsignallingmultifaceted pages 18-18).

Comprehensive target-gene identification reveals that Notch-responsive gene sets vary substantially among cell types, and many genes with RBPJ binding sites do not respond to Notch perturbation, emphasizing the importance of tissue-specific chromatin context and additional transcription factors (friedrich2023decipheringthenotch pages 23-27).

## Constraints, Dependencies, and Failure Modes

### Obligatory Sequential Order

The canonical pathway imposes a strict temporal sequence. **S1 cleavage must precede S2/S3 cleavages**: furin-dependent receptor maturation is required for surface expression, but constitutive S1 processing alone does not activate signaling (sen2023theintricatenotch pages 2-4, sprinzak2021biophysicsofnotch pages 7-9). **S2 must precede S3**: ADAM cleavage removes the extracellular domain and creates the NEXT substrate for γ-secretase; γ-secretase cannot access the S3 site while the NRR and ectodomain remain intact (sprinzak2021biophysicsofnotch pages 7-9, sprinzak2021biophysicsofnotch pages 9-11). **NICD release must precede transcriptional activation**: the nuclear NICD–RBPJ–MAML complex cannot form until NICD is liberated from the membrane (lv2024evolutionandfunction pages 2-4).

### Mechanical and Spatial Constraints

**Force-dependent activation** couples ligand endocytosis to receptor conformational change: ligand binding alone is insufficient without the pulling force that opens the NRR and exposes S2 (sprinzak2021biophysicsofnotch pages 11-13, lv2024evolutionandfunction pages 2-4, sprinzak2021biophysicsofnotch pages 1-3). Optical trap measurements estimate Notch1–Dll1 rupture forces around 19 pN, while endocytic forces are approximately 2–5 pN, sufficient to destabilize the NRR if sustained (sprinzak2021biophysicsofnotch pages 11-13). Soluble ligands or ligands lacking cytoplasmic tails cannot generate productive force and act as dominant-negative inhibitors (sprinzak2021biophysicsofnotch pages 11-13).

**Trans versus cis configuration** determines signaling outcome: trans interactions between cells activate, while cis interactions on the same cell typically inhibit by sequestering receptors or preventing force transmission (sprinzak2021biophysicsofnotch pages 7-9, sprinzak2021biophysicsofnotch pages 9-11). DLL3, which lacks critical DSL-domain residues, functions almost exclusively as a cis-inhibitor rather than trans-activator (sen2023theintricatenotch pages 4-5).

**Compartment-specific cleavage** can vary: γ-secretase-mediated S3 cleavage may occur at the plasma membrane, in early endosomes, or in late endosomal/lysosomal compartments depending on receptor trafficking and cellular context (hounjet2021theroleof pages 13-14). Aberrant trafficking can redirect Notch to degradative compartments, preventing NICD release and nuclear signaling (hounjet2021theroleof pages 13-14).

### Substrate and Pathway Specificity

**ADAM protease specificity** shows ligand-dependence: physiological ligand-triggered NOTCH1 activation requires ADAM10, whereas ADAM17 cleaves Notch primarily under ligand-independent or experimentally destabilized conditions such as EDTA treatment (alabi2021analysisofthe pages 2-3, alabi2021analysisofthe pages 3-5). The Notch S2 site contains a valine at P1′, matching ADAM17 substrate preference, yet in vivo evidence with endogenous Notch1 demonstrates selective ADAM10 dependence during Delta-like 4 stimulation (alabi2021analysisofthe pages 10-11).

**CSL/RBPJ binding does not guarantee transcriptional response**: many promoter-bound RBPJ sites fail to activate upon Notch stimulation, indicating that RBPJ occupancy is necessary but not sufficient and that additional chromatin, enhancer, or cofactor requirements determine responsiveness (friedrich2023decipheringthenotch pages 23-27).

### Failure Modes

Pathway dysfunction arises from multiple mechanisms: (1) **loss-of-function mutations** in receptors, ligands, or processing enzymes prevent signal transmission and cause developmental disorders; (2) **gain-of-function NRR mutations** or FBXW7 E3 ligase loss stabilize NICD, producing ligand-independent activation seen in T-cell acute lymphoblastic leukemia (sprinzak2021biophysicsofnotch pages 16-18); (3) **ligand-independent activation** through aberrant endosomal trafficking or receptor mutations bypasses normal regulatory checkpoints (zack2024anothernotchin pages 5-10); (4) **cis-inhibition** by overexpressed ligands or mislocalized receptors sequesters pathway components and blocks trans-activation (sprinzak2021biophysicsofnotch pages 7-9, sprinzak2021biophysicsofnotch pages 9-11).

## Controversies and Open Questions

### Mechanistic Uncertainties

**RBPJ binding dynamics** remain contentious. The canonical model proposes constitutive DNA binding regardless of pathway activity, with NICD recruitment converting repression to activation (friedrich2023decipheringthenotch pages 23-27). However, alternative evidence suggests activity-dependent RBPJ loading, differential residence times, and assisted complex assembly, raising questions about whether RBPJ remains stably bound or dynamically exchanges (friedrich2023decipheringthenotch pages 23-27). Human genome-wide studies reveal RBPJ site heterogeneity: some sites maintain similar occupancy regardless of Notch activity, while others show increased binding during activation (friedrich2023decipheringthenotch pages 23-27).

**Transcriptional burst regulation** links NICD concentration to stochastic gene activation, but the relationship between burst frequency, burst size, and overall output is incompletely understood (sprinzak2021biophysicsofnotch pages 16-18). How cells establish NICD response thresholds, how cooperative SPS (sequence-paired site) binding modulates bursts, and how other transcription factors alter thresholds remain active areas of investigation (sprinzak2021biophysicsofnotch pages 16-18).

**Non-canonical pathway definition and integration** pose major challenges. While canonical signaling is well-defined by NICD–RBPJ–MAML-dependent transcription, non-canonical mechanisms encompass diverse phenomena including ligand-independent activation, RBPJ-independent NICD functions, and membrane-tethered Notch signaling prior to S3 cleavage (zack2024anothernotchin pages 5-10, gratton2020pleiotropicroleof pages 5-7). The molecular mechanisms, physiological relevance, and integration with canonical signaling remain incompletely characterized (gratton2020pleiotropicroleof pages 5-7).

### Context-Dependence and Predictability

**Why Notch produces different outcomes in different contexts** represents a fundamental unresolved question (sachan2023notchsignallingmultifaceted pages 18-18). Systematic mapping of receptor, ligand, and pathway-component expression across tissues, combined with spatially resolved transcriptomics, is needed to clarify how cellular location, tissue architecture, and local cofactor availability shape outputs (zhou2022notchsignalingpathway pages 21-22, sachan2023notchsignallingmultifaceted pages 18-18).

**Ligand-specific functions** remain poorly understood. Different ligands produce distinct outcomes even within the same tissue, yet the molecular basis for these differences—particularly regulation at the ligand-receptor interaction level—is incompletely defined (sachan2023notchsignallingmultifaceted pages 18-18). DLL1 versus JAG1/2 engagement can produce opposing immune-regulatory effects, but the structural and biochemical determinants are not fully resolved (zhou2022notchsignalingpathway pages 21-22).

**Target-gene selection** varies dramatically among cell types. Beyond the canonical HES/HEY families, which genes respond to Notch depends on chromatin accessibility, enhancer architecture, methylation state, and interactions with other signaling pathways (friedrich2023decipheringthenotch pages 23-27, sachan2023notchsignallingmultifaceted pages 18-18). A comprehensive understanding of these combinatorial rules remains elusive.

### Therapeutic and Translational Challenges

**Clinical targeting** of Notch has proven difficult. Pan-NOTCH γ-secretase inhibitors cause substantial gastrointestinal toxicity due to on-target effects in intestinal stem cells, limiting therapeutic windows (zhou2022notchsignalingpathway pages 21-22). Antibody-drug conjugates and receptor-specific antibodies have shown modest efficacy, with resistance emerging through cell heterogeneity, insufficient affinity, and bypass pathway activation (zhou2022notchsignalingpathway pages 21-22). The field requires improved predictive biomarkers and more selective, isoform- or ligand-specific interventions.

**Dual oncogenic and tumor-suppressive roles** create therapeutic complexity. Notch can promote or inhibit tumor development depending on cancer type, genetic context, and microenvironment, making it unclear which conditions favor pathway activation versus inhibition as treatment strategy (zhou2022notchsignalingpathway pages 21-22, wang2024mechanismofnotch pages 3-5).

## Key References

The following primary literature and authoritative reviews provide detailed mechanistic, structural, evolutionary, and functional foundations:

**Comprehensive reviews:**
- Shi et al. (2024). Notch signaling pathway in cancer: from mechanistic insights to targeted therapies. Signal Transduction and Targeted Therapy 9:1828 (shi2024notchsignalingpathway pages 1-2)
- Zhou et al. (2022). Notch signaling pathway: architecture, disease, and therapeutics. Signal Transduction and Targeted Therapy 7:934 (zhou2022notchsignalingpathway pages 21-22)
- Sprinzak & Blacklow (2021). Biophysics of Notch Signaling. Annual Review of Biophysics 50:157-189 (sprinzak2021biophysicsofnotch pages 1-3, sprinzak2021biophysicsofnotch pages 7-9, sprinzak2021biophysicsofnotch pages 11-13)
- Sachan et al. (2024). Notch signalling: multifaceted role in development and disease. The FEBS Journal 291:3030-3059 (sachan2023notchsignallingmultifaceted pages 18-18)

**Molecular mechanisms:**
- Wang et al. (2024). Mechanism of Notch Signaling Pathway in Malignant Progression of Glioblastoma and Targeted Therapy. Biomolecules 14:480 (wang2024mechanismofnotch pages 3-5)
- Martin et al. (2023). A spatiotemporal Notch interaction map from plasma membrane to nucleus. Science Signaling 16:eadg6474
- Alabi et al. (2021). Analysis of the Conditions That Affect the Selective Processing of Endogenous Notch1 by ADAM10 and ADAM17. International Journal of Molecular Sciences 22:1846 (alabi2021analysisofthe pages 2-3, alabi2021analysisofthe pages 3-5)

**Structural biology:**
- Hall et al. (2022). The structure, binding and function of a Notch transcription complex involving RBPJ and the epigenetic reader protein L3MBTL3. Nucleic Acids Research 50:13083-13099 (hall2022thestructurebinding pages 1-2)
- Giaimo et al. (2021). Transcription Factor RBPJ as a Molecular Switch in Regulating the Notch Response. Advances in Experimental Medicine and Biology 1287:9-30 (giaimo2021transcriptionfactorrbpj pages 1-3, giaimo2021transcriptionfactorrbpj pages 3-5)

**Evolutionary and comparative biology:**
- Lv et al. (2024). Evolution and Function of the Notch Signaling Pathway: An Invertebrate Perspective. International Journal of Molecular Sciences 25:3322 (lv2024evolutionandfunction pages 1-2, lv2024evolutionandfunction pages 6-8, lv2024evolutionandfunction pages 14-15)
- Stein (2024). An Orthologics Study of the Notch Signaling Pathway. Genes 15:1452 (stein2024anorthologicsstudy pages 6-9)
- He et al. (2021). Comparative and evolutionary analyses reveal conservation and divergence of the notch pathway in lophotrochozoa. Scientific Reports 11:10800 (he2021comparativeandevolutionary pages 9-10, he2021comparativeandevolutionary pages 1-2)

**Canonical versus non-canonical signaling:**
- Zack et al. (2024). Another Notch in the Belt of Rheumatoid Arthritis. Arthritis & Rheumatology (zack2024anothernotchin pages 5-10)
- Gratton et al. (2020). Pleiotropic Role of Notch Signaling in Human Skin Diseases. International Journal of Molecular Sciences 21:4214 (gratton2020pleiotropicroleof pages 5-7)

This comprehensive review synthesizes current understanding of the canonical Notch pathway while highlighting critical unresolved questions. The pathway's elegant simplicity—direct cell contact triggering proteolytic release and nuclear translocation—belies profound context-dependence and regulatory sophistication that continue to challenge investigators across developmental biology, cancer research, and therapeutic development.

References

1. (lv2024evolutionandfunction pages 1-2): Yan Lv, Xuan Pang, Zhonghong Cao, Changping Song, Baohua Liu, Weiwei Wu, and Qiuxiang Pang. Evolution and function of the notch signaling pathway: an invertebrate perspective. International Journal of Molecular Sciences, 25:3322, Mar 2024. URL: https://doi.org/10.3390/ijms25063322, doi:10.3390/ijms25063322. This article has 36 citations.

2. (he2021comparativeandevolutionary pages 1-2): Xinyu He, Fucun Wu, Linlin Zhang, Li Li, and Guofan Zhang. Comparative and evolutionary analyses reveal conservation and divergence of the notch pathway in lophotrochozoa. Scientific Reports, May 2021. URL: https://doi.org/10.1038/s41598-021-90800-8, doi:10.1038/s41598-021-90800-8. This article has 8 citations and is from a peer-reviewed journal.

3. (sprinzak2021biophysicsofnotch pages 1-3): David Sprinzak and Stephen C. Blacklow. Biophysics of notch signaling. Annual Review of Biophysics, 50:157-189, May 2021. URL: https://doi.org/10.1146/annurev-biophys-101920-082204, doi:10.1146/annurev-biophys-101920-082204. This article has 280 citations and is from a domain leading peer-reviewed journal.

4. (lv2024evolutionandfunction pages 2-4): Yan Lv, Xuan Pang, Zhonghong Cao, Changping Song, Baohua Liu, Weiwei Wu, and Qiuxiang Pang. Evolution and function of the notch signaling pathway: an invertebrate perspective. International Journal of Molecular Sciences, 25:3322, Mar 2024. URL: https://doi.org/10.3390/ijms25063322, doi:10.3390/ijms25063322. This article has 36 citations.

5. (zack2024anothernotchin pages 5-10): Stephanie R. Zack, Osama Alzoubi, Neha Satoeya, Kunwar P. Singh, Sania Deen, Wes Nijim, Myles J. Lewis, Costantino Pitzalis, Nadera Sweiss, Lionel B. Ivashkiv, and Shiva Shahrara. Another notch in the belt of rheumatoid arthritis. Aug 2024. URL: https://doi.org/10.1002/art.42937, doi:10.1002/art.42937. This article has 26 citations and is from a highest quality peer-reviewed journal.

6. (guo2023notchsignalinghypoxia pages 1-2): Mingzhou Guo, Yang Niu, Min Xie, Xiansheng Liu, and Xiaochen Li. Notch signaling, hypoxia, and cancer. Frontiers in Oncology, Jan 2023. URL: https://doi.org/10.3389/fonc.2023.1078768, doi:10.3389/fonc.2023.1078768. This article has 65 citations.

7. (he2021comparativeandevolutionary pages 9-10): Xinyu He, Fucun Wu, Linlin Zhang, Li Li, and Guofan Zhang. Comparative and evolutionary analyses reveal conservation and divergence of the notch pathway in lophotrochozoa. Scientific Reports, May 2021. URL: https://doi.org/10.1038/s41598-021-90800-8, doi:10.1038/s41598-021-90800-8. This article has 8 citations and is from a peer-reviewed journal.

8. (zhou2022notchsignalingpathway pages 21-22): Binghan Zhou, Wan-Ying Lin, Yaling Long, Yunkai Yang, Huan Zhang, Kongming Wu, and Q. Chu. Notch signaling pathway: architecture, disease, and therapeutics. Signal Transduction and Targeted Therapy, Mar 2022. URL: https://doi.org/10.1038/s41392-022-00934-y, doi:10.1038/s41392-022-00934-y. This article has 1461 citations and is from a peer-reviewed journal.

9. (sachan2023notchsignallingmultifaceted pages 18-18): Nalani Sachan, Vartika Sharma, Mousumi Mutsuddi, and Ashim Mukherjee. Notch signalling: multifaceted role in development and disease. The FEBS Journal, 291:3030-3059, May 2024. URL: https://doi.org/10.1111/febs.16815, doi:10.1111/febs.16815. This article has 124 citations.

10. (wang2024mechanismofnotch pages 3-5): Shenghao Wang, Sikuan Gu, Junfan Chen, Zhiqiang Yuan, Ping Liang, and Hongjuan Cui. Mechanism of notch signaling pathway in malignant progression of glioblastoma and targeted therapy. Biomolecules, 14:480, Apr 2024. URL: https://doi.org/10.3390/biom14040480, doi:10.3390/biom14040480. This article has 25 citations.

11. (gratton2020pleiotropicroleof pages 5-7): Rossella Gratton, Paola Maura Tricarico, Chiara Moltrasio, Ana Sofia Lima Estevão de Oliveira, Lucas Brandão, Angelo Valerio Marzano, Luisa Zupin, and Sergio Crovella. Pleiotropic role of notch signaling in human skin diseases. Jun 2020. URL: https://doi.org/10.3390/ijms21124214, doi:10.3390/ijms21124214. This article has 62 citations.

12. (sen2023theintricatenotch pages 4-5): Plaboni Sen and Siddhartha Sankar Ghosh. The intricate notch signaling dynamics in therapeutic realms of cancer. ACS pharmacology & translational science, 6 5:651-670, May 2023. URL: https://doi.org/10.1021/acsptsci.2c00239, doi:10.1021/acsptsci.2c00239. This article has 26 citations and is from a peer-reviewed journal.

13. (sen2023theintricatenotch pages 2-4): Plaboni Sen and Siddhartha Sankar Ghosh. The intricate notch signaling dynamics in therapeutic realms of cancer. ACS pharmacology & translational science, 6 5:651-670, May 2023. URL: https://doi.org/10.1021/acsptsci.2c00239, doi:10.1021/acsptsci.2c00239. This article has 26 citations and is from a peer-reviewed journal.

14. (sprinzak2021biophysicsofnotch pages 7-9): David Sprinzak and Stephen C. Blacklow. Biophysics of notch signaling. Annual Review of Biophysics, 50:157-189, May 2021. URL: https://doi.org/10.1146/annurev-biophys-101920-082204, doi:10.1146/annurev-biophys-101920-082204. This article has 280 citations and is from a domain leading peer-reviewed journal.

15. (reichrath2020notchsignalingand pages 51-53): Jörg Reichrath and Sandra Reichrath. Notch signaling and embryonic development: an ancient friend, revisited. Advances in experimental medicine and biology, 1218:9-37, Jan 2020. URL: https://doi.org/10.1007/978-3-030-34436-8\_2, doi:10.1007/978-3-030-34436-8\_2. This article has 36 citations and is from a peer-reviewed journal.

16. (sprinzak2021biophysicsofnotch pages 11-13): David Sprinzak and Stephen C. Blacklow. Biophysics of notch signaling. Annual Review of Biophysics, 50:157-189, May 2021. URL: https://doi.org/10.1146/annurev-biophys-101920-082204, doi:10.1146/annurev-biophys-101920-082204. This article has 280 citations and is from a domain leading peer-reviewed journal.

17. (sprinzak2021biophysicsofnotch pages 9-11): David Sprinzak and Stephen C. Blacklow. Biophysics of notch signaling. Annual Review of Biophysics, 50:157-189, May 2021. URL: https://doi.org/10.1146/annurev-biophys-101920-082204, doi:10.1146/annurev-biophys-101920-082204. This article has 280 citations and is from a domain leading peer-reviewed journal.

18. (friedrich2023decipheringthenotch pages 23-27): Deciphering the Notch Pathway: A Bioinformatics Analysis of the RBPJ/Notch Axis This article has 0 citations.

19. (sprinzak2021biophysicsofnotch pages 26-30): David Sprinzak and Stephen C. Blacklow. Biophysics of notch signaling. Annual Review of Biophysics, 50:157-189, May 2021. URL: https://doi.org/10.1146/annurev-biophys-101920-082204, doi:10.1146/annurev-biophys-101920-082204. This article has 280 citations and is from a domain leading peer-reviewed journal.

20. (alabi2021analysisofthe pages 2-3): Rolake O. Alabi, Jose Lora, Arda B. Celen, Thorsten Maretzky, and Carl P. Blobel. Analysis of the conditions that affect the selective processing of endogenous notch1 by adam10 and adam17. International Journal of Molecular Sciences, 22:1846, Feb 2021. URL: https://doi.org/10.3390/ijms22041846, doi:10.3390/ijms22041846. This article has 30 citations.

21. (alabi2021analysisofthe pages 3-5): Rolake O. Alabi, Jose Lora, Arda B. Celen, Thorsten Maretzky, and Carl P. Blobel. Analysis of the conditions that affect the selective processing of endogenous notch1 by adam10 and adam17. International Journal of Molecular Sciences, 22:1846, Feb 2021. URL: https://doi.org/10.3390/ijms22041846, doi:10.3390/ijms22041846. This article has 30 citations.

22. (alabi2021analysisofthe pages 10-11): Rolake O. Alabi, Jose Lora, Arda B. Celen, Thorsten Maretzky, and Carl P. Blobel. Analysis of the conditions that affect the selective processing of endogenous notch1 by adam10 and adam17. International Journal of Molecular Sciences, 22:1846, Feb 2021. URL: https://doi.org/10.3390/ijms22041846, doi:10.3390/ijms22041846. This article has 30 citations.

23. (hounjet2021theroleof pages 13-14): Judith Hounjet and Marc Vooijs. The role of intracellular trafficking of notch receptors in ligand-independent notch activation. Biomolecules, 11:1369, Sep 2021. URL: https://doi.org/10.3390/biom11091369, doi:10.3390/biom11091369. This article has 36 citations.

24. (hall2022thestructurebinding pages 1-2): Daniel Hall, Benedetto Daniele Giaimo, Sung-Soo Park, Wiebke Hemmer, Tobias Friedrich, Francesca Ferrante, Marek Bartkuhn, Zhenyu Yuan, Franz Oswald, Tilman Borggrefe, Jean-François Rual, and Rhett A. Kovall. The structure, binding and function of a notch transcription complex involving rbpj and the epigenetic reader protein l3mbtl3. Nucleic Acids Research, 50:13083-13099, Feb 2022. URL: https://doi.org/10.1093/nar/gkac1137, doi:10.1093/nar/gkac1137. This article has 10 citations and is from a highest quality peer-reviewed journal.

25. (sprinzak2021biophysicsofnotch pages 13-14): David Sprinzak and Stephen C. Blacklow. Biophysics of notch signaling. Annual Review of Biophysics, 50:157-189, May 2021. URL: https://doi.org/10.1146/annurev-biophys-101920-082204, doi:10.1146/annurev-biophys-101920-082204. This article has 280 citations and is from a domain leading peer-reviewed journal.

26. (giaimo2021transcriptionfactorrbpj pages 3-5): Benedetto Daniele Giaimo, Ellen K. Gagliani, Rhett A. Kovall, and Tilman Borggrefe. Transcription factor rbpj as a molecular switch in regulating the notch response. Advances in experimental medicine and biology, 1287:9-30, Oct 2021. URL: https://doi.org/10.1007/978-3-030-55031-8\_2, doi:10.1007/978-3-030-55031-8\_2. This article has 56 citations and is from a peer-reviewed journal.

27. (sprinzak2021biophysicsofnotch pages 16-18): David Sprinzak and Stephen C. Blacklow. Biophysics of notch signaling. Annual Review of Biophysics, 50:157-189, May 2021. URL: https://doi.org/10.1146/annurev-biophys-101920-082204, doi:10.1146/annurev-biophys-101920-082204. This article has 280 citations and is from a domain leading peer-reviewed journal.

28. (shi2024notchsignalingpathway pages 1-2): Qingmiao Shi, Chen Xue, Yifan Zeng, Xin Yuan, Qingfei Chu, Shuwen Jiang, Jinzhi Wang, Yaqi Zhang, Danhua Zhu, and Lan-Ju Li. Notch signaling pathway in cancer: from mechanistic insights to targeted therapies. Signal Transduction and Targeted Therapy, May 2024. URL: https://doi.org/10.1038/s41392-024-01828-x, doi:10.1038/s41392-024-01828-x. This article has 513 citations and is from a peer-reviewed journal.

29. (sachan2023notchsignallingmultifaceted pages 2-2): Nalani Sachan, Vartika Sharma, Mousumi Mutsuddi, and Ashim Mukherjee. Notch signalling: multifaceted role in development and disease. The FEBS Journal, 291:3030-3059, May 2024. URL: https://doi.org/10.1111/febs.16815, doi:10.1111/febs.16815. This article has 124 citations.

30. (giaimo2021transcriptionfactorrbpj pages 1-3): Benedetto Daniele Giaimo, Ellen K. Gagliani, Rhett A. Kovall, and Tilman Borggrefe. Transcription factor rbpj as a molecular switch in regulating the notch response. Advances in experimental medicine and biology, 1287:9-30, Oct 2021. URL: https://doi.org/10.1007/978-3-030-55031-8\_2, doi:10.1007/978-3-030-55031-8\_2. This article has 56 citations and is from a peer-reviewed journal.

31. (pan2021transcriptionfactorrbpjl pages 1-2): Leiling Pan, Philipp Hoffmeister, Aleksandra Turkiewicz, N. N. Duyen Huynh, Andreas Große-Berkenbusch, Uwe Knippschild, J. Christof M. Gebhardt, Bernd Baumann, Tilman Borggrefe, and Franz Oswald. Transcription factor rbpjl is able to repress notch target gene expression but is non-responsive to notch activation. Oct 2021. URL: https://doi.org/10.18725/oparu-46089, doi:10.18725/oparu-46089. This article has 21 citations.

32. (zack2024anothernotchin pages 26-28): Stephanie R. Zack, Osama Alzoubi, Neha Satoeya, Kunwar P. Singh, Sania Deen, Wes Nijim, Myles J. Lewis, Costantino Pitzalis, Nadera Sweiss, Lionel B. Ivashkiv, and Shiva Shahrara. Another notch in the belt of rheumatoid arthritis. Aug 2024. URL: https://doi.org/10.1002/art.42937, doi:10.1002/art.42937. This article has 26 citations and is from a highest quality peer-reviewed journal.

33. (sen2023theintricatenotch pages 8-9): Plaboni Sen and Siddhartha Sankar Ghosh. The intricate notch signaling dynamics in therapeutic realms of cancer. ACS pharmacology & translational science, 6 5:651-670, May 2023. URL: https://doi.org/10.1021/acsptsci.2c00239, doi:10.1021/acsptsci.2c00239. This article has 26 citations and is from a peer-reviewed journal.

34. (reichrath2020notchsignalingand pages 134-138): Jörg Reichrath and Sandra Reichrath. Notch signaling and embryonic development: an ancient friend, revisited. Advances in experimental medicine and biology, 1218:9-37, Jan 2020. URL: https://doi.org/10.1007/978-3-030-34436-8\_2, doi:10.1007/978-3-030-34436-8\_2. This article has 36 citations and is from a peer-reviewed journal.

35. (stein2024anorthologicsstudy pages 6-9): Wilfred Donald Stein. An orthologics study of the notch signaling pathway. Genes, 15:1452, Nov 2024. URL: https://doi.org/10.3390/genes15111452, doi:10.3390/genes15111452. This article has 1 citations.

36. (lv2024evolutionandfunction pages 14-15): Yan Lv, Xuan Pang, Zhonghong Cao, Changping Song, Baohua Liu, Weiwei Wu, and Qiuxiang Pang. Evolution and function of the notch signaling pathway: an invertebrate perspective. International Journal of Molecular Sciences, 25:3322, Mar 2024. URL: https://doi.org/10.3390/ijms25063322, doi:10.3390/ijms25063322. This article has 36 citations.

37. (lv2024evolutionandfunction pages 6-8): Yan Lv, Xuan Pang, Zhonghong Cao, Changping Song, Baohua Liu, Weiwei Wu, and Qiuxiang Pang. Evolution and function of the notch signaling pathway: an invertebrate perspective. International Journal of Molecular Sciences, 25:3322, Mar 2024. URL: https://doi.org/10.3390/ijms25063322, doi:10.3390/ijms25063322. This article has 36 citations.

38. (lv2024evolutionandfunction pages 15-16): Yan Lv, Xuan Pang, Zhonghong Cao, Changping Song, Baohua Liu, Weiwei Wu, and Qiuxiang Pang. Evolution and function of the notch signaling pathway: an invertebrate perspective. International Journal of Molecular Sciences, 25:3322, Mar 2024. URL: https://doi.org/10.3390/ijms25063322, doi:10.3390/ijms25063322. This article has 36 citations.

39. (reichrath2020notchsignalingand pages 48-51): Jörg Reichrath and Sandra Reichrath. Notch signaling and embryonic development: an ancient friend, revisited. Advances in experimental medicine and biology, 1218:9-37, Jan 2020. URL: https://doi.org/10.1007/978-3-030-34436-8\_2, doi:10.1007/978-3-030-34436-8\_2. This article has 36 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](notch_signaling-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](notch_signaling-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. lv2024evolutionandfunction pages 2-4
2. sprinzak2021biophysicsofnotch pages 1-3
3. reichrath2020notchsignalingand pages 51-53
4. sprinzak2021biophysicsofnotch pages 7-9
5. hounjet2021theroleof pages 13-14
6. pan2021transcriptionfactorrbpjl pages 1-2
7. lv2024evolutionandfunction pages 14-15
8. lv2024evolutionandfunction pages 15-16
9. stein2024anorthologicsstudy pages 6-9
10. he2021comparativeandevolutionary pages 1-2
11. reichrath2020notchsignalingand pages 48-51
12. friedrich2023decipheringthenotch pages 23-27
13. sprinzak2021biophysicsofnotch pages 11-13
14. sen2023theintricatenotch pages 4-5
15. alabi2021analysisofthe pages 10-11
16. sprinzak2021biophysicsofnotch pages 16-18
17. zack2024anothernotchin pages 5-10
18. gratton2020pleiotropicroleof pages 5-7
19. sachan2023notchsignallingmultifaceted pages 18-18
20. zhou2022notchsignalingpathway pages 21-22
21. shi2024notchsignalingpathway pages 1-2
22. wang2024mechanismofnotch pages 3-5
23. hall2022thestructurebinding pages 1-2
24. lv2024evolutionandfunction pages 1-2
25. guo2023notchsignalinghypoxia pages 1-2
26. he2021comparativeandevolutionary pages 9-10
27. sen2023theintricatenotch pages 2-4
28. sprinzak2021biophysicsofnotch pages 9-11
29. sprinzak2021biophysicsofnotch pages 26-30
30. alabi2021analysisofthe pages 2-3
31. alabi2021analysisofthe pages 3-5
32. sprinzak2021biophysicsofnotch pages 13-14
33. giaimo2021transcriptionfactorrbpj pages 3-5
34. sachan2023notchsignallingmultifaceted pages 2-2
35. giaimo2021transcriptionfactorrbpj pages 1-3
36. zack2024anothernotchin pages 26-28
37. sen2023theintricatenotch pages 8-9
38. reichrath2020notchsignalingand pages 134-138
39. lv2024evolutionandfunction pages 6-8
40. E(spl)-C
41. https://doi.org/10.3390/ijms25063322,
42. https://doi.org/10.1038/s41598-021-90800-8,
43. https://doi.org/10.1146/annurev-biophys-101920-082204,
44. https://doi.org/10.1002/art.42937,
45. https://doi.org/10.3389/fonc.2023.1078768,
46. https://doi.org/10.1038/s41392-022-00934-y,
47. https://doi.org/10.1111/febs.16815,
48. https://doi.org/10.3390/biom14040480,
49. https://doi.org/10.3390/ijms21124214,
50. https://doi.org/10.1021/acsptsci.2c00239,
51. https://doi.org/10.1007/978-3-030-34436-8\_2,
52. https://doi.org/10.3390/ijms22041846,
53. https://doi.org/10.3390/biom11091369,
54. https://doi.org/10.1093/nar/gkac1137,
55. https://doi.org/10.1007/978-3-030-55031-8\_2,
56. https://doi.org/10.1038/s41392-024-01828-x,
57. https://doi.org/10.18725/oparu-46089,
58. https://doi.org/10.3390/genes15111452,