# HSPB7 (Q9UBY9) research notes

## Identity
- Heat shock protein beta-7 / cardiovascular heat shock protein (cvHsp), small heat shock protein (HSP20/alpha-crystallin) family, 170 aa, ~18.6 kDa.
- Identified as a novel small stress protein selectively expressed in cardiovascular and insulin-sensitive tissues [PMID:10593960 "a novel small stress protein of 170 amino acids that we named cvHsp"; "expression was high in heart, medium in skeletal muscle, and low in aorta or adipose tissues."].

## Tissue
- Heart-enriched; HPA group enriched (heart muscle, skeletal muscle, tongue) [file:human/HSPB7/HSPB7-uniprot.txt "HPA; ENSG00000173641; Group enriched (heart muscle, skeletal muscle, tongue)."]. Isoform 1 highly expressed in adult/fetal heart and skeletal muscle.

## Molecular interactions / function
- Binds alpha-filamin (filamin / actin-binding protein 280); residues 56-119 important [PMID:10593960 "cvHsp interacted ... with alpha-filamin or actin-binding protein 280. Within cvHsp, amino acid residues 56-119 were shown to be important for its specific interaction with the C-terminal tail of alpha-filamin."]. UniProt SUBUNIT: "Interacts with C-terminal domain of actin-binding protein 280." GOA: filamin binding (IEA, Ensembl ortholog).
- Forms hetero-oligomers with other small HSPs: HSPB8 (HSP22), HSPB2 (MKBP), HSPB1 (HSP27) [PMID:14594798 "HSP22 interacts with itself, cvHSP (HSPB7), MKBP (HSPB2) and HSP27"; "HSP22-cvHSP hetero-dimers through C-C interaction."]. UniProt INTERACTION list includes HSPB8 (Q9UJY1) and BAG3 (O95817).
- In the Vos HSPB-family survey, classical members HSPB1/HSPB5 refolded heat-unfolded substrate but HSPB7 did not [PMID:19464326 "Unlike HSPB1 and HSPB5, that chaperoned heat unfolded substrates and kept them folding competent, HSPB7 did not support refolding."; "Our data suggest a non-chaperone-like role of HSPB7 at SC35 speckles."]. This negative refolding result argues against GO:0044183 (protein folding chaperone).
- Direct evidence establishes substrate-selective antiaggregation activity. HSPB7 suppresses polyQ aggregation and toxicity early in aggregate formation [PMID:20843828 "HSPB7 prevents toxicity of polyQ proteins at an early stage of aggregate formation by a non-canonical mechanism that requires an active autophagy machinery."]. Full-text biochemical evidence shows that purified HSPB7 acts directly and binds early aggregation intermediates [PMID:31097540 "HSPB7 acts directly on the aggregation process as recombinant HSPB7 can delay in vitro polyQ aggregation, whereas HSPB1 cannot."; "Our co-IP experiments, performed using soluble material, suggest that HSPB7 binds to early profibrillar species."]. This does not establish GO:0140309 because its current definition additionally requires escort of the bound substrate to an acceptor molecule or specific location; the paper does not demonstrate that delivery step.

## Localization
- Cytoplasm and nucleus; constitutively resides in SC35 nuclear splicing speckles, driven by its N-terminus (residues 1-71) [file:human/HSPB7/HSPB7-uniprot.txt "Note=Resides in sub-nuclear structures known as SC35 speckles or nuclear splicing speckles."; FT REGION 1..71 "Required for localization to SC35 splicing speckles"; PMID:19464326 "HSPB7 constitutively localized to SC35 splicing speckles, driven by its N-terminus."].
- UniProt also lists Nucleus, Cajal body. GOA: aggresome (IDA, HPA), nucleoplasm (IDA, HPA), actin cytoskeleton (IEA ortholog).

## GO review reasoning
- protein binding (IPI, GO:0005515) x many: uninformative bare term. HSPB8-only signatures can be MODIFY-ed to heat shock protein binding and the FLNA-only signature to filamin binding. Heterogeneous high-throughput signatures from PMID:25416956 and PMID:32296183 are MARK_AS_OVER_ANNOTATED because no single evidence-matched MF covers their partner sets.
- filamin binding (GO:0031005, IEA ortholog): supported by direct experimental human data (PMID:10593960). ACCEPT/MODIFY-up; this is a genuine MF for cvHsp.
- regulation of heart contraction (GO:0008016, TAS): cvHsp is cardiac-enriched and binds filamin; plausible but indirect; KEEP_AS_NON_CORE.
- heart development (GO:0007507, IEA InterPro): IEA ortholog/family; KEEP_AS_NON_CORE.
- response to unfolded protein (GO:0006986, TAS): KEEP_AS_NON_CORE. PMID:10593960 identifies a small stress protein, expression pattern and filamin interaction, but its cached abstract does not report an unfolded-protein response assay.
- Localization terms (cytoplasm, nucleus IBA/IDA/IEA): ACCEPT. Cajal body (IEA): KEEP_AS_NON_CORE. actin cytoskeleton (IEA ortholog): KEEP_AS_NON_CORE (consistent with filamin binding).

## PAINT audit (2026-08-28)
- Both IBA rows trace exactly to `PANTHER:PTN002930548` in family `PTHR46907` (small heat shock protein HSP20; HSPB7 subfamily `PTHR46907:SF2`). The cached PAINT table places GO:0005634 (nucleus) and GO:0005737 (cytoplasm) at that node with human HSPB7/Q9UBY9 as descendant evidence.
- The target appearing in its own WITH/FROM is expected experimental grounding for an IBD placement, not circularity. Both transfers are retained as `NO_FAILURE_CORE`, independently corroborated by PMID:19464326 IDA annotations.

## Signature reconciliation (2026-08-28)
- The 41 physical GOA rows collapse to 17 exact qualifier-aware signatures: 6 `enables`, 3 `involved_in`, 2 `is_active_in`, and 6 `located_in`. All 17 are represented exactly once in the review.
- Final actions: 7 ACCEPT, 5 KEEP_AS_NON_CORE, 3 MODIFY, 2 MARK_AS_OVER_ANNOTATED, 0 REMOVE, and 0 UNDECIDED.
- GO:0051082 is obsolete in current GO, with GO:0044183 and GO:0140309 listed as considerations. It occurred only in the author-supplied core function, not in the current physical GOA rows, so no machine-sourced annotation id was rewritten.
- Follow-up evidence update: cached PMID:31097540 full text supplies direct binding and in-vitro aggregation-delay evidence, but no current term precisely captures that activity. GO:0140309 is not asserted because its live definition is carrier/delivery-specific, and GO:0044183 remains excluded because HSPB7 does not refold heat-denatured substrate.

## Core functions
1. Filamin binding (GO:0031005), established directly by yeast two-hybrid and immunoprecipitation in PMID:10593960.
2. HSPB7 has a directly demonstrated substrate-selective polyQ antiaggregation activity, but it is not assigned a core MF term: GO:0140309 requires evidence of substrate escort/delivery, whereas PMID:31097540 demonstrates binding and aggregation delay only. GO:0044183 is contradicted by the lack of refolding activity.
</content>
