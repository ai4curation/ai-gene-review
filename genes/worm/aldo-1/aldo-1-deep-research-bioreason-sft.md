    ---
    provider: bioreason-pro
    model: SFT
    source: huggingface.co/datasets/wanglab/protein_catalogue
    date: '2026-04-04'
    uniprot_id: P54216
    gene: aldo-1
    organism: Caenorhabditis elegans
    ---

    ## Thinking Trace

    The architecture begins with IPR013785 (Aldolase-type TIM barrel, homologous_superfamily) spanning residues 1–366, establishing an (α/β)8 barrel scaffold that positions catalytic residues at the C-terminal ends of the β-strands. Nested within this fold are two overlapping family signatures, IPR000741 (Fructose-bisphosphate aldolase, class-I) from residues 13–366 and IPR000741 (Fructose-bisphosphate aldolase, class-I) from residues 15–366, which specify a class I aldolase that uses a catalytic lysine to form a Schiff base with a carbonyl substrate. The catalytic center is pinpointed by IPR029768 (Fructose-bisphosphate aldolase class-I active site, conserved_site) at residues 223–233, marking the lysine-dependent iminium chemistry that drives carbon–carbon bond cleavage/formation. This ordered layout—TIM barrel scaffold, class I family determinants, and a conserved active-site lysine—causes a reversible aldol cleavage/condensation of fructose 1,6-bisphosphate into dihydroxyacetone phosphate and glyceraldehyde 3-phosphate, which defines GO:0004332 fructose-bisphosphate aldolase activity. Class I aldolases typically assemble as homotetramers; the quaternary interface arises from complementary TIM-barrel surfaces, which necessitates GO:0042802 identical protein binding to form the active oligomer.

Catalysis at this step channels carbon flux through glycolysis and supports gluconeogenesis. In the glycolytic direction, the Schiff-base mechanism cleaves fructose 1,6-bisphosphate to DHAP and G3P, embedding the enzyme in GO:0006096 glycolytic process. Because glycolytic throughput directly sets blood glucose levels in metazoans, the same reaction underpins systemic sugar balance, aligning with GO:0042593 glucose homeostasis. The reversibility of the reaction also supports gluconeogenic assembly of fructose 1,6-bisphosphate from triose phosphates, ensuring metabolic flexibility.

Cellular placement follows from both function and muscle-specific architecture. The TIM-barrel enzyme is soluble and lacks transmembrane features, favoring a cytosolic environment. In striated muscle, glycolytic enzymes are known to dock onto cytoskeletal and adhesion-associated structures to create metabolons that buffer ATP supply during contraction. This explains localization to GO:0030017 sarcomere and GO:0055120 striated muscle dense body, where anchoring near actin-attachment sites positions the enzyme to feed ATP-consuming myofibrillar processes. Association with GO:0005783 endoplasmic reticulum is consistent with peripheral binding to ER membranes or ER–myofibril junctions, enabling local exchange of metabolites and potentially coupling to calcium signaling that modulates glycolytic flux.

Mechanistically, the enzyme likely operates within a sarcomeric glycolytic metabolon. Upstream, ATP-dependent 6-phosphofructokinase 1 and 2 generate fructose 1,6-bisphosphate, which this enzyme cleaves; downstream, triosephosphate isomerase equilibrates DHAP and G3P, and glyceraldehyde-3-phosphate dehydrogenases 1–4 draw flux forward, while an FBPase domain-containing protein can reverse the direction during gluconeogenesis. Glucose-6-phosphate isomerase supplies the hexose substrate pool, and a transket_pyr domain-containing protein may provide auxiliary carbon-shuffling or regulatory interactions. The homomeric assembly (identical protein binding) stabilizes the active site geometry and supports high local catalytic throughput at dense bodies and sarcomeres, with transient ER contacts positioning the metabolon near excitation–contraction machinery. This arrangement ensures rapid, spatially focused energy production to sustain muscle contraction while maintaining whole-organism glucose balance.

    ## Functional Summary

    A class I aldolase in Caenorhabditis elegans that assembles as a homomeric TIM-barrel enzyme to catalyze the reversible cleavage of fructose 1,6-bisphosphate into triose phosphates during glycolysis and the corresponding condensation in gluconeogenesis. By anchoring to sarcomeric structures and dense bodies, and by transiently associating with endoplasmic reticulum interfaces, it forms part of a muscle glycolytic metabolon that channels substrates efficiently to ATP-producing steps, thereby supporting contraction and contributing to organismal glucose balance.

    ## UniProt Summary

    Plays a key role in glycolysis and gluconeogenesis.

    ## InterPro Domains

        - IPR013785: Aldolase-type TIM barrel (homologous_superfamily) [1-366]
    - IPR000741: Fructose-bisphosphate aldolase, class-I (family) [13-366]
    - IPR000741: Fructose-bisphosphate aldolase, class-I (family) [15-366]
    - IPR029768: Fructose-bisphosphate aldolase class-I active site (conserved_site) [223-233]

    ## GO Term Predictions

    ### Molecular Function


    ### Biological Process


    ### Cellular Component

