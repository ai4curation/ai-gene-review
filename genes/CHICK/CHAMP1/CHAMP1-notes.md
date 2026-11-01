# CHAMP1 (chicken) review notes

## 2026-10-28 session

- Fetched with `just fetch-gene CHICK CHAMP1`; accession A0A8V0YM97 confirmed (GeneID 418733),
  GOA keyed to it (10 IEA rows: 7 Ensembl Compara GO_REF:0000107 from human Q96JM3, 3
  combined GO_REF:0000120).
- No chicken functional studies. The only chicken datum: ZNF828 (CHAMP1) enriched on H3K9me3
  peptides in chicken/zebra finch extracts [PMID:26703087 "we found ZNF462, ZNF828 and POGZ
  enriched at H3K9me3"].
- Human mitotic function: [PMID:21063390 "CAMP localizes to chromosomes and the spindle
  including kinetochores"]; [PMID:21063390 "CAMP is required for maintaining
  kinetochore-microtubule attachment during bi-orientation"]. Full text not accessible to me
  (cache abstract-only; PMC tool returned no body).
- REV7 binding: [PMID:28887307] WK motif W334/K335/P341; chicken central repeat region is
  diverged (own analysis, CHAMP1-bioinformatics/RESULTS.md), so REV7 binding / MAD2L2
  spindle targeting in chicken is not assumed. GO:0035372 row -> UNDECIDED.
- Heterochromatin complex: [PMID:39962076 "is enriched in heterochromatin"]; chicken
  H3K9me3 pull-down is consistent. No NEW heterochromatin CC row added: a peptide pull-down
  is not a localization assay and the human data are not chicken evidence (kept in
  core_functions description/suggested questions instead).
- PMID:22448145 (workflow-designated "key paper") is a MARS2/ARSAL paper with no CHAMP1
  content; not used.
- Decisions: CC kinetochore/spindle/condensed chromosome/nucleus/nucleoplasm ACCEPT; nuclear
  body KEEP_AS_NON_CORE; BP attachment + biorientation ACCEPT; protein localization to
  kinetochore KEEP_AS_NON_CORE (downstream effect on CENP-E/F); protein localization to
  microtubule UNDECIDED.
