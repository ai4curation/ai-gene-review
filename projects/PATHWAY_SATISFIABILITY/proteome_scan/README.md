---
title: "Proteome scan: module holes from first-pass UniProt annotation"
maturity: IN_PROGRESS
tags: [PIPELINE]
autolink_gene_symbols: false
---

# Proteome scan

Part of [Pathway satisfiability](../../PATHWAY_SATISFIABILITY.md). `scan.py` evaluates
every module in `modules/` against a UniProt proteome, using only what UniProt already
says about each protein: its GO ids and its PANTHER, InterPro, NCBIfam and Pfam
cross-references. No sequence search is run. The logic is `module_logic.py`; the scan
adds one oracle. The scoring levels, module statuses and taxon scopes are defined in
the docstring of `scan.py`.

```bash
uv run python projects/PATHWAY_SATISFIABILITY/proteome_scan/scan.py \
    UP000000625 UP000035170 -o projects/PATHWAY_SATISFIABILITY/proteome_scan/results
```

It produces two kinds of lead for a curator:

- **Annotation hole**: a member of the step's family is in the proteome, but no protein
  is annotated to the step's function. The family members are the candidates.
- **Missing step**: nothing matches a step of a module that is otherwise at least 75%
  present with at most two gaps. Members of a sibling PANTHER subfamily are listed as
  paralog candidates.

## First run (2026-11-26)

Eight proteomes, 888 modules, GO release 2026-07-26. Counts are for modules in scope
(root taxon contains the organism, or no taxon declared). "Single" holes have exactly
one candidate protein.

| Proteome | Organism | Proteins (reviewed) | Satisfied | By family only | Near complete | Holes (single) | Missing steps |
|---|---|---|---|---|---|---|---|
| UP000000625 | *E. coli* K-12 | 4403 (4403) | 172 | 7 | 20 | 13 (8) | 24 |
| UP000000556 | *P. putida* KT2440 | 5527 (745) | 178 | 8 | 22 | 32 (19) | 27 |
| UP000035170 | *Variovorax paradoxus* | 6788 (1) | 125 | 31 | 24 | 87 (57) | 29 |
| UP000001425 | *Synechocystis* PCC 6803 | 3508 (1115) | 79 | 17 | 18 | 32 (25) | 21 |
| UP000002480 | *Rickettsia prowazekii* | 832 (584) | 34 | 10 | 12 | 29 (26) | 13 |
| UP000000805 | *M. jannaschii* | 1786 (1786) | 15 | 4 | 11 | 12 (10) | 15 |
| UP000002311 | *S. cerevisiae* | 6067 (6067) | 146 | 11 | 31 | 30 (15) | 38 |
| UP000006906 | *Chlamydomonas reinhardtii* | 18840 (109) | 110 | 30 | 32 | 66 (37) | 34 |

What the run shows:

- **The control behaves.** Methionine biosynthesis is satisfied in *E. coli*, *P. putida*,
  *V. paradoxus* and yeast, and incomplete in *Synechocystis*, *M. jannaschii* and
  *R. prowazekii*, as the KEGG-ortholog oracle found for the same organisms. Pathways
  *E. coli* lacks (catechol ortho-cleavage, PQQ biosynthesis, benzoate degradation) are
  absent or incomplete.
- **Holes track curation depth.** The unreviewed *Variovorax* proteome has 87 holes
  against 13 for *E. coli*. Typical ones are single-candidate and uncontroversial: the
  four PstSCAB subunits with no phosphate-transporter activity, SecB with no holdase
  activity, the DNA polymerase III clamp loader subunits, TatB/TatC, LptD.
- **Holes in a fully reviewed proteome are mostly not holes.** In *E. coli* the
  candidates are curated proteins of the same family with another activity (AtoD/AtoA
  for 3-oxoadipate CoA-transferase, PaaH for carnitine dehydrogenase). Family
  membership alone does not separate paralogs, so a hole is a lead, not a proposal.
- **Some leads are about the module, not the genome.** *E. coli* flagellar assembly
  reports FliQ and FlgC as missing because the module selects one PANTHER subfamily
  and the *E. coli* proteins sit in another; the paralog candidates name them. A
  selector that covers a fused enzyme (the ADP-heptose module lists the GmhA subfamily
  on the HldE steps for a fused representative) offers GmhA as a candidate for the
  kinase step.

## Limits

- Presence permits a step; it does not show the pathway runs.
- Only steps with a GO function or a PANTHER, InterPro, NCBIfam or Pfam selector can be
  judged in another organism. Steps grounded only by another organism's accession are
  assumed present, so they never raise a hole and can hide one.
- A function step counts as held when any protein carries the term, whatever its
  evidence; for an unreviewed proteome that is mostly electronic annotation.
- Modules whose root taxon is a single other organism are counted but not detailed,
  although many (central metabolism curated in human or yeast) do apply.
- Near-complete is a threshold on step counts, not a statement about biology: the
  *E. coli* list includes pathways the organism does not have.
