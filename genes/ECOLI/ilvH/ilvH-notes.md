# ilvH (P00894) — Escherichia coli K-12 — curation notes

Provider deep research was not run for this gene. These notes are drawn from
the cached publications in `publications/` (all relevant ones are
abstract-only) and the UniProt record (`ilvH-uniprot.txt`). IlvH is the
reference protein of the family review `interpro/panther/PTHR30239`.

## Three AHAS isozymes in E. coli K-12

- UniProt (P00894, MISCELLANEOUS): "E.coli contains genes for 3 AHAS isozymes:
  ilvBN, ilvGM and ilvIH." IlvBN is AHAS I, IlvGM is AHAS II and IlvIH is
  AHAS III [PMID:11243831 "AHAS III is one of three isozymes in Escherichia
  coli."].
- In K-12 only AHAS I and AHAS III are expressed: the curated UniProt entry
  for IlvG (P0DP90, MISCELLANEOUS, ECO:0000269 PubMed:7015336) states "In
  strain K12 only the Val-inhibitable ilvBN and ilvIH are expressed; ilvGM has
  a frameshift that disturbs the ilvG reading frame." (retrieved from the
  UniProt REST API during this review).
- ilvIH was recognised genetically as a distinct acetolactate synthase near
  leu [PMID:4612003 "This enzyme is the product of two genes, ilvH and ilvI,
  both located very close to leu."].

## IlvH is the small, regulatory subunit

- IlvI is the catalytic subunit; IlvI alone has 3-5% of holoenzyme activity
  and is valine-insensitive; IlvH is needed for full activity and valine
  sensitivity, and isolated IlvH binds valine [PMID:11243831 "The SSU
  (encoded by ilvH) associates with the large subunit and is required for full
  catalytic activity and valine sensitivity. The isolated SSU binds valine."].
- Valine-resistant (VAL^R) mutations map to the IlvH N-terminal ACT domain
  (N11A, G14D, N29H, A36V) without changing specific activity
  [PMID:11243831 "lead to a holoenzyme with drastically reduced valine
  sensitivity, but with a specific activity similar to that of the
  wild-type"].
- Genetic evidence: ilvH mutations make AHAS III valine-resistant, and an
  ilvH-containing extract makes purified IlvI enzyme valine-sensitive
  [PMID:4612003].
- AHAS III strongly prefers forming acetohydroxybutyrate (isoleucine route)
  over acetolactate; R = 40 [PMID:2675968].
- IlvH (163 aa) has an N-terminal ACT domain and a C-terminal domain (Pfam
  PF10369 ALS_ss_C), absent from the 96-aa IlvN; crystal structure 2F1F.

## Decisions (identical to ilvN where the evidence is the same)

- GO:0003984 (IBA, IDA PMID:2675968, IEA): MODIFY to GO:1990610, for the
  reasons given in `genes/ECOLI/ilvN/ilvN-notes.md` (complex-activity transfer;
  reconciles P. putida IlvH REMOVE and yeast ILV6 ACCEPT with
  contributes_to; PTHR30239 family review flags the node qualifier).
- GO:0009082 (IDA, IEA): MODIFY to L-valine + L-isoleucine biosynthetic
  process; GO:1901705 added as NEW.
- GO:0009099 rows (IBA, IDA, IEA, IMP): ACCEPT.
- GO:0005737 (ARBA): MODIFY to cytosol; cytosol IBA and IDA ACCEPT.
- GO:0005948 and GO:1990610: ACCEPT.
