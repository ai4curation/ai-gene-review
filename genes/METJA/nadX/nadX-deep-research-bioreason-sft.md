    ---
    provider: bioreason-pro
    model: SFT
    source: huggingface.co/datasets/wanglab/protein_catalogue
    date: '2026-04-04'
    uniprot_id: Q58325
    gene: nadX
    organism: Methanocaldococcus jannaschii (strain ATCC 43067 / DSM 2661 / JAL-1 / JCM 10045 / NBRC 100440) (Methanococcus jannaschii)
    ---

    ## Thinking Trace

    The architecture begins with an N-terminal dinucleotide-binding module: IPR036291 (NAD(P)-binding domain superfamily, residues 1–146) overlaps IPR005106 (Aspartate/homoserine dehydrogenase, NAD-binding domain, residues 8–121), establishing a Rossmann-like fold that positions the pyrophosphate and ribose of NADP(H) for hydride transfer. This is followed by a catalytic core: IPR002811 (Aspartate dehydrogenase domain, residues 168–253), which houses the active-site residues that bind L-aspartate and stabilize the oxaloacetate intermediate. Three family-level signatures span nearly the full polypeptide—IPR011182 (L-aspartate dehydrogenase family, residues 1–267), IPR020626 (L-aspartate dehydrogenase, prokaryotic family, residues 2–265), and IPR022487 (L-aspartate dehydrogenase, archaeal family, residues 27–264)—together specifying a prokaryotic/archaeal L-aspartate dehydrogenase scaffold. The juxtaposition of an N-terminal Rossmann-like NADP-binding region with a C-terminal aspartate dehydrogenase catalytic domain causes a reversible redox chemistry on L-aspartate’s C2, using NADP+ as electron acceptor to form oxaloacetate and NH4+, or using NAD+ as donor to oxidize oxaloacetate back to L-aspartate. The archaeal/prokaryotic family context typically enforces dimerization, where each protomer contributes to the stability of the partner’s active site; this explains protein homodimerization activity (GO:0042803). The presence of both NADP binding (GO:0050661) and NAD binding (GO:0051287) follows directly from the dual-cofactor Rossmann features and the known bidirectionality of the reaction.

At the process level, the NADP-dependent oxidative direction supplies oxaloacetate that feeds into the shikimate pathway, where oxaloacetate condenses with phosphoenolpyruvate to form phosphoenolpyruvate-derived intermediates en route to chorismate. Thus, the enzyme’s redox activity causally supports the chorismate biosynthetic process (GO:0009423) by provisioning oxaloacetate under NADP+–favored conditions. The archaeal family signature and lack of transmembrane segments indicate a soluble enzyme. In prokaryotic/archaeal cells, such central metabolic dehydrogenases operate in the cytoplasm, aligning with a cytoplasmic localization (GO:0005737).

Mechanistically, the N-terminal Rossmann-like domain binds NADP+ with preference, orienting the nicotinamide for hydride acceptance, while the C-terminal catalytic domain binds L-aspartate and promotes hydride transfer to NADP+, yielding oxaloacetate and releasing ammonium. The archaeal family context implies a homodimer that stabilizes the catalytic geometry and may create a metabolon interface. In this role, the enzyme likely associates with quinolinate synthetase (nadA) to channel aspartate-derived flux toward NAD biosynthesis, and with aspartate carbamoyltransferase regulatory and catalytic chains (pyrI, pyrB) to balance aspartate partitioning between pyrimidine and purine branches. Interactions with aspartate aminotransferase (aspB1) would buffer oxaloacetate/aspartate pools, while contacts with adenylosuccinate synthetase (purA), argininosuccinate synthetase (argG), and asparagine synthetase (asnB) would coordinate nitrogen and aspartate utilization. Association with a pantothenate metabolism flavoprotein (dfp) and a conserved hypothetical protein could stabilize a broader central-metabolism assembly that tunes cofactor availability and flux directionality according to cellular redox state.

    ## Functional Summary

    A soluble archaeal dehydrogenase that forms a homodimer and uses a Rossmann-like dinucleotide-binding module to bind NADP+ preferentially alongside a catalytic domain that oxidizes L-aspartate to oxaloacetate with release of ammonium, or reduces oxaloacetate to L-aspartate with NAD+. By supplying oxaloacetate under NADP+-favored conditions, it feeds the shikimate pathway toward chorismate and coordinates aspartate flux with neighboring metabolic nodes in the cytoplasm.

    ## UniProt Summary

    Catalyzes the reversible oxidation of L-aspartate to oxaloacetate. Has a preference for NADP(+) as a hydrogen acceptor. Plays a role in the chorismate biosynthesis pathway.

    ## InterPro Domains

        - IPR011182: L-aspartate dehydrogenase (family) [1-267]
    - IPR036291: NAD(P)-binding domain superfamily (homologous_superfamily) [1-146]
    - IPR020626: L-aspartate dehydrogenase, prokaryotic (family) [2-265]
    - IPR005106: Aspartate/homoserine dehydrogenase, NAD-binding (domain) [8-121]
    - IPR022487: L-aspartate dehydrogenase, archaeal (family) [27-264]
    - IPR002811: Aspartate dehydrogenase (domain) [168-253]

    ## GO Term Predictions

    ### Molecular Function


    ### Biological Process


    ### Cellular Component

