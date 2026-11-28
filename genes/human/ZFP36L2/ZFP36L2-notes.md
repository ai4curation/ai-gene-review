# ZFP36L2 notes

Deep research could not be generated in this environment: `just deep-research human ZFP36L2 --provider perplexity` failed because the installed client exposed only the `claude_code` provider. No provider-branded deep-research file was written; this note is the manual fallback.

ZFP36L2/BRF2/TIS11D is the third reviewed human TTP-family mRNA decay activator in PANTHER family `PTHR12547`. It has the same tandem CCCH RNA-binding domain as ZFP36 and ZFP36L1 and is placed in the PAINT TTP-like node `PTN002648882` for cytosol, AU-rich-element binding, protein-RNA adaptor activity, and poly(A)-tail shortening [PTHR12547-paint.tsv, "PTHR12547	PTN002648882	GO:0035925	F	IBD	false"].

Direct human ZFP36L2 evidence is concentrated in LDLR and early-embryo maternal-mRNA decay. Adachi et al. showed that ZFP36L2 and ZFP36L1 specifically bind the LDLR 3'-UTR, recruit CCR4-NOT, and destabilize LDLR mRNA [PMID:25106868, "ZFP36L1 and ZFP36L2 specifically bind to the 3'-UTR of LDLR mRNA and recruit the CCR4-NOT-deadenylase complex"]. Zheng et al. found biallelic human ZFP36L2 variants in recurrent preimplantation embryo arrest and showed that the recurrent p.Ser308_Ser310del variant prevented maternal mRNA decay [PMID:34611029, "the recurrent variant (p.Ser308_Ser310del) prevented maternal mRNA decay in zygotes and HeLa cells"].

The mouse orthology rows for hematopoiesis, B-cell and T-cell development, cell-cycle control, adipocyte differentiation, and stem-cell maintenance describe real developmental contexts for Zfp36l2, especially together with Zfp36l1. They are kept as non-core because the direct molecular role remains binding ARE-containing transcripts and acting as a sequence-specific adaptor for the decay machinery. Stimulus rows from generic growth-factor or cytokine induction are marked as over-annotations.

The `GO:0000900` mRNA regulatory element binding translation repressor activity PAINT row on the shared `PTN002648882` node is kept as a non-core translational-silencing output. Human ZFP36L2 lacks the direct BRF1/TTP P-body evidence, but the row is consistent with the eumetazoan placement and the conserved ZFP36-family AU-rich mRNA decay mechanism.
