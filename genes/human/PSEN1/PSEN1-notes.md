# PSEN1 Notes

## 2026-06-19

Manual notes created because provider deep research was unavailable in this run.
`just deep-research-falcon human PSEN1 --fallback perplexity-lite` stayed silent
without writing an artifact before interruption, and direct
`just deep-research-perplexity-lite human PSEN1` failed with a Perplexity 401
insufficient-quota error. Per project instructions, no provider-named
deep-research file was written manually.

Core biology: PSEN1 encodes presenilin-1, the catalytic presenilin component of
the gamma-secretase intramembrane protease complex. Purified active
gamma-secretase contains presenilin N- and C-terminal fragments together with
nicastrin, APH1, and PEN2 [PMID:15274632 "Extensive mass spectrometry of the
purified proteins strongly suggests that PS-NTF/CTF, mNCT, Aph-1, and Pen-2 are
the components of active gamma-secretase."]. This supports retaining
gamma-secretase complex membership and intramembrane protease activity as core
PSEN1 functions.

Substrate biology: gamma-secretase cleaves type I membrane proteins, including
APP and Notch receptor substrates [PMID:15274632 "This enzyme cleaves many type
I membrane proteins, including the amyloid beta-protein (Abeta) precursor (APP)
and the Notch receptor."]. For GO review, Notch receptor processing/signaling
and amyloid-beta formation are evolved substrate-processing functions of the
presenilin complex, not merely Alzheimer disease progression hypotheses.

Structural/catalytic support: high-resolution human gamma-secretase structure
places the two PSEN1 catalytic aspartates in the transmembrane active site
[PMID:26280335 "Among the two catalytic residues, Asp257 is located in the
middle of TM6 slightly to the extracellular side, whereas Asp385 maps to the
cytoplasmic side of TM7"]. This supports accepting GO:0042500 as a core
molecular function.

Calcium biology: presenilins also have experimental support for ER calcium leak
activity independent of gamma-secretase [PMID:16959576 "presenilins account for
approximately 80% of passive Ca(2+) leak from the endoplasmic reticulum."]. For
curation, calcium ion homeostasis should be retained but treated cautiously as a
non-core/secondary presenilin activity unless annotation evidence is specific to
normal in-vivo biology.

Knowledge gaps to curate:

- Which PSEN1/gamma-secretase substrates are established in evolved in-vivo
  biology across tissues, rather than inferred from overexpression or disease
  models? APP and Notch are clear; cadherin, EphB, TREM2-trafficking, and other
  candidate substrate/interactor annotations need evidence-by-evidence review.
- Which calcium-homeostasis annotations reflect a normal presenilin biological
  function in vivo versus cellular phenotypes of familial Alzheimer variants,
  knockout systems, or stress contexts?
- Which subcellular-location annotations correspond to endogenous mature
  gamma-secretase activity versus overexpressed full-length presenilin or
  isolated presenilin-interactor experiments?

Review update: completed first-pass review of all 197 seeded GO annotations.
Action distribution after validation: 65 ACCEPT, 52 KEEP_AS_NON_CORE, 57
MARK_AS_OVER_ANNOTATED, 7 MODIFY, and 16 UNDECIDED. The UNDECIDED annotations
are mostly unusual locations or context-specific assertions where cached
evidence was not strong enough to overrule or confidently retain curator
assertions. `just validate human PSEN1` passes cleanly.

## 2026-06-20 Second-Pass Review Notes

Second-pass audit confirmed that the core PSEN1 framing remains appropriate:
PSEN1 is the catalytic presenilin subunit of the gamma-secretase complex, with
APP and Notch processing as central evolved substrate biology. The main PMID
anchors now have `reference_review` metadata in the YAML: PMID:15274632 for
complex composition and APP/Notch substrate cleavage, PMID:26280335 for the
human gamma-secretase structure and catalytic aspartates, and PMID:16959576 for
ER calcium leak biology.

No annotation actions were changed in this pass. The remaining UNDECIDED
annotations are mostly unusual location terms such as kinetochore, nuclear
membrane, centrosome, mitochondrial membrane, synaptic vesicle, neuromuscular
junction, sarcolemma, and azurophil granule membrane. These were deliberately
left UNDECIDED rather than removed because the cached material is not sufficient
to overrule curator or electronic-source assertions without full-text review.
