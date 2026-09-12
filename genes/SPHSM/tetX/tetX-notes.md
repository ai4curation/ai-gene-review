# tetX notes

## 2026-06-13 AMR GO-gap review

Selected as a high-value unmapped ARO function because TetX is not merely a generic monooxygenase: it is a tetracycline destructase. UniProt Q06DK7 names the enzyme as TetX monooxygenase, gives EC 1.14.13.231, and records the reaction "tetracycline + NADPH + O2 + H(+) = 11a-hydroxytetracycline" [file:genes/SPHSM/tetX/tetX-uniprot.txt]. The primary PM2-P1-29 paper reports that tet(X) "encodes for a NADP-dependent monooxygenase that requires oxygen to degrade tetracycline" and that the strain transformed tetracycline relative to killed controls [PMID:19187139]. A later heterologous-host paper states that "TetX is a flavin-dependent monooxygenase" and reports metabolites formed after TetX transformation of tetracycline [PMID:26038239].

GOA has only the broad `GO:0004497` monooxygenase activity plus cofactor/location/high-level antibiotic-response terms. The AMR mapping file records `ARO:3000036` as `sssom:NoTermFound` because GO has no TetX/tetracycline-destructase molecular-function term [file:projects/ANTIMICROBIAL_RESISTANCE/aro2go.sssom.yaml]. The review therefore accepts the broad monooxygenase term but proposes a specific `tetracycline 11a-monooxygenase activity` term.
