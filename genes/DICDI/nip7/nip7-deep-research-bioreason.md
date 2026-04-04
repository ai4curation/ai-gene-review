    ---
    provider: bioreason-pro
    model: SFT
    source: huggingface.co/datasets/wanglab/protein_catalogue
    date: '2026-04-04'
    uniprot_id: B0G104
    gene: nip7
    organism: Dictyostelium discoideum (Social amoeba)
    ---

    ## Thinking Trace

    I begin with the InterPro architecture. The entire polypeptide (residues 1–177) is classified as IPR016686 (Ribosome biogenesis factor, NIP7 family), establishing a dedicated role in large subunit assembly. The N-terminus carries IPR040598 (60S ribosome subunit biogenesis protein NIP7, pre-PUA domain, residues 1–83) and its eukaryote-specific refinement IPR055359 (pre-PUA domain, eukaryotes, residues 2–88). This pre-PUA segment typically forms an extended, basic, protein-interaction arm that positions the core RNA-binding module and mediates contacts with assembly factors. The C-terminal half is dominated by a PUA fold: IPR002478 (PUA domain, residues 95–171) is corroborated by IPR005155 (UPF0113, PUA domain, residues 95–172) and encompassed by PUA-related superfamily signatures IPR036974 (PUA domain superfamily, residues 94–179) and IPR015947 (PUA-like superfamily, residues 95–170). PUA domains are specialized RNA-recognition modules that bind structured RNAs and tRNA-like elements; in nucleolar biogenesis factors, this fold anchors the protein to pre-rRNA segments within pre-60S particles. The ordered layout—pre-PUA for factor docking followed by a PUA core for RNA engagement—creates a bipartite clamp that couples protein and RNA binding during 60S maturation.

This architecture causes two primary molecular activities. First, the pre-PUA and surrounding family-specific surfaces provide multivalent protein interfaces, supporting GO:0005515 protein binding. Second, the PUA fold confers high-affinity binding to structured RNA, most plausibly pre-rRNA or tRNA-like moieties present in pre-60S particles; thus RNA binding (GO:0003723) is expected. Together, these activities enable the factor to stabilize specific rRNA helices, recruit partner assembly factors, and choreograph remodeling steps on nascent 60S subunits.

From these molecular functions, the biological process follows. By binding pre-rRNA and engaging assembly proteins, the factor drives maturation of the large ribosomal subunit, a core component of ribosome biogenesis (GO:0042254) and specifically ribosomal large subunit biogenesis (GO:0042273). Ribosome production is tightly integrated with cellular stress programs. Perturbations such as UV exposure or DNA damage rapidly reprogram nucleolar activity; a nucleolar assembly factor that senses or enforces pre-rRNA checkpoints can modulate growth and ribosome output during stress. This provides a mechanistic route to participation in cellular response to DNA damage stimulus (GO:0006974) and response to UV (GO:0009411): modulation of pre-60S assembly couples ribosome biogenesis capacity to genome integrity signals, throttling output and facilitating recovery.

The cellular component is dictated by the substrate and partners. Pre-rRNA transcription and early 60S assembly occur in the nucleolus, aligning with GO:0005730 nucleolus. The absence of transmembrane features and the presence of nucleolar specialization further support a soluble nucleolar residency.

This mechanistic model predicts specific interaction partners. The pre-PUA arm can dock assembly factors such as BRX1 and WDR12 (components of the PeBoW complex), NSA2, RPF2, and RLP24, while the PUA domain anchors to pre-rRNA near sites where MRT4 (a pre-60S P-stalk placeholder) is handled during maturation. Additional contacts with an RRM domain-containing protein and coiled-coil scaffolds would stabilize transient pre-60S intermediates. In sum, the protein likely bridges pre-rRNA elements to a cohort of 60S biogenesis factors, enforcing quality control and coordinating progression through nucleolar assembly checkpoints, with stress-responsive modulation during UV or DNA-damage conditions.

    ## Functional Summary

    A nucleolar assembly factor that promotes maturation of the large ribosomal subunit by combining an N-terminal docking module with a C-terminal RNA-recognition fold to bind pre-rRNA and recruit biogenesis factors. Through these multivalent contacts it stabilizes and remodels pre-60S particles, coordinating their progression and enforcing quality control. Its activity is expected to be tuned during UV and DNA-damage responses, coupling ribosome output to stress conditions to maintain cellular homeostasis.

    ## UniProt Summary

    Involved in the biogenesis of the 60S ribosomal subunit.

    ## InterPro Domains

        - IPR016686: Ribosome biogenesis factor, NIP7 (family) [1-177]
    - IPR040598: 60S ribosome subunit biogenesis protein NIP7, pre-PUA domain (domain) [1-83]
    - IPR055359: 60S ribosome subunit biogenesis protein Nip7, pre-PUA domain, eukaryotes (domain) [2-88]
    - IPR036974: PUA domain superfamily (homologous_superfamily) [94-179]
    - IPR002478: PUA domain (domain) [95-171]
    - IPR005155: UPF0113, PUA domain (domain) [95-172]
    - IPR015947: PUA-like superfamily (homologous_superfamily) [95-170]
    - IPR005155: UPF0113, PUA domain (domain) [96-175]

    ## GO Term Predictions

    ### Molecular Function


    ### Biological Process


    ### Cellular Component

