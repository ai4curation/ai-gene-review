    ---
    provider: bioreason-pro
    model: SFT
    source: huggingface.co/datasets/wanglab/protein_catalogue
    date: '2026-04-04'
    uniprot_id: Q7Z2B8
    gene: mlcD
    organism: Dictyostelium discoideum (Social amoeba)
    ---

    ## Thinking Trace

    The architecture begins with IPR050230 (Calmodulin/Myosin light chain/Troponin C-like family, residues 2–146), which defines a compact, helical EF-hand calcium sensor specialized for binding target peptides such as IQ motifs on myosins. This family scaffold is refined by IPR011992 (EF-hand domain pair homologous superfamily, residues 5–144), indicating two EF-hand pairs arranged N- and C-terminally. The N-terminal pair is marked by IPR002048 EF-hand domains at residues 8–43, 12–40, and 14–60, with IPR018247 specifying the canonical Ca2+-coordinating loop at residues 21–33 within this first pair. The C-terminal pair is demarcated by IPR002048 domains at residues 79–114 and 81–144, with overlapping confidence windows (83–111 and 83–144) that emphasize a functional Ca2+-binding site in the second lobe. This ordered layout—two Ca2+-binding pairs within a calmodulin-like fold—causes Ca2+-dependent conformational switching that exposes hydrophobic pockets for target engagement.

This EF-hand architecture directly encodes GO:0005509 calcium ion binding as the primary molecular function. The calmodulin/myosin light chain-like family context predicts high-affinity recognition of IQ motifs on myosin heavy chains, supporting GO:0032036 myosin heavy chain binding. In this protein, the paired EF-hands act as a Ca2+ sensor that toggles between low- and high-affinity states for myosin II regulatory segments, thereby modulating motor activity.

Calcium-gated control of myosin II provides a mechanistic route to multiple cellular processes. By binding the myosin II heavy chain, the protein can tune filament assembly and spacing at the cleavage furrow, accounting for GO:0043520 regulation of myosin II filament assembly and GO:0000281 mitotic cytokinesis. Targeting to the division plane is consistent with GO:0071976 protein localization to cell division site. The same Ca2+-dependent exposure of target pockets can regulate interactions with actin regulators, explaining GO:0030041 actin filament polymerization and GO:0030837 negative regulation of actin filament polymerization, as different target states promote or restrain filament growth depending on Ca2+ levels. In endocytic and phagocytic remodeling, Ca2+ spikes recruit this sensor to the cortex to coordinate myosin II contractility and actin assembly, aligning with GO:0006911 phagocytosis, engulfment and GO:0006907 pinocytosis. Rapid Ca2+-triggered assembly at membrane lesions leverages the same mechanism for GO:0001778 plasma membrane repair. By modulating the activity of myosin II and associated enzymes, the protein exerts GO:0043462 regulation of ATP-dependent activity. Its Ca2+-dependent binding to kinases, phosphatases, and small GTPase regulators provides a route to GO:0043087 regulation of GTPase activity and GO:0032092 positive regulation of protein binding. In Dictyostelium development, these cytoskeletal and signaling effects influence multicellular aggregation dynamics (GO:0031152 aggregation involved in sorocarp development) and can restrain proliferative cycles, supporting GO:1903665 negative regulation of asexual reproduction. Nuclear actomyosin and envelope mechanics suggest a role in GO:0006997 nucleus organization.

The EF-hand sensor lacks transmembrane segments and is optimized for dynamic association with actomyosin assemblies, placing it in the GO:0016459 myosin complex and at the GO:0030864 cortical actin cytoskeleton. Its recruitment to large endocytic structures is consistent with GO:0070685 macropinocytic cup. These localizations follow directly from Ca2+-induced exposure of myosin-binding pockets and affinity for IQ motifs on myosin II at the cortex and division site.

A coherent mechanistic model emerges: Ca2+ binding to the N-terminal EF-hands primes the sensor to engage myosin II heavy chain IQ motifs, while the C-terminal EF-hands stabilize the complex and tune affinity. This engagement alters myosin II filament assembly and spacing, thereby controlling contractility and actin polymerization at the cleavage furrow, during macropinocytosis, phagocytosis, and membrane repair. Through Ca2+-dependent docking, the protein likely associates with ROCO-family kinases (roco11, roco6, roco5, roco8) to couple cytoskeletal state to kinase signaling; with the serine/threonine-protein phosphatase 2B catalytic subunit to reset phosphorylation states in a Ca2+-dependent manner; with an inositol 1,4,5-trisphosphate receptor-like protein A to integrate Ca2+ release dynamics; and with the Ras GTPase-activating-like protein gapA to coordinate small GTPase cycles. Together, these interactions position the protein as a Ca2+-sensor that orchestrates myosin II–driven mechanics and signaling at the cortex and division site.

    ## Functional Summary

    A calmodulin-like calcium sensor in Dictyostelium that binds calcium to expose target-specific pockets and engage the myosin II heavy chain. By tuning myosin II filament assembly and contractility at the cortex and cleavage furrow, it coordinates actin polymerization dynamics for cytokinesis, macropinocytosis, phagocytic engulfment, and rapid plasma membrane repair. Its calcium-dependent interactions with kinases, phosphatases, and small GTPase regulators integrate cytoskeletal mechanics with signaling, influencing aggregation during development and restraining asexual proliferation. The protein operates within myosin-containing assemblies at the cortical actin cytoskeleton and macropinocytic cups.

    ## UniProt Summary

    Binds calcium. Binds to the myosin II heavy chain.

    ## InterPro Domains

        - IPR050230: Calmodulin/Myosin light chain/Troponin C-like (family) [2-146]
    - IPR011992: EF-hand domain pair (homologous_superfamily) [5-144]
    - IPR002048: EF-hand domain (domain) [8-43]
    - IPR002048: EF-hand domain (domain) [12-40]
    - IPR002048: EF-hand domain (domain) [14-60]
    - IPR018247: EF-Hand 1, calcium-binding site (binding_site) [21-33]
    - IPR002048: EF-hand domain (domain) [79-114]
    - IPR002048: EF-hand domain (domain) [81-144]
    - IPR002048: EF-hand domain (domain) [83-111]
    - IPR002048: EF-hand domain (domain) [83-144]

    ## GO Term Predictions

    ### Molecular Function


    ### Biological Process


    ### Cellular Component

