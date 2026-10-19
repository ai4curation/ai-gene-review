---
title: "eggNOG-mapper on Non-model Genomes"
autolink_gene_symbols: false
---

# eggNOG-mapper on non-model genomes

[Back to the eggNOG-mapper evaluation](../EGGNOG_MAPPER_EVALUATION.md)

eggNOG-mapper is mostly used on genomes nobody has curated, so this page tests
it where that is true. It covers every completed review for three non-model
organisms in the corpus:
- ***Pseudomonas putida* KT2440** (PSEPK, 847 proteins), a bacterial chassis
  with almost no experimental GO;
- **horse** (HORSE, 30 proteins), a mammal absent from eggNOG 5;
- **poplar** (POPTR, 113 proteins), a tree whose proteins are in eggNOG but
  carry almost no GO.

**Field pennycress** (THLAR) has only four reviewed genes, so it appears as
case studies rather than statistics. In total that is 994 proteins
([`deep_dive/cohort.yaml`](deep_dive/cohort.yaml)).

The same pipeline as the main evaluation was used: emapper 2.1.13 with
database 5.0.2 and default settings, the same scoring, plus a manual check of
65 sampled terms ([`deep_dive/adjudication/`](deep_dive/adjudication/summary.yaml)).

## Where the annotations come from

| Genome | Seed ortholog | Median seed identity | Level used for transfer | Proteins given GO |
|---|---|---|---|---|
| *P. putida* | KT2440 itself (798 of 847) | 100% | Gammaproteobacteria | 483 of 847 (57%) |
| Horse | other mammals (horse is not in eggNOG 5) | 92% | Metazoa (all 30) | 29 of 30 |
| Poplar | poplar for 44, otherwise other plants | 96% | Streptophyta (109 of 113) | 84 of 113 (74%) |
| Pennycress | other Brassicales and *Arabidopsis* (not in eggNOG) | 84% | Streptophyta | 4 of 4 |

Hiding each genome's own species changed almost nothing (*P. putida* 483 → 465
proteins with GO; horse unchanged). eggNOG holds essentially no GO for these
organisms, so every transferred term comes from other species. Unlike the
model organisms in the main cohort, the default run here is already an
honest test.

The transfer level is set by emapper's default `auto` scope list, and it is
broad: an entire kingdom-scale clade for horse and poplar. A horse protein can
therefore inherit terms from fly and worm orthologs, and a poplar protein from
moss and algae.

## Automatic comparison

Default run, as % of predicted leaf terms:

| Genome | Leaf terms | Median per protein | EXACT | BROADER | NARROWER | DOWNGRADED | REJECTED | UNDECIDED | UNRELATED | Core recall |
|---|---|---|---|---|---|---|---|---|---|---|
| *P. putida* | 2,232 | 4 | 54.7 | 3.8 | 7.4 | 4.9 | 1.6 | 0.4 | 27.1 | 0.41 |
| Horse | 631 | 18 | 12.5 | 0.5 | 10.9 | 1.4 | 0.3 | 4.3 | 70.0 | 0.69 |
| Poplar | 388 | 4 | 26.8 | 7.0 | 16.2 | 5.4 | 0.0 | 0.0 | 44.6 | 0.35 |
| Pennycress | 12 | 2 | 25.0 | 0 | 8.3 | 16.7 | 0 | 0 | 50.0 | 0.27 |

UNDECIDED marks leaves related only to terms the review left UNDECIDED, which
records an absence of judgment rather than a negative one.

Two very different profiles appear.

- ***P. putida* and poplar are under-annotated but on target.** Proteins get
  few terms (median 4), and many proteins get none. The terms that do arrive
  usually match what the reviews accepted. Those reviews start from GOA, which
  for these genomes is mostly electronic (IEA: 90% of *P. putida* rows, 78%
  of poplar rows). So an EXACT match here mostly means
  emapper agrees with InterPro2GO, ARBA and similar pipelines whose rows the
  reviewers kept. It is a consensus of electronic methods, not independent
  confirmation.
- **Horse is over-annotated.** Each protein gets a median of 18 leaf terms
  drawn from all of Metazoa, and 70% of them relate to nothing in horse GOA.
  Horse GOA is sparse, though: 319 rows for 30 proteins, mostly electronic.
  So UNRELATED here mixes real mammalian knowledge that horse GOA lacks with
  errors. The manual check separates the two.

### Added value over GOA

Each review's `core_functions` terms were compared with what each source
covers:

| Genome | Core terms | Already covered by GOA | Recovered by emapper | emapper only (not in GOA) |
|---|---|---|---|---|
| *P. putida* | 2,455 | 1,878 (76%) | 1,004 (41%) | 85 |
| Horse | 45 | 38 | 31 | 1 |
| Poplar | 442 | 371 | 156 | 6 |
| Pennycress | 11 | 4 | 3 | 1 |

For a genome that already has UniProt's electronic annotation, eggNOG-mapper
recovers fewer of the reviewed core functions than GOA already holds. It adds
a core term GOA lacked for about one protein in ten (*P. putida*) or fewer.
Its value is as an independent, offline annotation for sequences that have no
UniProt entry, such as new assemblies and metagenomes, rather than as an
addition to GOA.

## Manual check

Terms were sampled from the default run, as in the main evaluation: proteins
at random, then one term per protein. The rates are therefore per protein.
- *P. putida:* 24 terms (14 UNRELATED, 5 NARROWER, 5 REJECTED).
- Horse: 16 terms (12 UNRELATED, 4 NARROWER).
- Poplar: 16 terms (10 UNRELATED, 6 NARROWER).
- Pennycress: all 9 non-exact terms, a census of its 4 genes rather than a
  sample.

The mix of strata differs by genome, and NARROWER terms are the safest, so
the rows are not directly comparable. The UNRELATED terms alone compare like
for like: wrong in 8 of 14 for *P. putida*, 5 of 12 for horse, 8 of 10 for
poplar and 3 of 6 for pennycress. These reviewers saw each term's automatic
category. The five *P. putida* REJECTED claims are the exception: they were
also re-judged in the main cohort's blinded re-check.

| Genome | Claims | Correct (COR) | True but vague (LSP) | Undecided (UNC) | Wrong (NPI/PLI/REP) |
|---|---|---|---|---|---|
| *P. putida* | 24 | 8 | 2 | 0 | 14 |
| Horse | 16 | 7 | 0 | 4 | 5 |
| Poplar | 16 | 4 | 0 | 1 | 11 |
| Pennycress | 9 | 1 | 0 | 4 | 4 |

### *P. putida*: phenotypes and paralogs from *E. coli*

The commonest error, 6 of 14, is a process term inferred from an indirect
effect in an enterobacterial ortholog:
- HtpG and RfbC given DNA damage response;
- IscU given intracellular iron ion homeostasis;
- SdhD given citrate metabolic process;
- SsuD given response to heat;
- PstC given regulation of phosphatase activity, an *E. coli* Pho-regulon
  effect, carried onto a PstC from KT2440's second Pst-like operon.

The next is paralog pooling in large proteobacterial orthogroups:
- DavD, a glutarate-semialdehyde dehydrogenase, given the GABA shunt, which is
  GabD's job;
- BetB given fermentation from other aldehyde dehydrogenases;
- the AcnD-family 2-methylcitrate dehydratase given aconitate hydratase.

All five terms the curators had removed were wrong again:
- IlvH, the regulatory subunit, given acetolactate synthase activity, which
  belongs to the catalytic subunit;
- UbiX given 4-hydroxy-3-polyprenylbenzoate decarboxylase activity (it makes
  the prenylated FMN that the real decarboxylase, UbiD, uses);
- Exonuclease I (SbcB) given RNA exonuclease activity;
- PrpD given 2Fe-2S binding, although the purified enzyme has no cluster.

Correct additions were concrete and structural: two 4Fe-4S motifs in PydA,
zinc binding in AroB, signal sequence binding for SecY, and homodimerization
for RlmH.

### Horse: mostly right, wrong where mouse phenotypes leak in

- **Correct missing knowledge:** 4 of the 12 UNRELATED terms were correct
  mammalian knowledge absent from horse GOA: defense response to virus for
  CH25H, FFAT motif binding for VAPA, spliceosomal snRNP assembly for GEMIN5,
  and scaffold protein binding for MAP2K2.
- **NARROWER terms:** all four were correct or undecided.
- **Errors:**
  - process terms read from mouse knockout phenotypes: GPAM given regulation
    of cytokine production; OMA1 given glucose metabolic process;
  - a paralog's function: MYL10, a lymphocyte-precursor light chain, given
    muscle contraction;
  - old source annotations: USP8 given cysteine-type endopeptidase rather than
    deubiquitinase activity; HSPD1 given myelin sheath from rodent proteomics.

Of the three genomes, horse is where orthology transfer adds most. The cost
is a long list per protein that still needs filtering.

### Poplar: proteomics and paralogs from *Arabidopsis*

Poplar had the highest error rate (11 of 16).

- **Chloroplast proteomics carried over as locations:**
  - psaB in the plastoglobule;
  - psaA in the chloroplast envelope;
  - the membrane NDH subunit ndhH in the stroma.
- **Paralogs merged at the Streptophyta level:**
  - chloroplast-encoded rpl14 given a mitochondrial ribosome term;
  - a cytosolic NADP-malic enzyme given the plastid isoform's chloroplast
    location;
  - PtNRAMP6.1 given aluminium transport, which is specific to rice Nrat1.
- **Indirect or generic terms:**
  - LIP1 given glycine catabolism (it lipoylates the H-protein that the
    pathway needs);
  - METK1 given copper binding from affinity proteomics;
  - PRX2 given response to cadmium ion.

Correct additions included SAM binding for the radical-SAM lipoyl synthase and
heme transport for ccsA.

### Pennycress, gene by gene

| Gene | Leaves | Verdict |
|---|---|---|
| FAE1 | 2 | The core activity (fatty acid elongase) is an exact match, but ER membrane and very-long-chain fatty acid biosynthesis are missed. Captured, incompletely. |
| TFP | 6 | Glucosinolate catabolism is exact. It frames the protein as an enzyme regulator (outdated; TFP is an Fe²⁺-dependent lyase), misses the lyase activity, and imports *Arabidopsis* ESP's single-paper senescence, defence and nuclear terms. Partial and noisy. |
| CYP71B1 | 3 | Generic P450 monooxygenase activity, which is all anyone knows. Its location and process terms are guesses. |
| matK | 1 | Only "chloroplast", which is correct. Group II intron splicing, the actual function, is missed. |

## Narrowing the taxonomic scope does not fix it

The broad transfer level suggests an obvious fix: emapper's pre-configured
`--tax_scope all_narrow`, which includes clades such as Mammalia and
Brassicales.

| Genome | Proteins with GO, default → narrow | Core recall, default → narrow | EXACT % of leaves, default → narrow |
|---|---|---|---|
| *P. putida* | 483 → 57 | 0.41 → 0.04 | 55 → 60 |
| Horse | 29 → 12 | 0.69 → 0.22 | 13 → 29 |
| Poplar | 84 → 61 | 0.35 → 0.25 | 27 → 36 |

Precision rises, but coverage collapses: the narrowest clade containing the
seed usually has no GO-annotated members. In the main cohort with the own
species hidden, narrow scope gave GO to only 92 of 515 proteins (core recall
0.12), nearly all of them rat and mouse borrowing from each other. Neither
setting gets a broad scope's coverage without its errors.

## Take-aways for annotating a new genome

- **Treat BP terms as leads, not annotations.** Most errors here are process
  terms inferred from an ortholog's phenotype or expression response. MF terms
  backed by domain evidence are the safest.
- **Check paralog-rich families by hand.** Look at transporters,
  dehydrogenases, P450s and plastid/mitochondrial isoform pairs before trusting
  their terms.
- **Treat locations from proteomics with suspicion.** This applies especially
  to chloroplast sub-compartments and myelin, nucleoid or other
  fraction-derived terms.
- **For a genome in UniProt, emapper's GO adds little beyond GOA.** Its
  agreement with GOA's electronic terms is not independent evidence.
