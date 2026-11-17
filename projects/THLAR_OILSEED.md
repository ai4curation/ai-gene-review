---
title: "Pennycress (Thlaspi arvense) Oilseed Domestication Genes"
maturity: IN_PROGRESS
last_reviewed: 2026-11-04
tags: [BIOLOGY_DOMAIN]
species: [THLAR, ARATH]
genes: [FAE1, TFP, CYP71B1, matK, TAV2_LOCUS3068, TAV2_LOCUS7508, TAV2_LOCUS14099, CSD1, CSD2]
---

# Pennycress (Thlaspi arvense) Oilseed Domestication Genes

**Bottom line:** Field pennycress is a wild Brassicaceae being turned into a winter
oilseed cover crop, mostly by knocking out genes whose Arabidopsis orthologs are well
understood. Only three pennycress proteins are in Swiss-Prot (CYP71B1, TFP, matK), and all
three are already reviewed here. Everything else in the proteome (UP000836841, about 26,400
proteins) is unreviewed TrEMBL with electronic-only GO annotations. The pennycress mutant
papers are therefore a direct source of organism-specific experimental evidence (IMP) that
GOA does not yet have. The pilot gene, FAE1, is reviewed: its 6 IEA annotations are all
consistent with the literature (2 accepted, 2 made more specific, 2 kept as non-core), and
one new IMP annotation (very long-chain fatty acid biosynthetic process) is proposed from
the pennycress CRISPR knockouts.

## Why pennycress

- Domestication traits map onto single genes with strong knockout phenotypes in pennycress
  itself (oil composition, seed coat, glucosinolates, flowering habit, pod shatter, dormancy).
- Arabidopsis orthologs are already reviewed in this repo (e.g.
  <gene species="ARATH" symbol="FAE1">FAE1</gene>, TT8, TTG1, FLC, CBF1, WRI1,
  DGAT1, FAD2), so each pennycress review can be checked against its ortholog.
- The glucosinolate-myrosinase defence system links the existing TFP review to sulfate
  assimilation modules and is not yet represented as a module.

## Working with TrEMBL entries

- Most proteome entries carry only a locus name (`TAV2_LOCUS...`). Identify genes by
  orthology, and prefer a named entry with literature when one is identical or nearly
  identical to the proteome entry.
- FAE1 is reviewed on V9XY07 (named, cited). It differs from the proteome entry
  A0AAU9T3A1 / `TAV2_LOCUS26079` at 1 of 506 residues. Fetched with
  `just fetch-gene THLAR V9XY07 --alias FAE1`.
- **Species trap:** metal hyperaccumulation work (HMA4, ZIP transporters, Cd/Zn/Ni
  tolerance) was done in *Noccaea caerulescens*, formerly *Thlaspi caerulescens*, not in
  *T. arvense*. Check the species in every paper.

## Gene list

| Gene | UniProt | Theme | Status |
|------|---------|-------|--------|
| FAE1 | V9XY07 | Seed oil: erucic acid (VLCFA) | Reviewed (pilot) |
| TFP | G1FNI6 | Glucosinolate breakdown | Reviewed (earlier) |
| CYP71B1 | P49264 | Specialized metabolism, function unknown | Reviewed (earlier) |
| matK | Q9GF35 | Chloroplast intron splicing | Reviewed (earlier) |
| TAV2_LOCUS3068 (DCL1) | A0AAU9RFA2 | miRNA biogenesis (`miR162` homeostatic target) | Reviewed |
| TAV2_LOCUS7508 (APS1) | A0AAU9RRK7 | Sulfate activation / glucosinolates (`miR395` target) | Reviewed |
| TAV2_LOCUS14099 (LAC4) | A0AAU9S9S2 | Lignification / pod shatter (`miR397` target) | Reviewed |
| FAD2, ROD1, FAD3 | to identify | Seed oil: oleic vs. polyunsaturated | Planned |
| TT8, TT2, TTG1 | to identify | Seed coat, fibre, dormancy | Planned |
| MYB28, MYC3, GTR1/2, AOP2 | to identify | Seed glucosinolate | Planned |
| FLC, FRI, IND, ALC, DOG1 | to identify | Flowering habit, pod shatter, dormancy | Planned |

## FAE1 pilot: findings

- **Activity:** fatty acid elongase activity (the KCS condensation step) accepted. Pennycress
  FAE1 raises erucic acid when expressed in Arabidopsis seed (PMID:32740897), and CRISPR
  knockouts in pennycress remove erucic acid from seed oil (PMID:30230695).
- **Process:** `fatty acid biosynthetic process` sharpened to `very long-chain fatty acid
  biosynthetic process`, and that term added as a new IMP annotation. FAE1 catalyses a step
  of the process, so this is participation, not just requirement.
- **Not added:** triglyceride biosynthesis. FAE1 makes the acyl-CoA that DGAT1 and other
  acyltransferases put into oil; it does none of the acylation itself.
- **Location:** `membrane` sharpened to ER membrane. There is no pennycress localization
  data; this rests on the conserved ER elongase.

## Modules

- **Fatty acid elongation** (`modules/fatty_acid_elongation_cycle.yaml`, updated). The
  condensation step is now a choice between two unrelated enzyme families that carry out
  the same reaction: animal and fungal ELOVLs, and plant 3-ketoacyl-CoA synthases (KCS).
  The KCS variant uses Arabidopsis <gene species="ARATH" symbol="FAE1">FAE1</gene> and CER6
  and pennycress FAE1 as examples, and cites the PAINT node PTN000774398. The other three
  steps of the cycle are carried out by orthologous enzymes in plants and animals, so each
  now lists an Arabidopsis example (KCR1, PAS2, ECR/CER10) alongside the human one.
- **Glucosinolate-myrosinase defense**
  (`modules/aliphatic_glucosinolate_myrosinase_defense.yaml`, new). It has five parts:
    1. methionine chain elongation (BCAT4, MAM, IPMI, IPMDH1, BCAT3)
    2. core structure (CYP79F, CYP83A1, GSTU20, GSTF11, GGP1, SUR1, UGT74C1,
       SOT17, SOT18)
    3. side-chain modification (FMO GS-OX, AOP2), which is optional
    4. myrosinase hydrolysis (TGG1, TGG2)
    5. specifier proteins (ESP, NSP, and pennycress TFP), which are optional

    Each step cites a primary paper. Pennycress seed glucosinolate is mostly sinigrin
    (allylglucosinolate), which requires a working AOP2. The Arabidopsis Columbia AOP2 is
    inactive, so the module uses the functional Cvi-0 allele as its example.

All 28 Arabidopsis example enzymes named in these two modules now have full gene reviews
(`genes/ARATH/<GENE>/`), as does pennycress FAE1. Things the reviews found that bear on
the modules:

- **Missing GO terms:** GO has no activity term for the CYP83A1 or AOP2 reactions, or for
  the specific ESP, NSP1 and TFP specifier reactions. Each review proposes one.
- **Paralog mis-propagation:** leucine-biosynthesis annotations on MAM1 were inherited
  from its IPMS paralogs, and MAM1 shows no IPMS activity, so they are removed. MAM3 does
  have weak IPMS activity, so that annotation is kept as non-core.
- **Chain-elongation process term withdrawn:** BCAT4, BCAT3, MAM1 and MAM3 briefly carried the
  unused term `L-homomethionine biosynthetic process` (GO:0033322). It was withdrawn because GO has
  obsoleted its sibling terms as pathway variants out of scope, pointing to glucosinolate
  biosynthetic process instead. It is kept as a question for GO in each review.
- **Disputed ESP evidence:** the ESP leaf-senescence and defence annotations come from a
  study in Columbia, whose leaves are reported to have essentially no ESP. They are kept
  as non-core, not removed.

## Pennycress orthologs

`THLAR_OILSEED/ortholog_mapping/` holds a reproducible reciprocal-best-hit search of every
Arabidopsis enzyme in the two modules against the pennycress reference proteome and back.
The calls, with reasons, are in [CALLS.md](THLAR_OILSEED/ortholog_mapping/CALLS.md).

- **One-to-one:** 13 enzymes have clear one-to-one pennycress orthologs at 83-96% identity.
  11 of them are now module examples (for instance BCAT4, MAM1, SUR1, SOT17, KCR1, ECR and
  CUT1). Pennycress FAE1 was already in the module as V9XY07, and CYP83A1 is left out because
  its PANTHER family differs between sources.
- **Expanded families:** pennycress has at least five TGG1-like myrosinases and at least four
  SOT18-like sulfotransferases.
- **Single genes:** one pennycress gene corresponds to both Arabidopsis CYP79F1 and CYP79F2,
  and one to both SSU2 and SSU3.
- **No counterpart found:** MAM3, FMOGS-OX1 and NSP1. A missing MAM3 would fit seed
  glucosinolate dominated by the one-turn product sinigrin, but absence from a set of
  predicted genes is not proof of loss.
- **No true ESP:** the pennycress protein that best matches Arabidopsis ESP is 84% identical
  to pennycress TFP, so it is a TFP-like paralog.
- **Gene-model problems:** the AOP2, UGT74C1 and PAS2 matches sit in partial or fused gene
  models.
- **AOP2 is intact in the genome.** The predicted AOP2 protein is a fragment, but the genome
  carries the complete AOP2-type coding sequence, 84% identical to Brassica rapa AOP2. The
  annotation treated 568 bp of real coding sequence as intron, most of it one 474 bp false
  intron. This fits pennycress making
  sinigrin, which needs a working AOP2. Details are in
  [CALLS.md](THLAR_OILSEED/ortholog_mapping/CALLS.md#aop2-gene-model).

## Pennycress & plant miRNA–target datasets

`THLAR_OILSEED/mirna_targets/` holds the curated *Thlaspi arvense* and *Arabidopsis thaliana*
miRNA–target datasets, cross-mapped to the `T_arvense_v2` reference genome (`GCA_911865555.2`)
and UniProt proteome (`UP000836841`). Full documentation is in
[README.md](THLAR_OILSEED/mirna_targets/README.md).

- **`thlar_mirna_loci_72.tsv` (72 rows):** All 72 ShortStack-predicted pennycress miRNA loci
  from Nunn et al. 2022 (PMID:34990041 / PMC9055812, Additional file 2 Table S12), including 46
  conserved loci across 22 miRNABase families (`miR156` to `miR824`) and 26 novel pennycress-specific
  candidate miRNAs.
- **`thlar_mirna_targets.tsv` (88 rows across 73 unique `TAV2_LOCUS` genes):** High-confidence
  pennycress `miRNA -> target` interactions combining the 16 Nunn et al. 2022 Table S15 targets
  (such as `tar-miR156 -> SPL9/SPL13`, `tar-miR157 -> FLC`, `tar-miR160 -> ARF17`, and
  `tar-miR395 -> APS1/APS3/APS4`) with 72 conserved Brassicaceae miRNA–target modules mapped via
  orthology and direct target-site alignment on `T_arvense_v2` transcripts (`Allen_Score <= 2.5`).
- **`tardb_ath_degradome.tsv` (168 rows):** Experimentally supported *Arabidopsis thaliana*
  degradome/PARE cleavage interactions from TarDB across 39 miRNA families (`Allen_Score <= 2.0`,
  degradome `P < 0.05`).
- **`goa_tair_mirna_annotations.tsv` (54 rows):** Audit of all *Arabidopsis thaliana* EBI GOA RNA
  (`goa_arabidopsis_rna.gaf.gz`) and TAIR (`tair.gaf.gz`) annotations to `GO:1903231`
  (`mRNA binding involved in post-transcriptional gene silencing`) and `GO:0035195` (`miRNA-mediated
  post-transcriptional gene silencing`) and its descendants.

### Curation findings from miRNA-regulated gene reviews

- **Pennycress `DCL1` (`TAV2_LOCUS3068` / `A0AAU9RFA2`, `tar-miR162` target):** Primary RNase III
  endoribonuclease that processes plant `pri-miRNA` and `pre-miRNA` hairpins into mature 20-24 nt
  miRNA/miRNA* duplexes (`GO:0031053` primary miRNA processing, proposed as `NEW` `ISS` from
  `UniProtKB:Q9SP32`). Its own mRNA is cleaved by `tar-miR162` (`Allen_Score = 1.0`) in a conserved
  negative feedback loop that maintains DCL1 homeostasis, making DCL1 both an actor in and a
  substrate of `GO:0035195`. False IEA mappings inherited from animal Dicer and fungal nuclear-export
  orthologs (`GO:0000976` transcription cis-regulatory region binding, `GO:0006355` regulation of
  DNA-templated transcription, and `GO:0006406` mRNA export from nucleus) are removed.
- **Pennycress `APS1` (`TAV2_LOCUS7508` / `A0AAU9RRK7`, `tar-miR395` target):** Plastid-targeted
  ATP sulfurylase (`GO:0004022` sulfate adenylyltransferase (ATP) activity) that activates inorganic
  sulfate into APS at the entry point of the glucosinolate PAPS donor pathway (`GO:0019344` cysteine
  biosynthetic process and `GO:0019761` glucosinolate biosynthetic process proposed as `NEW` `ISS`
  from `UniProtKB:Q42559`). Although `tar-miR395a-f` directs cleavage of `TAV2_LOCUS7508` mRNA
  (`Allen_Score = 1.0`, PMID:34990041 Table S15), `APS1` is the substrate of RISC cleavage and is
  therefore not annotated to `GO:0035195`.
- **Pennycress `LAC4` (`TAV2_LOCUS14099` / `A0AAU9S9S2`, `tar-miR397` target):** Secreted apoplastic
  multi-copper oxidase (`GO:0052716` hydroquinone:oxygen oxidoreductase activity) that oxidizes
  monolignols for secondary cell wall and silique valve-margin lignification (`GO:0009809` lignin
  biosynthetic process, replacing broad `GO:0009808`). Targeted by `tar-miR397a/b` (`Allen_Score = 0.5`)
  to balance copper allocation and stem/pod lignification; as an mRNA substrate of `miR397`-RISC,
  `LAC4` is not annotated to `GO:0035195`.
- **Substrate-vs-actor mis-annotations in *Arabidopsis* (`ARATH/CSD1` and `ARATH/CSD2`):** Audit of
  `goa_tair_mirna_annotations.tsv` revealed that only three *Arabidopsis* mRNA target genes (`CSD1`,
  `CSD2`, and `PXMT1`) are annotated to `GO:0035195` (`miRNA-mediated post-transcriptional gene
  silencing`), all via `IEP`. Reviews of <gene species="ARATH" symbol="CSD1">CSD1</gene> (`P24704`)
  and <gene species="ARATH" symbol="CSD2">CSD2</gene> (`O78310`) remove `GO:0035195` (`PMID:16861386`)
  because `CSD1` and `CSD2` mRNAs are the cleaved substrates of `miR398`-loaded RISC rather than
  participants in the silencing machinery.

## Next steps

Tracked in [ai-gene-review#4015](https://github.com/ai4curation/ai-gene-review/issues/4015).

1. Review the other oil-composition genes (FAD2, ROD1) using PMID:33968108.
2. Report the pennycress gene-model errors to the assembly or annotation maintainers: AOP2
   (TAV2_LOCUS22152, a false intron), the AOP1-like fusion (TAV2_LOCUS20419) and PAS2 (fused
   to an MSL2-like gene). Check the PAS2 locus the same way as AOP2.
3. Review the glucosinolate regulators targeted in domestication (MYB28, MYC3;
   PMID:41578087). They are deliberately outside the module.
4. Seed coat and weediness: TT8 knockout (PMID:41578087; PMID:41685867).

## Key literature (PMIDs checked against PubMed)

- PMID:30230695 — molecular tools and CRISPR fae1 knockouts in pennycress.
- PMID:33968108 — fad2 and rod1 stacked with fae1 for high-oleic oil.
- PMID:39657724 — multi-omics of the fae1 knockout.
- PMID:32740897 — functional analysis of pennycress FAE1 in Arabidopsis.
- PMID:41578087 — stacking domestication traits by CRISPR (Nature Plants 2026).
- PMID:41685867 — tt8-2bp seed-coat anatomy and chemistry in pennycress.
- PMID:39470818 — review of pennycress domestication and engineering.
- PMID:34990041 — chromosome-level *Thlaspi arvense* genome (`T_arvense_v2`), sRNA-seq of 72 miRNA loci, and target predictions.
- PMID:16861386 — post-transcriptional regulation of *Arabidopsis* `CSD1` and `CSD2` by `miR398` during oxidative stress.
