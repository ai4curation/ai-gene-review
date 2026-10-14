# MAM3 (At5g23020, formerly MAM-L, Q9FN52) review notes

## Activity
- Broad-specificity MAM: [PMID:17369439 "MAM3 enzyme, which is able to catalyze all six condensation reactions of Met chain elongation that occur in Arabidopsis"].
- Residual IPMS activity: [PMID:17369439 "MAM3 was able to convert 2-oxoisovalerate (to isopropylmalate) and pyruvate (to citramalate), but based on their kinetic parameters, these were less preferred substrates"]; complements E. coli leuA at 28 C [PMID:17369439 "Hence, the Arabidopsis MAM3 was able to complement the mutant in the gene encoding IPMS and restored autotrophic growth."] but Field et al. 2004 did not observe complementation; unlikely to act as IPMS in planta [PMID:17369439 "it appears very unlikely that this enzyme is active as IPMS under normal growth conditions"].

## Localization and genetics
- Chloroplast by immunolocalization [PMID:17369439].
- Knockouts lack long-chain glucosinolates; complemented [PMID:15155874 "A MAML knockout line (KO) lacked long-chain aliphatic GSLs, which were restored when the KO was transformed with a functional MAML gene."].

## Curation decisions
- KEEP_AS_NON_CORE: GO:0003852 IPMS activity (IBA and NAS) - real but minor promiscuous activity.
- MARK_AS_OVER_ANNOTATED: GO:0009098 leucine biosynthesis (TAS, PMID:12432038).
- All other rows ACCEPT; core MF GO:0010177, process GO:0019761, chloroplast.
- NEW GO:0033322 L-homomethionine biosynthetic process (term unannotated anywhere per QuickGO).
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
