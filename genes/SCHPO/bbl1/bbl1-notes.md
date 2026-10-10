# bbl1 (SPBC13A2.03, UniProt Q9P381) notes

## Identity and naming
- UniProt Q9P381 (CDS1_SCHPO), "Putative phosphatidate cytidylyltransferase", EC 2.7.7.41, CDS family, ER membrane multi-pass [UniProt:Q9P381].
- PomBase symbol is bbl1 because S. pombe `cds1` is the checkpoint kinase (genes/SCHPO/cds1 is that gene). UniProt gives no gene name (ORF SPBC13A2.03 only), so `just fetch-gene SCHPO bbl1` failed; fetched by accession with `-u Q9P381`.
- The name comes from the S. japonicus "bubble1" mutant [PMID:25318672 "prompting us to name it bubble1 (bbl1; Figure 1A)"]; the paper calls the S. pombe gene cds1.

## Function
- ER-resident CDS: "cycling cells deficient in the function of the ER-resident CDP-DG synthase Cds1 exhibit markedly increased triacylglycerol content" [PMID:25318672].
- S. pombe ts allele: "The CDP-DG synthase activity was markedly decreased in cds1-9 cells at 36°C (Figure 5B)." [PMID:25318672]
- Loss of CDS diverts PA to TAG: "interfering with the CDP-DG route of phosphatidic acid utilization rewires cellular metabolism to adopt a triacylglycerol-rich lifestyle reliant on the Kennedy pathway" [PMID:25318672].
- 1992 extract study measured CDP-DG synthase regulation by growth phase, inositol, choline [PMID:1324908 "the membrane-associated phospholipid biosynthetic enzymes CDP-DG synthase, phosphatidylglycerolphosphate (PGP) synthase"] (pre-cloning; abstract-only).

## Review decisions
- MF/BP CDS and CDP-DAG biosynthesis: ACCEPT (EXP, IBA, IDA, IEA).
- Lipid droplet formation (IBA from mammalian CDS1/2): KEEP_AS_NON_CORE, indirect, matching S. cerevisiae CDS1 review.
- GO-CAM 6796b94c00000009: bbl1 GO:0004605 in ER membrane, part of GO:0016024 - consistent.
