# DHFR review notes

## Provenance

- The first `just deep-research-falcon human DHFR` attempt timed out; a later run
  completed and produced `DHFR-deep-research-falcon.md`. The review was drafted
  from the cached GOA references in `publications/`, the UniProt record, and the
  two founding disease papers (PMID:21310276, PMID:21310277, fetched with
  `just fetch-pmid`), then checked against the falcon report.

## Function

- Catalysis: recombinant human DHFR reduces dihydrofolate to tetrahydrofolate with
  NADPH [PMID:2303423 "kinetic scheme for recombinant human dihydrofolate reductase
  that correctly predicts full time course kinetics of the enzymatic reaction"].
- Nuclear thymidylate synthesis: DHFR joins SHMT1 and TYMS in a complex at the
  nuclear lamina [PMID:22235121 "this pathway forms a multienzyme complex that is
  associated with the nuclear lamina"].
- Tetrahydrobiopterin salvage: DHFR reduces 7,8-dihydrobiopterin, with low affinity
  in human endothelial cells [PMID:23707606 "is recycled back to BH₄ by dihydrofolate
  reductase (DHFR)"].
- Translational autoregulation by binding its own mRNA [PMID:8490020 "specific
  interaction between human recombinant DHFR protein and its corresponding DHFR mRNA"].
- Mitochondria: PMID:21876184 attributed mitochondrial reductase activity to the
  paralog DHFR2 (DHFRL1), but the falcon report summarizes a 2024 proteomic study of
  purified HEK293 mitochondria that found canonical DHFR and no DHFR2-specific
  peptide [file:human/DHFR/DHFR-deep-research-falcon.md "P00374-derived DHFR
  contributes mitochondrial reductase activity in the human cells tested"]. The
  mitochondrion annotations were therefore accepted; that 2024 paper is not yet in
  the local publication cache.

## Disease

- DHFR deficiency (constitutional megaloblastic anemia with severe neurologic
  disease): homozygous p.Asp153Val reduces DHFR activity and protein but not mRNA
  [PMID:21310277 "DHFR activity and fluorescein-labeled methotrexate (FMTX) binding
  were severely reduced in EBV-immortalized lymphoblastoid cells of all patients"];
  cerebral BH4 deficiency is part of the phenotype [PMID:21310276 "cerebral
  tetrahydrobiopterin deficiency due to a germline missense mutation in DHFR,
  resulting in profound enzyme deficiency"].
- This matches the dismech entry
  `Constitutional_Megaloblastic_Anemia_With_Severe_Neurologic_Disease`, which marks
  GO:0004146 dihydrofolate reductase activity and GO:0046654 tetrahydrofolate
  biosynthetic process DECREASED.

## 2026-10-20 ORGANELLES batch 1 (mitochondrion rows)

- GO:0005739 rows: HTP, IBA, IEA and ISS all stay ACCEPT. Before this batch the three synthesis rows shared one reason; each now has its own reason recording its check.
- IBA PTN000556119 (PTHR48069, Eukaryota) seeds: mouse Dhfr MGI:94890, rat Dhfr RGD:2500 and human DHFR2 Q86XF0. DHFR2 is a paralog, but the rodent seeds are canonical orthologues with IDA [PMID:25980602 "We demonstrate that dihydrofolate reductase activity is also a feature of the mitochondria in both rat and mouse but this is not due to a second enzyme."]. The human study assigns the mitochondrial activity to DHFR [PMID:38224738 "This data provides compelling evidence that DHFR (and not DHFR2) is the reductase activity in human mitochondria."]. So this is not a paralog over-transfer. The propagation_review is NO_FAILURE_NON_CORE.
- ISS from mouse P00375, which has IDA from PMID:25980602. The IEA (SL-0173) line is itself ECO:0000250 from P00375.
- Stayed at root. DHFR has no presequence and no TM segment. The only sub-mitochondrial result belongs to DHFRL1 [PMID:21876188 "Human DHFRL1, SHMT2, and TYMS were localized to mitochondrial matrix and inner membrane"], and the 2024 study revised that attribution, so the result cannot be transferred. That leaves fewer than two agreeing lines.
- New cached papers: PMID:25980602, PMID:21876188.
