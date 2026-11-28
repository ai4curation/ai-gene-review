# RUNX2 review notes

Deep research could not be generated in this worktree: Falcon was unavailable, the Perplexity fallback was unavailable, and the Claude Code provider was not logged in. I therefore used the cached UniProt record, GOA-seeded publications, Reactome records, and the PTHR11950 PAINT slice directly.

RUNX2 is the osteoblast-specialized member of the RUNX family. The shared mechanism is Runt-domain DNA binding in a RUNX:CBFB/core-binding-factor transcription complex, while the defining biological output is the osteoblast differentiation and ossification program. UniProt summarizes this directly as "Transcription factor involved in osteoblastic differentiation and skeletal morphogenesis", and the original Cbfa1 knockout study found that Cbfa1-deficient mice lacked osteoblasts and bone [PMID:9182764, "Analysis of their skeletons revealed an absence of osteoblasts and bone."].

Human genetics reinforces the same core biology. Heterozygous loss of CBFA1/RUNX2 causes cleidocranial dysplasia [PMID:9182765, "We conclude that CBFA1 mutations cause CCD and that heterozygous loss of function is sufficient to produce the disorder."], and more recent CCD mutation studies assay loss of nuclear accumulation or osteocalcin-promoter transactivation [PMID:28738062, "Luciferase reporter assay demonstrated that all the three novel RUNX2 mutations significantly reduced the transactivation activity of RUNX2 on osteocalcin promoter."].

The RUNX2-specific experimental rows for osteoblast differentiation, ossification, positive regulation of osteoblast differentiation, nuclear localization, Pol II transcriptional activation, and RUNX:CBFB complex membership are accepted. The generic InterPro DNA-binding and transcription rows are modified to Pol II-specific descendants, and `GO:0001216` DNA-binding transcription activator activity is modified to the Pol II-specific activator term `GO:0001228`.

The BMP/SMAD signaling rows overstate the role of RUNX2. The miR-205 paper identifies both RUNX2 and SMAD1 as direct targets of the same microRNA during vascular smooth-muscle osteogenic differentiation [PMID:25012146, "Runx2 and Smad1 were identified as direct targets of miR-205 by computational analysis and experimental assays."], which supports RUNX2 as an osteogenic transcriptional target in that system but not as a cell-surface BMP receptor or SMAD signal-transduction component.

RUNX2 has several real cytosolic or cytoplasmic degradation and interaction contexts, including Reactome's STUB1/CHIP ubiquitination events, but those are regulatory contexts around a transcription factor whose core site of action is nuclear chromatin. They are therefore kept as non-core localizations.

The 15 bare `GO:0005515` protein-binding rows are all uninformative interaction capture. Even where the interactions themselves are biologically real, they do not identify a more specific RUNX2 molecular activity and should be removed under the current protein-binding policy.
