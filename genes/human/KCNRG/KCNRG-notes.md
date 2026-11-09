# KCNRG notes

## 2026-11-05 ORGANELLES ER batch 2 (endoplasmic reticulum rows)

- Rows: GO:0005783 IBA (is_active_in), IEA GO_REF:0000044 and IDA PMID:19968958, all ACCEPT and core; no ER sub-compartment row.
- IBA: PAINT node PTN002684174 (PTHR14499, taxon:117571) has a single IBD seed, UniProtKB:Q8N5I3 (KCNRG itself) [interpro/panther/PTHR14499/PTHR14499-paint.tsv]. Target among its own seeds is expected.
- IEA: UniProt "Endoplasmic reticulum {ECO:0000269|PubMed:19968958}" with no sub-location [file:human/KCNRG/KCNRG-uniprot.txt].
- PMID:19968958 is abstract only: [PMID:19968958 "Our data indicates that KCNRG is an ER-associated protein, which we propose regulates Kv1 family channel proteins by retaining a fraction of channels in endomembranes."]
- is_active_in: the proposed activity (retaining Kv1 channels in endomembranes) acts at the ER; defensible, but an abstract-level proposal.
- KCNRG is a soluble BTB/T1 protein without a signal peptide or TM segment: ER-associated on the cytosolic face, stays at root.
- Outcome: root; all three rows stay ACCEPT, reasons record the check.
