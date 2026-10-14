# MAM1 (At5g23010, Q9FG67) review notes

## Activity
- Condensing enzyme of the first two Met chain-elongation cycles: [PMID:14740211 "MAM1, one of two similar genes in the A. thaliana ecotype Columbia, encodes a MAMS catalyzing the condensing reactions of the first two elongation cycles but not those of further cycles."]
- Neofunctionalized from MAMa/MAM2: [PMID:16754868 "Thus, Col-0 MAM1 controls the committed step in both the first and second round of methionine carbon chain elongation"].
- NO IPMS activity: [PMID:14740211 "However, the MAM1 protein does not show activity with the substrates of any of these other enzymes, and was chromatographically separable from isopropylmalate synthase in extracts of A. thaliana."] and no E. coli IPMS complementation [PMID:15155874 "Only the expression of MAML-3 restored the ability of the mutant to grow in the absence of Leu."]. True IPMSs are IPMS1/IPMS2 [PMID:17189332].

## Genetics
- GSL-ELONG / GSM1 locus; missense mutants lack C4 glucosinolates [PMID:11706188 "Two allelic mutants deficient in four-carbon side-chain glucosinolates were shown to contain independent missense mutations within this gene."]; gsm1-1 = TU1 [PMID:17369439 "gsm 1 - 1 = TU1 ) lacking a functional MAM1 allele"].

## Curation decisions
- REMOVE: IBA GO:0003852 2-isopropylmalate synthase activity and IBA GO:0009098 L-leucine biosynthetic process (paralog over-propagation from PTN000031336; target-specific evidence of loss). propagation_review added.
- KEEP_AS_NON_CORE: IEP response to water deprivation, response to insect (PMID:23144921, transcript changes).
- Everything else ACCEPT; core MF GO:0010177 in GO:0019761, chloroplast.
- NEW GO:0033322 L-homomethionine biosynthetic process (term unannotated anywhere; MAM1 catalyzes the committed step).
- Chloroplast localization for MAM1 itself is by sequence/proteomics; MAM3 paralog is immunolocalized [PMID:17369439].
- Cached PMID:31023839 (Kumar et al. 2019, Brassica juncea MAM structure) for background; not cited in review.
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
