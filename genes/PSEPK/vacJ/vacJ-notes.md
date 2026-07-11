# vacJ notes

2026-07-09 PDT / 2026-07-10 UTC: First-pass cell-envelope/division
VacJ/MlaA singleton curation. `vacJ` did not resolve through `just fetch-gene`
by symbol or ordered locus, so the review was seeded with the known UniProt
accession Q88KX6 and alias `vacJ` through the lower-level fetch helper. UniProt
names the protein VacJ lipoprotein, records the MlaA family, and assigns MlaA
domain/family evidence [file:PSEPK/vacJ/vacJ-uniprot.txt "DE   SubName:
Full=VacJ lipoprotein"; file:PSEPK/vacJ/vacJ-uniprot.txt "CC   -!-
SIMILARITY: Belongs to the MlaA family."; file:PSEPK/vacJ/vacJ-uniprot.txt "DR
InterPro; IPR007428; MlaA."]. Asta was retrieval only and confirmed the same
product/domain signal [file:PSEPK/vacJ/vacJ-deep-research-asta.md "- **Key
Domains:** MlaA. (IPR007428); MlaA (PF04333)"].

Decision: accept membrane localization and intermembrane phospholipid transfer
as first-pass MlaA/VacJ-family annotations. Keep the location as generic
membrane because the fetched GOA/UniProt record does not provide a more
specific GO location; represent vacJ as an MlaA-family context extension of the
existing `mla_phospholipid_transport_boundary` module.
