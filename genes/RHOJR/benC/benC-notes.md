# benC (Q93HW3, Rhodococcus jostii RHA1) notes

## 2026-10-23: review created for the benzoate_upper_pathway module

- Added as a cross-genus representative member of `modules/benzoate_upper_pathway.yaml`
  (benzoate 1,2-dioxygenase reductase) so the module is grounded beyond Pseudomonas putida KT2440.
- Deep research: `just deep-research-falcon RHOJR benC` was attempted and failed
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
- RHA1 BenC is 512 aa versus 336-348 aa for the proteobacterial BenC proteins; InterPro
  matches a C-terminal FadR/GntR C-terminal-like domain (IPR011711, IPR008920). The
  Rhodococcus sp. 19070 homologue BopZ likewise carries a 201-residue extension
  [PMID:11375157 "The reductase components of these latter dioxygenases, BenC and XylZ,
  are 201 residues shorter than the deduced BopZ sequence."]. Recorded as a question.
