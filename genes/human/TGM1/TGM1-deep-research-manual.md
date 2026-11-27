# TGM1 manual deep research

`just deep-research-perplexity-lite human TGM1` could not be run because the only configured provider in this checkout was `claude_code`, so this file records manual synthesis from cached UniProt, Reactome, GOA, PAINT, and primary-publication abstracts.

TGM1 encodes the membrane-anchored epidermal transglutaminase. The enzyme catalyzes calcium-dependent transfer between peptide-bound glutamine and lysine to form N-epsilon-(gamma-glutamyl)lysine isopeptide crosslinks, and UniProt cites direct biochemical support from PMID:7629111, PMID:8824274, and PMID:20663883 for that EC 2.3.2.13 activity. PAINT places the generic protein-glutamine gamma-glutamyltransferase activity on the PTHR11590 root, consistent with all reviewed human catalytic members of the family.

The main evolved role of TGM1 is formation of the cornified envelope at the cytoplasmic side of the keratinocyte plasma membrane. PMID:7629111 describes soluble full-length and processed 67/33 kDa active forms in epidermal keratinocytes, PMID:8824274 shows that myristate and palmitate attachment control partitioning between cytosol and membrane, and Reactome records TGM1 crosslinking of involucrin, loricrin, and small proline-rich substrates during early and reinforcing steps of cornified-envelope assembly. The root PANTHER family does not propagate the keratinocyte-differentiation term to every descendant; a narrower node, PTN002612891, supports that process for TGM1.

Several rows are generic interaction rows from high-throughput IntAct experiments. They preserve useful interaction evidence in IntAct, but GO:0005515 protein binding does not identify a specific activity and should be removed under the protein-binding policy while keeping each WITH/FROM value distinct.

TGM1 also has ARCI-mutation studies showing that loss-of-function alleles impair keratinocyte growth or differentiation markers. Those rows are biologically connected to the cornified-envelope defect but are best treated as downstream or peripheral process effects rather than separate core catalytic functions.
