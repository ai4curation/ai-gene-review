# Slc12a1 (rat, F7EUW9) review notes

## 2026-10-28 session

- `just fetch-gene rat Slc12a1` timed out on the UniProt gene_exact search (3 attempts); re-ran
  with `--uniprot-id F7EUW9`, which succeeded. Fetched record is F7EUW9 (RGD:3685, GeneID 25065),
  GOA file keyed to F7EUW9 (11 IEA rows). No accession switch.
- F7EUW9 is the TrEMBL entry from MGC cDNA (AAH87017.1). The Swiss-Prot entry P55016 (S12A1_RAT)
  is the same gene (RGD:3685, same length) and carries all the experimental rat annotations
  (EXP PMID:8021284 for GO:0008511; IDA PMID:19592485 for apical plasma membrane and cell surface;
  IDA PMID:16275913 for renal sodium ion absorption). This review treats the experimental literature
  on rat NKCC2 as applying to F7EUW9.
- All 11 GOA rows are IEA (InterPro2GO, ARBA, SubCell mapping, inter-ontology). None are wrong;
  the generic ones (membrane, plasma membrane, transmembrane transporter activity, ion transport,
  transmembrane transport, potassium ion transmembrane transporter activity, chloride:cation
  symporter activity) were MODIFIED toward the specific supported terms
  (GO:0008511 sodium:potassium:chloride symporter activity; GO:0016324 apical plasma membrane;
  GO:0035725/GO:0071805/GO:1902476 ion transmembrane transport).
- NEW: GO:0008511 (IDA-equivalent evidence: oocyte flux, PMID:8021284; PMID:16291577) and
  GO:0070294 renal sodium ion absorption. NKCC2 performs the apical Na+ entry step of TAL NaCl
  reabsorption itself (it is the transporter, not a substrate), and comparators in the same role
  (SLC12A3/NCC, CLCNKB, and the Swiss-Prot rat entry P55016 itself) carry this term. [Corrected 2026-10-28: CLCNKB, a basolateral Cl- exit channel, is not in the same role; it also carries the term but is not a comparator.] [Corrected 2026-10-28: ENaC was wrongly listed here; see dated note below.]
- Did not add regulatory / phenotype process terms (urine concentration, blood pressure) - these
  rest on knockout/disease phenotypes rather than a specific step NKCC2 performs at the level of
  those processes beyond NaCl uptake.
- Key paper PMID:19592485 (full text, rat TAL): apical surface NKCC2 by biotinylation and
  extracellular-epitope immunolabelling, cAMP/PKA-stimulated exocytic insertion.

## 2026-10-28 review-fix pass

- Corrected the GO:0070294 comparator claim. A QuickGO exact-term query (GO:0070294, taxa 9606,
  10090, 10116; 111 annotations) returns NKCC2/Slc12a1, NCC/SLC12A3, CLCNKB, KCNQ1, KCNJ1, the
  WNK/SPAK/OSR1/KLHL3 regulators, endothelin pathway genes and others, but no SCNN1A, SCNN1B or
  SCNN1G row in any of the three species. The review and these notes previously said ENaC carries
  the term; that statement was wrong and has been removed (the Scnn1a review was right). The NEW
  action on the Slc12a1 row is unchanged.
