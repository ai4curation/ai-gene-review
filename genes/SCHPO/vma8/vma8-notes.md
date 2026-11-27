# vma8 manual notes

## Sources checked

- UniProtKB O59823 is a reviewed S. pombe V-type proton ATPase subunit D record. Its curated function note describes Vma8 as a subunit of the V1 complex of vacuolar V-ATPase, with peripheral V1 hydrolyzing ATP and integral V0 translocating protons. It also records the protein at the vacuole membrane and classifies it in InterPro:IPR002699 and PANTHER:PTHR11671.
- Matsuyama et al. 2006 [PMID:16823372] generated the ORFeome C-terminal YFP localization resource used for the three direct PomBase HDA localization rows. The cached file has only the abstract, so it establishes the global screen but not the vma8-specific supplemental entries.
- PTHR11671 is the PAINT family for V-type ATPase subunit D. In `PTHR11671-paint.tsv`, fungal node `PANTHER:PTN000912657` carries IBD annotations to `GO:0000329` and `GO:0016471`; `PTN000186829` carries vacuolar acidification; `PTN002268884` carries proton-transporting ATPase activity, rotational mechanism. Per PAINT, these nodes are curated phylogenetic assertions and not pairwise transfers from the listed seed proteins.

## Review decisions

- Retain V1-domain and vacuolar V-ATPase complex membership as the central cellular-component assertions for vma8.
- Retain `contributes_to GO:0046961`, `GO:0007035`, and `GO:1902600`: Vma8 contributes to ATP-driven proton transport through the V-ATPase complex and thereby to vacuolar acidification.
- Treat broad `GO:0005774` vacuolar membrane as `TOO_GENERAL` because `GO:0000329` fungal-type vacuole membrane is the informative supported term in this fungal review.
- Accept the InterPro `GO:0046961` term while recording its `enables` qualifier as over-strong, and treat the IC `GO:0016887` row as too general beside the more specific rotary proton-pumping ATPase activity. Subunit D is not the independent ATP-hydrolytic motor; it contributes with subunit F to the central rotor stalk of the V-ATPase complex.
- Keep cytosol as a non-core localization because reversible V1-V0 dissociation can produce a soluble V1 pool, and mark the cell division site HDA `is_active_in` call as over-annotated because the abstract-only cached localization paper does not establish that Vma8 executes proton-pump activity at the division site. Vma8's established proton-pump role is at the vacuolar V-ATPase.

No nonredundant NEW rows are needed. The generic `GO:0033176` V-type ATPase complex node in the PAINT export is an ancestor of the more precise accepted vacuolar V-ATPase complex term.
