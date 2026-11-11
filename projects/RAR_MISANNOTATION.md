---
title: "Re-examining the RAR misannotation study (Wei et al. 2020)"
maturity: IN_PROGRESS
last_reviewed: 2026-10-18
tags: [EVALUATION]
collections: [HOMOLOGY_PROPAGATION]
species: [ARATH, worm, DROME, mouse, human, CHICK]
autolink_exclude: [ddl]
genes: [At3g08840, KDTA, cec-10, npp-20, CG3226, Gprc5c, BTBD3, LPXA, LPXB, LPXK, LPXD1, LPXD2, LPXC1, LPXC2, LPXC3, LPXC4, LPXC5]
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

## Gene reviews of the surviving cases

One full review per surviving case (2026-10-19). Each one checks the flagged
annotation against the literature and, for IBA rows, the PAINT node.

| Gene | Flagged term | Review action | Paper's flag |
|---|---|---|---|
| ARATH/KDTA | lipid A biosynthetic process (IBA) | ACCEPT, core | **Wrong.** Lipid IVA, KdtA's substrate, accumulates only in *atkdta* mutants; the enzyme is mitochondrial. |
| ARATH/At3g08840 | peptidoglycan biosynthetic process (IBA, now gone); D-Ala-D-Ala ligase activity (IBA) | MF ACCEPT; no BP proposed | **Holds for the process, for plastid reasons.** Catalytic residues are conserved, matching the moss enzyme, so the MF stays (untested). |
| worm/cec-10 | MBF transcription complex (IBA) | REMOVE (with four other MBF-derived IBAs) | **Holds.** cec-10 lacks the KilA-N DNA-binding domain; PTN000917496 is placed too deep over metazoan Swi6-family members. |
| worm/npp-20 | positive regulation of division septum assembly (IMP) | MODIFY → mitotic cytokinesis, non-core | **Holds for the term, not the experiment.** The full text reports that RNAi "blocked cytokinesis"; the curator chose a fungal septum term. |
| DROME/CG3226 | S100 protein binding (InterPro2GO) | REMOVE | **Holds.** No S100 proteins outside chordates; the IPR037893 mapping carries a vertebrate partner to flies. |
| mouse/Gprc5c | sevenless binding (InterPro2GO) | REMOVE (also visual perception from the same entry) | **Holds, for a different reason.** IPR002956 is a BOSS PRINTS signature matching two transmembrane segments; no GPRC5–ROS1 link is known. |
| CHICK/BTBD3 | cerebral cortex development (IBA) | MODIFY → pallium development | **Holds, weakly.** The node is sound; the anatomy term doesn't fit birds. About 1,760 bird annotations use it, constrained only to Bilateria. |

### The Arabidopsis lipid A pathway

Since the lipid A flags were the paper's one clear error, we reviewed the whole
Arabidopsis pathway rather than relying on KDTA alone (2026-10-26). All eleven
enzymes are reviewed here, with the experimental evidence from Li et al. 2011
and Joo et al. 2012 recorded on their rows.

| Gene | Key evidence | Outcome |
|---|---|---|
| ARATH/LPXA | Purified enzyme active in vitro; complements *E. coli lpxA*; mutant has ~21% of wild-type lipid X | Lipid A biosynthetic process added as NEW (IDA), the only term the experiments support that GOA lacked |
| ARATH/LPXC1 to ARATH/LPXC5 | Five tandem copies encoding identical proteins; RNAi of the cluster lowers lipid X; LpxC1.1-GFP is mitochondrial | Same calls on all five; the experiments cannot tell the copies apart |
| ARATH/LPXD2 | Lipid X undetectable in the null | Main LpxD; activity and process accepted as core |
| ARATH/LPXD1 | Lipid X not reduced in the null; R293K and missing acceptor-binding residues | Activity and process left UNDECIDED; only acyltransferase activity accepted |
| ARATH/LPXB | Two nulls accumulate lipid X (42-fold) and UDP-2,3-diacyl-GlcN | Accepted |
| ARATH/LPXK | Three nulls accumulate the disaccharide 1-phosphate | Accepted |
| ARATH/KDTA | Null accumulates lipid IVA | Accepted (see above) |

Across the set, the predicted `chloroplast` (ISM) rows were removed, because
GFP fusions in Li et al. 2011 did not colocalise with chloroplasts. Rows using
the obsolete `GO:2001289 lipid X metabolic process` were moved to `lipid A
biosynthetic process`, except on LPXD1, which has no phenotype.

Taken together, the paper was wrong about one family (plant lipid A). It was right
about five, but for three of those the cause was not the one it suggested (plastid
loss for DDL, a mis-scoped experimental term for npp-20, a bad InterPro signature
for Gprc5c). Only one of the five (cec-10) is the IBA node-depth problem the paper
emphasised. The other is too broad an anatomy term (BTBD3).

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

## RAR rerun on current GOA (2026-11-11)

[rar_rerun.py](RAR_MISANNOTATION/scripts/rar_rerun.py) reruns the screen on current data.
It uses the paper's 20 species and the authors' exact rate-ratio test with Benjamini-Hochberg
correction. The inputs are the GOA proteome files of 2026-11-04 and GO release 2026-07-26.
It counts asserted annotations only (NOT rows excluded).

| | Kingdom level | Vertebrates vs invertebrates |
|---|---|---|
| Terms with a rate ratio | 8,520 | 8,613 |
| Rate ratio < 0.1 | 2,862 (paper, 2019: 2,369) | 577 (paper: 618) |
| Of those, q < 0.05 | 2,615 | 550 |
| Review candidates | 1,241 | 280 |

The flag counts are close to the paper's, so the method reproduces on current data. Two
artefacts inflate the raw counts:

- **ND rows on root terms.** Flagged rows on the three root terms number 14,456, all of them
  ND, and assert no function, so they are dropped. The script records this and the other dropped counts in the
  candidates file.
- **The animal denominator.** It is 351,036 proteins, because the human, mouse and chicken
  proteome files include every unreviewed entry. A term curated only on reviewed animal
  proteins therefore looks rare in animals.

So the committed [candidates](RAR_MISANNOTATION/data/rar_rerun_direct_candidates.yaml) keep only
stray annotations: q < 0.05, not a root term, and at most three proteins in the flagged taxon.
Only 4 candidate terms were also flagged in 2018 or 2019, so nearly all of today's flags are new:
MBF transcription complex, positive regulation of division septum assembly, periplasmic space,
and (vertebrate vs invertebrate) sevenless binding. Three of these already have in-repo answers:
TPV-004, the npp-20 MODIFY, and TPV-008 with CR-0006.

### What is new since 2019

- **Annotations that break an existing GO taxon constraint.** 38 candidate annotations break
  a constraint GO already has, so they need no judgement about rates. Twelve are IBA from GO
  Central, for example:
  - histone deacetylase activity on *B. subtilis* AcuC (`never_in_taxon` Bacteria);
  - nuclear-transcribed mRNA decapping on three bacterial RppH proteins (`only_in_taxon` Eukaryota);
  - centrosome on Arabidopsis and *Selaginella* proteins (`never_in_taxon` Viridiplantae).

  The rest are curated rows from TAIR, MGI, CGD, FlyBase and UniProt. Of the 21 terms
  involved, the first pass finds 14 annotation errors, 5 constraints that look too narrow and
  2 open cases. The too-narrow constraints are:
  - glutamate-gated calcium channel activity, plus the signalling term inferred from it, and
    plasma membrane repair: all Metazoa-only, but plant GLR3.3 and SYT1 do these;
  - cholesterol binding: never in Fungi, but CAP/PRY proteins bind sterols;
  - sperm axoneme assembly: Metazoa-only, but *Selaginella* makes flagellate sperm.
- **TreeGrafter IEA in prokaryotes.** 47 prokaryote-flagged terms on 44 proteins come from
  TreeGrafter, PANTHER's automatic transfer of PAINT annotations to unreviewed proteins. Most are
  eukaryote-only structures and processes on *P. aeruginosa* PA14, *C. difficile* and archaeal
  proteins: microtubule binding, mitotic spindle, nuclear pore, Golgi organization,
  telomerase-dependent telomere maintenance, extracellular matrix. TreeGrafter postdates the
  paper, which saw this pattern only as IBA. Grafting a TrEMBL protein onto a PAINT node
  without a taxon check turns every node placed too deep into many IEA rows.
- **Prokaryote IBA, the paper's Udg pattern.** Eighteen PAINT nodes still give bacteria IBAs
  flagged at the kingdom level. The first pass finds:
  - 6 errors: ubiquitin/proteasome terms on two *B. subtilis* proteins; sterol metabolism on
    YjiC; carotenoid biosynthesis on YisP; a eukaryotic multi-synthetase complex on
    *Mycoplasma* ProS; the AcuC and RppH constraint breaks;
  - 5 that are rare but right: ecotin, PaaK, LigD NHEJ, NhaP2, EnvC;
  - 1 that is right but too general: PdxS, a MODIFY candidate;
  - 6 open cases.

  The false flags make the paper's point again: a low rate shows curation density as often as
  error.

Verdicts are in [rar_rerun_triage.yaml](RAR_MISANNOTATION/data/rar_rerun_triage.yaml). They are
first-pass: they rest on curated UniProt function text, term definitions and constraints, not on
reading each paper. Where a verdict rests on a cached paper or UniProt record, the file quotes it
verbatim, so `just validate-quotes` checks it. Plant-, animal- and fungus-flagged candidates (about 1,040 kingdom-level
terms) are not triaged yet.

### Plant and animal candidates (2026-11-11)

All 958 kingdom-level candidates flagged in plants (604) or animals (354) are triaged in
[rar_rerun_triage_plant_animal.yaml](RAR_MISANNOTATION/data/rar_rerun_triage_plant_animal.yaml).
They were triaged in five groups, by lineage and by evidence type: plant IBA, plant inferred,
plant experimental, animal inferred and animal experimental. A merge step checked that every
term is covered and that every proposed replacement is a live GO term (109 ids); `quote_check`
verifies all 39 quotes.

| Verdict | Entries |
|---|---|
| Annotation wrong | 142 |
| Rare but right (flag fails) | 363 |
| Experimental, deferred to the curator | 379 |
| Right but too general | 36 |
| Constraint looks too narrow | 4 |
| Uncertain | 63 |

Experimental rows are not overruled on first-pass evidence. They are called wrong only when
the term's definition or GO taxon constraint excludes the lineage, which makes the error a term
choice. Otherwise they are deferred to the curator, who read the full text.

Most flags fail. The flag measures curation density as often as error, as in the first round:
- plant metabolic enzymes look rare because bacteria dominate the denominator;
- conserved eukaryotic machinery looks rare in plants because plants are under-curated;
- many animal flags are real enzymology that is rare in animals, such as the nematode
  glyoxylate cycle, phytochelatin synthase and insect trehalose metabolism.

The 142 errors fall into a few kinds:

- **PAINT nodes placed above a lineage that lacks the function (IBA).** Examples:
  - GATOR2 (SEACAT) complex terms on plant SEH1 and SEC13. Neither Arabidopsis nor
    *Selaginella* has a member of the NPRL2, WDR24 or MIOS families.
  - TNF signalling on COMMD proteins, and Wnt signalling on cereblon.
  - Centrosome, polytene chromosome and myosin filament terms on plant proteins.
  - Calcium-dependent protein binding from a node seeded only by vertebrate S100 proteins.
  - In animals, yeast polarisome locations on fly CG6108.
- **Family signatures and rules that over-reach (IEA).** Examples:
  - InterPro2GO: Deltex to Notch signalling and HMMR to hyaluronic acid binding on plant
    proteins; plant tetraspanins to auxin signalling on TSPAN13; yeast Inp1 to peroxisome
    inheritance on worm spartin.
  - UniRules wrong for every protein they match: any RCK_C domain to potassium channel
    regulator activity, and a rule pooling mammalian PEMT with plant PLMT.
  - GO's SL-0038 mapping, which sends every plasmodesmal protein to anchoring junction.
- **Rat (RGD) rows that misread their papers, then copied to mouse by ISO.** Examples:
  - Pon3 to phenylacetate catabolism; the paper measured phenyl acetate esterase activity.
  - Txnrd1 to selenate reductase; the paper is about selenite.
  - Dgat1 to poly-hydroxybutyrate biosynthesis; the paper reports raised beta-hydroxybutyrate.
- **Term-choice slips on curated rows.** Examples:
  - "Cytokine" for "cytokinin" (FLZ17, KNAT3, Psg18).
  - Seed-coat "endothelium" read as vascular endothelium (MYB56).
  - CDPK annotated as protein kinase C (CPK32).
  - MyD88 annotated to the plant term induced systemic resistance.
  - Older TAS/NAS rows that picked the bacterial version of an enzyme class (NNT, PRDX3,
    NUDT2, ATP7A/B).
- **A symbol collision.** Arabidopsis CASP3, a Casparian strip protein, carries an
  amyloid-beta term transferred by ISS from human caspase-3.

The four too-narrow constraints repeat the first round's cases: glutamate-gated calcium channel
and plasma membrane repair (both Metazoa-only, but plant GLR3.3 and SYT1 do these), sperm
axoneme assembly (*Selaginella*), and ionotropic glutamate receptor signalling. One verdict
disagrees with an existing review. Mouse Acadl's carnitine catabolic process row is kept as
non-core in its review, but the term means breaking down carnitine itself, which mammals do
not do. The review should be revisited.

## Next steps

- [x] Gene review: Arabidopsis DDL (At3g08840), on the MF IBA.
- [x] Family check of PTN000917496 (MBF / worm cec-10), from domain and pairwise evidence; the PANTHER tree was not re-inferred.
- [x] Read the full text of PMID:12937276 for the npp-20 IMP row.
- [x] Chicken `cerebral cortex development`: reviewed in BTBD3.
- [x] Write the upstream requests in the repo's structured formats (2026-11-05):
  - Taxon constraints TPV-004 to TPV-007 in [proposed_taxon_constraints.yaml](TAXON_PATHWAY_VARIANCE/proposed_taxon_constraints.yaml): MBF and SBF complexes only in Fungi, S100 protein binding only in Chordata, cerebral cortex development never in Aves. The IRD on PTN000917496 is recorded with TPV-004.
  - InterPro2GO verdicts in [interpro2go.sssom.yaml](INTERPRO/interpro2go.sssom.yaml): narrow IPR037893 → S100 protein binding by taxon, narrow IPR002956 → sevenless binding to the BOSS family, and remove IPR002956 → visual perception (BOSS induces R7 fate but does not perceive light).
  - Curated replacement rules: CR-0005 (IPR037893 AND Chordata → S100 protein binding) and CR-0006 (IPR002956 AND IPR050726 AND Diptera → sevenless binding, sevenless signaling pathway), in `rules/curated/`. CR-0006 first used Arthropoda; the boss review narrowed it to Diptera on 2026-11-07.
  - The COPII coat structural-constituent term is a `proposed_new_terms` entry in the npp-20 review.
  - The LPXD1 UniProt disruption-phenotype error is a `source_defects` entry in the LPXD1 review.
- [x] Taxon constraint TPV-008 (2026-11-07): sevenless binding only in Arthropoda, matching GO's constraint on sevenless signaling pathway. It blocks 195 IPR002956 rows, all 172 vertebrate ones among them. Metazoa, which blocks only the 13 bacterial, fungal and plant rows, is recorded as the fallback in case GO reads the term as covering ROS1.
- [x] The other two IPR037893 mappings (2026-11-07): ubiquitin protein ligase binding is accepted (Skp1 binds the CS domain itself, PMID:15996101). Tubulin binding is removed: it rests on one mouse cell-line study that did not map the binding site (PMID:17916393), which is better curated directly to Cacybp.
- [ ] Submit these to GO, InterPro and UniProt (status is PROPOSED in each file).
- [x] Gene review: Drosophila boss, the positive control for curated rule CR-0006 (2026-11-07). It accepts both rule consequents on experimental evidence. It also narrowed CR-0006 from Arthropoda to Diptera, since experimental evidence for Boss acting as the Sev ligand is restricted to Drosophila, and no Sevenless-binding BOSS ectodomain has been identified outside Diptera (PMID:42043338); 135 of the 211 arthropod matches were non-dipteran.
- [x] Review the rest of the Arabidopsis lipid A pathway ourselves (LPXA, LPXB, LPXK, LPXD1-2, LPXC1-5).
- [x] Rerun RAR on current GOA (2026-11-11): script, candidates and a first-pass triage of the constraint breaks and prokaryote IBA nodes; see [above](#rar-rerun-on-current-goa-2026-11-11).
- [x] Triage the plant- and animal-flagged RAR candidates (958 terms, 2026-11-11); see [above](#plant-and-animal-candidates-2026-11-11).
- [ ] Triage the 81 fungus-flagged RAR candidates and the 280 vertebrate-vs-invertebrate candidates.
- [ ] Turn the family-wide mapping errors into SSSOM rows or curated rules: InterPro2GO for Deltex, HMMR and IPR021006; UniRules UR000414538 (RCK_C) and UR000345849 (PEMT/PLMT); GO's SL-0038 cell-junction mapping.
- [ ] Revisit the mouse Acadl review's carnitine catabolic process row (KEEP_AS_NON_CORE; the triage says the term does not apply).
- [ ] For the 14 annotation errors that break a taxon constraint, find out why GO's constraint check did not filter them; for the 5 questionable constraints, check the cited papers and propose TPV entries.
- [ ] Look at the TreeGrafter prokaryote annotations by PAINT node, since one deep node yields many rows.
- [ ] Check the archived neXtProt release for how IBA rows were graded.

## Sources

- Paper: [PMID:32470107](https://pubmed.ncbi.nlm.nih.gov/32470107/), doi:10.1093/bioinformatics/btaa548.
- Supplement and authors' code: <https://zhanggroup.org/RAR/> (the "full dataset" `full.zip` link returns 404; `SI.pdf` and `rateratio_test.zip` are available).
