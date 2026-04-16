    ---
    provider: bioreason-pro
    model: SFT
    source: huggingface.co/datasets/wanglab/protein_catalogue
    date: '2026-04-04'
    uniprot_id: P87179
    gene: wsc1
    organism: Schizosaccharomyces pombe (strain 972 / ATCC 24843) (Fission yeast)
    ---

    ## Thinking Trace

    I begin with the InterPro architecture. Two overlapping carbohydrate-binding signatures, IPR002889 (Carbohydrate-binding WSC domain, residues 31–119 and 36–109), occupy the N-terminal region, and these are embedded within a broader family assignment, IPR051836 (Kremen receptor family, residues 36–273). The WSC domain is a cysteine-rich, extracellular module that binds cell wall polysaccharides and senses mechanical strain transmitted through the cell wall–plasma membrane interface. Its placement at the N-terminus implies a luminal/extracellular position, consistent with a single-pass type I topology in which the N-terminus is outside and the C-terminus is cytosolic. The Kremen receptor family signature further supports a receptor-like scaffold that couples an extracellular ligand/mechanosensor module to intracellular signaling. This domain order—extracellular WSC followed by a transmembrane segment and a cytosolic tail—causally establishes a transmembrane signaling receptor that detects extracellular cues and transduces them across the membrane.

From this architecture, the molecular function resolves to GO:0004888 transmembrane signaling receptor activity. The WSC domain’s affinity for carbohydrate matrices and its known role in strain sensing explains how the receptor detects mechanical perturbations at the cell surface. Mechanical deformation of the cell wall–membrane interface would be captured by the WSC domain, triggering conformational changes that propagate through the single-pass helix to the cytosolic tail.

This receptor activity drives a cell surface receptor signaling pathway (GO:0007166). In fission yeast, cell wall integrity signaling is executed by a Rho1-centered cascade that culminates in a MAP kinase. The presence of interaction partners Rho1 guanine nucleotide exchange factor 1 and 2, GTP-binding protein Rho1, Protein kinase C-like 2, and MAP kinase kinase skh1/pek1 maps precisely onto the canonical cell wall integrity (CWI) module: the receptor activates Rho1 via its GEFs, Rho1 engages Protein kinase C-like 2, and PKC-like 2 activates the MAPKK Skh1/Pek1, which then phosphorylates downstream effectors. This chain of activation explains how the receptor’s extracellular sensing causes intracellular kinase signaling. Because the WSC domain detects strain, the process-level consequence is detection of mechanical stimulus (GO:0050982), which is converted into kinase signaling that remodels the cell wall and stabilizes the cortex. Sustained CWI signaling also buffers stress-induced apoptosis-like and necrotic pathways; thus, by maintaining wall integrity and kinase activity, the receptor contributes to negative regulation of necrotic cell death (GO:0060547).

The cellular component follows from the topology and the role in polarized growth. A single-pass type I receptor with an extracellular WSC domain must be an integral membrane protein, and in fission yeast, CWI signaling is concentrated at growth sites. Therefore, the protein resides at the plasma membrane of the cell tip (GO:0031520), where polarized exocytosis and wall synthesis occur, and it is an integral component of membrane (GO:0016021). The tip localization ensures that mechanical cues specific to elongation and septation are sensed where wall remodeling is most active.

Mechanistically, the extracellular WSC domain binds cell wall carbohydrates and experiences force under wall stress or growth-driven tension. This mechanical load stabilizes receptor dimerization/oligomerization, which promotes recruitment or activation of Rho1 GEFs at the cytosolic tail, switching Rho1 to its GTP-bound state. Activated Rho1 engages Protein kinase C-like 2, which in turn activates the MAPKK Skh1/Pek1, driving downstream transcriptional and enzymatic programs that reinforce the wall and maintain ion/osmotic balance. Through this signaling, the receptor prevents catastrophic wall rupture and dampens necrotic death pathways. The observed partners—Rho1 GEFs, Rho1, Protein kinase C-like 2, and Skh1/Pek1—fit this mechanism as direct or proximal transducers, while the uncharacterized aminotransferase C6B12.04c may modulate local metabolite pools that influence cell wall biosynthesis or stress responses at the tip.

    ## Functional Summary

    A single-pass plasma membrane receptor in fission yeast that uses an extracellular carbohydrate-binding module to sense mechanical strain at growth sites and transmit this information across the membrane to a Rho1-centered kinase cascade. By activating a protein kinase C–MAP kinase pathway, it maintains cell wall integrity, supports polarized growth at the cell tip, and restrains stress-induced necrotic death.

    ## UniProt Summary

    Cell membrane receptor that activates a cell wall integrity (CWI) signaling pathway involving the PKC1/PEK1/PEK2 and RHO1 proteins. Required for cell wall integrity and cell growth. May be involved in the control of apoptosis.

    ## InterPro Domains

        - IPR002889: Carbohydrate-binding WSC (domain) [31-119]
    - IPR002889: Carbohydrate-binding WSC (domain) [36-109]
    - IPR051836: Kremen receptor (family) [36-273]

    ## GO Term Predictions

    ### Molecular Function


    ### Biological Process


    ### Cellular Component

