    ---
    provider: bioreason-pro
    model: SFT
    source: huggingface.co/datasets/wanglab/protein_catalogue
    date: '2026-04-04'
    uniprot_id: O77457
    gene: TDO
    organism: Anopheles gambiae (African malaria mosquito)
    ---

    ## Thinking Trace

    I begin with the InterPro architecture. Three overlapping family signatures—IPR004981 (Tryptophan 2,3-dioxygenase family) spanning residues 8–378, 11–358, and 20–358—enclose a core catalytic region that is further encompassed by IPR037217 (Tryptophan/Indoleamine 2,3-dioxygenase-like homologous superfamily) from residues 27–359. This layered arrangement is characteristic of heme-dependent tryptophan/indoleamine 2,3-dioxygenases: a conserved catalytic fold that binds a b-type heme via a proximal histidine and positions molecular oxygen for insertion into the indole ring of L-tryptophan. The breadth of the family signatures across the central polypeptide indicates a single-domain enzyme whose N- and C-termini contribute to oligomerization interfaces rather than distinct modules. Such enzymes typically assemble into higher-order complexes (often tetramers), and the conserved fold stabilizes the heme pocket and the dioxygen activation chemistry.

This architecture causes two molecular functions. First, the heme pocket formed by the conserved fold enforces GO:0020037 heme binding. Second, the active-site geometry and redox environment enable GO:0004833 tryptophan 2,3-dioxygenase activity, in which O2 is inserted across the C2–C3 bond of the indole ring to generate N-formylkynurenine. The catalytic outcome is mechanistically inseparable from a heme–O2 adduct that is subsequently resolved by electron input from a reductant, consistent with the requirement for a physiological reductant such as NADPH via an associated reductase.

The immediate biochemical consequence of this activity is the first committed step of the kynurenine pathway, producing N-formylkynurenine that is then hydrolyzed to kynurenine. This places the enzyme squarely in GO:0019441 tryptophan catabolic process to kynurenine. Because the reaction irreversibly diverts L-tryptophan from biosynthesis and signaling roles into catabolism, the enzyme functions as a metabolic gatekeeper controlling flux into downstream kynurenine- and NAD+–related branches.

The oligomeric nature implied by the family architecture supports assembly into a GO:1902494 catalytic complex, where subunits cooperate to stabilize the heme environment and coordinate access to substrate and reductant. The absence of transmembrane segments and the soluble enzyme fold argue for a cytosolic location, where substrate availability and redox partners are abundant; thus a cytosolic catalytic complex is the most plausible operational site.

From this mechanistic base, I hypothesize interaction partners and pathway wiring. Kynurenine formamidase likely associates functionally to receive N-formylkynurenine or kynurenine, creating a substrate channel that minimizes diffusion and protects labile intermediates. Kynurenine 3-monooxygenase would engage downstream to convert kynurenine toward 3-hydroxykynurenine, linking to NAD+ biosynthesis and oxidative stress chemistry. Tyrosine aminotransferase may intersect at points of aromatic amino acid balance, drawing on kynurenine-derived pools or competing for shared cofactors and redox currency. Hormone-sensitive lipase could modulate local lipid-derived NADPH production or membrane-proximal redox microenvironments that influence the reductase-dependent step. The phosphotransferase LOC123688 and several Anopheles gene products (AGAP006020-PA., AGAP009091-PA., AGAP011158-PA., AGAP004500-PA., AGAP003887-PB.) plausibly act as regulatory or scaffolding factors that tune activity via phosphorylation, complex assembly, or localization, thereby coupling tryptophan catabolism to developmental or stress-responsive programs in the mosquito.

    ## Functional Summary

    A heme-dependent dioxygenase in the African malaria mosquito that assembles into a soluble catalytic complex and catalyzes the first, rate-setting step of tryptophan breakdown by inserting oxygen across the indole ring of L-tryptophan to form N-formylkynurenine. The reaction requires a physiological reductant, consistent with electron transfer to the heme–oxygen intermediate during catalysis. By committing tryptophan to the kynurenine pathway, it governs flux into downstream catabolic branches, with proximal enzymes likely associating to channel intermediates and coordinate redox supply in the cytosol.

    ## UniProt Summary

    Heme-dependent dioxygenase that catalyzes the first and rate-limiting step of the catabolism of the essential amino acid tryptophan along the kynurenine pathway. Catalyzes the oxidative cleavage of the L-tryptophan indole ring and converts L-tryptophan to N-formylkynurenine. Requires a reductant to be physically and functionally incorporated in the catalytic cycle (By similarity).

    ## InterPro Domains

        - IPR004981: Tryptophan 2,3-dioxygenase (family) [8-378]
    - IPR004981: Tryptophan 2,3-dioxygenase (family) [11-358]
    - IPR004981: Tryptophan 2,3-dioxygenase (family) [20-358]
    - IPR037217: Tryptophan/Indoleamine 2,3-dioxygenase-like (homologous_superfamily) [27-359]

    ## GO Term Predictions

    ### Molecular Function


    ### Biological Process


    ### Cellular Component

