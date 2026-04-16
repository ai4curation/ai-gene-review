    ---
    provider: bioreason-pro
    model: SFT
    source: huggingface.co/datasets/wanglab/protein_catalogue
    date: '2026-04-04'
    uniprot_id: P9WKX7
    gene: Rv3660c
    organism: Mycobacterium tuberculosis (strain ATCC 25618 / H37Rv)
    ---

    ## Thinking Trace

    I begin with the domain architecture. The N-terminus (residues 1–109) carries IPR059050, a CheY-like N-terminal domain. CheY-like modules are receiver-like folds that create a compact, β/α architecture optimized for protein–protein interaction and for coupling to partner surfaces rather than catalysis. From residue ~100 onward, the sequence is assigned to IPR050625 (ParA/MinD ATPase family, residues 100–334), which defines a deviant P-loop NTPase that uses ATP binding and hydrolysis to drive self-assembly and surface association. This is reinforced by two overlapping P-loop NTPase superfamily signatures, IPR027417 (P-loop containing nucleoside triphosphate hydrolase, residues 116–337 and 117–318), which specify the Walker A/B and switch elements that coordinate Mg2+-ATP and catalyze hydrolysis. The entire polypeptide is also encompassed by IPR022521 (Rv3660c family, residues 2–338), indicating a specialized lineage of ParA/MinD-like proteins. The ordered layout—an N-terminal CheY-like interaction module followed by a C-terminal ParA/MinD-type P-loop ATPase core—creates a two-part machine: the N-terminus provides a docking interface for regulatory partners, while the C-terminus supplies an ATP-dependent polymerization/oligomerization engine.

This architecture causes specific molecular functions. The P-loop core (IPR050625 with IPR027417) confers ATP binding and ATPase activity, enabling nucleotide-controlled assembly and disassembly cycles. The CheY-like N-terminus (IPR059050) contributes a broad protein-binding surface that recognizes transcriptional regulators. Together, these features support protein binding (GO:0005515) and ATP binding/ATPase activity as the operative molecular functions that modulate partner behavior.

The biological process follows from how these activities influence transcriptional control. ATP-driven polymerization of ParA/MinD-like ATPases often repositions or sequesters regulatory factors. Here, the N-terminal interaction module is poised to bind a transcriptional activator and the ATPase cycle is used to restrain its activity—either by direct occlusion, by trapping the activator in an inactive complex, or by spatially segregating it. This mechanism implements negative regulation of DNA-templated transcription (GO:0045892), consistent with inhibition of a transcriptional activator such as Rv3658c.

Cellular location is dictated by the absence of transmembrane segments and the soluble nature of CheY-like and ParA/MinD folds. These assemblies operate in the cytosol, where they can access transcription factors and nucleoid-proximal regions. Thus, the protein resides in the cytosol (GO:0005829), with likely enrichment near the inner membrane or nucleoid periphery when engaging partners, but without integral membrane features.

Mechanistically, I propose the following model. The N-terminal CheY-like domain binds the transcriptional activator Rv3658c and possibly other regulators encoded in the same operon. The C-terminal ParA/MinD-like ATPase binds ATP and cycles between monomeric and oligomeric states; ATP-bound oligomers could scaffold or cage the bound activator, reducing its ability to recruit RNA polymerase. Hydrolysis to ADP would trigger disassembly, potentially releasing the activator or resetting the complex. The operon partners—Rv3656c (a small conserved hypothetical protein), Rv3657c (a conserved membrane-like hypothetical protein), and Rv3658c (the transcriptional activator)—likely form a local regulatory module: the small cytosolic factor (Rv3656c) may chaperone or stabilize the ATPase–activator complex, the membrane-like protein (Rv3657c) could tether the complex to the inner membrane to spatially restrict activator function, and the transcriptional activator (Rv3658c) is the direct target of inhibition. Additional conserved hypothetical proteins may act as adaptors that tune oligomerization or localization. In sum, the domain architecture drives ATP-dependent assembly that binds and inhibits a transcriptional activator in the cytosol, thereby down-modulating transcriptional output.

    ## Functional Summary

    A cytosolic, ATP-dependent assembly factor that binds regulatory proteins and inhibits a nearby transcriptional activator. Its N-terminal interaction module engages the activator, while a C-terminal P-loop ATPase core drives nucleotide-controlled oligomerization that cages or sequesters the activator, reducing its ability to stimulate transcription. Within an operon of conserved hypothetical proteins, it likely collaborates with small cytosolic and membrane-associated partners to position and stabilize the inhibitory complex at the cytosolic face of the cell, thereby tuning transcriptional output.

    ## UniProt Summary

    Inhibits the transcriptional activator Rv3658c.

    ## InterPro Domains

        - IPR059050: Rv3660c-like, CheY-like N-terminal domain (domain) [1-109]
    - IPR022521: Rv3660c (family) [2-338]
    - IPR050625: ParA/MinD ATPase (family) [100-334]
    - IPR027417: P-loop containing nucleoside triphosphate hydrolase (homologous_superfamily) [116-337]
    - IPR027417: P-loop containing nucleoside triphosphate hydrolase (homologous_superfamily) [117-318]

    ## GO Term Predictions

    ### Molecular Function


    ### Biological Process


    ### Cellular Component

