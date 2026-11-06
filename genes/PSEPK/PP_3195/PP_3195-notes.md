# PP_3195 curation notes

- UniProt Q88I07 names a Peptidase S9 catalytic-domain protein
  [file:PSEPK/PP_3195/PP_3195-uniprot.txt "RecName: Full=Peptidase S9 prolyl
  oligopeptidase catalytic domain-containing protein"]. This is a fold-level
  prediction, not evidence for a peptide substrate.
- OpenScientist identifies KEGG K26184/FdeB and the predicted R13077 lactone
  hydrolysis [file:PSEPK/PP_3195/PP_3195-deep-research-openscientist.md "KEGG
  links FdeB (K26184) to **reaction R13077**, classified as a **hydrolase**"] but
  explicitly reports no direct PP_3195 characterization
  [file:PSEPK/PP_3195/PP_3195-deep-research-openscientist.md "No direct
  biochemical or genetic characterization of PP_3195/FdeB itself has been
  published."].
- A committed global alignment gives 81.6% identity to the corresponding
  Herbaspirillum locus protein D8J0W6 and finds the same GVSLG motif in both
  sequences [file:PSEPK/PP_3195/PP_3195-bioinformatics/RESULTS.md "Pairwise
  identity over aligned residue pairs: 81.6%"]. Neither protein has direct
  R13077 evidence.
- GO:0052689 is retained as the substrate-neutral core MF. Proteolysis is
  removed because no biological proteolysis role is supported. Serine-type
  peptidase activity is marked over-annotated: the Peptidase S9/IPR001375 and
  COG1506 family signal is real, but it does not identify a peptide substrate
  for this paralog. GO:0009812 is added at ISS level for the predicted pathway role.
- No cellular-component term is asserted. The report's AlphaFold triad geometry
  and cytoplasmic localization were not independently reproduced and are not
  needed to capture the defensible function.

## 2026-11-06 — comparative review follow-up

Reassessed the PR #6140 review requests against the original row payloads and independent sources. See `analysis/module_audits/bacterial_flavonoid_degradation/round1-source-review.md` for the mapping, family and participation decisions. All original rows remain in their original order; inherited proposals that lack positive participation evidence are withdrawn by review action rather than deleted. No raw UniProt, GOA or provider artifact was edited.

The inherited GO:0046275 proposal is explicitly `retired: true` because this review withdraws it from the active curator-authored set. Its source fields and row position are retained. This does not claim that an upstream GOA row disappeared. The current MAOA judgment records the reassessment; the original NEW judgment is preserved in git and the follow-up preservation record. The existing schema defines retirement as an annotation being retired or replaced, and `docs/goa_source_refresh.md` uses explicit retirement to preserve withdrawn curator-authored assertions.
