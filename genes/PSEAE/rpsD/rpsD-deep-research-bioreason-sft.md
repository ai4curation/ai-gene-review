    ---
    provider: bioreason-pro
    model: SFT
    source: huggingface.co/datasets/wanglab/protein_catalogue
    date: '2026-04-04'
    uniprot_id: O52759
    gene: rpsD
    organism: Pseudomonas aeruginosa (strain ATCC 15692 / DSM 22644 / CIP 104116 / JCM 14847 / LMG 12228 / 1C / PRS 101 / PAO1)
    ---

    ## Thinking Trace

    I begin with the InterPro architecture. The sequence is covered almost entirely by bacterial uS4 family signatures: IPR005709 (Small ribosomal subunit protein uS4, bacteria, residues 1–206) spans the full length, with a refined bacterial family call IPR005709 [3–206] and a core family IPR022801 (Small ribosomal subunit protein uS4, residues 7–152). The N-terminus is demarcated by IPR001912 (uS4, N-terminal domain, residues 3–95), followed by a conserved site IPR018079 (uS4 conserved site, residues 94–118) that sits at the junction between the N-terminal region and the canonical RNA-binding core. The central-to-C-terminal half is defined by the S4 RNA-binding fold: IPR036986 (RNA-binding S4 domain superfamily, residues 95–191) and its specific instances IPR002942 (RNA-binding S4 domain, residues 96–160) and IPR002942 (RNA-binding S4 domain, residues 97–143). This ordered layout—an N-terminal module leading into a conserved site and then a compact S4 RNA-binding fold—creates a basic, positively charged surface optimized to recognize and stabilize structured rRNA.

This architecture causes high-affinity binding to the bacterial 16S rRNA, particularly the 3′ major domain. The S4 fold clamps helical junctions and phosphate backbones, while the N-terminal region positions the protein on the platform of the small subunit. The conserved site at residues 94–118 likely contributes key contact residues that nucleate assembly on the rRNA scaffold. Consequently, the molecular function is rRNA binding (GO:0019843), with specificity for 16S rRNA.

By binding and stabilizing the 16S rRNA, uS4 seeds construction of the 30S particle. Its RNA-binding surface organizes early assembly intermediates and recruits additional small-subunit proteins, driving ribosomal small subunit assembly (GO:0000028). Once assembled, the mature 30S engages mRNA and tRNA to execute decoding; uS4, anchored on the platform, helps maintain the geometry of the mRNA channel and the rRNA framework, thereby contributing directly to translation (GO:0006412).

The absence of transmembrane segments and the ribosomal identity place the protein in the cytoplasm, where bacterial ribosomes reside. More specifically, its stable incorporation into the small subunit defines the cellular component as the cytosolic small ribosomal subunit (GO:0022627), consistent with a cytoplasmic localization.

Mechanistically, uS4 binds the 16S rRNA early, stabilizes helix junctions, and creates docking surfaces for other 30S proteins such as S2, S10, S13, and S17. During subunit joining and initiation, its position near the intersubunit interface brings it into transient proximity with large-subunit proteins, explaining functional contacts with L10, L17, L18, L20, L24, and L36. These interactions likely reflect assembly checkpoints and initiation-state contacts rather than permanent binary complexes, with uS4 acting as a structural organizer that ensures accurate 30S architecture and efficient translation initiation.

    ## Functional Summary

    A cytoplasmic small-subunit ribosomal protein that binds 16S rRNA to nucleate and stabilize early steps of 30S assembly on the platform, then remains as a structural organizer during translation. Its basic RNA-binding fold grips structured rRNA elements to shape the small-subunit architecture, recruit additional proteins, and maintain the geometry of the decoding environment, thereby supporting accurate and efficient protein synthesis.

    ## UniProt Summary

    One of the primary rRNA binding proteins, it binds directly to 16S rRNA where it nucleates assembly of the platform of the 30S subunit.

    ## InterPro Domains

        - IPR005709: Small ribosomal subunit protein uS4, bacteria (family) [1-206]
    - IPR001912: Small ribosomal subunit protein uS4, N-terminal (domain) [3-95]
    - IPR005709: Small ribosomal subunit protein uS4, bacteria (family) [3-206]
    - IPR022801: Small ribosomal subunit protein uS4 (family) [7-152]
    - IPR018079: Small ribosomal subunit protein uS4, conserved site (conserved_site) [94-118]
    - IPR036986: RNA-binding S4 domain superfamily (homologous_superfamily) [95-191]
    - IPR002942: RNA-binding S4 domain (domain) [96-160]
    - IPR002942: RNA-binding S4 domain (domain) [97-143]

    ## GO Term Predictions

    ### Molecular Function


    ### Biological Process


    ### Cellular Component

