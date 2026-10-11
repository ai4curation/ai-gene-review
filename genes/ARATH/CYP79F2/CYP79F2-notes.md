# CYP79F2 (hexahomomethionine N-hydroxylase) - Arabidopsis thaliana - review notes

UniProt: Q9FUY7 · At1g16400 · EC 1.14.14.42 · Taxon 3702
Tandem duplicate of CYP79F1 (~89% aa identity) [PMID:11226190].
No falcon deep-research file was present at review time.

## Core function
- Long-chain-specific homomethionine N-monooxygenase: only penta- and hexahomomethionine.
  [PMID:12609033 "In contrast, CYP79F2 exclusively metabolizes long-chain elongated penta- and hexahomomethionines."]
- Genetics: cyp79f2 knockout reduces long-chain aliphatic GSLs; short-chain unaffected.
  [PMID:12609033 "The level of long-chain aliphatic glucosinolates in a transposon-tagged CYP79F2 knockout mutant is substantially reduced, whereas the level of short-chain aliphatic glucosinolates is not affected."]
- Double mutant with cyp79f1 lacks all aliphatic GSLs [PMID:15194821].

## Expression / localization
- Hypocotyl and root vasculature [PMID:12609033 "CYP79F2 is highly expressed in hypocotyl and roots"];
  root-biased mutant phenotype [PMID:15194821 "defective mainly in the root system"] - treated as
  secondary; no developmental GO term proposed.
- ER by N-terminal GFP fusion [PMID:11226190]; chloroplast ISM -> REMOVE.
- MeJA-induced [PMID:12529537]; suppressed by caterpillar oral secretions [PMID:40546745].

## Decisions
- GO:0120526 IEA -> ACCEPT (core); GO:0016709 IDA -> MODIFY to GO:0120526; GO:0016709 IBA -> MODIFY to GO:0016712
- GO:0019761 IBA/IMP -> ACCEPT; ER IBA/IDA, ER membrane IEA, membrane IBA -> ACCEPT
- generic P450 IEA MF terms -> KEEP_AS_NON_CORE; chloroplast ISM -> REMOVE; response to insect IEP -> KEEP_AS_NON_CORE
