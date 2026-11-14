# imt3 notes

## PTHR32385 / IPC mannosyltransferase review, 2026-11-06

- `SPAC17G8.11c` is `imt3`, one of three S. pombe SUR1 homologues that
  catalyze Golgi conversion of IPC to MIPC.
- PANTHER `PTHR32385` is the fungal GT32 IPC mannosyltransferase family.
  `Q10323` sits in `PTHR32385:SF20`, the same CSH1-related subfamily as S.
  pombe Imt2 and S. cerevisiae Sur1/Csh1.
- The `GO:0000030` IBA from `PANTHER:PTN001285482` is inherited from the right
  node, but it is the generic parent of `GO:0103064 inositol phosphorylceramide
  mannosyltransferase activity`. SPAC17G8.11c lacks the exact MF row in GOA, so
  the parent is too broad and the exact activity is proposed as a `NEW` ISO
  assertion from the same orthologous yeast enzymes that seed PAINT.
- The `GO:0051999` IBA from `PANTHER:PTN001285482` is sound. The node is seeded
  by all three S. pombe Imt paralogs plus A. fumigatus MitA and orthologous
  SGD/CGD MIPC synthases, and Nakase et al. showed that the imt1 imt2 imt3
  triple disruptant lacks MIPC and accumulates IPC.
- The 2006 ORFeome screen reported high-throughput Golgi and ER localization
  for SPAC17G8.11c. The 2010 direct imt1/imt2/imt3 paper localized GFP-Imt3p
  to Golgi membranes, so the Golgi rows are core and the ER/ER-membrane rows
  are retained as non-core.
- The newer 2023 Willet et al. study found that imt3 deletion suppresses the
  css1-3 growth and cell-wall-material accumulation phenotypes. That result
  suggests Imt3-specific MIPC subspecies may be especially important to
  regulate, but it does not justify annotating imt3 directly to cell-wall
  assembly or plasma-membrane lipid organization processes.
