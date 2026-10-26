# FASTKD2 review notes

## Scope and evidence

This review covers the 31 imported GOA contexts without altering their source fields or order. It retains 25 reference records, two curated UniProt products and no supporting-text quotations. The [direct evidence guide](FASTKD2-source-guide.md), [database evidence guide](FASTKD2-database-source-guide.md) and [four interaction records](FASTKD2-binding-records.yaml) record source access and assay limits.

The integrated decisions are 21 ACCEPT, 7 KEEP_AS_NON_CORE, 1 TOO_GENERAL and 2 UNDECIDED. The two nucleoid records describe the same partial localization and are both non-core. This preserves the positive observation from PMID:25683715; it does not infer DNA binding or absence from the nucleoid region. The precise matrix assignment in PMID:27974379 remains source-specifically uncertain, while independent curated matrix inferences are retained. The transferred RNA-modification claim remains unresolved because association and PTCD1/synthase perturbations do not isolate FASTKD2's contribution to the chemical-modification step.

## Core synthesis

One RNA-binding activity covers rRNA and mRNA substrates. Human experiments support mitochondrial RNA maturation and large-subunit assembly (PMID:25683715; PMID:26370583). The ancestral mRNA-stability assertion is retained with its actual PAINT placement and donor experiments; FASTKD2's ND6 contact and abundance phenotype do not by themselves resolve direct decay from secondary assembly defects (PMID:27789713; PMID:28335001; PMID:29617655). Mitochondrial translation is supported as a process annotation through RNA handling and assembly, without inventing a separate catalytic translation activity. No kinase, autonomous nuclease, pseudouridine-synthase or ribosomal structural activity is assigned.

The RNA-granule term is a cellular location rather than a protein-containing complex. The human module study describes largely monomeric migration and transient RNA-associated interactions (PMID:27974379); no stable obligate holocomplex is asserted. Organelle-level mitochondrial annotations remain informative alongside matrix and granule evidence.

## Products and processing

Official UniProt and sequence reconstruction identify products Q9NYY8-1 (710 residues) and Q9NYY8-2 (648 residues). The second has the curated C-terminal replacement/deletion, not a measured alternative mitochondrial cleavage. Three captured RefSeq proteins match the first product. The captured Ensembl transcript models are distinguished from experimentally resolved protein products; sequence identity is not asserted for untested translations. UniProt leaves the transit-peptide endpoint and mature-chain start unresolved. Experimental tags and predicted targeting coordinates do not establish a mature product boundary.

## Research availability

The configured automated research providers failed authentication/quota checks, and no provider report was fabricated. The review instead uses genuine primary publications and database records with the access limits described in the evidence guides. A publication's committed normal cache may remain abstract-only even when the original article was recovered and read separately. Questions and proposed experiments are scoped to the inspected evidence rather than claims that no relevant work exists anywhere.

## Current-literature check

A bounded current search located [PMID:41994142](https://pmc.ncbi.nlm.nih.gov/articles/PMC13082123/), a Research Square preprint (2026-04-07, version 1; DOI 10.21203/rs.3.rs-8605748/v1). Its original Results, relevant Discussion and RNA-assay Methods were inspected. The glioma-cell study reports FASTKD2/YTHDF2 association with 12S rRNA (MT-RNR1) and altered distribution of that RNA in tumour microtubes. This is distinct from the ND6-mRNA mechanism discussed above. The Results assign the MT-RNR1 stability perturbation to YTHDF2, while the RNA-stability Methods name FASTKD2 siRNA; this discrepancy remains unresolved in the inspected text. The preprint therefore does not establish isolated FASTKD2-dependent ND6 decay or settle the modification-module question. Its context-specific transport and drug-mechanism claims are not promoted to core functions or new GO assertions here. Figures, supplements and the drug-screen evidence were not independently adjudicated. The genuine source remains in the private research record; existing publication caches are unchanged.
