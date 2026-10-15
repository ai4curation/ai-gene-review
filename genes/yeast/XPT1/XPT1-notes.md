# XPT1 (YJR133W, UniProt P47165) notes

## Function
- "A new Saccharomyces cerevisiae gene, XPT1, was isolated as a multicopy suppressor of a hypoxanthine phosphoribosyl transferase (HPRT) defect." [PMID:10217799]
- "Disruption of XPT1 affects xanthine utilization in vivo and results in a severe reduction of xanthine phosphoribosyl transferase (XPRT) activity while HPRT is unaffected." [PMID:10217799]
- UniProt is cautious: activity "unclear in vivo" [UniProt:P47165]; no purified-enzyme study.
- "Inosine recycling into the AXP pool was facilitated by purine nucleoside phosphorylase, Pnp1, and joint action of the phosphoribosyltransferases, Hpt1 and Xpt1." [PMID:20087341]
- Low abundance (721 molecules/cell) [UniProt:P47165]; cytoplasm (HDA).

## Pathway
- XANPRIBOSYLTRAN-RXN in PWY3O-1, PWY3O-285, PWY3O-743; correct.
- Paralog of HPT1 (PANTHER PTHR43363 SF4 vs SF1); IBA node PTN001262736 shares HPRT/GMP/IMP salvage terms across both.

## Decisions
- Core MF GO:0000310; BP GO:0032265 XMP salvage; cytoplasm.
- KEEP_AS_NON_CORE HPRT activity (IBA/ARBA/IGI), IMP/GMP salvage IBA, hypoxanthine metabolic process (dosage-dependent secondary activity).
