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

## 2026-10-01 Update: current-GOA refresh and exact-source review

Refreshed GOA and UniProt for the IBA re-review campaign. The current GOA has 55
raw rows, collapsing to 54 active exact source assertions in the review because SGD
and ComplexPortal emit the same `GO:0000932` / `PMID:12730603` / IDA P-body
assertion. All 23 newly seeded rows have now been reviewed:

- The new `GO:0003723 RNA binding` IEA row from `GO_REF:0000002` /
  `InterPro:IPR047575` was kept as non-core, in parallel with the older broad RNA
  binding row, because LSM1's direct molecular function is the more specific
  `GO:0003729 mRNA binding`.
- Nineteen newly split IntAct `GO:0005515 protein binding` rows were marked
  `REMOVE`, matching the already reviewed IntAct rows. These exact assertions cover
  Lsm-family and decapping-factor partners from `PMID:10688190`, `PMID:10900456`,
  `PMID:11805837`, `PMID:16429126`, `PMID:18719252`, `PMID:37070168`, and
  `PMID:37968396`; the interactions themselves are plausible but the generic
  `protein binding` molecular-function term is not informative for Lsm1p.
- The new UniProt `EXP` nucleus and cytoplasm rows from `PMID:10761922` were reviewed
  against the current UniProt record and retained as `KEEP_AS_NON_CORE` and `ACCEPT`,
  respectively.
- The new ComplexPortal `GO:1990726 Lsm1-7-Pat1 complex` row from `PMID:24139796`
  was accepted; the cached abstract explicitly supports both the heptameric Lsm1-7
  ring and the Pat1-bound structure [PMID:24139796 "structure of Lsm1-7 bound to the
  C-terminal domain of Pat1 reveals"].

Five no-longer-live exact source rows were kept with `retired: true`: the old CAA
`GO:0003723` row, old UniProt keyword rows for `GO:0006397` and `GO:1990904`, and
the `GO:0005515` buckets from `PMID:14759368` and `PMID:16554755`.

The PTHR15588 IBA calls remain unchanged. `PTN000400405` still carries conserved
`mRNA binding`, `PTN000400406` carries the cytoplasmic Lsm1 branch's P-body,
Lsm1-7-Pat1-complex, and decapping assertions, and `PTN000400465` carries the
separate Lsm2-8/U6 spliceosomal branch calls. `SGD:S000003660` is legitimate
descendant evidence for LSM1's own IBAs, not circular support.

The newer-paper search found no direct post-2024 budding-yeast LSM1 primary paper
that changes this review's GO actions. Pulido et al. 2024 mention Lsm1 in the
broader decapping/chromatin-transcription group but then test Pat1 in the cell-wall
integrity response [PMID:38604529 "Within this group are the so-called decapping
activators, including Pat1, Dhh1, and Lsm1. In this work, we have investigated the
role of Pat1 in the yeast"]. Zedan et al. 2024 refined the global relationship
between deadenylation and decapping, concluding that "for most yeast mRNAs, it is
not critical for mRNA decapping and degradation" [PMID:39322754]. Gouhier et al.
2026 uncovered NMD-dependent decapping of short-poly(A) noPTC mRNAs [PMID:41997935
"Recognition of short poly(A)-tailed mRNAs by Upf1, Upf2 and Upf3 (the NMD
machinery) triggers their decapping"], but this is an Upf1/NMD study that uses the
Lsm1-7/Pat1 short-tail recognition pathway as background.
