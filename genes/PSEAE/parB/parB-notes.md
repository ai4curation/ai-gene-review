# parB (PA5562, spoOJ, Q9HT12), Pseudomonas aeruginosa PAO1

## 2026-10-23: initial review

UniProt gene name "spoOJ" (with a letter O) is the PAO1 submitter name; the literature uses parB.

**Experimental evidence.**
- Purified ParB binds parS; C-terminal 56 aa dimerization domain; ParA interaction; parS-dependent
  silencing of nearby genes on overproduction [PMID:15466051].
- parB deletions: anucleate cells, growth and motility defects, irregular foci [PMID:19332810].
- Spreading-deficient but DNA-binding-competent alleles phenocopy the null; source of the IPI
  self-interaction annotation [PMID:21531806 "indicating that the ability to spread is vital for
  ParB function in the cell"].
- C-terminal leucine-zipper-like residues L282, V285, I289 are needed for dimerization and every
  function [PMID:22322962 "Thus so far all the properties of ParB seem to depend on
  dimerization."].
- Ten parS sites; any one of parS1-4 is necessary and sufficient [PMID:25794281]. ParB binds
  parS1-4 in vivo, and parS is the first locus separated after replication [PMID:27820816].
- ParB is a nucleoid-associated protein binding hundreds of half-parS sites [PMID:29648658], with
  occupancy shifting to half-parS on entry into stationary phase [PMID:37569892].
- Direct repression of genes adjacent to parS3/parS4 [PMID:28732084].
- The N-terminal motif of ParB binds ParA; other partners include NdpA, MinE, CTP synthetase and
  FleN [PMID:36622167, abstract only].
- **CTPase**: purified ParB hydrolyses CTP with KM 44 uM, stimulated fully by parS and partly by
  non-specific DNA; a sterigmatocystin derivative inhibits it [PMID:38843873].
- ParB is synthetically lethal with the condensins SMC and MksB [PMID:32907947 "synthetically
  lethal with ParB"].

**GOA rows.** DNA binding → MODIFY to sequence-specific DNA binding. Chromosome and chromosome
segregation → ACCEPT. Identical protein binding → MODIFY to protein homodimerization activity.
Regulation of transcription → MODIFY to negative regulation (non-core). DNA-templated
transcription → REMOVE. Positive regulation of sporulation (IBA, B. subtilis donor) → REMOVE.
NEW: CTPase activity (IDA), sequence-specific DNA binding (IDA).

The transcription rows come from UniRule UR000413841. This entry, unlike the P. putida
ortholog, has a PROSITE HTH_CROC1 (PS50943) / IPR001387 match, which may explain why only the
P. aeruginosa protein gets transcription terms.
