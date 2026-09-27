# kms1 (S. pombe, P87245) review notes

Context: fungal KASH-side comparator for `modules/linc_complex.yaml`. Human comparators: SYNE1/SYNE2, KASH5.

## Biology (with provenance)

- KASH ONM partner of Sad1 in the meiotic LINC complex [PMID:27889481 "the LINC complex, which comprises the KASH-domain outer NE protein Kms1 and the SUN-domain inner NE protein Sad1"].
- Present at vegetative SPB but dispensable for growth [PMID:10899136 "Kms1p was also present in vegetative cells and localized to the SPB"].
- kms1 blocks telomere clustering, disorganizes meiotic chromosomes, reduces allelic and raises ectopic recombination [PMID:10899136].
- Two-hybrid: Kms1 (202-607) binds dynein light chain Dlc1 [PMID:11907273]; Dlc1 vegetative SPB localization is Kms1-independent.
- Sad1-Kms1 foci at persistent DSBs couple them to microtubules; Kms1 affects repair pathway choice, not essential for repair [PMID:24943839].
- Sequence: no InterPro KASH match; C-terminal hydrophobic segment and short luminal tail (ends ...YELVQPS, not the canonical PPPX); EF-hand pair call (IPR011992) unexplained (deep research also flags this).

## Decisions

- Sad1 protein-binding rows -> MODIFY GO:0140444; Dlc1 row -> MODIFY GO:0045503 dynein light chain binding; Sif1/Ufe1/Hrs1 rows -> REMOVE (uninformative).
- Nuclear membrane (IC) -> MODIFY GO:0005640 nuclear outer membrane.
- GO:0034993, GO:1990612, GO:0045141 (IMP, IGI), SPB rows accepted; iMTOC and DSB attachment to NE kept as non-core.

## Deep research

`kms1-deep-research-falcon.md` read and incorporated (quoted in core function); it cites a 2025/2026 preprint (Laffitte et al.) on LINC and HR that was not used as evidence.

## Module implications

- Kms1 is the fungal analogue of the meiotic KASH5 variant: a KASH protein that couples telomeres (via SUN) to dynein for chromosome movement. Unlike KASH5, no direct dynein-activating-adaptor activity is shown (only Y2H with Dlc1), so GO:0140660 is not supported for Kms1.
- The fission-yeast complex term GO:1990612 is_a GO:0034993; fits a "fungal meiotic LINC" taxon variant.
