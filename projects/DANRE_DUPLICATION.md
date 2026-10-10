---
title: "Zebrafish Genome Duplication and Paralog Pairs"
maturity: MATURE
tags: [BIOLOGY_DOMAIN]
species: [DANRE]
genes:
  - LOC564220
  - wu_fi36a10
  - abi1a
  - abi1b
  - agxta
  - agxtb
  - col1a1a
  - col1a1b
  - cryaba
  - cryabb
  - ctdspl2a
  - ctdspl2b
  - eef1da
  - eef1db
  - elna
  - elnb
  - exoc3l2a
  - exoc3l2b
  - fgf8a
  - fgf8b
  - gad1a
  - gad1b
  - gria1a
  - gria1b
  - grk7a
  - grk7b
  - guca1c
  - guca1d
  - lhfpl5a
  - lhfpl5b
  - mapre3a
  - mapre3b
  - mitfa
  - mitfb
  - olfm3a
  - olfm3b
  - pax6a
  - pax6b
  - prom1a
  - prom1b
  - samsn1a
  - samsn1b
  - sh3glb2a
  - sh3glb2b
  - si_dkey-283b1.7
  - vwc2
  - slc7a10a
  - slc7a10b
  - smad3a
  - smad3b
  - sox9a
  - sox9b
  - tbx5a
  - tbx5b
  - tmc2a
  - tmc2b
  - tp53bp2a
  - tp53bp2b
  - tusc2a
  - tusc2b
  - vcla
  - vclb
---

# Zebrafish Genome Duplication and Paralog Pairs

**Bottom line:** zebrafish keeps thousands of ohnolog pairs from the
teleost-specific genome duplication (TGD), roughly 320-350 Mya. This project
reviews those pairs side by side and asks what happened to the ancestral
function: expression partition, protein-level innovation, dosage retention,
backup or unresolved divergence. The 2026-10-04 snapshot covers **31 pair pages /
62 gene reviews**: 10 literature-supported pairs plus a
PANTHER/Compara-informed random sample. The main result matches the genome-wide
literature: retained pairs usually keep the same molecular function and diverge
in *where and when* the copies are expressed; clear protein-level innovation
appeared only in `elnb`, and pure backup was not demonstrated. Details are in
the [pair index](DANRE_DUPLICATION/pairs/README.md), the
[random-sample summary](DANRE_DUPLICATION/random_sample_summary.md), and the
[background research](DANRE_DUPLICATION/DANRE_DUPLICATION-background.md).

## Motivation

A zebrafish gene often corresponds to one human gene through two "co-orthologs"
(the `a`/`b` pairs in ZFIN nomenclature). This matters for GO annotation in three
ways:

1. **Experimental annotations are split between the copies.** A zebrafish IMP or IDA
   is made on *one* copy. Whether it transfers to the other copy, or to the human
   ortholog, depends on whether the copies diverged in molecular function or only
   in expression.
2. **Phylogenetic propagation can treat copies as equivalent.** IBA and ISO often
   give both copies the same inherited or sequence-inferred molecular-function
   terms. Those usually transfer when the catalytic or binding activity is
   conserved, but tissue-specific process and location terms need copy-specific
   expression and localization checks.
3. **Mutant phenotypes can be masked.** Zebrafish mutants can hide phenotypes when a
   paralog is upregulated (transcriptional adaptation). This complicates any claim
   that "gene X is not required for Y" or "X and Y are redundant".

## Questions

1. For each pair, is the **molecular function** conserved in both copies? Or is there
   protein-level divergence, such as lost catalytic residues, domain gain or loss,
   or a changed interaction partner?
2. Are differences in **biological process and location** explained by expression
   partition, as in the DDC model? Or by new expression domains absent from the
   pre-duplication state (compared against gar or another non-teleost fish where
   possible)?
3. Is there positive evidence of **redundancy**, such as double-mutant synergy,
   cross-rescue, or paralog upregulation in mutants? Or is the "backup"
   interpretation only an inference from a mild single-mutant phenotype?
4. Do existing GOA annotations (experimental, IBA, ISO, IEA) handle the pair
   consistently? Are there annotations that should be copy-specific, or that should
   be shared but are missing from one copy?

## Results

### Reviewed pair set

As of 2026-10-04, the project has **31 side-by-side pair pages** whose 62
underlying gene reviews action all **1,022 GOA rows** present in the fetched
review files. No existing annotation is still `PENDING`, and every gene review
has a core-function summary.

| Set | Pair pages | Current readout |
|---|---:|---|
| Literature-supported pairs | 10 | Four expression-level partitions, five mixed cases, and one collagen dosage case; this set contains the only clear protein-level innovation, `elnb` |
| Random-sample pages | 21 | Seventeen non-`vcla` Compara-confirmed draws plus four early PANTHER-only draws retained as rejected or doubtful controls; most remain unresolved because few have perturbation data on both copies |

Across the 31 pages, the fate calls are:

| Fate | Pairs | Interpretation |
|---|---:|---|
| `PARTITION` | 8 | Usually an expression split with conserved molecular function; the `agxt` pair is the sequence-inferred protein-targeting exception |
| `MIXED` | 5 | A shared molecular function with copy-specific expression or quantitative protein changes; `elnb` is the single clear new protein function |
| `DOSAGE` | 1 | `col1a1a`/`col1a1b` both contribute chains to the type I collagen system |
| `BACKUP` | 1 | `smad3a`/`smad3b`, still provisional because the single-mutant evidence was not visible |
| `UNRESOLVED` | 16 | Mostly random pairs with expression-only, sequence-only or single-copy perturbation evidence |

The **18 Compara-confirmed random draws** give the less biased view: 12 are
`UNRESOLVED`, 4 are `PARTITION`, 1 is the provisional `smad3` backup, and 1 is
the already-reviewed `vcla` mixed case. Only 7 of 18 have experimental data on
both copies; 8 have expression data only, 2 have experiments on one copy only,
and 1 rests on sequence evidence.

### Curation consequences

- Core molecular-function terms usually survive on both copies; biological
  process and cellular-component annotations require copy-specific expression
  or localization evidence.
- Protein-level neofunctionalization was rare in the curated set. `elnb` gained
  a bulbus-arteriosus elastin role that `elna` cannot substitute for; other
  protein-level signals, such as `agxt` targeting or `guca1c`/`guca1d`
  calcium-sensitivity differences, need biochemical or mutant confirmation.
- The commonest GOA correction was removing IBA propagation of tissue-specific
  process terms onto the non-expressing copy, for example `sox9a` heart
  morphogenesis, `pax6a` pancreas development, `lhfpl5b` inner-ear/hearing
  terms, `prom1a` photoreceptor differentiation, and `agxtb` peroxisome terms.
- Apparent PANTHER `TGD_tree` calls still need an independent Compara or synteny
  check. Four early random draws were kept in the record after that check failed
  or weakened the TGD interpretation.

## Approach

### Pair selection criteria

- **TGD origin must be supported.** Acceptable evidence is double-conserved synteny
  (using the spotted gar "orthology bridge"), or a gene-tree duplication node at
  the base of teleosts. Pairs from the older vertebrate duplications (e.g.
  cyp26a1/cyp26b1) or younger tandem duplications are out of scope, or are used
  only as contrasts.
- **Do not trust `a`/`b` suffixes.** They are not a reliable guide to homeolog
  identity (PMID:35961774).
- **Prefer informative pairs:** pairs where at least one copy has experimental
  annotations, or published comparative work on the pair (expression, rescue,
  double mutants).
- **Mix the expected fates.** Include pairs expected to be dosage or backup cases
  (conserved enzymes), partition cases (developmental transcription factors), and
  candidate neofunctionalization cases.

### Per-pair workflow

1. `just fetch-gene DANRE <gene>` for both copies. Review each copy as usual.
2. Write a pair comparison note covering:
   - evidence of TGD origin;
   - protein-level comparison (domains, key residues, identity);
   - expression comparison (ZFIN, published in situs, PhyloFish or gar where
     available);
   - mutant, morphant and compensation evidence;
   - annotation consistency across the pair.
3. Classify the pair as one of: partition / innovation / backup / dosage /
   unresolved. Cite evidence for the classification.

### Tools

- `scripts/panther_tgd_pairs.py` finds zebrafish TGD pairs from **PANTHER v19**
  gene trees. It uses PANTHER's `AllParalogs` and `AllOrthologs` downloads, plus
  ZFIN and HGNC files for gene symbols; downloads are cached in `.cache/`, which
  is gitignored. Outputs:
  - `DANRE_DUPLICATION/panther_tgd_pairs.tsv`: candidate pairs with the evidence
    for each call.
  - `DANRE_DUPLICATION/panther_paralog_branch_counts.tsv`: zebrafish–zebrafish
    paralog pairs per duplication branch.
- `scripts/check_quotes.py` checks that every `[PMID:N "quote"]` in the project
  notes is verbatim in the cached publication (ignoring whitespace differences).

### How TGD pairs are called from PANTHER

PANTHER trees contain zebrafish, medaka, and spotted gar (the unduplicated
outgroup). For every paralog pair, PANTHER reports the tree branch that carries
the duplication, as `parent|child`. The calls, from strongest to weakest:

| Call | Rule | 1:1 pairs | All pairs |
|---|---|---|---|
| `TGD_tree` | Duplication on `Neopterygii|Teleostei`: after the gar split, before the zebrafish–medaka split. This is the TGD | 778 | 3,210 |
| `TGD_tree_no_gar` | Duplication on another branch ending at `Teleostei` (mostly `Euteleostomi|Teleostei`); no gar gene in the tree | 93 | 610 |
| `TGD_likely_parallel` | Duplication on `Teleostei|DANRE`, but both copies share one gar co-ortholog, and their medaka co-orthologs were also duplicated (`Teleostei|ORYLA`) | 1,062 | (1:1 only) |
| `TGD_or_lineage` | Duplication on `Teleostei|DANRE`, one shared gar co-ortholog, a single medaka co-ortholog. Either TGD with loss of one medaka copy, or a zebrafish-only duplication | 1,107 | (1:1 only) |
| `unresolved` | Duplication on `Teleostei|DANRE` without that gar/medaka pattern | 363 | (1:1 only) |

*1:1* means each gene has exactly one partner on that branch, i.e. a clean
ohnolog pair. From `Teleostei|DANRE` only 1:1 pairs are kept, because that branch
also holds large zebrafish-specific family expansions (40,822 pairs in all).

**Why `Teleostei|DANRE` pairs are included.** Many textbook TGD pairs are placed
there, not on the TGD branch: mitfa/b and pax6a/b come out as
`TGD_likely_parallel`, and sox9a/b as `TGD_or_lineage`. This happens because the
zebrafish and medaka copies do not group as ((zfA, medA), (zfB, medB)). That is
the gene-tree signature expected from lineage-specific resolution after delayed
rediploidization (PMID:35961774), or from poorly resolved trees. So strict
`TGD_tree` placement is conservative: it has high specificity and low
sensitivity.

**Total.** About 1,900 clean 1:1 pairs have tree-level support (`TGD_tree`,
`TGD_tree_no_gar` and `TGD_likely_parallel`), and 1,100 more are possible. That is
the same order as the 3,440 ohnolog pairs from synteny in Howe et al. 2013
(PMID:23594743).

**Caveats**

- *multi* pairs on the TGD branch include some implausible ones. For example,
  vegfaa is paired with vegfba and vegfbb, which come from an older vertebrate
  duplication. Treat multi pairs as family-level signals and check the tree.
- Some known pairs are absent. alcama/alcamb is placed at
  `Euteleostomi|DANRE`, and fabp1b does not appear in the PANTHER tables. The
  table is a PANTHER view, not a complete ohnolog catalogue.
- PANTHER places duplications by tree reconciliation. Synteny (ZFIN/Ensembl, or
  the gar bridge) remains the independent check for `TGD_or_lineage` and
  `unresolved` pairs.

## Candidate-pair triage

These tables record the starting candidate triage that was superseded by the
31-pair review set summarized above.

### Early candidates involving genes already reviewed in `genes/DANRE/`

From the initial `panther_tgd_pairs.tsv` pass:

| Pair | PANTHER call | Pair class | Partner reviewed? | Notes |
|---|---|---|---|---|
| cryaba / cryabb | TGD_or_lineage | 1:1 | yes | Pilot pair: both copies already reviewed; medaka has one co-ortholog |
| mfsd2aa / mfsd2ab | TGD_likely_parallel | 1:1 | no | LPC transporter (human MFSD2A) |
| flvcr2a / flvcr2b | TGD_likely_parallel | 1:1 | no | Human FLVCR2 |
| hs6st3a / hs6st3b | TGD_likely_parallel | 1:1 | no | Heparan sulfate 6-O-sulfotransferase 3 |
| he1.2 / he1.3 | TGD_likely_parallel | 1:1 | no | Hatching enzymes; also he1.2 / npsn as TGD_tree (multi) |
| spns1 / spns3 | TGD_tree_no_gar | 1:1 | no | Check: human has both SPNS1 and SPNS3, so this may be an older duplication |
| crppa / ispd | TGD_or_lineage | 1:1 | no | Check the symbols: ispd is a former name of CRPPA |
| rpe65a / rpe65b, rpe65c | TGD_tree | multi | no | Three copies |
| sult1st2 / sult1st5, sult1st6 | TGD_tree_no_gar | multi | no | Family expansion; weak candidate |

### Pairs with published comparative work

These pairs come from the background research.

| Pair | Published fate | PANTHER call | Reference |
|---|---|---|---|
| mitfa / mitfb | Expression partition; proteins interchangeable in rescue | TGD_likely_parallel | PMID:11543618 |
| pax6a / pax6b | cis-regulatory subfunctionalization (pancreas enhancer kept only at pax6b) | TGD_likely_parallel | PMID:18282108 |
| sox9a / sox9b | Subfunctionalization, partly lineage-specific | TGD_or_lineage | PMID:14579386 |
| elna / elnb | Subfunctionalization then neofunctionalization (bulbus arteriosus) | unresolved (no gar eln in tree) | PMID:26783159 |
| fabp1a / fabp1b | Hierarchical subfunctionalization of expression | not in PANTHER table | PMID:16857010 |
| vegfaa / vegfab | Paralog upregulation in PTC mutants (compensation) | TGD_tree (multi) | PMID:30944477 |
| hbegfa / hbegfb | Paralog upregulation in PTC mutants (compensation) | TGD_or_lineage | PMID:30944477 |
| vcla / vclb | Paralog upregulation in PTC mutants (compensation) | TGD_tree | PMID:30944477 |
| alcama / alcamb | Paralog upregulation in PTC mutants (compensation) | not called (Euteleostomi|DANRE) | PMID:30944477 |
| gpr22a / gpr22b | Clear subfunctionalization (brain vs heart), judged against gar | TGD_likely_parallel | PMID:28944589 |
| grk7a / grk7b | MIXED after review; asymmetric cone-GRK expression and a reportedly slower `grk7b` kinase | TGD_tree | [pair review](DANRE_DUPLICATION/pairs/grk7a_grk7b/grk7a_grk7b.md) |

---

# STATUS

*Last updated: 2026-10-04*

- [x] Create project page and folder
- [x] Background research on the TGD and fates of duplicates
  ([background](DANRE_DUPLICATION/DANRE_DUPLICATION-background.md); 36 publications
  cached, 85 quotes verified)
- [x] Genome-wide TGD pair calls from PANTHER v19 trees
  (`panther_tgd_pairs.tsv`; replaces the earlier Ensembl Compara script)
- [x] Decide the pair-selection strategy: targeted literature-supported pairs
  plus a random sample of `TGD_tree` pairs from `panther_tgd_pairs.tsv`
- [x] Synteny/Compara check for chosen `TGD_or_lineage` and sampled PANTHER
  pairs; `cryaba`/`cryabb`, `si:dkey-283b1.7`/`vwc2` and
  `magi3b`/`wu:fi36a10` are recorded as unconfirmed or doubtful rather than
  counted as established TGD cases
- [x] Define a pair-comparison template ([pairs/README.md](DANRE_DUPLICATION/pairs/README.md))
  and `scripts/compare_pair.py`
- [x] Batch 1, literature-supported pairs, all reviewed with pair pages:
  cryaba/cryabb, mitfa/mitfb, pax6a/pax6b, sox9a/sox9b, elna/elnb
- [x] Accession audit (`scripts/accession_audit.py`, results in
  [accession_audit.md](DANRE_DUPLICATION/accession_audit.md)). 8 of 10 genes are on the
  accession holding all their experimental GOA rows. pax6a is missing 9 ZFIN
  experimental rows and pax6b 3 UniProt rows, which sit on sibling accessions.
- [ ] Decide how to handle genes whose GOA annotations are split across UniProt
  accessions (option: let `fetch-gene` merge GOA rows from secondary accessions;
  tracked in [#3968](https://github.com/ai4curation/ai-gene-review/issues/3968))
- [x] Batch 2, literature-supported pairs, all reviewed with pair pages:
  fgf8a/fgf8b, tbx5a/tbx5b, col1a1a/col1a1b, grk7a/grk7b (grk7b updated), vcla/vclb
- [x] Batch 3: random sample of 8 `TGD_tree` 1:1 pairs (seed 20260928;
  `scripts/sample_pairs.py`, `batch3_sample.tsv`), all reviewed with pair pages
- [x] Batch 4: random sample enlarged to 18 Compara-confirmed pairs (35 draws);
  the 17 new non-`vcla` pairs were reviewed and tabulated in
  [random_sample_summary.md](DANRE_DUPLICATION/random_sample_summary.md)
  (`scripts/tabulate_sample.py`)
- [ ] Report upstream: PANTHER TGD_tree false positives (e.g. avp/oxt, myh10/myh14),
  PANTHER subfamily/ortholog errors (exoc3l2 as EXOC3L4, sh3glb2a in a drebrin-like
  subfamily, COL3A1 for col1a1a/b), and ZFIN attribution issues (col1a1a IMP genotypes;
  gad1 probe identity)
  ([#3968](https://github.com/ai4curation/ai-gene-review/issues/3968))
- [ ] Decide whether to fix PANTHER-derived symbol gaps in `panther_tgd_pairs.tsv`
  (e.g. tmc2a has no ZFIN id; tracked in
  [#3968](https://github.com/ai4curation/ai-gene-review/issues/3968))

# NOTES

## 2026-09-27

- Project created. Background research compiled from 36 cached publications. Key
  takeaways (details and quotes on the background page):
  - About 26% of zebrafish genes are TGD ohnologs (3,440 pairs; PMID:23594743).
  - Loss was rapid in the first ~60 My (PMID:26578810).
  - Using gar as the outgroup, clear neofunctionalization is 6.6% and clear
    subfunctionalization 0.8% of pairs. About 20% keep near-identical expression;
    about two-thirds are uncorrelated (PMID:28944589).
  - Regulatory divergence (93% of pairs) is far more common than protein-level
    divergence (24%) (PMID:19439512).
- **Methodological flag.** Transcriptional adaptation (PMID:30944477) means zebrafish
  PTC mutants can hide phenotypes by upregulating the paralog. When reviewing IMP
  annotations for pair members, check the allele type.
- **Ensembl Compara caveat.** Most candidate pairs are placed at the
  `Osteoglossocephalai` node rather than `Clupeocephala`. Both are plausibly TGD
  nodes, but hes6/her13 and gpat3/agpat9l look like older or unrelated paralogs.
  Synteny confirmation is needed before a pair is used.
- **Switched pair calling to PANTHER** (v19 `AllParalogs`/`AllOrthologs`). The
  trees include medaka and spotted gar, so the TGD branch
  (`Neopterygii|Teleostei`) can be read directly. Result: 778 clean 1:1 pairs on
  that branch, 93 more on teleost-stem branches in trees without gar, and 1,062
  "parallel duplication" pairs. Most literature pairs (mitfa/b, pax6a/b, gpr22a/b)
  fall in the last group, so strict branch placement alone would miss them. The
  Ensembl Compara script and its table were removed.

- **Batch 1 results** (details on each [pair page](DANRE_DUPLICATION/pairs/README.md)).
  - Three pairs are PARTITION at the expression level with the protein function
    conserved: mitfa/mitfb, sox9a/sox9b and pax6a/pax6b. For pax6 the partition
    sits on a dose-sensitive shared core (the eye).
  - Two pairs are MIXED. elna/elnb adds protein-level innovation in elnb, the one
    clear neofunctionalization case. In cryaba/cryabb both copies keep chaperone
    activity at different strengths, with an uneven expression split.
  - No pair shows pure backup; overlap is limited to shared expression domains.
  - This matches the genome-wide picture: regulatory divergence is common and
    protein divergence is rare.
- **Accession issue.** For pax6a, ZFIN's experimental annotations sit on
  RefSeq-derived TrEMBL accessions (e.g. A0A8M3AP00), not the Swiss-Prot entry
  (P26630) that was reviewed. This makes pax6a look less studied than pax6b in
  GOA. Audit the other genes before interpreting annotation gaps.
- **Deep research.** falcon ran for mitfa, sox9a/b and elna/b. It failed for mitfb
  and pax6a/b (Edison 402 Payment Required; OpenAI key invalid), so those
  literature searches were done by hand, as recorded in the gene notes.

## 2026-09-28

- **Accession audit.** For zebrafish, GOA spreads a gene's annotations over several
  UniProt entries:
  - IBA and UniProt-curated rows go to the reference-proteome or Swiss-Prot entry.
  - ZFIN's experimental rows go to RefSeq-derived TrEMBL entries.
  - For pax6a these do not overlap. P26630 has the IBAs and UniProt's IMPs;
    A0A8M9P6C7 (identical sequence) has ZFIN's 12 experimental rows. Switching
    accession would only move the gap, so pax6a stays on P26630. The missing rows
    are listed in the audit and on the pax6 pair page.
  - The 8 other genes are unaffected.
  - Batch 2 genes are audited before fetching, and each is fetched on the accession
    carrying the most experimental rows.
- **Batch 2 results.** Each gene was audited before fetching, and all ten were on
  complete accessions. Deep research failed for all nine new genes (Edison 402), so
  the literature searches were done by hand.
  - fgf8a/fgf8b: PARTITION, lopsided. fgf8a keeps most domains.
  - col1a1a/col1a1b: DOSAGE. alpha3(I) is an extra chain of the same trimer;
    double heterozygotes are fragile.
  - tbx5a/tbx5b: MIXED. Both copies are essential; the fin role is split; protein
    divergence is inferred.
  - grk7a/grk7b: MIXED. Asymmetric cone expression; grk7b is reportedly a slower
    kinase.
  - vcla/vclb: MIXED. Conserved protein with an expression-biased partition.
- **Across both batches (10 pairs).**
  - Clear protein-level innovation in only one pair (elnb). It is suspected but
    unestablished in tbx5b and grk7b.
  - No pair behaves as pure backup. Where copies overlap, the double heterozygote
    or double mutant shows a dosage requirement (pax6, col1a1, vcl).
  - The best-known "compensation" case (vcla to vclb) is mRNA-decay-triggered
    transcriptional adaptation. No protein-level substitution has been shown.
  - The partition is usually lopsided: one copy keeps most ancestral domains
    (fgf8a, tbx5a, cryabb, grk7a).
- **Curation findings worth reporting upstream.**
  - Two col1a1a "skeletal system development" IMP rows (PMID:30082390) are backed
    by col1a1b and col1a2 genotypes. This is a ZFIN gene-attribution error.
  - The PANTHER human-ortholog column lists COL3A1 for both col1a1 paralogs.
- **Batch 3 results (random sample, 8 pairs).** Each pair page carries a machine-readable
  **Sample record** line; the table is in the [pairs index](DANRE_DUPLICATION/pairs/README.md).

  | Fate | Pairs |
  |---|---|
  | PARTITION (expression) | tmc2a/tmc2b, lhfpl5a/lhfpl5b |
  | BACKUP (provisional) | smad3a/smad3b |
  | INNOVATION | none |
  | UNRESOLVED | eef1da/eef1db, abi1a/abi1b, olfm3a/olfm3b, si:dkey-283b1.7/vwc2, magi3b/wu:fi36a10 |

  - **Evidence is scarce for a typical pair.** Only 4 of 8 pairs have experimental
    data on both copies; 3 have expression data only. The literature-chosen batches
    (1-2) therefore give a much richer picture than a typical TGD pair supports.
  - **PANTHER placement is not sufficient on its own.** For 2 of 8 pairs
    (si:dkey-283b1.7/vwc2, magi3b/wu:fi36a10), Ensembl Compara and gar synteny do not
    support TGD origin: the duplication is placed deeper, or the partner is a
    divergent family member. For olfm3 the two sources disagree, although synteny
    supports duplicated segments. Pair selection should add a synteny or Compara
    check to the `TGD_tree` call.
  - **Where there is evidence, the pattern matches batches 1-2.** Proteins are
    conserved and the copies differ in where they are expressed (tmc2, lhfpl5; also
    the RNA-seq-only splits in abi1 and olfm3). The one backup call (smad3) is
    provisional: the single-mutant data were not accessible.
  - **Caution.** With n=8, none of these proportions is precise, and the absence of
    innovation in the sample is not evidence that it is rare beyond what the
    genome-wide studies already show (about 7% of pairs against gar, PMID:28944589).
- **Batch 4 and the confirmed random sample (18 pairs).** Details are in
  [random_sample_summary.md](DANRE_DUPLICATION/random_sample_summary.md).
  - **PANTHER placement alone is unreliable.** Of 34 drawn pairs with annotations, only 18
    (53%) were confirmed by Ensembl Compara. Rejected pairs include ancient paralogs such
    as avp/oxt, myh10/myh14 and hnrnpm/nucleolin.
  - **Fates:** UNRESOLVED 12, PARTITION 4, BACKUP 1 (smad3, provisional), MIXED 1 (vcl),
    INNOVATION 0.
    - Three partitions are at the expression level (tmc2, lhfpl5, prom1).
    - One is at the protein level: agxt split the ancestral dual peroxisomal and
      mitochondrial targeting signals between the copies, inferred from sequence.
  - **Evidence depth is the limiting factor.** Only 7 of 18 pairs have experimental data
    on both copies; 8 have expression data only, and 1 sequence only. Most UNRESOLVED
    calls reflect missing data, not ambiguous data.
  - **Where divergence is seen, it is mostly in expression** (11 pairs), often a
    maternal-versus-zygotic or broad-versus-restricted split with one copy gar-like.
    Protein-level signals are rare and mostly unverified:
    - agxt targeting signals;
    - guca1c/d Ca2+ sensitivity;
    - gria1b regulatory serines;
    - faster evolution of one copy in exoc3l2 and gria1.
  - **No INNOVATION in 18 random pairs.** By the rule of three this bounds its frequency
    at roughly 17% or less (95%). That is consistent with the genome-wide estimate of
    about 7% against gar (PMID:28944589).
- **Overall (literature-chosen batches 1-2 plus the random sample).**
  - The typical retained TGD pair keeps the same molecular function in both copies and
    differs in where and when each copy is expressed. The split is often lopsided, with
    one copy keeping the ancestral, gar-like pattern.
  - Clear protein-level innovation was found only in the literature-chosen elnb.
  - Pure backup was not demonstrated for any pair.
  - For GO curation this means:
    - MF annotations can usually be shared across a pair, while BP and CC need
      copy-specific evidence.
    - IBA propagation of tissue-specific processes to the non-expressing copy is the most
      common error found. Examples: sox9a heart, pax6a pancreas, lhfpl5b hearing, prom1a
      photoreceptor differentiation, agxtb peroxisome.
