# Ptpn11 (rat) review notes

- 2026-10-28: fetched P41499 (Swiss-Prot, RGD:3447, GeneID 25622); 135 GOA rows. Human PTPN11 review
  used as a consistency reference.
- PMID:17662049 (full text) read: rat RBE4 endothelium, PECAM-1 cross-linking recruits SHP-2
  [PMID:17662049 "Following PECAM-1 antibody cross-linking, we consistently observed a robust tyrosine
  phosphorylation of PECAM-1 and its interaction with SHP-2"]. The dominant-negative experiments were in
  human HBMECs. Used as support for cell adhesion molecule binding; no NEW process term added from it.
- Core MF chosen: GO:0004726 non-membrane spanning PTP activity; GO:0004725 and GO:0004721 rows modified
  to it. Added NEW GO:0035335 peptidyl-tyrosine dephosphorylation (SHP2 is the enzyme; rat IDA).
- Protein-binding rows MODIFIED to phosphotyrosine residue binding, RTK binding or PTK binding by partner.
- Mouse acts_upstream phenotype rows (metabolism, hormone secretion, platelets, cerebellum, growth) marked
  over-annotated; developmental Noonan-related rows kept non-core.
- Smooth muscle cell proliferation IEP row modified to positive regulation of vascular SMC proliferation;
  source_defects entry recorded.
- Insulin receptor binding IDA (PMID:7711057): abstract only shows the insulin receptor kinase domain as a
  PTP substrate, not binding; kept non-core with caveat, question raised.
- Mitochondrial Shp-2 (PMID:15378208) is not annotated in GOA as a CC; not added (single line of
  evidence, abstract only).
