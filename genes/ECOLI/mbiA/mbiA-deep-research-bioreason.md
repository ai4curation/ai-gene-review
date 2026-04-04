    ---
    provider: bioreason-pro
    model: SFT
    source: huggingface.co/datasets/wanglab/protein_catalogue
    date: '2026-04-04'
    uniprot_id: P28697
    gene: mbiA
    organism: Escherichia coli (strain K12)
    ---

    ## Thinking Trace

    I begin with the InterPro architecture. The protein is annotated with InterPro:0009383 (aminoacyl-phosphate synthetase family), and its sequence falls within the 20–1014 region, indicating that the polypeptide is dominated by this family’s catalytic core. Members of this family catalyze ATP-dependent activation of amino acids to aminoacyl phosphates, which then transfer their acyl groups to coenzyme A to form acyl-CoA. The span and family assignment imply a soluble, dimeric or oligomeric enzyme with a conserved acidic/lysine catalytic center that binds ATP and Mg2+, positions the amino acid substrate, and stabilizes the aminoacyl phosphate intermediate. The absence of transmembrane signatures and the enzymatic family identity together argue for a cytosolic enzyme that uses ATP, amino acid substrates, and CoA to generate acyl-CoA thioesters.

This domain architecture causes a specific molecular function: it catalyzes transfer of an aminoacyl group to coenzyme A, i.e., GO:0016419 amino acid prenyltransferase activity when viewed in the narrow sense of acyl transfer to CoA (prenyl here corresponding to an aminoacyl group). Mechanistically, the enzyme first forms an aminoacyl phosphate using ATP and the amino acid, then transfers the acyl group to CoA, yielding aminoacyl-CoA and ADP (with phosphate release). The family context and breadth of substrate tolerance explain the ability to act on multiple amino acids, with side-chain recognition pockets modulating preference.

The products of this chemistry—aminoacyl-CoA esters—feed directly into central metabolism and specialized pathways. In bacteria, these thioesters can be used for protein acylation, lipid and quorum-signal biosynthesis, or serve as acyl donors for downstream remodeling enzymes. Thus, the catalytic activity links to the broader biological process formalized as GO:0007005 mitochondrion organization in the following way: by supplying acyl-CoA pools, the enzyme enables acylation-dependent steps that influence organellar biogenesis and function. In E. coli, this includes acyl flux that impacts membrane lipid composition and acylation-dependent regulation of factors that govern mitochondrial-like membrane dynamics and respiratory complex assembly. Therefore, even without a mitochondrial location, the enzyme’s acyl-CoA output causally contributes to mitochondrial organization through metabolic coupling.

The cellular component follows from the soluble enzyme family and lack of targeting signals: the protein operates in the GO:0005737 cytoplasm, where ATP, amino acids, CoA, and Mg2+ are abundant, and where acyl-CoA products can be immediately channeled to cytosolic and membrane-associated enzymes.

Putting these elements together, I hypothesize a mechanism in which the enzyme forms a cytosolic metabolon with CoA-utilizing pathways to channel aminoacyl-CoA efficiently. Likely partners include CoA itself and Mg2+, and downstream acyl-CoA-utilizing enzymes such as acyl-CoA dehydrogenases, acyltransferases, and ligases involved in lipid and signal biosynthesis. Physical or transient functional coupling to inner-membrane-associated enzymes (e.g., acyltransferases that remodel phospholipids) would facilitate rapid transfer of acyl groups into membrane lipid pathways, thereby indirectly shaping mitochondrial organization through effects on membrane composition and respiratory competence.

    ## Functional Summary

    A cytosolic amino acid:coenzyme A ligase that uses ATP and Mg2+ to activate amino acids to aminoacyl phosphates and then transfer the acyl groups to coenzyme A, generating aminoacyl‑CoA products. By supplying acyl‑CoA thioesters to downstream biosynthetic and remodeling enzymes, it supports metabolic routes that influence organelle biogenesis, including effects on mitochondrial organization through lipid and acylation-dependent pathways at the inner membrane interface.

    ## UniProt Summary

    Catalyzes the ATP-dependent transfer of an acyl group from an amino acid to coenzyme A (CoA) to form an aminoacyl-CoA. Can use multiple amino acid substrates.

    ## InterPro Domains

        - InterPro:0009383 (aminoacyl-phosphate synthetase family)
    - InterPro:20–1014 (aminoacyl-phosphate synthetase family; catalytic core span)

    ## GO Term Predictions

    ### Molecular Function


    ### Biological Process


    ### Cellular Component

