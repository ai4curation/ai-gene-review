# BAZ2A notes

## 2026-10-05 review (PAINT, affinage)

- TIP5/NoRC: [PMID:11532953 "The cellular TIP5-SNF2h complex, termed NoRC (nucleolar remodeling complex), induces nucleosome sliding in an ATP- and histone H4 tail-dependent fashion."]. pRNA binding (mouse): PMID:16678107.
- Most mechanistic rows are ISS from mouse Tip5, and they are accepted.
- Over-annotated: DNA-templated transcription and nuclear receptor binding (NAS from the family-discovery paper), and RNA pol I preinitiation complex assembly (an IEA derived from the promoter-binding row, which inverts the direction).
- Removed 4 GO:0005515 rows (mouse Ttf1, NCK1, BEND3, USP21).
- PMID:28801535 says BAZ2A only "possibly" stimulates SMARCA5 ATPase, so ATPase activator activity is not asserted.

## 2026-10-05 PR 4374 follow-up

- GO:0003712 was too broad for a row whose support describes repressive NoRC targeting; the row now modifies to GO:0003714 transcription corepressor activity.
- GO:0006355 was made consistent with the sibling NAS rows from PMID:10662543 by modifying the generic transcription-regulation parent to GO:0016479 negative regulation of transcription by RNA polymerase I.
- Affinage had surfaced a set of relevant BAZ2A primary papers that were missing from the review. PMID:34715126 directly supports human TAM-domain dsDNA and dsRNA binding; PMID:25916849 maps the human TAM RNA-binding surface; PMID:25533489 shows the human PHD finger reads unmodified H3 and the bromodomain prefers KacXXR acetyl marks; PMID:34403195 shows human BAZ2A-BRD binding H3K14ac at inactive enhancers; PMID:37184661 links TAM, RNA, TOP2A and KDM1A to Pol II enhancer-gene repression distinct from rDNA silencing; PMID:33433018 supports a related BAZ2A/TOP2A/cohesin arm in mouse ESCs.
- GO:0042393 and GO:0140046 now avoid using the PIH1 abstract as if it directly demonstrated TIP5-H4 binding; the original IPI row is retained, but the human TIP5 reader-domain paper is used as the accessible support.
- GO:0031507 heterochromatin formation is retained as non-core because the child GO:0000183 rDNA heterochromatin formation carries the specific core rDNA claim.
