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

## 2026-09-28 Update: IBA and protein-binding re-review

Re-reviewed the LSM1 IBAs against the current PTHR15588 PAINT tree. The four GOA IBA
annotations all trace to appropriate PAINT placements:

- PTN000400405 carries `GO:0003729 mRNA binding`, with LSM1 itself among the
  experimental descendants. This is a valid self-supported IBA: the yeast IDA row helps
  place the ancestral state; the IBA then asserts conservation within the clade.
- PTN000400406 carries `GO:0000290 deadenylation-dependent decapping of
  nuclear-transcribed mRNA`, `GO:0000932 P-body`, and `GO:1990726 Lsm1-7-Pat1
  complex`. This node is specific to the cytoplasmic LSM1 branch and is separate from
  the nuclear/spliceosomal Lsm2-8 node PTN000400465.

Searched for newer LSM1 literature. The main post-2023 yeast-relevant paper found was
Musaev et al. 2024, Cell Reports, which reanalyzed yeast knockout mRNA-decay data and
found that `lsm1` deletion clusters with decapping mutants in ORF-length-mediated decay
[PMID:38625794 "In contrast, upf1Δ, upf2Δ, upf3Δ, not3Δ, lsm1Δ, edc3Δ, and dhh1Δ
strains elicited specific effects, suggesting that OMD functions through mRNA
surveillance, deadenylation, and decapping."]. This supports the existing core
deadenylation-dependent decapping function but does not warrant a new GO annotation.

Updated all eleven generic IntAct `GO:0005515 protein binding` buckets from
`MARK_AS_OVER_ANNOTATED` to `REMOVE`. The underlying interaction evidence is not
disputed, but `GO:0005515` adds no useful molecular-function assertion for LSM1 and the
previous proposed replacement term, `GO:1990726 Lsm1-7-Pat1 complex`, is a cellular
component term rather than a molecular-function replacement.

## 2026-09-29 Update: PR follow-up

Addressed post-review cleanup for the IBA re-review PR:

- Replaced the `GO:0000956 nuclear-transcribed mRNA catabolic process` changelog-style
  `review.reason` with the actual biological justification: the row is a broad but
  correct parent of the direct GO:0000288 and GO:0000290 decay subprocesses.
- Moved the generic `GO:0032991 protein-containing complex` and `GO:1990904
  ribonucleoprotein complex` IEA rows from `ACCEPT` to `KEEP_AS_NON_CORE`, in parallel
  with the generic `RNA binding` parent row.
- Corrected this note's description of the LSM1 self-supported `GO:0003729` IBA seed
  from IMP to IDA, matching the PMID:23222640 row.
- Removed PMID:38625794 from the mRNA-binding core function support because Musaev
  et al. 2024 corroborates the decapping/deadenylation process role, not the direct
  molecular function.
- Added `propagation_review` blocks to the four IBA annotations so the PANTHER
  PTN-level review is visible in the YAML, not only in this notes file.
- The 2026-09-04 note that the generic protein-binding rows were left unchanged is
  superseded by the 2026-09-28 update above.
