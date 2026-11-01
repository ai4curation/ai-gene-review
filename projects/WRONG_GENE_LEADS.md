---
title: "Wrong-Gene Leads"
maturity: IN_PROGRESS
tags: [PIPELINE]
species: [human, ECOLI]
genes: [CSGALNACT1, ARHGDIB, traB]
---

# Wrong-Gene Leads

**Bottom line:** UniProt lists the papers it used for each entry. When a GOA row with
experimental or author-statement evidence cites a paper that the annotated protein's
own entry does not cite, but another reviewed entry in the same species does, the
paper may have studied that other protein. A sweep of every gene folder in this
repository finds 9,963 such rows in 2,640 genes. After scoring, 473 rows in 233 genes
rank in the top tier. These are leads for review, not verdicts: a quick look at the
top tier finds a mix of plausible wrong-gene annotations and papers that legitimately
studied several related genes.

This is the reference-level counterpart of the
[function requirement rules](FUNCTION_REQUIREMENT_RULES.md): those ask whether a
protein *can* do what it is annotated with, this asks whether the cited paper was
*about* that protein. It follows
[issue #5727](https://github.com/ai4curation/ai-gene-review/issues/5727).

## Motivating cases

- **human/CSGALNACT1.** Ten rows cite PMID:11514575, which cloned the 802-residue
  chromosome-15 chondroitin synthase CHSY1 (Q86X52). CSGALNACT1 is 532 residues and
  was cloned a year later. Only CHSY1's UniProt entry cites the paper. The review
  records these rows as `WRONG_GENE_PRODUCT` source defects.
- **human/ARHGDIB.** A TAS cytoplasmic-vesicle row cites PMID:9113980, the
  RhoGDIγ (ARHGDIG, Q99819) paper; only ARHGDIG's entry cites it.
- **ECOLI/traB** (a known miss). The ATP hydrolysis IDA cites PMID:20172994, on
  plasmid pKM101's TraB (Q46698). That unreviewed entry does not cite the paper, so
  this signal cannot see the case.

## Method

`just wrong-gene-leads` (`src/ai_gene_review/tools/wrong_gene_leads.py`):

1. For each gene folder, take GOA rows with evidence EXP, IDA, IPI, IMP, IGI, IEP,
   TAS or NAS that cite a PMID the gene's own `*-uniprot.txt` does not cite. NOT rows
   and bare protein binding (`GO:0005515`) are skipped, as are high-throughput codes.
2. Ask UniProt which reviewed entries cite each such PMID, in batches, cached under
   `.cache/wrong-gene-leads/`. Papers cited by more than 20 reviewed entries are
   treated as large-scale and skipped.
3. Drop citing entries that are the same gene in the same species. An unreviewed or
   secondary entry annotated while the reviewed entry for the same gene cites the
   paper is not a wrong gene; before this filter, such cases dominated the top
   scores (for example Drosophila `loqs`, X2J5X6 against Q9VJY9).
4. Score each remaining row:

   | Signal | Score |
   |---|---|
   | A citing entry is a paralog in the same species (same PANTHER family) | +3 |
   | Otherwise, a citing entry is another gene in the same species | +2 |
   | A citing entry is the same-named gene in another species | +2 |
   | Three or fewer citing entries | +1 |
   | The cached title and abstract do not name the annotated gene | +2 |
   | The cached title or abstract names the annotated gene | −3 |

   The name check matters because papers often study several members of a family; a
   paper whose abstract names the annotated gene probably did study it. ARHGDIB's
   paper mentions "GDI/D4", one of its synonyms, so that lead is kept but ranks low.

The report is written to `reports/wrong-gene-leads/leads.tsv`. It is generated and
git-ignored, never committed, because it aggregates every review. It joins each lead
to the existing review action and to any `WRONG_GENE_PRODUCT` source defect.

## Results (2026-11-01)

9,963 leads in 2,640 genes:

| Score | Rows | Genes | Already `WRONG_GENE_PRODUCT` | Already `REMOVE` |
|---|---|---|---|---|
| 8 | 1 | 1 | 0 | 0 |
| 7 | 6 | 4 | 0 | 0 |
| 6 | 466 | 229 | 8 | 11 |
| 5 | 3,864 | 1,416 | 7 | 58 |
| 4 | 1,396 | 658 | 5 | 20 |
| 3 | 576 | 284 | 1 | 17 |
| 2 | 100 | 59 | 0 | 1 |
| 1 | 318 | 150 | 3 | 2 |
| 0 or below | 3,236 | 1,040 | 1 | 29 |

Agreement with past reviews is low at every tier. That is expected rather than
reassuring: reviewers almost never checked whether a cited paper studied the
annotated protein, so most rows were accepted on the term alone.

The top tier (score 6 or more) is 473 rows in 233 genes, mostly human (319) and
mostly IDA, IMP, TAS and NAS rows; 57 are IPI. A random sample of 25 non-IPI rows
from that tier, judged from paper titles only (not yet checked against the papers),
splits roughly in two:

- **Look like real candidates:** FLNC "cytoplasm" (IDA) from a paper on filamin A and
  filamin B; PAPSS1 "skeletal system development" (TAS) from a PAPSS2 dysplasia
  paper; AURKC "chromosome passenger complex" (TAS) from an Aurora A review; NLRP3
  "inflammatory response" (IMP) from an NLRP4 paper; SOCS3 "protein kinase inhibitor
  activity" (IDA) from a SOCS2 paper.
- **Probably legitimate multi-gene papers:** CALM2 and CALM3 from a calmodulin-mutation
  paper about CALM1 (the three genes encode the same protein), TRIM13 from a TRIM
  screen, fibrinogen gamma from a fibrinogen Aα paper, and calcineurin isozyme papers.

The score-5 tier is large (3,864 rows) and dominated by "another gene in the same
species, few citing entries, gene not named in the abstract". Many of these are
complex or pathway papers where UniProt cited the paper only for the protein it
foregrounded.

## Limitations

- **UniProt citation is incomplete.** An entry not citing a paper does not mean the
  paper is irrelevant, and unreviewed entries (like pKM101 TraB) rarely cite papers at
  all, so cases like traB are invisible.
- **The name check uses gene names only.** Abstracts that say "filamin C" or
  "calcineurin A beta" are not matched against FLNC or PPP3CB, which leaves some
  multi-gene papers ranked too high.
- **IPI rows are noisy.** An interaction paper is often cited by UniProt for only one
  partner.
- **Uncached papers** get no name-check adjustment.

## Next steps

- Review the top tier, starting with the non-IPI human rows, and record confirmed
  cases as `WRONG_GENE_PRODUCT` source defects in the gene reviews.
- Match UniProt protein names, not only gene names, in the abstract check.
- Consider scoring IPI rows separately, or requiring that the abstract names a citing
  entry's gene.
- Report the same-gene-other-species signal separately: a direct evidence code (IDA)
  on a human protein from a paper on the bovine or mouse ortholog is an evidence-code
  question (`WRONG_EVIDENCE_CODE`), not a wrong gene.
