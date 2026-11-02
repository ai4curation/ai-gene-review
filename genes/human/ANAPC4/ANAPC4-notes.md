# ANAPC4 notes

## 2026-10-04 review (PAINT campaign, affinage provider)

- APC4 is a core platform subunit of the APC/C. "The base of the APC/C comprises the platform subunits of Apc4 and Apc5, together with two domains of Apc1." (PMID:25043029). The catalytic APC2-APC11 module sits at the platform's periphery.
- **Affinage: trust gate tripped.** Affinage's pairwise self-evaluation lost to UniProt. Its narrative is a thyroid-cancer TRMT13 paper and ignores the APC/C. Nothing is used from it.
- **Wrong identifier: GO:0004842 TAS (PINC, 2003).** The row cites PMID:6180011, "Two subgroups of HLA Bw44 defined by cell-mediated lympholysis" (1982). The citation cannot be right. The row is MODIFY, to GO:0160072 since round 2 (originally GO:0061630). The WRONG_IDENTIFIER reference_review is what records it: projects/MISCITATIONS.md is generated from those blocks, so nothing else is needed.
- **Nuclear periphery IBA (single SGD donor):** MARK_AS_OVER_ANNOTATED. The yeast Apc4 IDA (PMID:25817432) comes from stress-induced INQ quality-control foci under genotoxic stress, not a constitutive location. propagation_review: PROPAGATION_BAD / CONTEXT_OR_TISSUE_MISMATCH.
- **PTEN protein phosphatase binding IPI (PMID:21241890):** kept as non-core. PTEN promotes APC/C-CDH1 association phosphatase-independently.
- **15 protein-binding IPIs:** removed. Partners are CDC27, CDC20, NEK2 and KIF18A, all APC/C subunits, coactivators or substrates.
- **Meiotic NAS:** kept as non-core; there is no APC4-specific evidence.
- **Other rows:** location, complex, catabolism, chain-type and mitotic-regulation rows are accepted.

## 2026-10-04 core MF update

- **Core MF:** GO:0140378 protein complex scaffold activity ("serves to hold the complex together") added to core_functions alongside contributes_to GO:0061630. This follows the ANAPC16 review (#4058). No NEW GOA row is proposed: no small APC/C subunit carries a scaffold MF in QuickGO, which reads as a convention.

## 2026-10-04 round 2 (reviewer comments on #4059)

- **The GO:0004842 MODIFY target is now GO:0160072** ubiquitin ligase complex scaffold activity (was GO:0061630). The core MF is also GO:0160072, replacing the GO:0140378 added earlier today.
  - This follows the repo convention for APC/C scaffold subunits: APC1/nuc2 in the same platform, cut9, CDC27, CDC16 and ANAPC2.
  - My earlier claim that contributes_to GO:0061630 was "the convention" for non-catalytic subunits was wrong: in GOA, only the catalytic module carries ligase MFs.
- **Protein-binding REMOVE reasons:** they no longer claim "no informative MF term describes it". They now explain that a proteome-scale co-purification does not show the direct contact GO:0160072 needs.
- **Miscitation:** the WRONG_IDENTIFIER reference_review is the complete action, since MISCITATIONS.md is generated from it. I corrected the earlier "not added" wording above.
- **Core locations added.**

## 2026-10-04 round 3 (reviewer comments on #4059)

- **Correction:** my round-2 reason and notes cited "APC1/nuc2 in the same platform" as a GO:0160072 precedent. That is wrong: S. pombe nuc2 is APC3, a TPR subunit, and APC1 (cut4) has no review here. Every current GO:0160072 holder among APC/C subunits is a TPR subunit or the cullin. APC4 (with APC5) is the first platform subunit to carry it, an extension the reason now states as such.
- **Evidence:** GO:0160072 is now grounded on APC4 itself. PMID:27120157 says the APC1-APC4-APC5 platform shifts on activation to move the catalytic module for E2 access. The PMID:27601667 sentence naming APC4 among the platform subunits is added.
- **Locations:** removed the redundant nucleus from core locations; nucleoplasm, its child, is kept.
