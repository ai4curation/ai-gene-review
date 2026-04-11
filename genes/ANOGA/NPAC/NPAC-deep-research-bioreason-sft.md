    ---
    provider: bioreason-pro
    model: SFT
    source: huggingface.co/datasets/wanglab/protein_catalogue
    date: '2026-04-04'
    uniprot_id: Q7Q161
    gene: NPAC
    organism: Anopheles gambiae (African malaria mosquito)
    ---

    ## Thinking Trace

    The architecture begins with a compact N-terminal PWWP module: IPR000313 (PWWP domain, residues 7–68) is present alongside overlapping, family-specific refinements IPR035501 (Cytokine-like nuclear factor N-PAC, PWWP domain, residues 7–93), IPR000313 (PWWP domain, residues 9–70), and IPR000313 (PWWP domain, residues 10–92). This cluster defines a chromatin-reading module that recognizes nucleosomal features—classically DNA and methylated histone marks—thereby causing nucleosome binding and direct DNA engagement. Downstream, the polypeptide transitions into a large dehydrogenase-like core: IPR051265 (HIBADH-related NP60 subfamily, residues 167–562) encompasses a Rossmann-like redox fold, with IPR036291 (NAD(P)-binding domain superfamily, residues 281–443) and IPR006115 (6-phosphogluconate dehydrogenase, NADP-binding, residues 282–441) specifying a canonical dinucleotide-binding site. The C-terminal region is further defined by IPR008927 (6-phosphogluconate dehydrogenase-like, C-terminal domain superfamily, residues 442–561) and IPR013328 (6-phosphogluconate dehydrogenase, domain 2, residues 444–563), culminating in IPR029154 (3-hydroxyisobutyrate dehydrogenase-like, NAD-binding domain, residues 444–561). This ordered layout—reader domain followed by a redox fold with a Rossmann site—creates a bifunctional protein: a chromatin-tethered scaffold that can bind nucleosomes and DNA, and a metabolite-sensing redox module.

The PWWP cluster confers molecular functions of nucleosome binding (GO:0031491) and DNA binding (GO:0003677). These reader interactions position the protein on chromatin, where the dehydrogenase-like core can act as a regulatory sensor: binding of NAD(H)/NADP(H) within the Rossmann pocket alters the conformation and interaction surface of the C-terminal lobe, thereby modulating recruitment of chromatin-modifying enzymes. Such a mechanism naturally promotes positive regulation of histone acetylation (GO:0035066), because a chromatin-tethered, metabolite-responsive scaffold enhances acetyltransferase access to nucleosomes. The resulting increase in histone acetylation loosens chromatin and facilitates assembly of the transcriptional machinery, driving positive regulation of transcription by RNA polymerase II (GO:0045944).

The presence of a chromatin reader and the absence of transmembrane segments or secretion signals place the protein in the nuclear compartment, consistent with a chromatin-associated nuclear factor and aligning with the cellular component nucleus (GO:0005634). Within the nucleus, the PWWP domain anchors the protein to specific nucleosomal contexts, while the dehydrogenase-like lobe senses cellular redox or metabolite status via NAD(P) binding, translating metabolic cues into chromatin acetylation and transcriptional outputs.

This mechanistic model suggests interaction partners that either bridge to chromatin-modifying enzymes or reflect metabolic coupling. The chromatin-tethered scaffold is poised to engage acetyltransferase complexes and nucleosome components. The observed associations with enzymes of branched-chain and aldehyde metabolism—3-hydroxyisobutyrate dehydrogenase, 3-hydroxyisobutyryl-CoA hydrolase, probable methylmalonate-semialdehyde dehydrogenase (acylating), aldehyde dehydrogenases (NAD+-dependent), and 4-aminobutyrate aminotransferase—can arise from metabolite-channeling or redox-state signaling: the dehydrogenase-like domain may sense NAD(H) availability and transiently bind metabolic enzymes to coordinate acetylation with metabolic flux. Alanine–glyoxylate aminotransferase 2 and aldehyde dehydrogenase family 7 member A1 fit this theme, potentially linking amino acid and aldehyde metabolism to chromatin regulation. The V-type proton ATPase catalytic subunit A and AGAP009944-PA may represent regulatory or scaffolding contacts that couple cellular energy status to chromatin engagement, indirectly influencing nuclear metabolite pools. Overall, the protein likely functions as a nuclear chromatin reader fused to a redox-sensing dehydrogenase-like module that promotes histone acetylation and transcriptional activation in response to metabolic cues.

    ## Functional Summary

    A nuclear chromatin reader that anchors to nucleosomes and DNA through an N-terminal reader module and uses a C-terminal dehydrogenase-like Rossmann fold to sense cellular redox or metabolite levels. By coupling nucleosome binding with dinucleotide-dependent conformational control, it promotes histone acetylation and activates RNA polymerase II–driven transcription, thereby translating metabolic state into chromatin remodeling and gene expression changes within the nucleus.

    ## UniProt Summary

    Nuclear factor that binds DNA and nucleosomes.

    ## InterPro Domains

        - IPR000313: PWWP domain (domain) [7-68]
    - IPR035501: Cytokine-like nuclear factor N-PAC, PWWP domain (domain) [7-93]
    - IPR000313: PWWP domain (domain) [9-70]
    - IPR000313: PWWP domain (domain) [10-92]
    - IPR051265: HIBADH-related NP60 subfamily (family) [167-562]
    - IPR036291: NAD(P)-binding domain superfamily (homologous_superfamily) [281-443]
    - IPR006115: 6-phosphogluconate dehydrogenase, NADP-binding (domain) [282-441]
    - IPR008927: 6-phosphogluconate dehydrogenase-like, C-terminal domain superfamily (homologous_superfamily) [442-561]
    - IPR013328: 6-phosphogluconate dehydrogenase, domain 2 (homologous_superfamily) [444-563]
    - IPR029154: 3-hydroxyisobutyrate dehydrogenase-like, NAD-binding domain (domain) [444-561]

    ## GO Term Predictions

    ### Molecular Function


    ### Biological Process


    ### Cellular Component

