    ---
    provider: bioreason-pro
    model: SFT
    source: huggingface.co/datasets/wanglab/protein_catalogue
    date: '2026-04-04'
    uniprot_id: Q550S9
    gene: tlcd4b
    organism: Dictyostelium discoideum (Social amoeba)
    ---

    ## Thinking Trace

    I begin with the InterPro architecture. The polypeptide is dominated by IPR050846 (TLC domain-containing family) spanning residues 10–247, within which lie two overlapping signatures of the same core module: IPR006634 (TRAM/LAG1/CLN8 homology domain, TRAM/LAG1/CLN8) at residues 44–243 and again at residues 48–235. This arrangement defines a compact, multi-pass membrane protein whose transmembrane helices scaffold a conserved TLC catalytic center. The TLC fold positions a histidine–aspartate motif within the membrane to activate a water molecule and cleave the amide bond of ceramide. This architecture causes ceramidase chemistry—hydrolysis of ceramide into sphingosine and a free fatty acid—thereby establishing the molecular function formalized as GO:0017040 N-acylsphingosine amidohydrolase activity.

Ceramidase activity directly rewires the flux of sphingolipids, shifting ceramide toward sphingosine and fatty acid pools. This enzymatic step is a control point in the ceramide metabolic process, aligning with GO:0006672 ceramide metabolic process. In amoebae, altering ceramide versus sphingosine balance modulates membrane biophysical properties and signaling, which in turn affects how cells interface with their surroundings.

The TLC domain’s multi-pass topology and lack of soluble domains indicate an integral membrane enzyme. The subcellular location points to the cell membrane, which is the site where ceramide is abundant and where signaling outputs are propagated; thus the cellular component is best captured by GO:0016021 integral component of membrane and GO:0005886 plasma membrane. The presence of GO:0031012 extracellular matrix suggests that, although the catalytic site resides in the membrane, the functional consequences extend to the extracellular milieu—consistent with sphingolipid remodeling influencing secretion, adhesion, or matrix organization at the cell surface.

Mechanistically, the transmembrane TLC core forms a hydrophobic pocket that binds ceramide within the bilayer. A membrane-embedded histidine–aspartate dyad activates a water molecule for nucleophilic attack on the ceramide amide bond, yielding sphingosine and a fatty acid. The reaction at the plasma membrane can rapidly tune local ceramide-dependent signaling and membrane order, with products further routed to downstream pathways. I therefore hypothesize interactions with ceramide transporters (e.g., CERT-like proteins) that deliver substrate to the membrane, with sphingosine kinases that channel the product into signaling lipids, and with membrane scaffolds (e.g., tetraspanins or flotillins) that cluster the enzyme in microdomains where extracellular matrix engagement occurs. Additional contacts with acyl-CoA synthetases and fatty acid transport proteins would couple the liberated fatty acid to re-esterification or export, while associations with cell-adhesion receptors could coordinate lipid remodeling with extracellular matrix binding and remodeling.

    ## Functional Summary

    A multi-pass membrane enzyme in social amoeba that hydrolyzes ceramide within the lipid bilayer to generate sphingosine and free fatty acid, thereby redirecting sphingolipid flux at the cell surface. By operating at the plasma membrane, it modulates local ceramide-dependent signaling and membrane properties, with consequences that extend to the extracellular environment where matrix engagement occurs. The transmembrane catalytic center likely uses a membrane-embedded histidine–aspartate motif to activate water for amide bond cleavage, positioning the enzyme as a key regulator of ceramide metabolism and cell–matrix interface dynamics.

    ## UniProt Summary

    Has ceramidase activity.

    ## InterPro Domains

        - IPR050846: TLC domain-containing (family) [10-247]
    - IPR006634: TRAM/LAG1/CLN8 homology domain (domain) [44-243]
    - IPR006634: TRAM/LAG1/CLN8 homology domain (domain) [48-235]

    ## GO Term Predictions

    ### Molecular Function


    ### Biological Process


    ### Cellular Component

