# XPO1 review notes

PTHR11223 is heterogeneous: the human family contains XPO1 in the exportin-1 subfamily and XPO5 in the exportin-5 subfamily, so XPO1 protein-cargo specificity was not projected onto XPO5 solely through the combined family.

XPO1 had 134 GOA rows and 132 seeded YAML entries. The missing entries were exact GOA duplicates for `GO:0005515` with PMID:21378169 and for `GO:0005049` with PMID:12773398; the final review intentionally carries both duplicate pairs so that one `existing_annotations` entry is present for each GOA row.

Most XPO1 annotations collapse onto three conclusions: accept the RanGTP-dependent NES export receptor activity and protein export rows as core; keep ribosomal subunit export, selected mRNA/RNP export, nucleolar/Cajal body localization and generic complex membership as direct but cargo-specific or peripheral; remove only bare `GO:0005515` rows and over-specific rat electronic response terms.
