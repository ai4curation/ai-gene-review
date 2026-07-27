# treSB curation notes

- Q88FN0 is a 1106-aa fusion with TreS/GH13 and maltokinase domain signatures. [file:PSEPK/treSB/treSB-uniprot.txt, "DR   InterPro; IPR012810; TreS/a-amylase_N."] [file:PSEPK/treSB/treSB-uniprot.txt, "DR   InterPro; IPR012811; TreS_maltokin_C_dom."]
- The TreS reaction is D-maltose to alpha,alpha-trehalose (EC 5.4.99.16; RHEA:15145). [file:PSEPK/treSB/treSB-uniprot.txt, "Reaction=D-maltose = alpha,alpha-trehalose"]
- The distinct maltokinase reaction is D-maltose + ATP to alpha-maltose 1-phosphate + ADP + H(+) (EC 2.7.1.175; RHEA:31915). [file:PSEPK/treSB/treSB-uniprot.txt, "Reaction=D-maltose + ATP = alpha-maltose 1-phosphate + ADP + H(+)"]
- The seeded GOA represents only the TreS activity. A NEW generic kinase annotation and a proposed substrate-specific maltokinase term were added so the fusion is not curated as monofunctional.
- PTHR10357 PAINT supports GO:0047471 at a bacterial ancestral node, but Q88FN0 is absent from the local PTHR10357 member snapshot; this was used only as family-level corroboration. [file:interpro/panther/PTHR10357/PTHR10357-paint.tsv, "PTN000039847"]
- No target-specific biochemical publication was present in the local publication cache. No whole-pathway process was inferred beyond the seeded broad carbohydrate-metabolism annotation.
