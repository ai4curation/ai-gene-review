---
title: "Re-examining the RAR misannotation study (Wei et al. 2020)"
maturity: IN_PROGRESS
last_reviewed: 2026-10-18
tags: [EVALUATION]
collections: [HOMOLOGY_PROPAGATION]
species: [ARATH, worm, DROME, mouse, human, CHICK]
---

# Re-examining the RAR misannotation study (Wei et al. 2020)

**Bottom line:** Wei *et al.* (2020) flagged 190 GO annotations in UniProt-GOA
2019-06-03 and 250 in 2018-11-06 as probable misannotations, using taxon-specific
annotation-rate ratios (RAR) followed by manual review
[PMID:32470107 "Detecting Gene Ontology misannotations using taxon-specific rate ratio comparisons."].
We rebuilt their complete case list from the supplement and checked every
protein–term pair against current GOA. Of the 290 distinct pairs, **216 are gone
from GOA**, 36 more vanished with their UniProt entry, and **38 persist**. Most of
the paper's calls therefore hold up and have been acted on. The survivors contain
one clear error by the paper: plant **lipid A biosynthesis** (25 of the 38 pairs),
which experimental work shows Arabidopsis really has
[PMID:21709257 "our work demonstrates that plants synthesize lipid A precursors using the same enzymatic pathway present in E. coli"].
They also contain one moot case (a GO term since renamed to a general meaning)
and a handful of animal annotations that still look wrong. The paper's two
best-known IBA case studies were right on the facts, but its reasoning for one of
them (plant DDL) was wrong.

This project is a companion to [IBA_REVIEW](IBA_REVIEW.md): the paper's headline
claim is that IBA had become the main source of non-electronic GO errors, and
its main mechanism (terms placed at a PAINT node deeper than the evidence
supports) is the same as the `LINEAGE_OR_TAXON_MISMATCH` pattern catalogued
there and the pathway-level problem in [TAXON_PATHWAY_VARIANCE](TAXON_PATHWAY_VARIANCE.md).

## The paper's method and claims

For a GO term *q*, the annotation rate in taxon *t* is the fraction of that
taxon's annotated proteins that carry *q*; RAR is the minimum rate over taxa
divided by the maximum. The authors computed RAR for five kingdoms (animals,
bacteria, archaea, fungi, plants; 20 reference proteomes) and for vertebrates
versus invertebrates, then manually inspected every term with RAR < 0.1.

| # | Claim | Our assessment |
|---|-------|----------------|
| C1 | 190 (2019-06-03) and 250 (2018-11-06) manually confirmed misannotations, over 43 and 50 terms | **Reproduced.** Our reconstruction from the supplement matches Table 1 on every line (terms, proteins, annotations). |
| C2 | Most flagged annotations are wrong | **Largely holds.** 216 of 254 pairs on still-active entries have since been removed from GOA. One family of flags (plant lipid A, 25 pairs) is refuted by experiment. |
| C3 | 56% of flagged errors are IBA, overtaking ISS as the main non-IEA error source | **Plausible for 2018–19.** The supplement only records each term's most frequent evidence code, so this cannot be re-counted per pair. |
| C4 | Only 25% were fixed six months later | **Superseded.** About 85% of pairs on still-active entries are now gone (see [Results](#results)). |
| C5 | *B. subtilis* Udg (P39615) wrongly gets IBA `nucleus` and `mitochondrion` from a root-placed PAINT node (PTN000137400) | **Holds; fixed.** These rows are gone; P39615, P56397 and P12295 keep only the `uracil DNA N-glycosylase activity` and `base-excision repair, AP site formation via deaminated base removal` IBAs. QuickGO now returns 0 bacterial annotations to `GO:0005634` or `GO:0005739`. |
| C6 | Arabidopsis DDL (A0A1I9LPE3) wrongly gets IBA `peptidoglycan biosynthetic process`, because plant walls are cellulose | **Conclusion holds; reasoning wrong.** See [DDL](#ddl-in-arabidopsis). |
| C7 | Human JUP wrongly gets IC `structural constituent of cell wall` | **Holds; fixed.** GOA keeps only NAS `GO:0005198 structural molecule activity`. |
| C8 | A low RAR can be biologically correct (Salmonella SspH2 E3 ligase) | Agreed. This is why the screen needs manual review: only ~9% of RAR < 0.1 terms were confirmed (Supplementary Table S2). |
| C9 | GOA error rate ≈ 7%, IBA ≈ 31%, estimated from later NOT annotations vs later confirmations | **Biased upward for IBA.** NOT annotations are made to counter propagated annotations, so IBA scores high by construction. |
| C10 | 12 of 43 flagged terms violated existing GO taxon constraints | Not re-checked; GO's constraints have changed since. |
| C11 | neXtProt would downgrade IBA from "Gold" to "Silver" | **Unverified.** See [neXtProt](#the-nextprot-claim). |

## Results

Scripts and data are in [RAR_MISANNOTATION/](RAR_MISANNOTATION/README.md).
The current-status check was run on 2026-10-18 against QuickGO and UniProt.

| Release flagged | Pairs | Removed from GOA | Entry deleted/merged | Still annotated |
|---|---:|---:|---:|---:|
| 2019-06-03 | 190 | 144 | 33 | 13 |
| 2018-11-06 | 250 | 191 | 26 | 33 |
| Distinct pairs (both releases) | 290 | 216 | 36 | 38 |

Removal is not proof that a pair was wrong: PAINT re-runs, InterPro2GO changes
and accession changes all remove rows. But it agrees with the paper's call in
almost every case we looked at, and none of the removed terms needs a second
look (bacterial `nucleus`/`mitochondrion`/`nucleolus`, animal `fungal-type
vacuole membrane` and `cell wall mannoprotein biosynthetic process`, fly
`inflammatory response`, and so on).

### The 38 surviving pairs

| Term | Proteins (taxon, evidence) | Verdict on the paper's flag |
|---|---|---|
| `GO:0009245` lipid A biosynthetic process | 25 Arabidopsis and Selaginella proteins (IBA from E. coli LpxA/LpxB/LpxD nodes; InterPro2GO IEA) | **Paper wrong.** Arabidopsis has LpxA, LpxC, LpxD, LpxB, LpxK and KdtA orthologs. Knocking them out shifts the expected lipid A precursors, and the enzymes are targeted to mitochondria [PMID:21709257 "the Lpx and KdtA proteins are expressed and targeted to mitochondria"]. AtLpxA complements an E. coli *lpxA* mutant [PMID:22545860 "A. thaliana lpxA complements an E. coli mutant lacking the chromosomal lpxA"]. A low RAR reflected curation density, not absence. |
| `GO:0001216` | 5 (human ZNF341 IDA, mouse Znf341 IEA, 3 Arabidopsis IDA/IMP) | **Moot.** In 2019 the term was "bacterial-type RNA polymerase transcriptional activator activity, sequence-specific DNA binding"; it is now the general "DNA-binding transcription activator activity". The flag was right against the old label; the current rows are fine. |
| `GO:0021987` cerebral cortex development | 4 chicken (BTBD3 IBA, NTRK2 ISS, two Ensembl IEA) | **Open.** Whether "cerebral cortex" ("the outer layered region of the telencephalon") applies to the avian pallium is a homology question, not a clear error. |
| `GO:0030907` MBF transcription complex | worm cec-10 (Q9N4L7), IBA from PTN000917496 seeded by fission yeast Res2 | **Flag holds (provisionally).** MBF is the fungal G1/S complex; cec-10 is a chromodomain protein. Needs a family-level check of the node. |
| `GO:0010973` positive regulation of division septum assembly | worm npp-20/SEC13 (Q9N4A7), IMP, PMID:12937276 | **Flag likely holds.** The cited paper is an RNAi survey of nucleoporins; division septum assembly is a fungal/bacterial process. This is an experimental row, so per project rules it needs the full text, not a REMOVE from the abstract. |
| `GO:0044548` S100 protein binding | fly CacyBP (Q9W3Y3), InterPro2GO IPR037893 | **Flag holds.** S100 proteins are a vertebrate family; the mapping transfers a vertebrate partner interaction to flies. |
| `GO:0005118` sevenless binding | mouse Gprc5c (Q8K3J9), InterPro2GO IPR002956 | **Open.** Vertebrates have a sevenless ortholog (ROS1), so this is a question about the InterPro2GO mapping, not the taxon. |

### DDL in Arabidopsis

The paper said At3g08840 cannot do peptidoglycan biosynthesis because plant cell
walls are cellulose. That misses the point: the question is the plastid, not the
cell wall. Moss chloroplasts do have a peptidoglycan wall, and moss *ddl*
knockouts give giant chloroplasts that D-Ala-D-Ala rescues
[PMID:27325639 "moss chloroplasts are completely surrounded by peptidoglycan"].
So the PAINT node uniting bacterial and plant Ddl is defensible for land plants
as a group. What makes the Arabidopsis annotation doubtful is lineage-specific
loss: Arabidopsis has no Pbp gene [PMID:16618924 "no Pbp gene was found in A. thaliana"],
and its *ddl* mutants have no plastid phenotype
[PMID:27325639 "no plastid phenotypes were observed in the T-DNA tagged ddl mutant lines of Arabidopsis thaliana"].
Current GOA has dropped the BP IBA but kept the MF IBA `D-alanine-D-alanine
ligase activity`, which is untested for the Arabidopsis protein. This is the
same "inside the clade, lost the function" question IBA_REVIEW asks, and is a
candidate for a gene review.

## The neXtProt claim

The paper says, citing personal communication with Lydie Lane, that neXtProt
"decided to downgrade the status of IBA annotations in the future release of
neXtProt from 'Gold' to 'Silver'". We could not confirm this:

- The neXtProt 2020 update paper (PMID:31724716) does not mention IBA, Gold/Silver
  quality, or GO evidence grading.
- neXtProt has since shut down. Its site now redirects to an archive page saying
  "After 14 years, neXtProt has reached its end of life and no longer provides
  data or services". The last archived release is from September 2023.
- Confirming it would need either a check of the archived neXtProt GO export for
  the quality tier on IBA rows, or an answer from the former neXtProt team.

So it is a plausible second-hand report, with no public record we could find,
about a resource that no longer exists. It should not be cited as evidence that
IBA is low quality.

## What this means for IBA review

- **Taxon-level screens work, but only with a human pass.** The RAR flags that
  held up are the ones where the term needs a structure the lineage lacks
  (nucleus, mitochondrion or fungal vacuole in bacteria; S100 or MBF partners in
  animals). The flag that failed, plant lipid A, is a pathway that seemed absent
  only because it is rarely studied in plants. That is the comparator check
  CLAUDE.md asks for before calling a gap.
- **The mechanism is node depth, not "IBA is unreliable".** Every IBA case here
  traces to a PAINT node placed above a lineage that lacks the function (Udg
  root, DDL, MBF). Those are `TOO_DEEP` / `LINEAGE_OR_TAXON_MISMATCH` in the
  [IBA_REVIEW taxonomy](IBA_REVIEW.md#propagation-taxonomy-and-checklist), and
  are better fixed with a GO taxon constraint or an IRD on the node than per gene.
- **A current RAR screen would be cheap.** The screen needs only GAF counts per
  taxon. Rerunning it on current GOA, restricted to species we review, would
  give [TAXON_PATHWAY_VARIANCE](TAXON_PATHWAY_VARIANCE.md) candidate constraints,
  as long as the comparator check is applied before any proposal.

## Next steps

- [ ] Gene review: Arabidopsis DDL (A0A1I9LPE3), on the MF IBA.
- [ ] Family check of PTN000917496 (MBF / worm cec-10).
- [ ] Read the full text of PMID:12937276 for the npp-20 IMP row.
- [ ] Decide whether chicken `cerebral cortex development` is a homology question to raise with GO.
- [ ] Rerun RAR on current GOA for our reviewed species (script not yet written).
- [ ] Check the archived neXtProt release for how IBA rows were graded.

## Sources

- Paper: [PMID:32470107](https://pubmed.ncbi.nlm.nih.gov/32470107/), doi:10.1093/bioinformatics/btaa548.
- Supplement and authors' code: <https://zhanggroup.org/RAR/> (the "full dataset" `full.zip` link returns 404; `SI.pdf` and `rateratio_test.zip` are available).
