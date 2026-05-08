    ---
    provider: bioreason-pro
    model: SFT
    source: huggingface.co/datasets/wanglab/protein_catalogue
    date: '2026-04-04'
    uniprot_id: P53270
    gene: YGR117C
    organism: Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast)
    ---

    ## Thinking Trace

    I begin with the domain architecture. The polypeptide is almost entirely covered by two family-level signatures: IPR016520 (Uncharacterised conserved protein UCP007778 family, residues 4–471) and IPR060045 (Uncharacterised conserved protein UCP007778-like family, residues 10–469). These broad family marks indicate a conserved, non-enzymatic scaffold-like role. At the extreme N-terminus lies IPR006594 (LIS1 homology motif, residues 7–39), a short conserved site classically associated with microtubule- and dynein-linked regulation and known to mediate contacts with cytoskeletal machinery. The C-terminal two-thirds are encompassed by IPR036322 (WD40-repeat-containing domain superfamily, residues 125–472), which denotes a beta-propeller platform optimized for multivalent protein–protein interactions rather than catalysis. The ordered layout—an N-terminal LIS1-like regulatory motif feeding into a large WD40 propeller embedded within a conserved UCP007778 scaffold—creates a modular adaptor that can couple motor proteins to specific macromolecular assemblies.

This architecture causes a molecular function centered on binding rather than enzymatic activity. The WD40 superfamily domain provides a rigid, solvent-exposed propeller surface for docking multiple partners, while the LIS1-like motif supplies a regulatory handle that can engage cytoskeletal motors or their adaptors. Such a composite scaffold is well-suited to bind class V myosins that drive nuclear positioning in yeast, supporting the molecular function formalized as GO:0032033 myosin V binding. The lack of catalytic domains and the dominance of interaction-centric folds further argue that the protein acts as a cargo/adaptor or assembly factor for motor complexes.

From this binding activity, a biological process emerges. In budding yeast, positioning of the nucleus (binuclearcytoskeleton-driven nuclear migration) requires coupling the nuclear envelope to actomyosin forces. A WD40/LIS1-like scaffold that binds myosin V can organize or stabilize the motor–cargo interface at the nuclear periphery, thereby enabling efficient nuclear translocation. The same scaffold can also influence chromatin states by recruiting or positioning silencing factors. WD40 propellers commonly serve as hubs for chromatin-modifying complexes; by assembling repressors at specific loci, the protein can promote formation of silent chromatin at the silent mating-type cassette, aligning with GO:0030466 silent mating-type cassette heterochromatin formation. Thus, the domain architecture causally links myosin V binding to two processes: force-coupling for nuclear movement and organization of repressive chromatin at the HMR locus.

Cellular location follows from these roles. The absence of transmembrane segments and the presence of interaction-centric domains indicate a soluble protein. Its function in nuclear migration implies association with the nuclear envelope and perinuclear cytoskeleton, while its role in heterochromatin formation implies nuclear access. Therefore, a primary residence in the cytoplasm with dynamic enrichment at the nuclear periphery is expected, consistent with GO:0005737 cytoplasm and a likely association with the nucleus.

Mechanistically, I hypothesize that the N-terminal LIS1-like motif tunes engagement with myosin V motors, while the WD40 propeller presents docking sites for both motor adaptors and nuclear-envelope tethers. This would create a force-transmission module that links the nuclear outer membrane to myosin V tracks, driving nuclear migration. In parallel, the same propeller could scaffold silencing assemblies at the HMR locus—recruiting chromatin readers and writers to nucleate heterochromatin. Likely interaction partners include the myosin V motor and its adaptors at the nuclear periphery, nuclear-envelope tethers, and chromatin-silencing factors that deposit or recognize histone modifications at mating-type loci.

    ## Functional Summary

    A cytoplasmic scaffold in baker’s yeast that binds myosin V to couple actomyosin forces to the nuclear periphery during nuclear migration, while also assembling silencing factors to promote formation of silent chromatin at the mating-type locus. Its N-terminal regulatory motif likely modulates motor engagement, and its beta-propeller core provides a multivalent platform to tether nuclear-envelope components and chromatin modifiers, enabling coordinated nuclear positioning and transcriptional repression.

    ## UniProt Summary

    Involved in nuclear migration. Also involved in transcriptional silencing at the HMR locus.

    ## InterPro Domains

        - IPR016520: Uncharacterised conserved protein UCP007778 (family) [4-471]
    - IPR006594: LIS1 homology motif (conserved_site) [7-39]
    - IPR060045: Uncharacterised conserved protein UCP007778-like (family) [10-469]
    - IPR036322: WD40-repeat-containing domain superfamily (homologous_superfamily) [125-472]

    ## GO Term Predictions

    ### Molecular Function


    ### Biological Process


    ### Cellular Component

