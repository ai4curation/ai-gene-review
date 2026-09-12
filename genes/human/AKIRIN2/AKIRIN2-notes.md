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

## Falcon deep research findings (2026-06-07)

A Falcon (Edison Scientific) deep research report was generated for AKIRIN2; the earlier note above (Falcon timed out) is now superseded for the transcription/immune arm. The report's mechanistic core overlaps with the existing review (nuclear adaptor; NF-kappaB-dependent transcription; SWI/SNF), but it adds named primary references and mechanistic specifics that were previously only implied via the UniProt summary. PMIDs below were resolved/confirmed via PubMed (search + metadata).

- CONFIRMS / NEW reference: AKIRIN2 acts as a molecular bridge linking NF-kappaB output to SWI/SNF (BAF/BRG1) chromatin remodelers, conferring *selective* (not global) induction of a subset of NF-kappaB target genes; Akirin-dependent promoters are enriched for lower CpG-island density. The conserved "molecular selector" mechanism (Akirin connecting Relish to the Osa/BAP60 SWI/SNF-like BAP complex; required for a subset of Relish-dependent effector genes, dispensable for negative-regulator genes) is from Drosophila but described as conserved to mammals [PMID:25180232 Bonnay et al. 2014 EMBO J "Akirins act as molecular selectors specifying the choice between subsets of NF-kappaB target genes"]. The mammalian B-cell/macrophage synthesis is reviewed in [PMID:28605346 Tartey & Takeuchi 2016 Crit Rev Immunol]. This adds primary-literature grounding for the existing GO:0003712 transcription coregulator activity and GO:0045944 annotations, which previously rested mainly on PMID:18066067.

- NEW reference (B-cell mechanism): Mouse Akirin2 is required for BRG1 (SWI/SNF) recruitment to Myc and Ccnd2 promoters after mitogenic (CD40/TLR/BCR) stimulation, supporting B-cell proliferation, survival, and T-dependent/independent humoral responses; Akirin2-deficient B cells show impaired cyclin D/c-Myc expression [PMID:26041538 Tartey et al. 2015 J Immunol "Brg1 recruitment to the Myc and Ccnd2 promoter was severely impaired in Akirin2-deficient B cells"]. This is the experimental primary support for the existing GO:0050871 positive regulation of B cell activation and GO:0002821 adaptive-immune annotations (previously IEA/ISS-only with PMID:18066067 as indirect support).

- NEW (disease link, provisional/association): Increased nuclear accumulation of Akirin-2 was reported in imatinib-resistant chronic myeloid leukemia (K562) cells, proposed as a candidate biomarker; notably the same study found NO direct NFkB-p65/Akirin-2 co-IP interaction in that system [PMID:29945498 Karabay et al. 2018 Hematology "increased Akirin-2 protein accumulation in the nucleus was shown for the first time in imatinib resistant CML cells"]. Association-level; not used to change any annotation.

- PROVISIONAL / not used for annotation: A 2024 chemoproteomics study lists AKIRIN2 Cys3 as a uniquely ligandable cysteine proximal to a 20S-proteasome-binding motif (Burton & Backus 2024, Commun Chem, doi:10.1038/s42004-024-01162-x). This is chemical-tractability data, not a function; consistent with the established proteasome-binding adaptor role but adds no GO annotation. Kept in notes only.

- PROVISIONAL / not used for annotation: A 2024 NRF2 transcriptomic meta-analysis reports AKIRIN2 as a *conditional* NRF2-responsive transcript (induced mainly under pharmacologic NRF2 activation, inconsistent across cancer cohorts) (Luo et al. 2024, Antioxid Redox Signal, doi:10.1089/ars.2023.0409). Expression-association only; does not establish direct NRF2 regulation of AKIRIN2. Kept in notes only.

Curation impact: The transcription/immune arm of the review is enriched with four genuine primary references (PMID:25180232, PMID:28605346, PMID:26041538, PMID:29945498) added as validation-safe statement-only entries. No proteasome-import (PN core) annotations are changed; the Falcon material is integrated as additional support for the already-present transcription-coregulator and immune-output annotations rather than as new GO terms. No annotation `action` values were altered.
