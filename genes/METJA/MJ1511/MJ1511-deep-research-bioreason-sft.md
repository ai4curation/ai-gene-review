    ---
    provider: bioreason-pro
    model: SFT
    source: huggingface.co/datasets/wanglab/protein_catalogue
    date: '2026-04-04'
    uniprot_id: Q58906
    gene: MJ1511
    organism: Methanocaldococcus jannaschii (strain ATCC 43067 / DSM 2661 / JAL-1 / JCM 10045 / NBRC 100440) (Methanococcus jannaschii)
    ---

    ## Thinking Trace

    I begin with the InterPro architecture. Three overlapping signatures define a compact AhpD-like fold: IPR029032 (AhpD-like homologous superfamily, residues 2–101) and IPR029032 (AhpD-like homologous superfamily, residues 10–104) encompass IPR003779 (Alkyl hydroperoxide reductase AhpD/CMD-like domain, residues 18–99). This arrangement places a canonical AhpD/CMD catalytic core centrally, flanked by the broader superfamily envelope. AhpD-like domains are small, soluble redox modules that typically harbor a conserved Cys-containing active site (often a Cys–X(–)4/Cys–X(n)–Cys motif) and assemble as dimers or higher-order oligomers. The absence of transmembrane segments or signal peptides implies a cytosolic enzyme. In the AhpD/CMD lineage, the fold creates a redox-active pocket that cycles between reduced and disulfide-oxidized states and couples to partner electron carriers.

This fold directly causes thiol–disulfide exchange chemistry. The catalytic cysteines form a transient disulfide that is reduced by an external electron donor, enabling transfer of reducing equivalents to disulfide-containing acceptors. That mechanism matches the molecular function formalized as GO:0016671 oxidoreductase activity, acting on a sulfur group of donors, disulfide as acceptor. In the present system, the physiological electron donor is rubredoxin reduced by a flavodoxin reductase using NAD(P)H, and the acceptor is the disulfide in the FAD cofactor of the dehydrogenase subunit of the desulfoferrodoxin complex. The AhpD-like pocket thus serves as the redox relay that resets the FAD from a disulfide to a dithiol state, priming the dehydrogenase for another catalytic turnover.

By enabling turnover of 2-hydroxy-6-oxo-3-methylchromo-3-carboxylate (HOCMC), this redox relay drives a specific step in the degradation of 5-hydroxymethylfurfural (HMF). HMF is a toxic by-product of lignocellulosic biomass processing; its detoxification proceeds through ring-oxidation and decarboxylation to HOCMC, which then requires reduction to complete catabolism. The AhpD-like oxidoreductase therefore sustains flux through the HMF catabolic route, aligning with GO:0046279 5-hydroxymethylfurfural catabolic process. The chemistry is consistent with an EC 1.8.-.- class reaction, where a sulfur-based redox couple mediates electron transfer to a flavin disulfide.

The structural and mechanistic features indicate a soluble enzyme that operates in the cytosol, where NAD(P)H, flavodoxin/flavodoxin reductase, rubredoxin, and the desulfoferrodoxin dehydrogenase co-reside. Functionally, it associates with the desulfoferrodoxin assembly, which constitutes a defined redox enzyme ensemble; this supports localization to the GO:1990204 oxidoreductase complex. Given the lack of targeting signals and the metabolic context, the most plausible subcellular site is the cytosol.

Mechanistically, I propose the following: reduced flavodoxin reduces rubredoxin, which in turn directly reduces the AhpD-like active site disulfide. The now-reduced AhpD transfers electrons to the FAD disulfide within the dehydrogenase subunit of desulfoferrodoxin, regenerating the catalytic dithiol state required for continued reduction of HOCMC. The enzyme likely forms a transient complex with the desulfoferrodoxin dehydrogenase and rubredoxin to enable efficient electron channeling. Consistent with this, plausible interaction partners include the desulfoferrodoxin (putative rbo) dehydrogenase, rubredoxin-like non-heme iron proteins (as electron shuttles), and additional conserved hypothetical proteins that may act as adaptors or scaffolds stabilizing the oxidoreductase complex in the archaeal cytosol.

    ## Functional Summary

    A small, soluble redox relay enzyme in Methanocaldococcus jannaschii that uses a cysteine-based active site to accept electrons from the rubredoxin/flavodoxin/NAD(P)H pathway and reduce the flavin disulfide within the dehydrogenase subunit of the desulfoferrodoxin complex. By regenerating the catalytic dithiol state required for turnover, it drives the reduction step in the detoxification of 5-hydroxymethylfurfural, converting the intermediate HOCMC to its reduced product and sustaining flux through lignocellulosic-derived aromatic catabolism. It likely operates in the cytosol as part of an oxidoreductase assembly, forming transient electron-transfer complexes with rubredoxin and the desulfoferrodoxin dehydrogenase.

    ## UniProt Summary

    Component of the desulfoferrodoxin complex, involved in the degradation of 5-hydroxymethylfurfural (HMF), a toxic by-product of lignocellulosic biomass processing. The complex catalyzes the reduction of 2-hydroxy-6-oxo-3-methylchromo-3-carboxylic acid (HOCMC). AhpD reduces the FAD cofactor of the dehydrogenase subunit (rbo) using reduced flavodoxin as an electron donor.

    ## InterPro Domains

        - IPR029032: AhpD-like (homologous_superfamily) [2-101]
    - IPR029032: AhpD-like (homologous_superfamily) [10-104]
    - IPR003779: Alkyl hydroperoxide reductase AhpD/CMD-like (domain) [18-99]

    ## GO Term Predictions

    ### Molecular Function


    ### Biological Process


    ### Cellular Component

