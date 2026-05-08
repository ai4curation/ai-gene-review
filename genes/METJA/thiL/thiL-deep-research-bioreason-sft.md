    ---
    provider: bioreason-pro
    model: SFT
    source: huggingface.co/datasets/wanglab/protein_catalogue
    date: '2026-04-04'
    uniprot_id: Q60337
    gene: thiL
    organism: Methanocaldococcus jannaschii (strain ATCC 43067 / DSM 2661 / JAL-1 / JCM 10045 / NBRC 100440) (Methanococcus jannaschii)
    ---

    ## Thinking Trace

    I begin with the InterPro architecture. The sequence is dominated by multiple overlapping signatures of the thiamine-monophosphate kinase-like family: IPR006283 (Thiamine-monophosphate kinase-like, family) spans residues 1–318, 1–305, 1–303, and 2–299, and is also captured as IPR006283 [3–303]. Embedded within this family scaffold are two PurM-like structural modules: an N-terminal PurM-like domain (IPR016188, residues 27–138) nested inside the PurM-like N-terminal domain superfamily (IPR036921, residues 1–142 and 2–139), followed by a C-terminal PurM-like domain superfamily (IPR036676, residues 145–317 and 146–303). This arrangement—an N-lobe and a C-lobe that together form a bilobal PurM-like fold—creates a cleft that binds a nucleotide and a small-molecule acceptor. In thiamine-phosphate kinases, this bilobal architecture positions ATP in the interdomain cleft while a basic pocket recognizes the thiamine monophosphate (TMP) phosphate and pyrimidine, enabling in-line transfer of the γ-phosphate from ATP to TMP. The repeated, nearly coterminous family signatures (residues ~1–317) indicate a single compact enzyme without accessory domains, consistent with a soluble, single-subunit kinase.

This domain architecture causally supports two molecular functions. First, the interdomain cleft and conserved P-loop-like/lysine-rich features typical of this fold create a canonical nucleotide-binding site, accounting for GO:0005524 ATP binding. Second, the family-defining chemistry of the thiamine-monophosphate kinase-like scaffold specifies GO:0004789 thiamine-phosphate kinase activity: the enzyme transfers a phosphate from ATP to TMP to generate thiamine pyrophosphate (TPP). The same active-site geometry can accommodate the closely related deaza analog, thus enabling activity toward 4-amino-5-hydroxymethyl-2-methylpyrimidin-4(3H)-one monophosphate (HOMO), i.e., a deazapurine monophosphate kinase reaction.

The catalytic output, TPP, is the active coenzyme form of thiamine diphosphate, a central cofactor for central carbon metabolism. Therefore, the enzyme’s activity directly drives GO:0009228 thiamine biosynthetic process by converting the monophosphate intermediate to the diphosphate coenzyme state. Because the architecture lacks transmembrane segments or export signals and matches a soluble PurM-like bilobal enzyme, the most plausible cellular location is the cytosol, aligning with GO:0005737 cytoplasm, where nucleotide and thiamine-pathway intermediates are abundant.

Mechanistically, the N- and C-terminal PurM-like lobes close around ATP and TMP to form a catalytically competent pocket. A conserved lysine and acidic residue network stabilizes the transition state and orients the phosphate groups for direct in-line transfer, yielding TPP and ADP. The same pocket tolerates the deaza analog HOMO, explaining the observed substrate flexibility. In the cellular context, this enzyme likely operates within a thiamine-biosynthesis metabolon: transient associations with thiamine biosynthesis protein (thiC) would channel upstream intermediates toward TMP, while adenylate kinase (adk) would buffer ATP/ADP ratios to sustain high-flux phosphoryl transfer. The proximity of purine-pathway enzymes such as GTP cyclohydrolase II (ribA) and phosphoribosylformylglycinamidine cyclo-ligase (purM) suggests a broader nucleotide-cofactor hub, where purine and thiamine biosynthesis co-localize to balance nucleotide pools and cofactor supply. Riboflavin synthase beta chain (ribH) indicates a possible cofactor biogenesis cluster coordinating multiple vitamin pathways. The proliferating-cell nucleolar antigen FMU/NOL1/NOP2 family protein implies a link to pyrimidine/folate-related metabolism, potentially stabilizing nucleotide pools that support cofactor synthesis. The conserved and hypothetical proteins likely act as adaptors or scaffolds that stabilize these transient assemblies, enhancing substrate channeling and protecting reactive intermediates. Altogether, the domain architecture dictates ATP-dependent phosphorylation of TMP (and HOMO) in the cytoplasm, feeding TPP production and integrating with adjacent vitamin and nucleotide metabolic nodes.

    ## Functional Summary

    A cytosolic enzyme that phosphorylates thiamine monophosphate using ATP to produce thiamine pyrophosphate, the active coenzyme form required for central carbon metabolism. Its bilobal active site binds ATP and the thiamine phosphate acceptor to drive in-line phosphate transfer, and the same pocket can accept the deaza analog of the substrate, enabling phosphorylation of a deazapurine monophosphate. The enzyme likely operates within a metabolon that couples thiamine pathway intermediates to ATP supply and coordinates with neighboring vitamin and nucleotide biosynthetic enzymes to sustain cofactor production.

    ## UniProt Summary

    Catalyzes the phosphorylation of thiamine-monophosphate (TMP) to thiamine-pyrophosphate (TPP). Also catalyzes the phosphorylation of 4-amino-5-hydroxymethyl-2-methylpyrimidin-4(3H)-one monophosphate (HOMO).

    ## InterPro Domains

        - IPR006283: Thiamine-monophosphate kinase-like (family) [1-318]
    - IPR006283: Thiamine-monophosphate kinase-like (family) [1-305]
    - IPR006283: Thiamine-monophosphate kinase-like (family) [1-303]
    - IPR036921: PurM-like, N-terminal domain superfamily (homologous_superfamily) [1-142]
    - IPR006283: Thiamine-monophosphate kinase-like (family) [2-299]
    - IPR036921: PurM-like, N-terminal domain superfamily (homologous_superfamily) [2-139]
    - IPR006283: Thiamine-monophosphate kinase-like (family) [3-303]
    - IPR016188: PurM-like, N-terminal domain (domain) [27-138]
    - IPR036676: PurM-like, C-terminal domain superfamily (homologous_superfamily) [145-317]
    - IPR036676: PurM-like, C-terminal domain superfamily (homologous_superfamily) [146-303]

    ## GO Term Predictions

    ### Molecular Function


    ### Biological Process


    ### Cellular Component

