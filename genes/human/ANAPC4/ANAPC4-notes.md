# ANAPC4 notes

## 2026-10-04 review (PAINT campaign, affinage provider)

- APC4 is a core platform subunit of the APC/C. "The base of the APC/C comprises the platform subunits of Apc4 and Apc5, together with two domains of Apc1." (PMID:25043029). The catalytic APC2-APC11 module sits at the platform's periphery.
- **Affinage: trust gate tripped.** Affinage's pairwise self-evaluation lost to UniProt. Its narrative is a thyroid-cancer TRMT13 paper and ignores the APC/C. Nothing is used from it.
- **Wrong identifier: GO:0004842 TAS (PINC, 2003).** The row cites PMID:6180011, "Two subgroups of HLA Bw44 defined by cell-mediated lympholysis" (1982). The citation cannot be right. The row is MODIFY to GO:0061630, which should be contributes_to for a non-catalytic subunit. **Candidate for the MISCITATIONS register** (not added in this PR).
- **Nuclear periphery IBA (single SGD donor):** MARK_AS_OVER_ANNOTATED. The yeast Apc4 IDA (PMID:25817432) comes from stress-induced INQ quality-control foci under genotoxic stress, not a constitutive location. propagation_review: PROPAGATION_BAD / CONTEXT_OR_TISSUE_MISMATCH.
- **PTEN protein phosphatase binding IPI (PMID:21241890):** kept as non-core. PTEN promotes APC/C-CDH1 association phosphatase-independently.
- **15 protein-binding IPIs:** removed. Partners are CDC27, CDC20, NEK2 and KIF18A, all APC/C subunits, coactivators or substrates.
- **Meiotic NAS:** kept as non-core; there is no APC4-specific evidence.
- **Other rows:** location, complex, catabolism, chain-type and mitotic-regulation rows are accepted.

## 2026-10-04 core MF update

- **Core MF:** GO:0140378 protein complex scaffold activity ("serves to hold the complex together") added to core_functions alongside contributes_to GO:0061630. This follows the ANAPC16 review (#4058). No NEW GOA row is proposed: no small APC/C subunit carries a scaffold MF in QuickGO, which reads as a convention.
