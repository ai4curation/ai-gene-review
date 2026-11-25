# mcrA (A0A284VQI9) — Ca. Methanoperedens nitratireducens (ANME-2d) MCR alpha

Part of the cross-clade MCR review (`projects/ARCHAEA/mcrA-across-clades.md`);
anaerobic methanotroph representative. Folder `mcrA__A0A284VQI9` because two
9EURY entries in this set share the symbol mcrA.

## Choice of entry

- ANME-1 (Ca. Methanophagales) has no full-length McrA in UniProt; the RCSB mapping of
  the ANME-1 structure (PDB 3SQG) points to K4Q4L0, a 162-residue environmental fragment.
- A0A284VQI9 is a full-length (567 aa) ANME-2d McrA, taxon 1392998, which UniProt lists
  with the Haroon et al. 2013 names (Ca. M. nitroreducens / nitratireducens) and strain
  BLZ1 as synonyms.
- The structurally characterized ANME-2d MCR (strain BLZ2, RefSeq WP_097300250.1) maps
  only to deleted UniProt entries. BLZ2 McrA vs A0A284VQI9: 89.7% identity over aligned
  positions (`projects/ARCHAEA/mcrA-across-clades/compare_anme2d_strains.py`, run
  2026-11-13).

## Literature search

No deep-research provider key is configured (checked 2026-11-13). PubMed searched for
"Methanoperedens methyl-coenzyme M reductase" and the ANME MCR structure papers.

## Evidence

- ANME-2d oxidizes methane by reverse methanogenesis with nitrate [PMID:23892779
  "ANME-2d is capable of independent AOM through reverse methanogenesis using nitrate
  as the terminal electron acceptor."].
- ANME-2d MCR structures resemble methanogenic Methanosarcinales MCR [PMID:40913044
  "these ANMEs have extremely conserved MCR structures, similar to homologs from
  methanogenic Methanosarcinales"]; a Gln next to the CoM tyrosine is Met in ANME-2d.
  Our comparison confirms Met347 at P11558 Gln332 in this sequence.
- Methanogenic MCR runs the reverse reaction [PMID:20520712].

## Review decisions (2026-11-13)

- GO:0050524 IEA: ACCEPT (reversible reaction).
- GO:0015948 methanogenesis IEA: MODIFY -> GO:0046188 methane catabolic process
  (direction correction); InterPro source defect filed (taxon-scope problem).
- NEW (ISS, PMID:40913044): GO:0044674 complex, GO:0046906 tetrapyrrole binding.
- UniProt ARBA physiological direction (left-to-right) flagged as a source defect.
