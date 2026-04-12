    ---
    provider: bioreason-pro
    model: SFT
    source: huggingface.co/datasets/wanglab/protein_catalogue
    date: '2026-04-04'
    uniprot_id: Q9LUJ8
    gene: CHL1
    organism: Arabidopsis thaliana (Mouse-ear cress)
    ---

    ## Thinking Trace

    I begin with the domain architecture. The N-terminus carries a Toll/interleukin-1 receptor homology module captured by IPR035897 (TIR domain superfamily, residues 12–140 and 15–171) and specifically by IPR000157 (TIR domain, residues 16–170 and 20–175). This tandem superfamily/domain coverage indicates a canonical plant TIR module positioned at the extreme N-terminus. Immediately downstream, the sequence transitions into a P-loop NTPase core defined by IPR027417 (P-loop containing nucleoside triphosphate hydrolase superfamily, residues 172–324 and 178–409), with a well-delimited IPR002182 NB-ARC domain (residues 199–348) and an IPR003593 AAA+ ATPase domain (residues 202–332). The C-terminal region includes IPR042197 (Apoptotic protease-activating factors, helical domain superfamily, residues 331–412), the helical scaffold that stabilizes the nucleotide-bound switch and oligomerization interfaces in NB-ARC/Apaf-like assemblies. The entire polypeptide is classified by IPR044974 (Disease resistance protein, plants family, residues 18–402), which unifies these modules into a plant immune receptor of the TIR–NB-ARC class. The ordered layout—TIR at the N-terminus followed by an NB-ARC/AAA+ P-loop engine and a C-terminal helical scaffold—creates a receptor that remains autoinhibited in the absence of stimulus and, upon activation, oligomerizes and exposes N-terminal effector surfaces.

This architecture causes a molecular function centered on regulated protein binding (GO:0005515). The TIR domain provides a docking surface for downstream immune adaptors, while the NB-ARC/AAA+ core drives conformational switching and multimerization, thereby increasing avidity for partner proteins. The P-loop NTPase cycle gates assembly: ATP-bound states favor the active oligomer, and ADP-bound states favor the inactive monomer, ensuring stimulus-coupled protein–protein interactions.

At the process level, such a TIR–NB-ARC receptor is a trigger for immune signaling. Oligomerization of the NB-ARC core exposes the TIR domain, which then recruits signaling partners to initiate defense pathways. This mechanism directly supports roles in defense response to fungus (GO:0050832) and defense response to bacterium (GO:0042742). The same signaling cascade is known to culminate in localized programmed cell death to contain infection, aligning with positive regulation of cell death (GO:0010942). The presence of a TIR domain suggests engagement of TIR-dependent pathways that can activate transcriptional defenses and cell death programs; the NB-ARC switch ensures that these outputs are tightly coupled to pathogen perception.

Cellular localization follows from the signaling logic and the provided compartment label. The GO:0005739 mitochondrion placement is consistent with immune receptor activation at or near mitochondria, where signaling nodes for reactive oxygen species production and death control assemble. The NB-ARC helical domain (Apaf-like) further supports mitochondrial proximity, as Apaf-like assemblies often interface with mitochondrial signaling hubs. Thus, a mitochondrial locale provides the platform for rapid conversion of receptor activation into oxidative and transcriptional outputs that drive defense and cell death.

From this, a mechanistic hypothesis emerges. In the resting state, the NB-ARC holds the TIR domain in a closed conformation. Pathogen-derived effectors or host guardees perturb this equilibrium, allowing the NB-ARC/AAA+ module to bind and hydrolyze NTPs, driving oligomerization. The exposed TIR domain then nucleates a signaling complex at mitochondria, recruiting immune adaptors and helper NLRs to propagate defense and execute cell death. Post-translational control likely tunes this switch: ERAD-associated E3 ubiquitin-protein ligase HRD1A could ubiquitinate the receptor to restrain signaling, while Ubiquitin C-terminal hydrolase 22 could remove ubiquitin to stabilize or reactivate the receptor. Additional partners are expected among TIR-NBS-LRR immune components that assemble higher-order complexes to amplify the defense response.

    ## Functional Summary

    A plant intracellular immune receptor that uses an N-terminal signaling module coupled to a nucleotide-gated switch to detect pathogen challenge and initiate defense. Upon activation, it oligomerizes and exposes effector surfaces that assemble signaling complexes at mitochondria, driving antimicrobial responses and promoting programmed cell death to contain infection. Its activity is likely tuned by ubiquitination and deubiquitination, with an E3 ligase dampening signaling and a deubiquitinase restoring competence.

    ## UniProt Summary

    Probable disease resistance protein.

    ## InterPro Domains

        - IPR035897: Toll/interleukin-1 receptor homology (TIR) domain superfamily (homologous_superfamily) [12-140]
    - IPR035897: Toll/interleukin-1 receptor homology (TIR) domain superfamily (homologous_superfamily) [15-171]
    - IPR000157: Toll/interleukin-1 receptor homology (TIR) domain (domain) [16-170]
    - IPR044974: Disease resistance protein, plants (family) [18-402]
    - IPR000157: Toll/interleukin-1 receptor homology (TIR) domain (domain) [20-175]
    - IPR027417: P-loop containing nucleoside triphosphate hydrolase (homologous_superfamily) [172-324]
    - IPR027417: P-loop containing nucleoside triphosphate hydrolase (homologous_superfamily) [178-409]
    - IPR002182: NB-ARC (domain) [199-348]
    - IPR003593: AAA+ ATPase domain (domain) [202-332]
    - IPR042197: Apoptotic protease-activating factors, helical domain (homologous_superfamily) [331-412]

    ## GO Term Predictions

    ### Molecular Function


    ### Biological Process


    ### Cellular Component

