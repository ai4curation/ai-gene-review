    ---
    provider: bioreason-pro
    model: SFT
    source: huggingface.co/datasets/wanglab/protein_catalogue
    date: '2026-04-04'
    uniprot_id: Q8RX66
    gene: NEK3
    organism: Arabidopsis thaliana (Mouse-ear cress)
    ---

    ## Thinking Trace

    I begin with the InterPro architecture. The polypeptide is assigned to IPR050660 (NEK Serine/Threonine Protein Kinase family, residues 1–518), which frames the entire sequence as a NIMA-related kinase with a conserved catalytic core and extended regulatory tail. Within this family envelope, the N-terminal half contains IPR011009 (Protein kinase-like domain superfamily, residues 1–301), and, more specifically, a canonical bilobal catalytic module defined by IPR000719 (Protein kinase domain, residues 4–257) and IPR000719 (Protein kinase domain, residues 4–258). The ATP-binding P-loop and adjacent glycine-rich segment are captured by IPR017441 (Protein kinase, ATP binding site, residues 10–33), while the catalytic HRD/DFG-centered machinery is pinpointed by IPR008271 (Serine/threonine-protein kinase, active site, residues 125–137). The ordered layout—ATP-binding segment leading into the catalytic loop within a NEK-family scaffold—causes ATP-dependent transfer of phosphate to serine/threonine residues on protein substrates. The NEK family context further implies regulation by activation-loop phosphorylation and docking interactions mediated by the C-terminal regulatory region (beyond residue ~257 up to 518), which typically confers subcellular targeting and substrate selection.

From this domain logic, the molecular function resolves to protein serine/threonine kinase activity (GO:0004674) driven by ATP binding (GO:0005524). The presence of broad interaction surfaces in NEK regulatory tails and the need to dock substrates and adaptors supports protein binding (GO:0005515). Together, these features define an enzyme that phosphorylates protein targets in a context-dependent manner.

NEK kinases are well known to control microtubule behavior. In plants, the cortical microtubule array dictates cell wall deposition patterns and anisotropic growth. A NEK with a long regulatory tail is well-suited to couple kinase activity to microtubule-associated proteins, thereby promoting microtubule bundle formation (GO:0001578). Phosphorylation of bundling factors, severing enzymes, or crosslinkers would stabilize parallel arrays and increase bundle longevity, which in turn drives directional expansion of specialized cells. In the male gametophyte, this control over cortical array stability and orientation provides the mechanical basis for polarized elongation, aligning with pollen development (GO:0009555). Thus, the catalytic architecture explains how the protein enforces microtubule bundle integrity and supports tip growth in pollen.

The cellular component follows from the same chain. A soluble kinase lacking transmembrane segments but equipped for cytoskeletal targeting will partition to the cytoplasm and associate with the microtubule cytoskeleton. The explicit functional tie to cortical microtubules places the protein at the cortical microtubule track (GO:0055028), embedded within the broader cytoskeleton (GO:0005856) and cytoplasm (GO:0005737). This localization allows direct access to substrates that shape the cortical array and to trafficking machinery that delivers wall materials.

A mechanistic hypothesis emerges: the kinase docks onto cortical microtubules via its NEK-family regulatory region, where it phosphorylates microtubule-associated proteins to promote bundle formation and persistence. SNAP29, a membrane trafficking factor at the plasma membrane–endomembrane interface, could act as a scaffold that positions the kinase near exocytic hotspots where cortical microtubules guide vesicle delivery. The T-complex protein 1 subunit epsilon (a CCT chaperonin component) likely assists in folding and assembly of the kinase and/or its microtubule-binding partners, ensuring a competent cortical complex. Beta-glucosidase 20, involved in cell wall carbohydrate remodeling, may be indirectly regulated through phosphorylation of trafficking or exocytosis components that control its delivery to growth sites. In aggregate, the kinase forms a cortical module that stabilizes microtubule bundles to steer vesicle traffic and cell wall deposition during pollen tube elongation.

    ## Functional Summary

    A cytoplasmic, cortical-cytoskeleton–associated serine/threonine kinase that promotes microtubule bundle formation to support polarized growth during pollen development. Its N-terminal catalytic core binds ATP and phosphorylates protein substrates, while a NEK-family regulatory region targets the enzyme to cortical microtubules and provides docking interfaces for partners. By stabilizing microtubule bundles, it organizes vesicle delivery and cell wall deposition patterns required for elongating pollen tubes, likely operating in concert with membrane trafficking and protein-folding factors at the cell cortex.

    ## UniProt Summary

    Involved in the regulation of cortical microtubule bundle integrity. Required for pollen tube elongation.

    ## InterPro Domains

        - IPR011009: Protein kinase-like domain superfamily (homologous_superfamily) [1-301]
    - IPR050660: NEK Serine/Threonine Protein Kinase (family) [1-518]
    - IPR000719: Protein kinase domain (domain) [4-257]
    - IPR000719: Protein kinase domain (domain) [4-258]
    - IPR017441: Protein kinase, ATP binding site (binding_site) [10-33]
    - IPR008271: Serine/threonine-protein kinase, active site (active_site) [125-137]

    ## GO Term Predictions

    ### Molecular Function


    ### Biological Process


    ### Cellular Component

