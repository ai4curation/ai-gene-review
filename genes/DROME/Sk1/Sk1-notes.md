# Sk1 review notes

## Session 2026-10-28

- `just fetch-gene DROME Sk1` resolved Q9VYY8 (TrEMBL, unreviewed); 13 GOA rows.
- Literature: only two Sk1 papers (PMID:14722126 abstract-only; PMID:21321100 full text read).
  See `Sk1-deep-research-manual.md`.

### Decisions

- Sphingosine kinase activity (IDA, IBA, IEA): ACCEPT. [PMID:14722126 "Both genes functionally and
  biochemically complement a yeast sphingosine kinase mutant"]
- Cytosol and plasma membrane (IDA, PMID:21321100): ACCEPT; caveat that S2-cell staining was of a
  stably expressed (metallothionein-promoter) construct. Cytoplasm (ARBA IEA) is MODIFY to cytosol.
- Mitochondrial inner membrane (ISS from mouse Sphk2 Q9JIA7): MARK_AS_OVER_ANNOTATED. No fly
  evidence; both fly studies find cytosolic/plasma-membrane Sk1. Mammalian SPHK2's mitochondrial
  pool is not established for the fly enzyme, and fly Sk1 is not a one-to-one SPHK2 ortholog
  (both fly paralogs sit in PTHR12358; orthology not resolved here).
- Endomembrane system (UniProt SubCell from ARBA): MARK_AS_OVER_ANNOTATED. No TM segment; the only
  membrane location seen is plasma membrane, which in GO is not part_of endomembrane system.
- Sphingosine biosynthetic process (IBA): the direction is wrong. Sphingosine kinase consumes
  sphingosine (sk1 nulls accumulate sphingosine and DHS). MODIFY to sphingosine metabolic process
  (GO:0006670, the parent of the IBA term).
- Sphingolipid metabolic process (IDA): correct but general; MODIFY to GO:0006670 sphingosine
  metabolic process and GO:0006669 sphinganine-1-phosphate biosynthetic process (Sk1 makes DHS1P,
  DHS = sphinganine).
- Kinase/transferase activity: MODIFY to sphingosine kinase activity. ATP binding: KEEP_AS_NON_CORE.
- No NEW process terms: the endolysosomal trafficking/photoreceptor phenotypes are downstream of
  the S1P/DHS1P balance and are mutant-phenotype evidence only.
