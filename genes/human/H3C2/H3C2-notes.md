# H3C2 (histone H3.1) review notes

## Provenance / process

- 2026-10-04: `just fetch-gene human H3C2` failed repeatedly against the UniProt
  search endpoint (502/503); succeeded with the accession pinned (`-u P68431`).
- H3C2 does not have its own UniProt entry: P68431 (H31_HUMAN, "Histone H3.1") is
  shared by the ten identical-protein genes H3C1, H3C2, H3C3, H3C4, H3C6, H3C7, H3C8,
  H3C10, H3C11 and H3C12. GOA annotations are therefore protein-level (P68431) and
  apply equally to all of them.
- Deep research could not be generated: falcon (Edison) returned `402 Payment
  Required` (and timed out on a first attempt), perplexity-lite is not configured,
  and the OpenAI key returned `401 invalid_api_key`. The review is based on the
  UniProt record and the 57 cached publications.

## Biology summary

- Core component of the nucleosome [file:human/H3C2/H3C2-uniprot.txt "Core component of nucleosome."].
- Octamer of two each of H2A, H2B, H3, H4 wraps ~146-147 bp DNA
  [PMID:21636898 "In the nucleosome, two copies of each core histone, H2A, H2B, H3 and H4, form a histone octamer which wraps 146 base pairs of DNA around itself."].
- H3.1 is the replication-coupled variant, deposited by CAF-1; H3.3 by HIRA
  [PMID:14718166 "Deposition of the major histone H3 (H3.1) is coupled to DNA synthesis during DNA replication and possibly DNA repair"].
- H3 and H4 are handled as dimers
  [PMID:14718166 "these complexes possess one molecule each of H3.1/H3.3 and H4, suggesting that histones H3 and H4 exist as dimeric units that are important intermediates in nucleosome formation"].
- H3.1 vs H3.3 chaperone discrimination at residue 89 (Val in H3.1)
  [PMID:25615412 "the H3.3 Ile89 residue, corresponding to the H3.1 Val89 residue, is responsible for the tNASP-mediated nucleosome assembly with H3.3"].
- Variant-specific PTM profiles [PMID:16267050 "quantitative mass spectrometry analysis of human H3.1, H3.2, and H3.3 showed modification differences between these three H3 variants, suggesting that they may have different biological functions"].

## Curation decisions (summary)

- ACCEPT: nucleosome (all evidence), structural constituent of chromatin, nucleosome
  assembly, chromatin organization, nucleus/chromatin/chromosome/nucleoplasm
  (including the 84 Reactome nucleoplasm TAS rows), DNA binding, protein
  heterodimerization activity.
- protein binding (83 rows): H4 partners -> MODIFY to GO:0046982 protein
  heterodimerization activity (H3-H4 histone-fold dimer). All others REMOVE as
  uninformative: partners are histone chaperones (H3 is cargo), tail readers or
  modifying enzymes (H3 is ligand/substrate; the activity belongs to the partner), or
  high-throughput screen hits (histones are frequent non-specific co-purifiers).
- KEEP_AS_NON_CORE: extracellular region (Reactome, extracellular nucleosomes/NETs),
  epigenetic regulation of gene expression, telomere organization, generic
  protein-containing complex.
- MARK_AS_OVER_ANNOTATED: extracellular exosome (HDA, ComplexPortal IPI), membrane (HDA).
- REMOVE: cadherin binding (HDA; E-cadherin interactome co-purification).
