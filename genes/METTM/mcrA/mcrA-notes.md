# mcrA (P11558, MCRA_METTM) — Methanothermobacter marburgensis MCR I alpha

Part of the cross-clade MCR review (see `projects/ARCHAEA/mcrA-across-clades.md`).
This is the reference enzyme for the set: every other mcrA review aligns to it.

## Literature search

Automated deep research was not run: no deep-research provider key is configured in
this environment (checked 2026-11-13). These notes are hand-written from the GOA-cited
papers and from PubMed searches for the structure, mechanism and reverse-reaction
papers (queries recorded in the project page).

## Organism

- Formerly *Methanobacterium thermoautotrophicum* strain Marburg; grows on H2/CO2
  [PMID:2269306 "which grow on H2 and CO2 as energy source"].
- Two isoenzymes, MCR I (mcr) and MCR II (mrt); MCR I dominates under gas limitation
  [PMID:2269306 "When growth was limited by the gas supply, MCR I predominated."].

## Function

- Purified enzyme reduces methyl-CoM with coenzyme B to methane and heterodisulfide,
  specific for coenzyme B [PMID:3350018 "Methyl-CoM reductase was specific for H-S-HTP
  as electron donor."].
- Ordered ternary-complex mechanism, methyl-SCoM binds first [PMID:25691570 "only one
  binary complex (MCR·methyl-SCoM) is productive"].
- Requires Ni(I); 3-NOP oxidizes Ni(I) and inactivates the enzyme [PMID:27140643 "With
  purified MCR, we found that 3-NOP indeed inactivates MCR at micromolar concentrations
  by oxidation of its active site Ni(I)."].
- Purified enzyme also runs the reverse, methane-activating reaction [PMID:20520712
  "purified MCR from Methanothermobacter marburgensis converts methane into
  methyl-coenzyme M under equilibrium conditions"]. GO:0050524 is written as a
  reversible reaction, so this needs no separate MF; it is not a process of this
  organism.
- Structure: alpha2beta2gamma2, two F430 between alpha, alpha', beta, gamma
  [PMID:9367957 "forming two identical active sites"].
- Location: cytoplasm by immunogold; facultative membrane proximity under Ni limitation
  [PMID:23533332 "MCR of Methanothermobacter marburgensis was located at the cytoplasmic
  membrane under nickel-depleted growth conditions."].

## Review decisions (2026-11-13)

- 4 EXP + 1 IDA GO:0050524 rows: ACCEPT. PMID:2448287 (cloning paper) is abstract-only
  and shows no assay; accepted in deference to the curator, reference marked UNVERIFIED.
- GO:0015948 methanogenesis -> MODIFY GO:0019386 (as for O27232).
- NEW: GO:0044674 MCR complex (IDA, PMID:9367957); GO:0046906 tetrapyrrole binding
  (IDA, PMID:9367957), plus proposed term "coenzyme F430 binding".

## Added UniProt-cited papers (2026-11-13, PR #6335)

Fetched the six UniProt references not previously cached and added them to the review:
- PMID:9030728: Ni(I) activation of purified MCR I (strain Marburg); specific activity
  2 -> ~100 U/mg on reduction [PMID:9030728 "methyl-coenzyme-M reductase is activated when
  the enzyme-bound coenzyme F430 is reduced to the Ni(I) oxidation state"]. Added to the
  activity IEA row and the tetrapyrrole binding row.
- PMID:10660523: methyl groups of the modified residues come from SAM. Description only.
- PMID:11491299: 1.16 A structure with exact F430 geometry. Tetrapyrrole binding row.
- PMID:20707311 (full text): methyl-SCoM binds before CoB; added to the ordered-mechanism row.
- PMID:21438550 (full text): Ni-methyl intermediate structure. Reference only.
- PMID:20802048: genome; "chemolithoautotrophic". Added to the methanogenesis MODIFY.
Full text for PMID:2448287 (the IDA activity row) is still unavailable: PMC210692 refuses
automated download (403) and the open-access warming chain found nothing for any of the
abstract-only P11558 papers.

## PMID:2448287 full text read (2026-11-13)

Read all ten pages from a reviewer-supplied PDF (J Bacteriol 170:568-577; PMC210692
scan). Not cached in publications/: not openly licensed. Contents: cloning of the mcr
cluster of strain Marburg in lambda gt11/EMBL4, expression of subclones in E. coli with
Western-blot detection (Fig. 2), sequence of the beta-ORF1-ORF2-gamma-alpha cluster
(Fig. 3), S1/primer-extension mapping of transcript ends, Northern blot. No activity
assay anywhere; MCR activity appears only as introductory background with citations to
other papers. Discussion: the E. coli-expressed alpha subunit was unstable, possibly
because F430 was missing. Outcome: the IDA GO:0050524 row (assigned_by MENGO, 2013) is
miscited; claim kept as ACCEPT (four EXP rows), reference MISCITED, source defect
WRONG_REFERENCE / DELETE_ROW filed (resource OTHER, naming MENGO).
The August 1988 erratum (J Bacteriol 170(8):3792, listed on the PubMed record) has no
PubMed entry of its own and could not be obtained; it was not checked.
