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

- `scripts/tgd_paralogs.py` queries Ensembl Compara for within-species paralogs of
  the reviewed zebrafish genes whose duplication node is at a teleost level
  (Clupeocephala / Osteoglossocephalai). Output:
  `DANRE_DUPLICATION/reviewed_gene_tgd_paralogs.tsv`. The list is a **candidate**
  list only. Compara node placement needs checking against synteny.
- `scripts/check_quotes.py` checks that every `[PMID:N "quote"]` in the project
  notes is verbatim in the cached publication (ignoring whitespace differences).

## Candidate pairs

### From genes already reviewed in `genes/DANRE/`

These come from Ensembl Compara (Ensembl REST, queried 2026-09-27). Each needs a
synteny check before it counts as a TGD pair.

| Reviewed gene | Paralog | Compara node | Partner reviewed? | Notes |
|---|---|---|---|---|
| cryaba | cryabb | Clupeocephala | yes | Best first pair: both copies already reviewed |
| hs6st3b | hs6st3a | Clupeocephala | no | Heparan sulfate 6-O-sulfotransferase |
| mfsd2aa | mfsd2ab | Osteoglossocephalai | no | LPC transporter; human MFSD2A |
| flvcr2a | flvcr2b | Osteoglossocephalai | no | Heme/choline transporter family |
| grk7b | grk7a | Osteoglossocephalai | no | Cone opsin kinase; possible photoreceptor-type partition |
| glceb | glcea | Osteoglossocephalai | no | Heparan sulfate C5-epimerase |
| rpe65a | rpe65b, rpe65c | Osteoglossocephalai | no | Three copies; the c copy may be a younger duplicate. Check |
| coq8a | coq8ab | Osteoglossocephalai | no | Check ZFIN symbol for the reviewed copy |
| tdp2 | tdp2a | Osteoglossocephalai | no | |
| hes6 | her13 | Osteoglossocephalai | no | Doubtful as a TGD pair; her genes have a complex history |
| gpat3 | agpat9l | Osteoglossocephalai | no | Doubtful; check synteny |

### Pairs with published comparative work

These pairs come from the background research.

| Pair | Published fate | Reference |
|---|---|---|
| mitfa / mitfb | Expression partition; proteins interchangeable in rescue | PMID:11543618 |
| pax6a / pax6b | cis-regulatory subfunctionalization (pancreas enhancer kept only at pax6b) | PMID:18282108 |
| sox9a / sox9b | Subfunctionalization, partly lineage-specific | PMID:14579386 |
| elna / elnb | Subfunctionalization then neofunctionalization (bulbus arteriosus) | PMID:26783159 |
| fabp1a / fabp1b | Hierarchical subfunctionalization of expression | PMID:16857010 |
| vegfaa / vegfab, hbegfa / hbegfb, alcama / alcamb | Paralog upregulation in PTC mutants (compensation) | PMID:30944477 |
| gpr22 ohnologs | Clear subfunctionalization (brain vs heart), judged against gar | PMID:28944589 |

---

# STATUS

*Last updated: 2026-09-27*

- [x] Create project page and folder
- [x] Background research on the TGD and fates of duplicates
  ([background](DANRE_DUPLICATION/DANRE_DUPLICATION-background.md); 36 publications
  cached, 85 quotes verified)
- [x] Candidate-pair script (Ensembl Compara) run on the reviewed zebrafish genes
- [ ] Decide the pair-selection strategy (targeted list, or a random sample of
  ohnologs, e.g. drawn from the Howe 2013 or Parey 2022 ohnolog sets)
- [ ] Confirm TGD origin (synteny or gar bridge) for the candidate pairs
- [ ] Pilot pair: cryaba / cryabb, side-by-side comparison of the existing reviews
- [ ] Define a pair-comparison template (markdown, or a schema extension)
- [ ] Review 5–10 further pairs across the expected fates

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
