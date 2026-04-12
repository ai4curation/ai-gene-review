    ---
    provider: bioreason-pro
    model: SFT
    source: huggingface.co/datasets/wanglab/protein_catalogue
    date: '2026-04-04'
    uniprot_id: B1X800
    gene: rlmC
    organism: Escherichia coli (strain K12 / DH10B)
    ---

    ## Thinking Trace

    I begin with the InterPro architecture. The sequence is saturated with signatures of the TrmA/RlmC clade of RNA C5-uracil methyltransferases. IPR011825 (23S rRNA (uracil(747)-C5)-methyltransferase RlmC family, residues 1–375) and its near-complete overlap with IPR010280 ((Uracil-5)-methyltransferase family, residues 2–373/12–375/208–374) define the enzyme class and substrate class: a uracil-directed C5-specific RNA methyltransferase. Two superfamily-level envelopes, IPR029063 (S-adenosyl-L-methionine-dependent methyltransferase superfamily, residues 3–374/14–368), indicate a Rossmann-like AdoMet-binding fold that donates a methyl group. The catalytic core is pinpointed by IPR030390 (RNA methyltransferase TrmA, active site, residues 307–338) and IPR030391 (RNA methyltransferase TrmA, conserved site, residues 357–367), which together mark the hallmark TrmA/RlmC catalytic constellation: a nucleophilic cysteine that forms a covalent adduct at the uracil C6 position, enabling electrophilic substitution at C5, and a basic residue that activates the target N1/C5 region. The ordered layout—AdoMet-binding superfamily spanning the full length, with embedded TrmA/RlmC active-site motifs in the C-terminal half—causes a methyl transfer reaction to the C5 position of a uracil base within structured rRNA.

This domain architecture dictates the molecular function as rRNA (uracil-C5)-specific methyltransferase activity (GO:0070043). The RlmC family assignment (IPR011825) narrows the substrate to 23S rRNA and the target nucleotide to U747, so the enzyme catalyzes formation of m5U747. The chemistry proceeds by AdoMet binding via the Rossmann-like fold (IPR029063), nucleophilic attack by the TrmA-like cysteine (IPR030390) to form a covalent Michael adduct at U747 C6, methyl transfer to C5, and beta-elimination to release m5U747, regenerating the active cysteine.

Installing m5U747 is a specific instance of rRNA base methylation (GO:0070475). This modification stabilizes local rRNA structure in the large subunit and tunes functional centers during ribosome assembly and translation, thereby contributing to robust ribosome biogenesis and performance. Because the enzyme acts on 23S rRNA within assembling 50S particles, its activity integrates into the maturation pathway rather than late-stage translation.

The absence of transmembrane segments and the soluble Rossmann-like fold, together with the need to access pre-50S assembly intermediates, place the enzyme in the cytosol (GO:0005829). In bacteria, 50S subunits assemble in the cytosol; thus the enzyme operates where pre-ribosomal particles are available.

Mechanistically, the enzyme likely recognizes a conserved structural context around U747 in 23S rRNA, using the TrmA-like active-site pocket to dock the helix bearing U747 and flip the base into the catalytic pocket. It should transiently associate with 50S assembly intermediates and accessory factors that present or stabilize the relevant helix. Plausible partners include 50S ribosomal proteins positioned near the 70S-binding region (e.g., L3 and L4) that help present the helix, and 23S rRNA chaperones or assembly factors (e.g., the ObgE GTPase and the RbgA GTPase) that coordinate maturation states. Because catalysis consumes S-adenosyl-L-methionine, coupling to local SAM supply is also likely, but the primary functional network centers on pre-50S particles and their maturation GTPases.

    ## Functional Summary

    A cytosolic RNA methyltransferase in E. coli that installs a 5-methyl group on uracil 747 within 23S rRNA during large-subunit assembly. It binds S-adenosyl-L-methionine, flips U747 into a TrmA-like active site, and uses a catalytic cysteine to form a transient covalent adduct that enables methyl transfer at C5, thereby stabilizing local rRNA structure and supporting efficient ribosome biogenesis.

    ## UniProt Summary

    Specifically methylates the uracil ring at position 747 of 23S rRNA.

    ## InterPro Domains

        - IPR011825: 23S rRNA (uracil(747)-C(5))-methyltransferase RlmC (family) [1-375]
    - IPR010280: (Uracil-5)-methyltransferase family (family) [2-373]
    - IPR011825: 23S rRNA (uracil(747)-C(5))-methyltransferase RlmC (family) [2-374]
    - IPR029063: S-adenosyl-L-methionine-dependent methyltransferase superfamily (homologous_superfamily) [3-374]
    - IPR010280: (Uracil-5)-methyltransferase family (family) [12-375]
    - IPR029063: S-adenosyl-L-methionine-dependent methyltransferase superfamily (homologous_superfamily) [14-368]
    - IPR010280: (Uracil-5)-methyltransferase family (family) [208-374]
    - IPR030390: RNA methyltransferase TrmA, active site (active_site) [307-338]
    - IPR030391: RNA methyltransferase TrmA, conserved site (conserved_site) [357-367]

    ## GO Term Predictions

    ### Molecular Function


    ### Biological Process


    ### Cellular Component

