# SK notes

## 2026-10-26 initial review
- fetch-gene resolved Q7KVW5 (KCNN_DROME). 19 GOA rows.
- Read full text of PMID:21957252 and PMID:22509342; abstracts of PMID:24671529, PMID:31350259.
- Key decision: REMOVE IDA GO:0009881 photoreceptor activity. dSK is a K+ channel acting
  in photoreceptor cells; the paper shows light-induced currents are normal in mutants
  [PMID:21957252 "This was supported by their normal somatic light-induced currents and high dSK expression in the lamina circuits."].
  The cell-level role is captured by GO:0016057.
- Generic terms refined: membrane -> plasma membrane; potassium ion transport -> K+
  transmembrane transport; Ca-activated K channel -> small conductance; neuron projection -> axon.
- No NEW process terms: memory and NMJ phenotypes are downstream of excitability; considered
  but not added (e.g. regulation of postsynaptic membrane potential) to stay conservative.
