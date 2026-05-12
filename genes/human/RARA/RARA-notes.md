# RARA curation notes

## 2026-05-12 Falcon integration

Generated `RARA-deep-research-falcon.md` and used it to complete the initialized
GO review.

Core synthesis: RARA/RARalpha is a retinoic-acid-binding nuclear receptor
transcription factor. The Falcon report summarizes the central mechanism as
[file:human/RARA/RARA-deep-research-falcon.md "**RARA encodes RARα**, a
ligand-activated nuclear receptor that functions as a **sequence-specific
DNA-binding transcription factor**."] RARA binds retinoic acid response elements
as an RXR heterodimer [file:human/RARA/RARA-deep-research-falcon.md "RARα binds
RAREs primarily as an RXR heterodimer."] and acts through a ligand-dependent
corepressor/coactivator switch [file:human/RARA/RARA-deep-research-falcon.md
"RARα supports a canonical nuclear-receptor **cofactor “switch” mechanism**"].

Core annotations retained as ACCEPT include nuclear receptor activity, retinoic
acid binding, RARE/RNA polymerase II cis-regulatory DNA binding, retinoic acid
receptor signaling, positive and negative regulation of RNA polymerase II
transcription, nucleus/chromatin localization, and RNA polymerase II
transcription regulator complex.

Broad developmental, immune, proliferation, apoptotic-cell-clearance, estrogen
response, and retinoid response terms were generally kept as non-core when the
evidence supported them. The main caveat is that many RA-treated cell phenotypes
are downstream programs rather than direct RARA DNA-bound functions
[file:human/RARA/RARA-deep-research-falcon.md "many transcriptomic or phenotypic
outcomes in RA-treated cells reflect indirect downstream programs"].

Several terms were removed or marked over-annotated:

- `protein binding` rows were marked over-annotated because the informative
  biology is RXR/cofactor complex membership and DNA-bound nuclear receptor
  transcriptional regulation.
- mRNA/translation-repressor annotations were changed to UNDECIDED because the
  GOA rows are Ensembl Compara transfers from rat RARalpha evidence, and the
  relevant neuronal translation-regulatory literature was not evaluated in this
  Falcon synthesis.
- protein phosphorylation was removed because RARA is a phosphorylation substrate
  rather than a kinase [PMID:16417524 "Akt, which is constitutively activated in
  NSCLC cells, phosphorylates RARalpha and inhibits its transactivation."].
- fusion-specific differentiation blockade was not transferred wholesale to
  wild-type RARA; Falcon explicitly cautions that PML::RARA adds fusion-specific
  behavior [file:human/RARA/RARA-deep-research-falcon.md "PML::RARA and other
  RARA fusions preserve some RARα biochemical properties"].
