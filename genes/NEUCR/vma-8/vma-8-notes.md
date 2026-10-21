# vma-8 manual review notes

- `vma-8` / `NCU08035` encodes UniProtKB `O59941`, a reviewed Neurospora
  V-type proton ATPase subunit D record in PANTHER family `PTHR11671` and
  InterPro entry `IPR002699` [file:genes/NEUCR/vma-8/vma-8-uniprot.txt].
- Margolles-Clark, Tenney, Bowman, and Bowman describe the Neurospora vacuolar
  ATPase as the ATP-driven proton pump of the vacuolar membrane and as a large
  multisubunit V-type ATPase whose subunit genes had been characterized
  [PMID:10340846, "The ATP-driven proton pump in the vacuolar membrane is a
  typical V-type ATPase"].
- The PTHR11671 PAINT export supports the key fungal assignments. Treat
  `PANTHER:PTN000912657` as the curated fungal node for
  `GO:0000329 fungal-type vacuole membrane` and
  `GO:0016471 vacuolar proton-transporting V-type ATPase complex`, seeded by
  Saccharomyces VMA8 and, for the complex term, Neurospora O59941. The broader
  `PTN000186829` and `PTN002268884` rows carry vacuolar acidification and
  `contributes_to` rotary proton-transporting ATPase activity, each seeded by
  Saccharomyces VMA8 and O59941
  [file:interpro/panther/PTHR11671/PTHR11671-paint.tsv].
- The only rows that look overstated rather than merely broad are the
  EnsemblFungi `membrane raft` transfer from budding yeast and the automated
  UniProt `enables GO:0046961` row. VMA8 is a peripheral V1 subunit of the
  assembled V-ATPase; the appropriate MF assertion is `contributes_to` the
  holoenzyme's proton-transporting ATPase activity, as in the IDA and IBA rows.
- Bounded PubMed/PMC searches for `Neurospora vma-8`, `O59941`, `subunit D`,
  and the 1999 title did not turn up another vma-8-specific experimental paper
  that would justify a nonredundant `NEW` annotation. Later Neurospora vacuole
  papers mostly use other V-ATPase subunits, especially VMA-1, as markers.
