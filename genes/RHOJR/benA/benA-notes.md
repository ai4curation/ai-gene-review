# benA (Q932V1, Rhodococcus jostii RHA1) notes

## 2026-10-23: review created for the benzoate_upper_pathway module

- Added as a cross-genus representative member of `modules/benzoate_upper_pathway.yaml`
  (benzoate 1,2-dioxygenase alpha subunit) so the module is grounded beyond Pseudomonas putida KT2440.
- Deep research: `just deep-research-falcon RHOJR benA` was attempted and failed
  with "Failed to authenticate" (provider credentials rejected), so there is no
  `-deep-research-*.md` file. The review is based on the UniProt entry and the
  cached publications: PMID:11673430.
- Every quotation in the review is verbatim from those cached sources (several
  are abstract-only; see `full_text_unavailable` on each reference).
- Process annotation GO:0043639 benzoate catabolic process is added as NEW where
  absent from GOA: the protein performs (part of) a step of the
  benzoate-to-catechol conversion, which the cited papers reconstitute.
- Propagated TreeGrafter terms from the broad PANTHER families
  (3-phenylpropionate catabolic process on BenB; fatty acid elongation on BenD)
  are removed, consistently with the PSEPK ben reviews.
- UniProt carries a ProRule caution on the Rieske domain; the CXH...CXXH Rieske motif is
  present by inspection of the sequence, and the knockout phenotype shows the protein is
  functional, so 2Fe-2S binding is accepted.
