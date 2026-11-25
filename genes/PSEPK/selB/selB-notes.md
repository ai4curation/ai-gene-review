# selB review notes

- Q88QJ7 is an unreviewed but strongly classified bacterial
  selenocysteyl-tRNA-specific elongation factor with a Tr-type GTPase domain and
  multiple SelB-specific winged-helix domains. [file:PSEPK/selB/selB-uniprot.txt
  "SubName: Full=Selenocysteyl-tRNA-specific translation elongation factor"]
  [file:PSEPK/selB/selB-uniprot.txt
  "InterPro; IPR004535; Transl_elong_SelB."]
- PANTHER/PAINT places SECIS binding and selenocysteine incorporation on the
  bacterial SelB clade node PTN000562733 of PTHR42854, seeded by E. coli SelB.
  [file:interpro/panther/PTHR42854/PTHR42854-paint.tsv
  "PTHR42854	PTN000562733	GO:0035368	F	IBD	false	UniProtKB:P14081"]
  Q88QJ7 is not a descendant of that node (it is HMM-classified in PTHR43721:SF9 and
  is not a PANTHER tree leaf); the stale PTHR43721 copy of the row has no leaves. The
  SECIS-binding refinement therefore rests on the NCBIfam SelB model, the two SelB
  winged-helix Pfam domains and the E. coli ortholog (PMID:9454578).
- Generic RNA binding was narrowed to SECIS binding, and generic translational
  elongation was narrowed to selenocysteine incorporation.
- Review boundary: SelB delivers already synthesized Sec-tRNA(Sec). It does not
  make the charged tRNA and is not assigned any catalytic or physiological
  function of the downstream selenoprotein.
