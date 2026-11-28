# ROCK2 notes

Per-provider deep research was attempted for ROCK1 with `perplexity`, but the local deep-research client reported that only the unavailable `claude_code` provider was installed. This family-slice review therefore uses the fetched UniProt, GOA, Reactome, PAINT and PMID caches as the evidence base.

ROCK2 is the second human ROCK isoform in the PTHR22988 AGC kinase family slice. Manual review should keep isoform-specific ROCK2 rows separate from ROCK1, while retaining the shared RhoA-regulated serine/threonine kinase activity and actomyosin/cytoskeleton outputs that both paralogs support.

## Curation summary

The completed review keeps ROCK2's serine/threonine kinase rows, Rho-dependent kinase and signaling rows, direct actomyosin and cytoskeletal outputs, and supported nuclear, centrosomal, cytoplasmic and plasma-membrane localization rows. Broad protein-binding rows were removed under the protein-binding policy, the HCV perturbation row was marked as over-annotated, and amyloid, endothelial-barrier and other context rows without direct accessible support for the exact human ROCK2 claim were left `UNDECIDED`.

## 2026-11-28 follow-up

- PMID:24305806 full text from PMC3850036 contains the BACE1 peptide kinase assay that is missing from the local abstract-only cache: "synthetic peptides comprising BACE1 amino acids 485-501 were incubated in the presence or absence of recombinant ROCK2 protein"; LC-MS/MS then "indicated that ROCK2 can phosphorylate BACE1 S498." This supports retaining the BACE1 `GO:0002020` IPI row as a non-core protease-substrate contact.
