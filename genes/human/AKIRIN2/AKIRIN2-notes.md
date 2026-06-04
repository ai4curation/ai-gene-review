# AKIRIN2 PN Review Notes

## Deep research status

Falcon deep research was attempted with `perplexity-lite` fallback for the PN review. Falcon timed out after 600 seconds, and the fallback provider returned a quota/401 error, so no provider-authored `AKIRIN2-deep-research-*.md` file was available for this review. The review below uses cached GOA, UniProt, PN projection, and publication files instead.

## Proteostasis projection

The PN projection has one AKIRIN2 candidate addition: `GO:0070628 proteasome binding`, from `Ubiquitin Proteasome System|Proteasome and associated proteins|adaptors|Akirin` in `projects/PROTEOSTASIS/reports/pn_projection/pn_projected_annotations.tsv`.

This projection is supported by direct primary evidence, not merely by the PN bucket. The AKIRIN2 proteasome-import paper reports that AKIRIN2 is required for nuclear protein degradation and that AKIRIN2 homodimers "directly bind to fully assembled 20S proteasomes" to mediate nuclear import [PMID:34711951 "directly bind to fully assembled 20S proteasomes"]. UniProt summarizes the same mechanism as AKIRIN2 binding 20S proteasomes at one end and IPO9 at the other to import pre-assembled proteasomes through the nuclear pore [file:human/AKIRIN2/AKIRIN2-uniprot.txt "directly binds to fully assembled 20S proteasomes at one end and to nuclear import receptor IPO9 at the other end"].

Decision: add `GO:0070628 proteasome binding` as a `NEW` annotation with `PMID:34711951`, and modify the generic `protein binding` annotation from the same paper toward `proteasome binding` plus `protein-macromolecule adaptor activity`.

## Existing GOA review stance

AKIRIN2's core PN function is proteasome binding/adaptor-mediated nuclear proteasome import, directly involved in `protein import into nucleus`, `proteasome localization`, and `nuclear protein quality control by the ubiquitin-proteasome system` [PMID:34711951 "nuclear import of proteasomes in vertebrates"; PMID:34711951 "nuclear protein degradation"].

The conserved transcriptional coregulator role is also real. The original akirin paper shows human AKIRIN2 is nuclear [PMID:18066067 "Antibody staining of the human cells clearly showed the nuclear localization of HsAkirin1 and HsAkirin2"] and that mouse Akirin2 acts downstream of NF-kappaB for TLR/IL-1R-inducible gene expression [PMID:18066067 "Akirins are novel important nuclear cofactors regulating the transcriptional activities of main transactivators"]. These transcription and immune annotations are valid, but in the PN batch they should not be used to broaden AKIRIN2 beyond the supported proteasome-import projection.

The high-throughput interactome `protein binding` and `enzyme binding` annotations do not establish a specific AKIRIN2 activity. They were marked as over-annotated unless rescued by more specific mechanistic evidence. The exception is identical protein binding, because the proteasome-import paper independently reports AKIRIN2 homodimer formation [PMID:34711951 "AKIRIN2 forms homodimers"].

## Open question

The main biology still unclear for curation is whether AKIRIN2's NF-kappaB/chromatin co-regulator complexes are mechanistically coupled to, or separable from, its proteasome-import adapter function.
