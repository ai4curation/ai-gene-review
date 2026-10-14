---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-27T15:38:30.938472'
end_time: '2026-09-27T15:49:48.437416'
duration_seconds: 677.5
template_file: templates/module_research.md.j2
template_variables:
  module_title: Nucleokinesis (motor-driven nuclear translocation) module
  module_summary: 'Nucleokinesis is the directed translocation of the nucleus within
    a cell that is migrating or changing shape, most prominently in migrating neurons
    and in the interkinetic nuclear migration of neuroepithelial and radial glial
    progenitors. In migrating neurons it follows a two-stroke cycle: the centrosome
    and Golgi first advance into a swelling of the leading process, and the nucleus
    then moves forward toward them in a saltatory step. The nucleus is coupled to
    cytoplasmic motors through its envelope, either by LINC complexes (inner-nuclear-membrane
    SUN proteins bound to outer-nuclear-membrane KASH nesprins) or, in G2 radial glial
    progenitors, by nuclear-pore-anchored dynein adaptors (RANBP2-BICD2 and NUP133-CENPF-NDE1/NDEL1).
    Cytoplasmic dynein, with dynactin and the LIS1-NDEL1/NDE1 regulatory module, pulls
    the nucleus toward microtubule minus ends at the centrosome along a perinuclear
    microtubule cage stabilized by doublecortin. Non-muscle myosin II contraction
    at the rear of the soma assists forward nuclear movement, and in progenitors the
    kinesin-3 KIF1A drives the opposite, basally directed nuclear movement. CDK5/p35
    phosphorylation of NDEL1 links the core machinery to migration signaling. Loss
    of LIS1 or DCX causes lissencephaly, reflecting the dependence of cortical neuronal
    migration on this machinery.'
  module_outline: "- Nucleokinesis\n  - 1. coupling the nucleus to cytoskeletal motors\
    \ at the nuclear envelope\n  - Nuclear-envelope motor coupling\n    - Alternative\
    \ versions by nuclear-envelope anchor (LINC complex vs nuclear pore complex):\
    \ Nuclear-envelope motor anchoring route\n      - LINC complex (SUN-KASH) coupling\n\
    \        - SUN-domain inner nuclear membrane anchor (molecular player: SUN-domain\
    \ proteins (SUN1, SUN2); activity or role: cytoskeleton-nuclear membrane anchor\
    \ activity)\n        - KASH-domain nesprin outer nuclear membrane motor adaptor\
    \ (molecular player: KASH-domain nesprins (nesprin-1, nesprin-2); activity or\
    \ role: cytoskeleton-nuclear membrane anchor activity)\n      - Nuclear-pore dynein\
    \ recruitment (G2 progenitors)\n        - BICD2 nuclear-pore dynein adaptor (molecular\
    \ player: BICD2; activity or role: cytoskeletal adaptor activity)\n        - CENPF\
    \ nuclear-pore NDE1/NDEL1 recruiter (molecular player: CENPF; activity or role:\
    \ dynein complex binding)\n  - 2. minus-end-directed force generation pulling\
    \ the nucleus toward the centrosome\n  - Dynein-dynactin-LIS1-NDEL1 nuclear motor\n\
    \    - Cytoplasmic dynein-1 motor with LIS1/NDEL1 regulators (molecular player:\
    \ cytoplasmic dynein-1 with dynactin, LIS1 and NDEL1/NDE1; activity or role: minus-end-directed\
    \ microtubule motor activity)\n  - 3. perinuclear microtubule track linking the\
    \ nucleus to the centrosome\n  - DCX-stabilized perinuclear microtubule cage\n\
    \    - Doublecortin perinuclear microtubule stabilizer (molecular player: DCX\
    \ (doublecortin); activity or role: microtubule binding)\n  - 4. actomyosin contraction\
    \ at the rear of the soma assisting forward nuclear movement\n  - Rear actomyosin\
    \ contraction\n    - Non-muscle myosin II rear contraction (molecular player:\
    \ non-muscle myosin II heavy chains; activity or role: microfilament motor activity)\n\
    \  - 5. plus-end-directed (basal) nuclear transport in interkinetic nuclear migration\n\
    \  - Kinesin-3 basal nuclear transport\n    - KIF1A plus-end nuclear motor (molecular\
    \ player: KIF1A; activity or role: plus-end-directed microtubule motor activity)\n\
    \  - 6. CDK5/p35 phosphorylation of NDEL1 linking migration signaling to the dynein\
    \ machinery\n  - CDK5/p35 regulation of NDEL1\n    - CDK5/p35 kinase (molecular\
    \ player: CDK5-p35 kinase complex; activity or role: protein serine/threonine\
    \ kinase activity)"
  module_connections: '- Nuclear-envelope motor coupling feeds into Dynein-dynactin-LIS1-NDEL1
    nuclear motor: Envelope anchors (nesprin-2, BICD2, CENPF-NDE1/NDEL1) attach dynein
    to the nucleus, so that minus-end motility is converted into nuclear translocation.

    - DCX-stabilized perinuclear microtubule cage feeds into Dynein-dynactin-LIS1-NDEL1
    nuclear motor: The DCX-stabilized, centrosome-anchored microtubule cage is the
    track along which dynein pulls the nucleus.

    - Nuclear-envelope motor coupling feeds into Kinesin-3 basal nuclear transport:
    Basal movement also requires the motor to be attached to the nucleus. Nesprin-2
    binds kinesin as well as dynein, but whether KIF1A itself is anchored through
    the LINC complex has not been established.

    - CDK5/p35 regulation of NDEL1 connects to Dynein-dynactin-LIS1-NDEL1 nuclear
    motor: CDK5/p35 phosphorylates NDEL1 within the LIS1-NDEL1-dynein module; direction
    of effect not asserted.'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 45
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: nucleokinesis-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Commissioned Review Brief

## Review Topic

Nucleokinesis (motor-driven nuclear translocation) module

## Working Scope

Nucleokinesis is the directed translocation of the nucleus within a cell that is migrating or changing shape, most prominently in migrating neurons and in the interkinetic nuclear migration of neuroepithelial and radial glial progenitors. In migrating neurons it follows a two-stroke cycle: the centrosome and Golgi first advance into a swelling of the leading process, and the nucleus then moves forward toward them in a saltatory step. The nucleus is coupled to cytoplasmic motors through its envelope, either by LINC complexes (inner-nuclear-membrane SUN proteins bound to outer-nuclear-membrane KASH nesprins) or, in G2 radial glial progenitors, by nuclear-pore-anchored dynein adaptors (RANBP2-BICD2 and NUP133-CENPF-NDE1/NDEL1). Cytoplasmic dynein, with dynactin and the LIS1-NDEL1/NDE1 regulatory module, pulls the nucleus toward microtubule minus ends at the centrosome along a perinuclear microtubule cage stabilized by doublecortin. Non-muscle myosin II contraction at the rear of the soma assists forward nuclear movement, and in progenitors the kinesin-3 KIF1A drives the opposite, basally directed nuclear movement. CDK5/p35 phosphorylation of NDEL1 links the core machinery to migration signaling. Loss of LIS1 or DCX causes lissencephaly, reflecting the dependence of cortical neuronal migration on this machinery.

## Provisional Biological Outline

- Nucleokinesis
  - 1. coupling the nucleus to cytoskeletal motors at the nuclear envelope
  - Nuclear-envelope motor coupling
    - Alternative versions by nuclear-envelope anchor (LINC complex vs nuclear pore complex): Nuclear-envelope motor anchoring route
      - LINC complex (SUN-KASH) coupling
        - SUN-domain inner nuclear membrane anchor (molecular player: SUN-domain proteins (SUN1, SUN2); activity or role: cytoskeleton-nuclear membrane anchor activity)
        - KASH-domain nesprin outer nuclear membrane motor adaptor (molecular player: KASH-domain nesprins (nesprin-1, nesprin-2); activity or role: cytoskeleton-nuclear membrane anchor activity)
      - Nuclear-pore dynein recruitment (G2 progenitors)
        - BICD2 nuclear-pore dynein adaptor (molecular player: BICD2; activity or role: cytoskeletal adaptor activity)
        - CENPF nuclear-pore NDE1/NDEL1 recruiter (molecular player: CENPF; activity or role: dynein complex binding)
  - 2. minus-end-directed force generation pulling the nucleus toward the centrosome
  - Dynein-dynactin-LIS1-NDEL1 nuclear motor
    - Cytoplasmic dynein-1 motor with LIS1/NDEL1 regulators (molecular player: cytoplasmic dynein-1 with dynactin, LIS1 and NDEL1/NDE1; activity or role: minus-end-directed microtubule motor activity)
  - 3. perinuclear microtubule track linking the nucleus to the centrosome
  - DCX-stabilized perinuclear microtubule cage
    - Doublecortin perinuclear microtubule stabilizer (molecular player: DCX (doublecortin); activity or role: microtubule binding)
  - 4. actomyosin contraction at the rear of the soma assisting forward nuclear movement
  - Rear actomyosin contraction
    - Non-muscle myosin II rear contraction (molecular player: non-muscle myosin II heavy chains; activity or role: microfilament motor activity)
  - 5. plus-end-directed (basal) nuclear transport in interkinetic nuclear migration
  - Kinesin-3 basal nuclear transport
    - KIF1A plus-end nuclear motor (molecular player: KIF1A; activity or role: plus-end-directed microtubule motor activity)
  - 6. CDK5/p35 phosphorylation of NDEL1 linking migration signaling to the dynein machinery
  - CDK5/p35 regulation of NDEL1
    - CDK5/p35 kinase (molecular player: CDK5-p35 kinase complex; activity or role: protein serine/threonine kinase activity)

## Known Relationships Among Steps

- Nuclear-envelope motor coupling feeds into Dynein-dynactin-LIS1-NDEL1 nuclear motor: Envelope anchors (nesprin-2, BICD2, CENPF-NDE1/NDEL1) attach dynein to the nucleus, so that minus-end motility is converted into nuclear translocation.
- DCX-stabilized perinuclear microtubule cage feeds into Dynein-dynactin-LIS1-NDEL1 nuclear motor: The DCX-stabilized, centrosome-anchored microtubule cage is the track along which dynein pulls the nucleus.
- Nuclear-envelope motor coupling feeds into Kinesin-3 basal nuclear transport: Basal movement also requires the motor to be attached to the nucleus. Nesprin-2 binds kinesin as well as dynein, but whether KIF1A itself is anchored through the LINC complex has not been established.
- CDK5/p35 regulation of NDEL1 connects to Dynein-dynactin-LIS1-NDEL1 nuclear motor: CDK5/p35 phosphorylates NDEL1 within the LIS1-NDEL1-dynein module; direction of effect not asserted.

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

Nucleokinesis (motor-driven nuclear translocation) module

## Working Scope

Nucleokinesis is the directed translocation of the nucleus within a cell that is migrating or changing shape, most prominently in migrating neurons and in the interkinetic nuclear migration of neuroepithelial and radial glial progenitors. In migrating neurons it follows a two-stroke cycle: the centrosome and Golgi first advance into a swelling of the leading process, and the nucleus then moves forward toward them in a saltatory step. The nucleus is coupled to cytoplasmic motors through its envelope, either by LINC complexes (inner-nuclear-membrane SUN proteins bound to outer-nuclear-membrane KASH nesprins) or, in G2 radial glial progenitors, by nuclear-pore-anchored dynein adaptors (RANBP2-BICD2 and NUP133-CENPF-NDE1/NDEL1). Cytoplasmic dynein, with dynactin and the LIS1-NDEL1/NDE1 regulatory module, pulls the nucleus toward microtubule minus ends at the centrosome along a perinuclear microtubule cage stabilized by doublecortin. Non-muscle myosin II contraction at the rear of the soma assists forward nuclear movement, and in progenitors the kinesin-3 KIF1A drives the opposite, basally directed nuclear movement. CDK5/p35 phosphorylation of NDEL1 links the core machinery to migration signaling. Loss of LIS1 or DCX causes lissencephaly, reflecting the dependence of cortical neuronal migration on this machinery.

## Provisional Biological Outline

- Nucleokinesis
  - 1. coupling the nucleus to cytoskeletal motors at the nuclear envelope
  - Nuclear-envelope motor coupling
    - Alternative versions by nuclear-envelope anchor (LINC complex vs nuclear pore complex): Nuclear-envelope motor anchoring route
      - LINC complex (SUN-KASH) coupling
        - SUN-domain inner nuclear membrane anchor (molecular player: SUN-domain proteins (SUN1, SUN2); activity or role: cytoskeleton-nuclear membrane anchor activity)
        - KASH-domain nesprin outer nuclear membrane motor adaptor (molecular player: KASH-domain nesprins (nesprin-1, nesprin-2); activity or role: cytoskeleton-nuclear membrane anchor activity)
      - Nuclear-pore dynein recruitment (G2 progenitors)
        - BICD2 nuclear-pore dynein adaptor (molecular player: BICD2; activity or role: cytoskeletal adaptor activity)
        - CENPF nuclear-pore NDE1/NDEL1 recruiter (molecular player: CENPF; activity or role: dynein complex binding)
  - 2. minus-end-directed force generation pulling the nucleus toward the centrosome
  - Dynein-dynactin-LIS1-NDEL1 nuclear motor
    - Cytoplasmic dynein-1 motor with LIS1/NDEL1 regulators (molecular player: cytoplasmic dynein-1 with dynactin, LIS1 and NDEL1/NDE1; activity or role: minus-end-directed microtubule motor activity)
  - 3. perinuclear microtubule track linking the nucleus to the centrosome
  - DCX-stabilized perinuclear microtubule cage
    - Doublecortin perinuclear microtubule stabilizer (molecular player: DCX (doublecortin); activity or role: microtubule binding)
  - 4. actomyosin contraction at the rear of the soma assisting forward nuclear movement
  - Rear actomyosin contraction
    - Non-muscle myosin II rear contraction (molecular player: non-muscle myosin II heavy chains; activity or role: microfilament motor activity)
  - 5. plus-end-directed (basal) nuclear transport in interkinetic nuclear migration
  - Kinesin-3 basal nuclear transport
    - KIF1A plus-end nuclear motor (molecular player: KIF1A; activity or role: plus-end-directed microtubule motor activity)
  - 6. CDK5/p35 phosphorylation of NDEL1 linking migration signaling to the dynein machinery
  - CDK5/p35 regulation of NDEL1
    - CDK5/p35 kinase (molecular player: CDK5-p35 kinase complex; activity or role: protein serine/threonine kinase activity)

## Known Relationships Among Steps

- Nuclear-envelope motor coupling feeds into Dynein-dynactin-LIS1-NDEL1 nuclear motor: Envelope anchors (nesprin-2, BICD2, CENPF-NDE1/NDEL1) attach dynein to the nucleus, so that minus-end motility is converted into nuclear translocation.
- DCX-stabilized perinuclear microtubule cage feeds into Dynein-dynactin-LIS1-NDEL1 nuclear motor: The DCX-stabilized, centrosome-anchored microtubule cage is the track along which dynein pulls the nucleus.
- Nuclear-envelope motor coupling feeds into Kinesin-3 basal nuclear transport: Basal movement also requires the motor to be attached to the nucleus. Nesprin-2 binds kinesin as well as dynein, but whether KIF1A itself is anchored through the LINC complex has not been established.
- CDK5/p35 regulation of NDEL1 connects to Dynein-dynactin-LIS1-NDEL1 nuclear motor: CDK5/p35 phosphorylates NDEL1 within the LIS1-NDEL1-dynein module; direction of effect not asserted.

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

# Nucleokinesis: a motor-driven nuclear-translocation module

## 1. Executive summary

Nucleokinesis is the **directed displacement of the nucleus within a cell**, usually as part of migration, morphogenesis, or cell-cycle-coupled nuclear positioning. In migrating neurons it is best understood as the nuclear/somal stroke within a saltatory cycle: a leading-process swelling forms, the centrosome and Golgi advance, and the nucleus and soma subsequently move toward that anterior compartment. In interkinetic nuclear migration (INM), by contrast, an elongated neuroepithelial or radial-glial progenitor remains in place while its nucleus moves basally during G1 and apically during G2. Thus, neuronal nucleokinesis and INM use overlapping motors but are not the same cellular program. Migrating human cortical neurons may travel approximately 2 cm, whereas retinal neurons migrate roughly 50–100 μm, illustrating the very different scales over which the module operates. (tsai2005nucleokinesisinneuronal pages 1-2)

The best-supported core is a **nuclear-envelope anchor–microtubule motor–polarized track** system. Postmitotic cortical neurons predominantly use SUN–KASH LINC complexes, especially Nesprin-2 linked through BICD2 to dynein and kinesin. G2 radial-glial progenitors instead recruit dynein to nuclear pores through sequential RanBP2–BICD2 and NUP133–CENP-F–NDE1/NDEL1 pathways. Dynein–dynactin, regulated by LIS1 and NDE1/NDEL1, provides minus-end-directed force; DCX-associated perinuclear microtubules provide mechanically coherent tracks; and rear non-muscle myosin-II contraction can assist movement in some neuronal and neuroepithelial settings. KIF1A drives the opposite, plus-end-directed basal phase of INM. (doobin2024theroleof pages 1-3, hu2013dyneinrecruitmentto pages 1-2, goncalves2020nesprin2recruitmentof pages 1-4, tanaka2004lis1anddoublecortin pages 1-2)

Three qualifications are essential. First, the centrosome is often an anterior organizer and directional landmark, but nuclear movement need not be mechanically caused by centrosome movement: disrupting Nesprin-2–BICD2 can stop the nucleus while centrosome advance continues. Second, actomyosin is context-dependent rather than universally obligatory. Third, CDK5/p35 phosphorylation of NDEL1/NDE1 links migration signaling to dynein regulation, but the direction and consequence of phosphorylation vary with residue, cell-cycle state, and cargo; it should not be described simply as a universal dynein “on switch.” (doobin2024theroleof pages 8-10, hu2013dyneinrecruitmentto pages 8-10, goncalves2020nesprin2recruitmentof pages 1-4, goncalves2020nesprin2recruitmentof pages 9-12)

Recent work has refined regulation rather than displaced this model. A 2023 study showed that sequential CDK1/PLK1 phosphorylation activates BICD2 and promotes its G2 association with phosphorylated RanBP2. A 2024 NDE1 study identified T215 and T243 as necessary for apical INM and reported that the schizophrenia-associated S214F variant selectively impairs adjacent CDK5-dependent phosphorylation and alters cortical lamination. A 2024 nervous-system LINC review emphasizes extensive isoform and cell-type diversity, reinforcing that “the LINC complex” is not one invariant assembly. (doobin2024theroleof pages 1-3, doobin2024theroleof pages 8-10, kuwako2024diverserolesof pages 1-2, kuwako2024diverserolesof pages 5-6)

## 2. Definition and biological boundaries

### Operational definition

A useful narrow definition is: **active, directional translocation of the intact nucleus, produced by cytoskeletal force transmitted directly or indirectly to the nuclear surface**. “Nuclear migration” is often used more broadly to include anchorage, rotation, passive displacement, pronuclear congression, myonuclear spreading, or meiotic chromosome-led nuclear-envelope movements. “Nucleokinesis” is commonly narrower in neurobiology, denoting the saltatory movement of the nucleus and soma following leading-process or centrosome advance. Some authors nevertheless apply it to INM and to nuclear movement in non-neural migrating cells; terminology is therefore contextual rather than fully standardized. (tsai2005nucleokinesisinneuronal pages 1-2, bone2016nuclearmigrationevents pages 1-2)

### Included processes

* The nuclear/somal stroke of radial, tangential, and glia-guided neuronal migration.
* Basal and apical INM in pseudostratified neural epithelia and radial glia.
* Nuclear-envelope coupling, motor activation, polarized microtubule tracks, nucleus–centrosome mechanical coordination, and accessory actomyosin force insofar as these directly move the nucleus.

### Adjacent processes that should remain analytically separate

1. **Leading-process extension and guidance.** Adhesion, Rac/Rho signaling, membrane trafficking, growth-cone behavior, and extracellular guidance determine where a neuron goes, but are not themselves nucleokinesis unless they generate or transmit nuclear force.
2. **Centrosome/Golgi advance.** This is the first stroke in the canonical neuronal cycle and establishes geometry for the second stroke, but it is not synonymous with nuclear movement.
3. **Whole-cell migration and terminal somal translocation.** These include adhesion turnover, trailing-process retraction, and tissue interactions beyond the nuclear module.
4. **Mitosis, spindle assembly, and nuclear-envelope breakdown (NEBD).** The same dynein–LIS1–NDE1/NDEL1 machinery contributes to these processes, but they are downstream or parallel functions. In RGPs, successful apical INM is a prerequisite for mitotic entry, creating a causal connection without making mitosis part of nucleokinesis. (hebbar2008lis1andndel1 pages 1-2, hu2013dyneinrecruitmentto pages 8-10)
5. **Mechanotransduction and chromatin organization.** LINC complexes also transmit force to lamins and chromatin, regulate differentiation, and mediate trafficking. These are biologically relevant consequences or additional functions, not necessarily force-producing steps in nuclear translocation. (kuwako2024diverserolesof pages 10-11, kuwako2024diverserolesof pages 1-2)
6. **Passive crowding or hydraulic displacement.** Nuclear movement can result from neighboring-cell pressure or intracellular pressure in other systems. Such movements belong to broad nuclear positioning but not necessarily to the motor-driven module reviewed here. (bone2016nuclearmigrationevents pages 1-2)

## 3. Mechanistic overview

### 3.1 Postmitotic migrating neurons: a two-stroke cycle

The canonical sequence is:

1. **Polarity and leading-process dilation.** A swelling forms proximal to the leading process.
2. **Centrosome/Golgi advance.** The centrosome and Golgi move into this swelling. Microtubules project anteriorly and wrap around the nucleus in fork- or cage-like arrays.
3. **Nuclear-envelope engagement.** In cortical neurons, SUN proteins in the inner nuclear membrane bind KASH-domain Nesprin-2 in the outer membrane. Nesprin-2 recruits BICD2 and associated microtubule motors.
4. **Nuclear stroke.** Dynein–dynactin moves toward anteriorly located microtubule minus ends. LIS1 and NDE1/NDEL1 regulate formation, localization, and load-bearing behavior of the motor assembly. The nucleus deforms and advances.
5. **Accessory force and reset.** Rear non-muscle myosin II may contract behind the soma, while the trailing process retracts and adhesions are remodeled. The cycle then repeats. (tsai2005nucleokinesisinneuronal pages 1-2, goncalves2020nesprin2recruitmentof pages 1-4, goncalves2020nesprin2recruitmentof pages 9-12, tanaka2004lis1anddoublecortin pages 1-2)

The ordering is robust, but a rigid “centrosome pulls nucleus” model is too simple. Nesprin-2/BICD2 disruption severely inhibited nuclear movement while centrosome advance continued, showing that the two strokes can be mechanically uncoupled. The centrosome organizes track polarity and commonly precedes the nucleus, but direct nuclear-envelope motor engagement is sufficient to explain much of the nuclear stroke. (goncalves2020nesprin2recruitmentof pages 1-4)

### 3.2 Radial-glial progenitors: bidirectional INM

RGP centrosomes remain near the ventricular/apical end, and microtubules are predominantly minus-end-apical and plus-end-basal. During G1, KIF1A carries the nucleus basally along plus-end-oriented tracks. During G2, cytoplasmic dynein returns it apically. The two directions are therefore different motor programs, not merely reversal of one motor. (doobin2024theroleof pages 1-3, hu2013dyneinrecruitmentto pages 1-2)

Apical movement is activated in stages:

* **Early G2:** CDK1-dependent modification of RanBP2 promotes BICD2 recruitment, which recruits dynein–dynactin.
* **Later G2/prophase:** NUP133 anchors CENP-F; CENP-F recruits phosphorylated NDE1/NDEL1 and additional dynein.
* **Terminal approach:** the nucleus reaches the ventricular surface and briefly meets a centrosome that can move approximately 5 μm on average and up to 8 μm from the apical terminus. Nuclear arrival is required for normal mitotic entry. (doobin2024theroleof pages 1-3, hu2013dyneinrecruitmentto pages 1-2, hu2013dyneinrecruitmentto pages 8-10)

The pathways are sequential rather than redundant. BICD2 depletion arrested nuclei mainly more than 30 μm from the ventricle; NUP133 or CENP-F depletion allowed initial approach but arrested nuclei mainly within 10 μm, with about 70% of NUP133-depleted nuclei in that terminal zone. Forced nuclear-envelope targeting of an active BICD2 fragment rescued apical migration, strongly supporting local force generation at the nuclear surface. (hu2013dyneinrecruitmentto pages 4-6, hu2013dyneinrecruitmentto pages 8-10)

The following table summarizes the assemblies and the strength and limits of current evidence.

| Submodule / assembly | Principal molecules | Direction / physical role | Best-established biological context | Key experimental evidence | Status | Major uncertainty |
|---|---|---|---|---|---|---|
| LINC motor anchor | SUN1/2–Nesprin-2–BICD2 | Couples the nuclear envelope to dynein and kinesin; converts microtubule-motor force into nuclear movement | Postmitotic cortical neurons; also implicated in cerebellar neurons and retinal nuclear positioning | A motor-binding ~100-kDa Nesprin-2 fragment largely supported rat cortical migration, whereas disrupting Nesprin-2–BICD2 severely inhibited nuclear movement without preventing centrosome advance. Kinesin-1 inhibition increased migration from **0.16 ± 0.05 to 0.23 ± 0.07 μm/min**; the Nesprin-2 actin-binding domain was dispensable in this assay (goncalves2020nesprin2recruitmentof pages 1-4, goncalves2020nesprin2recruitmentof pages 9-12) | **Obligatory or near-obligatory** for efficient postmitotic cortical nucleokinesis; not universal | Exact SUN paralog/isoform composition and whether kinesin binds Nesprin-2 directly, through BICD2, or by both routes remain unresolved; results should not be transferred automatically to progenitor INM |
| Early-G2 nuclear-pore anchor | RanBP2/NUP358–BICD2–dynein–dynactin | Recruits minus-end-directed dynein to nuclear pores, initiating apical nuclear transport | G2 radial glial progenitors (RGPs) in embryonic rat cortex | BICD2 RNAi selectively blocked apical, not basal, INM; nuclei arrested predominantly **>30 μm** from the ventricular surface and none reached it. Forced nuclear-envelope dynein targeting rescued transport (hu2013dyneinrecruitmentto pages 1-2, hu2013dyneinrecruitmentto pages 4-6, hu2013dyneinrecruitmentto pages 8-10) | **Obligatory** for early apical INM in the tested RGP system | Direct endogenous RanBP2–BICD2 dynamics are technically difficult to image in brain tissue; importance may differ among neuroepithelia and species |
| Late-G2 nuclear-pore anchor | NUP133–CENP-F–NDE1/NDEL1–dynein | Adds nuclear-envelope dynein later in G2 and supports the terminal apical approach and centrosome–nucleus interaction | Premitotic RGPs in embryonic rat cortex | NUP133 or CENP-F RNAi arrested nuclei mostly within **10 μm** of the ventricle; ~**70%** of NUP133-depleted nuclei lay within 10 μm. Centrosome departure was abolished in all examined CENP-F-depleted cells and in **83%** of NUP133-depleted cells (hu2013dyneinrecruitmentto pages 4-6, hu2013dyneinrecruitmentto pages 8-10) | **Obligatory** for terminal apical INM and normal mitotic entry in the tested system | Relative contributions of NDE1 versus NDEL1 are context-dependent; mitotic-entry defects can be secondary to failed apical arrival or reflect an additional direct NDE1 function |
| Core minus-end motor | Cytoplasmic dynein-1–dynactin–LIS1, regulated by NDE1/NDEL1 | Pulls the nucleus toward microtubule minus ends; promotes load-bearing motor assembly/activity and nucleus–centrosome coupling | Postmitotic neuronal migration and apical RGP INM | Dynein inhibition increased neuronal nucleus–centrosome distance by **63%**; Lis1 deficiency increased it by **70%**. Complete Lis1 or Ndel1 loss abolished nuclear movement in cortical slices, and defects were dosage-sensitive (youn2009distinctdosedependentcortical pages 1-2, tanaka2004lis1anddoublecortin pages 9-10) | **Core/obligatory** in the best-studied mammalian contexts | LIS1 is not simply a constitutive “force enhancer”; how its motor-assembly, load-response, and localization functions are apportioned during each nucleokinetic stroke remains unsettled |
| Perinuclear microtubule scaffold | DCX-bound microtubules; centrosomal microtubule array | Forms a cage/fork around the nucleus converging anteriorly; supplies and stabilizes tracks for force transmission | Cultured mouse cerebellar granule neurons; inferred in cortical neurons | Live imaging showed DCX on cage-like perinuclear microtubules converging at the centrosome. Nocodazole increased mean nucleus–centrosome distance from **0.92 ± 0.70 μm** to **1.54 ± 1.43 μm** at 100 nM and **2.41 ± 1.42 μm** at 1 μM; DCX overexpression rescued Lis1- and dynactin-related coupling defects (tanaka2004lis1anddoublecortin pages 1-2, tanaka2004lis1anddoublecortin pages 5-7, tanaka2004lis1anddoublecortin pages 9-10) | **Microtubule tracks obligatory; DCX contribution context-dependent** | “DCX-stabilized cage” is supported strongly in granule-neuron assays but is not proven to be a universal, static structure or the exclusive dynein track in every migrating neuron |
| Rear actomyosin force | F-actin–non-muscle myosin II, especially NMII-B | Contracts behind the soma and can push or squeeze the nucleus forward; may coordinate with anterior actin and microtubules | Several cultured neuronal systems; some neuroepithelial INM models | Myosin-II inhibition and perturbation studies support a rearward contractile contribution, but Nesprin-2’s actin-binding domain was dispensable for cortical neuronal migration in vivo, indicating that any actomyosin force need not be transmitted through that LINC linkage (goncalves2020nesprin2recruitmentof pages 1-4, goncalves2020nesprin2recruitmentof pages 9-12) | **Conditional/accessory or parallel force generator** | Requirement varies by cell type, substrate, confinement, and assay; rat-brain studies detected no clear myosin-II role in INM whereas mouse neocortex and zebrafish retina studies did (hu2013dyneinrecruitmentto pages 1-2) |
| Basal INM motor | KIF1A (kinesin-3) | Plus-end-directed transport of the RGP nucleus away from the ventricular surface during G1 | Embryonic cortical RGPs | With RGP microtubule minus ends oriented apically and plus ends basally, KIF1A RNAi selectively inhibited basal migration, whereas dynein/LIS1 perturbation selectively inhibited apical migration (hu2013dyneinrecruitmentto pages 1-2, doobin2024theroleof pages 1-3) | **Obligatory** for basal INM in the tested rat-cortex model | The nuclear-envelope receptor/adaptor for KIF1A and its G1-specific recruitment mechanism remain unknown; Nesprin-2 binding to other kinesins does not establish direct KIF1A anchoring |
| Cell-cycle phosphoregulation | CDK1→RanBP2/BICD2 and NDE1; PLK1→BICD2 | Switches on nuclear-pore dynein recruitment during G2 and temporally orders early and late apical-INM machinery | Premitotic RGPs; mechanistic support from dividing cultured cells | NDE1 T215 and T243 phosphomutants blocked apical INM and mitosis; T246 mutation impaired mitotic entry without detectably blocking INM. BICD2 appears at the envelope before CENP-F, consistent with sequential activation (doobin2024theroleof pages 1-3, hu2013dyneinrecruitmentto pages 1-2) | **Obligatory regulatory layer** for G2 apical INM | Phosphomutants may alter localization, binding, or protein conformation simultaneously; failure to enter mitosis after failed INM does not prove a direct mitotic role |
| Postmitotic phosphoregulation | CDK5/p35–NDEL1/NDE1–LIS1–dynein | Links neuronal developmental signaling to dynein regulation, polarity, lamination, and possibly nucleokinesis | Postmitotic migrating neurons; distinct from CDK1-controlled RGP G2 INM | NDEL1 is a CDK5/p35 substrate, and graded NDEL1 loss causes dose-dependent migration and polarity defects. A 2024 study found that schizophrenia-linked NDE1-S214F selectively reduced adjacent T215 phosphorylation by CDK5 and altered cortical lamination (youn2009distinctdosedependentcortical pages 1-2, doobin2024theroleof pages 1-3, doobin2024theroleof pages 8-10) | **Important regulatory input; direct nucleokinetic effect incompletely resolved** | Phosphorylation can have different effects in migration, organelle transport, and nuclear-envelope breakdown; a universal direction of effect on the dynein motor cannot yet be asserted |


*Table: Conservative comparison of the principal force generators, nuclear-envelope anchors, tracks, and regulatory pathways in postmitotic neurons versus radial glial progenitors. Status labels refer only to the biological contexts in which each component has been directly tested.*

## 4. Major molecular players and active assemblies

### 4.1 LINC complexes: postmitotic nuclear-envelope coupling

LINC complexes consist of inner-nuclear-membrane SUN proteins whose luminal SUN domains bind the C-terminal KASH domains of outer-nuclear-membrane proteins. In mammals, SUN1 and SUN2 are broadly expressed; Nesprin-1/2 are enormous, alternatively spliced spectrin-repeat proteins with tissue- and isoform-specific cytoskeletal interfaces. Their cytoplasmic regions can engage actin, microtubule motors, and intermediate-filament-associated proteins. (kuwako2024diverserolesof pages 1-2)

In embryonic rat cortical neurons, a roughly 100-kDa Nesprin-2 fragment retaining motor-binding capacity was sufficient to support near-normal migration despite the approximately 800-kDa size of giant Nesprin-2. Its actin-binding domain was dispensable in that assay. BICD2 linked Nesprin-2 to both dynein and kinesin-1, and mutation of the Nesprin-2 LEWD sequence impaired BICD2 binding. These data establish Nesprin-2–BICD2 as a motor-cargo interface, but whether kinesin-1 contacts Nesprin-2 directly, through BICD2, or through both routes remains unresolved. (goncalves2020nesprin2recruitmentof pages 1-4, goncalves2020nesprin2recruitmentof pages 9-12)

### 4.2 Nuclear-pore anchors: a G2-specific alternative

RGP apical INM uses two NPC-based routes:

* **RanBP2/NUP358–BICD2–dynein–dynactin**, active earlier in G2.
* **NUP133–CENP-F–NDE1/NDEL1–dynein**, active later.

Three-dimensional microscopy found dynein, dynactin, and BICD2 in puncta associated with nuclear pores. Only 21.4% ± 5.7% of BICD2-positive G2 nuclei were also CENP-F positive, whereas CENP-F-positive nuclei were BICD2 positive, supporting temporal ordering. A dominant-negative KASH fragment did not measurably reduce HeLa G2-envelope dynein recruitment, arguing that this particular route is NPC-, not Nesprin-, anchored. (hu2013dyneinrecruitmentto pages 1-2, hu2013dyneinrecruitmentto pages 8-10)

This distinction is a major system boundary: LINC coupling in postmitotic neurons should not be conflated with NPC recruitment in G2 progenitors. Both convert motor movement into nuclear translocation, but their upstream anchors and regulatory logic differ.

### 4.3 Dynein–dynactin–LIS1–NDE1/NDEL1

Cytoplasmic dynein-1 is the central minus-end motor. Dynactin and activating adaptors such as BICD2 assemble processive cargo-bound motor complexes. LIS1 is an evolutionarily conserved dynein regulator important for assembly and force production under load; NDE1 and NDEL1 interact with LIS1 and dynein and provide localization and regulatory interfaces. Describing LIS1 simply as increasing dynein velocity is obsolete: its effects depend on motor state, adaptor, stoichiometry, and load.

The developmental evidence is unusually strong. Complete Lis1 or Ndel1 loss abolished nuclear movement in cortical-slice assays, while partial reduction produced graded slowing, polarity defects, and abnormal neurites. At 35% of wild-type NDEL1, migrating cells developed multiple leading processes and branched trajectories. Dynein inhibition increased nucleus–centrosome separation by 63%; Lis1 deficiency increased it by 70%. (youn2009distinctdosedependentcortical pages 1-2, tanaka2004lis1anddoublecortin pages 9-10)

NDE1 and NDEL1 are not interchangeable. NDE1 is especially important in progenitor INM, cell-cycle progression, and neurogenesis; NDEL1 has a more evident role in postmitotic neuronal migration. Overexpression can produce partial functional compensation, but human NDE1 loss causes severe microcephaly/microlissencephaly, whereas LIS1 haploinsufficiency predominantly produces lissencephaly. (doobin2024theroleof pages 1-3, youn2009distinctdosedependentcortical pages 1-2)

### 4.4 DCX and the perinuclear microtubule array

DCX binds and stabilizes microtubules. In migrating mouse cerebellar granule neurons, live imaging showed DCX-decorated cage-like microtubules surrounding the nucleus and converging on the anterior centrosome. Nocodazole increased mean nucleus–centrosome separation from 0.92 ± 0.70 μm to 1.54 ± 1.43 μm at 100 nM and 2.41 ± 1.42 μm at 1 μM. DCX overexpression restored migration to 94% of wild-type distance in Lis1-deficient neurons and rescued coupling defects caused by Lis1 deficiency or dynactin inhibition. DCX also co-immunoprecipitated with dynein subunits. (tanaka2004lis1anddoublecortin pages 5-7, tanaka2004lis1anddoublecortin pages 9-10)

These results support a DCX-stabilized, dynein-compatible perinuclear track. They do not prove that every migrating neuron has a static cage, that DCX is the sole stabilizer, or that the structure itself generates force. “DCX-stabilized cage” should therefore be treated as a strong model in granule-neuron systems and a plausible cortical mechanism, not a universal anatomical invariant.

### 4.5 Actomyosin

Non-muscle myosin II, particularly NMII-B, can generate contractile force behind the nucleus, compressing the soma and assisting forward movement. Actin-rich structures in the proximal leading process may also pull or steer the centrosome and soma through microtubule–actin crosslinkers such as drebrin. However, requirement differs among preparations. Myosin-II dependence has been reported in cultured neurons, mouse neocortex, and zebrafish retinal INM, whereas one embryonic-rat cortex study detected no clear INM requirement. Moreover, the Nesprin-2 actin-binding domain was dispensable for cortical migration in vivo, indicating that actomyosin need not act through that particular LINC linkage. (hu2013dyneinrecruitmentto pages 1-2, goncalves2020nesprin2recruitmentof pages 1-4, goncalves2020nesprin2recruitmentof pages 9-12)

Thus, actomyosin is best classified as a **parallel, context-sensitive force generator and coordinator**, not an invariant core equivalent to dynein in the best-studied mammalian neuronal systems.

### 4.6 Kinesins

KIF1A is selectively required for basal G1 INM in embryonic rat RGPs, consistent with the basal orientation of microtubule plus ends. Its nuclear receptor remains unknown. Nesprin-2 binds kinesin-family machinery, but this does not establish that KIF1A itself is LINC-anchored. (doobin2024theroleof pages 1-3, hu2013dyneinrecruitmentto pages 1-2)

Kinesin-1 has a different and surprising role in postmitotic cortical neurons. Inhibiting KIF5B/KLC increased migration velocity from 0.16 ± 0.05 to 0.23 ± 0.07 μm/min—about a 44% increase—and increased the number of neurons reaching the cortical plate. Kinesin-1 therefore appears to oppose dynein and restrain forward nuclear movement rather than drive the normal forward stroke. This illustrates why “kinesin equals forward migration” is not a transferable rule: direction depends on microtubule polarity and cellular context. (goncalves2020nesprin2recruitmentof pages 9-12)

### 4.7 Kinase regulation

**CDK1/PLK1 in progenitors.** CDK1 activates G2 nuclear-envelope motor recruitment by modifying RanBP2 and components of the NDE1 pathway. The 2023 BICD2 study further showed that CDK1-dependent BICD2 association with PLK1 permits PLK1 phosphorylation of BICD2, relieving autoinhibition and promoting dynein–dynactin assembly and phosphorylated-RanBP2 binding. This provides a biochemical explanation for temporal activation of early-G2 apical INM.

**CDK5/p35 in postmitotic neurons.** NDEL1 is phosphorylated by CDK5/p35 and interacts with LIS1/dynein. Genetic reduction causes dose-dependent migration defects, but phosphorylation has also been studied in NEBD and axonal organelle transport, where its consequences may differ. A 2024 study found that NDE1 T215 and T243 phosphomutants blocked apical INM and mitosis, while T246 mutation impaired mitotic entry without blocking INM. The schizophrenia-associated S214F substitution selectively inhibited CDK5 phosphorylation of adjacent T215 and altered cortical lamination. Because CDK5 is primarily postmitotic whereas CDK1 controls G2 RGPs, kinase identity is a critical compartment and developmental-stage constraint. (doobin2024theroleof pages 1-3, doobin2024theroleof pages 8-10, youn2009distinctdosedependentcortical pages 1-2, hebbar2008lis1andndel1 pages 1-2)

## 5. Evolutionary and cell-biological variation

### 5.1 Deep conservation

The deepest plausible origin is an early-eukaryotic nuclear-positioning toolkit assembled from:

* microtubules and cytoplasmic dynein;
* LIS1/NudF and NudE-family dynein regulators;
* SUN–KASH nuclear-envelope bridges;
* actomyosin-based auxiliary force systems.

Fungal *nud* and *ropy* screens identified dynein, LIS1/NudF, and NudE-family proteins as nuclear-distribution factors. SUN–KASH systems occur across animals, fungi, amoebozoans, and plants, although KASH sequences and effectors have diverged substantially. LINC-dependent migration in *C. elegans*, Drosophila photoreceptors, vertebrate neurons, and plant cells supports ancient conservation of the bridge principle rather than conservation of one exact mammalian complex. (tanaka2004lis1anddoublecortin pages 1-2, bone2016nuclearmigrationevents pages 1-2, kuwako2024diverserolesof pages 1-2, kuwako2024diverserolesof pages 5-6)

The vertebrate cortical module is therefore a later specialization of ancient components. BICD2, CENP-F, NUP133/RanBP2-mediated cell-cycle recruitment, brain-enriched DCX, and paralog specialization between NDE1 and NDEL1 represent elaboration rather than the ancestral core. SUN1/2 and Nesprin-1/2 are better representatives for broadly expressed mammalian LINC function than testis-restricted SUN3–5 or specialized KASH5. (kuwako2024diverserolesof pages 1-2)

### 5.2 Cell-type and stage variation

* **Postmitotic cortical neurons:** Nesprin-2–BICD2–dynein is prominent; kinesin-1 acts antagonistically; centrosome and nucleus can move semi-independently.
* **Cerebellar granule neurons:** perinuclear DCX arrays and nucleus–centrosome coupling are especially well visualized; actomyosin and microtubule–actin steering are prominent in culture.
* **RGPs:** G1 KIF1A and G2 NPC-anchored dynein form a cell-cycle-switched bidirectional system.
* **Retinal neuroepithelia:** both dynein and actomyosin contributions are reported; dominant force may vary with developmental zone and species.
* **Photoreceptors:** LINC complexes position nuclei and thereby influence retinal architecture and synaptic efficiency, but this is nuclear positioning rather than a continuously repeated migratory cycle. (hu2013dyneinrecruitmentto pages 1-2, goncalves2020nesprin2recruitmentof pages 9-12, kuwako2024diverserolesof pages 5-6)
* **Fibroblasts, myotubes, leukocytes, and constrained cells:** nuclei may move through TAN-line actin coupling, microtubule pushing, pressure, or combinations distinct from neuronal two-stroke nucleokinesis. These systems illuminate physical principles but should not be imported wholesale into cortical migration. (bone2016nuclearmigrationevents pages 8-9, bone2016nuclearmigrationevents pages 1-2)

## 6. Constraints, dependencies, and failure modes

### Ordering and polarity constraints

1. In canonical neuronal migration, polarization and centrosome/Golgi advance normally precede the nuclear stroke.
2. The nucleus must be coupled to a motor-bearing surface; otherwise centrosome advance alone is insufficient.
3. Motor direction is meaningful only relative to local microtubule polarity. In RGPs, basal plus ends explain KIF1A-driven basal motion and dynein-driven apical motion.
4. RanBP2–BICD2 activation precedes NUP133–CENP-F–NDE1 recruitment in G2.
5. In RGPs, apical arrival precedes normal mitotic entry; failure to divide after motor perturbation may therefore be indirect.
6. CDK1-regulated pore recruitment is G2-specific, whereas CDK5/p35 regulation principally concerns postmitotic neurons. (doobin2024theroleof pages 1-3, hu2013dyneinrecruitmentto pages 1-2, hu2013dyneinrecruitmentto pages 8-10)

### Evidence excluding plausible alternatives

* **Nuclear movement is not merely passive following of the centrosome:** Nesprin-2/BICD2 disruption arrests the nucleus despite continued centrosome advance. (goncalves2020nesprin2recruitmentof pages 1-4)
* **The two NPC routes are not simply redundant:** depletion produces spatially distinct early versus terminal arrests. (hu2013dyneinrecruitmentto pages 4-6)
* **LINC is not the sole G2 dynein anchor:** dominant-negative KASH did not prevent G2-envelope dynein recruitment in the tested cultured-cell context, whereas nuclear-pore pathway perturbations did. (hu2013dyneinrecruitmentto pages 8-10)
* **Actin does not universally need Nesprin-2 coupling:** removal of the Nesprin-2 actin-binding function did not block in-vivo cortical migration. (goncalves2020nesprin2recruitmentof pages 1-4, goncalves2020nesprin2recruitmentof pages 9-12)
* **Apical nuclear arrival is functionally upstream of mitosis:** forced NE dynein targeting restored both migration and cell-cycle progression after selected pathway perturbations. (hu2013dyneinrecruitmentto pages 8-10)

### Disease and experimental failure modes

* **PAFAH1B1/LIS1 haploinsufficiency:** classical lissencephaly, reflecting dosage-sensitive dynein dysfunction, impaired nucleokinesis, and additional progenitor/mitotic effects.
* **DCX mutation:** X-linked lissencephaly in males and subcortical band heterotopia (“double cortex”) in many heterozygous females; impaired microtubule organization and neuronal migration.
* **NDE1 biallelic loss:** severe microcephaly or microlissencephaly, consistent with progenitor INM and cell-cycle failure.
* **NDEL1 loss:** embryonic lethality in mice; strong neuronal migration and polarity phenotypes in reduced-dose models.
* **BICD2 variants:** neurodevelopmental malformations in addition to motor-neuron phenotypes, depending on allele and domain.
* **LINC disruption:** nuclear mispositioning in neurons and photoreceptors, with neurological phenotypes that vary because Nesprins and SUN proteins have many non-nucleokinetic functions. (doobin2024theroleof pages 1-3, youn2009distinctdosedependentcortical pages 1-2, tanaka2004lis1anddoublecortin pages 1-2, kuwako2024diverserolesof pages 1-2, kuwako2024diverserolesof pages 5-6)

Disease causality should not be assigned exclusively to nucleokinesis. LIS1, NDE1/NDEL1, dynein, BICD2, and LINC proteins also affect spindle orientation, organelle transport, NEBD, cilia, chromatin, and neuronal polarity. Cortical malformation is therefore a systems-level phenotype in which defective nuclear translocation is central but not solitary.

## 7. Controversies and open questions

1. **What anchors KIF1A to the RGP nucleus?** KIF1A is genetically required for basal INM, but no definitive G1-specific nuclear receptor or activating adaptor has been established.
2. **How are opposite-polarity motors coordinated?** Nesprin-2/BICD2 can engage dynein and kinesin-1, and some KASH proteins recruit both motors. Whether direction is set by motor number, adaptor phosphorylation, microtubule post-translational modification, load-dependent competition, or spatial sequestration remains unresolved. The 2024 literature increasingly treats motor opposition as regulated coordination rather than a simple tug-of-war. (goncalves2020nesprin2recruitmentof pages 9-12, bone2016nuclearmigrationevents pages 8-9)
3. **How much force comes from dynein versus myosin II?** The answer likely depends on cell type, substrate stiffness, confinement, developmental stage, and whether the assay is dissociated culture, organotypic slice, or intact tissue. Contradictory INM results probably reflect biological variation as well as technical differences. (hu2013dyneinrecruitmentto pages 1-2)
4. **Is the DCX cage universal and dynamic?** High-resolution force-correlated imaging is needed to establish whether DCX-decorated bundles bear load during individual strokes and how they remodel as the nucleus deforms.
5. **What exactly does LIS1 do during a stroke?** Modern biochemical models emphasize dynein activation and load-bearing assembly, whereas developmental studies often infer localization or coupling functions. Direct in-tissue measurements of motor stoichiometry and force are lacking.
6. **Does centrosome–nucleus distance cause migration efficiency or merely report coupling state?** Rescue and uncoupling experiments support functional importance, but movement can occur without strict centrosome co-transport in some neurons and RGPs.
7. **How do NDE1 and NDEL1 partition functions?** Their overlap in dynein binding contrasts with distinct progenitor and postmitotic phenotypes. Residue-specific phosphorylation, expression timing, and binding partners require systematic comparison.
8. **How does phosphorylation change motor mechanics?** The 2023 BICD2 and 2024 NDE1 studies identify relevant residues and developmental phenotypes, but phosphomimetic mutants cannot fully reproduce reversible phosphorylation. It is also unclear whether T215/T243 must subsequently be dephosphorylated for mitotic progression. (doobin2024theroleof pages 1-3, doobin2024theroleof pages 8-10)
9. **How transferable are rodent findings to human corticogenesis?** Human cortical neurons migrate farther and develop over much longer intervals. Human organoids and fetal-tissue imaging are needed to test whether outer radial glia, expanded progenitor zones, and human-specific geometry alter the motor hierarchy.
10. **Can the module be targeted therapeutically?** Current applications are primarily mechanistic and diagnostic: interpreting lissencephaly/microcephaly variants, modeling cortical malformations in organoids, and using migration phenotypes to assess gene function. Direct pharmacological manipulation is hazardous because dynein, kinesins, CDKs, and LINC proteins are pleiotropic and essential.

## 8. Key references

1. **Tsai L-H, Gleeson JG.** “Nucleokinesis in Neuronal Migration.” *Neuron*. Published May 2005. DOI: [10.1016/j.neuron.2005.04.013](https://doi.org/10.1016/j.neuron.2005.04.013). Foundational definition and two-stroke framework. (tsai2005nucleokinesisinneuronal pages 1-2)
2. **Tanaka T et al.** “Lis1 and doublecortin function with dynein to mediate coupling of the nucleus to the centrosome in neuronal migration.” *Journal of Cell Biology*. Published June 1, 2004. DOI: [10.1083/jcb.200309025](https://doi.org/10.1083/jcb.200309025). Primary DCX/LIS1/coupling study. (tanaka2004lis1anddoublecortin pages 1-2, tanaka2004lis1anddoublecortin pages 5-7, tanaka2004lis1anddoublecortin pages 9-10)
3. **Youn YH et al.** “Distinct Dose-Dependent Cortical Neuronal Migration and Neurite Extension Defects in Lis1 and Ndel1 Mutant Mice.” *Journal of Neuroscience*. Published December 9, 2009. DOI: [10.1523/JNEUROSCI.4630-09.2009](https://doi.org/10.1523/JNEUROSCI.4630-09.2009). Genetic dose-response evidence. (youn2009distinctdosedependentcortical pages 1-2)
4. **Hu DJ-K et al.** “Dynein Recruitment to Nuclear Pores Activates Apical Nuclear Migration and Mitotic Entry in Brain Progenitor Cells.” *Cell*. Published September 12, 2013. DOI: [10.1016/j.cell.2013.08.024](https://doi.org/10.1016/j.cell.2013.08.024). Primary NPC anchoring and rescue study. (hu2013dyneinrecruitmentto pages 1-2, hu2013dyneinrecruitmentto pages 4-6, hu2013dyneinrecruitmentto pages 8-10)
5. **Gonçalves JC et al.** “Nesprin-2 Recruitment of BicD2 to the Nuclear Envelope Controls Dynein/Kinesin-Mediated Neuronal Migration In Vivo.” *Current Biology*. Published August 17, 2020. DOI: [10.1016/j.cub.2020.05.091](https://doi.org/10.1016/j.cub.2020.05.091). Primary LINC/BICD2 and antagonistic-kinesin study. (goncalves2020nesprin2recruitmentof pages 1-4, goncalves2020nesprin2recruitmentof pages 9-12)
6. **Hebbar S et al.** “Lis1 and Ndel1 influence the timing of nuclear envelope breakdown in neural stem cells.” *Journal of Cell Biology*. Published September 2008. DOI: [10.1083/jcb.200803071](https://doi.org/10.1083/jcb.200803071). Defines an adjacent, phosphorylation-sensitive NEBD function. (hebbar2008lis1andndel1 pages 1-2)
7. **Gallisà-Suñé N et al.** “BICD2 phosphorylation regulates dynein function and centrosome separation in G2 and M.” *Nature Communications*. Published April 2023. DOI: [10.1038/s41467-023-38116-1](https://doi.org/10.1038/s41467-023-38116-1). Recent biochemical refinement of BICD2 activation.
8. **Doobin DJ et al.** “The Role of Nde1 Phosphorylation in Interkinetic Nuclear Migration and Schizophrenia.” Preprint posted February 2024; subsequently reported in *Molecular Biology of the Cell* (2024). Preprint DOI: [10.1101/2024.02.25.581986](https://doi.org/10.1101/2024.02.25.581986); journal DOI: [10.1091/mbc.E24-05-0217](https://doi.org/10.1091/mbc.E24-05-0217). Residue-specific NDE1 regulation. (doobin2024theroleof pages 1-3, doobin2024theroleof pages 8-10)
9. **Kuwako K-I, Suzuki S.** “Diverse Roles of the LINC Complex in Cellular Function and Disease in the Nervous System.” *International Journal of Molecular Sciences*. Published October 26, 2024. DOI: [10.3390/ijms252111525](https://doi.org/10.3390/ijms252111525). Current authoritative LINC review. (kuwako2024diverserolesof pages 1-2, kuwako2024diverserolesof pages 5-6)
10. **Kroll J, Renkawitz J.** “Principles of organelle positioning in motile and non-motile cells.” *EMBO Reports*. Published April 2024. DOI: [10.1038/s44319-024-00135-4](https://doi.org/10.1038/s44319-024-00135-4). Current physical framework for organelle anchorage and force generation.
11. **Bone CR, Starr DA.** “Nuclear migration events throughout development.” *Journal of Cell Science*. Published May 2016. DOI: [10.1242/jcs.179788](https://doi.org/10.1242/jcs.179788). Comparative evolutionary and mechanistic review. (bone2016nuclearmigrationevents pages 8-9, bone2016nuclearmigrationevents pages 1-2)

### Overall assessment

The strongest consensus is that nucleokinesis is a modular mechanical process: a nuclear-envelope cargo interface engages polarized cytoskeletal motors, and microtubule organization converts motor directionality into tissue-appropriate nuclear movement. Dynein–dynactin–LIS1/NDE1/NDEL1 is the conserved core of forward neuronal and apical progenitor movement, but the envelope anchor is developmentally switched—from LINC-based coupling in postmitotic neurons to NPC-based recruitment in G2 RGPs. DCX and actomyosin improve mechanical coherence and force production in context-dependent ways, whereas KIF1A supplies the opposite basal INM stroke. The main frontier is no longer identifying a single missing motor; it is explaining how alternative anchors, opposing motors, phosphorylation states, and tissue mechanics are coordinated in space and time.

References

1. (tsai2005nucleokinesisinneuronal pages 1-2): Li-Huei Tsai and Joseph G. Gleeson. Nucleokinesis in neuronal migration. Neuron, 46:383-388, May 2005. URL: https://doi.org/10.1016/j.neuron.2005.04.013, doi:10.1016/j.neuron.2005.04.013. This article has 454 citations and is from a highest quality peer-reviewed journal.

2. (doobin2024theroleof pages 1-3): David J Doobin, Paige Helmer, Aurelie carabalona, Chiara Bertipaglia, and Richard B Vallee. The role of nde1 phosphorylation in interkinetic nuclear migration and schizophrenia. bioRxiv, Feb 2024. URL: https://doi.org/10.1101/2024.02.25.581986, doi:10.1101/2024.02.25.581986. This article has 0 citations.

3. (hu2013dyneinrecruitmentto pages 1-2): Daniel Jun-Kit Hu, Alexandre Dominique Baffet, Tania Nayak, Anna Akhmanova, Valérie Doye, and Richard Bert Vallee. Dynein recruitment to nuclear pores activates apical nuclear migration and mitotic entry in brain progenitor cells. Cell, 154:1300-1313, Sep 2013. URL: https://doi.org/10.1016/j.cell.2013.08.024, doi:10.1016/j.cell.2013.08.024. This article has 226 citations and is from a highest quality peer-reviewed journal.

4. (goncalves2020nesprin2recruitmentof pages 1-4): João Carlos Gonçalves, Sebastian Quintremil, Julie Yi, and Richard B. Vallee. Nesprin-2 recruitment of bicd2 to the nuclear envelope controls dynein/kinesin-mediated neuronal migration in vivo. Current Biology, 30:3116-3129.e4, Aug 2020. URL: https://doi.org/10.1016/j.cub.2020.05.091, doi:10.1016/j.cub.2020.05.091. This article has 87 citations and is from a highest quality peer-reviewed journal.

5. (tanaka2004lis1anddoublecortin pages 1-2): Teruyuki Tanaka, Finley F. Serneo, Christine Higgins, Michael J. Gambello, Anthony Wynshaw-Boris, and Joseph G. Gleeson. Lis1 and doublecortin function with dynein to mediate coupling of the nucleus to the centrosome in neuronal migration. The Journal of Cell Biology, 165:709-721, Jun 2004. URL: https://doi.org/10.1083/jcb.200309025, doi:10.1083/jcb.200309025. This article has 505 citations.

6. (doobin2024theroleof pages 8-10): David J Doobin, Paige Helmer, Aurelie carabalona, Chiara Bertipaglia, and Richard B Vallee. The role of nde1 phosphorylation in interkinetic nuclear migration and schizophrenia. bioRxiv, Feb 2024. URL: https://doi.org/10.1101/2024.02.25.581986, doi:10.1101/2024.02.25.581986. This article has 0 citations.

7. (hu2013dyneinrecruitmentto pages 8-10): Daniel Jun-Kit Hu, Alexandre Dominique Baffet, Tania Nayak, Anna Akhmanova, Valérie Doye, and Richard Bert Vallee. Dynein recruitment to nuclear pores activates apical nuclear migration and mitotic entry in brain progenitor cells. Cell, 154:1300-1313, Sep 2013. URL: https://doi.org/10.1016/j.cell.2013.08.024, doi:10.1016/j.cell.2013.08.024. This article has 226 citations and is from a highest quality peer-reviewed journal.

8. (goncalves2020nesprin2recruitmentof pages 9-12): João Carlos Gonçalves, Sebastian Quintremil, Julie Yi, and Richard B. Vallee. Nesprin-2 recruitment of bicd2 to the nuclear envelope controls dynein/kinesin-mediated neuronal migration in vivo. Current Biology, 30:3116-3129.e4, Aug 2020. URL: https://doi.org/10.1016/j.cub.2020.05.091, doi:10.1016/j.cub.2020.05.091. This article has 87 citations and is from a highest quality peer-reviewed journal.

9. (kuwako2024diverserolesof pages 1-2): Ken-ichiro Kuwako and Sadafumi Suzuki. Diverse roles of the linc complex in cellular function and disease in the nervous system. International Journal of Molecular Sciences, 25:11525, Oct 2024. URL: https://doi.org/10.3390/ijms252111525, doi:10.3390/ijms252111525. This article has 5 citations.

10. (kuwako2024diverserolesof pages 5-6): Ken-ichiro Kuwako and Sadafumi Suzuki. Diverse roles of the linc complex in cellular function and disease in the nervous system. International Journal of Molecular Sciences, 25:11525, Oct 2024. URL: https://doi.org/10.3390/ijms252111525, doi:10.3390/ijms252111525. This article has 5 citations.

11. (bone2016nuclearmigrationevents pages 1-2): Courtney R. Bone and Daniel A. Starr. Nuclear migration events throughout development. Journal of Cell Science, 129:1951-1961, May 2016. URL: https://doi.org/10.1242/jcs.179788, doi:10.1242/jcs.179788. This article has 146 citations and is from a domain leading peer-reviewed journal.

12. (hebbar2008lis1andndel1 pages 1-2): Sachin Hebbar, Mariano T. Mesngon, Aimee M. Guillotte, Bhavim Desai, Ramses Ayala, and Deanna S. Smith. Lis1 and ndel1 influence the timing of nuclear envelope breakdown in neural stem cells. The Journal of Cell Biology, 182:1063-1071, Sep 2008. URL: https://doi.org/10.1083/jcb.200803071, doi:10.1083/jcb.200803071. This article has 110 citations.

13. (kuwako2024diverserolesof pages 10-11): Ken-ichiro Kuwako and Sadafumi Suzuki. Diverse roles of the linc complex in cellular function and disease in the nervous system. International Journal of Molecular Sciences, 25:11525, Oct 2024. URL: https://doi.org/10.3390/ijms252111525, doi:10.3390/ijms252111525. This article has 5 citations.

14. (hu2013dyneinrecruitmentto pages 4-6): Daniel Jun-Kit Hu, Alexandre Dominique Baffet, Tania Nayak, Anna Akhmanova, Valérie Doye, and Richard Bert Vallee. Dynein recruitment to nuclear pores activates apical nuclear migration and mitotic entry in brain progenitor cells. Cell, 154:1300-1313, Sep 2013. URL: https://doi.org/10.1016/j.cell.2013.08.024, doi:10.1016/j.cell.2013.08.024. This article has 226 citations and is from a highest quality peer-reviewed journal.

15. (youn2009distinctdosedependentcortical pages 1-2): Yong Ha Youn, Tiziano Pramparo, Shinji Hirotsune, and Anthony Wynshaw-Boris. Distinct dose-dependent cortical neuronal migration and neurite extension defects in lis1 and ndel1 mutant mice. The Journal of Neuroscience, 29:15520-15530, Dec 2009. URL: https://doi.org/10.1523/jneurosci.4630-09.2009, doi:10.1523/jneurosci.4630-09.2009. This article has 139 citations.

16. (tanaka2004lis1anddoublecortin pages 9-10): Teruyuki Tanaka, Finley F. Serneo, Christine Higgins, Michael J. Gambello, Anthony Wynshaw-Boris, and Joseph G. Gleeson. Lis1 and doublecortin function with dynein to mediate coupling of the nucleus to the centrosome in neuronal migration. The Journal of Cell Biology, 165:709-721, Jun 2004. URL: https://doi.org/10.1083/jcb.200309025, doi:10.1083/jcb.200309025. This article has 505 citations.

17. (tanaka2004lis1anddoublecortin pages 5-7): Teruyuki Tanaka, Finley F. Serneo, Christine Higgins, Michael J. Gambello, Anthony Wynshaw-Boris, and Joseph G. Gleeson. Lis1 and doublecortin function with dynein to mediate coupling of the nucleus to the centrosome in neuronal migration. The Journal of Cell Biology, 165:709-721, Jun 2004. URL: https://doi.org/10.1083/jcb.200309025, doi:10.1083/jcb.200309025. This article has 505 citations.

18. (bone2016nuclearmigrationevents pages 8-9): Courtney R. Bone and Daniel A. Starr. Nuclear migration events throughout development. Journal of Cell Science, 129:1951-1961, May 2016. URL: https://doi.org/10.1242/jcs.179788, doi:10.1242/jcs.179788. This article has 146 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](nucleokinesis-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. tsai2005nucleokinesisinneuronal pages 1-2
2. bone2016nuclearmigrationevents pages 1-2
3. hu2013dyneinrecruitmentto pages 1-2
4. kuwako2024diverserolesof pages 1-2
5. hu2013dyneinrecruitmentto pages 4-6
6. hu2013dyneinrecruitmentto pages 8-10
7. youn2009distinctdosedependentcortical pages 1-2
8. doobin2024theroleof pages 1-3
9. doobin2024theroleof pages 8-10
10. kuwako2024diverserolesof pages 5-6
11. kuwako2024diverserolesof pages 10-11
12. bone2016nuclearmigrationevents pages 8-9
13. 10.1016/j.neuron.2005.04.013
14. 10.1083/jcb.200309025
15. 10.1523/JNEUROSCI.4630-09.2009
16. 10.1016/j.cell.2013.08.024
17. 10.1016/j.cub.2020.05.091
18. 10.1083/jcb.200803071
19. 10.1038/s41467-023-38116-1
20. 10.1101/2024.02.25.581986
21. 10.1091/mbc.E24-05-0217
22. 10.3390/ijms252111525
23. 10.1038/s44319-024-00135-4
24. 10.1242/jcs.179788
25. https://doi.org/10.1016/j.neuron.2005.04.013
26. https://doi.org/10.1083/jcb.200309025
27. https://doi.org/10.1523/JNEUROSCI.4630-09.2009
28. https://doi.org/10.1016/j.cell.2013.08.024
29. https://doi.org/10.1016/j.cub.2020.05.091
30. https://doi.org/10.1083/jcb.200803071
31. https://doi.org/10.1038/s41467-023-38116-1
32. https://doi.org/10.1101/2024.02.25.581986
33. https://doi.org/10.1091/mbc.E24-05-0217
34. https://doi.org/10.3390/ijms252111525
35. https://doi.org/10.1038/s44319-024-00135-4
36. https://doi.org/10.1242/jcs.179788
37. https://doi.org/10.1016/j.neuron.2005.04.013,
38. https://doi.org/10.1101/2024.02.25.581986,
39. https://doi.org/10.1016/j.cell.2013.08.024,
40. https://doi.org/10.1016/j.cub.2020.05.091,
41. https://doi.org/10.1083/jcb.200309025,
42. https://doi.org/10.3390/ijms252111525,
43. https://doi.org/10.1242/jcs.179788,
44. https://doi.org/10.1083/jcb.200803071,
45. https://doi.org/10.1523/jneurosci.4630-09.2009,