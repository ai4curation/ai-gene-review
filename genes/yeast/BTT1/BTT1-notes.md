# BTT1 curation notes

## 2026-10-01 update: GOA refresh and PTHR10351 IBA review

- Refreshed BTT1 from QuickGO and UniProt. Current GOA has 12 rows. The refresh added two live source rows to review: a ComplexPortal IPI row for `GO:0005854 nascent polypeptide-associated complex` from PMID:26618777 and a second SGD IGI row for `GO:0006613 cotranslational protein targeting to membrane` from PMID:10518932 with `SGD:S000005958` as the interacting gene.
- The following five exact source rows are absent from current GOA and were preserved as retired rows rather than silently dropped: `GO:0015031 protein transport` / IEA / GO_REF:0000043; three old `GO:0005515 protein binding` IPI rows from PMID:11283351, PMID:16554755, and PMID:37968396; and `GO:0051082 unfolded protein binding` / IMP / PMID:10219998.
- Re-read cached PTHR10351 PAINT. Both live IBA rows, `GO:0005854 nascent polypeptide-associated complex` and `GO:0005829 cytosol`, trace to `PANTHER:PTN000039173`, a eukaryotic NAC-beta node seeded by fly, fission yeast, budding yeast, and human descendants. Both transfers are sound for Btt1's conserved ribosome-associated NAC-beta role.
- Searched for newer BTT1/NAC papers. PMID:39426497 is directly relevant and identifies the Btt1/Nacbeta2 residues required for Caf130 binding and Rpl4/Acl4-linked CCR4-NOT recruitment. PMID:38177147 is a useful boundary paper: btt1 deletion has only a slight mitophagy phenotype compared with egd1 deletion, so it does not support adding mitophagy as a BTT1 process term.
