# velB (Aspergillus nidulans) — curation notes

UniProt C8VTS4 (VELB_EMENI). Velvet-family regulator; hub of two complexes.
Member of the `conidiation_regulatory_cascade` module (velvet maturation tier).

- VelB-VeA-LaeA (dark) velvet complex promotes sexual development + secondary
  metabolism; VosA-VelB controls spore maturation/trehalose. [PMID:18556559 "We identified the heterotrimeric velvet complex VelB/VeA/LaeA connecting light-responding developmental regulation and control of secondary metabolism"].
- NF-kB-like DNA-binding regulator [PMID:24391470]; positively regulates sexual
  sporulation and ST biosynthesis, negatively regulates conidiation.
- GO:0045461 (sterigmatocystin biosynthetic process) marked over-annotation (VelB
  is a regulator; use GO:0010914). Trehalose/light roles kept non-core.
- Core MF GO:0003700 proposed (not yet in GOA).

## 2026-10-01 re-review (GOA refresh)

- No new or vanished GOA rows.
- Protein binding IPI (PMID:24391470) changed KEEP_AS_NON_CORE -> MODIFY to GO:0046982 protein
  heterodimerization activity: the paper solves the VosA-VelB velvet-domain heterodimer structure.
- Core MF changed from GO:0003700 (asserted directly) to molecular_function GO:0046982 plus
  contributes_to GO:0003700: in EMSA "VelB alone at least does not bind the brlA promoter"
  [PMID:24391470], whereas the VosA-VelB heterodimer does. Description adjusted accordingly.
- Added supporting text to the nucleus/cytoplasm IDA rows from PMID:21152013.
