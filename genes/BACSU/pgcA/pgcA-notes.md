# pgcA (Bacillus subtilis 168, P18159) curation notes

## Deep research

`just deep-research BACSU pgcA --provider perplexity` was attempted on 2026-10-23 and
failed: the perplexity provider is not configured in this environment ("Provider
'perplexity' not available. Available: falcon, openscientist"). No deep-research file was
generated. These notes were compiled manually from cached publications and the UniProt record.

## Identity and family

- Phosphoglucomutase PgcA (YhxB; mutant alleles gtaC, gtaE), BSU09310, 581 aa (the original
  genome sequence contained deletions; corrected sequence AJ784890) [PMID:15640167 "the corrected nucleotide sequence with a 581-amino-acid coding capacity (accession number AJ784890 ) was considered the wild-type sequence"].
- PANTHER PTHR45745:SF1 (PHOSPHOGLUCOMUTASE 2B-RELATED). SF1 also contains yeast PRM15/PGM3
  (Q03262), S. pombe probable phosphoribomutase (O74478), S. aureus PgcA orthologs and
  Mycoplasma ManB proteins; SF2 holds vertebrate glucose-1,6-bisphosphate synthase (PGM2L1);
  SF3 holds vertebrate PGM2 phosphopentomutase [interpro/panther/PTHR45745/PTHR45745-entries.csv].
- Unlike E. coli Pgm (PTHR22573, PGM1-type), PgcA lacks the glucose-specific IPR005852 signature.

## Biochemistry

- Purified PgcA is active as a PGM, activated by 20 uM glucose 1,6-bisphosphate with 5 mM MgCl2
  [PMID:31589605 "Both PgcA and PgcA G47S were equally active in the PGM reaction, with indistinguishable kinetic parameters"].
- Secondary phosphoglucosamine mutase activity [PMID:31589605 "However, even native PgcA (with G47) has PNGM activity (~20-fold lower than PGM activity), and our results demonstrate that this functions in support of PG synthesis."];
  kcat/Km for GlcN-1-P is 9.38 mM-1 s-1 (WT) vs 40.14 (G47S). pgcA is synthetically lethal
  with glmR unless GlmM is overexpressed.

## Physiology

- Structural gene of alpha-PGM [PMID:15640167 "demonstrated that pgcA is the structural gene of α-PGM"];
  activity is measured in the soluble extract fraction.
- First step in UDP-glucose synthesis [PMID:15640167 "Since PgcA and GtaB catalyze successive steps in UDP-Glc synthesis"];
  UDP-Glc feeds Glc2-DAG (UgtP/YpfP; LTA anchor), WTA glucosylation (TagE) and the minor
  WTA. Phage phi29/rho11 resistance comes from the loss of glucosylated WTA.
- LTA poly(Gro-P) is NOT reduced in pgcA mutants [PMID:15640167 "The level of the poly(Gro-P) moiety of LTA was not affected in the pgcA- , gtaB- , and ypfP -deficient mutants"],
  so no lipoteichoic acid biosynthesis term was proposed. The glycolipid term
  (GO:0009247) is used instead, matching UniProt's curated pathway.
- Biofilm defect [PMID:15175311; PMID:15640167]: indirect, via UDP-Glc; no biofilm GO term proposed.
- Cell size: UgtP senses UDP-glucose to inhibit FtsZ [PMID:17662947, abstract does not name
  pgcA]; signalling consequence, not annotated.

## IBA rows from PTHR45745 (PAINT)

- PTN001860097 (root): GO:0008973 phosphopentomutase activity (IBD seeds SGD:S000004891
  PRM15 and UniProtKB:Q96G03 PGM2) and GO:0006166 purine ribonucleoside salvage (seed PRM15).
  PTN002907319 (vertebrate PGM2L1 clade) carries a NOT (IRD) for both, plus GO:0047933
  [interpro/panther/PTHR45745/PTHR45745-paint.tsv].
- Yeast data [PMID:23103740 "All tested enzymes were active on both substrates with Pgm1 exhibiting only residual activity on ribose-1-phosphate."; "but Pgm2 had a 2000 times higher preference for glucose-1-phosphate when compared to Pgm3."]:
  ribose-1-P activity is a shared, low-level property; PRM15 is a lineage specialist.
- PgcA has never been assayed on ribose 1-P. Decision: both IBA rows MARK_AS_OVER_ANNOTATED
  (not REMOVE), with propagation_review FUNCTIONAL_DIVERGENCE. For the PTHR45745 family
  review: consider whether the pentomutase IBD should be scoped to the eukaryotic
  PRM15/PGM2 lineages, or a NOT (IRD) added for the bacterial SF1 PgcA branch once
  substrate-specificity data exist.

## UniPathway ECA mapping defect

- P18159 carries "DR   UniPathway; UPA00894; -." with curated PATHWAY "Glycolipid metabolism;
  diglucosyl-diacylglycerol biosynthesis.", but GO gets GO:0009246 enterobacterial common
  antigen biosynthetic process (IEA:UniProtKB-UniPathway) [file:BACSU/pgcA/pgcA-uniprot.txt].
  B. subtilis has no ECA. MODIFY to GO:0009247; source_defect recorded (UNIPROT, CHECK).

## Curation decisions (summary)

- GO:0004614 IEA: ACCEPT (core).
- GO:0000287: KEEP_AS_NON_CORE.
- GO:0005975: MODIFY to GO:0019255; GO:0016868: MODIFY to GO:0004614.
- GO:0008973, GO:0006166 (IBA): MARK_AS_OVER_ANNOTATED.
- GO:0009246: MODIFY to GO:0009247 (+ source defect).
- NEW: GO:0120530 UDP-alpha-D-glucose biosynthetic process (IMP, PMID:15640167); GO:0008966
  phosphoglucosamine mutase activity (IDA, PMID:31589605, non-core); GO:0005737 cytoplasm
  (IDA, soluble extract activity, PMID:15640167).
