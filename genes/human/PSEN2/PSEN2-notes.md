# PSEN2 Notes

## 2026-06-19

Manual notes created because provider deep research was unavailable in this run.
`timeout 180 just deep-research-falcon human PSEN2 --fallback perplexity-lite`
stayed silent and timed out without writing an artifact. Publication caching was
refreshed separately with `just fetch-gene-pmids human PSEN2` and confirmed all
18 PSEN2 review PMIDs were already cached. Per project instructions, no
provider-named deep-research file was written manually.

Core biology: PSEN2 encodes presenilin-2, a catalytic presenilin isoform in the
gamma-secretase complex. Gamma-secretase cleaves membrane substrates including
APP and Notch [PMID:15274632 "This enzyme cleaves many type I membrane
proteins, including the amyloid beta-protein (Abeta) precursor (APP) and the
Notch receptor."]. Direct PSEN2 mutagenesis supports the catalytic annotation:
the two PS2 transmembrane aspartates are critical for gamma-secretase activity
[PMID:10652302 "Here, we show that the two TM aspartates in PS2 are also
critical for gamma-secretase activity, providing further evidence that PS2 is
functionally homologous to PS1."].

Substrate biology: PSEN2 participates in APP processing and Notch signaling.
The D366A catalytic-site mutation caused deficits in APP proteolytic processing
[PMID:10497236 "Cells expressing the PS2 D366A mutation exhibit significant
deficits in proteolytic processing of beta-amyloid precursor protein indicating
a defect in gamma-secretase activity."] and also impaired Notch signaling
[PMID:10497236 "the PS2 D366A mutation not only blocks gamma-secretase activity
but also inactivates PS2 activity in Notch signaling by inhibiting the
proteolytic release of the cytoplasmic Notch1 domain."].

PSEN2-specific localization: compared with PSEN1, PSEN2-containing
gamma-secretase has strong late endosome/lysosome enrichment. The Cell paper
identifies a PSEN2 sorting motif that directs the complex to late
endosomes/lysosomes through AP-1 [PMID:27293189 "identified a unique motif in
PSEN2 that directs this γ-secretase to late endosomes/lysosomes via a
phosphorylation-dependent interaction with the AP-1 adaptor complex."] and
states that PSEN2 selectively cleaves substrates in those compartments
[PMID:27293189 "PSEN2 selectively cleaves late endosomal/lysosomal localized
substrates and generates the prominent pool of intracellular Aβ that contains
longer Aβ"]. This supports accepting late endosome/lysosome annotations as
core localization context and treating repeated pathway-level plasma membrane
annotations cautiously.

Calcium and MAM biology: PSEN2 has evidence for ER-mitochondria calcium
coupling and membrane-contact effects [PMID:21285369 "we show that
overexpression or down-regulation of PS2, but not of presenilin 1 (PS1),
modulates the Ca(2+) shuttling between ER and mitochondria"]. For GO review,
calcium ion homeostasis, regulation of mitochondrial calcium import, and
mitochondria-associated ER membrane-contact annotations were retained as
non-core rather than promoted into the core function.

Knowledge gaps to curate:

- Which endogenous PSEN2 gamma-secretase complexes and APH1 isoform
  combinations define normal in-vivo PSEN2 substrate specificity across tissues?
- Which PSEN2 locations represent mature active gamma-secretase complexes, and
  which represent holoprotein trafficking, overexpression, or interactor-specific
  localization contexts?
- Which calcium-homeostasis and ER-mitochondria contact phenotypes reflect
  conserved normal PSEN2 biology rather than mutant, overexpression, stress, or
  disease-model context?

Review update: completed first-pass review of all 79 seeded GO annotations.
Final action distribution after validation: 40 ACCEPT, 24 KEEP_AS_NON_CORE, 11
MARK_AS_OVER_ANNOTATED, and 4 UNDECIDED. `just validate human PSEN2` passes
cleanly.

## 2026-06-20 Second-Pass Review Notes

Second-pass audit confirmed the core PSEN2 framing: PSEN2 is a catalytic
presenilin isoform in gamma-secretase complexes, with PSEN2-specific
late-endosome/lysosome enrichment and substrate specificity. The YAML now records
manual `reference_review` metadata for PMID:15274632, PMID:10497236,
PMID:10652302, PMID:27293189, and PMID:21285369.

No annotation actions were changed in this pass. The four remaining UNDECIDED
annotations are response to hypoxia and three electronically inferred synaptic
location terms. The local evidence supports PSEN2 endolysosomal localization in
neuronal contexts, but not specific synaptic vesicle, presynaptic membrane, or
synaptic membrane localization; these should remain UNDECIDED pending stronger
direct evidence.
