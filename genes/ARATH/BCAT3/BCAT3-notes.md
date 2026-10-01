# BCAT3 (At3g49680, Q9M401) review notes

## Identity and localization
- Plastid-targeted BCAT: [PMID:12068099 "three isoenzymes are imported into chloroplasts (AtBCAT-2, -3, and -5)"]; many HDA/IEA/ISM chloroplast rows all ACCEPT; the NOT-cytosol RCA row (PMID:21166475) is consistent and accepted.
- Complements yeast BCAA auxotrophy: [PMID:12068099 "Restored growth on minimal medium lacking the three branched-chain amino acids confirms the respective enzymatic activities for AtBCAT-1, -2, -3, -5, and -6"].

## Dual function (Knill et al. 2008)
- BCAA: [PMID:18162591 "Highest affinities were seen toward 4MOP ( K m , 0.14 ± 0.04 m m ) and 3MOP ( K m , 0.14 ± 0.3 m m )."]; bcat3-1 has reduced Val [PMID:18162591 "The reduction of Val in the bcat3-1 mutant suggests BCAT3 to be active in the formation of Val."]
- Glucosinolates: [PMID:18162591 "BCAT3 most likely catalyzes the terminal steps in the chain elongation process leading to short-chain glucosinolates"]; double mutant with bcat4 is additive [PMID:18162591 "the knockout of BCAT3 has a striking additive effect on the reduction of total Met-derived glucosinolate content"].

## Curation decisions
- All 22 GOA rows ACCEPT (activities are experimentally supported; leucine/valine biosynthesis IEA sound).
- Two core functions: (1) GO:0004084 in Leu/Val biosynthesis in chloroplast; (2) GO:0010326 in glucosinolate and homomethionine biosynthesis.
- NEW GO:0019761 glucosinolate biosynthetic process (IMP, PMID:18162591): BCAT3 lacks it in GOA although it catalyzes elongation-cycle transaminations; comparator BCAT4 and MAM1/MAM3 carry it.
- NEW GO:0033322 L-homomethionine biosynthetic process: term currently unannotated anywhere (QuickGO), so not a deliberate convention.
- No deep-research file was available at the time of review.

## 2026-10-01: GO:0033322 withdrawn

The NEW annotation to GO:0033322 (L-homomethionine biosynthetic process) has been removed, and the
term dropped from core_functions. GO obsoleted the sibling terms GO:0033506 ("glucosinolate
biosynthetic process from homomethionine": "a specific pathway variant, which is out of scope for
GO", replaced by GO:0019761) and GO:0033321 ("homomethionine metabolic process": "an unnecessary
grouping term"). No gene product in any species carries GO:0033322. Read together, this is a GO
convention to annotate the chain-elongation enzymes to glucosinolate biosynthetic process
(GO:0019761), which this gene already carries, not a gap to fill. The question is kept as a
suggested_question for GO.
