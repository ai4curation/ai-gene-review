# liuA (PA2015, Q9I296) notes

## Literature

No deep-research provider was available. PMC full text of PMID:16517656 was not returned by the PubMed
tool. Sources: cached abstracts of PMID:18625020, PMID:16517656 and PMID:16272386.

- Purified LiuA [PMID:18625020 "LiuA purified from recombinant E. coli revealed acyl-CoA dehydrogenase
  activity with isovaleryl-CoA (KM 2.3 microM) and butyryl-CoA as substrates"]; terpene-derived acyl-CoAs
  not used [PMID:18625020 "citronellyl-CoA or 5-methyl-hex-4-enoyl-CoA were not utilized"].
- Atu enters Liu downstream of LiuA [PMID:16272386 "enters that of leucine/isovalerate (Liu, leucine and
  isovalerate utilization) at the level of methylcrotonyl-CoA"]. Yet all liu mutants, including a
  complemented liuA mutant, fail on terpenes [PMID:18625020 "Mutants with insertion in any of the liu genes
  were unable to utilize acyclic terpenes or leucine/isovalerate"].

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN000744030 | GO:0003995 acyl-CoA dehydrogenase activity | 14 | 101 (51 taxa) | GO:0008470, IDA, PMID:18625020 (PseudoCAP) | SOUND | Abstract reports the purified-enzyme assay with Km. | human IVD P26440, SBCAD P45954, SCAD P16219, VLCAD P49748, ACAD9 Q9H845, rat/mouse ACADs, Arabidopsis AT3G45300, Aspergillus C8VQF1, bovine Q3ZBF6 | Yes. Thirteen other characterised ACADs; the broad node term suits a broad ACAD clade. |
| PTN000744030 | GO:0003995 acyl-CoA dehydrogenase activity | 14 | 101 (51 taxa) | GO:0008470, IMP, PMID:16517656 (PseudoCAP) | UNVERIFIABLE | Abstract describes atuF/liuD/liuE mutant phenotypes, not a liuA mutant or an IVD assay; full text unavailable. The term itself is right (IDA above), so no defect. | as above | Yes. |

No PSEUDOCAP or GO_CENTRAL defect on the seed rows. One UNIPROT defect (CONFIRMED): the ARBA RecName
"Isovaleryl-CoA dehydrogenase, mitochondrial" on a bacterial protein.

## Other decisions

- GO:0008300 isoprenoid catabolic process (PseudoCAP IMP): MARK_AS_OVER_ANNOTATED. LiuA's step is upstream
  of the Atu entry point and LiuA does not use the terpene acyl-CoAs tested; the terpene growth defect is
  unexplained necessity. This differs deliberately from liuC (MODIFY to GO:0016100) and liuE
  (TOO_GENERAL), which act downstream of the entry point. Raised as a suggested question.
- GO:0003995 (IBA, IEA), GO:0016627: TOO_GENERAL (GO:0008470 is_a GO:0003995, checked).

## Leucine catabolism module review (merged from a concurrent curation branch)


- Reviewed as an experimentally characterized bacterial exemplar of the distal L-leucine catabolism module
  (`modules/leucine_catabolism.yaml`); the P. aeruginosa liuRABCDE cluster (PA2011-PA2016) carries the
  direct enzymology and genetics that the P. putida KT2440 orthologs lack.
- Deep research: no provider deep-research file was generated for this gene in this session. The review
  rests on the cached PubMed records cited in the review (PMID:16517656, PMID:16820476, PMID:16272386,
  PMID:18469096, PMID:18625020, PMID:19459965, PMID:19597963, PMID:22158123), all abstract-only except
  PMID:22158123, and on the UniProt record.
- Acyclic terpene terms: the Atu pathway joins the Liu pathway at methylcrotonyl-CoA
  [PMID:16272386 "enters that of leucine/isovalerate (Liu, leucine and isovalerate utilization) at the level of methylcrotonyl-CoA"],
  so enzymes downstream of that point perform steps of acyclic monoterpenoid catabolism; PseudoCAP
  isoprenoid/terpene rows are refined to GO:0016100 monoterpenoid catabolic process, matching the liuC review.
- LiuA is upstream of methylcrotonyl-CoA and purified LiuA does not oxidize citronellyl-CoA or
  5-methyl-hex-4-enoyl-CoA [PMID:18625020 "citronellyl-CoA or 5-methyl-hex-4-enoyl-CoA were not utilized"],
  yet the complemented liuA mutant cannot grow on terpenes. For the isoprenoid IMP row,
  the requirement is shown, the step LiuA performs is not, so the row is marked over-annotated.
