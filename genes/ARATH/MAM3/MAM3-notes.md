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


## 2026-10-25 independent chain-elongation audit

Re-examined every existing annotation and core against the primary studies and exact GO reactions; preserved all machine-sourced fields and prior rows. Normal fetch-gene and fetch-gene-pmids completed. The default Falcon attempt for this panel (MAM1) failed authentication and perplexity-lite failed insufficient quota; no fabricated provider report was created. Existing provider reports were contextual only; primary sources govern decisions. Plant proteins do not require bacterial fitness fetches.

Correct broad terms now refine to supported descendants. IIL1 and SSU3 catalytic claims refer to heterodimers, with contributes_to in cores; catalytic-site ownership alone does not establish autonomous subunit activity. MAM1 lacks measured IPMS activity, whereas MAM3 retains a weak non-core activity without established native leucine-pathway participation. IMDH1 biochemical comparisons distinguish its specialized methylthioalkylmalate substrate from 3-isopropylmalate; IPMDH2 structural data are not direct IMDH1 structures. BCAT3 terminal transamination is distinct from unelongated methionine transamination and does not establish exclusivity over all chain lengths.
