---
title: "Wrong-Gene Leads"
maturity: IN_PROGRESS
tags: [PIPELINE]
species: [human, ECOLI, ARATH, DICDI, DROME, mouse]
genes: [CSGALNACT1, ARHGDIB, traB, PAPSS1, FLNC, SOCS3, NLRP3, AURKC, POFUT1, tagC, AHK2, GLN2, SYP121, BEH2, CYP71A12, statA, PARD6B, DLG3, GNAQ, JAK1, PPP3CA, AP2M1, Rbpj, EloC, Med, Septin1, Septin2, Septin4]
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
   `.cache/wrong-gene-leads/`. UniProt's `lit_pubmed:` search matches only an
   entry's own references (its `RX   PubMed=` lines), not the computationally
   mapped bibliography (GeneRIF, PRO, Reactome, GAD), so both sides of the
   comparison are the same kind of list. Checked 2026-11-06: for CSGALNACT1,
   ARHGDIB and SOCS3, `lit_pubmed_id` equals the flat file's RX set, and none of
   CSGALNACT1's eight mapped papers is matched by a `lit_pubmed:` search.
3. Drop citing entries that are the same gene in the same species (symbols are
   compared ignoring case, since UniProt writes rodent symbols in title case). Papers
   still cited by more than 20 other reviewed entries are treated as large-scale and
   skipped. An unreviewed or
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
   Gene names come from the whole `GN` block, and curated protein names (`DE`
   `Full=`/`Short=`) are matched as phrases. Protein names whose only evidence is an
   ARBA rule or submitter text are not used, and neither is a name shared by a citing
   entry: a family name such as "Tubulin alpha chain" does not say which paralog a
   paper studied. The check reads the cached title and abstract only, up to the next
   section heading.

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

## First lead review (2026-11-01)

The six top-tier leads that looked most plausible from paper titles were checked
against the cached abstracts. Full text could not be retrieved for any of them
(Europe PMC has none, and the JBC pages returned 403), so CLAUDE.md's rule applies:
an experimental row is not called wrong-gene unless the abstract itself says so.

| Gene | Row | Paper | Outcome |
|---|---|---|---|
| PAPSS1 | skeletal system development (TAS, PINC) | PMID:9771708, SEMD and brachymorphic mouse | **Confirmed.** The abstract names the mutated gene as ATPSK2 (PAPSS2); PAPSS1 is ATPSK1. The review had already marked the row over-annotated in prose; it now carries a `WRONG_GENE_PRODUCT` source defect (PINC, repoint to O95340). |
| FLNC | cytoplasm (IDA, MGI) | PMID:12393796, filamin A and B in neurons | **Query.** The abstract never mentions filamin C, but the row is experimental and the full text was unavailable. Recorded as a `WRONG_REFERENCE` / `CHECK` / `SUSPECTED` defect; the action (TOO_GENERAL) is unchanged. |
| SOCS3 | protein kinase inhibitor activity; cytoplasmic side of plasma membrane (IDA) | PMID:9727029, SOCS-2 and the IGF-I receptor | **Query**, as for FLNC; actions unchanged. The activity is well supported for SOCS3 by other evidence. |
| NLRP3 | inflammatory response (IMP) | PMID:12093792, PAN2 (NLRP4) | **Query**, as for FLNC; the abstract names Cryopyrin only as a protein PAN2 resembles. Action unchanged. |
| NLRP3 | NF-kappaB regulation (IPI) | PMID:15817483, PYPAF3 | **False positive.** The abstract discusses PYPAF1, an NLRP3 synonym. A parser bug missed synonyms that wrap onto a later `GN` line; it is fixed and tested. |
| AURKC | seven rows (TAS) | PMID:19774610, review on Aurora A | **False positive.** The review covers "aurora kinases A, B, and C"; the name check does not match "Aurora C" against AURKC. |

So one of six leads was confirmed, three need the full text, and two were detector
false positives. The two false-positive patterns, wrapped synonyms
and protein names written in words, are both name-matching gaps; the first is fixed.

## Protein-name matching and second lead review (2026-11-01)

The name check now also matches UniProt protein names (`DE` `Full=`/`Short=`) as
phrases in the cached title and abstract, including family enumerations such as
"aurora kinases A, B, and C" for "Aurora kinase C". This penalised papers that spell
out the protein, and the top tier fell from 466 to 390 rows.

The next 20 top-tier leads (one row per gene, IPI rows skipped, genes already checked
excluded) were then checked against the cached abstracts, and the cached full text
where available:

| Gene | Row | Outcome |
|---|---|---|
| DICDI/tagC | cell differentiation (IMP, dictyBase) | **Probable wrong gene.** The abstract of PMID:7744252 describes a tagB REMI mutant. `WRONG_GENE_PRODUCT` defect repointing to tagB (P54683); the reason, which had attributed the genetics to tagC, is corrected. Action unchanged (KEEP_AS_NON_CORE, consistent with the IEA row). |
| ARATH/AHK2 | response to toxic substance (IMP, TAIR) | **Probable wrong gene.** The abstract reports the cre1 (AHK4) mutant, not ahk2. `WRONG_GENE_PRODUCT` / `CHECK` toward AHK4 (Q9C5U0); the review had already noted this. |
| human/POFUT1 | three IDA rows (UniProt) | **Wrong evidence code, not wrong gene.** The 1996 paper assayed enzyme from CHO cells and rat liver; it is cited by the Chinese hamster and rat POFUT1 entries. `WRONG_EVIDENCE_CODE` / `CHECK` on all three rows. |
| ARATH/GLN2 | ammonia assimilation cycle (TAS, TAIR) | **Wrong reference.** The paper is about cytosolic GS1 isoenzymes; GLN2 is plastidic GS2. The claim is true; `WRONG_REFERENCE` / `CHECK`. |
| ARATH/SYP121 | plasma membrane (TAS, TIGR) | **Wrong reference.** The cached full text never mentions SYP121, SYR1, PEN1 or At3g11820. The location is true; `WRONG_REFERENCE` / `CHECK`. |
| ARATH/BEH2, ARATH/CYP71A12, DICDI/statA | TAS, IEP, IDA | **Query.** The abstracts concern BZR1, CYP71A13 and STATc respectively; full text unavailable. `WRONG_REFERENCE` / `CHECK` / `SUSPECTED`; actions unchanged. |
| rat/Dusp21, ARATH/ERS1, ARATH/FRK1, ARATH/ARR5, DANRE/tbx5a | various | **False positives.** The papers study DSP21 directly, all five ethylene receptor isoforms, the FRK1 marker gene, the ARR5 cytokinin marker, and Tbx5 DNA binding by gel-shift assay (in the full text). |
| human/ALDOA, ARATH/AGO1, ARATH/CCA1, ARATH/HSP17.7, ARATH/MLO2, ARATH/MYB34, ARATH/RGA | various | **No change.** An ortholog paper (rabbit aldolase), multi-gene papers whose abstracts do not settle it (AGO1, CCA1, a possible HSP17.6A/17.7 nomenclature mix-up), a family-wide statement (MLO), a gene discussed in the full text (MYB34), and a row the review already removes (RGA). |

Across both batches (26 leads): 3 rows are confirmed or probable wrong-gene
annotations (PAPSS1, tagC, AHK2), 1 is a wrong evidence code (POFUT1), 2 are wrong
references for true claims (GLN2, SYP121), 6 are unresolved queries pending full
text, 7 are false positives and 7 need no change. Remaining false positives
come mostly from synonyms UniProt does not list (DSP21) and from papers that study a
gene as an assay readout or as one of a named family ("five receptor isoforms").

## Review fixes and re-sweep (2026-11-06)

Three changes from PR review, re-run over the current corpus (10,169 leads in 2,684
genes; the corpus grew since the first sweep, so the earlier tables are not directly
comparable):

- **Gene symbols are compared ignoring case.** UniProt writes mouse and rat symbols
  in title case (`Socs3`), so before this fix the same-gene-other-species signal
  could not fire for human against rodent entries. It now fires on 845 rows instead
  of 128, and the top tier grows from 406 to 448 rows.
- **Protein names shared with a citing entry for another gene are not used.** A
  family name such as "Tubulin alpha chain" does not say which paralog a paper
  studied. The guard changes the score of 13 rows and brings one back into the top
  tier: PAPSS1's skeletal-development row, the confirmed wrong-gene case above,
  which the protein-name penalty had buried. Names whose only evidence is an ARBA
  rule or submitter text are also dropped.
- **The name check reads only the title and abstract.** It stops at the next
  section heading and drops the PubMed citation line, author list (including
  bylines with "Jr" suffixes or group authors), affiliations and identifiers,
  which a symbol that is also a surname could otherwise match. 796
  abstract-only records keep their abstract under `## Content`, and those are read
  too. Of the 299 full-text `## Content` records, 242 open with the same PubMed
  block, and their abstract is read up to its `DOI:`/`PMID:` trailer. The other 57
  do not mark where the abstract ends, so only their title is used. The window
  change altered the name-check result for 19 rows, and the trailer rule for 5
  more.
- **The review join keys on isoform and skips NOT rows**, so isoform-specific rows
  no longer overwrite each other.

The top tier (score 6 or more) is now 444 rows in 225 genes; 52 of them carry the
same-gene-other-species signal. The 406, 448 and 444 here count score 6 or more on
the 2026-11-06 corpus. They are not comparable with the 466 (score 6 only) and 390
from the 2026-11-01 corpus above.

## Third lead review (2026-11-10)

A fresh sweep after the byline fixes (bylines ending in NCBI's "New Collective
Author" placeholder or a lowercase group name, and "Collaborators:" paragraphs, are
now dropped) found 10,709 leads in 2,847 genes, with 460 rows in the top tier. The
next 20 top-tier genes were checked the same way as before: one gene per lead, IPI
rows skipped, genes already checked excluded, highest score first. All of a gene's
flagged rows were read, so some outcomes below come from a row other than the
highest-scoring one.

| Gene | Row | Outcome |
|---|---|---|
| mouse/Rbpj | chromatin binding (IDA, MGI) | **Wrong gene, confirmed.** Every ChIP in PMID:23571214 (full text cached) pulls down BEND6. MGI already has the identical row on Bend6, with Rbpj as its `has_input`. `WRONG_GENE_PRODUCT` / `DELETE_ROW` / `CONFIRMED`. |
| DROME/Septin1, Septin2, Septin4 | photoreceptor cell development (NAS, ComplexPortal) | **Probable wrong gene.** PMID:8181057 identifies peanut and its genetic interaction with seven in absentia; only pnut's entry cites it, and pnut carries the same row. `WRONG_GENE_PRODUCT` / `CHECK` / `PROBABLE` toward pnut (P40797) on each. |
| human/PARD6B | four UniProt rows; tight junction (NAS, ComplexPortal) | **Wrong evidence code**, and **wrong reference.** The four UniProt rows rest on mouse Pard6b work in PMID:12545177 (`WRONG_EVIDENCE_CODE` / `PROBABLE`). The ComplexPortal row cites PMID:11257119, which cloned a 346-residue PAR-6: that is PARD6A, while PARD6B has 372 residues (`WRONG_REFERENCE` / `CONFIRMED`). |
| human/DLG3 | kinase binding (IDA, MGI) | **Wrong evidence code, confirmed.** The PMC full text used mouse SAP102 (Dlg3) and rat DGKι constructs and rodent brain. `WRONG_EVIDENCE_CODE` / `CHECK`. |
| human/GNAQ | PLC-activating GPCR pathway (IDA, UniProt) | **Wrong evidence code**, probable. The paper is cited by mouse Gnaq for its structure and mutagenesis, not by human GNAQ. |
| human/PPP3CA | two TAS rows (UniProt) | **Wrong reference.** PMID:2556704 cloned the two PPP3CB isoforms (its proline run and 18-residue insert are PPP3CB features). `WRONG_REFERENCE` / `PROBABLE`; quotes swapped to PPP3CA papers. The flagged CHP2 rows need no change. |
| human/JAK1 | protein tyrosine kinase activity (EXP, Reactome) | **Wrong reference.** PMID:1386289 identifies TYK2 and never names JAK1. `WRONG_REFERENCE` / `PROBABLE`; quote swapped. Its seven flagged rows on PMID:8272873 are false positives: that abstract names "all known members of the Jak-Tyk family". |
| human/AP2M1, DROME/EloC, DROME/Med | IDA rows | **Query.** The abstracts image other adaptins (AP2M1), name only Slim and mammalian KLHDC10 (EloC, filed as an evidence-code query), or concern Schnurri and Mad (Med, two rows). `SUSPECTED`; actions unchanged. |
| human/AP3S2, human/JAK2, human/SRPRB, DROME/CycA, DROME/GstO1, DROME/GstO2, DROME/Prx4, DROME/RfC4 | various | **False positives or no change.** The cached full texts assay the gene itself (σ3B, cyclin A, the Omega GSTs, dPrx4), the abstract names the gene's family (JAK2), the evidence code already records mixed species (SRPRB), or the TAS rows rest on a statement about the whole complex (RfC4). |

So of 20 leads: 4 are wrong-gene annotations (Rbpj, three Septins), 3 are wrong
evidence codes (PARD6B, DLG3, GNAQ), 2 are wrong references for true claims (JAK1,
PPP3CA, plus PARD6B's second row), 3 are queries, and 8 are false positives or need
no change. A new pattern this round: a direct-evidence code on a human protein from a
paper on the rodent ortholog. The same-gene-other-species signal, which the case fix
turned on, now surfaces this pattern routinely.

Across all three batches (46 leads): 7 wrong-gene annotations, 4 wrong evidence codes,
4 wrong references, 9 queries pending full text, and 22 false positives or no change.
No review action was changed on the strength of an abstract alone.

## Limitations

- **UniProt citation is incomplete.** An entry not citing a paper does not mean the
  paper is irrelevant, and unreviewed entries (like pKM101 TraB) rarely cite papers at
  all, so cases like traB are invisible.
- **The name check misses names UniProt does not list.** An abstract that uses an
  unlisted synonym (DSP21 for rat Dusp21) is read as not naming the gene, which leaves
  some multi-gene papers ranked too high.
- **IPI rows are noisy.** An interaction paper is often cited by UniProt for only one
  partner.
- **Uncached papers** get no name-check adjustment.

## Next steps

- Review the top tier, starting with the non-IPI human rows, and record confirmed
  cases as `WRONG_GENE_PRODUCT` source defects in the gene reviews.
- Consider scoring IPI rows separately, or requiring that the abstract names a citing
  entry's gene.
- Report the same-gene-other-species signal separately: a direct evidence code (IDA)
  on a human protein from a paper on the bovine or mouse ortholog is an evidence-code
  question (`WRONG_EVIDENCE_CODE`), not a wrong gene.
