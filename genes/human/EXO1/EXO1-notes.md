# EXO1 (human, Q9UQ84) review notes

## Literature search (no deep-research provider available in this environment)

Sources checked:
- All 20 GOA-cited publications cached via `just fetch-gene-pmids human EXO1`
  (most are abstract-only in the cache; full text for PMID:26240375, PMID:26807646,
  PMID:27918544, PMID:34552057).
- Local publication cache searched for titles mentioning EXO1 / exonuclease 1 / EXOI:
  found PMID:21325134 (human resection reconstitution) in addition to GOA papers;
  PMID:22002605 and PMID:34520455 are yeast and were not used.
- Fetched PMID:28216226 (NBS1 phosphorylation and telomere repair choice; context for the telomere end-joining pathway-choice module proposed in ai4curation/ai-gene-review#5904, not used as evidence).
- Two speculative fetches (PMID:22325778, PMID:21496894) resolved to unrelated papers
  and were not used.

## Findings

- Biochemistry: 5'->3' exonuclease on ds and ssDNA plus 5'-flap endonuclease, Mg2+
  dependent [PMID:10608837 "exhibits both a robust 5' to 3' exonuclease activity on single- and double-stranded DNA substrates as well as a flap structure-specific endonuclease activity"].
  Preferred substrates are blunt / 5'-recessed duplexes [PMID:10608837 "2.5-7-fold higher on blunt end and 5'-recessed double-stranded DNA substrates"].
  Catalytic residues D78, D173, D225 [PMID:11842105 "amino acids D78, D173 and D225 are critical for Exo1 nuclease function"].
  RNase H activity reported [PMID:10364235 "also shows an RNase H activity"].
- Mismatch repair: required for 5'- and 3'-directed excision [PMID:11809771], MutSalpha
  activates and confers processivity [PMID:14636568 "MutSalpha confers high processivity on EXOI"];
  reconstituted with MutSalpha, RPA (5') or also MutLalpha, PCNA, RFC (3') [PMID:15225546].
- Interactions: MSH2 [PMID:9788596], MLH1, MSH3 [PMID:11427529], PCNA [PMID:15225546], RECQ1 [PMID:15886194], CtIP [PMID:21052091], ZGRF1 [PMID:34552057].
- HR end resection: EXO1-BLM-RPA-MRN is one of two long-range resection machineries
  [PMID:21325134 "EXO1 resects the DNA and is stimulated by BLM, MRN, and RPA"]; CtIP/MRN
  recruit EXO1 to DSBs [PMID:21052091]; ATM phosphorylation of EXO1 (via MRE11 phospho) limits the
  extent of resection after IR [PMID:26240375].
- Telomeres: dephospho-NBS1 recruits EXO1 to POT1-TPP1-deficient telomeres; fusions need
  EXO1 [PMID:28216226 "formation of end-to-end chromosomal fusions requires EXO1 and ATR, but not CTIP"].
- T-circle TAS (PMID:27918544): the paper attributes T-circles to Nbs1 and XRCC3; EXO1
  depletion had no effect on C-circles; "Exo1" used as a 3'-5' reagent is E. coli ExoI.
  No support for EXO1 in t-circle formation.
- Replication-fork resection IMP (PMID:26240375): paper studies IR-induced DSB resection
  in G2 cells, not replication forks; better captured as DSB processing.
- PMID:2414623 (protein binding, MLH1) resolves to a 1985 German paper on ulcer disease:
  wrong identifier in the UniProt-assigned GOA row.
