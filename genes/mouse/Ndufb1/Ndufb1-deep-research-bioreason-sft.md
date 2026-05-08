    ---
    provider: bioreason-pro
    model: SFT
    source: huggingface.co/datasets/wanglab/protein_catalogue
    date: '2026-04-04'
    uniprot_id: P0DN34
    gene: Ndufb1
    organism: Mus musculus (Mouse)
    ---

    ## Thinking Trace

    I begin with the InterPro architecture: IPR012575 (NADH dehydrogenase [ubiquinone] 1 beta subcomplex subunit 1, NDUB1 family) spans residues 1–57, covering essentially the entire polypeptide. A single, compact family domain of this length indicates a small, non-catalytic accessory subunit tailored to the membrane arm of respiratory complex I. NDUB1-family proteins are typically single-pass inner-membrane proteins with a short matrix-exposed region that dock onto neighboring transmembrane subunits. This architecture causes the protein to function as a structural and organizational element rather than as an active redox catalyst.

From this domain assignment and topology, the molecular function is best understood as participation in the enzymatic activity of complex I. Although the polypeptide lacks catalytic motifs, its embedding within the membrane arm positions it to stabilize the quinone-reactive module and to maintain the geometry required for electron transfer from NADH to ubiquinone. In GO terms, this supports the complex-level function formalized as GO:0008137 NADH dehydrogenase (ubiquinone) activity, with the caveat that the subunit itself is non-enzymatic and contributes structurally to that activity.

The biological process follows from the assembly logic of the respiratory chain. Accessory membrane subunits of the beta subcomplex (including NDUB1) nucleate and stabilize late-stage intermediates of complex I, ensuring proper incorporation of acyl carrier protein and other small membrane components. This assembly role provides a mechanistic route to influence the maturation and stability of the entire oxidative phosphorylation machinery. Through these assembly-dependent effects and potential transient contacts at supercomplex interfaces, the protein can contribute to GO:0034551 mitochondrial respiratory chain complex III assembly, helping coordinate the integrity of the III–I neighborhood that supports efficient electron flow.

Cellular localization is dictated by the single-pass membrane architecture and the NDUB1 family signature. The protein integrates into the mitochondrial inner membrane as a matrix-side peripheral element, consistent with a single transmembrane helix anchoring a matrix-exposed domain that contacts neighboring subunits. This places it within the GO:0005739 mitochondrion and more specifically at the inner membrane, where complex I resides.

A mechanistic hypothesis emerges from the interaction landscape. Contacts with NDUFB11, NDUFB5, NDUFB10, and NDUFB4 indicate lateral packing within the beta subcomplex; associations with NDUFA1, NDUFA2, NDUFA6, NDUFA8, and C2 (a core membrane anchor) position the subunit at a junction between the peripheral and membrane arms, where it can brace the quinone-access channel. Binding to the mitochondrial acyl carrier protein suggests a role in stabilizing the ACP module that is essential for complex I maturation. By organizing these interfaces, the subunit preserves the conformational coupling that allows electron transfer from NADH to be transmitted into controlled conformational changes that drive proton translocation across the inner membrane, thereby sustaining oxidative phosphorylation.

    ## Functional Summary

    A small, single-pass inner-membrane accessory subunit of mitochondrial complex I that anchors on the matrix side to stabilize the membrane arm and organize neighboring subunits around the quinone-reactive region. By scaffolding assembly intermediates and maintaining the geometry of the electron-transfer module, it supports the transfer of electrons from NADH to ubiquinone and couples this chemistry to proton pumping, thereby sustaining oxidative phosphorylation. Its assembly-stabilizing role likely extends to the integrity of adjacent respiratory supercomplexes.

    ## UniProt Summary

    Accessory subunit of the mitochondrial membrane respiratory chain NADH dehydrogenase (Complex I), that is believed not to be involved in catalysis. Complex I functions in the transfer of electrons from NADH to the respiratory chain. The immediate electron acceptor for the enzyme is believed to be ubiquinone. Essential for the catalytic activity of complex I. Essential for oxidative phosphorylation.

    ## InterPro Domains

        - IPR012575: NADH dehydrogenase [ubiquinone] 1 beta subcomplex subunit 1, NDUB1 (family) [1-57]

    ## GO Term Predictions

    ### Molecular Function


    ### Biological Process


    ### Cellular Component

