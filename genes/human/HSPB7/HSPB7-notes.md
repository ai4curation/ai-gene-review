# HSPB7 (Q9UBY9) research notes

## Identity
- Heat shock protein beta-7 / cardiovascular heat shock protein (cvHsp), small heat shock protein (HSP20/alpha-crystallin) family, 170 aa, ~18.6 kDa.
- Identified as a novel small stress protein selectively expressed in cardiovascular and insulin-sensitive tissues [PMID:10593960 "a novel small stress protein of 170 amino acids that we named cvHsp"; "expression was high in heart, medium in skeletal muscle, and low in aorta or adipose tissues."].

## Tissue
- Heart-enriched; HPA group enriched (heart muscle, skeletal muscle, tongue) [file:human/HSPB7/HSPB7-uniprot.txt "HPA; ENSG00000173641; Group enriched (heart muscle, skeletal muscle, tongue)."]. Isoform 1 highly expressed in adult/fetal heart and skeletal muscle.

## Molecular interactions / function
- Binds alpha-filamin (filamin / actin-binding protein 280); residues 56-119 important [PMID:10593960 "cvHsp interacted ... with alpha-filamin or actin-binding protein 280. Within cvHsp, amino acid residues 56-119 were shown to be important for its specific interaction with the C-terminal tail of alpha-filamin."]. UniProt SUBUNIT: "Interacts with C-terminal domain of actin-binding protein 280." GOA: filamin binding (IEA, Ensembl ortholog).
- Forms hetero-oligomers with other small HSPs: HSPB8 (HSP22), HSPB2 (MKBP), HSPB1 (HSP27) [PMID:14594798 "HSP22 interacts with itself, cvHSP (HSPB7), MKBP (HSPB2) and HSP27"; "HSP22-cvHSP hetero-dimers through C-C interaction."]. UniProt INTERACTION list includes HSPB8 (Q9UJY1) and BAG3 (O95817).
- Non-canonical chaperone: in the Vos HSPB-family survey, classical members HSPB1/HSPB5 refolded heat-unfolded substrate but HSPB7 did NOT support refolding [PMID:19464326 "Unlike HSPB1 and HSPB5, that chaperoned heat unfolded substrates and kept them folding competent, HSPB7 did not support refolding."; "Our data suggest a non-chaperone-like role of HSPB7 at SC35 speckles."]. HSPB7 is, however, an effective suppressor of protein aggregation (e.g. polyQ); it sequesters aggregation-prone proteins rather than refolding them (field consensus; Vos 2010 J Biol Chem).

## Localization
- Cytoplasm and nucleus; constitutively resides in SC35 nuclear splicing speckles, driven by its N-terminus (residues 1-71) [file:human/HSPB7/HSPB7-uniprot.txt "Note=Resides in sub-nuclear structures known as SC35 speckles or nuclear splicing speckles."; FT REGION 1..71 "Required for localization to SC35 splicing speckles"; PMID:19464326 "HSPB7 constitutively localized to SC35 splicing speckles, driven by its N-terminus."].
- UniProt also lists Nucleus, Cajal body. GOA: aggresome (IDA, HPA), nucleoplasm (IDA, HPA), actin cytoskeleton (IEA ortholog).

## GO review reasoning
- protein binding (IPI, GO:0005515) x many: uninformative bare term. The informative interactions are with small HSPs and filamin. MKBP/HSPB8 interactions -> heat shock protein binding. Filamin -> filamin binding (already an IEA term). KEEP_AS_NON_CORE the generic IPI; the HSPB8 (Q9UJY1) IPIs can be MODIFY-ed to heat shock protein binding.
- filamin binding (GO:0031005, IEA ortholog): supported by direct experimental human data (PMID:10593960). ACCEPT/MODIFY-up; this is a genuine MF for cvHsp.
- regulation of heart contraction (GO:0008016, TAS): cvHsp is cardiac-enriched and binds filamin; plausible but indirect; KEEP_AS_NON_CORE.
- heart development (GO:0007507, IEA InterPro): IEA ortholog/family; KEEP_AS_NON_CORE.
- response to unfolded protein (GO:0006986, TAS): stress-protein family role; but HSPB7 specifically does NOT refold. Still a member of the stress-response sHSP family and sequesters aggregates; KEEP as ACCEPT (process-level, stress response) — note it acts via sequestration not refolding.
- Localization terms (cytoplasm, nucleus IBA/IDA/IEA): ACCEPT. Cajal body (IEA): KEEP_AS_NON_CORE. actin cytoskeleton (IEA ortholog): KEEP_AS_NON_CORE (consistent with filamin binding).

## Core functions
1. Small-HSP holdase/sequestrase that binds aggregation-prone clients (and small-HSP partners) without refolding them -> unfolded protein binding (GO:0051082) / heat shock protein binding (GO:0031072).
2. Filamin binding (GO:0031005) - structural/cytoskeletal cardiac role.
</content>
