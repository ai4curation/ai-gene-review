    ---
    provider: bioreason-pro
    model: SFT
    source: huggingface.co/datasets/wanglab/protein_catalogue
    date: '2026-04-04'
    uniprot_id: P0DOV2
    gene: Ifi204
    organism: Mus musculus (Mouse)
    ---

    ## Thinking Trace

    The architecture begins with an N-terminal DAPIN/PYRIN module: IPR004020 (DAPIN domain, residues 1–88) is detected in three shifted spans (1–88, 6–84, 10–80) and is encompassed by IPR011029 (Death-like domain superfamily, residues 2–93). This death-fold scaffold is specialized for homotypic protein–protein interactions, particularly CARD-mediated assemblies, which equips the protein to nucleate signaling complexes. The central and C‑terminal two-thirds are dominated by a tripartite HIN-200/IF120x nucleic-acid-binding region: IPR004021 (HIN-200/IF120x domain, residues 213–413) is reinforced by two overlapping domain calls (225–393) and is followed by a second HIN-200/IF120x segment (417–615). This region is built from OB-fold modules, as indicated by IPR012340 (Nucleic acid-binding, OB-fold homologous superfamily, residues 212–324 and 325–417 for the first OB unit, and 418–526 and 527–619 for the second), which together create a tandem OB arrangement that grips double-stranded DNA in a sequence-independent manner. The entire polypeptide is classified within IPR040205 (HIN-200 family, residues 1–417), anchoring the identity as a PYHIN-family DNA-binding scaffold.

This domain layout causally specifies molecular functions. The DAPIN/PYRIN death-fold confers GO:0005515 protein binding through homotypic contacts with other death-domain proteins, enabling assembly of signaling platforms. The tandem OB-fold HIN region binds duplex DNA directly, supporting GO:0003690 double-stranded DNA binding, which allows the protein to sense aberrant or regulatory DNA structures. The combination of a DNA-binding HIN core with a signaling-competent PYRIN module enables transcriptional modulation: by docking onto chromatin and recruiting or stabilizing transcriptional regulators, the protein exerts GO:0003712 transcription coregulator activity, rather than acting as a sequence-specific transcription factor.

From these molecular activities, the biological processes follow. DNA binding coupled to transcriptional coregulation positions the protein to influence GO:0006357 regulation of transcription by RNA polymerase II, for example by modulating the activity of tumor suppressors and interferon-stimulated genes. The PYRIN/CARD-competent N-terminus drives assembly of inflammasome-like complexes with caspase adaptors, which activates caspase-1 and promotes IL-1β maturation; this innate immune signaling explains participation in GO:0009617 response to bacterium. The same scaffold integrates cytokine cues; interferon-inducible expression and promoter-proximal binding rationalize GO:0035457 cellular response to interferon-alpha and GO:0035458 cellular response to interferon-beta. Beyond immunity, PYHIN-mediated transcriptional control in lineage cells can tune differentiation programs, accounting for GO:0045669 positive regulation of osteoblast differentiation and developmental roles such as GO:0048839 inner ear development, where chromatin-bound regulation and nuclear substructures shape gene expression trajectories.

The cellular context is dictated by the domains and their binding partners. The absence of transmembrane segments and the presence of chromatin-binding HIN OB-folds point to a nuclear residency, consistent with localization to the nucleus. Within the nucleus, PYHIN proteins often concentrate in subnuclear bodies; the propensity to form higher-order assemblies on DNA explains accumulation in GO:0005730 nucleolus and in GO:0042405 nuclear inclusion body structures, which can serve as hubs for transcriptional control and stress-responsive sequestration.

Mechanistically, the N-terminal DAPIN/PYRIN domain recruits CARD-bearing adaptors to form signaling nodes, while the HIN tandem OB-folds anchor the complex to DNA. This architecture enables two coupled modes: (1) transcriptional coregulation at chromatin, where DNA-bound complexes modulate tumor suppressor and interferon-responsive genes; and (2) innate immune sensing, where DNA engagement and adaptor recruitment trigger inflammasome assembly and caspase-1 activation. In this framework, likely interaction partners include Apoptosis-associated speck-like protein containing a CARD (ASC/PYCARD) and Caspase-1 subunit p10 for inflammasome execution; Interferon-inducible proteins AIM2 and IFI16 (Interferon-activated gene 206 and 207) for cooperative DNA sensing; Stimulator of interferon genes protein (STING) for cGAS–STING axis crosstalk; Cyclic GMP-AMP synthase (cGAS) as the DNA sensor that feeds into STING; Pyrin and NLR family CARD domain-containing protein 4 (NLRC4) as additional CARD-bearing partners in inflammasome networks; and Cellular tumor antigen p53 as a transcriptional effector modulated by nuclear DNA-bound complexes. Together, these interactions implement a switchable system that couples nuclear DNA surveillance and transcriptional control with inflammasome activation and interferon-responsive programs.

    ## Functional Summary

    A nuclear PYHIN-family scaffold that binds double-stranded DNA via tandem OB-fold modules and uses an N-terminal death-fold to assemble signaling complexes. By anchoring to chromatin, it modulates transcriptional programs, including those governed by tumor suppressors and interferon-stimulated genes, thereby influencing differentiation and development. In parallel, its adaptor-binding module nucleates inflammasome assemblies with caspase adaptors to drive IL-1β maturation and antibacterial responses. The protein concentrates in subnuclear bodies, including nucleolar and inclusion-like structures, which organize its transcriptional and innate immune functions.

    ## UniProt Summary

    DNA-binding protein which may be involved in transcription regulation. May modulate the activity of some tumor suppressor genes, such as p53/TP53 and maspin/MSPN. Plays a role in IL-1 beta/IL-1B production and inflammation.

    ## InterPro Domains

        - IPR004020: DAPIN domain (domain) [1-88]
    - IPR040205: HIN-200 family (family) [1-417]
    - IPR011029: Death-like domain superfamily (homologous_superfamily) [2-93]
    - IPR004020: DAPIN domain (domain) [6-84]
    - IPR004020: DAPIN domain (domain) [10-80]
    - IPR012340: Nucleic acid-binding, OB-fold (homologous_superfamily) [212-324]
    - IPR004021: HIN-200/IF120x (domain) [213-413]
    - IPR004021: HIN-200/IF120x (domain) [225-393]
    - IPR012340: Nucleic acid-binding, OB-fold (homologous_superfamily) [325-417]
    - IPR004021: HIN-200/IF120x (domain) [417-615]
    - IPR012340: Nucleic acid-binding, OB-fold (homologous_superfamily) [418-526]
    - IPR004021: HIN-200/IF120x (domain) [429-595]
    - IPR012340: Nucleic acid-binding, OB-fold (homologous_superfamily) [527-619]

    ## GO Term Predictions

    ### Molecular Function


    ### Biological Process


    ### Cellular Component

