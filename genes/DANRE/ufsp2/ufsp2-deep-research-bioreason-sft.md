    ---
    provider: bioreason-pro
    model: SFT
    source: huggingface.co/datasets/wanglab/protein_catalogue
    date: '2026-04-04'
    uniprot_id: Q7T347
    gene: ufsp2
    organism: Danio rerio (Zebrafish)
    ---

    ## Thinking Trace

    I begin with the domain architecture. The N-terminus carries IPR049387 (UFSP2, second domain, residues 3–188), followed by a C-terminal catalytic module IPR012462 (UFSP1/2/DUB catalytic domain, residues 210–393). This arrangement places a UFSP-specific noncatalytic region upstream of a papain-like cysteine protease core. The UFSP1/2/DUB catalytic domain dictates a thiol protease chemistry tailored to ubiquitin-like modifiers, while the UFSP2-specific N-terminal domain provides substrate-recognition and positioning surfaces that guide the modifier’s C-terminal tail into the active site. The linear order—recognition domain leading into a cysteine protease core—causally enables selective hydrolysis of isopeptide bonds formed by a ubiquitin-like modifier rather than general proteolysis.

This architecture enforces a molecular function of ubiquitin-like protein peptidase activity (GO:0019783). The catalytic domain supplies the nucleophilic cysteine and general base histidine (with an acidic residue completing the triad), while the UFSP2-specific domain aligns the UFM1 C-terminus for precise scissile bond cleavage. The enzyme therefore processes UFM1 in two ways: it removes UFM1 from conjugated substrates (deconjugation) and trims the UFM1 precursor to its mature form (maturation). The same recognition logic explains specificity for UFM1 and the lack of activity toward SUMO1/2/3 or ISG15—surface features in the UFSP2-specific domain favor the hydrophobic patch and tail geometry unique to UFM1.

From this molecular activity, the biological process follows. By maturing UFM1 and editing UFM1 conjugations, the enzyme tunes the UFM1 conjugation cycle that supports ER-proximal protein quality control and proteostasis. In a developing vertebrate, such control impacts tissues with high secretory and proteostatic demand, notably the inner ear and visual system. Perturbations in UFM1 processing alter the function of UFM1-ubiquitin-like conjugation on ER-associated substrates, which in sensory neurons and hair cells influences protein folding, trafficking, and signaling pathways that underlie orientation in gravity fields and photoreceptor performance. This mechanistic link rationalizes involvement in gravitaxis (GO:0042332) and response to light stimulus (GO:0009416): precise UFM1 processing maintains cellular fitness in sensory circuits that execute these behaviors.

The cellular component is inferred from the soluble, two-domain protease lacking transmembrane segments, pointing to a cytosolic enzyme. Its role in UFM1 maturation and deconjugation requires access to UFM1 precursors and conjugates in the cytoplasm, consistent with cytoplasm (GO:0005737). The enzyme likely shuttles near the ER interface through transient recruitment by UFM1-pathway scaffolds, but its core residence and action remain cytoplasmic.

A coherent mechanistic model emerges: the UFSP2-specific N-terminal domain captures UFM1—either as a precursor or as the C-terminally attached modifier on target proteins—and funnels its tail into the C-terminal catalytic cleft for isopeptidase cleavage. This activity is coordinated with the UFM1 conjugation machinery. The enzyme likely associates with Ubiquitin-like modifier-activating enzyme 5 (UBA5), Ubiquitin-fold modifier-conjugating enzyme 1 (UBC13-like E2), and E3 UFM1-protein ligase 1 (UFL1) to balance conjugation with deconjugation. Scaffolds such as DDRGK domain-containing protein 1 and adaptors like CDK5 regulatory subunit-associated protein 3 and Thyroid hormone receptor interactor 4 can recruit the protease to ER-proximal sites or specific substrates. Direct binding to Ubiquitin-fold modifier 1 itself is expected during both maturation and de-UFMylase reactions. Through this cycle, the enzyme maintains UFM1 homeostasis that supports sensory physiology linked to gravitaxis and light responsiveness.

    ## Functional Summary

    A cytoplasmic cysteine protease that specializes in processing the ubiquitin-like modifier UFM1. It both matures UFM1 precursors to the mature form and removes UFM1 from conjugated substrates, thereby balancing the UFM1 conjugation cycle that supports ER-proximal protein quality control. By editing UFM1 attachments in sensory cells, it helps sustain proteostasis required for proper orientation in gravity fields and photoreceptor responsiveness. Mechanistically, an N-terminal recognition module positions the UFM1 tail for cleavage by a C-terminal papain-like catalytic core, and the enzyme likely operates in concert with the UFM1 E1, E2, and E3 enzymes and ER-associated scaffolds.

    ## UniProt Summary

    DUB-like protease which recognizes and hydrolyzes the peptide bond at the C-terminal Gly of UFM1, a ubiquitin-like modifier protein bound to a number of target proteins. Involved in the maturation of ufmylation by processing the precursor of UFM1 to mature UFM1. Does not cleave SUMO1, SUMO2, SUMO3 or ISG15 (By similarity).

    ## InterPro Domains

        - IPR049387: UFSP2, second domain (domain) [3-188]
    - IPR012462: UFSP1/2/DUB, catalytic domain (domain) [210-393]

    ## GO Term Predictions

    ### Molecular Function


    ### Biological Process


    ### Cellular Component

