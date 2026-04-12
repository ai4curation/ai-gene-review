    ---
    provider: bioreason-pro
    model: SFT
    source: huggingface.co/datasets/wanglab/protein_catalogue
    date: '2026-04-04'
    uniprot_id: Q96EA4
    gene: SPDL1
    organism: Homo sapiens (Human)
    ---

    ## Thinking Trace

    The architecture begins with IPR028593 (Protein Spindly, chordates family) spanning residues 1–605, covering the full polypeptide and defining a chordate-specific kinetochore adaptor scaffold. Nested within this, residues 3–468 carry IPR051149 (Spindly/BICDR Dynein Motor Adapter family), a hallmark of coiled-coil adaptors that couple cytoplasmic dynein to diverse cargo. The placement of the dynein-adapter core inside the broader Spindly family envelope indicates a bipartite design: an N-terminal-to-mid-region motor-adapter module that binds dynein and its regulatory subunits, and a C-terminal region within the full-length family signature that engages kinetochore receptors. This arrangement causes selective recruitment of dynein to kinetochores and spindle poles, and it provides a platform for regulatory enzymes at the kinetochore.

From this domain logic, the molecular function centers on assembling and positioning a motor-enzymatic module. The dynein-adapter core enforces dynein targeting to microtubule minus ends and kinetochore receptors, while the scaffolded surfaces accommodate regulatory enzymes. This supports GO:0019899 enzyme binding, as the adaptor is poised to bind kinases and phosphatases that tune kinetochore-microtubule attachments and checkpoint signaling.

The same architecture drives specific biological processes. By docking dynein at kinetochores, the adaptor generates poleward forces that align chromosomes at the metaphase plate, matching GO:0007080 mitotic metaphase plate congression. Dynein recruitment also biases spindle geometry and microtubule flux, enabling GO:0000132 establishment of mitotic spindle orientation. The scaffold’s ability to capture outer-kinetochore receptors and concentrate regulatory enzymes directly implements GO:0034501 protein localization to kinetochore. Outside mitosis, dynein-based transport along microtubules contributes to directed cell movement; by positioning dynein at specific cortical or Golgi sites, the adaptor can influence cytoskeletal polarity and vesicle trafficking, aligning with GO:0016477 cell migration.

The cellular context follows from the same chain. The dynein-adapter module and kinetochore-binding surfaces place the protein at the GO:0000940 outer kinetochore during mitosis, where it forms the GO:0098806 Spindly-BICDR complex that couples dynein to kinetochore receptors. Minus-end-directed transport and motor loading explain accumulation at the GO:0000922 spindle pole. Between divisions and during interphase transport, a soluble pool resides in the GO:0005829 cytosol, while regulatory cycles and chromatin-proximal functions rationalize presence in the GO:0005634 nucleus.

Mechanistically, the adaptor binds outer-kinetochore receptors such as BUB1B/BUB3 and the NDC80 complex to anchor dynein and its cofactors, creating a dynein–dynactin–adaptor assembly that exerts poleward forces on attached kinetochores. Phosphorylation by PLK1 and checkpoint factors modulates its affinity and timing, while association with MKLN1 (BICDR) tunes dynein loading in interphase. Through these regulated interactions, it promotes bi-orientation, error correction, and timely anaphase onset. The same scaffold can engage additional kinetochore modules (SKA1/2/3, CENP-F) to stabilize end-on attachments and coordinate with APC/C activation via CDC20. In non-mitotic contexts, adaptor-mediated dynein targeting to Golgi membranes and cortical sites can drive vesicle trafficking and polarity, contributing to cell migration. The observed partners—BUB1 beta, CENP-F, SKA1/2/3, BIO1, PLK1, CDC20, NDC80, and even developmental regulators like HOX-D13—fit a model in which the adaptor integrates checkpoint, structural, and regulatory inputs to choreograph dynein-dependent transport and kinetochore mechanics.

    ## Functional Summary

    A dynein-recruiting kinetochore adaptor that assembles a motor–regulatory module to capture and load dynein–dynactin at kinetochores and spindle poles. By anchoring to outer-kinetochore receptors and engaging checkpoint and structural factors, it generates poleward forces for chromosome alignment and proper spindle orientation, coordinates the timing of anaphase onset, and modulates kinetochore–microtubule attachments. In interphase, association with a dynein cofactor tunes dynein loading and extends its role to Golgi-directed transport and polarity programs that support cell migration. The protein cycles between cytosol and nucleus, concentrates at kinetochores during mitosis, and forms a dedicated adaptor complex with its dynein-binding partner.

    ## UniProt Summary

    Kinetochore adapter protein which recruits the dynein motor complex to kinetochores. Required for chromosome alignment and spindle orientation during mitosis. May also regulate the onset of anaphase and kinetochore microtubule attachment. Association with MKLN1/BICDR regulates dynein loading by SPINDLY onto the Golgi apparatus.

    ## InterPro Domains

        - IPR028593: Protein Spindly, chordates (family) [1-605]
    - IPR051149: Spindly/BICDR Dynein Motor Adapter (family) [3-468]

    ## GO Term Predictions

    ### Molecular Function


    ### Biological Process


    ### Cellular Component

