    ---
    provider: bioreason-pro
    model: SFT
    source: huggingface.co/datasets/wanglab/protein_catalogue
    date: '2026-04-04'
    uniprot_id: Q01989
    gene: jar
    organism: Drosophila melanogaster (Fruit fly)
    ---

    ## Thinking Trace

    I begin by dissecting the InterPro architecture and its order along the polypeptide. The extreme N-terminus carries an SH3-like module: IPR004009 (Myosin, SH3 domain, residues 3–54) and a coincident IPR008989 (Myosin S1 fragment, N-terminal homologous superfamily, residues 3–50). Immediately following, a dense cluster of myosin head signatures spans the core: IPR001609 (Myosin head, motor domain-like, residues 52–767) with overlapping superfamily annotations IPR027417 (P-loop containing nucleoside triphosphate hydrolase, residues 55–830), IPR036961 (Kinesin motor domain superfamily, residues 60–691), and the class-specific IPR036114 (Class VI myosin, motor domain, residues 71–754). Within this motor region lie multiple sub-motor elements: IPR001609 motor-like hits at residues 87–106, 144–169, 187–214, 451–479, and 504–532, which mark conserved subdomains of the actin-activated P-loop NTPase fold. Immediately C-terminal to the motor, IPR049016 (Myosin VI, lever arm, residues 765–913 and 768–882) defines the specialized lever that dictates the reverse stroke direction characteristic of class VI. Farther C-terminal, IPR032412 (Myosin VI, cargo binding domain, residues 1145–1231) provides the tail adaptor interface that couples the motor to vesicular and cortical cargos.

This architecture causes a specific molecular activity profile. The P-loop NTPase core (IPR027417) embedded in the myosin head (IPR001609; IPR036114) confers ATP binding and hydrolysis coupled to conformational changes; the class VI signature (IPR036114) and the reversed lever arm (IPR049016) impose a minus-end-directed bias on actin filaments. The actin-contacting surfaces within the head support GO:0051015 actin filament binding. The lever arm typically binds calmodulin light chains, explaining GO:0032027 myosin light chain binding and the presence of calmodulin-related partners as regulatory inputs. The cargo-binding tail (IPR032412) and SH3-like N-terminus enable adaptor-mediated interactions with membrane proteins and cytoskeletal regulators, rationalizing GO:0017022 myosin binding (assembly with other myosin-associated factors) and GO:0008017 microtubule binding, as the tail and associated adaptors can engage microtubule-associated complexes to coordinate actin–microtubule crosstalk.

From these molecular activities, the biological processes follow. A minus-end-directed actin motor with a dedicated cargo-binding tail is suited to retract and position cortical actin, remodel endocytic vesicles, and drive organelle transport. This directly supports GO:0033275 actin retrograde transport and GO:0032956 regulation of actin cytoskeleton organization. By coupling to endocytic adaptors and clathrin-associated machinery, the motor promotes vesicle internalization and trafficking, aligning with GO:0045921 positive regulation of exocytosis and GO:0032880 regulation of protein localization. The ability to bind microtubules and engage microtubule-associated complexes enables GO:0047497 mitochondrion transport along microtubule and GO:0007018 microtubule-based movement, while cortical recruitment and force generation underlie GO:0006997 nucleus organization and GO:0045217 cell-cell junction maintenance. In development, directed actin–membrane remodeling and vesicle trafficking by this motor contribute to epithelial morphogenesis (GO:0007391 dorsal closure; GO:0016333 morphogenesis of follicular epithelium), collective cell migration (GO:0007298 border follicle cell migration), and tissue-specific morphogenetic events (GO:0007301 follicle cell of egg chamber stalk formation). In the nervous system, actin-based transport and growth cone dynamics are consistent with GO:0030426 growth cone and GO:0007405 neuroblast proliferation, while polarized trafficking supports GO:0045167 asymmetric protein localization involved in cell fate determination. In the germline and sperm, actin-cone dynamics and cargo positioning explain GO:0007291 sperm individualization and GO:0007303 cytoplasmic transport, nurse cell to oocyte. The motor’s role in organizing and maintaining cytoskeletal polarity also contributes to GO:0008363 larval chitin-based cuticle development and GO:0007015 actin cytoskeleton organization. Finally, force-dependent positioning of the mitotic apparatus is consistent with GO:0040001 establishment of mitotic spindle localization.

The cellular component context emerges from the same architecture. The motor and lever arm define membership in GO:0031476 myosin VI complex. The tail’s adaptor interfaces and the minus-end bias target actin-rich cortical structures, matching GO:0005938 cell cortex and GO:0045172 germline ring canal. Engagement with endocytic machinery and clathrin-coated vesicles explains GO:0030139 endocytic vesicle. Participation in actin–microtubule coordination places the motor within GO:0005875 microtubule associated complex. Specialized actin structures in gametogenesis and morphogenesis align with GO:0070864 sperm individualization complex. The observed presence in growth cones and epithelial junctions is a direct consequence of the motor’s ability to bind actin filaments, calmodulin light chains, and cargo adaptors.

Mechanistically, the SH3-like N-terminus and cargo-binding tail recruit adaptors such as Disabled (Dab) and clathrin-associated factors to endocytic pits, while the motor domain hydrolyzes ATP to generate force toward actin filament minus ends, pulling vesicles inward and reorganizing cortical actin. Calmodulin and calmodulin-related protein 97A bind the lever arm to tune stiffness and calcium sensitivity. Dynamin cooperates at endocytic necks, with the motor providing retrograde tension to complete vesicle scission and internalization. Microtubule-associated partners (e.g., PFTAIRE-interacting factor 1A) couple actin-based forces to microtubule-guided transport, coordinating mitochondrial positioning and spindle localization. Interactions with translation initiation factors (eIF3 subunit M) and membrane receptors (N, Appl, Kermit) likely reflect cargo selection and localized translation at cortical sites, while Yuri gagarin and uncharacterized proteins may act as additional adaptors that specify tissue-specific cargo routing. This integrated mechanism explains the protein’s roles across epithelial morphogenesis, neurodevelopment, germline remodeling, and exocytic regulation.

    ## Functional Summary

    An actin-based, minus-end-directed motor that uses an ATP-hydrolyzing head and a calmodulin-regulated lever arm to generate force on actin filaments, while a cargo-binding tail recruits adaptors and membrane receptors to remodel cortical actin, drive endocytic vesicle internalization, and coordinate actin–microtubule crosstalk. By coupling force production to adaptor-mediated cargo selection, it positions organelles, organizes junctions and cortical structures, supports spindle placement, and orchestrates morphogenetic programs in epithelia, neuroblasts, and the germline, including vesicle trafficking and exocytosis control at specialized cortical sites.

    ## UniProt Summary

    Myosins are actin-based motor molecules with ATPase activity. Unconventional myosins serve in intracellular movements. Myosin VI is a minus-end-directed motor protein. Functions in endocytosis.

    ## InterPro Domains

        - IPR004009: Myosin, SH3 domain (domain) [3-54]
    - IPR008989: Myosin S1 fragment, N-terminal (homologous_superfamily) [3-50]
    - IPR004009: Myosin, SH3 domain (domain) [6-49]
    - IPR001609: Myosin head, motor domain-like (domain) [52-767]
    - IPR027417: P-loop containing nucleoside triphosphate hydrolase (homologous_superfamily) [55-830]
    - IPR001609: Myosin head, motor domain-like (domain) [57-766]
    - IPR001609: Myosin head, motor domain-like (domain) [59-754]
    - IPR036961: Kinesin motor domain superfamily (homologous_superfamily) [60-691]
    - IPR036114: Class VI myosin, motor domain (domain) [71-754]
    - IPR001609: Myosin head, motor domain-like (domain) [87-106]
    - IPR001609: Myosin head, motor domain-like (domain) [144-169]
    - IPR001609: Myosin head, motor domain-like (domain) [187-214]
    - IPR001609: Myosin head, motor domain-like (domain) [451-479]
    - IPR001609: Myosin head, motor domain-like (domain) [504-532]
    - IPR049016: Myosin VI, lever arm (domain) [765-913]
    - IPR049016: Myosin VI, lever arm (domain) [768-882]
    - IPR032412: Myosin VI, cargo binding domain (domain) [1145-1231]

    ## GO Term Predictions

    ### Molecular Function


    ### Biological Process


    ### Cellular Component

