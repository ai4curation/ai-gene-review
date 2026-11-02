# A0A2I4G8T1 (Juglans regia LOC109005703) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 prediction files were not opened or used.

Identity: TrEMBL A0A2I4G8T1, 488 aa, PE 3, single gene model shared by RefSeq
XP_018840292.1/XP_018840293.1/XP_018840295.1. Full-length family-1 UGT (Pfam PF26168 at
10-246 plus PF00201; PROSITE PS00375). Not an isoform or fragment: length matches the
490-496 aa Arabidopsis UGT73C proteins and the PSPG box is complete.

Evolutionary placement:
- PANTHER PTHR48047:SF229 (UDP-GLYCOSYLTRANSFERASE 73C3-RELATED). Arabidopsis SF229
  members are UGT73C3 (Q9ZQ96, AT2G36780) and UGT73C4 (Q9ZQ97); neither has experimental
  function data (UGT73C3 carries only ISM/IEA/IEP GO lines in UniProt).
- The IBA comes from PAINT node PTN008730368 (cached `interpro/panther/PTHR48047/PTHR48047-paint.tsv`),
  seeded by UGT89B1 (AT1G73880, SF8), UGT73C1 (AT2G36750, SF88), UGT73C6 (AT2G36790, SF153),
  UGT73C5/DOGT1 (AT2G36800, SF153), UGT73C7 (AT3G53160, SF77) and UGT89A2 (AT5G03490, SF209)
  — gene names checked against UniProt REST. The node spans UGT73C + UGT89, so the walnut
  protein is inside it. The previous review mislabelled AT1G73880 as UGT73C3; corrected.
- `A0A2I4G8T1-bioinformatics/RESULTS.md`: global identity is flat across UGT73C1-C6
  (57-59%), lower for UGT73C7 (55%), UGT73B1 (44%) and UGT89 (35-37%). Walnut is
  probably a co-ortholog of the Brassicales-expanded UGT73C cluster, so acceptor
  specificities of individual UGT73C members are not transferred.
- PSPG box 348-391 ends in Q (consistent with UDP-glucose donor use).

PANTHER family review `interpro/panther/PTHR48047/PTHR48047-review.yaml`: no
disagreement on subfamily placement (it records SF229 for this protein). It leaves the
family-wide scope of GO:0035251 UNRESOLVED; this gene-level review accepts the IBA for
this target only, which is consistent with that (target sits inside PTN008730368).

Deep research (`A0A2I4G8T1-deep-research-falcon.md`) found no literature on this gene and
discusses mainly UGT72 and UGT84A walnut/poplar enzymes, which are other subfamilies;
not used as support.

Actions: GO:0035251 IBA ACCEPT; GO:0008194 IEA MODIFY -> GO:0035251 (was KEEP_AS_NON_CORE);
GO:0016757 IEA MODIFY -> GO:0035251 (was MARK_AS_OVER_ANNOTATED, which wrongly implied doubt).
No NEW process terms: no substrate or pathway is established.

Modules: none in `modules/` cover UGT73C-type small-molecule glucosylation.

Relative to review next: Arabidopsis UGT73C5/DOGT1 (Q9ZQ94), a PTN008730368 seed in the
same UGT73C cluster and the best-characterized member (no review in repo). UGT73C3 (Q9ZQ96)
is the SF229 co-member but uncharacterized.
