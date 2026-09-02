# LSM1 (YJL124C) Gene Review Notes

## 2026-09-02 Update: chromatin-binding annotation corrected (REMOVE → KEEP_AS_NON_CORE)

Audited the existing `LSM1-ai-review.yaml` for oversights. Found one genuine issue:

- `GO:0003682 chromatin binding` (IDA, PMID:23706738) had been marked `REMOVE` with the
  reviewer's own unsupported speculation that it "likely represents mislocalization or
  experimental artifact." This is an experimental (IDA) annotation and per project
  policy should not be second-guessed without contrary evidence.
- The cached abstract for PMID:23706738 (Haimovich et al. 2013, *Cell*, "Gene expression
  is circular: factors for mRNA degradation also foster mRNA synthesis") directly confirms
  the finding is real, not an artifact: [PMID:23706738 "these components shuttle between
  the cytoplasm and the nucleus, in a manner dependent on proper mRNA degradation. In the
  nucleus, they associate with chromatin-preferentially ∼30 bp upstream of transcription
  start-sites-and directly stimulate transcription initiation and elongation."] This is the
  central, specifically-tested claim of the paper (cytoplasmic mRNA-decay "decaysome"
  factors, TAP-tagged and ChIP'd at promoters), not an incidental or contaminating
  observation, and secondary sources describing this paper specifically list Lsm1p-TAP
  among the factors assayed for promoter-proximal chromatin binding.
- Corrected action to `KEEP_AS_NON_CORE`: the annotation is retained as a real,
  gene-specific finding, but treated as a secondary/moonlighting nuclear role distinct
  from LSM1's well-established core cytoplasmic mRNA-decapping-activation function (which
  remains the sole entry in `core_functions`).

No other oversights found in this review; all other actions (including the large set of
duplicate protein-binding IPI annotations marked `MARK_AS_OVER_ANNOTATED` in favor of the
specific `GO:1990726` complex term, and the `mRNA processing` REMOVE) are well-supported
and left unchanged.
