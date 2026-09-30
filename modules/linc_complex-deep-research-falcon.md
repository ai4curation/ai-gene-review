---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-27T17:04:54.145719'
end_time: '2026-09-27T17:22:03.273115'
duration_seconds: 1029.13
template_file: templates/module_research.md.j2
template_variables:
  module_title: LINC complex (SUN-KASH nuclear envelope bridge) module
  module_summary: 'The LINC (linker of nucleoskeleton and cytoskeleton) complex is
    a transmembrane bridge across the nuclear envelope. It connects the cytoskeleton
    to the nuclear interior. Inner-nuclear-membrane SUN-domain proteins form trimers
    whose C-terminal SUN domains project into the perinuclear space. Each trimer binds
    the C-terminal KASH peptides of three outer-nuclear-membrane KASH proteins, and
    the pair is reinforced by a conserved intermolecular disulfide. On the nucleoplasmic
    side, SUN proteins bind the nuclear lamina and, in meiosis, telomeres. On the
    cytoplasmic side, different KASH proteins engage different cytoskeletal systems:
    nesprin-1 and nesprin-2 bind actin through calponin-homology domains and bind
    microtubule motors (dynein-dynactin through BICD2, and kinesin-1); nesprin-3 binds
    plectin and so intermediate filaments; nesprin-4 binds kinesin-1; and the meiosis-specific
    KASH5 recruits dynein-dynactin. The bridge transmits force for nuclear migration
    and anchorage, centrosome-nucleus coupling, meiotic telomere-led chromosome movement,
    and sperm head-tail attachment. Disruption causes muscular dystrophy, cerebellar
    ataxia, hearing loss, infertility and neuronal migration defects.'
  module_outline: "- LINC complex\n  - 1. inner-nuclear-membrane SUN component binding\
    \ KASH peptides and the nucleoskeleton\n  - SUN inner-nuclear-membrane component\n\
    \    - Alternative versions by somatic vs germline SUN proteins: SUN paralog by\
    \ cell context\n      - Somatic SUN1/SUN2\n        - SUN1/SUN2 KASH-binding anchor\
    \ (molecular player: SUN-domain proteins (SUN1, SUN2); activity or role: cytoskeleton-nuclear\
    \ membrane anchor activity)\n        - SUN1/SUN2 nucleoplasmic lamina anchor (molecular\
    \ player: SUN-domain proteins (SUN1, SUN2); activity or role: lamin binding)\n\
    \      - Germline SUN5 at the sperm head-tail junction\n        - SUN5 sperm head-tail\
    \ anchor (molecular player: SUN5; activity or role: sperm head-to-tail anchoring\
    \ role)\n  - 2. outer-nuclear-membrane KASH component coupling the bridge to a\
    \ cytoskeletal system\n  - KASH outer-nuclear-membrane component\n    - Alternative\
    \ versions by cytoskeletal system engaged (actin and microtubule motors; intermediate\
    \ filaments; kinesin-1; meiotic dynein): KASH protein by cytoskeletal partner\n\
    \      - Nesprin-1/2 (actin and microtubule motors)\n        - Nesprin-1/2 cytoskeletal\
    \ anchor (molecular player: giant nesprins (nesprin-1, nesprin-2); activity or\
    \ role: cytoskeleton-nuclear membrane anchor activity)\n      - Nesprin-3 (plectin\
    \ and intermediate filaments)\n        - Nesprin-3 plectin anchor (molecular player:\
    \ SYNE3 (nesprin-3); activity or role: cytoskeleton-nuclear membrane anchor activity)\n\
    \      - Nesprin-4 (kinesin-1)\n        - Nesprin-4 kinesin-1 anchor (molecular\
    \ player: SYNE4 (nesprin-4); activity or role: cytoskeleton-nuclear membrane anchor\
    \ activity)\n      - KASH5 with SUN1 (meiotic telomere attachment)\n        -\
    \ KASH5 meiotic dynein anchor (molecular player: KASH5; activity or role: dynein\
    \ complex binding)\n  - 3. torsinA-dependent assembly of LINC complexes into force-bearing\
    \ TAN lines\n  - TorsinA regulation of LINC assembly\n    - TorsinA luminal AAA+\
    \ ATPase (molecular player: TOR1A (torsinA); activity or role: ATP hydrolysis\
    \ activity)"
  module_connections: '- SUN inner-nuclear-membrane component connects to KASH outer-nuclear-membrane
    component: SUN trimers bind KASH peptides in the perinuclear space and are required
    to keep KASH proteins in the outer nuclear membrane.

    - TorsinA regulation of LINC assembly promotes KASH outer-nuclear-membrane component:
    TorsinA with LAP1 promotes assembly of nesprin-2G/SUN2 TAN lines and the mobility
    of nesprin-2G within the nuclear envelope.'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 87
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: linc_complex-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Commissioned Review Brief

## Review Topic

LINC complex (SUN-KASH nuclear envelope bridge) module

## Working Scope

The LINC (linker of nucleoskeleton and cytoskeleton) complex is a transmembrane bridge across the nuclear envelope. It connects the cytoskeleton to the nuclear interior. Inner-nuclear-membrane SUN-domain proteins form trimers whose C-terminal SUN domains project into the perinuclear space. Each trimer binds the C-terminal KASH peptides of three outer-nuclear-membrane KASH proteins, and the pair is reinforced by a conserved intermolecular disulfide. On the nucleoplasmic side, SUN proteins bind the nuclear lamina and, in meiosis, telomeres. On the cytoplasmic side, different KASH proteins engage different cytoskeletal systems: nesprin-1 and nesprin-2 bind actin through calponin-homology domains and bind microtubule motors (dynein-dynactin through BICD2, and kinesin-1); nesprin-3 binds plectin and so intermediate filaments; nesprin-4 binds kinesin-1; and the meiosis-specific KASH5 recruits dynein-dynactin. The bridge transmits force for nuclear migration and anchorage, centrosome-nucleus coupling, meiotic telomere-led chromosome movement, and sperm head-tail attachment. Disruption causes muscular dystrophy, cerebellar ataxia, hearing loss, infertility and neuronal migration defects.

## Provisional Biological Outline

- LINC complex
  - 1. inner-nuclear-membrane SUN component binding KASH peptides and the nucleoskeleton
  - SUN inner-nuclear-membrane component
    - Alternative versions by somatic vs germline SUN proteins: SUN paralog by cell context
      - Somatic SUN1/SUN2
        - SUN1/SUN2 KASH-binding anchor (molecular player: SUN-domain proteins (SUN1, SUN2); activity or role: cytoskeleton-nuclear membrane anchor activity)
        - SUN1/SUN2 nucleoplasmic lamina anchor (molecular player: SUN-domain proteins (SUN1, SUN2); activity or role: lamin binding)
      - Germline SUN5 at the sperm head-tail junction
        - SUN5 sperm head-tail anchor (molecular player: SUN5; activity or role: sperm head-to-tail anchoring role)
  - 2. outer-nuclear-membrane KASH component coupling the bridge to a cytoskeletal system
  - KASH outer-nuclear-membrane component
    - Alternative versions by cytoskeletal system engaged (actin and microtubule motors; intermediate filaments; kinesin-1; meiotic dynein): KASH protein by cytoskeletal partner
      - Nesprin-1/2 (actin and microtubule motors)
        - Nesprin-1/2 cytoskeletal anchor (molecular player: giant nesprins (nesprin-1, nesprin-2); activity or role: cytoskeleton-nuclear membrane anchor activity)
      - Nesprin-3 (plectin and intermediate filaments)
        - Nesprin-3 plectin anchor (molecular player: SYNE3 (nesprin-3); activity or role: cytoskeleton-nuclear membrane anchor activity)
      - Nesprin-4 (kinesin-1)
        - Nesprin-4 kinesin-1 anchor (molecular player: SYNE4 (nesprin-4); activity or role: cytoskeleton-nuclear membrane anchor activity)
      - KASH5 with SUN1 (meiotic telomere attachment)
        - KASH5 meiotic dynein anchor (molecular player: KASH5; activity or role: dynein complex binding)
  - 3. torsinA-dependent assembly of LINC complexes into force-bearing TAN lines
  - TorsinA regulation of LINC assembly
    - TorsinA luminal AAA+ ATPase (molecular player: TOR1A (torsinA); activity or role: ATP hydrolysis activity)

## Known Relationships Among Steps

- SUN inner-nuclear-membrane component connects to KASH outer-nuclear-membrane component: SUN trimers bind KASH peptides in the perinuclear space and are required to keep KASH proteins in the outer nuclear membrane.
- TorsinA regulation of LINC assembly promotes KASH outer-nuclear-membrane component: TorsinA with LAP1 promotes assembly of nesprin-2G/SUN2 TAN lines and the mobility of nesprin-2G within the nuclear envelope.

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

LINC complex (SUN-KASH nuclear envelope bridge) module

## Working Scope

The LINC (linker of nucleoskeleton and cytoskeleton) complex is a transmembrane bridge across the nuclear envelope. It connects the cytoskeleton to the nuclear interior. Inner-nuclear-membrane SUN-domain proteins form trimers whose C-terminal SUN domains project into the perinuclear space. Each trimer binds the C-terminal KASH peptides of three outer-nuclear-membrane KASH proteins, and the pair is reinforced by a conserved intermolecular disulfide. On the nucleoplasmic side, SUN proteins bind the nuclear lamina and, in meiosis, telomeres. On the cytoplasmic side, different KASH proteins engage different cytoskeletal systems: nesprin-1 and nesprin-2 bind actin through calponin-homology domains and bind microtubule motors (dynein-dynactin through BICD2, and kinesin-1); nesprin-3 binds plectin and so intermediate filaments; nesprin-4 binds kinesin-1; and the meiosis-specific KASH5 recruits dynein-dynactin. The bridge transmits force for nuclear migration and anchorage, centrosome-nucleus coupling, meiotic telomere-led chromosome movement, and sperm head-tail attachment. Disruption causes muscular dystrophy, cerebellar ataxia, hearing loss, infertility and neuronal migration defects.

## Provisional Biological Outline

- LINC complex
  - 1. inner-nuclear-membrane SUN component binding KASH peptides and the nucleoskeleton
  - SUN inner-nuclear-membrane component
    - Alternative versions by somatic vs germline SUN proteins: SUN paralog by cell context
      - Somatic SUN1/SUN2
        - SUN1/SUN2 KASH-binding anchor (molecular player: SUN-domain proteins (SUN1, SUN2); activity or role: cytoskeleton-nuclear membrane anchor activity)
        - SUN1/SUN2 nucleoplasmic lamina anchor (molecular player: SUN-domain proteins (SUN1, SUN2); activity or role: lamin binding)
      - Germline SUN5 at the sperm head-tail junction
        - SUN5 sperm head-tail anchor (molecular player: SUN5; activity or role: sperm head-to-tail anchoring role)
  - 2. outer-nuclear-membrane KASH component coupling the bridge to a cytoskeletal system
  - KASH outer-nuclear-membrane component
    - Alternative versions by cytoskeletal system engaged (actin and microtubule motors; intermediate filaments; kinesin-1; meiotic dynein): KASH protein by cytoskeletal partner
      - Nesprin-1/2 (actin and microtubule motors)
        - Nesprin-1/2 cytoskeletal anchor (molecular player: giant nesprins (nesprin-1, nesprin-2); activity or role: cytoskeleton-nuclear membrane anchor activity)
      - Nesprin-3 (plectin and intermediate filaments)
        - Nesprin-3 plectin anchor (molecular player: SYNE3 (nesprin-3); activity or role: cytoskeleton-nuclear membrane anchor activity)
      - Nesprin-4 (kinesin-1)
        - Nesprin-4 kinesin-1 anchor (molecular player: SYNE4 (nesprin-4); activity or role: cytoskeleton-nuclear membrane anchor activity)
      - KASH5 with SUN1 (meiotic telomere attachment)
        - KASH5 meiotic dynein anchor (molecular player: KASH5; activity or role: dynein complex binding)
  - 3. torsinA-dependent assembly of LINC complexes into force-bearing TAN lines
  - TorsinA regulation of LINC assembly
    - TorsinA luminal AAA+ ATPase (molecular player: TOR1A (torsinA); activity or role: ATP hydrolysis activity)

## Known Relationships Among Steps

- SUN inner-nuclear-membrane component connects to KASH outer-nuclear-membrane component: SUN trimers bind KASH peptides in the perinuclear space and are required to keep KASH proteins in the outer nuclear membrane.
- TorsinA regulation of LINC assembly promotes KASH outer-nuclear-membrane component: TorsinA with LAP1 promotes assembly of nesprin-2G/SUN2 TAN lines and the mobility of nesprin-2G within the nuclear envelope.

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

# LINC complex (SUN–KASH nuclear-envelope bridge): a concise mechanistic review

## 1. Executive summary

The **linker of nucleoskeleton and cytoskeleton (LINC) complex** is best defined narrowly as a membrane-spanning **SUN–KASH bridge**: SUN-domain proteins cross the inner nuclear membrane (INM), KASH-domain proteins cross the outer nuclear membrane (ONM), and their lumenal domains bind in the perinuclear space. In a broader functional sense, a LINC *module* includes the structures attached to each end—lamins, chromatin or meiotic telomeres inside, and actin, intermediate filaments or microtubule motors outside—but these partners are not core LINC subunits. Nuclear pores, lamins, centrosomes, motors, focal adhesions and mechanosensitive transcription pathways are neighboring systems, not parts of the minimal complex (cain2018conservedsunkashinterfaces pages 1-3, sosa2012linccomplexesform pages 1-2, mcgillivary2023buildingandbreaking pages 1-3).

The most secure structural unit is a **SUN trimer bound to three KASH peptides (3:3)**. Each peptide lies across an interface between neighboring SUN protomers and is stabilized by terminal KASH residues, the SUN “KASH lid,” and—where conserved—an intermolecular SUN–KASH disulfide. A competing model proposes that two 3:3 units associate back-to-back into **6:6 nodes**, potentially creating branched, force-distributing networks. The 6:6 model has substantial crystallographic and solution-biophysical support, but its prevalence in native membranes remains unresolved (gurusaran2021amolecularmechanism pages 12-15, sosa2012linccomplexesform pages 2-4, gurusaran2021amolecularmechanism pages 9-12).

Functional specificity is generated mainly by the cytoplasmic domains of KASH proteins and by cell context. Giant nesprin-1/2 proteins couple the envelope to actin and microtubule motors; nesprin-3 couples indirectly to intermediate filaments through plectin; nesprin-4 recruits kinesin-1 in cochlear outer hair cells; KASH5 recruits dynein–dynactin during meiosis; and SUN5 supports the sperm head–tail junction. TorsinA–LAP1 regulates nesprin-2G/SUN2 transmembrane actin-associated nuclear (TAN) lines in migrating fibroblasts, but current evidence does **not** justify treating torsinA as a universal LINC-assembly factor (ketema2013nesprin3connectsplectin pages 1-2, zhou2024nesprin2coordinatesopposing pages 1-2, luxton2014kashingupwith pages 3-4, taiber2022anesprin4kinesin1cargo pages 1-2, saunders2017torsinacontrolstan pages 11-12).

Recent work has shifted the field from viewing LINC complexes as passive tethers toward seeing them as regulated, redox-sensitive and compositionally specialized force-transmission assemblies. Important 2023–2024 advances include evidence for SUN2 disulfide remodeling, bidirectional motor coordination by neuronal nesprin-2, a pathogenic role for nesprin-1-dependent microtubule loading in laminopathy, and an in-vivo requirement for LINC coupling in exercise-induced osteoid deposition (sharma2023disulfidebondin pages 1-2, leong2023nesprin1linccomplexes pages 1-2, zhou2024nesprin2coordinatesopposing pages 1-2, birks2024prrx1drivenlinccomplex pages 1-2).

## 2. Definition and biological boundaries

### 2.1 Minimal versus extended definitions

The **minimal LINC complex** comprises an INM SUN protein and an ONM KASH protein joined in the nuclear-envelope lumen. SUN proteins expose N-terminal regions to the nucleoplasm and C-terminal SUN domains to the lumen; KASH proteins have large cytoplasmic N-termini, one C-terminal transmembrane helix and a short lumenal KASH peptide, commonly ending in a PPPX-like motif. SUN binding both creates the bridge and helps retain KASH proteins at the ONM (cain2018conservedsunkashinterfaces pages 1-3, hieda2017implicationsfordiverse pages 1-3, mcgillivary2023buildingandbreaking pages 1-3).

The **extended force-transmission module** includes:

- lamins and chromatin-associated proteins bound to nucleoplasmic SUN regions;
- meiosis-specific telomere adaptors such as TRF1–TERB1–TERB2–MAJIN;
- cytoplasmic actin, plectin/intermediate filaments, kinesin and dynein–dynactin;
- motor adaptors such as BICD2; and
- context-dependent regulators including torsinA, LAP1 and lumenal redox enzymes.

These are functionally coupled to LINC but should not be called SUN–KASH core subunits (mcgillivary2023buildingandbreaking pages 3-4, goncalves2020nesprin2recruitmentof pages 1-4, pereira2019nuclearenvelopedynamics pages 13-14).

### 2.2 Neighboring systems that should remain separate

**Nuclear pores** mediate nucleocytoplasmic transport and occupy membrane fusion sites; they do not form the mechanical SUN–KASH bridge. **The nuclear lamina** is a nucleoskeletal endpoint and mechanical substrate rather than the LINC complex itself. **Centrosomes and microtubule-organizing centers** are cargo-positioning partners; their coupling can be LINC-dependent but also uses nuclear-pore and other pathways. **Focal adhesions, adherens junctions, YAP/TAZ signaling and chromatin remodeling** lie upstream or downstream of force transmission and should not be conflated with the bridge. Likewise, the sperm head–tail coupling apparatus and the meiotic telomere attachment plate contain many proteins beyond SUN–KASH (sosa2012linccomplexesform pages 1-2, kuwako2024diverserolesof pages 2-5, pereira2019nuclearenvelopedynamics pages 13-14, zhang2021sun5interactingwith pages 1-2).

A useful terminological distinction is therefore: **“LINC complex”** for the core trans-envelope SUN–KASH linkage, and **“LINC-dependent mechanical pathway”** for the complete route from cytoskeleton or motor to lamina/chromosome and downstream signaling.

## 3. Mechanistic overview

### 3.1 Assembly and force-transmission sequence

1. **Membrane targeting and topology.** SUN proteins occupy the INM with their nucleoplasmic regions available to bind lamina/chromatin and their C-terminal SUN regions in the perinuclear lumen. KASH proteins are tail-anchored in the ONM, with cytoplasmic effector domains facing the cytoskeleton (cain2018conservedsunkashinterfaces pages 1-3, sosa2012linccomplexesform pages 1-2).

2. **SUN activation and trimerization.** Coiled-coil regions preceding the SUN domain promote trimerization and relieve a proposed KASH-lid-mediated autoinhibited state. Calcium has been reported to affect trimerization and binding, but its direction and physiological significance remain context-dependent (mcgillivary2023buildingandbreaking pages 3-4, hao2019sunkashinteractionsfacilitate pages 9-12).

3. **KASH capture.** Three KASH peptides bind grooves assembled across SUN-protomer interfaces. The terminal PPPX region occupies a conserved pocket, upstream residues contact the SUN surface, and the KASH lid contributes a cross-protomer clamp. Deleting terminal KASH residues abolishes binding (cain2018conservedsunkashinterfaces pages 1-3, sosa2012linccomplexesform pages 2-4).

4. **Covalent and noncovalent reinforcement.** A conserved KASH cysteine can form a disulfide with SUN2 C563. Genetic and cell-based mutagenesis shows that this bond strengthens nuclear anchorage and movement, while simulations indicate improved force transfer into the SUN coiled coil. It is not universally obligatory: some short KASH proteins or developmental movements tolerate loss of the cysteine linkage (hao2019sunkashinteractionsfacilitate pages 1-5, cain2018conservedsunkashinterfaces pages 1-3, hao2019sunkashinteractionsfacilitate pages 9-12).

5. **Higher-order organization.** Individual bridges can cluster in meiotic foci, puncta or TAN lines. Purified complexes can form 6:6 assemblies through KASH-lid contacts, KASH-mediated interactions or, for nesprin-4, zinc coordination. These may distribute load across a branched network, but endogenous stoichiometry and membrane geometry have not been decisively measured (gurusaran2021amolecularmechanism pages 12-15, gurusaran2021amolecularmechanism pages 9-12).

6. **Force application and nuclear response.** Cytoplasmic actomyosin flow or microtubule motors load the KASH protein; force passes through SUN to lamins, chromatin or meiotic chromosome ends. Depending on context, the result is nuclear translation, anchorage, deformation, chromosome movement or altered mechanosensitive signaling (sosa2012linccomplexesform pages 1-2, kuwako2024diverserolesof pages 2-5).

### 3.2 Obligatory, conditional and accessory steps

**Obligatory for a canonical bridge:** correct SUN/KASH membrane topology, lumenal SUN–KASH recognition and physical coupling to the relevant nuclear and cytoplasmic endpoints. SUN-dependent ONM retention is especially important because uncoupled KASH proteins redistribute toward contiguous ER membranes (mcgillivary2023buildingandbreaking pages 1-3, leong2023nesprin1linccomplexes pages 1-2).

**Conditional:** the intermolecular disulfide, a particular SUN paralog, 6:6 assembly, lamins, specific motors and particular cytoskeletal systems. For example, nesprin-2 actin binding can be dispensable during neuronal nuclear migration even though it is essential in actin-driven TAN-line movement (goncalves2020nesprin2recruitmentof pages 1-4, saunders2017torsinacontrolstan pages 1-2).

**Accessory/regulatory:** torsinA–LAP1, lumenal redox enzymes, BICD2 and chromosome-end adaptors. These govern assembly dynamics, motor recruitment or substrate attachment but do not define the minimal bridge (mcgillivary2023buildingandbreaking pages 3-4, saunders2017torsinacontrolstan pages 11-12).

### 3.3 Dynamic disulfide remodeling

A 2023 study using a conformation-specific SUN2 antibody, imaging and biochemical perturbation found KASH-dependent inter- and intramolecular rearrangements among conserved SUN2 cysteines. Disrupting the terminal disulfide altered SUN2 localization, turnover, LINC assembly, cytoskeletal organization and migration; ER-lumen components influenced its redox state. This argues against viewing the disulfide as an irreversible molecular rivet, although the responsible enzymatic sequence and its generality across SUN/KASH pairs remain uncertain (sharma2023disulfidebondin pages 1-2). A contemporary review also implicates TMX4/PDI-mediated cleavage and mixed-disulfide intermediates, but emphasizes the need for full-length membrane reconstitution and in-vivo validation (mcgillivary2023buildingandbreaking pages 3-4).

## 4. Major molecular players and active assemblies

The principal mammalian modules and the strength of evidence for each are summarized below.

| Module/assembly | Inner-nuclear-membrane SUN partner | Outer-nuclear-membrane KASH partner | Nucleoplasmic/chromosomal input | Cytoplasmic effector | Principal biological function | Evidence strength / key caveat |
|---|---|---|---|---|---|---|
| Somatic actin–microtubule LINC | SUN1 and/or SUN2 | Nesprin-1G or nesprin-2G | Lamins and chromatin-associated proteins | F-actin through N-terminal calponin-homology domains; kinesin-1; dynein–dynactin through BICD2 | Nuclear anchorage and migration, centrosome–nucleus coordination, cell polarity and force transmission | Strong biochemical, genetic and cell-biological support, but SUN/nesprin pairing and cytoskeletal dependence vary by cell type. In neurons, nesprin-2 coordinates kinesin-1 and dynein–dynactin–BICD2, whereas its actin-binding domain can be dispensable (goncalves2020nesprin2recruitmentof pages 1-4, zhou2024nesprin2coordinatesopposing pages 1-2). |
| Intermediate-filament LINC | SUN protein, usually SUN1/2 | Nesprin-3 | Nuclear lamina-associated structures | Plectin, which couples nesprin-3 indirectly to vimentin and other intermediate filaments | Perinuclear intermediate-filament organization and mechanical integration | Direct binding and knockout evidence support the linkage; physiological necessity is context-dependent—nesprin-3-null mice retain Sertoli-cell nuclear positioning and fertility (ketema2013nesprin3connectsplectin pages 1-2). |
| Auditory kinesin LINC | SUN1 is the best-supported partner | Nesprin-4 | Nuclear lamina | Kinesin-1, recruited through a conserved four-residue motif | Nuclear positioning and survival of cochlear outer hair cells; hearing | Strong human-genetic, mouse-knockout and AAV-rescue evidence. The requirement is highly cell-specific: outer, but not inner, hair cells are chiefly affected (taiber2022anesprin4kinesin1cargo pages 1-2). |
| Meiotic telomere–motor LINC | SUN1; SUN2 can associate with KASH5 and may partly compensate | KASH5 | Telomeres through the TRF1–TERB1–TERB2–MAJIN attachment machinery | Dynein–dynactin; KASH5 functions as a motor-recruiting/activating adaptor | Telomere-led chromosome movement, bouquet formation, homolog pairing and meiotic progression | Strong knockout, localization and motor-recruitment evidence; SUN2’s normal contribution versus compensatory role is less certain. TERB proteins, MAJIN and motors are associated factors, not core SUN–KASH bridge subunits (luxton2014kashingupwith pages 3-4, pereira2019nuclearenvelopedynamics pages 13-14). |
| Sperm head–tail junction | SUN5 | Nesprin-3 is a reported KASH partner | Sperm nucleus and implantation-fossa structures | Centrosome/head–tail coupling apparatus, with additional structural proteins | Anchoring the sperm head to the flagellar apparatus during spermiogenesis | SUN5 requirement is strongly supported by mouse knockout and human infertility evidence; the exact canonicality and complete composition of a SUN5–nesprin-3 LINC bridge remain less secure than SUN5’s anchoring function (shang2017essentialrolefor pages 1-2, zhang2021sun5interactingwith pages 1-2). |
| Actin-coupled TAN lines | SUN2 | Nesprin-2G | Lamins and nuclear-envelope anchorage sites | Retrograde-flowing dorsal actin cables bound by nesprin-2G calponin-homology domains | Rearward nuclear movement and centrosome orientation during fibroblast polarization | Strong cell-biological evidence in migrating fibroblasts. TorsinA is a luminal AAA+ ATPase and LAP1 its INM activator; they regulate nesprin-2G mobility, TAN-line assembly and actin flow but are accessory, context-specific regulators—not core SUN–KASH subunits or demonstrated universal LINC assembly factors (saunders2017torsinacontrolstan pages 11-12, saunders2017torsinacontrolstan pages 1-2). |


*Table: Comparison of major mammalian SUN–KASH bridges, their nuclear inputs, cytoplasmic effectors, and specialized functions. The table separates core membrane-spanning SUN/KASH proteins from motor adaptors, cytolinkers, chromosome-attachment factors, and torsinA–LAP1 regulators.*

### 4.1 Somatic SUN1/SUN2–nesprin-1/2 systems

SUN1 and SUN2 provide partially overlapping INM anchors, but they are not always interchangeable. Giant nesprin-1 and nesprin-2 contain N-terminal calponin-homology domains that bind F-actin and long spectrin-repeat rods that organize additional interactions. Microtubule coupling is modular: recent neuronal work identifies a kinesin-1-binding LEWD motif and separate nesprin-2 regions that recruit dynein–dynactin–BICD2 (ketema2013nesprin3connectsplectin pages 1-2, zhou2024nesprin2coordinatesopposing pages 1-2).

In developing neurons, nesprin-2 recruits both opposing motors and promotes prolonged bidirectional nuclear movement rather than a simple unregulated tug-of-war. Perturbing either dynein or kinesin reduces movement, and rescue requires both motor-interaction regions. This 2024 result refines the older model in which dynein alone was viewed as the forward force and kinesin chiefly as a brake (goncalves2020nesprin2recruitmentof pages 1-4, zhou2024nesprin2coordinatesopposing pages 1-2).

### 4.2 Nesprin-3–plectin–intermediate-filament coupling

Nesprin-3 binds plectin, which binds vimentin and other intermediate filaments. Nesprin-3 knockout reduces perinuclear plectin and vimentin in Sertoli cells, directly supporting the molecular linkage. Nevertheless, mutant mice retain normal Sertoli-cell nuclear positioning and fertility, demonstrating that a biochemically clear linkage need not be indispensable where redundant anchoring systems exist (ketema2013nesprin3connectsplectin pages 1-2).

### 4.3 Nesprin-4–kinesin-1 in the cochlea

Nesprin-4 recruits kinesin-1 through a conserved four-residue motif. Human and mouse SYNE4 deficiency mispositions outer-hair-cell nuclei, causes outer-hair-cell death and produces deafness. AAV experiments showed that restoring wild-type nesprin-4—but not a kinesin-binding-defective form—prevents nuclear mislocalization, cell death and hearing loss. The restriction to outer rather than inner hair cells illustrates stringent cell-type dependence (taiber2022anesprin4kinesin1cargo pages 1-2).

### 4.4 SUN1/2–KASH5 in meiosis

In mammalian meiotic prophase, TRF1 recruits TERB1; TERB1–TERB2–MAJIN builds an INM-associated attachment plate that recruits SUN1. SUN1 engages KASH5, and KASH5 recruits/activates dynein–dynactin, coupling telomeres to microtubules. The pathway drives bouquet formation and telomere-led motion that facilitates pairing and synapsis. Loss of SUN1 or KASH5 disrupts telomere dynamics and meiotic progression; KASH5-null males arrest in prophase I and are sterile (luxton2014kashingupwith pages 3-4, pereira2019nuclearenvelopedynamics pages 13-14).

SUN2 can bind KASH5 and may partly compensate when SUN1 is absent, but its normal contribution remains less clearly established. Plant meiosis uses homologous logic but different outer-envelope machinery: a 2024 *Arabidopsis* study measured rapid centromere movements up to **500 nm/s** during zygotene/pachytene and found them abolished in *sun1 sun2* double mutants, while bouquet organization and nucleolar displacement were also defective. This supports deep functional conservation without implying identical molecular partners in animals and plants.

### 4.5 SUN5 and sperm head–tail attachment

SUN5 is testis enriched and concentrates at the sperm neck/implantation fossa. Sun5-null mice form a head–tail coupling apparatus that subsequently detaches from the nucleus during spermatid elongation, producing headless tails and retained or detached heads. Human SUN5 variants cause acephalic spermatozoa syndrome; one study estimated SUN5 variants in approximately **33–47%** of affected patients (shang2017essentialrolefor pages 1-2, zhang2021sun5interactingwith pages 1-2, kmonickova2020theroleof pages 12-15).

Nesprin-3 has been reported as a SUN5 partner whose posterior localization is lost in Sun5-null spermatids. However, the complete composition and topology of this specialized bridge are less firmly resolved than the requirement for SUN5 itself. Additional head–tail coupling proteins should therefore not automatically be labeled LINC subunits (zhang2021sun5interactingwith pages 1-2).

### 4.6 TorsinA–LAP1 and TAN lines

In polarizing fibroblasts, nesprin-2G/SUN2 complexes assemble into TAN lines aligned with retrograde-flowing dorsal actin cables. Nesprin-2G’s actin-binding domains capture the cable; SUN2 and lamina-associated interactions resist slippage, allowing actin flow to move the nucleus rearward and orient the centrosome (saunders2017torsinacontrolstan pages 1-2).

TorsinA is a lumenal AAA+ ATPase activated by LAP1 at the INM. Depletion of torsinA or LAP1 impairs TAN-line assembly, nesprin-2G mobility, actin-cable flow and rearward nuclear movement. The best interpretation is a selective remodeling/chaperone role in this assay, possibly controlling SUN–KASH turnover or nesprin mobility. Direct substrates remain unknown, and evidence does not establish torsinA as obligatory for all LINC complexes (saunders2017torsinacontrolstan pages 11-12, saunders2016lincingdefectivenuclearcytoskeletal pages 6-7, saunders2016lincingdefectivenuclearcytoskeletal pages 3-4).

## 5. Evolutionary and cell-biological variation

### 5.1 Origin and conserved core

SUN proteins are widely distributed across animals, fungi, plants, amoebozoans and diverse protists. KASH-side proteins are far more sequence-divergent and difficult to identify outside animals. Functional and architectural analogs in fungi and plants make a SUN–KASH-like bridge in the last eukaryotic common ancestor plausible, but not proven; apparent absence can represent genuine loss, rapid divergence or replacement (koreny2016ancienteukaryoticorigin pages 5-7, koreny2016ancienteukaryoticorigin pages 7-8).

Thus the most defensible ancestral reconstruction is a **SUN-centered trans-envelope tether**, probably connected to a divergent outer-membrane partner. Modern mammalian SUN1/2 and giant nesprin systems should not be treated as direct proxies for every ancestral feature.

### 5.2 Plants, fungi and protists

Plants retain C-terminal and mid-SUN lineages. A survey of 216 SUN proteins divided plant, fungal and protist sequences into these two broad clades; plant mid-SUNs diversified into SUN3 and SUN5 before the angiosperm ancestor, whereas the C-terminal group retained a SUN1-like subfamily (yuan2021evolutionandfunctional pages 1-2). Plant outer-envelope WIP/SINE proteins share architecture and SUN-binding function with opisthokont KASH proteins despite weak sequence homology, and plant lamina-like CRWN/KAKU4/NEAP systems are not equivalent to metazoan lamins (poulet2017exploringtheevolution pages 11-15, zhou2013howplantslinc pages 1-2).

Fungal bridges couple chromosomes or spindle-pole bodies to cytoplasmic microtubules using lineage-specific SUN/KASH-like pairs. Protist sampling indicates both deep conservation and extensive replacement. Consequently, “conserved LINC function” is often safer than asserting one-to-one orthology of all partners.

### 5.3 Cell- and stage-specific alternatives

- **Migrating fibroblasts:** nesprin-2G/SUN2–actin TAN lines.
- **Developing neurons:** nesprin-2 plus dynein–dynactin–BICD2 and kinesin-1; actin binding can be dispensable.
- **Striated muscle:** nesprin-1-rich complexes recruit microtubule nucleation and motor machinery.
- **Cochlear outer hair cells:** nesprin-4–kinesin-1 is uniquely critical.
- **Meiotic prophase:** SUN1/2–KASH5 connects telomere attachment plates to motors.
- **Spermiogenesis:** SUN3/4/5-containing assemblies shape the sperm nucleus and secure the tail; SUN5 acts after the meiotic SUN1–KASH5 system (goncalves2020nesprin2recruitmentof pages 1-4, taiber2022anesprin4kinesin1cargo pages 1-2, kmonickova2020theroleof pages 1-4, leong2023nesprin1linccomplexes pages 1-2).

These alternatives are not freely interchangeable routes. Their availability is constrained by paralog expression, isoform architecture, chromosome-attachment factors, motor repertoire and developmental timing.

## 6. Constraints, dependencies and failure modes

### 6.1 Physical and temporal constraints

Topology imposes a strict order: proteins must first reach the correct nuclear membrane; SUN must expose a competent lumenal binding surface; KASH capture then stabilizes ONM localization; only afterward can cytoplasmic load be transmitted to nuclear substrates. A reversed membrane orientation or terminal KASH extension disrupts binding and nuclear movement, demonstrating that geometry—not merely affinity—is essential (cain2018conservedsunkashinterfaces pages 1-3, leong2023nesprin1linccomplexes pages 1-2).

Meiotic telomere motion additionally requires chromosome attachment before motor force can be productive: TRF1–TERB1–TERB2–MAJIN recruits SUN1, then SUN1–KASH5 engages dynein. SUN5 head–tail anchoring occurs later during spermiogenesis and cannot substitute for this meiotic pathway (kmonickova2020theroleof pages 1-4, pereira2019nuclearenvelopedynamics pages 13-14).

### 6.2 Disease mechanisms

**Muscle and heart.** SYNE1/2, LMNA, EMD and SUN variants are associated with Emery–Dreifuss muscular dystrophy and dilated cardiomyopathy. Disease may arise from excessive force transfer to mechanically fragile nuclei as well as altered gene regulation. In mouse laminopathy models, Sun1 deletion or dominant-negative SUN/KASH constructs suppress pathology, whereas Sun2 deletion does not; disrupting the nesprin-1 KASH connection reduces microtubule loading and can ameliorate LMNA-linked cardiac disease. This supports LINC attenuation as an experimental therapeutic strategy but does not yet establish a safe human treatment (leong2023nesprin1linccomplexes pages 1-2).

**Cerebellar ataxia and neurological disease.** A systematic review catalogued 141 SYNE1 variants: 127 (**90.07%**) were coding; among these, 62 (**48.82%**) were nonsense, 32 (**25.20%**) missense and 30 (**23.62%**) frameshift. Of all reported variants, 122 (**85.82%**) were associated with recessive spinocerebellar ataxia type 8 and 19 (**13.48%**) with ALS. These statistics summarize published pathogenic reports rather than population prevalence and are vulnerable to ascertainment bias (storey2022genotypephenotypecorrelationsin pages 11-13). Mouse phenotypes do not always reproduce human SYNE1 ataxia, and some cerebellar functions may involve KASH-less nesprin isoforms at synapses rather than canonical LINC bridges (kuwako2024diverserolesof pages 11-12, kuwako2024diverserolesof pages 12-14).

**Neuronal migration.** Loss of nesprin-2/BICD2 coupling impairs nuclear translocation while centrosome advance can remain intact, supporting a direct nuclear-migration mechanism. A human BICD2 truncation associated with lissencephaly disrupts this interaction, but BICD2 is an adaptor rather than a LINC core protein (goncalves2020nesprin2recruitmentof pages 1-4, kuwako2024diverserolesof pages 14-15).

**Hearing loss.** SYNE4 deficiency causes a highly specific outer-hair-cell nuclear-positioning defect. AAV restoration in mice improved nuclear positioning and hearing, providing one of the clearest preclinical implementations of LINC-directed therapy (taiber2022anesprin4kinesin1cargo pages 1-2, kuwako2024diverserolesof pages 12-14).

**Infertility.** SUN1/KASH5 failure blocks meiotic progression; SUN5 failure causes acephalic sperm. Intracytoplasmic sperm injection using isolated SUN5-mutant sperm heads produced healthy heterozygous offspring in reported mouse and patient settings, suggesting a practical assisted-reproduction route, although broader safety and outcome data remain limited (shang2017essentialrolefor pages 1-2).

**TorsinA-related dystonia.** TorsinA dysfunction perturbs selected nuclear-envelope and TAN-line behaviors, but a direct chain from defective LINC remodeling to DYT1 dystonia remains incompletely demonstrated. TorsinA has multiple nuclear-envelope/ER functions, so the disease should not be classified simply as a primary LINC disorder (saunders2017torsinacontrolstan pages 11-12, saunders2016lincingdefectivenuclearcytoskeletal pages 7-9).

### 6.3 Recent real-world and experimental applications

Beyond AAV rescue, ICSI and experimental laminopathy attenuation, LINC perturbation is being used to test tissue mechanobiology. In a 2024 mouse study, Cre-driven EGFP-KASH2 disrupted endogenous SUN–nesprin binding in Prrx1-positive skeletal progenitors. It abolished exercise-associated increases in osteoid volume and surface after six weeks of voluntary running, but did not alter bone microarchitecture or mechanical properties. This result supports a role in adaptive osteoid deposition, not a general requirement for bone quality (birks2024prrx1drivenlinccomplex pages 1-2).

## 7. Controversies and open questions

1. **3:3 or 6:6 in cells?** The 3:3 unit is structurally and genetically secure; purified SUN1–KASH complexes support constitutive 6:6 assemblies, but native stoichiometry, membrane curvature and force-dependent transitions remain unmeasured (gurusaran2021amolecularmechanism pages 12-15, sosa2012linccomplexesform pages 2-4).

2. **How are partners selected?** Purified SUN domains can bind several KASH peptides, yet cells produce preferential pairings. Full-length topology, tissue expression, membrane lipids, post-translational modifications and accessory factors probably impose specificity (mcgillivary2023buildingandbreaking pages 3-4, sharma2023disulfidebondin pages 1-2).

3. **What does the disulfide do dynamically?** It strengthens load transfer but is not universally essential. How lumenal oxidoreductases, calcium and mechanical load coordinate bond formation and cleavage is unresolved (mcgillivary2023buildingandbreaking pages 3-4, hao2019sunkashinteractionsfacilitate pages 9-12).

4. **What are torsinA’s direct substrates?** TAN-line phenotypes are compelling, but direct ATPase-dependent remodeling of a defined full-length SUN/KASH substrate has not been reconstituted (saunders2017torsinacontrolstan pages 11-12, saunders2016lincingdefectivenuclearcytoskeletal pages 3-4).

5. **How does force reach chromatin and alter transcription?** Physical continuity is established, but distinguishing direct chromatin deformation from secondary signaling, nuclear-pore effects and changes in actomyosin remains difficult.

6. **Why are disorders tissue selective?** Isoform complexity, mechanical load and redundancy explain part of the specificity, but ubiquitous expression does not predict whether muscle, cerebellum, cochlea or germ cells will fail. Human variant interpretation is particularly difficult for the enormous SYNE1/2 genes (storey2022genotypephenotypecorrelationsin pages 15-16, kuwako2024diverserolesof pages 11-12).

7. **How ancient is canonical KASH?** SUN conservation is clear; KASH homology outside animals is not. Better sampling and structure-based homology will be needed to distinguish ancestral conservation from convergent outer-envelope tethers (koreny2016ancienteukaryoticorigin pages 5-7, padillamejia2021evolutionanddiversification pages 1-3).

## 8. Key references

- **Sosa BA et al.** “LINC complexes form by binding of three KASH peptides to domain interfaces of trimeric SUN proteins.” *Cell* 149, 1035–1047. Published 25 May 2012. DOI: [10.1016/j.cell.2012.03.046](https://doi.org/10.1016/j.cell.2012.03.046). Foundational 3:3 SUN–KASH structure (sosa2012linccomplexesform pages 1-2, sosa2012linccomplexesform pages 2-4).
- **Cain NE et al.** “Conserved SUN–KASH interfaces mediate LINC complex-dependent nuclear movement and positioning.” *Current Biology* 28, 3086–3097.e4. Published October 2018. DOI: [10.1016/j.cub.2018.08.001](https://doi.org/10.1016/j.cub.2018.08.001). In-vivo interface mutagenesis (cain2018conservedsunkashinterfaces pages 1-3).
- **Gurusaran M, Davies OR.** “A molecular mechanism for LINC complex branching by structurally diverse SUN–KASH 6:6 assemblies.” 2021 preprint. DOI: [10.1101/2020.03.21.001867](https://doi.org/10.1101/2020.03.21.001867). Principal evidence for the 6:6 network model; interpret with the limitation that native cellular stoichiometry remains unresolved (gurusaran2021amolecularmechanism pages 1-5, gurusaran2021amolecularmechanism pages 12-15).
- **McGillivary RM et al.** “Building and breaking mechanical bridges between the nucleus and cytoskeleton.” *Current Opinion in Cell Biology* 85, 102260. Published December 2023. DOI: [10.1016/j.ceb.2023.102260](https://doi.org/10.1016/j.ceb.2023.102260). Authoritative review of assembly regulation (mcgillivary2023buildingandbreaking pages 1-3, mcgillivary2023buildingandbreaking pages 3-4).
- **Sharma R, Hetzer MW.** “Disulfide bond in SUN2 regulates dynamic remodeling of LINC complexes at the nuclear envelope.” *Life Science Alliance* 6, e202302031. Published May 2023. DOI: [10.26508/lsa.202302031](https://doi.org/10.26508/lsa.202302031) (sharma2023disulfidebondin pages 1-2).
- **Zhou C et al.** “Nesprin-2 coordinates opposing microtubule motors during nuclear migration in neurons.” *Journal of Cell Biology* 223. Published August 2024. DOI: [10.1083/jcb.202405032](https://doi.org/10.1083/jcb.202405032) (zhou2024nesprin2coordinatesopposing pages 1-2).
- **Leong EL et al.** “Nesprin-1 LINC complexes recruit microtubule cytoskeleton proteins and drive pathology in Lmna-mutant striated muscle.” *Human Molecular Genetics* 32, 177–191. Published 2023. DOI: [10.1093/hmg/ddac179](https://doi.org/10.1093/hmg/ddac179) (leong2023nesprin1linccomplexes pages 1-2).
- **Kuwako K, Suzuki S.** “Diverse roles of the LINC complex in cellular function and disease in the nervous system.” *International Journal of Molecular Sciences* 25, 11525. Published October 2024. DOI: [10.3390/ijms252111525](https://doi.org/10.3390/ijms252111525) (kuwako2024diverserolesof pages 11-12, kuwako2024diverserolesof pages 12-14).
- **Taiber S et al.** “A Nesprin-4/kinesin-1 cargo model for nuclear positioning in cochlear outer hair cells.” *Frontiers in Cell and Developmental Biology* 10. Published September 2022. DOI: [10.3389/fcell.2022.974168](https://doi.org/10.3389/fcell.2022.974168) (taiber2022anesprin4kinesin1cargo pages 1-2).
- **Saunders CA et al.** “TorsinA controls TAN line assembly and the retrograde flow of dorsal perinuclear actin cables.” *Journal of Cell Biology* 216, 657–674. Published March 2017. DOI: [10.1083/jcb.201507113](https://doi.org/10.1083/jcb.201507113) (saunders2017torsinacontrolstan pages 11-12, saunders2017torsinacontrolstan pages 1-2).
- **Shang Y et al.** “Essential role for SUN5 in anchoring sperm head to the tail.” *eLife* 6. Published September 2017. DOI: [10.7554/eLife.28199](https://doi.org/10.7554/eLife.28199) (shang2017essentialrolefor pages 1-2).
- **Storey EC, Fuller HR.** “Genotype–phenotype correlations in human diseases caused by mutations of LINC complex-associated genes.” *Cells* 11, 4065. Published December 2022. DOI: [10.3390/cells11244065](https://doi.org/10.3390/cells11244065) (storey2022genotypephenotypecorrelationsin pages 15-16, storey2022genotypephenotypecorrelationsin pages 11-13).
- **Birks S et al.** “Prrx1-driven LINC complex disruption in vivo reduces osteoid deposition but not bone quality after voluntary wheel running.” *PLOS ONE* 19. Published September 2024. DOI: [10.1371/journal.pone.0307816](https://doi.org/10.1371/journal.pone.0307816) (birks2024prrx1drivenlinccomplex pages 1-2).

References

1. (cain2018conservedsunkashinterfaces pages 1-3): Natalie E. Cain, Zeinab Jahed, Amy Schoenhofen, Venecia A. Valdez, Baila Elkin, Hongyan Hao, Nathan J. Harris, Leslie A. Herrera, Brian M. Woolums, Mohammad R.K. Mofrad, G.W. Gant Luxton, and Daniel A. Starr. Conserved sun-kash interfaces mediate linc complex-dependent nuclear movement and positioning. Current Biology, 28:3086-3097.e4, Oct 2018. URL: https://doi.org/10.1016/j.cub.2018.08.001, doi:10.1016/j.cub.2018.08.001. This article has 92 citations and is from a highest quality peer-reviewed journal.

2. (sosa2012linccomplexesform pages 1-2): Brian A. Sosa, Andrea Rothballer, Ulrike Kutay, and Thomas U. Schwartz. Linc complexes form by binding of three kash peptides to domain interfaces of trimeric sun proteins. Cell, 149:1035-1047, May 2012. URL: https://doi.org/10.1016/j.cell.2012.03.046, doi:10.1016/j.cell.2012.03.046. This article has 528 citations and is from a highest quality peer-reviewed journal.

3. (mcgillivary2023buildingandbreaking pages 1-3): Rebecca M. McGillivary, Daniel A. Starr, and G.W. Gant Luxton. Building and breaking mechanical bridges between the nucleus and cytoskeleton: regulation of linc complex assembly and disassembly. Current Opinion in Cell Biology, 85:102260, Dec 2023. URL: https://doi.org/10.1016/j.ceb.2023.102260, doi:10.1016/j.ceb.2023.102260. This article has 46 citations and is from a peer-reviewed journal.

4. (gurusaran2021amolecularmechanism pages 12-15): Manickam Gurusaran and Owen R. Davies. A molecular mechanism for linc complex branching by structurally diverse sun-kash 6:6 assemblies. BioRxiv, Mar 2021. URL: https://doi.org/10.1101/2020.03.21.001867, doi:10.1101/2020.03.21.001867. This article has 63 citations.

5. (sosa2012linccomplexesform pages 2-4): Brian A. Sosa, Andrea Rothballer, Ulrike Kutay, and Thomas U. Schwartz. Linc complexes form by binding of three kash peptides to domain interfaces of trimeric sun proteins. Cell, 149:1035-1047, May 2012. URL: https://doi.org/10.1016/j.cell.2012.03.046, doi:10.1016/j.cell.2012.03.046. This article has 528 citations and is from a highest quality peer-reviewed journal.

6. (gurusaran2021amolecularmechanism pages 9-12): Manickam Gurusaran and Owen R. Davies. A molecular mechanism for linc complex branching by structurally diverse sun-kash 6:6 assemblies. BioRxiv, Mar 2021. URL: https://doi.org/10.1101/2020.03.21.001867, doi:10.1101/2020.03.21.001867. This article has 63 citations.

7. (ketema2013nesprin3connectsplectin pages 1-2): Mirjam Ketema, Maaike Kreft, Pablo Secades, Hans Janssen, and Arnoud Sonnenberg. Nesprin-3 connects plectin and vimentin to the nuclear envelope of sertoli cells but is not required for sertoli cell function in spermatogenesis. Molecular Biology of the Cell, 24:2454-2466, Aug 2013. URL: https://doi.org/10.1091/mbc.e13-02-0100, doi:10.1091/mbc.e13-02-0100. This article has 116 citations and is from a domain leading peer-reviewed journal.

8. (zhou2024nesprin2coordinatesopposing pages 1-2): Chuying Zhou, You Kure Wu, Fumiyoshi Ishidate, Takahiro K. Fujiwara, and Mineko Kengaku. Nesprin-2 coordinates opposing microtubule motors during nuclear migration in neurons. The Journal of Cell Biology, Aug 2024. URL: https://doi.org/10.1083/jcb.202405032, doi:10.1083/jcb.202405032. This article has 25 citations.

9. (luxton2014kashingupwith pages 3-4): GW Gant Luxton and Daniel A Starr. Kashing up with the nucleus: novel functional roles of kash proteins at the cytoplasmic surface of the nucleus. Current opinion in cell biology, 28:69-75, Jun 2014. URL: https://doi.org/10.1016/j.ceb.2014.03.002, doi:10.1016/j.ceb.2014.03.002. This article has 150 citations and is from a peer-reviewed journal.

10. (taiber2022anesprin4kinesin1cargo pages 1-2): Shahar Taiber, Oren Gozlan, Roie Cohen, Leonardo R. Andrade, Ellen F. Gregory, Daniel A. Starr, Yehu Moran, Rebecca Hipp, Matthew W. Kelley, Uri Manor, David Sprinzak, and Karen B. Avraham. A nesprin-4/kinesin-1 cargo model for nuclear positioning in cochlear outer hair cells. Frontiers in Cell and Developmental Biology, Sep 2022. URL: https://doi.org/10.3389/fcell.2022.974168, doi:10.3389/fcell.2022.974168. This article has 19 citations.

11. (saunders2017torsinacontrolstan pages 11-12): Cosmo A. Saunders, Nathan J. Harris, Patrick T. Willey, Brian M. Woolums, Yuexia Wang, Alex J. McQuown, Amy Schoenhofen, Howard J. Worman, William T. Dauer, Gregg G. Gundersen, and G.W. Gant Luxton. Torsina controls tan line assembly and the retrograde flow of dorsal perinuclear actin cables during rearward nuclear movement. The Journal of Cell Biology, 216:657-674, Mar 2017. URL: https://doi.org/10.1083/jcb.201507113, doi:10.1083/jcb.201507113. This article has 85 citations.

12. (sharma2023disulfidebondin pages 1-2): Rahul Sharma and Martin W Hetzer. Disulfide bond in sun2 regulates dynamic remodeling of linc complexes at the nuclear envelope. Life Science Alliance, 6:e202302031, May 2023. URL: https://doi.org/10.26508/lsa.202302031, doi:10.26508/lsa.202302031. This article has 15 citations and is from a peer-reviewed journal.

13. (leong2023nesprin1linccomplexes pages 1-2): Ei Leen Leong, Nyein Thet Khaing, Bruno Cadot, Wei Liang Hong, Serguei Kozlov, Hendrikje Werner, Esther Sook Miin Wong, Colin L Stewart, Brian Burke, and Yin Loon Lee. Nesprin-1 linc complexes recruit microtubule cytoskeleton proteins and drive pathology in lmna-mutant striated muscle. Human Molecular Genetics, 32:177-191, Aug 2023. URL: https://doi.org/10.1093/hmg/ddac179, doi:10.1093/hmg/ddac179. This article has 47 citations and is from a domain leading peer-reviewed journal.

14. (birks2024prrx1drivenlinccomplex pages 1-2): Scott Birks, Sean Howard, Christian S. Wright, Caroline O’Rourke, Elicza A. Day, Alexander J. Lamb, James R. Walsdorf, Anthony Lau, William R. Thompson, and Gunes Uzer. Prrx1-driven linc complex disruption in vivo reduces osteoid deposition but not bone quality after voluntary wheel running. PLOS ONE, Sep 2024. URL: https://doi.org/10.1371/journal.pone.0307816, doi:10.1371/journal.pone.0307816. This article has 2 citations and is from a peer-reviewed journal.

15. (hieda2017implicationsfordiverse pages 1-3): Miki Hieda. Implications for diverse functions of the linc complexes based on the structure. Cells, 6:3, Jan 2017. URL: https://doi.org/10.3390/cells6010003, doi:10.3390/cells6010003. This article has 57 citations.

16. (mcgillivary2023buildingandbreaking pages 3-4): Rebecca M. McGillivary, Daniel A. Starr, and G.W. Gant Luxton. Building and breaking mechanical bridges between the nucleus and cytoskeleton: regulation of linc complex assembly and disassembly. Current Opinion in Cell Biology, 85:102260, Dec 2023. URL: https://doi.org/10.1016/j.ceb.2023.102260, doi:10.1016/j.ceb.2023.102260. This article has 46 citations and is from a peer-reviewed journal.

17. (goncalves2020nesprin2recruitmentof pages 1-4): João Carlos Gonçalves, Sebastian Quintremil, Julie Yi, and Richard B. Vallee. Nesprin-2 recruitment of bicd2 to the nuclear envelope controls dynein/kinesin-mediated neuronal migration in vivo. Current Biology, 30:3116-3129.e4, Aug 2020. URL: https://doi.org/10.1016/j.cub.2020.05.091, doi:10.1016/j.cub.2020.05.091. This article has 87 citations and is from a highest quality peer-reviewed journal.

18. (pereira2019nuclearenvelopedynamics pages 13-14): Cátia D. Pereira, Joana B. Serrano, Filipa Martins, Odete A. B. da Cruz e Silva, and Sandra Rebelo. Nuclear envelope dynamics during mammalian spermatogenesis: new insights on male fertility. Biological Reviews, 94:1195-1219, Aug 2019. URL: https://doi.org/10.1111/brv.12498, doi:10.1111/brv.12498. This article has 62 citations and is from a domain leading peer-reviewed journal.

19. (kuwako2024diverserolesof pages 2-5): Ken-ichiro Kuwako and Sadafumi Suzuki. Diverse roles of the linc complex in cellular function and disease in the nervous system. International Journal of Molecular Sciences, 25:11525, Oct 2024. URL: https://doi.org/10.3390/ijms252111525, doi:10.3390/ijms252111525. This article has 5 citations.

20. (zhang2021sun5interactingwith pages 1-2): Yunfei Zhang, Linfei Yang, Lihua Huang, Gang Liu, Xinmin Nie, Xinxing Zhang, and Xiaowei Xing. Sun5 interacting with nesprin3 plays an essential role in sperm head-to-tail linkage: research on sun5 gene knockout mice. Frontiers in Cell and Developmental Biology, Jun 2021. URL: https://doi.org/10.3389/fcell.2021.684826, doi:10.3389/fcell.2021.684826. This article has 39 citations.

21. (hao2019sunkashinteractionsfacilitate pages 9-12): Hongyan Hao and Daniel A. Starr. Sun/kash interactions facilitate force transmission across the nuclear envelope. Nucleus, 10:73-80, Jan 2019. URL: https://doi.org/10.1080/19491034.2019.1595313, doi:10.1080/19491034.2019.1595313. This article has 69 citations and is from a peer-reviewed journal.

22. (hao2019sunkashinteractionsfacilitate pages 1-5): Hongyan Hao and Daniel A. Starr. Sun/kash interactions facilitate force transmission across the nuclear envelope. Nucleus, 10:73-80, Jan 2019. URL: https://doi.org/10.1080/19491034.2019.1595313, doi:10.1080/19491034.2019.1595313. This article has 69 citations and is from a peer-reviewed journal.

23. (saunders2017torsinacontrolstan pages 1-2): Cosmo A. Saunders, Nathan J. Harris, Patrick T. Willey, Brian M. Woolums, Yuexia Wang, Alex J. McQuown, Amy Schoenhofen, Howard J. Worman, William T. Dauer, Gregg G. Gundersen, and G.W. Gant Luxton. Torsina controls tan line assembly and the retrograde flow of dorsal perinuclear actin cables during rearward nuclear movement. The Journal of Cell Biology, 216:657-674, Mar 2017. URL: https://doi.org/10.1083/jcb.201507113, doi:10.1083/jcb.201507113. This article has 85 citations.

24. (shang2017essentialrolefor pages 1-2): Yongliang Shang, Fuxi Zhu, Lina Wang, Ying-Chun Ouyang, Ming-Zhe Dong, Chao Liu, Haichao Zhao, Xiuhong Cui, Dongyuan Ma, Zhiguo Zhang, Xiaoyu Yang, Yueshuai Guo, Feng Liu, Li Yuan, Fei Gao, Xuejiang Guo, Qing-Yuan Sun, Yunxia Cao, and Wei Li. Essential role for sun5 in anchoring sperm head to the tail. eLife, Sep 2017. URL: https://doi.org/10.7554/elife.28199, doi:10.7554/elife.28199. This article has 143 citations and is from a domain leading peer-reviewed journal.

25. (kmonickova2020theroleof pages 12-15): Vera Kmonickova, Michaela Frolikova, Klaus Steger, and Katerina Komrskova. The role of the linc complex in sperm development and function. International Journal of Molecular Sciences, 21:9058, Nov 2020. URL: https://doi.org/10.3390/ijms21239058, doi:10.3390/ijms21239058. This article has 44 citations.

26. (saunders2016lincingdefectivenuclearcytoskeletal pages 6-7): Cosmo A. Saunders and G. W. Gant Luxton. Lincing defective nuclear-cytoskeletal coupling and dyt1 dystonia. Cellular and Molecular Bioengineering, 9:207-216, Feb 2016. URL: https://doi.org/10.1007/s12195-016-0432-0, doi:10.1007/s12195-016-0432-0. This article has 21 citations and is from a peer-reviewed journal.

27. (saunders2016lincingdefectivenuclearcytoskeletal pages 3-4): Cosmo A. Saunders and G. W. Gant Luxton. Lincing defective nuclear-cytoskeletal coupling and dyt1 dystonia. Cellular and Molecular Bioengineering, 9:207-216, Feb 2016. URL: https://doi.org/10.1007/s12195-016-0432-0, doi:10.1007/s12195-016-0432-0. This article has 21 citations and is from a peer-reviewed journal.

28. (koreny2016ancienteukaryoticorigin pages 5-7): Ludek Koreny and Mark C. Field. Ancient eukaryotic origin and evolutionary plasticity of nuclear lamina. Genome Biology and Evolution, 8:2663-2671, Apr 2016. URL: https://doi.org/10.1093/gbe/evw087, doi:10.1093/gbe/evw087. This article has 88 citations and is from a domain leading peer-reviewed journal.

29. (koreny2016ancienteukaryoticorigin pages 7-8): Ludek Koreny and Mark C. Field. Ancient eukaryotic origin and evolutionary plasticity of nuclear lamina. Genome Biology and Evolution, 8:2663-2671, Apr 2016. URL: https://doi.org/10.1093/gbe/evw087, doi:10.1093/gbe/evw087. This article has 88 citations and is from a domain leading peer-reviewed journal.

30. (yuan2021evolutionandfunctional pages 1-2): Li Yuan, Jingwen Pan, Shouhong Zhu, Yan Li, Jinbo Yao, Qiulin Li, Shengtao Fang, Chunyan Liu, Xinyu Wang, Bei Li, Wei Chen, and Yongshan Zhang. Evolution and functional divergence of sun genes in plants. Frontiers in Plant Science, Mar 2021. URL: https://doi.org/10.3389/fpls.2021.646622, doi:10.3389/fpls.2021.646622. This article has 10 citations.

31. (poulet2017exploringtheevolution pages 11-15): Axel Poulet, Aline V. Probst, Katja Graumann, Christophe Tatout, and David Evans. Exploring the evolution of the proteins of the plant nuclear envelope. Nucleus, 8:46-59, Jan 2017. URL: https://doi.org/10.1080/19491034.2016.1236166, doi:10.1080/19491034.2016.1236166. This article has 65 citations and is from a peer-reviewed journal.

32. (zhou2013howplantslinc pages 1-2): Xiao Zhou and Iris Meier. How plants linc the sun to kash. Nucleus, 4:206-215, May 2013. URL: https://doi.org/10.4161/nucl.24088, doi:10.4161/nucl.24088. This article has 65 citations and is from a peer-reviewed journal.

33. (kmonickova2020theroleof pages 1-4): Vera Kmonickova, Michaela Frolikova, Klaus Steger, and Katerina Komrskova. The role of the linc complex in sperm development and function. International Journal of Molecular Sciences, 21:9058, Nov 2020. URL: https://doi.org/10.3390/ijms21239058, doi:10.3390/ijms21239058. This article has 44 citations.

34. (storey2022genotypephenotypecorrelationsin pages 11-13): Emily C. Storey and Heidi R. Fuller. Genotype-phenotype correlations in human diseases caused by mutations of linc complex-associated genes: a systematic review and meta-summary. Cells, 11:4065, Dec 2022. URL: https://doi.org/10.3390/cells11244065, doi:10.3390/cells11244065. This article has 33 citations.

35. (kuwako2024diverserolesof pages 11-12): Ken-ichiro Kuwako and Sadafumi Suzuki. Diverse roles of the linc complex in cellular function and disease in the nervous system. International Journal of Molecular Sciences, 25:11525, Oct 2024. URL: https://doi.org/10.3390/ijms252111525, doi:10.3390/ijms252111525. This article has 5 citations.

36. (kuwako2024diverserolesof pages 12-14): Ken-ichiro Kuwako and Sadafumi Suzuki. Diverse roles of the linc complex in cellular function and disease in the nervous system. International Journal of Molecular Sciences, 25:11525, Oct 2024. URL: https://doi.org/10.3390/ijms252111525, doi:10.3390/ijms252111525. This article has 5 citations.

37. (kuwako2024diverserolesof pages 14-15): Ken-ichiro Kuwako and Sadafumi Suzuki. Diverse roles of the linc complex in cellular function and disease in the nervous system. International Journal of Molecular Sciences, 25:11525, Oct 2024. URL: https://doi.org/10.3390/ijms252111525, doi:10.3390/ijms252111525. This article has 5 citations.

38. (saunders2016lincingdefectivenuclearcytoskeletal pages 7-9): Cosmo A. Saunders and G. W. Gant Luxton. Lincing defective nuclear-cytoskeletal coupling and dyt1 dystonia. Cellular and Molecular Bioengineering, 9:207-216, Feb 2016. URL: https://doi.org/10.1007/s12195-016-0432-0, doi:10.1007/s12195-016-0432-0. This article has 21 citations and is from a peer-reviewed journal.

39. (storey2022genotypephenotypecorrelationsin pages 15-16): Emily C. Storey and Heidi R. Fuller. Genotype-phenotype correlations in human diseases caused by mutations of linc complex-associated genes: a systematic review and meta-summary. Cells, 11:4065, Dec 2022. URL: https://doi.org/10.3390/cells11244065, doi:10.3390/cells11244065. This article has 33 citations.

40. (padillamejia2021evolutionanddiversification pages 1-3): Norma E. Padilla-Mejia, Alexandr A. Makarov, Lael D. Barlow, Erin R. Butterfield, and Mark C. Field. Evolution and diversification of the nuclear envelope. Nucleus, 12:21-41, Jan 2021. URL: https://doi.org/10.1080/19491034.2021.1874135, doi:10.1080/19491034.2021.1874135. This article has 15 citations and is from a peer-reviewed journal.

41. (gurusaran2021amolecularmechanism pages 1-5): Manickam Gurusaran and Owen R. Davies. A molecular mechanism for linc complex branching by structurally diverse sun-kash 6:6 assemblies. BioRxiv, Mar 2021. URL: https://doi.org/10.1101/2020.03.21.001867, doi:10.1101/2020.03.21.001867. This article has 63 citations.

## Artifacts

- [Edison artifact artifact-00](linc_complex-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. sharma2023disulfidebondin pages 1-2
2. mcgillivary2023buildingandbreaking pages 3-4
3. saunders2017torsinacontrolstan pages 1-2
4. yuan2021evolutionandfunctional pages 1-2
5. storey2022genotypephenotypecorrelationsin pages 11-13
6. shang2017essentialrolefor pages 1-2
7. cain2018conservedsunkashinterfaces pages 1-3
8. sosa2012linccomplexesform pages 1-2
9. mcgillivary2023buildingandbreaking pages 1-3
10. gurusaran2021amolecularmechanism pages 12-15
11. sosa2012linccomplexesform pages 2-4
12. gurusaran2021amolecularmechanism pages 9-12
13. luxton2014kashingupwith pages 3-4
14. saunders2017torsinacontrolstan pages 11-12
15. hieda2017implicationsfordiverse pages 1-3
16. pereira2019nuclearenvelopedynamics pages 13-14
17. kuwako2024diverserolesof pages 2-5
18. hao2019sunkashinteractionsfacilitate pages 9-12
19. hao2019sunkashinteractionsfacilitate pages 1-5
20. kmonickova2020theroleof pages 12-15
21. saunders2016lincingdefectivenuclearcytoskeletal pages 6-7
22. saunders2016lincingdefectivenuclearcytoskeletal pages 3-4
23. koreny2016ancienteukaryoticorigin pages 5-7
24. koreny2016ancienteukaryoticorigin pages 7-8
25. poulet2017exploringtheevolution pages 11-15
26. zhou2013howplantslinc pages 1-2
27. kmonickova2020theroleof pages 1-4
28. kuwako2024diverserolesof pages 11-12
29. kuwako2024diverserolesof pages 12-14
30. kuwako2024diverserolesof pages 14-15
31. saunders2016lincingdefectivenuclearcytoskeletal pages 7-9
32. storey2022genotypephenotypecorrelationsin pages 15-16
33. padillamejia2021evolutionanddiversification pages 1-3
34. gurusaran2021amolecularmechanism pages 1-5
35. 10.1016/j.cell.2012.03.046
36. 10.1016/j.cub.2018.08.001
37. 10.1101/2020.03.21.001867
38. 10.1016/j.ceb.2023.102260
39. 10.26508/lsa.202302031
40. 10.1083/jcb.202405032
41. 10.1093/hmg/ddac179
42. 10.3390/ijms252111525
43. 10.3389/fcell.2022.974168
44. 10.1083/jcb.201507113
45. 10.7554/eLife.28199
46. 10.3390/cells11244065
47. 10.1371/journal.pone.0307816
48. https://doi.org/10.1016/j.cell.2012.03.046
49. https://doi.org/10.1016/j.cub.2018.08.001
50. https://doi.org/10.1101/2020.03.21.001867
51. https://doi.org/10.1016/j.ceb.2023.102260
52. https://doi.org/10.26508/lsa.202302031
53. https://doi.org/10.1083/jcb.202405032
54. https://doi.org/10.1093/hmg/ddac179
55. https://doi.org/10.3390/ijms252111525
56. https://doi.org/10.3389/fcell.2022.974168
57. https://doi.org/10.1083/jcb.201507113
58. https://doi.org/10.7554/eLife.28199
59. https://doi.org/10.3390/cells11244065
60. https://doi.org/10.1371/journal.pone.0307816
61. https://doi.org/10.1016/j.cub.2018.08.001,
62. https://doi.org/10.1016/j.cell.2012.03.046,
63. https://doi.org/10.1016/j.ceb.2023.102260,
64. https://doi.org/10.1101/2020.03.21.001867,
65. https://doi.org/10.1091/mbc.e13-02-0100,
66. https://doi.org/10.1083/jcb.202405032,
67. https://doi.org/10.1016/j.ceb.2014.03.002,
68. https://doi.org/10.3389/fcell.2022.974168,
69. https://doi.org/10.1083/jcb.201507113,
70. https://doi.org/10.26508/lsa.202302031,
71. https://doi.org/10.1093/hmg/ddac179,
72. https://doi.org/10.1371/journal.pone.0307816,
73. https://doi.org/10.3390/cells6010003,
74. https://doi.org/10.1016/j.cub.2020.05.091,
75. https://doi.org/10.1111/brv.12498,
76. https://doi.org/10.3390/ijms252111525,
77. https://doi.org/10.3389/fcell.2021.684826,
78. https://doi.org/10.1080/19491034.2019.1595313,
79. https://doi.org/10.7554/elife.28199,
80. https://doi.org/10.3390/ijms21239058,
81. https://doi.org/10.1007/s12195-016-0432-0,
82. https://doi.org/10.1093/gbe/evw087,
83. https://doi.org/10.3389/fpls.2021.646622,
84. https://doi.org/10.1080/19491034.2016.1236166,
85. https://doi.org/10.4161/nucl.24088,
86. https://doi.org/10.3390/cells11244065,
87. https://doi.org/10.1080/19491034.2021.1874135,