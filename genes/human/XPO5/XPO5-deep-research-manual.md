# XPO5 manual synthesis

XPO5/exportin-5 is the structured-RNA export branch of the PTHR11223 human pair. It binds RanGTP and structured RNAs in the nucleus, crosses the nuclear pore, and releases cargo on the cytoplasmic side after RanGTP hydrolysis.

Core function: XPO5 is a RanGTP-dependent export receptor that binds structured RNA cargos, especially pre-miRNAs, in nuclear export complexes and moves them from nucleus to cytoplasm.

XPO5 binds pre-miRNA directly as an XPO5:RanGTP complex; PMID:14681208 and PMID:21297638 support pre-miRNA binding and export, and PMID:19965479 structurally describes the pre-miRNA:Exp5:RanGTP export machinery.

XPO5 can also export aminoacyl-tRNA, Dicer mRNA, dsRNA-binding proteins and SNAG-containing proteins, so those tRNA, mRNA and protein-export annotations are supported secondary cargo classes rather than the core pre-miRNA export function.

PMID:11777942 identified XPO5 as a karyopherin that binds RanGTP and exports dsRNA-binding proteins. PMID:12426392 showed aminoacyl-tRNA-linked eEF1A export, PMID:21297638 showed direct Dicer mRNA binding/export, and PMID:24209753 added SNAG-containing proteins exported through the Exportin-5-aminoacyl-tRNA complex.

The RISC rows from PMID:19965479 were removed because that paper concerns the pre-miRNA:Exp5:RanGTP nuclear export machinery, not a mature Argonaute-containing RISC complex or RISC binding by XPO5.

XPO5 shuttles between nucleus and cytoplasm as part of the RanGTP export cycle; its active cargo-binding step is nuclear and its cargo-release step occurs on the cytoplasmic side.

Rows that assert only GO:0005515 protein binding were removed under the bare-protein-binding policy because they do not name a cargo-specific XPO5 molecular function.
