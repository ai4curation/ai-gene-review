# trhO (P24188) review notes

E. coli K-12 TrhO (formerly YceA / ORF39.9), tRNA uridine(34) hydroxylase. 350 aa, rhodanese
family (Pfam Rhodanese PF00581 + Rhodanese_C PF12368 + UPF0176_N), HAMAP MF_00469 (TrhO family).
Active-site cysteine C200 in a CTGGIR loop.

## Literature search (2026-11-24)

No deep-research file; searched PubMed directly.

- `TrhO tRNA hydroxylation ho5U` -> PMID:31253794 (the defining paper; Sakai, Suzuki et al.
  Nat Commun 2019, full text cached).
- GOA interaction rows cite PMID:15690043 (Butland TAP network) and PMID:19402753 (Hu/Emili
  global functional atlas), both high-throughput, partner RplL (L7/L12, P0A7K2).
- PMID:1840644 is the original sequencing paper that named orf39.9 adjacent to htrB; background
  only (abstract cached).

## Key findings

- TrhO (YceA) and TrhP together make ho5U34, the first step of (m)cmo5U34 wobble-uridine
  modification [PMID:31253794 "two genes, trhP and trhO, which are responsible for formation of
  ho5U at the initial step of xo5U biogenesis at the wobble position of bacterial tRNAs"].
- TrhO is a rhodanese-family protein that catalyses oxygen-dependent ho5U34 formation under
  aerobic conditions [PMID:31253794 "TrhO, a rhodanese family protein, catalyzes oxygen-dependent
  ho5U34 formation under aerobic conditions"]; molecular O2 is the source of the hydroxyl oxygen
  [PMID:31253794 "demonstrating that trhO-mediated tRNA hydroxylation utilizes O2 as an oxygen
  atom donor"].
- In vitro reconstitution: recombinant TrhO forms ho5U on tRNASer1 transcripts; up to 75% with
  excess enzyme [PMID:31253794 "successfully detected ho5U on tRNASer1 in the presence of
  recombinant TrhO"]. EMSA shows TrhO binds tRNAAla1 but not tRNALeu3 (substrate specificity).
- Active-site residues C200/T201/G203/R205 essential (mutagenesis); the UniProt record notes a
  cysteine persulfide intermediate (ACT_SITE 200), consistent with rhodanese chemistry.
- Single deletion has only a slight ho5U reduction (trhP is dominant); the double trhP/trhO
  deletion abolishes cmo5U and is temperature-sensitive and translation-impaired (UniProt
  DISRUPTION PHENOTYPE, PMID:31253794).

## RHEA backing (staged RHEA:64224 -> broadMatch GO:0016705)

- RHEA:64224 = uridine(34) in tRNA + AH2 + O2 = 5-hydroxyuridine(34) in tRNA + A + H2O. This is
  paired-donor/O2 monooxygenase chemistry. GO:0016705 (oxidoreductase, acting on paired donors,
  with incorporation or reduction of molecular oxygen) is the correct broad class, and the GOA
  already carries GO:0016705 by IDA and IEA. The review ACCEPTs GO:0016705 (IDA) -> staged row
  BACKED. No specific "tRNA uridine(34) hydroxylase activity" term exists (OLS search for
  "tRNA 5-hydroxyuridine" returns nothing relevant); proposed as NTR.
- Mechanistic caveat: the reaction uses a generic reductant AH2 + O2 (an external-monooxygenase
  formulation). TrhO is a rhodanese-fold enzyme with an active-site Cys persulfide, so the in
  vivo reductant/mechanism is not a classic Fe/2-OG dioxygenase; but GO:0016705 is a
  mechanism-agnostic "paired donors + O2" class, so the broad match is still appropriate.

## Curation decisions

- GO:0016705 (IDA PMID:31253794, IEA): ACCEPT the IDA (direct reconstitution), ACCEPT the IEA.
  Core MF. Most specific existing term; NTR "tRNA uridine(34) hydroxylase activity" proposed.
- GO:0016491 oxidoreductase activity (IBA, IDA): TOO_GENERAL — the root oxidoreductase term is
  subsumed by GO:0016705 which is asserted here and is a real, specific class.
- GO:0002098 tRNA wobble uridine modification (IBA, IMP): ACCEPT. TrhO performs the hydroxylation
  step of wobble-U34 modification (ho5U34 is the first step of cmo5U34). Participation test met
  (TrhO does the chemistry). It is the correct specific BP (position 34 / wobble).
- GO:0006400 tRNA modification (IDA, IEA): parent of GO:0002098; TOO_GENERAL once the wobble term
  is accepted.
- Protein binding GO:0005515 (two IPI rows, partner RplL/L7-L12): REMOVE per protein-binding
  policy; high-throughput, no functional meaning (L7/L12 is a sticky ribosomal protein, common
  false positive). TrhO acts on tRNA, not on L7/L12.
