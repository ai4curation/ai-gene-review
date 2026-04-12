    ---
    provider: bioreason-pro
    model: SFT
    source: huggingface.co/datasets/wanglab/protein_catalogue
    date: '2026-04-04'
    uniprot_id: Q01820
    gene: gcl
    organism: Drosophila melanogaster (Fruit fly)
    ---

    ## Thinking Trace

    The architecture begins with IPR043380 (Germ cell-less protein-like family, residues 1–497) spanning the full length, indicating a lineage-specific adaptor dedicated to germline specification. Embedded within the N-terminal third is a cluster of BTB/POZ signatures: IPR011333 (SKP1/BTB/POZ domain superfamily, residues 37–195) and its refined spans IPR011333 at residues 51–164, together with the core IPR000210 (BTB/POZ domain, residues 57–164, 66–136, 66–166). This arrangement defines a canonical BTB/POZ fold that dimerizes and creates a docking surface for Cullin-3. The BTB module causes high-affinity binding to CUL3 and positions the protein as a substrate-recognition subunit within a CUL3–RBX1 RING E3 ligase. The family-level envelope (IPR043380) implies additional, family-specific regions outside the BTB core that provide substrate-binding determinants and subcellular targeting cues.

From this domain logic, the molecular function resolves to ubiquitin ligase-substrate adaptor activity (GO:1990756): the BTB/POZ domain binds CUL3, while other regions capture specific targets, thereby determining which proteins are polyubiquitinated. The direct outcome of this adaptor action is protein polyubiquitination (GO:0000209) and subsequent proteasome-mediated ubiquitin-dependent protein catabolic process (GO:0043161). In the germline context, selective degradation of cortical determinants modulates cell fate. By promoting turnover of cortical factors such as the posterior determinant that seeds germ plasm, the adaptor enforces pole cell fate determination (GO:0007280) and contributes to germ cell development (GO:0007281). The same degradative control can attenuate transcriptional programs by clearing transcriptional regulators, providing a route to negative regulation of transcription by RNA polymerase III (GO:0016480), for example by removing factors that influence Pol III–dependent small RNA or tRNA gene expression during early development.

The BTB–CUL3 interface dictates assembly into a Cul3-RING ubiquitin ligase complex (GO:0031463). The family’s role in germline specification and cortical clearance points to a cytoplasmic (GO:0005737) and cell cortex (GO:0005938) residency, where it can access cortical germ plasm components. The presence of nuclear pore (GO:0005643) and nuclear periphery (GO:0034399) localization is consistent with shuttling adaptors that also sample the nuclear envelope to regulate nuclear-proximal substrates or to coordinate degradation with nuclear transport. This spatial distribution enables the protein to couple cortical remodeling with nuclear regulatory outputs.

Mechanistically, the BTB/POZ core dimerizes and binds CUL3, recruiting RBX1 to form the catalytic RING module. The family-specific regions likely recognize the posterior determinant and other cortical or nuclear-envelope substrates, positioning lysines for K48-linked polyubiquitin chain assembly and proteasomal delivery. Interaction partners align with this model: Cullin 3, isoform F and RING-box proteins 1A/1B provide the ligase scaffold and catalytic RING; roadkill and Kelch-like proteins (klhl18 and klhl10) are alternative CUL3 adaptors that may compete or cooperate to tune substrate selection; maternal effect protein oskar is a germ plasm component whose proximity at the posterior cortex makes it a plausible substrate or scaffolded client; and the succinate–CoA ligase beta subunit suggests metabolic coupling, where local ATP/GTP flux could influence ubiquitination efficiency at the cortex. Together, these features support a model in which a BTB-driven CUL3 adaptor orchestrates targeted polyubiquitination at the cortex and nuclear periphery to specify pole cells and modulate transcriptional programs during early germline development.

    ## Functional Summary

    A BTB/POZ-domain adaptor that assembles with a Cullin-3–RING E3 ligase to promote selective polyubiquitination and proteasomal degradation of specific substrates during early development. By concentrating at the cell cortex and sampling the nuclear periphery and nuclear pore, it clears posterior cortical determinants to drive pole cell specification and contributes to germ cell development, while also dampening RNA polymerase III–dependent transcriptional programs through turnover of regulatory factors. Its mechanism centers on BTB-mediated CUL3 binding and dimerization, with family-specific regions conferring substrate recognition and spatial targeting.

    ## UniProt Summary

    May function as a substrate recognition component of a SCF-like E3 ubiquitin-protein ligase complex which mediates the ubiquitination and subsequent proteasomal degradation of target proteins. Required for pole cell formation.

    ## InterPro Domains

        - IPR043380: Germ cell-less protein-like (family) [1-497]
    - IPR011333: SKP1/BTB/POZ domain superfamily (homologous_superfamily) [37-195]
    - IPR011333: SKP1/BTB/POZ domain superfamily (homologous_superfamily) [51-164]
    - IPR000210: BTB/POZ domain (domain) [57-164]
    - IPR000210: BTB/POZ domain (domain) [66-136]
    - IPR000210: BTB/POZ domain (domain) [66-166]

    ## GO Term Predictions

    ### Molecular Function


    ### Biological Process


    ### Cellular Component

