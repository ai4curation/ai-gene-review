# AVR9 (Fulvia fulva / Cladosporium fulvum; UniProt P22287) - curation notes

## 2026-10-02 - initial review

Sources: UniProt P22287, GOA (5 rows, all PHI-base), AVR9-deep-research-falcon.md,
cached publications (all abstract-only except PMID:25902074, which is full text).

### Identity, processing, structure
- 63-aa precursor: signal 1-23, propeptide 24-35, mature peptide 36-63 (UniProt).
- Processing: [PMID:8208859 "the elicitor accumulates in infected leaves as a 28-amino acid (aa) peptide"];
  [PMID:8208859 "We demonstrated that plant factors process the 34-aa peptide into the mature 28-aa peptide."]
- Apoplastic: [PMID:8555455 "processed AVR9 peptide present in apoplastic fluid (AF) of pAVIR1 transformed plants"]
  had the same sequence as AVR9 from infected tomato. UniProt ref 3 (non-PubMed) purified it from
  apoplastic fluids of infected tomato.
- Knottin: [PMID:9119054 "The AVR9 protein reveals the presence of a cystine knot"]; fold homologous to
  carboxypeptidase inhibitor, but no inhibitory activity shown (deep research, citing van den Burg 2003 thesis).

### Recognition
- HR in Cf-9 tomato: [PMID:8208859 "induces a hypersensitive response in tomato plants carrying the complementary resistance gene Cf9"].
- Indirect recognition: binding site independent of Cf-9
  [PMID:12239406 "Binding kinetics and binding capacity were similar for membranes of the MM-Cf0 and MM-Cf9 genotypes."];
  [PMID:9625714 "a positive correlation between their affinity to the membrane-localized binding site and their necrosis-inducing activity in MoneyMaker-Cf9 tomato was found"];
  [PMID:25902074 "Avr9 is also expected to interact indirectly with the Cf-9 protein"].
- Natural escape by gene loss: [PMID:25902074 "all Japanese isolates that can overcome the Cf-9 resistance gene lacked the entire Avr9 gene"].

### Virulence function: unknown
- [PMID:25902074 "Although the biological function of the Avr9 protein is not known"].
- NRF1 mutants with strongly reduced Avr9 expression were fully virulent on susceptible tomato
  [PMID:11277429 "On susceptible tomato plants, the Nrf1-deficient strains were as virulent as wild-type strains of C. fulvum, although the expression of the Avr9 gene was strongly reduced."]
  -- not a clean test of AVR9 itself. No virulence function asserted in the review.

### GO decisions
- GO:0080185 (EXP x2): ACCEPT. Definition explicitly includes recognition of the effector by plant R proteins;
  GO treats the recognised effector as participant (ligand-like). Same term used for AVR4 and other Avr effectors.
- GO:0140404 (EXP x1, TAS x2): MODIFY -> GO:0080185. Correct but uninformative parent; its subtree is mostly
  suppression terms, inviting an implied immunosuppressive role. PMID:26946045 (Ve1/Ave1 paper) abstract does not
  mention AVR9 -- likely the Cf-9/Avr9 control; not verifiable, so not removed.
- NEW GO:0140593 host apoplast (location; used for other apoplastic effectors such as Mg1LysM, AvrLm1).
- No MF: no biochemical activity shown; Cf-9 binding not shown. Did not propose a "recognised-by-host" MF.

### Ontology observation (project gap: how GO represents "being recognised")
- QuickGO ancestry: GO:0080185 is_a GO:0034055 "effector-mediated activation of host programmed cell death by symbiont",
  defined as activating PCD "to suppress the host innate immune response", and GO:0034055 is_a GO:0140403
  effector-mediated suppression of host innate immune response. So every avirulence effector annotated to
  GO:0080185 inherits a suppression-of-immunity claim -- logically inverted for AVR9. Raised in suggested_questions.
- "Being recognised" exists only as a process (GO:0080185); there is no MF/relation for an indirectly perceived elicitor.
