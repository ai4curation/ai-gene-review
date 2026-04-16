    ---
    provider: bioreason-pro
    model: SFT
    source: huggingface.co/datasets/wanglab/protein_catalogue
    date: '2026-04-04'
    uniprot_id: G5EGH7
    gene: lon-8
    organism: Caenorhabditis elegans
    ---

    ## Thinking Trace

    I begin with the domain architecture. The sequence contains IPR057449 (BPTI-like, C-terminal domain, residues 77–151). The BPTI/Kunitz fold is a compact, disulfide-rich inhibitory module classically used to block serine protease active sites. Its C-terminal placement implies an N-terminal signal peptide and pro-region preceding the Kunitz core, a layout that typically routes the protein into the secretory pathway and positions the inhibitory domain in the extracellular milieu. The disulfide-stabilized Kunitz scaffold is optimized for high-affinity, reversible protein–protein interactions rather than catalysis, and in extracellular matrices it often tunes proteolysis by restraining endopeptidases that would otherwise remodel matrix components.

This architecture causally supports a molecular function as an extracellular matrix structural constituent (GO:0005201). A secreted, disulfide-rich module can intercalate into matrix assemblies and provide mechanical stability and controlled viscoelasticity by modulating both direct binding to matrix proteins and the proteolytic turnover of those proteins. The Kunitz fold’s inhibitory geometry explains how the protein could regulate matrix remodeling enzymes, thereby preserving specific collagenous and glycoprotein architectures.

From this molecular role, the biological processes follow. By stabilizing and patterning the extracellular scaffold, the protein contributes to shaping specialized structures in the male tail, consistent with nematode male tail tip morphogenesis (GO:0045138). The same structural tuning can limit excessive body elongation by constraining extracellular matrix expansion and by signaling through a cell-surface receptor to temper cell proliferation, aligning with negative regulation of multicellular organism growth (GO:0040015). Mechanistically, a Kunitz-domain protein tethered to the matrix can both physically reinforce the cuticle and dampen protease-driven loosening, while its receptor engagement on hypodermal cells feeds back to restrain growth programs.

The cellular context is dictated by secretion and matrix integration. The Kunitz domain’s extracellular design, together with the protein’s role in morphogenesis and growth restraint, places it in the basement membrane (GO:0005604). Localization to the hypodermal basement membrane allows it to contact both apical extracellular matrix components and cell-surface receptors, enabling it to influence both matrix assembly and cell proliferation.

A coherent mechanistic model emerges: the protein is secreted by hypodermal cells into the basement membrane, where its BPTI-like domain binds and inhibits matrix-remodeling proteases, thereby stabilizing collagens and glycoproteins. In parallel, it engages a cell-surface receptor to trigger signaling that restrains body size and modulates proliferation. The observed partners—Col_cuticle_N domain-containing protein, ZP domain-containing protein, and cuticle collagen lon-3—fit this model as direct matrix ligands or co-scaffolds. The Kunitz module likely binds these extracellular components to form a protective network, while receptor engagement on adjacent cells transduces a growth-limiting signal. This dual action explains how the protein shapes the male tail tip and prevents overgrowth while remaining dispensable for the general integrity of the cuticle.

    ## Functional Summary

    A secreted, basement-membrane-associated extracellular matrix protein in C. elegans that uses a disulfide-rich inhibitory module to stabilize and pattern the matrix while tempering proteolytic remodeling. By binding cuticle and glycoprotein components and engaging a cell-surface receptor, it shapes the male tail tip and limits body elongation by dampening proliferation. Despite reinforcing local extracellular architecture, it is not essential for overall cuticle integrity.

    ## UniProt Summary

    Involved in male tail morphogenesis. Negatively regulates body size, probably by modulating cell proliferation through interaction with one or more cell surface receptors. Not required for the structural integrity of the cuticle.

    ## InterPro Domains

        - IPR057449: BPTI-like, C-terminal domain (domain) [77-151]

    ## GO Term Predictions

    ### Molecular Function


    ### Biological Process


    ### Cellular Component

