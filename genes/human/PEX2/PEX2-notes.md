# PEX2 (P28328) curation notes

## 2026-09-04 — Finishing pass (PAINT no-IBA project)

Completed the review pass over all existing annotations; status moved IN_PROGRESS → COMPLETE
(validation clean, zero warnings). Changes made:

1. **Resolved the GO:0000425 (pexophagy) action inconsistency.** The IDA annotation from
   PMID:26344566 was UNDECIDED on the grounds that the paper "does not directly test PEX2".
   The cached full text shows it does: siRNA knockdown of the RING peroxins was performed and
   reduced PEX5 ubiquitination in the ATM/ROS pexophagy pathway
   [PMID:26344566 "The RING peroxins PEX2, PEX10 and PEX12 are part of a peroxisome-localized
   E3 ligase responsible for polyubiquitination of PEX534, and as expected, siRNA knockdown of
   these peroxins reduced polyubiquitination of PEX5"] and
   [PMID:26344566 "Knockdown of these E3 ligases also reduced monoubiquitination of PEX5,
   suggesting this peroxisomal E3 ligase also participates in PEX5 monoubiquitination"].
   Changed to ACCEPT, consistent with the ACCEPT for the PMID:27597759 pexophagy IDA.

2. **Added structured `propagation_review` to the IBA REMOVE of GO:0016593 (Cdc73/Paf1
   complex).** The GOA WITH/FROM for this IBA is `PANTHER:PTN008299004|UniProtKB:P28328`,
   i.e. the phylogenetic assertion is seeded by PEX2's *own* IDA from PMID:18987311 — the
   parafibromin/PAF1 transcription-complex paper. That IDA is a homonym confusion between
   PEX2's historical synonym PAF1 (Peroxisome Assembly Factor 1
   [PMID:1546315 "A human complementary DNA has been cloned that complements the disease's
   symptoms (including defective peroxisome assembly) in fibroblasts from a patient with
   Zellweger syndrome."]) and the unrelated PAF1/RNA-polymerase-II-associated factor.
   Classified root_cause: SOURCE_BAD, failure_mode: SOURCE_MISCITATION. The four
   PMID:18987311-based annotations (Cdc73/Paf1 complex, protein destabilization, and the two
   proliferation terms) all carry REMOVE for the same reason. Note this is *not*
   second-guessing an experimental annotation on full-text grounds: the miscitation is a gene
   identity error, evident from the paper itself.

3. **Added `core_functions` (previously absent — was a validation warning).** Three functions:
   - E3 ubiquitin ligase (GO:0061630) within the PEX2-PEX10-PEX12 ubiquitin ligase complex
     (GO:0000151) monoubiquitinating PEX5 for receptor recycling (GO:0016562) during matrix
     protein import, at the peroxisomal membrane
     [PMID:35768507 "We propose that the N terminus of a recycling receptor is inserted from
     the peroxisomal lumen into the pore and monoubiquitylated by RF2 to enable extraction
     into the cytosol"].
   - Pexophagy trigger: PEX2-specific ubiquitination of peroxisomal membrane proteins during
     amino acid starvation [PMID:27597759 "PEX2, but not PEX10 or PEX12, acts as the E3
     ubiquitin ligase to selectively ubiquitinate peroxisomal membrane proteins to designate
     peroxisomes for autophagy-mediated degradation during amino acid starvation conditions."].
   - Lipolysis regulation: ROS-stabilized PEX2 polyubiquitinates ATGL at K92 (K48-linked)
     for proteasomal degradation [PMID:34903883 "PEX2 specifically poly-ubiquitinates
     lipolytic protein ATGL at the K92 site when ATGL distributes on the LD surface for
     proteasome-targeted degradation in different cell types."].

4. **Added two `action: NEW` annotations** so the core_functions terms are reflected in
   existing_annotations: GO:0000151 (ubiquitin ligase complex; IDA, PMID:35768507 — GOA has
   no complex-membership CC term for PEX2) and GO:0050995 (negative regulation of lipid
   catabolic process; IDA, PMID:34903883).

5. **Cited the deep research file** (`file:human/PEX2/PEX2-deep-research-falcon.md`) in the
   references list and in the NEW GO:0000151 annotation — its synthesis of the 2024
   Kumar et al. and Pandey reviews genuinely informed the framing of the heterotrimeric
   ligase/retrotranslocon complex as PEX2's core context.

Final action tally: 41 ACCEPT, 9 KEEP_AS_NON_CORE, 5 REMOVE (1 IBA + 4 IDA/IMP, all from the
PAF1 homonym miscitation), 4 MARK_AS_OVER_ANNOTATED (bare protein binding IPIs), 2 NEW,
0 UNDECIDED, 0 PENDING.

Notable curation finding worth flagging upstream: PEX2 receives no IBA for its actual core
functions (peroxisomal membrane / peroxisome organization IBAs exist, but nothing for the E3
ligase activity or receptor recycling), while its only *complex* IBA (Cdc73/Paf1) is a
propagation of its own homonym-confused IDA. See interpro/panther/PTHR48178/PTHR48178-review.yaml.
