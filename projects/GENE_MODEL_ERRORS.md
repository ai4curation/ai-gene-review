---
title: "Gene model errors: fused UniProt entries"
maturity: SCOPING
tags: [PIPELINE]
species: [RHOTO, 9POAL, ASPOR, HORSE, WHEAT]
genes: [NCGR_LOCUS27674, Q2U1U6, CTDSP2, A0A3B6GK97, A0A0K3C4U4, A0A0K3C6G6, A0A0K3C6K4, A0A0K3C7C1, A0A0K3C9W7, A0A0K3CA73, A0A0K3CAZ0, A0A0K3CD57, A0A0K3CDC5, A0A0K3CH38, A0A0K3CI66, A0A0K3CIB4, A0A0K3CKJ7, A0A0K3CPN4, A0A0K3CPS8]
---

# Gene model errors: fused UniProt entries

**Bottom line:** some UniProt entries are not one protein but two or more
neighbouring genes joined by a faulty gene prediction. Such an entry takes
its name, and often its GO terms, from one half, so the other gene's function
is mislabelled or lost. Working on *Rhodotorula toruloides* fitness data
([FUNGAL_PHENOTYPES/RHOTO](FUNGAL_PHENOTYPES/RHOTO.md)), we tested 59
reference-proteome entries that are at least 1.3 times longer than the
matching protein of a second strain's assembly, and found 26 that are
mostly covered by two to four separate genes of that assembly. In all 26 the
genes are neighbours. In 15, transposon mutants show that the parts act
independently: mutating one part gives a strong growth defect in some
condition while mutating its neighbour has no effect. Examples include a
3-methylcrotonyl-CoA carboxylase named "Nuclear pore complex protein Nup85"
and a branched-chain keto acid dehydrogenase fused to an amino acid
transporter. The repository already has one fused gene model
(a Miscanthus "UMP-CMP kinase") and three truncated ones, all recorded only in
review prose; the gene review schema has no field for such problems (see
Proposal).

## Why it matters for annotation review

A gene review is keyed on a UniProt accession and assumes it names one gene
product. For a fused entry that assumption fails:

- the protein name, and GO terms transferred from it, may describe the wrong
  half (A0A0K3CAZ0 is annotated to the nuclear pore, from a Nup85-like
  segment, *and* to methylcrotonoyl-CoA carboxylase activity, from the other);
- IBA/IEA annotations propagated by family membership can come from either
  half, so the entry can carry an incoherent mixture;
- a phenotype or experiment on the real gene attaches to an entry most of
  whose sequence is a different protein.

## Existing reviews with gene model problems

A text search of all `*-ai-review.yaml` files finds these, each recorded only
in the description or review prose:

| Review | Problem | How it is recorded |
|---|---|---|
| 9POAL/NCGR_LOCUS27674 | Fused: a UMP-CMP kinase joined to a chalcone isomerase-fold protein in an EVidenceModeler annotation | description and review text |
| ASPOR/Q2U1U6 | Possibly truncated model or non-catalytic fragment | description and review text |
| HORSE/CTDSP2 | Incomplete model diverging from the human ortholog | suggested question |
| WHEAT/A0A3B6GK97 | Truncated model (~100–130 residues short) lacking the catalytic serine | description and review text |

For contrast, 9POAL/NCGR_LOCUS67308 is tagged `chimeric-gene-model`, but it
is a real biological fusion (the grass `SDH2-RPS14` locus), not an annotation
error. That is the only gene-model tag in the corpus, and its meaning
differs from the cases here, which is part of the case for a controlled
field.

## Method

1. **Find candidates.** `PROTEOME_REMOVAL/scripts/resolve_deleted_accessions.py`
   maps each archived accession from the second assembly (here the IFO0880
   strain, UP000239560, deleted from UniProtKB) to its best match in the
   reference proteome (UP000199069). A current entry much longer than the
   sequence it replaced is the typical signature of a fusion.
2. **Tile.** `scripts/tile_gene_model.py` searches each candidate with phmmer
   against the second assembly's proteome, streamed from UniParc. It calls
   `FUSION` when at least two different proteins each match ≥ 100 residues at
   ≥ 90% identity, overlap by ≤ 30 residues, and together cover ≥ 70% of the
   entry. It also reports which InterPro domains fall in each segment.
3. **Check the genetics.** `scripts/rhoto_fusion_genetics.py` maps each part
   to its IFO0880 gene and RB-TDNAseq fitness profile, and records whether
   the parts are adjacent genes and whether they are genetically separated:
   in some condition one part's mutants have fitness ≤ −2.5 while another
   part's mutants have fitness > −1.

The tiling call is direction-neutral: it cannot by itself say whether the
reference entry is fused or the other assembly's genes are split. Two things
point to fusion. First, the parts often carry domains from unrelated families
(Nup85 and biotin carboxylase; E2 ubiquitin-conjugating enzyme and isocitrate
lyase; protein kinase and phosphoglucomutase). Second, genetic separation
shows that the parts act independently.

## Results (*R. toruloides*)

| Call | Entries |
|---|---|
| FUSION | 26 |
| SINGLE_GENE | 12 |
| INCONCLUSIVE | 21 |

All 26 fusions have adjacent component genes; 15 are also genetically
separated. These 15 are listed in this page's metadata.

| Entry (length) | Current name | Parts (IFO0880 gene: segment) | Separating condition |
|---|---|---|---|
| A0A0K3CAZ0 (1,419) | Nuclear pore complex protein Nup85 | RTO4_12868 Nup85-like: 1–650; RTO4_12867 biotin carboxylase (MCC α): 645–1,419 | leucine: 12867 −3.4, 12868 −0.1 |
| A0A0K3C7C1 (781) | ADP-ribose pyrophosphatase | RTO4_12623 intradiol dioxygenase: 1–368; RTO4_12624 DUF676 lipase-like: 419–686 | benzoate: 12623 −7.5, 12624 +0.3 |
| A0A0K3CA73 (754) | 2-oxoisovalerate dehydrogenase subunit α | RTO4_12567 amino acid transporter: 37–510; RTO4_12566 BCKDH E1α: 499–706 | leucine: 12566 −6.4, 12567 −0.3 |
| A0A0K3CD57 (992) | methylisocitrate lyase | RTO4_14022 isocitrate lyase: 1–571; RTO4_14021: 700–992 | oleic acid: 14022 −5.5, 14021 −0.1 |
| A0A0K3CIB4 (1,481) | Isocitrate lyase | RTO4_14161 UBE2O-like E2: 51–926; RTO4_14162 isocitrate lyase family: 901–1,481 | valine: 14162 −4.5, 14161 −0.1 |
| A0A0K3CKJ7 (938) | Amidohydrolase family protein | RTO4_10305 OTU domain: 1–381; RTO4_10306 amidohydrolase: 380–938 | phenylalanine: 10305 −5.5, 10306 −0.5 |
| A0A0K3C6G6 (1,978) | ER Ca-transporting P-type ATPase | RTO4_8483 P5A-ATPase; RTO4_8481; RTO4_8482 tyrosyl-DNA phosphodiesterase | benzoate: 8483 −4.1, 8482 +0.7 |
| A0A0K3C6K4 (1,433) | Protein-S-isoprenylcysteine O-methyltransferase | RTO4_12259 small GTPase; RTO4_12258 `Pal1`; RTO4_12257 isoprenylcysteine methyltransferase; RTO4_12256 | benzoate: 12259 −3.4, 12258 +0.6 |
| A0A0K3C4U4 (1,547) | Proteophosphoglycan ppg4 | RTO4_8965 APSES transcription factor: 1–466; RTO4_8966 F-box: 471–1,525 | benzoate: 8965 −3.8, 8966 +0.4 |
| A0A0K3CPS8 (704) | Succinate dehydrogenase assembly factor 3 | RTO4_11204 `TRIP4`-type zinc finger: 1–496; RTO4_11205 SDHAF3: 529–704 | ferulate: 11205 −2.8, 11204 +0.1 |
| A0A0K3CI66 (1,306) | `eIF3` subunit E | RTO4_14106 Serrate RNA effector; RTO4_14105 SERRATE/Ars2 C-term; RTO4_14104 `eIF3e` | p-coumarate: 14105 −2.8, 14106 −0.6 |
| A0A0K3CDC5 (1,070) | Membrane protein | RTO4_12145 GOLD/p24: 1–216; RTO4_12144 FHA + RING: 216–1,070 | leucine: 12145 −3.0, 12144 −0.9 |
| A0A0K3C9W7 (1,287) | Peptide hydrolase | RTO4_12450 M28 peptidase: 19–965; RTO4_12451 NUBPL-like: 1,098–1,287 | lactate: 12451 −2.9, 12450 −0.2 |
| A0A0K3CH38 (1,641) | Proteophosphoglycan ppg4 | RTO4_13662 Rad1/Rec1/Rad17: 1–363; RTO4_13661: 362–1,641 | lactate: 13662 −2.6, 13661 0.0 |
| A0A0K3CPN4 (1,297) | predicted protein | RTO4_16676 GNAT; RTO4_16675; RTO4_16674; RTO4_16673 | benzoate: 16675 −3.6, 16676 +0.8 |

The two isocitrate lyase-family entries are worth a closer look. The part of
A0A0K3CD57 ("methylisocitrate lyase") is needed on oleate and acetate, as
the glyoxylate-cycle isocitrate lyase would be; the part of A0A0K3CIB4
("Isocitrate lyase") is needed on valine, whose breakdown yields
propionyl-CoA and runs through the methylcitrate cycle. The phenotypes
therefore suggest the two names are swapped. This is a hypothesis from
growth data, not an established assignment.

### Scope and caveats

- Only entries linked to a carbon-source fitness defect were screened (59 of
  them), so 26 fusions is not an estimate of the rate in the whole
  reference proteome; a proteome-wide screen is the obvious next step.
- `INCONCLUSIVE` (21) covers entries tiled by one protein over too little of
  their length, or by segments below the identity threshold. Some will be
  fusions with a component missing from the IFO0880 annotation.
- Genetic separation needs a condition where one part has a phenotype, so
  fusions of two unphenotyped genes cannot be confirmed this way.

## Proposal: recording gene model problems

Nothing in the schema can carry this today. GeneReview has free-text `tags`
(used once, inconsistently, as above), and the prediction-review error enum
has `WRONG_INPUT_SEQUENCE` for pipeline errors, but neither says what is wrong
with the entry, or distinguishes an annotation artifact from a real
biological fusion. A structured slot on
GeneReview would let a review say "this accession is a fusion of A and B;
this review covers part A", for example:

```yaml
gene_model_issues:
  - issue_type: FUSED_GENE_MODEL   # also SPLIT_GENE_MODEL, TRUNCATED_MODEL, WRONG_START
    components:
      - comparison_accession: A0A2T0ACW0   # IFO0880, archived in UniParc
        segment: 645-1419
        description: 3-methylcrotonyl-CoA carboxylase biotin-carboxylase subunit
      - comparison_accession: A0A2T0ACV7
        segment: 1-650
        description: Nup85-like nucleoporin
    evidence: [TILING, ADJACENT_GENES, GENETIC_SEPARATION]
    reviewed_segment: 645-1419
    supported_by:
      - reference_id: file:projects/GENE_MODEL_ERRORS/data/rhoto_fusion_genetics.tsv
```

Until then, `data/rhoto_fusion_genetics.tsv` is the structured record (one
row per fused entry, with parts, adjacency, the separating condition and an
evidence list), and this page's `genes` metadata lists the four existing reviews above
and the 15 genetically separated *R. toruloides* entries.

## Next steps

1. Decide on the schema slot above (or an alternative) before the first
   *R. toruloides* gene reviews, since several candidates (BCKDH E1α, MCC α,
   the aromatic dioxygenase) sit in fused entries.
2. Once a field exists, back-fill the four existing reviews above.
3. Run the tiling screen across the whole UP000199069 reference proteome
   against IFO0880, not just phenotype-linked entries.
4. Report the 15 genetically separated fusions to UniProt.
5. Look for fusions in reviewed species by the same route: any organism with
   two independent assemblies in UniParc can be screened.

## Files

- `scripts/tile_gene_model.py` (needs `uv run --with pyhmmer`) →
  `data/rhoto_fusion_screen.tsv`
- `scripts/rhoto_fusion_genetics.py` → `data/rhoto_fusion_genetics.tsv`

Reproduce from the repository root after the FUNGAL_PHENOTYPES/RHOTO pipeline
(which caches the supplements and writes the resolution table):

    uv run --with pyhmmer python projects/GENE_MODEL_ERRORS/scripts/tile_gene_model.py \
        --from-resolution projects/FUNGAL_PHENOTYPES/data/rhoto_accession_resolution.tsv \
        --comparison-proteome UP000239560 \
        --out projects/GENE_MODEL_ERRORS/data/rhoto_fusion_screen.tsv
    uv run python projects/GENE_MODEL_ERRORS/scripts/rhoto_fusion_genetics.py
