    ---
    provider: bioreason-pro
    model: SFT
    source: huggingface.co/datasets/wanglab/protein_catalogue
    date: '2026-04-04'
    uniprot_id: O94267
    gene: spt16
    organism: Schizosaccharomyces pombe (strain 972 / ATCC 24843) (Fission yeast)
    ---

    ## Thinking Trace

    I begin by dissecting the InterPro architecture and its order along the polypeptide. The N-terminus (residues 1–173) is defined by IPR029149 (Creatinase/Aminopeptidase P/Spt16, N-terminal homologous superfamily) and, within it, a more specific N-terminal lobe module IPR029148 (FACT complex subunit SPT16, N-terminal lobe domain, residues 6–167/169). Immediately downstream, the core of the protein transitions into an M24-like metallopeptidase fold: IPR036005 (Creatinase/aminopeptidase-like homologous superfamily, residues 174–442) and its embedded IPR033825 (Spt16, peptidase M24-like domain, residues 181–427) together with IPR000994 (Peptidase M24 domain, residues 183–392). In Spt16, this M24-like scaffold is repurposed for histone handling rather than catalysis, creating a rigid cradle that binds histone surfaces. The mid-region is marked by IPR013953 (Spt16 middle domain, residues 540–652/690), a flexible but structured module that couples the N-terminal histone-binding lobes to distal interaction surfaces. The C-terminal half contains a PH-like fold: IPR056595 (Spt16 PH-like domain, residues 663–794) followed by a broader PH-like superfamily signature IPR011993 (residues 806–937) and a histone-chaperone-tuned variant IPR013719 (RTT106/FACT Spt16-like middle domain, residues 813–903/901). This PH-like platform is specialized to engage histone dimers and nucleosomal DNA, positioning them for transfer. The architecture culminates in IPR048969 (Spt16 C-terminal domain, residues 941–1018), a module that stabilizes histone contacts and completes the chaperone cradle. The entire sequence is encompassed by IPR040258 (FACT complex subunit Spt16 family, residues 1–1017), confirming a conserved, multi-lobed histone chaperone design.

This ordered arrangement causes a specific molecular function: the N-terminal lobe and M24-like core form a composite surface that grips H2A–H2B and H3–H3’ dimers, while the PH-like and C-terminal domains position and hand off histones to and from DNA. Such a multi-surface chaperone architecture directly encodes histone chaperone activity (GO:0140713). The extensive interaction surfaces across the middle and C-terminal regions also enable multivalent protein binding (GO:0005515), including contacts with partner proteins and the transcription machinery.

From this molecular activity, the biological processes follow. By binding and transferring H2A–H2B and mediating partial nucleosome disassembly and reassembly, the protein drives nucleosome organization (GO:0034728). During DNA synthesis, the same chaperoning of histones onto nascent DNA supports DNA replication-dependent chromatin assembly (GO:0006335). In addition, by stabilizing and reconfiguring nucleosomes across repetitive and silenced regions, the chaperone contributes to maintaining compacted chromatin states, consistent with constitutive heterochromatin formation (GO:0140719). The ability to transiently destabilize and reassemble nucleosomes also facilitates repair factor access and restoration of chromatin integrity after damage.

The cellular context is dictated by where nucleosomes and transcriptional elongation occur. The chaperone’s reliance on nucleosomal substrates places it in euchromatin (GO:0000791), where dynamic remodeling is required, and as a core constituent of the FACT complex (GO:0035101). Its operational niche during transcription and replication situates it in the nucleus, and its association with actively transcribed loci explains enrichment on chromosomes. Thus, the most plausible localization is the nucleus (GO:0005634) and chromosome (GO:0005694), with concentration in euchromatic regions and at transcribed genes.

Mechanistically, the protein likely functions as one half of a histone-handling clamp, cooperating with its partner subunit to transiently remove an H2A–H2B dimer during elongation or replication, escort histones via the PH-like and C-terminal domains, and reseat them to maintain chromatin integrity. This mechanism predicts interactions with the cognate FACT partner (pob3) to form the functional heteromer; with the RNA polymerase II machinery (Rpb1 and Rpb3) and elongation factors (Spt4, Spt5, Spt6) to couple histone transfer to polymerase passage; with transcription-coupled chromatin factors such as the Paf1-associated component Cdc73 to coordinate elongation and chromatin maturation; and with scaffold-like adaptors such as TPR-containing proteins and RNA polymerase-associated proteins that stabilize the complex on moving polymerase. Uncharacterized proteins (e.g., C13E7.08c and C651.09c) may act as adaptors or regulators that tune FACT engagement with specific genomic loci, including stress-responsive and telomeric chromatin, thereby linking chaperone activity to gene expression programs and genome maintenance.

    ## Functional Summary

    A nuclear chromatin chaperone that operates within the FACT complex to reorganize nucleosomes during DNA-templated processes. It transiently destabilizes a nucleosome by removing an H2A–H2B dimer to allow RNA polymerase II to pass, then restores the nucleosome to preserve chromatin integrity. The same histone-handling mechanism supports replication-coupled chromatin assembly and contributes to the stability of compacted chromatin domains, thereby influencing transcriptional output, DNA repair, and chromosome stability. It concentrates on actively transcribed chromosomal regions and likely coordinates with elongation factors and the polymerase to couple histone transfer to transcriptional progression.

    ## UniProt Summary

    Component of the FACT complex, a general chromatin factor that acts to reorganize nucleosomes. The FACT complex is involved in multiple processes that require DNA as a template such as mRNA elongation, DNA replication and DNA repair. During transcription elongation the FACT complex acts as a histone chaperone that both destabilizes and restores nucleosomal structure. It facilitates the passage of RNA polymerase II and transcription by promoting the dissociation of one histone H2A-H2B dimer from the nucleosome, then subsequently promotes the reestablishment of the nucleosome following the passage of RNA polymerase II. The FACT complex is also required for replication and repair of damaged DNA. The FACT complex activity is required in transcriptional regulation of a subset of genes involved in critical cellular functions such as DNA replication, DNA repair, and cellular stress responses. The FACT complex changes in response to environmental stress, and contributes to the adaptive transcriptional reprogramming of the cell. May also play a role in maintaining the stability of telomeres.

    ## InterPro Domains

        - IPR029149: Creatinase/Aminopeptidase P/Spt16, N-terminal (homologous_superfamily) [1-173]
    - IPR040258: FACT complex subunit Spt16 (family) [1-1017]
    - IPR029148: FACT complex subunit SPT16, N-terminal lobe domain (domain) [6-167]
    - IPR029148: FACT complex subunit SPT16, N-terminal lobe domain (domain) [6-169]
    - IPR036005: Creatinase/aminopeptidase-like (homologous_superfamily) [174-442]
    - IPR036005: Creatinase/aminopeptidase-like (homologous_superfamily) [176-429]
    - IPR033825: FACT complex subunit Spt16, peptidase M24-like domain (domain) [181-427]
    - IPR000994: Peptidase M24 (domain) [183-392]
    - IPR013953: FACT complex subunit SPT16, middle domain (domain) [540-652]
    - IPR013953: FACT complex subunit SPT16, middle domain (domain) [540-690]
    - IPR056595: FACT complex subunit SPT16, PH-like domain (domain) [663-794]
    - IPR011993: PH-like domain superfamily (homologous_superfamily) [806-937]
    - IPR013719: Histone chaperone RTT106/FACT complex subunit SPT16-like, middle domain (domain) [813-903]
    - IPR013719: Histone chaperone RTT106/FACT complex subunit SPT16-like, middle domain (domain) [815-901]
    - IPR048969: FACT complex subunit SPT16, C-terminal domain (domain) [941-1018]

    ## GO Term Predictions

    ### Molecular Function


    ### Biological Process


    ### Cellular Component

