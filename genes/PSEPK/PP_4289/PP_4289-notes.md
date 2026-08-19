# PP_4289 curation notes

## 2026-08-19

- Q88F11 has the defining full-length PuuD architecture: COG3748,
  IPR010389/PF06181, eight predicted transmembrane helices, a C-terminal
  cytochrome c-like domain, and the CXXCH heme-binding motif
  [file:PSEPK/PP_4289/PP_4289-uniprot.txt "eggNOG; COG3748; Bacteria";
  "InterPro; IPR010389; Urate_ox_N"]. This corrects the pathway gene assignment
  away from legacy `puuD` locus PP_3099.
- The direct experiment is on the A. fabrum COG3748 homolog Atu2314, not on
  Q88F11 [PMID:26349049 "Atu2314 and homologous genes belonging to COG3748 are
  responsible for urate oxidation"]. The KT2440 assignment is therefore ISS,
  strengthened by the adjacent PucM/UraH and PucL/UraD pathway genes.
- UniProtKB:A9CI11 was checked directly against UniProtKB and maps to the
  experimentally deleted ordered locus Atu2314 in A. fabrum C58; it carries
  COG3748, IPR010389, and the C-terminal cytochrome c domain. The generated
  report's 43.5% pairwise-identity value is not needed for the module and was
  not used as evidence.
- GO:0004846 and RHEA:21368 specify urate + O2 + H2O -> HIU + H2O2. The PuuD
  study instead found no PuuD-associated catalase induction and proposed
  cytochrome-mediated electron transfer [PMID:26349049 "production of H2O2 in
  the urate oxidation reaction catalysed by zfUox but not in the reaction
  catalysed by PuuD"]. No existing GO MF was used as a false exact match; a
  mechanism-appropriate term is proposed in the review.
- GO:0016491 is used as the core MF because it captures substrate oxidation
  without inventing an electron acceptor; GO:0009055 remains accepted as the
  electron-transfer component. Eight predicted transmembrane helices support
  plasma-membrane localization with ISM evidence. GO:0005887 cannot be used for
  the stronger wording because it is obsolete and replaced by GO:0005886.
- The OpenScientist report correctly recovered the PuuD architecture and states
  both `No direct biochemistry on PP_4289 itself.` and `Electron acceptor
  unidentified.` It nevertheless depicts the Q88F11 reaction as urate + O2 ->
  HIU and says electrons feed the respiratory chain. Those mechanistic claims
  exceed PMID:26349049, which presents electron transfer as a model and leaves
  the acceptor unresolved, so they were not imported into the review.
