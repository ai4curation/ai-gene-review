# hemC (P06983) notes, Escherichia coli K-12

## Sources and deep research

- Deep research was not available: the one attempted provider run for this batch
  (`just deep-research ECOLI hemA --provider perplexity`, 2026-11-10) failed with a missing
  template error ("All providers failed"). No deep-research file exists; this review uses
  the UniProt record and cached abstracts (PMID:3052434, PMID:379277, PMID:15911532 are
  abstract-only; PMID:18304323 has full text but HemC is not named in the cached text).

## Function

- Porphobilinogen deaminase (hydroxymethylbilane synthase) purified and crystallized
  [PMID:3052434 "The substrate, porphobilinogen, binds to the active-site dipyrromethane
  cofactor to form three intermediate complexes: ES, ES2 and ES3."].
- Dipyrromethane cofactor on Cys242 (UniProt FT MOD_RES); monomer (UniProt CC SUBUNIT,
  PMID:3529035, not cached).
- PBG-accumulating, heme-deficient hemC mutants [PMID:379277 "Extracts had one-tenth of the
  parental activity of the enzyme porphobilinogen deaminase."].

## Verdict notes

- GO:0004418 (IBA, IDA, IEA, IMP) ACCEPT core; GO:0006783 (IBA, IEA, IMP) ACCEPT.
- GO:0033014 (IEA, IMP) ACCEPT. The P. putida review (genes/PSEPK/hemC) modified this to
  GO:0006780 uroporphyrinogen III biosynthetic process. Comparator check (QuickGO,
  2026-11-10): human HMBS P08397 and ALAD P13716 carry GO:0006783 and GO:0033014 but not
  GO:0006780, whereas UROS P10746 carries GO:0006780 by IBA/IDA/IEA, so GO:0006780 is used
  for the cyclization (HemD) step. GO:0006780 is not proposed for HemC.
- Cytoplasm rows (IBA, IDA, ARBA IEA): MODIFY to GO:0005829 cytosol, which the gene carries
  by IDA (two fractionation proteomics studies). Cytosol rows ACCEPT.
