    ---
    provider: bioreason-pro
    model: SFT
    source: huggingface.co/datasets/wanglab/protein_catalogue
    date: '2026-04-04'
    uniprot_id: P53301
    gene: CRH1
    organism: Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast)
    ---

    ## Thinking Trace

    I begin with the InterPro architecture. The N-terminal half is dominated by glycoside hydrolase family-16 signatures: IPR050546 (Glycosyl Hydrolase Family 16, residues 11–258) overlaps with two concordant domain calls, IPR000757 (Beta-glucanase-like, N-terminal domain, residues 34–260) and IPR000757 (Beta-glucanase-like, N-terminal domain, residues 69–235), all embedded within the broader IPR013320 (Concanavalin A-like lectin/glucanase domain superfamily, residues 52–257). This cluster defines the canonical GH16 β-jelly-roll catalytic fold that uses a retaining double-displacement mechanism to cleave β-1,3-glucan with a catalytic glutamate pair and to transfer the glycan to an acceptor. The entire polypeptide is further classified by IPR017168 (CRH-like family, residues 18–485), which specifies the specialized fungal clade of GH16 enzymes that act as chitin β-glucan transglycosylases. The ordered layout—an N-terminal GH16 catalytic core followed by a C-terminal region that typically harbors a GPI-attachment signal—creates a secretory, cell-surface enzyme optimized to remodel the cell wall by forming new β-1,3-glucan linkages to chitin.

This GH16/CRH-like architecture causes glycosyltransfer-like chemistry in a transglycosylation mode: the catalytic nucleophile forms a glycosyl–enzyme intermediate from a β-1,3-glucan donor, then transfers the glucan to the non-reducing end of chitin, extending the chitin chain. That mechanism directly supports the molecular function formalized as GO:0016757 glycosyltransferase activity, here realized as a retaining transglycosylation rather than a simple hydrolysis.

By extending chitin with β-1,3-glucan and cross-linking these polymers, the enzyme drives the assembly and maturation of the fungal cell wall. This places it squarely in GO:0006037 cell wall chitin metabolic process and, at a higher organizational level, in GO:0031505 fungal-type cell wall organization. The CRH-like family is known to be essential for robust wall architecture, and the catalytic logic here provides the cross-linking needed to integrate chitin with the glucan network.

The presence of a GPI-anchor signal inferred from the CRH-like family and the absence of transmembrane helices indicate extracellular targeting via the secretory pathway, with the enzyme attached to the outer leaflet of the plasma membrane and covalently or noncovalently incorporated into the wall matrix. This explains localization to the GO:0009277 fungal-type cell wall and, during polarized growth, enrichment at the GO:0000131 incipient cellular bud site where wall construction is initiated. The GPI anchor ensures the catalytic domain is presented to the periplasmic/cell wall space, where its substrates—chitin and β-1,3-glucan—reside.

Mechanistically, the enzyme likely operates in concert with other wall-remodeling factors. A plausible partner is the probable glycosidase CRH2, which can provide complementary transglycosylation or processing of glucan acceptors, forming a cooperative pair that tunes cross-link density. The 1,3-beta-glucanosyltransferase GAS1 can elongate β-1,3-glucan chains that then become donors or acceptors for this enzyme, creating a feed-forward loop that builds robust glucan scaffolds. Endo-beta-1,3-glucanase can trim or open glucan chains to generate optimal acceptor termini, increasing efficiency of transglycosylation. Cell wall proteins with GPI-attachment sites, including mannoproteins that mark birth scars, likely serve as structural substrates or scaffolds that spatially constrain the reaction during bud formation and daughter-cell differentiation. Together, these interactions would coordinate polymer remodeling and cross-linking precisely where wall expansion and septation occur.

    ## Functional Summary

    A GPI-anchored cell-surface transglycosylase in baker’s yeast that extends chitin chains using β-1,3-glucan as a donor, thereby cross-linking chitin into the glucan network and strengthening the cell wall. Its GH16 catalytic core executes a retaining double-displacement reaction that transfers glucan to the non-reducing end of chitin, integrating polymers during wall assembly and polarized growth. The enzyme concentrates at nascent bud sites and birth scars, where it collaborates with glucanases, glucanosyltransferases, and other GPI-anchored mannoproteins to organize the wall architecture.

    ## UniProt Summary

    Involved in cell wall construction. Extends chitin with beta-1,3-glucan. May be involved in the cross-linking of chitin to the glucan network of the cell wall.

    ## InterPro Domains

        - IPR050546: Glycosyl Hydrolase Family 16 (family) [11-258]
    - IPR017168: CRH-like (family) [18-485]
    - IPR000757: Beta-glucanase-like, N-terminal domain (domain) [34-260]
    - IPR013320: Concanavalin A-like lectin/glucanase domain superfamily (homologous_superfamily) [52-257]
    - IPR000757: Beta-glucanase-like, N-terminal domain (domain) [69-235]

    ## GO Term Predictions

    ### Molecular Function


    ### Biological Process


    ### Cellular Component

