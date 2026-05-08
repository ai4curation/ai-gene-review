    ---
    provider: bioreason-pro
    model: SFT
    source: huggingface.co/datasets/wanglab/protein_catalogue
    date: '2026-04-04'
    uniprot_id: Q5VW00
    gene: DCAF12L2
    organism: Homo sapiens (Human)
    ---

    ## Thinking Trace

    I begin with the InterPro architecture. The core signature IPR051191 (DDB1-CUL4-associated factor 12 family, residues 44–463) defines the protein as a DCAF12-class substrate receptor for the CUL4-DDB1 cullin-RING E3 ligase. Within this, IPR056151 (DDB1- and CUL4-associated factor 12, beta-propeller domain, residues 83–463) specifies a C-terminal beta-propeller scaffold. Multiple WD40-related entries corroborate this fold: IPR015943 (WD40/YVTN repeat-like-containing domain superfamily, residues 85–243) and IPR036322 (WD40-repeat-containing domain superfamily, residues 92–385) cover the propeller’s blades, while discrete IPR001680 WD40 repeats are mapped at positions 137–178, 183–221, 190–223, 251–290, and 340–376, indicating a multi-bladed WD40 array that completes the propeller. The N-terminus preceding residue 44 likely forms a flexible segment that docks onto DDB1. This ordered layout—an N-terminal DDB1-interacting region followed by a C-terminal WD40 beta-propeller—creates a bipartite receptor: the N-terminus anchors the protein into the CUL4-DDB1 core, and the beta-propeller presents a multivalent surface to capture substrates.

This architecture causes protein binding as the primary molecular function (GO:0005515), with two binding modes: constitutive binding to the CUL4-DDB1 ligase core via the N-terminus and selective binding to substrates via the WD40 propeller surface. Because WD40 beta-propellers commonly recognize short linear motifs or post-translationally modified degrons, the propeller likely reads degrons on autophagy regulators.

Coupling this binding activity to cellular outcomes, a DCAF12-class receptor would recruit specific autophagy factors to a CRL4 ligase for ubiquitination. Targeting ATG8-family proteins (e.g., MAP1LC3B and GABARAPL1) for ubiquitin tagging promotes their proteasome-dependent turnover, thereby tuning autophagic flux. This mechanistic link places the protein in regulation of autophagy (GO:0010506) and in proteasome-mediated ubiquitin-dependent protein catabolic process (GO:0043161). The same WD40-guided recognition can extend to additional autophagy regulators such as WIPI2, and to non-autophagy substrates like the transcription factor KLF4, indicating a broader role as a substrate-specific adaptor that directs ubiquitination toward context-dependent targets.

The cellular context follows from the complex it assembles and the substrates it engages. As a DCAF, it is a component of the Cul4-RING E3 ubiquitin ligase complex (GO:0080008). Its action on ATG8-family proteins and WIPI2 situates it in the cytoplasm (GO:0005737), where autophagosome biogenesis and cargo turnover occur. The presence at the centrosome (GO:0005813) is consistent with cullin ligase assemblies that survey and remodel protein networks at this microtubule-organizing center, potentially coordinating localized ubiquitination events that intersect with autophagy initiation or cell-cycle–linked quality control.

Mechanistically, the N-terminal DCAF12 family segment binds DDB1 to position the receptor on CUL4-DDB1, while the WD40 beta-propeller captures degrons on ATG8-family proteins, WIPI2, and KLF4. The assembled CRL4 complex then catalyzes ubiquitin transfer to these substrates, committing them to proteasomal degradation and thereby modulating autophagy and transcriptional programs. Interaction partners are expected to include DNA damage-binding protein 1 (DDB1) as the core adaptor, and paralogous DCAF8-like proteins (DCAF8L1, DCAF8L2) that may form alternative or cooperative assemblies. A close functional neighbor is DCAF12-like protein 1, which could provide overlapping or redundant substrate capture, enabling robustness of the ubiquitination pathway at cytoplasmic and centrosomal sites.

    ## Functional Summary

    A WD40 beta-propeller substrate receptor for a CUL4–DDB1 cullin-RING E3 ligase that assembles on the ligase core via its N-terminus and captures specific targets with its propeller surface to drive ubiquitination. It directs proteasomal degradation of autophagy regulators, including ATG8-family proteins and WIPI2, thereby tuning autophagic flux, and it can also target the transcription factor KLF4. The complex operates primarily in the cytoplasm and at the centrosome, where localized ubiquitination integrates autophagy control with broader cellular remodeling.

    ## UniProt Summary

    Substrate-recognition component of a DCX (DDB1-CUL4-X-box) E3 ubiquitin-protein ligase complex of the Cul4-DDB1 E3 ubiquitin-protein ligase complex. Mediates the ubiquitination and subsequent proteasomal degradation of MAP1LC3B and GABARAPL1, thereby regulating autophagy. Mediates the ubiquitination and subsequent proteasomal degradation of WIPI2. Mediates the ubiquitination and subsequent proteasomal degradation of the transcription factor KLF4 (By similarity).

    ## InterPro Domains

        - IPR051191: DDB1-CUL4-associated factor 12 (family) [44-463]
    - IPR056151: DDB1- and CUL4-associated factor 12, beta-propeller domain (domain) [83-463]
    - IPR015943: WD40/YVTN repeat-like-containing domain superfamily (homologous_superfamily) [85-243]
    - IPR036322: WD40-repeat-containing domain superfamily (homologous_superfamily) [92-385]
    - IPR001680: WD40 repeat (repeat) [137-178]
    - IPR001680: WD40 repeat (repeat) [183-221]
    - IPR001680: WD40 repeat (repeat) [190-223]
    - IPR015943: WD40/YVTN repeat-like-containing domain superfamily (homologous_superfamily) [248-396]
    - IPR001680: WD40 repeat (repeat) [251-290]
    - IPR001680: WD40 repeat (repeat) [340-376]

    ## GO Term Predictions

    ### Molecular Function


    ### Biological Process


    ### Cellular Component

