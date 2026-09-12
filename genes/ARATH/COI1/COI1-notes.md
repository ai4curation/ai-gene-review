# COI1 review notes

Deep research provider status, 2026-05-06: Falcon timed out on CTR1 and the batch run was stopped before repeated timeouts; Perplexity returned 401 insufficient_quota; OpenAI timed out on CTR1. I reviewed COI1 manually from UniProt, cached publications, and PANTHER family context.

QuickGO annotation/search returned HTTP 500 for this accession on 2026-05-06, including with a `UniProtKB:` prefix. The GOA TSV in this branch was populated from UniProtKB REST GO cross-references so the existing-annotation validator has PMID/GO_REF provenance rather than treating known annotations as new.

Core interpretation: COI1 is the F-box substrate-recognition and hormone co-receptor subunit of SCF(COI1). It links jasmonate perception to JAZ repressor degradation and JA-dependent defense, fertility, and growth responses [PMID:9582125; PMID:12172031; PMID:17637675; PMID:17637677; PMID:20927106]. Developmental, defense, shade, wound, stomatal, and extracellular ATP annotations are retained as non-core downstream outputs unless they describe the SCF/JAZ degradation mechanism.

Falcon retry status, 2026-05-07: Falcon deep research completed in `COI1-deep-research-falcon.md`. The report supports the existing review conclusion that COI1 is the F-box/LRR SCF substrate adaptor and jasmonate co-receptor that promotes JAZ repressor degradation.

## 2026-09-12 — full annotation and evidence re-review

Reviewed all 23 rows (including the existing NEW adaptor proposal), 16 original
PMID caches, UniProt and the existing Falcon report. Publication caching completed
16/16 without force-refreshing any record. Falcon/perplexity-lite research was
launched concurrently; the outcome is recorded below. No generic protein-binding
row is present.

**Core mechanism.** Primary studies establish SCF assembly (PMID:12172031),
ligand-dependent COI1-JAZ interaction and proteasomal degradation (PMID:17637677,
PMID:17637675), and the structural co-receptor (PMID:20927106). Added exact
snippets and reference findings for these mechanisms and the physiological
outputs. The broad response-to-jasmonate rows now ACCEPT: breadth does not make
the protein's central hormone response non-core. The broad protein-catabolism
MODIFY now explicitly cites the primary SCF/JAZ experiments in addition to its
original general review; the inaccessible review abstract is not claimed to
establish the specific mechanism. QuickGO definitions verified GO:1990756 and
GO:0031146.

**Insect response corrected.** The old REMOVE extrapolated from the absence of
COI1 dependence for *induced* glucosinolate accumulation. Retrieved the actual
full [PMID:15923339 article](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1150428/?report=xml)
through the NCBI report endpoint. The Results distinguish consumption, growth and
constitutive versus induced chemistry: “the best insect growth was achieved on
coi1”. The cached abstract also explicitly reports lower constitutive
concentrations in coi1. The broader insect response is therefore retained as
non-core; the negative result for one metabolite endpoint is preserved in the
rationale. The local cache has only partial sections despite its full-text flag,
so the outside-cache result is documented here, not fabricated as a cached quote.

**Defense-source uncertainty.** Negative defense regulation (PMID:16732289)
changes from REMOVE to UNDECIDED. Independence of mlo resistance from jasmonate
is not evidence that all COI1-mediated defense regulation is absent, and the
publisher full text could not be accessed. Both original systemic-resistance
TAS sources lack accessible COI1-specific distal resistance assays; these also
become UNDECIDED. Bacterial defense and stomatal movement from PMID:16959575
become UNDECIDED because the accessible abstract does not expose the original
COI1 experiment. Jasmonate/coronatine binding is established, but it does not
by itself specify whether an immune outcome protects the plant or is exploited
by the pathogen. No removal is based on inaccessible evidence.

**Confirmed developmental assays.** Retrieved full PMC5129707 through the same
NCBI report endpoint. PMID:27756820 Results/Fig.5 show COI1-dependent root growth
inhibition by active analogues, and Results/Fig.1 show that CFA-Ile/coronatine
restore opr3 fertility but not coi1-1 fertility. These confirm the source-specific
root and reproductive contexts; PMID:23573263 additionally documents anther
failure to dehisce. The flowering/light source PMID:20435902 explicitly describes
early flowering of coi1-16 and COI1-dependent far-red responses. These downstream
roles remain non-core. The fungus-to-oomycete MODIFY remains supported by the
explicit Pythium irregulare identity in PMID:17513501 and QuickGO GO:0002229.

All source annotation fields are preserved; no identifiers were guessed. Removed
family member-list excerpts from core mechanistic support, and replaced the
stale proposed-question assertion that no suitable receptor term exists with a
biological question about ligand/degron/cofactor selectivity.

Falcon/Edison refresh completed successfully in 419.19 seconds; fallback was not
needed. Generated report/artifact retained without manual editing. It identified
an additional relevant primary source, PMID:34145662 (*The jasmonoyl-isoleucine
receptor CORONATINE INSENSITIVE1 suppresses defense gene expression in Arabidopsis
roots independently of its ligand*). DOI 10.1111/tpj.15372 was independently
resolved in Europe PMC; the CLI fetched the PubMed abstract. The study states
that genes affected by COI1 but not JA-Ile remain repressed by a COI1 variant
compromised in JAZ interaction. This is added as a bounded finding and description
extension, with the unidentified molecular mechanism retained as a question.
It supports root-context repression but does not resolve the original inaccessible
mlo-paper annotation; that source-specific row remains UNDECIDED.

Validation: `just validate ARATH COI1` passes. The sole advisory warning is
that no annotation cites the generated research report; original and independently
verified primary papers provide the actual support. History validation and
`git diff --check` pass. Source annotation fields match the before-review snapshot
exactly.
