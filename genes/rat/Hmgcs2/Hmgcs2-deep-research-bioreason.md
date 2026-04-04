    ---
    provider: bioreason-pro
    model: SFT
    source: huggingface.co/datasets/wanglab/protein_catalogue
    date: '2026-04-04'
    uniprot_id: P22791
    gene: Hmgcs2
    organism: Rattus norvegicus (Rat)
    ---

    ## Thinking Trace

    I begin with the InterPro architecture. The polypeptide is built on a thiolase-like scaffold captured by IPR016039 (Thiolase-like homologous superfamily, residues 49–508), which is subdivided into an N-terminal catalytic lobe IPR013528 (Hydroxymethylglutaryl-coenzyme A synthase, N-terminal domain, residues 50–223) and a C-terminal catalytic lobe IPR013746 (Hydroxymethylglutaryl-coenzyme A synthase, C-terminal domain, residues 224–506). The N-terminal region also carries IPR016039 (Thiolase-like homologous superfamily, residues 53–221), while the C-terminal region is likewise encompassed by IPR016039 (Thiolase-like homologous superfamily, residues 224–505). The family-level signature IPR010122 (Hydroxymethylglutaryl-CoA synthase, eukaryotic, residues 50–506) specifies the eukaryotic orthologous lineage, and the catalytic center is pinpointed by IPR000590 (Hydroxymethylglutaryl-coenzyme A synthase, active site, residues 154–169). This two-lobed thiolase-like fold creates an acyl-enzyme chemistry platform in which the active-site cysteine within 154–169 forms a covalent thioester with an acyl substrate, while the opposing lobe positions acetyl-CoA for a Claisen condensation. The eukaryotic family context and the thiolase-like superfamily geometry together cause the specific condensation of acetoacetyl-CoA with acetyl-CoA to produce 3-hydroxy-3-methylglutaryl-CoA, which is the molecular function formalized as GO:0004421 hydroxymethylglutaryl-CoA synthase activity.

This chemistry is the committed entry point to ketogenesis: by generating HMG-CoA, the enzyme supplies substrate to HMG-CoA lyase to form acetoacetate, the precursor of ketone bodies. Thus, the catalytic activity directly drives the GO:1902224 ketone body metabolic process. Because ketone production is mobilized when carbohydrate supply is limited or when fatty acid flux is high, the enzyme’s activity integrates with systemic energy signaling. Nutrient scarcity and hormonal cues (insulin, glucagon, growth hormone, cAMP, glucocorticoids, testosterone, prostaglandins) modulate expression and flux through this step, aligning the enzyme with GO:0042594 response to starvation, GO:0007584 response to nutrient, GO:0032868 cellular response to insulin stimulus, GO:0033762 response to glucagon, GO:0060416 response to growth hormone, GO:0051591 response to cAMP, GO:0071385 cellular response to glucocorticoid stimulus, GO:0033574 response to testosterone, GO:0071417 cellular response to organonitrogen compound, GO:0034694 response to prostaglandin, and GO:0071230 cellular response to amino acid stimulus. Xenobiotic and inflammatory cues (GO:0009410 response to xenobiotic stimulus and GO:0071222 cellular response to lipopolysaccharide) as well as ethanol exposure (GO:0045471 response to ethanol) reshape hepatic metabolism and can upshift ketogenesis, which this enzyme enables. Fatty acid availability (GO:0071398 cellular response to fatty acid) is a proximal determinant of acetyl-CoA supply, thereby causally linking the enzyme to GO:0071398. Developmental contexts that rely on ketone bodies for energy or signaling—GO:0007420 brain development, GO:0030324 lung development, GO:0001822 kidney development, GO:0007494 midgut development, and GO:0001889 liver development—are supported by this catalytic step, which provides the metabolic currency that fuels these tissues and organs during maturation and specialized states.

The thiolase-like fold lacks transmembrane segments and is characteristic of soluble matrix enzymes. The eukaryotic HMG-CoA synthase family is targeted to mitochondria, and the catalytic requirements (acetyl-CoA, acetoacetyl-CoA, and CoA handling) are met in the mitochondrial matrix. Therefore, the cellular component is the GO:0005759 mitochondrial matrix, consistent with a soluble enzyme that assembles transient metabolons with other matrix ketogenesis enzymes.

Mechanistically, the N-terminal thiolase-like lobe positions acetoacetyl-CoA and forms a covalent acyl-enzyme intermediate via the active-site cysteine (154–169). The C-terminal thiolase-like lobe binds acetyl-CoA and orchestrates its attack to forge the C–C bond, yielding HMG-CoA. In the matrix, the product is likely handed directly to hydroxymethylglutaryl-CoA lyase to minimize diffusion and protect reactive thioesters. This predicts physical or functional coupling with mitochondrial HMG-CoA lyase and with upstream acetyl-CoA–producing and –transfer reactions. Accordingly, plausible interaction partners include mitochondrial 3-ketoacyl-CoA thiolase and acetyl-CoA acetyltransferase (supplying acetoacetyl-CoA), the trifunctional enzyme subunit beta and enoyl-CoA hydratase/3,2-trans-enoyl-CoA isomerase (feeding acetyl-CoA via β-oxidation), and succinyl-CoA:3-ketoacid coenzyme A transferase 1 (linking ketone body interconversion). Coordination with 3-hydroxy-3-methylglutaryl-coenzyme A reductase and squalene monooxygenase is expected at the systems level: when reductase operates in the cytosol to make sterols, the mitochondrial synthase’s activity can shift toward ketogenesis, and cross-compartment regulation may involve regulatory crosstalk rather than stable complexes. Cytosolic acetyl-CoA acetyltransferase and cytosolic HMG-CoA lyase may engage during specific conditions or reflect exchange of metabolites and regulatory signals, but the primary catalytic assembly for ketogenesis occurs in the mitochondrial matrix.

    ## Functional Summary

    A soluble mitochondrial matrix enzyme that catalyzes the Claisen condensation of acetyl-CoA with acetoacetyl-CoA to form HMG-CoA, committing carbon flux into ketogenesis. By generating HMG-CoA for downstream cleavage to acetoacetate, it enables ketone body production during nutrient limitation and hormonal activation, integrates signals from insulin, glucagon, cAMP, and other systemic cues, and supports energy demands in developing and metabolically stressed tissues. The thiolase-like fold organizes a covalent acyl-enzyme intermediate and positions substrates for efficient carbon–carbon bond formation, likely operating within a matrix metabolon that channels intermediates to lyase and couples to β-oxidation–derived acetyl-CoA supply.

    ## UniProt Summary

    Catalyzes the condensation of acetyl-CoA with acetoacetyl-CoA to form HMG-CoA, which is converted to acetoacetate by HMG-CoA reductase (HMGCR). Mediates the metabolic flux during ketogenesis.

    ## InterPro Domains

        - IPR016039: Thiolase-like (homologous_superfamily) [49-508]
    - IPR010122: Hydroxymethylglutaryl-CoA synthase, eukaryotic (family) [50-506]
    - IPR013528: Hydroxymethylglutaryl-coenzyme A synthase, N-terminal (domain) [50-223]
    - IPR016039: Thiolase-like (homologous_superfamily) [53-221]
    - IPR000590: Hydroxymethylglutaryl-coenzyme A synthase, active site (active_site) [154-169]
    - IPR013746: Hydroxymethylglutaryl-coenzyme A synthase, C-terminal domain (domain) [224-506]
    - IPR016039: Thiolase-like (homologous_superfamily) [224-505]

    ## GO Term Predictions

    ### Molecular Function


    ### Biological Process


    ### Cellular Component

