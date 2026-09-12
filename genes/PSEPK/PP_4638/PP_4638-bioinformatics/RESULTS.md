# PP_4638 MTHFR-family comparison results

## Summary

Current InterPro matches support an MTHFR-like FAD-linked catalytic domain in
PP_4638 (Q88E30), but they do not establish that PP_4638 is functionally
equivalent to the canonical KT2440 MetF protein Q88D51. Q88E30 has a 495-aa
architecture: the MTHFR-like catalytic region spans approximately residues
5-294, while the MTHFR-like C-terminal PF12225/IPR022026 region spans residues
378-461. This extra region contains 9 cysteines in 84 residues, is absent from
Q88D51, and is distinct from the well-characterized eukaryotic SAM-regulatory
domain. Its presence supports a divergent architecture, not a specific reaction.

Local BLOSUM62 comparisons recover only 200 aligned residues between Q88E30 and
Q88D51 (26.50% identity; 40.40% Q88E30 coverage). In contrast, canonical E. coli
MetF P0AEZ1 and Q88D51 align over 265 residues at 41.89% identity. Q88E30 also
aligns weakly to experimentally characterized reverse-direction S6MTHFR
BAK65950.1 (179 residues at 31.28% identity) [PMID:40016375]. These pairwise
comparisons are not a phylogenetic or active-site classification and cannot
assign forward versus reverse physiological direction.

Independent KT2440 genetics argues against treating PP_4638 as a redundant
canonical MetF. Price et al. reported no significant PP_4638 phenotype across
101 fitness experiments, whereas the fitness profile of PP_4977 metF closely
tracked metH (r = 0.96); they concluded that PP_4638 did not provide MTHFR
activity in those conditions and that its close Acinetobacter homolog probably
has another function [PMID:33534785]. This is strong negative contextual
evidence, although it does not biochemically establish PP_4638's actual activity.

The results therefore support conservative family-level language such as
"MTHFR-like FAD-linked oxidoreductase." They do not independently support the
specific NADH-dependent GO:0106312 activity, equivalence to Q88D51, or a direct
role in methionine biosynthesis. Those claims require biochemical measurement,
genetic complementation, or a focused phylogenetic/active-site analysis.

## Provenance

- Q88E30 and Q88D51 sequences came from the fetched local UniProt records.
- P0AEZ1 was retrieved from UniProt REST; it is experimentally characterized
  E. coli MetF.
- BAK65950.1 was retrieved from NCBI EFetch; it is the experimentally
  characterized reverse-direction S6MTHFR used as a divergent comparator
  [PMID:40016375].
- Domain coordinates were retrieved from the InterPro API during the run.
- Pairwise comparisons used Biopython 1.85, BLOSUM62, local alignment, gap-open
  -10, and gap-extension -0.5.
- The KT2440 fitness comparison and its limitations come from the full text of
  PMID:33534785, cached at `publications/PMID_33534785.md`.
- The biochemical characterization of BAK65950.1 comes from PMID:40016375,
  cached at `publications/PMID_40016375.md`.

## Checklist

- [x] The analysis script takes all local inputs, reference accessions, and the
  output directory as arguments; it does not hardcode gene-specific paths or
  conclusions.
- [x] The script was tested on a second local input, canonical Q88D51 MetF.
- [x] Sequence retrieval, InterPro retrieval, and pairwise analyses completed.
- [x] Direct outputs are present under `results/`.
- [x] Conclusions above distinguish family-level support from unresolved
  catalytic specificity and physiological direction.
