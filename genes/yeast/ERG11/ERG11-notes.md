# ERG11 (YHR007C) notes

UniProt P10614; lanosterol 14alpha-demethylase CYP51, EC 1.14.14.154; heme [UniProt:P10614].

## Evidence journal
- Recombinant CYP51-reductase fusion demethylates at 14alpha [PMID:9087488 "FUS protein catalyzed the demethylation of substrate at the 14alpha position"].
- ER-associated, unlike Erg7 [PMID:15951236 "Erg11p in contrast to Erg7p is associated with the endoplasmic reticulum (ER)"]; erg11 lethality bypassed in erg3 background (same paper).
- Rate-limiting step [PMID:32679672 "Erg1 and Erg11 represent two rate-limiting steps in this part of the pathway."].
- Caution: PMID:200835 abstract assigns erg 9/10/11 groups to squalene synthetase [PMID:200835 "squalene synthetase (erg 9, erg 10, erg 11)"] -> IMP row UNDECIDED (historic allele naming may differ from modern ERG11).

## Decisions
- Generic monooxygenase / paired-donor oxidoreductase IEA -> MODIFY GO:0008398; deep P450 IBA oxidoreductase KEEP_AS_NON_CORE; iron ion binding KEEP_AS_NON_CORE (heme iron); protein binding REMOVE; RCA cytosol -> ER membrane.
