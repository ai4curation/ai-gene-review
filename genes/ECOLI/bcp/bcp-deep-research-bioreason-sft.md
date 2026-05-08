    ---
    provider: bioreason-pro
    model: SFT
    source: huggingface.co/datasets/wanglab/protein_catalogue
    date: '2026-04-04'
    uniprot_id: P0AE52
    gene: bcp
    organism: Escherichia coli (strain K12)
    ---

    ## Thinking Trace

    The architecture begins with a compact thioredoxin-like core: IPR036249 (Thioredoxin-like superfamily, residues 3–154) encompasses IPR013766 (Thioredoxin domain, residues 4–156), establishing the canonical β-sheet/α-helix fold that positions a nucleophilic cysteine for redox chemistry. Nested within this fold are peroxiredoxin-specific signatures: IPR024706 (Peroxiredoxin, AhpC-type family, residues 5–135) and IPR000866 (Alkyl hydroperoxide reductase subunit C / Thiol-specific antioxidant domain, residues 7–134) define the catalytic peroxidatic center and its resolving chemistry, while IPR050924 (Thiol-specific peroxidase BCP/PrxQ family, residues 3–155) specifies the BCP/PrxQ subclass that is optimized for hydrogen peroxide and organic hydroperoxide reduction. The ordered embedding of the AhpC-type core inside a thioredoxin-like scaffold causes a thiol-based peroxidase mechanism: the peroxidatic cysteine attacks H2O2 or ROOH to form a sulfenic intermediate that is then resolved via disulfide formation and reduction by thioredoxin.

This domain logic directly yields the molecular functions formalized as GO:0008379 thioredoxin peroxidase activity and GO:0032843 hydroperoxide reductase activity. The BCP/PrxQ family bias toward H2O2 and lipid/alkyl hydroperoxides explains the observed preference for H2O2 over organic hydroperoxides. The catalytic cycle requires electron input from thioredoxin, which is in turn reduced by thioredoxin reductase using NADPH, accounting for the observed NADPH dependence.

Detoxification of H2O2 and hydroperoxides is a primary defense against reactive oxygen species, placing the protein in GO:0006979 response to oxidative stress. By lowering peroxide levels, the enzyme preserves macromolecular integrity and supports redox homeostasis during aerobic metabolism and stress.

The absence of transmembrane segments and the soluble thioredoxin-like fold indicate a cytosolic enzyme. This aligns with a role in intercepting diffusible H2O2 and cytosolic lipid hydroperoxides, supporting localization to GO:0005829 cytosol.

Mechanistically, the peroxidatic cysteine cycles between reduced and sulfenylated states, forming an intramolecular or transient intermolecular disulfide that is resolved by thioredoxin. The enzyme likely operates within a broader redox network: it may receive electrons indirectly through the thioredoxin system that is also funneled to methionine sulfoxide reductase A and glutathione peroxidase, coordinating repair of oxidized proteins and membranes with peroxide removal. Functional coupling with alkyl hydroperoxide reductase complexes (AhpC/AhpF-type) would partition substrates, with this BCP/PrxQ enzyme specializing in H2O2 and certain organic hydroperoxides while Ahp systems handle lipid hydroperoxides more efficiently. Regulatory crosstalk with the accessory protein for GcvA suggests integration with acid-stress and redox-responsive transcriptional programs, ensuring peroxide detoxification is upregulated when oxidative load increases.

    ## Functional Summary

    A cytosolic thiol-dependent peroxidase that uses a thioredoxin-like catalytic center to reduce hydrogen peroxide and certain organic hydroperoxides to water and the corresponding alcohols, with a preference for hydrogen peroxide. It draws electrons from NADPH via the thioredoxin/thioredoxin reductase system, thereby protecting the cell from oxidative damage and integrating with broader redox-repair pathways.

    ## UniProt Summary

    Thiol-specific peroxidase that catalyzes the reduction of hydrogen peroxide and organic hydroperoxides to water and alcohols, respectively. Has a peroxidase activity towards H(2)O(2) and alkyl hydroperoxides, with a preference for H(2)O(2) over organic hydroperoxides. Acts as a hydrogen peroxide sensor. Required for protection against oxidative stress. Reduces H(2)O(2) in the presence of NADPH and thioredoxin reductase TrxB.

    ## InterPro Domains

        - IPR036249: Thioredoxin-like superfamily (homologous_superfamily) [3-154]
    - IPR050924: Thiol-specific peroxidase BCP/PrxQ (family) [3-155]
    - IPR013766: Thioredoxin domain (domain) [4-156]
    - IPR024706: Peroxiredoxin, AhpC-type (family) [5-135]
    - IPR000866: Alkyl hydroperoxide reductase subunit C/ Thiol specific antioxidant (domain) [7-134]

    ## GO Term Predictions

    ### Molecular Function


    ### Biological Process


    ### Cellular Component

