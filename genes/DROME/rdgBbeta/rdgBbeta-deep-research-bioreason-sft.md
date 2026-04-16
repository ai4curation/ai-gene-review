    ---
    provider: bioreason-pro
    model: SFT
    source: huggingface.co/datasets/wanglab/protein_catalogue
    date: '2026-04-04'
    uniprot_id: Q9U9P7
    gene: rdgBbeta
    organism: Drosophila melanogaster (Fruit fly)
    ---

    ## Thinking Trace

    The architecture begins with IPR023393 (START-like domain superfamily, residues 2–263), a fold that creates a deep hydrophobic cavity for lipid sequestration and exchange. Nested within this scaffold is IPR055261 (Phosphatidylinositol transfer protein, N-terminal domain, residues 2–244), which defines the specific PITP topology that opens and closes a lipid-binding pocket. Multiple family-level signatures of the phosphatidylinositol transfer protein lineage are embedded across the sequence—IPR001666 (PITP family) at residues 3–254, 17–36, 84–104, 110–125, 193–208, and 213–232—marking conserved motifs that line the cavity and the gating elements that control lipid capture and release. The ordered nesting of a PITP-specific N-terminal domain inside a START-like superfamily fold causes high-affinity, monomeric lipid transfer between membranes without vesicle budding or fusion.

This PITP fold enforces a molecular function centered on selective lipid exchange. The conserved cavity and gating residues accommodate phosphatidylinositol and phosphatidylcholine, enabling GO:0008526 phosphatidylinositol transfer activity and GO:0008525 phosphatidylcholine transporter activity. Because the cavity is optimized for neutral and anionic glycerophospholipids, the mechanism is a cycle of membrane docking, lipid extraction into the hydrophobic pocket, transit through the cytosol, and deposition at a target membrane.

Lipid transfer of PI and PC has direct consequences for membrane composition and signaling during cell division. By delivering PI to specific membrane subdomains, the protein sustains phosphoinositide synthesis and curvature-sensitive recruitment of cytokinetic machinery; by shuttling PC, it maintains bilayer integrity and supports membrane expansion at the ingressing furrow. These activities drive the processes formalized as GO:0007110 meiosis I cytokinesis and GO:0007111 meiosis II cytokinesis, and extend to GO:0007112 male meiosis cytokinesis and GO:0048137 spermatocyte division, where precise membrane remodeling is essential. The same lipid supply and signaling flux coordinate with the actomyosin apparatus, promoting GO:0000916 actomyosin contractile ring contraction and GO:0036090 cleavage furrow ingression by ensuring a competent, lipid-rich cortex that can withstand contractile forces and by positioning PI pools that recruit small GTPases and effectors. Proper PI availability also influences microtubule–cortex communication and membrane–microtubule interfaces, contributing to GO:0000212 meiotic spindle organization.

The domain architecture lacks transmembrane segments and secretion signals, indicating a soluble protein that cycles on and off membranes. Its action requires proximity to sites of intense membrane turnover and signaling. Thus, it operates in the cytoplasm and transiently associates with the GO:0005794 Golgi apparatus to acquire and dispatch lipids, with the GO:0032154 cleavage furrow where cytokinesis occurs, and with the GO:0031965 nuclear membrane during meiotic stages when nuclear envelope dynamics and membrane continuity are critical. This distribution is consistent with a soluble lipid-transfer factor that concentrates at division sites and organelles engaged in lipid trafficking.

Mechanistically, the protein likely docks to donor membranes via basic surface patches and amphipathic elements, captures PI or PC into its START-like cavity, and releases the lipid at target membranes to sustain phosphoinositide synthesis and bilayer homeostasis. At the cleavage furrow and nuclear envelope, it plausibly collaborates with small GTPases (e.g., ARF and RAB family members) and phosphoinositide kinases to position PI pools that recruit actomyosin regulators and membrane-sculpting factors. It may also engage cytokinetic scaffolds at the furrow to synchronize lipid supply with contractile ring constriction and with spindle–cortex communication during meiosis.

    ## Functional Summary

    A soluble lipid-transfer factor in fruit fly that uses a deep hydrophobic cavity to extract and shuttle phosphatidylinositol and phosphatidylcholine between membranes. By supplying these lipids to division sites and organelles, it sustains phosphoinositide signaling and bilayer integrity required for spindle organization, contractile ring function, and membrane expansion during meiotic and spermatocyte cytokinesis. It operates in the cytoplasm and transiently associates with the Golgi, the cleavage furrow, and the nuclear envelope to coordinate lipid flux with cell division mechanics.

    ## UniProt Summary

    Catalyzes the transfer of phosphatidylinositol and phosphatidylcholine between membranes.

    ## InterPro Domains

        - IPR023393: START-like domain superfamily (homologous_superfamily) [2-263]
    - IPR055261: Phosphatidylinositol transfer protein, N-terminal (domain) [2-244]
    - IPR001666: Phosphatidylinositol transfer protein (family) [3-254]
    - IPR001666: Phosphatidylinositol transfer protein (family) [17-36]
    - IPR001666: Phosphatidylinositol transfer protein (family) [84-104]
    - IPR001666: Phosphatidylinositol transfer protein (family) [110-125]
    - IPR001666: Phosphatidylinositol transfer protein (family) [193-208]
    - IPR001666: Phosphatidylinositol transfer protein (family) [213-232]

    ## GO Term Predictions

    ### Molecular Function


    ### Biological Process


    ### Cellular Component

