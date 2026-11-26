# RYR2 notes

## 2026-11-26 Codex review

Perplexity deep research was unavailable for this batch; see the RYR1 notes for
the exact failure mode. This review uses the fetched UniProt/GOA data, PAINT
node rows and cached primary literature.

RYR2 is the cardiac ryanodine receptor, a homotetrameric calcium-release
channel in junctional sarcoplasmic-reticulum membrane. In cardiomyocytes it
opens in response to Ca2+ entering through L-type calcium channels and releases
SR Ca2+ into the cytosol, thereby coupling the action potential to cardiac
muscle contraction [file:human/RYR2/RYR2-uniprot.txt].

Main curation decisions:

- Keep `GO:0005219`, intracellular calcium-gated channel activity, SR
  calcium-release transport and SR membrane/channel-complex terms as the core
  RYR2 channel function.
- Retain cardiac contraction, cytosolic calcium regulation, heart-rate and
  action-potential rows where they describe the direct effect of SR Ca2+ release
  on excitation-contraction coupling.
- Modify the transferred negative-regulation-of-cytosolic-calcium row to
  positive regulation, because opening the RYR2 SR pore directly increases
  cytosolic Ca2+.
- Remove bare `GO:0005515` rows under the project protein-binding policy while
  keeping the distinct rows separate.
- Treat plasma-membrane/sarcolemma rows as over-annotated for a channel whose
  catalytic pore is in the SR membrane, even though RYR2 is assembled in
  junctional membrane complexes apposed to sarcolemmal T-tubules.
- Leave the rat-derived nuclear envelope row undecided: a perinuclear RYR2
  pool is plausible because the nuclear envelope is continuous with ER/SR, but
  the rat donor row needs source-level review.
- Keep PKA-, FKBP-, calmodulin-, S100A1- and tetramerization-associated terms
  as supported regulatory or assembly annotations but distinguish those from
  the pore's core calcium-release activity.
- Mark broad stimulus-response rows, pancreatic-cell apoptosis, manganese
  transport and developmental morphogenesis terms as peripheral or
  over-propagated when they arise from downstream phenotypes rather than from a
  direct RYR2 channel function.
