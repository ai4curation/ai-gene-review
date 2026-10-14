# PRR9 (APRR9, At2g46790; UniProt Q8L500) curation notes

## 2026-10-06: initial review (module plant_circadian_clock_oscillator)

- Fetched with `just fetch-gene ARATH Q8L500 --alias PRR9` (UniProt gene name APRR9; folder and
  gene_symbol use the standard symbol PRR9).
- Falcon deep research (`just deep-research-falcon`) failed (provider exit code 1); no
  deep-research file. The review is based on cached publications.

### Key findings
- PRR family transcripts peak sequentially after dawn: PRR9 -> PRR7 -> PRR5 -> PRR3 -> TOC1
  [PMID:11100772 "the APRR-mRNAs started accumulating sequentially after dawn with 2-3 h intervals in the order of APRR9-->APRR7-->APRR5-->APRR3-->APRR1"].
- PRR9 transcription is light-induced via phytochrome [PMID:14634162 "A phytochrome-mediated signaling pathway(s) activates the transcription of APRR9"]; PIL1 is needed for maximal induction [PMID:16891401].
- Repressor of CCA1/LHY [PMID:20233950 "Here, we demonstrate that PRR9, PRR7, and PRR5 act as transcriptional repressors of CCA1 and LHY."].
- TPL/TPR corepressor and HDA6 recruitment [PMID:23267111 "a complex of PRR9, TPL, and histone deacetylase 6, can form in vivo"].
- Also occupies PRR5 output targets [PMID:23027938 "ChIP-quantitative PCR assays indicated that PRR7 and PRR9 bind to the direct-targets of PRR5."].
- Genetics: the prr9 prr7 prr5 triple mutant is arrhythmic in LL [PMID:15767265 "PRR9/PRR7/PRR5 together act as period-controlling factors"].
- Flowering output: PRR9/7/5 activate CO by repressing CDF1 [PMID:17504813].

### Decisions
- Phosphorelay and cytokinin-signalling IEA: REMOVE. The pseudo-receiver lacks the phospho-Asp, and these are domain over-propagation.
- DNA-binding TF activity IBA: MODIFY to GO:0001227 (repressor), consistent with the TOC1 review.
- Protein binding (Y2H: TOC1, BBX18/19, NF-YC2/4): REMOVE as uninformative.
- Red/far-red light signalling: KEEP_AS_NON_CORE.
