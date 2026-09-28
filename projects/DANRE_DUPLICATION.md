---
title: "Zebrafish Genome Duplication and Paralog Pairs"
maturity: SCOPING
tags: [BIOLOGY_DOMAIN]
species: [DANRE]
genes: [cryaba, cryabb]
---

# Zebrafish Genome Duplication and Paralog Pairs

**Bottom line:** Zebrafish keeps about 3,440 ohnolog pairs from the teleost-specific
genome duplication (TGD), roughly 320–350 Mya. This project will review such pairs
side by side and ask what happened to the ancestral function in each case:

- **Partition (subfunctionalization):** the two copies split the ancestral functions.
- **Innovation (neofunctionalization):** one copy gained a new function.
- **Backup (redundancy or dosage retention):** both copies keep the same function.

The first phase is background research, summarized in
[Background research](DANRE_DUPLICATION/DANRE_DUPLICATION-background.md).

- **Main finding so far:** most retained pairs diverged in *where and when* they are
  expressed rather than in *what the protein does*.
- **Clean cases are rare.** Only a small minority are clear cases of
  neofunctionalization or subfunctionalization, when judged against an unduplicated
  outgroup (spotted gar).
- **Next step:** choose pairs and run the first side-by-side review
  (cryaba/cryabb, which are already both reviewed).

## Motivation

A zebrafish gene often corresponds to one human gene through two "co-orthologs"
(the `a`/`b` pairs in ZFIN nomenclature). This matters for GO annotation in three
ways:

1. **Experimental annotations are split between the copies.** A zebrafish IMP or IDA
   is made on *one* copy. Whether it transfers to the other copy, or to the human
   ortholog, depends on whether the copies diverged in molecular function or only
   in expression.
2. **Phylogenetic propagation treats the copies as equivalent.** IBA and ISO usually
   give both copies the same terms. That is right for the backup and partition
   fates, but may be wrong for neofunctionalized copies.
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

## Candidate pairs

### Pairs involving genes already reviewed in `genes/DANRE/`

From `panther_tgd_pairs.tsv`:

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
| grk7a / grk7b | Not yet reviewed; cone photoreceptor kinases | TGD_tree | |

---

# STATUS

*Last updated: 2026-09-27*

- [x] Create project page and folder
- [x] Background research on the TGD and fates of duplicates
  ([background](DANRE_DUPLICATION/DANRE_DUPLICATION-background.md); 36 publications
  cached, 85 quotes verified)
- [x] Genome-wide TGD pair calls from PANTHER v19 trees
  (`panther_tgd_pairs.tsv`; replaces the earlier Ensembl Compara script)
- [ ] Decide the pair-selection strategy: a targeted list, or a random sample of
  1:1 `TGD_tree` / `TGD_likely_parallel` pairs from `panther_tgd_pairs.tsv`
- [ ] Synteny check for `TGD_or_lineage` pairs chosen for review (including
  cryaba/cryabb)
- [x] Define a pair-comparison template ([pairs/README.md](DANRE_DUPLICATION/pairs/README.md))
  and `scripts/compare_pair.py`
- [x] Batch 1, literature-supported pairs, all reviewed with pair pages:
  cryaba/cryabb, mitfa/mitfb, pax6a/pax6b, sox9a/sox9b, elna/elnb
- [x] Accession audit (`scripts/accession_audit.py`, results in
  [accession_audit.md](DANRE_DUPLICATION/accession_audit.md)). 8 of 10 genes are on the
  accession holding all their experimental GOA rows. pax6a is missing 9 ZFIN
  experimental rows and pax6b 3 UniProt rows, which sit on sibling accessions.
- [ ] Decide how to handle genes whose GOA annotations are split across UniProt
  accessions (option: let `fetch-gene` merge GOA rows from secondary accessions)
- [ ] Batch 2: further literature-supported pairs (e.g. vcla/vclb, vegfaa/vegfab,
  hbegfa/hbegfb, gpr22a/gpr22b, grk7a/grk7b), then a random sample of
  `TGD_tree` 1:1 pairs

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
