# ffh (E. coli K-12) review notes

## 2026-11-02

Reviewed as an experimentally characterized exemplar for the bacterial SRP
cotranslational targeting module. No deep-research provider run was made for
this gene in this session (no provider credentials available); the review rests
on the Swiss-Prot record and the cached publications cited by GOA. All seeded
GOA rows were reviewed against the cached abstracts or full texts.

Key evidence:

- Ffh and 4.5S RNA form a ribonucleoprotein resembling mammalian SRP
  [PMID:1701272, "An antiserum to Ffh precipitated 4.5S RNA from E. coli
  extracts, implying that the two molecules reside in a complex"].
- The particle recognizes signal sequences on nascent chains [PMID:1279430,
  "Here we show that the P48/4.5S RNA ribonucleoprotein complex interacts
  specifically with the signal sequence of a nascent secretory protein and
  therefore is a signal recognition particle."].
- Ffh is required for protein export [PMID:1331806, "Results of depletion
  experiments indicate that Ffh is important in protein translocation"].
- Ffh is a GTPase needed in vivo [PMID:7612669, "These results demonstrate that
  the GTPase activity of the Ffh protein is required for proper function of the
  protein in vivo"], reciprocally activated with FtsY [PMID:11735405, "both Ffh
  and FtsY act as GTPase activating proteins for one another"].
- SRP also binds the heat-shock sigma factor [PMID:24358019, "We show that SRP
  preferentially binds to WTσ32 compared to a mutant σ32 with a defective
  homeostatic control region"].

## 2026-11-03

PR #5924 review: the signal-sequence rows (GO:0005048, GO:0006617) now cite
PMID:1279430 as IDA. The PMID:1331806 sentence on signal-sequence binding is
background in that abstract, not its result. The sigma32 IPI row is refined to
GO:0008134 transcription factor binding, matching the partner-specific treatment
of the FtsY IPI rows. The ribosomal protein L23 contact in the description is
sourced from the Swiss-Prot SUBUNIT statement (file:ECOLI/ffh/ffh-uniprot.txt,
"Interacts with the ribosomes, via ribosomal protein L23.").
