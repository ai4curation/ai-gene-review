# UniProt: ITGB1–FLNB IPI pair cites the wrong PMID (digit transposition)

**Destination:** UniProt (uniprot.org update request), for the IntAct/UniProt
GO annotation.

**Summary.** Two reciprocal GO:0005515 IPI annotations, ITGB1 (P05556) with
FLNB (O75369) and the reverse, assigned by UniProt on 2006-03-16, cite
**PMID:10676904**. That PMID is "Effect of medium change on the development
of in vitro matured and fertilized bovine oocytes cultured in medium
containing amino acids" (J Vet Med Sci, 2000).

The intended paper is almost certainly **PMID:16076904**, "The Z-disc proteins
myotilin and FATZ-1 interact with each other and are connected to the
sarcolemma via muscle-specific filamins" (2005). The two numbers differ by a
transposition of the second and third digits.

**Evidence.**
- PMID:16076904 reports filamin "binding activity with the beta1A integrin
  subunit".
- UniProt cites it for "INTERACTION WITH FLNB AND FLNC" (P05556) and
  "INTERACTION WITH ITGB1" (O75369).
- The ITGB1–**FLNC** IPI row from the same date cites PMID:16076904
  correctly.

**Requested change.** Replace PMID:10676904 with PMID:16076904 on both rows.

**Repo references.** `genes/human/ITGB1/ITGB1-ai-review.yaml` (reference_review
`replacement`); `projects/MISCITATIONS.md`.
