# sopB (P62558), F plasmid centromere-binding protein, Escherichia coli K-12

## 2026-10-30: initial review

GOA had one row: DNA binding (InterPro IEA).

- sopC binding by purified SopB [PMID:2670941]; SopB-DNA crystal structures [PMID:20236989].
- CTPase measured on the F protein, called ParBF in [PMID:34286695]: CTP-specific, Michaelis-Menten,
  max rate ~14 h-1 rising to ~44 h-1 with sopC DNA; CTP promotes multiple SopB loading.
- Stimulates SopA ATPase via an arginine finger [PMID:19740757; PMID:1406581] -> ATPase activator
  activity (GO:0001671). This is the coupling row the chromosomal ParB reviews could not add,
  because the P. aeruginosa evidence for it is missing.
- sopB missense mutants from an instability screen [PMID:10395819]; cooperative repression of
  sopAB with SopA [PMID:9529520].

Decisions: DNA binding MODIFY -> sequence-specific DNA binding; NEW sequence-specific DNA binding,
CTPase activity, ATPase activator activity, plasmid partitioning (core); negative regulation of
transcription (non-core).
