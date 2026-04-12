    ---
    provider: bioreason-pro
    model: SFT
    source: huggingface.co/datasets/wanglab/protein_catalogue
    date: '2026-04-04'
    uniprot_id: O08675
    gene: F2rl2
    organism: Mus musculus (Mouse)
    ---

    ## Thinking Trace

    I begin by dissecting the InterPro architecture and its order along the sequence. Multiple family signatures specific to protease-activated receptor 3 cluster in the extreme N-terminus and early transmembrane-proximal regions: IPR003943 (Protease-activated receptor 3 family) appears at residues 2–22, 30–51, 56–73, 77–93, 118–132, 197–214, 232–243, and 292–337, while broader protease-activated receptor family marks (IPR003912) occur at 83–100, 150–164, 262–273 and 262–273. These N-terminal PAR3-specific motifs define a protease-cleavable segment that, once cut, exposes a tethered ligand (“activation peptide”) that folds back to engage and activate the receptor. Downstream, a canonical rhodopsin-like G protein-coupled receptor (GPCR) 7-transmembrane core is delineated by IPR017452 (GPCR, rhodopsin-like, 7TM domain) spanning residues 110–357, reinforced by multiple overlapping rhodopsin-like family signatures (IPR000276) at 95–119, 116–357, 127–148, 172–194, 208–229, 298–322 and 339–365. This arrangement—PAR3-specific N-terminus followed by a 7TM GPCR core—causally establishes a protease-gated GPCR whose activation mechanism is proteolytic unmasking of an intramolecular agonist.

From this architecture, the molecular function resolves as follows. The PAR3-specific N-terminus, once cleaved by trypsin-like serine proteases, generates an activation peptide that functions as an intrinsic ligand; this confers receptor ligand activity (GO:0048018) in the sense of an auto-ligand that binds the receptor’s own N-terminus. Engagement of the 7TM core initiates G protein coupling. The rhodopsin-like 7TM domain supports G protein activation; while the receptor is not a GTPase itself, its signaling complex recruits RGS proteins that accelerate GTP hydrolysis on Gα subunits. Through this scaffolding role, the receptor complex exerts GTPase activator activity (GO:0005096) via associated RGS proteins. The same GPCR signaling triggers phospholipase C-β activation (GO:0043532 phospholipase C activator activity) and protein kinase C activation (GO:0043537 protein kinase C activator activity) by coupling to Gq/11 and/or G12/13, respectively. Downstream, the pathway modulates calcium channels, providing calcium channel regulator activity (GO:0005246), and directly exhibits protein tyrosine kinase activator activity (GO:0043535) by engaging receptor-proximal tyrosine kinases such as Src. The receptor’s ability to functionally gate ion channels through Gβγ and second messengers supports ion channel regulator activity involved in ligand-gated ion channel signaling (GO:0099108). Collectively, these activities are the expected consequences of a PAR3-class rhodopsin-like GPCR.

These molecular activities drive specific biological processes. Proteolytic activation by trypsin-like enzymes (e.g., trypsin, matriptase, kallikreins) positions the receptor as a sensor of extracellular protease tone, translating protease availability into intracellular G protein signaling. The PLC/PKC axis and calcium channel regulation modulate excitability and secretion, aligning with participation in a ligand-gated ion channel signaling pathway (GO:1990806) via G protein–dependent control of channel opening probability and trafficking. In endocrine contexts, the same signaling enhances secretory output, consistent with positive regulation of insulin secretion (GO:0032024). In epithelia, the receptor’s apical positioning and protease gating enable rapid responses to luminal proteases, shaping barrier function and inflammatory signaling.

The cellular component follows directly from the 7TM GPCR core and the PAR-specific N-terminus: the protein is a multi-pass integral membrane receptor at the plasma membrane. Epithelial polarity cues and protease access favor localization to the apical plasma membrane (GO:0016324), where luminal proteases can cleave the N-terminus and initiate signaling. The multi-pass nature is inherent to the rhodopsin-like 7TM domain.

Mechanistically, proteolytic cleavage of the N-terminal PAR3 module exposes the tethered ligand, which binds intramolecularly to the receptor’s extracellular loops/orthosteric pocket, stabilizing an active 7TM conformation. This conformation couples to heterotrimeric G proteins (primarily Gq/11 and G12/13), leading to PLCβ activation, IP3/DAG production, Ca2+ mobilization via calcium channels, PKC activation, and engagement of tyrosine kinases. RGS proteins bound to the receptor complex accelerate GTP hydrolysis on Gα, shaping signal timing. The receptor likely forms functional complexes with other protease-activated receptors, particularly Proteinase-activated receptor 4, to diversify responses to distinct protease cleavages. The activation peptide fragment 1 represents the intramolecular agonist generated by initial cleavage, and additional extracellular partners plausibly include trypsin-like serine proteases (trypsin, matriptase, kallikreins) and intracellular effectors such as PLCβ isoforms, GNAQ/GNA11, GNA12/GNA13, RGS proteins, Src-family kinases, and epithelial calcium channels that implement the downstream physiological outputs.

    ## Functional Summary

    A multi-pass plasma membrane receptor in mouse that is activated by proteolytic cleavage of its N-terminus, exposing a tethered activation peptide that turns on a rhodopsin-like signaling core. Upon activation, it couples to heterotrimeric G proteins to stimulate phospholipase C, mobilize intracellular calcium, regulate ion channels, and activate protein kinase C and tyrosine kinases. These signaling outputs modulate epithelial and endocrine physiology, including enhancing insulin secretion and shaping responses to luminal proteases at the apical surface, with timing and amplitude tuned by associated GTPase-accelerating regulators and crosstalk with related protease-activated receptors.

    ## UniProt Summary

    Receptor for trypsin. When proteolytically cleaved in the N-terminus, the activation peptide internally binds and activates the receptor.

    ## InterPro Domains

        - IPR003943: Protease-activated receptor 3 (family) [2-22]
    - IPR003943: Protease-activated receptor 3 (family) [30-51]
    - IPR003943: Protease-activated receptor 3 (family) [56-73]
    - IPR003943: Protease-activated receptor 3 (family) [77-93]
    - IPR003912: Protease-activated receptor (family) [83-100]
    - IPR000276: G protein-coupled receptor, rhodopsin-like (family) [95-119]
    - IPR017452: GPCR, rhodopsin-like, 7TM (domain) [110-357]
    - IPR000276: G protein-coupled receptor, rhodopsin-like (family) [116-357]
    - IPR003943: Protease-activated receptor 3 (family) [118-132]
    - IPR003912: Protease-activated receptor (family) [150-164]
    - IPR000276: G protein-coupled receptor, rhodopsin-like (family) [172-194]
    - IPR003943: Protease-activated receptor 3 (family) [197-214]
    - IPR000276: G protein-coupled receptor, rhodopsin-like (family) [208-229]
    - IPR003943: Protease-activated receptor 3 (family) [232-243]
    - IPR003943: Protease-activated receptor 3 (family) [251-262]
    - IPR000276: G protein-coupled receptor, rhodopsin-like (family) [262-285]
    - IPR003912: Protease-activated receptor (family) [262-273]
    - IPR003943: Protease-activated receptor 3 (family) [292-304]
    - IPR000276: G protein-coupled receptor, rhodopsin-like (family) [298-322]
    - IPR003912: Protease-activated receptor (family) [300-313]
    - IPR003943: Protease-activated receptor 3 (family) [322-337]
    - IPR003912: Protease-activated receptor (family) [323-336]
    - IPR000276: G protein-coupled receptor, rhodopsin-like (family) [339-365]

    ## GO Term Predictions

    ### Molecular Function


    ### Biological Process


    ### Cellular Component

