# DNAH6 notes

## Identity and structure
- UniProt Q9C0G6, 4158 aa.
- IDAg heavy chain (centrin-associated): [PMID:39056782 "DNAH6, the dynein heavy chain of IDAg, is connected with the light intermediate chain of IDAd."]; [PMID:37258679 "the identities of only IDAf (DNAH2 and DNAH10), IDAd (DNAH1) and IDAg (DNAH6) had been confidently deduced on the basis of sequence conservation"].
- Ortholog of Chlamydomonas DHC2 [PMID:26918822 "It is an ortholog of Chlamydomonas DHC2, an inner dynein arm component essential for motile cilia function."].

## Cilia / laterality
- Knockdown: [PMID:26918822 "Functional analysis with gene knockdown in zebrafish embryos and in the human and mouse respiratory epithelia showed DNAH6 is required for left-right patterning and airway ciliary motion, respectively."]; central pair defects; off-target caveat acknowledged by authors.
- Oligogenic heterotaxy with DNAH5/DNAI1 (trans-heterozygous) [PMID:26918822].
- Absent from axonemes in CCDC39/40 PCD [PMID:39056782].

## Sperm
- MMAF: [PMID:31676830], [PMID:37424858], [PMID:37594300 "The absence of inner dynein arms and radial spokes was observed in the sperm of patients with DNAH6 variants."], [PMID:40592014].
- Flagellar localization: [PMID:37594300 "DNAH6 was localized throughout the flagella of normal sperm"].
- Reduced in DNAH3- and DNAH7-deficient sperm [PMID:39503742; PMID:40810911].
- Candidate reports: sperm head anomaly [PMID:29356036]; azoospermia [PMID:28206990] (single families, low confidence).

## Curation decisions
- dynein complex (IBA/IEA) -> MODIFY to inner dynein arm.
- NEW: epithelial cilium movement involved in extracellular fluid movement (IMP PMID:26918822); sperm flagellum assembly (IMP PMID:37594300).
- Light intermediate chain binding kept as non-core; intermediate chain binding UNDECIDED.

## PANTHER / IBA check
- Human Q9C0G6 and mouse E9Q0B6 have identical IBA sets (6 terms incl. dynein complex, but not inner dynein arm / IDA assembly / sperm flagellum assembly, which DNAH3 and DNAH7 get from PTN008503981/PTN008951089). No human/mouse split.

## Deep research
- Falcon deep research failed (Edison API authentication 503 errors on repeated attempts).
