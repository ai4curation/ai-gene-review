# ARMC10 (SVH) review notes

## Sources
- Affinage: trust gates clear. Checked against the cached papers:
  - PMID:30631047: AMPK S45, fission; full text, HEK293A/U2OS.
  - PMID:24722288: mitochondrial trafficking; co-IP with Miro1/2 and Trak2, but not KIF5; full text.
  - PMID:37556559: oncomodulin receptor; abstract only.
  - PMID:12839973 and PMID:17904127: ER splice variants and p53; abstracts.
- IBA donors were resolved via UniProt:
  - MGI:1914666 = Armcx2; MGI:1918953 = Armcx3; MGI:1925498 = Armcx1; MGI:2147993 = Armcx6.
  - The axonal-transport IBA is seeded by Armcx3 alone.
  - Mouse Armc10 itself is MGI:1914461 (Q9D0L7).

## Decisions
- ACCEPT:
  - Mitochondrion (IBA, IEA, IDA, HTP) and mitochondrial outer membrane (IEA, EXP).
  - Axonal transport of mitochondrion (IBA): ARMC10's own trafficking evidence supports the transfer from Armcx3.
- KEEP_AS_NON_CORE:
  - ER membrane and ER (2003 overexpression of splice variants).
  - Axon cytoplasm (IEA derived from the process row).
- NEW:
  - Positive regulation of mitochondrial fission (IDA, PMID:30631047).
  - Signaling receptor activity (ISO from mouse, PMID:37556559). The topology question is raised in suggested_questions.
- p53 binding (SVH-B) was not added as NEW: a single abstract-only study not linked to the main functions. It is raised as a suggested question.

## Review round 1 (PR #4185)
- Corrected the trafficking-complex claim: in PMID:24722288, Armc10 co-immunoprecipitates with Miro1/2 and Trak2, but not with KIF5A/B/C.
- Fission NEW row:
  - Now IMP: overexpression, plus CRISPR KO with AMPK activation.
  - It now records the opposite neuronal result: overexpression gives slightly larger mitochondria and protects against Abeta fragmentation.
- NEW nucleus (ISO from mouse Armc10): bimodal nuclear and mitochondrial staining in neurons (PMID:24722288).
