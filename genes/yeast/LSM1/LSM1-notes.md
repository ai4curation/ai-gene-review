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
  start-sites-and directly stimulate transcription initiation and elongation."] This is a
  headline claim of the paper, not an incidental or contaminating observation.
  Caveat on the evidence available here: `publications/PMID_23706738.md` is abstract-only
  (`full_text_available: false`), and the abstract never names Lsm1p or describes the
  assays used. It says only that decaysome components as a group shuttle and associate
  with chromatin. Whether Lsm1p specifically was among the factors ChIP'd at promoters is
  something only the full text (which the SGD curator read) can establish, so no assay
  detail is asserted in the review YAML.
- Corrected action to `KEEP_AS_NON_CORE`: the annotation is retained, but treated as a
  secondary/moonlighting nuclear role distinct from LSM1's well-established core
  cytoplasmic mRNA-decapping-activation function (which remains the sole entry in
  `core_functions`).

## 2026-09-04 Update: review follow-up (PR #2937)

Addressed reviewer feedback on the change above:

- Removed assay details from the `GO:0003682` review that the cached abstract does not
  contain ("TAP-tagged Lsm1p ChIP at promoters", the appeal to unnamed "published/secondary
  sources", and the claim that the abstract shows the finding is "gene-specific"). The
  annotation stands on the SGD curator's IDA plus the abstract's decaysome-chromatin claim.
- `GO:0005634 nucleus` changed `ACCEPT` → `KEEP_AS_NON_CORE` for both the IDA
  (PMID:23706738) and the IEA (GO_REF:0000044) entries. `ACCEPT` means retain as core, but
  the nuclear pool is the same secondary shuttling phenomenon as the chromatin binding
  entry, and `core_functions` lists only cytoplasmic and P-body locations.
- Replaced the paper *title* used as `supporting_text` on the nucleus and cytoplasm IDA
  entries with verbatim quotes from the abstract that actually bear on localization.
- Moved changelog framing ("Changed from REMOVE to ...") out of `review.reason` into
  these notes.

No other oversights found in this review; all other actions (including the large set of
duplicate protein-binding IPI annotations marked `MARK_AS_OVER_ANNOTATED` in favor of the
specific `GO:1990726` complex term, and the `mRNA processing` REMOVE) are well-supported
and left unchanged.
