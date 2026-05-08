    ---
    provider: bioreason-pro
    model: SFT
    source: huggingface.co/datasets/wanglab/protein_catalogue
    date: '2026-04-04'
    uniprot_id: P9WPC3
    gene: clpP2
    organism: Mycobacterium tuberculosis (strain ATCC 25618 / H37Rv)
    ---

    ## Thinking Trace

    I begin with the InterPro architecture, which is dominated by signatures of the ATP-dependent ClpP protease core. The central scaffold is IPR029045 (ClpP/crotonase-like domain superfamily, residues 24–208), a double β–β–α sandwich that forms the proteolytic barrel of ClpP-like peptidases. Nested within this fold are multiple family-level matches to the proteolytic subunit: IPR001907 (ATP-dependent Clp protease proteolytic subunit, residues 15–207; 31–46; 33–203; 71–91; 102–119; 182–201) and IPR023562 (Clp protease proteolytic subunit / Translocation-enhancing protein TepA, residues 17–208; 30–206). These overlapping entries collectively define the canonical ClpP protease subunit that assembles into a tetradecameric barrel with active sites facing the chamber interior. Two catalytic-site annotations pinpoint the catalytic machinery: IPR018215 (ClpP, Ser active site, residues 102–113) and IPR033135 (ClpP, histidine active site, residues 124–137). Together with the conserved acidic residue in the same family signatures, these features create a Ser–His–Asp triad that drives peptide-bond hydrolysis. The repeated IPR001907 entries across distinct spans indicate that multiple conserved submotifs are present, consistent with a proteolytically active barrel that requires partner ATPases for substrate delivery.

This architecture causes serine-type endopeptidase activity: the catalytic serine within the ClpP fold performs nucleophilic attack on peptide bonds, while the histidine and aspartate complete the charge-relay system. Because ClpP barrels lack ATPase modules, the protease itself does not hydrolyze ATP; instead, it binds AAA+ ATPase partners (e.g., ClpX or ClpC) that unfold substrates and translocate them through axial pores into the proteolytic chamber. The presence of multiple ClpP family signatures and the catalytic-site annotations therefore specify the molecular functions as serine-type endopeptidase activity and protein binding (the latter arising from obligatory assembly with AAA+ unfoldases and adaptor proteins).

At the process level, a ClpP barrel that is activated by ATP-dependent unfoldases is central to protein quality control. Under heat stress, misfolded and damaged proteins accumulate; AAA+ partners recognize degrons and feed substrates into the ClpP chamber for processive degradation. This mechanistic coupling places the enzyme in the response to heat, where it eliminates aggregation-prone proteins and restores proteostasis. More broadly, the same chemistry underlies cellular protein catabolic processes, including turnover of regulatory factors and removal of damaged proteins.

The cellular context follows from the protease’s solubility and its reliance on cytosolic AAA+ partners. The absence of transmembrane segments and the soluble ClpP fold indicate a cytosolic enzyme, aligning with cytosol as a primary location. In bacteria, AAA+ proteases can transiently associate with the inner membrane and the cell wall interface during stress responses or when processing envelope-associated substrates; this explains observed associations with the plasma membrane and peptidoglycan-based cell wall as peripheral or transiently engaged locales rather than integral residence.

Mechanistically, the protein assembles into a tetradecameric barrel that binds ClpX or ClpC via their N-terminal domains. ATP hydrolysis by the AAA+ partners drives substrate unfolding and axial translocation, positioning polypeptides into the ClpP chamber where the Ser–His–Asp triad executes endoproteolysis. Chaperones such as trigger factor and GroES/GroEL and disaggregase ClpB likely hand off or remodel substrates to the AAA+–ClpP complexes. The interaction list supports this model: ClpP1 suggests hetero-oligomeric pairing of ClpP paralogs; ClpX and ClpC are the ATPase unfoldases that gate substrate entry; ClpB, Tig (trigger factor), and GroES cooperate upstream to triage misfolded proteins; and additional partners (e.g., ClpB protein F84.1, GroES, and uncharacterized large proteins annotated as possible ClpC-like ATPases) suggest a network of proteostasis factors. Association with the 50S ribosomal protein L11 (RplK) hints at cotranslational quality control or turnover of ribosome-associated factors during stress. Overall, the domain architecture dictates a serine endopeptidase that, when coupled to AAA+ ATPases, degrades misfolded and regulatory proteins to maintain proteostasis during heat stress in the cytosol, with transient membrane/cell wall engagement for envelope-related quality control.

    ## Functional Summary

    A cytosolic protease that assembles into a tetradecameric barrel and, when engaged by AAA+ ATPase partners, degrades misfolded, damaged, or regulatory proteins to maintain proteostasis during heat stress. It recognizes substrates via partner ATPases, uses ATP hydrolysis by those partners to unfold and translocate polypeptides into its proteolytic chamber, and employs a catalytic serine–histidine–aspartate triad to cleave internal peptide bonds. Although primarily soluble, it likely interfaces with membrane- and cell wall–proximal quality-control pathways during envelope stress, coordinating with chaperones and disaggregases to triage substrates.

    ## UniProt Summary

    Component of the ClpC-ClpP protease. Involved in degradation of denatured proteins. Has serine protease activity.

    ## InterPro Domains

        - IPR001907: ATP-dependent Clp protease proteolytic subunit (family) [15-207]
    - IPR023562: Clp protease proteolytic subunit /Translocation-enhancing protein TepA (family) [17-208]
    - IPR029045: ClpP/crotonase-like domain superfamily (homologous_superfamily) [24-208]
    - IPR023562: Clp protease proteolytic subunit /Translocation-enhancing protein TepA (family) [30-206]
    - IPR001907: ATP-dependent Clp protease proteolytic subunit (family) [31-46]
    - IPR001907: ATP-dependent Clp protease proteolytic subunit (family) [33-203]
    - IPR001907: ATP-dependent Clp protease proteolytic subunit (family) [71-91]
    - IPR001907: ATP-dependent Clp protease proteolytic subunit (family) [102-119]
    - IPR018215: ClpP, Ser active site (active_site) [102-113]
    - IPR001907: ATP-dependent Clp protease proteolytic subunit (family) [123-142]
    - IPR033135: ClpP, histidine active site (active_site) [124-137]
    - IPR001907: ATP-dependent Clp protease proteolytic subunit (family) [182-201]

    ## GO Term Predictions

    ### Molecular Function


    ### Biological Process


    ### Cellular Component

