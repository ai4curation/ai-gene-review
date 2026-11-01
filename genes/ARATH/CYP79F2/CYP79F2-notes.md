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


## Module-member evidence audit — 2026-10-25

Reviewed every original row (15) and core function using review/annotation-reviewer instructions, current cached primary publications and the existing research. Preserved all source annotation fields and all pre-existing proposed rows. Reused the existing genuine Falcon provider report and its artifacts. These plant targets do not require bacterial FEBA retrieval.

GO:0120526 is defined for an L-polyhomomethionine, so it covers the directly measured penta-/hexahomomethionine activity in PMID12609033. It does not imply CYP79F2 accepts the shorter CYP79F1 substrates. ER localization is direct in PMID11226190. Broad terms are refined consistently across evidence codes.

Broad and substrate-specific terms were assessed consistently across evidence codes. No NEW rows were added. Previously proposed rows were evaluated for direct participation rather than filled from pathway adjacency. Experimental cohort calls whose protein-level data were not verified were left UNDECIDED; full-text availability alone was not treated as proof of a target-specific assay. Original sources and provider reports were not hand-edited.
