# ALMS1 review notes

## 2026-09-27: initial source review

The normal ClinGen seed contains 42 distinct annotations, all initially PENDING,
and three UniProt alternative products. Exact raw UniProt/GOA and seed bytes were
recovered from normal fetch run 36330587164 and imported without overwrites.
The original seed remains in the verified artifact and isolated staging area.
Falcon with the perplexity-lite fallback was attempted alongside publication
caching. The initial launcher could not use its default tools directory; the
installed matching client was then used, but both providers failed DNS. No
provider report was produced. These are manual primary-source notes.

ALMS1 is a large centrosome/basal-body-associated protein with an incompletely
resolved molecular activity. Human imaging places it at centriole proximal ends.
Depletion reduces centriolar C-Nap1 and weakens centrosome cohesion, but the
authors could not demonstrate ALMS1/C-Nap1 coimmunoprecipitation. A direct tether,
enzymatic activity, or autonomous microtubule-binding activity should not be
invented from these results. [PMID:20844083]
reports: “ALMS1 localizes specifically to the proximal ends of centrioles and basal
bodies”. Its Results, Figures 7–9, and discussion were read in the recovered full
article. C10orf90 and KIAA1731 experiments in this paper are distinguished from
the ALMS1 experiments; their phenotypes are not human ALMS1 assays.

[PMID:15855349] supports centrosome and
ciliary-base localization. Only its cached abstract was available. Patient
fibroblasts in that study could form apparently normal cilia, so disease status
does not establish universal failure of cilium formation in every cell type.

[PMID:22693585] supplies human patient
fibroblast evidence for altered actin stress fibers and slower transferrin
recycling. The actual full article distinguishes mouse C-terminal ALMS1 baits
in yeast, mouse-kidney coimmunoprecipitation, canine MDCK imaging, and the human
fibroblast experiments. The direct-interaction claim in its discussion must not
convert a tissue coimmunoprecipitation into a purified human binding assay.
Different N/C-terminal antibody patterns in MDCK cells suggest isoform-related
differences but do not map a function to a specific Q8TCU4 isoform accession.
ALMS1 is not thereby demonstrated to be the actin crosslinker or a motor.

[PMID:27803297] is an abstract-only
mouse physiological study. Impaired thermogenic adaptation in foz/foz mice and
improvement after intermittent cold exposure establish a whole-animal phenotype;
they do not expose a human ALMS1 molecular mechanism for cold thermogenesis.
The source-specific ISS assessment remains unresolved rather than rejecting the
mouse observations.

The cached article bodies for [PMID:21399614],
[PMID:31413325], and
[PMID:33961781] were inspected. The
centrosome proteomics paper corroborates the assay context but its target-level
supplementary row is not present in the extraction. Independent ALMS1 imaging
supports retaining centrosome localization. The two interaction papers describe
network generation/integration; the exact ALMS1–DISC1 record was not independently
recovered from their supplements. Their experimental protein-binding annotations
are left UNDECIDED, without alleging a false interaction or wrong-gene citation.

All 22 cited Reactome caches were read. They describe centrosome or cilium
events involving other proteins, including AURKA, PLK1, NuMA and distal-appendage
components. Their summaries do not mention ALMS1. This is not evidence that the
curated location assertion is false: membership in a larger modeled structure
may explain it. The broad cytosol location is retained as non-core; none of the
reaction titles is transferred into an ALMS1 kinase, exchange-factor, or motor
function. The original Reactome identifiers and machine titles are preserved.

The [Human Protein Atlas ALMS1 page](https://www.proteinatlas.org/ENSG00000116127-ALMS1/subcellular)
lists centrosome, cytosol, microtubules and basal-body-related locations. This
supports the localization context of GO_REF:0000052. It does not establish an
independent microtubule-binding molecular activity.

## Recent literature and remaining checks

[PMID:17954613] is titled for CEP164,
but its primary Figure 1 explicitly includes ALMS1 knockdown in human RPE1 cells.
It therefore must not be dismissed as a wrong-gene reference. Normal cache
retrieval was requested. This is a source lead, not a new annotation assertion.

[PMID:40021845] primarily studies
Drosophila Alms1a/b and also includes human ALMS1 localization. Its fly duplication
mechanism does not by itself establish identical human catalytic or regulatory
activity. Normal caching was requested for a source-specific full-text check.
The [July 2026 preprint](https://doi.org/10.64898/2026.07.15.738620) reports
human RPE1 centriole architecture defects after ALMS1 loss, arising after initial
procentriole assembly. It is unreviewed and rights reserved; no full article is
copied or novel GO assertion based solely on it. These leads reinforce the need
to separate centriole assembly, maturation/stability and cohesion when assessing
the existing ancestral regulation-of-replication inference.

No NEW term is proposed. Molecular activity remains unnamed rather than filling
the core with generic protein binding. Independent review, full validation and
the final citation census are pending.

## Independent-review refinements

The annotation peer read all 42 judgments and the compact core. Molecular activity
remains unnamed. A broader location alone is not a reason for NON_CORE: cytoplasm
and cytosol are now ACCEPT. The [Human Protein Atlas](https://www.proteinatlas.org/ENSG00000116127-ALMS1/subcellular)
reports supported cytosol with both HPA035276 and HPA043200 in U2OS; HPA035276 also
labels microtubules there. The microtubule pool remains NON_CORE because its role
is unresolved relative to the characterized centriolar and recycling functions.
Reactome cytosol assertions are retained with this independent location evidence;
their reaction titles do not establish ALMS1 catalytic functions. The misleading
use of a proximal-centriole quote as cytosol evidence was removed.

The peer independently read the human RPE1 U-ExM section of PMID:40021845:
ALMS1 caps proximal centrioles and is recruited after procentriole initiation.
The Plk4–Ana2 duplication perturbations are in flies. Its linked
funding correction [PMID:40102689], adds
omitted grants and does not change the experiments. Normal caching remains
pending for both this newer source and its correction.

The independent review and revised full validation pass. The 42 source annotations and three alternative products are preserved, with 36 ACCEPT, two KEEP_AS_NON_CORE and four UNDECIDED. PMID:21399614 identity/title/DOI were independently confirmed on primary PMC3102290; the ALMS1 supplementary row remains unverified. The remaining normal-cache requests are PMID:17954613, PMID:40021845 and PMID:40102689. No gene completion is claimed while these source requests remain unresolved.

## 2026-09-27: recovered-source assessment and citation closure

The three outstanding normal publication records are now cached byte-for-byte from hosted run 36335352002. All titles and identifiers were checked against primary PubMed. The records for PMID:17954613 and PMID:40021845 contain actual full article bodies; PMID:40102689 contains correction metadata only. Existing caches were not replaced.

The 2007 hTERT-RPE1 screen explicitly assays ALMS1 in Figure 1 and reports stunted cilia without substantially reducing the fraction of ciliated cells. The CEP164-specific distal-appendage work is not assigned to ALMS1. The 2025 human RPE-1 U-ExM Figure 2 directly supports the proximal centriole cap in the compact core. Human ALMS1 appears after procentriole initiation; the Plk4–Ana2 amplification and cartwheel perturbations are in Drosophila. Its discussion considers mammalian divergence or a shared function. The replication IBA therefore remains UNDECIDED, with this newer source now explicitly linked to that judgment. No NEW annotation is introduced from a necessity phenotype.

The earlier correction-body assessment came from the [original Springer notice](https://link.springer.com/article/10.1038/s44318-025-00411-6), which adds three omitted funding grant numbers. That external access does not change the normal correction cache into a full-text record. The correction content was checked on that original publisher page; the normal local record remains metadata-only.

All 42 source assertions, 42 actions, three products and prior reference entries remain intact; three assessed references were added. All ten cited PMID and 22 Reactome caches are present. COMPLETE denotes a finished review with explicit uncertainty in four decisions; it does not claim that the DISC1 supplementary interactions, exact centrosome-proteome target row, or ancestral placement have been resolved.


## 2026-09-27: independent response to PR 3318 evidence review

The full review at [comment 5858371146](https://github.com/ai4curation/ai-gene-review/pull/3318#issuecomment-5858371146) was assessed against the published 44c6cfd revision. All 42 source objects and actions, three products, reference identities and the two core locations remain unchanged (36 ACCEPT, two KEEP_AS_NON_CORE, four UNDECIDED). Source qualifiers are retained without using them to decide biological validity. No NEW annotation is proposed.

The two ALMS1–DISC1 IPI rows remain UNDECIDED. Generic protein binding is normally too uninformative to retain, but the annotation-reviewer skill explicitly preserves the standing UNDECIDED rule when the relevant evidence cannot be accessed or adjudicated. The exact supplementary pair-level records remain unrecovered. This is an evidence-access limitation, not a finding that the interactions are false or that network assays cannot support molecular function. The original [HENA PubMed record](https://pubmed.ncbi.nlm.nih.gov/31413325/) and [BioPlex PubMed record](https://pubmed.ncbi.nlm.nih.gov/33961781/) independently verify their identifiers, titles and DOIs. HENA citation correctness is therefore VERIFIED; both target-specific interaction assessments remain unresolved. No secondary interaction website was substituted for the primary target record.

The full [PMID:22693585] Methods, Results and Discussion provide positive physical-association evidence beyond the human loss phenotype: mouse C-terminal yeast-two-hybrid interactions with ACTN1/4, MYO5B and RINT1, mouse-kidney ACTN4 co-immunoprecipitation, and canine MDCK localization. Human patient fibroblasts show delayed transferrin recycling; the pericentrosomal recycling compartment remains appropriately positioned. The authors explicitly present the CART-associated transport subcomplex as a model. The study does not use rescue or separation-of-function experiments to connect an ALMS1 interface to the recycling step. The existing transport annotation is retained with curator deference and this positive context. Independently, the compact core now omits a structured directly_involved_in transport assertion while retaining the qualified biological connection and its evidence. This is a mechanistic boundary, not a demand for an autonomous motor or catalytic function. A separate annotation-reviewer peer independently read the same source and agreed with that distinction.

The actual [PMID:17954613] Figure 1/Results in human hTERT-RPE1 cells are now attached as a finding and core support: “the depletion of Cep57 or ALMS1 led to the formation of morphologically abnormal, stunted cilia without considerably reducing the efficiency of ciliogenesis”. The CEP164 distal-appendage mechanism is not transferred to ALMS1. [PMID:20844083] supports C-Nap1 retention and centrosome cohesion; its inspected experiments did not demonstrate direct ALMS1–C-Nap1 co-immunoprecipitation. No new cohesion or cilium-process annotation is manufactured from these perturbations. The biological questions distinguish elongation, cohesion and duplication.

The official [GO:0120162 definition](https://amigo.geneontology.org/amigo/term/GO:0120162) permits positive regulation through neural or endocrine control. It does not require a BAT-local enzyme. The [official mouse annotation graph](https://www.informatics.jax.org/homology/GOGraph/Alms1) preserves the IMP donor annotation from [PMID:27803297]. The positive foz/foz thermogenesis, sympathetic-tone and cold-exposure findings remain accepted as reported in the available abstract. The full donor paper remained inaccessible through the original publisher PDF and the request-only author-sharing route. UNDECIDED identifies the unresolved regulatory role and ortholog-transfer scope, not an absence of a BAT executor or a demand for direct human experiments. A finite question asks whether the role is neural/endocrine, adipocyte-autonomous or secondary to systemic effects.

The previous temporary-path correction receipt was replaced by the durable original publisher route. PMID display links were normalized to avoid duplicate URLs in the generated page. No publication record, provider output, GOA, UniProt record or prior history was edited. The unchanged finite citation census is ten PMIDs and 22 Reactome records, all locally present, plus the already documented July 2026 preprint; no new cache dependency is introduced. Known unchanged provider DNS failures were not retried.
