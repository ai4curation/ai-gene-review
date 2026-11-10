# ptsN / EIIA(Ntr) (E. coli K-12, P69829) notes

## Provenance

- Deep research could not be generated: no deep-research provider API key is
  configured in this session, so `just deep-research ECOLI ptsN` was not run and no
  `-deep-research-*.md` file exists. The review is based on the UniProt record, the
  GOA table and the cached publications PMID:7876255, PMID:17289841, PMID:19400808
  (abstracts), PMID:18304323 and PMID:24561554 (full text).

## Findings

- Dephosphorylated IIA(Ntr) binds TrkA and limits K+ accumulation [PMID:17289841
  "We demonstrate that dephosphorylated EIIA(Ntr), but not its phosphorylated form,
  forms a tight complex with TrkA that inhibits the accumulation of high
  intracellular concentrations of K(+)."].
- IIA(Ntr) binds KdpD and stimulates its kinase activity [PMID:19400808 "Two-hybrid
  data and biochemical analysis revealed that IIA(Ntr) interacts with sensor kinase
  KdpD and stimulates kinase activity, resulting in increased levels of
  phosphorylated response regulator KdpE."].
- In P. putida the PtsN-KdpD interaction represses kdpFABC (PMID:26224366, see the
  PSEPK ptsN review), so the direction of KdpD regulation is lineage-dependent.

## Curation decisions

- InterPro2GO maps IPR006320 (PTS_Nitro_regul, the nitrogen-regulatory IIA family
  itself) to sugar-PTS terms; both rows are removed and recorded as source defects.
- enzyme inhibitor activity (TrkA) is refined to transporter inhibitor activity:
  TrkA is the regulatory subunit of a K+ transporter, not an enzyme.
- The bare protein-binding rows are replaced by the regulatory activities each paper
  shows; the large-scale yeast two-hybrid row (PMID:24561554) is removed.
