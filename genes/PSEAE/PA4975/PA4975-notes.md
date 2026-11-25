# PA4975 (Q9HUJ0) notes

## Review session 2026-11-05 (PseudoCAP IBA-seed protocol, tier 2)

Fetched with `just fetch-gene PSEAE Q9HUJ0 --alias PA4975`; accession matches the
worklist. Unreviewed TrEMBL entry, no gene symbol. No deep-research provider was
used. NCBI E-utilities and Europe PMC search were unavailable; papers mentioning
PA4975 were found by searching the local publication cache. PMID:25085734 is
abstract-only (no PMC copy).

### Literature

- Flavodoxin_2 fold (PF02525), PTHR10204:SF34 (NQO1-like subfamily name).
- Quinone reductase activity of the purified P. aeruginosa orthologs
  [PMID:25085734 "In in vitro assays, each enzyme was shown to reduce quinone substrates with only minimal semiquinone formation."];
  overexpression gave no H2O2 protection except for WrbA and MdaB in a katA mutant
  [PMID:25085734 "in a katA mutant, H2O2 challenged strains over-expressing the WrbA and MdaB orthologs grew significantly better than the empty plasmid control"].
- PA4975 is named as an NQO [PMID:24915188 "Recent data have shown that PA0949, PA1204, PA2580 and PA4975, have NAD(P)H quinone oxidoreductase activities [75]."]
  and is NQO2-like [PMID:24915188 "PA4975 is unusual in bacteria in that it shows significant sequence similarity to the human enzyme NQO2 (61% similarity)."].
- Genomic context [PMID:17416670 "As shown in Table 2 , the contiguous PA4981-to-PA4975 genes were coordinately induced to a high level by l -arginine in the argR mutant."].

### Decisions

- ACCEPT: NAD(P)H dehydrogenase (quinone) activity (IBA; IMP with evidence-code
  defect), cytosol (IBA).
- TOO_GENERAL: catalytic activity (IEA).
- Counts: ACCEPT 3, TOO_GENERAL 1.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN000024521 | GO:0003955 NAD(P)H dehydrogenase (quinone) activity | 4 | 71 (30 taxa) | GO:0003955, IMP, PMID:25085734 (PseudoCAP) | SOUND | The abstract reports in vitro quinone reduction by the purified P. aeruginosa orthologs, and Ryan et al. name PA4975 among them. The term is right; the evidence code should be IDA (PSEUDOCAP WRONG_EVIDENCE_CODE, PROBABLE), as recorded for PA1204 from the same paper. | Human NQO1 (P15559; EXP/IDA GO:0008753 and GO:0050136, PMID:9271353, PMID:8999809), mouse Nqo1 (MGI:103187), rat Nqo1 (RGD:2503) | Yes; NQO1 is the reference enzyme for this activity |

One PSEUDOCAP defect (WRONG_EVIDENCE_CODE, PROBABLE); no GO_CENTRAL defect. Node
caveat, not filed: the same node carries a cytosol IBD seeded by human NQO2
(P16083), so NQO2 orthologs, which prefer dihydronicotinamide riboside over
NAD(P)H, sit below the NAD(P)H quinone dehydrogenase IBD. The term still holds for
the clade as a quinone reductase, and PA4975 itself has the measured activity.
