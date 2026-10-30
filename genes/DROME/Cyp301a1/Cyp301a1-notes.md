# Cyp301a1 notes

## 2026-10-28 initial review
- fetch-gene resolved Q9V6D6 (Swiss-Prot CP301_DROME, FlyBase FBgn0033753, GeneID 36378); 6 GOA rows.
- Key paper PMID:22574182 (Sztal 2012) cached with full text and read.
- GOA: 4 InterPro IEA MF rows (monooxygenase, iron ion binding, 16705 paired donors, heme binding),
  1 SubCell IEA CC (mitochondrial membrane), 1 FlyBase IMP BP (tergite morphogenesis, GO:0007490).
- Decisions:
  - Monooxygenase / GO:0016705: ACCEPT at the family level. Could be refined to GO:0016713
    (reduced iron-sulfur protein donor; adrenodoxin, as for mitochondrial P450s) but there is no
    biochemistry and the conserved Tyr in the heme motif [PMID:22574182 "Cyp301A1 in all insect species
    analysed has a Tyr (Y) instead of the highly conserved Phe (F)"] makes atypical chemistry possible,
    so left as a suggested question.
  - Heme / iron binding: KEEP_AS_NON_CORE (cofactor binding; iron is heme iron).
  - Mitochondrial membrane: ACCEPT (predicted transit peptide + mitochondrial clan membership;
    not experimentally localised). Inner membrane is likely by analogy to other mito-clan P450s, but
    only one line of target-specific evidence (transit peptide), so not added as NEW.
  - Tergite morphogenesis IMP: KEEP_AS_NON_CORE. Phenotype is supported by insertion, excision
    revertant and three RNAi lines; but the mechanism (histoblast spreading / LEC replacement /
    possibly 20E signalling) is unknown, so the role in the process may be indirect.
  - No NEW terms: 20E-related process terms (ecdysteroid metabolism) are speculation in the paper
    itself ("we cannot conclude that CYP301A1 is directly involved in 20E regulation").
- Other-species PubMed hits are insecticide-induction expression studies; not used.
